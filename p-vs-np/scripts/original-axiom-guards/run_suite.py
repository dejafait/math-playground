"""Complete fixed and bounded growing streams; concise results, full certificate."""
import copy
import gzip
import json
import math
from pathlib import Path
import build
ep,p,checker,aggregate=build.ep,build.p,build.checker,build.aggregate
HERE=Path(__file__).resolve().parent; OUT=HERE/'output'
CERT=OUT/'certificate-184.json'
def save(cert): CERT.write_text(json.dumps(cert,indent=2)+'\n')
def pair_images(native,image):
    def tr(s): return checker.serialize(ep.image(checker.parse(s,'native')[0]))
    with gzip.open(native,'rt') as ns,gzip.open(image,'rt') as ims:
        nh,ih=json.loads(next(ns)),json.loads(next(ims))
        assert ih=={'format':'not-or','goal':tr(nh['goal'])}
        for nr,ir in itertools.zip_longest(ns,ims):
            assert nr is not None and ir is not None
            n,i=json.loads(nr),json.loads(ir); expected=dict(n,f=tr(n['f']))
            if 'subs' in n: expected['subs']={k:tr(v) for k,v in n['subs'].items()}
            assert expected==i
import itertools
def library(cert):
    result={}
    for name,goal in build.schemas().items():
        paths={}; metrics={}
        native=OUT/('fixed-'+name+'.native.jsonl.gz')
        if native.exists():
            # Existing fixed evidence is validated in full before reuse.
            base=aggregate.load(native,p.text(goal))
            obj=build.store({}); obj.root=obj.copy(base['rows'],{})
        else:
            obj=p.Proof(); obj.build_helpers(); root=obj.prove_fixed(goal)
        for image,mode in [(False,'native'),(True,'not-or')]:
            path=OUT/('fixed-'+name+'.'+mode+'.jsonl.gz')
            if isinstance(obj,p.Proof): obj.write(root,path,image)
            else: obj.write(path,image)
            expected=p.text(goal,image)
            metrics[mode]=checker.check(path,expected); paths[mode]=path
        pair_images(paths['native'],paths['not-or'])
        result[name]=aggregate.load(paths['native'],p.text(goal))
        cert['library'][name]=metrics; save(cert)
        print('fixed',name,metrics['native']['lines'],'complete both formats',flush=True)
    return result
def lit(a,neg=False): return {'var':a,'negative':neg}
def OR(a,b): return {'op':'or','left':a,'right':b}
def package(cs,tree,q='q'):
    ds=sorted({o['var'] for c in cs for o in ep.clause(c)[2]})
    aa=ep.axioms(cs,ds)
    return {'q':q,'clauses':cs,'conjunction':tree,'dictionary':ds,'axioms':aa,
            'placeholders':['t_'+str(j+1) for j in range(len(aa))]}
