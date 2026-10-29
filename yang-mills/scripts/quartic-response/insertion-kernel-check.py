"""Finite supporting check of L284(7)–(8), not an asymptotic proof.

Apply the raw relative component Laplacian to every entry of selected
GC_12^* columns, including both normal endpoint rows. The independently
assembled right side is the oriented plaquette incidence transpose.
"""
from itertools import product
from math import asinh, cos, pi, sin, sinh, sqrt
from pathlib import Path
import json

threshold = 2e-11
checks = []
for n in (4, 6):
    a = 8 / n
    vertices = range(1, n)
    edges = range(n)
    v = {k: {j: .5 * sin(pi * k * j / n) for j in vertices}
         for k in vertices}
    e = {k: {j: (1 / sqrt(8) if k == 0 else
                     .5 * cos(pi * k * (j + .5) / n)) for j in edges}
         for k in edges}
    omega = {k: 2 / a * sin(pi * k / (2 * n)) for k in edges}
    sources = ((0, 0, 1, 1), (n-1, n-1, n-1, n-1),
               (1, n-2, n//2, n//2))
    for p in sources:
        for mu in (0, 1):
            grids = [edges if axis == mu else vertices for axis in range(4)]
            rows = list(product(*grids))
            values = dict.fromkeys(rows, 0.0)
            mode_grids = [edges if axis == mu else vertices for axis in range(3)]
            for k in product(*mode_grids):
                om = sqrt(sum(omega[j]**2 for j in k))
                gam = 2 / a * asinh(a * om / 2)
                phi = e[k[0]][p[0]] * e[k[1]][p[1]] * v[k[2]][p[2]]
                coeff = (-omega[k[1]] if mu == 0 else omega[k[0]]) * phi * a**3
                time = {}
                for it in vertices:
                    lo, hi = sorted((it, p[3]))
                    time[it] = (a * sinh(gam * a * lo) * sinh(gam * a * (n-hi))
                                / (sinh(a*gam) * sinh(8*gam)))
                basis = [e[k[axis]] if axis == mu else v[k[axis]]
                         for axis in range(3)]
                for row in rows:
                    values[row] += (coeff * basis[0][row[0]] * basis[1][row[1]]
                                    * basis[2][row[2]] * time[row[3]])
            residuals = []
            max_residual = 0.0
            failures = []
            for row in rows:
                actual = 0.0
                for axis in range(4):
                    low, high = (0, n-1) if axis == mu else (1, n-1)
                    diag = 1 if axis == mu and row[axis] in (low, high) else 2
                    actual += diag * values[row]
                    for offset in (-1, 1):
                        near = list(row)
                        near[axis] += offset
                        if low <= near[axis] <= high:
                            actual -= values[tuple(near)]
                if mu == 0:
                    rhs = (int(row == (p[0], p[1], p[2], p[3]))
                           - int(row == (p[0], p[1]+1, p[2], p[3])))
                else:
                    rhs = (int(row == (p[0]+1, p[1], p[2], p[3]))
                           - int(row == (p[0], p[1], p[2], p[3])))
                error = abs(actual-rhs)
                max_residual = max(max_residual, error)
                record = {'edge_index': row, 'actual_LR': actual,
                          'required_C_transpose': rhs, 'absolute_error': error}
                residuals.append(record)
                if error > threshold:
                    failures.append(record)
            checks.append({'N': n, 'a': a, 'source_12_index': p,
                           'component': mu+1, 'rows': len(rows),
                           'normal_endpoint_rows': sum(row[mu] in (0, n-1) for row in rows),
                           'max_residual': max_residual, 'failures': failures,
                           'complete_residuals': residuals})
summary = {'passed': all(not c['failures'] for c in checks),
           'actual_max_residual': max(c['max_residual'] for c in checks),
           'required_upper_bound': threshold, 'checks': len(checks),
           'rows_checked': sum(c['rows'] for c in checks),
           'normal_endpoint_rows_checked': sum(c['normal_endpoint_rows'] for c in checks),
           'failure_count': sum(len(c['failures']) for c in checks),
           'not_verified': ['uniform asymptotic estimates', 'weighted Wilson contraction',
                            'distinct-line quartic response', 'mass gap']}
out = Path(__file__).with_name('insertion-kernel-certificate.json')
out.write_text(json.dumps({'summary': summary, 'checks': checks}, indent=2) + '\n')
print('PASS' if summary['passed'] else 'FAIL',
      'finite relative GC_12^* kernel, all selected column rows and normal endpoints')
print('Actual maximum residual:', summary['actual_max_residual'],
      '; required upper bound:', threshold)
print('Failures:', summary['failure_count'], '; rows:', summary['rows_checked'])
print('Full certificate:', out)
raise SystemExit(0 if summary['passed'] else 1)
