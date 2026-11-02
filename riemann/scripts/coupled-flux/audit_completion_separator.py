"""Independent exact L593 audit: angular Fourier coefficients and trig primitives.

Run: python3 scripts/coupled-flux/audit_completion_separator.py
No imports from the construction script; only the standard library is used.
The analytic derivation and scope are in L593 Section 5.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json


# Rational Laurent polynomials in t=exp(i theta).
def plus(*terms):
    out = {}
    for poly in terms:
        for n, a in poly.items():
            out[n] = out.get(n, Q(0)) + a
    return {n: a for n, a in out.items() if a}


def times(a, b):
    out = {}
    for n, x in a.items():
        for m, y in b.items():
            out[n + m] = out.get(n + m, Q(0)) + x * y
    return {n: a for n, a in out.items() if a}


def scaled(poly, a):
    return {n: a * x for n, x in poly.items() if a * x}


def constant_product(a, b):
    return sum((x * b.get(-n, Q(0)) for n, x in a.items()), Q(0))


def cosine(n):
    return {n: Q(1, 2), -n: Q(1, 2)}


def imaginary_sine(n):
    # This is i sin(n theta); sin(n theta)=-i*imaginary_sine(n).
    return {n: Q(1, 2), -n: Q(-1, 2)}


c, s, c3, s3 = cosine(1), imaginary_sine(1), cosine(3), imaginary_sine(3)
cc, ss, cs = times(c, c), times(s, s), times(c, s)
checks = {}


def inner(f, g):
    # f=sqrt(2)*p+i*sqrt(6)*q, with p reciprocal and q anti-reciprocal.
    p, q = f
    r, u = g
    assert constant_product(p, u) + constant_product(q, r) == 0
    return 2 * constant_product(p, r) - 6 * constant_product(q, u)


def matrix_inner(left, right):
    return [[inner(a, b) for b in right] for a in left]


def product(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def trans(a):
    return [list(col) for col in zip(*a)]


def difference(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


K0 = [[Q(1), Q(0), Q(-1, 12)], [Q(0), Q(1, 12), Q(0)],
      [Q(-1, 12), Q(0), Q(1, 80)]]
# Solve K0 X=I by independent exact Gauss-Jordan elimination.
aug = [row[:] + [Q(int(i == j)) for j in range(3)] for i, row in enumerate(K0)]
for i in range(3):
    pivot = next(j for j in range(i, 3) if aug[j][i])
    aug[i], aug[pivot] = aug[pivot], aug[i]
    d = aug[i][i]
    aug[i] = [x / d for x in aug[i]]
    for j in range(3):
        if j != i:
            d = aug[j][i]
            aug[j] = [x - d * y for x, y in zip(aug[j], aug[i])]
Kinv = [row[3:] for row in aug]

cases = []
for weight, k in [(Q(1, 6), Q(1, 12)), (Q(5, 6), Q(-7, 60))]:
    # Derive the directional derivatives from polar dynamics, not from
    # the construction's restricted Cartesian derivative polynomials.
    a_cs = scaled(cs, 1 + 12 * k)
    b = plus(scaled(cc, 12 * k), ss)
    da = plus(scaled(times(a_cs, c3), Q(-1, 6)),
              scaled(times(b, s3), Q(1, 2)))  # DA=i*sqrt(6)*da
    db = plus(scaled(times(a_cs, s3), Q(-1, 12)),
              scaled(times(b, c3), Q(1, 4)))  # DB=sqrt(2)*db
    h = [(scaled(db, 2), da),
         (plus(c3, scaled(db, Q(-5, 8))),
          plus(scaled(s3, Q(-1, 3)), scaled(da, Q(-1, 2)))),
         (scaled(c3, Q(-1, 2)), scaled(s3, Q(5, 48)))]
    b0 = [(c, {}), ({}, scaled(s, Q(-1, 6))), (scaled(c, k), {})]
    for f in h + b0:
        p, q = f
        assert all(p.get(-n, Q(0)) == x for n, x in p.items())
        assert all(q.get(-n, Q(0)) == -x for n, x in q.items())
    cases.append({"weight": weight, "k": k, "h_fourier": h,
                  "b0_fourier": b0, "J": matrix_inner(h, b0),
                  "E_hh": matrix_inner(h, h), "K0": matrix_inner(b0, b0)})


def averaged(name):
    return [[sum((case["weight"] * case[name][i][j] for case in cases), Q(0))
             for j in range(3)] for i in range(3)]


J, Eh = averaged("J"), averaged("E_hh")
L = product(J, Kinv)
C = difference(Eh, product(L, trans(J)))
for case in cases:
    hp = []
    for i, (p, q) in enumerate(case["h_fourier"]):
        hp.append((plus(p, *[scaled(case["b0_fourier"][j][0], -L[i][j]) for j in range(3)]),
                   plus(q, *[scaled(case["b0_fourier"][j][1], -L[i][j]) for j in range(3)])))
    case["residual_fourier"] = hp
    case["residual_C"] = matrix_inner(hp, hp)
    case["residual_b0"] = matrix_inner(hp, case["b0_fourier"])
checks["full_marginal_K0"] = averaged("K0") == K0
checks["full_residual_covariance"] = averaged("residual_C") == C
checks["all_nine_orthogonality_entries"] = averaged("residual_b0") == [[Q(0)] * 3 for _ in range(3)]

# Intervals as endpoint tuples. The trig bounds use alternating series,
# independently of the original integrated exponential-Taylor intervals.
def point(x):
    return (Q(x), Q(x))


def interval_sum(*args):
    return (sum((a[0] for a in args), Q(0)), sum((a[1] for a in args), Q(0)))


def interval_product(a, b):
    candidates = [x * y for x in a for y in b]
    return (min(candidates), max(candidates))


def interval_scale(a, s):
    return interval_product(a, point(s))


def trig_interval(offset, N=16):
    terms = [Q((-1) ** n, 2 ** (2 * n + offset) * factorial(2 * n + offset))
             for n in range(N + 2)]
    total = sum(terms[:-1], Q(0))
    return tuple(sorted((total, total + terms[-1])))


sin_half, cos_half = trig_interval(1), trig_interval(0)
C0 = interval_scale(sin_half, 2)
S1 = interval_sum(interval_scale(sin_half, 2), interval_scale(cos_half, -1))
C2 = interval_sum(interval_scale(cos_half, 2), interval_scale(sin_half, Q(-7, 2)))
S3 = interval_sum(interval_scale(cos_half, Q(23, 4)), interval_scale(sin_half, Q(-21, 2)))
C4 = interval_sum(interval_scale(sin_half, Q(337, 8)), interval_scale(cos_half, -23))
D = [[C0, interval_scale(S1, -1), interval_scale(C2, -1)],
     [S1, C2, interval_scale(S3, -1)],
     [interval_scale(C2, -1), S3, C4]]
T = [[interval_sum(point(K0[i][j]),
                  *[interval_scale(interval_product(D[a][i], D[b][j]), -Kinv[a][b])
                    for a in range(3) for b in range(3)])
      for j in range(3)] for i in range(3)]
m = interval_sum(*[interval_scale(D[j][i], L[i][j]) for i in range(3) for j in range(3)])
error = interval_sum(*[interval_scale(T[i][j], 3 * C[j][i]) for i in range(3) for j in range(3)])

old_path = Path(__file__).with_name("exact_completion_separator.json")
old = json.loads(old_path.read_text())
for name, value in [("K0", K0), ("K0_inverse", Kinv), ("J", J), ("L", L),
                    ("E_hh_transpose", Eh), ("C", C)]:
    checks["all_entries_match_original_" + name] = value == [[Q(x) for x in row] for row in old[name]]


def contained(new, prior):
    return Q(prior["lower"]) <= new[0] <= new[1] <= Q(prior["upper"])


for name, value in [("D_intervals", D), ("T_intervals", T)]:
    checks["all_nine_inside_original_" + name] = all(contained(value[i][j], old[name][i][j])
                                                   for i in range(3) for j in range(3))
checks["main_inside_original"] = contained(m, old["main_interval"])
checks["error_square_inside_original"] = contained(error, old["error_square_interval"])
checks["main_above_required"] = m[0] > Q(21, 10000)
checks["error_square_nonnegative"] = error[0] >= 0
checks["error_square_below_required"] = error[1] < Q(1, 250000)
checks["main_displayed_coarsening_valid"] = contained(m, old["outward_summary"]["main"])
checks["error_displayed_coarsening_valid"] = contained(error, old["outward_summary"]["error_square"])


def enclosure_record(a):
    return {"lower": a[0], "upper": a[1]}


def outward(a, scale=10 ** 15):
    lo = a[0].numerator * scale // a[0].denominator
    hi = -((-a[1].numerator * scale) // a[1].denominator)
    return {"lower": Q(lo, scale), "upper": Q(hi, scale)}


def serial(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, dict):
        return {str(k): serial(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [serial(v) for v in x]
    return x


failures = [name for name, ok in checks.items() if not ok]
summary = {"main": outward(m), "error_square": outward(error)}
required = {"main_strictly_above": Q(21, 10000),
            "error_square_strictly_below": Q(1, 250000),
            "resulting_mean_strictly_above": Q(1, 10000)}
certificate = {"status": "FAIL" if failures else "PASS",
               "scope": "Independent exact arithmetic only; global C1 and quantifiers are audited in L593 Section 5.",
               "method": "Fourier constant coefficients; exact Gauss-Jordan; sine/cosine primitives and alternating bounds.",
               "cases": cases, "K0": K0, "K0_inverse": Kinv, "J": J, "L": L,
               "E_hh_transpose": Eh, "C": C,
               "sin_half": enclosure_record(sin_half), "cos_half": enclosure_record(cos_half),
               "D_intervals": [[enclosure_record(a) for a in row] for row in D],
               "T_intervals": [[enclosure_record(a) for a in row] for row in T],
               "main_interval": enclosure_record(m), "error_square_interval": enclosure_record(error),
               "actual_outward_bounds": summary, "required_bounds": required,
               "checks": checks, "failures": failures}
output = Path(__file__).with_name("audit_completion_separator.json")
output.write_text(json.dumps(serial(certificate), indent=2) + "\n")
print(json.dumps(serial({"status": certificate["status"], "actual_outward_bounds": summary,
                         "required_bounds": required, "failures": failures})))
print("Full independent certificate:", output)
raise SystemExit(bool(failures))
