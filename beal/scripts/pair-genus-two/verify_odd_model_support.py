"""Independent sparse-polynomial and Euclidean-resultant replay of L138.

Does not import the producer. Checks complete saved objects, not previews.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import comb, isqrt, prod
import hashlib
import json
import traceback

HERE = Path(__file__).resolve().parent
SOURCE = HERE/'odd-model-support-certificate.json'
OUTPUT = HERE/'odd-model-support-verification.json'
report = {'checks': [], 'failures': [], 'resultant_chains': {},
          'bounds': {'degree_cap': 12, 'matrix_size_cap': 12, 'rational_bits_cap': 4096,
                     'max_degree': 0, 'max_matrix_size': 0, 'max_rational_bits': 0,
                     'meaning': 'finite-domain/size bounds, not operation counts'}}


def record(name, value):
    report['checks'].append({'name': name, 'pass': bool(value)})
    if not value:
        report['failures'].append(name)
        raise AssertionError(name)


def observe(a):
    if isinstance(a, (Q, int)) and not isinstance(a, bool):
        q = Q(a)
        bits = max(abs(q.numerator).bit_length(), q.denominator.bit_length())
        report['bounds']['max_rational_bits'] = max(report['bounds']['max_rational_bits'], bits)
        assert bits <= 4096
    elif isinstance(a, (tuple, list)):
        for v in a:
            observe(v)
    elif isinstance(a, dict):
        for v in a.values():
            observe(v)


def sparse(values):
    return {i: Q(v) for i, v in enumerate(values) if Q(v)}


def tidy(a):
    a = {i: x for i, x in a.items() if x}
    observe(a)
    d = max(a, default=0)
    report['bounds']['max_degree'] = max(report['bounds']['max_degree'], d)
    assert d <= 12
    return a


def plus(a, b, coefficient=1):
    ans = dict(a)
    for i, x in b.items():
        ans[i] = ans.get(i, Q(0))+coefficient*x
    return tidy(ans)


def times(a, b):
    ans = {}
    for i, x in a.items():
        for j, y in b.items():
            ans[i+j] = ans.get(i+j, Q(0))+x*y
            observe(ans[i+j])
    return tidy(ans)


def remainder(a, b):
    a = dict(a)
    n = max(b)
    while a and max(a) >= n:
        m = max(a)
        q = a[m]/b[n]
        a = plus(a, {i+m-n: q*x for i, x in b.items()}, -1)
    return a


def compose(a, b, modulus):
    # Sum a_i b^i with separately built powers, rather than producer Horner.
    powers = [{0: Q(1)}]
    for _ in range(max(a, default=0)):
        powers.append(remainder(times(powers[-1], b), modulus))
    answer = {}
    for i, x in a.items():
        answer = plus(answer, powers[i], x)
    return remainder(answer, modulus)


def gcd(a, b):
    while b:
        a, b = b, remainder(a, b)
    lead = a[max(a)]
    return {i: x/lead for i, x in a.items()}


def derivative(a):
    return {i-1: i*x for i, x in a.items() if i}


def result(a, b, chain):
    m, n = max(a), max(b)
    if n == 0:
        value = b[0]**m
        chain.append({'a': dense(a), 'b': dense(b), 'terminal': value})
        return value
    r = remainder(a, b)
    if not r:
        chain.append({'a': dense(a), 'b': dense(b), 'zero_remainder': True})
        return Q(0)
    k = max(r)
    multiplier = (-1)**(m*n)*b[n]**(m-k)
    chain.append({'a': dense(a), 'b': dense(b), 'remainder': dense(r), 'multiplier': multiplier})
    v = multiplier*result(b, r, chain)
    observe(v)
    return v


def dense(a, length=None):
    return [a.get(i, Q(0)) for i in range(length or max(a, default=0)+1)]


def mat(v):
    return [[Q(x) for x in row] for row in v]


def mm(a, b):
    c = [[sum(a[i][k]*b[k][j] for k in range(len(b)))
          for j in range(len(b[0]))] for i in range(len(a))]
    observe(c)
    return c


def det(a):
    a = [row[:] for row in a]
    n, value = len(a), Q(1)
    report['bounds']['max_matrix_size'] = max(report['bounds']['max_matrix_size'], n)
    assert n <= 12
    for j in range(n):
        k = next((k for k in range(j, n) if a[k][j]), None)
        if k is None:
            return Q(0)
        if k != j:
            a[k], a[j] = a[j], a[k]
            value = -value
        pivot = a[j][j]
        value *= pivot
        for i in range(j+1, n):
            multiple = a[i][j]/pivot
            for k in range(j+1, n):
                a[i][k] -= multiple*a[j][k]
                observe(a[i][k])
            a[i][j] = Q(0)
    return value


def factor_replay(name, value, record_data):
    f = record_data['factors']
    record(name+'_all_factors_prime', all(type(p) is int and type(e) is int and p >= 2 and e >= 1
            and all(p % d for d in range(2, isqrt(p)+1)) for p, e in f))
    record(name+'_factor_product', prod(p**e for p, e in f) == abs(value))
    cofactor, divisions, facts = abs(int(value)), [], []
    for p in range(2, 12):
        if cofactor == 1:
            break
        trial = {'divisor': p, 'cofactor_before': cofactor, 'remainder': cofactor % p}
        record(name+'_trial_'+str(p), trial == record_data['trials'][p-2])
        e = 0
        while cofactor % p == 0:
            divisions.append([cofactor, p, cofactor//p])
            cofactor //= p
            e += 1
        if e:
            facts.append([p, e])
    record(name+'_all_divisions_and_end', divisions == record_data['divisions'] and
           facts == f and cofactor == record_data['cofactor'] == 1 and
           len(record_data['trials']) == p-1)


def encode(v):
    if isinstance(v, Q):
        return int(v) if v.denominator == 1 else str(v)
    if isinstance(v, dict):
        return {k: encode(x) for k, x in v.items()}
    if isinstance(v, list):
        return [encode(x) for x in v]
    return v


try:
    data = json.loads(SOURCE.read_text())
    report['input_sha256'] = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    record('producer_completed_without_failures', data['status'] == 'PASS' and not data['failures'] and
           all(x['pass'] is True for x in data['checks']))
    old = HERE/'rank-lower-certificate.json'
    saved = json.loads(old.read_text())['model']
    record('entire_original_model_binding', data['input']['saved_model'] == saved and
           data['input']['rank_model_sha256'] == hashlib.sha256(old.read_bytes()).hexdigest())
    # Audit the exact literal types before rational decoding; bool is not an int.
    for key in ['model', 'field', 'discriminants']:
        def valid_literal(x):
            if isinstance(x, list):
                return all(valid_literal(v) for v in x)
            if isinstance(x, dict):
                return all(valid_literal(v) for v in x.values())
            return type(x) in (int, str)
        record(key+'_exact_literal_types', valid_literal(data[key]))
    m, field = data['model'], data['field']
    f = sparse([-308, -2288, 341, 3388, 1034, -704, -275])
    q4 = sparse([7, 52, -6, -64, -25])
    c = Q(-36300)
    taylor = [sum(Q(comb(i,j))*f.get(i,0)*2**(i-j) for i in range(j,7)) for j in range(7)]
    new_G = [taylor[6-j]*c**(4-j) for j in range(5)]+[Q(1)]
    G, H = sparse(new_G), sparse(m['H'])
    r = Q(9075)
    record('full_input_polynomials', sparse(m['f']) == f and sparse(m['q4']) == q4 and Q(m['c']) == c)
    record('twist_11', f == {i: 11*x for i,x in times(sparse([-4,0,1]),q4).items()})
    record('full_Taylor_and_quintic', list(map(Q,m['taylor'])) == taylor == list(map(Q,saved['taylor_at_two'])) and
           list(map(Q,m['G'])) == new_G == list(map(Q,saved['g'])))
    substitution = sparse([c*c*x for x in new_G])
    record('homogeneous_entire_coefficient_identity', sparse(m['homogeneous_substitution']) == substitution and
           taylor[0] == 0 and taylor[1] == c)
    record('integral_monic_degree_five', max(G) == 5 and G[5] == 1 and all(x.denominator == 1 for x in G.values()))
    record('exact_gcds', gcd(f, derivative(f)) == gcd(G, derivative(G)) == sparse(m['gcd_f']) == sparse(m['gcd_G']) == {0:Q(1)})
    record('entire_linear_quartic_factorization', Q(m['linear_root']) == r and
           times(sparse([-r,1]),H) == G)
    qtaylor = [sum(Q(comb(i,j))*q4.get(i,0)*2**(i-j) for i in range(j,5)) for j in range(5)]
    quartic_sub = sparse([qtaylor[4-j]*c**(4-j) for j in range(5)])
    record('quartic_substitution_every_coefficient', quartic_sub == sparse(m['quartic_substitution']) ==
           {i:-825*x for i,x in H.items()})
    # Both compositions as Laurent monomials in T-2 (or X) and W (or Y).
    # A monomial is (constant, coordinate exponent, vertical exponent).
    forward_X, forward_Y = (c,-1,0), (c*c,-3,1)
    def monomial_product(a,b):
        return (a[0]*b[0],a[1]+b[1],a[2]+b[2])
    def monomial_power(a,n):
        return (a[0]**n,a[1]*n,a[2]*n)
    tminus2 = monomial_product((c,0,0),monomial_power(forward_X,-1))
    back_W = monomial_product((c,0,0),monomial_product(forward_Y,monomial_power(forward_X,-3)))
    inverse_T2, inverse_W = (c,-1,0),(c,-3,1)
    back_X = monomial_product((c,0,0),monomial_power(inverse_T2,-1))
    back_Y = monomial_product((c*c,0,0),monomial_product(inverse_W,monomial_power(inverse_T2,-3)))
    report['curve_compositions'] = [list(v) for v in [tminus2,back_W,back_X,back_Y]]
    record('both_complete_curve_compositions', [tminus2,back_W,back_X,back_Y] ==
           [(1,1,0),(1,0,1),(1,1,0),(1,0,1)])
    record('map_strings', m['forward'] == saved['forward'] and m['inverse'] == saved['inverse'])
    A = sparse([-109375,-32500,150,64,1])
    eta, alpha = sparse(field['eta_in_alpha']), sparse(field['alpha_in_eta'])
    record('L133_polynomial', sparse(field['alpha_polynomial']) == A)
    record('eta_rational_generator_map', remainder(times(eta,sparse([-50,1])),A) == {0:25*c})
    record('alpha_rational_generator_map', remainder(times(plus(alpha,{0:Q(50)},-1),sparse([0,1])),H) == {0:25*c})
    record('both_defining_relations', compose(H,eta,A) == {} and compose(A,alpha,H) == {})
    record('both_inverse_generators', compose(eta,alpha,H) == compose(alpha,eta,A) == {1:Q(1)})
    EA, AE = mat(field['eta_powers_in_alpha']), mat(field['alpha_powers_in_eta'])
    for name, matrix, image, modulus in [('eta',EA,eta,A),('alpha',AE,alpha,H)]:
        basis = {0:Q(1)}
        for j in range(4):
            record(name+'_power_basis_column_'+str(j), [row[j] for row in matrix] == dense(basis,4))
            basis = remainder(times(basis,image),modulus)
    eye = [[Q(i==j) for j in range(4)] for i in range(4)]
    record('full_matrix_inverses', mm(EA,AE) == mm(AE,EA) == eye)
    record('both_matrix_determinants', det(EA) == Q(field['eta_to_alpha_determinant']) and
           det(AE) == Q(field['alpha_to_eta_determinant']) and det(EA)*det(AE) == 1)
    B = mat([[1,0,'1/2','31/30'],[0,1,'7/25','179/750'],[0,0,'1/50','239/18750'],[0,0,0,'1/18750']])
    BE = mat(field['O_basis_in_eta'])
    record('whole_maximal_order_basis_transport', mat(field['O_basis_in_alpha']) == B and
           mm(AE,B) == BE and mm(EA,BE) == B and det(BE) != 0)
    for name, a, b in [('G',G,derivative(G)),('H',H,derivative(H)),('linear_H',sparse([-r,1]),H)]:
        rec = data['discriminants'][name]
        matrix = mat(rec['matrix'])
        da, db = dense(a),dense(b)
        rows = []
        for polynomial, shifts in [(da,max(b)),(db,max(a))]:
            for shift in range(shifts):
                row = [Q(0)]*(max(a)+max(b))
                row[shift:shift+len(polynomial)] = list(reversed(polynomial))
                rows.append(row)
        record(name+'_entire_Sylvester_matrix', rows == matrix)
        chain = []
        rr = result(a,b,chain)
        report['resultant_chains'][name] = chain
        record(name+'_Euclidean_and_Gaussian_resultant', rr == Q(rec['resultant']) == det(matrix))
        if name in ['G','H']:
            n = max(a)
            value = (-1)**(n*(n-1)//2)*rr/a[n]
            record(name+'_discriminant', value == Q(rec['discriminant']) and value != 0)
        else:
            value = rr
        factor_replay(name,value,rec['factorization'])
    D, DH, R = (Q(data['discriminants'][key][value]) for key,value in
                [('G','discriminant'),('H','discriminant'),('linear_H','resultant')])
    record('factor_product_discriminant', D == DH*R*R)
    # An additional all-prime identity from the complete basis determinants.
    DA = Q(2526820312500000000)  # audited L134 power-order discriminant
    record('quartic_discriminant_field_binding', DH == DA*det(EA)**2)
    record('support_exact', data['support'] == {
        'finite_rational_primes':[2,3,5,11], 'include_infinity':True,
        'minimal_theorem_finite_support':[2,3,5,11],
        'all_primes_in_each_maximal_order_factor':True, 'localization_integer':330})
    record('no_unlisted_discriminant_prime', data['discriminants']['G']['factorization']['factors'] ==
           [[2,32],[3,21],[5,27],[11,35]])
    report['status'] = 'PASS'
except Exception as exc:
    report['status'] = 'FAIL'
    report['exception'] = {'type':type(exc).__name__,'message':str(exc),'traceback':traceback.format_exc()}
    if not report['failures']:
        report['failures'].append(str(exc))
finally:
    OUTPUT.write_text(json.dumps(encode(report),indent=2)+'\n')
    print(json.dumps({'status':report['status'],'checks':len(report['checks']),
        'failures':report['failures'],'actual_required_bounds':report['bounds'],
        'certificate':str(OUTPUT.relative_to(HERE.parent.parent))}))
if report['status'] != 'PASS':
    raise SystemExit(1)
