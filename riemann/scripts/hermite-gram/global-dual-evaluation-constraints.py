#!/usr/bin/env python3
"""Exact allowed-square constraints; full pairing remains UNCERTIFIED."""
import json
from fractions import Fraction
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / 'global-dual-evaluation-constraints.json'


def main():
    diagnostic = json.loads((HERE / 'global-dual-screen.json').read_text())
    certificates = []
    failures = []
    for n, p in [(64, 163), (128, 271), (256, 447)]:
        q = 2*n-1
        # V_j=2^j H_j(p/4), with integer recurrence.
        v = [1, p]
        for j in range(1, q):
            v.append(p*v[-1]-8*j*v[-2])
        finite_formula_checks = []
        for j in range(q+1):
            value = sum((-1)**r * factorial(j) // (factorial(r)*factorial(j-2*r))
                        * 4**r * p**(j-2*r) for r in range(j//2+1))
            finite_formula_checks.append(value == v[j])
        blocks = []
        for j in range(2, q+1):
            a, b, c = v[j]**2, v[j]*v[j-2], v[j-2]**2
            determinant = a*c-b*b
            good = a >= 0 and c >= 0 and determinant == 0
            if not good:
                failures.append(f'N={n}, edge={j}: exact PSD failure')
            blocks.append({'j': j, 'determinant_numerator': determinant,
                           'nonnegative_diagonals': a >= 0 and c >= 0})
        if not all(finite_formula_checks):
            failures.append(f'N={n}: Hermite finite formula mismatch')
        row = diagnostic['selected_witnesses'][str(n)]
        if Fraction(row['t']) != Fraction(p,4):
            failures.append(f'N={n}: sample identity mismatch')
        certificates.append(dict(N=n, x=str(Fraction(p,4)), q=q,
            interpretation='H_j(x)=V_j/2^j; exact evaluation functional',
            V=[str(z) for z in v],
            diagonal_count=len(v), edge_block_count=len(blocks),
            finite_formula_checks=finite_formula_checks, blocks=blocks,
            complete_pairing_numerical_only=row['D'],
            rigorous_pairing_upper_bound=None,
            rigorous_negative_pairing=False))
    result = dict(status='CONSTRAINTS_VERIFIED_PAIRINGS_UNCERTIFIED' if not failures else 'FAIL',
        certificates=certificates, constraint_failures=failures,
        certified_negative_pairings=0,
        required='All square constraints and rigorous complete pairing upper bound <0.',
        unresolved=['Coefficient quadrature remainder', 'All omitted theta indices',
                    'Spatial integral tails', 'Full signed interval pairing',
                    'Any unbounded family'])
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    print('status:',result['status'])
    for c in certificates:
        print(f"N={c['N']}, x={c['x']}: {c['diagonal_count']} diagonals, "
              f"{c['edge_block_count']} blocks; all exact determinants zero; "
              'rigorous pairing upper bound MISSING')
    print('required:',result['required'])
    print('certified negative pairings: 0; constraint failures:',failures)
    print('full constraint certificate:',OUT)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
