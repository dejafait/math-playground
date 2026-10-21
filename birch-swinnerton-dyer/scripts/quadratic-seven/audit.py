#!/usr/bin/env python3
"""Complementary fixed n=2 audit: ceiling paths and full polynomial expansion.

Imports no notebook program. Canonical L027/L030--L032 supply theorems;
this program checks finite evidence, not those theorems.
"""
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path('scripts/quadratic-seven')

def read(path):
    return json.loads(Path(path).read_text())

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def dot(a, b):
    assert len(a) == len(b)
    return sum(x*y for x, y in zip(a, b))

def cusp(a, b):
    if not b:
        assert a
        return [1, 0]
    q = Q(a, b)
    return [q.numerator, q.denominator]

def valuation(x):
    x = Q(x)
    if not x:
        return 'infinity'
    a, b, v = x.numerator, x.denominator, 0
    while a % 7 == 0:
        a //= 7
        v += 1
    while b % 7 == 0:
        b //= 7
        v -= 1
    return v

def main():
    report = {'certificate_sha256': sha(ROOT/'certificate.json'),
              'checks': {}, 'failures': [], 'paths': {}, 'terms': [],
              'external_theorems_verified_by_script': False}
    def check(name, condition):
        report['checks'][name] = bool(condition)
        assert condition, name
    try:
        cert = read(ROOT/'certificate.json')
        base = read('scripts/relative-t2/certificate.json')
        cal = read('scripts/calibrated-symbols/certificate.json')
        run = read(ROOT/'audit-replays.json')
        expected = [f'scripts/{t}/{n}.json' for t in
                    ('relative-t2', 'twist-five', 'calibrated-symbols')
                    for n in ('certificate', 'verification', 'audit')]
        current = {p: sha(p) for p in expected}
        assert cert['input_sha256'] == current == run['before'] == run['after']
        assert len(run['runs']) == 7 and all(r['exit_code'] == 0 for r in run['runs'])
        assert run['unchanged'] is True
        check('all_input_hashes_and_complete_seven_replays', True)
        coords = base['presentation']['integral_generator_coordinates']
        lifts = base['SL2_lifts']
        f = [Q(x) for x in cal['basis_functional']]
        phi = [Q(x) for x in base['integration_line']['basis_functional']]
        y = [Q(x) for x in cal['integral_generator_values']]
        assert len(coords) == len(lifts) == len(y) == 390
        assert len(f) == len(phi) == 65 and f == [-v for v in phi]
        assert all(len(row) == 65 and all(type(x) is int for x in row) for row in coords)
        assert [dot(row, f) for row in coords] == y
        assert all((2*v).denominator == 1 for v in y) and y[7] == Q(-1, 2)
        relations = base['relations']+base['presentation']['saturated_relation_basis']
        assert len(relations) == 1105 and all(len(row) == 390 for row in relations)
        assert all(dot(row, y) == 0 for row in relations)
        check('all_390_values_65_coordinates_and_1105_relations', True)

        # Homogeneous count includes every projective point exactly once:
        # affine Z=1, then [X:1:0], then [1:0:0].
        projective = [[x, z, 1] for x in range(7) for z in range(7)]
        projective += [[x, 1, 0] for x in range(7)]+[[1, 0, 0]]
        points = [[x, yy, z] for x, yy, z in projective
                  if (yy*yy*z+yy*z*z-x**3-x*x*z+2*x*z*z) % 7 == 0]
        assert len(points) == 13 and [p for p in points if p[2] == 0] == [[0, 1, 0]]
        assert cert['ordinary']['point_count'] == 13 and cert['ordinary']['t'] == -5
        assert 389 % 7 and (-5) % 7
        report['projective_points'] = points
        check('complete_projective_count_good_ordinary', True)
        assert len(cert['attempts']) == 1
        a = cert['attempts'][0]
        assert (a['n'], a['M'], a['N']) == (2, 3, 1)
        assert cert['instance'] == {'model': [0, 1, 1, -2, 0], 'p': 7, 'level': 389,
                                   'C': 0, 'gamma': 8, 'branch': 'primitive untwisted trivial',
                                   'period': 'total minimal real'}
        roots = [w for w in range(1, 49) if (w**6-1) % 49 == 0]
        assert len(roots) == 6 and {w % 7 for w in roots} == set(range(1, 7))
        root_rows = []
        for d in range(1, 7):
            w, = [w for w in roots if w % 7 == d]
            row = {'d': d, 'w': w, 'sixth_residual': w**6-1,
                   'residual_valuation': valuation(w**6-1), 'derivative_mod_p': 6*w**5 % 7}
            assert row['derivative_mod_p'] and (row['residual_valuation'] == 'infinity' or row['residual_valuation'] >= 2)
            root_rows.append(row)
        assert root_rows == a['teichmuller']
        unit_candidates = [z for z in range(343) if z % 7 == 2 and (z*z+5*z+7) % 343 == 0]
        assert unit_candidates == [16]
        assert a['unit_root'] == {'u': '16', 'residual': 343, 'residual_valuation': 3,
                                  'derivative_mod_p': 2, 'valuation': 0}
        report['roots'] = {'teichmuller': root_rows, 'unit_root': a['unit_root'], 'unit_candidates': unit_candidates}
        check('all_simple_roots_and_exact_residuals', True)

        def segment(start, end):
            b, d = start
            aa, c = end
            sign = aa*d-b*c
            assert abs(sign) == 1
            A, B, C, D = sign*aa, b, sign*c, d
            assert A*D-B*C == 1
            # Projective bottom-row cross products, no modular inverses.
            hits = [i for i, (_, _, g, k) in enumerate(lifts) if (C*k-D*g) % 389 == 0]
            assert len(hits) == 1
            i = hits[0]
            e, ff, g, k = lifts[i]
            G, H, I, J = A*k-B*g, -A*ff+B*e, C*k-D*g, -C*ff+D*e
            assert G*J-H*I == 1 and I % 389 == 0
            assert [G*e+H*g, G*ff+H*k, I*e+J*g, I*ff+J*k] == [A,B,C,D]
            return {'start': start, 'end': end, 'lift': [A,B,C,D], 'coset': i,
                    'Gamma0_reduction': [G,H,I,J]}

        original_count = alternate_count = changed = 0
        values = {}
        for key, saved in cert['paths'].items():
            r = Q(key)
            assert saved['argument'] == cusp(r.numerator, r.denominator)
            original_raw = [0]*390
            previous = [1,0]
            for s in saved['segments']:
                assert s['start'] == previous
                rebuilt = segment(previous, s['end'])
                assert rebuilt == s
                original_raw[rebuilt['coset']] += 1
                previous = s['end']
                original_count += 1
            assert previous == saved['argument'] and original_raw == saved['raw']
            original_coords = [sum(original_raw[i]*coords[i][j] for i in range(390)) for j in range(65)]
            assert original_coords == saved['coordinates']
            assert dot(original_raw,y) == dot(original_coords,f) == Q(saved['value'])

            # Negative continued fraction: x=a-1/x', a=ceil(x).
            # Its endpoint is checked exactly; no convergence theorem is needed.
            x, digits = r, []
            while True:
                digit = -(-x.numerator//x.denominator)
                digits.append(digit)
                if x == digit:
                    break
                old_denominator = x.denominator
                x = 1/(digit-x)
                assert x.denominator < old_denominator
            previous, pm2, qm2, pm1, qm1 = [1,0], 0, -1, 1, 0
            raw, alt = [0]*390, []
            for digit in digits:
                p, q = digit*pm1-pm2, digit*qm1-qm2
                end = cusp(p,q)
                s = segment(previous,end)
                alt.append(s)
                raw[s['coset']] += 1
                previous, pm2, qm2, pm1, qm1 = end, pm1, qm1, p, q
            assert previous == saved['argument']
            quotient = [sum(raw[i]*coords[i][j] for i in range(390)) for j in range(65)]
            difference = [a-b for a,b in zip(quotient,original_coords)]
            assert difference == [0]*65
            value = dot(raw,y)
            assert value == dot(quotient,f) == Q(saved['value'])
            values[key] = value
            changed += alt != saved['segments']
            alternate_count += len(alt)
            report['paths'][key] = {'ceiling_digits': digits, 'segments': alt, 'raw':raw,
                                    'coordinates':quotient, 'difference':difference, 'value':str(value)}
        assert len(values) == 84 and original_count == 326
        report['path_counts'] = {'original':84,'original_segments':original_count,
                                 'alternate':84,'alternate_segments':alternate_count,'different_paths':changed}
        check('every_original_and_alternate_oriented_path_full_quotient', True)

        # Index by the 42 units, reconstruct their group coordinate by exhaustive
        # matching, and expand (1+T)^j by multiplication, with no binomial call.
        polyA, polyB = [Q(0)]*7, [Q(0)]*7
        seen, used_paths = set(), set()
        by_r = {term['r']:term for term in a['terms']}
        assert len(a['terms']) == len(by_r) == 42
        for r in range(1,49):
            if r % 7 == 0:
                continue
            candidates = [(w%7,j) for w in roots for j in range(7) if w*8**j % 49 == r]
            assert len(candidates) == 1
            d,j = candidates[0]
            seen.add((d,j))
            coeff = [1]
            for _ in range(j):
                coeff = [coeff[0]]+[coeff[k]+coeff[k-1] for k in range(1,len(coeff))]+[coeff[-1]]
            coeff += [0]*(7-len(coeff))
            ka, kb = str(Q(r,49)), str(Q(r,7))
            A,B = values[ka],values[kb]
            used_paths.update((ka,kb))
            for k in range(7):
                polyA[k] += coeff[k]*A
                polyB[k] += coeff[k]*B
            term = coeff[2]*(A/Q(16)**2-B/Q(16)**3)
            assert by_r[r] == {'d':d,'j':j,'r':r,'binomial':coeff[2],'A_path':ka,'B_path':kb,
                               'A':str(A),'B':str(B),'term':str(term)}
            report['terms'].append({'r':r,'d':d,'j':j,'power_coefficients':coeff,
                                     'A':str(A),'B':str(B),'quadratic_term':str(term)})
        assert seen == {(d,j) for d in range(1,7) for j in range(7)}
        assert used_paths == set(values)
        polynomial = [aa/Q(16)**2-bb/Q(16)**3 for aa,bb in zip(polyA,polyB)]
        b = polynomial[2]
        assert polyA[2] == Q(a['sum_A']) == 13 and polyB[2] == Q(a['sum_B']) == 0
        assert b == sum(Q(t['quadratic_term']) for t in report['terms']) == Q(a['b']) == Q(13,256)
        N, v = min(2-1-0,3-0), valuation(b)
        assert N == a['N'] == 1 and v == a['valuation_b'] == 0 and N>v
        assert a['strict_bound'] is True
        check('all_42_terms_full_expansion_and_strict_L027_bound', True)
        report['polynomials'] = {'A':[str(x) for x in polyA], 'B':[str(x) for x in polyB],
                                 'P2_u':[str(x) for x in polynomial]}
        report['result'] = {'b':str(b),'valuation_b':v,'tail_bound':1,'root_bound':3,
                            'N':N,'required':'N > valuation_b','strict':N>v,
                            'actual_terms':len(report['terms']),'required_terms':42,
                            'limiting_error_theorem':'L027; application reviewed in L033'}
    except Exception as error:
        report['failures'].append(f'{type(error).__name__}: {error}')
    out = ROOT/'audit.json'
    out.write_text(json.dumps(report,indent=2)+'\n')
    print('checks',len(report['checks']),'paths',report.get('path_counts'),
          'result',report.get('result'),'failures',report['failures'],'report',out)
    if report['failures']:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
