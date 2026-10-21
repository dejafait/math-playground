"""Step 174: read complete saved evidence, never regenerate old archives."""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SLOT = HERE.parent / 'balanced-slot'
sys.path.insert(0, str(SLOT))
import checker
import endpoints

OUT = HERE / 'output'
DEST = OUT / 'audit-174.json'

def main():
    saved = json.loads((OUT / 'certificate-172.json').read_text())
    result = dict(complete=False, failures=[], library={}, cases=[], corruptions=[])
    def save(): DEST.write_text(json.dumps(result, indent=2)+'\n')
    def require(ok, label):
        if not ok:
            result['failures'].append(label)
            save()
            raise AssertionError(label)
    save()
    try:
        require(saved['complete'] and not saved['failures'], 'prior completion')
        n, i, x, e, p = endpoints.n, endpoints.i, endpoints.x, endpoints.e, endpoints.p
        a,b,c = 'A','B','C'
        goals = dict(trans=i(e(a,b),i(e(b,c),e(a,c))),
                     congL=i(e(a,b),e(x(a,c),x(b,c))),
                     congR=i(e(a,b),e(x(c,a),x(c,b))),
                     refl=e(a,a), symm=i(e(a,b),e(b,a)),
                     dist=e(p(a,x(b,c)),x(p(a,b),p(a,c))),
                     prod_cong=i(e(b,c),e(p(a,b),p(a,c))))
        for name, goal in goals.items():
            result['library'][name] = {}
            for mode in ('native','not-or'):
                path = (OUT if name in ('dist','prod_cong') else SLOT/'output') / (name+'.'+mode+'.jsonl.gz')
                measured = checker.check(path, endpoints.encode(goal, mode))
                require(measured == saved['library'][name][mode], name+' '+mode+' full measurement/hash')
                result['library'][name][mode] = measured
                save()
            print('fixed', name, 'both complete streams accepted', flush=True)
        const = {'L': max(v['native']['lines'] for v in result['library'].values())}
        for mode in ('native','not-or'):
            values = [v[mode] for v in result['library'].values()]
            const[mode] = dict(D=max(v['max_line_depth'] for v in values),
                               S=max(v['max_record_nodes'] for v in values))
        require(const == saved['constants'] == {'L':2706,'native':{'D':18,'S':2040},
                    'not-or':{'D':24,'S':2712}}, 'selected constants')
        result['constants'] = const

        for case in saved['cases']:
            name = case['name']
            ts = [checker.parse(t,'native')[0] for t in case['slots']]
            factor = checker.parse(case['factor'],'native')[0]
            m = len(ts); h = m.bit_length()-1; H = h+1
            require(m == 2**h and h >= 1 and case['M'] == m and case['h'] == h, name+' request')
            # Tagged leaves keep opaque supplied terms distinct from skeleton X/P.
            def bal(seq):
                if len(seq)==1: return ('leaf',seq[0])
                k=len(seq)//2
                return ('X',bal(seq[:k]),bal(seq[k:]))
            def expand(t):
                if t[0]=='leaf': return t[1]
                return (x if t[0]=='X' else p)(expand(t[1]),expand(t[2]))
            def height(t):
                return 0 if t[0]=='leaf' else 1+max(height(t[1]),height(t[2]))
            def get(t,path):
                for k in path: t=t[k]
                return t
            def put(t,path,new):
                if not path: return new
                k=path[0]
                return (t[0],put(t[1],path[1:],new),t[2]) if k==1 else (t[0],t[1],put(t[2],path[1:],new))
            tree=('P',('leaf',factor),bal(ts)); initial=tree
            trace=json.loads((OUT/(name+'.trace.json')).read_text())
            require(trace['case']==case, name+' trace request/certificate')
            paths=[]
            def preorder(path,depth):
                if depth==h: return
                paths.append(list(path)); preorder(path+[1],depth+1); preorder(path+[2],depth+1)
            preorder([],0)
            require([ev['path'] for ev in trace['events']]==paths, name+' complete event order')
            args=[expand(initial)]
            checks=[]
            for ev in trace['events']:
                path=ev['path']; local=get(tree,path)
                require(local[0]=='P' and local[2][0]=='X',name+' pending product')
                aa=local[1]; bb,cc=local[2][1:]
                new=('X',('P',aa,bb),('P',aa,cc))
                args.extend(map(expand,(aa,bb,cc)))
                oldsub=local; newsub=new
                for length in range(len(path),0,-1):
                    parent=get(tree,path[:length-1]); side=path[length-1]
                    require(parent[0]=='X',name+' XOR ancestor')
                    sibling=parent[3-side]
                    args.extend(map(expand,(oldsub,newsub,sibling)))
                    oldsub=parent
                    newsub=('X',newsub,sibling) if side==1 else ('X',sibling,newsub)
                nxt=put(tree,path,new)
                require(nxt==newsub,name+' context result')
                args.extend(map(expand,(initial,tree,nxt)))
                require(ev['before']==checker.serialize(expand(tree)) and
                        ev['after']==checker.serialize(expand(nxt)),name+' complete before/after')
                require(ev['lifts']==len(path)<=h-1 and ev['height']==height(nxt)<=H,name+' geometry')
                checks.append(dict(path=path,lifts=ev['lifts'],height=ev['height']))
                tree=nxt
            expected_native=endpoints.goal(case['factor'],case['slots'],'native')
            require(checker.serialize(e(expand(initial),expand(tree)))==expected_native,name+' trace endpoint')
            require(len(checks)==case['events']==case['required_events']==m-1 and
                    max(v['height'] for v in checks)==case['max_height'] and
                    case['required_height_max']==H,name+' event summary')
            record=dict(name=name,events=checks,proofs={})
            for mode in ('native','not-or'):
                expected=endpoints.goal(case['factor'],case['slots'],mode)
                old=case['proofs'][mode]
                require(expected==old['expected_goal'],name+' saved endpoint '+mode)
                measured=checker.check(OUT/(name+'.'+mode+'.jsonl.gz'),expected)
                require(measured==old['measurement'],name+' measurement/hash '+mode)
                stats=[checker.parse(endpoints.encode(t,mode),mode)[1:] for t in [factor]+ts]
                tmax=max(v[0] for v in stats); dmax=max(v[1] for v in stats)
                def variables(t):
                    return {t} if isinstance(t,str) else set().union(*(variables(v) for v in t[1:]))
                names={'A','B','C'}|set().union(*(variables(t) for t in [factor]+ts))
                B=max(len(s.encode('ascii')) for s in names)
                L=const['L']; J=L+(m-1)*(h+1)*(L+2); P=128*m*m*(tmax+1); S=const[mode]['S']
                # Integer ceil(log2(J+2)), no floating rounding.
                bound=dict(lines=J,depth=const[mode]['D']+(3 if mode=='native' else 6)*H+dmax,
                           record_nodes=S*P,bytes=(J+2)*((B+4)*S*P+256+64*(J+1).bit_length()),
                           argument_nodes=P,term_nodes=tmax,term_depth=dmax,name_bytes=B)
                bound['bits']=8*bound['bytes']
                require(bound==old['bounds'],name+' recomputed bounds '+mode)
                actual_args=[checker.parse(endpoints.encode(t,mode),mode)[1:] for t in args]
                argcheck=dict(count=len(args),max_nodes=max(v[0] for v in actual_args),
                              required_nodes=P,max_depth=max(v[1] for v in actual_args),
                              required_depth=(3 if mode=='native' else 6)*H+dmax)
                require(argcheck['max_nodes']<=P and argcheck['max_depth']<=argcheck['required_depth'],name+' all actual arguments')
                pairs={key:dict(actual=measured[field],required=bound[key]) for key,field in
                       [('lines','lines'),('depth','max_line_depth'),('record_nodes','max_record_nodes'),('bytes','bytes')]}
                require(all(v['actual']<=v['required'] for v in pairs.values()),name+' ledger '+mode)
                require(old['bound_tests']=={key:True for key in pairs},name+' saved bound tests')
                record['proofs'][mode]=dict(measurement=measured,bounds=bound,checks=pairs,arguments=argcheck)
                result['cases']=[v for v in result['cases'] if v['name']!=name]+[record]
                save()
                print(name,mode,'accepted actual/required',pairs,'certificate',DEST.relative_to(ROOT),flush=True)
        require({c['name'] for c in result['cases']}=={'m2-variable','m4-composite','m8-composite'},'all cases')
        small=next(c for c in saved['cases'] if c['name']=='m2-variable')
        for mode, entries in saved['corruptions'].items():
            goal=endpoints.goal(small['factor'],small['slots'],mode)
            for old in entries:
                try: checker.check(ROOT/old['path'],goal)
                except checker.Invalid as err:
                    require(old['rejected'] and str(err)==old['reason'],'corruption saved reason')
                    result['corruptions'].append(dict(path=old['path'],rejected=True,reason=str(err)))
                else: require(False,'accepted corruption '+old['path'])
        require(len(result['corruptions'])==8,'eight corruptions')
        result['code_sha256']={str(path.relative_to(ROOT)):hashlib.sha256(path.read_bytes()).hexdigest()
            for path in [Path(__file__),HERE/'run_suite.py',HERE/'endpoints.py',SLOT/'checker.py',SLOT/'compiler.py']}
        result['complete']=True; save()
        print('Complete: 14 fixed, 6 growing, 3 full traces; 8 corruptions rejected; failures',result['failures'],
              'certificate',DEST.relative_to(ROOT),flush=True)
    except Exception as err:
        result['failures'].append(type(err).__name__+': '+str(err)); save(); raise

if __name__=='__main__': main()
