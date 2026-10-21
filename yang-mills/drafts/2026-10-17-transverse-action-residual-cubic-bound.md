# Transverse action residual covariance — bounded attempt

The unchanged approved target is the complete L025 nonradial action
response's finite cubic-scaled limit for both actual probes. L213 reduces
it to the full transverse 24-pair class with O(N^(5/2)) error. A local
O(N) bound for its signed residual covariance V, combined with L213's
O(N^-2) external U entries and O(N^4) plaquettes, would establish cubic
boundedness, a useful intermediate threshold before convergence.

Saved reasoning: in stored coordinates write R_F=I-D Phi and
K=Sigma A Sigma, so V=R_F K R_F^T. On transverse edges at interior
axial levels its row is a direct transverse selector minus a transverse
difference of a component-1 lower prefix. Expand both rows into four
terms only after using this exact lift. L211(5) bounds every K entry by
C N[(1+dist)^-2+N^-2]. Direct/direct is O(N). A direct/prefix term
samples at most two axial fibers; their inverse-square decay has a
uniformly summable axial series, also when their transverse separation
is zero. Thus each such term is O(N), without differentiating K.

For prefix/prefix, L065's scalar form gives
|f^T A_11 f|<=C f^T H_T f and Sigma_1 H_T Sigma_1<=Sigma_1.
Consequently |w^T Sigma_1 A_11 Sigma_1 w'| is at most
C sqrt(w^T Sigma_1 w) sqrt(w'^T Sigma_1 w'). L026's prefix-gradient
variance bound, extended to normal transverse end edges in L213,
bounds these two variances by N. This should close O(N) without
using the false full-vector version of L065 or bounded raw covariance.

Check all four orders, fixed endpoints, signed traversal entries and
the distinction between dimensionless and physical matrices. Continue
if this proves an all-plaquette cubic bound. Abandon this mechanism if
it requires a factorwise scalar-to-mixed extension or summing the
two-prefix kernel bound absolutely: that latter count loses a power.
Even success leaves convergence, a signed coefficient, full compensation,
finer asymptotics and the independent interacting/continuum/infrared gaps.

Completed in [L214](../lemmas/L214-complete-nonradial-action-cubic-bound.md).
The exact four-term row expansion closes the proposed local O(N)
bound, including every normal transverse end edge. Its complete
transverse 24-pair class and hence the complete L025 response are
O(a^-3). This is boundedness only; no signed coefficient or convergence
is established. No scripts or numerical sign premises were needed.
