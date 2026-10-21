# Three quaternionic lines — bounded gluing specialization

TARGET: Test the r_m-1 inference from L121's local branch data by computing the normalization quotient for the reduced union of H x 0, 0 x H and diagonal H in flat H^2.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The completed opposite normalization-quotient comparison checked local duplicates and primary seminormal-union/multicross results; no exact quaternionic three-line quotient computation was identified in that bounded search, without a novelty claim.
SOURCE_EVIDENCE: Leahy--Vitulli, Nagoya Math. J. 82 (1981), Propositions 2.18--2.23, pp. 46--50, https://doi.org/10.1017/S0027763000019279; Nagoya Math. J. 83 (1981), Lemma 3.4, sequence (3.3), Theorem 3.5, pp. 141--144, https://doi.org/10.1017/S0027763000019450; Vitulli correction, Nagoya Math. J. 107 (1987), pp. 148--149, 157, https://doi.org/10.1017/S0027763000002592; reuse the complete essential proof-case reading recorded in 2026-10-17-opposite-image-normalization-quotient.md.
COMPARISON: Known criteria supply the gluing test; the identified difference is an explicit normalization-quotient calculation for this chosen linear arrangement while checking the retained quaternionic and pairwise scheme conditions. Do not reprove the general criteria.
GAP: The model's complete local quotient and simultaneous ideal condition have not been calculated here; no identification with the actual image of F is available or sought in this model test.
REASON: This independent finite local-algebra test can determine whether pairwise local data justify the parked minimal-defect formula, avoiding a dependent attempt to assume actual image seminormality.
SCOPE: Only the stated flat reduced complex-analytic/algebraic local model at the origin, for one standard induced complex structure and compatible standard hyperkahler triple; comparison with audited L118/L120/L121 is limited to local branch data, not the full global F hypotheses.

## Coverage and exact proposed test

The source review is complete in the [parent assessment](2026-10-17-opposite-image-normalization-quotient.md).
Its primary theorem hypotheses, proof cases and 1987 correction are the
coverage for this specialization. This assessment is newly written and
receives separate supervisor approval next turn; no calculation or new
lemma was performed in the source-only step that wrote it.

Use the standard flat quaternionic vector space H^2 and the three stated
candidate real subspaces, with their induced complex structures. Write
the corresponding three complex-plane ideals in one ambient local ring;
use their intersection for the **reduced union**. Verify the normalization
and the complete finite-length quotient, including every homogeneous
degree needed to justify termination. Compare its actual length with the
candidate threshold r-1=2; a finite jet preview alone is insufficient.
Check the exact simultaneous ideal condition from the inspected criterion
and every relevant local comparison with L121. The goal is a concrete
specialization of known local algebra, classified REPRODUCTION, with no
originality assertion.

The independent checks are the full quotient computation and its gluing
criterion comparison. Check smooth immersed source branches, the
normalization map and its unramifiedness, quaternionic tangent behavior,
local parametrized geodesy and the off-diagonal fibre-product structure.
These are requirements to verify, not conclusions established by this
proposal. Do not import the actual global K3 normalization, Chern tensor,
or existence of F into this flat model. Do not infer a counterexample to
the full F hypotheses or the Hodge conjecture from a model outcome.
The selected comparison also drops the actual nonflat K3 source metric
and its curvature. A model outcome cannot settle an implication that
uses those additional local metric data.

The main gap is universal primitive Hodge realization. The plausible
downstream use is to decide which additional actual-image gluing input
a collision-defect argument must retain. Continue if a complete
certificate proves that the local data suffice or supplies a model
failure of the inference; abandon this particular model if it misses
one of the local conditions being tested. Stop after this three-branch
case, without broadening to arbitrary arrangements or pursuing global
cohomology. Actual F existence, actual-image seminormality and quotient,
collision emptiness, reconstruction and transverse transport remain
unresolved. Full matching Mathlib coverage is not checked.

## 2026-10-18 separate coverage approval and process repair

LITERATURE_REASON: The supervisor requires direct source URLs in this
ready assessment; this turn repairs that omission and reuses the unchanged
parent comparison rather than repeating theorem discovery. No mathematical
calculation or model verification is performed in this approval turn.

The primary statements already inspected in the parent assessment cover
reduced rings over an algebraically closed characteristic-zero field.
For the completed local criterion, the minimal-prime quotients must be
regular, the common radical of pairwise sums must be one prime with regular
quotient, and the simultaneous identities
P_i + intersection_{j != i} P_j = P must be checked. Sequence (3.3)
computes the quotient only under its multicross hypotheses. The union
criterion tests a branch against the preceding union, not merely each
other branch. Theorem 3.5 additionally assumes weak normality; smooth
normalization and unramifiedness do not replace it. These are source
hypotheses to test in the saved calculation, not claims about this model.
The 1987 correction retains the later union criteria while correcting the
function-theoretic characterization. No general criterion is to be reproved.

Access record: DOI opens in this turn returned tool access errors. This
is not a loss of the earlier recorded full statement/proof-case coverage.
A bounded publisher search located the correction's direct
[primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/210921193603FF18CCF06D8071093977/S0027763000002592a.pdf/corrections-to-seminormal-rings-and-weakly-normal-varieties.pdf).
Its search extract was not treated as a fresh proof reading. The primary
URLs above identify the exact sources whose inspected coverage is reused.
No new source theorem or stronger comparison is claimed.

Decision: SPECIALIZE remains appropriate for the exact unchanged TARGET.
This separate approval covers the one local-ring computation and its
listed geometric checks, classified REPRODUCTION. It does not approve
any actual-image identification or extension to the global F hypotheses.
The model computation is still unperformed. Mathlib coverage remains
not checked. This process repair is STALLED as mathematical evidence;
it neither renews the exploration budget nor changes any route stop.
