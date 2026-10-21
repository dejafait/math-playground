"""Complete bounded transition streams, input fixtures, rejection evidence."""
import copy
import gzip
import json
import math
import argparse
from pathlib import Path
import build as b
ep,p,c=b.ep,b.p,b.checker
HERE=Path(__file__).resolve().parent
OUT=HERE/'output'
ROOT=HERE.parents[1]

def save(path,obj): path.write_text(json.dumps(obj,indent=2)+'\n')
def fixture_write(o,root,path,extra=()):
    # This creates a test input from a newly synthesized derivation; it does
    # not prune any received package. Retain selected unused test axioms too.
    order=sorted(set(o.p.reachable(root))|set(extra))
    fresh=b.Store(o.library,o.q); moved={}
    for i in order:
        f,rule,refs,subs,deps=o.p.rows[i]
        if rule=='mp': j=fresh.p.mp(*(moved[a] for a in refs))
        else: j=fresh.p.ax(rule,subs['A'],subs['B'],subs.get('C'))
        if fresh.p.rows[j][0]!=f: raise AssertionError('fixture construction changed a record')
        moved[i]=j
    fresh.root=moved[root]
    if fresh.root!=len(fresh.p.rows)-1: raise AssertionError('fixture last record')
    return fresh.write(path)
def library(cert):
    lib={}; allfixed=ep.fixed()
    for name,goal in allfixed.items():
        if name in ('zeroR','zeroL','prod_zero'):
            path=OUT/(name+'.native.jsonl.gz')
            if not path.exists():
                synth=p.Proof(); synth.build_helpers()
                root=synth.prove_fixed(b.aggregate.native(goal))
                for image,mode in ((False,'native'),(True,'not-or')):
                    synth.write(root,OUT/(name+'.'+mode+'.jsonl.gz'),image)
            location=OUT
        else:
            location=HERE.parent/('balanced-distribution' if name in ('dist','prod_cong') else 'balanced-slot')/'output'
        checks={}
        for mode in ('native','not-or'):
            path=location/(name+'.'+mode+'.jsonl.gz')
            checks[mode]=c.check(path,ep.c.serialize(ep.image(goal) if mode=='not-or' else goal))
        lib[name]=b.aggregate.load(location/(name+'.native.jsonl.gz'),ep.c.serialize(goal))
        cert['library'][name]=checks
        print('fixed',name,'both formats checked;',checks['native']['lines'],'lines',flush=True)
    constants={'L':max(a['native']['lines'] for a in cert['library'].values())}
    for mode in ('native','not-or'):
        constants[mode]={'D':max(a[mode]['max_line_depth'] for a in cert['library'].values()),
                         'S':max(a[mode]['max_record_nodes'] for a in cert['library'].values())}
    cert['constants']=constants
    return lib

def request(N=2,n=1,k=0,q='q',r=None,beta=None,G=None,R=None,T=None,suffixes=None,letters=None):
    z=p.N(p.I(q,q)); y=p.I(q,q)
    beta=beta or [0]*N
    return {'N':N,'n':n,'k':k,'q':q,
            'suffixes':suffixes or [p.text(y if bit else z) for bit in beta],
            'letters':letters or ['x'+str(a) for a in range(n)],
            'beta':[[a] for a in beta],'r':[r if r is not None else [1]+[0]*(N-1)],
            'G':G if G is not None else [[[0]*N for _ in range(N)] for _ in range(n)],
            'R_next':R if R is not None else [[0]*N for _ in range(k)],
            'T':T if T is not None else [[[0]*k] for _ in range(n)]}

