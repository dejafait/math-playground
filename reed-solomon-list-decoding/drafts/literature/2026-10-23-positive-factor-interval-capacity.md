# Positive factors — proposed certified mixed-distance enclosure

TARGET: Assess certified interval Newton enclosure of L111's 64 positive distance factors using all mixed-distance contractions, with x_5^3<=c_5 as the single capacity test.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the local scaling/existence assessments and ATTEMPTS/082,093; searched Rump verification nonlinear systems Krawczyk interval Newton, positive triangle product scaling prescribed marginals interval Newton, tensor scaling interval Newton, and maximum entropy Krawczyk. Inspected Rump's primary theorem rather than relying on search summaries; no search established a precomputed enclosure or this capacity verdict.
SOURCE_EVIDENCE: Rump (2010), Acta Numerica 19, 287–449, DOI 10.1017/S096249291000005X, corrected author PDF https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf , Theorems 13.1–13.3 and proofs, Algorithm 13.4, author pp.88–90 and failure/exclusion discussion p.91; §5.3–5.5 (5.14)–(5.17), author pp.27–28. Canonical import: foundations/14-validated-nonlinear-enclosure-source.md. Reuse Csiszar–Shields 3.1–3.2 and Remark 3.1 through audited L111 and foundations/04,12,13.
COMPARISON: Rump supplies a sufficient rigorous local enclosure criterion for a square continuously differentiable system, covering the polynomial form of all 64 L111 equations. It supplies no candidate, computed inclusion, conditioning estimate, actual capacity verdict or global uniqueness. L110 and ATTEMPTS/082 remain distinct stopped tests.
GAP: Essential theorem coverage for one enclosed-root test is now available; construction and verification of a positive box, the entire residual/Jacobian, all strict inclusion margins and the distance-5 comparison remain mathematical work. Ansatz-wide rejection would still require a separate global uniqueness or exhaustive-coverage justification.
REASON: Complete the saved source assessment by importing the standard enclosure criterion and identifying its exact local obligations; do not derive an enclosure or approve global rejection. A new bounded implementation target is saved separately for next-turn approval.

SCOPE: Source assessment only, for exactly TARGET; step 419 imports a general criterion and compares hypotheses, without a factor solve, mathematical script, new lemma, interval construction or global-uniqueness proof. The original proposal below is retained as historical scope.
LITERATURE_REASON: The saved REVIEW_REQUIRED target lacked an essential validated-enclosure theorem; entropy existence coverage does not cover this changed quantitative task.

## Step 419 — source comparison completed

The main target gap is arbitrary-center safety at 67/68 agreements;
the route bottleneck is L098's shared capacitated-triangle feasibility.
The intermediate target is exactly TARGET. Its plausible use is a
decisive test of one actual capacity of a positive product weighting,
before spending effort on its other capacities. No new mathematics
beyond the sources is claimed by this literature step.

The canonical theorem statement, precise citation and Mathlib qualification
are in [foundations/14](../../foundations/14-validated-nonlinear-enclosure-source.md).
Comparison with L111 is as follows. Its equation (7), minus its right
side, is already a square 64-coordinate polynomial residual in the
positive x_i, i=5,...,68. Its rational c_i and integer D are fixed;
the function has no structural domain singularity. A future application
must nevertheless construct a strictly positive box and certify the
whole Jacobian enclosure there. Existence in L111 does not establish
Jacobian regularity or numerical conditioning. No redundant-row removal,
fixed gauge, logarithmic coordinate transformation or normalization is
assumed by this assessment. If rescaling is used later, keep it an
explicit invertible rational diagonal change and verify the original
64 residuals as well.

Retain every actual (i,j,t,s) and its D, including all t-s classes,
six presentations, both endpoint repetitions and the coincident row.
Only the distinct positive-edge equations are nonlinear unknowns;
the null and repeated cases stay fixed exactly as in L111. Coefficient
aggregation may sum all D for identical product monomials, but must
retain a complete reconstruction of which original orbits were summed.
No aggregation identifies the original source variables outside the
product ansatz. This is a comparison with the existing formula, not
a new coefficient calculation or derivative computation.

