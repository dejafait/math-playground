"""Independent exact arithmetic replay; imports no producer implementation.

Rebuild products by shift/reduce, determinants by subset expansion, and
kernel ranks by column-space elimination; also replay every saved row op.
"""
from fractions import Fraction
from pathlib import Path
from hashlib import sha256
from math import isqrt
import json
import traceback
from quartic_order_budget import Budget
budget = Budget()
ROOT = Path(__file__).resolve().parent
SOURCE = budget.op('/', ROOT, 'quartic-order-certificate.json')
OUTPUT = budget.op('/', ROOT, 'quartic-order-verification.json')
CHECKS = []
RECORDS = []
TERMINAL_WITNESSES = []
N = 4
POLY = [budget.op('-', 0, 109375), budget.op('-', 0, 32500), 150, 64, 1]

def decode(x):
    if isinstance(x, list):
        return [decode(v) for v in x]
    if isinstance(x, dict):
        return {k: decode(v) for k, v in x.items()}
    if isinstance(x, str) and budget.cmp('in', '/', x) and all((budget.cmp('in', c, '-0123456789/') for c in x)):
        return budget.rational(x)
    return x

def encode(x):
    if isinstance(x, Fraction):
        return int(x) if x.denominator == 1 else str(x)
    if isinstance(x, list):
        return [encode(v) for v in x]
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    return x

def equal(name, actual, required):
    ok = budget.cmp('==', actual, required)
    CHECKS.append(dict(name=name, actual=actual, required=required, passed=ok))
    assert ok, name

def integral(x):
    if isinstance(x, list):
        return all((integral(v) for v in x))
    return budget.cmp('==', budget.rational(x).denominator, 1)

def identity():
    return [[int(budget.cmp('==', i, j)) for j in range(N)] for i in range(N)]

def product(a, b):
    return [[budget.scalar_sum((budget.op('*', a[i][k], b[k][j]) for k in range(len(b)))) for j in range(len(b[0]))] for i in range(len(a))]

def determinant(a):
    partial = {0: budget.rational(1)}
    n = len(a)
    for row in range(n):
        following = {}
        for mask, value in partial.items():
            for col in range(n):
                if budget.op('&', mask, budget.op('<<', 1, col)):
                    continue
                inversions = budget.scalar_sum((bool(budget.op('&', mask, budget.op('<<', 1, k))) for k in range(budget.op('+', col, 1), n)))
                new = budget.op('|', mask, budget.op('<<', 1, col))
                following[new] = budget.op('+', following.get(new, 0), budget.op('*', budget.op('*', budget.op('**', budget.op('-', 0, 1), inversions), value), a[row][col]))
        partial = following
    return partial[budget.op('-', budget.op('<<', 1, n), 1)]

def field_times(a, b):
    result = budget.op('*', [budget.rational(0)], N)
    for coefficient in reversed(b):
        top = result[budget.op('-', 0, 1)]
        result = budget.op('+', [budget.rational(0)], result[:budget.op('-', 0, 1)])
        result = [budget.op('+', budget.op('-', result[i], budget.op('*', top, budget.rational(POLY[i], POLY[budget.op('-', 0, 1)]))), budget.op('*', coefficient, a[i])) for i in range(N)]
    return result

def order_record(o, number):
    b, inv = (o['basis'], o['inverse'])
    equal(f'order {number} left inverse', product(inv, b), identity())
    equal(f'order {number} right inverse', product(b, inv), identity())
    cols = list(zip(*b))
    rebuilt = []
    for x in cols:
        row = []
        for y in cols:
            z = field_times(x, y)
            row.append([budget.scalar_sum((budget.op('*', r[k], z[k]) for k in range(N))) for r in inv])
        rebuilt.append(row)
    equal(f'order {number} complete multiplication table', rebuilt, o['table'])
    equal(f'order {number} table integral', integral(rebuilt), True)
    one = [r[0] for r in inv]
    equal(f'order {number} one', one, o['one'])
    equal(f'order {number} one integral', integral(one), True)
    traces = [budget.scalar_sum((rebuilt[i][j][j] for j in range(N))) for i in range(N)]
    equal(f'order {number} all traces', traces, o['traces'])
    gram = [[budget.scalar_sum((budget.op('*', traces[k], rebuilt[i][j][k]) for k in range(N))) for j in range(N)] for i in range(N)]
    equal(f'order {number} entire trace Gram matrix', gram, o['gram'])
    equal(f'order {number} discriminant', determinant(gram), o['discriminant'])
    equal(f'order {number} nondegenerate', budget.cmp('!=', o['discriminant'], 0), True)

