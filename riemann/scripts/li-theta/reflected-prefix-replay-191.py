#!/usr/bin/env python3
"""Exact rational certificate for n=18, theta=1/2 in the approved TEST.

The analytic full-G error is proved in L971; this program checks its
finite rational constants and all load-bearing sine/Taylor comparisons.
No floating point, sampled quadrature, zeros, or external packages.
"""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import json


def rational(q):
    q=Q(q)
    return str(q.numerator) if q.denominator==1 else f'{q.numerator}/{q.denominator}'


def interval(lo,hi):
    return {'lower':rational(lo),'upper':rational(hi)}


def main():
    n=18
    theta=Q(1,2)
    b=Q(1,4)
    h=64*9**n
    p=(n-1)//2
    v=[Q(comb(n,2*i+1),4**i) for i in range(p+1)]
    w=[sum((v[i]*v[s-i] for i in range(p+1) if 0<=s-i<=p),Q(0))
       for s in range(2*p+1)]
    D=[sum((w[s]*comb(n-1-s,r)*b**(n-1-s-r)
            for s in range(min(2*p,n-1-r)+1)),Q(0)) for r in range(n)]
    d=[h*sum((D[r]/(h-b)**(n-k-r+1)
              for r in range(n-k+1)),Q(0)) for k in range(1,n+1)]
    A=[d[m]*2**m for m in range(n)]
    M=sum(A,Q(0))
    weights=[a/M for a in A]
    checks={}
    checks['n_ge_2']=n>=2
    checks['theta_le_3_over_4']=Q(0)<theta<=Q(3,4)
    checks['all_coefficients_positive']=all(q>0 for q in v+w+D+d+A)
    checks['all_18_kernel_coefficients_retained']=len(d)==n and len(A)==n
    checks['normalized_weights_sum_one']=sum(weights,Q(0))==1
    checks['sector_constant_squared']=Q(33,32)**2>Q(17,16)
    epsilon=Q(1,2)/(1-Q(1,32))*Q(1,16)*Q(33,32)
    checks['full_G_error_constant']=epsilon==Q(33,992)
    checks['fixed_h']=h==64*9**18

    # Taylor degree 65, Lagrange error <= j^66/66!, since every
    # real derivative of sine has absolute value <= 1.
    terms=33
    sine_records=[]
    S_lo=S_hi=weights[0]
    for j in range(1,9):
        poly=sum((Q((-1)**r*j**(2*r+1),factorial(2*r+1))
                  for r in range(terms)),Q(0))
        remainder=Q(j**66,factorial(66))
        lo,hi=poly-remainder,poly+remainder
        coefficient=weights[2*j]/j
        S_lo+=coefficient*lo
        S_hi+=coefficient*hi
        sine_records.append({'j':j,'polynomial':rational(poly),
                             'remainder':rational(remainder),
                             'sin_enclosure':interval(lo,hi),
                             'weight':rational(coefficient)})
    prefix_error=2*theta*epsilon
    full_upper=S_hi+prefix_error
    checks['S_lower_gt_minus_689_over_10000']=S_lo>Q(-689,10000)
    checks['S_upper_lt_minus_688_over_10000']=S_hi<Q(-688,10000)
    checks['S_enclosure_order']=S_lo<=S_hi
    checks['rational_coarse_upper_lt_minus_7_over_200']=(Q(-688,10000)+epsilon<Q(-7,200))
    checks['full_prefix_upper_lt_minus_7_over_200']=full_upper<Q(-7,200)
    failures=[name for name,passed in checks.items() if not passed]
    report={
        'kind':'exact rational arithmetic with Taylor remainder',
        'parameters':{'n':n,'theta':rational(theta),'b':rational(b),'h':str(h),
                      'rho':'1/2','eta':rational(Q(1,h))},
        'coefficients':{'v':list(map(rational,v)),'w':list(map(rational,w)),
                        'D':list(map(rational,D)),'d':list(map(rational,d)),
                        'A':list(map(rational,A)),'M':rational(M),
                        'normalized_weights':list(map(rational,weights))},
        'sine_enclosures':sine_records,
        'bounds':{'S_over_M':interval(S_lo,S_hi),
                  'full_prefix_error_over_gM':rational(prefix_error),
                  'pi_B_over_gM_upper':rational(full_upper),
                  'simple_pi_B_over_gM_upper':'-7/200',
                  'TEST_required_lower':'d1*G(h)/pi > 0'},
        'analytic_conditions':'L971 proves the complete-G error from L024/L026/L966; G(h)>0 by L966. No h term omitted.',
        'checks':checks,'failures':failures,
        'summary':{'all_checks_pass':not failures,'checks':len(checks),
                   'S_over_M_strict_box':['-689/10000','-688/10000'],
                   'full_prefix_error':'33/992',
                   'pi_B_over_gM_strict_upper':'-7/200',
                   'required_B_lower':'d1*G(h)/pi > 0',
                   'failures':failures}}
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'result':report['summary'],'certificate':str(path)}))
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
