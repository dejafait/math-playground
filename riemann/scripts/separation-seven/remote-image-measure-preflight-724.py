#!/usr/bin/env python3
"""Exact preflight for one uncompressed exponential prescription; no scalar."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
OUT = BASE / 'remote-image-measure-preflight-724.json'
WITNESS = BASE / 'defect-window-fixed-pair-707-witness.json'
PIN = '99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a'
A, B = 2**43, 2**23
CAP = 10**8
checks = []


def check(name, predicate):
    checks.append({'name': name, 'passed': bool(predicate)})


def cutoff(denominator):
    rhs = Fraction(2*A*denominator + 3, 4)
    n = -(-rhs.numerator // rhs.denominator)
    return n, Fraction(2*A, 4*n-3), Fraction(2*A, 4*(n-1)-3)


n, bound, previous = cutoff(10**7)
n_full, bound_full, previous_full = cutoff(10**6)
actual_hash = sha256(WITNESS.read_bytes()).hexdigest()
check('unchanged witness SHA256', actual_hash == PIN)
check('translation tail bound improves uniform-TV kernel bound', 2*A < B*B)
check('selected cutoff is positive', n >= 1)
check('selected tail majorant meets reserved budget', bound <= Fraction(1, 10**7))
check('previous cutoff misses reserved majorant budget', previous > Fraction(1, 10**7))
check('closed cutoff integer', n == 43980465111040000001)
check('one-accumulation-per-exponential work exceeds cap', n > CAP)
check('whole-budget majorant meets 1e-6', bound_full <= Fraction(1, 10**6))
check('previous whole-budget cutoff misses majorant budget', previous_full > Fraction(1, 10**6))
check('whole-budget cutoff integer', n_full == 4398046511104000001)
check('whole-budget work still exceeds cap', n_full > CAP)

certificate = {
    'scope': 'C998u one uncompressed geometric-prefix prescription; no actual scalar/error lower bound',
    'witness': {'path': str(WITNESS.relative_to(BASE)), 'expected_sha256': PIN, 'actual_sha256': actual_hash},
    'bounds': {'A': A, 'B': B, 'tail_formula': '2*A/(4*N-3)', 'total_error_goal': '1/1000000',
               'reserved_tail_budget': '1/10000000', 'remaining_error_allowance': '9/10000000'},
    'cutoff': {'N': n, 'tail_majorant': str(bound), 'previous_tail_majorant': str(previous),
               'whole_budget_N': n_full, 'whole_budget_tail_majorant': str(bound_full),
               'whole_budget_previous_tail_majorant': str(previous_full)},
    'work': {'required_total_cap': CAP, 'selected_loop_accumulations_only': n,
             'whole_budget_loop_accumulations_only': n_full, 'selected_cap_ratio': str(Fraction(n, CAP)),
             'all_other_costs_assigned_favorable_zero': True, 'cap_met': False},
    'unpaid': ['density quadrature and every mixed term', '512-mode and 334-shift preparation',
               'full K14 evaluation and exact projection coefficient enclosures',
               'location uncertainties and coincident-node handling', 'local scalar or linear-kernel term',
               'sweeps and elementary evaluations', 'rounding and cancellation', 'precision', 'byte storage'],
    'checks': checks,
    'failed_checks': [c['name'] for c in checks if not c['passed']],
    'target_failures': ['selected sufficient outer loop exceeds 1e8 before any density preparation',
                        'complete error, precision and storage ledger not obtained'],
    'analytic_proof_verified_by_script': False,
    'scalar_sweep_or_gram_evaluated': False,
}
OUT.write_text(json.dumps(certificate, indent=2) + '\n')
print(f'Checks: {sum(c["passed"] for c in checks)}/{len(checks)}; failures: {certificate["failed_checks"]}')
print(f'Tail majorant: {bound} <= 1/10000000; total goal: 1/1000000 (other errors unpaid)')
print(f'Outer accumulations: {n}; total allowed: {CAP}; prescription STOP')
print(f'Whole-budget accumulations: {n_full}; no scalar or sweep evaluated')
print(f'Certificate: {OUT.relative_to(BASE.parent.parent)}')
if certificate['failed_checks']:
    raise SystemExit(1)
