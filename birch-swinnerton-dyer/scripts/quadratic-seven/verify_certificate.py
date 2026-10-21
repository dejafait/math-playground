#!/usr/bin/env python3
"""Distinct full replay. No builder import; exhaustive cosets and integer sum."""
import hashlib
import json
from fractions import Fraction as Q
from math import gcd
from pathlib import Path

ROOT = Path('scripts/quadratic-seven')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rational(s):
    assert type(s) is str
    q = Q(s)
    assert str(q) == s
    return q


def integer_row(row, size):
    assert type(row) is list and len(row) == size and all(type(k) is int for k in row)
    return row


def dot(a, b):
    assert len(a) == len(b)
    return sum(x*y for x, y in zip(a, b))


def order(q):
    q = Q(q)
    if not q:
        return 'infinity'
    n, d, v = q.numerator, q.denominator, 0
    while n % 7 == 0:
        n //= 7
        v += 1
    while d % 7 == 0:
        d //= 7
        v -= 1
    return v


def cusp(pair):
    a, b = integer_row(pair, 2)
    assert a or b
    if b == 0:
        return [1, 0]
    q = Q(a, b)
    return [q.numerator, q.denominator]


def main():
    report = {'checks': {}, 'failures': [], 'attempts': [],
              'external_theorems_verified_by_script': False}
    def check(name, condition):
        report['checks'][name] = bool(condition)
        assert condition, name
    try:
        path = ROOT/'certificate.json'
        report['certificate_sha256'] = sha(path)
        cert = json.loads(path.read_text())
        inputs = [f'scripts/{topic}/{name}.json'
                  for topic in ('relative-t2', 'twist-five', 'calibrated-symbols')
                  for name in ('certificate', 'verification', 'audit')]
        assert set(cert['input_sha256']) == set(inputs)
        assert all(sha(p) == cert['input_sha256'][p] for p in inputs)
        data = [json.loads(Path(p).read_text()) for p in inputs]
        base, base_replay, base_audit, twist, twist_replay, twist_audit, symbols, replay, audit = data
        assert symbols['input_sha256'] == {p: sha(p) for p in inputs[:6]}
        for c, r, a, topic in [(base, base_replay, base_audit, 'relative-t2'),
                              (symbols, replay, audit, 'calibrated-symbols')]:
            assert not c['failures']
            for x in (r, a):
                assert x['certificate_sha256'] == sha(f'scripts/{topic}/certificate.json')
                assert not x['failures'] and x['checks'] and all(v is True for v in x['checks'].values())
        assert twist_replay['certificate_sha256'] == twist_audit['certificate_sha256'] == sha(inputs[3])
        assert twist_audit['base_certificate_sha256'] == sha(inputs[0])
        assert twist_replay['finite_arithmetic_verified'] is True
        assert not twist_audit['failures'] and rational(twist_audit['q']) == 4
        assert twist_replay['reports'] and all(r['isolated'] and rational(r['q']) == 4
                                               and not r['failures'] for r in twist_replay['reports'])
        isolation = twist['attempts'][twist['selected_attempt']]['isolation']
        assert isolation['isolated'] and isolation['candidates'] == ['4']
        check('all_nine_hashes_and_audited_input_reports', True)
        assert cert['instance'] == {'model': [0, 1, 1, -2, 0], 'p': 7, 'level': 389,
                                   'C': 0, 'gamma': 8, 'branch': 'primitive untwisted trivial',
                                   'period': 'total minimal real'}
        assert base['arithmetic']['model'] == [0, 1, 1, -2, 0]
        assert base['arithmetic']['discriminant'] == base['arithmetic']['conductor'] == 389
        check('exact_model_and_normalization_input', True)
        ordinary = cert['ordinary']
        points = [[x, y] for x in range(7) for y in range(7)
                  if (y*y+y-x**3-x*x+2*x) % 7 == 0]
        assert len(ordinary['rows']) == 7
        for x, row in enumerate(ordinary['rows']):
            ys = [y for a, y in points if a == x]
            rhs, disc = (x**3+x*x-2*x) % 7, (1+4*(x**3+x*x-2*x)) % 7
            assert row == {'x': x, 'rhs': rhs, 'disc': disc, 'legendre': len(ys)-1,
                           'ys': ys, 'count': len(ys)}
        t = 8-(1+len(points))
        assert ordinary['point_count'] == 1+len(points) == 13 and ordinary['t'] == t == -5
        assert ordinary['point_at_infinity'] == [0, 1, 0]
        assert ordinary['discriminant_mod_p'] == 389 % 7 == 4
        assert ordinary['good'] is True and gcd(389, 7) == 1
        assert ordinary['ordinary'] is True and t % 7 != 0
        report['ordinary_replay'] = {'affine_points': points, 'point_count': 13, 't': t,
                                     'good': True, 'ordinary': True}
        check('exhaustive_49_pair_count_and_good_ordinarity', True)

        coords = base['presentation']['integral_generator_coordinates']
        assert len(coords) == 390 and base['presentation']['dimension'] == 65
        for row in coords:
            integer_row(row, 65)
        lifts = [[0, -1, 1, i] for i in range(389)]+[[1, 0, 0, 1]]
        assert base['SL2_lifts'] == lifts
        phi = [rational(x) for x in base['integration_line']['basis_functional']]
        f = [rational(x) for x in symbols['basis_functional']]
        y = [rational(x) for x in symbols['integral_generator_values']]
        assert len(phi) == len(f) == 65 and len(y) == 390
        assert f == [-x for x in phi] and rational(symbols['scale']) == -1
        assert all(dot(row, f) == v for row, v in zip(coords, y))
        assert symbols['denominator']['lcm'] == 2 and all((2*v).denominator == 1 for v in y)
        doubled = [int(2*v) for v in y]
        assert len(base['relations']) == 780
        assert len(base['presentation']['saturated_relation_basis']) == 325
        for row in base['relations']+base['presentation']['saturated_relation_basis']:
            assert dot(integer_row(row, 390), doubled) == 0
        check('all_calibrated_values_full_coordinates_and_relations', True)

        # Reconstruct every raw vector from geometric endpoints. Locate the coset
        # by checking every lift, without the builder's modular inverse formula.
        computed, segments = {}, 0
        for key, saved in cert['paths'].items():
            r = rational(key)
            assert saved['argument'] == [r.numerator, r.denominator]
            cf = saved['continued_fraction']
            assert type(cf) is list and cf and all(type(k) is int for k in cf)
            v = Q(cf[-1])
            for k in cf[-2::-1]:
                assert v
                v = k+1/v
            assert v == r and len(cf) == len(saved['segments'])
            previous, raw = [1, 0], [0]*390
            for seg in saved['segments']:
                A, B, C, D = integer_row(seg['lift'], 4)
                assert A*D-B*C == 1
                assert seg['start'] == previous == cusp([B, D])
                assert seg['end'] == cusp([A, C])
                hits = []
                for i, (e, f0, g, k) in enumerate(lifts):
                    gamma = [A*k-B*g, -A*f0+B*e, C*k-D*g, -C*f0+D*e]
                    if gamma[2] % 389 == 0:
                        G, H, I, J = gamma
                        assert G*J-H*I == 1
                        assert [G*e+H*g, G*f0+H*k, I*e+J*g, I*f0+J*k] == [A, B, C, D]
                        hits.append((i, gamma))
                assert len(hits) == 1
                i, gamma = hits[0]
                assert type(seg['coset']) is int and seg['coset'] == i
                assert seg['Gamma0_reduction'] == gamma
                raw[i] += 1
                previous = seg['end']
                segments += 1
            assert previous == saved['argument']
            assert integer_row(saved['raw'], 390) == raw
            quotient = [sum(raw[i]*coords[i][j] for i in range(390)) for j in range(65)]
            assert integer_row(saved['coordinates'], 65) == quotient
            value2 = dot(raw, doubled)
            assert Q(value2, 2) == dot(quotient, f) == rational(saved['value'])
            computed[key] = value2
        check('every_oriented_path_segment_exhaustive_coset_and_full_quotient', True)

        used_paths, found = set(), False
        assert 1 <= len(cert['attempts']) <= 3
        for index, a in enumerate(cert['attempts']):
            assert not found
            n, M = 2+index, 3+index
            assert a['n'] == n and a['M'] == M and a['N'] == min(n-1, M)
            assert len(a['teichmuller']) == 6
            roots = {}
            for d, row in enumerate(a['teichmuller'], 1):
                candidates = [w for w in range(1, 7**n) if w % 7 == d and pow(w, 6, 7**n) == 1]
                assert len(candidates) == 1
                w = candidates[0]
                residual, deriv = w**6-1, 6*w**5 % 7
                assert row == {'d': d, 'w': w, 'sixth_residual': residual,
                               'residual_valuation': order(residual), 'derivative_mod_p': deriv}
                assert deriv != 0 and (order(residual) == 'infinity' or order(residual) >= n)
                roots[d] = w
            u = rational(a['unit_root']['u'])
            assert u.denominator == 1 and order(u) == 0 and u.numerator % 7 == t % 7
            candidates = [x for x in range(7**M) if x % 7 == t % 7
                          and (x*x-t*x+7) % (7**M) == 0]
            assert candidates == [int(u)]
            residual, deriv = int(u*u-t*u+7), int(2*u-t) % 7
            assert a['unit_root'] == {'u': str(u), 'residual': residual,
                                      'residual_valuation': order(residual),
                                      'derivative_mod_p': deriv, 'valuation': order(u)}
            assert deriv != 0 and (order(residual) == 'infinity' or order(residual) >= M)
            check(f'n{n}_complete_residues_and_correct_simple_unit_root', True)

            assert len(a['terms']) == a['actual_terms'] == a['required_terms'] == 6*7**(n-1)
            sum_A2, sum_B2, term_sum = 0, 0, Q(0)
            seen_residues = []
            for term_index, term in enumerate(a['terms']):
                d = 1+term_index//7**(n-1)
                j = term_index % 7**(n-1)
                # Repeated multiplication is independent of saved powers/r.
                r = roots[d]
                for _ in range(j):
                    r = (8*r) % (7**n)
                A_key, B_key = str(Q(r, 7**n)), str(Q(r, 7**(n-1)))
                weight = j*(j-1)//2
                assert term['d'] == d and term['j'] == j and term['r'] == r
                assert term['binomial'] == weight and term['A_path'] == A_key and term['B_path'] == B_key
                A2, B2 = computed[A_key], computed[B_key]
                A, B = Q(A2, 2), Q(B2, 2)
                assert rational(term['A']) == A and rational(term['B']) == B
                value = weight*(A/u**n-B/u**(n+1))
                assert rational(term['term']) == value
                term_sum += value
                sum_A2 += weight*A2
                sum_B2 += weight*B2
                seen_residues.append(r)
                used_paths.update((A_key, B_key))
            assert sorted(seen_residues) == [x for x in range(1, 7**n) if x % 7 != 0]
            # Integer numerator accumulation avoids the builder's summation path.
            b = Q(int(u)*sum_A2-sum_B2, 2*int(u)**(n+1))
            v = order(b)
            strict = v != 'infinity' and a['N'] > v
            assert term_sum == b == rational(a['b'])
            assert rational(a['sum_A']) == Q(sum_A2, 2) and rational(a['sum_B']) == Q(sum_B2, 2)
            assert a['valuation_b'] == v and a['strict_bound'] is strict
            report['attempts'].append({'n': n, 'M': M, 'N': a['N'], 'u': str(u),
                                        'residual': residual, 'valuation_residual': order(residual),
                                        'sum_A2': sum_A2, 'sum_B2': sum_B2, 'b': str(b),
                                        'valuation_b': v, 'strict_bound': strict,
                                        'actual_terms': len(a['terms']), 'required_terms': 6*7**(n-1)})
            check(f'n{n}_all_terms_integer_sum_and_strict_comparison', True)
            found = strict
        assert used_paths == set(cert['paths'])
        assert found or len(cert['attempts']) == 3
        assert not cert['failures'] and cert['result'] == {'strict_bound': found,
                'selected_n': cert['attempts'][-1]['n'], 'paths': len(computed), 'failures': []}
        check('bounded_schedule_first_strict_stop_and_no_unused_paths', True)
        report['results'] = {'paths': len(computed), 'segments': segments,
                             'strict_bound': found, 'selected_n': cert['attempts'][-1]['n']}
    except Exception as error:
        report['failures'].append(f'{type(error).__name__}: {error}')
    out = ROOT/'verification.json'
    out.write_text(json.dumps(report, indent=2)+'\n')
    print('checks', len(report['checks']), 'results', report.get('results'),
          'attempts', report['attempts'], 'failures', report['failures'], 'report', out)
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
