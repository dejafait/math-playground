"""Independent reconstruction and witness check; imports no producer code.

Products use coefficient expansion/Horner evaluation. Image coefficients
come from normalized covectors; quadratic coefficients use interpolation.
Gcd claims are checked by their complete division/Bezout certificates,
not by recomputing a gcd with the producer's algorithm.
"""
import hashlib
import itertools
import json
from pathlib import Path

P = 97
S = [1, 8, 12, 18, 22, 27, 33]
J = [47, 50, 64, 70, 75, 79, 85, 89, 96]
FIXED = [35, 522, 477, 566]
X0 = [2, 50, 5, 77, 16, 45, 81]
X1 = [58, 92, 4, 81, 71, 36, 26]
Y0 = [75, 32, 0, 69, 3, 1, 0]
Y1 = [0, 0, 30, 0, 0, 0, 1]
failures = []
checks = 0


def require(test, message):
    global checks
    checks += 1
    if not test:
        failures.append(message)


def canonical(a):
    result = [v % P for v in a]
    while result and result[-1] == 0:
        result.pop()
    return result


def polynomial_sum(terms):
    coeff = {}
    for a in terms:
        for degree, value in enumerate(a):
            coeff[degree] = (coeff.get(degree, 0) + value) % P
    return canonical([coeff.get(i, 0) for i in range(max(coeff, default=-1) + 1)])


def convolution(a, b):
    terms = {}
    for i, j in itertools.product(range(len(a)), range(len(b))):
        terms.setdefault(i + j, []).append(a[i] * b[j])
    return canonical([sum(terms.get(k, [])) for k in range(max(terms, default=-1) + 1)])


def horner(a, t):
    value = 0
    for c in reversed(a):
        value = (t * value + c) % P
    return value


def verify_gcd(polys, certificate, name):
    g = certificate['gcd']
    witnesses, quotients = certificate['bezout'], certificate['quotients']
    require(len(witnesses) == len(polys) == len(quotients), name + ' witness count')
    require(canonical(g) == g and (not g or g[-1] == 1), name + ' monic gcd')
    require(certificate['all_zero'] == (not g), name + ' all-zero flag')
    for i, (f, q) in enumerate(zip(polys, quotients)):
        require(convolution(g, q) == canonical(f), f'{name} division {i}')
    combination = polynomial_sum([convolution(f, w) for f, w in zip(polys, witnesses)])
    require(combination == g, name + ' Bezout identity')
    if not g:
        require(all(not canonical(f) for f in polys), name + ' all inputs zero')


def rank_at(matrix):
    minors = [(matrix[i][0] * matrix[j][1] - matrix[i][1] * matrix[j][0]) % P
              for i, j in itertools.combinations(range(4), 2)]
    witness = next((i for i, v in enumerate(minors) if v), None)
    if witness is not None:
        return dict(rank=2, minors=minors, nonzero_minor_index=witness,
                    nonzero_minor_value=minors[witness])
    return dict(rank=int(any(v for row in matrix for v in row)), minors=minors,
                nonzero_minor_index=None, nonzero_minor_value=None)


