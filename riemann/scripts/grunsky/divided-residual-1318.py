#!/usr/bin/env python3
"""One exact fixed-u divided-residual/ordinary-IFT hypothesis check.

No higher-order branch expansion, weight sweep or univalence test.
The complete quotient is retained; actual boxes are inherited, not recomputed.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'divided-residual-certificate-1318.json'
ENGINE = HERE / 'quadratic-defect-1314.py'
spec = importlib.util.spec_from_file_location('polynomial1318', ENGINE)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)  # Definitions only; no earlier main() invocation.
P, ZERO = old.P, old.ZERO
NAMES = ('a1', 'a2', 'a3', 'a4', 'a5', 'A', 'B', 'C', 'D', 'E', 'tau', 'u', 'v')


def record(p):
    return [{'powers': {name: k for name, k in zip(NAMES, e) if k},
             'coefficient': str(c)} for e, c in sorted(p.t.items())]


def read_polynomial(rows):
    terms = {}
    for row in rows:
        e = tuple(row['powers'].get(name, 0) for name in old.NAMES)
        assert e not in terms
        terms[e] = Q(row['coefficient'])
    return P(terms)


def substitute(p, replacements):
    out = P()
    for e, c in p.t.items():
        term = P(c)
        for j, exponent in enumerate(e):
            if exponent:
                term = term*replacements[j]**exponent
        out = out+term
    return out


def diff(p, j):
    out = {}
    for e, c in p.t.items():
        if e[j]:
            f = list(e)
            f[j] -= 1
            out[tuple(f)] = c*e[j]
    return P(out)


def tau_coefficient(p, degree):
    out = {}
    for e, c in p.t.items():
        if e[10] == degree:
            f = list(e)
            f[10] = 0
            out[tuple(f)] = c
    return P(out)


def divide_tau(p):
    # Return the exact quotient and the entire zero-slice remainder.
    out = {}
    for e, c in p.t.items():
        if e[10]:
            f = list(e)
            f[10] -= 1
            out[tuple(f)] = c
    return P(out), tau_coefficient(p, 0)


def determinant(matrix):
    if not matrix:
        return P(1)
    out = P()
    for j, entry in enumerate(matrix[0]):
        if entry.t:
            minor = [row[:j]+row[j+1:] for row in matrix[1:]]
            out = out+(-1)**j*entry*determinant(minor)
    return out


def main():
    xs = [old.var(j) for j in range(len(NAMES))]
    a = xs[:5]
    A, B, C, D, E, tau, _, v = xs[5:]
    replacements = [P(1)+tau*a[0], *[tau*x for x in a[1:]],
                    A, B, C, D, E, tau, P(400), v]
    source_cert = HERE / 'quadratic-defect-certificate-1314.json'
    tangent_cert = HERE / 'quadratic-tangent-certificate-1316.json'
    saved = json.loads(source_cert.read_text())
    tangent_saved = json.loads(tangent_cert.read_text())
    keys = ('1,1', '1,2', '1,3', '2,2', '2,3', '3,3')
    numerator = [substitute(read_polynomial(saved['six_equation_residuals'][key]), replacements)
                 for key in keys]

    # Reconstruct from the complete-column convolution formulas independently
    # of the saved expanded residuals, including every support entry.
    b = {j: replacements[j-1] for j in range(1, 6)}
    bj = lambda k: b.get(k, P())
    q = {k: bj(k+1)+sum((bj(i)*bj(k-i) for i in range(1, 6)), P())/2
         for k in range(1, 11)}
    r = {k: bj(k+2)+sum((bj(i)*bj(k+1-i) for i in range(1, 6)), P())
         -b[1]*bj(k)+sum((bj(i)*bj(j)*bj(k-i-j)
                           for i in range(1, 6) for j in range(1, 6)), P())/3
         for k in range(1, 16)}
    columns = {1: b, 2: q, 3: r}
    target = [A, 400*B, v*C, 160000*C, 400*v*D, v**2*E]
    direct = []
    for key, rhs in zip(keys, target):
        m, n = map(int, key.split(','))
        h = P(Q(1, m) if m == n else 0)-sum(
            (k*columns[m][k]*columns[n][k] for k in range(1, 5*min(m, n)+1)), P())
        direct.append(h-tau*rhs)

    divided = [divide_tau(p) for p in numerator]
    quotient = [entry[0] for entry in divided]
    zero_slice = [entry[1] for entry in divided]
    reconstruction = [p-tau*g for p, g in zip(numerator, quotient)]
    g0 = [tau_coefficient(g, 0) for g in quotient]
    expected = [-2*a[0]-A, -2*a[1]-400*B, -2*a[2]-v*C,
                -2*(a[0]+a[2])-160000*C,
                -2*(a[1]+a[3])-400*v*D,
                -2*(a[0]+a[2]+a[4])-v**2*E]
    derivative = [[diff(p, j) for j in (0, 1, 2, 3, 4, 12)] for p in g0]
    det = determinant(derivative)
    left = [-1, 0, -1, 1, 0, 0]
    left_product = [sum((left[i]*derivative[i][j] for i in range(6)), P())
                    for j in range(6)]

    # Verify the proposed base exactly, clearing only the known positive C.
    # All a_j use denominator denom=2*C^2; v0=W/C.
    W, denom = 160000*C-A, 2*C**2
    nums = [-A*C**2, -400*B*C**2, -W*C**2,
            400*B*C**2-400*W*D*C, -W**2*E+160000*C**3]
    rhs_scaled = [2*A*C**2, 800*B*C**2, 2*W*C**2,
                  320000*C**3, 800*W*D*C, 2*W**2*E]
    # g0 is linear in a, and has precisely the displayed quadratic target in v.
    jac_b = [[Q(entry.t.get(ZERO, 0)) for entry in row[:5]] for row in derivative]
    assert all(not (entry-P(value)).t for row, values in zip(derivative, jac_b)
               for entry, value in zip(row[:5], values))
    base_residuals = [sum((jac_b[i][j]*nums[j] for j in range(5)), P())-rhs_scaled[i]
                      for i in range(6)]
    boxes = {k: tuple(map(Q, vv)) for k, vv in tangent_saved['bounds']['input_boxes'].items()}
    alo, ahi = boxes['2']
    clo, chi = boxes['4']
    ratio_lo, ratio_hi = alo/chi, ahi/clo
    vlo, vhi = 160000-ratio_hi, 160000-ratio_lo
    det_lo, det_hi = -32*chi, -32*clo
    checks = {
        'complete_columns_match_saved_full_residuals': all(not (p-q).t for p, q in zip(numerator, direct)),
        'whole_zero_slice_vanishes_identically': all(not p.t for p in zero_slice),
        'exact_polynomial_reconstruction_all_six': all(not p.t for p in reconstruction),
        'all_six_quotient_zero_slice_formulas': all(not (p-q).t for p, q in zip(g0, expected)),
        'quotient_uses_only_allowed_variables': all(not e[11] for p in quotient for e in p.t),
        'base_numerators_match_1316': all(p.record() == row for p, row in zip(
            nums, tangent_saved['tangent']['witness']['tangent_numerators'])),
        'all_six_cleared_quotient_base_residuals_zero': all(not p.t for p in base_residuals),
        'dependent_determinant_exactly_minus32C': not (det+32*C).t,
        'left_product_exactly_00000C': all(not (p-(C if j == 5 else P())).t
                                         for j, p in enumerate(left_product)),
        'fixed_boxes_match_1314': all(boxes[k] == (Q(vv['lower']), Q(vv['upper']))
                                    for k, vv in saved['necessary_test']['outer_boxes'].items()),
        'all_five_input_boxes_strictly_positive': all(0 < lo <= hi for lo, hi in boxes.values()),
        'actual_ratio_and_positive_v0_bounds': Q(56064) < ratio_lo <= ratio_hi < Q(56065)
            and Q(103935) < vlo <= vhi < Q(103936),
        'actual_determinant_bounds_exclude_zero': det_lo <= det_hi < 0,
    }
    failures = [key for key, ok in checks.items() if not ok]
    report = {
        'status': 'passed' if not failures else 'failed', 'failures': failures,
        'checks': checks, 'row_order': list(keys), 'variables': list(NAMES),
        'input_hashes': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in (ENGINE, source_cert, tangent_cert, Path(__file__))},
        'substitution': 'b=(1+tau*a1,tau*a2,tau*a3,tau*a4,tau*a5); u=400',
        'full_substituted_numerators': [record(p) for p in numerator],
        'complete_quotient_polynomials': [record(p) for p in quotient],
        'zero_slice_remainders': [record(p) for p in zero_slice],
        'reconstruction_residuals': [record(p) for p in reconstruction],
        'quotient_zero_slice': [record(p) for p in g0],
        'base': {'v0': '(160000*C-A)/C', 'a_common_denominator': record(denom),
                 'a_numerators': [record(p) for p in nums],
                 'target_times_denominator_at_v0': [record(p) for p in rhs_scaled],
                 'all_six_cleared_quotient_residuals': [record(p) for p in base_residuals],
                 'denominator_guard': '2*C^2>0 since C>0'},
        'derivative': {'columns': ['a1', 'a2', 'a3', 'a4', 'a5', 'v'],
                       'matrix_on_zero_slice': [[record(p) for p in row] for row in derivative],
                       'determinant': record(det), 'left_vector': left,
                       'left_product': [record(p) for p in left_product]},
        'bounds': {'input_boxes': {k: list(map(str, box)) for k, box in boxes.items()},
                   'A_over_C': list(map(str, (ratio_lo, ratio_hi))),
                   'v0': list(map(str, (vlo, vhi))),
                   'determinant': list(map(str, (det_lo, det_hi))),
                   'required': 'C>0, A/C<160000; dependent determinant nonzero'},
        'theorem_application': 'Polynomial G is C1 on an open real neighborhood; verified base zero and det=-32C!=0 permit de Oliveira Section3 Theorem2. Continuity retains positive v for sufficiently small positive tau.',
        'decision': 'ALL FIXED DIVIDED-SYSTEM IFT HYPOTHESES PASS; local C1 finite matching branch',
        'limits': 'Qualitative existence only; no effective tau radius, pole exclusion, unit-disk univalence, whole-family branch classification, actual-block sign or RH. Actual inputs retain inherited arithmetic contracts.'}
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print('Whole zero slice=0; exact polynomial quotient; quotient base residuals=0 (six each).')
    print('Dependent derivative det=-32*C, required !=0; C>0 from inherited boxes.')
    print(f'Actual determinant in [{det_lo}, {det_hi}] <0; 103935<v0<103936, required v0>0.')
    print(f'Ordinary-IFT hypotheses pass; qualitative branch only. checks={len(checks)}, failures={failures}')
    print(f'Full certificate: {OUT.relative_to(ROOT)}')
    assert not failures


if __name__ == '__main__':
    main()
