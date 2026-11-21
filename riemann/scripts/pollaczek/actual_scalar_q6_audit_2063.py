#!/usr/bin/env python3
"""Independent fixed-input audit: integer-grid intervals, no original imports.

Reads every load-bearing entry of certificate2061; never rewrites it.
Also uses direct power evaluation and an independently enclosed chain.
"""
from fractions import Fraction as R
from math import comb, factorial, isqrt
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
OUT = HERE / 'actual-scalar-q6-audit-2063.json'
G = 10**60
report = {'status': 'STARTED', 'checks': {}, 'failures': [],
          'required_distinct_real_count': 4, 'grid_digits': 60}


def verify(label, condition):
    report['checks'][label] = bool(condition)
    if not condition:
        raise AssertionError(label)


def ceil_r(x):
    return -((-x.numerator)//x.denominator)


def grid(lo, hi):
    return (lo.numerator//lo.denominator, ceil_r(hi))


def decode(v):
    a, b = R(v['lower'])*G, R(v['upper'])*G
    if a.denominator != 1 or b.denominator != 1 or a > b:
        raise AssertionError('non-grid or unordered saved interval')
    return int(a), int(b)


def encode(v):
    return {'lower': str(R(v[0], G)), 'upper': str(R(v[1], G))}


def plus(a, b):
    return a[0]+b[0], a[1]+b[1]


def minus(a):
    return -a[1], -a[0]


def times(a, b):
    products = [x*y for x in a for y in b]
    return min(products)//G, -((-max(products))//G)


def rational_scale(a, c):
    values = [R(x)*c for x in a]
    return grid(min(values), max(values))


def rational_add(a, c):
    return grid(R(a[0])+G*c, R(a[1])+G*c)


def quotient(a, b):
    if b[0] <= 0 <= b[1]:
        raise AssertionError('zero divisor enclosure')
    values = [R(x*G, y) for x in a for y in b]
    return grid(min(values), max(values))


def polarity(v):
    if v[0] > 0:
        return 1
    if v[1] < 0:
        return -1
    raise AssertionError('unresolved sign')


def poly_encode(p):
    return [{'rational': str(a), 'sqrt2': str(b)} for a, b in p]


def horner(p, x, s):
    result = (0, 0)
    for a, b in reversed(p):
        result = plus(times(result, x), rational_add(rational_scale(s, b), a))
    return result


def direct(p, x, s):
    result, power = (0, 0), (G, G)
    for a, b in p:
        result = plus(result, times(power, rational_add(rational_scale(s, b), a)))
        power = times(power, x)
    return result


def division(a, b):
    # The discarded leading entry is exactly r_lc-(r_lc/b_lc)*b_lc.
    # Zero containment below is only a consistency check for that identity.
    polarity(b[-1])
    current = a[:]
    steps = []
    while len(current) >= len(b):
        h = len(current)-len(b)
        ratio = quotient(current[-1], b[-1])
        canceled = plus(current[-1], minus(times(ratio, b[-1])))
        if not canceled[0] <= 0 <= canceled[1]:
            raise AssertionError('exact cancellation not enclosed')
        current = [plus(v, minus(times(ratio, b[i-h])))
                   if h <= i < h+len(b)-1 else v
                   for i, v in enumerate(current[:-1])]
        steps.append({'shift': h, 'quotient_coefficient': encode(ratio),
                      'exact_zero_enclosure': encode(canceled),
                      'remaining_coefficients': list(map(encode, current))})
    return current, steps


def variations(v):
    return sum(v[i] != v[i-1] for i in range(1, len(v)))


def run():
    path = HERE / 'actual-scalar-q6-2061.json'
    original = json.loads(path.read_text())
    prior_path = HERE / 'tilted-boundary-metric-2010.json'
    prior = json.loads(prior_path.read_text())
    report['input_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
    report['audit_script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    verify('original_script_hash', original['script_sha256'] == hashlib.sha256(
        (HERE / 'actual_scalar_q6_2061.py').read_bytes()).hexdigest())
    verify('prior_input_hash', original['comparison_input_sha256'] == hashlib.sha256(
        prior_path.read_bytes()).hexdigest())

    # Independent Bernoulli table and its complete defining recurrence.
    bern = list(map(R, ['1','-1/2','1/6','0','-1/30','0','1/42','0',
        '-1/30','0','5/66','0','-691/2730','0','7/6','0',
        '-3617/510','0','43867/798']))
    for m in range(1, 19):
        verify('Bernoulli_recurrence_'+str(m), sum(
            R(comb(m+1,j))*bern[j] for j in range(m+1)) == 0)
    verify('saved_Bernoulli', list(map(str, bern)) == original['bernoulli_0_to_18'])
    phases = [(1,0), (1,1), (-1,0), (-1,-1)]
    v = []
    for n in range(9):
        p = [(R(0),R(0)) for _ in range(n+2)]
        for power in range(1,n+2):
            h = power-1
            c = (-R(factorial(n),factorial(n-h))*R(4**h*(4**(h+1)-1),
                 factorial(2*h+2))*bern[2*h+2]*2**(h+1))
            e = phases[(n-h)%4]
            p[power] = c*e[0], c*e[1]
        v.append(p)
    beta = []
    for k in range(7):
        p = [(R(0), R(0)) for _ in range(k+4)]
        for n, factor in [(k-2,4*k*(k-1)), (k,8*k*k+12*k+7),
                          (k+2,(2*k+3)*(2*k+5))]:
            if n < 0:
                continue
            for j, (a,b) in enumerate(v[n]):
                p[j] = p[j][0]+factor*a, p[j][1]+factor*b
        beta.append(p)
    jensen, weights, A, Q = [], [], [], []
    for k in range(7):
        j = R(1)
        for h in range(k):
            j *= R(6-h,6)
        w = R((2*k+1)*comb(2*k,k),4**k)
        jensen.append(j)
        weights.append(w)
        A.append([(j*a,j*b) for a,b in beta[k]])
        Q.append([(j*w*a,j*w*b) for a,b in beta[k]])
    for name, fresh in [('u_over_S_polynomials',v), ('beta_over_S_polynomials',beta),
                        ('A6_exact_polynomials',A), ('Q6_exact_coefficient_polynomials',Q)]:
        verify('exact_'+name, list(map(poly_encode,fresh)) == original[name])
    verify('Jensen_weights', list(map(str,jensen)) == original['N6_Jensen_weights'])
    verify('scalar_weights', list(map(str,weights)) == original['scalar_weights'])
    for key, fresh in [('u_over_S_polynomials',v),('beta_over_S_polynomials',beta),
                        ('a_over_S_polynomials',A)]:
        # The older file spells integral rationals as e.g. 0/1, not 0.
        decoded = [[(R(c['rational']),R(c['sqrt2'])) for c in p] for p in prior[key]]
        verify('prior_'+key, fresh == decoded)

    # Complete alternating-series evidence, including every saved term.
    arcs = []
    for d in (5,239):
        terms = [R(1 if j%2 == 0 else -1,(2*j+1)*d**(2*j+1)) for j in range(48)]
        total, error = sum(terms,R(0)), R(1,97*d**97)
        expected = {'argument': str(R(1,d)), 'term_count':48,
                    'terms':list(map(str,terms)), 'partial_sum':str(total),
                    'positive_remainder_upper':str(error)}
        verify('complete_arctan_'+str(d), original['arctan'+str(d)] == expected)
        arcs.append((total,total+error))
    raw = 16*arcs[0][0]-4*arcs[1][1], 16*arcs[0][1]-4*arcs[1][0]
    verify('raw_Machin_interval', original['pi_machin_interval'] ==
           {'lower':str(raw[0]), 'upper':str(raw[1])})
    pi = grid(raw[0]*G,raw[1]*G)
    b = isqrt(2*G*G)
    s = b,b+1
    verify('sqrt_strict_squares', 0 < b*b < 2*G*G < (b+1)**2)
    t2 = 2*R(1,5)/(1-R(1,5)**2)
    t4 = 2*t2/(1-t2*t2)
    verify('Machin_tangents', t2 == R(5,12) and t4 == R(120,119)
           and (t4-R(1,239))/(1+t4*R(1,239)) == 1)
    verify('Machin_branch_bounds', R(0) < 4*(R(1,5)-R(1,375))-R(1,239)
           and R(4,5) < 1)
    # atan(1)>1/2 follows by integrating 1/(1+t^2)>1/2 on (0,1).
    # Thus 4theta-phi<4/5<1<pi/2, proving the tangent branch.
    for key, val in [('pi_interval',pi),('sqrt2_interval',s)]:
        verify('fixed_'+key, encode(val) == original[key] == prior[key])

    coefficients = [horner(p,pi,s) for p in Q]
    verify('all_saved_coefficient_intervals', list(map(encode,coefficients)) ==
           original['Q6_coefficient_intervals'])
    verify('all_odd_nonzero', all(polarity(coefficients[k]) for k in (1,3,5)))
    chain = [coefficients, [rational_scale(coefficients[k],R(k)) for k in range(1,7)]]
    verify('saved_f0_f1', list(map(lambda p:list(map(encode,p)),chain)) ==
           original['sturm_chain'][:2])
    audit_trace = []
    for index, expected_degree in enumerate(range(4,-1,-1)):
        r, steps = division(chain[-2],chain[-1])
        trace = {'expected_remainder_degree':expected_degree,
                 'dividend':list(map(encode,chain[-2])),
                 'divisor':list(map(encode,chain[-1])), 'steps':steps,
                 'remainder':list(map(encode,r))}
        # Equality compares EVERY quotient, cancellation and lower update.
        verify('entire_saved_division_'+str(index), trace == original['division_trace'][index])
        verify('two_top_cancellations_'+str(index), [t['shift'] for t in steps] == [1,0])
        r = list(map(minus,r))
        verify('remainder_degree_and_sign_'+str(index), len(r) == expected_degree+1
               and polarity(r[-1]) != 0)
        chain.append(r)
        verify('entire_saved_chain_entry_'+str(index+2), list(map(encode,r)) ==
               original['sturm_chain'][index+2])
        audit_trace.append(trace)
    verify('complete_trace_lengths', len(original['division_trace']) == 5
           and len(original['sturm_chain']) == 7)
    # Second construction: direct power sum gives a different enclosure,
    # and is NOT seeded from the saved coefficient intervals or remainders.
    direct_coeff = [direct(p,pi,s) for p in Q]
    independent = [direct_coeff,[rational_scale(direct_coeff[k],R(k)) for k in range(1,7)]]
    independent_traces = []
    for degree in range(4,-1,-1):
        r, steps = division(independent[-2],independent[-1])
        r = list(map(minus,r))
        verify('direct_chain_degree_'+str(degree),len(r) == degree+1 and polarity(r[-1]) != 0)
        independent.append(r)
        independent_traces.append(steps)
    signs = [polarity(p[-1]) for p in chain]
    degrees = [len(p)-1 for p in chain]
    minus_signs = [s*(-1)**d for s,d in zip(signs,degrees)]
    vm,vp = variations(minus_signs),variations(signs)
    verify('degrees_6_to_0',degrees == list(range(6,-1,-1)) == original['sturm_degrees'])
    verify('saved_infinity_signs', signs == original['signs_at_positive_infinity'] and
           minus_signs == original['signs_at_negative_infinity'])
    verify('independent_chain_signs', [polarity(p[-1]) for p in independent] == signs)
    verify('variations_and_count', vm == 4 == original['variations_at_negative_infinity']
           and vp == 2 == original['variations_at_positive_infinity'] and
           vm-vp == 2 == original['actual_distinct_real_count'])
    verify('terminal_constant_nonzero',len(chain[-1]) == 1 and polarity(chain[-1][0]) == -1)
    verify('saved_result_and_checks', original['status'] == 'CERTIFIED' and
           original['square_free'] is True and original['threshold_passed'] is False
           and original['required_distinct_real_count'] == 4 and original['failures'] == []
           and all(original['checks'].values()))
    # All displayed 12-place bounds are checked independently as exact rationals.
    def outer12(iv):
        scale = 10**12
        lo,hi = R(iv[0]*scale,G),R(iv[1]*scale,G)
        return {'lower':str(R(lo.numerator//lo.denominator,scale)),
                'upper':str(R(ceil_r(hi),scale))}
    verify('displayed_coefficients', [outer12(v) for v in coefficients] ==
           original['Q6_coefficient_outer_12'])
    verify('displayed_leading_coefficients', [outer12(p[-1]) for p in chain] ==
           original['sturm_leading_outer_12'])
    report.update({'status':'AUDIT_PASSED', 'actual_distinct_real_count':vm-vp,
        'threshold_passed':False, 'square_free':True, 'degrees':degrees,
        'signs_at_negative_infinity':minus_signs,'signs_at_positive_infinity':signs,
        'variations':[vm,vp], 'exact_Q6_coefficients':list(map(poly_encode,Q)),
        'replayed_sturm_chain':[list(map(encode,p)) for p in chain],
        'replayed_division_trace':audit_trace,
        'direct_power_coefficient_intervals':list(map(encode,direct_coeff)),
        'direct_power_sturm_chain':[list(map(encode,p)) for p in independent],
        'direct_power_division_trace':independent_traces,
        'direct_terminal_constant':encode(independent[-1][0]),
        'source_scope':'Coste2002 Theorem1.1 / Proposition1.4 over real coefficients; finite Q6 only'})


if __name__ == '__main__':
    try:
        run()
    except Exception as exc:
        report['status'] = 'AUDIT_FAILED'
        report['error'] = str(exc)
    report['failures'] = [k for k,v in report['checks'].items() if not v]
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report.get(k) for k in ['status','actual_distinct_real_count',
        'required_distinct_real_count','threshold_passed','variations','failures','error']}))
    print('Checks:',len(report['checks']), 'Certificate: scripts/pollaczek/'+OUT.name)
    raise SystemExit(0 if report['status'] == 'AUDIT_PASSED' else 1)
