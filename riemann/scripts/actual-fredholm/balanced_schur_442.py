#!/usr/bin/env python3
"""One exact-rational block test on L779's already audited saved evidence.

No Xi evaluation, Fourier replay, parameter search or floating arithmetic.
The analytic entrywise transfer is proved in L780. Inherited bounds retain
L779's analytic and arithmetic contracts; hashes identify, not verify, them.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


BASE = Path(__file__).resolve().parent
SOURCE = BASE / "independent-phase-certificate-437.json"
AUDIT = BASE / "audit-439/audit-report.json"


def interval(raw):
    lo, hi = map(Q, raw)
    if lo > hi:
        raise ValueError("Reversed input interval")
    return lo, hi


def scalar_mul(q, box):
    values = [q * x for x in box]
    return min(values), max(values)


def decimal_out(q, places, upper=False):
    scale = 10**places
    n = q.numerator * scale
    z = -((-n) // q.denominator) if upper else n // q.denominator
    sign = "-" if z < 0 else ""
    z = abs(z)
    return f"{sign}{z // scale}.{z % scale:0{places}d}"


def exact(q):
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=BASE / "balanced-schur-certificate-442.json")
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit(f"Refusing to overwrite {args.output}")
    raw = SOURCE.read_bytes()
    data = json.loads(raw)
    audit = json.loads(AUDIT.read_text())
    signed = data["signed"]
    checks, failures = [], []

    def require(condition, label):
        (checks if condition else failures).append(label)
        if not condition:
            raise ValueError(label)

    report = {
        "step": 442,
        "status": "INCOMPLETE",
        "source": str(SOURCE.relative_to(BASE.parent.parent)),
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "audit_sha256": hashlib.sha256(AUDIT.read_bytes()).hexdigest(),
        "pair": data["pair"],
        "checks": checks,
        "failures": failures,
        "scope": "Actual scalar block transfer using L779; not a full replay or an independent source audit.",
        "arithmetic": "New operations use exact Python integer/Fraction arithmetic; inherited data retain L779 contracts.",
    }
    try:
        require(audit["status"] == "PASS" and audit["failures"] == [],
                "Inherited audit reports PASS with no failures")
        require(report["source_sha256"] == audit["input_sha256"],
                "Input file matches the hash of the source audited in step439")
        require(data["pair"] == [3, 2048], "Only the approved fixed pair is used")
        a = interval(signed["a"])[1]
        require(a == Q(7, 8), "Common node modulus bound is 7/8")
        alpha = list(map(Q, signed["alpha_hat"]))
        ea = list(map(Q, signed["alpha_error"]))
        d = list(map(Q, signed["residue_hat"]))
        ed = list(map(Q, signed["residue_error"]))
        require(all(0 <= x for x in ea + ed), "Node and complete residue errors are nonnegative")
        require(all(abs(x) + e <= a for x, e in zip(alpha, ea)),
                "Both exact node error intervals stay within modulus 7/8")
        require(d[0] - ed[0] > 0 and d[1] + ed[1] < 0,
                "Complete residues have signs positive, negative")
        for j in range(2):
            for field, hat, err in (("alpha", alpha[j], ea[j]),
                                    ("residue", d[j], ed[j])):
                lo, hi = interval(data["zeros"][j][field])
                require(hat - err <= lo <= hi <= hat + err,
                        f"Saved complete zero {j + 1} {field} enclosure is covered")
        db = interval(signed["delta_b"])[1]
        hb = interval(signed["h_b"])[1]
        require(0 <= db < Q("1.164e-12") and 0 <= hb < Q("10314"),
                "Complete Hankel error and approximant norm meet the stated upper bounds")
        require(1 / (1 - a*a) < 9 and 1 / (1 - a)**2 == 64,
                "Vector norm <3 and node Lipschitz constant <=64")
        sbox = interval(signed["finite"]["signed_pairing_Ystar_U"][1][1])
        sabs = max(map(abs, sbox))
        require(sabs < 11120, "Complete saved S_hat22 interval has modulus <11120")
        es = 9*db + 384*hb*ea[1]
        eb = ed[1]*sabs + (abs(d[1]) + ed[1])*es
        require(es < Q("1.06e-11"), "Full actual pairing-entry error is <1.06e-11")
        require(eb < Q("3.13e-13"), "Full residue-times-pairing error is <3.13e-13")
        prod = scalar_mul(d[1], sbox)
        dhat_box = (1-prod[1], 1-prod[0])
        actual = (dhat_box[0]-eb, dhat_box[1]+eb)
        require(Q("-0.0007617242877") < actual[0] <= actual[1]
                < Q("-0.0007617242869"), "Actual D lies strictly in the reported negative interval")
        require(actual[1] < 0, "The required positive eliminated-block margin fails")
        inverse_upper = -1 / actual[1]
        require(inverse_upper < 1313, "Both identical scalar eliminated blocks are invertible with inverse norm <1313")
        selected = {key: signed[key] for key in (
            "a", "alpha_hat", "alpha_error", "residue_hat", "residue_error", "delta_b", "h_b")}
        selected["S_hat22"] = signed["finite"]["signed_pairing_Ystar_U"][1][1]
        selected["complete_zero_intervals"] = [
            {key: zero[key] for key in ("alpha", "residue")} for zero in data["zeros"]]
        report.update({
            "inputs": selected,
            "pairing_error_upper": exact(es),
            "block_error_upper": exact(eb),
            "approximant_D_interval": [exact(x) for x in dhat_box],
            "actual_D_interval": [exact(x) for x in actual],
            "actual_D_outward_decimal": [decimal_out(actual[0], 22), decimal_out(actual[1], 22, True)],
            "required_D_lower": "strictly greater than 0",
            "D0_equals_D": True,
            "both_inverse_norm_upper": exact(inverse_upper),
            "reference_defect_evaluated": False,
            "reason_no_defect_evaluation": "Both first required coercivity conditions already fail on the actual pair.",
            "status": "PASS_NEGATIVE_BLOCK",
        })
    except Exception as exc:
        report["status"] = "FAIL"
        if str(exc) not in failures:
            failures.append(str(exc))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(report, stream, indent=2)
        stream.write("\n")
    print(f"status={report['status']}; failures={failures}")
    if "actual_D_outward_decimal" in report:
        print(f"actual D=D0 in {report['actual_D_outward_decimal']}; required D>0 and D0>0")
        print("pairing error <1.06e-11; block error <3.13e-13; both inverse norms <1313")
    print(f"certificate={args.output}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
