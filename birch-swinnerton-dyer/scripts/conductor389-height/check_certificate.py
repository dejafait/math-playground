#!/usr/bin/env python3
"""Read all saved finite witnesses; independently check their exact identities.

Uses sparse polynomial arithmetic, symbolic E2 perturbation for sigma, and
modular logarithm summation rather than the producer's exact log fractions.
This finite verification is not the separately scheduled mathematical audit.
"""
from fractions import Fraction as R
from pathlib import Path
from math import gcd, comb
import json
import sys
sys.set_int_max_str_digits(0)

DIR = Path(__file__).resolve().parent/'step-506'
C = json.loads((DIR/'certificate.json').read_text())
checks = {}


def poly(a):
    if isinstance(a,dict):
        return {k:R(v) for k,v in a.items() if v}
    return {i:R(v) for i,v in enumerate(a) if R(v)}


def plus(*polys):
    out = {}
    for a in polys:
        for i,v in a.items():
            out[i] = out.get(i,R(0))+v
    return {i:v for i,v in out.items() if v}


def times(a,b):
    out = {}
    for i,v in a.items():
        for j,w in b.items():
            out[i+j] = out.get(i+j,R(0))+v*w
    return {i:v for i,v in out.items() if v}


def sc(a,v):
    return {i:x*v for i,x in a.items() if x*v}


def pw(a,n):
    out = {0:R(1)}
    for _ in range(n):
        out = times(out,a)
    return out


def dx(a):
    return {i-1:i*v for i,v in a.items() if i and v}


def val(a):
    a = R(a)
    if not a:
        return 10**9
    z = 0
    n,d = abs(a.numerator),a.denominator
    while n % 5 == 0:
        z += 1
        n //= 5
    while d % 5 == 0:
        z -= 1
        d //= 5
    return z


def mod(a,n):
    a = R(a)
    return a.numerator*pow(a.denominator,-1,5**n) % 5**n


def require(key,condition):
    assert condition,key
    checks[key] = True


Q = poly(C['frobenius']['short_Q'])
require('short_polynomial',Q == poly([R(107,108),R(-7,3),0,1]))
require('smooth_reduction',mod(-4*Q[1]**3-27*Q[0]**2,1) != 0)
# The inverse is auxiliary: every load-bearing Bezout identity is checked
# explicitly at its use in a vertical reduction below.
delta = plus({5*i:v for i,v in Q.items()},sc(pw(Q,5),-1))
require('F_delta',delta == poly(C['frobenius']['delta']) and min(map(val,delta.values()))>=1)
columns = [{},{}]
require('term_count',len(C['frobenius']['terms']) == 16)
expected_pairs = {(j,i) for j in range(8) for i in range(2)}
observed_pairs = set()
for term in C['frobenius']['terms']:
    j,i = term['j'],term['basis_index']
    observed_pairs.add((j,i))
    binomial = R((-1)**j*comb(2*j,j),4**j)
    require(f'binomial_{j}_{i}',R(term['binomial'])==binomial)
    num = times({5*(i+1)-1:R(5)*binomial},pw(delta,j))
    require(f'numerator_{j}_{i}',num==poly(term['numerator']))
    reconstructed,vertical_sum = {},{}
    require(f'parts_indices_{j}_{i}',[p['Q_power'] for p in term['parts']] == list(range(len(term['parts']))))
    for part in term['parts']:
        a = poly(part['A'])
        s,m = part['Q_power'],part['m']
        require(f'part_bound_{j}_{i}_{s}',(not a or max(a)<=2) and m==5*j+2-s)
        reconstructed = plus(reconstructed,times(a,pw(Q,s)))
        before = a
        require(f'chain_length_{j}_{i}_{s}',len(part['vertical'])==max(m,0))
        for vstep in part['vertical']:
            b,c = poly(vstep['B']),poly(vstep['C'])
            require(f'vertical_{j}_{i}_{s}_{m}',
                m==vstep['m'] and before==poly(vstep['A']) and
                before==plus(times(c,Q),times(b,dx(Q))) and
                poly(vstep['next'])==plus(c,sc(dx(b),R(2,2*m-1))))
            before = poly(vstep['next'])
            m -= 1
        if part['m']<0:
            before = times(a,pw(Q,-part['m']))
        require(f'vertical_result_{j}_{i}_{s}',before==poly(part['reduced']))
        vertical_sum = plus(vertical_sum,before)
    require(f'Qadic_reconstruction_{j}_{i}',reconstructed==num)
    for hstep in term['horizontal']:
        degree = hstep['degree']
        primitive = {degree-2:R(hstep['primitive_coefficient'])}
        after = plus(vertical_sum,sc(plus(times(dx(primitive),Q),
                          sc(times(primitive,dx(Q)),R(1,2))),-1))
        require(f'horizontal_{j}_{i}_{degree}',poly(hstep['before'])==vertical_sum and
                poly(hstep['after'])==after)
        vertical_sum = after
    require(f'reduction_{j}_{i}',vertical_sum==poly(term['reduced']) and
            (not vertical_sum or max(vertical_sum)<=1))
    columns[i] = plus(columns[i],vertical_sum)
