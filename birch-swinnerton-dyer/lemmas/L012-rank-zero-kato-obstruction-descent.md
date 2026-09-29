# L012 — The rank-zero Kato representative and its descended obstruction

## Hypotheses

Retain L011's hypotheses and notation, except that its optional
rational points P,Q are not assumed. Thus F = Q_p, p > 3,
V = V_p E, S = Sel(K,V) = S^+ has dimension two, R is relaxed at
both primes above p, and S_00 has zero localization there. Retain
the full auxiliary and coefficient restrictions of L009. In
particular L(E^K,1) != 0. Let chi = chi_K and V' = V tensor chi.

Use the Beilinson--Kato element z_tw for E^K with the normalization
in [the reciprocity input](../foundations/11-rank-zero-kato-reciprocity.md).
Fix the twist identification V_p E^K = V'. Its restriction identifies
V'|_(G_K) with V|_(G_K). Let Sigma contain p, infinity, the bad
primes, and the primes ramifying in K. All global cohomology below
uses the groups unramified outside Sigma.

Write d for the fixed anticyclotomic tangent, so d^tau = -d, and
A = F[epsilon]/(epsilon^2). The deformation tested here is
V_A^- = V(1 - epsilon d). Use L011's local pairing convention,
a_mathfrak_p of logarithm 1, and
a_- = (a_mathfrak_p,-tau a_mathfrak_p).

## Conclusion

Put w = res_K(z_tw), using the twist identification. Then

\[
w\in R^-,\qquad
\lambda=\langle a_{\mathfrak p},\operatorname{loc}_{\mathfrak p}w\rangle_{\mathfrak p}\ne0,
\qquad z^-={w\over2\lambda}.
\tag{1}
\]

Here z^- is exactly L011's normalized relaxed minus generator.
For every x in S_00, its mixed pairing is

\[
\langle\beta_{00,d}(x),w\rangle_{\rm PT}
       =2\lambda\,t_d(x).
\tag{2}
\]

The global relaxed lifting obstruction is

\[
\operatorname{ob}_{-d}(w)=-d\cup w
      \in H^2(K,V)^+.
\tag{3}
\]

It vanishes exactly when t_d vanishes on **all** of S_00. Under
L011's additional independent-point hypothesis this is its previous
zero-determinant test. No value of (3) is established here.

There is also a concrete formulation over Q. Extend d to the
F(chi)-valued cocycle tilde_d on G_Q by

\[
\widetilde d(h\tau^e)=d(h),\qquad h\in G_K,\quad e\in\{0,1\}.
\]

Define the four-dimensional F-representation W_d on V direct-sum V
by, for rho = rho_V,

\[
\rho_{W_d}(g)(u,v)=
 \bigl(\rho(g)u-\widetilde d(g)\chi(g)\rho(g)v,
                         \chi(g)\rho(g)v\bigr).
\tag{4}
\]

It fits in 0 -> V -> W_d -> V' -> 0. A relaxed lift of w to
V_A^- exists if and only if z_tw lifts to H^1(Q,W_d). The latter
connecting class is

\[
-\widetilde d\cup z_{\rm tw}\in H^2(\mathbf Q,V),
\tag{5}
\]

using F(chi) tensor V' = V. Its restriction is (3). This specifies
the extension in which a constructive lift must be found; it does
not construct that lift.

The cyclotomic tangent c satisfies c^tau = c. Its connecting class
c cup w is in H^2(K,V)^- = 0, whereas (3) is in the plus part.
Thus the cyclotomic family gives no vanishing of (3). The descended
representation (4) also does not supply an A-linear rank-two G_Q
deformation: its natural epsilon action anticommutes with tau.

These are a specialization of the cited reciprocity law and a
reproduction of the existing cohomological formalism. Neither a new
rank bound nor Kummer membership is proved. The threshold remains
the vanishing of an uncomputed global class, not merely lambda != 0.

## Proof

**The arithmetic representative and its normalization.** Restriction
from Q with coefficients V' is invariant for the action on V'.
Since chi(tau) = -1, identifying V' with V over K makes w
anti-invariant. At a split prime the local twist identification
respects the finite local Kummer condition. The reciprocity input
and L(E^K,1) != 0 show that loc_mathfrak_p(w) lies outside the finite
line. In particular w is nonzero. Away from p the rational local
H^1 groups vanish, as checked in L009 and used in L011, so w belongs
to the relaxed group R.

The finite local line is its own annihilator for the perfect local
Tate pairing. Its nonzero vector a_mathfrak_p therefore pairs
nontrivially with loc_mathfrak_p(w), proving lambda != 0. Since
w is anti-invariant,
loc_bar(w) = -tau loc_mathfrak_p(w). Conjugation preserves local
invariants, so

\[
\begin{aligned}
b(a_-)(w)
 &=\langle a_{\mathfrak p},\operatorname{loc}_{\mathfrak p}w\rangle
   +\langle-\tau a_{\mathfrak p},-\tau\operatorname{loc}_{\mathfrak p}w\rangle\\
 &=2\lambda.
\end{aligned}
\]