For one future box [l,u] certified to contain a positive root, use
u_5^3<=c_5 as a pass of this single capacity and l_5^3>c_5 as rejection
of that enclosed root. Compare exact cubes; avoid an uncertified cube
root. A straddling box or failed inclusion is inconclusive. The imported
local uniqueness does not justify rejection of every positive product
solution. L111's projected distribution is unique in its stated role,
but neither that sentence alone nor the enclosure theorem is used here
as a global-factor uniqueness argument. Such a strengthening is outside
the approved enclosed-root test and needs its own assessment and proof.

Continue to a separately approved bounded construction/check if all
original coefficients can be reconstructed. Stop that run at its saved
budget; a failed inclusion does not warrant a precision/radius sweep or
revival of ATTEMPTS/082. All other capacities, Boolean lower rows, full
source feasibility, PSD and RS realization remain independent gaps.
The 955–957 bracket is unchanged.

Primary access qualifications: the author PDF's theorem/proof pages
and interval arithmetic passages were directly opened and read. Its
Lemma 10.5 author-p.56 extraction is garbled; a targeted primary index
returned its complete statement and short proof, but no independent
local audit of that auxiliary lemma is claimed. The load-bearing import
is the directly read Theorem 13.3 with its full proof. A shell download
failed DNS resolution; it was not used as evidence. Moore–Kearfott–Cloud,
*Introduction to Interval Analysis* (2009), chapter 8, pp.105–128,
DOI 10.1137/1.9780898717716.ch8, was inspected only through its publisher
preview; its full theorem text is an unread alternative, not an input.
The Wang–Cao–Li (2008) generalized-Krawczyk optimization paper appeared
as an abstract-only lead; no theorem from it is imported. These optional
leads do not block the directly accessible Rump criterion. No failed
search is evidence of novelty.

The new continuation is
`drafts/literature/2026-10-23-positive-factor-enclosure-implementation.md`.
Its ready source comparison must receive the supervisor's separate
next-turn approval before any implementation or mathematical attempt.

## Proposed bounded test and downstream use

The main gap remains arbitrary-center safety at 67/68 agreements. On
this route the shared capacitated-triangle problem at the fixed pairs
is unresolved. L111's critically audited existence theorem now permits
asking about an actual positive product weighting rather than a bound
conditional on existence. The proposed intermediate target is a certified
enclosure strong enough to decide one necessary capacity, not a full
capacitated feasibility or PSD solve.

Use L021,L098,L109,L110,L111 and foundations/04,12,13. Retain
N=floor(65537^28/2^128)+1, the exact c_i, and all 64 equations (7) of
L111, with every actual D(i,j,t,s) coefficient. Unknowns are the positive
x_i=c_i*f_i for 5<=i<=68. The two removed repetitions, null-edge zeros,
coincident row and every original t-s class remain as in L111. Any
aggregation must sum exact coefficients for all those classes; it cannot
discard a class or change the moment convention.

For a future separately approved mathematical turn, consider one bounded
candidate construction followed by one rigorous enclosure test for this
complete system. The source comparison must decide whether a usable
inclusion theorem applies, which exact or outward-rounded arithmetic is
required, and what a failed enclosure can legitimately conclude. It
must also check any normalization, Jacobian nonsingularity or uniqueness
assumption rather than infer these from existence. No iteration count,
precision schedule or implementation is approved here.

The discriminating threshold is the actual distance-5 equilateral
capacity x_5^3<=c_5. A certified positive-root box whose upper endpoint
cube is <=c_5 passes only this capacity; a lower endpoint cube >c_5
rejects that enclosed weighting. Rejection of all positive product
solutions additionally needs justified uniqueness or exhaustive coverage.
A straddling box or failed inclusion test is inconclusive, not evidence
of nonexistence or a capacity violation. Even a decisive pass leaves
all other triangle capacities, Boolean lower rows, full source
feasibility, PSD and RS realization unresolved.

This is materially different from ATTEMPTS/093: it uses all mixed-distance
marginals to enclose factors, not the same equilateral-only allowance.
It is not a rerun, rounding, parameter scan or retuning of ATTEMPTS/082's
full-variable proposed moment array. Both historical stops remain intact.
If primary coverage cannot support a bounded certified test, park this
proposal rather than start an uncertified numerical solve. No mathematical
advance or novelty is asserted by this proposal. Mathlib coverage for
the full enclosure theorem and this specialization is not checked.
