"""Exact GMP specialization of the saved1816 tail; no new evaluator formulas.

AST-extracted functions and tail preserve the prescribed arithmetic. The sole
tail rewrite reuses the already-completed first outer input. Reported fresh
operations exclude serialization/replay and do not certify a full-run cost.
"""
import ast
import ctypes as C
from collections import Counter
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json
import signal
import subprocess
import sys
import tempfile
import time

import gmp_adapter_slice_1821 as seam

ROOT = Path(__file__).resolve().parent
NOTEBOOK = ROOT.parent.parent
OUT = ROOT / "gmp_remaining_execution_1823a"
RESULT = ROOT / "gmp_remaining_execution_1823a.json"
PREFIX = ROOT / "direct_positive_real_remaining_execution_1816"
B, F = seam.BACKEND, seam.GMPQ
COUNTS = Counter()
TRACK = False
IN_FLIGHT = None


def strict_coerce(x):
    if isinstance(x, F):
        if x.backend is not B:
            raise TypeError("Mixed GMP backend")
        return x
    if isinstance(x, int):
        return F(x)
    raise TypeError("Mixed rational arithmetic: " + type(x).__name__)


def binary(self, other, op):
    global IN_FLIGHT
    other = strict_coerce(other)
    name = next(name for fn,name in [(B.mpq_add,"add"),(B.mpq_sub,"sub"),(B.mpq_mul,"mul"),(B.mpq_div,"div")] if op is fn)
    if name == "div" and other._q.numerator.size == 0:
        raise ZeroDivisionError("Exact zero divisor")
    if TRACK:
        IN_FLIGHT = name
    result = B.binary(op, self, other)
    if TRACK:
        COUNTS[name] += 1
        IN_FLIGHT = None
    return result


def compare(self, other, predicate):
    other = strict_coerce(other)
    result = B.mpq_cmp(C.byref(self._q), C.byref(other._q))
    if TRACK:
        COUNTS["comparison"] += 1
    return predicate(result)


def numeric_hash(self):
    # Python's exact numeric hash; administrative dictionary lookup only.
    n, d = B.parts(self)
    modulus = sys.hash_info.modulus
    value = (abs(n) % modulus) * pow(d, -1, modulus) % modulus if d % modulus else sys.hash_info.inf
    value = -value if n < 0 else value
    return -2 if value == -1 else value


F._coerce = staticmethod(strict_coerce)
F._binary = binary
F.__eq__ = lambda a, b: compare(a, b, lambda c: c == 0)
F.__lt__ = lambda a, b: compare(a, b, lambda c: c < 0)
F.__le__ = lambda a, b: compare(a, b, lambda c: c <= 0)
F.__gt__ = lambda a, b: compare(a, b, lambda c: c > 0)
F.__ge__ = lambda a, b: compare(a, b, lambda c: c >= 0)
F.__hash__ = numeric_hash
F.__neg__ = lambda a: F(0) - a


def abi_check():
    header = Path("/opt/homebrew/include/gmp.h")
    source = '''#include <gmp.h>
#include <stddef.h>
size_t abi_item(int i) { switch(i) {
case 0:return sizeof(__mpz_struct); case 1:return sizeof(__mpq_struct);
case 2:return offsetof(__mpz_struct,_mp_alloc); case 3:return offsetof(__mpz_struct,_mp_size);
case 4:return offsetof(__mpz_struct,_mp_d); case 5:return offsetof(__mpq_struct,_mp_num);
case 6:return offsetof(__mpq_struct,_mp_den); case 7:return sizeof(mp_limb_t)*8;
case 8:return __GNU_MP_VERSION; case 9:return __GNU_MP_VERSION_MINOR;
case 10:return __GNU_MP_VERSION_PATCHLEVEL; default:return 0; }}
const char* linked_version(void) {return gmp_version;}
'''
    source_path = OUT / "abi_probe.c"
    source_path.write_text(source)
    with tempfile.TemporaryDirectory(prefix="riemann-gmp1823-") as directory:
        library = Path(directory) / "probe.dylib"
        command = ["cc", "-dynamiclib", "-I"+str(header.parent), str(source_path), B.library, "-o", str(library)]
        done = subprocess.run(command, capture_output=True, text=True, check=True)
        probe = C.CDLL(str(library))
        probe.abi_item.argtypes, probe.abi_item.restype = [C.c_int], C.c_size_t
        probe.linked_version.restype = C.c_char_p
        actual = [probe.abi_item(i) for i in range(11)]
        expected = [C.sizeof(seam.MPZ), C.sizeof(seam.MPQ), seam.MPZ.allocated.offset,
                    seam.MPZ.size.offset, seam.MPZ.limbs.offset, seam.MPQ.numerator.offset,
                    seam.MPQ.denominator.offset, C.sizeof(C.c_ulong)*8]
        version = C.c_char_p.in_dll(B.lib, "__gmp_version").value.decode()
        assert actual[:8] == expected
        assert version == probe.linked_version().decode() == ".".join(map(str, actual[8:]))
        linked = subprocess.run(["otool", "-L", str(library)], capture_output=True, text=True, check=True).stdout
    return {"passed": True, "header": str(header), "header_sha256": digest(header),
            "library": B.library, "library_sha256": digest(Path(B.library)), "version": version,
            "sizes_offsets_limb_bits": actual[:8], "compiler_command": command,
            "compiler_stderr": done.stderr, "linked_objects": linked,
            "scope": "Generated header, compiled probe and ctypes layout/version agree; exact arithmetic replay remains required"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract(path, names, namespace):
    tree = ast.parse(path.read_text(), filename=str(path))
    nodes = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
    assert {n.name for n in nodes} == set(names)
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), "exec"), namespace)


