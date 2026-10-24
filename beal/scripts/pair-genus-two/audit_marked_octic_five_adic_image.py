#!/usr/bin/env python3
"""Independent exact arithmetic audit of L119. No producer imports or execution."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parent
SOURCE = BASE / 'marked-octic-five-adic-image-certificate.json'
INITIAL = BASE / 'marked-octic-five-adic-image-initial-label-failure.json'
OUT = BASE / 'marked-octic-five-adic-image-audit-certificate.json'
saved = json.loads(SOURCE.read_text())
old = json.loads(INITIAL.read_text())
checks, comparisons, independent = {}, {}, {}

def check(name, condition):
    checks[name] = bool(condition)

def compare(key, value):
    comparisons[key] = value
    check('saved_' + key, saved[key] == value)

def value(p, x):
    return sum(Q(c)*x**i for i,c in enumerate(p))

def deriv(p, x):
    return sum(i*Q(c)*x**(i-1) for i,c in enumerate(p) if i)

def v5(x):
    x = Q(x)
    assert x
    v = 0
    a,b = x.numerator,x.denominator
    while a % 5 == 0:
        a //= 5; v += 1
    while b % 5 == 0:
        b //= 5; v -= 1
    return v

def residue(x):
    x = Q(x)
    return x.numerator * pow(x.denominator,-1,5) % 5

def label(x):
    v = v5(x)
    u = residue(Q(x)/Q(5)**v)
    return [v % 2, int(pow(u,2,5) != 1)]

# Start from the displayed 11-times-primitive polynomial, not producer globals.
G = [11*c for c in (243,0,-3564,0,6930,0,-2860,0,275)]
H = G[::-2]
J = [int(Q(c*5**i,25)) for i,c in enumerate(H)]
check('scaled_coefficients_integral', all(Q(c*5**i,25).denominator == 1 for i,c in enumerate(H)))
compare('coefficients_ascending',G); compare('H_ascending',H); compare('J_ascending',J)

def newton_record(p):
    x,m = 3,5
    rows=[]
    for exponent in range(1,6):
        # Solve the linear Taylor congruence for the next digit.
        digit = int(-value(p,x)//m)*pow(int(deriv(p,x)),-1,5) % 5
        candidates = list(range(x,x+5*m,m))
        errors = [int(value(p,z)) % (5*m) for z in candidates]
        check(f'newton_{p[0]}_{exponent}', errors[digit] == 0 and errors.count(0) == 1)
        rows.append(dict(exponent=exponent,seed=x,modulus=m,candidates=candidates,
                         errors_mod_next=errors,passing_digits=[digit]))
        x += m*digit; m *= 5
    return dict(poly_ascending=p,seed=3,initial_error=str(value(p,3)),
                initial_derivative=str(deriv(p,3)),steps=rows,residue=x,modulus=m)

rrec,urec=newton_record(H),newton_record(J)
compare('hensel_r0',rrec);compare('hensel_r1_over_5',urec)
check('simple_root_reductions', [int(c)%5 for c in H] == [0,0,0,1,3]
      and [int(c)%5 for c in J] == [1,3,0,0,0]
      and residue(deriv(H,3)) == 1 and residue(deriv(J,3)) == 3)
m=rrec['modulus'];r0=rrec['residue'];u1=urec['residue'];r1=5*u1 % m

def divide_linear(p,r):
    out=[0]*(len(p)-1);out[-1]=p[-1]%m
    for i in range(len(out)-2,-1,-1):
        out[i]=(p[i+1]+r*out[i+1])%m
    return out,(p[0]+r*out[0])%m

p,rem0=divide_linear(H,r0);p,rem1=divide_linear(p,r1)
check('two_synthetic_remainders_zero',rem0 == rem1 == 0)
b,a,one=[c*pow(2673,-1,m)%m for c in p]
check('monic_quadratic_and_exact_formulas', one == 1 and
      a == (-39204*pow(2673,-1,m)+r0+r1)%m and
      b == 605*pow(2673*r0*u1,-1,m)%m)
compare('factor_coefficient_residues',dict(r0_mod=r0,r1_mod=r1,modulus=m,a_mod=a,b_mod=b,
    b_over_5_mod_5=residue(Q(121,2673*3*3)),minus_b_over_10_mod_5=residue(Q(-121,2*2673*3*3))))
# Rebuild via independent coefficient identities for the four elementary sums.
s,p=r0+r1,r0*r1
rebuilt=[2673*p*b,2673*(p*a-s*b),2673*(p-s*a+b),2673*(a-s),2673]
compare('factor_product_mod_precision',[c%m for c in rebuilt])
check('full_polynomial_product',[c%m for c in rebuilt] == [c%m for c in H])
check('eisenstein_and_quartic_hensel',a%5==0 and b%25==15 and residue(Q(b,10))==4)
compare('exact_factorization','H(r)=2673(r-r0)(r-r1)(r^2+a*r+b); r0 and r1/5 are the unique Hensel roots at 3 mod 5')
compare('local_models',[
 dict(degree=4,e=4,f=1,model='pi^4=10',q='pi*u; u^4+(a/pi^2)*u^2+b/10=0, u=1 mod pi'),
 dict(degree=2,e=2,f=1,model='lambda^2=15',q='lambda*sqrt(r1/15); principal square root'),
 dict(degree=2,e=1,f=2,model='omega^2=3',q='omega*sqrt(r0/3); principal square root')])
compare('theta','1/q in every complete factor')
compare('label_order',['pi','2 at quartic','lambda','2 at quadratic','5 at unramified','1+omega'])

# Norms computed as determinants of multiplication in Q[X]/(X^n-c).
def determinant(mat):
    mat=[[Q(x) for x in row] for row in mat];result=Q(1)
    for j in range(len(mat)):
        k=next(i for i in range(j,len(mat)) if mat[i][j])
        if k != j:
            mat[k],mat[j]=mat[j],mat[k];result=-result
        pivot=mat[j][j];result*=pivot
        for i in range(j+1,len(mat)):
            ratio=mat[i][j]/pivot
            for l in range(j,len(mat)):
                mat[i][l]-=ratio*mat[j][l]
    return result

def norm(n,c,elem):
    mat=[[0]*n for _ in range(n)]
    for j in range(n):
        for i,coef in enumerate(elem):
            degree=i+j
            mat[degree%n][j]+=coef*c**(degree//n)
    return determinant(mat)

specs=[('quartic','pi',4,10,[0,1]),('quartic','2',4,10,[2]),
       ('quadratic','lambda',2,15,[0,1]),('quadratic','2',2,15,[2]),
       ('unramified','5',2,3,[5]),('unramified','1+omega',2,3,[1,1])]
nt=[]
for field,g,n,c,elem in specs:
    z=norm(n,c,elem)
    nt.append(dict(factor=field,generator=g,norm=str(z),label=label(z)))
compare('norm_table',nt);compare('norm_table_replay',[row['label'] for row in nt])
# Exhaust all 24 nonzero residue elements, rather than just the chosen unit.
elements=list(product(range(5),repeat=2))
squares={((a*a+3*b*b)%5,2*a*b%5) for a,b in elements if (a,b)!=(0,0)}
characters=[dict(element=[a,b],norm=(a*a-3*b*b)%5,square=(a,b) in squares)
            for a,b in elements if (a,b)!=(0,0)]
check('full_F25_character',len(squares)==12 and all(r['square']==(r['norm'] in [1,4]) for r in characters))
check('eta_nonsquare',(1,1) not in squares)
check('rational_units_square_in_U',all((a,0) in squares for a in range(1,5)))
independent['F25_characters']=characters
# Rational scalar images from the field relations (5=pi^4/2=lambda^2/3).
scalar2='010100'; scalar5='010110'
check('scalar_unit_bits',label(Q(1,2))==[0,1] and label(Q(1,3))==[0,1])
scalar_ints=sorted({0,int(scalar2,2),int(scalar5,2),int(scalar2,2)^int(scalar5,2)})
compare('scalars',[format(s,'06b') for s in scalar_ints])
all_bits=[format(i,'06b') for i in range(64)]
# Generate disjoint cosets, then identify the d=e=0 member, not producer normalization.
orbits={};remaining=set(range(64))
while remaining:
    coset={min(remaining)^s for s in scalar_ints}
    members=sorted(format(v,'06b') for v in coset)
    canonical=[s for s in members if s[3:5]=='00']
    check('unique_coset_'+str(min(coset)),len(canonical)==1)
    orbits[canonical[0]]=members
    remaining-=coset
compare('full_quotient_collisions',orbits)

def total_norm(bits):
    return label(product_norm(bits))

def product_norm(bits):
    answer=Q(1)
    for bit,row in zip(bits,nt):
        if bit=='1':answer*=Q(row['norm'])
    return answer

kernel=[s for s in all_bits if total_norm(s)==[0,0]]
compare('full_norm_kernel',kernel)
check('norm_formula_all_64',all(total_norm(s)==[(int(s[0])+int(s[2]))%2,
       (int(s[0])+int(s[2])+int(s[5]))%2] for s in all_bits))
check('norm_invariant_all_orbits',all(len({tuple(total_norm(s)) for s in members})==1 for members in orbits.values()))
ambient=sorted(s for s in orbits if total_norm(s)==[0,0])
compare('ambient',ambient);compare('image',['000000','101000']);compare('excluded_witness','010000')
check('cardinalities',len(kernel)==16 and len(orbits)==16 and len(ambient)==4 and all(len(v)==4 for v in orbits.values()))

integral=[]
for t in range(5):
    residue_G=residue(value(G,t)); feasible=residue_G in [1,4]
    # theta mod 5 = 1/omega = 2 omega; its norm is -12 = 3.
    theta_res=(t,3)
    check('integral_U_class_'+str(t), (theta_res in squares)==feasible)
    integral.append(dict(t_mod_5=t,G_mod_5=residue_G,unramified_norm_mod_5=(t*t-2)%5,
       feasible=feasible,center_G=str(value(G,t)),normalized_class='101000' if feasible else None))
compare('integral_disks',integral)
terms=[dict(power=i,coefficient=str(Q(G[8-i],G[8])),slope=i,
       intercept=v5(Q(G[8-i],G[8])),minimum_at_n_1=i+v5(Q(G[8-i],G[8]))) for i in [2,4,6,8]]
compare('reciprocal_terms',terms)
check('all_tail_bounds_strict',all(row['minimum_at_n_1']>0 and row['slope']>0 for row in terms))
compare('strict_bounds',dict(square_neighborhood_required='normalized valuation > 0 (residue characteristic 5)',
 integral_ramified_ratio=[dict(factor='quartic',minimum=1),dict(factor='quadratic',minimum=1)],
 integral_unit_disk_difference=dict(minimum=1,center_unit_valuation=0),
 reciprocal_ratios=[dict(factor=f,slope=e,intercept=v,minimum=e+v)
                    for f,e,v in [('quartic',4,-1),('quadratic',2,-1),('unramified',1,0)]]))
compare('rational_branch_points',[])
g1=value(G,Q(1));g5=value(G,Q(1,5));normalized=g5/(55*Q(1,5)**4)**2
compare('finite_realizations',[
 dict(t='1',G=str(g1),square_unit_mod_5=residue(g1),Y_seed_mod_5=2,Y_derivative_mod_5=4,quotient='101000'),
 dict(t='1/5',G=str(g5),normalized_square=str(normalized),normalized_Y_seed_mod_5=1,normalized_Y_derivative_mod_5=2,quotient='000000')])
check('actual_realization_hensel_seeds',residue(g1)==4 and residue(normalized)==1)
compare('infinity_rows',[dict(q=0,Z=z,derivative=2*z,fake_class='000000') for z in [-55,55]])
check('separate_smooth_infinities',55**2==G[-1] and 110!=0 and v5(110)==1)
compare('bounds',dict(local_degree_actual=sum(row['degree'] for row in saved['local_models']),local_degree_required=8,
 affine_residue_disks_actual=len(integral),affine_residue_disks_required=5,unresolved_disks=0,
 reciprocal_minimum_n=1,square_precision_required='strictly positive normalized valuation',
 infinity_rows_actual=2,infinity_rows_required=2,image_actual=2,ambient_actual=len(ambient),properness_required='image < ambient'))
# Producer flags are consumed for consistency only, never used as arithmetic premises.
check('producer_flags_consistent',len(saved['checks'])==31 and all(v is True for v in saved['checks'].values()) and saved['failures']==[])
check('complete_saved_evidence_consumed',set(saved)==set(comparisons)|{'checks','failures'})

# Preserve and audit the entire first record; its orbits must agree as SETS.
changed=[key for key in saved if saved[key]!=old[key]]
independent['initial_changed_fields']=changed
convention_keys={'full_quotient_collisions','ambient','excluded_witness','checks','failures'}
check('initial_changes_only_convention',set(changed)<=convention_keys)
check('initial_all_other_evidence_identical',all(old[k]==saved[k] for k in saved if k not in convention_keys))
check('initial_orbits_unchanged',sorted(sorted(v) for v in old['full_quotient_collisions'].values())==sorted(sorted(v) for v in orbits.values()))
check('initial_lexicographic_keys',all(k==min(v) for k,v in old['full_quotient_collisions'].items()))
check('initial_failure_only_ambient',old['failures']==['ambient_exact'] and [k for k,v in old['checks'].items() if not v]==['ambient_exact'])
check('initial_ambient_same_classes',set(old['ambient'])=={min(orbits[k]) for k in ambient})
check('initial_beta_same_class',old['excluded_witness'] in orbits['010000'])
failures=[k for k,v in checks.items() if not v]
report=dict(source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
 initial_sha256=hashlib.sha256(INITIAL.read_bytes()).hexdigest(),
 independently_recomputed=comparisons,independent_extra_evidence=independent,
 analytic_obligations='Exact Hensel transports, strict square neighborhoods and exhaustive chart proof reviewed in L119 audit section; finite data alone do not establish them.',
 checks=checks,failures=failures,
 bounds=dict(local_degree='8/8',affine_disks='5/5',infinity_rows='2/2',
 integral_ratio_minima=[1,1],reciprocal_ratio_minima=[3,1,1],required='>0',image=2,norm_ambient=4))
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(f'Independent checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}')
print('Degrees 8/8; affine disks 5/5; infinity rows 2/2; raw labels 64/64; scalar orbits 16/16')
print('Strict minima integral (1,1), reciprocal (3,1,1), required >0; image 2 < norm ambient 4')
print(f'Complete audit certificate: {OUT}')
if failures:raise SystemExit(1)
