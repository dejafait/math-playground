"""Exact residual invariants; a factorization is not a root-count proof."""
from fractions import Fraction as F
from pathlib import Path
import json
from math import comb


class P(dict):
    def __init__(self, c=0):
        super().__init__(c if isinstance(c, dict) else ({(0, 0, 0): F(c)} if c else {}))
    def __add__(self, q):
        z = P(dict(self))
        for m, c in P(q).items():
            z[m] = z.get(m, F(0)) + c
        return P({m: c for m, c in z.items() if c})
    __radd__ = __add__
    def __neg__(self):
        return P({m: -c for m, c in self.items()})
    def __sub__(self, q):
        return self + -P(q)
    def __rsub__(self, q):
        return P(q) + -self
    def __mul__(self, q):
        z = {}
        for m, c in self.items():
            for n, d in P(q).items():
                a = tuple(i + j for i, j in zip(m, n))
                z[a] = z.get(a, F(0)) + c * d
        return P({m: c for m, c in z.items() if c})
    __rmul__ = __mul__
    def __pow__(self, n):
        z = P(1)
        for _ in range(n):
            z = z * self
        return z
    def divmod(self, q):
        q = P(q)
        assert q
        lead = max(q)
        rem, out = P(dict(self)), P(0)
        while rem:
            m = max(rem)
            if not all(i >= j for i, j in zip(m, lead)):
                break
            step = P({tuple(i-j for i, j in zip(m, lead)): rem[m]/q[lead]})
            out = out + step
            rem = rem - step*q
        return out, rem
    def sub(self, vals):
        z = P(0)
        for m, c in self.items():
            term = P(c)
            for a, v in zip(m, vals):
                term = term * (P(v)**a)
            z = z + term
        return z
    def encode(self):
        return [{'powers_l_k_t': list(m), 'coefficient': str(c)} for m, c in sorted(self.items())]


def v(i):
    m = [0, 0, 0]
    m[i] = 1
    return P({tuple(m): F(1)})


l, k, t = [v(i) for i in range(3)]
r = [P(1), 2*l, l*l+2*k, 2*l*k, k*k]
aa, bb = 1+4*t*l, 1+2*l+2*t*(l*l+2*k)
cc, dd = 1+4*l+6*t*(l*l+2*k), 2*l+2*(l*l+2*k)+12*t*l*k
ff, gg = -2*t, -2-12*t*l
det = aa*dd-bb*cc
nb, nc = ff*dd-bb*gg, aa*gg-ff*cc
pn = [P(0) for _ in range(7)]
for i, ri in enumerate(r):
    for j, qj in enumerate([nc, nb, det]):
        pn[i+j] = pn[i+j]+ri*qj
out = [pn[j]+((j+1)*pn[j+1] if j < 6 else 0)
       + (t*(j+1)*(j+2)*pn[j+2] if j < 5 else 0) for j in range(7)]
e, d, c, b, a = out[2:]
invariant_i = 12*a*e-3*b*d+c*c
invariant_j = 72*a*c*e+9*b*c*d-27*a*d*d-27*b*b*e-2*c*c*c
discriminant = F(1, 27)*(4*invariant_i**3-invariant_j**2)
factors = {'k': k, 't': t, 'det': det, 'input_separation': l*l-4*k}
reduced = discriminant
exponents = {}
for name, factor in factors.items():
    exponent = 0
    while reduced:
        quotient, remainder = reduced.divmod(factor)
        if remainder:
            break
        reduced = quotient
        exponent += 1
    exponents[name] = exponent
reconstruction = reduced
for name, exponent in exponents.items():
    reconstruction = reconstruction*factors[name]**exponent
# Clear negative t powers after L=t*l, K=t^2*k, then put
# K=(L^2-S)/4, S>0. The three variable slots now stand for L,S,z,
# with t=(9+z)/36 and 0<=z<=1. This is an exact positivity attempt,
# not a parameter sample or an assertion that every coefficient is positive.
clear_power = max(i+2*j-h for (i, j, h) in reduced)
scaled = P({(i, j, h-i-2*j+clear_power): c0
            for (i, j, h), c0 in reduced.items()})
transformed = scaled.sub([l, F(1, 4)*(l*l-k), F(1, 36)*(9+t)])
power_groups = {}
for (i, j, h), c0 in transformed.items():
    power_groups.setdefault(j, {}).setdefault(h, {})[i] = c0
