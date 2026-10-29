#!/usr/bin/env python3
"""One saved-history survivor; no block rank tests or cover mutations."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
S = [1, 8, 12, 18, 22, 27, 33]
J = [47, 50, 64, 70, 75, 79, 85, 89, 96]
HISTORY = [0, 51, 98, 177, 318]
PAIRS = list(combinations(range(7), 2))


def main():
    paths = ['scripts/pair-free-envelope/cover.json',
             'scripts/pair-free-envelope/verification.json',
             'scripts/residual-domination/verification.json']
    cover, prior, occurrence = [json.loads((ROOT/p).read_text()) for p in paths]
    node, span = cover['nodes'][1006], cover['spans'][274]
    failures = []

    def check(ok, name):
        if not ok:
            failures.append(name)

    check(cover['modulus'] == 97 and cover['S'] == S and cover['J'] == J,
          'parameters')
    check(node['id'] == 1006 and node['history'] == HISTORY and node['span'] == 274,
          'node_binding')
    check(prior['summary']['failures'] == [], 'prior_verification_failures')
    check(prior['summary']['certificate_sha256'] == sha256((ROOT/paths[0]).read_bytes()).hexdigest(),
          'prior_verification_binding')
    check(prior['spans'][274]['kernel_basis'] == span['kernel_basis'], 'saved_kernel_binding')
    check(any(n['id'] == 1006 and n['history'] == HISTORY and n['span'] == 274
              for n in occurrence['branch_arrow_nodes']), 'occurrence_binding')
    u, v = [1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0]
    p = [(u[a]*v[b]-u[b]*v[a]) % 97 for a,b in PAIRS]
    check(p == span['kernel_basis'][2] and any(p), 'nonzero_saved_wedge')
    plucker = []
    for a,b,c,d in combinations(range(7), 4):
        P = dict(zip(PAIRS, p))
        plucker.append((P[a,b]*P[c,d]-P[a,c]*P[b,d]+P[a,d]*P[b,c]) % 97)
    check(not any(plucker), 'all_plucker_equations')
    rows = []
    for label in HISTORY:
        I = list(combinations(S, 2))[label//36]
        K = list(combinations(J, 2))[label % 36]
        O = sorted(set(S)-set(I))
        z = min(O)
        roots = sorted(set(J)-set(K))

        def g(x):
            y = 1
            for root in roots:
                y = y*(x-root) % 97
            return y

        Q = [[(g(z)*(a == x)-g(x)*(a == z)) % 97 for a in S] for x in O[1:]]
        N = [[(Q[i][a]*Q[j][b]-Q[i][b]*Q[j][a]) % 97 for a,b in PAIRS]
             for i,j in combinations(range(4), 2)]
        saved = cover['universe'][label]
        check(list(I) == saved['I'] and list(K) == saved['K']
              and Q == saved['Q'] and N == saved['N'], f'original_maps_{label}')
        qu = [sum(a*b for a,b in zip(row,u)) % 97 for row in Q]
        qv = [sum(a*b for a,b in zip(row,v)) % 97 for row in Q]
        minors = [(qu[i]*qv[j]-qu[j]*qv[i]) % 97 for i,j in combinations(range(4),2)]
        residuals = [sum(a*b for a,b in zip(row,p)) % 97 for row in N]
        nonzero = next(((i,c,x) for c,col in enumerate([qu,qv])
                        for i,x in enumerate(col) if x), None)
        check(not any(minors) and not any(residuals) and nonzero is not None,
              f'exact_rank_one_{label}')
        rows.append(dict(label=label, I=I, K=K, z=z, roots=roots,
                         g_on_S=[g(x) for x in S], Q=Q, N=N,
                         Q_U=qu, Q_V=qv, restriction_minors=minors,
                         block_residuals=residuals, nonzero_entry=nonzero))
    out = dict(modulus=97, S=S, J=J, history=HISTORY, node=1006, span=274,
               input_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
               script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
               saved_generating_history=span['generating_history'],
               saved_kernel_basis=span['kernel_basis'], U=u, V=v, wedge=p,
               plucker_residuals=plucker, rows=rows,
               summary=dict(outcome='SURVIVOR' if not failures else 'FAILED',
                            failures=failures, exact_rank_one_actual=len(rows),
                            exact_rank_one_required=5, plucker_actual=len(plucker),
                            plucker_required=35, block_residual_actual=6*len(rows),
                            block_residual_required=30, field='F_97',
                            extension_irreducibility='Not needed: prime field',
                            all_chart_emptiness_claimed=False, new_block_rank_tests=0,
                            cover_modified=False, frontier_obligations_retained=1665))
    (HERE/'survivor.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out['summary'], sort_keys=True))
    print('Full certificate: scripts/span-274-geometry/survivor.json')
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())
