"""One rigorous interval-LDL attempt for the approved complete compression.

The positive response tail is retained as 0 <= T <= tau I. A positive
prefix would certify the full matrix; a failed interval pivot proves no
negative sign. Reuses accepted C744b diagonal enclosures and elementary
contracts. No unverified special function or floating sign is an input.
"""
import hashlib
import json
import runpy
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'certify-455.py'
BASE = HERE / 'certificate-455.json'
EXPECTED_SOURCE = '064e75d04fb24d0d3c47720652672166df78255f97a298170bffd8eb2b574afd'
EXPECTED_BASE = 'ffae7a92b9e072cf1632820fb243ca35fe56da2eda0a6ae6a9ec481c53ff58a6'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == EXPECTED_SOURCE
assert hashlib.sha256(BASE.read_bytes()).hexdigest() == EXPECTED_BASE
lib = runpy.run_path(str(SOURCE))
I, A, PI, ELL = (lib[x] for x in ('I', 'A', 'PI', 'ELL'))
sin_cos = lib['sincos']
UP, DOWN = lib['UP'], lib['DOWN']
base = json.loads(BASE.read_text())
D, N = 64, 2048


def saved(x):
    return I(x['lo'], x['hi'])


def zeros():
    return [[I(0) for _ in range(D)] for _ in range(D)]


def jmatrix(m):
    return [[x.json() for x in row] for row in m]


def magnitude(x):
    return max(x.lo.copy_abs(), x.hi.copy_abs())


def bilinear(m, z):
    return sum(((1 if r == s else 2)*z[r]*z[s]*m[r][s]
                for r in range(D) for s in range(r, D)), I(0))


checks = []


def check(name, condition):
    checks.append({'name': name, 'passed': bool(condition)})
    assert condition, name


check('all 64 accepted diagonals',
      [x['q'] for x in base['all_h_enclosures']] == list(range(D)))
check('same half width', base['constants']['a'] == A.json())
check('all nine active powers', [x['n'] for x in base['prime_terms']] ==
      [2, 3, 4, 5, 7, 8, 9, 11, 13])
check('ten physical moment indices',
      {(x['cell'], x['sigma']) for x in base['all_physical_moments']} ==
      {(j, s) for j in range(5) for s in (1, -1)})
k = [q*PI/A for q in range(D)]
k2 = [x.sq() for x in k]
norm = [(1/A).sqrt()] + [(2/A).sqrt()]*(D-1)
full = [x/I(2).sqrt() for x in norm]
h = [saved(x['h']) for x in base['all_h_enclosures']]
prime = zeros()
prime_components = []
for n, p, _ in lib['PRIMES']:
    delay = I(n).ln()
    half = A-delay/2
    factors, cosines = [], []
    for s in range(2*D-1):
        frequency = s*PI/A
        factors.append(half if s == 0 else sin_cos(frequency*half)[0]/frequency)
        cosines.append(sin_cos(frequency*delay/2)[1])
    weight = -2*I(p).ln()/I(n).sqrt()
    m = zeros()
    for r in range(D):
        for s in range(r, D):
            x, y = abs(r-s), r+s
            m[r][s] = weight*full[r]*full[s]*(
                factors[x]*cosines[y]+factors[y]*cosines[x])
            m[s][r] = m[r][s]
            prime[r][s] += m[r][s]
            prime[s][r] = prime[r][s]
    prime_components.append({'n': n, 'base_prime': p, 'matrix': jmatrix(m)})
print('All nine signed arithmetic matrices enclosed.', flush=True)

# All moment rows are physical full-interval rows, with the 1/sqrt(2).
trig = {(q, edge): sin_cos(q*edge*PI/5)
        for q in range(D) for edge in (-5, -3, -1, 1, 3, 5)}
moments, penalty = [], zeros()
for cell in range(5):
    le, re = 2*cell-5, 2*cell-3
    for sigma in (1, -1):
        beta = I(sigma)/2
        el, er = (-sigma*ELL/4).exp(), (sigma*ELL/4).exp()
        row = []
        for q in range(D):
            sl, cl = trig[q, le]
            sr, cr = trig[q, re]
            row.append(full[q]*(er*(beta*cr+k[q]*sr)-el*(beta*cl+k[q]*sl))
                       /(beta.sq()+k2[q]))
        moments.append({'cell': cell, 'sigma': sigma,
                        'row': [x.json() for x in row]})
        for r in range(D):
            for s in range(r, D):
                penalty[r][s] += 256*row[r]*row[s]
                penalty[s][r] = penalty[r][s]

responses, response_gram = [], zeros()
for j in range(N):
    c = I(4*j+1)/2
    factor = (1-(-2*A*c).exp()).sqrt()
    row = [norm[q]*((-1)**q)*c/(c.sq()+k2[q])*factor for q in range(D)]
    responses.append([x.json() for x in row])
    for r in range(D):
        for s in range(r, D):
            response_gram[r][s] += row[r]*row[s]
            response_gram[s][r] = response_gram[r][s]
    if j == 0:
        pole_row = [x*(A/2).exp()*(1-(-A).exp()).sqrt() for x in row]
    if (j+1) % 512 == 0:
        print('Response Gram prefix enclosed through j =', j, flush=True)
pole = [[pole_row[r]*pole_row[s] for s in range(D)] for r in range(D)]
prefix = [[prime[r][s]+penalty[r][s]+response_gram[r][s]+pole[r][s]
           +(h[r] if r == s else 0) for s in range(D)] for r in range(D)]

