# L175 — The actual first-factor Atiyah point projection

## Hypotheses

Retain L071, L108, L111, L116, L164, L165, L173 and L174's
conditional family and conventions. Thus X=S_1 x B has the identical
marked projective K3 factors, their fixed common metric, ordered triple,
holomorphic forms sigma_1,sigma_B and actual connection. The hypothetical
locally free rank-two product-polystable F has integral c_1(F)=0 and

\[
 \operatorname{ch}(F)=2-14e_1-21e_2-\tau_D+62e_1e_2.
\]

The full mixed class is retained. Write V=End_0(F), p:X -> B,
C=Rp_*V, M=R^1p_*V and W=R^2p_*V. Use the actual arrows
j:M[-1] -> C and a:C -> W[-2], and A=H^2(a):E -> U with
E=H^2(X,V), U=H^0(B,W). In particular M is locally free and W
has length one at each point of the finite reduced split set Z.
Put s=|Z|; Z may be empty and t=h^0(B,N) remains unknown.

Use L174's actual unscaled first-order Atiyah class a_X, the
Atiyah-first cup order, and its maps mathfrak a_1,mathfrak a_2 and
mathfrak a_perp. L173 fixes the sign by the positive deformation
class of bar-partial_F+epsilon a, and proves mathfrak a_2=iI,
where i=H^2(j). No other-factor Leray splitting is assumed.

Fix L071's generator k of NS(S_1) intersect h-perp, with k^2=-14,
and let L have c_1(L)=k. At each z in Z label the two summands
F_z=L direct sum L^{-1} by this same k. Write h_z=diag(1,-1)
in that labelled splitting. Let a_L be the line Atiyah class with
exactly the same unscaled first-order convention as a_X.

Let q(x,y)=integral_{S_1} x wedge y and retain
phi(u)=delta_u sigma_1 from L174, where
delta_{eta tensor v}(omega)=eta wedge iota_v omega.
Thus phi:H^1(S_1,T_S1) -> H^(1,1)(S_1) is an isomorphism.
Let chi_sigma in H^2(S_1,O) be normalized by
integral_{S_1} sigma_1 wedge chi_sigma=1. This is the fibre integral,
not a new choice of the base trace or of Q.

## Conclusion

For every u in H^1(S_1,T_S1) and every z in Z, L164's actual
top base-change isomorphism theta_z satisfies the intrinsic identity

\[
 \theta_z\bigl((A\mathfrak a_1(u))(z)\bigr)
       =h_z\,\operatorname{ev}(a_L\smile u).             \tag{1}
\]

With curvature R=nabla^2, first Chern convention
c_1(L)=[i R_L/(2pi)]=-[R_L/(2pi i)], and the fixed positive KS
convention above, its explicit value is

\[
 \operatorname{ev}(a_L\smile u)
       =-2\pi i\,q(\phi(u),k)\,\chi_\sigma.              \tag{2}
\]

In particular the normalized split trace coordinate is

\[
 \frac{(2\pi i)^{-2}}2
  \int_{S_1}\sigma_1\wedge
       \operatorname{Tr}\!\left(h_z\,
          \theta_z((A\mathfrak a_1(u))(z))\right)
          =-\frac{q(\phi(u),k)}{2\pi i}.                \tag{3}
\]

Define w_k in U by its components
(w_k)(z)=theta_z^{-1}(h_z chi_sigma). Finite reduced support
identifies U with the direct sum of these residue fibres. Then

\[
 A\mathfrak a_1(u)=A\mathfrak a_\perp(u)
                 =-2\pi i\,q(\phi(u),k)w_k.            \tag{4}
\]

If Z is nonempty, w_k is nonzero at every support point, the map
in (4) has rank exactly one, and its kernel is the nineteen-dimensional
hyperplane phi^{-1}(k^perp). If Z is empty, U=0 and the map has
rank zero and the whole twenty-dimensional domain as kernel.
Exchanging both labels k and -k leaves (1)--(4) as actual maps
unchanged; no independent point scalar is available in these coordinates.

This is a conditional ADVANCE / REPRODUCTION of the covered naturality
and Chern identities. The separate step 588 conceptual audit below
preserves (1)--(7), with EXPLORATION / REPRODUCTION and no substantive
mathematical correction or stronger conclusion. It evaluates
the point component, not the normal component or the actual map rank
assertions left open in L174. It gives no new square bound or exclusion
of F or s, constructs no F, and supplies neither transport nor primitive
Hodge realization. No progress beyond the checked general tools or
complete Hodge-conjecture candidate is claimed.

