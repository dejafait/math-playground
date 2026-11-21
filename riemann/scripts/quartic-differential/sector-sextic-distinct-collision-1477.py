"""Exact fixed-distinct-root collision calculation; discovery is labeled."""
from fractions import Fraction as F
from pathlib import Path
import json
import numpy as np

def trim(p):
    p=list(p)
    while len(p)>1 and not p[-1]: p.pop()
    return p
def add(p,q):
    return trim([(p[i] if i<len(p) else F(0))+(q[i] if i<len(q) else F(0))
                 for i in range(max(len(p),len(q)))])
def neg(p): return [-v for v in p]
def sub(p,q): return add(p,neg(q))
def scale(p,c): return trim([v*c for v in p])
def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]+=a*b
    return trim(r)
def der(p): return trim([i*p[i] for i in range(1,len(p))] or [F(0)])
def val(p,x):
    r=F(0)
    for a in reversed(p): r=r*x+a
    return r
def shift(p,d):
    r=[F(0)]
    for a in reversed(p): r=add(mul(r,[d,F(1)]),[a])
    return r
def image(p,t): return add(add(p,der(p)),scale(der(der(p)),t))
def encode(p): return [str(c) for c in p]

class I:
    def __init__(self,lo,hi=None): self.lo,self.hi=F(lo),F(lo if hi is None else hi)
    def __add__(self,q):
        q=q if isinstance(q,I) else I(q)
        return I(self.lo+q.lo,self.hi+q.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,q): return self+-q if isinstance(q,I) else self+(-I(q))
    def __mul__(self,q):
        q=q if isinstance(q,I) else I(q)
        v=[a*b for a in [self.lo,self.hi] for b in [q.lo,q.hi]]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,q):
        q=q if isinstance(q,I) else I(q)
        if q.lo<=0<=q.hi: raise ValueError('division by zero-containing interval')
        return self*I(1/q.hi,1/q.lo)
    def encode(self): return [str(self.lo),str(self.hi)]
def ival(p,x):
    r=I(0)
    for a in reversed(p): r=r*x+a
    return r

R=list(map(F,[4,0,-5,0,1]))
checks={}
record={'status':'IN_PROGRESS_EXACT_CALCULATION', 'R_ascending':encode(R),
        'parameter_interval':['1/4','5/18'], 'checks':checks,
        'discovery_only':[], 'limitations':['No general four-root or product exclusion.']}
for t in [F(1,4),F(5,18)]:
    B=image(R,t); A=image([F(0)]+R,t); C=image([F(0),F(0)]+R,t)
    K=add(R,scale(der(R),2*t))
    roots=np.roots(list(map(float,reversed(B))))
    info=[]
    for a in sorted(roots.real):
        k=float(val(K,a)); phi=a+float(t)*float(val(R,a))/k
        info.append({'root_TR_approx':float(a),'K_approx':k,'threshold_approx':-2*phi})
    record['discovery_only'].append({'t':str(t),'reference_roots':info})
    d=F(0)
    av,bv,cv=val(A,d),val(B,d),val(C,d)
    ap,bp,cp=val(der(A),d),val(der(B),d),val(der(C),d)
    delta=av*bp-ap*bv
    nb=bv*cp-cv*bp; nc=cv*ap-av*cp
    b,c=nb/delta,nc/delta
    P=mul(R,[c,b,F(1)]); out=image(P,t)
    checks['collision_at_zero_'+str(t)]=(out[0]==out[1]==0)
    record.setdefault('zero_collisions',[]).append({'t':str(t),'delta':str(delta),
        'b':str(b),'c':str(c),'pair_margin':str(c-b*b/4),
        'input_ascending':encode(P),'output_ascending':encode(out),
        'residual_quartic_ascending':encode(out[2:])})

