# Two real parts: bounded orbital attempt1218

17 November 2026. Work in progress on the unchanged TARGET of the
preexisting EXPLORE assessment1216/coverage1217. One mathematical
attempt; no new source theorem is being introduced. Existing notebook
changes and all prior stopping evidence are preserved.

Main gap: L030-L032/C032a actual-Xi all-degree positivity. The target
is an absolute bound for the separately normalized physical adjacent
response for exactly two conjugate pairs with unequal real parts and
one common real background. A bound would pay one finite-reference
perturbation cost; actual-Xi scales, signed-complement hypotheses,
theta signing and realization remain independent.

Test: obtain an explicit C independent of n and all real contrasts,
or a rigorous family with divergent |E|/[x*(b_1^2+b_2^2)]. Reality and
nonvanishing on the closed window come first. A dimension- or
contrast-dependent estimate, or a finite sample, is inconclusive.

Ready inputs read: C030l's complete weak-row comparison proof;
C030o's orientation and physical-derivative argument, with its
common-real-part restriction; C030n's statement/orientation setup;
working1213 and working1217. Stops1117/1181/1193/1200/1107 retain their
recorded scopes. The orbital-named local file search found no existing
two-real-part bound. The broader source comparison is reused, not
rerun. Full matching Mathlib coverage remains unchecked.

Current mechanism under test: block U(2) averaging within each pair
preserves the real reference, but the two corner spectra are disjoint.
Do not assume that their product is a test of one nested array or that
their laws are independent. C030l can compare a single pair placed
first with arbitrary fixed real fields on the other rows. The unpaid
issue is the joint physical response, including the derivative of the
real tilt. Investigate a controlled conditional representation before
claiming any joint derivative bound.

Completion, if obtained, will be recorded in a canonical lemma with
its exact hypotheses, proof and source qualifications. Otherwise retain
the unresolved estimate here. This checkpoint is not a proved result.

## Mechanism found; checks in progress

The disjoint-corner product is unnecessary. For Y=t*V*P_j*V*, let
S_r be the trace of its leading r-corner. The entire imaginary phase is

    T=2*b_1*S_1-(b_1+b_2)*S_2+2*b_2*S_3-b_2*S_4.

The real scaled-orbit law has fixed fields c_2=a_2-a_1 and, for n>4,
c_4=r-a_2; when n=4 the S_4 term is constant and only c_2 remains.
Thus one nested-array comparison can act on this entire phase.
Reality follows by swapping both conjugate pairs. On an actual orbit
with 0<=Y<=U*I, |T|<=U*(|b_1|+|b_2|). The positive quotient floor
31/32 at the closed phase window therefore has a direct route.

Write A=|b_1|+|b_2|, d=(2*b_1,-b_1-b_2,2*b_2,-b_2), and
K=sum_(r=1)^4 r*|d_r|. For U=t+eta, clipping the scalar phase to
[-U*A,U*A] makes its cosine globally U*A-Lipschitz. Adding the
linear correction U*A*sum_r |d_r|*S_r to either sign of this clipped
cosine gives a continuous increasing full-array test. C030l's scaled
top-row sandwich should then pay |F_j(t+eta)-F_j(t)|<=U*A*K*eta.
The fixed fields pay the derivative of the real tilt automatically.
Here K<=4*|b_1|+12*|b_2| and A*K<=20*(b_1^2+b_2^2), so this
would yield the explicit adjacent constant 1280/31.

Still to document carefully: extension of C030l's tests to the fixed
top row when n=4; translated-law normalization; full physical
differentiability, closed-window logarithm, endpoints and zero phases.
No stochastic order for complex laws or independence is being used.

## Completed attempt

The nested-trace mechanism yields the exact approved bound with
C=1280/31, independent of dimension and all real contrasts, and the
positive real partition-ratio floor31/32. The full proof, including
the physical covariance term, n=4 top-row test extension, translated
normalization, endpoints and zero phases, is canonical in
[C030p](../../lemmas/C030p-two-real-part-orbital-response-bound.md).
The earlier disjoint-corner-product approach above is exploratory
context only; it is not an assumption or an additional result.

Outcome: ADVANCE, RESEARCH, POTENTIALLY_NEW relative to the documented
search, not certified originality. This is one mathematical attempt,
not an independent audit. The constant is coarse and gives no actual-Xi
budget or positivity claim. C030l is the sole direct local mathematical
input; C030n/o compare scopes. Existing canonical proofs and source
assessment1216 are unchanged. No mathematical script was needed.

The next conceptual audit is nominated separately with REVIEW_REQUIRED.
It must check the increasing tests on the full coordinate space,
the deterministic top row at n=4 and the full time derivative before
the result is treated as audited. All unrelated Xi/signing/realization
gaps and the named historical stops remain in force within their scopes.
