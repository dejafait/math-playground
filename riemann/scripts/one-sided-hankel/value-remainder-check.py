"""Exact normalization checks for L653, not an angular quadrature proof.

Read the established Gaussian-rational/full-grid helpers without running
their old drivers. Save complete evidence; print only bounds and failures.
"""
import ast
from pathlib import Path

helper = Path(__file__).with_name('joint-polynomial-gram-check.py')
tree = ast.parse(helper.read_text(), filename=str(helper))
definitions = []
for node in tree.body:
    if (isinstance(node, ast.Assign) and
            any(isinstance(t, ast.Name) and t.id == 'cases' for t in node.targets)):
        break
    definitions.append(node)
else:
    raise RuntimeError('Expected joint helper driver boundary was not found')
exec(compile(ast.Module(body=definitions, type_ignores=[]), str(helper), 'exec'))


def evaluate(poly, z):
    out = ZERO
    for c in reversed(poly):
        out = out*z+c
    return out


def value_case(n, u, poles, residues):
    base = joint_case(n, u, poles, residues)
    count, mass = len(poles), sum(residues)
    ts = [F(j, n) for j in range(n)]
    B = lambda z, rot: product(R*(z-t*rot)/(U-t*rot.conjugate()*z)
                              for t in ts)
    bx = B(x, u)
    weights = [bx/B(a, u) for a in poles]
    reflected = [bx.conjugate()/B(2*x-a, u.conjugate()) for a in poles]
    vandermonde = [[power(a/R, k) for k in range(count)] for a in poles]
    coeffs = solve(vandermonde, reflected)
    lagrange = [ZERO]*count
    for j, a in enumerate(poles):
        rest = poles[:j]+poles[j+1:]
        term = scale(root_poly([v/R for v in rest]),
                     reflected[j]/product((a-v)/R for v in rest))
        lagrange = add(lagrange, term)
    interpolation_errors = [evaluate(coeffs, a/R)-weights[j].conjugate()
                            for j, a in enumerate(poles)]
    padded = coeffs+[ZERO]*(mass-count)
    # v=sum conjugate(s_k)*d_k because J is anti-linear.
    v_values = [sum((padded[k].conjugate()*base['dual_grid_values'][k][j]
                     for k in range(mass)), ZERO) for j in range(n)]
    v_grid_coeffs = solve(base['complete_grid_gram'], v_values)
    norm_v_grid = dot(v_values, v_grid_coeffs)
    response_grid = dot(v_values, base['F_grid_coefficients'])
    norm_s = sum((c.abs_squared() for c in coeffs), F(0))
    e = [sum((base['loss_matrix'][j][k]*padded[k].conjugate()
              for k in range(mass)), ZERO) for j in range(mass)]
    norm_e = sum((c.abs_squared() for c in e), F(0))
    correction = sum((padded[k]*base['correction'][k] for k in range(mass)), ZERO)
    A = sum((r*w.abs_squared()/R for r, w in zip(residues, weights)), F(0))
    diagonal = sum((r*r*w.abs_squared()/(U-a.abs_squared())
                    for r, w, a in zip(residues, weights, poles)), F(0))
    max_weight_squared = max(w.abs_squared() for w in weights)
    sigma_squared = F(137, 5000)
    checks = {
        'admissible': base['verification']['checks']['admissible'],
        'reflected_values_match': reflected == [w.conjugate() for w in weights],
        'lagrange_matches_vandermonde': lagrange == coeffs,
        'all_interpolation_errors_zero': all(v == ZERO for v in interpolation_errors),
        'degree_below_distinct_count': len(coeffs) == count <= mass,
        'complete_grid_response_matches': response_grid == correction-G(A),
        'complete_grid_norm_matches': norm_v_grid == G(norm_s-norm_e),
        'nonzero_dual': norm_v_grid.im == 0 and norm_v_grid.re > 0,
        'original_residue_diagonal_inequality':
            max_weight_squared*diagonal <= F(mass)*R*R*A*A/sigma_squared,
    }
    if count == 1:
        checks['repeated_anchor_constant'] = coeffs == [ONE]
        checks['repeated_anchor_relative_bound'] = (
            response_grid.abs_squared()/norm_v_grid.re/diagonal == F(21, 121))
    verification = {
        'checks': checks,
        'interpolation_errors': interpolation_errors,
        'response_error': response_grid-(correction-G(A)),
        'norm_error': norm_v_grid-G(norm_s-norm_e),
        'required_identity_error': '0',
        'actual_diagonal_product': max_weight_squared*diagonal,
        'required_diagonal_product_upper': F(mass)*R*R*A*A/sigma_squared,
    }
    return {
        'n': n, 'u': u, 'poles': poles, 'residues': residues,
        'distinct_count': count, 'mass': mass,
        'weights': weights, 'reflected_values': reflected,
        'interpolant_coefficients': coeffs, 'lagrange_coefficients': lagrange,
        'complete_dual_grid_values': v_values, 'complete_dual_grid_coefficients': v_grid_coeffs,
        'response_from_complete_grid': response_grid, 'correction': correction,
        'positive_pairing': A, 'norm_s_squared': norm_s, 'negative_coefficients': e,
        'norm_v_from_complete_grid': norm_v_grid, 'diagonal': diagonal,
        'verification': verification,
    }


