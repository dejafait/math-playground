"""Saved-certificate rejection tests and one deliberately identity-neutral change."""
import copy
import json
from pathlib import Path
import receive as r

OUT = Path(__file__).with_name('output-449')
MUT = OUT/'mutations'
MUT.mkdir(exist_ok=True)
original = r.load(OUT/'certificate.json')
results = []


def run(name, change, should_accept=False):
    cert = copy.deepcopy(original)
    source = change(cert)
    path, sp = MUT/(name+'.json'), MUT/(name+'.jsonl')
    path.write_text(json.dumps(cert,separators=(',',':'))+'\n')
    sp.write_text(cert['source_text'] if source is None else source)
    try:
        received = r.receive(path,sp)
        accepted, reason = True, 'both identities and full reception still hold'
    except (r.Rejected,r.checker.Invalid,ValueError,TypeError,KeyError) as err:
        accepted, reason = False,str(err)
    results.append(dict(case=name,accepted=accepted,expected_accept=should_accept,
                        passed=accepted == should_accept,reason=reason,
                        certificate_path=str(path.relative_to(BASE)),source_path=str(sp.relative_to(BASE))))


BASE = r.BASE.parent
run('missing-unused-boolean-entry',lambda d:d['dictionary']['placeholders'].pop(1) and None)
run('changed-pair-polynomial',lambda d:d['dictionary']['placeholders'][2]['polynomial'].pop() and None)
run('alphabet-order',lambda d:d['dictionary']['alphabet'].reverse())
run('placeholder-alias',lambda d:d['dictionary']['placeholders'][1].update(name='sigma:A'))
run('transport-alias',lambda d:d['name_transport'].update({'x2':'A'}))
run('foreign-symbol-in-disconnected-graph',lambda d:d['graph']['edges'][0][2].append('foreign'))
run('boolean-edge-index',lambda d:d['graph']['edges'][0].__setitem__(0,True))
run('out-of-range-edge',lambda d:d['graph']['edges'][0].__setitem__(1,d['graph']['vertices']))
run('boolean-vertex-count',lambda d:d['graph'].__setitem__('vertices',True))
run('malformed-affine-label',lambda d:d['graph']['edges'][0].__setitem__(2,'A'))
run('extra-graph-field',lambda d:d['graph'].__setitem__('implicit_circuit',{}))
run('missing-unused-root',lambda d:d['line_roots'].pop(3) and None)
run('boolean-root-index',lambda d:d['line_roots'].__setitem__(0,True))
run('wrong-final-endpoint',lambda d:d['graph'].__setitem__('sink',7))
run('changed-caps',lambda d:d['caps'].__setitem__('records',3_000_000))
run('changed-block-argument',lambda d:d['blocks'][3].__setitem__('arguments',['A']))
run('boolean-block-entry',lambda d:d['blocks'][0].__setitem__('entry',True))
run('unretained-source',lambda d:d.__setitem__('source_text',d['source_text']+'\n'))


def cycle(d):
    e = d['graph']['edges'][0]
    e[1] = e[0]
run('cycle',cycle)


def bad_source(d):
    lines = d['source_text'].splitlines()
    rec = json.loads(lines[4])
    rec['refs'] = [True]
    lines[4] = json.dumps(rec)
    return '\n'.join(lines)+'\n'
run('malformed-source-reference',bad_source)


def bad_endpoint(d):
    lines = d['source_text'].splitlines()
    h = json.loads(lines[0])
    h['goal'] = 'true'
    lines[0] = json.dumps(h)
    return '\n'.join(lines)+'\n'
run('changed-source-endpoint',bad_endpoint)


def damage_unused(d):
    block = next(b for b in d['blocks'] if b['line'] == 3 and b['role'] == 'seed')
    first,last = block['edge_range']
    hits = 0
    for _,_,label in d['graph']['edges'][first:last-2]:
        if 'tau:A:B' in label:
            label[:] = [x for x in label if x != 'tau:A:B']
            hits += 1
    assert hits > 0
run('unused-B-seed-damage',damage_unused)

# A legal cancelling affine-label change preserves the actual formal graph
# polynomial. Acceptance is expected and is not a missed corruption.
def neutral(d):
    label = d['graph']['edges'][0][2]
    label.extend(['A','A'])
run('neutral-cancelling-affine-label',neutral,True)

bad = copy.deepcopy(original)
damage_unused(bad)
g = bad['graph']
order = r.topo(g['vertices'],g['edges'])
a = r.Arithmetic()
probe = []
records = [json.loads(x) for x in bad['source_text'].splitlines()][1:]
for i in (3,8):
    zero = a.evaluate(g['vertices'],g['edges'],order,0,i+1,'zero')
    sub = a.evaluate(g['vertices'],g['edges'],order,0,i+1,'axioms')
    target = a.translation(records[i]['f'])
    probe.append(dict(line=i,zero=r.serial(zero),substituted=r.serial(sub),target=r.serial(target),
                      both_identities=not zero and sub == target))
assert not probe[0]['both_identities'] and probe[1]['both_identities']
# Reuse every preserved literal-checker corruption without modifying its archive.
source_tests = []
for path in sorted((r.BASE/'parity-four-rule/output-goal-directed-447').glob('corrupt-*.jsonl')):
    try:
        r.checker.check(path,r.GOAL)
        rejected, reason = False,'accepted'
    except r.checker.Invalid as err:
        rejected,reason = True,str(err)
    source_tests.append(dict(path=str(path.relative_to(BASE)),rejected=rejected,reason=reason))

result = dict(certificate_tests=results, source_tests=source_tests,
              unused_branch_discriminator=probe, discriminator_arithmetic=a.counts,
              summary=dict(certificate_cases=len(results),expected_rejections=sum(not v['expected_accept'] for v in results),
                           neutral_acceptances=sum(v['accepted'] and v['expected_accept'] for v in results),
                           source_rejections=sum(t['rejected'] for t in source_tests),
                           failures=[v['case'] for v in results if not v['passed']]))
(OUT/'mutation-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result['summary']))
print('Required: all expected rejections; neutral change accepted; damaged line 3 fails while final line 8 passes.')
print('Complete mutation evidence:',OUT/'mutation-results.json')
assert not result['summary']['failures'] and len(source_tests) == 20 and all(t['rejected'] for t in source_tests)
