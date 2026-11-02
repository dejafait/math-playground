"""Exact finite checks of L651 against complete grid interpolation.

No angular quadrature, spatial tail cutoff, or claim of a uniform lower
response bound. Import arithmetic definitions only; do not run old drivers.
"""
import ast
from pathlib import Path

helper = Path(__file__).with_name('common-polynomial-grid-certificate.py')
tree = ast.parse(helper.read_text(), filename=str(helper))
definitions = []
for node in tree.body:
    if (isinstance(node, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == 'cases' for t in node.targets)):
        break
    definitions.append(node)
else:
    raise RuntimeError('Expected helper driver boundary was not found')
exec(compile(ast.Module(body=definitions, type_ignores=[]), str(helper), 'exec'))


def power(z, k):
    return product([z]*k)


def dot(v, w):
    return sum((a.conjugate()*b for a, b in zip(v, w)), ZERO)


def positive_pivots(matrix):
    rows = [[G.cast(v) for v in row] for row in matrix]
    pivots = []
    for k in range(len(rows)):
        pivot = rows[k][k]
        pivots.append(pivot)
        if pivot.im != 0 or pivot.re <= 0:
            return False, pivots
        for i in range(k+1, len(rows)):
            for j in range(k+1, len(rows)):
                rows[i][j] -= rows[i][k]*rows[k][j]/pivot
    return True, pivots


def joint_case(n, u, poles, rs, close_pair=False):
    mass = sum(rs)
    ts = [F(j, n) for j in range(n)]
    grid = [t*u/R for t in ts]
    numerator, denominator = root_poly(grid), [ONE]
    for beta in grid:
        denominator = mul(denominator, [ONE, -beta.conjugate()])
    # Taylor division is exact through degree mass. No infinite tail is used.
    beta_coeffs = []
    for k in range(mass+1):
        val = numerator[k] if k < len(numerator) else ZERO
        val -= sum((denominator[j]*beta_coeffs[k-j]
                    for j in range(1, min(k, len(denominator)-1)+1)), ZERO)
        beta_coeffs.append(val)
    loss = [[beta_coeffs[k-j] if k >= j else ZERO
             for k in range(mass)] for j in range(mass)]
    gram_tail = [[G.cast(int(j == k)) -
                  sum((loss[i][j].conjugate()*loss[i][k]
                       for i in range(mass)), ZERO)
                  for k in range(mass)] for j in range(mass)]
    grid_gram = [[G(1/(1-ti*tj/U)) for tj in ts] for ti in ts]
    # These are values of the full rational d_k in K_b, not grid prefixes.
    dual_values = []
    for k in range(mass):
        vals = [beta_coeffs[k+1]]
        vals += [-sum((beta_coeffs[ell]/power(z, k+1-ell)
                       for ell in range(k+1)), ZERO) for z in grid[1:]]
        dual_values.append(vals)
    dual_grid_coeffs = [solve(grid_gram, vals) for vals in dual_values]
    gram_grid = [[dot(dual_values[j], dual_grid_coeffs[k])
                  for k in range(mass)] for j in range(mass)]
    B = lambda z: product(R*(z-R*beta)/(U-R*beta.conjugate()*z)
                          for beta in grid)
    L = lambda z: sum((r/(z-a) for a, r in zip(poles, rs)), ZERO)
    bx = B(x)
    weights = [bx/B(a) for a in poles]
    f_values = [bx*L(R*z) for z in grid]
    f_grid_coeffs = solve(grid_gram, f_values)
    response_grid = [dot(vals, f_grid_coeffs) for vals in dual_values]
    h = [sum((r*power(a/R, k)/R for a, r in zip(poles, rs)), ZERO)
         for k in range(mass)]
    c = [sum((r*w*power(a/R, k)/R
              for a, r, w in zip(poles, rs, weights)), ZERO)
         for k in range(mass)]
    correction = [bx*sum((loss[j][k].conjugate()*h[j]
                         for j in range(mass)), ZERO) for k in range(mass)]
    response_formula = [v-w for v, w in zip(correction, c)]
    response_norm = dot(response_grid, response_grid)
    projection_coeffs = solve(gram_grid, response_grid)
    projection_energy = dot(response_grid, projection_coeffs)
    full_energy = dot(f_values, f_grid_coeffs)
    full_energy_residue = (kernel_norm(poles, [r*w for r, w in zip(rs, weights)])
                          - bx.abs_squared()*kernel_norm(poles, [G(r) for r in rs]))
    gram_differences = [[gram_grid[j][k]-gram_tail[j][k]
                         for k in range(mass)] for j in range(mass)]
    response_differences = [v-w for v, w in zip(response_grid, response_formula)]
    lower_gram = [[gram_grid[j][k]-G(F(5, 13)*int(j == k))
                   for k in range(mass)] for j in range(mass)]
    gram_positive, pivots = positive_pivots(lower_gram)
    real_betas = [beta_coeffs[k]/power(u, n-k) for k in range(mass)]
    actual_l1 = sum((abs(v.re) for v in real_betas), F(0))
    required_l1 = F(2**mass)*F(19, 26)**n
    checks = {
        'admissible': (n >= 5 and mass <= F(n, 3) and x in poles
                       and len(set(poles)) == len(poles) and u.abs_squared() == 1
                       and all(isinstance(r, int) and r > 0 for r in rs)
                       and all(a.re == x.re and a.abs_squared() <= F(273, 200)**2
                               for a in poles)),
        'zero_constant_coefficient': beta_coeffs[0] == ZERO,
        'all_gram_entries_match': all(v == ZERO for row in gram_differences for v in row),
        'all_response_entries_match': all(v == ZERO for v in response_differences),
        'gram_lower_5_over_13': gram_positive,
        'full_energy_matches_residue_split': full_energy == full_energy_residue,
        'energies_real_nonnegative': all(v.im == 0 and v.re >= 0 for v in
                                         [response_norm, projection_energy, full_energy]),
        'joint_energy_lower_response': projection_energy.re >= response_norm.re,
        'joint_energy_upper_response': projection_energy.re <= F(13, 5)*response_norm.re,
        'joint_energy_below_full': projection_energy.re <= full_energy.re,
        'rotated_coefficients_real': all(v.im == 0 for v in real_betas),
        'all_cauchy_coefficient_bounds': all(beta_coeffs[k].abs_squared() <=
                                            (F(2**k)*F(19, 26)**n)**2
                                            for k in range(mass)),
        'loss_l1_bound': actual_l1 <= required_l1,
        'correction_bound': dot(correction, correction).re <=
                            F(mass*mass)*F(5000, 137)*required_l1**2,
        'constant_dual_unit_norm': gram_grid[0][0] == ONE,
        'constant_dual_response': response_grid[0] == -c[0],
    }
    pair_data = None
    if close_pair:
        a = poles[1]
        sx = [-a/(x-a), G(R)/(x-a)]
        sa = [-x/(a-x), G(R)/(a-x)]
        sums = [sx[k]+sa[k] for k in range(2)]
        pair_response = sum((sums[k]*response_grid[k] for k in range(2)), ZERO)
        checks['close_pair_sum_polynomial_one'] = sums == [ONE, ZERO]
        checks['close_pair_sum_unit_norm'] = gram_grid[0][0] == ONE
        checks['close_pair_sum_response'] = pair_response == -(1+weights[1])/R
        pair_data = {'s_x': sx, 's_a': sa, 'sum': sums,
                     'sum_norm_squared': gram_grid[0][0], 'sum_response': pair_response}
    return {
        'n': n, 'u': u, 'poles': poles, 'residues': rs, 'mass': mass,
        'beta_coefficients': beta_coeffs, 'loss_matrix': loss,
        'complete_grid_gram': grid_gram, 'dual_grid_values': dual_values,
        'dual_grid_coefficients': dual_grid_coeffs,
        'F_grid_values': f_values, 'F_grid_coefficients': f_grid_coeffs,
        'joint_gram_from_grid': gram_grid, 'joint_gram_from_loss': gram_tail,
        'response_from_grid': response_grid, 'response_from_moments': response_formula,
        'correction': correction, 'first_moments': c,
        'projection_coefficients': projection_coeffs,
        'joint_projection_energy': projection_energy, 'full_retained_energy': full_energy,
        'response_norm_squared': response_norm, 'lower_gram_pivots': pivots,
        'close_pair': pair_data,
        'verification': {'checks': checks, 'gram_differences': gram_differences,
                         'response_differences': response_differences,
                         'full_energy_difference': full_energy-full_energy_residue,
                         'actual_loss_l1': actual_l1, 'required_loss_l1_upper': required_l1,
                         'required_identity_error': '0'},
    }


