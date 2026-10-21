"""Independent fixed-root L030 audit; never imports or rewrites the generator.

Enumerate forward words and solve their affine equations, then replay actual
parities. Check the complete existing JSON and the canonical displayed tables.
"""
import hashlib
import itertools
import json
from pathlib import Path
import re


BASE = Path(__file__).resolve().parents[2]
SOURCE = BASE / "scripts/guarded-ancestor/depth12_certificate.json"
LEMMA = BASE / "lemmas/L030-guarded-residue290-depth12-cover-refutation.md"
OUT = BASE / "scripts/guarded-ancestor/depth12_audit_certificate.json"
ROOT, DEPTH = 3616859, 12
WORD = "OOEOOOEOOOOEE"


def step(x):
    return (3 * x + 1) // 2 if x & 1 else x // 2


def replay(x, word):
    states = [x]
    for letter in word:
        if (x & 1) != int(letter == "O"):
            return None
        x = step(x)
        states.append(x)
    return states


def affine(word):
    a, b, denominator = 1, 0, 1
    for letter in word:
        if letter == "O":
            a, b = 3 * a, 3 * b + denominator
        denominator *= 2
    return a, b, denominator


def main():
    source_bytes = SOURCE.read_bytes()
    saved = json.loads(source_bytes)
    prose = LEMMA.read_text()
    failures, checks = [], []

    def check(name, actual, required):
        ok = actual == required
        checks.append({"check": name, "passed": ok})
        if not ok:
            failures.append({"check": name, "actual": actual, "required": required})

    states = replay(ROOT, WORD)
    check("root positive and ternary guard", [ROOT > 0, ROOT % 729], [True, 290])
    check("thirteen actual inputs and odd endpoint",
          [states is not None, len(WORD), states[-1] % 2], [True, 13, 1])

    # Exhaust every binary word, using no inverse-node recurrence for discovery.
    accepted = [[{"value": ROOT, "forward_word": "", "states": [ROOT],
                  "a": 1, "b": 0, "denominator": 1}]]
    enumeration = []
    for depth in range(1, DEPTH + 1):
        level = []
        counts = {"depth": depth, "words": 0, "nonintegral": 0,
                  "nonpositive": 0, "parity_rejected": 0, "accepted": 0}
        for letters in itertools.product("EO", repeat=depth):
            word = "".join(letters)
            counts["words"] += 1
            a, b, denominator = affine(word)
            candidate, remainder = divmod(denominator * ROOT - b, a)
            if remainder:
                counts["nonintegral"] += 1
                continue
            if candidate <= 0:
                counts["nonpositive"] += 1
                continue
            orbit = replay(candidate, word)
            if orbit is None:
                counts["parity_rejected"] += 1
                continue
            check(f"word endpoint {depth}/{word}", orbit[-1], ROOT)
            counts["accepted"] += 1
            level.append({"value": candidate, "forward_word": word,
                          "states": orbit, "a": a, "b": b,
                          "denominator": denominator})
        check(f"all words length {depth}", counts["words"], 2 ** depth)
        accepted.append(level)
        enumeration.append(counts)

    values = [sorted(row["value"] for row in level) for level in accepted]
    levels = []
    for depth, level in enumerate(accepted):
        # Original storage order is the lexicographic reversed (inverse) word.
        ordered = sorted(level, key=lambda row: row["forward_word"][::-1])
        nodes = []
        prior = {row["inverse_word"]: i for i, row in enumerate(levels[-1])} if depth else {}
        for row in ordered:
            p = row["value"]
            inverse_word = row["forward_word"][::-1]
            node = {"value": p, "inverse_word": inverse_word}
            if depth:
                node.update(parent_index=prior[inverse_word[:-1]],
                            branch=inverse_word[-1], residue27=p % 27,
                            smaller_than_root=p < ROOT)
            if depth < DEPTH:
                node["odd_inverse_legal"] = (2 * p - 1) % 3 == 0
            nodes.append(node)
        levels.append(nodes)

    # Additional pointwise branch completeness check, independent of filters.
    for depth, level in enumerate(levels[:-1]):
        for index, node in enumerate(level):
            y = node["value"]
            candidates = [("E", 2 * y)]
            q, r = divmod(2 * y - 1, 3)
            if r == 0 and q > 0 and q % 2 == 1:
                candidates.append(("O", q))
            children = [(child["branch"], child["value"])
                        for child in levels[depth + 1] if child["parent_index"] == index]
            check(f"both guarded branches {depth}/{index}", children, candidates)

    smaller = [{"depth": d, "value": row["value"], "residue27": row["residue27"]}
               for d, level in enumerate(levels[1:], 1) for row in level
               if row["value"] < ROOT]
    hits = [{"depth": d, "value": row["value"], "inverse_word": row["inverse_word"],
             "smaller_than_root": row["smaller_than_root"]}
            for d, level in enumerate(levels[1:], 1) for row in level
            if row["residue27"] == 20]
    covered = any(row["smaller_than_root"] for row in hits)
    tree = {"levels": levels, "level_values": values, "below_root_nodes": smaller,
            "residue20_hits": hits, "covered": covered,
            "level_counts": [len(level) for level in levels]}
    check("required covered endpoints versus actual", covered, False)

    # Direct exhaustive finite residue coding, not the generator's one-bit lift.
    lifts = []
    for length in range(1, len(WORD) + 2):
        prefix = (WORD + "O")[:length]
        candidates = [r for r in range(2 ** length) if replay(r, prefix) is not None]
        check(f"unique coding class length {length}", len(candidates), 1)
        lifts.append({"length": length, "residue": candidates[0], "modulus": 2 ** length})
    residue, modulus = lifts[-1]["residue"], lifts[-1]["modulus"]
    roots = [residue + modulus * k for k in range(729)
             if (residue + modulus * k) % 729 == 290]
    check("unique least positive CRT root", roots, [ROOT])
    coding = {"binary_residue": residue, "binary_modulus": modulus,
              "lifts": lifts, "first_root": ROOT, "root_modulus": modulus * 729}
    expected = {"target": "guarded residue290 depth12 smaller residue20 ancestor",
                "word": WORD, "required_depth": DEPTH, "coding": coding,
                "tested": [{"root": ROOT, "covered": False}],
                "witness": {"root": ROOT, "parameter": 0, "forward_states": states,
                            "tree": tree}}
    # Whole-object equality covers every saved field, not only level previews.
    check("complete original JSON, including every metadata field", saved, expected)

    forward_section = prose.split("### Full actual forward check\n", 1)[1].split("### Exhaustive", 1)[0]
    printed_states = [(int(i), int(x), branch) for i, x, branch in
                      re.findall(r"\| (\d+) \| (\d+) \| (O|E|endpoint) \|", forward_section)]
    check("canonical forward table", printed_states,
          [(i, x, WORD[i] if i < len(WORD) else "endpoint") for i, x in enumerate(states)])
    block = prose.split("```text\nS_0 = ", 1)[1].split("```", 1)[0]
    displayed = re.findall(r"S_(\d+) = ([\d,\s]+?)(?=\nS_|\Z)", "S_0 = " + block)
    check("canonical set indices", [int(d) for d, _ in displayed], list(range(13)))
    check("all canonical inverse level values",
          [[int(x) for x in re.findall(r"\d+", body)] for _, body in displayed], values)
    below_section = prose.split("| Depth | p | p modulo 27 |", 1)[1].split("In particular", 1)[0]
    printed_below = [tuple(map(int, row)) for row in
                     re.findall(r"\| (\d+) \| (\d+) \| (\d+) \|", below_section)]
    check("canonical below-root table", printed_below,
          [(r["depth"], r["value"], r["residue27"]) for r in smaller])
    hit_section = prose.split("| Depth | p |\n", 1)[1].split("Each is strictly", 1)[0]
    printed_hits = [tuple(map(int, row)) for row in re.findall(r"\| (\d+) \| (\d+) \|", hit_section)]
    check("canonical residue-20 table", printed_hits, [(r["depth"], r["value"]) for r in hits])
    check("original certificate was not modified", SOURCE.read_bytes(), source_bytes)
    summary = {"passed": not failures, "failures": failures,
               "words_checked": sum(row["words"] for row in enumeration),
               "accepted_positive_words": sum(len(level) for level in accepted[1:]),
               "level_counts": tree["level_counts"], "root": ROOT,
               "required_depth": DEPTH, "required_cover_count_at_least": 1,
               "actual_smaller_residue20_count": sum(r["smaller_than_root"] for r in hits),
               "below_root_nodes": smaller, "residue20_hits": hits,
               "checks_passed": sum(row["passed"] for row in checks)}
    report = {"source_sha256": hashlib.sha256(source_bytes).hexdigest(),
              "summary": summary, "checks": checks, "word_enumeration": enumeration,
              "accepted_forward_words": accepted, "independent_expected_certificate": expected}
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Audit passed: {summary['passed']}; failures: {len(failures)}")
    print(f"Forward words checked: {summary['words_checked']}; accepted positive words: {summary['accepted_positive_words']}")
    print(f"Complete level counts: {tree['level_counts']}")
    print(f"Horizon: actual {DEPTH}, required 12; smaller residue-20 ancestors: actual {summary['actual_smaller_residue20_count']}, cover requires at least 1")
    print(f"Full certificate: {OUT.relative_to(BASE)}")
    if failures:
        print("Failed checks: " + ", ".join(row["check"] for row in failures))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
