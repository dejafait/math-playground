"""Replay the finite comparison from canonical intervals, retaining source scope."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name("complete-cubic-comparison-audit.json")
SOURCES = {
    "tr": "L133-other-other-actual-physical-heat-enclosures.md",
    "E": "L137-other-other-e-physical-heat-enclosures.md",
    "ax": "L139-other-other-ax-physical-contraction.md",
    "Q": "L138-other-other-q-physical-contraction.md",
    "G": "L144-other-other-g-physical-heat-enclosures.md",
    "R": "L146-other-other-r-physical-heat-enclosures.md",
}
certificate = json.loads(OUT.with_name("complete-cubic-comparison-certificate.json").read_text())
failures = []
checks = []
hashes = {}
inputs = {}
number = r"(-?\d+(?:\.\d+)?)"


def check(name, passed):
    checks.append({"check": name, "passed": bool(passed)})
    if not passed:
        failures.append(name)


def load_source(name):
    path = ROOT / "lemmas" / name
    raw = path.read_bytes()
    hashes[str(path.relative_to(ROOT))] = hashlib.sha256(raw).hexdigest()
    return raw.decode()


for term, filename in SOURCES.items():
    source = load_source(filename).split("## Conclusion", 1)[1].split("## Proof", 1)[0]
    if term in ("G", "R"):
        rows = re.findall(r"^\|\s*([36])\s*\|([^\n]+)\|\s*$", source, re.M)
        pairs = {i: tuple(F(v.strip()) for v in rest.split("|")[-2:]) for i, rest in rows}
    else:
        rows = re.findall(number + r"\s*<\s*K_\(([36])," + term + r"\)\s*<\s*" + number, source)
        pairs = {i: (F(lo), F(hi)) for lo, i, hi in rows}
    check(f"{term}: both canonical intervals extracted", set(pairs) == {"3", "6"})
    inputs[term] = {}
    for i, pair in pairs.items():
        check(f"{term}/{i}: ordered endpoints", pair[0] < pair[1])
        check(f"{term}/{i}: assembly input matches canonical interval",
              pair == tuple(map(F, certificate["inputs"][term][i])))
        inputs[term][i] = pair

gamma_source = load_source("L070-first-pair-frozen-circulation-symbol.md")
mixed_source = load_source("L084-complete-mixed-leading-scale.md")
assembly_source = load_source("L124-complete-other-other-cubic-limit-assembly.md")
check("L070 records bounded nonnegative integrand", "It is nonnegative and bounded by 1." in gamma_source)
check("L070 uses one third of normalized integral", "gamma=(1/3) integral" in gamma_source)
check("L084 imports that same gamma", "integral in L070(3)" in mixed_source)
check("L124 outside factor is three", "a^3 O_i(a)=3 K_(i,oo)" in assembly_source)
d_conclusion = mixed_source.split("## Conclusion", 1)[1].split("## Proof", 1)[0]
d_rows = re.findall(number + r"\s*<\s*D_([36])\s*<\s*" + number, d_conclusion)
d_intervals = {i: (F(lo), F(hi)) for lo, i, hi in d_rows}
check("both continuum diagnostic intervals extracted", set(d_intervals) == {"3", "6"})

results = {}
for i in ("3", "6"):
    signed = {term: (-pair[i][1], -pair[i][0]) if term == "Q" else pair[i]
              for term, pair in inputs.items()}
    bounds = tuple(sum(p[j] for p in signed.values()) for j in (0, 1))
    scaled = tuple(3 * x for x in bounds)
    check(f"{i}: all signed terms match complete assembly certificate",
          all(pair == tuple(map(F, certificate["results"][i]["signed_terms"][term]))
              for term, pair in signed.items()))
    check(f"{i}: complete coefficient endpoints match", bounds == tuple(map(F, certificate["results"][i]["K_oo"])))
    check(f"{i}: factor three applied once", scaled == tuple(map(F, certificate["results"][i]["limit_a3_O"])))
    check(f"{i}: negative diagnostic", d_intervals[i][1] < 0)
    results[i] = {"signed_terms": {k: list(map(str, v)) for k, v in signed.items()},
                  "K_oo": list(map(str, bounds)), "limit_a3_O": list(map(str, scaled)),
                  "D": list(map(str, d_intervals[i]))}

gamma_upper = F(1, 3)  # Import L070(3), proof section 4, by integral monotonicity.
necessary = tuple(map(F, certificate["shear_necessary_gamma_interval"]))
k6 = tuple(map(F, results["6"]["K_oo"]))
d6 = d_intervals["6"]
check("necessary gamma interval exact", necessary == (k6[0] / (-4*d6[0]), k6[1] / (-4*d6[1])))
check("known gamma upper bound strictly below necessary interval", gamma_upper < necessary[0])
shear_lower = 3*k6[0] + 12*gamma_upper*d6[0]
shear_upper = 3*k6[1]  # gamma>0 and D_6<0 give a strict upper bound.
check("shear two-group lower endpoint equals 11864.87528", shear_lower == F("11864.87528"))
check("shear two-group coefficient strictly positive", shear_lower > 0)
check("triplet complete coefficient strictly negative", F(results["3"]["K_oo"][1]) < 0)
check("original assembly has no failures", certificate["failures"] == [])

audit = {
    "step_id": "YM-20261012-174-complete-cubic-comparison-audit",
    "source_hashes": hashes, "results": results,
    "gamma_bound": {"lower_strict": "0", "upper_nonstrict": str(gamma_upper),
                    "citation": "L070(3), proof section 4; same gamma imported by L084"},
    "shear_necessary_gamma_interval": list(map(str, necessary)),
    "shear_two_group_strict_interval": [str(shear_lower), str(shear_upper)],
    "triplet_two_group_strict_upper": results["3"]["limit_a3_O"][1],
    "qualification": "Canonical limits and certified-input/IEEE intervals imported; no independent tensor or processor verification. Text matches identify sources, not proofs.",
    "prior_parser_failure": "complete-cubic-comparison-audit-first-parser-failure.json: unrestricted regex selected fractions from proof text; final extraction is restricted to canonical Conclusion sections.",
    "checks": checks, "failures": failures,
}
OUT.write_text(json.dumps(audit, indent=2) + "\n")
print(f"Canonical interval/certificate checks: {len(checks)}; failures: {len(failures)}")
print(f"gamma <= {gamma_upper}; shear compensation requires gamma > {necessary[0]}")
print(f"Two-group triplet upper {results['3']['limit_a3_O'][1]} < required threshold 0")
print(f"Two-group shear limit in ({shear_lower}, {shear_upper}); required lower threshold 0")
print(f"Certificate: {OUT.relative_to(ROOT)}")
if failures:
    raise SystemExit(1)
