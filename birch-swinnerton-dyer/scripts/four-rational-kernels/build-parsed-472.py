"""One-shot role-selected byte splicing; no arithmetic execution."""
import ast
import difflib
import hashlib
import json
from pathlib import Path
import sys
import traceback

sys.dont_write_bytecode = True
ROOT = Path.cwd()
BASE = ROOT / 'scripts/four-rational-kernels'
OUT = BASE / 'step-472-prelaunch'
OUT.mkdir()
edits = []

def save(name, value):
    (OUT/name).write_text(json.dumps(value, sort_keys=True, indent=2)+'\n')

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def one(values, role):
    assert len(values) == 1, ('unique_role', role, len(values))
    return values[0]

def assignment(body, name, path):
    return one([(n, f'{path}[{i}]') for i,n in enumerate(body)
        if isinstance(n, ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets)], name)

def paths(node, path):
    yield node, path
    for field, value in ast.iter_fields(node):
        if isinstance(value, ast.AST):
            yield from paths(value, path+'.'+field)
        elif isinstance(value, list):
            for i,child in enumerate(value):
                if isinstance(child,ast.AST):
                    yield from paths(child,f'{path}.{field}[{i}]')

try:
    raw=(BASE/'step-468/coordinator.py').read_bytes()
    assert len(raw)==19680 and sha(raw)=='2cdae569efd7406a76f61e89104f47d4b6301094223e0424d1c725dcf906af13'
    source=raw.decode('utf-8')
    assert source.encode('utf-8')==raw
    offsets=[0]
    for line in raw.splitlines(keepends=True): offsets.append(offsets[-1]+len(line))
    tree=ast.parse(source)

    def segment(node):
        a=offsets[node.lineno-1]+node.col_offset
        b=offsets[node.end_lineno-1]+node.end_col_offset
        return a,b,raw[a:b]

    def change(node,path,role,new,owner):
        a,b,old=segment(node)
        oa,ob,whole=segment(owner)
        assert old.decode()==ast.get_source_segment(source,node)
        assert oa<=a<b<=ob
        edits.append(dict(role=role,path=path,start=a,end=b,old=old.decode(),new=new,
                          owner_start=oa,owner_end=ob,complete_original_owner=whole.decode()))

    def constants(owner,path,old,new,count,role):
        found=[(n,p) for n,p in paths(owner,path) if isinstance(n,ast.Constant) and n.value==old]
        assert len(found)==count, ('constant_role_count',role,len(found),count)
        for n,p in found: change(n,p,role,repr(new),owner)

    n,p=assignment(tree.body,'OUT','Module.body')
    constants(n,p,'step-468','step-472',1,'exclusive_destination')
    n,p=assignment(tree.body,'INDICES','Module.body')
    assert ast.literal_eval(n.value)==(39,40,41,42)
    change(n.value,p+'.value','indices','(43,44,45,46)',n)
    n,p=assignment(tree.body,'steps','Module.body')
    old_steps=ast.literal_eval(n.value)
    assert old_steps==(417,419,422,424,429,431,433,435,437,440,442,446,449,451,453,455,457,459,461,463)
    change(n.value,p+'.value','historical_steps',repr(old_steps+(468,470)),n)
    n,p=assignment(tree.body,'roots','Module.body')
    old_roots=segment(n.value)[2].decode()
    root_tuple='(417,419,422,424,426,429,431,433,435,437,440,442,444,446,449,451,453,455,457,459,461,463)'
    assert old_roots.count(root_tuple)==1
    new_roots=old_roots.replace(root_tuple,root_tuple[:-1]+',468,470)',1)
    new_roots+="+[BASE/'step-468-prelaunch',BASE/'step-468-postcheck']"
    change(n.value,p+'.value','complete_frozen_roots',new_roots,n)
    n,p=assignment(tree.body,'transition_paths','Module.body')
    old_transitions=ast.literal_eval(n.value)
    assert len(old_transitions)==20
    new_transitions=old_transitions+[
        'drafts/2026-10-25-n39-42-parsed-document-transition.json',
        'drafts/2026-10-25-l114-audit-document-transition.json']
    change(n.value,p+'.value','twenty_two_transition_suffixes',repr(new_transitions),n)
    n,p=assignment(tree.body,'selected','Module.body')
    assert isinstance(n.value,ast.BinOp) and isinstance(n.value.op,ast.Add)
    assert isinstance(n.value.right,ast.Name) and n.value.right.id=='transition_paths'
    old_selected=ast.literal_eval(n.value.left)
    assert old_selected[0]=='lemmas/L113-kernels-thirty-five-through-thirty-eight-certificates.md'
    additions=[
        'scripts/four-rational-kernels/check-468-evidence.py',
        'drafts/literature/2026-10-25-kernels-forty-three-through-forty-six.md',
        'drafts/source-notes/2026-10-25-n43-46-production-coverage.md',
        'drafts/2026-10-25-n43-46-source-metadata.json',
        'drafts/2026-10-25-n43-46-attempt.md',
        'scripts/four-rational-kernels/build-parsed-472.py',
        'scripts/four-rational-kernels/step-472-prelaunch/edit-map.json',
        'scripts/four-rational-kernels/step-472-prelaunch/coordinator-source-diff.txt',
        'scripts/four-rational-kernels/step-472-prelaunch/verification.json',
        'scripts/four-rational-kernels/step-472-prelaunch/coordinator.py',
        'scripts/four-rational-kernels/step-472-prelaunch/worker-expected.py']
    new_selected=['lemmas/L114-kernels-thirty-nine-through-forty-two-certificates.md']+old_selected[1:]+additions
    assert len(new_selected)==len(set(new_selected))
    change(n.value.left,p+'.value.left','selected_inputs',repr(new_selected),n)
    outer,op=one([(n,f'Module.body[{i}]') for i,n in enumerate(tree.body) if isinstance(n,ast.Try)],'production_try')
    loop,lp=one([(n,f'{op}.body[{i}]') for i,n in enumerate(outer.body)
        if isinstance(n,ast.For) and isinstance(n.target,ast.Name) and n.target.id=='step'
        and isinstance(n.iter,ast.Name) and n.iter.id=='steps'],'historical_report_loop')
    old_test='step in (446,449,451,453,455,457,459,461,463)'
    new_test='step in (446,449,451,453,455,457,459,461,463,468,470)'
    n,p=one([(n,f'{lp}.body[{i}]') for i,n in enumerate(loop.body)
        if isinstance(n,ast.If) and ast.get_source_segment(source,n.test)==old_test],'direct_preservation_if')
    assert len(n.body)==1
    change(n.test,p+'.test','preservation_branch',new_test,n)
    dispatch,dp=one([(n,f'{lp}.body[{i}]') for i,n in enumerate(loop.body)
        if isinstance(n,ast.If) and ast.get_source_segment(source,n.test)=='step>=424'],'dispatch_owner')
    branch,bp=one([(n,f'{dp}.body[{i}]') for i,n in enumerate(dispatch.body) if isinstance(n,ast.If)],'dispatch_head')
    for expected in ('step==424','step==429','step in (431,435,440)','step==442'):
        assert ast.get_source_segment(source,branch.test)==expected
        assert len(branch.orelse)==1 and isinstance(branch.orelse[0],ast.If)
        branch=branch.orelse[0]; bp+='.orelse[0]'
    assert ast.get_source_segment(source,branch.test)==old_test
    change(branch.test,bp+'.test','original_report_dispatch_tail',new_test,branch)
    loop,lp=one([(n,f'{op}.body[{i}]') for i,n in enumerate(outer.body)
        if isinstance(n,ast.For) and isinstance(n.target,ast.Name) and n.target.id=='step'
        and isinstance(n.iter,ast.Tuple)],'source_map_loop')
    maps=ast.literal_eval(loop.iter)
    assert maps==(417,419,422,424,431,433,435,437,440,442,446,449,451,453,455,457,459,461,463)
    change(loop.iter,lp+'.iter','source_map_steps',repr(maps+(468,470)),loop)
    n,p=assignment(loop.body,'f',lp+'.body')
    assert isinstance(n.value,ast.IfExp)
    assert ast.get_source_segment(source,n.value.test)=='step in (417,424,431,435,440,449,453,457,461)'
    change(n.value.test,p+'.value.test','whole_source_map_dispatch','step in (417,424,431,435,440,449,453,457,461,468)',n)
    exprs=[(n,f'{op}.body[{i}]') for i,n in enumerate(outer.body) if isinstance(n,ast.Expr)]
    n,p=one([(n,p) for n,p in exprs if n.lineno==141],'coordinator_diff_call')
    constants(n,p,'step-461/coordinator.py','step-468/coordinator.py',2,'coordinator_diff_predecessor')
    constants(n,p,'step-468/coordinator.py','step-472/coordinator.py',1,'coordinator_diff_destination')
    n,p=one([(n,p) for n,p in exprs if n.lineno==142],'manifest_save')
    constants(n,p,'BSD-2026-10-25-468-kernels-thirty-nine-through-forty-two-parsed',
              'BSD-2026-10-25-472-kernels-forty-three-through-forty-six',1,'manifest_step')
    n,p=assignment(outer.body,'worker_before',op+'.body')
    constants(n,p,'step-461/worker.py','step-468/worker.py',1,'worker_predecessor')
    n,p=assignment(outer.body,'worker_changes',op+'.body')
    assert ast.literal_eval(n.value)==[('assert INDEX in (35,36,37,38)','assert INDEX in (39,40,41,42)'),("'kernel_461_'","'kernel_468_'")]
    worker_changes=[('assert INDEX in (39,40,41,42)','assert INDEX in (43,44,45,46)'),("'kernel_468_'","'kernel_472_'")]
    change(n.value,p+'.value','two_whole_worker_substitutions',repr(worker_changes),n)
    n,p=one([(n,p) for n,p in exprs if n.lineno==156],'worker_diff_call')
    constants(n,p,'step-461/worker.py','step-468/worker.py',1,'worker_diff_predecessor')
    constants(n,p,'step-468/worker.py','step-472/worker.py',1,'worker_diff_destination')
    loop,lp=one([(n,f'{op}.body[{i}]') for i,n in enumerate(outer.body)
        if isinstance(n,ast.For) and isinstance(n.iter,ast.Name) and n.iter.id=='INDICES'],'production_loop')
    n,p=one([(n,f'{lp}.body[{i}]') for i,n in enumerate(loop.body)
        if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='repl' for t in n.targets)
        and isinstance(n.value,ast.DictComp)],'replacement_value_binding')
    constants(n,p,'step-468','step-472',1,'arithmetic_replacement_destination_only')

    ordered=sorted(edits,key=lambda e:e['start'])
    assert len(ordered)==19
    for a,b in zip(ordered,ordered[1:]): assert a['end']<=b['start']
    changed=raw
    for e in reversed(ordered):
        a,b=e['start'],e['end']
        assert changed[a:b]==e['old'].encode()
        changed=changed[:a]+e['new'].encode()+changed[b:]
    intervals=[]; oc=nc=0
    for e in ordered:
        length=e['start']-oc
        assert raw[oc:e['start']]==changed[nc:nc+length]
        intervals.append(dict(old_start=oc,old_end=e['start'],new_start=nc,new_end=nc+length,sha256=sha(raw[oc:e['start']])))
        oc=e['end']; nc+=length+len(e['new'].encode())
    assert raw[oc:]==changed[nc:]
    intervals.append(dict(old_start=oc,old_end=len(raw),new_start=nc,new_end=len(changed),sha256=sha(raw[oc:])))
    new_source=changed.decode(); new_tree=ast.parse(new_source)
    new_nodes={p:n for n,p in paths(new_tree,'Module')}
    for e in ordered: assert ast.get_source_segment(new_source,new_nodes[e['path']])==e['new']
    for name,expected in [('INDICES',(43,44,45,46)),('steps',old_steps+(468,470)),('transition_paths',new_transitions)]:
        n,_=assignment(new_tree.body,name,'Module.body'); assert ast.literal_eval(n.value)==expected
    n,_=assignment(new_tree.body,'selected','Module.body')
    assert ast.literal_eval(n.value.left)==new_selected
    assert len(new_transitions)==22 and new_transitions[:20]==old_transitions
    assert not (BASE/'step-472').exists()
    for rel in new_selected+new_transitions:
        if rel.startswith('scripts/four-rational-kernels/step-472-prelaunch/'): continue
        assert (ROOT/rel).is_file(),('selected_file_exists',rel)
    compile(new_source,str(OUT/'coordinator.py'),'exec',flags=0,dont_inherit=True,optimize=0)
    worker_raw=(BASE/'step-468/worker.py').read_bytes()
    assert len(worker_raw)==5789 and sha(worker_raw)=='edb68bad705810bd9d3d1d8655b42a12165602e214e1713fac1323badd4e53ea'
    worker=worker_raw.decode()
    for old,new in worker_changes:
        assert worker.count(old)==1; worker=worker.replace(old,new,1)
    compile(worker,str(OUT/'worker-expected.py'),'exec',flags=0,dont_inherit=True,optimize=0)
    (OUT/'coordinator.py').write_bytes(changed)
    (OUT/'worker-expected.py').write_text(worker)
    (OUT/'coordinator-source-diff.txt').write_text(''.join(difflib.unified_diff(source.splitlines(True),new_source.splitlines(True),fromfile='step-468/coordinator.py',tofile='step-472/coordinator.py')))
    save('edit-map.json',dict(old_sha256=sha(raw),new_sha256=sha(changed),edits=ordered,untouched_intervals=intervals))
    save('verification.json',dict(status='PASS',unique_structural_roles=True,complete_old_bytes_pinned=True,
        disjoint_spans=True,untouched_intervals_equal=True,all_new_structural_values_equal=True,compile_optimize=0,
        coordinator_sha256=sha(changed),worker_sha256=sha(worker.encode()),edits=19,suffixes=22,
        execution_started=False,prelaunch_outside_unstarted_cap=True))
    print(json.dumps(dict(status='PASS',edits=19,suffixes=22,path=str(OUT.relative_to(ROOT)))))
except BaseException as exc:
    save('first-failure.json',dict(status='STOP',type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc(),execution_started=False,edits_constructed=edits))
    print(json.dumps(dict(status='STOP',error=str(exc),execution_started=False,path=str(OUT.relative_to(ROOT)))))
    sys.exit(1)
