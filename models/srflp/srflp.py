"""
## LICENSETYPE: Demo
## MODELTYPE: MIP, LP
## KEYWORDS: mixed integer linear programming, absolute value, facility layout, disjunctive constraints, formulations


Single Row Facility Layout Problem (SRFLP)

Machines of different lengths are placed side by side along a straight
corridor. Material flows between the machines, and the cost of a flow is
proportional to the distance between the centers of the machines. The
problem finds the positions that minimize the total transport cost:

  min sum((i,j), flow(i,j) * |x(i) - x(j)|)

The machines must not overlap, i.e. the distance between two centers must
be at least half of the sum of their lengths:

  |x(i) - x(j)| >= (length(i) + length(j)) / 2

The non-overlap constraint makes the problem non-convex, because it
requires one machine to be either left or right of the other.

The model is organized as follows:
  1) The usual linear formulation of an absolute value only requires the
     distance to be at least the difference and its negation. This works
     in the objective, because the model benefits from small distances,
     but not in the non-overlap constraint, which benefits from large
     distances. The solver places all machines at the same position.

  2) gamspy.formulations.absolute makes the distance equal to the absolute
     value by selecting the sign of the difference with a binary variable.
     The machines then do not overlap.


Simmons, D M, One-Dimensional Space Allocation: An Ordering Algorithm.
Operations Research 17, 5 (1969), 812-826.
"""

from __future__ import annotations

import gamspy.formulations as formulations
import pandas as pd
from gamspy import (
    Alias,
    Container,
    Equation,
    Model,
    Ord,
    Parameter,
    Sense,
    Set,
    Sum,
    Variable,
)


def report(i: Set, x: Variable, length: Parameter) -> pd.DataFrame:
    layout = pd.DataFrame(
        {"center": x.toDense(), "length": length.toDense()}, index=i.toList()
    )
    layout["start"] = layout["center"] - layout["length"] / 2
    layout["end"] = layout["center"] + layout["length"] / 2
    return layout.sort_values("center").round(3)


def overlap(layout: pd.DataFrame) -> float:
    # largest overlap of two neighboring machines
    return (layout["end"].iloc[:-1].values - layout["start"].iloc[1:].values).max()


def main():
    m = Container()

    # Sets
    i = Set(
        m,
        name="i",
        records=["saw", "lathe", "drill", "mill", "grinder", "paint"],
        description="machines",
    )
    j = Alias(m, name="j", alias_with=i)
    ij = Set(m, name="ij", domain=[i, j], description="pairs of machines")
    ij[i, j] = Ord(i) < Ord(j)

    # Parameters
    length = Parameter(
        m,
        name="length",
        domain=i,
        records=[
            ("saw", 3),
            ("lathe", 5),
            ("drill", 2),
            ("mill", 6),
            ("grinder", 4),
            ("paint", 7),
        ],
        description="length of machine i in meters",
    )
    flow = Parameter(
        m,
        name="flow",
        domain=[i, j],
        records=[
            ("saw", "lathe", 10),
            ("saw", "drill", 4),
            ("saw", "mill", 6),
            ("lathe", "drill", 8),
            ("lathe", "grinder", 7),
            ("drill", "mill", 9),
            ("drill", "paint", 2),
            ("mill", "grinder", 5),
            ("mill", "paint", 3),
            ("grinder", "paint", 12),
        ],
        description="transports between machine i and j per day",
    )

    # Variables
    x = Variable(
        m, name="x", domain=i, description="position of the center of machine i"
    )
    x.lo[i] = length[i] / 2
    x.up[i] = Sum(j, length[j]) - length[i] / 2

    delta = Variable(
        m, name="delta", domain=[i, j], description="difference of the centers"
    )
    defdelta = Equation(
        m,
        name="defdelta",
        domain=[i, j],
        description="define the difference of the centers",
    )
    defdelta[ij[i, j]] = delta[i, j] == x[i] - x[j]

    # 1) Linear formulation: dist[i, j] >= abs(x[i] - x[j])
    dist = Variable(
        m, name="dist", domain=[i, j], description="distance of the centers"
    )
    above_plus = Equation(m, name="above_plus", domain=[i, j])
    above_plus[ij[i, j]] = dist[i, j] >= delta[i, j]
    above_minus = Equation(m, name="above_minus", domain=[i, j])
    above_minus[ij[i, j]] = dist[i, j] >= -delta[i, j]
    no_overlap = Equation(
        m, name="no_overlap", domain=[i, j], description="machines do not overlap"
    )
    no_overlap[ij[i, j]] = dist[i, j] >= (length[i] + length[j]) / 2

    linear = Model(
        m,
        name="linear",
        equations=[defdelta, above_plus, above_minus, no_overlap],
        problem="lp",
        sense=Sense.MIN,
        objective=Sum(ij[i, j], (flow[i, j] + flow[j, i]) * dist[i, j]),
    )
    linear.solve()

    layout = report(i, x, length)
    print("Linear formulation")
    print("Objective Function Value: ", round(linear.objective_value, 3))
    print(layout)

    # The distances are not the absolute values anymore, so machines overlap
    if overlap(layout) < 1e-6:
        raise Exception("expected the linear formulation to overlap machines")

    # 2) Exact formulation: dist[i, j] == abs(x[i] - x[j])
    exact_dist, eqs = formulations.absolute(delta[ij])

    exact_no_overlap = Equation(
        m,
        name="exact_no_overlap",
        domain=[i, j],
        description="machines do not overlap",
    )
    exact_no_overlap[ij[i, j]] = exact_dist[i, j] >= (length[i] + length[j]) / 2

    exact = Model(
        m,
        name="exact",
        equations=[defdelta, exact_no_overlap, *eqs],
        problem="mip",
        sense=Sense.MIN,
        objective=Sum(ij[i, j], (flow[i, j] + flow[j, i]) * exact_dist[i, j]),
    )
    exact.solve()

    layout = report(i, x, length)
    print("Exact formulation")
    print("Objective Function Value: ", round(exact.objective_value, 3))
    print(layout)

    # The machines do not overlap
    if overlap(layout) > 1e-6:
        raise Exception("machines overlap")


if __name__ == "__main__":
    main()
