#!/usr/bin/env python3
"""One capped all-prefix third-derivative/single-difference budget test.

Reuses retained endpoint arithmetic definitions and C499d's input certificate;
never executes earlier producers. Not an independent arithmetic/source audit.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
import json
import types

HERE = Path(__file__).resolve().parent
OUT = HERE/'third-derivative-entry-budget.json'
CAP = 2**25
used = 4096  # conservative allowance for fixed exact-rational setup/formulas
counts = {'fixed_rational_setup': used}


def charge(kind, amount):
    global used
    if used+amount > CAP:
        raise RuntimeError('fixed cumulative scalar-operation cap exhausted')
    used += amount
    counts[kind] = counts.get(kind, 0)+amount


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


producer = HERE/'phase-sensitive-256-block-certificate.py'
ar = types.ModuleType('retained_arithmetic')
ar.__file__ = str(producer)
exec(compile(producer.read_text().split('\ndef run():')[0], str(producer), 'exec'), ar.__dict__)
B, read, enc = ar.Box, ar.read, ar.encode
# Overcount each method's direct endpoint rational operations, including
# comparisons/rounding. Nested calls charge again. No timing/proxy counters.
for name, cost in [('__add__', 32), ('__neg__', 8), ('__sub__', 8),
                   ('__mul__', 48), ('__truediv__', 32)]:
    original = getattr(B, name)
    def wrapped(self, other=None, _f=original, _n=name, _c=cost):
        charge(_n, _c)
        return _f(self) if _n == '__neg__' else _f(self, other)
    setattr(B, name, wrapped)
B.__radd__, B.__rmul__ = B.__add__, B.__mul__
for name, overhead in [('sqrt_box', 64), ('log_unit', 4096),
                       ('log_exact', 1024), ('exp_exact', 4096)]:
    original = getattr(ar, name)
    def wrapped(a, _f=original, _n=name, _c=overhead):
        charge(_n, _c)
        return _f(a)
    setattr(ar, name, wrapped)


def root_integer(v, k):
    lo, hi = 0, 1 << ((v.bit_length()+k-1)//k)
    while lo+1 < hi:
        charge('root_integer_iteration', 16*k)
        mid = (lo+hi)//2
        if mid**k <= v:
            lo = mid
        else:
            hi = mid
    return lo


def root(a, k):
    if a.lo < 0:
        raise ValueError('negative root operand')
    charge('root_endpoint_setup', 64*k)
    scale = ar.GRID**k
    lo = root_integer(a.lo.numerator*scale//a.lo.denominator, k)
    hi = root_integer(a.hi.numerator*scale//a.hi.denominator, k)+1
    return B(F(lo, ar.GRID), F(hi, ar.GRID))


def minimum(*values):
    charge('interval_minimum', 8*len(values))
    return B(min(v.lo for v in values), min(v.hi for v in values))


def maximum(*values):
    charge('interval_maximum', 8*len(values))
    return B(max(v.lo for v in values), max(v.hi for v in values))


checks, failures = [], []


def check(name, passed, actual, required):
    charge('check', 16)
    checks.append(dict(name=name, passed=bool(passed), actual=actual, required=required))
    if not passed:
        failures.append(name)


prior_path = HERE/'uniform-quadratic-curvature-budget.json'
prior = json.loads(prior_path.read_text())
corner = json.loads((HERE/'fixed-corner-two-charge.json').read_text())
endpoint_audit = json.loads((HERE/'c499c-certificate-audit.json').read_text())
check('arithmetic definitions unchanged', digest(producer) == endpoint_audit['producer_sha256'],
      digest(producer), endpoint_audit['producer_sha256'])
check('prior envelope completed', prior['result'] == 'ENVELOPE_FAIL' and not prior['failures'],
      prior['result'], 'ENVELOPE_FAIL with no implementation failures')
for row in prior['inputs']:
    check('retained input '+row['path'], digest(HERE/row['path']) == row['sha256'],
          digest(HERE/row['path']), row['sha256'])

t, X, n, N = F('.16836'), F('6000284561421.5'), 691004, 691260
ell0, eps = F('24.18022820120389'), F('.0000006')
eps1 = (eps+F('.0000013'))*F('8.770232')/F('.14142')
r0 = F(14176540015048665224252705167939023,
       33554432000000000000000000000000000000)
check('exact parameters', prior['parameters'] == enc(dict(t=t, X=X, n=n, N=N,
      ell0=ell0, epsilon=eps, epsilon_1=eps1, r0=r0)), prior['parameters'], 'specified target')
pi = read(corner['elementary_inputs']['pi'])
sig = read(corner['elementary_inputs']['sigma'])
LX = read(corner['elementary_inputs']['L'])
R, J, D = [read(corner['bounds'][key]) for key in ('R', 'Jplus', 'product_derivative_cap')]
Y = 4*pi*(N*N-t/16)
domain = t*(LX+(Y-X)/X)
cn, cn1 = 4*pi*(n*n-t/16), 4*pi*((n+1)**2-t/16)
check('closed analytic domain', Y.lo > X and domain.hi < F('5.17'), domain, '<5.17; Y>X')
check('initial floor cell', cn.hi <= X < cn1.lo, dict(left=cn, right=cn1), 'left<=X<right')
dmax = (7*t/(8*pi*X)).hi
lam = 2*(F(n*n)-dmax)/N**3
upper = F(2*(N+1)**2, n**3)
check('positive global third derivative range', 0 < lam <= upper,
      dict(lower=lam, upper=upper), '0<lambda<=Lambda')

A = (2/ar.sqrt_box(pi))*(1+ar.sqrt_box(1+3*pi/8))
V = 2+2*ar.sqrt_box(B(2))
A3 = V*ar.sqrt_box(B(2))
B3 = V*root(F(81, 8)*F(2, 3)**6*4*A*A/(V*V), 6)
C3 = V*ar.sqrt_box(8*A/V)
constant_term = B3*root(B(upper*upper/lam), 6)
shift_parameters = []
for a in range(1, 256):
    charge('shift_rational_setup', 32)
    la, ua = a*lam, a*upper
    shift_parameters.append(dict(a=a, lambda_lower=la, Lambda_upper=ua,
                                 multiplier=A/ar.sqrt_box(B(la))))

prefix_rows, shift_rows, difference_rows = [], [], []
all_shift_trivial, all_d3_trivial, all_H_trivial = True, True, True
best_raw_ratio = None
M = B(0)
for L in range(1, 257):
    # Theorem 11: integer L>3; otherwise only the absolute bound is used.
    direct, third_data = B(L), None
    if L >= 4:
        charge('third_rational_setup', 64)
        terms = [A3*root(B(upper/(lam*L)), 4), constant_term,
                 C3/root(B(lam*L**3), 4)]
        normalized = maximum(*terms)
        raw = L*normalized
        direct = minimum(B(L), raw)
        third_data = dict(terms=terms, normalized=normalized, raw_bound=raw)
        all_d3_trivial = all_d3_trivial and raw.lo > L
    cumulative = B(0)
    finite_best, best_H = None, None
    for H in range(1, L+1):
        if H > 1:
            a = H-1
            par = shift_parameters[a-1]
            residual = L-a
            raw_shift = par['multiplier']*(par['Lambda_upper']*residual+2)
            shift_cap = minimum(B(residual), raw_shift)
            all_shift_trivial = all_shift_trivial and raw_shift.lo > residual
            cumulative += shift_cap
            shift_rows.append(dict(L=L, a=a, residual=residual,
                                   raw_bound=raw_shift, selected_cap=shift_cap))
        T1 = cumulative/(L*H)
        # Squaring Theorem 7 gives max{V^2/H,V*T1}. Both are nonnegative.
        squared_terms = [V*V/H, V*T1]
        normalized_squared = maximum(*squared_terms)
        raw_difference = L*ar.sqrt_box(normalized_squared)
        ratio = raw_difference/L
        if best_raw_ratio is None or ratio.hi < best_raw_ratio['ratio'].hi:
            best_raw_ratio = dict(L=L, H=H, ratio=ratio)
        all_H_trivial = all_H_trivial and raw_difference.lo > L
        if finite_best is None or raw_difference.hi < finite_best.hi:
            finite_best, best_H = raw_difference, H
        difference_rows.append(dict(L=L, H=H, shift_cap_sum=cumulative, T1=T1,
                                    squared_terms=squared_terms,
                                    normalized_squared=normalized_squared,
                                    raw_bound=raw_difference))
    selected = minimum(B(L), direct, finite_best)
    M = maximum(M, selected)
    prefix_rows.append(dict(L=L, direct_third=third_data,
                            best_difference_H=best_H, best_difference_bound=finite_best,
                            selected_cap=selected))

check('complete shifted cases', len(shift_rows) == 32640, len(shift_rows), 32640)
check('complete prefix H cases', len(difference_rows) == 32896, len(difference_rows), 32896)
check('every shifted Lemma 5 bound loses to absolute cap', all_shift_trivial,
      all_shift_trivial, True)
check('every optimized d3 bound loses to absolute cap', all_d3_trivial, all_d3_trivial, True)
check('every finite H bound loses to absolute cap', all_H_trivial, all_H_trivial, True)
check('resulting all-prefix cap', M.lo == M.hi == 256, M, 256)

ar.LOG2 = ar.log_unit(F(2))
h, hn = ar.log_exact(F(n+1)), ar.log_exact(F(N))
d = sig-t*hn/2
check('decreasing heat weight', d.lo > 0, d, '>0')
check('decreasing logarithmic heat weight', (h*d).lo > 1, h*d, '>1')
wfirst = ar.exp_box(t*h*h/4-sig*h)
S_cap, L_cap = M*wfirst, M*h*wfirst
BG = R*(S_cap+2*(L_cap+J*S_cap)/ell0)
sumlogs = B(0)
for row in corner['prime_rows']:
    sumlogs += read(row['log_p'])
support = hn+sumlogs
K = R*(F(53, 3)+256*wfirst)*support  # charges use absolute, not cancellation mass
QX = X*(X*X+5)/(1+X*X)**2
CX = (7*X*X-5)/(1+X*X)**2
Us = t*(QX+CX)*K/ell0
Ur = R*eps/2+2*(D*eps+R*eps1)/ell0
total = BG+Us+Ur
check('adequate total enclosure width', total.hi-total.lo < F(1, 10**30),
      total.hi-total.lo, '<1e-30')
check('sufficient envelope fails strictly', total.lo > r0, total, '>r0')
check('cumulative operation cap respected', used+16 <= CAP, used+16, CAP)
result = 'ENVELOPE_FAIL' if not failures else 'CHECK_FAILURE'
report = dict(result=result, independent_audit=False,
    scope='One uniform third-derivative/single-difference envelope; no true-cost lower bound',
    parameters=dict(t=t, X=X, n=n, N=N, ell0=ell0, epsilon=eps, epsilon_1=eps1, r0=r0),
    inputs=[dict(path=p.name, sha256=digest(p)) for p in
            (producer, prior_path, HERE/'fixed-corner-two-charge.json',
             HERE/'c499c-certificate-audit.json')],
    domain=dict(Y=Y, initial_left=cn, initial_right=cn1, analytic_test=domain,
                delta_upper=dmax, a_lower=n*n-dmax, a_upper=(N+1)**2,
                lambda_lower=lam, Lambda_upper=upper,
                shifted_domain='n<u<=n+L-a; 0<=v<=a; n<u+v<=n+L<=N',
                cutoff='[X,C_(n+1)); [C_q,C_(q+1)); singleton Y, with canonical left equality'),
    constants=dict(A=A, B=V, A3=A3, B3=B3, C3=C3),
    shift_parameters=shift_parameters, shift_rows=shift_rows,
    difference_rows=difference_rows, prefix_rows=prefix_rows,
    summary=dict(all_shift_caps_trivial=all_shift_trivial,
                 all_optimized_d3_caps_trivial=all_d3_trivial,
                 all_finite_H_caps_trivial=all_H_trivial,
                 best_raw_normalized_difference=best_raw_ratio, all_prefix_cap=M),
    weights=dict(sigma_at_X=sig, log_first=h, log_N=hn, margin=d, first_weight=wfirst,
                 S_cap=S_cap, L_cap=L_cap),
    envelopes=dict(R0=R, J0=J, D0=D, full_output_log_cap=support, Lhat_cap=K,
                   B_uniform=BG, U_s_uniform=Us, U_r_uniform=Ur,
                   combined_cost=total, reserve=r0, excess=total-r0),
    operations=dict(charged_scalar_upper_bound=used, required_cap=CAP, charges=counts,
                    convention='Conservative rational-endpoint operation upper charges per method; nested calls counted again. Fixed formulas charged 4096; serialization/hashes are not enclosure operations.',
                    precision_refinements=0),
    checks=checks, failures=failures, elementary_evaluations=ar.evaluations,
    script_sha256=digest(Path(__file__)))
OUT.write_text(json.dumps(enc(report), separators=(',', ':'))+'\n')


def dec(q, upper=True):
    with localcontext() as ctx:
        ctx.prec = 25
        ctx.rounding = ROUND_CEILING if upper else ROUND_FLOOR
        return str(Decimal(q.numerator)/Decimal(q.denominator))


print(f'{result}: prefixes=256, shifted cases={len(shift_rows)}, H cases={len(difference_rows)}')
print(f'charged scalar operations<={used}; required cap={CAP}; failures={failures}')
print('all-prefix cap=256; all three families retain trivial caps')
for name, value in [('lambda', B(lam)), ('Lambda', B(upper)),
                    ('best_raw_difference_ratio', best_raw_ratio['ratio']),
                    ('B_uniform', BG), ('U_s_uniform', Us), ('U_r_uniform', Ur),
                    ('combined_cost', total), ('excess', total-r0)]:
    print(f'{name} in [{dec(value.lo, False)}, {dec(value.hi)}]')
print('required combined_cost < '+dec(r0, False))
print('certificate='+str(OUT.relative_to(HERE.parent.parent)))
raise SystemExit(bool(failures))
