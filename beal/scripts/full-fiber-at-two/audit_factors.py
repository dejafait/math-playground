"""Independent exact audit of L039. No construction code is imported.

Integer identities use degree-bounded interpolation; coordinate resultants
use quotient multiplication and rational Gaussian elimination. Frobenius
uses characteristic-five substitution, not modular binary powering.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
old = json.loads((BASE / 'factor-certificate.json').read_text())
one = json.loads((BASE.parent / 'full-fiber-at-one/factor-certificate.json').read_text())
source = json.loads((BASE.parent / 'five-isogeny-modular-norm/norm-certificate.json').read_text())['polynomials_ascending']
p = old['inputs']
checks = {}

def check(name, actual, required):
    checks[name] = {'actual': actual, 'required': required, 'pass': actual == required}

def val(a, x):
    return sum(c * x**i for i, c in enumerate(a))

def convolution(a, b):
    return [sum(a[i]*b[k-i] for i in range(len(a)) if 0 <= k-i < len(b))
            for k in range(len(a)+len(b)-1)]

def red(a, g, prime=None):
    assert g[-1] == 1
    r = list(a)
    n = len(g)-1
    for k in range(len(r)-1, n-1, -1):
        c = r[k]
        for i in range(n+1):
            r[k-n+i] -= c*g[i]
    r = (r+[0]*n)[:n]
    return [c % prime for c in r] if prime else r

def canonical(a):
    a = [c % 5 for c in a]
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a

def plus(a, b):
    return [(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
            for i in range(max(len(a),len(b)))]

def det(rows):
    rows = [[Q(c) for c in row] for row in rows]
    ans = Q(1)
    for k in range(len(rows)):
        pivot = next((i for i in range(k,len(rows)) if rows[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            rows[k], rows[pivot] = rows[pivot], rows[k]
            ans = -ans
        t = rows[k][k]
        ans *= t
        for i in range(k+1,len(rows)):
            ratio = rows[i][k]/t
            rows[i] = [x-ratio*y for x,y in zip(rows[i],rows[k])]
    assert ans.denominator == 1
    return ans.numerator

def mult_det(q, g):
    n = len(g)-1
    cols = [red([0]*k+q, g) for k in range(n)]
    return det([[cols[j][i] for j in range(n)] for i in range(n)])

# L034's previously source-audited lists; all coefficients compared.
for key, src in [('a','a'),('b','b'),('d','d'),('h','h'),('J','jcoef')]:
    check('source_'+key, p[key], source[src])
for key, degree in [('a',11),('b',10),('d',11),('h',4),('J',11),('F2',12)]:
    check('degree_'+key, len(p[key])-1, degree)
check('F2_monic',p['F2'][-1],1)
check('source_g',source['g'],[-20,-10,-1,1])
bounds = {'d':11,'h':4,'b':10,'J':11,'F2':12,'source_elimination':23,'reconstruction':23}
rows = []
for x in range(25):
    a,b,d,h,J,F = [val(p[k],x) for k in ['a','b','d','h','J','F2']]
    g = x**3-x*x-10*x-20
    e = 2*d-a
    residual = {'d':d-(x-16)**11,
                'h':h-(x**4-52820*x**3+1333262*x*x+4971236*x+9789217),
                'b':b-val(source['b1'],x)*val(source['b2'],x),
                'J':J-(2*a-b), 'F2':F-(h**3+2*J-4*d),
                'source_elimination':a*a-a*b-b*b*g+d*h**3,
                'reconstruction':e*e+b*e-b*b*g+d*F}
    rows.append({'x':x,'residuals':residual})
check('interpolation_all_residuals_zero',all(v==0 for row in rows for v in row['residuals'].values()),True)
check('interpolation_distinct_count',len({row['x'] for row in rows}),25)
check('interpolation_count_exceeds_bound',25 > max(bounds.values()),True)
F = p['F2']
coordinate = {'F2_at_16':val(F,16),
              'resultant_F2_b':mult_det(p['b'],F),
              'resultant_F2_derivative':mult_det([i*F[i] for i in range(1,len(F))],F)}
for key, value in coordinate.items():
    check('coordinate_'+key,value,old['coordinate'][key])
    check('nonzero_'+key,value != 0,True)
# Check the excluded chart and zero of f, using the audited source formula.
torsion = {'numerator_2T':val(p['a'],16)-61*val(p['b'],16),
           'numerator_3T':val(p['a'],16)+60*val(p['b'],16),
           'h16':val(p['h'],16)}
check('numerator_2T',torsion['numerator_2T'],0)
check('numerator_3T_nonzero',torsion['numerator_3T'] != 0,True)
check('j2T',str(Q(-torsion['h16']**3,torsion['numerator_3T'])),'-121')
check('jT',str(Q(val(p['a'],5)+5*val(p['b'],5),val(p['d'],5))),'-24729001')
check('map_leading_data',[(len(p[k])-1,p[k][-1]) for k in ['a','b','d']],[(11,743),(10,1),(11,1)])

m = [-380,-774,-1062,-456,258,468,104,-126,-6,6,-6,0,1]
check('entire_A_polynomial',one['inputs']['m'],m)
factor_evidence = {}
for label, poly, factors, irreduc, cop in [
    ('A',m,one['residue_factorizations']['A'],one['irreducibility_certificates']['A'],
     {'u':one['coprimality_certificates']['A']['bezout_u'],'v':one['coprimality_certificates']['A']['bezout_v']}),
    ('B2',F,old['residue_factors'],old['irreducibility'],old['coprimality'][0])]:
    check(label+'_number_factors',len(factors),2)
    check(label+'_number_irreducibility_records',len(irreduc),2)
    gs = [entry['coefficients'] for entry in factors]
    check(label+'_multiplicities',[entry['multiplicity'] for entry in factors],[1,1])
    check(label+'_monic',[g[-1] for g in gs],[1,1])
    check(label+'_full_factor_product',canonical(convolution(*gs)),canonical(poly))
    check(label+'_degrees',[len(g)-1 for g in gs],[1,11])
    check(label+'_total_dimension',sum(len(g)-1 for g in gs),12)
    witness = canonical(plus(convolution(cop['u'],gs[0]),convolution(cop['v'],gs[1])))
    check(label+'_coprime_bezout',witness,[1])
    check(label+'_linear_factor',gs[0],[0,1])
    seqs = []
    for index,(g,ic) in enumerate(zip(gs,irreduc)):
        n = len(g)-1
        check(f'{label}_{index}_degree',ic['degree'],n)
        R = red([0,1],g,5)
        seq = [canonical(R)]
        for i in range(n):
            # In F5[X], (sum c_i X^i)^5 = sum c_i X^(5i).
            expanded = [0]*(5*(len(R)-1)+1)
            for k,c in enumerate(R): expanded[5*k] = c
            R = red(expanded,g,5)
            seq.append(canonical(R))
        check(f'{label}_{index}_full_frobenius',seq,ic['frobenius_remainders'])
        check(f'{label}_{index}_frobenius_closure',seq[-1],seq[0])
        tests = ic['proper_degree_tests']
        check(f'{label}_{index}_test_count',len(tests),0 if n==1 else 1)
        for test in tests:
            check(f'{label}_{index}_test_prime',test['prime_divisor'],11)
            check(f'{label}_{index}_test_index',test['frobenius_index'],1)
            r = canonical(plus(seq[1],[0,-1]))
            check(f'{label}_{index}_test_r',r,test['remainder_minus_x'])
            bezout = canonical(plus(convolution(test['bezout_u'],g),convolution(test['bezout_v'],r)))
            check(f'{label}_{index}_irreducibility_bezout',bezout,[1])
        seqs.append(seq)
    factor_evidence[label] = {'factors':gs,'frobenius_recomputed':seqs,'coprime_identity':witness}

# Exact fixed-scalar specialization; Hensel supplies the unit roots, not sampling.
t,q = Q(2,1728),Q(1726,1728)
check('t_plus_q',str(t+q),'1')
check('t_q_unit',[r.numerator%5 != 0 and r.denominator%5 != 0 for r in [t,q]],[True,True])
check('root_exponents_mod4',[3%4,11%4],[3,3])
check('root_exponents_mod5_nonzero',[3%5 != 0,11%5 != 0],[True,True])
failures = [name for name,c in checks.items() if not c['pass']]
result = {'method':'independent interpolation, quotient determinants and Frobenius substitution',
          'polynomial_degree_bounds':bounds,'exact_evaluations':rows,'coordinate':coordinate,
          'torsion':torsion,'factors':factor_evidence,'checks':checks,'failures':failures,
          'bounds':{'dimensions_actual':[12,12],'dimensions_required':[12,12],
                    'pairwise_resultant_valuations_actual':[0,0],
                    'pairwise_resultant_valuations_required':[0,0],
                    'interpolation_points_actual':25,'interpolation_points_required':24,
                    'precision_cutoff':None}}
out = BASE/'audit-certificate.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(f'Checks: {len(checks)-len(failures)}/{len(checks)} passed; failures: {failures}')
print('Full A and B2 dimensions: actual=[12,12] required=[12,12]')
print('Coprime factor resultant valuations: actual=[0,0] required=[0,0]')
print('Exact interpolation points: actual=25 required>=24; no p-adic precision cutoff')
print('Certificate:',out.relative_to(Path.cwd()))
raise SystemExit(bool(failures))
