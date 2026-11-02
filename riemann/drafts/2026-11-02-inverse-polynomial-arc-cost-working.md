# Polynomial arc-cost attempt — working checkpoint, step 51

Approved scope: unchanged EXPLORE assessment in drafts/literature/2026-11-02-inverse-parameter-polynomial-separator.md. Main Xi signs remain open. Essential inputs: L666 rational identity and L675 coefficient relation and |F| >= (23/22)^(n-1). L674 is a comparison only.

Promising bounded mechanism, not yet independently audited: write w=(1+exp(i theta))/2 and theta0=2 atan(9/25). The required closed segment is |theta|<=theta0. Its complement satisfies |w|<=r=25/sqrt(706). Inner b and normalized Parseval give sum beta_k^2=1. For an exact degree<=n action, Cauchy--Schwarz in the prescribed coefficient relation should yield |P(w)|<=r*kappa^(-(n-1))*||psi||_2 on that complement, with kappa=23*sqrt(706)/605.

P(10/11)=0 corresponds to Poisson evaluation at z=9/11 of Q(z)=P((1+z)/2). The kernel is between 1/10 and 10. To force positive arc mass from h(0)=1, write h(theta)=S(cos theta), L=1-cos theta0, H(phi)=S(1-L/2+(L/2)*cos phi), and K(phi)=(1+cos phi)*H(phi). K is nonnegative of degree<=n+1 and K(0)=2. Elementary Fourier coefficient bounds give mean K>=2/(2n+3); the substitution gives integral_0^theta0 h(theta)dtheta >= pi*sin(theta0/2)/(2n+3).

If all details hold, Poisson balance forces ||psi||_2 >= 9*kappa^(n-1)/(2500*(2n+3)). Since log kappa >= 7449/739499 = 1/100+5401/73949900, this would stop the full degree<=n polynomial class, even allowing every free Fourier mode. Need check all coefficient conventions, mass constants, complete circle bound, Poisson identity, and exact arithmetic. No assumption that beta_k is nonzero is needed. This does not stop arbitrary nonpolynomial segment-positive actions or the cone, H, support, or Xi realization. No conclusion accepted yet.

## Resumption checkpoint — step 52

The supplied ready assessment is unchanged. Read L675 and L676 in full,
L666's complete product, and the scoped low-degree, disk and finite-sign
stops. The preceding unfinished argument is preserved. No other
canonical proof of the proposed complementary-arc obstruction was found
in the relevant L67x and polynomial-step paths.

One attempt now completes this proposed obstruction. The two load-bearing
checks are the degree-limited coefficient bound on the complementary arc
(using every possible preimage, including free moments), and the positive
arc mass lower bound after the cosine substitution. Direct differentiation
gives dtheta/dphi >= sin(theta0/2)*cos(phi/2), which bounds the mass below
by half the integral of K. The Poisson kernel calculation is finite
polynomial/Fourier algebra, using the already covered normalized Fourier
input. It needs no new positivity-domain theorem. These observations are
working reasoning pending the full proof and exact constants; no separate
audit or global cone obstruction is claimed.

## Completion — step 52

The full argument is now canonical in
`lemmas/L677-full-degree-polynomial-arc-cost-obstruction.md`.
All 15 exact constant checks passed in
`scripts/one-sided-hankel/polynomial-arc-cost-check.json`; the complete
check list and rate values were inspected. The result obstructs the
specified full degree<=n class, including all preimages, at the saved
rate. This working draft is preserved; its proposal is not counted
as a second result. L677 and its L675 input remain separately unaudited.
The new audit coverage nomination is saved for separate approval; no
audit or second mathematical attempt was performed in this turn.
