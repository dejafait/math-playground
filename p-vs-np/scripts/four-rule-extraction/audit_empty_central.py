"""Step 483: bounded finite audit of the saved step-481 run. No production edits.

Run without arguments once in a fresh output-483 directory. Child processes
separate emitter and receiver import environments. Full comparisons, not hash
previews, establish replay equality; hashes only retain preservation evidence.
"""
import ast
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OLD = HERE / 'output-481'
OUT = HERE / 'output-483'
RUN = OUT / 'replay'


def save(path, value):
    path.write_text(json.dumps(value, separators=(',', ':'))+'\n')


def manifest(folder):
    return {str(p.relative_to(folder)): dict(bytes=p.stat().st_size,
            sha256=hashlib.sha256(p.read_bytes()).hexdigest())
            for p in sorted(folder.rglob('*')) if p.is_file()}


def instrument(module, folder, report):
    """Inspect exact install then transparently delegate every captured write."""
    import parameterized_input as inputs
    original = inputs.write_json
    before = [name for name,m in list(sys.modules.items())
              if m is not None and getattr(m,'write_json',None) is original]
    writer = module.install_evidence_budget(folder)
    assert all(getattr(sys.modules[name],'write_json') is writer for name in before)
    calls = []
    def observed(path, value, key='certificate_bytes'):
        result = writer(path,value,key)
        p = Path(path)
        assert result == p.stat().st_size
        assert p.read_bytes().endswith(b'\n')
        calls.append(dict(path=str(p.relative_to(folder)),key=key,bytes=result,
                          caller=sys._getframe(1).f_globals.get('__name__')))
        return result
    for m in list(sys.modules.values()):
        if m is not None and getattr(m,'write_json',None) is writer:
            m.write_json = observed
    # report is retained outside the measured replay folder.
    def finish():
        save(report,dict(aliases=before,calls=calls,
                         all_initial_aliases_rebound=True,
                         remaining_old_aliases=[name for name,m in list(sys.modules.items())
                         if m is not None and getattr(m,'write_json',None) is original]))
    return observed, finish


def emit():
    import run_empty_central_occurrence as runner
    import receive_selected_commutator as selection
    # Alter exactly one path literal in memory; all other AST nodes are intact.
    tree = ast.parse(Path(runner.__file__).read_text())
    hits = [n for n in ast.walk(tree) if isinstance(n,ast.Constant) and n.value=='output-481']
    assert len(hits)==1
    hits[0].value='output-483/replay'
    ns = dict(__file__=runner.__file__,__name__='audit_relocated_runner')
    exec(compile(tree,runner.__file__,'exec'),ns)
    finishes=[]
    def install(folder):
        assert folder==RUN
        writer,finish=instrument(selection,folder,OUT/'emitter-writes.json')
        finishes.append(finish)
        return writer
    ns['install_evidence_budget']=install
    ns['main']()
    assert len(finishes)==1
    finishes[0]()
    assert not (RUN/'failure.json').exists()
    # All outputs are compared including complete trace graphs and K/H bytes.
    results=[]
    for p in sorted(RUN.rglob('*')):
        if not p.is_file(): continue
        rel=p.relative_to(RUN); prior=OLD/rel
        assert prior.is_file(), str(rel)
        raw=p.read_bytes(); expected=prior.read_bytes()
        if str(rel) in ('emission.json','emitted/construction.json'):
            raw=raw.replace(str(RUN).encode(),str(OLD).encode())
        assert raw==expected, str(rel)
        results.append(str(rel))
    save(OUT/'emission-comparison.json',dict(files=results,complete_equal=True,
        sole_normalization='absolute output path in two construction receipts'))


