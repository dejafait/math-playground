"""Exact algebra for C020p. The analytic/count proof is in the lemma."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

# Sparse rational polynomials in x,b,c,t, in that order.
Z = (0, 0, 0, 0)
def const(c):
    return {Z: F(c)} if c else {}
def var(i):
    m = [0]*4
    m[i] = 1
    return {tuple(m): F(1)}
def add(*ps):
    result = {}
    for p in ps:
        for m, c in p.items():
            result[m] = result.get(m, F(0))+c
    return {m:c for m,c in result.items() if c}
def mul(*ps):
    result = const(1)
    for p in ps:
        product = {}
        for m,c in result.items():
            for n,d in p.items():
                k = tuple(a+b for a,b in zip(m,n))
                product[k] = product.get(k,F(0))+c*d
        result = {m:c for m,c in product.items() if c}
    return result
def scale(p,c):
    return mul(const(c),p)
def power(p,n):
    return mul(*([p]*n))
def dx(p,k=1):
    for _ in range(k):
        result = {}
        for m,c in p.items():
            if m[0]:
                n = (m[0]-1,)+m[1:]
                result[n] = c*m[0]
        p = result
    return p
def substitute(p,i,value):
    result = {}
    for m,c in p.items():
        n = list(m)
        n[i] = 0
        result = add(result,{tuple(n): c*F(value)**m[i]})
    return result
def encoded(p):
    return [{'powers_x_b_c_t': list(m), 'coefficient': str(c)}
            for m,c in sorted(p.items())]

x,b,c,t = [var(i) for i in range(4)]
p = mul(power(x,4),add(power(x,2),mul(b,x),c))
out = add(p,dx(p),mul(t,dx(p,2)))
H = add(power(x,4),mul(add(b,const(6)),power(x,3)),
        mul(add(c,scale(b,5),scale(t,30)),power(x,2)),
        mul(add(scale(c,4),scale(mul(t,b),20)),x),scale(mul(t,c),12))
Ct = add(power(x,2),scale(x,4),scale(t,12))
quotient = add(power(x,2),mul(add(b,const(2)),x),c,b,scale(t,18),const(-8))
A = add(mul(add(const(32),scale(t,-96)),x),scale(t,96),scale(power(t,2),-216))
B = add(mul(add(scale(t,8),const(-4)),x),scale(t,-12))
a0 = add(const(-64),scale(t,288),scale(power(t,2),-216))
a1 = add(const(32),scale(t,-96))
b0 = add(const(8),scale(t,-28))
b1 = add(scale(t,8),const(-4))
s2 = add(const(4),scale(t,-12))
weight_gap = add(mul(power(b1,2),s2),scale(power(b0,2),-1))
weight_gap_expected = scale(mul(power(t,2),add(const(5),scale(t,-16))),48)
weighted_half_s = add(mul(b0,a1),scale(mul(b1,a0),-1))
weighted_expected = scale(mul(power(t,2),add(scale(t,18),const(-5))),96)
appell = add(power(x,6),scale(power(x,5),6),scale(mul(t,power(x,4)),30))
sector_ratio_squared = add(scale(t,4),const(-1))
disc = add(const(36),scale(t,-120))
flags = {
    'output_equals_x2_H': out == mul(power(x,2),H),
    'complete_division_identity': H == add(mul(Ct,quotient),A,mul(b,B)),
    'A_at_minus_two': substitute(A,0,-2) == a0,
    'A_x_coefficient': dx(A) == a1,
    'B_at_minus_two': substitute(B,0,-2) == b0,
    'B_x_coefficient': dx(B) == b1,
    'squared_weight_gap_identity': weight_gap == weight_gap_expected,
    'weighted_identity_after_division_by_2s': weighted_half_s == weighted_expected,
    'weighted_sign_factor_at_lower_endpoint': substitute(add(scale(t,18),const(-5)),3,F(1,4)) == const(F(-1,2)),
    'weighted_sign_factor_at_upper_endpoint': substitute(add(scale(t,18),const(-5)),3,F(5,18)) == {},
    's2_endpoint_bounds': [substitute(s2,3,z) for z in [F(1,4),F(5,18)]] == [const(1),const(F(2,3))],
    'b0_lower_bound': substitute(b0,3,F(5,18)) == const(F(2,9)),
    '5_minus_16t_lower_bound': substitute(add(const(5),scale(t,-16)),3,F(5,18)) == const(F(5,9)),
    'weight_gap_bound_arithmetic': 48*F(1,4)**2*F(5,9) == F(5,3),
    'sector_ratio_squared_upper': substitute(sector_ratio_squared,3,F(5,18)) == const(F(1,9)),
    'appell_discriminant_lower': substitute(disc,3,F(5,18)) == const(F(8,3)),
    'appell_identity': appell == add(power(x,6),dx(power(x,6)),mul(t,dx(power(x,6),2))),
    'walsh_linear_weight': F(factorial(5)*6,factorial(6)) == 1,
    'walsh_quadratic_weight_without_t': F(factorial(4)*30,factorial(6)) == 1,
}
record = {
    'scope': 'Fourfold real input root; one quadratic q=1+aD+t a^2D^2, 1/4<=t<=5/18. Full sextic target unresolved.',
    'encoding': 'Sparse exact rational coefficients; monomial powers ordered x,b,c,t.',
    'identities': {name:encoded(poly) for name,poly in {
        'input_normalized':p, 'output_normalized':out, 'H':H,
        'C_t':Ct, 'division_quotient':quotient, 'A_t':A, 'B_t':B,
        'a0':a0,'a1':a1,'b0':b0,'b1':b1,'s_squared':s2,
        'weight_gap_expanded':weight_gap,
        'weighted_sum_divided_by_2s':weighted_half_s,
        'appell':appell}.items()},
    'actual_bounds': {'appell_discriminant_over_a_squared_lower':'8/3',
                      'b0_lower':'2/9', 's_squared_lower':'2/3',
                      'squared_weight_gap_lower':'5/3',
                      'weighted_sign_factor_range':['-1/2','0'],
                      'real_input_count':4,'proved_real_output_lower':4},
    'required_bounds': {'appell_discriminant':'>=0','squared_weight_gap':'>0',
                        'weighted_sign_factor':'<=0; zero handled separately',
                        'witness_real_output_count':2},
    'checks':flags, 'failures':[k for k,v in flags.items() if not v],
    'limits':'Algebra cross-check only; see C020p for whole-interval inequalities, multiplicities, Walsh and limitations. Does not settle separated input roots or products.',
}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(record,indent=2)+'\n')
print('Actual bounds:',record['actual_bounds'])
print('Required bounds:',record['required_bounds'])
print('Algebra checks:',len(flags),'; failures:',record['failures'])
print('Full certificate:',path)
if record['failures']:
    raise SystemExit(1)
