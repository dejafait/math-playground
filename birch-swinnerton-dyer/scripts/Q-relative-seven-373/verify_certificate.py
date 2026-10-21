"""Independent full replay in Y^2=X^3-7X/3+107/108; no producer import."""
from fractions import Fraction as F
from pathlib import Path
from math import gcd
import hashlib
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent


def decode(z):
    assert len(z) == 2 and all(type(a) is int for a in z)
    assert z[1] > 0 and gcd(abs(z[0]), z[1]) == 1
    return F(*z)


def point(p):
    return None if p is None else tuple(decode(z) for z in p)


def enc(p):
    return None if p is None else [[z.numerator, z.denominator] for z in p]


def short(p):
    return None if p is None else (p[0]+F(1, 3), p[1]+F(1, 2))


def back(p):
    return None if p is None else (p[0]-F(1, 3), p[1]-F(1, 2))


def on(p):
    return p is None or p[1]**2 == p[0]**3-F(7, 3)*p[0]+F(107, 108)


def add(p, q):
    assert on(p) and on(q)
    if p is None or q is None:
        return (q if p is None else p), {'branch': 'identity'}
    x, y = p
    u, v = q
    if x == u and y == -v:
        return None, {'branch': 'inverse'}
    if p == q:
        denominator = 2*y
        assert denominator
        m = (3*x*x-F(7, 3))/denominator
        branch = 'tangent'
    else:
        denominator = u-x
        assert denominator
        m = (v-y)/denominator
        branch = 'chord'
    z = m*m-x-u
    r = z, -(y+m*(z-x))
    assert on(r)
    return r, {'branch': branch, 'denominator': [denominator.numerator, denominator.denominator],
               'slope': [m.numerator, m.denominator]}


def vdata(z):
    def exact(n):
        assert n
        k = 0
        while n % 7 == 0:
            n //= 7
            k += 1
        assert n % 7
        return k, n
    a, b = exact(z.numerator), exact(z.denominator)
    return {'fraction': [z.numerator, z.denominator], 'numerator_v7': a[0],
            'denominator_v7': b[0], 'v7': a[0]-b[0],
            'numerator_unit': a[1], 'denominator_unit': b[1],
            'unit_residues': [a[1] % 7, b[1] % 7]}


def check_local(p, evidence):
    X, Y, Z = evidence['primitive']
    assert gcd(gcd(abs(X), abs(Y)), abs(Z)) == 1
    assert Y*Y*Z+Y*Z*Z == X**3+X*X*Z-2*X*Z*Z
    assert evidence['reduction'] == [a % 7 for a in (X, Y, Z)]
    assert X % 7 == Z % 7 == 0 and Y % 7
    assert evidence['identity'] == (p is None)
    if p is None:
        assert [X, Y, Z] == [0, 1, 0] and evidence['in_E2']
        return None
    x, y = p
    assert Z > 0 and F(X, Z) == x and F(Y, Z) == y
    assert x and y
    for name, z in [('x', x), ('y', y), ('t', -x/y)]:
        assert evidence['values'][name] == vdata(z)
    valuation = vdata(-x/y)['v7']
    assert valuation >= 1 and evidence['in_E2'] == (valuation >= 2)
    return valuation


