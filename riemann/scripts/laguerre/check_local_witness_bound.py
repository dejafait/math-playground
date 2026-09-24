"""Exact arithmetic for L321 and a limited check of its saved sign inputs.

The analytic estimates are proved in L321. This script checks their rational
cutoff comparison and the saved L315 margins, coverage and source digests.
It does not rerun or independently verify the Fourier quadrature, polynomial
construction, or Decimal implementation.
"""

from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read_json(relative_path):
    data = (ROOT / relative_path).read_bytes()
    return json.loads(data), hashlib.sha256(data).hexdigest()


def main():
    radius, anchor = Q(7, 2), Q(3, 2)
    p = (anchor / radius) ** 2
    assert p == Q(9, 49)
    assert 20 - radius >= 1
    bound = 4608 * 40**4 * Q(6, 5)**6 * Q(11, 10)**2
    assert bound == Q(26638226030592, 625) < 43 * 10**9
    tail_ratio = 2 * (43 * 10**9) * p**15 / (1 - p)
    assert tail_ratio == Q(43000000000 * 9**15, 20 * 49**14) < 1
    assert 43000000000 * 9**15 < 20 * 49**14
    assert 15 <= 17

    cert, cert_digest = read_json(
        "scripts/laguerre/exterior-ordering-certificate.json"
    )
    source, source_digest = read_json(cert["source_fourier_inputs"])
    assert source_digest == cert["source_sha256"]
    _, moment_digest = read_json(source["source_moments"])
    assert moment_digest == source["source_sha256"]
    audit, _ = read_json("scripts/laguerre/exterior-ordering-audit.json")
    assert audit["certificate_sha256"] == cert_digest
    assert audit["checks_passed"] is True
    assert audit["height_band"] == [20, 40]

    levels = set(map(str, range(1, 18)))
    assert set(cert["mass_denominators"]) == levels
    for interval in cert["mass_denominators"].values():
        assert 0 < Q(interval["lower"]) <= Q(interval["upper"])

    expected = {"R_1"} | set(map(str, range(1, 17)))
    previous, count = Q(20), 0
    for cell in cert["cells"]:
        left, right = map(Q, cell["a_interval"])
        assert left == previous < right
        previous = right
        assert set(cell["comparisons"]) == expected
        for name, interval in cell["comparisons"].items():
            lower, upper = Q(interval["lower"]), Q(interval["upper"])
            target = Q(5, 10**20) if name == "R_1" else Q(7, 10**19)
            assert target < lower <= upper
            count += 1
    assert previous == 40
    assert len(cert["cells"]) == 1024 and count == 17408

    print(json.dumps({
        "exact_checks_passed": True,
        "height_band": [20, 40],
        "circle_radius": str(radius),
        "anchor": str(anchor),
        "circle_to_anchor_ratio_upper_bound": str(bound),
        "simplified_ratio_upper_bound": 43 * 10**9,
        "tail_comparison_upper_bound_at_level_15": str(tail_ratio),
        "witness_cutoff_at_most": 15,
        "inherited_signed_levels": 17,
        "inherited_height_cells_checked": len(cert["cells"]),
        "inherited_comparison_margins_checked": count,
        "inherited_certificate_sha256": cert_digest,
        "qualification": (
            "checks exact cutoff arithmetic and saved input consistency; "
            "does not independently verify quadrature, polynomial "
            "construction or Decimal implementation"
        ),
    }, indent=2))


if __name__ == "__main__":
    main()