def run(cert,lib):
    L=max(v['native']['lines'] for v in cert['library'].values())
    constants={mode:{'D':max(v[mode]['max_line_depth'] for v in cert['library'].values()),
                     'S':max(v[mode]['max_record_nodes'] for v in cert['library'].values())}
               for mode in ['native','not-or']}
    cert['constants']={'L':L,**constants}; save(cert)
    cs=[OR(lit('q'),lit('q',True)),OR(OR(lit('A'),lit('A')),lit('B',True)),
        OR(lit('A',True),OR(lit('B'),lit('q'))),lit('A'),lit('A')]
    deepcs=[OR(lit('A'),lit('A',True)) for _ in range(12)]
    skew=0
    for j in range(1,len(deepcs)): skew={'left':skew,'right':j}
    specs=[('one-clause-q-collision',package([lit('q')],0)),
           ('mixed-repeated-positions',package(cs,{'left':{'left':0,'right':1},'right':{'left':2,'right':{'left':3,'right':4}}})),
           ('deep-skew-equal-clauses',package(deepcs,skew)),
           ('long-name-negative',package([lit('x_'+'7'*180,True)],0,'x_'+'7'*180))]
    for name,data in specs:
        (OUT/(name+'-request.json')).write_text(json.dumps(data,indent=2)+'\n')
        g,_,evals,_=ep.request(data); m=len(data['clauses']); count=len(evals)
        J0=L+m*(2*L+2); J=count*J0
        case={'name':name,'request':str((OUT/(name+'-request.json')).relative_to(HERE.parent.parent)),
              'axiom_count':count,'m':m,'J0':J0,'total_line_bound':J,'proofs':[]}
        for index in range(count):
            o=build.compile_one(data,index,lib); paths={}; result={'position':index+1,'formats':{}}
            for image,mode in [(False,'native'),(True,'not-or')]:
                path=OUT/(name+'-a'+str(index+1)+'.'+mode+'.jsonl.gz'); written=o.write(path,image)
                measured=checker.check(path,ep.goals(data,mode)[index])
                assert all(written[k]==measured[k] for k in ('lines','bytes','sha256'))
                tr=ep.image if image else lambda t:t
                gs=ep.stats(tr(g)); es=[ep.stats(tr(a)) for a in evals]
                zs=ep.stats(tr(ep.n(ep.i(data['q'],data['q']))))
                # Image E has 8+2|A|+2|B| nodes and argument depth overhead <=6.
                W=2*gs[0]+2*max(a[0] for a in es)+2*zs[0]+16
                d=max(gs[1],max(a[1] for a in es)+6,zs[1]+6)
                B=max([gs[2],zs[2]]+[a[2] for a in es]); D,S=constants[mode]['D'],constants[mode]['S']
                F=256+64*math.ceil(math.log2(J0+2))
                bounds={'lines':J0,'depth':D+d,'record_nodes':S*W,
                        'bytes':(J0+2)*((B+4)*S*W+F)}
                tests={k:measured[v]<=bounds[k] for k,v in [('lines','lines'),('depth','max_line_depth'),
                                                                        ('record_nodes','max_record_nodes'),('bytes','bytes')]}
                assert all(tests.values()),tests
                result['formats'][mode]={'measurement':measured,'parameters':{'W':W,'d':d,'B':B},'bounds':bounds,'tests':tests}
                paths[mode]=path
            pair_images(paths['native'],paths['not-or']); case['proofs'].append(result)
            print(name,'axiom',index+1,'lines',result['formats']['native']['measurement']['lines'],'/',J0,
                  'bytes',result['formats']['native']['measurement']['bytes'],'/',result['formats']['native']['bounds']['bytes'],flush=True)
        for mode in ['native','not-or']:
            actual=sum(r['formats'][mode]['measurement']['lines'] for r in case['proofs'])
            assert actual<=J
        cert['cases'].append(case); save(cert)
    # Request-level mismatches are rejected before proof construction.
    good=specs[1][1]
    mutations=[('axiom-tree',lambda d:d['axioms'].__setitem__(0,0)),
               ('boolean-constant',lambda d:d['axioms'][0]['left'].__setitem__('left',True)),
               ('dictionary',lambda d:d['dictionary'].reverse()),
               ('placeholder-position',lambda d:d['placeholders'].__setitem__(0,'t_2')),
               ('clause-order',lambda d:d.__setitem__('conjunction',0)),
               ('empty-clause',lambda d:d['clauses'].__setitem__(0,{})),
               ('bad-name',lambda d:d.__setitem__('q','bad-name')),
               ('nonboolean-sign',lambda d:d['clauses'][0]['left'].__setitem__('negative',0)),
               ('wrong-product-bracketing',lambda d:d['axioms'].__setitem__(1,
                 ep.binop('product',d['axioms'][1]['left']['left'],
                          ep.binop('product',d['axioms'][1]['left']['right'],d['axioms'][1]['right'])))),
               ('overwidth',lambda d:d['clauses'].__setitem__(0,OR(OR(lit('A'),lit('A')),OR(lit('A'),lit('A')))))]
    for name,mutate in mutations:
        data=copy.deepcopy(good); mutate(data)
        path=OUT/('rejected-'+name+'.json'); path.write_text(json.dumps(data,indent=2)+'\n')
        try: build.compile_one(data,0,lib)
        except checker.Invalid as err:
            cert['rejections'].append({'name':name,'reason':str(err),'path':str(path.relative_to(HERE.parent.parent))})
        else: raise AssertionError('malformed request accepted '+name)
    # Preserve and reject corrupted complete strings in each format.
    for mode in ['native','not-or']:
        goodpath=OUT/('one-clause-q-collision-a1.'+mode+'.jsonl.gz')
        with gzip.open(goodpath,'rt') as stream: records=[json.loads(s) for s in stream]
        for tag in ['forward-reference','wrong-endpoint','bad-substitution']:
            bad=copy.deepcopy(records)
            if tag=='forward-reference':
                j=next(j for j,r in enumerate(bad[1:]) if r['rule']=='mp')
                bad[j+1]['refs'][0]=j
            elif tag=='wrong-endpoint': bad[0]['goal']='Q'
            else:
                r=next(r for r in bad[1:] if 'subs' in r); r['subs']['A']='Q'
            path=OUT/('rejected-'+tag+'.'+mode+'.jsonl.gz')
            with gzip.open(path,'wt') as stream:
                for r in bad: stream.write(json.dumps(r,separators=(',',':'))+'\n')
            try: checker.check(path)
            except checker.Invalid as err: cert['rejections'].append({'name':tag+'-'+mode,'reason':str(err),'path':str(path.relative_to(HERE.parent.parent))})
            else: raise AssertionError('bad primitive stream accepted')
    cert['complete']=True; save(cert)
    print('PASS',len(cert['library']),'fixed schemas;',sum(c['axiom_count'] for c in cert['cases']),
          'growing guards both formats;',len(cert['rejections']),'rejections; certificate',CERT,flush=True)
def main():
    OUT.mkdir(exist_ok=True)
    cert={'complete':False,'failures':[],'library':{},'cases':[],'rejections':[]}; save(cert)
    try: run(cert,library(cert))
    except Exception as err:
        cert['failures'].append(repr(err)); save(cert); raise
if __name__=='__main__': main()
