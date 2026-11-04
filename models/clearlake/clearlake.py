"""
## GAMSSOURCE: https://www.gams.com/latest/emplib_ml/libhtml/emplib_clearlaksp.html
## LICENSETYPE: Demo
## MODELTYPE: LP
## KEYWORDS: linear programming, stochastic programming, SDDP, reservoir management

ClearLake (CLEARLAKSP,SEQ=72)

Exercise, p. 44:

The Clear Lake Dam controls the water level in Clear Lake, a
well-known resort in Dreamland.  The Dam Commission is trying to
decide how much water to release in each of the next four months.
The Lake is currently 150 mm below flood stage.  The dam is capable
of lowering the water level 200 mm each month, but additional
precipitation and evaporation affect the dam.  The weather near Clear
Lake is highly variable.  The Dam Commission has divided the months
into two two-month blocks of similar weather.  The months within each
block have the same probabilities for weather, which are assumed
independent of one another.  In each month of the first block, they
assign a probability of 1/2 to having a natural 100-mm increase in
water levels and probabilities of 1/4 to having a 50-mm decrease or a
250-mm increase in water levels.  All these figures correspond to
natural changes in water level without dam releases.  In each month
of the second block, they assign a probability of 1/2 to having a
natural 150-mm increase in water levels and probabilities of 1/4 to
having a 50-mm increase or a 350-mm increase in water levels.  If a
flood occurs, then damage is assessed at $10,000 per mm above flood
level.  A water level too low leads to costly importation of water.
These costs are $5000 per mm less than 250 mm below flood stage.  The
commission first considers an overall goal of minimizing expected
costs.  This model only considers this first objective.


Birge, R, and Louveaux, F V, Introduction to Stochastic Programming.
Springer, 1997.
"""

from __future__ import annotations

import math

import numpy as np

from gamspy import Container, Equation, Parameter, Set, Sum, Variable
from gamspy.formulations.sddp import SDDP

L_FLOOD = 250.0
L0 = 100.0
R_MAX = 200.0


def main():
    m = Container()

    # Inflows by month (rows) and scenario (columns).
    scenario_data = np.array(
        [
            [-50.0, 100.0, 250.0],  # jan
            [-50.0, 100.0, 250.0],  # feb
            [50.0, 150.0, 350.0],  # mar
            [50.0, 150.0, 350.0],  # apr
        ]
    )
    probs = [0.25, 0.5, 0.25]

    # SETS
    t = Set(
        m, name="t", records=["jan", "feb", "mar", "apr"], description="Time periods"
    )

    # PARAMETERS
    delta = Parameter(m, name="delta", description="random changes in reservoir level")
    flood_cost = Parameter(
        m,
        name="flood_cost",
        records=10,
        description="K$/mm for amounts over flood level",
    )
    low_cost = Parameter(
        m,
        name="low_cost",
        records=5,
        description="K$/mm for amounts 250mm below flood level",
    )

    # VARIABLES
    obj = Variable(m, name="obj", description="cost")
    lvl = Variable(
        m,
        name="l",
        domain=t,
        type="positive",
        description="level of water in dam end of period",
    )
    r = Variable(
        m, name="r", domain=t, type="positive", description="mm released normally"
    )
    f = Variable(
        m, name="f", domain=t, type="positive", description="mm of floodwater released"
    )
    z = Variable(
        m, name="z", domain=t, type="positive", description="mm of water imported"
    )

    r.up[t] = R_MAX
    # Level zero is 250 mm below flood stage, so L0=100 starts 150 mm below it.
    lvl.up[t] = L_FLOOD

    # INIT SDDP
    sddp = SDDP(m, stage_set=t, n_trials=2, seed=42)
    stage = sddp.active_stage

    # EQUATIONS
    ldef = Equation(m, name="ldef", domain=t)
    defobj = Equation(m, name="defobj")
    ldef[t].where[stage[t]] = (
        lvl[t] - lvl[t.lag(1, "circular")] + r[t] + f[t] - z[t] == delta
    )
    defobj[...] = obj == Sum(stage[t], flood_cost * f[t] + low_cost * z[t])

    # SDDP supplies the initial level for the first month's predecessor.
    sddp.add_state(variable=lvl, initial_state=L0)
    sddp.set_noise(parameter=delta, scenario_data=scenario_data, probabilities=probs)
    sddp.build(stage_cost=obj)

    result = sddp.train(n_iter=20, rel_tol=1e-3, patience=3)
    print(f"Lower bound on expected cost: {result.lower_bound:.4f}")
    assert math.isclose(result.lower_bound, 70.3125, rel_tol=1e-6)

    # Ask what to do in March given an incoming level and an observed inflow.
    decision = sddp.policy(stage="mar", state=150.0, noise=350.0, report=[r, lvl, z, f])
    print("March policy decision:", decision.decisions)

    m.close()


if __name__ == "__main__":
    main()
