"""Exact inventory/work checks only: no profiles, loads or Gram entries evaluated."""
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
OUT = BASE / 'gaussian-dual-preflight-748.json'
WITNESS = BASE / 'defect-window-fixed-pair-707-witness.json'
checks = {}

def check(name, value):
    checks[name] = bool(value)

def prime(n):
    return n >= 2 and all(n % k for k in range(2, isqrt(n) + 1))

def prime_powers(separation):
    found = {}
    for p in range(2, 4096):
        if not prime(p):
            continue
        n = p
        while n < 4096:
            if 3**(separation-1) < n*n < 3**(separation+1):
                found[n] = p
            n *= p
    return found

p14, p7 = prime_powers(14), prime_powers(7)
check('334 U prime powers', len(p14) == 334)
check('identity2187 in U', 2187 in p14)
check('exact16 T prime powers', sorted(p7) ==
      [29,31,32,37,41,43,47,49,53,59,61,64,67,71,73,79])
events = []
for separation, powers in ((14, p14), (7, p7)):
    for n in powers:
        if n*n == 3**separation:
            continue
        exponent = separation if n*n > 3**separation else separation-1
        events.append({'separation': separation, 'n': n, 'exponent': exponent,
                       'exp_2x': F(n*n, 3**exponent)})
events.sort(key=lambda event: event['exp_2x'])
check('349 distinct interior union events', len(events) == 349 and
      all(a['exp_2x'] < b['exp_2x'] for a,b in zip(events,events[1:])))
check('all events interior', all(1 < e['exp_2x'] < 3 for e in events))
coordinates = [F(1)] + [e['exp_2x'] for e in events] + [F(3)]
ratios = [b/a for a,b in zip(coordinates, coordinates[1:])]
check('350 panels', len(ratios) == 350)
check('every panel width <1/100 by log(1+u)<u',
      all(r < F(51,50) for r in ratios))

# Proof uses K<4088, |Im z|<3/800 and e^16<3^16<2^26.
check('phase growth exponent <16', 4088*F(3,800) < 16)
check('elementary exponential majorant', 3**16 < 2**26)
check('h coefficient majorant <2^21', 1344 + 8 + 4*294912 < 2**21)
check('v coefficient majorant <2^8', 16*12 + 8 < 2**8)
check('Gaussian imaginary argument <1/4', 64*F(3,800) < F(1,4))
check('Gaussian derivative majorant <2^14', 2*64*34*2 < 2**14)
check('Gauss global rescaling factor <2', F(128,45)*F(3,5) < 2)
q_gauss, t_gauss, b_gauss = (F(1,2**33), F(1,2**46), F(1,2**66))
check('ideal q quadrature <1e-6', q_gauss < F(1,10**6))
check('ideal t quadrature <1e-6', t_gauss < F(1,10**6))
check('ideal load quadrature <1e-6', b_gauss < F(1,10**6))

panels, order, modes = len(ratios), 64, 510
nodes = panels*order
# At every node/mode: one phase product, separate sin and cos calls;
# two products and one sum for EACH of h's and (Tg)'s oscillatory parts.
categories = {'phase_products': nodes*modes,
              'sine_calls': nodes*modes,
              'cosine_calls': nodes*modes,
              'two_profile_products': nodes*modes*4,
              'two_profile_internal_sums': nodes*modes*2}
work = sum(categories.values())
cap = 10**8
check('mandatory work102816000', work == 102816000)
check('prescribed loop exceeds cap', work > cap)
check('witness pin', sha256(WITNESS.read_bytes()).hexdigest() ==
      '99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a')
failures = [name for name, ok in checks.items() if not ok]
max_index = max(range(len(ratios)), key=ratios.__getitem__)
unpaid = [
    'aggregate coefficient, exact Z, all shifts and panel preparation',
    'full K14/K7 values, both exact P0 moments and moment inverse',
    'certified nodes, weights, positions and complete value rounding',
    'leading F,G,p refinements to<=1e-6 (old intervals insufficient)',
    'd0, Gaussian norm entries, rational trial coefficient choices',
    'conditioning/solve certificates if inverse optimization is used',
    'weighted lower-comparison error, signed Schur debt and q in both roles',
    'sufficient precision, byte storage, output and replay work']
data = {
    'task': 'fixed33-Gaussian lower certificate / one aggregated Gauss preflight748',
    'witness_sha256': sha256(WITNESS.read_bytes()).hexdigest(),
    'prime_powers': {'U14': p14, 'T7': p7},
    'events': [{**event, 'exp_2x': str(event['exp_2x'])} for event in events],
    'panel_exp2_endpoint_ratios': list(map(str, ratios)),
    'largest_ratio': {'panel_index': max_index, 'ratio': str(ratios[max_index]),
                      'required_strict_upper': '51/50',
                      'implied_width_strict_upper': '1/100'},
    'ideal_exact_Gauss': {'nodes_per_panel': order, 'rho': 2,
        'q_error_strict_upper': str(q_gauss),
        'signed_t_error_strict_upper': str(t_gauss),
        'each_loading_error_strict_upper': str(b_gauss),
        'includes_value_or_rounding_error': False,
        'weighted_dual_error_certified': False},
    'prescription': {'panels': panels, 'nodes': nodes,
        'raw_modes_counted': modes, 'operations_by_category': categories,
        'mandatory_operations': work, 'required_total_upper': cap,
        'excess': work-cap, 'complete_work_cap_met': False,
        'fused_arithmetic_or_mode_recurrence_used': False,
        'scope': 'Specified separate scalar operations/direct common-phase loop only; not an optimized-algorithm lower bound.'},
    'sufficient_precision': None, 'actual_byte_storage': None,
    'all_entry_error_certified': False,
    'Gram_or_loading_or_profile_evaluated': False,
    'unpaid': unpaid, 'checks': checks, 'failures': failures,
    'decision': 'PARK this prescribed loop before any numerical Gram batch'}
OUT.write_text(json.dumps(data, indent=2)+'\n')
print(f'Checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}')
print(f'Panels={panels}, nodes={nodes}; ideal exact q error<{q_gauss}; goal<=1/1000000')
print(f'Mandatory work={work}; required total<={cap}; excess={work-cap}')
print('Precision/bytes/all-entry error: UNPAID; no Gram or load evaluated.')
print(f'Certificate: {OUT.relative_to(BASE.parent.parent)}')
raise SystemExit(bool(failures))
