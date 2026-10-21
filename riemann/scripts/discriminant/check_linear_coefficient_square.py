#!/usr/bin/env python3
"""Exact L405 specialization of audited L401; no analytic verification."""
from fractions import Fraction as F
from pathlib import Path
import json


def add(p, q):
    out = dict(p)
    for key, value in q.items():
        out[key] = out.get(key, F(0)) + value
    return {key: value for key, value in out.items() if value}


def scale(p, c):
    return {key: value*c for key, value in p.items() if value*c}


def mul(p, q):
    out = {}
    for m, c in p.items():
        for n, d in q.items():
            key = tuple(i+j for i, j in zip(m, n))
            out[key] = out.get(key, F(0)) + c*d
    return {key: value for key, value in out.items() if value}


def records(p):
    return [{"powers_xyz": list(k), "coefficient": str(v)}
            for k, v in sorted(p.items(), reverse=True)]


base = Path(__file__).parent
source_path = base / "response-linear-family-certificate.json"
source = json.loads(source_path.read_text())
C = [[F(entry) for entry in row] for row in source["matrix"]]
theta = [F(-1, 4), F(0), F(1), F(0), F(1), F(0)]
matrix_rows = []
for i in range(6):
    for j in range(i, 6):
        value = theta[i]*theta[j]*C[i][j]*(1 if i == j else 2)
        if value:
            matrix_rows.append({"i": i, "j": j, "contribution": str(value)})
matrix_value = sum((F(row["contribution"]) for row in matrix_rows), F(0))

x, y, z = [{tuple(int(i == j) for i in range(3)): F(1)} for j in range(3)]
x2, y2, z2 = mul(x, x), mul(y, y), mul(z, z)
xz = mul(x, z)
b = add(z, scale(x, F(-1, 4)))
S = add(add(scale(z2, F(3, 8)), scale(xz, F(5, 16))),
        add(scale(x2, F(3, 128)), scale(y2, F(-3, 8))))
T = add(add(scale(z2, F(1, 8)), scale(xz, F(7, 16))),
        add(scale(x2, F(1, 128)), scale(y2, F(-1, 8))))
P = add(add(mul(S, mul(b, b)), mul(T, y2)),
        scale(mul(mul(b, b), y2), F(1, 2)))
expected = {
    (4, 0, 0): F(3, 2048), (3, 0, 1): F(1, 128),
    (2, 2, 0): F(1, 64), (2, 0, 2): F(-7, 64),
    (1, 2, 1): F(3, 8), (1, 0, 3): F(1, 8),
    (0, 4, 0): F(-1, 8), (0, 2, 2): F(1, 4), (0, 0, 4): F(3, 8),
}
moments = {
    (4, 0, 0): F(1, 12), (3, 0, 1): F(-1, 240),
    (2, 2, 0): F(1, 720), (2, 0, 2): F(1, 4032),
    (1, 2, 1): F(-1, 20160), (1, 0, 3): F(-61, 3628800),
    (0, 4, 0): F(1, 6720), (0, 2, 2): F(19, 3628800),
    (0, 0, 4): F(17, 10644480),
}
rows = [{"powers_xyz": list(k), "factor": str(v),
         "moment": str(moments[k]), "contribution": str(v*moments[k])}
        for k, v in sorted(P.items(), reverse=True)]
polynomial_value = sum((F(row["contribution"]) for row in rows), F(0))
residual = add(P, scale(expected, -1))
checks = {
    "balanced_polynomial_identity": not residual,
    "matrix_matches_direct_moment": matrix_value == polynomial_value,
    "nonzero_coefficient": matrix_value != 0,
}
result = {
    "input": "audited L401 matrix and universal quartic table; no source theorem reproof",
    "theta_order": ["u0", "u1", "u2", "v0", "v1", "v2"],
    "theta": [str(v) for v in theta], "matrix": source["matrix"],
    "matrix_contributions": matrix_rows, "balanced_polynomial": records(P),
    "balanced_polynomial_residual": records(residual), "moment_contributions": rows,
    "matrix_value": str(matrix_value), "direct_moment_value": str(polynomial_value),
    "physical_coefficient": f"({matrix_value}) Psi/(256 pi^4 zeta(2))",
    "sign": "positive" if matrix_value > 0 else "negative" if matrix_value < 0 else "zero",
    "required_sign_threshold": "evaluation only; no prescribed sign", "checks": checks,
    "analytic_error_actual": "O(H (log H)^3) plus L401 o(H (log H)^4)",
    "analytic_error_required": "o(H (log H)^4)",
    "limitations": "Analytic errors proved in L405, not certified by this finite algebra; no clipping conclusion.",
    "failures": [name for name, passed in checks.items() if not passed],
    "initial_sign_test": "An unwarranted negative-sign assertion failed; retained in linear-coefficient-square-initial-sign-test.json. Both exact evaluations agreed on the positive value.",
}
path = base / "linear-coefficient-square-certificate.json"
path.write_text(json.dumps(result, indent=2) + "\n")
print(f"Matrix/direct moment: {matrix_value}/{polynomial_value}; required equality")
print(f"Coefficient sign: {result['sign']} ({matrix_value}); target prescribes no sign")
print(f"Balanced polynomial nonzero residuals: {len(residual)}; required 0")
print("Analytic target: O(H log^3 H)+o(H log^4 H) versus required o(H log^4 H); see L405")
print(f"Failures: {result['failures']}")
print("Certificate: scripts/discriminant/linear-coefficient-square-certificate.json")
raise SystemExit(bool(result["failures"]))
