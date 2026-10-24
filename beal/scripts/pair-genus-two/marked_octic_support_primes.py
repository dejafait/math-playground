"""Exact support-prime instance of the approved arbitrary-order method.

No external packages. Integer lattices have column bases in L116's basis.
Every product lattice records reversible integer row operations on its
full list of generators; no determinant-only ideal equality is used.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product as tuples
from hashlib import sha256
import json
import traceback
import marked_octic_maximal_order as base

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'marked-octic-maximal-order-certificate.json'
OUTPUT = HERE / 'marked-octic-support-primes-certificate.json'
N = 8


def decode(x):
    if isinstance(x, list):
        return [decode(v) for v in x]
    if isinstance(x, dict):
        return {k: decode(v) for k, v in x.items()}
    return Q(x) if isinstance(x, str) and '/' in x and all(
        c in '-0123456789/' for c in x) else x


def columns(a):
    return base.transpose(a)


def ident(scale=1):
    return [[scale*int(i == j) for j in range(N)] for i in range(N)]


def linear(columns_, coeffs, p):
    return [sum(v[i]*c for v, c in zip(columns_, coeffs)) % p for i in range(N)]


def select_basis(vectors, p):
    k = base.kernel(columns(vectors), p)
    return [vectors[j] for j in k['pivots']]


def coords(basis, v, p):
    # Invert a square minor obtained by complete row-space elimination.
    rows = base.kernel(basis, p)['pivots']
    a = [[b[i] % p for b in basis]+[v[i] % p] for i in rows]
    n = len(basis)
    assert len(rows) == n
    for j in range(n):
        k = next(k for k in range(j, n) if a[k][j])
        a[j], a[k] = a[k], a[j]
        c = pow(a[j][j], -1, p)
        a[j] = [c*x % p for x in a[j]]
        for k in range(n):
            if k != j:
                c = a[k][j]
                a[k] = [(x-c*y) % p for x, y in zip(a[k], a[j])]
    answer = [a[i][-1] for i in range(n)]
    assert linear(basis, answer, p) == [x % p for x in v]
    return answer


def remainder(a, g, p):
    a = [x % p for x in a]
    while a and not a[-1]:
        a.pop()
    while len(a) >= len(g):
        c = a[-1] * pow(g[-1], -1, p) % p
        shift = len(a)-len(g)
        for j, x in enumerate(g):
            a[shift+j] = (a[shift+j]-c*x) % p
        while a and not a[-1]:
            a.pop()
    return a


def irreducibility(g, p):
    # Exhaust every possible monic divisor of degree <= half deg(g).
    trials = []
    for d in range(1, (len(g)-1)//2+1):
        for coeff in tuples(range(p), repeat=d):
            h = list(coeff)+[1]
            r = remainder(g, h, p)
            assert r, ('reducible', p, g, h)
            trials.append(dict(divisor=h, remainder=r))
    return trials


def hnf_rows(generators):
    """Unimodular integer row reduction, retaining ALL operations."""
    a = [list(map(int, v)) for v in generators]
    operations = []
    def swap(i, j):
        if i != j:
            a[i], a[j] = a[j], a[i]
            operations.append(['swap', i, j])
    def add(i, j, q):
        if q:
            a[i] = [x+q*y for x, y in zip(a[i], a[j])]
            operations.append(['add', i, j, q])
    for j in range(N):
        k = next(k for k in range(j, len(a)) if a[k][j])
        swap(j, k)
        for i in range(j+1, len(a)):
            while a[i][j]:
                q = a[j][j]//a[i][j]
                add(j, i, -q)
                swap(j, i)
        if a[j][j] < 0:
            a[j] = [-x for x in a[j]]
            operations.append(['negate', j])
        for i in range(j):
            add(i, j, -(a[i][j]//a[j][j]))
    assert all(not any(r) for r in a[N:])
    basis = columns(a[:N])
    return dict(generators=generators, operations=operations,
                reduced_rows=a, basis=basis)


def ideal_product(a, b, table):
    generators = []
    for x in columns(a):
        for y in columns(b):
            generators.append([sum(x[i]*y[j]*table[i][j][k]
                                   for i in range(N) for j in range(N))
                               for k in range(N)])
    return hnf_rows(generators)


def contains_p(basis, p):
    coordinates = base.mm(base.inverse(basis), ident(p))
    return all(Q(x).denominator == 1 for r in coordinates for x in r), coordinates


def discover(o, p):
    table, one = o['table'], o['one']
    mul = lambda x, y: base.fp_product(x, y, table, p)
    q = p
    while q < N:
        q *= p
    frob = columns([base.fp_power(v, q, one, table, p) for v in ident()])
    k = base.kernel(frob, p)
    reduced_basis = [columns(frob)[j] for j in k['pivots']]
    elements = [(list(c), linear(reduced_basis, c, p))
                for c in tuples(range(p), repeat=len(reduced_basis))]
    idem = [(c, v) for c, v in elements if mul(v, v) == v]
    nonzero = [(c, v) for c, v in idem if any(v)]
    primitive = [(c, v) for c, v in nonzero
                 if not any(w != v and mul(v, w) == w for _, w in nonzero)]
    assert [sum(v[j] for _, v in primitive) % p for j in range(N)] == one
    assert all(not any(mul(v, w)) for i, (_, v) in enumerate(primitive)
               for _, w in primitive[i+1:])
    result = dict(prime=p, frobenius_exponent=q, frobenius=frob,
                  frobenius_kernel=k, reduced_basis=reduced_basis,
                  enumerated_elements=len(elements), idempotents=idem,
                  primitive_idempotents=primitive, primes=[], powers=[],
                  complete_product=[])
    for number, (_, e) in enumerate(primitive):
        comp = select_basis([mul(e, b) for b in reduced_basis], p)
        f = len(comp)
        found = None
        for c in tuples(range(p), repeat=f):
            a = linear(comp, c, p)
            powers = [e]
            for _ in range(f):
                powers.append(mul(powers[-1], a))
            if len(select_basis(powers[:f], p)) == f:
                rel = coords(powers[:f], powers[f], p)
                g = [(-x) % p for x in rel]+[1]
                found = (a, powers, g)
                break
        assert found is not None
        a, powers, g = found
        irred = irreducibility(g, p)
        images = [coords(powers[:f], mul(e, b), p) for b in columns(frob)]
        quotient = columns(images)
        assert coords(powers[:f], e, p) == [1]+[0]*(f-1)
        kernel = base.kernel(quotient, p)
        assert kernel['rank'] == f
        ideal = base.inverse_image_lattice(kernel, p)
        inv = base.inverse(ideal)
        stability = [base.ints(base.mm(inv, base.mm(columns(table[i]), ideal)))
                     for i in range(N)]
        assert base.mv(quotient, one) == [1]+[0]*(f-1) or \
            [x % p for x in base.mv(quotient, one)] == [1]+[0]*(f-1)
        record = dict(label=f'P{p}_{number+1}', idempotent=e,
                      component_basis=comp, residue_degree=f,
                      generator=a, generator_powers=powers,
                      residue_polynomial=g, irreducibility_trials=irred,
                      quotient_map=quotient, quotient_kernel=kernel,
                      ideal_basis=ideal, ideal_inverse=inv,
                      stability_matrices=stability,
                      contains_p_coordinates=base.ints(base.mm(inv, ident(p))))
        # Direct quotient product verification using polynomial reduction.
        products = []
        for i in range(N):
            row = []
            for j in range(N):
                poly = [0]*(2*f-1)
                for r, x in enumerate(images[i]):
                    for s, y in enumerate(images[j]):
                        poly[r+s] += x*y
                r = remainder(poly, g, p)
                r += [0]*(f-len(r))
                expected = [sum(quotient[k][l]*table[i][j][l]
                                for l in range(N)) % p for k in range(f)]
                assert r == expected
                row.append(r)
            products.append(row)
        record['quotient_products'] = products
        result['primes'].append(record)
    # Ramification is read by exact containment of pO in successive powers.
    # Unique ideal factorization makes the last containing power its e.
    for rec in result['primes']:
        current = ident()
        power_records = []
        for exponent in range(1, N+2):
            pr = ideal_product(current, rec['ideal_basis'], table)
            ok, inc = contains_p(pr['basis'], p)
            pr.update(exponent=exponent, contains_p=ok, p_coordinates=inc,
                      left_basis=current, right_basis=rec['ideal_basis'])
            power_records.append(pr)
            current = pr['basis']
            if not ok:
                break
        else:
            raise AssertionError('ramification cap exceeded')
        rec['ramification_index'] = len(power_records)-1
        assert rec['ramification_index'] >= 1
        result['powers'].append(dict(label=rec['label'], records=power_records))
    current = ident()
    for rec in result['primes']:
        for _ in range(rec['ramification_index']):
            pr = ideal_product(current, rec['ideal_basis'], table)
            pr.update(left_basis=current, right_basis=rec['ideal_basis'],
                      label=rec['label'])
            result['complete_product'].append(pr)
            current = pr['basis']
    assert current == ident(p), ('product failure', p, current)
    degree_sum = sum(rec['residue_degree']*rec['ramification_index']
                     for rec in result['primes'])
    assert degree_sum == N
    assert len({str(rec['ideal_basis']) for rec in result['primes']}) == len(result['primes'])
    result.update(final_product=current, degree_sum=degree_sum, completed=True)
    return result


def main():
    raw = SOURCE.read_bytes()
    src = decode(json.loads(raw))
    assert src['completed'] and not src['failures']
    o = src['orders'][src['final_order_id']]
    c = dict(source=SOURCE.name, source_sha256=sha256(raw).hexdigest(),
             basis=o['basis'], table=o['table'], one=o['one'],
             field_discriminant=o['discriminant'], decompositions=[],
             failures=[], completed=False)
    def save():
        OUTPUT.write_text(json.dumps(base.encode(c), indent=2)+'\n')
    save()
    try:
        for p in [2, 3, 5, 11]:
            result = discover(o, p)
            c['decompositions'].append(result)
            save()
            print('prime', p, 'e,f', [(r['ramification_index'], r['residue_degree'])
                                     for r in result['primes']],
                  'degree_sum', result['degree_sum'], 'required', N,
                  'exact_product', result['final_product'] == ident(p), flush=True)
        c['completed'] = True
    except Exception:
        c['failures'].append(traceback.format_exc())
        save()
        raise
    save()
    print('completed', c['completed'], 'failures', len(c['failures']),
          'certificate', OUTPUT)


if __name__ == '__main__':
    main()