def fixtures(d,name,lib,deep=False):
    """Test-only supplied records from explicit scalar equivalence seeds.

    No general coordinate proof finder is asserted. All G rows and next rows
    in these fixtures annihilate beta. Suffixes are literal constants or one
    repeated-term cancellation, with known paid seeds.
    """
    expected=ep.strings(d); o=b.Store(lib,d['q']); q=d['q']
    z=b.atom((9,),p.N(p.I(q,q))); y=b.atom((0,),p.I(q,q))
    S=[b.atom((1,v),b.aggregate.native(ep.c.parse(s,'native')[0])) for v,s in enumerate(d['suffixes'])]
    scalars=[y if row[0] else z for row in d['beta']]
    xs=[b.atom((3,v),name) for v,name in enumerate(d['letters'])]
    seeds=[]
    for sv,scalar in zip(S,scalars):
        if b.nt(sv)==b.nt(scalar): seeds.append(o.refl(sv))
        elif b.nt(sv)==p.X('A','A') and scalar==z:
            seeds.append(o.use('cancel',{'A':'A'}))
        else: raise c.Invalid('test fixture suffix outside explicit seeds')
    def rowsum(row):
        indices=[v for v,a in enumerate(row) if a]
        a,mid,j=b.combine(o,[S[v] for v in indices],[scalars[v] for v in indices],[seeds[v] for v in indices],z)
        out,k,tr=b.normalize(o,mid,z)
        if out!=z: raise c.Invalid('test fixture row is not scalar zero')
        return a,o.trans(a,mid,z,j,k)
    coord=[]; nxt=[]; unused=[]
    for v in range(d['N']):
        start=len(o.p.rows)
        if deep and v==0:
            dterm='deep_unused'
            for _ in range(35): dterm=p.N(dterm)
            unused.append(o.p.ax('ax1',dterm,'A'))
        terms=[]; refs=[]
        for letter in range(d['n']):
            a,j=rowsum(d['G'][letter][v]); pa,pz=b.product(xs[letter],a),b.product(xs[letter],z)
            j=o.product_congr(xs[letter],a,z,j)
            j=o.trans(pa,pz,z,j,o.law('prod_zero',{'A':xs[letter]}))
            terms.append(pa); refs.append(j)
        a,zeros,j=b.combine(o,terms,[z]*len(terms),refs,z)
        out,k=b.erase_zeros(o,zeros,z)
        j=o.trans(a,zeros,z,j,k)
        rhs=b.X(scalars[v],a); mid=b.X(scalars[v],z)
        lift=o.p.mp(j,o.law('congR',{'A':a,'B':z,'C':scalars[v]}))
        j=o.trans(rhs,mid,scalars[v],lift,o.law('zeroR',{'A':scalars[v]}))
        root=o.trans(S[v],scalars[v],rhs,seeds[v],o.symm(rhs,scalars[v],j))
        # Package all earlier fixture records, including the unused deep one.
        o.root=root
        path=OUT/(name+'-coordinate-'+str(v)+'.native.jsonl.gz')
        fixture_write(o,root,path,unused); c.check(path,expected['coordinates'][v]); coord.append(path)
    for j,row in enumerate(d['R_next']):
        a,root=rowsum(row); o.root=root
        path=OUT/(name+'-next-'+str(j)+'.native.jsonl.gz')
        fixture_write(o,root,path,unused); c.check(path,expected['next'][j]); nxt.append(path)
    return coord,nxt

def measured_terms(d,mode):
    trees=[ep.c.parse(a,'native')[0] for a in d['suffixes']+d['letters']]
    trees += [ep.imp(d['q'],d['q']),ep.neg(ep.imp(d['q'],d['q']))]
    if mode=='not-or': trees=[ep.image(t) for t in trees]
    stats=[b.aggregate.endpoints.stats(t) for t in trees]
    return max(a[0] for a in stats),max(a[1] for a in stats),max(a[2] for a in stats)

