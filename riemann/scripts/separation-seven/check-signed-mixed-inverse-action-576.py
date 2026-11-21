#!/usr/bin/env python3
"""Inspect all576 saved evidence; not an independent matrix-entry replay."""
import hashlib
import json
from pathlib import Path
import numpy as np

BASE=Path(__file__).resolve().parent
ns={'__file__':str(BASE/'signed-mixed-direct-action-575.py'),'__name__':'checkhelpers576'}
exec(compile((BASE/'signed-mixed-direct-action-575.py').read_text().split(
    '# Reuse complete proved enclosures;')[0],str(BASE/'signed-mixed-direct-action-575.py'),'exec'),ns)
I,fro_upper=ns['I'],ns['fro_upper']
record=json.loads((BASE/'signed-mixed-inverse-action-576.json').read_text())
checks,failures=[],[]

def check(ok,label):
    checks.append(dict(label=label,passed=bool(ok)))
    if not ok:failures.append(label)

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for b in iter(lambda:stream.read(8*1024*1024),b''):h.update(b)
    return h.hexdigest()

def interval(data):
    return I(data['lo'],data['hi'])

K,N,E,BLOCK=65536,512,1020,128
u=I(1)/2**53
gamma=lambda n:n*u/(1-n*u)
check(sha(BASE/'signed-mixed-inverse-action-576.py')==record['source_sha256'],'production source hash')
for name,digest in record['input_hashes'].items():check(sha(BASE/name)==digest,'full input hash '+name)
for name,data in record['archives'].items():check(sha(BASE/name)==data['sha256'],'full output hash '+name)
check(not record['failures'] and all(c['passed'] for c in record['checks']),'all production flags')
s={name:interval(data) for name,data in record['scalars'].items()}
action=np.load(BASE/'signed-mixed-inverse-action-center-576.npy',mmap_mode='r')
differences=np.load(BASE/'signed-mixed-inverse-action-difference-576.npy',mmap_mode='r')
v=np.load(BASE/'signed-mixed-inverse-output-565.npy',mmap_mode='r')
dhat=np.load(BASE/'signed-mixed-direct-center-575.npy',mmap_mode='r')
what=np.load(BASE/'signed-mixed-columns-565.npy',mmap_mode='r')
with np.load(BASE/'signed-mixed-finite-center-572.npz') as data:
    ratios=data['neutral_ratio_center'];weights=data['upward_inverse_sqrt_weight']
check(action.shape==differences.shape==dhat.shape==what.shape==(2,K,E),'all pair dimensions')
check(I(fro_upper(v)).json()==s['inverse_center_fro'].json(),'complete inverse norm')
esq,csq=I(0),I(0)
for number,b in enumerate(record['matrix_blocks']):
    first,last=b['first'],b['last']
    check(first==number*BLOCK and last==first+BLOCK-1 and b['entry_count']==BLOCK*K,
          'complete matrix rectangle '+str(first))
    esq+=I(b['radius_fro'])*I(b['radius_fro'])
    csq+=I(b['center_fro'])*I(b['center_fro'])
