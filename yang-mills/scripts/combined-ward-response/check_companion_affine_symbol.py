"""Exact affine stencil checks for L042; no numerical cutoff assertion."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

ZERO = (0, 0, 0)


def shift(n, j, sign):
    return tuple(x + (sign if k == j else 0) for k, x in enumerate(n))


def add(*polys):
    out = {}
    for p in polys:
        for k, value in p.items():
            out[k] = out.get(k, F(0)) + value
    return {k: v for k, v in out.items() if v}


def scale(c, p):
    return {k: c*v for k, v in p.items() if c*v}


def mul(p, q):
    out = {}
    for k, v in p.items():
        for ell, w in q.items():
            key = tuple(x+y for x, y in zip(k, ell))
            out[key] = out.get(key, F(0)) + v*w
    return {k: v for k, v in out.items() if v}


one = {ZERO: F(1)}
ts = [add({shift(ZERO, j, 1): F(1, 2)},
          {shift(ZERO, j, -1): F(-1, 2)}) for j in range(3)]
cs = [add({shift(ZERO, j, 1): F(1, 2)},
          {shift(ZERO, j, -1): F(1, 2)}) for j in range(3)]
ls = [add(scale(2, one), scale(-2, cs[j])) for j in range(3)]
lam = add(*ls)


def central(f, n, j):
    return (f(shift(n, j, 1)) - f(shift(n, j, -1)))/2


def lap(f, n, j=None):
    axes = range(3) if j is None else (j,)
    return sum(2*f(n)-f(shift(n, k, 1))-f(shift(n, k, -1)) for k in axes)


def direct_row(matrix, constant):
    # With a=1, u_k(n)=constant_k+sum_j M_jk n_j. This is the
    # exact affine rescaling u_k(x+a*n)/a in the residual stencils.
    def u(n, k):
        return constant[k]+sum(matrix[j][k]*n[j] for j in range(3))

    def transport(f, n):
        return sum(u(n, k)*central(f, n, k) for k in range(3))

    def transport_adj(f, n):
        return -sum(central(lambda y: u(y, k)*f(y), n, k) for k in range(3))

    def residual(f, n):
        sym = (lap(lambda y: transport(f, y), n)
               + transport_adj(lambda y: lap(f, y), n))/2
        q3 = sum(matrix[j][j]*lap(f, n, j) for j in range(3))
        q6 = -sum((matrix[j][k]+matrix[k][j])
                  * central(lambda y: central(f, y, k), n, j)
                  for j in range(3) for k in range(j+1, 3))
        return sym-q3-q6

    row = {}
    # Every composed stencil has l1 radius at most 2; this cube
    # contains its entire support, not just sampled coefficients.
    for offset in product(range(-2, 3), repeat=3):
        value = residual(lambda n: F(n == offset), ZERO)
        if value:
            row[offset] = value
    return row


def formula_row(w):
    return add(*(scale(w[j], add(scale(-1, mul(ts[j], ts[j])),
                                scale(-1, ls[j]),
                                scale(F(-1, 2), mul(lam, cs[j]))))
                 for j in range(3)))


def serialized(p):
    return [{"offset": list(k), "coefficient": str(v)} for k, v in sorted(p.items())]


records = []
for j, k in product(range(3), repeat=2):
    matrix = [[F(r == j and s == k) for s in range(3)] for r in range(3)]
    actual = direct_row(matrix, [F(0)]*3)
    expected = formula_row([matrix[r][r] for r in range(3)])
    defect = add(actual, scale(-1, expected))
    records.append(dict(check="affine_derivative_basis", derivative=j+2,
                        component=k+2, actual=serialized(actual),
                        expected=serialized(expected), defect=serialized(defect),
                        passed=not defect))
for k in range(3):
    actual = direct_row([[F(0)]*3 for _ in range(3)], [F(j == k) for j in range(3)])
    records.append(dict(check="constant_transport", component=k+2,
                        actual=serialized(actual), expected=[], defect=serialized(actual),
                        passed=not actual))
for w in ([1, -1, 0], [1, 0, -1]):
    actual = formula_row(w)
    expected = add(*(scale(F(w[j], 4), mul(ls[j], add(lam, scale(-1, ls[j]))))
                     for j in range(3)))
    defect = add(actual, scale(-1, expected))
    records.append(dict(check="trace_free_reduction", w=w,
                        actual=serialized(actual), expected=serialized(expected),
                        defect=serialized(defect), passed=not defect))
diff = add(ls[0], scale(-1, ls[1]))
numerator = mul(mul(ls[0], ls[2]), diff)
permuted = scale(-1, mul(mul(ls[1], ls[2]), diff))
positive = mul(ls[2], mul(diff, diff))
defect = add(numerator, permuted, scale(-1, positive))
records.append(dict(check="positive_constant_permutation_numerator",
                    actual=serialized(add(numerator, permuted)),
                    expected=serialized(positive), defect=serialized(defect),
                    passed=not defect))
failures = [r for r in records if not r["passed"]]
certificate = dict(
    scope="Complete finite Laurent identities only; no cutoff rate or signed companion limit certified.",
    records=records, failures=failures, passed=not failures,
    actual_maximum_coefficient_defect="0" if not failures else "nonzero",
    required_maximum_coefficient_defect="0",
    analytic_result="L042 proves a^4 T_i,a tends to zero; the finite checks do not establish this limit.",
    required_asymptotic_threshold="Control stronger powers before an a^2-scaled limit; cancellation would require +48 I_i.",
)
path = Path(__file__).with_name("companion-affine-symbol-certificate.json")
path.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"Exact identity records: {len(records)}; failures: {len(failures)}")
print("Actual/required maximum coefficient defect:", certificate["actual_maximum_coefficient_defect"], "/ 0")
print("Asymptotic requirement still open: control above a^-2, then compare with +48 I_i.")
print("Certificate:", path)
if failures:
    raise SystemExit(1)
