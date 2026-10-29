"""Separate critical audit of every L163 certificate record.

No producer/verifier imports. Direct integer products and explicit coefficient
formulas reconstruct the maps; expanded integer identities check witnesses.
All records are read, not a preview. This is not a new compatibility test.
"""
import hashlib
import json
from itertools import combinations
from math import prod
from pathlib import Path

P = 97
S = [1, 8, 12, 18, 22, 27, 33]
J = [47, 50, 64, 70, 75, 79, 85, 89, 96]
FIXED = [35, 522, 477, 566]
X = [[2, 50, 5, 77, 16, 45, 81], [58, 92, 4, 81, 71, 36, 26]]
Y = [[75, 32, 0, 69, 3, 1, 0], [0, 0, 30, 0, 0, 0, 1]]
B = [145, 147, 148, 149, 160, 161, 171, 174,
     325, 327, 328, 329, 340, 341, 351, 354,
     577, 581, 582, 583, 595, 596, 609, 610,
     649, 653, 654, 655, 667, 668, 681, 682,
     723, 724, 726, 727, 748, 749, 751, 752]
checks = []


def check(name, actual, required):
    checks.append(dict(name=name, actual=actual, required=required,
                       passed=actual == required))


def expanded_identity(terms):
    """Coefficient residual of a sum of products, over integers then mod 97."""
    coefficients = {}
    for sign, a, b in terms:
        for i, ai in enumerate(a):
            for j, bj in enumerate(b):
                coefficients[i + j] = coefficients.get(i + j, 0) + sign * ai * bj
    return [coefficients.get(i, 0) % P
            for i in range(max(coefficients, default=-1) + 1)]


def witnesses(polys, cert, tag):
    g, aa, qq = cert['gcd'], cert['bezout'], cert['quotients']
    check(tag + ' witness lengths', [len(aa), len(qq)], [len(polys)] * 2)
    check(tag + ' canonical monic', not g or (g[-1] == 1 and all(0 <= v < P for v in g)), True)
    check(tag + ' zero flag', cert['all_zero'], not g)
    residuals = [expanded_identity([(1, g, q), (-1, f, [1])])
                 for f, q in zip(polys, qq)]
    bezout = expanded_identity([(1, a, f) for a, f in zip(aa, polys)] + [(-1, g, [1])])
    for i, residual in enumerate(residuals):
        check(tag + f' division {i}', residual, [0] * len(residual))
    check(tag + ' Bezout', bezout, [0] * len(bezout))
    if not g:
        check(tag + ' zero system', all(all(v == 0 for v in f) for f in polys), True)
    return dict(division_residuals=residuals, bezout_residual=bezout)


def endpoint(minors, coordinate):
    values = [f[coordinate] for f in minors]
    index = next((i for i, value in enumerate(values) if value), None)
    # Every endpoint here must have a nonzero minor, so no other rank is inferred.
    return dict(rank=2 if index is not None else None, minors=values,
                nonzero_minor_index=index,
                nonzero_minor_value=values[index] if index is not None else None)


