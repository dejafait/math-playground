#!/usr/bin/env python3
"""Exact pinned-incidence algebra test; no actual-probe asymptotic test."""
import json
from fractions import Fraction as F
from pathlib import Path


def transpose(a):
    return list(map(list, zip(*a)))


def multiply(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def vector(a, x):
    return [sum(v*t for v, t in zip(row, x)) for row in a]


def subtract(a, b):
    return [[x-y for x, y in zip(r, s)] for r, s in zip(a, b)]


def diagonal(x):
    return [[v*F(i == j) for j in range(len(x))] for i, v in enumerate(x)]


def chain(*a):
    result = a[0]
    for b in a[1:]:
        result = multiply(result, b)
    return result


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def encode(a):
    return [[str(x) for x in row] for row in a]


def main():
    # One interior vertex, lower/upper normal edges in each of four directions.
    # This uses the pinned incidence/prefix, but S, A and B are synthetic.
    m = 8
    d = [F((-1)**i) for i in range(m)]
    identity = diagonal([F(1)]*m)
    p = [[identity[i][j]-d[i]*d[j]/8 for j in range(m)] for i in range(m)]
    phi = [[F(j == 0) for j in range(m)]]
    q = [[F(1)] for _ in range(m)]
    v = multiply(q, phi)
    f = multiply([[x] for x in d], phi)
    h = [[identity[i][j]-f[i][j]/2 for j in range(m)] for i in range(m)]
    r = subtract(identity, f)
    n = [F(i in (0, 1)) for i in range(m)]
    y = [F(i in (2, 3)) for i in range(m)]
    t = vector(p, [F(i == 2) for i in range(m)])
    tilt = [[a*b for b in t] for a in t]
    b = [[n[i]*y[j]+y[i]*n[j] for j in range(m)] for i in range(m)]
    assert multiply(p, p) == p
    assert multiply(p, [[x] for x in d]) == [[F(0)] for _ in range(m)]
    assert chain(p, tilt, p) == tilt and chain(p, b, p) == b
    records = []
    for nn, yy in ((n, y), (y, n)):
        raw = subtract(chain(transpose(h), diagonal(yy), v),
                       chain(transpose(v), diagonal(yy), h))
        jy = [[-x/2 for x in row] for row in raw]
        j = chain(p, jy, p)
        assert transpose(j) == [[-x for x in row] for row in j]
        alpha, beta = vector(v, nn), vector(r, nn)
        u = subtract(multiply(diagonal(alpha), h),
                     multiply(diagonal(vector(h, nn)), v))
        aa = chain(p, diagonal(alpha), p)
        c = chain(p, diagonal(beta), v, p)
        assert chain(p, u, p) == subtract(aa, c)
        direct = -6*trace(chain(p, jy, tilt, transpose(u)))
        multiplication = -3*trace(multiply(j, subtract(multiply(tilt, aa),
                                                      multiply(aa, tilt))))
        transport = 3*trace(multiply(j, subtract(multiply(tilt, transpose(c)),
                                               multiply(c, tilt))))
        assert direct == multiplication+transport
        records.append({'n': list(map(str, nn)), 'y': list(map(str, yy)),
                        'alpha': list(map(str, alpha)), 'beta': list(map(str, beta)),
                        'original_trace': str(direct),
                        'multiplication_commutator': str(multiplication),
                        'prefix_transport': str(transport), 'exact_match': True})
    total = sum(F(row['original_trace']) for row in records)
    assert total == F(-3, 8)
    assert all(F(row['multiplication_commutator']) == 0 for row in records)
    out = Path(__file__).with_name('probe-quartic-skew-split-certificate.json')
    out.write_text(json.dumps({
        'scope': 'Pinned-incidence synthetic algebra; S=P, A=M/2, B synthetic; no actual probe value.',
        'checks': records,
        'pinned_fixture': {'D': list(map(str, d)), 'Phi': encode(phi), 'q': encode(q),
                           'P': encode(p), 'M': encode(tilt), 'B': encode(b),
                           'full_symmetric_B_Q3': str(total)},
        'failures': [],
        'actual_bound': 'Unchanged: O(N^(7/2)) from L187',
        'required_bound': 'O(N^3), followed by a controlled limit',
        'actual_probe_limit': None,
    }, indent=2)+'\n')
    print('Skew split/product checks: 2/2 PASS; symmetric synthetic B Q3=-3/8')
    print('Multiplication commutators vanish; retained prefix transport does not; failures: 0')
    print('Actual bound unchanged O(N^(7/2)); required O(N^3); no actual-probe limit')
    print(out)


if __name__ == '__main__':
    main()
