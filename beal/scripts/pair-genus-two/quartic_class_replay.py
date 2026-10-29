"""Independent complete replay; imports only instrumentation/accounting.

Uses descending polynomial arithmetic, power-basis reconstruction,
determinants by permutations, and nonpivot-coordinate membership tests.
"""
import json
from pathlib import Path
from hashlib import sha256
from itertools import permutations
from fractions import Fraction as Q
from quartic_class_budget import run
ROOT = Path(__file__).resolve().parent
RESULT = dict(completed=False, failures=[], checks=0, regular=[], exceptional=[])

def check(value, name):
    RESULT['checks'] = RESULT['checks'] + 1
    if not value:
        raise AssertionError(name)

def dump():
    (ROOT / 'quartic-class-verification.json').write_text(json.dumps(RESULT, indent=2) + '\n')

def desc(a):
    while len(a) > 1 and a[0] == 0:
        a.pop(0)
    return a

def divmod_poly(a, h, p):
    b.charge('polynomial_divisions')
    work, divisor = list(reversed(a)), list(reversed(h))
    quotient = []
    while len(work) >= len(divisor):
        c = work[0] % p
        quotient.append(c)
        work = [(x - c * divisor[i]) % p if i < len(divisor) else x
                for i, x in enumerate(work)]
        check(work[0] == 0, 'division eliminates leading term')
        work.pop(0)
    return list(reversed(desc(quotient or [0]))), list(reversed(desc(work or [0])))

def candidates(p, d):
    for n in range(p ** d):
        # Lexicographic low-first coefficient lists without itertools.product.
        value = n
        coefficients = [0] * d
        for i in range(d - 1, -1, -1):
            coefficients[i] = value % p
            value = value // p
        yield coefficients + [1]

def polynomial_value(a, x):
    y = 0
    for c in reversed(a):
        y = y * x + c
    return y

def multiply(a, c, table):
    out = [0] * 4
    for i, x in enumerate(a):
        for j, y in enumerate(c):
            for k, z in enumerate(table[i][j]):
                out[k] = out[k] + x * y * z
    return out

def unit(i):
    return [int(i == j) for j in range(4)]

def member(w, v, p):
    b.charge('subspace_tests')
    piv = [next(i for i, x in enumerate(row) if x) for row in w]
    return all((v[j] - sum(v[c] * row[j] for c, row in zip(piv, w))) % p == 0
               for j in range(4) if j not in piv)

def canonical(w, p):
    check(len(w) <= 4, 'subspace dimension')
    piv = []
    for row in w:
        check(len(row) == 4 and all(0 <= x < p for x in row) and any(row), 'RREF row domain')
        c = next(i for i, x in enumerate(row) if x)
        check(row[c] == 1, 'unit pivot')
        piv.append(c)
    check(piv == sorted(set(piv)), 'ordered distinct pivots')
    check([[row[c] for c in piv] for row in w] ==
          [[int(i == j) for j in range(len(w))] for i in range(len(w))], 'reduced pivot columns')
    return piv

def det(a):
    total = 0
    for perm in permutations(range(4)):
        inversions = sum(int(perm[i] > perm[j]) for i in range(4) for j in range(i + 1, 4))
        term = (-1) ** inversions
        for i in range(4):
            term = term * a[i][perm[i]]
        total = total + term
    return total

def verify_lattice(I, w, p, table):
    canonical(w, p)
    cols = I['columns']
    check(len(cols) == 4 and all(len(c) == 4 for c in cols), 'four-dimensional lattice')
    check(all(member(w, c, p) for c in cols), 'lattice reduces into claimed ideal')
    norm = abs(det(cols))
    check(norm == p ** (4 - len(w)) and norm == I['norm'], 'exact determinant index')
    pc = I['p_coordinates']
    check(len(pc) == 4, 'p containment domain')
    for i, coords in enumerate(pc):
        check(len(coords) == 4, 'p coordinate length')
        check([sum(coords[k] * cols[k][j] for k in range(4)) for j in range(4)] ==
              [p * x for x in unit(i)], 'contains every p basis vector')
    actions = I['closure_actions']
    check(len(actions) == 4 and all(len(a) == 4 for a in actions), 'action domain')
    for i in range(4):
        for j in range(4):
            coords = actions[i][j]
            check(len(coords) == 4, 'closure coordinate length')
            check([sum(coords[k] * cols[k][t] for k in range(4)) for t in range(4)] ==
                  multiply(unit(i), cols[j], table), 'integral ideal closure')

