
import copy,hashlib,importlib.util,json,sys,time,traceback
from fractions import Fraction
from pathlib import Path
sys.dont_write_bytecode=True
INDEX=int(sys.argv[1]); OUT=Path(sys.argv[2]).resolve(); START=float(sys.argv[3])
assert sys.flags.optimize==0
assert INDEX in (35,36,37,38) and OUT.name=='n-'+str(INDEX)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
IDENTITY=(INDEX,str(OUT),'kernel_461_'+str(INDEX),sha(OUT/'producer.py'),sha(OUT/'replay.py'))
state={'n':IDENTITY[0],'stage':'setup','panels':0}
def save(name,obj):
    (OUT/name).write_text(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n')
def progress(stage,panels):
    state.update(stage=stage,panels=panels)
    assert time.monotonic()-START<174,'aggregate_work_deadline'
    assert sum(p.stat().st_size for p in OUT.parent.rglob('*') if p.is_file())+73728<=134217728
    save('working.json',{**state,'elapsed_seconds':time.monotonic()-START})
def load(name):
    spec=importlib.util.spec_from_file_location(IDENTITY[2]+'_'+name,OUT/(name+'.py'))
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod
def check_identity(producer,replay):
    assert IDENTITY[0]==INDEX and IDENTITY[1]==str(OUT) and OUT.name=='n-'+str(IDENTITY[0])
    for name,mod,expected in (('producer',producer,IDENTITY[3]),('replay',replay,IDENTITY[4])):
        assert mod.__name__==IDENTITY[2]+'_'+name
        assert Path(mod.__file__).resolve()==OUT/(name+'.py')
        assert sha(OUT/(name+'.py'))==expected
    assert producer.D==replay.SCALE==2**256
try:
    for name in ('producer','replay'):
        compile((OUT/(name+'.py')).read_text(),str(OUT/(name+'.py')),'exec',flags=0,dont_inherit=True,optimize=0)
    producer=load('producer'); replay=load('replay'); modules=(producer,replay)
    check_identity(*modules)
    save('identity-before.json',{'identity':IDENTITY})
    parameter=producer.parameter()
    fixed=json.loads(Path('scripts/first-rational-kernel/step-404/parameter.json').read_text())
    assert json.loads(json.dumps(parameter))==fixed,'complete_unchanged_parameter'
    assert parameter['midpoint']==[73775804382331484748893662180180200545104154546089041648426948815067512948607,2**257]
    save('parameter.json',parameter)
    save('parameter-identity.json',{'n':IDENTITY[0],'complete_record_equal':True,'midpoint_unchanged':True})
    progress('production',0)
    with (OUT/'panels.jsonl').open('x') as handle:
        def emit(record):
            assert record['n']==IDENTITY[0]
            raw=json.dumps(record,separators=(',',':'))+'\n'
            assert len(raw.encode())<=4096
            handle.write(raw); handle.flush()
        kernel=producer.run(parameter,emit,progress)
    kernel=copy.deepcopy(kernel)
    save('kernel.json',kernel)
    producer_ledger=copy.deepcopy(producer.COUNTS)
    save('producer-ledger.json',{'n':IDENTITY[0],'counts':producer_ledger})
    assert kernel['n']==IDENTITY[0] and kernel['counts']==producer_ledger
    check_identity(*modules)
    save('identity-after-production.json',{'identity':IDENTITY})
    progress('replay',0)
    with (OUT/'panels.jsonl').open() as handle:
        returned=replay.run(json.loads((OUT/'parameter.json').read_text()),
            (json.loads(line) for line in handle),json.loads((OUT/'kernel.json').read_text()),progress)
    returned=copy.deepcopy(returned)
    save('returned-report.json',returned)
    replay_ledger=copy.deepcopy(replay.LEDGER)
    save('replay-ledger.json',{'n':IDENTITY[0],'counts':replay_ledger})
    check_identity(*modules)
    save('identity-after-replay.json',{'identity':IDENTITY})
    assert 'n' not in returned
    report={**returned,'n':IDENTITY[0]}
    save('replay.json',report)
    assert json.loads((OUT/'returned-report.json').read_text())==returned
    assert json.loads((OUT/'replay.json').read_text())=={**returned,'n':IDENTITY[0]}
    expected={'add':21787232,'clip':24386,'coefficient_pairs':21264880,'convert':5083,
        'divide':716408,'enlarge':2034,'multiply':21801456,'negate':356616,'scale':2033}
    assert json.loads((OUT/'producer-ledger.json').read_text())=={'n':IDENTITY[0],'counts':producer_ledger}
    assert json.loads((OUT/'replay-ledger.json').read_text())=={'n':IDENTITY[0],'counts':replay_ledger}
    expected_report={'status':'PASS','parameter':'complete exact reconstruction','panels':1016,'coefficient_pairs':21264880,'counts':expected,'radius':kernel['radius'],'all_stage_comparisons':'PASS','signed_rounding_checks':'every conversion, multiplication and division','originals_preserved':'checked by aggregate runner'}
    assert returned==expected_report
    assert returned['counts']==kernel['counts']==producer_ledger==replay_ledger==expected
    assert returned['panels']==kernel['complete_panels']==1016
    assert returned['coefficient_pairs']==21264880
    assert returned['radius']==kernel['radius']
    radius=Fraction(*kernel['radius'])
    assert radius<Fraction(1,2**183) and radius<Fraction(1,2**50)
    assert kernel['final_grid']==[kernel['polynomial_sum'][0]-2**72,kernel['polynomial_sum'][1]+2**72]
    save('status.json',{'status':'PASS','n':IDENTITY[0],'panels':1016,'pairs_per_pass':21264880,
        'parameter_complete_equal':True,'ledger_equal':True,'identity_unchanged':True,
        'full_returned_report_persisted':True,'strict_radius_tests':[183,50],
        'radius':kernel['radius'],'elapsed_seconds':time.monotonic()-START})
    print(json.dumps({'n':IDENTITY[0],'status':'PASS','radius':kernel['radius']}),flush=True)
except BaseException as exc:
    save('first-failure.json',{'type':type(exc).__name__,'message':str(exc),'state':state,'traceback':traceback.format_exc()})
    print(json.dumps({'n':IDENTITY[0],'status':'STOP','state':state,'error':str(exc)}),flush=True)
    sys.exit(1)