def main():
    path = HERE / 'certificate.json'
    c = json.loads(path.read_text())
    assert c['schema'] == 'Q-relative-seven-373-v1'
    assert c['model'] == [0, 1, 1, -2, 0] and c['prime'] == 7 and c['depth'] == 1
    P, Q = (F(0), F(0)), (F(1), F(0))
    assert point(c['P']) == P and point(c['Q']) == Q
    # Translation identity, including the constant term; projectively fixes O.
    assert F(-1, 27)+F(1, 9)+F(2, 3)+F(1, 4) == F(107, 108)
    assert F(1, 3)-F(2, 3)-2 == -F(7, 3)
    known = {(0, 0): None, (1, 0): P, (0, 1): Q}
    checks = []
    assert len(c['rows']) == 23
    for i, row in enumerate(c['rows']):
        lp, lq, lr = [tuple(row[k]) for k in ('left_label', 'right_label', 'output_label')]
        assert lr == tuple(a+b for a, b in zip(lp, lq))
        for label in (lp, lq):
            if label not in known:
                inv = tuple(-a for a in label)
                assert inv in known
                a = known[inv]
                known[label] = None if a is None else (a[0], -a[1]-1)
        p, q = point(row['left']), point(row['right'])
        assert p == known[lp] and q == known[lq]
        r, details = add(short(p), short(q))
        assert row['branch'] == details['branch']
        assert point(row['output']) == back(r)
        if 'denominator' in details:
            assert row['denominator'] == details['denominator']
            assert row['slope'] == details['slope']
            m, n = decode(row['slope']), decode(row['intercept'])
            x, y = p
            u, v = q
            z, w = back(r)
            assert m*x+n == y and m*u+n == v and m*z+n == -w-1
            # Complete polynomial factorization of line/curve intersection.
            residual = [n*n+n-x*u*z, 2*m*n+m+2+(x*u+x*z+u*z),
                        m*m-1-(x+u+z), F(0)]
            assert residual == [0, 0, 0, 0]
        if lr in known:
            assert known[lr] == back(r)
        known[lr] = back(r)
        checks.append({'row': i, 'branch': row['branch'], 'label': list(lr), 'passed': True})
    # Distinct sequential chains from O through 78P and 13Q.
    sequential = {}
    for name, base, bound in [('P', P, 78), ('Q', Q, 13)]:
        a = None
        seq = []
        for k in range(1, bound+1):
            before = a
            a, detail = add(a, short(base))
            seq.append({'scalar': k, 'left_short': enc(before),
                        'output_short': enc(a), **detail})
            label = (k, 0) if name == 'P' else (0, k)
            if label in known:
                assert known[label] == back(a)
        sequential[name] = seq
    assert point(c['W_P']) == known[(13, 0)]
    assert point(c['W_Q']) == known[(0, 13)]
    up = HERE.parent / 'known-point-seven-307/certificate.json'
    assert hashlib.sha256(up.read_bytes()).hexdigest() == c['upstream_sha256']
    assert json.loads(up.read_text())['W'] == c['W_P']
    qv = check_local(point(c['W_Q']), c['W_Q_local'])
    assert [r['c'] for r in c['candidates']] == list(range(7))
    results = []
    for item in c['candidates']:
        n = item['c']
        p = point(item['point'])
        assert p == known[(-13*n, 13)]
        v = check_local(p, item['local'])
        results.append({'c': n, 'identity': p is None, 't_v7': v,
                        'in_E2': item['local']['in_E2'],
                        'reduction': item['local']['reduction'],
                        'valuation_triples': {k: [z['numerator_v7'], z['denominator_v7'], z['v7']]
                                              for k, z in item['local'].get('values', {}).items()},
                        't_unit_residues': item['local'].get('values', {}).get('t', {}).get('unit_residues')})
    winners = [r['c'] for r in results if r['in_E2']]
    assert winners == c['winners'] and len(winners) == 1
    assert all(r['in_E2'] or r['t_v7'] == 1 for r in results)
    report = {'certificate_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
              'status': 'PASS', 'failures': [], 'row_checks': checks,
              'sequential_checks': sequential, 'Q_t_v7': qv,
              'candidate_checks': results, 'winner': winners[0],
              'threshold': 'exactly one O or t valuation >=2; six valuations exactly 1',
              'upstream_P_match': True}
    out = HERE / 'verification.json'
    out.write_text(json.dumps(report, indent=2)+'\n')
    print(f'PASS: {len(checks)} full rows, 91 sequential additions, all 7 candidates; '
          f'actual winner={winners[0]}, valuations={[r["t_v7"] for r in results]}; '
          f'required=one >=2 or O, six =1; failures=0; {out}')


if __name__ == '__main__':
    main()
