"""Exact endpoint assembly of canonical full coefficient intervals."""
from fractions import Fraction as F
from pathlib import Path
import json

INPUTS = {
    "tr": {"source": "L133(1)", "3": ["-3417", "742"], "6": ["7862", "13095"]},
    "E": {"source": "L137(1)", "3": ["-5184", "-4342"], "6": ["471", "702"]},
    "ax": {"source": "L139(3)", "3": ["786", "1770"], "6": ["234", "528"]},
    "Q": {"source": "L138(2)", "3": ["13590", "20768"], "6": ["2971", "4137"]},
    "G": {"source": "L144 conclusion", "3": ["-146.92", "-103.56"], "6": ["-315.66", "-222.51"]},
    "R": {"source": "L146 conclusion", "3": ["-74.916", "-52.809"], "6": ["-27.545", "-19.416"]},
}

def pair_json(pair):
    return [str(x) for x in pair]

results = {}
failures = []
for probe in ("3", "6"):
    terms = {}
    for name, record in INPUTS.items():
        lo, hi = map(F, record[probe])
        if not lo < hi:
            failures.append(f"{name}/{probe}: unordered interval")
        terms[name] = (-hi, -lo) if name == "Q" else (lo, hi)
    bounds = tuple(sum(p[j] for p in terms.values()) for j in (0, 1))
    scaled = tuple(3*x for x in bounds)
    results[probe] = {
        "signed_terms": {name: pair_json(p) for name, p in terms.items()},
        "K_oo": pair_json(bounds),
        "limit_a3_O": pair_json(scaled),
        "sign": "negative" if bounds[1] < 0 else "positive" if bounds[0] > 0 else "unresolved",
    }
    print(f"probe {probe}: K_oo in ({float(bounds[0]):.3f}, {float(bounds[1]):.3f}); "
          f"a^3 O limit in ({float(scaled[0]):.3f}, {float(scaled[1]):.3f}); sign {results[probe]['sign']}")

if not F(results["3"]["K_oo"][1]) < 0:
    failures.append("triplet upper bound fails required strict threshold 0")
if not F(results["6"]["K_oo"][0]) > 0:
    failures.append("shear lower bound fails sign threshold 0")

# D_6 is negative; a necessary interval for gamma under K_oo=-4 gamma D_6.
d6_abs = (F("98.877429"), F("98.877430"))
k6 = tuple(map(F, results["6"]["K_oo"]))
gamma = (k6[0]/(4*d6_abs[1]), k6[1]/(4*d6_abs[0]))
certificate = {
    "inputs": INPUTS, "assembly": "L124(1): E+ax-Q+G+R+tr; outside factor 3 once",
    "strict_intervals": True, "results": results,
    "triplet_required_K_oo": "-4 gamma D_3 > 0 by L084; gamma > 0",
    "shear_necessary_gamma_interval": pair_json(gamma),
    "qualification": "Imported certified-input and IEEE assumptions; no independent source audit",
    "failures": failures,
}
path = Path(__file__).with_name("complete-cubic-comparison-certificate.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"triplet exclusion: upper {float(F(results['3']['K_oo'][1])):.3f} < required threshold 0")
print(f"shear compensation requires gamma in ({float(gamma[0]):.6f}, {float(gamma[1]):.6f}); gamma unevaluated")
print(f"failures: {len(failures)}; certificate: {path}")
if failures:
    raise SystemExit(1)
