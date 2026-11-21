#!/usr/bin/env python3
"""Independent C029q fixed N=6,7 audit; standard library only.

Sparse Q[X,s]/(s^2-2); verifies stored kernels by basis expansion,
not the original telescoping/basis inversion implementation.
Full rational evidence is saved; console output is bounded.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import sys

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent
OUT = ROOT / 'tilted-affine-residual-audit-2024.json'
checks = {}
evidence = {'status': 'STARTED', 'checks': checks}


def check(name, value):
    checks[name] = bool(value)


def save(stage):
    evidence['status'] = stage
    evidence['failures'] = [k for k,v in checks.items() if not v]
    OUT.write_text(json.dumps(evidence, indent=2)+'\n')
    if evidence['failures']:
        print(json.dumps({'status': stage, 'failures': evidence['failures'],
                          'certificate': str(OUT)}))
        raise SystemExit(1)


def add(*args):
    r = {}
    for a in args:
        for k,v in a.items():
            r[k] = r.get(k,F(0))+v
    return {k:v for k,v in r.items() if v}


def scale(a,c):
    return {k:v*c for k,v in a.items() if v*c}


def mul(a,b):
    r = {}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            key = i+k,(j+l)%2
            r[key] = r.get(key,F(0))+v*w*2**((j+l)//2)
    return {k:v for k,v in r.items() if v}


def dec(p):
    return {(i,j):F(c[key]) for i,c in enumerate(p)
            for j,key in enumerate(('rational','sqrt2')) if F(c[key])}


def matrix(a):
    return [[dec(p) for p in row] for row in a]


def tr(a):
    return list(map(list,zip(*a)))


def mm(a,b):
    return [[add(*(mul(a[i][k],b[k][j]) for k in range(len(b))))
             for j in range(len(b[0]))] for i in range(len(a))]


def iv(a):
    return F(a['lower']),F(a['upper'])


def ij(a):
    return {'lower':str(a[0]),'upper':str(a[1])}


def ia(*args):
    return sum((a[0] for a in args),F(0)),sum((a[1] for a in args),F(0))


def im(a,b):
    z = [v*w for v in a for w in b]
    return min(z),max(z)


def isc(a,c):
    return min(c*a[0],c*a[1]),max(c*a[0],c*a[1])


def inv(a):
    assert a[1]<0 or a[0]>0, 'zero in denominator'
    return 1/a[1],1/a[0]


def enclose(p,x,s):
    r = F(0),F(0)
    for i in range(max((k[0] for k in p),default=0),-1,-1):
        a,b = p.get((i,0),F(0)),p.get((i,1),F(0))
        r = ia(im(r,x),ia((a,a),isc(s,b)))
    return r


def outer(a):
    return isc(iv(a['scaled_interval']),F(10)**a['power_of_ten'])


def contains(a,b):
    return a[0]<=b[0]<=b[1]<=a[1]


def main():
    names = ('tilted-boundary-metric-2010.json',
             'tilted-bezoutian-n6-2014.json',
             'tilted-affine-quotient-residual-2022.json')
    raw = {name:(ROOT/name).read_bytes() for name in names}
    source,prior,cert = [json.loads(raw[name]) for name in names]
    evidence['input_sha256'] = {k:hashlib.sha256(v).hexdigest() for k,v in raw.items()}
    evidence['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    for name,wanted in cert['input_sha256'].items():
        check('pin_'+name, hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==wanted)
    check('original_check_record',len(cert['checks'])==99 and all(cert['checks'].values())
          and cert['failures']==[] and cert['incomplete_certification']==[])
    x,s = iv(source['pi_interval']),iv(source['sqrt2_interval'])
    check('same_fixed_inputs',cert['pi_interval']==prior['pi_interval']==source['pi_interval']
          and cert['sqrt2_interval']==prior['sqrt2_interval']==source['sqrt2_interval']
          and x[1]-x[0]==s[1]-s[0]==F(1,10**60))
    check('sqrt2_containment',0<s[0] and s[0]**2<2<s[1]**2)
    atan = []
    for d,key in ((5,'atan5'),(239,'atan239')):
        terms = [F((-1)**j,(2*j+1)*d**(2*j+1)) for j in range(48)]
        partial = sum(terms,F(0))
        error = F(1,97*d**97)
        record = source[key]
        check(key+'_all_terms',record['term_count']==48 and F(record['argument'])==F(1,d)
              and list(map(F,record['terms']))==terms and F(record['partial_sum'])==partial
              and F(record['positive_remainder_upper'])==error)
        atan.append((partial,partial+error))
    machin = ia(isc(atan[0],16),isc(atan[1],-4))
    check('machin_interval',machin==iv(source['pi_machin_interval']) and contains(x,machin))
    evidence['input_containment'] = {'machin':ij(machin),'pi':ij(x),'sqrt2':ij(s),
        'branch': 'C029n analytic argument; arithmetic containment independently recomputed'}
    bern = [F(1)]
    for j in range(1,21):
        bern.append(-sum((comb(j+1,k)*bern[k] for k in range(j)),F(0))/(j+1))
    check('B0_to_B20',bern==list(map(F,cert['bernoulli_0_to_20'])) and bern[20]==F(-174611,330))
    phases = [{(0,0):F(1)},{(0,0):F(1),(0,1):F(1)},
              {(0,0):F(-1)},{(0,0):F(-1),(0,1):F(-1)}]
    v = []
    for n in range(10):
        v.append(add(*(mul({(h+1,0):-F(factorial(n)*4**h*(4**(h+1)-1)*2**(h+1),
                  factorial(n-h)*factorial(2*h+2))*bern[2*h+2]},phases[(n-h)%4])
                  for h in range(n+1))))
    beta = [add(scale(v[k],8*k*k+12*k+7),scale(v[k+2],(2*k+3)*(2*k+5)),
                scale(v[k-2],4*k*(k-1)) if k>=2 else {}) for k in range(8)]
    check('all_v_and_beta',v==list(map(dec,cert['u_over_S_polynomials']))
          and beta==list(map(dec,cert['beta_over_S_polynomials'])))
    check('prior_v_and_beta',v[:9]==list(map(dec,source['u_over_S_polynomials']))
          and beta[:7]==list(map(dec,source['beta_over_S_polynomials'])))
    p = [[F(1)]]
    for k in range(7):
        row = [F(0)]+p[k]
        if k:
            for j,a in enumerate(p[k-1]):
                row[j] -= F(2*k+1,2)*a
        p.append([a/F(k+1) for a in row])
    check('basis_and_degrees',p==[list(map(F,row)) for row in cert['basis_p_0_to_7']]
          and all(p[k][k]==F(1,factorial(k)) for k in range(8)))
    b = {}
    for n in (6,7):
        weights = [F(factorial(n),factorial(n-k)*n**k) for k in range(n+1)]
        a = [scale(beta[k],weights[k]) for k in range(n+1)]
        b[n] = [add(*(scale(a[k],p[k][i]) for k in range(i,n+1))) for i in range(n+1)]
        check(f'N{n}_all_coefficients',weights==list(map(F,cert['weights'][str(n)]))
              and a==list(map(dec,cert['Jensen_coefficients'][str(n)]))
              and b[n]==list(map(dec,cert['U_monomial_coefficients'][str(n)])))
        lead = enclose(b[n][n],x,s)
        check(f'N{n}_degree_and_bound',lead==iv(cert['leading_coefficient_intervals'][str(n)])
              and (lead[1]<0 or lead[0]>0)
              and contains(outer(cert['leading_coefficient_outer_bounds'][str(n)]),lead))
    check('prior_U6',b[6]==list(map(dec,prior['U_monomial_coefficients'])))
    save('COEFFICIENTS_VERIFIED')

    l,m,L,M = b[6][6],b[6][5],b[7][7],b[7][6]
    D = mul(l,l)
    Q = [add(mul(M,l),scale(mul(L,m),-1)),mul(L,l)]
    check('quotient_D_Q',D==dec(cert['quotient']['denominator_D_l_squared'])
          and Q==list(map(dec,cert['quotient']['Q_constant_then_linear'])))
    R = [add(mul(D,b[7][i]),scale(mul(Q[0],b[6][i]),-1) if i<=6 else {},
             scale(mul(Q[1],b[6][i-1]),-1) if i else {}) for i in range(8)]
    check('division_all_coefficients',not R[6] and not R[7]
          and R[:6]==list(map(dec,cert['quotient']['remainder_numerators_over_D']))
          and list(map(dec,cert['quotient']['division_identity_residual']))==[{}]*8)
    H = matrix(cert['embedding']['numerator_H'])
    expected = [[{} for _ in range(6)] for _ in range(7)]
    for j in range(6):
        k = 5-j
        expected[5-k][j] = scale(Q[1],k+1)
        expected[6-k][j] = Q[0]
        if k:
            expected[7-k][j] = scale(Q[1],F(2*k+1,2))
        for i in range(7):
            rhs = add(*(scale(H[a][j],p[6-a][i]) for a in range(7) if i<len(p[6-a])))
            lhs = add(scale(Q[0],p[k][i]) if i<=k else {},
                      scale(Q[1],p[k][i-1]) if 1<=i<=k+1 else {})
            check(f'embedding_column{j}_coefficient{i}',lhs==rhs)
    check('H_orientation_and_stored_residual',H==expected and
          matrix(cert['embedding']['identity_residual'])==[[{}]*7 for _ in range(6)])
    B = {}
    for n in (6,7):
        record = cert['kernels'][str(n)]
        B[n] = matrix(record['B_descending'])
        K = [[add(*(scale(B[n][a][c],p[n-1-a][i]*p[n-1-c][j])
                for a in range(n) for c in range(n)
                if i<len(p[n-1-a]) and j<len(p[n-1-c])))
              for j in range(n)] for i in range(n)]
        check(f'N{n}_K_basis_expansion',K==matrix(record['monomial_kernel']))
        deriv = [scale(b[n][i+1],i+1) for i in range(n)]+[{}]
        numerator = [[add(mul(b[n][i],deriv[j]),scale(mul(b[n][j],deriv[i]),-1))
                      for j in range(n+1)] for i in range(n+1)]
        multiplied = [[add(K[i-1][j] if i and j<n else {},
                      scale(K[i][j-1],-1) if j and i<n else {})
                       for j in range(n+1)] for i in range(n+1)]
        check(f'N{n}_complete_kernel_identity',multiplied==numerator
              ==matrix(record['numerator']) and deriv==list(map(dec,record['derivative_coefficients']))
              and B[n]==tr(B[n]))
        C = matrix(record['basis_conversion_R_descending'])
        for i in range(n):
            check(f'N{n}_inverse_basis_row{i}',all(
                add(*(scale(C[i][j],p[n-1-j][k]) for j in range(n) if k<len(p[n-1-j])))
                == ({(0,0):F(1)} if i==k else {}) for k in range(n)))
        check(f'N{n}_stored_identity_residuals',
              matrix(record['kernel_identity_residual'])==[[{}]*(n+1) for _ in range(n+1)]
              and matrix(record['basis_conversion_residual'])==[[{}]*n for _ in range(n)])
    check('B6_prior',B[6]==matrix(prior['B_descending']))
    D2 = mul(D,D)
    HBH = mm(mm(H,B[6]),tr(H))
    PN = [[add(mul(D2,B[7][i][j]),scale(HBH[i][j],-1)) for j in range(7)] for i in range(7)]
    check('full_residual',PN==matrix(cert['residual']['numerator'])
          and D2==dec(cert['residual']['denominator_D_squared']) and PN==tr(PN))
    save('ALL_EXACT_IDENTITIES_VERIFIED')

    ints = cert['intervals']
    coeff = {k:enclose(poly,x,s) for k,poly in zip(('l','m','L','M'),(l,m,L,M))}
    check('all_coefficient_intervals',coeff=={k:iv(z) for k,z in ints['leading_coefficients'].items()})
    il = inv(coeff['l'])
    di = im(coeff['l'],coeff['l'])
    iden = inv(di)
    check('all_reciprocals_and_denominators',coeff['l'][1]<0<di[0]
          and il==iv(ints['reciprocal_l']) and di==iv(ints['D'])
          and im(di,di)==iv(ints['D_squared']) and iden==iv(ints['reciprocal_D']))
    alpha = im(coeff['L'],il)
    gamma = im(ia(coeff['M'],isc(im(alpha,coeff['m']),-1)),il)
    check('alpha_gamma_endpoints',alpha==iv(ints['quotient_alpha']) and gamma==iv(ints['quotient_gamma']))
    qi = [ia(im(coeff['M'],coeff['l']),isc(im(coeff['L'],coeff['m']),-1)),im(coeff['L'],coeff['l'])]
    check('alternative_quotient_overlap',all(max(a[0],c[0])<=min(a[1],c[1])
          for a,c in zip((gamma,alpha),[im(z,iden) for z in qi])))
    Ei = [[(F(0),F(0)) for _ in range(6)] for _ in range(7)]
    for j in range(6):
        k = 5-j
        Ei[5-k][j],Ei[6-k][j] = isc(alpha,k+1),gamma
        if k:
            Ei[7-k][j] = isc(alpha,F(2*k+1,2))
    Bi = {n:[[enclose(z,x,s) for z in row] for row in B[n]] for n in (6,7)}
    Pi = [[ia(Bi[7][i][j],isc(ia(*(im(im(Ei[i][a],Bi[6][a][c]),Ei[j][c])
            for a in range(6) for c in range(6))),-1)) for j in range(7)] for i in range(7)]
    for key,wanted in (('E',Ei),('B6',Bi[6]),('B7',Bi[7]),('P',Pi)):
        check('all_interval_endpoints_'+key,[[iv(z) for z in row] for row in ints[key]]==wanted)
    directions = [(f'e{i+1}',[int(k==i) for k in range(7)]) for i in range(7)]
    directions += [(f'e{i+1}{"+" if sign==1 else "-"}e{j+1}',
                    [int(k==i)+sign*int(k==j) for k in range(7)])
                   for i in range(7) for j in range(i+1,7) for sign in (1,-1)]
    check('direction_set_size',len(cert['quadratic_forms'])==len(directions)==49
          and len({tuple(v) for _,v in directions})==49)
    forms = []
    for (name,v),record in zip(directions,cert['quadratic_forms']):
        poly = add(*(scale(PN[i][j],v[i]*v[j]) for i in range(7) for j in range(7)))
        z = ia(*(isc(Pi[i][j],v[i]*v[j]) for i in range(7) for j in range(7)))
        sign = 'NEGATIVE' if z[1]<0 else 'POSITIVE' if z[0]>0 else 'UNRESOLVED'
        check('complete_direction_'+name,record['name']==name and record['vector']==v
              and dec(record['exact_numerator_over_D_squared'])==poly
              and iv(record['interval'])==z and record['sign']==sign and contains(outer(record['outer_bound']),z))
        forms.append({'name':name,'vector':v,'interval':ij(z),'sign':sign})
    counts = {key:sum(z['sign']==key for z in forms) for key in ('NEGATIVE','POSITIVE','UNRESOLVED')}
    check('complete_sign_count',counts==cert['sign_counts']=={'NEGATIVE':48,'POSITIVE':1,'UNRESOLVED':0})
    check('selected_witness',cert['selected_witness']==cert['quadratic_forms'][1]
          and forms[0]['sign']=='POSITIVE' and forms[1]['name']=='e2')
    evidence['quadratic_forms'] = forms
    evidence['sign_counts'] = counts
    save('ALL_DIRECTIONS_AND_ENDPOINTS_VERIFIED')

    short = cert['witness_scalar_check']
    r,c = b[6][4],b[7][5]
    formulas = [scale(mul(l,l),86400),scale(mul(l,m),14400),
                scale(add(scale(mul(m,m),5),scale(mul(l,r),-2)),576),
                scale(add(scale(mul(M,M),6),scale(mul(L,c),-2)),14400)]
    check('four_short_kernel_formulas',formulas==[B[6][0][0],B[6][0][1],B[6][1][1],B[7][1][1]])
    scalar = scale(add(scale(mul(mul(L,c),D),-2),scale(mul(mul(mul(L,M),m),l),2),
                       scale(mul(mul(L,L),mul(m,m)),-1),scale(mul(mul(mul(L,L),r),l),2)),14400)
    check('short_scalar_exact_identity',scalar==dec(short['simplified_numerator_over_D'])
          and mul(D,scalar)==PN[1][1] and not dec(short['exact_identity_residual']))
    small = {k:outer(z) for k,z in short['six_small_rational_input_bounds'].items()}
    true_inputs = dict(zip(('alpha','gamma','B6_11','B6_12','B6_22','B7_22'),
                      (alpha,gamma,Bi[6][0][0],Bi[6][0][1],Bi[6][1][1],Bi[7][1][1])))
    check('six_small_bounds_contain_complete_intervals',all(contains(small[k],v) for k,v in true_inputs.items()))
    aa,gg = small['alpha'],small['gamma']
    coarse = ia(small['B7_22'],isc(ia(im(im(gg,gg),small['B6_11']),
                isc(im(im(aa,gg),small['B6_12']),10),isc(im(im(aa,aa),small['B6_22']),25)),-1))
    claim = (F('-7.961713e-7'),F('-7.961712e-7'))
    check('coarse_exact_rational_endpoints',coarse==iv(short['coarse_interval'])==
          (F(-15923511251909218749,20000000000000000000000000),
           F(-159233597632112199611,200000000000000000000000000)))
    margin = -F(79,10**8)-coarse[1]
    check('entire_strict_upper_bound_comparison',margin==F(short['strict_upper_margin'])==
          F(1233597632112199611,200000000000000000000000000)>0
          and F(short['strict_comparison_upper_bound'])==-F(79,10**8))
    tight = iv(forms[1]['interval'])
    check('complete_tight_claim',contains(claim,tight) and contains(coarse,tight) and claim[1]<0)
    direct = ia(Bi[7][1][1],isc(im(im(gamma,gamma),Bi[6][0][0]),-1),
                isc(im(im(alpha,gamma),Bi[6][0][1]),-10),isc(im(im(alpha,alpha),Bi[6][1][1]),-25))
    check('direct_six_input_full_interval_agrees',direct==tight)
    evidence['witness'] = {'tight':ij(tight),'claimed':ij(claim),'coarse':ij(coarse),
        'required_upper':str(-F(79,10**8)),'strict_margin':str(margin),
        'small_bounds':{k:ij(z) for k,z in small.items()}}
    evidence['scope'] = 'N=6,7 only; fixed inputs, no original algebra helpers; no RH or eventual index claim'
    save('AUDIT_PASSED')
    print(json.dumps({'status':evidence['status'],'checks':len(checks),'failures':evidence['failures'],
          'actual_e2_bounds':ij(claim),'required_upper':'<0','sign_counts':counts,
          'strict_coarse_margin':str(margin),'certificate':str(OUT.relative_to(ROOT.parent.parent))},indent=2))


if __name__=='__main__':
    main()
