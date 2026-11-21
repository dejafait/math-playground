# Double-contact isolation: bounded mathematical attempt, 6 November 2026

Invocation-start assessment: `literature/2026-11-06-double-contact-isolation-scope.md` (EXPLORE). Target unchanged. Inputs are L847 full pullback and audited L864, exact orders m=n=2, both real ranks one, C2 real radial u, q>=0 and J(p)!=0. Main Xi positivity gap remains open.

## Saved reasoning before completion

Translate p to (0,0); w1=Phi1-zeta, w2=Phi2-eta, alpha=zeta(a+i), beta=eta(d+i). L864 gives b=c=0, alpha beta!=0 and K0 alpha^2 beta^2>0. The exact full density is q=K w1^2 w2^2; set H=w1 w2/(alpha beta), B=K alpha^2 beta^2. Shrink so Re B>0 and all coefficient units remain nonzero. Then q=B H^2 exactly. At any point with Re H=0, q>=0 implies 0<=Re q=-(Re B)(Im H)^2, so H=0. No square-root theorem or high-order expansion is needed.

Differentiability gives H(t,t)/t^2 ->1 and H(-t,t)/t^2 ->-1 as t->0 from either side. For each small t!=0, continuity on the fixed-angle segment y=t, x between -|t| and |t| yields Re H=0 somewhere. Since the second angle is nonzero, w2 cannot vanish; hence w1=0, and its own angle then forces x=0. Therefore w1(0,t)=0 for every sufficiently small t!=0. Symmetrically H(t,-t)/t^2 ->-1 gives w2(t,0)=0. This appears to force the entire local G-contact union to be exactly the two coordinate fibers, contradicting isolation.

Remaining checks before canonical statement: uniform shrinking for all signed t; isolate the two selected G zeros and exclude Phi1=Phi2; verify no use of an unapproved higher-order Taylor or inverse; retain orientation and actual coefficient; make the conclusion explicitly conditional, unaudited, and limited to two double zeros/rank one. No actual double zeros or global extension asserted. Existing count-only, moment and flux stops remain.

## Completion

The completed proof and qualifications are canonical in L865,
`lemmas/L865-double-rank-one-contacts-force-crossing-fibers.md`.
The common neighborhood uses only three fixed directional limits;
the angular exclusions handle both signs of t and both zero-set
inclusions. The result excludes isolation under the exact hypotheses,
without assuming scalar nondegeneracy or proving germ existence.
It is independently unaudited. The saved preliminary reasoning above
is preserved as work history, not a separate canonical proof.
