# Grouped finite reference quartic — working save1405

The start-of-turn EXPLORE assessment1402 approves exactly the fixed
actual-Jensen squared-pair target. No source refresh or new target is
being approved in this research step. Existing unfinished work is kept.

Main gap: L030-L032/C032a actual-Xi all-degree positivity, with the
unbounded exceptional-root deficit still open. Intermediate target:
I_P=O(B), equivalently I_V=O(X) by C019t. Together with C019r's
retained negative mean this could support opposite-sign density;
ordered roots and bulk separation would remain separate obligations.

Bounded test: group the finite positive-frequency half-sums by integer
product before estimating their squared product with H^2, where
H=M(Y)M(Y+h). Retain each heat multiplier, entry interval, alpha
coefficient, linear taper, h=3*pi/log X and L=floor(X^(1/1000)).
Do not repeat C019s's termwise sixteen-channel bound. Seek O(X), or
incompatible growth for the exact observable; failure of a stronger
half-sum upper bound would not refute I_V=O(X).

Working idea, not yet a conclusion: V=F+conj(F), so pointwise
V(Y)^2 V(Y+h)^2 |H|^4 <=16 |F(Y)F(Y+h)H(Y)^2|^2.
The grouped length is N_*^2 L^4, exceeding X. Establishing only a
formal grouped identity will not pay this stronger norm. Its moving
coefficient variation and arithmetic diagonal must both be examined.

Essential inputs: C019m/p/s/t; C019r supplies the downstream mean,
with C019j/k,l/q and L018/L021 inherited as qualified in those files.
C019s/t remain unaudited. There is no RH, random-law, nonvanishing,
ordinary-to-heat or critical-line reciprocal assumption. Mathlib full
matching coverage is unchecked. No numerical experiment is planned.

## Completed bounded calculation

The full calculation is canonical in
`lemmas/C019u-grouped-half-sum-quartic-upper-bound.md`.
Grouping before estimation gives exact integer frequencies with
piecewise smooth coefficients G_k retaining both heat times and
entries. The coefficient supremum plus total variation B_k is at
most C d_4(k). Finite integration by parts and a weighted square
inequality give the explicit signed budgets in C019u (8).

The absolute divisor envelope yields I_V and I_P bounded by
O(X^(251/250)q^16), losing X^(1/250)q^16 against the required O(X).
Neither incompatible growth nor the O(X) target is established.
This is EXPLORATION: an elementary full upper bound and a more
explicit unpaid norm, not a successful M2 test or a new moment theorem.

Hand checks cover the exact shifted coefficient n^(-ih), the common
unit-modulus phase, each entry jump, the three integer-kernel ranges,
the divisor-square inequality at every prime power, and the actual-P
norm transfer. C019u remains unaudited. No mathematical script or
numerical evidence is used. The main PROOF overview remains accurate:
transfer is available and the required quartic bound is still open.

The next refined subtest within unchanged ready1402 is the signed
low-index coefficient budget sum_(k<=L) B_k^2/k=O(1). For these
indices every m,n<=k<=L is already present throughout J; retain
the exact alpha convolutions, shifts and heat weights. This would
pay only that portion of the diagonal. Larger indices and (8)'s
off-diagonal variation budget remain independent gaps. If cancellation
does not improve the divisor envelope, preserve the first unpaid
coefficient sum rather than repeat the present estimate. Failure of
this stronger sufficient test is not a refutation of the real pair.