# Uniform reference-root proof. Floating roots only propose rational boxes.
# Every accepted box is checked with exact endpoint signs over the WHOLE
# t-cell, and all subsequent enclosures use rational interval arithmetic.
cells=[]
for j in range(32):
    tl=F(1,4)+F(j,32)*F(1,36); th=F(1,4)+F(j+1,32)*F(1,36)
    ti=I(tl,th)
    endpoint_roots=[sorted(np.roots(list(map(float,reversed(image(R,t))))).real)
                    for t in [tl,th]]
    boxes=[]
    for k in range(4):
        lo=F(int(np.floor(min(v[k] for v in endpoint_roots)*10000))-1,10000)
        hi=F(int(np.ceil(max(v[k] for v in endpoint_roots)*10000))+1,10000)
        yi=I(lo,hi)
        # J(y,t) is affine in t for fixed y, so endpoint extrema are exact.
        left=I(min(val(image(R,t),lo) for t in [tl,th]),
               max(val(image(R,t),lo) for t in [tl,th]))
        right=I(min(val(image(R,t),hi) for t in [tl,th]),
                max(val(image(R,t),hi) for t in [tl,th]))
        expect_left,expect_right=((1,-1) if k%2==0 else (-1,1))
        sign=lambda z,s: z.lo>0 if s>0 else z.hi<0
        checks[f'cell{j}_root{k}_endpoint_signs']=sign(left,expect_left) and sign(right,expect_right)
        ki=ival(R,yi)+2*ti*ival(der(R),yi)
        checks[f'cell{j}_root{k}_K_sign']=sign(ki,1 if k%2==0 else -1)
        ph=yi+ti*ival(R,yi)/ki
        threshold=-2*ph
        boxes.append({'root_interval':yi.encode(),'J_left_interval':left.encode(),
                      'J_right_interval':right.encode(),'K_interval':ki.encode(),
                      'threshold_interval':threshold.encode()})
    checks[f'cell{j}_root_boxes_disjoint']=all(F(boxes[k]['root_interval'][1])<F(boxes[k+1]['root_interval'][0]) for k in range(3))
    gaps=[F(boxes[k]['threshold_interval'][0])-F(boxes[k+1]['threshold_interval'][1]) for k in range(3)]
    checks[f'cell{j}_thresholds_strictly_ordered']=all(g>0 for g in gaps)
    cells.append({'t_interval':ti.encode(),'roots':boxes,'threshold_gap_lower_bounds':[str(g) for g in gaps]})
record['uniform_reference_certificate']={'cells':cells,'cell_count':len(cells),
    'minimum_threshold_gap_lower_bound':str(min(F(g) for cell in cells for g in cell['threshold_gap_lower_bounds'])),
    'minimum_absolute_K_lower_bound':str(min(min(abs(F(x)) for x in root['K_interval']) for cell in cells for root in cell['roots']))}

# The following compact rational table is implied by every saved interval,
# not by evaluating a finite list of t values.
coarse=[{'root':[-4,-3],'K':[20,60],'threshold':[5,7]},
        {'root':[-2,-1],'K':[-6,-4],'threshold':[3,4]},
        {'root':[0,1],'K':[3,4],'threshold':[-1,0]},
        {'root':[1,2],'K':[-4,-2],'threshold':[-4,-3]}]
for k,row in enumerate(coarse):
    for field,source in [('root','root_interval'),('K','K_interval'),('threshold','threshold_interval')]:
        checks[f'all_cells_root{k}_coarse_{field}']=all(F(row[field][0])<F(cell['roots'][k][source][0]) and F(cell['roots'][k][source][1])<F(row[field][1]) for cell in cells)
record['coarse_uniform_table']=coarse

# Sparse exact bivariate algebra in d,t, independent of the interval proof.
def ba(*args):
    out={}
    for p in args:
        for e,c in p.items(): out[e]=out.get(e,F(0))+c
    return {e:c for e,c in out.items() if c}
def bs(p,c): return {e:v*c for e,v in p.items() if v*c}
def bm(*args):
    out={(0,0):F(1)}
    for p in args:
        nxt={}
        for (i,j),a in out.items():
            for (k,l),b in p.items(): nxt[i+k,j+l]=nxt.get((i+k,j+l),F(0))+a*b
        out={e:c for e,c in nxt.items() if c}
    return out
def bd(p): return {(i-1,j):i*c for (i,j),c in p.items() if i}
def bc(c): return {(0,0):F(c)} if c else {}
def be(p): return [{'d_power':i,'t_power':j,'coefficient':str(c)} for (i,j),c in sorted(p.items())]
dd={(1,0):F(1)}; tt={(0,1):F(1)}
rr={(i,0):c for i,c in enumerate(R) if c}
bt=lambda p: ba(p,bd(p),bm(tt,bd(bd(p))))
bb=bt(rr); aa=bt(bm(dd,rr)); cc=bt(bm(dd,dd,rr))
de=ba(bm(aa,bd(bb)),bs(bm(bd(aa),bb),-1))
nb=ba(bm(bb,bd(cc)),bs(bm(cc,bd(bb)),-1))
nc=ba(bm(cc,bd(aa)),bs(bm(aa,bd(cc)),-1))
r1=bd(rr); r2=bs(bd(r1),F(1,2))
e=ba(bs(bm(r1,r1),3),bs(bm(rr,r2),-8))
ne=ba(bm(ba(bs(tt,2),bc(-2)),rr,rr),bs(bm(tt,rr,r1),-6),
      bs(bm(tt,tt,r1,r1),-12),bs(bm(tt,tt,rr,r2),12))
