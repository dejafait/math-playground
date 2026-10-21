"""One fixed ideal, one reduced order-lattice basis; exact norm certificates.

Rounded embeddings select candidates only. No LLL theorem, maximal-order
basis, principal-ideal decision or completeness claim depends on them.
"""
import json
from fractions import Fraction
from itertools import permutations
from pathlib import Path

import numpy as np

from check_affine import M, F, mul, norm, determinant

BASE = Path(__file__).resolve().parent
N = 36


def identity():
    return [[int(i == j) for j in range(N)] for i in range(N)]


def residue(v, k, t):
    return sum(v[12*j+i]*pow(k, i, 11)*pow(t, j, 11)
               for j in range(3) for i in range(12)) % 11


def order_lattice():
    rows = identity()
    for i in (0, 12):
        rows[i][i] = 11
    for q in range(N):
        if q in (0, 12):
            continue
        i, j = q % 12, q // 12
        a, b = pow(8, i, 11)*pow(6, j, 11), pow(8, i, 11)*pow(3, j, 11)
        ct = ((a-b)*4+5) % 11-5
        c0 = (b-3*ct+5) % 11-5
        rows[q][0], rows[q][12] = -c0, -ct
    return rows


def matrix_product(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def gram_schmidt(gram):
    mu = [[Fraction(0) for _ in range(N)] for _ in range(N)]
    lengths = []
    for i in range(N):
        for j in range(i):
            mu[i][j] = (gram[i][j]-sum(mu[i][l]*mu[j][l]*lengths[l]
                                      for l in range(j)))/lengths[j]
        length = gram[i][i]-sum(mu[i][l]**2*lengths[l] for l in range(i))
        assert length > 0, 'Rounded embedding matrix has deficient rank'
        lengths.append(length)
    return mu, lengths


def reduce_basis(gram):
    mu, lengths = gram_schmidt(gram)
    trans = identity()
    k, swaps, reductions = 1, 0, 0
    while k < N and swaps < 10000:
        for j in range(k-1, -1, -1):
            q = round(mu[k][j])
            if q:
                trans[k] = [x-q*y for x, y in zip(trans[k], trans[j])]
                for l in range(j):
                    mu[k][l] -= q*mu[j][l]
                mu[k][j] -= q
                reductions += 1
        if lengths[k] >= (Fraction(3, 4)-mu[k][k-1]**2)*lengths[k-1]:
            k += 1
            continue
        old_mu = mu[k][k-1]
        combined = lengths[k]+old_mu**2*lengths[k-1]
        mu[k][k-1] = old_mu*lengths[k-1]/combined
        lengths[k] = lengths[k-1]*lengths[k]/combined
        lengths[k-1] = combined
        trans[k], trans[k-1] = trans[k-1], trans[k]
        for j in range(k-1):
            mu[k][j], mu[k-1][j] = mu[k-1][j], mu[k][j]
        for i in range(k+1, N):
            old = mu[i][k]
            mu[i][k] = mu[i][k-1]-old_mu*old
            mu[i][k-1] = old+mu[k][k-1]*mu[i][k]
        swaps += 1
        k = max(1, k-1)
    return trans, dict(swaps=swaps, reductions=reductions, cap=10000,
                       completed=k == N)


def relative_norm(v):
    # Multiplication by a+b*t+c*t^2 in K[t]/(t^3-t^2+t+1).
    blocks = [v[12*j:12*j+12] for j in range(3)]
    columns = []
    for shift in range(3):
        out = [[0]*12 for _ in range(5)]
        for j in range(3):
            out[j+shift] = blocks[j][:]
        for j in range(4, 2, -1):
            for l in range(3):
                out[j-3+l] = [x-F[l]*y for x, y in zip(out[j-3+l], out[j])]
        columns.append(out[:3])
    result = [0]*12
    for p in permutations(range(3)):
        sign = (-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))
        term = [1]+[0]*11
        for i in range(3):
            term = mul(term, columns[p[i]][i], M)
        result = [x+sign*y for x, y in zip(result, term)]
    return result


def absolute_matrix(v):
    # Independent full degree-36 regular representation.
    columns = []
    for tj in range(3):
        for ki in range(12):
            out = [0]*36
            for j in range(3):
                kt = mul(v[12*j:12*j+12], [0]*ki+[1], M)
                tt = mul([0]*j+[1], [0]*tj+[1], F)
                for l in range(3):
                    for h in range(12):
                        out[12*l+h] += tt[l]*kt[h]
            columns.append(out)
    return [list(row) for row in zip(*columns)]


def main():
    initial = order_lattice()
    assert abs(determinant(initial)) == 121
    assert all(residue(v, 8, 6) == residue(v, 8, 3) == 0 for v in initial)
    # All 36 embeddings; using real and imaginary parts retains conjugates.
    kr = np.roots(list(reversed(M)))
    tr = np.roots(list(reversed(F)))
    embeddings = [(complex(k), complex(t)) for k in kr for t in tr]
    rounded = []
    for j in range(3):
        for i in range(12):
            values = [k**i*t**j for k, t in embeddings]
            rounded.append([round(c*10**6) for z in values for c in (z.real, z.imag)])
    search_basis = matrix_product(initial, rounded)
    gram = [[sum(x*y for x, y in zip(a, b)) for b in search_basis] for a in search_basis]
    transform, reduction = reduce_basis(gram)
    final = matrix_product(transform, initial)
    checks = dict(initial_index_121=abs(determinant(initial)) == 121,
                  transformation_unimodular=abs(determinant(transform)) == 1,
                  final_index_121=abs(determinant(final)) == 121,
                  all_residue_memberships=all(residue(v, 8, 6) == residue(v, 8, 3) == 0 for v in final),
                  exactly_36_distinct_candidates=len({tuple(v) for v in final}) == 36)
    candidates, hits = [], []
    for i, v in enumerate(final):
        rel = relative_norm(v)
        tower = norm(rel, M)
        direct = determinant(absolute_matrix(v))
        row = dict(index=i, coefficients_k_then_t=v, relative_norm=rel,
                   absolute_norm=tower, independent_absolute_norm=direct,
                   residue_pair=[residue(v, 8, 6), residue(v, 8, 3)],
                   generator_norm=abs(tower) == 121)
        candidates.append(row)
        checks[f'norm_agreement_{i}'] = tower == direct != 0
        checks[f'ideal_norm_divides_{i}'] = tower % 121 == 0
        if row['generator_norm']:
            hits.append(i)
    failures = [key for key, passed in checks.items() if not passed]
    summary = dict(candidates=36, required_generator_absolute_norm=121,
                   generator_hits=hits, required_separating_units=1,
                   minimum_candidate_absolute_norm=min(abs(row['absolute_norm']) for row in candidates),
                   failures=failures, checks_passed=sum(checks.values()),
                   checks_total=len(checks), reduction=reduction,
                   scope='Only 36 final basis rows in I intersect Z[k,t]; no nonprincipality conclusion')
    result = dict(summary=summary, field_polynomials=dict(K=M, cubic=F),
                  basis_order='k^i*t^j at index 12*j+i', initial_basis=initial,
                  rounded_embedding_matrix=rounded, transformation=transform,
                  final_basis=final, candidates=candidates, checks=checks)
    path = BASE/'fixed-ideal-certificate.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(summary, indent=2))
    print('Certificate:', path.relative_to(BASE.parent.parent))
    assert not failures


if __name__ == '__main__':
    main()
