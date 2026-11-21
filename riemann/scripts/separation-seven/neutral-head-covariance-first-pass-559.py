#!/usr/bin/env python3
"""One fixed N512/K65536 endpoint-family test; assessment558.

Full finite weighted residual covariance, structured analytic infinite tail,
and verified finite factor/solve ledgers. No allocation or resolution search.
Analytic and IEEE754/Decimal contracts of C744v/w remain hypotheses.
"""
import hashlib
import importlib.util
import json
import sys
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
N, K, F, E = 512, 65536, 510, 1020


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


iv = load('interval559', BASE/'complete-schur-531.py')
iv.DOWN = Context(prec=80, rounding=ROUND_FLOOR)
iv.UP = Context(prec=80, rounding=ROUND_CEILING)
iv.NEAR = Context(prec=80, rounding=ROUND_HALF_EVEN)
I = iv.I
old = load('entries559', BASE/'residual-certificate-532.py')
checks, failures, ledger, factors = [], [], {}, {}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok:
        failures.append(label)


def fro(a):
    return float(np.linalg.norm(a))


def ab(x):
    return max(x.lo.copy_abs(), x.hi.copy_abs())


def sq(x):
    if x.lo <= 0 <= x.hi:
        return I(0, iv.UP.multiply(ab(x), ab(x)))
    return x*x


def powi(x, n):
    ans = I(1)
    for _ in range(n):
        ans *= x
    return ans


def atan(q):
    x = I(1)/q
    a = sum(((-1)**j*powi(x, 2*j+1)/(2*j+1) for j in range(80)), I(0))
    err = powi(x, 161)/161
    return a+I(err.hi.copy_negate(), err.hi)


def upper_float(x):
    return float(np.nextafter(float(x.hi), np.inf))


def positive(label, matrix):
    """Certify a proposed PSD factor with a separate 1e-6 ledger.

    The caller pays this operator allowance when using positivity.
    All factors are saved, including an unsuccessful proposed factor.
    """
    try:
        ff = np.linalg.cholesky(matrix)
        residual = fro(matrix-ff@ff.T)
        nf = fro(ff)**2
        maximum = float(np.max(np.abs(matrix)))
        ok = residual < 1e-7 and nf < 100000 and maximum < 400
        factors[label] = ff
        ledger[label] = dict(reconstruction_fro_float=residual,
            factor_fro_squared_float=nf, maximum_entry=maximum,
            operator_allowance='1e-6', proposed=True)
        check(ok, 'factor reconstruction '+label)
        return ok
    except np.linalg.LinAlgError:
        ledger[label] = dict(proposed=False, operator_allowance='1e-6')
        check(False, 'factor reconstruction '+label)
        return False


# Audited inputs are reused; no old certificate is regenerated or overwritten.
audit534 = json.loads((BASE/'certificate-audit-534.json').read_text())
audit548 = json.loads((BASE/'response-prefix-audit-548.json').read_text())
audit557 = json.loads((BASE/'fixed-block-metric-audit-557.json').read_text())
fixed = json.loads((BASE/'fixed-block-metric-555.json').read_text())
pins = {}
for name, expected in [
    ('complete-covariance-532.npz', audit534['original_sha256']['complete-covariance-532.npz']),
    ('residual-certificate-532.py', audit534['original_sha256']['residual-certificate-532.py']),
    ('complete-schur-531.py', audit534['original_sha256']['complete-schur-531.py']),
    ('response-prefix-remote-546.npz', audit548['input_hashes']['response-prefix-remote-546.npz'])]:
    pins[name] = sha(BASE/name)
    check(pins[name] == expected, 'audited hash '+name)
for name, data in [('534', audit534), ('548', audit548), ('557', audit557)]:
    check(not data['failures'], 'inherited failures empty '+name)
for name in ['certificate-audit-534.json', 'response-prefix-audit-548.json',
             'fixed-block-metric-audit-557.json', 'fixed-block-metric-555.json']:
    pins[name] = sha(BASE/name)

