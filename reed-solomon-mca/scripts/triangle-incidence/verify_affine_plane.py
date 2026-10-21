"""Supplementary complete certificate for L072; no moment claims."""
import json
from pathlib import Path


def multiply(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7  # u^2+u+1
    return result


labels = {
    (0, 0): "a", (0, 1): "b", (0, 2): "y_1", (0, 3): "y_2",
    (1, 0): "c", (1, 1): "d_1", (1, 2): "d_2", (1, 3): "d_3",
    (2, 0): "z_1", (2, 1): "d_4", (2, 2): "d_5", (2, 3): "w_1",
    (3, 0): "z_2", (3, 1): "d_6", (3, 2): "w_2", (3, 3): "d_7",
}
blocks = []
for x in range(4):
    blocks.append({"id": f"V{x}", "points": [(x, y) for y in range(4)]})
for slope in (0, 1, 2):
    for intercept in range(4):
        blocks.append({"id": f"M{slope}D{intercept}",
                       "points": [(x, multiply(slope, x) ^ intercept)
                                  for x in range(4)]})
triangle = {"V0": {"a", "b", "y_1", "y_2"},
            "M0D0": {"a", "c", "z_1", "z_2"},
            "M1D1": {"b", "c", "w_1", "w_2"}}
for block in blocks:
    block["labels"] = [labels[p] for p in block["points"]]
degrees = {label: sum(label in b["labels"] for b in blocks)
           for label in labels.values()}
pairs = []
for i, left in enumerate(blocks):
    for right in blocks[i + 1:]:
        common = sorted(set(left["labels"]) & set(right["labels"]))
        pairs.append({"left": left["id"], "right": right["id"],
                      "intersection": common,
                      "both_additional": left["id"] not in triangle
                                         and right["id"] not in triangle})
failures = []
if set(labels) != {(x, y) for x in range(4) for y in range(4)} or len(set(labels.values())) != 16:
    failures.append("label bijection")
if len(blocks) != 16 or len({frozenset(b["labels"]) for b in blocks}) != 16:
    failures.append("distinct block count")
if any(len(set(b["labels"])) != 4 for b in blocks):
    failures.append("block size")
if any(degree != 4 for degree in degrees.values()):
    failures.append("degree")
for block in blocks:
    if block["id"] in triangle and set(block["labels"]) != triangle[block["id"]]:
        failures.append("prescribed triangle " + block["id"])
if len(pairs) != 120 or any(len(p["intersection"]) > 1 for p in pairs):
    failures.append("complete pair intersections")
additional_pairs = [p for p in pairs if p["both_additional"]]
if len(additional_pairs) != 78:
    failures.append("additional-pair coverage")
certificate = {
    "field": "F_2[u]/(u^2+u+1); bits 0,1,2,3 denote 0,1,u,u+1",
    "label_bijection": [{"point": p, "label": label} for p, label in labels.items()],
    "blocks": blocks, "triangle_ids": list(triangle), "degrees": degrees,
    "pair_intersections": pairs,
    "actual": {"blocks": len(blocks), "block_size": 4,
               "degree_min": min(degrees.values()), "degree_max": max(degrees.values()),
               "additional_blocks": len(blocks) - len(triangle),
               "additional_pair_count": len(additional_pairs),
               "additional_pair_max_intersection": max(len(p["intersection"]) for p in additional_pairs)},
    "required": {"blocks": 16, "block_size": 4, "degree": 4,
                 "additional_blocks": 13, "additional_pair_max_intersection": 1},
    "failures": failures,
}
output = Path(__file__).with_name("affine-plane-certificate.json")
output.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"{'FAIL' if failures else 'PASS'}: blocks {len(blocks)}/16; degree "
      f"{min(degrees.values())}..{max(degrees.values())}/4; additional pairs "
      f"{len(additional_pairs)}/78; max intersection "
      f"{certificate['actual']['additional_pair_max_intersection']} <= 1.")
print(f"Failures: {failures}; certificate: {output}")
raise SystemExit(bool(failures))
