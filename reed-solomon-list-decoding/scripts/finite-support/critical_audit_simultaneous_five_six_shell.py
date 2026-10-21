"""Critical finite application audit: direct region counts and exact arithmetic.

Imports no notebook code or optimizer. All original load-bearing witness
coordinates are reconstructed and compared, not sampled. The imported
Schrijver theorem, not a quotient dimension guess, supplies full-space coverage.
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
OUT = ROOT / 'simultaneous-five-six-shell-critical-audit.json'


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(value):
    if isinstance(value, F):
        return [value.numerator, value.denominator]
    if isinstance(value, dict):
        return {str(k): enc(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [enc(v) for v in value]
    return value


def eig(n, l, a, r):
    return sum((-1)**h*c(a, h)*c(l-a, r-h)*c(n-l-a, r-h)
               for h in range(r+1))


def beta(n, l, m, a, t):
    return sum((-1)**(u-t)*c(u, t)*c(n-2*a, u-a)
               *c(n-a-u, l-u)*c(n-a-u, m-u)
               for u in range(max(a, t), min(l, m)+1))


def solve_and_det(matrix, rhs):
    a = [[F(x) for x in row]+[F(b)] for row, b in zip(matrix, rhs)]
    n, det = len(a), F(1)
    for k in range(n):
        pivot = next(i for i in range(k, n) if a[i][k])
        if pivot != k:
            a[pivot], a[k] = a[k], a[pivot]
            det = -det
        value = a[k][k]
        det *= value
        a[k] = [x/value for x in a[k]]
        for i in range(n):
            if i != k:
                value = a[i][k]
                a[i] = [x-value*y for x, y in zip(a[i], a[k])]
    return [row[-1] for row in a], det


def main():
    checks, failures = [], []

    def check(name, valid):
        checks.append(name)
        if not valid:
            failures.append(name)

    paths = [ROOT/'simultaneous-five-six-shell-results.json',
             ROOT/'simultaneous-five-six-shell-verification.json',
             ROOT/'full-shell-nullspace-results.json',
             ROOT/'full-shell-column-energy-results.json',
             NB/'lemmas/L056-released-zero-five-shell-nonexclusion.md',
             NB/'lemmas/L060-full-shell-one-column-psd-extension.md',
             NB/'lemmas/L061-simultaneous-five-six-shell-psd-extension.md']
    original, verified, affine, energy = [json.loads(p.read_text()) for p in paths[:4]]
    text5, text60, text61 = [p.read_text() for p in paths[4:]]
    for name, data in zip(['original', 'verified', 'affine', 'energy'],
                          [original, verified, affine, energy]):
        check(name+'_failure_list', data['failures'] == [])
    for name, digest in original['source_hashes'].items():
        check('source_hash_'+name, hashlib.sha256((NB/name).read_bytes()).hexdigest() == digest)
    check('verification_source_hash', verified['source_sha256'] == hashlib.sha256(paths[0].read_bytes()).hexdigest())
    p5, p6 = F(1, 68881143660), F(133, 9357995374380)
    check('positive_unchanged_pairs', p5 > 0 and p6 > 0 and
          original['pairs'] == enc({'p5': p5, 'p6': p6}) == energy['pairs'])
    coeff = {key: F(value) for key, value in re.findall(
        r'^\| (A|B0|C0) \| (-?[0-9]+/[0-9]+) \|$', text60, re.M)}
    star = -coeff['B0']/(2*coeff['A'])
    check('unchanged_minimizer', enc(star) == original['minimizer'] == energy['optimization']['minimizer'])
    z5 = {(int(r), int(q)): F(value) for r, q, value in re.findall(
        r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', text5, re.M)}
    check('complete_five_manuscript', set(z5) == {(r, q) for r in range(6) for q in range(6) if r+q >= 5})
    d5 = {(r, q): z5.get((r, q), F(0))/(c(5, r)*c(63, r)*c(5, q)*c(951, q))
          for r in range(6) for q in range(6)}
    d5[0, 0] = F(1)
    free = [tuple(x) for x in affine['free']]
    intercept = dict(zip(free, map(lambda x: F(*x), affine['nonnegative_test']['intercept'])))
    slope = dict(zip(free, map(lambda x: F(*x), affine['nonnegative_test']['slope'])))
    check('affine_domain', set(free) == {(i, j) for i in range(6) for j in range(6) if i+j <= 5})
    t = {}
    for i, j in itertools.product(range(6), repeat=2):
        t[i, j] = (intercept[i, j]+star*slope[i, j] if i+j <= 5
                   else d5[6-i, i] if i+j == 6 else F(0))
        saved = energy['optimization']['minimizing_column'][6*i+j]
        check(f'column_{i}_{j}', t[i, j] >= 0 and saved == {'i': i, 'j': j, 'value': enc(t[i, j])})

    # Independent actual-subset quotient. U is a distinguished six-set;
    # i=|X cap U|, j=|Y cap U|, t=|X cap Y|. Enumerate the four occupancies.
    factor, norm, basis, gamma, quotient_records = {}, {}, {}, {}, []
    for n in [68, 956]:
        for l in [5, 6]:
            weights = [c(6, i)*c(n-6, l-i) for i in range(l+1)]
            h, ns = [], []
            for a in range(l+1):
                v = [F(i**a) for i in range(l+1)]
                for old, oldnorm in zip(h, ns):
                    projection = sum(w*x*y for w, x, y in zip(weights, v, old))/oldnorm
                    v = [x-projection*y for x, y in zip(v, old)]
                h.append(v)
                ns.append(sum(w*x*x for w, x in zip(weights, v)))
                check(f'positive_norm_{n}_{l}_{a}', ns[-1] > 0)
            basis[n, l], norm[n, l] = h, ns
            factor[n, l] = {'weights': weights, 'basis': h, 'norms': ns}
        for l, m in itertools.product([5, 6], repeat=2):
            for overlap in range(min(l, m)+1):
                matrix = [[sum(c(i, x)*c(6-i, j-x)*c(l-i, overlap-x)
                               *c(n-6-l+i, m-j-overlap+x)
                               for x in range(7))
                           for j in range(m+1)] for i in range(l+1)]
                check(f'quotient_valency_{n}_{l}_{m}_{overlap}',
                      all(sum(row) == c(l, overlap)*c(n-l, m-overlap) for row in matrix))
                factors = []
                for a in range(m+1):
                    v = [sum(F(q)*x for q, x in zip(row, basis[n, m][a])) for row in matrix]
                    if a <= l:
                        scale = sum(w*x*y for w, x, y in zip(factor[n, l]['weights'], v, basis[n, l][a]))/norm[n, l][a]
                        check(f'quotient_full_action_{n}_{l}_{m}_{overlap}_{a}',
                              v == [scale*x for x in basis[n, l][a]])
                        if l == m:
                            check(f'diagonal_eigenvalue_{n}_{l}_{overlap}_{a}', scale == eig(n, l, a, l-overlap))
                            check(f'diagonal_beta_{n}_{l}_{overlap}_{a}',
                                  beta(n, l, l, a, overlap) == c(n-2*a, l-a)*scale)
                        gamma[n, l, m, a, overlap] = scale
                    else:
                        scale = F(0)
                        check(f'absent_layer_annihilation_{n}_{l}_{m}_{overlap}_{a}', not any(v))
                    factors.append(scale)
                quotient_records.append({'n': n, 'l': l, 'm': m, 'intersection': overlap,
                                         'matrix': matrix, 'actions': factors})
        for a in range(6):
            ratios = []
            for overlap in range(6):
                B = beta(n, 5, 6, a, overlap)
                g56, g65 = gamma[n, 5, 6, a, overlap], gamma[n, 6, 5, a, overlap]
                check(f'weighted_rectangular_adjoint_{n}_{a}_{overlap}',
                      norm[n, 5][a]*g56 == norm[n, 6][a]*g65)
                check(f'rectangular_beta_product_{n}_{a}_{overlap}',
                      g56*g65 == F(B*B, c(n-2*a, 5-a)*c(n-2*a, 6-a)))
                if B:
                    ratios.append(g56/B)
                else:
                    check(f'rectangular_beta_zero_{n}_{a}_{overlap}', g56 == g65 == 0)
            check(f'common_signed_rectangular_scale_{n}_{a}', len(set(ratios)) == 1 and ratios[0] > 0)

    S5, S6 = c(68, 5)*c(956, 5), c(68, 6)*c(956, 6)
    R = [(r, q) for r in range(7) for q in range(7) if r+q >= 6]
    val = lambda r, q: c(6, r)*c(62, r)*c(6, q)*c(950, q)
    fixed = {(r, 5-r): p5*t[5-r, r]/p6 for r in range(6)}
    A, B, blocks, multiplicities = [], [], [], []
    for index, (a, b) in enumerate(itertools.product(range(7), repeat=2)):
        D6 = c(68-2*a, 6-a)*c(956-2*b, 6-b)
        C55 = C56 = g56 = g65 = F(0)
        D5, N5 = None, None
        N6 = norm[68, 6][a]*norm[956, 6][b]
        if max(a, b) <= 5:
            D5 = c(68-2*a, 5-a)*c(956-2*b, 5-b)
            N5 = norm[68, 5][a]*norm[956, 5][b]
            lam = sum(x*eig(68, 5, a, r)*eig(956, 5, b, q) for (r, q), x in d5.items())
            if a == b == 0:
                lam -= p5*S5
            C55 = p5*D5*lam
            C56 = p5*sum(x*beta(68, 5, 6, a, i)*beta(956, 5, 6, b, j) for (i, j), x in t.items())
            g56 = p5*sum(x*gamma[68, 5, 6, a, i]*gamma[956, 5, 6, b, j] for (i, j), x in t.items())
            g65 = p5*sum(x*gamma[68, 6, 5, a, i]*gamma[956, 6, 5, b, j] for (i, j), x in t.items())
            if a == b == 0:
                C56 -= p5*p6*S5*S6
                g56 -= p5*p6*S6
                g65 -= p5*p6*S5
            check(f'old_spectrum_{a}_{b}', enc(lam) == energy['modes'][6*a+b]['eigenvalue'] and C55 >= 0)
            check(f'actual_cross_norm_{a}_{b}', g56*g65 == C56*C56/(D5*D6) and N5*g56 == N6*g65)
            check(f'full_singular_range_{a}_{b}', C55 > 0 or C56 == g56 == g65 == 0)
        eta = C56*C56/(C55*p6*D6) if C55 else F(0)
        row = [-F(eig(68, 6, a, r)*eig(956, 6, b, q), val(r, q)) for r, q in R]
        fixedvalue = sum(x*eig(68, 6, a, r)*eig(956, 6, b, q) for (r, q), x in fixed.items())
        correction = p6*S6 if a == b == 0 else F(0)
        bound = 1+fixedvalue-correction-eta
        A.append(row)
        B.append(bound)
        saved = {'a': a, 'b': b, 'five_block': enc(C55), 'cross_block': enc(C56),
                 'six_rescaling': D6, 'coupling_requirement': enc(eta),
                 'anchor_correction': enc(correction), 'fixed_contribution': enc(fixedvalue), 'rhs': enc(bound)}
        check(f'complete_source_mode_{a}_{b}', original['modes'][index] == saved)
        check(f'complete_inequality_{a}_{b}', enc(row) == original['matrix'][index] and enc(bound) == original['rhs'][index])
        mult = (c(68, a)-c(68, a-1))*(c(956, b)-c(956, b-1))
        check(f'positive_mode_multiplicity_{a}_{b}', mult > 0 and D6 > 0)
        multiplicities.append(mult)
        if D5 is not None:
            old = energy['modes'][6*a+b]
            projection = F(*old['projection_intercept'])+star*F(*old['projection_slope'])
            expected = p5*projection**2/(F(*old['norm'])*F(*old['eigenvalue'])) if C55 else F(0)
            check(f'one_column_energy_normalization_{a}_{b}', expected == p6*mult*eta/S6)
        blocks.append({'a': a, 'b': b, 'D5': D5, 'D6': D6, 'N5': N5, 'N6': N6,
                       'C55': C55, 'C56': C56, 'g56': g56, 'g65': g65, 'eta': eta})

    # Solve exactly the manuscript's definition, independently of saved z.
    I = [int(x) for x in re.search(r'I=\((.*?)\)\.', text61, re.S).group(1).replace('\n', '').split(',')]
    J = list(range(21))+list(range(23, 28))
    check('manuscript_fixed_coordinates', 'Set z_21=z_22=0.' in text61 and 'J=(0,1,...,20,23,24,25,26,27)' in text61)
    check('manuscript_basis_indices', I == original['exact']['active_rows'] and J == original['exact']['active_columns'] and len(I) == len(J) == 26)
    values, determinant = solve_and_det([[A[i][j] for j in J] for i in I], [B[i] for i in I])
    numerator, denominator = re.search(r'exact determinant is\s+(\d+)/\s+(\d+),', text61).groups()
    check('manuscript_determinant', determinant == F(int(numerator), int(denominator)) > 0 and enc(determinant) == verified['basis_determinant'])
    z = [F(0)]*28
    for j, value in zip(J, values):
        z[j] = value
    check('independently_solved_witness', enc(z) == original['exact']['z'] == verified['complete_z'])
    check('fixed_zero_coordinates', z[21] == z[22] == 0)
    for j, value in enumerate(z):
        check(f'nonnegative_free_coordinate_{j}', value >= 0)
    d6 = {(r, q): F(0) for r in range(7) for q in range(7)}
    d6.update(fixed)
    d6.update({relation: value/val(*relation) for relation, value in zip(R, z)})
    d6[0, 0] = F(1)
    check('six_partition_and_fixed_values', original['six_shell'] ==
          {'size': S6, 'free_relations': enc(R), 'fixed_coefficients':
           [{'r': r, 'q': q, 'value': enc(x)} for (r, q), x in fixed.items()]})

    # Every actual representative and six support permutations, including
    # Boolean coincidences. Reconstruct memberships by set operations.
    universe, D = set(range(1024)), set(range(68))
    region_records, orbit_values, prescribed = [], {}, 0
    for l, m in [(5, 5), (5, 6), (6, 6)]:
        for i, j in itertools.product(range(min(l, m)+1), repeat=2):
            X = set(range(i)) | set(range(m, m+l-i))
            Y = set(range(68, 68+j)) | set(range(68+m, 68+m+l-j))
            E = (D-X)|Y
            G = (D-set(range(m)))|set(range(68, 68+m))
            supports = [D, E, G]
            index = len(region_records)
            saved = original['presentations'][index]
            check(f'representative_{index}', all(len(s) == 68 for s in supports) and
                  len(D-E) == l and len(D-G) == m and len((D-E)&(D-G)) == i and len((E-D)&(G-D)) == j)
            atoms0 = [956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i]
            moments, details, keys = [], [], []
            for order_index, order in enumerate(itertools.permutations(range(3))):
                P, Q, T = [supports[k] for k in order]
                regions = [set() for k in range(8)]
                for point in universe:
                    regions[4*(point in P)+2*(point in Q)+(point in T)].add(point)
                atoms = list(map(len, regions))
                distances = [len(P-Q), len(P-T), len(Q-T)]
                ab, ac, bc = distances
                if order_index == 0:
                    check(f'manuscript_atoms_{index}', atoms == atoms0)
                moment, origin, prior = None, None, None
                if len({frozenset(s) for s in supports}) == 2:
                    moment, origin = {5: p5, 6: p6}[max(distances)], 'Boolean_pair'
                elif any(1 <= d <= 4 for d in distances):
                    moment, origin = F(0), 'forbidden'
                elif ab == ac == 5:
                    moment, origin = p5*d5[5-len((P-Q)&(P-T)), 5-len((Q-P)&(T-P))], 'L056'
                elif sorted([ab, ac]) == [5, 6]:
                    moment, origin = p5*t[len((P-Q)&(P-T)), len((Q-P)&(T-P))], 'L060'
                prior = moment
                if prior is not None:
                    prescribed += 1
                if moment is None and ab == ac == 6:
                    moment = p6*d6[6-len((P-Q)&(P-T)), 6-len((Q-P)&(T-P))]
                check(f'complete_original_presentation_{index}_{order_index}',
                      saved['presentations'][order_index] == {'order': list(order), 'atoms': atoms,
                      'distances': distances, 'origin': origin, 'value': enc(prior)})
                if moment is not None:
                    moments.append(moment)
                keys.append(tuple(atoms))
                details.append({'order': order, 'atoms': atoms, 'distances': distances, 'moment': moment})
            check(f'all_eligible_presentations_{index}', len(set(moments)) == 1 and moments[0] >= 0)
            key = min(keys)
            check(f'full_unordered_orbit_{index}', key not in orbit_values or orbit_values[key] == moments[0])
            orbit_values[key] = moments[0]
            check(f'complete_verification_presentation_{index}', verified['completed_presentations'][index] ==
                  {'layers': [l, m], 'intersections': [i, j], 'atoms': atoms0, 'moment': enc(moments[0])})
            check(f'original_entry_record_{index}', saved['layers'] == [l, m] and saved['intersections'] == [i, j]
                  and (saved['value'] is None or saved['value'] == enc(moments[0])))
            region_records.append({'layers': [l, m], 'intersections': [i, j],
                                   'supports': [sorted(s) for s in supports], 'presentations': details})
    check('full_region_counts', len(region_records) == 121 and prescribed == original['presentation_count'] == 434)
    slacks, critical_blocks = [], []
    for index, block in enumerate(blocks):
        a, b = block['a'], block['b']
        C55, C56, D5, D6 = [block[key] for key in ['C55', 'C56', 'D5', 'D6']]
        C66 = p6*sum(value*beta(68, 6, 6, a, 6-r)*beta(956, 6, 6, b, 6-q) for (r, q), value in d6.items())
        six_action = p6*sum(value*gamma[68, 6, 6, a, 6-r]*gamma[956, 6, 6, b, 6-q] for (r, q), value in d6.items())
        if a == b == 0:
            C66 -= p6*p6*S6*S6
            six_action -= p6*p6*S6
        check(f'actual_six_layer_action_{a}_{b}', six_action == C66/D6)
        remainder = C66-C56*C56/C55 if C55 else C66
        slack = remainder/(p6*D6)
        check(f'full_schur_remainder_{a}_{b}', slack == B[index]-sum(x*y for x, y in zip(A[index], z)) and slack >= 0)
        check(f'original_slack_{a}_{b}', enc(slack) == original['exact']['slacks'][index] == verified['complete_slacks'][index])
        check(f'complete_verified_block_{a}_{b}', verified['complete_blocks'][index] ==
              {'a': a, 'b': b, 'five': enc(C55), 'cross': enc(C56), 'six': enc(C66),
               'remainder': enc(remainder), 'normalized_slack': enc(slack)})
        if D5 is not None:
            # Symmetric bilinear form in the actual weighted polynomial bases.
            P = block['N5']*C55/D5
            T = block['N5']*block['g56']
            Q = block['N6']*six_action
            check(f'actual_weighted_block_psd_{a}_{b}', P >= 0 and Q >= 0 and P*Q-T*T >= 0 and (P > 0 or T == 0))
            check(f'actual_weighted_schur_{a}_{b}', (Q-T*T/P if P else Q) == block['N6']*remainder/D6)
            block['actual_symmetric_block'] = [[P, T], [T, Q]]
        else:
            check(f'new_only_psd_{a}_{b}', six_action >= 0)
        block.update({'C66': C66, 'remainder': remainder, 'slack': slack})
        critical_blocks.append(block)
        slacks.append(slack)
    check('all_49_modes', len(blocks) == 49 and sum(x > 0 for x in slacks) == 20 and sum(x == 0 for x in slacks) == 29)
    check('all_20_singular_old_modes', sum(block['D5'] is not None and not block['C55'] for block in blocks) == 20)
    check('all_dimensions', sum(multiplicities) == S6 and sum(m for m, block in zip(multiplicities, blocks) if block['D5'] is not None) == S5)
    check('six_boolean_trace', sum(m*block['C66']/(p6*block['D6']) for m, block in zip(multiplicities, blocks)) == S6*(1-p6))
    check('anchor_plus_energy_trace', p6*p6+p6*sum(m*block['eta'] for m, block in zip(multiplicities, blocks))/S6 == F(*energy['optimization']['minimum_energy']))
    check('active_witness_equations', all(slacks[i] == 0 for i in I))
    result = {'source_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'summary': {'checks': len(checks), 'relation_types': len(region_records), 'presentations': 6*len(region_records),
                          'range_equations': 20, 'remainder_modes': len(slacks), 'positive_remainders': sum(x > 0 for x in slacks),
                          'zero_remainders': sum(x == 0 for x in slacks), 'nonnegative_free_coordinates': sum(x >= 0 for x in z)},
              'factor_bases': factor, 'factor_relation_quotients': quotient_records, 'complete_regions': region_records,
              'complete_blocks': critical_blocks, 'matrix': A, 'rhs': B, 'witness': z, 'slacks': slacks,
              'basis_rows': I, 'basis_columns': J, 'basis_determinant': determinant,
              'check_names': checks, 'failures': failures}
    OUT.write_text(json.dumps(enc(result), indent=2)+'\n')
    print(f'critical checks={len(checks)}; failures={failures}; certificate={OUT.relative_to(NB)}')
    print(f'complete region types={len(region_records)}/121; presentations={6*len(region_records)}/726; singular range equations=20/20')
    print(f'nonnegative witness coordinates={sum(x >= 0 for x in z)}/28; PSD remainders={sum(x >= 0 for x in slacks)}/49; positive/zero={sum(x > 0 for x in slacks)}/{sum(x == 0 for x in slacks)}; required >=0')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
