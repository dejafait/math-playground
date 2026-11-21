"""Independent exact audit of748's complete finite evidence; no Gram evaluation."""
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt, prod
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
ORIGINAL = BASE / 'gaussian-dual-preflight-748.json'
WITNESS = BASE / 'defect-window-fixed-pair-707-witness.json'
OUT = BASE / 'gaussian-dual-audit-750.json'
old = json.loads(ORIGINAL.read_text())
checks = {}


def check(name, condition):
    checks[name] = bool(condition)


def factor(n):
    """Trial division of every candidate, rather than prime-power generation."""
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


inventory = {}
factorizations = {}
for m, label in ((7, 'T7'), (14, 'U14')):
    active = {}
    rows = []
    for n in range(isqrt(3**(m-1)) + 1, isqrt(3**(m+1)) + 1):
        if not 3**(m-1) < n*n < 3**(m+1):
            continue
        fac = factor(n)
        check(f'factorization {m}/{n}',
              n == prod(p**e for p, e in fac.items()))
        selected = len(fac) == 1
        rows.append({'n': n, 'factors': fac, 'prime_power': selected})
        if selected:
            active[n] = next(iter(fac))
    inventory[label] = active
    factorizations[label] = rows
    check(f'entire {label} prime-power map',
          {int(n): p for n, p in old['prime_powers'][label].items()} == active)

events = []
for m, label in ((7, 'T7'), (14, 'U14')):
    for n in inventory[label]:
        if n*n == 3**m:
            continue
        exponent = m if n*n > 3**m else m-1
        events.append({'separation': m, 'n': n, 'exponent': exponent,
                       'exp_2x': str(F(n*n, 3**exponent))})
events.sort(key=lambda e: F(e['exp_2x']))
check('entire ordered event records agree', events == old['events'])
xs = [F(1)] + [F(e['exp_2x']) for e in events] + [F(3)]
panels = []
for i, (left, right) in enumerate(zip(xs, xs[1:])):
    ratio = right / left
    panels.append({'index': i, 'left_exp2': str(left), 'right_exp2': str(right),
                   'ratio': str(ratio), 'strict_order': left < right,
                   'below_51_over_50': ratio < F(51, 50),
                   'rational_width_upper': str((ratio - 1)/2),
                   'width_upper_below_1_over_100': (ratio - 1)/2 < F(1, 100)})
    check(f'complete panel {i}', left < right and ratio < F(51, 50)
          and str(ratio) == old['panel_exp2_endpoint_ratios'][i])
ratios = [F(row['ratio']) for row in panels]
check('entire ratio list length', len(old['panel_exp2_endpoint_ratios']) == len(ratios))
largest = max(range(len(ratios)), key=ratios.__getitem__)
check('entire largest-ratio record', old['largest_ratio'] == {
    'panel_index': largest, 'ratio': str(ratios[largest]),
    'required_strict_upper': '51/50', 'implied_width_strict_upper': '1/100'})

# Rational bounds supporting the analytic prose, not evaluations of h or v.
bounds = {
    'ellipse_imag_upper': F(3, 800), 'ellipse_real_extension_upper': F(1, 800),
    'kernel_real_argument_lower': 6*F(1, 2)-F(1, 800),
    'phase_exponent_upper': 4088*F(3, 800),
    'projection_abs_real_exponent_upper': (F(3, 5)+F(1, 800))/2,
    'gaussian_imag_upper': 64*F(3, 800),
    'gaussian_real_abs_upper': 32+64*F(1, 800),
    'h_coefficient_upper': F(1344+8+4*294912),
    'v_coefficient_upper': F(192+8),
    'gaussian_derivative_upper': F(2*64*34*2),
    'gauss_length_factor': F(128, 45)*F(3, 5),
}
check('kernel open half-plane margin', bounds['kernel_real_argument_lower'] > 2)
check('projection exponential bounded by sqrt(e)<2',
      bounds['projection_abs_real_exponent_upper'] < F(1, 2))
check('Gaussian real argument <33', bounds['gaussian_real_abs_upper'] < 33)
check('Gaussian modulus <34', 33**2+F(1, 4)**2 < 34**2)
check('Gaussian e^(1/16)<2 majorant', 3 < 2**16)
ideal = {'nodes_per_panel': 64, 'rho': 2,
         'q_error_strict_upper': str(F(1, 2**33)),
         'signed_t_error_strict_upper': str(F(1, 2**46)),
         'each_loading_error_strict_upper': str(F(1, 2**66)),
         'includes_value_or_rounding_error': False,
         'weighted_dual_error_certified': False}
check('entire ideal exact Gauss record', old['ideal_exact_Gauss'] == ideal)
for label, exponent, bound_exponent in (('q', 94, 33), ('t', 81, 46), ('b', 61, 66)):
    check(f'{label} affine rescaling and error exponent',
          bounds['gauss_length_factor'] * F(2**exponent, 2**128)
          < F(1, 2**bound_exponent))

