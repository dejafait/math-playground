# Lemma 846: an angular period excludes finite real-box relative replacement

## Hypotheses

Use the actual entire completion of L018 and the function and radius
from L775,

\[
 G(z)=\frac18\xi\left(\frac12+\frac{\sqrt z}{2}\right),
 \qquad R=R_1>0,\qquad RG'(R)/G(R)=1,\qquad G(R)>0.
\]

Evenness gives an entire G, not a choice of a square-root branch.
Set

\[
 X=(\mathbb C\setminus\{0\})^2,\qquad
 Z=\{(z_1,z_2)\in X:G(z_1)G(z_2)(z_1-z_2)=0\}.
 \tag{1}
\]

All homology below is ordinary singular relative homology; chains
are finite. Let T be the product |z_1|=|z_2|=R, oriented by the two
counterclockwise circles in coordinate order. For any ordered,
separated intervals I_j=[a_j,b_j] of L845 with
0<a_1<b_1<a_2<b_2, let B be the image of I_1 x I_2 under

\[
 \phi(t_1,t_2)=(-4t_1^2,-4t_2^2),
 \tag{2}
\]

oriented by the pushforward of dt_1 wedge dt_2. Each endpoint is a
positive real Xi zero, and each interval has no other distinct real
zero in its interior. The collection of allowed B includes every such
pair, not just the first two intervals. Reversing orientation is allowed
by a negative chain coefficient. Write [T] and [B] for their relative
fundamental classes, represented by finite triangulations. The torus
may meet Z. No hypothesis that these chains lie in X minus Z is made.

Retain exactly L845 (4) at r=2,k=1 and its complete volume form:

\[
 F_2(z_1,z_2)=-\frac{R^2}{G(R)^2}
    \frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},\qquad
 \omega=F_2\,\frac{dz_1}{iz_1}\wedge\frac{dz_2}{iz_2}.
 \tag{3}
\]

No RH, simplicity of zeros, normal-crossing hypothesis, stationarity
or Hessian nondegeneracy is assumed in this homology test.

## Conclusion

The smooth real closed form

\[
 \eta_j=\operatorname{Im}\frac{dz_j}{z_j},\qquad
 \beta=\frac{\eta_1\wedge\eta_2}{(2\pi)^2}
 \tag{4}
\]

defines a relative period on H_2(X,Z;R), with

\[
 \langle\beta,[T]\rangle=1,\qquad
 \langle\beta,[B]\rangle=0
 \quad\hbox{for every allowed box B}.                         \tag{5}
\]

Consequently, for every finite list B_1,...,B_N and real coefficients
c_1,...,c_N,

\[
 [T]\ne\sum_{\nu=1}^N c_\nu[B_\nu]\quad\hbox{in }H_2(X,Z;\mathbb R).
 \tag{6}
\]

In particular no finite integer relation of this form holds in
H_2(X,Z;Z). The full form omega also has a well-defined relative
pairing. A relative class equality would therefore imply equality of
its full-form integrals, including their volume factors; (6) excludes
that proposed justification for finite-box replacement.

This does not exclude an accidental equality of the integrals of omega
alone. It makes no assertion about infinite or locally finite chains,
other contours, saddle participation by other mechanisms, signs of
minors, or RH. It is a local obstruction obtained from known topology
and integration inputs, not a new general homology theorem. The
invocation-start search did not locate this exact application; no
claim of certified originality is made. The separate conceptual audit
below accepts this statement at exactly its finite-chain scope.

## Proof

### Imported inputs and the actual representatives

Use the source coverage saved before this attempt in
`drafts/literature/2026-11-06-real-zero-box-relative-cycle-test.md`.
The following are imported, not reproved:

