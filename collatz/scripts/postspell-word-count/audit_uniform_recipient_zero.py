#!/usr/bin/env python3
"""Independent finite audit of L090. Does not execute its constructor.

The all-allocation and logarithm-remainder proofs are in canonical L090.
All source operands are read and compared, not just the stored pass flags.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = HERE / "uniform-recipient-zero-certificate.json"
raw = SOURCE.read_bytes()
source = json.loads(raw)
base = [
    (8, 40), (15, 72), (28, 134), (52, 249), (98, 467),
    (184, 877), (347, 1650), (653, 3106), (1230, 5849),
    (2317, 11018), (4365, 20756), (8224, 39104),
    (15494, 73672), (29191, 138802), (54998, 261511),
    (103621, 492705), (195229, 928293), (367827, 1748976),
    (693015, 3295208), (1305695, 6208431), (2460032, 11697176),
    (4634896, 22038409), (8732512, 41522114),
    (16452748, 78230965), (30998279, 32670621),
]
checks = []
comparisons = []


def verify(name, value):
    checks.append(dict(name=name, passed=bool(value)))


def comparison(record, name, a, relation, b):
    a, b = F(a), F(b)
    cross = a.numerator*b.denominator-b.numerator*a.denominator
    passed = {"<": cross < 0, ">": cross > 0, "==": cross == 0}[relation]
    matches = (
        set(record) == {"name", "actual", "relation", "required", "difference", "passed"}
        and record["name"] == name and F(record["actual"]) == a
        and record["relation"] == relation and F(record["required"]) == b
        and F(record["difference"]) == a-b and record["passed"] == passed
    )
    comparisons.append(dict(name=name, actual=a, relation=relation, required=b,
                            cross_product=cross, difference=a-b, passed=passed,
                            source_matches=matches))
    verify(name + ": independently reconstructed comparison", passed and matches)


def group(records, specs):
    verify("complete comparison names: " + specs[0][0],
           [r["name"] for r in records] == [s[0] for s in specs])
    for record, spec in zip(records, specs):
        comparison(record, *spec)


def fields(record, expected, label):
    for key, value in expected.items():
        verify(label + " numeric field " + key, F(record[key]) == value)


canonical = [tuple(map(int, row)) for row in re.findall(
    r"^\|(\d+)\|(\d+)\|(\d+)\|$",
    (ROOT / "lemmas/L055-fixed-count-twenty-five-word-real-witness.md").read_text(),
    re.M)]
verify("all 25 independently transcribed pairs equal L055",
       canonical == [(i, j, h) for i, (j, h) in enumerate(base)])
B, U, kappa = 9250245, F(20_000_000_000), F(23, 11)
lam = F(10584, 10**14)
E = F(24*23, (1 << 62)-23)
residual = lam-E
cap = kappa/residual+kappa
threshold = F(1 << 62, 11)
A = F(27, 16)**8*U-F(12, 11)
fields(source, dict(B=B, kappa=kappa, lambda_lower=lam, E=E,
                   residual=residual, cap=cap, U=U, row1_threshold=threshold),
       "common")
verify("lower domain is precisely n>=47", F(540, 11)-kappa == 47)
group(source["common_checks"], [
    ("row count", len(base), "==", 25),
    ("first J", base[0][0], "==", 8),
    ("next J", base[1][0], "==", 15),
    ("minimum J increment", min(base[i+1][0]-base[i][0] for i in range(24)), ">", 0),
    ("positive residual", residual, ">", 0),
    ("guard-conditioned cap", cap, "<", U),
    ("positive H coefficient", A, ">", 0),
    ("row1 guard lower", threshold, ">", 4*10**17),
])

verify("exact approved range and ordering",
       [c["d"] for c in source["cases"]] == list(range(6, 34)))
cases = []
for d, old in zip(range(6, 34), source["cases"]):
    rows = [[i, j, h + (d if i == 24 else -d if i == 0 else 0)]
            for i, (j, h) in enumerate(base)]
    verify(f"d{d} complete changed table", old["rows"] == rows)
    verify(f"d{d} every eta-domain and every residual J comparison",
           all(j >= 2 and h >= 3 for _, j, h in rows)
           and all(j >= 15 for _, j, _ in rows[1:]))
    sumj = sum(j for _, j, _ in rows)
    sumh = sum(h for _, _, h in rows)
    tail_sum = 25*2+18*B
    K, N = 3*sumj+sumh, 4*sumj+sumh+tail_sum
    h = rows[0][2]
    # Product-of-powers evaluation, independent of constructor exponent sums.
    G = F(27, 16)**8*F(3, 2)**h
    Q = F(12, 11)*F(3, 2)**h+1
    eta = kappa-Q/G
    offset = kappa-Q/(1 << 20)
    # Evaluate first in the unshifted coordinate; retain both shifts.
    endpoint = G*(U-kappa+eta)/(1 << 20)+kappa
    direct = (G*U-Q)/(1 << 20)+kappa
    factored = A*F(3, 2)**h/(1 << 20)+kappa-F(1, 1 << 20)
    verify(f"d{d} eta and actual pre-tail bracket positive",
           0 < eta < kappa and G*F(540, 11)-Q > 0)
    verify(f"d{d} independent endpoint evaluations", endpoint == direct == factored)
    numeric = dict(K=K, N=N, G0=G, Q0=Q, signed_offset=offset,
                   endpoint_upper=endpoint, factored_endpoint=factored,
                   strict_separation=threshold-endpoint)
    fields(old, numeric, f"d{d}")
    group(old["checks"], [
        (f"d{d} minimum H", min(hh for _, _, hh in rows), ">", 2),
        (f"d{d} sum J", sumj, "==", 66061058),
        (f"d{d} sum H", sumh, "==", 199390205),
        (f"d{d} K", K, "==", 397573379),
        (f"d{d} N", N, "==", 630138897),
        (f"d{d} signed offset positive", offset, ">", 0),
        (f"d{d} factored endpoint agrees", factored, "==", endpoint),
        (f"d{d} endpoint common upper", endpoint, "<", 2*10**12),
        (f"d{d} strict own-input rejection", endpoint, "<", threshold),
    ])
    cases.append(dict(d=d, rows=rows, eta0=eta, **numeric))

maximum = cases[0]["endpoint_upper"]
for previous, current in zip(cases, cases[1:]):
    d = previous["d"]
    difference = A*F(3, 2)**(39-d)/(1 << 21)
    verify(f"d{d} exact adjacent decrease",
           previous["endpoint_upper"]-current["endpoint_upper"] == difference > 0)
uniform = dict(coefficient=A, maximum_d=6, maximum_endpoint=maximum,
               endpoint_bound=2*10**12, threshold=threshold,
               minimum_separation=threshold-maximum)
fields(source["uniform_comparison"], uniform, "uniform")
group(source["uniform_comparison"]["checks"], [
    ("maximum at d6", max(cases, key=lambda c: c["endpoint_upper"])["d"], "==", 6),
    ("maximum signed endpoint", maximum, "<", 2*10**12),
    ("uniform strict separation", threshold-maximum, ">", 0),
])
verify("all stored table verdicts agree with complete reconstruction",
       source["case_verdicts"] ==
       [dict(d=d, checks=9, passed=True) for d in range(6, 34)])
verify("complete original summary agrees",
       source["summary"] == dict(tables=28, checks=263, failures=[], passed=True))
verify("all 263 original rational comparisons inspected", len(comparisons) == 263)


def log_interval(t):
    x = (t-1)/(t+1)
    assert 0 < x < 1
    terms = [2*x**(2*m+1)/(2*m+1) for m in range(96)]
    partial = sum(terms, F(0))
    remainder = 2*x**193/(193*(1-x*x))
    return dict(argument=t, x=x, terms=terms, remainder=remainder,
                lower=partial, upper=partial+remainder)


logs = {str(t): log_interval(F(t)) for t in (2, 3)}
lo = 630138897*logs["2"]["lower"]-397573379*logs["3"]["upper"]
hi = 630138897*logs["2"]["upper"]-397573379*logs["3"]["lower"]
grid_lo, grid_hi = F(105843488, 10**18), F(105843489, 10**18)
verify("complete Lambda enclosure including amplified errors",
       lam < grid_lo < lo < hi < grid_hi < F(10585, 10**14))
failures = [c["name"] for c in checks if not c["passed"]]
result = dict(
    source=str(SOURCE.relative_to(ROOT)), source_sha256=sha256(raw).hexdigest(),
    common=dict(B=B, U=U, kappa=kappa, lambda_lower=lam, E=E,
                residual=residual, cap=cap, tail_sum=25*2+18*B),
    uniform=uniform, cases=cases, comparisons=comparisons, logarithms=logs,
    lambda_enclosure=dict(lower=lo, upper=hi, outward_grid=[grid_lo, grid_hi]),
    checks=checks,
    summary=dict(tables=len(cases), original_comparisons=len(comparisons),
                 audit_checks=len(checks), failures=failures, passed=not failures),
    limitations="Finite arithmetic only; quantified proof and analytic remainder in L090. "
                "No other recipients, range extension, feasibility or actual-word verdict.")
out = HERE / "uniform-recipient-zero-audit-certificate.json"
out.write_text(json.dumps(result, indent=2, default=str)+"\n")
print(f"Tables: {len(cases)}; original comparisons: {len(comparisons)}; "
      f"audit checks: {len(checks)}; failures: {failures}")
print(f"Cap actual {cap}; required < {U}")
print(f"Maximum actual {maximum}; required < {2*10**12}")
print(f"Row1 requires >= {threshold}; all comparisons checked by integer cross products")
print(f"Lambda outward bounds: {grid_lo}, {grid_hi}; "
      f"required inside ({lam}, {F(10585, 10**14)})")
print(f"Certificate: {out.relative_to(ROOT)}")
if failures:
    raise SystemExit(1)