cases = [
    joint_case(5, G(F(-1)), [x], [1]),
    joint_case(6, ONE, [x, x+G(F(0), F(1, 2**6))], [1, 1], True),
    joint_case(10, G(F(3, 5), F(4, 5)),
               [x, x+G(F(0), F(1, 2**10))], [1, 1], True),
    joint_case(9, G(F(3, 5), F(-4, 5)), [x, x+G(F(0), F(-1, 3))], [2, 1]),
    joint_case(9, G(F(0), F(1)),
               [x, x+G(F(0), F(1, 3)), x+G(F(0), F(-1, 4))], [1, 1, 1]),
    joint_case(12, G(F(3, 5), F(4, 5)),
               [x, x+G(F(0), F(1, 2)), x+G(F(0), F(-1, 3)),
                x+G(F(0), F(1, 5))], [1, 1, 1, 1]),
]
failures = [{'case': i, 'check': name}
            for i, c in enumerate(cases)
            for name, passed in c['verification']['checks'].items() if not passed]
summary = {
    'cases': len(cases),
    'checks': sum(len(c['verification']['checks']) for c in cases),
    'actual_identity_error': '0' if not failures else 'FAILED',
    'required_identity_error': '0', 'failures': failures,
    'analytic_loss_exponent_lower': F(643, 8788),
    'required_loss_exponent_for_stated_bound': F(1, 16),
    'uniform_gram_lower': F(5, 13), 'uniform_gram_upper': F(1),
    'target_squared_rate': F(1, 16), 'target_response_lower_bound_proved': False,
    'scope': 'Exact finite normalization checks; uniform conditioning proof is L651. '
             'No uniform response bound or angular quadrature.',
}
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(encode({'summary': summary, 'cases': cases}), indent=2)+'\n')
print(json.dumps(encode({**summary, 'certificate': str(output)}), sort_keys=True))
if failures:
    raise SystemExit(1)
