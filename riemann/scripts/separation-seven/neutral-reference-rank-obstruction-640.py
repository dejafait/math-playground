#!/usr/bin/env python3
"""Fixed638/639 test. Eigenvectors propose; exact rational arithmetic certifies.

No source artifacts are mutated. All saved binary64 entries are interpreted
as exact dyadics. Full2044 vectors have explicitly zero omitted coordinates.
"""
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
TARGET = "Test whether the exact two-moment correction to C999k's reference inverse can raise certificate598's complete joint2044 lower matrix to .000999, starting with a certified three-dimensional rank obstruction."
EXPECTED = {
    'joint-galerkin-family-certificate-598.json': '42a2b96a000ec519cb926a752e32bf364c3e880cfb06436d59a6ecc4cdbfb290',
    'joint-galerkin-family-certificate-598.npz': 'f5035b5e28bf85b7b8329a6675f910a8545208ad931bb983938ee14f30970876',
    'joint-galerkin-family-ledger-598.json': 'd531db86b4b1c98ae9e41a9c973d8d5528336c7e6e6b0649c921b16df587dce2',
}
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def encode(x):
    return {'numerator': str(x.numerator), 'denominator': str(x.denominator)}
def emat(a):
    return [[encode(x) for x in row] for row in a]
def dd_lower(a):
    return min(a[i][i] - sum(abs(a[i][j]) for j in range(3) if i != j) for i in range(3))
def determinant(a):
    if len(a) == 1:
        return a[0][0]
    return sum(((-1)**j * a[0][j] * determinant([r[:j] + r[j+1:] for r in a[1:]])
                for j in range(len(a))), Q(0))

checks = []
def check(ok, label):
    checks.append({'check': label, 'passed': bool(ok)})
    if not ok:
        raise ValueError(label)

report = {'target': TARGET, 'required_floor': encode(Q(999, 10**6)),
          'input_sha256': {}, 'checks': checks, 'failures': [],
          'qualification': 'Only the pinned lower matrix plus any rank-at-most-two correction is stopped; no upper bound on the actual comparison, S3 counterexample or RH conclusion.'}
try:
    for name, expected in EXPECTED.items():
        report['input_sha256'][name] = sha(BASE / name)
        check(report['input_sha256'][name] == expected, 'pinned input ' + name)
    cert = json.loads((BASE / 'joint-galerkin-family-certificate-598.json').read_text())
    ledger = json.loads((BASE / 'joint-galerkin-family-ledger-598.json').read_text())
    check(cert['archive']['sha256'] == EXPECTED['joint-galerkin-family-certificate-598.npz'], 'certificate archive pin')
    check(cert['failures'] == ['quarter_comparison factor unavailable'], 'original failure preserved')
    check(ledger['failures'] == [] and all(c['passed'] for c in ledger['checks']), 'saved ledger checks all pass')
    check(ledger['certificate_sha256'] == EXPECTED['joint-galerkin-family-certificate-598.json'], 'ledger certificate pin')
    check(sha(BASE / 'joint-galerkin-family-certificate-598.py') == cert['script_sha256'], '598 executed source pin')
    check(sha(BASE / 'joint-galerkin-family-ledger-598.py') == ledger['script_sha256'], '598 ledger source pin')
    for name, expected in cert['input_hashes'].items():
        check(sha(BASE / name) == expected, '598 inherited input preserved ' + name)
    with np.load(BASE / 'joint-galerkin-family-certificate-598.npz', allow_pickle=False) as arrays:
        matrix = arrays['comparison_lower'].copy()
    check(matrix.shape == (2044, 2044), 'complete2044 dimensions')
    check(np.isfinite(matrix).all() and np.array_equal(matrix, matrix.T), 'finite symmetric exact dyadic matrix')
    # One fixed32-dimensional coordinate subspace, both independent endpoints.
    # A small eigensolve is only a proposal, never a proof premise.
    indices = list(range(16)) + list(range(1022, 1038))
    principal = matrix[np.ix_(indices, indices)]
    values, proposal = np.linalg.eigh(principal)
    denominator = 2**24
    integers = np.rint(proposal[:, :3] * denominator).astype(np.int64)
    x = [[Q(int(integers[i, j]), denominator) for j in range(3)] for i in range(32)]
    m = [[Q.from_float(float(principal[i, j])) for j in range(32)] for i in range(32)]
    gram = [[sum(x[k][i]*x[k][j] for k in range(32)) for j in range(3)] for i in range(3)]
    mx = [[sum(m[i][k]*x[k][j] for k in range(32)) for j in range(3)] for i in range(32)]
    threshold = Q(999, 10**6)
    compression = [[sum(x[k][i]*mx[k][j] for k in range(32)) - threshold*gram[i][j] for j in range(3)] for i in range(3)]
    negative = [[-compression[i][j] for j in range(3)] for i in range(3)]
    gram_lower, negative_lower = dd_lower(gram), dd_lower(negative)
    report['witness'] = {'ambient_dimension': 2044, 'support_indices_zero_based': indices,
                         'omitted_coordinates': 'exactly zero', 'denominator': denominator,
                         'integer_columns_by_row': integers.tolist()}
    report['exact'] = {'gram': emat(gram), 'shifted_compression': emat(compression),
                       'gram_diagonal_dominance_lower': encode(gram_lower),
                       'negative_compression_diagonal_dominance_lower': encode(negative_lower)}
    minors = {key: [determinant([r[:k] for r in a[:k]]) for k in range(1, 4)]
              for key, a in [('gram', gram), ('negative_shifted_compression', negative)]}
    report['exact']['leading_principal_determinants'] = {key: [encode(x) for x in vals]
                                                        for key, vals in minors.items()}
    report['diagnostic_only'] = {'unshifted_principal_first_three_eigenvalues': values[:3].tolist()}
    check(gram_lower > Q(999, 1000), 'exact entire Gram dominates .999 I3: independence')
    check(negative_lower > Q(8, 100), 'exact entire negative shifted compression dominates .08 I3')
    check(all(val > 0 for vals in minors.values() for val in vals), 'alternate exact Sylvester signs all positive')
    check(all(sha(BASE / name) == expected for name, expected in EXPECTED.items()), 'original inputs unchanged after calculation')
    report['result'] = 'FIXED_LOWER_MATRIX_RANK_TWO_REPAIR_IMPOSSIBLE'
except Exception as exc:
    report['failures'].append(type(exc).__name__ + ': ' + str(exc))
    report['result'] = 'INCONCLUSIVE'
report['script_sha256'] = sha(Path(__file__))
out = BASE / 'neutral-reference-rank-obstruction-640.json'
out.write_text(json.dumps(report, indent=2) + '\n')
print('Result:', report['result'])
if 'exact' in report:
    for key, required in [('gram_diagonal_dominance_lower', '.999'), ('negative_compression_diagonal_dominance_lower', '.08')]:
        val = report['exact'][key]
        print(key, 'actual:', float(Q(int(val['numerator']), int(val['denominator']))), 'required strictly greater than:', required)
print('Required target floor: .000999; exact rational checks, rounding allowance zero.')
print('Failures:', report['failures'])
print('Full certificate:', out.relative_to(BASE.parent.parent))
