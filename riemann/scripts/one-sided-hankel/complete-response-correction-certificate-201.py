"""Exact rational rectangle certificate for the complete-response bounds.

No sampled transcendental value is used. Each of 2048 closed t cells
has a rational upper enclosure; the only square root is rounded up
to a dyadic rational and checked by exact squaring.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json

CELLS = 2048
SCALE = 1 << 50
d, U, A, p, beta = F(5,4), F(121,64), F(27,10), F(3,10), F(2,5)
C = d*d-U/4
H = 2*beta*C
x = F(2,5)

def interval(value):
    return value if isinstance(value, tuple) else (F(value), F(value))

def add(a,b):
    a,b = interval(a),interval(b)
    return a[0]+b[0], a[1]+b[1]

def neg(a):
    a = interval(a)
    return -a[1],-a[0]

def sub(a,b):
    return add(a,neg(b))

def mul(a,b):
    a,b = interval(a),interval(b)
    terms = [s*t for s in a for t in b]
    return min(terms),max(terms)

def div(a,b):
    b = interval(b)
    assert b[0]>0
    return mul(a,(1/b[1],1/b[0]))

def square_positive(a):
    a = interval(a)
    assert a[0]>=0
    return a[0]*a[0],a[1]*a[1]

def ceil_scaled(a):
    return -((-a.numerator*SCALE)//a.denominator)

def sqrt_upper(a):
    assert a>=0
    num = a.numerator*SCALE*SCALE
    root = isqrt(num//a.denominator)
    if root*root*a.denominator<num:
        root += 1
    assert root*root*a.denominator>=num
    assert root == 0 or (root-1)*(root-1)*a.denominator<num
    return F(root,SCALE)

rows = []
for j in range(CELLS):
    t = (F(j,CELLS),F(j+1,CELLS))
    t2 = square_positive(t)
    L = add(add(d*d,mul(2*d*p,t)),mul(F(1,4),t2))
    B = add(add(U*U/4,mul(2*U*p*d,t)),mul(d*d,t2))
    E = add(add(U/4,mul(2*d*p,t)),mul(F(1,4),t2))
    Ut = sub(U,t2)
    # (|Q(u,-x)|^2-1)/2, including its signed numerator.
    numerator = mul(mul(Ut,x),sub(mul(H,t),mul(E,x)))
    denominator = mul(B,add(add(L,mul(2*beta*x,t)),x*x))
    tail = mul(F(1,2),div(numerator,denominator))
    # The global real-y upper bound for log |Q|.
    numerator = mul(Ut,square_positive(mul(H,t)))
    denominator = mul(8,mul(mul(E,B),L))
    glob = div(numerator,denominator)
    # Exact variation-mass formula at the exponential tilt n/5.
    ratio = div(L,B)
    root = sqrt_upper(ratio[1])
    bracket = add(t,div(Ut,mul(2,add(d-A/5,mul(p,t)))))
    tilt_upper = root*bracket[1]
    rows.append({"cell":j,"tail_upper_scaled":ceil_scaled(tail[1]),
                 "global_upper_scaled":ceil_scaled(glob[1]),
                 "tilt_upper_scaled":ceil_scaled(tilt_upper)})

def rational(x):
    return {"numerator":str(x.numerator),"denominator":str(x.denominator)}

checks = []
for label,key,target in [
    ("tail_integral","tail_upper_scaled",F(-1,400)),
    ("global_integral","global_upper_scaled",F(1,125)),
    ("tilt_integral","tilt_upper_scaled",F(3,2)),
]:
    actual = F(sum(row[key] for row in rows),SCALE*CELLS)
    checks.append({"name":label,"actual_upper":rational(actual),
                   "actual_upper_decimal_preview":float(actual),
                   "required_strict_upper":rational(target),
                   "passed":actual<target})

# Scalar inequalities used to turn the integral bounds into rates.
scalar_cases = [
    ("moment_rate_gap",F(67,6050)-F(1,120),F(1,400)),
    ("pole_decay_from_L722",F(1,8)*(U-1)/((d+1)*(U+d))-F(1,5000),F(1,100)),
    ("exponential_tilt_log_bound",1+F(41,100)+F(41,100)**2/2+F(41,100)**3/6,F(3,2)),
    ("tail_first_omitted_y_at_n15",F(9,20)-A/(8*15),F(2,5)),
]
for label,actual,target in scalar_cases:
    checks.append({"name":label,"actual":rational(actual),
                   "required_strict_lower":rational(target),"passed":actual>target})

failures = [c['name'] for c in checks if not c['passed']]
result = {"status":"EXACT_RATIONAL_CERTIFICATE","cells":CELLS,
          "cell_domain":"[j/2048,(j+1)/2048], 0<=j<2048; full closed cover of [0,1]",
          "rounding_scale":str(SCALE),"rounding_direction":"upper",
          "checks":checks,"failures":failures,"cell_upper_bounds":rows,
          "qualification":"Finite integral/scalar certificate only. The proof must justify its application to all n and all correction sums."}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(result,indent=2)+'\n')
for check in checks:
    print(check['name'], 'PASS' if check['passed'] else 'FAIL',
          'actual =',check.get('actual_upper',check.get('actual')),
          'required =',check.get('required_strict_upper',check.get('required_strict_lower')))
print('failures =',failures)
print('certificate =',path)
if failures:
    raise SystemExit(1)
