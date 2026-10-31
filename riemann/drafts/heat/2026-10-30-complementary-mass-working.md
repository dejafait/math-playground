# Fixed-corner complement calculation — working record

Approved target: the exact Next action in the supplied reproduction
assessment. Main gap: actual-Xi all-degree positivity. This computation
can supply a fixed-corner unit budget for the collision route, not the
strict charges, transport, H1, other times or zero time.

Inputs: L494 normalization, L495 complete signed beta_m, L496 exact
sigma, L497 parameters/prefix and its complete initial interval ledger;
Planat v2 Section 6.6, Lemma 6.7, both cases as transcribed in the
approved source comparison. No extra literature review is needed.
The L497 proof/code audit remains pending.

Implementation plan: rescale all 691004 input intervals outward to the
binary rational grid 2^-56. Enumerate every increasing squarefree prime
subset with product d<=floor(exp(ell0)); positive factors make pruning
exact. Store d<=H for signed block convolution, including d=1. Accumulate
both clipped-moment and residual-Euler-moment contributions with signed
integer interval arithmetic. Check the exponential floor by high precision
rational intervals and compare the complete edge plus remainder against
.301408572679396256667379418689. Preserve every block and moment total.

Continuation test: only a complete bound below that threshold passes.
An excessive bound needs quantified grouping/moment/rounding loss; a
resource interruption leaves unfinished evidence, not a complement claim.
No source decimal, partial subset or timing estimate counts as a certificate.

Completed: [L498](../../lemmas/L498-fixed-corner-complementary-coefficient-mass.md)
records the full fixed-corner bound, proof, source citation and qualifications.
The exact complete majorant upper bound is
21688332681815698/72057594037927936, below the threshold. Every block
and every edge divisor was consumed by the reporter. The complete
moment enumeration and signed coefficient computation still need a
separate critical audit, as does the retained L497 input. The source
method was reproduced; no collision charge or central positivity gap
was closed.
