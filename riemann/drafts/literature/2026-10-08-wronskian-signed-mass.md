# Proposed signed-mass consequence of the actual Wronskian moments

TARGET: Assess whether L380, L381 and L320 force both signs of the actual normalized Wronskian on every sufficiently high dyadic interval, with quantitative lower bounds for both signed masses.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the two prior Wronskian assessments and searched exact signed-Wronskian terminology plus standard Lp interpolation; inspected Tao primary statements and relevant proof cases, and Mathlib Holder documentation.
SOURCE_EVIDENCE: Tao, 245B Notes 3 (9 January 2009), Proposition 3 and infinity-endpoint qualification; 245C Notes 1 (30 March 2009), Lemma 9 and Holder proof; L380 (2), audited L381 (1), L320 (4) with complete strip proof, L366 (1)-(2), L368 (3)-(5).
COMPARISON: Known Holder interpolation covers the absolute-mass mechanism; no inspected source states the actual signed-mass theorem. The fixed-strip normalized jet envelope and signed-part comparisons remain a separate mathematical application.
GAP: Both actual signed masses remain unproved; establish a fixed-strip envelope with exponent below one half, retaining gamma normalization and derivative disks, then compare with the complete first-mean error. Noncommon localization remains independent.
REASON: Essential endpoint-inequality coverage is now adequate; reuse existing moment and gamma coverage for a bounded specialization without a fourth moment or new general inequality.
SCOPE: The fixed actual Wcal of L380/L381, ordinary real derivatives, H tending to infinity, and signed masses H^(-1) integral_[H,2H] max(plus-or-minus Wcal,0); no RH, simplicity, noncoincidence, discriminant or common-zero premise.

Main gap: global actual-theta mixed positivity and the total L367 margin.
This intermediate target concerns signed mass, a potential input to later
localization. Reuse the prior comparisons in
`2026-10-08-actual-wronskian-noncommon-zeros.md` and
`2026-10-08-wronskian-second-moment.md` without repeating broad discovery.
Check standard Hölder/Cauchy–Schwarz interpolation and the exact hypotheses of
any imported sign criterion; no new fourth moment or phase window is presumed.
Compare the absolute first-mean error with the lower absolute-mass scale
permitted by the second moment and a justified pointwise jet bound. Any use
of L320 must fix its strip parameter first and include derivative disks,
gamma normalization and the full right-line series.

Essential input IDs: L380, L381, L320, L368. Existing L373 is the recorded
common-zero reset obstruction, not a mathematical premise of a signed-mass
estimate. Reuse that warning: both signs do not locate a zero away from common
F_0,G zeros. The response-grid absolute-margin and first-mean signing failures
remain recorded; this proposal uses the second moment and asks a different
question, not a sign for the small first mean.

Continue only if the inspected standard inequality plus the proved envelopes
can separate both signed masses from zero at a stated scale. If the available
envelope cannot dominate the first-mean error, record that exact comparison
and choose another independently testable localization input. No scale,
constant, inequality application or conclusion is proved in this proposal.
Global positivity, total margin, low indices, heights above forty and endpoint
margin remain open. Full matching Mathlib coverage is not checked.

## Completed source comparison, 2026-10-08

The preceding proposal records the scope before review; its absence-of-proof
qualifications still apply. LITERATURE_REASON: the newly proposed target
required essential unread endpoint-inequality coverage after the moment audit.
No actual-family envelope or signed-mass conclusion is derived in this review.

