# L118 — Opposite charge-twenty-one placement and local total geodesy

## Hypotheses

Use L071's identical marked smooth projective complex K3 surfaces
X=S_1 x S_2, common hyperkähler metric g, ordered structures I,J,K,
real ample divisor class h and Omega=p_1^*h+p_2^*h. Set
e_1=eta tensor 1 and e_2=1 tensor eta, with integral_S eta=1.
Retain its full integral mixed tensor tau_D, with cup-product operator
D=D^*, D[sigma]=2lambda[sigma], sigma=omega_J+i omega_K and
1<lambda<5/4. Here omega_L(u,v)=g(Lu,v).

Suppose F is holomorphic locally free of rank two, Omega-slope-polystable,
with integral c_1(F)=0 and

\[
             \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Use its actual compatible unitary hyperholomorphic connection supplied by
L071. In this lemma B=S_1 is the base and Y=S_2 is the fibre; put
E_x=F|_{\{x\}\times Y}. No split point, F existence, global separation,
embedding, compact ambient metric, image deformation or transport is assumed.

## Conclusion

Every E_x is h-slope-stable. There exists one very ample integral line
bundle H on Y that preserves h-slope stability and semistability uniformly
for all torsion-free sheaves of rank two, c_1=0 and c_2=21 eta.
The actual family defines an algebraic morphism

\[
 f^-:B\longrightarrow M_H^s(2,0,-19),\qquad x\longmapsto[E_x],
 \qquad P_H(n)=H^2n^2-17.                              \tag{1}
\]

Here M_H^s is the fixed-numerical-class stable part of the Gieseker
moduli scheme. Near every f^-(x), its locally free H-slope-stable
germ is naturally identified with the fixed-h irreducible connection
germ, carrying the actual family to x -> [A_x]. For real skew-adjoint
ASD-harmonic one-forms normalize the latter's metric by

\[
 G_A(a,b)=-\frac1{4\pi^2}\int_Y
            \sum_{j=0}^3\operatorname{Tr}(a(t_j)b(t_j))\,dVol_g,
                                                               \tag{2}
\]

where t_j is any orthonormal fibre frame. In these natural charts,

\[
 df^-\circ L_B=L_M\circ df^-\quad(L=I,J,K),\qquad
                    (f^-)^*G=2\lambda g.                \tag{3}
\]

Thus f^- is everywhere a local quaternionic immersion, and each local
embedded branch is totally geodesic. For the parametrized map this means

\[
 \nabla^{(f^-)^*TM}_u(df^-(v))=df^-(\nabla^g_u v).        \tag{4}
\]

The conclusion is conditional and is a REPRODUCTION/specialization of
the inspected general tools. The separate critical audit below preserves it. Local
branches can coincide or intersect; no global separation, normality,
embedding, common kernel, extra normal section, compactification, image
deformation, new algebraic Hodge class or transport is established.

## Proof

**Scope and imported tools.** The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-17-opposite-charge-twenty-one-local-comparison.md`.
Its covered target is this application. L100's audited proof is a
methodological comparison; neither its charge-fourteen H nor its forward
map or geodesy conclusion is used as a theorem for the opposite family.
L093 supplies the equality context, not an identification of a direct
image bundle with this classifying family. The mathematical inputs below
are L071's connection/factor classification and L095's audited coefficient
and raw-pairing identities, with their opposite specialization checked.
The general wall, moduli and embedding results are imported, not reproved.

**All opposite fibres are stable.** L071 first proves stability of F
on the product and then obtains its compatible connection; pulling back
the actual invariant curvature gives a zero-contraction unitary
connection on every factor fibre. Consequently each E_x is locally free
and h-slope-polystable, with integral c_1=0 and c_2=21 eta. This is a
curvature restriction argument, not ordinary restriction stability.
L071's exact lattice NS(Y) intersect h-perp=Z k, k^2=-14 shows that a
nonstable such rank-two polystable bundle must be L direct sum L^{-1}
of charge 14r^2. Since 21=14r^2 would give r^2=3/2, no integer r
works. Every E_x is therefore stable, at every complex parameter.

**One new uniform polarization.** Import Greb--Toma, *Compact moduli
spaces for slope-semistable sheaves*, Algebraic Geometry **4** (2017),
40--78, doi:10.14231/AG-2017-003,
[Theorem 6.6 and full proof, p. 74; Section 6.3.3, p. 75](https://content.algebraicgeometry.nl/2017-1/2017-1-003.pdf#page=35).
For fixed topological invariants and a compact set in
P(Y)={A^(dim Y-1): A real ample}, finitely many rational linear walls
give uniform slope stability and semistability for all torsion-free
sheaves with those invariants in each connected relative stratum,
including smaller-dimensional strata. On the surface Y, P(Y) is
identified with the real ample cone by the intersection pairing.
The surface invariants here are (rank,c_1,c_2)=(2,0,21 eta).

Choose a compact convex neighborhood K of h inside that cone, with
h in its interior, and apply the theorem with these invariants.
Write its finitely many rational wall functionals as ell_i. Set
I_0={i:ell_i(h)=0} and W=intersection_{i in I_0} ker ell_i.
This is a rational linear subspace containing h. Its rational points
are dense: row reduction of its rational defining matrix gives a
rational basis. For all remaining walls the value at h is nonzero.
In a small relative neighborhood of h in W inside the interior of K,
their strict signs are unchanged. Choose a rational ample alpha there.
The segment from h to alpha stays in K and on the walls I_0 and
crosses none of the other walls. Thus both lie in the same connected
relative stratum. The theorem preserves both slope conditions for
every torsion-free sheaf with the specified invariants, not merely
the original fibres E_x.

Clear denominators to obtain an ample integral line class H_0 and
take a very ample positive power H, using Hartshorne, *Algebraic
Geometry*, Chapter II, Theorem 7.6. Positive scaling multiplies all
surface slopes by the same positive scalar, so h/H stability and
semistability remain equivalent over this entire fixed-invariant class.
No charge-fourteen wall system, full-dimensional chamber, numerical
wall enumeration, H.k=0 or v-genericity is assumed.

**Actual algebraic placement.** Serre, *Géométrie algébrique et
géométrie analytique*, Ann. Inst. Fourier **6** (1956),
[Sections 9, 11--13, Proposition 10 and Theorem 1, pp. 16--22](https://www.numdam.org/item/AIF_1956__6__1_0/),
algebraizes the vector bundle on the projective product and preserves
its actual restrictions and exact sequences. Since p_1 is flat and F
is locally free, it is flat over B. Each E_x is pure of dimension two,
and its H-slope stability implies H-Gieseker stability by
Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves*, E31
(1997), [Lemma 1.2.13, p. 14](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=26).
With td(Y)=1+2 eta, surface HRR gives

\[
 \begin{aligned}
 \operatorname{ch}(E_x)&=2-21\eta,\\
 \chi(E_x\otimes H^n)
   &=\int_Y(2-21\eta)e^{nH}(1+2\eta)=H^2n^2-17,\\
 v(E_x)&=(2-21\eta)(1+\eta)=(2,0,-19).
 \end{aligned}                                               \tag{5}
\]

Use smooth proper HRR, [Stacks Tag 02UO](https://stacks.math.columbia.edu/tag/02UO).
For any class A in K_0(Y), the same formula with ch(A) shows that
all Euler pairings are independent of x. Thus the numerical K-class
is fixed as well as the Hilbert polynomial. This does not identify the
entire fixed-polynomial scheme with a single numerical-class part.

Huybrechts--Lehn [Corollary 1.5.11, p. 24](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=36)
makes these stable complex fibres geometrically stable; their
[Proposition 2.3.1 and proof, p. 45](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=57)
give openness of geometric stability in the actual flat polarized
family. Its locus contains every closed point of B, so its closed
complement is empty: any nonempty closed subset of a finite-type
C-scheme has a closed point. All geometric fibres, including those
over nonclosed scheme points, are therefore stable. The flat-family
moduli functor in [Section 4.1, p. 80](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=92)
and its corepresentation in [Theorem 4.3.4, p. 91](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=103)
now give (1). The fixed numerical part is open and closed as in
Section 8.1 before Definition 8.1.4, p. 180. No universal sheaf or
extension of a punctured map is required.

**Actual opposite harmonic derivative and orientation.** For a real
u in T_xB define a fibre one-form by
r^-_u(t)=R((u,0),(0,t)). A smooth local unitary trivialization over
B gives a family A_x of vertical connections and a horizontal
coefficient H_u. The actual identity is

\[
 r^-_u=\dot A_u-d_{A_x}H_u,\qquad
 d_{A_x}r^-_u=\dot R_Y+[H_u,R_Y].                       \tag{6}
\]

L095's audited coefficient proof applies with these base/fibre labels:
the fixed fibre star makes the right side ASD, and curvature invariance
gives r^-_{Lu}=L_c r^-_u, where (L_c a)(t)=-a(Lt). Applying the
linearized ASD equation to Iu and the coefficient contraction
C_I(I_c a)=C_0(a) gives d_{A_x}^*r^-_u=0. Thus r^-_u is already
ASD-harmonic, and its (0,1) part is Dolbeault-harmonic. This use of
L095 needs no split point; its split-point hypothesis was used only
for its additional reducible-slice identification. Both coefficient
arguments use an arbitrary fibre and the fixed product connection.
The determinant is holomorphically trivial, since integral c_1=0
and Pic^0(X)=0; its zero-constant HE connection has zero curvature
by the compact-product harmonic-log-metric argument of L095. Hence
r^-_u is trace-free as an actual form.

For clarity about exchange, identify the swapped product by
iota:Y x B -> B x Y, (y,x) -> (x,y). Its mixed tensor is
tau_{D^*}=tau_D: exchanging degree-two classes has sign
(-1)^(2 times 2)=+1, and D is self-adjoint on the full cup space,
including the divisor component. The pure coefficients interchange,
giving ch_2(iota^*F)=-21 e'_1-14 e'_2-tau_D. The mixed curvature
with base written first still means R(u,t); antisymmetry gives
R(t,u)=-R(u,t), not an alteration of the ordered quaternionic triple.
We compute the pairing with the base-first convention in (6).

Apply L095's raw exterior identity to this orientation. Put
G_x(r^-_u,r^-_v)=c(x)g(u,v). This follows because G is positive,
symmetric and quaternionic-invariant on the quaternionic-line base.
Writing curvature as R_B+R_m+R_Y, the two mixed products contribute
-2 Tr(r^-_u wedge r^-_v); the two pure cross products vanish after
wedging with each fibre omega_L because R_Y wedge omega_L=0
coefficientwise. Chern--Weil's factor 1/(2(2pi i)^2) and the same
ordered frame identity as in L095 therefore give

\[
 \gamma^-:=p_{1*}\left(
   \frac{\operatorname{Tr}(R\wedge R)}{2(2\pi i)^2}
                     \wedge p_2^*\sigma\right)
                     =-c(x)\sigma_B.                         \tag{7}
\]

Swapping two real four-dimensional factors preserves orientation;
the complex fibre orientation here is unchanged. On cohomology
p_{1*}(tau_D p_2^*[sigma])=D^*[sigma]=2lambda[sigma].
Neither pure point term survives: its fibre degree after wedging
with sigma is either two or six. Thus [gamma^-]=-2lambda[sigma_B].
The actual integral in (7) is closed and of pure type (2,0), since
the integrand is closed of type (4,2). It is a holomorphic two-form
on compact Kähler B, whose map to de Rham cohomology is injective.
Consequently (7) is the actual identity
-c(x)sigma_B=-2lambda sigma_B. The nowhere-zero sigma_B forces
c(x)=2lambda everywhere. This checks the opposite scale by the
full tensor, rather than assigning a sign to a Yoneda form.

**Natural coarse/connection germ comparison.** Import Verbitsky,
*Hyperholomorphic bundles over a hyperkahler manifold*,
[alg-geom/9307008v1 (29 July 1993), Definition 6.3, Theorems 6.1--6.4,
Section 7 through Corollary 7.1, Section 9/Proposition 9.1 and
Corollary 10.1, PDF pp. 22--28, 34--37](https://arxiv.org/pdf/alg-geom/9307008v1#page=22).
These supply natural local classifying families and KS maps for
stable hyperholomorphic bundles, smooth surface connection germs,
the harmonic L2 hyperkähler metric, and rotations through the same
connections. The inspected surface smoothness qualification is used,
not a general assertion that every moduli reduction is smooth.

At any x, stability of E_x makes A_x irreducible: a parallel proper
orthogonal summand would be a holomorphic zero-slope summand at I.
At any induced structure L the same restricted connection remains
invariant, irreducible and zero-contraction, hence defines a stable
bundle for the rotated metric. Simultaneous rotation of the product
connection gives the actual local families through these same classes.
No projectivity of a rotated surface is needed for this local input.

At E=E_x, simplicity gives Hom(E,E)=C. Serre duality gives
Ext^2(E,E)=C, but the trace map to H^2(O_Y) is an isomorphism:
its dual sends 1 to id_E and is an isomorphism. Thus Ext^2(E,E)_0=0.
Since H^1(O_Y)=0, fixing determinant removes no tangent directions.
Huybrechts--Lehn [4.5.1--4.5.4, pp. 101--102](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=113)
give a smooth algebraic coarse germ with natural Ext^1 tangent and
an actual étale slice family Q through E. For consistency,
v(E)^2=76, so the smooth complex dimension is 78; no dimension-four
or isotropic-vector hypothesis enters the connection theorem.

Shrink the slice so that Q is locally free and H-slope-stable,
using local-freeness openness and
[Huybrechts--Lehn 3.A.1 and slope openness, p. 74](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=86).
Its fibres retain rank two, c_1=0 and c_2=21 eta. The uniform
fixed-invariant h/H equivalence proved above therefore makes this
entire slice neighborhood h-stable. Stability of the original E_x
alone would not have justified this neighborhood.

Choose a small analytic slice neighborhood mapping biholomorphically
to an open coarse neighborhood V. Its actual analytified family
Q^an has a holomorphic classifying map to the I-connection germ.
The natural slice tangent theorem and exact GAGA identify its
dual-number deformation with the same extension
0 -> E -> E_epsilon -> E -> 0. The named Dolbeault theorem for
the holomorphic bundle End(E) carries that extension to its actual
KS class. Therefore the derivative of this map is the natural
Ext^1 isomorphism, not an arbitrary vector-space identification.
Both germs are smooth, and the holomorphic inverse function theorem
gives a biholomorphism after shrinking. For nearby z the slice fibre
representing f^-(z) is E_z itself; HE uniqueness assigns it precisely
[A_z]. Thus this comparison carries the actual algebraic f^- to
the actual connection map phi^-(z)=[A_z]. Pointwise equality here
is equality of holomorphic maps on the reduced smooth source.
No relative algebraization of arbitrary analytic families is used.

For the natural differential one may also check the representative
directly, using Biswas--Schumacher, *Geometry of moduli spaces of
Higgs bundles*, [math/0605589v1, Section 3, Lemma 3.3/equation (12),
p. 7](https://arxiv.org/pdf/math/0605589v1#page=7).
The actual family variation dot A_u differs from r^-_u by the gauge
term d_A H_u in (6); its harmonic tangent is therefore r^-_u.
If two harmonic representatives differ by d_A s, integration by
parts gives their difference norm squared zero. For
v=(u-iIu)/2 and a fibre (0,1) vector bar t, curvature invariance
gives R(Iu,bar t)=iR(u,bar t), so R(v,bar t)=R(u,bar t).
Hence the complex tangent is exactly (r^-_u)^{0,1}, with no factor
or conjugation. Skew-adjoint reality recovers the full real form.

**Positive metric normalization and local geodesy.** Verbitsky's
Section 9 harmonic metric has real skew-adjoint expression equal
to a fixed positive multiple of the negative-unitary-trace L2 norm.
In the explicit local convention of Yang Li,
*Mukai duality on K3 surfaces from the differential geometric
perspective*, [1908.05017v1, Section 2.2, Theorem 2.10/equations
(1)--(2), pp. 5--6, and Lemma 2.12/equation (4), p. 7](https://arxiv.org/pdf/1908.05017v1#page=5),
write b=a^{0,1}, a=b-b^*. The two types have equal norm and are
orthogonal, giving integral -Tr(a wedge *a)=2 integral |b|^2 dVol.
Thus (2) is one fixed positive normalization of that hyperkähler
metric, independent of connection and parameter. A scalar change
of a stable fibre's HE metric cancels in its End metric; unitary
gauge changes preserve trace. These conventions consequently agree
on chart overlaps, including around isomorphic fibres. Li's global
isotropic-duality conclusions and printed global period sign are
not used.

Equation (6) identifies dphi^-(u)=r^-_u, and its quaternionic formula
and (7) give exactly (3). The scale satisfies 2<2lambda<5/2,
strictly exceeding the required threshold zero. Hence the differential
is injective everywhere. The holomorphic constant-rank theorem
allows shrinking about any x to a local embedded branch. Give its
source the metric 2lambda g with its original I,J,K.

Import Verbitsky, *Deformations of trianalytic subvarieties of
hyperkahler manifolds*, [alg-geom/9610010v1 (9 October 1996),
Propositions 5.1--5.2, Definition 5.3/Corollary 5.4 and Appendix 5.3,
PDF pp. 29--31](https://arxiv.org/pdf/alg-geom/9610010v1#page=29).
The local branch now preserves both metric and quaternionic structures,
the hypotheses of the hyperkähler embedding corollary. Its tangent,
normal and pulled-back ambient connections are in the all-induced-
hyperholomorphic scope of Propositions 5.1--5.2; the zero middle
curvature contraction used in the appendix is retained. The broader
printed Proposition 5.5 alone is not invoked. The result makes the
second fundamental form zero. Neither completeness nor compactness
of the target is a hypothesis of this local application.

The induced tangential connection is that of 2lambda g. In the
Koszul formula this constant multiplies every metric term and cancels,
so that connection is precisely nabla^g. This proves (4) for each
local branch and hence the parametrized map everywhere on B.
It supplies no identification of different branches. All continuation
thresholds of this bounded local application are met; independent
kernel existence, global separation, image deformation, compact metric
extension, transverse transport and universal primitive Hodge realization
remain unresolved. No numerical certificate or script is needed.

**Separate critical audit, 2026-10-17 (step 346).** The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-17-opposite-charge-twenty-one-critical-audit.md`.
This audit finds no substantive error, stronger obstruction or existence
conclusion. Its outcome is EXPLORATION / RESEARCH / REPRODUCTION,
with actual task type proof_audit. It verifies this conditional application
of the cited tools; it is not a new mathematical discovery. The direct
mathematical inputs remain L071 and L095.

First check the changed projection without assuming the desired fibre
stability. Restriction of L071's actual invariant connection is HE of
constant zero on each Y fibre. A strictly polystable rank-two restriction
with trivial determinant is a sum of two inverse lines of zero h-slope.
Their integral classes are rk and -rk, so their charge is 14r^2. Charge
21 would require the impossible integral equation 2r^2=3. This argument
works at every parameter and does not require a split fibre in the other
projection. It also does not assert ordinary restriction stability.

The uniform-polarization quantifier is essential. Theorem 6.6 and its
proof, and Section 6.3.3 of Greb--Toma, at the precise citation above,
were checked again: the walls depend on the fixed invariants and the
compact polarization region, not on a selected family. For the surface
the power map is the identity. The common kernel W of walls through h
is rational, and a small convex neighborhood in W retains the signs of
all remaining walls. A rational point there and positive integral
scaling retain all zero and strict slope conditions for this entire
class of sheaves. In particular they apply to every member of the
shrunk, locally free H-slope-stable slice. An auxiliary H from charge
fourteen would not justify this step. No application of Proposition
6.7 in a dimension outside its printed scope is needed.

Independently, surface HRR gives rank two, Euler characteristic -17,
polynomial H^2 n^2-17 and Mukai vector (2,0,-19). The product bundle
is base-flat. Geometric stability is open and contains all closed
points; a nonempty closed complement on B would contain a closed point.
Thus corepresentation applies to the whole family, including its
geometric fibres over nonclosed points. Fixed Euler pairings with K_0(Y)
give the numerical-class part. These checks supply the actual algebraic
map without any global universal sheaf.

For the natural germ, the trace-dual map H^0(O_Y) -> Hom(E,E)
sends 1 to id_E and is an isomorphism by stability. Consequently the
trace-free Ext^2 is zero, while full Ext^2 has dimension one. With
H^1(O_Y)=0 there is no additional determinant tangent to remove.
The cited actual etale slice and stable connection germ are therefore
smooth of complex dimension 78. The analytified slice family carries
the same dual-number short exact sequence through exact GAGA; the
Dolbeault resolution computes that sequence's same extension class.
The natural connection-moduli classifying map hence has invertible
derivative. This is the map to which the inverse function theorem
applies, rather than an abstract identification of tangent spaces.
The h-stability of the entire slice was established above. HE uniqueness
then identifies the slice class of E_z with the actual restricted
connection A_z, and gives the asserted comparison for the family itself.

The harmonic check can be made before this quotient. In a smooth unitary
trivialization, r_u=dot A_u-d_A H_u and d_A^2 H_u=[R_Y,H_u], whence

\[
 d_A r_u=\dot R_{Y,u}+[H_u,R_Y].
\]

The fixed fibre star and R_Y^+=0 imply d_A^+r_u=0. Quaternionic
invariance gives r_{Iu}=-r_u composed with I. Since
sum_j(nabla_{t_j}(I_c r_u))(It_j)=sum_j(nabla_{t_j}r_u)(t_j),
the ASD equation for r_{Iu} gives d_A^*r_u=0. These are L095's
coefficient identities on an arbitrary fibre; its extra reducible-slice
identification is unused. Trace-flatness follows from the zero-constant
HE metric on the holomorphically trivial determinant over compact X.
The actual harmonic derivative is r_u, since the discarded horizontal
term is d_A-exact. For v=(u-iIu)/2 and a (0,1) fibre vector bar t,
R(Iu,bar t)=iR(u,bar t) gives R(v,bar t)=R(u,bar t). Thus the
natural complex tangent is r_u^{0,1}, without a factor two or conjugation.

For an independent sign check take an oriented fibre frame with
omega_I=theta_0 wedge theta_1+theta_2 wedge theta_3. Direct expansion
for arbitrary coefficient one-forms a,b gives

\[
 -\operatorname{Tr}(a\wedge b)\wedge\omega_I
 =-\operatorname{Tr}(-a_1b_0+a_0b_1-a_3b_2+a_2b_3)\,dVol.
\]

This is exactly the pointwise negative-trace pairing of I_c a with b.
The same identity holds for J,K in the ordered quaternionic frame.
In the curvature square only R_B R_Y, R_Y R_B and R_m^2 have the
required fibre degree before wedging with omega_L. The first two vanish
by the coefficientwise ASD identity R_Y wedge omega_L=0, even when
R_B is noncentral and depends on the fibre. The two ordered mixed
products give -2 Tr(r_u wedge r_v). Division by 2(2pi i)^2 gives
the coefficient +1/(4pi^2), so the resulting integral is
-G(L_c r_u,r_v). There is no missing Chern--Weil factorial.

The positive symmetric raw pairing is quaternionic-invariant, hence
c(x)g on the four-real-dimensional base. Integration over the second
factor contracts tau_D to D^*sigma, not D sigma by convention. The
full operator is self-adjoint, so this is 2lambda sigma; even-degree
exchange and the swap of two real four-dimensional orientations both
have sign +1. The pure terms have fibre degrees two and six and vanish.
The resulting actual closed (2,0) form has class -2lambda[sigma_B].
Its comparison with -c(x)sigma_B is legitimate on compact Kähler B:
holomorphic two-forms inject into de Rham cohomology. Therefore
c(x)=2lambda everywhere, with actual/required bounds (2,5/2) versus
c>0. No signed Yoneda form is being assigned positivity.

Finally, the real harmonic norm in (2) is a single positive normalization
of the cited local hyperkähler L2 metric. For b=a^{0,1}, skew-adjoint
reality gives a=b-b^*, and the two orthogonal types have equal norms.
Thus the real squared norm is twice the Dolbeault squared norm in this
convention. Scalar choices of HE metric cancel in End(E), and gauge
changes preserve trace, so the normalization is consistent on overlaps.
Quaternionic equivariance and the strictly positive scale now give a
local embedding preserving both structures after scaling the source
metric to 2lambda g. The hypotheses and complete proof of Verbitsky's
Propositions 5.1--5.2 and Corollary 5.4 at the citation above were
checked again. All three induced connections are hyperholomorphic;
in particular the middle curvature has zero Kähler contraction, as
required in the appendix. Its pointwise second-fundamental-form argument
applies to these local branches without compactness. The induced source
connection is the Levi-Civita connection of 2lambda g, equal to that of
g because the scale is constant. This verifies (4) for the original
source connection, including overlap compatibility.

No failed bridge requires repair or narrowing. Local branches may still
meet, and none of the above supplies an embedding of the whole source,
normality of the image, a compact ambient metric or an image deformation.
Common F existence, transverse transport and universal primitive Hodge
realization remain unresolved. The compact-Douady, boundary-class and
uncontrolled scalar-cup stops remain unchanged. This completed audit
neither reopens those inferences nor asserts a complete candidate.

## Mathlib

Full matching coverage for this opposite-family uniform placement,
natural germ comparison, harmonic normalization and local geodesy:
**not checked**. Unknown availability is not absence. The precise
primary citations above supply the general inputs. The conditional
application is a REPRODUCTION of these tools, with no originality
or beyond-source claim. The separate critical audit above preserves
the conditional result and its stated limitations.
