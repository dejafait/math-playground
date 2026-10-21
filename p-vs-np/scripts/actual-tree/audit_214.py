"""Archive-only L066 audit. No actual-tree emitter or receiver execution."""
import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
import verify

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / 'output'
sys.path.insert(0, str(HERE.parent / 'backward-zero'))
spec = importlib.util.spec_from_file_location('audit214_scan', HERE.parent / 'backward-zero' / 'audit_archives.py')
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)
e, c = verify.e, verify.c
DEST = OUT / 'audit-214.json'


def compact(scan):
    return {k: v for k, v in scan.items() if k not in ('rows', 'references')}


def seeds():
    A, B, C = 'A', 'B', 'C'
    y = e.imp('q', 'q'); z = e.neg(y)
    E, X, P, I = e.eq, e.xor, e.prod, e.imp
    return dict(refl=E(A,A), symm=I(E(A,B),E(B,A)),
        trans=I(E(A,B),I(E(B,C),E(A,C))),
        congL=I(E(A,B),E(X(A,C),X(B,C))),
        congR=I(E(A,B),E(X(C,A),X(C,B))),
        zeroL=E(X(z,A),A), zeroR=E(X(A,z),A), prod_zero=E(P(A,z),z),
        prod_assoc=E(P(P(A,B),C),P(A,P(B,C))),
        right_dist=E(P(X(A,B),C),X(P(A,C),P(B,C))),
        unitL=E(P(y,A),A), unitR=E(P(A,y),A), zero_prodL=E(P(z,A),z))


def tree_size(t):
    if t[0] not in ('add', 'mul'): return 1, 0
    u,d = tree_size(t[1]); v,f = tree_size(t[2])
    return 1+u+v, 1+max(d,f)


def bound(source, packages, lib):
    U,d = tree_size(source['tree']); n = len(source['letters']); N = 2*U
    assert d <= 4*(U+1).bit_length()
    H = 2*d+(n+1).bit_length()+8
    T = 1000*(n+2); G = 2568*T
    I = sum(p['measurements']['native']['lines'] for p in packages)
    J = I+G; P = 48*4**(H+1)
    B = max([1,len(source['q'])]+[len(x) for x in source['letters']]+
            [p['name_bytes'] for p in packages]+[p['name_bytes'] for p in lib.values()])
    ans = dict(U=U,source_depth=d,N=N,n=n,H=H,operations=T,
               generated_records=G,argument_nodes=P,formats={})
    for mode,D,S,k in [('native',18,2040,3),('not-or',24,2712,6)]:
        K = sum(p['node_sums'][mode] for p in packages)
        delta = max([0]+[p['depths'][mode] for p in packages])
        bytes_ = (B+4)*(K+(G+1)*S*P)+(J+2)*(256+64*(J+1).bit_length())
        ans['formats'][mode] = dict(lines=J,depth=max(delta,D+k*H+3),
            record_nodes=max(K,S*P),bytes=bytes_,aggregate_bytes=N*bytes_,aggregate_bits=8*N*bytes_)
    return ans


def scan_pair(native, expected, image=None, imports=()):
    a.syntax = a.Syntax()
    return a.scan(native, expected, image, imports=imports)


