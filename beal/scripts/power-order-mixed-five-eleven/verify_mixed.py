"""Independent whole-certificate check; does not import generation code."""
from fractions import Fraction as Q
from pathlib import Path
import json

N = 12
EXPECTED_M = [-380,-774,-1062,-456,258,468,104,-126,-6,6,-6,0,1]
PAIRS = [(h,t) for h in range(1,5) for t in range(1,5)]
ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).with_name('mixed-test-certificate.json')
OUT = Path(__file__).with_name('mixed-test-verification.json')
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
              'failures':[],'checks_passed':0,'actual_candidates':0,
              'required_candidates':2304,'actual_lattices':0,'required_lattices':24,
              'actual_products':0,'required_products':16,'required_rank':12,
              'per_pair':[],'mixed_equalities':0,'class_value':'UNRESOLVED'}
    try:
        data = decode(json.loads(SOURCE.read_text()))
        require(data['polynomial_ascending']==EXPECTED_M,'polynomial')
        require(data['pairs']==[list(p) for p in PAIRS],'approved pairs')
        require(data['status'] in ['BOUNDED_LIST_EXHAUSTED','MIXED_EQUALITY_FOUND'],'completed search')
        require(data['failures']==[],'generation failures')
        require(data['maximum_candidates']==2304 and data['maximum_candidates_per_pair']==144,'bounds')
        labels = ['J','Q']+[f'J^{h}' for h in range(2,5)]+[f'Q^{t}' for t in range(2,5)]
        labels += [f'J^{h} Q^{t}' for h,t in PAIRS]
        require([c['label'] for c in data['lattices']]==labels,'exact lattice scope/order')
        bases = {}
        for c in data['lattices']:
            label,g,b = c['label'],c['generators'],c['basis']
            if label=='J':
                expected = [[11*IDENTITY[i][j] for j in range(N)]+
                            [T[i][j]-8*IDENTITY[i][j] for j in range(N)] for i in range(N)]
            elif label=='Q':
                expected = [[5*IDENTITY[i][j] for j in range(N)]+T[i][:] for i in range(N)]
            else:
                if ' ' in label:
                    left,right = label.split()
                else:
                    symbol,exponent = label.split('^')
                    e = int(exponent)
                    left,right = (symbol if e==2 else f'{symbol}^{e-1}'),symbol
                if left.endswith('^1'): left=left[0]
                if right.endswith('^1'): right=right[0]
                expected = columns([multiply(x,y) for x in columns(bases[left])
                                    for y in columns(bases[right])])
            q = len(expected[0])
            integer_matrix(g,N,q)
            integer_matrix(b,N,N)
            integer_matrix(c['basis_in_generators'],q,N)
            integer_matrix(c['generators_in_basis'],N,q)
            integer_matrix(c['k_action'],N,N)
            require(g==expected,'every product generator')
            require(matmul(g,c['basis_in_generators'])==b,'basis in full generators')
            require(matmul(b,c['generators_in_basis'])==g,'full generators in basis')
            require(matmul(T,b)==matmul(b,c['k_action']),'k-stability')
            d = determinant(b)
            require(d!=0 and d==c['determinant'],'full rank/determinant')
            require(c['rank']==c['required_rank']==12,'rank fields')
            bases[label]=b
            report['actual_lattices']+=1
        require([(c['h'],c['t']) for c in data['tests']]==PAIRS,'complete tests')
        successes=[]
        for test in data['tests']:
            h,t,r = test['h'],test['t'],test['reduction']
            label = f'J^{h} Q^{t}'
            basis = bases[label]
            require(test['label']==label,'mixed label')
            require(test['actual_rank']==test['required_rank']==12,'test ranks')
            original,rows = r['original_rows'],r['reduced_rows']
            integer_matrix(rows,N,N)
            integer_matrix(r['transformation'],N,N)
            integer_matrix(r['inverse_transformation'],N,N)
            require(original==columns(basis),'LLL original')
            require(matmul(r['transformation'],original)==rows,'LLL forward')
            require(matmul(r['inverse_transformation'],rows)==original,'LLL reverse')
            require(matmul(r['transformation'],r['inverse_transformation'])==IDENTITY,'transform inverse')
            require(matmul(r['inverse_transformation'],r['transformation'])==IDENTITY,'inverse transform')
            du = determinant(r['transformation'])
            require(abs(du)==1 and du==r['transformation_determinant'],'unimodular transform')
            mu,squared = gram(rows)
            require(mu==r['gram_schmidt_mu'] and squared==r['gram_schmidt_squared_norms'],'whole GS data')
            require(r['delta']==Q(3,4),'delta')
            require(all(abs(mu[i][j])<=Q(1,2) for i in range(N) for j in range(i)),'size reduction')
            require(all(squared[i]>=(Q(3,4)-mu[i][i-1]**2)*squared[i-1]
                        for i in range(1,N)),'Lovasz')
            candidates = [(f'b{i+1}',rows[i]) for i in range(N)]
            for i in range(N):
                for j in range(i+1,N):
                    candidates.append((f'b{i+1}+b{j+1}',[rows[i][k]+rows[j][k] for k in range(N)]))
                    candidates.append((f'b{i+1}-b{j+1}',[rows[i][k]-rows[j][k] for k in range(N)]))
            require(len(test['candidates'])==len(candidates)==144,'all 144 candidates')
            indices=[]
            for record,(name,beta) in zip(test['candidates'],candidates):
                require(record['name']==name and record['beta']==beta,'candidate reconstruction')
                require(any(beta),'nonzero beta')
                mb = columns([multiply(beta,e) for e in columns(IDENTITY)])
                inclusion = record['principal_in_product']
                integer_matrix(inclusion,N,N)
                require(matmul(basis,inclusion)==mb,'entire principal inclusion')
                index = abs(determinant(inclusion))
                require(index.denominator==1 and index>0,'positive integer index')
                require(index==record['index_of_principal_in_product'],'exact index')
                eq = index==1
                require(record['whole_lattice_equal']==eq,'equality flag')
                if eq:
                    reverse = record['product_in_principal']
                    integer_matrix(reverse,N,N)
                    require(matmul(mb,reverse)==basis,'whole reverse inclusion')
                    successes.append({'h':h,'t':t,'beta':beta,'candidate':name})
                else:
                    require(index>1,'proved proper sublattice')
                indices.append(int(index))
                report['actual_candidates']+=1
            report['per_pair'].append({'h':h,'t':t,'actual_rank':12,'required_rank':12,
                'product_lattice_index_in_R':int(abs(determinant(basis))),
                'candidates':144,'minimum_principal_sublattice_index':min(indices),
                'maximum_principal_sublattice_index':max(indices),
                'required_index_for_equality':1,'equalities':sum(c['whole_lattice_equal'] for c in test['candidates'])})
            report['actual_products']+=1
        require(successes==data['successes'],'all reported successes')
        require(report['actual_candidates']==data['actual_candidates']==2304,'total candidates')
        require(data['candidate_rejections']==2304-len(successes),'all rejections')
        require(data['status']==('MIXED_EQUALITY_FOUND' if successes else 'BOUNDED_LIST_EXHAUSTED'),'status')
        report['mixed_equalities']=len(successes)
        report['class_value']='u=0 BY VERIFIED L059 IDENTITY' if successes else 'UNRESOLVED'
        report['status']='PASS'
    except Exception as exc:
        report['status']='FAIL'
        report['failures'].append(repr(exc))
    report['checks_passed']=CHECKS
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print(f'{report["status"]}: products {report["actual_products"]}/16; lattices {report["actual_lattices"]}/24; '
          f'candidates {report["actual_candidates"]}/2304; rank 12/12; equalities {report["mixed_equalities"]}')
    for p in report['per_pair']:
        print(f'(h,t)=({p["h"]},{p["t"]}): minimum principal index {p["minimum_principal_sublattice_index"]}; '
              'required 1')
    print('Failures:',report['failures'])
    print('Full verification:',OUT.relative_to(ROOT))
    if report['failures']: raise SystemExit(1)


if __name__=='__main__':
    main()
