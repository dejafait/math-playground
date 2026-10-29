#!/usr/bin/env python3
"""Exact dyadic enclosure of L123's finite circulant; no float arithmetic."""
import hashlib
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / 'ratio-spectral-bound.json'
N, QFIELD, CORE, TOTAL = 1024, 65537, 61, 2298250371072
BASELINE = 1600876449624


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def ceildiv(a, b):
    return -((-a) // b)


def rat(x):
    return {'numerator': x.numerator, 'denominator': x.denominator}


def build(bits):
    scale = 1 << bits
    checks, hashes = {}, {}

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise ValueError(name)

    audit = json.loads((BASE / 'l123-critical-audit.json').read_text())
    caudit = json.loads((BASE / 'c122a-critical-audit.json').read_text())
    data = json.loads((BASE / 'endpoint-pair-count.json').read_text())
    for name, a in [('l123', audit), ('c122a', caudit)]:
        check(name + '_accepted_completion', a['complete'] and not a['failures'])
        check(name + '_all_audit_checks', all(c['ok'] for c in a['checks']))
        script = 'critical_audit_' + name + '.py'
        hashes[script] = digest(BASE / script)
        check(name + '_audit_script_hash', hashes[script] == a['script_sha256'])
        for p, expected in a['original_sha256'].items():
            hashes[p] = digest(BASE / p)
            check(name + '_hash_' + p, hashes[p] == expected)
    for p, expected in caudit['fresh_artifacts'].items():
        hashes[p] = digest(BASE / p)
        check('c122a_fresh_hash_' + p, hashes[p] == expected)
    for p in ['l123-critical-audit.json', 'c122a-critical-audit.json']:
        hashes[p] = digest(BASE / p)
    check('l123_full_manifest_match', data == audit['expected_complete_manifest'])
    for p, key in [('l122-full-count.json', 'expected_production_manifest'),
                   ('l122-full-count-replay.json', 'expected_replay_manifest')]:
        check(p + '_full_manifest_match', json.loads((BASE / p).read_text()) == caudit[key])
    check('production_complete', data['complete'] and not data['failures'])
    check('parameters', (data['q'], data['n'], data['ordered_count']) == (QFIELD, N, TOTAL))
    check('old_threshold', data['deletion']['bonferroni_upper'] == BASELINE)

    h = pow(3, 64, QFIELD)
    powers = [pow(h, j, QFIELD) for j in range(N)]
    check('generator_order', h == 19139 and pow(h, N, QFIELD) == 1
          and pow(h, N // 2, QFIELD) == QFIELD - 1)
    check('cyclic_distinct', len(set(powers)) == N and powers[0] == 1)
    roots = {a for a in range(1, QFIELD) if pow(a, N, QFIELD) == 1}
    check('all_subgroup_roots', set(powers) == roots)
    for j in range(N):
        check('cyclic_step_' + str(j), powers[(j + 1) % N] == h * powers[j] % QFIELD)
    rows = [tuple(map(int, line.split())) for line in
            (BASE / 'endpoint-pair-counts.txt').read_text().splitlines()]
    check('ratio_row_lengths', all(len(row) == 3 for row in rows))
    check('all_1023_ratios_once', len(rows) == N - 1
          and len({r[0] for r in rows}) == N - 1
          and {r[0] for r in rows} == roots - {1})
    check('cyclic_ratio_order', [r[0] for r in rows] == powers[1:])
    counts = {str(a): {'same': s, 'different': d, 'total': s + d}
              for a, s, d in rows}
    check('every_ratio_manifest_match', counts == data['counts'])
    weights = [0] + [s + d for _, s, d in rows]
    check('nonnegative_zero_diagonal', weights[0] == 0 and min(weights) >= 0)
    check('every_inverse_symmetry', all(weights[j] == weights[-j % N] for j in range(N)))
    row_sum = sum(weights)
    singleton = 6 * TOTAL // N
    check('singleton_integer', 6 * TOTAL % N == 0 and singleton == data['singleton'])
    check('row_sum', row_sum == 5 * singleton == 67331553840)
    check('antipodal', powers[N // 2] == QFIELD - 1
          and weights[N // 2] == data['maximum'] == 67798380)

    # Positive half-angle square roots; each integer inequality is saved.
    half, c = [], (0, 0)
    for level in range(1, 9):
        lo_rad = (scale + c[0]) * scale
        hi_rad = (scale + c[1]) * scale
        lo = isqrt(lo_rad // 2)
        hi = isqrt(hi_rad // 2)
        if 2 * hi * hi < hi_rad:
            hi += 1
        check('root_lower_' + str(level), 2 * lo * lo <= lo_rad < 2 * (lo + 1) ** 2)
        check('root_upper_' + str(level), 2 * (hi - 1) ** 2 < hi_rad <= 2 * hi * hi)
        check('root_quadrant_' + str(level), 0 <= lo <= hi <= scale)
        half.append({'level': level, 'input': list(c), 'radicand_numerators': [lo_rad, hi_rad],
                     'root_interval': [lo, hi]})
        c = (lo, hi)

    quadrant = [(scale, scale), c]
    recurrence = []
    for r in range(2, N // 4):
        a, b = (r + 1) // 2, r // 2
        subtract = (scale, scale) if a == b else c
        raw = (2 * quadrant[a][0] * quadrant[b][0] // scale - subtract[1],
               ceildiv(2 * quadrant[a][1] * quadrant[b][1], scale) - subtract[0])
        enclosed = (max(0, raw[0]), min(scale, raw[1]))
        check('quadrant_valid_' + str(r), 0 <= enclosed[0] <= enclosed[1] <= scale)
        quadrant.append(enclosed)
        recurrence.append({'r': r, 'a': a, 'b': b, 'subtract': list(subtract),
                           'raw': list(raw), 'enclosed': list(enclosed)})
    quadrant.append((0, 0))  # cos(pi/2), exact endpoint

    cosines = []
    for r in range(N):
        t = min(r, N - r)
        if t <= N // 4:
            v = quadrant[t]
        else:
            lo, hi = quadrant[N // 2 - t]
            v = (-hi, -lo)
        cosines.append(v)
    check('cosine_completeness', len(cosines) == N)
    check('cosine_symmetry', all(cosines[r] == cosines[-r % N] for r in range(N)))
    check('real_antipodal_cosine', cosines[N // 2] == (-scale, -scale))

    modes = []
    for m in range(N):
        low = sum(weights[j] * cosines[m * j % N][0] for j in range(N))
        high = sum(weights[j] * cosines[m * j % N][1] for j in range(N))
        check('mode_interval_' + str(m), low <= high)
        modes.append({'mode': m, 'lower_scaled': low, 'upper_scaled': high})
    check('constant_mode', modes[0]['lower_scaled'] == modes[0]['upper_scaled'] == row_sum * scale)
    check('all_modes_retained', [r['mode'] for r in modes] == list(range(N)))
    check('repeated_modes_retained', all(modes[m]['lower_scaled'] == modes[-m % N]['lower_scaled']
          and modes[m]['upper_scaled'] == modes[-m % N]['upper_scaled'] for m in range(N)))
    lower_max = max(r['lower_scaled'] for r in modes[1:])
    upper_max = max(r['upper_scaled'] for r in modes[1:])
    maximizing = [r['mode'] for r in modes[1:] if r['upper_scaled'] == upper_max]
    maximum_cosine_width = max(b - a for a, b in cosines)
    check('all_mode_width_bounds', all(r['upper_scaled'] - r['lower_scaled']
          <= row_sum * maximum_cosine_width for r in modes))
    check('norm_positive', CORE * (N - CORE) > 0)
    norm2 = Fraction(CORE * (N - CORE), N)
    constant = Fraction(row_sum * CORE * CORE, N)
    pair_lower_endpoint = (constant + Fraction(lower_max, scale) * norm2) / 2
    pair_upper = (constant + Fraction(upper_max, scale) * norm2) / 2
    # pair_lower_endpoint is a LOWER ENCLOSURE OF THE SPECTRAL CERTIFICATE,
    # never a lower bound on the pair energy of any core.
    survivor_lower_endpoint = TOTAL - CORE * singleton + pair_lower_endpoint
    survivor_upper = TOTAL - CORE * singleton + pair_upper
    pair_integer_upper = pair_upper.numerator // pair_upper.denominator
    survivor_integer_upper = TOTAL - CORE * singleton + pair_integer_upper
    threshold_pairs = BASELINE - (TOTAL - CORE * singleton)
    verdict = ('strict_improvement' if survivor_upper < BASELINE else
               'no_improvement' if survivor_lower_endpoint >= BASELINE else 'rounding_straddle')
    return {'complete': True, 'failures': [], 'checks': checks,
            'precision_bits': bits, 'scale': scale, 'input_sha256': hashes,
            'script_sha256': digest(Path(__file__)),
            'parameters': {'q': QFIELD, 'n': N, 'core': CORE, 'total': TOTAL,
                           'singleton': singleton, 'generator': h, 'row_sum': row_sum},
            'cyclic_order': powers, 'weights': weights,
            'half_angle_steps': half, 'cosine_recurrence': recurrence,
            'cosine_intervals_scaled': cosines, 'modes': modes,
            'nonconstant_max': {'lower_scaled': lower_max, 'upper_scaled': upper_max,
                                'upper_attaining_modes': maximizing},
            'error': {'maximum_cosine_width_scaled': maximum_cosine_width,
                      'maximum_mode_width_scaled': max(r['upper_scaled'] - r['lower_scaled'] for r in modes),
                      'proved_uniform_width_scaled': row_sum * maximum_cosine_width},
            'bounds': {'centered_norm_squared': rat(norm2), 'constant_quadratic': rat(constant),
                       'pair_upper': rat(pair_upper), 'pair_integer_upper': pair_integer_upper,
                       'spectral_certificate_lower_endpoint': rat(survivor_lower_endpoint),
                       'survivor_upper': rat(survivor_upper),
                       'survivor_integer_upper': survivor_integer_upper,
                       'baseline': BASELINE, 'required_pair_threshold': threshold_pairs,
                       'integer_improvement': BASELINE - survivor_integer_upper},
            'verdict': verdict,
            'qualification': 'Uniform upper diagnostic only; no core attainment, selected-family transfer or RS safety.'}


def main():
    try:
        result = build(128)
        if result['verdict'] == 'rounding_straddle':
            result = build(256)
        OUT.write_text(json.dumps(result, indent=2) + '\n')
        # Read the complete saved artifact; compare all fields, not a preview.
        assert json.loads(OUT.read_text()) == json.loads(json.dumps(result))
        b = result['bounds']
        print(json.dumps({'complete': result['complete'], 'checks': len(result['checks']),
                          'failures': result['failures'], 'precision_bits': result['precision_bits'],
                          'verdict': result['verdict'], 'actual_survivor_upper': b['survivor_integer_upper'],
                          'required_strict_upper': b['baseline'], 'improvement': b['integer_improvement'],
                          'max_modes': result['nonconstant_max']['upper_attaining_modes'],
                          'certificate': str(OUT.relative_to(BASE.parent.parent))}))
    except Exception as exc:
        OUT.write_text(json.dumps({'complete': False, 'failures': [repr(exc)]}, indent=2) + '\n')
        print(json.dumps({'complete': False, 'failures': [repr(exc)], 'certificate': str(OUT)}))
        raise


if __name__ == '__main__':
    main()
