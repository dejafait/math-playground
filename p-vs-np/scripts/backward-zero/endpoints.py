"""Literal requested endpoints; no emitter/planner import."""
import importlib.util
import re
from pathlib import Path

_spec = importlib.util.spec_from_file_location('zero_checker', Path(__file__).resolve().parent.parent/'balanced-slot'/'checker.py')
c = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(c)

def neg(a): return ('not', a)
def imp(a,b): return ('imp', a,b)
def xor(a,b): return imp(imp(a,b),neg(imp(b,a)))
def eq(a,b): return neg(xor(a,b))
def prod(a,b): return neg(imp(a,neg(b)))
def image(a):
    if isinstance(a,str): return a
    if a[0]=='not': return neg(image(a[1]))
    return ('or',neg(image(a[1])),image(a[2]))
def bal(ts,z):
    if not ts: return z
    if len(ts)==1: return ts[0]
    m=1<<(len(ts)-1).bit_length()
    ts=list(ts)+[z]*(m-len(ts))
    def go(lo,hi):
        if hi-lo==1: return ts[lo]
        md=(lo+hi)//2
        return xor(go(lo,md),go(md,hi))
    return go(0,m)
def choose(row,ts,z): return bal([t for bit,t in zip(row,ts) if bit],z)
def _payload(t):
    if isinstance(t,str):
        if not re.fullmatch(r'[A-Za-z0-9_]+',t): raise c.Invalid('ASCII payload required')
    else:
        for a in t[1:]: _payload(a)
def _matrix(a,h,w,label):
    if not isinstance(a,list) or len(a)!=h: raise c.Invalid(label+' height')
    for row in a:
        if not isinstance(row,list) or len(row)!=w: raise c.Invalid(label+' width')
        if any(type(v) is not int or v not in (0,1) for v in row): raise c.Invalid(label+' non-bit')
def request(d):
    required={'N','n','k','q','suffixes','letters','beta','G','r','R_next','T'}
    if set(d)!=required: raise c.Invalid('request fields')
    N,n,k=d['N'],d['n'],d['k']
    if any(type(a) is not int for a in (N,n,k)) or N<2 or n<0 or not 0<=k<=N:
        raise c.Invalid('dimensions')
    if not isinstance(d['q'],str) or not re.fullmatch(r'[A-Za-z0-9_]+',d['q']):
        raise c.Invalid('q payload')
    if len(d['suffixes'])!=N or len(d['letters'])!=n: raise c.Invalid('term dimensions')
    S=[c.parse(s,'native')[0] for s in d['suffixes']]
    xs=[c.parse(s,'native')[0] for s in d['letters']]
    if any(not isinstance(a,str) for a in xs): raise c.Invalid('letters must be variables')
    for a in S+xs: _payload(a)
    _matrix(d['beta'],N,1,'beta'); _matrix(d['r'],1,N,'r')
    _matrix(d['R_next'],k,N,'R_next')
    if not isinstance(d['G'],list) or len(d['G'])!=n or not isinstance(d['T'],list) or len(d['T'])!=n:
        raise c.Invalid('letter tables')
    for b in range(n):
        _matrix(d['G'][b],N,N,'G'); _matrix(d['T'][b],1,k,'T')
    r=d['r'][0]
    if sum(a*v[0] for a,v in zip(r,d['beta']))%2: raise c.Invalid('r beta != 0')
    products=[]
    for b in range(n):
        left=[sum(r[v]*d['G'][b][v][w] for v in range(N))%2 for w in range(N)]
        right=[sum(d['T'][b][0][j]*d['R_next'][j][w] for j in range(k))%2 for w in range(N)]
        if left!=right: raise c.Invalid('r G != T R_next')
        products.append(left)
    y=imp(d['q'],d['q']); z=neg(y)
    rows=[choose(row,S,z) for row in d['R_next']]
    coordinates=[eq(S[v],xor(y if d['beta'][v][0] else z,
        bal([prod(xs[b],choose(d['G'][b][v],S,z)) for b in range(n)],z))) for v in range(N)]
    nxt=[eq(row,z) for row in rows]
    L=choose(r,S,z)
    Q7=bal([prod(xs[b],choose(products[b],S,z)) for b in range(n)],z)
    Q8=bal([prod(xs[b],choose(d['T'][b][0],rows,z)) for b in range(n)],z)
    return {'coordinates':coordinates,'next':nxt,'terms':[L,Q7,Q8,z],
            'goals':[eq(L,Q7),eq(Q7,Q8),eq(Q8,z),eq(L,z)],'products':products}
def strings(d,mode='native'):
    out=request(d)
    def render(ts): return [c.serialize(image(t) if mode=='not-or' else t) for t in ts]
    return {key:render(out[key]) for key in ('coordinates','next','goals')}
def fixed():
    a,b,cc='A','B','C'; z=neg(imp('q','q'))
    return {'refl':eq(a,a),'symm':imp(eq(a,b),eq(b,a)),
            'trans':imp(eq(a,b),imp(eq(b,cc),eq(a,cc))),
            'congL':imp(eq(a,b),eq(xor(a,cc),xor(b,cc))),
            'congR':imp(eq(a,b),eq(xor(cc,a),xor(cc,b))),
            'assoc':eq(xor(xor(a,b),cc),xor(a,xor(b,cc))),
            'comm':eq(xor(a,b),xor(b,a)),'cancel':eq(xor(a,a),z),
            'zero_slots':eq(z,xor(z,z)),
            'dist':eq(prod(a,xor(b,cc)),xor(prod(a,b),prod(a,cc))),
            'prod_cong':imp(eq(b,cc),eq(prod(a,b),prod(a,cc))),
            'zeroR':eq(xor(a,z),a),'zeroL':eq(xor(z,a),a),
            'prod_zero':eq(prod(a,z),z)}
