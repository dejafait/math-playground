"""Independent one-mark context request validation and endpoint reconstruction."""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/'balanced-slot'))
import checker

def validate_term(s):
    t = checker.parse(s, 'native')[0]
    def walk(t):
        if isinstance(t, str):
            if re.fullmatch(r'[A-Za-z0-9_]+', t) is None:
                raise checker.Invalid('non-ASCII payload')
        else:
            for a in t[1:]: walk(a)
    walk(t)
    return t

def nt(a): return ('not', a)
def im(a,b): return ('imp',a,b)
def xx(a,b): return im(im(a,b),nt(im(b,a)))
def ee(a,b): return nt(xx(a,b))
def aa(a,b): return nt(im(a,nt(b)))
def image(t):
    if isinstance(t,str): return t
    if t[0]=='not': return nt(image(t[1]))
    return ('or',nt(image(t[1])),image(t[2]))
def stats(t):
    if isinstance(t,str): return (1,0,len(t))
    ss=[stats(a) for a in t[1:]]
    return (1+sum(s[0] for s in ss),1+max(s[1] for s in ss),max(s[2] for s in ss))

def inspect(context):
    """Exact dictionary shapes; count skeleton nodes, height and marks."""
    if not isinstance(context,dict): raise checker.Invalid('context dictionary required')
    if context == {'mark':True}: return (1,0,1,[])
    if set(context)=={'term'}:
        validate_term(context['term'])
        return (1,0,0,[context['term']])
    if set(context)!={'op','left','right'} or context['op'] not in ('xor','and'):
        raise checker.Invalid('invalid context node')
    l,r=inspect(context['left']),inspect(context['right'])
    return (1+l[0]+r[0],1+max(l[1],r[1]),l[2]+r[2],l[3]+r[3])

def request(g,u,v,context):
    for s in (g,u,v): validate_term(s)
    count,height,marks,terms=inspect(context)
    if marks!=1: raise checker.Invalid('exactly one mark required')
    return count,height,terms

def fill(context,term):
    if context=={'mark':True}: return term
    if set(context)=={'term'}: return validate_term(context['term'])
    op=xx if context['op']=='xor' else aa
    return op(fill(context['left'],term),fill(context['right'],term))

def goal(g,u,v,context,mode='native'):
    request(g,u,v,context)
    t=im(validate_term(g),ee(fill(context,validate_term(u)),fill(context,validate_term(v))))
    if mode=='not-or': t=image(t)
    elif mode!='native': raise checker.Invalid('invalid format')
    return checker.serialize(t)

def coordinate(g,u,v):
    return checker.serialize(im(validate_term(g),ee(validate_term(u),validate_term(v))))
