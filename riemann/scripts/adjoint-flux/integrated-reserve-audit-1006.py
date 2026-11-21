"""Read-only replay of C467c's saved certificate, with audit-specific checks.

The original generator is never invoked and its artifacts are not rewritten.
This checks finite arithmetic only; the analytic audit is canonical in C467c.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import runpy


def main():
    base = Path(__file__).parent
    source = base / "integrated-reserve-certificate-1004.py"
    certificate = source.with_suffix(".json")
    output = Path(__file__).with_suffix(".json")
    raw = certificate.read_bytes()
    data = json.loads(raw)
    verifier = runpy.run_path(str(source))
    val, rec = verifier["value"], verifier["record"]
    grid = 2**64
    dt = F(1, 1920 * 256)
    report = {
        "scope": "All accepted saved tubes and exact comparisons; analytic antecedents are audited in C467c, audit1006.",
        "source": str(source), "source_sha256": sha256(source.read_bytes()).hexdigest(),
        "certificate": str(certificate), "certificate_sha256": sha256(raw).hexdigest(),
        "verification_failures": [],
    }
    try:
        assert data["constants"] == {
            "h": rec(F(1, 2209)), "T": rec(F(1, 1920)), "a": rec(F(1, 16)),
            "steps": 256, "grid": grid, "mass_grid": 10**40,
        }
        expected_grid = {
            (F(580+2*i, 10000), F(582+2*i, 10000), F(j, 10000), F(j+1, 10000))
            for i in range(22) for j in range(12)
        }
        actual_grid = [tuple(val(b[k]) for k in ("rlo", "rhi", "vlo", "vhi"))
                       for b in data["boxes"]]
        assert len(actual_grid) == 264 and set(actual_grid) == expected_grid
        for b in data["boxes"]:
            assert val(b["center_half_width"]) == F(1, 16)-val(b["rhi"])-val(b["vhi"])/3-F(1, 10**6)

        # This executes every saved accepted row, all 64 bump-envelope bins,
        # exact moments, disjointness, mass arithmetic, and both thresholds.
        replay = verifier["verify_saved"](data)
        assert replay == data["summary"]
        assert (replay["accepted_boxes"], replay["rejected_boxes"], replay["verified_tubes"]) == (100, 164, 25600)

        gaps, radius_slacks, shape_slacks, losses = [], [], [], []
        for b in data["boxes"]:
            if not b["accepted"]:
                continue
            rlo, rhi, vhi = (val(b[k]) for k in ("rlo", "rhi", "vhi"))
            lo = F(verifier["floor_grid"](rlo*rlo), grid)
            v = F(verifier["ceil_grid"](vhi), grid)
            loss = F(0)
            for j, row in enumerate(b["tubes"]):
                ell, w, next_lo, next_v, next_loss = (F(x, grid) for x in row)
                hi = rhi*rhi-F(567, 100)*j*dt
                sminus, splus = verifier["sqrt_lower"](ell), verifier["sqrt_upper"](hi)
                assert 0 <= sminus and sminus*sminus <= ell < (sminus+F(1, grid))**2
                assert splus*splus >= hi and (splus-F(1, grid))**2 < hi
                assert 0 < next_lo < lo and next_v > v >= 0 and next_loss > loss
                assert hi > ell > w*w and sminus > w
                decay, growth, _ = verifier["rates"](ell, w, hi)
                gaps.append(sminus-w)
                radius_slacks.append(lo-ell-decay*dt)
                shape_slacks.append(w-v-growth*dt)
                lo, v, loss = next_lo, next_v, next_loss
            losses.append(loss)
            assert verifier["exp_negative_lower"](F(15, 64)+loss) > 0
        assert min(radius_slacks) > 0 and min(shape_slacks) > 0

        actual = val(replay["mass_lower_over_exp_minus_H0"])
        required = val(replay["required_initial_upper_over_exp_minus_H0"])
        assert actual == F(12701285019439211927675528954987981661,
                           31250000000000000000000000000000000000000000000000000)
        assert actual > F(4, 10**16) > F(2, 10**16) > F(8, 10**17) > required > 0
        # Audit the elementary replacement tan(1/48)<1/47 using sin x<=x,
        # cos x>=1-x^2/2, rather than trusting a floating trigonometric call.
        x = F(1, 48)
        assert x/(1-x*x/2) < F(1, 47)
        assert certificate.read_bytes() == raw
        report.update(
            replay=replay,
            minimum_gap_throughout_tubes=rec(min(gaps)),
            minimum_radius_exit_slack=rec(min(radius_slacks)),
            minimum_shape_exit_slack=rec(min(shape_slacks)),
            maximum_accumulated_loss=rec(max(losses)),
            monotone_endpoint_bounds_checked=True,
            square_root_enclosures_checked=True,
            original_grid_and_constants_checked=True,
            original_certificate_unchanged=True,
            rejected_box_reasons=dict(Counter(b["failure"] for b in data["boxes"] if not b["accepted"])),
            all_checks_passed=True,
        )
    except Exception as exc:
        report["verification_failures"].append(f"{type(exc).__name__}: {exc}")
        report["all_checks_passed"] = False
        output.write_text(json.dumps(report, indent=2)+"\n")
        print(f"FAIL: {report['verification_failures']}; full audit: {output}")
        raise

    output.write_text(json.dumps(report, indent=2)+"\n")
    print(f"PASS: {replay['accepted_boxes']} accepted boxes, {replay['verified_tubes']} saved tubes; {replay['rejected_boxes']} uncertified boxes contribute zero.")
    print(f"Mass/e^-H0: lower {float(actual):.12g} > 4e-16; initial upper {float(required):.12g} < 8e-17; ratio {float(actual/required):.9g}.")
    print(f"Every-time gap lower {float(min(gaps)):.12g} > 0; all strict tube barriers pass; verification failures: [].")
    print(f"Original certificate unchanged; full audit: {output}")


if __name__ == "__main__":
    main()
