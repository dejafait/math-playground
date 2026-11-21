#!/usr/bin/env python3
"""Exact acceptance inspection of every saved step140 margin and error record.
Not a second implementation of the transcendental/quadrature evaluator.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

base=Path(__file__).parent
path=base/'rational-replay-140.json'
v=json.loads(path.read_text())
Q=1<<256
fail=[]
def require(ok,msg):
    if not ok: fail.append(msg)
def bounds(x):
    require(x['denominator_power_two']==256,'unexpected precision')
    l,h=int(x['lo']),int(x['hi'])
    require(l<=h,'reversed enclosure')
    return l,h

def evidence(e,label):
    if 'exact' in e: require(e['exact'] is True,label)
    else: require(bounds(e['positive_margin'])[0]>0,label)

require(v['status']=='PASS','status')
require(len(v['leaves'])==151,'leaf count')
require(len(v['gates'])==914 and all(x is True for x in v['gates'].values()),'all original gate flags')
require(all(v['self_checks'].values()),'arithmetic self checks')
require(all(v['exact_cover_checks'].values()),'exact cover checks')
ends=[690988]
while ends[-1]<3100000: ends.append(min(3100000,101*ends[-1]//100))
require(v['closed_index_endpoints']==ends,'full exact endpoint recurrence')
for name,e in v['global_evidence'].items(): evidence(e,name)
records=[]
for i,leaf in enumerate(v['leaves'],1):
    require((leaf['index'],leaf['left'],leaf['right'])==(i,ends[i-1],ends[i]),f'leaf {i} cover')
    for name,e in leaf['gate_evidence'].items(): evidence(e,f'leaf {i} {name}')
    for name in ['x_left','c_left','sigma','B','logU','g_low','g_high','prefix','I','tail','bound']: bounds(leaf[name])
    pl,ph=bounds(leaf['prefix']);tl,th=bounds(leaf['tail']);bl,bh=bounds(leaf['bound'])
    require((bl,bh)==(pl+tl,ph+th),f'leaf {i} prefix+tail')
    require(4*bh<81*Q,f'leaf {i} cap')
    require(bounds(leaf['I'])[0]>0 and tl>0,f'leaf {i} two positive integrals')
    qe=leaf['quadrature']
    require(qe['mesh']==4096,f'leaf {i} even mesh')
    for name in ['width','h','r_abs_upper','u_minus_kappa_abs_upper','exp_upper','I_fourth_derivative_bound','tail_fourth_derivative_bound','I_error','tail_error']:
        l,h=bounds(qe[name]);require(l>=0 and h>=0,f'leaf {i} nonnegative {name}')
    for what,final in [('I',leaf['I']),('tail',leaf['tail'])]:
        sl,sh=bounds(qe[what+'_simpson']);el,eh=bounds(qe[what+'_error'])
        require(bounds(final)==(sl-eh,sh+eh),f'leaf {i} charged {what} error')
    rl,rh=bounds(qe['last_E_recurrence']);dl,dh=bounds(qe['last_E_direct'])
    require(max(rl,dl)<=min(rh,dh),f'leaf {i} exponential recurrence endpoint')
    records.append({'leaf':i,'bound_upper_numerator':str(bh),'cap_margin_numerator':str(81*Q-4*bh),
        'I_error_upper_numerator':qe['I_error']['hi'],'tail_error_upper_numerator':qe['tail_error']['hi']})
maximum=max(int(r['bound_upper_numerator']) for r in records)
max_leaf=next(r['leaf'] for r in records if int(r['bound_upper_numerator'])==maximum)
require(v['maximum_upper_endpoint']=={'numerator':str(maximum),'denominator_power_two':256},'maximum of all151 endpoints')
simple_upper=maximum*1000000//Q+1
report={'status':'PASS' if not fail else 'FAIL','certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'script_sha256':hashlib.sha256((base/'rational_replay_140.py').read_bytes()).hexdigest(),
        'checked_original_gates':914,'checked_leaf_records':151,'failures':fail,
        'maximum_leaf':max_leaf,'maximum_upper_numerator':str(maximum),'denominator_power_two':256,
        'simple_rational_upper_bound':str(simple_upper)+'/1000000',
        'max_tail_error_upper_numerator':str(max(int(r['tail_error_upper_numerator']) for r in records)),
        'records':records,
        'qualification':'Inspects every stored exact margin/error/bound; not an independent analytic or code audit.'}
out=base/'rational-inspection-140.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(report['status'],'checked all151 leaves/all914 margins; maximum leaf',max_leaf)
print('Exact maximum:',maximum,'/2^256; required <81/4; display ceiling:',str(simple_upper)+'/1000000')
print('Failures:',fail,'certificate:',out)
raise SystemExit(bool(fail))
