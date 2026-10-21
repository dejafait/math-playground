"""Exact bounded arithmetic and small-case checks for L099; no fiber search on H."""
from collections import defaultdict
from itertools import combinations, product
from math import comb, prod
from pathlib import Path
import json


def root_product(roots, p):
    out = [1]
    for r in roots:
        nxt = [0] * (len(out) + 1)
        for j, v in enumerate(out):
            nxt[j] = (nxt[j] - r * v) % p
            nxt[j + 1] = (nxt[j + 1] + v) % p
        out = nxt
    return out


def evaluate(coeffs, x, p):
    out = 0
    for v in reversed(coeffs):
        out = (out * x + v) % p
    return out


def main():
    checks, failures = 0, []

    def check(label, ok):
        nonlocal checks
        checks += 1
        if not ok:
            failures.append(label)

    Q, n, k, agreement = 65537, 1024, 64, 67
    numerator = comb(n, agreement)
    # Independent Pascal recursion, retaining just the required degree.
    row = [1] + [0] * agreement
    for i in range(1, n + 1):
        for j in range(min(i, agreement), 0, -1):
            row[j] += row[j - 1]
    check('complete Pascal reconstruction', row[agreement] == numerator)
    check('factorial product reconstruction',
          numerator * prod(range(1, agreement + 1)) == prod(range(n-agreement+1, n+1)))
    classes = n * Q**2
    lower, remainder = divmod(numerator, classes)
    lower += bool(remainder)
    ambient, denominator = Q**28, 2**128
    scaled_lower = lower * denominator
    check('exact ceiling lower endpoint', (lower-1)*classes < numerator)
    check('exact ceiling upper endpoint', numerator <= lower*classes)
    check('strict threshold failure', scaled_lower < ambient)
    check('lower positive', lower > 0)
    scale = 10**9
    ratio_floor = scaled_lower * scale // ambient
    check('ratio interval lower', ratio_floor * ambient <= scale * scaled_lower)
    check('ratio interval upper', scale * scaled_lower < (ratio_floor+1) * ambient)
    # The full Hayes class count is larger; the subgroup restriction is retained.
    check('Hayes subgroup index', (Q-1)*Q**2 == 64*classes)
    check('minus one in H', pow(19139, 512, Q) == Q-1)

    # Independent scalar enumeration on an order-eight proper subgroup of F_17.
    # This is a sanity check; the large-instance proof is symbolic.
    p, small_n, small_k = 17, 8, 2
    H = sorted({pow(9, i, p) for i in range(small_n)})
    A = small_k + 3
    check('small subgroup', len(H) == small_n and p-1 in H)
    fibers, messages = defaultdict(list), {}
    for roots in combinations(H, A):
        g = root_product(roots, p)
        a, b, c = g[2], g[1], g[0]
        label = (a, b, c)
        check('small constant sign', c == -prod(roots) % p and c in H)
        inverses = [pow(x, -1, p) for x in roots]
        u = sum(inverses) % p
        v = sum(x*y for x, y in combinations(inverses, 2)) % p
        check('small first ending coefficient', b == -c*u % p)
        check('small second ending coefficient', a == c*v % p)
        numerator_coeffs = [0] * (A+1)
        numerator_coeffs[0:3] = [c, b, a]
        numerator_coeffs[A] = 1
        delta = [(v-w) % p for v, w in zip(numerator_coeffs, g)]
        check('small three cancellations', delta[:3] == [0, 0, 0])
        check('small monic cancellation', delta[A] == 0)
        message = tuple(delta[3:A])
        check('small strict message degree', len(message) == small_k)
        center = [(pow(x, A, p)+a*x*x+b*x+c)*pow(x**3, -1, p) % p for x in H]
        actual = tuple(x for x, y in zip(H, center) if evaluate(message, x, p) == y)
        check('small exact support', actual == roots)
        fibers[label].append((roots, message))
        messages[roots] = message
    # Inspect every occupied center, one empty admissible center and one
    # outside-H constant. Enumerate every scalar message at each such center.
    empty = next(z for z in product(range(p), range(p), H) if z not in fibers)
    outside = next(c for c in range(1, p) if c not in H)
    centers = sorted(fibers) + [empty, (0, 0, outside)]
    all_messages = list(product(range(p), repeat=small_k))
    full_lists = []
    for a, b, c in centers:
        center = [(pow(x, A, p)+a*x*x+b*x+c)*pow(x**3, -1, p) % p for x in H]
        actual = []
        for message in all_messages:
            support = tuple(x for x, y in zip(H, center) if evaluate(message, x, p) == y)
            if len(support) >= A:
                actual.append((support, message))
        expected = fibers.get((a, b, c), [])
        check('small exhaustive full list', sorted(actual) == sorted(expected))
        check('small distinct evaluations', len({m for _, m in expected}) == len(expected))
        full_lists.append({'label': [a, b, c], 'candidates': [
            {'support': list(s), 'message': list(m)} for s, m in actual]})
    result = {
        'target': 'L099 order-three pole dictionary and bounded class average',
        'fixed': {'Q': Q, 'n': n, 'k': k, 'agreements': agreement,
                  'binomial': numerator, 'class_count': classes,
                  'full_Hayes_class_count': (Q-1)*Q**2,
                  'ceiling_lower': lower, 'threshold_numerator': ambient,
                  'threshold_denominator': denominator,
                  'positive_threshold_minus_lower_scaled': ambient-scaled_lower,
                  'ratio_interval': {'lower_numerator': ratio_floor,
                                     'upper_numerator': ratio_floor+1, 'denominator': scale},
                  'strictly_exceeds_threshold': scaled_lower > ambient},
        'small': {'p': p, 'H': H, 'k': small_k, 'agreements': A,
                  'subset_count': len(messages), 'occupied_centers': len(fibers),
                  'tested_centers': len(centers), 'all_message_count_per_center': len(all_messages),
                  'full_lists': full_lists},
        'checks': checks, 'failures': failures,
        'limitations': ['No large-domain fiber enumeration or maximum estimate.',
                        'No extension-field enumeration; completeness is symbolic.',
                        'Failure of this lower certificate gives no safety bound.']}
    path = Path(__file__).with_name('order-three-pole-results.json')
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(f'checks={checks}; failures={len(failures)}; certificate={path.as_posix()}')
    print(f'actual/required lower certificate: [{ratio_floor},{ratio_floor+1})/10^9; required >1')
    print(f'class count={classes}; small subsets={len(messages)}; tested centers={len(centers)}')
    print('Large-fiber maximum, RS safety and boundary improvement: not established.')
    if failures:
        print('Failures:', ', '.join(failures))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
