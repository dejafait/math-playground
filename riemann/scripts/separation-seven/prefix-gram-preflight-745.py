"""Exact, small preflight; never evaluate a Gram entry or density node."""
from fractions import Fraction as F
from functools import cmp_to_key
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
OLD = BASE / 'defect-window-fixed-pair-707.json'
WITNESS = BASE / 'defect-window-fixed-pair-707-witness.json'
OUT = BASE / 'prefix-gram-preflight-745.json'
checks = {}

def check(name, value):
    checks[name] = bool(value)

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))

weights = {}
for p in range(2, 4096):
    if not prime(p):
        continue
    n = p
    while n < 4096:
        if 3**13 < n*n < 3**15:
            weights[n] = p
        n *= p
ns = sorted(weights)
check('334 prime powers', len(ns) == 334)
check('identity 2187 retained', 2187 in ns)

# For each interior breakpoint z=log(n)-a*ell, exp(2z)=n^2/3^a.
# All comparisons below are integer products, not rounded logarithms.
events = [(n, 14, 1) if n > 2187 else (n, 13, -1)
          for n in ns if n != 2187]
def compare(u, v):
    delta = u[0]**2 * 3**v[1] - v[0]**2 * 3**u[1]
    return (delta > 0) - (delta < 0)
events.sort(key=cmp_to_key(compare))
check('333 distinct interior events', len(events) == 333 and
      all(compare(u, v) < 0 for u, v in zip(events, events[1:])))
check('all events interior', all(3**a < n*n < 3**(a+1)
      for n, a, _ in events))

active = {n for n in ns if n <= 2187}
counts = [len(active)]
panel_active = [sorted(active)]
for n, _, direction in events:
    if direction == 1:
        check(f'enter {n} inactive', n not in active)
        active.add(n)
    else:
        check(f'exit {n} active', n in active)
        active.remove(n)
    counts.append(len(active))
    panel_active.append(sorted(active))
check('334 open panels', len(counts) == 334)
check('identity in every panel', all(2187 in row for row in panel_active))
incidence = sum(counts)
independent_incidence = 0
for n in ns:
    if n == 2187:
        independent_incidence += 334
    else:
        pos = next(i for i, event in enumerate(events) if event[0] == n)
        independent_incidence += 333-pos if n > 2187 else pos+1
check('independent incidence counts agree', incidence == independent_incidence)

old = json.loads(OLD.read_text())['actual_intervals']
iv = {k: {end: F(value) for end, value in old[k].items()}
      for k in ('energy_f', 'energy_g', 'pairing')}
flo, glo = iv['energy_f']['lo'], iv['energy_g']['lo']
plo, phi = iv['pairing']['lo'], iv['pairing']['hi']
check('energies > .9998', min(flo, glo) > F('0.9998'))
check('0 < pairing < .922', 0 < plo <= phi < F('0.922'))
eigen_floor = F('0.9998') - F('0.922')
det_floor = F('0.9998')**2 - F('0.922')**2
check('leading block positive', eigen_floor > 0 and det_floor > 0)

degree_nodes, guaranteed_modes, cap = 32, 510, 10**8
mandatory_products = degree_nodes * guaranteed_modes * incidence
check('mandatory products exceed complete cap', mandatory_products > cap)
per_node_order = guaranteed_modes * incidence
max_affordable_order = cap // per_node_order
check('favorable direct-density allowance at most 3 nodes per panel',
      max_affordable_order == 3)
check('frozen witness hash', sha256(WITNESS.read_bytes()).hexdigest() ==
      '99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a')
failures = [name for name, ok in checks.items() if not ok]
data = {
    'task': 'fixed aggregate256 direct-density Gauss preflight745',
    'input_sha256': {p.name: sha256(p.read_bytes()).hexdigest()
                     for p in (OLD, WITNESS)},
    'prime_powers_and_base_primes': weights,
    'ordered_events': [{'n': n, 'a': a, 'direction': direction}
                       for n, a, direction in events],
    'active_counts': counts,
    'panel_active_sets': panel_active,
    'incidence': incidence,
    'independent_incidence': independent_incidence,
    'leading_block': {
        'input_intervals': {k: {end: str(v) for end, v in value.items()}
                            for k, value in iv.items()},
        'lambda_min_strict_lower': str(eigen_floor),
        'determinant_strict_lower': str(det_floor)},
    'prescription': {'Gauss_nodes_per_open_panel': degree_nodes,
                     'nonzero_free_derivative_modes_counted': guaranteed_modes,
                     'rates': 256,
                     'mandatory_mode_products': mandatory_products,
                     'products_per_common_panel_node_order': per_node_order,
                     'max_order_from_products_alone': max_affordable_order,
                     'complete_work_cap': cap,
                     'excess': mandatory_products-cap},
    'scope': 'One direct-density evaluation loop only; no lower bound for reassociated or optimized algorithms.',
    'unpaid': ['density quadrature and same-panel cusp error',
               'all node/value/location/atom/rounding errors',
               'full K14 and both exact P0 moment enclosures',
               'C(0), d0 and all signed entry certification',
               'sufficient precision, byte storage and remaining work'],
    'no_entry_or_density_evaluation': True,
    'checks': checks, 'failures': failures,
}
OUT.write_text(json.dumps(data, indent=2) + '\n')
print(f'Checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}')
print(f'Active incidences: {incidence}; mandatory products: {mandatory_products}; required <= {cap}')
print(f'Leading lambda_min > {eigen_floor}; determinant > {det_floor}')
print(f'Certificate: {OUT.relative_to(BASE.parent.parent)}')
raise SystemExit(bool(failures))
