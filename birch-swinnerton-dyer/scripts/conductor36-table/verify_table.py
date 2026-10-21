#!/usr/bin/env python3
"""Exhaustive independent coupled-table replay. Imports no producer.

Fraction endpoints reconstruct finite operations. The existing audited
geometry/tail/period verifier rebuilds all required input lists read-only.
"""
import json
import sys
import traceback
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial, gcd, isqrt, lcm
from pathlib import Path

from verify_exponential_plan import replay as replay_tail_plan

HERE = Path(__file__).resolve().parent


def digest(path):
    h = sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def coefficient_replay(evidence):
    assert evidence['T'] == 4860
    aps = {2: 0, 3: 0}
    primes = [p for p in range(2, 4861) if all(p % d for d in range(2, isqrt(p)+1))]
    counts = evidence['point_counts']
    assert [r['p'] for r in counts] == [p for p in primes if p not in (2, 3)]
    xchecks = 0
    for row in counts:
        p = row['p']
        histogram = [0]*p
        for y in range(p):
            histogram[y*y % p] += 1
        characters = [histogram[(x*x*x+1) % p]-1 for x in range(p)]
        total = p+1+sum(characters)
        aps[p] = p+1-total
        assert row == {'p': p, 'characters': characters, 'total': total, 'a_p': aps[p]}
        xchecks += p
    coefficients = [0, 1]
    factorizations = []
    for n in range(2, 4861):
        m, factors, p = n, [], 2
        while p*p <= m:
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            if e:
                factors.append((p, e))
            p += 1
        if m > 1:
            factors.append((m, 1))
        product, records = 1, []
        for p, e in factors:
            sequence = [1, aps[p]]
            for k in range(2, e+1):
                sequence.append(aps[p]*sequence[-1]-(p if 36 % p else 0)*sequence[-2])
            product *= sequence[e]
            records.append([p, e, sequence])
        coefficients.append(product)
        factorizations.append([n, records])
    assert coefficients == evidence['coefficients'] and factorizations == evidence['factorizations']
    assert all(abs(a) <= n for n, a in enumerate(coefficients[1:], 1))
    return coefficients, {'good_primes': len(counts), 'point_count_x_checks': xchecks,
                          'coefficient_entries': len(coefficients), 'factorizations': len(factorizations)}


