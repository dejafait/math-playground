"""Full certificate and complete primitive checks, no sampled proof evidence."""
import copy
import gzip
import itertools
import json
import math
from pathlib import Path
import build
p,ep,checker,aggregate=build.p,build.ep,build.checker,build.aggregate
HERE=Path(__file__).resolve().parent; OUT=HERE/'output'; CERT=OUT/'certificate-188.json'

def save(c): CERT.write_text(json.dumps(c,indent=2)+'\n')
def pair_images(native,image):
    def tr(s): return checker.serialize(ep.f.image(checker.parse(s,'native')[0]))
    with gzip.open(native,'rt') as ns,gzip.open(image,'rt') as ims:
        nh,ih=json.loads(next(ns)),json.loads(next(ims))
        assert ih=={'format':'not-or','goal':tr(nh['goal'])}
        for nr,ir in itertools.zip_longest(ns,ims):
            assert nr is not None and ir is not None
            n,i=json.loads(nr),json.loads(ir); wanted=dict(n,f=tr(n['f']))
            if 'subs' in n: wanted['subs']={k:tr(v) for k,v in n['subs'].items()}
            assert i==wanted

def library(cert):
    lib={}
    for name,goal in build.schemas().items():
        path=OUT/('fixed-'+name+'.native.jsonl.gz')
        if path.exists():
            obj=build.base.store({}); obj.root=obj.copy(aggregate.load(path,p.text(goal))['rows'],{})
        else:
            obj=p.Proof(); obj.build_helpers(); root=obj.prove_fixed(goal)
        paths={}; checks={}
        for image,mode in [(False,'native'),(True,'not-or')]:
            path=OUT/('fixed-'+name+'.'+mode+'.jsonl.gz')
            if isinstance(obj,p.Proof): obj.write(root,path,image)
            else: obj.write(path,image)
            # Independent builder reconstructs each finite bridge, including word order/tree.
            if name.startswith('bridge-'):
                signs,shape=name.split('-')[1:]; vs=['A','B','C'][:len(signs)]
                ls=[{'var':a,'negative':s=='n'} for a,s in zip(vs,signs)]
                c=ls[0] if len(ls)==1 else {'op':'or','left':ls[0],'right':ls[1]}
                if len(ls)==3:
                    c=({'op':'or','left':c,'right':ls[2]} if shape=='left' else
                       {'op':'or','left':ls[0],'right':{'op':'or','left':ls[1],'right':ls[2]}})
                ds=sorted(vs); aa=ep.f.axioms([c],ds)
                fact={'q':'q','clauses':[c],'conjunction':0,'dictionary':ds,'axioms':aa,
                      'placeholders':['t_'+str(j+1) for j in range(len(aa))]}
                ws,es=ep.expanded(fact); data={'factored':fact,'expanded_words':ws,'expanded_axioms':es}
                expected=ep.bridges(data,mode)[0]
            else:
                f=ep.f
                t=f.e('A','A') if name=='refl' else f.i(f.i('G',f.e('A','D')),f.i(f.e('A','B'),f.i('G',f.e('B','D'))))
                expected=checker.serialize(f.image(t) if image else t)
            assert expected==p.text(goal,image)
            checks[mode]=checker.check(path,expected); paths[mode]=path
        pair_images(paths['native'],paths['not-or'])
        lib[name]=aggregate.load(paths['native'],p.text(goal))
        cert['library'][name]=checks; save(cert)
        print('fixed',name,'lines',checks['native']['lines'],'both complete',flush=True)
    return lib

