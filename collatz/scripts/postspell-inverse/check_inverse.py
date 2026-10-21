"""Exact endpoint-fiber test for the approved 625 two-word labels.

Reuse the imported finite coding implementation already used by L022.
Full certificates go to disk; stdout reports only results and bounds.
"""

import json
from math import gcd
from pathlib import Path
import runpy


HERE = Path(__file__).resolve().parent
helpers = runpy.run_path(str(HERE.parent / 'growing-postspell/check_chains.py'))
coding, word, parameters, crt, replay = (
    helpers[k] for k in ('coding', 'word', 'parameters', 'crt', 'replay'))


def history_at(row, endpoint):
    A, C, D = (row[k] for k in ('A', 'C', 'D'))
    numerator = (1 << D)*endpoint-C
    assert numerator % A == 0
    root = numerator//A
    assert root >= row['minimum_root']
    assert (root-row['minimum_root']) % row['root_period'] == 0
    states, ends, tails = replay(root, row['chain'])
    assert ends[-1] == endpoint and all(x % 2 for x in ends)
    assert all(t == 4*e and e % 2 for t, e in zip(tails, ends))
    return dict(chain=row['chain'], root=root, predecessor=ends[0],
                endpoint=endpoint, states=states, pre_tail_states=tails,
                endpoints=ends)


def main():
    alphabet = [(j, h) for j in range(2, 7) for h in range(3, 8)]
    rows = []
    checks = dict(labels=0, class_replays=0, pair_comparisons=0,
                  compatible_pairs=0, distinct_final_word_compatible_pairs=0,
                  collision_replays=0, failed_checks=0)
    for first in alphabet:
        for last in alphabet:
            chain = [list(first), list(last)]
            w = word(*first)+word(*last)
            D = len(w)
            A1, C1, D1 = parameters(*first)
            A2, C2, D2 = parameters(*last)
            A, C = A2*A1, A2*C1+(1 << D1)*C2
            assert D == D1+D2
            assert coding(w)[:2] == (A, C)
            Aextra, Cextra, r = coding(w+'O')
            assert (Aextra, Cextra) == (3*A, 3*C+(1 << D))
            period = 27*(1 << (D+1))
            p0 = crt(r, 1 << (D+1))
            states, ends, tails = replay(p0, chain)
            m0 = ends[-1]
            assert m0 % 2 and m0*(1 << D) == A*p0+C
            row = dict(chain=chain, A=A, C=C, D=D,
                       parity_residue_with_endpoint_O=r,
                       minimum_root=p0, root_period=period,
                       minimum_endpoint=m0, endpoint_period=54*A,
                       endpoint_residue=m0 % (54*A), predecessor=ends[0])
            history_at(row, m0)
            history_at(row, m0+54*A)
            checks['class_replays'] += 2
            checks['labels'] += 1
            rows.append(row)

    comparisons, candidates = [], []
    for i, left in enumerate(rows):
        for j in range(i+1, len(rows)):
            right = rows[j]
            lmod, rmod = left['endpoint_period'], right['endpoint_period']
            g = gcd(lmod, rmod)
            compatible = (left['endpoint_residue']-right['endpoint_residue']) % g == 0
            # Every modulus is 2 times a power of 3; compatibility is exact.
            assert max(lmod, rmod) % min(lmod, rmod) == 0
            checks['pair_comparisons'] += 1
            comparisons.append(dict(left=i, right=j, gcd=g, compatible=compatible))
            if not compatible:
                continue
            checks['compatible_pairs'] += 1
            if left['chain'][-1] == right['chain'][-1]:
                continue
            checks['distinct_final_word_compatible_pairs'] += 1
            big = left if lmod >= rmod else right
            modulus, residue = big['endpoint_period'], big['endpoint_residue']
            lower = max(left['minimum_endpoint'], right['minimum_endpoint'])
            endpoint = residue+modulus*max(0, (lower-residue+modulus-1)//modulus)
            assert endpoint >= lower and endpoint % 2 and endpoint % 27 == 20
            hl, hr = history_at(left, endpoint), history_at(right, endpoint)
            checks['collision_replays'] += 2
            assert hl['predecessor'] != hr['predecessor']
            candidates.append(dict(left=i, right=j, endpoint=endpoint,
                                   common_endpoint_period=modulus))

    assert checks['labels'] == 625
    assert checks['pair_comparisons'] == 625*624//2
    witness = None
    if candidates:
        selected = min(candidates, key=lambda c: c['endpoint'])
        endpoint = selected['endpoint']
        left, right = rows[selected['left']], rows[selected['right']]
        witness = dict(**selected, left_class=left, right_class=right,
                       histories=[history_at(left, endpoint), history_at(right, endpoint)],
                       next_lift_histories=[history_at(left, endpoint+selected['common_endpoint_period']),
                                            history_at(right, endpoint+selected['common_endpoint_period'])])
        checks['collision_replays'] += 4
    result = dict(result='PASS', outcome='COLLISION' if witness else 'NO_FINITE_COLLISION',
                  scope='2<=J<=6,3<=H<=7 for both words; exact E^2 tails; odd residue-20 states',
                  checks=checks, witness=witness, classes=rows,
                  comparisons=comparisons, collisions=candidates,
                  required_bound='at most one distinct positive extendible predecessor at every endpoint',
                  achieved_bound='two verified distinct predecessors' if witness else 'finite screen only',
                  limitations=['No least-root filters imposed.',
                               'No forward escape or convergence conclusion.'])
    path = HERE/'result.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('result','outcome','scope','checks',
                                          'required_bound','achieved_bound')}, indent=2))
    if witness:
        print(json.dumps(dict(endpoint=witness['endpoint'],
                              chains=[h['chain'] for h in witness['histories']],
                              roots=[h['root'] for h in witness['histories']],
                              predecessors=[h['predecessor'] for h in witness['histories']]), indent=2))
    print(f'certificate: {path}')


if __name__ == '__main__':
    main()
