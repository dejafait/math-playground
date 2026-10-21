# Direct expanded joint-residual calculation stopped

2026-10-15.

WHY IT FAILS: The direct F_97(c,d,e,g)[X] expansion was interrupted
during construction of V, before E,P, their residuals or any joint
factor test were obtained. Rational-function cancellation was already
expensive at this preparatory stage. The saved artifact is explicitly
INCOMPLETE, not a certificate of incompatibility, a lower bound on
computation cost, or a mathematical obstruction to elimination. See
the [attempt record](../drafts/2026-10-15-cyclic-joint-elimination-attempt.md).
Do not repeat this expanded calculation as a continuation. The same
bounded attempt instead established
[L095](../lemmas/L095-cyclic-rational-seven-seed-reconstruction.md):
a changed seed set gives a rational reconstruction with all pole
branches handled. Its direct G,J test is still open and requires a
new analytic factor/pole argument; no larger expansion, labeling sweep
or rank sampling is justified by this failure.
