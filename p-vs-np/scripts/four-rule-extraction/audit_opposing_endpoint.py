"""Step 487: read-only independent audit of the fixed output-485 transcript.

No constructor import/replay, extraction, or polynomial evaluation. Refuse to
replace evidence; run from the notebook with PYTHONDONTWRITEBYTECODE=1.
"""
import collections
import copy
import hashlib
import importlib.util
import json
import platform
from pathlib import Path
import parameterized_input as production

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BASE = HERE/'output-461/final/opposing-units'
SAVED = HERE/'output-485'
OUT = HERE/'output-487/verified'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def write(name, obj):
    (OUT/name).write_text(json.dumps(obj, separators=(',', ':'))+'\n')


def unique(pairs):
    d = {}
    for k, v in pairs:
        assert k not in d, ('duplicate key', k)
        d[k] = v
    return d


def parse(b):
    return json.loads(b, object_pairs_hook=unique)


def same(a, b):
    assert type(a) is type(b), (type(a), type(b))
    if isinstance(a, dict):
        assert a.keys() == b.keys()
        for k in a:
            same(a[k], b[k])
    elif isinstance(a, list):
        assert len(a) == len(b)
        for x, y in zip(a, b):
            same(x, y)
    else:
        assert a == b, (a, b)


def N(x):
    return ['not', x]


def O(x, y):
    return ['or', x, y]


def AND(x, y):
    return N(O(N(x), N(y)))


def tree_stats(t, alphabet, depth=1):
    if type(t) is str:
        assert t in alphabet  # This exact transcript is constant-free.
        return 1, depth
    assert type(t) is list
    assert (len(t) == 2 and t[0] == 'not') or (len(t) == 3 and t[0] == 'or')
    children = [tree_stats(c, alphabet, depth+1) for c in t[1:]]
    return 1+sum(x[0] for x in children), max(x[1] for x in children)


def check_rows(rows, goal, alphabet):
    evidence = []
    for i, r in enumerate(rows):
        assert set(r) == {'rule','f','refs'}
        f, refs, tag = r['f'], r['refs'], r['rule']
        needed = {'axiom':0, 'expansion':1, 'contraction':1, 'association':1, 'cut':2}
        assert tag in needed and type(refs) is list and len(refs) == needed[tag]
        assert all(type(j) is int and 0 <= j < i for j in refs), ('reference',i)
        ns, depth = tree_stats(f, alphabet)
        ps = [rows[j]['f'] for j in refs]
        if tag == 'axiom':
            assert f[0] == 'or' and f[1] == N(f[2]), ('axiom',i)
        elif tag == 'expansion':
            assert f[0] == 'or' and f[2] == ps[0], ('expansion',i)
        elif tag == 'contraction':
            assert ps[0] == O(f,f), ('contraction',i)
        elif tag == 'association':
            p = ps[0]
            assert p[0] == 'or' and p[2][0] == 'or', ('association premise',i)
            assert f == O(O(p[1],p[2][1]),p[2][2]), ('association',i)
        else:
            p, q = ps
            assert p[0] == q[0] == 'or' and q[1] == N(p[1]), ('cut pivot',i)
            assert f == O(p[2],q[2]), ('cut result',i)
        evidence.append(dict(record=i,rule=tag,refs=refs,nodes=ns,depth=depth,accepted=True))
    same(rows[-1]['f'], goal)
    return evidence


def nesting(x):
    if type(x) is dict:
        return 1+max((nesting(v) for v in x.values()),default=0)
    if type(x) is list:
        return 1+max((nesting(v) for v in x),default=0)
    return 0


