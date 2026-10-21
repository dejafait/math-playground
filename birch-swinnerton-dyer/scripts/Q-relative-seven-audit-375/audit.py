"""One unchanged-instance replay and independent projective integer check."""
from pathlib import Path
import hashlib
import importlib.util
import json
from math import gcd
import shutil
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "Q-relative-seven-373"
UPSTREAM = HERE.parent / "known-point-seven-307/certificate.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strip_integer(value):
    assert type(value) is int and value != 0
    original = value
    divisions = []
    exponent = 0
    while True:
        quotient, remainder = divmod(value, 7)
        divisions.append({"dividend": value, "quotient": quotient, "remainder": remainder})
        assert value == 7 * quotient + remainder and 0 <= remainder < 7
        if remainder:
            break
        exponent += 1
        value = quotient
    assert original == 7**exponent * value and value % 7 != 0
    return {"original": original, "exponent": exponent, "unit": value,
            "unit_residue": value % 7, "divisions": divisions}


def projective_check(point, local, label):
    # Compute from full primitive coordinates; do not use saved t or valuations.
    X, Y, Z = local["primitive"]
    assert all(type(a) is int for a in (X, Y, Z))
    assert Z > 0 and gcd(gcd(abs(X), abs(Y)), Z) == 1
    assert Y*Y*Z + Y*Z*Z == X**3 + X*X*Z - 2*X*Z*Z
    assert X % 7 == Z % 7 == 0 and Y % 7 != 0
    assert not local["identity"]
    divisions = {k: strip_integer(v) for k, v in zip(("X", "Y", "Z"), (X, Y, Z))}
    eX, eY, eZ = [divisions[k]["exponent"] for k in ("X", "Y", "Z")]
    actual = [eX-eZ, eY-eZ, eX-eY]
    # Cross multiplication binds both affine coordinates to the primitive triple.
    for pair, numerator in zip(point, (X, Y)):
        n, d = pair
        assert d > 0 and gcd(abs(n), d) == 1 and n*Z == d*numerator
    # Reduce -X/Y independently, keeping the positive-denominator convention.
    common = gcd(abs(X), abs(Y))
    sign = 1 if Y > 0 else -1
    numerator, denominator = -sign*X//common, sign*Y//common
    assert denominator > 0 and gcd(abs(numerator), denominator) == 1
    nt, dt = strip_integer(numerator), strip_integer(denominator)
    assert nt["exponent"]-dt["exponent"] == actual[2]
    expected_values = {
        "fraction": [numerator, denominator],
        "numerator_v7": nt["exponent"], "denominator_v7": dt["exponent"],
        "v7": actual[2], "numerator_unit": nt["unit"],
        "denominator_unit": dt["unit"],
        "unit_residues": [nt["unit_residue"], dt["unit_residue"]]}
    assert expected_values == local["values"]["t"]
    assert actual == [local["values"][k]["v7"] for k in ("x", "y", "t")]
    assert local["in_E2"] == (actual[2] >= 2)
    assert local["reduction"] == [X % 7, Y % 7, Z % 7]
    return {"label": label, "projective_divisions": divisions,
            "actual_valuations": actual, "reduced_parameter": expected_values,
            "parameter_divisions": {"numerator": nt, "denominator": dt},
            "passed": True}


def main():
    files = sorted(p for p in SOURCE.iterdir() if p.is_file()) + [UPSTREAM]
    before = {str(p.relative_to(HERE.parent.parent)): digest(p) for p in files}
    report = {"status": "IN_PROGRESS", "failures": [], "original_hashes": before}
    (HERE / "audit.json").write_text(json.dumps(report, indent=2) + "\n")
    try:
        shutil.copyfile(SOURCE / "certificate.json", HERE / "certificate.json")
        shutil.copyfile(SOURCE / "verify_certificate.py", HERE / "verify_certificate.py")
        spec = importlib.util.spec_from_file_location("fixed_replay_375", HERE / "verify_certificate.py")
        module = importlib.util.module_from_spec(spec)
        sys.dont_write_bytecode = True
        spec.loader.exec_module(module)
        module.main()
        original_report = json.loads((SOURCE / "verification.json").read_text())
        fresh_report = json.loads((HERE / "verification.json").read_text())
        # This checks every original sequential intermediate and every report field.
        assert fresh_report == original_report
        certificate = json.loads((HERE / "certificate.json").read_text())
        checks = [projective_check(certificate["W_Q"], certificate["W_Q_local"], "13Q")]
        for item in certificate["candidates"]:
            checks.append(projective_check(item["point"], item["local"], item["c"]))
        actual = [item["actual_valuations"][2] for item in checks[1:]]
        assert actual == [1, 1, 1, 1, 2, 1, 1]
        branches = {}
        for row in certificate["rows"]:
            branches[row["branch"]] = branches.get(row["branch"], 0) + 1
        report.update({"complete_fresh_report_equals_original": True,
                       "projective_checks": checks, "candidate_t_valuations": actual,
                       "branch_counts": branches, "row_count": len(certificate["rows"]),
                       "sequential_count": sum(len(v) for v in fresh_report["sequential_checks"].values()),
                       "required": "seven labels; exactly c=4 has valuation 2, six have valuation 1"})
        assert all(digest(p) == before[str(p.relative_to(HERE.parent.parent))] for p in files)
        report.update({"status": "PASS", "originals_preserved": len(files)})
    except Exception as error:
        report["status"] = "FAIL"
        report["failures"].append(repr(error))
        raise
    finally:
        (HERE / "audit.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"PASS: all {report['row_count']} rows and {report['sequential_count']} sequential additions; "
          f"8 projective checks; actual={actual}; required=[1,1,1,1,2,1,1]; "
          f"failures=0; preserved={report['originals_preserved']}; {HERE / 'audit.json'}")


if __name__ == "__main__":
    main()