pi, ell = 16*atan(5)-4*atan(239), I(3).ln()/2
k2 = [sq(n*pi/ell) for n in range(N)]
z = np.eye(N)[:, 2:]
ratios, ratio_error, ratio_sq = [], I(0), [I(0), I(0)]
for n in range(2, N):
    p = n % 2
    r = (I('.25')+k2[p])/(I('.25')+k2[n])
    if p == 0:
        r *= I(2).sqrt()
    rf = float(iv.NEAR.divide(iv.NEAR.add(r.lo, r.hi), Decimal(2)))
    z[p, n-2] = -rf
    ratio_error += I(ab(r-I(Decimal(rf))))
    ratio_sq[p] += sq(r)
    ratios.append(r.json())
check(ratio_error.hi < Decimal('1e-14'), 'entire neutral basis conversion <1e-14')
zn = I('1.008')
check((1+max(ratio_sq, key=lambda q: q.hi)).sqrt().hi < zn.lo,
      'exact neutral basis operator norm <1.008')

with np.load(BASE/'complete-covariance-532.npz') as d:
    m0, t0, cov = d['m0'], d['mc']+d['mg'], d['cov00']
with np.load(BASE/'response-prefix-remote-546.npz') as d:
    remote = d['remote_prime']
check(max(float(np.max(np.abs(q))) for q in [m0, t0, cov, remote]) < 400,
      'all stored entries <400')
hf = m0-.00024*np.eye(N)-(100/307)*(cov+.0046*np.eye(N))
aa = z.T@m0@z
bb = z.T@np.hstack((t0@z, t0.T@z))
yy = np.linalg.solve(aa, bb)  # proposal only; its entire residual is checked
gg = z@yy
eta_a = I('.00024')*sq(zn)+I('1e-7')
eta_b = I(2).sqrt()*sq(zn)*I(N)*I('2.1e-7')+I('1e-7')
kappa14 = 1/(I(3**16)*I(3).sqrt().sqrt()*I('2.5')*(1-I(1)/3**13))
eta_u = sq(zn)*(I(N)*I('1e-7')+kappa14)+I('1e-7')
positive('galerkin_floor', aa-.7793*np.eye(F))
check((I('.7793')-eta_a-I('1e-6')).lo > Decimal('.779'),
      'exact Galerkin floor >.779')
positive('predictor_norm', 1.32**2*np.eye(F)-yy@yy.T)
check(fro(yy) < 10, 'predictor Frobenius <10')
check(fro(aa@yy-bb) < 1e-9, 'complete floating Galerkin residual <1e-9')
positive('head_LZ_norm', 6.19**2*np.eye(F)-(m0@z).T@(m0@z))
# Factors above prove slightly weaker strict bounds because of their 1e-6
# allowance. Use the enlarged displayed norm bounds, not the factor shifts.
yn, mz = I('1.320001'), I('6.190001')
gn = zn*yn
rgal = eta_b+eta_a*yn+I('1e-7')
dy = rgal/I('.779')

endpoint = np.block([[aa, -z.T@remote.T@z], [-z.T@remote@z, aa]])
trial = endpoint-bb.T@yy-yy.T@bb+yy.T@aa@yy
trial = (trial+trial.T)/2
trial_error = eta_a*(1+sq(yn))+2*eta_b*yn+eta_u+I('1e-6')
# Exact Galerkin square completion: trial(g*)=trial(Z*Yhat)-r*A^-1*r.
trial_error += sq(rgal)/I('.779')

rhead = np.hstack((t0@z, t0.T@z))-m0@gg
sol = np.linalg.solve(hf, rhead)
head_solve_float = fro(rhead-hf@sol)
head_solve_error = I(str(head_solve_float))+I('1e-8')*I(str(fro(sol)))+I('1e-7')
head_action_error = (I(str(fro(rhead)))+I('1e-7'))*head_solve_error/I('.239999')+I('1e-7')
check(head_action_error.hi < Decimal('1e-6'), 'full head inverse-action matrix error <1e-6')
head_cov = (rhead.T@sol+sol.T@rhead)/2