L011 gives dim R^- = 1 and the normalization b(a_-)(z^-) = 1.
This proves (1). Rescaling the chosen Kato element rescales lambda
by the same factor. No period factor or factor of 2 has been silently
absorbed. Equation (2) is L011's pairing formula applied to (1).

**The global obstruction.** For a cocycle f representing w, its
constant F-linear lift to V_A^- has coboundary

\[
(\partial_A f)(h,k)=-\epsilon d(h)\rho(h)f(k).
\]

Thus the coefficient connecting map is (3), in the fixed cup-product
convention. Its vanishing is equivalent to a global lift by the
cohomology exact sequence. The relaxed conditions add no obstruction
at p; away from p their local complexes remain acyclic for the
first-order extension. Such a global lift is consequently relaxed.

Duality identifies H^2(C_rel) with S_00^dual and with global H^2(K,V)
in this setting. L011's adjointness of the two Bocksteins says that
(3) is zero if and only if the left side of (2) vanishes for every
x in S_00. Since 2 lambda != 0, this is precisely the stated test.
If localization on S has not independently been shown nonzero, one
must retain all of S_00; evaluating on kappa alone need not suffice.
This avoids adding a hidden rank-one localization assumption.

S_00 is a subspace of S^+, so its dual, and hence H^2(K,V), is plus.
The sign of d cup w is positive because both d and w are negative.
The sign of c cup w is negative because c is cyclotomic. This proves
the assertion concerning the cyclotomic obstruction without identifying
the two tangent directions or assuming any height nondegeneracy.

**Descent of the actual inverse deformation.** The relation
d(tau h tau^(-1)) = -d(h) gives

\[
\widetilde d(g_1g_2)
 =\widetilde d(g_1)+\chi(g_1)\widetilde d(g_2).
\tag{6}
\]

This is the cocycle identity for F(chi). In particular the scalar
off-diagonal entry of the product of the two matrices in (4) is

\[
-\chi(g_2)\widetilde d(g_2)
 -\chi(g_1)\chi(g_2)\widetilde d(g_1)
 =-\chi(g_1g_2)\widetilde d(g_1g_2).
\]

Thus (4) defines a representation and the displayed extension.
The F-linear section v |-> (0,v) computes its connecting map:
the first component of the coboundary of a lifted cocycle z is
-tilde_d(g) chi(g) rho(g) z(k). This is exactly (5). Restriction
to K removes chi and gives (3).

For completeness the lift equivalence can also be checked directly.
Identify W_d|_(G_K) with V_A^- by (u,v) |-> v + epsilon u.
Its action is rho(h)(1 - epsilon d(h)). The natural semilinear
involution T on V_A^- sends v + epsilon u to
rho(tau)v - epsilon rho(tau)u. The action of tau in (4) is -T.
Any lift y of the anti-invariant w can be replaced by
(y - Ty)/2, still a lift and now anti-invariant for T. It is
therefore invariant for the W_d action of tau.

Restriction identifies H^1(Q,W_d) with H^1(K,W_d)^tau:
the positive-degree cohomology of the order-two quotient vanishes
over F, by averaging. The anti-invariant lift descends, and its
quotient descends to z_tw because restriction for V' is injective.
Conversely a lift of z_tw restricts to a lift of w. The same
restriction argument in degree two identifies H^2(Q,V) with
H^2(K,V)^+, so (3) and (5) vanish together.

Finally multiplication by epsilon on the underlying space is
N(u,v) = (v,0). Formula (4) at tau gives
rho_W(tau) N = -N rho_W(tau), with N != 0. Since p > 3, these
operators do not commute. The natural A structure is consequently
semilinear under tau, not an A-linear rank-two deformation over Q.
This checks the missing hypothesis in the proposed universal-deformation
shortcut; it does not rule out other constructions of a class in W_d.

**What the calculation leaves open.** Formula (2) expresses the
obstruction through the same t_d that was unknown in L011.
Reciprocity establishes the nonzero multiplier 2 lambda, not t_d.
No cochain cancelling (5), nonvanishing evaluation of (5), or
arithmetic counterexample has been obtained. In particular the
nonzero multiplier cannot be treated as a nonzero obstruction.
The existing bound r <= 2 is unchanged, and r >= 2 is still missing.

## Mathlib

Full coverage of this normalization and descended lifting criterion:
**not checked**. Supporting coverage for twist restriction,
connecting cup products, and finite-group averaging: **not checked**.
The reciprocity input retains the source's Section 1.1.3 and
Theorems 3.13--3.14 with direct links. L011 uses Nekovar's
*Selmer complexes*, Theorem 6.3.4 and Section 11.1.3, linked in
[the duality foundation](../foundations/10-selmer-bockstein-duality.md).
These support the inputs; no cited theorem or Mathlib match asserts
vanishing of (3) or (5). No originality claim is made for the
specialization and extension calculation above.
