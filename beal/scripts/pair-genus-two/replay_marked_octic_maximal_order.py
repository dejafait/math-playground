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

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'marked-octic-maximal-order-certificate.json'
OUTPUT = ROOT / 'marked-octic-maximal-order-replay.json'
CHECKS = []
RECORDS = []
N = 8
POLY = [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]


def decode(x):
    if isinstance(x, list):
        return [decode(v) for v in x]
    if isinstance(x, dict):
        return {k: decode(v) for k, v in x.items()}
    if isinstance(x, str) and '/' in x and all(c in '-0123456789/' for c in x):
        return Fraction(x)
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
    ok = actual == required
    CHECKS.append(dict(name=name, actual=actual, required=required, passed=ok))
    assert ok, name


def integral(x):
    if isinstance(x, list):
        return all(integral(v) for v in x)
    return Fraction(x).denominator == 1


def identity():
    return [[int(i == j) for j in range(N)] for i in range(N)]


def product(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def determinant(a):
    # Laplace expansion along successive rows, caching all selected-column
    # subsets: no producer pivot or fraction-free recurrence is used.
    partial = {0: Fraction(1)}
    n = len(a)
    for row in range(n):
        following = {}
        for mask, value in partial.items():
            for col in range(n):
                if mask & (1 << col):
                    continue
                inversions = sum(bool(mask & (1 << k)) for k in range(col+1, n))
                new = mask | (1 << col)
                following[new] = following.get(new, 0) + (-1)**inversions*value*a[row][col]
        partial = following
    return partial[(1 << n)-1]


def field_times(a, b):
    # Horner in the second operand. Multiplication by t is one companion
    # shift with reduction of the top term, unlike producer convolution.
    result = [Fraction(0)]*N
    for coefficient in reversed(b):
        top = result[-1]
        result = [Fraction(0)]+result[:-1]
        result = [result[i]-top*Fraction(POLY[i], POLY[-1])+coefficient*a[i]
                  for i in range(N)]
    return result


def order_record(o, number):
    b, inv = o['basis'], o['inverse']
    equal(f'order {number} left inverse', product(inv, b), identity())
    equal(f'order {number} right inverse', product(b, inv), identity())
    cols = list(zip(*b))
    rebuilt = []
    for x in cols:
        row = []
        for y in cols:
            z = field_times(x, y)
            row.append([sum(r[k]*z[k] for k in range(N)) for r in inv])
        rebuilt.append(row)
    equal(f'order {number} complete multiplication table', rebuilt, o['table'])
    equal(f'order {number} table integral', integral(rebuilt), True)
    one = [r[0] for r in inv]
    equal(f'order {number} one', one, o['one'])
    equal(f'order {number} one integral', integral(one), True)
    traces = [sum(rebuilt[i][j][j] for j in range(N)) for i in range(N)]
    equal(f'order {number} all traces', traces, o['traces'])
    gram = [[sum(traces[k]*rebuilt[i][j][k] for k in range(N))
             for j in range(N)] for i in range(N)]
    equal(f'order {number} entire trace Gram matrix', gram, o['gram'])
    equal(f'order {number} discriminant', determinant(gram), o['discriminant'])
    equal(f'order {number} nondegenerate', o['discriminant'] != 0, True)


def mod_product(a, b, table, p):
    # Linear combination of multiplication-matrix columns.
    out = [0]*N
    for j in range(N):
        for k in range(N):
            column_entry = sum(a[i]*table[i][j][k] for i in range(N))
            out[k] = (out[k]+b[j]*column_entry) % p
    return out


def rank_by_columns(a, p):
    # Incremental column-space reduction, retaining the complete echelon
    # vectors. Independent of the producer's row-reduction implementation.
    basis = {}
    for col in zip(*a):
        v = [int(x) % p for x in col]
        for pivot in sorted(basis):
            c = v[pivot]
            v = [(x-c*y) % p for x, y in zip(v, basis[pivot])]
        pivot = next((i for i, x in enumerate(v) if x), None)
        if pivot is not None:
            inv = pow(v[pivot], -1, p)
            basis[pivot] = [x*inv % p for x in v]
    return len(basis), basis


def check_kernel(name, matrix, k, p):
    rows = [[int(x) % p for x in r] for r in matrix]
    for op in k['operations']:
        if op[0] == 'swap':
            _, i, j = op
            rows[i], rows[j] = rows[j], rows[i]
        elif op[0] == 'scale':
            _, i, c = op
            assert 0 < c < p
            rows[i] = [c*x % p for x in rows[i]]
        elif op[0] == 'add':
            _, i, j, c = op
            assert i != j and 0 <= c < p
            rows[i] = [(x+c*y) % p for x, y in zip(rows[i], rows[j])]
        else:
            raise AssertionError('unknown row operation')
    equal(name+' complete row operation replay', rows, k['rref'])
    pivots = []
    for r in rows:
        first = next((i for i, x in enumerate(r) if x), None)
        if first is not None:
            pivots.append(first)
    equal(name+' pivots', pivots, k['pivots'])
    equal(name+' increasing pivots', pivots, sorted(set(pivots)))
    equal(name+' reduced pivots', [[rows[i][j] for j in pivots] for i in range(len(pivots))],
          [[int(i == j) for j in range(len(pivots))] for i in range(len(pivots))])
    free = [i for i in range(N) if i not in pivots]
    equal(name+' free columns', free, k['free'])
    rank, column_echelon = rank_by_columns(matrix, p)
    equal(name+' independent column rank', rank, k['rank'])
    equal(name+' rank/nullity', rank+len(k['vectors']), N)
    equal(name+' nullspace equations',
          [[sum(x*y for x, y in zip(row, v)) % p for row in matrix] for v in k['vectors']],
          [[0]*len(matrix) for _ in free])
    equal(name+' free-coordinate independence', [[v[j] for j in free] for v in k['vectors']],
          [[int(i == j) for j in range(len(free))] for i in range(len(free))])
    RECORDS.append(dict(name=name, prime=p, independent_rank=rank,
                        column_echelon={str(i): v for i, v in column_echelon.items()}))


def check_preimage(name, lattice, inv, matrix, kern, p):
    equal(name+' inverse identity', product(inv, lattice), identity())
    equal(name+' reverse inverse identity', product(lattice, inv), identity())
    equal(name+' lattice integral', integral(lattice), True)
    equal(name+' contains pA', integral([[p*x for x in r] for r in inv]), True)
    equal(name+' determinant', abs(determinant(lattice)), p**kern['rank'])
    # Complete kernel dimension and pA containment make determinant equality
    # plus this inclusion a two-way lattice equality, not just containment.
    equal(name+' reduction lies in kernel',
          [[int(x) % p for x in r] for r in product(matrix, lattice)],
          [[0]*N for _ in matrix])


def step_record(s, orders, name):
    p = s['prime']
    equal(name+' prime', p >= 2 and all(p % d for d in range(2, isqrt(p)+1)), True)
    o = orders[s['order_id']]
    q, frobcols = p, []
    while q < N:
        q *= p
    equal(name+' least Frobenius exponent', q, s['frobenius_exponent'])
    for j in range(N):
        v = [int(i == j) for i in range(N)]
        r = [x % p for x in o['one']]
        # q ordinary successive multiplications, independent of binary powering.
        for _ in range(q):
            r = mod_product(r, v, o['table'], p)
        frobcols.append(r)
    frob = [list(r) for r in zip(*frobcols)]
    equal(name+' entire Frobenius matrix', frob, s['frobenius_matrix'])
    check_kernel(name+' nilpotent', frob, s['nilpotent_kernel'], p)
    j, ji = s['radical_basis'], s['radical_inverse']
    check_preimage(name+' radical', j, ji, frob, s['nilpotent_kernel'], p)
    action = []
    for i in range(N):
        mi = [list(r) for r in zip(*o['table'][i])]
        action.append(product(product(ji, mi), j))
    equal(name+' complete actions on I', action, s['action_matrices'])
    equal(name+' action integrality', integral(action), True)
    joint = [[int(action[k][i][j]) % p for k in range(N)] for i in range(N) for j in range(N)]
    equal(name+' full joint action matrix', joint, s['joint_matrix'])
    check_kernel(name+' multiplier', joint, s['multiplier_kernel'], p)
    e, ei = s['overorder_transform'], s['overorder_inverse']
    pe = [[p*x for x in r] for r in e]
    pei = [[Fraction(x, p) for x in r] for r in ei]
    check_preimage(name+' pM', pe, pei, joint, s['multiplier_kernel'], p)
    equal(name+' old order containment', integral(ei), True)
    equal(name+' saved old-in-new matrix', ei, s['old_in_new'])
    equal(name+' exact multiplier index', abs(determinant(ei)), s['index'])
    equal(name+' index from nullity', s['index'], p**len(s['multiplier_kernel']['free']))
    ma = []
    for v in zip(*e):
        ma.append([[sum(v[k]*action[k][i][j] for k in range(N))
                    for j in range(N)] for i in range(N)])
    equal(name+' multiplier preserves I exactly', integral(ma), True)
    equal(name+' all saved multiplier actions', ma, s['multiplier_actions'])
    equal(name+' terminal equivalence', s['terminal'], s['index'] == 1)
    if not s['terminal']:
        new = orders[s['next_order_id']]
        equal(name+' basis transport', product(o['basis'], e), new['basis'])
        equal(name+' reverse basis transport', product(new['basis'], ei), o['basis'])
        equal(name+' discriminant-index identity', o['discriminant'], s['index']**2*new['discriminant'])


def factorization_record(name, value, factors, divisions):
    remaining = abs(value)
    primes = []
    for row in divisions:
        p = row['prime']
        equal(name+f' primality {p}', p >= 2 and all(p % d for d in range(2, isqrt(p)+1)), True)
        chain = [remaining]
        while remaining % p == 0:
            remaining //= p
            chain.append(remaining)
        equal(name+f' complete division chain {p}', chain, row['chain'])
        equal(name+f' exponent {p}', len(chain)-1, row['exponent'])
        equal(name+f' factorization dictionary {p}', row['exponent'], factors[str(p)])
        primes.append(p)
    equal(name+' distinct prime list', primes, sorted(set(map(int, factors))))
    equal(name+' residual cofactor', remaining, 1)


def main():
    raw = SOURCE.read_bytes()
    c = decode(json.loads(raw))
    failure = []
    try:
        equal('input polynomial', c['polynomial'], POLY)
        equal('dimension', c['dimension'], N)
        equal('completed producer', c['completed'], True)
        equal('producer failures', c['failures'], [])
        orders = c['orders']
        # Reconstruct the named nonmonic order directly, no claimed label.
        start = identity()
        for j in range(1, N):
            for i in range(N):
                start[i][j] = POLY[N-j+i] if i <= j else 0
        equal('complete nonmonic starting basis', orders[0]['basis'], start)
        for i, o in enumerate(orders):
            order_record(o, i)
        initial = orders[0]['discriminant']
        equal('starting polynomial discriminant', initial, 2**72*3**27*5**8*11**7)
        equal('G scalar discriminant crosscheck', initial*11**14, 2**72*3**27*5**8*11**21)
        equal('saved polynomial crosscheck', c['polynomial_discriminant_crosscheck'], initial)
        factorization_record('initial', initial, c['initial_factorization'], c['initial_divisions'])
        expected_primes = [int(p) for p, e in c['initial_factorization'].items() if e >= 2]
        current, visited, strict_counts, strict_product, total_strict = 0, [], {}, 1, 0
        for i, s in enumerate(c['steps']):
            p = s['prime']
            if not visited or visited[-1] != p:
                if visited:
                    equal('previous prime terminal', c['steps'][i-1]['terminal'], True)
                visited.append(p)
                strict_counts[p] = 0
            equal(f'step {i} linked input order', s['order_id'], current)
            cap = c['initial_factorization'][str(p)]//2
            equal(f'step {i} source strict cap', s['strict_cap'], cap)
            step_record(s, orders, f'step {i}')
            if not s['terminal']:
                strict_counts[p] += 1
                total_strict += 1
                strict_product *= s['index']
                equal(f'step {i} next order consecutive', s['next_order_id'], current+1)
                current = s['next_order_id']
                equal(f'step {i} cap respected', strict_counts[p] <= cap, True)
        equal('all and only index primes', visited, expected_primes)
        equal('last sequential prime terminal', c['steps'][-1]['terminal'], True)
        equal('all order records used', len(orders), total_strict+1)
        equal('final order link', c['final_order_id'], current)
        equal('all final primes', [s['prime'] for s in c['final_checks']], expected_primes)
        for s in c['final_checks']:
            equal(f'final prime {s["prime"]} uses final basis', s['order_id'], current)
            step_record(s, orders, f'final prime {s["prime"]}')
            equal(f'final prime {s["prime"]} rank', s['multiplier_kernel']['rank'], N)
            equal(f'final prime {s["prime"]} stable', s['terminal'], True)
        final = orders[current]
        inc = product(final['inverse'], orders[0]['basis'])
        equal('initial in final lattice', inc, c['initial_in_final'])
        equal('initial in final integral', integral(inc), True)
        equal('total index determinant', abs(determinant(inc)), c['total_index'])
        equal('total index strict product', strict_product, c['total_index'])
        equal('final discriminant/index', initial, c['total_index']**2*final['discriminant'])
        factorization_record('final', final['discriminant'], c['final_factorization'], c['final_divisions'])
        summary = dict(orders_checked=len(orders), strict_steps=total_strict,
                       strict_by_prime={str(p): k for p, k in strict_counts.items()},
                       sequential_checks=len(c['steps']), final_checks=len(c['final_checks']),
                       final_multiplier_ranks=[s['multiplier_kernel']['rank'] for s in c['final_checks']],
                       required_final_rank=N, total_index=c['total_index'],
                       field_discriminant=final['discriminant'], factorization=c['final_factorization'])
    except Exception:
        failure.append(traceback.format_exc())
        summary = {}
    out = dict(method='Independent shift/reduce products, subset determinants, column ranks and full row-operation replay; no producer imports',
               producer_sha256=sha256(raw).hexdigest(), summary=summary, checks=CHECKS,
               independent_kernel_records=RECORDS, failures=failure,
               passed=not failure and all(r['passed'] for r in CHECKS))
    OUTPUT.write_text(json.dumps(encode(out), indent=2)+'\n')
    print('passed', out['passed'], 'checks', len(CHECKS), 'failures', len(failure))
    print('summary', summary)
    print('replay', OUTPUT)
    if failure:
        print(failure[0])
        raise SystemExit(1)


if __name__ == '__main__':
    main()
