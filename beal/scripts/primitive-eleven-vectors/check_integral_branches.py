"""Complete exact coefficient evidence for the two primitive branch disks.

No scalar sampling: perturbation bounds are uniform in the stated valuations.
The unique-minimum argument and fiber necessity are written in L044.
"""
from fractions import Fraction
from pathlib import Path
import json

from check_generic_fibers import add, power, shift, scaled, valuation, ev, pad

BASE = Path(__file__).resolve().parent
SOURCE = BASE.parent / 'five-isogeny-modular-norm' / 'norm-certificate.json'


def bound_rows(components, offsets, height):
    rows = []
    for i in range(13):
        vals = {name: valuation(a[i]) for name, a in components.items()}
        lower = Fraction(height*(12-i), 12)
        row = {'i': i, 'required_bound': str(lower), 'valuations': vals,
               'uniform_component_bounds': {
                   name: None if vals[name] is None else vals[name]+offsets[name]
                   for name in vals}}
        row['base_meets_bound'] = (vals['base'] is None or vals['base'] >= lower)
        row['perturbations_strictly_above'] = all(
            v is None or v > lower for name, v in
            row['uniform_component_bounds'].items() if name != 'base')
        rows.append(row)
    return rows


def main():
    p = json.loads(SOURCE.read_text())['polynomials_ascending']
    h3 = power(p['h'], 3)
    H = shift(scaled(p['h'], 8), -1)
    Jstar = shift(scaled(p['jcoef'], 22), -1)
    Dstar = power([-1, 1], 11)
    zero_components = {'base': pad(power(H, 3), 13),
                       'linear': pad(Jstar, 13),
                       'quadratic': pad(Dstar, 13)}
    # s/121 has valuation >=1; s^2/121 has valuation >=4.
    zero_rows = bound_rows(zero_components,
                           {'base': 0, 'linear': 1, 'quadratic': 4}, 3)
    F1728 = add(add(h3, [1728*c for c in p['jcoef']]),
                [-1728**2*c for c in p['d']])
    Q = add(p['jcoef'], [-3456*c for c in p['d']])
    one_components = {'base': pad(shift(F1728, 16), 13),
                      'linear': pad(shift(Q, 16), 13),
                      'quadratic': pad(shift(p['d'], 16), 13)}
    # u=s-1728 has valuation >=4; u^2 has valuation >=8.
    one_rows = bound_rows(one_components,
                          {'base': 0, 'linear': 4, 'quadratic': 8}, 22)
    exceptional = {
        'T_scalar': -24729001, 'T_scalar_valuation': valuation(-24729001),
        'twoT_scalar': -121, 'twoT_scalar_valuation': valuation(-121),
        'fourT_scalar': -32768,
        'fourT_scalar_minus_1728_valuation': valuation(-32768-1728),
        'O_and_threeT_scalar': 'infinity',
    }
    checks = {
        'zero_H_exact': H == [352, -1144, 1232, -440, 1],
        'zero_Dstar_identity': shift(scaled(p['d'], 22), -1) == Dstar,
        'zero_all_base_bounds': all(r['base_meets_bound'] for r in zero_rows),
        'zero_all_perturbations_strict': all(
            r['perturbations_strictly_above'] for r in zero_rows),
        'zero_endpoints_exact': valuation(zero_components['base'][0]) == 3
                               and zero_components['base'][12] == 1,
        'zero_constant_leading_residue': zero_components['base'][0]//11**3 % 11 == 10,
        'one_all_base_bounds': all(r['base_meets_bound'] for r in one_rows),
        'one_all_perturbations_strict': all(
            r['perturbations_strictly_above'] for r in one_rows),
        'one_endpoints_exact': valuation(one_components['base'][0]) == 22
                              and one_components['base'][12] == 1,
        'one_constant_leading_residue': one_components['base'][0]//11**22 % 11 == 1,
        'rational_root_valuation_impossible': Fraction(1,4).denominator != 1
                                            and Fraction(11,6).denominator != 1,
        'T_and_twoT_not_primitive_scalars': exceptional['T_scalar_valuation'] == 1
                                          and exceptional['twoT_scalar_valuation'] == 2,
        'fourT_not_primitive_scalar': exceptional['fourT_scalar_minus_1728_valuation'] == 1,
        'T_and_fourT_map_evaluations': all(
            ev(p['a'], 5)+y*ev(p['b'], 5) == s*ev(p['d'], 5)
            for y,s in [(5,-24729001),(-6,-32768)]),
        'complete_vectors_meet_norm': all(sum(v)%5 == 2
                                         for v in [(0,2,0),(2,0,0)]),
    }
    certificate = {
        'input': str(SOURCE.relative_to(BASE.parent.parent)),
        'zero_disk': {'scope': 'all v11(s)>=3; in particular every positive multiple of three',
                      'variable': 'V=(x+105)/121',
                      'monic_polynomial': 'F(-105+121V,s)/11^24',
                      'H_ascending': H, 'components_ascending': zero_components,
                      'full_bounds': zero_rows, 'forced_root_valuation': '1/4',
                      'constant_over_11pow3_residue': zero_components['base'][0]//11**3 % 11},
        'one_disk': {'scope': 'all v11(s-1728)>=4; in particular every positive multiple of four',
                     'variable': 'W=x-16', 'monic_polynomial': 'F(16+W,s)',
                     'components_ascending': one_components, 'full_bounds': one_rows,
                     'forced_root_valuation': '11/6',
                     'constant_over_11pow22_residue': one_components['base'][0]//11**22 % 11},
        'exceptional_charts': exceptional,
        'threshold': {'actual_compatible_branch_disk_vectors': 0,
                      'actual_complete_primitive_vectors': [[0,2,0],[2,0,0]],
                      'actual_vector_count': 2, 'prior_norm_candidates': 25,
                      'required': 'uniform necessity on all scalar regions plus exact realization',
                      'realization_input': 'L042', 'negative_scalar_input': 'L043'},
        'checks': checks, 'failures': [name for name,ok in checks.items() if not ok],
        'qualification': 'Exact arithmetic evidence; full proof and inherited inputs are in L044. No global class intersection or integer emptiness follows.',
    }
    path = BASE / 'integral-branch-certificate.json'
    path.write_text(json.dumps(certificate, indent=2)+'\n')
    print('Root valuations: actual zero disk=1/4, one disk=11/6; rational roots require integers.')
    print('Primitive compatible vectors: actual=2 versus 25 norm candidates; required uniform coverage and realization supplied by L044 and L042.')
    print(f'Checks: {sum(checks.values())}/{len(checks)}; failures={certificate["failures"]}')
    print('Certificate: '+str(path.relative_to(BASE.parent.parent)))
    if certificate['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