def mod_product(a, b, table, p):
    out = budget.op('*', [0], N)
    for j in range(N):
        for k in range(N):
            column_entry = budget.scalar_sum((budget.op('*', a[i], table[i][j][k]) for i in range(N)))
            out[k] = budget.op('%', budget.op('+', out[k], budget.op('*', b[j], column_entry)), p)
    return out

def rank_by_columns(a, p):
    basis = {}
    for col in zip(*a):
        v = [budget.op('%', int(x), p) for x in col]
        for pivot in sorted(basis):
            c = v[pivot]
            v = [budget.op('%', budget.op('-', x, budget.op('*', c, y)), p) for x, y in zip(v, basis[pivot])]
        pivot = next((i for i, x in enumerate(v) if x), None)
        if budget.cmp('is not', pivot, None):
            inv = budget.modpow(v[pivot], budget.op('-', 0, 1), p)
            basis[pivot] = [budget.op('%', budget.op('*', x, inv), p) for x in v]
    return (len(basis), basis)

def check_kernel(name, matrix, k, p):
    rows = [[budget.op('%', int(x), p) for x in r] for r in matrix]
    for op in k['operations']:
        if budget.cmp('==', op[0], 'swap'):
            _, i, j = op
            rows[i], rows[j] = (rows[j], rows[i])
        elif budget.cmp('==', op[0], 'scale'):
            _, i, c = op
            assert budget.cmp('<', 0, c) and budget.cmp('<', c, p)
            rows[i] = [budget.op('%', budget.op('*', c, x), p) for x in rows[i]]
        elif budget.cmp('==', op[0], 'add'):
            _, i, j, c = op
            assert budget.cmp('!=', i, j) and (budget.cmp('<=', 0, c) and budget.cmp('<', c, p))
            rows[i] = [budget.op('%', budget.op('+', x, budget.op('*', c, y)), p) for x, y in zip(rows[i], rows[j])]
        else:
            raise AssertionError('unknown row operation')
    equal(budget.op('+', name, ' complete row operation replay'), rows, k['rref'])
    pivots = []
    for r in rows:
        first = next((i for i, x in enumerate(r) if x), None)
        if budget.cmp('is not', first, None):
            pivots.append(first)
    equal(budget.op('+', name, ' pivots'), pivots, k['pivots'])
    equal(budget.op('+', name, ' increasing pivots'), pivots, sorted(set(pivots)))
    equal(budget.op('+', name, ' reduced pivots'), [[rows[i][j] for j in pivots] for i in range(len(pivots))], [[int(budget.cmp('==', i, j)) for j in range(len(pivots))] for i in range(len(pivots))])
    free = [i for i in range(N) if budget.cmp('not in', i, pivots)]
    equal(budget.op('+', name, ' free columns'), free, k['free'])
    rank, column_echelon = rank_by_columns(matrix, p)
    equal(budget.op('+', name, ' independent column rank'), rank, k['rank'])
    equal(budget.op('+', name, ' rank/nullity'), budget.op('+', rank, len(k['vectors'])), N)
    equal(budget.op('+', name, ' nullspace equations'), [[budget.op('%', budget.scalar_sum((budget.op('*', x, y) for x, y in zip(row, v))), p) for row in matrix] for v in k['vectors']], [budget.op('*', [0], len(matrix)) for _ in free])
    equal(budget.op('+', name, ' free-coordinate independence'), [[v[j] for j in free] for v in k['vectors']], [[int(budget.cmp('==', i, j)) for j in range(len(free))] for i in range(len(free))])
    RECORDS.append(dict(name=name, prime=p, independent_rank=rank, column_echelon={str(i): v for i, v in column_echelon.items()}))

