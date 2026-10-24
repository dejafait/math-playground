# Preferred twisted bundle — Chern-bound source assessment

TARGET: Evaluate the real-Kähler Hermite–Einstein Chern inequality for L147's rank-24 M using L152 and determine its conditional bound on |Z|.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-inequality and real-metric searches in 2026-10-04-fixed-lower-chern-stability-test.md and the 2026-10-17 normal-summand application/audit assessments; compared L147/L152 hypotheses and conclusions and targeted local failures/history; reopened the versioned primary statements and relevant HE proof cases, without repeating adequate discovery searches.
SOURCE_EVIDENCE: Perego, arXiv:1910.01867v1 (4 October 2019), Definition 3.7 p. 47, Theorem 4.19 pp. 63–65, Definition 4.20 and Theorem 4.21 p. 65, and Corollary 6.42 with its citation paragraph p. 118; complete prior HE proof coverage in 2026-10-11-nonspin-normalized-tensor-realization.md is reused.
COMPARISON: The full known inequality permits arbitrary rank and nonzero first Chern class at a real Kähler metric, and HE implies polystability without irreducibility; L115 concerns a different rank-48 determinant-trivial bundle and its numerical bound cannot be imported for M.
GAP: The separate research turn must check ASD-to-HE at the original surface metric, then evaluate the entire discriminant using L147's actual rank, first class and point-corrected second class; no evaluation or bound is established in this review.
REASON: Essential coverage now matches the saved target; use the cited theorem without a general reproof, retaining all first-Chern terms and allowing reducibility and empty Z.
SCOPE: Exactly TARGET under conditional L147/L152: identical marked K3 factors/common g and h, locally free Omega-polystable rank-two F, integral c_1(F)=0, ch_2(F)=-14e_1-21e_2-tau_D, k=(-4,-2,1,2), preferred dual HE twist, finite possibly empty Z and the actual rank-24 M. No equality-case enhancement is covered.
LITERATURE_REASON: The startup REVIEW_REQUIRED gate requires separate source-scope approval of the changed nonzero-first-class Chern application; reuse adequate known coverage rather than repeat browsing for a quota.

## Relevance and bounded test

The main gap remains universal primitive rational Hodge realization, already
unresolved on arbitrary fourfolds. The single intermediate target is the
conditional restriction on the split count from this particular bundle's
Chern inequality. Its downstream use would be a stronger necessary test for
the equality-kernel recipe, possibly compared later with independent lower
control. F existence, nonempty Z, a contradictory lower count and transverse
transport remain unresolved. An upper bound alone resolves none of them.

Continue with one numerical specialization only if the actual extended
connection supplies the inspected HE hypothesis on the same M and metric.
Check the entire signed discriminant against zero with the normalized point
class. A failed hypothesis or sign comparison stops this application; a
satisfied inequality supplies only a necessary condition. Do not replace
nonzero c_1 by degree zero or assume strict stability. No evaluation is
performed here.

## Precise standard input and inspection

Arvid Perego, *Kobayashi-Hitchin corrispondence for twisted vector bundles*,
[arXiv:1910.01867v1](https://arxiv.org/pdf/1910.01867v1),
Definition 3.7 (printed p. 47) defines HE by constant scalar mean curvature.
Theorem 4.21 and Definition 4.20 (p. 65) give HE implying polystability,
including semistability, on a compact Kähler manifold. Corollary 6.42
(p. 118) gives, for a semistable rank-r bundle on a compact Kähler n-fold,

\[
 \int_X ((r-1)c_1^2-2r c_2)\wedge\sigma_g^{n-2}\leq0.
\]

There is no zero-c_1, irreducibility or integral-polarization restriction.
Use trivial twisting cocycle and zero auxiliary B-field for ordinary M.
The whole corollary and its proof/citation paragraph were read. It refers
to Kobayashi, *Differential Geometry of Complex Vector Bundles* (1987),
Chapter IV, Theorems 4.7/5.7, and Lübke–Teleman (1995), Theorem 2.2.3 and
Corollary 2.2.4; these books were not newly inspected. Theorem 4.19's
saturated-subsheaf slope argument and equality splitting/extension and
rank induction were reopened, reusing the prior complete proof assessment.
No general theorem is reproved here.

## Local specialization obligations and duplicate/failure comparison

L147 supplies an ordinary locally free M, rank 24, integral c_1=-4k,
c_2=(55-|Z|)eta, k^2=-14 and integral_B eta=1. In particular its
nonzero first class survives even though k.h=0. Its top-image residue
fields enter the middle character with the recorded positive correction;
no hull defect may be inserted or removed. Audited L152 supplies the
smooth positive metric and ASD Chern connection on this very M over all B.
The next research step must state explicitly the Kähler-surface
ASD/primitive-(1,1) bridge and the resulting HE factor before applying
the source. This is a known surface linear-algebra specialization covered
by the reused real-Kähler assessments, not a new extension theorem.

The 2026-10-17 application/audit assessments cover L115's real-metric
Chern input; the 2026-10-04 assessment retains the full discriminant even
though its own later application set c_1=0. Neither supplies the requested
rank-24 evaluation. Histories 469/471 preserve L147's bookkeeping only;
histories 491/493 explicitly defer the new inequality. No duplicate of
this evaluation was found in these scoped records.

ATTEMPTS/066 rejects reflexivity as automatic chosen-metric extension;
this target instead uses audited L152. ATTEMPTS/067 rejects duality alone
as a defect bound; the proposed additional input is a curvature inequality.
ATTEMPTS/086's arbitrary twisting-metric obstacle remains parked: L152
uses the separately assessed preferred dual HE metric. These failures
remain evidence and are not global bans. No cross-notebook input is used.

## Classification and Mathlib

This is literature-only theorem comparison and source approval. The next
application is REPRODUCTION of known tools; no novelty is inferred from
the absence of a matching local numerical calculation. Full Mathlib
coverage of the HE/Chern theorem and this specialization was not checked;
unknown availability is not evidence of absence. No lemma, mathematical
script, new inequality, evaluated split-count bound or Hodge class is
created in this step.
