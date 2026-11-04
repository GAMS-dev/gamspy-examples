"""
## GAMSSOURCE: https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_sddp.html
## LICENSETYPE: Demo
## MODELTYPE: LP
## DATAFILES: water.xlsx
## KEYWORDS: linear programming, stochastic programming, scenario analysis, GUSS, water resource management


Multi-Stage Stochastic Water Reservoir Model solved with SDDP (SDDP,SEQ=357)

The Stochastic Dual Dynamic Programming (SDDP) algorithm for solving
multi-stochastic linear programs uses, similar to the well known
Benders decomposition, the concept of a future cost function (FCF).
The algorithm works with an underestimate approximation of this FCF by
iteratively adding supporting hyperplanes (Benders cuts) and
therefore improving the approximation.

The original GAMS implementation uses Gather-Update-Solve-Scatter (GUSS)
to make the many related solves efficient. An implementation using
traditional loops can be found at:

https://www.gams.com/modlib/adddocs/sddp_trad.gms

This SDDP algorithm has been implemented using IBM Ilog's Concert
Technology (Version 12.2). The C++ source code is available at:

https://www.gams.com/modlib/adddocs/sddp.cpp

The data and core model has been provided by Vattenfall Energy Trading.


Pereira, M V F, and Pinto, L M V G, Stochastic optimization of a
multireservoir hydroelectric system: A decomposition approach. Water
Resources Research 21, 6 (1985), 779-792.

Pereira, M V F, and Pinto, L M V G, Multi-stage stochastic
optimization applied to energy planning. Mathematical Programming 52
(1991), 359-375.

This GAMSPy example delegates the forward and backward passes, cuts and
future-cost approximation to the SDDP formulation. Each stage contains
one week's 168 hours. Inflow is supplied as a weekly scalar and costs
are expressed internally in million EUR for numerical scaling.
This version applies the inflow scenarios to every week; the original
GAMS model uses the fixed wInflow value for the first week.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from gamspy import Card, Container, Domain, Equation, Parameter, Set, Sum, Variable
from gamspy.formulations.sddp import SDDP

RESMIN = 10.0e6
RESMAX = 106.2e6
RES_W52 = 87.0e6


def main():
    data = Path(__file__).with_name("water.xlsx")
    demand_data = pd.read_excel(data, sheet_name="t_Demand", skiprows=1, header=None)
    exchange_data = pd.read_excel(data, sheet_name="t_Flow", skiprows=1, header=None)
    wCapacity_data = pd.read_excel(
        data, sheet_name="w_Capacity", skiprows=1, header=0, index_col=0
    ).stack()
    wPrices_data = pd.read_excel(
        data, sheet_name="w_Prices", skiprows=1, header=0, index_col=0
    ).stack()
    sw_Inflow = pd.read_excel(
        data, sheet_name="sw_Inflow", skiprows=1, header=0, index_col=0
    ).values

    m = Container()

    # Sets
    w = Set(m, name="w", records=[f"w{k}" for k in range(1, 53)], description="weeks")
    t = Set(
        m,
        name="t",
        records=[f"t{k}" for k in range(1, 8737)],
        description="hours of the year",
    )
    ft = Set(
        m,
        name="ft",
        records=["Hydro", "HardCoal", "Nuclear"],
        description="types of fuel available (plants)",
    )
    h = Set(
        m,
        name="h",
        records=[f"h{k}" for k in range(1, 169)],
        description="hours of one week",
    )

    # Week-to-hour mapping
    w_labels = w.toList()
    t_labels = t.toList()
    hours_per_week = 168
    wt_records = [
        (week, t_labels[pos * hours_per_week + hour])
        for pos, week in enumerate(w_labels)
        for hour in range(hours_per_week)
    ]

    wt = Set(
        m,
        name="wt",
        domain=[w, t],
        records=wt_records,
        description="map weeks and hours",
    )

    # Parameters
    demand = Parameter(
        m, name="demand", domain=t, records=demand_data, description="power demand MW"
    )
    exchange = Parameter(
        m,
        name="exchange",
        domain=t,
        records=exchange_data,
        description="cross border flow MW",
    )
    wCapacity = Parameter(
        m,
        name="wCapacity",
        domain=[w, ft],
        records=wCapacity_data,
        description="capacity of plant MW",
    )
    wPrices = Parameter(
        m,
        name="wPrices",
        domain=[w, "*"],
        records=wPrices_data,
        description="coal and CO2 price EUR per ton",
    )

    resmax = Parameter(m, name="resmax", domain=t, description="max reservoir level MW")
    resmin = Parameter(m, name="resmin", domain=t, description="min reservoir level MW")
    # Reservoir limits are soft; both use the same target at the final hour.
    resmax[t] = RESMAX
    resmax["t8736"] = RES_W52
    resmin[t] = RESMIN
    resmin["t8736"] = RES_W52

    capacity = Parameter(
        m, name="capacity", domain=[t, ft], description="capacity of plant MW"
    )
    gencost = Parameter(
        m, name="gencost", domain=[t, ft], description="generating cost EUR per MW"
    )
    capacity[t, ft] = Sum(wt[w, t], wCapacity[w, ft])
    gencost[t, "Hydro"] = 0
    gencost[t, "Nuclear"] = 15
    gencost[t, "HardCoal"] = Sum(
        wt[w, t], wPrices[w, "HardCoal"] + 2.361 * wPrices[w, "CO2"]
    ) / (6.98 * 0.39)

    inflow = Parameter(
        m,
        name="inflow",
        description="inflows into the reservoir MWh per week (set by SDDP)",
    )

    # Variables
    RES = Variable(
        m,
        name="RES",
        type="positive",
        domain=t,
        description="reservoir energy (level) at end of t MW",
    )
    X = Variable(
        m,
        name="X",
        type="positive",
        domain=[t, ft],
        description="generated power in hour t by plant with fuel type MW",
    )
    GAP = Variable(
        m,
        name="GAP",
        type="positive",
        domain=t,
        description="gap generation in hour t MW",
    )
    SPILL = Variable(
        m, name="SPILL", type="positive", domain=t, description="spillage in hour t MW"
    )
    SLACKUP = Variable(
        m,
        name="SLACKUP",
        type="positive",
        domain=t,
        description="slack variable for the upper reservoir level equation MW",
    )
    SLACKLO = Variable(
        m,
        name="SLACKLO",
        type="positive",
        domain=t,
        description="slack variable for the lower reservoir level equation MW",
    )
    COST = Variable(m, name="COST", description="stage generation cost (million EUR)")

    # Initialize SDDP
    sddp = SDDP(m, stage_set=w, time_set=t, n_trials=5, seed=123)
    ww = sddp.active_stage

    # Equations
    Cont = Equation(
        m, name="Cont", domain=t, description="hydraulic continuity equation"
    )
    DemSat = Equation(m, name="DemSat", domain=t, description="demand satisfaction")
    ResUp = Equation(m, name="ResUp", domain=t, description="maximum reservoir level")
    ResLo = Equation(m, name="ResLo", domain=t, description="minimum reservoir level")
    PlantCap = Equation(
        m,
        name="PlantCap",
        domain=[t, ft],
        description="plant power generation capacity",
    )
    Obj = Equation(m, name="Obj", description="objective function")

    # The active week selects its hourly equations. Weekly inflow is spread
    # evenly over those hours.
    Cont[t].where[Sum(w.where[ww[w]], wt[w, t])] = RES[t] - RES[
        t.lag(1, "circular")
    ] + X[t, "Hydro"] + SPILL[t] == inflow / Card(h)
    DemSat[t].where[Sum(w.where[ww[w]], wt[w, t])] = (
        Sum(ft.where[capacity[t, ft]], X[t, ft]) + GAP[t] >= demand[t] - exchange[t]
    )
    ResUp[t].where[Sum(w.where[ww[w]], wt[w, t])] = -RES[t] + SLACKUP[t] >= -resmax[t]
    ResLo[t].where[Sum(w.where[ww[w]], wt[w, t])] = RES[t] + SLACKLO[t] >= resmin[t]
    PlantCap[t, ft].where[Sum(w.where[ww[w]], wt[w, t]) & capacity[t, ft]] = (
        -X[t, ft] >= -capacity[t, ft]
    )
    # Express all costs in million EUR to improve numerical scaling.
    Obj[...] = (
        COST
        == (
            Sum(
                Domain(w, t, ft).where[ww[w] & wt[w, t] & capacity[t, ft]],
                gencost[t, ft] * X[t, ft],
            )
            + Sum(
                Domain(w, t).where[ww[w] & wt[w, t]],
                1_000 * GAP[t] + 10e6 * (SLACKUP[t] + SLACKLO[t]),
            )
        )
        / 1e6
    )

    # Register the reservoir state and the 12 inflow scenarios per week.
    sddp.add_state(
        variable=RES,
        lower_bound=RESMIN,
        upper_bound=RESMAX,
        initial_state=RES_W52,
    )
    sddp.set_noise(parameter=inflow, scenario_data=sw_Inflow)
    sddp.build(stage_cost=COST)

    result = sddp.train(n_iter=20, rel_tol=1e-6, patience=5)
    print(
        f"Lower bound on expected generation cost: {result.lower_bound * 1e6:,.2f} EUR"
    )
    m.close()


if __name__ == "__main__":
    main()
