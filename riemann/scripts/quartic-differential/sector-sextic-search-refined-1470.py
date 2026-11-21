"""Bounded floating discovery only; exact proof/certification is separate."""
import json
from pathlib import Path
import numpy as np

rng = np.random.default_rng(1470)
t = 5 / 18
histogram = {}
candidates = []
N = 80000
for k in range(N):
    if k < N // 4:
        real_roots = np.zeros(4)
    elif k < 3 * N // 4:
        radius = 10 ** rng.uniform(-3, 1.5)
        real_roots = np.array([-radius, -radius, radius, radius])
    else:
        real_roots = np.sort(rng.normal(0, 1, 4)) * 10 ** rng.uniform(-2, 1)
        real_roots -= real_roots.mean()
    u = rng.uniform(-12, 12)
    v = 10 ** rng.uniform(-2, 1.5)
    p = np.polymul(np.poly(real_roots), [1, -2*u, u*u+v*v])
    out = np.polyadd(np.polyadd(p, np.polyder(p)), t*np.polyder(p, 2))
    if k < N // 4:
        out_test = out[:-2]  # exact x^2 factor for the fourfold-zero inputs
        nreal = sum(abs(z.imag) < 1e-7 for z in np.roots(out_test)) + 2
    else:
        out_test = out
        nreal = sum(abs(z.imag) < 1e-7 for z in np.roots(out_test))
    nreal = int(nreal)
    histogram[nreal] = histogram.get(nreal, 0) + 1
    if nreal == 2:
        candidates.append({'real_roots': real_roots.tolist(), 'u': u, 'v': v,
                           'input_descending': p.tolist(),
                           'output_descending': out.tolist(),
                           'roots_test': [[float(z.real), float(z.imag)] for z in np.roots(out_test)]})
        if len(candidates) == 5:
            break

record = {'status': 'DISCOVERY_ONLY_NOT_A_PROOF', 'seed': 1470, 'families': '20000 fourfold, 40000 two-double, 20000 simple-root samples',
          'q_ascending': ['1', '1', '5/18'], 'iterations': k+1,
          'cap': N, 'approximate_real_count_histogram': histogram,
          'candidates': candidates,
          'required': 'exact rational witness; sector; universal preservation; multiplicity-aware counts (2,4)',
          'limits': 'One quadratic endpoint and a finite input sample only; floating roots are not certification.',
          'failures': [],
          'execution_note': 'Initial run failed JSON serialization on a numpy.int64 histogram key; corrected to int and rerun with identical seed.'}
path = Path(__file__).with_name('sector-sextic-search-refined-1470.json')
path.write_text(json.dumps(record, indent=2)+'\n')
print('Discovery only:', k+1, 'of', N, 'inputs; candidate count', len(candidates))
print('Approximate real count histogram:', histogram)
print('Required exact counts: input 4 real / output 2 real; no numerical claim certified.')
print('Execution failures:', record['failures'])
print('Full record:', path)
