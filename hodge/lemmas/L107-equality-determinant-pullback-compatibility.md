# L107 — Equality-family determinant pullbacks and compatible ampleness

## Hypotheses

Retain L071's identical marked projective K3 surfaces S_1 and
B=S_2, real ample class h, integral self-adjoint mixed tensor tau_D,
and correspondence convention

\[
 p_{2*}(\tau_D p_1^*x)=D(x),\qquad D(h)=2\lambda h,
 \qquad 1<\lambda<5/4.
\]

Suppose the locally free rank-two Omega-polystable F of L097 exists,
with integral c_1(F)=0 and

\[
 \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D,
 \qquad e_1=\eta\otimes1,\quad e_2=1\otimes\eta,
 \quad\int_S\eta=1.
\]

Use L097's actual algebraic flat family and its whole classifying
map f:B -> M_H^{ss}(2,0,-12), for a common very ample H with
H.k=0. L098 makes f finite, with a finite surjective factor onto
its reduced projective image. The finite reducible set Z may be
empty. No universal sheaf or generic polarization is assumed.

Write c for the numerical fibre K-class, b=[O_H] in K(S_1), and
x for a closed point of S_1. With the determinant of the alternating
derived pushforward convention, put

\[
 u_i=-2b^i+\chi(c b^i)[O_x],\qquad L_i=\lambda(u_i),
 \qquad i=0,1,
\]

where b^0=[O_{S_1}]. These are the whole-semistable-space
determinant lines in the cited construction below.

## Conclusion

The actual pullbacks satisfy

\[
 f^*L_0\simeq O_B,\qquad c_1(f^*L_1)=2D(H)\quad
                       \hbox{in }H^2(B,\mathbb Z).                 \tag{1}
\]

The right side is an integral divisor class. In particular the
published ample combination L_0 tensor L_1^ell, for sufficiently
large positive integers ell, imposes precisely the necessary
condition D(H) in Amp(B). This condition is compatible with the
retained full D: L097's rational same-stratum choice can be made
so that D(H) is ample as well as H. This proves compatibility of
this bounded filter, not existence of F or preservation of the
entire ample cone by D.

This is a NEGATIVE / REPRODUCTION for exclusion by these two
determinant classes, using the pre-existing SPECIALIZE assessment
drafts/literature/2026-10-15-equality-determinant-pullback-test.md.
The separate critical audit below preserves this compatibility stop.
Common-kernel existence,
other representatives, transverse transport and universal primitive
rational Hodge realization remain unresolved.

## Proof

**Import the determinant framework.** Use Huybrechts--Lehn,
*The Geometry of Moduli Spaces of Sheaves*, Aspects of Mathematics
E31 (1997), [Theorem 8.1.5, Definition 8.1.9, Proposition 8.1.10,
Theorem 8.1.11 and Remark 8.1.12(i), pp. 180--185; Section 8.3
and Proposition 8.3.1(ii), pp. 195--197](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf).
Their whole-space descent gives

\[
 f^*\lambda(u_i)=\det Rp_{2*}(F\otimes^{\mathbf L}p_1^*u_i).
                                                                    \tag{2}
\]

