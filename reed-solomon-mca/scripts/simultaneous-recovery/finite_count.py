"""Exact bounded test of L043 (4)-(7); not an all-labeling certificate.

All arithmetic is modulo 97. No E exclusion is imposed: this counts M
from L044, which is attained when the original rho is outside F_97.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import math

P = 97
H = tuple(x for x in range(1, P) if pow(x, 16, P) == 1)
V = {x: tuple(pow(x, j, P) for j in range(1, 9)) for x in H}
SUPPORTS = tuple(combinations(H, 4))
SHARED = (1, 96)
YS, ZS = (8, 89), (12, 85)
A0, A1 = tuple(sorted(SHARED + YS)), tuple(sorted(SHARED + ZS))
STAR = tuple(sorted(YS + ZS))
OUTSIDE = tuple(x for x in H if x not in SHARED + YS + ZS)


def solve(columns, rhs):
    """Full RREF, returning rank, consistency, and the unique solution if any."""
    n = len(columns)
    a = [[columns[j][i] % P for j in range(n)] + [b % P]
         for i, b in enumerate(rhs)]
    pivots = []
    for j in range(n):
        k = next((k for k in range(len(pivots), len(a)) if a[k][j]), None)
        if k is None:
            continue
        row = len(pivots)
        a[row], a[k] = a[k], a[row]
        inv = pow(a[row][j], -1, P)
        a[row] = [x * inv % P for x in a[row]]
        for k in range(len(a)):
            if k != row and a[k][j]:
                factor = a[k][j]
                a[k] = [(x - factor * y) % P for x, y in zip(a[k], a[row])]
        pivots.append(j)
    ok = not any(not any(row[:n]) and row[n] for row in a)
    answer = tuple(a[i][n] for i in range(n)) if ok and len(pivots) == n else None
    return len(pivots), ok, answer


def root_value(support, x):
    return math.prod(x - y for y in support) % P


def moment(weights):
    return tuple(sum(w * V[x][j] for x, w in weights.items()) % P for j in range(8))


def recurrence_columns(k):
    return {x: tuple(root_value(k, x) * V[x][j] % P for j in range(4))
            for x in SHARED + YS + ZS}


REC = {k: recurrence_columns(k) for k in SUPPORTS}


def classify(w):
    u = set(SHARED + YS + ZS + w)
    c = {x: root_value([a for a in H if a not in u], x) for x in u}
    a2 = tuple(sorted((SHARED[0],) + w))
    records, eligible = [], []
    for k in SUPPORTS:
        rec = {"K": k}
        if k in (A0, A1, a2, STAR):
            rec["status"] = "original" if k != STAR else "universal_excluded"
            records.append(rec)
            continue
        cols = REC[k]
        fy = tuple(sum(c[x] * cols[x][j] for x in YS) % P for j in range(4))
        fz = tuple(sum(c[x] * cols[x][j] for x in ZS) % P for j in range(4))
        missing = tuple(x for x in SHARED if x not in k)
        # FZ - mu*FY + sum beta_x*Fx = 0, exactly L043 (6).
        mat = [tuple(-a % P for a in fy)] + [cols[x] for x in missing]
        rank, ok, solution = solve(mat, tuple(-a % P for a in fz))
        rec.update(rank=rank, consistent=ok, missing=missing)
        if not ok:
            rec["status"] = "inconsistent"
        elif solution is None:
            raise AssertionError(("unexpected universal system", w, k))
        else:
            mu, *beta = solution
            rec.update(mu=mu, beta=beta)
            # With nonzero mu and full column rank both quotient vectors
            # are nonzero proportional; all one-zero cases are rejected.
            if mu in (0, P - 1):
                rec["status"] = "selected_parameter"
            else:
                rec["status"] = "eligible_equations"
                normalized = {x: b * pow(c[x], -1, P) % P
                              for x, b in zip(missing, beta)}
                req_r = ((1 - normalized[SHARED[1]]) * pow(1 + mu, -1, P) % P
                         if SHARED[1] in missing else None)
                a = normalized.get(SHARED[0])
                rec.update(required_r=req_r, q_minus_mu_p=a)
                eligible.append(rec)
        records.append(rec)
    return c, records, eligible


def count_weights(rows):
    histogram = Counter()
    best, witness, best_count = -1, None, 0
    for r in range(2, P):
        active = [row for row in rows if row["required_r"] in (None, r)]
        for p in range(1, P):
            baseline = set()
            qsets = {}
            for row in active:
                mu, a = row["mu"], row["q_minus_mu_p"]
                if a is None:
                    baseline.add(mu)
                else:
                    q = (mu * p + a) % P
                    qsets.setdefault(q, set()).add(mu)
            for q in range(1, P):
                if (1 - p - q) % P == 0:
                    continue
                mus = baseline | qsets.get(q, set())
                count = len(mus)
                histogram[count] += 1
                if count > best:
                    best, witness, best_count = count, (p, q, r, sorted(mus)), 1
                elif count == best:
                    best_count += 1
    expected = 95 * (96 + 95 * 95)
    assert sum(histogram.values()) == expected
    return {"maximum": best, "histogram": dict(sorted(histogram.items())),
            "gated_weights_checked": expected, "maximizer_count": best_count,
            "first_maximizer": witness}


def verify_maximizer(c, w, count):
    """Independent full-moment support membership at all 95 possible mu.

    Instead of reusing the recurrence solver, recover from moments 1..4
    for every support, then compare moments 5..8. This checks rejected
    supports as well as every admitted support at the chosen maximizer.
    """
    p, q, r, expected = count["first_maximizer"]
    a2 = tuple(sorted((SHARED[0],) + w))
    verified, actual = [], set()
    for mu in range(1, P - 1):
        weights = {x: (-mu * c[x]) % P for x in YS}
        weights.update({x: c[x] for x in ZS})
        weights[SHARED[0]] = c[SHARED[0]] * (q - mu * p) % P
        weights[SHARED[1]] = c[SHARED[1]] * (1 - (1 + mu) * r) % P
        n = moment(weights)
        for k in SUPPORTS:
            if k in (A0, A1, a2, STAR):
                continue
            inv = INVERSES[k]
            omega = tuple(sum(a * b for a, b in zip(row, n[:4])) % P for row in inv)
            if all(sum(omega[i] * V[x][j] for i, x in enumerate(k)) % P == n[j]
                   for j in range(4, 8)):
                actual.add(mu)
                verified.append({"mu": mu, "K": k, "omega": omega,
                                 "all_eight_moments": True,
                                 "full_weight": all(omega)})
    assert actual == set(expected), (w, sorted(actual), expected)
    return {"mu_support_memberships_checked": 95 * (len(SUPPORTS) - 4),
            "complete_admitted_records": verified, "exact_set_match": True}


def inverses():
    result = {}
    for k in SUPPORTS:
        cols = [V[x][:4] for x in k]
        answers = [solve(cols, [int(i == j) for i in range(4)])[2] for j in range(4)]
        result[k] = tuple(zip(*answers))
    return result


INVERSES = inverses()


def main():
    result = {"scope": {"prime": P, "H": H, "h_d": SHARED, "Y": YS, "Z": ZS,
                         "all_W": list(combinations(OUTSIDE, 3)),
                         "threshold_sought": 12, "uniform_bound_sought": 11,
                         "E_exclusion": False, "fourth_weight_gate": False,
                         "all_labelings": False}, "cases": [], "failures": []}
    out = Path(__file__).with_name("finite-count-result.json")
    for i, w in enumerate(combinations(OUTSIDE, 3), 1):
        c, records, eligible = classify(w)
        counts = count_weights(eligible)
        verified = verify_maximizer(c, w, counts)
        result["cases"].append({"W": w, "c": c, "support_classification": records,
                                "count": counts, "verification": verified})
        if i % 10 == 0:
            out.write_text(json.dumps(result, separators=(",", ":")) + "\n")
            print(f"completed {i}/120; maximum so far "
                  f"{max(a['count']['maximum'] for a in result['cases'])}", flush=True)
    assert len(result["cases"]) == 120
    maxima = Counter(a["count"]["maximum"] for a in result["cases"])
    result["summary"] = {"cases": len(result["cases"]),
                          "maximum": max(maxima), "case_maximum_histogram": dict(sorted(maxima.items())),
                          "gated_weight_cases": sum(a["count"]["gated_weights_checked"] for a in result["cases"]),
                          "classified_supports": 120 * len(SUPPORTS),
                          "independent_membership_checks": sum(a["verification"]["mu_support_memberships_checked"] for a in result["cases"]),
                          "all_maximizers_verified": False,
                          "one_maximizer_per_case_verified": True,
                          "counterexample_found": max(maxima) >= 12,
                          "proves_uniform_bound": False, "failures": []}
    out.write_text(json.dumps(result, separators=(",", ":")) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))
    print(f"actual maximum {max(maxima)}; refutation threshold 12; desired uniform bound 11; certificate {out}")


if __name__ == "__main__":
    main()
