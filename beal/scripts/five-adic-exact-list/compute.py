"""Complete finite certificate for L061; ascending polynomial coefficients.

Standard-library arithmetic only. General local arguments are in L061.
No global field/class computation and no numerical p-adic sampling.
"""
import json
from itertools import product
from pathlib import Path

BASE = Path(__file__).resolve().parent
N, Q = 11, 5**11
H = [3, 1, 2, 0, 4, 4, 2, 3, 1, 4, 3, 1]


class Ring:
    def __init__(self, modulus):
        self.m = modulus
        self.zero = (0,)*N
        self.one = self.c(1)

    def c(self, n): return (n % self.m,)+(0,)*(N-1)
    def add(self, a, b): return tuple((x+y) % self.m for x, y in zip(a, b))
    def neg(self, a): return tuple(-x % self.m for x in a)
    def sub(self, a, b): return self.add(a, self.neg(b))
    def scale(self, a, n): return tuple(x*n % self.m for x in a)

    def mul(self, a, b):
        c = [0]*(2*N-1)
        for i, u in enumerate(a):
            if u:
                for j, v in enumerate(b): c[i+j] += u*v
        for i in range(2*N-2, N-1, -1):
            u = c[i] % self.m
            for j in range(N): c[i-N+j] -= u*H[j]
        return tuple(x % self.m for x in c[:N])

    def pow(self, a, n):
        b = self.one
        while n:
            if n & 1: b = self.mul(b, a)
            a = self.mul(a, a)
            n >>= 1
        return b

    def inv(self, a):
        a0 = tuple(x % 5 for x in a)
        if a0 == K.zero: raise ArithmeticError('nonunit inverse')
        b = K.pow(a0, Q-2)
        for _ in range(2): b = self.mul(b, self.sub(self.c(2), self.mul(a, b)))
        assert self.mul(a, b) == self.one
        return b

    def ev(self, p, a):
        z = self.zero
        for u in reversed(p): z = self.add(self.mul(z, a), self.c(u))
        return z


K, R, R25 = Ring(5), Ring(125), Ring(25)
T = (0, 1)+(0,)*(N-2)


def trim(p):
    while len(p) > 1 and p[-1] == K.zero: p.pop()
    return p


def psub(a, b):
    c = list(a)+[K.zero]*max(0, len(b)-len(a))
    for i, x in enumerate(b): c[i] = K.sub(c[i], x)
    return trim(c)


def pmul(a, b):
    c = [K.zero]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] = K.add(c[i+j], K.mul(x, y))
    return trim(c)


def pdiv(a, b):
    a = list(a)
    q = [K.zero]*max(1, len(a)-len(b)+1)
    bi = K.inv(b[-1])
    while a != [K.zero] and len(a) >= len(b):
        j = len(a)-len(b)
        v = K.mul(a[-1], bi)
        q[j] = v
        a = psub(a, [K.zero]*j+[K.mul(v, x) for x in b])
    return trim(q), a


def pgcd(a, b):
    while b != [K.zero]: a, b = b, pdiv(a, b)[1]
    return [K.mul(x, K.inv(a[-1])) for x in a]


def ppow(a, n, f):
    b = [K.one]
    while n:
        if n & 1: b = pdiv(pmul(b, a), f)[1]
        a = pdiv(pmul(a, a), f)[1]
        n >>= 1
    return b


