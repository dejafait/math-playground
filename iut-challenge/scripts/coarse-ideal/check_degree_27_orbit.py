#!/usr/bin/env python3
"""Exact full-orbit certificate, using the complete logarithm image in L016.

Analytic completeness and group saturation are proved in L017, not sampled here.
"""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

N = 27


def val(x):
    x = Q(x)
    if not x:
        return 10**6
    a, b, v = abs(x.numerator), x.denominator, 0
    while a % 3 == 0:
        a //= 3
        v += 1
    while b % 3 == 0:
        b //= 3
        v -= 1
    return v


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(c) for c in zip(*a)]


def matmul(a, b):
    return [[dot(row, c) for c in transpose(b)] for row in a]


def mv(a, v):
    return [dot(row, v) for row in a]


def scale(v, q):
    return [q*x for x in v]


def pi(v):
    return [3*v[-1]] + v[:-1]


def field_val(v):
    return min(Q(val(x))+Q(r, N) for r, x in enumerate(v) if x)


def parse_matrix(a):
    return [[Q(x) for x in row] for row in a]


def primitive_reduction(c):
    """Return A and its inverse over Z_3 with A*c=e_0."""
    assert min(map(val, c)) == 0
    j = next(i for i, x in enumerate(c) if val(x) == 0)
    s = eye(N)
    s[0], s[j] = s[j], s[0]
    d = mv(s, c)
    unit = d[0]
    r = eye(N)
    ri = eye(N)
    r[0][0], ri[0][0] = 1/unit, unit
    for i in range(1, N):
        r[i][0] = -d[i]/unit
        ri[i][0] = d[i]
    a, ai = matmul(r, s), matmul(s, ri)
    assert matmul(a, ai) == eye(N) == matmul(ai, a)
    assert mv(a, c) == [Q(i == 0) for i in range(N)]
    assert all(val(x) >= 0 for m in (a, ai) for row in m for x in row)
    return a, ai


def serial(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, list):
        return [serial(y) for y in x]
    if isinstance(x, dict):
        return {k: serial(v) for k, v in x.items()}
    return x