def check_preimage(name, lattice, inv, matrix, kern, p):
    equal(budget.op('+', name, ' inverse identity'), product(inv, lattice), identity())
    equal(budget.op('+', name, ' reverse inverse identity'), product(lattice, inv), identity())
    equal(budget.op('+', name, ' lattice integral'), integral(lattice), True)
    equal(budget.op('+', name, ' contains pA'), integral([[budget.op('*', p, x) for x in r] for r in inv]), True)
    equal(budget.op('+', name, ' determinant'), abs(determinant(lattice)), budget.op('**', p, kern['rank']))
    equal(budget.op('+', name, ' reduction lies in kernel'), [[budget.op('%', int(x), p) for x in r] for r in product(matrix, lattice)], [budget.op('*', [0], N) for _ in matrix])

def prime_test(p):
    if budget.cmp('<', p, 2):
        return False
    divisor = 2
    while budget.cmp('<=', budget.op('*', divisor, divisor), p):
        budget.charge('factor_trials')
        if budget.cmp('==', budget.op('%', p, divisor), 0):
            return False
        divisor = budget.op('+', divisor, 1)
    return True

def terminal_witness(s):
    # The full joint action matrix has already been independently rebuilt.
    matrix, p = s['joint_matrix'], s['prime']
    selected = []
    rank = 0
    for i in range(len(matrix)):
        trial = selected + [i]  # list bookkeeping, not scalar arithmetic
        transposed = [[matrix[j][k] for j in trial] for k in range(N)]
        new_rank, _ = rank_by_columns(transposed, p)
        if budget.cmp('>', new_rank, rank):
            selected = trial
            rank = new_rank
        if budget.cmp('==', rank, N):
            break
    minor = [matrix[i] for i in selected]
    residue = budget.op('%', determinant(minor), p)
    equal('terminal witness rank '+str(p), rank, N)
    equal('terminal witness determinant '+str(p), budget.cmp('!=', residue, 0), True)
    TERMINAL_WITNESSES.append(dict(prime=p, exponent=s['frobenius_exponent'],
        frobenius=s['frobenius_matrix'], radical_kernel=s['nilpotent_kernel']['vectors'],
        radical_basis=s['radical_basis'], minor_rows=selected, minor=minor,
        determinant_mod_p=residue))

def step_record(s, orders, name):
    p = s['prime']
    equal(budget.op('+', name, ' prime'), prime_test(p), True)
    o = orders[s['order_id']]
    q, frobcols = (p, [])
    while budget.cmp('<=', q, N):
        q = budget.op('*', q, p)
    equal(budget.op('+', name, ' least Frobenius exponent'), q, s['frobenius_exponent'])
    for j in range(N):
        v = [int(budget.cmp('==', i, j)) for i in range(N)]
        r = [budget.op('%', x, p) for x in o['one']]
        for _ in range(q):
            r = mod_product(r, v, o['table'], p)
        frobcols.append(r)
    frob = [list(r) for r in zip(*frobcols)]
    equal(budget.op('+', name, ' entire Frobenius matrix'), frob, s['frobenius_matrix'])
    check_kernel(budget.op('+', name, ' nilpotent'), frob, s['nilpotent_kernel'], p)
    j, ji = (s['radical_basis'], s['radical_inverse'])
    check_preimage(budget.op('+', name, ' radical'), j, ji, frob, s['nilpotent_kernel'], p)
    action = []
    for i in range(N):
        mi = [list(r) for r in zip(*o['table'][i])]
        action.append(product(product(ji, mi), j))
    equal(budget.op('+', name, ' complete actions on I'), action, s['action_matrices'])
    equal(budget.op('+', name, ' action integrality'), integral(action), True)
    joint = [[budget.op('%', int(action[k][i][j]), p) for k in range(N)] for i in range(N) for j in range(N)]
    equal(budget.op('+', name, ' full joint action matrix'), joint, s['joint_matrix'])
    check_kernel(budget.op('+', name, ' multiplier'), joint, s['multiplier_kernel'], p)
    e, ei = (s['overorder_transform'], s['overorder_inverse'])
    pe = [[budget.op('*', p, x) for x in r] for r in e]
    pei = [[budget.rational(x, p) for x in r] for r in ei]
    check_preimage(budget.op('+', name, ' pM'), pe, pei, joint, s['multiplier_kernel'], p)
    equal(budget.op('+', name, ' old order containment'), integral(ei), True)
    equal(budget.op('+', name, ' saved old-in-new matrix'), ei, s['old_in_new'])
    equal(budget.op('+', name, ' exact multiplier index'), abs(determinant(ei)), s['index'])
    equal(budget.op('+', name, ' index from nullity'), s['index'], budget.op('**', p, len(s['multiplier_kernel']['free'])))
    ma = []
    for v in zip(*e):
        ma.append([[budget.scalar_sum((budget.op('*', v[k], action[k][i][j]) for k in range(N))) for j in range(N)] for i in range(N)])
    equal(budget.op('+', name, ' multiplier preserves I exactly'), integral(ma), True)
    equal(budget.op('+', name, ' all saved multiplier actions'), ma, s['multiplier_actions'])
    equal(budget.op('+', name, ' terminal equivalence'), s['terminal'], budget.cmp('==', s['index'], 1))
    if not s['terminal']:
        new = orders[s['next_order_id']]
        equal(budget.op('+', name, ' basis transport'), product(o['basis'], e), new['basis'])
        equal(budget.op('+', name, ' reverse basis transport'), product(new['basis'], ei), o['basis'])
        equal(budget.op('+', name, ' discriminant-index identity'), o['discriminant'], budget.op('*', budget.op('**', s['index'], 2), new['discriminant']))

