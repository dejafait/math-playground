#!/usr/bin/env python3
"""Independent sparse exact replay of C029s, at unchanged N and precision.

No imports from the original mathematical implementation. Sparse keys
(i,j,k) represent pi**i * sqrt(2)**j * alpha**k, with j in {0,1}.
Full coefficients, endpoints and comparisons are saved, never sampled.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).parent
SOURCE = ROOT / 'tilted-boundary-metric-2010.json'
ORIGINAL = ROOT / 'quadratic-differential-range-2030.json'
source = json.loads(SOURCE.read_text())
original = json.loads(ORIGINAL.read_text())
checks = {}


def check(name, value):
    checks[name] = bool(value)


def add(*polys):
    out = {}
    for p in polys:
        for key, value in p.items():
            out[key] = out.get(key, F(0)) + value
    return {key: value for key, value in out.items() if value}


def scale(p, c):
    return {key: c*value for key, value in p.items() if c*value}


def mul(p, q):
    out = {}
    for (i,j,k), a in p.items():
        for (l,m,n), b in q.items():
            key = i+l, (j+m) % 2, k+n
            out[key] = out.get(key, F(0)) + a*b*2**((j+m)//2)
    return {key: value for key, value in out.items() if value}


def constant(c):
    return {(0,0,0): F(c)} if c else {}


def decode(p):
    return {(i,j,0): F(c[name]) for i,c in enumerate(p)
            for j,name in enumerate(('rational','sqrt2')) if F(c[name])}


def encode(p):
    return [{'pi_power': i, 'sqrt2_power': j, 'alpha_power': k,
             'coefficient': str(v)} for (i,j,k),v in sorted(p.items())]


def interval(obj):
    return F(obj['lower']), F(obj['upper'])


def ivadd(a,b):
    return a[0]+b[0], a[1]+b[1]


def ivscale(a,c):
    return min(a[0]*c,a[1]*c), max(a[0]*c,a[1]*c)


def ivmul(a,b):
    products = [u*v for u in a for v in b]
    return min(products), max(products)


def horner(p,x,s):
    assert all(k == 0 for i,j,k in p)
    out = F(0), F(0)
    for i in range(max((i for i,j,k in p), default=0), -1, -1):
        c = ivadd((p.get((i,0,0), F(0)),)*2,
                  ivscale(s,p.get((i,1,0), F(0))))
        out = ivadd(ivmul(out,x),c)
    return out


def ivjson(iv):
    return dict(zip(('lower','upper'), map(str,iv)))


# Recheck the full analytic-input certificate, with C029n's branch proof.
atans = []
for den,key in ((5,'atan5'), (239,'atan239')):
    terms = [F((-1)**j, (2*j+1)*den**(2*j+1)) for j in range(48)]
    partial = sum(terms,F(0))
    remainder = F(1,97*den**97)
    saved = source[key]
    check(key+'_all_terms_and_remainder', saved['term_count'] == 48
          and F(saved['argument']) == F(1,den)
          and list(map(F,saved['terms'])) == terms
          and F(saved['partial_sum']) == partial
          and F(saved['positive_remainder_upper']) == remainder)
    atans.append((partial,partial+remainder))
machin = ivadd(ivscale(atans[0],16),ivscale(atans[1],-4))
x,s = interval(source['pi_interval']), interval(source['sqrt2_interval'])
check('machin_and_outward_pi', machin == interval(source['pi_machin_interval'])
      and x[0] <= machin[0] <= machin[1] <= x[1])
check('positive_squared_sqrt2', 0 < s[0] and s[0]**2 < 2 < s[1]**2)
check('unchanged_input_intervals', x == interval(original['pi_interval'])
      and s == interval(original['sqrt2_interval'])
      and x[1]-x[0] == s[1]-s[0] == F(1,10**60))

bern = [F(1)]
for m in range(1,19):
    bern.append(-sum((comb(m+1,k)*bern[k] for k in range(m)),F(0))/F(m+1))
check('bernoulli_complete', bern == list(map(F,source['bernoulli_0_through_18'])))
check('screen_bernoulli_complete', bern == list(map(F,original['bernoulli'])))
phases = [constant(1), add(constant(1),{(0,1,0): F(1)}),
          constant(-1), add(constant(-1),{(0,1,0): F(-1)})]
u = []
for n in range(9):
    terms = []
    for h in range(n+1):
        c = -F(factorial(n)*4**h*(4**(h+1)-1)*2**(h+1),
                factorial(n-h)*factorial(2*h+2))*bern[2*h+2]
        terms.append(mul({(h+1,0,0): c}, phases[(n-h)%4]))
    u.append(add(*terms))
    check('source_u_'+str(n), u[n] == decode(source['u_over_S_polynomials'][n]))
    check('screen_u_'+str(n), u[n] == decode(original['u_over_S'][n]))
a,beta,weights = [],[],[]
for n in range(7):
    beta.append(add(scale(u[n],8*n*n+12*n+7),
                    scale(u[n+2],(2*n+3)*(2*n+5)),
                    scale(u[n-2],4*n*(n-1)) if n>=2 else {}))
    weights.append(F(factorial(6),factorial(6-n)*6**n))
    a.append(scale(beta[n],weights[n]))
    check('source_beta_weight_A_'+str(n),
          beta[n] == decode(source['beta_over_S_polynomials'][n])
          and weights[n] == F(source['weights'][n])
          and a[n] == decode(source['a_over_S_polynomials'][n]))
    check('screen_beta_weight_A_'+str(n),
          beta[n] == decode(original['beta_over_S'][n])
          and weights[n] == F(original['weights'][n])
          and a[n] == decode(original['a_over_S'][n]))

# Sparse rational polynomials in t, starting with p_{-1}=0, p_0=1.
p = [{0:F(1)}]
for k in range(6):
    row = {j+1:c for j,c in p[k].items()}
    for j,c in (p[k-1] if k else {}).items():
        row[j] = row.get(j,F(0))-F(2*k+1,2)*c
    p.append({j:c/F(k+1) for j,c in row.items() if c})
for k in range(7):
    saved = {j:F(c) for j,c in enumerate(original['basis_p_0_to_6'][k]) if F(c)}
    check('basis_complete_'+str(k), p[k] == saved and max(p[k]) == k
          and p[k][k] == F(1,factorial(k)) and all((j-k)%2 == 0 for j in p[k]))
b = [add(*(scale(a[k],p[k].get(j,F(0))) for k in range(7))) for j in range(7)]
b_iv = [horner(v,x,s) for v in b]
printed_b = [('1.842192025','1.842192026'),('-1.762759216','-1.762759215'),
             ('0.602116495','0.602116496'),('-0.084441231','-0.084441230'),
             ('0.004543068','0.004543069'),('-0.000049788','-0.000049787'),
             ('-0.000001242','-0.000001241')]
for j in range(7):
    lo,hi = map(F,printed_b[j])
    check('U_complete_coefficients_endpoints_and_printed_'+str(j),
          b[j] == decode(original['U_coefficients'][j])
          and b_iv[j] == interval(original['U_coefficient_intervals'][j])
          and interval(original['U_coefficient_outer_bounds'][j]) == (lo,hi)
          and lo <= b_iv[j][0] <= b_iv[j][1] <= hi)
check('degree_six_normalization', b[6] == scale(a[6],F(1,720)) and b_iv[6][1]<0)

# Independently form every differential-operator entry as a polynomial in alpha.
alpha = {(0,0,1): F(1)}
M = [[{} for k in range(6)] for j in range(7)]
for k in range(6):
    M[k+1][k] = add(constant(k),scale(alpha,2))
    if k:
        M[k-1][k] = constant(F(k,4))
for j in range(7):
    for k in range(6):
        saved = add(*(scale({(0,0,r): F(1)},F(c))
                      for r,c in enumerate(original['operator_matrix_affine_alpha'][j][k])))
        check('operator_entry_'+str(j)+'_'+str(k),M[j][k] == saved)

# Necessary row R annihilates M, so R*U=0 is required for every preimage.
l1,l3,l5 = [add(constant(k),scale(alpha,2)) for k in (1,3,5)]
R = [scale(mul(mul(l1,l3),l5),-4),{},mul(l3,l5),{},scale(l5,F(-3,4)),{},constant(F(15,16))]
residuals = [add(*(mul(R[j],M[j][k]) for j in range(7))) for k in range(6)]
for k,residual in enumerate(residuals):
    check('elimination_annihilates_column_'+str(k), not residual)
necessary = add(*(mul(R[j],b[j]) for j in range(7)))
f = [{(i,j,0):v for (i,j,k),v in necessary.items() if k==r} for r in range(4)]
check('necessary_degree_at_most_three',all(k<=3 for i,j,k in necessary))
expanded = [add(scale(b[2],15),scale(b[0],-60),scale(b[4],F(-15,4)),scale(b[6],F(15,16))),
            add(scale(b[2],16),scale(b[0],-184),scale(b[4],F(-3,2))),
            add(scale(b[2],4),scale(b[0],-144)),scale(b[0],-32)]
check('all_expanded_coefficients', f == expanded)
f_iv = [horner(v,x,s) for v in f]
printed_f = [('-101.516811776','-101.516811775'),('-329.336283397','-329.336283396'),
             ('-262.867185716','-262.867185715'),('-58.950144823','-58.950144822')]
for j in range(4):
    lo,hi = map(F,printed_f[j])
    check('F_complete_coefficients_endpoints_and_printed_'+str(j),
          f[j] == decode(original['necessary_cubic_coefficients'][j])
          and f_iv[j] == interval(original['necessary_cubic_intervals'][j])
          and interval(original['necessary_cubic_outer_bounds'][j]) == (lo,hi)
          and lo <= f_iv[j][0] <= f_iv[j][1] <= hi < 0)

failures = [name for name,ok in checks.items() if not ok]
report = {'scope':'C029s fixed full U_6, q=t^2+1/4, every real alpha>=0; independent exact replay',
          'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (SOURCE,ORIGINAL)},
          'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'checks':checks,'failures':failures,'result':'PASS' if not failures else 'FAIL',
          'U_coefficients':list(map(encode,b)), 'U_intervals':list(map(ivjson,b_iv)),
          'U_printed_bounds':printed_b,'eliminating_row':list(map(encode,R)),
          'operator_matrix':[[encode(v) for v in row] for row in M],
          'annihilation_residuals':list(map(encode,residuals)),
          'necessary_cubic_coefficients':list(map(encode,f)),
          'necessary_cubic_intervals':list(map(ivjson,f_iv)),
          'necessary_cubic_printed_bounds':printed_f,
          'required':'All f_j upper bounds strictly negative; alpha>=0 implies F(alpha)<0, including alpha=0.',
          'qualification':'Paper argument and C029n analytic input proof remain essential; no formal verification or RH conclusion.'}
out = ROOT/'quadratic-differential-range-audit-2032.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print('Result:',report['result'],'; checks:',len(checks),'; failures:',failures)
for j,(lo,hi) in enumerate(printed_f):
    print('f_'+str(j)+': exact replay enclosure contained in ['+lo+', '+hi+']; required upper < 0')
print('All six elimination residuals:', 'zero' if not any(residuals) else 'FAIL')
print('Full coefficients, endpoints and comparisons:',out.relative_to(Path.cwd()))
if failures:
    raise SystemExit(1)
