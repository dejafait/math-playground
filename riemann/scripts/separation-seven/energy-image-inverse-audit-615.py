#!/usr/bin/env python3
"""Audit C999t's fixed certificate, without changing any input or proposal.

All complete dyadic products below use Python integers. The analytic input
and exact-neutral conversion remain the qualified C999k/l audited inputs.
No solve, eigensolver, Cholesky, parameter search or covariance replay.
"""
from fractions import Fraction as F
from math import lcm
from pathlib import Path
import hashlib
import json
import numpy as np

BASE = Path(__file__).resolve().parent
checks, failures, evidence, pins = [], [], {}, {}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(name, actual, op, required):
    passed = {"<": lambda: actual < required, "==": lambda: actual == required,
              ">": lambda: actual > required}[op]()
    checks.append(dict(name=name, actual=str(actual), relation=op,
                       required=str(required), passed=bool(passed)))
    if not passed:
        failures.append(name)


def dyadic(a):
    ratios = [float(x).as_integer_ratio() for x in a.flat]
    den = max((d for _, d in ratios), default=1)
    return np.array([n*(den//d) for n, d in ratios], dtype=object).reshape(a.shape), den


def add(a, b, sign=1):
    den = lcm(a[1], b[1])
    return a[0]*(den//a[1])+sign*b[0]*(den//b[1]), den


def scale(a, q):
    q = F(q)
    return a[0]*q.numerator, a[1]*q.denominator


def product(a, b):
    # dtype=object with Python int operands: no floating contraction.
    return a[0]@b[0], a[1]*b[1]


def trans(a):
    return a[0].T, a[1]


def sym(a):
    return a[0]+a[0].T, 2*a[1]


def squared(a):
    return F(sum(int(x)**2 for x in a[0].flat), a[1]**2)


def bound(name, a, required):
    value = squared(a)
    evidence[name] = dict(exact_squared_frobenius=str(value),
                          required_norm=str(required), shape=list(a[0].shape))
    check(name, value, "<", F(required)**2)
    # The summary is diagnostic; the saved rational comparison is decisive.
    print(name+":", float(value)**.5, "<", float(required), flush=True)
    return value


def read_json(name):
    pins[name] = digest(BASE/name)
    return json.loads((BASE/name).read_text())


original = read_json("energy-image-inverse-613.json")
audit561 = read_json("neutral-head-covariance-audit-561.json")
audit557 = read_json("fixed-block-metric-audit-557.json")
check("original failures", original["failures"], "==", [])
check("audit561 failures (qualified import)", audit561["failures"], "==", [])
check("audit557 failures (qualified import)", audit557["failures"], "==", [])
check("original complete check count", len(original["checks"]), "==", 43)
check("original all check flags", all(c["passed"] for c in original["checks"]), "==", True)
for name, expected in original["input_hashes"].items():
    pins[name] = digest(BASE/name)
    check("original pin "+name, pins[name], "==", expected)
for name in ("neutral-head-covariance-559.npz", "neutral-head-covariance-559.json",
             "complete-covariance-532.npz", "fixed-block-metric-audit-557.json"):
    check("audit561 pin "+name, pins[name], "==", audit561["original_hashes"][name])
for name, key in (("energy-image-inverse-613.npz", "arrays_sha256"),
                  ("energy-image-inverse-613.py", "source_script_sha256")):
    pins[name] = digest(BASE/name)
    check("saved proposal pin "+name, pins[name], "==", original[key])

with np.load(BASE/"energy-image-inverse-613.npz", allow_pickle=False) as data:
    arrays = {k: data[k] for k in data.files}
with np.load(BASE/"neutral-head-covariance-559.npz", allow_pickle=False) as data:
    for name in ("z", "a"):
        check("full inherited array "+name, np.array_equal(arrays[name], data[name]), "==", True)
with np.load(BASE/"complete-covariance-532.npz", allow_pickle=False) as data:
    arrays["m"], arrays["cov"] = data["m0"], data["cov00"]
expected_shapes = dict(z=(512,510), a=(510,510), h=(512,512), g=(510,510),
    x=(512,510), y=(510,510), head_inverse_remainder=(510,510),
    residual_H=(512,510), residual_A=(510,510), trial=(510,510),
    factor=(510,510), factor_reconstruction=(510,510), m=(512,512), cov=(512,512))
for name, shape in expected_shapes.items():
    check("shape "+name, arrays[name].shape, "==", shape)
    check("finite real binary64 "+name,
          arrays[name].dtype == np.dtype("float64") and bool(np.isfinite(arrays[name]).all()), "==", True)
for name in ("m", "cov", "h", "g", "head_inverse_remainder", "trial"):
    check("exact symmetry "+name, np.array_equal(arrays[name], arrays[name].T), "==", True)
check("Z free block is identity", np.array_equal(arrays["z"][2:], np.eye(510)), "==", True)
for p in (0, 1):
    check("Z parity zeros "+str(p), bool(np.all(arrays["z"][p, (1-p)::2] == 0)), "==", True)

d = {name: dyadic(a) for name, a in arrays.items()}
limits = dict(m=400, cov=1, z=23, a=500, h=500, g=100, x=100, y=100,
              head_inverse_remainder=20000, trial=20001, factor=300,
              residual_H=F(1,10**7), residual_A=F(1,10**7),
              factor_reconstruction=F(1,10**7))
for name, limit in limits.items():
    bound("complete stored magnitude "+name, d[name], limit)

# Exact rational reference assembly, with no floating scalar conversion.
identity512 = (np.eye(512, dtype=object), 1)
identity510 = (np.eye(510, dtype=object), 1)
h_exact = add(add(d["m"], scale(d["cov"], F(100,307)), -1),
              scale(identity512, F(6671,307*12500)), -1)
bound("exact H assembly error", add(h_exact,d["h"],-1), F(1,10**8))
del h_exact

# Full exact Gram, both solve residuals, subtraction, and reconstruction.
gram = product(trans(d["z"]),d["z"])
bound("exact Gram assembly error", add(gram,d["g"],-1), F(1,10**7))
del gram
bound("exact H solve residual", add(product(d["h"],d["x"]),d["z"],-1), F(1,10**6))
bound("exact A solve residual", add(product(d["a"],d["y"]),d["g"],-1), F(1,10**6))
zx = product(trans(d["z"]),d["x"])
gy = product(d["g"],d["y"])
bound("exact Zhat transpose X magnitude",zx,2301)
bound("exact Ghat Y magnitude",gy,10001)
b_exact = sym(add(zx,gy,-1))
bound("exact B assembly error",add(b_exact,d["head_inverse_remainder"],-1),F(1,10**7))
del zx, gy, b_exact
trial_exact = add(add(scale(d["g"],F(99,100)),d["head_inverse_remainder"],-1),
                  scale(identity510,F(1,20)),-1)
bound("exact trial assembly error",add(trial_exact,d["trial"],-1),F(1,10**7))
del trial_exact
bound("exact full factor reconstruction",add(d["trial"],product(d["factor"],trans(d["factor"])), -1),F(1,10**6))

# Independently recompute every scalar allowance in the original proof.
u, gamma = F(1,2**53), F(1,2**43-1)
dz, dh, dg = F(1,10**14), F(1,10**8), F(1,10**7)
eta = F(".00024")*F("1.008")**2+F(1,10**7)
check("qualified exact basis conversion",F(audit561["evidence"]["basis_conversion"]["hi"]),"<",dz)
for side in ("lo","hi"):
    check("qualified eta_A "+side,F(audit561["evidence"]["integer_scalar_bounds"]["head_form_error"][side]),"==",eta)
ledger = {
    "H assembly": (50*u*500, dh),
    "solve product and subtraction": (gamma*500*100+u*(500*100+100+1), F(1,10**7)),
    "solve total": (F(1,10**7)+gamma*500*100+u*(500*100+100+1), F(1,10**6)),
    "Gram total including exact-neutral conversion": (gamma*23**2+dz*(2*F("1.009")+dz), dg),
    "B products subtraction and symmetrization": (gamma*(23*100+100*100)+10*u*50000,F(1,10**7)),
    "factor product and subtraction total": (F(1,10**7)+gamma*100000+10*u*50000,F(1,10**6)),
    "trial conversion and assembly": (10*u*50000,F(1,10**7)),
}
for name,(actual,required) in ledger.items():
    check("original ledger "+name,actual,"<",required)
evidence["rounding_ledger"] = {k:dict(actual=str(v[0]),required=str(v[1])) for k,v in ledger.items()}
ex = (F(1,10**6)+100*dh+dz)/F(".239999")
ey = (F(1,10**6)+100*eta+dg)/F(".779")
eb = 100*dz+F("1.008")*ex+100*dg+F("1.008")**2*ey+F(1,10**7)
slack = F(".05")-F(1,10**6)-F(1,10**7)-F(".99")*dg-eb
check("exact claimed e_B",eb,"==",F(5952684418352310837,186959221000000000000))
check("exact claimed finite slack",slack,"==",F(3395052467541710163,186959221000000000000))
check("finite slack threshold",slack,">",F(".01815"))
check("reference inverse norm bound",1/F(".239999"),"<",F(5))
tailmoment = F(4,3*511**3)
check("entire parity moment tail",tailmoment,"<",F(1,10**8))
head = F(99,100)+F(5,10000)
tail = F(100,307)+F(5,10000)+F(5,10**8)
check("exact tail coefficient",tail,"==",F(2003070307,6140000000))
check("tail coefficient below head",tail,"<",head)
check("head bound unchanged",head,"==",F(1981,2000))
check("threshold one",head,"<",F(1))
evidence["analytic_scalar_bounds"] = {k:str(v) for k,v in dict(eta_A=eta,e_X=ex,e_Y=ey,e_B=eb,
    finite_slack=slack,entire_moment_tail_squared=tailmoment,head=head,tail=tail).items()}
for name, old in pins.items():
    check("input preserved "+name,digest(BASE/name),"==",old)
out = dict(scope="C999t fixed conceptual audit615; complete exact integer finite products",
    source_script_sha256=digest(Path(__file__)),input_hashes=pins,checks=checks,
    evidence=evidence,failures=failures,
    summary=dict(passed=not failures,check_count=len(checks),finite_slack=str(slack),
                 squared_norm_upper=str(head),required_upper="1"),
    qualifications=["C999k/l/s and audits557/561/611 remain qualified inputs.",
       "No validation of analytic response, original core or c_star source.",
       "Exact finite integer checks do not remove inherited IEEE754/Decimal contracts.",
       "Full projection and infinite-neutral argument is in C999t Section7."])
path = BASE/"energy-image-inverse-audit-615.json"
path.write_text(json.dumps(out,indent=2)+"\n")
print("Checks:",len(checks),"failures:",failures)
print("Finite slack:",float(slack),"> .01815; squared norm:",head,"< 1")
print("Certificate:",path.relative_to(BASE.parent.parent))
if failures:
    raise SystemExit(1)
