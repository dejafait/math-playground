# L174 — Rank fifteen in the first-factor residual Atiyah Gram form

## Hypotheses

Retain the full conditional family and fixed conventions of L071,
L108, L116, L165 and L173. Thus X=S_1 x B is the product of the
identical marked projective K3 surfaces, with their original common
metric, ordered triple, identical holomorphic forms sigma_1,sigma_B
and actual connection. The hypothetical locally free rank-two bundle
F is product-polystable, has integral c_1(F)=0, and has

\[
 \operatorname{ch}(F)=2-14e_1-21e_2-\tau_D+62e_1e_2.
\]

Here e_i is the normalized factor point class and tau_D is L071's
full integral mixed class, including its transcendental part. Its
q-self-adjoint Hodge correspondence D satisfies D sigma=d sigma,
where d=2lambda and lambda is the positive root of
f(z)=z^3+z^2-2z-1. In H^2(S,C) its eigenvalues are d, 2mu, 2nu
with multiplicity seven each, and 4 with multiplicity one; mu,nu
are the other two roots of f. These are the retained full spectrum
in L071's audited mixed-square computation, not only divisor data.

Set V=End_0(F) and E=H^2(X,V). Use L165's actual symmetric complex
Serre form Q, normalized with L108's relative matrix-trace factor
(2pi i)^(-2) and the fixed base trace. Keep L116's actual maps j,r,a
and L173's i,I. Thus the known base image is iI H^1(B,T_B), not an
arbitrarily chosen twenty-dimensional subspace. The finite reduced
split set Z may be empty; s=|Z| and t=h^0(B,N) remain unknown.

Let a_X be the trace-free Atiyah class with the one global first-order
extension sign of L173. Use this same sign on both cotangent factors.
For u in H^1(S_i,T_{S_i}) define the actual maps

\[
 \mathfrak a_i(u)=\operatorname{ev}(a_X\smile p_i^*u)
       \in E,\qquad \mathfrak a_2=iI.                 \tag{1}
\]

The cotangent and tangent coefficient bundles in (1) have degree
zero; the cup order is Atiyah class first and u second. Both have
cohomological degree one, so the output has degree two. The second
equality is L173's global identity, including the finite top term.
No corresponding Leray splitting for p_1 is assumed.

Write L=H^(1,1)(S) and q(x,y)=integral_S x wedge y, identifying the
factors by their fixed markings and forms. The bundle isomorphism
T_S -> Omega_S^1 induced by sigma identifies H^1(T_S) with L.
To fix its de Rham sign, write this identification as

\[
 \phi(u)=\delta_u\sigma,\qquad
 \delta_{\eta\otimes v}(\omega)=\eta\wedge\iota_v\omega,
                                                               \tag{2}
\]

for a Dolbeault (0,1)-form eta and a (1,0)-vector v. Let gamma be
the fixed nonzero base-trace scalar defined by
Tr_B(z)=gamma integral_B sigma_B wedge z for z in H^2(O_B).
The forms here are bilinear over C, not Hermitian.

## Conclusion

For u,v on either marked factor put x=phi(u), y=phi(v). All four
ordered Gram blocks of the actual maps (1) are

\[
 \begin{aligned}
 Q(\mathfrak a_1u,\mathfrak a_1v)&=\gamma d\,q(x,y),\\
 Q(\mathfrak a_2u,\mathfrak a_2v)&=\gamma d\,q(x,y),\\
 Q(\mathfrak a_1u,\mathfrak a_2v)&=-\gamma q(Dx,y),\\
 Q(\mathfrak a_2u,\mathfrak a_1v)&=-\gamma q(Dx,y).
 \end{aligned}                                             \tag{3}
\]

Let P_2 be Q-orthogonal projection onto the nondegenerate actual
base image mathfrak a_2 H^1(T_B), and put

\[
 \begin{aligned}
 \mathfrak a_\perp(u)
   &:=(1-P_2)\mathfrak a_1(u)\\
   &=\mathfrak a_1(u)+\mathfrak a_2
                    \bigl(\phi^{-1}(D\phi(u)/d)\bigr).
 \end{aligned}                                             \tag{4}
\]

Then its exact pulled-back Gram form is

\[
 Q(\mathfrak a_\perp u,\mathfrak a_\perp v)
       =\gamma q\bigl((d-D^2/d)x,y\bigr),\qquad
 \operatorname{rank}(d-D^2/d)|_L=15.                       \tag{5}
\]

