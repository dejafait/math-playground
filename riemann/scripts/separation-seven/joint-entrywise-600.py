#!/usr/bin/env python3
"""Fixed entrywise test599/600; stop on first failed sufficient gate.

All intervals are conservative boxes, not a correlated uncertainty model.
No sign of the exact target is inferred from a failed lower certificate.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
import numpy as np

P = Path(__file__).resolve().parent
ROOT = P.parent.parent
TARGET = ('Test whether componentwise verified solves and entrywise residual Gram '
          'enclosures certify the unchanged joint2044 Galerkin comparison at '
          '.000999 free Euclidean floor, retaining the entire infinite output.')
J, F, E, N, K = 1024, 1022, 2044, 512, 65536
spec = importlib.util.spec_from_file_location('iv600', P/'complete-schur-531.py')
iv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iv)
iv.DOWN = Context(prec=80, rounding=ROUND_FLOOR)
iv.UP = Context(prec=80, rounding=ROUND_CEILING)
iv.NEAR = Context(prec=80, rounding=ROUND_HALF_EVEN)
I = iv.I
arrays, record, checks, failures = {}, {}, [], []

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def ck(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok:
        failures.append(label)
        raise RuntimeError(label)

def up(a):
    return np.nextafter(a, np.inf)

def positive_dot(a, b):
    # Max contraction length2044, gamma_2044<2.28e-13.
    # Inflation1e-11 also pays its own multiplication/conversion.
    assert a.shape[-1] <= E
    return up((a@b)*(1+1e-11)+1e-280)

class Ball:
    def __init__(self, c, r=0):
        self.c = np.asarray(c, dtype=float)
        self.r = np.broadcast_to(np.asarray(r, dtype=float), self.c.shape).copy()
        assert np.all(self.r >= 0)
        assert np.isfinite(self.c).all() and np.isfinite(self.r).all()

    @property
    def T(self):
        return Ball(self.c.T, self.r.T)

    def __neg__(self):
        return Ball(-self.c, self.r)

    def __add__(self, b):
        c = self.c+b.c
        er = up((np.abs(self.c)+np.abs(b.c))*1e-15+1e-280)
        return Ball(c, up(up(self.r+b.r)+er))

    def __sub__(self, b):
        return self+(-b)

    def __matmul__(self, b):
        c = self.c@b.c
        er = up(positive_dot(np.abs(self.c), np.abs(b.c))*1e-11+1e-280)
        r = up(positive_dot(np.abs(self.c), b.r)+positive_dot(self.r, np.abs(b.c)))
        r = up(up(r+positive_dot(self.r, b.r))+er)
        return Ball(c, r)

    def take(self, rows):
        return Ball(self.c[rows], self.r[rows])

    def scale(self, a):
        # a is an exact scalar dyadic here (.5 or an upward saved weight).
        c = self.c*a
        return Ball(c, up(up(self.r*np.abs(a))+up(np.abs(c)*1e-15+1e-280)))

def block(bs):
    return Ball(np.block([[b.c for b in row] for row in bs]),
                np.block([[b.r for b in row] for row in bs]))

def exact_scalar(s):
    d = Decimal(s)
    f = float(d)
    r = float(abs(d-Decimal(f)))
    return f, float(up(r))

def times_scalar(b, pair):
    a, ar = pair
    c = b.c*a
    r = up(up(np.abs(a)*b.r)+up(np.abs(b.c)*ar))
    r = up(up(r+up(b.r*ar))+up(np.abs(c)*1e-15+1e-280))
    return Ball(c, r)

def save_ball(name, b):
    arrays[name+'_center'] = b.c
    arrays[name+'_radius'] = b.r

def abs_upper(b):
    return up(np.abs(b.c)+b.r)

def summary(b):
    return dict(shape=list(b.c.shape), max_center=float(np.abs(b.c).max()),
                max_radius=float(b.r.max()))

def response_radius():
    n = np.arange(J, dtype=float)
    q = 1.415/(6*(64.25**2+(5.719*n/2)**2))
    den = np.abs(n[:, None]**2-n[None, :]**2)
    same = den == 0
    den[same] = 1
    rad = (2/3.14159)*(n[:, None]*q[:, None]+n[None, :]*q[None, :])/den
    rad *= ((n[:, None]-n[None, :]) % 2 == 0)
    c = 131072.5
    np.fill_diagonal(rad, q+8*(c**-2+2*(5.720*n)**2*(1/(6*c**3)+c**-4)))
    # C999q Sections2/8: <50 operations, expressions<.001, extra1e-12.
    return up(rad+1e-7+1e-12)

def verified_solve(name, a, b, proposal):
    w = np.linalg.inv(a.c)  # fixed dyadic proposal, never trusted as inverse
    wb = Ball(w)
    kk = Ball(np.eye(a.c.shape[0]))-wb@a
    z = wb@(b-a@Ball(proposal))
    au = abs_upper(kk)
    zu = abs_upper(z)
    x = up(1.1*zu+1e-260)
    save_ball(name+'_A', a)
    save_ball(name+'_B', b)
    save_ball(name+'_K', kk)
    save_ball(name+'_z', z)
    arrays[name+'_W'] = w
    arrays[name+'_proposal'] = proposal
    iterations = []
    for it in range(1, 16):
        image_radius = up(z.r+positive_dot(au, x))
        image_abs = up(np.abs(z.c)+image_radius)
        margins = np.nextafter(x-image_abs, -np.inf)
        columns = np.all(margins > 0, axis=0)
        iterations.append(dict(iteration=it, included_columns=int(columns.sum()),
                               required_columns=b.c.shape[1],
                               min_margin=float(margins.min()), max_box=float(x.max())))
        if columns.all():
            arrays[name+'_inclusion_box'] = x
            arrays[name+'_inclusion_image_radius'] = image_radius
            arrays[name+'_inclusion_margins'] = margins
            arrays[name+'_included_columns'] = columns
            sol = Ball(proposal)+Ball(z.c, image_radius)
            save_ball(name+'_solution', sol)
            row_sum = up(np.sum(au, axis=1)*(1+1e-11)+1e-280)
            record[name] = dict(iterations=iterations, max_K_rowsum=float(row_sum.max()),
                                solution=summary(sol), regularity='strict Rump inclusion')
            ck(float(row_sum.max()) < 1, name+' additional contraction check')
            print(name, 'inclusion', it, 'all', b.c.shape[1],
                  'columns; |K| row upper',float(row_sum.max()),flush=True)
            return sol
        x = up(1.1*image_abs+1e-260)
    record[name] = dict(iterations=iterations)
    ck(False, name+' failed strict inclusion in15 iterations')

def interval_quadratic(name, matrix, x):
    xb = Ball(x[:, None])
    val = xb.T@matrix@xb
    lo = float(np.nextafter(val.c[0, 0]-val.r[0, 0], -np.inf))
    hi = float(up(val.c[0, 0]+val.r[0, 0]))
    record[name] = dict(lo=lo, hi=hi, norm_squared=float(x@x))
    arrays[name+'_direction'] = x
    return lo, hi

names = ['original-galerkin-586.npz', 'original-galerkin-586.json',
         'original-minimum-audit-588.json', 'certificate-audit-534.json',
         'fixed-block-metric-audit-557.json', 'fixed-block-metric-555.json',
         'complete-covariance-532.npz', 'joint-galerkin-family-locator-598.npz',
         'joint-galerkin-family-certificate-598.json',
         'joint-galerkin-family-certificate-598.npz',
         'joint-galerkin-family-ledger-598.json', 'complete-schur-531.py']
pins = {n: sha(P/n) for n in names}
result = 'INCONCLUSIVE'
try:
    orig = json.loads((P/'original-galerkin-586.json').read_text())
    previous = json.loads((P/'joint-galerkin-family-certificate-598.json').read_text())
    ck(pins['original-galerkin-586.npz'] == orig['archive']['sha256'], 'audited square pin')
    ck(pins['joint-galerkin-family-certificate-598.npz'] == previous['archive']['sha256'],
       'complete previous certificate archive pin')
    ck(previous['failures'] == ['quarter_comparison factor unavailable'], 'preserved598 stop')
    ck(not json.loads((P/'joint-galerkin-family-ledger-598.json').read_text())['failures'],
       'complete598 arithmetic ledger')
    for n in ['original-minimum-audit-588.json', 'fixed-block-metric-audit-557.json']:
        ck(not json.loads((P/n).read_text())['failures'], 'inherited no failures '+n)
    aud = json.loads((P/'certificate-audit-534.json').read_text())
    ck(pins['complete-covariance-532.npz'] == aud['original_sha256']['complete-covariance-532.npz'],
       'exact reference dyadic data pin')
    with np.load(P/'original-galerkin-586.npz') as q:
        mc, tc, tsc, uc = [q[n].copy() for n in ['local_matrix','t_entries','ts_entries','u_entries']]
    with np.load(P/'joint-galerkin-family-locator-598.npz') as q:
        zc, yh = [q[n].copy() for n in ['Z','Y']]
    ck(np.array_equal(tc, tsc.T), 'both complete forcing orientations')
    ck(np.array_equal(mc, mc.T), 'symmetric raw local center')
    ck(yh.shape == (F,E), 'full2044-column proposal')
    zr = np.zeros_like(zc)
    def powi(v, n):
        ans = I(1)
        for _ in range(n):
            ans *= v
        return ans
    def atan(q):
        t = I(1)/q
        ans = sum(((-1)**j*powi(t,2*j+1)/(2*j+1) for j in range(80)), I(0))
        rem = powi(t,161)/161
        return ans+I(-rem.hi, rem.hi)
    pi, ell = 16*atan(5)-4*atan(239), I(3).ln()/2
    ratio_evidence = []
    for n in range(2,J):
        p = n % 2
        rr = (I('.25')+powi(p*pi/ell,2))/(I('.25')+powi(n*pi/ell,2))
        if p == 0:
            rr *= I(2).sqrt()
        err = rr+I(Decimal(float(zc[p,n-2])))
        zr[p,n-2] = up(float(max(abs(err.lo),abs(err.hi))))
        ratio_evidence.append(rr.json())
    template = np.eye(J)[:,2:]
    template[:2] = zc[:2]
    ck(np.array_equal(template, zc), 'all exact-coordinate sparse positions')
    ck((pi/ell).lo > Decimal('5.719') and (pi/ell).hi < Decimal('5.720'),
       'response rational constants')
    record['neutral_ratio_intervals'] = ratio_evidence
    z = Ball(zc, zr)
    m = Ball(mc, response_radius())
    cross_radius = float(up(float(Decimal('.000001'))))
    t, ts, u = Ball(tc,cross_radius), Ball(tsc,cross_radius), Ball(uc,cross_radius)
    save_ball('Z',z)
    save_ball('M',m)
    a = z.T@m@z
    forcing = block([[t@z, ts@z]])
    b = z.T@forcing
    y = verified_solve('galerkin', a, b, yh)
    g = z@y
    save_ball('exact_predictor_raw',g)
    endpoint = block([[a, -(z.T@u.T@z)],[-(z.T@u@z), a]])
    energy = endpoint-b.T@y-y.T@b+y.T@a@y
    energy = (energy+energy.T).scale(.5)
    save_ball('energy',energy)
    print('Full original energy entry boxes formed',summary(energy),flush=True)
    rho = forcing-m@g
    save_ball('residual_first1024',rho)
    with np.load(P/'complete-covariance-532.npz') as q:
        mh, ch = Ball(q['m0']), Ball(q['cov00'])
    fi, fr = exact_scalar('.00024')
    dc, dr = exact_scalar('.0046')
    coef = I(100)/307
    cf = float((coef.lo+coef.hi)/2)
    cr = float(up(float(max(abs(coef.lo-Decimal(cf)),abs(coef.hi-Decimal(cf))))))
    h = mh-Ball(fi*np.eye(N),fr*np.eye(N))-times_scalar(ch+Ball(dc*np.eye(N),dr*np.eye(N)),(cf,cr))
    xh = np.linalg.solve(h.c,rho.c[:N])
    head_solution = verified_solve('head_reference',h,rho.take(slice(0,N)),xh)
    head = rho.take(slice(0,N)).T@head_solution
    head = (head+head.T).scale(.5)
    save_ball('head_covariance',head)
    fixed = json.loads((P/'fixed-block-metric-555.json').read_text())
    lows = fixed['middle']['diagonal_lower_endpoints']
    ck(len(lows)==K-N,'all65024 inherited reference weights available')
    # An upward inverse weight is a sufficient majorant, not exact R^-1.
    weights = np.array([up(float(iv.UP.divide(Decimal(2),Decimal(s)))) for s in lows[:N]])
    arrays['first_complement_weights'] = weights
    rm = rho.take(slice(N,J))
    comp = rm.T@rm.scale(weights[:,None])
    comp = (comp+comp.T).scale(.5)
    save_ball('covariance_512_1023',comp)
    partial = energy-head-comp
    partial = (partial+partial.T).scale(.5)
    save_ball('partial_comparison',partial)
    # Deliberately test the already-assessed symmetric nonnegative radius
    # norm criterion. Failure here stops BEFORE paying remaining outputs.
    rad = np.maximum(partial.r,partial.r.T)
    rows = up(np.sum(rad,axis=1)*(1+1e-11)+1e-280)
    r = float(rows.max())
    arrays['partial_symmetric_radius'] = rad
    arrays['partial_radius_rowsum_upper'] = rows
    shifted = partial.c-(r+.000999)*np.eye(E)
    arrays['partial_shifted_lower'] = shifted
    # A dyadic direction is only a witness against THIS sufficient matrix.
    vals, vecs = np.linalg.eigh((shifted+shifted.T)/2)
    x = vecs[:,0]
    # Recompute the subtraction as interval arithmetic; stored shifted
    # rounding is not assumed exact. This covers the selected full value.
    shift_ball = Ball(partial.c)-Ball(np.eye(E)*(r+.000999),
                                    np.eye(E)*up((abs(r)+.000999)*1e-15+1e-280))
    lo, hi = interval_quadratic('partial_lower_direction',shift_ball,x)
    record['partial_radius_test'] = dict(radius_norm_upper=r,
        required_floor='.000999', rows_included='0:1023',
        unverified_outputs='1024:65535 and every n>=65536',
        diagnostic_center_minimum=float(vals[0]+r+.000999),
        shifted_lower_rayleigh=dict(lo=lo,hi=hi))
    if hi < 0:
        record['stop_reason'] = 'Excessive finite entry-radius norm: shifted lower matrix has a verified negative direction.'
        result = 'FINITE_RADIUS_GATE_FAILED'
        print('Finite radius gate failed: radius upper',r,
              'shifted-lower Rayleigh interval',[lo,hi],
              'required >=0 for .000999 comparison',flush=True)
    else:
        record['stop_reason'] = 'Finite radius gate not rejected; full remaining output calculation still unpaid.'
        failures.append('complete remaining finite/infinite output not evaluated')
        result = 'INCOMPLETE'
except Exception as ex:
    if not failures:
        failures.append(type(ex).__name__+': '+str(ex))
    record['stop_reason'] = type(ex).__name__+': '+str(ex)

preserved = all(sha(P/n)==s for n,s in pins.items())
checks.append(dict(label='all inherited inputs unchanged',passed=preserved))
if not preserved:
    failures.append('inherited input changed')
archive = P/'joint-entrywise-600.npz'
np.savez_compressed(archive,**arrays)
out = P/'joint-entrywise-600.json'
report = dict(target=TARGET,result=result,actual_target_sign='UNDECIDED',
              independently_audited=False,checks=checks,failures=failures,
              record=record,input_hashes=pins,script_sha256=sha(Path(__file__)),
              archive=dict(path=str(archive.relative_to(ROOT)),sha256=sha(archive)),
              complete_infinite_output_paid=False,
              qualifications=['Inherited analytic-response and IEEE754/Decimal contracts',
              'Neutral form core and original c_star remain independently unaudited',
              'No complete joint comparison or actual violating direction certified',
              'Interval boxes discard dependencies; no new general theorem',
              'Finite-radius stop: remaining rows/tail are deliberately uncomputed'])
out.write_text(json.dumps(report,indent=2)+'\n')
print('Result',result,'actual target UNDECIDED; failures',failures,flush=True)
print('Full certificate',out.relative_to(ROOT),'arrays',archive.relative_to(ROOT),flush=True)
