#!/usr/bin/env python3
"""Fixed inverse Galerkin comparison; approved assessment611/review612.

Propose two finite solves and one factor; verify complete residuals and
exact dyadic Frobenius magnitudes. Import qualified C999k/l contracts.
No parameter search, reference change, or large covariance replay.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
checks, failures, values, pins = [], [], {}, {}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(name, actual, relation, required):
    ok = {"<": lambda: actual < required, ">": lambda: actual > required,
          "==": lambda: actual == required}[relation]()
    checks.append(dict(name=name, actual=str(actual), relation=relation,
                       required=str(required), passed=bool(ok)))
    if not ok:
        failures.append(name)


def fro2(a):
    """Exact squared Frobenius norm of the full stored dyadic array."""
    terms = [float(x).as_integer_ratio() for x in a.flat]
    exponent = max((d.bit_length()-1 for _, d in terms), default=0)
    total = sum(n*n << (2*(exponent-(d.bit_length()-1))) for n, d in terms)
    return F(total, 1 << (2*exponent))


def magnitude(name, a, bound):
    q = fro2(a)
    values[name+"_fro_squared"] = str(q)
    check(name+" complete Frobenius bound squared", q, "<", F(bound)**2)


audit = json.loads((BASE/"neutral-head-covariance-audit-561.json").read_text())
check("audit561 failures", audit["failures"], "==", [])
for name in ["neutral-head-covariance-559.npz", "neutral-head-covariance-559.json",
             "complete-covariance-532.npz", "fixed-block-metric-audit-557.json"]:
    pins[name] = sha(BASE/name)
    check("audit561 input pin "+name, pins[name], "==", audit["original_hashes"][name])
reference_audit = json.loads((BASE/"fixed-block-metric-audit-557.json").read_text())
check("audit557 failures", reference_audit["failures"], "==", [])
pins["neutral-head-covariance-audit-561.json"] = sha(BASE/"neutral-head-covariance-audit-561.json")
evidence = audit["evidence"]
check("imported complete Z conversion", F(evidence["basis_conversion"]["hi"]), "<", F(1,10**14))
eta = F(".00024")*F("1.008")**2+F(".0000001")
for end in ("lo", "hi"):
    check("imported eta_A "+end, F(evidence["integer_scalar_bounds"]["head_form_error"][end]), "==", eta)

with np.load(BASE/"neutral-head-covariance-559.npz") as data:
    z, a = data["z"], data["a"]
with np.load(BASE/"complete-covariance-532.npz") as data:
    m, covariance = data["m0"], data["cov00"]
check("Z shape", z.shape, "==", (512,510))
check("A center shape", a.shape, "==", (510,510))
check("M exact symmetry", np.array_equal(m,m.T), "==", True)
check("covariance exact symmetry", np.array_equal(covariance,covariance.T), "==", True)
h = m-.00024*np.eye(512)-(100/307)*(covariance+.0046*np.eye(512))
g = z.T@z
check("G center exact symmetry",np.array_equal(g,g.T),"==",True)
x = np.linalg.solve(h,z)
y = np.linalg.solve(a,g)
rx, ry = h@x-z, a@y-g
zx, gy = z.T@x, g@y
b_unsym = zx-gy
b = (b_unsym+b_unsym.T)/2
trial = .99*g-b-.05*np.eye(510)
trial = (trial+trial.T)/2
arrays = dict(z=z,a=a,h=h,g=g,x=x,y=y,head_inverse_remainder=b,
              residual_H=rx,residual_A=ry,trial=trial)
for name, matrix, limit in [("M",m,400),("covariance",covariance,1),
                           ("Zhat",z,23),("Ahat",a,500),("Hhat",h,500),
                           ("Ghat",g,100),("X",x,100),("Y",y,100),
                           ("Zhat_t_X",zx,2301),("Ghat_Y",gy,10001),
                           ("Bhat",b,20000),("trial",trial,20001)]:
    magnitude(name,matrix,limit)
for name, r in [("H solve floating residual",rx),("A solve floating residual",ry)]:
    magnitude(name,r,F(1,10**7))

try:
    factor = np.linalg.cholesky(trial)
    arrays["factor"] = factor
    reconstruction = trial-factor@factor.T
    arrays["factor_reconstruction"] = reconstruction
    magnitude("factor",factor,300)  # squared norm <90000<100000
    magnitude("factor floating reconstruction",reconstruction,F(1,10**7))
    check("factor proposed",True,"==",True)
except np.linalg.LinAlgError:
    check("factor proposed",False,"==",True)

# Uniform arithmetic ledger, under the inherited binary64 contract.
# Complete stored norms above are exact dyadic sums, not rounded norm calls.
gamma = F(1,2**43-1)  # gamma_1024; all products contract <=512 terms
u = F(1,2**53)
residual_round = gamma*500*100+u*(500*100+100+1)
gram_round = gamma*23**2
gram_error = gram_round+F(1,10**14)*(2*F("1.009")+F(1,10**14))
b_round = gamma*(23*100+100*100)+10*u*50000
factor_round = gamma*100000+10*u*50000
trial_round = 10*u*50000
check("rational H assembly budget",50*u*500,"<",F(1,10**8))
check("complete solve residual rounding",residual_round,"<",F(1,10**7))
check("complete solve residual budget",residual_round+F(1,10**7),"<",F(1,10**6))
check("complete G conversion budget",gram_error,"<",F(1,10**7))
check("complete B assembly budget",b_round,"<",F(1,10**7))
check("complete factor reconstruction budget",factor_round+F(1,10**7),"<",F(1,10**6))
check("complete trial assembly budget",trial_round,"<",F(1,10**7))

dz, dg, dh = F(1,10**14), F(1,10**7), F(1,10**8)
ex = (F(1,10**6)+dh*100+dz)/F(".239999")
ey = (F(1,10**6)+eta*100+dg)/F(".779")
eb = dz*100+F("1.008")*ex+dg*100+F("1.008")**2*ey+F(1,10**7)
finite_slack = F(".05")-F(1,10**6)-F(1,10**7)-F(".99")*dg-eb
check("finite head certificate slack",finite_slack,">",F(0))
check("reference inverse norm <5",1/F(".239999"),"<",F(5))
eps = F(1,10000)
tail_moment_sq = F(4,3*511**3)
check("entire moment tail squared",tail_moment_sq,"<",eps**2)
head_bound = F(".99")+5*eps
tail_bound = F(100,307)+5*eps+5*eps**2
check("complete tail coefficient",tail_bound,"<",head_bound)
check("complete squared norm upper bound",head_bound,"<",F(1))

for name,value in dict(gamma_1024=gamma,eta_A=eta,solve_rounding=residual_round,
        gram_error=gram_error,b_assembly_rounding=b_round,factor_rounding=factor_round,
        trial_rounding=trial_round,X_error_upper=ex,Y_error_upper=ey,
        head_matrix_error_upper=eb,finite_slack=finite_slack,
        moment_tail_squared_upper=tail_moment_sq,head_coefficient=head_bound,
        tail_coefficient=tail_bound).items():
    values[name] = str(value)

array_path = BASE/"energy-image-inverse-613.npz"
np.savez_compressed(array_path,**arrays)
out = dict(scope="Fixed N512 energy-image inverse Galerkin reference comparison",
    source_script_sha256=sha(Path(__file__)),input_hashes=pins,
    arrays_sha256=sha(array_path),exact_values=values,checks=checks,failures=failures,
    summary=dict(passed=not failures,head_target="99/100",finite_slack=str(finite_slack),
        squared_norm_upper=str(head_bound),required_upper="1",norm_upper="sqrt(1981/2000)"),
    qualifications=["Import C999k/l and audits557/561; no large covariance replay.",
        "Retain analytic response, IEEE754, directed Decimal, neutral-core and unreplayed c_star contracts.",
        "Domains, projection identity, full comparison and infinite tail justified in C999t.",
        "No mixed-block sign, Xi positivity, H2 or novelty claim."])
path = BASE/"energy-image-inverse-613.json"
path.write_text(json.dumps(out,indent=2)+"\n")
print("Checks:",len(checks),"failures:",failures)
print("Finite head: required <=99/100; certificate slack =",float(finite_slack),">0")
print("Complete squared norm upper:",head_bound,"required <=1")
print("Certificate:",path.relative_to(BASE.parent.parent))
print("Full matrices:",array_path.relative_to(BASE.parent.parent))
if failures:
    raise SystemExit(1)
