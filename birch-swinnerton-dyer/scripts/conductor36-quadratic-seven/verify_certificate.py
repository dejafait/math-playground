#!/usr/bin/env python3
"""Distinct full replay. No builder import; exhaustive cosets and integer sum."""
import hashlib
import subprocess
import sys
import traceback
import json
from fractions import Fraction as Q
from math import gcd, lcm
from pathlib import Path

ROOT = Path('scripts/conductor36-quadratic-seven')
BASE = Path('scripts/conductor36-table')


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
    report = {'checks': {}, 'attempts': [], 'failures': [], 'path_replay': {}}
    def check(name, condition):
        assert condition, name
        report['checks'][name] = True
    try:
        cert = json.loads((ROOT/'certificate.json').read_text())
        expected = cert['input_sha256']
        required = {BASE/'table_certificate.json', BASE/'presentation.json'}
        required.update(BASE/('table-data/point-%03d.jsonl' % i) for i in range(98))
        required.update(Path(p) for p in (
            'scripts/conductor36-table/coupled_plan.json',
            'scripts/conductor36-table/exponential_plan.json',
            'scripts/nonunitary-cusp/reduced_phase_certificate.json',
            'scripts/nonunitary-cusp/exact_value_certificate.json',
            'scripts/conductor36-table/verify_table.py',
            'scripts/conductor36-table/verify_exponential_plan.py',
            'scripts/conductor36-table/verify_coupled_plan.py',
            'scripts/conductor36-table/verify_compressed_plan.py',
            'scripts/general-relative/verify_certificate.py'))
        assert set(expected) == {str(p) for p in required}
        assert all(sha(p) == h for p, h in expected.items())
        check('complete_original_bindings_before_replay', True)
        # The CLI verifiers reconstruct all finite evidence, not only flags.
        commands = [
            [sys.executable, 'scripts/general-relative/verify_certificate.py',
             str(BASE/'presentation.json'), '--level', '36', '--out',
             str(ROOT/'coefficient-upstream-structure.json')],
            [sys.executable, str(BASE/'verify_table.py'), str(BASE/'table_certificate.json'),
             str(ROOT/'coefficient-upstream-table.json')]]
        for i, command in enumerate(commands):
            proc = subprocess.run(command, capture_output=True, text=True)
            (ROOT/('upstream-command-%d.txt' % i)).write_text(proc.stdout+proc.stderr)
            assert proc.returncode == 0, ('upstream replay', i, proc.returncode)
        structure_report = json.loads((ROOT/'coefficient-upstream-structure.json').read_text())
        table_report = json.loads((ROOT/'coefficient-upstream-table.json').read_text())
        assert not structure_report['failures'] and not table_report['failures']
        assert table_report['replay_passed'] and table_report['table_complete']
        assert table_report['checks']['Fourier_terms'] == 476280
        assert table_report['checks']['integer_isolations'] == 72
        assert table_report['checks']['generator_reconstructions'] == 72
        assert all(structure_report['actual'][k] == v for k,v in structure_report['required'].items())
        report['upstream_replays'] = {
            'structure': str(ROOT/'coefficient-upstream-structure.json'),
            'table': str(ROOT/'coefficient-upstream-table.json')}
        check('fresh_complete_upstream_finite_replay', True)
        base = json.loads((BASE/'presentation.json').read_text())
        table = json.loads((BASE/'table_certificate.json').read_text())
        assert base['inputs'] == {'N': 36, 'P': []}
        assert table['arithmetic_evidence']['arithmetic']['model'] == [0,0,0,0,1]
        assert cert['instance'] == {'model': [0,0,0,0,1], 'p': 7, 'level': 36,
                                    'C': 0, 'gamma': 8, 'branch': 'primitive untwisted trivial',
                                    'period': 'total minimal real'}
        points = [[x,y] for x in range(7) for y in range(7) if (y*y-x*x*x-1)%7 == 0]
        ordinary = cert['ordinary']
        assert len(ordinary['rows']) == 7
        for x,row in enumerate(ordinary['rows']):
            ys = [y for a,y in points if a == x]
            rhs = (x*x*x+1)%7
            assert row == {'x': x, 'rhs': rhs, 'disc': rhs, 'legendre': len(ys)-1,
                           'ys': ys, 'count': len(ys)}
        t = 8-(len(points)+1)
        assert ordinary['point_count'] == len(points)+1 == 12 and ordinary['t'] == t == -4
        assert ordinary['point_at_infinity'] == [0,1,0]
        assert ordinary['discriminant_mod_p'] == (-432)%7
        assert ordinary['good'] and gcd(432,7)==1 and ordinary['ordinary'] and t%7
        report['ordinary_replay'] = {'affine_points': points, 'point_count': 12, 't': t}
        check('exact_model_and_exhaustive_49_pair_ordinary_count', True)
        coords = base['presentation']['generator_coordinates']
        assert len(coords) == 72 and base['presentation']['d'] == 13
        for row in coords: integer_row(row,13)
        lifts = base['cosets']['lifts']
        assert len(lifts) == 72
        # Independent partition of ALL primitive pairs at composite level.
        units = [u for u in range(36) if gcd(u,36)==1]
        primitive = {(c,d) for c in range(36) for d in range(36) if gcd(gcd(c,d),36)==1}
        unseen, reps = set(primitive), []
        while unseen:
            c,d = min(unseen)
            orbit = {(u*c%36,u*d%36) for u in units}
            assert orbit <= unseen and len(orbit)==len(units)
            reps.append([c,d]); unseen -= orbit
        assert base['cosets']['representatives'] == reps and len(reps)==72
        for h,rep in zip(lifts,reps):
            A,B,C,D = integer_row(h,4)
            assert A*D-B*C==1
            assert any([u*C%36,u*D%36]==rep for u in units)
        f = [rational(v) for v in table['relations']['quotient_values']]
        y = [rational(row['value']) for row in table['generators']]
        assert len(f)==13 and len(y)==72
        assert [row['generator_id'] for row in table['generators']]==list(range(72))
        assert all(dot(row,f)==v for row,v in zip(coords,y))
        assert lcm(*(v.denominator for v in y))==table['relations']['common_denominator']==12
        assert sum(v==0 for v in y)==16
        assert all((12*v).denominator==1 and (order(v)=='infinity' or order(v)>=0) for v in y)
        scaled = [int(12*v) for v in y]
        relations = base['A']['entries']
        saturated = list(map(list,zip(*base['presentation']['K']['entries'])))
        assert len(relations)==144 and len(saturated)==59
        for row in relations+saturated: assert dot(integer_row(row,72),scaled)==0
        check('full_composite_orbits_and_all_normalized_values_relations_quotient', True)

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
            previous, raw = [1, 0], [0]*72
            for seg in saved['segments']:
                A, B, C, D = integer_row(seg['lift'], 4)
                assert A*D-B*C == 1
                assert seg['start'] == previous == cusp([B, D])
                assert seg['end'] == cusp([A, C])
                hits = []
                for i, (e, f0, g, k) in enumerate(lifts):
                    gamma = [A*k-B*g, -A*f0+B*e, C*k-D*g, -C*f0+D*e]
                    if gamma[2] % 36 == 0:
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
            assert integer_row(saved['raw'], 72) == raw
            quotient = [sum(raw[i]*coords[i][j] for i in range(72)) for j in range(13)]
            assert integer_row(saved['coordinates'], 13) == quotient
            value12 = dot(raw, scaled)
            assert Q(value12, 12) == dot(quotient, f) == rational(saved['value'])
            computed[key] = value12
            report['path_replay'][key] = {'raw': raw, 'coordinates': quotient,
                                         'value12': value12, 'segments': len(saved['segments'])}
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
            sum_A12, sum_B12, term_sum = 0, 0, Q(0)
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
                A12, B12 = computed[A_key], computed[B_key]
                A, B = Q(A12, 12), Q(B12, 12)
                assert rational(term['A']) == A and rational(term['B']) == B
                value = weight*(A/u**n-B/u**(n+1))
                assert rational(term['term']) == value
                term_sum += value
                sum_A12 += weight*A12
                sum_B12 += weight*B12
                seen_residues.append(r)
                used_paths.update((A_key, B_key))
            assert sorted(seen_residues) == [x for x in range(1, 7**n) if x % 7 != 0]
            # Integer numerator accumulation avoids the builder's summation path.
            b = Q(int(u)*sum_A12-sum_B12, 12*int(u)**(n+1))
            v = order(b)
            strict = v != 'infinity' and a['N'] > v
            assert term_sum == b == rational(a['b'])
            assert rational(a['sum_A']) == Q(sum_A12, 12) and rational(a['sum_B']) == Q(sum_B12, 12)
            assert a['valuation_b'] == v and a['strict_bound'] is strict
            report['attempts'].append({'n': n, 'M': M, 'N': a['N'], 'u': str(u),
                                        'residual': residual, 'valuation_residual': order(residual),
                                        'sum_A12': sum_A12, 'sum_B12': sum_B12, 'b': str(b),
                                        'valuation_b': v, 'strict_bound': strict,
                                        'actual_terms': len(a['terms']), 'required_terms': 6*7**(n-1)})
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
        report['traceback'] = traceback.format_exc()
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