def replay(data):
    assert data['schema'] == 'conductor36-coupled-table-v1'
    assert data['bits'] == 96 and data['scale'] == 2**96 and data['H'] == 4860
    D, H = 2**96, 4860
    paths = {'geometry': HERE/'coupled_plan.json', 'tails': HERE/'exponential_plan.json',
             'presentation': HERE/'presentation.json',
             'analytic': HERE.parent/'nonunitary-cusp/reduced_phase_certificate.json',
             'denominator': HERE.parent/'nonunitary-cusp/exact_value_certificate.json'}
    before = {n: digest(p) for n, p in paths.items()}
    assert data['input_sha256'] == before
    originals = {n: json.loads(p.read_text()) for n, p in paths.items()}
    geometry, tails, structure, old = [originals[n] for n in ('geometry', 'tails', 'presentation', 'analytic')]
    upstream = replay_tail_plan(tails)
    assert upstream['replay_passed'] and upstream['workload_passed'] and upstream['failures'] == []
    assert upstream['checks']['uncombined_occurrences'] == 1316
    evidence = data['arithmetic_evidence']
    fields = ('arithmetic', 'pi', 'T', 'point_counts', 'coefficients', 'factorizations', 'period')
    assert set(evidence) == set(fields) and all(evidence[k] == old[k] for k in fields)
    assert evidence['arithmetic']['model'] == [0, 0, 0, 0, 1]
    assert evidence['arithmetic']['N'] == 36
    coefficients, coeff_checks = coefficient_replay(evidence)
    assert data['clearing_integer'] == 24 and data['infinity_primitive'] == '0'
    assert data['real_part_only'] is True and data['critical_audit_complete'] is False
    # Clearing integer is the audited all-cusp theorem L052, not inferred
    # from a numeric table or the old recovered single value.
    assert upstream['period']['positive'] and upstream['period']['component_factor'] == 1
    period = evidence['period']['total']
    assert [str(Q(v, D)) for v in period] == [upstream['period']['lower'], upstream['period']['upper']]

    def endpoints(a):
        assert type(a) is list and len(a) == 2
        assert all(type(v) is int for v in a) and a[0] <= a[1]
        return [Q(v, D) for v in a]

    def enclose(values):
        low, high = min(values)*D, max(values)*D
        return [low.numerator//low.denominator, -((-high.numerator)//high.denominator)]

    def times(a, b):
        return enclose([u*v for u in endpoints(a) for v in endpoints(b)])

    def scalar(a, f):
        return enclose([u*f for u in endpoints(a)])

    def plus(a, b):
        endpoints(a); endpoints(b)
        return [a[0]+b[0], a[1]+b[1]]

    def reduced(x):
        t = x+Q(1, 2)
        return x-t.numerator//t.denominator

    required_keys = sorted({reduced(n*Q(p['x_reduced']))
                            for p in geometry['primitives'] for n in range(1, H+1)})
    assert [Q(r['phase']) for r in data['phases']] == required_keys
    phases = []
    pi = evidence['pi']['interval']
    rem = Q(4**81, factorial(81))
    radius = -((-D*rem).__floor__())
    phase_steps = 0
    for row, x in zip(data['phases'], required_keys):
        assert -Q(1, 2) <= x < Q(1, 2) and row['degree'] == 80
        theta = scalar(pi, 2*x)
        assert row['theta'] == theta and max(map(abs, theta)) <= 4*D
        square = times(theta, theta)
        assert row['square'] == square
        term = total = [D, D]
        assert len(row['trace']) == 40
        for k, saved in enumerate(row['trace'], 1):
            term = scalar(times(term, square), -Q(1, (2*k)*(2*k-1)))
            total = plus(total, term)
            assert saved == {'k': k, 'term': term, 'partial': total}
            phase_steps += 1
        cosine = [total[0]-radius, total[1]+radius]
        assert row['polynomial'] == total and Q(row['remainder']) == rem
        assert row['radius'] == radius and row['cosine'] == cosine
        phases.append(cosine)
    phase_index = {x: i for i, x in enumerate(required_keys)}
    # The upstream replay has checked every attenuation Taylor/remainder,
    # binary tail power and quotient operation on all sixteen heights.
    assert data['attenuation'] == tails['attenuation']
    assert len(data['primitives']) == len(geometry['primitives']) == len(tails['primitives']) == 98
    term_checks = zero_terms = 0
    phase_uses, attenuation_uses, file_uses = set(), set(), set()
    enclosures = []
    for i, (row, g, t) in enumerate(zip(data['primitives'], geometry['primitives'], tails['primitives'])):
        assert row['point_id'] == i and row['H'] == H
        assert row['x_reduced'] == g['x_reduced'] == t['x_reduced']
        assert row['y'] == g['y'] == t['y']
        j = t['attenuation_id']
        assert row['attenuation_id'] == j and 0 <= j < 16
        attenuation_uses.add(j)
        q = data['attenuation'][j]['q']
        assert 0 < q[0] <= q[1] < D and data['attenuation'][j]['y'] == row['y']
        relative = f'table-data/point-{i:03d}.jsonl'
        assert row['term_file'] == relative and relative not in file_uses
        file_uses.add(relative)
        path = HERE/relative
        assert digest(path) == row['term_sha256']
        power, total = [D, D], [0, 0]
        x, records = Q(g['x_reduced']), 0
        with path.open() as stream:
            for n, line in enumerate(stream, 1):
                assert n <= H, (i, n, 'extra term')
                saved = json.loads(line)
                assert type(saved) is list and len(saved) == 6
                key = reduced(n*x)
                phase_id = phase_index[key]
                phase_uses.add(phase_id)
                power = times(power, q)
                product = times(power, phases[phase_id])
                term = scalar(product, Q(coefficients[n], n))
                total = plus(total, term)
                assert saved == [n, phase_id, power, product, term, total], (i, n, 'finite operation mismatch')
                records += 1
                term_checks += 1
                zero_terms += coefficients[n] == 0
        assert records == H, (i, records, H, 'missing terms')
        assert row['last_power'] == power and row['finite_sum'] == total
        tail = Q(t['tail_bounds'][1])
        r = -((-D*tail).__floor__())
        assert Q(row['tail_upper']) == tail and row['tail_radius'] == r
        enclosure = [total[0]-r, total[1]+r]
        assert row['enclosure'] == enclosure
        enclosures.append(enclosure)
        if (i+1) % 14 == 0:
            print('replay:', i+1, '/98 points;', term_checks, '/476280 terms', flush=True)
    assert term_checks == 476280 <= 1000000
    assert phase_uses == set(range(len(phases))) and attenuation_uses == set(range(16))

    assert len(data['generators']) == len(geometry['generators']) == 72
    width_failures, isolation_failures, widths, values = [], [], [], []
    quotient_rows, occurrence_count = [], 0
    for i, (row, g) in enumerate(zip(data['generators'], geometry['generators'])):
        assert row['generator_id'] == i and row['endpoints'] == g['endpoints'] == structure['endpoints'][i]
        assert len(row['occurrence_trace']) == len(g['occurrences'])
        total = [0, 0]
        for saved, (j, w) in zip(row['occurrence_trace'], g['occurrences']):
            term = scalar(enclosures[j], Q(w))
            total = plus(total, term)
            assert saved == {'point_id': j, 'weight': w, 'term': term, 'partial': total}
            occurrence_count += 1
        assert row['integral'] == total
        quotients = [a/b for a in endpoints(total) for b in endpoints(period)]
        assert period[0] > 0
        assert row['quotient_endpoints'] == list(map(str, quotients))
        normalized = enclose(quotients)
        assert row['normalized'] == normalized
        low, high = endpoints(normalized)
        width = high-low
        assert Q(row['width']) == width
        widths.append(width)
        if width > Q(1, 2**38):
            width_failures.append(i)
        scaled_low, scaled_high = 24*low, 24*high
        ceil = -((-scaled_low.numerator)//scaled_low.denominator)
        floor = scaled_high.numerator//scaled_high.denominator
        assert ceil-1 < scaled_low <= ceil and floor <= scaled_high < floor+1
        assert row['scaled_ceil'] == ceil and row['scaled_floor'] == floor
        value = Q(ceil, 24) if ceil == floor else None
        assert row['scaled_integer'] == (ceil if value is not None else None)
        assert row['value'] == (str(value) if value is not None else None)
        if value is None:
            isolation_failures.append(i)
        else:
            assert low <= value <= high
        values.append(value)
        quotient_rows.append({'generator_id': i, 'interval': [str(low), str(high)],
                              'width': str(width), 'ceil': ceil, 'floor': floor,
                              'value': str(value) if value is not None else None})
    assert occurrence_count == 1316
    assert data['width_failures'] == width_failures and data['isolation_failures'] == isolation_failures
    relation_checks = None
    if not isolation_failures:
        pr = structure['presentation']
        A, K, section = structure['A']['entries'], pr['K']['entries'], pr['Q']['entries']
        assert len(A) == 144 and all(len(r) == 72 for r in A)
        assert len(K) == 72 and all(len(r) == 59 for r in K)
        assert len(section) == 72 and all(len(r) == 13 for r in section)
        source = [sum((Q(a)*v for a, v in zip(r, values)), Q(0)) for r in A]
        saturated = [sum((values[i]*K[i][j] for i in range(72)), Q(0)) for j in range(59)]
        quotient = [sum((values[i]*section[i][j] for i in range(72)), Q(0)) for j in range(13)]
        coordinates = pr['generator_coordinates']
        assert len(coordinates) == 72 and all(len(c) == 13 for c in coordinates)
        reconstructed = [sum((quotient[j]*c[j] for j in range(13)), Q(0)) for c in coordinates]
        relation_checks = {'source_images': list(map(str, source)),
                           'saturated_images': list(map(str, saturated)),
                           'quotient_values': list(map(str, quotient)),
                           'reconstructed': list(map(str, reconstructed)),
                           'denominators': [v.denominator for v in values],
                           'common_denominator': lcm(*(v.denominator for v in values)),
                           'zero_generators': [i for i, v in enumerate(values) if not v],
                           'source_failures': [i for i, v in enumerate(source) if v],
                           'saturated_failures': [i for i, v in enumerate(saturated) if v],
                           'reconstruction_failures': [i for i in range(72) if reconstructed[i] != values[i]]}
    assert data['relations'] == relation_checks
    passed = not width_failures and not isolation_failures and relation_checks is not None and all(
        not relation_checks[k] for k in ('source_failures', 'saturated_failures', 'reconstruction_failures'))
    assert data['table_complete'] == passed
    actual = {'points': 98, 'heights': 16, 'terms': term_checks, 'generators': 72,
              'occurrences': occurrence_count, 'phases': len(phases), 'max_width': str(max(widths))}
    required = {'points': 98, 'heights': 16, 'terms': 1000000, 'H': 4860,
                'generators': 72, 'occurrences': 1316, 'max_width': '1/274877906944'}
    assert data['actual'] == actual and data['required'] == required
    assert before == {n: digest(p) for n, p in paths.items()}
    width_power = max(k for k in range(101) if max(widths) <= Q(1, 2**k))
    return {'replay_passed': True, 'table_complete': passed, 'failures': [],
            'width_failures': width_failures, 'isolation_failures': isolation_failures,
            'actual': actual, 'required': required, 'max_width_le_dyadic_power': width_power,
            'worst_generator_id': max(range(72), key=lambda i: widths[i]),
            'coefficient_checks': coeff_checks,
            'checks': {'primitive_records': 98, 'Fourier_terms': term_checks,
                       'zero_coefficient_terms_retained': zero_terms, 'cosine_Taylor_steps': phase_steps,
                       'attenuation_brackets': 16, 'uncombined_signed_occurrences': occurrence_count,
                       'signed_quotient_endpoints': 288, 'integer_isolations': 72-len(isolation_failures),
                       'source_relations': 144 if relation_checks else 0,
                       'saturated_columns': 59 if relation_checks else 0,
                       'quotient_coordinates': 13 if relation_checks else 0,
                       'generator_reconstructions': 72 if relation_checks else 0},
            'generator_results': quotient_rows, 'relations': relation_checks,
            'period': upstream['period'], 'source_checks': upstream,
            'input_preservation_sha256': before, 'critical_audit_complete': False}


if __name__ == '__main__':
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE/'table_certificate.json'
    destination = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE/'table_verification.json'
    try:
        report = replay(json.loads(path.read_text()))
    except Exception as exc:
        report = {'replay_passed': False, 'table_complete': False,
                  'failures': [repr(exc)], 'traceback': traceback.format_exc()}
    report['certificate_sha256'] = digest(path)
    destination.write_text(json.dumps(report, indent=2)+'\n')
    print('replay:', report['replay_passed'], 'table:', report['table_complete'],
          'actual:', report.get('actual'), 'required:', report.get('required'),
          'failures:', report['failures'], 'width failures:', report.get('width_failures'),
          'isolation failures:', report.get('isolation_failures'), 'report:', destination, flush=True)
    raise SystemExit(0 if report['replay_passed'] and report['table_complete'] else 1)
