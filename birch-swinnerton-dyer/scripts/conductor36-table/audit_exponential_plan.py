#!/usr/bin/env python3
"""Fixed L055 audit: full replay plus distinct exact containment checks.

Uses no producer. Original artifacts are read only. Large integer witnesses
are written in hexadecimal; all comparisons use full integers, not previews.
"""
import json
import sys
import traceback
from collections import defaultdict
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path

from verify_exponential_plan import replay

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def dump(name, data):
    path = HERE/name
    path.write_text(json.dumps(data, indent=2)+'\n')
    return str(path.relative_to(ROOT))


def audit():
    originals = [HERE/name for name in (
        'presentation.json', 'presentation_verification.json', 'plan.json',
        'plan_verification.json', 'compressed_plan.json',
        'compressed_plan_verification.json', 'coupled_plan.json',
        'coupled_plan_verification.json', 'exponential_plan.json',
        'exponential_plan_verification.json')]
    originals += [HERE.parent/'nonunitary-cusp'/name for name in (
        'reduced_phase_certificate.json', 'reduced_phase_verification.json')]
    originals += sorted((ROOT/'ATTEMPTS').glob('02[5-8]-*.md'))
    before = {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in originals}
    data = json.loads((HERE/'exponential_plan.json').read_text())
    full = replay(data)
    full['certificate_sha256'] = before['scripts/conductor36-table/exponential_plan.json']
    full_path = dump('exponential_audit_full_replay.json', full)
    assert full['replay_passed'] and full['workload_passed']
    assert full['checks'] == {'all_q_brackets': 16, 'Taylor_steps': 2560,
        'power_multiplications': 336, 'primitive_tail_rows': 98,
        'uncombined_occurrences': 1316, 'generator_width_rows': 72}
    assert not full['failures'] and not full['threshold_failures']
    print('Complete replay passed:', full['checks'], 'report=', full_path, flush=True)

    D, exponent = 2**96, 4861
    degree = 200
    remainder = Q(8**(degree+1), factorial(degree+1))
    # D^(exponent-1), shared by the exact endpoint-power comparisons.
    common = D**(exponent-1)
    attenuation = []
    for index, row in enumerate(data['attenuation']):
        l, u = (Q(x, D) for x in row['w'])
        assert -8 <= l <= u < 0
        center, delta = (l+u)/2, (u-l)/2
        # Exact Horner, with no rounded interval recurrence:
        # P_k(c)=1+c/(k+1)+... encoded from the top degree downwards.
        polynomial = Q(1)
        for k in range(degree, 0, -1):
            polynomial = 1+center*polynomial/k
        error = delta+remainder
        inner = [polynomial-error, polynomial+error]
        q0, q1 = row['q']
        assert 0 < Q(q0, D) <= inner[0] <= inner[1] <= Q(q1, D) < 1
        # Exact endpoint integer powers bypass every rounded binary step.
        lower_power, upper_power = pow(q0, exponent), pow(q1, exponent)
        p0, p1 = row['power_interval']
        assert 0 <= p0*common <= lower_power <= upper_power <= p1*common
        # Independently cross-multiply each saved majorant endpoint.
        lower_tail, upper_tail = map(Q, row['tail_bounds'])
        assert lower_tail >= 0 and upper_tail >= lower_tail
        assert lower_tail.numerator*common*(D-q0) <= lower_power*lower_tail.denominator
        assert upper_power*upper_tail.denominator <= upper_tail.numerator*common*(D-q1)
        attenuation.append({'id': index, 'y': row['y'],
            'argument': list(map(str, (l, u))), 'center': str(center),
            'argument_radius': str(delta), 'degree': degree,
            'exact_polynomial': str(polynomial), 'remainder': str(remainder),
            'independent_containing_bracket': list(map(str, inner)),
            'inside_saved_q': True, 'q_numerators': [q0, q1],
            'scale': D, 'exponent': exponent,
            'exact_power_numerators_hex': [hex(lower_power), hex(upper_power)],
            'power_denominator_exponent': exponent,
            'saved_power_interval': [p0, p1], 'exact_power_contained': True,
            'tail_bounds': row['tail_bounds'], 'exact_tail_contained': True})

    # Aggregate positive occurrence weights by height only after taking each
    # absolute value. This is an alternate sum order, never signed cancellation.
    saved = json.loads((HERE/'coupled_plan.json').read_text())
    omega = Q(full['period']['lower'])
    assert omega == Q(166638467572977606763020498997, 2**95) > 0
    width_rows = []
    occurrences = 0
    for i, (g, row) in enumerate(zip(saved['generators'], data['generators'])):
        weights = defaultdict(Q)
        for point, weight in g['occurrences']:
            a = data['primitives'][point]['attenuation_id']
            weights[a] += abs(Q(weight))
            occurrences += 1
        bounds = [2*sum((w*Q(attenuation[a]['tail_bounds'][s])
                          for a, w in weights.items()), Q(0))/omega for s in (0, 1)]
        assert list(map(Q, row['normalized_tail_width_bounds'])) == bounds
        assert 0 <= bounds[0] <= bounds[1] <= Q(1, 2**60) < Q(1, 2**38)
        width_rows.append({'id': i, 'positive_height_weights':
            [[a, str(w)] for a, w in sorted(weights.items())],
            'normalized_tail_width_bounds': list(map(str, bounds)),
            'passes_2_minus_60': True, 'passes_2_minus_38': True})
    assert occurrences == 1316 and len(width_rows) == 72
    worst = max(range(72), key=lambda i: Q(width_rows[i]['normalized_tail_width_bounds'][1]))
    assert worst == 28 and data['generators'][worst]['endpoints'] == [[-1, 27], [0, 1]]
    workload = sum(p['H'] for p in data['primitives'])
    assert len(data['primitives']) == 98 and workload == 476280 <= 1000000
    assert all(p['H'] == 4860 for p in data['primitives'])
    assert all(Q(p['tail_bounds'][1]) <= Q(data['uniform_rho']) for p in data['primitives'])

    # Retest the historical lower contribution to the dyadic majorant, not
    # a lower bound for the analytic error, using the same uncombined rows.
    selected = [(j, Q(w)) for j, w in saved['generators'][28]['occurrences']
                if Q(saved['primitives'][j]['y']) == Q(1, 684)]
    assert len(selected) == 2 and {j for j, _ in selected} == {5, 34}
    dyadic = 2*sum((abs(w) for _, w in selected), Q(0))*Q(57, 2**41)/omega
    assert dyadic == Q(684547143360315392, 166638467572977606763020498997) > Q(1, 2**38)
    old_report = json.loads((HERE/'coupled_plan_verification.json').read_text())
    assert Q(old_report['cutoff_obstruction']['selected_contribution']) == dyadic
    assert full['preserved_upstream_threshold_failures'] == ['maximum cutoff exceeds 4860']

    after = {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in originals}
    assert before == after
    certificate = {'schema': 'L055-fixed-independent-containment-audit-v1',
        'attenuation': attenuation, 'generators': width_rows,
        'original_sha256_before': before, 'original_sha256_after': after,
        'original_bytes_preserved': True,
        'dyadic_stop': {'selected_occurrences': [[j, str(w)] for j, w in selected],
                       'contribution': str(dyadic), 'required': str(Q(1, 2**38)),
                       'still_exceeds_required': True}}
    evidence_path = dump('exponential_audit_containment.json', certificate)
    result = {'audit_passed': True, 'failures': [], 'full_replay': full_path,
        'independent_evidence': evidence_path,
        'actual': {'attenuation_containments': len(attenuation),
                   'exact_power_endpoint_tests': 2*len(attenuation),
                   'exact_tail_endpoint_tests': 2*len(attenuation),
                   'uncombined_occurrences': occurrences, 'generator_widths': len(width_rows),
                   'distinct_terms': workload, 'max_H': 4860},
        'required': {'attenuation_containments': 16, 'exact_power_endpoint_tests': 32,
                     'exact_tail_endpoint_tests': 32, 'uncombined_occurrences': 1316,
                     'generator_widths': 72, 'distinct_terms_at_most': 1000000,
                     'max_H_at_most': 4860, 'normalized_width_at_most': str(Q(1, 2**38))},
        'worst_generator_id': worst,
        'worst_width_bounds': width_rows[worst]['normalized_tail_width_bounds'],
        'every_width_at_most': str(Q(1, 2**60)),
        'original_bytes_preserved': before == after, 'preserved_original_count': len(before),
        'dyadic_stop_preserved': True,
        'scope': 'L055 fixed tail feasibility only; upstream instance audits pending; no table'}
    return result


if __name__ == '__main__':
    try:
        result = audit()
    except Exception as exc:
        result = {'audit_passed': False, 'failures': [repr(exc)], 'traceback': traceback.format_exc()}
    destination = dump('exponential_critical_audit.json', result)
    print('L055 audit=', result['audit_passed'], 'actual=', result.get('actual'),
          'required=', result.get('required'), 'failures=', result['failures'], 'report=', destination)
    raise SystemExit(0 if result['audit_passed'] else 1)
