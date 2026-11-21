#!/usr/bin/env python3
"""Directed-Decimal certificate for a signed middle-diagonal comparison stop.

The free coefficients are exact dyadics; low coefficients impose both
exponential moments exactly. No eigensolver, float, or finite inverse is
used for verification. The full actual form is also enclosed, distinctly.
"""
import importlib.util
import json
import math
from decimal import Decimal
from pathlib import Path

BASE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('interval545', BASE/'complete-schur-531.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
I = mod.I
N, J = 16, 1024


def power(x, n):
    result = I(1)
    for _ in range(n):
        result *= x
    return result


def ab(x):
    return max(x.lo.copy_abs(), x.hi.copy_abs())


def square(x):
    if x.lo <= 0 <= x.hi:
        return I(0, mod.UP.multiply(ab(x), ab(x)))
    return x*x


def inflate(x, error):
    return x+I(error.hi.copy_negate(), error.hi)


def dot(x, y):
    return sum((a*b for a,b in zip(x,y)), I(0))


def norm2(x):
    return sum((square(a) for a in x), I(0))


def atan_reciprocal(q):
    x = I(1)/q
    total = I(0)
    for j in range(80):
        total += ((-1)**j)*power(x, 2*j+1)/(2*j+1)
    return inflate(total, power(x, 161)/161)


pi = 16*atan_reciprocal(5)-4*atan_reciprocal(239)
ell = I(3).ln()/2
fourth = I(3).sqrt().sqrt()
k = [n*pi/ell for n in range(N)]
k2 = [square(x) for x in k]
norm = [(I(1 if n==0 else 2)/ell).sqrt() for n in range(N)]
alpha = [I(2).sqrt()*x for x in norm]
eta = [(-1)**n for n in range(N)]


def sincos(x):
    # The integer is only a reduction choice; its certified radius is checked.
    mid = mod.NEAR.divide(mod.NEAR.add(x.lo,x.hi),Decimal(2))
    q = int(mod.NEAR.divide(mid,mod.NEAR.divide(pi.lo,Decimal(2))).to_integral_value())
    r = x-q*pi/2
    assert ab(r) < Decimal('.786')
    sn, cs = I(0), I(0)
    for j in range(16):
        sn += ((-1)**j)*power(r,2*j+1)/math.factorial(2*j+1)
        cs += ((-1)**j)*power(r,2*j)/math.factorial(2*j)
    sn = inflate(sn, power(I(ab(r)),33)/math.factorial(33))
    cs = inflate(cs, power(I(ab(r)),32)/math.factorial(32))
    return [(sn,cs),(cs,-sn),(-sn,-cs),(-cs,sn)][q%4]


f_int = [-663346670,533331766,164165448,-88458226,176787232,184734098,
         -306743621,-247733884,347656722,3818045,-65652459,-195071970,
         84842579,-48880280]
g_int = [-2110590631,-264410890,-276887860,-677439980,485951745,
         72428290,207301287]


def neutral(free):
    out = [I(0),I(0)]+free
    for n in range(2,N):
        p = n%2
        ratio = (I('.25')+k2[p])/(I('.25')+k2[n])
        if p==0:
            ratio *= I(2).sqrt()
        out[p] -= ratio*out[n]
    return out


f = neutral([I(x)/2**30 for x in f_int])
g = neutral([I(g_int[(n-2)//2])/2**30 if n%2==0 else I(0)
             for n in range(2,N)])
h = [eta[n]*f[n] for n in range(N)]

# Exact digamma recurrence with the cited C744w(12) sector remainder.
diag = []
for n in range(N):
    y2 = k2[n]/4
    den = I('64.25')*I('64.25')+y2
    value = den.ln()/2-I('64.25')/(2*den)-pi.ln()
    for j in range(64):
        a = I(j)+I('.25')
        value -= a/(a*a+y2)
    diag.append(inflate(value,I(2).sqrt()/(6*den)))


def response(coeff):
    # Complete response: explicit prefix and C744v(10)'s analytic tail.
    prefix = I(0)
    q = 1/fourth
    for j in range(J):
        c = I(2*j)+I('.5')
        for p in [0,1]:
            total = sum((alpha[n]*c*coeff[n]/(c*c+k2[n])
                         for n in range(p,N,2)),I(0))
            prefix += (1-((-1)**p)*q)*square(total)
        q /= 3
    cj = I(2*J)+I('.5')
    leading = sum((square(sum((alpha[n]*coeff[n] for n in range(p,N,2)),I(0)))
                   /(2*cj) for p in [0,1]),I(0))
    scalar_error = 1/(cj*cj)+2*k2[-1]*(1/(6*power(cj,3))+1/power(cj,4))
    scalar_error += q*(1/(2*cj)+1/(cj*cj))
    abs_parity_squares = sum((square(sum((I(ab(alpha[n]*coeff[n]))
                                          for n in range(p,N,2)),I(0)))
                              for p in [0,1]),I(0))
    error = scalar_error*abs_parity_squares
    return inflate(prefix+leading,error),dict(prefix=prefix.json(),
        leading_tail=leading.json(),entire_tail_error=error.json(),
        scalar_tail_error=scalar_error.json())


def prime_powers(s):
    result=[]
    for n in range(2,4000):
        if not 3**(s-1)<n*n<3**(s+1):
            continue
        rem=n; factors=[]
        for p in range(2,math.isqrt(n)+1):
            if rem%p==0:
                factors.append(p)
                while rem%p==0:
                    rem//=p
        if rem>1:
            factors.append(rem)
        if len(factors)==1:
            result.append((n,factors[0]))
    assert 4000**2>3**(s+1)
    return result


def translations(s, pairs):
    totals = [I(0) for _ in pairs]
    records=[]
    for n,p in prime_powers(s):
        weight=I(p).ln()/I(n).sqrt()
        zero=(n*n==3**s)
        delta=I(0) if zero else s*ell-I(n).ln()
        if zero:
            values=[dot(x,y) for x,y in pairs]
        else:
            assert delta.lo>0 or delta.hi<0
            positive=delta.lo>0
            sign=1 if positive else -1
            trigs=[sincos(w*delta) for w in k]
            values=[I(0) for _ in pairs]
            for a in range(N):
                for b in range(N):
                    if a==b:
                        entry=ell-sign*delta if a==0 else (
                            (ell-sign*delta)*trigs[a][1]/2-sign*trigs[a][0]/(2*k[a]))
                    else:
                        entry=(-eta[a]*eta[b]*k[a]*trigs[a][0]+k[b]*trigs[b][0]
                               if positive else k[a]*trigs[a][0]-eta[a]*eta[b]*k[b]*trigs[b][0])
                        entry /= k2[a]-k2[b]
                    entry *= norm[a]*norm[b]
                    for index,(x,y) in enumerate(pairs):
                        values[index] += entry*x[b]*y[a]
        for index,v in enumerate(values):
            totals[index] += weight*v
        records.append(dict(n=n,prime=p,weight=weight.json(),delta=delta.json(),
            contributions=[(weight*v).json() for v in values]))
    return totals,records


def continuous(s, x, y):
    total=I(0)
    for j in range(1,8):
        c=I(2*j)+I('.5')
        q=1/(I(3**j)*fourth)
        minus=sum((norm[n]*c*(1-eta[n]*q)*y[n]/(c*c+k2[n]) for n in range(N)),I(0))
        plus=sum((norm[n]*c*(eta[n]-q)*x[n]/(c*c+k2[n]) for n in range(N)),I(0))
        total += power(q,s-1)*minus*plus
    q8=1/(I(3**8)*fourth)
    tail=power(q8,s-1)/(I('16.5')*(1-I(1)/3**(s-1)))
    tail *= (norm2(x)*norm2(y)).sqrt()
    return inflate(total,tail),dict(prefix=total.json(),entire_tail_error=tail.json())


sf,sf_evidence=response(f)
sg,sg_evidence=response(g)
df=sum((diag[n]*square(f[n]) for n in range(N)),I(0))
dg=sum((diag[n]*square(g[n]) for n in range(N)),I(0))
seven,seven_rows=translations(7,[(f,g),(g,h)])
remote,remote_rows=translations(14,[(f,h)])
continuous_records=[]
for s,x,y,index in [(7,f,g,0),(7,g,h,1),(14,f,h,0)]:
    value,record=continuous(s,x,y)
    (seven if s==7 else remote)[index] += value
    continuous_records.append(dict(separation=s,**record))

endpoint=2*(df+sf)-2*remote[0]
middle=dg-2*sum(seven,I(0))
comparison=endpoint+middle
original=comparison+sg
failures=[]
checks=dict(complete_seven_count=len(seven_rows)==16,
    complete_remote_count=len(remote_rows)==334,
    zero_delay_present=sum(row['n']==2187 for row in remote_rows)==1,
    comparison_strict_negative=comparison.hi<Decimal('-.530'),
    original_strict_positive=original.lo>Decimal('.770'),
    original_bounded=original.hi<Decimal('.774'),
    exact_even_middle=all(g[n].lo==g[n].hi==0 for n in range(1,N,2)))
failures.extend(name for name,ok in checks.items() if not ok)
result=dict(scope='exact-neutral finite-form comparison obstruction, not an original negative triple',
    parameters=dict(modes=N,response_prefix=J,dyadic_denominator=2**30),
    exact_free_numerators=dict(f=f_int,g_even=g_int),
    constants=dict(ell=ell.json(),pi=pi.json()),
    coefficients=dict(f=[x.json() for x in f],g=[x.json() for x in g],h=[x.json() for x in h]),
    diagonal_entries=[x.json() for x in diag],
    response=dict(f=sf_evidence,g=sg_evidence),
    primes=dict(seven=seven_rows,remote=remote_rows),continuous=continuous_records,
    summary=dict(endpoint_energy_minus_remote=endpoint.json(),
        signed_diagonal_middle_contribution=middle.json(),
        comparison_value=comparison.json(),required_comparison='>=0 on every neutral triple',
        restored_middle_response=sg.json(),original_form_value=original.json(),
        comparison_rejected=not failures),checks=checks,failures=failures,
    limitations=['The full middle response must be retained for the actual problem.',
        'This is not a lower bound on the true endpoint residual.',
        'Finite cosine profiles are in the closed form domain; smooth transfer uses C744z Section1.',
        'No H2-budget witness, separation-uniform result, or RH conclusion.'])
path=BASE/'signed-diagonal-stop-545.json'
path.write_text(json.dumps(result,indent=2)+'\n')
print('Comparison:',comparison.lo,comparison.hi,'required >=0')
print('Original form:',original.lo,original.hi,'(different quantity)')
print('Checks:',len(checks),'failures:',failures,'certificate:',path.relative_to(BASE.parent.parent))
assert not failures
