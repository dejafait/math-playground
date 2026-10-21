"""Full-cell integer-interval inclusion for L134's two E scalars.

Run from the notebook with no arguments; --audit replays every saved record.
Only printed decimal summaries use floating point.
"""
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from check_joint_curl_tensor import I, SCALE, atan_bounds, cosine

N = 64
PATH = Path(__file__).with_name('e-scalar-enclosure-certificate.json')
TARGETS = [(F(-93, 100), F(-17, 20)), (F(-11, 50), F(-11, 100))]


def inputs():
    al, au = atan_bounds(5, 60)
    bl, bu = atan_bounds(239, 20)
    pl, ph = 16*al-4*bu, 16*au-4*bl
    assert F(3) < pl <= ph < F(22, 7)
    pi = I(I.rat(pl).lo, I.rat(ph).hi)
    nodes = []
    for j in range(N+1):
        theta = pi*I.rat(F(j, N))
        co = cosine(theta)
        x = I.rat(2)-I.rat(2)*co
        x = I(max(0, x.lo), min(4*SCALE, x.hi))
        if j == 0:
            x = I(0)
        if j == N:
            x = I(4*SCALE)
        assert 0 <= x.lo <= x.hi <= 4*SCALE
        nodes.append({'index': j, 'theta': theta.data(),
                      'cosine': co.data(), 'X': x.data()})
    return {'lower': str(pl), 'upper': str(ph), 'interval': pi.data()}, nodes


def square(v):
    lo = 0 if v.lo <= 0 <= v.hi else min(v.lo*v.lo, v.hi*v.hi)//SCALE
    hi = -(-max(v.lo*v.lo, v.hi*v.hi)//SCALE)
    return I(lo, hi)


def cell_values(x, y, z, corner):
    one, four, eight = [I.rat(v) for v in (1, 4, 8)]
    lam = x+y+z
    if corner:
        return [I(0, (lam/four).hi), I(0, (z*(z+four)/eight).hi)]
    assert lam.lo > 0
    den = square(lam)
    j = x*z*(y+z)*(one-x/four)/den
    a = square(x-y)*z*(z+four)/(eight*den)
    assert j.lo >= 0 and a.lo >= 0
    return [j, a]


def records(nodes):
    xs = [I(*map(int, row['X'])) for row in nodes]
    ranges = [I(xs[j].lo, xs[j+1].hi) for j in range(N)]
    for j, x in enumerate(ranges):
        for m, y in enumerate(ranges):
            for p, z in enumerate(ranges):
                vals = cell_values(x, y, z, j == m == p == 0)
                yield [j, m, p, *[v.data() for v in vals]], vals


def bounds(totals):
    den = N**3*SCALE
    endpoints = [(F(totals[0].lo, den)-1, F(totals[0].hi, den)-1),
                 (-F(totals[1].hi, den), -F(totals[1].lo, den))]
    return [{'name': name, 'lower': str(lo), 'upper': str(hi),
             'required_lower': str(target[0]), 'required_upper': str(target[1]),
             'width': str(hi-lo), 'required_max_width': str(target[1]-target[0])}
            for name, (lo, hi), target in zip(('beta_E', 'alpha_E'), endpoints, TARGETS)]


def main(audit=False):
    pi, nodes = inputs()
    totals = [I(0), I(0)]
    saved = json.loads(PATH.read_text()) if audit else None
    if audit:
        assert saved['N'] == N and saved['SCALE'] == str(SCALE)
        assert saved['pi'] == pi and saved['nodes'] == nodes
        assert len(saved['cells']) == N**3
    cells = []
    for q, (record, vals) in enumerate(records(nodes)):
        if audit:
            assert saved['cells'][q] == record
        else:
            cells.append(record)
        totals = [a+b for a, b in zip(totals, vals)]
    b = bounds(totals)
    failures = [row['name']+' required enclosure not met' for row in b
                if not F(row['required_lower']) < F(row['lower'])
                <= F(row['upper']) < F(row['required_upper'])]
    total_data = [t.data() for t in totals]
    if audit:
        assert saved['totals'] == total_data and saved['bounds'] == b
        assert saved['failures'] == failures
        path = PATH.with_name('e-scalar-enclosure-audit.json')
        cert = {'certificate': PATH.name, 'nodes_replayed': N+1,
                'cells_replayed': N**3, 'bounds_replayed': b, 'failures': failures}
    else:
        path = PATH
        cert = {'schema': 'L134-complete-E-cell-inclusion-v1',
                'N': N, 'SCALE': str(SCALE), 'pi': pi, 'nodes': nodes,
                'cells': cells, 'totals': total_data, 'bounds': b,
                'failures': failures,
                'method': 'Entire [0,pi]^3; exact weight 1/N^3; corner J<=L/4, A<=Z(Z+4)/8',
                'qualification': 'Universal E scalars only; no physical heat-form value, E sign or compensation.'}
    path.write_text(json.dumps(cert, separators=(',', ':'))+'\n')
    for row in b:
        print(f"{row['name']}: [{float(F(row['lower'])):.9f}, {float(F(row['upper'])):.9f}], "
              f"required ({row['required_lower']}, {row['required_upper']}), "
              f"width {float(F(row['width'])):.9f}, required below {row['required_max_width']}")
    print(f"Complete {'audit' if audit else 'certificate'}: {path}; failures: {failures}")
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main('--audit' in sys.argv)