* Allen Hatcher, *Algebraic Topology* (2002),
  [Section 2.1, pp.115–117](https://pi.math.cornell.edu/~hatcher/AT/ATch2.pdf#page=19):
  the relative chain complex is C_*(X)/C_*(Z). In particular, equality
  of two relative cycles means their difference is a boundary in X
  plus a chain in Z. This definition and the exact-sequence input of
  Theorem 2.16 require no good-pair or compactness hypothesis.
* Leonid Shartser and Guillaume Valette, *De Rham Theorem for
  L-infinity forms and homology on singular spaces*,
  [arXiv:1002.4143v1, 22 February 2010](https://arxiv.org/pdf/1002.4143v1),
  Definitions 2.2/2.10/2.14, Proposition 2.13 and Theorem 3.6
  (pp.12–14 for the Stokes theorem and proof): integration of bounded
  smooth stratified forms with bounded exterior derivative over
  continuous semialgebraic chains on compact semialgebraic sets is
  well defined, independent of compatible refinements, and satisfies
  Stokes. The forms themselves need not be semialgebraic (p.2).
* Mário J. Edmundo and Arthur Woerheide, *Comparison theorems for
  o-minimal singular (co)homology*,
  [institutional manuscript revised 4 September 2006](https://repositorioaberto.uab.pt/bitstreams/e3125e0f-316c-403f-b987-e0d9aecc5aca/download),
  Theorems 1.1/1.2 and the real-field comparison paragraph (pp.2–3),
  with the pair comparison and naturality in Section 7 (pp.30–31):
  semialgebraic and ordinary singular homology over the real field
  agree naturally, for pairs and coefficient modules. We use the
  comparison taking a semialgebraic simplex to the same continuous
  simplex, with real parameters and real or integer coefficients.
  The published article is *Trans. Amer. Math. Soc.* **360** (2008),
  4889–4912, DOI 10.1090/S0002-9947-08-04403-6; page and theorem
  references here are to the inspected institutional manuscript.

L845 supplies the existence of the separated intervals and the exact
identity G(-4t^2)=Xi(t)/8. A box is a compact smoothly embedded real
rectangle: each derivative -8t_j is nonzero because t_j>0.
On each boundary edge at least one Xi endpoint vanishes. Thus
partial B lies in Z, including all corners. The closed torus has
zero boundary. These are valid relative cycles even where T meets
the diagonal or a coordinate-zero branch. Their geometric supports
and finite triangulations are semialgebraic with real parameters.
Choose those triangulations with the orientations above. Computing
a torus integral using angular coordinates is compatible with that
orientation; it does not require a globally semialgebraic angular
parametrization.

### Finite-support reduction, including every complex zero

An ordinary singular chain is a finite linear combination of
continuous maps from compact simplices. Its support is compact.
For any finite collection of chains in X, their union S is compact
and avoids both zero-coordinate axes. Hence there exist numbers
0<epsilon<M<infinity with

\[
 \epsilon<|z_j|<M\quad(z\in S,\ j=1,2).
\]

Let A={z:epsilon<=|z|<=M}, K=A x A and D=Z intersection K.
In particular, if a proposed relation (6) held, the finitely many
representative chains and the chains U in X and V in Z witnessing

\[
 T-\sum_\nu c_\nu B_\nu=\partial U+V                         \tag{7}
\]

would all be contained in such a K. Equation (7) would then hold
in the ordinary chain complex of the compact pair (K,D). The annulus
can depend on the alleged relation. No uniform zero cutoff is assumed.

The entire G is not identically zero, since G(R)>0 by L775 (also
G(1)=xi(1)/8=1/16 by L018). The isolated-zero theorem therefore gives
a finite set A_G={a in A:G(a)=0}. For the named input, use Jiří Lebl,
*Guide to Cultivating Complex Analysis*, v1.10 (5 November 2026),
[Theorem 2.4.7, p.49](https://www.jirka.org/ca/ca.pdf#page=49),
as already imported in L845. An infinite set of zeros in the compact
annulus would have a finite accumulation point in the entire domain.
The set A_G includes all complex zeros in A, with no RH restriction.

It follows exactly, as an equality of sets, that

\[
 D=\bigcup_{a\in A_G}(\{a\}\times A)
   \ \cup\!\bigcup_{a\in A_G}(A\times\{a\})
   \ \cup\{(z,z):z\in A\}.                                   \tag{8}
\]

K and D are compact semialgebraic sets in R^4 with parameters: the
annulus inequalities are polynomial inequalities in real coordinates,
the coordinate constants are allowed real parameters, and the
diagonal is linear. This does not assert that G, its global zero
set, or the global pair (X,Z) is semialgebraic. Multiplicities of zeros
do not change the set (8) or remove any intersection point.

### Branch restrictions and passage to ordinary relative homology

For z=x+iy the angular form is the globally defined smooth real form

\[
 \operatorname{Im}(dz/z)=\frac{x\,dy-y\,dx}{x^2+y^2}.
\]

It uses no global argument function. Since d(dz/z)=0 away from zero,
d eta_j=0 and d beta=0. On a vertical branch {a} x A the restriction
of eta_1 is zero; on a horizontal branch A x {a} the restriction of
eta_2 is zero. On the diagonal the two restrictions are equal, so
their wedge is zero. Thus beta restricts to zero on each smooth
two-dimensional branch of D.

Choose a compatible finite semialgebraic stratification for K and
the branches in (8). Away from intersections its two-dimensional
D strata lie in one of the stated branches. Distinct branches meet
only at isolated points; a vertical, horizontal and diagonal branch
can all meet at (a,a). Annular boundary strata in a branch have
dimension at most one. A 2-form restricts to zero on every such
lower-dimensional stratum as well. Consequently beta vanishes
tangentially on every D stratum, including the triple points. No
simple normal-crossing model has been invoked.

On a neighborhood of K avoiding the axes, beta is smooth and
bounded, with exterior derivative zero. Its restrictions give a
bounded stratified form of the type required by Shartser–Valette:
matching of tangential values follows from continuity of the
ambient form evaluated on converging tangent vectors. The same
observation applies to any further compatible stratification used
for a semialgebraic simplex. In particular singularities of a
simplex parametrization do not require a new smooth-chain theorem;
the cited integration and Stokes results cover continuous
semialgebraic simplices.

Integration therefore gives a real cochain on the semialgebraic
C_2(K): it is zero on C_2(D) by the restrictions just checked and
zero on boundaries from C_3(K) by Stokes and d beta=0. It descends
to semialgebraic relative homology. The cited natural comparison
then defines the same functional on ordinary H_2(K,D;R). In
particular it takes the actual oriented torus and box fundamental
classes to their integrals, since the comparison takes their
semialgebraic triangulations to those same continuous chains. An
abstract, unspecified isomorphism of groups would not suffice here.

These functionals are compatible when the compact annuli are
enlarged: integration on a represented semialgebraic cycle is
unchanged, and comparison is natural for inclusions of pairs.
Every ordinary relative cycle, and every finite chain relation
between two such cycles, is contained in one of these compact
pairs by the finite-support argument. Choosing a common larger
annulus thus makes the values independent of representatives and
cutoffs. This defines the claimed period on ordinary H_2(X,Z;R).
Equivalently, for the proposed relation alone one can apply the
compact-pair functional directly to (7). No integration over an
arbitrary nonsmooth continuous simplex has been silently assumed.

### Exact periods and the contradiction

On T, z_j=R exp(i theta_j) gives eta_j=d theta_j. The orientation
chosen above therefore yields

\[
 \int_T\beta=\frac1{(2\pi)^2}
       \int_0^{2\pi}\int_0^{2\pi}d\theta_1\,d\theta_2=1.
\]

On every box (2),

\[
 \phi^*(dz_j/z_j)=2\,dt_j/t_j,
 \qquad \phi^*\eta_j=0,\qquad \int_B\beta=0.
\]

This holds for both orientations and for any allowed endpoints.
The normalized period of every finite real linear combination of
boxes is exactly zero. Equality with the torus class would force
1=0, contradicting the relative pairing. Applying the coefficient
map from Z to R also excludes an integer relation. This proves
(5)–(6) without computing the entire relative homology group.

### The retained full holomorphic form

The complete form in (3), including both factors 1/i, can also be
written

\[
 \omega=\frac{R^2}{G(R)^2}
       \frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^3z_2^3}
       dz_1\wedge dz_2.                                       \tag{9}
\]

Its coefficient is holomorphic on X, so d omega=0: the antiholomorphic
derivatives vanish and every holomorphic derivative wedges a repeated
dz_j into dz_1 wedge dz_2. On K the form is smooth and bounded, with
bounded exterior derivative zero. In fact its ambient coefficient
vanishes at every point of D, by (8) and (9); hence all tangential
restrictions vanish, also at the singular intersections. Its real
and imaginary parts separately satisfy all the stratified-form and
relative-cochain conditions above. The cited theorem explicitly
allows these nonsemialgebraic coefficients. The same comparison and
finite-support argument therefore define the full omega pairing.

For clarity, its coordinate expressions on the representatives are

\[
 \omega|_T=F_2(Re^{i\theta_1},Re^{i\theta_2})
                 d\theta_1\wedge d\theta_2,
 \qquad
 \phi^*\omega=-\frac{4F_2(-4t_1^2,-4t_2^2)}{t_1t_2}
                 dt_1\wedge dt_2.                            \tag{10}
\]

The negative sign in the box expression is the product of the two
factors 1/i; neither the density nor the Jacobian has been dropped.
These are finite integrals on compact representatives avoiding the
axes. L775's already imported Katkova identity identifies the torus
integral with 2!(2pi)^2 R^2 D_(2,1)/G(R)^2; no new coefficient
identity or positivity input is required here. An equality of
relative classes would imply equality of the integrals in (10),
by the pairing just proved. The beta obstruction shows that this
class equality cannot be supplied by a finite sum of the stated
boxes. It does not compare their omega periods or rule out an
identity obtained for some other reason. ∎

### Independent conceptual audit, 6 November 2026

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-06-finite-box-angular-period-audit.md`
covers this audit. The general comparison and integration theorems
above are reused with their recorded hypotheses, not reproved. The
audit accepts (5)–(6) and the full-form pairing. No mathematical defect
requiring a changed statement was found. The following checks make
explicit why the two potentially delicate passages are valid.

First, (7) is an equality of **ordinary chains**, not merely a relation
between geometric supports. Its finite U and V and the chosen finite
fundamental cycles have compact supports in X. The continuous functions
|z_1| and |z_2| have positive minima on their union; taking epsilon
smaller than both minima and M larger than both maxima places every
simplex and every chain identity in (K,D). The boundary of each box
is in D, while T is an absolute cycle. No transversality to D is needed.
Entirety and nonidentity of G imply that the compact annulus contains
finitely many zeros, including nonreal zeros and zeros on its boundary.
Thus (8) is exact. Multiplicities do not change this pair.

Write j_K for the inclusion-induced comparison from semialgebraic to
ordinary relative H_2(K,D;R). The cited theorem makes j_K an isomorphism.
Let I_K be integration of beta on semialgebraic relative homology.
The ordinary functional is specifically I_K composed with j_K inverse.
For the semialgebraic fundamental chains t and b of T and B, its values
on j_K[t] and j_K[b] are I_K[t] and I_K[b]. This explicitly preserves
the representatives whose integrals are computed; an arbitrary group
isomorphism is not being substituted. The theorem also covers real
coefficients, so no scalar-extension assumption is missing.

For inclusion i:(K,D)->(K',D'), naturality gives
j_K' i_*^sa=i_*^sing j_K, and integration gives
I_K' i_*^sa=I_K. Hence these ordinary functionals agree under i_*^sing.
Every ordinary relative cycle is supported in one compact pair, and
any equality between two such represented classes is witnessed by
finite chains in a common larger pair. These facts prove independence
both of the cutoff and of the representing ordinary cycle. They do
not assume smoothness of arbitrary continuous singular simplices or
global semialgebraicity of Z. The identical argument applies to the
real and imaginary parts of omega. No infinite-chain limit is taken.

For the form hypotheses, in the Euclidean metric |eta_j|<=1/epsilon
on K, hence |beta|<=1/((2pi)^2 epsilon^2), and d beta=0.
The ambient smooth form has the required matching tangential limits
on any compatible refinement. A vertical and horizontal branch meet
only at their fixed-coordinate point; the diagonal meets either only
at (a,a), where all three can meet. Annular boundary pieces have real
dimension at most one. The vertical, horizontal and diagonal
restrictions are respectively zero because eta_1=0, eta_2=0 and
eta_1=eta_2. All lower-dimensional restrictions vanish by degree.
Thus no omitted intersection stratum or normal-crossing assumption
is hidden in the relative cochain. Shartser–Valette Stokes annihilates
boundaries, and the restrictions annihilate chains in D.

The counterclockwise product orientation makes eta_1 wedge eta_2
equal to dtheta_1 wedge dtheta_2 on T, so its normalized period is
exactly 1. The polynomial embedding phi has nonzero derivatives
-8t_j; its stipulated pushforward orientation introduces no extra
sign. Since phi^*(dz_j/z_j)=2dt_j/t_j is real, its beta period is
exactly zero. Reversing a box orientation preserves that zero value.
The comparison and finite-support checks therefore establish the
contradiction for every finite real linear combination. Coefficient
change Z->R suffices for the asserted integer obstruction.

Finally the two factors 1/i multiply to -1 and cancel the minus sign
in F_2 to give precisely (9). Its holomorphic coefficient is smooth
and bounded on a neighborhood of each K, and its exterior derivative
is zero by holomorphy and the repeated dz_j factors. The coefficient
vanishes on all of D. Nonsemialgebraicity of G is allowed for these
forms by the cited source. On the box the same factors instead give
(-2i)^2=-4, verifying (10). As an independent normalization check,
the complete pullback is

\[
 \phi^*\omega=\frac{R^2}{256G(R)^2}
 \frac{\Xi(t_1)\Xi(t_2)(t_1^2-t_2^2)^2}{t_1^5t_2^5}
 \,dt_1\wedge dt_2.
\]

The factors are 1/64 from the two G values, 16 from the squared
difference, 1/256 from z_1^2 z_2^2, and -4/(t_1t_2) from the volume
form, with F_2's initial minus sign. This check does not assume a sign
for Xi(t_1)Xi(t_2). On T the volume form is dtheta_1 wedge dtheta_2;
L775's cited Katkova identity therefore has exactly the factor
2!(2pi)^2 R^2/G(R)^2 stated above.

The direct mathematical inputs remain L018, L775 and L845. The audit
does not import L845's stationary-point or Hessian properties into a
homology assertion, and does not strengthen the finite obstruction to
an inequality of omega integrals or an exclusion of other cycles.

## Mathlib

Full matching coverage and supporting theorem names were not checked.
Availability is unknown, not asserted absent. The proof imports the
precise topological and integration inputs above and supplies their
local application. No formal verification or numerical certificate
is claimed; no mathematical script is needed for the exact periods.