# Every complementary row is regenerated with the audited entry formulas.
con = old.constants()
el, pif = con['ell'], con['pi']
indices = np.arange(K)
k = indices*pif/el
nu = np.full(K, np.sqrt(2/el)); nu[0] = 1/np.sqrt(el)
parity = np.where(indices % 2 == 0, 1., -1.)
imag, _ = old.psi_imag(k, pif)
bpsi = k*imag/2
moments = np.array([nu*c*(parity*(con['fourth'] if c > 0 else 1/con['fourth'])-1)
                    /(c*c+k*k) for c in [.5, -.5]])
saved_lowers = fixed['middle']['diagonal_lower_endpoints']
check(len(saved_lowers) == K-N, 'complete audited diagonal lower list')
weights = np.array([np.nextafter(float(2/Decimal(s)), np.inf) for s in saved_lowers])
check(float(weights.max()) < 2/6.14, 'all complementary weights below 2/6.14')


def translation(rows, delta):
    kn, km = k[rows, None], k[None, :N]
    sn, _ = old.sincos(k[rows]*delta, pif)
    sm, _ = old.sincos(k[:N]*delta, pif)
    signs = parity[rows, None]*parity[None, :N]
    if delta > 0:
        numerator = -signs*kn*sn[:, None]+km*sm[None, :]
    else:
        numerator = kn*sn[:, None]-signs*km*sm[None, :]
    return numerator/(kn*kn-km*km)*np.outer(nu[rows], nu[:N])


finite_cov = np.zeros((E, E))
row_blocks, raw_normsq = [], 0.
residual_hash = hashlib.sha256()
for start in range(N, K, N):
    rows = slice(start, start+N)
    kn, km = k[rows, None], k[None, :N]
    same = parity[rows, None] == parity[None, :N]
    response = (bpsi[rows, None]-bpsi[None, :N])/(kn*kn-km*km)
    for j in range(64):
        c = 2*j+.5
        response -= ((3.**(-j)/con['fourth'])*parity[rows, None]*c*c
                     /((c*c+kn*kn)*(c*c+km*km)))
    response *= 2*np.outer(nu[rows], nu[:N])*same
    tt, ts = np.zeros_like(response), np.zeros_like(response)
    for delta, weight in zip(con['deltas'], con['weights']):
        tt += weight*translation(rows, delta)
        ts += weight*translation(rows, -delta)
    for j in range(1, 8):
        c = 2*j+.5
        decay = 3.**(-j)/con['fourth']
        minus = nu*c*(1-parity*decay)/(c*c+k*k)
        plus = nu*c*(parity-decay)/(c*c+k*k)
        prefactor = 3.**(-6*j)/(3*np.sqrt(3.))
        tt += prefactor*np.outer(minus[rows], plus[:N])
        ts += prefactor*np.outer(plus[rows], minus[:N])
    w0 = response+256*moments[:, rows].T@moments[:, :N]
    rho = np.hstack((tt@z, ts@z))-w0@gg
    residual_hash.update(rho.tobytes())
    weighted = np.sqrt(weights[start-N:start+N-N, None])*rho
    finite_cov += weighted.T@weighted
    maximum = max(float(np.max(np.abs(x))) for x in [w0, tt, ts])
    normsq = sum(fro(x)**2 for x in [w0, tt, ts])
    raw_normsq += normsq
    check(maximum < 400, 'entry magnitudes rows '+str(start))
    row_blocks.append(dict(first=start, last=start+N-1, maximum_entry=maximum,
                           raw_factor_fro_squared=normsq, weighted_residual_fro=fro(weighted)))
    if start % 8192 == 0:
        print('Completed residual rows through', start+N-1, flush=True)
check(raw_normsq < 20, 'complete raw finite factor squared Frobenius <20')

e0 = I('.000000181')+I((K-N)*N).sqrt()*I('1e-7')
delta_p = I(2).sqrt()*I(N)*I('2.1e-7')*zn+I('.00024')*gn+I('1e-7')
delta_m = (I(2).sqrt()*I((K-N)*N).sqrt()*I('2.1e-7')*zn
           +e0*gn+I('1e-7'))
