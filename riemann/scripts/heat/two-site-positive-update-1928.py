"""One approved two-site Uvarov whole-collar test; exact rational enclosures.
No subdivision, sweep, solver, changed mass or refined input.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = Path(__file__).with_suffix('.json')
spec = importlib.util.spec_from_file_location('collar1925', HERE/'two-site-actual-collar-1925.py')
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
arith, I, D = old.arith, old.I, old.D
record = old.record


def constant(x):
    return D(I.lift(x), I.lift(0), I.lift(0))


def square(x):
    # Exact univariate square range, retaining BOTH complete derivatives.
    return D(old.power(x.v, 2), 2*x.v*x.a, 2*x.v*x.b)


def poly_value(coeff, x):
    result = constant(0)
    for c in reversed(coeff):
        result = result*x + D(c, I.lift(0), I.lift(0))
    return result


def main():
    paths = [HERE/'low-time-h2-uniform-195.json', HERE/'low-time-h2-audit-197.json']
    source, audit = [json.loads(p.read_bytes()) for p in paths]
    assert audit['status'] == 'passed' and not audit['failures']
    hashes = {name: sha256((ROOT/name).read_bytes()).hexdigest() == digest
              for name, digest in audit['input_sha256'].items()}
    assert all(hashes.values())
    selected = {str(k): source['panels'][0]['moments'][str(k)] for k in (0,2,4,6,8)}
    assert all(v == audit['panels'][0]['moments'][k] for k,v in selected.items())
    assert arith.box(source['panels'][0]['lambda']) == (F(0),F(1,5120))
    prior = json.loads((HERE/'two-site-actual-collar-1925.json').read_bytes())
    prior_check = json.loads((HERE/'two-site-actual-collar-check-1925.json').read_bytes())
    assert not prior_check['failures'] and prior_check['status'] == 'passed'
    assert prior['selected_inputs'] == selected
    for saved in (prior, prior_check):
        assert all(sha256((ROOT/n).read_bytes()).hexdigest() == h
                   for n,h in saved['input_sha256'].items())
    raw = {k:I(arith.box(v),'input',('/panels/0/moments/'+k,)) for k,v in selected.items()}
    assert raw['0'].pair[0] > 0
    mu = {k:raw[str(k)]/raw['0'] for k in (2,4,6,8)}
    u,v,w = [mu[k] for k in (2,4,6)]
    h2 = v-old.power(u,2)
    assert u.pair[0]>0 and h2.pair[0]>0
    alpha = v/u
    h3 = w-old.power(v,2)/u
    assert h3.pair[0]>0
    A = (w-u*v)/h2
    B = (u*w-old.power(v,2))/h2
    zero,one = I.lift(0),I.lift(1)
    polynomials = [[one],[zero,one],[-u,zero,one],
                   [zero,-alpha,zero,one],[B,zero,-A,zero,one]]
    norms = [one,u,h2,h3]
    base = {'polynomials':[[record(c) for c in p] for p in polynomials],
            'norms':[record(h) for h in norms]}
    bj = {j:mu[2*j]*F(factorial(j),factorial(2*j)) for j in range(1,5)}
    b1,b2,b3,b4 = [bj[j] for j in range(1,5)]
    q2=-6*(old.power(b1,2)-b2)
    q3=4*(b3-3*b1*b2+2*b1**3)
    q4=b4-4*b1*b3+6*b1**2*b2-3*b1**4
    Va=-q2/2
    Ta=-3*q3/4
    Qa=q2**2/2-q4
    assert Va.pair[0]>0
    gamma=Ta/(Va*Va.sqrt())
    ka=Qa/(Va**2)
    actual={'variance':record(Va),'gamma':record(gamma),'k':record(ka)}

    def reference(a,b):
        sites=[D(a,I.lift(1),I.lift(0)),D(b,I.lift(0),I.lift(1))]
        pa,pb=[[poly_value(p,x) for p in polynomials] for x in sites]
        h=[D(n,I.lift(0),I.lift(0)) for n in norms]
        kaa=sumdual([square(pa[j]).divide(h[j]) for j in range(4)])
        kbb=sumdual([square(pb[j]).divide(h[j]) for j in range(4)])
        kab=sumdual([(pa[j]*pb[j]).divide(h[j]) for j in range(4)])
        # det(I+K) = 1 + trace(K) + sum of squared 2x2 minors.
        terms=[]
        for j in range(4):
            for l in range(j+1,4):
                minor=pa[j]*pb[l]-pa[l]*pb[j]
                terms.append(square(minor).divide(h[j]*h[l]))
        delta=constant(1)+kaa+kbb+sumdual(terms)
        saved={'site_values':[[x.encode() for x in values] for values in (pa,pb)],
               'kernel':{'aa':kaa.encode(),'ab':kab.encode(),'bb':kbb.encode()},
               'positive_minor_terms':[x.encode() for x in terms],
               'update_divisor':delta.encode()}
        if delta.v.pair[0]<=0:
            saved['blocked']='update divisor lower bound not positive'
            return saved,None,None
        wa=(pa[4]*(constant(1)+kbb)-pb[4]*kab).divide(delta)
        wb=(pb[4]*(constant(1)+kaa)-pa[4]*kab).divide(delta)
        coeff=[]
        for k in range(4):
            ka_coeff=sumdual([(pa[j]*D(polynomials[j][k],I.lift(0),I.lift(0))).divide(h[j])
                              for j in range(k,4)])
            kb_coeff=sumdual([(pb[j]*D(polynomials[j][k],I.lift(0),I.lift(0))).divide(h[j])
                              for j in range(k,4)])
            coeff.append(D(polynomials[4][k],I.lift(0),I.lift(0))-wa*ka_coeff-wb*kb_coeff)
        saved['update_weights']=[wa.encode(),wb.encode()]
        saved['coefficients']=[x.encode() for x in coeff]
        # Preserve the prescribed Newton-sum evaluation and complete derivatives.
        c0,c1,c2,c3=coeff
        p1=-c3
        p2=-(c3*p1+c2.scale(2))
        r1,r2=p1.scale(F(1,4)),p2.scale(F(1,4))
        variance=r2-r1**2
        saved['predivision_variance']=variance.encode()
        if variance.v.pair[0]<=0:
            saved['blocked']='variance lower bound not positive'
            return saved,None,None
        obs,values,J=old.observables(coeff)
        saved.update(obs)
        return saved,values,J

    point,fp,Jp=reference(I.lift(0),I.lift(1))
    midpoint=None
    if Jp is not None:
        midpoint=[[sum(x.pair)/2 for x in row] for row in Jp]
        a,b=midpoint[0]
        c,d=midpoint[1]
        det=a*d-b*c
        assert det!=0
        Rp=[[d/det,-b/det],[-c/det,a/det]]
    collar,fb,Jb=reference(I((F(-1,4),F(1,4)),'box_input',('a',)),
                           I((F(3,4),F(5,4)),'box_input',('b',)))
    orientations={}
    for sign in (1,-1):
        result={'krawczyk_evaluated':False,'range_exclusion_evaluated':False}
        if fp is None or fb is None:
            result.update(status='inconclusive_unpaid_variance' if fb is None and
                          collar.get('blocked')=='variance lower bound not positive'
                          else 'inconclusive_unpaid_bound',
                          blocked=collar.get('blocked') or point.get('blocked'))
        else:
            R=[[row[0]*sign,row[1]] for row in Rp]
            residual=[sign*fb[0]-gamma,fb[1]-ka]
            z=[sign*fp[0]-gamma,fp[1]-ka]
            J=[[x*sign for x in Jb[0]],Jb[1]]
            X=[I((F(-1,4),F(1,4)),'box_input',('X'+str(j),)) for j in range(2)]
            K=[-sum((R[i][j]*z[j] for j in range(2)),I.lift(0))+
               sum(((int(i==j)-sum((R[i][l]*J[l][j] for l in range(2)),I.lift(0)))*X[j]
                    for j in range(2)),I.lift(0)) for i in range(2)]
            included=all(F(-1,4)<x.pair[0]<=x.pair[1]<F(1,4) for x in K)
            excluded=any(not x.pair[0]<=0<=x.pair[1] for x in residual)
            result.update(R=[[str(x) for x in row] for row in R],
                          range=[record(x) for x in residual],K=[record(x) for x in K],
                          strict_inclusion=included,range_exclusion=excluded,
                          status='included' if included else ('excluded' if excluded else 'inconclusive'),
                          krawczyk_evaluated=True,range_exclusion_evaluated=True)
        orientations[str(sign)]=result
    inputs=paths+[Path(__file__),HERE/'two-site-actual-collar-1925.py',
                   HERE/'two-site-theta-jacobian-1921.py',HERE/'two-site-theta-jacobian-check-1921.py',
                   HERE/'two-site-actual-collar-1925.json',HERE/'two-site-actual-collar-check-1925.json']
    result={'status':'fixed_collar_test_completed','selected_inputs':selected,
            'fixed_box':[['-1/4','1/4'],['3/4','5/4']],
            'accepted_audit_hash_checks':hashes,
            'input_sha256':{str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in inputs},
            'base':base,'actual':actual,'point':point,'collar':collar,
            'point_midpoint':None if midpoint is None else [[str(x) for x in row] for row in midpoint],
            'orientations':orientations,'trace':arith.TRACE,'divisors':arith.DIVISORS,
            'failures':[],
            'qualification':'Conditional L917/L037; failed sufficient enclosure is not nonexistence',
            'required':'positive base norms, update divisor and variance before normalized range/Jacobian/Krawczyk'}
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    summary={'status':{k:v['status'] for k,v in orientations.items()},
             'norms': [display(x) for x in norms],
             'collar_update_divisor':display_record(collar['update_divisor']['value']),
             'collar_variance':display_record(collar.get('predivision_variance',{}).get('value')),
             'point_blocked':point.get('blocked'),'collar_blocked':collar.get('blocked'),
             'required':result['required'],'failures':[],
             'certificate':str(OUT.relative_to(ROOT))}
    print(json.dumps(summary))


def sumdual(xs):
    return sum(xs[1:],xs[0]) if xs else constant(0)


def display(x):
    return display_record(record(x))


def display_record(x):
    if x is None:
        return None
    # These exact, deliberately weaker bounds are display only.
    lo,hi=F(x['lower']),F(x['upper'])
    scale=10**6
    return {'lower':str(F((lo*scale).__floor__(),scale)),
            'upper':str(F((hi*scale).__ceil__(),scale))}


if __name__=='__main__':
    main()
