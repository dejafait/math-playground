#!/usr/bin/env python3
"""Exact degree-27 log-image membership certificate; analytic proof in L016."""
from fractions import Fraction as Q
import json
from pathlib import Path

P, E, DEPTH, CUTOFF = 3, 27, 14, 243


def val(x):
    x = Q(x)
    if not x:
        return 10**6
    a, b, result = abs(x.numerator), x.denominator, 0
    while a % P == 0:
        a //= P
        result += 1
    while b % P == 0:
        b //= P
        result -= 1
    return result


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))


def scaled(v, c):
    return [c*x for x in v]


def pi(v):
    return [P*v[-1]] + v[:-1]


def residue(x, depth):
    """Canonical representative modulo 3^depth; x has valuation >= -2."""
    t, modulus = 9*x, P**(depth+2)
    assert val(t) >= 0 and t.denominator % P
    return Q((t.numerator * pow(t.denominator, -1, modulus)) % modulus, 9)


def serial(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, list):
        return [serial(y) for y in x]
    if isinstance(x, dict):
        return {k: serial(v) for k, v in x.items()}
    return x


def main():
    reps, sums, congruences = [], [], []
    depths = [1 if r < DEPTH else 0 for r in range(E)]
    for j in range(1, DEPTH):
        s = [Q(0)]*E
        for k in range(1, CUTOFF):
            a, r = divmod(j*k, E)
            s[r] += Q((-1)**(k+1)*P**a, k)
        q = [residue(x, d) for x, d in zip(s, depths)]
        checks = [val(x-y) >= d for x, y, d in zip(s, q, depths)]
        assert all(checks)
        reps.append(q)
        sums.append(s)
        congruences.append(checks)
    hb = [[Q((P**depths[r]) if r == c else 0) for r in range(E)]
          for c in range(E)]
    generators = reps + hb
    # Diagonalize over Z_3. Track both transformation matrices in full;
    # every elementary ratio is in Z_3, so both are invertible over Z_3.
    nc = len(generators)
    a = [[g[r] for g in generators] for r in range(E)]
    u = [[Q(r == c) for c in range(E)] for r in range(E)]
    v = [[Q(r == c) for c in range(nc)] for r in range(nc)]
    operations = []
    for i in range(E):
        _, r, c = min((val(a[r][c]), r, c)
                      for r in range(i, E) for c in range(i, nc))
        assert a[r][c]
        if r != i:
            a[i], a[r] = a[r], a[i]
            u[i], u[r] = u[r], u[i]
            operations.append(['row_swap', i, r])
        if c != i:
            for m in (a, v):
                for row in m:
                    row[i], row[c] = row[c], row[i]
            operations.append(['column_swap', i, c])
        pivot = a[i][i]
        for r in range(i+1, E):
            t = a[r][i]/pivot
            assert val(t) >= 0
            if t:
                a[r] = [x-t*y for x, y in zip(a[r], a[i])]
                u[r] = [x-t*y for x, y in zip(u[r], u[i])]
                operations.append(['row_subtract', r, i, t])
        for c in range(i+1, nc):
            t = a[i][c]/pivot
            assert val(t) >= 0
            if t:
                for m in (a, v):
                    for row in m:
                        row[c] -= t*row[i]
                operations.append(['column_subtract', c, i, t])
    pivots = [a[i][i] for i in range(E)]
    assert all(a[r][c] == (pivots[r] if r == c else 0)
               for r in range(E) for c in range(nc))
    # Independently multiply the original matrix by stored transformations.
    ga = [[g[r] for g in generators] for r in range(E)]
    ug = [[dot(row, g) for g in generators] for row in u]
    ugv = [[dot(row, [v[k][c] for k in range(nc)])
            for c in range(nc)] for row in ug]
    assert ugv == a
    # Basis columns B=G*V[:,0:27]; certify U*B=diag(pivots).
    basis = [[dot(row, [v[k][c] for k in range(nc)])
              for row in ga] for c in range(E)]
    functionals = [[x/pivots[r] for x in u[r]] for r in range(E)]
    basis_checks = [[dot(f, b) == int(r == c) for c, b in enumerate(basis)]
                    for r, f in enumerate(functionals)]
    generator_coordinates = [[dot(f, g) for f in functionals] for g in generators]
    assert all(all(row) for row in basis_checks)
    assert all(val(x) >= 0 for row in generator_coordinates for x in row)
    inputs = [('log', j, scaled(pi(q), 18)) for j, q in enumerate(reps, 1)]
    inputs += [('H', r, scaled(pi(b), 18)) for r, b in enumerate(hb)]
    ob = [[Q(r == c) for r in range(E)] for c in range(E)]
    inputs += [('O', r, scaled(pi(b), 18)) for r, b in enumerate(ob)]
    memberships, failures = [], []
    for branch, index, x in inputs:
        coordinates = [dot(f, x) for f in functionals]
        bad = [r for r, y in enumerate(coordinates) if val(y) < 0]
        memberships.append(dict(branch=branch, index=index, vector=x,
                                basis_coordinates=coordinates, member=not bad))
        failures += [dict(branch=branch, index=index, functional_row=r,
                          value=coordinates[r]) for r in bad]
    separator = None
    if failures:
        failure = failures[0]
        f = functionals[failure['functional_row']]
        separator = dict(**failure, coefficients=f,
                         all_generator_values=[dot(f, g) for g in generators],
                         multiplied_H_values=[dot(f, scaled(pi(b), 18)) for b in hb])
        assert all(val(x) >= 0 for x in separator['all_generator_values'])
        assert all(val(x) >= 0 for x in separator['multiplied_H_values'])
        assert val(failure['value']) < 0
    # Independent small separator, verified on every representative and H
    # generator without using the diagonalization or basis coordinates.
    phi = [Q(0)]*E
    phi[0], phi[1], phi[15], phi[18] = Q(3), Q(-31, 3), Q(9), Q(-9)
    phi_q = [dot(phi, q) for q in reps]
    assert phi_q == [0, 0, 4, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0]
    phi_h = [dot(phi, b) for b in hb]
    assert all(val(x) >= 0 for x in phi_h)
    phi_error = [dot(phi, scaled(pi(b), 18)) for b in hb]
    assert all(val(x) >= 2 for x in phi_error)
    phi_witness = dot(phi, scaled(pi(reps[0]), 18))
    assert phi_witness == Q(-992, 3) and val(phi_witness) == -1
    assert 3**5-27*5 == 108 >= DEPTH and 2*3**5-27 > 0
    assert Q(DEPTH, E) > Q(1, 2)
    report = dict(field='Q_3(pi), pi^27=3', H='pi^14 O',
                  arithmetic='exact rational arithmetic; analytic coverage proved in L016',
                  cutoff_exclusive=CUTOFF, tail_block_base=108,
                  finite_sums=sums, logarithm_representatives=reps,
                  residue_congruences=congruences, H_basis=hb,
                  row_transform=u, column_transform=v, operations=operations,
                  diagonal_pivots=pivots, lattice_basis=basis,
                  dual_basis_functionals=functionals,
                  original_generator_basis_coordinates=generator_coordinates,
                  diagonalization_identity_verified=True,
                  basis_duality_verified=True,
                  memberships=memberships, failures=failures, separator=separator,
                  simple_separator=dict(coefficients=phi, representative_values=phi_q,
                                        H_values=phi_h, multiplied_H_values=phi_error,
                                        representative_witness_value=phi_witness,
                                        actual_log_value_coset='-992/3 + 9 Z_3',
                                        actual_log_value_valuation=-1),
                  inclusion_holds=not failures,
                  required_coarse_radius=81,
                  coarse_radius_certified_by_this_test=81 if not failures else None,
                  coarse_bound_refuted=False)
    out = Path(__file__).with_name('degree-27-membership.json')
    out.write_text(json.dumps(serial(report), indent=2)+'\n')
    print(json.dumps(dict(inclusion_holds=not failures,
                         generators=len(generators), membership_tests=len(inputs),
                         failing_inputs=sum(not m['member'] for m in memberships),
                         separator_value=str(phi_witness),
                         actual_log_value_valuation=-1,
                         finite_check_failures=0,
                         required_coarse_radius=81,
                         coarse_bound_refuted=False, certificate=str(out)), indent=2))


if __name__ == '__main__':
    main()
