#!/usr/bin/env python3
"""Step138 approved independent replay; standard-library exact dyadic intervals.
See L960, step140 specialization. No float is accepted as mathematical input.
"""
import argparse
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt
import json
from pathlib import Path
import time

BITS = 256
Q = 1 << BITS

def ceildiv(n, d):
    if d <= 0:
        raise ArithmeticError('nonpositive integer divisor')
    return -((-n)//d)

class IV:
    __slots__ = ('l', 'h')
    def __init__(self, x=0):
        if isinstance(x, IV):
            self.l, self.h = x.l, x.h
            return
        if not isinstance(x, (int, F)):
            raise TypeError('exact integer or Fraction required')
        x = F(x)
        self.l, self.h = x.numerator*Q//x.denominator, ceildiv(x.numerator*Q, x.denominator)
    @classmethod
    def raw(cls, l, h):
        if l > h:
            raise ArithmeticError('reversed interval')
        o = cls.__new__(cls)
        o.l, o.h = l, h
        return o
    def __add__(self, b):
        b = IV(b)
        return IV.raw(self.l+b.l, self.h+b.h)
    __radd__ = __add__
    def __neg__(self):
        return IV.raw(-self.h, -self.l)
    def __sub__(self, b): return self+-IV(b)
    def __rsub__(self, b): return IV(b)+-self
    def __mul__(self, b):
        b = IV(b)
        p = (self.l*b.l, self.l*b.h, self.h*b.l, self.h*b.h)
        return IV.raw(min(p)//Q, ceildiv(max(p), Q))
    __rmul__ = __mul__
    def reciprocal(self):
        if self.l <= 0 <= self.h:
            raise ArithmeticError('zero in divisor')
        # Fraction avoids sign-sensitive integer division of negative endpoints.
        lo, hi = F(Q, self.h), F(Q, self.l)
        return IV.raw(IV(lo).l, IV(hi).h)
    def __truediv__(self, b): return self*IV(b).reciprocal()
    def __rtruediv__(self, b): return IV(b)*self.reciprocal()
    def __pow__(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError('nonnegative integer powers only')
        v, z = IV(1), self
        while n:
            if n & 1: v = v*z
            n //= 2
            if n: z = z*z
        return v
    def abs_upper(self): return IV.raw(max(abs(self.l), abs(self.h)), max(abs(self.l), abs(self.h)))
    def enc(self): return {'lo':str(self.l), 'hi':str(self.h), 'denominator_power_two':BITS}

@lru_cache(None)
def log_unit(x):
    # 1<=x<=2; z in [0,1/3]. DLMF4.6.4, first100 odd terms.
    x = F(x)
    if not 1 <= x <= 2: raise ValueError('log unit range')
    z = IV((x-1)/(x+1))
    zz, term, s = z*z, z, IV(0)
    for j in range(100):
        s += term/(2*j+1)
        term *= zz
    remainder = 2*term/(201*(1-zz))
    return IV.raw((2*s).l, (2*s+remainder).h)

@lru_cache(None)
def log_point(x):
    x = F(x)
    if x <= 0: raise ValueError('nonpositive logarithm')
    m, k = x, 0
    while m >= 2: m /= 2; k += 1
    while m < 1: m *= 2; k -= 1
    return log_unit(m)+k*log_unit(F(2))

def log_iv(x):
    x = IV(x)
    return IV.raw(log_point(F(x.l,Q)).l, log_point(F(x.h,Q)).h)

def exp_point(x):
    x = F(x)
    if x < 0: return exp_point(-x).reciprocal()
    r = 0
    while x > F(1,8): x /= 2; r += 1
    t, term, s = IV(x), IV(1), IV(1)
    for j in range(1,80):
        term = term*t/j
        s += term
    term = term*t/80
    rem = term/(1-t/81)
    y = IV.raw(s.l, (s+rem).h)
    if y.l <= 0: raise ArithmeticError('exp positivity')
    for _ in range(r): y = y*y
    return y

def exp_iv(x):
    x = IV(x)
    return IV.raw(exp_point(F(x.l,Q)).l, exp_point(F(x.h,Q)).h)

def sqrt_iv(x):
    x = IV(x)
    if x.l < 0: raise ValueError('negative square root')
    lo, hi = isqrt(x.l*Q), isqrt(x.h*Q)
    hi += int(hi*hi < x.h*Q)
    return IV.raw(lo, hi)

def pi_iv():
    def atan(x, m):
        s = sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(m)), F(0))
        nxt = (-1)**m*x**(2*m+1)/F(2*m+1)
        return IV.raw(IV(min(s,s+nxt)).l, IV(max(s,s+nxt)).h)
    return 16*atan(F(1,5),120)-4*atan(F(1,239),40)

def integrate(lo, hi, kappa, a, B, m):
    if m < 2 or m % 2: raise ValueError('even Simpson mesh required')
    width = hi-lo
    if width.l <= 0: raise ArithmeticError('integral endpoint ordering')
    h = width/m
    q = lambda u: a*u*u/4-B*u
    # E_i=exp(q(lo+i*h)), r_i=E_(i+1)/E_i; r_(i+1)/r_i=exp(a*h^2/2).
    e = exp_iv(q(lo))
    ratio = exp_iv((a*lo/2-B)*h+a*h*h/4)
    ratio_step = exp_iv(a*h*h/2)
    si, st = IV(0), IV(0)
    for i in range(m+1):
        u = lo+i*h
        weight = 1 if i in (0,m) else (4 if i % 2 else 2)
        si += weight*e
        st += weight*(u-kappa)*e
        if i < m:
            e *= ratio
            ratio *= ratio_step
    approx_i, approx_t = width*si/(3*m), width*st/(3*m)
    domain = IV.raw(lo.l, hi.h)
    R = (a*domain/2-B).abs_upper()
    D = a/2
    M = (domain-kappa).abs_upper()
    # q convex: maximum on the two exact endpoints. Interval endpoint
    # evaluations cover all admissible uncertain endpoints/parameters.
    em = IV.raw(0,max(exp_iv(q(lo)).h,exp_iv(q(hi)).h))
    i4 = em*(R**4+6*D*R**2+3*D**2)
    t4 = em*(M*(R**4+6*D*R**2+3*D**2)+4*(R**3+3*D*R))
    err_i, err_t = width**5*i4/(180*m**4), width**5*t4/(180*m**4)
    I = IV.raw(approx_i.l-err_i.h, approx_i.h+err_i.h)
    tail = IV.raw(approx_t.l-err_t.h, approx_t.h+err_t.h)
    return I, tail, {'mesh':m, 'width':width.enc(), 'h':h.enc(),
        'r_abs_upper':R.enc(), 'u_minus_kappa_abs_upper':M.enc(),
        'exp_upper':em.enc(), 'I_fourth_derivative_bound':i4.enc(),
        'tail_fourth_derivative_bound':t4.enc(), 'I_simpson':approx_i.enc(),
        'tail_simpson':approx_t.enc(), 'I_error':err_i.enc(), 'tail_error':err_t.enc(),
        'last_E_recurrence':e.enc(), 'last_E_direct':exp_iv(q(hi)).enc()}

def self_checks():
    # Exact enclosure properties (including signed divisions and rounding),
    # independent special values, and endpoint/recurrence overlap.
    checks = {}
    for a in [F(-7,3),F(-1,Q*3),F(0),F(1,7),F(9,2)]:
        for b in [F(-5,7),F(2,3)]:
            for name, val, iv in [('add',a+b,IV(a)+IV(b)), ('mul',a*b,IV(a)*IV(b)), ('div',a/b,IV(a)/IV(b))]:
                checks[f'{name}_{a}_{b}'] = F(iv.l,Q) <= val <= F(iv.h,Q)
    checks['log1_exact'] = log_point(F(1)).l == log_point(F(1)).h == 0
    checks['exp0_exact'] = exp_point(F(0)).l == exp_point(F(0)).h == Q
    p = sqrt_iv(IV(F(2)))
    checks['sqrt2_squares'] = p.l*p.l <= 2*Q*Q <= p.h*p.h
    p = pi_iv()
    checks['pi_333_106_355_113'] = IV(F(333,106)).h < p.l < p.h < IV(F(355,113)).l
    return checks

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('rational-replay-140.json'))
    ap.add_argument('--mesh',type=int,default=4096)
    ap.add_argument('--seconds',type=int,default=55)
    args = ap.parse_args()
    if not 1 <= args.seconds <= 60: raise ValueError('bounded run <=60 seconds')
    if args.mesh != 4096: raise ValueError('initial approved mesh4096')
    start = time.monotonic()
    X,W,C,H,K = 6000000185827,120000000000000,690988,3100000,128
    ends=[C]
    while ends[-1]<H: ends.append(min(H,101*ends[-1]//100))
    global_names=['positive_heat_band','finite_natural_index_upper_wall','finite_natural_index_lower_wall','prefix_above_centre','centre_log_between_3_and_7_2','cover_starts_at_C','cover_ends_at_H','cover_strictly_increasing']
    leaf_names=['position_not_left_of_X','all_coefficient_heat_exponents_nonpositive','convex_derivative_at_prefix_negative','convex_derivative_at_upper_negative','tail_integrals_positive','complete_centred_moment_below_81_4']
    gates={s:None for s in global_names}
    for j in range(1,len(ends)):
        gates.update({f'leaf_{j:03d}_{s}':None for s in leaf_names})
    out={'status':'INCOMPLETE','method':'independent rational Simpson reconstruction',
         'bits':BITS,'domain':{'a':'98/625','T':'1/5','X':X,'W':W},
         'required_cap':'81/4','required_gate_count':914,'closed_index_endpoints':ends,
         'required_leaf_count':151,'gates':gates,'failures':[],'leaves':[],
         'maximum_upper_endpoint':None,'actual_uniform_bound':None,
         'self_checks':self_checks(),'series':{'log_terms':100,'exp_terms':80,'atan5_terms':120,'atan239_terms':40}}
    def gate(name, margin):
        if isinstance(margin, bool): result=margin; ev={'exact':margin}
        else:
            result=True if margin.l>0 else False if margin.h<=0 else 'INCONCLUSIVE'
            ev={'positive_margin':margin.enc()}
        gates[name]=result
        if result is not True: out['failures'].append({'gate':name,'result':result,'evidence':ev})
        return ev
    def save():
        out['gate_counts']={'passed':sum(v is True for v in gates.values()),'failed':sum(v is False for v in gates.values()),'inconclusive':sum(v=='INCONCLUSIVE' for v in gates.values()),'unexecuted':sum(v is None for v in gates.values()),'required':914}
        out['elapsed_seconds']=time.monotonic()-start
        args.output.write_text(json.dumps(out,indent=2)+'\n')
    save()
    try:
        if not all(out['self_checks'].values()): raise ArithmeticError('self-check failed')
        a,T=IV(F(98,625)),IV(F(1,5))
        pi=pi_iv(); kappa=log_point(F(32)); low=log_point(F(K)); cap=IV(F(81,4))
        out['constants']={'pi':pi.enc(),'kappa':kappa.enc(),'logK':low.enc()}
        ge={}
        ge['positive_heat_band']=gate('positive_heat_band',F(0)<F(98,625)<F(1,5)<F(1,2))
        ge['finite_natural_index_upper_wall']=gate('finite_natural_index_upper_wall',IV(H+1)**2-W/(4*pi)-T/16)
        ge['finite_natural_index_lower_wall']=gate('finite_natural_index_lower_wall',X/(4*pi)+a/16-C*C)
        ge['prefix_above_centre']=gate('prefix_above_centre',K>32)
        # two separate strict margins must both pass.
        centre=IV.raw(min((kappa-3).l,(IV(F(7,2))-kappa).l),min((kappa-3).h,(IV(F(7,2))-kappa).h))
        ge['centre_log_between_3_and_7_2']=gate('centre_log_between_3_and_7_2',centre)
        for name,test in [('cover_starts_at_C',ends[0]==C),('cover_ends_at_H',ends[-1]==H),('cover_strictly_increasing',all(l<u for l,u in zip(ends,ends[1:])) )]: ge[name]=gate(name,test)
        out['global_evidence']=ge
        out['exact_cover_checks']={'151_leaves':len(ends)-1==151,'914_gates':len(gates)==914,'adjacent_closed_cover':ends[0]==C and ends[-1]==H and all(l<u for l,u in zip(ends,ends[1:]))}
        logs={n:log_point(F(n)) for n in range(1,K+1)}
        max_hi=None
        for j,(L,U) in enumerate(zip(ends,ends[1:]),1):
            xl=IV(X) if j==1 else 4*pi*(IV(L)**2-T/16)
            c=log_iv(sqrt_iv(1+xl*xl)/(4*pi))/4-1/(2*(1+xl*xl))
            sigma=IV(F(1,2))+a*c; B=sigma-1; high=log_point(F(U))
            g=lambda u:1+(u-kappa)*(a*u/2-sigma)
            prefix=IV(0)
            for n in range(1,K+1):
                # exact n=32, complete n=1, both absolute-log cases.
                d=IV(0) if n==32 else (kappa-logs[n] if n<32 else logs[n]-kappa)
                if n!=32 and d.l<=0: raise ArithmeticError('absolute log sign')
                prefix+=d*exp_iv(a*logs[n]*logs[n]/4-sigma*logs[n])
            I,tail,qe=integrate(low,high,kappa,a,B,args.mesh)
            bound=prefix+tail
            vals=[xl-X,4*c-high,-g(low),-g(high),IV.raw(min(I.l,tail.l),min(I.h,tail.h)),cap-bound]
            evidence={}
            for name,v in zip(leaf_names,vals):
                # First leaf x_L=X is an allowed equality, not a strict gate.
                if name=='position_not_left_of_X' and j==1:
                    evidence[name]=gate(f'leaf_{j:03d}_{name}',xl.l==xl.h==X*Q)
                else: evidence[name]=gate(f'leaf_{j:03d}_{name}',v)
            re, de=qe['last_E_recurrence'],qe['last_E_direct']
            overlap=max(int(re['lo']),int(de['lo']))<=min(int(re['hi']),int(de['hi']))
            if not overlap: raise ArithmeticError('E recurrence endpoint disjoint')
            out['leaves'].append({'index':j,'left':L,'right':U,'x_left':xl.enc(),'c_left':c.enc(),'sigma':sigma.enc(),'B':B.enc(),'logU':high.enc(),'g_low':g(low).enc(),'g_high':g(high).enc(),'prefix':prefix.enc(),'I':I.enc(),'tail':tail.enc(),'bound':bound.enc(),'quadrature':qe,'gate_evidence':evidence,'endpoint_recurrence_overlap':overlap})
            max_hi=bound.h if max_hi is None else max(max_hi,bound.h)
            out['maximum_completed_leaf_upper_endpoint']={'numerator':str(max_hi),'denominator_power_two':BITS}
            save()
            if out['failures']:
                out['stop_reason']='definite or inconclusive original gate; no further leaves'; break
            if time.monotonic()-start>args.seconds:
                out['stop_reason']='bounded execution slice exhausted'; break
        if len(out['leaves'])==151 and not out['failures'] and all(v is True for v in gates.values()) and all(out['exact_cover_checks'].values()) and max_hi<cap.l:
            out['status']='PASS'; out['maximum_upper_endpoint']=out['maximum_completed_leaf_upper_endpoint'];out['actual_uniform_bound']=out['maximum_upper_endpoint']
    except Exception as e:
        out['failures'].append({'exception':type(e).__name__,'message':str(e)})
    save()
    print(out['status'],out['gate_counts'],'completed leaves',len(out['leaves']),'/151')
    print('Actual uniform bound:',out['actual_uniform_bound'],'required <81/4')
    print('Failures:',out['failures'],'stop:',out.get('stop_reason'))
    print('Certificate:',args.output,'elapsed seconds',round(out['elapsed_seconds'],3))
    return 0 if out['status']=='PASS' else 1

if __name__=='__main__': raise SystemExit(main())
