"""Exact finite gauge-jet sign check for L156; no mesh asymptotic computation."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import json


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def determinant(a, b, c):
    return dot(a, cross(b, c))


def basis(j):
    return [tuple(int(3*v+c == j) for c in range(3)) for v in range(4)]


def gradient(phi):
    return [tuple(phi[(e+1) % 4][c]-phi[e][c] for c in range(3))
            for e in range(4)]


def third_action(h, g, q):
    vectors = (h, g, q)
    return -F(1, 2) * sum(
        determinant(vectors[p[0]][i], vectors[p[1]][j], vectors[p[2]][k])
        for i, j, k in combinations(range(4), 3)
        for p in permutations(range(3)))


checks = []
for hi, pi, qi in product(range(12), repeat=3):
    h, phi, psi = basis(hi), basis(pi), basis(qi)
    g, q = gradient(phi), gradient(psi)
    # D_1 is (1,1,1,1) in the four oriented traversal coordinates.
    lh = tuple(sum(h[e][c] for e in range(4)) for c in range(3))
    bracket = []
    for e in range(4):
        endpoints = tuple(phi[e][c]+phi[(e+1) % 4][c] for c in range(3))
        bracket.append(tuple(-x for x in cross(q[e], endpoints)))
    actual = third_action(h, g, q)
    required = -F(1, 2) * sum(dot(lh, b) for b in bracket)
    checks.append(dict(h=hi, phi=pi, psi=qi, actual=str(actual),
                       required=str(required), error=str(actual-required),
                       passed=actual == required))
normalization = -36 * (-F(1, 6)) * (-F(1, 12))
failures = [i for i, row in enumerate(checks) if not row['passed']]
if normalization != -F(1, 2):
    failures.append('normalization')
path = Path(__file__).with_name('cubic-gradient-ward-certificate.json')
path.write_text(json.dumps(dict(
    scope='Complete one-cycle action gauge-jet basis check; not the actual residual or a cutoff test',
    checks=checks, check_count=len(checks),
    nonzero_checks=sum(row['actual'] != '0' for row in checks),
    maximum_absolute_error=str(max(abs(F(row['error'])) for row in checks)),
    normalization=dict(actual=str(normalization), required='-1/2'),
    failures=failures, passed=not failures), indent=2) + '\n')
print(f'Gauge-jet basis checks: {len(checks)-len([i for i in failures if isinstance(i, int)])}/{len(checks)} pass.')
print(f'Maximum exact error: {max(abs(F(row["error"])) for row in checks)}; required: 0.')
print(f'Contraction factor: {normalization}; required: -1/2.')
print(f'Failures: {failures}. Certificate: {path.relative_to(Path.cwd())}')
assert not failures
