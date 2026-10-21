#!/usr/bin/env python3
"""Bounded altered-evidence tests; retain copies and preserve original bytes."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parent

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    original=[ROOT/n for n in ["certificate.json","build_certificate.py","verify_certificate.py","producer-draft-v0.json"]]
    before={p.name:digest(p) for p in original}
    base=json.loads((ROOT/"certificate.json").read_text())
    dest=ROOT/"rejections";dest.mkdir(exist_ok=True)
    results=[]
    for name,expected in [("corrupted-psi7","psi7_odd_recurrence"),("missing-X-map","required_fields")]:
        copy=json.loads(json.dumps(base))
        if name=="corrupted-psi7":
            from fractions import Fraction
            copy["psi7"][0]=str(Fraction(copy["psi7"][0])+1)
        else:del copy["X_of_t"]
        source=dest/(name+".json");report=dest/(name+"-report.json")
        source.write_text(json.dumps(copy,separators=(",",":"))+"\n")
        result=subprocess.run([sys.executable,str(ROOT/"verify_certificate.py"),"--certificate",str(source),"--report",str(report)],capture_output=True,text=True)
        outcome=json.loads(report.read_text())
        ok=result.returncode==1 and outcome["status"]=="REJECTED" and outcome["failure"]==expected
        results.append({"case":name,"expected_failure":expected,"actual_failure":outcome.get("failure"),"pass":ok,"report":str(report.relative_to(ROOT))})
        if not ok:raise RuntimeError(result.stdout+result.stderr)
    # Preserve the initial producer mistake as explicitly INVALID evidence.
    draft=json.loads((ROOT/"producer-draft-v0.json").read_text())
    assert len(draft["h"])-1==47
    after={p.name:digest(p) for p in original}
    assert before==after
    output={"status":"PASS","cases":results,"original_bytes_preserved":True,
            "original_sha256":before,"invalid_draft":{"path":"producer-draft-v0.json","actual_degree":47,"required_degree":48,"reason":"trimmed zero t^47 slot before appending monic coefficient; superseded, never verified"}}
    (ROOT/"rejection-verification.json").write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps({"status":"PASS","intended_rejections":len(results),"required_rejections":2,"original_bytes_preserved":True,"report":str(ROOT/"rejection-verification.json")}))

if __name__=="__main__":main()