def run_case(name,d,lib,cert,deep=False,uniform=False):
    save(OUT/(name+'.request.json'),d)
    paths,nxt=fixtures(d,name,lib,deep)
    obj=b.compile_one(d,paths,nxt,lib)
    expected=ep.strings(d); actualmax=max([a['max_height'] for a in obj.traces]+[0])
    data={'name':name,'request':str((OUT/(name+'.request.json')).relative_to(ROOT)),
          'input_paths':[str(a.relative_to(ROOT)) for a in paths+nxt],
          'required_roots':obj.required_roots,'imports':obj.imports,'proofs':{},
          'normalizations':obj.traces,'max_argument_height':obj.max_argument_height,
          'max_normalization_height':actualmax,'table_checks':True,'full_import_retention':True,
          'all_size_ledger_status':'NOT_ESTABLISHED'}
    if uniform:
        import ledger
        data['uniform_ledger'] = ledger.thresholds(
            d, obj.packages, cert['constants'],
            {mode:measured_terms(d,mode) for mode in ('native','not-or')},
            max(a['name_bytes'] for a in lib.values()))
        if max(obj.max_argument_height,actualmax)>data['uniform_ledger']['H']:
            raise AssertionError('L062 skeleton-height threshold failed')
        data['all_size_ledger_status']='L062_INFORMAL_BOUND_INSTRUMENTED_AUDIT_PENDING'
    # The following are finite exact-copy thresholds, not an all-size theorem.
    # Imported records stay unchanged. Each copied template has node bound
    # S*largest actual argument; every external MP is its subformula.
    for mode,image in (('native',False),('not-or',True)):
        path=OUT/(name+'.'+mode+'.jsonl.gz')
        writer=obj.write(path,image)
        check=c.check(path,ep.strings(d,mode)['goals'][-1])
        if any(writer[key]!=check[key] for key in ('bytes','lines','sha256')): raise AssertionError('writer/checker mismatch')
        maxima=[(0,0,0)]
        for call in obj.calls:
            for text in call['arguments'].values():
                tree=ep.c.parse(text,'native')[0]
                if image: tree=ep.image(tree)
                maxima.append(b.aggregate.endpoints.stats(tree))
        A=max(t[0] for t in maxima); ad=max(t[1] for t in maxima); B=max([t[2] for t in maxima]+[a['name_bytes'] for a in obj.packages])
        K=sum(a['node_sums'][mode] for a in obj.packages); delta=max([a['depths'][mode] for a in obj.packages]+[0])
        D,S=cert['constants'][mode]['D'],cert['constants'][mode]['S']
        imported=sum(len(a['rows']) for a in obj.packages)
        copies=sum(cert['library'][a['name']]['native']['lines'] for a in obj.calls)
        mp=len(obj.p.rows)-imported-copies
        J=imported+copies+mp
        bounds={'lines':J,'depth':max(delta,D+ad),'record_nodes':max(K,S*max(1,A)),
                'bytes':(B+4)*(K+(copies+mp+1)*S*max(1,A))+(J+2)*(256+64*math.ceil(math.log2(J+2))),
                'basis':'exact finite event/copy measurements; not input-independent all-size bounds'}
        passbounds=check['lines']<=bounds['lines'] and check['max_line_depth']<=bounds['depth'] and check['max_record_nodes']<=bounds['record_nodes'] and check['bytes']<=bounds['bytes']
        if not passbounds: raise AssertionError('finite copying threshold failed')
        # Read the ENTIRE stream and verify the three earlier requested lines,
        # plus last record, independently of the planner's tree annotations.
        seen={}
        with gzip.open(path,'rt') as f:
            next(f)
            for i,line in enumerate(f):
                if i in obj.required_roots: seen[i]=json.loads(line)['f']
        if [seen[i] for i in obj.required_roots]!=ep.strings(d,mode)['goals']: raise AssertionError('intermediate endpoints failed')
        data['proofs'][mode]={'measurement':check,'bounds':bounds,'finite_bounds_pass':True,'all_requested_records_pass':True}
        if uniform:
            ub=data['uniform_ledger']['formats'][mode]
            data['proofs'][mode]['uniform_bounds']=ub
            data['proofs'][mode]['uniform_checks']=ledger.check(check,ub)
            data['proofs'][mode]['uniform_bounds_pass']=True
            if A>ub['argument_nodes'] or ad>ub['argument_depth']:
                raise AssertionError('L062 argument threshold failed')
            print(name,mode,'uniform actual/required: lines',check['lines'],'/',ub['lines'],
                  'bytes',check['bytes'],'/',ub['bytes'],
                  'depth',check['max_line_depth'],'/',ub['depth'],
                  'record nodes',check['max_record_nodes'],'/',ub['record_nodes'],flush=True)
        print(name,mode,'lines',check['lines'],'bytes',check['bytes'],'depth',check['max_line_depth'],'/',bounds['depth'],flush=True)
    save(OUT/(name+'.trace.json'),{'calls':obj.calls,'normalizations':obj.traces,'imports':obj.imports,'required_roots':obj.required_roots})
    cert['cases'].append(data)
    return paths,nxt

