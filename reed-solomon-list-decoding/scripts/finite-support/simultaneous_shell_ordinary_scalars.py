"""Exact approved fixed-row test, with every source presentation on disk.

No optimizer and no verdict about omitted moment matrices. A fixed-row
contradiction is sufficient to stop before the PSD completion calculation.
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
OUT = ROOT / 'simultaneous-shell-ordinary-scalars-results.json'


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def main():
    paths = [ROOT / 'delsarte-lp-results.json',
             ROOT / 'full-shell-column-energy-results.json',
             ROOT / 'simultaneous-five-six-shell-results.json',
             NB / 'lemmas/L056-released-zero-five-shell-nonexclusion.md']
    lp, energy, simultaneous = [json.loads(p.read_text()) for p in paths[:3]]
    checks, failures = [], []

    def check(name, condition):
        checks.append(name)
        if not condition:
            failures.append(name)

    check('prior_certificate_failures_empty',
          all(not d['failures'] for d in [lp, energy, simultaneous]))
    a = [F(v['numerator'], v['denominator']) for v in lp['exact']['primal']]
    check('L021_complete_domain', lp['active_distances'] == list(range(5, 69)) and len(a) == 64)
    for j in range(1, 65):
        row = [F(sum((-1)**h*choose(j, h)*choose(68-j, i-h)*choose(956-j, i-h)
                     for h in range(i+1)), choose(68, i)*choose(956, i))
               for i in range(5, 69)]
        check(f'L021_defining_equation_{j}', sum(x*y for x, y in zip(row, a)) == -1)
    p = [F(1)]+[F(0)]*4+[x/(2*choose(68, i)*choose(956, i))
                          for i, x in zip(range(5, 69), a)]
    check('positive_and_bounded_pairs', all(0 <= x <= 1 for x in p))
    check('p5_p6_match', p[5] == F(1, 68881143660) and p[6] == F(133, 9357995374380))
    N = choose(1024, 68)
    M = (F(choose(1024, 64), choose(68, 64))+1)/2
    rho = M/N
    check('positive_conditional_normalization', rho > 0 and N*rho == M)
    z5 = {(int(r), int(q)): F(value) for r, q, value in re.findall(
        r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', paths[3].read_text(), re.M)}
    check('full_L056_domain', set(z5) == {(r, q) for r in range(6) for q in range(6) if r+q >= 5})
    d5 = {(r, q): z/(choose(5, r)*choose(63, r)*choose(5, q)*choose(951, q))
          for (r, q), z in z5.items()}
    d5[0, 0] = F(1)
    t = {(v['i'], v['j']): F(*v['value']) for v in energy['optimization']['minimizing_column']}
    check('full_L060_domain', set(t) == set(itertools.product(range(6), repeat=2)))
    star = F(*energy['optimization']['minimizer'])
    for row in energy['column_affine']:
        check(f'L060_unchanged_minimizer_{row["i"]}_{row["j"]}',
              t[row['i'], row['j']] == F(*row['intercept'])+star*F(*row['slope']))
    R = [(r, q) for r in range(7) for q in range(7) if r+q >= 6]
    check('same_28_free_coordinates', simultaneous['six_shell']['free_relations'] == [list(v) for v in R])
    d6 = {(r, q): F(*z)/(choose(6, r)*choose(62, r)*choose(6, q)*choose(950, q))
          for (r, q), z in zip(R, simultaneous['exact']['z'])}
    d6[0, 0] = F(1)
    for r in range(6):
        d6[r, 5-r] = p[5]*t[5-r, r]/p[6]

    records, violations, fixed_violations = [], [], []
    unordered_values = {}
    seen_distances = set()
    D = set(range(68))
    for l, m in [(5, 5), (5, 6), (6, 6)]:
        U, V = set(range(m)), set(range(68, 68+m))
        G = (D-U)|V
        for i, j in itertools.product(range(min(l, m)+1), repeat=2):
            X = set(range(i))|set(range(m, m+l-i))
            Y = set(range(68, 68+j))|set(range(68+m, 68+m+l-j))
            E = (D-X)|Y
            supports = [D, E, G]
            r, q = m-i, m-j
            free = l == m == 6 and r+q >= 6
            if (l, m) == (5, 5):
                y = p[5]*d5.get((5-i, 5-j), F(0))
            elif (l, m) == (5, 6):
                y = p[5]*t[i, j]
            else:
                y = p[6]*d6.get((r, q), F(0))
            presentation_rows, orbit_keys, invariants = [], [], []
            for order in itertools.permutations(range(3)):
                A, B, C = [supports[k] for k in order]
                aa, bb, h = len(A-B), len(A-C), len(B-C)
                tt, ss = len((A-B)&(A-C)), len((B-A)&(C-A))
                seen_distances.update([aa, bb, h])
                atoms = [sum(4*(x in A)+2*(x in B)+(x in C) == mask
                             for x in range(1024)) for mask in range(8)]
                check(f'actual_orbit_{l}_{m}_{i}_{j}_{order}',
                      sum(atoms) == 1024 and min(atoms) >= 0
                      and all(len(S) == 68 for S in [A, B, C])
                      and h == aa+bb-tt-ss
                      and 0 <= tt <= min(aa, bb) and 0 <= ss <= min(aa, bb)
                      and aa+bb-tt <= 68 and aa+bb-ss <= 956)
                # A uniform conditional orbit contains exactly this positive
                # number of ordered pairs B,C; total ordered triples is N*orbit.
                orbit = (comb(68, tt)*comb(68-tt, aa-tt)*comb(68-aa, bb-tt)
                         *comb(956, ss)*comb(956-ss, aa-ss)*comb(956-aa, bb-ss))
                check(f'source_normalization_{l}_{m}_{i}_{j}_{order}',
                      orbit > 0 and (N*orbit*rho*y)/(M*orbit) == y)
                invariants.append(tt-ss)
                orbit_keys.append(tuple(atoms))
                check(f'Boolean_and_forbidden_{l}_{m}_{i}_{j}_{order}',
                      (0 not in [aa, bb, h] or y == p[max(aa, bb, h)])
                      and (not any(1 <= d <= 4 for d in [aa, bb, h]) or y == 0))
                slacks = [y, p[aa]-y, 1+y-p[aa]-p[bb]]
                row = {'order': list(order), 'atoms': atoms,
                       'source_indices': [aa, bb, tt, ss], 'third_distance': h,
                       't_minus_s': tt-ss, 'orbit_size': orbit,
                       'pairs': [enc(p[aa]), enc(p[bb]), enc(p[h])],
                       'slacks': [enc(v) for v in slacks]}
                presentation_rows.append(row)
                for kind, slack in zip(['nonnegative', 'upper', 'lower'], slacks):
                    if slack < 0:
                        v = {'type': [l, m, i, j], 'free': free, 'kind': kind,
                             'order': list(order), 'source_indices': [aa, bb, tt, ss],
                             'y': enc(y), 'slack': enc(slack), 'upper_bound': enc(p[aa])}
                        violations.append(v)
                        if not free:
                            fixed_violations.append(v)
            check(f'six_presentation_invariant_{l}_{m}_{i}_{j}', len(set(invariants)) == 1)
            key = min(orbit_keys)
            check(f'unordered_coordinate_{l}_{m}_{i}_{j}',
                  key not in unordered_values or unordered_values[key] == y)
            unordered_values[key] = y
            record = {'type': [l, m, i, j], 'free': free, 'y': enc(y),
                      'presentations': presentation_rows}
            records.append(record)
    check('all_121_types_726_presentations', len(records) == 121
          and sum(len(v['presentations']) for v in records) == 726)
    check('exact_required_pair_range', seen_distances == set(range(13)))
    fixed_count = sum(not v['free'] for v in records)
    summary = {'checks': len(checks), 'failures': len(failures), 'types': len(records),
               'fixed_types': fixed_count, 'free_types': 121-fixed_count,
               'scalar_rows': 2178, 'violations': len(violations),
               'fixed_violations': len(fixed_violations),
               'fixed_slice_excluded': not failures and bool(fixed_violations),
               'PSD_test': 'unnecessary_fixed_scalar_contradiction' if fixed_violations else 'delegated_to_complete_PSD_verifier'}
    result = {'source_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in paths},
              'pairs_through_12': [enc(v) for v in p[:13]], 'rho': enc(rho),
              'types': records, 'violations': violations, 'fixed_violations': fixed_violations,
              'checks': checks, 'failures': failures, 'summary': summary}
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    if fixed_violations:
        v = fixed_violations[0]
        print('First fixed contradiction:', json.dumps(v, sort_keys=True))
    print('Certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit('Reconstruction failures: '+str(failures))


if __name__ == '__main__':
    main()
