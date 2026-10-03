#!/usr/bin/env python3
"""Check L015's Boolean case inference, not its supplied mathematical premises.

For each listed tuple use E_i for tuple equality and H_i for the second
predicate after its own challenge substitution. The checked premises are:
  t -> OR E_i;  (not t) OR H_i;  E_i -> (H_i -> not t).
The written proof handles arbitrary list length; this is a finite polarity check.
"""

from itertools import product


def main():
    checked_total = 0
    for count in range(6):
        checked = 0
        models = 0
        for values in product((False, True), repeat=1 + 2 * count):
            t = values[0]
            equalities = values[1 : 1 + count]
            predicates = values[1 + count :]
            cover = (not t) or any(equalities)
            strategies = all((not t) or h for h in predicates)
            reductions = all(
                (not e) or (not h) or (not t)
                for e, h in zip(equalities, predicates)
            )
            checked += 1
            if cover and strategies and reductions:
                models += 1
                if t:
                    raise AssertionError((count, values))
        checked_total += checked
        print(f"cases={count}: {checked} valuations, {models} premise models, no violation")

    # Removing coverage leaves an invalid inference even if each listed case
    # has a challenge. This valuation is a check of the Boolean skeleton only.
    t = True
    equalities = (False, False)
    predicates = (True, True)
    strategies = all((not t) or h for h in predicates)
    reductions = all(
        (not e) or (not h) or (not t)
        for e, h in zip(equalities, predicates)
    )
    assert strategies and reductions and t
    assert not ((not t) or any(equalities))
    print("without coverage: t=1, E=(0,0), H=(1,1) satisfies the other premises")
    print(f"PASS: {checked_total} valuations; finite check only, no EF-bound verification")


if __name__ == "__main__":
    main()
