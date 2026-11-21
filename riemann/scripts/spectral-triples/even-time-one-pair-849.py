"""One fixed even time-one evolution attempt. All sampled data are diagnostic.

NPZ binary64 values define exact dyadic modal data. The exact candidate is
v + sum_j expm1(-lambda_j*t)*f_j. Thus its initial value is EXACTLY v,
regardless of floating diagonalization error. No quadrature/sample is a
certificate of the infinite-dimensional defect or of B_1.
"""
from pathlib import Path
import hashlib
import json
import math
import numpy as np
from numpy.polynomial.legendre import leggauss, legvander, legval

ROOT = Path(__file__).parent
STEM = Path(__file__).stem
DIM, DEG, ORDER = 256, 510, 1024


def bump(x, center):
    return np.maximum(1-(40*(x-center))**2, 0)**2


def quartic(x, center):
    return bump(x, center)+bump(x, -center)


def smooth_kernel(r):
    small = r < 1.e-3
    z = np.where(small, 1., r)
    k = np.exp(z/2)/(2*np.sinh(z))-1/(2*z)
    s = r[small]
    k[small] = .25-s/48-s*s/32+7*s**3/11520+5*s**4/1536
    return k


# 255 prescribed polynomials, together with v, give the one allowed W.
B = np.zeros((DEG+1, DIM-1))
for j in range(DIM-1):
    n = 2*j
    a, d = (n+1)/(2*n+1), n/(2*n+1)
    B[n, j] = 1-a*(n+1)/(2*n+3)
    B[n+2, j] = -a*(n+2)/(2*n+3)
    if n:
        B[n, j] -= d*n/(2*n-1)
        B[n-2, j] = -d*(n-1)/(2*n-1)
H = np.concatenate(([0.], np.cumsum(1/np.arange(1, DEG+1))))
x, wx = leggauss(ORDER)
poly = legvander(x, DEG)@B
xp, wp = leggauss(272)
support = np.concatenate((-.8+xp/40, .8+xp/40))
support_w = np.tile(wp/40, 2)
support_v = np.tile((1-xp*xp)**2, 2)
mass_v = 64/1575


def polynomial_action(z):
    p = legvander(z, DEG)@B
    a = legvander(z, DEG)@(H[:, None]*B)
    a += (-np.euler_gamma-math.log(2*math.pi)
          -.5*np.log1p(-z*z))[:, None]*p
    a -= smooth_kernel(np.abs(z[:, None]-x[None, :]))@(wx[:, None]*poly)
    for n in (2, 3, 4, 5, 7):
        delay = math.log(n)
        prime_a = math.log(2 if n == 4 else n)/math.sqrt(n)
        for sign in (-1, 1):
            y = z+sign*delay
            mask = np.abs(y) < 1
            a[mask] -= prime_a*(legvander(y[mask], DEG)@B)
    pole_moments = (wx*np.cosh(x/2))@poly
    a += 2*np.cosh(z/2)[:, None]*pole_moments
    return a


def v_arch_action(z):
    # Diagnostic finite-part integral for the piecewise quartic, including
    # the complete singular term and the smooth kernel. No validated
    # quadrature or floating error bound is claimed for this formula.
    val = np.zeros_like(z)
    outside_rule, outside_weights = leggauss(64)
    outside_h = (1-outside_rule**2)**2
    for center in (-.8, .8):
        zz = 40*(z-center)
        inside = np.abs(zz) < 1
        zi = zz[inside]
        # Primitive of (h(s)-h(zi))/(s-zi).
        def primitive(s):
            return s**4/4+zi*s**3/3+(zi*zi-2)*s*s/2+(zi**3-2*zi)*s
        quotient_integral = primitive(1)+primitive(-1)-2*primitive(zi)
        hh = (1-zi*zi)**2
        val[inside] += (-np.euler_gamma-math.log(2*math.pi)
                       -.5*np.log((1-zi*zi)/1600))*hh
        val[inside] -= .5*quotient_integral
        # Gauss integral of h(s)/|s-zz| outside this bump. It remains
        # diagnostic even though the integrand is positive and smooth.
        zo = zz[~inside]
        val[~inside] -= .5*((outside_weights*outside_h)[None, :]
                           /np.abs(zo[:, None]-outside_rule[None, :])).sum(axis=1)
    val -= smooth_kernel(np.abs(z[:, None]-support[None, :]))@(support_w*support_v)
    return val


