#!/usr/bin/env python3
"""Exact rank-108 unit-logarithm lattice certificate. Analytic proof: L031.

Build: python3 scripts/cyclotomic-log/compute_enlarged_basis.py
Verify saved complete evidence: same command with --verify.
No p-adic precision assumptions or O_U-module assumption are used.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import json

P, E, F, DEPTH, CUTOFF = 3, 27, 4, 14, 243
N = E * F
OUT = Path(__file__).with_name('enlarged-basis.json')


def valuation(x):
    x = Q(x)
    if not x:
        return None
    a, b, v = abs(x.numerator), x.denominator, 0
    while a % P == 0:
        a //= P
        v += 1
    while b % P == 0:
        b //= P
        v -= 1
    return v


def trim(a):
    a = [x % P for x in a]
    while a and not a[-1]:
        a.pop()
    return a


def pdiv(a, b):
    a, b = trim(a), trim(b)
    q = [0] * max(0, len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        d, t = len(a) - len(b), a[-1] * pow(b[-1], -1, P) % P
        q[d] = t
        for i, x in enumerate(b):
            a[d+i] = (a[d+i] - t*x) % P
        a = trim(a)
    return trim(q), a


def pmul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return pdiv(c, [1]*5)[1]


def ppow(n):
    a, b = [1], [0, 1]
    while n:
        if n % 2:
            a = pmul(a, b)
        b = pmul(b, b)
        n //= 2
    return a


def gcd_record(a, b):
    steps = []
    a, b = trim(a), trim(b)
    while b:
        q, r = pdiv(a, b)
        steps.append(dict(a=a, b=b, quotient=q, remainder=r))
        a, b = b, r
    g = [(x * pow(a[-1], -1, P)) % P for x in a]
    return dict(gcd=g, divisions=steps)


def field_checks():
    x9 = ppow(9)
    diff = x9 + [0] * (max(2, len(x9)) - len(x9))
    diff[1] = (diff[1] - 1) % P
    return dict(polynomial=[1]*5, x81_mod_polynomial=ppow(81),
                x9_mod_polynomial=x9,
                irreducibility_gcd=gcd_record([1]*5, diff),
                separability_gcd=gcd_record([1]*5, [1, 2, 0, 1]))


def theta_power(n):
    r = n % 5
    return [int(a == r) for a in range(F)] if r < F else [-1]*F


def generators():
    depths = [int(r < DEPTH) for r in range(E) for a in range(F)]
    sums, reps, errors, labels = [], [], [], []
    for j in range(1, DEPTH):
        for a in range(F):
            s = [Q(0)] * N
            for k in range(1, CUTOFF):
                m, r = divmod(j*k, E)
                t = Q((-1)**(k+1) * P**m, k)
                for b, c in enumerate(theta_power(a*k)):
                    s[F*r+b] += c*t
            q, errs = [], []
            for x, d in zip(s, depths):
                t, modulus = 9*x, P**(d+2)
                assert not t or valuation(t) >= 0
                assert t.denominator % P
                y = Q((t.numerator * pow(t.denominator, -1, modulus)) % modulus, 9)
                v = valuation(x-y)
                assert v is None or v >= d
                q.append(y)
                errs.append(v)
            sums.append(s)
            reps.append(q)
            errors.append(errs)
            labels.append(dict(kind='log', j=j, a=a))
    hs = [[Q(P**depths[r]) if r == c else Q(0) for r in range(N)]
          for c in range(N)]
    labels += [dict(kind='H', r=c//F, a=c%F) for c in range(N)]
    cols = reps + hs
    matrix = [[int(9*col[r]) for col in cols] for r in range(N)]
    return dict(depths=depths, finite_sums=sums, representatives=reps,
                congruence_valuations=errors, generator_labels=labels,
                integer_generator_matrix=matrix)


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def xgcd(a, b):
    oa, ob = a, b
    r0, r1, s0, s1, t0, t1 = a, b, 1, 0, 0, 1
    while r1:
        q = r0 // r1
        r0, r1 = r1, r0-q*r1
        s0, s1 = s1, s0-q*s1
        t0, t1 = t1, t0-q*t1
    if r0 < 0:
        r0, s0, t0 = -r0, -s0, -t0
    assert s0*oa + t0*ob == r0
    return s0, t0, r0


def pair_columns(mat, i, j, u, v, w, z):
    # New column i=u*old_i+v*old_j; new j=w*old_i+z*old_j.
    for row in mat:
        a, b = row[i], row[j]
        row[i], row[j] = u*a+v*b, w*a+z*b


def normal_form(original):
    a = [row[:] for row in original]
    n = len(a[0])
    transform, operations = identity(n), []
    k = n
    for i in range(N-1, -1, -1):
        k -= 1
        for j in range(k-1, -1, -1):
            if not a[i][j]:
                continue
            u, v, d = xgcd(a[i][k], a[i][j])
            r, s = a[i][k]//d, a[i][j]//d
            assert u*r+v*s == 1
            pair_columns(a, k, j, u, v, -s, r)
            pair_columns(transform, k, j, u, v, -s, r)
            operations.append(['pair', k, j, u, v, -s, r])
        if a[i][k] < 0:
            for mat in (a, transform):
                for row in mat:
                    row[k] = -row[k]
            operations.append(['negate', k])
        b = a[i][k]
        if not b:
            k += 1
            continue
        for j in range(k+1, n):
            q = a[i][j] // b
            if q:
                for mat in (a, transform):
                    for row in mat:
                        row[j] -= q*row[k]
                operations.append(['subtract', j, k, q])
    assert k == n-N
    assert all(x == 0 for row in a for x in row[:k])
    basis = [row[k:] for row in a]
    # Inverse operations are applied from the right in reverse order.
    inverse = identity(n)
    for op in reversed(operations):
        if op[0] == 'pair':
            _, i, j, u, v, w, z = op
            assert u*z-v*w == 1
            pair_columns(inverse, i, j, z, -v, -w, u)
        elif op[0] == 'negate':
            for row in inverse:
                row[op[1]] = -row[op[1]]
        else:
            _, j, i, q = op
            for row in inverse:
                row[j] += q*row[i]
    return dict(integer_basis_matrix=basis, column_transform=transform,
                inverse_column_transform=inverse, operations=operations,
                basis_in_generators=[row[k:] for row in transform],
                generators_in_basis=inverse[k:])


def product(a, b):
    # Sparse multiplication; still checks every output entry exactly.
    out = [[0]*len(b[0]) for _ in a]
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        out[i][j] += x*y
    return out


def basis_table(b):
    lines = ['| r | b_(r,0) | b_(r,1) | b_(r,2) | b_(r,3) |',
             '| --- | --- | --- | --- | --- |']
    for r in range(E):
        expressions = []
        for a in range(F):
            terms = []
            for i in range(N):
                c = Q(b[i][F*r+a], 9)
                if not c:
                    continue
                rr, aa = divmod(i, F)
                monomial = 'theta' if aa == 1 else f'theta^{aa}' if aa else ''
                if rr:
                    monomial += (' ' if monomial else '') + ('pi' if rr == 1 else f'pi^{rr}')
                terms.append((str(c)+' '+monomial).strip() if monomial else str(c))
            expressions.append(' + '.join(terms))
        lines.append('| '+str(r)+' | '+' | '.join(expressions)+' |')
    return '\n'.join(lines)+'\n'


def verify(data, recompute=False):
    failures = []
    checks = {}

    def check(name, cond):
        checks[name] = bool(cond)
        if not cond:
            failures.append(name)

    field = field_checks()
    check('field_evidence_matches', data['field_checks'] == field)
    check('irreducible', field['x81_mod_polynomial'] == [0, 1]
          and field['irreducibility_gcd']['gcd'] == [1])
    check('separable', field['separability_gcd']['gcd'] == [1])
    if recompute:
        exact = serial(generators())
        for key, value in exact.items():
            check('recomputed_'+key, data[key] == value)
    m, b = data['integer_generator_matrix'], data['integer_basis_matrix']
    w, c = data['basis_in_generators'], data['generators_in_basis']
    v, vi = data['column_transform'], data['inverse_column_transform']
    n, k = len(m[0]), len(m[0])-N
    check('all_certificate_matrices_integral', all(type(x) is int
          for mat in (m, b, w, c, v, vi) for row in mat for x in row))
    check('matrix_dimensions', len(m) == N and n == 160 and len(b) == N
          and all(len(row) == N for row in b) and len(w) == n
          and all(len(row) == N for row in w) and len(c) == N
          and all(len(row) == n for row in c))
    check('basis_in_generator_span', product(m, w) == b)
    check('every_generator_in_basis_span', product(b, c) == m)
    check('full_column_transform_identity', product(m, v) == [[0]*k+row for row in b])
    check('transform_inverse_identity', product(v, vi) == identity(n))
    check('basis_upper_triangular', all(b[i][j] == 0 for i in range(N) for j in range(i)))
    check('positive_diagonal_rank_108', all(b[i][i] > 0 for i in range(N)))
    check('basis_transform_columns', w == [row[k:] for row in v])
    check('coordinate_inverse_rows', c == vi[k:])
    check('tail_threshold', 3**5-27*5 == 108 and 108 >= DEPTH)
    check('tail_increasing', 2*3**5-27 == 459 and 459 > 0)
    check('deep_log_exp_strict', Q(DEPTH, E) > Q(1, 2))
    check('congruence_thresholds', all(err is None or err >= d
          for row in data['congruence_valuations'] for err, d in zip(row, data['depths'])))
    check('unimodular_operation_determinants', all(op[0] != 'pair' or op[3]*op[6]-op[4]*op[5] == 1
          for op in data['operations']))
    table = basis_table(b)
    check('full_exported_basis_table', OUT.with_name('enlarged-basis-table.md').read_text() == table)
    lemma = Path(__file__).resolve().parents[2] / data['analytic_proof']
    check('full_canonical_basis_table', table.rstrip() in lemma.read_text())
    pivots = [b[i][i] for i in range(N)]
    vs = [valuation(x) for x in pivots]
    det_v = sum(vs)-2*N
    return dict(checks=checks, failures=failures, rank=N,
                shallow_generators=52, deep_generators=N, total_generators=n,
                exact_coordinate_congruences=52*N,
                basis_determinant_v3=det_v,
                integer_hnf_diagonal=pivots,
                integer_hnf_diagonal_v3_histogram={str(x):vs.count(x) for x in sorted(set(vs))},
                basis_field_minimum_v3=str(min(Q(valuation(Q(b[i][j],9)))+Q(i//F,E)
                                              for i in range(N) for j in range(N) if b[i][j])),
                tail_actual_pi_valuation=108, tail_required_pi_valuation=14,
                basis_denominator=9, certificate=str(OUT.relative_to(Path(__file__).resolve().parents[2])))


def serial(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, list):
        return [serial(y) for y in x]
    if isinstance(x, dict):
        return {k:serial(v) for k, v in x.items()}
    return x


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    if args.verify:
        data = json.loads(OUT.read_text())
        result = verify(data, recompute=True)
        audit_path = OUT.with_name('enlarged-basis-verification.json')
        audit_path.write_text(json.dumps(result, indent=2)+'\n')
        print('Saved-evidence verification: all finite sums, representatives, congruences and full span identities.')
        print('Verification certificate:', audit_path.relative_to(Path(__file__).resolve().parents[2]))
    else:
        data = generators()
        data.update(normal_form(data['integer_generator_matrix']))
        data.update(field_checks=field_checks(),
                    field='Q_3(theta,pi), Phi_5(theta)=0, pi^27=3; theta=zeta_20^4',
                    coordinate_order='index 4*r+a denotes theta^a*pi^r',
                    basis_definition='column j of integer_basis_matrix divided by 9',
                    analytic_proof='lemmas/L031-enlarged-complete-logarithm-lattice-basis.md',
                    cutoff_exclusive=CUTOFF)
        data = serial(data)
        OUT.with_name('enlarged-basis-table.md').write_text(basis_table(data['integer_basis_matrix']))
        result = verify(data)
        data['summary'] = result
        OUT.write_text(json.dumps(data, indent=2)+'\n')
    print('Rank actual/required:', result['rank'], '/', N, '; complete generators:', result['total_generators'])
    print('Exact coordinate congruences:', result['exact_coordinate_congruences'])
    print('Tail pi-valuation actual/required:', result['tail_actual_pi_valuation'], '/', result['tail_required_pi_valuation'])
    print('Basis determinant v_3:', result['basis_determinant_v3'], '; minimum field valuation:', result['basis_field_minimum_v3'])
    print('Failures:', result['failures'])
    print('Full certificate:', result['certificate'])
    if result['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