def receive():
    import verify_empty_central_occurrence as audit
    import receive_selected_commutator as selection
    import receive_occurrence as production
    import parameterized_input as inputs
    # No constructor is loaded in this process.
    assert not any(name in sys.modules for name in
        ('emit_parameterized','emit_occurrence','empty_central_translation','constant_translation'))
    audit.OUT=audit.base.OUT=RUN
    audit.base.Reception=audit.Reception
    writer,finish=instrument(selection,RUN,OUT/'receiver-writes.json')
    paths={k:RUN/'inputs'/(k+('.jsonl' if k=='proof' else '.json'))
           for k in ('manifest','source','annotations','pair','proof','request')}
    fresh=production.receive(**paths,K=RUN/'emitted/K.json',H=RUN/'emitted/H.json')
    # The public result contains tuples inside serial(word); receive the actual
    # wire JSON before exact typed comparison with a parsed saved certificate.
    # Initial receive.log preserves the failed pre-serialization comparison.
    writer(RUN/'reception.json',fresh)
    assert (RUN/'reception.json').read_bytes()==(OLD/'reception.json').read_bytes()
    audit.base.main()
    finish()
    result=[]
    for p in [RUN/'integration-reception.json',RUN/'trace-received-prefix.json',
              *sorted((RUN/'references').glob('*.json'))]:
        rel=p.relative_to(RUN)
        assert p.read_bytes()==(OLD/rel).read_bytes(),str(rel)
        result.append(str(rel))
    assert len(list((RUN/'references').glob('*.json')))==206
    save(OUT/'reception-comparison.json',dict(files=result,complete_equal=True,
        production_full_receipt_equal=True,emitter_modules_loaded=False))


