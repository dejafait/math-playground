#!/usr/bin/env python3
"""Fixed middle indicator; full spatial-J 2x2 matrix, no parameter search.

MPFR384 endpoint rectangles on a fixed dyadic s mesh, with complete
analytic small-s and large-s allowances. Proof: canonical C750l.
"""
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / 'scripts/pivot-area/certify_1136.py'
spec = importlib.util.spec_from_file_location('mpfr_backend_1157', BACKEND)
bk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bk)
I, Real, op = bk.I, bk.Real, bk.op
pi = I(Real(), Real())
bk.lib.mpfr_const_pi(bk.ct.byref(pi.lo.raw), bk.DOWN)
bk.lib.mpfr_const_pi(bk.ct.byref(pi.hi.raw), bk.UP)
log2 = I(2).unary('log')
a = I(9)/4
b = I(101).unary('log')/2
r = (a/b)*I(97).unary('log')
w = 2*a-r
middle = 2*a-2*w
k = 2*I(97).unary('log')/I(97).unary('sqrt')
DELTA_EXP, LAST_EXP, PANELS = -24, 4, 2048
S = I(2)**LAST_EXP
delta = I(1)/2**(-DELTA_EXP)
KEYS = ['A_w', 'A_middle', 'K_adjacent', 'K_far']

def sq(x):
    # Every call here is on a strictly positive interval.
    assert x.positive()
    return I(op('mul', x.lo, x.lo), op('mul', x.hi, x.hi, bk.UP))


def node_values(s):
    # Phi(s,z)=-z/s atan(s/z) - log(s^2+z^2)/2.
    # Its second z derivative is 1/(s^2+z^2), modulo the
    # cancelled linear term pi*z/(2s) in the primitive.
    s2 = sq(s)
    zs = [w, middle, w+middle, 2*a]
    ats = [(z/s)*(s/z).unary('atan') for z in zs]
    logs = [(s2+sq(z)).unary('log') for z in zs]
    phis = [-at-lg/2 for at, lg in zip(ats, logs)]
    Aw = (1+sq(w/s)).unary('log')+2*ats[0]
    Am = (1+sq(middle/s)).unary('log')+2*ats[1]
    Kadj = phis[2]-phis[0]-phis[1]-s.unary('log')
    Kfar = phis[3]-2*phis[2]+phis[1]
    decay = (-2*s).unary('exp')
    return [decay*x for x in (Aw, Am, Kadj, Kfar)]

# Exact rational dyadic nodes; use monotonicity in s, not interval-wide
# dependency evaluation, for every entire panel. Retain all endpoint
# values and every octave's cumulative bounds for complete replay.
nodes = []
blocks = []
lower, upper = [I(0) for _ in KEYS], [I(0) for _ in KEYS]
s_prev = delta
v_prev = node_values(s_prev)
nodes.append({'s':s_prev.dump(), 'values':[v.dump() for v in v_prev]})
positive_endpoints = all(v.positive() for v in v_prev)
for exponent in range(DELTA_EXP, LAST_EXP):
    scale = I(2)**exponent if exponent >= 0 else I(1)/2**(-exponent)
    width = scale/PANELS
    for panel in range(1, PANELS+1):
        s_next = scale*I(PANELS+panel)/PANELS
        v_next = node_values(s_next)
        positive_endpoints = positive_endpoints and all(v.positive() for v in v_next)
        for j in range(4):
            # Right rectangles are lower; left rectangles are upper.
            lower[j] = lower[j]+width*v_next[j]
            upper[j] = upper[j]+width*v_prev[j]
        nodes.append({'s':s_next.dump(), 'values':[v.dump() for v in v_next]})
        s_prev, v_prev = s_next, v_next
    blocks.append({'octave_exponent':exponent,
                   'cumulative_lower':[x.dump() for x in lower],
                   'cumulative_upper':[x.dump() for x in upper]})
    print('Completed dyadic octave', exponent, flush=True)

# Complete integral upper bounds on (0,delta) and (S,infinity).
small_A = [2*delta*((2*L/delta).unary('log')+2) for L in (w,middle)]
small_adj = delta*(pi/2+(w/delta).unary('log')+1)
small_far = delta*sq(w)/sq(middle)
small = small_A+[small_adj, small_far]
decay_tail = (-2*S).unary('exp')/2
large_A = [decay_tail*(sq(L/S)+pi*L/S) for L in (w,middle)]
large_adj = decay_tail*w*middle/sq(S)
large_far = decay_tail*sq(w)/sq(S)
large = large_A+[large_adj,large_far]
full_integrals = [I(lo.lo, (hi+sm+lg).hi)/pi
                  for lo,hi,sm,lg in zip(lower,upper,small,large)]
