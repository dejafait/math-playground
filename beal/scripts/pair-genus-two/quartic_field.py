"""Approved exact-instance quartic resolvent and field-map producer."""
import hashlib
import json
import argparse
from fractions import Fraction as F
from pathlib import Path
from quartic_field_budget import Budget, ROOT

OUT = ROOT / 'quartic-field-certificate.json'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--resume-ledger', action='store_true',
                        help='Explicitly retain all earlier charges after a code repair')
    args = parser.parse_args()
    budget = Budget(fresh=not args.resume_ledger)
    try:
        run(budget)
    except Exception as error:
        budget.data.setdefault('execution_errors', []).append(repr(error))
        raise
    finally:
        budget.save()


def run(budget):
    budget.phase('producer: normalization, resolvent, complete divisor test, field maps')
    checks = {}
    add = lambda a, b: budget.op('+', a, b)
    sub = lambda a, b: budget.op('-', a, b)
    mul = lambda a, b: budget.op('*', a, b)
    div = lambda a, b: budget.op('/', a, b)

    def power(a, n):
        out = F(1)
        for _ in range(n):
            out = mul(out, a)
        return out

    def same(name, actual, expected):
        checks[name] = budget.equal(actual, expected)

    q = budget.polynomial([7, 52, -6, -64, -25])
    monic = budget.polynomial([div(c, q[-1]) for c in q])
    d, c, b, a, _ = monic
    # Conrad's equation (3.7), in ascending order.
    resolvent = budget.polynomial([
        sub(0, sub(add(mul(power(a, 2), d), power(c, 2)), mul(4, mul(b, d)))),
        sub(mul(a, c), mul(4, d)), sub(0, b), F(1)])
    # H(Y)=25^3 R(Y/25); this is monic integral, hence primitive.
    h = budget.polynomial([mul(v, power(25, 3-i))
                           for i, v in enumerate(resolvent)])
    same('scaled_resolvent', h, [F(-43128), F(-2628), F(-6), F(1)])
    same('monic_integral', [v.denominator for v in h], [1, 1, 1, 1])
    # Exhaust the integer divisors, including rejected generating candidates.
    constant = sub(0, int(h[0]))
    budget.observe(constant)
    scan = []
    divisors = []
    t = 1
    # No isqrt shortcut: the stopping square and every division are charged.
    while not budget.equal(mul(t, t) > constant, True):
        budget.charge('root_trials')
        rem = budget.op('%', constant, t)
        scan.append([t, rem])
        if budget.equal(rem, 0):
            other = budget.op('//', constant, t)
            divisors.append(t)
            if not budget.equal(t, other):
                divisors.append(other)
        t = add(t, 1)
    divisors.sort()
    root_rows = []
    roots = []
    # Deliberately use power-sum evaluation, unlike replay's Horner scheme.
    for n in divisors:
        for sign in (-1, 1):
            budget.charge('root_trials')
            candidate = mul(sign, n)
            value = F(0)
            for i, coeff in enumerate(h):
                value = add(value, mul(coeff, power(candidate, i)))
            root_rows.append([candidate, int(value)])
            if budget.equal(value, 0):
                roots.append(candidate)
                budget.charge('resolvent_root_branches')
    same('no_rational_roots', roots, [])
    # This certificate implements the irreducible-resolvent branch only.
    # Stop rather than silently omit factor/tower cases if there is a root.
    if roots:
        raise RuntimeError('Rational-root branch requires approved exceptional-case construction')
    # alpha=25 theta gives an integral monic polynomial, not a height saving.
    g = budget.polynomial([mul(v, power(25, 4-i)) for i, v in enumerate(monic)])
    same('integral_absolute_polynomial', g,
         [F(-109375), F(-32500), F(150), F(64), F(1)])
    # Substitution residuals are checked coefficientwise before quotienting.
    forward = budget.polynomial([sub(mul(v, power(25, i)),
                                      mul(power(25, 4), monic[i]))
                                  for i, v in enumerate(g)])
    reverse = budget.polynomial([sub(mul(v, power(F(1, 25), i)),
                                      div(g[i], power(25, 4)))
                                  for i, v in enumerate(monic)])
    same('g_25theta_equals_25power4_f', forward, [F(0)]*5)
    same('f_alpha_over25_equals_g_over25power4', reverse, [F(0)]*5)
    matrix = []
    inverse_matrix = []
    for row in range(4):
        matrix.append([power(25, col) if budget.equal(row, col) else F(0)
                       for col in range(4)])
        inverse_matrix.append([power(F(1, 25), col) if budget.equal(row, col)
                               else F(0) for col in range(4)])
    determinant = F(1)
    for i in range(4):
        determinant = mul(determinant, matrix[i][i])
    products = []
    for left, right in ((matrix, inverse_matrix), (inverse_matrix, matrix)):
        product = []
        for i in range(4):
            row = []
            for j in range(4):
                total = F(0)
                for k in range(4):
                    total = add(total, mul(left[i][k], right[k][j]))
                row.append(total)
            product.append(row)
        products.append(product)
    for i, product in enumerate(products):
        same('basis_composition_' + str(i), product,
             [[F(int(j == k)) for k in range(4)] for j in range(4)])
    same('basis_determinant_nonzero', determinant != 0, True)
    heights = dict(input=max(abs(v) for v in q),
                   integral_model=max(abs(v) for v in g))
    budget.observe(*heights.values())
    same('no_height_saving_from_scaling', heights['integral_model'] < heights['input'], False)
    result = dict(
        input_q4=q, monic_quartic=monic, resolvent=resolvent,
        scaled_resolvent=h, scaling='Y=25r; H(Y)=25^3 R(Y/25)',
        divisor_scan=scan, positive_divisors=divisors,
        integer_root_trials=root_rows, rational_resolvent_roots=roots,
        integral_absolute_polynomial=g,
        field_maps=dict(alpha_to_theta=[0, 25], theta_to_alpha=['0', '1/25'],
                        forward_relation_residual=forward,
                        inverse_relation_residual=reverse,
                        basis_matrix=matrix, inverse_basis_matrix=inverse_matrix,
                        basis_determinant=determinant, compositions=products),
        coefficient_heights=heights,
        conclusion='No quadratic subfield; no quadratic tower over Q',
        checks=checks, failures=[name for name, passed in checks.items() if not passed],
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        budget=budget.summary())
    OUT.write_text(json.dumps(result, indent=2, default=str) + '\n')
    budget.save()
    print(json.dumps(dict(result=result['conclusion'], root_trials=len(root_rows),
                          failures=result['failures'], heights=heights,
                          budget=budget.summary(), certificate=str(OUT)), default=str))
    if result['failures']:
        raise RuntimeError('Failed producer checks')


if __name__ == '__main__':
    main()
