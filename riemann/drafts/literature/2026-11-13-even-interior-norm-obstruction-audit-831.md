# Concentrating-family obstruction — approved audit coverage

TARGET: Critically audit C759j's full-operator concentrating-family obstruction to unrestricted L2-residual-to-interior-sup control, checking domain, the entire Fourier tail, both poles and all five compressed prime shifts.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step832 reuses assessment829/approval830 and assessment828's exact-target searches; compared C759j with C759a Proof1/3, C759h Proof1-2 and recorded stops822/823/826/829/831. Same family/operator; no new broad query or exhaustive coverage claim.
SOURCE_EVIDENCE: Reopened the author-hosted Teschl2014 second edition GSM157, Section7.1, equation7.3, Lemmas7.1/7.2, Theorem7.5 and Lemma7.6, printed pp187-190 (PDF198-201 zero based), https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf; read applicable hypotheses and norm/identification proof cases. Reuse829's local operator coverage; C759j remains unaudited.
COMPARISON: The Fourier imports cover norm and integral identification; C759a/h specify the actual operator. Neither is a citation of C759j's full concentrating-family estimate. Only that existing specialization's domain, arithmetic and logical replay is approved, classified REPRODUCTION.
GAP: Source scope is approved separately in832; independent verification of C759j(1)-(12) remains pending. Eigenfunction sign, restricted-error estimates, spectral isolation and Xi transfer remain uncovered by this audit.
REASON: The saved target stays unchanged and requires an audit before use. Existing sources suffice for its replay, without repeating searches or importing an unread embedding theorem.
LITERATURE_REASON: This newly nominated audit was REVIEW_REQUIRED at invocation; separate source approval is required. Reuse ready829/830 coverage and check the exact audit scope; no new mathematical target or extended literature survey.
SCOPE: C759j's single family h(s)=(max(1-s^2,0))^2, f_epsilon(x)=h(x/epsilon), 0<epsilon<1/8; complete even C759a operator on (-1,1), shift16, interior(-1/4,1/4), both poles and n=2,3,4,5,7. No sweep, spectral projection, eigenfunction conclusion or new norm-conversion mechanism.

The original831 nomination required a separate source comparison;
step832 supplies that approval below. It does not approve the proof's
correctness. No lemma or mathematical script was modified in832.

Audit the canonical C759j proof: C759h's H1_0 action criterion, integral
substitution and two actual integrations by parts, the full low-frequency
and tail integrals (7), multiplier scaling (8)-(9), compression (10),
and both poles (11). Check the nonzero denominator and that only an
unrestricted domain inequality is excluded. Accept if these pass, or
identify and repair/reject the precise faulty estimate. No parameter,
basis or forcing sweep or stronger sign claim is authorized. Full
matching Mathlib coverage is unchecked.

## Separate source comparison832 — 13 November2026

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target is the independent audit of this one norm
obstruction. Its downstream use is to decide whether the unrestricted
residual-to-interior-uniform ingredient is excluded; it cannot supply
ground-state sign or a restricted-error estimate. Parity, spectral
isolation, boundary-relative control and Xi realization remain separate.

The [primary source](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf)
was reopened at the cited locations. Equation7.3 uses (2pi)^(-n/2).
Theorem7.5 extends the transform unitarily to L2; the norm proof uses
7.10, density and continuity. Lemma7.6 assumes L1 intersect L2 and
identifies the extension with the integral; both its bounded-support
approximation and general truncation cases were read. Lemmas7.1/7.2
are Schwartz-only: their derivative and positive-dilation statements
cannot simply be applied to the proposed piecewise polynomial.
The future audit must check its own substitution and integrations by
parts, maintaining dt/(2pi). The unrelated transform-spectrum claim
is not an input. This is reuse of the precise2014 citation, not the
different numbering of C759h's2009 resolvent reference.

Read C759j solely to map its obligations to that coverage. C759a(1),
(5)-(6),Proof1/3 and C759h Proof1-2 supply the existing local closed
form, multiplier, bounded perturbations, H1_0 action and floor to replay.
No new external operator theorem is needed for this bounded audit.
Check their actual stated hypotheses, rather than identifying the
compression with a periodic or Dirichlet multiplier. Their numerical
certificate is unnecessary if the coarse C<4 used here is established
from the displayed coefficients; do not rerun the unrelated256-mode
weak-pair solve or treat a diagnostic preview as verification.

Assessment828's completed searches remain adequate: its generalized
embedding leads were not inspected necessity theorems and remain
unimported. Stops822/823 concern a missing ordinary kernel and an
inconclusive weak pairing; stop826 concerns order preservation; stop829
parks the direct weighted sign implementation. None settles this norm
audit. Stop831 records the existing concentration claim pending audit;
repeating its bump calculation as a new discovery is not authorized.
There is no novelty or general nonexistence claim from these comparisons.

Accept only after every load-bearing domain/tail/scaling/perturbation
estimate and denominator justification passes independent replay. A
fault requires identification and repair or rejection of the precise
claim; an unrepairable gap leaves the obstruction unverified. Either
decision ends this audit without a sweep or stronger sign inference.
SPECIALIZE is appropriate because the needed full operator estimate
is a local application, not the statement of a cited general theorem.
No new estimate or audit verdict was derived here. Mathlib full-match
and supporting coverage remain unchecked. Outcome STALLED: source-gate
approval only, with no new mathematical or informative negative result.
