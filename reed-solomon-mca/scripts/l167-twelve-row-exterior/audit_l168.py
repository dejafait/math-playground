#!/usr/bin/env python3
"""Separate L168 audit. Never regenerates or imports either original program.

All fields of both load-bearing reconstructions are compared, including the
full stack and minor. Bareiss exact-division elimination provides a third
determinant path, distinct from modular and rational Gaussian elimination.
"""
from hashlib import sha256
from itertools import combinations
from math import prod
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
J = [47, 50, 64, 70, 75, 79, 85, 89, 96]
IDS = [2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16]
MINOR_ROWS = [6, 7, 2, 3, 4, 8, 9, 13, 14, 10, 12, 15, 16, 11,
              18, 0, 1, 17, 5, 19, 20]
DET = -564277021063479563603400000


def bareiss(matrix):
    a = [row[:] for row in matrix]
    previous, sign, trace = 1, 1, []
    for k in range(len(a) - 1):
        pos = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pos is None:
            return 0, trace
        if pos != k:
            a[k], a[pos] = a[pos], a[k]
            sign = -sign
        pivot = a[k][k]
        divisions = 0
        for i in range(k + 1, len(a)):
            for j in range(k + 1, len(a)):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                value, remainder = divmod(numerator, previous)
                if remainder:
                    raise ArithmeticError('Bareiss division not exact')
                a[i][j] = value
                divisions += 1
            a[i][k] = 0
        trace.append({'column': k, 'swap_with': pos, 'pivot': pivot,
                      'divisor': previous, 'exact_divisions': divisions})
        previous = pivot
    return sign * a[-1][-1], trace


def rank(matrix):
    # Auxiliary prefix checks only; the Bareiss minor is the rank certificate.
    basis = []
    for row in matrix:
        v = row[:]
        for col, b in basis:
            t = v[col]
            v = [(x - t*y) % P for x, y in zip(v, b)]
        col = next((i for i, x in enumerate(v) if x), None)
        if col is not None:
            t = pow(v[col], P-2, P)
            basis.append((col, [x*t % P for x in v]))
    return len(basis)


