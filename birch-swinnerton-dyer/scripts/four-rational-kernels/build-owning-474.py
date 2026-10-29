"""Fresh one-shot source builder. Never imports or executes a predecessor."""
import ast
import difflib
import hashlib
import json
from pathlib import Path
import sys
import traceback

sys.dont_write_bytecode = True
ROOT = Path.cwd()
BASE = ROOT/'scripts/four-rational-kernels'
OUT = BASE/'step-474-prelaunch'
OUT.mkdir()
edits = []

def save(name, value):
    (OUT/name).write_text(json.dumps(value, sort_keys=True, indent=2)+'\n')

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def identity(path):
    raw = path.read_bytes()
    return dict(bytes=len(raw), sha256=sha(raw))

def one(values, role):
    assert len(values) == 1, ('unique_role', role, len(values))
    return values[0]

def assignment(body, name, path):
    return one([(n, f'{path}[{i}]') for i,n in enumerate(body)
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in n.targets)], name)

def paths(node, path):
    yield node, path
    for field, value in ast.iter_fields(node):
        if isinstance(value, ast.AST):
            yield from paths(value, path+'.'+field)
        elif isinstance(value, list):
            for i, child in enumerate(value):
                if isinstance(child, ast.AST):
                    yield from paths(child, f'{path}.{field}[{i}]')

def same(node, expression):
    return ast.dump(node, include_attributes=False) == ast.dump(ast.parse(expression, mode='eval').body, include_attributes=False)

def production(tree):
    return one([(n, f'Module.body[{i}]') for i,n in enumerate(tree.body) if isinstance(n, ast.Try)], 'production_try')

def owners(tree, predecessor, destination):
    """Select by complete argument roles; locations are observations only."""
    outer, op = production(tree)
    exprs = [(n, f'{op}.body[{i}]') for i,n in enumerate(outer.body)
             if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call)]
    result = {}
    for kind in ('coordinator', 'worker'):
        receiver = f"(OUT/'{kind}-source-diff.txt').write_text"
        node, path = one([(n,p) for n,p in exprs if same(n.value.func, receiver)
                         and len(n.value.args) == 1 and not n.value.keywords], kind+'_diff_receiver')
        join = node.value.args[0]
        assert isinstance(join, ast.Call) and same(join.func, "''.join") and len(join.args) == 1 and not join.keywords
        diff = join.args[0]
        assert isinstance(diff, ast.Call) and same(diff.func, 'difflib.unified_diff') and len(diff.args) == 2
        assert len(diff.keywords) == 2 and {k.arg for k in diff.keywords} == {'fromfile', 'tofile'}
        keyword_nodes = {k.arg:k.value for k in diff.keywords}
        old = f'step-{predecessor}/{kind}.py'
        new = f'step-{destination}/{kind}.py'
        assert same(keyword_nodes['fromfile'], repr(old)) and same(keyword_nodes['tofile'], repr(new))
        if kind == 'coordinator':
            assert same(diff.args[0], f"(BASE/{old!r}).read_text().splitlines(True)")
            assert same(diff.args[1], 'COORDINATOR.splitlines(True)')
            first = diff.args[0].func.value.func.value.right
            fields = [first, keyword_nodes['fromfile'], keyword_nodes['tofile']]
        else:
            assert same(diff.args[0], 'worker_before.splitlines(True)')
            assert same(diff.args[1], 'worker.splitlines(True)')
            fields = [keyword_nodes['fromfile'], keyword_nodes['tofile']]
        result[kind+'_diff'] = (node, path, fields)
    node, path = one([(n,p) for n,p in exprs if same(n.value.func, 'save')
        and len(n.value.args) == 2 and not n.value.keywords and same(n.value.args[0], "'manifest.json'")
        and isinstance(n.value.args[1], ast.Dict)], 'manifest_destination_arguments')
    data = node.value.args[1]
    assert all(isinstance(k, ast.Constant) and isinstance(k.value, str) for k in data.keys)
    keys = [k.value for k in data.keys]
    assert len(keys) == len(set(keys)) and keys.count('step') == 1
    result['manifest'] = (node, path, [data.values[keys.index('step')]])
    return result

