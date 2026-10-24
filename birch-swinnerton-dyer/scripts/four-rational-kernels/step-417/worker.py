
import importlib.util,json,sys,time,traceback
from pathlib import Path
from fractions import Fraction
sys.dont_write_bytecode=True
n=int(sys.argv[1]); out=Path(sys.argv[2]); start=float(sys.argv[3])
state={'n':n,'stage':'setup','panels':0}
def save(name,value):
    (out/name).write_text(json.dumps(value,sort_keys=True,separators=(',',':'))+'\n')
def progress(stage,panels):
    state.update(stage=stage,panels=panels)
    assert time.monotonic()-start<174,'aggregate_work_deadline'
    save('working.json',{**state,'elapsed_seconds':time.monotonic()-start})
def load(name):
    spec=importlib.util.spec_from_file_location('kernel_'+str(n)+'_'+name,out/(name+'.py'))
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
try:
    producer=load('producer'); replay=load('replay')
    parameter=producer.parameter()
    fixed=json.loads(Path('scripts/first-rational-kernel/step-404/parameter.json').read_text())
    normalized=json.loads(json.dumps(parameter))
    assert normalized==fixed,'complete_unchanged_parameter'
    assert parameter['midpoint']==[73775804382331484748893662180180200545104154546089041648426948815067512948607,2**257]
    save('parameter.json',parameter)
    save('parameter-identity.json',{'n':n,'complete_record_equal':True,'midpoint_unchanged':True})
    progress('production',0)
    with (out/'panels.jsonl').open('x') as handle:
        def emit(record):
            assert record['n']==n
            handle.write(json.dumps(record,separators=(',',':'))+'\n')
            handle.flush()
        kernel=producer.run(parameter,emit,progress)
    assert kernel['n']==n and kernel['counts']['coefficient_pairs']==21264880
    kernel['counts']=dict(kernel['counts'])
    save('kernel.json',kernel)
    save('producer-ledger.json',{'n':n,'counts':dict(producer.COUNTS)})
    progress('replay',0)
    with (out/'panels.jsonl').open() as handle:
        report=replay.run(json.loads((out/'parameter.json').read_text()),
            (json.loads(line) for line in handle),json.loads((out/'kernel.json').read_text()),progress)
    report['n']=n; report['counts']=dict(report['counts'])
    assert report['counts']==kernel['counts']==replay.LEDGER
    assert report['panels']==1016 and report['coefficient_pairs']==21264880
    radius=Fraction(*kernel['radius'])
    assert radius<Fraction(1,2**183) and radius<Fraction(1,2**50)
    assert kernel['final_grid']==[kernel['polynomial_sum'][0]-2**72,kernel['polynomial_sum'][1]+2**72]
    save('replay-ledger.json',{'n':n,'counts':dict(replay.LEDGER)})
    save('replay.json',report)
    save('status.json',{'status':'PASS','n':n,'panels':1016,'pairs_per_pass':21264880,
        'parameter_complete_equal':True,'ledger_equal':True,'strict_radius_tests':[183,50],
        'radius':kernel['radius'],'elapsed_seconds':time.monotonic()-start})
    print(json.dumps({'n':n,'status':'PASS','radius':kernel['radius']}),flush=True)
except BaseException as exc:
    save('first-failure.json',{'type':type(exc).__name__,'message':str(exc),'state':state,'traceback':traceback.format_exc()})
    print(json.dumps({'n':n,'status':'STOP','state':state,'error':str(exc)}),flush=True)
    sys.exit(1)
