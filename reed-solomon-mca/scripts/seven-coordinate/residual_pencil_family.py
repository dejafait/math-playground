"""One structurally selected original quadruple; exact family certificate.

No sample of projective parameters is used to prove the family identities.
"""
from itertools import combinations, product
from pathlib import Path
import json

import zero_anchor_support_filter as direct

P = 97
KEYS = [((1, 8), (89, 96)), ((12, 33), (64, 85)),
        ((12, 27), (50, 70)), ((18, 22), (75, 79))]


def rref(matrix):
    a = [[v % P for v in row] for row in matrix]
    pivots, rank = [], 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank,len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, P)
        a[rank] = [v*inv % P for v in a[rank]]
        for i in range(len(a)):
            if i != rank:
                c = a[i][col]
                a[i] = [(v-c*w) % P for v,w in zip(a[i],a[rank])]
        pivots.append(col)
        rank += 1
    free = [j for j in range(len(a[0])) if j not in pivots]
    basis = []
    for f in free:
        v = [0]*len(a[0])
        v[f] = 1
        for i,c in enumerate(pivots):
            v[c] = -a[i][f] % P
        basis.append(v)
    return dict(rank=rank,pivots=pivots,free_columns=free,rref=a,kernel_basis=basis)


def apply(matrix, v):
    return [sum(a*b for a,b in zip(row,v)) % P for row in matrix]


def run():
    failures = []
    # The first surviving singleton assignment has the first two rows
    # reversed relative to KEYS. Solve its remaining singleton equation.
    B,D,A,C = 9,40,45,74
    a,b,c,d = 52,88,23,57
    def ratio(n,den):
        return n*pow(den % P,-1,P) % P
    u, w = ratio(D-c,D-a), ratio(C-d,C-a)
    numerator = (ratio(w,B-d)-ratio(1,B-a)) % P
    denominator = (ratio(u,B-c)-ratio(1,B-a)) % P
    old_t = ratio(numerator,denominator)
    t = pow(old_t,-1,P)
    if t in (0,1):
        failures.append('Forbidden cross-ratio')
    blocks = [direct.block(*key) for key in KEYS]
    Q = [block['covectors'] for block in blocks]
    matrix = ([row+[0]*7 for row in Q[0]] + [[0]*7+row for row in Q[1]]
              + [row+row for row in Q[2]]
              + [row+[t*v % P for v in row] for row in Q[3]])
    linear = rref(matrix)
    basis = linear['kernel_basis']
    residuals = [apply(matrix,v) for v in basis]
    if linear['rank'] != 12 or len(basis) != 2 or any(map(any,residuals)):
        failures.append('Required two-dimensional family kernel not established')
    free_matrix = [[v[c] for c in linear['free_columns']] for v in basis]
    if free_matrix != [[1,0],[0,1]]:
        failures.append('Family parameter independence failed')
    pair_certificates = []
    for i,j in ((0,1),(2,3)):
        stacked = Q[i]+Q[j]
        rank, rows = direct.rank_and_rows(stacked)
        minor = [stacked[r] for r in rows]
        det = direct.integer_determinant(minor) if rank == 7 else 0
        if rank != 7 or det % P == 0:
            failures.append(f'Pair {i,j} disjointness not established')
        pair_certificates.append(dict(rows=[i,j],stacked_matrix=stacked,
                                      actual_rank=rank,required_rank=7,
                                      minor_row_indices=rows,minor=minor,
                                      integer_determinant=det,residue=det%P))
    # Independently reconstruct each actual row by its defining formula.
    independent_Q = []
    for I,K in KEYS:
        vals = []
        for r in direct.S:
            val = 1
            for z in direct.J:
                if z not in K:
                    val = val*(r-z) % P
            vals.append(val)
        observed = [i for i,r in enumerate(direct.S) if r not in I]
        pivot = observed[0]
        independent_Q.append([[((vals[pivot] if col == r else 0)
                                -(vals[r] if col == pivot else 0)) % P
                               for col in range(7)] for r in observed[1:]])
    if independent_Q != Q:
        failures.append('Independent actual-map reconstruction disagrees')
    universe = list(product(combinations(direct.S,2),combinations(direct.J,2)))
    labels = [universe.index(k) for k in KEYS]
    supports = [set(I+K) for I,K in KEYS]
    intersections = [sorted(supports[i]&supports[j]) for i,j in combinations(range(4),2)]
    eligible = (not intersections[0] and not intersections[5]
                and max(map(len,intersections)) <= 1
                and labels[0] < labels[1] and labels[2] < labels[3])
    if not eligible:
        failures.append('Original-domain eligibility failed')
    family = [dict(x=v[:7],y=v[7:]) for v in basis]
    out = dict(modulus=P,S=direct.S,J=direct.J,keys=KEYS,labels_zero_based=labels,
               intersections=intersections,eligible=eligible,
               discovery=dict(B=B,D=D,A=A,C=C,s=[a,b,c,d],u=u,w=w,
                              numerator=numerator,denominator=denominator,old_t=old_t),
               t=t,blocks=blocks,matrix=matrix,linear=linear,kernel_residuals=residuals,
               parameter_identity=free_matrix,family=family,pair_certificates=pair_certificates,
               independent_map_check=(independent_Q==Q),failures=failures)
    path = Path(__file__).with_name('residual-pencil-family.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(f'Eligible original labels: {labels}; cross-ratio t={t}')
    print(f'Combined kernel dimension: actual {14-linear["rank"]}, required 2; '
          f'parameter independence {free_matrix == [[1,0],[0,1]]}')
    print(f'Pair stacked ranks: actual {[r["actual_rank"] for r in pair_certificates]}, required [7,7]; '
          f'minor residues {[r["residue"] for r in pair_certificates]}')
    print(f'All basis-vector identity residuals zero: {not any(map(any,residuals))}; failures: {failures}')
    print(f'Full certificate: {path}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
