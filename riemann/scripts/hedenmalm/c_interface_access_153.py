"""Bounded access probe only; does not certify any mathematical value."""
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "scripts/hedenmalm/c-interface-access-153.json"
WORK = ROOT / "scripts/hedenmalm/c-interface-probe-153"
WORK.mkdir(exist_ok=True)


def run(args):
    try:
        result = subprocess.run(args, text=True, capture_output=True, timeout=25)
        return dict(argv=args, exit_code=result.returncode,
                    stdout=result.stdout, stderr=result.stderr)
    except subprocess.TimeoutExpired as exc:
        return dict(argv=args, timeout_seconds=25,
                    stdout=str(exc.stdout or ""), stderr=str(exc.stderr or ""))


source = WORK / "probe.c"
source.write_text(
    '#include <acb.h>\n#include <acb_dirichlet.h>\n'
    'int main(void) { acb_t z; acb_init(z); acb_clear(z); return 0; }\n'
)
compile_result = run([
    "/usr/bin/clang", "-I/opt/homebrew/include",
    "-I/opt/homebrew/include/flint", "-L/opt/homebrew/lib",
    str(source), "-larb", "-lflint", "-lmpfr", "-lgmp",
    "-o", str(WORK / "probe"),
])
# No system installation. This is the only alternate source-access route.
download_result = run([
    "/usr/bin/curl", "--fail", "--location", "--connect-timeout", "5",
    "--max-time", "20", "--output", str(WORK / "arb-2.23.0.tar.gz"),
    "https://github.com/fredrik-johansson/arb/archive/refs/tags/2.23.0.tar.gz",
])
cert = dict(
    purpose="Certified C-interface access prerequisite, not a root or Gram certificate",
    compile=compile_result, source_download=download_result,
    numerical_precision_passes=0, root_certificate=False, gram_certificate=False,
    required="Working rigorous indexed-zero and ball integration implementation before a 128-bit pass",
    mathematical_conclusion="None; no claim about the Gram entry or RH",
)
OUT.write_text(json.dumps(cert, indent=2) + "\n")
print("C compile exit:", compile_result.get("exit_code", "timeout"))
print("Frozen Arb source download exit:", download_result.get("exit_code", "timeout"))
print("Actual: no numerical pass; required: certified indexed roots and complete Gram enclosure")
print("Full command evidence:", OUT.relative_to(ROOT))
