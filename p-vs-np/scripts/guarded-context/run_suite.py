"""Bounded complete primitive proof test with full certificates and paid copying."""
import gzip
import itertools
import json
import math
from pathlib import Path
import lift
import context_endpoints as ep
p,checker,aggregate=lift.primitive,lift.checker,lift.aggregate
HERE=Path(__file__).resolve().parent; OUT=HERE/'output'
SLOT=HERE.parent/'balanced-slot'/'output'

def save(path,obj): path.write_text(json.dumps(obj,indent=2)+'\n')
def read(path):
    with gzip.open(path,'rt') as f: return json.loads(next(f)),[json.loads(s) for s in f]
def write(path,head,rows):
    with gzip.open(path,'wt') as f:
        for row in [head]+rows: f.write(json.dumps(row,separators=(',',':'))+'\n')
def bare_store():
    o=aggregate.Combination.__new__(aggregate.Combination)
    o.p=aggregate.AppendProof()
    return o
def check_images(native,image):
    nh,nr=read(native); ih,ir=read(image)
    def translated(s): return checker.serialize(ep.image(ep.validate_term(s)))
    assert ih=={'format':'not-or','goal':translated(nh['goal'])}
    assert len(nr)==len(ir)
    for n,i in zip(nr,ir):
        target=dict(n,f=translated(n['f']))
        if 'subs' in n: target['subs']={k:translated(v) for k,v in n['subs'].items()}
        assert i==target

def fixed_library(cert):
    a,b,c,g='A','B','C','G'; library={}
    for op,side in itertools.product(['xor','and'],['left','right']):
        name=op+'-'+side
        fun=p.X if op=='xor' else lift.conjunction
        left,right=(fun(a,c),fun(b,c)) if side=='left' else (fun(c,a),fun(c,b))
        law=p.I(p.E(a,b),p.E(left,right))
        if op=='xor':
            base=aggregate.load(SLOT/('cong'+('L' if side=='left' else 'R')+'.native.jsonl.gz'),p.text(law))
        else:
            synth=p.Proof(); synth.build_helpers(); root=synth.prove_fixed(law)
            path=OUT/(name+'-unguarded.native.jsonl.gz'); synth.write(root,path)
            base=aggregate.load(path,p.text(law))
            cert['unguarded'][name]=base['measurement']
        o=bare_store(); old=o.copy(base['rows'],{})
        glaw=o.p.mp(old,o.p.ax('ax1',law,g))
        o.root=o.p.mp(glaw,o.p.ax('ax2',g,p.E(a,b),p.E(left,right)))
        expected=p.text(p.I(p.I(g,p.E(a,b)),p.I(g,p.E(left,right))))
        paths={}
        for image,mode in [(False,'native'),(True,'not-or')]:
            path=OUT/('fixed-'+name+'.'+mode+'.jsonl.gz'); o.write(path,image)
            goal=expected if not image else checker.serialize(ep.image(ep.validate_term(expected)))
            cert['library'][name+'-'+mode]=checker.check(path,goal)
            paths[mode]=path
        check_images(paths['native'],paths['not-or'])
        library[name]=aggregate.load(paths['native'],expected)
        save(OUT/'certificate-180.json',cert)
        print('fixed',name,'lines',len(library[name]['rows']),'both formats checked',flush=True)
    return library

def supplied(path,g,u,v,law,env,pad):
    base=aggregate.load(SLOT/(law+'.native.jsonl.gz'),p.text(p.schemas()[law]))
    o=bare_store()
    if pad:
        deep='G'
        for _ in range(pad): deep=p.N(deep)
        o.p.ax('ax1',deep,'q')
    eq=o.copy(base['rows'],env)
    f=o.p.rows[eq][0]
    o.root=o.p.mp(eq,o.p.ax('ax1',f,aggregate.native(ep.validate_term(g))))
    o.write(path)
    return aggregate.load(path,ep.coordinate(g,u,v))

