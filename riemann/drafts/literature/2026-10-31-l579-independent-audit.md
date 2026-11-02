# L579 finite-covariance obstruction: audit nomination

TARGET: Audit L579's finite-K resonant-mixture obstruction, checking the mass constraint, global phase envelope, integral and endpoint cases.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the exact finite-K searches, stronger-result comparison and failure checks in drafts/literature/2026-10-31-resonant-finite-k-relaxation.md; the audit changes no hypothesis or mathematical family and no new browsing was performed.
SOURCE_EVIDENCE: Directly rechecked on 2026-10-31 the author PDF of Rahimi--Recht (2007), Section 3, Theorem 1, equation (2) and subsequent real-phase formula, printed p. 3, https://people.eecs.berkeley.edu/~brecht/papers/07.rah.rec.nips.pdf, as qualified in the L578 assessment; Bayer--Teichmann Corollary 2 and di Dio--Schmuedgen moment-cone sources in the prior finite-K assessment are not mathematical inputs to the necessary-bound proof. L473 (6) and audited L578 (6)--(7) supply the local definitions and phase identities.
COMPARISON: The sources cover independent-phase spectral realization and supported moment representation, not the clipped threshold; L579 avoids representation sufficiency by using only a necessary variance constraint and sharp integration of the already assessed phase envelope.
GAP: Independently replay L579's amplitude-product normalization, entire-circle Taylor envelope, positive-part integration, strict rational comparison and all degenerate selector/amplitude/frequency cases; no separate audit has yet been performed.
REASON: Separate literature approval completed 2026-10-31: the unchanged audit has adequate source coverage; reuse this assessment next turn for mathematics. No new mathematical conclusion or independent proof verification is claimed.
SCOPE: Exactly L579's deterministic A,C,D in [0,4], uniform U on [-1/4,1/4], independent uniform B, fixed phi, path-constant selector independent of (U,B,V,E), and positive even supported single-wave remainder with independent uniform E, matching all 21 K entries. No family enlargement, fourth-law realization or Hardy/Xi transfer is covered.
COVERED_TARGET: Audit L579's finite-K resonant-mixture obstruction, checking the mass constraint, global phase envelope, integral and endpoint cases.

The audited L578 identity is reused without its full spectral-completion
condition: verify that its algebraic phase expansion and single-wave
identity precede and do not use that condition. L473 is needed only for
the definition of K and its variance entry, not its arithmetic imports
or nonstationary bulk. The proof's choice of a necessary subset of K
is expressly permitted by the prior finite-K assessment.

The audit must check the Taylor remainder on the stated interval and
monotonicity outside it, so that the dual bound holds on the whole
phase circle. Check the uniform-phase normalization and independence
factors before comparing the integral with 1/288. A grid is unnecessary
and insufficient. Do not infer an existing positive remainder from the
variance constraint; the theorem only bounds any law that already meets
the hypotheses. Verify the cited nonempty example separately if retained.

Continue with this stop only if the independent replay passes every
case. Repair a defect within this exact family or record it explicitly;
do not restore L578's full-spectrum density inequality to prove L579.
Full matching Mathlib coverage is unchecked, not asserted absent. A
passing audit verifies local route evidence, not an RH advance or novelty.
No new primary extraction, theorem proof or mathematical computation is
performed in this nomination; all substantive new reasoning is canonical
in L579 and remains subject to that later audit.

## Separate coverage approval, 2026-10-31

LITERATURE_REASON: The startup literature gate requires separate approval of the saved audit nomination; check its source-to-input scope against L579 before mathematical replay. No changed family or renewed discovery search is proposed.

Reused the exact searches, primary moment-theorem hypotheses and failure
comparison in `2026-10-31-resonant-finite-k-relaxation.md`, especially its
completed source comparison and approved necessary-subset test. Inspected
L579's hypotheses, conclusion and source-qualification section; L473
(6)--(7); L578's hypothesis distinction, single-wave identity and (6)--(7);
and the finite-K stop and preceding calculation/source history. This is
a coverage check, not independent verification of the new inequalities.
No duplicate theorem or contrary source was newly identified.

Directly opened Rahimi--Recht's author PDF, Section 3, printed p. 3
(PDF index 2), Theorem 1, (2) and the following real-phase construction.
The theorem requires a continuous translation-invariant positive-definite
kernel and a nonnegative spectral measure; normalization gives a frequency
probability law. The subsequent cosine construction uses a uniform phase.
It supplies neither a positive residual from finite covariance matching
nor a nonlinear clipped-mean estimate. For this audit the remainder law
is already a positive probability law by hypothesis; the source is
background coverage of that construction, not a premise for recovering
an unknown measure. The finite-sum derivative and phase claims still
require their local algebraic replay. No new specialization is derived here.

Bayer--Teichmann and di Dio--Schmuedgen are inspected background in the
prior assessment, not essential inputs to L579's necessary-bound proof;
no re-extraction is needed. L473 contributes its exact K definition only.
L578's phase identities and single-wave clipping identity are stated
independently of full completion; do not import its (5). Whether L579
uses these inputs correctly, including its claimed nonempty example,
remains for the audit. Its whole-circle Taylor envelope, integration,
strict arithmetic and degenerate cases have not been verified this turn.

DECISION remains EXPLORE for the exact saved target. Source coverage is
approved, with no new theorem, source import or claim of novelty. The
next turn should execute that audit using this unchanged assessment,
not request another coverage approval. Continue the family stop only
after every proof case passes; a failure must be repaired within scope
or explicitly recorded. Full matching Mathlib coverage remains unchecked.