def main():
    OUT.mkdir(parents=True, exist_ok=False)
    names = ('source.json','annotations.json','request.json','proof.jsonl')
    original = {n:(BASE/n).read_bytes() for n in names}
    saved = {p.name:p.read_bytes() for p in SAVED.iterdir() if p.is_file()}
    protected = {str(BASE/n):b for n,b in original.items()}
    protected.update({str(SAVED/n):b for n,b in saved.items()})
    pins = parse(saved['retained-inputs.json'])
    manifest = parse((BASE/'manifest.json').read_bytes())
    # Bind to the prior audit archive as well as the constructor's own pins.
    prior = parse((HERE/'output-468/archive-preservation.json').read_bytes())['hashes']
    for n,b in original.items():
        digest = sha(b)
        assert digest == pins[n] == manifest[n.split('.')[0]] == prior[str((BASE/n).relative_to(ROOT))]
    source, ann, oldreq = [parse(original[n]) for n in names[:3]]
    same(source,dict(format='ordered-width-three-v1',clauses=[
        dict(literals=[dict(variable='x',negative=False)],tree=0),
        dict(literals=[dict(variable='x',negative=True)],tree=0)],tree=['and',0,1]))
    same(ann,dict(format='L087-occurrences-v1',gadget=['u','v'],
        names=[['y0'],['y1'],['y2','y3'],['y4','y5']],alphabet=['y5','y4','y3','y2','y1','y0']))
    # Independently reconstruct complemented source leaves from signed positions.
    full = source['clauses'] + [dict(literals=[dict(variable=x,negative=sign) for x in ann['gadget']])
                                for sign in (False,True)]
    groups = {x:[] for x in ['x']+ann['gadget']}
    clauses = []
    for row,names_row in zip(full,ann['names']):
        leaves = []
        for lit,name in zip(row['literals'],names_row):
            groups[lit['variable']].append(name)
            leaves.append(N(N(name)) if lit['negative'] else N(name))
        clauses.append(leaves[0] if len(leaves)==1 else O(*leaves))
    f = AND(*clauses[:2]); c = AND(AND(f,clauses[2]),clauses[3])
    us = [O(AND(N(N(x)),N(N(y))),AND(N(x),N(y))) for x,y in groups.values()]
    u = AND(us[0],AND(us[1],us[2])); goal = N(AND(c,u))
    same(goal,oldreq['goal']); same(oldreq['alphabet'],ann['alphabet'])
    alpha = ann['alphabet']
    # Full dictionary including list order and deliberately colliding display names.
    ps = [dict(name=x,kind='boolean',originals=[x],polynomial=[[x,x],[x]]) for x in alpha]
    for i,x in enumerate(alpha):
        for j in range(i+1,len(alpha)):
            y = alpha[j]
            ps.append(dict(name=f'p{i}_{j}',kind='commutator',originals=[x,y],polynomial=[[x,y],[y,x]]))
    same(oldreq['dictionary'],dict(alphabet=alpha,placeholders=list(reversed(ps))))
    req = parse(saved['request.json']); raw = saved['proof.jsonl']
    delta = sorted(k for k in set(req)|set(oldreq) if req.get(k) != oldreq.get(k))
    assert delta == ['source_sha256']
    same(req,dict(oldreq,source_sha256=sha(raw)))
    assert oldreq['source_sha256'] == sha(original['proof.jsonl'])
    lines = raw.split(b'\n'); assert lines.pop() == b'' and all(lines)
    header,*rows = [parse(line) for line in lines]
    same(header,dict(format='literal-four-rule-v1',alphabet=alpha,goal=goal))
    record_evidence = check_rows(rows,goal,alpha)
    write('records.json',record_evidence)
    # Stage formulas obtained from independently reconstructed caller subtrees.
    s = f[1]  # f = not S: extract its literal child, without simplifying NN.
    a,b = us[0][1:]
    expected = [O(N(a),s),O(N(b),s),O(N(f),N(us[0])),O(N(c),N(us[0])),O(N(c),N(u)),goal]
    indices = [32,49,149,183,204,211]
    labels = ['first-consistency-disjunct','second-consistency-disjunct','source-and-first-consistency-core',
              'both-gadgets-attached','whole-formula-before-standalone-bridge','exact-goal']
    stages = parse(saved['stages.json'])
    wanted = [dict(label=l,record=i,endpoint=t) for l,i,t in zip(labels,indices,expected)]
    same(stages,wanted)
    for stage in wanted:
        same(rows[stage['record']]['f'],stage['endpoint'])
    write('stages.json',wanted)
    counts = dict(collections.Counter(r['rule'] for r in rows))
    assert counts == dict(axiom=77,cut=77,expansion=18,association=35,contraction=5)
    receipt = dict(accepted=True,records=len(rows),rule_counts=counts,
        formula_nodes=sum(r['nodes'] for r in record_evidence),bytes=len(raw),sha256=sha(raw))
    original_verdict = parse(saved['verification.json'])
    same(receipt,original_verdict['literal_receipt'])
    sizes = [tree_stats(goal,alpha)]+[(r['nodes'],r['depth']) for r in record_evidence]
    actual = dict(source_bytes=len(raw),request_bytes=len(saved['request.json']),
        tree_depth=max(d for _,d in sizes),tree_nodes=sum(n for n,_ in sizes),
        source_lines=len(rows),alphabet=len(alpha),dictionary_entries=len(ps),
        name_bytes=max(len(x.encode()) for x in alpha+[p['name'] for p in ps]))
    required = dict(source_bytes=2000000,request_bytes=2000000,tree_depth=64,tree_nodes=100000,
        source_lines=10000,alphabet=256,dictionary_entries=32896,name_bytes=4096)
    bounds = dict(actual=actual,required=required)
    same(bounds,original_verdict['input_bounds'])
    assert all(actual[k]<=required[k] for k in actual) and len(rows)<=1000
    json_actual = max(nesting(x) for x in [req,header]+rows)
    assert json_actual <= 160
    for key, val in required.items():
        assert production.CAPS['input_bytes' if key in ('source_bytes','request_bytes') else key] == val
    assert production.CAPS['json_depth'] == 160
    # Reuse the precise audited receiving boundary only after checking its pins.
    module_pins = parse((HERE/'output-466/verification.json').read_bytes())['scripts']
    module_evidence = {}
    for name in ('scripts/four-rule-extraction/parameterized_input.py','scripts/parity-four-rule/checker.py'):
        digest = sha((ROOT/name).read_bytes()); assert digest == module_pins[name]
        module_evidence[name] = digest
    spec = importlib.util.spec_from_file_location('audit487_checker',ROOT/'scripts/parity-four-rule/checker.py')
    checker = importlib.util.module_from_spec(spec); spec.loader.exec_module(checker)
    same(checker.check_bytes(raw,goal,2000000),receipt)
    reads = []; original_reader = production.read_bytes
    def observed_reader(path,key):
        b = original_reader(path,key); reads.append((str(path),key,b)); return b
    production.read_bytes = observed_reader
    try:
        received,received_raw,received_rows,received_receipt = production.request(SAVED/'proof.jsonl',SAVED/'request.json')
    finally:
        production.read_bytes = original_reader
    same(received,req); same(received_rows,rows); same(received_receipt,receipt)
    assert len(reads)==3 and reads[1][0]==reads[2][0]==str(SAVED/'proof.jsonl')
    assert received_raw is reads[1][2] and all(b==raw for _,_,b in reads[1:])
    same(production.input_bounds(req,raw,rows,SAVED/'request.json'),bounds)
    read_evidence = [dict(path=p,key=k,bytes=len(b),sha256=sha(b)) for p,k,b in reads]
    # Focused negative controls tied to this transcript, plus original diagnostic.
    negative = []
    for tag in counts:
        damaged = copy.deepcopy(rows); i = next(i for i,r in enumerate(rows) if r['rule']==tag)
        damaged[i]['f'] = alpha[0]
        data = (json.dumps(header)+'\n'+''.join(json.dumps(r)+'\n' for r in damaged)).encode()
        (OUT/('invalid-'+tag+'.jsonl')).write_bytes(data)
        try:
            checker.check_bytes(data,goal,2000000)
        except checker.Invalid as e:
            negative.append(dict(case=tag,record=i,error=str(e)))
        else:
            raise AssertionError(('mutation accepted',tag))
    for label,proof_path,request_path in [('old-diagnostic',BASE/'proof.jsonl',BASE/'request.json'),
                                         ('new-proof-old-request',SAVED/'proof.jsonl',BASE/'request.json')]:
        try:
            production.request(proof_path,request_path)
        except production.Rejected as e:
            negative.append(dict(case=label,error=str(e)))
        else:
            raise AssertionError(('binding negative accepted',label))
    assert negative[-2]['error']=='caller exact final endpoint'
    assert negative[-1]['error']=='caller source digest'
    write('negative-controls.json',negative)
    for path,b in protected.items():
        assert Path(path).read_bytes()==b
    write('binding.json',dict(original_files={n:sha(b) for n,b in original.items()},
        previous_audit_pins_matched=True,complete_request_delta=delta,groups=groups,
        original_request=oldreq,new_request=req,module_hashes=module_evidence,reads=read_evidence,
        first_immutable_bytes_returned=True,protected_files={p:sha(b) for p,b in protected.items()}))
    result = dict(accepted=True,failures=[],python=platform.python_version(),receipt=receipt,input_bounds=bounds,
        attempt_records=dict(actual=len(rows),required=1000),json_depth=dict(actual=json_actual,required=160),
        stages=len(stages),negative_controls=negative,protected_files=len(protected),
        full_saved_verification_compared=False,constructor_replayed=False,extraction_performed=False)
    # Compare all saved verdict fields, not just its accepting flag.
    same(original_verdict,dict(accepted=True,literal_receipt=receipt,input_bounds=bounds,
        attempt_records=dict(actual=len(rows),required=1000),retained_inputs_unchanged={n:True for n in names},
        changed_request_fields=delta,exact_goal_alphabet_dictionary=True,
        extraction_performed=False,full_composition_performed=False,failures=[]))
    result['full_saved_verification_compared']=True
    write('verification.json',result)
    print(json.dumps(dict(accepted=True,actual=actual,required=required,
        json_depth=result['json_depth'],attempt_records=result['attempt_records'],failures=[],
        evidence=str((OUT/'verification.json').relative_to(ROOT)))))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        if OUT.exists() and not (OUT/'verification.json').exists():
            write('failure.json',dict(accepted=False,error=repr(e)))
        raise
