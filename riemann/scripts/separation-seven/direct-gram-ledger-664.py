#!/usr/bin/env python3
"""Exact finite ledger for C998e; no quadrature or special-function batch.

Checks bounds and the cost of the explicitly prescribed direct first-order
digamma recurrence only. Analytic identities and applicability are in C998e.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import numpy as np

B = Path(__file__).resolve().parent
checks = []
pins = {}


def check(name, condition):
    checks.append({'name': name, 'pass': bool(condition)})


def read(name):
    data = (B / name).read_bytes()
    pins[name] = sha256(data).hexdigest()
    return json.loads(data)


def dec(x):
    return Q(int(x['numerator']), int(x['denominator']))


def enc(x):
    if isinstance(x, Q):
        return {'numerator': str(x.numerator), 'denominator': str(x.denominator)}
    if isinstance(x, dict):
        return {k: enc(v) for k, v in x.items()}
    if isinstance(x, list):
        return [enc(v) for v in x]
    return x


old = read('jump-log-h1-bounds-654.json')
audit = read('jump-log-h1-audit-655.json')
check('655 pins complete654', audit['input_sha256']['jump-log-h1-bounds-654.json'] ==
      pins['jump-log-h1-bounds-654.json'])
check('655 reports no finite failures', audit['failures'] == [])
archive = B / 'frozen-reference-proposal-652.npz'
pins[archive.name] = sha256(archive.read_bytes()).hexdigest()
check('pinned652 archive', pins[archive.name] ==
      '2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6')
with np.load(archive, allow_pickle=False) as data:
    raw = data['free_middle_dyadics'].copy()
check('exact trial shape and finite binary64', raw.shape == (254, 3) and
      raw.dtype == np.dtype('float64') and bool(np.isfinite(raw).all()))
rows = old['exact_X_witness']['integer_columns_by_row']
check('exact witness shape/denominator', len(rows) == 32 and all(len(x) == 3 for x in rows)
      and old['exact_X_witness']['denominator'] == 2**24)
columns = []
for j in range(3):
    q = [Q(*float(x).as_integer_ratio()) for x in raw[:, j]]
    check(f'all254 exact trial coefficients column{j}', q ==
          [dec(x) for x in old['exact_free_middle_columns'][j]])
    f = [Q(row[j], 2**24) for row in rows[:16]]
    h = [Q(row[j], 2**24) for row in rows[16:]]
    F, H, V = [6*sum(map(abs, v), Q()) for v in (f, h, q)]
    saved = old['columns'][j]['bounds']
    check(f'654/655 envelopes column{j}',
          [F, H, V] == [dec(saved[k]) for k in ('F', 'H', 'V')] ==
          [dec(audit['columns'][j]['all_bounds'][k]) for k in ('F', 'H', 'V')])
    check(f'common amplitude/forcing/norm bounds column{j}',
          F+H < 26 and V < 14 and 5*(F+H)+45*V < 760)
    columns.append({'column': j, 'F': F, 'H': H, 'V': V,
                    'raw_norm_bound': 5*(F+H)+45*V})

active = [n for n in range(2, 256) if any(raw[n-2, j] != 0 for j in range(3))]
check('all254 free diagonal modes are used', active == list(range(2, 256)))
check('bounded parity action', Q(3, 2)*(17*26+21*14)+Q(43, 2)*14 < 1500)

tau = Q(3, 10)*Q(1, 2**80)  # upper bound on a*2^-80
A = Q(1500+7*81)
raw_edge = 2*tau*(A*A+14*A+98)
moment_edge = 6*tau*(A+7)  # per moment component
projection_edge = 384*(3040*moment_edge+2*moment_edge**2)
edge = raw_edge+projection_edge
check('complete output-edge and projection loss below1e-14', edge < Q(1, 10**14))
r, N = Q(1, 64), 12
suffix = 3*r**N*(Q(N)/(1-r)+r/(1-r)**2)
suffix_action = 26*suffix
suffix_gram = (1520+suffix_action)*suffix_action
check('complete forcing suffix including products below1e-14', suffix_gram < Q(1, 10**14))

eps_i, eps_m, eps_g = Q(1, 10**9), Q(1, 10**16), Q(1, 10**16)
moment_solve = eps_i+384*(2150*eps_m+eps_m**2)+eps_g*(1075+eps_m)**2
check('conditional integration/moment/inverse error below2e-9', moment_solve < Q(2, 10**9))

diag_analytic = Q(1, 2**45)
diag_round = Q(1, 2**47)
diag_action = 14*(diag_analytic+diag_round)
diag_gram = (1520+diag_action)*diag_action
check('prescribed diagonal contribution below1e-9', diag_gram < Q(1, 10**9))
check('moment norm bound survives diagonal perturbation',
      Q(99, 70)**2 > 2 and Q(99, 70)*(760+diag_action) < 1075)
K_excluded, K_sufficient = 2800000, 3000000
remainder_lower = Q(7, 30)/((Q(K_excluded)+Q(1, 4))**2+1020**2)
remainder_upper = Q(1, 4)/(Q(K_sufficient)+Q(1, 4))**2
check('every shift through2800000 fails declared remainder budget', remainder_lower > diag_analytic)
check('shift3000000 suffices for analytic remainder only', remainder_upper < diag_analytic)
divisions_min = len(active)*(K_excluded+1)
check('shared diagonal reciprocal count alone exceeds total ceiling', divisions_min > 100000000)

beta = Q(219999, 1000000)
u = Q(1, 10**10)
trial_entry_error = 932*u+3*u*u+Q(3, 10**9)
trial_op_error = 3*trial_entry_error
gram_op_radius = Q(3, 10**8)
pairing_radius = trial_op_error+gram_op_radius/beta
check('conditional numerical inverse-upper radius below1e-4', pairing_radius < Q(1, 10000))
check('outward padding excess below1e-6', 2*pairing_radius < Q(1, 10**6))
total_allocated = edge+suffix_gram+moment_solve+diag_gram+Q(3, 10**9)
check('conditional full entry allocation below1e-8', total_allocated < Q(1, 10**8))

report = {
    'result': 'LOCAL_LEDGER_CHECKS_PASS_DIRECT_FIRST_ORDER_DIAGONAL_STOP',
    'scope': 'Exact finite bounds and prescribed recurrence cost; analytic proof in C998e, no Gram computation',
    'checks': checks, 'failures': [c['name'] for c in checks if not c['pass']],
    'columns': columns, 'active_shared_diagonal_modes': active,
    'endpoint': {'tau_upper': tau, 'log_majorant': 81, 'raw': raw_edge,
                 'moment_component': moment_edge, 'projected_gram': edge},
    'forcing_suffix': {'first_omitted_index': N, 'bound': suffix,
                       'action': suffix_action, 'gram': suffix_gram},
    'conditional_moment_solve_error': moment_solve,
    'diagonal': {'analytic_allowance': diag_analytic, 'rounding_allowance': diag_round,
                 'gram_contribution': diag_gram, 'excluded_shifts_through': K_excluded,
                 'remainder_lower_at_excluded_shift': remainder_lower,
                 'sufficient_shift_for_analytic_bound_only': K_sufficient,
                 'remainder_upper_at_sufficient_shift': remainder_upper,
                 'required_divisions_lower_bound': divisions_min,
                 'total_work_ceiling': 100000000,
                 'excess_lower_bound': divisions_min-100000000},
    'conditional_inverse_pairing': {'beta': beta, 'forcing_column_norm_bound': 130,
        'trial_column_norm_bound': 14, 'B0_trial_column_norm_bound': 630,
        'trial_entry_error': trial_entry_error, 'operator_radius': pairing_radius,
        'required_radius': Q(1, 10000), 'padding_excess': 2*pairing_radius},
    'conditional_total_entry_allocation': total_allocated,
    'unpaid': ['analytic/rounded quadrature nodes and weights', 'interior product-kernel evaluator',
              'interface strip setup', 'all actual scalar enclosures and moment solve',
              'complete quadrature work ledger', 'actual residual Gram and inverse remainder size',
              'signed S3 comparison and inherited source/core contracts'],
    'input_sha256': pins, 'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
}
out = B / 'direct-gram-ledger-664.json'
out.write_text(json.dumps(enc(report), indent=2)+'\n')
print(f"checks={len(checks)} failures={report['failures']}")
print(f'diagonal divisions>{divisions_min-1}; required total<=100000000; prescription STOP')
print(f'conditional Gram entry error<{float(total_allocated):.6g}; required<=1e-8')
print(f'conditional inverse numerical radius<{float(pairing_radius):.6g}; required<=1e-4')
print('No Gram, scalar batch or sign certificate computed.')
print(out.relative_to(B.parent.parent))
if report['failures']:
    raise SystemExit(1)
