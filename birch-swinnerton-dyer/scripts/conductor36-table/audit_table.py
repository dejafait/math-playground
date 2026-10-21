#!/usr/bin/env python3
"""L056 distinct fixed audit: exact rational containment and integer checks.

No producer or replay implementation is imported. Complete replay is a
separate prerequisite, saved in table-critical-audit/full-replay.json.
All witnesses, including exact rational polynomials, are saved to disk.
"""
import json
import sys
import traceback
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial, gcd, lcm
from pathlib import Path

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE/'table-critical-audit'
D = 2**96


def dump(name, data):
    path = OUT/name
    path.write_text(json.dumps(data, indent=2)+'\n')
    return str(path.relative_to(ROOT))


def read(name):
    return json.loads((HERE/name).read_text())


def check(condition, context):
    if not condition:
        raise AssertionError(context)


def signed_interval(data, weights):
    """Exact sums of the individual signed endpoints; no dyadic rounding."""
    lo = hi = Q(0)
    trace = []
    for j, w in weights:
        w = Q(w)
        a, b = (Q(t, D) for t in data[j]['enclosure'])
        left, right = (w*a, w*b) if w >= 0 else (w*b, w*a)
        lo += left
        hi += right
        trace.append([j, str(w), str(left), str(right), str(lo), str(hi)])
    return lo, hi, trace


