"""Independent literal-row check against the retained PSS Theorem 1.1 list."""
import json
from math import gcd, isqrt
from pathlib import Path

rows = [
    (1,-1,0), (-1,-1,0), (1,0,1), (-1,0,1),
    (0,1,1), (0,-1,-1), (3,-2,1), (-3,-2,1),
    (71,-17,2), (-71,-17,2), (2213459,1414,65),
    (-2213459,1414,65), (15312283,9262,113),
    (-15312283,9262,113), (21063928,-76271,17),
    (-21063928,-76271,17),
]
base = Path(__file__).parent
prior = json.loads((base/'remaining-placements.json').read_text())
failures = []
evidence = []
counts = {'743':0, '374':0}
sign_rows = {'743':[], '374':[]}
expected_bounds = {7:(1,1,4), 9:(8,64,81), 15:(4589,21058921,21068100)}
if len(prior['rows']) != 16:
    failures.append('prior row count differs from 16')
for i,(x,y,z) in enumerate(rows,1):
    difference = x**2+y**3-z**7
    common = gcd(gcd(abs(x),abs(y)),abs(z))
    n = isqrt(x) if x>0 else None
    bounds = [n,n*n,(n+1)*(n+1)] if n is not None else None
    square = x>0 and n*n==x
    signs = {'743':x>0 and y<0 and z<0, '374':x>0 and y<0 and z>0}
    result = dict(row=i,triple=[x,y,z],equation_difference=difference,gcd=common,
                  signs_743=signs['743'],signs_374=signs['374'],
                  positive_square=square,square_bounds=bounds,
                  survivor_743=signs['743'] and square,
                  survivor_374=signs['374'] and square)
    if difference!=0 or common!=1:
        failures.append(f'row {i}: equation/gcd failure')
    if i>len(prior['rows']) or result!=prior['rows'][i-1]:
        failures.append(f'row {i}: full prior evidence mismatch')
    for p in counts:
        if signs[p]: sign_rows[p].append(i)
        if signs[p] and square: counts[p]+=1
    if i in expected_bounds:
        b=expected_bounds[i]
        if tuple(bounds)!=b or not b[1]<x<b[2]:
            failures.append(f'row {i}: exact consecutive-square bound failed')
    evidence.append(result)
if sign_rows!={'743':[], '374':[7,9,15]}:
    failures.append('sign-compatible rows mismatch')
if counts!={'743':0,'374':0}:
    failures.append('zero-survivor threshold failed; inverse substitution required')
if prior['actual_survivors']!=counts or prior['required_survivors']!={'743':0,'374':0} or prior['failures']:
    failures.append('prior summary mismatch or prior failure')
output = dict(source='PSS Theorem 1.1; signed list retained in classification-scope assessment',
              rows=evidence, sign_compatible_rows=sign_rows,
              actual_survivors=counts,required_survivors={'743':0,'374':0},failures=failures,
              limitation='Checks cited classification applications; does not reprove completeness.')
path=base/'remaining-application-audit.json'
path.write_text(json.dumps(output,indent=2)+'\n')
print(f'rows={len(evidence)}; actual={counts}; required=0 each; failures={failures}; certificate={path}')
for i,b in expected_bounds.items():
    print(f'row {i}: {b[0]}^2={b[1]} < {rows[i-1][0]} < {b[2]}=({b[0]}+1)^2')
if failures: raise SystemExit(1)
