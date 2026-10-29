#!/usr/bin/env python3
"""Stop at the first guarded 01->10 margin reversal, in lengths 1..24.

Run from the active notebook: python3 scripts/first-drop-swap-margin/test_swap_margin.py
The adjacent comparison is the EXPLORE target assessed on 2026-10-28.
All arithmetic is integral. Full checked edges and witness evidence go to disk.
"""

import json
from pathlib import Path


MAX_LENGTH = 24
OUTPUT = Path(__file__).with_name("certificate.json")


def first_drop(word):
    q = 0
    for k, bit in enumerate(word):
        if 3**q < 2**k:
            return False
        q += int(bit)
    return 3**q < 2 ** len(word)


def candidate_words(length):
    """Lexicographic DFS; prune only prefixes already below coefficient 1."""
    def extend(prefix, q):
        k = len(prefix)
        if k == length:
            if 3**q < 2**k:
                yield prefix
            return
        if 3**q < 2**k:
            return
        yield from extend(prefix + "0", q)
        yield from extend(prefix + "1", q + 1)

    yield from extend("", 0)


def word_evidence(word):
    length = len(word)
    modulus = 2**length
    q = word.count("1")
    # Sourced affine numerator, evaluated directly as a sum.
    numerator = sum(
        2**i * 3 ** word[i + 1:].count("1")
        for i, bit in enumerate(word) if bit == "1"
    )
    residue = (-numerator * pow(3**q, -1, modulus)) % modulus
    rho = 2 + (residue - 2) % modulus
    states = [rho]
    actual_word = ""
    for _ in word:
        n = states[-1]
        actual_word += str(n % 2)
        states.append((3*n + 1)//2 if n % 2 else n//2)
    guards = []
    q_k = 0
    for k in range(length + 1):
        lhs, rhs = 3**q_k, 2**k
        relation = "<" if k == length else ">="
        passed = lhs < rhs if k == length else lhs >= rhs
        guards.append({"k": k, "q_k": q_k, "three_power": lhs,
                       "two_power": rhs, "required_relation": relation,
                       "passed": passed})
        if k < length:
            q_k += int(word[k])
    d = modulus - 3**q
    margin = d*rho - numerator
    checks = {
        "all_first_drop_guards": all(g["passed"] for g in guards),
        "first_drop_predicate": first_drop(word),
        "least_representative_interval": 2 <= rho <= modulus + 1,
        "previous_class_member_below_two": rho-modulus < 2,
        "residue_matches": rho % modulus == residue,
        "affine_congruence": (3**q*rho + numerator) % modulus == 0,
        "direct_parity_matches": actual_word == word,
        "affine_endpoint_matches": modulus*states[-1] == 3**q*rho+numerator,
        "margin_matches_direct_descent": margin == modulus*(rho-states[-1]),
    }
    return {"word": word, "length": length, "q": q, "modulus": modulus,
            "D": d, "A": numerator, "residue": residue, "rho": rho,
            "M": margin, "prefix_guards": guards, "trajectory": states,
            "actual_parity": actual_word, "checks": checks}


def edge_evidence(word, swapped, index):
    left, right = word_evidence(word), word_evidence(swapped)
    r = index
    s = word[index + 2:].count("1")
    b = 2**r * 3**s
    m = left["modulus"]
    residue_jump = b*pow(3**left["q"], -1, m) % m
    carry = (left["rho"] - 2 + residue_jump)//m
    delta = right["M"]-left["M"]
    checks = {
        "both_endpoint_checks": all(left["checks"].values()) and all(right["checks"].values()),
        "directed_adjacent_swap": word[index:index+2] == "01" and swapped == word[:index]+"10"+word[index+2:],
        "same_length_and_ones": left["length"] == right["length"] and left["q"] == right["q"],
        "strict_coefficient_drop": left["D"] > 0,
        "numerator_difference": left["A"]-right["A"] == b,
        "nonzero_residue_jump": 0 < residue_jump < m,
        "binary_carry": carry in (0, 1),
        "representative_difference": right["rho"]-left["rho"] == residue_jump-carry*m,
        "exact_swap_margin_formula": delta == left["D"]*(residue_jump-carry*m)+b,
    }
    return {"swap_index_zero_based": index, "u": word[:index],
            "v": word[index+2:], "r": r, "s": s, "B": b,
            "R": residue_jump, "carry": carry,
            "original": left, "swapped": right,
            "margin_delta": delta, "required_upper_bound": 0,
            "conjectured_inequality_holds": delta <= 0, "checks": checks}


def main():
    report = {
        "target": "M(u10v) <= M(u01v) when both endpoints are first-coefficient-drop words",
        "requested_max_length": MAX_LENGTH,
        "ordering": "Increasing length, lexicographic words, increasing zero-based swap index",
        "representative_domain": "Least integer >=2, equivalently the class member in [2,2^j+1]",
        "lengths": [], "checked_edges": [], "failures": [], "counterexample": None,
    }
    for length in range(1, MAX_LENGTH + 1):
        counts = {"length": length, "first_drop_words_visited": 0,
                  "directed_01_pairs_seen": 0, "guarded_edges_checked": 0,
                  "rejected_swapped_guard": 0, "completed_length": False}
        report["lengths"].append(counts)
        for word in candidate_words(length):
            counts["first_drop_words_visited"] += 1
            if not first_drop(word):
                report["failures"].append({"generated_word_not_first_drop": word})
                break
            for index in range(length - 1):
                if word[index:index+2] != "01":
                    continue
                counts["directed_01_pairs_seen"] += 1
                swapped = word[:index]+"10"+word[index+2:]
                if not first_drop(swapped):
                    counts["rejected_swapped_guard"] += 1
                    continue
                edge = edge_evidence(word, swapped, index)
                counts["guarded_edges_checked"] += 1
                report["checked_edges"].append(edge)
                bad_checks = [name for name, passed in edge["checks"].items() if not passed]
                if bad_checks:
                    report["failures"].append({"word": word, "swap_index": index, "checks": bad_checks})
                    break
                if edge["margin_delta"] > 0:
                    report["counterexample"] = edge
                    break
            if report["failures"] or report["counterexample"] is not None:
                break
        if report["failures"] or report["counterexample"] is not None:
            break
        counts["completed_length"] = True

    witness = report["counterexample"]
    report["result"] = "VERIFICATION_FAILURE" if report["failures"] else (
        "COUNTEREXAMPLE" if witness is not None else "FINITE_PASS_ONLY")
    report["completed_lengths"] = [c["length"] for c in report["lengths"] if c["completed_length"]]
    report["last_visited_length"] = report["lengths"][-1]["length"]
    report["complete_through_requested_bound"] = len(report["completed_lengths"]) == MAX_LENGTH
    OUTPUT.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(f"Result: {report['result']}; requested length bound: {MAX_LENGTH}; last visited: {report['last_visited_length']}")
    print(f"Completed lengths: {report['completed_lengths']}; guarded edges checked: {len(report['checked_edges'])}")
    if witness is not None:
        print(f"Words: {witness['original']['word']} -> {witness['swapped']['word']}; swap index: {witness['swap_index_zero_based']}")
        print(f"Margins: {witness['original']['M']} -> {witness['swapped']['M']}; actual difference: {witness['margin_delta']}; required <= 0")
    print(f"Verification failures: {len(report['failures'])}; certificate: {OUTPUT.relative_to(Path.cwd())}")
    if report["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
