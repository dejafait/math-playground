"""Independent exact replay of completed1823a artifacts, no evaluator import.

Uses Python integers/Fraction, with the saved GMP gcd-only verifier bridge.
Direct Taylor/power and common-denominator identities replace GMP Horner.
Complete prefix/lineage certificates are rebound, never inferred from previews.
"""
from fractions import Fraction as Q
from math import factorial, lcm
from pathlib import Path
import hashlib
import json
import signal
import time

from direct_positive_real_ihat_integer_backend_1814 import enable
from direct_positive_real_remaining_replay_1816 import (
    decode, polynomial, taylor_power_matches, root_cell,
)

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parent.parent
INDEX = HERE/"gmp_remaining_execution_1823a.json"
DATA = HERE/"gmp_remaining_execution_1823a"
PREFIX = HERE/"direct_positive_real_remaining_execution_1816"
OLD = HERE/"direct_positive_real_execution_1808"
OUT = HERE/"gmp_remaining_replay_1823.json"


def atanh_matches(z, count, expected):
    n,d = z.numerator,z.denominator
    degree = 2*count-1
    common = lcm(*(2*j+1 for j in range(count)))
    den = common*d**degree
    num = sum(2*(common//(2*j+1))*n**(2*j+1)*d**(degree-2*j-1) for j in range(count))
    return num*expected.denominator == expected.numerator*den


def main():
    if OUT.exists():
        raise SystemExit("Preserve replay1823")
    started = time.monotonic()
    checks, hashes = {}, {}
    report = {"status":"REPLAY_IN_PROGRESS", "checks":checks, "artifacts_replayed":[],
              "profiles_replayed":0, "scalars_certified":0, "full_evaluator_count_verified":False,
              "pending":"prefix/lineage", "backend":enable(),
              "limitations":["Saved partial execution only; no absent scalar, radius or full count is inferred",
                             "Arithmetic replay is distinct from source-wide/zero-data validity and actual-Xi positivity"]}
    def digest(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()
    def load(path):
        raw = path.read_bytes()
        hashes[str(path.relative_to(NOTEBOOK))] = hashlib.sha256(raw).hexdigest()
        return decode(json.loads(raw))
    def check(name,condition):
        checks[name] = bool(condition)
        if not condition:
            raise ArithmeticError("Failed: "+name)
    def checkpoint():
        report.update(check_count=len(checks), inputs_sha256=hashes,
                      failures=[k for k,v in checks.items() if not v],
                      elapsed_seconds=round(time.monotonic()-started,3))
        temporary = OUT.with_suffix(".tmp")
        temporary.write_text(json.dumps(report,indent=2)+"\n")
        temporary.replace(OUT)
    def pending(value):
        report["pending"] = value
        checkpoint()
    class Limit(Exception):
        pass
    def timeout(_s,_f):
        raise Limit()
    signal.signal(signal.SIGALRM,timeout)
    signal.alarm(300)
    try:
        run = load(INDEX)
        check("execution_stopped", not run["status"].startswith("RUNNING"))
        for path,sha in run["inputs_sha256"].items():
            check("input_hash:"+path,digest(NOTEBOOK/path)==sha)
        for path,sha in run["source_sha256"].items():
            check("source_hash:"+path,digest(NOTEBOOK/path)==sha)
        check("compiled_ABI_passed",run["abi"]["passed"] and run["abi"]["version"]=="6.3.0")
        check("installed_header_unchanged",digest(Path(run["abi"]["header"]))==run["abi"]["header_sha256"])
        check("installed_library_unchanged",digest(Path(run["abi"]["library"]))==run["abi"]["library_sha256"])
        for filename,status in [("direct_positive_real_remaining_replay_1816.json","PASS_COMPLETE_SAVED_PREFIX_ONLY"),
                                ("direct_positive_real_remaining_lineage_1816.json","PASS_LINEAGE_ONLY")]:
            previous = load(HERE/filename)
            check("prior_status:"+filename,previous["status"]==status and not previous["failures"])
            for path,sha in previous["inputs_sha256"].items():
                check("prior_hash:"+filename+":"+path,digest(NOTEBOOK/path)==sha)
        for item in run["artifacts"]:
            check("artifact_hash:"+item["path"],digest(NOTEBOOK/item["path"])==item["sha256"])
        constants = load(PREFIX/"constants.json")
        ell,pi,p,K = [constants[k] for k in ("ell","pi","p","K")]
        prime = load(PREFIX/"prime_constants.json")
        core = load(PREFIX/"shared_core.json")
        rule = load(OLD/"reference_rules.json")["rules"][1]
        nodes = load(OLD/"inner_nodes.json")["nodes_and_weights"]
        aa = load(OLD/"moment_inputs.json")["a"]
        for path in sorted(DATA.glob("outer_inputs_*.json")):
            pending(path.name)
            inp = load(path)
            panel,j = inp["panel"],inp["node"]
            index = 13*panel+j
            if index == 0:
                check("first_outer_input_reuse",inp==load(PREFIX/"outer_inputs_000.json"))
            else:
                v = max(Q(0),min(Q(21),ell*(30-Q(7*panel,5)-Q(7,10)*(1+rule["nodes"][j]))))
                check(f"input{index}:v",inp["v"]==v)
                check(f"input{index}:E",taylor_power_matches(v/32,40,5,inp["E"]))
                check(f"input{index}:t",inp["t"]==max(Q(0),min(Q(1,4),1/inp["E"])))
                check(f"input{index}:r",taylor_power_matches(v/64,20,5,inp["r"]))
            report["artifacts_replayed"].append(path.name)
            factors_path = DATA/f"outer_factors_{index:03d}.json"
            if factors_path.exists():
                factors = load(factors_path)
                weight = Q(7,10)*ell*max(Q(0),min(Q(2),rule["weights"][j]))
                for s in (1,2):
                    pending(f"factor{index}:g{s} integer Taylor identity")
                    u = 1-factors["g"][str(s)]/(p*inp["r"])
                    check(f"factor{index}:g{s}",taylor_power_matches(-s*inp["t"],20,0,u,True))
                    check(f"factor{index}:weighted_g{s}",factors["weighted_g"][str(s)]==weight*factors["g"][str(s)])
                report["artifacts_replayed"].append(factors_path.name)
            for cpath in sorted(DATA.glob(f"core_{index:03d}_*.json")):
                pending(cpath.name)
                sigma = Q(cpath.stem.split("_",2)[2].replace("_","/"))
                value = load(cpath)
                w,q,J = [value[k] for k in ("w","q","J")]
                check(cpath.name+":w",w==sigma+inp["E"]/4)
                check(cpath.name+":inverse_root_cell",root_cell(w,q,Q(0),Q(1)))
                check(cpath.name+":q_clamp",0<=q<=(Q(1,4) if panel<17 else Q(1)))
                if panel<17:
                    expected = q*polynomial(core["d"],4*q)
                else:
                    expected = q*sum((aj*(polynomial([Q(1,2**k*factorial(k)) for k in range(1,17)],x*q)
                        -sum(((x*q)**(2*k-1)/factorial(2*k+1) for k in range(1,11)),Q(0)))
                        /(2*(1+x*q*sum(((x*q)**(2*k-1)/factorial(2*k+1) for k in range(1,11)),Q(0))))
                        for (x,_),aj in zip(nodes,aa)),Q(0))
                check(cpath.name+":J",J==expected)
                report["artifacts_replayed"].append(cpath.name)
                suffix = cpath.stem.removeprefix("core_")
                lpath = DATA/("logprime_"+suffix+".json")
                if lpath.exists():
                    pending(lpath.name)
                    lp = load(lpath)
                    check(lpath.name+":D",lp["D"]==J-core["fixed"])
                    selected = next(row["retained"] for row in prime["schedules"] if row["panel"]==panel and row["sigma"]==sigma)
                    psum = Q(0)
                    for n in selected:
                        arg = w*prime["log_squares"][str(n)]
                        if arg<32:
                            u = polynomial([Q(1,factorial(k)) for k in range(21)],-arg/32)
                            psum += prime["coefficients"][str(n)]*max(Q(0),min(Q(1),u))**32
                    check(lpath.name+":prime_sum",lp["prime_sum"]==psum)
                    x = 4*sigma*inp["t"]
                    check(lpath.name+":logw",atanh_matches(x/(2+x),16,lp["logw"]-inp["v"]+2*ell))
                    report["artifacts_replayed"].append(lpath.name)
                checkpoint()
            checkpoint()
        all_artifacts = {Path(item["path"]).name for item in run["artifacts"]}
        check("complete_new_artifact_coverage",all_artifacts==set(report["artifacts_replayed"]))
        check("no_absent_scalar_claim",run["profiles_evaluated"]==run["scalars_evaluated"]==0)
        report["status"] = "PASS_COMPLETE_SAVED_GMP_PREFIX_ONLY"
        report["pending"] = "Complete profiles/scalars/radii/full-cost absent"
    except Limit:
        report["status"] = "TIME_LIMIT_PARTIAL_GMP_PREFIX_REPLAY"
    except Exception as exc:
        report["status"] = "REPLAY_ERROR_INCOMPLETE"
        report["error"] = f"{type(exc).__name__}: {exc}"
        raise
    finally:
        signal.alarm(0)
        checkpoint()
        print(f"{report['status']}; checks {len(checks)}; failures {report['failures']}; replayed artifacts {len(report['artifacts_replayed'])}")
        print(f"Scalars certified0/8; radii<1/256/full cap<=1000000 NOT ESTABLISHED; {OUT.relative_to(NOTEBOOK)}")


if __name__ == "__main__":
    main()
