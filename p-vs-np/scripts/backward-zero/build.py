"""Conditional one-row compiler. No table/basis/proof existence oracle."""
import importlib.util
import sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
ep=module('zero_endpoints',HERE/'endpoints.py')
# aggregate imports its own endpoints module by name; it is loaded before ours.
sys.path.insert(0,str(HERE.parent/'balanced-coordinate'))
aggregate=module('zero_aggregate',HERE.parent/'balanced-coordinate'/'aggregate.py')
p=aggregate.primitive
checker=aggregate.checker

def P(a,b): return p.N(p.I(a,p.N(b)))
def atom(key,t): return ('a',key,t)
def X(a,b): return ('x',a,b)
def product(a,b): return ('p',a,b)
def nt(t):
    if t[0]=='a': return t[2]
    return (p.X if t[0]=='x' else P)(nt(t[1]),nt(t[2]))
def height(t):
    return 0 if t[0]=='a' else 1+max(height(t[1]),height(t[2]))
def leaves(t):
    if t[0]=='a': return [t]
    if t[0]!='x': raise checker.Invalid('non-X sum in normalization')
    return leaves(t[1])+leaves(t[2])
def balanced(ts):
    if len(ts)==1: return ts[0]
    k=len(ts)//2
    return X(balanced(ts[:k]),balanced(ts[k:]))
def Bal(ts,z):
    if not ts: return z
    if len(ts)==1: return ts[0]
    M=1<<(len(ts)-1).bit_length()
    return balanced(list(ts)+[z]*(M-len(ts)))
def W(bits,ts,z): return Bal([t for b,t in zip(bits,ts) if b],z)
def at(t,path):
    for side in path: t=t[side]
    return t
def replace(t,path,new):
    if not path: return new
    k=path[0]
    return (t[0],replace(t[1],path[1:],new),t[2]) if k==1 else (t[0],t[1],replace(t[2],path[1:],new))

class Store:
    def __init__(self,library,q='q'):
        self.p=aggregate.AppendProof(); self.library=library; self.q=q
        self.calls=[]; self.max_argument_height=0; self.imports=[]; self.law_cache={}
    def copy(self,rows,env):
        moved=[]
        for f,rule,refs,subs in rows:
            if rule=='mp': j=self.p.mp(*(moved[a] for a in refs))
            else:
                e={a:p.sub(v,env) for a,v in subs.items()}
                j=self.p.ax(rule,e['A'],e['B'],e.get('C'))
            if self.p.rows[j][0]!=p.sub(f,env): raise checker.Invalid('copy mismatch')
            moved.append(j)
        return moved[-1]
    def use(self,name,env):
        env=dict(env); env.setdefault('q',self.q)
        key=(name,tuple(sorted(env.items())))
        if key in self.law_cache: return self.law_cache[key]
        begin=len(self.p.rows); j=self.copy(self.library[name]['rows'],env)
        self.calls.append({'name':name,'start':begin,'root':j,
                           'arguments':{a:p.text(v) for a,v in env.items()}})
        self.law_cache[key]=j
        return j
    def law(self,name,env):
        self.max_argument_height=max(self.max_argument_height,max([height(t) for t in env.values()]+[0]))
        return self.use(name,{a:nt(v) for a,v in env.items()})
    def refl(self,a): return self.law('refl',{'A':a})
    def symm(self,a,b,j): return self.p.mp(j,self.law('symm',{'A':a,'B':b}))
    def trans(self,a,b,c,ab,bc):
        j=self.law('trans',{'A':a,'B':b,'C':c})
        return self.p.mp(bc,self.p.mp(ab,j))
    def congr(self,a,b,c,d,ab,cd):
        ac,bc,bd=X(a,c),X(b,c),X(b,d)
        j=self.p.mp(ab,self.law('congL',{'A':a,'B':b,'C':c}))
        k=self.p.mp(cd,self.law('congR',{'A':c,'B':d,'C':b}))
        return self.trans(ac,bc,bd,j,k)
    def product_congr(self,a,b,c,bc):
        return self.p.mp(bc,self.law('prod_cong',{'A':a,'B':b,'C':c}))
    def retain(self,package,label):
        start=len(self.p.rows); root=self.copy(package['rows'],{})
        if len(self.p.rows)-start!=len(package['rows']): raise checker.Invalid('import length')
        # Every field and reference, including unused records, is compared.
        for i,(f,rule,refs,subs) in enumerate(package['rows']):
            got=self.p.rows[start+i]
            want=(f,rule,tuple(start+a for a in refs),subs if rule!='mp' else None,frozenset())
            if (got[0],got[1],tuple(got[2]),got[3],got[4])!=want:
                raise checker.Invalid('full import retention mismatch')
        self.imports.append({'label':label,'start':start,'lines':len(package['rows']),'root':root})
        return root
    def write(self,path,image=False):
        # Reuse serialization only; no synthesis/cache/reachability pruning.
        obj=object.__new__(aggregate.Combination); obj.p=self.p; obj.root=self.root
        return obj.write(path,image)