def main():
    paths = [HERE/'certificate.json', HERE/'verification.json',
             ROOT/'lemmas/L167-completed-family-marked-extraction-counterexample.md',
             ROOT/'lemmas/L109-seven-coordinate-parameter-free-support-filter.md']
    raw = {str(p.relative_to(ROOT)): p.read_bytes() for p in paths}
    hashes = {name: sha256(value).hexdigest() for name, value in raw.items()}
    c = json.loads(paths[0].read_text())
    v = json.loads(paths[1].read_text())
    checks, failures = [], []

    def check(name, actual, required):
        ok = actual == required
        checks.append({'name': name, 'passed': ok})
        if not ok:
            failures.append({'name': name, 'actual': actual, 'required': required})

    check('97 prime by trial division', all(P % d for d in range(2, 10)), True)
    check('original source hashes', c['source_sha256'],
          {str(p.relative_to(ROOT)): hashes[str(p.relative_to(ROOT))] for p in paths[2:]})
    check('verification pins original certificate', v['certificate_sha256'],
          hashes[str(paths[0].relative_to(ROOT))])
    text = paths[2].read_text()
    table_text = text.split('| Row | Class | A intersection S | A intersection J |\n', 1)[1]
    table = []
    for line in table_text.splitlines()[1:]:
        if not line.startswith('|'):
            break
        cells = [s.strip() for s in line.strip('|').split('|')]
        table.append({'id': int(cells[0]), 'I': list(map(int, cells[2].split(','))),
                      'K': list(map(int, cells[3].split(',')))})
    check('all sixteen canonical row IDs', [r['id'] for r in table], list(range(1, 17)))
    check('entire canonical table', c['canonical_table'], table)
    selected = [r for r in table if len(r['I']) == 2]
    check('complete overlap-two rows', [r['id'] for r in selected], IDS)
    check('saved complete E2', c['E2_rows'], IDS)
    check('all row parts in original partition',
          all(set(r['I']) <= set(S) and set(r['K']) <= set(J) and
              len(r['I']) + len(r['K']) == 4 for r in table), True)
    h = sorted(S+J)
    check('fixed H exactly all sixteenth roots', h,
          [x for x in range(1, P) if pow(x, 16, P) == 1])
    check('modulus/ordered parts', [c['modulus'], c['S'], c['J']], [P, S, J])
    pairs = list(combinations(range(7), 2))
    check('all 21 exterior column labels', c['column_pairs'], [[S[a], S[b]] for a, b in pairs])
    blocks, stack, identities, polys, denominators, prefixes = [], [], [], [], [], []
    for row in selected:
        n, overlap, outside = row['id'], row['I'], row['K']
        roots = [x for x in J if x not in outside]
        coeff = [1]
        for y in roots:
            # Integer coefficients, without intermediate residue reduction.
            coeff = [-y*coeff[0]] + [coeff[i-1]-y*coeff[i]
                                     for i in range(1, len(coeff))] + [coeff[-1]]
        g = {x: prod(x-y for y in roots) % P for x in h}
        check(f'{n}: all exact product/polynomial values',
              [sum(a*x**i for i, a in enumerate(coeff)) % P for x in h],
              [g[x] for x in h])
        check(f'{n}: complete zero/nonzero domain', [x for x in h if not g[x]], roots)
        o = [x for x in S if x not in overlap]
        z, rest = o[0], o[1:]
        check(f'{n}: all normalization denominators nonzero', all(g[x] for x in o), True)
        inverses = {x: pow(g[x], P-2, P) for x in o}
        check(f'{n}: every denominator inverse', [g[x]*inverses[x] % P for x in o], [1]*5)
        # Images of each standard basis vector under the quotient map.
        images = [[(g[z]*int(a == x)-g[x]*int(a == z)) % P
                   for x in rest] for a in S]
        q = [list(col) for col in zip(*images)]
        d = [[(int(a == x)*inverses[x]-int(a == z)*inverses[z]) % P
              for a in S] for x in rest]
        check(f'{n}: full quotient normalization', q,
              [[g[z]*g[x]*value % P for value in d[i]] for i, x in enumerate(rest)])
        block = []
        for i, j in combinations(range(4), 2):
            block.append([(images[a][i]*images[b][j]-images[b][i]*images[a][j]) % P
                          for a, b in pairs])
            identities.append({'support_row': n, 'pivot': z,
                               'covector_pair': [rest[i], rest[j]]})
        check(f'{n}: all normalized exterior entries', block,
              [[(d[i][a]*d[j][b]-d[i][b]*d[j][a])*g[z]**2*g[rest[i]]*g[rest[j]] % P
                for a, b in pairs] for i, j in combinations(range(4), 2)])
        record = {**row, 'roots': roots, 'g': {str(x): g[x] for x in h},
                  'pivot': z, 'covector_labels': rest, 'Q': q, 'N': block}
        blocks.append(record)
        polys.append({'support_row': n, 'coefficients_ascending': [a % P for a in coeff],
                      'normalized_covectors': d})
        denominators.append({'support_row': n, 'labels': o, 'values': [g[x] for x in o],
                             'inverses': [inverses[x] for x in o]})
        check(f'{n}: original complete block', c['blocks'][len(blocks)-1], record)
        check(f'{n}: verifier complete block', v['blocks'][len(blocks)-1], record)
        check(f'{n}: quotient/exterior dimensions', [rank(q), rank(block)], [4, 6])
        stack.extend(block)
        prefixes.append(rank(stack))
    for name, data in [('producer', c), ('verifier', v)]:
        check(name+': every one of 1512 stack entries', data['stack'], stack)
        check(name+': all twelve blocks', data['blocks'], blocks)
        check(name+': exact selected row ordering', data['minor_row_indices'], MINOR_ROWS)
        check(name+': all minor columns in order', data['minor_column_indices'], list(range(21)))
    check('all 72 support/pivot/covector identities', c['row_identities'], identities)
    check('all polynomial coefficients/normalized covectors', v['polynomial_records'], polys)
    check('all twelve verifier prefix ranks', v['prefix_ranks'], prefixes)
    check('required prefix ranks', prefixes, [6, 12, 18]+[21]*9)
    minor = [stack[i][:] for i in MINOR_ROWS]
    check('entire producer 441-entry minor', c['minor'], minor)
    check('entire verifier 441-entry minor', v['minor'], minor)
    check('all selected row identities', c['minor_row_identities'], [identities[i] for i in MINOR_ROWS])
    determinant, trace = bareiss(minor)
    check('Bareiss exact integer determinant', determinant, DET)
    check('complete verifier integer determinant', v['integer_minor_determinant'], determinant)
    check('nonzero residue', determinant % P, 95)
    for name, data in [('producer', c), ('verifier', v)]:
        check(name+': determinant residue', data['minor_determinant_mod_97'], determinant % P)
        check(name+': complete kernel basis', data['kernel_basis'], [])
        check(name+': rank threshold/kernel summary',
              [data['summary']['actual_rank'], data['summary']['required_rank'],
               data['summary']['kernel_dimension']], [21, 21, 0])
        check(name+': no failures', data['summary']['failures'], [])
    check('all producer pivots', c['pivot_columns'], list(range(21)))
    check('all producer free columns', c['free_columns'], [])
    check('all producer RREF entries', c['rref'],
          [[int(i == j) for j in range(21)] for i in range(72)])
    check('verifier complete kernel residuals', v['kernel_residuals'], [])
    check('original verifier complete check list',
          [len(v['checks']), all(r['passed'] for r in v['checks']), v['summary']['checks']],
          [67, True, 67])
    check('input certificates unchanged',
          {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in paths}, hashes)
    out = {'input_sha256': hashes, 'construction': 'integer products and coefficients; basis images; Bareiss',
           'canonical_table': table, 'E2_rows': IDS, 'blocks': blocks, 'stack': stack,
           'row_identities': identities, 'polynomial_records': polys, 'denominators': denominators,
           'prefix_ranks': prefixes, 'minor_row_indices': MINOR_ROWS,
           'minor_column_indices': list(range(21)), 'minor': minor,
           'integer_minor_determinant': determinant, 'minor_determinant_mod_97': determinant % P,
           'bareiss_trace': trace, 'kernel_basis': [], 'checks': checks,
           'summary': {'actual_rank': 21 if determinant % P else None, 'required_rank': 21,
                       'matrix_shape': [len(stack), len(stack[0])], 'kernel_dimension': 0 if determinant % P else None,
                       'checked_stack_entries': sum(map(len, stack)), 'checked_minor_entries': sum(map(len, minor)),
                       'checks': len(checks), 'failures': failures}}
    dest = HERE/'l168-critical-audit.json'
    dest.write_text(json.dumps(out, indent=2)+'\n')
    print(f'Actual rank {out["summary"]["actual_rank"]}; required 21; residue {determinant % P}; kernel dimension {out["summary"]["kernel_dimension"]}.')
    print(f'Checked 12 blocks, {sum(map(len, stack))} stack entries, {sum(map(len, minor))} minor entries; {len(checks)} checks; {len(failures)} failures.')
    print(f'Complete audit: {dest.relative_to(ROOT)}')
    if failures:
        print('Failed checks:', [f['name'] for f in failures])
        raise SystemExit(1)


if __name__ == '__main__':
    main()
