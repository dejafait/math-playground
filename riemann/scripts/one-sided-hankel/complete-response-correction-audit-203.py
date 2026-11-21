"""Independent exact audit of L723's algebra and complete interval certificate.

Replays step 201 without overwriting it. Certifies every stored cell
bound by clearing positive denominators and checking all coefficients
in the Bernstein basis on that cell, rather than repeating its interval
arithmetic. All arithmetic deciding a check is rational.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import contextlib
import hashlib
import io
import json

ROOT = Path(__file__).resolve().parent
OLD = ROOT / "complete-response-correction-certificate-201.json"
SOURCE = ROOT / "complete-response-correction-certificate-201.py"
REPLAY = ROOT / "complete-response-correction-replay-203.json"
OUT = Path(__file__).with_suffix(".json")
checks = []


def check(name, passed, **details):
    checks.append(dict(name=name, passed=bool(passed), **details))


def rat(value):
    value = F(value)
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def read_rat(value):
    return F(int(value["numerator"]), int(value["denominator"]))


# Bivariate rational polynomials in t,x; exact formal identity checks.
def const(v):
    return {(0, 0): F(v)} if v else {}


def add(*polys):
    result = {}
    for poly in polys:
        for monomial, coeff in poly.items():
            result[monomial] = result.get(monomial, F(0)) + coeff
    return {m: c for m, c in result.items() if c}


def scale(poly, factor):
    return {m: c * factor for m, c in poly.items() if c * factor}


def sub(a, b):
    return add(a, scale(b, -1))


def mul(*polys):
    result = const(1)
    for poly in polys:
        new = {}
        for (a, b), c in result.items():
            for (d, e), f in poly.items():
                key = (a + d, b + e)
                new[key] = new.get(key, F(0)) + c * f
        result = {m: c for m, c in new.items() if c}
    return result


def dx(poly):
    return {(a, b - 1): c * b for (a, b), c in poly.items() if b}


def at_x(poly, x):
    result = {}
    for (a, b), c in poly.items():
        result[(a, 0)] = result.get((a, 0), F(0)) + c * x**b
    return {m: c for m, c in result.items() if c}


def bernstein(poly, left, width):
    """Exact coefficients after t=left+width*s in degree d Bernstein basis.

    If P(s)=sum a_k*s^k, then b_j=sum_{k<=j} a_k*C(j,k)/C(d,k).
    The identity follows by expanding (s+(1-s))^(d-k).
    Nonnegative b_j imply P>=0 on the entire closed unit interval.
    """
    assert all(b == 0 for a, b in poly)
    degree = max((a for a, b in poly), default=0)
    ordinary = [F(0)] * (degree + 1)
    for (a, _), c in poly.items():
        for k in range(a + 1):
            ordinary[k] += c * comb(a, k) * left**(a - k) * width**k
    return [sum((ordinary[k] * F(comb(j, k), comb(degree, k))
                 for k in range(j + 1)), F(0)) for j in range(degree + 1)]


d, U, A, p, beta, c0 = F(5, 4), F(121, 64), F(27, 10), F(3, 10), F(2, 5), F(1, 8)
T, X = {(1, 0): F(1)}, {(0, 1): F(1)}
T2, X2 = mul(T, T), mul(X, X)
L = add(const(d*d), scale(T, 2*d*p), scale(T2, F(1, 4)))
B = add(const(U*U/4), scale(T, 2*U*p*d), scale(T2, d*d))
Et = add(const(U/4), scale(T, 2*d*p), scale(T2, F(1, 4)))
Ut = sub(const(U), T2)
C, H = d*d-U/4, 2*beta*(d*d-U/4)
Np = add(B, scale(mul(T, X), -2*U*beta), mul(T2, X2))
Nm = add(B, scale(mul(T, X), 2*U*beta), mul(T2, X2))
Dp = add(L, scale(mul(T, X), -2*beta), X2)
Dm = add(L, scale(mul(T, X), 2*beta), X2)
variable_numerator = mul(X, sub(scale(T, H), mul(Et, X)))
identities = {
    "modulus_expansion_4": sub(sub(mul(L, Nm), mul(B, Dm)), mul(Ut, variable_numerator)),
    "sign_comparison": sub(sub(mul(Np, Dm), mul(Nm, Dp)),
                           scale(mul(T, X, Ut, add(const(C), X2)), -4*beta)),
    "derivative_numerator": sub(sub(mul(dx(variable_numerator), Dm), mul(variable_numerator, dx(Dm))),
                                sub(sub(scale(mul(T, L), H), scale(mul(Et, L, X), 2)),
                                    mul(add(scale(T, H), scale(mul(T, Et), 2*beta)), X2))),
    "monotonicity_margin": sub(sub(scale(Et, F(3, 5)), scale(T, H)),
                               add(const(F(3, 256)), mul(sub(const(1), T), sub(const(F(87, 320)), scale(T, F(3, 20)))))),
    "square_completion": sub(sub(scale(T2, H*H), scale(mul(Et, variable_numerator), 4)),
                             mul(sub(scale(mul(Et, X), 2), scale(T, H)), sub(scale(mul(Et, X), 2), scale(T, H)))),
}
for name, residual in identities.items():
    check(name, not residual, residual={str(k): rat(v) for k, v in residual.items()})

original_bytes = OLD.read_bytes()
original = json.loads(original_bytes)
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(SOURCE.read_text(), str(SOURCE), "exec"),
         {"__name__": "__main__", "__file__": str(REPLAY.with_suffix(".py"))})
replayed = json.loads(REPLAY.read_text())
check("complete_original_replay", replayed == original)
check("original_preserved", OLD.read_bytes() == original_bytes)
cells, scale_value = original["cells"], int(original["rounding_scale"])
rows = original["cell_upper_bounds"]
check("complete_partition", cells == 2048 and len(rows) == cells and
      [row["cell"] for row in rows] == list(range(cells)))
check("positive_denominator_constants", d > 0 and U-1 > 0 and d-A/5 > 0 and C > 0)

tail_num = at_x(mul(Ut, variable_numerator), F(2, 5))
tail_den = scale(at_x(mul(B, Dm), F(2, 5)), 2)
global_num = scale(mul(Ut, T2), H*H)
global_den = scale(mul(Et, B, L), 8)
Dtilt = add(const(d-A/5), scale(T, p))
Ntilt = add(scale(mul(T, Dtilt), 2), Ut)
tilt_den = scale(mul(Dtilt, Dtilt, B), 4)
tilt_num = mul(L, Ntilt, Ntilt)
cell_proofs = []
cell_failures = []
coefficient_count = 0
for row in rows:
    j = row["cell"]
    tail = F(row["tail_upper_scaled"], scale_value)
    glob = F(row["global_upper_scaled"], scale_value)
    tilt = F(row["tilt_upper_scaled"], scale_value)
    proof = {"cell": j, "left": rat(F(j, cells)), "right": rat(F(j+1, cells))}
    polynomials = {
        "tail": sub(scale(tail_den, tail), tail_num),
        "global": sub(scale(global_den, glob), global_num),
        "tilt_squared": sub(scale(tilt_den, tilt*tilt), tilt_num),
    }
    if tilt < 0:
        cell_failures.append({"cell": j, "bound": "negative_tilt_upper"})
    for name, poly in polynomials.items():
        coefficients = bernstein(poly, F(j, cells), F(1, cells))
        coefficient_count += len(coefficients)
        proof[name] = [rat(v) for v in coefficients]
        if min(coefficients) < 0:
            cell_failures.append({"cell": j, "bound": name})
    cell_proofs.append(proof)
check("all_cell_polynomial_certificates", not cell_failures,
      intervals=cells, inequalities=3*cells, coefficients=coefficient_count,
      failed_cells=cell_failures)

for index, (key, threshold) in enumerate([
    ("tail_upper_scaled", F(-1, 400)),
    ("global_upper_scaled", F(1, 125)),
    ("tilt_upper_scaled", F(3, 2)),
]):
    actual = F(sum(row[key] for row in rows), cells*scale_value)
    stored = original["checks"][index]
    check(stored["name"], actual < threshold and actual == read_rat(stored["actual_upper"])
          and threshold == read_rat(stored["required_strict_upper"]),
          actual_upper=rat(actual), required_strict_upper=rat(threshold))

scalar_cases = [
    (F(67,6050)-F(1,120), F(1,400)),
    (c0*(U-1)/((d+1)*(U+d))-F(1,5000), F(1,100)),
    (1+F(41,100)+F(41,100)**2/2+F(41,100)**3/6, F(3,2)),
    (F(9,20)-A/(8*15), F(2,5)),
]
for index, (actual, threshold) in enumerate(scalar_cases, start=3):
    stored = original["checks"][index]
    check(stored["name"], actual > threshold and actual == read_rat(stored["actual"])
          and threshold == read_rat(stored["required_strict_lower"]),
          actual=rat(actual), required_strict_lower=rat(threshold))

failures = [item["name"] for item in checks if not item["passed"]]
result = {
    "status": "EXACT_INDEPENDENT_AUDIT" if not failures else "AUDIT_FAILURE",
    "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "original_certificate_sha256": hashlib.sha256(original_bytes).hexdigest(),
    "checks": checks, "failures": failures,
    "cell_proofs": cell_proofs,
    "qualification": "Exact algebra and full interval/scalar certificate only; the analytic reductions are audited in L723 Section 7.",
}
OUT.write_text(json.dumps(result, indent=2)+"\n")
for item in checks:
    message = f'{item["name"]}: {"PASS" if item["passed"] else "FAIL"}'
    if "actual_upper" in item:
        message += f' actual <= {read_rat(item["actual_upper"])}; required < {read_rat(item["required_strict_upper"])}'
    elif "actual" in item:
        message += f' actual = {read_rat(item["actual"])}; required > {read_rat(item["required_strict_lower"])}'
    print(message)
print(f'complete cells = {cells}; polynomial inequalities = {3*cells}; exact Bernstein coefficients = {coefficient_count}')
print("failures =", failures)
print("audit =", OUT)
print("replay =", REPLAY)
if failures:
    raise SystemExit(1)
