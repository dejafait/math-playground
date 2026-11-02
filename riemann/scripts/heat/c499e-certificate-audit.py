#!/usr/bin/env python3
"""Read-only independent consumer of C499e's saved rows; no producer imports.

Checks existing operands/rows, not a new estimator run or parameter search.
Output is separate from every producer certificate. Exact arithmetic only.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
import sys

BASE = Path(__file__).resolve().parent
OUT = BASE/'c499e-certificate-audit.json'
G = 10**60
ledger = {'fixed_rational_setup': 4096}
evidence, failures, roots, elementary = [], [], [], []
stats = dict(rationals=0, intervals=0)


def save_failure(kind, value, traceback):
    OUT.write_text(json.dumps(enc(dict(result='AUDIT_FAILURE',error=str(value),
        failures=failures,checks=evidence,roots=roots,elementary_evaluations=elementary,
        reconstructed_assembly_charges=ledger)),separators=(',',':'))+'\n')
    print('AUDIT_FAILURE: '+str(value)+'; certificate='+str(OUT))
    sys.__excepthook__(kind,value,traceback)


sys.excepthook = save_failure


def enc(v):
    if isinstance(v, Q):
        return dict(numerator=str(v.numerator), denominator=str(v.denominator))
    if isinstance(v, I):
        return dict(lower=enc(v.l), upper=enc(v.h))
    if isinstance(v, dict):
        return {k: enc(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [enc(x) for x in v]
    return v


def dec(v):
    if isinstance(v, float):
        raise ValueError('floating point in exact evidence')
    if isinstance(v, list):
        return [dec(x) for x in v]
    if not isinstance(v, dict):
        return v
    if set(v) == {'numerator', 'denominator'}:
        n, d = int(v['numerator']), int(v['denominator'])
        if d <= 0:
            raise ValueError('nonpositive denominator')
        stats['rationals'] += 1
        return Q(n, d)
    if set(v) == {'lower', 'upper'}:
        stats['intervals'] += 1
        return I(dec(v['lower']), dec(v['upper']))
    return {k: dec(x) for k, x in v.items()}


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def load(name):
    return dec(json.loads((BASE/name).read_text()))


def require(label, actual, expected=True):
    ok = actual == expected
    evidence.append(dict(label=label, passed=ok, actual=actual, required=expected))
    if not ok:
        failures.append(label)
        raise AssertionError(label)


def tick(name, amount):
    ledger[name] = ledger.get(name, 0)+amount


def floor(q):
    return Q(q.numerator*G//q.denominator, G)


def ceil(q):
    return -floor(-q)


class I:
    def __init__(self, lo, hi=None):
        self.l, self.h = Q(lo), Q(lo if hi is None else hi)
        if self.l > self.h:
            raise ValueError('reversed interval')

    def __eq__(self, other):
        return isinstance(other, I) and (self.l, self.h) == (other.l, other.h)

    def __add__(self, other):
        tick('__add__', 32)
        b = iv(other)
        return I(floor(self.l+b.l), ceil(self.h+b.h))

    __radd__ = __add__

    def __neg__(self):
        tick('__neg__', 8)
        return I(-self.h, -self.l)

    def __sub__(self, other):
        tick('__sub__', 8)
        return self + -iv(other)

    def __rsub__(self, other):
        return iv(other)+-self

    def __mul__(self, other):
        tick('__mul__', 48)
        b = iv(other)
        v = [self.l*b.l, self.l*b.h, self.h*b.l, self.h*b.h]
        return I(floor(min(v)), ceil(max(v)))

    __rmul__ = __mul__

    def __truediv__(self, other):
        tick('__truediv__', 32)
        b = iv(other)
        if b.l <= 0 <= b.h:
            raise ValueError('zero divisor')
        return self*I(floor(1/b.h), ceil(1/b.l))

    def __rtruediv__(self, other):
        return iv(other)/self


def iv(v):
    return v if isinstance(v, I) else I(v)


def nth_floor(z, k):
    # Newton iteration, independent of the producer's binary search.
    if z == 0:
        return 0
    x = 1 << ((z.bit_length()+k-1)//k)
    while True:
        y = ((k-1)*x+z//x**(k-1))//k
        if y >= x:
            break
        x = y
    if not x**k <= z < (x+1)**k:
        raise ArithmeticError('Newton root bracket failed')
    return x


def radical(a, k, name):
    if a.l < 0:
        raise ValueError('negative radical')
    if k == 2:
        tick('sqrt_box', 64)
    else:
        tick('root_endpoint_setup', 64*k)
    r = []
    for v in (a.l, a.h):
        z = v.numerator*G**k//v.denominator
        root = isqrt(z) if k == 2 else nth_floor(z, k)
        if not root**k <= z < (root+1)**k:
            raise ArithmeticError('integer root inequality failed')
        if not Q(root, G)**k <= v < Q(root+1, G)**k:
            raise ArithmeticError('rational root inequality failed')
        r.append(root)
        if k != 2:
            # Count the producer's binary-search control path from the proven
            # integer root, without using its exponentiation or implementation.
            left, right, iterations = 0, 1 << ((z.bit_length()+k-1)//k), 0
            while right-left > 1:
                mid = (left+right)//2
                if mid <= root:
                    left = mid
                else:
                    right = mid
                iterations += 1
            if left != root:
                raise ArithmeticError('binary-search trace disagrees')
            tick('root_integer_iteration', 16*k*iterations)
    answer = I(Q(r[0], G), Q(r[1]+1, G))
    roots.append(dict(name=name, degree=k, operand=a, lower_integer=r[0],
                      upper_floor_integer=r[1], enclosure=answer))
    return answer


def smallest(*xs):
    tick('interval_minimum', 8*len(xs))
    return I(min(x.l for x in xs), min(x.h for x in xs))


def largest(*xs):
    tick('interval_maximum', 8*len(xs))
    return I(max(x.l for x in xs), max(x.h for x in xs))


def ln_unit(v):
    tick('log_unit', 4096)
    if not 1 <= v <= 2:
        raise ValueError('log domain')
    z = (v-1)/(v+1)
    z2, power, total = z*z, I(z), I(0)
    for j in range(100):
        total = total+power/(2*j+1)
        power = power*z2
    tail = 2*power.h/((201)*(1-z2))
    ans = I(floor(2*total.l), ceil(2*total.h+tail))
    elementary.append(dict(kind='log_unit', v=v, z=z, terms=100,
                           half_sum=total, first_omitted_power=power,
                           tail_upper=tail, enclosure=ans))
    return ans


def ln(v):
    tick('log_exact', 1024)
    if v <= 0:
        raise ValueError('log argument')
    k = v.numerator.bit_length()-v.denominator.bit_length()
    w = v/Q(2)**k
    if w < 1:
        k, w = k-1, 2*w
    if w >= 2:
        k, w = k+1, w/2
    return k*LOG2+ln_unit(w)


def exp(v):
    tick('exp_exact', 4096)
    u, term, total = abs(v), I(1), I(1)
    if not u < 182:
        raise ValueError('exp tail ratio')
    for j in range(1, 181):
        term = term*u/j
        total = total+term
    ratio = u/182
    tail = term.h*u/181/(1-ratio)
    positive = I(total.l, ceil(total.h+tail))
    ans = I(1)/positive if v < 0 else positive
    elementary.append(dict(kind='exp', argument=v, degree=180, sum=total,
                           last_term=term, subsequent_ratio_cap=ratio,
                           tail_upper=tail, positive_enclosure=positive,
                           enclosure=ans))
    return ans


def prod_check(name, truth, actual, required):
    tick('check', 16)
    reconstructed_checks.append(dict(name=name, passed=bool(truth),
                                     actual=actual, required=required))
    require('predicate '+name, bool(truth))


data = load('third-derivative-entry-budget.json')
prior = load('uniform-quadratic-curvature-budget.json')
corner = load('fixed-corner-two-charge.json')
audit = load('c499c-certificate-audit.json')
reconstructed_checks = []
producer_name = 'phase-sensitive-256-block-certificate.py'
prod_check('arithmetic definitions unchanged', digest(BASE/producer_name) == audit['producer_sha256'],
           digest(BASE/producer_name), audit['producer_sha256'])
prod_check('prior envelope completed', prior['result'] == 'ENVELOPE_FAIL' and not prior['failures'],
           prior['result'], 'ENVELOPE_FAIL with no implementation failures')
for row in prior['inputs']:
    prod_check('retained input '+row['path'], digest(BASE/row['path']) == row['sha256'],
               digest(BASE/row['path']), row['sha256'])
for row in data['inputs']:
    require('input hash '+row['path'], digest(BASE/row['path']), row['sha256'])
for row in audit['inputs']:
    require('accepted C499c linkage '+row['path'], digest(BASE/row['path']), row['sha256'])
require('target script hash', digest(BASE/'third-derivative-entry-budget.py'), data['script_sha256'])

t, X, n, N = Q('.16836'), Q('6000284561421.5'), 691004, 691260
ell0, eps = Q('24.18022820120389'), Q('.0000006')
eps1 = (eps+Q('.0000013'))*Q('8.770232')/Q('.14142')
r0 = Q(14176540015048665224252705167939023,33554432000000000000000000000000000000)
params = dict(t=t, X=X, n=n, N=N, ell0=ell0, epsilon=eps, epsilon_1=eps1, r0=r0)
prod_check('exact parameters', prior['parameters'] == params, prior['parameters'], 'specified target')
require('target parameters', data['parameters'], params)
pi, sig, LX = [corner['elementary_inputs'][k] for k in ('pi', 'sigma', 'L')]
R, J, D = [corner['bounds'][k] for k in ('R', 'Jplus', 'product_derivative_cap')]
Y = 4*pi*(N*N-t/16)
domain = t*(LX+(Y-X)/X)
cn, cn1 = 4*pi*(n*n-t/16), 4*pi*((n+1)**2-t/16)
prod_check('closed analytic domain', Y.l > X and domain.h < Q('5.17'), domain, '<5.17; Y>X')
prod_check('initial floor cell', cn.h <= X < cn1.l, dict(left=cn, right=cn1), 'left<=X<right')
dmax = (7*t/(8*pi*X)).h
lam, upper = 2*(Q(n*n)-dmax)/N**3, Q(2*(N+1)**2, n**3)
prod_check('positive global third derivative range', 0 < lam <= upper,
           dict(lower=lam, upper=upper), '0<lambda<=Lambda')
require('full domain', data['domain'], dict(Y=Y, initial_left=cn, initial_right=cn1,
    analytic_test=domain, delta_upper=dmax, a_lower=n*n-dmax, a_upper=(N+1)**2,
    lambda_lower=lam, Lambda_upper=upper,
    shifted_domain='n<u<=n+L-a; 0<=v<=a; n<u+v<=n+L<=N',
    cutoff='[X,C_(n+1)); [C_q,C_(q+1)); singleton Y, with canonical left equality'))

A = (2/radical(pi, 2, 'sqrt pi'))*(1+radical(1+3*pi/8, 2, 'sqrt 1+3pi/8'))
V = 2+2*radical(I(2), 2, 'sqrt 2 B')
A3 = V*radical(I(2), 2, 'sqrt 2 A3')
B3 = V*radical(Q(81,8)*Q(2,3)**6*4*A*A/(V*V), 6, 'B3 sixth root')
C3 = V*radical(8*A/V, 2, 'C3 square root')
constant_term = B3*radical(I(upper*upper/lam), 6, 'constant sixth root')
require('constants', data['constants'], dict(A=A, B=V, A3=A3, B3=B3, C3=C3))
require('shift parameter ordering', [p['a'] for p in data['shift_parameters']], list(range(1,256)))
for par in data['shift_parameters']:
    a = par['a']
    tick('shift_rational_setup', 32)
    require('shift parameter '+str(a), par, dict(a=a, lambda_lower=a*lam,
            Lambda_upper=a*upper, multiplier=A/radical(I(a*lam), 2, 'shift '+str(a))))

require('prefix coverage', [p['L'] for p in data['prefix_rows']], list(range(1,257)))
require('shift coverage', [(r['L'],r['a']) for r in data['shift_rows']],
        [(L,a) for L in range(1,257) for a in range(1,L)])
require('difference coverage', [(r['L'],r['H']) for r in data['difference_rows']],
        [(L,H) for L in range(1,257) for H in range(1,L+1)])
si, di, M, best = 0, 0, I(0), None
shift_good, direct_good, difference_good = True, True, True
for prefix in data['prefix_rows']:
    L = prefix['L']
    direct, third = I(L), None
    if L >= 4:
        tick('third_rational_setup', 64)
        terms = [A3*radical(I(upper/(lam*L)),4,'direct first '+str(L)), constant_term,
                 C3/radical(I(lam*L**3),4,'direct third '+str(L))]
        normalized = largest(*terms)
        raw = L*normalized
        direct = smallest(I(L), raw)
        third = dict(terms=terms, normalized=normalized, raw_bound=raw)
        direct_good = direct_good and raw.l > L
    require('prefix direct '+str(L), prefix['direct_third'], third)
    cumulative, best_H, finite_best = I(0), None, None
    for H in range(1,L+1):
        if H > 1:
            a = H-1
            par = data['shift_parameters'][a-1]
            residual = L-a
            raw_shift = par['multiplier']*(par['Lambda_upper']*residual+2)
            selected_shift = smallest(I(residual), raw_shift)
            require('shift row '+str(si), data['shift_rows'][si], dict(L=L, a=a,
                residual=residual, raw_bound=raw_shift, selected_cap=selected_shift))
            require('strict shifted loss '+str(si), raw_shift.l > residual)
            shift_good = shift_good and raw_shift.l > residual
            cumulative += selected_shift
            si += 1
        T1 = cumulative/(L*H)
        terms = [V*V/H, V*T1]
        normalized2 = largest(*terms)
        raw = L*radical(normalized2,2,'difference '+str(di))
        ratio = raw/L
        if best is None or ratio.h < best['ratio'].h:
            best = dict(L=L,H=H,ratio=ratio)
        require('difference row '+str(di), data['difference_rows'][di], dict(L=L,H=H,
            shift_cap_sum=cumulative,T1=T1,squared_terms=terms,
            normalized_squared=normalized2,raw_bound=raw))
        require('strict difference loss '+str(di), raw.l > L)
        difference_good = difference_good and raw.l > L
        if finite_best is None or raw.h < finite_best.h:
            finite_best, best_H = raw,H
        di += 1
    selected = smallest(I(L),direct,finite_best)
    M = largest(M,selected)
    require('complete prefix '+str(L), prefix, dict(L=L,direct_third=third,
        best_difference_H=best_H,best_difference_bound=finite_best,selected_cap=selected))
prod_check('complete shifted cases', si == 32640, si, 32640)
prod_check('complete prefix H cases', di == 32896, di, 32896)
for name, val in [('every shifted Lemma 5 bound loses to absolute cap',shift_good),
                  ('every optimized d3 bound loses to absolute cap',direct_good),
                  ('every finite H bound loses to absolute cap',difference_good)]:
    prod_check(name,val,val,True)
prod_check('resulting all-prefix cap',M.l == M.h == 256,M,256)
require('summary', data['summary'], dict(all_shift_caps_trivial=shift_good,
    all_optimized_d3_caps_trivial=direct_good,all_finite_H_caps_trivial=difference_good,
    best_raw_normalized_difference=best,all_prefix_cap=M))

LOG2 = ln_unit(Q(2))
h, hn = ln(Q(n+1)), ln(Q(N))
d = sig-t*hn/2
prod_check('decreasing heat weight',d.l>0,d,'>0')
prod_check('decreasing logarithmic heat weight',(h*d).l>1,h*d,'>1')
argument = t*h*h/4-sig*h
w = I(exp(argument.l).l,exp(argument.h).h)
Scap, Lcap = M*w,M*h*w
BG = R*(Scap+2*(Lcap+J*Scap)/ell0)
logs = I(0)
for row in corner['prime_rows']:
    logs += row['log_p']
support = hn+logs
K = R*(Q(53,3)+256*w)*support
QX = X*(X*X+5)/(1+X*X)**2
CX = (7*X*X-5)/(1+X*X)**2
Us = t*(QX+CX)*K/ell0
Ur = R*eps/2+2*(D*eps+R*eps1)/ell0
total = BG+Us+Ur
prod_check('adequate total enclosure width',total.h-total.l < Q(1,10**30),total.h-total.l,'<1e-30')
prod_check('sufficient envelope fails strictly',total.l>r0,total,'>r0')
before_check = sum(ledger.values())
prod_check('cumulative operation cap respected',before_check+16<=2**25,before_check+16,2**25)
excess = total-r0
require('weights',data['weights'],dict(sigma_at_X=sig,log_first=h,log_N=hn,margin=d,
    first_weight=w,S_cap=Scap,L_cap=Lcap))
require('envelopes',data['envelopes'],dict(R0=R,J0=J,D0=D,full_output_log_cap=support,
    Lhat_cap=K,B_uniform=BG,U_s_uniform=Us,U_r_uniform=Ur,
    combined_cost=total,reserve=r0,excess=excess))
require('all elementary series records',data['elementary_evaluations'],elementary)
# The producer's range dictionary {lower:lambda, upper:Lambda} and an
# interval have the same exact JSON schema. Compare canonical encodings.
require('all producer check fields',enc(data['checks']),enc(reconstructed_checks))
require('producer failures',data['failures'],[])
require('result',data['result'],'ENVELOPE_FAIL')
require('recorded operation categories',data['operations']['charges'],ledger)
assembly_count = sum(ledger.values())
require('recorded assembly total',data['operations']['charged_scalar_upper_bound'],assembly_count)
require('required cap',data['operations']['required_cap'],2**25)
require('no refinements',data['operations']['precision_refinements'],0)
require('quoted total lower',total.l>Q('.00072254689054510978'))
require('quoted total upper',total.h<Q('.00072254689054510979'))
require('quoted excess',excess.l>Q('.00030005307467456650'))
require('quoted best ratio lower',best['ratio'].l>Q('1.48146535638109'))
require('quoted best ratio upper',best['ratio'].h<Q('1.48146535638110'))
require('inherited exact reserve',corner['bounds']['reserve_lower'],r0)
require('inherited exact corner parameters',corner['parameters'],dict(x=X,t=t,N=n,
    ell0=ell0,cap=Q('.500000000001'),epsilon=eps,epsilon_1=eps1,
    grid_denominator=str(10**50)))
require('small positive delta bound',0<dmax<Q('1e-12'))
for name,value,lower_text,upper_text in [
    ('lambda',I(lam),'.000002891124788659806773214336','.000002891124788659806773214337'),
    ('Lambda',I(upper),'.000002896492591979200986242150','.000002896492591979200986242151'),
    ('B_uniform',BG,'.00070171640076552016','.00070171640076552017')]:
    require('quoted '+name+' endpoints',Q(lower_text)<value.l<=value.h<Q(upper_text))
require('quoted U_s upper',Us.h<Q('1.254886146337842e-11'))
require('quoted U_r upper',Ur.h<Q('.000020830477230729'))
require('quoted reserve upper',r0<Q('.000422493815870544'))
# The producer recomputes total-r0 once after serialization for its print list.
# This is an additional interval subtraction (8+8+32), absent from its JSON.
executed_count = assembly_count+48
require('whole execution enclosure count below cap',executed_count<=2**25)

report = dict(result='PASS_WITH_RESOURCE_QUALIFICATION',failures=failures,
    scope='Independent saved-row audit only; manuscript source proofs remain qualified.',
    inputs=[dict(path=name,sha256=digest(BASE/name)) for name in
       ('third-derivative-entry-budget.json','third-derivative-entry-budget.py',
        'uniform-quadratic-curvature-budget.json','fixed-corner-two-charge.json',
        'c499c-certificate-audit.json')],
    counts=dict(prefixes=256,shift_rows=si,difference_rows=di,root_enclosures=len(roots),
                elementary_records=len(elementary),checks=len(evidence),**stats),
    domain=data['domain'],constants=data['constants'],weights=data['weights'],
    envelopes=data['envelopes'],best_normalized_difference=best,
    operations=dict(assembly_count=assembly_count,assembly_categories=ledger,
      post_serialization_enclosure_subtraction=48,whole_execution_upper_bound=executed_count,
      required_cap=2**25,cap_margin=2**25-executed_count,
      qualification='Printed excess is recomputed after JSON assembly; displayed ledger omits 48 charges. Serialization/hash/decimal formatting and bit complexity excluded.'),
    roots=roots,elementary_evaluations=elementary,checks=evidence,
    script_sha256=digest(Path(__file__)))
OUT.write_text(json.dumps(enc(report),separators=(',',':'))+'\n')
print('PASS_WITH_RESOURCE_QUALIFICATION: all 256 prefixes, 32640 shifts, 32896 differences checked')
print('assembly='+str(assembly_count)+'; whole enclosure execution<='+str(executed_count)+'; cap='+str(2**25))
print('total in (.00072254689054510978,.00072254689054510979); required <r0<.000422493815870544')
print('excess>.00030005307467456650; failures='+str(failures))
print('certificate='+str(OUT.relative_to(BASE.parent.parent)))