cases = [
    value_case(9, G(F(3, 5), F(4, 5)), [x], [3]),
    value_case(12, G(F(0), F(1)), [x, x+G(F(0), F(1, 64))], [3, 1]),
    value_case(9, G(F(-1)),
               [x, x+G(F(0), F(1, 1024)), x+G(F(0), F(1, 512))], [1, 1, 1]),
    value_case(9, G(F(3, 5), F(-4, 5)),
               [x, x+G(F(0), F(1, 3)), x+G(F(0), F(-1, 4))], [1, 1, 1]),
]
sigma_squared = F(137, 5000)
constants = {
    'numerator_factor_margin': U-F(273, 200),
    'required_numerator_margin_lower': F(1, 2),
    'R_over_sigma_squared': R*R/sigma_squared,
    'required_R_over_sigma_squared_upper': F(81),
    'local_log_coefficient_upper': F(22, 3),
    'required_local_log_coefficient': F(8),
    'derived_amplitude_exponent_upper': F(11, 512),
    'used_amplitude_exponent': F(1, 40),
    'correction_prefactor_squared': F(21)/(576*sigma_squared),
    'required_correction_prefactor_squared_upper': F(4),
    'correction_relative_bound_at_onset': F(6144000, 27*8192**2),
    'required_correction_relative_upper': F(1, 2),
    'proved_sparse_squared_rate': F(1, 20),
    'required_squared_rate': F(1, 16),
}
constant_checks = {
    'numerator_margin': constants['numerator_factor_margin'] > F(1, 2),
    'R_over_sigma': constants['R_over_sigma_squared'] < 81,
    'local_log_bound': F(22, 3) < 8,
    'log_constant': 1800 < 2**11,
    'constant_at_onset': 27 <= F(8192, 256),
    'log_onset': 13 < F(8192, 256),
    'amplitude_rate': F(11, 512) < F(1, 40),
    'correction_prefactor': constants['correction_prefactor_squared'] < 4,
    'correction_at_onset': constants['correction_relative_bound_at_onset'] <= F(1, 2),
    'squared_rate_margin': F(1, 20) < F(1, 16),
}
failures = [{'case': i, 'check': name} for i, c in enumerate(cases)
            for name, passed in c['verification']['checks'].items() if not passed]
failures += [{'constants': name} for name, passed in constant_checks.items() if not passed]
summary = {
    'cases': len(cases),
    'checks': sum(len(c['verification']['checks']) for c in cases)+len(constant_checks),
    'actual_identity_error': '0' if not failures else 'FAILED',
    'required_identity_error': '0', 'failures': failures,
    'proved_sparse_squared_rate': '1/20', 'required_squared_rate': '1/16',
    'sparse_onset': 8192, 'restriction': 'N <= n/(64 log(2 R n))',
    'scope': 'Exact finite normalization and rational-constant checks; '
             'uniform sparse result is L653 analytic proof; unrestricted target remains open.',
}
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(encode({'summary': summary, 'constants': constants,
                                   'constant_checks': constant_checks, 'cases': cases}), indent=2)+'\n')
print(json.dumps({**summary, 'certificate': str(output)}, sort_keys=True))
if failures:
    raise SystemExit(1)
