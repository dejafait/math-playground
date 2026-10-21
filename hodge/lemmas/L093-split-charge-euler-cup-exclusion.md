# L093 — Split-charge Euler exclusion by determinant cup

## Hypotheses

Use L071's marked projective complex K3 surface S, identical fixed
hyperkähler metrics on X=S_1 x S_2, real Kähler class h and
Omega=p_1^*h+p_2^*h. Retain its full integral mixed tensor tau_D,
including the divisor component. Put e_1=eta tensor 1,
e_2=1 tensor eta, P=e_1e_2, with integral_S eta=1. Let

\[
a,b\leq-9,\qquad (a+4)(b+4)\equiv6\pmod{12},\qquad
m=-(a+4),\quad n=-(b+4).
\]

Assume at least one of m,n equals 14r^2 for an integer r. This is
a numerical split charge; the corresponding fibres are permitted
to be stable or split, with no assumption of constant type.
Suppose F is holomorphic locally free of rank two, Omega-slope-polystable,
with integral c_1(F)=0 and

\[
\operatorname{ch}_2(F)=-m e_1-n e_2-\tau_D.
\]

Initial higher characters and K-class are unrestricted subject to
actual rank two. No inverse transform, chosen image, common-kernel
existence or transport is assumed. L090, L091 and L092 are used for
their coefficient, actual-map and full-trivial-part methods, not by
applying their numerical conclusions outside their hypotheses.

## Conclusion

Every hypothetical F satisfying these hypotheses has H^1(X,F)=0 and

\[
\chi(X,F)=\frac{(m-12)(n-12)-18}{6}\geq0.
\tag{1}
\]

Thus no such F exists in the admitted split-charge domain with

\[
\boxed{(m-12)(n-12)<18}.
\tag{2}
\]

Its actual images G=R^1p_{2*}F and H=R^1p_{1*}F have ranks m-4 and
n-4, respectively, are slope-zero polystable at the same h, and carry
perfect symmetric forms. Each has cohomology (0,chi(X,F),0).
In particular equality forces acyclic images, not a contradiction
or their existence. The positive Euler side also receives no
existence assertion. Together with L092, this establishes the same
necessary Euler inequality throughout L071's admitted domain.

This is a NEGATIVE / REPRODUCTION specialization of the assessed
known tools. The changed endpoint application is proved below;
the separate critical audit below preserves the enlarged-domain argument.
It supplies no common F, algebraic cycle, transverse transport or
universal primitive rational Hodge realization, and claims no
certified originality or progress beyond the inspected general sources.

## Proof

**Every-fibre endpoints, including split fibres.** L071 proves that
F is stable on X, supplies its actual compatible hyperholomorphic
unitary connection, and restricts its curvature to every factor
fibre. Thus every restriction is locally free rank-two slope-zero
polystable at h with determinant O and fixed charge c=m or c=n.
This uses actual curvature, not ordinary restriction stability.
Here c>=5 by the hypotheses.

Import K3 Riemann--Roch and Serre duality from Huybrechts,
*Lectures on K3 Surfaces*, author-hosted prepublication,
[Chapter 1 (2.5)--(2.6), Proposition 2.4, pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11),
and real-Kähler slope stability, dual stability and the equal-slope
stable-Hom criterion from
[Chapter 9 Section 3.1(ii)--(iv), pp. 175--176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175).
If a restriction E is stable, a map O->E of equal slope is impossible
because the stable bundles have different ranks. Its stable dual
has the same property. Hence H^0(E)=H^2(E)=0.