def v_action(z):
    a = v_arch_action(z)
    for n in (2, 3, 4, 5, 7):
        delay = math.log(n)
        prime_a = math.log(2 if n == 4 else n)/math.sqrt(n)
        for sign in (-1, 1):
            y = z+sign*delay
            a -= prime_a*quartic(y, .8)*(np.abs(y) < 1)
    pole_moment = (support_w*support_v)@np.cosh(support/2)
    a += 2*np.cosh(z/2)*pole_moment
    return a


M = np.empty((DIM, DIM))
M[0, 0] = mass_v
vpoly = (support_w*support_v)@(legvander(support, DEG)@B)
M[0, 1:] = M[1:, 0] = vpoly
M[1:, 1:] = B.T@((2/(2*np.arange(DEG+1)+1))[:, None]*B)
Q = np.empty_like(M)
Q[0, 0] = (support_w*support_v)@v_action(support)
Q[0, 1:] = Q[1:, 0] = (support_w*support_v)@polynomial_action(support)
Q[1:, 1:] = poly.T@(wx[:, None]*polynomial_action(x))
asymmetry = float(np.max(np.abs(Q-Q.T)))
Q = (Q+Q.T)/2
chol = np.linalg.cholesky(M)
scaled = np.linalg.solve(chol, Q)
scaled = np.linalg.solve(chol, scaled.T).T
scaled = (scaled+scaled.T)/2
eigenvalues, eigenvectors = np.linalg.eigh(scaled)
initial = chol.T[:, 0]
amplitudes = eigenvectors.T@initial
modal = np.linalg.solve(chol.T, eigenvectors*amplitudes[None, :])
assert eigenvalues.shape == (DIM,) and modal.shape == (DIM, DIM)
assert np.isfinite(eigenvalues).all() and np.isfinite(modal).all()

# These exact binary64 values are interpreted as dyadic real constants in
# the candidate definition; w(0)=v is an identity, not a floating test.
data_path = ROOT/(STEM+'.npz')
np.savez(data_path, eigenvalues=eigenvalues, modal_coefficients=modal,
         assembly_mass_DIAGNOSTIC=M, assembly_form_DIAGNOSTIC=Q)

def candidate(t):
    coeff = modal@np.expm1(-eigenvalues*t)
    coeff[0] += 1
    derivative = modal@(-eigenvalues*np.exp(-eigenvalues*t))
    return coeff, derivative

# Testing u on its own compact supports avoids a coarse global sampling.
u_support = np.concatenate((-.2+xp/40, .2+xp/40))
u_row = np.empty(DIM)
u_row[0] = 0.0  # exact disjoint supports
u_row[1:] = (support_w*support_v)@(legvander(u_support, DEG)@B)
one_coeff, _ = candidate(1.)
center = float(u_row@one_coeff)

# Sample the COMBINED complete defect, not separate norm majorants.
# Independent spatial grid; time samples are not quadrature certificates.
rx, rw = leggauss(1536)
values = np.column_stack((quartic(rx, .8), legvander(rx, DEG)@B))
actions = np.column_stack((v_action(rx), polynomial_action(rx)))
tt, wt = leggauss(64)
tt, wt = (tt+1)/2, wt/2
defect_samples = []
weighted_integral_sample = 0.
for t, weight in zip(tt, wt):
    coeff, derivative = candidate(float(t))
    defect = values@derivative+actions@coeff
    defect_norm = float(np.sqrt(rw@(defect*defect)))
    defect_samples.append({'t': float(t), 'L2_norm_NOT_CERTIFIED': defect_norm})
    weighted_integral_sample += weight*math.exp(10*(1-t))*defect_norm
