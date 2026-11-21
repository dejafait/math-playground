# Coupled stopped weighted density — bounded attempt nomination955

TARGET: Attempt a class-uniform measurable-set modulus for the stopped full weighted Jacobian of S(q,z)=-2 log q+H(q,z), initial (q,z)=(ir,s), using real tangent two-volume on the original flat raw flow with the assessed bidisk derivative bounds.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed review955 in assessment954 searched the exact coupled weighted-density claim and stronger singular-volume/compound-growth formulations; no matching theorem was identified. Local C466r/C466q and stops927/932/941/947/948 were compared. This is bounded coverage, not certified novelty.
SOURCE_EVIDENCE: TNV arXiv1706.03822v2 AppendixB(B.1)–(B.5), printed p22 https://arxiv.org/pdf/1706.03822v2 and conjugation-readable https://arxiv.org/html/1706.03822v2#A2; Wu–Kanevskiy–Margaliot arXiv2008.10321v2 Section3.1, Theorem4 printed p8 and Proposition5/full proof printed p9 https://arxiv.org/pdf/2008.10321v2; broader source cases and searches retained in assessment954.
COMPARISON: Available nonsingular variational and real-volume machinery supports one attempt; the full complex determinant with its singular weight, stopping and uniformity are the explicit missing specialization. C466r controls only one variable; changed-metric completeness and action-phase constancy do not pay this target.
GAP: Prove the stated class-uniform modulus or supply an admissible counterexample; the real-to-complex volume comparison, singular growth estimate, finite-lifetime interpretation and measurable extension are not established by this nomination.
REASON: This is an independently testable unpaid local coupling input for a possible later actual-weight deformation; a full matching theorem was not read, and no estimate is derived here. This newly written ready continuation requires separate approval next turn before mathematical invocation.
SCOPE: Two complex variables, a single double-zero divisor q=0, bounded bidisk, unit flat raw conjugated-gradient flow, fixed physical time, full real-parameter complex Jacobian, common derivative data and stopped density; no metric change, divisor intersections, actual-h or global-sign claim.

## Exact retained hypotheses and desired conclusion

Fix real 0<a<R<infinity, 0<b<L<infinity and finite common
nonnegative M_1,M_2, and fix the complex value H(0,0).
Let H be holomorphic on B={|q|<R,|z|<L}, with
||grad H||_2<=M_1 and ||D^2H||_op<=M_2 throughout B.
Derivatives are complex holomorphic derivatives; norms are the
standard Hermitian vector and induced operator norms.

On B minus {q=0} use S(q,z)=-2 log q+H(q,z) and
(dot q,dot z)=(overline(partial_q S),overline(partial_z S)),
with initial point (ir,s) for (r,s) in
I=(-a,a) times (-b,b), r!=0. The raw vector field and q^2 exp(-H)
are single valued although a local logarithm is used for S.

Let tau(r,s) be the maximal forward lifetime in that domain.
For T<tau let J_T be the full complex 2 by 2 derivative matrix
of (q(T,r,s),z(T,r,s)) with respect to real (r,s), holding T
fixed, with rows ordered (q,z) and columns (r,s). Retain
J_0=diag(i,1). Set
W_T=-q(T,r,s)^2 exp(-H(q(T,r,s),z(T,r,s))) det(J_T)/i
on survivors; set W_T=0 for T>=tau and for r=0.
Neither a classical Jacobian after stopping nor a conserved
signed integral is part of the definition.

Seek a positive T_0 and finite modulus omega(u), depending only
on a,R,b,L,H(0,0),M_1,M_2, with omega(u)->0 as u decreases
to zero, such that for every Lebesgue measurable E subset I,
sup_{H,0<=T<=T_0} integral_E |W_T|<=omega(|E|).
The supremum includes the complete class sharing those data.
Prove any needed finite-lifetime zero-hit/escape interpretation
and Borel measurability of the zero extension, including simultaneous
limiting boundary events. C466r's one-variable proof cannot simply
be cited for these changed hypotheses.

## Bounded test and decision rule

Use the assessed real compound-volume machinery on nonsingular
surviving intervals to seek one common integrable estimate for the
full weighted determinant. The determinant-versus-real-volume
comparison and treatment of the weight must be explicit, without
assuming determinant nonvanishing, a holomorphic initial-data flow,
independent scalar variations, or regularity of the survivor boundary.
Any singular cutoff must have constants uniform as it is removed.
The source machinery is imported by citation; reprove only the
missing comparison, singular estimate and endpoint specialization.

Success is the stated modulus with all common data and measurable
sets retained. An admissible counterexample must violate this
modulus, not merely a proposed pointwise envelope. A failure of the
chosen volume bound is a method limitation: preserve that reasoning
and report the exact unpaid estimate, without asserting non-UI.
Do not repeat the completed scalar audit. This is one bounded proof
attempt, not an invitation to accumulate variants or new lemmas.

Local comparison inputs: C466r (audited nonzero-background scalar
estimate) and C466q (frozen scalar control). Their conclusions are
not asserted as premises for a coupled theorem. Essential external
inputs, hypotheses and proof cases are recorded in
[review955](2026-11-14-coupled-normal-tangential-weighted-flow-954.md).
No cross-notebook input is involved. Full matching Mathlib coverage
has not been checked; the attempt must retain that qualification.

Plausible downstream use is a local analytic factor depending on
both a collision coordinate and a tangential coordinate. Even
success leaves metric normalization under original-coordinate
changes, intersecting divisors, noncompact ends, homology, endpoint
payment, signed integration, all-order signs and actual-Xi realization
unproved. Stops927/932/941/947/948 remain in force in their scopes.
There is no RH candidate and no source-backed central creative
mechanism: the global signed-contour condition is still missing.

This target develops established variational/volume tools. Any local
success is a specialization beyond the exact passages inspected,
not a demonstrated advance beyond the literature. EXPLORE permits
that investigation without a novelty claim. Approval of this fresh
assessment is reserved for the next turn; no mathematical attempt
has been performed in source step955.

## Separate approval and direct-source repair956 — 14 November 2026

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this ready assessment; repair that provenance defect and verify the load-bearing passages without repeating discovery or changing the target.

The primary links now occur directly in SOURCE_EVIDENCE. Reopened
TNV Appendix B (B.1)–(B.5), printed p22, and checked the conjugations
in rendered HTML equation (73): both the Hessian and tangent matrix
are conjugated in the flat-flow equation. This is a local variational
identity on nonsingular surviving intervals, not a stopped-density theorem.

Reopened WKM Section3.1's continuous real A(t) hypothesis, Theorem4
and its full proof, and Proposition5 and its full proof, printed pp8–9.
The latter uses the compound transition equation and Coppel's
inequality; its growth estimate does not require the uniform negative
matrix-measure hypothesis used for contraction. It does not supply
a cutoff-independent singular estimate or stopped measurable extension.
The rectangular-volume interpretation and earlier source comparison
remain in assessment954; no new specialization is proved here.

The two PDF screenshot requests again returned reference-only output;
no visual check is claimed. Primary extracted text and the TNV HTML
were the inspected evidence. Full matching Mathlib coverage remains
not checked. C466r/C466q and recorded stops are reused from review955;
no changed hypothesis calls for reopening their detailed proofs.

Separate source approval is now completed for this unchanged target:
DECISION remains EXPLORE, authorizing one bounded attempt next turn.
This repairs provenance only: outcome STALLED, with no new theorem,
negative mathematical evidence or exploration-budget reset. Preserve
the exact common data, desired modulus and abandonment test above.
Failure of the volume envelope alone still cannot refute uniform
integrability. No new mathematical target has been introduced.
