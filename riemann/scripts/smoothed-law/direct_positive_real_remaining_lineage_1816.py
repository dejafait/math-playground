"""Bind1816's arithmetic replay to the reused1808/1814 certificates.

Only artifact lineage is checked here; arithmetic is not repeated.
"""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parent.parent
OUT = HERE/"direct_positive_real_remaining_lineage_1816.json"


def main():
    if OUT.exists():
        raise SystemExit("Preserve lineage evidence: refuses to overwrite1816")
    checks, hashes = {}, {}

    def load(path):
        raw = path.read_bytes()
        hashes[str(path.relative_to(NOTEBOOK))] = hashlib.sha256(raw).hexdigest()
        return json.loads(raw)

    def digest(path):
        return hashlib.sha256((NOTEBOOK/path).read_bytes()).hexdigest()

    run = load(HERE/"direct_positive_real_remaining_execution_1816.json")
    replay = load(HERE/"direct_positive_real_remaining_replay_1816.json")
    prefix = load(HERE/"direct_positive_real_execution_1808.json")
    old_verify = load(HERE/"direct_positive_real_execution_verify_1808.json")
    ihat_verify = load(HERE/"direct_positive_real_ihat_replay_1814fast.json")
    checks["complete1816_saved_prefix_replay"] = replay["status"] == "PASS_COMPLETE_SAVED_PREFIX_ONLY" and not replay["failures"]
    checks["complete1808_input_replay"] = old_verify["status"] == "PASS_COMPLETE_SAVED_PREFIX_ONLY" and not old_verify["failures"]
    checks["complete1814_Ihat_replay"] = ihat_verify["status"] == "PASS_COMPLETE_IHAT_ONLY" and not ihat_verify["failures"]
    old_hashes = {item["path"]:item["sha256"] for item in prefix["artifacts"]}
    for path, sha in run["inputs_sha256"].items():
        if "/direct_positive_real_execution_1808/" in path:
            checks["reused1808_original_artifact_hash:"+path] = old_hashes.get(path) == sha == digest(path)
    ihat_path = "scripts/smoothed-law/direct_positive_real_ihat_execution_1814c.json"
    checks["reused1814_index_bound_to_full_replay"] = (
        ihat_verify["inputs_sha256"].get(ihat_path) == run["inputs_sha256"][ihat_path] == digest(ihat_path))
    for path, sha in replay["inputs_sha256"].items():
        checks["1816_replay_input_hash:"+path] = digest(path) == sha
    checks["unchanged_formula_driver"] = digest("scripts/smoothed-law/direct_positive_real_execution_remaining_1808.py") == run["formula_driver_sha256"]
    report = {"status":"PASS_LINEAGE_ONLY" if all(checks.values()) else "FAIL_LINEAGE",
        "checks":checks,"check_count":len(checks),
        "failures":[k for k,v in checks.items() if not v],"inputs_sha256":hashes,
        "scope":"Only certificate/input lineage; no repeated arithmetic, analytic-source or scalar/cap verification"}
    OUT.write_text(json.dumps(report,indent=2)+"\n")
    print(f"Lineage: {report['status']}; checks{len(checks)}; failures{report['failures']}")
    print(f"Certificate: {OUT.relative_to(NOTEBOOK)}")
    if report["failures"]:
        raise ArithmeticError(report["failures"])


if __name__ == "__main__":
    main()
