#!/usr/bin/env python3
"""Independent Horner/normalized-quotient reconstruction; no producer imports.

Rank is bounded below by a rationally evaluated integer minor and above
by the complete independently checked nullspace. Column insertion gives
an additional exact rank computation, separate from producer row reduction.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
J = [47, 50, 64, 70, 75, 79, 85, 89, 96]
TABLE = [([1], [47, 50, 64]), ([8, 12], [70, 75]),
         ([18, 22], [79, 85]), ([27, 33], [89, 96]),
         ([1, 18], [70, 89]), ([22], [47, 75, 96]),
         ([8, 27], [50, 79]), ([12, 33], [64, 85]),
         ([1, 33], [75, 79]), ([27], [47, 70, 85]),
         ([12, 18], [50, 96]), ([8, 22], [64, 89]),
         ([1, 8], [85, 96]), ([12], [47, 79, 89]),
         ([22, 33], [50, 70]), ([18, 27], [64, 75])]


def column_rank(matrix):
    basis = {}
    for column in zip(*matrix):
        v = [x % P for x in column]
        for pivot in sorted(basis):
            factor = v[pivot]
            v = [(x - factor*y) % P for x, y in zip(v, basis[pivot])]
        pivot = next((i for i, x in enumerate(v) if x), None)
        if pivot is not None:
            inv = pow(v[pivot], -1, P)
            basis[pivot] = [x*inv % P for x in v]
    return len(basis)


def integer_determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    result = Fraction(1)
    for col in range(len(a)):
        pos = next((i for i in range(col, len(a)) if a[i][col]), None)
        if pos is None:
            return 0
        if pos != col:
            a[pos], a[col] = a[col], a[pos]
            result = -result
        value = a[col][col]
        result *= value
        a[col] = [x/value for x in a[col]]
        for i in range(col + 1, len(a)):
            factor = a[i][col]
            a[i] = [x - factor*y for x, y in zip(a[i], a[col])]
    if result.denominator != 1:
        raise ArithmeticError('integer minor determinant had a denominator')
    return result.numerator


def main():
    path = HERE / 'certificate.json'
    raw = path.read_bytes()
    data = json.loads(raw)
    checks, failures = [], []

    def check(name, actual, required):
        passed = actual == required
        checks.append({'name': name, 'passed': passed})
        if not passed:
            failures.append({'name': name, 'actual': actual, 'required': required})

    source = ROOT / 'lemmas/L167-completed-family-marked-extraction-counterexample.md'
    lines = source.read_text().splitlines()
    start = lines.index('| Row | Class | A intersection S | A intersection J |')
    parsed = []
    for line in lines[start+2:]:
        if not line.startswith('|'):
            break
        c = [v.strip() for v in line.strip('|').split('|')]
        parsed.append({'id': int(c[0]), 'I': list(map(int, c[2].split(','))),
                       'K': list(map(int, c[3].split(',')))})
    expected_table = [{'id': n, 'I': i, 'K': k} for n, (i, k) in enumerate(TABLE, 1)]
    check('literal transcription versus complete canonical table', parsed, expected_table)
    check('producer complete table', data['canonical_table'], expected_table)
    h = sorted({pow(8, i, P) for i in range(16)})
    check('generator exact order', [pow(8, 16, P), pow(8, 8, P)], [1, 96])
    check('fixed H partition', sorted(S + J), h)
    check('modulus and fixed parts', [data['modulus'], data['S'], data['J']], [P, S, J])
    for name, digest in data['source_sha256'].items():
        check('source hash ' + name, sha256((ROOT/name).read_bytes()).hexdigest(), digest)
    selected = [(n, i, k) for n, (i, k) in enumerate(TABLE, 1) if len(i) == 2]
    ids = [n for n, i, k in selected]
    check('complete E2 IDs', data['E2_rows'], ids)
    check('complete E2 size', len(ids), 12)
    pairs = list(combinations(S, 2))
    check('all exterior columns in order', data['column_pairs'], list(map(list, pairs)))
    blocks, stack, identities, polynomial_records = [], [], [], []
    prefix_ranks = []
    for n, overlap, outside in selected:
        roots = sorted(set(J)-set(outside))
        coeff = [1]
        for root in roots:
            new = [0]*(len(coeff)+1)
            for degree, value in enumerate(coeff):
                new[degree] = (new[degree]-root*value) % P
                new[degree+1] = (new[degree+1]+value) % P
            coeff = new
        g = {}
        for x in h:
            val = 0
            for a in reversed(coeff):
                val = (val*x+a) % P
            g[x] = val
        check(f'row {n} exact polynomial zero set', [x for x in h if not g[x]], roots)
        o = [x for x in S if x not in overlap]
        z, rest = o[0], o[1:]
        d = {x: [((pow(g[x], -1, P) if a == x else 0) -
                   (pow(g[z], -1, P) if a == z else 0)) % P for a in S]
             for x in rest}
        q = [[g[z]*g[x]*v % P for v in d[x]] for x in rest]
        block = []
        for x, y in combinations(rest, 2):
            scale = g[z]**2*g[x]*g[y] % P
            block.append([scale*(d[x][S.index(a)]*d[y][S.index(b)] -
                                 d[x][S.index(b)]*d[y][S.index(a)]) % P for a, b in pairs])
            identities.append({'support_row': n, 'pivot': z, 'covector_pair': [x, y]})
        record = {'id': n, 'I': overlap, 'K': outside, 'roots': roots,
                  'g': {str(x): g[x] for x in h}, 'pivot': z,
                  'covector_labels': rest, 'Q': q, 'N': block}
        check(f'row {n} every block field, g value, covector and exterior entry',
              data['blocks'][len(blocks)], record)
        check(f'row {n} quotient and exterior ranks', [column_rank(q), column_rank(block)], [4, 6])
        polynomial_records.append({'support_row': n, 'coefficients_ascending': coeff,
                                   'normalized_covectors': list(d.values())})
        blocks.append(record)
        stack.extend(block)
        prefix_ranks.append(column_rank(stack))
    check('block count', len(data['blocks']), 12)
    check('all row identities', data['row_identities'], identities)
    check('all 1512 stack entries', data['stack'], stack)
    actual_rank = column_rank(stack)
    reported = data['summary']['actual_rank']
    check('independent column rank', reported, actual_rank)
    check('actual and required shape', data['summary']['matrix_shape'], [72, 21])
    check('required threshold', data['summary']['required_rank'], 21)
    rowids, colids = data['minor_row_indices'], data['minor_column_indices']
    check('minor row count and uniqueness', [len(rowids), len(set(rowids))], [reported]*2)
    check('minor column count and uniqueness', [len(colids), len(set(colids))], [reported]*2)
    check('minor indices in range', all(0 <= i < 72 for i in rowids) and
          all(0 <= j < 21 for j in colids), True)
    minor = [[stack[i][j] for j in colids] for i in rowids]
    check('entire selected minor', data['minor'], minor)
    check('minor support/covector identities', data['minor_row_identities'], [identities[i] for i in rowids])
    det = integer_determinant(minor)
    check('independent rational determinant residue', data['minor_determinant_mod_97'], det % P)
    check('rank lower bound from nonzero minor', det % P != 0, True)
    pivots, free, kernel = data['pivot_columns'], data['free_columns'], data['kernel_basis']
    check('pivot and minor columns agree', pivots, colids)
    check('all nonpivot columns', free, [i for i in range(21) if i not in pivots])
    check('kernel dimension and basis sizes', [data['summary']['kernel_dimension'], len(kernel)], [21-reported]*2)
    check('kernel vector lengths', [len(v) for v in kernel], [21]*len(kernel))
    check('kernel independence on free coordinates', [[v[j] for j in free] for v in kernel],
          [[int(i == j) for j in range(len(free))] for i in range(len(free))])
    residuals = [[sum(a*b for a, b in zip(row, v)) % P for row in stack] for v in kernel]
    check('every kernel annihilation entry', residuals, [[0]*72 for v in kernel])
    # With the lower minor and 21-r independent kernel vectors, completeness
    # follows by rank-nullity. The unique RREF can also be rebuilt from this basis.
    expected_rref = [[0]*21 for _ in stack]
    for i, col in enumerate(pivots):
        expected_rref[i][col] = 1
        for j, v in zip(free, kernel):
            expected_rref[i][j] = -v[col] % P
    check('all RREF entries from complete kernel', data['rref'], expected_rref)
    check('producer failures', data['summary']['failures'], [])
    out = {'certificate_sha256': sha256(raw).hexdigest(),
           'construction': 'polynomial coefficients/Horner; normalized quotients; no producer imports',
           'polynomial_records': polynomial_records, 'blocks': blocks, 'stack': stack,
           'prefix_ranks': prefix_ranks, 'minor_row_indices': rowids,
           'minor_column_indices': colids, 'minor': minor,
           'integer_minor_determinant': det, 'minor_determinant_mod_97': det % P,
           'kernel_basis': kernel, 'kernel_residuals': residuals,
           'checks': checks, 'summary': {'actual_rank': actual_rank, 'required_rank': 21,
                                        'kernel_dimension': len(kernel),
                                        'checks': len(checks), 'failures': failures}}
    dest = HERE / 'verification.json'
    dest.write_text(json.dumps(out, indent=2) + '\n')
    print(f'Independent rank {actual_rank}; required 21; complete kernel dimension {len(kernel)}.')
    print(f'Checks {len(checks)}; failures {len(failures)}; minor residue {det % P}; prefix ranks {prefix_ranks}.')
    print(f'Complete independent evidence: {dest.relative_to(ROOT)}')
    if failures:
        print('Failed checks:', [f['name'] for f in failures])
        raise SystemExit(1)


if __name__ == '__main__':
    main()
