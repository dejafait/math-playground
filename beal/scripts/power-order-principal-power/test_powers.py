"""Approved bounded test; stdlib exact arithmetic, full inclusion evidence.

Run from beal: python3 scripts/power-order-principal-power/test_powers.py
All matrices use columns in (1,k,...,k^11), except named LLL row matrices.
No enumeration completeness, class nonvanishing or maximal-order claim.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import platform
import traceback

N = 12
M = [-380, -774, -1062, -456, 258, 468, 104, -126, -6, 6, -6, 0, 1]
HS = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12]
OUT = Path(__file__).with_name('power-test-certificate.json')


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def tr(a):
    return [list(x) for x in zip(*a)]


def mm(a, b):
    bt = tr(b)
    return [[sum(x*y for x, y in zip(row, col)) for col in bt] for row in a]


def inv(a):
    n = len(a)
    c = [[F(x) for x in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for j in range(n):
        p = next(i for i in range(j, n) if c[i][j])
        c[j], c[p] = c[p], c[j]
        d = c[j][j]
        c[j] = [x/d for x in c[j]]
        for i in range(n):
            if i != j and c[i][j]:
                d = c[i][j]
                c[i] = [x-d*y for x, y in zip(c[i], c[j])]
    return [row[n:] for row in c]


def det(a):
    c = [row[:] for row in a]
    n, prev, sign = len(c), 1, 1
    for j in range(n-1):
        p = next((i for i in range(j, n) if c[i][j]), None)
        if p is None:
            return 0
        if p != j:
            c[j], c[p] = c[p], c[j]
            sign = -sign
        pivot = c[j][j]
        for i in range(j+1, n):
            for k in range(j+1, n):
                num = c[i][k]*pivot-c[i][j]*c[j][k]
                assert num % prev == 0
                c[i][k] = num//prev
            c[i][j] = 0
        prev = pivot
    return sign*c[-1][-1]


def ints(a):
    assert all(F(x).denominator == 1 for row in a for x in row)
    return [[int(x) for x in row] for row in a]


def reduce_poly(c):
    c = c[:] + [0]*max(0, N-len(c))
    for j in range(len(c)-1, N-1, -1):
        d = c[j]
        for i in range(N):
            c[j-N+i] -= d*M[i]
    return c[:N]


POWERS = [reduce_poly([0]*i+[1]) for i in range(2*N-1)]


def mul(a, b):
    c = [0]*N
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            if y:
                for t, z in enumerate(POWERS[i+j]):
                    c[t] += x*y*z
    return c


R = eye(N)
T = tr([POWERS[i+1] for i in range(N)])


def multiplication(a):
    return tr([mul(a, col) for col in tr(R)])


def product(a, b):
    return tr([mul(x, y) for x in tr(a) for y in tr(b)])


def egcd(a, b):
    r, s, t, rr, ss, tt = a, 1, 0, b, 0, 1
    while rr:
        q = r//rr
        r, rr = rr, r-q*rr
        s, ss = ss, s-q*ss
        t, tt = tt, t-q*tt
    if r < 0:
        r, s, t = -r, -s, -t
    assert s*a+t*b == r and r > 0
    return r, s, t


def compress(gens, label):
    """Integer column elimination; proof is the two verified inclusions."""
    cols = tr(gens)
    q = len(cols)
    coeff = tr(eye(q))
    p = q-1
    for row in range(N-1, -1, -1):
        for j in range(p):
            a, b = cols[p][row], cols[j][row]
            if not b:
                continue
            g, s, t = egcd(a, b)
            cp, cj = cols[p][:], cols[j][:]
            xp, xj = coeff[p][:], coeff[j][:]
            cols[p] = [s*x+t*y for x, y in zip(cp, cj)]
            cols[j] = [(-b//g)*x+(a//g)*y for x, y in zip(cp, cj)]
            coeff[p] = [s*x+t*y for x, y in zip(xp, xj)]
            coeff[j] = [(-b//g)*x+(a//g)*y for x, y in zip(xp, xj)]
        assert cols[p][row] != 0, 'rank defect'
        if cols[p][row] < 0:
            cols[p] = [-x for x in cols[p]]
            coeff[p] = [-x for x in coeff[p]]
        assert all(cols[j][row] == 0 for j in range(p))
        p -= 1
    assert all(x == 0 for col in cols[:p+1] for x in col)
    basis = tr(cols[p+1:])
    x = tr(coeff[p+1:])
    y = ints(mm(inv(basis), gens))
    assert mm(gens, x) == basis
    assert mm(basis, y) == gens
    stability = ints(mm(mm(inv(basis), T), basis))
    assert mm(T, basis) == mm(basis, stability)
    determinant = det(basis)
    assert determinant
    return basis, {'label': label, 'generators': gens, 'basis': basis,
                   'basis_in_generators': x, 'generators_in_basis': y,
                   'k_action': stability, 'determinant': determinant,
                   'rank': N, 'required_rank': N, 'inclusions_verified': True}


def gs(rows):
    orth, norms = [], []
    mu = [[F(0) for _ in rows] for _ in rows]
    for i, row in enumerate(rows):
        v = [F(x) for x in row]
        for j, w in enumerate(orth):
            mu[i][j] = sum(F(x)*y for x, y in zip(row, w))/norms[j]
            v = [x-mu[i][j]*y for x, y in zip(v, w)]
        orth.append(v)
        norms.append(sum(x*x for x in v))
        assert norms[-1] > 0
    return mu, norms


def lll(basis):
    original = tr(basis)
    rows = [row[:] for row in original]
    u = eye(N)
    k, steps = 1, 0
    while k < N:
        steps += 1
        assert steps <= 20000, 'LLL implementation iteration cap'
        mu, norms = gs(rows)
        for j in range(k-1, -1, -1):
            z = (mu[k][j]+F(1, 2)).numerator//(mu[k][j]+F(1, 2)).denominator
            if z:
                rows[k] = [x-z*y for x, y in zip(rows[k], rows[j])]
                u[k] = [x-z*y for x, y in zip(u[k], u[j])]
                mu, norms = gs(rows)
        if norms[k] >= (F(3, 4)-mu[k][k-1]**2)*norms[k-1]:
            k += 1
        else:
            rows[k], rows[k-1] = rows[k-1], rows[k]
            u[k], u[k-1] = u[k-1], u[k]
            k = max(1, k-1)
    assert mm(u, original) == rows
    du = det(u)
    assert abs(du) == 1
    ui = ints(inv(u))
    assert mm(ui, rows) == original
    mu, norms = gs(rows)
    assert all(abs(mu[i][j]) <= F(1, 2) for i in range(N) for j in range(i))
    assert all(norms[i] >= (F(3,4)-mu[i][i-1]**2)*norms[i-1] for i in range(1,N))
    return tr(rows), {'original_rows': original, 'reduced_rows': rows,
                      'transformation': u, 'inverse_transformation': ui,
                      'transformation_determinant': du, 'delta': F(3,4),
                      'gram_schmidt_mu': mu, 'gram_schmidt_squared_norms': norms,
                      'steps': steps, 'checks_passed': True}


def encode(x):
    if isinstance(x, F):
        return {'numerator': x.numerator, 'denominator': x.denominator}
    raise TypeError(type(x))


def save(data):
    OUT.write_text(json.dumps(data, default=encode, indent=2)+'\n')


def main():
    data = {'status': 'IN_PROGRESS', 'python': platform.python_version(),
            'backend': 'stdlib integers/Fraction; exact two-inclusion verified compression',
            'polynomial_ascending': M, 'exponents': HS,
            'maximum_candidates_per_exponent': 144, 'maximum_candidates': 1440,
            'actual_candidates': 0, 'required_rank': N, 'powers': [],
            'tests': [], 'successes': [], 'failures': [],
            'L058_identity': 'NOT_RUN', 'mathematical_conclusion': 'NONE'}
    save(data)
    try:
        generators = [ [11*x for x in row] + [T[i][j]-8*R[i][j] for j in range(N)]
                       for i, row in enumerate(R)]
        jb, cert = compress(generators, 'J')
        data['powers'].append(cert)
        assert abs(det(jb)) == 11
        power = jb
        for h in range(1, 13):
            if h > 1:
                power, cert = compress(product(power, jb), f'J^{h}')
                data['powers'].append(cert)
            assert abs(det(power)) == 11**h
            if h not in HS:
                continue
            reduced, reduction = lll(power)
            rb = tr(reduced)
            candidates = [(f'b{i+1}', b) for i,b in enumerate(rb)]
            for i in range(N):
                for j in range(i+1, N):
                    candidates.append((f'b{i+1}+b{j+1}', [x+y for x,y in zip(rb[i],rb[j])]))
                    candidates.append((f'b{i+1}-b{j+1}', [x-y for x,y in zip(rb[i],rb[j])]))
            assert len(candidates) == 144
            inverse_power = inv(power)
            test = {'h': h, 'reduction': reduction, 'candidates': [],
                    'actual_rank': N, 'required_rank': N}
            data['tests'].append(test)
            for name, beta in candidates:
                assert any(beta)
                mb = multiplication(beta)
                inclusion = ints(mm(inverse_power, mb))
                assert mm(power, inclusion) == mb
                d = det(inclusion)
                assert d != 0
                eq = abs(d) == 1
                record = {'name': name, 'beta': beta, 'principal_in_power': inclusion,
                          'index_of_principal_in_power': abs(d), 'whole_lattice_equal': eq}
                if eq:
                    reverse = ints(inv(inclusion))
                    assert mm(mb, reverse) == power
                    record['power_in_principal'] = reverse
                    data['successes'].append({'h': h, 'beta': beta, 'candidate': name})
                test['candidates'].append(record)
                data['actual_candidates'] += 1
            save(data)
            print(f'h={h}: rank 12/12, index {11**h}/{11**h}, exact compression/reduction PASS; '
                  f'candidates 144/144; principal equalities '
                  f'{sum(c["whole_lattice_equal"] for c in test["candidates"])}', flush=True)
            if data['successes']:
                data['status'] = 'PRINCIPAL_POWER_FOUND_REQUIRES_L058_VERIFICATION'
                save(data)
                break
        else:
            data['status'] = 'BOUNDED_LIST_EXHAUSTED'
        data['candidate_rejections'] = data['actual_candidates']-len(data['successes'])
        save(data)
    except Exception as exc:
        data['status'] = 'IMPLEMENTATION_DEFECT'
        data['failures'].append({'error': repr(exc), 'traceback': traceback.format_exc()})
        save(data)
        raise
    print(f'{data["status"]}: candidates {data["actual_candidates"]}/1440; '
          f'L058 identity {data["L058_identity"]}; failures {len(data["failures"])}')
    print('Certificate:', OUT)


if __name__ == '__main__':
    main()
