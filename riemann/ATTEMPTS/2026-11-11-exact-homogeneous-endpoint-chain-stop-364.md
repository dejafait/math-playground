# Exact homogeneous endpoint-chain stop — step364

The pre-approved endpoint-chain test used the complete C997c kernel
with finite complex band measures on E=[15/8,17/8], z_star=1+i/8 and
integer n>=2. The requested simultaneous bounds remain subexponential
original band-TV and slope residual O(exp(-n/64)). The tested exact
cancellation ansatz imposes r q(rx)=q(x) on the upper window, retaining
its terminal values and the lower-window boundary constant.

WHY IT FAILS: [C997q](../lemmas/C997q-finite-endpoint-chain-exact-band-incompatibility.md)
proves that a finite band measure makes q entire; the homogeneous
identity on any open subinterval then forces q=0 globally and the band
transform to equal exp(i z_star t), contradicting its boundedness on
the real axis. This covers all zeros and multiplicities without
division by g_n and cannot be repaired by terminal or lower-window
choices. The stop is exact-homogeneity only. It supplies no quantitative
lower bound on an approximate defect and does not exclude approximate
band duals or prove/disprove RH. C997q(1)–(5),(8)–(10) preserve the
boundary, zero, terminal and weighted-cost conditions for future work.

A different candidate is a finite-band exponential-sum construction
with a nonzero controlled defect. Its superoscillation/cost comparison
has not been completed; the proposed source review is REVIEW_REQUIRED.
No existence, cost rate or new source coverage is asserted.
