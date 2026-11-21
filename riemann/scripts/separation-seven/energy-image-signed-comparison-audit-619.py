#!/usr/bin/env python3
"""Independent exact scalar reconstruction for the C999u conceptual audit.

No earlier program is executed and no earlier artifact is overwritten.
The canonical proof audits operator/domain logic; C999n's analytic ledger
and C999t's full order are qualified inputs, not revalidated here.
"""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
checks, failures, reconstructed = [], [], []


def sha(name):
    return hashlib.sha256((BASE / name).read_bytes()).hexdigest()


def read(name):
    return json.loads((BASE / name).read_text())


def check(name, actual, relation, required):
    passed = {"<": lambda: actual < required, ">": lambda: actual > required,
              "==": lambda: actual == required, "<=": lambda: actual <= required}[relation]()
    item = dict(name=name, actual=str(actual), relation=relation,
                required=str(required), passed=bool(passed))
    checks.append(item)
    if not passed:
        failures.append(name)
    return item


def original(name, actual, relation, required):
    item = check(name, actual, relation, required)
    reconstructed.append(item)


old_name = "energy-image-signed-comparison-617.json"
old = read(old_name)
cert = read("endpoint-complement-certificate-581.json")
loc = read("endpoint-complement-locator-581.json")
prior_audit = read("endpoint-quarter-audit-583.json")
archive = "endpoint-complement-locator-581.npz"
names = {old_name, "energy-image-signed-comparison-617.py",
         "endpoint-quarter-audit-583.json", "endpoint-quarter-audit-583.py",
         "endpoint-complement-certificate-581.json", "endpoint-complement-locator-581.json",
         "endpoint-complement-certificate-581.py", "endpoint-complement-locator-581.py", archive}
names.update(loc["input_hashes"])
names.update(prior_audit["details"]["input_hashes"])
before = {name: sha(name) for name in sorted(names)}
check("617 generator unchanged", before["energy-image-signed-comparison-617.py"],
      "==", old["script_sha256"])
check("583 generator unchanged", before["endpoint-quarter-audit-583.py"],
      "==", prior_audit["script_sha256"])
for name, digest in old["input_pins"].items():
    check("617 import pin: " + name, before[name], "==", digest)
for name, digest in prior_audit["details"]["input_hashes"].items():
    check("583 import pin: " + name, before[name], "==", digest)

original("certificate frozen archive pin", before[archive], "==", cert["archive"]["sha256"])
original("locator frozen archive pin", before[archive], "==", loc["archive"]["sha256"])
original("certificate generator pin", before["endpoint-complement-certificate-581.py"],
         "==", cert["script_sha256"])
original("locator generator pin", before["endpoint-complement-locator-581.py"],
         "==", loc["script_sha256"])
for name, digest in loc["input_hashes"].items():
    original("unchanged original input " + name, before[name], "==", digest)
original("imported certificate failures", cert["failures"], "==", [])
original("all imported certificate checks", all(c["passed"] for c in cert["checks"]), "==", True)
original("imported audit passed", prior_audit["audit_passed"], "==", True)
original("imported audit failures", prior_audit["failures"], "==", [])
original("all imported audit checks", all(c["passed"] for c in prior_audit["checks"]), "==", True)

with np.load(BASE / archive, allow_pickle=False) as data:
    ints, diagonal = data["free_numerators"], data["diagonal"]
    original("frozen free shape", ints.shape, "==", (1024,))
    original("diagonal shape", diagonal.shape, "==", (1024,))
    check("integer dtype", ints.dtype.kind in "iu", "==", True)
    check("all frozen entries nonzero", all(int(n) != 0 for n in ints), "==", True)
    check("complete finite real binary64 diagonal", diagonal.dtype == np.dtype("float64")
          and bool(np.isfinite(diagonal).all()), "==", True)
    y = [[Q(int(n), 1 << 40) for n in ints[j:j+512]] for j in (0, 512)]
    d = [Q(*float(v).as_integer_ratio()) for v in diagonal]

l1 = [sum(map(abs, row), Q(0)) for row in y]
squares = [[v*v for v in row] for row in y]
norm2 = sum((sum(row, Q(0)) for row in squares), Q(0))
eps = Q(1, 10000)
energy = sum((d[n+512]*(squares[0][n]+squares[1][n]) for n in range(512)), Q(0))
energy_hi = energy + eps*norm2
for label, value in zip(("f", "h"), l1):
    original("full frozen free L1 " + label, value, "<", Q(721, 500))
original("full frozen free L2 squared", norm2, "<", Q(1, 5))
original("complete high diagonal upper", max(d[512:])+eps, "<", Q(8))
original("both low diagonal absolute bounds", max(map(abs, d[:2]))+eps, "<", Q(401))
original("entire frozen tail diagonal energy upper", energy_hi, "<", Q(1001, 1000))
bounds = cert["bounds"]
original("imported weighted norm lower", Q(bounds["weighted_free_norm_squared"]["lo"]), ">", Q(1))
original("imported endpoint energy upper", Q(bounds["endpoint_energy"]["hi"]), "<", Q(".723746547"))
original("imported full inverse pairing lower", Q(bounds["inverse_pairing_lower_quotient"]["lo"]),
         ">", Q(".5917169000"))

