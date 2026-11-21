"""Complete arithmetic replay and independent symbolic/centering checks.

No import of the producer. Laplace expansion uses full five-variable
moments before site specialization, rather than the producer's dual
three-variable permutation expansion. A second centered-quartic formula
checks the empirical observables and determinant. No new source moments.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / 'scripts/heat/two-site-theta-jacobian-1921.json'
OUT = Path(__file__).with_suffix('.json')
GRID = 10**50


def interval(record):
    a,b = F(record['lower']),F(record['upper'])
    assert a <= b
    return a,b


def enc(x):
    return dict(zip(('lower','upper'),map(str,x)))


def rounded(x):
    return F((x[0]*GRID).__floor__(),GRID),F((x[1]*GRID).__ceil__(),GRID)


def add(x,y):
    return rounded((x[0]+y[0],x[1]+y[1]))


def neg(x):
    return -x[1],-x[0]


def mul(x,y):
    terms = [a*b for a in x for b in y]
    return rounded((min(terms),max(terms)))


def reciprocal(x):
    assert not x[0] <= 0 <= x[1]
    return rounded((1/x[1],1/x[0]))


def scale(x,c):
    return mul(x,(F(c),F(c)))


def power(x,n):
    result = F(1),F(1)
    for _ in range(n):
        result = mul(result,x)
    return result


# Independent polynomial representation: dict of five-variable monomials.
def constant(c):
    return {(0,0,0,0,0):F(c)} if c else {}


def padd(x,y):
    z = x.copy()
    for e,c in y.items():
        z[e] = z.get(e,F(0))+c
    return {e:c for e,c in z.items() if c}


def pmul(x,y):
    z = {}
    for e,c in x.items():
        for f,d in y.items():
            g = tuple(a+b for a,b in zip(e,f))
            z[g] = z.get(g,F(0))+c*d
    return {e:c for e,c in z.items() if c}


def pneg(x):
    return {e:-c for e,c in x.items()}


def det(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    result = {}
    for j in range(len(matrix)):
        minor = [row[:j]+row[j+1:] for row in matrix[1:]]
        term = pmul(matrix[0][j],det(minor))
        result = padd(result,pneg(term) if j%2 else term)
    return result


def specialize(poly,derivative):
    result = {}
    for exponents,c in poly.items():
        e = list(exponents)
        if derivative is not None:
            c *= e[derivative]
            if not c:
                continue
            e[derivative] -= 1
        if e[3]:  # at a=0; b=1 contributes1 at every power
            continue
        key = tuple(e[:3])
        result[key] = result.get(key,F(0))+c
    return {e:c for e,c in result.items() if c}


def main():
    saved = json.loads(CERT.read_bytes())
    failures = []

    def check(name,condition):
        if not condition:
            failures.append(name)

    hashes = {name:sha256((ROOT/name).read_bytes()).hexdigest()==expected
              for name,expected in saved['input_sha256'].items()}
    check('all producer inputs unchanged',all(hashes.values()))
    source = json.loads((ROOT/saved['source']).read_bytes())
    check('complete selected input records', saved['selected_inputs']=={
        'lambda':source['panels'][0]['lambda'],
        'moments':{str(k):source['panels'][0]['moments'][str(k)] for k in (0,2,4,6)}})
    check('fixed degree and sites', saved['degree']==4 and saved['fixed_sites']==['0','1'])
    check('fixed rational grid', saved['arithmetic']['grid_denominator']==str(GRID))
    check('all inherited audit input hashes passed',all(saved['prior_hash_checks'].values()))
    values,divisors = [],[]
    for n,row in enumerate(saved['trace']):
        check('trace sequential id '+str(n),row['id']==n)
        kind,ids = row['operation'],row['inputs']
        if kind=='input':
            check('selected input path '+str(n),ids[0] in [
                '/panels/0/moments/'+str(k) for k in (0,2,4,6)])
            result = interval(source['panels'][0]['moments'][ids[0].split('/')[-1]])
        elif kind=='constant':
            result = interval(row['interval'])
            check('point constant '+str(n),result[0]==result[1] and not ids)
        else:
            check('backward operands '+str(n),all(isinstance(i,int) and 0<=i<n for i in ids))
            x = values[ids[0]]
            if kind=='add':
                result = add(x,values[ids[1]])
            elif kind=='negate':
                result = neg(x)
            elif kind=='multiply':
                result = mul(x,values[ids[1]])
            elif kind=='reciprocal':
                result = reciprocal(x)
                divisors.append({'trace_id':ids[0],'interval':enc(x),'excludes_zero':True})
            elif kind=='sqrt':
                actual = interval(row['interval'])
                check('complete square root inequalities '+str(n),
                      actual[0]>=0 and actual[0]**2<=x[0]<=x[1]<=actual[1]**2)
                lower = isqrt((x[0]*GRID*GRID).__floor__())
                upper = isqrt((x[1]*GRID*GRID).__floor__())
                if F(upper*upper,GRID*GRID)<x[1]:
                    upper+=1
                result = F(lower,GRID),F(upper,GRID)
            else:
                raise ValueError(kind)
        check('all trace endpoints '+str(n),result==interval(row['interval']))
        values.append(result)
    check('complete divisor list',divisors==saved['divisors'])

    def result_copies(obj):
        if isinstance(obj,dict):
            if 'trace_id' in obj:
                check('result copy '+str(obj['trace_id']),
                      values[obj['trace_id']]==interval(obj))
            else:
                for x in obj.values():
                    result_copies(x)
        elif isinstance(obj,list):
            for x in obj:
                result_copies(x)
    result_copies(saved['results'])

    # Reconstruct the whole moment polynomial before differentiating at sites.
    moments = []
    for k in range(8):
        base = constant(1) if k==0 else {}
        if k in (2,4,6):
            e = [0]*5
            e[k//2-1]=1
            base={tuple(e):F(1)}
        for site in (3,4):
            e=[0]*5
            e[site]=k
            base=padd(base,{tuple(e):F(1)})
        moments.append(base)
    gram = [[moments[i+j] for j in range(4)] for i in range(4)]
    expected = {'gram_det':det(gram)}
    for j in range(4):
        matrix = [row.copy() for row in gram]
        for i in range(4):
            matrix[i][j]=pneg(moments[i+4])
        expected['numerator_c'+str(j)]=det(matrix)
    polynomial_checks = []
    for name,poly in expected.items():
        for key,derivative in [('value',None),('da',3),('db',4)]:
            actual = {tuple(r['exponents']):F(r['coefficient'])
                      for r in saved['polynomials'][name][key]}
            equal = specialize(poly,derivative)==actual
            check('independent symbolic polynomial '+name+'/'+key,equal)
            polynomial_checks.append({'name':name+'/'+key,'all_coefficients_equal':equal,
                                      'terms':len(actual)})

    # Independent centered quartic coefficient identities, including derivatives.
    co = saved['results']['coefficients_ascending']
    c0,c1,c2,c3 = [interval(x['value']) for x in co]
    V = add(scale(power(c3,2),F(3,16)),scale(c2,F(-1,2)))
    T = add(add(scale(c1,F(-3,4)),scale(mul(c2,c3),F(3,8))),
            scale(power(c3,3),F(-3,32)))
    Q = add(add(add(scale(power(c2,2),F(1,2)),
                       scale(mul(c2,power(c3,2)),F(-7,16))),
                   scale(power(c3,4),F(21,256))),
               add(scale(mul(c1,c3),F(1,4)),neg(c0)))
    independent = {'variance':{'value':enc(V)},'third_centered':{'value':enc(T)},
                   'fourth_centered':{'value':enc(Q)}}
    As,Bs=[],[]
    for direction in ('da','db'):
        d0,d1,d2,d3 = [interval(x[direction]) for x in co]
        dV = add(scale(mul(c3,d3),F(3,8)),scale(d2,F(-1,2)))
        dT = add(add(scale(d1,F(-3,4)),scale(add(mul(d2,c3),mul(c2,d3)),F(3,8))),
                 scale(mul(power(c3,2),d3),F(-9,32)))
        dQ = add(add(add(mul(c2,d2),scale(add(mul(d2,power(c3,2)),
                          scale(mul(mul(c2,c3),d3),2)),F(-7,16))),
                     scale(mul(power(c3,3),d3),F(21,64))),
                 add(scale(add(mul(d1,c3),mul(c1,d3)),F(1,4)),neg(d0)))
        for label,val in [('variance',dV),('third_centered',dT),('fourth_centered',dQ)]:
            independent[label][direction]=enc(val)
        As.append(add(mul(V,dT),scale(mul(T,dV),F(-3,2))))
        Bs.append(add(mul(V,dQ),scale(mul(Q,dV),-2)))
    for label,record in independent.items():
        for key,x in record.items():
            a,b=interval(x),interval(saved['results'][label][key])
            check('centered formula overlap '+label+'/'+key,max(a[0],b[0])<=min(a[1],b[1]))
    numerator=add(mul(As[0],Bs[1]),neg(mul(As[1],Bs[0])))
    check('independent numerator strictly negative',numerator[1]<0)
    check('primary Gram determinant strictly positive',interval(saved['results']['gram_determinant']['value'])[0]>0)
    check('primary variance strictly positive',interval(saved['results']['variance']['value'])[0]>0)
    check('primary determinant strictly negative',interval(saved['results']['determinant'])[1]<0)
    check('empty producer failures',saved['failures']==[])
    check('producer rank conclusion',saved['rank_certified_subject_to_input_contracts'] is True)
    report={'status':'passed' if not failures else 'failed',
            'qualification':'Complete finite arithmetic/symbolic checks; L917/L037 analytic input and Decimal correctness remain assumed',
            'input_sha256':{str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in (CERT,Path(__file__))},
            'producer_input_hashes':hashes,'trace_records_checked':len(values),
            'divisors_checked':len(divisors),'polynomial_checks':polynomial_checks,
            'independent_centered_formula':independent,
            'independent_rank_numerator':enc(numerator),
            'primary_determinant':saved['results']['determinant'],
            'required':'all arithmetic and symbolic checks pass; determinant upper<0',
            'failures':failures}
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'trace_records_checked':len(values),
                      'symbolic_components_checked':len(polynomial_checks),
                      'divisors_checked':len(divisors),'independent_numerator_upper_negative':numerator[1]<0,
                      'required':report['required'],'failures':failures,
                      'certificate':str(OUT.relative_to(ROOT))}))
    assert not failures


if __name__=='__main__':
    main()
