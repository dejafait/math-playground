# Step634 — approved endpoint calculation working record

Gate: the unchanged SPECIALIZE assessment
`drafts/literature/2026-11-05-log-theta-endpoint-sign-test.md`.
Read L016/L019/L021, the complete L821 proof/audit and the named
common-symbol, automatic-variation and automatic-adjoint stops.
No global sign transfer is inferred. Existing changes are preserved.

Main gap: actual-Xi all-degree mixed positivity. Sole intermediate target:
the two endpoint signs of the existing normalized Q_3. A negative sign
excludes global TN3 for H(x-y); positive signs give only necessary endpoint
conditions. Stop at origin order eight if signs/cancellation are unresolved.

Provisional algebra, not yet a verified result: for even K write
K/K(0)=1+c2 u^2+c4 u^4+... . Substitution in L821(1) suggests
Q_3=-256 c2 c4 u^6+O(u^8). Need exact verification, signed
enclosures and justified four differentiated errors. Obtain K derivatives
from P_0(a)=8a^2-12a,
P_(r+1)=(1/2-2a)P_r+2a P_r', r<=8.

At infinity the full n=1 logarithm is
v+9u/2-c+log(8pi^2)+log(1-3/(2c))-log(m0).
Use its exact derivatives before selecting a leading term. The actual
relative tail must be controlled separately through D^4, not by
differentiating a scalar O-bound. Plausible leading term: 128 c^3 u^6;
this and the error propagation remain pending. All global minors,
lower oscillation, unbounded Laguerre interface and Xi transfer stay open.

Completed: both endpoint signs are positive. Canonical statement, full
analytic error propagation and qualifications are in L826. The exact
origin certificate is `scripts/log-theta/endpoints_634.json`; all checks
pass, including -10<c2<-9, 37<c4<39 and 90000<C6<91000.
Formal polynomial operations verify all Q3 cancellations through u^8.
The provisional infinity leading term above is now proved with separate
D^j tail bounds for 0<=j<=4, positive denominators, and a final relative
bound tending to zero. Neither scalar O differentiation nor plots are used.
No explicit finite onset, bridge to the compact interval, global TN3 or
Xi positivity is established. This is REPRODUCTION/local specialization
under the reused literature gate, not a claim of research novelty.
