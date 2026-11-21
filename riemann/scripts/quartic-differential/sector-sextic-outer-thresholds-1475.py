"""Exact symbolic outer-pair reduction; inequalities are proved in C020s."""
from fractions import Fraction as F
from pathlib import Path
import json


class P(dict):
    def __init__(self, c=0):
        super().__init__(c if isinstance(c, dict) else ({(0, 0, 0): F(c)} if c else {}))

    def __add__(self, q):
        z = dict(self)
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
                z[a] = z.get(a, F(0)) + c*d
        return P({m: c for m, c in z.items() if c})

    __rmul__ = __mul__

    def __pow__(self, n):
        z = P(1)
        for _ in range(n):
            z *= self
        return z

    def sub(self, values):
        z = P(0)
        for m, c in self.items():
            term = P(c)
            for a, v in zip(m, values):
                term *= P(v)**a
            z += term
        return z

    def encode(self):
        return [{'powers': list(m), 'coefficient': str(c)}
                for m, c in sorted(self.items())]

    def fmt(self, names=('W', 't', 'H')):
        return ' + '.join(str(c) + ''.join('*'+v+(f'^{a}' if a > 1 else '')
                    for v, a in zip(names, m) if a)
                    for m, c in sorted(self.items(), reverse=True)) or '0'


def var(i):
    m = [0, 0, 0]
    m[i] = 1
    return P({tuple(m): F(1)})


W, t, H = [var(i) for i in range(3)]
V, U8 = W*W+12*t-4, W*W+8*t-4
inner = V*((W-2)*U8-(W+2)*(W-2+8*t)**2) + 16*t*W*(W-2+9*t)*U8
reduced = ((10*t-3)*W**3 + (6-24*t)*W**2
           + (48*t*t-60*t+12)*W - 192*t*t+136*t-24)
# Numerator of E after multiplying by 4W^2*(W^2+8t-4).
cleared_E = ((W-2)**2*V**2*U8
             + 2*W*(W-2)*V*(8*t*(W-2)+72*t*t)*U8
             - (W*W-4)*V**2*(W-2+8*t)**2)
factored_E = 8*t*(W-2)*V*reduced
# W now denotes s=r-2 in these two polynomial identities.
upper = (-(3-10*t)*W**3-12*(1-3*t)*W**2
         -12*t*(3-4*t)*W-96*t*t)
lower = ((3-10*t)*W**3+12*(2-7*t)*W**2
         +12*(4-13*t-4*t*t)*W+16*t*(5-18*t))
# Generic variables u,v,H, with t renamed only in this check.
u, v, hh = W, t, H
su, sv = u*u-hh, v*v-hh
# Verify the coefficient of t in the difference of the two rational terms.
rational_difference = u*sv-v*su
original_Aprod_coeffs = [su*sv, 8*(u*sv+v*su), 64*u*v]
symmetric_Aprod_coeffs = [(u*v+hh)**2-hh*(u+v)**2,
                         8*(u+v)*(u*v-hh), 64*u*v]
# Verify E's symmetric expansion using independent variables w,z,t and H=H.
# Three-variable arithmetic suffices coefficient by coefficient in t.
w, z, hh = W, t, H
Aprod_coeffs = [(z+hh)**2-hh*w*w, 8*w*(z-hh), 64*z]
E_coeffs = [Aprod_coeffs[0], Aprod_coeffs[1], Aprod_coeffs[2]+8*(z+hh)]
sym_E_coeffs = [(z+hh)**2-hh*w*w, 8*w*(z+hh)-16*hh*w,
                72*(z+hh)-64*hh]
