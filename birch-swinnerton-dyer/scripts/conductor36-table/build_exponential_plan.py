#!/usr/bin/env python3
"""Fixed H=4860 full-exponential tail plan; no new Fourier sums."""
import json
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
BITS = 96
D = 1 << BITS
H = 4860


def out(lo, hi=None):
    hi = lo if hi is None else hi
    return [(F(lo)*D).__floor__(), -((-F(hi)*D).__floor__())]


def mul(a, b):
    products = [x*y for x in a for y in b]
    return [min(products)//D, -((-max(products))//D)]


def scale(a, c):
    vals = sorted(F(v, D)*c for v in a)
    return out(*vals)


def power(q, exponent):
    n = exponent
    base = q[:]
    result = [D, D]
    trace = []
    while n:
        row = {'remaining': n, 'base': base[:], 'before': result[:]}
        if n % 2:
            result = mul(result, base)
        row['after'] = result[:]
        n //= 2
        if n:
            base = mul(base, base)
        row['next_base'] = base[:]
        trace.append(row)
    return result, trace


def build():
    plan_path = HERE/'coupled_plan.json'
    old_path = HERE.parent/'nonunitary-cusp/reduced_phase_certificate.json'
    saved = json.loads(plan_path.read_text())
    old = json.loads(old_path.read_text())
    assert saved['schema'] == 'conductor36-coupled-T5-plan-v1'
    assert old['bits'] == BITS and old['scale'] == D
    pi = old['pi']['interval']
    assert 3*D < pi[0] <= pi[1] < 4*D
    omega = F(saved['omega_lower'])
    budget = F(1, 1 << 38)
    remainder = F(3**8*8**161, factorial(161))
    radius = -((-D*remainder).__floor__())
    heights = sorted({F(p['y']) for p in saved['primitives']})
    attenuation = []
    for y in heights:
        assert 0 < y <= 1
        w = scale(pi, -2*y)
        assert -8*D <= w[0] <= w[1] < 0
        term = partial = [D, D]
        trace = []
        for k in range(1, 161):
            term = scale(mul(term, w), F(1, k))
            partial = [partial[0]+term[0], partial[1]+term[1]]
            trace.append({'k': k, 'term': term, 'partial': partial})
        q = [partial[0]-radius, partial[1]+radius]
        assert 0 < q[0] <= q[1] < D
        powered, power_trace = power(q, H+1)
        # Positive dyadic endpoints cancel D in this quotient.
        bounds = [F(powered[0], D-q[0]), F(powered[1], D-q[1])]
        attenuation.append({'y': str(y), 'w': w, 'degree': 160,
                            'taylor_trace': trace, 'polynomial': partial,
                            'remainder': str(remainder), 'radius': radius, 'q': q,
                            'power_exponent': H+1, 'power_trace': power_trace,
                            'power_interval': powered, 'tail_bounds': list(map(str, bounds))})
    height_id = {y: i for i, y in enumerate(heights)}
    primitives = []
    for p in saved['primitives']:
        i = height_id[F(p['y'])]
        primitives.append({'x_reduced': p['x_reduced'], 'y': p['y'], 'H': H,
                           'attenuation_id': i, 'tail_bounds': attenuation[i]['tail_bounds']})
    rows = []
    for i, g in enumerate(saved['generators']):
        bounds = [F(0), F(0)]
        for j, w in g['occurrences']:
            for side in (0, 1):
                bounds[side] += 2*abs(F(w))*F(primitives[j]['tail_bounds'][side])/omega
        rows.append({'generator_id': i, 'endpoints': g['endpoints'],
                     'occurrences': g['occurrences'],
                     'absolute_occurrence_weight': g['absolute_occurrence_weight'],
                     'normalized_tail_width_bounds': list(map(str, bounds))})
    upper = [F(r['normalized_tail_width_bounds'][1]) for r in rows]
    lower = [F(r['normalized_tail_width_bounds'][0]) for r in rows]
    worst = max(range(len(rows)), key=lambda i: upper[i])
    threshold_failures = [i for i, width in enumerate(upper) if width > budget]
    obstruction_rows = [i for i, width in enumerate(lower) if width > budget]
    inconclusive_rows = [i for i in threshold_failures if i not in obstruction_rows]
    uniform_rho = budget*omega/(2*max(F(r['absolute_occurrence_weight']) for r in rows))
    width_power = max(k for k in range(101) if upper[worst] <= F(1, 1 << k))
    actual = {'generators': len(rows), 'points': len(primitives), 'heights': len(heights),
              'endpoint_occurrences': 144, 'max_H': H, 'distinct_terms': H*len(primitives),
              'worst_generator_id': worst, 'max_width_le_dyadic_power': width_power,
              'passing_width_rows': len(rows)-len(threshold_failures),
              'uniform_rho_all_pass': all(F(p['tail_bounds'][1]) <= uniform_rho for p in primitives)}
    required = {'generators': 72, 'points': 98, 'max_H': 4860, 'distinct_terms': 1000000,
                'normalized_two_sided_tail_width': str(budget)}
    return {'schema': 'conductor36-full-exponential-tail-plan-v1', 'bits': BITS, 'scale': D,
            'coupled_plan_sha256': sha256(plan_path.read_bytes()).hexdigest(),
            'audited_analytic_sha256': sha256(old_path.read_bytes()).hexdigest(),
            'pi': pi, 'omega_lower': str(omega), 'infinity_primitive': '0',
            'H': H, 'minimality_claimed': False, 'uniform_rho': str(uniform_rho),
            'attenuation': attenuation, 'primitives': primitives, 'generators': rows,
            'actual': actual, 'required': required,
            'threshold_failures': threshold_failures, 'obstruction_rows': obstruction_rows,
            'inconclusive_rows': inconclusive_rows,
            'workload_passed': not threshold_failures and H <= 4860 and actual['distinct_terms'] <= 1000000,
            'table_complete': False}


if __name__ == '__main__':
    result = build()
    destination = HERE/'exponential_plan.json'
    destination.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print('full-exponential plan actual=', result['actual'], 'required=', result['required'],
          'threshold failures=', result['threshold_failures'], 'certificate=', destination)