def main():
    assert not DEST.exists(), 'preserve previous evidence'
    oldpath = OUT / 'certificate-212-complete.json'
    old = json.loads(oldpath.read_text())
    cert = dict(step=214,complete=False,failures=[],library={},inputs=[],cases=[],rejections=[],
                prior=str(oldpath.relative_to(ROOT)),prior_sha256=hashlib.sha256(oldpath.read_bytes()).hexdigest())
    def save(): DEST.write_text(json.dumps(cert,indent=2)+'\n')
    save()
    try:
        assert old['complete'] and old['failures']==[] and len(old['cases'])==6
        lib = {}
        for name,goal in seeds().items():
            saved = old['library'][name]
            got = scan_pair(ROOT/saved['native']['path'],c.serialize(goal),ROOT/saved['not-or']['path'])
            assert got['measurements']==saved
            lib[name] = compact(got); cert['library'][name] = compact(got); save()
        constants = {'L':max(p['measurements']['native']['lines'] for p in lib.values())}
        for mode in ('native','not-or'):
            constants[mode] = dict(D=max(p['depths'][mode] for p in lib.values()),
                S=max(p['measurements'][mode]['max_record_nodes'] for p in lib.values()))
        assert constants==old['constants']==dict(L=2567,native=dict(D=18,S=2040),**{'not-or':dict(D=24,S=2712)})
        cert['constants']=constants; save()
        packages=[]; imports=[]
        for index,depth in enumerate((0,35)):
            term='unused'
            for _ in range(depth): term=e.neg(term)
            path=OUT/('retained-'+str(index)+'.native.jsonl.gz')
            got=scan_pair(path,c.serialize(e.imp(term,term)))
            packages.append(compact(got)); imports.append((path,len(got['rows'])))
            cert['inputs'].append(compact(got)); save()
        for case in old['cases']:
            assert case['complete']
            inp=json.loads((ROOT/case['input']).read_text())
            goals=verify.contract(inp['source'],inp['edges'],inp['request'])
            required=bound(inp['source'],packages,lib)
            assert required==case['bounds'] and len(goals)==len(case['vertices'])
            record=dict(name=case['name'],input=case['input'],bounds=required,vertices=[],aggregate={},complete=False)
            cert['cases'].append(record); save()
            for v,saved in enumerate(case['vertices']):
                assert saved['v']==v
                modes=saved['measures']
                got=scan_pair(ROOT/modes['native']['path'],goals[v],ROOT/modes['not-or']['path'],imports)
                assert got['measurements']==modes
                assert saved['retained']==[dict(start=sum(k for _,k in imports[:i]),lines=count) for i,(_,count) in enumerate(imports)]
                for mode in modes:
                    m=got['measurements'][mode]; r=required['formats'][mode]
                    assert m['lines']<=r['lines'] and m['bytes']<=r['bytes']
                    assert got['depths'][mode]<=r['depth'] and m['max_record_nodes']<=r['record_nodes']
                record['vertices'].append(dict(v=v,case=saved['case'],full=compact(got),retention_checked=True))
                save()
                print(case['name'],v,'PASS complete pair',modes['native']['lines'],'records',flush=True)
            for mode in ('native','not-or'):
                actual=sum(v['full']['measurements'][mode]['bytes'] for v in record['vertices'])
                r=required['formats'][mode]['aggregate_bytes']
                record['aggregate'][mode]=dict(actual_bytes=actual,required_bytes=r,actual_bits=8*actual,required_bits=8*r)
                assert record['aggregate'][mode]==case['aggregate'][mode] and actual<=r
            record['complete']=True; save()
        source=json.loads((ROOT/old['cases'][4]['input']).read_text())
        edits=[('wrong-suffix',lambda g,d:d['suffixes'].__setitem__(0,'wrong')),
               ('wrong-constant',lambda g,d:d.__setitem__('q','wrong')),
               ('wrong-connector',lambda g,d:g[0].__setitem__('w',0)),
               ('duplicated-letter-position',lambda g,d:d['Eb'][1][1].__setitem__(2,1)),
               ('selected-order',lambda g,d:d['suffixes'].reverse())]
        for label,edit in edits:
            g,d=copy.deepcopy(source['edges']),copy.deepcopy(source['request']); edit(g,d)
            try: verify.contract(source['source'],g,d)
            except c.Invalid as error: cert['rejections'].append(dict(label=label,rejected=True,reason=str(error)))
            else: raise AssertionError('accepted '+label)
        case=old['cases'][3]; inp=json.loads((ROOT/case['input']).read_text())
        expected=verify.contract(inp['source'],inp['edges'],inp['request'])[0]
        native=ROOT/case['vertices'][0]['measures']['native']['path']
        for reject in old['rejections'][5:]:
            path=ROOT/reject['path']
            try:
                scan_pair(native,expected,path) if reject['label']=='literal-image-substitution' else scan_pair(path,expected)
            except (AssertionError,ValueError) as error:
                cert['rejections'].append(dict(label=reject['label'],path=reject['path'],rejected=True,reason=str(error)))
            else: raise AssertionError('accepted '+reject['label'])
        assert len(cert['rejections'])==8
        cert['complete']=True; save()
        print('PASS 13 fixed pairs, 24 full local pairs, 2 retained inputs, 8 rejections;',DEST.relative_to(ROOT),flush=True)
    except BaseException as error:
        cert['failures'].append(type(error).__name__+': '+str(error)); save(); raise


if __name__=='__main__': main()
