"""L063 critical audit: complete set entries and signed subset actions.

Imports no notebook programs or optimizer. The separately rerun verifier
reconstructs canonical input recipes; this audit consumes its complete
evidence and the previously audited unchanged input certificates.
"""
import hashlib
import itertools as it
import json
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'complemented-five-six-shell-critical-audit.json'


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(v):
    if isinstance(v, F):
        return [v.numerator, v.denominator]
    if isinstance(v, dict):
        return {str(k): enc(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [enc(x) for x in v]
    return v


def beta(n, l, m, a, t):
    return sum((-1)**(u-t)*c(u, t)*c(n-2*a, u-a)
               *c(n-a-u, l-u)*c(n-a-u, m-u)
               for u in range(t, min(l, m)+1))


def main():
    names = ['complemented-five-six-shell-results.json',
             'complemented-five-six-shell-verification.json',
             'simultaneous-shell-ordinary-scalars-critical-audit.json',
             'simultaneous-five-six-shell-critical-audit.json',
             'simultaneous-five-six-shell-verification.json',
             'simultaneous-five-six-shell-results.json']
    paths = [ROOT / name for name in names]
    original, verified, scalar, included, incverify, initial = [
        json.loads(path.read_text()) for path in paths]
    checks, failures = [], []

    def check(name, valid):
        checks.append(name)
        if not valid:
            failures.append(name)

    for name, data in zip(names, [original, verified, scalar, included, incverify, initial]):
        check('input_failure_list_'+name, data['failures'] == [])
        for path, digest in data.get('source_hashes', {}).items():
            check('input_hash_'+name+'_'+path, hashlib.sha256((NB/path).read_bytes()).hexdigest() == digest)
    check('all_28_unchanged_coordinates', len(included['witness']) == 28 and
          scalar['witness'] == included['witness'] == initial['exact']['z'] == incverify['complete_z'])
    p = [F(*v) for v in verified['pairs_through_12']]
    check('all_13_pairs', enc(p) == original['pairs_through_12'] and len(p) == 13
          and p[0] == 1 and p[1:5] == [0]*4)
    types = [(l, m, i, j) for l, m in [(5, 5), (5, 6), (6, 6)]
             for i, j in it.product(range(min(l, m)+1), repeat=2)]
    check('complete_certificate_lengths', len(original['entries']) == len(verified['reconstructed_entries']) == 121
          and len(scalar['rows']) == 726 and len(included['complete_regions']) == 121)
    dictionary, presentations, closure = {}, [], {}
    boolean = forbidden = 0
    for idx, (l, m, i, j) in enumerate(types):
        sizes = [956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i]
        # Build disjoint atoms in consecutive point intervals, unlike the
        # constructor's overlapping set formulas.
        supports = [set(), set(), set()]
        offset = 0
        for mask, size in enumerate(sizes):
            for h, bit in enumerate([4, 2, 1]):
                if mask & bit:
                    supports[h].update(range(offset, offset+size))
            offset += size
        check(f'actual_supports_{idx}', offset == 1024 and min(sizes) >= 0
              and all(len(s) == 68 for s in supports))
        y = F(*scalar['rows'][6*idx]['y'])
        saved = original['entries'][idx]
        check(f'complete_entry_{idx}', saved['type'] == [l, m, i, j]
              and saved['y'] == enc(y) and saved['affine'] == enc(p[l+m-i-j]-y)
              and len(saved['presentations']) == 6)
        check(f'verified_entry_{idx}', verified['reconstructed_entries'][idx] == enc({
            'type': [l, m, i, j], 'atoms': sizes, 'y': y, 'affine': p[l+m-i-j]-y}))
        for k, order in enumerate(it.permutations(range(3))):
            A, B, C = [supports[h] for h in order]
            atoms = [0]*8
            for x in range(1024):
                atoms[4*(x in A)+2*(x in B)+(x in C)] += 1
            aa, bb, h = len(A-B), len(A-C), len(B-C)
            t, s = len(A-(B|C)), len((B&C)-A)
            record = {'order': list(order), 'atoms': atoms, 'source_indices': [aa, bb, t, s],
                      'h': h, 'pair': p[h], 'y': y, 'affine': p[h]-y}
            check(f'all_affine_fields_{idx}_{k}', enc(record) == saved['presentations'][k]
                  and h == aa+bb-t-s and t-s == i-j and p[h]-y >= 0)
            prior = scalar['rows'][6*idx+k]
            check(f'identical_audited_moment_{idx}_{k}', prior['y'] == enc(y)
                  and prior['source_indices'] == [aa, bb, t, s]
                  and included['complete_regions'][idx]['presentations'][k]['moment'] in [None, enc(y)])
            key = (tuple(sorted([aa, bb, h])), t-s)
            check(f'complete_source_equality_{idx}_{k}', key not in closure or closure[key] == y)
            closure[key] = y
            if 0 in [aa, bb, h]:
                boolean += 1
                check(f'Boolean_{idx}_{k}', y == p[max(aa, bb, h)])
            if any(1 <= d <= 4 for d in [aa, bb, h]):
                forbidden += 1
                check(f'forbidden_{idx}_{k}', y == 0)
            presentations.append({'type': [l, m, i, j], **record})
        for ll, mm in [(l, m), (m, l)]:
            dictionary[ll, mm, i, j] = y
    check('complete_lower_order_counts', boolean == 12 and forbidden == 228)
    anchors = []
    for l, m in [(0, 0), (0, 5), (5, 0), (0, 6), (6, 0)]:
        anchors.append({'layers': [l, m], 'source_indices': [l, m, 0, 0],
                        'h': l+m, 'pair': p[l+m], 'y': p[max(l, m)], 'affine': F(0)})
        check(f'zero_anchor_{l}_{m}', p[l+m]-p[max(l, m)] == 0)
    check('all_five_anchor_records', enc(anchors) == original['anchor_cases'])

    # Verify the saved monic orthogonal bases completely. Vanishing forward
    # differences above degree a and leading difference a! certify monicity.
    basis, norms, gamma, transitions = {}, {}, {}, []
    for saved in verified['factors']:
        n, l = saved['n'], saved['layer']
        weights = [c(6, i)*c(n-6, l-i) for i in range(l+1)]
        vectors = [[F(*x) for x in row] for row in saved['basis']]
        ns = []
        check(f'weights_{n}_{l}', weights == saved['weights'] and len(vectors) == l+1 and min(weights) > 0)
        for a, v in enumerate(vectors):
            diff = v[:]
            for _ in range(a):
                diff = [y-x for x, y in zip(diff, diff[1:])]
            check(f'monic_degree_{n}_{l}_{a}', diff == [F(factorial(a))]*len(diff) and len(v) == l+1)
            norm = sum(w*x*x for w, x in zip(weights, v))
            check(f'orthogonal_norm_{n}_{l}_{a}', norm > 0 and enc(norm) == saved['norms'][a]
                  and all(sum(w*x*y for w, x, y in zip(weights, v, old)) == 0 for old in vectors[:a]))
            ns.append(norm)
        basis[n, l], norms[n, l] = vectors, ns
    check('complete_factor_bases', set(basis) == {(n, l) for n in [68, 956] for l in [5, 6]})
    for n, l, m in it.product([68, 956], [5, 6], [5, 6]):
        Q = [[[0]*(m+1) for _ in range(l+1)] for _ in range(min(l, m)+1)]
        for i in range(l+1):
            for u, v, w in it.product(range(m+1), repeat=3):
                z = m-u-v-w
                if z < 0 or u+w > min(l, m) or u+v > m:
                    continue
                Q[u+w][i][u+v] += c(i, u)*c(6-i, v)*c(l-i, w)*c(n-6-l+i, z)
        for t, matrix in enumerate(Q):
            check(f'count_all_Y_{n}_{l}_{m}_{t}', all(sum(row) == c(l, t)*c(n-l, m-t) for row in matrix))
            for a in range(m+1):
                action = [sum(count*x for count, x in zip(row, basis[n, m][a])) for row in matrix]
                if a > l:
                    check(f'absent_action_{n}_{l}_{m}_{t}_{a}', not any(action))
                    continue
                weights = [c(6, i)*c(n-6, l-i) for i in range(l+1)]
                scale = sum(w*x*y for w, x, y in zip(weights, basis[n, l][a], action))/norms[n, l][a]
                check(f'complete_action_{n}_{l}_{m}_{t}_{a}', action == [scale*x for x in basis[n, l][a]])
                gamma[n, l, m, a, t] = scale
            transitions.append({'n': n, 'l': l, 'm': m, 't': t, 'quotient': matrix})
    ratios = []
    for n, l, m in it.product([68, 956], [5, 6], [5, 6]):
        for a in range(min(l, m)+1):
            nonzero = []
            for t in range(min(l, m)+1):
                b = beta(n, l, m, a, t)
                g = gamma[n, l, m, a, t]
                if b:
                    nonzero.append(g/b)
                else:
                    check(f'zero_signed_action_{n}_{l}_{m}_{a}_{t}', g == 0)
                check(f'factor_adjoint_{n}_{l}_{m}_{a}_{t}', norms[n, l][a]*g == norms[n, m][a]*gamma[n, m, l, a, t])
            check(f'positive_signed_ratio_{n}_{l}_{m}_{a}', len(set(nonzero)) == 1 and nonzero[0] > 0)
            if l == m:
                check(f'diagonal_scale_{n}_{l}_{a}', nonzero[0] == F(1, c(n-2*a, l-a)))
            ratios.append({'n': n, 'l': l, 'm': m, 'a': a, 'ratio': nonzero[0]})

    blocks, pivots, minima = [], [], []
    dimensions, traces = {5: 0, 6: 0}, {5: F(0), 6: F(0)}
    for a, b in it.product(range(7), repeat=2):
        idx = 7*a+b
        layers = [l for l in [5, 6] if max(a, b) <= l]
        D = [c(68-2*a, l-a)*c(956-2*b, l-b) for l in layers]
        N = [norms[68, l][a]*norms[956, l][b] for l in layers]
        P, Y, B, actions = [], [], [], []
        for l in layers:
            pr, yr, br, ar = [], [], [], []
            for m in layers:
                pairs = list(it.product(range(min(l, m)+1), repeat=2))
                pair = sum(beta(68, l, m, a, i)*beta(956, l, m, b, j)*p[l+m-i-j] for i, j in pairs)
                moment = sum(beta(68, l, m, a, i)*beta(956, l, m, b, j)*dictionary[l, m, i, j] for i, j in pairs)
                act = sum(gamma[68, l, m, a, i]*gamma[956, l, m, b, j]*(p[l+m-i-j]-dictionary[l, m, i, j]) for i, j in pairs)
                pr.append(pair); yr.append(moment); br.append(pair-moment); ar.append(act)
            P.append(pr); Y.append(yr); B.append(br); actions.append(ar)
        mult = (c(68, a)-c(68, a-1))*(c(956, b)-c(956, b-1))
        minors = [B[k][k] for k in range(len(layers))]
        if len(layers) == 2:
            minors.append(B[0][0]*B[1][1]-B[0][1]**2)
        weighted = [[N[k]*x for x in row] for k, row in enumerate(actions)]
        pp = [actions[0][0]]
        if len(layers) == 2:
            pp.append(actions[1][1]-actions[1][0]*actions[0][1]/actions[0][0])
            check(f'signed_tensor_rectangle_{a}_{b}', N[0]*actions[0][1] == N[1]*actions[1][0]
                  and actions[0][1]*actions[1][0] == B[0][1]**2/(D[0]*D[1])
                  and (not B[0][1] or actions[0][1]/B[0][1] > 0))
        check(f'full_constructor_block_{a}_{b}', original['complete_blocks'][idx] == enc({
            'a': a, 'b': b, 'layers': layers, 'multiplicity': mult, 'matrix': B,
            'pair_matrix': P, 'y_matrix': Y, 'principal_minors': minors, 'PSD': True}))
        record = {'a': a, 'b': b, 'layers': layers, 'D': D, 'N': N, 'source_matrix': B,
                  'actual_actions': actions, 'weighted_matrix': weighted, 'normalized_pivots': pp, 'principal_minors': minors}
        check(f'full_verification_block_{a}_{b}', enc(record) == verified['complete_blocks'][idx])
        check(f'all_signs_and_symmetry_{a}_{b}', min(D+N+minors+pp) > 0 and mult > 0
              and B == list(map(list, zip(*B))) and weighted == list(map(list, zip(*weighted))))
        for k, l in enumerate(layers):
            check(f'normalized_diagonal_{a}_{b}_{l}', actions[k][k] == B[k][k]/D[k])
            dimensions[l] += mult
            traces[l] += mult*actions[k][k]
            for h, m in enumerate(layers):
                old = incverify['complete_blocks'][idx]['five' if l == m == 5 else 'six' if l == m == 6 else 'cross']
                reconstructed_y = F(*old)
                if a == b == 0:
                    reconstructed_y += p[l]*p[m]*c(68, l)*c(956, l)*c(68, m)*c(956, m)
                check(f'unchanged_included_overlap_{a}_{b}_{l}_{m}', Y[k][h] == reconstructed_y)
        pivots.extend(pp); minima.extend(minors); blocks.append(record)
    for l in [5, 6]:
        size = c(68, l)*c(956, l)
        check(f'full_layer_dimension_and_trace_{l}', dimensions[l] == size and traces[l] == size*(1-p[l]))
    check('complete_block_counts', len(blocks) == len(original['complete_blocks']) == len(verified['complete_blocks']) == 49
          and sum(len(b['layers']) == 2 for b in blocks) == 36 and len(pivots) == 85 and len(minima) == 121)
    check('exact_pivot_minimum', min(pivots) == F(1, 2))
    check('all_prior_failure_modes_absent', original['negative_modes'] == [])
    summary = {'checks': len(checks), 'failures': len(failures), 'presentations': len(presentations),
               'types': len(types), 'Boolean': boolean, 'forbidden': forbidden, 'zero_anchor_cases': len(anchors),
               'shared_new_only_blocks': [36, 13], 'positive_minors': sum(x > 0 for x in minima),
               'positive_pivots': sum(x > 0 for x in pivots), 'minimum_pivot': min(pivots),
               'required_pivot': '>0', 'audit_retains_L063': not failures}
    result = {'source_hashes': {str(path.relative_to(NB)): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths},
              'summary': summary, 'presentations': presentations, 'anchor_cases': anchors,
              'factor_bases': verified['factors'], 'transitions': transitions, 'factor_actions': gamma,
              'signed_ratios': ratios, 'complete_blocks': blocks, 'dimensions': dimensions, 'traces': traces,
              'witness': included['witness'], 'check_names': checks, 'failures': failures}
    OUT.write_text(json.dumps(enc(result), indent=2)+'\n')
    print(json.dumps(enc(summary), sort_keys=True))
    print('certificate='+str(OUT.relative_to(NB)))
    print('Failures:', failures)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