def audit():
    data = read('table_certificate.json')
    geometry = read('coupled_plan.json')
    structure = read('presentation.json')
    full = json.loads((OUT/'full-replay.json').read_text())
    check(full['certificate_sha256'] == sha256((HERE/'table_certificate.json').read_bytes()).hexdigest(),
          'full replay certificate identity')
    check(full['replay_passed'] and full['table_complete'] and not full['failures'], 'complete replay')
    check(full['checks'] == {'primitive_records': 98, 'Fourier_terms': 476280,
        'zero_coefficient_terms_retained': 423360, 'cosine_Taylor_steps': 149760,
        'attenuation_brackets': 16, 'uncombined_signed_occurrences': 1316,
        'signed_quotient_endpoints': 288, 'integer_isolations': 72,
        'source_relations': 144, 'saturated_columns': 59,
        'quotient_coordinates': 13, 'generator_reconstructions': 72}, 'complete replay counts')

    # Independent exact Horner polynomial at the midpoint. On the real line,
    # cosine is 1-Lipschitz. Taylor degree 80 on [-4,4] has error <=4^81/81!.
    # This bypasses every rounded theta-square/term/partial-sum recurrence.
    phases = []
    remainder = Q(4**81, factorial(81))
    pi_lo, pi_hi = (Q(t, D) for t in data['arithmetic_evidence']['pi']['interval'])
    for i, row in enumerate(data['phases']):
        x = Q(row['phase'])
        exact_arguments = sorted((2*x*pi_lo, 2*x*pi_hi))
        a, b = (Q(t, D) for t in row['theta'])
        check(-4 <= a <= exact_arguments[0] <= exact_arguments[1] <= b <= 4, ('phase argument', i))
        center, delta = (a+b)/2, (b-a)/2
        square = center*center
        polynomial = Q(1)
        for k in range(40, 0, -1):
            polynomial = 1-square*polynomial/((2*k)*(2*k-1))
        error = delta+remainder
        inner = [polynomial-error, polynomial+error]
        lo, hi = (Q(t, D) for t in row['cosine'])
        check(lo <= inner[0] <= inner[1] <= hi, ('cosine containment', i, str(x)))
        phases.append({'id': i, 'phase': str(x), 'argument': list(map(str, (a, b))),
            'center': str(center), 'radius': str(delta), 'exact_polynomial': str(polynomial),
            'taylor_remainder': str(remainder), 'containing_bracket': list(map(str, inner)),
            'saved_bracket': list(map(str, (lo, hi))), 'contained': True})
        if (i+1) % 624 == 0:
            print('distinct cosine containment:', i+1, '/3744', flush=True)
    check(len(phases) == 3744, 'phase count')
    phase_path = dump('cosine-containment.json', {'degree': 80, 'phases': phases, 'failures': []})

    # Sign cases produce extrema without using the production four-corner
    # minimum/maximum operation. Integer recovery uses direct inequalities
    # excluding both adjacent integers, independently of saved ceil/floor.
    p, q = (Q(t, D) for t in data['arithmetic_evidence']['period']['total'])
    check(0 < p <= q, 'positive independent period')
    generator_rows, integers, sign_counts = [], [], {'positive': 0, 'negative': 0, 'crossing': 0}
    occurrences = 0
    for i, (row, g) in enumerate(zip(data['generators'], geometry['generators'])):
        a, b, trace = signed_interval(data['primitives'], g['occurrences'])
        occurrences += len(trace)
        stored_a, stored_b = (Q(t, D) for t in row['integral'])
        check(stored_a <= a <= b <= stored_b, ('exact signed sum containment', i))
        if a >= 0:
            lower, upper, case = a/q, b/p, 'positive'
        elif b <= 0:
            lower, upper, case = a/p, b/q, 'negative'
        else:
            lower, upper, case = a/p, b/p, 'crossing'
        sign_counts[case] += 1
        saved_lo, saved_hi = (Q(t, D) for t in row['normalized'])
        check(saved_lo <= lower <= upper <= saved_hi, ('signed division containment', i))
        # Finite enumeration is determined only by the containing interval.
        start = (24*lower).__floor__()-1
        stop = (24*upper).__ceil__()+1
        candidates = [m for m in range(start, stop+1) if 24*lower <= m <= 24*upper]
        check(len(candidates) == 1, ('independent integer enumeration', i, candidates))
        m = candidates[0]
        check(m-1 < 24*saved_lo <= m <= 24*saved_hi < m+1, ('adjacent integer exclusion', i))
        check(m == row['scaled_integer'] and Q(m, 24) == Q(row['value']), ('recovered value', i))
        check(saved_hi-saved_lo <= Q(1, 2**60) < Q(1, 2**38), ('actual width', i))
        # Recheck all four recorded quotient identities by multiplication.
        recorded = list(map(Q, row['quotient_endpoints']))
        check(len(recorded) == 4, ('quotient count', i))
        residuals = [v*den-num for v, (num, den) in zip(recorded,
            ((stored_a, p), (stored_a, q), (stored_b, p), (stored_b, q)))]
        check(all(t == 0 for t in residuals), ('quotient endpoint identities', i))
        integers.append(m)
        generator_rows.append({'id': i, 'occurrences': trace,
            'exact_integral': list(map(str, (a, b))), 'sign_case': case,
            'independent_normalized': list(map(str, (lower, upper))),
            'saved_normalized': list(map(str, (saved_lo, saved_hi))),
            'enumeration_range': [start, stop], 'integer_candidates': candidates,
            'adjacent_integer_margins': [str(24*saved_lo-(m-1)), str(m+1-24*saved_hi)],
            'quotient_cross_product_residuals': list(map(str, residuals)),
            'width': str(saved_hi-saved_lo)})
    check(len(generator_rows) == 72 and occurrences == 1316, 'all signed rows/occurrences')

    # Work at integer scale 24, using column accumulation instead of rational
    # row-dot-products. This preserves exact zero and saturation tests.
    A = structure['A']['entries']
    pr = structure['presentation']
    source = [0]*144
    saturated, quotient = [0]*59, [0]*13
    for i, m in enumerate(integers):
        for j in range(144):
            source[j] += A[j][i]*m
        for j in range(59):
            saturated[j] += pr['K']['entries'][i][j]*m
        for j in range(13):
            quotient[j] += pr['Q']['entries'][i][j]*m
    check(source == [0]*144 and saturated == [0]*59, 'integer relation images')
    reconstructed = [sum(c*v for c, v in zip(row, quotient)) for row in pr['generator_coordinates']]
    check(reconstructed == integers, 'all integer quotient reconstructions')
    check(list(map(Q, data['relations']['quotient_values'])) == [Q(m, 24) for m in quotient], 'quotient agreement')
    denominator = lcm(*(24//gcd(24, m) for m in integers))
    check(denominator == data['relations']['common_denominator'] == 12, 'common reduced denominator')
    zeros = [i for i, m in enumerate(integers) if m == 0]
    check(len(zeros) == 16 and zeros == data['relations']['zero_generators'], 'all zeros')
    exact_path = dump('signed-isolation-and-relations.json', {'period': list(map(str, (p, q))),
        'generators': generator_rows, 'integer_vector': integers, 'source_images_scaled_24': source,
        'saturated_images_scaled_24': saturated, 'quotient_values_scaled_24': quotient,
        'reconstructed_scaled_24': reconstructed, 'common_denominator': denominator,
        'zero_generators': zeros, 'sign_counts': sign_counts, 'failures': []})

    before = json.loads((OUT/'preservation-before.json').read_text())
    after = {path: sha256((ROOT/path).read_bytes()).hexdigest() for path in before}
    dump('preservation-after.json', after)
    check(before == after, 'all original bytes preserved')
    return {'audit_passed': True, 'failures': [], 'full_replay': str((OUT/'full-replay.json').relative_to(ROOT)),
        'independent_cosine_evidence': phase_path, 'independent_integer_evidence': exact_path,
        'actual': {'phase_containments': len(phases), 'signed_occurrences': occurrences,
            'generator_isolations': len(integers), 'zero_isolations': len(zeros),
            'source_relations': len(source), 'saturated_columns': len(saturated),
            'quotient_values': len(quotient), 'reconstructions': len(reconstructed),
            'common_denominator': denominator, 'max_width': full['actual']['max_width']},
        'required': {'phase_containments': 3744, 'signed_occurrences': 1316,
            'generator_isolations': 72, 'zero_isolations': 16, 'source_relations': 144,
            'saturated_columns': 59, 'quotient_values': 13, 'reconstructions': 72,
            'max_width': str(Q(1, 2**38))}, 'sign_counts': sign_counts,
        'preserved_original_files': len(before), 'originals_preserved': before == after,
        'scope': 'fixed L056 evidence, with imported audited source hypotheses; no generic software theorem'}


if __name__ == '__main__':
    try:
        result = audit()
    except Exception as exc:
        result = {'audit_passed': False, 'failures': [repr(exc)], 'traceback': traceback.format_exc()}
    destination = dump('distinct-report.json', result)
    print('distinct audit:', result['audit_passed'], 'actual:', result.get('actual'),
          'required:', result.get('required'), 'failures:', result['failures'], 'report:', destination, flush=True)
    raise SystemExit(0 if result['audit_passed'] else 1)
