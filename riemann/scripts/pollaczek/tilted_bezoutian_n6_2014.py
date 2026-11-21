#!/usr/bin/env python3
"""Approved full T_6 derivative Bezoutian: exact coefficients and intervals.

Run from riemann: python3 scripts/pollaczek/tilted_bezoutian_n6_2014.py
Polynomials in pi have coefficients (a,b)=a+b*sqrt(2), a,b rational.
The determinant recursion is the finite Leibniz sum grouped by column
subsets (Laplace expansion); no division or numerical matrix API is used.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import sys

import tilted_boundary_metric_2010 as base

ROOT = Path(__file__).parent
INPUT = ROOT / 'tilted-boundary-metric-2010.json'
# Exact generated endpoints can exceed Python's input-string safety limit.
# This only permits serialization; it changes no arithmetic or enclosure.
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
Z = (F(0), F(0))
ONE = [(F(1), F(0))]


def trim(p):
    p = list(p)
    while p and p[-1] == Z:
        p.pop()
    return p


def add(*ps):
    out = []
    for p in ps:
        if len(out) < len(p):
            out.extend([Z] * (len(p)-len(out)))
        for i, (a, b) in enumerate(p):
            out[i] = out[i][0]+a, out[i][1]+b
    return trim(out)


def scale(p, c):
    return trim([(a*c, b*c) for a,b in p])


def mul(p, q):
    if not p or not q:
        return []
    out = [Z] * (len(p)+len(q)-1)
    for i, (a,b) in enumerate(p):
        if (a,b) == Z:
            continue
        for j, (c,d) in enumerate(q):
            if (c,d) != Z:
                v,w = out[i+j]
                out[i+j] = v+a*c+2*b*d, w+a*d+b*c
    return trim(out)


def decode(p):
    return trim([(F(c['rational']),F(c['sqrt2'])) for c in p])


def encode(p):
    return base.poly_json(p)


def rat(p):
    return [(F(c),F(0)) for c in p]


def matmul(a,b):
    return [[add(*(mul(a[i][k],b[k][j]) for k in range(len(b))))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def matrix_json(a):
    return [[encode(p) for p in row] for row in a]


def determinant(a):
    n = len(a)

    @lru_cache(None)
    def expand(cols):
        row = n-len(cols)
        if not cols:
            return ONE
        return add(*(scale(mul(a[row][j],expand(cols[:k]+cols[k+1:])),
                           (-1)**k) for k,j in enumerate(cols)))
    return expand(tuple(range(n)))


def main():
    raw = INPUT.read_bytes()
    data = json.loads(raw)
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)

    pi_iv = tuple(F(data['pi_interval'][k]) for k in ('lower','upper'))
    sqrt_iv = tuple(F(data['sqrt2_interval'][k]) for k in ('lower','upper'))
    # Reuse exactly the audited grid, never increase the input precision.
    check('fixed_pi_grid_width', pi_iv[1]-pi_iv[0] == F(1,10**60))
    check('fixed_sqrt2_grid', sqrt_iv[1]-sqrt_iv[0] == F(1,10**60)
          and 0 < sqrt_iv[0]**2 < 2 < sqrt_iv[1]**2)
    bern = [F(1)]
    for m in range(1,19):
        bern.append(-sum((comb(m+1,k)*bern[k] for k in range(m)),F(0))/(m+1))
    phase = [(F(1),F(0)),(F(1),F(1)),(F(-1),F(0)),(F(-1),F(-1))]
    u = []
    for n in range(9):
        p = [Z]*(n+2)
        for h in range(n+1):
            c = -F(factorial(n)*4**h*(4**(h+1)-1)*2**(h+1),
                   factorial(n-h)*factorial(2*h+2))*bern[2*h+2]
            a,b = phase[(n-h)%4]
            p[h+1] = c*a,c*b
        u.append(trim(p))
    beta = [add(scale(u[n],8*n*n+12*n+7),
                scale(u[n+2],(2*n+3)*(2*n+5)),
                scale(u[n-2],4*n*(n-1)) if n>=2 else []) for n in range(7)]
    weights = [F(factorial(6),factorial(6-k)*6**k) for k in range(7)]
    a = [scale(beta[k],weights[k]) for k in range(7)]
    check('all_input_u_coefficients',u == list(map(decode,data['u_over_S_polynomials'])))
    check('all_input_beta_coefficients',beta == list(map(decode,data['beta_over_S_polynomials'])))
    check('all_input_a_coefficients',a == list(map(decode,data['a_over_S_polynomials'])))
    check('all_input_weights',weights == list(map(F,data['weights'])))
    top_iv = base.peval(a[6],pi_iv,sqrt_iv)
    check('actual_degree_six',top_iv[1] < 0)

    # Rational monomial coefficients of p_0,...,p_6, ascending powers.
    p = [[F(1)]]
    for k in range(6):
        t = [F(0)]+p[k]
        if k:
            for j,c in enumerate(p[k-1]):
                t[j] -= F(2*k+1,2)*c
        p.append([c/F(k+1) for c in t])
    check('basis_leading_coefficients',all(p[k][k] == F(1,factorial(k)) for k in range(7)))
    b = [add(*(scale(a[k],p[k][i]) for k in range(i,7))) for i in range(7)]
    d = [scale(b[i+1],i+1) for i in range(6)]+[[]]

    # N(x,y)=U(x)U'(y)-U'(x)U(y); exact quotient K=N/(x-y).
    numerator = [[add(mul(b[i],d[j]),scale(mul(d[i],b[j]),-1))
                  for j in range(7)] for i in range(7)]
    bm = [[[] for _ in range(6)] for _ in range(6)]
    for i in range(7):
        for j in range(i):
            for l in range(i-j):
                bm[i-1-l][j+l] = add(bm[i-1-l][j+l],numerator[i][j])
    residual = [[list(v) for v in row] for row in numerator]
    for i in range(6):
        for j in range(6):
            residual[i+1][j] = add(residual[i+1][j],scale(bm[i][j],-1))
            residual[i][j+1] = add(residual[i][j+1],bm[i][j])
    check('all_49_kernel_residual_coefficients',not any(v for row in residual for v in row))
    check('monomial_kernel_symmetric',bm == transpose(bm))

    # V_ik=[t^i]p_k. R expresses t^i=sum_k R_ik p_k.
    v = [[p[k][i] if i<=k else F(0) for k in range(6)] for i in range(6)]
    r = []
    for i in range(6):
        rem = [F(0)]*6
        rem[i] = F(1)
        coeff = [F(0)]*6
        for k in range(5,-1,-1):
            coeff[k] = rem[k]/p[k][k]
            for j,c in enumerate(p[k]):
                rem[j] -= coeff[k]*c
        check('basis_conversion_remainder_'+str(i),not any(rem))
        r.append(coeff)
    rr = [[rat([x]) for x in row] for row in r]
    # Descending basis: Rdesc has its columns reversed.
    rd = [list(reversed(row)) for row in rr]
    bd = matmul(matmul(transpose(rd),bm),rd)
    vd = [[rat([x]) for x in reversed(row)] for row in v]
    check('all_basis_conversion_coefficients',matmul(matmul(vd,bd),transpose(vd)) == bm)
    check('all_36_B_entries_symmetric',bd == transpose(bd))

    # Clear only alpha=a6/S, proved nonzero, from the evaluation comrade.
    ct = [[[] for _ in range(6)] for _ in range(6)]
    for i in range(5):
        k = 5-i
        ct[i][i+1] = scale(a[6],F(2*k+1,2))
        ct[i+1][i] = scale(a[6],k)
    for j in range(6):
        ct[0][j] = add(ct[0][j],scale(a[5-j],-6))
    # Check Ctilde Phi = alpha*t*Phi - 6Ue1, coefficient by coefficient.
    comrade_residual = []
    for i in range(6):
        row = []
        for power in range(7):
            val = add(*(scale(ct[i][j],p[5-j][power])
                        for j in range(6) if power<len(p[5-j])))
            if power>=1 and power-1<len(p[5-i]):
                val = add(val,scale(a[6],-p[5-i][power-1]))
            if i==0:
                val = add(val,scale(b[power],6))
            row.append(val)
        comrade_residual.append(row)
    check('all_42_comrade_identity_coefficients',not any(v for row in comrade_residual for v in row))
    left,right = matmul(transpose(ct),bd),matmul(bd,ct)
    metric_residual = [[add(left[i][j],scale(right[i][j],-1)) for j in range(6)] for i in range(6)]
    check('all_36_cleared_left_metric_entries',not any(v for row in metric_residual for v in row))
    d2 = list(map(F,data['D_squared']))
    check('positive_D_scaling',d2 == [F(693,256),F(315,128),F(35,16),F(15,8),F(3,2),F(1)]
          and all(t>0 for t in d2)
          and all(F(11-2*i,2)*d2[i+1] == (5-i)*d2[i] for i in range(5)))

    dets,intervals,signs,readable,zero_witnesses = [],[],[],[],[]
    for n in range(1,7):
        delta = determinant([row[:n] for row in bd[:n]])
        iv = base.peval(delta,pi_iv,sqrt_iv)
        sign = 1 if iv[0]>0 else -1 if iv[1]<0 else 0
        dets.append(delta)
        intervals.append(iv)
        signs.append(sign)
        # Convenient scale-free rational comparison, keeping full endpoints.
        magnitude = max(abs(iv[0]),abs(iv[1]))
        if magnitude:
            exponent = len(str(magnitude.numerator))-len(str(magnitude.denominator))
            unit = F(10)**exponent
            while magnitude<unit:
                exponent-=1
                unit/=10
            while magnitude>=10*unit:
                exponent+=1
                unit*=10
            normalized = base.outward_grid((iv[0]/unit,iv[1]/unit),6)
            readable.append({'power_of_ten':exponent,'scaled_interval':base.interval_json(normalized)})
            check('readable_bounds_outward_'+str(n),
                  normalized[0]*unit <= iv[0] <= iv[1] <= normalized[1]*unit)
            if not sign:
                witness = unit/10
                contained = iv[0] <= -witness < 0 < witness <= iv[1]
                check('raw_interval_straddles_zero_'+str(n),contained)
                zero_witnesses.append({'minor':n,'negative_inner_bound':str(-witness),
                                       'positive_inner_bound':str(witness),
                                       'contained_in_complete_raw_interval':contained})
        else:
            readable.append({'power_of_ten':0,'scaled_interval':base.interval_json(iv)})
        print('Delta_'+str(n)+': sign '+str(sign)+'; exact pi degree '+str(len(delta)-1),flush=True)
        print('  Actual enclosing bounds:',readable[-1],'; required: exclude zero',flush=True)
    # A separate literal Leibniz comparison checks the recursion at small size.
    for n in range(1,4):
        terms=[]
        for perm in permutations(range(n)):
            parity=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
            term=ONE
            for i,j in enumerate(perm):
                term=mul(term,bd[i][j])
            terms.append(scale(term,(-1)**parity))
        check('literal_Leibniz_comparison_'+str(n),add(*terms)==dets[n-1])
    failures = [k for k,v in checks.items() if not v]
    unresolved = [i+1 for i,s in enumerate(signs) if not s]
    complete = not failures and not unresolved
    seq = [1]+signs
    negative = sum(seq[i]!=seq[i+1] for i in range(6)) if complete else None
    inertia = {'positive':6-negative,'negative':negative,'zero':0} if complete else None
    result = ('CERTIFIED_N6_INDEX_AT_MOST_ONE' if negative<=1 else 'CERTIFIED_N6_INDEX_AT_LEAST_TWO') if complete else 'INCONCLUSIVE'
    report = {
        'target':'Full Kuznetsov T_6/S derivative Bezoutian in descending Pollaczek basis',
        'method':'Exact Q(sqrt(2))[pi]; Leibniz determinants grouped by column subsets; fixed rational Horner enclosures',
        'input_certificate':str(INPUT.name),'input_sha256':hashlib.sha256(raw).hexdigest(),
        'input_degree_proof':'C029n; top coefficient interval is strictly negative',
        'reproduction':'python3 scripts/pollaczek/tilted_bezoutian_n6_2014.py',
        'normalization':'U=T_6/S, S=sin(pi/8)/sqrt(2)>0; alpha=a6/S; Ctilde=alpha*C',
        'pi_interval':base.interval_json(pi_iv),'sqrt2_interval':base.interval_json(sqrt_iv),
        'u_over_S_polynomials':list(map(encode,u)),'beta_over_S_polynomials':list(map(encode,beta)),
        'weights':list(map(str,weights)),'a_over_S_polynomials':list(map(encode,a)),
        'top_coefficient_interval':base.interval_json(top_iv),
        'basis_p_0_to_6':[[str(x) for x in row] for row in p],
        'basis_V_ascending':[[str(x) for x in row] for row in v],
        'monomials_in_ascending_basis_R':[[str(x) for x in row] for row in r],
        'U_monomial_coefficients':list(map(encode,b)),'derivative_coefficients':list(map(encode,d)),
        'kernel_numerator':matrix_json(numerator),'B_monomial':matrix_json(bm),
        'B_descending':matrix_json(bd),'kernel_residual':matrix_json(residual),
        'Ctilde':matrix_json(ct),'comrade_residual':matrix_json(comrade_residual),
        'cleared_left_metric_residual':matrix_json(metric_residual),'D_squared':list(map(str,d2)),
        'scaled_metric_identity':'G=D*B_descending*D; A=D^-1*C*D; A^t*G-G*A=D*(C^t*B-B*C)*D=0',
        'leading_determinant_polynomials':list(map(encode,dets)),
        'leading_determinant_intervals':list(map(base.interval_json,intervals)),
        'readable_determinant_enclosures':readable,'leading_determinant_signs':signs,
        'zero_containment_witnesses':zero_witnesses,
        'required':'All six nonzero leading determinant signs; nonsingular negative index<=1',
        'actual_inertia':inertia,'unresolved_determinants':unresolved,
        'threshold_pass':negative<=1 if complete else None,
        'source_interpretation':'Heinig-Rost Example7.2/Prop7.15/Thm10.4; Jacobi in Coste p19',
        'checks':checks,'failures':failures,'result':result,
        'scope':'N=6 only; no eventual bound, compact convergence, actual-Xi sign or RH claim',
    }
    out = ROOT/'tilted-bezoutian-n6-2014.json'
    out.write_text(json.dumps(report,indent=2)+'\n')
    print('Result:',result,'; actual inertia:',inertia)
    print('Required:',report['required'])
    print('Signs:',signs,'; unresolved:',unresolved,'; failures:',failures)
    print('Certificate:',out.relative_to(Path.cwd()))
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
