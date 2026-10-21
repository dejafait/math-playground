#!/usr/bin/env python3
"""Independent L436 audit: saved tape plus binary finite-sum evaluation.

Does not import or execute the construction program. All arithmetic is
integer/Fraction; the new finite evaluator uses block concatenation, not
the construction's differentiated rational closed forms.
"""
from fractions import Fraction as F
from math import isqrt, prod
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'three_prime_finite_fejer_witness_certificate.json'
raw = SOURCE.read_bytes()
data = json.loads(raw)
checks = {}
records = {}
N = 131071
assert data['degree_each_coordinate'] == N
assert data['kernel_terms_each_coordinate'] == N + 1

# Reconstruct and check the entire partial-fraction identity, not its flag.
def multiply_polynomials(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

coefficients = {}
for p in (2, 3, 5):
    d = data['local'][str(p)]
    parts = {F(k): list(map(F, v)) for k, v in d['partial_fractions'].items()}
    roots = {F(1): 1, F(p): 2, F(1, p*p): 2, F(p**3): 1}
    assert set(parts) == set(roots)
    residual = [F(0)]*6
    residual[3] = F(p**3*(p-1)**2)
    for a, multiplicity in roots.items():
        assert len(parts[a]) == multiplicity
        for order, coefficient in enumerate(parts[a], 1):
            polynomial = [F(1)]
            for b, m in roots.items():
                for _ in range(m - (order if b == a else 0)):
                    polynomial = multiply_polynomials(polynomial, [-b, F(1)])
            for j, value in enumerate(polynomial):
                residual[j] += coefficient*value
    checks[f'p{p}_full_rational_identity'] = residual == [F(0)]*6
    D = parts[F(1)][0]
    O, T = parts[F(p)]
    U, V = parts[F(1, p*p)]
    J = parts[F(p**3)][0]
    a = F(1, p*p)
    A, B, C = -O/p+T/p**2, T/p**2, -J/p**3
    E, G = U/a-V/a**2, V/a**2
    b0 = A+C
    coefficients[p] = A, B, C, D, E, G, b0
    checks[f'p{p}_recorded_coefficients'] = (
        [A, B, C] == list(map(F, d['positive_coefficients_A_B_C']))
        and [D, E, G] == list(map(F, d['negative_coefficients_D_E_G']))
        and b0 == F(d['B0']) == F(d['independent_B0']) > 0)
    checks[f'p{p}_inner_boundary'] = (E+G)*a == U
    lo, hi = F(d['radius_lower']), F(d['radius_upper'])
    checks[f'p{p}_radii'] = 1 < lo < hi < p and lo**2 < p < hi**2
    z, w, t = hi/p, hi/p**3, a/lo
    s = (A/(1-z)+B*z/(1-z)**2+C/(1-w)
         +D/(lo-1)+E*t/(1-t)+G*t/(1-t)**2)/b0
    m = (A*z/(1-z)**2+B*z*(1+z)/(1-z)**3+C*w/(1-w)**2
         +D*lo/(lo-1)**2+E*t/(1-t)**2+G*t*(1+t)/(1-t)**3)/b0
    checks[f'p{p}_complete_mass_moment'] = (
        0 < s == F(d['normalized_mass_upper_exact']) < F(d['normalized_mass_upper_simple'])
        and 0 < m == F(d['normalized_first_moment_upper_exact']) < F(d['normalized_first_moment_upper_simple']))
    records[str(p)] = {'cleared_residual': list(map(str, residual)),
                        'mass_bound': str(s), 'first_moment_bound': str(m)}

mass = [F(data['local'][str(p)]['normalized_mass_upper_simple']) for p in (2, 3, 5)]
moment = [F(data['local'][str(p)]['normalized_first_moment_upper_simple']) for p in (2, 3, 5)]
total = sum(moment[i]*prod(mass[j] for j in range(3) if i != j) for i in range(3))
upper = -F(3, 100)+total/(N+1)
checks['joint_moment_and_degree'] = total == F(1995293, 1000) and upper == -F(1936867, 131072000) < -F(1, 100)
checks['imported_point_bound'] = F(data['effective_bound']['point_upper_imported_L435']) < -F(3, 100)

# Verify every saved operation including causal indexing, roots and divisions.
unit = 2**data['interval_arithmetic']['bits']
tape = data['interval_arithmetic']['tape']
saved = []
tape_failures = []
division_count = 0
sqrt_count = 0
for i, entry in enumerate(tape):
    lo, hi = F(int(entry['lo_units']), unit), F(int(entry['hi_units']), unit)
    ids = entry['args']
    assert all(isinstance(j, int) and 0 <= j < i for j in ids)
    operands = [saved[j] for j in ids]
    op = entry['op']
    if op in ('constant', 'sqrt2_bracket'):
        assert not ids
        l, h = map(F, entry['exact_input_bounds'])
        if op == 'constant':
            assert l == h
        else:
            sqrt_count += 1
            assert 0 < l < h and l*l < 2 < h*h
    elif op == 'add':
        (a, b), (c, d) = operands
        l, h = a+c, b+d
    elif op == 'negate':
        ((a, b),) = operands
        l, h = -b, -a
    elif op == 'multiply':
        (a, b), (c, d) = operands
        products = [a*c, a*d, b*c, b*d]
        l, h = min(products), max(products)
    elif op == 'inverse':
        ((a, b),) = operands
        assert a*b > 0
        division_count += 1
        l, h = 1/b, 1/a
    else:
        raise ValueError(op)
    if not lo <= l <= h <= hi:
        tape_failures.append(i)
    saved.append((lo, hi))
checks['all_saved_operations'] = not tape_failures and len(tape) == 2993 and sqrt_count == 1
for name, summary in list(data['finite_contraction']['local_smoothed_factors'].items()) + [('product', data['finite_contraction']['complete_product'])]:
    checks[f'saved_summary_{name}'] = all(
        saved[index] == tuple(map(F, summary[part]))
        for index, part in zip(summary['tape_indices'], ('re', 'im')))

# Independent outward integer-grid arithmetic at 160 bits.
SCALE = 2**160
def box(x):
    v = F(x)*SCALE
    return v.numerator//v.denominator, -((-v.numerator)//v.denominator)
def add(a, b):
    return a[0]+b[0], a[1]+b[1]
def neg(a):
    return -a[1], -a[0]
def mul(a, b):
    v = [x*y for x in a for y in b]
    return min(v)//SCALE, -((-max(v))//SCALE)
def reciprocal(a):
    assert a[0]*a[1] > 0
    l, h = F(SCALE*SCALE, a[1]), F(SCALE*SCALE, a[0])
    return l.numerator//l.denominator, -((-h.numerator)//h.denominator)
def scalar(z, q):
    return mul(z[0], box(q)), mul(z[1], box(q))
def cx(re=0, im=0):
    return box(re), box(im)
def plus(z, w):
    return add(z[0], w[0]), add(z[1], w[1])
def times(z, w):
    return add(mul(z[0], w[0]), neg(mul(z[1], w[1]))), add(mul(z[0], w[1]), mul(z[1], w[0]))
def invert(z):
    v = reciprocal(add(mul(z[0], z[0]), mul(z[1], z[1])))
    return mul(z[0], v), mul(neg(z[1]), v)
def finite(z):
    # s_k = sum_{j=0}^{m-1} j^k z^j, k=0,1,2; q=z^m.
    m, q, s0, s1, s2 = 1, z, cx(1), cx(), cx()
    while m < N+1:
        new0 = plus(s0, times(q, s0))
        new1 = plus(s1, times(q, plus(s1, scalar(s0, m))))
        new2 = plus(s2, times(q, plus(plus(s2, scalar(s1, 2*m)), scalar(s0, m*m))))
        q, m, s0, s1, s2 = times(q, q), 2*m, new0, new1, new2
    assert m == N+1
    return plus(s0, scalar(s1, -F(1, m))), plus(s1, scalar(s2, -F(1, m)))

root = isqrt(2*SCALE*SCALE)
assert root*root < 2*SCALE*SCALE < (root+1)**2
points = {2: cx(1, 1), 3: (box(1), (root, root+1)), 5: cx(1, 2)}
computed = {}
for p, u in points.items():
    A, B, C, D, E, G, b0 = coefficients[p]
    fp, gp = finite(scalar(u, F(1, p)))
    fw, _ = finite(scalar(u, F(1, p**3)))
    fm, _ = finite(invert(u))
    ft, gt = finite(scalar(invert(u), F(1, p*p)))
    terms = [scalar(fp, A), scalar(gp, B), scalar(fw, C),
             scalar(plus(fm, cx(-1)), D), scalar(plus(ft, cx(-1)), E), scalar(gt, G)]
    value = cx()
    for term in terms:
        value = plus(value, term)
    computed[str(p)] = scalar(value, 1/b0)
computed['product'] = times(times(computed['2'], computed['3']), computed['5'])
independent = {}
for name, value in computed.items():
    original = (data['finite_contraction']['complete_product'] if name == 'product'
                else data['finite_contraction']['local_smoothed_factors'][name])
    independent[name] = {}
    for k, part in enumerate(('re', 'im')):
        l, h = (F(x, SCALE) for x in value[k])
        a, b = map(F, original[part])
        checks[f'independent_{name}_{part}_inside_saved'] = a <= l <= h <= b
        independent[name][part] = [str(l), str(h)]
checks['independent_strict_sign'] = F(computed['product'][0][1], SCALE) < -F(1, 100)
checks['original_claimed_enclosure'] = list(map(F, data['finite_contraction']['complete_product']['re'])) == [
    -F(2584151874139662159245424023, 2**96), -F(2584151874139662159245423689, 2**96)]
failures = [name for name, valid in checks.items() if not valid]
certificate = {
    'scope': 'Independent audit of L436 algebra, saved operation inclusions and complete finite sums; analytic reasoning is canonical in L436.',
    'source_sha256': hashlib.sha256(raw).hexdigest(),
    'degree': N, 'independent_bits': 160,
    'local': records, 'joint_first_moment_upper': str(total),
    'apriori_upper': str(upper), 'required_upper': '-1/100',
    'saved_tape_operations': len(tape), 'nonzero_divisions': division_count,
    'tape_failures': tape_failures, 'independent_finite_contraction': independent,
    'checks': checks, 'failures': failures,
}
output = HERE / 'three_prime_finite_fejer_audit_certificate.json'
output.write_text(json.dumps(certificate, indent=2)+'\n')
print(f'Independent audit: {sum(checks.values())}/{len(checks)} checks; failures={failures}.')
print(f'Entire saved tape: {len(tape)} operations, {division_count} nonzero divisions; failures={tape_failures}.')
print(f'First-moment upper={total}; a priori integral upper={upper}; required < -1/100.')
print('Independent finite real enclosure:', independent['product']['re'])
print(f'Complete audit certificate: {output}')
if failures:
    raise SystemExit(1)