a, delta = Q(721, 500*131072), Q(1, 2500)
original("physical pair norm squared <1/4", norm2+2*a*a, "<", Q(1, 4))
transfer2 = 2*21**2*a*a
original("full transferred pair error squared", transfer2, "<", delta*delta)
mnorm = Q(30)+10*Q(471, 100)**2
original("full M_ref norm upper", mnorm, "<", Q(252))
perturbation = Q(252)*delta*(1+delta)
bhi = Q(1001, 2000)+160*a*a
mlo = 1-802*a*a-Q(".723746547")+Q(".5917169000")
# Independently collect all diagonal-loss coefficients in the final expression.
upper = (Q(1001, 2000)-1+Q(".723746547")-Q(".5917169000")
         +962*a*a+perturbation)
original("strict negative signed comparison", upper, "<", Q(-133, 500))
check("exact original 27-check reconstruction", reconstructed, "==", old["checks"])
check("original check count", len(reconstructed), "==", 27)
check("original result true", old["certified_under_inherited_contracts"], "==", True)
check("original failures empty", old["failures"], "==", [])

values = dict(low_physical_norm_upper=a, low_preimage_norm_upper=4*a,
              transferred_pair_error_upper=delta, reference_form_upper=bhi,
              original_signed_debt_lower=mlo, full_output_debt_perturbation=perturbation,
              signed_comparison_upper=upper, tail_diagonal_energy_upper=energy_hi)
for name, value in values.items():
    check("complete exact value: " + name, value, "==", Q(old["exact_values"][name]))
check("grouped final bound", upper, "==", bhi-mlo+perturbation)
check("published exact fraction", upper, "==", Q(-71572923236209923, 268435456000000000))
check("strict sign threshold", upper, "<", Q(0))
check("R inverse cap", 1/Q(".239999"), "<", Q(5))
check("uniform band moment ratio cap", Q(2, 512**2), "==", Q(1, 131072))
check("transferred vector nonzero", norm2, ">", Q(0))
check("low-square total loss", 2*401*a*a, "==", 802*a*a)

# Inspect the complete relevant imported enclosures, including quotient direction.
for label, bound in bounds.items():
    check("581 interval order: " + label, Q(bound["lo"]), "<=", Q(bound["hi"]))
ib = prior_audit["details"]["independent_bounds"]
for label, bound in ib.items():
    check("583 interval order: " + label, Q(bound["lo"]), "<=", Q(bound["hi"]))
check("583 same endpoint upper threshold", Q(ib["endpoint"]["hi"]), "<", Q(".723746547"))
check("583 same inverse lower threshold", Q(ib["inverse_lower_quotient"]["lo"]), ">", Q(".5917169000"))
check("583 same weighted norm lower", Q(ib["weighted_free_norm_squared"]["lo"]), ">", Q(1))
for label, b, pairkey, invkey in [("581", bounds, "trial_pairing", "inverse_pairing_lower_quotient"),
                                ("583", ib, "pairing", "inverse_lower_quotient")]:
    check(label+" positive trial denominator", Q(b["reference_energy"]["lo"]), ">", Q(0))
    check(label+" positive pairing lower", Q(b[pairkey]["lo"]), ">", Q(0))
    check(label+" quotient lower outward direction", Q(b[invkey]["lo"]), "<=",
          Q(b[pairkey]["lo"])**2/Q(b["reference_energy"]["hi"]))
rmax = Q(prior_audit["details"]["analytic_ledger"]["rmax"]["hi"])
check("inherited analytic plus arithmetic diagonal cap", rmax+Q(".0000001"), "<", eps)
for name, digest in before.items():
    check("preserved input: " + name, sha(name), "==", digest)

out = BASE / "energy-image-signed-comparison-audit-619.json"
report = dict(audit_passed=not failures, checks=checks, failures=failures,
              original_checks_reconstructed=len(reconstructed), input_hashes=before,
              exact_values={k: str(v) for k, v in values.items()},
              complete_scalar_sums=dict(endpoint_l1=[str(v) for v in l1],
                                        pair_tail_norm2=str(norm2), tail_diagonal_center=str(energy),
                                        transfer_error_squared_upper=str(transfer2)),
              imported_relevant_bounds={"581": bounds, "583": ib},
              actual_upper=str(upper), required_upper_strictly_below="0",
              limitation="Conditional obstruction to B-B M_ref B only. No actual S3 sign. Analytic response, IEEE754/Decimal, neutral core and unreplayed c_* remain qualified inputs. No source/core or large-matrix replay.",
              script_sha256=sha(Path(__file__).name))
out.write_text(json.dumps(report, indent=2)+"\n")
print(f"C999u audit: {len(checks)} checks; original checks reconstructed={len(reconstructed)}; failures={failures}")
print(f"Signed comparison upper={upper} ({float(upper):.12f}); required<0; transfer error<{delta}; perturbation={perturbation}")
print("Full certificate="+str(out.relative_to(BASE.parent.parent)))
if failures:
    raise SystemExit(1)
