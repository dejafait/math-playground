"""Complete independent replay of L087's supplementary certificate."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
certificate = HERE / "cyclic-nonrigidity-certificate.json"
before = hashlib.sha256(certificate.read_bytes()).hexdigest()
subprocess.run([sys.executable, str(HERE / "verify_cyclic_nonrigidity.py")], check=True)
after = hashlib.sha256(certificate.read_bytes()).hexdigest()
saved = json.loads(certificate.read_text())
failures = []
checks = {}


def check(name, condition):
    checks[name] = bool(condition)
    if not condition:
        failures.append(name)


def mul(a, b):
    # Polynomial basis 1,u with u^2=u+1; addition is XOR.
    product = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & (b >> j) & 1:
                product ^= 1 << (i + j)
    return product ^ 7 if product & 4 else product


lemma = (ROOT / "lemmas/L072-triangle-balanced-linear-support-witness.md").read_text()
point_rows = [line.split("|")[2:6] for line in lemma.splitlines()
              if line.startswith("| ") and "{" not in line
              and line.split("|")[1].strip() in ["0", "1", "u", "u+1"]]
labels = [cell.strip() for row in point_rows for cell in row]
check("canonical_label_bijection", len(labels) == len(set(labels)) == 16)
label_to_number = {label: i for i, label in enumerate(labels)}
block_rows = [re.findall(r"\{([^}]+)\}", line) for line in lemma.splitlines()
              if line.startswith("| ") and "{" in line]
canonical_blocks = [sorted(label_to_number[x.strip()] for x in block_rows[e][c].split(","))
                    for c in range(4) for e in range(4)]
plane = [[4 * e + y for y in range(4)] for e in range(4)]
plane += [[4 * x + (mul(m, x) ^ e) for x in range(4)]
          for m in [0, 1, 2] for e in range(4)]
check("all_16_canonical_blocks_equal_coordinate_lines", canonical_blocks == plane)
missing_lines = [[4 * x + (mul(3, x) ^ e) for x in range(4)] for e in range(4)]
cyclic = [sorted((b + t) % 16 for b in [0, 1, 4, 6]) for t in range(16)]
differences = [{"marks": [b, c], "residue": (b - c) % 16}
               for b in [0, 1, 4, 6] for c in [0, 1, 4, 6] if b != c]
check("all_12_ordered_differences", sorted(d["residue"] for d in differences)
      == list(range(1, 7)) + list(range(10, 16)))
expected_families = {}
for name, blocks in [("cyclic", cyclic), ("L072", plane)]:
    degrees = {str(x): sum(x in b for b in blocks) for x in range(16)}
    intersections = [{"blocks": [i, j], "intersection": [x for x in range(16)
                       if x in blocks[i] and x in blocks[j]]}
                     for i in range(16) for j in range(i + 1, 16)]
    pairs = [{"pair": [x, y], "count": sum(x in b and y in b for b in blocks)}
             for x in range(16) for y in range(x + 1, 16)]
    edges = [p["pair"] for p in pairs if p["count"] == 0]
    reach = [[x == y or [min(x, y), max(x, y)] in edges
              for y in range(16)] for x in range(16)]
    for k in range(16):
        for x in range(16):
            for y in range(16):
                reach[x][y] = reach[x][y] or (reach[x][k] and reach[k][y])
    components = sorted({tuple(y for y in range(16) if reach[x][y]) for x in range(16)})
    expected = {"blocks": blocks, "degrees": degrees,
                "block_intersections": intersections, "pair_multiplicities": pairs,
                "noncollinearity_edges": edges, "components": [list(c) for c in components],
                "component_sizes": sorted(map(len, components)), "failures": []}
    expected_families[name] = expected
    check(name + "_every_certificate_field", saved[name] == expected)
    check(name + "_all_incidence_hypotheses", len({tuple(b) for b in blocks}) == 16
          and all(len(set(b)) == 4 for b in blocks)
          and set(degrees.values()) == {4}
          and max(len(r["intersection"]) for r in intersections) == 1)
    if name == "cyclic":
        analytic_edges = [[x, y] for x in range(16) for y in range(x + 1, 16)
                          if (y - x) % 16 in [7, 8, 9]]
        required_components = [16]
    else:
        analytic_edges = [[x, y] for x in range(16) for y in range(x + 1, 16)
                          if any(x in b and y in b for b in missing_lines)]
        required_components = [4, 4, 4, 4]
    check(name + "_complete_analytic_graph", edges == analytic_edges)
    check(name + "_required_components", expected["component_sizes"] == required_components)
check("certificate_unchanged", before == after)
check("exact_top_level_schema", set(saved) == {"cyclic", "L072", "failures"})
check("producer_no_failures", saved["failures"] == [])
output = HERE / "cyclic-nonrigidity-audit.json"
output.write_text(json.dumps({"checks": checks, "failures": failures,
    "certificate_sha256_before": before, "certificate_sha256_after": after,
    "ordered_differences": differences, "canonical_labels": labels,
    "omitted_slope_lines": missing_lines, "independent_replay": expected_families}, indent=2) + "\n")
print(f"Audit: {sum(checks.values())}/{len(checks)} checks; required {len(checks)}; failures: {failures}")
print(f"Full replay: 16 blocks, 16 degrees, 120 block pairs, 120 vertex pairs per family; {output}")
raise SystemExit(bool(failures))
