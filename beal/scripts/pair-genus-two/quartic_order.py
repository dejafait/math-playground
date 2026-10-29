"""Exact Stevenhagen Section 9 radical/multiplier certificate for L133.

Matrices act on columns. Field coordinates are 1,alpha,alpha^2,alpha^3 in Q[t]/(F).
No class groups, numerical fields, or trace-radical shortcut are used.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import isqrt
import json
import traceback
from quartic_order_budget import Budget
budget = Budget()
HERE = Path(__file__).resolve().parent
OUTPUT = budget.op('/', HERE, 'quartic-order-certificate.json')
budget.phase('generation: power-basis multiplication setup')
N = 4
F = [budget.op('-', 0, 109375), budget.op('-', 0, 32500), 150, 64, 1]

def eye(n):
    return [[budget.rational(budget.cmp('==', i, j)) for j in range(n)] for i in range(n)]

def transpose(a):
    return [list(c) for c in zip(*a)]

def mm(a, b):
    return [[budget.scalar_sum((budget.op('*', x, y) for x, y in zip(r, c))) for c in zip(*b)] for r in a]

def mv(a, v):
    return [budget.scalar_sum((budget.op('*', x, y) for x, y in zip(r, v))) for r in a]

def inverse(a):
    n = len(a)
    m = [budget.op('+', list(map(budget.rational, r)), s) for r, s in zip(a, eye(n))]
    for j in range(n):
        k = next((i for i in range(j, n) if m[i][j]))
        m[j], m[k] = (m[k], m[j])
        d = m[j][j]
        m[j] = [budget.op('/', x, d) for x in m[j]]
        for i in range(n):
            if budget.cmp('!=', i, j):
                d = m[i][j]
                m[i] = [budget.op('-', x, budget.op('*', d, y)) for x, y in zip(m[i], m[j])]
    return [r[n:] for r in m]

def determinant(a):
    """Fraction-free elimination with exact rational pivots."""
    a = [list(map(budget.rational, r)) for r in a]
    sign, old = (1, budget.rational(1))
    for k in range(budget.op('-', len(a), 1)):
        if not a[k][k]:
            j = next((j for j in range(budget.op('+', k, 1), len(a)) if a[j][k]), None)
            if budget.cmp('is', j, None):
                return budget.rational(0)
            a[k], a[j] = (a[j], a[k])
            sign = budget.op('-', 0, sign)
        pivot = a[k][k]
        for i in range(budget.op('+', k, 1), len(a)):
            for j in range(budget.op('+', k, 1), len(a)):
                a[i][j] = budget.op('/', budget.op('-', budget.op('*', pivot, a[i][j]), budget.op('*', a[i][k], a[k][j])), old)
            a[i][k] = 0
        old = pivot
    return budget.op('*', sign, a[budget.op('-', 0, 1)][budget.op('-', 0, 1)])

def ints(a):
    if isinstance(a, list):
        return [ints(x) for x in a]
    a = budget.rational(a)
    assert budget.cmp('==', a.denominator, 1), ('nonintegral', str(a))
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
for degree in range(N, budget.op('-', budget.op('*', 2, N), 1)):
    v = budget.op('*', [budget.rational(0)], N)
    for k in range(N):
        for j in range(N):
            v[j] = budget.op('-', v[j], budget.op('*', budget.rational(F[k], F[N]), POWERS[budget.op('+', budget.op('-', degree, N), k)][j]))
    POWERS.append(v)

def field_product(a, b):
    v = budget.op('*', [budget.rational(0)], N)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    for k, z in enumerate(POWERS[budget.op('+', i, j)]):
                        v[k] = budget.op('+', v[k], budget.op('*', budget.op('*', x, y), z))
    return v

def order(basis):
    bi = inverse(basis)
    assert budget.cmp('==', mm(basis, bi), eye(N)) and budget.cmp('==', eye(N), mm(bi, basis))
    cols = transpose(basis)
    table = [[ints(mv(bi, field_product(x, y))) for y in cols] for x in cols]
    one = ints(mv(bi, budget.op('+', [1], budget.op('*', [0], budget.op('-', N, 1)))))
    traces = [budget.scalar_sum((table[i][j][j] for j in range(N))) for i in range(N)]
    gram = [[budget.scalar_sum((budget.op('*', a, b) for a, b in zip(v, traces))) for v in row] for row in table]
    disc = ints(determinant(gram))
    assert budget.cmp('!=', disc, 0)
    return dict(basis=basis, inverse=bi, one=one, table=table, traces=traces, gram=gram, discriminant=disc)

def fp_product(a, b, table, p):
    return [budget.op('%', budget.scalar_sum((budget.op('*', budget.op('*', a[i], b[j]), table[i][j][k]) for i in range(N) for j in range(N))), p) for k in range(N)]

def fp_power(a, q, one, table, p):
    r = [budget.op('%', x, p) for x in one]
    while q:
        if budget.op('&', q, 1):
            r = fp_product(r, a, table, p)
        q = budget.op('>>', q, 1)
        if q:
            a = fp_product(a, a, table, p)
    return r

def kernel(a, p):
    """Full row reduction, recording operations, rank, free columns and nullspace."""
    r = [[budget.op('%', int(x), p) for x in row] for row in a]
    pivots, operations = ([], [])
    for j in range(len(r[0])):
        h = len(pivots)
        k = next((k for k in range(h, len(r)) if r[k][j]), None)
        if budget.cmp('is', k, None):
            continue
        if budget.cmp('!=', k, h):
            r[k], r[h] = (r[h], r[k])
            operations.append(['swap', h, k])
        c = budget.modpow(r[h][j], budget.op('-', 0, 1), p)
        r[h] = [budget.op('%', budget.op('*', c, x), p) for x in r[h]]
        operations.append(['scale', h, c])
        for k in range(len(r)):
            if budget.cmp('!=', k, h) and r[k][j]:
                c = budget.op('%', budget.op('-', 0, r[k][j]), p)
                r[k] = [budget.op('%', budget.op('+', x, budget.op('*', c, y)), p) for x, y in zip(r[k], r[h])]
                operations.append(['add', k, h, c])
        pivots.append(j)
    free = [j for j in range(len(r[0])) if budget.cmp('not in', j, pivots)]
    vectors = []
    for j in free:
        v = budget.op('*', [0], len(r[0]))
        v[j] = 1
        for h, k in enumerate(pivots):
            v[k] = budget.op('%', budget.op('-', 0, r[h][j]), p)
        vectors.append(v)
    assert all((all((budget.cmp('==', budget.op('%', budget.scalar_sum((budget.op('*', x, y) for x, y in zip(row, v))), p), 0) for row in a)) for v in vectors))
    return dict(rref=r, pivots=pivots, free=free, vectors=vectors, rank=len(pivots), operations=operations)

def inverse_image_lattice(kern, p):
    cols = []
    freevectors = dict(zip(kern['free'], kern['vectors']))
    for j in range(N):
        cols.append(freevectors[j] if budget.cmp('in', j, freevectors) else [budget.op('*', p, int(budget.cmp('==', i, j))) for i in range(N)])
    return transpose(cols)

def radical_multiplier(o, p):
    q = p
    while budget.cmp('<=', q, N):
        q = budget.op('*', q, p)
    frob = transpose([fp_power([int(budget.cmp('==', i, j)) for i in range(N)], q, o['one'], o['table'], p) for j in range(N)])
    nil = kernel(frob, p)
    jmat = inverse_image_lattice(nil, p)
    ji = inverse(jmat)
    assert budget.cmp('==', abs(determinant(jmat)), budget.op('**', p, nil['rank']))
    assert ints(mm(ji, [[budget.op('*', p, x) for x in r] for r in eye(N)]))
    actions = []
    for i in range(N):
        mi = transpose(o['table'][i])
        actions.append(ints(mm(mm(ji, mi), jmat)))
    joint = [[budget.op('%', actions[k][i][j], p) for k in range(N)] for i in range(N) for j in range(N)]
    ann = kernel(joint, p)
    emat = [[budget.rational(x, p) for x in row] for row in inverse_image_lattice(ann, p)]
    ei = inverse(emat)
    inclusion = ints(ei)
    assert budget.cmp('==', abs(determinant(emat)), budget.rational(1, budget.op('**', p, len(ann['free']))))
    multiplier_actions = []
    for v in transpose(emat):
        m = [[budget.scalar_sum((budget.op('*', v[k], actions[k][i][j]) for k in range(N))) for j in range(N)] for i in range(N)]
        multiplier_actions.append(ints(m))
    return dict(prime=p, frobenius_exponent=q, frobenius_matrix=frob, nilpotent_kernel=nil, radical_basis=jmat, radical_inverse=ji, action_matrices=actions, joint_matrix=joint, multiplier_kernel=ann, overorder_transform=emat, overorder_inverse=ei, old_in_new=inclusion, multiplier_actions=multiplier_actions, index=budget.op('**', p, len(ann['free'])), terminal=not ann['free'])

def factor_disc(d):
    remaining = abs(d)
    factors, trials = ({}, [])
    p = 2
    ACTIVE_CERT['factor_in_progress'] = dict(value=d, trial_chain=trials)
    while budget.cmp('<=', budget.op('*', p, p), remaining):
        budget.charge('factor_trials')
        before = remaining
        chain = [remaining]
        while budget.cmp('==', budget.op('%', remaining, p), 0):
            remaining = budget.op('//', remaining, p)
            chain.append(remaining)
        trials.append(dict(divisor=p, before=before, chain=chain))
        if budget.cmp('>', len(chain), 1):
            factors[str(p)] = budget.op('-', len(chain), 1)
        p = budget.op('+', p, 1)
    if budget.cmp('>', remaining, 1):
        factors[str(remaining)] = 1
    return dict(value=d, factors=factors, trial_chain=trials, next_divisor=p, residual=remaining)

def save(c):
    OUTPUT.write_text(budget.op('+', json.dumps(encode(c), indent=2), '\n'))
    budget.save()

def main():
    global ACTIVE_CERT
    c = dict(method='Stevenhagen Section 9 Proposition 9.3', polynomial=F, dimension=N, coordinate_convention='columns in 1,alpha,alpha^2,alpha^3', orders=[], steps=[], final_checks=[], failures=[], completed=False)
    ACTIVE_CERT = c
    budget.phase('generation: initial order and complete discriminant factorization')
    try:
        initial = order(eye(N))
        c['orders'].append(initial)
        c['initial_factorization'] = factor_disc(initial['discriminant'])
        save(c)
        current = 0
        for ps, exponent in c['initial_factorization']['factors'].items():
            if budget.cmp('<', exponent, 2):
                continue
            p, strict = (int(ps), 0)
            budget.phase(budget.op('+', 'generation: saturation at ', str(p)))
            while True:
                s = radical_multiplier(c['orders'][current], p)
                s['order_id'] = current
                c['steps'].append(s)
                if s['terminal']:
                    print('prime', p, 'strict_steps', strict, 'terminal_rank', s['multiplier_kernel']['rank'], flush=True)
                    save(c)
                    break
                budget.charge('strict_enlargements')
                strict = budget.op('+', strict, 1)
                old = c['orders'][current]
                new = order(mm(old['basis'], s['overorder_transform']))
                assert budget.cmp('==', old['discriminant'], budget.op('*', budget.op('**', s['index'], 2), new['discriminant']))
                assert budget.cmp('==', mm(new['inverse'], old['basis']), s['old_in_new'])
                c['orders'].append(new)
                current = budget.op('-', len(c['orders']), 1)
                s['next_order_id'] = current
                save(c)
        c['final_order_id'] = current
        final = c['orders'][current]
        budget.phase('generation: final all-prime maximality and index checks')
        for ps, exponent in c['initial_factorization']['factors'].items():
            if budget.cmp('<', exponent, 2):
                continue
            s = radical_multiplier(final, int(ps))
            s['order_id'] = current
            c['final_checks'].append(s)
            assert s['terminal'] and budget.cmp('==', s['multiplier_kernel']['rank'], N)
            save(c)
        c['initial_in_final'] = ints(mm(final['inverse'], initial['basis']))
        c['total_index'] = abs(ints(determinant(c['initial_in_final'])))
        assert budget.cmp('==', initial['discriminant'], budget.op('*', budget.op('**', c['total_index'], 2), final['discriminant']))
        c['final_factorization'] = factor_disc(final['discriminant'])
        c['completed'] = True
    except Exception:
        detail = traceback.format_exc()
        c['failures'].append(detail)
        budget.failure(detail)
        save(c)
        raise
    save(c)
    print('completed', c['completed'], 'orders', len(c['orders']), 'steps', len(c['steps']))
    print('discriminant', final['discriminant'], 'index', c['total_index'])
    print(json.dumps(budget.summary(), sort_keys=True))
    print('certificate', OUTPUT)
if budget.cmp('==', __name__, '__main__'):
    main()
