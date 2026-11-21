"""Independent L760 audit; original candidates and certificates are preserved.

Replay the Decimal certificate unchanged in a temporary directory. Independently
recompute every load-bearing finite bound with integer endpoint intervals, a
different LDL recurrence, integer square roots and a positive sinh Taylor sum.
No Decimal arithmetic is imported by the independent calculation.
"""
from fractions import Fraction
from math import isqrt
from pathlib import Path
import hashlib
import json
import platform
import shutil
import tempfile
import time

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / 'commutator-audit-366.json'
REPLAY = HERE / 'commutator-replay-366.json'
DIGITS = 240
SCALE = 10**DIGITS
started = time.monotonic()
report = dict(kind='independent integer-interval L760 audit',
              python=platform.python_version(), scale_digits=DIGITS,
              checks={}, failures=[], outcome='IN_PROGRESS')


def encode(value):
    if isinstance(value, J):
        return [str(value.lo)+'e-'+str(DIGITS), str(value.hi)+'e-'+str(DIGITS)]
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, list):
        return [encode(v) for v in value]
    return value


def save():
    report['elapsed_seconds'] = time.monotonic()-started
    OUTPUT.write_text(json.dumps(encode(report), indent=2)+'\n')


def require(ok, label):
    if not ok:
        report['failures'].append(label)
        save()
        raise ArithmeticError(label)


