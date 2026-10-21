"""Independent exact substitution verifier; no constructor/optimizer imports.

Rebuild columns from L059's affine input and L060's manuscript quadratic,
all membership atoms, all source beta blocks and the entire proposed witness.
"""
import hashlib
import itertools
import json
import re
from fractions import Fraction as Q
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'simultaneous-five-six-shell-verification.json'


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(x):
    x = Q(x)
    return [x.numerator, x.denominator]


def beta(n, l, m, a, t):
    return sum((-1)**(u-t)*choose(u, t)*choose(n-2*a, u-a)
               *choose(n-a-u, l-u)*choose(n-a-u, m-u)
               for u in range(a, min(n-a, l, m)+1) if u >= t)


def E(n, layer, a, r):
    return sum((-1)**h*choose(a, h)*choose(layer-a, r-h)*choose(n-layer-a, r-h)
               for h in range(r+1))


def main():
    data = json.loads((ROOT / 'simultaneous-five-six-shell-results.json').read_text())
    old = json.loads((ROOT / 'full-shell-nullspace-results.json').read_text())
    energy = json.loads((ROOT / 'full-shell-column-energy-results.json').read_text())
    manuscript5 = (NB / 'lemmas/L056-released-zero-five-shell-nonexclusion.md').read_text()
    manuscript60 = (NB / 'lemmas/L060-full-shell-one-column-psd-extension.md').read_text()
    checks, failures = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    check('source_hashes', all(hashlib.sha256((NB/name).read_bytes()).hexdigest() == h
                              for name, h in data['source_hashes'].items()))
    check('prior_input_checks', not data['failures'] and not old['failures'] and not energy['failures'])
    p5, p6 = Q(1, 68881143660), Q(133, 9357995374380)
    coefficients = {name: Q(value) for name, value in re.findall(
        r'^\| (A|B0|C0) \| (-?[0-9]+/[0-9]+) \|$', manuscript60, re.M)}
    star = -coefficients['B0']/(2*coefficients['A'])
    check('manuscript_minimizer', enc(star) == data['minimizer'] == energy['optimization']['minimizer'])
    z5 = {(int(r), int(q)): Q(value) for r, q, value in re.findall(
        r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', manuscript5, re.M)}
    d5 = {(r, q): x/(choose(5, r)*choose(63, r)*choose(5, q)*choose(951, q)) for (r, q), x in z5.items()}
    d5[0, 0] = Q(1)
    free = [tuple(v) for v in old['free']]
    c0 = dict(zip(free, map(lambda v: Q(*v), old['nonnegative_test']['intercept'])))
    c1 = dict(zip(free, map(lambda v: Q(*v), old['nonnegative_test']['slope'])))
    t = {}
    for i, j in itertools.product(range(6), repeat=2):
        t[i, j] = c0[i, j]+star*c1[i, j] if i+j <= 5 else d5[6-i, i] if i+j == 6 else Q(0)
        saved = energy['optimization']['minimizing_column'][6*i+j]
        check(f'complete_column_{i}_{j}', enc(t[i, j]) == saved['value'] and t[i, j] >= 0)
    R = [(r, q) for r in range(7) for q in range(7) if r+q >= 6]
    z = [Q(*x) for x in data['exact']['z']]
    check('full_witness_domain', data['six_shell']['free_relations'] == [list(v) for v in R] and len(z) == 28)
    val = lambda r, q: choose(6, r)*choose(62, r)*choose(6, q)*choose(950, q)
    d6 = {(r, q): x/val(r, q) for (r, q), x in zip(R, z)}
    d6[0, 0] = Q(1)
    for r in range(6):
        d6[r, 5-r] = p5*t[5-r, r]/p6
        saved = data['six_shell']['fixed_coefficients'][r]
        check(f'fixed_six_{r}', saved == {'r': r, 'q': 5-r, 'value': enc(d6[r, 5-r])})
    check('complete_nonnegative_six_coefficients', all(x >= 0 for x in d6.values()))

    # Independent atom reconstruction for all 121 types and 726 orderings.
    full_moments, presentation_records, type_index = {}, [], 0
    for l, m in [(5, 5), (5, 6), (6, 6)]:
        for i, j in itertools.product(range(min(l, m)+1), repeat=2):
            atoms = {4: i, 5: l-i, 6: m-i, 7: 68-l-m+i,
                     3: j, 2: l-j, 1: m-j, 0: 956-l-m+j}
            check(f'complete_atoms_{l}_{m}_{i}_{j}', sum(atoms.values()) == 1024 and min(atoms.values()) >= 0)
            moments, keys = [], []
            saved = data['presentations'][type_index]
            check(f'relation_record_{type_index}', saved['layers'] == [l, m] and saved['intersections'] == [i, j])
            for order_index, order in enumerate(itertools.permutations(range(3))):
                perm = [0]*8
                for mask, size in atoms.items():
                    newmask = sum((4 >> k) for k, h in enumerate(order) if mask & (4 >> h))
                    perm[newmask] = size
                ab, ac, bc = perm[4]+perm[5], perm[4]+perm[6], perm[2]+perm[6]
                check(f'full_regions_{type_index}_{order_index}', saved['presentations'][order_index]['atoms'] == perm
                      and saved['presentations'][order_index]['distances'] == [ab, ac, bc])
                if 0 in [ab, ac, bc]:
                    moment = {5: p5, 6: p6}[max(ab, ac, bc)]
                elif any(1 <= h <= 4 for h in [ab, ac, bc]):
                    moment = Q(0)
                elif ab == ac == 5:
                    moment = p5*d5.get((5-perm[4], 5-perm[3]), Q(0))
                elif sorted([ab, ac]) == [5, 6]:
                    moment = p5*t[perm[4], perm[3]]
                elif ab == ac == 6:
                    moment = p6*d6.get((6-perm[4], 6-perm[3]), Q(0))
                else:
                    moment = None
                prior = saved['presentations'][order_index]['value']
                if prior is not None:
                    check(f'preserved_entry_{type_index}_{order_index}', enc(moment) == prior)
                if moment is not None:
                    moments.append(moment)
                keys.append(tuple(perm))
            check(f'full_completed_unordered_consistency_{type_index}', len(set(moments)) == 1 and moments[0] >= 0)
            key = min(keys)
            check(f'full_completed_orbit_consistency_{type_index}', key not in full_moments or full_moments[key] == moments[0])
            full_moments[key] = moments[0]
            presentation_records.append({'layers': [l, m], 'intersections': [i, j],
                                         'atoms': [atoms[k] for k in range(8)], 'moment': enc(moments[0])})
            type_index += 1

    S5, S6 = choose(68, 5)*choose(956, 5), choose(68, 6)*choose(956, 6)
    blocks, slacks, rebuilt_matrix = [], [], []
    multiplicities = []
    for index, (a, b) in enumerate(itertools.product(range(7), repeat=2)):
        D6 = choose(68-2*a, 6-a)*choose(956-2*b, 6-b)
        Y6 = p6*sum(beta(68, 6, 6, a, 6-r)*beta(956, 6, 6, b, 6-q)*x for (r, q), x in d6.items())
        if (a, b) == (0, 0):
            Y6 -= p6*p6*S6*S6
        Y5 = X = Q(0)
        if a <= 5 and b <= 5:
            Y5 = p5*sum(beta(68, 5, 5, a, 5-r)*beta(956, 5, 5, b, 5-q)*x for (r, q), x in d5.items())
            X = p5*sum(beta(68, 5, 6, a, i)*beta(956, 5, 6, b, j)*x for (i, j), x in t.items())
            if (a, b) == (0, 0):
                Y5 -= p5*p5*S5*S5
                X -= p5*p6*S5*S6
            check(f'complete_singular_range_{a}_{b}', Y5 >= 0 and (Y5 > 0 or X == 0))
        remainder = Y6-X*X/Y5 if Y5 > 0 else Y6
        check(f'full_block_psd_{a}_{b}', remainder >= 0)
        slack = remainder/(p6*D6)
        slacks.append(slack)
        row = data['modes'][index]
        check(f'five_cross_blocks_{a}_{b}', row['five_block'] == enc(Y5) and row['cross_block'] == enc(X))
        constant = p6*S6 if (a, b) == (0, 0) else Q(0)
        requirement = (X*X/Y5)/(p6*D6) if Y5 > 0 else Q(0)
        fixed = sum(d6[r, 5-r]*E(68, 6, a, r)*E(956, 6, b, 5-r) for r in range(6))
        rhs = 1+fixed-constant-requirement
        H = [Q(E(68, 6, a, r)*E(956, 6, b, q), val(r, q)) for r, q in R]
        rebuilt_matrix.append([-h for h in H])
        check(f'complete_linear_row_{a}_{b}', list(map(enc, [-h for h in H])) == data['matrix'][index]
              and enc(rhs) == data['rhs'][index])
        check(f'full_exact_slack_{a}_{b}', rhs+sum(h*x for h, x in zip(H, z)) == slack
              and enc(slack) == data['exact']['slacks'][index])
        blocks.append({'a': a, 'b': b, 'five': enc(Y5), 'cross': enc(X), 'six': enc(Y6),
                       'remainder': enc(remainder), 'normalized_slack': enc(slack)})
        mult = (choose(68, a)-choose(68, a-1))*(choose(956, b)-choose(956, b-1))
        multiplicities.append(mult)
    check('six_boolean_trace', sum(mult*Q(*row['six'])/(p6*data['modes'][index]['six_rescaling'])
                                  for index, (mult, row) in enumerate(zip(multiplicities, blocks))) == S6*(1-p6))
    check('six_complete_dimension', sum(multiplicities) == S6)
    check('all_coordinates_and_modes', len(z) == 28 and all(x >= 0 for x in z+slacks))
    rows = [1, 2, 3, 5, 7, 8, 9, 11, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 28, 29, 30, 31, 35, 36, 37, 42]
    cols = list(range(21))+list(range(23, 28))
    check('explicit_witness_basis', rows == data['exact']['active_rows'] and cols == data['exact']['active_columns'])
    matrix = [[rebuilt_matrix[i][j] for j in cols] for i in rows]
    determinant = Q(1)
    for k in range(len(rows)):
        pivot = next((r for r in range(k, len(rows)) if matrix[r][k]), None)
        if pivot is None:
            determinant = Q(0)
            break
        if pivot != k:
            matrix[k], matrix[pivot] = matrix[pivot], matrix[k]
            determinant = -determinant
        value = matrix[k][k]
        determinant *= value
        for r in range(k+1, len(rows)):
            scale = matrix[r][k]/value
            matrix[r] = [x-scale*y for x, y in zip(matrix[r], matrix[k])]
    check('unique_rational_witness_definition', determinant != 0)
    result = {'source_sha256': hashlib.sha256((ROOT/'simultaneous-five-six-shell-results.json').read_bytes()).hexdigest(),
              'completed_presentations': presentation_records, 'complete_blocks': blocks,
              'complete_z': list(map(enc, z)), 'complete_slacks': list(map(enc, slacks)),
              'basis_determinant': enc(determinant),
              'summary': {'checks': len(checks), 'relation_types': type_index,
                          'positive_remainders': sum(x > 0 for x in slacks),
                          'zero_remainders': sum(x == 0 for x in slacks),
                          'nonnegative_coordinates': sum(x >= 0 for x in z)},
              'check_names': checks, 'failures': failures}
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(f'independent checks={len(checks)}; failures={failures}; certificate={OUT.relative_to(NB)}')
    print(f'full unordered completed types={type_index}/121; nonnegative coordinates={sum(x >= 0 for x in z)}/28')
    print(f'exact PSD remainder modes={sum(x >= 0 for x in slacks)}/49; positive/zero={sum(x > 0 for x in slacks)}/{sum(x == 0 for x in slacks)}; required >=0')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
