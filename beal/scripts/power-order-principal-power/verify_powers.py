"""Independent whole-certificate check; does not import generation code."""
from fractions import Fraction as Q
from pathlib import Path
import json

N = 12
EXPECTED_M = [-380,-774,-1062,-456,258,468,104,-126,-6,6,-6,0,1]
EXPECTED_H = [1,2,3,4,6,7,8,9,11,12]
ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).with_name('power-test-certificate.json')
OUT = Path(__file__).with_name('power-test-verification.json')
CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def decode(value):
    if isinstance(value, dict) and set(value) == {'numerator','denominator'}:
        require(value['denominator'] > 0, 'positive denominator')
        return Q(value['numerator'],value['denominator'])
    if isinstance(value, dict):
        return {k: decode(v) for k,v in value.items()}
    if isinstance(value, list):
        return [decode(v) for v in value]
    return value


def columns(a):
    return [list(v) for v in zip(*a)]


def matmul(a,b):
    require(len(a[0]) == len(b), 'matrix dimensions')
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def integer_matrix(a, rows, cols):
    require(len(a)==rows and all(len(r)==cols for r in a), 'matrix shape')
    require(all(type(x) is int for r in a for x in r), 'integer matrix')


def determinant(a):
    # Independent rational Gaussian elimination, not generator's Bareiss.
    b = [[Q(x) for x in r] for r in a]
    d = Q(1)
    for j in range(len(b)):
        pivots = [i for i in range(j,len(b)) if b[i][j]]
        if not pivots:
            return Q(0)
        p = pivots[0]
        if p != j:
            b[p],b[j] = b[j],b[p]
            d = -d
        d *= b[j][j]
        for i in range(j+1,len(b)):
            v = b[i][j]/b[j][j]
            for k in range(j,len(b)):
                b[i][k] -= v*b[j][k]
    return d


def multiply(a,b):
    # Independently form convolution then reduce by the entire polynomial.
    c = [0]*23
    for i in range(N):
        for j in range(N):
            c[i+j] += a[i]*b[j]
    for degree in range(22,11,-1):
        leading = c[degree]
        for j in range(13):
            c[degree-12+j] -= leading*EXPECTED_M[j]
        require(c[degree] == 0, 'monic reduction')
    return c[:N]


IDENTITY = [[int(i==j) for j in range(N)] for i in range(N)]
K = [0,1]+[0]*10
T = columns([multiply(K,c) for c in columns(IDENTITY)])


def gram(rows):
    star, squared, mu = [], [], [[Q(0)]*N for _ in range(N)]
    for i in range(N):
        w = [Q(x) for x in rows[i]]
        for j in range(i):
            mu[i][j] = sum(Q(rows[i][t])*star[j][t] for t in range(N))/squared[j]
            w = [w[t]-mu[i][j]*star[j][t] for t in range(N)]
        star.append(w)
        squared.append(sum(x*x for x in w))
        require(squared[-1]>0,'independent LLL rows')
    return mu,squared


