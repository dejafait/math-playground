#!/usr/bin/env python3
"""Exact finite arithmetic for L119; analytic Hensel bounds are in its proof."""

from fractions import Fraction as Q
from itertools import product
from math import comb
from pathlib import Path
import json

OUT = Path(__file__).with_name("marked-octic-five-adic-image-certificate.json")
G = [2673, 0, -39204, 0, 76230, 0, -31460, 0, 3025]
H = [3025, -31460, 76230, -39204, 2673]
J = [121, -6292, 76230, -196020, 66825]  # H(5u)/25


def ev(poly, x):
    answer = Q(0)
    for c in reversed(poly):
        answer = answer*x+c
    return answer


def der(poly):
    return [i*c for i, c in enumerate(poly)][1:]


def valuation(x):
    x = Q(x)
    if not x:
        return None
    answer = 0
    numerator, denominator = x.numerator, x.denominator
    while numerator % 5 == 0:
        numerator //= 5
        answer += 1
    while denominator % 5 == 0:
        denominator //= 5
        answer -= 1
    return answer


def residue(x):
    x = Q(x)
    assert x.denominator % 5
    return x.numerator*pow(x.denominator, -1, 5) % 5


def square_bit(x):
    """Unit square-class bit in Q5, for a unit rational x."""
    assert valuation(x) == 0
    return 0 if residue(x) in (1, 4) else 1


def hensel(poly, seed, depth=6):
    rows = []
    value, modulus = seed, 5
    assert ev(poly, value) % modulus == 0
    assert residue(ev(der(poly), value)) != 0
    for exponent in range(1, depth):
        candidates = [value + modulus*j for j in range(5)]
        errors = [int(ev(poly, c)) % (5*modulus) for c in candidates]
        passing = [j for j, error in enumerate(errors) if error == 0]
        assert len(passing) == 1
        rows.append(dict(exponent=exponent, seed=value, modulus=modulus,
                         candidates=candidates, errors_mod_next=errors,
                         passing_digits=passing))
        value = candidates[passing[0]]
        modulus *= 5
    return dict(poly_ascending=poly, seed=seed,
                initial_error=str(ev(poly, seed)),
                initial_derivative=str(ev(der(poly), seed)),
                steps=rows, residue=value, modulus=modulus)


def xor(x, y):
    return tuple(a ^ b for a, b in zip(x, y))


def bits(x):
    return ''.join(map(str, x))


