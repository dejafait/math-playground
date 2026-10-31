"""Audit only the two existing L530 endpoints; no project math imports/search."""
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import json


def clean(a):
    a = list(a)
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def plus(a, b):
    n = max(len(a), len(b))
    return clean([(a[k] if k < len(a) else Q(0)) +
                  (b[k] if k < len(b) else Q(0)) for k in range(n)])


def times(a, c):
    return clean([c*x for x in a])


def divmod_poly(a, b):
    a, b = clean(a), clean(b)
    assert b != [0]
    quotient = [Q(0)] * max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        k = len(a)-len(b)
        c = a[-1]/b[-1]
        quotient[k] += c
        a = plus(a, [Q(0)]*k + times(b, -c))
    return clean(quotient), a


def determinant(matrix):
    # Leibniz determinant: just 5! terms, separate from discriminant formula.
    total = Q(0)
    n = len(matrix)
    for p in permutations(range(n)):
        term = Q((-1)**sum(p[i] > p[j] for i in range(n) for j in range(i+1, n)))
        for i in range(n):
            term *= matrix[i][p[i]]
        total += term
    return total


def sign(x):
    return (x > 0)-(x < 0)


def variations(values):
    v = [x for x in values if x]
    return sum(v[k] != v[k+1] for k in range(len(v)-1))


def strings(p):
    return [str(x) for x in p]


