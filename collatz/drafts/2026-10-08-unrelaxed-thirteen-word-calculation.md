# Thirteen-word retained-coefficient attempt — 2026-10-08

Approved target: Determine whether L041's unrelaxed per-word logarithmic
and height-transfer estimates exclude actual closed concatenations of
thirteen allowed postspell words.

Pre-invocation assessment:
`drafts/literature/2026-10-08-unrelaxed-thirteen-word-estimates.md`
(SPECIALIZE). Completed classification: REPRODUCTION; actual task:
proof_attempt. The main gap is universal eventual descent. This bounded
test can extend the restricted cycle exclusion, leaving entry, arbitrary
counts/cycles and divergence independent. Continue only on an all-length
contradiction above the published primitive odd-count threshold; otherwise
record the precise failed comparison and stop this sharpening route.

Inputs read: complete L041 and L043, Attempt 019, history 069. Reuse
the supplied primary-source assessment; no further literature is needed.
The scalar feasibility witness in L043 does not test wordwise heights;
the guard-only and full-minimum-count failures remain untouched.

Completed calculation, not yet independently audited: put ell=log 2,
delta=log 3/ell, cJ=log(11/4). L041 gives
4J ell<=h+cJ and H ell<h+J(3 log 3-4 ell).
With G=(27/16)^J(3/2)^H, these imply
log G<(delta-1)h+delta J(3 log 3-4 ell).
Its positive J coefficient permits substitution of the first bound:
h_next<(3 delta^2/4)h+delta(3delta-4)cJ/4.
Since 4/3<delta<8/5 and 0<cJ<4/3, this is less than
(48/25)h+32/75<2h+1. Thus h_next+1<2(h+1).
Starting at the smallest designated junction and traversing thirteen
occurrences gives sum P_i<(15/4)(2^13-1)(h_0+1), using L041 (7).
The seed h_0<13.3 log N+8+log 13 and log 13<3 yield
N<(399/5)*8191 log N+72*8191+897/1034.
Compare on all real N>=338460000, not on a finite parameter screen.

The initial working calculation was saved before completing the proof.
The canonical result is now
[L044](../lemmas/L044-thirteen-postspell-retained-coefficient-exclusion.md).
All substitutions have positive coefficients, and the shifted endpoint
comparison retains both offsets. At C=338460000, the right side with
log C replaced by 20 is 14127116889/1034<13662589; the margin
is greater than 324797411, with required margin zero. Since
A=3268209/5<C, the difference is strictly increasing on all real t>=C.
The imported primitive threshold forces N>C and hence a contradiction.
Actual closure, integer parameter guards, exact independent tails,
repeated periods and coincident junctions are retained; no junction is
a presumed global minimum. No claim for fourteen words is made.

`python3 scripts/postspell-word-count/certify_thirteen.py` passed all
17 exact arithmetic checks with no failures; complete evidence is in
`scripts/postspell-word-count/thirteen-certificate.json`. These finite
checks supplement the full analytic argument, not an infinite search.

Outcome ADVANCE, RESEARCH/REPRODUCTION: a relevant restricted exclusion,
with no originality claim or advance beyond the checked general source
mathematics. The prior two mathematical EXPLORATION attempts remain
historical; this completed mathematical advance ends that unresolved
exploration streak. L043's scalar maximality and earlier failure records
remain valid. The bounded continuation test succeeds, so retain the
result for a separate critical audit. Audit coverage is REVIEW_REQUIRED
in `drafts/literature/2026-10-08-thirteen-word-exclusion-audit.md`.
The primitive source computations, Rhin/Crandall originals, external Lean
and Mathlib matching coverage remain unchecked. Universal entry, arbitrary
counts/cycles, divergence and eventual descent remain unresolved.