def tail_code():
    path = ROOT / "direct_positive_real_remaining_execution_1816.py"
    tree = ast.parse(path.read_text())
    main = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "main")
    attempt = next(n for n in main.body if isinstance(n, ast.Try))
    start = next(i for i,n in enumerate(attempt.body) if isinstance(n,ast.Assign)
                 and isinstance(n.targets[0],ast.Name) and n.targets[0].id == "r13")
    tail = attempt.body[start:]
    original = ast.dump(ast.Module(body=tail, type_ignores=[]), include_attributes=False)
    class ReuseFirst(ast.NodeTransformer):
        replacements = 0
        def visit_For(self, node):
            self.generic_visit(node)
            if isinstance(node.target,ast.Tuple) and [getattr(n,"id",None) for n in node.target.elts] == ["j","root"]:
                # Only replace v,E,t,r assignments with their saved identical values
                # for panel0/node0. All later assignments are byte-for-byte ASTs.
                assert [n.targets[0].id for n in node.body[1:5]] == ["v","E","t","r"]
                load = ast.parse('saved = load(PREFIX / "outer_inputs_000.json")\nv,E,t,r = [saved[k] for k in ("v","E","t","r")]').body
                condition = ast.parse("panel == 0 and j == 0", mode="eval").body
                node.body[1:5] = [ast.If(test=condition, body=load, orelse=node.body[1:5])]
                self.replacements += 1
            return node
    transformer = ReuseFirst()
    module = transformer.visit(ast.Module(body=tail, type_ignores=[]))
    assert transformer.replacements == 1
    ast.fix_missing_locations(module)
    return compile(module, str(path)+":GMP_tail", "exec"), hashlib.sha256(original.encode()).hexdigest()


