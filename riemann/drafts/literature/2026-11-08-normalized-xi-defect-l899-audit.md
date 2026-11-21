# L899 normalized Xi-defect bound — audit scope

TARGET: Audit L899's normalized Xi-defect full-L1 bound, checking the zero endpoint, essential infima, Sprungk applicability and the explicit constant M=Q/(3A_0(0)).
CHECKED: 2026-11-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the prior ready assessment 2026-11-08-normalized-xi-defect-interpolation.md for exactly the same theta densities and squared-height range; step111's scoped duplicate search found no earlier matching local bound, while L898 and the recorded L309/L312 comparisons remain distinct.
SOURCE_EVIDENCE: Rechecked Sprungk arXiv:1906.07120v3 Theorem8 (printed p.10), Sections2-3 and AppendixA before (13), https://arxiv.org/pdf/1906.07120v3#page=10 ; rechecked NIST DLMF equations https://dlmf.nist.gov/4.36.E1 , https://dlmf.nist.gov/4.33.E1 and https://dlmf.nist.gov/25.6.E1 on 2026-11-08; theorem hypotheses and conventions agree with the reused assessment.
COMPARISON: L899 supplies the actual-theta applicability calculation within the previously approved scope; its separate audit is a reproduction/hypothesis check of that specialization, not discovery or an extension of the stability theorem.
GAP: Independently verify L899's product/log limit at zero, integrable p² bound, positive-measure essential-infimum argument, exact reference-density normalization and full-L1 coefficient; positivity margins and all-height signs are outside this audit.
REASON: Recovery adds missing direct primary URLs and verifies access for the unchanged audit target; source coverage is ready for mathematics, but L899 is not certified as audited. No changed mathematical hypothesis or new mechanism is introduced.
SCOPE: Only L899 with actual Phi=K(|u|)/2, 0<=v,y<=1/2, finite explicit theta-integral M and no sign premise; no numerical value, finite certificate, derivative under an unbounded integral or all-height sign transfer is requested.

The prior search record, primary theorem hypotheses, source version
qualifications and known failure comparisons remain in
[the reused assessment](2026-11-08-normalized-xi-defect-interpolation.md).
The full mathematical assertion, citations and proposed proof are
canonical in
[L899](../../lemmas/L899-normalized-xi-defect-measure-lipschitz.md).
No new proof is asserted in this assessment.

The audit should check all uses of the imported stability inequality
and its total-variation convention, the real sinh product and removable
zero, and the actual-theta positivity/decay and mass statements from
L019 and L898. L020's Xi normalization is already carried through L898.
Confirm that the conclusion uses the same normalized measure and that
no mass on a null line or oscillatory sign assumption enters. Check
the DAG's direct uses against the proof, not just its syntax.

Accept only if M is rigorously finite and the displayed full-L1 bound
holds throughout the closed parameter square with its stated factor.
If a flaw occurs, record and repair it within this same scope where
possible, otherwise narrow or withdraw the unsupported assertion while
preserving the original evidence. There is no numerical tolerance or
positive-margin target to substitute for this theorem check.

L030–L032/C032a remains the main gap. This audit cannot establish the
independent reference signs required for a later interpolation use.
L898's fixed cross-endpoint stop, the qualified L312 ordering failure,
and parked source blockers remain preserved. Full matching Mathlib
coverage remains unchecked. No cross-notebook theorem is an input.

## Recovery source check (2026-11-08, step112)

LITERATURE_REASON: The supervisor required direct source URLs in the ready assessment; this bounded retrieval repairs that omission for the saved audit, without extending its scope.

[Sprungk v3](https://arxiv.org/pdf/1906.07120v3#page=10) was
reopened at Section2 (printed p.3), Section3 (p.7), Theorem8 (p.10),
and AppendixA before (13) (p.24). The arXiv version stamp is
22 January2020; the title page is dated23 January2020.
The setting is a complete separable metric space with Borel probability
measure. Theorem8 assumes integrable real potentials, first essential
infimum zero, and defined normalized probabilities. Its coefficient is
exp(-[essinf g]_-)/Z_f, with [a]_- = min(0,a). Section3 defines
TV as half the full density L1 distance. The source directs the proof
to adaptations of Theorems5/7; AppendixA displays the likelihood
difference estimate. These inspected passages support the intended
import; applicability to theta remains the audit's obligation.

The live NIST pages were reopened at
[4.36.1](https://dlmf.nist.gov/4.36.E1),
[4.33.1](https://dlmf.nist.gov/4.33.E1), and
[25.6.1](https://dlmf.nist.gov/25.6.E1): respectively the sinh
product, sinh series and zeta(2)=pi²/6. The prior version1.2.8
record is retained; this retrieval checks those displayed formulas
without independently identifying the live release.

No additional duplicate search or theorem extension was needed: the
prior assessment's exact-target search and L898/L309/L312 contrasts
remain applicable. No lemma, mathematical script, proof overview or DAG
was changed. No Mathlib matching result was checked. Proceed to the
unchanged bounded audit; accept only if all source hypotheses and the
uniform finite constant survive, otherwise repair or narrow the claim.
