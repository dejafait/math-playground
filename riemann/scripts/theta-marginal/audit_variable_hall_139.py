"""Audit only the two saved L905 grids; never refine or sign the full cut.

Regenerate cached elementary enclosures under L037, then reconstruct all
box sums by exact integers/fractions rather than the original I summation.
The original certificates are read-only. All comparisons go to disk.
"""
import hashlib
import itertools
import json
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path

from equal_neighbor_budget_135 import I, nonnegative, pi_bounds, self_check, sin_cos

HERE = Path(__file__).resolve().parent


def pair(d):
    return F(d['lower']), F(d['upper'])


def data(p):
    return {'lower': str(p[0]), 'upper': str(p[1])}


def contained(outer, inner):
    return pair(outer)[0] <= inner[0] <= inner[1] <= pair(outer)[1]


def product(a, b):
    p = [x*y for x in a for y in b]
    return min(p), max(p)


def quotient(a, b):
    assert b[0] > 0
    return product(a, (1/b[1], 1/b[0]))


def scaled(values):
    # Decimal denominators divide a common power of ten, exactly.
    digits = max(0, max(-Decimal(s).as_tuple().exponent
                        for d in values for s in d.values()))
    scale = 10**digits
    integers = []
    for d in values:
        v = tuple(F(s)*scale for s in d.values())
        assert all(x.denominator == 1 for x in v)
        integers.append(tuple(x.numerator for x in v))
    return scale, integers


