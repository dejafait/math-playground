# Fixed Jacobi heat derivative: saved calculation

Approved target: ordinary full-line L2 membership of Q in
drafts/literature/2026-10-31-jacobi-heat-profile-integrability.md.
No corrected profile, complete-kernel identity or sign is being tested.

Put H(u)=partial_z^2 B(u,0), x=exp(2u), y=1/x.
DLMF 20.7.32 gives the full transform
theta_3(z|ix)=x^(-1/2) exp(-z^2/(pi x)) theta_3(iz/x|i/x).
Differentiating twice in z, including the Gaussian and transformed
argument, gives
H=-(1/pi)y^(5/4) -(2/pi)y^(5/4) sum exp(-pi n^2 y)
  +4y^(9/4) sum n^2 exp(-pi n^2 y).

Provisional calculation: with E=y d/dy, Q=(8E^2-1/2)H.
The zero mode contributes -(12/pi)y^(5/4). For v=pi n^2 y,
the complete remainder should be
(y^(5/4)/pi) sum (32v^3-192v^2+216v-24) exp(-v).
Need check every coefficient and justify two u derivatives uniformly
on compact sets and a full-series remainder at y>=1.

Expected bound: |remainder|<=C y^(17/4)exp(-pi y), so
Q=-(12/pi)exp(-5u/2)(1+O(exp(-6u)exp(-pi exp(-2u))))
as u tends to minus infinity. A relative o(1) yields the required
divergent L2 lower bound. Positive endpoint direct-series estimate:
|Q|<=C exp(9u/2)exp(-pi exp(2u)), u>=0.

Completed this invocation: every coefficient, local differentiation,
full infinite-series remainder and both endpoints are proved in
[canonical L600](../lemmas/L600-jacobi-heat-profile-not-square-integrable.md).
The saved provisional calculation above is preserved as working history;
it is superseded by that full proof, which still awaits independent
critical audit. Existing L019/L239 describe actual k and do not supply
auxiliary-profile parity or decay. No mathematical script was needed.
