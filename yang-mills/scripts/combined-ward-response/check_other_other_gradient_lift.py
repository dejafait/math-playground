"""Exact supplemental interval checks for L092; not a probe asymptotic test."""
from fractions import Fraction as F
from pathlib import Path
import json


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), F(0))
             for col in bt] for row in a]


def inverse(a):
    n = len(a)
    rows = [list(row) + [F(i == j) for j in range(n)]
            for i, row in enumerate(a)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        scale = rows[j][j]
        rows[j] = [x / scale for x in rows[j]]
        for i in range(n):
            if i != j:
                scale = rows[i][j]
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


def resolvent(a, lam):
    return inverse([[x + (lam if i == j else 0)
                     for j, x in enumerate(row)] for i, row in enumerate(a)])


def serialize(a):
    return [[str(x) for x in row] for row in a]


def main():
    records, failures = [], []
    for n in (2, 4, 6, 8):
        b0 = [[F((ell == s) - (ell == s - 1)) for ell in range(n)]
              for s in range(1, n)]
        b = [[F(ell < s) for ell in range(n)] for s in range(1, n)]
        bt, b0t = transpose(b), transpose(b0)
        ld, le = multiply(b0, b0t), multiply(b0t, b0)
        prefix = multiply(b0, bt)
        prefix_error = [[x + F(i == j) for j, x in enumerate(row)]
                        for i, row in enumerate(prefix)]
        m = [[F(min(s, t)) for t in range(1, n)] for s in range(1, n)]
        for lam in (F(1, 7), F(1), F(5)):
            rd, ra = resolvent(ld, lam), resolvent(le, lam)
            left, right = multiply(ra, bt), multiply(b0t, rd)
            error = [[lam * left[i][j] - bt[i][j] - right[i][j]
                      for j in range(n - 1)] for i in range(n)]
            c = [[x / lam for x in row] for row in b]
            energy = multiply(c, transpose(c))
            energy_error = [[lam * x - m[i][j] / lam for j, x in enumerate(row)]
                            for i, row in enumerate(energy)]
            constant_error = [sum(row, F(0)) for row in le]
            values = [x for matrix in (prefix_error, error, energy_error)
                      for row in matrix for x in row] + constant_error
            actual = max(map(abs, values))
            record = dict(N=n, lambda_value=str(lam), actual_max_error=str(actual),
                          required_max_error="0", prefix_error=serialize(prefix_error),
                          resolvent_error=serialize(error), energy_error=serialize(energy_error),
                          constant_mode_error=list(map(str, constant_error)))
            records.append(record)
            if actual:
                failures.append(dict(N=n, lambda_value=str(lam)))
    path = Path(__file__).with_name("other-other-gradient-lift-certificate.json")
    path.write_text(json.dumps(dict(arithmetic="exact fractions", cases=records,
                                   failures=failures), indent=2) + "\n")
    actual_max = max(F(record["actual_max_error"]) for record in records)
    print(f"cases={len(records)}; actual_max_error={actual_max}; required_max_error=0; "
          f"failures={len(failures)}; certificate={path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