delta_finite = (sq(delta_p)/I('.239999')+2*sq(delta_m)/I('6.14')).sqrt()
finite_trace_upper = I(str(float(np.trace(head_cov+finite_cov))))+I('.00001')
check(finite_trace_upper.lo > 0, 'positive finite trace expression')
finite_error = 2*finite_trace_upper.sqrt()*delta_finite+sq(delta_finite)+I('.00001')

# Complete n>=K tail, retaining six boundary functionals. See the proof.
d = np.ones(N); d[0] = 1/np.sqrt(2)
ve = d*(indices[:N] % 2 == 0)
vo = d*(indices[:N] % 2 == 1)
vp, va = d, d*parity[:N]
vf, vh = np.zeros((2, E)), np.zeros((2, E))
vf[0, :F], vf[1, :F] = va@z, vp@z
vh[0, F:], vh[1, F:] = vp@z, va@z
boundary = np.vstack((vf, vh, ve@gg, vo@gg))
ap, am = I(0), I(0)
for n, p in old.POWERS:
    a = I(p).ln()/I(n).sqrt()
    delay = 7*ell-I(n).ln()
    check(delay.lo > 0 or delay.hi < 0, 'separation7 delay sign '+str(n))
    if delay.lo > 0:
        ap += a
    else:
        am += a
wb = 4*ell*(1+I('1.5')/(I(3).sqrt().sqrt()))/sq(pi)
tail_weights = [2*ap/pi/I(K-1).sqrt(), 2*am/pi/I(K-1).sqrt(),
                2*ap/pi/I(K-1).sqrt(), 2*am/pi/I(K-1).sqrt(),
                I(2).sqrt()*(1+wb/K)/I(K-1).sqrt(), (1+wb/K)/I(K-1).sqrt()]
wj = np.array([upper_float(x) for x in tail_weights])
sumw = np.nextafter(wj.sum(), np.inf)
leading_cov = sumw*(boundary.T@(wj[:, None]*boundary))
m2 = I(sum(n*n for n in range(1, N))).sqrt()
m4 = I(sum(n**4 for n in range(1, N))).sqrt()
prime_remainder = (2/pi)/(1-I((N-1)**2)/(K*K))*(
    m4/(I(5).sqrt()*I(K-1)*I(K-1)*I(K-1).sqrt())
    +m2/(I(3).sqrt()*I(K-1)*I(K-1).sqrt()))*(ap+am)
response_c = 16*ell/sq(pi)
response_remainder = sum((sq(4*n+response_c) for n in range(N)), I(0)).sqrt()/(
    I(3).sqrt()*I(K-1)*I(K-1).sqrt())
kappa = 1/(I(2187)*I(3).sqrt()*I('2.5')*(1-I(1)/729))
tail_remainder = I(2).sqrt()*zn*(prime_remainder+kappa)+response_remainder*gn
dk = (K/(2*ell)).ln()-2*sq(ell)/(9*K*K)
tail_matrix = upper_float(2/dk)*(1.1*leading_cov+
    upper_float(11*sq(tail_remainder))*np.eye(E))
# One 1e-6 norm allowance pays the complete tail matrix assembly, constant
# conversion, and replacing exact Z by its saved center in the functionals.
tail_matrix += 1e-6*np.eye(E)
tilde_cov = (head_cov+finite_cov+tail_matrix)
tilde_cov = (tilde_cov+tilde_cov.T)/2+upper_float(finite_error)*np.eye(E)
tilde_trace = I(str(float(np.trace(tilde_cov))))+I('.00001')
qlz = (I('.586')+e0+I('.062501906'))*zn
weighted_lz = (sq(mz+I('.00024')*zn+I('1e-7'))/I('.239999')
               +2*sq(qlz)/I('6.14')).sqrt()
predictor_delta = weighted_lz*dy
predictor_cov_error = 2*tilde_trace.sqrt()*predictor_delta+sq(predictor_delta)
comparison = trial-tilde_cov-upper_float(trial_error+predictor_cov_error)*np.eye(E)
comparison = (comparison+comparison.T)/2
positive('comparison_margin', comparison-.001*np.eye(E))

