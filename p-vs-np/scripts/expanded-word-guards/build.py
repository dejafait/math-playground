"""Finite bridges and complete append-only guard import/composition."""
import importlib.util
import itertools
from pathlib import Path
HERE=Path(__file__).resolve().parent

def module(name,path):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
base=module('factored_build',HERE.parent/'original-axiom-guards'/'build.py')
ep=module('expanded_endpoints',HERE/'endpoints.py')
p,aggregate,checker=base.p,base.aggregate,base.checker

def word(w):
    if not w: return p.I('q','q')
    t=w[0]
    for a in w[1:]: t=base.P(t,a)
    return t

def summation(ws):
    if len(ws)==1: return word(ws[0])
    k=len(ws)//2
    return p.X(summation(ws[:k]),summation(ws[k:]))

def schemas():
    out={'guard-compose':p.I(p.I('G',p.E('A','D')),p.I(p.E('A','B'),p.I('G',p.E('B','D')))),
         'refl':p.E('A','A')}
    for arity in (1,2,3):
        vs=['A','B','C'][:arity]
        for signs in itertools.product((False,True),repeat=arity):
            choices=[[[a]] if s else [[],[a]] for a,s in zip(vs,signs)]
            ws=[sum(parts,[]) for parts in itertools.product(*choices)]
            fs=[a if s else p.X(p.I('q','q'),a) for a,s in zip(vs,signs)]
            for shape in (('left','right') if arity==3 else ('left',)):
                key='bridge-'+''.join('n' if s else 'p' for s in signs)+'-'+shape
                out[key]=p.E(base.fold(fs,shape,base.P),summation(ws))
    return out

def compile_one(data,index,guard_path,library):
    g,fs,es=ep.request(data); fact=data['factored']
    expected=ep.f.goals(fact)[index]
    imported=aggregate.load(guard_path,expected)
    o=base.store(library); root=o.copy(imported['rows'],{})
    import_end=len(o.p.rows)
    if index<len(fact['clauses']):
        c=fact['clauses'][index]; occ=ep.f.clause(c)[2]
        shape='left' if len(occ)!=3 or c['left'].get('op')=='or' else 'right'
        key='bridge-'+''.join('n' if a['negative'] else 'p' for a in occ)+'-'+shape
        env={a:b['var'] for a,b in zip(['A','B','C'],occ)}; env['q']=fact['q']
        bridge=o.use(key,env)
    else:
        assert fs[index]==es[index]
        bridge=o.use('refl',{'A':aggregate.native(fs[index])})
    assert p.text(o.p.rows[bridge][0])==ep.bridges(data)[index]
    law=o.use('guard-compose',{'G':aggregate.native(g),'A':aggregate.native(fs[index]),
                             'B':aggregate.native(es[index]),'D':p.N(p.I(fact['q'],fact['q']))})
    o.root=o.p.mp(bridge,o.p.mp(root,law))
    assert o.root==len(o.p.rows)-1 and p.text(o.p.rows[o.root][0])==ep.goals(data)[index]
    return o,imported,import_end
