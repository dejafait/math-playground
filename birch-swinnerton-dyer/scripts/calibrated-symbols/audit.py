#!/usr/bin/env python3
"""Fixed L032 audit: alternate Farey paths and complete doubled-value checks.

Imports neither production nor replay. Use with the complete prior replays;
the source theorems and normalization applicability are justified in L032.
"""
import hashlib
import json
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path('scripts/calibrated-symbols')


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dot(a, b):
    assert len(a) == len(b)
    return sum(x*y for x, y in zip(a, b))


def canonical(pair):
    assert len(pair) == 2 and all(type(x) is int for x in pair)
    a, b = pair
    assert (a, b) != (0, 0)
    if b == 0:
        return [1, 0]
    f = Q(a, b)
    return [f.numerator, f.denominator]


def main():
    report = {'checks': {}, 'failures': [], 'external_theorems_verified_by_script': False}
    def check(name, flag):
        report['checks'][name] = bool(flag)
        assert flag, name
    try:
        cert = json.loads((ROOT/'certificate.json').read_text())
        report['certificate_sha256'] = digest(ROOT/'certificate.json')
        required = [f'scripts/{topic}/{name}.json'
                    for topic in ('relative-t2', 'twist-five')
                    for name in ('certificate', 'verification', 'audit')]
        check('all_six_unchanged_input_hashes', set(cert['input_sha256']) == set(required)
              and all(digest(p) == cert['input_sha256'][p] for p in required))
        base = json.loads(Path(required[0]).read_text())
        replay = json.loads((ROOT/'verification.json').read_text())
        check('complete_L032_replay_bound_to_certificate',
              replay['certificate_sha256'] == report['certificate_sha256']
              and replay['failures'] == [] and len(replay['checks']) == 8
              and all(v is True for v in replay['checks'].values()))
        coords = base['presentation']['integral_generator_coordinates']
        lifts = base['SL2_lifts']
        v = [Q(x) for x in base['integration_line']['basis_functional']]
        y = [Q(x) for x in cert['integral_generator_values']]
        assert len(coords) == len(lifts) == len(y) == 390 and len(v) == 65
        assert all(len(row) == 65 and all(type(x) is int for x in row) for row in coords)
        check('all_390_values_and_65_basis_entries',
              y == [-dot(row, v) for row in coords]
              and [Q(x) for x in cert['basis_functional']] == [-x for x in v]
              and [Q(x) for x in base['integration_line']['integral_generator_values']]
              == [-x for x in y])

        # Identify a coset by testing Gamma_0 membership against ALL lifts.
        # This avoids the production/replay's modular-inverse lookup formula.
        def segment(start, end, h):
            a, b, c, d = h
            assert all(type(x) is int for x in h) and a*d-b*c == 1
            assert canonical([b, d]) == start and canonical([a, c]) == end
            matches = []
            for i, (e, f, g, k) in enumerate(lifts):
                gamma = [a*k-b*g, -a*f+b*e, c*k-d*g, -c*f+d*e]
                A, B, C, D = gamma
                if C % 389 == 0:
                    assert A*D-B*C == 1
                    assert [A*e+B*g, A*f+B*k, C*e+D*g, C*f+D*k] == h
                    matches.append((i, gamma))
            assert len(matches) == 1
            i, gamma = matches[0]
            return {'start': start, 'end': end, 'lift': h, 'coset': i,
                    'Gamma0_reduction': gamma}

        originals, alternatives = [], []
        chains = [
            [[1, 0], [0, 1], [1, 5]],
            [[1, 0], [0, 1], [1, 3], [2, 5]],
            [[1, 0], [1, 1], [2, 3], [3, 5]],
            [[1, 0], [1, 1], [4, 5]],
        ]
        assert len(cert['paths']) == 4
        for a, (path, chain) in enumerate(zip(cert['paths'], chains), 1):
            assert path['a'] == a and path['chi'] == (1 if a in (1, 4) else -1)
            previous, raw, witnesses = [1, 0], [0]*390, []
            for saved in path['segments']:
                assert saved['start'] == previous
                w = segment(saved['start'], saved['end'], saved['lift'])
                assert w == saved
                raw[w['coset']] += 1
                previous = saved['end']
                witnesses.append(w)
            assert previous == [a, 5] and raw == path['raw']
            original_coords = [sum(raw[i]*coords[i][j] for i in range(390)) for j in range(65)]
            assert original_coords == path['coordinates']
            original_value = dot(original_coords, v)
            assert original_value == Q(path['phi_value']) == (-1, 1, 1, -1)[a-1]
            originals.append({'a': a, 'segments': witnesses, 'phi_value': str(original_value)})

            raw, witnesses = [0]*390, []
            for start, end in zip(chain, chain[1:]):
                b, d = start
                A, C = end
                det = A*d-b*C
                assert abs(det) == 1
                h = [det*A, b, det*C, d]
                w = segment(start, end, h)
                raw[w['coset']] += 1
                witnesses.append(w)
            alternate_coords = [sum(raw[i]*coords[i][j] for i in range(390)) for j in range(65)]
            residual = [x-z for x, z in zip(alternate_coords, original_coords)]
            assert residual == [0]*65
            assert dot(raw, y) == -original_value
            alternatives.append({'a': a, 'segments': witnesses, 'raw': raw,
                                 'coordinates': alternate_coords,
                                 'original_coordinate_residual': residual,
                                 'F_value': str(dot(raw, y))})
        check('all_original_segments_by_exhaustive_coset_membership',
              sum(len(x['segments']) for x in originals) == 12)
        check('four_alternate_paths_agree_in_full_relative_module', len(alternatives) == 4)
        report['original_paths'] = originals
        report['alternate_paths'] = alternatives

        # Reconstruct source tau=(1,-1;1,0) relations by cross products,
        # rather than the builders' U=tau^2 permutations.
        cosets = [[1, i] for i in range(389)]+[[0, 1]]
        def locate(c, d):
            hits = [i for i, (e, f) in enumerate(cosets) if (c*f-d*e) % 389 == 0]
            assert len(hits) == 1
            return hits[0]
        rows = []
        for i, (c, d) in enumerate(cosets):
            two, three = [0]*390, [0]*390
            for j in (i, locate(d, -c)):
                two[j] += 1
            for j in (i, locate(c+d, -c), locate(d, -c-d)):
                three[j] += 1
            rows.extend([two, three])
        assert rows == base['relations']
        doubled = [2*x for x in y]
        assert all(x.denominator == 1 for x in doubled)
        doubled = [int(x) for x in doubled]
        saturated = base['presentation']['saturated_relation_basis']
        assert len(saturated) == 325
        assert all(len(row) == 390 and all(type(x) is int for x in row) for row in saturated)
        residuals = {'source_Manin': [dot(row, doubled) for row in rows],
                     'saturated': [dot(row, doubled) for row in saturated]}
        check('all_source_and_saturated_relations_on_doubled_values',
              residuals['source_Manin'] == [0]*780 and residuals['saturated'] == [0]*325)
        check('exact_value_set_and_denominator_two',
              set(y) == {Q(0), Q(1), Q(-1), Q(1, 2), Q(-1, 2)}
              and y[7] == Q(-1, 2) and cert['denominator']['lcm'] == 2
              and cert['denominator']['prime_factorization'] == [[2, 1]])
        raw = [sum(path['chi']*path['raw'][i] for path in cert['paths']) for i in range(390)]
        check('scale_minus_one_uses_independent_q_four',
              raw == cert['G5']['raw'] and dot(raw, [-x for x in y]) == Q(cert['G5']['phi_value']) == -4
              and Q(cert['scale']) == Q(4, -4) == -1 and dot(raw, y) == 4)
        report['doubled_generator_values'] = doubled
        report['relation_residuals'] = residuals
        report['results'] = {'original_segments': 12, 'alternate_segments': sum(len(x['segments']) for x in alternatives),
                             'generator_count': len(y), 'required_generator_count': 390,
                             'value_counts': dict(sorted(Counter(map(str, y)).items())),
                             'd': '-4', 'scale': '-1', 'common_denominator': 2,
                             'C_for_retained_primes': 0}
    except Exception as error:
        report['failures'].append(f'{type(error).__name__}: {error}')
    out = ROOT/'audit.json'
    out.write_text(json.dumps(report, indent=2)+'\n')
    print('checks', len(report['checks']), 'results', report.get('results', {}),
          'failures', report['failures'], 'full evidence', out)
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
