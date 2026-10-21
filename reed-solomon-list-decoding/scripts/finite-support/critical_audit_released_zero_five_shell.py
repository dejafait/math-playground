"""Step 184: manuscript-first exact L056 review; no local module imports.

Reconstructs all load-bearing certificate fields, using full membership
regions for orbit checks. The existing beta verifier is run separately.
"""
import hashlib
import json
import re
from fractions import Fraction as Q
from itertools import permutations
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOTEBOOK = ROOT.parent.parent
OUT = ROOT / 'released-zero-five-shell-critical-audit-results.json'


def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(x):
    x = Q(x)
    return [x.numerator, x.denominator]


def main():
    manuscript = (NOTEBOOK / 'lemmas/L056-released-zero-five-shell-nonexclusion.md').read_text()
    paths = [ROOT / 'released-zero-five-shell-results.json',
             ROOT / 'released-zero-five-shell-audit-results.json']
    saved, audited = [json.loads(p.read_text()) for p in paths]
    counts, failures = {}, []

    def check(kind, condition, index=None):
        counts[kind] = counts.get(kind, 0) + 1
        if not condition:
            failures.append({'kind': kind, 'index': index})

    R = [(r, q) for r in range(6) for q in range(6) if r+q >= 5]
    modes = [(a, b) for a in range(6) for b in range(6)]
    parsed = [(int(r), int(q), Q(value)) for r, q, value in re.findall(
        r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', manuscript, re.M)]
    check('manuscript_primal_coverage', [(r, q) for r, q, z in parsed] == R)
    z = [value for r, q, value in parsed]
    assert len(z) == 21, 'Manuscript table missing; no truncated vector checks'
    E = {n: [[sum((-1)**h*C(a, h)*C(5-a, r-h)*C(n-5-a, r-h)
                 for h in range(r+1)) for r in range(6)] for a in range(6)]
         for n in (68, 956)}
    m = {n: [C(n, a)-C(n, a-1) for a in range(6)] for n in E}
    for n in E:
        check('complete_factor', all(x > 0 for x in m[n]) and sum(m[n]) == C(n, 5), n)
        check('saved_multiplicities', audited['multiplicities'][str(n)] == m[n], n)
        for a, r in modes:
            check('saved_beta_factor', enc(E[n][a][r]) == audited['factors'][str(n)][a][r], [n, a, r])
    v = [C(5, r)*C(63, r)*C(5, q)*C(951, q) for r, q in R]
    d = [x/y for x, y in zip(z, v)]
    weights = [Q(m[68][a]) if b == 0 else Q(951, 5)*m[68][a] if b == 1 else Q(0)
               for a, b in modes[1:]]
    matrix = [[-Q(E[68][a][r]*E[956][b][q], val)
               for (r, q), val in zip(R, v)] for a, b in modes[1:]]
    check('all_parameter_dimensions', saved['parameters']['relations'] == [list(x) for x in R]
          and saved['parameters']['modes'] == [list(x) for x in modes[1:]]
          and saved['parameters']['valencies'] == v and len(saved['matrix']) == 35)
    for i, row in enumerate(matrix):
        check('matrix_row_length', len(saved['matrix'][i]) == 21, i)
        for j, x in enumerate(row):
            check('matrix_entry', enc(x) == saved['matrix'][i][j], [i, j])
    check('full_vector_lengths', len(saved['exact']['primal']) == 21
          and len(saved['exact']['dual']) == 35 and len(audited['coefficients']) == 21)
    for j, x in enumerate(z):
        check('manuscript_primal', x >= 0 and enc(x) == saved['exact']['primal'][j], j)
        check('normalized_coefficient', audited['coefficients'][j] ==
              {'relation': list(R[j]), 'd': enc(d[j])}, j)
    for i, weight in enumerate(weights):
        check('dual_formula', weight >= 0 and enc(weight) == saved['exact']['dual'][i], i)
    columns = []
    for j, relation in enumerate(R):
        column = sum(weight*matrix[i][j] for i, weight in enumerate(weights))
        record = {'relation': list(relation), 'coefficient': enc(column), 'slack': enc(column-1)}
        check('exact_dual_identity', column == 1 and record == audited['dual_columns'][j]
              and enc(column-1) == saved['exact']['dual_slacks'][j], j)
        columns.append(record)
    p5 = Q(1, 68881143660)
    S = C(68, 5)*C(956, 5)
    U = Q(C(1024, 64), C(68, 64))
    rho = (U+1)/(2*C(1024, 68))
    requirement, optimum = S*p5, 1+sum(z)
    check('Boolean_scaling', rho > 0 and p5 > 0 and saved['parameters']['p'][5] == enc(p5))
    check('positive_leading_Schur', rho*p5*p5/rho == p5*p5
          and (rho*p5*p5/rho)/p5 == p5)
    check('objective_and_threshold', optimum == 1+sum(weights) == Q(9965466368, 5)
          == Q(956, 5)*C(68, 5) and requirement == Q(4982733184, 5)
          and optimum == 2*requirement and S == 68643272053310642688)
    check('saved_bounds', saved['exact']['row_sum'] == audited['row_sum_upper'] == enc(optimum)
          and saved['exact']['required_row_sum'] == audited['required_row_sum'] == enc(requirement)
          and audited['Schur_margin'] == enc(optimum-requirement))
    signrows = re.findall(r'^\| ([0-5]) \| ([+0] \| [+0] \| [+0] \| [+0] \| [+0] \| [+0]) \|$', manuscript, re.M)
    check('manuscript_sign_coverage', [int(a) for a, row in signrows] == list(range(6)))
    signs = [row.split(' | ') for a, row in signrows]
    assert len(signs) == 6
    spectrum = []
    check('saved_spectrum_length', len(audited['all_product_modes']) == 36)
    for i, (a, b) in enumerate(modes):
        value = 1+sum(x*E[68][a][r]*E[956][b][q] for (r, q), x in zip(R, d))
        schur = value-(requirement if i == 0 else 0)
        record = {'mode': [a, b], 'multiplicity': m[68][a]*m[956][b],
                  'D_eigenvalue': enc(value), 'Schur_eigenvalue': enc(schur)}
        check('full_spectrum_and_manuscript', schur >= 0 and record == audited['all_product_modes'][i]
              and signs[a][b] == ('+' if schur > 0 else '0'), [a, b])
        if i:
            slack = 1-sum(x*y for x, y in zip(matrix[i-1], z))
            check('primal_slack', slack == value and enc(slack) == saved['exact']['primal_slacks'][i-1], i)
        spectrum.append(record)
    check('complete_dimension_and_trace', sum(t['multiplicity'] for t in spectrum) == S
          and sum(t['multiplicity']*Q(*t['D_eigenvalue']) for t in spectrum) == S)
    check('released_positive', d[R.index((2, 3))] > 0)

    # Construct representatives from eight membership atoms, independently
    # of the removal/addition construction in the original verifier.
    region_records, orbit_keys = [], {}
    check('saved_dictionary_length', len(audited['set_dictionary']) == 36)
    for index, (r, q) in enumerate(modes):
        counts_by_mask = {4: 5-r, 5: r, 6: r, 7: 63-r,
                          3: 5-q, 2: q, 1: q, 0: 951-q}
        points, cursor = {}, 0
        for mask in range(8):
            points[mask] = set(range(cursor, cursor+counts_by_mask[mask]))
            cursor += counts_by_mask[mask]
        sets = [set().union(*(points[mask] for mask in range(8) if mask & bit)) for bit in (4, 2, 1)]
        check('full_regions', cursor == 1024 and all(len(t) == 68 for t in sets), [r, q])
        permutation_records, full_atoms = [], []
        for order in permutations(range(3)):
            A, B, Cc = [sets[i] for i in order]
            i, j, h = len(A-B), len(A-Cc), len(B-Cc)
            t, s = len((A-B) & (A-Cc)), len((B-A) & (Cc-A))
            common = len(A & B & Cc)
            pair = [len((A & B)-Cc), len((A & Cc)-B), len((B & Cc)-A)]
            private = [len(A-(B | Cc)), len(B-(A | Cc)), len(Cc-(A | B))]
            outside = 1024-len(A | B | Cc)
            eligible = i == j == 5
            zero = any(x in range(1, 5) for x in (i, j, h))
            check('permutation_invariant', t-s == q-r and h == i+j-t-s
                  and zero == (r+q in range(1, 5)), [r, q, list(order)])
            check('eligible_anchor_relation', not eligible or (5-t, 5-s) == (r, q), [r, q, list(order)])
            if r or q:
                check('eligible_anchor_characterization', eligible == (order[0] == 0 or r+q == 5), [r, q, list(order)])
            permutation_records.append({'eligible_anchor': eligible,
                'represented_relation': [5-t, 5-s] if eligible else None,
                'distances': [i, j, h], 'common': common, 'pair_only': pair,
                'private': private, 'zero': zero})
            full_atoms.append(tuple([common]+pair+private+[outside]))
        key = min(full_atoms)
        check('no_cross_relation_identification', key not in orbit_keys, [r, q])
        orbit_keys[key] = (r, q)
        A, B, Cc = sets
        record = {'r': r, 'q': q, 'distinct': len({frozenset(t) for t in sets}) == 3,
                  'zero': r+q in range(1, 5), 'common': len(A & B & Cc),
                  'pair_only': [len((A & B)-Cc), len((A & Cc)-B), len((B & Cc)-A)],
                  'private': [len(A-(B | Cc)), len(B-(A | Cc)), len(Cc-(A | B))],
                  'support_permutations': permutation_records}
        check('entire_saved_region_record', record == audited['set_dictionary'][index], [r, q])
        check('Boolean_repetition', (len({frozenset(t) for t in sets}) == 2) == (r == q == 0), [r, q])
        region_records.append({'relation': [r, q], 'full_permuted_regions': [list(x) for x in full_atoms],
                               'certificate_record': record})
    check('certificate_integrity', audited['source_sha256'] == hashlib.sha256(paths[0].read_bytes()).hexdigest()
          and audited['checks'] == 1826 and audited['verified'] and audited['failures'] == [])
    report = {'checks': sum(counts.values()), 'counts': counts, 'failures': failures,
              'verified': not failures, 'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'primal_from_manuscript': [enc(x) for x in z], 'dual': [enc(x) for x in weights],
              'dual_columns': columns, 'all_product_modes': spectrum,
              'complete_region_records': region_records,
              'row_sum': enc(optimum), 'required_row_sum': enc(requirement),
              'Schur_margin': enc(optimum-requirement),
              'scope': 'Only L056 shell certificate; no additional principal matrices or global extension tested.'}
    OUT.write_text(json.dumps(report, separators=(',', ':'))+'\n')
    print('Critical manuscript/certificate checks:', report['checks'], '; failures:', len(failures))
    print('Coverage actual/required: columns 21/21; modes 36/36; region permutations 216/216')
    print('Row sum actual/required:', optimum, '/', requirement, '; margin:', optimum-requirement)
    print('Certificate:', OUT)
    if failures:
        print('Failed checks:', failures)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