require('complete_F_terms',observed_pairs==expected_pairs)
f = [[columns[c].get(r,R(0)) for c in range(2)] for r in range(2)]
require('F_exact',f==[[R(x) for x in row] for row in C['frobenius']['F_exact_truncation']])
require('F_residues',[[mod(x,7) for x in row] for row in f]==C['frobenius']['F_mod_5^7'])
require('F_trace_determinant_diagnostics',mod(f[0][0]+f[1][1]+3,7)==0 and
        mod(f[0][0]*f[1][1]-f[0][1]*f[1][0]-5,7)==0)
fpow = [[R(int(r==c)) for c in range(2)] for r in range(2)]
# Avoid growth in six exact matrix powers; all entries are integral, so reduce.
for _ in range(6):
    fpow = [[R(mod(sum(fpow[r][k]*f[k][c] for k in range(2)),7))
              for c in range(2)] for r in range(2)]
e2 = mod(-12*fpow[0][1]/fpow[1][1],6)
require('E2_MST_power',e2==C['frobenius']['E2_mod_5^6'] and val(fpow[1][1])==0)

# Formal series identities and symbolic sigma(E2+5^6*z) coefficients.
S = C['sigma']
w,x,omega = poly(S['w']),poly(S['t_squared_x']),poly(S['omega'])
def trunc(a,n):
    return {i:v for i,v in a.items() if i<n}
require('w_equation',trunc(plus(w,{3:R(-1)},sc(times({2:R(1)},w),-1),
                sc(pw(w,2),-1),sc(times({1:R(1)},pw(w,2)),2)),12)=={})
require('x_inverse',trunc(times({i-3:v for i,v in w.items()},x),9)=={0:R(1)})
require('omega_equation',trunc(plus(times(omega,plus(sc(x,2),{3:R(-1)})),
                sc(plus(sc(x,2),sc(times({1:R(1)},dx(x)),-1)),-1)),8)=={})
cp = {0:R(4-e2,12),1:R(-5**6,12)}  # polynomial in uncertainty z
integral = {}
for k in range(-2,5):
    coeff = {0:sum(x.get(j,R(0))*omega.get(k+2-j,R(0)) for j in range(k+3))}
    if k>=0:
        coeff = plus(coeff,sc(cp,omega.get(k,R(0))))
    require(f'xomega_{k}',coeff.get(0,0)==R(S['xomega'][str(k)][0]))
    if k!=-1:
        integral[k+1] = sc(coeff,R(1,k+1))
    else:
        require('no_log_formal_integral',not any(coeff.values()))
h = [plus(*(sc(a,-omega.get(k-j,R(0))) for j,a in integral.items()))
     for k in range(5)]
theta = [{0:R(1)}]
symbolic_profile = []
for k in range(1,6):
    theta.append(sc(plus(*(times(h[j],theta[k-1-j]) for j in range(k))),R(1,k)))
for k,a in enumerate(theta):
    center,exponent = R(S['theta_balls'][k][0]),S['theta_balls'][k][1]
    uncertainty = min([val(v) for j,v in a.items() if j>0] or [10**9])
    require(f'sigma_center_and_error_{k+1}',a.get(0,0)==center and
            uncertainty>=exponent and exponent>=6-k and val(center)>=0)
    symbolic_profile.append({'degree':k+1,'polynomial_in_z':{str(j):str(v) for j,v in a.items()},
                             'certified_exponent':uncertainty,'required':6-k})


def curve(a):
    if a is None:
        return True
    x,y = map(R,a)
    return y*y+y==x*x*x+x*x-2*x


