#!/usr/bin/env python3
"""Single fixed-angle radial IFT specialization; exact rational evidence.

Pairs represent x+y*i*sqrt(3). No branch solve, sweep or new quadrature.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'conjugate-collision-certificate-1322.json'


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def mul(x, y):
    return x[0]*y[0]-3*x[1]*y[1], x[0]*y[1]+x[1]*y[0]


def scale(x, c):
    return c*x[0], c*x[1]


def conj(x):
    return x[0], -x[1]


def div(x, y):
    norm = y[0]**2+3*y[1]**2
    assert norm > 0, 'zero field denominator'
    return scale(mul(x, conj(y)), 1/norm)


def power(x, n):
    out = (Q(1), Q(0))
    for _ in range(n):
        out = mul(out, x)
    return out


def imul(x, y):
    products = [a*b for a in x for b in y]
    return min(products), max(products)


def iadd(x, y):
    return x[0]+y[0], x[1]+y[1]


def iscale(x, c):
    return imul(x, (Q(c), Q(c)))


def enc(x):
    return {'lower': str(x[0]), 'upper': str(x[1])}


def pair(x):
    return list(map(str, x))


def main():
    one, zero = (Q(1), Q(0)), (Q(0), Q(0))
    w = (Q(1, 2), Q(1, 2))
    wc = conj(w)
    p = add(one, power(w, 2))
    pc = add(one, power(wc, 2))
    value = div(w, p)
    valuec = div(wc, pc)
    # d/dr f_0(r*w) at r=1 is w*(1-w^2)/(1+w^2)^2.
    dr = div(mul(w, add(one, scale(power(w, 2), -1))), power(p, 2))
    # H = Im(f)/sqrt(3); partial_tau f = -w*sum a_j*w^(j+1)/P^2.
    dt = [div(scale(mul(w, power(w, j+1)), -1), power(p, 2))
          for j in range(1, 6)]
    h_tau = [x[1] for x in dt]
    radial = [-2*x/dr[1] for x in h_tau]
    # Tangent basis is (A, B, v0*C, v0*D, v0^2*E), from C031c.
    tangent = [[Q(-1, 2), 0, 0, 0, 0],
               [0, -200, 0, 0, 0],
               [0, 0, Q(-1, 2), 0, 0],
               [0, 200, 0, -200, 0],
               [Q(1, 2), 0, Q(1, 2), 0, Q(-1, 2)]]
    reduced = [sum(radial[j]*tangent[j][k] for j in range(5)) for k in range(5)]
    box_text = {
        'A': ('3.7172599285e-5', '3.7172599286e-5'),
        'B': ('1.4417393139e-7', '1.4417393141e-7'),
        'C': ('6.6303168020e-10', '6.6303168031e-10'),
        'D': ('3.2136641485e-12', '3.2136641527e-12'),
        'E': ('1.5876934435e-14', '1.5876934595e-14')}
    boxes = {k: tuple(map(Q, x)) for k, x in box_text.items()}
    source = HERE / 'quadratic-tangent-certificate-1316.json'
    saved = json.loads(source.read_text())
    A, B, C, D, E = [boxes[k] for k in 'ABCDE']
    v = (160000-A[1]/C[0], 160000-A[0]/C[1])
    components = [A, B, imul(v, C), imul(v, D), imul(imul(v, v), E)]
    interval = (Q(0), Q(0))
    for c, x in zip(reduced, components):
        interval = iadd(interval, iscale(x, c))
    simple = (Q('-0.000024'), Q('-0.000022'))
    checks = {
        'unit_distinct_nonreal_conjugates': mul(w, wc) == one and w != wc and w[1] != 0,
        'base_denominators_w_and_conjugate': p == w and pc == wc,
        'base_denominator_norms_one': mul(p, conj(p)) == one and mul(pc, conj(pc)) == one,
        'both_base_values_one': value == one and valuec == one,
        'radial_spatial_derivative_minus_i_sqrt3': dr == (0, -1),
        'normalized_scalar_jacobian_minus_one': dr[1] == -1,
        'parameter_partials_minus_powers': all(x == scale(power(w, j), -1)
                                             for j, x in enumerate(dt, 1)),
        'H_tau_coefficients': h_tau == [Q(-1, 2), Q(-1, 2), 0, Q(1, 2), Q(1, 2)],
        'squared_radius_derivative_coefficients': radial == [-1, -1, 0, 1, 1],
        'tangent_substitution': reduced == [1, 400, Q(1, 2), -200, Q(-1, 2)],
        'fixed_boxes_unchanged': all(boxes[k] == tuple(map(Q, saved['bounds']['input_boxes'][str(j)]))
                                    for j, k in enumerate('ABCDE', 2)),
        'positive_ordered_boxes': all(0 < x[0] <= x[1] for x in boxes.values()),
        'v_positive': Q(103935) < v[0] <= v[1] < Q(103936),
        'strict_inward_bound': simple[0] < interval[0] <= interval[1] < simple[1] < 0,
    }
    failures = [k for k, ok in checks.items() if not ok]
    inputs = [Path(__file__), source,
              ROOT / 'lemmas/C031c-quadratic-grunsky-local-positive-branch.md',
              ROOT / 'lemmas/C030z-positive-diagonal-grunsky-finite-scalar-reduction.md']
    report = {
        'status': 'passed' if not failures else 'failed', 'checks': checks, 'failures': failures,
        'scope': 'C031c, u=400, fixed angle pi/3, first order, fixed1307 boxes only',
        'field_convention': 'pair (x,y) means x+y*i*sqrt(3); H=Im(f)/sqrt(3)',
        'base': {'w': pair(w), 'w_conjugate': pair(wc), 'P': pair(p), 'P_conjugate': pair(pc),
                 'f': pair(value), 'f_conjugate': pair(valuec), 'f_radial_derivative': pair(dr)},
        'derivatives': {'H_r': str(dr[1]), 'f_tau_a_coefficients': list(map(pair, dt)),
                        'H_tau_a_coefficients': list(map(str, h_tau)),
                        'squared_radius_a_coefficients': list(map(str, radial)),
                        'tangent_basis': ['A', 'B', 'v0*C', 'v0*D', 'v0^2*E'],
                        'tangent_matrix': [[str(x) for x in row] for row in tangent],
                        'reduced_coefficients': list(map(str, reduced))},
        'bounds': {'boxes': {k: enc(x) for k, x in boxes.items()}, 'v0': enc(v),
                   'components': list(map(enc, components)), 'squared_radius_derivative': enc(interval),
                   'strict_simple_enclosure': enc(simple), 'required_upper_bound': '0'},
        'input_hashes': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in inputs},
        'inherited_contracts': 'C031c; fixed1307 inclusion; L019,L021,L025,L027,L036,L037,L917; conditional Decimal contracts',
        'conclusion': 'Strict inward first variation; qualitative scalar IFT gives distinct interior conjugate points with equal finite values for all sufficiently small positive tau. No effective interval or RH conclusion.'}
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print(f"{report['status']}: {len(checks)} checks; failures={failures}; {OUT.relative_to(ROOT)}")
    print(f'actual squared-radius derivative interval: [{interval[0]}, {interval[1]}]')
    print(f'simple enclosure: ({simple[0]}, {simple[1]}); required upper bound <0')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
