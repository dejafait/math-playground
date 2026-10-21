# Signed prefix transition: energy-weighted coefficient test

STEP_ID: YM-20261016-245-prefix-transition-coefficient-test

The approved target remains the complete joint cubic probe-jet limit
for both actual probes. L202 and L205 reduce it to the negative
polynomial Q_3 trace up to o(N^3). This attempt tests the transition
coefficient replacement in L206, leaving its long plateaus and the
finite projection/Green factors untouched. Inputs needed for this
local test are L205 and L206; its downstream trace use retains L187,
L196 and L202. The approved literature assessment is unchanged.

Proposed test: with T=Delta_T+epsilon, show

    sum_t C(x_j+a(t-1/2)) ell_t(T) T^2
          =-a C'(x_j)+o(a)

in transverse operator norm, for uniformly C^2 operator-valued axial
coefficients C acting on the left. No commutation with C is allowed.
The desired two estimates are ||T^2 p'(T)+I||=o(1) and a uniformly
controlled weighted absolute second transition moment. A useful
local reduction may leave the actual trace energy insertion open.

Working approach: compare each axial Fourier coefficient of the
polynomial with the positive one-dimensional massive resolvent at
transverse spectral value mu. L205 gives relative error eta<=2N^-2.
The resolvent kernel is q(mu)^|r|/sqrt(mu(mu+4)). Its axial tails
control the transition. Polynomial support cuts the error at degree d.
Chebyshev differentiation bounds the relative p' error by
C eta(1+m^2). Check all sums before asserting a remainder bound.

Continuation test: retain an actual o(N^3) trace estimate only if its
remaining factors absorb the right T^2 in their original order.
Abandon inferring that from operator convergence alone, smoothness of
a rough projection kernel, or deletion of plateaus/upper jumps.
The full coefficient and independent f_(i,2),r_0, matching, reflected
comparison, continuum and infrared gaps remain unresolved.

Completed: L207 gives the proposed energy-weighted expansion with
remainder O(N^(-9/8)+N^(-5/4)(log N)^4+N^(-2)(log N)^2)=o(a).
It also proves the needed derivative estimate rather than assuming
derivative convergence. The absolute second moment is controlled
after the right T^2 insertion, using scalar resolvent Fourier
coefficients and the actual Chebyshev residual. This is local
standard-method progress, not an actual signed trace limit.

Canonical proof: `lemmas/L207-prefix-transition-energy-weighted-coefficient-test.md`.
The remaining trace must absorb T^2 without commuting nonlocal
prefixes/projections or paying the generic epsilon^(-2) inverse
loss. No such estimate has been established. Retain both long
plateaus, all four covariance blocks, finite Green terms, upper
jumps and the complete heat sum for that continuation.
