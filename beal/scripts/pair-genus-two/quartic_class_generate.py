"""Approved bounded Minkowski factor base, exact producer (low-first polys)."""
import json
from pathlib import Path
from hashlib import sha256
from itertools import combinations, product
from fractions import Fraction as Q
from quartic_class_budget import run
ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'quartic-class-certificate.json'
DATA = dict(completed=False, failures=[], regular=[], exceptional=[])

def save():
    OUT.write_text(json.dumps(DATA, separators=(',', ':')) + '\n')

def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def divide(a, h, p):
    b.charge('polynomial_divisions')
    r = [x % p for x in a]
    q = [0] * max(1, len(a) - len(h) + 1)
    for i in range(len(a) - len(h), -1, -1):
        c = r[i + len(h) - 1]
        q[i] = c
        for j, x in enumerate(h):
            r[i + j] = (r[i + j] - c * x) % p
    return trim(q), trim(r)

def mulpoly(a, c, p):
    r = [0] * (len(a) + len(c) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(c):
            r[i + j] = (r[i + j] + x * y) % p
    return trim(r)

def inv(x, p):
    # Tiny complete prime-field inverse search, charged by instrumentation.
    return next(y for y in range(1, p) if x * y % p == 1)

def rref(rows, p):
    rows = [[x % p for x in r] for r in rows]
    j = 0
    for c in range(4):
        k = next((i for i in range(j, len(rows)) if rows[i][c]), None)
        if k is None:
            continue
        rows[j], rows[k] = rows[k], rows[j]
        u = inv(rows[j][c], p)
        rows[j] = [x * u % p for x in rows[j]]
        for i in range(len(rows)):
            if i != j:
                u = rows[i][c]
                rows[i] = [(x - u * y) % p for x, y in zip(rows[i], rows[j])]
        j = j + 1
    return rows[:j]

def contains(w, v, p):
    b.charge('subspace_tests')
    v = list(v)
    for row in w:
        pivot = next(i for i, x in enumerate(row) if x)
        u = v[pivot]
        v = [(x - u * y) % p for x, y in zip(v, row)]
    return not any(v)

def times(a, c, table):
    return [sum(a[i] * c[j] * table[i][j][k] for i in range(4) for j in range(4)) for k in range(4)]

def unit(i):
    return [int(j == i) for j in range(4)]

def lattice(w, p, table):
    piv = [next(i for i, x in enumerate(row) if x) for row in w]
    cols = w + [[p * x for x in unit(i)] for i in range(4) if i not in piv]
    def coords(v):
        v = list(v)
        coefficients = []
        for row, pivot in zip(w, piv):
            c = v[pivot]
            coefficients.append(c)
            v = [x - c * y for x, y in zip(v, row)]
        for i in range(4):
            if i not in piv:
                assert v[i] % p == 0
                coefficients.append(v[i] // p)
        return coefficients
    pcoords = [coords([p * x for x in unit(i)]) for i in range(4)]
    actions = [[coords(times(unit(i), v, table)) for v in cols] for i in range(4)]
    return dict(columns=cols, norm=p ** (4 - len(w)), p_coordinates=pcoords, closure_actions=actions)

def allspaces(p):
    for d in range(5):
        for piv in combinations(range(4), d):
            free = [(i, j) for i, c in enumerate(piv) for j in range(c + 1, 4) if j not in piv]
            for entries in product(range(p), repeat=len(free)):
                b.charge('exceptional_subspaces')
                rows = [[int(j == c) for j in range(4)] for c in piv]
                for (i, j), x in zip(free, entries):
                    rows[i][j] = x
                yield rows

def main():
    source = ROOT / 'quartic-order-certificate.json'
    payload = source.read_bytes()
    old = json.loads(payload)
    final = old['orders'][old['final_order_id']]
    table = final['table']
    g = old['polynomial']
    assert g == [-109375, -32500, 150, 64, 1]
    assert final['discriminant'] == 2874960 and old['total_index'] == 937500
    DATA.update(input_sha256=sha256(payload).hexdigest(), order=final,
                index=old['total_index'], polynomial=g)
    b.phase('signature and rational bound')
    # Deterministic integer interval scan, preserving every rejected evaluation.
    values = []
    for x in range(-100, 101):
        b.charge('sign_evaluations')
        y = sum(c * x ** i for i, c in enumerate(g))
        values.append([x, y])
    intervals = [[a, c] for a, c in zip(values, values[1:]) if a[1] * c[1] < 0]
    assert len(intervals) == 4
    D, upper_sqrt, U = final['discriminant'], 1696, 159
    assert D < upper_sqrt ** 2 and 3 * upper_sqrt == 32 * U and U <= 300
    DATA.update(signature=dict(values=values, intervals=intervals, real=4, complex_pairs=0),
                bound=dict(discriminant=D, sqrt_upper=upper_sqrt, coefficient='3/32', U=U))
    trials, primes = [], []
    for n in range(2, U + 1):
        divisions = [[d, n % d] for d in range(2, n) if d * d <= n]
        prime = all(r != 0 for d, r in divisions)
        trials.append(dict(n=n, divisions=divisions, prime=prime))
        if prime:
            primes.append(n)
    DATA.update(prime_trials=trials, primes=primes)
    save()
    for p in primes:
        if p in (2, 3, 5):
            continue
        b.phase('regular prime ' + str(p))
        residual = [x % p for x in g]
        factors, extraction = [], []
        for degree in (1, 2):
            for coefficients in product(range(p), repeat=degree):
                h = list(coefficients) + [1]
                attempts = []
                while len(residual) - 1 >= 2 * degree:
                    q, r = divide(residual, h, p)
                    attempts.append(dict(dividend=residual, quotient=q, remainder=r))
                    if any(r):
                        break
                    factors.append(h)
                    residual = q
                # Every domain candidate is recorded, including ineligible ones.
                extraction.append(dict(factor=h, attempts=attempts))
        if len(residual) > 1:
            factors.append(residual)
        assert factors
        distinct = []
        for h in factors:
            if h not in distinct:
                distinct.append(h)
        irreducibility = []
        for h in distinct:
            tests = []
            for degree in range(1, (len(h) - 1) // 2 + 1):
                for coefficients in product(range(p), repeat=degree):
                    divisor = list(coefficients) + [1]
                    q, r = divide(h, divisor, p)
                    assert any(r)
                    tests.append(dict(divisor=divisor, quotient=q, remainder=r))
            irreducibility.append(dict(factor=h, tests=tests))
        reconstruction = [1]
        for h in factors:
            reconstruction = mulpoly(reconstruction, h, p)
        assert reconstruction == [x % p for x in g]
        ideals = []
        for h in distinct:
            # h(alpha) by Horner in the audited integral basis.
            v = [0] * 4
            for c in reversed(h):
                v = times(v, unit(1), table)
                v[0] = v[0] + c
            image = [times(v, unit(i), table) for i in range(4)]
            w = rref(image, p)
            I = lattice(w, p, table)
            assert I['norm'] == p ** (len(h) - 1)
            ideals.append(dict(factor=h, h_alpha=v, image_generators=image,
                               rref=w, lattice=I, included=I['norm'] <= U))
        DATA['regular'].append(dict(p=p, factors=factors, extraction=extraction,
                                    irreducibility=irreducibility, ideals=ideals))
        save()
    for p in (2, 3, 5):
        b.phase('exceptional prime ' + str(p))
        spaces = []
        for w in allspaces(p):
            witness = None
            for i in range(4):
                for j, v in enumerate(w):
                    z = [x % p for x in times(unit(i), v, table)]
                    if not contains(w, z, p):
                        witness = dict(basis=i, row=j, product=z)
                        break
                if witness is not None:
                    break
            spaces.append(dict(rref=w, ideal=witness is None, nonideal_witness=witness))
        proper = [i for i, s in enumerate(spaces) if s['ideal'] and len(s['rref']) < 4]
        maximal = []
        for i in proper:
            w = spaces[i]['rref']
            bigger = next((j for j in proper if len(spaces[j]['rref']) > len(w)
                           and all(contains(spaces[j]['rref'], v, p) for v in w)), None)
            spaces[i]['containing_proper_ideal'] = bigger
            if bigger is None:
                maximal.append(i)
        ideals = [dict(space_id=i, lattice=lattice(spaces[i]['rref'], p, table)) for i in maximal]
        for I in ideals:
            I['included'] = I['lattice']['norm'] <= U
        DATA['exceptional'].append(dict(p=p, spaces=spaces, proper_ideals=proper,
                                        maximal_ideals=maximal, ideals=ideals))
        save()
    DATA['generators'] = [dict(p=r['p'], factor=I['factor'], lattice=I['lattice'])
                          for r in DATA['regular'] for I in r['ideals'] if I['included']]
    DATA['generators'].extend(dict(p=r['p'], space_id=I['space_id'], lattice=I['lattice'])
                              for r in DATA['exceptional'] for I in r['ideals'] if I['included'])
    DATA['completed'] = True
    save()
    print(json.dumps(dict(completed=True, cutoff=U, rational_primes=len(primes),
                         generators=len(DATA['generators']), certificate=str(OUT), budget=b.summary())))

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
