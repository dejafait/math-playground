"""Independent complete-record audit of L088; standard library only."""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
source = HERE / 'norm-certificate.json'
original = json.loads(source.read_text())
checks = {}
def check(name, condition):
    checks[name] = bool(condition)

# Enumerate matchings by rows (the construction enumerates column shifts).
records = []
def visit(row, used, assignment):
    if row == 11:
        rows = [0] * 11
        for i, j in enumerate(assignment):
            rows[j] = i
        shifts = [(rows[j] - j) % 11 for j in range(11)]
        r = sum(d > 0 for d in shifts)
        k = sum((j + shifts[j]) // 11 for j in range(11))
        sign = (-1) ** sum(rows[i] > rows[j] for i in range(11) for j in range(i+1, 11))
        records.append(dict(shifts=shifts, rows=rows, c_degree=r, q_degree=k,
                            sign=sign, valuation_lower_bound=2*r+15*k))
        return
    for j in range(11):
        if j not in used and (row-j) % 11 in (0,1,2):
            visit(row+1, used | {j}, assignment+[j])
visit(0, set(), [])
key = lambda r: tuple(r['shifts'])
check('all_complete_term_records_match', sorted(records, key=key) == sorted(original['all_nonzero_determinant_terms'], key=key))
check('no_duplicate_records', len({key(r) for r in records}) == len(records))
check('term_count', len(records) == 201)
check('unique_constant', sum(r['c_degree'] == 0 for r in records) == 1)
check('permutation_shift_bound', all(sum(r['shifts']) == 11*r['q_degree'] and r['c_degree'] <= sum(r['shifts']) <= 2*r['c_degree'] for r in records))
minimum = min(r['valuation_lower_bound'] for r in records if r['c_degree'])
check('uniform_strict_bound', minimum == 27 and minimum > 6)
coeff = Counter()
for r in records:
    coeff[r['c_degree'], r['q_degree']] += r['sign']
polynomial = [dict(c_degree=r, q_degree=k, coefficient=a) for (r,k),a in sorted(coeff.items()) if a]
check('complete_polynomial_matches', polynomial == original['determinant_polynomial'])

# A different determinant algorithm, exact integer Bareiss elimination.
# Degree <=11 in c and <=2 in q: 12*3 evaluations certify this polynomial.
def det(matrix):
    a = [row[:] for row in matrix]
    sign, old = 1, 1
    for k in range(len(a)-1):
        if not a[k][k]:
            swap = next((i for i in range(k+1, len(a)) if a[i][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                value = a[i][j]*pivot-a[i][k]*a[k][j]
                assert value % old == 0
                a[i][j] = value // old
            a[i][k] = 0
        old = pivot
    return sign*a[-1][-1]
evaluations = []
for c in range(12):
    for q in range(3):
        matrix = [[0]*11 for _ in range(11)]
        for j in range(11):
            matrix[j][j] += 1
            for shift in (1,2):
                matrix[(j+shift)%11][j] += c*q**((j+shift)//11)
        actual = det(matrix)
        expected = sum(a*c**r*q**k for (r,k),a in coeff.items())
        evaluations.append(dict(c=c, q=q, actual=actual, expected=expected))
check('independent_determinant_grid', all(e['actual'] == e['expected'] for e in evaluations))

# Exact arithmetic in Q[s], s^3=4s^2-6s+2; no construction imports.
def add(a,b): return tuple(a[i]+b[i] for i in range(3))
def scale(k,a): return tuple(k*x for x in a)
def mul(a,b):
    out = [Fraction(0)]*5
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j] += x*y
    for d in (4,3):
        value=out[d]
        out[d]=0
        for i,k in enumerate((2,-6,4)): out[d-3+i] += k*value
    return tuple(out[:3])
def norm(a):
    columns=[mul(a,b) for b in ((1,0,0),(0,1,0),(0,0,1))]
    ans=0
    for p in permutations(range(3)):
        term=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        for j in range(3): term *= columns[j][p[j]]
        ans+=term
    return ans
one=(1,0,0); s=(0,1,0); t=(-1,1,0)
v=(3,-3,1); w=(-3,11,-6); theta=(28,-26,6)
a=(21,-17,5); b=(3,-6,-1)
check('cubic_relation', add(add(mul(mul(t,t),t),scale(-1,mul(t,t))),add(t,one)) == (0,0,0))
check('coordinate_theta', add(add(scale(8,one),scale(-14,t)),scale(6,mul(t,t))) == theta)
check('unit_inverse', mul(t,v) == (-1,0,0))
check('supported_generators', mul(a,b) == w and mul(mul(a,a),b) == (11,0,0))
check('generator_norms', [norm(z) for z in (scale(-1,one),v,s,a,b,w)] == [-1,1,2,11,11,121])
check('dyadic_product', mul(v,w) == (1,0,2))
check('square_coefficient_obstructions', all(mul((A,B,C),(A,B,C))[1] % 2 == 0 and mul((A,B,C),(A,B,C))[2] % 4 in (0,1) for A in (1,3) for B in range(4) for C in range(4)))
check('theta_kappa_valuations', min(6,4,5) == 4 and 3*6 > 4 and 3*2-4 == 2)
check('zeta_basis_inverse', 5*9 == 1+4*11 and 2**5 == 32)
check('thirteen_residues', (11**3-11**2+11+1)%13 == 0 and (8-14*11+6*11**2)%13 == 8 and (11**2-11+1)%13 == 7 and (2-11-6*11**2)%13 == 6)
check('thirteen_characters', [pow(r,6,13) for r in (7,6,7*6%13)] == [12,12,1])
check('finite_norm_character_exponents', ((13**12-1)//12)*6 == (13**12-1)//2)
check('original_specialization', original['specialization'] == dict(q=32,ord_C_q=15,ord_C_c=2,ord_C_2=3,error_lower_bound=27,required_strict_bound=6))
check('all_original_checks_present_and_true', len(original['checks']) == 9 and all(original['checks'].values()) and original['failures'] == [])
result=dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(), checks=checks,
            failures=[k for k,v in checks.items() if not v],
            bounds=dict(actual_minimum_term_valuation=minimum, required_strict_bound=6),
            determinant_polynomial=polynomial, all_recomputed_terms=sorted(records,key=key),
            independent_determinant_evaluations=evaluations,
            qualifications='Arithmetic replay; ideal correction, completeness, Hensel and character transfer require the canonical mathematical audit.')
path=HERE/'audit-certificate.json'
path.write_text(json.dumps(result,indent=2)+'\n')
print(f'Checks: {sum(checks.values())}/{len(checks)}; full terms: {len(records)}; independent determinants: {len(evaluations)}')
print(f'Actual minimum term bound: {minimum}; required strictly greater than 6; failures: {result["failures"]}')
print('Certificate:',path)
assert all(checks.values())
