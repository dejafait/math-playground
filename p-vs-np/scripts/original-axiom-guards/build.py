"""Paid fixed strings and actual-tree conjunction projections."""
import itertools
import sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'balanced-coordinate'))
import aggregate
# aggregate imports its own endpoints module; load our independent module explicitly.
import importlib.util
spec=importlib.util.spec_from_file_location('guard_endpoints',HERE/'endpoints.py')
ep=importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
p,checker=aggregate.primitive,aggregate.checker
def P(a,b): return p.N(p.I(a,p.N(b)))
def OR(a,b): return p.I(p.N(a),b)
def fold(items,shape,op):
    if len(items)==1: return items[0]
    if len(items)==2: return op(*items)
    return op(op(items[0],items[1]),items[2]) if shape=='left' else op(items[0],op(items[1],items[2]))
def schemas():
    a,b,c='A','B','C'; t=p.I('q','q'); z=p.N(t)
    out={'id':p.I(a,a),'projection-left':p.I(P(a,b),a),'projection-right':p.I(P(a,b),b),
         'syl':p.I(p.I(a,b),p.I(p.I(b,c),p.I(a,c))),
         'boolean':p.E(p.X(P(a,a),a),z),
         'commutator':p.E(p.X(P(a,b),P(b,a)),z)}
    for arity in (1,2,3):
        for signs in itertools.product((False,True),repeat=arity):
            for shape in (('left','right') if arity==3 else ('left',)):
                vs=[a,b,c][:arity]
                lits=[p.N(v) if s else v for v,s in zip(vs,signs)]
                fs=[v if s else p.X(t,v) for v,s in zip(vs,signs)]
                key='clause-'+''.join('n' if s else 'p' for s in signs)+'-'+shape
                out[key]=p.I(fold(lits,shape,OR),p.E(fold(fs,shape,P),z))
    return out
def store(library):
    o=aggregate.Combination.__new__(aggregate.Combination)
    o.p=aggregate.AppendProof(); o.library=library; return o
def compile_one(data,index,library):
    g,terms,evals,paths=ep.request(data)
    g=aggregate.native(g); value=aggregate.native(evals[index]); z=p.N(p.I(data['q'],data['q']))
    o=store(library); m=len(terms); ds=data['dictionary']
    if index<m:
        current=g; root=o.use('id',{'A':g})
        for side in paths[index]:
            # The conjunction expansion is NOT(left -> NOT right).
            left,right=current[1][1],current[1][2][1]
            child=left if side=='left' else right
            projection=o.use('projection-'+side,{'A':left,'B':right})
            syl=o.use('syl',{'A':g,'B':current,'C':child})
            root=o.p.mp(projection,o.p.mp(root,syl)); current=child
        c=data['clauses'][index]; _,_,occ=ep.clause(c)
        shape='left' if len(occ)!=3 or c['left'].get('op')=='or' else 'right'
        key='clause-'+''.join('n' if t['negative'] else 'p' for t in occ)+'-'+shape
        env={k:t['var'] for k,t in zip(['A','B','C'],occ)}; env['q']=data['q']
        law=o.use(key,env)
        target=p.E(value,z)
        assert o.p.rows[law][0]==p.I(current,target)
        syl=o.use('syl',{'A':g,'B':current,'C':target})
        o.root=o.p.mp(law,o.p.mp(root,syl))
    else:
        if index<m+len(ds):
            key='boolean'; env={'A':ds[index-m],'q':data['q']}
        else:
            pairs=list(itertools.combinations(ds,2)); a,b=pairs[index-m-len(ds)]
            key='commutator'; env={'A':a,'B':b,'q':data['q']}
        law=o.use(key,env); target=p.E(value,z)
        assert o.p.rows[law][0]==target
        o.root=o.p.mp(law,o.p.ax('ax1',target,g))
    assert p.text(o.p.rows[o.root][0])==ep.goals(data)[index]
    assert o.root==len(o.p.rows)-1
    return o
