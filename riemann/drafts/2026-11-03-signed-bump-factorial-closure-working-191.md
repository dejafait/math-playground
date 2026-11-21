# Integer-kernel factorial closure — step 191

Saved before lengthy reasoning. The invocation-start EXPLORE assessment
`literature/2026-11-03-signed-bump-analytic-symbol.md` is reused unchanged
for its exact TARGET. This is one mathematical attempt, not source review.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
the original exact integer-size p_n, normalized by n^(1/2) exp(n S),
has a holomorphic elliptic amplitude with factorial errors for every
1<=m<=epsilon*n on one fixed complex neighborhood of I. A possible
downstream use is support-edge singularity transfer for the signed bump;
that theorem, signed noncancellation and full-response/Xi gaps remain open.

Inputs: L719's full proof has been read, together with the exact L714
kernel and L715--L716 hypotheses. L719 is unaudited; its use here does
not audit it. Its circle, common local domains, phase identity, quadratic
decay and full complementary gap are the provisional inputs. The ready
assessment's source comparison and five preserved route failures are
reused. No change to chi, integer sizes or normalization is allowed.

Bounded test: first exponentiate the local logarithmic expansion using
a finite coefficient polynomial on an auxiliary disk of radius O(1/m).
Then use the already assessed analytic Morse/Gaussian theorem, retaining
one fixed parameter domain and combining the coefficient-order and
Gaussian-order remainders. All exponentially small contour errors must
be dominated by the same factorial bound for every m<=epsilon*n.
Continue only with this full estimate; fixed-order or formal closure is
inconclusive. No new general stationary-phase theorem will be claimed.

Potential weak points to check: constants uniform in complex v; matching
the finite-polynomial coefficients to all orders; uniform bounds for the
exponential on its auxiliary disk; Morse chart and endpoint connectors;
the double-index convolution; and absorption of exp(-c*n) at all orders.

## Intermediate reasoning saved

Set h=1/n. L719's odd-order logarithmic expansion converts to coefficients
ell_j (zero for even j) with |ell_j|<=B^j*j! and remainder
B^(m+1)*m!*h^m for m*h small. For even m use its next odd remainder,
whose extra factor (m+1)*h is uniformly bounded. Its m=1 estimate also
gives a bounded exact logarithmic correction.

For P_m(z)=sum_(1<=j<m) ell_j*z^j, take radius 1/(4*B*m).
Since j!<=m^(j-1), P_m is uniformly bounded on this disk. Cauchy's
Taylor tail for exp(P_m) then gives C^(m+1)*m!*h^m when
h<=1/(8*B*m), using m^m<=e^m*m!. The first m exponential coefficients
are independent of the truncation. This is a finite-polynomial argument;
no convergence of the formal factorial series is assumed.

For the stationary integral, the fixed local Morse coordinate is
w=tau*sqrt(2*psi(tau,v)/tau^2), with derivative sqrt(H(v)).
Re(H)>1/3 and common upper bounds permit uniform charts and fixed
positive/negative Gaussian sectors. Endpoint connectors to a fixed
real segment stay away from zero and have a common positive phase gap.
Use Hitrik--Sjostrand Thm 2.3.1 for every Gaussian order, rather than
Thm 2.3.3's optimal-order conclusion alone. A product coefficient of
order k is expanded to Gaussian order m-k. The remainder sum contains
k!*(m-k)!<=m!, so no second factorial loss occurs. Exponential contour
errors are absorbable because exp(-c/h)<=m!*(h/c)^m for every m.

These are working estimates awaiting full canonical write-up and a later
independent audit; they do not establish signed bump noncancellation.

## Completed attempt

Full reasoning is now canonical in L720, including the complex-domain
and endpoint checks and the exact leading normalization. Outcome:
ADVANCE as a local reproduction/specialization of the assessed tools.
No new general calculus or certified originality is claimed. L719 and
L720 remain unaudited, so the next task is independent conceptual review
of the same exact target using the unchanged prior assessment. No signed
bump rate or other RH gap is inferred from the factorial expansion.
