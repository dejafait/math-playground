#!/usr/bin/env python3
"""One fixed support-grid NNLS test; exact rational separator verification.

Candidate solve: 80-digit Decimal, Chebyshev coordinates. Candidate NNLS
is not certified optimal. The final separator is checked independently
using exact Fractions on ALL original atoms and ALL candidate nodes.
No728 data or other generated coefficients are read. No all-work upper
bound is claimed if the residual test fails first.
"""
from decimal import Decimal as D, localcontext, Context, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
import sys
sys.set_int_max_str_digits(0)  # Selected exact certificate values can exceed4300 digits.

HERE = Path(__file__).resolve()
K = int(sys.argv[1]) if len(sys.argv) > 1 else 8
assert 8 <= K <= 12, 'direct original-support feasibility checks are bounded at J<=4096'
OUT = HERE.with_name('support-grid-nnls-731-k'+str(K)+'.json')
J, DEG, NC, PREC = 2**K, 34, 129, 80
EPS = F(5, 10**19)
SEC_CAP, TOTAL_CAP = 387, 774


def cheb(t, n):
    v = [F(1), t]
    for k in range(2, n+1):
        v.append(2*t*v[-1]-v[-2])
    return v[:n+1]


indices = [J+i*(J-1)//(NC-1) for i in range(NC)]
assert len(set(indices)) == NC and min(indices) == J and max(indices) == 2*J-1
ts = [F(4*j+1, 2*J)-3 for j in range(J, 2*J)]
masses = [F(16*J, (4*j+1)**2) for j in range(J, 2*J)]
original_values = [cheb(t, 2*DEG) for t in ts]
moments = [sum((mass*row[k] for mass, row in zip(masses, original_values)), F(0))
           for k in range(2*DEG+1)]
columns = [original_values[j-J][:DEG+1] for j in indices]
trace = []
secondary = 0
outer = 0
solve_steps = 0


def decimal(q):
    return D(q.numerator)/D(q.denominator)


def solve(g, h, active):
    """Partial-pivot candidate solve; small pivots stop this prescription."""
    global solve_steps
    n = len(active)
    a = [[g[i][j] for j in active]+[h[i]] for i in active]
    for k in range(n):
        pivot = max(range(k, n), key=lambda i: abs(a[i][k]))
        if abs(a[pivot][k]) < D('1e-60'):
            raise ArithmeticError('fixed candidate normal-equation pivot below1e-60')
        a[k], a[pivot] = a[pivot], a[k]
        for i in range(k+1, n):
            factor = a[i][k]/a[k][k]
            for j in range(k+1, n+1):
                a[i][j] -= factor*a[k][j]
                solve_steps += 1
            a[i][k] = D(0)
    z = [D(0)]*n
    for i in reversed(range(n)):
        z[i] = (a[i][n]-sum((a[i][j]*z[j] for j in range(i+1, n)), D(0)))/a[i][i]
    return z


with localcontext() as ctx:
    ctx.prec = PREC
    a = [[decimal(q) for q in col] for col in columns]
    b = [decimal(q) for q in moments[:DEG+1]]
    gram = [[D(0) for _ in range(NC)] for _ in range(NC)]
    rhs = [sum((col[k]*b[k] for k in range(DEG+1)), D(0)) for col in a]
    for i in range(NC):
        for j in range(i+1):
            value = sum((a[i][k]*a[j][k] for k in range(DEG+1)), D(0))
            gram[i][j] = gram[j][i] = value
    x = [D(0)]*NC
    passive = []
    state = 'not_started'
    try:
        while outer+secondary < TOTAL_CAP:
            w = [rhs[i]-sum((gram[i][j]*x[j] for j in passive), D(0)) for i in range(NC)]
            inactive = [i for i in range(NC) if i not in passive]
            if not inactive or max(w[i] for i in inactive) <= D('1e-65'):
                state = 'candidate_stationary'
                break
            enter = max(inactive, key=lambda i: w[i])
            passive.append(enter)
            outer += 1
            while True:
                zvalues = solve(gram, rhs, passive)
                z = {i: v for i, v in zip(passive, zvalues)}
                if all(v > 0 for v in zvalues):
                    x = [z.get(i, D(0)) for i in range(NC)]
                    break
                secondary += 1
                if secondary > SEC_CAP or outer+secondary >= TOTAL_CAP:
                    raise ArithmeticError('fixed NNLS iteration cap')
                alpha = min(x[i]/(x[i]-z[i]) for i in passive if z[i] <= 0)
                x = [x[i]+alpha*(z.get(i, D(0))-x[i]) for i in range(NC)]
                passive = [i for i in passive if x[i] > D('1e-65')]
                x = [x[i] if i in passive else D(0) for i in range(NC)]
            residual = [sum((a[i][k]*x[i] for i in passive), D(0))-b[k]
                        for k in range(DEG+1)]
            trace.append({'outer': outer, 'secondary': secondary, 'active': list(passive),
                          'raw_chebyshev_residual_squared': str(sum(v*v for v in residual))})
        else:
            state = 'fixed_total_iteration_cap'
    except ArithmeticError as exc:
        state = str(exc)
    residual = [sum((a[i][k]*x[i] for i in range(NC)), D(0))-b[k]
                for k in range(DEG+1)]
    raw_norm2 = sum(v*v for v in residual)

# Construct a rational dual candidate; these exact checks alone certify it.
q = [F(v) for v in residual]
grid_before = [sum((c*v for c, v in zip(q, col)), F(0)) for col in columns]
shift = max(F(0), -min(grid_before))
q[0] += shift
grid_values = [sum((c*v for c, v in zip(q, col)), F(0)) for col in columns]
original_q = [sum((c*v for c, v in zip(q, row)), F(0)) for row in original_values]
integral = sum((mass*v for mass, v in zip(masses, original_q)), F(0))
norm2 = sum((mass*v*v for mass, v in zip(masses, original_q)), F(0))
integral_moments = sum((q[k]*moments[k] for k in range(DEG+1)), F(0))
norm2_moments = sum((q[i]*q[j]*(moments[i+j]+moments[abs(i-j)])/2
                     for i in range(DEG+1) for j in range(DEG+1)), F(0))
checks = {
    'all_candidates_are_distinct_original_support': len(set(indices)) == NC and all(J <= j < 2*J for j in indices),
    'original_mass_below_one': 0 < moments[0] < 1,
    'all_output_weights_nonnegative': all(v >= 0 for v in x),
    'separator_nonnegative_on_ALL_candidates': min(grid_values) >= 0,
    'separator_integral_strictly_negative': integral < 0,
    'separator_norm_strictly_positive': norm2 > 0,
    'direct_integral_matches_ALL_moments': integral == integral_moments,
    'direct_norm_matches_ALL_degree68_moments': norm2 == norm2_moments,
    'every_nonnegative_rule_residual_above_fixed_budget': integral < 0 and norm2 > 0 and integral*integral > EPS*EPS*norm2,
}
# Fixed rational displayed lower bound, independent of floating square roots.
lower = F(1, 10**6)
checks['every_nonnegative_rule_residual_above_1e-6'] = integral < 0 and norm2 > 0 and integral*integral > lower*lower*norm2
theory = F(2**37)*(F(1, 5**34)+EPS*(1+F(1, 5**34)))+F(2**46, 4*2**72-3)
checks['prescribed_residual_budget_would_pay_uniform_error'] = theory < F(1, 10**7)

# Certify the ORIGINAL-measure residual. Let H be the Chebyshev Gram
# matrix. A numerical inverse R is accepted only after interval checking
# e=||I-RH||_infinity<1. Then ||H^-1||_infinity<=||R||_infinity/(1-e).
# r^T H^-1 r <= d*||r||_infinity^2*||H^-1||_infinity.
dn, up = Context(prec=100, rounding=ROUND_FLOOR), Context(prec=100, rounding=ROUND_CEILING)
dim = DEG+1
hq = [[(moments[i+j]+moments[abs(i-j)])/2 for j in range(dim)] for i in range(dim)]
with localcontext() as ctx:
    ctx.prec = PREC
    hd = [[decimal(v) for v in row] for row in hq]
    inverse_columns = [solve(hd, [D(int(i == j)) for i in range(dim)], list(range(dim)))
                       for j in range(dim)]
    inverse = [[inverse_columns[j][i] for j in range(dim)] for i in range(dim)]


def enclose(v):
    return dn.divide(D(v.numerator), D(v.denominator)), up.divide(D(v.numerator), D(v.denominator))


def interval_add(a, b):
    return dn.add(a[0], b[0]), up.add(a[1], b[1])


def interval_multiply_scalar(a, c):
    if c >= 0:
        return dn.multiply(a[0], c), up.multiply(a[1], c)
    return dn.multiply(a[1], c), up.multiply(a[0], c)


hb = [[enclose(v) for v in row] for row in hq]
ebox = []
rowbounds = []
for i in range(dim):
    row = []
    bound = D(0)
    for j in range(dim):
        value = (D(0), D(0))
        for k in range(dim):
            value = interval_add(value, interval_multiply_scalar(hb[k][j], inverse[i][k]))
        delta = D(int(i == j))
        value = (dn.subtract(delta, value[1]), up.subtract(delta, value[0]))
        row.append(list(map(str, value)))
        bound = up.add(bound, max(value[0].copy_abs(), value[1].copy_abs()))
    ebox.append(row)
    rowbounds.append(bound)
eupper = max(rowbounds)
rnorm = D(0)
for row in inverse:
    rownorm = D(0)
    for v in row:
        rownorm = up.add(rownorm, v.copy_abs())
    rnorm = max(rnorm, rownorm)
weights_exact = [F(v) for v in x]
rq = [sum((weights_exact[i]*columns[i][k] for i in range(NC)), F(0))-moments[k]
      for k in range(dim)]
rmax = max(enclose(abs(v))[1] for v in rq)
assert eupper < 1, 'inverse residual does not certify original-measure Gram inverse'
hinv_bound = up.divide(rnorm, dn.subtract(D(1), eupper))
epsilon_squared_bound = up.multiply(up.multiply(D(dim), up.multiply(rmax, rmax)), hinv_bound)
checks['original_gram_inverse_residual_below_half'] = eupper < D('0.5')
checks['original_orthonormal_residual_within_fixed_budget'] = F(epsilon_squared_bound) <= EPS*EPS
checks['original_orthonormal_residual_below_1e-70'] = F(epsilon_squared_bound) < F(1, 10**140)
checks['exactly35_strictly_positive_original_support_weights'] = sum(v > 0 for v in weights_exact) == 35
checks['inactive_weights_exactly_zero'] = all(x[i] == 0 for i in range(NC) if i not in passive)
separator_tests = {k: checks.pop(k) for k in ['separator_integral_strictly_negative',
    'every_nonnegative_rule_residual_above_fixed_budget', 'every_nonnegative_rule_residual_above_1e-6']}

def short(q):
    with localcontext() as ctx:
        ctx.prec = 12
        return str(decimal(q))


certificate = {
    'scope': 'partial fixed129-index degree34 original-support feasibility certificate; separator not found; NOT a full kernel construction',
    'script_sha256': sha256(HERE.read_bytes()).hexdigest(),
    'parameters': {'J': J, 'degree': DEG, 'candidates': NC, 'precision': PREC,
                   'secondary_cap': SEC_CAP, 'total_iteration_cap': TOTAL_CAP,
                   'all_blocks_k': [8, 71], 'exact_prefix_count': 256,
                   'required_residual_per_block': str(EPS), 'required_uniform_error': '1e-7',
                   'required_complete_work_cap': 10**8},
    'candidate_indices': indices, 'candidate_weights_decimal': list(map(str, x)),
    'solver': {'state': state, 'outer': outer, 'secondary': secondary,
               'active': passive, 'trace': trace, 'raw_chebyshev_residual_squared': str(raw_norm2),
               'qualification': 'candidate generation only; not a certified minimizer or orthonormal residual'},
    'exact_separator': {'basis': 'Chebyshev T_0,...,T_34 on C998v normalized t',
                        'coefficients': list(map(str, q)), 'constant_shift': str(shift),
                        'candidate_values_ALL': list(map(str, grid_values)),
                        'original_values_ALL': list(map(str, original_q)),
                        'original_moments_degree0_through68': list(map(str, moments)),
                        'integral': str(integral), 'norm_squared': str(norm2),
                        'residual_lower_bound_squared': str(integral*integral/norm2) if norm2 else None,
                        'display_integral': short(integral), 'display_norm_squared': short(norm2)},
    'uniform_bound_if_all_blocks_passed': str(theory),
    'original_measure_residual_certificate': {
        'normalization': 'nu_J of C998v(3); mass=16J/(4j+1)^2 on t=(4j+1)/(2J)-3',
        'inverse_decimal': [[str(v) for v in row] for row in inverse],
        'inverse_error_intervals_ALL': ebox, 'inverse_error_infinity_upper': str(eupper),
        'inverse_infinity_upper': str(rnorm), 'gram_inverse_infinity_upper': str(hinv_bound),
        'exact_chebyshev_residual_ALL': list(map(str, rq)), 'residual_infinity_upper': str(rmax),
        'orthonormal_residual_squared_upper': str(epsilon_squared_bound),
        'interval_digits': 100, 'all_arithmetic_outward': True},
    'separator_discriminator_tests': separator_tests,
    'checks': checks, 'failed_checks': [k for k, v in checks.items() if not v],
    'work': {'favorable_gram_multiply_add_arithmetic_lower_bound': NC*(NC+1)//2*(DEG+1)*2,
             'actual_candidate_elimination_inner_updates': solve_steps,
             'complete_upper_bound_certified': False,
             'reason': 'bounded partial feasibility test; remaining61 blocks and complete work are unverified; high-level routines are not single work units'},
    'storage': {'original_chebyshev_fraction_entries': J*(2*DEG+1),
                'candidate_gram_decimal_entries': NC*NC,
                'byte_upper_bound_certified': False},
    'unresolved': ['other candidate grids or degrees', 'actual exponential error', 'complete preparation and validation work/storage',
                   'full signed measure scalar and remaining9e-7', 'signed S3', 'H2', 'actual Xi/global assembly'],
}
OUT.write_text(json.dumps(certificate, indent=2)+'\n')
print('Candidate solver:', state, '; outer/secondary:', outer, secondary)
print('Raw Chebyshev residual squared:', raw_norm2, '(not the certified residual)')
print('Exact separator integral:', short(integral), '; norm squared:', short(norm2))
print('Original-orthonormal residual squared <=', epsilon_squared_bound, '; required <=', str(EPS*EPS))
print('Separator discriminator:', separator_tests)
print('Conditional all-block uniform bound:', short(theory), '; required <=1e-7')
print('All checks:', sum(checks.values()), '/', len(checks), '; failures:', certificate['failed_checks'])
print('Complete all-block work/storage upper bounds: unproved; partial feasibility check only.')
print('Certificate:', OUT.relative_to(HERE.parents[2]))
