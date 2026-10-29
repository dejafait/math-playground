#!/usr/bin/env python3
"""Bind the complete step-554/556 replay and check supplementary evidence.

Run after both existing producer and independent receiver. Does not claim
independent reception of the higher-weight histogram bins.
"""

import json
from pathlib import Path


def apply(row, values):
    value = 0
    for i, item in enumerate(values):
        if row & (1 << i):
            value ^= item
    return value


def reduce(row, pivots):
    for bit in sorted(pivots, reverse=True):
        if row & (1 << bit):
            row ^= pivots[bit]
    return row


def main():
    base = Path('scripts/batched-incidence')
    old_dir, new_dir = base / 'output-554', base / 'output-556'
    checks, supplementary, failures = [], [], []

    def check(name, actual, required):
        passed = actual == required
        checks.append({'check': name, 'actual': actual, 'required': required,
                       'passed': passed})
        if not passed:
            failures.append(name)

    certificates = [directory / 'two-local-source-certificate.json'
                    for directory in (old_dir, new_dir)]
    receipts = [directory / 'two-local-source-receipt.json'
                for directory in (old_dir, new_dir)]
    old, new = [json.loads(path.read_text()) for path in certificates]
    check('complete nested certificate equality', old == new, True)
    old_receipt, new_receipt = [json.loads(path.read_text()) for path in receipts]
    for receipt, certificate in zip((old_receipt, new_receipt), certificates):
        check(f'receipt input binding {certificate.parent.name}',
              receipt['input'], str(certificate))
    check('complete nested receipt equality except explicitly bound input',
          {k: v for k, v in old_receipt.items() if k != 'input'} ==
          {k: v for k, v in new_receipt.items() if k != 'input'}, True)

    check('exact case list', [case['N'] for case in new['cases']], [4, 8])
    for case in new['cases']:
        n = case['N']
        details = {'N': n, 'pairs': {}, 'AV_coefficient_checks': []}
        for label, test in case['local_tests'].items():
            left, right = case[label[0]], case[label[1]]
            width = len(left['vertices']) + len(right['vertices'])
            prefix = f'N={n} {label}'
            expected_names = [label[0] + ':' + v for v in left['vertices']]
            expected_names += [label[1] + ':' + v for v in right['vertices']]
            check(prefix + ' coordinate names', test['coordinate_names'], expected_names)
            check(prefix + ' pair/N metadata', [test['pair'], test['N']], [label, n])
            pivots = {int(bit): row for bit, row in test['low_weight_span_pivots'].items()}
            basis = test['low_weight_span_basis']
            columns = test['residual_columns_bits']
            shift = test['block_shift_rows']
            check(prefix + ' valid echelon pivots',
                  all(0 < row < 1 << width and row.bit_length() - 1 == bit
                      and apply(row, columns) == 0 for bit, row in pivots.items()), True)
            check(prefix + ' pivot and independently received basis counts',
                  len(pivots), len(basis))
            check(prefix + ' all received basis rows in stored pivot span',
                  all(reduce(row, pivots) == 0 for row in basis), True)
            initial = test['initial_pair']
            check(prefix + ' stored initial remainder',
                  test['initial_remainder'], reduce(initial, pivots))
            check(prefix + ' all stored Krylov remainders',
                  test['paired_krylov_span_remainders'],
                  [reduce(row, pivots) for row in test['paired_krylov_rows']])
            images = [apply(row, shift) for row in basis]
            remainders = [reduce(row, pivots) for row in images]
            check(prefix + ' every stored shift image', test['shifted_pool_basis'], images)
            check(prefix + ' every stored shift remainder',
                  test['shifted_pool_basis_remainders'], remainders)
            check(prefix + ' invariant image count', len(images), len(basis))
            check(prefix + ' initial membership binding',
                  test['initial_in_low_weight_span'], reduce(initial, pivots) == 0)
            check(prefix + ' invariant binding', test['low_weight_span_is_invariant'],
                  not any(remainders))
            check(prefix + ' source realization not claimed', test['source_graphs_constructed'], False)
            details['pairs'][label] = {'basis_rows': len(basis),
                                      'shift_images_checked': len(images),
                                      'krylov_rows_checked': len(test['paired_krylov_rows'])}

        a, v = case['A'], case['V']
        offset = len(a['vertices'])
        ai, vi = ({name: i for i, name in enumerate(graph['vertices'])}
                  for graph in (a, v))
        test = case['local_tests']['AV']
        count = 0
        for pool in test['all_weight_at_most_six_rows_by_weight']:
            for row in pool:
                u, w = row & ((1 << offset) - 1), row >> offset
                r = sum(((u >> ai[f'f{n-1-j}']) & 1) << j for j in range(n))
                powers, polynomial = [], 1
                for _ in range(n):
                    powers.append(polynomial)
                    polynomial ^= polynomial << 1
                q = apply(r, powers)
                low_a = sum(((u >> ai[f'h{n-j}']) & 1) << (j-1) for j in range(1, n+1))
                b = sum(((w >> vi[f'd{n-j}']) & 1) << (j-1) for j in range(1, n+1))
                c = sum(((w >> vi[f'd{2*n-j}']) & 1) << (j-1) for j in range(1, n+1))
                valid = (b == q and low_a == (b ^ c)
                         and ((u >> ai['t']) & 1) == ((w >> vi['t']) & 1)
                         and row.bit_count() >= r.bit_count() + 2 * q.bit_count())
                details['AV_coefficient_checks'].append({'row_bits': row, 'r_bits': r,
                    'q_bits': q, 'a_bits': low_a, 'b_bits': b, 'c_bits': c,
                    'actual_weight': row.bit_count(),
                    'required_lower_bound': r.bit_count() + 2 * q.bit_count(), 'passed': valid})
                if not valid:
                    failures.append(f'N={n} AV coefficient/charge row {row}')
                count += 1
        check(f'N={n} all admitted AV coefficient rows', count, sum(test['low_weight_counts']))

        u_names = [f'f{i}' for i in range(n // 2)] + ['h0', f'h{n//2}']
        v_names = ['d0', f'd{n//2}']
        u = sum(1 << ai[name] for name in u_names)
        w = sum(1 << vi[name] for name in v_names)
        lhs, rhs = apply(u, a['all_residual_polynomial_bits']), apply(w, v['all_residual_polynomial_bits'])
        expected = sum(1 << j for j in (n//2, n, 3*n//2, 2*n))
        check(f'N={n} displayed witness full residuals', [lhs, rhs], [expected, expected])
        check(f'N={n} displayed witness weight', u.bit_count() + w.bit_count(), 6 if n == 4 else 8)
        check(f'N={n} displayed witness forced coordinate', (u >> ai['f0']) & 1, 1)
        details['displayed_witness'] = {'u_bits': u, 'v_bits': w,
            'left_residual_bits': lhs, 'right_residual_bits': rhs,
            'required_residual_bits': expected, 'weight': u.bit_count() + w.bit_count()}
        supplementary.append(details)

    output = new_dir / 'audit-replay-comparison.json'
    report = {'scope': 'Complete replay binding plus supplementary fields, all admitted AV coefficient charges and displayed witnesses; higher-weight histograms only replayed.',
              'certificates': [str(path) for path in certificates],
              'receipts': [str(path) for path in receipts],
              'checks': checks, 'supplementary': supplementary,
              'failures': failures}
    output.write_text(json.dumps(report, indent=2) + '\n')
    print(f'Exact checks: {sum(check["passed"] for check in checks)}/{len(checks)}')
    for item in supplementary:
        rows = item['AV_coefficient_checks']
        print(f'N={item["N"]}: full AV charges {sum(row["passed"] for row in rows)}/{len(rows)}; '
              f'displayed witness weight {item["displayed_witness"]["weight"]}; cap 6')
    print('Failures:', failures)
    print('Full audit certificate:', output)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
