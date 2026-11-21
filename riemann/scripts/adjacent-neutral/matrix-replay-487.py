#!/usr/bin/env python3
"""Replay every saved block matrix operation, not the analytic input proofs."""
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('arithmetic487',HERE/'matrix-enclosure-487.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
path = HERE/'matrix-enclosure-487.json'
data = json.loads(path.read_text())
S = int(data['interval_denominator'])
assert S==m.S


def ball(x):
    return m.B(int(x['lower_numerator']),int(x['upper_numerator']))


checks = {'coefficient_artifact_sha256': hashlib.sha256(
    (HERE.parent.parent/data['coefficient_artifact']).read_bytes()).hexdigest()
    ==data['coefficient_artifact_sha256']}
exact = {}
for sign in ('-1','1'):
    d = data['signs'][sign]
    projected = [[ball(x) for x in row] for row in d['projected_moments']]
    head = [[ball(x) for x in row] for row in d['unsymmetrized_head']]
    gram = [[ball(x) for x in row] for row in d['total_gram']]
    saved_cov = [[ball(x) for x in row] for row in d['complete_covariance']]
    saved_s = [[ball(x) for x in row] for row in d['schur']]
    checks[sign+'_all_257_rows'] = len(projected)==3 and all(len(row)==257 for row in projected)
    cov = [[gram[i][j]-m.interval_dot(projected[i],projected[j]) for j in range(3)] for i in range(3)]
    schur = [[(head[i][j]+head[j][i]).integer_div(2)-cov[i][j]*m.B.rational(250,171)
              for j in range(3)] for i in range(3)]
    checks[sign+'_all_covariance_endpoints'] = all(
        cov[i][j].json()==saved_cov[i][j].json() for i in range(3) for j in range(3))
    checks[sign+'_all_schur_endpoints'] = all(
        schur[i][j].json()==saved_s[i][j].json() for i in range(3) for j in range(3))
    lower = min(schur[i][i].lo-sum(max(abs(schur[i][j].lo),abs(schur[i][j].hi))
                for j in range(3) if j!=i) for i in range(3))
    checks[sign+'_gershgorin_endpoint'] = lower==int(d['gershgorin_lower_numerator'])
    threshold = F(5879,10000) if sign=='-1' else F(2331,2000)
    checks[sign+'_conservative_reported_lower_bound'] = F(lower,S)>threshold
    widths = [x.hi-x.lo for matrix in (head,gram,cov,schur) for row in matrix for x in row]
    checks[sign+'_reported_width_below_1_046e_minus_236'] = F(max(widths),S)<F(1046,10**239)
    exact[sign] = {'gershgorin_lower':m.scalar.frac_json(F(lower,S)),
                   'maximum_matrix_width':m.scalar.frac_json(F(max(widths),S)),
                   'conservative_lower':m.scalar.frac_json(threshold)}
result = {'scope':'Saved3 by3 matrix operations only; full255 by255 margin unproved.',
          'checks':checks,'exact_bounds':exact,'failures':[k for k,v in checks.items() if not v]}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(f'Saved matrix replay: {sum(checks.values())}/{len(checks)}; failures {result["failures"]}')
print('Principal lower bounds >0.5879 and>1.1655; widths<1.046e-236; full matrix threshold1/25 remains unpaid.')
print(f'Full replay evidence: {out}')
if result['failures']: raise SystemExit(1)
