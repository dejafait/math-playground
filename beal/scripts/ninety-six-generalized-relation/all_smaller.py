"""Exact exhaustive subgroup coverage and all rational orbital maps.

The C backend is an unfiltered one-element-extension enumeration, not a
classification shortcut. This driver preserves its full evidence and checks
every completed class, normalizer, extension, and all qualifying orbital maps.
The prior audited field-to-group interface remains L055, not a program claim.
"""
from array import array
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json
import platform
import subprocess
import sys

folder = Path(__file__).resolve().parent
prefix = folder / 'all-smaller'
saved = json.loads((folder / 'coverage-certificate.json').read_text())
pg = saved['projective_group']['all_normalized_matrices_and_permutations']
s3 = saved['joint_group']['S3_permutations']
pairs = saved['joint_group']['all_index_pairs']
perms = [tuple(pg[i]['permutation'] + [12+x for x in s3[j]]) for i,j in pairs]
lookup = {p:i for i,p in enumerate(perms)}
assert len(perms) == len(lookup) == 3960
identity = lookup[tuple(range(15))]
def action(m):
    a,b,c,d=m
    return tuple(11 if den == 0 else num*pow(den,-1,11)%11
                 for num,den in [((a*x+b)%11,(c*x+d)%11) for x in range(11)]+[(a,c)])
gens = [lookup[action(m)+tuple(12+x for x in s)] for m,s in
        [((1,1,0,1),(0,1,2)),((1,0,1,1),(0,1,2)),
         ((2,0,0,1),(1,0,2)),((1,0,0,1),(1,2,0))]]
target = [tuple(3*p[a]+p[12+b]-12 for a,b in product(range(12),range(3))) for p in perms]
input_path = folder/'all-smaller-group.txt'
input_path.write_text(f'3960 {identity}\n'+ ' '.join(map(str,gens))+'\n'+
                      '\n'.join(' '.join(map(str,p)) for p in perms)+'\n')
binary = folder/'all_subgroups'
if '--process-only' not in sys.argv:
    subprocess.run(['clang','-O2','-std=c11','-Wall','-Wextra',str(folder/'all_subgroups.c'),'-o',str(binary)],check=True)
    run = subprocess.run([str(binary),str(input_path),str(prefix)])
    if run.returncode not in (0,3):
        raise SystemExit(f'Backend failure {run.returncode}; preserved partial evidence at {prefix}')
summary = json.loads(Path(str(prefix)+'-summary.json').read_text())
classes = [json.loads(line) for line in Path(str(prefix)+'-classes.jsonl').read_text().splitlines()]
table = array('H')
with Path(str(prefix)+'-multiplication.bin').open('rb') as f:
    table.fromfile(f,3960*3960)
assert table.itemsize == 2
def mul(a,b): return table[a*3960+b]
inverses = [next(b for b in range(3960) if mul(a,b)==identity) for a in range(3960)]
failures=[]
checks=[]
def check(label,condition):
    checks.append(label)
    if not condition: failures.append(label)
def closure(gs):
    seen={identity};queue=[identity]
    for x in queue:
        for g in gs:
            y=mul(x,g)
            if y not in seen:seen.add(y);queue.append(y)
    return seen
check('exact full group generator closure',len(closure(gens))==3960)
check('backend identity matches audited action',summary['identity']==identity)
check('all rows reported',len(classes)==summary['processed_classes'])
check('target stabilizer order',sum(p[0]==0 for p in target)==110)
check('all target points reached',len({p[0] for p in target})==36)
class_sets=[set(c['elements']) for c in classes]
for k,c in enumerate(classes):
    subgroup=class_sets[k]
    check(f'class {k}: exact generated subgroup',c['class']==k and closure(c['generators'])==subgroup and len(subgroup)==c['order'])
    normalizer={g for g in range(3960) if all(mul(mul(g,x),inverses[g]) in subgroup for x in c['generators'])}
    check(f'class {k}: complete normalizer',normalizer==set(c['normalizer_elements'])==closure(c['normalizer_generators']))
    orbit_ids=c['element_orbit_ids']; exts=c['extensions']
    check(f'class {k}: orbit domain',len(orbit_ids)==3960 and set(orbit_ids)==set(range(len(exts))))
    # Reconstruct full reducing orbits; equality verifies all 3960 elements.
    unseen=set(range(3960))
    for i,ext in enumerate(exts):
        g=ext['element'];seen={g};q=[g]
        for x in q:
            images=[mul(a,x) for a in c['generators']]+[mul(x,a) for a in c['generators']]
            images += [mul(mul(a,x),inverses[a]) for a in c['normalizer_generators']]
            for y in images:
                if y not in seen:seen.add(y);q.append(y)
        check(f'class {k} orbit {i}: complete reduction orbit',seen=={x for x,v in enumerate(orbit_ids) if v==i} and seen<=unseen)
        unseen-=seen
        if ext['class'] < len(classes):
            w=ext['conjugator']
            rhs={mul(mul(w,x),inverses[w]) for x in class_sets[ext['class']]}
            check(f'class {k} orbit {i}: exact extension and fusion witness',closure(c['generators']+[g])==rhs)
        elif summary['complete']:
            check(f'class {k} orbit {i}: missing class',False)
    check(f'class {k}: no unprocessed elements',not unseen)
    if k%10==0: print(f'Checked full subgroup/normalizer/extension evidence: {k+1}/{len(classes)}',flush=True)

