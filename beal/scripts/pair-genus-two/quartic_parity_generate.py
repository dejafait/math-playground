"""Fixed approved box; exact ideal products with two-way span witnesses."""
import json
from pathlib import Path
from hashlib import sha256
from itertools import product, permutations
from quartic_parity_budget import run

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'quartic-parity-certificate.json'
DATA = dict(completed=False, failures=[], lattices=[], elements=[])

def save():
    OUT.write_text(json.dumps(DATA, separators=(',', ':')) + '\n')

def unit(i, n=4):
    return [int(j == i) for j in range(n)]

def times(a, c):
    pairs = [(i, j, x * y) for i, x in enumerate(a) if x
             for j, y in enumerate(c) if y]
    return [sum(z * TABLE[i][j][k] for i, j, z in pairs) for k in range(4)]

def determinant(rows):
    result = 0
    for perm in permutations(range(4)):
        inversions = sum(int(perm[i] > perm[j]) for i in range(4) for j in range(i + 1, 4))
        term = 1
        for i in range(4):
            term = term * rows[i][perm[i]]
        result = result + (-term if inversions % 2 else term)
    return result

def coordinates(h, v):
    residual, answer, divisions = list(v), [], []
    for i in range(4):
        q, r = residual[i] // h[i][i], residual[i] % h[i][i]
        divisions.append([residual[i], h[i][i], q, r])
        if r:
            return dict(member=False, divisions=divisions)
        answer.append(q)
        residual = [x - q * y for x, y in zip(residual, h[i])]
    assert not any(residual)
    return dict(member=True, divisions=divisions, coordinates=answer)