class Rewrite:
    def __init__(self,o,t):
        self.o=o; self.initial=self.tree=t; self.eq=o.refl(t); self.events=[]
    def change(self,path,new,j,label):
        old=self.tree; subold=at(old,path); subnew=new
        if self.o.p.rows[j][0]!=p.E(nt(subold),nt(subnew)): raise checker.Invalid('local equality endpoint')
        for length in range(len(path),0,-1):
            parent=at(old,path[:length-1]); side=path[length-1]; sibling=parent[3-side]
            if parent[0]!='x': raise checker.Invalid('non-X rewrite ancestor')
            law=self.o.law('congL' if side==1 else 'congR',{'A':subold,'B':subnew,'C':sibling})
            j=self.o.p.mp(j,law)
            subold=parent; subnew=X(subnew,sibling) if side==1 else X(sibling,subnew)
        self.tree=replace(old,path,new)
        if self.tree!=subnew: raise checker.Invalid('lift mismatch')
        self.eq=self.o.trans(self.initial,old,self.tree,self.eq,j)
        self.events.append({'kind':label,'path':list(path),'height':height(self.tree),
                            'leaves':len(leaves(self.tree)),'root':self.eq})
    def rotate(self,path,direction):
        t=at(self.tree,path)
        if direction=='right':
            a,b,c=t[1][1],t[1][2],t[2]; new=X(a,X(b,c))
            j=self.o.law('assoc',{'A':a,'B':b,'C':c})
        else:
            a,b,c=t[1],t[2][1],t[2][2]; new=X(X(a,b),c)
            j=self.o.law('assoc',{'A':a,'B':b,'C':c}); j=self.o.symm(new,t,j)
        self.change(path,new,j,'rotate-'+direction)
    def split(self,path,k):
        t=at(self.tree,path); size=len(leaves(t))
        if not 0<k<size or t[0]!='x': raise checker.Invalid('split boundary')
        left=len(leaves(t[1]))
        if k==left: return
        if k<left:
            self.split(path+(1,),k); self.rotate(path,'right')
        else:
            self.split(path+(2,),k-left); self.rotate(path,'left')
    def rebalance(self,path=()):
        count=len(leaves(at(self.tree,path)))
        if count==1: return
        if count&(count-1): raise checker.Invalid('perfect rebalance requires power of two')
        self.split(path,count//2)
        self.rebalance(path+(1,)); self.rebalance(path+(2,))
    def expose(self,path,pair,rotations):
        t=at(self.tree,path); left=len(leaves(t[1]))
        if pair+1<left: return self.expose(path+(1,),pair,rotations)
        if pair>=left: return self.expose(path+(2,),pair-left,rotations)
        def rot(where,direction):
            self.rotate(where,direction); rotations.append((where,direction))
        while at(self.tree,path+(1,))[0]=='x' and at(self.tree,path+(1,))[2][0]=='x': rot(path+(1,),'left')
        while at(self.tree,path+(2,))[0]=='x' and at(self.tree,path+(2,))[1][0]=='x': rot(path+(2,),'right')
        t=at(self.tree,path); li=t[1][0]=='x'; ri=t[2][0]=='x'
        if li:
            rot(path,'right')
            if ri: rot(path+(2,),'left'); return path+(2,1)
            return path+(2,)
        if ri: rot(path,'left'); return path+(1,)
        return path
    def slots(self,pair,cancel,z):
        before=leaves(self.tree); rotations=[]; path=self.expose((),pair,rotations)
        a,b=at(self.tree,path)[1:]
        if a[0]!='a' or b[0]!='a': raise checker.Invalid('pair not exposed')
        if cancel:
            if a!=b: raise checker.Invalid('nonidentical cancellation')
            j=self.o.law('cancel',{'A':a}); zz=X(z,z)
            k=self.o.law('zero_slots',{}); j=self.o.trans(X(a,a),z,zz,j,k)
            new=zz
        else: j=self.o.law('comm',{'A':a,'B':b}); new=X(b,a)
        self.change(path,new,j,'cancel' if cancel else 'exchange')
        for where,direction in reversed(rotations): self.rotate(where,'left' if direction=='right' else 'right')
        wanted=list(before)
        if cancel: wanted[pair:pair+2]=[z,z]
        else: wanted[pair:pair+2]=[b,a]
        if self.tree!=balanced(wanted): raise checker.Invalid('perfect slot restoration failed')

def expand(o,t,z):
    if t[0]=='a': return t,o.refl(t)
    if t[0]=='x':
        a,ja=expand(o,t[1],z); b,jb=expand(o,t[2],z)
        return X(a,b),o.congr(t[1],a,t[2],b,ja,jb)
    a,b=t[1:]
    if a[0]!='a': raise checker.Invalid('single left letter factor required')
    if b[0]=='x':
        u,v=b[1:]; first=o.law('dist',{'A':a,'B':u,'C':v})
        left,jl=expand(o,product(a,u),z); right,jr=expand(o,product(a,v),z)
        mid=X(product(a,u),product(a,v)); out=X(left,right)
        second=o.congr(product(a,u),left,product(a,v),right,jl,jr)
        return out,o.trans(t,mid,out,first,second)
    if b[0]!='a': raise checker.Invalid('nested product not approved')
    if b[1]==z[1]: return z,o.law('prod_zero',{'A':a})
    if b[1][0]!=1: raise checker.Invalid('product leaf is not a suffix')
    out=atom((2,a[1][1],b[1][1]),P(nt(a),nt(b)))
    # This is a skeleton annotation change; the native trees are identical.
    if nt(out)!=nt(t): raise checker.Invalid('product annotation mismatch')
    return out,o.refl(out)

def erase_zeros(o,t,z):
    if t[0]=='a': return t,o.refl(t)
    a,ja=erase_zeros(o,t[1],z); b,jb=erase_zeros(o,t[2],z)
    mid=X(a,b); first=o.congr(t[1],a,t[2],b,ja,jb)
    if b==z:
        j=o.law('zeroR',{'A':a}); return a,o.trans(t,mid,a,first,j)
    if a==z:
        j=o.law('zeroL',{'A':b}); return b,o.trans(t,mid,b,first,j)
    return mid,first

def normalize(o,t,z):
    expanded,j=expand(o,t,z)
    # Pad with explicit false leaves, then balance without reordering.
    ls=leaves(expanded); M=1<<(len(ls)-1).bit_length()
    work=Rewrite(o,expanded)
    if len(ls)<M:
        extra=Bal([z]*(M-len(ls)),z)
        if len(leaves(extra))!=M-len(ls):
            # Bal would itself pad this range; choose an ordered near-balanced
            # unpadded zero tree. Its height is ceil(log2(range)).
            extra=balanced([z]*(M-len(ls)))
        zero,jzero=erase_zeros(o,extra,z)
        if zero!=z: raise checker.Invalid('padding zero reduction')
        old=work.tree; mid=X(old,z); new=X(old,extra)
        a=o.law('zeroR',{'A':old}); a=o.symm(mid,old,a)
        b=o.p.mp(o.symm(extra,z,jzero),o.law('congR',{'A':z,'B':extra,'C':old}))
        local=o.trans(old,mid,new,a,b); work.change((),new,local,'append-padding')
    work.rebalance()
    if work.tree!=balanced(ls+[z]*(M-len(ls))): raise checker.Invalid('ordered rebalance failed')
    # Adjacent exchanges restore the perfect shape after every operation.
    for i in range(1,M):
        jpos=i
        while jpos>0 and leaves(work.tree)[jpos-1][1]>leaves(work.tree)[jpos][1]:
            work.slots(jpos-1,False,z); jpos-=1
    i=0
    while i+1<M:
        ls2=leaves(work.tree)
        if ls2[i]!=z and ls2[i]==ls2[i+1]: work.slots(i,True,z); i+=2
        else: i+=1
    # Stable-sort surviving atoms followed by all false slots.
    for i in range(1,M):
        jpos=i
        while jpos>0 and leaves(work.tree)[jpos-1][1]>leaves(work.tree)[jpos][1]:
            work.slots(jpos-1,False,z); jpos-=1
    slim,jslim=erase_zeros(o,work.tree,z)
    survivors=[a for a in leaves(work.tree) if a!=z]
    wanted=Bal(survivors,z)
    # Re-pad compacted intervals to exactly the requested selected Bal tree.
    compact,jcompact=erase_zeros(o,wanted,z)
    # Both are obtained by deleting the zero suffix in the same perfect tree
    # at different capacities. Their order may agree but shape need not.
    # Normalize shapes by splitting only at the desired subtree boundaries.
    shape=Rewrite(o,slim)
    def match(path,target):
        if target[0]=='a':
            if at(shape.tree,path)!=target: raise checker.Invalid('compact leaf mismatch')
            return
        k=len(leaves(target[1])); shape.split(path,k)
        match(path+(1,),target[1]); match(path+(2,),target[2])
    match((),compact)
    if shape.tree!=compact: raise checker.Invalid('compact shape mismatch')
    a=o.trans(expanded,work.tree,slim,work.eq,jslim)
    b=o.trans(expanded,slim,compact,a,shape.eq)
    c=o.trans(expanded,compact,wanted,b,o.symm(wanted,compact,jcompact))
    return wanted,o.trans(t,expanded,wanted,j,c),{
        'slots':M,'survivors':len(survivors),'events':work.events+shape.events,
        'max_height':max([height(t),height(expanded),height(wanted),height(slim)]+[e['height'] for e in work.events+shape.events])}

def compare(o,a,b,z):
    aa,ja,ta=normalize(o,a,z); bb,jb,tb=normalize(o,b,z)
    if aa!=bb: raise checker.Invalid('checked coefficients did not give literal normal forms')
    return o.trans(a,aa,b,ja,o.symm(b,bb,jb)),[ta,tb]

def combine(o,old,new,proofs,z):
    if not old: return z,z,o.refl(z)
    if len(old)==1: return old[0],new[0],proofs[0]
    M=1<<(len(old)-1).bit_length()
    old=list(old)+[z]*(M-len(old)); new=list(new)+[z]*(M-len(new))
    proofs=list(proofs)+[o.refl(z) for _ in range(M-len(proofs))]
    def go(lo,hi):
        if hi-lo==1: return old[lo],new[lo],proofs[lo]
        md=(lo+hi)//2; a,b,j=go(lo,md); c,d,k=go(md,hi)
        return X(a,c),X(b,d),o.congr(a,b,c,d,j,k)
    return go(0,M)

def compile_one(d,coordinate_paths,next_paths,library):
    requested=ep.request(d); expected=ep.strings(d)
    if len(coordinate_paths)!=d['N'] or len(next_paths)!=d['k']: raise checker.Invalid('complete proof counts')
    # Validate every input package, including unused coordinates/rows, first.
    packages=[aggregate.load(path,goal) for path,goal in zip(coordinate_paths+next_paths,
                                                          expected['coordinates']+expected['next'])]
    o=Store(library,d['q']); inputs=[o.retain(pkg,'coordinate-'+str(i) if i<d['N'] else 'next-'+str(i-d['N'])) for i,pkg in enumerate(packages)]
    imported_end=len(o.p.rows)
    result=emit_transition(o,d,inputs[:d['N']],inputs[d['N']:])
    o.required_roots=result['required_roots']; o.traces=result['traces']
    o.packages=packages; o.imported_end=imported_end
    return o

def emit_transition(o,d,coordinate_roots,next_roots):
    """Internal checked earlier-line interface; creates no new store/imports.

    A whole-chain caller must additionally own/validate its indexed row roots.
    The original fresh wrapper continues to receive complete packages.
    """
    requested=ep.request(d); expected=ep.strings(d)
    begin=len(o.p.rows)
    if o.q!=d['q'] or len(coordinate_roots)!=d['N'] or len(next_roots)!=d['k']:
        raise checker.Invalid('row interface dimensions/state')
    for root,goal in zip(list(coordinate_roots)+list(next_roots),
                         expected['coordinates']+expected['next']):
        if type(root) is not int or not 0<=root<begin:
            raise checker.Invalid('row root not strictly earlier')
        if p.text(o.p.rows[root][0])!=goal:
            raise checker.Invalid('row root exact endpoint')
    z=atom((9,),p.N(p.I(d['q'],d['q']))); y=atom((0,),p.I(d['q'],d['q']))
    S=[atom((1,v),aggregate.native(ep.c.parse(s,'native')[0])) for v,s in enumerate(d['suffixes'])]
    xs=[atom((3,b),name) for b,name in enumerate(d['letters'])]
    nxt=[W(row,S,z) for row in d['R_next']]
    coordinates=[X(y if d['beta'][v][0] else z,
        Bal([product(xs[b],W(d['G'][b][v],S,z)) for b in range(d['n'])],z)) for v in range(d['N'])]
    indices=[v for v,bit in enumerate(d['r'][0]) if bit]
    L,coord,j=combine(o,[S[v] for v in indices],[coordinates[v] for v in indices],[coordinate_roots[v] for v in indices],z)
    Q7=Bal([product(xs[b],W(requested['products'][b],S,z)) for b in range(d['n'])],z)
    Q8=Bal([product(xs[b],W(d['T'][b][0],nxt,z)) for b in range(d['n'])],z)
    first,traces1=compare(o,coord,Q7,z)
    q7=o.trans(L,coord,Q7,j,first)
    q8,traces2=compare(o,Q7,Q8,z)
    # Receive next rows via references. No suffix-coordinate premise is reused
    # as a guarded statement and no row theorem is an axiom.
    left=[]; right=[]; roots=[]
    for b in range(d['n']):
        selected=[j for j,bit in enumerate(d['T'][b][0]) if bit]
        inn,zeros,j=combine(o,[nxt[j] for j in selected],[z]*len(selected),[next_roots[j] for j in selected],z)
        compact,jcompact=erase_zeros(o,zeros,z)
        if compact!=z: raise checker.Invalid('next-row false sum')
        j=o.trans(inn,zeros,z,j,jcompact)
        pa,pz=product(xs[b],inn),product(xs[b],z)
        j=o.product_congr(xs[b],inn,z,j)
        j=o.trans(pa,pz,z,j,o.law('prod_zero',{'A':xs[b]}))
        left.append(pa); right.append(z); roots.append(j)
    a,zeros,j=combine(o,left,right,roots,z)
    if nt(a)!=nt(Q8): raise checker.Invalid('Q8 next-row syntax')
    zz,jz=erase_zeros(o,zeros,z)
    if zz!=z: raise checker.Invalid('outer false sum')
    end8=o.trans(Q8,zeros,z,j,jz)
    end7=o.trans(Q7,Q8,z,q8,end8)
    o.root=o.trans(L,Q7,z,q7,end7)
    required_roots=[q7,q8,end8,o.root]
    for root,goal in zip(required_roots,expected['goals']):
        if p.text(o.p.rows[root][0])!=goal: raise checker.Invalid('required endpoint mismatch')
    if o.root!=len(o.p.rows)-1: raise checker.Invalid('last record mismatch')
    return {'required_roots':required_roots,'traces':traces1+traces2,
            'start':begin,'end':len(o.p.rows)}
