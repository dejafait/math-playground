"""Complete fixed affine source-block test; no optimizer or retuning.

Consume the audited L062 dictionary and check every actual presentation.
Write all entries, zero-anchor cases and exact source blocks to disk.
"""
import hashlib
import itertools
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'complemented-five-six-shell-results.json'


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(x):
    if isinstance(x, F):
        return [x.numerator, x.denominator]
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [enc(v) for v in x]
    return x


def beta(n, l, m, a, t):
    return sum((-1)**(u-t)*c(u, t)*c(n-2*a, u-a)
               *c(n-a-u, l-u)*c(n-a-u, m-u)
               for u in range(max(a, t), min(l, m)+1))


def main():
    paths = [ROOT/'simultaneous-shell-ordinary-scalars-results.json',
             ROOT/'simultaneous-shell-ordinary-scalars-critical-audit.json',
             ROOT/'simultaneous-five-six-shell-verification.json']
    scalar, audit, included = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, valid):
        checks.append(name)
        if not valid:
            failures.append(name)

    check('audited_input_failure_lists', all(d['failures'] == [] for d in [scalar, audit, included]))
    p = [F(*x) for x in scalar['pairs_through_12']]
    check('complete_pair_range', len(p) == 13 and p[0] == 1 and p[1:5] == [0]*4)
    check('positive_rho', F(*scalar['rho']) > 0)
    entries, dictionary = [], {}
    D = set(range(68))
    for record in scalar['types']:
        l, m, i, j = record['type']
        y = F(*record['y'])
        E = (D-(set(range(i))|set(range(m, m+l-i)))) | (set(range(68, 68+j))|set(range(68+m, 68+m+l-j)))
        G = (D-set(range(m))) | set(range(68, 68+m))
        supports = [D, E, G]
        presentations = []
        for k, order in enumerate(itertools.permutations(range(3))):
            A, B, C = [supports[v] for v in order]
            atoms = [sum(4*(x in A)+2*(x in B)+(x in C) == mask for x in range(1024))
                     for mask in range(8)]
            a, b, h = len(A-B), len(A-C), len(B-C)
            t, s = len((A-B)&(A-C)), len((B-A)&(C-A))
            saved = record['presentations'][k]
            check(f'actual_presentation_{l}_{m}_{i}_{j}_{k}',
                  saved['atoms'] == atoms and saved['source_indices'] == [a, b, t, s]
                  and saved['third_distance'] == h and a+b-t-s == h
                  and all(len(S) == 68 for S in [A, B, C]))
            check(f'Boolean_forbidden_{l}_{m}_{i}_{j}_{k}',
                  (0 not in [a, b, h] or y == p[max(a, b, h)])
                  and (not any(1 <= v <= 4 for v in [a, b, h]) or y == 0))
            value = p[h]-y
            check(f'affine_scalar_{l}_{m}_{i}_{j}_{k}', value >= 0)
            presentations.append({'order': list(order), 'atoms': atoms,
                                  'source_indices': [a, b, t, s], 'h': h,
                                  'pair': p[h], 'y': y, 'affine': value})
        affine = p[l+m-i-j]-y
        dictionary[l, m, i, j] = affine
        dictionary[m, l, i, j] = affine
        entries.append({'type': [l, m, i, j], 'y': y, 'affine': affine,
                        'presentations': presentations})
    expected = {(l, m, i, j) for l, m in itertools.product([5, 6], repeat=2)
                for i, j in itertools.product(range(min(l, m)+1), repeat=2)}
    check('complete_dictionary_and_rectangles', set(dictionary) == expected and len(entries) == 121)

    anchor_cases = []
    for l, m in [(0, 0), (0, 5), (5, 0), (0, 6), (6, 0)]:
        y = p[max(l, m)]
        affine = p[l+m]-y
        check(f'zero_anchor_{l}_{m}', affine == 0)
        anchor_cases.append({'layers': [l, m], 'source_indices': [l, m, 0, 0],
                             'h': l+m, 'pair': p[l+m], 'y': y, 'affine': affine})
    for l in [5, 6]:
        check(f'Boolean_shell_diagonal_{l}', dictionary[l, l, l, l] == 1-p[l])
    blocks, negative, dimensions = [], [], {5: 0, 6: 0}
    for a, b in itertools.product(range(7), repeat=2):
        layers = [l for l in [5, 6] if a <= l and b <= l]
        matrix, pair_matrix, y_matrix = [], [], []
        for l in layers:
            affine_row, pair_row, y_row = [], [], []
            for m in layers:
                P = sum(beta(68, l, m, a, i)*beta(956, l, m, b, j)*p[l+m-i-j]
                        for i, j in itertools.product(range(min(l, m)+1), repeat=2))
                B = sum(beta(68, l, m, a, i)*beta(956, l, m, b, j)*dictionary[l, m, i, j]
                        for i, j in itertools.product(range(min(l, m)+1), repeat=2))
                affine_row.append(B)
                pair_row.append(P)
                y_row.append(P-B)
            matrix.append(affine_row)
            pair_matrix.append(pair_row)
            y_matrix.append(y_row)
        check(f'block_symmetry_{a}_{b}', matrix == list(map(list, zip(*matrix))))
        minors = [matrix[k][k] for k in range(len(layers))]
        if len(layers) == 2:
            minors.append(matrix[0][0]*matrix[1][1]-matrix[0][1]**2)
        psd = all(x >= 0 for x in minors)
        if not psd:
            negative.append([a, b])
        mult = (c(68, a)-c(68, a-1))*(c(956, b)-c(956, b-1))
        check(f'positive_multiplicity_{a}_{b}', mult > 0)
        for l in layers:
            dimensions[l] += mult
        # Recover the audited included blocks, undoing only their anchor
        # correction. No such correction is applied to this complement.
        prior = included['complete_blocks'][7*a+b]
        for k, l in enumerate(layers):
            for h, m in enumerate(layers):
                key = 'five' if l == m == 5 else 'six' if l == m == 6 else 'cross'
                previous = F(*prior[key])
                if (a, b) == (0, 0):
                    previous += p[l]*p[m]*c(68, l)*c(956, l)*c(68, m)*c(956, m)
                check(f'unchanged_included_block_{a}_{b}_{l}_{m}', y_matrix[k][h] == previous)
        blocks.append({'a': a, 'b': b, 'layers': layers, 'multiplicity': mult,
                       'matrix': matrix, 'pair_matrix': pair_matrix, 'y_matrix': y_matrix,
                       'principal_minors': minors, 'PSD': psd})
    check('full_space_dimensions', all(dimensions[l] == c(68, l)*c(956, l) for l in [5, 6]))
    result = {'source_hashes': {str(path.relative_to(NB)): hashlib.sha256(path.read_bytes()).hexdigest()
                                for path in paths},
              'pairs_through_12': p, 'entries': entries, 'anchor_cases': anchor_cases,
              'complete_blocks': blocks, 'negative_modes': negative,
              'summary': {'checks': len(checks), 'types': len(entries), 'presentations': 726,
                          'source_blocks': len(blocks), 'shared_blocks': 36,
                          'new_only_blocks': 13, 'zero_anchor_cases': len(anchor_cases),
                          'PSD_blocks': sum(v['PSD'] for v in blocks),
                          'positive_definite_blocks': sum(all(x > 0 for x in v['principal_minors']) for v in blocks),
                          'verdict': 'RECONSTRUCTION_FAILURE' if failures else 'NEGATIVE_MODE' if negative else 'PSD'},
              'check_names': checks, 'failures': failures}
    OUT.write_text(json.dumps(enc(result), indent=2)+'\n')
    print(f'checks={len(checks)}; failures={failures}; certificate={OUT.relative_to(NB)}')
    print(f'PSD blocks={sum(v["PSD"] for v in blocks)}/49; required=49; negative modes={negative}')
    print('zero anchor=5/5; complete shared/new-only blocks=36/13; no anchor Schur subtraction')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
