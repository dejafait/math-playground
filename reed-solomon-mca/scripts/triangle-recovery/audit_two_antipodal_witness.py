"""Audit L068's displayed witness directly; replay its bounded certificate.

No arithmetic utility or producer formula is imported. Same-support failure
is also checked by degree-seven Lagrange interpolation of the actual direction.
"""
from pathlib import Path
from itertools import combinations
from math import prod
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
MOD = 97
H = [1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96]
P = [64,75,33]
Y,Z,W = [1,96],[18,79],[8,50]
weights = [71,5,17]
base = [{1:52,96:57,64:72,75:33},
        {18:4,79:9,64:15,33:91}, {8:27,50:23,75:90,33:80}]
claimed = [([22,27,47,85],30,32,91,[34,55,84,93],[21,48]),
           ([22,27,47,89],50,52,56,[20,81,69,71],[13,68]),
           ([22,27,85,89],22,24,89,[72,26,96,29],[90,40]),
           ([22,47,85,89],34,36,27,[86,15,92,55],[56,61]),
           ([27,47,85,89],63,65,6,[35,6,75,20],[39,32])]
failures = []

def check(name, actual, required):
    if actual != required:
        failures.append({'test':name, 'actual':actual, 'required':required})

def moments(e):
    return [sum(w*pow(x,j,MOD) for x,w in e.items()) % MOD for j in range(1,9)]

def interpolate(nodes, values, x):
    return sum(v*prod((x-y)*pow(t-y,-1,MOD) % MOD for y in nodes if y!=t)
               for t,v in zip(nodes,values)) % MOD

certificate = ROOT/'two-antipodal-witness-verification.json'
before = certificate.read_bytes()
saved = json.loads(before)
check('H', [x for x in range(1,MOD) if pow(x,16,MOD)==1], H)
U = set(P+Y+Z+W)
check('distinct labels',len(U),9)
check('two antipodal pairs and nonantipodal W',
      [sum(t)%MOD==0 for t in (Y,Z,W)], [True,True,False])
check('base gates',all(x not in (0,1) for x in weights),True)
cx = {x:prod(x-h for h in H if h not in U)%MOD for x in U}
check('Q evaluations', {str(x):v for x,v in cx.items()}, saved['CX'])
p,q,r=weights
norms=[{1:1,96:1,64:p,75:q},{18:1,79:1,64:1-p,33:r},
       {8:1,50:1,75:1-q,33:1-r}]
check('L057 base construction',
      [{x:cx[x]*v*pow(a,-1,MOD)%MOD for x,v in n.items()}
       for a,n in zip([-1,2,-1],norms)],base)
check('base errors', [{str(x):v for x,v in e.items()} for e in base],saved['base_errors'])
bm=[moments(e) for e in base]
check('base moment values',bm,saved['base_moments'])
check('affine base relation',[(c-2*b+a)%MOD for a,b,c in zip(*bm)],[0]*8)
direction={x:(base[1].get(x,0)-base[0].get(x,0))%MOD for x in H}
rows=[]
for K,mu,E,T,ws,proj in claimed:
    tag=str(K)
    check(tag+' full support',all(ws) and len(K)==len(set(K))==4,True)
    check(tag+' disjoint P',set(K).isdisjoint(P),True)
    check(tag+' finite gates',mu not in (0,96) and E!=0 and T not in (0,1,2),True)
    check(tag+' E',(2+mu)%MOD,E)
    check(tag+' T',2*pow(E,-1,MOD)%MOD,T)
    actual=moments(dict(zip(K,ws)))
    expected=[(a+T*(b-a))%MOD for a,b in zip(*bm[:2])]
    check(tag+' original moments',actual,expected)
    projections=[sum(cx[x]*x*prod(x-k for k in K)*prod(x-t for t in P)
                     for x in pair)%MOD for pair in (Y,Z)]
    check(tag+' projection values',projections,proj)
    check(tag+' isolated',all(projections),True)
    check(tag+' projected equation',(projections[1]-mu*projections[0])%MOD,0)
    coeff={x:-mu*cx[x]%MOD for x in Y}
    coeff.update({x:cx[x] for x in Z})
    coeff.update({64:cx[64]*(1-(1+mu)*p)%MOD,75:-mu*cx[75]*q%MOD,33:cx[33]*r%MOD})
    numerator=moments(dict(zip(K,[E*w%MOD for w in ws])))
    check(tag+' numerator moments',numerator,moments(coeff))
    S=[x for x in H if x not in K]
    nodes=S[:8]
    direction_residuals=[(direction[x]-interpolate(nodes,[direction[t] for t in nodes],x))%MOD for x in S]
    check(tag+' same-support input failure',any(direction_residuals),True)
    word={x:(base[0].get(x,0)+T*direction[x]-dict(zip(K,ws)).get(x,0))%MOD for x in H}
    code_residuals=[(word[x]-interpolate(H[:8],[word[t] for t in H[:8]],x))%MOD for x in H]
    check(tag+' actual agreement codeword',code_residuals,[0]*16)
    row={'K':K,'mu':mu,'E':E,'T':T,'actual_weights':ws,'moments8':actual,
         'expected_moments8':expected,'projections':projections,'numerator_moments8':numerator,
         'same_support':S,'direction_interpolation_nodes':nodes,
         'direction_restriction_residuals12':direction_residuals,
         'agreement_codeword_residuals16':code_residuals}
    rows.append(row)
    old=next(v for v in saved['witness_rows'] if v['K']==K)
    for key,value in [('mu',mu),('E',E),('original_T',T),('actual_weights',ws),
                      ('projected_Y_Z',proj),('actual_moments8',actual)]:
        check(tag+' saved '+key,old[key],value)
check('distinct finite T',len({v['T'] for v in rows}),5)
check('distinct mu',len({v['mu'] for v in rows}),5)
check('715 support set',sorted(tuple(v['K']) for v in saved['complete_fixed_assignment_tests']),
      list(combinations([x for x in H if x not in P],4)))
check('saved failures',saved['failures'],[])
replay=subprocess.run([sys.executable,str(ROOT/'check_two_antipodal_witness.py')],
                      capture_output=True,text=True)
check('bounded replay return code',replay.returncode,0)
after=certificate.read_bytes()
check('complete certificate byte equality',after==before,True)
result={'scope':'L068 separate critical audit; no enlarged maximum',
        'H':H,'P':P,'Y':Y,'Z':Z,'W':W,'weights':weights,
        'CX':cx,'base_errors':base,'base_moments':bm,'witness_audits':rows,
        'actual_witnesses':len(rows),'required_witnesses':5,'refuted_upper_bound':3,
        'actual_replayed_supports':715 if replay.returncode==0 else None,'required_replayed_supports':715,
        'before_certificate_sha256':hashlib.sha256(before).hexdigest(),
        'after_certificate_sha256':hashlib.sha256(after).hexdigest(),
        'bounded_replay_stdout':replay.stdout,'bounded_replay_stderr':replay.stderr,
        'prefix_equation_replayed':False,'actual_failures':len(failures),
        'required_failures':0,'failures':failures}
out=ROOT/'two-antipodal-critical-audit.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(f'Explicit witnesses {len(rows)}/5; isolated count 5 > proposed bound 3; complete fixed-assignment replay 715/715')
print(f'Original moments, finite gates, same-support interpolation: failures {len(failures)}/0')
print(f'Complete evidence: {out}')
if failures:
    print(failures)
    raise SystemExit(1)
