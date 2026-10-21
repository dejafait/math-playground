"""Abstract-index diagnostic; no field labels, rank tests or family census."""

import itertools
import json
from pathlib import Path


def gate_rules():
    definitions = [
        ("third", (-1, 0, 4, 9, 6, 8), (-1, 0, 4, 9, 6, 8)),
        ("second", (-1, 0, 1, 2, 6, 7, 8, 9, 10), (-1, 0, 1, 6, 7, 9, 10)),
        ("first", (-2, -1, 0, 1, 4, 5, 6, 7, 8, 9), (-2, -1, 0, 4, 5, 6, 7, 8, 9)),
    ]
    rules = []
    for name, offsets, solvable in definitions:
        for t in range(16):
            indices = {(t + offset) % 16 for offset in offsets}
            assert len(indices) == len(offsets)
            for offset in solvable:
                target = (t + offset) % 16
                required = indices - {target}
                rules.append((name, t, target, required))
    return rules


def closure(seeds, rules):
    known = set(seeds)
    steps = []
    while True:
        changed = False
        for name, t, target, required in rules:
            if target not in known and required <= known:
                steps.append({"gate": name, "t": t, "new_index": target,
                              "required_indices": sorted(required)})
                known.add(target)
                changed = True
        if not changed:
            return known, steps


def main():
    rules = gate_rules()
    closures = []
    witness = None
    for seeds in itertools.combinations(range(16), 7):
        known, steps = closure(seeds, rules)
        closures.append({"seeds": list(seeds), "closure": sorted(known)})
        if len(known) == 16:
            witness = {"seeds": list(seeds), "steps": steps}
            break
    result = {
        "task": "seven-seed abstract-index reconstruction diagnostic",
        "field_assignments_tested": 0,
        "rank_tests": 0,
        "required_closure": 16,
        "largest_closure": max(len(row["closure"]) for row in closures),
        "seed_sets_examined": len(closures),
        "witness": witness,
        "examined_closures": closures,
        "qualification": "Rules require analytic fractional-linear justification; no kernel existence is tested.",
    }
    path = Path(__file__).with_name("seed-reconstruction-result.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Largest closure {result['largest_closure']}; required 16; "
          f"seed sets examined {len(closures)}; field assignments 0; rank tests 0.")
    print("Seven-seed witness found." if witness else "No seven-seed witness under these rules.")
    print(f"Certificate: {path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
