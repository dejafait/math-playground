"""Step 196: archive-only primitive audit; never emits transition proofs.

Native axiom instances are reconstructed from checked substitution syntax.
MP uses interned syntax nodes, not semantic evaluation. Every serialized native
and image record must equal the reconstructed record. Interning is solely a
checker implementation: counts and byte comparisons use fully expanded trees.
"""
import copy
import gzip
import hashlib
import json
import re
import sys
import importlib.util
from functools import lru_cache
from itertools import zip_longest
from pathlib import Path
import ledger

# Do not occupy the generic `endpoints` name: aggregate deliberately resolves
# that name to balanced-coordinate/endpoints.py when build is imported later.
spec = importlib.util.spec_from_file_location('audit_zero_endpoints', Path(__file__).with_name('endpoints.py'))
ep = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ep)

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / 'output'
DEST = OUT / 'audit-196.json'


def unique(pairs):
    d = {}
    for k, v in pairs:
        if k in d: raise ValueError('duplicate field')
        d[k] = v
    return d


def read(raw): return json.loads(raw, object_pairs_hook=unique)


class Syntax:
    def __init__(self):
        self.ids = {}
        self.nodes = []
        self.stats = []

    def node(self, tag, *args):
        key = (tag, *args)
        if key in self.ids: return self.ids[key]
        j = len(self.nodes)
        self.ids[key] = j
        self.nodes.append(key)
        if tag == 'v':
            assert re.fullmatch(r'[A-Za-z0-9_]+', args[0])
            s = (1, 0, 1, 0, len(args[0]))
        elif tag == 'n':
            a = self.stats[args[0]]
            s = (1+a[0], 1+a[1], 1+a[2], 1+a[3], a[4])
        else:
            a, b = [self.stats[k] for k in args]
            s = (1+a[0]+b[0], 1+max(a[1],b[1]),
                 2+a[2]+b[2], 1+max(1+a[3],b[3]), max(a[4],b[4]))
        self.stats.append(s)
        return j

    def tree(self, t):
        if isinstance(t,str): return self.node('v',t)
        return self.node('n' if t[0]=='not' else 'i', *(self.tree(a) for a in t[1:]))

    @lru_cache(512)
    def parse(self, text): return self.tree(ep.c.parse(text,'native')[0])

    @lru_cache(512)
    def text(self, j, image=False):
        tag,*args = self.nodes[j]
        if tag=='v': return args[0]
        if tag=='n': return '(~'+self.text(args[0],image)+')'
        a,b = [self.text(k,image) for k in args]
        return '((~'+a+')|'+b+')' if image else '('+a+'>'+b+')'

    def ax(self, rule, subs):
        required = {'A','B','C'} if rule=='ax2' else {'A','B'}
        assert rule in ('ax1','ax2','ax3') and set(subs)==required
        a,b = [self.parse(subs[k]) for k in ('A','B')]
        I = lambda a,b:self.node('i',a,b)
        N = lambda a:self.node('n',a)
        if rule=='ax1': return I(a,I(b,a))
        if rule=='ax3': return I(I(N(a),N(b)),I(b,a))
        c = self.parse(subs['C'])
        return I(I(a,I(b,c)),I(I(a,b),I(a,c)))


syntax = Syntax()


