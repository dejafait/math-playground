"""Critical-audit orchestration and complete table bridge checks for L079."""
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOTEBOOK = ROOT.parent.parent
ARTIFACTS = [
    'affine-plane-certificate.json', 'affine-plane-quadrilaterals.json',
    'affine-plane-ratio-minors.json', 'affine-plane-affine-rank.json',
    'affine-plane-affine-rank-rows.csv', 'affine-plane-affine-rank-rank-drops.jsonl',
    'affine-plane-affine-rank-replay.csv', 'affine-plane-affine-rank-replay.json',
    'affine-plane-full-ratio.json', 'affine-plane-full-ratio-rows.csv',
    'affine-plane-full-ratio-passing.jsonl', 'affine-plane-full-ratio-incidence.json',
    'affine-plane-full-ratio-replay.json',
]
def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()

cert = {'scope': 'Complete direct L079 audit replay and equation-table bridges',
        'before_sha256': {n: digest(ROOT/n) for n in ARTIFACTS},
        'runs': [], 'failures': []}
output = ROOT/'affine-plane-critical-audit.json'
def save():
    output.write_text(json.dumps(cert, indent=2)+'\n')
save()
def run(args):
    result = subprocess.run(args, cwd=NOTEBOOK, text=True, capture_output=True)
    cert['runs'].append({'command': args, 'exit_code': result.returncode,
                         'stdout': result.stdout, 'stderr': result.stderr})
    if result.returncode:
        cert['failures'].append('command failed: '+str(args))
    save()
    print(f"{'PASS' if result.returncode == 0 else 'FAIL'}: {' '.join(args)}", flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)

for stem in ['verify_affine_plane', 'affine_plane_quadrilaterals', 'affine_plane_ratio_elimination']:
    run(['python3', f'scripts/triangle-incidence/{stem}.py'])
for stem, binary, arguments in [
    ('affine_plane_affine_rank', '/tmp/mca-affine-rank', ['scripts/triangle-incidence/affine-plane-affine-rank']),
    ('verify_affine_plane_affine_rank', '/tmp/mca-affine-rank-verify', ['scripts/triangle-incidence/affine-plane-affine-rank']),
    ('affine_plane_full_ratio', '/tmp/mca-full-ratio', ['scripts/triangle-incidence/affine-plane-affine-rank-rows.csv', 'scripts/triangle-incidence/affine-plane-full-ratio']),
]:
    run(['c++', '-std=c++17', '-O2', f'scripts/triangle-incidence/{stem}.cpp', '-o', binary])
    run([binary]+arguments)
run(['python3', 'scripts/triangle-incidence/verify_affine_plane_full_ratio.py'])

# Bridge the shared original twelve-equation table to actual incidence,
# for every possible value of each permuted label cross-ratio.
inc = json.loads((ROOT/'affine-plane-full-ratio-incidence.json').read_text())['quadruples']
def inv(x): return pow(x % 97, -1, 97)
def det(p, q): return (p[0]*q[1]-p[1]*q[0]) % 97
def ratio(q, r):
    pts = [(0,1),(1,0),(1,1),(1,r)]
    a,b,c,d = [pts[i] for i in q['permutation']]
    return det(a,c)*det(b,d)*inv(det(a,d)*det(b,c)) % 97
spec = [(0,1,3,0,0),(0,2,1,1,0),(0,3,2,2,0),
        (1,0,2,1,1),(1,2,3,3,0),(1,3,0,0,2),
        (2,0,3,2,1),(2,1,0,1,2),(2,3,1,3,2),
        (3,0,1,0,1),(3,1,2,3,1),(3,2,0,2,2)]
checks = []
for j,k,l,g,form in spec:
    matches = [q for q in inc if q['blocks'] == [0,4+j,8+k,12+l]]
    ok = len(matches)==1 and matches[0]['ratio_group']==g
    residues = []
    if ok:
        q = matches[0]
        for r in range(2,97):
            expected = [r, inv(1-r), (r-1)*inv(r)%97][form]
            residues.append((ratio(q,r)-expected)%97)
        ok = not any(residues)
    checks.append({'blocks':[0,4+j,8+k,12+l], 'group':g, 'form':form,
                   'all_95_differences':residues, 'pass':ok})
    if not ok: cert['failures'].append('V0 table bridge')
vertical = []
for v,g in [(1,2),(2,0),(3,1)]:
    q = next(q for q in inc if q['blocks']==[v,4,8,12+v])
    residues = [(ratio(q,r)-(r-1)*inv(r))%97 for r in range(2,97)]
    ok = q['ratio_group']==g and not any(residues)
    vertical.append({'vertical':v,'group':g,'all_95_differences':residues,'pass':ok})
    if not ok: cert['failures'].append('vertical table bridge')
counts = Counter(q['ratio_group'] for q in inc)
if dict(counts)!={0:12,1:12,2:12,3:12}: cert['failures'].append('group counts')
cert['V0_table_bridge']=checks
cert['vertical_table_bridge']=vertical
cert['group_counts']=dict(counts)
cert['after_sha256']={n:digest(ROOT/n) for n in ARTIFACTS}
cert['changed_artifacts']=[n for n in ARTIFACTS if cert['before_sha256'][n]!=cert['after_sha256'][n]]
if cert['changed_artifacts']: cert['failures'].append('artifact content changed: inspect before acceptance')
cert['actual']={'artifact_replays':len(ARTIFACTS),'V0_bridge_values':sum(len(c['all_95_differences']) for c in checks),
                'vertical_bridge_values':sum(len(c['all_95_differences']) for c in vertical),
                'unchanged_artifacts':len(ARTIFACTS)-len(cert['changed_artifacts']), 'failures':len(cert['failures'])}
cert['required']={'artifact_replays':13,'V0_bridge_values':1140,'vertical_bridge_values':285,'unchanged_artifacts':13,'failures':0}
save()
print('Actual:',cert['actual'],'Required:',cert['required'],'Certificate:',output)
raise SystemExit(bool(cert['failures']))
