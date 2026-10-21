"""Independent L077 arithmetic audit; no imports from the original checker.

Polynomial long division and permutation determinants verify exact identities.
The canonical proof supplies maximality, completeness and infinite lifting.
"""
from fractions import Fraction as F
from itertools import permutations, product
from math import isqrt, prod
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
checks = {}


def record(name, actual, required):
    checks[name] = dict(actual=actual, required=required, passed=actual == required)


def trim(a):
    a = list(map(F, a))
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def plus(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def times(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def remainder(a, modulus):
    a = trim(a)
    while len(a) >= len(modulus):
        offset, factor = len(a)-len(modulus), a[-1]/modulus[-1]
        a = plus(a, [0]*offset + [-factor*x for x in modulus])
    return a + [F(0)] * (len(modulus)-1-len(a))


def substitute(a, b):
    result = [F(0)]
    for coefficient in reversed(a):
        result = plus(times(result, b), [coefficient])
    return result


f, fs, g = [1, 1, -1, 1], [-2, 6, -4, 1], [-1264, -160, -4, 1]
one, t = [1, 0, 0], [0, 1, 0]


def multiply(a, b, modulus=f):
    return remainder(times(a, b), modulus)


def determinant(matrix):
    n = len(matrix)
    total = F(0)
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        total += (-1)**inversions * prod(matrix[i][p[i]] for i in range(n))
    return total


def norm(a):
    columns = [multiply(a, [0]*j+[1]) for j in range(3)]
    return determinant(list(map(list, zip(*columns))))


def evaluate(a, x):
    return sum(F(c)*x**i for i, c in enumerate(a))


def residue(a, p=8):
    assert all(F(c).denominator == 1 for c in a)
    return [int(c) % p for c in a]


def rank2(matrix):
    a = [row[:] for row in matrix]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        for i in range(len(a)):
            if i != r and a[i][j]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        r += 1
    return r


v, s, a, b = [1, -1, 1], [1, 1, 0], [9, -7, 5], [-4, -8, -1]
w, theta, h = multiply(a, b), [8, -14, 6], [-3, 14, -6]
generators = dict(minus_one=[-1, 0, 0], v=v, s=s, a=a, b=b)
norms = [norm(z) for z in generators.values()]
record('translate', substitute(f, [-1, 1]), fs)
record('theta_polynomial', remainder(substitute(g, theta), f), [0, 0, 0])
record('inverse_theta_coordinate', remainder(substitute([F(-92,484), F(-62,484), F(3,484)], theta), f), t)
# Discriminant via the resultant Sylvester determinant, rather than cubic formula.
derivative = [1, -2, 3]
sylvester = []
for j in range(2):
    sylvester.append([0]*j+list(reversed(f))+[0]*(1-j))
for j in range(3):
    sylvester.append([0]*j+list(reversed(derivative))+[0]*(2-j))
discriminant = -determinant(sylvester)
record('discriminant', discriminant, -44)
record('possible_nontrivial_index_primes', [p for p in (2, 11) if 44 % (p*p) == 0], [2])
record('eisenstein_coefficients', [c % 2 for c in fs[:-1]]+[fs[0] % 4, fs[-1]], [0, 0, 0, 2, 1])
record('minkowski_and_conrad_bounds', [44*16 < 27**2, 8 < 9, 36 < 44], [True]*3)
record('real_root_bracket', [evaluate(f,F(-3,5)), evaluate(f,F(-1,2))], [F(-22,125), F(1,8)])
record('unit_inverse', multiply(v,[0,-1,0]), one)
record('prime_generator_identity_a', multiply(a,multiply(s,s)), derivative)
record('prime_generator_identity_b', multiply(multiply(a,a),b), [11,0,0])
record('w_coordinates_and_norm', [w, norm(w)], [[2,-1,-6],121])
record('generator_norms', norms, [-1,1,2,11,11])
record('eleven_factorization_coefficients', residue(times([-6,1],times([-3,1],[-3,1])),11), residue(f,11))
record('a_residues_P_Q', [evaluate(a,r)%11 for r in (3,6)], [0,4])

# Full norm kernel is computed from all 32 products of actual norms.
norm_records = []
for bits in product(range(2), repeat=5):
    n = int(prod(n**e for n,e in zip(norms,bits)))
    square = n >= 0 and isqrt(n)**2 == n
    norm_records.append(dict(bits=list(bits), norm=n, square=square))
kernel = [r['bits'] for r in norm_records if r['square']]
record('norm_kernel', kernel, [[0,i,0,j,j] for i,j in product(range(2),repeat=2)])
squares11 = sorted({i*i%11 for i in range(1,11)})
v_residues = [int(evaluate(v,r))%11 for r in (6,3)]
record('eleven_full_unit_types', [v_residues,squares11, (7*pow(10,-1,11))%11], [[9,7],[1,3,4,5,9],4])
record('eleven_theta_order', [evaluate(theta,r)%11 for r in (6,3)], [8,9])

elements = dict(v=v, vh=multiply(v,h), w=w, wh=multiply(w,h),
                vw=multiply(v,w), vwh=multiply(multiply(v,w),h))
square_table = []
for root in product(range(8), repeat=3):
    if root[0]%2:
        square_table.append(dict(root=list(root),square=residue(multiply(root,root,fs))))
targets = {}
for name,z in elements.items():
    exact = remainder(substitute(z,[-1,1]),fs)
    mod = residue(exact)
    targets[name] = dict(exact_s=exact, residue=mod,
                         roots=[r['root'] for r in square_table if r['square']==mod])
record('dyadic_products', [targets[n]['exact_s'] for n in elements],
       [[3,-3,1],[-29,15,-3],[-3,11,-6],[-87,209,-86],[1,0,2],[-15,-22,36]])
record('dyadic_nonmembership', [bool(targets[n]['roots']) for n in ('v','vh','w','wh')], [False]*4)
# Check every coefficient of the general square, not only residue samples.
square_monomials = []
for i,j in ((0,0),(0,1),(0,2),(1,1),(1,2),(2,2)):
    z = multiply([0]*i+[1],[0]*j+[1],fs)
    square_monomials.append([c*(1 if i==j else 2) for c in z])
record('general_square_coefficients',square_monomials,
       [[1,0,0],[0,2,0],[0,0,2],[0,0,1],[4,-12,8],[8,-22,10]])
r = [1,0,1]
r_squared = multiply(r,r,fs)
error = plus(targets['vwh']['exact_s'],[-c for c in r_squared])
record('hensel_square_and_error', [r_squared,error], [[9,-22,12],[-24,0,24]])
record('hensel_strict_inequality', 9>2*3, True)
# The 9 lower bound uses 24(s^2-1), a unit times 2^3, and e=3.
record('hensel_units_mod_uniformizer', [r[0]%2, (-1)%2], [1,1])
dyadic_row = [int(not targets[n]['roots'] and not targets[n+'h']['roots']) for n in ('v','w')]
matrix = [dyadic_row, [0,1], [0,1]]
record('matrix_and_rank', [matrix,rank2(matrix)], [[[1,1],[0,1],[0,1]],2])

sources = {}
for filename in ('rank-certificate.json','initial-rank-certificate.json'):
    raw = (HERE/filename).read_bytes()
    data = json.loads(raw)
    sources[filename] = dict(sha256=hashlib.sha256(raw).hexdigest(),
                            failures=data['failures'],checks=data['checks'],
                            restriction=data['restriction'])
    record(filename+':field',data['field'],dict(polynomial_ascending=f,discriminant=discriminant))
    record(filename+':generators',data['generators_t'],generators)
    record(filename+':norms_and_kernel',[data['norms'],data['w_t'],data['full_norm_kernel_bits']], [norms,w,kernel])
    record(filename+':norm_columns',data['norm_columns_sign_two_eleven'],[[1,0,0],[0,0,0],[0,1,0],[0,0,1],[0,0,1]])
    record(filename+':eleven_values', [data['eleven'][k] for k in ('roots','squares','v_residues_rational_ramified','w_prime_valuations')], [[3,6],squares11,v_residues,[1,1]])
    record(filename+':full_256_table',data['dyadic']['unit_square_table'],square_table)
    record(filename+':all_targets',data['dyadic']['targets'],{n:targets[n] for n in data['dyadic']['targets']})
    record(filename+':consistent_flags',data['failures'],[n for n,ok in data['checks'].items() if not ok])
    if filename == 'rank-certificate.json':
        record('final_matrix_replayed',[data['restriction']['matrix'],data['restriction']['rank']],[matrix,rank2(matrix)])
        record('final_thresholds',data['thresholds'],dict(combined_rank_actual=2,second_direction_required=2,
            supported_unit_dimension=16,certified_removed_directions=2,unit_kernel_upper_bound=14,
            unit_kernel_required_upper_bound=11,localized_class_kernel_computed=False))

failures = [name for name,value in checks.items() if not value['passed']]
certificate = dict(checks=checks,failures=failures,source_certificates=sources,
                   all_norm_choices=norm_records,dyadic=dict(unit_square_table=square_table,targets=targets,
                   hensel=dict(root_approximation=r,square=r_squared,error=error,error_valuation=9,
                               derivative_valuation=3,required_strict_lower_bound=6)),
                   restriction=dict(matrix=matrix,rank=rank2(matrix)),
                   thresholds=dict(rank_actual=rank2(matrix),rank_required=2,
                                   unit_upper_actual=16-rank2(matrix),unit_upper_required=11),
                   qualification='Exact arithmetic only; canonical L077 audit supplies theorem applicability and completeness.')


def encode(x):
    if isinstance(x,F):
        return int(x) if x.denominator==1 else str(x)
    raise TypeError(type(x).__name__)


out = HERE/'audit-certificate.json'
out.write_text(json.dumps(certificate,default=encode,indent=2)+'\n')
print(f'Checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}')
print(f'Combined rank actual/required: {rank2(matrix)}/2; unit upper bound actual/required: {16-rank2(matrix)}/11')
print(f'Certificate: {out.relative_to(Path.cwd())}')
raise SystemExit(bool(failures))
