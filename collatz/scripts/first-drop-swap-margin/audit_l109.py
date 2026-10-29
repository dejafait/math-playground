#!/usr/bin/env python3
"""Replay only L109's existing evidence; do not extend its stopped search."""

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUT = HERE / "certificate.json"
OUTPUT = HERE / "audit-certificate.json"


def orbit(n, length):
    states = [n]
    for _ in range(length):
        x = states[-1]
        states.append((3*x+1)//2 if x % 2 else x//2)
    return states


def guards(word):
    result = []
    for k in range(len(word)+1):
        q = word[:k].count("1")
        lhs, rhs = 3**q, 2**k
        final = k == len(word)
        result.append(dict(k=k, q_k=q, three_power=lhs, two_power=rhs,
                           required_relation="<" if final else ">=",
                           passed=lhs < rhs if final else lhs >= rhs))
    return result


def endpoint(word, rho):
    j, q = len(word), word.count("1")
    m, a_power = 2**j, 3**q
    states = orbit(rho, j)
    parity = "".join(str(x % 2) for x in states[:-1])
    # Recover A from direct iteration, independently of the source sum.
    a = m*states[-1]-a_power*rho
    residue = rho % m
    margin = m*(rho-states[-1])
    prefix_guards = guards(word)
    matches = [n for n in range(2, m+2)
               if "".join(str(x % 2) for x in orbit(n, j)[:-1]) == word]
    checks = dict(
        all_first_drop_guards=all(g["passed"] for g in prefix_guards),
        first_drop_predicate=all(3**word[:k].count("1") >= 2**k
                                 for k in range(j)) and a_power < m,
        least_representative_interval=2 <= rho <= m+1,
        previous_class_member_below_two=rho-m < 2,
        residue_matches=rho % m == (-a*pow(a_power, -1, m)) % m,
        affine_congruence=(a_power*rho+a) % m == 0,
        direct_parity_matches=parity == word,
        affine_endpoint_matches=m*states[-1] == a_power*rho+a,
        margin_matches_direct_descent=margin == (m-a_power)*rho-a,
    )
    extra = dict(
        unique_representative_by_direct_iteration=matches == [rho],
        recovered_A_matches_source_sum=a == sum(
            2**i*3**word[i+1:].count("1")
            for i, bit in enumerate(word) if bit == "1"),
    )
    value = dict(word=word, length=j, q=q, modulus=m, D=m-a_power,
                 A=a, residue=residue, rho=rho, M=margin,
                 prefix_guards=prefix_guards, trajectory=states,
                 actual_parity=parity, checks=checks)
    return value, extra


def main():
    raw = INPUT.read_bytes()
    saved = json.loads(raw)
    left, left_extra = endpoint("11010", 11)
    right, right_extra = endpoint("11100", 23)
    b, r_jump, carry = 4, 12, 0
    edge_checks = dict(
        both_endpoint_checks=all(left["checks"].values()) and all(right["checks"].values()),
        directed_adjacent_swap=left["word"][:2]+"10"+left["word"][4:] == right["word"],
        same_length_and_ones=left["length"] == right["length"] and left["q"] == right["q"],
        strict_coefficient_drop=left["D"] > 0,
        numerator_difference=left["A"]-right["A"] == b,
        nonzero_residue_jump=0 < r_jump < 32 and r_jump == b*pow(27, -1, 32) % 32,
        binary_carry=carry in (0, 1) and carry == (left["rho"]-2+r_jump)//32,
        representative_difference=right["rho"]-left["rho"] == r_jump-carry*32,
        exact_swap_margin_formula=right["M"]-left["M"] == left["D"]*(r_jump-carry*32)+b,
    )
    expected = dict(swap_index_zero_based=2, u="11", v="0", r=2, s=0,
                    B=b, R=r_jump, carry=carry, original=left, swapped=right,
                    margin_delta=right["M"]-left["M"], required_upper_bound=0,
                    conjectured_inequality_holds=False, checks=edge_checks)
    completed = []
    for j in range(1, 5):
        words = sorted({"".join(str(x % 2) for x in orbit(n, j)[:-1])
                        for n in range(2, 2**j+2)})
        selected = [w for w in words if all(g["passed"] for g in guards(w))]
        edges = [(w, i) for w in selected for i in range(j-1)
                 if w[i:i+2] == "01" and
                 all(g["passed"] for g in guards(w[:i]+"10"+w[i+2:]))]
        completed.append(dict(length=j, all_parity_classes_present=len(words) == 2**j,
                              first_drop_words=selected, guarded_edges=edges))
    expected_lengths = [dict(length=j, first_drop_words_visited=count,
                             directed_01_pairs_seen=0, guarded_edges_checked=0,
                             rejected_swapped_guard=0, completed_length=True)
                        for j, count in [(1, 1), (2, 1), (3, 0), (4, 1)]]
    expected_lengths.append(dict(length=5, first_drop_words_visited=1,
                                 directed_01_pairs_seen=1, guarded_edges_checked=1,
                                 rejected_swapped_guard=0, completed_length=False))
    checks = dict(
        entire_counterexample_matches=saved["counterexample"] == expected,
        all_endpoint_checks=all(left["checks"].values()) and all(right["checks"].values()),
        all_independent_endpoint_checks=all(left_extra.values()) and all(right_extra.values()),
        all_edge_checks=all(edge_checks.values()),
        actual_exceeds_required_bound=expected["margin_delta"] == 64 > expected["required_upper_bound"],
        entire_lengths_matches=saved["lengths"] == expected_lengths,
        completed_lengths_independently_replayed=[c["first_drop_words"] for c in completed]
            == [["0"], ["10"], [], ["1100"]] and all(
                c["all_parity_classes_present"] and not c["guarded_edges"] for c in completed),
        checked_edges_exactly_the_witness=saved["checked_edges"] == [expected],
        original_failures_empty=saved["failures"] == [],
        stopping_report_exact=saved["requested_max_length"] == 24 and
            saved["result"] == "COUNTEREXAMPLE" and saved["completed_lengths"] == [1, 2, 3, 4]
            and saved["last_visited_length"] == 5 and saved["complete_through_requested_bound"] is False,
        class_containing_one_retained=orbit(1, 2) == [1, 2, 1] and
            orbit(5, 2) == [5, 8, 4],
    )
    failures = [name for name, passed in checks.items() if not passed]
    report = dict(result="PASS" if not failures else "FAIL", input_path="certificate.json",
                  input_sha256=hashlib.sha256(raw).hexdigest(), checks=checks, failures=failures,
                  counterexample=expected, independent_endpoint_checks=[left_extra, right_extra],
                  completed_length_replay=completed, lengths=expected_lengths,
                  scope="Existing L109 witness and completed lengths1–4 only; length5 incomplete, lengths6–24 untested",
                  general_carry_proof="Manual audit in canonical L109; finite replay alone does not prove the general formula")
    OUTPUT.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(f"L109 audit: {report['result']}; failures: {failures}")
    print(f"Actual margin difference: {expected['margin_delta']}; required upper bound: 0")
    print("Replayed completed lengths: 1–4; length5 remains incomplete; lengths6–24 untested")
    print(f"Certificate: {OUTPUT.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
