#!/usr/bin/env python3
"""Independent full scalar-transcript evaluation and exact accuracy-trace match.

Verification only. This does not rerun/tune the numerical prescription.
"""
from array import array
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import gzip
import json

HERE=Path(__file__).resolve()
SOURCE=HERE.with_name('scalar-register-gauss-694.json')
TRACE=HERE.with_name('scalar-register-gauss-694.trace.jsonl.gz')
OLD=HERE.with_name('certified-gauss-adaptive-692.json')
OLDREPLAY=HERE.with_name('certified-gauss-adaptive-replay-692.json')
OUT=HERE.with_suffix('.json')
counts=Counter();failures=[]

def ck(b,name):
    counts[name]+=1
    if not b:
        failures.append(name)
        raise AssertionError(name)

def zi(q): return int(q['odd_hex'],16)<<q['shift']
def rf(q): return F(zi(q['num']),zi(q['den']))
def inter(q): return tuple(map(rf,q))
def uses(e):
    if e[0] in ('+','-','*','/'): return e[2:4]
    if e[0]=='copy': return e[2:3]
    if e[0]=='compare': return e[2:4]
    if e[0]=='output': return e[3:7]
    return ()

report={'result':'INCOMPLETE','failures':failures}
try:
    data=json.loads(SOURCE.read_text())
    old=json.loads(OLD.read_text())
    oldcheck=json.loads(OLDREPLAY.read_text())
    ck(data['failures']==[] and data['result']=='PASS_REGISTER_PROGRAM_AND_ALL_ACCURACY_GUARDS','constructor completed')
    ck(data['rows']==old['rows'],'entire exact mathematical trace equals692')
    ck(data['summary']['maximum_node_radius']==old['summary']['maximum_node_radius'],'complete maximum node radius matches')
    ck(data['summary']['maximum_weight_radius']==old['summary']['maximum_weight_radius'],'complete maximum weight radius matches')
    ck(oldcheck['failures']==[],'independent unscaled692 replay passed')
    # Check saved verifier's source binding rather than only its pass label.
    ck(oldcheck['source_certificate_sha256']==sha256(OLD.read_bytes()).hexdigest(),'unscaled692 replay source hash')
    expected=[]
    for row in data['rows']:
        n=row['degree']
        ck(row['total_nodes']==n,'each degree complete')
        for root in row['positive_roots']:
            f=root['final']
            expected.append(('positive',n,inter(f['node'])+inter(f['weight'])))
            expected.append(('negative',n,inter(root['negative_node'])+inter(root['negative_weight'])))
        expected.append(('zero',n,inter(row['zero_node']['node'])+inter(row['zero_node']['weight'])))
    ck(len(expected)==261,'all261 expected outputs')
    # Whole-program liveness prepass lets the full rational replay discard
    # huge recurrence registers immediately after their last numeric use.
    remaining=array('I',[0])*data['scalar_work']['register_count']
    lines=0
    with gzip.open(TRACE,'rt') as stream:
        for line in stream:
            e=json.loads(line); lines+=1
            for i in uses(e): remaining[i]+=1
    registers={}; allocated=0; cost=0; by=Counter(); category='constants'; outputs=0
    ins=Counter();peak=0
    with gzip.open(TRACE,'rt') as stream:
        for line in stream:
            e=json.loads(line);op=e[0];ins[op]+=1
            if op=='mark': category=e[1];continue
            operands=uses(e)
            for i in operands: ck(i in registers,'every operand defined and live')
            if op=='literal':
                ck(e[2] in set(range(-1,129))|{550,560,640,16384},'only approved small literal')
                result=F(e[2]); charge=1
            elif op=='copy': result=registers[e[2]];charge=1
            elif op in ('+','-','*','/'):
                a,b=registers[e[2]],registers[e[3]]
                if op=='+':result=a+b
                elif op=='-':result=a-b
                elif op=='*':result=a*b
                else:
                    ck(b!=0,'every exact division defined');result=a/b
                charge=2
            elif op=='compare':
                a,b=registers[e[2]],registers[e[3]]
                rel=e[1]
                if rel=='<':truth=a<b
                elif rel=='<=':truth=a<=b
                elif rel=='>':truth=a>b
                elif rel=='>=':truth=a>=b
                elif rel=='==':truth=a==b
                elif rel=='!=':truth=a!=b
                else:raise ValueError(rel)
                ck(truth==e[4],'every complete rational comparison replays');charge=1
            elif op=='output':
                kind,n,values=expected[outputs]
                ck((e[1],e[2])==(kind,n),'all outputs in prescription order')
                ck(tuple(registers[i] for i in operands)==values,'every full rational output matches accuracy trace')
                for offset in (0,2):
                    ck(values[offset]<=values[offset+1],'ordered output endpoints')
                    ck((values[offset+1]-values[offset])/2<=F(1,2**512),'every separate output radius target')
                outputs+=1;charge=0
            else:raise ValueError(op)
            cost+=charge;by[category]+=charge
            # Destination ids are fresh consecutive SSA registers.
            if op in ('literal','copy','+','-','*','/'):
                ck(e[1]==allocated,'fresh consecutive register')
                if remaining[allocated]:registers[allocated]=result
                allocated+=1
            for i in operands:
                remaining[i]-=1
                if not remaining[i]:del registers[i]
            peak=max(peak,len(registers))
    ck(not registers and not any(remaining),'complete transcript consumed')
    ck(outputs==261,'all261 transcript outputs')
    ck(cost==data['scalar_work']['complete_register_cost']==3290939,'full instruction cost matches')
    ck(cost<=5000000,'setup threshold')
    ck(dict(by)==data['scalar_work']['by_category'],'all category costs match')
    ck(allocated==data['scalar_work']['register_count'],'all register assignments counted')
    ck(sha256(TRACE.read_bytes()).hexdigest()==data['trace_sha256'],'full transcript hash')
    report.update(result='PASS_FULL_TRANSCRIPT_AND_ALL_EXACT_TRACE_VALUES',
        scalar_work=cost,required_upper=5000000,headroom=5000000-cost,
        output_node_weight_pairs=outputs,instruction_inventory=dict(ins),
        transcript_lines=lines,register_assignments=allocated,peak_live_registers=peak,
        entire_mathematical_trace_equal_to692=True,by_category=dict(by),
        note='Full rational replay of every instruction; exact equality of all692 accuracy-trace values; scalar-program source correspondence still merits separate audit.')
except (AssertionError,ValueError,KeyError,IndexError) as exc:
    if not failures:failures.append(str(exc))
    report['result']='FAIL'
report.update(check_counts=dict(counts),total_checks=sum(counts.values()),
    source_sha256=sha256(SOURCE.read_bytes()).hexdigest(),
    trace_sha256=sha256(TRACE.read_bytes()).hexdigest(),
    old_accuracy_source_sha256=sha256(OLD.read_bytes()).hexdigest(),
    old_accuracy_replay_sha256=sha256(OLDREPLAY.read_bytes()).hexdigest(),
    script_sha256=sha256(HERE.read_bytes()).hexdigest())
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(report['result'])
print('Checks:',report['total_checks'],'; failures:',failures)
print('Scalar work:',report.get('scalar_work'),'; required <=5000000; outputs:',report.get('output_node_weight_pairs'))
print('Certificate:',OUT.relative_to(HERE.parents[2]))
if failures:raise SystemExit(1)