art = BASE/'neutral-head-covariance-559.npz'
np.savez_compressed(art, z=z, a=aa, b=bb, predictor_free=yy, predictor_raw=gg,
    trial=trial, head_residual=rhead, head_solution=sol, head_covariance=head_cov,
    finite_covariance=finite_cov, boundary_functionals=boundary,
    tail_covariance_upper=tail_matrix, full_covariance_upper=tilde_cov,
    comparison_lower=comparison, **{'factor_'+key: value for key, value in factors.items()})
out = BASE/'neutral-head-covariance-559.json'
result = dict(scope='N512/K65536 independent complex neutral endpoints; exact Galerkin middle',
    parameters=dict(N=N, K=K, endpoint_dimension=E, middle_dimension=F,
                    d0='6.14', fraction='1/2', penalty=256),
    source_script_sha256=sha(Path(__file__)), input_hashes=pins,
    constants=dict(pi=pi.json(), ell=ell.json()), neutral_ratios=ratios,
    neutral_basis_conversion_L1=ratio_error.json(),
    finite=dict(basis_norm_bound=zn.json(), head_form_error=eta_a.json(),
        forcing_error=eta_b.json(), remote_error=eta_u.json(),
        galerkin_floor='.779', predictor_norm_bound=yn.json(),
        galerkin_equation_error=rgal.json(), predictor_free_error=dy.json(),
        full_trial_error=trial_error.json(), head_solve_residual_float=head_solve_float,
        head_solve_error=head_solve_error.json(), head_action_error=head_action_error.json(),
        residual_head_error=delta_p.json(), residual_middle_error=delta_m.json(),
        weighted_residual_error=delta_finite.json(), finite_covariance_error=finite_error.json(),
        raw_factor_fro_squared=raw_normsq, row_blocks=row_blocks,
        regenerated_combined_residual_sha256=residual_hash.hexdigest()),
    tail=dict(first=K, prime_weight_positive=ap.json(), prime_weight_negative=am.json(),
        six_weights=[x.json() for x in tail_weights], response_b=wb.json(),
        prime_remainder=prime_remainder.json(), response_remainder=response_remainder.json(),
        complete_continuous_norm=kappa.json(), remainder=tail_remainder.json(),
        diagonal_lower=dk.json(), young_factors=['1.1', '11'], matrix_error='1e-6'),
    exact_predictor=dict(reference_weighted_LZ_bound=weighted_lz.json(),
        residual_change=predictor_delta.json(), covariance_error=predictor_cov_error.json(),
        tilde_covariance_trace_upper=tilde_trace.json()),
    factor_ledger=ledger,
    summary=dict(required_matrix_lower='0', proposed_shift='.001',
        certified_lower_if_all_checks_pass='.000999', passed=not failures,
        diagnostic_minimum_comparison=float(np.linalg.eigvalsh(comparison)[0]),
        diagnostic_minimum_trial=float(np.linalg.eigvalsh(trial)[0])),
    arithmetic=dict(unit_roundoff='2^-53', finite_matrix_allowance='1e-7',
        accumulated_Gram_and_head_allowance='.00001', factor_allowance='1e-6',
        explanation='Canonical proof gives dimension/magnitude gamma ledgers; no spectral routine is trusted.'),
    checks=checks, failures=failures,
    binary_artifact=dict(path=art.name, sha256=sha(art)),
    qualifications=['Inherited analytic response, IEEE754/Decimal contracts.',
        'Neutral core and unreplayed c_star retain C744z/C999k qualifications.',
        'Fixed finite endpoint family only; no endpoint complement, H2 or RH claim.',
        'New certificate is unaudited pending a separate conceptual review.'])
out.write_text(json.dumps(result, indent=2)+'\n')
print('Trial error upper:', trial_error.hi)
print('Finite covariance error upper:', finite_error.hi)
print('Tail remainder L2 upper:', tail_remainder.hi)
print('Exact-predictor covariance error upper:', predictor_cov_error.hi)
print('Comparison diagnostic minimum:', result['summary']['diagnostic_minimum_comparison'])
print('Required >=0; certified lower if all ledgers pass: .000999')
print('Checks:', len(checks), '; failures:', failures)
print('Certificate:', out.relative_to(BASE.parent.parent))
print('Full matrices/factors:', art.relative_to(BASE.parent.parent))
assert not failures