# Independent count of the literal expression syntax specified in C998y.
node_count = len(panels)*64
mode_count = len(range(2, 512))
visits = node_count * mode_count
category = {'phase_products': visits, 'sine_calls': visits, 'cosine_calls': visits,
            'two_profile_products': 4*visits, 'two_profile_internal_sums': 2*visits}
work = sum(category.values())
prescription = {
    'panels': len(panels), 'nodes': node_count, 'raw_modes_counted': mode_count,
    'operations_by_category': category, 'mandatory_operations': work,
    'required_total_upper': 10**8, 'excess': work-10**8,
    'complete_work_cap_met': False, 'fused_arithmetic_or_mode_recurrence_used': False,
    'scope': 'Specified separate scalar operations/direct common-phase loop only; not an optimized-algorithm lower bound.'}
check('entire prescription record', old['prescription'] == prescription)
pin = sha256(WITNESS.read_bytes()).hexdigest()
check('original witness hash field', old['witness_sha256'] == pin)

# Recompute every original assertion, without trusting its Boolean value.
original_checks = {
    '334 U prime powers': len(inventory['U14']) == 334,
    'identity2187 in U': 2187 in inventory['U14'],
    'exact16 T prime powers': sorted(inventory['T7']) ==
        [29,31,32,37,41,43,47,49,53,59,61,64,67,71,73,79],
    '349 distinct interior union events': len(events) == 349 and
        len(set(e['exp_2x'] for e in events)) == 349,
    'all events interior': all(1 < F(e['exp_2x']) < 3 for e in events),
    '350 panels': len(panels) == 350,
    'every panel width <1/100 by log(1+u)<u': all(r < F(51,50) for r in ratios),
    'phase growth exponent <16': bounds['phase_exponent_upper'] < 16,
    'elementary exponential majorant': 3**16 < 2**26,
    'h coefficient majorant <2^21': bounds['h_coefficient_upper'] < 2**21,
    'v coefficient majorant <2^8': bounds['v_coefficient_upper'] < 2**8,
    'Gaussian imaginary argument <1/4': bounds['gaussian_imag_upper'] < F(1,4),
    'Gaussian derivative majorant <2^14': bounds['gaussian_derivative_upper'] < 2**14,
    'Gauss global rescaling factor <2': bounds['gauss_length_factor'] < 2,
    'ideal q quadrature <1e-6': F(1,2**33) < F(1,10**6),
    'ideal t quadrature <1e-6': F(1,2**46) < F(1,10**6),
    'ideal load quadrature <1e-6': F(1,2**66) < F(1,10**6),
    'mandatory work102816000': work == 102816000,
    'prescribed loop exceeds cap': work > 10**8,
    'witness pin': pin == '99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a',
}
check('entire original assertion dictionary', old['checks'] == original_checks)
check('all original assertions independently true', all(original_checks.values()))
check('original failure list', old['failures'] == [])
check('unpaid precision bytes and errors remain explicit',
      old['sufficient_precision'] is None and old['actual_byte_storage'] is None
      and old['all_entry_error_certified'] is False
      and old['Gram_or_loading_or_profile_evaluated'] is False and len(old['unpaid']) == 8)
failures = [key for key, value in checks.items() if not value]
data = {
    'task': 'C998y conceptual-audit finite certificate750',
    'input_sha256': {p.name: sha256(p.read_bytes()).hexdigest()
                     for p in (ORIGINAL, BASE/'gaussian-dual-preflight-748.py', WITNESS)},
    'factorizations': factorizations, 'prime_powers': inventory,
    'events': events, 'complete_panel_checks': panels,
    'largest_ratio': {'panel_index': largest, 'ratio': str(ratios[largest]),
                      'required_strict_upper': '51/50'},
    'analytic_rational_bounds': {key: str(val) for key, val in bounds.items()},
    'ideal_exact_Gauss': ideal, 'prescription': prescription,
    'original_assertions_recomputed': original_checks,
    'checks': checks, 'failures': failures,
    'all_cases_compared': {'events': len(events), 'panels': len(panels),
                          'original_assertions': len(original_checks)},
    'unpaid': old['unpaid'],
    'limitations': ['Finite checks do not prove the analytic reasoning.',
                   'Inherited response, neutral-core and c_* certificates not revalidated.',
                   'No profile, load, Gaussian matrix, inverse or Gram evaluated.',
                   'Only the specified loop is stopped; no algorithmic lower bound.'],
    'decision': 'UPHOLD finite evidence748' if not failures else 'FAIL audit; inspect failures'}
OUT.write_text(json.dumps(data, indent=2) + '\n')
print(f'Checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}')
print(f'Entire comparisons: {len(events)} events, {len(panels)} panels, {len(original_checks)} original assertions.')
print(f'Max ratio={ratios[largest]} < required51/50; ideal q,t,b errors<2^-33,2^-46,2^-66.')
print(f'Specified work={work}; required total<={10**8}; excess={work-10**8}.')
print('Precision, bytes and complete entry errors remain UNPAID. No Gram/load evaluated.')
print(f'Certificate: {OUT.relative_to(BASE.parent.parent)}')
raise SystemExit(bool(failures))
