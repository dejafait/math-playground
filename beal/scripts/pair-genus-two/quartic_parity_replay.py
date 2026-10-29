"""Complete independent replay; imports only accounting, no producer math.

Rebuild the order table by companion Horner arithmetic, determinants by
fraction-free elimination, membership by rational triangular solving,
and parity rank by descending-pivot elimination. Verify the producer's
division and two-way lattice-span witnesses as additional exact identities.
"""
import json
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
from quartic_parity_budget import run

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'quartic-parity-verification.json'
RESULT = dict(completed=False, failures=[], checks=0, lattices=[], elements=[])

def check(ok, name):
    RESULT['checks'] = RESULT['checks'] + 1
    if not ok:
        raise AssertionError(name)

def save():
    OUT.write_text(json.dumps(RESULT, separators=(',', ':')) + '\n')

def unit(i, n=4):
    return [int(j == i) for j in range(n)]

def combination(coefficients, rows):
    check(len(coefficients) == len(rows), 'combination dimensions')
    return [sum(c * row[j] for c, row in zip(coefficients, rows)) for j in range(4)]

def determinant(rows):
    a = [list(row) for row in rows]
    sign, previous = 1, 1
    for k in range(3):
        pivot = next((i for i in range(k, 4) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        value = a[k][k]
        for i in range(k + 1, 4):
            for j in range(k + 1, 4):
                numerator = value * a[i][j] - a[i][k] * a[k][j]
                check(numerator % previous == 0, 'Bareiss exact division')
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = value
    return sign * a[3][3]

def field_product(x, y):
    # Only for reconstructing the sixteen basis products from g.
    z = [Q(0)] * 4
    for coefficient in reversed(y):
        top = z[3]
        z = [Q(0)] + z[:3]
        z = [z[k] - top * POLY[k] + coefficient * x[k] for k in range(4)]
    return z

def multiply(x, y):
    # Matrix action, distinct from producer's sparse pair list.
    action = [[sum(x[i] * TABLE[i][j][k] for i in range(4))
               for j in range(4)] for k in range(4)]
    return [sum(action[k][j] * y[j] for j in range(4)) for k in range(4)]

def witness(h, v, saved, prime_power=False):
    if prime_power:
        b.charge('membership_tests')
    # Unique rational coordinates exist, even after an initial divisibility
    # failure. Integrality of all coordinates is the independent decision.
    rational = []
    for i in range(4):
        rational.append((Q(v[i]) - sum(rational[j] * h[j][i] for j in range(i))) / h[i][i])
    member = all(c.denominator == 1 for c in rational)
    check(saved['member'] == member, 'rational membership decision')
    divisions, integer = saved['divisions'], []
    check(1 <= len(divisions) <= 4, 'division witness domain')
    for i, record in enumerate(divisions):
        check(len(record) == 4, 'division tuple dimension')
        numerator, divisor, q, r = record
        expected = v[i] - sum(integer[j] * h[j][i] for j in range(i))
        check(numerator == expected and divisor == h[i][i], 'division input')
        check(numerator == divisor * q + r and 0 <= r < divisor, 'Euclidean division identity')
        if r:
            check(i == len(divisions) - 1 and not member, 'first failed division is terminal')
        else:
            integer.append(q)
    if member:
        check(len(integer) == 4 and len(divisions) == 4, 'complete member witness')
        check(saved['coordinates'] == integer and integer == rational, 'all membership coordinates')
        check(combination(integer, h) == v, 'integral reconstruction')
    else:
        check(divisions[-1][3] != 0 and 'coordinates' not in saved, 'nonmembership witness')
    return member

def main():
    global POLY, TABLE
    source = (ROOT / 'quartic-parity-certificate.json').read_bytes()
    data = json.loads(source)
    base_payload = (ROOT / 'quartic-class-certificate.json').read_bytes()
    base = json.loads(base_payload)
    RESULT['certificate_sha256'] = sha256(source).hexdigest()
    RESULT['input_sha256'] = sha256(base_payload).hexdigest()
    check(RESULT['input_sha256'] == 'c5363d1b846188e37fc53590b61de34923bb981da25ddd895cd82e14dda9b73b', 'audited L135 input')
    check(data['input_sha256'] == RESULT['input_sha256'], 'producer input binding')
    check(data['completed'] and data['failures'] == [], 'producer complete without failure')
    check(base['completed'] and base['failures'] == [], 'audited input completion')
    check(data['primes'] == base['generators'], 'full ordered factor base including lattices')
    check(len(data['primes']) == 32 and data['box'] == [-2, 2] and data['excluded'] == [0, 0, 0, 0], 'fixed target')
    POLY = [-109375, -32500, 150, 64, 1]
    basis = [[Q(x) for x in row] for row in base['order']['basis']]
    inverse = base['order']['inverse']
    check(basis == [[1, 0, Q(1, 2), Q(31, 30)], [0, 1, Q(7, 25), Q(179, 750)],
                    [0, 0, Q(1, 50), Q(239, 18750)], [0, 0, 0, Q(1, 18750)]], 'fixed integral basis')
    check(inverse == [[1, 0, -25, -13400], [0, 1, -14, -1129],
                      [0, 0, 50, -11950], [0, 0, 0, 18750]], 'fixed basis inverse')
    check([[sum(inverse[i][k] * basis[k][j] for k in range(4)) for j in range(4)]
           for i in range(4)] == [unit(i) for i in range(4)], 'basis inverse identity')
    TABLE = []
    for i in range(4):
        row = []
        for j in range(4):
            power = field_product([r[i] for r in basis], [r[j] for r in basis])
            value = [sum(inverse[k][t] * power[t] for t in range(4)) for k in range(4)]
            check(all(c.denominator == 1 for c in value), 'integral basis product')
            row.append([int(c) for c in value])
        TABLE.append(row)
    check(TABLE == data['table'] and TABLE == base['order']['table'], 'complete independently rebuilt table')
    primes = data['primes']
    check(all(p['p'] == p['lattice']['norm'] for p in primes), 'degree-one prime norms')
    b.phase('replay: all lattice span certificates')
    exponents = []
    for lattice_id, lattice in enumerate(data['lattices']):
        origin, h = lattice['origin'], lattice['rows']
        check(len(h) == 4 and all(len(v) == 4 and all(type(x) is int for x in v) for v in h), 'integral full lattice')
        check(all(h[i][i] > 0 and all(h[i][j] == 0 for j in range(i)) for i in range(4)), 'positive upper triangular rows')
        if origin == {'identity': True}:
            check(lattice_id == 0, 'unique identity lattice')
            generators, vector, norm = [unit(i) for i in range(4)], [0] * 32, 1
        elif 'prime' in origin:
            i = origin['prime']
            check(origin == dict(prime=i) and 0 <= i < 32 and lattice_id == i + 1, 'ordered prime origin')
            generators, vector, norm = primes[i]['lattice']['columns'], unit(i, 32), primes[i]['p']
        else:
            left, right = origin['product']
            check(origin == dict(product=[left, right]) and 0 <= left < lattice_id and 0 <= right < lattice_id, 'acyclic product origin')
            a, c = data['lattices'][left], data['lattices'][right]
            generators = [multiply(v, w) for v in a['rows'] for w in c['rows']]
            vector = [u + v for u, v in zip(exponents[left], exponents[right])]
            norm = a['norm'] * c['norm']
        forward, backward = lattice['forward'], lattice['backward']
        check(len(forward) == 4 and len(backward) == len(generators), 'both span witness domains')
        for row, coordinates in zip(h, forward):
            check(all(type(x) is int for x in coordinates), 'integral forward span')
            check(combination(coordinates, generators) == row, 'reduced lattice contained in product span')
        for generator, record in zip(generators, backward):
            check(witness(h, generator, record), 'product span contained in reduced lattice')
        check(abs(determinant(h)) == norm and lattice['norm'] == norm, 'exact lattice index and product norm')
        exponents.append(vector)
        RESULT['lattices'].append(dict(id=lattice_id, norm=norm, exponents=vector))
    check(len(data['lattices']) >= 33, 'all base lattices present')
    b.phase('replay: exhaustive elements, support and principal ideals')
    check(len(data['elements']) == 624, 'complete nonzero box size')
    rational_primes = sorted(set(p['p'] for p in primes))
    accepted, parity, counts = [], [], dict(accepted=0, rational_cofactor=0, omitted_prime=0)
    expected_ids = [i for i in range(625) if i != 312]
    check([e['tuple_id'] for e in data['elements']] == expected_ids, 'every tuple exactly once')
    for entry in data['elements']:
        tuple_id = entry['tuple_id']
        integer, a = tuple_id, []
        for i in range(4):
            a.insert(0, integer % 5 - 2)
            integer = integer // 5
        check(integer == 0 and entry['coefficients'] == a and any(a), 'independent base-five tuple enumeration')
        principal = [multiply(unit(i), a) for i in range(4)]
        n = abs(determinant(principal))
        check(n > 0 and principal == entry['principal'] and n == entry['norm'], 'principal matrix and absolute norm')
        remainder, position = n, 0
        for p in rational_primes:
            while True:
                check(position < len(entry['smooth_divisions']), 'all filter divisions present')
                divisor, numerator, q, r = entry['smooth_divisions'][position]
                check(divisor == p and numerator == remainder and numerator == p * q + r
                      and 0 <= r < p, 'filter Euclidean identity')
                position = position + 1
                if r:
                    break
                remainder = q
        check(position == len(entry['smooth_divisions']) and remainder == entry['residual'], 'complete filter and residual')
        record = dict(tuple_id=tuple_id, norm=n)
        if remainder > 1:
            decision = 'rational_cofactor'
            check('valuations' not in entry and 'membership' not in entry, 'filter rejection is terminal')
        else:
            check(remainder == 1 and len(entry['valuations']) == 32 and len(entry['membership']) == 32, 'all valuations retained')
            valuations = []
            for i, tests in enumerate(entry['membership']):
                check(len(tests) >= 1, 'first nonmembership required')
                for j, test in enumerate(tests):
                    lattice_id = test['lattice']
                    check(0 <= lattice_id < len(exponents), 'power lattice exists')
                    check(exponents[lattice_id] == [x * (j + 1) for x in unit(i, 32)], 'successive power of this prime')
                    member = witness(data['lattices'][lattice_id]['rows'], a, test['witness'], True)
                    check(member == (j < len(tests) - 1), 'all successes then first failure')
                e = len(tests) - 1
                check(2 ** e <= n, 'integer norm valuation bound')
                valuations.append(e)
            check(valuations == entry['valuations'], 'complete exact exponent vector')
            supported = 1
            for p, e in zip(primes, valuations):
                supported = supported * p['p'] ** e
            check(supported == entry['supported_norm'] and n % supported == 0, 'exact supported norm divides total')
            if supported < n:
                decision = 'omitted_prime'
                check('product_lattice' not in entry, 'support deficit never accepted')
            else:
                check(supported == n, 'supported norm equality')
                decision = 'accepted'
                lattice_id = entry['product_lattice']
                check(exponents[lattice_id] == valuations, 'full product ideal exponents')
                h = data['lattices'][lattice_id]['rows']
                check(len(entry['principal_containment']) == 4, 'all principal generators checked')
                for v, w in zip(principal, entry['principal_containment']):
                    check(witness(h, v, w), 'principal contained in product')
                check(data['lattices'][lattice_id]['norm'] == n, 'equal indices certify ideal equality')
                accepted.append(tuple_id)
                parity.append(sum((e % 2) * 2 ** i for i, e in enumerate(valuations)))
            record.update(valuations=valuations, supported_norm=supported)
        check(entry['decision'] == decision, 'exact support classification')
        counts[decision] = counts[decision] + 1
        record['decision'] = decision
        RESULT['elements'].append(record)
        if len(RESULT['elements']) % 64 == 0:
            save()
    check(accepted == data['accepted_ids'] and parity == data['parity_rows'] and counts == data['counts'], 'all accepted rows and counts')
    b.phase('replay: complete producer elimination and independent opposite-pivot rank')
    check(len(data['elimination']) == len(parity), 'one elimination record per relation')
    pivots, reduced = {}, []
    for i, (mask, operation) in enumerate(zip(parity, data['elimination'])):
        current, used = mask, []
        for column in sorted(pivots):
            if (current >> column) & 1:
                row = pivots[column]
                current = current ^ reduced[row]
                used.append(row)
        pivot = next((j for j in range(32) if (current >> j) & 1), None)
        check(operation == dict(input=mask, subtract=used, output=current, pivot=pivot), 'complete elimination operation')
        if pivot is not None:
            pivots[pivot] = i
        reduced.append(current)
    check(sorted(pivots) == data['pivot_columns'] and len(pivots) == data['rank'], 'producer pivots and rank')
    independent = {}
    independent_records = []
    for mask in reversed(parity):
        current, used = mask, []
        while current:
            pivot = current.bit_length() - 1
            if pivot not in independent:
                independent[pivot] = current
                break
            used.append(pivot)
            current = current ^ independent[pivot]
        independent_records.append(dict(input=mask, subtract_columns=used, output=current))
    rank = len(independent)
    check(rank == data['rank'], 'independent descending-pivot rank')
    RESULT.update(completed=True, counts=counts, rank=rank, required_rank=32,
                  class_two_rank_upper_bound=32 - rank, accepted_ids=accepted,
                  parity_rows=parity, producer_pivots=sorted(pivots),
                  independent_pivots=sorted(independent), independent_elimination=independent_records,
                  budget=b.summary())
    save()
    print(json.dumps(dict(completed=True, checks=RESULT['checks'], rank=rank, required_rank=32,
                         counts=counts, budget=b.summary(), verification=str(OUT))))

if __name__ == '__main__':
    if not globals().get('__instrumented__'):
        run(__file__)
    else:
        try:
            main()
        except Exception as exc:
            RESULT['failures'].append(repr(exc))
            save()
            raise
