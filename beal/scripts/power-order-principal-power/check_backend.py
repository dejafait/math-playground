"""Bounded, read-only preflight for the approved principal-power test.

No arithmetic search is performed by this diagnostic. Full results are
written next to the script; failed imports are not mathematical evidence.
"""
import json
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
EXPONENTS = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12]
PATHS = [
    Path(sys.executable), ROOT / ".venv/bin/python",
    ROOT.parent / ".venv/bin/python",
    Path("/opt/homebrew/bin/python3"),
    Path("/opt/homebrew/bin/python3.13"),
    Path("/opt/homebrew/bin/python3.12"),
    Path("/opt/homebrew/bin/python3.11"),
    Path("/usr/local/bin/python3"), Path("/usr/bin/python3"),
]
PROBE = """import json, sys
import sympy
from sympy.polys.matrices import DomainMatrix
from sympy.matrices.normalforms import hermite_normal_form
print(json.dumps({'python': sys.executable, 'version': sys.version,
    'sympy_version': sympy.__version__,
    'lll_transform_callable': callable(DomainMatrix.lll_transform),
    'hnf_callable': callable(hermite_normal_form)}))
"""


def main():
    probes = []
    for path in dict.fromkeys(PATHS):
        if not path.is_file():
            probes.append({"path": str(path), "exists": False})
            continue
        result = subprocess.run([str(path), "-c", PROBE],
                                capture_output=True, text=True, timeout=20)
        probes.append({"path": str(path), "exists": True,
                       "returncode": result.returncode,
                       "stdout": result.stdout, "stderr": result.stderr})
    ready = [p for p in probes if p.get("returncode") == 0]
    data = {
        "status": "BACKEND_AVAILABLE" if ready else "BLOCKED_BEFORE_ARITHMETIC",
        "probes": probes,
        "other_backend_paths": {name: shutil.which(name) for name in ["gp", "sage"]},
        "approved_exponents": EXPONENTS,
        "maximum_candidates_per_exponent": 144,
        "maximum_candidates": 144 * len(EXPONENTS),
        "actual_candidates": 0,
        "required_rank": 12,
        "actual_ranks": None,
        "stability": "NOT_RUN", "compression_checks": "NOT_RUN",
        "principal_power_equalities": "NOT_RUN", "L058_identity": "NOT_RUN",
        "candidate_rejections": 0,
        "mathematical_conclusion": "NONE",
        "failures": [] if ready else ["No probed interpreter imports the documented SymPy backend"],
    }
    out = Path(__file__).with_name("backend-certificate.json")
    out.write_text(json.dumps(data, indent=2) + "\n")
    print(data["status"])
    print("Candidates: 0 / maximum 1440; rank: NOT_RUN / required 12")
    print("Stability, compression and identities: NOT_RUN")
    print("Failures:", data["failures"])
    print("Certificate:", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