class J:
    """[lo/SCALE, hi/SCALE], with exact integer arithmetic and outward division."""
    def __init__(self, value=0):
        if isinstance(value, J):
            self.lo, self.hi = value.lo, value.hi
        else:
            q = Fraction(value)
            self.lo = q.numerator*SCALE//q.denominator
            self.hi = -((-q.numerator*SCALE)//q.denominator)

    @classmethod
    def bounds(cls, lo, hi):
        require(lo <= hi, 'ordered integer interval')
        out = cls()
        out.lo, out.hi = lo, hi
        return out

    @classmethod
    def pair(cls, p):
        require(len(p) == 2 and Fraction(p[0]) <= Fraction(p[1]), 'ordered input pair')
        return cls.bounds(cls(p[0]).lo, cls(p[1]).hi)

    def __add__(a, b):
        b = J(b)
        return J.bounds(a.lo+b.lo, a.hi+b.hi)

    __radd__ = __add__

    def __neg__(a):
        return J.bounds(-a.hi, -a.lo)

    def __sub__(a, b):
        return a + (-J(b))

    def __rsub__(a, b):
        return J(b) - a

    def __mul__(a, b):
        b = J(b)
        values = [x*y for x in (a.lo, a.hi) for y in (b.lo, b.hi)]
        return J.bounds(min(values)//SCALE, -((-max(values))//SCALE))

    __rmul__ = __mul__

    def __truediv__(a, b):
        b = J(b)
        require(not b.lo <= 0 <= b.hi, 'nonzero integer divisor')
        lows, highs = [], []
        for x in (a.lo, a.hi):
            for y in (b.lo, b.hi):
                n, d = x*SCALE, y
                if d < 0:
                    n, d = -n, -d
                lows.append(n//d)
                highs.append(-((-n)//d))
        return J.bounds(min(lows), max(highs))

    def square(a):
        low = 0 if a.lo <= 0 <= a.hi else min(a.lo*a.lo, a.hi*a.hi)
        high = max(a.lo*a.lo, a.hi*a.hi)
        return J.bounds(low//SCALE, -((-high)//SCALE))

    def sqrt(a):
        require(a.lo >= 0, 'nonnegative square root')
        low, high = isqrt(a.lo*SCALE), isqrt(a.hi*SCALE)
        if high*high < a.hi*SCALE:
            high += 1
        return J.bounds(low, high)

    def upper(a):
        return J.bounds(a.hi, a.hi)

    def lower(a):
        return J.bounds(a.lo, a.lo)

    def absupper(a):
        r = max(abs(a.lo), abs(a.hi))
        return J.bounds(r, r)


def dot(a, b):
    require(len(a) == len(b), 'equal dot dimensions')
    return sum((x*y for x, y in zip(a, b)), J())


def norm(v):
    return sum((x.square() for x in v), J()).sqrt()


def mv(a, v):
    return [dot(row, v) for row in a]


def inflate(v, radius):
    r = radius.absupper().hi
    return J.bounds(v.lo-r, v.hi+r)


def normalize(raw, dimension):
    require(len(raw) == dimension, 'full candidate dimension')
    v = [J(x) for x in raw]
    n = norm(v)
    require(n.lo > 0, 'positive candidate norm')
    return [x/n for x in v], n


def bracket(v, lo, hi, name):
    require(v.lo > J(lo).hi and v.hi < J(hi).lo, name)
    report['checks'][name] = dict(actual=v, required=[lo, hi])


def below(v, hi, name):
    require(v.hi < J(hi).lo, name)
    report['checks'][name] = dict(actual=v, required_upper=hi)


def show(v):
    # Presentation only: never used by the certificate or its comparisons.
    return [format(float(Fraction(x, SCALE)), '.9e') for x in (v.lo, v.hi)]


def inertia(a, shift, name):
    n = len(a)
    h = [[J(int(i == j)) for j in range(n)] for i in range(n)]
    piv = []
    for j in range(n):
        p = a[j][j]-shift-sum((h[j][r].square()*piv[r] for r in range(j)), J())
        require(not p.lo <= 0 <= p.hi, name+' nonzero pivot '+str(j))
        piv.append(p)
        for i in range(j+1, n):
            h[i][j] = (a[i][j]-sum((h[i][r]*h[j][r]*piv[r]
                                    for r in range(j)), J()))/p
    negative = sum(p.hi < 0 for p in piv)
    report[name] = dict(shift=shift, pivots=piv, factors=h, negative=negative,
                        nonzero_pivots=len(piv))
    save()
    print(name, 'negative', negative, 'nonzero pivots', len(piv), flush=True)
    return negative


try:
    names = ['finite-parity-359.py', 'finite-parity-359.json',
             'commutator-screen-364.json', 'commutator-certificate-364.py',
             'commutator-certificate-364.json']
    report['hashes'] = {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                        for name in names}
    report['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    old = json.loads((HERE/names[-1]).read_text())
    data = json.loads((HERE/names[1]).read_text())
    screen = json.loads((HERE/names[2]).read_text())
    require(old['failures'] == [] and data['failures'] == [], 'input failures empty')
    require(data['script_sha256'] == report['hashes'][names[0]], 'audited generator hash')
    require(old['script_sha256'] == report['hashes'][names[3]], 'certificate script hash')
    require(old['entry_certificate_sha256'] == report['hashes'][names[1]], 'entry hash')
    require(old['screen_sha256'] == report['hashes'][names[2]], 'candidate hash')
    require(data['parameters'] == dict(N=120, K=512, R=160, EM=80, precision=170), 'exact cell')
    with tempfile.TemporaryDirectory(prefix='riemann-commutator-366-') as folder:
        for name in names[:-1]:
            shutil.copyfile(HERE/name, Path(folder)/name)
        copied = Path(folder)/names[3]
        namespace = {'__file__': str(copied), '__name__': '__main__'}
        exec(compile(copied.read_bytes(), str(copied), 'exec'), namespace)
        shutil.copyfile(copied.with_suffix('.json'), REPLAY)
    replay = json.loads(REPLAY.read_text())
    require(set(replay) == set(old), 'replay key set')
    for key in old:
        if key != 'elapsed_seconds':
            require(old[key] == replay[key], 'complete replay field '+key)
    report['checks']['complete_replay'] = [k for k in old if k != 'elapsed_seconds']
    report['replay_sha256'] = hashlib.sha256(REPLAY.read_bytes()).hexdigest()
    require(all(set(flags) <= {'Rounded', 'Inexact'} for flags in replay['arithmetic_flags'].values()),
            'replayed arithmetic flags')
    print('complete original replay matches, including all coordinates and flags', flush=True)
    save()

    mats = {}
    for name, dimension in [('even', 121), ('odd', 120)]:
        raw = data[name+'_matrix']
        require(len(raw) == dimension and all(len(row) == dimension for row in raw), 'matrix dimension')
        mats[name] = [[J.pair(p) for p in row] for row in raw]
    even, odd = mats['even'], mats['odd']
    L, pi = [J.pair(data['constants'][k]) for k in ['L', 'pi']]
    root2, rootL, t = J(2).sqrt(), L.sqrt(), J('0.25')
    w, wn = normalize(screen['eigenpairs']['ground']['vector'], 121)
    theta = J(screen['eigenpairs']['ground']['value'])
    residual = [a-theta*b for a, b in zip(mv(even, w), w)]
    e = norm(residual)
    below(theta+e, '5e-56', 'select_ground')
    epsilon = inflate(theta, e)
    separation = J('1e-55')-theta
    require(separation.lo > 0, 'positive ground separation')
    E = 2*e.upper()/separation
    below(E, '1.22e-104', 'unit_ground_error')
    report['ground'] = dict(unit_candidate=w, raw_norm=wn, center=theta,
                           residual=residual, residual_norm=e, epsilon=epsilon,
                           unit_error=E)
    tau = J('3.0559e-55')
    require(inertia(even, tau, 'even_inertia') == 1, 'one even below tau')
    require(inertia(odd, tau, 'odd_inertia') == 0, 'no odd below tau')
    oy, oyn = normalize(screen['eigenpairs']['first_odd']['vector'], 120)
    rayleigh = dot(oy, mv(odd, oy))
    gap = J.bounds((tau-epsilon).lo, (rayleigh-epsilon).hi)
    bracket(gap, '3.0555e-55', '3.0556e-55', 'actual_gap')
    report['gap'] = dict(odd_unit_candidate=oy, raw_norm=oyn, rayleigh=rayleigh, gap=gap)
    print('actual gap', show(gap), 'required (3.0555e-55, 3.0556e-55)', flush=True)

    # Direct positive series, independent of the generator's exp method.
    z = L*t/2
    require(0 < z.lo and z.hi < SCALE, 'sinh argument in (0,1)')
    term, sinh = z, z
    for n in range(1, 100):
        term = term*z.square()/((2*n)*(2*n+1))
        sinh += term
    next_term = term*z.square()/(200*201)
    # Subsequent ratios <1/2; positivity makes the truncated sum a lower bound.
    sinh = J.bounds(sinh.lo, (sinh+2*next_term).hi)
    p = 2*sinh/rootL
    erow, orow = [p/t], []
    for j in range(1, 121):
        nu = 2*pi*j/L
        den = nu.square()+t.square()
        erow.append(root2*p*t/den)
        orow.append(-root2*p*nu/den)
    b = [J(1)/rootL]+[root2/rootL]*120
    overlap = inflate(dot(b, w), norm(b)*E)
    require(overlap.lo > 0, 'positive boundary overlap')
    transform = inflate(dot(erow, w), norm(erow)*E)
    value = transform/overlap
    qe = [a-value*c for a, c in zip(erow, b)]
    qo = orow
    nq = norm(qe+qo)
    require(nq.lo > 0, 'nonzero full dual row')
    report['row'] = dict(sinh=sinh, sinh_tail_upper=2*next_term,
                        fourier_even=erow, fourier_odd_imag=orow, boundary_even=b,
                        overlap=overlap, transform_unit=transform, transform_xi=value,
                        q_even=qe, q_odd_imag=qo, norm=nq)

    ke, ko = [[J(v) for v in screen[k]] for k in ['h_even', 'h_odd_imag']]
    require(len(ke) == 121 and len(ko) == 120, 'full preimage dimension')
    re = [a-epsilon*v-q for a, v, q in zip(mv(even, ke), ke, qe)]
    ro = [a-epsilon*v-q for a, v, q in zip(mv(odd, ko), ko, qo)]
    ns = norm(re+ro)
    kernel = dot(w, ke).absupper()+E*norm(ke)
    error = ns.upper()/gap.lower()+kernel.upper()
    below(error, '2.33e9', 'preimage_error')
    nk = norm(ke+ko)
    nh = inflate(nk, error)
    require(nh.lo > 0, 'positive reduced-preimage norm')
    rho = gap*nh/nq
    bracket(rho, '5.25e-30', '5.26e-30', 'full_ratio')
    report['preimage'] = dict(candidate_even=ke, candidate_odd_imag=ko,
                            residual_even=re, residual_odd_imag=ro, residual_norm=ns,
                            kernel_upper=kernel, error=error, norm_candidate=nk, norm=nh,
                            ratio=rho)

    u = [inflate(v, E) for v in w]
    x = [v/(rootL*overlap) for v in u]
    beta = [J()]+[j*J.pair(data['full_matrix'][120+j][120]) for j in range(1, 121)]
    y, k0 = t*L/(2*pi), rootL*sinh/pi
    # Compute S from the frequency sum itself, rather than from value/(k0*sqrt(L)).
    S = x[0]/y+dot(x[1:], [root2*y/(J(j*j)+y.square()) for j in range(1, 121)])
    original_S = J.pair(old['commutator_ansatz']['f_negative_imag'])
    require(max(S.lo, original_S.lo) <= min(S.hi, original_S.hi), 'independent f overlap')
    scale = k0*S
    c = dot(x[1:], [root2*j*beta[j] for j in range(1, 121)])
    bracket(c, '-1447', '-1446', 'c_cancellation')
    h = [J()]+[-scale/c*x[j]*j*j for j in range(1, 121)]
    rem = [erow[0]]+[erow[j]-scale/c*root2*j*beta[j] for j in range(1, 121)]
    nr, nhb = norm(rem+orow), norm(h)
    rel = nr/nq
    cost = gap*nhb/nq
    bound = rel+cost
    bracket(rel, '0.02196', '0.02197', 'remainder_ratio')
    below(cost, '7e-31', 'explicit_cost')
    below(bound, '0.022', 'commutator_bound')
    report['second_commutator'] = dict(x_even=x, beta_positive=beta, f_negative_imag=S,
                                     scale=scale, c=c, partial_preimage_even=h,
                                     partial_preimage_norm=nhb, residual_even=rem,
                                     residual_odd_imag=orow, residual_norm=nr,
                                     relative_remainder=rel, relative_cost=cost, bound=bound)

    av = [-j*beta[j]/(J(j*j)+y.square()) for j in range(1, 121)]
    a = dot(x[1:], [root2*v for v in av])
    require(not a.lo <= 0 <= a.hi, 'nonzero direct ansatz scalar')
    direct_scale = scale/a
    dre = [-direct_scale*a]+[root2*direct_scale*(v-a) for v in av]
    dro = [-root2*direct_scale*beta[j]*y/(J(j*j)+y.square()) for j in range(1, 121)]
    direct = norm(dre+dro)/nq
    excess = direct-1
    bracket(excess, '2.2592e-29', '2.2593e-29', 'direct_ansatz_excess')
    report['direct_ansatz'] = dict(a=a, residual_even=dre, residual_odd_imag=dro,
                                  ratio=direct, excess=excess)
    report['outcome'] = 'AUDIT_PASSED'
    print('full ratio', show(rho), 'required (5.25e-30, 5.26e-30)', flush=True)
    print('c', show(c), 'required (-1447, -1446)', flush=True)
    print('commutator bound', show(bound), 'required <0.022; R retained on remainder', flush=True)
    print('direct ansatz excess', show(excess), 'required (2.2592e-29, 2.2593e-29)', flush=True)
except Exception as exc:
    report['outcome'] = 'FAILED'
    if repr(exc) not in report['failures']:
        report['failures'].append(repr(exc))
    raise
finally:
    save()
    print('RESULT', report['outcome'], 'failures', report['failures'],
          'full certificate', OUTPUT, 'replay', REPLAY, flush=True)
