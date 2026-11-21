"""Complete fixed 64-mode compression, elementary series, directed intervals.

All proposals are untrusted until the directed congruence test. No form
parameter changes and no external numerical data. See canonical proof.
"""
import hashlib
import json
import math
import runpy
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE/'certify-455.py'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == '064e75d04fb24d0d3c47720652672166df78255f97a298170bffd8eb2b574afd'
lib = runpy.run_path(str(SOURCE))
I, A, PI, UP, DOWN = (lib[k] for k in ('I', 'A', 'PI', 'UP', 'DOWN'))
oldpath = HERE/'compression-463.json'
old = json.loads(oldpath.read_text())
D, N, K, DEG, END = 64, 512, 32, 144, 2**180


def ipow(x, n):
    y = I(1)
    while n:
        if n % 2:
            y *= x
        x = x.sq()
        n //= 2
    return y


def saved(x): return I(x['lo'], x['hi'])
def jm(m): return [[x.json() for x in row] for row in m]
def mag(x): return max(x.lo.copy_abs(), x.hi.copy_abs())
def symerr(x): return I(x.hi.copy_negate(), x.hi)
def zeros(): return [[I(0) for _ in range(D)] for _ in range(D)]

# The same exact centered integer moments serve both types of inverse sums.
# w=2j-3J+1, J<=j<2J; odd powers sum to zero. Telescoping (w+1)^t-(w-1)^t
# yields the recurrence below; every division is checked exact.
S = {p: I(0) for p in range(2, 2*K+3)}
G = {p: I(0) for p in range(2, K+2)}
blocks = []
J = N
while J < END:
    moments = [J]
    for l in range(2, DEG+1, 2):
        num = J**(l+1)-sum(math.comb(l+1, i)*moments[(l+1-i)//2]
                           for i in range(3, l+2, 2))
        val, rem = divmod(num, l+1)
        assert rem == 0 and val >= 0
        moments.append(val)
    record = {'J': J, 'response': {}, 'integer': {}}
    for kind, sums, C, delta_den in (
        ('response', S, I(6*J-1)/2, I(6*J-1)/2),
        ('integer', G, I(3*J-1)/2, I(3*J-1))):
        rho = I(J-1)/delta_den
        rho_power = ipow(rho, DEG+1)
        den2 = delta_den.sq()
        denpow = I(1)
        normalized = []
        for l, mom in zip(range(0, DEG+1, 2), moments):
            normalized.append(I(mom)/denpow)
            denpow *= den2
        cinv = C.reciprocal()
        cpow = cinv.sq()
        for p in sums:
            total = sum((math.comb(p+l-1,l)*normalized[l//2]
                         for l in range(0, DEG+1, 2)), I(0))*cpow
            ratio = rho*I(p+DEG+1)/(DEG+2)
            assert ratio.hi < 1
            error = J*cpow*math.comb(p+DEG, DEG+1)*rho_power/(1-ratio)
            enclosure = total+symerr(error)
            assert enclosure.lo > 0
            sums[p] += enclosure
            record[kind][str(p)] = {'sum': enclosure.json(), 'error': error.json()}
            cpow *= cinv
    blocks.append(record)
    J *= 2
    if len(blocks) % 24 == 0:
        print('Dyadic blocks:', len(blocks), '; next J bits:', J.bit_length(), flush=True)
# Integral comparison encloses the remaining infinite positive sums.
final_tails = {}
for kind, sums, C, spacing in (('response', S, I(4*J+1)/2, 2), ('integer', G, I(J), 1)):
    final_tails[kind] = {}
    for p in sums:
        tail = ipow(C.reciprocal(), p)+ipow(C.reciprocal(), p-1)/(spacing*(p-1))
        sums[p] += I(0, tail.hi)
        final_tails[kind][str(p)] = tail.json()
print('All inverse-power sums enclosed.', flush=True)

# gamma = H_(N-1)-log(N)+sum_(n>=N)(1/n-log(1+1/n)).
# Alternating log remainder <= sum n^(-K-1)/(K+1), here K=32.
gamma = sum((I(1)/j for j in range(1,N)), I(0))-I(N).ln()
for p in range(2,K+1):
    gamma += ((-1)**p)*G[p]/p
gamma_error = G[K+1]/(K+1)
gamma += symerr(gamma_error)
h0 = -gamma-PI/2-3*I(2).ln()-PI.ln()
k = [q*PI/A for q in range(D)]
u = [x.sq() for x in k]
norm = [(1/A).sqrt()]+[(2/A).sqrt()]*(D-1)
cN = I(4*N+1)/2
R = u[-1]/cN.sq()
assert R.hi < Decimal('.02')
powers = [[ipow(x,m) for m in range(K+1)] for x in u]
h, herrors = [], []
for q in range(D):
    v = h0+sum((2*u[q]/((I(4*j+1)/2)*((I(4*j+1)/2).sq()+u[q]))
               for j in range(N)), I(0))
    v += sum((2*((-1)**m)*powers[q][m+1]*S[2*m+3]
              for m in range(K)), I(0))
    error = 2*u[q]*ipow(u[q]/cN.sq(), K)*S[3]
    h.append(v+symerr(error))
    herrors.append(error.json())
print('Sharpened all 64 diagonal values.', flush=True)

# Rational Gram tail, total-degree expansion. Handles r=s and zero modes
# without divisions by a frequency or a frequency difference.
gram = zeros()
for j in range(N):
    c = I(4*j+1)/2
    row = [norm[q]*((-1)**q)*c/(c.sq()+u[q]) for q in range(D)]
    factor2 = 1-(-2*A*c).exp()
    for r in range(D):
        for s in range(r,D):
            gram[r][s] += row[r]*row[s]*factor2
            gram[s][r] = gram[r][s]
response_error = S[2]*(K+1)*ipow(R,K)/(1-R).sq()
exponential_error = (-2*A*cN).exp()*S[2]
for r in range(D):
    for s in range(r,D):
        v = I(0)
        for m in range(K):
            poly = sum((powers[r][t]*powers[s][m-t] for t in range(m+1)), I(0))
            v += ((-1)**m)*poly*S[2*m+2]
        v += symerr(response_error+exponential_error)
        gram[r][s] += norm[r]*norm[s]*((-1)**(r+s))*v
        gram[s][r] = gram[r][s]
# Reuse all nine full arithmetic matrices, all ten full moment Gram terms,
# and the pole from the prior complete assembly. Recheck their sums.
prime, penalty, pole = ( [[saved(x) for x in row] for row in old[key]]
                         for key in ('prime_matrix','penalty_matrix','pole_matrix'))
for r in range(D):
    for s in range(r,D):
        assert prime[r][s].json() == sum((saved(c['matrix'][r][s]) for c in old['prime_components']), I(0)).json()
        assert penalty[r][s].json() == sum((256*saved(m['row'][r])*saved(m['row'][s]) for m in old['all_ten_moment_rows']), I(0)).json()
        assert pole[r][s].json() == (saved(old['pole_row'][r])*saved(old['pole_row'][s])).json()
M = [[prime[r][s]+penalty[r][s]+pole[r][s]+gram[r][s]+(h[r] if r==s else 0)
      for s in range(D)] for r in range(D)]
assert all(M[r][s].json()==M[s][r].json() for r in range(D) for s in range(D))
print('Complete matrix assembled; every omitted response enclosed.', flush=True)

out = {
 'status': 'MATRIX_ENCLOSED_SIGN_PENDING',
 'matrix_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'inputs': {'ids':['L744','C744b','C744c','C744d'], 'interval_source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'old_assembly_sha256':hashlib.sha256(oldpath.read_bytes()).hexdigest(),
            'assessment':'drafts/literature/2026-11-11-five-cell-complete-compression-461.md'},
 'parameters':{'dimension':D,'K_cells':5,'penalty':256,'a':A.json(),'rational_prefix':N,
               'geometric_terms':K,'block_degree':DEG,'final_index':J},
 'inverse_power_sums':{'response':{str(p):x.json() for p,x in S.items()}, 'integer':{str(p):x.json() for p,x in G.items()}},
 'blocks':blocks, 'final_positive_tails':final_tails,
 'gamma':gamma.json(),'gamma_log_series_error':gamma_error.json(),
 'h': [x.json() for x in h], 'h_geometric_errors':herrors,
 'gram_geometric_error_before_normalization':response_error.json(),
 'gram_exponential_error_before_normalization':exponential_error.json(),
 'response_gram':jm(gram),'complete_matrix':jm(M),
 'max_entry_width':str(max(UP.subtract(x.hi,x.lo) for row in M for x in row)),
 'failures':[], 'scope':'complete fixed even compression only; no complement/neutral/global sign'}
path=HERE/'refined-464.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print('Matrix enclosure saved:',path,'; max entry width',out['max_entry_width'],flush=True)

