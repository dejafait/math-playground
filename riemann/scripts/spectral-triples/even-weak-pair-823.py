"""One fixed 256-dimensional even resolvent diagnostic and honest certificate.

The real-space assembly and sampled full residual are DIAGNOSTIC ONLY.
An exact dyadic polynomial candidate and rational full-residual majorant
are separately recorded. No quadrature accuracy is inferred from samples.
See C759h for the operator action, rigorous bounds and limitations.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import math
import numpy as np
from numpy.polynomial.legendre import leggauss, legvander, legval

DIM = 256
ORDER = 1024
NDEG = 2*DIM
outpath = Path(__file__).with_suffix('.json')


def bump(x, center):
    return np.maximum(1-(40*(x-center))**2, 0)**2


def uv(x, center):
    return bump(x, center)+bump(x, -center)


def basis_coefficients():
    b = np.zeros((NDEG+1, DIM))
    for j in range(DIM):
        n = 2*j
        a = (n+1)/(2*n+1)
        d = n/(2*n+1)
        b[n, j] = 1-a*(n+1)/(2*n+3)
        b[n+2, j] = -a*(n+2)/(2*n+3)
        if n:
            b[n, j] -= d*n/(2*n-1)
            b[n-2, j] = -d*(n-1)/(2*n-1)
    return b


def kernel(r):
    # Continuous k(0)=1/4; expansion avoids cancellation near zero.
    small = r < 1.e-3
    z = np.where(small, 1., r)
    k = np.exp(z/2)/(2*np.sinh(z))-1/(2*z)
    s = r[small]
    k[small] = .25-s/48-s*s/32+7*s**3/11520+5*s**4/1536
    return k


B = basis_coefficients()
x, weights = leggauss(ORDER)
V = legvander(x, NDEG)
Psi = V @ B
H = np.concatenate(([0.], np.cumsum(1/np.arange(1, NDEG+1))))
K = kernel(np.abs(x[:, None]-x[None, :]))*weights[None, :]
potential = -0.5772156649015328606-math.log(2*math.pi)-.5*np.log1p(-x*x)
Act = V @ (H[:, None]*B)+potential[:, None]*Psi-K@Psi
for n in (2, 3, 4, 5, 7):
    d = math.log(n)
    a = math.log(2 if n == 4 else n)/math.sqrt(n)
    for sign in (-1, 1):
        y = x+sign*d
        valid = np.abs(y) < 1
        shifted = np.zeros_like(Psi)
        shifted[valid] = legvander(y[valid], NDEG)@B
        Act -= a*shifted
c = np.cosh(x/2)
Act += 2*c[:, None]*(weights*c)@Psi
mass = Psi.T@(weights[:, None]*Psi)
mat = Psi.T@(weights[:, None]*(Act+16*Psi))

# Integrate the fixed compact quartic forcing on its actual supports.
t, tw = leggauss(272)
rhs = np.zeros(DIM)
vrow = np.zeros(DIM)
for center, row in ((.2, rhs), (.8, vrow)):
    for sign in (-1, 1):
        z = sign*center+t/40
        row += (tw*(1-t*t)**2/40)@(legvander(z, NDEG)@B)
chol = np.linalg.cholesky(mass)
sym_defect = float(np.max(np.abs(mat-mat.T)))
mat = (mat+mat.T)/2
scaled = np.linalg.solve(chol, mat)
scaled = np.linalg.solve(chol, scaled.T).T
scaled_rhs = np.linalg.solve(chol, rhs)
zcoef = np.linalg.solve(scaled, scaled_rhs)
coef = np.linalg.solve(chol.T, zcoef)
pair_diagnostic = float(vrow@coef)

# Independently sample the complete physical residual at a different grid.
# This is never used as a rigorous residual bound.
rx, rw = leggauss(1536)
wc = B@coef
wv = legval(rx, wc)
ma = legval(rx, H*wc)
ma += (-0.5772156649015328606-math.log(2*math.pi)
       -.5*np.log1p(-rx*rx))*wv
ma -= kernel(np.abs(rx[:, None]-x[None, :]))@(weights*(Psi@coef))
for n in (2, 3, 4, 5, 7):
    d = math.log(n)
    a = math.log(2 if n == 4 else n)/math.sqrt(n)
    for sign in (-1, 1):
        y = rx+sign*d
        valid = np.abs(y) < 1
        ma[valid] -= a*legval(y[valid], wc)
ma += 2*np.cosh(rx/2)*float((weights*c)@(Psi@coef))
res = uv(rx, .2)-ma-16*wv
res_norm_diagnostic = float(np.sqrt(rw@(res*res)))

# Exact dyadic candidate in the prescribed space. All following arithmetic
# is rational. Rounded-up rational square roots avoid a floating certificate.
q = [F(float(v)) for v in coef]
pol = [F(0) for _ in range(NDEG+1)]
for j, cj in enumerate(q):
    n = 2*j
    a, d = F(n+1, 2*n+1), F(n, 2*n+1)
    pol[n] += cj*(1-a*F(n+1, 2*n+3))
    pol[n+2] -= cj*a*F(n+2, 2*n+3)
    if n:
        pol[n] -= cj*d*F(n, 2*n-1)
        pol[n-2] -= cj*d*F(n-1, 2*n-1)
der = [F(0) for _ in range(NDEG)]
running = F(0)
for k in range(NDEG-1, -1, -2):
    running += pol[k+1]
    der[k] = (2*k+1)*running
norm2 = sum((F(2, 2*n+1)*a*a for n, a in enumerate(pol)), F(0))
dnorm2 = sum((F(2, 2*n+1)*a*a for n, a in enumerate(der)), F(0))


def sqrt_upper(value, digits=24):
    scale = 10**digits
    numerator = value.numerator*scale*scale
    den = value.denominator
    root = math.isqrt(numerator//den)
    if root*root*den < numerator:
        root += 1
    return F(root, scale)


wn, dwn = sqrt_upper(norm2), sqrt_upper(dnorm2)
# ||u||=||v||=sqrt(2/40 * integral_-1^1(1-s²)^4 ds).
un2 = F(64, 1575)
un = sqrt_upper(un2)
# Rational bound: symbol |m(t)| <= |t|+7; C<4; even pole norm<8.
# Hence ||u-(A+16)w|| <= ||u||+||w'||+35||w||.
res_upper = un+dwn+35*wn
# The exact integral <v,w> is also computed, not a sampled quadrature.
# Integrate Legendre polynomials against each quartic bump using the
# polynomial recurrence at x=center+s/40 and the exact weighted moments.


def v_pair_exact(center):
    # Each polynomial in s is rational; even-s moments eliminate odd terms.
    # Maximum degree 512. Dense rational recurrence is deliberately local.
    pprev = [F(1)]
    pcur = [center, F(1, 40)]
    total = F(0)
    moments = [F(0)]*(NDEG+1)
    for k in range(0, NDEG+1, 2):
        moments[k] = 2*(F(1, k+1)-2*F(1, k+3)+F(1, k+5))/40
    def integrate(p):
        return sum((p[k]*moments[k] for k in range(0, len(p), 2)), F(0))
    total += pol[0]*integrate(pprev)
    for n in range(1, NDEG+1):
        if pol[n]:
            total += pol[n]*integrate(pcur)
        if n == NDEG:
            break
        nxt = [F(0)]*(len(pcur)+1)
        fac = F(2*n+1, n+1)
        for k, value in enumerate(pcur):
            nxt[k] += fac*center*value
            nxt[k+1] += fac*value/40
        for k, value in enumerate(pprev):
            nxt[k] -= F(n, n+1)*value
        pprev, pcur = pcur, nxt
    return 2*total  # even w: the negative-center bump contributes equally


pair = v_pair_exact(F(4, 5))
error = un*res_upper/6
interval = [pair-error, pair+error]
required = 6*abs(pair)/un
checks = {
    'candidate_even_and_endpoint_zero': sum(pol) == 0 and all(
        pol[n] == 0 for n in range(1, NDEG+1, 2)),
    'u_norm_squared_direct_integral': un2 == F(1, 10)*sum(
        (F((-1)**k*math.comb(4, k), 2*k+1) for k in range(5)), F(0)),
    'norm_upper_rounding': wn*wn >= norm2 and dwn*dwn >= dnorm2 and un*un >= un2,
    'trial_pair_bracket': F('-0.00001309225721') < pair < F('-0.00001309225720'),
    'whole_residual_upper_bracket': F('1.3555247225') < res_upper < F('1.3555247227'),
    'sufficient_residual_threshold_bracket': F('0.0003896871374') < required < F('0.0003896871375'),
    'whole_resolvent_enclosure_lower_bracket': F('-0.045555') < interval[0] < F('-0.045554'),
    'whole_resolvent_enclosure_upper_bracket': F('0.045528') < interval[1] < F('0.045529'),
    'zero_in_enclosure': interval[0] < 0 < interval[1],
}
assert all(checks.values()), checks


def rational(v):
    return {'numerator': str(v.numerator), 'denominator': str(v.denominator)}


result = {
    'scope': {'dimension': DIM, 'ceiling': 256, 'parameter': -16,
              'forcing_centers': ['1/5', '4/5'], 'width': '1/40',
              'quadrature_order_DIAGNOSTIC': ORDER},
    'diagnostic_NOT_CERTIFIED': {
        'pair': pair_diagnostic, 'full_residual_sample_norm': res_norm_diagnostic,
        'symmetry_defect': sym_defect,
        'scaled_matrix_min_eigenvalue': float(np.linalg.eigvalsh(scaled)[0]),
        'sample_error_radius_using_delta6': float(un)*res_norm_diagnostic/6},
    'exact_candidate': {'basis': '(1-x^2)P_(2j), j=0..255',
                        'coefficients': [rational(a) for a in q],
                        'endpoint_sum_is_zero': sum(pol) == 0,
                        'legendre_coefficients': [rational(a) for a in pol]},
    'rational_certificate': {
        'exact_checks': checks,
        'squared_w_norm': rational(norm2), 'squared_derivative_norm': rational(dnorm2),
        'squared_u_v_norm': rational(un2),
        'w_norm_upper': rational(wn), 'derivative_norm_upper': rational(dwn),
        'pair': rational(pair), 'residual_norm_upper': rational(res_upper),
        'pair_error_upper_delta6': rational(error),
        'pair_enclosure': [rational(a) for a in interval],
        'strict_negative_test_required_residual_below': rational(required),
        'strict_negative_test_passes': interval[1] < 0,
        'strict_nonnegative_test_passes': interval[0] >= 0},
    'analytic_bounds': {'even_floor_strictly_above': -10,
                        'inverse_norm_strictly_below': '1/6',
                        'symbol_abs_bound': '|t|+7',
                        'prime_operator_norm_strictly_below': 4,
                        'even_pole_operator_norm_strictly_below': 8,
                        'complete_residual_bound': '||u||+||w_prime||+35||w||'},
    'outcome': 'INCONCLUSIVE: rigorous full-residual enclosure contains zero',
    'failures': ['No certified sharp residual norm; sampled residual is not proof.',
                 'The certified whole-residual majorant is too large for either sign.'],
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
outpath.write_text(json.dumps(result, indent=2)+'\n')
print('fixed trial dimension', DIM, '/', 256, '; endpoints zero:', sum(pol) == 0)
print('DIAGNOSTIC pair', pair_diagnostic, '; sampled residual', res_norm_diagnostic)
print('CERTIFIED pair approx', float(pair), '; full residual upper', float(res_upper))
print('required residual below', float(required), '; enclosure', [float(a) for a in interval])
print(result['outcome'])
print('failures:', '; '.join(result['failures']))
print('certificate:', outpath)