def run(cert,lib):
    constants={'L':max(v['native']['lines'] for v in cert['library'].values())}
    for mode in ['native','not-or']:
        constants[mode]={'D':max(v[mode]['max_line_depth'] for v in cert['library'].values()),
                         'S':max(v[mode]['max_record_nodes'] for v in cert['library'].values())}
    cert['constants']=constants; save(cert)
    # Reuse complete audited guards, preserving every imported record.
    source=HERE.parent/'original-axiom-guards'/'output'
    names=['one-clause-q-collision','mixed-repeated-positions','deep-skew-equal-clauses','long-name-negative']
    for name in names:
        fact=json.loads((source/(name+'-request.json')).read_text())
        ws,aa=ep.expanded(fact); data={'factored':fact,'expanded_words':ws,'expanded_axioms':aa}
        req=OUT/(name+'-request.json'); req.write_text(json.dumps(data,indent=2)+'\n')
        g,fs,es=ep.request(data); z=ep.f.n(ep.f.i(fact['q'],fact['q']))
        case={'name':name,'request':str(req.relative_to(HERE.parent.parent)),'proofs':[]}
        for index in range(len(es)):
            guard=source/(name+'-a'+str(index+1)+'.native.jsonl.gz')
            o,imp,end=build.compile_one(data,index,guard,lib)
            J=imp['measurement']['lines']+2*constants['L']+2
            entry={'position':index+1,'import':str(guard.relative_to(HERE.parent.parent)),
                   'import_lines':end,'import_sha256':imp['measurement']['sha256'],'formats':{}}
            paths={}
            for image,mode in [(False,'native'),(True,'not-or')]:
                path=OUT/(name+'-a'+str(index+1)+'.'+mode+'.jsonl.gz'); written=o.write(path,image)
                measured=checker.check(path,ep.goals(data,mode)[index])
                assert all(written[k]==measured[k] for k in ('lines','bytes','sha256'))
                tr=ep.f.image if image else lambda t:t
                st=[ep.f.stats(tr(t)) for t in [g,fs[index],es[index],z]]
                W=sum(s[0] for s in st)+8; d=max(s[1] for s in st)
                B=max([imp['name_bytes'],1]+[s[2] for s in st])
                # Imported nodes/depths are entire-package upper bounds, not maxima from previews.
                R=max(imp['node_sums'][mode],constants[mode]['S']*W)
                depth=max(imp['depths'][mode],constants[mode]['D']+d)
                bounds={'lines':J,'depth':depth,'record_nodes':R,
                        'bytes':(J+2)*((B+4)*R+256+64*math.ceil(math.log2(J+2)))}
                tests={k:measured[v]<=bounds[k] for k,v in [('lines','lines'),('depth','max_line_depth'),
                                  ('record_nodes','max_record_nodes'),('bytes','bytes')]}
                assert all(tests.values()),tests
                entry['formats'][mode]={'measurement':measured,'bounds':bounds,'tests':tests,
                      'parameters':{'W':W,'d':d,'B':B,'import_record_node_sum':imp['node_sums'][mode]}}
                paths[mode]=path
            pair_images(paths['native'],paths['not-or']); case['proofs'].append(entry)
            # Prefix equality checks complete import, including unused rows and references.
            with gzip.open(guard,'rt') as a,gzip.open(paths['native'],'rt') as b:
                next(a); next(b)
                for line in a: assert json.loads(line)==json.loads(next(b))
            cert['cases_in_progress']=case; save(cert)
            print(name,index+1,'lines',measured['lines'],'/',J,'bytes',measured['bytes'],'/',bounds['bytes'],flush=True)
        case['whole_list']={mode:{'actual_lines':sum(a['formats'][mode]['measurement']['lines'] for a in case['proofs']),
                                 'required_lines':sum(a['formats'][mode]['bounds']['lines'] for a in case['proofs']),
                                 'actual_bytes':sum(a['formats'][mode]['measurement']['bytes'] for a in case['proofs']),
                                 'required_bytes':sum(a['formats'][mode]['bounds']['bytes'] for a in case['proofs'])}
                            for mode in ['native','not-or']}
        cert['cases'].append(case); cert.pop('cases_in_progress',None); save(cert)
    good=json.loads((OUT/'mixed-repeated-positions-request.json').read_text())
    changes=[('reverse-words',lambda d:d['expanded_words'][1].reverse()),
             ('cancel-multiplicity',lambda d:d['expanded_words'][1].pop()),
             ('word-order',lambda d:d['expanded_words'][2][-1]['word'].reverse()),
             ('bad-coefficient',lambda d:d['expanded_words'][0][0].__setitem__('coefficient',True)),
             ('padded-sum',lambda d:d['expanded_axioms'].__setitem__(0,ep.f.binop('sum',d['expanded_axioms'][0],0))),
             ('wrong-tree',lambda d:d['expanded_axioms'].__setitem__(1,1)),
             ('role-collision',lambda d:d['factored']['placeholders'].__setitem__(0,'q')),
             ('missing-dictionary',lambda d:d['factored']['dictionary'].pop())]
    for name,mut in changes:
        d=copy.deepcopy(good); mut(d); path=OUT/('rejected-'+name+'.json'); path.write_text(json.dumps(d,indent=2)+'\n')
        try: ep.request(d)
        except checker.Invalid as err: cert['rejections'].append({'name':name,'reason':str(err),'path':str(path.relative_to(HERE.parent.parent))})
        else: raise AssertionError('malformed request accepted '+name)
    # Exact mismatching guard endpoints are rejected even if primitive valid.
    try: build.compile_one(good,1,source/'mixed-repeated-positions-a1.native.jsonl.gz',lib)
    except checker.Invalid as err: cert['rejections'].append({'name':'wrong-guard-endpoint','reason':str(err)})
    else: raise AssertionError('wrong guard accepted')
    for mode in ['native','not-or']:
        path=OUT/('one-clause-q-collision-a1.'+mode+'.jsonl.gz')
        with gzip.open(path,'rt') as s: rows=[json.loads(r) for r in s]
        for tag in ['forward-reference','bad-substitution','wrong-endpoint']:
            bad=copy.deepcopy(rows)
            if tag=='wrong-endpoint': bad[0]['goal']='Q'
            elif tag=='bad-substitution': next(r for r in bad[1:] if 'subs' in r)['subs']['A']='Q'
            else:
                j=next(j for j,r in enumerate(bad[1:]) if r['rule']=='mp'); bad[j+1]['refs'][0]=j
            dest=OUT/('rejected-'+tag+'.'+mode+'.jsonl.gz')
            with gzip.open(dest,'wt') as s:
                for r in bad: s.write(json.dumps(r,separators=(',',':'))+'\n')
            try: checker.check(dest)
            except checker.Invalid as err: cert['rejections'].append({'name':tag+'-'+mode,'reason':str(err),'path':str(dest.relative_to(HERE.parent.parent))})
            else: raise AssertionError('bad stream accepted')
    cert['complete']=True; save(cert)
    print('PASS',len(cert['library']),'fixed;',sum(len(c['proofs']) for c in cert['cases']),
          'guards both formats;',len(cert['rejections']),'rejections; failures',cert['failures'],'certificate',CERT,flush=True)

def main():
    OUT.mkdir(exist_ok=True)
    cert={'complete':False,'failures':[],'library':{},'cases':[],'rejections':[]}; save(cert)
    try: run(cert,library(cert))
    except Exception as err: cert['failures'].append(repr(err)); save(cert); raise
if __name__=='__main__': main()
