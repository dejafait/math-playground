#!/usr/bin/env python3
"""Separate bounded L041 audit; preserve production evidence and replay copies."""
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
from fractions import Fraction as F
from math import lcm
from pathlib import Path

ROOT = Path('scripts/conductor-eleven/calibrated-symbols')
OUT = ROOT/'critical-audit'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2)+'\n')


def product(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return [a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h]


def inverse(x):
    a, b, c, d = x
    assert a*d-b*c == 1
    return [d, -b, -c, a]


def dot(x, y):
    assert len(x) == len(y)
    return sum(a*b for a, b in zip(x, y))


def run():
    OUT.mkdir(parents=True, exist_ok=True)
    names = ['certificate.json', 'verification.json', 'build_certificate.py',
             'verify_certificate.py', 'audit.py']
    original_hashes = {name: sha(ROOT/name) for name in names}
    for name in names:
        destination = OUT/'originals'/name
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            assert sha(destination) == original_hashes[name], 'preserved original differs'
        else:
            destination.write_bytes((ROOT/name).read_bytes())
    cert = read(ROOT/'certificate.json')
    bindings = cert['input_sha256']
    assert all(sha(path) == h for path, h in bindings.items())
    save(OUT/'pre-replay-manifest.json', {'original_sha256': original_hashes,
                                      'prior_input_sha256': bindings})
    report = {'original_sha256': original_hashes, 'checks': {}, 'failures': []}

    def check(label, condition):
        report['checks'][label] = bool(condition)
        if not condition:
            raise AssertionError(label)

    try:
        spec = importlib.util.spec_from_file_location('l041_replay', OUT/'originals/verify_certificate.py')
        replay = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(replay)

        def execute(data, directory, seed=None):
            directory.mkdir(parents=True, exist_ok=True)
            save(directory/'certificate.json', data)
            if seed is not None:
                save(directory/'verification.json', seed)
            replay.SOURCE, replay.OUT = directory/'certificate.json', directory/'verification.json'
            output = io.StringIO()
            code = 0
            with contextlib.redirect_stdout(output):
                try:
                    replay.verify()
                except SystemExit as error:
                    code = error.code
            (directory/'replay.txt').write_text(output.getvalue())
            return code, read(replay.OUT)

        code, fresh = execute(cert, OUT/'replay')
        check('complete_replay_equals_original', code == 0 and not fresh['failures']
              and fresh == read(ROOT/'verification.json'))
        report['complete_replay'] = fresh

        base = read('scripts/conductor-eleven/structural-certificate.json')
        dual = read('scripts/conductor-eleven/dual-certificate.json')
        pr = base['presentation']
        coordinates, lifts = pr['generator_coordinates'], base['cosets']['lifts']
        phi = [F(x) for x in dual['line']['v']]
        K, head = pr['K']['entries'], pr['head']['entries']
        check('fixed_full_relative_shapes', len(coordinates) == len(lifts) == 12
              and all(len(row) == 3 for row in coordinates) and len(K) == 12
              and all(len(row) == 9 for row in K) and len(head) == 9
              and all(len(row) == 12 for row in head))

        def locate(h):
            # Exhaust exact Gamma_0 group reductions, not a bottom-row lookup.
            candidates = [(i, product(h, inverse(g))) for i, g in enumerate(lifts)]
            matches = [(i, gamma) for i, gamma in candidates if gamma[2] % 11 == 0]
            assert len(matches) == 1
            i, gamma = matches[0]
            assert inverse(gamma) and product(gamma, lifts[i]) == h
            return i, gamma

        def project(raw):
            return [sum(raw[i]*coordinates[i][j] for i in range(12)) for j in range(3)]

        # These upper Farey chains are specified independently of both CF programs.
        chains = [
            [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],
            [[1, 0], [1, 1], [1, 2], [2, 5]],
            [[1, 0], [1, 1], [2, 3], [3, 5]],
            [[1, 0], [1, 1], [4, 5]],
        ]
        paths = []
        for a, chain in enumerate(chains, 1):
            raw, segments = [0]*12, []
            assert chain[0] == [1, 0] and chain[-1] == [a, 5]
            for start, end in zip(chain, chain[1:]):
                determinant = end[0]*start[1]-start[0]*end[1]
                assert abs(determinant) == 1
                h = [determinant*end[0], start[0], determinant*end[1], start[1]]
                assert h[0]*h[3]-h[1]*h[2] == 1
                # Projective endpoint equality, including infinity, without normalization code.
                assert h[0]*end[1] == h[2]*end[0]
                assert h[1]*start[1] == h[3]*start[0]
                index, gamma = locate(h)
                raw[index] += 1
                segments.append({'start': start, 'end': end, 'lift': h,
                                 'coset': index, 'Gamma0_reduction': gamma})
            original = cert['paths'][a-1]
            quotient = project(raw)
            diff = [x-y for x, y in zip(raw, original['raw'])]
            coeffs = [dot(row, diff) for row in head]
            check('distinct_path_'+str(a), raw != original['raw'] and len(segments) != 0)
            check('full_quotient_path_'+str(a), quotient == original['coordinates']
                  and project(diff) == [0]*3 and [dot(row, coeffs) for row in K] == diff)
            paths.append({'a': a, 'chain': chain, 'segments': segments, 'raw': raw,
                          'coordinates': quotient, 'phi_value': str(dot(quotient, phi)),
                          'difference_from_original': diff, 'saturated_coefficients': coeffs})

        signs = [1, -1, -1, 1]
        total = [sum(sign*path['raw'][i] for sign, path in zip(signs, paths)) for i in range(12)]
        quotient = project(total)
        d = dot(quotient, phi)
        check('alternative_character_sum', quotient == [0, 5, 0] and d == 25
              and sum(sign*F(path['phi_value']) for sign, path in zip(signs, paths)) == d)
        scale = F(5)/d  # Independent q from audited L040, not inferred from this sum.
        y = [scale*dot(row, phi) for row in coordinates]
        expected = [F(-1, 5), F(1, 5), F(0), F(1), F(1, 2), F(-1, 2),
                    F(-1), F(-1), F(-1, 2), F(1, 2), F(1), F(0)]
        check('all_twelve_values', scale == F(1, 5) and y == expected
              and y == [F(x) for x in cert['integral_generator_values']])

        # Reconstruct each relation by actual right multiplication of integral lifts.
        S, U = [0, -1, 1, 0], [0, -1, 1, -1]
        relations = []
        for i, g in enumerate(lifts):
            row2, row3 = [0]*12, [0]*12
            row2[i] += 1
            row2[locate(product(g, S))[0]] += 1
            row3[i] += 1
            row3[locate(product(g, U))[0]] += 1
            row3[locate(product(product(g, U), U))[0]] += 1
            relations.extend([row2, row3])
        sat = list(map(list, zip(*K)))
        residuals = {label: [str(dot(row, y)) for row in rows]
                     for label, rows in [('Manin', relations), ('saturated', sat)]}
        check('all_source_and_saturated_relations', len(relations) == 24 and len(sat) == 9
              and relations == base['A']['entries'] and residuals == cert['relation_residuals']
              and all(F(x) == 0 for rows in residuals.values() for x in rows)
              and all(project(row) == [0]*3 for row in relations+sat))
        denominators = [v.denominator for v in y]
        common = lcm(*denominators)
        check('all_reduced_denominators', denominators == [5, 5, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]
              and common == cert['denominator']['lcm'] == 10
              and cert['denominator']['prime_factorization'] == [[2, 1], [5, 1]])
        alternative = {'paths': paths, 'character_raw': total, 'character_coordinates': quotient,
                       'd': str(d), 'scale': str(scale), 'values': [str(v) for v in y],
                       'source_relations': relations, 'saturated_relations': sat,
                       'relation_residuals': residuals, 'denominators': denominators,
                       'common_denominator': common, 'failures': []}
        save(OUT/'alternative-paths.json', alternative)
        report['alternative_sha256'] = sha(OUT/'alternative-paths.json')

        mutations = {}
        changed = copy.deepcopy(cert)
        changed['paths'][0]['segments'][0]['start'] = [0, 1]
        mutations['reversed-start'] = changed
        changed = copy.deepcopy(cert)
        changed['paths'][1]['coordinates'][0] += 1
        mutations['full-relative-coordinate'] = changed
        changed = copy.deepcopy(cert)
        changed['scale'] = '1/10'
        mutations['scale'] = changed
        changed = copy.deepcopy(cert)
        changed['integral_generator_values'][4] = '1'
        mutations['generator-value'] = changed
        changed = copy.deepcopy(cert)
        changed['denominator']['lcm'] = 2
        mutations['omitted-five'] = changed
        report['expected_rejections'] = {}
        for name, changed in mutations.items():
            directory = OUT/'rejections'/name
            code, result = execute(changed, directory, seed=fresh)
            check('rejection_'+name, code == 1 and bool(result['failures']) and result['results'] == {}
                  and result['certificate_sha256'] == sha(directory/'certificate.json'))
            report['expected_rejections'][name] = result['failures']
        report['results'] = {'original_paths_actual_required': [4, 4],
                             'original_segments_actual_required': [fresh['results']['segments'], 12],
                             'distinct_paths_actual_required': [len(paths), 4],
                             'distinct_segments_actual_required': [sum(len(p['segments']) for p in paths), 13],
                             'values_actual_required': [len(y), 12],
                             'source_relations_actual_required': [len(relations), 24],
                             'saturated_relations_actual_required': [len(sat), 9],
                             'd': str(d), 'scale': str(scale), 'denominator': common,
                             'C_for_good_ordinary_p_ge_5_p_ne_5': 0}
        check('all_counts_match', all(pair[0] == pair[1] for name, pair in report['results'].items()
                                      if name.endswith('_actual_required')))
    except Exception as error:
        report['failures'].append(type(error).__name__+': '+str(error))
    finally:
        report['original_inputs_unchanged'] = all(sha(ROOT/name) == value for name, value in original_hashes.items())
        report['prior_inputs_unchanged'] = all(sha(path) == value for path, value in bindings.items())
        if not report['original_inputs_unchanged'] or not report['prior_inputs_unchanged']:
            report['failures'].append('original or prior input bytes changed')
        save(OUT/'audit.json', report)
    print('checks', len(report['checks']), 'failures', report['failures'],
          'results', report.get('results', {}), 'report', OUT/'audit.json')
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
