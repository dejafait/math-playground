# L137 — Opposite determinant pullbacks and fixed projective parameters

## Hypotheses

Retain L071's identical marked smooth projective complex K3 surfaces
X=B x Y=S_1 x S_2, the common metric and real class h, and the full
integral mixed tensor tau_D. The correspondence convention is
p_{2*}(tau_D p_1^*a)=D(a); its cup-product adjoint is D^*=D.
Write e_1=eta tensor 1, e_2=1 tensor eta and integral_S eta=1.
Suppose F is locally free of rank two, Omega-slope-polystable, with
integral c_1(F)=0 and

\[
             \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Use L118's own very ample integral H on Y, fixed using the surface,
h and rank-two charge-21 invariants, uniformly for all sheaves with
those invariants. Use its actual all-stable classifying map
f:B -> M_H^s(2,0,-19). By L120 its reduced integral image Z has
finite birational normalization nu:B -> Z. Neither point separation,
normality or Cohen--Macaulayness of Z nor existence of F is assumed.

Put t=H^2, b=[O_H] in K(Y), and c for the numerical fibre K-class.
Fix a closed point y of Y and, with b^0=[O_Y], set

\[
 u_i=-2b^i+\chi(cb^i)[O_y],\qquad L_i=\lambda(u_i),\quad i=0,1.
\]

The determinant convention is det of the alternating derived
pushforward, as in the cited whole-semistable descent theorem.

## Conclusion

For this opposite family the actual pullbacks are

\[
 f^*L_0\simeq O_B,\qquad c_1(f^*L_1)=2D^*(H)=2D(H)
                                  \quad\hbox{in }H^2(B,\mathbb Z).       \tag{1}
\]

In particular D(H) is an integral divisor class. Let Mbar be the
fixed-numerical-class, determinant-O_Y projective Gieseker moduli
space containing this stable open. One may fix a positive integer
ell for which A=L_0 tensor L_1^ell is ample on Mbar, then a positive
integer k for which A^k is very ample. Set

\[
 N=h^0(Mbar,A^k)-1,\qquad j:Mbar\hookrightarrow\mathbf P^N
\]

using its complete linear system. All these choices depend only
on the fixed surface, H, numerical class, determinant and chosen
point y, independently of F, Z and their unknown Hilbert data.
They are existence choices, with no numerical thresholds supplied.
For the restriction of this actual embedding to the original Z,

\[
 \boxed{\deg j(Z)=\delta=4k^2\ell^2 q(D(H),D(H)).}                    \tag{2}
\]

Thus the degree is specified by the fixed choices and surface
intersection form. It is positive under the conditional hypotheses;
D(H) is then ample. For Hoa's reduced-coordinate-ring framework the
parameters are n=N+1 variables, ring dimension d=3, c=N-2 and
e=adeg=delta. This identifies the input parameters; it does not
apply Hoa's inequalities or bound a normalization defect.

This conditional ADVANCE / REPRODUCTION resolves the parameter
obligation using known tools. It is not progress beyond those general
sources, a numerical effective embedding bound, a contradiction,
existence of F, or a new algebraic Hodge class. The separate critical
audit below preserves the result. Quantitative usefulness of a global defect
comparison, transport and universal primitive Hodge realization remain
unresolved.

## Proof

**Scope and imported framework.** The pre-existing SPECIALIZE gate is
`drafts/literature/2026-10-20-opposite-projective-polarization-specialization.md`.
Use Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves*,
Aspects of Mathematics E31 (1997),
[Theorem 8.1.5, Definition 8.1.9, Proposition 8.1.10, Theorem 8.1.11,
Remark 8.1.12(i), pp. 180--185; Section 8.3 and Proposition 8.3.1(ii),
pp. 195--197](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf).
The first statements give the descended lines, actual-family
pullback and sufficiently-large-ell ampleness on the fixed-determinant
projective surface moduli space. Section 8.3 gives K-theoretic GRR.
These general theorems are imported without reproof. L107 is a
comparison for a different projection and is not used as an input.
Neither L129's local defect bound nor L136's Hom Euler identity is
used. No new source discovery or theorem beyond the saved scope is
claimed.

**Descent hypotheses and fibre calculations.** L118 supplies flatness,
the fixed numerical class, and stability of every geometric fibre.
Integral c_1(F)=0 and Pic(Y) -> H^2(Y,Z) injective imply determinant
O_Y on each fibre. The numerical-class part is open and closed in
the projective fixed-polynomial Gieseker space, and its determinant
fibre is closed. Consequently Mbar is projective. On this K3 all
sheaves in that numerical class already have determinant O_Y.
No primitive vector, generic polarization or universal sheaf is
needed for the cited determinant results.

For clarity the classes lie in the whole-space descent domain
K_{c,H}=c^perp intersect {1,b,b^2}^{perp perp}, with pairing
(v,w) -> chi(vw). If a is orthogonal to 1,b,b^2, then
ch(b^2)=t eta and 0=chi(ab^2)=t rank(a). Since t>0,
rank(a)=0 and chi(a[O_y])=0. Thus [O_y] is in the double
perpendicular, integrally; so are u_0,u_1. Moreover
chi(c[O_y])=2 implies chi(cu_i)=0. This checks the descent
hypotheses without dividing a K-class or assuming b^2=t[O_y]
in the actual K-group.

Since ch(c)=2-21eta and td(Y)=1+2eta, surface HRR gives

\[
 \begin{aligned}
 \chi(c)&=-17,& \operatorname{ch}(b)&=H-(t/2)\eta,\\
 \chi(cb)&=-t,& \operatorname{ch}(u_0)&=-2-17\eta,\\
 &&\operatorname{ch}(u_1)&=-2H.                                  \tag{3}
 \end{aligned}
\]

The point term cancels the degree-four term of -2b exactly.
The book's descent identity for the actual family is

\[
        f^*L_i=\det Rp_{1*}(F\otimes^{\mathbf L}p_2^*u_i).         \tag{4}
\]

The complex is perfect on the smooth base B. Separate ordinary
higher-direct-image ranks need not be constant for (4) or GRR.

**Actual rank-two characters.** Rank truncation and the Chern
character polynomials give c_3=c_4=0, ch_1=ch_3=0 and
ch_4=c_2^2/12 when rank(F)=2 and c_1=0. These are the standard
identities used in L071, from Fulton, *Intersection Theory*, 2nd ed.,
Theorem 3.2(a), and [Stacks, 02UM](https://stacks.math.columbia.edu/tag/02UM).
In particular L071's full tau_D^2=156e_1e_2 gives
ch_2(F)^2=(588+156)e_1e_2 and ch_4(F)=62e_1e_2.
These are the characters of the hypothetical actual bundle, rather
than a retained virtual representative. Only ch_1 and ch_3 enter
the first determinant computation; ch_4 cannot enter base degree two.

**Opposite relative GRR and integral lines.** Cancel the base Todd
factor in relative GRR. With fibre Y the formula is

\[
 c_1(f^*L_i)=
 \left[p_{1*}\left(\operatorname{ch}(F)\,
            p_2^*\operatorname{ch}(u_i)(1+2e_2)\right)\right]_2.  \tag{5}
\]

For i=0 the other factor is -2-21e_2. Total degree six could
only come from ch_3(F) or ch_1(F)e_2, both zero. Hence this
pullback has zero rational first Chern class. For i=1 the factor
is -2p_2^*H, since H eta=0 on Y. The e_2 H contribution
vanishes by fibre dimension. The e_1 H contribution has fibre
degree two, so its pushforward is zero. The remaining term is

\[
 c_1(f^*L_1)=2p_{1*}(\tau_D p_2^*H)=2D^*(H)=2D(H).                \tag{6}
\]

Indeed, for any a on B the pairing of p_{1*}(tau_D p_2^*H)
with a is q(Da,H)=q(a,D^*H). Exchanging the two degree-two
factors has sign +1. This checks the opposite orientation on the
full tensor, including its divisor part; there is no independently
integral NS/transcendental splitting. As an independent sign check,
Huybrechts--Lehn Proposition 8.3.1(ii) gives
p_{1*}(Delta(F) p_2^*H)/2. Here Delta=4c_2 and
c_2=14e_1+21e_2+tau_D, so it gives the same +2D(H).

The full tensor and H are integral, hence the pushforward D(H)
is integral, and it has type (1,1). Lefschetz (1,1) makes it a
divisor class. Torsion-free H^2(B,Z) upgrades (5)--(6) to integral
identities. The exponential sequence and H^1(B,O_B)=0 make
c_1:Pic(B) -> H^2(B,Z) injective, so the first line is actually
trivial. This proves (1).

**Fixed embedding choices.** Fix Mbar and the descended lines from
its surface and moduli data before using any image or defect.
The cited ample-combination theorem permits a fixed sufficiently
large positive ell. The definition of an ample line bundle on a
projective scheme, equivalently Hartshorne, *Algebraic Geometry*,
Chapter II, Theorem 7.6, permits a fixed positive k with A^k very
ample. Finite-dimensionality of global sections on the projective
scheme gives the stated N and complete-system closed immersion.
Neither step uses the Hilbert polynomial of Z. Dependence on the
fixed moduli space, including its own geometry and section space,
is allowed; an algorithm or explicit bound for ell,k,N has not
been supplied by this argument.

The actual image in Mbar is the same Z as in the stable open.
To check this without a boundary assumption, compose the actual
map with M_H^s -> Mbar. It is proper because B is projective and
Mbar separated, and quasi-finite because its fibres are unchanged
from L120. It is finite by
[Stacks, Lemma 37.44.1, 02LS](https://stacks.math.columbia.edu/tag/02LS).
Its scheme-theoretic image is reduced and integral, since its
source is; its closed support is f(B), contained entirely in the
stable open. Restriction there recovers L120's scheme-theoretic
image. Thus j restricts to a closed immersion of the original
reduced Z, without adding boundary points or changing its structure.
Write L=A^k|_Z for its hyperplane line. Equations (1) give

\[
                  c_1(\nu^*L)=2k\ell D(H).                     \tag{7}
\]

Finite pullback of an ample line is ample, by
[Stacks, Lemma 30.17.2, 0B5V](https://stacks.math.columbia.edu/tag/0B5V).
Apply it to nu, finite and surjective between proper schemes.
It follows that D(H) lies in the real ample cone and has positive
square. This is a conditional consequence, not a proof that D
preserves the whole ample cone or that F exists.

**Degree under finite birational normalization.** The exact sequence

\[
          0\longrightarrow O_Z\longrightarrow\nu_*O_B
                      \longrightarrow Q\longrightarrow0          \tag{8}
\]

has Q supported on a proper closed subset of the integral surface
Z: the finite birational map is an isomorphism at its generic
point. Thus dim Supp(Q)<=1, which already suffices here; no
coherent vanishing or local length formula is needed. The
Hilbert--Serre theorem makes chi(Z,Q tensor L^m) a polynomial
of degree at most one (zero if Q=0). Finite pushforward is exact,
and its projection formula gives

\[
 \chi(B,(\nu^*L)^m)=\chi(Z,\nu_*O_B\otimes L^m)
                  =\chi(Z,L^m)+\chi(Z,Q\otimes L^m).             \tag{9}
\]

The generic rank in (8) is one because nu is birational; no
closed immersion of nu is being assumed. K3 HRR and (7) give

\[
 \chi(B,(\nu^*L)^m)=2+\frac{m^2}{2}(2k\ell D(H))^2.              \tag{10}
\]

The leading coefficient of chi(Z,L^m) is deg j(Z)/2 by the
Hilbert-polynomial degree theorem. Comparing (9)--(10) proves
(2). Equivalently this is the degree-one finite projection formula
for the hyperplane self-intersection. Every term affecting lower
Hilbert coefficients is retained in Q rather than set to zero.

Finally, the homogeneous ideal of the integral reduced projective
Z is prime. Its homogeneous coordinate ring in N+1 variables is
a domain of dimension three. Its only associated prime is its
minimal prime, so arithmetic degree equals ordinary degree; this
is the arithmetic-degree convention in Hoa,
[*Finiteness of Hilbert functions and bounds for Castelnuovo--Mumford
regularity of initial ideals*, arXiv:math/0608118v1,
pp. 4--5, Theorems 0.2/4.1](https://arxiv.org/pdf/math/0608118v1).
Consequently n,d,c,e,adeg have the values claimed. The original
embedding can be linearly degenerate; no generic projection or
change of its coordinate ring was made. No regularity inequality,
Hilbert-constant estimate or defect comparison is derived in this
bounded parameter step.

**Separate critical audit, 2026-10-20 (step 427).** The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-20-opposite-projective-parameters-critical-audit.md`.
The audit finds no substantive error, stronger obstruction or existence
conclusion. Its outcome is EXPLORATION / RESEARCH / REPRODUCTION,
with actual task type proof_audit. It checks the specialization of
the cited theorems rather than claiming a new general result. The
mathematical inputs remain L071, L118 and L120.

The opposite restriction has charge 21, not 14: its character is
2-21eta and its Mukai vector is (2,0,-19). Independently expanding
(2-21eta)(1+2eta) gives Euler characteristic -17; multiplying
additionally by H-(H^2/2)eta gives -H^2. Thus the point terms in
u_0 and u_1 have exactly the signs and coefficients in (3).
For the descent-domain test, b^2 has character H^2 eta, so
chi(ab^2)=H^2 rank(a) for every K-class a. Orthogonality forces
rank(a)=0, and chi(a[O_y])=rank(a) then vanishes. This proves
membership of [O_y] in the double perpendicular without division
in K(Y). Orthogonality of u_i to c follows from chi(c[O_y])=2.
These are the whole-semistable hypotheses of Huybrechts--Lehn
Theorem 8.1.5, with their Definition 8.1.9 convention, not merely
the weaker stable-open descent hypotheses.

Rank truncation of the actual bundle, together with integral c_1=0,
gives ch_1=ch_3=0. The full square is 2(14)(21)+156=744,
and the resulting fourth-character coefficient is 62. For the
determinant calculation this last term has excessive total degree:
base H^2 after integration over a surface requires total degree six.
For u_0 the only candidates are ch_3 and ch_1 times eta_Y,
and both vanish. For u_1 the sole surviving term is
2tau_D p_2^*H; the two pure terms have respectively insufficient
or excessive fibre degree. Pairing its pushforward with arbitrary
a in H^2(B) gives 2q(Da,H)=2q(a,D^*H). The full self-adjoint
operator from L071, rather than only its positive-plane action,
therefore gives +2DH. The independent discriminant formula in
Huybrechts--Lehn Proposition 8.3.1(ii) agrees. Integrality of tau_D
and H makes DH integral directly, and torsion-free H^2 upgrades
the rational GRR identity. Picard injection on the K3 then proves
actual triviality of f^*L_0; rational Chern-class vanishing alone
on an arbitrary base would not suffice.

L118's polarization construction quantifies over all torsion-free
sheaves with fixed rank and Chern classes in a relative wall stratum.
Its compact neighborhood, rational point, denominator and very ample
power can thus be selected from Y,h and those invariants before
choosing F. With H fixed, the numerical-class locus is open and
closed in the projective fixed-polynomial moduli scheme. A numerical
first class zero has zero divisor class by nondegeneracy of the
K3 Neron--Severi intersection form, and Pic^0(Y)=0 with torsion-free
H^2 fixes its determinant. Equivalently, one restricts to the closed
determinant-O_Y fibre. The cited Theorem 8.1.11 and Remark 8.1.12(i)
give the ample combination there. Hence ell, k and the entire
section space defining N depend on fixed moduli data, with no
dependence on Z's Hilbert polynomial. This is an existence argument
for fixed choices, not an effective estimate for any of them.

The composition B -> Mbar is proper because B is projective and
Mbar separated. Its geometric fibres are the original finite
fibres, so Stacks 02LS applies. On each affine open the quotient
by the image-kernel ideal embeds in sections on a reduced inverse
image; hence the kernel is radical. Properness makes its support
the closed set f(B), entirely within the stable open. Restriction
to that open gives exactly L120's original image, so no boundary
components or nilpotent structure have been added. The restriction
of j is a closed immersion of Z, whereas nu remains only the
finite birational normalization. Stacks 0B5V applies to its ample
hyperplane pullback and establishes the stated conditional ampleness.

For the degree calculation, O_Z -> nu_*O_B is injective and an
isomorphism at the generic point of this integral surface. Therefore
Q in (8) has support dimension at most one. The precise general
inputs are [Stacks, Lemmas 33.45.1--2, Definition 33.45.10 and
Lemma 33.45.11](https://stacks.math.columbia.edu/tag/0BEL):
support dimension bounds the Euler-polynomial degree, generic
lengths determine top coefficients, and a finite dominant map
multiplies degree by its function-field degree. None requires
normality or Cohen--Macaulayness of Z. Finite pushforward and its
projection formula justify (9); K3 HRR gives (10). Generic rank
one therefore identifies the quadratic coefficients and yields
exactly 4k^2 ell^2 q(DH,DH), with no lost factor two. The linear
and constant contributions of Q are not evaluated or set to zero.

Finally the actual homogeneous coordinate ring is a domain, even
if the chosen embedding is linearly degenerate. Its dimension is
three, its polynomial presentation has N+1 variables, and its
only associated prime has generic length one. Thus c=N-2 and
adeg=e=delta agree with Hoa's cited definitions. No inequality
from Hoa is applied in this audit.

The bounded continuation test passes. The audit preserves the
conditional projective input, not a quantitative defect comparison.
It supplies no numerical ell,k,N, no F or collision, no coherent
vanishing and no new Hodge algebraicity. ATTEMPTS/070,073,078 and
the parked order-five route remain intact. A separate specialization
must address the normalization quotient's support and Hilbert
constant before claiming a total-defect bound or testing its use.

## Mathlib

Full matching coverage for whole-semistable determinant descent,
fixed-determinant positivity and this exact opposite-family
projective specialization: **not checked**. Supporting Chern,
HRR, Hilbert-polynomial and intersection results are used through
the named classical inputs above; no absence from Mathlib is claimed.
