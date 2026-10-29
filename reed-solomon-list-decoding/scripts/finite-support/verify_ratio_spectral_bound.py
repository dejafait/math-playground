#!/usr/bin/env python3
"""Read and check all saved enclosure evidence, without calling the producer.

This is finite certificate verification, not the later independent critical
audit of the mathematics and implementation.
"""
import hashlib
import json
from fractions import Fraction
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / 'ratio-spectral-verification.json'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    checks = {}

    def ck(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise ValueError(name)

    try:
        p = BASE / 'ratio-spectral-bound.json'
        d = json.loads(p.read_text())
        ck('completion', d['complete'] and not d['failures'] and all(d['checks'].values()))
        ck('producer_hash', sha(BASE / 'ratio_spectral_bound.py') == d['script_sha256'])
        for name, expected in d['input_sha256'].items():
            ck('hash_' + name, sha(BASE / name) == expected)
        scale = d['scale']
        ck('precision', d['precision_bits'] in (128, 256) and scale == 2 ** d['precision_bits'])
        pms = d['parameters']
        n, k, total, single, R = (pms[a] for a in ['n', 'core', 'total', 'singleton', 'row_sum'])
        ck('fixed_parameters', (n, k, total, single, R) ==
           (1024, 61, 2298250371072, 13466310768, 67331553840))
        powers, w = d['cyclic_order'], d['weights']
        ck('cyclic_order', powers == [pow(19139, j, 65537) for j in range(n)]
           and len(set(powers)) == n)
        rows = [list(map(int, s.split())) for s in (BASE / 'endpoint-pair-counts.txt').read_text().splitlines()]
        ck('all_ratios_weights', len(rows) == 1023 and [r[0] for r in rows] == powers[1:]
           and w == [0] + [r[1] + r[2] for r in rows])
        ck('weight_properties', len(w) == n and min(w) >= 0 and sum(w) == R
           and all(w[j] == w[-j % n] for j in range(n)))
        root = [0, 0]
        ck('eight_half_angles', len(d['half_angle_steps']) == 8)
        for level, row in enumerate(d['half_angle_steps'], 1):
            lo, hi = row['root_interval']
            a, b = [(scale + v) * scale for v in root]
            ck('root_' + str(level), row['level'] == level and row['input'] == root
               and row['radicand_numerators'] == [a, b]
               and 0 <= lo <= hi <= scale
               and 2 * lo * lo <= a < 2 * (lo + 1) ** 2
               and 2 * (hi - 1) ** 2 < b <= 2 * hi * hi)
            root = [lo, hi]
        quad = [[scale, scale], root]
        ck('recurrence_completeness', len(d['cosine_recurrence']) == 254)
        for r, row in enumerate(d['cosine_recurrence'], 2):
            a, b = (r + 1) // 2, r // 2
            sub = [scale, scale] if r % 2 == 0 else root
            exactlo = Fraction(2 * quad[a][0] * quad[b][0], scale) - sub[1]
            exacthi = Fraction(2 * quad[a][1] * quad[b][1], scale) - sub[0]
            raw = [exactlo.__floor__(), exacthi.__ceil__()]
            enc = [max(0, raw[0]), min(scale, raw[1])]
            ck('recurrence_' + str(r), row == {'r': r, 'a': a, 'b': b, 'subtract': sub,
               'raw': raw, 'enclosed': enc} and 0 <= enc[0] <= enc[1] <= scale)
            quad.append(enc)
        quad.append([0, 0])
        cs = d['cosine_intervals_scaled']
        ck('cosine_table_length', len(cs) == n)
        for r in range(n):
            t = min(r, n - r)
            expected = quad[t] if t <= 256 else [-quad[512 - t][1], -quad[512 - t][0]]
            ck('cosine_' + str(r), cs[r] == expected)
        modes = d['modes']
        ck('mode_table_length', len(modes) == n)
        for m, row in enumerate(modes):
            # Group weights by angle residue, then evaluate the saved cosine table.
            buckets = [0] * n
            for j, v in enumerate(w):
                buckets[m * j % n] += v
            lo = sum(v * cs[t][0] for t, v in enumerate(buckets))
            hi = sum(v * cs[t][1] for t, v in enumerate(buckets))
            ck('mode_' + str(m), row == {'mode': m, 'lower_scaled': lo, 'upper_scaled': hi})
        ck('principal_mode', modes[0]['lower_scaled'] == modes[0]['upper_scaled'] == R * scale)
        lower = max(row['lower_scaled'] for row in modes[1:])
        upper = max(row['upper_scaled'] for row in modes[1:])
        ck('nonconstant_max', d['nonconstant_max'] == {'lower_scaled': lower, 'upper_scaled': upper,
           'upper_attaining_modes': [r['mode'] for r in modes[1:] if r['upper_scaled'] == upper]})
        width = max(b - a for a, b in cs)
        ck('error_bounds', d['error'] == {'maximum_cosine_width_scaled': width,
           'maximum_mode_width_scaled': max(r['upper_scaled'] - r['lower_scaled'] for r in modes),
           'proved_uniform_width_scaled': R * width}
           and all(r['upper_scaled'] - r['lower_scaled'] <= R * width for r in modes))
        norm, constant = Fraction(k * (n - k), n), Fraction(R * k * k, n)
        pair = (constant + Fraction(upper, scale) * norm) / 2
        low_surv = total - k * single + (constant + Fraction(lower, scale) * norm) / 2
        survivor = total - k * single + pair
        integer = survivor.__floor__()
        def rat(f):
            return {'numerator': f.numerator, 'denominator': f.denominator}
        expected_bounds = {'centered_norm_squared': rat(norm), 'constant_quadratic': rat(constant),
            'pair_upper': rat(pair), 'pair_integer_upper': pair.__floor__(),
            'spectral_certificate_lower_endpoint': rat(low_surv), 'survivor_upper': rat(survivor),
            'survivor_integer_upper': integer, 'baseline': 1600876449624,
            'required_pair_threshold': 1600876449624 - (total - k * single),
            'integer_improvement': 1600876449624 - integer}
        ck('all_exact_bounds', d['bounds'] == expected_bounds)
        ck('strict_comparison', survivor < 1600876449624 and d['verdict'] == 'strict_improvement')
        report = {'complete': True, 'failures': [], 'checks': checks,
                  'certificate_sha256': sha(p), 'script_sha256': sha(Path(__file__)),
                  'verified_half_angles': 8, 'verified_recurrences': 254,
                  'verified_cosines': n, 'verified_modes': n, 'verified_nonconstant_modes': n - 1,
                  'actual_survivor_upper': integer, 'required_strict_upper': 1600876449624,
                  'improvement': 1600876449624 - integer}
    except Exception as exc:
        report = {'complete': False, 'failures': [repr(exc)], 'checks': checks}
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({a: v for a, v in report.items() if a not in ['checks', 'script_sha256', 'certificate_sha256']} |
                     {'check_count': len(checks), 'certificate': str(OUT.relative_to(BASE.parent.parent))}))
    if not report['complete']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