# Check every conjugate witness, and that every saved class's conjugacy orbit
# is exhausted under the actual G generators. This also certifies distinctness.
conjugates=[json.loads(line) for line in Path(str(prefix)+'-conjugates.jsonl').read_text().splitlines()]
all_sets={frozenset(c['elements']):(c['class'],c['conjugator']) for c in conjugates}
check('all actual subgroup entries distinct',len(all_sets)==len(conjugates)==summary['actual_subgroups'])
for c in conjugates:
    k=c['class'];w=c['conjugator'];s=frozenset(c['elements'])
    if k>=len(classes):continue
    check(f'conjugate {k}/{w}: full witness',s==frozenset(mul(mul(w,x),inverses[w]) for x in class_sets[k]))
    for g in gens:
        z=frozenset(mul(mul(g,x),inverses[g]) for x in s)
        check(f'conjugate {k}/{w}: generator {g} closure',z in all_sets and all_sets[z][0]==k)

qualifying=[]
columns=[]
if summary['complete']:
    for c in classes:
        degree=3960//c['order']
        if degree>=36:continue
        jset=set(c['elements']);unseen=set(range(3960));cosets=[];coset_reps=[]
        while unseen:
            g=min(unseen);coset={mul(g,j) for j in jset}
            check(f'class {c["class"]}: coset partition',coset<=unseen)
            cosets.append(sorted(coset));coset_reps.append(g);unseen-=coset
        check(f'class {c["class"]}: exact degree',len(cosets)==degree)
        unseen=set(range(36));orbits=[];maps=[]
        while unseen:
            x=min(unseen);orbit={x};q=[x]
            for x0 in q:
                for g in c['generators']:
                    y=target[g][x0]
                    if y not in orbit:orbit.add(y);q.append(y)
            unseen-=orbit;orbits.append(sorted(orbit))
            cols=[sorted(target[g][x] for x in orbit) for g in coset_reps]
            matrix=[[int(x in col) for col in cols] for x in range(36)]
            maps.append(matrix)
            columns.extend([[matrix[x][i] for x in range(36)] for i in range(degree)])
        qualifying.append({'class':c['class'],'degree':degree,'generators':c['generators'],
                           'cosets':cosets,'coset_representatives':coset_reps,
                           'target_subgroup_orbits':orbits,'all_orbital_map_matrices':maps})
    # Complete exact row reduction, not a floating-point or selected-minor rank.
    mat=[[Fraction(v[x]) for v in columns] for x in range(36)]
    pivots=[];r=0
    for col in range(len(columns)):
        i=next((i for i in range(r,36) if mat[i][col]),None)
        if i is None:continue
        mat[r],mat[i]=mat[i],mat[r];p=mat[r][col];mat[r]=[v/p for v in mat[r]]
        for i in range(36):
            if i!=r and mat[i][col]:
                q=mat[i][col];mat[i]=[a-q*b for a,b in zip(mat[i],mat[r])]
        pivots.append(col);r+=1
        if r==36:break
    rref=[[str(x) for x in row] for row in mat]
else:
    r=None;pivots=[];rref=[]
coordinate_checks = None
if summary['complete']:
    # Independent elementary upper bound for every complete map column.
    coordinate_checks = all(v[3*a+b]-v[3*a]-v[b]+v[0]==0
                            for v in columns for a in range(12) for b in range(3))
    check('every complete map column is f(a)+g(b)',coordinate_checks)
    check('exact rational rank matches coordinate upper bound',r==14)
compiler=subprocess.run(['clang','--version'],capture_output=True,text=True,check=True).stdout.splitlines()[0]
artifact_paths=[Path(str(prefix)+suffix) for suffix in ['-classes.jsonl','-conjugates.jsonl','-multiplication.bin']]
cert={'target':'All subfields of MN of degree less than 36; all rational maps to Q[G/H]',
      'backend':{'method':'unfiltered one-element extension and full conjugacy orbit fusion',
                 'compiler':compiler,'python':platform.python_version(),'byteorder':sys.byteorder,
                 'sources':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [folder/'all_subgroups.c',Path(__file__)]}},
      'field_inputs':['L051','L055'], 'group':{'order':3960,'identity':identity,'generators':gens,
                 'all_disjoint_permutations':perms,'all_target_permutations':target,
                 'target_stabilizer_elements':[g for g,p in enumerate(target) if p[0]==0]},
      'enumeration':summary,'subgroup_classes':classes,
      'complete_conjugate_and_table_artifacts':{str(p.relative_to(folder)):hashlib.sha256(p.read_bytes()).hexdigest() for p in artifact_paths},
      'qualifying_subgroups':qualifying,
      'coverage':{'actual_rank':r,'required_rank':36,'total_map_columns':len(columns),
                  'pivot_columns':pivots,'exact_rref':rref,'complete':summary['complete'],
                  'all_columns_have_zero_mixed_coordinate_differences':coordinate_checks},
      'checks':checks,'failures':failures}
path=folder/'all-smaller-certificate.json'
path.write_text(json.dumps(cert,indent=2)+'\n')
print(f'Exhaustive coverage: {summary["complete"]}; qualifying classes: {len(qualifying)}')
print(f'Complete rational rank: actual {r}, required 36; failures {len(failures)}')
print(f'Full certificate: {path.relative_to(Path.cwd())}')
if failures:raise SystemExit(1)
if not summary['complete']:raise SystemExit(3)
