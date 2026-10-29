"""One-shot prelaunch byte-splice construction; never runs arithmetic."""
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
OUT = BASE / 'step-468-prelaunch'
OUT.mkdir()
edits = []

def save(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

try:
    raw = (BASE / 'step-461/coordinator.py').read_bytes()
    assert sha(raw) == 'ed7b021281df11e29bdab0b640fdc8feb62e1f7e916761915569a05cb436891c'
    source = raw.decode('utf-8')
    assert source.encode('utf-8') == raw
    lines = raw.splitlines(keepends=True)
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line))
    tree = ast.parse(source)

    def one(values, role):
        assert len(values) == 1, ('unique_role', role, len(values))
        return values[0]

    def assignment(body, name, path):
        return one([(n, f'{path}[{i}]') for i, n in enumerate(body)
                    if isinstance(n, ast.Assign) and
                    any(isinstance(t, ast.Name) and t.id == name for t in n.targets)], name)

    def segment(node):
        start = offsets[node.lineno - 1] + node.col_offset
        end = offsets[node.end_lineno - 1] + node.end_col_offset
        return start, end, raw[start:end]

    def change(node, path, role, new, owner):
        start, end, old = segment(node)
        assert old.decode('utf-8') == ast.get_source_segment(source, node)
        owner_start, owner_end, owner_old = segment(owner)
        assert owner_start <= start < end <= owner_end
        edits.append({'role': role, 'path': path, 'start': start, 'end': end,
                      'old': old.decode('utf-8'), 'new': new,
                      'owner_start': owner_start, 'owner_end': owner_end,
                      'complete_original_owner': owner_old.decode('utf-8')})

    def paths(node, path):
        yield node, path
        for field, value in ast.iter_fields(node):
            if isinstance(value, ast.AST):
                yield from paths(value, path + '.' + field)
            elif isinstance(value, list):
                for i, child in enumerate(value):
                    if isinstance(child, ast.AST):
                        yield from paths(child, f'{path}.{field}[{i}]')

    def constant_changes(owner, path, old, new, count, role):
        matches = [(n, p) for n, p in paths(owner, path)
                   if isinstance(n, ast.Constant) and n.value == old]
        assert len(matches) == count, ('constant_role_count', role, len(matches), count)
        for n, p in matches:
            change(n, p, role, repr(new), owner)

    node, path = assignment(tree.body, 'OUT', 'Module.body')
    assert node.lineno == 6
    constant_changes(node, path, 'step-461', 'step-468', 1, 'exclusive_destination')
    node, path = assignment(tree.body, 'INDICES', 'Module.body')
    assert ast.literal_eval(node.value) == (35, 36, 37, 38)
    change(node.value, path + '.value', 'indices', '(39,40,41,42)', node)
    node, path = assignment(tree.body, 'steps', 'Module.body')
    old_steps = ast.literal_eval(node.value)
    assert old_steps == (417,419,422,424,429,431,433,435,437,440,442,446,449,451,453,455,457,459)
    change(node.value, path + '.value', 'historical_steps', repr(old_steps + (461,463)), node)
    node, path = assignment(tree.body, 'roots', 'Module.body')
    old_roots = segment(node.value)[2].decode()
    roots_tuple = '(417,419,422,424,426,429,431,433,435,437,440,442,444,446,449,451,453,455,457,459)'
    assert old_roots.count(roots_tuple) == 1
    new_roots = old_roots.replace(roots_tuple, roots_tuple[:-1] + ',461,463)', 1)
    new_roots += "+[BASE/'step-465-postmortem']"
    change(node.value, path + '.value', 'frozen_roots', new_roots, node)
    node, path = assignment(tree.body, 'transition_paths', 'Module.body')
    old_transitions = ast.literal_eval(node.value)
    assert len(old_transitions) == 18
    new_transitions = old_transitions + [
        'drafts/2026-10-24-kernels-thirty-five-through-thirty-eight-document-transition.json',
        'drafts/2026-10-24-l113-audit-document-transition.json']
    change(node.value, path + '.value', 'twenty_transition_suffixes', repr(new_transitions), node)
    node, path = assignment(tree.body, 'selected', 'Module.body')
    assert isinstance(node.value, ast.BinOp) and isinstance(node.value.op, ast.Add)
    assert isinstance(node.value.right, ast.Name) and node.value.right.id == 'transition_paths'
    old_selected = ast.literal_eval(node.value.left)
    assert old_selected[0] == 'lemmas/L112-kernels-thirty-one-through-thirty-four-certificates.md'
    additions = [
        'drafts/literature/2026-10-24-kernels-thirty-nine-through-forty-two.md',
        'drafts/source-notes/2026-10-24-kernels-thirty-nine-through-forty-two-coverage.md',
        'drafts/2026-10-24-n39-42-source-metadata.json',
        'drafts/literature/2026-10-25-kernels-thirty-nine-through-forty-two-parsed-adapter.md',
        'drafts/source-notes/2026-10-25-parsed-coordinator-interface-review.md',
        'drafts/2026-10-25-kernels-thirty-nine-through-forty-two-attempt.md',
        'ATTEMPTS/051-coordinator-if-elif-substring-stop.md',
        'history/465-2026-10-25-n39-42-adapter-stop.md',
        'history/466-2026-10-25-parsed-adapter-interface-review.md',
        'history/467-2026-10-25-direct-source-field-recovery.md',
        'drafts/2026-10-25-n39-42-parsed-attempt.md',
        'scripts/four-rational-kernels/build-parsed-468.py',
        'scripts/four-rational-kernels/step-468-prelaunch/edit-map.json',
        'scripts/four-rational-kernels/step-468-prelaunch/coordinator-source-diff.txt',
        'scripts/four-rational-kernels/step-468-prelaunch/verification.json',
        'scripts/four-rational-kernels/step-468-prelaunch/coordinator.py',
        'scripts/four-rational-kernels/step-468-prelaunch/worker-expected.py']
    new_selected = ['lemmas/L113-kernels-thirty-five-through-thirty-eight-certificates.md'] + old_selected[1:] + additions
    assert new_selected[1:len(old_selected)] == old_selected[1:]
    assert len(new_selected) == len(set(new_selected))
    change(node.value.left, path + '.value.left', 'selected_inputs', repr(new_selected), node)

    outer, outer_path = one([(n, f'Module.body[{i}]') for i, n in enumerate(tree.body)
                             if isinstance(n, ast.Try)], 'production_try')
    report_loop, report_path = one([(n, f'{outer_path}.body[{i}]') for i, n in enumerate(outer.body)
                                   if isinstance(n, ast.For) and isinstance(n.target, ast.Name)
                                   and n.target.id == 'step' and isinstance(n.iter, ast.Name)
                                   and n.iter.id == 'steps'], 'historical_report_loop')
    assert report_loop.lineno == 103
    old_membership = 'step in (446,449,451,453,455,457,459)'
    new_membership = 'step in (446,449,451,453,455,457,459,461,463)'
    preservation_if, preservation_path = one([(n, f'{report_path}.body[{i}]') for i, n in enumerate(report_loop.body)
        if isinstance(n, ast.If) and ast.get_source_segment(source, n.test) == old_membership], 'direct_preservation_if')
    assert preservation_if.lineno == 108 and len(preservation_if.body) == 1
    change(preservation_if.test, preservation_path + '.test', 'preservation_branch', new_membership, preservation_if)
    dispatch_owner, dispatch_path = one([(n, f'{report_path}.body[{i}]') for i, n in enumerate(report_loop.body)
        if isinstance(n, ast.If) and ast.get_source_segment(source, n.test) == 'step>=424'], 'report_dispatch_owner')
    branch, branch_path = one([(n, f'{dispatch_path}.body[{i}]') for i, n in enumerate(dispatch_owner.body)
        if isinstance(n, ast.If)], 'report_dispatch_head')
    for expected in ('step==424', 'step==429', 'step in (431,435,440)', 'step==442'):
        assert ast.get_source_segment(source, branch.test) == expected
        assert len(branch.orelse) == 1 and isinstance(branch.orelse[0], ast.If)
        branch = branch.orelse[0]
        branch_path += '.orelse[0]'
    assert ast.get_source_segment(source, branch.test) == old_membership and branch.lineno == 125
    change(branch.test, branch_path + '.test', 'original_report_dispatch_tail', new_membership, branch)
    source_loop, source_loop_path = one([(n, f'{outer_path}.body[{i}]') for i, n in enumerate(outer.body)
        if isinstance(n, ast.For) and isinstance(n.target, ast.Name) and n.target.id == 'step'
        and isinstance(n.iter, ast.Tuple)], 'source_map_loop')
    assert source_loop.lineno == 129
    old_maps = ast.literal_eval(source_loop.iter)
    assert old_maps == (417,419,422,424,431,433,435,437,440,442,446,449,451,453,455,457,459)
    change(source_loop.iter, source_loop_path + '.iter', 'source_map_steps', repr(old_maps + (461,463)), source_loop)
    f, fp = assignment(source_loop.body, 'f', source_loop_path + '.body')
    assert isinstance(f.value, ast.IfExp)
    assert ast.get_source_segment(source, f.value.test) == 'step in (417,424,431,435,440,449,453,457)'
    change(f.value.test, fp + '.value.test', 'whole_source_map_dispatch', 'step in (417,424,431,435,440,449,453,457,461)', f)

    # Select complete owning statements within this try, then exact literal fields.
    expressions = [(n, f'{outer_path}.body[{i}]') for i, n in enumerate(outer.body) if isinstance(n, ast.Expr)]
    coord_diff, coord_path = one([(n,p) for n,p in expressions if n.lineno == 141], 'coordinator_diff_call')
    constant_changes(coord_diff, coord_path, 'step-457/coordinator.py', 'step-461/coordinator.py', 2, 'coordinator_diff_predecessor')
    constant_changes(coord_diff, coord_path, 'step-461/coordinator.py', 'step-468/coordinator.py', 1, 'coordinator_diff_destination')
    manifest, manifest_path = one([(n,p) for n,p in expressions if n.lineno == 142], 'manifest_save_call')
    constant_changes(manifest, manifest_path, 'BSD-2026-10-24-461-kernels-thirty-five-through-thirty-eight',
                     'BSD-2026-10-25-468-kernels-thirty-nine-through-forty-two-parsed', 1, 'manifest_step')
    wb, wp = assignment(outer.body, 'worker_before', outer_path + '.body')
    assert wb.lineno == 150
    constant_changes(wb, wp, 'step-457/worker.py', 'step-461/worker.py', 1, 'worker_predecessor')
    wc, wcp = assignment(outer.body, 'worker_changes', outer_path + '.body')
    assert ast.literal_eval(wc.value) == [('assert INDEX in (31,32,33,34)', 'assert INDEX in (35,36,37,38)'), ("'kernel_457_'", "'kernel_461_'")]
    new_worker_changes = [('assert INDEX in (35,36,37,38)', 'assert INDEX in (39,40,41,42)'), ("'kernel_461_'", "'kernel_468_'")]
    change(wc.value, wcp + '.value', 'two_whole_worker_substitutions', repr(new_worker_changes), wc)
    worker_diff, worker_diff_path = one([(n,p) for n,p in expressions if n.lineno == 156], 'worker_diff_call')
    constant_changes(worker_diff, worker_diff_path, 'step-457/worker.py', 'step-461/worker.py', 1, 'worker_diff_predecessor')
    constant_changes(worker_diff, worker_diff_path, 'step-461/worker.py', 'step-468/worker.py', 1, 'worker_diff_destination')
    production, production_path = one([(n, f'{outer_path}.body[{i}]') for i,n in enumerate(outer.body)
        if isinstance(n, ast.For) and isinstance(n.iter, ast.Name) and n.iter.id == 'INDICES'], 'production_loop')
    repl, repl_path = one([(n, f'{production_path}.body[{i}]') for i,n in enumerate(production.body)
        if isinstance(n, ast.Assign) and any(isinstance(t,ast.Name) and t.id=='repl' for t in n.targets)
        and isinstance(n.value, ast.DictComp)], 'replacement_value_binding')
    assert repl.lineno == 170
    constant_changes(repl, repl_path, 'step-461', 'step-468', 1, 'arithmetic_replacement_destination_only')

    ordered = sorted(edits, key=lambda e:e['start'])
    assert len(ordered) == 19
    for left, right in zip(ordered, ordered[1:]):
        assert left['end'] <= right['start'], ('disjoint_edits', left['role'], right['role'])
    changed = raw
    for entry in reversed(ordered):
        a,b = entry['start'],entry['end']
        assert changed[a:b] == entry['old'].encode()
        changed = changed[:a] + entry['new'].encode() + changed[b:]
    intervals = []
    old_cursor = new_cursor = 0
    for entry in ordered:
        length = entry['start']-old_cursor
        assert raw[old_cursor:entry['start']] == changed[new_cursor:new_cursor+length]
        intervals.append({'old_start':old_cursor,'old_end':entry['start'],
                          'new_start':new_cursor,'new_end':new_cursor+length,
                          'sha256':sha(raw[old_cursor:entry['start']])})
        new_cursor += length + len(entry['new'].encode())
        old_cursor = entry['end']
    assert raw[old_cursor:] == changed[new_cursor:]
    intervals.append({'old_start':old_cursor,'old_end':len(raw),'new_start':new_cursor,
                      'new_end':len(changed),'sha256':sha(raw[old_cursor:])})
    new_source = changed.decode('utf-8')
    new_tree = ast.parse(new_source)
    # Resolve every saved structural path in the new tree and check its new value.
    new_nodes = dict((p,n) for n,p in paths(new_tree, 'Module'))
    for entry in ordered:
        assert ast.get_source_segment(new_source, new_nodes[entry['path']]) == entry['new']
    for name, expected in [('INDICES',(39,40,41,42)),('steps',old_steps+(461,463)),('transition_paths',new_transitions)]:
        n,_ = assignment(new_tree.body,name,'Module.body')
        assert ast.literal_eval(n.value) == expected
    n,_ = assignment(new_tree.body,'selected','Module.body')
    assert ast.literal_eval(n.value.left) == new_selected
    assert len(new_transitions) == 20 and new_transitions[:18] == old_transitions
    assert not (BASE/'step-468').exists()
    for rel in new_selected + new_transitions:
        if rel.startswith('scripts/four-rational-kernels/step-468-prelaunch/'):
            continue
        assert (ROOT/rel).is_file(), ('selected_file_exists',rel)
    compile(new_source, str(OUT/'coordinator.py'),'exec',flags=0,dont_inherit=True,optimize=0)
    worker_raw = (BASE/'step-461/worker.py').read_bytes()
    assert sha(worker_raw) == '628f7f9dbb42289e16d906b90e0f1f11b1b21d08be58273e34f8e6d8739c6e56'
    worker = worker_raw.decode()
    for old,new in new_worker_changes:
        assert worker.count(old) == 1
        worker = worker.replace(old,new,1)
    compile(worker,str(OUT/'worker-expected.py'),'exec',flags=0,dont_inherit=True,optimize=0)
    (OUT/'coordinator.py').write_bytes(changed)
    (OUT/'worker-expected.py').write_text(worker)
    (OUT/'coordinator-source-diff.txt').write_text(''.join(difflib.unified_diff(source.splitlines(True),new_source.splitlines(True),fromfile='step-461/coordinator.py',tofile='step-468/coordinator.py')))
    save('edit-map.json', {'old_sha256':sha(raw),'new_sha256':sha(changed),'edits':ordered,'untouched_intervals':intervals})
    save('verification.json', {'status':'PASS','unique_structural_roles':True,'complete_old_bytes_pinned':True,
        'disjoint_spans':True,'untouched_intervals_equal':True,'all_new_structural_values_equal':True,
        'compile_optimize':0,'coordinator_sha256':sha(changed),'worker_sha256':sha(worker.encode()),
        'edits':len(ordered),'suffixes':len(new_transitions),'execution_started':False,
        'prelaunch_outside_unstarted_cap':True})
    print(json.dumps({'status':'PASS','edits':len(ordered),'suffixes':20,'path':str(OUT.relative_to(ROOT))}))
except BaseException as exc:
    save('first-failure.json', {'status':'STOP','type':type(exc).__name__,'message':str(exc),
                              'traceback':traceback.format_exc(),'execution_started':False,
                              'edits_constructed':edits})
    print(json.dumps({'status':'STOP','error':str(exc),'execution_started':False,'path':str(OUT.relative_to(ROOT))}))
    sys.exit(1)
