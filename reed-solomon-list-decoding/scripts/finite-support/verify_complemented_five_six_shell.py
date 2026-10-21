"""Independent fixed-input reconstruction and subset-action verification.

No constructor imports or optimizer. Recover moments from canonical input
recipes; compare all beta blocks to weighted subset-transition actions.
"""
import hashlib
import itertools
import json
import re
from fractions import Fraction as F
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'complemented-five-six-shell-verification.json'


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


def eig(n, l, a, r):
    return sum((-1)**h*c(a, h)*c(l-a, r-h)*c(n-l-a, r-h) for h in range(r+1))


def main():
    names = ['complemented-five-six-shell-results.json', 'delsarte-lp-results.json',
             'full-shell-nullspace-results.json', 'full-shell-column-energy-results.json',
             'simultaneous-five-six-shell-results.json',
             'simultaneous-five-six-shell-critical-audit.json',
             'simultaneous-shell-ordinary-scalars-results.json']
    paths = [ROOT/name for name in names]
    original, lp, affine, energy, simultaneous, audit, scalar = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(name, valid):
        checks.append(name)
        if not valid:
            failures.append(name)

    for name, data in zip(names, [original, lp, affine, energy, simultaneous, audit, scalar]):
        check('input_failures_'+name, data['failures'] == [])
    for name, h in original['source_hashes'].items():
        check('source_hash_'+name, hashlib.sha256((NB/name).read_bytes()).hexdigest() == h)
    a = [F(x['numerator'], x['denominator']) for x in lp['exact']['primal']]
    check('complete_pair_recipe', len(a) == 64 and lp['active_distances'] == list(range(5, 69)))
    for j in range(1, 65):
        check(f'L021_equation_{j}', sum(x*F(eig(1024, 68, j, i), c(68, i)*c(956, i))
                                       for i, x in zip(range(5, 69), a)) == -1)
    p = [F(1)]+[F(0)]*4+[x/(2*c(68, i)*c(956, i)) for i, x in zip(range(5, 69), a)]
    check('all_required_pairs_match', enc(p[:13]) == original['pairs_through_12'] == scalar['pairs_through_12'])
    five_path = NB/'lemmas/L056-released-zero-five-shell-nonexclusion.md'
    sixty_path = NB/'lemmas/L060-full-shell-one-column-psd-extension.md'
    z5 = {(int(r), int(q)): F(value) for r, q, value in re.findall(
        r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', five_path.read_text(), re.M)}
    check('full_five_input', len(z5) == 21)
    d5 = {(r, q): x/(c(5, r)*c(63, r)*c(5, q)*c(951, q)) for (r, q), x in z5.items()}
    d5[0, 0] = F(1)
    coeff = {key: F(value) for key, value in re.findall(
        r'^\| (A|B0|C0) \| (-?[0-9]+/[0-9]+) \|$', sixty_path.read_text(), re.M)}
    star = -coeff['B0']/(2*coeff['A'])
    check('same_stationary_parameter', enc(star) == energy['optimization']['minimizer'])
    free = [tuple(x) for x in affine['free']]
    intercept = dict(zip(free, [F(*x) for x in affine['nonnegative_test']['intercept']]))
    slope = dict(zip(free, [F(*x) for x in affine['nonnegative_test']['slope']]))
    t = {(i, j): intercept[i, j]+star*slope[i, j] if i+j <= 5
         else d5[6-i, i] if i+j == 6 else F(0) for i, j in itertools.product(range(6), repeat=2)}
    for k, (i, j) in enumerate(itertools.product(range(6), repeat=2)):
        check(f'complete_minimizing_column_{i}_{j}', enc(t[i, j]) == energy['optimization']['minimizing_column'][k]['value'])
    R = [(r, q) for r in range(7) for q in range(7) if r+q >= 6]
    z = [F(*x) for x in simultaneous['exact']['z']]
    check('unchanged_audited_z', len(z) == 28 and simultaneous['six_shell']['free_relations'] == [list(v) for v in R]
          and enc(z) == audit['witness'])
    d6 = {(r, q): x/(c(6, r)*c(62, r)*c(6, q)*c(950, q)) for (r, q), x in zip(R, z)}
    d6[0, 0] = F(1)
    for r in range(6):
        d6[r, 5-r] = p[5]*t[5-r, r]/p[6]
    ydict, adict, entries, unordered = {}, {}, [], {}
    index = 0
    for l, m in [(5, 5), (5, 6), (6, 6)]:
        for i, j in itertools.product(range(min(l, m)+1), repeat=2):
            atoms = (956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i)
            y = p[5]*d5.get((5-i, 5-j), F(0)) if l == m == 5 else p[5]*t[i, j] if l == 5 else p[6]*d6.get((6-i, 6-j), F(0))
            record = original['entries'][index]
            check(f'fixed_moment_{index}', record['type'] == [l, m, i, j] and record['y'] == enc(y)
                  and scalar['types'][index]['y'] == enc(y))
            keys = []
            for k, order in enumerate(itertools.permutations(range(3))):
                perm = [0]*8
                for mask, size in enumerate(atoms):
                    perm[sum(4 >> v for v, h in enumerate(order) if mask & (4 >> h))] = size
                aa, bb, h, tt, ss = perm[4]+perm[5], perm[4]+perm[6], perm[2]+perm[6], perm[4], perm[3]
                value = p[h]-y
                expected = {'order': list(order), 'atoms': perm, 'source_indices': [aa, bb, tt, ss],
                            'h': h, 'pair': p[h], 'y': y, 'affine': value}
                check(f'complete_affine_presentation_{index}_{k}', enc(expected) == record['presentations'][k]
                      and value >= 0 and h == aa+bb-tt-ss and tt-ss == i-j)
                check(f'lower_order_cases_{index}_{k}',
                      (0 not in [aa, bb, h] or y == p[max(aa, bb, h)])
                      and (not any(1 <= v <= 4 for v in [aa, bb, h]) or y == 0))
                keys.append(tuple(perm))
            key = min(keys)
            check(f'unordered_moment_{index}', key not in unordered or unordered[key] == y)
            unordered[key] = y
            for ll, mm in [(l, m), (m, l)]:
                ydict[ll, mm, i, j], adict[ll, mm, i, j] = y, p[l+m-i-j]-y
            entries.append({'type': [l, m, i, j], 'atoms': atoms, 'y': y, 'affine': p[l+m-i-j]-y})
            index += 1
    check('all_entries_consumed', index == len(original['entries']) == 121)
    for record in original['anchor_cases']:
        l, m = record['layers']
        check(f'zero_anchor_{l}_{m}', record == enc({'layers': [l, m], 'source_indices': [l, m, 0, 0],
              'h': l+m, 'pair': p[l+m], 'y': p[max(l, m)], 'affine': F(0)}))

    # Count transitions on actual subsets, independently of beta sums.
    basis, norms, gamma, factors = {}, {}, {}, []
    for n in [68, 956]:
        for l in [5, 6]:
            weights = [c(6, i)*c(n-6, l-i) for i in range(l+1)]
            vectors, ns = [], []
            for a in range(l+1):
                v = [F(i**a) for i in range(l+1)]
                for old, norm in zip(vectors, ns):
                    projection = sum(w*x*y for w, x, y in zip(weights, v, old))/norm
                    v = [x-projection*y for x, y in zip(v, old)]
                vectors.append(v)
                ns.append(sum(w*x*x for w, x in zip(weights, v)))
                check(f'positive_norm_{n}_{l}_{a}', ns[-1] > 0)
            basis[n, l], norms[n, l] = vectors, ns
            factors.append({'n': n, 'layer': l, 'weights': weights, 'basis': vectors, 'norms': ns})
        for l, m in itertools.product([5, 6], repeat=2):
            for overlap in range(min(l, m)+1):
                transition = [[sum(c(i, x)*c(6-i, j-x)*c(l-i, overlap-x)
                                   *c(n-6-l+i, m-j-overlap+x) for x in range(7))
                               for j in range(m+1)] for i in range(l+1)]
                check(f'transition_row_count_{n}_{l}_{m}_{overlap}',
                      all(sum(row) == c(l, overlap)*c(n-l, m-overlap) for row in transition))
                for a in range(m+1):
                    action = [sum(q*x for q, x in zip(row, basis[n, m][a])) for row in transition]
                    if a <= l:
                        scale = action[-1]/basis[n, l][a][-1]
                        check(f'full_transition_action_{n}_{l}_{m}_{overlap}_{a}',
                              action == [scale*x for x in basis[n, l][a]])
                        if l == m:
                            check(f'diagonal_mode_identity_{n}_{l}_{overlap}_{a}', scale == eig(n, l, a, l-overlap))
                        gamma[n, l, m, a, overlap] = scale
                    else:
                        check(f'absent_mode_action_{n}_{l}_{m}_{overlap}_{a}', not any(action))
    blocks, pivots, dimensions = [], [], {5: 0, 6: 0}
    for a, b in itertools.product(range(7), repeat=2):
        source = original['complete_blocks'][7*a+b]
        layers = [l for l in [5, 6] if a <= l and b <= l]
        actions = [[sum(adict[l, m, i, j]*gamma[68, l, m, a, i]*gamma[956, l, m, b, j]
                        for i, j in itertools.product(range(min(l, m)+1), repeat=2))
                    for m in layers] for l in layers]
        D = [c(68-2*a, l-a)*c(956-2*b, l-b) for l in layers]
        N = [norms[68, l][a]*norms[956, l][b] for l in layers]
        B = [[F(*x) for x in row] for row in source['matrix']]
        for k, l in enumerate(layers):
            check(f'diagonal_source_action_{a}_{b}_{l}', actions[k][k] == B[k][k]/D[k])
        if len(layers) == 2:
            # Check the SIGN of the rectangular congruence as well as its square.
            ratios = []
            for i, j in itertools.product(range(6), repeat=2):
                source_beta = (sum((-1)**(u-i)*c(u, i)*c(68-2*a, u-a)*c(68-a-u, 5-u)*c(68-a-u, 6-u)
                                   for u in range(max(a, i), 6))
                               *sum((-1)**(v-j)*c(v, j)*c(956-2*b, v-b)*c(956-b-v, 5-v)*c(956-b-v, 6-v)
                                    for v in range(max(b, j), 6)))
                act = gamma[68, 5, 6, a, i]*gamma[956, 5, 6, b, j]
                if source_beta:
                    ratios.append(act/source_beta)
                else:
                    check(f'zero_rectangular_relation_{a}_{b}_{i}_{j}', act == 0)
            ratio = ratios[0]
            check(f'signed_rectangular_scale_{a}_{b}', len(set(ratios)) == 1 and ratio > 0
                  and actions[0][1] == ratio*B[0][1])
            check(f'weighted_adjoint_{a}_{b}', N[0]*actions[0][1] == N[1]*actions[1][0])
            check(f'rectangular_normalization_{a}_{b}', actions[0][1]*actions[1][0] == B[0][1]**2/(D[0]*D[1]))
        weighted = [[N[k]*value for value in row] for k, row in enumerate(actions)]
        check(f'weighted_symmetry_{a}_{b}', weighted == list(map(list, zip(*weighted))))
        remainder = actions[-1][-1] if len(layers) == 1 else actions[1][1]-actions[1][0]*actions[0][1]/actions[0][0]
        normalized_pivots = [actions[0][0], remainder] if len(layers) == 2 else [remainder]
        check(f'exact_positive_pivots_{a}_{b}', all(x > 0 for x in normalized_pivots))
        minors = [B[k][k] for k in range(len(layers))]
        if len(layers) == 2:
            minors.append(B[0][0]*B[1][1]-B[0][1]**2)
            check(f'source_remainder_{a}_{b}', remainder == (B[1][1]-B[0][1]**2/B[0][0])/D[1])
        check(f'complete_source_minors_{a}_{b}', source['principal_minors'] == enc(minors)
              and all(x > 0 for x in minors) and source['PSD'])
        multiplicity = (c(68, a)-c(68, a-1))*(c(956, b)-c(956, b-1))
        check(f'complete_layer_indices_{a}_{b}', source['layers'] == layers and source['multiplicity'] == multiplicity)
        for l in layers:
            dimensions[l] += multiplicity
        pivots.extend(normalized_pivots)
        blocks.append({'a': a, 'b': b, 'layers': layers, 'D': D, 'N': N, 'source_matrix': B,
                       'actual_actions': actions, 'weighted_matrix': weighted,
                       'normalized_pivots': normalized_pivots, 'principal_minors': minors})
    check('complete_dimensions', all(dimensions[l] == c(68, l)*c(956, l) for l in [5, 6]))
    check('complete_pivot_lower_bound', min(pivots) == F(1, 2))
    paths.extend([five_path, sixty_path])
    result = {'source_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'pairs_through_12': p[:13], 'reconstructed_entries': entries,
              'factors': factors, 'complete_blocks': blocks,
              'summary': {'checks': len(checks), 'types': index, 'source_blocks': len(blocks),
                          'positive_definite_blocks': sum(all(x > 0 for x in row['normalized_pivots']) for row in blocks),
                          'normalized_pivot_count': len(pivots), 'minimum_normalized_pivot': min(pivots),
                          'minimum_pivot_equals_one_half': min(pivots) == F(1, 2)},
              'check_names': checks, 'failures': failures}
    OUT.write_text(json.dumps(enc(result), indent=2)+'\n')
    print(f'independent checks={len(checks)}; failures={failures}; certificate={OUT.relative_to(NB)}')
    print(f'positive normalized pivots={sum(x > 0 for x in pivots)}/{len(pivots)}; required >0')
    print(f'complete positive definite shell blocks=49/49; minimum normalized pivot={min(pivots)}; required >0')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
