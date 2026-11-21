#!/usr/bin/env python3
"""Fixed694 scalar-register prescription. See working694 before execution.

All numerical service values are engine registers. Host loops with static
bounds expand a finite program; host indices are symbolic instruction slots.
The gzip JSON-lines transcript contains every executed scalar instruction.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import gzip
import json

HERE = Path(__file__).resolve()
OUT = HERE.with_suffix('.json')
TRACE = HERE.with_suffix('.trace.jsonl.gz')
CAP = 5000000

class Stop(Exception):
    pass

class R:
    def __init__(self, i, q):
        self.i, self.q = i, q

class Engine:
    def __init__(self):
        self.file = gzip.open(TRACE, 'wt')
        self.next = 0
        self.cost = 0
        self.by = Counter()
        self.category = 'constants'
        self.guards = Counter()
    def emit(self, entry, cost):
        self.file.write(json.dumps(entry, separators=(',', ':'))+'\n')
        self.cost += cost
        self.by[self.category] += cost
        if self.cost > CAP:
            raise Stop('complete scalar transcript exceeds cap')
    def mark(self, label):
        self.category = label
        self.file.write(json.dumps(['mark', label])+'\n')
    def new(self, q):
        r = R(self.next, q)
        self.next += 1
        return r
    def literal(self, x):
        r = self.new(F(x))
        self.emit(['literal', r.i, x], 1)
        return r
    def cp(self, x):
        r = self.new(x.q)
        self.emit(['copy', r.i, x.i], 1)
        return r
    def op(self, op, x, y):
        if op == '+': q = x.q+y.q
        elif op == '-': q = x.q-y.q
        elif op == '*': q = x.q*y.q
        elif op == '/':
            # Division domain guard is an actual counted comparison.
            self.need(self.cmp('!=', y, C[0]), 'division denominator nonzero')
            q = x.q/y.q
        else: raise ValueError(op)
        r = self.new(q)
        self.emit([op, r.i, x.i, y.i], 2)
        return r
    def cmp(self, op, x, y):
        if op == '<': b = x.q < y.q
        elif op == '<=': b = x.q <= y.q
        elif op == '>': b = x.q > y.q
        elif op == '>=': b = x.q >= y.q
        elif op == '==': b = x.q == y.q
        elif op == '!=': b = x.q != y.q
        else: raise ValueError(op)
        self.emit(['compare', op, x.i, y.i, b], 1)
        return b
    def need(self, b, label):
        self.guards[label] += 1
        if not b: raise Stop(label)
    def low(self, x, y):
        return self.cp(x if self.cmp('<=', x, y) else y)
    def high(self, x, y):
        return self.cp(x if self.cmp('>=', x, y) else y)
    def absolute(self, x):
        return self.cp(x) if self.cmp('>=', x, C[0]) else self.op('-', C[0], x)

E = Engine()
report = {'prescription':'working694; same numerical map as692; explicit scalar registers',
          'degrees':[63,81,117], 'grid_bits':640,
          'conversion_tolerance_width':'2^-560', 'rows':[], 'failures':[],
          'required':{'node_radius':'2^-512','weight_radius':'2^-512','total_setup_work':CAP}}

def add(x,y): return E.op('+',x,y)
def sub(x,y): return E.op('-',x,y)
def mul(x,y): return E.op('*',x,y)
def div(x,y): return E.op('/',x,y)
def zi(a):
    a = int(a)
    if not a: return {'odd_hex':'0x0','shift':0}
    s = (abs(a)&-abs(a)).bit_length()-1
    return {'odd_hex':hex(a>>s),'shift':s}
def rf(q):
    if isinstance(q,R): q=q.q
    q=F(q)
    return {'num':zi(q.numerator),'den':zi(q.denominator)}
def iv(lo,hi): return [rf(lo),rf(hi)]
def gr(lo,hi): return [zi(lo.q),zi(hi.q)]
def sign(x):
    if E.cmp('>',x,C[0]): return E.cp(C[1])
    if E.cmp('<',x,C[0]): return E.cp(C[-1])
    return E.cp(C[0])

def ev(n,a):
    E.need(E.cmp('<=',C[0],a),'point lower domain')
    E.need(E.cmp('<=',a,D),'point upper domain')
    # This is a finite SSA expansion at each static degree: Q[k] never
    # requires a numeric stage counter or a copy from Q[k] to Q[k-1].
    p,q=C[1],a
    for k in range(1,n):
        z=sub(mul(mul(A[k],a),q),mul(B[k],p))
        p,q=q,z
    return p,q

def derivative(n,lo,hi,depth,allow_zero=False):
    E.mark('derivative')
    E.need(E.cmp('<',depth,C[640]),'midpoint grid depth')
    a=div(add(lo,hi),C[2])
    pm,pn=ev(n,a)
    x=div(a,D)
    p,prev=div(pn,DEN[n]),div(pm,DEN[n-1])
    d=div(mul(C[n],sub(prev,mul(x,p))),sub(C[1],mul(x,x)))
    r=div(sub(hi,lo),TWO_D)
    h=div(hi,D)
    E.need(E.cmp('<',h,C[1]),'interior upper endpoint')
    v=sub(C[1],mul(h,h))
    interior=div(FOUR_N2[n],mul(v,v))
    M=E.low(GLOBAL[n],interior)
    mr=mul(M,r)
    dl,du=sub(d,mr),add(d,mr)
    if not allow_zero:
        E.need(E.cmp('>',dl,C[0]) or E.cmp('<',du,C[0]),'derivative excludes zero')
    return a,p,d,dl,du,M,pm,pn,mr

def quantize(jlo,jhi,oldlo,oldhi,depth):
    E.mark('conversion')
    E.need(E.cmp('<',jlo,jhi),'strictly positive image')
    center=div(mul(add(jlo,jhi),D),C[2])
    width=mul(sub(jhi,jlo),D)
    target=E.high(width,CONVERSION_GRID)
    ll,uu=E.cp(oldlo),E.cp(oldhi)
    h=sub(uu,ll)
    steps=E.cp(C[0])
    while E.cmp('>',h,target):
        E.need(E.cmp('<',depth,C[640]),'conversion grid depth')
        mid=div(add(ll,uu),C[2])
        if E.cmp('<=',mid,center): ll=E.cp(mid)
        else: uu=E.cp(mid)
        h=div(h,C[2])
        depth=add(depth,C[1])
        steps=add(steps,C[1])
    E.need(E.cmp('==',sub(uu,ll),h),'cell size invariant')
    E.need(E.cmp('>',h,div(target,C[2])),'cell lower size')
    nl,nu=E.high(oldlo,sub(ll,h)),E.low(oldhi,add(uu,h))
    E.need(E.cmp('<=',div(nl,D),jlo),'conversion lower coverage')
    E.need(E.cmp('<=',jhi,div(nu,D)),'conversion upper coverage')
    E.need(E.cmp('<',sub(nu,nl),sub(oldhi,oldlo)),'strict contraction')
    return nl,nu,depth,steps

def weights(n,lo,hi,depth):
    a,p,d,dl,du,M,pm,pn,_=derivative(n,lo,hi,depth)
    E.mark('weights')
    xl,xh=div(lo,D),div(hi,D)
    dl2,du2=mul(dl,dl),mul(du,du)
    dslo,dshi=E.low(dl2,du2),E.high(dl2,du2)
    zl=mul(sub(C[1],mul(xh,xh)),dslo)
    zh=mul(sub(C[1],mul(xl,xl)),dshi)
    E.need(E.cmp('>',zl,C[0]),'positive weight denominator')
    E.need(E.cmp('<=',zl,zh),'ordered weight denominator')
    wl,wu=div(C[2],zh),div(C[2],zl)
    nr,wr=div(sub(hi,lo),TWO_D),div(sub(wu,wl),C[2])
    E.need(E.cmp('<=',nr,TOL),'node radius target')
    E.need(E.cmp('<=',wr,TOL),'weight radius target')
    # Explicit numerical output copies, rather than free endpoint stores.
    outs=[E.cp(x) for x in (xl,xh,wl,wu)]
    E.file.write(json.dumps(['output','positive',n,*[x.i for x in outs]])+'\n')
    out={'node':iv(outs[0],outs[1]),'weight':iv(outs[2],outs[3]),
         'node_radius':rf(nr),'weight_radius':rf(wr),
         'derivative_point':zi(a.q),'scaled_adjacent_values':[zi(pm.q),zi(pn.q)],
         'derivative_range':iv(dl,du),'second_derivative_bound':rf(M),'depth':int(depth.q)}
    return out,nr,wr,outs

def main():
    global C,D,TWO_D,DEN,A,B,GLOBAL,FOUR_N2,TOL,NODE_GATE,CONVERSION_GRID
    # Every small integer is a literal assignment; no floating or high
    # precision constant appears. The lists below are static code indices.
    literals=sorted(set(range(-1,129))|{550,560,640,16384})
    C={k:E.literal(k) for k in literals}
    D=E.cp(C[1]); powers={0:D}
    for k in range(1,641):
        D=mul(D,C[2]); powers[k]=D
    TWO_D=mul(C[2],D)
    TOL=div(C[1],powers[512])
    NODE_GATE=div(C[1],powers[550])
    CONVERSION_GRID=div(D,powers[560])
    D2=mul(D,D)
    A,B,DEN={},{},{0:E.cp(C[1])}
    for k in range(1,118):
        A[k]=add(mul(C[2],C[k]),C[1])
        B[k]=mul(mul(C[k],C[k]),D2)
        DEN[k]=mul(mul(DEN[k-1],C[k]),D)
    GLOBAL,FOUR_N2={},{}
    for n in (63,81,117):
        GLOBAL[n]=div(mul(mul(mul(C[n-1],C[n]),C[n+1]),C[n+2]),C[8])
        FOUR_N2[n]=mul(C[4],mul(C[n],C[n]))
    mesh=[]
    gridunit=div(D,C[16384])
    E.mark('mesh')
    for j in range(128):
        a=mul(sub(C[16384],mul(C[j],C[j])),gridunit)
        E.need(E.cmp('>',a,C[0]),'mesh positive')
        E.need(E.cmp('<=',a,D),'mesh upper domain')
        if j: E.need(E.cmp('<',a,mesh[-1]),'mesh descending')
        mesh.append(a)
    maxnr,maxwr=E.cp(C[0]),E.cp(C[0])
    inventory=E.cp(C[0])
    for n in (63,81,117):
        E.mark('mesh point recurrence')
        row={'degree':n,'mesh_sign_evidence':[],'positive_roots':[]}
        report['rows'].append(row)
        signs=[]
        for a in mesh:
            _,q=ev(n,a); s=sign(q)
            E.need(E.cmp('!=',s,C[0]),'mesh endpoint nonzero')
            signs.append(s)
            row['mesh_sign_evidence'].append({'point':zi(a.q),'scaled_value':zi(q.q),'sign':int(s.q)})
        brackets=[]; count=E.cp(C[0])
        E.mark('isolation')
        for j in range(127):
            if E.cmp('!=',signs[j],signs[j+1]):
                brackets.append(tuple(E.cp(v) for v in (mesh[j+1],mesh[j],signs[j+1],signs[j])))
                count=add(count,C[1])
        expected=div(sub(C[n],C[1]),C[2])
        E.need(E.cmp('==',count,expected),'complete positive root count')
        for index,(lo,hi,sl,su) in enumerate(brackets):
            root={'index_descending':index,'initial_grid_bracket':gr(lo,hi),
                  'initial_signs':[int(sl.q),int(su.q)],'adaptive_trials':[],'bisections':[],'newton':[]}
            row['positive_roots'].append(root)
            depth=E.cp(C[14]); seed=None
            for trial in range(17):
                values=derivative(n,lo,hi,depth,True)
                a,p,d,dl,du,M,pm,pn,mr=values
                E.mark('adaptive control')
                accepted=(E.cmp('>',dl,C[0]) or E.cmp('<',du,C[0])) and E.cmp('<=',mr,div(E.absolute(d),C[8]))
                root['adaptive_trials'].append({'old_grid_interval':gr(lo,hi),'depth':int(depth.q),
                    'point':zi(a.q),'scaled_adjacent_values':[zi(pm.q),zi(pn.q)],
                    'derivative_range':iv(dl,du),'second_derivative_bound':rf(M),'accepted':accepted})
                if accepted: seed=values; break
                # Static final-trial branch, not a scalar comparison.
                if trial==16: raise Stop('adaptive prefix bounded schedule')
                s=sign(pn); E.need(E.cmp('!=',s,C[0]),'bisection point nonzero')
                root['bisections'].append({'point':zi(a.q),'scaled_value':zi(pn.q),'sign':int(s.q)})
                if E.cmp('==',s,sl): lo,sl=E.cp(a),E.cp(s)
                else: hi,su=E.cp(a),E.cp(s)
                depth=add(depth,C[1])
            if seed is None: raise Stop('prefix did not accept')
            done=False
            for iteration in range(12):
                oldlo,oldhi=E.cp(lo),E.cp(hi)
                if iteration==0: values=seed
                else: values=derivative(n,lo,hi,depth)
                a,p,d,dl,du,M,pm,pn,_=values
                E.mark('Newton image')
                m=div(a,D)
                u,v=sub(m,div(p,dl)),sub(m,div(p,du))
                il,iu=E.low(u,v),E.high(u,v)
                jl,ju=E.high(il,div(lo,D)),E.low(iu,div(hi,D))
                lo,hi,depth,steps=quantize(jl,ju,lo,hi,depth)
                root['newton'].append({'old_grid_interval':gr(oldlo,oldhi),'point':zi(a.q),
                    'scaled_adjacent_values':[zi(pm.q),zi(pn.q)],'derivative_range':iv(dl,du),
                    'second_derivative_bound':rf(M),'raw_newton_image':iv(il,iu),'intersected_image':iv(jl,ju),
                    'new_grid_interval':gr(lo,hi),'binary_halvings':int(steps.q),'depth':int(depth.q)})
                E.mark('stopping and output')
                if E.cmp('<=',div(sub(hi,lo),D),NODE_GATE):
                    final,nr,wr,outs=weights(n,lo,hi,depth)
                    root['final']=final
                    maxnr,maxwr=E.high(maxnr,nr),E.high(maxwr,wr)
                    neg=[sub(C[0],outs[1]),sub(C[0],outs[0]),E.cp(outs[2]),E.cp(outs[3])]
                    E.file.write(json.dumps(['output','negative',n,*[x.i for x in neg]])+'\n')
                    root['negative_node']=iv(neg[0],neg[1]); root['negative_weight']=iv(neg[2],neg[3])
                    inventory=add(inventory,C[2]); done=True; break
            if not done: raise Stop('bounded Newton schedule')
        E.mark('zero node and degree inventory')
        pm,pn=ev(n,C[0])
        E.need(E.cmp('==',pn,C[0]),'exact zero node')
        E.need(E.cmp('!=',pm,C[0]),'simple zero node')
        d0=mul(C[n],div(pm,DEN[n-1])); w0=div(C[2],mul(d0,d0))
        z=[E.cp(C[0]),E.cp(C[0]),E.cp(w0),E.cp(w0)]
        E.file.write(json.dumps(['output','zero',n,*[x.i for x in z]])+'\n')
        row['zero_node']={'node':iv(z[0],z[1]),'weight':iv(z[2],z[3]),
                          'scaled_adjacent_values':[zi(pm.q),zi(pn.q)]}
        inventory=add(inventory,C[1])
        total=add(mul(C[2],count),C[1])
        E.need(E.cmp('==',total,C[n]),'degree inventory')
        row['total_nodes']=int(total.q)
    E.mark('global checks')
    required=add(add(C[63],C[81]),C[117])
    E.need(E.cmp('==',inventory,required),'global inventory')
    E.need(E.cmp('<=',maxnr,TOL),'global node accuracy')
    E.need(E.cmp('<=',maxwr,TOL),'global weight accuracy')
    report['summary']={'all_nodes':int(inventory.q),'all_weights':int(inventory.q),
        'maximum_node_radius':rf(maxnr),'maximum_weight_radius':rf(maxwr),
        'all_node_and_weight_radii_pass':True}

try:
    main(); report['result']='PASS_REGISTER_PROGRAM_AND_ALL_ACCURACY_GUARDS'
except Stop as exc:
    report['result']='PRESCRIPTION_STOPPED';report['failures'].append(str(exc))
finally:
    E.file.close()
report['scalar_work']={'complete_register_cost':E.cost,'required_upper':CAP,'headroom':CAP-E.cost,
    'by_category':dict(E.by),'register_count':E.next,
    'convention':'arithmetic+destination assignment2; comparison1; literal/copy1; division zero guard counted; fixed static program unrolling'}
report['guard_counts']=dict(E.guards)
report['script_sha256']=sha256(HERE.read_bytes()).hexdigest()
report['trace_sha256']=sha256(TRACE.read_bytes()).hexdigest()
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(report['result'])
print('Scalar register work:',E.cost,'; required <=',CAP,'; headroom:',CAP-E.cost)
print('Completed degrees:',[r.get('total_nodes',0) for r in report['rows']])
print('Separate radii required <=2^-512; all pass:',report.get('summary',{}).get('all_node_and_weight_radii_pass',False))
print('Failures:',report['failures'])
print('Full evidence:',OUT.relative_to(HERE.parents[2]),TRACE.relative_to(HERE.parents[2]))
if report['failures']: raise SystemExit(1)
