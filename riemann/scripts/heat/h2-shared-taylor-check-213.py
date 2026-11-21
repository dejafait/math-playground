"""Independent rational inclusion replay plus separate complete quadrature replay.

Uses the same inspected L037 Decimal/jet primitives for quadrature only.
Does not verify the Decimal library. No refinement of the test budget.
"""
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as F
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE/'h2-shared-taylor-213.json'
OUT = Path(__file__).with_suffix('.json')
sys.set_int_max_str_digits(100000)


class Q:
    def __init__(self,a,b=None):
        if isinstance(a,dict):
            self.a,self.b = F(a['lower']),F(a['upper'])
        else:
            self.a,self.b = F(a),F(a if b is None else b)
        assert self.a <= self.b

    @staticmethod
    def lift(a):
        return a if isinstance(a,Q) else Q(a)

    def __add__(self,b):
        b=Q.lift(b)
        return Q(self.a+b.a,self.b+b.b)

    __radd__=__add__

    def __neg__(self):
        return Q(-self.b,-self.a)

    def __sub__(self,b):
        return self+-Q.lift(b)

    def __mul__(self,b):
        b=Q.lift(b)
        c=[x*y for x in (self.a,self.b) for y in (b.a,b.b)]
        return Q(min(c),max(c))

    __rmul__=__mul__

    def __truediv__(self,b):
        b=Q.lift(b)
        assert not b.a <= 0 <= b.b
        return self*Q(1/b.b,1/b.a)

    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        # Same enclosing endpoint multiplication rule; exact arithmetic.
        a=Q(1)
        x=self
        while n:
            if n%2:
                a=a*x
            x=x*x
            n//=2
        return a

    def contains(self,b):
        b=Q.lift(b)
        return self.a <= b.a <= b.b <= self.b

    def data(self):
        return {'lower':str(self.a),'upper':str(self.b)}


def polynomial_range(c):
    return c[0]+c[1]*Q(-1,1)+c[2]*Q(0,1)


def convolution(a,b):
    return [sum((a[j]*b[n-j] for j in range(3) if 0<=n-j<3),Q(0))
            for n in range(5)]


def product(a,ar,b,br):
    c=convolution(a,b)
    discarded=c[3]*Q(-1,1)+c[4]*Q(0,1)
    return c[:3],discarded+polynomial_range(a)*br+polynomial_range(b)*ar+ar*br


def negative_exp(x):
    term=F(1)
    total=term
    for j in range(1,1001):
        term*=x/j
        total+=term
    following=term*x/1001
    assert 0<=x<F(1002)
    return Q(1/(total+following/(1-x/1002)),1/total)