**Primary inequalities.** Terence Tao, [245B, Notes 3: Lp spaces](https://terrytao.wordpress.com/2009/01/09/245b-notes-3-lp-spaces/),
9 January 2009, Proposition 3: on a measure space, for 0<p,q<=infinity,
f in Lp and g in Lq, the product belongs to Lr and its norm is at most
the product of the norms, where 1/r=1/p+1/q. Read the statement and
proof through normalization and convexity. The theorem includes infinity;
the proof explicitly leaves that endpoint as an exercise. The proposed
application uses this endpoint, not an assumed fourth moment.

Tao, [245C, Notes 1: Interpolation of Lp spaces](https://terrytao.wordpress.com/2009/03/30/245c-notes-1-interpolation-of-lp-spaces/),
30 March 2009, Lemma 9, assumes 0<p0<p1<=infinity and membership in
both endpoint spaces. It bounds the intermediate norm by geometric
interpolation of endpoint norms when reciprocal exponents interpolate.
Read norm definitions, statement and first Holder proof; here too the
infinity-endpoint proof modification is left to the reader. This is
standard inequality coverage, not a theorem about the actual zeta pair.

The intended measure is dt/H on [H,2H]. Wcal is real and continuous
there since A>0, so endpoint membership holds; quantitative supremum
control does not follow from continuity. The application should cite the
known inequality and write its endpoint applicability explicitly. A
reproof of general interpolation is unnecessary. No signed conclusion
for Wcal is imported from these sources.

**Local applicability comparison.** Read the complete L320 (4)-(5) strip
proof: polynomial preliminary growth, reflected boundary, damped rectangles
and sequential limits. R must exceed 1/2 and be fixed before H varies.
For the application choose R=3/4 and disk radius 1/8 about 1/2+it.
The prospective test is sup_[H,2H]|Wcal| <= C H^(3/8), not an estimate
proved here. The mathematical turn must bound F0 and F0' using the entire
completion on these disks, divide by the real A at the disk center,
retain bounded height shifts in the exponential decay, and use the full
right-line response jets. L366 (1) fixes F0=2 xi(1/2+it); its (2)
already bounds G,G'. L368 (3)-(5)'s carrier and complete Dirichlet
series were read to check their normalization and absolute convergence.
No zero-free, central-value lower bound or derivative of an uncontrolled
asymptotic remainder is allowed.

The candidate scale to test for each normalized signed integral is
H^(-3/8) log H. The competing error is the complete proved
O(H^(-1/2)(log H)^2) in L380 (2), rather than its smaller positive
diagonal. No value of a signed mass, constant or onset is asserted here.
The unchanged audited moments do not require reproof or source refresh.

**Duplicates and recorded failures.** Targeted searches in current
Wronskian drafts, assessments and histories found only the proposed
signed-mass continuation. Read the first-mean ATTEMPTS record: L380 stops
signing the mean itself, not an absolute-mass argument using L381. Reused
the previous noncommon-zero assessment's Bui–Hall comparison; its different
Hardy-derivative sign-set theorem is not imported for this pair. L373's
common-only reset obstruction remains: both signs need not give a zero
away from common F0,G zeros. Response-grid and sharp-discriminant stops
are preserved. A failed search is not evidence of originality.

Queries actually submitted: `site.mathlib.org integral_mul_le_Lp_mul_Lq holder`;
`site.terrytao.wordpress.com log convexity Lp norms Holder interpolation`;
`"zeta" "Wronskian" "signed" moment`. No matching actual signed-mass
theorem was inspected. An unrelated external notebook search hit was not
read or used. Young, Bui–Hall, gamma and Dirichlet coverage is reused from
the two prior assessments named above; no changed source hypothesis needs
another extraction.

**Mathlib.** Inspected supporting [Holder documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/Holder.html#MeasureTheory.Lp.norm_smul_le).
`MeasureTheory.Lp.norm_smul_le` assumes a HolderTriple and bounds the Lp
scalar-product norm. `MeasureTheory.eLpNorm_le_enorm_mul_eLpNorm_mul_eLpNorm`
requires a continuous bilinear map and almost-everywhere strong measurability.
These are supporting inequalities, not full matching coverage of the actual
signed-mass theorem; the latter is not checked. No Lean verification or
library absence is claimed.

**Decision and stopping test.** SPECIALIZE: import known inequalities,
then verify the actual envelope and signed-part algebra in a separate
research turn. Continue if the justified absolute-mass scale dominates
the entire mean error and separates both signed masses from zero. Stop
this certificate if it cannot meet that comparison. Even success supplies
no noncommon witness, discriminant sign or RH conclusion. The separately
saved application assessment awaits the supervisor's next-turn approval.