def finish():
    before=json.loads((OUT/'preservation-before.json').read_text())
    assert manifest(OLD)==before
    summary=json.loads((OLD/'bounds-and-scope.json').read_text())
    sizes={p:v['bytes'] for p,v in before.items() if p!='bounds-and-scope.json'}
    assert sizes==summary['final_files']
    assert sum(sizes.values())==summary['evidence_bytes_before_summary']
    assert sum(v['bytes'] for v in before.values())==49491927
    receipt=json.loads((RUN/'integration-reception.json').read_text())
    assert receipt['events']==529 and receipt['K_blocks']==64
    assert receipt['source']['records']==31
    assert receipt['accepted'] and receipt['complete_KH_received'] and not receipt['failures']
    import parameterized_input as inputs
    from receive_parameterized import serial
    in_memory=serial({(('original',0),)})
    wire=inputs.parse(json.dumps(in_memory))
    assert type(in_memory[0][0]) is tuple and type(wire[0][0]) is list
    assert not inputs.exact_equal(in_memory,wire)
    assert inputs.exact_equal(inputs.parse(json.dumps(in_memory)),wire)
    save(OUT/'comparison-boundary.json',dict(
        in_memory_symbol_type='tuple',wire_symbol_type='list',wire=wire,
        direct_typed_comparison=False,serialized_typed_comparison=True,
        original_failure='receive.log and audit-failure.json (first run only)',
        correction='serialize the entire result before comparing complete wire bytes'))
    boundary=inputs.load(HERE/'output-468/module-review.json')
    source_checks={}
    for name,item in boundary['pinned_baselines_and_dependencies'].items():
        # The two changed boundary files have their post-change hashes below.
        if item['path']!=name: continue
        actual=hashlib.sha256((HERE.parents[1]/name).read_bytes()).hexdigest()
        assert actual==item['sha256']
        source_checks[name]=actual
    for name,recorded in inputs.load(HERE/'output-466/verification.json')['scripts'].items():
        actual=hashlib.sha256((HERE.parents[1]/name).read_bytes()).hexdigest()
        assert actual==recorded
        source_checks[name]=actual
    for name,item in boundary['occurrence_hashes'].items():
        actual=hashlib.sha256((HERE/name).read_bytes()).hexdigest()
        assert actual==item['actual']==item['snapshot']==item['recorded']
        source_checks[name]=actual
    save(OUT/'audited-dependency-preservation.json',source_checks)
    isolated=HERE/'output-479'
    old_input=inputs.load(isolated/'inputs.json')
    event=inputs.load(RUN/'trace/event-00219.json')
    for key,value in old_input['original_event'].items():
        assert inputs.exact_equal(event[key],value),key
    assert inputs.exact_equal(old_input['parent'],inputs.load(RUN/'trace/event-00196.json'))
    candidate=inputs.load(isolated/'candidate.json')
    output=inputs.load(RUN/'trace/event-00220.json')
    for key in ('graph','branches'):
        assert inputs.exact_equal(candidate[key],output[key]),key
    inventory=inputs.load(isolated/'inventory.json')
    assert inputs.exact_equal(inventory['pairs'],event['inventory'])
    assert (isolated/'reference.json').read_bytes()==(RUN/'references/event-00219.json').read_bytes()
    previous=inputs.load(isolated/'reception.json')
    assert previous['accepted'] and not previous['failures']
    units=inputs.load(OUT/'units/verification.json')
    assert units['accepted'] and not units['failures']
    # The in-memory runner namespace is outside sys.modules: its two direct
    # writes use the unchanged per-file writer. Actual registered runner aliases
    # are separately tested by units/writer-tests.json. Full file equality and
    # final aggregate enumeration cover the relocated replay's two writes.
    emitter_io=inputs.load(OUT/'emitter-writes.json')
    actual_calls={item['path'] for item in emitter_io['calls']}
    save(OUT/'replay-io-qualification.json',dict(
        registered_original_runner_alias_test='units/writer-tests.json',
        relocated_namespace_writes=['run-scope.json','trace-summary.json'],
        reason='in-memory exec namespace is not a sys.modules entry',
        per_file_guards_unchanged=True,final_aggregate_verified=True,
        captured_emitter_paths=sorted(actual_calls)))
    result=dict(accepted=True,failures=[],preserved_files=len(before),
        original_evidence_bytes=sum(v['bytes'] for v in before.values()),
        required_evidence_bytes=200000000,events=receipt['events'],
        statistics=receipt['statistics'],K_bounds=receipt['K_bounds'],H_bounds=receipt['H_bounds'],
        arithmetic={k:receipt[k] for k in ('trace_arithmetic','K_arithmetic','correction_arithmetic','H_arithmetic')},
        isolated_event_219_complete_match=True,focused_units=units,
        audit_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        qualifications=['finite same-caller audit','f=0 does not test nonzero fJ',
                        'trusted paths and remaining SHA bindings',
                        'not total interpreter time, memory or peak temporary disk'])
    existing_bytes=sum(p.stat().st_size for p in OUT.rglob('*')
                       if p.is_file() and p!=OUT/'verification.json')
    result['audit_evidence_bytes']=0
    while True:
        total=existing_bytes+len((json.dumps(result,separators=(',',':'))+'\n').encode())
        if total==result['audit_evidence_bytes']:break
        result['audit_evidence_bytes']=total
    assert total<=inputs.CAPS['certificate_bytes']
    save(OUT/'verification.json',result)
    print(dict(accepted=True,events=529,K=receipt['K_bounds'],H=receipt['H_bounds'],
               audit_evidence_bytes=total,required_bytes=inputs.CAPS['certificate_bytes'],
               failures=[],path=str(OUT/'verification.json')),flush=True)


def units():
    subprocess.run([sys.executable,str(HERE/'audit_empty_central_units.py')],check=True)


def main():
    if len(sys.argv)>1:
        {'emit':emit,'receive':receive,'units':units,'finish':finish}[sys.argv[1]]()
        return
    OUT.mkdir(exist_ok=False)
    save(OUT/'preservation-before.json',manifest(OLD))
    save(OUT/'started.json',dict(status='IN_PROGRESS',target='step-481 finite critical audit',
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()))
    for stage in ('emit','units','receive','finish'):
        with (OUT/(stage+'.log')).open('w') as log:
            completed=subprocess.run([sys.executable,__file__,stage],stdout=log,stderr=subprocess.STDOUT)
        if completed.returncode:
            save(OUT/'audit-failure.json',dict(stage=stage,returncode=completed.returncode,
                                             evidence=stage+'.log'))
            raise RuntimeError('audit stage failed: '+stage)
        print(dict(stage=stage,completed=True,evidence=str(OUT/(stage+'.log'))),flush=True)


if __name__=='__main__':
    main()
