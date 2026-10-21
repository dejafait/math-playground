"""Independent atom-based scalar audit plus full prior PSD evidence checks.

Imports no constructor or optimizer. The unchanged complete PSD verifier
must be rerun separately; its full saved blocks are consumed here.
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
OUT = ROOT / 'simultaneous-shell-ordinary-scalars-verification.json'


def enc(x):
    x = Q(x)
    return [x.numerator, x.denominator]


def main():
    data = json.loads((ROOT / 'simultaneous-shell-ordinary-scalars-results.json').read_text())
    lp = json.loads((ROOT / 'delsarte-lp-results.json').read_text())
    null = json.loads((ROOT / 'full-shell-nullspace-results.json').read_text())
    simultaneous = json.loads((ROOT / 'simultaneous-five-six-shell-results.json').read_text())
    psd = json.loads((ROOT / 'simultaneous-five-six-shell-verification.json').read_text())
    text5 = (NB / 'lemmas/L056-released-zero-five-shell-nonexclusion.md').read_text()
    text60 = (NB / 'lemmas/L060-full-shell-one-column-psd-extension.md').read_text()
    checks, failures, rows = [], [], []

    def check(name, condition):
        checks.append(name)
        if not condition:
            failures.append(name)

    check('input_failures_empty', all(not v['failures'] for v in [data, lp, null, simultaneous, psd]))
    check('constructor_input_hashes', all(hashlib.sha256((NB/name).read_bytes()).hexdigest() == digest
                                          for name, digest in data['source_hashes'].items()))
    check('same_full_PSD_input_hash', psd['source_sha256'] == hashlib.sha256(
        (ROOT / 'simultaneous-five-six-shell-results.json').read_bytes()).hexdigest())
    primal = [Q(v['numerator'], v['denominator']) for v in lp['exact']['primal']]
    pairs = [Q(1)]+[Q(0)]*4+[v/(2*comb(68, h)*comb(956, h))
                             for h, v in zip(range(5, 69), primal)]
    check('all_required_pairs', data['pairs_through_12'] == list(map(enc, pairs[:13])))
    check('distinct_pair_upper_bound', all(0 <= p <= pairs[5] for p in pairs[1:13]))
    shell = {(int(r), int(q)): Q(v)/(comb(5, int(r))*comb(63, int(r))*comb(5, int(q))*comb(951, int(q)))
             for r, q, v in re.findall(r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', text5, re.M)}
    shell[0, 0] = Q(1)
    poly = {name: Q(v) for name, v in re.findall(r'^\| (A|B0|C0) \| (-?[0-9]+/[0-9]+) \|$', text60, re.M)}
    star = -poly['B0']/(2*poly['A'])
    free = [tuple(v) for v in null['free']]
    ci = dict(zip(free, [Q(*v) for v in null['nonnegative_test']['intercept']]))
    cs = dict(zip(free, [Q(*v) for v in null['nonnegative_test']['slope']]))
    column = {(i, j): ci[i, j]+star*cs[i, j] if i+j <= 5
              else shell[6-i, i] if i+j == 6 else Q(0)
              for i, j in itertools.product(range(6), repeat=2)}
    relations = [(r, q) for r in range(7) for q in range(7) if r+q >= 6]
    six = {(r, q): Q(*v)/(comb(6, r)*comb(62, r)*comb(6, q)*comb(950, q))
           for (r, q), v in zip(relations, simultaneous['exact']['z'])}
    six[0, 0] = Q(1)
    for r in range(6):
        six[r, 5-r] = pairs[5]*column[5-r, r]/pairs[6]
    boolean_rows, forbidden_rows = 0, 0
    upper_ratios = []
    for index, record in enumerate(data['types']):
        l, m, i, j = record['type']
        atoms = [956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i]
        y = pairs[5]*shell.get((5-i, 5-j), Q(0)) if l == m == 5 else (
            pairs[5]*column[i, j] if (l, m) == (5, 6) else pairs[6]*six.get((6-i, 6-j), Q(0)))
        check(f'unchanged_entry_{index}', enc(y) == record['y'])
        check(f'same_PSD_moment_{index}', psd['completed_presentations'][index]['moment'] == enc(y)
              and psd['completed_presentations'][index]['layers'] == [l, m]
              and psd['completed_presentations'][index]['intersections'] == [i, j])
        invariant = i-j
        for order_index, order in enumerate(itertools.permutations(range(3))):
            transformed = [0]*8
            for mask, size in enumerate(atoms):
                newmask = sum(4 >> k for k, h in enumerate(order) if mask & (4 >> h))
                transformed[newmask] = size
            aa, bb = transformed[4]+transformed[5], transformed[4]+transformed[6]
            h = transformed[2]+transformed[6]
            tt, ss = transformed[4], transformed[3]
            saved = record['presentations'][order_index]
            slacks = [y, pairs[aa]-y, 1+y-pairs[aa]-pairs[bb]]
            check(f'complete_source_row_{index}_{order_index}',
                  saved['atoms'] == transformed and saved['source_indices'] == [aa, bb, tt, ss]
                  and saved['third_distance'] == h and tt-ss == invariant
                  and h == aa+bb-tt-ss and saved['slacks'] == list(map(enc, slacks)))
            check(f'every_scalar_sign_{index}_{order_index}', all(s >= 0 for s in slacks))
            if 0 in [aa, bb, h]:
                boolean_rows += 1
                check(f'Boolean_pair_{index}_{order_index}', y == pairs[max(aa, bb, h)])
            else:
                check(f'distinct_lower_uniform_bound_{index}_{order_index}',
                      slacks[2] >= 1-2*pairs[5] > 0)
                if all(pairs[d] > 0 for d in [aa, bb, h]):
                    ratio = y/min(pairs[d] for d in [aa, bb, h])
                    upper_ratios.append(ratio)
                    check(f'all_three_pair_upper_bounds_{index}_{order_index}', 0 <= ratio <= 1)
            if any(1 <= d <= 4 for d in [aa, bb, h]):
                forbidden_rows += 1
                check(f'forbidden_zero_{index}_{order_index}', y == 0)
            rows.append({'type': record['type'], 'order': list(order),
                         'source_indices': [aa, bb, tt, ss], 'y': enc(y),
                         'slacks': list(map(enc, slacks))})
    # Full existing PSD verification is checked, rather than its summary alone.
    check('full_PSD_verifier_check_count', len(psd['check_names']) == 1928)
    check('same_PSD_witness', psd['complete_z'] == simultaneous['exact']['z'])
    positive, zero = 0, 0
    for block in psd['complete_blocks']:
        # Field names are those of the independent existing verifier.
        a, b = block['a'], block['b']
        c55, c56, c66 = [Q(*block[k]) for k in ['five', 'cross', 'six']]
        remainder = c66-c56*c56/c55 if c55 > 0 else c66
        check(f'complete_singular_Schur_{a}_{b}', c55 >= 0 and remainder >= 0
              and (c55 != 0 or c56 == 0) and enc(remainder) == block['remainder'])
        positive += remainder > 0
        zero += remainder == 0
    check('all_49_modes', len(psd['complete_blocks']) == 49 and positive == 20 and zero == 29)
    summary = {'checks': len(checks), 'failures': len(failures), 'scalar_rows': 3*len(rows),
               'presentations': len(rows), 'Boolean_presentations': boolean_rows,
               'forbidden_presentations': forbidden_rows, 'PSD_modes': len(psd['complete_blocks']),
               'positive_zero_remainders': [positive, zero],
               'minimum_scalar_slack': enc(min(Q(*s) for row in rows for s in row['slacks'])),
               'distinct_upper_ratio_below_one': max(upper_ratios) < 1,
               'maximum_distinct_upper_ratio': enc(max(upper_ratios)),
               'distinct_lower_bound': enc(1-2*pairs[5]),
               'scalar_plus_PSD_feasible': not failures}
    OUT.write_text(json.dumps({'summary': summary, 'rows': rows,
                              'checks': checks, 'failures': failures}, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print('Certificate:', OUT.relative_to(NB))
    if failures:
        raise SystemExit(str(failures))


if __name__ == '__main__':
    main()
