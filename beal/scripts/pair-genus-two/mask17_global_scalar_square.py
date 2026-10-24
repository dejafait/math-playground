#!/usr/bin/env python3
"""Exact positive identity certificate; no factor irreducibility is needed."""
from fractions import Fraction as Q
from pathlib import Path
import json


def trim(a):
    a = list(map(Q, a))
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a or [Q(0)]


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([x*c for x in a])


def mul(a, b):
    out = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def divmod_poly(a, b):
    a, b = trim(a), trim(b)
    assert b != [0]
    q = [Q(0)]*max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        k, c = len(a)-len(b), a[-1]/b[-1]
        q[k] += c
        a = add(a, [Q(0)]*k+scale(b, -c))
    return trim(q), a


def inverse(a, modulus):
    r0, r1, s0, s1 = modulus, a, [Q(0)], [Q(1)]
    while r1 != [0]:
        q, r = divmod_poly(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, add(s0, scale(mul(q, s1), -1))
    assert len(r0) == 1 and r0[0]
    return divmod_poly(scale(s0, 1/r0[0]), modulus)[1]


def encode(a):
    return [str(x) for x in a]


def main():
    f = list(map(Q, [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]))
    quartic = list(map(Q, [243, -3564, 6930, -2860, 275]))
    mod = lambda a: divmod_poly(a, f)[1]
    u = [Q(0), Q(0), Q(1)]
    v = mod(add([1], scale(inverse(u, f), -9)))
    # Q(v)=0 and Q(-Y^2/11)*11^4 = H(Y) H(-Y).
    qv = [Q(1024), Q(4352), Q(1920), Q(128), Q(1)]
    hfactor = list(map(Q, [-3872, -1936, 264, 44, 1]))
    opposite = [a*(-1)**i for i, a in enumerate(hfactor)]
    c = Q(-11)
    norm_poly = [Q(0)]*9
    for i, a in enumerate(qv):
        norm_poly[2*i] = a*c**(4-i)
    # H(Y)=E(v)+Y*D(v) modulo Y^2=-11v.
    even = mod(add(add(scale(mul(v, v), c*c), scale(v, 264*c)), [-3872]))
    denominator = mod(add(scale(v, 44*c), [-1936]))
    denom_inv = inverse(denominator, f)
    y = mod(scale(mul(even, denom_inv), -1))
    h = mod(scale(mul([0, 1], y), Q(1, 11)))
    delta = list(map(Q, [-9, 0, 1]))
    identity_numerator = add(scale(mul(h, h), -11), scale(delta, -1))
    quotient, remainder = divmod_poly(identity_numerator, f)
    v_relation = [Q(0)]
    for coefficient in reversed(qv):
        v_relation = mod(add(mul(v_relation, v), [coefficient]))
    checks = []
    def check(name, actual, required):
        checks.append(dict(name=name, actual=encode(actual),
                           required=encode(required), passed=actual == required))
    check('complete factor product', mul(hfactor, opposite), norm_poly)
    check('quartic relation in entire field', v_relation, [Q(0)])
    check('denominator inverse in entire field', mod(mul(denominator, denom_inv)), [Q(1)])
    check('square-root identity in entire field', mod(add(mul(y, y), scale(v, 11))), [Q(0)])
    check('final exact remainder', remainder, [Q(0)])
    check('full unreduced polynomial identity', identity_numerator, mul(quotient, f))
    failures = [r['name'] for r in checks if not r['passed']]
    record = dict(
        target='theta^2-9 = -11*h(theta)^2 in Q[theta]/(F)',
        classification='REPRODUCTION; positive certificate only',
        polynomial_convention='ascending rational coefficient vectors',
        F=encode(f), quartic_u=encode(quartic), Q_v=encode(qv),
        discovery=dict(scalar=-11, H=encode(hfactor), H_negative=encode(opposite),
                       factor_product=encode(norm_poly),
                       method='bounded integral quartic-factor coefficient search; no negative inference'),
        v=encode(v), even_part=encode(even), denominator=encode(denominator),
        denominator_inverse=encode(denom_inv), y=encode(y), h=encode(h),
        scalar=-11, delta=encode(delta),
        unreduced_identity=encode(identity_numerator), F_multiple=encode(quotient),
        exact_remainder=encode(remainder), checks=checks, failures=failures,
        nonzero=dict(delta='degree 2 < irreducible degree 8, so nonzero',
                     denominator='explicit inverse certified',
                     h='h^2=-delta/11, so nonzero'),
        limits='No supported-group completeness, rational-point classification or integer exclusion.')
    path = Path(__file__).with_name('mask17-global-scalar-square-certificate.json')
    path.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(dict(result='IDENTITY' if not failures else 'FAILURE',
                          actual_remainder=encode(remainder), required_remainder=['0'],
                          checks=len(checks), failures=failures, h=encode(h),
                          certificate=str(path.relative_to(Path.cwd())))))
    assert not failures


if __name__ == '__main__':
    main()
