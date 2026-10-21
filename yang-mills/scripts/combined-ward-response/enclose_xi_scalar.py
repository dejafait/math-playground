"""L131 complete xi cell enclosure and supporting exact matrix checks.

Run: python3 scripts/combined-ward-response/enclose_xi_scalar.py
Audit: python3 scripts/combined-ward-response/enclose_xi_scalar.py --audit
Finite matrix checks support, but do not replace, L131's analytic proof.
"""
import json
import sys
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from check_joint_curl_tensor import I, SCALE, atan_bounds, cosine, matmul, transpose

N = 256
PATH = Path(__file__).with_name('xi-scalar-enclosure-certificate.json')
TARGET = (F(1, 100), F(1, 10))


def matrix_checks():
    choices = [(F(6, 5), F(4, 5)), (F(8, 5), F(3, 5)),
               (F(24, 13), F(5, 13))]
    records = []
    for selected in product(choices, repeat=3):
        for signs in product((-1, 1), repeat=3):
            d = [s*q[0] for s, q in zip(signs, selected)]
            x, y, z = d
            A, B, C = [q[1] for q in selected]
            L = sum(t*t for t in d)
            p = [[d[i]*d[j]/L for j in range(3)] for i in range(3)]
            q = [[F(i == j)-p[i][j] for j in range(3)] for i in range(3)]
            Z = [[-y, x, F(0)], [-z, F(0), x], [F(0), -z, y]]
            R = [[-2*B, F(0), F(0)], [F(0)]*3, [F(0), F(0), 2*B]]
            C0 = [[F(0), 2*A*B, F(0)], [-2*A*B, F(0), F(0)], [F(0)]*3]
            U = [[F(0)]*3, [A*B*B, F(0), F(0)], [F(0), A*C*C, F(0)]]
            alpha = matmul(matmul(matmul(p, R), Z), q)
            beta = matmul(matmul(p, C0), q)
            first = matmul(transpose(beta), alpha)
            second = matmul(transpose(alpha), beta)
            bracket = [[first[i][j]-second[i][j] for j in range(3)] for i in range(3)]
            traced = matmul(matmul(q, bracket), matmul(U, Z))
            actual = -sum(traced[j][j] for j in range(3))/L
            required = A*A*B*B*y*y*z*z*(z*z-y*y)/L**2
            swapped = A*A*C*C*y*y*z*z*(y*y-z*z)/L**2
            sym_actual = (actual+swapped)/2
            sym_required = A*A*y*y*z*z*(z*z-y*y)**2/(8*L**2)
            records.append({'d': list(map(str, d)), 'eta': list(map(str, (A, B, C))),
                'actual': str(actual), 'required': str(required),
                'residual': str(actual-required),
                'symmetrized_actual': str(sym_actual),
                'symmetrized_required': str(sym_required),
                'symmetrized_residual': str(sym_actual-sym_required)})
    return records


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
        v = I.rat(2)-I.rat(2)*co
        v = I(max(0, v.lo), min(4*SCALE, v.hi))
        if j == 0:
            v = I(0)
        if j == N:
            v = I(4*SCALE)
        nodes.append({'index': j, 'theta': theta.data(),
                      'cosine': co.data(), 'd_squared': v.data()})
    return {'lower': str(pl), 'upper': str(ph), 'interval': pi.data()}, nodes


def square(v):
    # Exact enclosure of the range of t^2, including intervals crossing 0.
    lo = 0 if v.lo <= 0 <= v.hi else min(v.lo*v.lo, v.hi*v.hi)
    hi = max(v.lo*v.lo, v.hi*v.hi)
    return I(lo//SCALE, -((-hi)//SCALE))


def cell_value(y, z, corner):
    k = y+z
    if corner:
        bound = k*k*k.sqrt()/I.rat(128)
        return I(0, bound.hi)
    assert k.lo > 0
    val = y*z*square(z-y)/(I.rat(16)*k*(k*(k+I.rat(4))).sqrt())
    assert 0 <= val.lo <= val.hi
    return val


def main(audit=False):
    pi, nodes = inputs()
    checks = matrix_checks()
    failures = [f'matrix check {j}' for j, row in enumerate(checks)
                if row['residual'] != '0' or row['symmetrized_residual'] != '0']
    saved = json.loads(PATH.read_text()) if audit else None
    if audit:
        assert saved['N'] == N and saved['SCALE'] == str(SCALE)
        assert saved['pi'] == pi and saved['nodes'] == nodes
        assert saved['exact_matrix_checks'] == checks
        assert len(saved['cells']) == N*N
    xs = [I(*map(int, row['d_squared'])) for row in nodes]
    total, cells = I(0), []
    for j in range(N):
        y = I(xs[j].lo, xs[j+1].hi)
        for m in range(N):
            z = I(xs[m].lo, xs[m+1].hi)
            val = cell_value(y, z, j == 0 and m == 0)
            record = [j, m, val.data()]
            if audit:
                assert saved['cells'][j*N+m] == record
            else:
                cells.append(record)
            total = total+val
    lo, hi = F(total.lo, N*N*SCALE), F(total.hi, N*N*SCALE)
    bounds = {'lower': str(lo), 'upper': str(hi),
              'required_lower': str(TARGET[0]), 'required_upper': str(TARGET[1])}
    if not TARGET[0] < lo <= hi < TARGET[1]:
        failures.append('required xi enclosure not met')
    if audit:
        assert saved['totals'] == total.data() and saved['bounds'] == bounds
        assert saved['failures'] == failures
        path = PATH.with_name('xi-scalar-enclosure-audit.json')
        data = {'certificate': PATH.name, 'nodes_replayed': N+1,
                'cells_replayed': N*N, 'matrix_checks_replayed': len(checks),
                'bounds_replayed': bounds, 'failures': failures}
    else:
        path = PATH
        data = {'schema': 'L131-complete-xi-cell-inclusion-v1',
                'N': N, 'SCALE': str(SCALE), 'pi': pi, 'nodes': nodes,
                'exact_matrix_checks': checks, 'cells': cells,
                'totals': total.data(), 'bounds': bounds, 'failures': failures,
                'method': 'Full-cell integer interval inclusion; continuous corner bound k^(5/2)/128; equal normalized area 1/N^2',
                'qualification': 'Universal xi only. Analytic matrix/integral proof in L131; no actual-probe sign or complete compensation.'}
    path.write_text(json.dumps(data, separators=(',', ':'))+'\n')
    print(f'xi: [{float(lo):.9f}, {float(hi):.9f}], required ({TARGET[0]}, {TARGET[1]})')
    print(f'Nodes: {N+1}; cells: {N*N}; exact matrix checks: {len(checks)}')
    print(f'Failures: {failures}; full {"audit" if audit else "certificate"}: {path}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main('--audit' in sys.argv)
