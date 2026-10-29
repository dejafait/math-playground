#!/usr/bin/env python3
"""Independent polynomial expansion and all-minor check of the one survivor."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def main():
    data = json.loads((HERE/'survivor.json').read_text())
    failures, evidence = [], []

    def check(ok, name):
        if not ok:
            failures.append(name)

    S = [1,8,12,18,22,27,33]
    J = [47,50,64,70,75,79,85,89,96]
    labels = [0,51,98,177,318]
    pairs = list(combinations(S, 2))
    check(data['modulus'] == 97 and data['S'] == S and data['J'] == J
          and data['history'] == labels and data['node'] == 1006 and data['span'] == 274,
          'fixed_parameters')
    for path,digest in data['input_sha256'].items():
        check(sha256((ROOT/path).read_bytes()).hexdigest() == digest, 'input_hash_'+path)
    cover = json.loads((ROOT/'scripts/pair-free-envelope/cover.json').read_text())
    check(cover['nodes'][1006]['history'] == labels and cover['nodes'][1006]['span'] == 274,
          'node_binding')
    check(data['saved_kernel_basis'] == cover['spans'][274]['kernel_basis'], 'kernel_binding')
    u = dict(zip(S, data['U']))
    v = dict(zip(S, data['V']))
    p = {(a,b):(u[a]*v[b]-u[b]*v[a]) % 97 for a,b in pairs}
    check(data['wedge'] == [p[a,b] for a,b in pairs]
          == [int((a,b) == (1,22)) for a,b in pairs], 'specified_nonzero_wedge')
    plucker = [(p[a,b]*p[c,d]-p[a,c]*p[b,d]+p[a,d]*p[b,c]) % 97
               for a,b,c,d in combinations(S,4)]
    check(len(plucker) == 35 and plucker == data['plucker_residuals']
          and all(x == 0 for x in plucker), 'complete_plucker_check')
    check([r['label'] for r in data['rows']] == labels, 'complete_row_list')
    for label,record in zip(labels, data['rows']):
        I = list(combinations(S,2))[label//36]
        K = list(combinations(J,2))[label % 36]
        roots = [x for x in J if x not in K]
        # Expand the polynomial first, then use Horner evaluation.
        poly = [1]
        for root in roots:
            new = [0]*(len(poly)+1)
            for i,c in enumerate(poly):
                new[i] = (new[i]-root*c) % 97
                new[i+1] = (new[i+1]+c) % 97
            poly = new

        def g(x):
            value = 0
            for c in reversed(poly):
                value = (value*x+c) % 97
            return value

        O = [x for x in S if x not in I]
        z = O[0]
        covectors = [{a:(int(a == x)*g(z)-int(a == z)*g(x)) % 97
                      for a in S} for x in O[1:]]
        Q = [[c[a] for a in S] for c in covectors]
        N = [[(c[a]*d[b]-c[b]*d[a]) % 97 for a,b in pairs]
             for c,d in combinations(covectors,2)]
        qu = [(g(z)*u[x]-g(x)*u[z]) % 97 for x in O[1:]]
        qv = [(g(z)*v[x]-g(x)*v[z]) % 97 for x in O[1:]]
        minors = [(qu[i]*qv[j]-qu[j]*qv[i]) % 97 for i,j in combinations(range(4),2)]
        residuals = [sum(row[k]*p[a,b] for k,(a,b) in enumerate(pairs)) % 97 for row in N]
        check(list(I) == record['I'] and list(K) == record['K'] and z == record['z']
              and roots == record['roots'] and [g(x) for x in S] == record['g_on_S']
              and Q == record['Q'] == cover['universe'][label]['Q']
              and N == record['N'] == cover['universe'][label]['N'], f'all_coefficients_{label}')
        check(qu == record['Q_U'] and qv == record['Q_V']
              and minors == record['restriction_minors'] and not any(minors)
              and residuals == record['block_residuals'] and not any(residuals),
              f'all_equations_{label}')
        i,col,value = record['nonzero_entry']
        check(value != 0 and [qu,qv][col][i] == value, f'rank_not_zero_{label}')
        evidence.append(dict(label=label, polynomial_coefficients=poly, Q=Q, N=N,
                             Q_U=qu, Q_V=qv, minors=minors, residuals=residuals,
                             nonzero_entry=record['nonzero_entry']))
    out = dict(certificate_sha256=sha256((HERE/'survivor.json').read_bytes()).hexdigest(),
               verifier_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
               plucker_residuals=plucker, row_checks=evidence,
               summary=dict(failures=failures, exact_rank_one_actual=len(evidence),
                            exact_rank_one_required=5, plucker_actual=len(plucker),
                            plucker_required=35, new_block_rank_tests=0,
                            result='VERIFIED_SURVIVOR' if not failures else 'FAILED'))
    (HERE/'verification.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out['summary'], sort_keys=True))
    print('Full independent evidence: scripts/span-274-geometry/verification.json')
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())
