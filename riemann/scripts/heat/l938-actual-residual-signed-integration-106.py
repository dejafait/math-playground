#!/usr/bin/env python3
"""One approved fixed weighted quadrature. Full evidence stays beside script."""
import hashlib
import importlib.util
import json
import sys
from decimal import Decimal, InvalidOperation, Overflow, Underflow, Subnormal, DivisionByZero
from fractions import Fraction as F
from math import factorial, prod
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE / 'l938-actual-residual-signed-integration-106.json'
NODES = BASE / 'l938-actual-residual-nodes-106.json'
report = dict(status='IN_PROGRESS', inputs_sha256={}, checks=[], failures=[],
              qualification='Inherited theta, exact derivative-prefix, full-polynomial '
              'and directed Decimal/exponential execution contracts persist.')


def save():
    OUT.write_text(json.dumps(report, indent=2)+'\n')


def check(name, condition):
    report['checks'].append(dict(name=name, passed=bool(condition)))
    if not condition:
        report['failures'].append(name)
        report['status'] = 'ARITHMETIC_FAILURE'
        save()
        raise AssertionError(name)


def read(name):
    raw = (BASE/name).read_bytes()
    report['inputs_sha256'][name] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


save()
lib = load('fixed_interval106', BASE.parent/'hankel/certify_hankel.py')
for ctx in (lib.DOWN, lib.UP, lib.NEAR):
    ctx.prec = 200
    ctx.clear_flags()
I, DOWN, UP = lib.I, lib.DOWN, lib.UP
kernel = read('actual-h2-energy-cell-48.json')
prefix = read('l938-signed-response-coefficients-89.json')
prefix_producer = read('l938-signed-response-89.json')
point = read('l938-pointwise-signed-response-104.json')
point_check = read('l938-pointwise-signed-response-check-104.json')
for name, obj in [('prefix89', prefix_producer), ('endpoint104', point),
                  ('endpoint check104', point_check)]:
    check(name+' full flags', len(obj['checks']) > 0 and not obj['failures']
          and all(c['passed'] is True for c in obj['checks']))
check('exact saved prefix hash', report['inputs_sha256']['l938-signed-response-coefficients-89.json']
      == prefix_producer['coefficient_sha256'])
check('kernel identity89', report['inputs_sha256']['actual-h2-energy-cell-48.json']
      == prefix_producer['inputs_sha256']['actual-h2-energy-cell-48.json'])
check('kernel identity104', report['inputs_sha256']['actual-h2-energy-cell-48.json']
      == point['inputs_sha256']['actual-h2-energy-cell-48.json'])
ap = kernel['approximation']
G, J, n = 10**120, 1411, 4096
check('fixed scope', (ap['degree'], ap['nodes'], ap['theta_terms'], ap['precision'])
      == (256,257,8,200) and int(ap['chebyshev_denominator']) == G
      and prefix['cut'] == J and prefix['full_degree'] == 2816)
pi_lo, pi_hi = F(ap['pi']['lower']), F(ap['pi']['upper'])
pi = I(ap['pi']['lower'], ap['pi']['upper'])
epsilon = F(ap['epsilon'])
check('full epsilon retained', epsilon == F(point['exact']['epsilon']))
C = int(prefix['C'])
check('C normalization', C == 2*factorial(12)*int(ap['power_denominator'])*4**262)
grad = [list(map(int, row)) for row in prefix['gradients']]
check('all exact signed prefix entries', len(grad) == 7 and all(len(row)==J+1 for row in grad))
odd = [1]
for h in range(1,18+J):
    odd.append(odd[-1]*(2*h-1))
trows = []
for k, row in enumerate(grad):
    converted = []
    for l, d in enumerate(row):
        h = 17-k+l
        exact = F(d*2**(h+3*l), 2*C**11*factorial(2*k)*odd[h])
        interval = I.rational(exact)
        check('response rational inclusion '+str(k)+','+str(l),
              F(interval.lo) <= exact <= F(interval.hi))
        converted.append(interval)
    trows.append(converted)
cheb = [I.rational(F(int(c['chosen_numerator']),G)) for c in ap['chebyshev_coefficients']]
check('all unchanged Chebyshev coefficients', len(cheb)==257)


def positive_horner(row, x):
    """Exact interval recurrence specialized only to x>=0."""
    if x.lo < 0:
        raise ArithmeticError('positive Horner argument')
    lo, hi = row[-1].lo, row[-1].hi
    for c in reversed(row[:-1]):
        lo = DOWN.add(DOWN.multiply(lo, x.lo if lo >= 0 else x.hi), c.lo)
        hi = UP.add(UP.multiply(hi, x.hi if hi >= 0 else x.lo), c.hi)
    return I(lo,hi)


# Full analytic amplitude majorant on the prescribed complex ellipse.
rho, a = F(3,2), F(25,24)
pmajor = sum((abs(F(int(c['chosen_numerator']),G))*rho**l
              for l,c in enumerate(ap['chebyshev_coefficients'])),F(0))
abs_sums = []
for row in trows:
    value = positive_horner([I(c.magnitude()) for c in row], I.rational(a))
    abs_sums.append(F(value.hi))
M = a**17*(10**9+pmajor)*sum(abs_sums,F(0))
delta = 2*M*F(2,3)**8191/(rho-1)
quadrature_error = 2*pi_hi**6*8**17*delta
complement = epsilon*pi_hi**6*F(point['exact']['complement_norm'])
second = F(point['exact']['second_order_upper'])
vp_lo, vp_hi = (F(point['exact']['polynomial_endpoint_'+s]) for s in ('lower','upper'))
check('positive complete analytic payments', 0 < quadrature_error and 0 < complement and 0 < second)
report['analytic'] = {k:str(v) for k,v in dict(rho=rho, ellipse_y_radius=a,
    polynomial_majorant=pmajor, amplitude_majorant=M, projection_error=delta,
    quadrature_error=quadrature_error, complement=complement, second_order=second,
    polynomial_endpoint_lower=vp_lo,polynomial_endpoint_upper=vp_hi).items()}