def audit(mesh):
    path = HERE / f'variable-hall-cuts-137-m{mesh}.json'
    original_bytes = path.read_bytes()
    c = json.loads(original_bytes)
    checks = []

    def check(name, condition):
        checks.append({'check': name, 'pass': bool(condition)})
        if not condition:
            raise AssertionError(name)

    pi = pi_bounds()
    h = pi/(64*mesh)
    nt, nq = 32*mesh, 9*mesh
    check('grid metadata', (c['mesh'], c['t_cells'], c['q_cells'],
                           c['box_count'], c['precision'], c['theta_terms']) ==
          (mesh, nt, nq, nt*nq, 70, 4))
    check('Machin pi and exact-grid h', c['pi'] == pi.data() and c['h'] == h.data())

    # Recompute every cache entry; no selection or sampling.
    keys = list(c['kernel_cache'])
    for key in keys:
        lo, hi = map(int, key.split(':'))
        check(f'cache nonnegative domain {key}', 0 <= lo <= hi)
        u = I((h*lo).lo, (h*hi).hi)
        v = [pi*n*n*(2*u).exp() for n in range(1, 5)]
        k = nonnegative((u/2).exp()*sum(((8*x*x-12*x)*(-x).exp() for x in v), I(0)))
        k = I(k.lo, min(k.hi, 16))
        check(f'kernel {key}', c['kernel_cache'][key] == k.data())

    sines = [sin_cos(pi*j/(2*mesh), pi)[0] for j in range(nq+1)]
    for k in range(10):
        j = k*mesh
        exact = (0, 1, 0, -1)[k % 4]
        check(f'exact sine {j}', sines[j].lo <= exact <= sines[j].hi)
        sines[j] = I(exact)
    weights = [(sines[j+1]-sines[j])/16 for j in range(nq)]
    check('all integrated cosine weights', c['integrated_cosine_weights'] ==
          [w.data() for w in weights])

    eps = 160000*I(-75).exp()
    et = I.rational(F(512, 3))*eps
    es = 131072*I(-106).exp()*I.rational(F(9, 4*231)+F(3, 231**2)+F(2, 231**3))
    errors = [pi/(32 if ell == 0 else 16)*(et+es) for ell in range(5)]
    ms = {0: 256*I(-53).exp()/115,
          2: 256*I(-53).exp()*I.rational(F(9, 4*115)+F(3, 115**2)+F(2, 115**3))}
    mt = {0: 2*eps, 2: I.rational(F(8, 3))*eps}
    expected_bounds = {'epsilon': eps.data(), 'theta_density_error': et.data(),
                       'spatial_density_error': es.data(),
                       'lobe_tail_errors': [x.data() for x in errors],
                       'normalizer_spatial_errors': {str(r): x.data() for r, x in ms.items()},
                       'normalizer_theta_errors': {str(r): x.data() for r, x in mt.items()}}
    check('all complete-domain tail constants', c['bounds'] == expected_bounds)

    # A common exact decimal scale makes millions of summands integer-only.
    scale, ints = scaled([c['kernel_cache'][key] for key in keys])
    cache = dict(zip(keys, ints))
    qscale, qints = scaled(c['integrated_cosine_weights'])
    positive = [cache[f'{n}:{n+2}'] for n in range(nt+nq-1)]
    reflected = [cache['0:1']] + [cache[f'{n-1}:{n+1}'] for n in range(1, nt)]
    deltas = [(i+1)**3-i**3 for i in range(nt)]
    used = set()
    low_sums, high_sums = [0]*5, [0]*5
    counts = {'positive': 0, 'negative': 0}
    for j in range(nq):
        ell = (j+mesh)//(2*mesh)
        qlo, qhi = qints[j]
        sign = (-1)**ell
        check(f'fixed cosine sign cell {j}', qlo > 0 if sign > 0 else qhi < 0)
        counts['positive' if sign > 0 else 'negative'] += 1
        sl, su = 0, 0
        for i, d in enumerate(deltas):
            p = positive[i+j]
            m = reflected[abs(i-j)]
            sl += d*p[0]*m[0]
            su += d*p[1]*m[1]
        if sign > 0:
            low_sums[ell] += sl*qlo
            high_sums[ell] += su*qhi
        else:
            low_sums[ell] += su*qlo
            high_sums[ell] += sl*qhi
    check('cell signs count', c['cell_sign_counts'] == counts)
    # Every possible positive and reflected interval is used, along with
    # every normalizer interval. Exact coverage follows from index ranges.
    used.update(f'{n}:{n+2}' for n in range(nt+nq-1))
    used.add('0:1')
    used.update(f'{n-1}:{n+1}' for n in range(1, nt))
    used.update(f'{n}:{n+1}' for n in range(nt))
    check('complete cache key set', used == set(keys))
    hp = pair(c['h'])
    factor = (2*hp[0]**3/3, 2*hp[1]**3/3)
    sums = [(F(l, scale**2*qscale), F(u, scale**2*qscale))
            for l, u in zip(low_sums, high_sums)]
    finite = [product(factor, s) for s in sums]
    for ell in range(5):
        check(f'exact integer box sum B{ell}', contained(c['result']['finite_B'][ell], finite[ell]))
        old = pair(c['result']['finite_B'][ell])
        error = F(errors[ell].hi)
        check(f'complete lobe B{ell}', contained(c['result']['complete_B'][ell],
                                               (old[0]-error, old[1]+error)))

    moment_details = {}
    for r in (0, 2):
        sl, su = 0, 0
        for i in range(nt):
            kl, ku = cache[f'{i}:{i+1}']
            d = 1 if r == 0 else deltas[i]
            sl += d*kl
            su += d*ku
        f = hp if r == 0 else (hp[0]**3/3, hp[1]**3/3)
        moment = product(f, (F(sl, scale), F(su, scale)))
        moment = (moment[0], moment[1]+F((ms[r]+mt[r]).hi))
        check(f'full moment M{r}', contained(c['result']['moments'][str(r)], moment))
        moment_details[str(r)] = data(moment)
    a0 = product(pair(c['result']['moments']['0']), pair(c['result']['moments']['2']))
    a0 = (2*a0[0], 2*a0[1])
    check('positive normalizer', a0[0] > 0 and contained(c['result']['A0'], a0))
    a0 = pair(c['result']['A0'])
    lobes = list(map(pair, c['result']['complete_B']))
    for j in range(-2, 3):
        ell, mult = 2*abs(j), 2 if j == 0 else 1
        expected = quotient(tuple(mult*x for x in lobes[ell]), a0)
        check(f'resource {j}', contained(c['result']['resources'][str(j)], expected))
    for k in range(-2, 2):
        ell = abs(2*k+1)
        expected = quotient((-lobes[ell][1], -lobes[ell][0]), a0)
        check(f'demand {k}', contained(c['result']['demands'][str(k)], expected))

    expected_subsets = [s for n in range(1, 5) for s in itertools.combinations(range(-2, 2), n)]
    check('all fifteen subsets once', [tuple(d['S']) for d in c['result']['cuts']] == expected_subsets)
    cut_details = []
    for cut in c['result']['cuts']:
        subset = cut['S']
        neighbors = sorted({j for k in subset for j in (k, k+1)})
        coefficients = [0]*5
        for j in neighbors:
            coefficients[2*abs(j)] += 2 if j == 0 else 1
        for k in subset:
            coefficients[abs(2*k+1)] += 1
        check(f'union and coefficients {subset}', cut['T'] == neighbors and cut['B_coefficients'] == coefficients)
        raw = tuple(sum((n*b[e] for n, b in zip(coefficients, lobes)), F(0)) for e in (0, 1))
        check(f'exact cut sum {subset}', contained(cut['raw_A0_H'], raw))
        normalized = quotient(pair(cut['raw_A0_H']), a0)
        check(f'exact normalized cut {subset}', contained(cut['H'], normalized))
        proper = len(subset) < 4
        check(f'decision {subset}', cut['decision'] == ('PASS' if proper else 'INCONCLUSIVE'))
        threshold = F(1, 100) if mesh == 128 else F(0)
        if proper:
            check(f'proper threshold {subset}', pair(cut['H'])[0] > threshold)
        else:
            check('full cut contains zero', pair(cut['H'])[0] < 0 < pair(cut['H'])[1])
            if mesh == 128:
                check('full cut rational range', -F(1, 125) < pair(cut['H'])[0] and pair(cut['H'])[1] < F(1, 100))
        cut_details.append({'S': subset, 'coefficients': coefficients,
                            'exact_raw': data(raw), 'exact_quotient': data(normalized),
                            'saved_H': cut['H'], 'required_proper_lower': str(threshold)})
    check('full decision and retained failure', c['result']['decision'] == 'INCONCLUSIVE' and
          c['result']['negative_cuts'] == [] and c['result']['unresolved_cuts'] == [[-2, -1, 0, 1]] and
          c['result']['failures'] == ['Zero-containing cut enclosure'])
    if mesh == 128:
        # Check every displayed coarse rational row, not only its sign.
        table = [
            ('0.00114816', '0.00121249'), ('0.00224814', '0.00248407'),
            ('0.00224814', '0.00248407'), ('0.00114816', '0.00121249'),
            ('0.00182739', '0.00208212'), ('0.00339630', '0.00369656'),
            ('0.00229633', '0.00242498'), ('0.00066034', '0.00102719'),
            ('0.00339630', '0.00369656'), ('0.00182739', '0.00208212'),
            ('0.00023960', '0.00062524'), ('0.00297556', '0.00329461'),
            ('0.00297556', '0.00329461'), ('0.00023960', '0.00062524'),
            ('-0.00018115', '0.00022330')]
        for cut, (l, u) in zip(c['result']['cuts'], table):
            r = pair(cut['raw_A0_H'])
            check(f'displayed rational row {cut["S"]}', F(l) < r[0] <= r[1] < F(u))
        check('displayed normalizer range', F('0.022681') < a0[0] <= a0[1] < F('0.023'))
        check('displayed weakest-margin implication', F('0.00023960')/F('0.023') > F(1, 100))
        check('displayed full-cut implications', -F('0.00018115')/F('0.022681') > -F(1, 125) and
              F('0.00022330')/F('0.022681') < F(1, 100))
        check('displayed error scales', F(et.hi) < F('7.315e-26') and
              F(es.hi) < F('1.185e-43') and F(errors[0].hi) < F('7.181e-27') and
              all(F(e.hi) < F('1.437e-26') for e in errors[1:]) and
              F(ms[0].hi) < F('2.138e-23') and F(ms[2].hi) < F('4.866e-23'))
        full_raw = pair(c['result']['cuts'][-1]['raw_A0_H'])
        check('displayed full-cut width', full_raw[1]-full_raw[0] > F('0.000404'))
    check('original certificate unchanged', path.read_bytes() == original_bytes)
    minimum_cut = min(c['result']['cuts'][:-1], key=lambda cut: pair(cut['H'])[0])
    return {'mesh': mesh, 'input': path.name,
            'sha256': hashlib.sha256(original_bytes).hexdigest(),
            'boxes_checked': nt*nq, 'cache_entries_checked': len(keys),
            'checks': checks, 'finite_B_exact': [data(p) for p in finite],
            'moments_exact': moment_details, 'cuts': cut_details,
            'minimum_saved_proper_H_lower': minimum_cut['H']['lower'],
            'full_cut_saved_H': c['result']['cuts'][-1]['H'],
            'failures': []}


if __name__ == '__main__':
    self_check()
    output = HERE/'variable-hall-audit-139.json'
    result = {'scope': 'L905 saved M=64/128 only, no refinement',
              'contract': 'L037 Decimal/exp trusted; integer sums and comparisons exact',
              'grids': [], 'failures': []}
    try:
        for mesh in (64, 128):
            result['grids'].append(audit(mesh))
    except Exception as exc:
        result['failures'].append(f'{type(exc).__name__}: {exc}')
        output.write_text(json.dumps(result, indent=2)+'\n')
        raise
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'result': 'AUDIT_PASS',
                      'grids': [{'M': g['mesh'], 'boxes': g['boxes_checked'],
                                 'checks': len(g['checks']),
                                 'minimum_proper_H_lower': g['minimum_saved_proper_H_lower']}
                                for g in result['grids']],
                      'required_M128_proper_H': '>1/100', 'full_cut': 'INCONCLUSIVE',
                      'failures': result['failures'], 'certificate': str(output)}))
