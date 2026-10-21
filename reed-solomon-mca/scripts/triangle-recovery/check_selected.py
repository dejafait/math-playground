"""Selected-pencil regression for L057; no uniform count certificate.

Compare the projected/Lagrange criterion against direct first-four
Gaussian recovery followed by all eight moment checks at every eligible
prime-field parameter, for each nonbase four-support of one fixed
triangle. Save every support row; never use the regression as a proof
over F_(97^20), all labels, or arbitrary extension-field free weights.
"""
from itertools import combinations
from pathlib import Path
import json

PCHAR = 97
H = [x for x in range(1, PCHAR) if pow(x, 16, PCHAR) == 1]
a, b, c, y1, y2, z1, z2, w1, w2 = H[:9]
PAIRS = (a, b, c)
YS, ZS, WS = (y1, y2), (z1, z2), (w1, w2)
U = set(H[:9])
BASE = {frozenset((a, b, *YS)), frozenset((a, c, *ZS)),
        frozenset((b, c, *WS))}


def inv(x):
    if x % PCHAR == 0:
        raise ValueError("zero denominator")
    return pow(x % PCHAR, -1, PCHAR)


def prod(values):
    result = 1
    for value in values:
        result = result * value % PCHAR
    return result


CX = {x: prod(x - h for h in H if h not in U) for x in U}


def lagrange_value(x, labels, value):
    return prod((value - u) * inv(x - u) for u in labels if u != x)


