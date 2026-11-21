#!/usr/bin/env python3
"""Exact planning arithmetic for C998j; no quadrature batch is evaluated."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import numpy as np

B = Path(__file__).resolve().parent
checks = []


def ck(name, value):
    checks.append({'name': name, 'pass': bool(value)})


def enc(x):
    x = F(x)
    return {'numerator': str(x.numerator), 'denominator': str(x.denominator)}


def ceil(x):
    return -(-x.numerator // x.denominator)


report = {
    'result': 'UNFINISHED', 'checks': checks,
    'scope': 'One fixed direct-moment schedule: ideal error and mandatory scalar work only',
    'service_failures': [
        'The mandatory direct accumulation alone exceeds 20000000 scalar operations.',
        'Finite nodes, weights, primitive rounding, constants and coefficient errors remain unpaid.',
        'No actual square entry, complete residual, inverse debt or sign is evaluated.'
    ],
}
try:
    archive = B / 'frozen-reference-proposal-652.npz'
    original = archive.read_bytes()
    pin = '2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6'
    ck('complete frozen archive pin', sha256(original).hexdigest() == pin)
    with np.load(archive, allow_pickle=False) as z:
        free = z['free_middle_dyadics'].copy()
    ck('all free binary64 coordinates', free.shape == (254, 3)
       and free.dtype == np.dtype('float64') and np.isfinite(free).all())
    columns = [[F(*float(v).as_integer_ratio()) for v in free[:, j]] for j in range(3)]
    masses = [sum(map(abs, col), F()) for col in columns]
    for j, mass in enumerate(masses):
        ck(f'column{j} exact free mass < 7/3', mass < F(7, 3))
        ck(f'column{j} full completion mass bound < 8', 2 * mass < 8)
    report['input_sha256'] = {archive.name: pin}
    report['exact_free_columns'] = [[enc(x) for x in col] for col in columns]
    report['coefficient_mass'] = [
        {'column': j, 'free_l1': enc(m), 'exact_completion_l1_upper': enc(2 * m)}
        for j, m in enumerate(masses)
    ]

    A, eta = 2**18, F(1, 2**84)
    panels = []
    total_nodes, quad = 0, F()
    for j in range(1, 85):
        b = F(1, 2**j)
        n = 44 + ceil(144 * b)
        ck(f'panel{j} complex prefactor', b*b*(j+3)**2 <= 4)
        ck(f'panel{j} exponential degree balance', 2*n >= 88+288*b)
        bound = F(32, 45)*b*F(1, 2**65)
        panels.append({'j': j, 'left': enc(b), 'right': enc(2*b),
                       'n_in_theorem19_3': n, 'nodes': n+1,
                       'per_moment_exact_node_error_upper': enc(bound)})
        total_nodes += n+1
        quad += bound
    ck('retained panels cover [eta,1]',
       panels[0]['right'] == enc(1) and panels[-1]['left'] == enc(eta)
       and all(panels[j]['left'] == panels[j+1]['right'] for j in range(83)))
    strip = A * eta
    eps = strip + quad
    ck('sum of local error bounds', quad == F(32, 45)*(1-eta)*F(1, 2**65))
    ck('uniform ideal moment error < 2^-64', eps < F(1, 2**64))
    ck('off-diagonal propagation including both endpoints', 10*A+1028+4*eps < 2**22)
    ck('diagonal propagation including all residues', 5*A+521+4*eps < 2**22)
    normalized_error = 2**21 * eps
    pairs = []
    for i in range(3):
        for j in range(3):
            bound = 4*masses[i]*masses[j]*normalized_error
            ck(f'complete ideal square entry{i}{j} meets allowance', bound < F(1, 2**37))
            pairs.append({'i': i, 'j': j, 'ideal_absolute_error_upper': enc(bound)})
    ck('uniform contracted allowance below required threshold', F(1, 2**37) < F(1, 10**10))
    report['prescription'] = {
        'eta': enc(eta), 'rho': 2, 'fractional_bits_proposed_unpaid': 512,
        'panels': panels, 'total_nodes': total_nodes, 'positive_frequencies': 255,
        'direct_moments_per_frequency': 14,
        'sharing': 'common nodes, weights, seven weighted factors and base trigonometric recurrence',
        'finite_setup': 'Specified in C998j; stopped before execution and error/cost certification'
    }
    report['error'] = {
        'strip_per_moment': enc(strip), 'ideal_gauss_per_moment': enc(quad),
        'ideal_total_per_moment': enc(eps),
        'undotted_true_magnitude_upper': A, 'dotted_true_magnitude_upper': 1,
        'dimensionless_entry_error_factor_upper': 2**22,
        'normalized_basis_entry_error_factor_upper': 2**21,
        'complete_square_pairs': pairs,
        'uniform_ideal_square_error_upper': enc(F(1, 2**37)),
        'required_complete_square_error': enc(F(1, 10**10)),
        'finite_arithmetic': 'UNPAID; all claimed error bounds above use exact constants/nodes/weights/coefficients'
    }

    # Favorable count: exclude both dotted P,T moment sums for every n;
    # even exclude initialization/assignment of the first product.
    retained = 12*255
    products = retained*total_nodes
    additions = retained*(total_nodes-1)
    mandatory = products+additions
    ck('fixed node inventory', total_nodes == 4002)
    ck('mandatory count', mandatory == 24489180)
    ck('mandatory direct work exceeds service cap', mandatory > 20_000_000)
    report['work'] = {
        'retained_moment_sums': retained, 'products': products, 'additions': additions,
        'mandatory_scalar_operations': mandatory, 'allowed_total': 20_000_000,
        'excess': mandatory-20_000_000,
        'all14_accumulation_only': 14*255*(2*total_nodes-1),
        'omitted': ['both dotted P/T sums', 'all density and weight evaluations',
                    'nodes/weights and constants', 'interval and rounding overhead',
                    'initialization/comparisons/assignments', 'neutral completion',
                    'entry assembly and all three-column contractions'],
        'scope': 'Only this unaggregated direct-moment prescription; no universal lower bound'
    }
    ck('archive unchanged', archive.read_bytes() == original)
except Exception as exc:
    ck(f'exception {type(exc).__name__}: {exc}', False)

report['failures'] = [c['name'] for c in checks if not c['pass']]
report['script_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
report['result'] = ('PASS_PLANNING_CHECKS_PRESCRIBED_WORK_FAILS'
                    if not report['failures'] else 'FAIL')
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2) + '\n')
print(report['result'])
if not report['failures']:
    print('Ideal contracted error < 2^-37 < 7.3e-12; required complete error <= 1e-10; finite arithmetic unpaid.')
    print('Mandatory scalar work:', report['work']['mandatory_scalar_operations'],
          '; required total <=', report['work']['allowed_total'])
print('Failed planning checks:', report['failures'])
print('Service failures:', '; '.join(report['service_failures']))
print('Full certificate:', out.relative_to(B.parent.parent))
if report['failures']:
    raise SystemExit(1)
