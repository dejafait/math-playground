#!/usr/bin/env python3
"""Exact Fraction replay of every saved Gaussian root/weight enclosure.

This checks the finite evidence, not the moment preparation theorem or a
complete work upper bound. No numerical root solver is used in this replay.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json

HERE = Path(__file__).resolve()
SOURCE = HERE.with_name('spectral-block-compression-728.json')
OUT = HERE.with_suffix('.json')
data = json.loads(SOURCE.read_text())
checks = []


def ck(name, yes):
    checks.append({'name': name, 'passed': bool(yes)})


def iv(a):
    return tuple(map(F, a))


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def mul(a, b):
    vals = [x*y for x in a for y in b]
    return min(vals), max(vals)


def divide(a, b):
    assert b[0] > 0
    return mul(a, (1/b[1], 1/b[0]))


def evaluate(p, t):
    result = p[-1]
    for a in reversed(p[:-1]):
        result = add(mul(result, t), a)
    return result


def contains(a, b):
    return a[0] <= b[0] <= b[1] <= a[1]


ck('complete consecutive Gaussian blocks', [row['k'] for row in data['blocks']] == list(range(5, 72)))
coefficient_error, root_count = F(0), 0
for row in data['blocks']:
    k, J = row['k'], row['J']
    p = list(map(iv, row['degree17_polynomial']))
    pp = [[iv(v) for v in pol] for pol in row['orthogonal_polynomials']]
    hh = list(map(iv, row['norms']))
    ck(f'block{k} monic degree and positive norms', len(p) == 18 and p[-1] == (1, 1) and all(h[0] > 0 for h in hh))
    previous, err = F(-1), F(0)
    for i, node in enumerate(row['nodes']):
        r, wbox = iv(node['root_bracket']), iv(node['weight_enclosure'])
        t, w, rate = map(F, (node['t'], node['weight'], node['rate']))
        ck(f'block{k} node{i} disjoint interior bracket', -1 < r[0] < r[1] < 1 and previous < r[0])
        previous = r[1]
        left, right = evaluate(p, (r[0], r[0])), evaluate(p, (r[1], r[1]))
        ck(f'block{k} node{i} exact opposite endpoint signs', (left[1] < 0 < right[0]) or (right[1] < 0 < left[0]))
        kernel = (F(0), F(0))
        for pol, h in zip(pp, hh):
            value = evaluate(pol, r)
            kernel = add(kernel, divide(mul(value, value), h))
        weight = divide((F(1, 4*J), F(1, 4*J)), kernel)
        ck(f'block{k} node{i} weight enclosure', contains(wbox, weight) and wbox[0] > 0)
        ck(f'block{k} node{i} exact output rate/weight', contains(r, (t, t)) and contains(wbox, (w, w)) and rate == J*(t+3) and rate > 0 and w > 0)
        err += max(w-wbox[0], wbox[1]-w)+w*max(t-r[0], r[1]-t)
        root_count += 1
    ck(f'block{k} complete root count', len(row['nodes']) == 17)
    ck(f'block{k} coefficient error bound', err <= F(row['coefficient_kernel_error_upper']))
    coefficient_error += F(row['coefficient_kernel_error_upper'])

theory = F(30*2**46, 5**34)+F(2**46, 4*2**72-3)
ck('exact theoretical formula', theory == F(data['theoretical']['sum_upper_bound']))
ck('full coefficient bound', coefficient_error*2**46 == F(data['coefficient_error_weighted_bound']))
ck('rank1171', root_count+32 == 1171)
ck('weighted coefficient/rate bound below1e-21', coefficient_error*2**46 < F(1, 10**21))
ck('full weighted error below1e-7', theory+coefficient_error*2**46 < F(1, 10**7))
ck('constructor has no recorded failures', not data['failures'])
report = {'scope': 'all finite node brackets, positive weight enclosures, exact output rates and uniform coefficient budget; source/moment derivation and work upper bound not verified',
          'source_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
          'replay_script_sha256': sha256(HERE.read_bytes()).hexdigest(),
          'checks': checks, 'failed_checks': [c['name'] for c in checks if not c['passed']],
          'all_checks_pass': all(c['passed'] for c in checks), 'root_count': root_count,
          'rank': root_count+32, 'weighted_uniform_bound': str(theory+coefficient_error*2**46),
          'required': '1/10000000', 'complete_work_ledger_certified': False}
OUT.write_text(json.dumps(report, indent=2)+'\n')
print('Exact enclosure replay:', sum(c['passed'] for c in checks), '/', len(checks), '; failures:', report['failed_checks'])
print('Weighted uniform error:', float(theory+coefficient_error*2**46), '; required <=1e-7; work cap UNPAID')
print('Certificate:', OUT.relative_to(HERE.parent.parent.parent))
if report['failed_checks']:
    raise SystemExit(1)
