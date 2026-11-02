#!/usr/bin/env python3
"""Read every recorded leaf and provenance hash; no new enclosure evaluations.

This checks record completeness/threshold comparisons, not the Taylor
coefficients, elementary arithmetic or mathematical correctness of the producer.
"""
from pathlib import Path
from hashlib import sha256
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
import json

HERE = Path(__file__).resolve().parent
BASE = HERE/'spatial-signed'
report = json.loads((BASE/'certificate.json').read_text())
checks, failures = [], []


def check(name, condition):
    checks.append(dict(name=name,passed=bool(condition)))
    if not condition:
        failures.append(name)


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def ordered(v):
    if isinstance(v,list):
        if len(v)==2 and all(isinstance(a,str) and a.lstrip('-').isdigit() for a in v):
            return int(v[0]) <= int(v[1])
        return all(ordered(a) for a in v)
    if isinstance(v,dict):
        return all(ordered(a) for a in v.values())
    return True


G=1 << report['precision_bits']
reserve=int(report['parameters']['reserve'][0])
check('producer unchanged',digest(HERE/'spatial-signed-enclosure.py')==report['script_sha256'])
for name,h in report['inputs'].items():
    check('input '+name,digest(HERE/name)==h)
check('exact operation cap',report['operations']==report['limits']['scalar_interval_ops']==1<<28)
check('evaluation cap respected',report['evaluations'] <= report['limits']['evaluations']==65536)
empty_cases=2 # Both the original and normalized initialization tested q=n.
check('full case cap including repeated empty cell',report['evaluations']+empty_cases <= 65536)
check('outcome inconclusive',report['result']=='INCONCLUSIVE' and report['stop']=='scalar interval operation cap')
check('no producer implementation failure',report['failures']==[])
check('canonical consecutive completed roots',
      [r['q'] for r in report['roots']]==list(range(691005,report['completed_through']+1)))
complete_leaf_count=all_leaf_count=0
costs=[]
depths=[]
for entry in report['roots']:
    path=BASE/entry['path']
    check('hash '+path.name,digest(path)==entry['sha256'])
    cell=json.loads(path.read_text())
    q=entry['q']
    check('ordered intervals '+str(q),ordered(cell))
    check('canonical left entry '+str(q),cell['q']==cell['canonical_left']==cell['right_comparison']==q)
    check('right closure comparison '+str(q),cell['canonical_right']==(q if q==691260 else q+1))
    attempt=cell['attempts'][-1]
    check('full final partition '+str(q),len(attempt['leaves'])==attempt['pieces']==1<<attempt['depth'])
    check('indices '+str(q),[r['index'] for r in attempt['leaves']]==list(range(attempt['pieces'])))
    check('depth cap '+str(q),all(a['depth']<=16 for a in cell['attempts']))
    check('all complete dimensions '+str(q),all(len(r['coefficients'])==4 and
         all(len(p)==17 for p in r['coefficients']) and len(r['ranges'])==4
         for a in cell['attempts'] for r in a['leaves']))
    check('strict final thresholds '+str(q),all(r['passed'] and int(r['total_cost'][1])<reserve
          for r in attempt['leaves']))
    recorded_max=max(int(r['total_cost'][1]) for r in attempt['leaves'])
    check('root max '+str(q),recorded_max==int(entry['max_cost'][1]))
    check('root evaluation count '+str(q),sum(len(a['leaves']) for a in cell['attempts'])==entry['evaluations'])
    complete_leaf_count+=len(attempt['leaves'])
    all_leaf_count+=entry['evaluations']
    costs.append(recorded_max)
    depths.append(attempt['depth'])

prior=report['prior_interrupted_run']
check('prior interrupted manifest hash',digest(BASE/prior['path'])==prior['sha256'])
check('prior producer hash',digest(BASE/prior['producer'])==prior['producer_sha256'])
partial_rows=[]
for name,h in [(prior['partial'],prior['partial_sha256']),
               (report['partial_cell']['path'],report['partial_cell']['sha256'])]:
    check('partial hash '+name,digest(BASE/name)==h)
    cell=json.loads((BASE/name).read_text())
    check('partial ordered intervals '+name,ordered(cell))
    leaves=sum(len(a['leaves']) for a in cell['attempts'])
    all_leaf_count+=leaves
    partial_rows.append(dict(path=name,q=cell['q'],recorded_leaves=leaves,
                             depths=[a['depth'] for a in cell['attempts']]))
check('incomplete interrupted and capped evaluations counted',report['evaluations']-all_leaf_count==2)
check('final maximum matches every complete cell',max(costs)==int(report['maximum_completed_cost'][1]))


def decimal(v,upper=True):
    with localcontext() as ctx:
        ctx.prec=26
        ctx.rounding=ROUND_CEILING if upper else ROUND_FLOOR
        return str(Decimal(v)/Decimal(G))


out=dict(result='PASS' if not failures else 'FAIL',
         scope='Complete recorded leaf dimensions, ordering, provenance, threshold and counter checks only; no independent enclosure audit',
         mathematical_enclosure_evaluations=0,scalar_interval_arithmetic_operations=0,
         manifest_sha256=digest(BASE/'certificate.json'),
         completed_roots=len(report['roots']),completed_through=report['completed_through'],
         complete_final_leaves=complete_leaf_count,all_recorded_leaves=all_leaf_count,
         evaluations=report['evaluations'],uncompleted_evaluations=report['evaluations']-all_leaf_count,
         empty_initial_case_evaluations=empty_cases,total_case_evaluations=report['evaluations']+empty_cases,
         operations=report['operations'],partial_records=partial_rows,
         maximum_recorded_cost_upper=decimal(max(costs)),reserve_lower=decimal(reserve,False),
         max_complete_depth=max(depths),charges={k:decimal(int(report['charges'][k][1]))
                    for k in ('saddle','remainder')},checks=checks,failures=failures)
(BASE/'ledger-check.json').write_text(json.dumps(out,indent=2)+'\n')
print(f"{out['result']}: {len(checks)} record checks; failures={failures}")
for k in ('completed_roots','completed_through','complete_final_leaves','evaluations','total_case_evaluations','operations',
          'maximum_recorded_cost_upper','reserve_lower','charges','partial_records'):
    print(str(k)+'='+str(out[k]))
print('certificate=scripts/heat/spatial-signed/ledger-check.json')
raise SystemExit(bool(failures))
