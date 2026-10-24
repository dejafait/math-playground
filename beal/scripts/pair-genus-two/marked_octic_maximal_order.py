"""Exact Lenstra radical/multiplier certificate for L115; standard library only.

Matrices act on columns. Field coordinates are 1,t,...,t^7 in Q[t]/(F).
No class groups, numerical fields, or trace-radical shortcut are used.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import isqrt
import json
import traceback

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / 'marked-octic-maximal-order-certificate.json'
N = 8
F = [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(c) for c in zip(*a)]


def mm(a, b):
    return [[sum(x*y for x, y in zip(r, c)) for c in zip(*b)] for r in a]


def mv(a, v):
    return [sum(x*y for x, y in zip(r, v)) for r in a]


def inverse(a):
    n = len(a)
    m = [list(map(Q, r))+s for r, s in zip(a, eye(n))]
    for j in range(n):
        k = next(i for i in range(j, n) if m[i][j])
        m[j], m[k] = m[k], m[j]
        d = m[j][j]
        m[j] = [x/d for x in m[j]]
        for i in range(n):
            if i != j:
                d = m[i][j]
                m[i] = [x-d*y for x, y in zip(m[i], m[j])]
    return [r[n:] for r in m]


def determinant(a):
    """Fraction-free elimination with exact rational pivots."""
    a = [list(map(Q, r)) for r in a]
    sign, old = 1, Q(1)
    for k in range(len(a)-1):
        if not a[k][k]:
            j = next((j for j in range(k+1, len(a)) if a[j][k]), None)
            if j is None:
                return Q(0)
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                a[i][j] = (pivot*a[i][j]-a[i][k]*a[k][j])/old
            a[i][k] = 0
        old = pivot
    return sign*a[-1][-1]


def ints(a):
    if isinstance(a, list):
        return [ints(x) for x in a]
    a = Q(a)
    assert a.denominator == 1, ('nonintegral', str(a))
    return int(a)


def encode(a):
    if isinstance(a, Q):
        return int(a) if a.denominator == 1 else str(a)
    if isinstance(a, list):
        return [encode(x) for x in a]
    if isinstance(a, dict):
        return {k: encode(v) for k, v in a.items()}
    return a


POWERS = eye(N)
for degree in range(N, 2*N-1):
    v = [Q(0)]*N
    for k in range(N):
        for j in range(N):
            v[j] -= Q(F[k], F[N])*POWERS[degree-N+k][j]
    POWERS.append(v)


def field_product(a, b):
    v = [Q(0)]*N
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    for k, z in enumerate(POWERS[i+j]):
                        v[k] += x*y*z
    return v


def order(basis):
    bi = inverse(basis)
    assert mm(basis, bi) == eye(N) == mm(bi, basis)
    cols = transpose(basis)
    table = [[ints(mv(bi, field_product(x, y))) for y in cols] for x in cols]
    one = ints(mv(bi, [1]+[0]*(N-1)))
    traces = [sum(table[i][j][j] for j in range(N)) for i in range(N)]
    gram = [[sum(a*b for a, b in zip(v, traces)) for v in row] for row in table]
    disc = ints(determinant(gram))
    assert disc != 0
    return dict(basis=basis, inverse=bi, one=one, table=table,
                traces=traces, gram=gram, discriminant=disc)


def fp_product(a, b, table, p):
    return [sum(a[i]*b[j]*table[i][j][k] for i in range(N) for j in range(N)) % p
            for k in range(N)]


def fp_power(a, q, one, table, p):
    r = [x % p for x in one]
    while q:
        if q & 1:
            r = fp_product(r, a, table, p)
        q >>= 1
        if q:
            a = fp_product(a, a, table, p)
    return r


def kernel(a, p):
    """Full row reduction, recording operations, rank, free columns and nullspace."""
    r = [[int(x) % p for x in row] for row in a]
    pivots, operations = [], []
    for j in range(len(r[0])):
        h = len(pivots)
        k = next((k for k in range(h, len(r)) if r[k][j]), None)
        if k is None:
            continue
        if k != h:
            r[k], r[h] = r[h], r[k]
            operations.append(['swap', h, k])
        c = pow(r[h][j], -1, p)
        r[h] = [c*x % p for x in r[h]]
        operations.append(['scale', h, c])
        for k in range(len(r)):
            if k != h and r[k][j]:
                c = -r[k][j] % p
                r[k] = [(x+c*y) % p for x, y in zip(r[k], r[h])]
                operations.append(['add', k, h, c])
        pivots.append(j)
    free = [j for j in range(len(r[0])) if j not in pivots]
    vectors = []
    for j in free:
        v = [0]*len(r[0])
        v[j] = 1
        for h, k in enumerate(pivots):
            v[k] = -r[h][j] % p
        vectors.append(v)
    assert all(all(sum(x*y for x, y in zip(row, v)) % p == 0 for row in a)
               for v in vectors)
    return dict(rref=r, pivots=pivots, free=free, vectors=vectors,
                rank=len(pivots), operations=operations)


def inverse_image_lattice(kern, p):
    # L = {v in Z^n : v mod p lies in kernel}. Each free-coordinate
    # vector is normalized there; p times the pivot e_i finish a basis.
    cols = []
    freevectors = dict(zip(kern['free'], kern['vectors']))
    for j in range(N):
        cols.append(freevectors[j] if j in freevectors else
                    [p*int(i == j) for i in range(N)])
    return transpose(cols)


def radical_multiplier(o, p):
    q = p
    while q < N:
        q *= p
    frob = transpose([fp_power([int(i == j) for i in range(N)], q,
                                o['one'], o['table'], p) for j in range(N)])
    nil = kernel(frob, p)
    jmat = inverse_image_lattice(nil, p)
    ji = inverse(jmat)
    assert abs(determinant(jmat)) == p**nil['rank']
    assert ints(mm(ji, [[p*x for x in r] for r in eye(N)]))
    actions = []
    for i in range(N):
        mi = transpose(o['table'][i])
        actions.append(ints(mm(mm(ji, mi), jmat)))
    joint = [[actions[k][i][j] % p for k in range(N)]
             for i in range(N) for j in range(N)]
    ann = kernel(joint, p)
    # pM is inverse image of the joint kernel; dividing its lattice by p
    # gives the full multiplier ring, including the old order.
    emat = [[Q(x, p) for x in row] for row in inverse_image_lattice(ann, p)]
    ei = inverse(emat)
    inclusion = ints(ei)
    assert abs(determinant(emat)) == Q(1, p**len(ann['free']))
    multiplier_actions = []
    for v in transpose(emat):
        m = [[sum(v[k]*actions[k][i][j] for k in range(N))
              for j in range(N)] for i in range(N)]
        multiplier_actions.append(ints(m))
    return dict(prime=p, frobenius_exponent=q, frobenius_matrix=frob,
                nilpotent_kernel=nil, radical_basis=jmat, radical_inverse=ji,
                action_matrices=actions, joint_matrix=joint,
                multiplier_kernel=ann, overorder_transform=emat,
                overorder_inverse=ei, old_in_new=inclusion,
                multiplier_actions=multiplier_actions,
                index=p**len(ann['free']), terminal=not ann['free'])


def factor_disc(d):
    remaining = abs(d)
    result = {}
    divisions = []
    for p in [2, 3, 5, 11]:
        assert p >= 2 and all(p % k for k in range(2, isqrt(p)+1))
        e, chain = 0, [remaining]
        while remaining % p == 0:
            e += 1
            remaining //= p
            chain.append(remaining)
        result[str(p)] = e
        divisions.append(dict(prime=p, exponent=e, chain=chain))
    assert remaining == 1, ('unfactored discriminant', remaining)
    return result, divisions


def save(c):
    OUTPUT.write_text(json.dumps(encode(c), indent=2)+'\n')


def main():
    c = dict(method='Lenstra Theorem 4.5, all-prime radical/multiplier iteration',
             polynomial=F, dimension=N, coordinate_convention='basis vectors are columns in 1,t,...,t^7',
             orders=[], steps=[], final_checks=[], failures=[])
    try:
        desc = list(reversed(F))
        cols = [[Q(1)]+[Q(0)]*(N-1)]
        for i in range(1, N):
            cols.append([Q(desc[i-j]) if j <= i else Q(0) for j in range(N)])
        initial = order(transpose(cols))
        c['orders'].append(initial)
        c['initial_factorization'], c['initial_divisions'] = factor_disc(initial['discriminant'])
        expected = 2**72*3**27*5**8*11**7
        assert initial['discriminant'] == expected
        assert initial['discriminant']*11**14 == 2**72*3**27*5**8*11**21
        c['polynomial_discriminant_crosscheck'] = expected
        save(c)
        current = 0
        for ps, e in c['initial_factorization'].items():
            p, strict = int(ps), 0
            if e < 2:
                continue
            cap = e//2
            while True:
                s = radical_multiplier(c['orders'][current], p)
                s['order_id'], s['strict_cap'] = current, cap
                c['steps'].append(s)
                if s['terminal']:
                    print('prime', p, 'strict_steps', strict, 'cap', cap, 'terminal_rank', s['multiplier_kernel']['rank'], flush=True)
                    save(c)
                    break
                strict += 1
                assert strict <= cap, ('strict cap exceeded', p, strict, cap)
                old = c['orders'][current]
                new = order(mm(old['basis'], s['overorder_transform']))
                assert old['discriminant'] == s['index']**2*new['discriminant']
                assert mm(new['inverse'], old['basis']) == s['old_in_new']
                assert mm(old['inverse'], new['basis']) == s['overorder_transform']
                c['orders'].append(new)
                current = len(c['orders'])-1
                s['next_order_id'] = current
                save(c)
        c['final_order_id'] = current
        final = c['orders'][current]
        for ps, e in c['initial_factorization'].items():
            if e >= 2:
                s = radical_multiplier(final, int(ps))
                s['order_id'] = current
                c['final_checks'].append(s)
                assert s['terminal'] and s['multiplier_kernel']['rank'] == N
                save(c)
        itof = ints(mm(final['inverse'], initial['basis']))
        idx = abs(ints(determinant(itof)))
        assert initial['discriminant'] == idx**2*final['discriminant']
        c['initial_in_final'] = itof
        c['total_index'] = idx
        c['final_factorization'], c['final_divisions'] = factor_disc(final['discriminant'])
        c['completed'] = True
    except Exception:
        c['failures'].append(traceback.format_exc())
        c['completed'] = False
        save(c)
        raise
    save(c)
    print('completed', c['completed'], 'orders', len(c['orders']), 'steps', len(c['steps']))
    print('field_discriminant', final['discriminant'], 'factorization', c['final_factorization'])
    print('total_index', idx, 'failures', len(c['failures']), 'certificate', OUTPUT)


if __name__ == '__main__':
    main()