def main():
    saved=json.loads(SOURCE.read_text())
    report={'status':'running','failures':[],
            'scope':'Exact rational trace/tail/seed replay and all quadrature records; shared Decimal primitives, not independently verified library',
            'input_sha256':{str(p.relative_to(HERE.parent.parent)):hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in (SOURCE,Path(__file__),HERE/'h2-shared-taylor-213.py',
                                      HERE/'low-time-h2-uniform-195.py',HERE.parent/'hankel/certify_hankel.py')}}
    # The new tail exponent and coefficient, including every numerical premise.
    beta=F(119,40)
    assert sum((F(4)**j/factorial(j) for j in range(8)),F(0))>50
    assert sum((F(9)**j/factorial(j) for j in range(5)),F(0))>32
    assert 11*beta>9
    space=(128*sum((F(factorial(11),factorial(11-j))*50**(11-j)/beta**(j+1)
                    for j in range(12)),F(0)))*negative_exp(50*beta)
    theta=(128*625*factorial(11))*negative_exp(25*beta-1)
    for key,value in (('spatial',space),('theta',theta),('total',space+theta)):
        assert Q(saved['tails'][key]).contains(value),key
    report['exact_tails']={k:v.data() for k,v in (('spatial',space),('theta',theta),('total',space+theta))}
    spec=importlib.util.spec_from_file_location('replay213',HERE/'h2-shared-taylor-213.py')
    p=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(p)
    base,I=p.base,p.I
    pi=base.pi_bounds()
    assert pi.data()==saved['pi']
    # Different loop order, complete midpoint jets and eighth coefficients.
    # Kernels are prepared once, moments outermost; no producer quadrature call.
    quadrature_replay=[]
    for key,exact_lam in (('center',F(1,10240)),('right',F(1,5120))):
        row=saved['quadrature'][key]
        lam=I.rational(exact_lam)
        assert row['lambda']==lam.data()
        h=I.rational(F(1,64))
        weights={n:2*h**(n+1)/(n+1) for n in (0,2,4,6)}
        rw=2*h**9/9
        cache=[]
        assert len(row['spatial_records'])==64
        for j,record in enumerate(row['spatial_records']):
            c=I.rational(F(2*j+1,64))
            d=I(I.rational(F(2*j,64)).lo,I.rational(F(2*j+2,64)).hi)
            assert record['index']==j and record['center']==c.data() and record['domain']==d.data()
            cache.append((c,d,base.multiply(base.theta_kernel_jet(c,pi),p.p.tilt_jet(c,lam)),
                          base.multiply(base.theta_kernel_jet(d,pi),p.p.tilt_jet(d,lam))))
        checked={}
        for k in range(0,20,2):
            integral,error_sum=I(0),I(0)
            for j,(c,d,kc,kd) in enumerate(cache):
                mid=base.moment_jet(c,k,kc)
                dom=base.moment_jet(d,k,kd)
                value=sum((mid[n]*weights[n] for n in weights),I(0))
                err=I(dom[8].magnitude())*rw
                expected={'midpoint_coefficients':[a.data() for a in mid],
                          'eighth_coefficient':dom[8].data(),
                          'polynomial_integral':value.data(),'error':err.data()}
                assert row['spatial_records'][j]['orders'][str(k)]==expected,(key,j,k)
                integral=integral+value+I(err.hi.copy_negate(),err.hi)
                error_sum=error_sum+err
            result=integral+I(0,saved['tails']['total']['upper'])
            assert result.data()==row['moments'][str(k)],(key,k)
            assert error_sum.data()==row['quadrature_error_bounds'][str(k)],(key,k)
            checked[str(k)]={'moment':result.data(),'error':error_sum.data()}
        quadrature_replay.append({'point':key,'checked':checked})
        print(f'Complete separate quadrature replay: {key}',flush=True)
    report['quadrature_replay']=quadrature_replay
    trace=saved['trace']
    seeds={v:int(k) for k,v in saved['moment_models'].items()}
    expected_trace=[]
    radius=F(1,10240)
    for j,node in enumerate(trace):
        assert node['id']==j and all(a<j for a in node['args'])
        op=node['op']
        parents=[trace[a] for a in node['args']]
        cc=[[Q(v) for v in a['coefficients']] for a in parents]
        rr=[Q(a['remainder']) for a in parents]
        if op=='seed':
            k=seeds[j]
            c=[Q(saved['quadrature']['center']['moments'][str(k+2*n)])*(radius**n/F(factorial(n)))
               for n in range(3)]
            bound=(Q(saved['quadrature']['right']['moments'][str(k+6)])*F(radius**3,6)).b
            r=Q(-bound,bound)
            assert node['label']==f'M{k}'
        elif op=='constant':
            c=[Q(node['label']),Q(0),Q(0)]; r=Q(0)
        elif op=='add':
            c=[a+b for a,b in zip(*cc)]; r=rr[0]+rr[1]
        elif op=='neg':
            c=[-a for a in cc[0]]; r=-rr[0]
        elif op=='scale':
            c=[a*F(node['extra']) for a in cc[0]]; r=rr[0]*F(node['extra'])
        elif op=='mul':
            c,r=product(cc[0],rr[0],cc[1],rr[1])
        elif op=='remove_constant':
            c=[Q(0),cc[0][1],cc[0][2]]; r=rr[0]
        elif op=='inverse':
            a,v,v2=cc
            a0=a[0]
            whole=polynomial_range(a)+rr[0]
            # Use saved widened divisor/geometric intervals: directed intermediates
            # can be wider than an all-rational fused expression.
            divisor=Q(node['extra']['divisor_range'])
            assert divisor.contains(whole) and divisor.a>0 and a0.a>0
            geometric=-((polynomial_range(v)+rr[1])**3)/(a0**3*divisor)
            g=Q(node['extra']['geometric_remainder'])
            assert g.contains(geometric)
            c=[Q(1)/a0+v2[0]/a0**3,
               -v[1]/a0**2+v2[1]/a0**3,
               -v[2]/a0**2+v2[2]/a0**3]
            r=-rr[1]/a0**2+rr[2]/a0**3+g
            assert parents[1]['op']=='remove_constant' and parents[1]['args']==[parents[0]['id']]
            assert parents[2]['op']=='mul' and parents[2]['args']==[parents[1]['id']]*2
        else:
            raise AssertionError(op)
        assert all(Q(a).contains(b) for a,b in zip(node['coefficients'],c)),('coefficient',j,op)
        assert Q(node['remainder']).contains(r),('remainder',j,op)
        expected_trace.append({'id':j,'op':op,'exact_coefficients':[a.data() for a in c],
                               'exact_remainder':r.data(),'containment':True})
    report['rational_trace']=expected_trace
    # Verify the finite expression structure all the way from inputs to minors.
    def is_scaled(node_id,source,factor):
        a=trace[node_id]
        assert a['op']=='scale' and a['args']==[source] and F(a['extra'])==factor
    mass_id=saved['moment_models']['0']
    inv=saved['inverse_mass']
    assert trace[inv]['op']=='inverse' and trace[inv]['args'][0]==mass_id
    q=saved['q_models']
    for n in range(1,7):
        a=trace[q[n]]; assert a['op']=='scale' and F(a['extra'])==F((-1)**n,factorial(2*n))
        prod=trace[a['args'][0]]
        assert prod['op']=='mul' and prod['args']==[saved['moment_models'][str(2*n)],inv]
    # An independent exact-rational expression evaluator mirrors only the finite
    # mathematical recurrence, never the producer's TM class.
    class Model:
        def __init__(self,c,r): self.c,self.r=c,r
        def __add__(self,b): return Model([a+d for a,d in zip(self.c,b.c)],self.r+b.r)
        def __neg__(self): return Model([-a for a in self.c],-self.r)
        def __sub__(self,b): return self+-b
        def __mul__(self,b): return Model(*product(self.c,self.r,b.c,b.r))
        def scale(self,v): return Model([a*v for a in self.c],self.r*v)
    def m(node_id):
        node=trace[node_id]; return Model([Q(v) for v in node['coefficients']],Q(node['remainder']))
    ss={}
    for n in range(1,7):
        raw=m(q[n]).scale(-n)
        for k in range(1,n): raw=raw-m(saved['S_models'][str(k)])*m(q[n-k])
        dest=m(saved['S_models'][str(n)])
        # Different subtraction grouping may widen endpoints differently;
        # check the exact producer expression's sum-then-negate structure too.
        total=Model([Q(0)]*3,Q(0))
        for k in range(1,n): total=total+m(saved['S_models'][str(k)])*m(q[n-k])
        exact=m(q[n]).scale(-n)-total
        assert all(a.contains(b) for a,b in zip(dest.c,exact.c)) and dest.r.contains(exact.r)
        ss[n]=dest
    a,b,c,d,e=[ss[n] for n in range(2,7)]
    exact_minors=[a,a*c-b*b,a*(c*e-d*d)-b*(b*e-d*c)+c*(b*d-c*c)]
    for node_id,exact in zip(saved['minor_models'],exact_minors):
        dest=m(node_id)
        assert all(u.contains(v) for u,v in zip(dest.c,exact.c)) and dest.r.contains(exact.r)
    final=m(saved['minor_models'][2])
    full=polynomial_range(final.c)+final.r
    assert Q(saved['summary']['determinant']).contains(full)
    assert full.a<0<full.b
    assert full.a>F('-4.482e-31') and full.b<F('1.073e-30')
    assert Q(saved['summary']['final_remainder']).a>F('-4.893e-37')
    assert Q(saved['summary']['final_remainder']).b<F('4.893e-37')
    assert Q(saved['summary']['mass_range']).a>F('.49712')
    assert Q(saved['tails']['total']).b<F('4.345e-20')
    # The final constant coefficient interval alone already straddles zero.
    assert final.c[0].a<0<final.c[0].b
    for ctx in saved['arithmetic'].values():
        assert ctx['precision']==100 and all(ctx['traps'].values()) and not any(ctx['exceptional_flags'].values())
    report['final_model']={'coefficients':[a.data() for a in final.c],
                           'remainder':final.r.data(),'range':full.data()}
    report['status']='passed'
    report['summary']={'quadrature_points':2,'full_moments_replayed':20,
                       'spatial_moment_records_replayed':1280,'trace_nodes_replayed':len(trace),
                       'all_exact_containments':True,'failures':[],
                       'determinant_required':'>0 lower endpoint',
                       'determinant_outer_bound':['-4.482e-31','1.073e-30'],
                       'zero_containing':True,'constant_coefficient_zero_containing':True,
                       'no_budget_refinement':True}
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report['summary'],indent=2))
    print(f'Full replay evidence: {OUT.relative_to(HERE.parent.parent)}')


if __name__=='__main__':
    main()
