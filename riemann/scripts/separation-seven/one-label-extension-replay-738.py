#!/usr/bin/env python3
"""Independent exact replay of all94 original-residual obstructions.

Rebuild cardinal polynomials by synthetic division of the full35-root
integer polynomial. Integrate by direct original-atom Horner sums,
not the constructor's weighted power sums or any Decimal enclosure.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from math import lcm
import json
import sys

sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve()
INPUT=HERE.with_name('one-label-extension-738.json')
OUT=HERE.with_suffix('.json')
d=json.loads(INPUT.read_text())
J,N=2048,35
labels=d['parameters']['labels']
indices=[J+i*(J-1)//128 for i in labels]
nodes=[F(4*j+1,2*J)-3 for j in indices]

def cheb(t):
    r=[F(1),t]
    for _ in range(2,N):
        r.append(2*t*r[-1]-r[-2])
    return r

def evaluate(poly,x):
    z=0
    for c in reversed(poly):
        z=z*x+c
    return z

P=[1]
for root in indices:
    r=[0]*(len(P)+1)
    for a,c in enumerate(P):
        r[a]-=root*c
        r[a+1]+=c
    P=r
L=lcm(*((4*j+1)**2 for j in range(J,2*J)))
integer_masses=[16*J*(L//((4*j+1)**2)) for j in range(J,2*J)]
mass=F(sum(integer_masses),L)
checks={
    'constructor_source_bound':d['script_sha256']==sha256(INPUT.with_suffix('.py').read_bytes()).hexdigest(),
    '94_distinct_unused_labels_in_order':[z['label'] for z in d['residual_duals']]==[i for i in range(129) if i not in labels],
    '35_distinct_original_base_nodes':len(indices)==N and len(set(indices))==N and all(J<=i<2*J for i in indices),
    'exact_original_mass_below_one':0<mass<1 and mass==F(d['exact_original_measure']['mass_exact']),
    'all35_integer_cardinal_polynomials':True,
    'all35_chebyshev_cardinal_polynomials':True,
    'all35_direct_original_integrals':True,
    'all94_positive_cardinal_combinations':True,
    'all94_coefficients_match':True,
    'all3384_exact_support_values_nonnegative':True,
    'all94_exact_negative_integrals':True,
    'all94_norm_upper_bounds':True,
    'all94_residual_lower_bounds':True,
    'all94_residuals_exceed_1_over10000':True,
}
cardinal_data=[]
ccs=[]
Is=[]
for i,root in enumerate(indices):
    # Descending synthetic division, then restore ascending coefficient order.
    desc=list(reversed(P))
    quotient=[desc[0]]
    for c in desc[1:-1]:
        quotient.append(c+root*quotient[-1])
    assert desc[-1]+root*quotient[-1]==0
    poly=list(reversed(quotient))
    denominator=evaluate(poly,root)
    saved=d['exact_cardinal_polynomials'][i]
    checks['all35_integer_cardinal_polynomials'] &= (poly==list(map(int,saved['integer_coefficients_ascending'])) and denominator==int(saved['integer_denominator']) and denominator!=0)
    cc=list(map(F,saved['chebyshev_coefficients']))
    checks['all35_chebyshev_cardinal_polynomials'] &= (len(cc)==N and
        all(sum((a*b for a,b in zip(cc,cheb(t))),F(0))==int(h==i) for h,t in enumerate(nodes)))
    numerator=0
    digest=sha256()
    for j,m in zip(range(J,2*J),integer_masses):
        value=evaluate(poly,j)
        numerator+=m*value
        digest.update((str(value)+'\n').encode())
    integral=F(numerator,L*denominator)
    checks['all35_direct_original_integrals'] &= integral==F(saved['integral_exact'])
    ccs.append(cc)
    Is.append(integral)
    cardinal_data.append({'coordinate':i,'original_integral_exact':str(integral),
        'all2048_integer_cardinal_numerators_sha256':digest.hexdigest()})

dual_data=[]
for z in d['residual_duals']:
    label=z['label']
    coeff={int(i):F(c) for i,c in z['positive_cardinal_combination'].items()}
    checks['all94_positive_cardinal_combinations'] &= all(0<=i<N and c>0 for i,c in coeff.items())
    pc=[sum((c*ccs[i][a] for i,c in coeff.items()),F(0)) for a in range(N)]
    checks['all94_coefficients_match'] &= pc==list(map(F,z['chebyshev_coefficients']))
    newnode=F(4*(J+label*(J-1)//128)+1,2*J)-3
    values=[sum((a*b for a,b in zip(pc,cheb(t))),F(0)) for t in nodes+[newnode]]
    checks['all3384_exact_support_values_nonnegative'] &= values==list(map(F,z['all36_support_values_exact'])) and min(values)>=0
    I=sum((c*Is[i] for i,c in coeff.items()),F(0))
    norm=sum(map(abs,pc),F(0))
    bound=-I/norm
    checks['all94_exact_negative_integrals'] &= I<0 and I==F(z['original_integral_exact'])
    checks['all94_norm_upper_bounds'] &= norm>0 and norm==F(z['original_L2_norm_strict_upper'])
    checks['all94_residual_lower_bounds'] &= bound==F(z['residual_strict_lower'])
    checks['all94_residuals_exceed_1_over10000'] &= bound>F(1,10000)>F(5,10**19)
    dual_data.append({'label':label,'integral_negative':I<0,
        'all36_support_values_nonnegative':min(values)>=0,
        'strict_residual_lower_exceeds_1_over10000':bound>F(1,10000)})

report={'script_sha256':sha256(HERE.read_bytes()).hexdigest(),
    'input_sha256':sha256(INPUT.read_bytes()).hexdigest(),
    'full35_root_integer_polynomial_ascending':list(map(str,P)),
    'direct_original_cardinal_integrals':cardinal_data,'dual_checks':dual_data,
    'rigorous_common_bound':{'all94_residual_strict_lower':'1/10000',
        'required_residual_upper':'5/10000000000000000000',
        'original_atoms_per_integral':2048,'exact_integrals':35,
        'support_values_checked':94*36,'precision_assumption':'none; exact integer/Fraction semantics'},
    'checks':checks,'failed_checks':[k for k,v in checks.items() if not v],
    'complete_work_upper':None,'peak_bytes_upper':None}
OUT.write_text(json.dumps(report,indent=2)+'\n')
print('Direct original integrals:',35,'x2048 atoms; dual support values:',94*36)
print('All94 supports: epsilon>1/10000; required<=5e-19')
print('Checks:',sum(checks.values()),'/',len(checks),'; failures:',report['failed_checks'])
print('Certificate:',OUT.relative_to(HERE.parents[2]),'; observed bytes:',OUT.stat().st_size)
if report['failed_checks']:
    raise SystemExit(1)
