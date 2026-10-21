# Equality whole-map finiteness — working checkpoint

2026-10-13, step 254. Actual task: proof_attempt. The pre-invocation
SPECIALIZE assessment is drafts/literature/2026-10-12-equality-classifying-map-finiteness.md;
its exact TARGET is the only mathematical task of this step.

Main gap: universal primitive rational Hodge realization. Intermediate
threshold: finiteness of L097's actual whole map onto its reduced image,
including the possible exceptional fibre. Downstream use: a controlled
global image for later reconstruction or separation tests. Continue only
if the natural stable differential is injective and the entire split
fibre is finite; narrow or stop if either fails. F existence, integrated
germs, separation and transport are independent unresolved assumptions.

Inputs inspected: full L095 and L096, L097's statement and relevant
whole-family/stable-open/audit passages, L064's natural tangent bridge
as methodological comparison, histories 246/248/250/252 and ATTEMPTS/061.
No duplicate whole equality-family finiteness result occurs there. The
compatible split quadratic tangent remains a preserved stop, not a
reason to prohibit this global scheme test. Ready known-tool coverage
is reused; no new theorem search or new scope is proposed for this attempt.

Unfinished reasoning: for real u, L095 gives r_(Iu)=I_c r_u and
r_u harmonic. For v=(u-i Iu)/2, mixed-curvature contraction on (0,1)
fibre vectors is r_u^(0,1). Its harmonic vanishing forces r_u=0 by
skew-adjoint reality, then u=0 by the positive norm. Need write the
same-family dual-number/GAGA/natural Ext1 comparison and verify this
applies only over the stable open. Thereafter extend unramifiedness
from closed complex points by openness. The full exceptional fibre
is supported in the finite complement of that open; check this as a
scheme-point statement, without assuming its scheme structure reduced.
Apply proper locally quasi-finite finiteness, then reduced-image and
finite-factor criteria. No quotient derivative at a split point is used.

Completed outcome: the canonical proof is
lemmas/L098-equality-whole-classifying-map-finiteness.md. The same
first-order extension and complex curvature contraction give natural
stable tangent injectivity. The stable-open preimage identifies the
full exceptional support, including the empty case, so all-points
quasi-finiteness and whole-map finiteness follow. Reducedness of the
source and the separated closed image immersion justify the finite
surjective reduced-image factor. Spot checks read the relevant primary
Biswas--Schumacher 3.3 formula and Stacks 0B2G/02G4/02V5/02NG/01W6/
02LS/056B/035D statements and proof cases; these are forward-proof
applicability checks, not a new literature assessment. A separate
critical audit remains pending; no stronger image or existence claim
is made. Documentation validation is recorded by the scoped checker.
