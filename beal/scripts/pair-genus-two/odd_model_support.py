"""Fixed L110 odd model and descent-support certificate; no search boxes.

Ascending polynomial coefficients; matrices have power-basis columns.
Standard-library exact arithmetic. Re-running overwrites only this output.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import comb, isqrt
import hashlib
import json
import traceback

HERE = Path(__file__).resolve().parent
OUT = HERE / 'odd-model-support-certificate.json'
checks = []
data = {'checks': checks, 'failures': [], 'bounds': {
    'degree_cap': 12, 'matrix_size_cap': 12, 'rational_bits_cap': 4096,
    'prime_trial_cap': 100000, 'max_degree': 0, 'max_matrix_size': 0,
    'max_rational_bits': 0, 'max_prime_trial': 0,
    'meaning': 'finite-domain/size bounds; not an elementary-operation count'}}


def observe(v):
    if isinstance(v, (int, Q)) and not isinstance(v, bool):
        q = Q(v)
        bits = max(abs(q.numerator).bit_length(), q.denominator.bit_length())
        data['bounds']['max_rational_bits'] = max(data['bounds']['max_rational_bits'], bits)
        assert bits <= 4096, 'rational size cap'
    elif isinstance(v, (tuple, list)):
        for x in v:
            observe(x)


def check(name, condition):
    checks.append({'name': name, 'pass': bool(condition)})
    if not condition:
        data['failures'].append(name)
        raise AssertionError(name)


def trim(a):
    a = list(map(Q, a)) or [Q(0)]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    observe(a)
    data['bounds']['max_degree'] = max(data['bounds']['max_degree'], len(a)-1)
    assert len(a) <= 13, 'polynomial degree cap'
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([x*c for x in a])


def mul(a, b):
    v = [Q(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            v[i+j] += x*y
            observe(v[i+j])
    return trim(v)


def divrem(a, b):
    a, b = trim(a), trim(b)
    assert b != [0]
    q = [Q(0)] * max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        d, c = len(a)-len(b), a[-1]/b[-1]
        q[d] += c
        a = add(a, [Q(0)]*d + scale(b, -c))
    return trim(q), a


def rem(a, b):
    return divrem(a, b)[1]


def power(a, n, modulus=None):
    r = [Q(1)]
    for _ in range(n):
        r = mul(r, a)
        if modulus is not None:
            r = rem(r, modulus)
    return r


def evaluate(a, x, modulus=None):
    r = [Q(0)]
    for c in reversed(a):
        r = add(mul(r, x), [c])
        if modulus is not None:
            r = rem(r, modulus)
    return r


def inverse(a, modulus):
    r0, r1, s0, s1 = modulus, a, [Q(0)], [Q(1)]
    while r1 != [0]:
        q, r = divrem(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, add(s0, scale(mul(q, s1), -1))
    assert len(r0) == 1 and r0[0]
    return rem(scale(s0, 1/r0[0]), modulus)


def gcd(a, b):
    while b != [0]:
        a, b = b, rem(a, b)
    return scale(a, 1/a[-1])


def derivative(a):
    return trim([i*a[i] for i in range(1, len(a))])


def determinant(matrix):
    a = [list(map(Q, row)) for row in matrix]
    n = len(a)
    data['bounds']['max_matrix_size'] = max(data['bounds']['max_matrix_size'], n)
    assert n <= 12
    sign, old = 1, Q(1)
    for k in range(n-1):
        if a[k][k] == 0:
            j = next((j for j in range(k+1, n) if a[j][k]), None)
            if j is None:
                return Q(0)
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = a[i][j]*pivot - a[i][k]*a[k][j]
                observe(numerator)
                a[i][j] = numerator/old
                observe(a[i][j])
            a[i][k] = 0
        old = pivot
    return sign*a[-1][-1]


def resultant_record(a, b):
    m, n = len(a)-1, len(b)-1
    # n shifted rows of a (descending), then m shifted rows of b.
    mat = [[Q(0)]*i + list(reversed(a)) + [Q(0)]*(n-1-i) for i in range(n)]
    mat += [[Q(0)]*i + list(reversed(b)) + [Q(0)]*(m-1-i) for i in range(m)]
    return {'matrix': mat, 'resultant': determinant(mat)}


def discriminant_record(a):
    n = len(a)-1
    r = resultant_record(a, derivative(a))
    r['discriminant'] = (-1)**(n*(n-1)//2)*r['resultant']/a[-1]
    return r


def matrix_columns(columns):
    return [[columns[j][i] if i < len(columns[j]) else Q(0) for j in range(4)]
            for i in range(4)]


def mm(a, b):
    ans = [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]
    observe(ans)
    return ans


def factor_integer(n):
    n = abs(int(n))
    trial, divisions, factors = [], [], []
    p = 2
    while n > 1:
        assert p <= 100000, 'prime trial cap with unresolved cofactor'
        data['bounds']['max_prime_trial'] = max(data['bounds']['max_prime_trial'], p)
        trial.append({'divisor': p, 'cofactor_before': n, 'remainder': n % p})
        e = 0
        while n % p == 0:
            divisions.append([n, p, n//p])
            n //= p
            e += 1
        if e:
            factors.append([p, e])
        p += 1
    # Every integer below each retained divisor was tried, proving primality.
    return {'factors': factors, 'trials': trial, 'divisions': divisions, 'cofactor': n}


def encode(v):
    if isinstance(v, Q):
        return int(v) if v.denominator == 1 else str(v)
    if isinstance(v, dict):
        return {k: encode(x) for k, x in v.items()}
    if isinstance(v, (tuple, list)):
        return [encode(x) for x in v]
    return v


try:
    saved_path = HERE/'rank-lower-certificate.json'
    saved = json.loads(saved_path.read_text())['model']
    data['input'] = {'rank_model_sha256': hashlib.sha256(saved_path.read_bytes()).hexdigest(),
                     'saved_model': saved}
    f = list(map(Q, [-308, -2288, 341, 3388, 1034, -704, -275]))
    q4 = list(map(Q, [7, 52, -6, -64, -25]))
    A = list(map(Q, [-109375, -32500, 150, 64, 1]))
    c = Q(saved['c'])
    G = list(map(Q, saved['g']))
    check('exact_saved_c_and_maps', c == -36300 and
          saved['forward'] == 'X=c/(T-2),Y=c^2*W/(T-2)^3' and
          saved['inverse'] == 'T=2+c/X,W=c*Y/X^3')
    check('original_twist', f == scale(mul([-4, 0, 1], q4), 11))
    # Homogeneous substitution of (2X+c)/X; all coefficients, including X^6.
    substituted = [Q(0)]
    for i, a in enumerate(f):
        term = [Q(0)]*(6-i) + scale(power([c, 2], i), a)
        substituted = add(substituted, term)
    check('entire_model_identity', substituted == scale(G, c*c))
    check('monic_integral_degree_five', len(G) == 6 and G[-1] == 1 and
          all(a.denominator == 1 for a in G))
    gcd_f = gcd(f, derivative(f))
    gcd_G = gcd(G, derivative(G))
    check('both_models_squarefree', gcd_f == gcd_G == [1])
    taylor = [sum(f[i]*comb(i, j)*2**(i-j) for i in range(j, 7)) for j in range(7)]
    check('saved_complete_taylor', taylor == list(map(Q, saved['taylor_at_two'])))
    check('nonzero_branch_derivative', taylor[0] == 0 and taylor[1] == c != 0)
    r = Q(9075)
    H, leftover = divrem(G, [-r, 1])
    check('linear_quartic_factorization', leftover == [0] and len(H) == 5 and H[-1] == 1)
    # X^4 Q4(2+c/X) = Q4(2) H(X) = -825 H(X).
    quartic_sub = [Q(0)]
    for i, a in enumerate(q4):
        quartic_sub = add(quartic_sub, [Q(0)]*(4-i) + scale(power([c, 2], i), a))
    check('quartic_branch_substitution', quartic_sub == scale(H, -825))
    # In K=Q[a]/A: eta=25c/(a-50). In Q[e]/H: a=50+25c/e.
    eta = scale(inverse([-50, 1], A), 25*c)
    alpha = add([50], scale(inverse([0, 1], H), 25*c))
    check('eta_defining_relation', evaluate(H, eta, A) == [0])
    check('alpha_defining_relation', evaluate(A, alpha, H) == [0])
    check('inverse_generator_eta', evaluate(eta, alpha, H) == [0, 1])
    check('inverse_generator_alpha', evaluate(alpha, eta, A) == [0, 1])
    E_to_A = matrix_columns([power(eta, j, A) for j in range(4)])
    A_to_E = matrix_columns([power(alpha, j, H) for j in range(4)])
    I = [[Q(i == j) for j in range(4)] for i in range(4)]
    check('both_full_basis_compositions', mm(E_to_A, A_to_E) == I and mm(A_to_E, E_to_A) == I)
    # L134's full O-basis in alpha, not the nonmaximal order Z[eta].
    B = [[Q(1), 0, Q(1, 2), Q(31, 30)],
         [0, Q(1), Q(7, 25), Q(179, 750)],
         [0, 0, Q(1, 50), Q(239, 18750)],
         [0, 0, 0, Q(1, 18750)]]
    transported_B = mm(A_to_E, B)
    check('transported_entire_maximal_basis', mm(E_to_A, transported_B) == B)
    check('nondegenerate_maximal_basis', determinant(transported_B) != 0)
    data['model'] = {'f': f, 'q4': q4, 'c': c, 'G': G,
                     'homogeneous_substitution': substituted, 'taylor': taylor,
                     'gcd_f': gcd_f, 'gcd_G': gcd_G, 'linear_root': r, 'H': H,
                     'quartic_substitution': quartic_sub,
                     'forward': saved['forward'], 'inverse': saved['inverse']}
    data['field'] = {'alpha_polynomial': A, 'eta_in_alpha': eta, 'alpha_in_eta': alpha,
                     'eta_powers_in_alpha': E_to_A, 'alpha_powers_in_eta': A_to_E,
                     'eta_to_alpha_determinant': determinant(E_to_A),
                     'alpha_to_eta_determinant': determinant(A_to_E),
                     'O_basis_in_alpha': B, 'O_basis_in_eta': transported_B}
    discs = {'G': discriminant_record(G), 'H': discriminant_record(H),
             'linear_H': resultant_record([-r, 1], H)}
    dG, dH, resultant = discs['G']['discriminant'], discs['H']['discriminant'], discs['linear_H']['resultant']
    check('discriminant_integral_nonzero', dG.denominator == dH.denominator == 1 and dG*dH != 0)
    check('factor_discriminant_identity', dG == dH*resultant**2)
    for name, value in [('G', dG), ('H', dH), ('linear_H', resultant)]:
        discs[name]['factorization'] = factor_integer(value)
        facts = discs[name]['factorization']['factors']
        product = 1
        for p, e in facts:
            product *= p**e
        check(name+'_complete_prime_factorization', product == abs(value))
    finite = sorted({2, 3, 5, 11} | {p for p, e in discs['G']['factorization']['factors'] if e >= 2})
    data['support'] = {'finite_rational_primes': finite, 'include_infinity': True,
                       'minimal_theorem_finite_support': sorted({2} | {p for p, e in discs['G']['factorization']['factors'] if e >= 2}),
                       'all_primes_in_each_maximal_order_factor': True,
                       'localization_integer': 1}
    for p in finite:
        data['support']['localization_integer'] *= p
    check('contains_L137_localization', data['support']['localization_integer'] % 330 == 0)
    data['discriminants'] = discs
    data['status'] = 'PASS'
except Exception as exc:
    data['status'] = 'FAIL'
    data['exception'] = {'type': type(exc).__name__, 'message': str(exc), 'traceback': traceback.format_exc()}
    if not data['failures']:
        data['failures'].append(str(exc))
finally:
    OUT.write_text(json.dumps(encode(data), indent=2)+'\n')
    print(json.dumps({'status': data.get('status'), 'checks': len(checks),
                      'failures': data['failures'], 'actual_required_bounds': data['bounds'],
                      'support': data.get('support'), 'certificate': str(OUT.relative_to(HERE.parent.parent))}))
if data.get('status') != 'PASS':
    raise SystemExit(1)
