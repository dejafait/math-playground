# Spatial maximum continuation — working record, step 168

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-spatial-doubling-growth-attempt-scope.md`.
The approved target is unchanged: test B_sp(n)=o(n), s=65/64,
for the complete fixed L703/L666 family on |u|=1/2.

Main gap: actual-Xi all-degree positivity. The intermediate target is
L710's full unit-disk maximum comparison near i/2, with the centered
bump bound retained as an independent obligation. Paying both with
the specified strict rates would give a positive B_sp/n lower limit
and stop this sufficient defect-payment mechanism; a sublinear ratio
would instead help pay L707's defect. Amplitude, full charge, H/support,
L657 accounting and Xi realization remain open.

Inputs read: L666's full-family definitions; L703's fixed bump and width
selection; L709's full proof; L710's full signed-residue reduction;
L708's real-frequency identity and relevant audited convolution cases;
the parent source comparison and the four recorded spatial stops.
No new essential source is imported. L709 and L710 remain unaudited.

Bounded test: seek S_(n,1)/|W_n(u,-Y)| <= exp(n/20000) uniformly
on a fixed arc near i/2, retaining the complete signed finite sum.
First examine the spatial-resolvent pole rates on the entire unit
boundary, including poles reaching the real line and physical tails.
A pointwise endpoint rate or an absolute residue bound is insufficient.
If this bound cannot be justified, preserve the exact unpaid term or
refined contour mechanism; do not infer an actual positive B_sp rate.

The bump obligation max_(D_*)|E_n| >= exp(-n/10000) is also unpaid.
The already assessed three-circles theorem may give a propagation
bound, but a new entire-function theorem would require a separate
literature turn. No new source gate is bypassed by this attempt.

## Refined contour mechanism (unfinished)

Put y_z=-i(d+R/z). A contour entirely inside |y+i*d|<R,
enclosing [-Y,Y], permits an exterior maximum-principle bound on
the finite F_n(z(y)); it has no exterior poles and a finite value
at infinity. This avoids extending the infinite resolvent through
its remote lattice poles. Use a polygon just below the upper circle
c=sqrt(U-X^2)-d for -1/2<=X<=1/2, bottom c=-1/10, and vertical
sides X=+-1/2. The top retains L710's residue. On the bottom the
positive-frequency resolvent is pole-free down to c=-1/20.

On the sides away from c=0, use the same residue calculation with
the lower-contour residue included when the pole has negative c.
Near c=0, do not bound the infinite resolvent separately. The finite
F_n is analytic on rectangles |X+-1/2|<=1/100, |c|<=1/1000.
Horizontal-edge bounds can be propagated to the center by a harmonic
cosh barrier, with the crude full finite bound on the vertical edges.
These rectangles contain no retained pole. Every proposed contour
and rate estimate still needs its complete check.

Initial floating screens (not evidence): the unit-pole centered rate
peaks near X=-.387 at about .020099, versus the negative endpoint's
.020516. The proposed outer point from L710 has rate about .020763.
No conclusion follows until continuous enclosures and all signed
frequency/physical tails are supplied. The bump lower bound remains
independent even if the complete unit upper bound succeeds.

## Completed attempt

[L711](../lemmas/L711-full-unit-spatial-maximum-endpoint-rate.md)
proves the full unit maximum has the negative endpoint's exponential
rate, uniformly on a fixed arc near i/2. The rational polygon lies
inside the unit spatial-pole circle and encloses all retained nodes.
Both crossed-pole signs, negative frequencies, the zero comb sample,
all remaining samples, both physical tails and all finite moments
are retained. The real-axis bridge uses only the finite rational
function, so remote infinite-lattice poles are never canceled by
an unjustified separate estimate. A variable bridge width gives
the uniform o(n) logarithmic loss; its angular neighborhood is fixed
before that width is varied.

All 28 exact auxiliary comparisons pass in
`scripts/one-sided-hankel/spatial-unit-contour-rates-168.json`.
The entire top-edge upper rate is <.0203, versus the endpoint lower
rate >.0204. The stored certificate includes all cell remainders;
it is not a separate audit of the analytic proof or L709/L710.
The original floating screens above remain nonproof diagnostics.

This pays the full unit-maximum obligation in L710 (19), including
the stronger eventual bound exp(n/100000). It supplies no lower
bound on E_n over D_*. The unchanged ready target can continue by
testing that single remaining bound with the assessed analytic tools;
an essential new theorem requires a separate source review. No B_sp
decision or RH candidate is obtained. All earlier stops are preserved.
