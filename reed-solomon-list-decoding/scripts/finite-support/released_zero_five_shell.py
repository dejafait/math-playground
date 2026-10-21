"""Gate-approved shell without the incidence zero: bounded LP and exact certificates.

Decimal simplex proposes a basis only; all reported bounds are rational.
No output overwrites the fixed-trial certificates.
"""
import json
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from conditioned_five_shell import factor
from delsarte_lp import solve_exact

ROOT = Path(__file__).parent
OUT = ROOT / 'released-zero-five-shell-results.json'


def enc(z):
    z = Q(z)
    return [z.numerator, z.denominator]


def main():
    saved = json.loads((ROOT / 'selected-triple-sdp-results.json').read_text())
    p = [Q(*z) for z in saved['p']]
    assert p[0] == 1 and p[1:5] == [0]*4 and p[5] > 0
    relations = [(r, q) for r in range(6) for q in range(6)
                 if r+q >= 5]
    modes = [(a, b) for a in range(6) for b in range(6) if (a, b) != (0, 0)]
    E, F = factor(68), factor(956)
    val = [E[0][r]*F[0][q] for r, q in relations]
    A = [[-Q(E[a][r]*F[b][q], v) for (r, q), v in zip(relations, val)]
         for a, b in modes]
    m, n = len(modes), len(relations)
    basis = list(range(n, n+m))
    trace = []
    with localcontext() as ctx:
        ctx.prec = 140
        dec = lambda z: Decimal(z.numerator)/Decimal(z.denominator)
        tab = [[dec(z) for z in row]+[Decimal(int(i == j)) for j in range(m)]
               +[Decimal(1)] for i, row in enumerate(A)]
        tab.append([-Decimal(1)]*n+[Decimal(0)]*(m+1))
        eps = Decimal('1e-100')
        status = 'iteration_limit'
        for iteration in range(600):
            entering = next((j for j, z in enumerate(tab[-1][:-1]) if z < -eps), None)
            if entering is None:
                status = 'decimal_optimal'
                break
            options = [(row[-1]/row[entering], basis[i], i)
                       for i, row in enumerate(tab[:-1]) if row[entering] > eps]
            if not options:
                status = 'decimal_unbounded_or_scaling_failure'
                break
            _, old, leaving = min(options)
            pivot = tab[leaving][entering]
            tab[leaving] = [z/pivot for z in tab[leaving]]
            for i in range(m+1):
                if i != leaving:
                    scale = tab[i][entering]
                    if scale:
                        tab[i] = [z-scale*t for z, t in zip(tab[i], tab[leaving])]
                        tab[i][entering] = Decimal(0)
            basis[leaving] = entering
            trace.append({'entering': entering, 'leaving': old})
    columns = sorted(j for j in basis if j < n)
    rows = [i for i in range(m) if n+i not in basis]
    matrix = [[A[i][j] for j in columns] for i in rows]
    xsmall = solve_exact(matrix, [Q(1)]*len(rows))
    ysmall = solve_exact(list(map(list, zip(*matrix))), [Q(1)]*len(columns))
    x, y = [Q(0)]*n, [Q(0)]*m
    for j, z in zip(columns, xsmall):
        x[j] = z
    for i, z in zip(rows, ysmall):
        y[i] = z
    ps = [1-sum(a*z for a, z in zip(row, x)) for row in A]
    ds = [sum(y[i]*A[i][j] for i in range(m))-1 for j in range(n)]
    value = sum(x)
    size = comb(68, 5)*comb(956, 5)
    required = size*p[5]
    exact = {'primal': list(map(enc, x)), 'dual': list(map(enc, y)),
             'primal_slacks': list(map(enc, ps)), 'dual_slacks': list(map(enc, ds)),
             'primal_nonnegative': all(z >= 0 for z in x),
             'dual_nonnegative': all(z >= 0 for z in y),
             'primal_feasible': all(z >= 0 for z in x+ps),
             'dual_feasible': all(z >= 0 for z in y+ds),
             'equal_objectives': value == sum(y),
             'row_sum': enc(1+value), 'required_row_sum': enc(required)}
    valid = exact['primal_feasible'] and exact['dual_feasible'] and exact['equal_objectives']
    data = {'parameters': {'p': list(map(enc, p)), 'shell_size': size,
                           'relations': relations, 'modes': modes, 'valencies': val},
            'matrix': [[enc(z) for z in row] for row in A],
            'discovery': {'status': status, 'pivot_count': len(trace), 'basis': basis,
                          'active_rows': rows, 'active_columns': columns, 'trace': trace},
            'exact': exact, 'summary': {'shell_lp_verified': valid,
                                      'shell_excludes': valid and 1+value < required,
                                      'shell_verdict': 'EXCLUDED' if valid and 1+value < required else 'FEASIBLE' if valid else 'UNRESOLVED'},
            'failures': [] if valid else ['rational shell LP validation failed']}
    OUT.write_text(json.dumps(data, separators=(',', ':'))+'\n')
    print('Shell modes/required: 35/35 nonconstant, plus constant Schur test')
    print('Discovery:', status, '; pivots:', len(trace), '/ <=600')
    print('Exact primal/dual/equal:', exact['primal_feasible'], exact['dual_feasible'], exact['equal_objectives'])
    print('Shell row sum actual/required:', 1+value, '/', required)
    print('Shell excludes:', data['summary']['shell_excludes'], '; shell:', data['summary']['shell_verdict'])
    print('Failures:', len(data['failures']), '; certificate:', OUT)


if __name__ == '__main__':
    main()