def factorization_record(name, value, record):
    equal(budget.op('+', name, ' input'), record['value'], value)
    remaining = abs(value)
    factors = {}
    expected = 2
    for row in record['trial_chain']:
        budget.charge('factor_trials')
        p = row['divisor']
        equal(budget.op('+', budget.op('+', name, ' no skipped trial '), str(p)), p, expected)
        equal(budget.op('+', budget.op('+', name, ' trial necessary '), str(p)), budget.cmp('<=', budget.op('*', p, p), remaining), True)
        equal(budget.op('+', budget.op('+', name, ' prior remainder '), str(p)), row['before'], remaining)
        chain = [remaining]
        while budget.cmp('==', budget.op('%', remaining, p), 0):
            remaining = budget.op('//', remaining, p)
            chain.append(remaining)
        equal(budget.op('+', budget.op('+', name, ' complete division chain '), str(p)), chain, row['chain'])
        if budget.cmp('>', len(chain), 1):
            factors[str(p)] = budget.op('-', len(chain), 1)
        expected = budget.op('+', expected, 1)
    equal(budget.op('+', name, ' next untested divisor'), record['next_divisor'], expected)
    equal(budget.op('+', name, ' terminal residual'), record['residual'], remaining)
    equal(budget.op('+', name, ' termination justified'), budget.cmp('>', budget.op('*', expected, expected), remaining), True)
    if budget.cmp('>', remaining, 1):
        factors[str(remaining)] = 1
    equal(budget.op('+', name, ' full factor dictionary'), sorted(factors.items()), sorted(record['factors'].items()))
    reconstructed = 1
    for ps, exponent in factors.items():
        p = int(ps)
        equal(budget.op('+', budget.op('+', name, ' positive prime '), ps), budget.cmp('>=', p, 2), True)
        divisor = 2
        while budget.cmp('<=', budget.op('*', divisor, divisor), p):
            budget.charge('factor_trials')
            equal(budget.op('+', budget.op('+', budget.op('+', budget.op('+', name, ' primality '), ps), ' divisor '), str(divisor)), budget.cmp('!=', budget.op('%', p, divisor), 0), True)
            divisor = budget.op('+', divisor, 1)
        reconstructed = budget.op('*', reconstructed, budget.op('**', p, exponent))
    equal(budget.op('+', name, ' product identity'), reconstructed, abs(value))

