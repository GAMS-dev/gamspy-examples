"""
## GAMSSOURCE: https://www.gams.com/latest/noalib_ml/libhtml/noalib_heatex3.html
## LICENSETYPE: Demo
## MODELTYPE: NLP


Optimal Design of Network of Heat Exchangers in Parallel (with Recirculation) with Two Hot Streams and One Cold Stream

Design of a network of heat exchangers in parallel (with recirculation)
with two hot streams and one cold stream.

Floudas, C.A., Pardalos, P.M., et al. "Handbook of Test Problems in
Local and Global Optimization".
Kluwer Academic Publishers, Dordrecht, 1999.
Section 5.4.3. Test Problem 2, pages 52-54.
"""

from __future__ import annotations

import os

from gamspy import Container, Equation, Model, Parameter, Variable


def main():
    m = Container(
        system_directory=os.getenv("GAMSPY_GAMS_SYSDIR", None),
    )

    # SCALARS #
    Tcin = Parameter(
        m,
        name="Tcin",
        records=150,
        description="inlet temperature of cold stream",
    )
    Tcout = Parameter(
        m,
        name="Tcout",
        records=310,
        description="outlet temperature of cold stream",
    )

    # VARIABLES #
    dT11 = Variable(
        m,
        name="dT11",
        description="temperature difference at hot end of exchanger H1-",
    )
    dT12 = Variable(
        m,
        name="dT12",
        description="temperature difference at cold end of exchanger H1-",
    )
    dT21 = Variable(
        m,
        name="dT21",
        description="temperature difference at hot end of exchanger H2-C",
    )
    dT22 = Variable(
        m,
        name="dT22",
        description="temperature difference at cold end of exchanger H2-C",
    )
    f11 = Variable(m, name="f11")
    f12 = Variable(m, name="f12")
    f13 = Variable(m, name="f13")
    f14 = Variable(m, name="f14")
    f21 = Variable(m, name="f21")
    f22 = Variable(m, name="f22")
    f23 = Variable(m, name="f23")
    f24 = Variable(m, name="f24")
    t1i = Variable(m, name="t1i")
    t2i = Variable(m, name="t2i")
    t1o = Variable(m, name="t1o")
    t2o = Variable(m, name="t2o")

    # EQUATIONS #
    g1 = Equation(m, name="g1", type="regular")
    g2 = Equation(m, name="g2", type="regular")
    g3 = Equation(m, name="g3", type="regular")
    g4 = Equation(m, name="g4", type="regular")
    g5 = Equation(m, name="g5", type="regular")
    g6 = Equation(m, name="g6", type="regular")
    g7 = Equation(m, name="g7", type="regular")
    g8 = Equation(m, name="g8", type="regular")
    g9 = Equation(m, name="g9", type="regular")
    g10 = Equation(m, name="g10", type="regular")
    g11 = Equation(m, name="g11", type="regular")
    g12 = Equation(m, name="g12", type="regular")
    g13 = Equation(m, name="g13", type="regular")

    # Objective function:
    objval = (
        1300
        * (1000 / ((1 / 30) * (dT11 * dT12) + (1 / 6) * (dT11 + dT12))) ** 0.6
        + 1300
        * (600 / ((1 / 30) * (dT21 * dT22) + (1 / 6) * (dT21 + dT22))) ** 0.6
    )

    # Constraints:
    g1[...] = f11 + f21 == 10
    g2[...] = f11 + f23 - f12 == 0
    g3[...] = f21 + f13 - f22 == 0
    g4[...] = f14 + f13 - f12 == 0
    g5[...] = f24 + f23 - f22 == 0
    g6[...] = Tcin * f11 + t2o * f23 - t1i * f12 == 0
    g7[...] = Tcin * f21 + t1o * f13 - t2i * f22 == 0
    g8[...] = f12 * (t1o - t1i) == 1000
    g9[...] = f22 * (t2o - t2i) == 600
    g10[...] = dT11 + t1o == 500
    g11[...] = dT12 + t1i == 250
    g12[...] = dT21 + t2o == 350
    g13[...] = dT22 + t2i == 200

    # Bounds on variables:
    dT11.lo[...] = 10
    dT11.up[...] = 350
    dT12.lo[...] = 10
    dT12.up[...] = 350
    dT21.lo[...] = 10
    dT21.up[...] = 200
    dT22.lo[...] = 10
    dT22.up[...] = 200
    f11.lo[...] = 0
    f11.up[...] = 10
    f12.lo[...] = 0
    f12.up[...] = 10
    f13.lo[...] = 0
    f13.up[...] = 10
    f14.lo[...] = 0
    f14.up[...] = 10
    f21.lo[...] = 0
    f21.up[...] = 10
    f22.lo[...] = 0
    f22.up[...] = 10
    f23.lo[...] = 0
    f23.up[...] = 10
    f24.lo[...] = 0
    f24.up[...] = 10
    t1i.lo[...] = 150
    t1i.up[...] = Tcout
    t1o.lo[...] = 150
    t1o.up[...] = Tcout
    t2i.lo[...] = 150
    t2i.up[...] = Tcout
    t2o.lo[...] = 150
    t2o.up[...] = Tcout

    # Initial point:
    dT11.l[...] = 200
    dT12.l[...] = 50
    dT21.l[...] = 150
    dT22.l[...] = 50
    f11.l[...] = 10
    f12.l[...] = 10
    f13.l[...] = 10
    f14.l[...] = 10
    f21.l[...] = 10
    f22.l[...] = 10
    f23.l[...] = 10
    f24.l[...] = 10
    t1i.l[...] = 200
    t1o.l[...] = 100
    t2i.l[...] = 300
    t2o.l[...] = 200

    HeatEx3 = Model(
        m,
        name="HeatEx3",
        equations=m.getEquations(),
        problem="nlp",
        sense="MIN",
        objective=objval,
    )

    HeatEx3.solve()
    print("Objective Function Variable:  ", HeatEx3.objective_value)

    import math

    assert math.isclose(HeatEx3.objective_value, 5937.437344646649)

    # End HeatEx3


if __name__ == "__main__":
    main()