# Mixed covariance weight: completed source and scope assessment

TARGET: Test whether a fixed convex mixture of L419's k=13 and k=14 covariance weights matches L422's added correlation while preserving every L421 constraint.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 169 searched moment-constrained convex mixtures, prescribed marginals, finite cubature and zeta covariance matching; inspected Bayer--Teichmann Corollary 2/Remark 2 and Theorem 2/Remark 4 and Carlen--Lieb's Horn statement/proof in primary PDFs. Scoped October-16 records contain the proposal but no completed mixture compatibility proof.
SOURCE_EVIDENCE: Bayer--Teichmann, The proof of Tchakaloff's Theorem, arXiv:math/0502473v2, pp. 3--5, https://arxiv.org/pdf/math/0502473v2 ; Carlen--Lieb, arXiv:0904.0734v2, Horn theorem after (1.1), proof through (1.2), pp. 1--2, https://arxiv.org/pdf/0904.0734v2 ; reuse Young, A short proof of Levinson's theorem, Arch. Math. 95 (2010), 539--548, Lemmas 4--5/(4.1)--(4.5), pp. 542--543, https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf , as assessed in step 164 and audited in L422.
COMPARISON: Finite moment convexity/cubature is standard and Schur--Horn supplies the existing pointwise matrix input; neither certifies the proposed covariance substitution with the full prescribed-response interface. The actual moment constants and source hypotheses are unchanged. The remaining work is an elementary specialization of audited L419/L421/L422, not a new zeta moment theorem.
GAP: Verify both constituent admissibility inequalities, an H-independent convex parameter matching the added coefficient, fixed positive bounds, gamma cancellation, both first means, six second entries, all 23 quartic coefficients, cubic/envelopes, support and capped cubic. No mixture parameter or feasibility is established in this literature turn.
REASON: The changed family required a separate scope comparison, now completed with no essential source blocker. A bounded mathematical attempt on this exact target is approved; reuse known moment inputs and the explicit Borel construction rather than reprove their general source theorems.
SCOPE: E=H^(-1) integral_[H,2H], ell=log H, W=|zeta(5/2+it)|^2; only a convex combination of the two individually calibrated L419 weights at k=13,14, with all parameters fixed independently of H. Keep the actual response, uniform height marginal and L421 high/intermediate components. No growing powers, height-dependent mixing or global critical-function realization is covered.
COVERED_TARGET: Test whether a fixed convex mixture of L419's k=13 and k=14 covariance weights matches L422's added correlation while preserving every L421 constraint.

LITERATURE_REASON: The two-weight family was outside the completed single-fixed-k assessment. This required comparison reuses its moment coverage and reviews only the new convex/covariance interface.

The main RH gap is global mixed positivity. The proposed intermediate
target asks whether this particular added response correlation defeats
only the single-power ansatz or also this specified two-weight extension.
If feasible, it would clarify what further information is necessary for
actual capped nondegeneracy; if infeasible, the failed compatibility
condition would constrain this alternative as well. Neither outcome
alone decides actual critical-function realization, clipping, the
full-error regulator margin or RH.

Essential local inputs are L419's fixed weights and response moments,
L421's complete rare/intermediate/bulk construction and its separate
audit, and L422's actual coefficient and certified comparisons. The
proposed mixing parameter must be fixed independently of H. Both
constituent weights must be admissible, and all bounds must work with
one eventual onset for that fixed choice. No mixture coefficient,
compatibility proof or feasibility conclusion is supplied here.

The continuation test is exact leading-coefficient matching together
with the entire existing list and fixed support/envelope requirements.
A coefficient match alone is insufficient if any construction interface
fails. Stop this candidate if the admissible convex range misses the
actual coefficient or a required L421 condition cannot be preserved.
The historical fixed-g0 stop remains intact in either case.

The source comparison below completes that review. It approves a separate
mathematical attempt, not the proposed law's correctness. The retained
test and unresolved assumptions above are unchanged.

## Primary statements and their limits — step 169

