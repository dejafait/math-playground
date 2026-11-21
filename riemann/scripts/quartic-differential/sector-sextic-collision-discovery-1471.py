"""Bounded collision discovery. Floating screening is NOT a certificate."""
import json
from pathlib import Path
import numpy as np

rng = np.random.default_rng(1471)
cap = 60000
counts = {'singular_or_ill_conditioned': 0, 'nonreal_input_pair': 0,
          'remaining_quartic_two_real': 0, 'other_remaining_counts': {}}
candidates = []
for k in range(cap):
    t = 5/18 if k < cap//2 else rng.uniform(1/4, 5/18)
    # Locate the prescribed collision at zero. Roots vary relative to it.
    radius = 10**rng.uniform(-2, 1)
    center = rng.uniform(-8, 4)
    if k % 3 == 0:
        roots = center + radius*np.array([-1, -1, 1, 1])
    elif k % 3 == 1:
        roots = np.full(4, center)
    else:
        roots = center + radius*np.sort(rng.normal(size=4))
    r = np.poly(roots)[::-1]
    a, b = r[0]+2*t*r[1], r[0]+r[1]+2*t*r[2]
    c, d = r[0]+2*r[1]+6*t*r[2], r[1]+2*r[2]+6*t*r[3]
    rhs1, rhs2 = -2*t*r[0], -2*r[0]-6*t*r[1]
    delta = a*d-b*c
    if abs(delta) < 1e-10*max(1, abs(a*d), abs(b*c)):
        counts['singular_or_ill_conditioned'] += 1
        continue
    B, C = (rhs1*d-b*rhs2)/delta, (a*rhs2-rhs1*c)/delta
    margin = C-B*B/4
    if margin <= 1e-8*max(1, abs(C), B*B):
        continue
    counts['nonreal_input_pair'] += 1
    p = np.polynomial.polynomial.polymul(r, [C, B, 1])
    out = np.array([p[j]+((j+1)*p[j+1] if j<6 else 0)
                    +(t*(j+2)*(j+1)*p[j+2] if j<5 else 0)
                    for j in range(7)])
    if k % 3 == 1:
        # A fourfold input root leaves an exact double output root.
        # Remove it before numerical roots: tiny imaginary roundoff is
        # not a nonreal pair. Remaining quartic is (x-center)^2*Q2.
        qa = out[5]+2*center
        qb = out[4]+2*center*out[5]+3*center*center
        roots_out = np.roots([1, qa, qb])
        nreal = 2+int(sum(abs(z.imag)<1e-6 for z in roots_out))
    else:
        roots_out = np.roots(out[2:][::-1])
        nreal = int(sum(abs(z.imag)<1e-6 for z in roots_out))
    if nreal == 2:
        counts['remaining_quartic_two_real'] += 1
        candidates.append({'t': float(t), 'real_input_roots': roots.tolist(),
                           'B': float(B), 'C': float(C),
                           'pair_margin': float(margin),
                           'input_ascending': p.tolist(),
                           'output_ascending': out.tolist(),
                           'remaining_roots': [[float(z.real),float(z.imag)] for z in roots_out]})
        break
    key = str(nreal)
    counts['other_remaining_counts'][key] = counts['other_remaining_counts'].get(key, 0)+1

record = {'status': 'DISCOVERY_ONLY_NOT_PROOF', 'seed': 1471,
          'iterations': k+1, 'cap': cap, 'counts': counts,
          'candidates': candidates,
          'required': 'Exact (2,4) witness including sector and universal preservation, or whole-class impossibility',
          'limits': 'Floating direct-collision screen for one quadratic factor; no exhaustiveness or exact count claim.',
          'failures': [],
          'rejected_preliminary_candidate': 'Seed1471 iteration2 had an exact retained double root numerically split by imaginary parts of size 9.32e-7. It was NOT a witness. Fourfold-input branches now remove that factor before screening; the same seed is replayed.'}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(record, indent=2)+'\n')
print('Collision discovery only:', record['iterations'], '/', cap)
print('Actual screening counts:', counts)
print('Required:', record['required'])
print('Candidates:', len(candidates), '; failures:', record['failures'])
print('Full record:', path)
