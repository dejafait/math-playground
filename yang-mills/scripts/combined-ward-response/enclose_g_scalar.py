"""Full-cell integer inclusion of L140's G scalar; --audit replays all cells.

Only decimal output uses floating point. All inclusion uses L127's
arbitrary-precision fixed-point arithmetic and endpoint cosine bounds.
"""
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from check_joint_curl_tensor import I, SCALE, atan_bounds, cosine

N = 64
PATH = Path(__file__).with_name('g-scalar-enclosure-certificate.json')
TARGET = (F(-1, 8), F(-1, 100))
WIDTH = F(1, 20)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
        nodes.append(dict(index=j, theta=theta.data(), cosine=co.data(), X=x.data()))
    return dict(lower=str(pl), upper=str(ph), interval=pi.data()), nodes


def square(v):
    lo = 0 if v.lo <= 0 <= v.hi else min(v.lo*v.lo, v.hi*v.hi)//SCALE
    hi = -(-max(v.lo*v.lo, v.hi*v.hi)//SCALE)
    return I(lo, hi)


def cell_value(x, y, z, corner):
    lam = x+y+z
    if corner:
        return I(0, (square(lam)/I.rat(16)).hi)
    assert lam.lo > 0
    result = x*y*square(x-y)/(I.rat(4)*square(lam))
    assert result.lo >= 0
    return result


def records(nodes):
    xs = [I(*map(int, r['X'])) for r in nodes]
    ranges = [I(xs[j].lo, xs[j+1].hi) for j in range(N)]
    for j, x in enumerate(ranges):
        for m, y in enumerate(ranges):
            for p, z in enumerate(ranges):
                value = cell_value(x, y, z, j == m == p == 0)
                yield [j, m, p, value.data()], value


def main(audit=False):
    pi, nodes = inputs()
    saved = json.loads(PATH.read_text()) if audit else None
    hashes = dict(script=sha(Path(__file__)),
                  arithmetic=sha(Path(__file__).with_name('check_joint_curl_tensor.py')))
    if audit:
        assert saved['N'] == N and saved['SCALE'] == str(SCALE)
        assert saved['hashes'] == hashes
        assert saved['pi'] == pi and saved['nodes'] == nodes
        assert len(saved['cells']) == N**3
    cells, total = [], I(0)
    count = 0
    for q, (record, value) in enumerate(records(nodes)):
        if audit:
            assert saved['cells'][q] == record
        else:
            cells.append(record)
        total = total+value
        count += 1
    assert count == N**3
    den = N**3*SCALE
    lower, upper = -F(total.hi, den), -F(total.lo, den)
    bounds = dict(lower=str(lower), upper=str(upper), width=str(upper-lower),
                  required_lower=str(TARGET[0]), required_upper=str(TARGET[1]),
                  required_max_width=str(WIDTH))
    failures = []
    if not TARGET[0] < lower <= upper < TARGET[1]:
        failures.append('required containing interval not met')
    if not upper-lower < WIDTH:
        failures.append('required width not met')
    if audit:
        assert saved['total'] == total.data() and saved['bounds'] == bounds
        assert saved['failures'] == failures
        path = PATH.with_name('g-scalar-enclosure-audit.json')
        certificate = dict(certificate=PATH.name, certificate_sha256=sha(PATH),
                           nodes_replayed=N+1, cells_replayed=count,
                           bounds_replayed=bounds, failures=failures)
    else:
        path = PATH
        certificate = dict(schema='L140-complete-G-cell-inclusion-v1', N=N,
                           SCALE=str(SCALE), hashes=hashes, pi=pi, nodes=nodes,
                           cells=cells, total=total.data(), bounds=bounds,
                           failures=failures,
                           method='Entire [0,pi]^3; exact weight 1/N^3; corner 0<=T<=L^2/16',
                           qualification='Universal G scalar only; physical B_G, G signs and compensation remain unresolved.')
    path.write_text(json.dumps(certificate, separators=(',', ':'))+'\n')
    print(f'g_G: [{float(lower):.9f}, {float(upper):.9f}], '
          f'required ({TARGET[0]}, {TARGET[1]}), width {float(upper-lower):.9f}, '
          f'required below {WIDTH}; cells {count}; failures {failures}; path {path}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main('--audit' in sys.argv)
