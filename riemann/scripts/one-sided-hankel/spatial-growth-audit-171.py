"""Replay the reviewed L709--L711 arithmetic without changing prior artifacts.

Every original calculation is rerun; full certificates, including all cells,
are compared. Analytic hypotheses/signs/uniformity are audited in the lemmas,
not established by this script. Decimal previews never decide a comparison.
"""
import ast
import contextlib
from fractions import Fraction
import hashlib
import io
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
STEMS = (
    "spatial-complex-phase-166",
    "spatial-residue-rates-167",
    "spatial-unit-contour-rates-168",
)
EXPECTED_COUNTS = (21, 13, 28)


def fraction(value):
    assert isinstance(value["numerator"], int)
    assert isinstance(value["denominator"], int) and value["denominator"] > 0
    return Fraction(value["numerator"], value["denominator"])


def validate_fractions(value):
    if isinstance(value, dict):
        if "numerator" in value and "denominator" in value:
            fraction(value)
            return 1
        return sum(validate_fractions(v) for v in value.values())
    if isinstance(value, list):
        return sum(validate_fractions(v) for v in value)
    return 0


class RedirectCertificate(ast.NodeTransformer):
    def __init__(self, destination):
        self.destination = destination
        self.replacements = 0

    def visit_Assign(self, node):
        if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) and node.targets[0].id == "path":
            assert isinstance(node.value, ast.Call)
            assert isinstance(node.value.func, ast.Attribute)
            assert node.value.func.attr == "with_suffix"
            self.replacements += 1
            node.value = ast.Call(func=ast.Name(id="Path", ctx=ast.Load()),
                                  args=[ast.Constant(str(self.destination))], keywords=[])
        return node


def replay(stem, expected_count):
    source_path = BASE / (stem + ".py")
    original_path = BASE / (stem + ".json")
    destination = BASE / (stem + "-replay-171.json")
    source = source_path.read_text()
    original_bytes = original_path.read_bytes()
    old = json.loads(original_bytes)
    transformer = RedirectCertificate(destination)
    tree = transformer.visit(ast.parse(source))
    assert transformer.replacements == 1
    ast.fix_missing_locations(tree)
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        exec(compile(tree, str(source_path), "exec"), {"__file__": str(source_path), "__name__": "__main__"})
    replayed = json.loads(destination.read_text())
    assert original_path.read_bytes() == original_bytes, "Original certificate changed"
    assert old == replayed, "Full replay differs from the original certificate"
    assert len(replayed["checks"]) == expected_count
    failures = []
    comparisons = {}
    for name, row in replayed["checks"].items():
        actual, required = fraction(row["actual"]), fraction(row["required"])
        relation = row["relation"]
        passed = {"<": actual < required, ">": actual > required,
                  "=": actual == required, "<=": actual <= required}[relation]
        if not passed:
            failures.append(name)
        comparisons[name] = {"actual": str(actual), "relation": relation,
                             "required": str(required), "passed": passed}
    assert failures == replayed["failures"] == []
    if stem.endswith("166"):
        counts = {name: len(block["cells"]) for name, block in replayed["rate_certificates"].items()}
        assert counts == {"upper_contour": 200, "lower_contour": 200, "real_line": 200}
        counts["negative_tail_derivative"] = len(replayed["negative_tail_derivative_cells"])
        assert counts["negative_tail_derivative"] == 200
    elif stem.endswith("167"):
        counts = {"rectangle": len(replayed["rectangle_cells"])}
        assert counts == {"rectangle": 40}
    else:
        counts = {"top_segments": len(replayed["top_segments"]),
                  "left_real_cells": len(replayed["left_real_cells"]),
                  "left_c_derivative_cells": len(replayed["left_c_derivative_cells"])}
        counts.update({name: len(rows) for name, rows in replayed["contour_cells"].items()})
        assert counts == {"top_segments": 100, "left_real_cells": 20,
                          "left_c_derivative_cells": 160, "bottom_density": 200,
                          "side_lower_density": 200}
    if "helper" in replayed:
        helper = BASE / replayed["helper"]["path"]
        assert replayed["helper"]["sha256"] == hashlib.sha256(helper.read_bytes()).hexdigest()
    report = dict(source=source_path.name,
                  source_sha256=hashlib.sha256(source.encode()).hexdigest(),
                  original_sha256=hashlib.sha256(original_bytes).hexdigest(),
                  replay=destination.name, full_certificate_equal=True,
                  exact_fraction_records=validate_fractions(replayed),
                  complete_partition_counts=counts, comparisons=comparisons,
                  failures=failures)
    print(f"{stem}: {expected_count} exact comparisons; {sum(counts.values())} complete cells/segments; full replay equal; failures={failures}; {destination.name}")
    return report


reports = {stem: replay(stem, count) for stem, count in zip(STEMS, EXPECTED_COUNTS)}
result = dict(purpose="Complete arithmetic replay for the L709--L712 conceptual audit",
              certificates=reports, failures=[],
              qualification="Analytic proof and source applicability are checked in canonical lemma audit sections; this is auxiliary arithmetic evidence.")
path = BASE / "spatial-growth-audit-171.json"
path.write_text(json.dumps(result, indent=2) + "\n")
for stem, key in ((STEMS[0], "negative_endpoint_rate"),
                  (STEMS[1], "outer_centered_coefficient_margin"),
                  (STEMS[2], "top_rate_vs_endpoint")):
    row = reports[stem]["comparisons"][key]
    print(f"{key}: actual {row['actual']} {row['relation']} required {row['required']}; pass={row['passed']}")
print(f"Total: {sum(EXPECTED_COUNTS)} comparisons; failures=[]; certificate: {path}")