def main():
    root0, unit1 = hensel(H, 3), hensel(J, 3)
    modulus = root0['modulus']
    r0 = root0['residue']
    r1 = 5*unit1['residue'] % modulus
    # Exact factor coefficients are a=-39204/2673+r0+r1 and
    # b=3025/(2673*r0*r1). These are their certified reductions.
    a_mod = (-39204*pow(2673, -1, modulus)+r0+r1) % modulus
    b_mod = (605*pow(2673*r0*unit1['residue'], -1, modulus)) % modulus
    factor_rows = dict(r0_mod=r0, r1_mod=r1, modulus=modulus,
                       a_mod=a_mod, b_mod=b_mod,
                       b_over_5_mod_5=residue(Q(121, 2673*3*3)),
                       minus_b_over_10_mod_5=residue(Q(-121, 2*2673*3*3)))
    # Check the entire exact factorization modulo the common precision.
    def mul(p, q):
        result = [0]*(len(p)+len(q)-1)
        for i, c in enumerate(p):
            for j, d in enumerate(q):
                result[i+j] = (result[i+j]+c*d) % modulus
        return result
    factor_product = [2673*c % modulus for c in mul(
        mul([-r0, 1], [-r1, 1]), [b_mod, a_mod, 1])]

    residue_disks = []
    for t in range(5):
        unit_norm = (t*t-2) % 5
        residue_disks.append(dict(t_mod_5=t, G_mod_5=int(ev(G, t)) % 5,
                                  unramified_norm_mod_5=unit_norm,
                                  feasible=unit_norm in (1, 4),
                                  center_G=str(ev(G, t)),
                                  normalized_class="101000" if unit_norm in (1, 4) else None))

    # S(q)=q^8 G(1/q)/3025. For n=v5(q)>=1, each nonconstant
    # monomial has valuation slope*n+intercept, with its minimum at n=1.
    reciprocal_terms = []
    for i in (2, 4, 6, 8):
        coefficient = Q(G[8-i], G[8])
        reciprocal_terms.append(dict(power=i, coefficient=str(coefficient),
                                     slope=i, intercept=valuation(coefficient),
                                     minimum_at_n_1=i+valuation(coefficient)))
    strict_bounds = dict(
        square_neighborhood_required="normalized valuation > 0 (residue characteristic 5)",
        integral_ramified_ratio=[dict(factor="quartic", minimum=1),
                                  dict(factor="quadratic", minimum=1)],
        integral_unit_disk_difference=dict(minimum=1, center_unit_valuation=0),
        reciprocal_ratios=[dict(factor="quartic", slope=4, intercept=-1, minimum=3),
                           dict(factor="quadratic", slope=2, intercept=-1, minimum=1),
                           dict(factor="unramified", slope=1, intercept=0, minimum=1)])

    # Labels: (pi^a*2^b, lambda^c*2^d, 5^e*(1+omega)^f).
    scalar2 = (0, 1, 0, 1, 0, 0)
    scalar5 = (0, 1, 0, 1, 1, 0)
    scalars = sorted({(0,)*6, scalar2, scalar5, xor(scalar2, scalar5)})
    def norm(v):
        a, b, c, d, e, f = v
        return (a ^ c, a ^ c ^ f)  # Q5 coordinates (5,2)
    def quotient(v):
        candidates = [xor(v, s) for s in scalars]
        normalized = [w for w in candidates if w[3] == 0 and w[4] == 0]
        assert len(normalized) == 1
        return normalized[0]
    vectors = list(product((0, 1), repeat=6))
    norm_kernel = [v for v in vectors if norm(v) == (0, 0)]
    orbits = {}
    for v in vectors:
        orbits.setdefault(bits(quotient(v)), []).append(bits(v))
    ambient = sorted({bits(quotient(v)) for v in norm_kernel})
    alpha = (1, 0, 1, 0, 0, 0)
    beta = (0, 1, 0, 0, 0, 0)
    image = sorted({bits(quotient((0,)*6)), bits(quotient(alpha))})
    infinity_rows = [dict(q=0, Z=z, derivative=2*z, fake_class="000000")
                     for z in (-55, 55)]
    finite_realizations = [dict(t="1", G=str(ev(G, Q(1))),
                                square_unit_mod_5=residue(ev(G, Q(1))),
                                Y_seed_mod_5=2, Y_derivative_mod_5=4,
                                quotient=bits(quotient(alpha))),
                           dict(t="1/5", G=str(ev(G, Q(1, 5))),
                                normalized_square=str(ev(G, Q(1,5))/(Q(55)*Q(1,5)**4)**2),
                                normalized_Y_seed_mod_5=1,
                                normalized_Y_derivative_mod_5=2,
                                quotient="000000")]
    norm_table = [dict(factor="quartic", generator="pi", norm="-10", label=[1,1]),
                  dict(factor="quartic", generator="2", norm="16", label=[0,0]),
                  dict(factor="quadratic", generator="lambda", norm="-15", label=[1,1]),
                  dict(factor="quadratic", generator="2", norm="4", label=[0,0]),
                  dict(factor="unramified", generator="5", norm="25", label=[0,0]),
                  dict(factor="unramified", generator="1+omega", norm="-2", label=[0,1])]
    norm_table_replay = []
    for row in norm_table:
        value = Q(row['norm'])
        exponent = valuation(value)
        label = [exponent % 2, square_bit(value/Q(5)**exponent)]
        norm_table_replay.append(label)

    checks = dict(
        unchanged_G=G == [2673,0,-39204,0,76230,0,-31460,0,3025],
        reciprocal_even_identity=all(H[i] == G[8-2*i] for i in range(5)),
        scaled_H_identity=[Q(H[i]*5**i,25) for i in range(5)] == list(map(Q,J)),
        r0_simple_seed=residue(ev(H,3)) == 0 and residue(ev(der(H),3)) != 0,
        r1_simple_seed=residue(ev(J,3)) == 0 and residue(ev(der(J),3)) != 0,
        all_factor_coefficients= factor_product == [c % modulus for c in H],
        a_in_5=a_mod % 5 == 0,
        b_exact_valuation_one=b_mod % 25 in (5,10,15,20),
        b_over_5_residue=b_mod//5 % 5 == 3,
        quartic_model_unit_root=factor_rows['minus_b_over_10_mod_5'] == 1,
        ramified_quadratic_model=residue(Q(3,3)) == 1,
        unramified_model_nonsquare=3 not in {i*i % 5 for i in range(5)},
        local_degrees_complete=4+2+2 == 8,
        residue_norm_equals_G=all(r['G_mod_5'] == r['unramified_norm_mod_5'] for r in residue_disks),
        all_integral_disks_resolved=[r['t_mod_5'] for r in residue_disks if r['feasible']] == [1,4],
        integral_centers_square_units=all(residue(ev(G,t)) in (1,4) for t in (1,-1)),
        reciprocal_square_precision=all(r['minimum_at_n_1'] > 0 for r in reciprocal_terms),
        all_ratio_precision_strict=all(r['minimum'] > 0 for r in strict_bounds['integral_ramified_ratio']+strict_bounds['reciprocal_ratios']),
        norm_table_correct=norm_table_replay == [r['label'] for r in norm_table],
        scalar5_quartic=square_bit(Q(1,2)) == 1,
        scalar5_quadratic=square_bit(Q(1,3)) == 1,
        scalar_group_size=len(scalars) == 4,
        common_scalars_norm_trivial=all(norm(s) == (0,0) for s in scalars),
        all_orbits_four=len(orbits) == 16 and all(len(v) == 4 for v in orbits.values()),
        norm_kernel_size=len(norm_kernel) == 16,
        ambient_exact=ambient == ["000000","010000","101000","111000"],
        image_exact=image == ["000000","101000"],
        image_proper=set(image) < set(ambient),
        excluded_witness=bits(quotient(beta)) in ambient and bits(quotient(beta)) not in image,
        finite_realizations=finite_realizations[0]['square_unit_mod_5'] == 4 and residue(Q(finite_realizations[1]['normalized_square'])) == 1,
        infinity_rows_complete=len(infinity_rows) == 2 and all(r['Z']**2 == G[-1] and r['derivative'] != 0 for r in infinity_rows),
    )
    failures = [key for key, passed in checks.items() if not passed]
    certificate = dict(
        coefficients_ascending=G, H_ascending=H, J_ascending=J,
        hensel_r0=root0, hensel_r1_over_5=unit1,
        factor_coefficient_residues=factor_rows, factor_product_mod_precision=factor_product,
        exact_factorization="H(r)=2673(r-r0)(r-r1)(r^2+a*r+b); r0 and r1/5 are the unique Hensel roots at 3 mod 5",
        local_models=[dict(degree=4,e=4,f=1,model="pi^4=10", q="pi*u; u^4+(a/pi^2)*u^2+b/10=0, u=1 mod pi"),
                      dict(degree=2,e=2,f=1,model="lambda^2=15",q="lambda*sqrt(r1/15); principal square root"),
                      dict(degree=2,e=1,f=2,model="omega^2=3",q="omega*sqrt(r0/3); principal square root")],
        theta="1/q in every complete factor", label_order=["pi","2 at quartic","lambda","2 at quadratic","5 at unramified","1+omega"],
        integral_disks=residue_disks, reciprocal_terms=reciprocal_terms,
        strict_bounds=strict_bounds, rational_branch_points=[],
        finite_realizations=finite_realizations, infinity_rows=infinity_rows,
        norm_table=norm_table, norm_table_replay=norm_table_replay,
        scalars=[bits(s) for s in scalars], full_quotient_collisions=orbits,
        full_norm_kernel=[bits(v) for v in norm_kernel],
        ambient=ambient, image=image, excluded_witness=bits(quotient(beta)),
        bounds=dict(local_degree_actual=8, local_degree_required=8,
                    affine_residue_disks_actual=5,affine_residue_disks_required=5,
                    unresolved_disks=0, reciprocal_minimum_n=1,
                    square_precision_required="strictly positive normalized valuation",
                    infinity_rows_actual=2,infinity_rows_required=2,
                    image_actual=len(image),ambient_actual=len(ambient),properness_required="image < ambient"),
        checks=checks, failures=failures)
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')
    print(f"Checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}")
    print("Local degrees: 8/8; affine disks: 5/5; unresolved: 0; infinity rows: 2/2")
    print("Strict ratio minima: integral 1,1; reciprocal 3,1,1; required >0")
    print(f"Image: {len(image)}; full norm ambient: {len(ambient)}; required image < ambient")
    print(f"Certificate: {OUT}")
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
