# Arbitrary middle gap — proposed uniform two-peak source assessment

TARGET: Assess source coverage for T^j(n)<=n+1 on actual first-drop words 1^a0^b1^c0^d with arbitrary a,b,c,d>=1, all proper-prefix guards and a potentially partial final run.
CHECKED: 2026-10-29
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: Prepared during step552 from the supplied family overview, L111's canonical scope and the existing two-peak assessments; no external search or theorem-level comparison for arbitrary b has been performed.
SOURCE_EVIDENCE: Existing assessments inspect Rozier2019 Lemma1/equation(4)/affine proof pp.2–3 and Rozier–Terracol arXiv:2502.00948v5 Remark5.5/AppendixA; their arbitrary-b endpoint-cap applicability has not been assessed. Simons–deWeger2005 Theorem3(b) is a closed-cycle input, not a substitute for an open-endpoint cap.
COMPARISON: The notebook establishes caps at b=1 and b=2 in L110/L111; their approved mathematical scopes do not include arbitrary b. No matching uniform cap or novelty conclusion is asserted by this proposed assessment.
GAP: Complete the exact-statement and stronger-result search and inspect primary hypotheses and essential proof cases before authorizing any uniform-b derivation or test.
REASON: A single uniform-family assessment could replace repeated fixed-b extensions, but its changed unbounded middle-run hypothesis needs separate literature-only coverage first.
SCOPE: Literature comparison only for the stated open-endpoint cap; no equality application, new lemma, mathematical script or universal finite-drop assertion is approved here.

## Exact proposed family and downstream use

Use the shortcut map T of C111a and L111. Let n>1 be an integer
with actual first j parity bits 1^a0^b1^c0^d, where all four run
lengths are positive integers and j=a+b+c+d. For q_k counting odd
inputs among the first k bits, require 3^{q_k}>=2^k at every k<j
and 3^{a+c}<2^j. Both odd runs and the middle even run are exact;
the observed final even segment may continue after j. There is no
closure, minimum, least-period, numerical-distinctness or endpoint-parity
premise. Existence of such a finite first drop is assumed only for
the given word, not for arbitrary positive starts.

The proposed intermediate cap is y=T^j(n)<=n+1 over this whole family,
with b unbounded. Its plausible use is reduction of all two-peak
non-descent endpoints to equality or unit growth. A uniform equality
application would still require its own justified specialization.
Other peak shapes and finite coefficient-drop existence would remain
independent gaps even if the cap were established. No general-b
identity, inequality or derivation is supplied by step552.

## Reusable evidence and missing comparison

L110/L111 and their saved assessments provide established-method
comparisons only; neither restricted conclusion can be applied to b>2.
C111a is now critically audited for b=2, but its cycle-theorem import
does not bound open endpoints for another family. The ready assessment
`2026-10-29-c111a-descent-critical-audit.md` must not be repurposed as
uniform-cap approval.

Reuse the primary finite-input record from
`2026-10-29-two-peak-double-gap-endpoint-bound.md` and
`2026-10-29-two-peak-double-gap-symbolic-test.md`:
[Rozier2019, Lemma1/equation(4), printed pp.2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2).
The structural lead is
[Rozier–Terracol, arXiv:2502.00948v5, Remark5.5 and AppendixA](https://arxiv.org/html/2502.00948v5).
These passages were inspected in prior recorded comparisons; no fresh
source retrieval or arbitrary-b theorem comparison was performed here.
Search the exact uniform statement, coefficient stopping-time terminology,
stronger two-peak results and known counterexamples, and inspect any
load-bearing theorem/proof cases. Do not infer novelty from a failed
search or replace an actual open orbit by a closed m-cycle.

Attempt036 and L109 retain the counterexample to uniform adjacent-swap
margin order; this continuation proposes chronological junction methods,
not that order. Attempt037 retains the repeated-approval failure. A
new review is justified here by the genuinely changed unbounded b
hypothesis, not by a missing source for C111a or another b=2 audit.

## Decision test and routing

Import a matching published theorem with its precise hypotheses if one
is found. Otherwise approve at most one bounded symbolic junction pass
only after documenting adequate comparison coverage and its stopping
test. A specific sign obstruction or a compatible actual counterexample
would stop the proposed cap route; an unread essential theorem leaves
it SOURCE_BLOCKED or REVIEW_REQUIRED. No mathematics is authorized by
this file's current REVIEW_REQUIRED decision.

The next task is literature_comparison, using standard/high settings.
The uniform-family development would be an established-method extension,
not a creative mechanism. Saved coefficient-prefix discovery still lacks
a bounded pointwise arithmetic bridge, so it does not justify a central
creative nomination. Full matching and supporting Mathlib coverage for
the proposed cap are not checked.
