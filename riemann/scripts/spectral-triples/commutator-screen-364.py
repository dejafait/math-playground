"""Point-Decimal diagnostic ONLY for the approved single cell; not a certificate."""
from decimal import Decimal as D, getcontext
from pathlib import Path
import hashlib
import json
import time

getcontext().prec = 160
HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'finite-parity-359.json'
OUTPUT = Path(__file__).with_suffix('.json')
started = time.monotonic()
data = json.loads(SOURCE.read_text())
report = dict(kind='NONRIGOROUS point-Decimal diagnostic',
              input_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              cell=dict(lambda_squared=13, N=120, z='i/4'),
              precision=160, failures=[], outcome='IN_PROGRESS')

def save():
    report['elapsed_seconds'] = time.monotonic() - started
    OUTPUT.write_text(json.dumps(report, indent=2, default=str) + '\n')

def mid(pair):
    return (D(pair[0]) + D(pair[1])) / 2

def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), D(0))

def norm(x):
    return dot(x, x).sqrt()

def mv(A, x):
    return [dot(row, x) for row in A]

def ldl(A):
    n = len(A)
    H = [[D(int(i == j)) for j in range(n)] for i in range(n)]
    piv = []
    for j in range(n):
        p = A[j][j] - sum((H[j][r]**2*piv[r] for r in range(j)), D(0))
        if not p:
            raise ArithmeticError('point zero pivot')
        piv.append(p)
        for i in range(j+1, n):
            H[i][j] = (A[i][j] - sum((H[i][r]*H[j][r]*piv[r]
                                     for r in range(j)), D(0))) / p
    return H, piv

def solve(factors, rhs):
    H, piv = factors
    n = len(rhs)
    y = [D(0)] * n
    for i in range(n):
        y[i] = rhs[i] - dot(H[i][:i], y[:i])
    v = [y[i]/piv[i] for i in range(n)]
    out = [D(0)] * n
    for i in reversed(range(n)):
        out[i] = v[i] - sum((H[j][i]*out[j] for j in range(i+1, n)), D(0))
    return out

def inverse_eigen(A, factors, seed, previous=()):
    v = [D(int(i == seed)) for i in range(len(A))]
    for iteration in range(32):
        v = solve(factors, v)
        for u in previous:
            alpha = dot(u, v)
            v = [a-alpha*b for a, b in zip(v, u)]
        nv = norm(v)
        v = [a/nv for a in v]
        if v[seed] < 0:
            v = [-a for a in v]
    Av = mv(A, v)
    lam = dot(v, Av)
    residual = norm([a-lam*b for a, b in zip(Av, v)])
    return dict(value=lam, vector=v, residual=residual, iterations=32)

try:
    matrices = {name: [[mid(x) for x in row] for row in data[name+'_matrix']]
                for name in ['even', 'odd']}
    even, odd = matrices['even'], matrices['odd']
    ef, of = ldl(even), ldl(odd)
    print('point LDL factors built', flush=True)
    ground = inverse_eigen(even, ef, 0)
    second = inverse_eigen(even, ef, 1, [ground['vector']])
    first_odd = inverse_eigen(odd, of, 0)
    report['eigenpairs'] = dict(ground=ground, second_even=second, first_odd=first_odd)
    save()
    for name, pair in report['eigenpairs'].items():
        print(name, 'value', format(pair['value'], '.8E'),
              'residual', format(pair['residual'], '.3E'), flush=True)

    L, pi = mid(data['constants']['L']), mid(data['constants']['pi'])
    root2 = D(2).sqrt()
    # At i/4, the Fourier row has real even and imaginary odd components.
    t = D(1)/4
    sinh = ((L*t/2).exp() - (-L*t/2).exp())/2
    pref = 2*sinh/L.sqrt()
    erow = [pref/t]
    orow = []
    for j in range(1, 121):
        freq = 2*pi*j/L
        erow.append(root2*pref*t/(freq*freq+t*t))
        orow.append(-root2*pref*freq/(freq*freq+t*t))
    boundary = [1/L.sqrt()] + [root2/L.sqrt()]*120
    u = ground['vector']
    overlap = dot(boundary, u)
    xi = [a/overlap for a in u]
    value = dot(erow, xi)
    qe = [a-value*b for a, b in zip(erow, boundary)]
    qo = orow
    epsilon = ground['value']
    # This deliberately uses a full inverse: it measures the ratio and
    # does not purport to supply the sought commutator factorization.
    Te = [[even[i][j] - (epsilon if i == j else 0) + u[i]*u[j]
           for j in range(121)] for i in range(121)]
    To = [[odd[i][j] - (epsilon if i == j else 0)
           for j in range(120)] for i in range(120)]
    he, ho = solve(ldl(Te), qe), solve(ldl(To), qo)
    alpha = dot(he, u)
    he = [a-alpha*b for a, b in zip(he, u)]
    g = min(second['value'], first_odd['value'])-epsilon
    nq = (dot(qe, qe)+dot(qo, qo)).sqrt()
    nh = (dot(he, he)+dot(ho, ho)).sqrt()
    rho = g*nh/nq
    report.update(boundary_overlap=overlap, xi_even=xi, fourier_value=value,
                  q_even=qe, q_odd_imag=qo, h_even=he, h_odd_imag=ho,
                  actual_gap_estimate=g, row_norm_estimate=nq,
                  preimage_norm_estimate=nh, ratio_estimate=rho,
                  threshold='0.1', outcome='DIAGNOSTIC_ONLY')
    print('DIAGNOSTIC rho', format(rho, '.8E'), 'required <=0.1',
          'gap', format(g, '.8E'), 'boundary overlap', format(overlap, '.5E'), flush=True)
except Exception as exc:
    report['failures'].append(repr(exc))
    report['outcome'] = 'FAILED'
    raise
finally:
    save()
    print('failures', report['failures'], 'full diagnostic', OUTPUT, flush=True)