def reduce_lattice(gens):
    rows = [list(v) for v in gens]
    n = len(rows)
    transform = [unit(i, n) for i in range(n)]
    for j in range(4):
        pivot = next(i for i in range(j, n) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        transform[j], transform[pivot] = transform[pivot], transform[j]
        for i in range(j + 1, n):
            while rows[i][j]:
                q = rows[j][j] // rows[i][j]
                rows[j] = [x - q * y for x, y in zip(rows[j], rows[i])]
                transform[j] = [x - q * y for x, y in zip(transform[j], transform[i])]
                rows[j], rows[i] = rows[i], rows[j]
                transform[j], transform[i] = transform[i], transform[j]
        if rows[j][j] < 0:
            rows[j] = [-x for x in rows[j]]
            transform[j] = [-x for x in transform[j]]
        for i in range(j):
            q = rows[i][j] // rows[j][j]
            rows[i] = [x - q * y for x, y in zip(rows[i], rows[j])]
            transform[i] = [x - q * y for x, y in zip(transform[i], transform[j])]
    assert not any(any(v) for v in rows[4:])
    h = rows[:4]
    backward = [coordinates(h, v) for v in gens]
    assert all(w['member'] for w in backward)
    return dict(rows=h, forward=transform[:4], backward=backward,
                norm=abs(determinant(h)))

def add_lattice(gens, origin, norm):
    record = reduce_lattice(gens)
    assert record['norm'] == norm
    record['origin'] = origin
    i = len(DATA['lattices'])
    DATA['lattices'].append(record)
    return i

def ideal_product(left, right):
    key = (left, right)
    if key not in PRODUCTS:
        a, c = DATA['lattices'][left], DATA['lattices'][right]
        gens = [times(v, w) for v in a['rows'] for w in c['rows']]
        PRODUCTS[key] = add_lattice(gens, dict(product=[left, right]), a['norm'] * c['norm'])
    return PRODUCTS[key]

def power(prime, exponent):
    while len(POWERS[prime]) <= exponent:
        POWERS[prime].append(ideal_product(POWERS[prime][-1], POWERS[prime][1]))
    return POWERS[prime][exponent]

def main():
    global TABLE, PRODUCTS, POWERS
    source = (ROOT / 'quartic-class-certificate.json').read_bytes()
    old = json.loads(source)
    assert sha256(source).hexdigest() == 'c5363d1b846188e37fc53590b61de34923bb981da25ddd895cd82e14dda9b73b'
    assert old['completed'] and old['failures'] == []
    TABLE = old['order']['table']
    primes = old['generators']
    assert len(primes) == 32 and all(P['p'] == P['lattice']['norm'] for P in primes)
    DATA.update(input_sha256=sha256(source).hexdigest(), table=TABLE,
                primes=primes, box=[-2, 2], excluded=[0, 0, 0, 0])
    PRODUCTS = {}
    identity = add_lattice([unit(i) for i in range(4)], dict(identity=True), 1)
    POWERS = [[identity, add_lattice(P['lattice']['columns'], dict(prime=i), P['p'])]
              for i, P in enumerate(primes)]
    rational_primes = sorted(set(P['p'] for P in primes))
    rows, accepted_ids = [], []
    b.phase('producer: exact complete coefficient box')
    save()
    for tuple_id, a in enumerate(product(range(-2, 3), repeat=4)):
        if not any(a):
            continue
        principal = [times(a, unit(i)) for i in range(4)]
        n = abs(determinant(principal))
        assert n > 0
        entry = dict(tuple_id=tuple_id, coefficients=a, principal=principal, norm=n)
        remainder, division_record = n, []
        for p in rational_primes:
            while True:
                q, r = remainder // p, remainder % p
                division_record.append([p, remainder, q, r])
                if r:
                    break
                remainder = q
        entry.update(smooth_divisions=division_record, residual=remainder)
        if remainder > 1:
            entry['decision'] = 'rational_cofactor'
            DATA['elements'].append(entry)
            continue
        valuations, witnesses = [], []
        for i in range(32):
            e, tests = 0, []
            while True:
                lattice_id = power(i, e + 1)
                b.charge('membership_tests')
                w = coordinates(DATA['lattices'][lattice_id]['rows'], a)
                tests.append(dict(lattice=lattice_id, witness=w))
                if not w['member']:
                    break
                e = e + 1
                assert 2 ** e <= n
            valuations.append(e)
            witnesses.append(tests)
        supported_norm = 1
        for P, e in zip(primes, valuations):
            supported_norm = supported_norm * P['p'] ** e
        assert n % supported_norm == 0
        entry.update(valuations=valuations, membership=witnesses, supported_norm=supported_norm)
        if supported_norm != n:
            entry['decision'] = 'omitted_prime'
        else:
            ideal = identity
            for i, e in enumerate(valuations):
                if e:
                    ideal = ideal_product(ideal, power(i, e))
            containment = [coordinates(DATA['lattices'][ideal]['rows'], v) for v in principal]
            assert all(w['member'] for w in containment)
            assert DATA['lattices'][ideal]['norm'] == n
            entry.update(decision='accepted', product_lattice=ideal, principal_containment=containment)
            mask = sum((e % 2) << i for i, e in enumerate(valuations))
            rows.append(mask)
            accepted_ids.append(tuple_id)
        DATA['elements'].append(entry)
        if len(DATA['elements']) % 32 == 0:
            save()
    b.phase('producer: parity elimination')
    pivots, operations = {}, []
    for row_id, mask in enumerate(rows):
        current, used = mask, []
        for col in sorted(pivots):
            if (current >> col) & 1:
                current = current ^ pivots[col]['mask']
                used.append(pivots[col]['row'])
        pivot = next((i for i in range(32) if (current >> i) & 1), None)
        if pivot is not None:
            pivots[pivot] = dict(mask=current, row=row_id)
        operations.append(dict(input=mask, subtract=used, output=current, pivot=pivot))
    DATA.update(completed=True, accepted_ids=accepted_ids, parity_rows=rows,
                elimination=operations, pivot_columns=sorted(pivots), rank=len(pivots),
                counts={d: sum(int(e['decision'] == d) for e in DATA['elements'])
                        for d in ('accepted', 'rational_cofactor', 'omitted_prime')}, budget=b.summary())
    assert len(DATA['elements']) == 624
    save()
    print(json.dumps(dict(completed=True, rank=DATA['rank'], required_rank=32,
                         counts=DATA['counts'], lattices=len(DATA['lattices']),
                         budget=b.summary(), certificate=str(OUT))))

if __name__ == '__main__':
    if not globals().get('__instrumented__'):
        run(__file__)
    else:
        try:
            main()
        except Exception as exc:
            DATA['failures'].append(repr(exc))
            save()
            raise
