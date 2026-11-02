# L613 full triangular contrast: approved audit scope

TARGET: Audit L613's full weighted triangular-contrast O(T) bound, including all ordered multiplicities, the convolution representation and both tails.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the unchanged exact-target searches in 2026-11-01-charged-block-triangular-contrast.md and the full-pair scope comparison; read L613, corrected L612 hypotheses/conclusion, the fixed-contrast and direct-transfer stops. No broader theorem search is needed for this audit.
SOURCE_EVIDENCE: Directly inspected BGST https://arxiv.org/html/2306.04799v1 Section 3 (3.1)–(3.4), complete Lemma 5 proof, and (4.3); https://arxiv.org/html/2501.14545v3 Section 3 MT, correction footnote and cumulative proof (3.3)–(3.5). Corrected L612 supplies only the finite parameters. Exact audit scope is approved below.
COMPARISON: BGST supplies the entire triangular transform and actual-zeta fixed-test error scale, not L613's finite-family bound. The audit must check the new integral specialization without applying an actual-zeta theorem to artificial points.
GAP: L613's analytic and finite-multiplicity argument remains independently unaudited. Source coverage is ready, but no inspected source supplies its uniform finite bound, and this review does not certify it.
REASON: Before reusing the negative diagnostic, independently test the exact weight, finite expansion, removable values, uniformity and error-scale comparison, using the already available literature rather than a broad new search.
SCOPE: Exactly the stated L613 bound and corrections within that finite problem; no new test function, different model, charge conversion, all-test compatibility or actual-Xi theorem.

## Exact audit and bounded decision test

Compare the imported transform and theorem hypotheses with the saved
primary-source evidence. The entire transform in L613 is evaluated at
complex arguments, whereas the Cauchy-weight integral has the open strip
|Re u|<2. Its tail computation uses F_A(2), not the weight at its pole.
Confirm that every pair difference lies inside that open strip and all
interchanges are absolutely integrable. Preserve the exact q_A, gamma_0,
integer floor, gamma_n endpoint and collapsed multiplicity two.

Replay the complete ordered-pair identity, the central cancellation at
x=0 and bounds up to 3L/2, then BOTH exponential tails and every constant
in the explicit O(T) upper bound. Do not infer that O(T) is the actual
order or that either artificial multiset meets the BGST main term.
Accept only a uniform little-o comparison with T sqrt(log T), or record
the specific failed estimate and repair/reject the precise conclusion.

Inputs are L613, corrected L612 and the cited BGST transform/error
interface. C464c and L018 remain interpretation only. The main gap is
actual-Xi all-degree signs at unbounded heights; charge conversion,
complementary pairs, model normalization, Xi realization and initial
signs remain unresolved. A valid negative diagnostic parks only this
fixed contrast at this source error scale. No creative continuation is
prepared by this nomination. Full and supporting Mathlib coverage is
not checked. The exact target now has source/scope approval for a separate
mathematical audit; no bound has been replayed in this literature turn.


## Separate source/scope review — 2026-11-01

LITERATURE_REASON: The supervisor requires separate approval of the newly
nominated L613 audit; the underlying fixed contrast and sources have not
changed. Reuse the prior duplicate searches and failure comparisons.

The v1 source uses the negative-exponent Fourier convention and a fixed
real-even L1 test supported in [-1,1], Lipschitz at zero. Lemma 5 evaluates
the complete multiplicity-counted actual-zeta pair sum. Its proof treats
the peak at zero by Lipschitz continuity. Equation (4.3) gives the triangle
and squared-sinc pair. This covers the imported transform, including the
compact-support complex-argument interface; it does not cover L613's
convolution or lattice estimate. The source's general sentence after
(3.1) about arbitrary L1 transforms is not an unrestricted entire-extension
theorem; only its compactly supported test is used here.

The v3 correction footnote preserves the earlier Lemma 5 application.
The cumulative proof (3.3)–(3.5) supplies the additive error benchmark.
This review imports that statement, without re-auditing its analytic
number-theory proof or using its dyadic extension. No theorem is applied
to the artificial families. Version URLs and equation labels identify
these sources despite their differing HTML header/manuscript dates.

SPECIALIZE approves checking the difference not supplied by those known
inputs: L613's finite-family bound under its exact hypotheses. Retain all
checks in the bounded test above. In particular the entire transform's
value at 2 cannot justify evaluating the Cauchy-weight integral there.
The audit must check the open strip, the finite ordered-pair identity,
central cancellation and both tails, then accept the uniform little-o
comparison or identify the precise repair/rejection. These are pending
checks, not conclusions of this review. The elementary weight integral
and inequalities need replay because the exact weight and constants are
load-bearing; a reproof of the imported transform is unnecessary.

The fixed-contrast stop and the earlier signed-complement obstruction
remain distinct. Neither establishes an all-test nonimplication. A sharper
source error or a different observable would need new assessment. The
main actual-Xi gap and unresolved assumptions above are unchanged.
Mathlib coverage remains not checked. This is scope approval with no
new mathematical evidence, reported STALLED; next work defaults to the
approved mathematical audit, not another source review.
