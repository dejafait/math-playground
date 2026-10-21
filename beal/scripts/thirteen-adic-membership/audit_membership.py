"""Independent L064 replay: sparse polynomial arithmetic, no original code imports.

Source coefficients are transcribed from FNS (2019), printed pp.26--27.
Only the existing canonical and scalar-three witnesses are tested.
"""
from fractions import Fraction
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
OLD = json.loads((HERE / 'membership-certificate.json').read_text())
P = 13
checks = {}
evidence = {}

def check(name, condition):
    checks[name] = bool(condition)

def poly(coeffs, modulus=None):
    return clean(dict(enumerate(coeffs)), modulus)

def clean(a, modulus=None):
    return {i: (c % modulus if modulus else c) for i, c in a.items()
            if (c % modulus if modulus else c)}

def plus(a, b, modulus=None):
    r = a.copy()
    for i, c in b.items(): r[i] = r.get(i, 0) + c
    return clean(r, modulus)

def times(a, b, modulus=None):
    r = {}
    for i, c in a.items():
        for j, d in b.items(): r[i+j] = r.get(i+j, 0) + c*d
    return clean(r, modulus)

def scale(a, c, modulus=None):
    return clean({i: c*v for i, v in a.items()}, modulus)

def division(a, b):
    r, q = clean(a, P), {}
    while r and max(r) >= max(b):
        shift = max(r)-max(b)
        c = r[max(r)]*pow(b[max(b)], -1, P) % P
        q[shift] = c
        r = plus(r, {i+shift: -c*v for i, v in b.items()}, P)
    return q, r

def rem(a, b): return division(a, b)[1]

def power(a, n, h=None):
    # Left-to-right binary powering, with optional reduction over F13.
    r = {0: 1}
    for bit in bin(n)[2:]:
        r = times(r, r, P if h else None)
        if h: r = rem(r, h)
        if bit == '1':
            r = times(r, a, P if h else None)
            if h: r = rem(r, h)
    return r

def bezout(a, b):
    r0, r1 = clean(a, P), clean(b, P)
    s0, s1, t0, t1 = {0: 1}, {}, {}, {0: 1}
    while r1:
        q, r2 = division(r0, r1)
        r0, r1 = r1, r2
        s0, s1 = s1, plus(s0, scale(times(q, s1, P), -1, P), P)
        t0, t1 = t1, plus(t0, scale(times(q, t1, P), -1, P), P)
    u = pow(r0[max(r0)], -1, P)
    return tuple(scale(z, u, P) for z in (r0, s0, t0))

def asc(a): return [a.get(i, 0) for i in range(max(a, default=0)+1)]

def bezout_record(a, b):
    g, u, v = bezout(a, b)
    assert plus(times(u, a, P), times(v, b, P), P) == g
    return {'gcd': asc(g), 'u': asc(u), 'v': asc(v)}

# Independent primary-source transcription; coefficients ascending.
a = poly([-39176677684144739,108160113602504237,74593328129816300,
          420015065507429,-14545268641576841,-1895608370650736,
          576036867160006,82165362766027,2536749758583,19162005343,
          21559874,743])
b1 = poly([-707351591,271927184,65058492,1304157,4518,1])
b2 = poly([-37315543,-37789861,-3406817,3626752,192189,1])
b = times(b1, b2)
d = power(poly([-16,1]),11)
h = poly([9789217,4971236,1333262,-52820,1])
J = poly([-104748564078368391,199736619430410535,159480622275659333,
          6839041777752481,-29669709666741936,-4074814667347831,
          1134855511654843,164063633585170,5072626276355,38323813979,
          43119747,1486])
