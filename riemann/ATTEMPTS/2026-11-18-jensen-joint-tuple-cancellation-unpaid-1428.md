# Joint-channel tuple cancellation does not pay the near layer

18 November 2026. The exact identity, multiplicity, cutoff comparison
and retained Gaussian remainder are canonical in
[C020g](../lemmas/C020g-real-prime-witness-joint-source-frequency-matching.md).

WHY THE AUTOMATIC CANCELLATION IMPLEMENTATION FAILS: expressing both
channels with delta=log(lns/(vr)) produces D_l+b_l/2, not a difference.
The two descriptions of the direct channel must be averaged. Direct
source support and interior dual saddles overlap at most at the last
cutoff index, within O(X^(-1/2)q^(-2)) of its endpoint. Exact heat
reflection supplies the same conjugate weight and a positive Gaussian
center normalization; the finite Gaussian and its remainder remain.
Consequently matching the frequency and heat weight is insufficient
to cancel original tuples. This does not exclude cancellation between
different factorizations of a common rational frequency, and proves
no residual lower bound. The exhibited unmatched family is already
O(B), below the required Bq^2 scale. The full joint estimate is unpaid.

This is an EXPLORATION outcome, not an impossibility theorem or a
counterexample to the target. Earlier stops remain intact and scoped.
A possible refinement is completion across source factorizations into
a divisor convolution, using the now-explicit multiplicity and
complementary supports. Its coverage is REVIEW_REQUIRED; no such
completion or bound has been derived here. The existing mathematical
exploration budget is not renewed.
