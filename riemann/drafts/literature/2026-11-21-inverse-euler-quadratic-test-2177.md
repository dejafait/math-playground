# Reciprocal Euler quadratic diagnostic2177

TARGET: Test the inverse-Euler diagonal weights v_j=1/[2(2j+3)] on one real quadratic with unit-modulus conjugate roots on the boundary of K_theta={w:|arg(w)|<=theta or w=0}, for arbitrary fixed 0<theta<pi/2, using Cardon et al. Section4.2; decide whether a universal real-polynomial sector-preserver is obstructed, without drawing an actual-Xi conclusion.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Source review2177 searched reciprocal linear multiplier, inverse-Euler and Bernardi sector terminology; checked stops379/618/1459 and exact operator duplicates; reused source-notes1461/1500. No ready exact-weight test or matching actual-Xi inverse theorem was located. No originality claim.
SOURCE_EVIDENCE: Cardon et al., https://arxiv.org/pdf/1802.02641v1#page=8 (direct primary PDF), arXiv1802.02641v1, 7 February2018, Section4.2 p8 supplies the real three-term coefficient-ratio diagnostic; Theorem4.1/Proposition4.2/proof p7 and Theorem5.2/necessity proof pp8-9 delimit multiplier and complex-input conclusions. Earlier Section2 coverage is reused. Full source details and limitations are in source-notes2177.
COMPARISON: The ratio diagnostic is known; the prescribed rational weights and fixed positive cone angle are the proposed specialization. A real quadratic tests the actual real-polynomial universal claim directly, avoiding inference from complex-only failures or a theta=0 limiting claim. No source result decides the single actual-Xi input here.
GAP: Evaluate the prescribed weights in the known diagnostic and rigorously locate the input and output roots relative to the same closed cone, retaining the nonzero scalar normalization. No such evaluation or counterexample was derived during review2177.
REASON: This bounded reproduction can decide whether sector membership alone justifies a universal inverse shortcut. A negative requires additional actual-Xi information; a pass gives no general theorem. It is distinct from the prescribed primitive and reciprocal theta-moment inverse stops.
SCOPE: One exact real quadratic family parameterized by fixed 0<theta<pi/2; no sweep, actual gamma computation, transcendental extension, claim against GORRTTW, Chasse access retry, unshifted descent or all-degree sign claim. New continuation requires separate approval before research.

Main gap: L030/L032/C032a actual-Xi all-degree mixed positivity.
Essential input C034z fixes the Euler weights and actual function
conventions from L018/L021. Its canonical proof still awaits later
independent review; the diagnostic relies only on the displayed
operator specification, not on an asserted actual-Xi sector theorem.
K_theta includes its boundary and zero. The source ratio notation is
independent of the actual gamma sequence.

An informative negative must exhibit both conjugate output roots and
compare their arguments with theta exactly, using the source's
three-term mechanism. It rejects only preservation on all real
polynomials of the specified cone. It is not a counterexample meeting
Kim--Lee's transcendence hypothesis or GORRTTW's actual-Xi hypothesis.
No polynomial may be substituted for actual A'', and no conclusion for
order-at-most1/2 transcendental inputs is authorized without a new
assessment. If no cone escape occurs, stop after the one diagnostic;
do not infer preservation or expand the search without review.

Plausible use: delimit the missing input in the conditional shifted
Jensen route and prevent automatic removal of Euler weights. RH_2(T),
actual transformed-sector membership, uniform degree, unshifted
descent and original mixed positivity remain unresolved regardless
of the diagnostic. No cross-notebook input. Matching Mathlib coverage
is unchecked. No code or numerical certificate is necessary.

## Separate source approval2180 — 21 November2026

Recovery repair: the ready assessment now contains its direct primary
source URL in SOURCE_EVIDENCE. The exact TARGET, SPECIALIZE decision,
scope and uncomputed diagnostic are unchanged. This is source approval,
not a mathematical advance or a new literature search.

Reopened [Cardon et al., *On Zero-Sector Reducing Operators*,
arXiv:1802.02641v1](https://arxiv.org/pdf/1802.02641v1#page=8),
7 February2018: introduction p1 (closed cone convention), Section4.1
p7 (preservation versus reduction), Section4.2 p8 (complete three-term
argument), and Theorem5.2 with its necessity proof pp8–9 (complex-input
scope). Section4.2 uses b>0, two right-half-plane roots, and the ratio
of adjacent diagonal weights. Its strict-reduction condition alone
does not decide fixed-cone preservation. The saved real quadratic test
is covered as a specialization, with no transcendental inference.

The extracted displayed transformed-root formula must not be copied
without checking its leading-coefficient normalization. A screenshot
request returned only an image marker, so no visual verification is
claimed. The next calculation must solve the weighted quadratic
directly, retaining all nonzero scalar factors; the source's argument
and ratio definition suffice for this diagnostic. No rational-weight
ratio, roots or angle comparison was evaluated in this approval.

Reused the local duplicate/failure comparison in source-notes2177 and
the operator specification in C034z; its conditional actual-Xi claims
remain outside this approval. No new source search or Chasse retry was
needed. Full matching Mathlib coverage remains unchecked. The main
mixed-sign gap is unchanged; this approval only permits the saved test.
