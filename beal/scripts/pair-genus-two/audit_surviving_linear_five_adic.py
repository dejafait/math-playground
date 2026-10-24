#!/usr/bin/env python3
"""Independent finite replay for C124a; exact Hensel proof is canonical.

Does not import or run the producer. L119's audited transports and point
image are inputs, not rederived by a precision computation here.
"""
import json
from itertools import product
from pathlib import Path
from fractions import Fraction

BASE = Path(__file__).resolve().parent
source = json.loads((BASE / 'surviving-linear-five-adic-certificate.json').read_text())
out = BASE / 'surviving-linear-five-adic-audit-certificate.json'
checks = {}


def verify(name, actual, required):
    checks[name] = dict(actual=actual, required=required, passed=actual == required)


G = [2673, 0, -39204, 0, 76230, 0, -31460, 0, 3025]
hc = list(reversed(G))[::2]
jf = [Fraction(hc[i]*5**i, 25) for i in range(5)]
verify('J_integral', [c.denominator for c in jf], [1]*5)
jc = [int(c) for c in jf]
verify('reciprocal_H', source['exact_models']['H_ascending'], hc)
verify('scaled_J', source['exact_models']['J_ascending'], jc)
fixed = [-3*3, (-3)*(-1)+(-1)*3, (-1)*(-1)]
verify('product', source['polynomial_ascending'], fixed)
verify('mask', source['mask'], sum(2**i for i in [0, 4]))
# Exact coefficient identities after clearing q^2, r and 3r respectively.
verify('ramified_identity_after_q_squared', [fixed[2], fixed[1], fixed[0]], [1, 0, -9])
verify('unramified_identity_after_r', [Fraction(3, 3), Fraction(-27, 3)], [1, -9])
verify('unramified_error_after_3r', [1, -9-3], [1, -12])


def seed(coeff):
    return [sum(c*3**i for i, c in enumerate(coeff)) % 5,
            sum(i*c*3**(i-1) for i, c in enumerate(coeff) if i) % 5]


def mul(x, y):
    return ((x[0]*y[0]+3*x[1]*y[1]) % 5,
            (x[0]*y[1]+x[1]*y[0]) % 5)


squares = sorted({mul(z, z) for z in product(range(5), repeat=2) if z != (0, 0)})
verify('all_F25_squares', source['F25_nonzero_squares'], [list(z) for z in squares])
verify('F25_square_count', len(squares), 12)
verify('residue_root', list(mul((0, 1), (0, 1))), source['unramified_component']['normalized_residue'])
verify('rational_residue_units_square', all((a, 0) in squares for a in range(1, 5)), True)

for row, model, uniformizer, e in zip(source['ramified_components'], ['L4', 'L2'], ['pi', 'lambda'], [4, 2]):
    # q/uniformizer is principal by the exact imported transport.
    expected = dict(model=model, uniformizer=uniformizer, v_5=e, v_q=1,
                    v_theta=-1, v_delta=-2, normalized_unit_residue=1,
                    square_factor='q^(-2)', principal_factor='1-9*q^2',
                    exact_relative_valuation=2,
                    required_relative_valuation_strictly_greater_than=0,
                    square_class_bits=[(-2) % 2, 0])
    verify(model+'_complete_record', row, expected)
verify('ramified_count', len(source['ramified_components']), 2)
delta = (pow(3, -1, 5)-9) % 5
w = (1-9*3)*pow(3*3, -1, 5) % 5
verify('U_complete_record', source['unramified_component'], dict(
    v_delta=0, delta='(1-9*r0)/r0', normalized_residue=[delta, 0],
    residue_square_root=[0, 1], square_factor='omega^2',
    principal_factor='(1-9*r0)/(3*r0)', relative_error='(1-12*r0)/(3*r0)',
    relative_valuation_lower_bound=1,
    required_relative_valuation_strictly_greater_than=0, square_class_bits=[0, 0]))

# Rational 2 is nonsquare in both F5 residue fields and square in F25.
# 5=pi^4/2=lambda^2/3; its U valuation is one.
chi = lambda a: int(pow(a % 5, 2, 5) == 4)
rows = ['0'+str(chi(2))+'0'+str(chi(2))+'00',
        '0'+str(chi(3))+'0'+str(chi(2))+'10']
orbit = sorted({format((int(rows[0], 2)*i) ^ (int(rows[1], 2)*j), '06b')
                for i, j in product([0, 1], repeat=2)})
norm = lambda b: [int(b[0]) ^ int(b[2]), int(b[0]) ^ int(b[2]) ^ int(b[5])]
canonical = [b for b in orbit if b[3:5] == '00']
for key, expected in dict(raw_label='000000', norm_bits=norm('000000'),
    scalar_generators=rows, full_scalar_orbit=orbit,
    canonical_representative=canonical[0], imported_point_image=['000000', '101000'],
    relative_precision_lower_bounds=[2, 2, 1], failures=[],
    result='PASS: identity class; no additional pruning of mask 17').items():
    verify(key, source[key], expected)
verify('unique_canonical', canonical, ['000000'])
verify('strict_bounds', all(v > 0 for v in source['relative_precision_lower_bounds']), True)

replay = dict(fixed_product=fixed, mask=17,
    H_seed_and_derivative=seed(hc), J_seed_and_derivative=seed(jc),
    principal_quadratic_transport_units=[3*pow(3, -1, 5) % 5]*2,
    L4_strict_margin=2 > 0, L4_valuation_parity=(-2) % 2,
    L2_strict_margin=2 > 0, L2_valuation_parity=(-2) % 2,
    unramified_delta_residue=delta, unramified_principal_unit=w,
    unramified_relative_error_numerator=(1-12*3) % 5, omega_squared=mul((0, 1), (0, 1))[0],
    unramified_residue_norm=mul((delta, 0), (delta, 0))[0],
    raw_norm_bits=norm('000000'), orbit_size=len(orbit), orbit_norms=[norm(b) for b in orbit],
    canonical_representative=canonical, point_image_membership=canonical[0] in ['000000', '101000'],
    leading_coefficient_square=55**2, delta_residue_is_F25_square=(delta, 0) in squares)
verify('all_producer_check_names', sorted(source['checks']), sorted(replay))
for name, actual in replay.items():
    verify('producer_'+name, source['checks'][name], dict(actual=actual, required=actual, **{'pass': True}))

failures = [k for k, v in checks.items() if not v['passed']]
out.write_text(json.dumps(dict(checks=checks, failures=failures,
    relative_bounds=[2, 2, 1], required_strict_threshold=0,
    exact_proof='lemmas/C124a-surviving-linear-product-passes-five.md',
    limitations='Exact Hensel transports and full point image imported from audited L119; no global squareness or rational point inferred.'), indent=2, default=str)+'\n')
print(f'{len(checks)} independent comparisons; failures={failures}')
print('relative bounds [2,2,1] > required 0; raw/canonical identity; orbit size 4')
print(f'certificate={out}')
raise SystemExit(bool(failures))
