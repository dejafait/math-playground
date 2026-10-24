# Preferred twisted removal — step 491 working checkpoint

Approved target: test smooth positive extension of the preferred twisted
harmonic metric and Chern connection across Z on L147's rank-24 M.
Use the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-23-preferred-twisted-surface-removal.md`.
Actual task type: proof_attempt; RESEARCH / REPRODUCTION.

The main gap is universal primitive Hodge realization; even the equality
kernel F is hypothetical. The intermediate target could support a later
Chern inequality on this specific M. Continue only if the actual metric,
finite energy, unitary removal and both holomorphic inverse matrices
match; otherwise park or narrow the failed bridge. Z may be empty.

Input checks completed: L147 gives the actual locally free rank-24 M;
L148 supplies its natural harmonic metric; audited L149 bounds curvature
when its central block vanishes; audited L150 makes that block zero for
exactly the preferred dual HE twisting metric; audited L151 supplies ASD
for that same metric and Chern connection on U. L149 allowed any fixed
smooth positive line metric, so this is a specialization, not a change
of its conclusion. The older rank-50 L114 is only a comparison, not a
rank-24 input. ATTEMPTS/063/066/086 remain valid in their stated scopes.

Proof plan to finish and check: bounded curvature gives energy O(epsilon^4)
at each point. A holomorphic M-frame and its positive smooth punctured
Gram matrix give an actual smooth unitary frame, meeting Platt A.10 for
U(24) on the original smooth metric. ASD and Bianchi give differential
Yang--Mills as well. The smooth unitary gauge extension has integrable
(0,1) operator by continued ASD. Koszul--Malgrange gives local holomorphic
frames; extend the punctured comparison and its inverse entrywise by
Hartogs, retain both inverse identities, and transport the smooth
positive metric onto M. No limit of the removing gauge in the original
frame is needed. Check overlap agreement by equality on the dense
puncture. Do not compute a Chern inequality or split-count bound here.

No mathematical script, cross-notebook input, new removal theorem or
new source retrieval is needed. Preserve all preexisting changes.

## Completion

The full application and all qualifications are canonical in
`lemmas/L152-preferred-twisted-harmonic-connection-smooth-removal.md`.
The conditional extension threshold is met, including the given metric,
original curved base, U(24) scope, smooth punctured comparison, both
holomorphic inverses and positive transport. No Chern inequality or count
is evaluated. The separate audit continuation is REVIEW_REQUIRED in
`drafts/literature/2026-10-23-preferred-twisted-removal-critical-audit.md`.
