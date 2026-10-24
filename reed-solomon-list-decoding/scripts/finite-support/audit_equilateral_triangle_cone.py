"""Independent finite checks for L108; no optimizer or cone witness is used.

Import only L021's canonical rational vector. Group averaging and finite
Farkas are audited symbolically in L108, not certified by this script.
"""
import hashlib
import itertools
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = BASE / 'delsarte-lp-results.json'
OUT = BASE / 'equilateral-triangle-cone-critical-audit.json'


def encode(x):
    x = F(x)
    return dict(numerator=x.numerator, denominator=x.denominator)


def indices(A, B, Z):
    return (len(A-B), len(A-Z), len((A-B) & (A-Z)),
            len((B-A) & (Z-A)))


def multiplicity(i, j, t, s):
    return comb(i, t)*comb(68-i, j-t)*comb(i, s)*comb(956-i, j-s)


checks = {}


def check(name, condition):
    assert name not in checks
    checks[name] = bool(condition)


source = json.loads(SOURCE.read_text())
a = [F(x['numerator'], x['denominator']) for x in source['exact']['primal']]
H = comb(1024, 68)
N = 65537**28 // 2**128 + 1
U = F(comb(1024, 64), comb(68, 64))
alpha = 2*F(N-1, U-1)
check('vector_length', len(a) == 64)
check('vector_positive', all(x > 0 for x in a))
check('vector_objective', sum(a) == U-1)
check('N_floor', (N-1)*2**128 <= 65537**28 < N*2**128)
check('nontrivial_parameters', H > N > 2 and alpha > 0)
g = [comb(68, i)*comb(956, i) for i in range(69)]
c = [F(1)] + [F(0)]*4 + [alpha*a[i-5]/(2*g[i]) for i in range(5, 69)]
check('pair_objective', sum(g[i]*c[i] for i in range(69)) == N)
check('neighbor_partition', sum(g) == H)
universe = set(range(1024))
rows = []
for i in range(1, 69):
    # Actual complete sets, not a test on formal distance triples alone.
    K = set(range(68-i))
    P = set(range(68-i, 68))
    Q = set(range(68, 68+i))
    R = set(range(68+i, 68+2*i))
    supports = [K | P, K | Q, K | R]
    A, B, Z = supports
    check(f'distinct_supports_{i}', len({frozenset(X) for X in supports}) == 3)
    check(f'weights_{i}', all(len(X) == 68 and X <= universe for X in supports))
    atoms = []
    for bits in itertools.product((0, 1), repeat=3):
        atom = set(universe)
        for X, bit in zip(supports, bits):
            atom &= X if bit else universe-X
        atoms.append(dict(bits=list(bits), size=len(atom)))
    expected_atoms = [956-2*i, i, i, 0, i, 0, 0, 68-i]
    check(f'eight_atoms_{i}', [x['size'] for x in atoms] == expected_atoms)
    presentations = []
    for order in itertools.permutations(range(3)):
        X, Y, V = [supports[k] for k in order]
        ii, jj, t, s = indices(X, Y, V)
        h = len(Y-V)
        actual_D = multiplicity(ii, jj, t, s)
        tag = ''.join(map(str, order))
        check(f'indices_{i}_{tag}', (ii, jj, t, s) == (i, i, i, 0))
        check(f'third_distance_{i}_{tag}', h == ii+jj-t-s == i)
        check(f'ranges_{i}_{tag}',
              max(0, ii+jj-68) <= t <= min(ii, jj) and
              max(0, ii+jj-956) <= s <= min(ii, jj))
        check(f'multiplicity_{i}_{tag}', actual_D == comb(956-i, i) > 0)
        presentations.append(dict(order=list(order), indices=[ii, jj, t, s],
                                  h=h, t_minus_s=t-s, multiplicity=actual_D))
    repetitions = [indices(A, B, V) for V in (A, B)]
    check(f'repeated_indices_{i}', repetitions == [(i, 0, 0, 0), (i, i, i, i)])
    check(f'repeated_multiplicities_{i}',
          all(multiplicity(*entry) == 1 for entry in repetitions))
    demand = N*c[i]-2*c[i]
    edges = H*g[i]//2
    coefficient = edges*demand
    check(f'nonnegative_pair_{i}', c[i] >= 0)
    check(f'distinct_demand_{i}', demand == (N-2)*c[i] >= 0)
    check(f'unordered_edges_{i}', 2*edges == H*g[i])
    check(f'adjacent_shell_count_{i}', g[i]*i*i == g[i-1]*(69-i)*(957-i))
    check(f'pairing_coefficient_{i}', coefficient == F(H*(N-2), 2)*g[i]*c[i] >= 0)
    if i <= 4:
        check(f'null_class_retained_{i}', demand == coefficient == 0 and edges > 0)
    rows.append(dict(i=i, supports=[sorted(X) for X in supports], atoms=atoms,
                     presentations=presentations, repetitions=[list(x) for x in repetitions],
                     g=g[i], c=encode(c[i]), demand=encode(demand),
                     unordered_edges=edges, pairing_coefficient=encode(coefficient)))

# At i=0 there is one repeated support, and no graph edge.
check('coincident_repetitions', indices(A, A, A) == (0, 0, 0, 0))
for j in range(69):
    check(f'diagonal_contraction_{j}', multiplicity(0, j, 0, 0) == g[j])
check('all_unordered_edges', sum(r['unordered_edges'] for r in rows) == H*(H-1)//2)
check('total_demand', sum(F(r['pairing_coefficient']['numerator'],
                            r['pairing_coefficient']['denominator']) for r in rows)
      == F(H*(N-2)*(N-1), 2))
failures = [name for name, passed in checks.items() if not passed]
data = dict(scope='Finite L108 audit; symbolic averaging and Farkas remain in the manuscript.',
            input_path='scripts/finite-support/delsarte-lp-results.json',
            input_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            H=H, N=N, U=encode(U), alpha=encode(alpha), coordinates=rows,
            dual_minimum=0, strict_separator_requirement='pairing < 0',
            check_count=len(checks), checks=checks, failures=failures)
OUT.write_text(json.dumps(data, indent=2)+'\n')
print(f'L108 independent finite audit: {len(checks)} checks; failures: {failures}')
print('68 actual equal-side triangles; 408 presentations; 136 distinct-edge repetitions.')
print('All 68 unordered pairing coefficients >= 0; actual dual minimum 0; separator requires < 0.')
print('The dual minimum also uses the symbolic averaging and sign proof in L108.')
print(f'Full certificate: {OUT}')
assert not failures
