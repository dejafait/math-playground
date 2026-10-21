#!/usr/bin/env python3
"""Exact prime-field diagnostics for the selected-support criterion L020."""
import json
from pathlib import Path

Q = 65537
N = 1024
K = 64
OUT = Path(__file__).with_name("triple-support-rank-results.json")


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % Q
    return c


def root_product(points):
    p = [1]
    for x in points:
        p = mul(p, [-x % Q, 1])
    return p


def evaluate(p, x):
    value = 0
    for a in reversed(p):
        value = (value * x + a) % Q
    return value


def rref(a):
    a = [[x % Q for x in row] for row in a]
    pivots = []
    for col in range(len(a[0])):
        pivot = next((i for i in range(len(pivots), len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        row = len(pivots)
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, Q)
        a[row] = [x * inv % Q for x in a[row]]
        for i in range(len(a)):
            if i != row:
                scale = a[i][col]
                a[i] = [(x - scale * y) % Q for x, y in zip(a[i], a[row])]
        pivots.append(col)
    return a, pivots


def determinant(a):
    return (a[0][0] * (a[1][1]*a[2][2] - a[1][2]*a[2][1])
            - a[0][1] * (a[1][0]*a[2][2] - a[1][2]*a[2][0])
            + a[0][2] * (a[1][0]*a[2][1] - a[1][1]*a[2][0])) % Q


def diagnostic(h, pairs, construct):
    flat = sum(pairs, [])
    assert len(set(flat)) == 6 and all(x in h for x in flat)
    remaining = [x for x in h if x not in flat]
    core = remaining[:61]
    unique = [remaining[61+3*i:64+3*i] for i in range(3)]
    u12, u23, u31 = pairs
    supports = [core + u12 + u31 + unique[0],
                core + u12 + u23 + unique[1],
                core + u23 + u31 + unique[2]]
    ss = list(map(set, supports))
    assert all(len(s) == 68 for s in ss)
    assert ss[0] & ss[1] & ss[2] == set(core)
    for i, j, pair in [(0, 1, u12), (1, 2, u23), (2, 0, u31)]:
        assert (ss[i] & ss[j]) - set(core) == set(pair)
    polynomials = [root_product(pair) for pair in pairs]
    matrix = [[p[row] for p in polynomials] for row in range(3)]
    reduced, pivots = rref(matrix)
    det = determinant(matrix)
    # Separate two-point coefficient formula checks determinant expansion.
    sums = [sum(pair) % Q for pair in pairs]
    products = [pair[0] * pair[1] % Q for pair in pairs]
    formula = ((sums[1]-sums[0])*(products[2]-products[0])
               - (sums[2]-sums[0])*(products[1]-products[0])) % Q
    assert formula == det
    assert (len(pivots) == 3) == (det != 0)
    record = dict(pairs=pairs, core=core, unique=unique, supports=supports,
                  overlap_quadratics_constant_first=polynomials,
                  coefficient_matrix_constant_first=matrix,
                  rref=reduced, rank=len(pivots), determinant=det,
                  determinant_pair_formula=formula)
    if not construct:
        assert len(pivots) == 3
        record["realizable"] = False
        return record
    assert len(pivots) == 2 and pivots == [0, 1]
    kernel = [-reduced[0][2] % Q, -reduced[1][2] % Q, 1]
    assert all(kernel)
    assert all(sum(x*y for x, y in zip(row, kernel)) % Q == 0 for row in matrix)
    # Independent antipodal relation: (p23-p31, p31-p12, p12-p23).
    antipodal_kernel = [(products[1]-products[2]) % Q,
                        (products[2]-products[0]) % Q,
                        (products[0]-products[1]) % Q]
    assert all(antipodal_kernel)
    assert all(sum(x*y for x, y in zip(row, antipodal_kernel)) % Q == 0 for row in matrix)
    g = root_product(core)
    f1 = [0]
    f2 = [(-kernel[0]*x) % Q for x in mul(g, polynomials[0])]
    f3 = [(kernel[2]*x) % Q for x in mul(g, polynomials[2])]
    messages = [f1, f2, f3]
    assert all(len(f) <= K for f in messages) and len({tuple(f) for f in messages}) == 3
    values = [[evaluate(f, x) for x in h] for f in messages]
    center = []
    for index, x in enumerate(h):
        owners = [i for i, s in enumerate(ss) if x in s]
        assert len({values[i][index] for i in owners}) <= 1
        center.append(values[owners[0]][index] if owners else 0)
    agreements = [[x for j, x in enumerate(h) if values[i][j] == center[j]]
                  for i in range(3)]
    assert all(ss[i] <= set(agreements[i]) for i in range(3))
    pair_equalities = []
    for i, j, pair in [(0, 1, u12), (1, 2, u23), (2, 0, u31)]:
        equal = [x for z, x in enumerate(h) if values[i][z] == values[j][z]]
        assert set(equal) == set(core + pair) and len(equal) == K-1
        assert values[i] != values[j]
        pair_equalities.append(equal)
    assert [len(a) for a in agreements] == [1016, 68, 68]
    record.update(realizable=True, kernel=kernel, antipodal_kernel=antipodal_kernel,
                  common_root_polynomial_constant_first=g,
                  message_coefficients_constant_first=messages,
                  message_values=values, center_values=center,
                  full_agreement_sets=agreements,
                  full_agreement_counts=list(map(len, agreements)),
                  pairwise_equality_sets=pair_equalities)
    return record


def main():
    generator = pow(3, 64, Q)
    assert pow(generator, N, Q) == 1 and pow(generator, N//2, Q) == Q-1
    h = [pow(generator, i, Q) for i in range(N)]
    assert len(set(h)) == N
    antipodal = [[h[i], -h[i] % Q] for i in range(3)]
    consecutive = [[h[2*i], h[2*i+1]] for i in range(3)]
    cases = {"antipodal": diagnostic(h, antipodal, True),
             "consecutive": diagnostic(h, consecutive, False)}
    certificate = dict(field_order=Q, domain_size=N, message_dimension=K,
                       generator=generator, domain=h, cases=cases, failures=[],
                       required_agreements=68, established_list_lower_bound=3,
                       threshold_numerator=Q**28, threshold_denominator=2**128,
                       threshold_closed_ball_check=3*2**128 <= Q**28,
                       scope="Exact E-field examples; every m follows by zero-row embedding. No maximum or threshold safety conclusion.")
    OUT.write_text(json.dumps(certificate, indent=2) + "\n")
    for name, case in cases.items():
        print(f"{name}: rank={case['rank']}, determinant={case['determinant']}, realizable={case['realizable']}")
    print(f"antipodal actual agreements={cases['antipodal']['full_agreement_counts']}; required=68 each")
    print("established list lower bound=3; required unsafe bound >65537^28/2^128; threshold not reached")
    print(f"failures=[]; full certificate: {OUT}")


if __name__ == "__main__":
    main()
