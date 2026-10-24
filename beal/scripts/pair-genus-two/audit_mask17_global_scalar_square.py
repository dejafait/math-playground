#!/usr/bin/env python3
"""Critical-audit arithmetic for the fixed positive certificate only.

No producer/replay imports; preserve both original artifacts. Discovery
factorization completeness is deliberately not an obligation of this audit.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json


def product(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            out[i+j] += a[i] * b[j]
    return out


def evaluate(a, x):
    out = 0
    for c in reversed(a):
        out = x*out + c
    return out


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, list):
        return [encode(x) for x in value]
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    return value


def main():
    directory = Path(__file__).parent
    names = ['mask17-global-scalar-square-certificate.json',
             'mask17-global-scalar-square-replay.json']
    paths = [directory/name for name in names]
    producer, replay = [json.loads(path.read_text()) for path in paths]
    hashes = {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
              for path in paths}
    f = [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]
    p = [0, -6183, 0, 8865, 0, -3085, 0, 275]
    r = [-110592, 0, 120825, 0, -36410, 0, 3025]
    d = 1728
    delta = [-9, 0, 1]
    h = [Q(c, d) for c in p]
    displayed = [-26873856, 0, 423510363, 0, -1205870490, 0,
                 1284110685, 0, -639074700, 0, 158322725, 0,
                 -18664250, 0, 831875]
    rows = []

    def check(name, actual, required):
        rows.append(dict(name=name, actual=actual, required=required,
                         passed=actual == required))

    lhs = [11*x for x in product(p, p)]
    for i, c in enumerate(delta):
        lhs[i] += d*d*c
    rhs = product(f, r)
    for i in range(15):
        check(f'coefficient {i}', [lhs[i], rhs[i]], [displayed[i]]*2)
    # A separate Horner-value proof: both polynomials have degree <=14.
    for x in range(15):
        check(f'exact evaluation {x}',
              11*evaluate(p, x)**2 + d*d*(x*x-9),
              evaluate(f, x)*evaluate(r, x))
    check('mask 17 bit positions', [i for i in range(5) if 17 & (1 << i)], [0, 4])
    check('actual generator product', product([-3, -1], [3, -1]), delta)
    check('denominator nonzero', d != 0, True)
    check('delta degree below minimal degree', len(delta)-1 < 8, True)
    check('h nonzero representative below degree eight', any(h) and len(h)-1 < 8, True)

    # Monomial reduction uses repeated shift, not polynomial long division.
    monomials = [[Q(1)] + [Q(0)]*7]
    for degree in range(1, 15):
        previous = monomials[-1]
        next_row = [Q(0)] + previous[:7]
        for i in range(8):
            next_row[i] -= previous[7]*Q(f[i], f[8])
        monomials.append(next_row)
    numerator = [-11*x for x in product(h, h)]
    for i, c in enumerate(delta):
        numerator[i] -= c
    reduced = [sum(c*monomials[k][i] for k, c in enumerate(numerator))
               for i in range(8)]
    check('entire quotient identity', reduced, [Q(0)]*8)
    multiple = [-Q(c, d*d) for c in r]
    check('unreduced identity from exact F multiple', numerator, product(f, multiple))
    selected = dict(F=list(map(Q, f)), h=h, scalar=-11,
                    delta=list(map(Q, delta)), unreduced_identity=numerator,
                    F_multiple=multiple, exact_remainder=[Q(0)])
    for key, required in selected.items():
        actual = producer[key]
        if isinstance(required, list):
            actual = list(map(Q, actual))
        check('producer '+key, actual, required)
    check('producer failures', producer['failures'], [])
    expected_replay = dict(F=f, P=p, R=r, denominator=d, scalar=-11,
                           left_coefficients=lhs, right_coefficients=rhs,
                           producer_sha256=hashes[names[0]],
                           producer_h=[str(c) for c in h],
                           expected_h=[str(c) for c in h],
                           comparisons=18, failures=[])
    for key, required in expected_replay.items():
        check('replay '+key, replay[key], required)
    failures = [row['name'] for row in rows if not row['passed']]
    result = dict(scope='C124b positive identity and its complete load-bearing evidence',
                  source_sha256=hashes, F=f, P=p, R=r, denominator=d,
                  scalar=-11, h=h, delta=delta, left_coefficients=lhs,
                  right_coefficients=rhs, monomial_reductions=monomials,
                  quotient_remainder=reduced, comparisons=rows, failures=failures,
                  limitations='No discovery-search completeness, supported-group or point calculation.')
    target = directory/'mask17-global-scalar-square-audit-certificate.json'
    target.write_text(json.dumps(encode(result), indent=2)+'\n')
    print(json.dumps(dict(result='PASS' if not failures else 'FAIL',
                          comparisons=len(rows), coefficient_equalities='15/15',
                          exact_evaluation_equalities='15/15',
                          actual_quotient_remainder=encode(reduced),
                          required_quotient_remainder=['0']*8, failures=failures,
                          certificate=str(target.relative_to(Path.cwd())))))
    assert not failures


if __name__ == '__main__':
    main()