def main():
    path = Path(__file__).with_name('l162-additional-row-loci.json')
    raw = path.read_bytes()
    data = json.loads(raw)
    require(data['modulus'] == P and data['S'] == S and data['J'] == J, 'field/coordinates')
    require(data['fixed_labels'] == FIXED, 'fixed labels')
    require(data['X'] == [X0, X1] and data['Y'] == [Y0, Y1], 'L162 input vectors')
    labels = [(list(i), list(k)) for i in itertools.combinations(S, 2)
              for k in itertools.combinations(J, 2)]
    require(len(labels) == 756, 'universe 756')
    fixed_supports = [set(labels[j][0] + labels[j][1]) for j in FIXED]
    expected_coverage, eligible = [], []
    for label, (I, K) in enumerate(labels):
        intersections = [sorted(set(I + K).intersection(T)) for T in fixed_supports]
        retain = label not in FIXED and all(len(v) <= 1 for v in intersections)
        expected_coverage.append(dict(label=label, I=I, K=K,
                                      intersections=intersections, eligible=retain))
        if retain:
            eligible.append(label)
    require(data['coverage'] == expected_coverage, 'complete independent coverage')
    require([row['label'] for row in data['rows']] == eligible, 'all and only eligible original rows')
    results = []
    for record in data['rows']:
        label = record['label']
        I, K = labels[label]
        tag = f'row {label}'
        roots = [z for z in J if z not in K]
        polynomial = [1]
        for z in roots:
            polynomial = convolution(polynomial, [-z % P, 1])
        values = [horner(polynomial, x) for x in S]
        require(all(values), tag + ' denominators nonzero')
        retained = [i for i in range(7) if S[i] not in I]
        anchor, target = retained[0], retained[1:]

        def image(vector):
            return [((vector[i] * pow(values[i], -1, P)
                      - vector[anchor] * pow(values[anchor], -1, P))
                     * values[anchor] * values[i]) % P for i in target]

        def image_at(t):
            xx = image([(u + t * v) % P for u, v in zip(X0, X1)])
            yy = image([(u + t * v) % P for u, v in zip(Y0, Y1)])
            return [list(pair) for pair in zip(xx, yy)]

        at0, at1, atm1 = [image_at(t) for t in (0, 1, -1)]
        inf = [list(pair) for pair in zip(image(X1), image(Y1))]
        entries = [[[at0[i][c], (at1[i][c] - at0[i][c]) % P]
                    for c in range(2)] for i in range(4)]
        for i in range(4):
            for c in range(2):
                require(entries[i][c][1] == inf[i][c], tag + ' homogeneous leading entry')
        minor_values = [rank_at(m)['minors'] for m in (at0, at1, atm1)]
        minors = []
        for f0, f1, fm1 in zip(*minor_values):
            minors.append([f0, (f1 - fm1) * 49 % P,
                           ((f1 + fm1) * 49 - f0) % P])
        infinity = rank_at(inf)
        zero = rank_at(at0)
        require([f[2] for f in minors] == infinity['minors'], tag + ' homogeneous leading minors')
        expected_Q = []
        for i in target:
            basis_images = [image([int(c == k) for c in range(7)]) for k in range(7)]
            expected_Q.append([v[target.index(i)] for v in basis_images])
        for key, value in dict(I=I, K=K, roots=roots, g_values=values,
                               anchor=S[anchor], target=[S[i] for i in target],
                               Q=expected_Q, homogeneous_entries=entries,
                               homogeneous_minors=minors,
                               infinity_rank=infinity['rank'], zero_rank=zero['rank']).items():
            require(record[key] == value, tag + ' ' + key)
        flat_entries = [col for row in entries for col in row]
        verify_gcd(minors, record['affine_minor_certificate'], tag + ' minor gcd')
        verify_gcd(flat_entries, record['affine_entry_certificate'], tag + ' entry gcd')
        g = record['affine_minor_certificate']['gcd']
        h = record['affine_entry_certificate']['gcd']
        require(record['affine_locus'] == dict(vanishing_polynomial=g,
                                               remove_vanishing_polynomial=h), tag + ' locus')
        results.append(dict(label=label, product_polynomial=polynomial,
                            minor_gcd=g, entry_gcd=h,
                            zero=zero, infinity=infinity,
                            all_entry_and_minor_coefficients_verified=True,
                            all_division_and_bezout_identities_verified=True))
    summary = dict(original_labels=len(labels), required_original_labels=756,
                   eligible_labels=len(results), required_eligible_labels=len(eligible),
                   coverage_entries=len(expected_coverage),
                   minor_gcd_histogram={}, entry_gcd_histogram={},
                   infinity_rank_histogram={}, zero_rank_histogram={},
                   empty_labels=[], whole_family_labels=[], other_labels=[], failures=[])
    for row in results:
        for field, value in [('minor_gcd_histogram', row['minor_gcd']),
                             ('entry_gcd_histogram', row['entry_gcd']),
                             ('infinity_rank_histogram', row['infinity']['rank']),
                             ('zero_rank_histogram', row['zero']['rank'])]:
            key = str(value)
            summary[field][key] = summary[field].get(key, 0) + 1
        if row['minor_gcd'] == [1] and row['infinity']['rank'] != 1:
            summary['empty_labels'].append(row['label'])
        elif not row['minor_gcd'] and row['entry_gcd'] == [1] and row['infinity']['rank'] == 1:
            summary['whole_family_labels'].append(row['label'])
        else:
            summary['other_labels'].append(row['label'])
    for key, value in data['summary'].items():
        require(summary.get(key) == value, 'summary ' + key)
    out = dict(source_sha256=hashlib.sha256(raw).hexdigest(),
               method='Independent coefficient products, normalized maps, interpolation, witness checking',
               summary=summary, row_checks=results, checks=checks, failures=failures)
    destination = path.with_name('l162-additional-row-loci-verification.json')
    destination.write_text(json.dumps(out, indent=2) + '\n')
    print('Original-label coverage:', len(expected_coverage), '; required: 756')
    print('Eligible rows verified:', len(results), '; required:', len(eligible))
    print('Minor gcds:', summary['minor_gcd_histogram'], '; entry gcds:', summary['entry_gcd_histogram'])
    print('Endpoints: zero', summary['zero_rank_histogram'], '; infinity', summary['infinity_rank_histogram'])
    print('Checks:', checks, '; failures:', failures)
    print('Certificate:', destination.relative_to(Path.cwd()))
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()
