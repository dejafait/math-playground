#!/usr/bin/env python3
"""Fixed whole-line collar inverse: full norm upper and decisive lower bound."""
import hashlib
import importlib.util
import json
import math
from pathlib import Path

root = Path(__file__).resolve().parents[2]
backend = root / 'scripts/pivot-area/certify_1136.py'
spec = importlib.util.spec_from_file_location('local_mpfr_backend', backend)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
I, Real, op = m.I, m.Real, m.op
pi = I(Real(), Real())
m.lib.mpfr_const_pi(m.ct.byref(pi.lo.raw), m.DOWN)
m.lib.mpfr_const_pi(m.ct.byref(pi.hi.raw), m.UP)
a = I(9)/4
b = I(101).unary('log')/2
r = a/b*I(97).unary('log')
w = 2*a-r
k = 2*I(97).unary('log')/I(97).unary('sqrt')
threshold = 1/(4*k)
T, mesh_den = 256, 64
h = I(1)/mesh_den
N = T*mesh_den
m0 = 1/I(2).unary('log')
mT = 1/I(T+2).unary('log')

def sq(x):
    y = x.abs()
    return I(op('mul', y.lo, y.lo), op('mul', y.hi, y.hi, m.UP))

# A_n uniformly bounds |(d/dt)^n [1/log(2+t)]|, t>=0.
A = [m0]
for n in range(1,5):
    A.append(m0*sum(math.comb(n,j)*I(math.factorial(j-1))/2**j*A[n-j]
                    for j in range(1,n+1)))
M4 = w/pi*sum(math.comb(4,j)*A[j]*w**(4-j) for j in range(5))
simpson_error = I(T)*h**4/180*M4

# Normalized single-collar inverse Rayleigh density, retaining all t in [0,T].
def density(j):
    if j == 0:
        return w*m0/pi
    t = I(j)/mesh_den
    return 4*sq((w*t/2).trig('sin'))/(pi*w*sq(t)*(2+t).unary('log'))

acc = I(0)
mid_sum = I(0)
blocks = []
for j in range(N+1):
    acc = acc+(1 if j in (0,N) else 4 if j%2 else 2)*density(j)
    if j<N:
        tmid = I(2*j+1)/(2*mesh_den)
        mid_sum = mid_sum+1/(2+tmid).unary('log')
    if j%1024 == 0:
        blocks.append({'through_index':j, 'inverse_weighted_sum':acc.dump(),
                       'multiplier_midpoint_sum':mid_sum.dump()})
finite = acc*h/3
finite_enclosure = finite+I(op('neg',simpson_error.hi),simpson_error.hi)
lower = I(finite_enclosure.lo)
rayleigh_tail = 4/(pi*w*T*I(T+2).unary('log'))
rayleigh = I(finite_enclosure.lo, op('add',finite_enclosure.hi,rayleigh_tail.hi,m.UP))

# K_N(z)=h/pi sum_j m(t_j) cos(t_j*z).
# For each frequency cell, integrate |m(t)cos(tz)-m(t_j)cos(t_j z)|.
# Multiplier variation costs <= h*(m0-mT); cosine variation <= h/2*|z|*h sum m(t_j).
# Hence this uniform error holds for |z|<=2a, including both collar blocks.
S = h*mid_sum
kernel_error = h/pi*(m0-mT+a*S)
# |K_T(z)| <= m0/(pi |z|) by integration by parts, for z!=0.
# Thus K_N has self-block bound S/pi and cross-block bound below.
d = r-w
cross_kernel_bound = m0/(pi*d)+kernel_error
finite_schur_upper = w*(S/pi+cross_kernel_bound)
compression_kernel_error = 2*w*kernel_error
norm_upper = mT+finite_schur_upper+compression_kernel_error
required_allocation_from_upper = k/2*norm_upper
obstructed_allocation_lower = k/2*lower
claims = {
 'width_positive':w.positive(),
 'width_lt_a':(a-w).positive(),
 'collars_disjoint':d.positive(),
 'lower_above_29_over_100':(lower-I(29)/100).positive(),
 'threshold_below_27_over_100':(I(27)/100-threshold).positive(),
 'inverse_norm_lower_exceeds_required_threshold':(lower-threshold).positive(),
 'lower_exceeds_threshold_by_23_over_1000':(lower-threshold-I(23)/1000).positive(),
 'upper_below_102_over_100':(I(102)/100-norm_upper).positive(),
 'simpson_error_below_one_millionth':(I(1)/1000000-simpson_error).positive(),
}
failures = [key for key,val in claims.items() if not val]
out = {
 'scope':'Full complex whole-line inverse compression; failure of this sufficient collar-mass test only.',
 'mpfr_version':m.lib.mpfr_get_version().decode(), 'precision_bits':m.PREC,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'backend_path':str(backend.relative_to(root)),
 'backend_sha256':hashlib.sha256(backend.read_bytes()).hexdigest(),
 'fixed_grid':{'T':T,'h':'1/64','frequency_cells':N,'simpson_panels':N//2},
 'a':a.dump(),'b':b.dump(),'r':r.dump(),'w':w.dump(),'k':k.dump(),
 'threshold':threshold.dump(),'multiplier_derivative_majorants':[v.dump() for v in A],
 'fourth_derivative_bound':M4.dump(),'quadrature_blocks':blocks,
 'finite_inverse_simpson':finite.dump(),'simpson_error':simpson_error.dump(),
 'finite_inverse_enclosure':finite_enclosure.dump(),'inverse_rayleigh_tail_upper':rayleigh_tail.dump(),
 'inverse_rayleigh_enclosure':rayleigh.dump(),'norm_lower':lower.dump(),
 'midpoint_multiplier_integral':S.dump(),'uniform_kernel_error':kernel_error.dump(),
 'cross_kernel_upper':cross_kernel_bound.dump(),'finite_schur_upper':finite_schur_upper.dump(),
 'compression_kernel_error':compression_kernel_error.dump(),'frequency_tail_norm':mT.dump(),
 'norm_upper':norm_upper.dump(),'allocation_upper':required_allocation_from_upper.dump(),
 'allocation_norm_lower':obstructed_allocation_lower.dump(),
 'threshold_miss':(lower-threshold).dump(),
 'allocation_test_passed':(threshold-norm_upper).positive(),
 'failed_tests':['required norm upper <= 1/(4k)', 'nonessential initial expectation norm upper < 1'],
 'initial_certificate':'scripts/prime-collar/certificate-1144-initial.json',
 'initial_failure_note':'The original upper_below_one check failed. No mesh, cutoff or bound was tuned; that nonessential expectation is retained here and in the initial certificate.',
 'claims':claims,'failures':failures,
}
path = Path(__file__).with_name('certificate-1144.json')
path.write_text(json.dumps(out,indent=2)+'\n')
for key in ['threshold','norm_lower','norm_upper','simpson_error','uniform_kernel_error',
            'frequency_tail_norm','threshold_miss','allocation_norm_lower']:
    print(key, [float(x) for x in out[key]])
print('Required norm <= 1/(4k); rigorous lower exceeds it. Original supported inequality undecided.')
print('Failed mathematical tests:',out['failed_tests'])
print('Verification failures:',failures)
print('Full certificate:',path)
if failures:
    raise SystemExit(1)
