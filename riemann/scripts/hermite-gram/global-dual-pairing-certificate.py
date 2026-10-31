#!/usr/bin/env python3
"""Rational enclosures of all three complete finite evaluation pairings.

No floating arithmetic enters the certificate. See L567 for remainder
and tail proofs. Full node, moment and signed-pairing evidence is saved.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import importlib.util
import json
import sys
import time

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('rational_rules', HERE / 'leading-block-boundary-certificate.py')
ar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ar)
ar.S = S = 1 << 2048
ar.ORDER = 320
M = 256
PANELS = 128
THETA = 24
OUT = HERE / 'global-dual-pairing-certificate.json'


def exp_point(x):
    x = F(x)
    if x <= -2048:
        return 0, 1  # e>2, with scale 2^2048
    if x < 0:
        # Reciprocal is taken before repeated squaring; no huge positive exp.
        y = -x
        squares = 0
        while y > 1:
            y /= 2
            squares += 1
        a, b = exp_point(y)
        value = (S*S//b, ar.ceildiv(S*S, a))
        for _ in range(squares):
            value = ar.mul(value, value)
        return value
    squares = 0
    while x > 1:
        x /= 2
        squares += 1
    z = ar.point(x)
    term = total = (S, S)
    for j in range(1, ar.ORDER + 1):
        term = ar.divide(ar.mul(term, z), j)
        total = ar.add(total, term)
    total = total[0], total[1] + ar.ceildiv(3*S, factorial(ar.ORDER+1))
    for _ in range(squares):
        total = ar.mul(total, total)
    return total


ar.exp_point = exp_point


def power(a, n):
    v = (S, S)
    while n:
        if n & 1:
            v = ar.mul(v, a)
        a = ar.mul(a, a)
        n //= 2
    return v


def weights():
    # P(t)=prod_(i=0)^M(t-i), stored in ascending powers.
    p = [1]
    for i in range(M+1):
        new = [0]*(len(p)+1)
        for k, a in enumerate(p):
            new[k] -= i*a
            new[k+1] += a
        p = new
    result = []
    for i in range(M+1):
        q = [0]*(M+1)
        q[M] = p[M+1]
        for k in range(M-1, -1, -1):
            q[k] = p[k+1]+i*q[k+1]
        assert p[0]+i*q[0] == 0
        integral = sum((F(a*M**(k+1), k+1) for k, a in enumerate(q)), F(0))
        denominator = (-1)**(M-i)*factorial(i)*factorial(M-i)*M
        result.append(integral/denominator)
    # All monomial moments of the unit-panel rule, not only normalization.
    for k in range(M+1):
        assert sum((w*F(i, M)**k for i,w in enumerate(result)), F(0)) == F(1,k+1)
    assert result == list(reversed(result))
    return result


def pair_add(a,b):
    return a[0]+b[0], a[1]+b[1]


def pair_scale(a,c):
    return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)


def pair_mul(a,b):
    v=[x*y for x in a for y in b]
    return min(v),max(v)


def encoded(a):
    return [str(x) for x in a]


def scientific_bound(x):
    # Exact signed decimal with six significant figures, rounded outward
    # is unnecessary here: label as a display only; rationals are decisive.
    if not x:
        return '0'
    sign = '-' if x<0 else ''
    x=abs(x)
    exponent=len(str(x.numerator))-len(str(x.denominator))
    if x < F(10)**exponent:
        exponent-=1
    digits=(x/F(10)**exponent*10**5).numerator//(x/F(10)**exponent*10**5).denominator
    return sign+str(digits/100000)+'e'+str(exponent)


def main():
    start=time.time()
    w=weights()
    a=ar.atan_bounds(F(1,5),512)
    b=ar.atan_bounds(F(1,239),150)
    pi_bounds=(16*a[0]-4*b[1],16*a[1]-4*b[0])
    pi=(ar.point(pi_bounds[0])[0],ar.point(pi_bounds[1])[1])
    pi2=ar.mul(pi,pi)
    integrals=[(0,0) for _ in range(257)]
    nodes=[]
    resume='--reuse-nodes' in sys.argv
    if resume:
        old=json.loads(OUT.read_text())
        assert old['parameters']==dict(bits=2048,exp_order=320,degree=256,panels=128,length='1/32',limit=4,theta_terms=24)
        assert old['weights']==[str(v) for v in w]
        nodes=old['node_base_fixedpoint']
        integrals=old['integral_totals_fixedpoint']
        assert len(nodes)==PANELS*M+1 and len(integrals)==257
    for index in ([] if resume else range(PANELS*M+1)):
        panel_i=index%M
        weight=w[panel_i]
        if panel_i==0 and index not in (0,PANELS*M):
            weight+=w[M]
        weight/=32
        u=F(index,32*M)
        ui=ar.point(u)
        ehalf=exp_point(u/2)
        e2=power(ehalf,4)
        e5=power(ehalf,5)
        e9=power(ehalf,9)
        q=ar.exp_interval(tuple(-v for v in reversed(ar.mul(pi,e2))))
        kernel=(0,0)
        for k in range(1,THETA+1):
            bracket=ar.sub(ar.scale(ar.mul(pi2,e9),2*k**4),ar.scale(ar.mul(pi,e5),3*k*k))
            bracket=(max(0,bracket[0]),bracket[1])
            kernel=ar.add(kernel,ar.scale(ar.mul(bracket,power(q,k*k)),2))
        base=ar.mul(exp_point(-u*u/4),kernel)
        nodes.append([base[0],base[1]])
        weighted=ar.mul(base,ar.point(weight))
        u2=ar.mul(ui,ui)
        moment=weighted
        for n in range(257):
            integrals[n]=ar.add(integrals[n],moment)
            moment=ar.mul(moment,u2)
        if index and index%(M*16)==0:
            print('enclosed nodes',index,'/',PANELS*M,flush=True)
    moments=[]
    remainders=[]
    absolute_weight_norm=sum(map(abs,w))
    for n, v in enumerate(integrals):
        interpolation=8*F(2)**60*F(9,2)**(2*n)*F(16)**(-257)
        # The rule has SIGNED weights. Its omitted-theta error has BOTH
        # signs and requires the absolute-weight norm, not an integral.
        theta=512*F(3)**18*F(2)**(-1849)*F(4)**(2*n)*absolute_weight_norm
        spatial=19200*F(3)**18*F(4)**(2*n)*F(2)**(-3072)
        full=(2*F(v[0],S)-interpolation-theta,2*F(v[1],S)+interpolation+theta+spatial)
        moments.append(full)
        remainders.append(dict(interpolation=str(interpolation),theta=str(theta),spatial=str(spatial)))
    coefficient_bounds=[pair_scale(v,F(1,2**(2*n)*factorial(2*n))) for n,v in enumerate(moments)]
    rows=[]
    coarse_intervals={64:(F(-2728,10**25),F(-2726,10**25)),128:(F(-8226,10**41),F(-8224,10**41)),256:(F(-2006,10**72),F(-2004,10**72))}
    for n,p in [(64,163),(128,271),(256,447)]:
        x=F(p,4)
        h=[F(1),2*x]
        for j in range(1,2*n):
            h.append(2*x*h[-1]-2*j*h[-2])
        sums=[(F(0),F(0)) for _ in range(3)]
        for k in range(n+1):
            j=2*k
            c=F((-1)**k,2**j*factorial(j))
            terms=[h[j],2*j*h[j-1] if j else F(0),4*j*(j-1)*h[j-2] if j else F(0)]
            for d in range(3):
                sums[d]=pair_add(sums[d],pair_scale(moments[k],c*terms[d]))
        p0,p1,p2=sums
        square=(F(0) if p1[0]<=0<=p1[1] else min(p1[0]**2,p1[1]**2),max(p1[0]**2,p1[1]**2))
        product=pair_mul(p0,p2)
        disc=(square[0]-product[1],square[1]-product[0])
        coarse=coarse_intervals[n]
        coarse_pass=coarse[0]<=disc[0]<=disc[1]<=coarse[1]
        rows.append(dict(N=n,x=str(x),P=encoded(p0),derivative=encoded(p1),second_derivative=encoded(p2),D=encoded(disc),negative_certified=disc[1]<0,coarse_D=encoded(coarse),coarse_contains_full_enclosure=coarse_pass,display_D=[scientific_bound(v) for v in disc]))
    failures=[f'N={r["N"]}: upper bound is not negative' for r in rows if not r['negative_certified']]
    failures += [f'N={r["N"]}: displayed coarse enclosure failed' for r in rows if not r['coarse_contains_full_enclosure']]
    certificate=dict(status='PASS' if not failures else 'INCONCLUSIVE',required='Complete D(P_N)(x) upper bound < 0',parameters=dict(bits=2048,exp_order=320,degree=256,panels=128,length='1/32',limit=4,theta_terms=24),pi_bounds=encoded(pi_bounds),weights=[str(v) for v in w],absolute_weight_norm=str(absolute_weight_norm),node_base_fixedpoint=nodes,panel_rule_moment_checks=257,integral_totals_fixedpoint=integrals,moments=[encoded(v) for v in moments],remainders=remainders,pairings=rows,failures=failures,certified_negative_pairings=sum(r['negative_certified'] for r in rows),scope='Three finite global obstructions only; no unbounded family, interval or Xi sign transfer.',elapsed_seconds=time.time()-start)
    certificate['coefficients_b_even']=[encoded(v) for v in coefficient_bounds]
    certificate['node_values_reused']=resume
    certificate['software']=sys.version
    OUT.write_text(json.dumps(certificate,indent=2)+'\n')
    print('status',certificate['status'],'certified',certificate['certified_negative_pairings'])
    for r in rows:
        print('N',r['N'],'D interval (display)',r['display_D'],'negative',r['negative_certified'])
        print('certified rational coarse bounds' if r['coarse_contains_full_enclosure'] else 'coarse bound FAILED',r['coarse_D'])
    print('required',certificate['required'],'failures',failures,'certificate',OUT)


if __name__=='__main__':
    main()
