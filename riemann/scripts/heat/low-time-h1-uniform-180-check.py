"""Exact-rational replay of all saved moment-to-determinant enclosures.

This checks coverage, sign thresholds and cancellation-sensitive algebra.
It does not independently verify Decimal exp or repeat the quadrature.
"""
import json
from fractions import Fraction as F
from pathlib import Path


class R:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def read(data):
        return R(data["lower"], data["upper"])

    def __add__(self, other):
        other = other if isinstance(other, R) else R(other)
        return R(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return R(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -(other if isinstance(other, R) else R(other))

    def __mul__(self, other):
        other = other if isinstance(other, R) else R(other)
        ends = [a*b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return R(min(ends), max(ends))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, R) else R(other)
        assert not other.lo <= 0 <= other.hi
        return self * R(1/other.hi, 1/other.lo)

    def __pow__(self, n):
        result = R(1)
        for _ in range(n):
            result = result*self
        return result

    def contained_by(self, record):
        return F(record["lower"]) <= self.lo <= self.hi <= F(record["upper"])


def main():
    source = Path(__file__).with_name("low-time-h1-uniform-180.json")
    data = json.loads(source.read_text())
    assert data["status"] == "certified" and data["failed_panels"] == []
    assert (data["precision"], data["parameter_panels"], data["spatial_panels"],
            data["theta_terms"], data["spatial_cutoff"], data["taylor_remainder_order"]) == (100, 256, 64, 4, 2, 8)
    assert len(data["panels"]) == 256
    assert (R.read(data["tails"]["spatial"])+R.read(data["tails"]["theta"])).contained_by(data["tails"]["total"])
    assert 0 < F(data["tails"]["total"]["upper"]) < F("7.836e-25")
    checks = []
    for i, panel in enumerate(data["panels"]):
        lam = R.read(panel["lambda"])
        assert panel["index"] == i and lam.lo == F(i, 5120) and lam.hi == F(i+1, 5120)
        assert panel["strict_signs_certified"] is True
        moments = {int(k): R.read(v) for k, v in panel["moments"].items()}
        assert set(moments) == {0, 2, 4, 6, 8}
        assert all(v.lo > 0 for v in moments.values())
        assert all(R.read(v).lo >= 0 for v in panel["quadrature_error_bounds"].values())
        m0 = moments[0]
        a, b = moments[2]/(2*m0), moments[4]/(24*m0)
        c, d = moments[6]/(720*m0), moments[8]/(40320*m0)
        for key, val in zip(("a", "b", "c", "d"), (a, b, c, d)):
            assert val.contained_by(panel["coefficients"][key])
        s2 = a*a-2*b
        s3 = a*a*a-3*a*b+3*c
        s4 = a*a*a*a-4*a*a*b+2*b*b+4*a*c-4*d
        for key, val in zip(("S2", "S3", "S4"), (s2, s3, s4)):
            assert val.contained_by(panel[key])
        # Use exact rational intermediate intervals, independently of Decimal.
        determinant = s2*s4-s3*s3
        assert determinant.contained_by(panel["determinant"])
        assert F(panel["S2"]["lower"]) > F("3.714e-5")
        assert F(panel["determinant"]["lower"]) > F("9.7e-16")
        assert F(panel["determinant"]["upper"]) < F("7.026e-15")
        assert moments[0].lo > F("0.49712")
        checks.append({"index": i, "closed_parameter_panel_exact": True,
                       "rational_algebra_contained": True, "strict_thresholds_passed": True})
    summary = data["summary"]
    for summary_key, key, side, operation in (
            ("minimum_mass_lower", "moments", "lower", min),
            ("minimum_S2_lower", "S2", "lower", min),
            ("minimum_determinant_lower", "determinant", "lower", min),
            ("maximum_determinant_upper", "determinant", "upper", max)):
        values = [F((row[key]["0"] if key == "moments" else row[key])[side]) for row in data["panels"]]
        assert F(summary[summary_key]) == operation(values)
    output = source.with_name("low-time-h1-uniform-180-check.json")
    result = {"status": "passed", "panels_checked": 256, "failures": [],
              "scope": "exact coverage and moment-algebra replay; quadrature/exp governed by the proof and L037",
              "thresholds": {"M0": ">0.49712", "S2": ">3.714e-5", "determinant": ">9.7e-16 and <7.026e-15"},
              "panels": checks}
    output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS: 256/256 closed panels, rational moment-algebra replay and strict thresholds; failures=0")
    print(f"Audit certificate: {output.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
