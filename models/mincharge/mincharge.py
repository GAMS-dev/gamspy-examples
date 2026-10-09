"""
## LICENSETYPE: Demo
## MODELTYPE: MIP, LP
## KEYWORDS: mixed integer linear programming, maximum, minimum charge, capacity allocation, formulations


Capacity Allocation under Minimum Charge Contracts (MINCHARGE)

A supplier with limited capacity serves customers under contracts with a
minimum charge, as it is common for utilities, telecommunication or cloud
services. Each customer pays for the delivered quantity, but at least the
minimum charge:

  bill(c) = max(price(c) * deliver(c), mincharge(c))

The supplier allocates its capacity to maximize the total bill minus the
production cost. Delivering less than mincharge(c) / price(c) to a customer
does not increase the bill, so the supplier either serves a customer well
or not at all. This makes the problem non-convex.

The model is organized as follows:
  1) The usual linear formulation of a maximum only requires the bill to
     be at least each operand. This only works if the model benefits from
     a small maximum. Here, the supplier benefits from a large bill and
     charges every customer the upper bound of the bill without
     delivering anything.

  2) gamspy.formulations.maximum makes the bill equal to the maximum by
     selecting one operand with a binary variable. The supplier then
     only bills for what it delivers.
"""

from __future__ import annotations

import gamspy.formulations as formulations
import pandas as pd
from gamspy import (
    Container,
    Equation,
    Model,
    Parameter,
    Sense,
    Set,
    Sum,
    Variable,
)


def report(c: Set, deliver: Variable, bill: Variable) -> pd.DataFrame:
    return pd.DataFrame(
        {"deliver": deliver.toDense(), "bill": bill.toDense()}, index=c.toList()
    )


def main():
    m = Container()

    # Sets
    c = Set(
        m,
        name="c",
        records=["hospital", "factory", "school", "office", "mall"],
        description="customers",
    )

    # Parameters
    price = Parameter(
        m,
        name="price",
        domain=c,
        records=[
            ("hospital", 12),
            ("factory", 9),
            ("school", 10),
            ("office", 11),
            ("mall", 8),
        ],
        description="price per delivered unit",
    )
    mincharge = Parameter(
        m,
        name="mincharge",
        domain=c,
        records=[
            ("hospital", 900),
            ("factory", 1500),
            ("school", 400),
            ("office", 1000),
            ("mall", 1200),
        ],
        description="minimum charge per period",
    )
    demand = Parameter(
        m,
        name="demand",
        domain=c,
        records=[
            ("hospital", 120),
            ("factory", 250),
            ("school", 60),
            ("office", 140),
            ("mall", 200),
        ],
        description="maximum quantity the customer takes",
    )
    capacity = Parameter(
        m, name="capacity", records=400, description="production capacity"
    )
    cost = Parameter(m, name="cost", records=2, description="production cost per unit")

    # Variables
    deliver = Variable(
        m,
        name="deliver",
        type="positive",
        domain=c,
        description="delivered quantity",
    )
    deliver.up[c] = demand[c]

    # Equations
    produce = Equation(m, name="produce", description="observe the capacity")
    produce[...] = Sum(c, deliver[c]) <= capacity

    # 1) Linear formulation: bill[c] >= max(price[c] * deliver[c], mincharge[c])
    bill = Variable(m, name="bill", domain=c, description="bill of the customer")
    bill.up[c] = price[c] * demand[c]

    above_usage = Equation(
        m,
        name="above_usage",
        domain=c,
        description="bill is at least the delivered quantity",
    )
    above_usage[c] = bill[c] >= price[c] * deliver[c]
    above_minimum = Equation(
        m,
        name="above_minimum",
        domain=c,
        description="bill is at least the minimum charge",
    )
    above_minimum[c] = bill[c] >= mincharge[c]

    linear = Model(
        m,
        name="linear",
        equations=[produce, above_usage, above_minimum],
        problem="lp",
        sense=Sense.MAX,
        objective=Sum(c, bill[c]) - cost * Sum(c, deliver[c]),
    )
    linear.solve()

    print("Linear formulation")
    print("Objective Function Value: ", round(linear.objective_value, 3))
    print(report(c, deliver, bill))

    # The bill is not the maximum anymore, e.g. customers pay their full
    # demand without receiving anything
    overbilled = (
        bill.toDense()
        - (price.toDense() * deliver.toDense()).clip(min=mincharge.toDense())
    ).max()
    if overbilled < 1e-6:
        raise Exception("expected the linear formulation to overbill")

    # 2) Exact formulation: bill[c] == max(price[c] * deliver[c], mincharge[c])
    exact_bill, eqs = formulations.maximum(price[c] * deliver[c], mincharge[c])

    exact = Model(
        m,
        name="exact",
        equations=[produce, *eqs],
        problem="mip",
        sense=Sense.MAX,
        objective=Sum(c, exact_bill[c]) - cost * Sum(c, deliver[c]),
    )
    exact.solve()

    print("Exact formulation")
    print("Objective Function Value: ", round(exact.objective_value, 3))
    print(report(c, deliver, exact_bill))

    # The bill equals the maximum for every customer
    expected = (price.toDense() * deliver.toDense()).clip(min=mincharge.toDense())
    if abs(exact_bill.toDense() - expected).max() > 1e-6:
        raise Exception("bill does not equal the maximum")


if __name__ == "__main__":
    main()
