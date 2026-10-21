"""Exact upper-vertex and Green-column checks for L163; no probe values."""
from fractions import Fraction as Q
from pathlib import Path
import json


def eps(i, j, k):
    if len({i, j, k}) < 3:
        return 0
    return (-1) ** sum(x > y for x, y in ((i, j), (i, k), (j, k)))


def plus(*vectors):
    return [sum(x) for x in zip(*vectors)]


def cubic(v):
    # L155's ordered word (x,z,-y,0): +x dot (z cross y)/2.
    x, z, y = v[:3], v[3:6], v[6:]
    return sum(Q(eps(i, j, k), 2)*x[i]*z[j]*y[k]
               for i in range(3) for j in range(3) for k in range(3))


def tensor(i, j, k):
    return Q(eps(i//3, j//3, k//3)*eps(i % 3, j % 3, k % 3), 12)


def polarization(h, x, y):
    return (cubic(plus(h, x, y))-cubic(plus(h, x))-cubic(plus(h, y))
            -cubic(plus(x, y))+cubic(h)+cubic(x)+cubic(y))/6


basis = [[Q(i == j) for i in range(9)] for j in range(9)]
vertices = []
failures = []
max_error = Q(0)
for profile in ((Q(1), Q(1)), (Q(2), Q(-3))):
    for color in range(3):
        h = [Q(0)]*9
        h[color], h[6+color] = profile
        actual = [[sum(h[k]*tensor(k, i, j) for k in range(9))
                   for j in range(9)] for i in range(9)]
        independent = [[polarization(h, basis[i], basis[j])
                        for j in range(9)] for i in range(9)]
        error = max(abs(actual[i][j]-independent[i][j])
                    for i in range(9) for j in range(9))
        max_error = max(max_error, error)
        invalid_blocks = [(i, j) for i in range(9) for j in range(9)
                          if actual[i][j] and ((i//3 == 1) == (j//3 == 1))]
        fixed_controls = []
        for fixed in range(3):
            hf = [value if k//3 != fixed else Q(0) for k, value in enumerate(h)]
            restricted = [[sum(hf[k]*tensor(k, i, j) for k in range(9))
                           for j in range(9) if j//3 != fixed]
                          for i in range(9) if i//3 != fixed]
            residual = max(abs(x) for row in restricted for x in row)
            fixed_controls.append(dict(fixed_link=fixed, required_zero=residual == 0,
                                       full_restricted_matrix=restricted))
        nonzero = sum(x != 0 for row in actual for x in row)
        passed = not error and not invalid_blocks and nonzero > 0 and all(
            item['required_zero'] for item in fixed_controls)
        name = f'profile={profile}, color={color}'
        if not passed:
            failures.append(name)
        vertices.append(dict(name=name, exterior=h, tensor_contraction=actual,
                             polarized_polynomial=independent, maximum_exact_error=error,
                             forbidden_component_entries=invalid_blocks,
                             nonzero_entry_count=nonzero, fixed_controls=fixed_controls,
                             passed=passed))

columns = []
for n in (4, 6, 8, 12):
    for t in (Q(3, 2), Q(2), Q(3)):
        lam = t+1/t-2
        den = t**n-t**(-n)
        edge = [(t**(r+1)+t**(-r))/((t-1)*den) for r in range(n)]
        vertex = [(t**s-t**(-s))/den for s in range(1, n)]
        for boundary, values in (('edge_Neumann', edge), ('vertex_Dirichlet', vertex)):
            size = len(values)
            product = []
            for row in range(size):
                diagonal = Q(1 if boundary == 'edge_Neumann' and row in (0, size-1) else 2)
                value = (diagonal+lam)*values[row]
                if row:
                    value -= values[row-1]
                if row+1 < size:
                    value -= values[row+1]
                product.append(value)
            required = [Q(row == size-1) for row in range(size)]
            error = max(abs(x-y) for x, y in zip(product, required))
            max_error = max(max_error, error)
            passed = error == 0 and all(x > 0 for x in values)
            if not passed:
                failures.append(f'N={n}, t={t}, {boundary}')
            columns.append(dict(N=n, exp_eta=t, lambda_value=lam, boundary=boundary,
                                full_column=values, full_matrix_product=product,
                                required_unit_source=required, maximum_exact_error=error,
                                passed=passed))

certificate = dict(
    scope='Upper action tensor with one fixed face edge and all endpoint/color cases; exact relative last columns. No actual-probe numerical or asymptotic claims.',
    vertex_cases=vertices, green_column_cases=columns,
    summary=dict(vertex_case_count=len(vertices),
                 polarization_entry_checks=81*len(vertices),
                 additional_fixed_link_cases=3*len(vertices),
                 green_column_case_count=len(columns),
                 maximum_exact_error=max_error, required_exact_error=0,
                 analytic_normal_column_bound='C N^-2',
                 analytic_transverse_column_bound='C N^-3',
                 analytic_trace_bound='C_i N^2; a^3 contribution tends to zero',
                 required_complete_response_bound='o(N^3); unresolved'),
    failures=failures, passed=not failures)
path = Path(__file__).with_name('cubic-hodge-upper-jump-certificate.json')
path.write_text(json.dumps(certificate, default=str, indent=2)+'\n')
print(f'Vertex cases: {len(vertices)}; polarization entries: {81*len(vertices)}; fixed-link cases: {3*len(vertices)}; Green columns: {len(columns)}.')
print(f'Maximum exact error: {max_error}; required: 0; failures: {failures}.')
print('Analytic upper-jump trace: O(N^2), below required o(N^3). Complete response remains unresolved.')
print(f'Certificate: {path.relative_to(Path.cwd())}.')
assert not failures
