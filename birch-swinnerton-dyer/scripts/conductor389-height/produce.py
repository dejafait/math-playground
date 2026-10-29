#!/usr/bin/env python3
"""Fixed E=[0,1,1,-2,0], p=5; exact-rational Kedlaya/MST/Harvey replay.

No external arithmetic package. Certificate contains every rational intermediate
needed by the finite reduction. Mathematical interpretation is in the step note;
the flags are implementation checks, not independent proof/audit assertions.
"""
from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path
import json
import sys

# Exact logarithm partial sums can exceed Python's display guard; no input is
# accepted from outside this fixed calculation.
sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'step-506'
P = 5
INF = 10**9


def vp(a):
    a = F(a)
    if not a:
        return INF
    def vint(n):
        n = abs(n)
        z = 0
        while n % P == 0:
            z += 1
            n //= P
        return z
    return vint(a.numerator) - vint(a.denominator)


def residue(a, n):
    a = F(a)
    assert vp(a) >= 0
    mod = P**n
    return a.numerator * pow(a.denominator, -1, mod) % mod


def trim(a):
    a = list(map(F, a))
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([v*c for v in a])


def mul(a, b):
    if not a or not b:
        return []
    c = [F(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def power(a, n):
    r = [F(1)]
    for _ in range(n):
        r = mul(r, a)
    return r


def divmod_poly(a, b):
    a, b = trim(a), trim(b)
    q = [F(0)] * max(0, len(a)-len(b)+1)
    while a and len(a) >= len(b):
        j, c = len(a)-len(b), a[-1]/b[-1]
        q[j] += c
        a = add(a, [F(0)]*j + scale(b, -c))
    return trim(q), a


def deriv(a):
    return trim([i*a[i] for i in range(1, len(a))])


def invmod(a, mod):
    r0, r1, t0, t1 = mod, a, [], [F(1)]
    while r1:
        q, r = divmod_poly(r0, r1)
        r0, r1 = r1, r
        t0, t1 = t1, add(t0, scale(mul(q, t1), -1))
    assert len(r0) == 1
    return divmod_poly(scale(t0, 1/r0[0]), mod)[1]


# X=x+1/3, Y=y+1/2. No differential scaling: dX/(2Y)=dx/(2y+1).
QPOLY = [F(107,108), F(-7,3), F(0), F(1)]
QD = deriv(QPOLY)
QI = invmod(QD, QPOLY)
assert divmod_poly(mul(QI, QD), QPOLY)[1] == [F(1)]
assert all(vp(c) >= 0 for c in QI)


def horizontal(a):
    steps = []
    a = trim(a)
    while len(a) > 2:
        d = len(a)-1
        r = d-2
        # d(x^r Y)=(r*x^(r-1)*Q + x^r*Q'/2) dx/Y.
        relation = add([F(0)]*(r-1) + scale(QPOLY, r) if r else [],
                       [F(0)]*r + scale(QD, F(1,2)))
        c = a[-1]/relation[-1]
        before = a
        a = add(a, scale(relation, -c))
        steps.append({'degree':d, 'primitive_coefficient':c,
                      'before':before, 'after':a})
    return a + [F(0)]*(2-len(a)), steps


def vertical(a, m):
    stages = []
    while m > 0:
        b = divmod_poly(mul(a, QI), QPOLY)[1]
        c, rem = divmod_poly(add(a, scale(mul(b, QD), -1)), QPOLY)
        assert not rem
        nxt = add(c, scale(deriv(b), F(2, 2*m-1)))
        stages.append({'m':m, 'A':a, 'B':b, 'C':c, 'next':nxt})
        a = nxt
        m -= 1
    return a, stages


def frobenius():
    qx5 = [F(0)]*16
    for k, v in enumerate(QPOLY):
        qx5[5*k] = v
    delta = add(qx5, scale(power(QPOLY, 5), -1))
    assert min(map(vp, delta)) >= 1
    delta_power, binom = [F(1)], F(1)
    cols = [[F(0), F(0)] for _ in range(2)]
    terms = []
    for j in range(8):
        for i in range(2):
            numerator = [F(0)]*(5*(i+1)-1) + scale(delta_power, 5*binom)
            parts = []
            rem = numerator
            qpower = 0
            total = []
            while rem:
                rem, a = divmod_poly(rem, QPOLY)
                m = 5*j+2-qpower
                original = a
                if m < 0:
                    a = mul(a, power(QPOLY, -m))
                    stages = []
                else:
                    a, stages = vertical(a, m)
                total = add(total, a)
                parts.append({'Q_power':qpower, 'm':m, 'A':original,
                              'vertical':stages, 'reduced':a})
                qpower += 1
            reduced, hsteps = horizontal(total)
            cols[i] = add(cols[i], reduced)
            cols[i] += [F(0)]*(2-len(cols[i]))
            terms.append({'j':j, 'basis_index':i, 'binomial':binom,
                          'numerator':numerator, 'parts':parts,
                          'horizontal':hsteps, 'reduced':reduced})
        delta_power = mul(delta_power, delta)
        binom *= F(-1,2)-j
        binom /= j+1
    fexact = [[cols[c][r] for c in range(2)] for r in range(2)]
    fmod = [[residue(x, 7) for x in row] for row in fexact]
    mod = 5**7
    assert (fmod[0][0]+fmod[1][1]+3) % mod == 0
    assert (fmod[0][0]*fmod[1][1]-fmod[0][1]*fmod[1][0]-5) % mod == 0
    assert fmod[0][0] % 5 == fmod[1][0] % 5 == 0
    def mm(a,b):
        return [[sum(a[r][k]*b[k][c] for k in range(2)) % mod
                 for c in range(2)] for r in range(2)]
    fpow = [[1,0],[0,1]]
    for _ in range(6):
        fpow = mm(fpow, fmod)
    b,d = fpow[0][1],fpow[1][1]
    assert d % 5
    e2 = (-12*b*pow(d,-1,5**6)) % 5**6
    return e2, {'short_Q':QPOLY, 'Qprime_inverse':QI, 'delta':delta,
                'terms':terms, 'F_exact_truncation':fexact,
                'F_mod_5^7':fmod, 'F_power_6_mod_5^7':fpow,
                'E2_mod_5^6':e2,
                'tail':{'first_omitted_j':8,'absolute_F_exponent':7,
                        'bound':'j+1-floor(log_5(10*j+5)) >= 7 for all j>=8'}}


def oncurve(a):
    if a is None:
        return True
    x,y = a
    return y*y+y == x*x*x+x*x-2*x


def pointadd(a,b):
    if a is None:
        return b
    if b is None:
        return a
    x,y = a
    u,v = b
    if x == u and y+v+1 == 0:
        return None
    if x == u:
        lam = (3*x*x+2*x-2)/(2*y+1)
    else:
        lam = (v-y)/(u-x)
    nu = y-lam*x
    z = lam*lam-1-x-u
    w = -(lam*z+nu)-1
    out = z,w
    assert oncurve(out)
    return out


def pointmul(a,n):
    r = None
    chain = []
    for k in range(1,n+1):
        r = pointadd(r,a)
        chain.append({'multiple':k, 'point':r})
    return r,chain


# Exact centers + absolute exponents; INF denotes exact rational data.
def ball(c,n=INF):
    return F(c),n


def badd(a,b):
    return a[0]+b[0], min(a[1],b[1])


def bscale(a,c):
    c = F(c)
    return a[0]*c, min(INF,a[1]+vp(c))


def bmul(a,b):
    return (a[0]*b[0], min(INF,a[1]+vp(b[0]),b[1]+vp(a[0]),a[1]+b[1]))


def seriesmul(a,b,n):
    return (mul(a,b)+[F(0)]*n)[:n]


def seriesinv(a,n):
    out = [1/a[0]]
    for k in range(1,n):
        out.append(-sum(a[j]*out[k-j] for j in range(1,min(k+1,len(a))))/a[0])
    return out


def sigma(e2):
    length = 12
    w = [F(0)]*length
    w[3] = F(1)
    for k in range(4,length):
        w[k] = w[k-2] + sum(w[i]*w[k-i] for i in range(k+1)) - \
            2*sum(w[i]*w[k-1-i] for i in range(k))
    # w=t^3*u, x=t^-2/u, y=-t^-3/u.
    u = w[3:]
    xin = seriesinv(u,9)
    # x'/(2y+1) = (2*xin-t*xin') / (2*xin-t^3).
    top = [(2-k)*xin[k] for k in range(len(xin))]
    den = scale(xin,2)
    den[3] -= 1
    omega = seriesmul(top,seriesinv(den,8),8)
    c = ball(F(4-e2,12),6)
    # Laurent product (x+c)*omega, exponents -2,...,4.
    xomega = {}
    for k in range(-2,5):
        v = sum(xin[j]*omega[k+2-j]
                for j in range(k+3) if 0<=j<len(xin) and 0<=k+2-j<len(omega))
        xomega[k] = ball(v)
        if k>=0:
            xomega[k] = badd(xomega[k],bscale(c,omega[k]))
    assert xomega[-2] == ball(1) and xomega[-1][0] == 0
    integ = {k+1:bscale(v,F(1,k+1)) for k,v in xomega.items() if k != -1}
    h = []
    for k in range(5):
        v = ball(0)
        for j,a in integ.items():
            if 0 <= k-j < len(omega):
                v = badd(v,bscale(a,-omega[k-j]))
        h.append(v)
    assert h[0][0] == 0  # a1/2
    theta = [ball(1)]
    for k in range(1,6):
        val = ball(0)
        for j in range(k):
            val = badd(val,bmul(h[j],theta[k-1-j]))
        theta.append(bscale(val,F(1,k)))
    profile = []
    for k,z in enumerate(theta):
        # sigma coefficient t^(k+1) must be known mod 5^(6-k).
        need = 6-k
        assert vp(z[0]) >= 0 and z[1]>=need
        profile.append({'sigma_degree':k+1,'center':z[0],
                        'absolute_exponent':z[1], 'required':need})
    return theta, {'w':w,'t_squared_x':xin,'omega':omega,
                   'c':c,'xomega':xomega,'h':h,'theta_balls':theta,
                   'sigma_profile':profile,'sigma_tail_degree':7,
                   'imported_sigma_integrality':True}


def pointheight(r,theta):
    a,chain = pointmul(r,9)
    assert a is not None
    x,y = a
    d = isqrt(x.denominator)
    assert d*d == x.denominator
    alpha,beta = x*d*d,y*d*d*d
    assert alpha.denominator == beta.denominator == 1
    assert gcd(int(alpha),d) == gcd(int(beta),d) == 1
    t = -x/y
    assert vp(t)>=1 and vp(-alpha/beta)==0
    # theta(t)=sigma(t)/t: omitted integral coefficients start at t^6.
    value = ball(0)
    for k,z in enumerate(theta):
        value = badd(value,bscale(z,t**k))
    value = value[0],min(value[1],6*vp(t))
    unit = bscale(value,-alpha/beta)
    assert vp(unit[0]) == 0 and unit[1]>=6
    # Iwasawa log(u) = log(u^4)/4. Its tail terms k>=8 have
    # valuation >=k-v5(k)>=6; the finite terms k=1,...,7 are exact.
    z = unit[0]**4-1
    assert vp(z)>=1
    partial = sum((-1)**(k+1)*z**k/k for k in range(1,8))/4
    height = 2*partial/81
    return residue(height,6), {'point':r,'multiplication_chain':chain,
             'multiple_9':a,'alpha':alpha,'beta':beta,'d':d,'t':t,
             'v_t':vp(t),'theta_value':value,'sigma_over_d_unit':unit,
             'log_power_minus_one':z,'log_partial':partial,
             'log_tail_first_k':8,'log_tail_exponent_lower_bound':6,
             'q_H_center_mod_5^6':residue(height,6),'absolute_exponent':6}


def encode(a):
    if isinstance(a,F):
        return str(a)
    if isinstance(a,dict):
        return {str(k):encode(v) for k,v in a.items()}
    if isinstance(a,(list,tuple)):
        return [encode(v) for v in a]
    return a


def main():
    OUT.mkdir(exist_ok=True)
    cert = {'status':'INCOMPLETE','curve':[0,1,1,-2,0], 'p':5,
            'output_absolute_exponent':6,'n1':9,'n2':1,'n':9,
            'method':'Kedlaya exact binomial reduction; MST E2; Harvey sigma/log'}
    path = OUT/'certificate.json'
    def save():
        path.write_text(json.dumps(encode(cert),indent=2)+'\n')
    save()
    points = {'P':(F(0),F(0)), 'Q':(F(1),F(0))}
    points['P+Q'] = pointadd(points['P'],points['Q'])
    assert points['P+Q'] == (F(-2),F(-1))
    assert all(oncurve(r) for r in points.values())
    cert['points'] = points
    e2,frob = frobenius()
    cert['frobenius'] = frob
    save()
    theta,sig = sigma(e2)
    cert['sigma'] = sig
    save()
    heights,details = {},{}
    for label,r in points.items():
        heights[label],details[label] = pointheight(r,theta)
        cert['height_details'] = details
        save()
    h00,h11 = -heights['P'],-heights['Q']
    h01 = -F(heights['P+Q']-heights['P']-heights['Q'],2)
    det = h00*h11-h01*h01
    cert['L119'] = {'height_centers':heights,'H_hat':[[h00,h01],[h01,h11]],
                    'a':0,'N':6,'B0':6,'D0':det,'v_D0':vp(det),
                    'strict_test_pass':vp(det)<6,'b':2,'t':0,'k':2}
    cert['status'] = 'FINITE_PRODUCTION_COMPLETE_UNAUDITED'
    save()
    print(json.dumps({'status':cert['status'],'E2_mod_5^6':e2,
          'q_H_mod_5^6':heights,'det_valuation':vp(det),'required_strict_bound':6,
          'strict_test_pass':vp(det)<6,'certificate':str(path.relative_to(ROOT)),
          'failures':[]},indent=2))


if __name__ == '__main__':
    main()
