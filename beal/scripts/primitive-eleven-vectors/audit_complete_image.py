"""Independent arithmetic audit of L041--L044; no original code imports.

Horner composition over Fraction recomputes every shifted/scaled coefficient.
The source map is the previously audited L034 coefficient transcription.
Complete evidence is written to disk; lifting/completeness remains a proof.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent


def read(name):
    return json.loads((BASE / name).read_text())


def clean(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def plus(a, b):
    c = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a): c[i] += x
    for i, x in enumerate(b): c[i] += x
    return clean(c)


def times(a, b):
    c = [Q(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += x*y
    return clean(c)


def scale(a, c): return clean([x*c for x in a])


def compose(a, b):
    r = [Q(0)]
    for c in a[::-1]: r = plus(times(r, b), [Q(c)])
    return r


def power(a, n):
    r = [Q(1)]
    for _ in range(n): r = times(r, a)
    return r


def pad(a, n=13): return a + [Q(0)]*(n-len(a))
def value(a, x): return compose(a, [Q(x)])[0]
def deriv(a): return [i*a[i] for i in range(1, len(a))]


def integral(a):
    assert all(Q(x).denominator == 1 for x in a)
    return [int(x) for x in a]


def residue(a): return clean([x % 11 for x in integral(a)])


def val(x):
    if not x: return None
    x = Q(x)
    n, d, v = abs(x.numerator), x.denominator, 0
    while n % 11 == 0: n //= 11; v += 1
    while d % 11 == 0: d //= 11; v -= 1
    return v


def main():
    p = read('../five-isogeny-modular-norm/norm-certificate.json')['polynomials_ascending']
    old = {n: read(n+'-certificate.json') for n in
           ['vector-prerequisites', 'generic-fiber', 'negative-scalar', 'integral-branch']}
    checks, data = {}, {}
    def check(name, test): checks[name] = bool(test)
    h3 = power(p['h'], 3)
    J, d, a, b = (list(map(Q, p[n])) for n in ['jcoef','d','a','b'])
    check('source_J', plus(scale(a, 2), scale(b, -1)) == J)
    check('source_elimination', plus(plus(times(a,a),scale(times(a,b),-1)),
          scale(times(times(b,b),p['g']),-1)) == scale(times(d,h3),-1))
    shifted = {n: pad(compose(poly, [Q(16),Q(1)])) for n,poly in [('h3',h3),('J',J),('d',d)]}
    generic = old['generic-fiber']
    check('all_shifted_coefficients', shifted == generic['shifted_components_ascending'] == old['negative-scalar']['shifted_components_ascending'])
    R = {n: pad(scale(compose(poly, [Q(16),Q(121)]), Q(1,11**22)))
         for n,poly in [('h3',h3),('J',J),('d',d)]}
    D = {n: scale(deriv(poly), Q(1,11)) for n,poly in R.items()}
    B = scale(compose(b,[Q(16),Q(121)]),Q(1,11**20))
    N = scale(compose(plus(a,scale(b,60)),[Q(16),Q(121)]),Q(1,11**22))
    check('all_scaled_coefficients', R == generic['scaled_components_ascending'])
    check('all_derivative_coefficients', all(pad(D[n],12)==generic['derivative_over_11_components_ascending'][n] for n in D))
    check('reconstruction_coefficients', B==generic['scaled_b_ascending'] and N==generic['scaled_numerator0_ascending'])
    check('generic_reductions', {n:residue(v) for n,v in R.items()} == {'h3':[0], 'J':[1]+[0]*10+[1], 'd':[0]*11+[1]})
    check('b_reduction', residue(B)==residue(power([1,1],10)))
    check('uniform_generic_bounds', all(c==0 or val(c)>=23-2*i for poly in shifted.values() for i,c in enumerate(poly) if 1<=i<=10))
    check('generic_endpoints', shifted['h3'][0]==11**24 and shifted['J'][0]==11**22 and shifted['d']==[0]*11+[1,0])
    cases = []
    for s in range(2,11):
        z=pow(s-1,-1,11)
        derivative=int(value(D['h3'],z)+s*value(D['J'],z)-s*s*value(D['d'],z))%11
        C=derivative*pow(s*(1-s),-1,11)%11
        br,nr=int(value(B,z))%11,int(value(N,z))%11
        v=(s*pow(z,11,11)-nr)*pow(br,-1,11)%11
        row=[s,z,derivative,s*(1-s)%11,C,br,nr,v,(1-38*z+12*v)%11]
        cases.append(row)
    expected=[[c[k] for k in ['s','z','Rprime_over_11','cluster_leading_unit','C','b_over_11pow20','numerator0_over_11pow22','v','f_over_121']] for c in generic['all_generic_residue_cases']]
    check('all_generic_cases', cases==expected)
    check('generic_field_and_f', [r[0] for r in cases if r[4]==5]==[4,10] and all(r[2] and r[5]==1 and r[7]==6*r[1]%11 and r[8]==(1+r[1])%11!=0 for r in cases))
    data['generic']={'columns':['s','z','Rprime/11','lambda','C','B','N','V','f/121'], 'rows':cases, 'shifted_valuations':{n:list(map(val,v)) for n,v in shifted.items()}, 'derivative_reductions':{n:residue(v) for n,v in D.items()}, 'B_reduction':residue(B),'N_reduction':residue(N)}

    # Exact curve and f identities under the simultaneous cluster coordinates.
    curve_scaled=scale(plus(compose(p['g'],[Q(16),Q(121)]),[-3660]),Q(1,121**2))
    check('curve_identity', curve_scaled==[0,6,47,121])
    f_constant=plus(plus(scale([12,121],60), scale(power([16,121],2),-4)),plus(scale([16,121],30),[-55]))
    check('f_identity', scale(f_constant,Q(1,121))==[1,-38,-484])
    xv=500
    av,bv,dv=(value(poly,xv) for poly in [a,b,d])
    point={'curve_rhs':int(value(curve_scaled,4)), 'root_residue':2,
           'equation_residue':int(6-value(curve_scaled,4))%11,'derivative_residue':5,
           'valuations':[val(bv),val(av+60*bv),val(dv)],
           'normalized_residues':[int((av+60*bv)/11**22)%11,int(121*bv/11**22)%11,int(dv/11**22)%11],
           's_residue':int((av+302*bv)/11**22)*pow(int(dv/11**22),-1,11)%11,
           'f_residue':int(value(scale(f_constant,Q(1,121)),4)+value([12,121],4)*2)%11}
    check('exact_realization_data', point=={'curve_rhs':8520,'root_residue':2,'equation_residue':0,'derivative_residue':5,'valuations':[20,22,22],'normalized_residues':[3,1,4],'s_residue':4,'f_residue':5})
    data['realization']=point

    branch=old['integral-branch']
    zero={'base':pad(scale(compose(h3,[-105,121]),Q(1,11**24))),
          'linear':pad(scale(compose(J,[-105,121]),Q(1,11**22))),
          'quadratic':pad(scale(compose(d,[-105,121]),Q(1,11**22)))}
    one={'base':pad(compose(plus(plus(h3,scale(J,1728)),scale(d,-1728**2)),[16,1])),
         'linear':pad(compose(plus(J,scale(d,-3456)),[16,1])), 'quadratic':shifted['d']}
    for name,comp,height,offset in [('zero_disk',zero,3,[0,1,4]),('one_disk',one,22,[0,4,8])]:
        check(name+'_all_coefficients', comp==branch[name]['components_ascending'])
        rows=[]
        for i in range(13):
            vs=[val(comp[n][i]) for n in ['base','linear','quadratic']]
            bound=Q(height*(12-i),12)
            actual=[None if v is None else v+o for v,o in zip(vs,offset)]
            rows.append({'i':i,'valuations':vs,'actual_lower_bounds':actual,'required':str(bound)})
        check(name+'_uniform_bounds', all((r['actual_lower_bounds'][0] is None or r['actual_lower_bounds'][0]>=Q(r['required'])) and all(v is None or v>Q(r['required']) for v in r['actual_lower_bounds'][1:]) for r in rows))
        check(name+'_endpoints', val(comp['base'][0])==height and comp['base'][12]==1 and not comp['linear'][12] and not comp['quadratic'][12])
        check(name+'_original_bounds', all(r['valuations']==[o['valuations'][n] for n in ['base','linear','quadratic']] and r['required']==o['required_bound'] for r,o in zip(rows,branch[name]['full_bounds'])))
        data[name]={'rows':rows,'constant_residue':int(comp['base'][0]/11**height)%11,'forced_valuation':str(Q(height,12))}

    negative=old['negative-scalar']
    negrows=[]
    for n in ['h3','J']:
        for i,c in enumerate(shifted[n]):
            if not c: continue
            slope=i+(11 if n=='h3' else 0)
            intercept=val(c)+2*i-22
            minimum=slope+intercept
            derivative_min=None if i==0 else minimum+val(i)-1
            negrows.append([n,i,slope,intercept,minimum,derivative_min])
    check('negative_all_affine_rows', [r[:5] for r in negrows]==[[r['component'],r['i'],r['k_slope'],r['intercept'],r['minimum_k_ge_1']] for r in negative['R_affine_valuation_bounds']])
    check('negative_uniform_derivative', all(r[2]>=0 and (r[4]>=2 if r[:2]!=['J',0] else r[4]==0) and (r[5] is None or r[5]>=1) for r in negrows))
    check('negative_original_derivative', [r[5] for r in negrows if r[1]]==[r['minimum_Rprime_over_11_coefficient_valuation'] for r in negative['Rprime_over_11_bounds']])
    infinity=[]
    for n,poly,offset in [('h3',h3,24),('J',J,23),('d',d,22)]:
        for i,c in enumerate(poly):
            if c: infinity.append([n,i,int(c),offset-2*i])
    check('infinity_all_coefficients', infinity==[[r['component'],r['i'],r['coefficient'],r['s_inverse_exponent']] for r in negative['infinity_scaling_terms']])
    check('infinity_uniform', all(r[3]>=0 for r in infinity) and [r[:3] for r in infinity if r[3]==0]==[['h3',12,1],['d',11,1]])
    negcases=[[s,pow(s,-1,11),pow(pow(s,-1,11),10,11)] for s in range(1,11)]
    check('negative_all_unit_cases', negcases==[[r['sigma'],r['z0'],r['C']] for r in negative['all_unit_residue_cases']] and all(r[2]==1!=5 for r in negcases))
    data['negative']={'affine_columns':['component','i','slope','intercept','minimum_k=1','derivative_minimum'],'affine_rows':negrows,'infinity_columns':['component','i','inverse_s_exponent'],'infinity_rows':[[r[0],r[1],r[3]] for r in infinity],'unit_rows':negcases,'required_C':5}

    pre=old['vector-prerequisites']
    m=pre['inputs']['field_polynomial_ascending']
    blocks=[power([1,1],10),[3,1],[9,1]]
    check('field_reduction', residue(m)==residue(times(times(*blocks[:2]),blocks[2])))
    check('field_shift', compose(m,[-1,1])==pre['shifted_polynomial_ascending'])
    check('field_bezout', all(residue(plus(times(r['u'],blocks[r['pair'][0]]),times(r['v'],blocks[r['pair'][1]])))==[1] for r in pre['pairwise_bezout']))
    roots=[[x,int(value(m,x))%11,int(value(deriv(m),x))%11] for x in [8,2]]
    check('field_simple_roots', roots==[[8,0,6],[2,0,5]])
    shifted_m=compose(m,[-1,1]); C=int(shifted_m[0]/11)*pow(16,-1,11)%11
    check('field_eisenstein', val(shifted_m[0])==1 and C==5)
    check('scalar_all_unit_lifts', all(pow(pow(t,7,11),3,11)==t and t*pow(pow(t,-1,11),11,11)%11==1 for t in range(1,11)))
    data['field']={'shifted_coefficients':integral(shifted_m),'simple_roots':roots,'C':C,'dimensions':[1,1,10],'e':[1,1,10],'f':[1,1,1]}
    exceptions={str(y):int((value(a,5)+y*value(b,5))/value(d,5)) for y in [5,-6]}
    removable=-value(p['h'],16)**3/(value(a,16)+60*value(b,16))
    check('exceptional_values', exceptions=={'5':-24729001,'-6':-32768} and removable==-121)
    check('exceptional_primitive_failure', [val(-24729001),val(removable),val(-32768-1728)]==[1,2,1])
    data['exceptions']={'T':exceptions['5'],'twoT':int(removable),'fourT':exceptions['-6'],'excluded_valuations':[1,2,1],'O_threeT':'infinity'}
    data['exact_recomputed_coefficients']={'shifted':shifted,'R':R,'D':D,'B':B,'N':N,'zero':zero,'one':one}
    data['checks']=checks
    data['failures']=[n for n,ok in checks.items() if not ok]
    data['threshold']={'actual_root_valuations':['1/4','11/6'],'required_for_rational_root':'integer','negative_C':1,'required_C':5,'realized_vectors':[[0,2,0],[2,0,0]],'global_emptiness':'not established'}
    def encode(x):
        if isinstance(x,Q): return int(x) if x.denominator==1 else str(x)
        raise TypeError(type(x))
    path=BASE/'complete-image-audit-certificate.json'
    path.write_text(json.dumps(data,indent=2,default=encode)+'\n')
    print(f'Checks {sum(checks.values())}/{len(checks)}; failures={data["failures"]}')
    print('Branch root valuations actual=1/4,11/6; rational roots require integers.')
    print('Negative field residue actual=1; required=5. Realization s mod11=4; derivative=5 (required nonzero).')
    print('Certificate: '+str(path.relative_to(BASE.parent.parent)))
    if data['failures']: raise SystemExit(1)


if __name__=='__main__': main()
