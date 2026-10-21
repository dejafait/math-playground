"""Exact finite hypotheses for the two Hensel lifts in L096."""
import json
from pathlib import Path

COEFF = [55, 165, 594, 1100, 2145, 2475, 2970, 1782, 1215]


def h(m, n):
    return sum(c * m**i * n**(8-i) for i, c in enumerate(COEFF))


def valuation(x):
    if x == 0:
        return None
    v = 0
    while x % 11 == 0:
        x //= 11
        v += 1
    return v


records = []
failures = []
for name, d, c, scale, a0 in [
    ('I', 1, 6, 1, 3),
    ('II', 5, 1 + 5**10, 5**11, 1),
]:
    m = u = 1
    n = d*c
    q = 3*m*m + m*n + n*n
    hv = h(m, n)
    error = scale*a0**3-hv
    derivative = 3*scale*a0**2
    checks = {
        'linear_equation': c == (5*m+u**5 if d == 1 else m+5**10*u**5),
        'complement_identity': n**11-q**5*(n-5*m) == m**3*hv,
        'linear_numerator': n-5*m == d**11*u**5,
        'H_residue': hv % 11 == 5,
        'error_divisible_by_11': error % 11 == 0,
        'derivative_unit': derivative % 11 != 0,
        'strict_hensel_bound': valuation(error) is not None and valuation(error) > 2*valuation(derivative),
        'all_coordinate_residues_nonzero': all(x % 11 != 0 for x in [m,u,a0,m*a0,q*u,c]),
    }
    failures.extend(f'{name}:{key}' for key, ok in checks.items() if not ok)
    records.append(dict(system=name, m=m, u=u, C=c, n=n, Q=q, H=hv,
                        scale=scale, a0=a0, error=error, derivative=derivative,
                        error_valuation=valuation(error), derivative_valuation=valuation(derivative),
                        residues={k: v % 11 for k,v in dict(a=a0,A=m*a0,B=q*u,C=c).items()},
                        checks=checks))
output = Path(__file__).with_name('eleven-lifts-certificate.json')
output.write_text(json.dumps(dict(records=records, checks=16, failures=failures), indent=2)+'\n')
for record in records:
    print(f"{record['system']}: v11(error)={record['error_valuation']}, "
          f"required > {2*record['derivative_valuation']}; residues={record['residues']}")
print(f'Checks: 16; failures: {failures}; certificate: {output}')
assert not failures