def key(w):
    return tuple(tuple(row) for row in w)

def expected_spaces(p):
    result = set()
    for mask in range(16):
        piv = [c for c in range(4) if mask & (1 << c)]
        free = [(i, j) for i, c in enumerate(piv) for j in range(4) if j > c and j not in piv]
        for n in range(p ** len(free)):
            b.charge('exceptional_subspaces')
            value = n
            w = [[int(j == c) for j in range(4)] for c in piv]
            for i, j in free:
                w[i][j] = value % p
                value = value // p
            result.add(key(w))
    return result

def main():
    source = ROOT / 'quartic-class-certificate.json'
    payload = source.read_bytes()
    data = json.loads(payload)
    RESULT['certificate_sha256'] = sha256(payload).hexdigest()
    order_payload = (ROOT / 'quartic-order-certificate.json').read_bytes()
    old = json.loads(order_payload)
    final = old['orders'][old['final_order_id']]
    check(data['input_sha256'] == sha256(order_payload).hexdigest(), 'bind audited input')
    check(data['completed'] and data['failures'] == [], 'producer completed without failures')
    for k in final:
        check(data['order'][k] == final[k], 'full final-order input: ' + k)
    g = [-109375, -32500, 150, 64, 1]
    check(data['polynomial'] == g and old['polynomial'] == g, 'exact field')
    check(data['index'] == old['total_index'] and data['index'] == 937500, 'exact index')
    b.phase('replay: rebuild full multiplication from power basis')
    basis = [[Q(1), Q(0), Q(1, 2), Q(31, 30)],
             [Q(0), Q(1), Q(7, 25), Q(179, 750)],
             [Q(0), Q(0), Q(1, 50), Q(239, 18750)],
             [Q(0), Q(0), Q(0), Q(1, 18750)]]
    inverse = [[1, 0, -25, -13400], [0, 1, -14, -1129],
               [0, 0, 50, -11950], [0, 0, 0, 18750]]
    check([[Q(x) for x in row] for row in final['basis']] == basis, 'canonical integral basis')
    check(final['inverse'] == inverse, 'canonical inverse')
    check([[sum(inverse[i][k] * basis[k][j] for k in range(4)) for j in range(4)] for i in range(4)] ==
          [unit(i) for i in range(4)], 'basis inverse')
    table = []
    for i in range(4):
        row = []
        for j in range(4):
            terms = [sum(basis[u][i] * basis[v][j] for u in range(4) for v in range(4) if u + v == k)
                     for k in range(7)]
            for k in range(6, 3, -1):
                c = terms[k]
                for t in range(4):
                    terms[k - 4 + t] = terms[k - 4 + t] - c * g[t]
                terms[k] = 0
            coordinates = [sum(inverse[t][k] * terms[k] for k in range(4)) for t in range(4)]
            check(all(c.denominator == 1 for c in coordinates), 'integral rebuilt product')
            row.append([int(c) for c in coordinates])
        table.append(row)
    check(table == final['table'], 'complete multiplication table rebuilt')
    sig = data['signature']
    check([r[0] for r in sig['values']] == list(range(-100, 101)), 'full sign-scan domain')
    for x, y in sig['values']:
        b.charge('sign_evaluations')
        check(polynomial_value(g, x) == y, 'exact sign value')
    intervals = [[a, c] for a, c in zip(sig['values'], sig['values'][1:]) if a[1] * c[1] < 0]
    check(intervals == sig['intervals'] and len(intervals) == 4, 'four disjoint real intervals')
    check(sig['real'] == 4 and sig['complex_pairs'] == 0, 'degree-four signature')
    D = final['discriminant']
    bound = data['bound']
    U = bound['U']
    check(D == 2874960 and bound['discriminant'] == D and bound['coefficient'] == '3/32', 'Minkowski inputs')
    check(D < bound['sqrt_upper'] ** 2 and 3 * bound['sqrt_upper'] == 32 * U and U <= 300, 'rational upper cutoff')
    trials = data['prime_trials']
    check([r['n'] for r in trials] == list(range(2, U + 1)), 'rational-prime domain')
    primes = []
    for r in trials:
        n = r['n']
        divisors = []
        d = 2
        while d * d <= n:
            divisors.append([d, n % d])
            d = d + 1
        check(divisors == r['divisions'], 'all trial divisions through square root')
        prime = not any(rem == 0 for d, rem in divisors)
        check(prime == r['prime'], 'primality decision')
        if prime:
            primes.append(n)
    check(primes == data['primes'], 'complete rational-prime list')
    check([r['p'] for r in data['regular']] == [p for p in primes if p not in (2, 3, 5)], 'regular domain')
    check([r['p'] for r in data['exceptional']] == [2, 3, 5], 'exceptional domain')
    generators = []
    for r in data['regular']:
        p = r['p']
        b.phase('replay: regular ' + str(p))
        check(data['index'] % p != 0, 'regular-prime hypothesis')
        residual = [x % p for x in g]
        extracted, at = [], 0
        for degree in (1, 2):
            for h in candidates(p, degree):
                entry = r['extraction'][at]
                at = at + 1
                check(h == entry['factor'], 'complete factor-search domain')
                attempt_id = 0
                while len(residual) - 1 >= 2 * degree:
                    saved = entry['attempts'][attempt_id]
                    attempt_id = attempt_id + 1
                    check(saved['dividend'] == residual, 'factor extraction state')
                    q, rem = divmod_poly(residual, h, p)
                    check(q == saved['quotient'] and rem == saved['remainder'], 'complete division evidence')
                    if any(rem):
                        break
                    extracted.append(h)
                    residual = q
                check(attempt_id == len(entry['attempts']), 'no omitted or surplus division')
        check(at == len(r['extraction']), 'factor-search exact length')
        if len(residual) > 1:
            extracted.append(residual)
        check(extracted == r['factors'], 'all factors with multiplicity')
        # Independently reconstruct product by descending convolution.
        rebuilt = [1]
        for h in extracted:
            hdesc = list(reversed(h))
            rebuilt = [sum(rebuilt[i] * hdesc[k - i] for i in range(len(rebuilt))
                           if 0 <= k - i < len(hdesc)) % p for k in range(len(rebuilt) + len(hdesc) - 1)]
        check(list(reversed(rebuilt)) == [x % p for x in g], 'factor product')
        distinct = []
        for h in extracted:
            if h not in distinct:
                distinct.append(h)
        check([s['factor'] for s in r['irreducibility']] == distinct, 'irreducibility coverage')
        for s in r['irreducibility']:
            h, at = s['factor'], 0
            for degree in range(1, (len(h) - 1) // 2 + 1):
                for divisor in candidates(p, degree):
                    rec = s['tests'][at]
                    at = at + 1
                    check(rec['divisor'] == divisor, 'full irreducibility divisor domain')
                    q, rem = divmod_poly(h, divisor, p)
                    check(q == rec['quotient'] and rem == rec['remainder'] and any(rem), 'irreducible factor test')
            check(at == len(s['tests']), 'irreducibility exact length')
        check([I['factor'] for I in r['ideals']] == distinct, 'prime-ideal factor coverage')
        for I in r['ideals']:
            h = I['factor']
            # Evaluate using powers, independently of the producer's Horner rule.
            power, value = unit(0), [0] * 4
            for c in h:
                value = [v + c * x for v, x in zip(value, power)]
                power = multiply(power, unit(1), table)
            check(value == I['h_alpha'], 'factor evaluation in maximal order')
            images = [multiply(value, unit(i), table) for i in range(4)]
            check(images == I['image_generators'], 'full principal-ideal image')
            w = I['rref']
            canonical(w, p)
            check(all(member(w, v, p) for v in images), 'images lie in RREF span')
            # The regular-prime theorem independently gives image dimension
            # 4-deg(h). Containment plus this RREF dimension proves equality;
            # no unperformed minor computation is being claimed.
            check(len(w) == 4 - (len(h) - 1), 'exact image dimension')
            verify_lattice(I['lattice'], w, p, table)
            check(I['lattice']['norm'] == p ** (len(h) - 1), 'factor ideal norm')
            check(I['included'] == (I['lattice']['norm'] <= U), 'norm-cutoff inclusion')
            if I['included']:
                generators.append(dict(p=p, factor=h, lattice=I['lattice']))
        RESULT['regular'].append(dict(p=p, factors=r['factors'], norms=[I['lattice']['norm'] for I in r['ideals']]))
        dump()
    for r in data['exceptional']:
        p, spaces = r['p'], r['spaces']
        b.phase('replay: exceptional ' + str(p))
        keys = [key(s['rref']) for s in spaces]
        check(len(set(keys)) == len(keys), 'no duplicate subspaces')
        check(set(keys) == expected_spaces(p), 'complete exceptional RREF domain')
        for s in spaces:
            w = s['rref']
            canonical(w, p)
            invariant = all(member(w, multiply(unit(i), v, table), p) for i in range(4) for v in w)
            check(invariant == s['ideal'], 'full ideal invariance test')
            witness = s['nonideal_witness']
            if invariant:
                check(witness is None, 'ideal has no rejection witness')
            else:
                i, j = witness['basis'], witness['row']
                check(0 <= i < 4 and 0 <= j < len(w), 'nonideal witness domain')
                z = [x % p for x in multiply(unit(i), w[j], table)]
                check(z == witness['product'] and not member(w, z, p), 'valid nonideal witness')
        proper = [i for i, s in enumerate(spaces) if s['ideal'] and len(s['rref']) < 4]
        check(proper == r['proper_ideals'], 'all proper ideals')
        maximal = []
        for i in proper:
            w = spaces[i]['rref']
            supersets = [j for j in proper if len(spaces[j]['rref']) > len(w)
                        and all(member(spaces[j]['rref'], v, p) for v in w)]
            witness = spaces[i]['containing_proper_ideal']
            if supersets:
                check(witness in supersets, 'every rejected ideal has containing proper ideal')
            else:
                check(witness is None, 'maximal ideal has no proper enlargement')
                maximal.append(i)
        check(maximal == r['maximal_ideals'] and maximal == [I['space_id'] for I in r['ideals']], 'all and only maximal ideals')
        for I in r['ideals']:
            verify_lattice(I['lattice'], spaces[I['space_id']]['rref'], p, table)
            check(I['included'] == (I['lattice']['norm'] <= U), 'exceptional norm cutoff')
            if I['included']:
                generators.append(dict(p=p, space_id=I['space_id'], lattice=I['lattice']))
        RESULT['exceptional'].append(dict(p=p, subspaces=len(spaces), proper_ideals=len(proper),
                                         maximal_ideals=maximal, norms=[I['lattice']['norm'] for I in r['ideals']]))
        dump()
    check(generators == data['generators'], 'entire generator list')
    RESULT.update(completed=True, cutoff=U, generators=len(generators),
                  generator_norms=[I['lattice']['norm'] for I in generators], budget=b.summary())
    dump()
    print(json.dumps(dict(completed=True, checks=RESULT['checks'], cutoff=U,
                         generators=len(generators), budget=b.summary(),
                         verification=str(ROOT / 'quartic-class-verification.json'))))

if __name__ == '__main__':
    if not globals().get('__instrumented__'):
        run(__file__)
    else:
        try:
            main()
        except Exception as exc:
            RESULT['failures'].append(repr(exc))
            dump()
            raise
