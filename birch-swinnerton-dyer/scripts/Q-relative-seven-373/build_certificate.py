"""One fixed depth-one test; exact general-Weierstrass arithmetic."""
from fractions import Fraction as F
from pathlib import Path
from math import gcd, lcm
import hashlib
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
UPSTREAM = HERE.parent / 'known-point-seven-307/certificate.json'


def enc(q):
    q = F(q)
    return [q.numerator, q.denominator]


def pt(p):
    return None if p is None else [enc(z) for z in p]


def good(p):
    return p is None or p[1]**2+p[1] == p[0]**3+p[0]**2-2*p[0]


def add(p, q):
    assert good(p) and good(q)
    if p is None or q is None:
        return (q if p is None else p), {'branch': 'identity'}
    x, y = p
    u, v = q
    if x == u and y+v+1 == 0:
        return None, {'branch': 'inverse'}
    if p == q:
        d = 2*y+1
        assert d
        m = (3*x*x+2*x-2)/d
        n = (-x**3-2*x-y)/d
        branch = 'tangent'
    else:
        d = u-x
        assert d
        m, n = (v-y)/d, (y*u-v*x)/d
        branch = 'chord'
    z = m*m-1-x-u
    r = z, -m*z-n-1
    assert good(r)
    return r, {'branch': branch, 'denominator': enc(d),
               'slope': enc(m), 'intercept': enc(n)}


def strip(n):
    assert n
    e = 0
    while n % 7 == 0:
        n //= 7
        e += 1
    return e, n


def val(z):
    a, b = strip(z.numerator), strip(z.denominator)
    return {'fraction': enc(z), 'numerator_v7': a[0],
            'denominator_v7': b[0], 'v7': a[0]-b[0],
            'numerator_unit': a[1], 'denominator_unit': b[1],
            'unit_residues': [a[1] % 7, b[1] % 7]}


def local(p):
    if p is None:
        return {'identity': True, 'primitive': [0, 1, 0],
                'reduction': [0, 1, 0], 'in_E2': True}
    x, y = p
    assert x and y
    z = lcm(x.denominator, y.denominator)
    raw = [int(x*z), int(y*z), z]
    g = gcd(gcd(abs(raw[0]), abs(raw[1])), raw[2])
    X, Y, Z = triple = [a//g for a in raw]
    assert Y*Y*Z+Y*Z*Z == X**3+X*X*Z-2*X*Z*Z
    values = {name: val(a) for name, a in [('x', x), ('y', y), ('t', -x/y)]}
    assert X % 7 == Z % 7 == 0 and Y % 7 != 0
    return {'identity': False, 'primitive': triple,
            'reduction': [a % 7 for a in triple], 'values': values,
            'in_E2': values['t']['v7'] >= 2}


def main():
    rows = []

    def row(p, q, lp, lq):
        r, data = add(p, q)
        lr = [a+b for a, b in zip(lp, lq)]
        rows.append({'left': pt(p), 'right': pt(q), 'output': pt(r),
                     'left_label': lp, 'right_label': lq,
                     'output_label': lr, **data})
        return r

    ends = []
    for basis, point in enumerate([(F(0), F(0)), (F(1), F(0))]):
        points = {1: point}
        for a, b in [(1, 1), (2, 1), (3, 3), (6, 6), (12, 1)]:
            la, lb = [0, 0], [0, 0]
            la[basis], lb[basis] = a, b
            points[a+b] = row(points[a], points[b], la, lb)
        ends.append(points[13])
    wp, wq = ends
    assert pt(wp) == json.loads(UPSTREAM.read_text())['W']
    multiples = [None]
    for c in range(1, 7):
        multiples.append(row(multiples[-1], wp, [13*(c-1), 0], [13, 0]))
    candidates = []
    for c in range(7):
        p = multiples[c]
        negative = None if p is None else (p[0], -p[1]-1)
        a = row(wq, negative, [0, 13], [-13*c, 0])
        candidates.append({'c': c, 'point': pt(a), 'local': local(a)})
    winners = [r['c'] for r in candidates if r['local']['in_E2']]
    assert len(winners) == 1
    assert all(r['local']['in_E2'] or r['local']['values']['t']['v7'] == 1
               for r in candidates)
    cert = {'schema': 'Q-relative-seven-373-v1', 'model': [0, 1, 1, -2, 0],
            'prime': 7, 'depth': 1, 'P': pt((F(0), F(0))),
            'Q': pt((F(1), F(0))), 'rows': rows,
            'W_P': pt(wp), 'W_Q': pt(wq), 'W_Q_local': local(wq),
            'candidates': candidates, 'winners': winners,
            'upstream_sha256': hashlib.sha256(UPSTREAM.read_bytes()).hexdigest()}
    out = HERE / 'certificate.json'
    out.write_text(json.dumps(cert, indent=2)+'\n')
    print(f'PASS: {len(rows)} complete rows; winner={winners}; '
          f't valuations={[r["local"].get("values", {}).get("t", {}).get("v7", "O") for r in candidates]}; '
          f'required=one >=2 (or O), six =1; failures=0; {out}')


if __name__ == '__main__':
    main()
