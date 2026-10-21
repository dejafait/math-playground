# L092 — Uniform stable-fibre Euler exclusion by determinant cup

## Hypotheses

Use L071's marked projective complex K3 surface S, identical fixed
hyperkähler metrics on X=S_1 x S_2, real Kähler class h and product
class Omega=p_1^*h+p_2^*h. Retain its full integral mixed tensor
tau_D, including its divisor component. Write e_1=eta tensor 1,
e_2=1 tensor eta, with integral_S eta=1. Let a,b be integers with

\[
a,b\leq-9,\qquad (a+4)(b+4)\equiv6\pmod{12}.
\]

Put m=-(a+4), n=-(b+4), and assume neither m nor n equals
14r^2 for any integer r. Suppose F is holomorphic locally free of
rank two, Omega-slope-polystable, with integral c_1(F)=0 and

\[
\operatorname{ch}_2(F)=(a+4)e_1+(b+4)e_2-\tau_D.
\]

Initial higher characters and K-class are unrestricted subject to
actual rank two. F and both images below are hypothetical; no image
identification, inverse transform, lifted projector or transport is
assumed. L090 and L091 are used for their audited coefficient identity
and actual-map/trivial-part methods, not their exact-pair conclusions.

## Conclusion

Every such hypothetical F satisfies H^1(X,F)=0 and

\[
\chi(X,F)=\frac{(m-12)(n-12)-18}{6}\geq0.
\tag{1}
\]

Consequently no such F exists in the precise strict region

\[
\boxed{(m-12)(n-12)<18},
\quad\text{equivalently}\quad (a+16)(b+16)<18,
\tag{2}
\]

intersected with the stated admitted and nonsplit-charge domain.
The two actual images have ranks m-4 and n-4, are slope-zero
polystable at h, and have perfect symmetric forms. Their cohomology
is (0,chi(X,F),0). Equality in (1) forces both images acyclic;
it does not give a contradiction or a kernel. Positive Euler values
and the omitted split-factor charges are not excluded by this result.

This is a NEGATIVE / REPRODUCTION specialization of assessed known
tools, preserved by the separate critical audit below. It removes common-kernel
data beyond the two earlier exact pairs without claiming progress
beyond the sources checked in general theory or certified originality.
It constructs no bundle or cycle, supplies no transverse transport,
and leaves universal primitive rational Hodge realization open.

## Proof

**Both all-fibre concentrations and actual images.** L071 first
proves that hypothetical F is stable on X and supplies its compatible
unitary hyperholomorphic connection, using the invariant full Chern
classes. Its curvature restriction gives slope-polystability at h
on every factor fibre, with determinant-zero rank-two charges m and n.
Its exact-h split test says a nonstable such fibre has charge 14r^2.
Our exclusions therefore make every fibre stable, in both directions.
This is not ordinary restriction stability or a generic-fibre assertion.

Import K3 Riemann--Roch, Serre duality and dual stability from
Huybrechts, *Lectures on K3 Surfaces*, author-hosted prepublication,
Chapter 1 (2.5)--(2.6), Proposition 2.4,
[pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11),
and the equal-slope stable-Hom criterion, Chapter 9 Section 3.1(ii)--(iv),
[pp. 175--176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175).
A stable rank-two slope-zero fibre has no map from O, and its stable
dual also has none. With omega_S=O, this removes H^0 and H^2.
RR gives h^1=m-4 on every p_2 fibre and n-4 on every p_1 fibre.
Both ranks are positive since m,n>=5.

