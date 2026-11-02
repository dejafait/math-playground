"""Exact finite checks for L650. No floating point, quadrature or tail cutoff.

Load only arithmetic definitions from the C645y checker; its driver is
not executed and its certificate is not rewritten. The uniform proof is
in L650; these cases check full-grid dual norms and conjugations.
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


def dual_case(n, u):
    epsilon = F(1, 2**n)
    poles = [x, x + G(F(0), epsilon)]
    base = case(n, u, poles, [1, 1])
    ts = [F(j, n) for j in range(n)]
    bs = [t*u for t in ts]
    betas = [b/R for b in bs]
    B = lambda z: product(R*(z-b)/(U-b.conjugate()*z) for b in bs)
    bx = B(x)
    weights = [bx/B(a) for a in poles]
    beta1 = product(-beta for beta in betas[1:])
    beta2 = beta1*sum((beta.conjugate()-1/beta for beta in betas[1:]), ZERO)
    p = F(1)
    for t in ts[1:]:
        p *= t/R
    gram = [[1/(1-ti*tj/U) for tj in ts] for ti in ts]
    duals = []
    checks = {f'base_{key}': ok for key, ok in base['checks'].items()}
    for index, v in enumerate(poles):
        w = poles[1-index]
        s0, s1 = -w/(v-w), G(R)/(v-w)
        e0 = beta1*s1.conjugate()
        values = [beta1*s0.conjugate()+beta2*s1.conjugate()]
        values += [-e0/beta for beta in betas[1:]]
        coeffs = solve(gram, values)
        gram_norm = sum((value.conjugate()*c for value, c in zip(values, coeffs)), ZERO)
        required_norm = (w.abs_squared()+R*R*(1-p*p))/(epsilon*epsilon)
        pairing = sum((residue*(s0+s1*beta)/R
                       for residue, beta in zip(base['grid_residues'], betas)), ZERO)
        required_pairing = 2*bx*beta1.conjugate()/(v-w)-weights[index]/R
        ratio_squared = pairing.abs_squared()/required_norm
        required_upper = F(217, 55)**2/R**(2*n)
        checks[f'dual_{index}_norm_difference_zero'] = gram_norm == G(required_norm)
        checks[f'dual_{index}_pairing_difference_zero'] = pairing == required_pairing
        checks[f'dual_{index}_bound'] = ratio_squared <= required_upper
        checks[f'dual_{index}_nonzero'] = required_norm > 0
        duals.append({
            's_coefficients': [s0, s1], 'negative_coefficient': e0,
            'all_grid_values': values, 'all_gram_coefficients': coeffs,
            'actual_norm_squared': gram_norm, 'required_norm_squared': required_norm,
            'norm_difference': gram_norm-G(required_norm),
            'actual_pairing': pairing, 'required_pairing': required_pairing,
            'pairing_difference': pairing-required_pairing,
            'actual_response_squared': ratio_squared, 'required_upper': required_upper,
        })
    checks['beta1_modulus'] = beta1.abs_squared() == p*p
    checks['dual_sum_s_is_one'] = all(
        duals[0]['s_coefficients'][j]+duals[1]['s_coefficients'][j] == (ONE if j == 0 else ZERO)
        for j in range(2))
    checks['dual_sum_negative_zero'] = sum((v['negative_coefficient'] for v in duals), ZERO) == ZERO
    combined_pairing = sum((v['actual_pairing'] for v in duals), ZERO)
    checks['combined_pairing'] = combined_pairing == -(1+weights[1])/R
    checks['combined_coercivity'] = base['grid_norm_squared'].re >= combined_pairing.abs_squared()
    if n >= 10:
        checks['retained_energy_lower_bound'] = base['grid_norm_squared'].re >= F(232, 165)**2
        checks['combined_lower_bound'] = combined_pairing.abs_squared() >= F(232, 165)**2
    return {'n': n, 'u': u, 'poles': poles, 'residues': [1, 1],
            'epsilon': epsilon, 'weights': weights, 'beta1': beta1, 'p_n': p,
            'grid_residues': base['grid_residues'], 'dual_checks': duals,
            'combined_pairing': combined_pairing,
            'full_retained_energy': base['grid_norm_squared'], 'checks': checks}


cases = [dual_case(n, u) for n in [6, 10]
         for u in [ONE, G(F(0), F(1)), G(F(3, 5), F(4, 5))]]
failures = [{'case': i, 'check': k} for i, c in enumerate(cases)
            for k, passed in c['checks'].items() if not passed]
summary = {
    'cases': len(cases), 'checks': sum(len(c['checks']) for c in cases),
    'actual_identity_error': '0' if not failures else 'FAILED',
    'required_identity_error': '0', 'failures': failures,
    'proved_rate_gap_lower_bound': F(85, 176),
    'required_squared_rate': F(1, 16),
    'scope': 'Exact finite normalization checks; uniform proof is L650, not these cases.'
}
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(encode({'summary': summary, 'cases': cases}), indent=2)+'\n')
print(json.dumps(encode({**summary, 'certificate': str(output)}), sort_keys=True))
if failures:
    raise SystemExit(1)