def gaussian_inverse(matrix):
    n = len(matrix)
    rows = [list(row) + [int(i == j) for j in range(n)]
            for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j] % PCHAR)
        rows[j], rows[pivot] = rows[pivot], rows[j]
        scale = inv(rows[j][j])
        rows[j] = [x * scale % PCHAR for x in rows[j]]
        for i in range(n):
            if i != j:
                scale = rows[i][j]
                rows[i] = [(x - scale * y) % PCHAR
                           for x, y in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


def dot(row, col):
    return sum(x * y for x, y in zip(row, col)) % PCHAR


def label_data(k):
    missing = tuple(x for x in PAIRS if x not in k)
    fk = lambda x: prod(x - u for u in k)
    gj = lambda x: prod(x - u for u in missing)
    vectors = [[sum(CX[x] * x * fk(x) * gj(x) * pow(x, j, PCHAR)
                    for x in labels) % PCHAR
                for j in range(4 - len(missing))] for labels in (YS, ZS)]
    beta = [{x: -sum(CX[u] * u * fk(u)
                    * lagrange_value(x, missing, u) for u in labels)
             * inv(x * fk(x)) % PCHAR for x in missing}
            for labels in (YS, ZS)]
    vy, vz = vectors
    if not any(vy) and not any(vz):
        kind, mu = "both_zero", None
    elif not any(vy) or not any(vz):
        kind, mu = "one_zero", None
    else:
        pivot = next(i for i, value in enumerate(vy) if value)
        mu = vz[pivot] * inv(vy[pivot]) % PCHAR
        kind = ("proportional" if all((zz - mu * yy) % PCHAR == 0
                                      for yy, zz in zip(vy, vz))
                else "independent")
    return missing, vectors, beta, kind, mu


def criterion(k, data, weights, rho, gamma0, g, lam):
    missing, vectors, (by, bz), kind, mu = data
    p, q, r = weights
    aa = {a: CX[a] * (1 - p) - bz.get(a, 0), b: -bz.get(b, 0),
          c: CX[c] * r - bz.get(c, 0)}
    bb = {a: -CX[a] * p + by.get(a, 0),
          b: -CX[b] * q + by.get(b, 0), c: by.get(c, 0)}
    if kind == "both_zero":
        assert len(missing) == 3
        assert any(aa[x] % PCHAR or bb[x] % PCHAR for x in missing)
        pivot = next((x for x in missing if bb[x] % PCHAR), None)
        if pivot is None:
            return {}
        mu = -aa[pivot] * inv(bb[pivot]) % PCHAR
    elif kind != "proportional":
        return {}
    ee = (rho - (1 - rho) * mu) % PCHAR
    if mu in (0, PCHAR - 1) or ee == 0:
        return {}
    if any((aa[x] + mu * bb[x]) % PCHAR for x in missing):
        return {}
    coeff = {x: -mu * CX[x] % PCHAR for x in YS}
    coeff.update({x: CX[x] for x in ZS})
    coeff.update({a: CX[a] * (1 - (1 + mu) * p) % PCHAR,
                  b: -mu * CX[b] * q % PCHAR, c: CX[c] * r % PCHAR})
    omega = [sum(value * x * lagrange_value(xi, k, x)
                 for x, value in coeff.items()) * inv(xi) % PCHAR
             for xi in k]
    actual = [value * lam * inv(g * ee) % PCHAR for value in omega]
    tt = (gamma0 + g * rho * inv(ee)) % PCHAR
    return {tt: actual}


def run():
    label_rows = [(k, label_data(k)) for k in combinations(H, 4)
                  if frozenset(k) not in BASE]
    # Fixed gated weights, plus one deliberately recoverable isolated
    # m=3 configuration, selected solely to exercise positive recovery.
    cases = [(2, 3, 4)]
    for k, data in label_rows:
        missing, _, (by, bz), kind, mu = data
        if len(missing) == 3 and kind == "proportional" and mu not in (0, 96):
            p = (1 - (bz[a] - mu * by[a]) * inv(CX[a])) * inv(1 + mu) % 97
            q = (by[b] - bz[b] * inv(mu)) * inv(CX[b]) % 97
            r = (bz[c] - mu * by[c]) * inv(CX[c]) % 97
            if all(value not in (0, 1) for value in (p, q, r)):
                cases.append((p, q, r))
                break
    assert len(cases) == 2, "positive-case selection failed"
    # Positive both-zero lift at K=(18,22,64,89), mu=1. This
    # exercises the exceptional quotient branch independently of (7).
    cases.append((94, 95, 44))
    gamma0, g, rho, lam = 7, 11, 4, 5
    gammas = (gamma0, (gamma0 + g) % 97, (gamma0 + g * rho) % 97)
    alphas = ((gammas[1] - gammas[2]) % 97,
              (gammas[2] - gammas[0]) % 97,
              (gammas[0] - gammas[1]) % 97)
    matrices = {k: [[pow(x, j, 97) for x in k] for j in range(1, 9)]
                for k, _ in label_rows}
    inverses = {k: gaussian_inverse(matrix[:4]) for k, matrix in matrices.items()}
    reports, failures = [], []
    for p, q, r in cases:
        normalized = ({a: p, b: q, y1: 1, y2: 1},
                      {a: 1 - p, c: r, z1: 1, z2: 1},
                      {b: 1 - q, c: 1 - r, w1: 1, w2: 1})
        moments = [[sum(lam * CX[x] * weight * inv(alpha)
                        * pow(x, j, 97) for x, weight in error.items()) % 97
                    for j in range(1, 9)]
                   for alpha, error in zip(alphas, normalized)]
        by_parameter = {tt: [(moments[0][j] + (tt - gamma0) * inv(g)
                             * (moments[1][j] - moments[0][j])) % 97
                            for j in range(8)] for tt in range(97)}
        assert by_parameter[gammas[2]] == moments[2], "third base moments"
        rows, kind_counts, relaxed, full = [], {}, 0, 0
        for k, data in label_rows:
            predicted = criterion(k, data, (p, q, r), rho, gamma0, g, lam)
            direct = {}
            for tt, syndrome in by_parameter.items():
                if tt in gammas:
                    continue
                actual = [dot(row, syndrome[:4]) for row in inverses[k]]
                if all(dot(row, actual) == value
                       for row, value in zip(matrices[k], syndrome)):
                    direct[tt] = actual
            if predicted != direct:
                failures.append({"weights": [p, q, r], "K": k,
                                 "predicted": predicted, "direct": direct})
            kind_counts[data[3]] = kind_counts.get(data[3], 0) + 1
            relaxed += len(direct)
            full += sum(all(weights) for weights in direct.values())
            rows.append({"K": k, "m": len(data[0]), "kind": data[3],
                         "projected": data[1], "beta_Y_Z": data[2],
                         "label_mu": data[4], "predicted": predicted,
                         "direct_eight_moment": direct})
        reports.append({"weights": [p, q, r], "label_classes": kind_counts,
                        "support_rows": len(rows), "eligible_parameters_per_row": 94,
                        "relaxed_witnesses": relaxed, "full_witnesses": full,
                        "rows": rows})
    result = {"scope": "Three selected prime-field pencils only; regression, not uniform proof",
              "H": H, "labels": list(H[:9]), "gammas": gammas, "lambda": lam,
              "required_failures": 0, "actual_failures": len(failures),
              "required_support_rows_per_case": 1817, "cases": reports,
              "failures": failures}
    path = Path(__file__).with_name("selected-regression.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Actual/required failures: {len(failures)}/0; "
          f"support rows per case: {[r['support_rows'] for r in reports]}/1817; "
          "eligible parameters per row: 94/94")
    for report in reports:
        print(f"weights={report['weights']}; classes={report['label_classes']}; "
              f"relaxed/full witnesses={report['relaxed_witnesses']}/{report['full_witnesses']}")
    print(f"Certificate: {path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    run()
