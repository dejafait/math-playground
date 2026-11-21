#!/usr/bin/env python3
"""Fresh source-audited coefficient/moment reconstruction; no Gram-output audit.

High-level interval formulas and scalar inputs reuse reviewed 487/489 code.
Signed convolution uses a separate centered-digit implementation, retaining
GMP only for exact integer multiplication. All original data are read-only.
Complete comparisons and hashes are checkpointed per column, not sampled.
"""
import argparse
import concurrent.futures as cf
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path
import sys
import time

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('full489audit', HERE/'full-matrix-enclosure-489.py')
q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)
m, B, S = q.m, q.B, q.S
OUT = HERE/'finite-reconstruction-491'
OUT.mkdir(exist_ok=True)


def centered_convolution(a, b):
    """Exact convolution, no nonnegative coefficient offsets.

    Choose base > twice a bound on every signed result coefficient.
    Evaluate each input polynomial at base as a signed integer, multiply,
    then recover its unique centered base expansion by carry adjustment.
    """
    if not a or not b:
        return []
    count = len(a)+len(b)-1
    bound = min(len(a), len(b))*max(map(abs, a))*max(map(abs, b))
    if not bound:
        return [0]*count
    width = ((2*bound).bit_length()+7)//8
    bits, base = 8*width, 1 << (8*width)
    def pack(values):
        positive = b''.join(max(x, 0).to_bytes(width, 'little') for x in values)
        negative = b''.join(max(-x, 0).to_bytes(width, 'little') for x in values)
        return int.from_bytes(positive, 'little')-int.from_bytes(negative, 'little')
    x, y = pack(a), pack(b)
    value = m.fastmul(abs(x), abs(y))
    direction = -1 if (x < 0) != (y < 0) else 1
    packed = value.to_bytes(width*count, 'little')
    out, carry = [], 0
    for k in range(count):
        digit = int.from_bytes(packed[k*width:(k+1)*width], 'little')+carry
        carry = 0
        if digit > base//2:
            digit -= base
            carry = 1
        out.append(direction*digit)
    assert carry == 0
    return out


def self_checks():
    cases = [([2, -3, 7], [-8, 1]), ([0], [3, -4]), ([-4], [-5]),
             ([2**2500, -3, 2**2000], [7, -2**2100, 4]),
             ([-1, -2, -3], [4, -5, 6]), ([1, -1]*20, [-1, 0, 1]*11)]
    checks = {'centered_convolution_all_direct_test_coefficients': all(
        centered_convolution(a, b) == [sum(a[i]*b[k-i] for i in range(len(a))
            if 0 <= k-i < len(b)) for k in range(len(a)+len(b)-1)] for a, b in cases)}
    # Every kernel degree and head monomial: the beta identity underlying
    # the shorter Phi action, not three point evaluations of a polynomial.
    checks['all_24929_kernel_beta_identities'] = all(
        sum((F((-1)**r*comb(j, r), k+r+1) for r in range(j+1)), F(0))
        == F(1, (j+k+1)*comb(j+k, j)) for j in range(97) for k in range(257))
    checks['all_257_integer_legendre_recurrences'] = m.check_integer_polynomials()
    return checks


def initialize():
    # Replacement is local to this audit process, never a file edit.
    m.iconv = centered_convolution
    q.initialize()


