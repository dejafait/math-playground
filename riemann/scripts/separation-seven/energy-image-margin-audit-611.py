#!/usr/bin/env python3
"""Independent exact scalar audit of C999s; import, do not replay, audit561."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
checks, failures = [], []


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(name, actual, relation, required):
    passed = {"<": lambda: actual < required,
              ">": lambda: actual > required,
              "==": lambda: actual == required}[relation]()
    checks.append(dict(name=name, actual=str(actual), relation=relation,
                       required=str(required), passed=passed))
    if not passed:
        failures.append(name)


old = json.loads((BASE / "energy-image-margin-610.json").read_text())
prior = json.loads((BASE / "neutral-head-covariance-audit-561.json").read_text())
check("610 source hash", sha(BASE / "energy-image-margin-610.py"), "==",
      old["source_script_sha256"])
for name, expected in old["input_hashes"].items():
    check("610 input hash: " + name, sha(ROOT / name), "==", expected)
check("559 certificate remains pinned by audit561",
      sha(BASE / "neutral-head-covariance-559.json"), "==",
      prior["original_hashes"]["neutral-head-covariance-559.json"])

# Inspect the complete relevant imported scalar values, not a JSON preview.
evidence = prior["evidence"]
conversion = F(evidence["basis_conversion"]["hi"])
factor_error = F(evidence["factor_reconstructions"]["head_LZ_norm"]["upper"]["hi"])
eta = F(24, 100000) * F(1008, 1000)**2 + F(1, 10**7)
check("imported exact-neutral conversion", conversion, "<", F(1, 10**14))
check("imported complete factor allowance", factor_error, "<", F(1, 10**6))
check("enlarged exact Mhat Zhat norm squared", F(6190001, 10**6)**2,
      ">", F(619, 100)**2 + F(1, 10**6))
for end in ("lo", "hi"):
    check("imported eta_A endpoint " + end,
          F(evidence["integer_scalar_bounds"]["head_form_error"][end]), "==", eta)

# Independently simplify gamma_1024 and the two-product expression.
gamma = F(1, 2**43 - 1)
e1 = F(9200) * gamma
e2 = F(211623) * gamma
assembly = gamma * F(1104529, 5)
metric = F(1009, 1000) * F(6190001, 10**6) + F(1, 10**7) + eta
computed = dict(gamma_1024=gamma, first_product_error_upper=e1,
                second_product_error_upper=e2,
                Ahat_vs_exact_dyadic_assembly_upper=assembly,
                eta_A=eta, full_metric_upper=metric,
                coarse_normalized_lower=F(999, 7000000))
check("all stored rational value keys", sorted(old["rational_values"]), "==",
      sorted(computed))
for name, value in computed.items():
    check("independent rational identity: " + name,
          value, "==", F(old["rational_values"][name]))

expected = [
    (F(1008, 1000) + F(1, 10**14), "<", F(1009, 1000)),
    (gamma, "<", F(12, 10**14)),
    (F(9200) + e1, "<", F(9201)),
    (assembly, "<", F(1, 10**7)),
    (eta, "==", F(24395536, 10**11)),
    (metric, "<", F(7)),
    (F(7) * F(14, 100000), "<", F(999, 10**6)),
    (F(14, 100000), ">", F(0)),
]
check("complete original check count", len(old["checks"]), "==", len(expected))
for i, (actual, relation, required) in enumerate(expected):
    saved = old["checks"][i]
    check("original check identity " + str(i),
          (str(F(saved["actual"])), saved["relation"], str(F(saved["required"]))),
          "==", (str(actual), relation, str(required)))
    check("independent bound " + saved["name"], actual, relation, required)
check("original certificate failures", old["failures"], "==", [])
check("exact two-product expression", e1 * F(1009, 1000) + e2, "==", assembly)
check("full metric decimal identity", metric, "==", F("6.24595506436"))
check("normalized slack", F(999, 10**6) - 7 * F(14, 100000), ">", F(0))

inputs = ["energy-image-margin-610.py", "energy-image-margin-610.json",
          "neutral-head-covariance-audit-561.json", "neutral-head-covariance-559.json"]
out = dict(scope="Scalar bridge and provenance only; conceptual proof in C999s Section5",
           source_script_sha256=sha(Path(__file__)),
           input_hashes={name: sha(BASE / name) for name in inputs},
           exact_values={name: str(value) for name, value in computed.items()},
           imported_selected_values=dict(basis_conversion_upper=str(conversion),
                                         head_factor_error_upper=str(factor_error)),
           checks=checks, failures=failures,
           summary=dict(passed=not failures, metric_actual=str(metric),
                        metric_required="7", assembly_actual=str(assembly),
                        assembly_required="1/10000000", margin_actual="7/50000",
                        margin_required="0", coefficient_slack="19/1000000"),
           qualifications=["Import C999l/audit561; no large covariance or factor replay.",
                           "Inherited analytic/arithmetic/core/c_star contracts remain.",
                           "No complement, mixed-block, global sign or novelty claim."])
path = BASE / "energy-image-margin-audit-611.json"
path.write_text(json.dumps(out, indent=2) + "\n")
print("Checks:", len(checks), "failures:", failures)
print("Assembly:", assembly, "required < 1/10000000")
print("Metric:", metric, "required < 7")
print("Margin: 7/50000 required > 0; coefficient slack: 19/1000000")
print("Certificate:", path.relative_to(ROOT))
if failures:
    raise SystemExit(1)
