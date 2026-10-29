#!/usr/bin/env python3
"""Audit complete L124 evidence; preserve original programs and certificates.

Reviewed producer/verifier replays supplement an independent rational check
of every enclosure and a paired-index reconstruction of every Fourier mode.
This does not rerun the accepted upstream enumeration or prove core sharpness.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import sys
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True
BASE = Path(__file__).resolve().parent
OUT = BASE / 'l124-critical-audit.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name):
    return json.loads((BASE / name).read_text())


def module(name):
    spec = importlib.util.spec_from_file_location(name, BASE / (name + '.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    checks, failures = [], []
    report = {'complete': False, 'checks': checks, 'failures': failures}

    def ck(name, actual, required=True):
        ok = actual == required
        checks.append({'name': name, 'actual': actual, 'required': required, 'ok': ok})
        if not ok:
            raise ValueError(name)

    try:
        d = read('ratio-spectral-bound.json')
        v = read('ratio-spectral-verification.json')
        a, c = read('l123-critical-audit.json'), read('c122a-critical-audit.json')
        expected_hashes = {}
        for tag, upstream, count in [('l123', a, 207), ('c122a', c, 420)]:
            ck(tag + '_accepted_completion', upstream['complete'] and not upstream['failures'])
            ck(tag + '_check_count', len(upstream['checks']), count)
            ck(tag + '_all_checks', all(row['ok'] for row in upstream['checks']))
            expected_hashes.update(upstream['original_sha256'])
            expected_hashes['critical_audit_' + tag + '.py'] = upstream['script_sha256']
            expected_hashes[tag + '-critical-audit.json'] = sha(BASE / (tag + '-critical-audit.json'))
        expected_hashes.update(c['fresh_artifacts'])
        ck('complete_input_hash_dictionary', d['input_sha256'], expected_hashes)
        for name, expected in expected_hashes.items():
            ck('input_hash_' + name, sha(BASE / name), expected)
        ck('endpoint_manifest_all_fields', read('endpoint-pair-count.json'), a['expected_complete_manifest'])
        ck('histogram_manifest_all_fields', read('l122-full-count.json'), c['expected_production_manifest'])
        ck('histogram_replay_manifest_all_fields', read('l122-full-count-replay.json'), c['expected_replay_manifest'])
        for replay in a['replays']:
            ck(replay['tag'] + '_accepted_exit', replay['returncode'], 0)
            ck(replay['tag'] + '_saved_replay_bytes',
               (BASE / replay['path']).read_bytes() == (BASE / (replay['tag'] + '-counts.txt')).read_bytes())

        preserved = set(expected_hashes) | {'ratio_spectral_bound.py', 'verify_ratio_spectral_bound.py',
                                          'ratio-spectral-bound.json', 'ratio-spectral-verification.json'}
        before = {name: sha(BASE / name) for name in sorted(preserved)}
        report['original_sha256'] = before
        ck('producer_hash', before['ratio_spectral_bound.py'], d['script_sha256'])
        ck('verifier_hash', before['verify_ratio_spectral_bound.py'], v['script_sha256'])
        ck('verified_certificate_hash', before['ratio-spectral-bound.json'], v['certificate_sha256'])

        # Execute reviewed code to separate destinations. Full object equality
        # includes schema, every diagnostic, every record and every check flag.
        fresh = module('ratio_spectral_bound').build(128)
        fresh_path = BASE / 'l124-audit-production-replay.json'
        fresh_path.write_text(json.dumps(fresh, indent=2) + '\n')
        ck('complete_production_replay', read(fresh_path.name), d)
        verify = module('verify_ratio_spectral_bound')
        verify.OUT = BASE / 'l124-audit-verification-replay.json'
        with contextlib.redirect_stdout(io.StringIO()):
            verify.main()
        ck('complete_verification_replay', read(verify.OUT.name), v)
        ck('production_check_count', len(d['checks']), 2386)
        ck('verification_check_count', len(v['checks']), 2355)

        n, k, T = 1024, 61, 2298250371072
        B = 2**128
        ck('precision_and_scale', [d['precision_bits'], d['scale']], [128, B])
        powers = [pow(19139, j, 65537) for j in range(n)]
        roots = {x for x in range(1, 65537) if pow(x, n, 65537) == 1}
        ck('entire_subgroup', set(powers) == roots and len(roots) == n)
        ck('cyclic_order', d['cyclic_order'], powers)
        rows = [list(map(int, row.split())) for row in (BASE / 'endpoint-pair-counts.txt').read_text().splitlines()]
        ck('row_shapes', len(rows) == 1023 and all(len(row) == 3 for row in rows))
        ck('row_labels', [row[0] for row in rows], powers[1:])
        counts = a['expected_complete_manifest']['counts']
        for x, same, different in rows:
            ck('ratio_' + str(x), {'same': same, 'different': different, 'total': same + different}, counts[str(x)])
        w = [0] + [row[1] + row[2] for row in rows]
        ck('all_weights', d['weights'], w)
        ck('inverse_symmetry_and_sign', all(w[j] == w[-j % n] and w[j] >= 0 for j in range(n)))
        s, rem = divmod(6*T, n)
        ck('singleton_normalization', [s, rem], [13466310768, 0])
        R = sum(w)
        ck('row_sum', R, 5*s)
        ck('parameters', d['parameters'], {'q': 65537, 'n': n, 'core': k, 'total': T,
                                         'singleton': s, 'generator': 19139, 'row_sum': R})

        ck('half_angle_count', len(d['half_angle_steps']), 8)
        root = [0, 0]
        for level, row in enumerate(d['half_angle_steps'], 1):
            lo, hi = row['root_interval']
            rad = [(B + r)*B for r in root]
            ck('root_record_' + str(level), row, {'level': level, 'input': root,
               'radicand_numerators': rad, 'root_interval': [lo, hi]})
            ck('root_inequalities_' + str(level), 0 <= lo <= hi <= B
               and 2*lo**2 <= rad[0] < 2*(lo+1)**2
               and 2*(hi-1)**2 < rad[1] <= 2*hi**2)
            root = [lo, hi]
        quad = [[B, B], root]
        ck('recurrence_count', len(d['cosine_recurrence']), 254)
        for r, row in enumerate(d['cosine_recurrence'], 2):
            if r % 2 == 0:
                aidx = bidx = r // 2
                sub = [B, B]
            else:
                aidx, bidx = (r+1)//2, (r-1)//2
                sub = root
            ck('prior_nonnegative_factors_' + str(r), aidx < r and bidx < r
               and 0 <= quad[aidx][0] <= quad[aidx][1] <= B
               and 0 <= quad[bidx][0] <= quad[bidx][1] <= B)
            raw = [(F(2*quad[aidx][0]*quad[bidx][0], B)-sub[1]).__floor__(),
                   (F(2*quad[aidx][1]*quad[bidx][1], B)-sub[0]).__ceil__()]
            enc = [max(0, raw[0]), min(B, raw[1])]
            ck('recurrence_record_' + str(r), row, {'r': r, 'a': aidx, 'b': bidx,
               'subtract': sub, 'raw': raw, 'enclosed': enc})
            ck('nonempty_intersection_' + str(r), 0 <= enc[0] <= enc[1] <= B)
            quad.append(enc)
        quad.append([0, 0])
        cs = d['cosine_intervals_scaled']
        ck('cosine_count', len(cs), n)
        # Four explicit quadrants, independently of min(r,n-r) reflection.
        for r, interval in enumerate(cs):
            if r <= 256:
                expected = quad[r]
            elif r <= 512:
                expected = [-quad[512-r][1], -quad[512-r][0]]
            elif r <= 768:
                expected = [-quad[r-512][1], -quad[r-512][0]]
            else:
                expected = quad[1024-r]
            ck('cosine_' + str(r), interval, expected)

        modes = []
        ck('mode_count', len(d['modes']), n)
        for m in range(n):
            # Pair j with -j, retaining the single self-inverse index 512.
            antipodal = w[512]*B*(-1 if m % 2 else 1)
            lo = antipodal + sum(2*w[j]*cs[(m*j) % n][0] for j in range(1, 512))
            hi = antipodal + sum(2*w[j]*cs[(m*j) % n][1] for j in range(1, 512))
            row = {'mode': m, 'lower_scaled': lo, 'upper_scaled': hi}
            ck('paired_mode_' + str(m), d['modes'][m], row)
            ck('mode_ordered_' + str(m), lo <= hi)
            modes.append(row)
        ck('constant_mode', modes[0], {'mode': 0, 'lower_scaled': R*B, 'upper_scaled': R*B})
        lower = max(row['lower_scaled'] for row in modes[1:])
        upper = max(row['upper_scaled'] for row in modes[1:])
        attaining = [row['mode'] for row in modes[1:] if row['upper_scaled'] == upper]
        ck('full_maximum', d['nonconstant_max'], {'lower_scaled': lower, 'upper_scaled': upper,
                                               'upper_attaining_modes': attaining})
        ck('claimed_negative_numerator', upper, -18018083607067510117209940640903437490413147824)
        ck('upper_attaining_modes', attaining, [426, 598])
        cw = max(hi-lo for lo, hi in cs)
        mw = max(row['upper_scaled']-row['lower_scaled'] for row in modes)
        ck('error_fields', d['error'], {'maximum_cosine_width_scaled': cw,
           'maximum_mode_width_scaled': mw, 'proved_uniform_width_scaled': R*cw})
        ck('claimed_widths', [cw, mw, R*cw], [97339, 3012990786359568, 6553986119231760])
        ck('uniform_width_below_two_to_minus_75', F(mw, B) <= F(R*cw, B) < F(1, 2**75))
        norm, constant = F(k*(n-k), n), F(R*k*k, n)
        ck('positive_norm', norm, F(58743, 1024))
        pair = (constant + F(upper, B)*norm)/2
        survivor = T-k*s+pair
        low_surv = T-k*s+(constant+F(lower, B)*norm)/2
        rat = lambda f: {'numerator': f.numerator, 'denominator': f.denominator}
        expected_bounds = {'centered_norm_squared': rat(norm), 'constant_quadratic': rat(constant),
           'pair_upper': rat(pair), 'pair_integer_upper': pair.__floor__(),
           'spectral_certificate_lower_endpoint': rat(low_surv), 'survivor_upper': rat(survivor),
           'survivor_integer_upper': survivor.__floor__(), 'baseline': 1600876449624,
           'required_pair_threshold': 1830*67798380,
           'integer_improvement': 1600876449624-survivor.__floor__()}
        ck('complete_rational_bounds', d['bounds'], expected_bounds)
        ck('claimed_pair_rational', rat(pair), {'numerator': 5262259384323702554445122878822311364591458658052163,
           'denominator': 43556142965880123323311949751266331066368})
        ck('pair_floor', pair.__floor__(), 120815550367)
        ck('survivor_floor', survivor.__floor__(), 1597620964591)
        ck('floor_commutes_with_integer_translation', survivor.__floor__(), T-k*s+pair.__floor__())
        ck('strict_improvement', survivor < 1600876449624 and d['verdict'] == 'strict_improvement')
        ck('originals_preserved', {name: sha(BASE / name) for name in before}, before)
        report.update({'complete': True, 'actual_survivor_upper': survivor.__floor__(),
            'required_strict_upper': 1600876449624, 'improvement': 1600876449624-survivor.__floor__(),
            'verified_counts': {'ratios': 1023, 'half_angles': 8, 'recurrences': 254,
                                'cosines': 1024, 'modes': 1024, 'nonconstant_modes': 1023},
            'fresh_artifacts': {p.name: sha(p) for p in [fresh_path, verify.OUT]},
            'qualification': 'Accepted finite diagnostic only; no sharpness, selected-family transfer or RS safety.'})
    except Exception as exc:
        failures.append(repr(exc))
    report['script_sha256'] = sha(Path(__file__))
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: report.get(key) for key in ['complete', 'failures', 'actual_survivor_upper',
          'required_strict_upper', 'improvement', 'verified_counts']} |
          {'checks': len(checks), 'certificate': str(OUT.relative_to(BASE.parent.parent))}))
    if not report['complete']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