sample_radius = math.sqrt(mass_v)*weighted_integral_sample

result = {
    'status': 'INCONCLUSIVE_NOT_A_SIGN_CERTIFICATE',
    'scope': {'dimension': DIM, 't': 1, 'polynomial_even_degrees': [0, 508],
              'prime_powers': [2, 3, 4, 5, 7], 'both_poles': True,
              'pair': 'C759i(2)', 'space': 'assessment847/848 W',
              'space_time_or_pair_sweep': False},
    'exact_candidate': {
        'data': data_path.name, 'sha256': hashlib.sha256(data_path.read_bytes()).hexdigest(),
        'data_interpretation': 'Each stored binary64 lambda/modal entry is its exact dyadic value.',
        'basis_order': 'v, (1-x^2)P_0, (1-x^2)P_2, ..., (1-x^2)P_508',
        'definition': 'w(t)=v+sum_j (exp(-lambda_j*t)-1)*f_j; f_j has modal_coefficients[:,j]',
        'initial_identity': 'w(0)=v exactly',
        'regularity': 'Finite real analytic time coefficients in W subset D(A_e); A_e w is continuous.',
        'not_claimed': 'Stored approximate eigendata need not exactly diagonalize the assembled Galerkin matrix.'},
    'defect_identity': {
        'source': 'Jacob-Zwart ISEM2010-11 Lemma10.1.2, p120, via assessment847/848',
        'exact_error_bound': '|B_1-<u,w(1)>| <= sqrt(64/1575)*integral_0^1 exp(10*(1-t))*||w\u0027(t)+A_e w(t)||_2 dt',
        'initial_error': 0,
        'required_for_negative_upper_endpoint': 'A certified center upper bound b<0 and a complete error upper bound E<-b.'},
    'diagnostic_NOT_CERTIFIED': {
        'pair_center': center,
        'matrix_asymmetry_before_symmetrizing': asymmetry,
        'mass_min_eigenvalue': float(np.linalg.eigvalsh(M)[0]),
        'compressed_eigenvalue_range': [float(eigenvalues[0]), float(eigenvalues[-1])],
        'initial_reconstruction_L2_sample': float(np.sqrt(max(0, (modal.sum(axis=1)-np.eye(DIM)[0])@M@(modal.sum(axis=1)-np.eye(DIM)[0])))),
        'combined_defect_samples': defect_samples,
        'floor_weighted_error_radius_sample': sample_radius,
        'sample_interval_NOT_AN_ENCLOSURE': [center-sample_radius, center+sample_radius]},
    'certification': {
        'B1_enclosure': None, 'full_defect_bound': None,
        'finite_spatial_quadrature_validated': False,
        'complete_action_identity_for_quartic_independently_validated': False,
        'fourier_or_spatial_tail_bound_evaluated': False,
        'time_quadrature_validated': False, 'roundoff_enclosure': False,
        'all_error_terms_paid': False,
        'failure': 'The complete sampled defect is not a bound. No rigorously negative center or paid full error radius is available.'},
    'data_integrity': {'finite_exact_dyadic_constants': True,
                       'eigenvalue_count': DIM, 'modal_shape': [DIM, DIM],
                       'dimension_check': 'one quartic plus 255 even endpoint-vanishing polynomials'},
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
out = ROOT/(STEM+'.json')
out.write_text(json.dumps(result, indent=2)+'\n')
print('Fixed W dimension:', DIM, '; t=1; no sweep')
print('Diagnostic pairing:', center)
print('Diagnostic combined-defect weighted radius:', sample_radius)
print('Required: rigorous center b<0 and complete radius E<-b; achieved: neither certified')
print('FAIL: spatial/tail/time/roundoff certificates unpaid; no B_1 enclosure')
print('Records:', out, data_path)
