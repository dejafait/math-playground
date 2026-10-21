"""Independent exact factored-axiom request validation and goal construction."""
import re
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/'balanced-slot'))
import checker

def n(a): return ('not',a)
def i(a,b): return ('imp',a,b)
def x(a,b): return i(i(a,b),n(i(b,a)))
def e(a,b): return n(x(a,b))
def p(a,b): return n(i(a,n(b)))
def image(t):
    if isinstance(t,str): return t
    if t[0]=='not': return n(image(t[1]))
    return ('or',n(image(t[1])),image(t[2]))
def stats(t):
    if isinstance(t,str): return (1,0,len(t))
    s=[stats(a) for a in t[1:]]
    return (1+sum(a[0] for a in s),1+max(a[1] for a in s),max(a[2] for a in s))
def name(s):
    if not isinstance(s,str) or re.fullmatch('[A-Za-z0-9_]+',s) is None:
        raise checker.Invalid('ASCII name required')
    return s
def binop(op,a,b): return {'op':op,'left':a,'right':b}
def clause(tree):
    if not isinstance(tree,dict): raise checker.Invalid('clause tree required')
    if set(tree)=={'var','negative'}:
        name(tree['var'])
        if type(tree['negative']) is not bool: raise checker.Invalid('literal sign required')
        lit=n(tree['var']) if tree['negative'] else tree['var']
        factor=tree['var'] if tree['negative'] else binop('sum',1,tree['var'])
        return lit,factor,[tree]
    if set(tree)!={'op','left','right'} or tree['op']!='or':
        raise checker.Invalid('literal or OR required')
    l,r=clause(tree['left']),clause(tree['right'])
    return i(n(l[0]),r[0]),binop('product',l[1],r[1]),l[2]+r[2]
def evaluate(tree,q):
    if type(tree) is int:
        if tree not in (0,1): raise checker.Invalid('F2 constant required')
        t=i(q,q); return t if tree else n(t)
    if isinstance(tree,str): return name(tree)
    if not isinstance(tree,dict) or set(tree)!={'op','left','right'} or tree['op'] not in ('sum','product'):
        raise checker.Invalid('exact arithmetic tree required')
    op=x if tree['op']=='sum' else p
    return op(evaluate(tree['left'],q),evaluate(tree['right'],q))
def axioms(clauses,dictionary):
    result=[clause(c)[1] for c in clauses]
    for a in dictionary: result.append(binop('sum',binop('product',a,a),a))
    for j,a in enumerate(dictionary):
        for b in dictionary[j+1:]:
            result.append(binop('sum',binop('product',a,b),binop('product',b,a)))
    return result
def request(data):
    if not isinstance(data,dict) or set(data)!={'q','clauses','conjunction','dictionary','axioms','placeholders'}:
        raise checker.Invalid('complete guard package required')
    q=name(data['q']); cs=data['clauses']; ds=data['dictionary']
    if not isinstance(cs,list) or not cs: raise checker.Invalid('nonempty CNF required')
    terms=[]; allnames=[]
    for c in cs:
        t,_,occ=clause(c)
        if not 1<=len(occ)<=3: raise checker.Invalid('nonempty width-three clause required')
        terms.append(t); allnames.extend(o['var'] for o in occ)
    if ds!=sorted(set(allnames)): raise checker.Invalid('occurring dictionary mismatch')
    seen=[]; paths={}
    def guard(tree,path):
        if type(tree) is int:
            if not 0<=tree<len(cs): raise checker.Invalid('clause position out of range')
            seen.append(tree); paths[tree]=path; return terms[tree]
        if not isinstance(tree,dict) or set(tree)!={'left','right'}:
            raise checker.Invalid('binary conjunction tree required')
        return p(guard(tree['left'],path+['left']),guard(tree['right'],path+['right']))
    g=guard(data['conjunction'],[])
    if seen!=list(range(len(cs))): raise checker.Invalid('ordered clause positions mismatch')
    expected=axioms(cs,ds)
    # Typed JSON comparison forbids True masquerading as the arithmetic constant 1.
    if json.dumps(data['axioms'],sort_keys=True)!=json.dumps(expected,sort_keys=True):
        raise checker.Invalid('factored ordered axiom tree mismatch')
    names=['t_'+str(j+1) for j in range(len(expected))]
    if data['placeholders']!=names: raise checker.Invalid('A-position placeholder mismatch')
    # Placeholder strings are role identifiers in a disjoint namespace, not native variables.
    z=n(i(q,q)); evals=[evaluate(a,q) for a in expected]
    return g,terms,evals,paths
def goals(data,mode='native'):
    g,_,es,_=request(data); z=n(i(data['q'],data['q']))
    ts=[i(g,e(a,z)) for a in es]
    if mode=='not-or': ts=[image(t) for t in ts]
    elif mode!='native': raise checker.Invalid('unknown format')
    return [checker.serialize(t) for t in ts]