report['analytic']['response_absolute_sum_bounds'] = list(map(str,abs_sums))
report['settings'] = dict(integration_nodes=n, projection_degree=8191,
    response_prefix=J, precision=200, interpolation_nodes=257, theta_terms=8,
    coefficient_grid=str(G), energy=8)
save()
print('Complete ellipse majorant constructed; fixed analytic error below endpoint:',
      quadrature_error < vp_lo, flush=True)
if quadrature_error >= vp_lo:
    report['status']='FIXED_TEST_ENDED_EXCESSIVE_ANALYTIC_ERROR'
    save()
    print('Actual error:', float(quadrature_error), '; required <', float(vp_lo), '; path:',OUT)
    sys.exit(0)

cosine_error = F(ap['cosine_remainder'])
tail = F(ap['full_theta_tail_bound'])
cos_coeff = [I.rational(F((-1)**r,factorial(2*r))) for r in range(129)]
cos_error = I.rational(cosine_error).hi


def cosine(theta):
    check('cosine argument '+str(len(nodes)), 0 <= theta.lo <= theta.hi <= 4)
    value = positive_horner(cos_coeff,theta*theta)
    return value+I(cos_error.copy_negate(),cos_error)


def polynomial(z):
    # Clenshaw for sum d_l T_l(z), with exactly the saved rational d_l.
    b1, b2 = I(0), I(0)
    for c in reversed(cheb[1:]):
        b0 = c+2*z*b1-b2
        b2,b1 = b1,b0
    return cheb[0]+z*b1-b2


nodes, total = [], I(0)
for j in range(n):
    theta = pi*I.rational(F(2*j+1,2*n))
    z = cosine(theta)
    y = (1+z)/2
    x = 8*(1-y)
    check('node interior '+str(j), 0 < y.lo <= y.hi < 1 and 0 < x.lo <= x.hi < 8)
    root_lo = lib.NEAR.next_minus(lib.NEAR.sqrt(x.lo))
    root_hi = lib.NEAR.next_plus(lib.NEAR.sqrt(x.hi))
    check('exact sqrt squares '+str(j), 0 <= F(root_lo)**2 <= F(x.lo)
          and F(root_hi)**2 >= F(x.hi) and root_hi < 3)
    u = I(root_lo,root_hi)
    e2, eh = (2*u).exp(),(u/2).exp()
    kval = I(0)
    for q in range(1,9):
        v = pi*(q*q)*e2
        kval += eh*(8*v*v-12*v)*(-v).exp()
    kval += I(0,I.rational(tail).hi)
    pval = polynomial(-z)
    residual = kval-pval
    fk = [positive_horner(row,y) for row in trows]
    response = sum((y**(6-k)*(1-y)**k*fk[k] for k in range(7)),I(0))
    amplitude = y**11*residual*response
    total += amplitude
    nodes.append(dict(j=j,theta=theta.data(),z=z.data(),y=y.data(),energy=x.data(),
        sqrt_energy=u.data(),kernel=kval.data(),polynomial=pval.data(),residual=residual.data(),
        response_rows=[v.data() for v in fk],response=response.data(),amplitude=amplitude.data(),
        running_sum=total.data()))
    if (j+1)%256==0:
        NODES.write_text(json.dumps(dict(status='IN_PROGRESS',nodes=nodes),indent=2)+'\n')
        report['completed_nodes']=j+1
        save()
        print('Enclosed nodes:',j+1,'/',n,flush=True)

quad = pi**6*I.rational(F(8**17,n))*total
payment = quadrature_error+complement+second
actual_lo = vp_lo+F(quad.lo)-payment
actual_hi = vp_hi+F(quad.hi)+payment
check('complete ordered enclosure', actual_lo <= actual_hi)
for name,ctx in [('DOWN',DOWN),('UP',UP),('NEAR',lib.NEAR)]:
    check('no forbidden arithmetic flags '+name, all(not ctx.flags[signal] for signal in
          (InvalidOperation,Overflow,Underflow,Subnormal,DivisionByZero)))
sign = 'POSITIVE' if actual_lo>0 else 'NEGATIVE' if actual_hi<0 else 'INCONCLUSIVE'
report['result'] = dict(signed_sum=total.data(),signed_quadrature=quad.data(),
    total_external_payment=str(payment),actual_lower=str(actual_lo),actual_upper=str(actual_hi),
    sign=sign,strict_positive_test=actual_lo>0,
    mathematical_failures=[] if sign!='INCONCLUSIVE' else ['Complete enclosure contains zero; fixed test ends.'])
report['status']='COMPLETED_CONDITIONAL_'+sign
NODES.write_text(json.dumps(dict(status='COMPLETE',nodes=nodes),indent=2)+'\n')
report['nodes_sha256']=hashlib.sha256(NODES.read_bytes()).hexdigest()
report['producer_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
save()


def display(value):
    return I.rational(value).data()


print(json.dumps(dict(status=report['status'],checks=len(report['checks']),failures=report['failures'],
    signed_quadrature=quad.data(),external_payment=display(payment),actual_lower=display(actual_lo),
    actual_upper=display(actual_hi),required_lower='>0',certificate=str(OUT),nodes=str(NODES)),indent=2))