The full forty-dimensional pulled-back form (3) has rank 35.
In particular there is a specified fifteen-dimensional subspace of
the first-factor domain whose residual image is Q-nondegenerate
and orthogonal to the base image. Its Q-transpose gives fifteen
independent Serre functionals, independent also of L173's twenty
base functionals. This is a certificate of positive rank, not a
claim of positivity of a complex bilinear form.

The possible five-dimensional radical of the pulled-back residual
form is not proved to map to zero. Thus (5) does not assert that
the actual residual map or the full Atiyah map has rank exactly
15 or 35. No normal/point placement of these extra functionals,
actual bracket, improved square count, exclusion of F or split
cardinality, transport, or primitive Hodge realization is proved.
This is a conditional ADVANCE / REPRODUCTION of the assessed trace
identities and retained correspondence data. The separate conceptual
audit below preserves the certificate without a substantive correction
or stronger conclusion (EXPLORATION / REPRODUCTION). No progress beyond
the checked general theorems or complete Hodge-conjecture candidate is
claimed.

## Proof

**Imported identity and its applicability.** Reuse the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-26-first-factor-residual-atiyah-detector.md`.
Import Buchweitz--Flenner, *A Semiregularity Map for Modules and
Applications to Deformations*, Compositio Math. 137 (2003), 135--210,
[arXiv:math/9912245v1, Definition 4.1, Proposition 4.2 and
Corollary 4.3, printed pp.28--29](https://arxiv.org/pdf/math/9912245v1#page=28).
Their character is Tr(exp(-At)); for r=2, k=1 the contraction identity
applies to every H^1(T_X) input. Their shifted coefficient contraction
is a derivation, compatible with trace and coefficient cup products.
The statement and complete relevant Proposition 4.2 proof were
retrieved for this specialization. F is locally free and hence
perfect, and X is smooth projective over C. No semiregularity
injectivity or hypothesis about the fibres of either projection is
used in this identity.

Here are the necessary normalization and sign checks, rather than a
reproof of that general theorem. Write the actual curvature locally
as R_0=sum dz_j wedge r_j after taking its trace-free part. In the
coherent-cup convention of (1), contraction with u=sum eta_j tensor
partial_j is represented by sum r_j wedge eta_j, with L173's one
universal first-order sign. On de Rham forms delta_u R_0 is instead
sum eta_j wedge r_j. The two are negatives. The same negative,
and the same possible universal Atiyah sign, occur for both factors;
they disappear in the product of two contracted classes. In BF's
shifted algebra these H^1(T) contractions have degree two, while
At has degree zero. There is consequently no odd derivation sign
between the two Atiyah factors. In the resulting coherent cup the
two contracted classes have degree two, also giving positive cyclic
trace sign. A factor-dependent sign cannot be inserted.

Integral c_1(F)=0 makes Tr(At(F)) zero in H^1(Omega_X^1). Indeed
this is the first Chern class under the Dolbeault/de Rham comparison.
Projecting a rank-two class to End_0 changes half its traced square
by minus one quarter of the square of its trace. That correction
is zero here. Equivalently the trace-free curvature satisfies

\[
 \beta:=\operatorname{ch}_2(F)
    =\left[\frac{\operatorname{Tr}(R_0\wedge R_0)}
                         {2(2\pi i)^2}\right].          \tag{6}
\]

This is a cohomological assertion about the given connection; it
does not replace it by a connection with new metric properties.
The scalar Atiyah summand therefore contributes nothing to (3).

In the de Rham convention (2), delta_u has bidegree (-1,1) and is
an even derivation on total forms. It acts on the coefficient forms,
not by differentiating u. Since delta_u R_0 has type (0,2), its
further coefficient contraction by any v is zero. Specializing the
imported trace/derivation identity thus gives

\[
 \delta_v\delta_u\beta
  =\left[\frac{\operatorname{Tr}
                (\delta_u R_0\wedge\delta_v R_0)}{(2\pi i)^2}\right].
                                                               \tag{7}
\]

The two ordered terms from the first contraction cancel the 2! in
(6); there is no residual factor two. All inputs are pulled back
to X before this formula is used. They are global H^1 classes,
not ordinary vector fields substituted for them.

L165's relative normalization and composition with the fixed base
trace make the global form on Dolbeault degree-two representatives
equal to gamma (2pi i)^(-2) times integral_X sigma_1 sigma_B Tr(xy).
Using the two signs just checked in (7), this yields the single
formula for all ordered choices of factors:

\[
 Q(\mathfrak a_i u,\mathfrak a_j v)
   =\gamma\int_X\sigma_1\sigma_B\,
                  \delta_{p_j^*v}\delta_{p_i^*u}\beta.  \tag{8}
\]

The holomorphic volume forms have even degree. The tensor-shift sign
in L165 is already present in the actual product, not an additional
sign to attach to only one block. We will verify the base block
against that sign explicitly below.

**Surface contraction signs.** Let C(u,v) in H^2(O_S) be the cup
of u and v followed by the alternating coefficient form sigma.
It is symmetric, since the cohomological degree-one interchange
and coefficient alternation each contribute minus one. Locally take
sigma=dz_1 wedge dz_2, u=eta_1 tensor partial_1+eta_2 tensor partial_2
and v=theta_1 tensor partial_1+theta_2 tensor partial_2. Directly,

\[
 \begin{aligned}
 \delta_u\sigma&=\eta_1\wedge dz_2-\eta_2\wedge dz_1,\\
 \delta_v\delta_u\sigma&=\eta_1\wedge\theta_2
                            -\eta_2\wedge\theta_1=C(u,v),\\
 (\delta_u\sigma)\wedge(\delta_v\sigma)
                         &=-\sigma\wedge C(u,v).
 \end{aligned}                                             \tag{9}
\]

These tensorial identities imply
integral sigma C(u,v)=-q(phi(u),phi(v)). For any x in L,
the form sigma wedge x is zero by holomorphic degree on a surface.
Applying the even derivation delta_u gives a second identity:

\[
       \int_S\sigma\wedge\delta_u x=-q(\phi(u),x).     \tag{10}
\]

This proves the signs needed for both kinds of block without a
choice of positive real form or any star operation.

**Retain the full mixed tensor.** Put c_sigma=q(sigma,barsigma),
which is nonzero. The Hodge-orthogonal decomposition
H^2(S,C)=C sigma direct sum L direct sum C barsigma, with the two
outer lines paired together, and the equality D sigma=d sigma give

\[
 \tau_D=\frac{d}{c_\sigma}
       (\sigma_1\otimes\bar\sigma_B
                  +\bar\sigma_1\otimes\sigma_B)+\tau_L. \tag{11}
\]

Here tau_L in L tensor L represents the full D|_L. In particular
if tau_L=sum x_a tensor y_a, then
sum q(x,x_a)q(y,y_a)=q(Dx,y). This is a decomposition over C for
calculation, not a separate integral NS/transcendental splitting.

For two first-factor contractions, only the first term displayed
in (11) survives. A second contraction on a (1,1) factor is zero
because the first has already removed its sole holomorphic degree.
Contraction of barsigma is zero. The pure term -14e_1 would lie in
H^4(S_1,O_S1)=0 after two contractions, and e_2 is untouched by a
first-factor contraction. Thus (8), (9), and beta=-14e_1-21e_2-tau_D
give

\[
 \begin{aligned}
 Q(\mathfrak a_1u,\mathfrak a_1v)
  &=-\gamma\frac d{c_\sigma}
          \left(\int_{S_1}\sigma_1 C(u,v)\right)
          \left(\int_B\sigma_B\bar\sigma_B\right)\\
  &=\gamma d\,q(\phi(u),\phi(v)).
 \end{aligned}                                             \tag{12}
\]

For two base contractions the second term of (11) gives the same
calculation; now the pure term -21e_2 has zero H^4(B,O_B) image.
This verifies both self blocks despite the unequal factor charges.
It also matches the actual base comparison: L108 gives the pulled-back
relative coefficient form d sigma_B, whereas L165 gives S=-B_M.
Consequently Q(iIu,iIv)=-d Tr_B C(u,v)=gamma d q(phi(u),phi(v))
by (9). Formula (12) has exactly that sign and normalization.

For one contraction on each factor, neither pure point term
contributes, and the two outer terms of (11) are killed by the
contraction on their antiholomorphic factor. Only tau_L remains.
The contractions are even and the factor classes have total degree
two, so separating the factors adds no exterior interchange sign.
Equations (8) and (10) give

\[
 \begin{aligned}
 Q(\mathfrak a_1u,\mathfrak a_2v)
   &=-\gamma\sum_a
       \left(\int_{S_1}\sigma_1\delta_u x_a\right)
       \left(\int_B\sigma_B\delta_v y_a\right)\\
   &=-\gamma q(D\phi(u),\phi(v)).
 \end{aligned}                                             \tag{13}
\]

Interchanging the two degree-two outputs in Q has sign +1;
q-self-adjointness of D gives the fourth ordered block in (3).
All blocks therefore use the same gamma and the full D.

**Actual projection and its rank.** The restriction of q to L is
nondegenerate: it is the orthogonal complement of the nondegenerate
plane spanned by sigma,barsigma in H^2(S,C). Since gamma d is
nonzero, (3) also proves nondegeneracy of the base image, consistently
with L173. Pairing mathfrak a_1(u) with every mathfrak a_2(v) shows

\[
 P_2\mathfrak a_1(u)
        =-\mathfrak a_2\bigl(\phi^{-1}(D\phi(u)/d)\bigr).
\]

This is the actual Q-orthogonal projection, since its difference
from mathfrak a_1(u) pairs to zero with that whole image. Expanding
its complement by all four blocks of (3) gives

\[
 \gamma d q(x,y)-\frac{\gamma}{d}q(Dx,Dy)
          =\gamma q((d-D^2/d)x,y),
\]

as asserted. No projection through a second Leray decomposition
has entered.

For completeness, the root separation used in this rank calculation
is exact. The values of f at -2,-3/2,-1/2,0,1,5/4 are respectively
-1,7/8,1/8,-1,-1,1/64. Thus its three roots lie in the disjoint
intervals (-2,-3/2), (-1/2,0), and (1,5/4), exhausting its degree.
In particular their absolute values are distinct. The retained
spectrum of D is semisimple: on the cubic summands its annihilating
polynomial has simple roots, and the additional one-dimensional
block is 4. Because D is q-self-adjoint, distinct eigenspaces are
q-orthogonal and each is nondegenerate.

The d-eigenspace in H^2 has dimension seven and contains sigma
and barsigma. Removing their nondegenerate plane leaves dimension
five in L. All other eigenspaces lie in L. Hence on L the
eigenvalue multiplicities of D are

\[
 \begin{array}{c|rrrr}
 \text{eigenvalue}&d&2\mu&2\nu&4\\ \hline
 \text{multiplicity}&5&7&7&1 .
 \end{array}
\]

The operator d-D^2/d is zero precisely on the first of these:
the other cubic roots have different absolute values and 2<d<5/2<4.
Its rank is therefore 7+7+1=15. Let L_* be the direct sum of these
last three eigenspaces. Its residual Gram restriction is nondegenerate,
so mathfrak a_perp is injective on phi^(-1)(L_*). Its image has
dimension fifteen and is orthogonal to the actual base image.
The Q-transpose restricted to this nondegenerate image is invertible,
giving fifteen independent functionals. A combination of them
cannot be a combination of the base functionals: evaluate on the
residual image and then on the base image to force both coefficients
to zero.

Finally, orthogonal elimination of the base block of (3) is an
invertible change of coordinates on the forty-dimensional domain.
It leaves a nondegenerate rank-twenty base block and the rank-fifteen
residual block. The full pulled-back rank is exactly 35. A vector
in the remaining five-dimensional domain radical might still have
nonzero isotropic image orthogonal to the whole Atiyah image.
Neither its vanishing nor a sharper actual map rank follows.
The bound exceeds the required continuation threshold of positive
residual rank, but determines none of the normal or point operations.

**Separate conceptual audit (2026-10-27, step 584).** This audit uses
the unchanged invocation-start SPECIALIZE assessment for the same
two-factor Gram target. It checks the specialization conditional on
the stated local inputs, rather than independently reproving their
entire ancestry. BF Definition 4.1, the coefficient construction,
the full proof of Proposition 4.2 and Corollary 4.3 were rechecked
at [the cited primary version, printed pp.28–29](https://arxiv.org/pdf/math/9912245v1#page=28).
The domain really includes H^1(T_X) (r=2); the shifted contraction
has even degree and is trace-compatible. Locally free F on smooth X
meets perfectness. This confirms the already covered identity, not
a new literature assessment or an injectivity theorem.

The determinant correction is cohomological. If a is a rank-two
Atiyah class and c=Tr(a), then a_0=a-id_F c/2 satisfies
Tr(a_0^2)/2=Tr(a^2)/2-c^2/4, with products in the shifted algebra.
Integral c_1(F)=0 makes c=0 after the Dolbeault comparison, regardless
of the universal sign convention. For curvature the same calculation
is valid modulo exact forms; it does not require pointwise zero trace
curvature. Closed tangent-valued Dolbeault representatives define
coefficient contractions on Dolbeault cohomology, so replacing that
representative does not alter (7) or its Serre integral. No metric or
connection is replaced by this argument.

For the signs, write a curvature summand dz_j wedge r_j. Coherent
cup in (1) contracts it to r_j wedge eta_j, while (2) gives
eta_j wedge r_j. Their minus sign is identical for the two factors.
Both universal Atiyah signs therefore cancel in a pairing. Applying
two even contractions to Tr(R_0^2)/2 gives two equal traced terms;
the terms with two contractions on one R_0 vanish by holomorphic
degree. The coefficient is exactly one, not two or one half.
This verifies (7) independently of the Serre normalization. The
coefficient trace in Q has precisely L108's factor (2pi i)^(-2),
and composition with the base trace gives the single gamma in (8).

The surface sign can be checked on the ordered local pair
u=eta tensor partial_1, v=theta tensor partial_2, with
sigma=dz_1 wedge dz_2: delta_u sigma=eta wedge dz_2,
delta_v sigma=-theta wedge dz_1, and their product is
-sigma wedge eta wedge theta. Reversing the vector indices reverses
both alternating coefficients; equal vector indices give zero.
By bilinearity this checks all terms of (9). Applying the even
derivation to the identically zero sigma wedge x for a (1,1)-form
x then gives (10), with its minus sign. This computation uses no
Hermitian positivity.

Now retain every Kunneth component of beta. Two contractions on
factor 1 kill its point term by antiholomorphic degree four on that
surface; they also kill tau_L and the barsigma_1 term. Exactly
-(d/c_sigma) sigma_1 tensor barsigma_B remains before contraction.
It yields +gamma d q by (9). Exchanging the factors gives the
same block; the unequal coefficients -14 and -21 never survive.
One contraction on each factor kills both pure terms and the two
outer Hodge components of tau_D. For tau_L the two signs from (10)
multiply to plus, leaving the original minus in beta. Its contraction
is therefore -gamma q(Dx,y). The factor classes have even total
degree, and the two resulting obstruction classes both have degree
two; reversing their order adds no sign. Self-adjointness of D
then verifies both ordered mixed blocks, rather than assuming their
sign by analogy with the self blocks.

The independent actual-map check uses L173's identity mathfrak a_2=iI,
L108's relative form d sigma_B and L165's S=-B_M. Together they give
Q(iIu,iIv)=-d Tr_B C(u,v)=gamma d q(phi(u),phi(v)). Thus the
curvature computation matches the actual inclusion and its tensor
shift. This comparison retains W and requires no other-factor Leray
splitting or ordinary middle base change at a split point.

For the projection, nondegeneracy of gamma d q on L implies that
mathfrak a_2 is injective and its image is nondegenerate. Pairing
mathfrak a_1(u)+mathfrak a_2(phi^{-1}(Dx/d)) against this image
gives zero for every x=phi(u). Expanding its self-pairing gives,
in order, one gamma d q term, two -gamma q(Dx,Dy)/d terms and
one +gamma q(Dx,Dy)/d term. This reproduces (5) with the actual
orthogonal projection, including its sign.

Finally the retained construction behind L071 supplies f(U)=0 on
the transcendental summand and f(A_c|_W)=0 on its three-dimensional
divisor summand, with the remaining divisor line scalar 4 for D.
Thus semisimplicity follows from the simple roots, not merely from
self-adjointness for an indefinite form. The six rational endpoint
values of f displayed above check exactly; the three disjoint root
intervals exhaust its degree and have pairwise disjoint absolute-value
intervals. With L071's multiplicities, removing sigma,barsigma leaves
5,7,7,1 in L. Hence d-D^2/d vanishes on precisely the five-dimensional
d-eigenspace. The other three eigenspaces are q-nondegenerate and
give rank 15. Orthogonal elimination adds the base rank 20 to give
35. Neither calculation establishes vanishing of the actual image
of the five radical directions.

All stated cases survive, including empty Z and t=0: neither s nor t
enters this Gram calculation. No substantive defect or stronger bound
was found. The certificate exceeds the required positive-rank threshold,
but the actual normal/point placement and bracket values remain open.
This completed audit is EXPLORATION / REPRODUCTION; it neither improves
the certificate nor constructs F or algebraic representatives of
primitive Hodge classes. No mathematical script was used.

## Mathlib

Full matching coverage for the trace--Atiyah contraction identity and
this actual two-factor Serre Gram specialization has not been checked;
no absence claim is made. The cited primary theorem supplies the
general identity. The tensor signs, full-spectrum substitution and
actual orthogonal projection above are an informal specialization,
not formal verification. The separate conceptual audit preserves
these qualifications and does not establish formal coverage.
