#!/usr/bin/env python3
"""Exact first-order necessary test only; no nonlinear branch solver."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import importlib.util
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'quadratic-tangent-certificate-1316.json'
source_py = HERE / 'quadratic-defect-1314.py'
spec = importlib.util.spec_from_file_location('polynomial1314', source_py)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)  # Definitions only; its main() is not invoked.
P, NAMES, ZERO = old.P, old.NAMES, old.ZERO


def diff(p, j):
    terms = {}
    for e, c in p.t.items():
        if e[j]:
            h = list(e)
            h[j] -= 1
            terms[tuple(h)] = c*e[j]
    return P(terms)


def at_base(p):
    # b1=1; b2=b3=b4=b5=t=0. A,...,E,u,v remain symbols.
    out = {}
    for e, c in p.t.items():
        if any(e[j] for j in (1, 2, 3, 4, 10)):
            continue
        h = list(e)
        h[0] = 0
        key = tuple(h)
        out[key] = out.get(key, F(0)) + c
    return P(out)


def constant(p):
    assert all(e == ZERO for e in p.t)
    return p.t.get(ZERO, F(0))


def rank_and_pivots(matrix):
    a = [list(map(F, row)) for row in matrix]
    pivots, i = [], 0
    for j in range(len(a[0])):
        pivot = next((k for k in range(i, len(a)) if a[k][j]), None)
        if pivot is None:
            continue
        a[i], a[pivot] = a[pivot], a[i]
        scale = a[i][j]
        a[i] = [x/scale for x in a[i]]
        for k in range(len(a)):
            if k != i:
                scale = a[k][j]
                a[k] = [x-scale*y for x, y in zip(a[k], a[i])]
        pivots.append(j)
        i += 1
        if i == len(a):
            break
    return len(pivots), pivots, [[str(x) for x in row] for row in a]


def determinant(matrix):
    a, det = [list(map(F, row)) for row in matrix], F(1)
    for j in range(len(a)):
        k = next((k for k in range(j, len(a)) if a[k][j]), None)
        if k is None:
            return F(0)
        if k != j:
            a[k], a[j] = a[j], a[k]
            det = -det
        p = a[j][j]
        det *= p
        for k in range(j+1, len(a)):
            q = a[k][j]/p
            for l in range(j, len(a)):
                a[k][l] -= q*a[j][l]
    return det


def main():
    xs = [old.var(i) for i in range(len(NAMES))]
    b = {j: xs[j-1] for j in range(1, 6)}
    A, B, C, D, E, t, u, v = xs[5:]
    bj = lambda k: b.get(k, P())
    q = {k: bj(k+1)+sum((bj(i)*bj(k-i) for i in range(1, 6)), P())/2
         for k in range(1, 11)}
    r = {k: bj(k+2)+sum((bj(i)*bj(k+1-i) for i in range(1, 6)), P())
         -b[1]*bj(k)+sum((bj(i)*bj(j)*bj(k-i-j)
                           for i in range(1, 6) for j in range(1, 6)), P())/3
         for k in range(1, 16)}
    columns = {1: b, 2: q, 3: r}
    order = ((1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3))
    d, moments = {1: P(1), 2: u, 3: v}, {2: A, 3: B, 4: C, 5: D, 6: E}
    h, target, residual = {}, {}, {}
    for m, n in order:
        key = f'{m},{n}'
        h[key] = P(F(1, m) if m == n else 0)-sum(
            (k*columns[m][k]*columns[n][k] for k in range(1, 5*min(m, n)+1)), P())
        target[key] = d[m]*d[n]*moments[m+n]
        residual[key] = h[key]-t*target[key]

    source_cert = HERE / 'quadratic-defect-certificate-1314.json'
    saved = json.loads(source_cert.read_text())
    checks = {
        'all_columns_match_1314': all(p.record() == saved['columns'][str(m)][str(k)]
                                    for m, col in columns.items() for k, p in col.items()),
        'all_six_full_residuals_match_1314': all(
            p.record() == saved['six_equation_residuals'][key] for key, p in residual.items())}
    keys = [f'{m},{n}' for m, n in order]
    jac_b = [[constant(at_base(diff(residual[key], j))) for j in range(5)] for key in keys]
    jac_weights = [[constant(at_base(diff(residual[key], j))) for j in (11, 12)] for key in keys]
    jac = [x+y for x, y in zip(jac_b, jac_weights)]
    rank, pivots, reduced = rank_and_pivots(jac)
    left = [-1, 0, -1, 1, 0, 0]
    left_products = [sum((left[i]*jac[i][j] for i in range(6)), F(0)) for j in range(7)]
    minor_rows = [0, 1, 2, 4, 5]
    minor = [[jac_b[i][j] for j in range(5)] for i in minor_rows]
    minor_det = determinant(minor)
    dt = [at_base(diff(residual[key], 10)) for key in keys]
    compatibility = C*u**2-A-C*v
    left_dt = sum((left[i]*dt[i] for i in range(6)), P())

    tangent = [-A/2, -u*B/2, -v*C/2, u*(B-v*D)/2, (A+v*C-v**2*E)/2]
    tangent_residuals = [sum((jac_b[i][j]*tangent[j] for j in range(5)), P())-target[key]
                         for i, key in enumerate(keys)]
    expected = [P(), P(), P(), -compatibility, P(), P()]

    # One exact feasible tangent: u0=400, v0=W/C; common denominator 2*C^2.
    # This is not a solution of the nonlinear equations at positive tau.
    W = 160000*C-A
    tangent_numerators = [-A*C**2, -400*B*C**2, -W*C**2,
                          400*B*C**2-400*W*D*C, -W**2*E+160000*C**3]
    rhs_scaled = [2*A*C**2, 800*B*C**2, 2*W*C**2,
                  320000*C**3, 800*W*D*C, 2*W**2*E]
    witness_residuals = [sum((jac_b[i][j]*tangent_numerators[j] for j in range(5)), P())
                         -rhs_scaled[i] for i in range(6)]
    boxes = {k: (F(vv['lower']), F(vv['upper']))
             for k, vv in saved['necessary_test']['outer_boxes'].items()}
    alo, ahi = boxes['2']
    clo, chi = boxes['4']
    qlo, qhi = alo/chi, ahi/clo
    vlo, vhi = 160000-qhi, 160000-qlo
    checks.update({
        'all_base_residuals_zero': all(not at_base(p).t for p in residual.values()),
        'weight_derivative_columns_zero': all(x == 0 for row in jac_weights for x in row),
        'b_and_weight_jacobian_rank_five': rank == 5 and pivots == list(range(5)),
        'five_by_five_minor_minus32': minor_det == -32,
        'sole_left_null_relation': all(x == 0 for x in left_products),
        'augmented_tau_left_relation_is_minus_compatibility': not (left_dt+compatibility).t,
        'general_tangent_residuals_exact': all(not (x-y).t for x, y in zip(tangent_residuals, expected)),
        'all_witness_cleared_tangent_residuals_zero': all(not x.t for x in witness_residuals),
        'all_five_boxes_strictly_positive': all(0 < lo <= hi for lo, hi in boxes.values()),
        'ratio_bounds': F(56064) < qlo <= qhi < F(56065),
        'finite_positive_witness_bounds': F(103935) < vlo <= vhi < F(103936)})
    failures = [key for key, ok in checks.items() if not ok]
    inputs = (source_py, source_cert)
    report = {
        'status': 'passed' if not failures else 'failed', 'failures': failures,
        'checks': checks, 'row_order': keys,
        'hashes': {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                   for path in (*inputs, Path(__file__))},
        'full_equation_residuals': {key: p.record() for key, p in residual.items()},
        'base_residuals': {key: at_base(p).record() for key, p in residual.items()},
        'jacobian': {
            'column_order': ['b1', 'b2', 'b3', 'b4', 'b5', 'u', 'v'],
            'matrix': [[str(x) for x in row] for row in jac],
            'tau_partial_column': [p.record() for p in dt],
            'rank': rank, 'pivots_zero_based': pivots, 'rref': reduced,
            'minor_rows_zero_based': minor_rows, 'minor': [[str(x) for x in row] for row in minor],
            'minor_determinant': str(minor_det), 'left_null_vector': left,
            'left_null_product': list(map(str, left_products)),
            'left_tau_product': left_dt.record(),
            'augmented_rank': '5 if C*u^2-A-C*v=0; otherwise 6'},
        'tangent': {
            'regularity_hypotheses': 'b is right differentiable at tau=0 with b(0)=(1,0,0,0,0); u,v have finite strictly positive limits',
            'compatibility': 'C*u0^2=A+C*v0; equivalently u0>sqrt(A/C), v0=u0^2-A/C',
            'generic_tangent': [p.record() for p in tangent],
            'all_six_residuals': [p.record() for p in tangent_residuals],
            'witness': {'u0': '400', 'v0': '(160000*C-A)/C',
                        'tangent_common_denominator': '2*C^2',
                        'tangent_numerators': [p.record() for p in tangent_numerators],
                        'all_six_scaled_rhs': [p.record() for p in rhs_scaled],
                        'all_six_cleared_residuals': [p.record() for p in witness_residuals]}},
        'bounds': {
            'input_boxes': {k: list(map(str, box)) for k, box in boxes.items()},
            'A_over_C': {'lower': str(qlo), 'upper': str(qhi), 'weaker_strict': '56064 < A/C < 56065'},
            'witness_v0': {'lower': str(vlo), 'upper': str(vhi), 'weaker_strict': '103935 < v0 < 103936'},
            'required_for_witness': 'A/C < 160000, C>0'},
        'decision': 'FIRST-ORDER COMPATIBLE ONLY; direct dependent-variable IFT is unavailable at this base',
        'limits': 'No actual branch, nonlinear existence, higher-order condition, univalence or Xi sign. Actual boxes retain L037/1307 contracts; no singular/unbounded branch excluded.'}
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print('Base residual=0; rank D_(b,u,v)F=5; nonzero 5x5 minor=-32.')
    print('Necessary and tangent-sufficient: C*u0^2=A+C*v0. Witness u0=400, v0=160000-A/C.')
    print('Actual bounds: 56064<A/C<56065, 103935<v0<103936; required A/C<160000, C>0.')
    print(f'First-order test passes only; branch existence unresolved. checks={len(checks)}, failures={failures}')
    print(f'Full certificate: {OUT.relative_to(ROOT)}')
    assert not failures


if __name__ == '__main__':
    main()
