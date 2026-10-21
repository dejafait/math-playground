"""Exact local filters of the cited PSS Theorem 1.1 signed list."""
import json
from math import gcd, isqrt
from pathlib import Path

triples = []
for x, y, z in [(1,-1,0), (1,0,1), (0,1,1), (3,-2,1),
                (71,-17,2), (2213459,1414,65), (15312283,9262,113),
                (21063928,-76271,17)]:
    triples.extend([(x,y,z), (-x,-y,-z) if x == 0 else (-x,y,z)])
rows = []
failures = []
for i, (x,y,z) in enumerate(triples, 1):
    difference = x*x + y**3 - z**7
    common = gcd(gcd(x,y),z)
    if difference or common != 1:
        failures.append(f"row {i}: equation={difference}, gcd={common}")
    n = isqrt(x) if x > 0 else None
    square = x > 0 and n*n == x
    signs_743 = x > 0 and y < 0 and z < 0
    signs_374 = x > 0 and y < 0 and z > 0
    rows.append(dict(row=i, triple=[x,y,z], equation_difference=difference,
                     gcd=common, signs_743=signs_743, signs_374=signs_374,
                     positive_square=square,
                     square_bounds=[n,n*n,(n+1)*(n+1)] if x > 0 else None,
                     survivor_743=signs_743 and square,
                     survivor_374=signs_374 and square))
counts = {p: sum(r['survivor_'+p] for r in rows) for p in ['743','374']}
result = dict(source='Poonen–Schaefer–Stoll, Duke Math. J. 137 (2007), Theorem 1.1',
              rows=rows, failures=failures, actual_survivors=counts,
              required_survivors={'743':0, '374':0})
path = Path(__file__).with_name('remaining-placements.json')
path.write_text(json.dumps(result, indent=2)+'\n')
print(f"rows={len(rows)}; failures={failures}; actual={counts}; required=0 each; certificate={path}")
for r in rows:
    if r['signs_743'] or r['signs_374']:
        print(f"sign-compatible row {r['row']}: {r['triple']}; square bounds={r['square_bounds']}; square={r['positive_square']}")
if failures or any(counts.values()):
    raise SystemExit(1)
