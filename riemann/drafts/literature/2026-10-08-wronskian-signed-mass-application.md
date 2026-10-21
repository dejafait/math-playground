# Covered signed-mass application

TARGET: Prove quantitative lower bounds for both signed masses of the actual normalized Wronskian on every sufficiently high dyadic interval using L380, L381 and the fixed-strip envelope of L320.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed bounded search and duplicate/failure checks in drafts/literature/2026-10-08-wronskian-signed-mass.md; no novelty claim.
SOURCE_EVIDENCE: Tao, 245B Notes 3 (2009-01-09), Proposition 3, https://terrytao.wordpress.com/2009/01/09/245b-notes-3-lp-spaces/; Tao, 245C Notes 1 (2009-03-30), Lemma 9, https://terrytao.wordpress.com/2009/03/30/245c-notes-1-interpolation-of-lp-spaces/; infinity-endpoint qualifications inspected 2026-10-08; local applicability details in the completed comparison.
COMPARISON: Standard Holder covers the absolute-mass mechanism; the actual normalized jet envelope and signed-part comparison require a mathematical specialization. No source states the actual signed-mass result.
GAP: Neither signed-mass bound is proved; common-free localization, common-zero counts and the total discriminant margin remain independent.
REASON: Ready coverage supports one bounded mathematical application without a new moment theorem or general inequality reproof.
SCOPE: Fixed actual Wcal=(F0'G-F0G')/(A^2 T^2 L), T=1+t, L=log(2+t), ordinary real derivatives, normalized dt/H on [H,2H], H tending to infinity; no RH, simplicity, noncoincidence or discriminant premise.

This newly saved continuation requires separate supervisor approval next
turn and makes no mathematical assertion. The full primary hypotheses,
endpoint-proof qualifications and source versions are in
[the completed comparison](2026-10-08-wronskian-signed-mass.md).

Essential input IDs: L380, L381, L320, L366 and L368. Cite the existing
moments and known Holder inequality. Fix R=3/4 and disk radius 1/8 before
H varies; test sup|Wcal| <= C H^(3/8) and each signed mass
>= c_* H^(-3/8) log H, with c_*>0. These are proposed thresholds only.
Write the Cauchy derivative estimates, bounded height shifts and real
center gamma normalization; retain full response jets, the complete
first-mean error and second-moment little-o term. Constants and onset may
remain existential but must be uniform in H. No zeta division is allowed.

Continue if the absolute-mass lower scale dominates the full mean error
and both signed masses are separated from zero. Otherwise record the
exact failed comparison and stop this certificate. L373's common-only
reset warning remains even after success. Global mixed positivity, total
L367 margin, low indices, heights above forty and endpoint margin remain
open. The intended classification is REPRODUCTION of known inequalities
and existing local inputs; no originality is claimed.

## Direct-source recovery, 2026-10-08

Reopened the two primary URLs above only to verify and expose the exact
source statements for this unchanged target. Proposition 3 assumes a measure
space, endpoint membership for exponents in (0,infinity], and reciprocal
exponent addition. Its finite-exponent proof uses normalization and convexity;
the infinity case is explicitly left as an exercise. Lemma 9 assumes
0<p0<p1<=infinity and membership in both endpoint spaces, and states
log-convex interpolation in the reciprocal exponent. Its first proof uses
Holder; its infinity-endpoint modification is also left to the reader.
Thus the endpoint qualification recorded in the completed comparison is
retained, not silently upgraded to an inspected written endpoint proof.

The intended application has normalized measure dt/H on a compact dyadic
interval and a continuous real Wcal with positive A. This supplies qualitative
endpoint membership only. The quantitative Cauchy envelope, signed-part
application and comparison with the complete first-mean error still require
the separate mathematical step. Existing duplicate checks, moment-source
assessments and failure records are reused unchanged; no broad search or
new result is claimed. Supporting Mathlib coverage remains as documented
in the completed comparison; full actual-family coverage is not checked.

This repairs the direct-URL process defect. SPECIALIZE and the exact TARGET
are unchanged. No lemma, mathematical script, mathematical argument or
exploration counter changed.
