# Gaussian compensation packet test — working record, step347

11 November 2026. One RESEARCH attempt under the unchanged, supplied,
pre-invocation EXPLORE assessment345. No new literature approval is
made here. The exact family, fixed parameters and complete response
are those in assessment344/345. Preserve the earlier stops.

Main gap: L030-L032/C032a actual-Xi positivity and L966/L968 signed
forcing, with L984(H) unpaid. This packet tests the intervening point
bridge; it does not supply actual zeros or signed positivity.

Write delta=1/8, x=c-2, q=floor(theta*n), r=floor(lambda*n),
b_n(x)=(1-64*x^2)^q and
w_n(x)=b_n(x)*exp(-A*n*x^2)*E_r(A*n*x^2). The parameters
theta,lambda>0 and A>=A_0 are fixed before n. The original normalization
is M_n=integral_[-delta,delta] w_n, since the weight is nonnegative.
The response includes both endpoints, both Laguerre branches, both
beta terms, both short intervals and K's -1.

Bounded test: obtain exp(-o(n)) target retention together with uniform
exp(-sigma*n) closed-J suppression, or a rigorous conflicting rate on
an explicitly stated parameter range. A failed upper estimate alone
is inconclusive. C997i already excludes its actual-degree<=n,
A>=max{A_0,6553600} overlap; do not reprove that overlap as new work.

Unfinished reasoning saved before further work:

- On the real interval, exp(-u)E_r(u) is in [0,1] and decreases for
  u>=0. Hence w_n is even, decreases for x>0 and has total variation
  at most 2. For x=y/sqrt(n), the finite exponential tends to exp(A*y^2)
  because r tends to infinity, whereas b_n tends to exp(-64*theta*y^2).
  A Gaussian domination should give sqrt(n)*M_n -> sqrt(pi/(64*theta)).
- C997e's exact minus amplitude is nonzero at (z_star,2). Real
  concentration should retain its limit. The other branch has phase
  2*n*phi(c), with phi' bounded away from zero on J. Integration by
  parts against the monotone weight, using the exact amplitudes and
  their uniform derivative bounds, may make its normalized integral
  O(n^(-1/2)). This is a proposed proof, not yet a certified conclusion.
- These real-axis facts alone do not control the data band: multiplication
  by exp(c*n/8) can amplify an exponentially small compensation error.
  Complex growth and endpoint charges must still be paid for any band
  assertion. No successful parameter choice or family-wide obstruction
  has yet been established.

Essential inputs: C997c(1),(4)-(6), C997e(4),(15)-(16), with L997(4),(7)
through those contracts. Source tools and comparisons are read in
reviews329/332/344/345. C997f uses a different phase multiplier;
C997g/l impose response jets absent here. Failures340/341 leave an
actual target spectral tail unpaid and are not reopened. Mathlib
matching coverage remains unchecked. No cross-notebook input.

## Developed calculation before canonical write-up

The target argument above closes: sqrt(n)*M_n tends to
sqrt(pi/(64*theta)); integration by parts bounds the unwanted branch
by O(1/n) before normalization. The leading target constant is C997e's
nonzero B_star. All original remainder terms are paid by TV=1.

For lambda>=A, the exact lower-incomplete-gamma identity and
k!>=(k/e)^k give 0<=1-exp(-u)E_r(u)<=exp(-2*lambda*n) on the real
interval, since u<=An/64 and k=r+1>lambda*n. This error remains
exponentially negligible after the data factor exp(17n/64). Thus one
can replace w_n by b_n in the real data integral before deformation;
no complex compensation claim is needed.

For t=q_n/n, beta=1/8+i, the pure endpoint phase has the exact saddle
s_t=delta^2*beta/(t+sqrt(t^2+delta^2*beta^2)). For sufficiently large
fixed theta, it lies in the audited amplitude rectangle, with
0<Im(s_t) and |s_t|<=1/(32t)<=1/256. Its phase S_t obeys
Re(S_t)>=29/128. On the shifted central half-interval the real second
derivative is <=-12t. Both horizontal outer pieces and both vertical
endpoints have modulus rate <=17/64+t*log(7/8)<=-47/64 for t>=8.
The plus Laguerre branch loses at least 2*Im(s_t)/3 on the horizontal
segment. A dominated rescaled complex Gaussian integral therefore
gives a nonzero leading data response at 2, with rate Re(S_theta)>0.

The canonical write-up must retain the moving t=q_n/n in exp(n*S_t),
prove the Hessian and endpoint bounds, choose the large-theta threshold
before n, and record its existential analytic-domain dependence. This
only stops lambda>=A and sufficiently large theta. Smaller theta or
lambda<A remain open; this is not an all-family impossibility.

The completed calculation is now canonical in
[C997m](../lemmas/C997m-gaussian-compensated-endpoint-packet-leakage.md).
It is unaudited. This working record preserves the unfinished reasoning
and decisions; subsequent corrections belong in the canonical proof.