# ||b_j||^2 <= sum n_q^2/c_j^2; thus sum b_j b_j^T <= tau I.
# This is an operator bound, independent of the old scalar cancellation.
cn = I(4*N+1)/2
u2 = 1/cn.sq()+1/(2*cn)
sum_norm2 = sum((x.sq() for x in norm), I(0))
tau = sum_norm2*u2
tail_entry_magnitudes = [[norm[r]*norm[s]*u2 for s in range(D)] for r in range(D)]
complete_entries = zeros()
for r in range(D):
    for s in range(D):
        # Every term has the same sign (-1)^(r+s); include its full tail.
        upper = tail_entry_magnitudes[r][s].hi
        tail = I(0, upper) if (r+s) % 2 == 0 else I(upper.copy_negate(), 0)
        complete_entries[r][s] = prefix[r][s]+tail

# Exact LDL recurrences evaluated outward; stop at the first unpaid pivot.
lower = zeros()
pivots, failed = [], None
for j in range(D):
    numerator = prefix[j][j]-sum((lower[j][k].sq()*pivots[k]
                                 for k in range(j)), I(0))
    if numerator.lo <= 0:
        failed = {'index': j, 'interval': numerator.json(),
                  'reason': 'pivot lower endpoint is not strictly positive; no sign conclusion'}
        break
    pivots.append(numerator)
    lower[j][j] = I(1)
    for i in range(j+1, D):
        lower[i][j] = (prefix[i][j]-sum((lower[i][k]*lower[j][k]*pivots[k]
                                       for k in range(j)), I(0)))/numerator

z = [I(n)/base['witness']['denominator'] for n in base['witness']['numerators']]
witness_prefix = bilinear(prefix, z)
witness_complete = bilinear(complete_entries, z)
old_complete = json.loads((HERE/'complete-response-459.json').read_text())
old_value = saved(old_complete['complete_penalized_energy'])
check('old complete positive scalar intersects rebuilt full enclosure',
      max(witness_complete.lo, old_value.lo) <= min(witness_complete.hi, old_value.hi))
check('symmetric complete interval matrix',
      all(complete_entries[r][s].json() == complete_entries[s][r].json()
          for r in range(D) for s in range(D)))

max_diag_width = max(UP.subtract(x.hi, x.lo) for x in h)
max_prefix_radius_row_sum = Decimal(0)
for row in prefix:
    # Half-width of every entry bounds its distance to its exact midpoint.
    width_sum = sum((I(UP.subtract(x.hi, x.lo)) for x in row), I(0))/2
    max_prefix_radius_row_sum = max(max_prefix_radius_row_sum, width_sum.hi)

result = {
    'status': 'CERTIFIED_POSITIVE_COMPLETE_COMPRESSION' if len(pivots) == D else 'INCONCLUSIVE',
    'scope': 'Fixed complete even 64-mode penalty256 form only; no complement, neutral or global sign.',
    'parameters': {'K': 5, 'a': A.json(), 'ell': ELL.json(), 'dimension': D,
                   'penalty': 256, 'response_prefix_end_exclusive': N},
    'inputs': {'interval_source_sha256': EXPECTED_SOURCE, 'diagonal_certificate_sha256': EXPECTED_BASE,
               'ids': ['L744', 'C744b', 'C744c'], 'prior_assessment':
               'drafts/literature/2026-11-11-five-cell-complete-compression-461.md'},
    'constants': {'pi': PI.json(), 'c_N': cn.json(), 'U2': u2.json(),
                  'sum_basis_normalization_squares': sum_norm2.json()},
    'diagonal_enclosures': [x.json() for x in h],
    'prime_components': prime_components, 'prime_matrix': jmatrix(prime),
    'all_ten_moment_rows': moments, 'penalty_matrix': jmatrix(penalty),
    'all_prefix_response_rows': responses, 'response_prefix_gram': jmatrix(response_gram),
    'pole_row': [x.json() for x in pole_row], 'pole_matrix': jmatrix(pole),
    'prefix_matrix': jmatrix(prefix), 'complete_entrywise_enclosure': jmatrix(complete_entries),
    'tail_operator_enclosure': {'lower': '0 (positive semidefinite)', 'upper_scalar': str(tau.hi),
                                 'formula': 'sum_q n_q^2 * (c_N^-2+(2*c_N)^-1)'},
    'interval_ldl': {'positive_pivot_count': len(pivots), 'pivots': [x.json() for x in pivots],
                     'partial_unit_lower': jmatrix(lower), 'first_unpaid_pivot': failed},
    'error_budget': {'max_diagonal_interval_width': str(max_diag_width),
                    'prefix_entry_radius_row_sum_upper': str(max_prefix_radius_row_sum),
                    'tail_operator_upper': str(tau.hi),
                    'required': '64 strictly positive interval LDL pivots suffice; alternatively an exact direction needs a strictly negative complete upper enclosure'},
    'old_witness_consistency': {'prefix_value': witness_prefix.json(),
                              'complete_entrywise_value': witness_complete.json(),
                              'accepted_scalar_value': old_value.json()},
    'checks': checks, 'failures': [] if len(pivots) == D else ['interval LDL did not certify all 64 pivots'],
    'conclusion': 'Full sign established by PSD response-tail order.' if len(pivots) == D else
                  'No positive or negative complete sign certified. Failed pivots are not negative directions. No form parameter retuned.'}
path = HERE/'compression-463.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print('Result:', result['status'], '; positive pivots:', len(pivots), '/ required', D)
print('First unpaid pivot:', failed)
print('Prefix radius row-sum upper:', max_prefix_radius_row_sum)
print('Full response-tail operator upper:', tau.hi, '; required tail lower: 0 PSD')
print('Max accepted diagonal interval width:', max_diag_width)
print('Failures:', result['failures'])
print('Full certificate:', path)
