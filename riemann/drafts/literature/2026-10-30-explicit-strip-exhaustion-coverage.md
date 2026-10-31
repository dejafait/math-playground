# Explicit strip exhaustion — completed source review

TARGET: Localize every zero H_t(x+iy)=0 with 1/25<=t<=11/50, |y|<=1 and x>=4*pi*exp(10000)+3 inside an L492 disk with center X>=4*pi*exp(10000)+2.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the local-circle, phase and explicit-tail reviews and recorded extraction failures; supplemented with six exhaustion/localization and H_t/x_n queries. No matching numerical theorem was inspected. Exact queries, results and duplicate checks are in drafts/heat/2026-10-30-explicit-strip-exhaustion-source-review.md; failed searches are not novelty evidence.
SOURCE_EVIDENCE: D. H. J. Polymath, arXiv:1904.12438v2 (4 August 2019), https://arxiv.org/html/1904.12438v2 , Theorem 1.5(i)–(ii) and (26), pp.9–10; Proposition 9.1(i) with reflection, pp.56–58; Lemma 9.2 and (100)–(101), pp.58–59; (102)–(104), pp.59–60, and the complete separate exhaustion case on p.60 were inspected. The versioned PDF confirms the exhaustion location. Saddle proofs remain imported, not audited.
COMPARISON: The source covers the qualitative mechanism, including arbitrary-zero exhaustion, but leaves numerical constants unnamed. L488 already replays that qualitative argument; L490/L491 provide explicit residual/log inputs and L492 the audited disk count. The remaining difference is full-domain numerical inversion and edge control, not a new localization mechanism or a result obtainable by direct citation.
GAP: Prove quantitative modulus/phase localization at arbitrary strip zeros, existence of an allowed integer-phase center, and strict distance below 1/log(X/(4*pi)) with X>=4*pi*exp(10000)+2. The proposed extra unit of padding, all endpoints and comparison of the two logarithmic scales remain unproved. No essential additional theorem was identified for this bounded specialization.
REASON: Approve one subsequent proof attempt on the unchanged exact target using the inspected exhaustion method and audited local estimates. Numerical bounds must be supplied rather than extracted from unnamed constants; this literature review proves no new estimate, center inversion or exhaustion result.
SCOPE: Exact TARGET only. The strip |y|<=1 is a hypothesis, not a claimed global strip theorem. No zero-time passage, collision exclusion, change to L490's saddle imports or new zero-free region is included.
LITERATURE_REASON: The target changes from counting selected disks to localizing arbitrary zeros at a prescribed spatial edge; the previous exact-target assessment explicitly excluded exhaustion and edge transfer.

The separate literature approval is now complete. See
[the source comparison](../heat/2026-10-30-explicit-strip-exhaustion-source-review.md)
for exact hypotheses, remaining application obligations and the unit-disk
domain issue. The approval concerns coverage for a future attempt, not
validity of its proposed numerical conclusion. No mathematical attempt
was performed in this turn.

The proposed mathematical input is the arbitrary-zero localization above,
using L490's upper-strip additive residual, L491's fixed-log certificate,
L492's now-audited disk count, and the source reflection framework. The
same g(X,t) and radius 1/log(X/(4*pi)) as L492 are intended. The extra
unit of spatial padding in the target is a proposed test parameter, not
an established allowance. The source's separate exhaustion argument is
the precise passage for the next comparison; reuse the prior searches
and source notes to the extent their scope remains adequate.

The downstream use would be an explicit real/simple tail within the
stated strip, followed only in separately assessed work by any global
strip or normalization transfer needed for a bounded collision domain.
The finite interior, smaller positive times and zero-time conclusion
remain unresolved. No new theta-specific sign inequality was obtained
that could justify labeling this known-source development creative.

Continue only if the comparison covers a full-domain quantitative test:
every zero in the target range must lie strictly within one allowed disk,
including the time and height endpoints, and its center must meet L492's
padded onset. If essential coverage is missing, identify it; if the
numerical edge fails in subsequent approved mathematics, retain the
failed inequality rather than silently shifting it. Finite samples,
unspecified Section 9 constants and source (76) cannot certify this target.
Full matching Mathlib coverage remains unchecked. No new lemma or
mathematical script was written in this review.