## Proof

**Imported identities and scope.** Reuse the invocation-start SPECIALIZE
assessment `drafts/literature/2026-10-27-first-factor-atiyah-point-projection.md`.
Import coefficient naturality and derived pullback of Atiyah classes
from Nikolas Kuhn, *The Atiyah class on algebraic stacks*, Forum Math.
Sigma **12** (2024), e100,
[Lemma 4.2 and Corollary 4.7](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/atiyah-class-on-algebraic-stacks/92C44757D4DCF43E4B6F368DDC5179EC).
The complete pullback square is also in
[arXiv:2306.13934v1, Corollary 4.7, p.32](https://arxiv.org/pdf/2306.13934v1#page=32).
F and the split lines are locally free, hence perfect and in the
required D^{<=0}; the fibre square is over C. Neither theorem requires
simple fibres. Kuhn's Corollary 5.10 identifies determinant trace.

For the line curvature normalization use the degree-one Chern--Weil
theorem with R=nabla^2 and c_1(L)=[i R_L/(2pi)]. Separately import
the Atiyah/Chern comparison in Buchweitz--Flenner, *A Semiregularity
Map for Modules and Applications to Deformations*,
[math/9912245v1, Remark 3.17 and Section 4 opening, pp.27--28](https://arxiv.org/pdf/math/9912245v1#page=27).
Their convention is ch=Tr exp(-At). This comparison does not itself
identify their At with the unscaled curvature cochain or fix the
notebook's KS sign. Those local conversions are checked below; their
At is not silently substituted for a_X. These exact source passages
were already assessed and were spot-checked for this normalization.

Derived base change is
[Stacks Lemma 36.30.4(1), 0B91](https://stacks.math.columbia.edu/tag/0B91);
compatibility with cup and evaluation is
[Lemma 20.31.8, 0H99](https://stacks.math.columbia.edu/tag/0H99).
The projection is proper, flat and finitely presented, and V is locally
free. Canonical truncation is
[Remark 13.12.4, 08J5](https://stacks.math.columbia.edu/tag/08J5).
L164 has already specialized these inputs to the same C,a,W and
fibre square. General naturality and Chern theorems are imported;
the work here compares the actual input and its normalization.

**The actual top edge on an arbitrary degree-two input.** For z in Z
let i_z:{z} -> B and ell_z:S_1 -> X be the fibre inclusions. Derived
base change identifies Li_z^*C with RΓ(S_1,V_z). Pulling back the
actual truncation triangle, Li_z^*(M[-1]) has cohomology only in
degree one because M is locally free. Thus H^2(Li_z^*a) is an
isomorphism onto H^2(Li_z^*(W[-2]))=W(z). L164 identifies it with
theta_z^{-1}. Equivalently, L111's minimal complex and its actual
top quotient both reduce the same last free term. The lower Tor
terms of W remain in lower degrees and have not been deleted.

Naturality of global restriction with a therefore gives, for every
x in E, not only for a bracket input,

\[
 \theta_z((Ax)(z))=\operatorname{res}_z(x).              \tag{5}
\]

On the W side the degree-two restriction is exactly ordinary
evaluation H^0(W) -> W(z). This is the comparison already used
in L164 before its specialization to brackets. It requires neither
ordinary middle base change nor a choice of an additive splitting.

**Restriction and the two line coefficients.** The cotangent map
ell_z^*Omega_X^1 -> Omega_S1^1 is projection onto the first factor.
Kuhn's pullback identity consequently sends the first component of
a_X to the Atiyah class of F_z. Trace-free projection commutes with
this operation. Cup/evaluation compatibility sends p_1^*u to u
in the same Atiyah-first order, without interchanging two degree-one
classes.

Coefficient naturality for each inclusion and projection of
L direct sum L^{-1} identifies its Atiyah class with the diagonal
matrix having entries a_L and a_{L^{-1}}. For lines, the Chern
identity gives a_{L^{-1}}=-a_L: both lines are in the same convention,
and their integral first Chern classes are k and -k. The trace is
therefore zero already. Subtracting half the trace does not remove
the diagonal matrix h_z a_L, nor does it introduce a factor one half.
Combining this with (5) proves (1). L094's off-diagonal degree-two
groups vanish; the surviving diagonal is the full one-dimensional
trace-free H^2 at the split fibre.

**Common normalization and cup order.** L108 writes the actual mixed
curvature as sum dz_j wedge r_j and identifies the fibre class of
r_j with the positive family KS class. L173 fixes exactly that
first-order sign for a_X. Locally this follows from
R_{z,bar w}=partial_z A_{bar w}-(bar-partial_A A_z)_{bar w}:
the second term is the horizontal Dolbeault coboundary, and the first
is the variation of bar-partial_F. Thus in this convention the
unscaled Atiyah Dolbeault cochain has coefficients r_j tensor dz_j,
with no 2pi i division or extra minus. The same convention applies
to a_L and to both cotangent factors.

Write R_L=sum dz_j wedge r_j and
u=sum eta_j tensor partial_j. Atiyah-first cup/evaluation gives
sum r_j wedge eta_j. In contrast delta_u R_L=sum eta_j wedge r_j.
Consequently, in H^2(O_S1),

\[
 \operatorname{ev}(a_L\smile u)
       =-[\delta_u R_L]
       =2\pi i\,\delta_u k.                            \tag{6}
\]

The last equality uses the degree-one identity [R_L]=-2pi i k,
not an inference from the even Chern character. One can compute
the line representative with any Hermitian metric: the resulting
Atiyah class is independent of that choice. This does not replace
the actual connection on F by a different family connection.

To pair (6), use the tensorial surface identity in L174 (10).
Indeed sigma_1 wedge k=0 by holomorphic degree, and delta_u is an
even derivation on total forms. Hence

\[
 0=(\delta_u\sigma_1)\wedge k+
                        \sigma_1\wedge\delta_u k,
 \qquad
 \int_{S_1}\sigma_1\wedge\delta_u k=-q(\phi(u),k).     \tag{7}
\]

Here forms representing the classes may be chosen closed, and the
contraction is the cohomological cup operation; no derivative of u
or limit is involved. H^2(O_S1) is one-dimensional and the displayed
integral is nonzero on chi_sigma. Equations (6)--(7) prove (2).
Since Tr(h_z^2)=2, substituting (1)--(2) in the fixed trace coordinate
proves (3), including its factor one half. A consistent change of
universal Atiyah sign changes all Atiyah inputs together; the intrinsic
identity (1) persists. In the retained convention no such change is made.

**Uniformity, rank, and the residual image.** L071 gives the exact
zero-slope line lattice Z k. A split charge-14 fibre has line class
r k with 14r^2=14, hence r=+/-1. Pic^0(S_1)=0 fixes the line
isomorphism class, so labelling the k summand at each point is
legitimate without constructing a splitting over a neighbourhood.
It also makes h_z intrinsic: the two lines are nonisomorphic and
the off-diagonal Hom groups vanish by L094. Labelling by -k instead
changes both h_z and q(phi(u),k) by a minus sign. Their product is
unchanged. No isomorphism of stalk generators with a common scalar
has been assumed; w_k is defined using the actual theta_z.

Finite reduced support gives (4)'s formula for A mathfrak a_1 by
evaluation at every point. If Z is nonempty, every component of w_k
is nonzero. The functional q(phi(-),k) is nonzero since its value at
phi^{-1}(k) is k^2=-14. Its domain has dimension twenty, proving
the stated rank and kernel. For Z empty the finite sheaf and U are
zero, proving the separate case.

Finally L174 defines mathfrak a_perp by adding to mathfrak a_1 an
element in the image of mathfrak a_2. L173 identifies that image
with iI, and the actual triangle gives Ai=0. Thus its subtraction
or addition has zero A-projection, proving the remaining equality
in (4). No Gram-rank equality for the actual residual map, evaluation
of its normal part, bracket integrability or existence of F was used.

**Separate conceptual audit (2026-10-27, step 588).** The unchanged
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-27-first-factor-atiyah-point-critical-audit.md`
covers exactly this audit. The named naturality, cup, truncation and
Chern inputs are reused with their stated hypotheses. The published
Kuhn Corollary 5.10 is the determinant-trace result; no assertion is
borrowed from the differently numbered v1 Proposition 5.10. The
cited BF Remark 3.17 and Section 4 opening were spot-checked again:
they supply the Atiyah/Chern comparison, not an independent curvature
normalization or the notebook's positive KS sign. The attribution
above now separates that comparison from the named Chern--Weil theorem.
This clarification changes none of (1)--(7).

First, take an arbitrary x in E as a morphism O_B[-2] -> C. Its
composite with a is the class Ax in H^0(W). Derived pullback of
this equality gives the restriction square without assuming x is a
Yoneda bracket. Since M is locally free, the two terms flanking
H^2(Li_z^*a) in the triangle's long exact sequence are H^2(M(z)[-1])
and H^3(M(z)[-1]), both zero. Its target is W(z); Tor_1(W,k(z))
and Tor_2(W,k(z)) remain in degrees one and zero. Pulling back the
morphism O_B -> W representing Ax induces on degree zero precisely
(Ax)(z). L111's last free-term reduction and L164 fix the inverse
top map as theta_z. This verifies (5)'s direction and scalar, with
no statement that the ordinary and derived middle fibres coincide.

The fibre cotangent map kills the base factor. Applying Kuhn's
pullback identity and coefficient naturality to the two inclusions
and projections therefore gives diag(a_L,a_{L^{-1}}) for the actual
restricted first-factor class. The two line classes are opposite,
so this is diag(a_L,-a_L). Its trace-free projection is itself:
the factor 1/2 multiplies its zero trace, not its diagonal entry.
The unchanged Atiyah-first cup order then proves (1). L094 gives
H^2(L^{2})=H^2(L^{-2})=0, so h_z H^2(O) is the entire trace-free
top fibre, not merely an arbitrarily selected line in it.

The first-order sign can be checked before invoking any Chern
character. In a smooth frame write the connection components as
A_z and A_bar_w. For R=nabla^2 its dz wedge dbar_w coefficient is
partial_z A_bar_w - partial_bar_w A_z + [A_z,A_bar_w], namely
partial_z A_bar_w - (bar-partial_A A_z)_bar_w. Modulo the vertical
Dolbeault coboundary this is the derivative of bar-partial_F with
a plus sign, exactly L108/L173's positive KS convention. It fixes
the coefficient r tensor dz of the unscaled class on either factor;
it introduces no 2pi i. Applied to a line in a holomorphic frame it
also reads r=-bar-partial A_z. This is the same convention, not a
new sign chosen at a split fibre.

Now check a single tensor term: for R_L=dz_j wedge r_j and
u=eta tensor partial_j, the coherent Atiyah-first contraction is
r_j wedge eta, while delta_u R_L=eta wedge r_j. They differ by
minus one. The named Chern--Weil normalization gives
[R_L]=-2pi i k, so their cohomology relation is exactly (6).
For the surface sign take sigma=dz_1 wedge dz_2 and the same term
with j=1. Then phi(u)=eta wedge dz_2 and
(eta wedge dz_2) wedge (dz_1 wedge r_1)
=-sigma wedge eta wedge r_1. The j=2 term has the same identity;
bilinearity, or the even derivation applied to sigma wedge k=0,
gives (7). Closed representatives and Dolbeault cup compatibility
make these tensor identities cohomological. Consequently the integral
of (6) against sigma is -2pi i q(phi(u),k), verifying (2).
The trace in (3) is twice this value because Tr(h_z^2)=2; multiplying
by (2pi i)^(-2)/2 gives exactly its displayed scalar. No even-degree
Chern-character calculation has been used to infer the first-order sign.

Finally L071's retained lattice makes the charge equation 14r^2=14,
so the line classes at each split fibre are exactly +/-k. Pic^0=0
fixes their isomorphism classes, and L094's vanishing off-diagonal
Hom groups makes the two labelled subbundles, and hence h_z,
independent of their scalar trivializations. A simultaneous exchange
k -> -k changes h_z and w_k as well as the functional by minus one.
It leaves the actual map unchanged. Finite reduced support makes
evaluation U -> direct sum W(z) an isomorphism; theta_z and
chi_sigma make each component of w_k nonzero. The functional is
nonzero at phi^{-1}(k), with value -14. This proves the rank-one
and nineteen-dimensional-kernel claims when Z is nonempty. For
Z empty, W=U=0 and the twenty-dimensional domain is all kernel.
Neither case prescribes s or t.

L174's actual correction lies in im(mathfrak a_2)=im(iI), and
consecutive arrows in the truncation triangle give Ai=0. It
therefore has zero point projection, verifying the residual equality
in (4) without a choice of lift of U. The full original input list
in the DAG is sufficient and unchanged. The audit preserves the
conditional point formula; it finds no substantive mathematical error,
new normal constraint, actual residual-rank equality, bracket value
or exclusion. F existence and primitive realization remain open.

## Mathlib

Full matching coverage of this actual derived point projection and its
Atiyah/KS/Chern normalization has **not been checked**. No absence claim
or Lean verification is made. The cited primary theorems supply the
general inputs; the displayed family specialization has received the
separate informal audit above, not a formal verification.
