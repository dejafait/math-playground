"""Independent all-record/all-orbit reconstruction; no generator imports."""
import json
import sys
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import factorial, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent
SOURCE = ROOT / 'global-triple-principal-results.json'
OUT = ROOT / 'global-triple-principal-audit-results.json'


def binomial(n, k):
    return factorial(n)//factorial(k)//factorial(n-k) if 0 <= k <= n else 0


def enc(x):
    return [x.numerator, x.denominator]


def determinant(matrix):
    total = 0
    for perm in permutations(range(len(matrix))):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i+1, len(perm)))
        term = sign
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        total += term
    return total


def main():
    saved = json.loads(SOURCE.read_text())
    lp = json.loads((ROOT/'delsarte-lp-results.json').read_text())
    old = json.loads((ROOT/'selected-triple-sdp-results.json').read_text())
    failures, counts = [], {}

    def check(group, truth, detail=None):
        counts[group] = counts.get(group, 0)+1
        if not truth:
            failures.append({'kind': group, 'detail': detail})

    primal = [Q(z['numerator'], z['denominator']) for z in lp['exact']['primal']]
    p = [Q(1)]+[Q(0)]*4+[x/(2*binomial(68, i)*binomial(956, i))
                              for i, x in zip(range(5, 69), primal)]
    params = saved['parameters']
    check('parameters', (params['n'], params['w'], params['d']) == (1024, 68, 10))
    check('pair_values', params['p'] == list(map(enc, p)) == old['p'])
    U = Q(binomial(1024, 64), binomial(68, 64))
    universe = binomial(1024, 68)
    M = (U+1)/2
    rho = M/universe
    tau = Q(65537**28, 2**128)
    T = tau.numerator//tau.denominator+1
    for key, val in [('U', U), ('rho', rho), ('objective', M), ('threshold', tau)]:
        check('parameters', params[key] == enc(val), key)
    check('parameters', params['T'] == T and params['universe'] == universe)
    check('threshold', M >= T and M.__floor__() >= T and T-1 <= tau < T)
    check('normalization', 0 < rho <= 1 and p[0] == 1 and p[68] > 0)
    check('pair_nonnegative', all(z >= 0 for z in p) and p[1:5] == [0]*4)
    valencies = [binomial(68, i)*binomial(956, i) for i in range(69)]
    eigenvalues = []
    for j in range(69):
        pol = [0]*69
        for r in range(69-j):
            c = binomial(68-j, r)*binomial(956-j, r)
            for h in range(j+1):
                pol[r+h] += (-1)**h*binomial(j, h)*c
        row = saved['pair_spectra'][j]
        check('spectral_coefficients', row['j'] == j and row['coefficients'] == pol, j)
        eigen = sum(c*x for c, x in zip(pol, p))
        eigenvalues.append(eigen)
        check('spectral_signs', eigen >= 0 and row['eigenvalue_over_rho'] == enc(eigen), j)
        if 1 <= j <= 64:
            check('L021_basis_equations', 1+sum(Q(pol[i], valencies[i])*primal[i-5]
                                              for i in range(5, 69)) == 0, j)
    check('constant_schur', eigenvalues[0] == M == rho*universe
          and saved['constant_schur_over_rho'] == [0, 1])
    D = lcm(*(z.denominator for z in p))
    A = [int(z*D) for z in p]
    H = D*D*A[-1]
    P = [z*D*A[-1] for z in A]
    check('denominators', saved['common_denominators'] ==
          {'pair': D, 'triple': H, 'pair_numerators': A, 'pair_numerators_over_H': P})
    records = saved['records']
    keys = {}
    for index, record in enumerate(records):
        a, b, c = record['distances']
        changed = record['incidence_override']
        key = (a, b, c, changed)
        check('record_uniqueness', key not in keys and 0 <= a <= b <= c <= 68, key)
        keys[key] = index
        if changed:
            check('override_key', (a, b, c) == (5, 5, 5))
        y = Q(0) if changed or any(1 <= z <= 4 for z in (a, b, c)) else (
            p[b] if a == 0 else p[a]*p[b]*p[c]/p[68])
        Y = int(y*H)
        check('triple_values', Q(Y, H) == y and record['triple_numerator'] == Y and Y >= 0, index)
        expected_anchors = sorted(set(((a, b), (a, c), (b, c))))
        check('anchor_completeness', [r['distances_from_anchor'] for r in record['anchors']]
              == [list(z) for z in expected_anchors], index)
        for anchored in record['anchors']:
            i, j = anchored['distances_from_anchor']
            h = a+b+c-i-j
            # Boolean set unions handle every equality of A,B,C explicitly.
            labels = [0, 0 if i == 0 else 1, 2]
            if j == 0:
                labels[2] = 0
            elif h == 0:
                labels[2] = labels[1]
            sets = [frozenset([labels[0]]), frozenset(labels[:2]),
                    frozenset([labels[0], labels[2]])]
            indices = list(dict.fromkeys(sets))
            pair_distance = {frozenset(labels[:2]): i,
                             frozenset([labels[0], labels[2]]): j,
                             frozenset(labels[1:]): h}

            def moment(union):
                return H if len(union) == 1 else P[pair_distance[union]] if len(union) == 2 else Y

            matrix = [[moment(I | J) for J in indices] for I in indices]
            minors = [determinant([[matrix[r][s] for s in sub] for r in sub])
                      for size in range(1, len(matrix)+1)
                      for sub in combinations(range(len(matrix)), size)]
            check('full_minor_identities', anchored['dimension'] == len(matrix)
                  and anchored['principal_minor_numerators'] == minors, [index, i, j])
            check('full_minor_signs', all(z >= 0 for z in minors), [index, i, j])
    entries = {(r['i'], r['j']): r for r in saved['entries']}
    check('entry_completeness', len(saved['entries']) == len(entries) == 4761)
    orbit_count = repeated = forbidden = changed_count = 0
    used = set()
    for i in range(69):
        for j in range(69):
            entry = entries[i, j]
            actual_t, actual_s = set(), set()
            overrides = []
            for t in range(min(i, j)+1):
                for s in range(min(i, j)+1):
                    parts = (t, i-t, j-t, 68-i-j+t, s, i-s, j-s, 956-i-j+s)
                    if min(parts) < 0:
                        continue
                    actual_t.add(t)
                    actual_s.add(s)
                    h = i+j-t-s
                    sorted_d = tuple(sorted((i, j, h)))
                    incidence = (parts[3], parts[2], parts[1], parts[4], parts[0], parts[5], parts[6])
                    changed = incidence == (61, 2, 2, 2, 3, 3, 3)
                    if changed:
                        index = entry['override']['record']
                        overrides.append({'t': t, 's': s, 'record': index})
                    else:
                        index = entry['h_records'][h-entry['h_first']]
                    key = (*sorted_d, changed)
                    check('original_orbit_map', keys.get(key) == index, [i, j, t, s])
                    used.add(index)
                    orbit_count += 1
                    repeated += min(i, j, h) == 0
                    forbidden += any(1 <= z <= 4 for z in (i, j, h))
                    changed_count += changed
                    if changed:
                        for ii, jj, hh in permutations((i, j, h)):
                            tt = (ii+jj-hh+t-s)//2
                            ss = (ii+jj-hh-t+s)//2
                            check('incidence_permutations', (ii, jj, tt, ss) == (5, 5, 3, 2))
            check('source_ranges', entry['t_range'] == [min(actual_t), max(actual_t)]
                  and entry['s_range'] == [min(actual_s), max(actual_s)], [i, j])
            hl = i+j-max(actual_t)-max(actual_s)
            hh = i+j-min(actual_t)-min(actual_s)
            check('h_maps_complete', entry['h_first'] == hl and len(entry['h_records']) == hh-hl+1)
            for h, index in zip(range(hl, hh+1), entry['h_records']):
                check('h_maps_complete', keys.get((*sorted((i, j, h)), False)) == index)
            check('override_maps', overrides == ([] if entry['override'] is None else [entry['override']]))
    actual_counts = {'ordered_orbits': orbit_count, 'repeated_orbits': repeated,
                     'pair_forbidden_orbits': forbidden, 'incidence_zero_orbits': changed_count,
                     'numerical_records': len(records), 'ordered_entries': len(entries),
                     'retained_matrix_checks': orbit_count,
                     'distinct_numeric_anchor_checks': sum(len(r['anchors']) for r in records),
                     'stored_principal_minors': sum(len(r['principal_minor_numerators'])
                                                  for rec in records for r in rec['anchors'])}
    check('counts', actual_counts == saved['counts'] and orbit_count == 1500625
          and repeated == 205 and forbidden == 10232 and changed_count == 1)
    check('all_records_used', used == set(range(len(records))))
    check('claimed_result', saved['failures'] == [] and saved['summary']['trial_feasible']
          and saved['summary']['objective_at_least_T'] and saved['summary']['batch_insufficient'])
    result = {'source': SOURCE.name, 'counts': actual_counts, 'check_counts': counts,
              'total_checks': sum(counts.values()), 'objective': enc(M), 'T': T,
              'constant_schur_over_rho': [0, 1], 'spectra_over_rho': list(map(enc, eigenvalues)),
              'failures': failures, 'verified': not failures}
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print('Complete reconstruction:', sum(counts.values()), 'checks; actual orbits:', orbit_count, '/ 1500625')
    print('All saved principal minors:', actual_counts['stored_principal_minors'], '; pair spectra: 69/69; Schur: 0')
    print('Objective:', M, '; required useful bound <', T)
    print('Failures:', len(failures), '; audit:', OUT)
    assert not failures


if __name__ == '__main__':
    main()
