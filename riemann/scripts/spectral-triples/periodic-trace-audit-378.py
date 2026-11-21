"""Exact scalar checks for L762's step378 audit; no spectral replay."""

from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "scripts/spectral-triples/periodic-trace-audit-378.json"
LEMMA = ROOT / "lemmas/L762-effective-ccm-periodic-boundary-trace.md"
checks = []


def check(name, actual, relation, required):
    actual, required = Q(actual), Q(required)
    passed = {"=": actual == required, "<": actual < required,
              ">": actual > required}[relation]
    checks.append({"name": name, "actual": str(actual),
                   "relation": relation, "required": str(required),
                   "passed": passed})


energy = Q(4, 3) * 726
g1 = 800 * (Q(1, 2) + 82)
g2 = 800 * (Q(1, 4) + 2 * 82 + 82**2)
v = 24 * g1 + 36 * g2
a = Q(11 * 800 * 39, 6)
coefficient = a + Q(100000000, 3)
check("local_derivative_energy_upper", energy, "=", 968)
check("segment_energy_upper", energy / 2, "=", 22**2)
check("finite_Fourier_eigenvalue_lower", Q(7, 460), ">", Q(1, 100))
check("G1", g1, "=", 66000)
check("G2", g2, "=", 5510600)
check("V_expression", v, "=", 199965600)
check("V_upper", v, "<", 200000000)
check("A_upper", a, "=", 57200)
check("all_N_coefficient_upper", coefficient, "<", 34000000)
check("all_N_slack", 34000000 - coefficient, "=", Q(1828400, 3))
failures = [item["name"] for item in checks if not item["passed"]]
certificate = {
    "step_id": "2026-11-04-ccm-periodic-trace-conceptual-audit-378",
    "outcome": "PASS" if not failures else "FAIL",
    "scope": "Exact rational arithmetic only; not a Fourier or spectral proof.",
    "analytic_proof": str(LEMMA.relative_to(ROOT)) + ", section5",
    "inherited_inputs": "L760 row convention; L761 certified scalar data and trust assumptions",
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "lemma_sha256": hashlib.sha256(LEMMA.read_bytes()).hexdigest(),
    "checks": checks,
    "failures": failures,
}
OUTPUT.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
print(f"{certificate['outcome']}: {len(checks)} exact scalar checks; failures={failures}")
print(f"V: actual={v}, required<200000000")
print(f"all-N coefficient: actual={coefficient}, required<34000000")
print(f"all-N slack: {34000000-coefficient}")
print(f"certificate: {OUTPUT.relative_to(ROOT)}")
if failures:
    raise SystemExit(1)
