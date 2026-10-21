"""Exact uniform coefficient evidence for the negative-scalar proof in L043.

No p-adic sampling or precision cutoff. Each exponent is affine in k>=1;
the certificate records its minimum at k=1 and its nonnegative slope.
"""
from pathlib import Path
import json
from check_generic_fibers import power, shift, pad, valuation

BASE = Path(__file__).resolve().parent
SOURCE = BASE.parent / 'five-isogeny-modular-norm' / 'norm-certificate.json'


def main():
    p = json.loads(SOURCE.read_text())['polynomials_ascending']
    h3 = power(p['h'], 3)
    shifted = {name: pad(shift(poly, 16), 13) for name, poly in
               [('h3', h3), ('J', p['jcoef']), ('d', p['d'])]}
    rows = []
    # For R=F(16+11^(k+2)Z,11^(-11k)sigma)/11^(22-11k),
    # h3 coefficients have slope i+11 and J coefficients have slope i.
    for name in ['h3', 'J']:
        for i, c in enumerate(shifted[name]):
            if c == 0:
                continue
            v = valuation(c)
            slope = i + (11 if name == 'h3' else 0)
            intercept = v + 2*i - 22
            rows.append({'component': name, 'i': i, 'coefficient': c,
                         'valuation': v, 'k_slope': slope,
                         'intercept': intercept,
                         'minimum_k_ge_1': intercept+slope})
    derivative_rows = []
    for row in rows:
        if row['i']:
            derivative_rows.append({
                'component': row['component'], 'i': row['i'],
                'minimum_Rprime_over_11_coefficient_valuation':
                    row['minimum_k_ge_1'] + valuation(row['i']) - 1,
                'required_minimum': 1})
    # F(s^2 X,s)/s^24: each nonleading h3 term has exponent
    # 24-2i in 11^(-v(s)), J terms 23-2i, d terms 22-2i.
    infinity_rows = []
    for name, poly, offset in [('h3', h3, 24), ('J', p['jcoef'], 23),
                               ('d', p['d'], 22)]:
        for i, c in enumerate(poly):
            if c:
                infinity_rows.append({'component': name, 'i': i,
                                      'coefficient': c,
                                      's_inverse_exponent': offset-2*i})
    scalar_cases = [{'sigma': u, 'z0': pow(u, -1, 11),
                     'R_constant': u, 'R_leading_cluster': -u*u % 11,
                     'Rprime_over_11_at_z0':
                        (-u*u*pow(pow(u, -1, 11), 10, 11)) % 11,
                     'C': pow(pow(u, -1, 11), 10, 11),
                     'required_C_for_L': 5}
                    for u in range(1, 11)]
    checks = {
        'shifted_d_is_Wpow11': shifted['d'] == [0]*11+[1, 0],
        'shifted_J_constant_exact': shifted['J'][0] == 11**22,
        'shifted_h3_constant_exact': shifted['h3'][0] == 11**24,
        'monic_F': h3[-1] == 1 and len(h3) == 13,
        'degree_J_d_b': [len(p[n])-1 for n in ['jcoef', 'd', 'b']] == [11,11,10],
        'monic_d_b': p['d'][-1] == p['b'][-1] == 1,
        'intermediate_original_bounds': all(
            shifted[name][i] == 0 or valuation(shifted[name][i]) >= 23-2*i
            for name in ['h3', 'J'] for i in range(1,11)),
        'R_J_constant_unique_unit': all(
            row['minimum_k_ge_1'] >= 2 and row['k_slope'] >= 0
            for row in rows if not (row['component'] == 'J' and row['i'] == 0)),
        'Rprime_over_11_only_d_survives': all(
            row['minimum_Rprime_over_11_coefficient_valuation'] >= 1
            for row in derivative_rows),
        'infinity_scaling_nonnegative_exponents': all(
            row['s_inverse_exponent'] >= 0 for row in infinity_rows),
        'infinity_reduction_exactly_Xpow12_minus_Xpow11':
            [(row['component'], row['i'], row['coefficient'])
             for row in infinity_rows if row['s_inverse_exponent'] == 0]
            == [('h3',12,1), ('d',11,1)],
        'all_ten_unit_cases_C_one_not_five': all(
            row['C'] == 1 != row['required_C_for_L'] for row in scalar_cases),
        'cusp_b_unit_after_scaling':
            p['b'][-1] == 1 and
            valuation(shift(p['b'],16)[0]) == 20 and
            all(c == 0 or valuation(c)+2*i >= 20
                for i,c in enumerate(shift(p['b'],16))),
    }
    certificate = {
        'input': str(SOURCE.relative_to(BASE.parent.parent)),
        'scope': 'all primitive negative scalars s=11^(-11k)sigma, k>=1, sigma unit',
        'shifted_components_ascending': shifted,
        'R_affine_valuation_bounds': rows,
        'Rprime_over_11_bounds': derivative_rows,
        'infinity_scaling_terms': infinity_rows,
        'all_unit_residue_cases': scalar_cases,
        'bounds': {'actual_degree_ten_constant_over_11_residue': 1,
                   'required_for_L': 5,
                   'actual_negative_slice_vector_count': 0,
                   'remaining_norm_candidates': 25,
                   'complete_restricted_vector_count': None,
                   'remaining_cases': ['integral s=0 mod11', 'integral s=1 mod11']},
        'checks': checks, 'failures': [name for name,ok in checks.items() if not ok],
        'qualification': 'The root coverage and full-fiber comparison require the uniform proof in L043; coefficient checks alone are not a proof.',
    }
    path = BASE / 'negative-scalar-certificate.json'
    path.write_text(json.dumps(certificate, indent=2)+'\n')
    print('Primitive negative scalars: actual compatible vector count=0; full image remains unresolved.')
    print('Degree-ten constant/11 residue: actual=1, required for L=5; all k>=1, all ten unit residues.')
    print(f'Checks: {sum(checks.values())}/{len(checks)}; failures={certificate["failures"]}')
    print('Certificate: '+str(path.relative_to(BASE.parent.parent)))
    if certificate['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
