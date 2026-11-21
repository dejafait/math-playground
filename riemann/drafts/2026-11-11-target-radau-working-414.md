# Exact target-Radau attempt — step414 (unfinished checkpoint)

Approved target: review412, unchanged SPECIALIZE. RESEARCH/REPRODUCTION.
Main gap: actual-Xi positivity and unpaid transfer; finite F signs alone
cannot supply the unbounded target-mass rate. Use C997c/C997s exactly.

Attempt: n=64,128, lambda=exp(-n/16), original complex cap,
ordinary Lebesgue I=[7/4,9/4], all prescribed columns, at most eight
Lanczos products per degree. Fixed 660-digit directed Decimal arithmetic
(exceeding 2048 bits); no parameter or precision sweep.

Integration plan: C997s's exact polynomial primitives express each kernel
as five exponential-polynomial terms in c (four moving endpoints and the
summed lower-window constant). Multiply complete terms before integrating.
For exponent a, moments M_k=int_I c^k exp(a c) dc satisfy
M_0=(exp(ab)-exp(aa0))/a and
M_k=(b^k exp(ab)-a0^k exp(aa0)-k M_(k-1))/a.
For a=0 use (b^(k+1)-a0^(k+1))/(k+1). Conjugate coefficients and
exponents, not the variable. Every actual combined real part is negative.
Dyadic coefficient rounding and moment rounding must be paid explicitly;
exact integer polynomial convolutions may accelerate finite sums.

Before a sign: prove PSD/regularization, cyclic compression/normalization,
zero target/exact termination, strict left endpoint, Gauss/Radau direction,
L2 relaxation and original-cap conversion. Citation contracts are in
reviews410/411/412; no general quadrature theorem needs reproof.

Acceptance: coordinate widths<=2^-256, quadrature endpoint arithmetic
widths<=2^-64, propagated F endpoint arithmetic widths<=2^-60. Keep full
Gauss/Radau gap. Park on any failed bound, nonpositive lower F endpoint,
uncertain termination or denominator failure. No sign conclusion on failure.
No new creative mechanism is presently justified: an analytic mass mechanism
remains unidentified and would need its own source assessment.

## Completion

The necessary-condition screen succeeded in certifying FAILURE of the
prescribed positive-F finite test at BOTH degrees. Exact complete d and
penalty intervals prove F_64<-162754 and F_128<-2252197; see canonical
C999e. This made cyclic compression, Lanczos and quadrature unnecessary;
none was implemented or claimed. No G or h was computed. All fixed
entry and screen-width budgets pass; the separate 2^-64 quadrature
endpoint budget is inapplicable because no endpoint was used. Full
proof/certificates are canonical; independent integration audit pending.
