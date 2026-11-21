#!/usr/bin/env python3
"""Independent L837 arithmetic audit in Q(u), u^2=-3.

Uses characteristic derivatives/Vandermonde squares for the cross
denominators and integer Bareiss elimination for orientation checks.
Source applicability and the all-rank inequalities are checked in L837.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json


def z(a=0, b=0):
    return F(a), F(b)


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def scale(x, q):
    return x[0]*q, x[1]*q


def mul(x, y):
    return x[0]*y[0]-3*x[1]*y[1], x[0]*y[1]+x[1]*y[0]


def norm(x):
    return x[0]**2+3*x[1]**2


def div(x, y):
    return scale(mul(x, (y[0], -y[1])), 1/norm(y))


def power(x, n):
    out = z(1)
    for _ in range(n):
        out = mul(out, x)
    return out


def product(values):
    out = z(1)
    for value in values:
        out = mul(out, value)
    return out


def data(x):
    return {"u_coordinates": [str(v) for v in x], "norm_squared": str(norm(x))}


def read_w(d):
    return z(F(d["a"])+F(d["b"])/2, F(d["b"])/2)


def abs_w(x):
    return abs(x[0]-x[1])+abs(2*x[1])


def bareiss(a):
    a = [row[:] for row in a]
    previous, sign = 1, 1
    for k in range(len(a)-1):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                numerator = p*a[i][j]-a[i][k]*a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator//previous
            a[i][k] = 0
        previous = p
    return sign*a[-1][-1]


original_path = Path(__file__).with_name("adjacent-degree-five-exact.json")
original = json.loads(original_path.read_text())
failures, checks = [], []


def check(name, actual, required):
    ok = actual == required
    checks.append({"name": name, "actual": str(actual),
                   "required": str(required), "passed": ok})
    if not ok:
        failures.append(name)


labels = ["4", "3", "2", "w", "wbar"]
xs = [z(4), z(3), z(2), z(F(1, 2), F(1, 2)), z(F(1, 2), F(-1, 2))]
# Multiply the rational real factors, independently of the original root loop.
coefficients = [1]
for factor in ([1, 4], [1, 3], [1, 2], [1, 1, 1]):
    out = [0]*(len(coefficients)+len(factor)-1)
    for i, a in enumerate(coefficients):
        for j, b in enumerate(factor):
            out[i+j] += a*b
    coefficients = out
check("all polynomial coefficients", original["coefficients"], list(map(str, coefficients)))


def evaluate(cs, x):
    out = z()
    for c in cs:
        out = add(mul(out, x), z(c))
    return out


characteristic = [(-1)**j*a for j, a in enumerate(coefficients)]
derivative = [(5-j)*characteristic[j] for j in range(5)]
for label, x in zip(labels, xs):
    check("variable "+label, read_w(original["variables"][label]), x)
    check("characteristic root "+label, evaluate(characteristic, x), z())
for entry in original["pairwise_differences"]:
    i, j = labels.index(entry["i"]), labels.index(entry["j"])
    difference = add(xs[i], scale(xs[j], -1))
    check("difference "+entry["i"]+"/"+entry["j"], read_w(entry["difference"]), difference)
    check("difference norm "+entry["i"]+"/"+entry["j"], F(entry["difference"]["norm_squared"]), norm(difference))
    check("distinct "+entry["i"]+"/"+entry["j"], norm(difference) > 0, True)

terms, term_records = {}, []
for c in (3, 4):
    terms[c] = []
    subsets = list(combinations(range(5), c))
    check("complete subset list shift"+str(c),
          [t["subset"] for t in original["terms"][str(c)]],
          [[labels[i] for i in subset] for subset in subsets])
    for subset, expected in zip(subsets, original["terms"][str(c)]):
        base = product(xs[i] for i in subset)
        vandermonde = product(add(xs[i], scale(xs[j], -1))
                              for i, j in combinations(subset, 2))
        # Product chi'(x_i) includes every cross difference and every
        # internal unordered pair twice with opposite signs.
        cross = scale(div(product(evaluate(derivative, xs[i]) for i in subset),
                          power(vandermonde, 2)), (-1)**(c*(c-1)//2))
        coefficient = div(power(base, 5-c), cross)
        name = ",".join(labels[i] for i in subset)
        for field, value in (("base", base), ("cross_denominator", cross),
                             ("coefficient", coefficient)):
            check(name+"/"+field, read_w(expected[field]), value)
            check(name+"/"+field+"/norm", F(expected[field]["norm_squared"]), norm(value))
            check(name+"/"+field+"/upper", F(expected[field]["absolute_upper"]), abs_w(value))
        conjugate_subset = tuple(sorted({3: 4, 4: 3}.get(i, i) for i in subset))
        partner = next(t for t in original["terms"][str(c)]
                       if t["subset"] == [labels[i] for i in conjugate_subset])
        check(name+"/conjugation", read_w(partner["coefficient"]),
              (coefficient[0], -coefficient[1]))
        terms[c].append((subset, base, coefficient))
        term_records.append({"shift": c, "subset": expected["subset"],
                             "base": data(base), "cross_denominator": data(cross),
                             "coefficient": data(coefficient)})

rest3, rest4 = terms[3][1:], terms[4][2:]
for c, rest in ((3, rest3), (4, rest4)):
    check("all remainder base norms shift"+str(c), all(norm(b) <= 144 for s, b, t in rest), True)
bound3 = sum(abs_w(t) for s, b, t in rest3)
bound4 = sum(abs_w(t) for s, b, t in rest4)
lead3, lead4 = terms[3][0][2], terms[4][0][2]
phases = [2*mul(lead4, power(xs[3], j))[0] for j in range(6)]
check("period six", power(xs[3], 6), z(1))
check("all six leading phases", list(map(str, phases)), original["proof_bounds"]["shift4_period6_normalized_leading"])
margin3, margin4 = lead3[0]-bound3/2**16, -phases[5]-bound4/2**16
bounds = {"shift3_remainder_coefficient_sum_upper": bound3,
          "shift4_remainder_coefficient_sum_upper": bound4,
          "shift3_normalized_error_at_onset": bound3/2**16,
          "shift4_normalized_error_at_onset": bound4/2**16,
          "shift3_actual_margin": margin3,
          "shift4_actual_negative_margin": margin4}
for key, value in bounds.items():
    check(key, F(original["proof_bounds"][key]), value)
check("strict all-rank shift3 margin at onset16", margin3 > 0, True)
check("strict residue5 margin at onset16", margin4 > 0, True)

replays = []
for c in (3, 4):
    for r in range(1, 18):
        matrix = [[coefficients[c+j-i] if 0 <= c+j-i <= 5 else 0
                   for j in range(r)] for i in range(r)]
        direct = bareiss(matrix)
        formula = z()
        for subset, base, coefficient in terms[c]:
            formula = add(formula, mul(coefficient, power(base, r)))
        check(f"Bareiss/formula shift{c} rank{r}", formula, z(direct))
        replays.append({"shift": c, "rank": r, "determinant": str(direct),
                        "formula": data(formula)})

output = Path(__file__).with_suffix(".json")
certificate = {"method": "Q(u), u^2=-3; derivative/Vandermonde denominators; integer Bareiss",
               "original_certificate": str(original_path.name), "coefficients": coefficients,
               "terms": term_records, "checks": checks, "replays": replays,
               "bounds": {k: str(v) for k, v in bounds.items()},
               "required": "both margins >0; every exact identity holds",
               "failures": failures, "passed": not failures}
output.write_text(json.dumps(certificate, indent=2)+"\n")
print("Independent terms:", len(term_records), "; Bareiss replays:", len(replays))
print("Shift3 margin:", margin3, "; shift4 residue5 margin:", margin4, "; required both >0")
print("All exact checks:", len(checks), "; failures:", failures)
print("Certificate:", output)
raise SystemExit(bool(failures))