def main():
    folder = Path(__file__).parent
    data = json.loads((folder / 'collision-certificate.json').read_text())
    failures, checks, records = [], [], []

    def check(name, condition):
        checks.append(dict(check=name, passed=bool(condition)))
        if not condition:
            failures.append(name)

    q, u, v = Q(12, 25), Q(0), Q(1)
    moments = [(1-q)*u**j + q*v**j for j in range(4)]
    check('zero-atom convention and all moments', moments == [1, q, q, q])
    check('certificate parameters', all(Q(data['parameters'][key]) == val
          for key, val in dict(q=q, u=u, v=v, m1=q, m2=q, m3=q).items()))
    radii = [Q(9, 32), Q(1, 3)]
    check('ordered outward radii', 0 < radii[0] < radii[1] <= 1)
    check('exactly two endpoint records', len(data['endpoints']) == 2)

    # Romik Table A.1, independently transcribed in x, degrees 0 through 6.
    table = [[Q(1)], [Q(0), Q(2)], [Q(-3,4), Q(0), Q(2)],
             [Q(0), Q(-13,6), Q(0), Q(4,3)],
             [Q(21,32), Q(0), Q(-17,6), Q(0), Q(2,3)],
             [Q(0), Q(177,80), Q(0), Q(-7,3), Q(0), Q(4,15)],
             [Q(-77,128), Q(0), Q(2401,720), Q(0), Q(-25,18), Q(0), Q(4,45)]]
    basis = [[c/Q(2)**k for k,c in enumerate(row)] for row in table]
    for n in range(1,6):
        residual = plus(plus(times(basis[n+1], n+1),
                            times([Q(0)]+basis[n], -1)),
                        times(basis[n-1], Q(2*n+1,2)))
        check(f'table versus recurrence n={n}', residual == [0])

    scales = [Q(4294967296000), Q(8748000)]
    expected_ints = [[4426352279635, -91525040694, 626050620, -1417176],
                     [9135405, -274802, 2660, -8]]
    expected_delta = [1593895952528326541214254588811264, -112042936313856]
    for idx, (record, radius) in enumerate(zip(data['endpoints'], radii)):
        prefix = f'endpoint {idx}: '
        check(prefix+'radius', Q(record['radius']) == radius)
        pt = [Q(0)]
        for j in range(4):
            pt = plus(pt, times(basis[2*j], (-1)**j*moments[j]*radius**(2*j)))
        check(prefix+'even degree six', len(pt) == 7 and pt[-1] != 0
              and all(pt[k] == 0 for k in [1,3,5]))
        cubic = pt[::2]
        s = radius**2
        A, B, C = [moments[j]*s**j for j in range(1,4)]
        formula = [1+3*A/4+21*B/32+77*C/128,
                   -A/2-17*B/24-2401*C/2880,
                   B/24+25*C/288, -C/720]
        check(prefix+'all four displayed coefficient identities', cubic == formula)
        scale = Q(record['positive_scale_from_original'])
        integers = [Q(x) for x in record['integer_coefficients_ascending']]
        check(prefix+'positive scale and every integer coefficient',
              scale == scales[idx] and scale > 0 and
              times(cubic, scale) == integers == list(map(Q, expected_ints[idx])))
        check(prefix+'strict signs exclude z<=0',
              all((-1)**k*c > 0 for k,c in enumerate(integers)))
        d,c,b,a = integers
        delta = b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d
        derivative = [c, 2*b, 3*a]
        sylvester = [[a,b,c,d,0], [0,a,b,c,d],
                     [3*a,2*b,c,0,0], [0,3*a,2*b,c,0], [0,0,3*a,2*b,c]]
        resultant = determinant(sylvester)
        check(prefix+'complete discriminant via formula and Sylvester determinant',
              delta == -resultant/a == expected_delta[idx] == Q(record['integer_discriminant']))
        check(prefix+'original discriminant and scaling power four',
              delta/scale**4 == Q(record['original_discriminant']))
        chain = [[Q(x) for x in row] for row in record['sturm_chain']]
        check(prefix+'full initial Sturm rows',
              len(chain) == 4 and chain[0] == integers and chain[1] == derivative)
        divisions = []
        for k in range(2, len(chain)):
            quotient, remainder = divmod_poly(chain[k-2], chain[k-1])
            negative = times(remainder, -1)
            factor = chain[k][-1]/negative[-1]
            check(prefix+f'complete Sturm row {k} positive rescaled negative remainder',
                  negative != [0] and factor > 0 and times(negative, factor) == chain[k])
            divisions.append(dict(quotient=strings(quotient),
                                  negative_remainder=strings(negative),
                                  positive_normalization=str(factor),
                                  normalized_row=strings(chain[k])))
        terminal_quotient, terminal_remainder = divmod_poly(chain[-2], chain[-1])
        check(prefix+'nonzero constant gcd and terminal zero remainder',
              len(chain[-1]) == 1 and chain[-1][0] != 0 and terminal_remainder == [0])
        zero_signs = [sign(row[0]) for row in chain]
        infinity_signs = [sign(row[-1]) for row in chain]
        count = variations(zero_signs)-variations(infinity_signs)
        check(prefix+'every endpoint sign and variation',
              zero_signs == record['signs_at_zero'] and
              infinity_signs == record['signs_at_positive_infinity'] and
              count == record['positive_distinct_roots'] == [3,1][idx])
        check(prefix+'Sturm/discriminant and recorded simplicity/root count',
              sign(delta) == [1,-1][idx] and record['squarefree'] is True and
              2*count == record['real_t_roots'] == [6,2][idx])
        alpha = -Q(720)/(q*radii[0]**6)
        check(prefix+'flow monic leading coefficient identity',
              alpha*cubic[-1] == (radius/radii[0])**6)
        records.append(dict(radius=str(radius), cubic=strings(cubic),
                            integer_coefficients=strings(integers), positive_scale=str(scale),
                            discriminant=str(delta), resultant=str(resultant),
                            full_sturm_chain=[strings(row) for row in chain],
                            sturm_divisions=divisions, terminal_quotient=strings(terminal_quotient),
                            terminal_remainder=strings(terminal_remainder),
                            zero_signs=zero_signs, infinity_signs=infinity_signs,
                            variations=[variations(zero_signs),variations(infinity_signs)],
                            positive_simple_z_roots=count, real_simple_t_roots=2*count,
                            nonreal_simple_t_roots=6-2*count))
    report = dict(result='PASS' if not failures else 'FAIL', checks=checks,
                  endpoints=records, failures=failures,
                  actual_endpoints=len(records), required_endpoints=2,
                  additional_samples=0, required_maximum_additional_samples=0,
                  flow=dict(initial_monic_scalar=str(-Q(720)/(q*radii[0]**6)),
                            final_radius_ratio=str(radii[1]/radii[0]),
                            time_relation='sigma=-log(r/r0)<0 at r=r1'),
                  limitation='Only the fixed finite moment family; no actual-theta or RH transfer.')
    dest = folder/'l530-independent-audit.json'
    dest.write_text(json.dumps(report, indent=2)+'\n')
    print(report['result'], '; exact checks:', len(checks), '; failures:', failures)
    print('Endpoint records:', len(records), '; required: 2; real simple t roots:',
          [r['real_simple_t_roots'] for r in records], '; certificate required: [6, 2]')
    print('Preservation would require [6, 6]; additional samples: 0; required maximum: 0')
    print('Certificate:', dest)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
