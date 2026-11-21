#!/usr/bin/env python3
"""Exact planning certificate for C998g; no quadrature or scalar oracle run."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import numpy as np

B = Path(__file__).resolve().parent
checks, snapshots = [], {}


def check(name, condition):
    checks.append({'name': name, 'pass': bool(condition)})


def read(name):
    raw = (B / name).read_bytes()
    snapshots[name] = raw
    return json.loads(raw)


def decode(value):
    return Q(int(value['numerator']), int(value['denominator']))


def encode(value):
    value = Q(value)
    return {'numerator': str(value.numerator), 'denominator': str(value.denominator)}


def ceil(value):
    return -(-value.numerator // value.denominator)


report = {'result': 'UNFINISHED', 'checks': checks,
          'scope': 'C998g exact-node analytic ledger and prescribed direct contraction work only',
          'not_verified': ['Gauss nodes/weights or scalar evaluation enclosures',
                           'finite arithmetic error at proposed 256 fractional bits',
                           'actual square or full residual Gram entries',
                           'inverse debt, signed S3, source/core/c_* contracts or RH']}
try:
    original = read('jump-log-h1-bounds-654.json')
    audit = read('jump-log-h1-audit-655.json')
    archive = 'frozen-reference-proposal-652.npz'
    snapshots[archive] = (B / archive).read_bytes()
    pinned = '2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6'
    check('652 archive and both complete prior pins',
          sha256(snapshots[archive]).hexdigest() == pinned ==
          original['input_sha256'][archive] == audit['input_sha256'][archive])
    check('655 pins complete654 certificate',
          sha256(snapshots['jump-log-h1-bounds-654.json']).hexdigest() ==
          audit['input_sha256']['jump-log-h1-bounds-654.json'])
    check('all prior654/655 checks and failures inspected',
          len(original['checks']) == 12 and all(c['passed'] for c in original['checks']) and
          original['failures'] == [] and len(audit['checks']) == 41 and
          all(c['pass'] for c in audit['checks']) and audit['failures'] == [])
    with np.load(B / archive, allow_pickle=False) as data:
        free = data['free_middle_dyadics'].copy()
    check('complete finite binary64 shape', free.shape == (254, 3) and
          free.dtype == np.dtype('float64') and bool(np.isfinite(free).all()))
    report['exact_free_columns'] = []
    counts = []
    for j in range(3):
        values = [Q(*float(x).as_integer_ratio()) for x in free[:, j]]
        report['exact_free_columns'].append([encode(v) for v in values])
        check(f'column{j} all254 exact dyadics match654',
              values == [decode(v) for v in original['exact_free_middle_columns'][j]])
        saved = {k: decode(v) for k, v in original['columns'][j]['bounds'].items()}
        replay = {k: decode(v) for k, v in audit['columns'][j]['all_bounds'].items()}
        check(f'column{j} all11 rational ledger values match655', saved == replay)
        mass = sum(map(abs, values), Q())
        check(f'column{j} amplitude envelope recomputed', 6*mass == saved['V'] < 14)
        check(f'column{j} forcing/norm audit envelopes',
              saved['F'] + saved['H'] < 26 and saved['unprojected_l2'] < 760)
        counts.append({'column': j,
                       'even_nonzero': sum(v != 0 for n, v in enumerate(values, 2) if n % 2 == 0),
                       'odd_nonzero': sum(v != 0 for n, v in enumerate(values, 2) if n % 2 == 1)})
    count = sum(c['even_nonzero'] + c['odd_nonzero'] for c in counts)
    check('every one of762 free coefficients is nonzero', count == 762)
    report['coefficient_counts'] = counts

    eta = Q(1, 2**48)
    edge = Q(196)*Q(3, 10)*50*eta
    radial_M_prefactor = Q(3, 10)*196*Q(8, 7)*49
    check('radial complex prefactor<3300', radial_M_prefactor < 3300)
    check('radial exponential exponent<574 log2 using log2>2/3', Q(765, 2) < 574*Q(2, 3))
    radial = Q(32, 45)*3300*Q(1, 2**66)
    check('angular prefactor<84', Q(32, 45)*118 < 84)
    check('angular exponential exponent<288b log2', Q(765, 4) < 288*Q(2, 3))
    panels = []
    for j in range(1, 49):
        b = Q(1, 2**j)
        n = 32 + ceil(144*b)
        check(f'panel{j} exponent balance', 2*n >= 64 + 288*b)
        panels.append({'j': j, 'left': encode(b), 'right': encode(2*b),
                       'n_in_Trefethen_19_3': n, 'gauss_points': n+1,
                       'exact_node_error_upper': encode(Q(84, 2**64))})
    angular = Q(48*84, 2**64)
    total = edge + radial + angular
    check('all48 panels cover retained angular interval',
          panels[0]['right'] == encode(1) and panels[-1]['left'] == encode(eta) and
          all(panels[j]['left'] == panels[j+1]['right'] for j in range(47)))
    check('exact-node analytic bound<1.1e-11', total < Q(11, 10**12))
    check('analytic allowance below full1e-10 entry target', total < Q(1, 10**10))
    angular_points = sum(p['gauss_points'] for p in panels)
    pairs = 321*angular_points
    mandatory = pairs*count
    check('prescribed node inventory', angular_points == 1770 and pairs == 568170)
    check('mandatory multiplications exceed20million', mandatory > 20_000_000)
    report['prescription'] = {
        'eta': encode(eta), 'radial_n': 320, 'radial_gauss_points': 321,
        'rho': 2, 'proposed_fractional_bits_unverified': 256,
        'panels': panels, 'angular_points': angular_points, 'scaled_density_points': pairs,
        'sharing': 'cosine bases across six outputs; all unscaled density values cached',
        'contraction': 'direct coefficient sum per ordered tensor-node key; no fast transform or coefficient pruning'}
    report['error'] = {
        'corner': encode(edge), 'radial_exact_node': encode(radial),
        'angular_exact_node': encode(angular), 'total_analytic': encode(total),
        'required_total_including_finite_arithmetic': encode(Q(1, 10**10)),
        'finite_arithmetic': 'UNPAID: stopped before scalar evaluator/node/weight construction'}
    report['work'] = {
        'nonzero_free_coefficients': count, 'mandatory_real_multiplications': mandatory,
        'required_square_service_maximum': 20_000_000,
        'excess_ratio': encode(Q(mandatory, 20_000_000)),
        'other_work': 'omitted from lower count: additions, cosine generation, exact-neutral setup, kernel/diagonal, constants, nodes, weights, accumulation, registers',
        'scope': 'lower count for this prescribed direct summation, not for all integration methods'}
    check('all loaded sources preserved', all((B / name).read_bytes() == raw for name, raw in snapshots.items()))
except Exception as exc:
    check('exception: ' + type(exc).__name__ + ': ' + str(exc), False)

failures = [c['name'] for c in checks if not c['pass']]
report['failures'] = failures
report['input_sha256'] = {name: sha256(raw).hexdigest() for name, raw in snapshots.items()}
report['script_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
report['result'] = 'PASS_PLANNING_CHECKS_PRESCRIBED_WORK_FAILS' if not failures else 'FAIL'
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2) + '\n')
print(report['result'])
if not failures:
    print('Exact-node analytic entry error < 1.1e-11; required complete error <= 1e-10; finite arithmetic unpaid.')
    print('Mandatory real multiplications:', report['work']['mandatory_real_multiplications'],
          '; allowed total scalar operations:', report['work']['required_square_service_maximum'])
print('Failed finite checks:', failures)
print('Full certificate:', out.relative_to(B.parent.parent))
if failures:
    raise SystemExit(1)