# Restore the names W,t,H for pair-factor checks.
pair_constant_cleared = (W*W-4)*V**2-4*W*W*H*(V-4*t)
pair_relation = (W*W-4)*V**2-4*W*W*H*U8
lower_product_num = (W+2)*V-2*W*H
upper_product_num = (W-2)*V-2*W*H
J = W**4+4*W**3+(12*t-2*H)*W*W-4*H*W+H*H-4*t*H
checks = {
    'odd_reference_difference': J-J.sub([-W,t,H]) == 8*W*(W*W-H),
    'rational_difference': rational_difference == (v-u)*(u*v+hh),
    'A_product_symmetric_expansion': original_Aprod_coeffs == symmetric_Aprod_coeffs,
    'E_symmetric_expansion': E_coeffs == sym_E_coeffs,
    'pair_sum_product_lower': (W+2)*V+(W-2)*V == 2*W*V,
    'pair_product_difference': (W+2)*V-(W-2)*V == 4*V,
    'pair_constant_relation': pair_constant_cleared == pair_relation,
    'pair_factor_constant_coefficient': (
        lower_product_num*upper_product_num-4*W*W*(H*H-4*t*H) == pair_relation),
    'pair_factor_linear_coefficient': (
        (-2-W)*upper_product_num+(-2+W)*lower_product_num == 8*W*H),
    'inner_reduction': inner == 8*t*reduced,
    'cleared_E_factorization': cleared_E == factored_E,
    'upper_branch_shift': reduced.sub([W+2,t,H]) == upper,
    'lower_branch_shift': reduced.sub([-W-2,t,H]) == lower,
    'lower_branch_endpoint_bounds': (
        3-10*F(5,18) == F(2,9)
        and 2-7*F(5,18) == F(1,18)
        and 4-13*F(5,18)-4*F(5,18)**2 == F(13,162)
        and 5-18*F(5,18) == 0),
    'upper_branch_endpoint_bounds': (
        1-3*F(5,18) == F(1,6)
        and 3-4*F(5,18) == F(17,9)
        and 96*F(1,4)**2 == 6),
}
polys = {'V': V, 'denominator_factor': U8, 'inner': inner,
         'reduced': reduced, 'cleared_E': cleared_E, 'factored_E': factored_E,
         'upper_shift_s': upper, 'lower_shift_s': lower,
         'pair_relation': pair_relation}
record = {
    'status': 'EXACT_IDENTITIES_SUPPORT_C020S_UNIFORM_PROOF',
    'variables': ['W', 't', 'H'],
    'qualifications': ['H denotes h^2, not the residual polynomial.',
                       'In upper_shift_s and lower_shift_s the first variable denotes s=r-2>0.',
                       'Pair-root locations, r>2, sign arguments and multiplicity claims require the proof in C020s, not these algebra checks.'],
    'polynomials': {n: p.encode() for n, p in polys.items()},
    'formulas': {n: p.fmt() for n, p in polys.items()},
    'checks': checks,
    'failures': [n for n, ok in checks.items() if not ok],
    'actual_bounds': {
        'lower_branch': 'B_t(-r)>=(2/9)s^3+(2/3)s^2+(26/27)s>0 for s=r-2>0; omitted constant 16t(5-18t)>=0.',
        'upper_branch': 'B_t(r)<=-96t^2<=-6<0.',
        'outer_comparisons': 'E<0 for both outer pairs; therefore b_1>b_2 and b_3>b_4 (analytic proof in C020s).',
        'family_count': 'T((y^2-h^2)^2 Q) has at least four distinct real roots for every monic real quadratic Q; a double-collision residual has four simple real roots.'
    },
    'required_bounds': {
        'intermediate': 'E<0 for both W=-r and W=r, r>2, 1/4<=t<=5/18.',
        'full_target': 'An exact (2,4) witness or impossibility for the entire nominated rational sector-sextic class; unresolved.'
    },
    'limitations': ['C020s is unaudited; the script is not an independent proof audit.',
                   'No general four-real-root-input, higher-symbol-degree, product or deformation result.',
                   'No actual-Xi transfer or RH conclusion.']
}
record['development_failures'] = ['An initial assertion guessed divisibility of inner by t^2; exact expansion rejected it. The correct reduction divides by 8t only. No output theorem used the failed guess.']
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(record, indent=2)+'\n')
print('Exact checks:', sum(checks.values()), '/', len(checks))
print('Actual lower B >= (2/9)s^3+(2/3)s^2+(26/27)s > 0; upper B <= -6.')
print('Required: opposite branch signs, giving E<0; full sextic (2,4) target unresolved.')
print('Failures:', record['failures'])
print('Full certificate:', path)
if record['failures']:
    raise SystemExit(1)
