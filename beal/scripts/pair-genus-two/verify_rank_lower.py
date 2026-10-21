"""Independent finite-box replay: factor-form points, quadratic in b1^2.

Does not import rank_lower.py. The alternate elimination checks absence
of quadratic divisors without repeating its slope enumeration.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
raw = (HERE/'rank-lower-certificate.json').read_bytes()
cert = json.loads(raw)
f = [-308, -2288, 341, 3388, 1034, -704, -275]
checks = {}


def check(name, ok):
    checks[name] = bool(ok)


points, point_count = [], 0
for m in range(-500, 501):
    for n in range(1, 501):
        if gcd(m, n) != 1:
            continue
        point_count += 1
        h = 11*(m*m-4*n*n)*(7*n**4+52*m*n**3-6*m*m*n*n-64*m**3*n-25*m**4)
        if h >= 0 and isqrt(h)**2 == h:
            for w in sorted(set([isqrt(h), -isqrt(h)])):
                points.append((m, n, w))
check('all_point_hits', sorted(points) == sorted((v['m'], v['n'], v['W_numerator']) for v in cert['points']))
check('point_count', point_count == cert['search']['point_tests'] == 304463)

records, divisor_hits = [], []
counts = {'repeated': 0, 'branch': 0, 'eligible_pairs': 0,
          'negative_discriminant': 0, 'nonsquare_discriminant': 0,
          'integer_square_k_outside_cap': 0}
for a0 in range(-25, 26):
    for a1 in range(-25, 26):
        A = a1*a1-4*a0
        if A == 0:
            counts['repeated'] += 1
            continue
        # Compute T^i residues first, then a dot product with f.
        powers = [(1, 0), (0, 1)]
        for i in range(2, 7):
            u, v = powers[-1]
            powers.append((-a0*v, u-a1*v))
        r0 = sum(v*powers[i][0] for i, v in enumerate(f))
        r1 = sum(v*powers[i][1] for i, v in enumerate(f))
        branch = (r1 == 0 and r0 == 0) or (r1 != 0 and r0*r0-a1*r0*r1+a0*r1*r1 == 0)
        if branch:
            counts['branch'] += 1
            continue
        counts['eligible_pairs'] += 1
        # Necessary and sufficient for b1 != 0, with k=b1^2:
        # A k^2 + (2 a1 r1 - 4 r0) k + r1^2 = 0.
        B, C = 2*a1*r1-4*r0, r1*r1
        discriminant = B*B-4*A*C
        candidates = []
        if discriminant < 0:
            counts['negative_discriminant'] += 1
        elif isqrt(discriminant)**2 != discriminant:
            counts['nonsquare_discriminant'] += 1
        else:
            root = isqrt(discriminant)
            for k in sorted(set([Q(-B+root, 2*A), Q(-B-root, 2*A)])):
                if k > 0 and k.denominator == 1 and isqrt(k.numerator)**2 == k:
                    candidates.append([k.numerator, k.denominator])
                    b1 = isqrt(k.numerator)
                    if b1 <= 500:
                        for b in (b1, -b1):
                            b0 = Q(r1+a1*b*b, 2*b)
                            divisor_hits.append([a0, a1, b, b0.numerator, b0.denominator])
                    else:
                        counts['integer_square_k_outside_cap'] += 1
        if r1 == 0 and r0 >= 0 and isqrt(r0)**2 == r0:
            for b0 in sorted(set([isqrt(r0), -isqrt(r0)])):
                divisor_hits.append([a0, a1, 0, b0, 1])
        records.append({'a0': a0, 'a1': a1, 'remainder': [r0, r1],
                        'equation_in_k': [C, B, A], 'discriminant': discriminant,
                        'positive_integral_square_k': candidates})
check('no_divisor_hits', not divisor_hits and cert['quadratic_divisors'] == [])
check('eligible_count', counts['eligible_pairs']*1001 == cert['search']['quadratic_b1_tests'])
check('all_quadratic_pairs', counts['eligible_pairs']+counts['repeated']+counts['branch'] == 2601)
check('repeated_rejections', counts['repeated'] == cert['search']['rejections']['quadratic_repeated_roots'])
check('branch_rejections', counts['branch'] == cert['search']['rejections']['quadratic_meets_branch'])
check('no_columns', cert['columns'] == [] and all(row == [] for row in cert['matrix']))
check('zero_detector_rank', cert['summary']['d'] == 0 and cert['pivots'] == [] and cert['row_operations'] == [])

report = {'input_sha256': sha256(raw).hexdigest(), 'point_tests': point_count,
          'point_hits': points, 'quadratic_counts': counts,
          'quadratic_elimination': records, 'divisor_hits': divisor_hits,
          'checks': checks, 'failures': [k for k, v in checks.items() if not v]}
out = HERE/'rank-lower-search-replay.json'
out.write_text(json.dumps(report, indent=2)+'\n')
print('Independent search replay:', len(checks), 'checks; failures:', report['failures'])
print('Points:', points, '; quadratic hits:', divisor_hits)
print('Quadratic counts:', counts)
print('Full certificate:', out.relative_to(HERE.parent.parent))
if report['failures']:
    raise SystemExit(1)
