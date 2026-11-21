#!/usr/bin/env python3
"""Check the complete L690 replay and its inherited evidence linkage.

First run common-displacement-full-circle-94.py with --output pointing
to common-displacement-full-circle-audit-96.json. This script checks every
saved row, not previews. It does not implement a new interval backend.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

base = Path(__file__).resolve().parent
names = {
    "original": "common-displacement-full-circle-certificate-94.json",
    "replay": "common-displacement-full-circle-audit-96.json",
    "inherited": "full-circle-root-compensation-certificate.json",
    "prior_audit": "full-circle-root-compensation-audit.json",
}
raw = {key: (base / name).read_bytes() for key, name in names.items()}
data = {key: json.loads(value) for key, value in raw.items()}
out = {"status": "INCOMPLETE", "checks": {}, "failures": [],
       "scope": "Complete stored evidence linkage and exact rational aggregation; inherited interval backend, no independent derivative recomputation.",
       "inputs": {key: {"path": names[key], "sha256": hashlib.sha256(value).hexdigest()}
                  for key, value in raw.items()}, "bounds": {}}


def check(label, condition):
    out["checks"][label] = bool(condition)
    if not condition:
        out["failures"].append(label)


original, replay = data["original"], data["replay"]
inherited, prior = data["inherited"], data["prior_audit"]
scale = int(replay["scale"])
check("original_and_replay_identical", original == replay)
check("all_statuses_and_failure_lists", all(v["status"] == "PASS" and not v["failures"]
                                          for v in data.values()))
check("all_replay_checks", all(replay["checks"].values()))
check("all_prior_audit_checks", all(prior["checks"].values()))
check("inherited_hash", replay["original_sha256"] == hashlib.sha256(raw["inherited"]).hexdigest())
check("backend_hash", replay["interval_producer_sha256"] == hashlib.sha256(
    (base / "full-circle-root-compensation.py").read_bytes()).hexdigest())
check("scales_agree", all(int(v["scale"]) == scale for v in data.values()))


def key(row):
    return row["region"], row["sign"], tuple(row["e_cell"]), tuple(row["theta_cell"])


old_rows = {key(row): row for row in inherited["derivative_leaves"]}
audit_rows = {key(row): row for row in prior["derivative_replay"]}
check("all_derivative_records_linked", len(old_rows) == len(audit_rows) == 8192
      and len(inherited["derivative_leaves"]) == len(prior["derivative_replay"]) == 8192
      and old_rows.keys() == audit_rows.keys())
derivative_ok = True
for row_key, row in old_rows.items():
    audited = audit_rows[row_key]
    lo, hi = (F(int(v), scale) for v in row["integral_interval"])
    derivative_ok &= all(audited[k] == v for k, v in row.items())
    derivative_ok &= audited["replayed_interval"] == row["integral_interval"]
    derivative_ok &= audited["matches"] and audited["threshold_pass"] and lo <= hi
    derivative_ok &= hi <= F(-3, 10) if row["region"] == "top" else lo >= F(-9, 4)
check("every_prior_derivative_replay_value_and_threshold", derivative_ok)

rows = replay["angular_rows"]
check("all_angular_records_linked", rows == inherited["angular_rows"] == prior["angular_replay"])
check("full_angular_cover", [r["angle"] for r in rows] == [[k, 512] for k in range(513)])
check("every_four_edge_maximum", all(len(r["rate_uppers"]) == 4 and
      int(r["maximum_upper"]) == max(map(int, r["rate_uppers"])) for r in rows))
comparison = replay["uniform_comparison"]
node = F(max(int(r["maximum_upper"]) for r in rows), scale)
error = F(int(comparison["pointwise_angular_error_upper"]), scale)
pi_upper = F(int(replay["global_bounds"]["pi_interval"][1]), scale)
required_error = 100 * pi_upper**2 / (8 * 512**2)
check("outward_pointwise_chord_error", error >= required_error)
check("uniform_aggregation_and_strict_margin", node + error == F(comparison["actual_upper"])
      and node + error < F(-1, 500)
      and F(-1, 500) - node - error == F(comparison["positive_margin"]))
out["bounds"]["uniform_contour"] = {"actual": str(node + error), "required": "< -1/500",
                                     "pointwise_error": str(error), "required_error": str(required_error)}
sigma2 = F(121, 64) - F(273, 200)**2
check("original_D_clearance", sigma2 == F(137, 5000))
check("original_D_rate", F(1, 16) - 2 * F(91, 5000) == F(261, 10000))
out["bounds"]["original_D_rate_margin"] = {"actual": "261/10000", "required": "> 0"}
out["bounds"]["onset_error"] = {"actual": str(F(30000**2, 2**38)), "required": "< 1/64"}
check("uniform_onset", F(30000**2, 2**38) < F(1, 64))
out["counts"] = {"angular_rows": len(rows), "inherited_derivative_rows": len(old_rows)}
out["status"] = "PASS" if not out["failures"] else "FAIL"
dest = base / "common-displacement-full-circle-audit-checks-96.json"
dest.write_text(json.dumps(out, indent=2) + "\n")
print("Audit checks:", out["status"], "; angular rows:", len(rows), "; linked derivative rows:", len(old_rows))
for label, bound in out["bounds"].items():
    print(label + ":", bound["actual"], "; required", bound["required"])
print("Failures:", out["failures"])
print("Complete evidence:", dest.relative_to(base.parent.parent))
if out["failures"]:
    raise SystemExit(1)