check(len(record['matrix_blocks'])==K//BLOCK,'all K-square matrix blocks')
check(esq.sqrt().json()==s['finite_translation_radius'].json()
      and csq.sqrt().json()==s['finite_translation_center_fro'].json(),'full matrix norm ledgers')
fv=s['inverse_center_fro'];fc=csq.sqrt()
entry=esq.sqrt()*fv
product=gamma(2*K+32)*(fc*fv+1)
ce,cm=I(0),I(0)
for j,t in enumerate(record['continuous_terms'],1):
    fa,fb,ea,eb=[interval(t[n]) for n in
        ['a_center_fro','b_center_fro','a_radius_fro','b_radius_fro']]
    et=ea*(fb+eb)+fa*eb
    ar=gamma(2*K+32)*(fa*fb*fv+1)
    q=et*fv+ar
    check(t['j']==j and et.json()==t['operator_entry_error']
          and ar.json()==t['product_rounding'] and q.json()==t['one_orientation_error'],
          'full continuous ledger '+str(j))
    ce+=q;cm+=fa*fb
addition=gamma(32)*((fc+cm)*fv+1)
tail=1/(I(3**49)*I(3).sqrt()*I('16.5')*(1-I(1)/3**6))
pair=I(2).sqrt()*(entry+product+ce+addition+tail*fv)
check(len(record['continuous_terms'])==7 and entry.json()==s['one_action_entry_error'].json()
      and product.json()==s['one_action_product_rounding'].json()
      and ce.json()==s['one_action_continuous_error'].json()
      and addition.json()==s['one_action_continuous_addition'].json()
      and tail.json()==s['continuous_tail_operator'].json()
      and pair.json()==s['pair_action_error'].json(),'complete action error ledger')
low=[];lowerrors=[]
for side in range(2):
    aa=np.array(action[side,:2]);dd=np.array(dhat[side,:2]);ww=np.array(what[side,:2])
    delta=aa-(dd-ww);low.append(delta)
    lowerrors.append(gamma(8)*(I(fro_upper(aa))+I(fro_upper(dd))+I(fro_upper(ww))+1))
    check(np.array_equal(delta,differences[side,:2]),'complete low difference '+str(side))
wsq,ssq,qsq=I(0),I(0),I(0)
for number,b in enumerate(record['difference_blocks']):
    side,first,last=b['side'],b['first'],b['last']
    check(first==N+(number//2)*BLOCK and side==number%2 and last==first+BLOCK-1,
          'full difference rectangle '+str(number))
    rows=slice(first,last+1);pos=slice(first-N,last+1-N)
    aa=np.array(action[side,rows]);dd=np.array(dhat[side,rows]);ww=np.array(what[side,rows])
    delta=aa-(dd-ww)
    repeat=low[side][np.arange(first,last+1)%2]
    weighted=(delta-ratios[pos,None]*repeat)*weights[pos,None]
    fw,fd,fl=I(fro_upper(weighted)),I(fro_upper(delta)),I(fro_upper(repeat))
    sub=gamma(8)*(I(fro_upper(aa))+I(fro_upper(dd))+I(fro_upper(ww))+1)
    coord=I('.5')*(I('1e-20')*fl+gamma(16)*(fd+I('1e-5')*fl+1))
    check(np.array_equal(delta,differences[side,rows])
          and hashlib.sha256(delta.tobytes()).hexdigest()==b['difference_sha256']
          and np.all(np.isfinite(weighted)),'every saved difference row '+str(number))
    check(fw.json()==b['weighted_center_fro'] and fd.json()==b['difference_fro']
          and fl.json()==b['repeated_low_fro'] and sub.json()==b['subtraction_error']
          and coord.json()==b['coordinate_error'],'entire difference error ledger '+str(number))
    wsq+=fw*fw;ssq+=sub*sub;qsq+=coord*coord
check(len(record['difference_blocks'])==2*(K-N)//BLOCK,'both full difference ranges')
alpha=(4/(3*I('6.14')*511**3)).sqrt()
zeta=(1/I('6.14')+4/(3*I('6.14')*511**3)).sqrt()
subtraction=I('.5')*ssq.sqrt()+alpha*(lowerrors[0]*lowerrors[0]+lowerrors[1]*lowerrors[1]).sqrt()
eta=(wsq.sqrt()+subtraction+qsq.sqrt()+zeta*pair)/I('.000999').sqrt()
check(wsq.sqrt().json()==s['weighted_difference_center_fro'].json()
      and subtraction.json()==s['weighted_subtraction_error'].json()
      and qsq.sqrt().json()==s['weighted_coordinate_error'].json()
      and eta.json()==s['normalized_inverse_action_error'].json(),'complete normalized comparison ledger')
check(eta.hi<=ns['Decimal']('.002645'),'required inverse-action threshold')
eta_total=I('.001556')+I('.000002')+I('.000001')+eta
finite=(I('.083').sqrt()+eta_total)*(I('.083').sqrt()+eta_total)
whole=(finite+I('.151')*I('.151')).sqrt()+I('.163')+I('.008')
check(finite.hi<ns['Decimal']('.085440') and whole.hi<ns['Decimal']('.5'),
      'fixed finite and full mixed thresholds from C999m(46)/(51)')
out=dict(scope='complete evidence inspection, not independent entry replay or conceptual audit',
    source_sha256=sha(Path(__file__)),production_sha256=sha(BASE/'signed-mixed-inverse-action-576.json'),
    checks=checks,failures=failures,normalized_action_error=eta.json(),
    combined_finite_error=eta_total.json(),finite_covariance_upper=finite.json(),
    full_mixed_norm_upper=whole.json(),full_mixed_covariance_upper=(whole*whole).json())
path=BASE/'signed-mixed-inverse-action-check-576.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print('Complete evidence checks:',len(checks),'failures:',failures)
print('Normalized action error upper:',eta.hi,'required <=.002645')
print('Finite covariance upper:',finite.hi,'required <=.085440')
print('Full mixed norm upper:',whole.hi,'required <=.5; independent audits still open')
print('Evidence:',path.relative_to(BASE.parent.parent))
