"""Exact original-label rank loci on the fixed L162 projective family.

Coefficients are in F_97, low degree first. Homogeneous entry/minor
lists mean [r,s] / [r^2,rs,s^2]. No parameter sampling proves a locus.
"""
from itertools import combinations, product
from pathlib import Path
import json

P = 97
S = (1, 8, 12, 18, 22, 27, 33)
J = (47, 50, 64, 70, 75, 79, 85, 89, 96)
FIXED = (35, 522, 477, 566)
X = ((2, 50, 5, 77, 16, 45, 81), (58, 92, 4, 81, 71, 36, 26))
Y = ((75, 32, 0, 69, 3, 1, 0), (0, 0, 30, 0, 0, 0, 1))


def trim(a):
    a = [v % P for v in a]
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0)
                 + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([c * v for v in a])


def mul(a, b):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i + j] += v * w
    return trim(out)


def divmod_poly(a, b):
    a, b = trim(a), trim(b)
    if not b:
        raise ZeroDivisionError
    q = [0] * max(0, len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        i = len(a) - len(b)
        c = a[-1] * pow(b[-1], -1, P) % P
        q[i] = c
        a = add(a, [0] * i + scale(b, -c))
    return trim(q), a


def xgcd(a, b):
    u, v, uu, vv = [1], [], [], [1]
    while b:
        q, remainder = divmod_poly(a, b)
        a, b = b, remainder
        u, uu = uu, add(u, scale(mul(q, uu), -1))
        v, vv = vv, add(v, scale(mul(q, vv), -1))
    if not a:
        return [], [], []
    inv = pow(a[-1], -1, P)
    return scale(a, inv), scale(u, inv), scale(v, inv)


def gcd_certificate(polys):
    g, witnesses = [], []
    for f in polys:
        g, a, b = xgcd(g, trim(f))
        witnesses = [mul(a, w) for w in witnesses] + [b]
    quotients = []
    for f in polys:
        if g:
            q, remainder = divmod_poly(f, g)
            assert not remainder
            quotients.append(q)
        else:
            assert not trim(f)
            quotients.append([])
    combination = []
    for f, w in zip(polys, witnesses):
        combination = add(combination, mul(f, w))
    assert combination == g
    return dict(gcd=g, bezout=witnesses, quotients=quotients,
                all_zero=not g)


def quotient(I, K):
    roots = [z for z in J if z not in K]
    values = []
    for t in S:
        v = 1
        for z in roots:
            v = v * (t - z) % P
        values.append(v)
    target = [i for i, t in enumerate(S) if t not in I]
    z = target[0]
    matrix = [[((values[z] if c == i else 0)
                - (values[i] if c == z else 0)) % P
               for c in range(7)] for i in target[1:]]
    return dict(roots=roots, g_values=values, anchor=S[z],
                target=[S[i] for i in target[1:]], Q=matrix)


def endpoint_rank(entries, coordinate):
    a = [[col[coordinate] for col in row] for row in entries]
    if all(not v for row in a for v in row):
        return 0
    if any((a[i][0] * a[j][1] - a[j][0] * a[i][1]) % P
           for i, j in combinations(range(4), 2)):
        return 2
    return 1


def main():
    labels = list(product(combinations(S, 2), combinations(J, 2)))
    supports = [set(labels[j][0] + labels[j][1]) for j in FIXED]
    coverage, rows = [], []
    for label, (I, K) in enumerate(labels):
        intersections = [sorted(set(I + K) & T) for T in supports]
        eligible = label not in FIXED and all(len(v) <= 1 for v in intersections)
        coverage.append(dict(label=label, I=I, K=K,
                             intersections=intersections, eligible=eligible))
        if not eligible:
            continue
        data = quotient(I, K)
        entries = [[[sum(q * v for q, v in zip(row, vec)) % P
                     for vec in basis] for basis in (X, Y)] for row in data['Q']]
        minors = []
        for i, j in combinations(range(4), 2):
            p = add(mul(entries[i][0], entries[j][1]),
                    scale(mul(entries[j][0], entries[i][1]), -1))
            minors.append(p + [0] * (3 - len(p)))
        minor_gcd = gcd_certificate(minors)
        entry_gcd = gcd_certificate([col for row in entries for col in row])
        g, h = minor_gcd['gcd'], entry_gcd['gcd']
        rows.append(dict(label=label, I=I, K=K, **data,
                         homogeneous_entries=entries, homogeneous_minors=minors,
                         affine_minor_certificate=minor_gcd,
                         affine_entry_certificate=entry_gcd,
                         affine_locus=dict(vanishing_polynomial=g,
                                           remove_vanishing_polynomial=h),
                         infinity_rank=endpoint_rank(entries, 1),
                         zero_rank=endpoint_rank(entries, 0)))
    empty = [r['label'] for r in rows if r['affine_locus']['vanishing_polynomial'] == [1]
             and r['infinity_rank'] != 1]
    whole = [r['label'] for r in rows if not r['affine_locus']['vanishing_polynomial']
             and r['affine_locus']['remove_vanishing_polynomial'] == [1]
             and r['infinity_rank'] == 1]
    summary = dict(original_labels=len(labels), required_original_labels=756,
                   eligible_labels=len(rows), coverage_entries=len(coverage),
                   minor_gcd_histogram={}, entry_gcd_histogram={},
                   infinity_rank_histogram={}, zero_rank_histogram={},
                   empty_labels=empty, whole_family_labels=whole,
                   other_labels=[r['label'] for r in rows
                                 if r['label'] not in set(empty + whole)],
                   failures=[])
    for row in rows:
        for field, value in [('minor_gcd_histogram', row['affine_locus']['vanishing_polynomial']),
                             ('entry_gcd_histogram', row['affine_locus']['remove_vanishing_polynomial']),
                             ('infinity_rank_histogram', row['infinity_rank']),
                             ('zero_rank_histogram', row['zero_rank'])]:
            key = str(value)
            summary[field][key] = summary[field].get(key, 0) + 1
    certificate = dict(modulus=P, S=S, J=J, fixed_labels=FIXED,
                       X=X, Y=Y, chart='[r:s]=[1:t]; missing endpoint [0:1]',
                       coefficient_orders=dict(entries=['r', 's'], minors=['r^2', 'rs', 's^2']),
                       coverage=coverage, rows=rows, summary=summary)
    path = Path(__file__).with_name('l162-additional-row-loci.json')
    path.write_text(json.dumps(certificate, indent=2) + '\n')
    print('Original labels:', len(labels), '; required: 756; eligible:', len(rows))
    print('Affine minor gcd histogram:', summary['minor_gcd_histogram'])
    print('Affine entry gcd histogram:', summary['entry_gcd_histogram'])
    print('Infinity ranks:', summary['infinity_rank_histogram'])
    print('Empty / whole / other loci:', len(empty), len(whole), len(summary['other_labels']))
    print('Failures:', summary['failures'])
    print('Certificate:', path.relative_to(Path.cwd()))


if __name__ == '__main__':
    main()