def scan(path, expected, imagepath=None, roots=None, imports=()):
    """Check every record, both literal formats, and full relocated imports."""
    roots = roots or {}
    paths = [path] + ([imagepath] if imagepath else [])
    modes = ['native'] + (['not-or'] if imagepath else [])
    streams = [gzip.open(p,'rb') for p in paths]
    measurements = []
    digests = [hashlib.sha256() for p in paths]
    goal = syntax.parse(expected)
    for stream,mode,digest in zip(streams,modes,digests):
        raw = stream.readline(); digest.update(raw)
        image = mode=='not-or'
        assert read(raw)=={'format':mode,'goal':syntax.text(goal,image)}
        s=syntax.stats[goal]; a=2 if image else 0
        measurements.append({'path':str(paths[len(measurements)].relative_to(ROOT)),
            'format':mode,'accepted':True,'lines':0,'bytes':len(raw),
            'formula_nodes':0,'substitution_nodes':0,'max_line_nodes':0,
            'max_record_nodes':0,'max_line_depth':0,
            'goal_nodes':s[a],'goal_depth':s[a+1]})
    imported = iter(import_rows(imports))
    next_import = next(imported,None)
    formulas=[]; references=[]; payload=1; depths=[0,0]; sums=[0,0]
    for index,raws in enumerate(zip_longest(*streams)):
        assert all(raw is not None for raw in raws), 'different stream lengths'
        row=read(raws[0]); rule=row['rule']
        if rule=='mp':
            assert set(row)=={'f','rule','refs'}
            refs=row['refs']
            assert len(refs)==2 and all(type(k)is int and 0<=k<index for k in refs)
            antecedent,conditional=[formulas[k] for k in refs]
            tag,*args=syntax.nodes[conditional]
            assert tag=='i' and args[0]==antecedent, 'MP mismatch'
            f=args[1]; subs={}
        else:
            assert set(row)=={'f','rule','subs'}
            subs=row['subs']; f=syntax.ax(rule,subs); refs=[]
        assert row['f']==syntax.text(f), 'native record differs'
        if index in roots: assert row['f']==roots[index], 'requested root differs'
        if next_import is not None:
            at,wanted=next_import
            assert index==at and row==wanted, 'full import mismatch'
            next_import=next(imported,None)
        formulas.append(f); references.append(refs)
        fields=[f]+[syntax.parse(v) for v in subs.values()]
        payload=max(payload,*(syntax.stats[t][4] for t in fields))
        for m,(raw,mode,digest) in enumerate(zip(raws,modes,digests)):
            image=mode=='not-or'; a=2 if image else 0
            wanted={'f':syntax.text(f,image),'rule':rule}
            if rule=='mp': wanted['refs']=refs
            else: wanted['subs']={k:syntax.text(syntax.parse(v),image) for k,v in subs.items()}
            assert read(raw)==wanted, 'literal image/record differs'
            count=syntax.stats[f][a]; depth=syntax.stats[f][a+1]
            scount=sum(syntax.stats[t][a] for t in fields[1:])
            info=measurements[m]
            info['lines']+=1; info['bytes']+=len(raw); digest.update(raw)
            info['formula_nodes']+=count; info['substitution_nodes']+=scount
            info['max_line_nodes']=max(info['max_line_nodes'],count)
            info['max_record_nodes']=max(info['max_record_nodes'],count+scount)
            info['max_line_depth']=max(info['max_line_depth'],depth)
        for m,a in enumerate((0,2)):
            sums[m]+=sum(syntax.stats[t][a] for t in fields)
            depths[m]=max(depths[m],*(syntax.stats[t][a+1] for t in fields))
    assert next_import is None and formulas and formulas[-1]==goal
    assert all(0<=k<len(formulas) for k in roots)
    for stream in streams: stream.close()
    for info,digest in zip(measurements,digests): info['sha256']=digest.hexdigest()
    return {'measurements':dict(zip(modes,measurements)),
            'rows':range(len(formulas)), 'node_sums':dict(zip(('native','not-or'),sums)),
            'depths':dict(zip(('native','not-or'),depths)), 'name_bytes':payload,
            'references':references}


def import_rows(imports):
    offset=0
    for path,count in imports:
        with gzip.open(path,'rb') as stream:
            next(stream)
            got=0
            for raw in stream:
                row=read(raw)
                if row['rule']=='mp': row['refs']=[offset+k for k in row['refs']]
                yield offset+got,row
                got+=1
            assert got==count
        offset+=count


def same_measurement(actual,saved):
    for key,value in actual.items(): assert saved[key]==value,(key,value,saved.get(key))


def ancestors(references, root):
    seen=set(); todo=[root]
    while todo:
        i=todo.pop()
        if i in seen: continue
        seen.add(i); todo.extend(references[i])
    return seen


def term_stats(d,mode):
    texts=d['suffixes']+d['letters']+['('+d['q']+'>'+d['q']+')','(~('+d['q']+'>'+d['q']+'))']
    a=2 if mode=='not-or' else 0
    stats=[syntax.stats[syntax.parse(t)] for t in texts]
    return max(s[a] for s in stats),max(s[a+1] for s in stats),max(s[4] for s in stats)