Christian Bayer and Josef Teichmann, *The proof of Tchakaloff's Theorem*,
[arXiv:math/0502473v2](https://arxiv.org/pdf/math/0502473v2), revised
4 May 2005: read Corollary 2, Remark 2 and its pushforward proof on
pp. 3--4, and Theorem 2/Remark 4 on p. 5. Corollary 2 assumes a positive
measure concentrated on a measurable set and a measurable finite feature
map with integrable coordinates. It represents their integrals by positive
weights at finitely many points of that set. For finite mass, adjoining
the constant feature preserves mass. Theorem 2 gives the polynomial
version for a finite positive Borel measure with the required absolute
monomial moments. Remark 4 describes representability on a closed set by
the convex hull of its polynomial feature image.

These results require a representing measure or verified convex-hull
membership. They do not certify our parameter or covariance feasible.
Finite cubature on the joint height/state space does not retain its full
continuous height marginal by finitely many feature matches. Do not use
it to replace that marginal. No general moment theorem needs reproof.

Eric A. Carlen and Elliott H. Lieb, *Short proofs of theorems of Horn
and Mirsky on diagonals and eigenvalues of matrices*,
[arXiv:0904.0734v2](https://arxiv.org/pdf/0904.0734v2), 13 May 2009:
read Horn's theorem after (1.1) and its two-dimensional and inductive
proof through (1.2), pp. 1--2. For real eigenvalue and diagonal lists,
majorization suffices for an orthogonal conjugation with that diagonal.
L419 already imports the constant trace-average case. This is pointwise
existence, without Borel dependence or negative translated support.
Reuse L419's coordinate algorithm for measurability, after verifying
the covariance and negative-trace hypotheses needed for strict support.

Young's fixed-twist theorem is reused from
[step 164](2026-10-16-response-modulus-weighted-second-moment.md) and
[the audit assessment](2026-10-16-response-modulus-second-moment-audit.md);
it was not freshly retrieved here. Its small complex shifts, fixed
twists, smooth weights, both diagonals, sharp bracketing and sequential
head/tail limits have already been checked for this observable in L422.
The proposed weight change does not change that observable or call for
a new zeta moment. Import L422's actual T; do not reprove Young or put
a fast gamma phase into its smooth weight.

The underlying Bui--Hall, Hughes--Young and Curran--Heycock scope and
exact old tolerances remain as inspected in
[step 162](2026-10-16-prescribed-response-two-scale-counterlaw-audit.md).
L421's step-163 audit and L422's step-168 audit are completed inputs.
No new derivative order, critical shift, growing twist or conditional
actual-moment assertion is proposed. Reuse their unchanged assessments;
no additional essential source remains unread. Full matching Mathlib
coverage of the proposed specialization is not checked; unknown is not
evidence of absence.

## Boundary of the approved mathematical attempt

The proposed object is a convex combination of the two g0 functions
defined by L419 (4), each with its own prescribed theta. This specifies
the test family, without deriving a mixture coefficient or its feasibility.
Do not substitute uncalibrated powers or a parameter depending on H.
Mixing whole conditional laws is a different implementation and must not
silently replace the specified covariance-weight test.

1. Check R_13>S and R_14>S with justified exact bounds before using
   either constituent as admissible. The B_k formula alone does not
   prove theta in (0,1). L422's audited B_13,T,B_14 bounds are reusable;
   no fresh certificate was run here. Determine the fixed convex
   coefficient, if one exists, in the separate mathematical attempt.
2. Establish average normalization, the W calibration needed for first
   Delta, the added W^2 calibration, positive upper/lower bounds and
   complete gamma cancellation. Use L419 (3)--(5) at fixed powers,
   with the height-first finite-frequency limit, without independence.
3. Normalize against L421's actual remaining mass and check (7)--(9):
   retain the full O(sqrt(ell)) matrix subtraction, bounded mean,
   positive covariance and uniform negative trace. Apply the Borel
   six-state implementation only after these hypotheses hold.
4. Verify both first means separately: first Bcal is exact in L421;
   first Delta permits o(ell). Four even second entries allow only
   O(1), and xy,yz have the much smaller L416 (1) tolerances. Retain
   exact full-matrix cancellation; O(sqrt(ell)) errors cannot remain
   in those entries or in first Bcal.
5. Retain every high/intermediate contribution, all 23 quartic limits,
   beta_* ell^2+o(ell^2) signed cubic, both absolute third envelopes,
   fourth envelope, exact curvature and support avoidance. Check the
   added correlation for the complete law using L422's component
   comparison, not just its leading bulk covariance.
6. Check fixed support constants and one eventual real-H onset, and
   capped absolute cubic o(ell^2) for every fixed lambda>0 with the
   same law independent of lambda. No consistency across H or global
   critical-function realization is required or concluded.

These are obligations, not conclusions of this source review. SPECIALIZE
permits this bounded elementary verification as REPRODUCTION, with no
new general moment theorem. A successful construction needs a canonical
proof and a later separate critical audit. An arbitrary covariance design
or changed implementation outside this scope requires its own review.

## Search, duplicates and preserved failures

Queries on 2026-10-16 included `moment constraints probability measures
convex mixtures support constraints Tchakaloff theorem Bayer Teichmann`,
`Carlen Lieb short proof Schur Horn theorem applications arxiv 0904.0734`,
`zeta covariance moment matching mixture modulus weights prescribed
response`, and `"convex" "moment constraints" "prescribed marginal"
probability measures`. Generic moment terminology led to the primary
statements above. The zeta covariance query found no matching construction;
this does not establish novelty. Entropy, transport and scenario-generation
hits were not inspected as theorem inputs and are not needed premises.

Scoped reads covered L419's weight and matrix construction, L421's
components/interface and step-163 audit, L415/L416's exact tolerances,
L422's coefficient comparison and step-168 audit, and the fixed-g0
failure. The exact two-weight proposal occurs in step 168's continuation
without a proof. No completed duplicate was found in those records.
The older capped-radial-lift failure concerns its unevaluated cubic,
not this replacement within audited L421. Neither stop is discarded.

Outcome EXPLORATION records a new bounded literature comparison, not a
mathematical advance. No parameter, new lemma or mathematical script was
derived or written. PROOF.md and DAG.md do not change. Mathematical
exploration usage remains 0 of 3; the main RH gap is unchanged.
