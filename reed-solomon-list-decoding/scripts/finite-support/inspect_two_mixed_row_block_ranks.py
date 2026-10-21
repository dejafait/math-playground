"""Resolve old-block singularity wording from complete audited matrices."""
import hashlib
import json
import sys
from pathlib import Path
from fractions import Fraction as F
from verify_simultaneous_eight_shell import det, enc
sys.set_int_max_str_digits(0)
root=Path(__file__).resolve().parent
source=root/'two-mixed-row-critical-audit.json'
data=json.loads(source.read_text())
rows=[]; failures=[]
for added in data['added_modes']:
    i=added['index']
    B=[[F(*v) for v in r] for r in added['base']]
    value=det(B)
    saved=F(*added['minors'][-1]['determinant'])
    agrees=value==saved
    expected=(value>0) if i==23 else (value==0)
    if not agrees: failures.append('determinant_agreement_'+str(i))
    if not expected: failures.append('old_block_classification_'+str(i))
    rows.append({'index':i,'base':B,'complete_determinant':value,
                 'saved_agrees':agrees,'determinant_sign':(value>0)-(value<0),
                 'classification':'nonsingular' if value else 'singular'})
out=root/'two-mixed-row-critical-block-classification.json'
report={'input_hashes':{str(source.relative_to(root.parent.parent)):hashlib.sha256(source.read_bytes()).hexdigest(),str(Path(__file__).relative_to(root.parent.parent)):hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
        'rows':rows,'checks':4,'failures':failures,
        'qualification':'Both enlarged blocks pass; only old block31 is singular. No new witness or omitted-mode evaluation.'}
out.write_text(json.dumps(enc(report),indent=2)+'\n')
print('Complete old determinants: row23 > 0 (nonsingular); row31 = 0 (singular).')
print('Checks: 4; failures:',failures,'; full certificate:',out.relative_to(root.parent.parent))
if failures: raise SystemExit(1)
