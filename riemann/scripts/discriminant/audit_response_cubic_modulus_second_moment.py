"""Independent step-203 audit of both saved L427 rational certificates.

No imports from either coefficient generator. Finite T factors are obtained
from binomial coefficients and generating-function finite differences.
Proofs of the infinite tail bounds are in L427; this checks their complete
rational specialization and all saved load-bearing fields.
"""
import hashlib
import json
from fractions import Fraction as Q
from math import comb, isqrt
from pathlib import Path

BASE = Path(__file__).resolve().parent
GRID = 10**18
FAILURES = []
RECORDS = []


def check(label, actual, expected):
    ok = actual == expected
    RECORDS.append({"field": label, "passed": ok})
    if not ok:
        FAILURES.append({"field": label, "actual": str(actual),
                         "expected": str(expected)})


def outward(lo, hi):
    a, ar = divmod(lo * GRID, 1)
    b, br = divmod(hi * GRID, 1)
    assert lo <= hi
    return Q(int(a), GRID), Q(int(b) + (br != 0), GRID)


def plus(a, b):
    return outward(a[0] + b[0], a[1] + b[1])


def minus(a, b):
    return outward(a[0] - b[1], a[1] - b[0])


def times(a, b):
    corners = [a[i] * b[j] for i in (0, 1) for j in (0, 1)]
    return outward(min(corners), max(corners))


def quotient(a, b):
    assert b[0] > 0
    return times(a, (1 / b[1], 1 / b[0]))


def point(x):
    return Q(x), Q(x)


def encoded(a):
    return {"lower": str(a[0]), "upper": str(a[1])}


def compare_tree(label, saved, expected):
    if isinstance(expected, dict):
        check(label + "/keys", set(saved) - {"decimal_preview"}, set(expected))
        for key, value in expected.items():
            compare_tree(label + "/" + str(key), saved[key], value)
    elif isinstance(expected, list):
        check(label + "/length", len(saved), len(expected))
        for i, value in enumerate(expected):
            compare_tree(label + "/" + str(i), saved[i], value)
    else:
        # All rational strings are exact; decimal previews are never consulted.
        if isinstance(expected, str):
            try:
                saved, expected = Q(saved), Q(expected)
            except (ValueError, ZeroDivisionError):
                pass
        check(label, saved, expected)


def t_numerator(j):
    """Coefficients after multiplying by (1-v)^(2j-1)(1-u)^j.

    For r>0 the coefficients are polynomial of degrees <=2j-2 in e
    and <=j-1 in r. The exceptional r=0 coefficient adds a polynomial
    times (1-u)^j. Thus the numerator has e<=2j-2 and r<=j.
    Extra computed coefficients check the implementation of this identity.
    """
    dv, du = 2*j-1, j

    def coefficient(e, r):
        if min(e, r) < 0:
            return 0
        return (1 if r == 0 else 2) * comb(e+j-1, j-1) * comb(e+r+j-1, j-1)

    result = []
    for e in range(dv+3):
        for r in range(du+4):
            value = sum((-1)**(a+b) * comb(dv, a) * comb(du, b)
                        * coefficient(e-a, r-b)
                        for a in range(dv+1) for b in range(du+1))
            if e >= dv or r > du:
                check(f"T{j}/numerator_zero/{e}/{r}", value, 0)
            elif value:
                result.append([e, r, value])
    return result


NUMERATORS = {j: t_numerator(j) for j in (2, 3)}


def t_factor(p, j):
    u, v = Q(1, p**3), Q(1, p**5)
    numerator = sum(Q(c) * v**e * u**r for e, r, c in NUMERATORS[j])
    return numerator / ((1-v)**(2*j-1) * (1-u)**j)


def power_log_tail(P, s, multiplicity=1):
    return Q(multiplicity, (s-1)*P**(s-1)) / (1-Q(1, (P+1)**s))


