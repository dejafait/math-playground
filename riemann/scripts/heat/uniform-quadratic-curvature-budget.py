#!/usr/bin/env python3
"""One approved uniform curvature/Abel envelope, including a negative budget.

Reuse only the arithmetic definitions of the audited endpoint producer.
Do not run that producer, rewrite its certificate, or treat this as an audit.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
import json
import types

HERE = Path(__file__).resolve().parent
OUT = HERE / 'uniform-quadratic-curvature-budget.json'
producer = HERE / 'phase-sensitive-256-block-certificate.py'
ar = types.ModuleType('retained_endpoint_arithmetic')
ar.__file__ = str(producer)
exec(compile(producer.read_text().split('\ndef run():')[0], str(producer), 'exec'), ar.__dict__)
B, read, enc = ar.Box, ar.read, ar.encode
checks, failures = [], []


def check(name, passed, actual, required):
    checks.append(dict(name=name, passed=bool(passed), actual=actual, required=required))
    if not passed:
        failures.append(name)


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


corner = json.loads((HERE/'fixed-corner-two-charge.json').read_text())
audit = json.loads((HERE/'l499-certificate-audit.json').read_text())
endpoint_audit = json.loads((HERE/'c499c-certificate-audit.json').read_text())
check('retained arithmetic source unchanged', digest(producer) == endpoint_audit['producer_sha256'],
      digest(producer), endpoint_audit['producer_sha256'])
for row in audit['inputs']:
    check('retained audited input '+row['path'], digest(HERE/row['path']) == row['sha256'],
          digest(HERE/row['path']), row['sha256'])
check('corner linkage', any(row['path'] == 'fixed-corner-two-charge.json' and
      row['sha256'] == digest(HERE/row['path']) for row in audit['inputs']),
      digest(HERE/'fixed-corner-two-charge.json'), 'retained audit input')

t, X, n, N = F('.16836'), F('6000284561421.5'), 691004, 691260
ell0, eps = F('24.18022820120389'), F('.0000006')
eps1 = (eps+F('.0000013'))*F('8.770232')/F('.14142')
r0 = F(14176540015048665224252705167939023,
       33554432000000000000000000000000000000)
pi = read(corner['elementary_inputs']['pi'])
sig = read(corner['elementary_inputs']['sigma'])
LX = read(corner['elementary_inputs']['L'])
R, J, D = [read(corner['bounds'][k]) for k in ('R', 'Jplus', 'product_derivative_cap')]
check('exact inherited reserve', ar.rat(corner['bounds']['reserve_lower']) == r0,
      ar.rat(corner['bounds']['reserve_lower']), r0)
check('exact inherited parameters', corner['parameters'] == enc(dict(
      x=X, t=t, N=n, ell0=ell0, cap=F('.500000000001'), epsilon=eps,
      epsilon_1=eps1, grid_denominator=str(10**50))), corner['parameters'], 'specified corner')
ar.LOG2 = ar.log_unit(F(2))
Y = 4*pi*(N*N-t/16)
domain = t*(LX+(Y-X)/X)
check('closed domain', Y.lo > X and domain.hi < F('5.17'), domain, '<5.17 and Y>X')
cn, cn1 = 4*pi*(n*n-t/16), 4*pi*((n+1)**2-t/16)
check('initial canonical cell', cn.hi <= X < cn1.lo, dict(left=cn, X=X, right=cn1), 'left<=X<right')

# delta(x) < 7t/(8*pi*X), since atan(1/x)<1/x and x/(1+x*x)<1/x.
dmax = (7*t/(8*pi*X)).hi
check('small positive delta cap', 0 < dmax < F(1, 10**12), dmax, '(0,1e-12)')
Lambda = F((N+1)**2, n*n)-1
LambdaY = F(N*N, n*n)-1
A = (2/ar.sqrt_box(pi))*(1+ar.sqrt_box(1+3*pi/8))
split_rows = []
for r in range(1, 256):
    lam = (F(N*N)-dmax)/(N-r)**2-1
    check('positive lower curvature '+str(r), lam > 0, lam, '>0')
    C = A/ar.sqrt_box(B(lam))
    raw = r+C*(Lambda*(256-r)+2)
    endpoint_raw = r+C*(LambdaY*(256-r)+2)
    check('uniform split loses '+str(r), raw.lo > 256, raw, '>256')
    check('endpoint split also loses '+str(r), endpoint_raw.lo > 256, endpoint_raw, '>256')
    split_rows.append(dict(tail=r, smooth_length=256-r, lambda_lower=lam,
                           uniform_raw_bound=raw, endpoint_raw_bound=endpoint_raw,
                           affine_prefix_intercept=2*C))
best = min(split_rows, key=lambda row: row['uniform_raw_bound'].hi)
best_endpoint = min(split_rows, key=lambda row: row['endpoint_raw_bound'].hi)

h = ar.log_exact(F(n+1))
hn = ar.log_exact(F(N))
# Uniformity in x comes from sigma(x)>=sigma(X); in the weight variable
# sigma(X)-t*log(u)/2>=d>0 and log(u)*d>1 imply w and log(u)w decrease.
d = sig-t*hn/2
check('heat weight decreasing', d.lo > 0, d, '>0')
check('log weight decreasing', (h*d).lo > 1, h*d, '>1')
wfirst = ar.exp_box(t*h*h/4-sig*h)
Sprefix = 256*wfirst
Lprefix = 256*h*wfirst
BG = R*(Sprefix+2*(Lprefix+J*Sprefix)/ell0)
sumlogs = B(0)
prime_rows = corner['prime_rows']
for row in prime_rows:
    sumlogs += read(row['log_p'])
support = hn+sumlogs
K = R*(F(53, 3)+Sprefix)*support
QX = X*(X*X+5)/(1+X*X)**2
CX = (7*X*X-5)/(1+X*X)**2
Us = t*(QX+CX)*K/ell0
Ur = R*eps/2+2*(D*eps+R*eps1)/ell0
total = BG+Us+Ur
check('budget failure is resolved', total.lo > r0, total, '>r0 (failure of this envelope)')
check('adequate enclosure width', total.hi-total.lo < F(1, 10**30),
      total.hi-total.lo, '<1e-30')
report = dict(
    result='ENVELOPE_FAIL' if not failures and total.lo > r0 else 'CHECK_FAILURE',
    scope='One uniform quadratic-curvature/absolute-tail/Abel envelope; not actual increment failure',
    independent_audit=False,
    parameters=dict(t=t, X=X, n=n, N=N, ell0=ell0, epsilon=eps, epsilon_1=eps1, r0=r0),
    inputs=[dict(path=p.name, sha256=digest(p)) for p in
            (producer, HERE/'fixed-corner-two-charge.json', HERE/'l499-certificate-audit.json',
             HERE/'c499c-certificate-audit.json')],
    arithmetic_reuse='Definitions before def run() only; no producer execution',
    domain=dict(Y=Y, t_log_upper=domain, initial_left=cn, initial_right=cn1,
                cells=list(range(n,N+1)), last_cell='singleton Y; earlier cells right-open',
                derivative='freeze canonical q independently at every centre'),
    derivative=dict(delta_upper=dmax, global_Lambda=Lambda, endpoint_Lambda=LambdaY,
                    theorem_constant=A, split_rows=split_rows,
                    best_uniform=best, best_endpoint=best_endpoint,
                    all_prefix_cap=256,
                    prefix_reason='raw(m,r)-m is affine in m; positive at m=r and m=256'),
    weights=dict(sigma_at_X=sig, log_first=h, log_N=hn, derivative_margin=d,
                 first_weight_at_X=wfirst, S_cap=Sprefix, L_cap=Lprefix),
    envelopes=dict(R0=R,J0=J,D0=D,full_output_log_cap=support,Lhat_cap=K,
                   B_uniform=BG, U_s_uniform=Us, U_r_uniform=Ur,combined_cost=total,
                   reserve=r0,excess=total-r0),
    mathematical_budget_failures=['B_uniform+U_s_uniform+U_r_uniform<r0 is not certified'],
    checks=checks, failures=failures, elementary_evaluations=ar.evaluations,
    script_sha256=digest(Path(__file__)))
OUT.write_text(json.dumps(enc(report),indent=2)+'\n')


def dec(v, upper=True):
    with localcontext() as ctx:
        ctx.prec=25
        ctx.rounding=ROUND_CEILING if upper else ROUND_FLOOR
        return str(Decimal(v.numerator)/Decimal(v.denominator))


print(f"{report['result']}: {len(checks)} checks; implementation failures={failures}")
for name, v in [('best_uniform_curvature_plus_tail',best['uniform_raw_bound']),
                ('best_endpoint_curvature_plus_tail',best_endpoint['endpoint_raw_bound']),
                ('B_uniform',BG),('U_s_uniform',Us),('U_r_uniform',Ur),('combined_cost',total)]:
    print(f'{name} in [{dec(v.lo,False)}, {dec(v.hi)}]')
print('required combined_cost < '+dec(r0,False))
print('mathematical failure: explicit envelope exceeds reserve; actual increment unresolved')
print('certificate='+str(OUT.relative_to(HERE.parent.parent)))
raise SystemExit(bool(failures))
