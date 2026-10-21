"""Exact occurrence-preserving receiving syntax; no emitter/planner imports."""
import importlib.util
import itertools
import json
from pathlib import Path
BASE=Path(__file__).resolve().parent.parent/'original-axiom-guards'
spec=importlib.util.spec_from_file_location('factored_endpoints',BASE/'endpoints.py')
f=importlib.util.module_from_spec(spec); spec.loader.exec_module(f)
checker=f.checker

def words(occ):
    choices=[[[o['var']]] if o['negative'] else [[],[o['var']]] for o in occ]
    return [{'coefficient':1,'word':sum(selection,[])} for selection in itertools.product(*choices)]

def word_tree(w):
    if not w: return 1
    t=w[0]
    for a in w[1:]: t=f.binop('product',t,a)
    return t

def sum_tree(ws):
    if len(ws)==1: return word_tree(ws[0]['word'])
    mid=len(ws)//2
    return f.binop('sum',sum_tree(ws[:mid]),sum_tree(ws[mid:]))

def expanded(data):
    out=[words(f.clause(c)[2]) for c in data['clauses']]
    for a in data['dictionary']:
        out.append([{'coefficient':1,'word':[a,a]},{'coefficient':1,'word':[a]}])
    for i,a in enumerate(data['dictionary']):
        for b in data['dictionary'][i+1:]:
            out.append([{'coefficient':1,'word':[a,b]},{'coefficient':1,'word':[b,a]}])
    return out,[sum_tree(w) for w in out]

def request(data):
    if not isinstance(data,dict) or set(data)!={'factored','expanded_words','expanded_axioms'}:
        raise checker.Invalid('complete expanded package required')
    g,ts,es,paths=f.request(data['factored'])
    ws,aa=expanded(data['factored'])
    for key,value in [('expanded_words',ws),('expanded_axioms',aa)]:
        if json.dumps(data[key],sort_keys=True)!=json.dumps(value,sort_keys=True):
            raise checker.Invalid('exact occurrence-preserving '+key+' mismatch')
    return g,es,[f.evaluate(a,data['factored']['q']) for a in aa]

def goals(data,mode='native'):
    g,_,es=request(data); z=f.n(f.i(data['factored']['q'],data['factored']['q']))
    trees=[f.i(g,f.e(a,z)) for a in es]
    if mode=='not-or': trees=[f.image(t) for t in trees]
    elif mode!='native': raise checker.Invalid('unknown format')
    return [checker.serialize(t) for t in trees]

def bridges(data,mode='native'):
    _,fs,es=request(data); trees=[f.e(a,b) for a,b in zip(fs,es)]
    if mode=='not-or': trees=[f.image(t) for t in trees]
    elif mode!='native': raise checker.Invalid('unknown format')
    return [checker.serialize(t) for t in trees]
