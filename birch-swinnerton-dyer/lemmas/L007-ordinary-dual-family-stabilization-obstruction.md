# L007 — Ordinary tame duality selects crossed weight-one stabilizations

## Hypotheses

Let p be an odd prime and chi a finite-order Dirichlet character of
conductor prime to p. Fix a p-adic embedding of its values and of the
coefficients below. Let g be a normalized cuspidal newform of weight
one, nebentype chi, and level prime to p. Assume that its p-Hecke
polynomial has distinct roots alpha,beta, so

\[
X^2-a_p(g)X+\chi(p)=(X-\alpha)(X-\beta),\qquad
\alpha\beta=\chi(p).
\]

Put h = g tensor chi^(-1), the form dual to g in weight one. Label
its roots by their actual values alpha^(-1),beta^(-1), avoiding any
choice of their order.

Let bold g and bold h be ordinary families whose weight-one
specializations are g_alpha and h_eta, respectively, where
eta is one of these two inverse roots. Denote their continuous U_p
eigenvalue functions by A_g and A_h. Assume there is a sequence of
pairs of classical points (y_n,z_n) tending to these weight-one
points, with common integral weight k_n >= 2, such that:

- bold g_(y_n) and bold h_(z_n) are the ordinary p-stabilizations of
  normalized newforms G_n,H_n of levels prime to p;
- G_n has nebentype chi and H_n = G_n tensor chi^(-1).

These are explicit hypotheses on a proposed continuation of the
classical dual pairing. No existence of such a sequence on the
diagonal branch is assumed. A tame-twist identity throughout a family
with such accumulating classical points would supply this hypothesis.

## Conclusion

Necessarily

\[
\eta=\chi(p)^{-1}\alpha=\beta^{-1}.
\tag{1}
\]

Consequently this continuation of the ordinary tame-twist pairing
cannot pass through (g_alpha,h_(alpha^(-1))). Starting instead with
g_beta forces h_(alpha^(-1)), so it also cannot pass through
(g_beta,h_(beta^(-1))). Only crossed pairs of root labels can meet
these hypotheses; their existence is not a conclusion of this lemma.

This excludes only the proposed construction that keeps the two
ordinary families related by the indicated classical tame twist.
It neither excludes a trace projector at the weight-one fiber nor
proves nonexistence of a different motivic lift of a diagonal class.

## Proof

Write c = chi(p), a root of unity and hence a p-adic unit. The two
p-Hecke roots of G_n have product c p^(k_n-1). Since G_n is ordinary,
one root u_n is a unit; the other is

\[
v_n=c p^{k_n-1}/u_n,\qquad v_p(v_n)=k_n-1>0.
\]

Thus the unit root is unique, and u_n = A_g(y_n).

Twisting by chi^(-1) multiplies the p-th Hecke coefficient by c^(-1)
and changes the nebentype from chi to chi^(-1). This can be read
directly from the defining coefficient twist at indices coprime to
the character's conductor; p is such an index. The Hecke polynomial
of H_n is therefore

\[
X^2-c^{-1}a_p(G_n)X+c^{-1}p^{k_n-1}
 =(X-c^{-1}u_n)(X-c^{-1}v_n).
\]

Its unique unit root is c^(-1)u_n. Ordinary stabilization therefore
gives A_h(z_n) = c^(-1)A_g(y_n). Continuity at the limiting points
implies eta = c^(-1)alpha. The weight-one determinant identity
alpha beta = c now gives (1). As alpha != beta, their inverses are
different, excluding the first diagonal pair. Interchanging alpha
and beta proves the second assertion.

The dual terminology has no hidden rank assumption: for a
two-dimensional representation V, the map v to (w maps to v wedge w)
identifies V with V^dual tensor det(V). Thus the weight-one Artin
representation of h is V_g^dual. At higher weights the determinant
also has its cyclotomic factor; the usual self-dual normalization
of the tensor product supplies that factor. The lemma concerns the
explicit tame-twist relation of the underlying newforms and the
ordinary roots, so no weight-coordinate convention is needed.

For the research application, the checked maps are recorded in
[the construction audit](../foundations/08-diagonal-cycle-specialization.md).
The tested shortcut was to contract the two auxiliary factors via
their usual dual pairing throughout the family, then specialize a
cycle-valued construction to E. Its assumed classical tame-twist
identity fails the root test for the diagonal branch. A trace on the
isolated Artin fiber does not, by itself, repair this failed family
identification or produce an Abel--Jacobi-compatible map to rational
points.

The naming agrees with [Darmon--Rotger (2016), Section 4.5](https://link.springer.com/article/10.1186/s40687-016-0074-9),
where alpha_h = alpha_g^(-1) and beta_h = beta_g^(-1). In the more
restricted Castella--Hsieh setting, the already checked
[Theorem A](../foundations/07-castella-hsieh-nonvanishing.md) kills the
crossed classes. That vanishing is contextual evidence for why this
test matters; it is not used to prove the root obstruction above.
There is no new rational-rank bound or Kummer-membership claim.

## Mathlib

Full statement: **not checked**. Supporting coverage for polynomial
roots, valuations, Dirichlet twists, and continuity: **not checked**.
The root-switch argument is proved here. The direct references
identify the construction and its root labels; neither is cited as
a theorem asserting this full obstruction or the missing motivic lift.
