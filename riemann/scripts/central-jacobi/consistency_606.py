"""Inspect every leaf of step606's certificate; no independent interval replay."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

base = Path(__file__).resolve().parents[2]
p = base / 'scripts/central-jacobi/three-factor-certificate-606.json'
c = json.loads(p.read_text())
leaves = c['leaves']
paths = sorted(v['path'] for v in leaves)
errors = []
for v in leaves:
    if v['reason'] != 'symmetry_x_gt_y':
        lo,hi = map(F,v['bound'])
        if not lo <= hi or not (hi<0 or lo>0):
            errors.append(v['path'])
    if v['reason'] == 'b_negative' and F(v['bound'][1]) >= 0:
        errors.append(v['path'])
weight = sum((F(1,2**len(p)) for p in paths),F(0))
prefix_free = all(not b.startswith(a) for a,b in zip(paths,paths[1:]))
mins = {k:str(min(min(abs(F(v['bound'][0])),abs(F(v['bound'][1])))
                 for v in leaves if v['reason']==k))
        for k in ['b_negative','F1','F2']}
check = {
    'pass':not errors and prefix_free and weight==1 and c['pass'] and c['actual_unresolved']==0,
    'certificate_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
    'leaves_inspected':len(leaves),'prefix_free':prefix_free,'kraft_sum':str(weight),
    'sign_failures':errors,'minimum_stored_absolute_margins':mins,
    'qualification':'complete certificate consistency check; not an independent replay of leaf interval evaluations'}
out = base / 'scripts/central-jacobi/three-factor-consistency-606.json'
out.write_text(json.dumps(check,indent=2)+'\n')
print('certificate consistency:',check['pass'],'all',len(leaves),'leaves inspected;',
      'sign failures:',errors,'Kraft sum:',weight,'required:',1)
print('evidence:',out.relative_to(base))
