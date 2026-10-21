#!/usr/bin/env python3
"""Independent exact replay of all new paths, values and denominator evidence.

Imports no construction program. L030/L031's audited theorems remain inputs;
hash binding does not purport to prove their source theorems anew.
"""
import hashlib
import json
from fractions import Fraction
from math import gcd, lcm
from pathlib import Path

SOURCE = Path('scripts/calibrated-symbols/certificate.json')
OUT = Path('scripts/calibrated-symbols/verification.json')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rational(value):
    assert isinstance(value, str)
    result = Fraction(value)
    assert str(result) == value
    return result


def integers(row, count):
    assert isinstance(row, list) and len(row) == count
    assert all(type(entry) is int for entry in row)
    return row


def dot(a, b):
    assert len(a) == len(b)
    return sum(x*y for x, y in zip(a, b))


def normalize(pair):
    p, q = integers(pair, 2)
    if q == 0:
        assert p
        return [1, 0]
    divisor = gcd(p, q)
    return [p//divisor, q//divisor] if q > 0 else [-p//divisor, -q//divisor]


def product(left, right):
    a, b, c, d = left
    e, f, g, h = right
    return [a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h]


def verify():
    raw_certificate = SOURCE.read_bytes()
    cert = json.loads(raw_certificate)
    checks, failures = {}, []

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            failures.append(name)
            raise AssertionError(name)

    try:
        expected = [f'scripts/{topic}/{name}.json'
                    for topic in ('relative-t2', 'twist-five')
                    for name in ('certificate', 'verification', 'audit')]
        assert set(cert['input_sha256']) == set(expected)
        inputs = {}
        for path in expected:
            assert sha(path) == cert['input_sha256'][path]
            inputs[path] = json.loads(Path(path).read_text())
        base, replay, audit, twist, t_replay, t_audit = [inputs[p] for p in expected]
        for report in (replay, audit):
            assert report['certificate_sha256'] == sha(expected[0])
            assert not report['failures'] and report['checks']
            assert all(flag is True for flag in report['checks'].values())
        assert t_replay['certificate_sha256'] == t_audit['certificate_sha256'] == sha(expected[3])
        assert t_audit['base_certificate_sha256'] == sha(expected[0])
        assert t_replay['finite_arithmetic_verified'] is True
        assert t_replay['reports'] and not t_audit['failures']
        assert rational(t_audit['q']) == 4
        assert all(r['isolated'] and rational(r['q']) == 4 and not r['failures']
                   for r in t_replay['reports'])
        isolation = twist['attempts'][twist['selected_attempt']]['isolation']
        assert isolation['isolated'] and isolation['candidates'] == ['4']
        check('all_six_input_hashes_and_audited_premises', True)

        n, s, dimension = 389, 390, 65
        check('exact_instance_and_counts', cert['instance'] == {
            'model': [0, 1, 1, -2, 0], 'level': n, 'twist': 5, 'q': '4',
            'generator_count': s, 'relative_dimension': dimension}
            and base['arithmetic']['model'] == [0, 1, 1, -2, 0]
            and base['arithmetic']['discriminant'] == n
            and base['arithmetic']['conductor'] == n
            and not base['failures'] and not cert['failures'])
        presentation = base['presentation']
        coordinates = presentation['integral_generator_coordinates']
        assert len(coordinates) == s
        for row in coordinates:
            integers(row, dimension)
        assert presentation['dimension'] == dimension and presentation['rank'] == 325
        lifts = [[0, -1, 1, i] for i in range(n)]+[[1, 0, 0, 1]]
        assert lifts == base['SL2_lifts']
        assert base['projective_cosets'] == [[1, i] for i in range(n)]+[[0, 1]]
        phi = [rational(v) for v in base['integration_line']['basis_functional']]
        assert len(phi) == dimension and any(phi)
        x = [dot(row, phi) for row in coordinates]
        assert x == [rational(v) for v in base['integration_line']['integral_generator_values']]
        assert len(base['dual']['B']) == 130
        assert all(dot(integers(row, dimension), phi) == 0 for row in base['dual']['B'])
        check('full_integral_coordinates_and_original_functional', True)

        assert len(cert['paths']) == 4
        segment_count = 0
        for a, path in enumerate(cert['paths'], 1):
            assert path['a'] == a and path['start'] == [1, 0] and path['end'] == [a, 5]
            assert path['chi'] == (1 if pow(a, 2, 5) == 1 else -1)
            cf = path['continued_fraction']
            assert cf and len(cf) == len(path['segments'])
            assert all(type(k) is int for k in cf)
            value = Fraction(cf[-1])
            for k in reversed(cf[:-1]):
                assert value
                value = k+1/value
            assert value == Fraction(a, 5)
            previous, vector = [1, 0], [0]*s
            for segment in path['segments']:
                h = integers(segment['lift'], 4)
                aa, bb, cc, dd = h
                assert aa*dd-bb*cc == 1
                assert segment['start'] == previous == normalize([bb, dd])
                assert segment['end'] == normalize([aa, cc])
                assert normalize(segment['start']) == segment['start']
                assert normalize(segment['end']) == segment['end']
                index = segment['coset']
                assert type(index) is int and 0 <= index < s
                bottom = ((dd % n)*pow(cc % n, -1, n)) % n if cc % n else n
                assert index == bottom
                la, lb, lc, ld = lifts[index]
                gamma = product(h, [ld, -lb, -lc, la])
                assert integers(segment['Gamma0_reduction'], 4) == gamma
                assert gamma[0]*gamma[3]-gamma[1]*gamma[2] == 1 and gamma[2] % n == 0
                assert product(gamma, lifts[index]) == h
                vector[index] += 1
                previous = segment['end']
                segment_count += 1
            assert previous == [a, 5]
            assert integers(path['raw'], s) == vector
            quotient = [sum(vector[i]*coordinates[i][j] for i in range(s))
                        for j in range(dimension)]
            assert integers(path['coordinates'], dimension) == quotient
            assert rational(path['phi_value']) == dot(quotient, phi) == dot(vector, x)
        check('all_four_oriented_paths_and_every_coset_segment', True)

        raw = [sum(path['chi']*path['raw'][i] for path in cert['paths']) for i in range(s)]
        quotient = [sum(path['chi']*path['coordinates'][j] for path in cert['paths'])
                    for j in range(dimension)]
        assert integers(cert['G5']['raw'], s) == raw
        assert integers(cert['G5']['coordinates'], dimension) == quotient
        assert quotient == [sum(raw[i]*coordinates[i][j] for i in range(s))
                            for j in range(dimension)]
        d = dot(raw, x)
        assert d == dot(quotient, phi) == rational(cert['G5']['phi_value'])
        assert d == sum(path['chi']*rational(path['phi_value']) for path in cert['paths'])
        check('exact_nonzero_character_sum', d != 0)
        scale = rational(cert['scale'])
        assert scale == Fraction(4)/d
        y = [rational(v) for v in cert['integral_generator_values']]
        assert len(y) == s and y == [scale*v for v in x]
        new_phi = [rational(v) for v in cert['basis_functional']]
        assert len(new_phi) == dimension and new_phi == [scale*v for v in phi]
        assert y == [dot(row, new_phi) for row in coordinates]
        check('exact_scale_and_all_390_calibrated_values', dot(raw, y) == dot(quotient, new_phi) == 4)

        def coset(c, d):
            return (d*pow(c % n, -1, n)) % n if c % n else n
        relations = []
        for i, (c, dd) in enumerate([[1, i] for i in range(n)]+[[0, 1]]):
            two, three = [0]*s, [0]*s
            for k in [i, coset(dd, -c)]:
                two[k] += 1
            for k in [i, coset(dd, -c-dd), coset(-c-dd, c)]:
                three[k] += 1
            relations.extend([two, three])
        assert relations == base['relations']
        saturated = presentation['saturated_relation_basis']
        assert len(saturated) == 325
        for row in saturated:
            integers(row, s)
        assert set(cert['relation_residuals']) == {'Manin', 'saturated'}
        for label, rows in [('Manin', relations), ('saturated', saturated)]:
            residuals = cert['relation_residuals'][label]
            assert len(residuals) == len(rows)
            assert [dot(row, y) for row in rows] == [rational(z) for z in residuals] == [0]*len(rows)
            assert all(dot(row, x) == 0 for row in rows)
        check('every_780_Manin_and_325_saturated_relation', True)

        den = cert['denominator']
        common = den['lcm']
        assert type(common) is int and common >= 1
        assert common == lcm(*(v.denominator for v in y))
        factors = []
        remaining, candidate = common, 2
        while candidate*candidate <= remaining:
            power = 0
            while remaining % candidate == 0:
                remaining //= candidate
                power += 1
            if power:
                factors.append([candidate, power])
            candidate += 1
        if remaining > 1:
            factors.append([remaining, 1])
        assert den['prime_factorization'] == factors
        witnesses = den['max_valuation_generator_witnesses']
        assert len(witnesses) == len(factors)
        for (prime, exponent), witness in zip(factors, witnesses):
            integers(witness, 3)
            assert witness[:2] == [prime, exponent]
            index = witness[2]
            assert 0 <= index < s
            denominator = y[index].denominator
            assert denominator % (prime**exponent) == 0
            assert denominator % (prime**(exponent+1)) != 0
        assert den['all_scaled_values_integral'] is True
        assert all((common*v).denominator == 1 for v in y)
        check('exact_lcm_factorization_and_valuation_witnesses', True)
        results = {'path_count': 4, 'segments': segment_count, 'd': str(d),
                   'scale': str(scale), 'generator_count': len(y), 'required_generator_count': s,
                   'Manin_relations': len(relations), 'saturated_relations': len(saturated),
                   'common_denominator': common, 'prime_factorization': factors,
                   'C_for_good_ordinary_p_ge_5_p_ne_5':
                   0 if all(prime < 5 or prime == 5 for prime, _ in factors)
                   else 'read v_p(common_denominator) for each permitted p'}
    except Exception as error:
        if not failures:
            failures.append(f'{type(error).__name__}: {error}')
        results = {}
    report = {'certificate_sha256': hashlib.sha256(raw_certificate).hexdigest(),
              'checks': checks, 'failures': failures, 'results': results,
              'external_theorems_verified_by_script': False}
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print('checks', len(checks), 'failures', failures, 'results', results, 'report', OUT)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    verify()
