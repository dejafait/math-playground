#!/usr/bin/env python3
"""One fixed L042 audit: isolated replay and complementary upper paths."""
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

ROOT = Path('scripts/conductor-eleven/quadratic-seven')
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
             'verify_certificate.py', 'development-failure-01.json']
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
        save(OUT/'pre-replay-manifest.json', {'original_sha256': original, 'prior_input_sha256': bindings})
        builder = module(OUT/'originals/build_certificate.py', 'l042_preserved_builder')
        builder.ROOT = OUT/'rebuild'
        log = io.StringIO()
        with contextlib.redirect_stdout(log):
            builder.main()
        (OUT/'rebuild/replay.txt').write_text(log.getvalue())
        check('isolated_rebuild_exact_bytes', sha(builder.ROOT/'certificate.json') == original['certificate.json'])
        verifier = module(OUT/'originals/verify_certificate.py', 'l042_preserved_verifier')

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
        check('original_84_paths_326_segments_42_terms', fresh['results']['paths'] == 84
              and fresh['results']['segments'] == 326 and fresh['results']['required_segment_occurrences'] == 326
              and len(fresh['attempts']) == 1 and fresh['attempts'][0]['actual_terms'] == 42)
        check('development_failure_retained', bool(read(ROOT/'development-failure-01.json')['failures']))

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
            value = dot(quotient, [Q(1, 2), Q(1), Q(1, 5)])
            assert value == Q(original_path['value'])
            alternatives[key] = {'argument': original_path['argument'], 'negative_cf': digits,
                                 'chain': chain, 'segments': segments, 'raw': raw,
                                 'coordinates': quotient, 'difference_from_original': delta,
                                 'saturated_coefficients': c, 'value': str(value)}
            count += len(segments)
        save(OUT/'alternative-paths.json', alternatives)
        check('all_84_distinct_upper_chains_full_relative_equality', len(alternatives) == 84)
        report['alternative_paths'] = {'actual': len(alternatives), 'required': 84, 'segments': count,
                                       'distinct_raw_vectors': sum(v['raw'] != cert['paths'][k]['raw'] for k, v in alternatives.items()),
                                       'sha256': sha(OUT/'alternative-paths.json')}

        f = [Q(1, 2), Q(1), Q(1, 5)]
        values = [dot(row, f) for row in coords]
        check('all_twelve_values_and_denominator', values == list(map(Q, ['-1/5','1/5','0','1','1/2','-1/2','-1','-1','-1/2','1/2','1','0']))
              and lcm(*(v.denominator for v in values)) == 10)
        check('all_source_and_saturated_pairings', all(dot(row, values) == 0 for row in base['A']['entries'])
              and all(dot(list(col), values) == 0 for col in zip(*K)))
        # Independently enumerate the simple roots and term labels; use only
        # alternative path evaluations, and exact rational accumulation.
        roots = [next(w for w in range(d, 49, 7) if (w**6-1) % 49 == 0) for d in range(1, 7)]
        assert roots == [1, 30, 31, 18, 19, 48]
        candidates = [u for u in range(343) if u % 7 == 5 and (u*u+2*u+7) % 343 == 0]
        assert candidates == [222]
        u = candidates[0]
        check('exact_unit_root_precision', u*u+2*u+7 == 145*343 and 145 % 7 != 0 and (2*u+2) % 7 == 5)
        terms, sums_A, sums_B = [], [], []
        for d, w in enumerate(roots, 1):
            row_A, row_B = Q(0), Q(0)
            for j in range(7):
                r = w*8**j % 49
                A, B = (Q(alternatives[str(Q(r, den))]['value']) for den in [49, 7])
                weight = sum(range(j))
                term = weight*(A/Q(u)**2-B/Q(u)**3)
                saved = cert['attempts'][0]['terms'][7*(d-1)+j]
                assert saved == {'d': d, 'j': j, 'r': r, 'binomial': weight,
                                 'A_path': str(Q(r, 49)), 'B_path': str(Q(r, 7)),
                                 'A': str(A), 'B': str(B), 'term': str(term)}
                row_A += weight*A
                row_B += weight*B
                terms.append(saved)
            sums_A.append(row_A)
            sums_B.append(row_B)
        b = sum((Q(v['term']) for v in terms), Q(0))
        check('all_42_terms_both_weighted_sums', len(terms) == 42 and sum(sums_A) == -18 and sum(sums_B) == -28
              and b == Q(-496, 1367631) == (-18*Q(u)+28)/Q(u)**3)
        N = min(2-1-0, 3-0)
        check('limiting_not_only_finite_threshold', N == 1 and b.numerator % 7 != 0 and b.denominator % 7 != 0 and N > 0)
        report['coefficient'] = {'row_A': list(map(str, sums_A)), 'row_B': list(map(str, sums_B)),
                                 'sum_A': '-18', 'sum_B': '-28', 'b': str(b), 'valuation_b': 0,
                                 'n': 2, 'M': 3, 'C': 0, 'N': N, 'required_strictly_above': 0,
                                 'terms': terms}

        mutations = ['path_coordinate', 'root_residual', 'late_term', 'gamma', 'limit_bound']
        report['rejections'] = {}
        for name in mutations:
            bad = copy.deepcopy(cert)
            if name == 'path_coordinate':
                bad['paths'][next(iter(bad['paths']))]['coordinates'][2] += 1
            elif name == 'root_residual':
                bad['attempts'][0]['unit_root']['residual'] += 343
            elif name == 'late_term':
                bad['attempts'][0]['terms'][6]['term'] = '0'
                assert cert['attempts'][0]['terms'][6]['term'] != '0'
            elif name == 'gamma':
                bad['instance']['gamma'] = 7
            else:
                bad['attempts'][0]['N'] = 2
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
          'b', report.get('coefficient', {}).get('b'), 'actual N', report.get('coefficient', {}).get('N'),
          'required >', 0, 'failures', report['failures'], 'report', OUT/'audit.json')
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