def main():
    OUT.mkdir(exist_ok=True)
    cert={'complete':False,'failures':[],'library':{},'unguarded':{},'cases':[],'corruptions':[]}
    certpath=OUT/'certificate-180.json'; save(certpath,cert)
    try:
        library=fixed_library(cert)
        constants={mode:{'D':max(cert['library'][n+'-'+mode]['max_line_depth'] for n in library),
                         'S':max(cert['library'][n+'-'+mode]['max_record_nodes'] for n in library),
                         'c':3 if mode=='native' else 6} for mode in ['native','not-or']}
        L=max(len(v['rows']) for v in library.values()); cert['constants']={'L':L,**constants}
        mark={'mark':True}
        term=lambda t:{'term':p.text(t)}
        node=lambda op,l,r:{'op':op,'left':l,'right':r}
        t=p.I('q','q'); z=p.N(t)
        deep='A'
        for _ in range(28): deep=p.N(deep)
        specs=[('identity','G','double_neg_bridge',{'A':'A'},'A',p.N(p.N('A')),mark,40)]
        for op,side in itertools.product(['xor','and'],['left','right']):
            ctx=node(op,mark,term(z)) if side=='left' else node(op,term(t),mark)
            specs.append((op+'-'+side,p.text(deep),'comm',{'A':'A','B':'G'},p.X('A','G'),p.X('G','A'),ctx,42))
        ctx2=node('and',node('xor',term('A'),mark),node('xor',term(z),term(t)))
        ctx3=node('xor',node('and',node('xor',term('G'),term('A')),node('xor',mark,term('q'))),
                  node('xor',node('and',term(t),term(z)),node('and',term('A'),term('A'))))
        specs.extend([
            ('mixed-h2',p.text(deep),'double_neg_bridge',{'A':z},z,p.N(p.N(z)),ctx2,44),
            ('mixed-h3','G','double_neg_bridge',{'A':'C'},'C',p.N(p.N('C')),ctx3,48)])
        guard80='G'; payload22='A'; sibling34='C'
        for _ in range(80): guard80=p.N(guard80)
        for _ in range(22): payload22=p.N(payload22)
        for _ in range(34): sibling34=p.N(sibling34)
        deepctx=node('and',node('xor',node('and',term(sibling34),mark),node('and',term(t),term(z))),
                     node('xor',node('and',term('G'),term('G')),node('xor',term('A'),term('q'))))
        specs.append(('mixed-h3-deep-payload',p.text(guard80),'double_neg_bridge',{'A':payload22},
                      payload22,p.N(p.N(payload22)),deepctx,0))
        for name,g,law,env,u,v,ctx,pad in specs:
            u,v=p.text(u),p.text(v)
            path=OUT/(name+'-supplied.native.jsonl.gz')
            package=supplied(path,g,u,v,law,env,pad)
            o=lift.Lift(g,u,v,ctx,path,library); o.run()
            # Inspect every retained input record, including unused padded records.
            for k,(f,rule,refs,subs) in enumerate(package['rows']):
                out=o.p.rows[k]
                assert out[0]==f and out[1]==rule and tuple(out[2])==tuple(refs)
                assert out[3]==(subs if rule!='mp' else None)
            s,h,terms=ep.request(g,u,v,ctx); k=len(o.events); N=len(package['rows'])
            R=k*(L+1); J=N+R
            assert k<=h and h<=math.ceil(math.log2(s+1))
            case={'name':name,'guard':g,'U':u,'V':v,'context':ctx,'s':s,'h':h,'k':k,'N':N,'R':R,'J':J,
                  'input':{**package['measurement'],'node_sums':package['node_sums'],'depths':package['depths']},
                  'events':o.events,'proofs':{}}
            paths={}
            for image,mode in [(False,'native'),(True,'not-or')]:
                outpath=OUT/(name+'.'+mode+'.jsonl.gz'); written=o.write(outpath,image)
                measured=checker.check(outpath,ep.goal(g,u,v,ctx,mode))
                assert all(measured[key]==written[key] for key in ['bytes','lines','sha256'])
                fmt=lambda tree:ep.image(tree) if image else tree
                ts=[ep.stats(fmt(ep.validate_term(t))) for t in [u,v]+terms]
                t,d=max(a[0] for a in ts),max(a[1] for a in ts)
                gs=ep.stats(fmt(ep.validate_term(g))); gn,gd=gs[:2]
                B=max([package['name_bytes'],gs[2]]+[a[2] for a in ts])
                K=package['node_sums'][mode]; delta=package['depths'][mode]
                P=max(gn,8*4**(h+1)*(t+1)); D,S,c=(constants[mode][key] for key in ['D','S','c'])
                F=256+64*math.ceil(math.log2(J+2))
                # Identity endpoint is already present; generated header still paid conservatively.
                bounds={'lines':J,'depth':max(delta,D+max(gd,c*h+d)),
                        'record_nodes':max(K,S*P),'bytes':(B+4)*(K+(R+1)*S*P)+(J+2)*F}
                bounds['bits']=8*bounds['bytes']
                tests={key:measured[field]<=bounds[key] for key,field in
                       [('lines','lines'),('depth','max_line_depth'),('record_nodes','max_record_nodes'),('bytes','bytes')]}
                args=[ep.stats(fmt(ep.validate_term(a))) for event in o.events for key,a in event['arguments'].items() if key!='G']
                argmax={'nodes':max([t]+[a[0] for a in args]),'depth':max([d]+[a[1] for a in args])}
                tests['context_argument_nodes']=argmax['nodes']<=P
                tests['context_argument_depth']=argmax['depth']<=c*h+d
                tests['exact_guard_arguments']=all(e['arguments']['G']==g for e in o.events)
                assert all(tests.values()),tests
                case['proofs'][mode]={'measurement':dict(measured,storage_bytes=written['storage_bytes']),
                                      'parameters':{'t':t,'d':d,'guard_nodes':gn,'guard_depth':gd,'B':B,'K':K,'delta':delta,'P':P},
                                      'bounds':bounds,'tests':tests,'context_arguments':argmax}
                paths[mode]=outpath
                print(name,mode,'lines',measured['lines'],'/',J,'depth',measured['max_line_depth'],'/',bounds['depth'],
                      'bytes',measured['bytes'],'/',bounds['bytes'],'passed',flush=True)
            check_images(paths['native'],paths['not-or'])
            cert['cases'].append(case); save(certpath,cert)
        # Corrupt the complete identity package; rejection is at reception, not output checking.
        head,rows=read(OUT/'identity-supplied.native.jsonl.gz')
        mp=next(k for k,r in enumerate(rows) if r['rule']=='mp')
        wrong=next(k for k,r in enumerate(rows) if r['rule']=='mp' and any(rows[j]['f']!=rows[r['refs'][0]]['f'] for j in range(k)))
        other=next(j for j in range(wrong) if rows[j]['f']!=rows[rows[wrong]['refs'][0]]['f'])
        changes=[('endpoint',None,dict(head,goal='BAD')),
                 ('substitution',0,dict(rows[0],subs=dict(rows[0]['subs'],A='BAD'))),
                 ('reference',mp,dict(rows[mp],refs=[0,len(rows)])),
                 ('mp-antecedent',wrong,dict(rows[wrong],refs=[other,rows[wrong]['refs'][1]])),
                 ('premise',0,{'f':rows[0]['f'],'rule':'assume'}),
                 ('image-input',None,dict(head,format='not-or'))]
        g,u,v='G','A',p.text(p.N(p.N('A')))
        for label,index,replacement in changes:
            hh,rr=dict(head),list(rows)
            if index is None: hh=replacement
            else: rr[index]=replacement
            bad=OUT/('corrupt-'+label+'.native.jsonl.gz'); write(bad,hh,rr)
            try: lift.Lift(g,u,v,mark,bad,library)
            except (ValueError,checker.Invalid) as err:
                cert['corruptions'].append({'name':label,'path':str(bad.relative_to(HERE.parents[1])),
                                           'rejected':True,'reason':str(err)})
            else: raise AssertionError('accepted '+label)
        for label,badg,badpath,badctx in [
            ('changed-guard','CHANGED',OUT/'identity-supplied.native.jsonl.gz',mark),
            ('missing-proof',g,None,mark),
            ('missing-mark',g,OUT/'identity-supplied.native.jsonl.gz',term('A')),
            ('two-marks',g,OUT/'identity-supplied.native.jsonl.gz',node('xor',mark,mark))]:
            try: lift.Lift(badg,u,v,badctx,badpath,library)
            except checker.Invalid as err:
                cert['corruptions'].append({'name':label,'rejected':True,'reason':str(err)})
            else: raise AssertionError('accepted '+label)
        cert['complete']=True; save(certpath,cert)
        print('10 malformed receptions rejected; complete certificate',certpath.relative_to(HERE.parents[1]),
              'failures',len(cert['failures']),flush=True)
    except Exception as err:
        cert['failures'].append(repr(err)); save(certpath,cert); raise

if __name__=='__main__': main()
