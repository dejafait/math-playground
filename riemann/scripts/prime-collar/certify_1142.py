#!/usr/bin/env python3
"""One prescribed pair, MPFR outward Simpson bounds plus full positive tail."""
import importlib.util
import json
import math
import hashlib
from pathlib import Path

backend = Path(__file__).resolve().parents[1] / 'pivot-area' / 'certify_1136.py'
spec = importlib.util.spec_from_file_location('local_mpfr_backend', backend)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
I, Real, op = m.I, m.Real, m.op
pi = I(Real(), Real())
m.lib.mpfr_const_pi(m.ct.byref(pi.lo.raw), m.DOWN)
m.lib.mpfr_const_pi(m.ct.byref(pi.hi.raw), m.UP)
a = I(9)/4
b = I(101).unary('log')/2
r = a/b*I(97).unary('log')
w = 2*a-r
c = a-w/2
h = I(1)/32
T = 4096

# Exhaustive integer prime-power list; activation is log(n)<2 radius.
powers = []
for p in range(2,102):
    if all(p%d for d in range(2,math.isqrt(p)+1)):
        n=p
        while n<=101:
            powers.append(n)
            n*=p
powers.sort()
old = [n for n in powers if (2*a-I(n).unary('log')).positive()]
new = [n for n in powers if (I(101).unary('log')-I(n).unary('log')).positive()]

# Nonnegative square enclosure without dependency inflation across zero.
def sq(x):
    y=x.abs()
    return I(op('mul',y.lo,y.lo),op('mul',y.hi,y.hi,m.UP))

def density(k):
    if k==0:
        return I(2).unary('log')*4*sq(w)/pi
    t=I(k)/32
    return 16/pi*(2+t).unary('log')*sq((w*t/2).trig('sin'))*sq((c*t).trig('cos'))/sq(t)

# Retain exact partition and outward weighted sums for all 32 blocks.
blocks=[]
sums=[I(0),I(0)]
for left,right,part in [(0,32,0),(32,T*32,1)]:
    acc=I(0)
    count=right-left
    for k in range(left,right+1):
        coeff=1 if k in (left,right) else 4 if (k-left)%2 else 2
        acc=acc+coeff*density(k)
        if (k-left)%4096==0 or k==right:
            blocks.append({'part':part,'through_grid_index':k,'cumulative_weighted_sum':acc.dump()})
    sums[part]=acc*h/3
    print('Completed finite quadrature part',part,flush=True)

# Low interval: |(|F|²)^(j)| <= 4w²(2a)^j from the double integral.
low_M=4*sq(w)/pi*sum(math.comb(4,p)*(I(3).unary('log') if p==0 else I(math.factorial(p-1))/2**p)*(2*a)**(4-p) for p in range(5))
low_error=h**4/180*low_M
# High interval: A=log(2+t)/t²; positive decreasing derivative majorants D_n.
# integral_1^infty D_n <= (n+1)!*(3/2)log3
#                          +sum_{p=1}^n binom(n,p)(p-1)!(n-p+1)!/(n+1).
int_M=I(0)
at1_M=I(0)
for n in range(5):
    bound=math.factorial(n+1)*I(3)/2*I(3).unary('log')
    at1=math.factorial(n+1)*I(3).unary('log')
    for p in range(1,n+1):
        coeff=math.comb(n,p)*math.factorial(p-1)*math.factorial(n-p+1)
        bound=bound+I(coeff)/(n+1)
        at1=at1+I(coeff)/3**p
    factor=math.comb(4,n)*(2*a)**(4-n)*16/pi
    int_M=int_M+factor*bound
    at1_M=at1_M+factor*at1
high_error=h**4/180*(int_M+2*h*at1_M)
error=low_error+high_error
finite=sums[0]+sums[1]
finite_enclosure=finite+I(op('neg',error.hi),error.hi)
tail=16/pi*((2+I(T)).unary('log')/T+(1+I(2)/T).unary('log')/2)
J=I(finite_enclosure.lo,op('add',finite_enclosure.hi,tail.hi,m.UP))
numerator=2*I(97).unary('log')/I(97).unary('sqrt')*w
ratio=numerator/J
claims={
 'pulse_width_positive':w.positive(),
 'pulse_width_lt_a':(a-w).positive(),
 'separation_gt_width':(r-w).positive(),
 'old_34_terms':len(old)==34,
 'new_35_terms':len(new)==35,
 'only_new_97':sorted(set(new)-set(old))==[97],
 '101_endpoint_excluded':101 not in new,
 'J_gt_293_over_1000':(J-I(293)/1000).positive(),
 'J_lt_307_over_1000':(I(307)/1000-J).positive(),
 'ratio_gt_119_over_1000':(ratio-I(119)/1000).positive(),
 'ratio_lt_one_eighth':(I(1)/8-ratio).positive(),
}
failures=[key for key,val in claims.items() if not val]
out={'scope':'Only prescribed endpoint pulses; passing sample leaves uniform complex inequality open.',
 'mpfr_version':m.lib.mpfr_get_version().decode(),'precision_bits':m.PREC,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'backend_path':str(backend.relative_to(Path(__file__).resolve().parents[2])),
 'backend_sha256':hashlib.sha256(backend.read_bytes()).hexdigest(),
 'a':a.dump(),'b':b.dump(),'r':r.dump(),'w':w.dump(),'c':c.dump(),
 'old_prime_powers':old,'new_prime_powers':new,
 'grid':{'h':'1/32','T':T,'low_panels':16,'high_panels':65520},
 'quadrature_blocks':blocks,'simpson_low':sums[0].dump(),'simpson_high':sums[1].dump(),
 'fourth_derivative_integral_majorant':int_M.dump(),
 'fourth_derivative_majorant_at_one':at1_M.dump(),
 'low_error':low_error.dump(),'high_error':high_error.dump(),
 'finite_integral_enclosure':finite_enclosure.dump(),'positive_tail_upper':tail.dump(),
 'J':J.dump(),'numerator':numerator.dump(),'ratio':ratio.dump(),
 'claims':claims,'failures':failures}
path=Path(__file__).with_name('certificate-1142.json')
path.write_text(json.dumps(out,indent=2)+'\n')
for key in ['w','low_error','high_error','finite_integral_enclosure','positive_tail_upper','J','numerator','ratio']:
 print(key, [float(x) for x in out[key]])
print('Required ratio <= 0.125; passing sample only. Failures:',failures)
print('Full certificate:',path)
if failures: raise SystemExit(1)
