"""Independent coefficient/quotient-ring and full-root-evidence replay.

Imports only budget accounting, not the producer or its arithmetic.
"""
import hashlib
import json
from fractions import Fraction as F
from quartic_field_budget import Budget, ROOT

CERT = ROOT / 'quartic-field-certificate.json'
OUT = ROOT / 'quartic-field-verification.json'


def main():
    budget = Budget()
    try:
        run(budget)
    finally:
        budget.save()


def run(budget):
    budget.phase('independent replay: Horner, mod 7, quotient rings, determinant')
    saved = json.loads(CERT.read_text())
    checks = {}
    def op(kind, a, b):
        return budget.op(kind, a, b)
    def check(name, a, b):
        checks[name] = budget.equal(a, b)
    def trim(a):
        while len(a) > 1 and budget.equal(a[-1], 0):
            a.pop()
        return budget.polynomial(a)
    def multiply(a, b):
        out = [F(0)] * (len(a)+len(b)-1)
        budget.polynomial(out)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i+j] = op('+', out[i+j], op('*', x, y))
        return trim(out)
    def remainder(a, modulus):
        a = trim(list(a))
        while len(a) >= len(modulus) and a != [0]:
            shift = op('-', len(a), len(modulus))
            scale = op('/', a[-1], modulus[-1])
            for i, c in enumerate(modulus):
                a[shift+i] = op('-', a[shift+i], op('*', scale, c))
            a = trim(a)
        return a
    def evaluate_poly(coeffs, value, modulus):
        out = [F(0)]
        for c in reversed(coeffs):
            out = remainder(multiply(out, value), modulus)
            out[0] = op('+', out[0], c)
            out = trim(out)
        return out
    q = budget.polynomial([F(7), F(52), F(-6), F(-64), F(-25)])
    f = budget.polynomial([op('/', c, -25) for c in q])
    g = budget.polynomial([F(-109375), F(-32500), F(150), F(64), F(1)])
    check('exact_input', list(map(F, saved['input_q4'])), q)
    check('monic_normalization', list(map(F, saved['monic_quartic'])), f)
    check('integral_model', list(map(F, saved['integral_absolute_polynomial'])), g)
    # Formula evaluated with different parenthesization from the producer.
    d, c, b, a, _ = f
    r = budget.polynomial([
        op('-', op('*', op('*', 4, b), d),
           op('+', op('*', op('*', a, a), d), op('*', c, c))),
        op('-', op('*', a, c), op('*', 4, d)), op('*', -1, b), F(1)])
    check('resolvent_formula', list(map(F, saved['resolvent'])), r)
    h = budget.polynomial([F(-43128), F(-2628), F(-6), F(1)])
    scale = F(1)
    transformed = []
    for coeff in reversed(r):
        transformed.append(op('*', coeff, scale))
        scale = op('*', scale, 25)
    check('scaled_resolvent_formula', list(reversed(transformed)), h)
    check('saved_scaled_resolvent', list(map(F, saved['scaled_resolvent'])), h)
    # Reconstruct divisor generation and compare ALL saved rejected candidates.
    divisors = set()
    scan = []
    t = 1
    while op('*', t, t) <= 43128:
        budget.charge('root_trials')
        residue = op('%', 43128, t)
        scan.append([t, residue])
        if budget.equal(residue, 0):
            divisors.add(t)
            divisors.add(op('//', 43128, t))
        t = op('+', t, 1)
    check('complete_divisor_scan', saved['divisor_scan'], scan)
    check('complete_positive_divisors', saved['positive_divisors'], sorted(divisors))
    expected_candidates = {op('*', sign, n) for n in divisors for sign in (-1, 1)}
    check('candidate_count', len(saved['integer_root_trials']), len(expected_candidates))
    actual_candidates = set()
    root_rows = []
    for index, (candidate, value) in enumerate(saved['integer_root_trials']):
        budget.charge('root_trials')
        actual_candidates.add(candidate)
        horner = F(0)
        for coeff in reversed(h):
            horner = op('+', op('*', horner, candidate), coeff)
        check('root_value_' + str(index), F(value), horner)
        check('root_nonzero_' + str(index), horner != 0, True)
        root_rows.append([candidate, str(horner)])
    check('complete_signed_candidates', actual_candidates, expected_candidates)
    check('saved_no_roots', saved['rational_resolvent_roots'], [])
    # Independent irreducibility-by-reduction certificate: cubic, no F7 roots.
    mod_rows = []
    mod_coeffs = [op('%', int(c), 7) for c in h]
    for candidate in range(7):
        budget.charge('root_trials')
        v = 0
        for coeff in reversed(mod_coeffs):
            v = op('%', op('+', op('*', v, candidate), coeff), 7)
        mod_rows.append([candidate, v])
        check('mod7_nonzero_' + str(candidate), v != 0, True)
    # Verify both field substitutions by actual quotient-ring arithmetic.
    alpha = budget.polynomial([F(0), F(25)])
    theta = budget.polynomial([F(0), F(1, 25)])
    check('saved_forward_map', list(map(F, saved['field_maps']['alpha_to_theta'])), alpha)
    check('saved_inverse_map', list(map(F, saved['field_maps']['theta_to_alpha'])), theta)
    relation_forward = evaluate_poly(g, alpha, f)
    relation_inverse = evaluate_poly(f, theta, g)
    check('forward_relation', relation_forward, [F(0)])
    check('inverse_relation', relation_inverse, [F(0)])
    check('saved_forward_coefficient_residual', list(map(F, saved['field_maps']['forward_relation_residual'])), [F(0)]*5)
    check('saved_inverse_coefficient_residual', list(map(F, saved['field_maps']['inverse_relation_residual'])), [F(0)]*5)
    check('theta_composition', evaluate_poly(alpha, theta, g), [F(0), F(1)])
    check('alpha_composition', evaluate_poly(theta, alpha, f), [F(0), F(1)])
    matrices = []
    for value, modulus in ((alpha, f), (theta, g)):
        columns = []
        term = [F(1)]
        for _ in range(4):
            columns.append(term + [F(0)]*(4-len(term)))
            term = remainder(multiply(term, value), modulus)
        matrices.append([[columns[j][i] for j in range(4)] for i in range(4)])
    check('full_basis_map', [[F(c) for c in row] for row in saved['field_maps']['basis_matrix']], matrices[0])
    check('full_inverse_basis_map', [[F(c) for c in row] for row in saved['field_maps']['inverse_basis_matrix']], matrices[1])
    # Generic elimination for determinant, rather than producer's diagonal product.
    m = [row[:] for row in matrices[0]]
    determinant = F(1)
    for col in range(4):
        pivot_row = next(i for i in range(col, 4) if not budget.equal(m[i][col], 0))
        if pivot_row != col:
            m[col], m[pivot_row] = m[pivot_row], m[col]
            determinant = op('*', -1, determinant)
        pivot = m[col][col]
        determinant = op('*', determinant, pivot)
        for row in range(col+1, 4):
            factor = op('/', m[row][col], pivot)
            for k in range(col, 4):
                m[row][k] = op('-', m[row][k], op('*', factor, m[col][k]))
    check('full_determinant', determinant, F(saved['field_maps']['basis_determinant']))
    check('nonzero_determinant', determinant != 0, True)
    for which in range(2):
        left, right = matrices[which], matrices[1-which]
        product = []
        for i in range(4):
            row = []
            for j in range(4):
                v = F(0)
                for k in range(4):
                    v = op('+', v, op('*', left[i][k], right[k][j]))
                check('composition_' + str((which, i, j)), v, F(int(i == j)))
                row.append(v)
            product.append(row)
        check('saved_composition_' + str(which),
              [[F(c) for c in row] for row in saved['field_maps']['compositions'][which]], product)
    check('height_input', F(saved['coefficient_heights']['input']), max(abs(c) for c in q))
    check('height_integral', F(saved['coefficient_heights']['integral_model']), max(abs(c) for c in g))
    # Every named producer check must have passed; mathematical claims replayed above.
    check('producer_failures', saved['failures'], [])
    check('producer_checks', all(saved['checks'].values()), True)
    result = dict(checks=checks, failures=[k for k, v in checks.items() if not v],
                  mod7_coefficients=mod_coeffs, mod7_all_root_trials=mod_rows,
                  full_integer_root_rows=root_rows,
                  relation_forward=relation_forward, relation_inverse=relation_inverse,
                  basis_matrices=matrices, determinant=determinant,
                  certificate_sha256=hashlib.sha256(CERT.read_bytes()).hexdigest(),
                  verifier_sha256=hashlib.sha256(__import__('pathlib').Path(__file__).read_bytes()).hexdigest(),
                  budget=budget.summary())
    OUT.write_text(json.dumps(result, indent=2, default=str) + '\n')
    budget.save()
    print(json.dumps(dict(checks=len(checks), failures=result['failures'],
                          mod7_all_root_trials=mod_rows, budget=budget.summary(),
                          verification=str(OUT)), default=str))
    if result['failures']:
        raise RuntimeError('Independent replay failures')


if __name__ == '__main__':
    main()
