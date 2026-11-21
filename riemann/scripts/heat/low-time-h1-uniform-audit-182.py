"""Audit L914's existing finite certificate; original evidence is preserved.

Analytic/code review is recorded in L914. This replays the complete producer,
the independent rational algebra checker, and exact-rational pi/tail bounds.
It does not independently verify the Decimal library.
"""
import hashlib
import importlib.util
import json
import platform
from decimal import (DivisionByZero, InvalidOperation, Overflow, Underflow,
                     Subnormal, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN)
from fractions import Fraction as F
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUTPUT = HERE / "low-time-h1-uniform-audit-182.json"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exp_negative(x):
    """Exact rational enclosure: reciprocal of a bounded positive series."""
    x = F(x)
    assert x >= 0
    term = total = F(1)
    for j in range(1, 1001):
        term *= x / j
        total += term
    next_term = term * x / 1001
    ratio = x / 1002
    assert ratio < 1
    upper = total + next_term / (1-ratio)
    return F(1)/upper, F(1)/total


def contained(bounds, record):
    assert F(record["lower"]) <= bounds[0] <= bounds[1] <= F(record["upper"])


def arctan(q):
    x = F(1, q)
    total = sum(((-1)**j*x**(2*j+1)/(2*j+1) for j in range(96)), F(0))
    return total, total+x**193/193


def main():
    paths = [HERE / "low-time-h1-uniform-180.py",
             HERE / "low-time-h1-uniform-180.json",
             HERE / "low-time-h1-uniform-180-check.py",
             HERE / "low-time-h1-uniform-180-check.json",
             ROOT / "scripts/hankel/certify_hankel.py"]
    hashes = {str(p.relative_to(ROOT)): digest(p) for p in paths}
    data = json.loads(paths[1].read_text())

    # Independent rational evaluation of the complete analytic tail constants.
    beta = F(119, 40)
    coefficient = 128*sum((F(factorial(6), factorial(6-j))*50**(6-j)
                           / beta**(j+1) for j in range(7)), F(0))
    spatial = tuple(coefficient*v for v in exp_negative(50*beta))
    theta = tuple(57600000*v for v in exp_negative(25*beta-1))
    total = tuple(spatial[j]+theta[j] for j in range(2))
    for name, bounds in (("spatial", spatial), ("theta", theta), ("total", total)):
        contained(bounds, data["tails"][name])
    assert total[1] < F("7.836e-25")
    assert exp_negative(F(9))[1]*16 < F(1, 2)
    assert exp_negative(11*beta)[1]*16 < F(1, 2)
    assert sum((F(4)**j/factorial(j) for j in range(8)), F(0)) > 50
    a, b = arctan(5), arctan(239)
    contained((16*a[0]-4*b[1], 16*a[1]-4*b[0]), data["pi"])

    # Complete replay at the stated precision, leaving the original untouched.
    producer = load("l914_producer_182", paths[0])
    producer.OUTPUT = HERE / "low-time-h1-uniform-replay-182.json"
    producer.main()
    replay = json.loads(producer.OUTPUT.read_text())
    assert replay == data, "Full producer replay differs from original evidence"
    assert len(replay["panels"]) == 256
    assert replay["failed_panels"] == []
    assert replay["status"] == "certified"

    # The existing checker performs every Fraction-based algebra containment.
    checker = load("l914_checker_182", paths[2])
    checker.main()
    report = json.loads(paths[3].read_text())
    assert report["status"] == "passed" and report["failures"] == []
    assert report["panels_checked"] == len(report["panels"]) == 256
    for i, row in enumerate(report["panels"]):
        assert row == {"index": i, "closed_parameter_panel_exact": True,
                       "rational_algebra_contained": True,
                       "strict_thresholds_passed": True}

    # Confirm active contexts, mandatory traps, and absence of forbidden flags.
    contexts = []
    signals = (DivisionByZero, InvalidOperation, Overflow, Underflow, Subnormal)
    for ctx, rounding in zip((producer.base.DOWN, producer.base.UP, producer.base.NEAR),
                             (ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN)):
        assert ctx.prec == 100 and ctx.rounding == rounding
        assert all(ctx.traps[s] and not ctx.flags[s] for s in signals)
        contexts.append({"precision": ctx.prec, "rounding": ctx.rounding,
                         "mandatory_traps": {s.__name__: ctx.traps[s] for s in signals},
                         "forbidden_flags": {s.__name__: ctx.flags[s] for s in signals},
                         "other_set_flags": [s.__name__ for s, flag in ctx.flags.items() if flag]})
    assert all(digest(p) == hashes[str(p.relative_to(ROOT))] for p in paths)
    result = {
        "status": "passed", "failures": [], "panels_checked": 256,
        "python_version": platform.python_version(),
        "source_hashes": hashes,
        "full_replay_identical": True,
        "replay_path": str(producer.OUTPUT.relative_to(ROOT)),
        "rational_checker_report": str(paths[3].relative_to(ROOT)),
        "all_rational_report_entries_verified": True,
        "exact_rational_tail_and_pi_enclosure_checks": True,
        "rational_exp_method": "1000-term positive series plus geometric remainder, reciprocated",
        "contexts": contexts,
        "summary": replay["summary"],
        "required_bounds": {"M0": ">0.49712", "S2": ">3.714e-5",
                            "D": ">9.7e-16 and <7.026e-15", "tail": "<7.836e-25"},
        "qualification": "Analytic/code audit in L914; Decimal contracts assumed, library unverified",
    }
    OUTPUT.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS: full 256-panel replay identical; rational algebra, pi/tails and contexts pass; failures=0")
    print("Actual determinant bounds:", replay["summary"]["minimum_determinant_lower"],
          replay["summary"]["maximum_determinant_upper"])
    print("Required: 9.7e-16 < D < 7.026e-15; tail < 7.836e-25")
    print("Complete audit:", OUTPUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