Aw = w*log2+full_integrals[0]
Am = middle*log2+full_integrals[1]
Kadj, Kfar = full_integrals[2:]
EE = 2*Aw-2*Kfar
EM = -2*Kadj
MM = Am
threshold = 8*k*w
assert MM.positive(), 'Response coefficient is not certified positive'
minimum_amplitude = -EM/MM
minimum_energy = EE-sq(EM.abs())/MM
minimum_margin = minimum_energy-threshold
# Fix an exact rational inside a certified negative witness region;
# this is a verification of t=1/20, not an amplitude search. The
# minimizing-amplitude interval is also retained without rounding.
witness_t = I(1)/20
witness_energy = EE+2*witness_t*EM+sq(witness_t)*MM
witness_margin = witness_energy-threshold
claims = {
    'geometry_0_delta_lt_w':delta.positive() and (w-delta).positive(),
    'geometry_w_lt_a':(a-w).positive(),
    'geometry_r_gt_w':(r-w).positive(),
    'middle_positive':middle.positive(),
    'response_positive':MM.positive(),
    'all_sample_integrands_strictly_positive':positive_endpoints,
    'cross_strictly_negative':(-EM).positive(),
    'quadratic_gram_positive':(EE*MM-sq(EM.abs())).positive(),
}
failures = [name for name, ok in claims.items() if not ok]
negative_minimum = (-minimum_margin).positive()
nonnegative_minimum = minimum_margin.positive()
negative_witness = (-witness_margin).positive()
result = ('STRICT_NEGATIVE_MINIMUM' if negative_minimum else
          'STRICT_POSITIVE_MINIMUM' if nonnegative_minimum else
          'INCONCLUSIVE_STRADDLING_ZERO')
output = {
    'scope':'Only fixed real family 1_E+t1_M; original full-J allocation, no cap or support relaxation.',
    'status':'UNVERIFIED allocation counterexample candidate; independent critical audit pending.' if negative_minimum else result,
    'mpfr_version':bk.lib.mpfr_get_version().decode(), 'precision_bits':bk.PREC,
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'backend_path':str(BACKEND.relative_to(ROOT)),
    'backend_sha256':hashlib.sha256(BACKEND.read_bytes()).hexdigest(),
    'geometry':{name:val.dump() for name,val in [('a',a),('b',b),('r',r),('w',w),('middle_length',middle),('k',k)]},
    'quadrature':{'first_exponent':DELTA_EXP,'last_exponent':LAST_EXP,
                  'panels_per_octave':PANELS,'total_panels':len(nodes)-1,
                  'delta':delta.dump(),'S':S.dump(),'integrand_order':KEYS,
                  'method':'decreasing-positive left/right rectangle bounds'},
    'nodes':nodes, 'cumulative_octave_bounds':blocks,
    'small_s_upper':[x.dump() for x in small],
    'large_s_upper':[x.dump() for x in large],
    'full_kernel_integrals':[x.dump() for x in full_integrals],
    'interval_energies':{'A_w':Aw.dump(),'A_middle':Am.dump(),
                         'K_adjacent':Kadj.dump(),'K_far':Kfar.dump()},
    'matrix':[[EE.dump(),EM.dump()],[EM.dump(),MM.dump()]],
    'correlation':w.dump(), 'required_threshold':threshold.dump(),
    'minimizing_amplitude':minimum_amplitude.dump(),
    'minimum_energy':minimum_energy.dump(),'minimum_margin':minimum_margin.dump(),
    'rational_witness':{'t':'1/20','energy':witness_energy.dump(),'margin':witness_margin.dump(),
                        'strict_negative_certified':negative_witness},
    'decision':result,'claims':claims,'verification_failures':failures,
    'failed_mathematical_tests':['universal_prime97_one_eighth_allocation'] if negative_witness else [],
}
path = Path(__file__).with_name('certificate-1157.json')
path.write_text(json.dumps(output,indent=2)+'\n')
for name, value in [('EE',EE),('EM',EM),('MM',MM),('required_threshold',threshold),
                    ('minimizing_amplitude',minimum_amplitude),('minimum_margin',minimum_margin),
                    ('rational_witness_margin',witness_margin)]:
    print(name, [float(x) for x in value.dump()])
print('Required allocation margin >= 0; result:',result)
print('Verification failures:',failures,'; rational witness negative:',negative_witness)
print('Full certificate:',path)
if failures:
    raise SystemExit(1)