def relation(a,b,c):
    # Check chord/tangent Vieta identity and the negation of the third root.
    if a is None:
        return tuple(map(R,b))==tuple(map(R,c))
    x,y = map(R,a)
    u,v = map(R,b)
    z,w = map(R,c)
    lam = (v-y)/(u-x) if x!=u else (3*x*x+2*x-2)/(2*y+1)
    return z+x+u==lam*lam-1 and -w-1==y+lam*(z-x)


height_results = {}
point_summary = {}
for label,D in C['height_details'].items():
    r = D['point']
    require(f'point_on_curve_{label}',curve(r) and r==C['points'][label])
    require(f'chain_has_nine_steps_{label}',len(D['multiplication_chain'])==9)
    prev = None
    for k,entry in enumerate(D['multiplication_chain'],1):
        out = entry['point']
        require(f'point_chain_{label}_{k}',entry['multiple']==k and out is not None and curve(out) and relation(prev,r,out))
        prev = out
    require(f'multiple9_matches_{label}',prev==D['multiple_9'])
    x,y = map(R,prev)
    d = D['d']
    alpha,beta = R(D['alpha']),R(D['beta'])
    require(f'point_reduced_coordinates_{label}',x*d*d==alpha and y*d**3==beta and
            alpha.denominator==beta.denominator==1 and d>0 and x.denominator==d*d and
            gcd(int(alpha),d)==gcd(int(beta),d)==1)
    t = -x/y
    require(f'formal_eligibility_{label}',t==R(D['t']) and val(t)>=1 and val(-alpha/beta)==0)
    # Direct bad-prime nonsingularity check in addition to the I_1 argument.
    def rmod389(a):
        return a.numerator*pow(a.denominator,-1,389) % 389
    if d % 389:
        xr,yr = rmod389(x),rmod389(y)
        nonsingular = (2*yr+1) % 389 != 0 or (3*xr*xr+2*xr-2) % 389 != 0
    else:
        nonsingular = True  # reduced projective point is O
    require(f'bad_prime_nonsingular_{label}',nonsingular)
    theta_value = sum(a.get(0,0)*t**k for k,a in enumerate(theta))
    unit = (-alpha/beta)*theta_value
    eval_exponent = min([6*val(t)]+[S['theta_balls'][k][1]+k*val(t) for k in range(6)])
    require(f'unit_center_{label}',unit==R(D['sigma_over_d_unit'][0]) and
            eval_exponent==D['sigma_over_d_unit'][1] and eval_exponent>=6)
    z = unit**4-1
    # Modular sum removes the large exact rational fractions in the producer.
    partial = 0
    for k in range(1,8):
        term = z**k/R(k)
        partial = (partial+(-1)**(k+1)*mod(term,6)) % 5**6
    height_results[label] = mod(R(2*partial,4*81),6)
    require(f'height_log_{label}',height_results[label]==D['q_H_center_mod_5^6'] and val(z)>=1 and
            mod(R(D['log_partial']),6)==mod(R(partial,4),6))
    point_summary[label] = {'multiple9':[str(x),str(y)],'alpha':str(alpha),'beta':str(beta),
                            'd':d,'v_t':val(t),'unit_mod_5^6':mod(unit,6),
                            'q_H_mod_5^6':height_results[label]}
require('sum_points',relation(C['points']['P'],C['points']['Q'],C['points']['P+Q']))
require('all_three_heights',set(height_results)=={'P','Q','P+Q'})
a,b,c = height_results['P'],height_results['Q'],height_results['P+Q']
off = R(a+b-c,2)
det = a*b-off**2
require('L119_matrix',C['L119']['H_hat']==[[-a,str(off)],[str(off),-b]])
require('L119_strict',str(det)==C['L119']['D0'] and val(det)==2<6 and
        C['L119']['a']==0 and C['L119']['B0']==6 and C['L119']['N']==6)
report = {'status':'FINITE_WITNESSES_PASS_UNAUDITED_MATHEMATICAL_WRITEUP',
          'checks':checks,'check_count':len(checks),'symbolic_sigma':symbolic_profile,
          'points':point_summary,'E2_mod_5^6':e2,'determinant':str(det),
          'actual_determinant_valuation':val(det),'required_strict_bound':6,
          'failures':[], 'limitations':['Infinite tails use the cited bounds and written specialization; this is not their independent audit.',
          'Published group/Sha results remain unreplayed; no general BSD conclusion.']}
path = DIR/'verification.json'
path.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['status','check_count','E2_mod_5^6',
                 'actual_determinant_valuation','required_strict_bound','failures']},indent=2))
print('Full verification: '+str(path))
