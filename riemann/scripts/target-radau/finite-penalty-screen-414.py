#!/usr/bin/env python3
"""Fixed-precision necessary-condition screen for the approved Radau test.

Exact complete continuum target norm; no slope samples or asymptotics.
If d < lambda B^2, PSD proves F < 0 before any Lanczos step.
The full certificate records terms, products, moments and directed bounds.
"""
from pathlib import Path
import importlib.util
from decimal import Decimal as D, getcontext
from fractions import Fraction as Q
from math import factorial, isqrt
import json

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('atomic371', ROOT/'scripts/adaptive-slope/direct-kernel-atomic-371.py')
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)
PREC = 660
getcontext().prec = PREC
getcontext().Emax = 999999
getcontext().Emin = -999999
a.LO.prec = a.HI.prec = PREC
R, C = a.R, a.C
LO, HI = a.LO, a.HI


def exp(z):
    z = C(z)
    scale = 0
    while z.upper_abs() > D(1)/8:
        z = z/2
        scale += 1
    term = total = C(1)
    for k in range(1, 257):
        term = term*z/k
        total = total+term
    err = R(Q(2, 8**257*factorial(257))).hi
    total = total+C(R(-err, err), R(-err, err))
    for _ in range(scale):
        total = total*total
    return total


def conjugate(z):
    return C(z.re, -z.im)


def width(z):
    return max(HI.subtract(z.re.hi,z.re.lo), HI.subtract(z.im.hi,z.im.lo))


def target_terms(n):
    """k(c,1+i/8) = sum P_l(c) exp(alpha_l c), exactly."""
    terms, lower = [], C(0)
    for base in (Q(-1,8), Q(-7,8)):
        ar, ai = base-Q(1,8), Q(1)
        coeff = a.primitive_coefficients(n, C(ar, ai))
        def at(t):
            return exp(C(ar*t, ai*t))*a.evaluate_polynomial(coeff, Q(t))
        lower = lower+at(n+2)-at(n)
        for s, sign in ((n,1),(n+2,-1)):
            p = [v*(sign*s**j) for j,v in enumerate(coeff)]
            terms.append({'alpha':(ar*s-Q(n,4),ai*s), 'coeff':p})
    terms.append({'alpha':(-Q(n,4),Q(0)), 'coeff':[lower]})
    return terms


def moments(ar, ai, degree):
    left, right = Q(7,4), Q(9,4)
    if ar == 0 and ai == 0:
        return [C((right**(k+1)-left**(k+1))/Q(k+1)) for k in range(degree+1)], 'zero'
    alpha = C(ar, ai)
    ea, eb = exp(C(ar*left,ai*left)), exp(C(ar*right,ai*right))
    result = [(eb-ea)/alpha]
    for k in range(1, degree+1):
        result.append((eb*(right**k)-ea*(left**k)-result[-1]*k)/alpha)
    return result, 'nonzero'


def product_integral(t1,t2):
    # conjugate(P1(c))*P2(c), with c real, then integrate each monomial.
    ar = t1['alpha'][0]+t2['alpha'][0]
    ai = -t1['alpha'][1]+t2['alpha'][1]
    p,q = t1['coeff'], t2['coeff']
    prod = [C(0) for _ in range(len(p)+len(q)-1)]
    for j,pj in enumerate(p):
        cp = conjugate(pj)
        for k,qk in enumerate(q):
            prod[j+k] = prod[j+k]+cp*qk
    ms,case = moments(ar,ai,len(prod)-1)
    value = C(0)
    for coeff,m in zip(prod,ms):
        value = value+coeff*m
    return value, {'alpha':[str(ar),str(ai)], 'case':case,
                   'product_coefficients':[v.json() for v in prod],
                   'moments':[v.json() for v in ms], 'integral':value.json()}


def one(n, out):
    result = {'n':n, 'status':'IN_PROGRESS', 'precision_decimal_digits':PREC,
              'interval':['7/4','9/4'], 'target':['1','1/8'], 'lanczos_steps':0}
    out.write_text(json.dumps(result))
    terms = target_terms(n)
    result['target_terms']=[{'alpha':[str(x) for x in t['alpha']],
                            'coefficients':[v.json() for v in t['coeff']]} for t in terms]
    result['products'] = []
    # Diagonals plus twice real off-diagonals; no imaginary cancellation claim.
    d = R(0)
    for i in range(len(terms)):
        for j in range(i,len(terms)):
            value,record = product_integral(terms[i],terms[j])
            record.update({'i':i,'j':j,'multiplicity':1 if i==j else 2})
            result['products'].append(record)
            d = d+value.re*(1 if i==j else 2)
        print('completed target product row',n,i,flush=True)
        result['partial_d'] = d.json()
        out.write_text(json.dumps(result))
    lam = exp(C(Q(-n,16))).re
    denominator = 2**2048
    root = isqrt(n*denominator**2)
    sqrt_n = R(R(Q(root,denominator)).lo,R(Q(root+1,denominator)).hi)
    budget = exp(C(sqrt_n)).re
    penalty = lam*budget*budget
    f_upper = HI.subtract(d.hi,penalty.lo)
    entry_limit = R(Q(1,2**256)).lo
    endpoint_limit = R(Q(1,2**60)).lo
    entry_widths = {
        'd':str(HI.subtract(d.hi,d.lo)),
        'lambda':str(HI.subtract(lam.hi,lam.lo)),
        'B':str(HI.subtract(budget.hi,budget.lo))}
    # This is arithmetic uncertainty in the upper-obstruction expression,
    # not an enclosure of F, whose nonnegative inverse term is uncomputed.
    screen = d-penalty
    screen_width = HI.subtract(screen.hi,screen.lo)
    checks = {
        'd_interval_nonnegative':d.lo>=0,
        'd_width_le_2^-256':D(entry_widths['d'])<=entry_limit,
        'lambda_width_le_2^-256':D(entry_widths['lambda'])<=entry_limit,
        'B_width_le_2^-256':D(entry_widths['B'])<=entry_limit,
        'screen_arithmetic_width_le_2^-60':screen_width<=endpoint_limit,
        'strict_penalty_obstruction':f_upper<0,
        'zero_lanczos_steps':True}
    result.update({'status':'COMPLETED','d':d.json(),'lambda':lam.json(),
                   'B':budget.json(),'penalty':penalty.json(),
                   'screen_d_minus_penalty':screen.json(),'F_upper':str(f_upper),
                   'entry_widths':entry_widths,'entry_required':str(entry_limit),
                   'screen_arithmetic_width':str(screen_width),
                   'screen_width_required':str(endpoint_limit),
                   'checks':checks,'failures':[k for k,v in checks.items() if not v],
                   'not_computed':['G','h','Gauss endpoint','Radau endpoint','inverse form'],
                   'decision':'PARK' if all(checks.values()) else 'UNRESOLVED'})
    out.write_text(json.dumps(result))
    print(json.dumps({'n':n,'d_upper_approx':format(d.hi,'.9E'),
                      'penalty_lower_approx':format(penalty.lo,'.9E'),
                      'F_upper_approx':format(f_upper,'.9E'), 'd_width':entry_widths['d'],
                      'screen_width':str(screen_width), 'checks':checks,
                      'failures':result['failures'],'certificate':str(out.relative_to(ROOT))}),flush=True)
    return result


if __name__ == '__main__':
    for n in (64,128):
        path = ROOT/f'scripts/target-radau/finite-penalty-screen-{n}-414.json'
        one(n,path)
