"""Exact finite test of the approved guarded ancestor target.

Write complete forward and inverse certificates; print bounded results.
No external packages and no probabilistic parity assumptions.
"""
import json
from pathlib import Path


WORD = "OOEO" * 2 + "O" * 3 + "E" * 2
DEPTH = 12
OUT = Path(__file__).resolve().parent / "depth12_certificate.json"


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def code_word(word):
    residue = 0
    modulus = 1
    lifts = []
    for i, branch in enumerate(word):
        candidates = []
        for root in (residue, residue + modulus):
            value = root
            for _ in range(i):
                value = shortcut(value)
            if value % 2 == (branch == "O"):
                candidates.append(root)
        assert len(candidates) == 1
        residue = candidates[0]
        modulus *= 2
        lifts.append({"length": i + 1, "residue": residue,
                      "modulus": modulus})
    return residue, modulus, lifts


def replay(root):
    value = root
    states = [value]
    for branch in WORD:
        assert value > 0 and value % 2 == (branch == "O")
        value = shortcut(value)
        states.append(value)
    assert value % 2 == 1
    return states


def inverse_tree(root):
    levels = [[{"value": root, "inverse_word": ""}]]
    hits = []
    for depth in range(1, DEPTH + 1):
        level = []
        for parent_index, parent in enumerate(levels[-1]):
            y = parent["value"]
            children = [("E", 2 * y)]
            if y % 3 == 2:
                children.append(("O", (2 * y - 1) // 3))
            parent["odd_inverse_legal"] = y % 3 == 2
            for branch, p in children:
                assert p > 0 and shortcut(p) == y
                node = {"value": p, "inverse_word": parent["inverse_word"] + branch,
                        "parent_index": parent_index, "branch": branch,
                        "residue27": p % 27, "smaller_than_root": p < root}
                level.append(node)
                if p % 27 == 20:
                    hits.append({"depth": depth, "value": p,
                                 "inverse_word": node["inverse_word"],
                                 "smaller_than_root": p < root})
        levels.append(level)
    return {"levels": levels,
            "level_values": [sorted({node["value"] for node in level}) for level in levels],
            "below_root_nodes": [
                {"depth": d, "value": node["value"], "residue27": node["residue27"]}
                for d, level in enumerate(levels[1:], 1) for node in level
                if node["value"] < root],
            "residue20_hits": hits,
            "covered": any(hit["smaller_than_root"] for hit in hits),
            "level_counts": [len(level) for level in levels]}


def validate_tree(root, tree):
    assert tree["levels"][0] == [{"value": root, "inverse_word": "",
                                 "odd_inverse_legal": root % 3 == 2}]
    for depth in range(1, DEPTH + 1):
        expected = []
        for index, node in enumerate(tree["levels"][depth - 1]):
            y = node["value"]
            expected.append((index, "E", 2 * y))
            if (2 * y - 1) % 3 == 0:
                expected.append((index, "O", (2 * y - 1) // 3))
        actual = [(node["parent_index"], node["branch"], node["value"])
                  for node in tree["levels"][depth]]
        assert actual == expected
        for node in tree["levels"][depth]:
            value = node["value"]
            for _ in range(depth):
                value = shortcut(value)
            assert value == root


def main():
    binary_residue, binary_modulus, lifts = code_word(WORD + "O")
    multiplier = ((290 - binary_residue) * pow(binary_modulus, -1, 729)) % 729
    first_root = binary_residue + binary_modulus * multiplier
    root_modulus = binary_modulus * 729
    assert first_root > 0 and first_root % 729 == 290
    tested = []
    witness = None
    for k in range(256):
        root = first_root + k * root_modulus
        forward = replay(root)
        tree = inverse_tree(root)
        validate_tree(root, tree)
        tested.append({"root": root, "covered": tree["covered"]})
        if not tree["covered"]:
            witness = {"root": root, "parameter": k, "forward_states": forward,
                       "tree": tree}
            break
    certificate = {"target": "guarded residue290 depth12 smaller residue20 ancestor",
                   "word": WORD, "required_depth": DEPTH,
                   "coding": {"binary_residue": binary_residue,
                              "binary_modulus": binary_modulus, "lifts": lifts,
                              "first_root": first_root, "root_modulus": root_modulus},
                   "tested": tested, "witness": witness}
    OUT.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Required ancestor horizon: {DEPTH}; roots tested: {len(tested)}")
    print(f"Guarded root class: {first_root} modulo {root_modulus}")
    if witness is None:
        print("No uncovered root found in this bounded screen; no universal conclusion.")
    else:
        print(f"UNCOVERED root: {witness['root']}; actual forward length: {len(WORD)}")
        print(f"Complete inverse level counts: {witness['tree']['level_counts']}")
        hits = witness["tree"]["residue20_hits"]
        print(f"All residue20 inverse hits: {hits}")
        print("Smaller positive residue20 ancestors through depth12: 0")
    print(f"Certificate: {OUT.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
