#!/usr/bin/env python3
"""Bounded fixed-label shared-preconditioner test. No NNLS/adaptation.

Correctly directed Decimal basic arithmetic is the inherited contract.
Counters below are subtotals, not a complete-work upper bound. A failed
sufficient test is not proof of negative quadrature weights.
"""
from decimal import Decimal as D, Context, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from math import comb
from hashlib import sha256
from pathlib import Path
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve()
OUT = HERE.with_suffix('.json')
PREC, DIM, DEG, EM, LOG_TERMS, ITER_CAP = 256, 35, 34, 64, 256, 15
LABELS = [29,36,21,15,46,55,64,10,74,83,6,92,3,100,107,40,113,1,
          25,118,122,125,0,69,127,51,87,18,128,96,2,8,120,124,104]
DOWN = Context(prec=PREC, rounding=ROUND_FLOOR)
UP = Context(prec=PREC, rounding=ROUND_CEILING)
ZERO = D(0)
counts = {'directed_scalar_product_terms': 0, 'single_anchor_inverse_calls': 0}


def q(v):
    v = F(v)
    return (DOWN.divide(D(v.numerator), D(v.denominator)),
            UP.divide(D(v.numerator), D(v.denominator)))


def add(a, b):
    return DOWN.add(a[0], b[0]), UP.add(a[1], b[1])


def sub(a, b):
    return DOWN.subtract(a[0], b[1]), UP.subtract(a[1], b[0])


def scale(a, c):
    c = D(c)
    if c >= 0:
        return DOWN.multiply(a[0], c), UP.multiply(a[1], c)
    return DOWN.multiply(a[1], c), UP.multiply(a[0], c)


def cheb_polynomials(n):
    result = [[1], [0, 1]]
    for k in range(2, n+1):
        nxt = [0]*(k+1)
        for i, v in enumerate(result[-1]):
            nxt[i+1] += 2*v
        for i, v in enumerate(result[-2]):
            nxt[i] -= v
        result.append(nxt)
    return result[:n+1]


def original_moments(J, bern, periodic_bound):
    # Exact finite algebra in positive powers; exact rational EM correction.
    # Only the logarithm and its remainder need directed summation.
    u, v = F(4*J+1, 4), F(8*J+1, 4)
    z = (v-u)/(v+u)
    assert 0 < z < F(1, 3)
    logpart, power = (ZERO, ZERO), z
    for i in range(LOG_TERMS):
        logpart = add(logpart, q(2*power/(2*i+1)))
        power *= z*z
    logtail = F(2, 513*3**513)*F(9, 8)
    logpart = add(logpart, (ZERO, q(logtail)[1]))
    s1 = (1/u-1/v)/2
    s2 = 1/u-1/v+(u**-2-v**-2)/2
    for r in range(1, EM):
        s1 += bern[2*r]/(2*r)*(u**(-2*r)-v**(-2*r))
        s2 += bern[2*r]*(u**(-2*r-1)-v**(-2*r-1))
    err1 = periodic_bound/(2*EM)*u**(-2*EM)
    err2 = periodic_bound*u**(-2*EM-1)
    e1, e2 = q(err1)[1], q(J*err2)[1]
    xm = [add(q(J*s2), (-e2, e2)),
          add(add(logpart, q(s1)), (-e1, e1))]
    sums = []
    for p in range(2*DEG-1):
        val = (v**(p+1)-u**(p+1)
               -sum((F(comb(p+1,l))*sums[l] for l in range(p)), F(0)))/(p+1)
        sums.append(val)
        xm.append(q(val/J**(p+1)))
    assert len(xm) == 69
    tm = []
    for n in range(69):
        total = (ZERO, ZERO)
        for p in range(n+1):
            total = add(total, scale(xm[p], comb(n,p)*2**p*(-3)**(n-p)))
        tm.append(total)
    cm = []
    for poly in cheb_polynomials(68):
        total = (ZERO, ZERO)
        for i, coefficient in enumerate(poly):
            total = add(total, scale(tm[i], coefficient))
        cm.append(total)
    return cm, {'inverse_moment_remainders': [str(J*err2), str(err1)],
                'log_remainder': str(logtail),
                'power_sums_exact': list(map(str, sums))}


