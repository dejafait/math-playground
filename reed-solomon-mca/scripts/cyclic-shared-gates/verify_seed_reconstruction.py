"""Replay every abstract seed closure by simultaneous bit-mask updates."""

import hashlib
import itertools
import json
import math
from pathlib import Path


def mask(indices):
    return sum(1 << i for i in indices)


def main():
    source = Path(__file__).with_name("seed-reconstruction-result.json")
    certificate_bytes = source.read_bytes()
    certificate = json.loads(certificate_bytes)
    gates = []
    for t in range(16):
        # Separate presentation from the producer: a whole gate and a mask
        # of positions at which a unique fractional-linear recovery is valid.
        triples = [
            ([-1, 0, 4, 6, 8, 9], [-1, 0, 4, 6, 8, 9]),
            ([-1, 0, 1, 2, 6, 7, 8, 9, 10], [-1, 0, 1, 6, 7, 9, 10]),
            ([-2, -1, 0, 1, 4, 5, 6, 7, 8, 9], [-2, -1, 0, 4, 5, 6, 7, 8, 9]),
        ]
        for whole, allowed in triples:
            gates.append((mask({(t + i) % 16 for i in whole}),
                          mask({(t + i) % 16 for i in allowed})))
    rows = certificate["examined_closures"]
    assert len(rows) == math.comb(16, 7)
    maximum = 0
    maximum_case = None
    for seeds, row in zip(itertools.combinations(range(16), 7), rows):
        assert row["seeds"] == list(seeds)
        current = mask(seeds)
        while True:
            added = 0
            for whole, allowed in gates:
                missing = whole & ~current
                if missing and missing & (missing - 1) == 0 and missing & allowed:
                    added |= missing
            if added == 0:
                break
            current |= added
        closure = [i for i in range(16) if current & (1 << i)]
        assert row["closure"] == closure
        if len(closure) > maximum:
            maximum = len(closure)
            maximum_case = row
    assert certificate["largest_closure"] == maximum == 9
    assert certificate["seed_sets_examined"] == len(rows) == 11440
    assert certificate["required_closure"] == 16
    assert certificate["field_assignments_tested"] == certificate["rank_tests"] == 0
    assert certificate["witness"] is None
    result = {
        "verified": True,
        "certificate_sha256": hashlib.sha256(certificate_bytes).hexdigest(),
        "all_seed_sets_replayed": len(rows),
        "largest_closure": maximum,
        "required_closure": 16,
        "failure_count": 0,
        "maximal_case": maximum_case,
        "scope": "Only the stated one-unknown fractional-linear rules on abstract indices; no nonlinear elimination or field labeling is excluded.",
    }
    output = source.with_name("seed-reconstruction-audit.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS: all {len(rows)} seed sets replayed; actual maximum {maximum}; "
          "required 16; failures 0.")
    print(f"Audit: {output.relative_to(Path.cwd())}")
    print(f"Complete certificate: {source.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
