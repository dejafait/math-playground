"""Independent complete interval trace replay plus base and Gram identities.
Does not import the1928 producer; no new site evaluations or input refinement.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import importlib.util
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
CERT=HERE/'two-site-positive-update-1928.json'
OUT=Path(__file__).with_suffix('.json')
spec=importlib.util.spec_from_file_location('independent1921',HERE/'two-site-theta-jacobian-check-1921.py')
p=importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


def main():
    saved=json.loads(CERT.read_bytes())
    failures=[]
    checks=0
    def check(name,condition):
        nonlocal checks
        checks+=1
        if not condition:
            failures.append(name)
    check('all complete input hashes',all(sha256((ROOT/n).read_bytes()).hexdigest()==h
          for n,h in saved['input_sha256'].items()))
    source=json.loads((HERE/'low-time-h2-uniform-195.json').read_bytes())
    check('all five full raw inputs',saved['selected_inputs']=={
          str(k):source['panels'][0]['moments'][str(k)] for k in (0,2,4,6,8)})
    check('prior audit checks',all(saved['accepted_audit_hash_checks'].values()))
    values=[]
    divisors=[]
    boxes={'a':(F(-1,4),F(1,4)),'b':(F(3,4),F(5,4))}
    for n,row in enumerate(saved['trace']):
        check('sequential id '+str(n),n==row['id'])
        op,ids=row['operation'],row['inputs']
        if op=='constant':
            expected=p.interval(row['interval'])
            check('point constant '+str(n),expected[0]==expected[1] and not ids)
        elif op=='input':
            expected=p.interval(source['panels'][0]['moments'][ids[0].split('/')[-1]])
        elif op=='box_input':
            expected=boxes[ids[0]]
        else:
            operands=ids[:1] if op=='integer_power' else ids
            check('backward operands '+str(n),all(0<=j<n for j in operands))
            x=values[ids[0]]
            if op=='add':
                expected=p.add(x,values[ids[1]])
            elif op=='negate':
                expected=p.neg(x)
            elif op=='multiply':
                expected=p.mul(x,values[ids[1]])
            elif op=='reciprocal':
                check('positive divisor '+str(n),x[0]>0)
                expected=p.reciprocal(x)
                divisors.append({'trace_id':ids[0],'interval':p.enc(x),'excludes_zero':True})
            elif op=='integer_power':
                k=ids[1]
                endpoints=[x[0]**k,x[1]**k]
                if k and not k%2 and x[0]<=0<=x[1]:
                    endpoints.append(F(0))
                expected=p.rounded((min(endpoints),max(endpoints)))
            elif op=='sqrt':
                expected=p.interval(row['interval'])
                check('sqrt full squared inequalities '+str(n),
                      expected[0]>=0 and expected[0]**2<=x[0]<=x[1]<=expected[1]**2)
            else:
                raise ValueError(op)
        check('complete endpoints '+str(n),expected==p.interval(row['interval']))
        values.append(expected)
    check('all divisors',saved['divisors']==divisors)
    def copies(obj):
        if isinstance(obj,dict):
            if 'trace_id' in obj:
                check('result copy '+str(obj['trace_id']),p.interval(obj)==values[obj['trace_id']])
            else:
                for v in obj.values(): copies(v)
        elif isinstance(obj,list):
            for v in obj: copies(v)
    for key in ('base','actual','point','collar','orientations'):
        copies(saved[key])

    # Independent finite polynomial identities. Cleared denominators keep
    # this exact and require no symbolic-algebra package or interval producer.
    def variable(i,n=5):
        e=[0]*n
        e[i]=1
        return {tuple(e):F(1)}
    def const(c,n=5):
        return {(0,)*n:F(c)} if c else {}
    def plus(*args):
        z={}
        for a in args: z=p.padd(z,a)
        return z
    def minus(a,b): return p.padd(a,p.pneg(b))
    def times(*args):
        z=const(1,len(next(iter(args[0]))) if args[0] else 5)
        for a in args: z=p.pmul(z,a)
        return z
    u,v,w=[variable(i) for i in range(3)]
    one=const(1)
    h2=minus(v,times(u,u))
    h3num=minus(times(u,w),times(v,v))
    beta={0:one,2:u,4:v,6:w}
    def moment(k): return beta.get(k,{})
    base=[([one],one),([{},one],one),
          ([p.pneg(u),{},one],one),
          ([{},p.pneg(v),{},u],u),
          ([h3num,{},p.pneg(minus(w,times(u,v))),{},h2],h2)]
    def inner(a,b):
        return plus(*(times(c,d,moment(i+j)) for i,c in enumerate(a) for j,d in enumerate(b)))
    for n,(coeff,denom) in enumerate(base):
        for k in range(n):
            check('base orthogonality '+str(n)+'/'+str(k),
                  plus(*(times(c,moment(i+k)) for i,c in enumerate(coeff)))=={})
    norm_numerators=[one,u,h2,times(u,h3num)]
    for n in range(4):
        check('cleared base norm '+str(n),inner(base[n][0],base[n][0])==norm_numerators[n])
    # For p3 the polynomial numerator is u*p3, so its norm is u^2*h3.
    check('p3 norm division identity',norm_numerators[3]==times(u,h3num))
    # Standard 2-row Gram/Cauchy--Binet identity in eight formal entries.
    xs=[variable(i,8) for i in range(4)]
    ys=[variable(i+4,8) for i in range(4)]
    o=const(1,8)
    aa=plus(*(times(x,x) for x in xs))
    bb=plus(*(times(y,y) for y in ys))
    ab=plus(*(times(x,y) for x,y in zip(xs,ys)))
    direct=minus(times(plus(o,aa),plus(o,bb)),times(ab,ab))
    positive=plus(o,aa,bb,*(times(z,z) for j in range(4) for l in range(j+1,4)
                     for z in [minus(times(xs[j],ys[l]),times(xs[l],ys[j]))]))
    check('complete eight-variable Gram identity',direct==positive)
    # The adjugate used by the producer solves the symmetric two-site system.
    A,B,C,va,vb=[variable(i) for i in range(5)]
    delta=minus(times(A,C),times(B,B))
    wa=minus(times(C,va),times(B,vb))
    wb=minus(times(A,vb),times(B,va))
    check('adjugate first row',plus(times(A,wa),times(B,wb))==times(delta,va))
    check('adjugate second row',plus(times(B,wa),times(C,wb))==times(delta,vb))

    norms=[p.interval(x) for x in saved['base']['norms']]
    required_norms=[(F(1),F(1)),(F(46209,10**6),F(46212,10**6)),
                    (F(3824,10**6),F(3825,10**6)),(F(436,10**6),F(437,10**6))]
    for i,(actual,bounds) in enumerate(zip(norms,required_norms)):
        check('quoted norm bound '+str(i),bounds[0]<=actual[0]<=actual[1]<=bounds[1] and actual[0]>0)
    d=p.interval(saved['collar']['update_divisor']['value'])
    variance=p.interval(saved['collar']['predivision_variance']['value'])
    check('quoted positive update bound',F(573530616,10**6)<d[0]<=d[1]<F(73569449116,10**6))
    check('quoted failed variance',F(-22369279057,10**6)<variance[0]<0<variance[1]<F(34276881561,10**6))
    check('six nonnegative minors',len(saved['collar']['positive_minor_terms'])==6 and all(
          p.interval(x['value'])[0]>=0 for x in saved['collar']['positive_minor_terms']))
    check('point paid', 'blocked' not in saved['point'] and 'jacobian' in saved['point'])
    check('collar stopped at variance',saved['collar']['blocked']=='variance lower bound not positive')
    check('both orientations stopped honestly',all(x['status']=='inconclusive_unpaid_variance' and
          not x['krawczyk_evaluated'] and not x['range_exclusion_evaluated']
          for x in saved['orientations'].values()))
    prior=json.loads((HERE/'two-site-actual-collar-1925.json').read_bytes())
    def overlap(a,b):
        a,b=p.interval(a),p.interval(b)
        return max(a[0],b[0])<=min(a[1],b[1])
    for key in ('gamma','k'):
        check('actual consistency '+key,overlap(saved['actual'][key],prior['actual'][key]))
    for j in range(4):
        for key in ('value','da','db'):
            check('point coefficient consistency '+str(j)+'/'+key,
                  overlap(saved['point']['coefficients'][j][key],prior['point']['coefficients'][j][key]))
    report={'status':'passed' if not failures else 'failed','checks':checks,
            'trace_nodes':len(values),'divisor_count':len(divisors),
            'base_orthogonality_and_norms':'checked as complete cleared rational polynomials',
            'gram_identity':'checked in eight independent formal entries',
            'update_divisor':p.enc(d),'failed_variance':p.enc(variance),
            'required':'all positive numerical divisors before any normalized collar test',
            'failures':failures,
            'input_sha256':{str(path.relative_to(ROOT)):sha256(path.read_bytes()).hexdigest()
                            for path in (CERT,Path(__file__),HERE/'two-site-theta-jacobian-check-1921.py')},
            'qualification':'Finite arithmetic and algebra replay; not a separate proof audit or Decimal verification'}
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','checks','trace_nodes','divisor_count','failures','required')} |
                     {'certificate':str(OUT.relative_to(ROOT))}))
    assert not failures


if __name__=='__main__':
    main()
