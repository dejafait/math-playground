# Integrated n=2 moment attempt — step184, working record

Approved target and source scope: drafts/literature/2026-11-10-integrated-theta-variance-review-182.md (EXPLORE, supplied at startup).
Main gap: actual-Xi all-index L966(16), within L030-L032/C032a positivity.
Attempt only the prescribed n=2, b=1/4, h=5184 ratio boxes.

L967(5), divided by the positive F(b)^2 F(h), gives
Q=d1*r+d2*s-d2*r^2-d1*t, where r=I1(b)/I0(b),
s=I2(b)/I0(b)>0, t=I1(h)/I0(h).
The nominated boxes give Q >= d1(1/50-1/100)-d2/1600 > 0.
Both negative terms are charged. This exact rational propagation is
local progress only; the moment boxes are not yet certified and no
sign is asserted at this checkpoint.

Plan: positive theta truncation n<=4 on [0,3], outward elementary
intervals, composite-trapezoid second-derivative error, and explicit
omitted-n and u>=3 bounds. One initial mesh, at most one refinement.
A pass provides one finite-index payment case, leaving higher indices
unresolved. Audited L968 already supplies the conditional all-index
prescribed-sign implication to RH; that implication is downstream
context and not a moment-estimate input. Failed boxes stop this test,
not the sign. No numerical-zero or RH input.

Completed: the initial N=3072 mesh passed with no refinement. Full
proof and exact error qualifications are canonical in L970; full
arithmetic evidence is scripts/li-theta/integrated-moment-certificate-184.json.
Both boxes and the complete signed bound passed. Independent audit
remains pending. The conservative box lower bound is
423263556/10748505625>39/1000; this is one fixed-index advance only.
