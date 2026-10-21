"""Independent exact replay of L062's scalar certificate; no local enumeration."""

from fractions import Fraction
import json
from pathlib import Path


def pair(x):
    return [x.numerator, x.denominator]


def valuation(x, p):
    assert x != 0
    result = 0
    n, d = abs(x.numerator), x.denominator
    while n % p == 0:
        n //= p
        result += 1
    while d % p == 0:
        d //= p
        result -= 1
    return result


def discriminant(a1, a2, a3, a4, a6):
    b2 = a1*a1 + 4*a2
    b4 = a1*a3 + 2*a4
    b6 = a3*a3 + 4*a6
    b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
    return -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6


root = Path(__file__).resolve().parent
original = json.loads((root / 'scalar-certificate.json').read_text())
s = Fraction(9261, 8)
t = s / 1728
q = 1 - t
checks = {}
local = {}
for p, expected_residue in ((5, 2), (11, 4)):
    vp = [valuation(t, p), valuation(q, p)]
    residue = s.numerator * pow(s.denominator, -1, p) % p
    local[str(p)] = {
        't': pair(t), 'q': pair(q),
        'unit_numerators_and_denominator':
            all(n % p != 0 for n in (t.numerator, q.numerator, t.denominator)),
        'actual_valuation_pair': vp,
        'required_valuation_domain': '3*N0 x 4*N0',
        'actual_scalar_residue': residue,
        'required_scalar_residue': expected_residue,
    }
    checks[f'local_{p}_full_field_replay'] = local[str(p)] == original['local'][str(p)]
    checks[f'local_{p}_domain_and_residue'] = (
        vp[0] >= 0 and vp[0] % 3 == 0 and vp[1] >= 0 and vp[1] % 4 == 0
        and residue == expected_residue
    )

replayed_original_checks = {
    't_exact': t == Fraction(343, 512),
    'q_exact': q == Fraction(169, 512),
    'ordinary_scalar': s not in (0, 1728, -24729001),
    'primitive_domain_5': local['5']['actual_valuation_pair'] == [0, 0],
    'compatible_residue_5': local['5']['actual_scalar_residue'] == 2,
    'primitive_domain_11': local['11']['actual_valuation_pair'] == [0, 0],
    'compatible_residue_11': local['11']['actual_scalar_residue'] == 4,
}
checks['original_scalar_exact'] = original['scalar'] == pair(s)
checks['original_checks_full_replay'] = original['checks'] == replayed_original_checks
checks['all_original_checks_true'] = all(replayed_original_checks.values())
checks['original_failures_empty'] = original['failures'] == []
checks['scalar_differences'] = (
    1728-s == Fraction(4563, 8)
    and s-2 == Fraction(5*1849, 8)
    and s-4 == Fraction(11*839, 8)
)
exceptional = {'T': -24729001, '2T': -121, '4T': -32768}
checks['finite_exceptional_values_avoided'] = all(s != x for x in exceptional.values())
d0 = discriminant(0, -1, 1, -10, -20)
d1 = discriminant(0, -1, 1, -7820, -263580)
checks['curve_discriminants'] = [d0, d1] == [-11**5, -11]

result = {
    'scope': 'Exact scalar/support arithmetic only; the four mathematical interfaces are audited in L062.',
    'scalar': pair(s), 't': pair(t), 'q': pair(q), 'local': local,
    'complement': pair(1728-s),
    'residue_differences': {'5': pair(s-2), '11': pair(s-4)},
    'finite_exceptional_scalars': exceptional,
    'curve_discriminants': {'actual': [d0, d1], 'required': [-11**5, -11]},
    'replayed_original_checks': replayed_original_checks,
    'checks': checks, 'failures': [name for name, ok in checks.items() if not ok],
}
path = root / 'audit-certificate.json'
path.write_text(json.dumps(result, indent=2) + '\n')
print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {result['failures']}")
print(f"Valuation pairs: {local['5']['actual_valuation_pair']}, {local['11']['actual_valuation_pair']}; required: 3*N0 x 4*N0")
print(f"Scalar residues: {local['5']['actual_scalar_residue']}, {local['11']['actual_scalar_residue']}; required: 2, 4")
print(f"Discriminants: {d0}, {d1}; required: {-11**5}, {-11}")
print(f"Certificate: {path.relative_to(root.parent.parent)}")
if result['failures']:
    raise SystemExit(1)