def nodes_and_matrix(J):
    indices = [J+i*(J-1)//128 for i in LABELS]
    assert len(set(indices)) == DIM and all(J <= j < 2*J for j in indices)
    ts = [F(4*j+1, 2*J)-3 for j in indices]
    cols = []
    for t in ts:
        col = [F(1), t]
        for n in range(2, DIM):
            col.append(2*t*col[-1]-col[-2])
        cols.append(col)
    exact = [[cols[j][i] for j in range(DIM)] for i in range(DIM)]
    return indices, ts, exact, [[q(v) for v in row] for row in exact]


def gram(moments):
    return [[scale(add(moments[i+j], moments[abs(i-j)]), D('0.5'))
             for j in range(DIM)] for i in range(DIM)]


def midpoint(v):
    return (v[0]+v[1])/2


def inverse(matrix):
    # ONE augmented elimination with all35 right sides; pivoting candidate only.
    counts['single_anchor_inverse_calls'] += 1
    a = [[midpoint(v) for v in row]+[D(int(i == j)) for j in range(DIM)]
         for i, row in enumerate(matrix)]
    for k in range(DIM):
        pivot = max(range(k, DIM), key=lambda i: abs(a[i][k]))
        assert abs(a[pivot][k]) > D('1e-200'), 'fixed pivot threshold failed'
        a[k], a[pivot] = a[pivot], a[k]
        for i in range(k+1, DIM):
            factor = a[i][k]/a[k][k]
            for j in range(k+1, 2*DIM):
                a[i][j] -= factor*a[k][j]
            a[i][k] = ZERO
    r = [[ZERO]*DIM for _ in range(DIM)]
    for column in range(DIM):
        for i in range(DIM-1, -1, -1):
            r[i][column] = (a[i][DIM+column]
                           -sum((a[i][j]*r[j][column] for j in range(i+1, DIM)), ZERO))/a[i][i]
    return r


def error_certificate(R, A):
    E, lower_rows, upper_rows = [], [], []
    for i in range(DIM):
        row, lower, upper = [], ZERO, ZERO
        for j in range(DIM):
            lo, hi = ZERO, ZERO
            for k in range(DIM):
                c = R[i][k]
                a, b = A[k][j]
                if c >= 0:
                    lo = DOWN.add(lo, DOWN.multiply(c, a))
                    hi = UP.add(hi, UP.multiply(c, b))
                else:
                    lo = DOWN.add(lo, DOWN.multiply(c, b))
                    hi = UP.add(hi, UP.multiply(c, a))
                counts['directed_scalar_product_terms'] += 1
            delta = D(int(i == j))
            el, eh = DOWN.subtract(delta, hi), UP.subtract(delta, lo)
            row.append((el, eh))
            abslo = ZERO if el <= 0 <= eh else min(el.copy_abs(), eh.copy_abs())
            abshi = max(el.copy_abs(), eh.copy_abs())
            lower = DOWN.add(lower, abslo)
            upper = UP.add(upper, abshi)
        E.append(row)
        lower_rows.append(lower)
        upper_rows.append(upper)
    return {'error_intervals': E, 'row_norm_lower': lower_rows,
            'row_norm_upper': upper_rows, 'norm_lower': max(lower_rows),
            'norm_upper': max(upper_rows), 'contraction_pass': max(upper_rows) < 1}


def scalar_solve(R, A, b, certificate):
    # Reachable only after contraction. Fixed15 preconditioned iterations.
    x = [ZERO]*DIM
    am = [[midpoint(v) for v in row] for row in A]
    bm = [midpoint(v) for v in b]
    for _ in range(ITER_CAP):
        residual = [bm[i]-sum((am[i][j]*x[j] for j in range(DIM)), ZERO) for i in range(DIM)]
        x = [x[i]+sum((R[i][j]*residual[j] for j in range(DIM)), ZERO) for i in range(DIM)]
    residual_box = [sub(b[i], sum_intervals([scale(A[i][j], x[j]) for j in range(DIM)]))
                    for i in range(DIM)]
    z = [sum_intervals([scale(residual_box[j], R[i][j]) for j in range(DIM)]) for i in range(DIM)]
    znorm = max(max(a.copy_abs(), b.copy_abs()) for a,b in z)
    radius = UP.divide(znorm, DOWN.subtract(D(1), certificate['norm_upper']))
    return x, radius, residual_box


def sum_intervals(values):
    total = (ZERO, ZERO)
    for v in values:
        total = add(total, v)
    return total


def sum_up(values):
    total = ZERO
    for v in values:
        total = UP.add(total, v)
    return total


def export(obj):
    if isinstance(obj, D):
        return str(obj)
    if isinstance(obj, dict):
        return {k: export(v) for k,v in obj.items()}
    if isinstance(obj, (tuple, list)):
        return [export(v) for v in obj]
    return obj


# Before numerical work: validation loop has12 charged units per term:
# 4 arithmetic, c binding1, a/b bindings2, sign comparison1, lo/hi stores2,
# k binding1 and successful advance1. This is only a LOWER bound.
mandatory_product_lower_bound = 61*2*DIM**3*12
assert mandatory_product_lower_bound <= 10**8  # Not a complete-work PASS.
report = {'scope': 'fixed k10 anchor unweighted infinity-norm Rump10.2 test; stop first failed sufficient criterion',
          'script_sha256': sha256(HERE.read_bytes()).hexdigest(),
          'parameters': {'precision': PREC, 'labels': LABELS, 'anchor_k': 10,
                         'required_k': list(range(11,72)), 'EM_order': EM,
                         'log_terms': LOG_TERMS, 'iteration_cap': ITER_CAP,
                         'epsilon_limit': '5e-19', 'uniform_limit': '1e-7', 'work_cap': 10**8},
          'pricing': {'mandatory_product_lower_bound': mandatory_product_lower_bound,
                      'complete_work_upper_bound': None, 'complete_storage_upper_bound': None,
                      'existing_three_rules_production': 'not included; no complete-cost claim'},
          'anchor': {}, 'blocks': [], 'checks': {}, 'failures': []}

with localcontext() as ctx:
    ctx.prec = PREC
    bern = [F(1)]
    for n in range(1, 2*EM+1):
        bern.append(-sum((F(comb(n+1,j))*bern[j] for j in range(n)), F(0))/(n+1))
    periodic = abs(bern[128])+sum((F(comb(128,j))*abs(bern[j]) for j in range(129)), F(0))
    moments, moment_evidence = original_moments(1024, bern, periodic)
    indices, ts, exactA, A = nodes_and_matrix(1024)
    H = gram(moments)
    RA, RH = inverse(A), inverse(H)
    ca, ch = error_certificate(RA, A), error_certificate(RH, H)
    report['anchor'] = {'indices': indices, 'nodes': list(map(str,ts)),
                        'original_moments': moments, 'moment_evidence': moment_evidence,
                        'interpolation_preconditioner': RA, 'gram_preconditioner': RH,
                        'interpolation': ca, 'gram': ch}
    report['checks']['anchor_interpolation_contraction'] = ca['contraction_pass']
    report['checks']['anchor_gram_contraction'] = ch['contraction_pass']
    assert ca['contraction_pass'] and ch['contraction_pass']
    # Check moment enclosures against the independently enumerated original
    # k10 moment certificate, not against its solver or claimed residual.
    oldpath = HERE.with_name('support-grid-nnls-731-k10.json')
    old = json.loads(oldpath.read_text())
    exact_old = list(map(F, old['exact_separator']['original_moments_degree0_through68']))
    report['checks']['all69_anchor_moments_enclose_exact731_values'] = all(
        F(a) <= m <= F(b) for (a,b),m in zip(moments,exact_old)) and len(exact_old)==69
    report['checks']['labels_equal_exact_saved_active_order'] = LABELS == old['solver']['active']
    report['anchor']['reference_sha256'] = sha256(oldpath.read_bytes()).hexdigest()
    for k in range(11,72):
        J = 2**k
        moments, evidence = original_moments(J, bern, periodic)
        indices, ts, exactA, A = nodes_and_matrix(J)
        H = gram(moments)
        ca, ch = error_certificate(RA, A), error_certificate(RH, H)
        block = {'k': k, 'indices': indices, 'nodes': list(map(str,ts)),
                 'original_moments': moments, 'moment_evidence': evidence,
                 'interpolation': ca, 'gram': ch}
        report['blocks'].append(block)
        print('k=', k, ' interpolation ||I-RA|| in', str(ca['norm_lower'])[:18], str(ca['norm_upper'])[:18],
              '; Gram in', str(ch['norm_lower'])[:18], str(ch['norm_upper'])[:18], flush=True)
        if not ca['contraction_pass'] or not ch['contraction_pass']:
            # Exact rational check for the failed interpolation row, independently
            # of interval products. Print/save the selected exact load-bearing value.
            if not ca['contraction_pass']:
                row = max(range(DIM), key=lambda i: ca['row_norm_lower'][i])
                exact_error_row = [F(int(row == j))-sum((F(RA[row][s])*exactA[s][j] for s in range(DIM)), F(0))
                                   for j in range(DIM)]
                exact_norm = sum(map(abs,exact_error_row),F(0))
                block['exact_failed_row'] = {'index': row, 'entries': list(map(str,exact_error_row)),
                                              'absolute_sum': str(exact_norm),
                                              'above_one': exact_norm > 1,
                                              'interval_row_contains_exact': all(F(a)<=v<=F(b) for (a,b),v in zip(ca['error_intervals'][row],exact_error_row))}
            report['failures'].append({'k': k, 'reason': 'unweighted infinity-norm sufficient criterion failed',
                                       'interpolation': not ca['contraction_pass'], 'gram': not ch['contraction_pass']})
            break
        x, radius, residual = scalar_solve(RA, A, moments[:DIM], ca)
        rmax = max(max(a.copy_abs(),b.copy_abs()) for a,b in residual)
        # Outward accumulation for the preconditioner norm.
        rnorm = max(sum_up([v.copy_abs() for v in row]) for row in RH)
        inverse_bound = UP.divide(rnorm, DOWN.subtract(D(1), ch['norm_upper']))
        eps2 = UP.multiply(D(DIM), UP.multiply(UP.multiply(rmax,rmax),inverse_bound))
        block['weights'] = x
        block['weight_radius'] = radius
        block['weight_lower_bound'] = DOWN.subtract(min(x),radius)
        block['epsilon_squared_upper'] = eps2
        if DOWN.subtract(min(x),radius) <= 0 or F(eps2) > F(5,10**19)**2:
            report['failures'].append({'k': k, 'reason': 'fixed weight positivity or original residual check failed'})
            break

report['counts_subtotals_not_complete_work'] = counts
report['status'] = 'STOP_SUFFICIENT_TEST' if report['failures'] else 'NUMERICAL_GATE_ONLY_COST_UNPAID'
report['checks']['no_per_block_inverse'] = counts['single_anchor_inverse_calls'] == 2
report['checks']['all_recorded_intervals_ordered'] = all(a <= b for block in [report['anchor']]+report['blocks']
    for system in ['interpolation','gram'] for row in block[system]['error_intervals'] for a,b in row)
OUT.write_text(json.dumps(export(report), indent=2)+'\n')
print('Status:', report['status'], '; checked blocks:', [b['k'] for b in report['blocks']])
print('Mandatory product-work lower bound:', mandatory_product_lower_bound, '; full cap:', 10**8, '; upper ledger UNPAID')
print('Checks:', report['checks'], '; failures:', report['failures'])
print('Certificate:', OUT.relative_to(HERE.parents[2]))