square=ba(bm(tt,r1),bs(rr,F(2,5)))
ne_completion=ba(bs(bm(square,square),-F(15,2)),bs(bm(tt,tt,e),-F(3,2)),
                 bm(ba(bs(tt,2),bc(-F(4,5))),rr,rr))
checks['shifted_c_numerator_identity']=ba(nc,bm(dd,nb),bm(dd,dd,de))==ne
checks['negative_numerator_square_completion']=ne==ne_completion
e_square=ba(bs(bm(ba(bm(dd,dd),bc(-F(23,20))),ba(bm(dd,dd),bc(-F(23,20)))),40),bc(F(1071,10)))
checks['E_square_completion']=e==e_square
checks['negative_numerator_uniform_bound_arithmetic']=F(3,2)*F(1,16)*F(1071,10)==F(3213,320)
checks['cramer_first_identity']=ba(bm(aa,nb),bm(bb,nc),bm(cc,de))=={}
checks['cramer_second_identity']=ba(bm(bd(aa),nb),bm(bd(bb),nc),bm(bd(cc),de))=={}
record['collision_algebra']={'variables':['d','t'],
    'A':be(aa),'B':be(bb),'C':be(cc),'delta':be(de),'N_b':be(nb),'N_c':be(nc),
    'shifted_c_numerator':be(ne),'E':be(e),
    'admissibility':'delta<0 and M=4*N_c*delta-N_b^2>0; b=N_b/delta, c=N_c/delta',
    'uniform_shifted_c_numerator_upper_bound':'-3213/320',
    'singular_consistency':'would require shifted_c_numerator=0; impossible',
    'residual_formula':'H coefficients in z=y-d are shifted_output[2:7]; full input/output coefficients are recorded for both zero collisions'}
record['cell_summaries']=[{'t':c['t_interval'],
    'endpoint_sign_checks':all(checks[f'cell{j}_root{k}_endpoint_signs'] for k in range(4)),
    'K_sign_checks':all(checks[f'cell{j}_root{k}_K_sign'] for k in range(4)),
    'disjoint':checks[f'cell{j}_root_boxes_disjoint'],
    'threshold_order':checks[f'cell{j}_thresholds_strictly_ordered']} for j,c in enumerate(cells)]
record['root_box_table_10000']=[[j]+[int(10000*F(x)) for r in cell['roots'] for x in r['root_interval']] for j,cell in enumerate(cells)]
record['algebra_checks']={n:v for n,v in checks.items() if not n.startswith(('cell','all_cells'))}
record['coarse_table_checks']={n:v for n,v in checks.items() if n.startswith('all_cells')}
record['minimum_signed_endpoint_margin']=str(min((F(root[key][0]) if s>0 else -F(root[key][1])) for cell in cells for k,root in enumerate(cell['roots']) for key,s in [('J_left_interval',1 if k%2==0 else -1),('J_right_interval',-1 if k%2==0 else 1)]))
record['actual_bounds']={'reference_roots':'four distinct simple roots for each t, by four disjoint IVT brackets',
    'F_real_roots':'at least four distinct, by strict threshold order and IVT',
    'collision_residual_real_roots':'four distinct simple roots whenever F=(y-d)^2 H',
    'witness':'none in this fixed R family for one quadratic symbol'}
record['required_bounds']={'whole_target':'input two nonreal roots and output four, all saved restrictions',
    'family':'a root-free residual or separately certified pair-removing perturbation; neither exists if the interval checks pass'}
record['status']='EXACT_FIXED_DISTINCT_FAMILY_EXCLUSION' if all(checks.values()) else 'CHECK_FAILURE'
path=Path(__file__).with_suffix('.json')
record['failures']=[n for n,v in checks.items() if not v]
path.write_text(json.dumps(record,indent=2)+'\n')
print('Exact checks:',sum(checks.values()),'/',len(checks))
print('Uniform parameter cells:',len(cells),'cover [1/4,5/18].')
print('Actual: at least four real output roots; collision residual four simple real roots.')
print('Threshold gap lower bound:',record['uniform_reference_certificate']['minimum_threshold_gap_lower_bound'])
print('Shifted Cramer numerator <= -3213/320 < 0; singular consistency requires zero.')
print('Required global target: exact (2,4) witness or whole-class impossibility; not settled.')
print('Failures:',record['failures']);print('Full certificate:',path)