bernstein_groups = {}
bad_constant_values = []
bernstein_reconstruction = P(0)
for j, zgroups in sorted(power_groups.items()):
    n = max(zgroups)
    for bindex in range(n+1):
        coefficient = {}
        for h in range(bindex+1):
            for i, c0 in zgroups.get(h, {}).items():
                coefficient[i] = coefficient.get(i, F(0))+F(comb(bindex, h), comb(n, h))*c0
        coefficient = {i: c0 for i, c0 in coefficient.items() if c0}
        key = f'S^{j};Bernstein_{bindex}_of_{n}'
        bernstein_groups[key] = {str(i): str(c0) for i, c0 in sorted(coefficient.items())}
        coeff_poly = P({(i, j, 0): c0 for i, c0 in coefficient.items()})
        bernstein_reconstruction = (bernstein_reconstruction
            + coeff_poly*comb(n, bindex)*t**bindex*(1-t)**(n-bindex))
        if coefficient.get(0, F(0)) < 0:
            bad_constant_values.append({'coefficient': key, 'L': '0',
                                        'value': str(coefficient[0])})
endpoint_s17 = sum((c0*(-F(1, 4))**17*F(5, 18)**(h-34+clear_power)
                   for (i, j, h), c0 in reduced.items() if i == 0 and j == 17), F(0))
checks = {'collision_constant': not out[0], 'collision_linear': not out[1],
          'discriminant_factorization': reconstruction == discriminant,
          'bernstein_reconstruction': bernstein_reconstruction == transformed,
          'independent_endpoint_s17_coefficient': endpoint_s17 == -F(5036661, 128)}
record = {
    'status': 'EXACT_INVARIANTS_NOT_ROOT_COUNT',
    'variables': ['l', 'k', 't'],
    'normalization': 'a*x^4+b*x^3+c*x^2+d*x+e=Delta*H; actual H has leading coefficient k^2',
    'domain': '1/4<=t<=5/18; k!=0; l^2>4k; Delta<0; 4*N_C*Delta-N_B^2>0',
    'invariant_i': invariant_i.encode(), 'invariant_j': invariant_j.encode(),
    'discriminant': discriminant.encode(), 'factor_exponents': exponents,
    'reduced_discriminant': reduced.encode(),
    'sign_attempt': {
        'change_of_variables': 'L=t*l; S=t^2*(l^2-4*k)>0; z=36*t-9 in [0,1]',
        'clearing_power': clear_power,
        'identity': 'transformed=t^clearing_power*reduced_discriminant after substitution',
        'transformed_L_S_z': [{'powers_L_S_z': list(m), 'coefficient': str(c0)}
                              for m, c0 in sorted(transformed.items())],
        'bernstein_coefficients_as_polynomials_in_L': bernstein_groups,
        'negative_coefficients_at_L_zero': bad_constant_values,
        'independent_endpoint_s17_coefficient': str(endpoint_s17),
        'actual_coefficient_bound': '-5036661/128 < 0 at L=0,z=1 for S^17',
        'required_coefficient_bound': 'Every coefficient polynomial in L must be >=0 on the whole real line for this coefficientwise certificate.',
        'failed_sign_conditions': len(bad_constant_values),
        'interpretation': 'Any negative value blocks coefficientwise positivity in this representation; it is not a negative discriminant or a count witness.'},
    'checks': checks, 'failures': [n for n, ok in checks.items() if not ok],
    'actual_bounds': 'No sign or root count follows from factor extraction alone.',
    'required_bounds': 'H must have four real roots to exclude this collision family.'}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(record, indent=2)+'\n')
print('Exact invariant checks:', sum(checks.values()), '/', len(checks))
print('Extracted exponents:', exponents)
print('Discriminant/reduced term counts:', len(discriminant), len(reduced))
print('Bernstein coefficient polynomials:', len(bernstein_groups),
      '; negative values at L=0:', len(bad_constant_values))
print('Sign-certificate failure: S^17 endpoint coefficient =', endpoint_s17, '; required >=0.')
print('Actual: sign unresolved. Required: four real residual roots, including multiplicities.')
print('Failures:', record['failures'])
print('Full certificate:', path)
