#!/usr/bin/env python3
"""One original frozen-endpoint finite minimum; assessment584/approval585.

All complete entries use the audited C999n/C744w analytic/arithmetic
contracts. Proposed solves and Cholesky factors have no accuracy premise.
Old artifacts are read-only. Full evidence and factors are saved locally.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
from decimal import Decimal
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
OUT = BASE/'original-galerkin-586.json'
ARRAYS = BASE/'original-galerkin-586.npz'
checks, details, bounds = [], {}, {}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok:
        raise AssertionError(label)


pins = {p: sha(BASE/p) for p in [
    'endpoint-complement-locator-581.py', 'endpoint-complement-locator-581.npz',
    'endpoint-complement-locator-581.json', 'endpoint-quarter-audit-583.json',
    'residual-certificate-532.py', 'complete-schur-531.py',
    'response-prefix-stop-546.json', 'complete-covariance-532.npz']}


def main():
    spec = importlib.util.spec_from_file_location('interval586', BASE/'complete-schur-531.py')
    a = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(a)
    I = a.I

    def exact(x):
        return I(Decimal(float(x)))

    def ab(x):
        return max(x.lo.copy_abs(), x.hi.copy_abs())

    def sq(x):
        if x.lo <= 0 <= x.hi:
            return I(0, a.UP.multiply(ab(x), ab(x)))
        return x*x

    def inflate(x, error):
        return x+I(ab(error).copy_negate(), ab(error))

    def norm(x):
        # Covers full <=1024^2 sum-of-squares and sqrt rounding.
        return exact(float(np.linalg.norm(x)))*I('1.00000001')+I('1e-30')

    def gamma(n):
        t = I(n)/2**53
        return t/(1-t)

    def power(x, n):
        result = I(1)
        for _ in range(n):
            result *= x
        return result

    def atan(q):
        x = I(1)/q
        result = sum((((-1)**j)*power(x, 2*j+1)/(2*j+1)
                      for j in range(80)), I(0))
        return inflate(result, power(x, 161)/161)

    def l1(xs):
        return sum((I(ab(x)) for x in xs), I(0))

    def dot(x, matrix, y):
        error = I('1e-8')*l1([exact(t) for t in x])*l1([exact(t) for t in y])
        return inflate(exact(float(x@matrix@y)), error)

    old = json.loads((BASE/'endpoint-complement-locator-581.json').read_text())
    check(old['archive']['sha256'] == pins['endpoint-complement-locator-581.npz'], 'frozen endpoint archive hash')
    check(old['script_sha256'] == pins['endpoint-complement-locator-581.py'], 'original generator hash')
    for name, digest in old['input_hashes'].items():
        check(sha(BASE/name) == digest, 'original input hash '+name)
    with np.load(BASE/'endpoint-complement-locator-581.npz') as z:
        frozen = {key: z[key].copy() for key in z.files}

    # Replay only complete entry assembly, never the selection/eigensolve/write.
    source_path = BASE/'endpoint-complement-locator-581.py'
    marker = '# Exact object Z'
    source = source_path.read_text()
    check(source.count(marker) == 1, 'unique pre-selection assembly boundary')
    prefix = source.split(marker)[0]
    oldidx = 'idx = np.r_[0, 1, np.arange(N, J)]'
    check(prefix.count(oldidx) == 1, 'unique physical-column expansion')
    prefix = prefix.replace(oldidx, 'idx = np.arange(J)')
    env = dict(__file__=str(source_path), __name__='original586_entries')
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        exec(compile(prefix, str(source_path), 'exec'), env)
    details['assembly_stdout'] = capture.getvalue()
    M, T, Ts, U = [env[key] for key in ['L', 'T', 'Ts', 'U']]
    check(all(x.shape == (1024, 1024) and np.isfinite(x).all()
              and np.abs(x).max() < 400 for x in [M, T, Ts, U]), 'all complete entry shapes/magnitudes')
    idx = frozen['physical_index_set']
    for key, center in [('local_matrix', M[np.ix_(idx, idx)]),
                        ('t_entries', T[:, idx]), ('ts_entries', Ts[:, idx]),
                        ('u_entries', U[np.ix_(idx, idx)])]:
        check(np.array_equal(center, frozen[key]), 'entire old rectangle replay '+key)
    check(np.array_equal(T, Ts.T), 'both full T orientations agree exactly')
    check(len(env['powers']) == 334 and (2187, 3) in env['powers'], 'all334 remote powers including zero shift')
    check(len(env['con']['weights']) == 16, 'all16 nearest-cell powers')
    pi = 16*atan(5)-4*atan(239)
    ell = I(3).ln()/2
    check(ab(pi-I(env['e'].PI_TEXT)) < Decimal('1e-55'), 'complete pi decimal enclosure')
    k = [n*pi/ell for n in range(1024)]
    nu0, nu = (1/ell).sqrt(), (2/ell).sqrt()
    ratios = [(nu/(nu0 if n % 2 == 0 else nu))*(I('.25')+sq(k[n % 2]))
              /(I('.25')+sq(k[n])) for n in range(2, 1024)]
    rhat = np.array([float(a.NEAR.divide(a.NEAR.add(t.lo, t.hi), Decimal(2))) for t in ratios])
    Z = np.zeros((1024, 1022))
    Z[2:] = np.eye(1022)
    Z[np.arange(2, 1024) % 2, np.arange(1022)] = -rhat
    dz = sum((sq(I(ab(t-exact(c)))) for t, c in zip(ratios, rhat)), I(0)).sqrt()
    zr = sum((sq(t) for t in ratios), I(0))
    zbound = (1+zr).sqrt()
    check(zbound.hi < Decimal('1.008'), 'exact neutral coordinate operator norm<1.008')
    check(dz.hi < Decimal('1e-14'), 'complete neutral coordinate Frobenius error<1e-14')
    free = frozen['free_numerators'].astype(float)/2**40
    check(np.array_equal(free*2**40, frozen['free_numerators']), 'every endpoint dyadic is exact')

    def complete(v):
        ints = [exact(t) for t in v]
        raw = [I(0), I(0)]+ints
        for j, n in enumerate(range(2, 1024)):
            raw[n % 2] -= ratios[j]*ints[j]
        center = Z@v
        delta = sum((I(ab(t-exact(c))) for t, c in zip(raw, center)), I(0))
        return raw, center, delta

    vf, vh = np.zeros(1022), np.zeros(1022)
    vf[510:], vh[510:] = free[:512], free[512:]
    fi, f, df = complete(vf)
    hi, h, dh = complete(vh)
    # All real centers are also Hermitian matrices on complex coordinates.
    Araw = Z.T@M@Z
    A = (Araw+Araw.T)/2
    rho = T@f+Ts@h
    b = Z.T@rho
    v = np.linalg.solve(A, b)  # proposal; full gradient bounded below
    gi, g, dg = complete(v)
    factor = np.linalg.cholesky(A-.5*np.eye(1022))
    reconstruction = norm(A-.5*np.eye(1022)-factor@factor.T)
    factor_round = gamma(2048)*norm(factor)*norm(factor)
    residual_round = gamma(8)*(norm(A)+I('.5')*I(1022).sqrt()+norm(factor)**2+1)
    positive_error = reconstruction+factor_round+residual_round
    check(positive_error.hi < Decimal('1e-6'), 'full proposed factor verifies A_center>=.5-1e-6')
    # Full matrix multiplication, subtraction and symmetrization errors.
    assembly_error = gamma(4096)*norm(Z)*norm(Z)*norm(M)+I('1e-7')
    check(assembly_error.hi < Decimal('1e-5'), 'full neutral matrix arithmetic error<1e-5')
    local_entry = I('.0001')
    cross_entry = I('.000001')
    analytic_A = zbound*zbound*1024*local_entry
    coord_A = dz*(2*zbound+dz)*norm(M)
    coercivity = I('.5')-positive_error-assembly_error-analytic_A-coord_A
    check(coercivity.lo > Decimal('.39'), 'exact finite coercivity>.39')
    lf, lh, lg = l1(fi), l1(hi), l1(gi)
    check(all(t.hi < Decimal('1e-12') for t in [df, dh, dg]), 'exact neutral physical coefficient errors<1e-12')
    endpoint = dot(f, M, f)+dot(h, M, h)-2*dot(h, U, f)
    trial = endpoint+dot(g, M, g)-2*dot(g, T, f)-2*dot(g, Ts, h)
    entry_energy = local_entry*(lf*lf+lh*lh+lg*lg)+2*cross_entry*(lf*lh+lg*lf+lg*lh)
    # Full signed-form perturbations, using every center entry<400.
    coord_energy = I(401)*(df*(2*lf+df)+dh*(2*lh+dh)+dg*(2*lg+dg)
        +2*(df*lh+dh*lf+df*dh+dg*lf+df*lg+df*dg+dg*lh+dh*lg+dh*dg))
    trial = inflate(trial, entry_energy+coord_energy)
    # Exact coordinate gradient c=Z_exact^*(M_exact*g_exact-rho_exact).
    wc = M@g-T@f-Ts@h
    cc = Z.T@wc
    arith_w = gamma(4096)*(norm(M)*norm(g)+norm(T)*norm(f)+norm(Ts)*norm(h)+1)
    arith_c = gamma(2048)*norm(Z)*norm(wc)
    physical_entry = 32*(local_entry*lg+cross_entry*(lf+lh))
    physical_coord = norm(M)*dg+32*I(400)*(df+dh)
    gradient_error = (zbound+dz)*(physical_entry+physical_coord+arith_w)+dz*norm(wc)+arith_c
    gradient = norm(cc)+gradient_error
    debt = gradient*gradient/coercivity
    minimum = I(a.DOWN.subtract(trial.lo, debt.hi), trial.hi)
    sign = 'POSITIVE' if minimum.lo > 0 else ('NEGATIVE' if minimum.hi < 0 else 'UNRESOLVED')
    for name, value in dict(coercivity=coercivity, trial_energy=trial,
        gradient_bound=gradient, gradient_error=gradient_error,
        gradient_debt=debt, finite_minimum=minimum,
        analytic_matrix_error=analytic_A, matrix_arithmetic_error=assembly_error,
        factor_reconstruction_error=positive_error, coordinate_matrix_error=coord_A,
        trial_entry_error=entry_energy, trial_coordinate_error=coord_energy,
        neutral_coordinate_error=dz, neutral_coordinate_norm=zbound,
        endpoint_f_l1=lf, endpoint_h_l1=lh, middle_l1=lg,
        endpoint_f_coordinate_error=df, endpoint_h_coordinate_error=dh,
        middle_coordinate_error=dg, physical_gradient_entry_error=physical_entry,
        physical_gradient_arithmetic_error=arith_w).items():
        bounds[name] = value.json()
    details.update(sign=sign, center_trial=float(endpoint.lo)+float(g@M@g-2*g@T@f-2*g@Ts@h),
        center_gradient_norm=float(np.linalg.norm(cc)),
        factor_frobenius_squared=float(np.linalg.norm(factor)**2),
        maximum_matrix_entry=float(max(np.abs(x).max() for x in [M,T,Ts,U])),
        exact_neutral_ratio_intervals=[t.json() for t in ratios],
        exact_neutral_middle_intervals=[t.json() for t in gi],
        exact_neutral_f_intervals=[t.json() for t in fi],
        exact_neutral_h_intervals=[t.json() for t in hi])
    np.savez_compressed(ARRAYS, local_matrix=M, t_entries=T, ts_entries=Ts,
        u_entries=U, neutral_coordinate_center=Z, neutral_matrix=A,
        forcing=b, middle_free_dyadic=v, middle_raw_center=g,
        endpoint_f_center=f, endpoint_h_center=h, lower_factor=factor,
        center_gradient=cc, free_numerators=frozen['free_numerators'])
    check(all(sha(BASE/name) == digest for name, digest in pins.items()), 'all original artifacts preserved')
    return sign


failure = None
try:
    sign = main()
except Exception as error:
    failure = type(error).__name__+': '+str(error)
    sign = 'UNRESOLVED'
report = dict(target="Certify the sign of the original three-cell Galerkin minimum for C999n's frozen endpoint pair, with the middle restricted to the exact neutral raw modes0:1023.",
    sign=sign, certified_under_inherited_contracts=failure is None and sign != 'UNRESOLVED',
    independently_audited=False, checks=checks, bounds=bounds, details=details,
    failures=([failure] if failure else [])+[c['label'] for c in checks if not c['passed']],
    required='a strict finite minimum interval above or below zero',
    analytic_ledger='C999n Section4 changed raw0:1023 range: local<.000097173<.0001, cross<.000001; all16/334 translations, zero shift and continuous tails retained',
    qualifications='C744v/w analytic and IEEE754/Decimal contracts; C744z whole-core and unreplayed c_* qualifications; finite positive minimum gives no infinite-middle/complement/RH sign',
    input_hashes=pins, script_sha256=sha(Path(__file__)),
    archive=({'path':str(ARRAYS.relative_to(ROOT)), 'sha256':sha(ARRAYS)} if ARRAYS.exists() else None))
OUT.write_text(json.dumps(report, indent=2)+'\n')
print('Original finite minimum sign='+sign+'; required strict separation from0; failures='+str(report['failures']))
print('Actual/required bounds='+json.dumps({k:bounds.get(k) for k in ['finite_minimum','coercivity','gradient_debt']}))
print('Full certificate='+str(OUT.relative_to(ROOT))+'; arrays='+str(ARRAYS.relative_to(ROOT)))
if failure:
    raise SystemExit(1)
