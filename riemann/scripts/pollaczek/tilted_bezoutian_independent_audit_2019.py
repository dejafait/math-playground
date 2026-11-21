#!/usr/bin/env python3
"""Independent fixed-input audit of C029p; no imported research helpers.

Reconstruct the full coefficient family and verify its kernel by basis
expansion rather than reusing the original kernel-construction routine.
Read and recompute every stored interval endpoint/permutation term.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent
checks = {}


def check(name, value):
    checks[name] = bool(value)


# Sparse polynomials in X,s modulo s^2=2. No original math helper imported.
def plus(*items):
    ans = {}
    for p in items:
        for key, value in p.items():
            ans[key] = ans.get(key, Q(0)) + value
    return {k: v for k, v in ans.items() if v}


def scale(p, c):
    return {k: v*c for k, v in p.items() if v*c}


def product(p, q):
    ans = {}
    for (i,j), a in p.items():
        for (k,l), b in q.items():
            key = i+k, (j+l) % 2
            ans[key] = ans.get(key,Q(0)) + a*b*2**((j+l)//2)
    return {k: v for k,v in ans.items() if v}


def decode(p):
    return {(i,j): Q(c[key]) for i,c in enumerate(p)
            for j,key in enumerate(('rational','sqrt2')) if Q(c[key])}


def decode_matrix(m):
    return [[decode(p) for p in row] for row in m]


def transpose(m):
    return list(map(list,zip(*m)))


def matmul(a,b):
    return [[plus(*(product(a[i][k],b[k][j]) for k in range(len(b))))
             for j in range(len(b[0]))] for i in range(len(a))]


def iv(obj):
    return Q(obj['lower']), Q(obj['upper'])


def isum(a,b):
    return a[0]+b[0], a[1]+b[1]


def itimes(a,b):
    corners = [x*y for x in a for y in b]
    return min(corners),max(corners)


def istretch(a,c):
    return min(c*a[0],c*a[1]),max(c*a[0],c*a[1])


def enclose(p,x,s):
    value = Q(0),Q(0)
    for i in range(max((k[0] for k in p), default=0),-1,-1):
        coefficient = isum((p.get((i,0),Q(0)),)*2,
                            istretch(s,p.get((i,1),Q(0))))
        value = isum(itimes(value,x),coefficient)
    return value


def interval_json(x):
    return {'lower':str(x[0]),'upper':str(x[1])}


def main():
    paths = ['tilted-boundary-metric-2010.json',
             'tilted-bezoutian-n6-2014.json','tilted-bezoutian-entrywise-2017.json']
    raw = {p:(ROOT/p).read_bytes() for p in paths}
    source, construction, cert = [json.loads(raw[p]) for p in paths]
    for p,wanted in cert['required_sha256'].items():
        check('pinned_'+p,hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==wanted
              ==cert['input_sha256'][p])
    x,s = iv(source['pi_interval']),iv(source['sqrt2_interval'])
    check('unchanged_input_intervals',
          cert['pi_interval']==construction['pi_interval']==source['pi_interval']
          and cert['sqrt2_interval']==construction['sqrt2_interval']==source['sqrt2_interval'])
    check('fixed_grid',x[1]-x[0]==s[1]-s[0]==Q(1,10**60))
    check('sqrt2_containment',0<s[0] and s[0]**2<2<s[1]**2)
    atan = []
    for denominator,key in ((5,'atan5'),(239,'atan239')):
        terms=[Q((-1)**j,(2*j+1)*denominator**(2*j+1)) for j in range(48)]
        partial=sum(terms,Q(0))
        remainder=Q(1,97*denominator**97)
        record=source[key]
        check(key+'_complete_terms',record['term_count']==48
              and Q(record['argument'])==Q(1,denominator)
              and list(map(Q,record['terms']))==terms
              and Q(record['partial_sum'])==partial
              and Q(record['positive_remainder_upper'])==remainder)
        atan.append((partial,partial+remainder))
    machin=isum(istretch(atan[0],16),istretch(atan[1],-4))
    check('machin_exact_and_contained',machin==iv(source['pi_machin_interval'])
          and x[0]<=machin[0]<=machin[1]<=x[1])
    # The analytic branch justification is in C029n, not proved by this equality.
    check('machin_tangent_identity',
          (Q(120,119)-Q(1,239))/(1+Q(120,119)*Q(1,239))==1)

    bern=[Q(1)]
    for m in range(1,19):
        bern.append(-sum((Q(comb(m+1,k))*bern[k] for k in range(m)),Q(0))/(m+1))
    check('every_bernoulli',bern==list(map(Q,source['bernoulli_0_through_18'])))
    phases=[{(0,0):Q(1)}, {(0,0):Q(1),(0,1):Q(1)},
            {(0,0):Q(-1)}, {(0,0):Q(-1),(0,1):Q(-1)}]
    u=[]
    for n in range(9):
        terms=[]
        for h in range(n+1):
            scalar=-Q(factorial(n)*4**h*(4**(h+1)-1)*2**(h+1),
                       factorial(n-h)*factorial(2*h+2))*bern[2*h+2]
            terms.append(product({(h+1,0):scalar},phases[(n-h)%4]))
        u.append(plus(*terms))
        check('source_u_'+str(n),u[n]==decode(source['u_over_S_polynomials'][n]))
    coefficients=[]
    for n in range(7):
        beta=plus(scale(u[n],8*n*n+12*n+7),scale(u[n+2],(2*n+3)*(2*n+5)),
                  scale(u[n-2],4*n*(n-1)) if n>=2 else {})
        weight=Q(factorial(6),factorial(6-n)*6**n)
        coefficients.append(scale(beta,weight))
        check('source_beta_and_weight_'+str(n),beta==decode(source['beta_over_S_polynomials'][n])
              and weight==Q(source['weights'][n]))
        check('all_saved_coefficients_'+str(n),coefficients[n]==decode(source['a_over_S_polynomials'][n])
              ==decode(construction['a_over_S_polynomials'][n]))
    top=enclose(coefficients[6],x,s)
    check('actual_degree_six',Q('-0.000894198695')<=top[0]<=top[1]
          <=Q('-0.000894198694')<0)

    # Rational basis: every recurrence coefficient is independently applied.
    basis=[[Q(1)]]
    for k in range(6):
        row=[Q(0)]+basis[k]
        if k:
            for j,c in enumerate(basis[k-1]):
                row[j]-=Q(2*k+1,2)*c
        basis.append([v/(k+1) for v in row])
    check('all_basis_coefficients',basis==[list(map(Q,p)) for p in construction['basis_p_0_to_6']])
    check('invertible_degree_graded_basis',all(len(p)==k+1 and p[k]==Q(1,factorial(k))
                                             for k,p in enumerate(basis)))
    b=[plus(*(scale(coefficients[k],basis[k][i]) for k in range(i,7))) for i in range(7)]
    d=[scale(b[i+1],i+1) for i in range(6)]+[{}]
    check('U_and_derivative',b==list(map(decode,construction['U_monomial_coefficients']))
          and d==list(map(decode,construction['derivative_coefficients'])))
    B=decode_matrix(cert['B_descending'])
    check('full_B_unchanged_and_symmetric',len(B)==6 and all(len(r)==6 for r in B)
          and B==decode_matrix(construction['B_descending']) and B==transpose(B))
    # Expand the STORED B in the polynomial basis, without using the original
    # construction formula or its basis-inversion helper.
    kernel=[[plus(*(scale(B[h][k],basis[5-h][i]*basis[5-k][j])
                    for h in range(6) if i<len(basis[5-h])
                    for k in range(6) if j<len(basis[5-k])))
             for j in range(6)] for i in range(6)]
    check('all_monomial_kernel_coefficients',kernel==decode_matrix(construction['B_monomial']))
    numerator=[[plus(product(b[i],d[j]),scale(product(d[i],b[j]),-1))
                for j in range(7)] for i in range(7)]
    residual=[]
    for i in range(7):
        for j in range(7):
            multiplied=plus(kernel[i-1][j] if i>0 and j<6 else {},
                            scale(kernel[i][j-1],-1) if i<6 and j>0 else {})
            residual.append(plus(multiplied,scale(numerator[i][j],-1)))
    check('all_49_kernel_identity_coefficients',not any(residual))
    # Independently verify V/R conversion by its defining coefficient equations.
    R=[[Q(c) for c in row] for row in construction['monomials_in_ascending_basis_R']]
    check('all_36_inverse_basis_coefficients',all(
        sum((R[i][k]*(basis[k][j] if j<len(basis[k]) else 0) for k in range(6)),Q(0))
        ==int(i==j) for i in range(6) for j in range(6)))

    alpha=coefficients[6]
    C=[[{} for _ in range(6)] for _ in range(6)]
    for i in range(5):
        C[i][i+1]=scale(alpha,Q(11-2*i,2))
        C[i+1][i]=scale(alpha,5-i)
    for j in range(6):
        C[0][j]=plus(C[0][j],scale(coefficients[5-j],-6))
    check('cleared_C_unchanged',C==decode_matrix(construction['Ctilde']))
    comrade=[]
    for i in range(6):
        for j in range(7):
            expression=plus(*(scale(C[i][k],basis[5-k][j]) for k in range(6)
                              if j<len(basis[5-k])))
            if j>0 and j-1<len(basis[5-i]):
                expression=plus(expression,scale(alpha,-basis[5-i][j-1]))
            if i==0:
                expression=plus(expression,scale(b[j],6))
            comrade.append(expression)
    check('all_42_evaluation_comrade_coefficients',not any(comrade))
    check('all_36_left_metric_coefficients',matmul(transpose(C),B)==matmul(B,C))
    leading_row=[plus(*(scale(B[0][j],basis[5-j][i]) for j in range(6)
                        if i<len(basis[5-j]))) for i in range(6)]
    check('all_6_leading_row_orientation_coefficients',
          leading_row==[scale(poly,Q(1,6)) for poly in [product(alpha,d[i]) for i in range(6)]])
    squared=[Q(1)]
    for k in range(1,6):
        squared.insert(0,Q(2*k+1,2*k)*squared[0])
    check('positive_D_squared',squared==list(map(Q,cert['D_squared']))
          ==list(map(Q,construction['D_squared']))==list(map(Q,source['D_squared']))
          and all(t>0 for t in squared))

    entries=[[enclose(p,x,s) for p in row] for row in B]
    check('all_36_exact_entry_intervals',entries==[[iv(p) for p in row] for row in cert['entry_intervals']])
    check('six_minors',len(cert['minors'])==6)
    signs=[]
    details=[]
    for n,minor in enumerate(cert['minors'],1):
        records=minor['permutations']
        seen=[tuple(r['permutation_zero_based']) for r in records]
        check('complete_unique_permutations_'+str(n),len(seen)==factorial(n)
              and len(set(seen))==len(seen) and set(seen)==set(permutations(range(n))))
        total=Q(0),Q(0)
        term_checks=[]
        for index,r in enumerate(records):
            perm=tuple(r['permutation_zero_based'])
            inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
            sign=1 if inversions%2==0 else -1
            term=Q(1),Q(1)
            for row,col in enumerate(perm):
                term=itimes(term,entries[row][col])
            signed=istretch(term,sign)
            valid=(r['inversions']==inversions and r['sign']==sign
                   and term==iv(r['product_interval']) and signed==iv(r['signed_product_interval']))
            term_checks.append({'term':index,'all_endpoints_and_parity_match':valid})
            total=isum(total,signed)
        check('every_term_'+str(n),all(t['all_endpoints_and_parity_match'] for t in term_checks))
        check('complete_raw_minor_endpoints_'+str(n),total==iv(minor['interval']))
        outer=minor['readable_outer_enclosure']
        short=iv(outer['scaled_interval'])
        unit=Q(10)**outer['power_of_ten']
        check('outer_bound_'+str(n),short[0]*unit<=total[0]<=total[1]<=short[1]*unit)
        sign=1 if total[0]>0 else -1 if total[1]<0 else 0
        check('strict_sign_'+str(n),sign==minor['sign']!=0)
        signs.append(sign)
        details.append({'minor':n,'terms':term_checks,'raw_interval':interval_json(total),
                        'outer_bound':outer,'sign':sign})
    check('required_six_signs',signs==cert['leading_determinant_signs']==[1,1,1,1,1,-1])
    count=sum(a!=b for a,b in zip([1]+signs,signs))
    inertia={'positive':6-count,'negative':count,'zero':0}
    check('Jacobi_and_report',inertia==cert['actual_inertia']=={'positive':5,'negative':1,'zero':0}
          and cert['threshold_pass'] is True and cert['unresolved_determinants']==[])
    failures=[k for k,v in checks.items() if not v]
    report={'target':'Independent audit of C029p at fixed N=6 and unchanged inputs',
            'reproduction':'python3 scripts/pollaczek/tilted_bezoutian_independent_audit_2019.py',
            'input_sha256':{p:hashlib.sha256(raw[p]).hexdigest() for p in paths},
            'checks':checks,'failures':failures,'degree_coefficient_interval':interval_json(top),
            'complete_minor_evidence':details,'permutation_terms_checked':sum(len(d['terms']) for d in details),
            'signs':signs,'actual_inertia':inertia,
            'required':'All six strict signs and correct real symmetric kernel orientation; N=6 only',
            'result':'PASS' if not failures else 'FAIL',
            'scope':'Independent exact application audit, not formal verification or eventual index bound'}
    out=ROOT/'tilted-bezoutian-independent-audit-2019.json'
    out.write_text(json.dumps(report,indent=2)+'\n')
    print('Result:',report['result'],'; checks:',len(checks),'; failures:',failures)
    print('Actual signs:',signs,'; inertia:',inertia,'; all terms:',report['permutation_terms_checked'])
    print('Required:',report['required'])
    for d in details:
        print('Delta_'+str(d['minor'])+':',d['outer_bound'])
    print('Full exact certificate:',out.relative_to(Path.cwd()))
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
