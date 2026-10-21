#!/usr/bin/env python3
"""Exact finite checks for L041; no numerical asymptotic assertion."""
from fractions import Fraction as F
from pathlib import Path
import json

records = []
for n in (2, 3, 8, 24):
    for q in (F(3, 2), F(2), F(5, 4)):
        sigma = q + 1/q - 2
        rn = [(q**(r+1) + q**(-r))/((q-1)*(q**n-q**(-n))) for r in range(n)]
        rd = [(q**j-q**(-j))/(q**n-q**(-n)) for j in range(1, n)]
        for kind, col in (("Neumann", rn), ("Dirichlet", rd)):
            residuals = []
            for r, value in enumerate(col):
                diag = 1 if kind == "Neumann" and r in (0, len(col)-1) else 2
                got = (diag+sigma)*value
                if r:
                    got -= col[r-1]
                if r+1 < len(col):
                    got -= col[r+1]
                residuals.append(got - int(r == len(col)-1))
            records.append({"check": "endpoint_inverse", "N": n, "q": str(q),
                            "boundary": kind, "residuals": list(map(str, residuals)),
                            "passed": all(x == 0 for x in residuals)})
# Exhaust all bilinear coefficients in the pinned summation-by-parts identity.
for n in (2, 3, 8, 24):
    defects = []
    for edge in range(n):
        for vertex in range(1, n):
            c = [F(j == edge) for j in range(n)]
            z = [F(j == vertex) for j in range(n+1)]
            lhs = sum(c[j]*(z[j]-z[j+1])/2 for j in range(n))
            rhs = sum((c[j]-c[j-1])*z[j]/2 for j in range(1, n))
            if lhs != rhs:
                defects.append({"edge": edge, "vertex": vertex, "defect": str(lhs-rhs)})
    records.append({"check": "pinned_summation_by_parts", "N": n,
                    "basis_pairs": n*(n-1), "failures": defects, "passed": not defects})
certificate = {"scope": "Exact endpoint normalizations and full pinned bilinear summation identities only; not an asymptotic certificate.",
               "records": records, "required_defect": "0", "actual_max_defect": "0" if all(r["passed"] for r in records) else "nonzero",
               "passed": all(r["passed"] for r in records)}
path = Path(__file__).with_name("companion-separated-identities-certificate.json")
path.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"{sum(r['passed'] for r in records)}/{len(records)} records pass; actual/required exact defect: {certificate['actual_max_defect']}/0")
print(f"Summation basis pairs: {sum(r.get('basis_pairs', 0) for r in records)}; failures: {sum(not r['passed'] for r in records)}")
print(path)
if not certificate["passed"]:
    raise SystemExit(1)
