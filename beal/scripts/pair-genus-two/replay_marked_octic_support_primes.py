"""Independent full replay of support-prime certificates.

Imports the previously independent L116 replay for field arithmetic,
rank certificates and determinants, never the support-prime producer.
Every integer row operation is checked forward AND backward.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product as tuples
from hashlib import sha256
import json
import traceback
import replay_marked_octic_maximal_order as old

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'marked-octic-support-primes-certificate.json'
OUTPUT = HERE / 'marked-octic-support-primes-replay.json'
N = 8
E = old.equal


def transpose(a):
    return [list(v) for v in zip(*a)]


def identity(scale=1):
    return [[scale*int(i == j) for j in range(N)] for i in range(N)]


def multiply(x, y, table):
    answer = [0]*N
    for j in range(N):
        col = [sum(x[i]*table[i][j][k] for i in range(N)) for k in range(N)]
        answer = [a+y[j]*b for a, b in zip(answer, col)]
    return answer


def modmul(x, y, table, p):
    return [a % p for a in multiply(x, y, table)]


def polyreduce(a, g, p):
    a = [x % p for x in a]
    for i in range(len(a)-1, len(g)-2, -1):
        c = a[i]*pow(g[-1], -1, p) % p
        for j in range(len(g)):
            a[i-len(g)+1+j] = (a[i-len(g)+1+j]-c*g[j]) % p
    r = a[:len(g)-1]
    while r and r[-1] == 0:
        r.pop()
    return r


def scalar_combine(basis, c, p):
    return [sum(b[j]*a for b, a in zip(basis, c)) % p for j in range(N)]


def inv(a):
    n = len(a)
    rows = [[Q(x) for x in r]+[Q(i == j) for j in range(n)]
            for i, r in enumerate(a)]
    for j in range(n):
        k = next(k for k in range(j, n) if rows[k][j])
        rows[j], rows[k] = rows[k], rows[j]
        q = rows[j][j]
        rows[j] = [x/q for x in rows[j]]
        for i in range(n):
            if i != j:
                q = rows[i][j]
                rows[i] = [x-q*y for x, y in zip(rows[i], rows[j])]
    return [r[n:] for r in rows]


def check_hnf(name, r, left, right, table):
    E(name+' linked left basis', r['left_basis'], left)
    E(name+' linked right basis', r['right_basis'], right)
    gens = [multiply(x, y, table) for x in transpose(left) for y in transpose(right)]
    E(name+' complete 64 product generators', r['generators'], gens)
    rows = [list(x) for x in gens]
    def apply(op, backward=False):
        if op[0] == 'swap':
            _, i, j = op
            assert 0 <= i < len(rows) and 0 <= j < len(rows)
            rows[i], rows[j] = rows[j], rows[i]
        elif op[0] == 'negate':
            _, i = op
            assert 0 <= i < len(rows)
            rows[i] = [-x for x in rows[i]]
        elif op[0] == 'add':
            _, i, j, q = op
            assert i != j and 0 <= i < len(rows) and 0 <= j < len(rows)
            assert isinstance(q, int)
            q *= -1 if backward else 1
            rows[i] = [x+q*y for x, y in zip(rows[i], rows[j])]
        else:
            raise AssertionError(('unknown operation', op))
    for op in r['operations']:
        apply(op)
    # Reverse replay below mutates rows in place. Retain the forward state,
    # rather than a reference whose saved actual value later changes.
    E(name+' all forward row operations', [row[:] for row in rows], r['reduced_rows'])
    E(name+' terminal zero rows', rows[N:], [[0]*N]*(len(rows)-N))
    E(name+' full terminal basis', transpose(rows[:N]), r['basis'])
    E(name+' positive pivots', all(rows[j][j] > 0 for j in range(N)), True)
    E(name+' triangular and reduced',
      all(rows[i][j] == 0 for i in range(N) for j in range(i)) and
      all(0 <= rows[i][j] < rows[j][j] for j in range(N) for i in range(j)), True)
    for op in reversed(r['operations']):
        apply(op, True)
    E(name+' all reverse row operations', rows, gens)
    return r['basis']


def main():
    old.CHECKS.clear()
    old.RECORDS.clear()
    raw = SOURCE.read_bytes()
    c = old.decode(json.loads(raw))
    report = dict(source=SOURCE.name, source_sha256=sha256(raw).hexdigest(),
                  checks=old.CHECKS, rank_records=old.RECORDS,
                  summaries=[], failures=[], completed=False)
    try:
        prior_raw = (HERE/c['source']).read_bytes()
        E('L116 source hash', sha256(prior_raw).hexdigest(), c['source_sha256'])
        prior = old.decode(json.loads(prior_raw))
        E('L116 completed and no failures', prior['completed'] and not prior['failures'], True)
        o = prior['orders'][prior['final_order_id']]
        # Independently reconstruct every fixed basis product and trace.
        old.order_record(o, 'support-prime input')
        E('same field basis', c['basis'], o['basis'])
        E('same full table', c['table'], o['table'])
        E('same one', c['one'], o['one'])
        E('same discriminant', c['field_discriminant'], 2**8*3**7*5**4*11**7)
        table, one = o['table'], o['one']
        E('exact support', [d['prime'] for d in c['decompositions']], [2, 3, 5, 11])
        for d in c['decompositions']:
            p = d['prime']
            prefix = f'p={p}'
            q = p
            while q < N:
                q *= p
            E(prefix+' nilpotent-killing exponent', d['frobenius_exponent'], q)
            frobcols = []
            for v in identity():
                r = list(one)
                for _ in range(q):
                    r = modmul(r, v, table, p)
                frobcols.append(r)
            frob = transpose(frobcols)
            E(prefix+' full Frobenius matrix', d['frobenius'], frob)
            old.check_kernel(prefix+' Frobenius', frob, d['frobenius_kernel'], p)
            reduced = [frobcols[j] for j in d['frobenius_kernel']['pivots']]
            E(prefix+' reduced algebra basis', d['reduced_basis'], reduced)
            E(prefix+' reduced basis independent', old.rank_by_columns(transpose(reduced), p)[0], len(reduced))
            all_idem = []
            count = 0
            for c0 in tuples(range(p), repeat=len(reduced)):
                count += 1
                v = scalar_combine(reduced, c0, p)
                if modmul(v, v, table, p) == v:
                    all_idem.append([list(c0), v])
            E(prefix+' exhaustive element count', d['enumerated_elements'], count)
            E(prefix+' complete idempotent list', d['idempotents'], all_idem)
            nonzero = [r for r in all_idem if any(r[1])]
            primitive = [r for r in nonzero if not any(
                s[1] != r[1] and modmul(r[1], s[1], table, p) == s[1] for s in nonzero)]
            E(prefix+' complete primitive idempotents', d['primitive_idempotents'], primitive)
            E(prefix+' primitive sum one', [sum(r[1][j] for r in primitive) % p for j in range(N)], one)
            E(prefix+' primitive orthogonality', all(not any(modmul(r[1], s[1], table, p))
                for i, r in enumerate(primitive) for s in primitive[i+1:]), True)
            E(prefix+' prime count', len(d['primes']), len(primitive))
            for i, r in enumerate(d['primes']):
                name = r['label']
                E(name+' ordered label', name, f'P{p}_{i+1}')
                e, f, g = r['idempotent'], r['residue_degree'], r['residue_polynomial']
                E(name+' idempotent linkage', e, primitive[i][1])
                compcols = [modmul(e, b, table, p) for b in reduced]
                E(name+' component dimension', old.rank_by_columns(transpose(compcols), p)[0], f)
                comp = r['component_basis']
                E(name+' component basis independent', old.rank_by_columns(transpose(comp), p)[0], f)
                E(name+' component span correct', old.rank_by_columns(transpose(comp+compcols), p)[0], f)
                powers = [e]
                for _ in range(f):
                    powers.append(modmul(powers[-1], r['generator'], table, p))
                E(name+' all generator powers', r['generator_powers'], powers)
                E(name+' generator power basis rank', old.rank_by_columns(transpose(powers[:f]), p)[0], f)
                E(name+' monic polynomial degree', (len(g)-1, g[-1]), (f, 1))
                E(name+' polynomial relation', scalar_combine(powers, g, p), [0]*N)
                trials = []
                for deg in range(1, f//2+1):
                    for cc in tuples(range(p), repeat=deg):
                        h = list(cc)+[1]
                        rr = polyreduce(g, h, p)
                        assert rr, (name, 'reducible', h)
                        trials.append(dict(divisor=h, remainder=rr))
                E(name+' every irreducibility trial', r['irreducibility_trials'], trials)
                quotient = r['quotient_map']
                E(name+' quotient shape', (len(quotient), [len(row) for row in quotient]), (f, [N]*f))
                E(name+' quotient one', [sum(a*b for a, b in zip(row, one)) % p for row in quotient], [1]+[0]*(f-1))
                E(name+' all quotient basis images',
                  [scalar_combine(powers[:f], v, p) for v in transpose(quotient)],
                  [modmul(e, v, table, p) for v in frobcols])
                prods = []
                for j, x in enumerate(transpose(quotient)):
                    row = []
                    for k, y in enumerate(transpose(quotient)):
                        poly = [sum(x[a]*y[b] for a in range(f) for b in range(f) if a+b == h)
                                for h in range(2*f-1)]
                        rem = polyreduce(poly, g, p)
                        rem += [0]*(f-len(rem))
                        expected = [sum(u*v for u, v in zip(qq, table[j][k])) % p for qq in quotient]
                        assert rem == expected, (name, 'quotient multiplication', j, k)
                        row.append(rem)
                    prods.append(row)
                E(name+' all 64 quotient products', r['quotient_products'], prods)
                old.check_kernel(name+' quotient', quotient, r['quotient_kernel'], p)
                E(name+' surjective quotient rank', r['quotient_kernel']['rank'], f)
                b, bi = r['ideal_basis'], r['ideal_inverse']
                E(name+' integral ideal basis', old.integral(b), True)
                E(name+' ideal left inverse', old.product(bi, b), identity())
                E(name+' ideal right inverse', old.product(b, bi), identity())
                E(name+' full ideal maps to zero',
                  [[v % p for v in row] for row in old.product(quotient, b)], [[0]*N for _ in range(f)])
                E(name+' exact kernel index', abs(old.determinant(b)), p**f)
                pinc = old.product(bi, identity(p))
                E(name+' p inclusion coordinates', r['contains_p_coordinates'], pinc)
                E(name+' contains pO', old.integral(pinc), True)
                E(name+' proper ideal', p**f > 1, True)
                actions = [old.product(old.product(bi, transpose(table[j])), b) for j in range(N)]
                E(name+' all eight stability matrices', r['stability_matrices'], actions)
                E(name+' all stability coordinates integral', old.integral(actions), True)
            # Distinctness is checked by two-way containment, not by basis strings.
            for i, a in enumerate(d['primes']):
                for b in d['primes'][i+1:]:
                    both = old.integral(old.product(a['ideal_inverse'], b['ideal_basis'])) and \
                           old.integral(old.product(b['ideal_inverse'], a['ideal_basis']))
                    E(prefix+' distinct '+a['label']+' '+b['label'], both, False)
            E(prefix+' power list labels', [r['label'] for r in d['powers']], [r['label'] for r in d['primes']])
            for r, powers in zip(d['primes'], d['powers']):
                current = identity()
                e = r['ramification_index']
                E(r['label']+' positive bounded ramification', 1 <= e <= N, True)
                E(r['label']+' terminal power included', len(powers['records']), e+1)
                for k, pr in enumerate(powers['records'], 1):
                    name = r['label']+f' power {k}'
                    E(name+' exponent', pr['exponent'], k)
                    current = check_hnf(name, pr, current, r['ideal_basis'], table)
                    pinc = old.product(inv(current), identity(p))
                    E(name+' p coordinates', pr['p_coordinates'], pinc)
                    E(name+' p containment result', pr['contains_p'], old.integral(pinc))
                    E(name+' exact terminal transition', old.integral(pinc), k <= e)
            expected_factors = [r for r in d['primes'] for _ in range(r['ramification_index'])]
            E(prefix+' full product factor count', len(d['complete_product']), len(expected_factors))
            current = identity()
            for j, (r, pr) in enumerate(zip(expected_factors, d['complete_product'])):
                E(prefix+f' product {j} factor', pr['label'], r['label'])
                current = check_hnf(prefix+f' complete product {j}', pr, current, r['ideal_basis'], table)
            E(prefix+' stored final product', d['final_product'], current)
            E(prefix+' full lattice equality product=pO', current, identity(p))
            degree = sum(r['residue_degree']*r['ramification_index'] for r in d['primes'])
            E(prefix+' recorded degree sum', d['degree_sum'], degree)
            E(prefix+' required degree sum', degree, N)
            E(prefix+' completed', d['completed'], True)
            summary = dict(prime=p, ef=[[r['ramification_index'], r['residue_degree']] for r in d['primes']],
                           degree_sum=degree, required_degree_sum=N, exact_product=True)
            report['summaries'].append(summary)
            print('replayed', prefix, 'e,f', summary['ef'], 'degree', degree, 'required', N, 'exact_product', True, flush=True)
        E('producer complete', c['completed'], True)
        E('producer failures', c['failures'], [])
        report['completed'] = True
    except Exception:
        report['failures'].append(traceback.format_exc())
        raise
    finally:
        OUTPUT.write_text(json.dumps(old.encode(report), indent=2)+'\n')
        print('replay_completed', report['completed'], 'checks', len(old.CHECKS),
              'failures', len(report['failures']), 'certificate', OUTPUT)


if __name__ == '__main__':
    main()