def audit(P, E):
    source = BASE / f"response-cubic-modulus-second-moment-{P}-{E}.json"
    raw = source.read_bytes()
    saved = json.loads(raw)
    prefix = f"P{P}E{E}"
    check(prefix + "/prime_cutoff", saved["prime_cutoff"], P)
    check(prefix + "/local_order", saved["local_order"], E)
    check(prefix + "/denominator", saved["denominator"], GRID)
    primes = [n for n in range(2, P+1)
              if all(n % d != 0 for d in range(2, isqrt(n)+1))]
    check(prefix + "/complete_prime_list", saved["primes"], primes)
    cs, c_locals, tails = {}, {}, {}
    for j in (1, 2, 3, 13, 14, 15, 16, 17):
        value, rows = point(1), []
        for p in primes:
            terms = [Q(comb(j+e-1, e)**2, p**(5*e)) for e in range(E+2)]
            partial = sum(terms[:-1])
            ratio = terms[-1] / terms[-2]
            assert 0 < ratio < 1
            remainder = terms[-1] / (1-ratio)
            factor = outward(partial, partial+remainder)
            rows.append({"p": p, "factor": encoded(factor),
                         "local_tail_upper": str(remainder), "next_ratio": str(ratio)})
            value = times(value, factor)
        tail = Q(j*j, 4*P**4) / (1-Q(j*j, (P+1)**5))
        assert 0 < tail < 1
        tails[f"C{j}"] = str(tail)
        cs[j] = times(value, (Q(1), 1/(1-tail)))
        c_locals[str(j)] = rows

    zs = {}
    for s in (3, 5, 6):
        value = point(1)
        for p in primes:
            value = times(value, point(Q(p**s, p**s-1)))
        tail = power_log_tail(P, s)
        assert 0 < tail < 1
        tails[f"zeta{s}"] = str(tail)
        zs[s] = times(value, (Q(1), 1/(1-tail)))
    S = quotient(times(zs[5], times(zs[3], zs[3])), zs[6])
    ts, t_locals = {}, {}
    for j in (2, 3):
        value, rows = point(1), []
        for p in primes:
            factor = t_factor(p, j)
            assert factor > 1
            rows.append({"p": p, "factor": str(factor)})
            value = times(value, point(factor))
        tail = power_log_tail(P, 3, 2*j) + power_log_tail(P, 5, j*j)
        assert 0 < tail < 1
        tails[f"T{j}"] = str(tail)
        ts[j] = times(value, (Q(1), 1/(1-tail)))
        t_locals[str(j)] = rows

    ratios, theta, bs, ds = {}, {}, {}, {}
    for k in (13, 14):
        ratios[k] = quotient(cs[k+1], cs[k])
        theta[k] = quotient(minus(S, cs[1]), minus(ratios[k], cs[1]))
        bs[k] = plus(cs[2], times(theta[k], minus(quotient(cs[k+2], cs[k]), cs[2])))
        ds[k] = plus(cs[3], times(theta[k], minus(quotient(cs[k+3], cs[k]), cs[3])))
    alpha = quotient(minus(bs[14], ts[2]), minus(bs[14], bs[13]))
    independent = plus(times(alpha, ds[13]), times(minus(point(1), alpha), ds[14]))
    # Preserve the historical certificate's original expression and threshold.
    law = (independent if P == 200 else
           plus(ds[14], times(alpha, minus(ds[13], ds[14]))))
    law_minus_actual = minus(law, ts[3])
    actual_minus_law = minus(ts[3], law)
    bounds = {"S": encoded(S), "T2": encoded(ts[2]), "T3": encoded(ts[3]),
              "B13": encoded(bs[13]), "B14": encoded(bs[14]),
              "D13": encoded(ds[13]), "D14": encoded(ds[14]),
              "alpha": encoded(alpha), "law3": encoded(law),
              "law3_minus_T3": encoded(law_minus_actual),
              "law3_independent_box": encoded(independent),
              "C": {str(k): encoded(v) for k, v in cs.items()},
              "theta": {str(k): encoded(v) for k, v in theta.items()}}
    if P == 200:
        del bounds["law3_independent_box"]
    checks = {"S_above_C1": S[0] > cs[1][1],
              "R13_above_S": ratios[13][0] > S[1],
              "R14_above_S": ratios[14][0] > S[1],
              "B13_below_T2": bs[13][1] < ts[2][0],
              "T2_below_B14": ts[2][1] < bs[14][0],
              "alpha_in_unit_interval": 0 < alpha[0] <= alpha[1] < 1,
              "actual_minus_law_exceeds_7_over_1000": actual_minus_law[0] > Q(7, 1000)}
    if P == 200:
        del checks["actual_minus_law_exceeds_7_over_1000"]
        checks["gap_exceeds_1_over_100000"] = (
            law_minus_actual[0] > Q(1, 100000) or law_minus_actual[1] < -Q(1, 100000))
    original_failures = [key for key, ok in checks.items() if not ok]
    reconstructed = {"bounds": bounds, "checks": checks, "failures": original_failures,
                     "log_tail_upper_bounds": tails, "C_local_factors": c_locals,
                     "T_local_factors": t_locals}
    for field, value in reconstructed.items():
        compare_tree(prefix + "/" + field, saved[field], value)
    overlap = max(independent[0], ts[3][0]) <= min(independent[1], ts[3][1])
    check(prefix + "/preserved_independent_box_overlap", overlap, True)
    if P == 1000:
        check(prefix + "/equation10_T3_lower", ts[3][0], Q(3474983372117534637, GRID))
        check(prefix + "/equation10_law_upper", law[1], Q(3467058691456416067, GRID))
        check(prefix + "/equation10_gap_lower", actual_minus_law[0], Q(792468066111857, 10**17))
        check(prefix + "/strict_separator", actual_minus_law[0] > Q(7, 1000), True)
    else:
        check(prefix + "/initial_independent_gap_not_certified",
              actual_minus_law[0] > Q(7, 1000), False)
    return {"source": source.name, "sha256": hashlib.sha256(raw).hexdigest(),
            "prime_count": len(primes), "prime_cutoff": P, "local_order": E,
            "verified_C_factor_count": len(primes)*8,
            "verified_T_factor_count": len(primes)*2,
            "actual_minus_law": encoded(actual_minus_law),
            "expression": "independent alpha boxes" if P == 200 else "correlated convex identity",
            "required_lower_bound": "7/1000",
            "saved_required_gap": saved["required_gap"],
            "independent_box_overlaps_actual": overlap,
            "reconstructed": reconstructed}


def main():
    runs = [audit(200, 40), audit(1000, 80)]
    out = {"status": "PASS" if not FAILURES else "FAIL",
           "method": "independent binomial and finite-difference rational verifier; no generator imports",
           "T_numerators": {str(k): v for k, v in NUMERATORS.items()},
           "runs": runs, "comparison_count": len(RECORDS),
           "comparisons": RECORDS, "failures": FAILURES,
           "qualifications": "Analytic tail inequalities and limiting arguments are audited in L427; not formal verification. Decimal previews ignored."}
    path = BASE / "response-cubic-modulus-second-moment-audit-203.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    for run in runs:
        print(f"P={run['prime_cutoff']}, E={run['local_order']}: "
              f"{run['verified_C_factor_count']} C factors, {run['verified_T_factor_count']} T factors; "
              f"actual-law={run['actual_minus_law']}; required >7/1000; "
              f"original failures={run['reconstructed']['failures']}")
    print(f"Audit comparisons={len(RECORDS)}; audit failures={len(FAILURES)}; certificate={path}")
    if FAILURES:
        print(FAILURES)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
