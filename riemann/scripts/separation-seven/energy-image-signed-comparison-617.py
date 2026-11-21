#!/usr/bin/env python3
"""Fixed C999n witness transfer for the assessment615 comparison.

Only exact integer/rational arithmetic is used for new scalar checks.
Import C999n's audited entry ledger and one-sided scalar enclosures;
do not replay its source/core contracts or claim an actual S3 sign.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
checks, failures, pins = [], [], {}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(name, actual, relation, required):
    passed = {"<": lambda: actual < required, ">": lambda: actual > required,
              "==": lambda: actual == required}[relation]()
    checks.append(dict(name=name, actual=str(actual), relation=relation,
                       required=str(required), passed=bool(passed)))
    if not passed:
        failures.append(name)


def dyadic(value):
    return F.from_float(float(value))


archive = BASE / "endpoint-complement-locator-581.npz"
cert = json.loads((BASE / "endpoint-complement-certificate-581.json").read_text())
locator = json.loads((BASE / "endpoint-complement-locator-581.json").read_text())
audit = json.loads((BASE / "endpoint-quarter-audit-583.json").read_text())
for name in [archive.name, "endpoint-complement-certificate-581.json",
             "endpoint-complement-locator-581.json", "endpoint-quarter-audit-583.json"]:
    pins[name] = sha(BASE / name)
check("certificate frozen archive pin", pins[archive.name], "==", cert["archive"]["sha256"])
check("locator frozen archive pin", pins[archive.name], "==", locator["archive"]["sha256"])
check("certificate generator pin", sha(BASE / "endpoint-complement-certificate-581.py"),
      "==", cert["script_sha256"])
check("locator generator pin", sha(BASE / "endpoint-complement-locator-581.py"),
      "==", locator["script_sha256"])
for name, digest in locator["input_hashes"].items():
    check("unchanged original input " + name, sha(BASE / name), "==", digest)
check("imported certificate failures", cert["failures"], "==", [])
check("all imported certificate checks", all(c["passed"] for c in cert["checks"]), "==", True)
check("imported audit passed", audit["audit_passed"], "==", True)
check("imported audit failures", audit["failures"], "==", [])
check("all imported audit checks", all(c["passed"] for c in audit["checks"]), "==", True)

with np.load(archive) as stored:
    numerators = stored["free_numerators"]
    diagonal = stored["diagonal"]
    check("frozen free shape", numerators.shape, "==", (1024,))
    check("diagonal shape", diagonal.shape, "==", (1024,))
    free = [F(int(n), 2**40) for n in numerators]
    dcenter = [dyadic(x) for x in diagonal]

l1 = [sum((abs(x) for x in free[j:j+512]), F(0)) for j in (0,512)]
tail_norm2 = sum((x*x for x in free), F(0))
for endpoint, value in zip(("f", "h"), l1):
    check("full frozen free L1 " + endpoint, value, "<", F("1.442"))
check("full frozen free L2 squared", tail_norm2, "<", F(1,5))
# C999n Sections2/4 supply |h(k_n)-stored D_n|<.0001 on0:1023.
diag_error = F(".0001")
check("complete high diagonal upper", max(dcenter[512:])+diag_error, "<", F(8))
check("both low diagonal absolute bounds", max(abs(dcenter[0]),abs(dcenter[1]))+diag_error,
      "<", F(401))
tail_energy_center = sum((dcenter[512+j%512]*x*x for j,x in enumerate(free)),F(0))
tail_energy_upper = tail_energy_center + diag_error*tail_norm2
check("entire frozen tail diagonal energy upper", tail_energy_upper, "<", F("1.001"))
check("imported weighted norm lower", F(cert["bounds"]["weighted_free_norm_squared"]["lo"]),
      ">", F(1))
check("imported endpoint energy upper", F(cert["bounds"]["endpoint_energy"]["hi"]),
      "<", F(".723746547"))
check("imported full inverse pairing lower", F(cert["bounds"]["inverse_pairing_lower_quotient"]["lo"]),
      ">", F(".5917169000"))

# r_n<2/n^2<=1/131072. Each endpoint's low norm is <=a.
a = F("1.442") / 131072
xlow = 4*a  # exact neutral completion of (D_tail/2)y, D_tail<8
check("physical pair norm squared <1/4", tail_norm2+2*a*a, "<", F(1,4))
delta = F(".0004")
check("full transferred pair error squared", 2*(5*xlow+a)**2, "<", delta*delta)
# Full U<30, full T<4.71, full reference inverse<5.
check("full M_ref norm upper", F(30)+2*F("4.71")**2*5, "<", F(252))
b_upper = F("1.001")/2 + 10*xlow*xlow
m_lower = 1-802*a*a-F(".723746547")+F(".5917169000")
perturbation = 252*delta*(1+delta)  # pair norm <1/2
negative_upper = b_upper-m_lower+perturbation
check("strict negative signed comparison", negative_upper, "<", F("-.266"))

values = dict(low_physical_norm_upper=a,low_preimage_norm_upper=xlow,
              transferred_pair_error_upper=delta,reference_form_upper=b_upper,
              original_signed_debt_lower=m_lower,full_output_debt_perturbation=perturbation,
              signed_comparison_upper=negative_upper,tail_diagonal_energy_upper=tail_energy_upper)
report = dict(certified_under_inherited_contracts=not failures,independently_audited=False,
              task="fixed witness transfer for B-B M_ref B",checks=checks,failures=failures,
              input_pins=pins,exact_values={k:str(v) for k,v in values.items()},
              actual_upper=str(negative_upper),required_upper_strictly_below="0",
              limitation="Stops only the sufficient signed reference comparison; no actual S3 negative direction or RH conclusion. Inherits C999n/t analytic, IEEE754/Decimal, core and c_* contracts.",
              script_sha256=sha(Path(__file__)))
out = BASE / "energy-image-signed-comparison-617.json"
out.write_text(json.dumps(report,indent=2)+"\n")
print("Conditional signed comparison upper=",float(negative_upper),"; required<0; failures=",failures)
print("Full transfer error<",float(delta),"; full debt perturbation<=",float(perturbation))
print("Evidence="+str(out.relative_to(BASE.parent.parent)))
if failures:
    raise SystemExit(1)