def main():
    global TRACK
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=int, default=300)
    args = parser.parse_args()
    if OUT.exists() or RESULT.exists():
        raise SystemExit("Preserve evidence: refuses to overwrite1823")
    OUT.mkdir()
    started = time.monotonic()
    namespace = {"F": F, "json": json}
    extract(ROOT/"direct_positive_real_execution_1808.py",
            {"rational","encode","write_json","bits","horner","power2","clamp"}, namespace)
    extract(ROOT/"direct_positive_real_execution_remaining_1808.py",
            {"decode","inverse_root","atanh_series","quotient"}, namespace)
    write_json, decode = namespace["write_json"], namespace["decode"]
    report = {"status":"INITIALIZING_GMP_TAIL", "assessment":"drafts/literature/2026-11-19-direct-positive-real-gmp-execution-review-1816.md",
              "artifacts":[], "inputs_sha256":{}, "failures":[], "profiles_evaluated":0,
              "scalars_evaluated":0, "required_scalar_radius":"1/256", "required_operation_cap":1000000,
              "inherited_full_operation_upper":997104, "actual_complete_operation_count_verified":False,
              "reserved_exponent_allowance":"1/1024", "reserved_final_exponential_allowance":"1/1024",
              "arithmetic":"Exact GMP mpq throughout tail/helpers/encoder; only reused Ihat is rounded",
              "time_limit_seconds":args.seconds, "pending":"ABI and saved-prefix lineage",
              "limitations":["No scalar, radius, full executed-cost or runtime theorem from a partial run",
                             "Reused constructor costs remain in the inherited ledger; fresh operator counts exclude validation/I/O/hash/serialization",
                             "No source-wide validity, interpolation, TV or Xi positivity claim"]}

    def checkpoint():
        global TRACK
        previous, TRACK = TRACK, False
        try:
            report.update(elapsed_seconds=round(time.monotonic()-started,3), fresh_completed_operations=dict(COUNTS),
                          fresh_completed_operation_total=sum(COUNTS.values()), interrupted_operation=IN_FLIGHT)
            write_json(RESULT,report)
        finally:
            TRACK = previous

    def load(path):
        raw = path.read_bytes()
        report["inputs_sha256"][str(path.relative_to(NOTEBOOK))] = hashlib.sha256(raw).hexdigest()
        return decode(json.loads(raw))

    def pending(value):
        report["pending"] = value
        checkpoint()

    def save(name,value):
        global TRACK
        previous, TRACK = TRACK, False
        try:
            path = OUT/(name+".json")
            write_json(path,value)
            report["artifacts"].append({"path":str(path.relative_to(NOTEBOOK)), "bytes":path.stat().st_size,
                                        "sha256":digest(path), "operations_completed":sum(COUNTS.values())})
            report["last_completed_artifact"] = str(path.relative_to(NOTEBOOK))
            checkpoint()
        finally:
            TRACK = previous

    class Deadline(Exception):
        pass
    def timeout(_signum,_frame):
        raise Deadline()

    checkpoint()
    try:
        report["abi"] = abi_check()
        prefix_run = load(ROOT/"direct_positive_real_remaining_execution_1816.json")
        for filename,status in [("direct_positive_real_remaining_replay_1816.json","PASS_COMPLETE_SAVED_PREFIX_ONLY"),
                                ("direct_positive_real_remaining_lineage_1816.json","PASS_LINEAGE_ONLY")]:
            certificate = load(ROOT/filename)
            assert certificate["status"] == status and not certificate["failures"]
            for path,sha in certificate["inputs_sha256"].items():
                assert digest(NOTEBOOK/path) == sha
        for item in prefix_run["artifacts"]:
            assert digest(NOTEBOOK/item["path"]) == item["sha256"]
        assert prefix_run["profiles_evaluated"] == prefix_run["scalars_evaluated"] == 0
        constants = load(PREFIX/"constants.json")
        prime = load(PREFIX/"prime_constants.json")
        core = load(PREFIX/"shared_core.json")
        namespace.update(constants)
        namespace.update({"logs":{int(k):v for k,v in prime["logs"].items()},
                          "prime_coeff":{int(k):v for k,v in prime["coefficients"].items()},
                          "log_squares":{int(k):v for k,v in prime["log_squares"].items()},
                          "schedules":prime["schedules"], "fixed":core["fixed"], "d":core["d"]})
        def read(name):
            return load(ROOT/"direct_positive_real_execution_1808"/(name+".json"))
        inner_data = read("inner_nodes")
        namespace.update(inner=inner_data["nodes_and_weights"], tcoeff=inner_data["taylor_coefficients_ascending"],
                         a=read("moment_inputs")["a"],
                         ecoeff=[F(1,2**k*factorial(k)) for k in range(1,17)],
                         ucoeff=[F(1,factorial(2*j+1)) for j in range(1,11)],
                         read=read, load=load, save=save, pending=pending, report=report, PREFIX=PREFIX)
        code, ast_sha = tail_code()
        report["original_tail_ast_sha256"] = ast_sha
        report["source_sha256"] = {str(p.relative_to(NOTEBOOK)):digest(p) for p in
            [Path(__file__),ROOT/"gmp_adapter_slice_1821.py",ROOT/"direct_positive_real_remaining_execution_1816.py",
             ROOT/"direct_positive_real_execution_1808.py",ROOT/"direct_positive_real_execution_remaining_1808.py"]}
        report["prefix_lineage_passed"] = True
        report["status"] = "RUNNING_GMP_EXACT_TAIL"
        signal.signal(signal.SIGALRM,timeout)
        signal.alarm(args.seconds)
        checkpoint()
        TRACK = True
        exec(code,namespace)
    except Deadline:
        signal.alarm(0)
        report["status"] = "TIME_LIMIT_GMP_EXACT_TAIL_INCOMPLETE"
        report["failures"].append("Operational limit; complete radii/cap not established")
    except Exception as exc:
        signal.alarm(0)
        report["status"] = "GMP_EXECUTION_ERROR_INCOMPLETE"
        report["failures"].append(f"{type(exc).__name__}: {exc}")
        raise
    finally:
        TRACK = False
        signal.alarm(0)
        checkpoint()
        print(f"{report['status']}; profiles {report['profiles_evaluated']}/780; scalars {report['scalars_evaluated']}/8")
        print(f"Fresh completed operations {sum(COUNTS.values())}; inherited upper997104; required full cap<=1000000 remains unverified")
        print(f"All eight radii<1/256 and both1/1024 allowances NOT ESTABLISHED; pending: {report['pending']}")
        print(f"Failures: {report['failures']}; certificate: {RESULT.relative_to(NOTEBOOK)}")


if __name__ == "__main__":
    main()
