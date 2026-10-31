# Proposed independent audit of the banded leading-coefficient diagnostic

TARGET: Audit L566's four-coefficient Hermite Gram construction for every N>=3 and its actual N=2 obstruction, including all free entries, singular PSD cases, exact rational coefficient enclosures and the unbounded-cutoff qualification.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact Hermite/banded-Gram, stronger univariate SOS and sparse-PSD searches in 2026-10-31-hermite-banded-gram-diagnostic.md; compared L566 hypotheses and its certificate specification with the ready L564/L565 coverage and recorded diagnostic stop. No repeated discovery search or novelty inference.
SOURCE_EVIDENCE: Reuse inspected Gatermann–Parrilo math/0211450v1 Lemma 2.1/Theorem 3.3, Laurent 2008 Lemmas 3.1/3.5/3.8 and Vandenberghe–Andersen section 9.1/Theorems 9.2/10.1 with proof cases from the parent assessment; reopened O’Sullivan 2007.13582v2 section 2 finite formula and Romik 1902.06330v3 Theorem 2.1; ready L564/L565 assessments supply actual-coefficient integral, positivity and kernel normalization. Precise versions and links below.
COMPARISON: Known Gram equivalence, finite Hermite normalization and actual coefficient inputs cover the audit framework; no cited source supplies L566’s four-coefficient construction or its exact actual N=2 interval certificate. Audit that finite specialization and implementation, without reproving the imported framework or treating PSD completion as zero-filled PSD.
GAP: Source approval is complete; independent verification of equations, every free entry, singular cases, rational rounding/exponential enclosures and both moment tails remains the mathematical task. Full large-cutoff Gram identity and signed Xi transfer are outside scope.
REASON: The newly specified audit uses the same assessed hypotheses and known framework; its new certificate uses elementary exact arithmetic and calculus rather than an unread external theorem. This separate literature-only comparison clears the gate, without certifying L566.
SCOPE: Ready for the exact TARGET only, including all integers N>=3, actual N=2 and comparison with L564 cutoffs N>=64; subsequent REPRODUCTION audit. No full Gram construction, stronger Xi sign, lower-coefficient search or new mathematics is approved.

The main gap remains actual-Xi all-degree positivity. The intermediate
audit would accept or repair the new diagnostic limit before any
further investment in a restricted Gram certificate. Essential local
inputs are L566 and L564, the actual b_(2n) and inherited L018–L020
normalization. L565 is a contrast and historical stop, not a direct
input to L566. No cross-notebook input is needed.

The completed result claims that the four-coefficient test passes
every N>=3 through an explicit PSD matrix, while N=2 fails by a
negative actual discriminant value. The bounded audit should verify
the exact equations and square completions, replay the saved rational
certificate with its exponential enclosures and both tails, and
check the N=2/N>=3 and L564-cutoff qualifications. A discrepancy must
be repaired and its route effect recorded. Passing means only that
the diagnostic limit is sound; it does not prove lower-coefficient
matching, a signed Xi margin, higher positivity or RH.

Proposed routing after approval: proof_audit/routine_audit, standard,
high. This is finite coefficient bookkeeping, exact arithmetic and
ordinary hypothesis/tail verification, not a new creative mechanism
or complete-candidate review. The preceding research outcome is complete
independently of this continuation's separate source gate. Mathlib
coverage remains not checked.

## Separate source-scope approval (2026-10-31)

LITERATURE_REASON: The supervisor required separate approval of the newly specified audit; the difference is its finite coefficient construction and rational implementation, not a changed Hermite family or a new analytic sign theorem.

The ready parent comparison is
[the banded-Gram assessment](2026-10-31-hermite-banded-gram-diagnostic.md).
Its inspected primary statements and essential proof cases are reused:
Gatermann–Parrilo, [arXiv:math/0211450v1](https://arxiv.org/pdf/math/0211450v1),
Lemma 2.1, pp. 4–5, concerns a real polynomial and a real PSD
coefficient-matching Gram matrix in a complete degree-bounded basis;
Theorem 3.3, pp. 7–9, assumes an invariant convex feasible set under
a finite orthogonal group action. Neither imposes the extra bandwidth.
Laurent, [author manuscript dated 2008-02-05](https://homepages.cwi.nl/~monique/files/moment-ima.pdf),
Lemmas 3.1/3.5/3.8, pp. 22–25, supplies the stronger unrestricted
univariate SOS comparison, not a matching banded matrix.
Vandenberghe–Andersen, [DOI 10.1561/2400000006](https://www.seas.ucla.edu/~vandenbe/publications/chordalsdp.pdf),
section 9.1, pp. 337–338, includes zero pivots with zero coupling;
Theorem 9.2, pp. 340–341, concerns sparse zero-filled PSD matrices,
whereas Theorem 10.1, pp. 356–357, concerns PSD-completable partial
matrices on a chordal pattern. The parent inspected both proofs.
The author PDF remains accessible; this turn does not repeat its
full proof review. The audit must verify the written square
completions on the actual zero-filled matrix, including zero rows.

O'Sullivan, [arXiv:2007.13582v2](https://arxiv.org/html/2007.13582v2#S2),
9 December 2020, opening of section 2, was directly inspected again:
the generating function is exp(2Xt-t^2) and the displayed finite
formula applies at nonnegative integer degree. This fixes the basis
and excludes using negative indices at boundary cases. No Jensen
hyperbolicity or asymptotic theorem from that paper is needed.
Romik, [arXiv:1902.06330v3](https://arxiv.org/html/1902.06330v3#S2),
5 May 2019, Theorem 2.1/(2.2)–(2.3), was reopened: it gives the
alternating even-Hermite expansion with compact-dependent constants.
The exact coefficient integral (2.1), positivity immediately after
it, kernel (1.8) and normalization are reused from the inspected
L564/L565 assessments, not inferred from asymptotics. L566's finite
audit does not require a moving-interval convergence import. Its
beyond-six moment estimate invokes the audited L564 full-kernel
envelope, whose specialization must be checked locally in the audit.

The additional exact-integration specification uses elementary
integer/rational order arithmetic, Taylor's theorem with remainder,
the alternating-series theorem, monotonicity, the arctangent addition
identity and integration by parts. These are standard named inputs;
there is no specialized quadrature theorem to retrieve. The future
audit must check their actual domains, outward rounding, argument
reduction, reciprocal positivity, branch selection, all finite panels,
the omitted theta-index tail and the entire spatial tail. The script
and saved certificate have NOT been replayed or verified this turn.
The written numerical bounds and square completions remain claims
to audit, not source conclusions approved by this assessment.

The recorded L566 attempt stop parks only the four-leading-coefficient
diagnostic. L565's audited diagonal-CD obstruction is a distinct cone
and remains contrast only. No duplicate source theorem was found in
the reused comparison that would replace this finite audit; that
bounded statement is not an originality claim. Existing unfinished
proofs, scripts and certificates are preserved.

Accept the audit only after checking every relevant coefficient and
PSD case and the complete exact enclosure evidence; repair or qualify
any discrepancy. Passing authorizes retaining only L566's stated
N>=3 leading feasibility and N=2 failure. It does not exclude full
large-cutoff feasibility or establish a Xi sign. Essential inputs
remain L566, L564 and inherited L018–L020; no cross-notebook result.
Mathlib coverage is unknown/not checked. This review creates no lemma,
calculation or argument change. The next turn defaults to the same
approved mathematical audit rather than another approval turn.
