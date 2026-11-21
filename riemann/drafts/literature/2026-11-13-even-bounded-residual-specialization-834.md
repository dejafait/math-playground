# Complete even operator — fixed-shift bounded-forcing specialization

TARGET: Specialize the killed-reference and bounded-perturbation theorems to C759a's complete even operator at shift32, proving an explicit finite L-infinity resolvent bound for every real even bounded g or identifying the failed hypothesis, with both poles and all five prime shifts retained.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse completed assessment833 comparison834's exact-target searches, local duplicate/failure screen and primary theorem comparison; no changed operator, forcing class, parameter or mechanism is nominated.
SOURCE_EVIDENCE: Direct primary sources https://www.math.tecnico.ulisboa.pt/~czaja/ISEM/14internetseminar201011.pdf and https://arxiv.org/html/1107.0745v1 ; assessment833 records GR1107.0745v1 Section2(2.1)-(2.4) and killed formulas; reused FOT second edition4.4.2-4.4.3 and Engel-Nagel2000 III.1.3/1.9-1.10; fresh Jacob-Zwart2010-11 Proposition5.2.4(a), pp59-60, full proof, and Theorem10.2.1,p124. Its exact URLs and access qualifications are preserved there.
COMPARISON: This is an application of known killed-reference contraction, bounded perturbations and the Laplace-resolvent theorem. L515 covers a convolution-only eigenfunction method, whereas this test retains the actual complete pole and every bounded forcing. The remaining work is the identified specialization, not a new general theorem or smoothing mechanism.
GAP: Exact supported reference/form identity, consistent L2/L-infinity perturbation action, stronger-norm limit, explicit perturbation/growth budget below32 and final finite constant must be established. No value of the constant or successful budget is asserted.
REASON: A verified unsigned bounded-residual estimate could supply one ingredient for a future error enclosure. It would not prove isolation, simplicity, boundary-relative positivity, parity ordering or actual-Xi mixed positivity. Failure of this sufficient budget stops this test only.
SCOPE: One mathematical specialization on (-1,1), real even bounded g, with the inverse initially interpreted in L2. No shift/dimension/forcing sweep, complete-semigroup order assumption, ordinary Green-kernel representation, spectral-gap claim or eigenfunction sign proof. Source-link repair and separate literature approval835 completed; the mathematical specialization remains unperformed.

## Exact application and bounded decision test

Use C759a(1),(5)-(6), Proof1/3 for the complete form, supported core
and integrable digamma remainder; C759h Proof1-2 for the complete
even pole and actual action. Use L515 only for its reference/core
and standard L2 construction with their existing qualifications,
not as an already proved full-Q bound. L741(13),(16) gives the
remainder normalization if needed; its causal generator is different.
Recorded C759i/C759j stops remain in force as contrasts.

Prove the exact form/operator comparison with the smooth-core killed
reference, rather than identify operators through symbol growth.
Account for scalar, integrable remainder, all zero-extended prime
translations and both original poles. The even finite-rank pole must
be treated as a bounded operator; no convolution representation of it
is supplied. Establish compatible action on equivalence classes of
bounded data and L2 data, and justify the stronger norm passage in
the chosen standard Dyson/Laplace or reference-resolvent method.
Do not apply a C0 theorem directly on L-infinity without its hypothesis.

The test seeks an explicit finite M for
||(A_e+32I)^(-1)g||_infinity <= M||g||_infinity
for every real even bounded g. Compute a justified strict budget
below32 for the selected known-method implementation. If it works,
state all constants and the L2 inverse identification in one canonical
result. If it fails, preserve the exact failed hypothesis or bound;
do not change the parameter or claim that no such estimate exists.
No mathematics for this application was performed in review834.

Full matching Mathlib coverage is unchecked. No original source theorem
needs reproving. The full-pole and consistent-space specialization is
needed because it was excluded from L515 and from the October30 model
assessment. All essential source premises for this bounded test are
available in completed assessment833; there is no source-blocked
premise to defer silently. Independent spectral and Xi gaps stay open.

## Source-link recovery and separate approval835 — 13 November2026

LITERATURE_REASON: Supervisor recovery explicitly requires direct source URLs
in this ready assessment. The target and mathematical assumptions are unchanged;
this is a link repair and approval of assessment834, not a new comparison claim.

Direct primary sources:
- [Jacob–Zwart, 14th Internet Seminar, 2010–11 course PDF](https://www.math.tecnico.ulisboa.pt/~czaja/ISEM/14internetseminar201011.pdf),
  Proposition5.2.4(a), printed59–60 (PDF pages66–67), and Theorem10.2.1,
  printed124 (PDF page132). The primary PDF opened successfully this turn;
  theorem locations were checked. Reuse assessment833's full relevant proof
  inspection and exact Hilbert-space/growth hypotheses; no new proof read or
  new L-infinity conclusion is claimed by this repair.
- [Grzywny–Ryznar, arXiv:1107.0745v1, 4 July2011](https://arxiv.org/html/1107.0745v1),
  Section2, equations(2.1)–(2.4) and subsequent killed-process formulas.
  The primary HTML opened successfully; reuse assessment833's inspected
  reference normalization and killed-kernel coverage.
- [Engel–Nagel, One-Parameter Semigroups, GTM194, 2000](https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf),
  III.1.3 and III.1.9–1.10, with unchanged prior coverage and retrieval
  qualifications in assessment833. No repeated failed retrieval is needed.
  FOT second revised edition4.4.2–4.4.3, printed173–175, remains reused
  prior coverage, not a newly accessed source.

The existing duplicate and failure comparison in assessment833 is reused:
L515 excludes this complete-pole, all-bounded-forcing assertion; C759i/j
and stops829/831 do not settle the unsigned norm question. No novelty
inference, new mathematical result, or change of method follows from adding
links. SPECIALIZE is retained for the exact TARGET. This separate literature
turn approves the saved continuation's source coverage while leaving every
operator identity, consistency, strict budget and final constant obligation
in the application unproved. Full matching Mathlib coverage remains unchecked.