def main():
    base = Path(__file__).parent
    source = base / 'l162-additional-row-loci.json'
    verification = base / 'l162-additional-row-loci-verification.json'
    raw, vraw = source.read_bytes(), verification.read_bytes()
    data, previous = json.loads(raw), json.loads(vraw)
    digest = hashlib.sha256(raw).hexdigest()
    check('source hash in reviewed verifier', previous['source_sha256'], digest)
    check('verifier failures', previous['failures'], [])
    for key, required in dict(modulus=P, S=S, J=J, fixed_labels=FIXED, X=X, Y=Y,
                              chart='[r:s]=[1:t]; missing endpoint [0:1]',
                              coefficient_orders=dict(entries=['r', 's'], minors=['r^2', 'rs', 's^2'])).items():
        check('header ' + key, data[key], required)
    labels = [(list(i), list(k)) for i in combinations(S, 2) for k in combinations(J, 2)]
    fixed_supports = [set(labels[i][0] + labels[i][1]) for i in FIXED]
    coverage = []
    for label, (I, K) in enumerate(labels):
        intersections = [sorted(set(I + K) & T) for T in fixed_supports]
        eligible = label not in FIXED and all(len(part) <= 1 for part in intersections)
        coverage.append(dict(label=label, I=I, K=K, intersections=intersections, eligible=eligible))
    check('complete coverage', data['coverage'], coverage)
    eligible = [r['label'] for r in coverage if r['eligible']]
    check('coverage count', len(coverage), 756)
    check('eligible count', len(eligible), 112)
    check('all and only row labels', [r['label'] for r in data['rows']], eligible)
    check('all and only verifier labels', [r['label'] for r in previous['row_checks']], eligible)
    verified_rows, audit_rows = [], []
    for row in data['rows']:
        label = row['label']
        I, K = labels[label]
        roots = [v for v in J if v not in K]
        # Elementary-symmetric expansion, distinct from iterative polynomial products.
        polynomial = [((-1) ** (len(roots) - d)
                       * sum(prod(part) for part in combinations(roots, len(roots) - d))) % P
                      for d in range(len(roots) + 1)]
        values = [prod(t - z for z in roots) % P for t in S]
        check(f'{label} nonzero denominators', all(values), True)
        omitted = [n for n, t in enumerate(S) if t not in I]
        z, target = omitted[0], omitted[1:]
        Q = [[(values[z] * (c == n) - values[n] * (c == z)) % P for c in range(7)] for n in target]
        entries = [[[(values[z] * vector[n] - values[n] * vector[z]) % P
                     for vector in pair] for pair in (X, Y)] for n in target]
        minors = []
        for i, j in combinations(range(4), 2):
            a, b = entries[i]
            c, d = entries[j]
            minors.append([(a[0]*d[0] - b[0]*c[0]) % P,
                           (a[0]*d[1] + a[1]*d[0] - b[0]*c[1] - b[1]*c[0]) % P,
                           (a[1]*d[1] - b[1]*c[1]) % P])
        for key, expected in dict(I=I, K=K, roots=roots, g_values=values, anchor=S[z],
                                  target=[S[n] for n in target], Q=Q,
                                  homogeneous_entries=entries, homogeneous_minors=minors).items():
            check(f'{label} ' + key, row[key], expected)
        flat = [entry for pair in entries for entry in pair]
        minor_residuals = witnesses(minors, row['affine_minor_certificate'], f'{label} minors')
        entry_residuals = witnesses(flat, row['affine_entry_certificate'], f'{label} entries')
        g, h = row['affine_minor_certificate']['gcd'], row['affine_entry_certificate']['gcd']
        check(f'{label} claimed minor gcd', g, [3, 1] if label in B else [1])
        check(f'{label} claimed entry gcd', h, [1])
        check(f'{label} locus', row['affine_locus'], dict(vanishing_polynomial=g, remove_vanishing_polynomial=h))
        zero, infinity = endpoint(minors, 0), endpoint(minors, 2)
        for key, value in [('zero', zero), ('infinity', infinity)]:
            check(f'{label} {key} nonzero minor', value['rank'], 2)
            check(f'{label} {key} saved rank', row[key + '_rank'], value['rank'])
        verified_rows.append(dict(label=label, product_polynomial=polynomial, minor_gcd=g, entry_gcd=h,
                                  zero=zero, infinity=infinity,
                                  all_entry_and_minor_coefficients_verified=True,
                                  all_division_and_bezout_identities_verified=True))
        audit_rows.append(dict(label=label, minor_witness_residuals=minor_residuals,
                               entry_witness_residuals=entry_residuals))
    check('complete saved verifier row evidence', previous['row_checks'], verified_rows)
    check('exact forty-label set', [r['label'] for r in verified_rows if r['minor_gcd'] == [3, 1]], B)
    example = next(r for r in data['rows'] if r['label'] == 145)
    for key, expected in dict(I=[1, 27], K=[47, 64], anchor=8,
                              g_values=[11, 54, 62, 69, 28, 79, 40],
                              homogeneous_entries=[[[80, 41], [53, 68]], [[29, 63], [63, 0]],
                                                   [[46, 94], [42, 0]], [[46, 52], [78, 54]]],
                              homogeneous_minors=[[11, 85, 81], [49, 14, 10], [19, 82, 36],
                                                  [66, 22, 0], [43, 3, 7], [7, 66, 32]]).items():
        check('printed label-145 example ' + key, example[key], expected)
    check('printed label-145 quotients', example['affine_minor_certificate']['quotients'],
          [[36, 81], [81, 10], [71, 36], [22], [79, 7], [67, 32]])
    check('printed simple minor Bezout identity', [(75*v) % P for v in [66, 22]], [3, 1])
    check('printed simple entry Bezout identity', (67*42) % P, 1)
    check('interpolation inverse of two', (2*49) % P, 1)
    summary = dict(original_labels=756, required_original_labels=756, eligible_labels=112,
                   coverage_entries=756, minor_gcd_histogram={'[1]': 72, '[3, 1]': 40},
                   entry_gcd_histogram={'[1]': 112}, infinity_rank_histogram={'2': 112},
                   zero_rank_histogram={'2': 112}, empty_labels=[j for j in eligible if j not in B],
                   whole_family_labels=[], other_labels=B, failures=[])
    check('complete producer summary', data['summary'], summary)
    check('complete verifier summary', previous['summary'], dict(summary, required_eligible_labels=112))
    failures = [c['name'] for c in checks if not c['passed']]
    result = dict(source_sha256=digest, verifier_sha256=hashlib.sha256(vraw).hexdigest(),
                  summary=dict(checks=len(checks), failures=failures, original_labels=756,
                               eligible_labels=112, empty_loci=72, singleton_loci=40,
                               required_singleton_parameter=[1, 94], endpoint_rank=2,
                               entry_gcd=[1]), checks=checks, witness_residuals=audit_rows)
    destination = base / 'l163-critical-audit.json'
    destination.write_text(json.dumps(result, indent=2) + '\n')
    print('Coverage 756/756; eligible 112/112; empty/singleton 72/40 required 72/40')
    print('Every coefficient, division/Bezout identity, endpoint and exact forty-label set checked')
    print('Checks:', len(checks), '; failures:', failures)
    print('Certificate:', destination.relative_to(Path.cwd()))
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()