m = poly([-380,-774,-1062,-456,258,468,104,-126,-6,6,-6,0,1])
g = poly([-20,-10,-1,1])
x = {1:1}
F3 = plus(plus(power(h,3),scale(J,3)),scale(d,-9))
F12 = plus(plus(power(h,3),scale(J,12)),scale(d,-144))
G = poly([10,0,1,12,5,9,1],P)
M = clean(F3,P)
mbar = clean(m,P)
check('J_source_identity', plus(scale(a,2),scale(b,-1)) == J)
identity = plus(plus(plus(times(a,a),scale(times(a,b),-1)),
                     scale(times(times(b,b),g),-1)),times(d,power(h,3)))
check('exact_integer_elimination_identity', identity == {})
check('canonical_residue_square', clean(F12,P) == times(G,G,P))
check('canonical_scalar_residue', (9261*pow(8,-1,P))%P == 12 == 1728%P)
check('K_source_reduction', asc(mbar) == OLD['K_polynomial_mod13'])
check('scalar_three_monic_degree12', max(F3)==12 and F3[12]==1)
check('scalar_three_reduction', asc(M)==OLD['target_scalar_three']['polynomial'])
evidence['integer_coefficients'] = {name:asc(v) for name,v in
    [('a',a),('b1',b1),('b2',b2),('b',b),('d',d),('h',h),('J',J),('m',m),('F3',F3)]}
evidence['elimination_residual'] = asc(identity)