try:
    evidence = json.loads((ROOT/'drafts/source-notes/2026-10-25-n43-46-owning-call-evidence.json').read_text())
    for rel, expected in evidence['frozen_files'].items():
        assert identity(ROOT/rel) == expected, ('frozen_file', rel)
    for rel, expected in evidence['frozen_trees'].items():
        actual = sorted(str(p.relative_to(ROOT)) for p in (ROOT/rel).rglob('*') if p.is_file())
        assert actual == expected, ('frozen_tree', rel)
    assert all(not (ROOT/rel).exists() for rel in evidence['absent'])
    raw = (BASE/'step-468/coordinator.py').read_bytes()
    assert len(raw) == 19680 and sha(raw) == '2cdae569efd7406a76f61e89104f47d4b6301094223e0424d1c725dcf906af13'
    source = raw.decode('utf-8')
    assert source.encode('utf-8') == raw
    offsets = [0]
    for line in raw.splitlines(keepends=True):
        offsets.append(offsets[-1]+len(line))
    tree = ast.parse(source)

    def segment(node):
        a = offsets[node.lineno-1]+node.col_offset
        b = offsets[node.end_lineno-1]+node.end_col_offset
        return a,b,raw[a:b]

    def change(node, path, role, new, owner):
        a,b,old = segment(node)
        oa,ob,whole = segment(owner)
        assert old.decode() == ast.get_source_segment(source, node)
        assert oa <= a < b <= ob
        edits.append(dict(role=role, path=path, start=a, end=b, old=old.decode(), new=new,
            owner_start=oa, owner_end=ob, complete_original_owner=whole.decode()))

    def constants(owner, path, old, new, count, role):
        found = [(n,p) for n,p in paths(owner,path) if isinstance(n, ast.Constant) and n.value == old]
        assert len(found) == count, ('constant_role_count', role, len(found), count)
        for n,p in found:
            change(n,p,role,repr(new),owner)

    selected_owners = owners(tree, 461, 468)
    for role, (node, path, fields) in selected_owners.items():
        pin = evidence['owners'][role]
        a,b,whole = segment(node)
        assert pin['count'] == 1 and whole.decode() == pin['complete_original_owner']
        assert (a,b,sha(whole)) == (pin['start'],pin['end'],pin['sha256'])
        assert path == pin['path'] and len(fields) == len(pin['fields'])
        role_paths = {id(n):p for n,p in paths(node,path)}
        for field, field_pin in zip(fields, pin['fields']):
            fa,fb,old = segment(field)
            assert (fa,fb,old.decode(),role_paths[id(field)],field.value) == (
                field_pin['start'],field_pin['end'],field_pin['old_bytes'],field_pin['path'],field_pin['value'])

    n,p = assignment(tree.body,'OUT','Module.body')
    constants(n,p,'step-468','step-474',1,'exclusive_destination')
    n,p = assignment(tree.body,'INDICES','Module.body')
    assert ast.literal_eval(n.value) == (39,40,41,42)
    change(n.value,p+'.value','indices','(43,44,45,46)',n)
    n,p = assignment(tree.body,'steps','Module.body')
    old_steps = ast.literal_eval(n.value)
    assert old_steps == (417,419,422,424,429,431,433,435,437,440,442,446,449,451,453,455,457,459,461,463)
    change(n.value,p+'.value','historical_steps',repr(old_steps+(468,470)),n)
    n,p = assignment(tree.body,'roots','Module.body')
    old_roots = segment(n.value)[2].decode()
    root_tuple = '(417,419,422,424,426,429,431,433,435,437,440,442,444,446,449,451,453,455,457,459,461,463)'
    assert old_roots.count(root_tuple) == 1
    new_roots = old_roots.replace(root_tuple,root_tuple[:-1]+',468,470)',1)
    new_roots += "+[BASE/'step-468-prelaunch',BASE/'step-468-postcheck',BASE/'step-472-prelaunch',BASE/'step-472-postmortem']"
    change(n.value,p+'.value','complete_frozen_roots',new_roots,n)
    n,p = assignment(tree.body,'transition_paths','Module.body')
    old_transitions = ast.literal_eval(n.value)
    assert len(old_transitions) == 20
    new_transitions = old_transitions+['drafts/2026-10-25-n39-42-parsed-document-transition.json',
                                    'drafts/2026-10-25-l114-audit-document-transition.json']
    change(n.value,p+'.value','twenty_two_transition_suffixes',repr(new_transitions),n)
    n,p = assignment(tree.body,'selected','Module.body')
    assert isinstance(n.value,ast.BinOp) and isinstance(n.value.op,ast.Add) and same(n.value.right,'transition_paths')
    old_selected = ast.literal_eval(n.value.left)
    assert old_selected[0] == 'lemmas/L113-kernels-thirty-five-through-thirty-eight-certificates.md'
    additions = [
        'scripts/four-rational-kernels/check-468-evidence.py',
        'drafts/literature/2026-10-25-kernels-forty-three-through-forty-six.md',
        'drafts/source-notes/2026-10-25-n43-46-production-coverage.md',
        'drafts/2026-10-25-n43-46-source-metadata.json',
        'drafts/2026-10-25-n43-46-attempt.md',
        'scripts/four-rational-kernels/build-parsed-472.py',
        'ATTEMPTS/052-coordinator-obsolete-line-selection-stop.md',
        'history/472-2026-10-25-n43-46-owning-statement-stop.md',
        'drafts/literature/2026-10-25-n43-46-statement-owner-selection.md',
        'drafts/source-notes/2026-10-25-n43-46-owning-call-coverage.md',
        'drafts/source-notes/2026-10-25-n43-46-owning-call-evidence.json',
        'scripts/four-rational-kernels/build-owning-474.py',
        'drafts/2026-10-25-n43-46-role-selected-attempt.md']
    fresh_products = ['scripts/four-rational-kernels/step-474-prelaunch/'+name for name in
        ('edit-map.json','coordinator-source-diff.txt','verification.json','coordinator.py','worker-expected.py')]
    new_selected = ['lemmas/L114-kernels-thirty-nine-through-forty-two-certificates.md']+old_selected[1:]+additions+fresh_products
    assert len(new_selected) == len(set(new_selected))
    change(n.value.left,p+'.value.left','selected_inputs',repr(new_selected),n)

    outer,op = production(tree)
    loop,lp = one([(n,f'{op}.body[{i}]') for i,n in enumerate(outer.body) if isinstance(n,ast.For)
        and same(n.target,'step') and same(n.iter,'steps')], 'historical_report_loop')
    old_test = 'step in (446,449,451,453,455,457,459,461,463)'
    new_test = 'step in (446,449,451,453,455,457,459,461,463,468,470)'
    n,p = one([(n,f'{lp}.body[{i}]') for i,n in enumerate(loop.body) if isinstance(n,ast.If)
        and same(n.test,old_test)], 'direct_preservation_if')
    assert len(n.body) == 1
    change(n.test,p+'.test','preservation_branch',new_test,n)
    dispatch,dp = one([(n,f'{lp}.body[{i}]') for i,n in enumerate(loop.body) if isinstance(n,ast.If)
        and same(n.test,'step>=424')], 'dispatch_owner')
    branch,bp = one([(n,f'{dp}.body[{i}]') for i,n in enumerate(dispatch.body) if isinstance(n,ast.If)], 'dispatch_head')
    for expected in ('step==424','step==429','step in (431,435,440)','step==442'):
        assert same(branch.test,expected) and len(branch.orelse) == 1 and isinstance(branch.orelse[0],ast.If)
        branch = branch.orelse[0]
        bp += '.orelse[0]'
    assert same(branch.test,old_test)
    change(branch.test,bp+'.test','original_report_dispatch_tail',new_test,branch)
    loop,lp = one([(n,f'{op}.body[{i}]') for i,n in enumerate(outer.body) if isinstance(n,ast.For)
        and same(n.target,'step') and isinstance(n.iter,ast.Tuple)], 'source_map_loop')
    maps = ast.literal_eval(loop.iter)
    assert maps == (417,419,422,424,431,433,435,437,440,442,446,449,451,453,455,457,459,461,463)
    change(loop.iter,lp+'.iter','source_map_steps',repr(maps+(468,470)),loop)
    n,p = assignment(loop.body,'f',lp+'.body')
    assert isinstance(n.value,ast.IfExp) and same(n.value.test,'step in (417,424,431,435,440,449,453,457,461)')
    change(n.value.test,p+'.value.test','whole_source_map_dispatch','step in (417,424,431,435,440,449,453,457,461,468)',n)

    for role,(node,path,fields) in selected_owners.items():
        field_paths = {id(n):p for n,p in paths(node,path)}
        if role == 'manifest':
            assert fields[0].value == 'BSD-2026-10-25-468-kernels-thirty-nine-through-forty-two-parsed'
            values = ['BSD-2026-10-25-474-kernels-forty-three-through-forty-six']
        else:
            kind = role.removesuffix('_diff')
            values = ([f'step-468/{kind}.py']*(len(fields)-1))+[f'step-474/{kind}.py']
        for field,value in zip(fields,values):
            change(field,field_paths[id(field)],role,repr(value),node)
    n,p = assignment(outer.body,'worker_before',op+'.body')
    constants(n,p,'step-461/worker.py','step-468/worker.py',1,'worker_predecessor')
    n,p = assignment(outer.body,'worker_changes',op+'.body')
    assert ast.literal_eval(n.value) == [('assert INDEX in (35,36,37,38)','assert INDEX in (39,40,41,42)'),("'kernel_461_'","'kernel_468_'")]
    worker_changes = [('assert INDEX in (39,40,41,42)','assert INDEX in (43,44,45,46)'),("'kernel_468_'","'kernel_474_'")]
    change(n.value,p+'.value','two_whole_worker_substitutions',repr(worker_changes),n)
    loop,lp = one([(n,f'{op}.body[{i}]') for i,n in enumerate(outer.body) if isinstance(n,ast.For)
        and same(n.iter,'INDICES')], 'production_loop')
    n,p = one([
        (n,f'{lp}.body[{i}]') for i,n in enumerate(loop.body) if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id == 'repl' for t in n.targets)
        and isinstance(n.value,ast.DictComp)], 'replacement_value_binding')
    constants(n,p,'step-468','step-474',1,'arithmetic_replacement_destination_only')

    ordered = sorted(edits,key=lambda e:e['start'])
    assert len(ordered) == 19
    for a,b in zip(ordered,ordered[1:]):
        assert a['end'] <= b['start']
    # Complete finite map exists before the first byte is applied.
    changed = raw
    for e in reversed(ordered):
        a,b = e['start'],e['end']
        assert changed[a:b] == e['old'].encode()
        changed = changed[:a]+e['new'].encode()+changed[b:]
    intervals = []
    oc = nc = 0
    for e in ordered:
        length = e['start']-oc
        assert raw[oc:e['start']] == changed[nc:nc+length]
        intervals.append(dict(old_start=oc,old_end=e['start'],new_start=nc,new_end=nc+length,sha256=sha(raw[oc:e['start']])))
        oc = e['end']
        nc += length+len(e['new'].encode())
    assert raw[oc:] == changed[nc:]
    intervals.append(dict(old_start=oc,old_end=len(raw),new_start=nc,new_end=len(changed),sha256=sha(raw[oc:])))
    restored = changed
    new_offsets = []
    shift = 0
    for e in ordered:
        new_offsets.append((e['start']+shift,e['start']+shift+len(e['new'].encode()),e['old'].encode()))
        shift += len(e['new'].encode())-(e['end']-e['start'])
    for a,b,old in reversed(new_offsets):
        restored = restored[:a]+old+restored[b:]
    assert restored == raw
    new_source = changed.decode('utf-8')
    assert new_source.encode('utf-8') == changed
    new_tree = ast.parse(new_source)
    new_nodes = {p:n for n,p in paths(new_tree,'Module')}
    for e in ordered:
        assert ast.get_source_segment(new_source,new_nodes[e['path']]) == e['new']
    new_owners = owners(new_tree,468,474)
    assert new_owners['manifest'][2][0].value == 'BSD-2026-10-25-474-kernels-forty-three-through-forty-six'
    for name,expected in [('INDICES',(43,44,45,46)),('steps',old_steps+(468,470)),('transition_paths',new_transitions)]:
        n,_ = assignment(new_tree.body,name,'Module.body')
        assert ast.literal_eval(n.value) == expected
    n,_ = assignment(new_tree.body,'selected','Module.body')
    assert ast.literal_eval(n.value.left) == new_selected
    assert len(new_transitions) == 22 and new_transitions[:20] == old_transitions
    assert not (BASE/'step-474').exists()
    for rel in new_selected+new_transitions:
        if rel not in fresh_products:
            assert (ROOT/rel).is_file(), ('selected_file_exists',rel)
    worker_raw = (BASE/'step-468/worker.py').read_bytes()
    assert len(worker_raw) == 5789 and sha(worker_raw) == 'edb68bad705810bd9d3d1d8655b42a12165602e214e1713fac1323badd4e53ea'
    worker = worker_raw.decode('utf-8')
    worker_edits = []
    for old,new in worker_changes:
        assert worker.count(old) == 1
        start = worker.index(old)
        worker_edits.append(dict(start=start,end=start+len(old),old=old,new=new))
    worker_edits.sort(key=lambda e:e['start'])
    assert worker_edits[0]['end'] <= worker_edits[1]['start']
    worker_intervals = []
    oc = nc = 0
    for e in worker_edits:
        length = e['start']-oc
        worker_intervals.append(dict(old_start=oc,old_end=e['start'],new_start=nc,new_end=nc+length,
                                     complete_untouched_bytes=worker[oc:e['start']]))
        oc = e['end']
        nc += length+len(e['new'])
    worker_intervals.append(dict(old_start=oc,old_end=len(worker),new_start=nc,new_end=nc+len(worker)-oc,
                                 complete_untouched_bytes=worker[oc:]))
    for e in reversed(worker_edits):
        worker = worker[:e['start']]+e['new']+worker[e['end']:]
    for span in worker_intervals:
        assert worker[span['new_start']:span['new_end']] == span['complete_untouched_bytes']
    wtree = ast.parse(worker)
    assert any(isinstance(n,ast.Assert) and isinstance(n.test,ast.BoolOp)
        and same(n.test.values[0],'INDEX in (43,44,45,46)') for n in wtree.body)
    n,_ = assignment(wtree.body,'IDENTITY','Module.body')
    assert any(isinstance(n,ast.Constant) and n.value == 'kernel_474_' for n in ast.walk(n.value))
    compile(new_source,str(OUT/'coordinator.py'),'exec',flags=0,dont_inherit=True,optimize=0)
    compile(worker,str(OUT/'worker-expected.py'),'exec',flags=0,dont_inherit=True,optimize=0)
    (OUT/'coordinator.py').write_bytes(changed)
    (OUT/'worker-expected.py').write_text(worker)
    (OUT/'coordinator-source-diff.txt').write_text(''.join(difflib.unified_diff(source.splitlines(True),new_source.splitlines(True),fromfile='step-468/coordinator.py',tofile='step-474/coordinator.py')))
    save('edit-map.json',dict(old_sha256=sha(raw),new_sha256=sha(changed),edits=ordered,untouched_intervals=intervals,
        worker_old_sha256=sha(worker_raw),worker_new_sha256=sha(worker.encode()),worker_edits=worker_edits,
        worker_untouched_intervals=worker_intervals))
    save('verification.json',dict(status='PASS',unique_structural_roles=True,complete_old_bytes_pinned=True,
        disjoint_spans=True,untouched_intervals_and_tails_equal=True,reverse_edits_restore_source=True,
        all_new_structural_values_equal=True,owning_roles_reselected=True,compile_optimize=0,
        coordinator_sha256=sha(changed),worker_sha256=sha(worker.encode()),edits=19,suffixes=22,
        frozen_files=evidence['frozen_files'],frozen_trees=evidence['frozen_trees'],absent=evidence['absent'],
        fresh_products=fresh_products,execution_started=False,prelaunch_outside_unstarted_cap=True))
    assert all((ROOT/rel).is_file() for rel in new_selected+new_transitions)
    assert all(identity(ROOT/rel) == expected for rel,expected in evidence['frozen_files'].items())
    print(json.dumps(dict(status='PASS',edits=19,suffixes=22,path=str(OUT.relative_to(ROOT)))))
except BaseException as exc:
    save('first-failure.json',dict(status='STOP',type=type(exc).__name__,message=str(exc),
        traceback=traceback.format_exc(),execution_started=False,edits_constructed=edits))
    print(json.dumps(dict(status='STOP',error=str(exc),execution_started=False,path=str(OUT.relative_to(ROOT)))))
    sys.exit(1)
