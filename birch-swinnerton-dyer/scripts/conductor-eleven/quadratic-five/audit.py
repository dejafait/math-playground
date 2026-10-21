#!/usr/bin/env python3
"""One fixed L047 audit: isolated replay and complementary upper paths."""
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import sys
from fractions import Fraction as Q
from math import lcm
from pathlib import Path

ROOT = Path('scripts/conductor-eleven/quadratic-five')
BASE = ROOT.parent
OUT = ROOT/'critical-audit'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2)+'\n')


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def dot(a, b):
    assert len(a) == len(b)
    return sum(x*y for x, y in zip(a, b))


def product(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return [a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h]


def inverse(x):
    a, b, c, d = x
    assert a*d-b*c == 1
    return [d, -b, -c, a]


def main():
    assert sys.flags.optimize == 0
    OUT.mkdir(parents=True, exist_ok=True)
    cert = read(ROOT/'certificate.json')
    names = ['certificate.json', 'verification.json', 'build_certificate.py',
             'verify_certificate.py']
    names += [str(p.relative_to(ROOT)) for p in sorted((ROOT/'upstream-replay').rglob('*')) if p.is_file()]
    original = {name: sha(ROOT/name) for name in names}
    bindings = cert['input_sha256']
    report = {'program_sha256': sha(__file__), 'original_sha256': original,
              'checks': {}, 'failures': [], 'external_theorems_verified_by_script': False}

    def check(label, condition):
        report['checks'][label] = bool(condition)
        assert condition, label

    try:
        for name, digest in original.items():
            dest = OUT/'originals'/name
            dest.parent.mkdir(parents=True, exist_ok=True)
            if dest.exists():
                assert sha(dest) == digest
            else:
                dest.write_bytes((ROOT/name).read_bytes())
        check('prior_bindings_before_replay', all(sha(p) == h for p, h in bindings.items()))
        for p, digest in bindings.items():
            dest = OUT/'originals/upstream'/(p+'.snapshot' if p.endswith('.md') else p)
            dest.parent.mkdir(parents=True, exist_ok=True)
            if dest.exists():
                assert sha(dest) == digest
            else:
                dest.write_bytes(Path(p).read_bytes())
        check('all_bound_upstream_bytes_archived', all(sha(OUT/'originals/upstream'/(p+'.snapshot' if p.endswith('.md') else p)) == h for p, h in bindings.items()))
        save(OUT/'pre-replay-manifest.json', {'original_sha256': original, 'prior_input_sha256': bindings})
        builder = module(OUT/'originals/build_certificate.py', 'l047_preserved_builder')
        builder.ROOT = OUT/'rebuild'
        log = io.StringIO()
        with contextlib.redirect_stdout(log):
            builder.main()
        (OUT/'rebuild/replay.txt').write_text(log.getvalue())
        check('isolated_rebuild_exact_bytes', sha(builder.ROOT/'certificate.json') == original['certificate.json'])
        verifier = module(OUT/'originals/verify_certificate.py', 'l047_preserved_verifier')

        def execute(data, directory):
            directory.mkdir(parents=True, exist_ok=True)
            save(directory/'certificate.json', data)
            # Seed a success so failed replay must replace it with fresh evidence.
            save(directory/'verification.json', read(ROOT/'verification.json'))
            verifier.ROOT = directory
            log, code = io.StringIO(), 0
            try:
                with contextlib.redirect_stdout(log):
                    verifier.main()
            except SystemExit as error:
                code = error.code
            finally:
                (directory/'replay.txt').write_text(log.getvalue())
            return code, read(directory/'verification.json')

        code, fresh = execute(cert, OUT/'replay')
        check('complete_replay', code == 0 and not fresh['failures'] and all(fresh['checks'].values()))
        old = read(ROOT/'verification.json')
        comparable = copy.deepcopy(fresh)
        comparable['upstream_replay'] = old['upstream_replay']
        check('original_report_agrees_except_output_paths', comparable == old)
        report['complete_replay'] = fresh
        structural = read(OUT/'replay/upstream-replay/dual-verification-structure/general-verification.json')
        check('every_upstream_domain_and_218_segments', not structural['failures']
              and all(structural['actual'][k] == v for k, v in structural['required'].items())
              and structural['actual']['segments'] == 218)
        check('full_structural_report_equals_original', structural == read(ROOT/'upstream-replay/dual-verification-structure/general-verification.json'))
        report['upstream_domain_counts'] = {'actual': structural['actual'], 'required': structural['required']}
        check('original_1120_paths_6688_segments_620_terms', fresh['results']['paths'] == 1120
              and fresh['results']['segments'] == 6688 and fresh['results']['required_segment_occurrences'] == 6688
              and [a['actual_terms'] for a in fresh['attempts']] == [20, 100, 500])

        base = read(BASE/'structural-certificate.json')
        pr = base['presentation']
        coords, lifts = pr['generator_coordinates'], base['cosets']['lifts']
        K, head = pr['K']['entries'], pr['head']['entries']
        assert len(coords) == len(lifts) == len(K) == 12 and len(head) == 9
        assert all(len(r) == 3 for r in coords) and all(len(r) == 9 for r in K)
        assert all(len(r) == 12 for r in head)

        def project(raw):
            return [sum(raw[i]*coords[i][j] for i in range(12)) for j in range(3)]

        # Ceiling Euclidean expansion r=[k0,k1,...]_- is distinct from
        # the production floor expansion. Denominators strictly decrease.
        alternatives, count = {}, 0
        for key, original_path in cert['paths'].items():
            r = Q(key)
            a, b = r.numerator, r.denominator
            digits = []
            while b:
                k = -((-a)//b)
                rem = k*b-a
                assert 0 <= rem < b
                digits.append(k)
                a, b = b, rem
            val = Q(digits[-1])
            for k in digits[-2::-1]:
                assert val != 0
                val = k-1/val
            assert val == r
            p0, q0, p1, q1 = 0, -1, 1, 0
            raw, chain, segments = [0]*12, [[1, 0]], []
            for k in digits:
                p2, q2 = k*p1-p0, k*q1-q0
                assert q2 > 0 and p2*q1-p1*q2 == -1
                start, end = [p1, q1], [p2, q2]
                h = [-p2, p1, -q2, q1]
                assert inverse(h)
                hits = [(i, product(h, inverse(g))) for i, g in enumerate(lifts)]
                hits = [(i, gamma) for i, gamma in hits if gamma[2] % 11 == 0]
                assert len(hits) == 1
                i, gamma = hits[0]
                assert inverse(gamma) and product(gamma, lifts[i]) == h
                raw[i] += 1
                segments.append({'start': start, 'end': end, 'lift': h,
                                 'coset': i, 'Gamma0_reduction': gamma})
                chain.append(end)
                p0, q0, p1, q1 = p1, q1, p2, q2
            assert chain[-1] == original_path['argument']
            assert chain[1] != original_path['segments'][0]['end']
            delta = [x-y for x, y in zip(raw, original_path['raw'])]
            c = [dot(row, delta) for row in head]
            quotient = project(raw)
            assert quotient == original_path['coordinates'] and project(delta) == [0, 0, 0]
            assert [dot(row, c) for row in K] == delta
            value = dot(quotient, [Q(5, 2), Q(5), Q(1)])
            assert value == Q(original_path['value'])
            alternatives[key] = {'argument': original_path['argument'], 'negative_cf': digits,
                                 'chain': chain, 'segments': segments, 'raw': raw,
                                 'coordinates': quotient, 'difference_from_original': delta,
                                 'saturated_coefficients': c, 'value': str(value)}
            count += len(segments)
        save(OUT/'alternative-paths.json', alternatives)
        check('all_1120_distinct_upper_chains_full_relative_equality', len(alternatives) == 1120)
        report['alternative_paths'] = {'actual': len(alternatives), 'required': 1120, 'segments': count,
                                       'distinct_raw_vectors': sum(v['raw'] != cert['paths'][k]['raw'] for k, v in alternatives.items()),
                                       'sha256': sha(OUT/'alternative-paths.json')}

        f = [Q(5, 2), Q(5), Q(1)]
        values = [dot(row, f) for row in coords]
        check('all_twelve_values_and_denominator', values == list(map(Q, ['-1','1','0','5','5/2','-5/2','-5','-5','-5/2','5/2','5','0']))
              and lcm(*(v.denominator for v in values)) == 2)
        check('all_source_and_saturated_pairings', all(dot(row, values) == 0 for row in base['A']['entries'])
              and all(dot(list(col), values) == 0 for col in zip(*K)))

        def valuation(x):
            x = Q(x)
            if not x:
                return 'infinity'
            v, num, den = 0, x.numerator, x.denominator
            while num % 5 == 0:
                v, num = v+1, num//5
            while den % 5 == 0:
                v, den = v-1, den//5
            return v

        # Reconstruct every root, label and summand solely from alternate paths.
        # Explicit expectations also detect a shortened production schedule.
        expected = [(2, 96, 9125, Q(90), Q(-10), Q(4325,442368)),
                    (3, 346, 119375, Q(5350), Q(700), Q(115650,895745041)),
                    (4, 2846, 8096875, Q(1360275), Q(164250), Q(120974325,5834780198523343))]
        check('exact_three_depth_schedule', [a['n'] for a in cert['attempts']] == [2,3,4])
        report['coefficients'] = []
        for attempt, (n, expected_u, residual, expected_A, expected_B, expected_b) in zip(cert['attempts'], expected):
            M, modulus = n+1, 5**n
            roots, root_evidence = [], []
            for d in range(1, 5):
                candidates = [w for w in range(d, modulus, 5) if (w**4-1) % modulus == 0]
                assert len(candidates) == 1
                w = candidates[0]
                row = {'d': d, 'w': w, 'fourth_residual': w**4-1,
                       'residual_valuation': valuation(w**4-1), 'derivative_mod_p': 4*w**3 % 5}
                assert row == attempt['teichmuller'][d-1] and row['derivative_mod_p']
                assert row['residual_valuation'] == 'infinity' or row['residual_valuation'] >= n
                roots.append(w)
                root_evidence.append(row)
            candidates = [u for u in range(1, 5**M, 5) if (u*u-u+5) % (5**M) == 0]
            assert candidates == [expected_u]
            u = candidates[0]
            check(f'n{n}_exact_unit_root_precision', u*u-u+5 == residual and valuation(residual) == M
                  and (2*u-1) % 5 == 1 and attempt['unit_root'] == {'u': str(u), 'residual': residual,
                  'residual_valuation': M, 'derivative_mod_p': 1, 'valuation': 0})
            terms, sums_A, sums_B = [], [], []
            for d, w in enumerate(roots, 1):
                row_A, row_B = Q(0), Q(0)
                for j in range(5**(n-1)):
                    r = w*6**j % modulus
                    A, B = (Q(alternatives[str(Q(r, den))]['value']) for den in [modulus, 5**(n-1)])
                    weight = sum(range(j))
                    term = weight*(A/Q(u)**n-B/Q(u)**(n+1))
                    saved = attempt['terms'][5**(n-1)*(d-1)+j]
                    assert saved == {'d': d, 'j': j, 'r': r, 'binomial': weight,
                                     'A_path': str(Q(r, modulus)), 'B_path': str(Q(r, 5**(n-1))),
                                     'A': str(A), 'B': str(B), 'term': str(term)}
                    row_A += weight*A
                    row_B += weight*B
                    terms.append(saved)
                sums_A.append(row_A)
                sums_B.append(row_B)
            b = sum((Q(v['term']) for v in terms), Q(0))
            check(f'n{n}_all_terms_both_weighted_sums', len(terms) == 4*5**(n-1)
                  and sum(sums_A) == expected_A and sum(sums_B) == expected_B
                  and b == expected_b == (expected_A*Q(u)-expected_B)/Q(u)**(n+1))
            N, vb = min(n-1, M), valuation(b)
            check(f'n{n}_limiting_threshold', vb == 2 and N == n-1 and (N > vb) == (n == 4)
                  and attempt['N'] == N and attempt['strict_bound'] == (n == 4))
            report['coefficients'].append({'n': n, 'M': M, 'C': 0, 'N': N, 'valuation_b': vb,
                    'strict_bound': N > vb, 'required_strictly_above': vb, 'u': u,
                    'residual': residual, 'valuation_residual': M, 'teichmuller': root_evidence,
                    'row_A': list(map(str, sums_A)), 'row_B': list(map(str, sums_B)),
                    'sum_A': str(sum(sums_A)), 'sum_B': str(sum(sums_B)), 'b': str(b),
                    'actual_terms': len(terms), 'required_terms': 4*5**(n-1), 'terms': terms})
        save(OUT/'alternate-coefficients.json', report['coefficients'])

        mutations = ['input_binding', 'path_coordinate', 'n2_false_strict_bound', 'n3_root_residual',
                     'n4_late_term', 'gamma', 'n4_limit_bound']
        report['rejections'] = {}
        for name in mutations:
            bad = copy.deepcopy(cert)
            if name == 'input_binding':
                bad['input_sha256'][next(iter(bad['input_sha256']))] = '0'*64
            elif name == 'path_coordinate':
                bad['paths'][next(iter(bad['paths']))]['coordinates'][2] += 1
            elif name == 'n2_false_strict_bound':
                bad['attempts'][0]['strict_bound'] = True
            elif name == 'n3_root_residual':
                bad['attempts'][1]['unit_root']['residual'] += 625
            elif name == 'n4_late_term':
                bad['attempts'][2]['terms'][-1]['term'] = str(Q(bad['attempts'][2]['terms'][-1]['term'])+1)
            elif name == 'gamma':
                bad['instance']['gamma'] = 5
            else:
                bad['attempts'][2]['N'] = 4
            directory = OUT/'rejections'/name
            code, rejected = execute(bad, directory)
            check('fresh_rejection_'+name, code != 0 and bool(rejected['failures']) and rejected['results'] == {}
                  and rejected['certificate_sha256'] == sha(directory/'certificate.json'))
            report['rejections'][name] = {'report': str(directory/'verification.json'), 'failures': rejected['failures']}
    except (Exception, SystemExit) as error:
        report['failures'].append(f'{type(error).__name__}: {error}')
    finally:
        report['original_inputs_unchanged'] = all(sha(ROOT/p) == h for p, h in original.items())
        report['prior_inputs_unchanged'] = all(sha(p) == h for p, h in bindings.items())
        if not report['original_inputs_unchanged'] or not report['prior_inputs_unchanged']:
            report['failures'].append('input bytes changed')
        save(OUT/'audit.json', report)
    print('audit checks', len(report['checks']), 'alternative paths', report.get('alternative_paths'),
          'bounds', [(a['n'], a['N'], a['valuation_b'], a['strict_bound']) for a in report.get('coefficients', [])], 'failures', report['failures'], 'report', OUT/'audit.json')
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
