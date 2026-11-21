#!/usr/bin/env python3
"""One frozen capped-symbol certificate: exact support/translation, no search."""
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

def sq(x):
    y = x.abs()
    return I(op('mul', y.lo, y.lo), op('mul', y.hi, y.hi, m.UP))

a = I(9)/4
b = I(101).unary('log')/2
r = a/b*I(97).unary('log')
w = 2*a-r
c = a-w/2
k = 2*I(97).unary('log')/I(97).unary('sqrt')
T, panel_den, phase_count = 256, 16, 4096
h, N = I(1)/panel_den, T*panel_den
alpha = I(T+2).unary('log')
q0 = alpha-I(2).unary('log')
qder = [q0]+[I(math.factorial(j-1))/2**j for j in range(1,5)]
M4 = sum(math.comb(4,j)*qder[j]*(2*a)**(4-j) for j in range(5))
kernel_error = I(T)*h**4*M4/(4320*pi)
operator_error = 2*a*kernel_error
phase_error = 4*k*pi/phase_count
total_error = operator_error+phase_error
base_coercivity = alpha-4*k
paid_base_coercivity = base_coercivity-total_error
root3 = I(3).unary('sqrt')
norm2 = 2*w
base_pulse = base_coercivity*norm2
required_energy = 8*k*w

# Each positive-frequency Gauss node has integration weight h/2.
# K_N quadratic on this real-even pulse = h/(2pi) sum q(t)|F(t)|^2.
# All 8192 nodes are used. Save every enclosed node, multiplier,
# Fourier square and contribution; a preview is not the certificate.
acc, nodes, blocks = I(0), [], []
for panel in range(N):
    center = I(2*panel+1)/(2*panel_den)
    for sign in (-1,1):
        t = center+sign*h/(2*root3)
        q = alpha-(2+t).unary('log')
        F = 4*(w*t/2).trig('sin')*(c*t).trig('cos')/t
        F2 = sq(F)
        term = h/(2*pi)*q*F2
        acc = acc+term
        nodes.append({'panel':panel, 'sign':sign, 't':t.dump(),
                      'q':q.dump(), 'F2':F2.dump(), 'term':term.dump()})
    if (panel+1)%256 == 0:
        blocks.append({'panels_completed':panel+1, 'quadratic_sum':acc.dump()})

quadratic_error = operator_error*norm2
defect = acc+I(op('neg',quadratic_error.hi),quadratic_error.hi)
capped_energy = alpha*norm2-defect
capped_form = base_pulse-defect
finite_form = base_pulse-acc
# Exact finite Gram G=V*B_0^{-1}V has norm >= this quotient.
# No rounded matrix or finite-section upper inference is involved.
gram_lower_quotient = acc/base_pulse
paid_gram_lower_quotient = acc/(paid_base_coercivity*norm2)
rounding_width = I(op('sub',acc.hi,acc.lo,m.UP))

claims = {
    'positive_width':w.positive(),
    'disjoint_collars_and_nilpotent_shift':(r-a).positive() and (r-w).positive(),
    'width_less_than_a':(a-w).positive(),
    'base_coercive':base_coercivity.positive(),
    'error_paid_base_coercive':paid_base_coercivity.positive(),
    'all_quadrature_nodes_and_weights_positive':all(
        I(row['t'][0]).positive() and I(row['q'][0]).positive() for row in nodes),
    'every_node_below_cap':all((I(T)-I(row['t'][1])).positive() for row in nodes),
    'entire_fixed_node_set_used':len(nodes)==2*N,
    'capped_form_strictly_negative':(-I(capped_form.hi)).positive(),
    'finite_gram_norm_exceeds_one':(gram_lower_quotient-1).positive(),
    'paid_finite_gram_norm_exceeds_one':(paid_gram_lower_quotient-1).positive(),
    'rounding_width_below_1e_minus_90':(I('1e-90')-rounding_width).positive(),
}
failures = [key for key,value in claims.items() if not value]
out = {
    'scope':'Failure test of one T=256 capped supported certificate; original J allocation undecided.',
    'mpfr_version':m.lib.mpfr_get_version().decode(), 'precision_bits':m.PREC,
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'backend_path':str(backend.relative_to(root)),
    'backend_sha256':hashlib.sha256(backend.read_bytes()).hexdigest(),
    'scheme':{'T':T, 'panel_width':'1/16','gauss_order':2, 'panels':N,
              'positive_frequency_nodes':2*N,'feature_columns':4*N,
              'phase_count':phase_count,'tested_phase':'exactly 0',
              'full_phase_matrix_evaluation':'not performed: necessary phase-zero condition fails',
              'pulse':'unchanged C750h two endpoint indicators'},
    'a':a.dump(),'b':b.dump(),'r':r.dump(),'w':w.dump(),'c':c.dump(),'k':k.dump(),
    'alpha':alpha.dump(),'q_derivative_majorants':[v.dump() for v in qder],
    'kernel_fourth_derivative_majorant':M4.dump(),
    'uniform_kernel_error':kernel_error.dump(), 'supported_operator_error':operator_error.dump(),
    'phase_cover_error':phase_error.dump(),'combined_positive_test_error':total_error.dump(),
    'base_coercivity':base_coercivity.dump(),'paid_base_coercivity':paid_base_coercivity.dump(),
    'norm_squared':norm2.dump(),'base_pulse_energy':base_pulse.dump(),
    'required_capped_energy':required_energy.dump(),
    'finite_kernel_pulse_quadratic':acc.dump(),'scalar_arithmetic_width':rounding_width.dump(),
    'quadratic_error':quadratic_error.dump(),'exact_kernel_pulse_quadratic':defect.dump(),
    'capped_energy':capped_energy.dump(),'capped_form':capped_form.dump(),
    'finite_form':finite_form.dump(),'gram_norm_lower_quotient':gram_lower_quotient.dump(),
    'paid_gram_norm_lower_quotient':paid_gram_lower_quotient.dump(),
    'positive_frequency_nodes':nodes, 'cumulative_blocks':blocks,
    'matrix_error':'No matrix assembled. All scalar operations, nodes and weights enclosed; exact finite Gram norm lower bounded by the factorization identity.',
    'phase_error_used_in_negative_test':'0: phase zero is exact and necessary for the universal claim.',
    'tail_treatment':'J-J_T is the nonnegative complete integral over |t|>256; never bounded by an operator-norm tail or discarded to disprove J.',
    'claims':claims,'failures':failures,
    'failed_mathematical_tests':['J_T[f]>=8k|C_f(r)| for all supported f',
                                'phase-zero finite Gram norm <=1',
                                'error-paid all-phase sufficient certificate'],
}
path = Path(__file__).with_name('certificate-1148.json')
path.write_text(json.dumps(out,indent=2)+'\n')
for key in ['base_coercivity','supported_operator_error','phase_cover_error',
            'required_capped_energy','capped_energy','capped_form','quadratic_error',
            'gram_norm_lower_quotient','paid_gram_norm_lower_quotient']:
    print(key, [float(x) for x in out[key]])
print('Required capped form >= 0 and Gram norm <= 1; original J remains undecided.')
print('Verification failures:',failures)
print('Failed mathematical tests:',out['failed_mathematical_tests'])
print('Full certificate:',path)
if failures:
    raise SystemExit(1)
