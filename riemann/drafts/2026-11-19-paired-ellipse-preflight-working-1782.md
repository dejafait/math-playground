# Analytic-ellipse preflight1782: working record

Approved scope: unchanged SPECIALIZE assessment1780, exact scalar
preflight at order128, cuts2^+/-256, n=1, delta=1/16, error2^-20,
aggregate10^7 elementary terms and precision512. Main gap remains
L030-L032/C032a actual-Xi positivity, signed height and realization.
This attempt tests an analytic quadrature certificate, not midpoint1781.

Inputs inspected: C033s and C033t in full; C032w's explicit formula
and its complete Gaussian specialization; C033m(3), C033j's signed
construction and C033r's fixed sample interface. Reused notes1778/1780;
retrieved Johansson1802.07942v1 Section2, p2, for the exact ellipse
bound M*C_rho*rho^(-2n), C_rho<50 for rho>1.1. No new source scope.

Unfinished test: let F(w)=p_w(0), w_sigma(y)=sigma+exp(-y)/4.
The direct integrand is sqrt(pi)*exp(-y/2)*(F(w_sigma)-F(w_1)).
Establish a right-half-plane continuation from the assessed Gaussian
explicit formula and bound the difference by integrating F' along
the real width segment. On |Im y|<=1/2, Re w_sigma>=1+exp(-Re y)/8.
This should pay small-time cancellation without bounding two enormous
profiles independently. Then count outer analytic nodes AND every
prime-power callback under a fully declared finite certificate.

Continue only with explicit uniform domain, error and aggregate cost;
a failed sufficient certificate is not an actual-error or algorithmic
lower bound. Keep finite polynomial/atoms/signs and all fixed-v1,
counting, zero-data and heat qualifications. C033s/t remain unaudited.
If this branch also fails, park the numerical interface and nominate
an independently testable next target for separate source approval.
No observable has been evaluated and no precision implementation passed.

Intermediate derivation saved: the explicit formula extends to Re(w)>0.
For v=Re(w)>=1, its differentiated pole, archimedean and prime terms
give |F'(w)|<17/v. On |Im(y)|<=11/10, cos(Im(y))>=79/200;
integrating along sigma in[1,2] gives |d_sigma(y)|<64. The positive
Laplace factors have modulus<=1 there. This supplies an actual analytic
ellipse majorant, including enlarged widths and small-time cancellation.

Declared branch:128 equal logarithmic panels, rho=2, degree67,
positive Gauss weights, shared d_sigma nodes for its five scalar integrals.
The outer quadrature allowance is819200*4^-67<2^-114. Uniform direct
prime-power callbacks, with one common dyadic cutoff N=2^k and no
node-dependent pruning, have total weighted omission allowance
256*exp(-(log N)^2+log(N)/2). Acceptance at2^-114 is exactly
k^2*log(2)>=122+k/2; k=14 is the least accepted dyadic exponent.
Count all prime powers<=16384 at all8576 nodes, already for one
nontrivial width and its mass scalar. If that exceeds10^7, stop before
archimedean, width-interpolation or512-bit implementation work.
This is a sufficient-certificate failure only; adaptive/rearranged
algorithms are not lower-bounded. Full proof and exact count are pending.

Completed: C033u now contains the canonical proof. Certificate1782
checks all finite inequalities and independently counts1961 prime
powers, for16817536 terms already at one width and one mass scalar.
The analytic allowances pass; aggregate cost fails. No observable or
full512-bit implementation is certified. Earlier unfinished reasoning
above is preserved as the working record. Numerical work is parked;
the separate audit-coverage nomination remains REVIEW_REQUIRED.
