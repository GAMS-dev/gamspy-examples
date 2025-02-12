"""
## GAMSSOURCE: https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_cpack.html
## LICENSETYPE: Demo
## MODELTYPE: QCP
## KEYWORDS: quadratic constraint programming, circle packing problem, mathematics


Packing identical size circles in the unit circle (CPACK)

Given the unit circle (of radius 1), find a set of identical
size circles with an optimized (maximal) radius r so that all
such circles are contained by the unit circle, in a non-overlapping
arrangement.

A test example from  the LGO library


Pinter, J D, Nonlinear optimization with GAMS/LGO.
Journal of Global Optimization 38 (2007), 79-101.
"""

from __future__ import annotations

import math
import sys

from gamspy import (
    Alias,
    Container,
    Equation,
    Model,
    Options,
    Ord,
    Problem,
    Sense,
    Set,
    Variable,
)
from gamspy.math import sqr


def main():
    # take number of circles as first argument
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print("Number of circles =", k)

    c = Container()

    # Set
    i = Set(
        c, name="i", description="circles", records=[str(i) for i in range(k)]
    )
    j = Alias(c, name="j", alias_with=i)
    ij = Set(c, name="ij", domain=[i, j])
    ij[i, j].where[Ord(i) < Ord(j)] = True

    # Variables
    r = Variable(c, name="r", description="radius of circles")
    x = Variable(c, name="x", domain=i, description="abscissa of circle")
    y = Variable(c, name="y", domain=i, description="ordinate of circle")

    # Equations
    circumscribe = Equation(
        c,
        name="circumscribe",
        domain=i,
        description="enforce circle is enclosed in unit circle",
    )
    circumscribe[i] = sqr(1 - r) >= sqr(x[i]) + sqr(y[i])

    nonoverlap = Equation(
        c,
        name="nonoverlap",
        domain=[i, j],
        description="enforce that circles do not overlap",
    )
    nonoverlap[ij[i, j]] = sqr(x[i] - x[j]) + sqr(y[i] - y[j]) >= 4 * sqr(r)

    x.lo[i] = -1
    x.up[i] = 1
    y.lo[i] = -1
    y.up[i] = 1

    x.l[i] = -0.2 + Ord(i) * 0.1
    y.l[i] = -0.2 + Ord(i) * 0.1

    r.lo = 0.05
    r.up = 0.4

    m = Model(
        c,
        name="cpack",
        equations=c.getEquations(),
        problem=Problem.QCP,
        sense=Sense.MAX,
        objective=r,
    )

    # solve with a good global solver
    print("Starting solve, be patient (log only shown afterwards)...")
    m.solve(solver="scip", options=Options(relative_optimality_gap=0.01))

    print(f"{m.objective_value=}")
    assert math.isclose(m.objective_value, 0.3701919131257)

    rval = r.records.loc[0, "level"]
    print("Maximized radius:", rval)

    # draw solution
    width = 100
    height = int(width / 2)
    picture = bytearray(b" " * (width * height))

    # enclosing circle at origin of radius 1
    for v in range(1000):
        phi = 2.0 * math.pi * v / 1000.0
        # shift coordinates by 1.1 and scale down by 2.2
        xcoord = (math.cos(phi) + 1.1) / 2.2 * width
        ycoord = (math.sin(phi) + 1.1) / 2.2 * height
        pos = int(xcoord) + int(ycoord) * width
        if pos < len(picture):
            picture[int(xcoord) + int(ycoord) * width] = 42

    # circles that were packed
    for circle in range(k):
        xl = x.records.loc[circle, "lower"]
        yl = y.records.loc[circle, "lower"]
        # print('circle at', xl, yl, 'radius', rval)
        for v in range(1000):
            phi = 2.0 * math.pi * v / 1000.0
            xcoord = (xl + rval * math.cos(phi) + 1.1) / 2.2 * width
            ycoord = (yl + rval * math.sin(phi) + 1.1) / 2.2 * height
            pos = int(xcoord) + int(ycoord) * width
            if pos < len(picture):
                picture[pos] = 97 + circle

    # linebreaks
    for v in range(height):
        picture[v * width] = 10

    # print(picture.decode())


if __name__ == "__main__":
    main()