def bad_inputs(d,paths,nxt,lib):
    out=[]
    def reject(label,data,ps,ns):
        try: b.compile_one(data,ps,ns,lib)
        except (c.Invalid,ep.c.Invalid) as e: out.append({'name':label,'rejected':True,'reason':str(e)})
        else: raise AssertionError('malformed input accepted: '+label)
    for label,change in [('r-beta',lambda a:a['beta'].__setitem__(0,[1])),
                         ('matrix-identity',lambda a:a['G'][0][0].__setitem__(0,1-a['G'][0][0][0])),
                         ('dimension',lambda a:a['G'][0][0].append(0)),
                         ('non-bit',lambda a:a['G'][0][0].__setitem__(0,2))]:
        a=copy.deepcopy(d); change(a); reject(label,a,paths,nxt)
    reject('missing-coordinate',d,paths[:-1],nxt)
    reject('missing-next-row',d,paths,nxt[:-1])
    with gzip.open(paths[0],'rt') as f: lines=[json.loads(a) for a in f]
    mp=next(i for i,a in enumerate(lines[1:],1) if a['rule']=='mp')
    ax=next(i for i,a in enumerate(lines[1:],1) if a['rule']!='mp')
    different=next(j for j in range(1,mp) if lines[j]['f']!=lines[1+lines[mp]['refs'][0]]['f'])
    mods=[('endpoint',0,dict(lines[0],goal='BAD_ENDPOINT')),
          ('assumption',ax,{'f':lines[ax]['f'],'rule':'assume'}),
          ('axiom-substitution',ax,dict(lines[ax],subs=dict(lines[ax]['subs'],A='BAD_SUB'))),
          ('forward-reference',mp,dict(lines[mp],refs=[0,len(lines)])),
          ('mp-antecedent',mp,dict(lines[mp],refs=[different-1,lines[mp]['refs'][1]])),
          ('image-header',0,dict(lines[0],format='not-or'))]
    for label,i,row in mods:
        rows=list(lines); rows[i]=row
        path=OUT/('corrupt-'+label+'.native.jsonl.gz')
        with gzip.open(path,'wt') as f:
            for item in rows: f.write(json.dumps(item,separators=(',',':'))+'\n')
        reject(label,d,[path]+paths[1:],nxt)
        out[-1]['path']=str(path.relative_to(ROOT))
    with gzip.open(nxt[0],'rt') as f: nextlines=[json.loads(a) for a in f]
    nextlines[0]['goal']='BAD_NEXT_ENDPOINT'
    path=OUT/'corrupt-next-endpoint.native.jsonl.gz'
    with gzip.open(path,'wt') as f:
        for item in nextlines: f.write(json.dumps(item,separators=(',',':'))+'\n')
    reject('next-endpoint',d,paths,[path]+nxt[1:]); out[-1]['path']=str(path.relative_to(ROOT))
    return out

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--case',default='all',choices=['all','empty-alphabet','zero-next-space','cancellation','small-cancellation','constant-parity','nonpower-selection','zero-row'])
    args=parser.parse_args(); OUT.mkdir(exist_ok=True)
    cert={'complete':False,'failures':[],'library':{},'cases':[],'corruptions':[],
          'all_size_ledger_status':'NOT_ESTABLISHED','target_complete':False}
    path=OUT/('certificate-192'+('' if args.case=='all' else '-'+args.case)+'.json'); save(path,cert)
    try:
        lib=library(cert); save(path,cert)
        cases=[('empty-alphabet',request(n=0)),
               ('zero-next-space',request()),
               ('cancellation',request(k=2,r=[1,1],G=[[[1,1],[1,1]]],R=[[1,1],[1,1]],T=[[[1,1]]],
                    suffixes=[p.text(p.X('A','A'))]*2,letters=['A'])),
               ('small-cancellation',request(k=1,q='A',r=[1,1],G=[[[1,0],[1,0]]],R=[[0,0]],T=[[[0]]],
                    suffixes=[p.text(p.X('A','A'))]*2,letters=['A'])),
               ('constant-parity',request(n=0,k=1,r=[1,1],beta=[1,1],R=[[1,1]])),
               ('nonpower-selection',request(N=3,n=0,k=1,r=[1,1,1],R=[[1,1,1]])),
               ('zero-row',request(k=1,r=[0,0],G=[[[1,1],[0,0]]],R=[[1,1]],T=[[[0]]]))]
        for name,d in cases:
            if args.case!='all' and name!=args.case: continue
            if args.case=='all' and name=='cancellation': continue  # Preserved interrupted larger fixture.
            paths,nxt=run_case(name,d,lib,cert,deep=name in ('cancellation','small-cancellation')); save(path,cert)
            if name in ('cancellation','small-cancellation'):
                cert['corruptions']=bad_inputs(d,paths,nxt,lib); save(path,cert)
                print('all malformed inputs rejected:',len(cert['corruptions']),flush=True)
        cert['complete']=True; save(path,cert)
        print('finite suite complete; all-size ledger and exact target remain unfinished:',str(path.relative_to(ROOT)),flush=True)
    except Exception as e:
        cert['failures'].append({'type':type(e).__name__,'message':str(e)}); save(path,cert); raise

if __name__=='__main__': main()
