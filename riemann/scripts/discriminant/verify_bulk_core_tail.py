"""Replay all step-196 angular cells and positive Euler moment records."""
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import certify_bulk_conditional_sign as c


def main():
    directory = Path(__file__).parent
    data = json.loads((directory/'bulk-core-tail-196.json').read_text())
    source = json.loads((directory/'bulk-haar-conditional-sign-194.json').read_text())
    pre = json.loads((directory/'bulk-core-tail-preliminary-196.json').read_text())
    fail = json.loads((directory/'bulk-core-tail-failed-196.json').read_text())
    checks = {'generator_checks': all(data['checks'].values())}
    for k in c.calls:
        c.calls[k] = 0
    a, b = [F(data['g_full_range'][k]) for k in ('lower', 'upper')]
    cells = data['cells']
    checks['partition'] = (cells[0]['left'] == '0' and cells[-1]['right'] == '1'
        and all(x['right'] == y['left'] for x, y in zip(cells, cells[1:]))
        and all(F(r['right'])-F(r['left']) == F(r['mass']) > 0 for r in cells)
        and sum((F(r['mass']) for r in cells), F(0)) == 1)
    for r in cells:
        actual, _ = c.cell(F(r['left']), F(r['right']), [c.I(30)])
        assert json.loads(json.dumps(actual)) == r
    lo = sum(F(r['values'][0]['integral']['lower']) for r in cells)
    hi = sum(F(r['values'][0]['integral']['upper']) for r in cells)
    checks['every_branch_jet_and_cell_replayed'] = data['conditional_value'] == {'lower': str(lo), 'upper': str(hi)}
    checks['positive_point'] = lo > 0
    T = c.I(F(13, 4))
    B = c.I(F(1, 4))+c.I(3)/c.I(80).sqrt()
    C = c.I(F(3, 2))*(1+c.I(1)/c.I(80).sqrt())
    transport = data['transport']
    end = F(transport['c'])
    D = B+(2*C+T*B)*end+T*C*end**2
    c.calls['state_response_derivative'] += 1
    checks['full_core_transport'] = (transport['anchor'] == source['centers'][0]['value']
        and end-a == F(1, 100000) and F(transport['sup_abs_derivative']) == F(D.hi, c.S)
        and F(transport['core_upper']) == F(transport['anchor']['upper'])+F(D.hi, c.S)*(end-a) < 0
        and F(transport['delta']) == -F(transport['core_upper']))
    M = F(c.fallback(c.I(b)).hi, c.S)
    checks['full_global_M'] = F(data['M']) == M
    checks['failed_and_preliminary_callback_counts'] = (fail['state_response_derivative_callbacks'] ==
        3*next(i for i, r in enumerate(source['cells']) if 'state_jets' not in r)
        and pre['state_response_derivative_callbacks'] == 3*sum('state_jets' in r for r in source['cells']))
    # Re-evaluate every preliminary derivative, including all tie neighborhoods.
    def dec24(r):
        return c.I(c.I(F(r['lower'])).lo, c.I(F(r['upper'])).hi, True)
    gg = c.I(c.I(a).lo, c.I(1).hi, True)
    pre_total = c.I(0)
    for r, saved in zip(source['cells'], pre['cell_derivatives']):
        if 'state_jets' not in r:
            bound = B+(2*C+T*B)*gg+T*C*gg.square()
            value = c.I(-bound.hi, bound.hi, True)
        else:
            vals = []
            for state in r['state_jets']:
                x, y, z = [dec24(q['value']) for q in state]
                t, p, cc = 3*(x.square()+y.square()), 3*(y.square()+x*z), -18*y.square()*(x.square()+x*z)
                c.calls['state_response_derivative'] += 1
                vals.append(c.b.exp_negative(t*gg)*(p+(2*cc-t*p)*gg-t*cc*gg.square()))
            value = sum(vals, c.I(0))/3
        assert value.enc() == saved
        pre_total = pre_total+value*F(r['mass'])
    checks['complete_preliminary_derivative_replay'] = pre_total.enc() == pre['derivative']
    callback_counts = dict(c.calls)
    complete_callbacks = data['callback_total']+sum(callback_counts.values())
    checks['complete_work_cap'] = complete_callbacks <= 262144
    # No geometry object is used after changing the integer scale.
    base = c.b
    base.SCALE = 10**160
    I = base.I
    moments = json.loads((directory/'bulk-core-tail-moments-196.json').read_text())
    def dec(r):
        return I(I(F(r['lower'])).lo, I(F(r['upper'])).hi, True)
    _, coefficients = base.source_coefficients(directory)
    checks['source_coefficient_replay'] = coefficients == moments['source']
    alpha = dec(coefficients['alpha'])
    theta = {j: dec(coefficients['theta'][str(j)]) for j in (13, 14)}
    cc = {j: dec(coefficients['source_bounds']['C'][str(j)]) for j in (13, 14)}
    weight = {0: alpha*(1-theta[13])+(1-alpha)*(1-theta[14]),
              13: alpha*theta[13]/cc[13], 14: (1-alpha)*theta[14]/cc[14]}
    assert {str(j): v.enc() for j, v in weight.items()} == moments['positive_weight']
    assert all(v.lo > 0 for v in weight.values())
    local = {(r['j'], r['p']): r for r in moments['local_factors']}
    primes = [p for p in range(2, 201) if all(p % q for q in range(2, isqrt(p)+1))]
    evaluated = {0: I(1)}
    assert set(local) == {(r['j'], p) for r in moments['C'] for p in primes}
    for r in moments['C']:
        j, value = r['j'], I(1)
        for p in primes:
            record = local[j, p]
            e = record['e']
            assert 1 <= e <= 1024
            term = total = I(1)
            for k in range(1, e+1):
                term = term*F((j+k-1)**2, k*k*p**5)
                total = total+term
            ratio = F((j+e)**2, (e+1)**2*p**5)
            assert 0 < ratio < 1 and str(ratio) == record['ratio']
            tail = term*ratio/(1-ratio)
            factor = I(total.lo, total.hi+tail.hi, True)
            assert total.enc() == record['sum'] and tail.enc() == record['tail'] and factor.enc() == record['factor']
            assert tail.hi*10**110 <= total.lo
            value = value*factor
        denominator = 1-F(j*j, 201**5)
        assert denominator > 0
        tail = F(j*j, 4*200**4)/denominator
        assert 0 < tail < 1 and str(tail) == r['prime_log_tail']
        value = I(value.lo, (value/(1-tail)).hi, True)
        assert value.enc() == r['moment']
        evaluated[j] = value
    checks['all_2024_local_factors_and_full_prime_tails_replayed'] = len(local) == 2024
    poly, required = {0: I(1)}, {0}
    for r in moments['G_moments']:
        new = {}
        for k, v in poly.items():
            for j, w in weight.items():
                new[k+j] = new.get(k+j, I(0))+v*w
        poly = new
        required.update(poly)
        assert {str(j): v.enc() for j, v in poly.items()} == r['polynomial']
        raw = sum((v*evaluated[j] for j, v in poly.items()), I(0))
        used = raw.intersect(I(1)) if r['r'] == 1 else raw
        assert raw.enc() == r['raw_moment'] and used.enc() == r['moment']
    checks['all_eight_positive_expansions_replayed'] = sorted(required) == moments['orders'] and max(required) == 112
    for r in data['candidate_cutoffs']:
        x = F(r['c'])
        tails = [min(F(1), F(m['moment']['upper'])/x**m['r']) for m in moments['G_moments']]
        assert list(map(str, tails)) == r['markov_bounds'] and min(tails) == F(r['pbar'])
        if r['negative_core_certified']:
            upper = -F(transport['delta'])*(1-min(tails))+M*min(tails)
            assert str(upper) == r['comparison_upper'] and upper > 0
    checks['all_32_markov_tests_replayed'] = len(data['candidate_cutoffs']) == 32
    obs = data['global_M_obstruction']
    delta_max = -F(transport['anchor']['lower'])
    floor = min(F(1), *[F(m['moment']['upper'])/F(30)**m['r'] for m in moments['G_moments']])
    lower = -delta_max*(1-floor)+M*floor
    checks['optimistic_global_M_obstruction'] = (str(delta_max) == obs['delta_upper_for_any_negative_core']
        and str(floor) == obs['computed_pbar_lower_for_c_below_point']
        and str(lower) == obs['optimistic_comparison_lower'] and lower > 0 and lo > 0 and obs['certified'])
    assert all(checks.values()), checks
    out = {'checks': checks, 'verification_callback_counts': callback_counts,
           'complete_callbacks': complete_callbacks, 'total_cap': 262144,
           'conditional_point': data['conditional_value'], 'transport': transport,
           'global_M_obstruction': obs, 'failures': [],
           'qualification': 'Full arithmetic replay; not an independent critical audit.'}
    path = directory/'bulk-core-tail-verification-196.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print('Checks passed:', len(checks), '; all cells, local Euler factors, expansions and candidate bounds replayed.')
    print('Callbacks total / cap:', complete_callbacks, 262144)
    print('Strict obstruction comparison lower:', float(lower))
    print('Failures:', out['failures'])
    print('Certificate:', path)


if __name__ == '__main__':
    main()