def main():
    report = {'status':'IN_PROGRESS','source':str(SOURCE.relative_to(ROOT)),
              'failures':[], 'checks_passed':0,'actual_candidates':0,
              'required_candidates':1440,'actual_powers':0,'required_powers':12,
              'required_rank':12,'per_exponent':[],
              'principal_power_equalities':0,'L058_identity':'NOT_RUN',
              'class_value':'UNRESOLVED'}
    try:
        raw = json.loads(SOURCE.read_text())
        data = decode(raw)
        require(data['polynomial_ascending']==EXPECTED_M,'polynomial')
        require(data['exponents']==EXPECTED_H,'approved exponents')
        require(data['status']=='BOUNDED_LIST_EXHAUSTED','complete bounded search')
        require(data['failures']==[],'generation failures')
        require(data['successes']==[],'no reported success')
        require(data['maximum_candidates']==1440,'candidate bound')
        require(len(data['powers'])==12,'all consecutive powers')
        jb = None
        previous = None
        bases = {}
        for h, c in enumerate(data['powers'],1):
            g,b = c['generators'],c['basis']
            integer_matrix(g,N,24 if h==1 else 144)
            integer_matrix(b,N,N)
            q = len(g[0])
            integer_matrix(c['basis_in_generators'],q,N)
            integer_matrix(c['generators_in_basis'],N,q)
            integer_matrix(c['k_action'],N,N)
            if h==1:
                expected = [[11*IDENTITY[i][j] for j in range(N)] +
                            [T[i][j]-8*IDENTITY[i][j] for j in range(N)]
                            for i in range(N)]
                jb = b
            else:
                expected = columns([multiply(x,y) for x in columns(previous)
                                    for y in columns(jb)])
            require(g==expected,'complete ideal-product generators')
            require(matmul(g,c['basis_in_generators'])==b,'basis inclusion')
            require(matmul(b,c['generators_in_basis'])==g,'generator inclusion')
            require(matmul(T,b)==matmul(b,c['k_action']),'k stability')
            d = determinant(b)
            require(d == c['determinant'] and abs(d)==11**h,'power full rank and index')
            require(c['rank']==12 and c['required_rank']==12,'rank report')
            bases[h] = b
            previous = b
            report['actual_powers'] += 1
        require([c['h'] for c in data['tests']]==EXPECTED_H,'test exponents')
        for test in data['tests']:
            h,r = test['h'],test['reduction']
            original,rows = r['original_rows'],r['reduced_rows']
            integer_matrix(rows,N,N)
            integer_matrix(r['transformation'],N,N)
            integer_matrix(r['inverse_transformation'],N,N)
            require(original==columns(bases[h]),'LLL input basis')
            require(matmul(r['transformation'],original)==rows,'LLL transformation')
            require(matmul(r['inverse_transformation'],rows)==original,'LLL inverse')
            du = determinant(r['transformation'])
            require(abs(du)==1 and du==r['transformation_determinant'],'unimodularity')
            mu,squared = gram(rows)
            require(mu==r['gram_schmidt_mu'] and squared==r['gram_schmidt_squared_norms'],
                    'complete exact Gram-Schmidt data')
            require(r['delta']==Q(3,4),'LLL parameter')
            require(all(abs(mu[i][j])<=Q(1,2) for i in range(N) for j in range(i)),
                    'LLL size conditions')
            require(all(squared[i]>=(Q(3,4)-mu[i][i-1]**2)*squared[i-1]
                        for i in range(1,N)), 'LLL Lovasz conditions')
            candidates = [(f'b{i+1}', rows[i]) for i in range(N)]
            for i in range(N):
                for j in range(i+1,N):
                    candidates.append((f'b{i+1}+b{j+1}',[rows[i][t]+rows[j][t] for t in range(N)]))
                    candidates.append((f'b{i+1}-b{j+1}',[rows[i][t]-rows[j][t] for t in range(N)]))
            require(len(test['candidates'])==len(candidates)==144,'complete candidate list')
            indices = []
            for record,(name,beta) in zip(test['candidates'],candidates):
                require(record['name']==name and record['beta']==beta,'exact candidate')
                require(any(beta),'nonzero candidate')
                mb = columns([multiply(beta,e) for e in columns(IDENTITY)])
                inclusion = record['principal_in_power']
                integer_matrix(inclusion,N,N)
                require(matmul(bases[h],inclusion)==mb,'entire principal lattice inclusion')
                index = abs(determinant(inclusion))
                require(index.denominator==1 and index>1,'certified proper sublattice')
                require(index==record['index_of_principal_in_power'],'exact sublattice index')
                require(record['whole_lattice_equal'] is False,'equality rejection')
                indices.append(int(index))
                report['actual_candidates'] += 1
            report['per_exponent'].append({'h':h,'actual_rank':12,'required_rank':12,
                'candidates':144,'minimum_principal_sublattice_index':min(indices),
                'maximum_principal_sublattice_index':max(indices),
                'required_index_for_equality':1,'equalities':0})
        require(report['actual_candidates']==data['actual_candidates']==1440,'total candidates')
        require(data['candidate_rejections']==1440,'all rejections')
        report['status']='PASS'
    except Exception as exc:
        report['status']='FAIL'
        report['failures'].append(repr(exc))
    report['checks_passed']=CHECKS
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print(f'{report["status"]}: {CHECKS} checks; powers {report["actual_powers"]}/12; '
          f'candidates {report["actual_candidates"]}/1440; rank 12/12; equalities 0')
    for p in report['per_exponent']:
        print(f'h={p["h"]}: minimum index {p["minimum_principal_sublattice_index"]}; '
              'required for equality 1')
    print('Failures:',report['failures'])
    print('Full verification:',OUT.relative_to(ROOT))
    if report['failures']:
        raise SystemExit(1)


if __name__=='__main__':
    main()