For each projection p, projective GAGA algebraizes F. The morphism
is proper flat of finite presentation between Noetherian schemes;
O_X is perfect and F[0] is bounded coherent, base-flat, with proper
support. Import [Stacks 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
and [36.31.3, 0BDK](https://stacks.math.columbia.edu/tag/0BDK).
The pushforward is perfect with derived base change. Its open
degree-one bundle locus contains all closed points by the fibre
calculation. A nonempty closed complement in the finite-type complex
base would have a closed point, so the complement is empty. Thus

\[
G=R^1p_{2*}F,\quad Rp_{2*}F=G[-1],\quad\operatorname{rk}G=m-4,
\qquad
H=R^1p_{1*}F,\quad Rp_{1*}F=H[-1],\quad\operatorname{rk}H=n-4.
\tag{3}
\]

All other higher images vanish. These are actual locally free bundles
with ordinary as well as derived base change, since the coefficient
and image bundles are locally free. Proper GAGA identifies their
holomorphic higher images with these algebraic ones.

For both directions import Bartocci--Bruzzo--Hernandez Ruiperez,
*A hyperkahler Fourier transform*, Differential Geometry and its
Applications **8** (1998), 239--249, Sections 3.1--3.3, Definition 2,
Lemmas 1--2 and [Theorem 3, pp. 243--246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=5).
The source is the compact K3 factor, the source coefficient is its flat
O, the spheres are compatible, and the actual hermitian kernel is
L071's quaternionic instanton F. Every-parameter odd IT was just
proved. The preservation theorem identifies each actual higher image
in (3) with a compatible quaternionic instanton; it has no restriction
to the earlier image ranks or correction pairs. Its invariant surface
curvature has zero h-contraction by Verbitsky, *Hyperholomorphic
connections on coherent sheaves and stability*, math/0107182v10,
Proposition 3.7/Lemma 3.8,
[pp. 12--13](https://arxiv.org/pdf/math/0107182v10#page=12).
The real-Kähler Kobayashi--Hitchin correspondence, Huybrechts Chapter 9,
[Theorem 4.9, p. 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182),
makes G and H slope-zero polystable at precisely h. Reducibility is
allowed. The alternating classes -[G] and -[H] do not negate these
positive bundles or their connections. This applies the inspected
arbitrary-rank sources as in L091; no preservation theorem is reproved.

**One determinant and both perfect section forms.** Since H^1(X,O)=0,
the exponential sequence makes Pic(X)->H^2(X,Z) injective. Integral
c_1(F)=0 therefore trivializes det(F) holomorphically. Fix one such
trivialization, with alternating wedge A:F tensor F->O_X, and
nowhere-zero two-forms sigma_i on S_i. For either p:X->B and its
actual degree-one image E, define Q_E by cup, the same A, the relative
sigma_i and trace:

\[
Rp_*F\otimes^{\mathbf L}Rp_*F\longrightarrow Rp_*O_X
\longrightarrow Rp_*\omega_p\longrightarrow O_B[-2].
\tag{4}
\]

Substitute Rp_*F=E[-1] and take degree two to obtain E tensor E->O_B.
Import smooth proper coherent duality in relative dimension two,
[Stacks 48.19(2),(9), 0AU3](https://stacks.math.columbia.edu/tag/0AU3),
[48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT), and
[48.3.6, 0A9Q](https://stacks.math.columbia.edu/tag/0A9Q), using its
internal-Hom comparison only in the bounded coherent/perfect setting.
Here p^!O_B=omega_p[2]. Fibre base change makes (4) the perfect
Serre pairing on H^1(F|_{X_z}), so Q_E is perfect on every fibre
and hence on the bundle. The odd-degree interchange sign and the
alternating coefficient sign cancel: Q_E is symmetric. No positivity,
parallelness or determinant triviality of E is needed.

Single-row Leray, [Stacks 20.13.1/4, 01EZ/01F2](https://stacks.math.columbia.edu/tag/01F2),
gives actual isomorphisms on the same finite-dimensional space

\[
V=H^1(X,F)\xrightarrow{\ell_G}H^0(S_2,G),\qquad
V\xrightarrow{\ell_H}H^0(S_1,H).
\tag{5}
\]

Write d=dim V. For either polystable E, a nontrivial stable summand
M and its stable dual have no sections: the equal-slope stable-Hom
criterion makes a nonzero map O->M an isomorphism, which would make
M trivial. Individual nonzero first classes are permitted. Hence the
full trivial isotypic part is T=O^d, and E=T direct sum W with
H^0(W)=H^0(W^vee)=0. Both cross blocks of Q_E vanish because
Hom(T,W^vee)=Hom(W,T^vee)=0. Perfection of Q_E makes its T block
perfect. The block has constant entries on the connected projective
base. Evaluation identifies H^0(E) with T_z, so Q_E induces a
nondegenerate symmetric form on H^0(E). This is L091's arbitrary-rank
trivial-part method with its fixed count replaced by the actual d;
perfection on E alone would not suffice.

**The same coefficient class forces d=0.** Define B(u,v)=A_*(u cup v)
in H^2(X,O_X). L090's audited coefficient identity applies to this
F without its numerical pair: the coefficient Dolbeault resolution
is Demailly, *L2 vanishing theorems for positive line bundles and
adjunction theory*, alg-geom/9410022v3, 28 February 1995, Section 1.A
(1.1)--(1.3), [pp. 4--5](https://arxiv.org/pdf/alg-geom/9410022v3),
with coefficient Serre pairing Section 4.A (4.3)--(4.4'), pp. 27--28.
The holomorphic A defines a morphism of these resolutions and computes
the coherent cup. Locally a closed representative of u is
alpha=f_1 a_0+f_2 b_0 in a determinant-one frame. Then
A(alpha wedge alpha)=2a_0 wedge b_0, whose scalar exterior square
is zero, since a_0,b_0 have degree one. The resulting closed scalar
form is global. Therefore

\[
B(u,u)^2=0\quad\text{for every }u\in V.
\tag{6}
\]

This uses ordinary coefficient forms, not multiplication of harmonic
representatives. Fix nonzero theta_i in H^2(S_i,O), and put
x=p_1^*theta_1, y=p_2^*theta_2. Cup-defined Künneth,
[Stacks 36.23.1, 0FLN](https://stacks.math.columbia.edu/tag/0FLN),
applies to the projective quasi-compact quasi-separated factors over
C; Tor-independence is over this field. K3 H^1(O)=0 and surface
dimension give H^2(O_X)=Cx direct sum Cy, x^2=y^2=0 and
x cup y a nonzero generator of H^4(O_X). Write
B(u,u)=alpha(u)x+beta(u)y.

The actual comparisons of L090/L091 apply after (3)--(5), in both
directions and all ranks. Explicitly, for a closed fibre square (i,j),
the class u corresponds to s:O_B->Rp_*F[1]=E under (5). Its
counterpart on X is the pullback of s followed by the counit.
The base-change map is adjoint to the pulled-back counit,
[Stacks 20.28.3, 08HY](https://stacks.math.columbia.edu/tag/08HY);
thus s(z) maps to exactly i^*u under our actual fibre isomorphism.
No coefficient Tor correction occurs since E,F are locally free.
Cup and the same A commute with this pullback,
[20.31.7/8, 0FP6/0H99](https://stacks.math.columbia.edu/tag/0H99);
the general proof in 0H99 is omitted in that source, while the
coefficient Dolbeault pullback gives the same comparison here.
The fibre square is Tor independent because p is flat, not because
the point map j is flat. Proper flat finite presentation and the
Noetherian hypotheses permit dualizing base change and trace
compatibility, [48.12.4, 0AAB](https://stacks.math.columbia.edu/tag/0AAB)
and [48.7.1, 0B6J](https://stacks.math.columbia.edu/tag/0B6J).
Applied to the actual morphism (4), they identify its evaluation with
the fibre Serre trace of the restricted determinant cup. Hence

\[
Q_G(\ell_Gu,\ell_Gu)=c_1\alpha(u),\qquad
Q_H(\ell_Hu,\ell_Hu)=c_2\beta(u),\qquad
c_i=\operatorname{Tr}_{S_i}(\sigma_i\theta_i)\ne0.
\tag{7}
\]

The constants are nonzero because multiplication by sigma_i identifies
O with omega and trace is an isomorphism H^2(omega)->C. Functions on
the connected projective bases are constant, so fibre evaluation
proves (7) as equalities of scalars. The same u and the same A are
used twice; no independently chosen image identification intervenes.

Suppose d>0. Pull back the two nondegenerate section forms through
(5), with quadratic polynomials q_G,q_H on V. Each is nonzero by
polarization over C. Choose v with q_G(v) nonzero and w with q_H(w)
nonzero. The polynomials q_G(v+s w) and q_H(v+s w) are nonzero:
the former has nonzero constant coefficient, the latter nonzero
quadratic coefficient. Avoid their finite root sets in C. This gives
one u with both values nonzero in every positive finite dimension,
including dimension one, while allowing isotropic vectors. By (7),
alpha(u)beta(u) is nonzero, so
B(u,u)^2=2alpha(u)beta(u) x cup y is nonzero, contrary to (6).
Thus d=0. This finite-dimensional extension, not a reproof of the
general sources, is required by the enlarged parameter domain.

**Euler threshold and exact region.** The perfect Q_E gives E=E^vee.
Serre duality on its K3 base implies h^2(E)=h^0(E)=d. Thus
chi(E)=2d-h^1(E). The proper-pushforward Euler identity,
[Stacks 33.33.5, 0BEI](https://stacks.math.columbia.edu/tag/0BEI),
applies to these proper complex schemes and coherent F. With the
single nonzero row (3) it gives, for both E=G,H,

\[
\chi(X,F)=-\chi(E)=h^1(E)-2d.
\tag{8}
\]

In particular negative chi(X,F) alone would force
d>=ceil(-chi(X,F)/2)>0, contradicting the cup test. Since d=0 has
already been proved, (8) gives chi(X,F)=h^1(E)>=0 and the asserted
image cohomology. This also shows the limit of the Euler-only test:
if chi(X,F)>=0, its dimension bookkeeping allows d=0 and
h^1(E)=chi(X,F). This is formal compatibility, not image or kernel
existence and not a converse to the exclusion.

Finally L071's full forced character, including the complete mixed
square 156 and relative sign, gives

\[
\chi(X,F)=8-2(m+n)+\frac{mn+78}{6}
=\frac{mn-12m-12n+126}{6}
=\frac{(m-12)(n-12)-18}{6}.
\]

The admitted congruence makes this an integer (indeed even).
This proves precisely (1)--(2). For example m=13,n=18, or
(a,b)=(-17,-22), is admitted, has neither split charge and has
chi=-2, so is excluded. There are infinitely many newly covered
inputs beyond the earlier five-, six- and seven-charge slices and
L090/L091's exact pairs: m=9,n=18+84j for integers j>=0 have
mn=6 modulo 12, neither charge divisible by 14, and
(m-12)(n-12)=-3(6+84j)<18. The originally displayed m=5 tail
also satisfies the theorem but already belongs to L072's entire
five-charge slice; it is an overlap example, not a new exclusion.
No assertion is made about split-charge fibres outside our scope.

At the exact boundary (m-12)(n-12)=18, integer factorization with
m,n>=5 gives, after imposing the congruence and omitting charge 14,
exactly (6,9), (9,6), (13,30), (30,13), (15,18), (18,15).
Indeed the negative factors must both have magnitude at most seven,
leaving (-6,-3) and (-3,-6); positive factors are the ordered
divisors (1,18),(2,9),(3,6) and their reversals, with the charge-14
pairs removed. Each retained pair has mn=6 modulo 12 and no split
charge. Both images would be acyclic there. Such a possibility, and
the positive side of (1), needs other tests or construction; this
argument does not exclude them. Independent common-kernel existence,
prescribed action, transverse transport and the universal Hodge gap
remain unresolved. The older exact-pair and numerical stops are
preserved, not used to claim exclusion of these remaining cases.

**Separate critical audit, 2026-10-11 (step 230).** The uniform
exclusion survives under exactly the stated nonsplit-charge hypotheses.
This audit is EXPLORATION / REPRODUCTION, not a new mathematical
advance: no substantive bridge fails or stronger exclusion is obtained.
The example-overlap wording above is corrected; L072 is a historical
comparison here, not a mathematical premise of this proof.

For each projection, the charge on every fibre is fixed, namely m
or n, and L071 gives its actual compatible Hermite--Einstein connection.
The split-charge exclusion makes each such rank-two polystable fibre
stable. Its dual is stable, and its rank is greater than that of O,
so both endpoint cohomology groups vanish. The positive dimensions
m-4 and n-4 follow from RR separately on every fibre. Thus the
perfect-pushforward/base-change and open bundle-locus applications
in (3) meet their full hypotheses. The complement of the bundle
locus is closed in a finite-type complex scheme and contains no
closed point, so it is empty. No statement only about a generic
fibre or an Euler value substitutes for concentration. BBHR applies
in each direction to the same hermitian kernel, compact source,
compatible spheres and flat source O, with this everywhere odd IT.
Its preserved bundles have their positive ranks in (3), regardless
of the negative alternating classes. The surface contraction and
real-Kähler correspondence give polystability at the unchanged h.

Integral determinant triviality supplies one holomorphic wedge A.
For either E=G,H, relative dimension two gives p^!O=omega_p[2]
and concentration gives Rp_*F=E[-1]. All coefficients are perfect
and bounded coherent. The actual cup/wedge/trace morphism (4)
therefore restricts to the perfect Serre pairing on every H^1 fibre.
Its two interchange signs cancel, giving a symmetric form, in every
image rank. This does not require the form to be positive or parallel.

In the polystable decomposition of E, each stable summand is locally
free as a direct summand of E and has slope zero. Equal-slope stable
Hom vanishing against O applies to every nontrivial summand and its
dual, with no restriction on individual first Chern classes. Thus
the entire section space comes from T=O^d, and both cross blocks
between T and W vanish. The invertible block-diagonal map
E->E^vee has an invertible T block. Since its entries are global
functions on a connected projective surface, they are constants;
evaluation identifies that block with the form on H^0(E). This
justifies section-form perfection for every finite d. When d=0
there is no assertion of a vector with nonzero quadratic value.

Both comparisons in (7) concern the same u in H^1(X,F). More
explicitly, for p:X->B write P=Rp_*F=E[-1] and let
s:O_B->P[1]=E represent u by derived composition. Under adjunction
its counterpart is O_X->Lp^*P[1]->F[1], with the second arrow the
counit. For a closed fibre square (i,j), coefficient base change
is the adjoint of the pulled-back counit, so the image of j^*s=s(z)
is exactly i^*u. Local freeness removes coefficient Tor terms.
The square is Tor independent because p is flat; flatness of j is
unnecessary. The cited smooth proper dualizing identification and
right-adjoint base change identify the pullback of the actual trace
with the fibre trace. Pullback preserves the same A and the cup.
Hence evaluation of Q_E(s,s) is precisely
Tr_(S_i)(sigma_i A_*((i^*u) cup (i^*u))). The two fibre restrictions
of (x,y) are respectively (theta_1,0) and (0,theta_2), proving
both equalities in (7). Multiplication by sigma_i and the Serre
trace are isomorphisms on the relevant one-dimensional groups,
so neither c_i vanishes. No normalization equates the two images
or chooses different coefficient classes for them.

In a determinant-one frame the scalar form 2a_0 wedge b_0 has
square zero before taking cohomology. Frame invariance and the
holomorphic wedge make this a global closed scalar form. Thus
(6) really concerns the same global coherent cup used in (7),
without a multiplicative harmonic-projection assumption. If d>0,
nondegeneracy and characteristic-zero polarization make each q_E
a nonzero polynomial. On v+s w the constant coefficient of q_G
and the quadratic coefficient of q_H are nonzero. This holds in
dimension one and when v,w are dependent as well as in higher
dimension. A complex parameter outside the finite root sets gives
one u with both values nonzero. Künneth makes x cup y nonzero,
and its even degrees give B(u,u)^2=2alpha(u)beta(u)x cup y,
contradicting (6). Therefore d=0, rather than merely an upper bound.

For the Euler sign, concentration shifts by -1 in each derived
pushforward, so chi(X,F)=-chi(E). Self-duality of E and Serre
duality give h^2(E)=h^0(E)=d, whence (8) and the image cohomology
(0,chi(X,F),0). Independently, the full lower character is
-m e_1-n e_2-tau_D, whose square is (2mn+156)P. Rank two and
c_1=0 give ch_4=(mn+78)P/6. Multiplication by
td(X)=1+2(e_1+e_2)+4P gives exactly
8-2m-2n+(mn+78)/6. Writing mn=6+12k shows this is
22-2m-2n+2k, an even integer. This confirms the strict threshold
(m-12)(n-12)<18, with equality giving no Euler contradiction.

For completeness, put x_0=m-12 and y_0=n-12 at equality. They
are integers at least -7 with product 18. Positive ordered pairs
are (1,18),(2,9),(3,6),(6,3),(9,2),(18,1). Negative ordered pairs
within that bound are only (-6,-3),(-3,-6). Adding twelve gives
(13,30),(14,21),(15,18),(18,15),(21,14),(30,13),(6,9),(9,6).
All eight pass mn=6 modulo 12; precisely (14,21) and (21,14)
violate the split-charge exclusion. The other charges are positive
and below 56 and are not 14, hence none equals 14r^2. This proves
the complete six-pair boundary list, without bounded sampling.
Their images would be acyclic by (8); this is neither existence
nor a claim that other recorded tests cannot exclude some of them.

The corrected infinite example has m=9 and n=18+84j, so its
residue is 9*6=6 modulo 12 and n=4 modulo 14. Both charges are
nonsplit and its product threshold is -18-252j<18. The former m=5
example is retained explicitly as overlap with L072. This correction
changes no hypothesis, exclusion region or direct mathematical input.
The audit imports the already assessed general theorems rather than
reproving them. Nonnegative Euler, split-charge cases, actual common
kernels, transport and universal primitive Hodge realization remain
outside this conclusion. No new-domain result is established here.

## Mathlib

Full matching coverage of this uniform exclusion, arbitrary-rank
preservation, coefficient Dolbeault and both actual trace comparisons:
**not checked**. Unknown coverage is not absence. The precise general
inputs above are imported; only their uniform applicability, the
variable-dimensional polynomial argument and the Euler-region
specialization are proved here. No mathematical script or numerical
preview is used as proof. The separate critical audit above preserves
these conclusions and qualifications.
