#!/usr/bin/env python3
"""Distinct full replay. No builder import; exhaustive cosets and integer sum."""
import hashlib
import contextlib
import importlib.util
import io
import json
from fractions import Fraction as Q
from math import gcd, lcm
from pathlib import Path

ROOT = Path('scripts/conductor-eleven/quadratic-five')
BASE = Path('scripts/conductor-eleven')
CAL = BASE/'five-isogeny'
ABS = BASE/'absolute-cycles'


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
    while n % 5 == 0:
        n //= 5
        v += 1
    while d % 5 == 0:
        d //= 5
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
        def load(p):
            return json.loads(Path(p).read_text())
        symbols = load(CAL/'certificate.json')
        expected = {}
        for directory in (ABS, CAL):
            manifest = directory/'critical-audit/pre-replay-manifest.json'
            audit_path = directory/'critical-audit/audit.json'
            assert not load(audit_path)['failures']
            for p, h in load(manifest).items():
                if p in expected:
                    assert expected[p] == h
                expected[p] = h
            for p in (manifest, audit_path):
                expected[str(p)] = sha(p)
        for p in (BASE/'arithmetic-certificate.json',
                  Path('lemmas/L027-conditional-quadratic-coefficient-enclosure.md'),
                  Path('lemmas/L039-conductor-eleven-general-adapter-integration-line.md'),
                  Path('lemmas/L043-conductor-eleven-absolute-cycle-normalization.md'),
                  Path('lemmas/L045-prime-degree-nonoptimal-symbol-transfer.md'),
                  Path('lemmas/L046-conductor-eleven-five-isogeny-normalization.md')):
            expected[str(p)] = sha(p)
        assert cert['input_sha256'] == expected
        assert all(sha(p) == h for p, h in expected.items())
        check('all_prior_inputs_programs_audits_and_complete_binding', True)

        # Full upstream verifiers run into NEW paths; originals remain read-only.
        # Import only verification programs, never either construction program.
        upstream = ROOT/'upstream-replay'
        upstream.mkdir(parents=True, exist_ok=True)
        def verifier(p, name):
            spec = importlib.util.spec_from_file_location(name, p)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        log = io.StringIO()
        try:
            with contextlib.redirect_stdout(log):
                dual_checker = verifier('scripts/dual-kernel/verify_certificate.py', 'eleven_dual_replay')
                dr = dual_checker.verify(BASE/'dual-certificate.json', BASE/'structural-certificate.json',
                                         BASE/'arithmetic-input.json', upstream/'dual-verification.json')
                assert not dr['failures'] and dr['summary']['rank'] == 2 and dr['summary']['nullity'] == 1
                structural_report = load(upstream/'dual-verification-structure/general-verification.json')
                assert not structural_report['failures']
                assert all(structural_report['actual'][name] == count
                           for name, count in structural_report['required'].items()), 'structural domain count'
                assert structural_report['actual']['segments'] == 218, 'all upstream segment occurrences'
                absolute_checker = verifier(ABS/'verify_certificate.py', 'eleven_absolute_replay')
                absolute_checker.HERE = upstream/'absolute'
                absolute_checker.HERE.mkdir(parents=True, exist_ok=True)
                ac = load(ABS/'certificate.json')
                checks = []
                summary = absolute_checker.replay(ac, checks)
                ar = {'certificate_sha256': sha(ABS/'certificate.json'), 'summary': summary,
                      'checks': checks, 'failures': []}
                (upstream/'absolute-verification.json').write_text(json.dumps(ar, indent=2)+'\n')
                assert summary == load(ABS/'verification.json')['summary']
                isogeny_checker = verifier(CAL/'verify_certificate.py', 'eleven_isogeny_replay')
                checks, failures, evidence = isogeny_checker.verify(symbols)
                ir = {'certificate_sha256': sha(CAL/'certificate.json'),
                      'checks': checks, 'failures': failures, 'evidence': evidence}
                (upstream/'isogeny-verification.json').write_text(json.dumps(ir, indent=2)+'\n')
                assert not failures and len(checks) == 56
                assert evidence == load(CAL/'verification.json')['evidence']
        finally:
            (upstream/'replay.txt').write_text(log.getvalue())
        report['upstream_replay'] = {
            'dual': str(upstream/'dual-verification.json'),
            'structural': str(upstream/'dual-verification-structure/general-verification.json'),
            'absolute': str(upstream/'absolute-verification.json'),
            'isogeny': str(upstream/'isogeny-verification.json')}
        check('complete_fresh_structural_dual_absolute_and_isogeny_replays', True)
        base, dual = load(BASE/'structural-certificate.json'), load(BASE/'dual-certificate.json')
        assert cert['instance'] == {'model': [0, -1, 1, -7820, -263580], 'p': 5, 'level': 11,
                                   'C': 0, 'gamma': 6, 'branch': 'primitive untwisted trivial',
                                   'period': 'total minimal real'}
        assert dual['arithmetic']['model'] == [0, -1, 1, -10, -20]
        assert dual['arithmetic']['conductor'] == 11
        assert load(BASE/'arithmetic-certificate.json')['invariants']['Delta'] == -11**5
        assert base['inputs'] == {'N': 11, 'P': [2]}
        assert symbols['target'] == cert['instance']['model']
        assert symbols['invariants']['delta'] == -11
        assert cert['non_CM'] == {'source_result': 'L039', 'isogeny_result': 'L046',
                                  'theorem': 'Sutherland 2015 Lecture 13 Theorem 13.18',
                                  'base_field': 'algebraic closure of Q', 'conclusion': 'geometric non-CM'}
        check('exact_model_and_normalization_input', True)
        ordinary = cert['ordinary']
        points = [[x, y] for x in range(5) for y in range(5)
                  if (y*y+y-x**3+x*x+7820*x+263580) % 5 == 0]
        assert len(ordinary['rows']) == 5
        for x, row in enumerate(ordinary['rows']):
            ys = [y for a, y in points if a == x]
            rhs, disc = (x**3-x*x-7820*x-263580) % 5, (1+4*(x**3-x*x-7820*x-263580)) % 5
            assert row == {'x': x, 'rhs': rhs, 'disc': disc, 'legendre': len(ys)-1,
                           'ys': ys, 'count': len(ys)}
        t = 6-(1+len(points))
        assert ordinary['point_count'] == 1+len(points) == 5 and ordinary['t'] == t == 1
        assert ordinary['point_at_infinity'] == [0, 1, 0]
        assert ordinary['discriminant_mod_p'] == (-11) % 5 == 4
        assert ordinary['good'] is True and gcd(-11, 5) == 1
        assert ordinary['ordinary'] is True and t % 5 != 0
        report['ordinary_replay'] = {'affine_points': points, 'point_count': 5, 't': t,
                                     'good': True, 'ordinary': True}
        check('exhaustive_25_pair_count_and_good_ordinarity', True)

        coords = base['presentation']['generator_coordinates']
        assert len(coords) == 12 and base['presentation']['d'] == 3
        for row in coords:
            integer_row(row, 3)
        lifts = base['cosets']['lifts']
        assert len(lifts) == 12
        reps = [[0, 1]]+[[1, i] for i in range(11)]
        assert base['cosets']['representatives'] == reps
        for h, rep in zip(lifts, reps):
            A, B, C, D = integer_row(h, 4)
            assert A*D-B*C == 1
            assert any([u*C % 11, u*D % 11] == rep for u in range(1, 11))
        phi = [rational(x) for x in dual['line']['v']]
        f = [rational(x) for x in dual['line']['v']]
        y = [rational(x) for x in symbols['transfer']['target_values']]
        assert len(phi) == len(f) == 3 and len(y) == 12
        assert phi == [Q(5, 2), Q(5), Q(1)]
        assert f == phi
        assert all(dot(row, f) == v for row, v in zip(coords, y))
        assert lcm(*(v.denominator for v in y)) == symbols['transfer']['common_denominator'] == 2
        assert all((2*v).denominator == 1 and (order(v) == 'infinity' or order(v) >= 0) for v in y)
        scaled = [int(2*v) for v in y]
        relations = base['A']['entries']
        saturated = list(map(list, zip(*base['presentation']['K']['entries'])))
        assert len(relations) == 24 and len(saturated) == 9
        for row in relations+saturated:
            assert dot(integer_row(row, 12), scaled) == 0
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
            previous, raw = [1, 0], [0]*12
            for seg in saved['segments']:
                A, B, C, D = integer_row(seg['lift'], 4)
                assert A*D-B*C == 1
                assert seg['start'] == previous == cusp([B, D])
                assert seg['end'] == cusp([A, C])
                hits = []
                for i, (e, f0, g, k) in enumerate(lifts):
                    gamma = [A*k-B*g, -A*f0+B*e, C*k-D*g, -C*f0+D*e]
                    if gamma[2] % 11 == 0:
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
            assert integer_row(saved['raw'], 12) == raw
            quotient = [sum(raw[i]*coords[i][j] for i in range(12)) for j in range(3)]
            assert integer_row(saved['coordinates'], 3) == quotient
            value2 = dot(raw, scaled)
            assert Q(value2, 2) == dot(quotient, f) == rational(saved['value'])
            computed[key] = value2
        check('every_oriented_path_segment_exhaustive_coset_and_full_quotient', True)

        used_paths, found = set(), False
        assert 1 <= len(cert['attempts']) <= 3
        for index, a in enumerate(cert['attempts']):
            assert not found
            n, M = 2+index, 3+index
            assert a['n'] == n and a['M'] == M and a['N'] == min(n-1, M)
            assert len(a['teichmuller']) == 4
            roots = {}
            for d, row in enumerate(a['teichmuller'], 1):
                candidates = [w for w in range(1, 5**n) if w % 5 == d and pow(w, 4, 5**n) == 1]
                assert len(candidates) == 1
                w = candidates[0]
                residual, deriv = w**4-1, 4*w**3 % 5
                assert row == {'d': d, 'w': w, 'fourth_residual': residual,
                               'residual_valuation': order(residual), 'derivative_mod_p': deriv}
                assert deriv != 0 and (order(residual) == 'infinity' or order(residual) >= n)
                roots[d] = w
            u = rational(a['unit_root']['u'])
            assert u.denominator == 1 and order(u) == 0 and u.numerator % 5 == t % 5
            candidates = [x for x in range(5**M) if x % 5 == t % 5
                          and (x*x-t*x+5) % (5**M) == 0]
            assert candidates == [int(u)]
            residual, deriv = int(u*u-t*u+5), int(2*u-t) % 5
            assert a['unit_root'] == {'u': str(u), 'residual': residual,
                                      'residual_valuation': order(residual),
                                      'derivative_mod_p': deriv, 'valuation': order(u)}
            assert deriv != 0 and (order(residual) == 'infinity' or order(residual) >= M)
            check(f'n{n}_complete_residues_and_correct_simple_unit_root', True)

            assert len(a['terms']) == a['actual_terms'] == a['required_terms'] == 4*5**(n-1)
            sum_A2, sum_B2, term_sum = 0, 0, Q(0)
            seen_residues = []
            for term_index, term in enumerate(a['terms']):
                d = 1+term_index//5**(n-1)
                j = term_index % 5**(n-1)
                # Repeated multiplication is independent of saved powers/r.
                r = roots[d]
                for _ in range(j):
                    r = (6*r) % (5**n)
                A_key, B_key = str(Q(r, 5**n)), str(Q(r, 5**(n-1)))
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
            assert sorted(seen_residues) == [x for x in range(1, 5**n) if x % 5 != 0]
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
                                        'actual_terms': len(a['terms']), 'required_terms': 4*5**(n-1)})
            check(f'n{n}_all_terms_integer_sum_and_strict_comparison', True)
            found = strict
        assert used_paths == set(cert['paths'])
        assert found or len(cert['attempts']) == 3
        assert not cert['failures'] and cert['result'] == {'strict_bound': found,
                'selected_n': cert['attempts'][-1]['n'], 'paths': len(computed), 'failures': []}
        check('bounded_schedule_first_strict_stop_and_no_unused_paths', True)
        assert all(sha(p) == h for p, h in expected.items())
        check('all_prior_input_bytes_unchanged_after_replay', True)
        report['results'] = {'paths': len(computed), 'required_paths': len(used_paths),
                             'segments': segments,
                             'required_segment_occurrences': sum(len(p['segments']) for p in cert['paths'].values()),
                             'strict_bound': found, 'selected_n': cert['attempts'][-1]['n']}
    except Exception as error:
        report['failures'].append(f'{type(error).__name__}: {error}')
    if report['failures']:
        report['results'] = {}
    out = ROOT/'verification.json'
    out.write_text(json.dumps(report, indent=2)+'\n')
    print('checks', len(report['checks']), 'results', report.get('results'),
          'attempts', report['attempts'], 'failures', report['failures'], 'report', out)
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
