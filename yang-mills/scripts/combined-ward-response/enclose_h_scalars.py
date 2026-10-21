"""Complete cell-interval integration of L129; exact integer arithmetic.

Run: python3 scripts/combined-ward-response/enclose_h_scalars.py
Audit: python3 scripts/combined-ward-response/enclose_h_scalars.py --audit
"""
import json
import sys
from fractions import Fraction as F
from pathlib import Path
from check_joint_curl_tensor import I, SCALE, atan_bounds, cosine

N = 512
PATH = Path(__file__).with_name('h-scalar-enclosure-certificate.json')
TARGETS = [(F(1, 5), F(3, 10)), (F(1, 10), F(1, 6)),
           (F(-7, 20), F(-1, 4))]


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
        nodes.append({'index': j, 'theta': theta.data(),
                      'cosine': co.data(), 'X': x.data()})
    return {'lower': str(pl), 'upper': str(ph),
            'interval': pi.data()}, nodes


def cell_values(x, z, corner):
    one, two, four, six, sixteen = [I.rat(v) for v in (1, 2, 4, 6, 16)]
    k = x+z
    if corner:
        # L129(4); only k's upper bound is needed.
        root = k.sqrt()
        bd = (four*root).hi
        bx = (two*root).hi
        ba = (k/four+I.rat(3)*root).hi
        return [I(-bd, bd), I(0, bx), I(SCALE-ba, SCALE+ba)]
    assert k.lo > 0
    a, c = one-x/four, one-z/four
    root = (k*(k+four)).sqrt()
    j0 = one/root
    j1 = (k+two)/(root*root*root)
    u0 = ((k+four)*j0-one)/four
    u1 = ((k+four)*j1-j0)/four
    v0 = ((k+four)*(k+four)*j0-k-six)/sixteen
    v1 = ((k+four)*(k+four)*j1-two*(k+four)*j0+one)/sixteen
    w = u0-k*u1
    # All five moments are nonnegative by L129(10).
    u0, u1, v0, v1, w = [I(max(0, v.lo), v.hi)
                          for v in (u0, u1, v0, v1, w)]
    assert all(v.lo <= v.hi for v in (u0, u1, v0, v1, w))
    shared = x*(four+z)*v0/two
    fd = shared-two*a*z*(k*v1+c*w)
    fx = a*z*(k*v1+c*k*u1+two*c*w)
    fa = a-two*a*k*u0-shared
    return [fd, fx, fa]


def records(nodes):
    xs = [I(*map(int, n['X'])) for n in nodes]
    for j in range(N):
        x = I(xs[j].lo, xs[j+1].hi)
        for m in range(N):
            z = I(xs[m].lo, xs[m+1].hi)
            vals = cell_values(x, z, j == 0 and m == 0)
            yield [j, m, *[v.data() for v in vals]], vals


def bounds(totals):
    return [{'lower': str(F(t.lo, N*N*SCALE)),
             'upper': str(F(t.hi, N*N*SCALE)),
             'required_lower': str(lo), 'required_upper': str(hi)}
            for t, (lo, hi) in zip(totals, TARGETS)]


def main(audit=False):
    pi, nodes = inputs()
    totals = [I.rat(0) for _ in range(3)]
    saved = json.loads(PATH.read_text()) if audit else None
    if audit:
        assert saved['N'] == N and saved['SCALE'] == str(SCALE)
        assert saved['pi'] == pi and saved['nodes'] == nodes
        assert len(saved['cells']) == N*N
    cells = []
    for q, (record, vals) in enumerate(records(nodes)):
        if audit:
            assert saved['cells'][q] == record
        else:
            cells.append(record)
        totals = [a+b for a, b in zip(totals, vals)]
    b = bounds(totals)
    failures = []
    for name, row in zip(('h_D', 'h_X', 'h_A'), b):
        if not F(row['required_lower']) < F(row['lower']) <= F(row['upper']) < F(row['required_upper']):
            failures.append(name+' required enclosure not met')
    total_data = [t.data() for t in totals]
    if audit:
        assert saved['totals'] == total_data and saved['bounds'] == b
        assert saved['failures'] == failures
        path = PATH.with_name('h-scalar-enclosure-audit.json')
        path.write_text(json.dumps({'certificate': PATH.name,
            'nodes_replayed': N+1, 'cells_replayed': N*N,
            'bounds_replayed': b, 'failures': failures}, indent=2)+'\n')
    else:
        path = PATH
        cert = {'schema': 'L129-complete-cell-inclusion-v1',
            'N': N, 'SCALE': str(SCALE), 'pi': pi, 'nodes': nodes,
            'cells': cells, 'totals': total_data, 'bounds': b,
            'failures': failures, 'method': 'full-cell integer interval inclusion; corner L129(4); equal normalized area 1/N^2',
            'qualification': 'Universal H scalars only; no actual-probe sign or compensation.'}
        path.write_text(json.dumps(cert, separators=(',', ':'))+'\n')
    for name, row in zip(('h_D', 'h_X', 'h_A'), b):
        print(f"{name}: [{float(F(row['lower'])):.9f}, {float(F(row['upper'])):.9f}], required ({row['required_lower']}, {row['required_upper']})")
    print(f"Complete {'audit' if audit else 'certificate'}: {path}; failures: {failures}")
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main('--audit' in sys.argv)
