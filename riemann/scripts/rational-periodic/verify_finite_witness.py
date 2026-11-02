#!/usr/bin/env python3
"""Exact finite arithmetic for L590; analytic chain rule remains in its proof."""

from fractions import Fraction as F
import json
from pathlib import Path


def rational(value):
    return str(value)


def dr(q, k):
    # x^2=1, y^2=q, z=k*x; independent of the signs of x and y.
    return (q * (1 + 3 * q) + k * (1 - q)) / (1 + q) ** 2


def finite_table(q_law, k_law):
    rows = []
    totals = {name: F(0) for name in ("mass", "q", "k", "k2", "DR", "Q")}
    for q, pq in q_law:
        for k, pk in k_law:
            p = pq * pk
            vals = {"mass": F(1), "q": q, "k": k, "k2": k * k,
                    "DR": dr(q, k), "Q": max(F(0), k - q)}
            rows.append({"q": rational(q), "k": rational(k),
                         "probability": rational(p),
                         "DR": rational(vals["DR"]), "Q": rational(vals["Q"])})
            for name, value in vals.items():
                totals[name] += p * value
    return rows, totals


def main():
    k_law = [(F(1, 12), F(1, 6)), (F(-7, 60), F(5, 6))]
    old_q = [(F(0), F(1, 2)), (F(1, 6), F(1, 2))]
    new_q = [(F(0), F(625, 672)), (F(1), F(38, 672)), (F(2), F(9, 672))]
    old_rows, old = finite_table(old_q, k_law)
    new_rows, new = finite_table(new_q, k_law)
    threshold = F(1, 288)
    bound = F(625, 48384)
    margin = bound - threshold
    failures = []

    def check(name, actual, expected):
        if actual != expected:
            failures.append({"check": name, "actual": rational(actual),
                             "required": rational(expected)})

    for label, values in (("old", old), ("new", new)):
        for name, expected in (("mass", F(1)), ("q", F(1, 12)),
                               ("k", F(-1, 12)), ("k2", F(1, 80))):
            check(label + "_" + name, values[name], expected)
    check("old_DR", old["DR"], F(29, 1176))
    check("old_Q", old["Q"], F(1, 144))
    check("new_DR", new["DR"], F(0))
    check("new_Q", new["Q"], bound)
    check("margin", margin, F(457, 48384))
    if not bound > threshold:
        failures.append({"check": "strict_threshold", "actual": rational(bound),
                         "required": "> " + rational(threshold)})

    # The centered sign variables make xy=yz=0. These are all six
    # unordered entries of the first block, not just its diagonal.
    k0 = [[F(1), F(0), new["k"]],
          [F(0), new["q"], F(0)],
          [new["k"], F(0), new["k2"]]]
    expected_k0 = [[F(1), F(0), F(-1, 12)],
                   [F(0), F(1, 12), F(0)],
                   [F(-1, 12), F(0), F(1, 80)]]
    for i in range(3):
        for j in range(3):
            check(f"K0_{i}_{j}", k0[i][j], expected_k0[i][j])

    conditionals = []
    for q, pq in new_q:
        conditional = sum((pk * dr(q, k) for k, pk in k_law), F(0))
        conditionals.append({"q": rational(q), "probability": rational(pq),
                             "conditional_mean_DR": rational(conditional)})
    certificate = {
        "scope": "Complete reduced finite tables; signs are proved irrelevant in L590.",
        "old_law": {"rows": old_rows, "totals": {k: rational(v) for k, v in old.items()}},
        "new_law": {"rows": new_rows, "totals": {k: rational(v) for k, v in new.items()},
                    "conditionals": conditionals,
                    "K0": [[rational(v) for v in row] for row in k0]},
        "actual_bound": rational(bound), "required_strict_upper_cost": rational(threshold),
        "margin_above_threshold": rational(margin),
        "analytic_obligations": [
            "C1 extension and growth at the origin",
            "Periodic chain rule and zero endpoint flux for every P>0 and lag one",
            "Full six-coordinate covariance by the symbolic Schur extension",
            "All quadratic derivatives cancel by L589",
            "Both global branches imply the clipped inequality at every atom"
        ],
        "failures": failures,
        "result": "PASS" if not failures else "FAIL",
    }
    path = Path(__file__).with_name("finite-witness-certificate.json")
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print("Finite arithmetic:", certificate["result"])
    print("Old E[DR] =", old["DR"], "; new E[DR] =", new["DR"])
    print("Actual lower bound =", bound, "; required cost <", threshold)
    print("Margin above threshold =", margin)
    print("Failures:", len(failures))
    print("Certificate:", path.relative_to(Path.cwd()))
    raise SystemExit(bool(failures))


if __name__ == "__main__":
    main()
