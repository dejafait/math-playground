"""One prescribed rational logarithmic Hankel test; no parameter sweep."""
from fractions import Fraction as Q
from pathlib import Path
import json


def encoded(x):
    return {"numerator": x.numerator, "denominator": x.denominator}


e = [Q(1)]
gamma = [Q(1)]
for n in range(1, 5):
    # e_n = (3/2)_n / ((1)_n (100)_n n! 4^n).
    e.append(e[-1] * (Q(3, 2) + n - 1) / (4*n*n*(100+n-1)))
    gamma.append(gamma[-1] * (Q(3, 2) + n - 1) / (4*n*(100+n-1)))

# G=1+sum a_n w^n, G'=-G sum S_k w^(k-1).
a = [(-1)**n * e[n] for n in range(5)]
S = [Q(0)]
recurrence_residuals = []
for k in range(1, 5):
    S.append(-k*a[k] - sum(a[j]*S[k-j] for j in range(1, k)))
    recurrence_residuals.append(k*a[k] + sum(a[j]*S[k-j] for j in range(k)))

# Independently calculate the formal logarithm through degree four.
log_coefficients = [Q(0)]*5
power = [Q(1)] + [Q(0)]*4
x = [Q(0)] + a[1:]
for j in range(1, 5):
    power = [sum(power[i]*x[k-i] for i in range(k+1)) for k in range(5)]
    for k in range(1, 5):
        log_coefficients[k] += Q((-1)**(j+1), j)*power[k]
log_residuals = [S[k] + k*log_coefficients[k] for k in range(1, 5)]

H = [[S[2], S[3]], [S[3], S[4]]]
det = S[2]*S[4] - S[3]**2
v = [S[3], -S[2]]
form = sum(v[i]*H[i][j]*v[j] for i in range(2) for j in range(2))
checks = {
    "normalization": e[0] == gamma[0] == 1,
    "factorial_normalization": all(gamma[n] == e[n]*__import__('math').factorial(n) for n in range(5)),
    "recurrence_exact": all(r == 0 for r in recurrence_residuals),
    "independent_formal_log_agreement": all(r == 0 for r in log_residuals),
    "S2_positive": S[2] > 0,
    "determinant_negative": det < 0,
    "witness_identity": form == S[2]*det,
    "witness_negative": form < 0,
}
certificate = {
    "target": "1F2(3/2;1,100;-t^2/4), H_1 only",
    "arithmetic": "exact fractions; no floating-point inputs",
    "e_0_to_4": list(map(encoded, e)),
    "gamma_0_to_4": list(map(encoded, gamma)),
    "S_1_to_4": list(map(encoded, S[1:])),
    "log_coefficients_1_to_4": list(map(encoded, log_coefficients[1:])),
    "H_1": [[encoded(x) for x in row] for row in H],
    "determinant": encoded(det),
    "required_determinant_upper_threshold": encoded(Q(0)),
    "witness": list(map(encoded, v)),
    "witness_quadratic_form": encoded(form),
    "recurrence_residuals": list(map(encoded, recurrence_residuals)),
    "formal_log_residuals": list(map(encoded, log_residuals)),
    "checks": checks,
    "failures": [k for k, ok in checks.items() if not ok],
}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(certificate, indent=2) + '\n')
print(f"det(H_1)={det}; required <0; S2={S[2]}")
print(f"witness form={form}; required <0")
print(f"checks={len(checks)}, failures={certificate['failures']}; certificate={path}")
if certificate['failures']:
    raise SystemExit(1)