def independent_bound(d,packages,constants,library_names):
    D=2+d['N']+d['n']+d['k']; h=(D-1).bit_length()
    V=2**(3*h+4); H=9*h+20; E=10000*V*V*(H+1)**2
    G=(constants['L']+1)*E; J=sum(len(p['rows']) for p in packages)+G
    out={}
    for mode,c in [('native',3),('not-or',6)]:
        t,depth,names=term_stats(d,mode)
        B=max(1,names,library_names,*(p['name_bytes'] for p in packages))
        K=sum(p['node_sums'][mode] for p in packages)
        delta=max(p['depths'][mode] for p in packages)
        S=constants[mode]['S']; DD=constants[mode]['D']; P=8*4**(H+1)*(t+1)
        out[mode]={'lines':J,'depth':max(delta,DD+c*H+depth),
                   'record_nodes':max(K,S*P),
                   'bytes':(B+4)*(K+(G+1)*S*P)+(J+2)*(256+64*(J+1).bit_length())}
    return out


def main():
    cert={'complete':False,'failures':[],'library':{},'cases':[],'corruptions':[]}
    finish = '--finish-preserved-replay' in sys.argv
    if finish:
        cert=json.loads((OUT/'audit-196-initial.json').read_text())
        assert len(cert['library'])==14 and len(cert['cases'])==6
        cert['harness_failures']=cert['failures']
        cert['failures']=[]
        cert['corruptions']=[]
        cert['resumption']='Retained complete same-step record replay; repaired auditor module-name collision before reception/geometry checks.'
    def save(): DEST.write_text(json.dumps(cert,indent=2)+'\n')
    save()
    try:
        old=json.loads((OUT/'certificate-192-summary.json').read_text())
        new=json.loads((OUT/'certificate-194.json').read_text())
        constants={'L':0,'native':{'D':0,'S':0},'not-or':{'D':0,'S':0}}
        library_names=1
        for name,goal in ([] if finish else ep.fixed().items()):
            saved=new['library'][name]
            result=scan(ROOT/saved['native']['path'],ep.c.serialize(goal),ROOT/saved['not-or']['path'])
            # Cross-check the second implementation against the existing full
            # primitive checker on all fourteen fixed laws in both formats.
            for mode,measurement in result['measurements'].items():
                existing=ep.c.check(ROOT/measurement['path'],syntax.text(syntax.parse(ep.c.serialize(goal)),mode=='not-or'))
                same_measurement(measurement,existing); same_measurement(measurement,saved[mode])
                constants[mode]['D']=max(constants[mode]['D'],measurement['max_line_depth'])
                constants[mode]['S']=max(constants[mode]['S'],measurement['max_record_nodes'])
            constants['L']=max(constants['L'],len(result['rows']))
            library_names=max(library_names,result['name_bytes'])
            cert['library'][name]=result['measurements']; save()
        if finish: constants=cert['constants']
        assert constants==new['constants']==old['constants']
        cert['constants']=constants
        print('library: 28 full streams, literal pairs and two checkers agree',flush=True)
        for case in ([] if finish else old['cases']+new['cases']):
            d=json.loads((ROOT/case['request']).read_text()); ends=ep.strings(d)
            inputs=[]; imports=[]; offset=0
            for i,(path,goal) in enumerate(zip(case['input_paths'],ends['coordinates']+ends['next'])):
                data=scan(ROOT/path,goal)
                count=len(data['rows']); saved=case['imports'][i]
                assert saved=={'label':('coordinate-'+str(i) if i<d['N'] else 'next-'+str(i-d['N'])),
                               'start':offset,'lines':count,'root':offset+count-1}
                inputs.append(data); imports.append((ROOT/path,count)); offset+=count
            assert len(inputs)==d['N']+d['k']
            actual=scan(ROOT/case['proofs']['native']['measurement']['path'],ends['goals'][-1],
                        ROOT/case['proofs']['not-or']['measurement']['path'],
                        dict(zip(case['required_roots'],ends['goals'])),imports)
            assert case['required_roots'][-1]==len(actual['rows'])-1
            ub=ledger.thresholds(d,inputs,constants,{m:term_stats(d,m) for m in ('native','not-or')},library_names)
            independently=independent_bound(d,inputs,constants,library_names)
            if 'uniform_ledger' in case: assert case['uniform_ledger']==ub
            checks={}
            for mode,measurement in actual['measurements'].items():
                same_measurement(measurement,case['proofs'][mode]['measurement'])
                assert independently[mode]=={k:ub['formats'][mode][k] for k in independently[mode]}
                checks[mode]=ledger.check(measurement,ub['formats'][mode])
                print(case['name'],mode,'lines',measurement['lines'],'/',ub['lines'],
                      'depth',measurement['max_line_depth'],'/',ub['formats'][mode]['depth'],
                      'bytes',measurement['bytes'],'/',ub['formats'][mode]['bytes'],flush=True)
            selected=sorted({j for table in d['T'] for j,bit in enumerate(table[0]) if bit})
            used=ancestors(actual['references'],case['required_roots'][2])
            nextroots=[case['imports'][d['N']+j]['root'] for j in selected]
            assert all(root in used for root in nextroots), 'selected next-row premise unused'
            cert['cases'].append({'name':case['name'],'measurements':actual['measurements'],
                'input_measurements':[p['measurements']['native'] for p in inputs],
                'uniform_ledger':ub,'uniform_checks':checks,'full_imports':True,
                'all_four_endpoints':True,'literal_image_every_record':True,
                'selected_next_rows':selected,'selected_roots_in_Q8_zero_ancestry':nextroots})
            save()
        # Reception negatives use the actual receiver, but never synthesize.
        import build as b
        base=next(a for a in old['cases'] if a['name']=='small-cancellation')
        d=json.loads((ROOT/base['request']).read_text())
        paths=[ROOT/a for a in base['input_paths'][:d['N']]]
        nxt=[ROOT/a for a in base['input_paths'][d['N']:]]
        mutations={'r-beta':lambda a:a['beta'].__setitem__(0,[1]),
                   'matrix-identity':lambda a:a['G'][0][0].__setitem__(0,1-a['G'][0][0][0]),
                   'dimension':lambda a:a['G'][0][0].append(0),
                   'non-bit':lambda a:a['G'][0][0].__setitem__(0,2)}
        for item in old['corruptions']:
            dd=copy.deepcopy(d); ps=list(paths); ns=list(nxt); name=item['name']
            if name in mutations: mutations[name](dd)
            elif name=='missing-coordinate': ps=ps[:-1]
            elif name=='missing-next-row': ns=ns[:-1]
            elif name=='next-endpoint': ns[0]=ROOT/item['path']
            else: ps[0]=ROOT/item['path']
            try: b.compile_one(dd,ps,ns,{})
            except (ValueError, b.checker.Invalid, b.ep.c.Invalid) as err:
                assert str(err)==item['reason'],(name,str(err),item['reason'])
                cert['corruptions'].append({'name':name,'rejected':True,'reason':str(err)})
            else: raise AssertionError('malformed reception accepted')
        import check_geometry as geometry
        saved=json.loads((OUT/'geometry-193.json').read_text())
        def decode(t):
            return b.atom((1,t),'v'+str(t)) if isinstance(t,int) else b.X(*(decode(a) for a in t))
        for case in saved['cases']:
            source=decode(case['source'])
            replay=(geometry.single(source,case['cut']) if case['kind']=='single'
                    else geometry.match(source,decode(case['target'])))
            assert replay==case, 'complete geometry trace mismatch'
        cert['geometry']={'cases':len(saved['cases']),
                          'rotations':sum(len(a['events']) for a in saved['cases']),
                          'all_records_replayed':True}
        cert['complete']=True; save()
        print('complete:',len(cert['cases'])*2,'transition streams;',len(cert['corruptions']),
              'rejections; geometry',cert['geometry'],'failures',cert['failures'],'path',DEST.relative_to(ROOT),flush=True)
    except Exception as err:
        cert['failures'].append({'type':type(err).__name__,'message':str(err)})
        save(); raise


if __name__=='__main__': main()