target_rows = [r for r in OLD['primitive_regular_residue_fibers'] if r['scalar_residue']==3]
check('unique_saved_target_row',len(target_rows)==1)
target = target_rows[0]
evidence['irreducibility'] = {}
for name,H,n,saved in [('mbar',mbar,12,OLD['K_factors'][0]),
                        ('G',G,6,OLD['canonical_branch']['square_factor']),
                        ('M',M,12,target['factors'][0])]:
    # Recompute every remainder directly from x, not from the previous remainder.
    R = [power(x,P**i,H) for i in range(n+1)]
    tests = []
    for ell in (2,3):
        diff = plus(R[n//ell],scale(x,-1,P),P)
        record = bezout_record(H,diff)
        record.update({'prime':ell,'remainder_minus_x':asc(diff)})
        tests.append(record)
        check(name+'_gcd_'+str(ell), record['gcd']==[1])
    derivative = clean({i-1:i*c for i,c in H.items() if i},P)
    sep = bezout_record(H,derivative)
    check(name+'_separable',sep['gcd']==[1])
    check(name+'_frobenius_closure',R[n]==x)
    check(name+'_full_saved_sequence', [asc(r) for r in R]==saved['frobenius_remainders'])
    check(name+'_saved_factor_degree', asc(H)==saved['factor'] and n==saved['degree'])
    check(name+'_full_saved_gcd_tests',
          [{k:t[k] for k in ('prime','remainder_minus_x','gcd')} for t in tests]==saved['gcd_tests'])
    evidence['irreducibility'][name] = {'degree':n,'factor':asc(H),
        'frobenius_remainders':[asc(r) for r in R],'gcd_tests':tests,'separability':sep}

evidence['points'] = {}
for name,H,s,y_coeff,w_coeff,saved in [
    ('canonical',G,12,[10,4,3,8,7,5],[0,2,6,0,3,3],OLD['canonical_branch']),
    ('three',M,3,[1,10,12,4,5,7,5,2,5,5,4,5],[5,3,10,11,11,6,9,12,7,9,0,8],OLD['target_scalar_three'])]:
    y,w = poly(y_coeff,P),poly(w_coeff,P)
    bg,dg = bezout_record(clean(b,P),H),bezout_record(clean(d,P),H)
    check(name+'_b_unit',bg['gcd']==[1]==saved['b_gcd'])
    check(name+'_d_unit',dg['gcd']==[1]==saved['d_gcd'])
    reconstruction = rem(plus(plus(times(b,y),a),scale(d,-s)),H)
    curve = rem(plus(plus(times(y,y),y),scale(g,-1)),H)
    f = rem(plus(times(poly([-4,1]),y),poly([-55,30,-4])),H)
    fifth = power(w,5,H)
    deriv = scale(power(w,4,H),5,P)
    deriv_gcd = bezout_record(deriv,H)
    check(name+'_reconstruction',reconstruction=={})
    check(name+'_curve',curve=={})
    check(name+'_nonzero_fifth_root',bool(w) and bool(f) and fifth==f)
    check(name+'_hensel_unit_derivative',deriv_gcd['gcd']==[1])
    check(name+'_saved_fifth_data',asc(w)==saved['fifth_root_residue'] and
          asc(f)==saved['f_residue']==saved['fifth_root_check'])
    check(name+'_saved_y',asc(y)==(saved['y_residue'] if name=='canonical' else target['points'][0]['y']))
    evidence['points'][name]={'y':asc(y),'w':asc(w),'f':asc(f),'w_fifth':asc(fifth),
        'reconstruction_residual':asc(reconstruction),'curve_residual':asc(curve),
        'b_bezout':bg,'d_bezout':dg,'fifth_derivative_bezout':deriv_gcd,
        'hensel_value_valuation_lower_bound':1,'hensel_derivative_valuation':0,
        'required_strict_lower_bound':0}

# Exact scalar roots and the common power identities, independently recomputed.
def val(n):
    if not n: raise ValueError('valuation of zero not needed')
    v=0
    while n%P==0: n//=P; v+=1
    return v

def vf(q): return val(q.numerator)-val(q.denominator)

def pair(q): return [q.numerator,q.denominator]

A,C = Fraction(16,575),Fraction(9216,575)
ra,rc = 1,10
av,cv = Fraction(ra**3)-A,Fraction(rc**11)-C
ad,cd = Fraction(3*ra**2),Fraction(11*rc**10)
primitive={'b':2,'a_cubed':pair(A),'c_eleventh':pair(C),'a_start':ra,'c_start':rc,
    'a_polynomial_value':pair(av),'c_polynomial_value':pair(cv),
    'a_value_valuation':vf(av),'c_value_valuation':vf(cv),
    'a_derivative_residue':int(ad)%P,'c_derivative_residue':int(cd)%P}
check('full_saved_primitive_witness',primitive==OLD['primitive_power_witness'])
check('a_strict_hensel',vf(av)>2*vf(ad))
check('c_strict_hensel',vf(cv)>2*vf(cd))
check('all_power_coordinates_units',vf(A)==vf(C)==val(2)==0)
check('one_shared_power_sum',A+2**4==C)
check('one_shared_scalar',1728*A/C==3)
s0=Fraction(9261,8)
t=s0/1728
q=1-t
check('canonical_obstruction_valuations',vf(t)==0 and vf(q)==2)
evidence['primitive_witness']=primitive
evidence['hensel_bounds']={'a_actual':vf(av),'a_required_strictly_greater_than':2*vf(ad),
    'c_actual':vf(cv),'c_required_strictly_greater_than':2*vf(cd)}
evidence['canonical_ratios']={'t':pair(t),'q':pair(q),'t_valuation':vf(t),'q_valuation':vf(q)}
evidence['whole_field_degrees']={'K_actual':max(mbar),'B3_actual':max(M),'required':12}
# The extra source-program good-reduction flag is not used in the proof.
result={'checks':checks,'failures':[n for n,v in checks.items() if not v],
        'evidence':evidence,'scope':'Only the existing L064 canonical and scalar-three witnesses; no scalar search.'}
out=HERE/'audit-certificate.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print('Independent checks:',sum(checks.values()),'/',len(checks))
print('Whole-field degrees actual:',max(mbar),max(M),'required: 12 each')
print('Hensel bounds actual:',vf(av),vf(cv),'required >',2*vf(ad),2*vf(cd))
print('Failures:',result['failures'])
print('Certificate:',out.relative_to(HERE.parents[1]))
if result['failures']: raise SystemExit(1)
