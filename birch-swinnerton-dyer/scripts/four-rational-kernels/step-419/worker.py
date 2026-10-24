
import importlib.util,json,sys,time,traceback
from pathlib import Path
from fractions import Fraction
sys.dont_write_bytecode=True
n=int(sys.argv[1]); OUT=Path(sys.argv[2]); START=float(sys.argv[3]); OLD=Path('scripts/four-rational-kernels/step-417')/('n-'+str(n))
state={'n':n,'stage':'setup','panels':0}
def read(name): return json.loads((OLD/name).read_text())
def save(name,obj): (OUT/name).write_text(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n')
def progress(stage,panels):
    state.update(stage=stage,panels=panels)
    assert time.monotonic()-START<174
    save('working.json',{**state,'elapsed_seconds':time.monotonic()-START})
try:
    spec=importlib.util.spec_from_file_location('fixed_replay_419_'+str(n),OLD/'replay.py')
    replay=importlib.util.module_from_spec(spec); spec.loader.exec_module(replay)
    D=replay.SCALE
    assert D==2**256
    signed={k:0 for k in ('floor','ceiling','multiply','divide','convert','plus','negate','clip','products','zero_operand_multiplications')}
    signed['sign_cases']=[0]*9
    # Fresh retained source containing only the individually reviewed primitive wrappers/controls.
    exec(compile((OUT.parent/'signed-checks.py').read_text(),'signed-checks-419','exec'))
    parameter=read('parameter.json')
    assert parameter==json.loads(Path('scripts/first-rational-kernel/step-404/parameter.json').read_text())
    assert parameter['midpoint']==[73775804382331484748893662180180200545104154546089041648426948815067512948607,2**257]
    final=read('kernel.json')
    progress('replay',0)
    with (OLD/'panels.jsonl').open() as handle:
        report=replay.run(parameter,(json.loads(line) for line in handle),final,progress)
    assert 'n' not in report
    assert {**report,'n':n}==read('replay.json')
    counts=dict(replay.LEDGER)
    assert report['counts']==counts==final['counts']
    for name in ('producer-ledger.json','replay-ledger.json'):
        assert read(name)=={'n':n,'counts':counts}
    for key,expected in {'multiply':21801456,'divide':716408,'convert':5083,'negate':356616,'clip':24386}.items():
        assert signed[key]==counts[key]==expected
    assert signed['products']==2032 and counts['coefficient_pairs']==21264880
    assert counts['add']==21787232==signed['plus']+21264880+1016
    assert counts['scale']==2033 and counts['enlarge']==2034
    assert sum(signed['sign_cases'])==signed['multiply']
    assert signed['floor']==signed['ceiling']==signed['multiply']+signed['divide']+signed['convert']+1
    expected=json.loads((OUT.parent/'expected-endpoints.json').read_text())[str(n)]
    l,u,w=expected
    assert final['n']==n and final['final_grid']==[l,u]
    assert final['polynomial_sum']==[l+2**72,u-2**72]
    assert u-l==2**73+w
    assert Fraction(*final['midpoint'])==Fraction(l+u,2*D)
    assert Fraction(*final['radius'])==Fraction(2**73+w,2*D)<Fraction(1,2**183)<Fraction(1,2**50)
    assert final['required_radius']==[1,2**50] and final['stronger_radius']==[1,2**183]
    assert read('parameter-identity.json')=={'n':n,'complete_record_equal':True,'midpoint_unchanged':True}
    status=read('status.json')
    for key,value in {'status':'PASS','n':n,'panels':1016,'pairs_per_pass':21264880,'parameter_complete_equal':True,'ledger_equal':True,'strict_radius_tests':[183,50],'radius':final['radius']}.items(): assert status[key]==value
    save('complete-replay.json',{'status':'PASS','n':n,'replay':report,'immutable_ledger':counts,'distinct_signed_checks':signed,'parameter':parameter,'kernel':final,'sole_metadata_addition':'n','producer_executed':False,'strict_radius_powers':[183,50]})
    state.update(stage='complete',panels=1016)
    save('status.json',{'status':'PASS','state':state,'elapsed_seconds':time.monotonic()-START})
    print(json.dumps({'n':n,'status':'PASS','panels':1016,'coefficient_pairs':counts['coefficient_pairs'],'strict_radius_powers':[183,50]}),flush=True)
except BaseException as exc:
    save('first-failure.json',{'type':type(exc).__name__,'message':str(exc),'state':state,'traceback':traceback.format_exc()})
    print(json.dumps({'n':n,'status':'STOP','state':state,'error':str(exc)}),flush=True)
    sys.exit(1)
