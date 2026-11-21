# Weighted Gaussian sign attempt1556 — preserved working notes

Completed in C032t; the strategy and calculation checkpoints below
are preserved intermediate reasoning, not an additional proof source.
The separate critical audit remains pending.

Approved target: the exact TARGET of assessment1554 (SPECIALIZE at
invocation), K'(u)<0 on [1/10000,1/200]. Main gap remains actual-Xi
all-degree positivity; this tests only one finite Levy comparison.

Inputs read: C032j, C032s, source-notes1555, counting-envelope stop1554
and reverse-order stop1553. Existing unfinished changes are preserved.
No fresh literature search or source approval is being claimed.

Proposed calculation: import the unconditional Gaussian explicit formula
H=e^(u/4)+A-P with the positive-ordinate half-sum normalization.
The weighted prime term is a positive sum of exp(-(log n)^2/(4u));
its derivative should be positive, hence its contribution to K' negative.
Check uniform dominators. Seek an effective lower bound for the
archimedean integral after its constant part cancels under weighting.
The positive pole derivative must remain in the comparison. Retrieve
the already assessed Connes regularization before using its constants.

Pass: a strict uniform negative upper bound on the entire closed interval.
A failed bound is inconclusive; positive K' would stop only this test.
Do not infer D<0, a law comparison, J_eta=0, or Xi realization from
such failure. Full cancellation and realization remain independent.

This draft contains a strategy, not a certified inequality. Save the full
proof in a canonical lemma if the bound closes, then nominate a separate
critical audit with all external-input qualifications intact.

## Calculation checkpoint

Retrieved the already assessed Connes2402.13082v1 equations (5), (7),
(9), (13), (15), printed pp.4-5. Use (5) with all complex zeros;
do not use the real-spectrum reading (11) or Theorem1.1. Set
B(x)=exp(x/2)/(exp(x)-exp(-x)). The exact weighted identity gives

    K'(u)=exp(u/4)*(1/(2*sqrt(u))+sqrt(u)/4)
          -integral_0^infinity x^2*B(x)*exp(-x^2/(4*u)) dx
                                      /(8*sqrt(pi)*u^2)
          -sum_(n>=2) Lambda(n)*(log n)^2*n^(-1/2)
                   *exp(-(log n)^2/(4*u))/(8*sqrt(pi)*u^2).

The prime term is nonpositive. For 0<x<=1, the power series gives
sinh(x)/x <= 1+x^2*(sinh(1)-1) < 1+x/2 <= exp(x/2),
using e<3. Thus B(x)>1/(2*x) there and the integral is greater
than u*(1-exp(-1/(4*u))). For u<=1/200 the latter exponential
is below 1/100. With pi<4 the negative weighted contribution is
greater in magnitude than 99/(1600*u). The pole contribution,
after multiplication by u, is below
401/11186 < 59/1600 (sqrt(u)<1/14, exp(u/4)<800/799).
Therefore K'(u)<-1/(40*u) on the requested compact interval.

Before promoting: write the full real-parameter dominators on
[1/20000,1/100], including the canceled archimedean integrand at
zero, the Gaussian prime-series derivative and the complex-zero
sum. Keep all source qualifications. No mathematical script or
numerical certificate is needed for these exact inequalities.
