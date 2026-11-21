#!/usr/bin/env python3
"""Exact endpoint/error and direct nested-work ledger; no residual evaluation.

Analytic arguments are in C998b. This script neither runs a quadrature nor
certifies a norm. Old inputs and certificates are read without modification.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import numpy as np

B = Path(__file__).resolve().parent
checks, snapshots = [], {}


def check(name, value):
    checks.append({'name': name, 'pass': bool(value)})


def read(name):
    raw = (B / name).read_bytes()
    snapshots[name] = raw
    return json.loads(raw)


def enc(q):
    q = Q(q)
    return {'numerator': str(q.numerator), 'denominator': str(q.denominator)}


def dec(q):
    return Q(int(q['numerator']), int(q['denominator']))


def ceil(q):
    return -(-q.numerator // q.denominator)


def log_unit(r, terms=100):
    # 1 <= r <= 2: positive atanh expansion and its entire positive tail.
    assert 1 <= r <= 2
    z = (r - 1) / (r + 1)
    lo = 2 * sum((z**(2*k+1) / (2*k+1) for k in range(terms)), Q())
    hi = lo + 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return lo, hi


log2 = log_unit(Q(2))


def log_integer(n):
    k = n.bit_length()-1
    lo, hi = log_unit(Q(n, 2**k))
    return k*log2[0]+lo, k*log2[1]+hi


report = {'result': 'UNFINISHED', 'checks': checks}
old = read('jump-log-h1-bounds-654.json')
audit = read('jump-log-h1-audit-655.json')
archive_name = 'frozen-reference-proposal-652.npz'
snapshots[archive_name] = (B / archive_name).read_bytes()
check('frozen652 archive SHA256', sha256(snapshots[archive_name]).hexdigest() ==
      '2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6')
check('audit655 pins complete654 certificate',
      sha256(snapshots['jump-log-h1-bounds-654.json']).hexdigest() ==
      audit['input_sha256']['jump-log-h1-bounds-654.json'])
check('audit655 passes', audit['failures'] == [] and
      len(audit['checks']) == 41 and all(c['pass'] for c in audit['checks']))
with np.load(B / archive_name, allow_pickle=False) as data:
    free = data['free_middle_dyadics'].copy()
check('complete free array shape and finiteness',
      free.shape == (254, 3) and bool(np.isfinite(free).all()))
witness = old['exact_X_witness']
check('exact witness support and denominator', witness['denominator'] == 2**24 and
      witness['support_indices_zero_based'] == list(range(16))+list(range(1022, 1038)))
rows = witness['integer_columns_by_row']
check('96 integer endpoint entries', len(rows) == 32 and
      all(len(row) == 3 and all(type(x) is int for x in row) for row in rows))
columns = []
for j in range(3):
    q = [Q(*float(x).as_integer_ratio()) for x in free[:, j]]
    F = 6*sum((abs(Q(row[j], 2**24)) for row in rows[:16]), Q())
    H = 6*sum((abs(Q(row[j], 2**24)) for row in rows[16:]), Q())
    V = 6*sum(map(abs, q), Q())
    stored = audit['columns'][j]['all_bounds']
    check(f'column{j} exact envelopes match655',
          (F, H, V) == tuple(dec(stored[k]) for k in ['F', 'H', 'V']))
    check(f'column{j} uniform envelopes', F+H < 32 and V < 16)
    counts = [sum(c != 0 for c in q[p::2]) for p in [0, 1]]
    check(f'column{j} both free parities nonzero', counts == [127, 127])
    columns.append({'column': j, 'F': enc(F), 'H': enc(H), 'V': enc(V),
                    'nonzero_even_odd': counts})
report['columns'] = columns

log3 = log_integer(3)
alo, ahi = log3[0]/4, log3[1]/4
check('a and log2 elementary bounds', Q(1, 4) < alo < ahi < Q(3, 10) and
      Q(3, 8) < log2[0] < log2[1] < 1)
report['a_interval'] = {'lower': enc(alo), 'upper': enc(ahi)}

# Work on normalized x/a in [0,2]; symmetry reduces to [0,1].
events = [(Q(i, 286), Q(i, 286), 'grid:'+str(i)) for i in range(1, 286)]
for n in [29,31,32,37,41,43,47,49,53,59,61,64,67,71,73,79]:
    lnlo, lnhi = log_integer(n)
    b = 6 if n*n < 3**7 else 7
    xlo, xhi = 4*lnlo/log3[1]-2*b, 4*lnhi/log3[0]-2*b
    if xlo > 1:
        xlo, xhi = 2-xhi, 2-xlo
    check(f'prime{n} normalized location in left half', 0 < xlo < xhi < 1)
    events.append((xlo, xhi, 'translation-pair:'+str(n)))
events.sort(key=lambda row: row[0])
check('301 left-half interior interfaces', len(events) == 301)
check('event widths less than2^-180', all(hi-lo < Q(1, 2**180) for lo, hi, _ in events))
gaps = [events[0][0], 1-events[-1][1]]
gaps += [events[i+1][0]-events[i][1] for i in range(len(events)-1)]
check('every neighboring gap exceeds2^-30', min(gaps) > Q(1, 2**30))
report['event_intervals_left_half'] = [
    {'name': name, 'lower': enc(lo), 'upper': enc(hi)} for lo, hi, name in events]
report['minimum_normalized_gap_lower'] = enc(min(gaps))

# Remove [0,a*2^-80], and symmetric endpoint, plus interface hulls
# expanded by a*2^-120 on either side. Each normalized hull width<4*2^-120.
A, V, L = Q(1408), Q(16), Q(81)
tau_upper = Q(3, 10*2**80)
endpoint_square = 4*tau_upper*(A*A+V*V*(L*L+2*L+2))
endpoint_moment = 4*tau_upper*(A+V*(L+1))
strip_length = 603*4*Q(3, 10*2**120)
interior_amplitude = A+V*L
strip_square = strip_length*interior_amplitude**2
strip_moment = 2*strip_length*interior_amplitude
check('full endpoint squared mass<2^-54', endpoint_square < Q(1, 2**54))
check('each endpoint moment allowance<2^-68', endpoint_moment < Q(1, 2**68))
check('full interface squared mass<2^-87', strip_square < Q(1, 2**87))
check('each interface moment allowance<2^-97', strip_moment < Q(1, 2**97))
report['excluded_neighborhoods'] = {
    'tau_over_a': enc(Q(1, 2**80)), 'interface_radius_over_a': enc(Q(1, 2**120)),
    'A': enc(A), 'V': enc(V), 'interior_amplitude': enc(interior_amplitude),
    'endpoint_squared_mass_upper': enc(endpoint_square),
    'endpoint_each_moment_upper': enc(endpoint_moment),
    'interface_squared_mass_upper': enc(strip_square),
    'interface_each_moment_upper': enc(strip_moment)}

# Shared inner Gauss nodes for ALL output t in [tau,a]. The h coefficients
# are 2^-80,2^-80,2^-79,...,2^-1 times a, hence81 panels in all.
lengths = [Q(1, 2**80)] + [Q(1, 2**k) for k in range(80, 0, -1)]
check('81 complete inner input panels', len(lengths) == 81 and sum(lengths) == 1)
panels = []
for i, factor in enumerate(lengths):
    low, high = ceil(1020*alo*factor), ceil(1020*ahi*factor)
    check(f'inner panel{i} exact degree ceiling', low == high)
    n = 32+high
    panels.append({'index': i, 'h_over_a': enc(factor), 'n': n, 'gauss_points': n+1})
inner_nodes = sum(p['gauss_points'] for p in panels)
inner_error = 81*V/Q(2**64)
check('entire inner error<2^-53', inner_error < Q(1, 2**53))
outer_half_lower = 302*37
contributions = 6*outer_half_lower*inner_nodes
budget = 100_000_000
check('direct nested contributions exceed execution budget', contributions > budget)
report['inner_panels'] = panels
report['work'] = {
    'distinct_half_outer_nodes_lower': outer_half_lower,
    'inner_nodes_per_parity_value': inner_nodes,
    'parity_column_densities': 6,
    'real_coefficient_kernel_contributions_lower': contributions,
    'execution_budget_contributions': budget,
    'inner_truncation_error_upper_each_value': enc(inner_error),
    'inner_required_threshold': enc(Q(1, 2**53)),
    'included_reuse': ['common inner density values', 'shared denominators across six densities',
                      'complete reflected outer-point reuse'],
    'excluded_work': ['Gauss-node generation', 'scalar enclosures', 'outer integration',
                      'other action terms', 'forcing suffix', 'projection and square root'],
    'scope': 'lower work count for prescribed direct summation; not a necessary complexity lower bound'}
check('all input bytes preserved', all((B/name).read_bytes() == raw for name, raw in snapshots.items()))
failures = [c['name'] for c in checks if not c['pass']]
report['failures'] = failures
report['unresolved'] = ['outer quadrature and its complete analytic bounds',
    'finite scalar and node errors, complete forcing evaluation and projection errors',
    'all three residual norm intervals and their widths', 'inverse pairings and signs',
    'original source/core/c_* contracts']
report['input_sha256'] = {name: sha256(raw).hexdigest() for name, raw in snapshots.items()}
report['script_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
report['result'] = 'DIRECT_NESTED_WORK_STOP_PARTIAL_ERROR_LEDGER' if not failures else 'FAIL'
report['summary'] = {'checks_passed': len(checks)-len(failures), 'checks_total': len(checks),
    'inner_nodes': inner_nodes, 'contributions_lower': contributions, 'budget': budget,
    'requested_norm_width': '1e-4', 'actual_norm_intervals': 'NOT_COMPUTED', 'failures': failures}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2)+'\n')
print(report['result'])
print(json.dumps(report['summary'], sort_keys=True))
print('Full certificate:', out.relative_to(B.parent.parent))
if failures:
    raise SystemExit(1)