def main():
    budget.phase('independent replay: field products, full lattices, kernels, factors')
    raw = SOURCE.read_bytes()
    c = decode(json.loads(raw))
    failure = []
    summary = {}
    try:
        equal('input polynomial', c['polynomial'], POLY)
        equal('dimension', c['dimension'], N)
        equal('completed producer', c['completed'], True)
        equal('producer failures', c['failures'], [])
        orders = c['orders']
        equal('complete power-order starting basis', orders[0]['basis'], identity())
        for i, o in enumerate(orders):
            order_record(o, i)
        initial = orders[0]['discriminant']
        factorization_record('initial', initial, c['initial_factorization'])
        expected_primes = [int(p) for p, e in c['initial_factorization']['factors'].items() if budget.cmp('>=', e, 2)]
        current, visited, strict_counts, strict_product, total_strict = (0, [], {}, 1, 0)
        for i, s in enumerate(c['steps']):
            p = s['prime']
            if not visited or budget.cmp('!=', visited[budget.op('-', 0, 1)], p):
                if visited:
                    equal(budget.op('+', 'previous prime terminal ', str(i)), c['steps'][budget.op('-', i, 1)]['terminal'], True)
                visited.append(p)
                strict_counts[p] = 0
            equal(budget.op('+', budget.op('+', 'step ', str(i)), ' linked input order'), s['order_id'], current)
            step_record(s, orders, budget.op('+', 'step ', str(i)))
            if not s['terminal']:
                strict_counts[p] = budget.op('+', strict_counts[p], 1)
                total_strict = budget.op('+', total_strict, 1)
                strict_product = budget.op('*', strict_product, s['index'])
                equal(budget.op('+', budget.op('+', 'step ', str(i)), ' next order consecutive'), s['next_order_id'], budget.op('+', current, 1))
                current = s['next_order_id']
        equal('all and only index primes', visited, expected_primes)
        equal('last sequential prime terminal', c['steps'][budget.op('-', 0, 1)]['terminal'], True)
        equal('all order records used', len(orders), budget.op('+', total_strict, 1))
        equal('final order link', c['final_order_id'], current)
        equal('all final primes', [s['prime'] for s in c['final_checks']], expected_primes)
        for s in c['final_checks']:
            equal(budget.op('+', budget.op('+', 'final prime ', str(s['prime'])), ' uses final basis'), s['order_id'], current)
            step_record(s, orders, budget.op('+', 'final prime ', str(s['prime'])))
            terminal_witness(s)
            equal(budget.op('+', budget.op('+', 'final prime ', str(s['prime'])), ' rank'), s['multiplier_kernel']['rank'], N)
            equal(budget.op('+', budget.op('+', 'final prime ', str(s['prime'])), ' stable'), s['terminal'], True)
        final = orders[current]
        inc = product(final['inverse'], orders[0]['basis'])
        equal('initial in final lattice', inc, c['initial_in_final'])
        equal('initial in final integral', integral(inc), True)
        equal('total index determinant', abs(determinant(inc)), c['total_index'])
        equal('total index strict product', strict_product, c['total_index'])
        equal('final discriminant/index', initial, budget.op('*', budget.op('**', c['total_index'], 2), final['discriminant']))
        equal('basis determinant/index', budget.op('*', abs(determinant(final['basis'])), c['total_index']), 1)
        factorization_record('final', final['discriminant'], c['final_factorization'])
        summary = dict(orders_checked=len(orders), strict_steps=total_strict, strict_by_prime={str(p): k for p, k in strict_counts.items()}, sequential_checks=len(c['steps']), final_checks=len(c['final_checks']), final_multiplier_ranks=[s['multiplier_kernel']['rank'] for s in c['final_checks']], required_final_rank=N, total_index=c['total_index'], field_discriminant=final['discriminant'], factorization=c['final_factorization']['factors'])
    except Exception:
        detail = traceback.format_exc()
        failure.append(detail)
        budget.failure(detail)
    out = dict(method='Independent Horner products, subset determinants, column ranks and complete row-operation replay; accounting-only shared import', producer_sha256=sha256(raw).hexdigest(), summary=summary, checks=CHECKS, independent_kernel_records=RECORDS, terminal_witnesses=TERMINAL_WITNESSES, failures=failure, passed=not failure and all((r['passed'] for r in CHECKS)))
    OUTPUT.write_text(budget.op('+', json.dumps(encode(out), indent=2), '\n'))
    budget.save()
    print('passed', out['passed'], 'checks', len(CHECKS), 'failures', len(failure))
    print('summary', summary)
    print(json.dumps(budget.summary(), sort_keys=True))
    print('replay', OUTPUT)
    if failure:
        print(failure[0])
        raise SystemExit(1)
if budget.cmp('==', __name__, '__main__'):
    main()