It applies to the actual flat family, including its strictly
semistable fibres, and uses no moduli universal sheaf. Integral
c_1(F)=0 fixes each fibre determinant to O_{S_1}, since Pic(S_1)
injects into H^2(S_1,Z). Thus f lands in the fixed-determinant
part, on which the cited sufficiently-large-ell combination is
ample. The sign convention for u_i is also recorded in
[Abe, *Semistable sheaves with symmetric c_1 on a quadric surface*,
Nagoya Math. J. 227 (2017), Section 10.1, pp. 151--152](https://doi.org/10.1017/nmj.2016.50).
Only that convention is used from Abe, not a quadric-specific theorem.
These general results and the book's K-theoretic family GRR are
imported; they need no reproof here. Derived pushforward is perfect
on the smooth base, so its determinant and GRR do not require
constant ranks of its separate cohomology sheaves.

**Evaluate the K-classes.** Put t=q(H,H). The surface exact sequence
for O_H gives ch(b)=1-exp(-H)=H-(t/2)eta. The fibre character is
ch(c)=2-14eta and td(S_1)=1+2eta. Surface HRR therefore gives

\[
 \chi(c)=-10,\qquad \chi(c b)=-t,
 \qquad \operatorname{ch}(u_0)=-2-10\eta,
 \qquad \operatorname{ch}(u_1)=-2H.                                \tag{3}
\]

In the last identity, the +t eta from -2b cancels the -t eta
from the point term. The evenness of the K3 intersection form
also makes t/2 integral, although GRR is evaluated rationally.
For rank two with c_1=0, the Chern character identities give
ch_1(F)=ch_3(F)=0, as in L071. No former virtual higher character
is substituted for the actual bundle.

**Compute degree two on the base.** The book's relative GRR and
c_1(det E^bullet)=ch_1(E^bullet) give

\[
 c_1(f^*L_i)=
 \left[p_{2*}\left(\operatorname{ch}(F)
              p_1^*\operatorname{ch}(u_i)(1+2e_1)\right)\right]_2.
                                                                    \tag{4}
\]

Here the relative Todd factor is that of S_1; the base Todd factor
has already cancelled in relative GRR. For i=0, the other factor
in the integrand is -2-14e_1. A total degree-six term could only
come from ch_3(F) or ch_1(F)e_1, both zero. Hence the first
pullback has zero rational first Chern class.

For i=1, H eta=0 on S_1, so its other factor remains -2p_1^*H.
Only ch_2(F) contributes in total degree six. The term e_1 H
vanishes by first-factor dimension. The term e_2 H has first-factor
degree two, so its fibre integral is zero. Consequently

\[
 c_1(f^*L_1)
  =2p_{2*}(\tau_D p_1^*H)=2D(H).                                  \tag{5}
\]

This uses the full integral tau_D and the stated correspondence
orientation. Its transcendental projection pairs trivially with H,
but its divisor projection has not been treated as an independently
integral tensor. Higher characters cannot contribute by degree.
As a sign check, Proposition 8.3.1(ii) gives
p_{2*}(Delta(F)H)/2 with Delta(F)=4c_2(F) here; its mixed
contribution is again +2D(H), since c_2(F)=-ch_2(F).

The integral pushforward of the full integral tau_D paired with H
is integral, so D(H) is an integral class of type (1,1).
Lefschetz (1,1) makes it a divisor class. H^2(B,Z) is torsion-free,
so (4)--(5), initially rational identities, give the asserted integral
identities. The exponential sequence and H^1(B,O_B)=0 give
injectivity of c_1:Pic(B)->H^2(B,Z); thus f^*L_0 is actually trivial.
These are the standard K3 and Lefschetz inputs, not a division of
an integral determinant class by an unverified lattice factor.

**Test the actual divisor cone.** Restrict the ample combination to
the reduced projective image and apply finite pullback ampleness,
[Stacks, Lemma 30.17.2, Tag 0B5V](https://stacks.math.columbia.edu/tag/0B5V),
to L098's finite surjective factor. It follows that

\[
 c_1(f^*(L_0\otimes L_1^{\ell}))=2\ell D(H)
                       \quad\hbox{is ample for all large }\ell.    \tag{6}
\]

Since ell is positive and f^*L_0 is trivial, this is equivalent
to ampleness of the actual line f^*L_1, or to D(H) in the real
ample cone. No ampleness of L_1 on the entire moduli space is used.

To evaluate compatibility at permitted H, identify the divisor spaces
of the two marked factors and let A be their open real ample cone.
The linear map D restricts to N^1(S)_R. Since
D(h)=2lambda h belongs to A, the open set

\[
                       V=A\cap D^{-1}(A)
\]

contains h. This is a divisor-cone argument, not merely positivity
on the hyperkahler three-plane. In L097's proof, intersect the small
relative neighborhood of h in its rational subspace W with V.
That proof's finitely many nonvanishing wall functionals keep their
strict signs after this further shrinking; every wall through h
and the equality k.alpha=0 are still imposed exactly. Density of
W_Q in W supplies a rational alpha in this intersection. Thus both
alpha and D(alpha) are ample, while alpha remains in the same
relative wall stratum as h for every fixed-Chern sheaf at once.

Clearing denominators and taking a very ample positive power gives
H=m alpha as in L097. Then D(H)=mD(alpha) is ample. All stable
fibres remain slope-stable and all split fibres keep equal reduced
Hilbert polynomials, so the same actual-family moduli construction
applies. L098's finiteness argument uses precisely these properties
and the unchanged stable derivative and therefore applies to this
choice too. This proves that the necessary condition (6) has
permitted choices satisfying it. It asserts neither that arbitrary
permitted H has ample D(H) independently of F, nor that D carries
the whole ample cone into itself. The bounded determinant filter
is compatible and stops without a kernel-existence conclusion.

**Separate critical audit (2026-10-15).** The pre-existing SPECIALIZE
assessment is
`drafts/literature/2026-10-15-equality-determinant-pullback-critical-audit.md`.
This audit checks the complete conditional specialization, using L071,
L097 and audited L098. It finds no substantive error and no stronger
exclusion. The following details make the descent and integral checks
explicit; they do not reprove the published determinant theorems.

First, the domain in Huybrechts--Lehn Definition 8.1.4 is

\[
 K_{c,H}=c^\perp\cap\{1,b,b^2\}^{\perp\perp},
 \qquad \langle v,w\rangle=\chi(vw).
\]

Write t=H^2>0. For any a in {1,b,b^2}^perp, surface HRR and
ch(b^2)=t eta give

\[
 0=\chi(ab^2)=t\,\operatorname{rk}(a),\qquad
 \chi(a[O_x])=\operatorname{rk}(a)=0.
\]

Thus [O_x] lies in the double perpendicular integrally: this argument
uses no division of a class in K(S_1), nor an assertion that
b^2=t[O_x] in the actual K-group. Since chi(ab^i)=0 for i=0,1,
both u_i also lie in that double perpendicular. Moreover,

\[
 \chi(cu_i)=-2\chi(cb^i)+\chi(cb^i)\chi(c[O_x])=0,
 \qquad \chi(c[O_x])=2.
\]

They therefore belong to K_{c,H}, not merely to the stable-open
domain c^perp. Theorem 8.1.5(2) now applies to L097's whole actual
flat family. Its polystable stabilizer and frame-bundle proof cases
(pp. 181--182) were checked against this domain; no rank constancy
for F tensor u_i is needed. As a direct check at the exceptional
object, chi(L^{+/-1})=-5 and H.k=0 give
chi(L^{+/-1}u_0)=-2(-5)-10=0 and
chi(L^{+/-1}u_1)=-2(+-k.H)=0. Both summand stabilizers act
trivially on both determinant fibres. These equalities are not being
used as a substitute for descent over the rest of the moduli space.

Second, the actual integral first class gives det(F_y)=O_{S_1}:
H^1(S_1,O)=0 makes the exponential-sequence first-class map
injective. The determinant morphism of the actual family thus lands
in the fixed-determinant fibre. Equivalently, Pic(S_1) is discrete
and reduced and the connected base maps constantly to O_{S_1}.
There is no hidden base infinitesimal motion in this assertion.
Theorem 8.1.11 and Proposition 8.1.10, with the surface statement in
Remark 8.1.12(i) and the opening of Section 8.2, give the positive
large-exponent combination used in (6). This is relative ampleness
specialized to that fibre; L_1 itself need not be ample on M.

Third, a fresh degree check of (3)--(5) retains the point term in
both u_i. Multiplication of 2-14 eta by 1+2 eta gives 2-10 eta,
so chi(c)=-10. Multiplication by H-(t/2)eta instead gives Euler
value -t. Hence ch(u_0)td(S_1)=-2-14 eta and
ch(u_1)td(S_1)=-2H. A first Chern class after surface integration
requires total cohomological degree six. In the first expression
only ch_3(F) and e_1 ch_1(F) can occur, and both vanish for this
actual rank-two determinant-trivial bundle. In the second expression
the two negative signs, in ch_2(F)'s mixed term and in -2H,
give +2 tau_D H. Neither pure factor term survives fibre integration.
This checks the alternating determinant sign rather than assigning
the determinant of a single higher direct image. The relative Todd
factor contains no base Todd contribution, and ch_4 cannot contribute.

The integral Kunneth tensor is used before projection to rational
N and T summands. Pairing and oriented first-factor pushforward give
D(H) in H^2(B,Z) with the convention of the hypotheses. This class
is of type (1,1); the full D preserves the rational divisor space.
Torsion-free H^2(B,Z) upgrades the two rational GRR equalities to
integral equalities, and Picard injection gives the actual trivial
line in (1). In particular 2D(H) being integral is not the reason
for declaring D(H) integral. Its integral tensor construction is.

Finally, restrict the ample combination to L098's reduced projective
image. Its actual finite surjective factor has proper source and
target over C, so Stacks 0B5V applies without normality or degree
one. The pulled-back class is exactly 2ell D(H), with ell>0.
Positive scaling preserves the real ample cone, which proves the
necessary ampleness condition, not existence of the family.

For the compatibility test keep the compact convex neighborhood K,
finitely many rational wall equations and rational subspace W from
L097. Since D(h)=2lambda h is ample and D is linear, choose a
sufficiently small relative ball about h in W contained in
int(K), Amp(S_1), and D^{-1}(Amp(B)), on which every wall not
containing h keeps its sign. Such a ball exists even when W is
proper; h belongs to all its defining open sets. The rational points
of W are dense. A rational alpha in the ball stays on every wall
through h and on k^perp; the segment from h to alpha stays in K
and in the same wall stratum. L097's uniform fixed-Chern theorem
therefore retains all its stable fibres, and its actual split-line
polynomial check still applies. Clearing denominators and taking a
very ample power multiply H and D(H) by the same positive integer.
All slope comparisons and k-orthogonality survive that scaling.
L098 only needs these placement properties and the unchanged actual
stable differential; its finite-map proof applies to the new choice.
This verifies the permitted choice, without claiming that every
allowed H independently has ample D(H) or that D preserves the
whole ample cone.

The audit preserves ATTEMPTS/065's bounded stop, including Z empty.
It adds no mathematical dependency, existence conclusion, cycle,
transport or universal Hodge realization. Its completed outcome is
EXPLORATION / REPRODUCTION: independent verification with explicit
applicability details, not an advance beyond the cited sources.

## Mathlib

Full matching coverage for whole-semistable determinant descent,
fixed-determinant positivity, family GRR and this exact real-stratum
specialization: **not checked**. Unknown coverage is not absence.
The cited primary results supply the general framework; (3)--(6)
and the neighborhood argument are its conditional specialization.