def split_roots(f):
    """Bounded deterministic splitting; complete root checks certify success."""
    pending, roots, trials = [f], [], []
    while pending:
        g = pending.pop()
        if len(g) == 2:
            roots.append(K.neg(K.mul(g[0], K.inv(g[1]))))
            continue
        for i in range(1, N):
            for c in range(5):
                v = K.add(K.pow(T, i), K.c(c))
                z = psub(ppow([v, K.one], (Q-1)//2, g), [K.one])
                h = pgcd(g, z)
                if 1 < len(h) < len(g):
                    quotient, remainder = pdiv(g, h)
                    assert remainder == [K.zero]
                    trials.append({'degree': len(g)-1, 'i': i, 'c': c,
                                   'factor': h, 'quotient': quotient})
                    pending.extend([h, quotient])
                    break
            else: continue
            break
        else: raise ArithmeticError('bounded splitting failed')
    return sorted(roots), trials


def deriv(p): return [i*p[i] for i in range(1, len(p))]


def scalar_div(a, b):
    a = [x % 5 for x in a]
    while len(a) > 1 and not a[-1]: a.pop()
    q = [0]*max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        j = len(a)-len(b)
        v = a[-1]*pow(b[-1], -1, 5) % 5
        q[j] = v
        for i, x in enumerate(b): a[i+j] = (a[i+j]-v*x) % 5
        while len(a) > 1 and not a[-1]: a.pop()
    return q, a


def scalar_factors(f):
    remaining, factors = f, []
    for degree in range(1, len(f)//2+1):
        for coeff in product(range(5), repeat=degree):
            g = list(coeff)+[1]
            while len(remaining) >= len(g):
                q, r = scalar_div(remaining, g)
                if r != [0]: break
                factors.append(g)
                remaining = q
    if len(remaining) > 1: factors.append(remaining)
    return factors


def lift(p, root):
    dp = deriv(p)
    x = root
    for _ in range(2): x = R.sub(x, R.mul(R.ev(p, x), R.inv(R.ev(dp, x))))
    assert R.ev(p, x) == R.zero
    assert tuple(v % 5 for v in x) == root
    return x


def label(a):
    b = R25.pow(tuple(x % 25 for x in a), Q-1)
    assert tuple(x % 5 for x in b) == K.one
    return tuple(((x-int(i == 0)) % 25)//5 for i, x in enumerate(b))


def fifth_root(a):
    """Return a root mod 125, or reject by the exact mod-25 invariant."""
    if label(a) != K.zero: return None
    t = K.pow(tuple(x % 5 for x in a), 5**10)
    t5 = R.pow(t, 5)
    u = R.mul(a, R.inv(t5))
    assert tuple(x % 25 for x in u) == R25.one
    w = tuple(((x-int(i == 0)) % 125)//25 for i, x in enumerate(u))
    root = R.mul(t, R.add(R.one, R.scale(w, 5)))
    assert R.pow(root, 5) == a
    return root


def main():
    source_path = BASE.parent/'five-isogeny-modular-norm/norm-certificate.json'
    src = json.loads(source_path.read_text())['polynomials_ascending']
    a, b, d, h, J = [src[k] for k in ['a', 'b', 'd', 'h', 'jcoef']]
    checks, factors, roots, records, classes = {}, {}, {}, [], []
    # F_s coefficients are reconstructed by integer polynomial multiplication.
    def imul(p, q):
        v = [0]*(len(p)+len(q)-1)
        for i, x in enumerate(p):
            for j, y in enumerate(q): v[i+j] += x*y
        return v
    h3 = imul(imul(h, h), h)
    def fs(s): return [h3[i]+(s*J[i] if i < len(J) else 0)
                             -(s*s*d[i] if i < len(d) else 0)
                             for i in range(13)]
    # Prove the ring's residue polynomial is irreducible by the prime-degree test.
    frobenius, z = [T], T
    for _ in range(N):
        z = K.pow(z, 5)
        frobenius.append(z)
    Hk = [K.c(v) for v in H]
    checks['model_frobenius_closes'] = z == T
    checks['model_no_linear_factor'] = pgcd(Hk, psub([K.zero]*5+[K.one], [K.zero, K.one])) == [K.one]
    checks['model_squarefree'] = pgcd(Hk, [K.c(v) for v in deriv(H)]) == [K.one]
    for r in [2, 4]:
        F = fs(r)
        fk = [K.c(v) for v in F]
        assert F[0] % 5 == 0
        hr = [v % 5 for v in F[1:]]
        if r == 4:
            sf = scalar_factors([v % 5 for v in F])
            prod = [K.one]
            for fac in sf: prod = pmul(prod, [K.c(v) for v in fac])
            checks['4_complete_factorization'] = prod == fk
            checks['4_two_linear_factors'] = [0, 1] in sf and [4, 1] in sf
            checks['4_no_degree_eleven'] = max(len(fac)-1 for fac in sf) < 11
            checks['4_squarefree_b_unit'] = pgcd(fk, [K.c(v) for v in deriv(F)]) == [K.one] and pgcd(fk, [K.c(v) for v in b]) == [K.one]
            irreducibility = []
            for fac in sf:
                degree = len(fac)-1
                fkfac = [K.c(v) for v in fac]
                z, seq = [K.zero, K.one], [[K.zero, K.one]]
                for _ in range(degree):
                    z = ppow(z, 5, fkfac)
                    seq.append(z)
                start = pdiv([K.zero, K.one], fkfac)[1]
                primes = [p for p in range(2, degree+1) if degree % p == 0 and all(p % q for q in range(2, p))]
                gcds = [pgcd(fkfac, psub(seq[degree//p], start)) for p in primes]
                okay = z == start and all(g == [K.one] for g in gcds)
                checks[f'4_factor_{len(irreducibility)}_irreducible'] = okay
                irreducibility.append({'factor': fac, 'frobenius': seq, 'proper_degree_gcds': gcds})
            factors['4'] = {'F_mod5': [v % 5 for v in F], 'factors': sf,
                            'irreducibility': irreducibility,
                            'excluded': 'Two distinct linear factors; every lifted factor has degree below eleven.'}
            continue
        rr = sorted(frobenius[:N]); trials = []
        roots[r] = rr
        checks[f'{r}_eleven_distinct_roots'] = len(rr) == len(set(rr)) == N
        checks[f'{r}_root_equations'] = all(K.ev(hr, x) == K.zero and x != K.zero for x in rr)
        orbit = [rr[0]]
        for _ in range(N-1): orbit.append(K.pow(orbit[-1], 5))
        checks[f'{r}_full_frobenius_orbit'] = set(orbit) == set(rr) and K.pow(orbit[-1], 5) == orbit[0]
        prod = [K.one]
        for x in [K.zero]+rr: prod = pmul(prod, [K.neg(x), K.one])
        checks[f'{r}_complete_factorization'] = prod == fk
        checks[f'{r}_simple_roots_b_units'] = all(K.ev(deriv(F), x) != K.zero and K.ev(b, x) != K.zero for x in [K.zero]+rr)
        factors[str(r)] = {'F_mod5': [v % 5 for v in F], 'linear': [0, 1],
                           'degree_eleven': hr, 'roots': rr,
                           'frobenius_orbit': orbit, 'splitting_trials': trials}
    if not all(checks.values()): raise ArithmeticError(str(checks))
    # Validate the removable chart exactly; no division by d at x=16.
    ev = lambda p, x: sum(v*x**i for i, v in enumerate(p))
    checks['removable_F16_linear'] = ev(h3, 16) == 121*ev(J, 16)
    checks['removable_b_unit'] = ev(b, 16) % 5 != 0
    checks['removable_y'] = -ev(a, 16) == -61*ev(b, 16)
    # The already source-audited identity is checked afresh over Z[X].
    identity = imul(a, a)
    terms = [imul(a, b), imul(imul(b, b), src['g']), imul(d, h3)]
    full = [0]*24
    for i, v in enumerate(identity): full[i] += v
    for sign, term in zip([-1, -1, 1], terms):
        for i, v in enumerate(term): full[i] += sign*v
    checks['integer_elimination_identity'] = full == [0]*24
    collisions = []
    for s in range(125):
        if s % 5 not in roots: continue
        F = fs(s)
        units = []
        for i, x0 in enumerate(roots[s % 5]):
            x = lift(F, x0)
            y = R.mul(R.sub(R.scale(R.ev(d, x), s), R.ev(a, x)), R.inv(R.ev(b, x)))
            f = R.add(R.mul(R.sub(x, R.c(4)), y), R.add(R.scale(R.mul(x, x), -4), R.add(R.scale(x, 30), R.c(-55))))
            assert R.sub(R.add(R.mul(y, y), y), R.ev(src['g'], x)) == R.zero
            assert tuple(v % 5 for v in f) != K.zero
            units.append(f)
            records.append({'s': s, 'embedding': i, 'residue_x': x0, 'x': x,
                            'y': y, 'f': f, 'label': label(f)})
        norm = R.one
        for f in units: norm = R.mul(norm, f)
        assert norm[1:] == (0,)*(N-1) and norm[0] % 5
        rational = 121*pow(norm[0], -1, 125) % 125
        for row in records[-N:]:
            row['norm'] = norm[0]
            row['rational_representative'] = rational
            found = next((j for j, cls in enumerate(classes) if cls['label'] == row['label']), None)
            if found is None:
                found = len(classes)
                classes.append({'label': row['label'], 'representative_record': len(records)-N+row['embedding'],
                                'f': row['f'], 'rational_representative': rational, 'members': []})
            cls = classes[found]
            ratio = R.mul(row['f'], R.inv(cls['f']))
            witness = fifth_root(ratio)
            assert witness is not None
            qr = rational*pow(cls['rational_representative'], -1, 125) % 125
            rational_witness = next((w for w in range(125) if w % 5 and pow(w, 5, 125) == qr), None)
            assert rational_witness is not None
            idx = len(records)-N+row['embedding']
            row['class_index'] = found
            cls['members'].append(idx)
            collisions.append({'record': idx, 'class': found, 'U_fifth_root': witness,
                               'Q5_fifth_root': rational_witness})
        print('Completed scalar', s, 'classes so far', len(classes), flush=True) if s in [22, 47, 72, 97, 124] else None
    noncollisions = []
    for cls in classes:
        explicit = R.add(R.one, R.scale(cls['label'], -5))
        witness = fifth_root(R.mul(cls['f'], R.inv(explicit)))
        assert witness is not None and label(explicit) == cls['label']
        cls['explicit_U_representative'] = explicit
        cls['explicit_representative_fifth_root'] = witness
    for i, cls in enumerate(classes):
        for j in range(i):
            diff = tuple((x-y) % 5 for x, y in zip(cls['label'], classes[j]['label']))
            pivot = next(k for k, v in enumerate(diff) if v)
            noncollisions.append({'i': i, 'j': j, 'coordinate': pivot, 'difference': diff[pivot]})
    checks['all_scalar_embedding_pairs'] = len(records) == 25*N == 275
    checks['all_collision_witnesses'] = len(collisions) == len(records)
    checks['all_noncollision_pairs'] = len(noncollisions) == len(classes)*(len(classes)-1)//2
    checks['all_members_retained'] = sorted(i for cls in classes for i in cls['members']) == list(range(275))
    checks['all_explicit_representatives'] = len(classes) == 55 and all(label(cls['explicit_U_representative']) == cls['label'] for cls in classes)
    checks['nonempty_below_prior_bound'] = 0 < len(classes) <= 600
    out = {'model': {'H': H, 'modulus': 125, 'residue_order': Q,
                     'frobenius': frobenius}, 'source_polynomials': src,
           'factors': factors, 'records': records, 'classes': classes,
           'collisions': collisions, 'noncollisions': noncollisions,
           'summary': {'candidate_pairs': len(records), 'exact_class_count': len(classes),
                       'required_pairs': 275, 'excluded_scalar_residue': 4, 'prior_upper_bound': 600,
                       'checks': len(checks)},
           'checks': checks, 'failures': [k for k, v in checks.items() if not v]}
    path = BASE/'certificate.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print('Result:', out['summary'], 'failures:', out['failures'])
    print('Certificate:', path.relative_to(BASE.parent.parent))
    assert not out['failures']


if __name__ == '__main__': main()