def main():
    source = Path(__file__).with_name('degree-27-membership.json')
    raw = source.read_bytes()
    old = json.loads(raw)
    reps = parse_matrix(old['logarithm_representatives'])
    hb = parse_matrix(old['H_basis'])
    gens = reps + hb
    original = transpose(gens)
    a, u, v = [row[:] for row in original], eye(N), eye(len(gens))
    # Replay every elementary operation; invertibility follows from swaps and
    # integral elementary subtractions, rather than from a stored success flag.
    for op in old['operations']:
        kind, i, j = op[:3]
        if kind == 'row_swap':
            a[i], a[j] = a[j], a[i]
            u[i], u[j] = u[j], u[i]
        elif kind == 'column_swap':
            for m in (a, v):
                for row in m:
                    row[i], row[j] = row[j], row[i]
        elif kind == 'row_subtract':
            t = Q(op[3])
            assert val(t) >= 0
            for m in (a, u):
                m[i] = [x-t*y for x, y in zip(m[i], m[j])]
        elif kind == 'column_subtract':
            t = Q(op[3])
            assert val(t) >= 0
            for m in (a, v):
                for row in m:
                    row[i] -= t*row[j]
        else:
            raise AssertionError(kind)
    assert u == parse_matrix(old['row_transform'])
    assert v == parse_matrix(old['column_transform'])
    pivots = [Q(x) for x in old['diagonal_pivots']]
    assert a == [[pivots[r] if r == c else Q(0)
                  for c in range(len(gens))] for r in range(N)]
    assert matmul(matmul(u, original), v) == a
    basis = transpose(matmul(original, v)[:])[:N]
    f = [[x/pivots[r] for x in u[r]] for r in range(N)]
    assert basis == parse_matrix(old['lattice_basis'])
    assert f == parse_matrix(old['dual_basis_functionals'])
    assert matmul(f, transpose(basis)) == eye(N)
    all_coords = [mv(f, x) for x in gens]
    assert all(val(x) >= 0 for c in all_coords for x in c)
    # Full input coverage is pi times the exact generating lattices, not a
    # sample of logarithms or automorphisms.
    ob = eye(N)
    branch_data = {}
    for name, inputs in [('O', ob), ('J', gens)]:
        vectors = [pi(x) for x in inputs]
        coords = [scale(mv(f, x), Q(6)) for x in vectors]
        contents = [min(map(val, c)) for c in coords]
        branch_data[name] = dict(vectors=vectors, I_coordinates=coords,
                                 contents=contents, minimum_content=min(contents))
    cmin = min(b['minimum_content'] for b in branch_data.values())
    ib = [scale(b, Q(1, 6)) for b in basis]
    generator_vals = [field_val(g) for g in gens]
    jmin = min(generator_vals)
    imin = jmin-1
    orbit_min = imin+cmin
    assert orbit_min.denominator == 1
    radius = Q(3)**(-int(orbit_min))
    # Choose an attained minimal-content input and an I-basis field extreme.
    branch = min(branch_data, key=lambda k: branch_data[k]['minimum_content'])
    ix = branch_data[branch]['contents'].index(cmin)
    x = branch_data[branch]['vectors'][ix]
    primitive_x = scale(x, Q(3)**(-cmin))
    cx = scale(mv(f, primitive_x), Q(6))
    ti = next(i for i, b in enumerate(ib) if field_val(b) == imin)
    t = ib[ti]
    ct = [Q(i == ti) for i in range(N)]
    ax, aix = primitive_reduction(cx)
    at, ait = primitive_reduction(ct)
    m, mi = matmul(ait, ax), matmul(aix, at)
    assert matmul(m, mi) == eye(N) == matmul(mi, m)
    assert all(val(q) >= 0 for mat in (m, mi) for row in mat for q in row)
    assert mv(m, cx) == ct
    bmat = transpose(ib)
    binv = [[6*q for q in row] for row in f]
    g = matmul(matmul(bmat, m), binv)
    gi = matmul(matmul(bmat, mi), binv)
    assert matmul(g, gi) == eye(N) == matmul(gi, g)
    witness = mv(g, x)
    assert witness == scale(t, Q(3)**cmin)
    assert field_val(witness) == orbit_min
    assert matmul(matmul(binv, g), bmat) == m
    # A second, compact witness avoids dependence on the diagonalized basis.
    # a(y)=27*c_0/8 and b(y)=-3*phi(y)/496 split z=q_1/6 and w=9*pi*q_1.
    phi = [Q(0)]*N
    phi[0], phi[1], phi[15], phi[18] = Q(3), Q(-31, 3), Q(9), Q(-9)
    af = [Q(0)]*N
    af[0] = Q(27, 8)
    bf = scale(phi, Q(-3, 496))
    w, z = scale(pi(reps[0]), Q(9)), scale(reps[0], Q(1, 6))
    assert [dot(af, z), dot(af, w), dot(bf, z), dot(bf, w)] == [1, 0, 0, 1]
    for functional in (af, bf):
        assert all(val(dot(functional, scale(q, Q(1, 6)))) >= 0 for q in gens)
    delta, functional = [s-t for s, t in zip(w, z)], [s-t for s, t in zip(af, bf)]
    involution = [[Q(r == c)+delta[r]*functional[c] for c in range(N)] for r in range(N)]
    assert dot(functional, delta) == -2
    assert matmul(involution, involution) == eye(N)
    assert mv(involution, w) == z and mv(involution, z) == w
    im = matmul(matmul(binv, involution), bmat)
    assert all(val(q) >= 0 for row in im for q in row)
    sharp = mv(involution, pi(reps[0]))
    assert sharp == scale(reps[0], Q(1, 54))
    assert field_val(sharp) == orbit_min
    error_vectors = [mv(involution, pi(h)) for h in hb]
    error_vals = [field_val(y) for y in error_vectors]
    assert min(error_vals) >= -2
    summary = dict(branch_contents={k: b['minimum_content'] for k, b in branch_data.items()},
                   minimum_J_valuation=jmin, minimum_I_valuation=imin,
                   orbit_lattice_scaling_exponent=cmin,
                   orbit_minimum_field_valuation=orbit_min,
                   actual_radius=radius, required_radius=81,
                   radius_ratio=radius/81, witness_branch=branch,
                   witness_generator_index=ix, target_I_basis_index=ti,
                   coarse_bound_violated=radius > 81,
                   verification_failures=0)
    report = dict(summary=summary,
                  input_certificate_sha256=hashlib.sha256(raw).hexdigest(),
                  replayed_operations=old['operations'],
                  J_basis=basis, J_dual_basis=f, I_basis=ib,
                  branch_data=branch_data, J_generator_field_valuations=generator_vals,
                  witness_input=x, witness_primitive_I_coordinates=cx,
                  target_primitive_vector=t, automorphism_I_coordinates=m,
                  inverse_I_coordinates=mi, automorphism_field_coordinates=g,
                  inverse_field_coordinates=gi, attained_witness=witness,
                  compact_involution=dict(a=af, b=bf, w=w, z=z,
                                          field_matrix=involution, I_matrix=im,
                                          attained_witness=sharp,
                                          logarithm_tail_image_generators=error_vectors,
                                          logarithm_tail_image_valuations=error_vals,
                                          actual_infinite_log_witness_valuation=orbit_min),
                  qualifications='L016 proves infinite log coverage; L017 proves full-group saturation; no original IUT realization')
    out = Path(__file__).with_name('degree-27-orbit.json')
    out.write_text(json.dumps(serial(report), indent=2)+'\n')
    print(json.dumps(serial(dict(**summary, certificate=str(out))), indent=2))


if __name__ == '__main__':
    main()