def reconstruct(n):
    start = time.monotonic()
    saved_coefficients = q.WORK/f'coefficients-{n}.json.gz'
    saved_column = q.WORK/f'column-{n}.json.gz'
    pieces = m.build_column(n, q.CONST, q.RATIOS[n-2], q.Q, q.H)
    raw = q.loadgz(saved_coefficients)
    saved = q.loadgz(saved_column)
    checks = {}
    checks['all_three_piece_dimensions'] = len(raw) == len(pieces) == 3
    checks['original_coefficient_hash_matches_column'] = hashlib.sha256(
        saved_coefficients.read_bytes()).hexdigest() == saved['coefficients_sha256']
    count = 0
    for j, piece in enumerate(pieces):
        checks[f'{j}_all_neutral_polynomial_endpoints'] = [x.json() for x in piece['g']] == raw[j]['g']
        count += len(piece['g'])
        for sign in (-1, 1):
            pair = piece['signs'][sign]
            for key, pol in zip(('P', 'Q'), pair):
                checks[f'{j}_{sign}_{key}_all_action_endpoints'] = [x.json() for x in pol] == raw[j]['signs'][str(sign)][key]
                count += len(pol)
    for sign in (-1, 1):
        powers = []
        for j, piece in enumerate(pieces):
            pair = piece['signs'][sign]
            pm, qm, u, v = q.moment_numerators(pair)
            left = pm+[0]*(1025-len(pm))+qm+[0]*(257-len(qm))
            saved_dot = q.loadgz(q.WORK/f'dot-{sign}-{j}-{n}.json.gz')
            checks[f'{j}_{sign}_all_1282_midpoint_left_operands'] = left == list(map(int, saved_dot['left']))
            checks[f'{j}_{sign}_all_1282_exact_moment_operands'] = u+v == list(map(int, saved_dot['right']))
            size, error = m.action_size_error(pair)
            checks[f'{j}_{sign}_both_size_error_operands'] = [str(size), str(error)] == saved['signs'][str(sign)]['piece_size_error'][j]
            moments = []
            for x in u[:257]:
                center = B.rational(x, q.DEN*S)
                moments.append(B(center.lo-error, center.hi+error))
            powers.append(moments)
        projected = []
        for k in range(257):
            value = q.ZERO
            for j in range(3):
                value = value+m.interval_dot(q.TRANSFORMS[j][k], powers[j])*q.LENGTHS[j]
            projected.append(q.enc(q.grid(value)))
        checks[f'{sign}_all_257_projection_endpoints'] = projected == saved['signs'][str(sign)]['projected_moments']
    result = {'n': n, 'scope': 'Fresh coefficient/moment operands, not native Gram output.',
              'coefficient_intervals_compared': count, 'checks': checks,
              'input_sha256': {'coefficients': hashlib.sha256(saved_coefficients.read_bytes()).hexdigest(),
                               'column': hashlib.sha256(saved_column.read_bytes()).hexdigest()},
              'failures': [key for key, value in checks.items() if not value]}
    (OUT/f'column-{n}.json').write_text(json.dumps(result, indent=2)+'\n')
    return n, len(checks), count, result['failures'], time.monotonic()-start


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--columns', type=int, nargs='+', default=list(range(2, 257)))
    parser.add_argument('--workers', type=int, default=6)
    parser.add_argument('--skip-self-checks', action='store_true')
    args = parser.parse_args()
    assert all(2 <= n <= 256 for n in args.columns)
    checks = self_checks() if not args.skip_self_checks else {}
    if not all(checks.values()):
        raise RuntimeError(checks)
    print(f'Source primitive checks {sum(checks.values())}/{len(checks)}; reconstructing {len(args.columns)} columns', flush=True)
    with cf.ProcessPoolExecutor(max_workers=args.workers, initializer=initialize) as pool:
        for n, tests, count, failures, elapsed in pool.map(reconstruct, args.columns, chunksize=1):
            print(f'Column {n}: {tests-len(failures)}/{tests}, {count} coefficient intervals; failures={failures}; {elapsed:.1f}s', flush=True)
    columns = [json.loads((OUT/f'column-{n}.json').read_text()) for n in args.columns]
    result = {'scope': 'Source-audited high-level reconstruction; independent centered convolution encoding; same GMP integer multiplication. Native Gram outputs not recomputed.',
              'indices': args.columns, 'checks': checks,
              'complete_255_columns': args.columns == list(range(2, 257)),
              'coefficient_intervals_compared': sum(x['coefficient_intervals_compared'] for x in columns),
              'column_check_count': sum(len(x['checks']) for x in columns),
              'failures': [f'column-{x["n"]}/{key}' for x in columns for key in x['failures']],
              'native_gram_outputs_independently_recomputed': False,
              'full_margin_independently_reviewed': False, 'rh_conclusion': False,
              'column_evidence': str(OUT.relative_to(HERE.parent.parent))}
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Completed {len(columns)}/255 columns; coefficient intervals {result["coefficient_intervals_compared"]}; column checks {result["column_check_count"]}; failures {result["failures"]}; evidence {path}', flush=True)
    print('Required full finite threshold I/25 unchanged; no new matrix bound; native Gram-output audit remains pending.', flush=True)
    if result['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