If E is nonstable, polystability and determinant triviality give
E=L direct sum L^{-1}. L071's exact-h classification gives
c_1(L)=rk, k^2=-14, h.k=0 and c=14r^2. Since c>=5, r is nonzero;
both L and L^{-1} have nonzero integral first class and are nontrivial.
Import the degree-zero line section criterion used and proved in
R. P. Thomas, *Examples of bundles on Calabi-Yau 3-folds for string
theory compactifications*, Adv. Theor. Math. Phys. **4** (2000),
231--247, [math/9912179v2, 19 April 2001, Lemma 1.5 proof, p. 5](https://arxiv.org/pdf/math/9912179v2#page=5).
Its applicability at our real h is explicit: a nonzero section of
either line has an effective zero divisor Z. If Z is nonzero then
h.Z>0, because h is Kähler, contrary to the line's zero h-degree.
If Z is zero, the nowhere-vanishing section trivializes the line,
contrary to its nonzero c_1. A nonzero section of a line on a smooth
integral surface has a Cartier zero divisor, so there is no additional
isolated-zero case. Both line H^0 groups vanish. As omega_S=O,
Serre duality exchanges H^2(L) with H^0(L^{-1})^vee and vice versa.
Thus the split E also has H^0(E)=H^2(E)=0. No integral-degree
rounding, global choice of the lines or stability of a split fibre
is used. The trivial split O^2, whose charge is zero, is excluded
by the admitted domain.

In either case RR gives chi(E)=4-c and h^1(E)=c-4. These statements
hold separately on every fibre of both projections, including at
points where stability type might change.

**Actual concentration and preservation.** Projective GAGA algebraizes
F. For either projection p, the schemes are Noetherian, p is proper
flat of finite presentation, F[0] is bounded coherent and base-flat
with proper support, and O_X is perfect. Import
[Stacks 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
with perfect O_X and base-flat F[0], and
[36.31.3, 0BDK](https://stacks.math.columbia.edu/tag/0BDK).
The pushforward is perfect and has derived coefficient base change.
All its closed derived fibres are vector spaces of the same rank
c-4 in degree one. The open locus of degree-one bundle concentration
of that rank therefore contains every closed point. Its closed
complement is empty: a nonempty closed subset of a finite-type
complex scheme would contain a closed point. Consequently

\[
Rp_{2*}F=G[-1],\quad\operatorname{rk}G=m-4>0,
\qquad Rp_{1*}F=H[-1],\quad\operatorname{rk}H=n-4>0.
\tag{3}
\]

All other higher images vanish; G,H are locally free with derived
and ordinary base change. Proper GAGA identifies these with the
actual holomorphic images. Constancy of the cohomology dimensions,
not constancy of the stable/split type, supplies this application.

Import Bartocci--Bruzzo--Hernandez Ruiperez, *A hyperkahler Fourier
transform*, Differential Geometry and its Applications **8** (1998),
239--249, Definition 2, Section 3.3, Lemmas 1--2 and
[Theorem 3, pp. 244--246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=6).
For each direction the source is compact K3, the source coefficient
is flat O, the spheres are compatible, and the hermitian kernel
is L071's actual quaternionic instanton F. The endpoints just proved
give every-parameter odd IT. The theorem has no fibre-irreducibility
or constant-type hypothesis and gives compatible quaternionic-instanton
connections on these actual G,H. Apply the invariant surface-curvature
contraction input, Verbitsky, *Hyperholomorphic connections on coherent
sheaves and stability*,
[math/0107182v10, Proposition 3.7/Lemma 3.8, pp. 12--13](https://arxiv.org/pdf/math/0107182v10#page=12),
and the real-Kähler Kobayashi--Hitchin correspondence, Huybrechts,
[Chapter 9 Theorem 4.9, p. 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182).
Their zero-contraction compatible unitary connections make G,H
slope-zero polystable at precisely h, allowing reducibility. The
alternating classes -[G],-[H] do not negate their connections.
No invertibility theorem or irreducibility theorem is imported.

**Both actual section forms.** Integral c_1(F)=0 and H^1(X,O)=0
give det(F)=O by the exponential-sequence Picard injection. Fix one
holomorphic trivialization and its alternating wedge A:F tensor F->O.
Fix nowhere-zero sigma_i in H^0(S_i,omega_{S_i}). For p:X->B and
E=R^1p_*F define its form by the actual cup, A, sigma_i and trace:

\[
Rp_*F\otimes^{\mathbf L}Rp_*F\longrightarrow Rp_*O_X
\longrightarrow Rp_*\omega_p\longrightarrow O_B[-2].
\tag{4}
\]

Import smooth proper dimension-two coherent duality,
[Stacks 48.19(2),(9), 0AU3](https://stacks.math.columbia.edu/tag/0AU3),
[48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT), and
[48.3.6, 0A9Q](https://stacks.math.columbia.edu/tag/0A9Q), restricting
the internal-Hom comparison to our bounded coherent/perfect coefficients.
Here p^!O_B=omega_p[2]. By (3), the degree-two part of (4) defines
Q_E:E tensor E->O_B. Actual base change makes its fibre the perfect
Serre pairing on H^1(X_z,F|_{X_z}).
Coefficient self-duality comes from A and omega_p is trivialized by
sigma_i. This reasoning does not need fibre simplicity: it applies
equally to the stable and split restrictions. Thus Q_E is perfect.
The odd cohomological interchange sign and alternating coefficient
sign cancel, so Q_E is symmetric.

Single-row Leray,
[Stacks 20.13.1/4, 01EZ/01F2](https://stacks.math.columbia.edu/tag/01F2),
gives two actual isomorphisms from the same V=H^1(X,F):

\[
\ell_G:V\simeq H^0(S_2,G),\qquad
\ell_H:V\simeq H^0(S_1,H).
\tag{5}
\]

Put d=dim V. For either polystable image E, the equal-slope
stable-Hom criterion against O shows that each nontrivial stable
summand and its stable dual has no sections. This permits arbitrary
individual first Chern classes. Therefore its full trivial part is
T=O^d, with E=T direct sum W and H^0(W)=H^0(W^vee)=0. Both cross
blocks of Q_E vanish, since Hom(T,W^vee)=Hom(W,T^vee)=0. Perfection
of Q_E makes its T block perfect. Its matrix is constant on connected
projective B. Evaluation identifies H^0(E) with T_z, giving a
nondegenerate symmetric form on H^0(E). This is L091/L092's full
trivial-part argument, now justified for the actual images in (3).

**The same cup comparisons force d=0.** Use L090's audited coefficient
identity, whose proof is independent of its numerical pair: for
B(u,v)=A_*(u cup v), a closed smooth coefficient Dolbeault representative
of u is locally f_1 alpha+f_2 beta in a determinant-one frame. Its
scalar determinant cup is 2alpha wedge beta, with square zero because
alpha,beta are ordinary degree-one scalar forms. This global closed
form represents the coherent cup. The imported coefficient-resolution
input is Demailly, *L2 vanishing theorems for positive line bundles
and adjunction theory*,
[alg-geom/9410022v3, Section 1.A (1.1)--(1.3), pp. 4--5](https://arxiv.org/pdf/alg-geom/9410022v3),
with coefficient Serre pairing Section 4.A (4.3)--(4.4'), pp. 27--28.
Holomorphicity of A gives the resolution product comparison; harmonic
representatives need not multiply. Hence B(u,u)^2=0 for every u.

Cup-defined scalar Künneth,
[Stacks 36.23.1, 0FLN](https://stacks.math.columbia.edu/tag/0FLN),
applies to the projective qcqs factors over C. For nonzero
theta_i in H^2(S_i,O), put x=p_1^*theta_1, y=p_2^*theta_2.
Then H^2(X,O)=Cx direct sum Cy, x^2=y^2=0 and x cup y is a
nonzero generator of H^4(X,O). Write B(u,u)=alpha(u)x+beta(u)y.

The actual-map comparison of L090/L091 and audited L092 uses only
(3), the locally free coefficient, and the same cup/wedge/trace
(4); its hypotheses now hold for both projections. Explicitly, the
section s=ell_E(u):O_B->Rp_*F[1]=E represents u by pullback followed
by the counit. In a closed fibre square (i,j), coefficient base change
is the adjoint of that pulled-back counit,
[Stacks 20.28.3, 08HY](https://stacks.math.columbia.edu/tag/08HY).
Thus s(z) maps to i^*u. Local freeness removes coefficient Tor terms;
the square is Tor independent because p is flat, although j need
not be flat. Cup and the same A commute with pullback,
[20.31.7/8, 0FP6/0H99](https://stacks.math.columbia.edu/tag/0H99).
The general proof in 0H99 is omitted in that source; the coefficient
Dolbeault pullback just used supplies the comparison here.
For these Noetherian proper-flat finite-presentation projections,
dualizing/right-adjoint base change and trace compatibility are
[48.12.4, 0AAB](https://stacks.math.columbia.edu/tag/0AAB) and
[48.7.1, 0B6J](https://stacks.math.columbia.edu/tag/0B6J).
They identify the evaluation of (4) with the fibre Serre trace.
Consequently, on the same u and with the same A,

\[
Q_G(\ell_Gu,\ell_Gu)=c_1\alpha(u),\qquad
Q_H(\ell_Hu,\ell_Hu)=c_2\beta(u),\qquad
c_i=\operatorname{Tr}_{S_i}(\sigma_i\theta_i)\ne0.
\tag{6}
\]

Indeed the two fibre restrictions of (x,y) are (theta_1,0) and
(0,theta_2), respectively. Multiplication by sigma_i and Serre trace
are isomorphisms on the one-dimensional groups, so c_i is nonzero.
The base functions are constant. Neither the comparisons nor the
nonzero constants use stability of the restricted coefficient.

If d>0, pull the two perfect section forms back through (5) to
quadratic polynomials q_G,q_H on V. Polarization over C makes each
nonzero. Choose v with q_G(v) nonzero and w with q_H(w) nonzero.
On v+t w, the first polynomial has nonzero constant coefficient
and the second has nonzero quadratic coefficient. A t outside their
finite root sets makes both values nonzero. This is L092's
arbitrary-positive-dimensional argument; it permits isotropic vectors.
Equation (6) then makes alpha(u)beta(u) nonzero for one u, so
B(u,u)^2=2alpha(u)beta(u)x cup y is nonzero, a contradiction.
Therefore d=0.

**Euler threshold and limitations.** Q_E gives E=E^vee. K3 Serre
duality then gives h^2(E)=h^0(E)=d=0. The proper-pushforward Euler
identity,
[Stacks 33.33.5, 0BEI](https://stacks.math.columbia.edu/tag/0BEI),
and (3) give chi(X,F)=-chi(E)=h^1(E)>=0. L071 supplies the full
character: tau_D^2=156P, ch_3(F)=0 and
ch_4(F)=(mn+78)P/6. With td(X)=1+2(e_1+e_2)+4P this gives

\[
\chi(X,F)=8-2(m+n)+(mn+78)/6
=((m-12)(n-12)-18)/6.
\]

No mixed term or alternating sign has changed. The congruence
mn=6 modulo 12 makes the expression an even integer. This proves
(1)--(2) and the image cohomology assertion. Nonnegative Euler
permits d=0 and h^1(E)=chi(X,F), without proving realization.

The extension is nonempty and not merely an overlap with the earlier
five-, six- or seven-charge slices: m=14,n=15 passes mn=6 modulo 12,
has (m-12)(n-12)=6 and chi=-2, and is excluded. More generally
m=14(6j+1)^2,n=9 for j>=0 has m=2 modulo 12 and mn=6 modulo 12;
its threshold product is -3(m-12)<=-6<18. This is an infinite
admitted split-charge family omitted from L092, not an existence claim.
At the split-charge boundary, L092's complete integer factorization
before its charge exclusions gives precisely (14,21),(21,14) among
the eight possible equality pairs; the other six have no split charge.
These two inputs force acyclic images but are not excluded here.

The new application is exactly the endpoint check for nontrivial
split lines and its consequences for the two actual transforms.
General preservation, concentration, duality and product theorems
are imported, not reproved. The nonsplit stop, individual factor
constructions and topological realizations remain intact. Common
kernels, equality/positive Euler, prescribed mixed action, transport
and universal Hodge realization remain independent unresolved gaps.

**Separate critical audit, 2026-10-12 (step 234).** The exclusion
survives with its stated hypotheses and strict boundary. This is
EXPLORATION / REPRODUCTION: no substantive error, stronger exclusion
or new existence result is obtained. The primary inputs above are
reused from the approved assessment, not independently rediscovered.

For the changed endpoint, L071 supplies actual polystability on every
fibre and the complete rank-two alternatives. In the split alternative,
the positive charge forces r nonzero, so both integral classes +/-rk
are nonzero. Positivity of a real Kähler class on every nonzero
effective curve is sufficient for the line section argument; no
arithmetic property of the degree is needed. A nonzero holomorphic
section of a line on a smooth surface is locally one nonzero divisor.
If it vanishes anywhere its zero scheme is a nonempty effective
Cartier divisor, so isolated zeros cannot evade positivity. If it
vanishes nowhere the line is trivial, also impossible here. Applying
this separately to L and L^{-1}, then Serre duality, removes both
endpoints. In the stable alternative the equal-slope stable-Hom
criterion applies to the bundle and its dual against O. RR therefore
gives the same dimension c-4 on every fibre of fixed charge c.

For each projection all derived fibres at closed points consequently
have exactly one cohomology group, of fixed positive rank in degree
one. Properness, Noetherian hypotheses, local freeness and base
flatness justify the cited perfect-pushforward and base-change input.
Its open fixed-rank concentration locus contains every closed point;
the finite-type closed complement must be empty. No local choice of
split lines or constancy of stability type enters this argument.
Both positive bundles in (3), rather than their alternating negatives,
meet BBHR's hypotheses with flat source O, compact source K3,
compatible spheres and the same actual quaternionic-instanton kernel.
The cited preservation result permits reducible fibre restrictions
and images. Its surface connections have zero contraction and yield
polystability at the unchanged real h in both directions.

The split case does not spoil the relative form. On a split fibre,
the coefficient wedge pairs L with L^{-1}, while each same-line
wedge is zero. Multiplication by the chosen sigma identifies the
opposite coefficient with its Serre dual coefficient. The off-diagonal
pairing between H^1(L) and H^1(L^{-1}) is therefore perfect; the odd
cohomological sign and the alternating coefficient sign make the total
form symmetric. This also follows directly from coefficient Serre
duality without choosing the splitting. On stable fibres the same
duality applies. Base change thus makes (4) perfect at every point.

For each image E, its slope-zero stable decomposition consists of
locally free summands. Every summand other than O, and its stable
dual, has no section by the equal-slope criterion. Thus the full
trivial part is exactly O^d with d=dim H^1(X,F). Both cross blocks
with its complement vanish. Invertibility of Q_E on this block-diagonal
decomposition forces invertibility on O^d; its entries are constant
on the connected projective base. Consequently both section forms,
pulled back to the same V by (5), are nondegenerate. No positivity,
parallelness of the form, or arbitrary selection of a trivial subspace
is substituted for this full-isotypic-part argument.

To verify that these are the forms required by the coefficient cup,
put P=Rp_*F=E[-1]. A class u corresponds to s:O_B->P[1]=E;
its adjoint is O_X->Lp^*P[1]->F[1], with the second arrow the
counit. In a closed-fibre square (i,j), the coefficient base-change
map is adjoint to the pulled-back counit. It sends j^*s=s(z) to
exactly i^*u. The coefficient bundles are locally free and the square
is Tor independent because p is flat, even though j need not be.
The cited proper-flat dualizing and trace base change applies to
these bounded coherent/perfect objects and to p^!O=omega_p[2].
Hence evaluation of (4) is
Tr_(S_i)(sigma_i A_*((i^*u) cup (i^*u))). Coefficient Dolbeault
pullback verifies cup compatibility in this specialization, without
claiming the omitted general proof in Stacks 0H99. The restrictions
of (x,y) are respectively (theta_1,0) and (0,theta_2). Multiplication
by sigma_i and the Serre trace are isomorphisms on the relevant
one-dimensional spaces, giving precisely the nonzero constants in
(6). This uses one u and one determinant wedge in both directions.

In a determinant-one local frame the same closed representative has
scalar cup 2alpha wedge beta. Ordinary scalar one-forms square to
zero, so its scalar exterior square vanishes before cohomology.
Frame invariance and holomorphicity of A make the scalar form global
and closed. The coherent cup comparison therefore gives B(u,u)^2=0.
If d>0, polarization makes each perfect symmetric form a nonzero
quadratic polynomial. In the proof's line v+t w, one polynomial has
nonzero constant term and the other nonzero quadratic term, even
if v,w are dependent. Avoiding the two finite root sets produces
one u with both coefficients in (6) nonzero. Künneth gives x cup y
nonzero and the even degrees give the factor 2. This contradicts
square-zero and proves d=0 in every possible image rank.

Finally the full lower character squares to (2mn+156)P; rank two
with integral c_1=0 forces ch_3=0 and ch_4=(mn+78)P/6. The Todd
product gives 8-2m-2n+(mn+78)/6, exactly (1). Writing mn=6+12j
makes this 22-2m-2n+2j, an even integer. Concentration gives
chi(X,F)=-chi(E), not +chi(E). Self-duality and surface Serre
duality give h^2(E)=h^0(E)=0, so chi(X,F)=h^1(E)>=0.
Thus precisely the strict negative-Euler region is excluded by this
test; no additional claim on the nonnegative side follows.

For the complete equality check put u_0=m-12,v_0=n-12, both at
least -7. The positive ordered factor pairs of 18 are
(1,18),(2,9),(3,6) and their reversals. The only negative ordered
factor pairs within these lower bounds are (-6,-3),(-3,-6).
Adding twelve gives (13,30),(14,21),(15,18) and their reversals,
plus (6,9),(9,6). Every pair passes mn=6 modulo 12. All charges
are below 56, so the only possible positive split charge is 14;
this leaves precisely (14,21),(21,14) in the present domain.
Their images are only forced acyclic. The strict examples also
check directly: (14,15) has threshold product 6 and chi=-2;
m=14(6j+1)^2,n=9 has m=2 modulo 12 and threshold product
-3(m-12)<18 for every j>=0. These verify the recorded examples,
not a fresh exclusion beyond L093. The nonsplit stop, individual
constructions, topological realizations and all independent unresolved
gaps remain as qualified above.

## Mathlib

Full matching coverage of this split-charge exclusion and supporting
geometric coefficient/base-change/preservation results: **not checked**.
Unknown coverage is not absence. Precise primary inputs and their
qualifications are given above. No mathematical script or numerical
preview is used as proof. The separate critical audit above preserves
the enlarged-domain result and its qualifications.
