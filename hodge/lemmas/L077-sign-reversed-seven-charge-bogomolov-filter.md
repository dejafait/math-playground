# L077 — Sign-reversed seven-charge direct-image Bogomolov filter

## Hypotheses

Retain L071's marked smooth projective complex K3 surface S, real
Kähler class h and identical hyperkähler metric on both factors of
X=S x S. Write Omega=p_1^*h+p_2^*h, e_1=eta tensor 1,
e_2=1 tensor eta and P=e_1e_2, with integral_S eta=1.
Use L071's **full integral** mixed class tau_D, including the divisor
and transcendental blocks, with tau_D^2=156P. Its operator D is
q-self-adjoint, scalar 2lambda on the metric's positive three-plane
and preserves its orthogonal complement, as specified there.

Let b be any integer in L071's survivor domain at a=-11:

\[
b\leq-9,\qquad -7(b+4)\equiv6\pmod{12}.                 \tag{1}
\]

Suppose F is an actual locally free holomorphic rank-two bundle on X,
slope-polystable at the real class Omega, with integral c_1(F)=0 and

\[
\operatorname{ch}_2(F)=-7e_1+(b+4)e_2-\tau_D.             \tag{2}
\]

Initial higher characters and the initial K-class are unrestricted.
No existence of F, opposite-fibre stability, transform equivalence,
inverse, reconstruction, gluing or transverse transport is assumed.

## Conclusion

For pi=p_2 the actual holomorphic image G=R^1pi_*F is locally free
of rank three, commutes with algebraic base change, and carries a
compatible unitary quaternionic-instanton connection. It is
slope-polystable of slope zero at the unchanged h, allowing reducibility.
Necessarily

\[
R^i\pi_*F=0\ (i\ne1),\qquad R\pi_*F\simeq G[-1],
\qquad \pi_![F]=-[G],                                  \tag{3}
\]
\[
\operatorname{ch}(G)=3-\frac{5b+98}{6}\eta,\qquad
c_1(G)=0\text{ integrally},\qquad
c_2(G)=\frac{5b+98}{6}\eta.                             \tag{4}
\]

Domain (1) is exactly b=-10-12j for integers j>=0. The real-metric
Bogomolov inequality on G requires

\[
\int_S c_2(G)=8-10j\geq0.                               \tag{5}
\]

Thus **only b=-10 passes this particular necessary test**; every
b=-22,-34,-46,... is excluded as a realization of (2). At b=-10
the image has rank three and charge eight, and its discriminant
number is 48. Passing this test asserts neither image nor F
existence and does not decide that remaining input. No equality-case
or stable-image assertion is made.

This informative NEGATIVE result is a REPRODUCTION/specialization
of the approved preservation, base-change, GRR and real-metric
Bogomolov inputs. It eliminates infinitely many candidates in this
slice but supplies no algebraic cycle, transverse surface, originality
claim or resolution of universal primitive Hodge-class algebraicity.
The separate critical audit below preserves this necessary filter
without a substantive repair or stronger conclusion.

## Proof

**The actual kernel and every-fibre odd IT.** L071 applies to (1)--(2).
Its proof first establishes stability of F: a polystable rank-two
splitting into lines has mixed character supported on divisor tensors
and annihilates the holomorphic two-form, whereas -tau_D acts there
by the nonzero scalar -2lambda. Its invariant full c_1,c_2 and
Verbitsky's connection criterion then supply the actual compatible
unitary hyperholomorphic connection. Neither topological existence
nor positivity of the mixed scalar is used. This connection is
quaternionic for the simultaneous rotations of these identical metrics.

For every closed y in S, L071's equivariant curvature-restriction
argument makes E_y=F|_(S x {y}) locally free, rank two and
slope-polystable at h, with c_1(E_y)=0 and c_2(E_y)=7eta.
The pure second-factor and mixed classes restrict to zero. A
nonstable polystable factor at this h has charge 14r^2, r in Z,
by L071's exact zero-slope line lattice. Seven cannot have that form,
so every E_y is stable. This is a curvature argument on every fibre,
not an ordinary restriction-stability claim.

Use slope stability and dual stability, Huybrechts, *Lectures on
K3 Surfaces*, author-hosted prepublication, [Chapter 9, Section 3.1,
pp. 175--176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175),
and K3 RR and Serre duality, [Chapter 1, (2.5)--(2.6) and
Proposition 2.4, pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11).
A nonzero section injects O_S into E_y and contradicts strict
stability of this slope-zero rank-two bundle. Thus H^0(E_y)=0.
The dual is stable of slope zero, so H^0(E_y^*)=0; K_S=O_S
and Serre duality give H^2(E_y)=0. Surface RR gives
chi(E_y)=4-7=-3. Therefore every closed fibre has

\[
(h^0,h^1,h^2)(E_y)=(0,3,0).                            \tag{6}
\]

Cohomology above degree two vanishes on a surface. In particular
(6) is odd IT on every parameter, without an opposite-fibre assumption.

**Actual base change and compatible preservation.** Serre GAGA
algebraizes F on projective X and compares fibre cohomology.
The projection pi is smooth projective, flat and of finite
presentation. Apply [Stacks Lemma 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
with perfect object O_X and bounded finitely presented base-flat
complex F[0], whose support is proper over S. It gives the perfect
complex K=Rpi_*F and arbitrary derived base change. Its derived
fibre at every closed y is R Gamma(S,E_y), as in (6).
Apply [Stacks Lemma 36.31.3, 0BDK](https://stacks.math.columbia.edu/tag/0BDK)
with degree one and rank three. The open locus on which K is a
rank-three locally free sheaf in that degree contains every closed
point. Its closed complement is empty, since a nonempty closed
subset of a finite-type complex variety has a closed point.
Hence G=H^1(K) is locally free of rank three, all other cohomology
sheaves vanish, and canonical truncation gives K=G[-1]. This proves
(3), including its negative alternating sign.

For any algebraic f:T->S, smoothness of pi and local freeness of F
identify the derived pullback with the actual pulled-back bundle F_T.
Local freeness of G then gives
R(pi_T)_*F_T=Lf^*K=f^*G[-1]. Thus G commutes with arbitrary
algebraic base change. Proper GAGA comparison identifies its
analytification with the actual holomorphic first higher direct image.

Import Bartocci--Bruzzo--Hernandez Ruiperez, *A hyperkahler Fourier
transform*, Differential Geometry and its Applications **8** (1998),
239--249, [Definition 2, Lemmas 1--2 and Theorem 3,
pp. 243--246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=5).
The theorem requires a compact hyperkähler source, compatible
complex-structure spheres, a hermitian quaternionic-instanton kernel,
a source instanton and IT. Use source and target S with these
identical metrics, kernel F with L071's actual connection, and
the source line O_S with its flat hermitian connection. Equation
(6) verifies precisely its odd IT condition. The cited lemmas and
descent argument identify the resulting connection with the actual
holomorphic higher images. Here their sum is exactly G. The theorem
has no positive-mixed-scalar or target-rank restriction and requires
neither irreducibility of G nor an equivalence kernel. Import the
published theorem and its identification without reproof.

Its compatible connection on G has invariant endomorphism-valued
surface curvature. Verbitsky, *Hyperholomorphic connections on
coherent sheaves and stability*, [arXiv:math/0107182v10,
Proposition 3.7 and Lemma 3.8, pp. 12--13](https://arxiv.org/pdf/math/0107182v10#page=12),
give zero Kähler contraction coefficientwise. Thus i Lambda_h R_G=0.
Tracing and the surface wedge/contraction identity give degree_h(G)=0.
The real-metric Hermite--Einstein/polystability correspondence,
Huybrechts, [Chapter 9, Theorem 4.9, p. 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182),
gives slope-zero polystability at the same h, allowing reducibility.
The negative K-class in (3) does not negate G's hermitian connection.

**Full signed relative GRR.** Put t=b+4. L071's rank-two identities
give ch_3(F)=0 and ch_4(F)=ch_2(F)^2/12. Factor degrees give
e_i^2=e_i tau_D=0 and e_1e_2=P. Keeping the full 156P mixed
square, including its 120P transcendental part, yields

\[
\operatorname{ch}_2(F)^2=(-14t+156)P,\qquad
\operatorname{ch}(F)=2-7e_1+t e_2-\tau_D+
                       \frac{78-7t}{6}P.               \tag{7}
\]

The higher character is forced by actual rank two and c_1=0;
it is not freely assigned or inherited from a virtual class.
The square is unchanged by mixed-sign reversal, but this is
computed from the new F, not an application of an old sign's lemma.

Import Fulton, *Intersection Theory*, second edition (1998),
Theorem 15.2, pp. 286--287, and Example 15.2.8, pp. 291--292:
smooth relative GRR after applying the rational cycle-class map gives

\[
\operatorname{ch}(\pi_![F])=
\pi_*\bigl(\operatorname{ch}(F)\operatorname{td}(T_{X/S})\bigr).
                                                               \tag{8}
\]

Pi is proper smooth between nonsingular projective varieties, F
algebraizes, and its higher images are locally free by the preceding
argument. These also meet the displayed case of [Stacks 02UO](https://stacks.math.columbia.edu/tag/02UO);
Fulton is the proof citation, with the saved assessment's scan-host
qualification retained. Neither h's rationality nor a mixed-sign
condition is a GRR hypothesis. No reproof is needed.

Here td(T_{X/S})=1+2e_1, pi_*e_1=1 and pi_*P=eta.
The first-factor degree of tau_D is two, so pi_*tau_D=0;
also e_1 tau_D=0 by dimension. Only -7e_1+4e_1 and
((78-7t)/6+2t)P contribute. Thus

\[
\operatorname{ch}(\pi_![F])=-3+\frac{78+5t}{6}\eta.      \tag{9}
\]

There is no degree-six term before pushforward, hence no degree-two
first character afterwards. Negating (9) using (3) gives (4)
rationally. H^2(S,Z) is torsion-free, so rational vanishing of
c_1(G) upgrades to integral vanishing. For this K3 input see
Huybrechts, [Chapter 1, Section 3.2, (3.1) and its torsion-freeness
discussion, p. 15](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=15).
With c_1(G)=0, ch_2(G)=-c_2(G), proving (4). This first-class
check precedes the discriminant specialization.

**The whole integer domain and the real-metric inequality.**
Modulo 12, -7=5 and 5 is its own inverse. Hence (1) gives
t=6 modulo 12, or b=2 modulo 12. Together with b<=-9 this
is exactly b=-10-12j, j>=0. Equation (4) then gives the integral
charge 8-10j on the entire infinite domain, without sampling.

Import Perego, *Kobayashi-Hitchin correspondence for twisted vector
bundles*, [arXiv:1910.01867v1, Corollary 6.42, p. 118](https://arxiv.org/pdf/1910.01867v1#page=118),
with trivial twisting and zero auxiliary B-field. For a semistable
rank-r holomorphic bundle on a compact Kähler n-fold it states

\[
\int ((r-1)c_1^2-2r c_2)\wedge\sigma_g^{n-2}\leq0.       \tag{10}
\]

Definition 4.7, p. 59 tests slope with the real Kähler form;
Definition 4.20, p. 65 includes semistability in polystability.
Thus the established polystable G meets the hypotheses at its
actual h without a rational approximation or stability assumption.
On the target K3, n=2, r=3 and integral c_1(G)=0, so (10)
is -6 integral_S c_2(G)<=0, exactly (5).

Since j is a nonnegative integer, 8-10j>=0 holds exactly for j=0.
The standard discriminant number
integral_S(6c_2(G)-2c_1(G)^2) is 48-60j: it is 48 at b=-10,
-12 at the first excluded b=-22, and strictly decreases thereafter.
There is no integral equality case. This is an infinite-domain
exclusion, not a finite numerical certificate or existence test.

**Independent index sign check and limit of the conclusion.**
Using td(X)=1+2(e_1+e_2)+4P, absolute HRR on (7) gives

\[
\chi(X,F)=8+2(-7+t)+\frac{78-7t}{6}
          =\frac{42+5t}{6}=2-10j.                      \tag{11}
\]

Surface RR on (4) gives chi(S,G)=6-(8-10j)=-2+10j,
the negative of (11), as required by (3). These independent
Todd calculations check the rank, fractional coefficient and
alternating sign. The congruence and inequalities are exact;
no mathematical script or finite enumeration is necessary.

All applicability obligations succeed and the filter removes every
j>=1 input. Its surviving j=0 input has a positive discriminant;
this inequality alone cannot decide it. The approved directional
Bogomolov filter is exhausted. A stronger or different test requires
its own assessment. L060 and L073 are method/source comparisons,
not changed-charge mathematical premises; no positive-tensor
curvature exclusion, opposite projection, stable-image argument
or inverse has been imported. Other larger charges, the flat
(-10,-17) input, product-kernel existence, gluing, reconstruction,
transport and the main Hodge gap remain unresolved.

**Separate critical audit, 2026-10-10.** This audit reuses the approved
SPECIALIZE coverage and the precise primary citations above. It checks
their local application, not their general proofs. No substantive error,
additional exclusion or existence conclusion was found. The result is
REPRODUCTION with an EXPLORATION outcome, rather than a new advance.

First, the connection input really comes from the changed-sign F.
L071 excludes its two-line polystable alternative using the nonzero
action on the holomorphic two-form. The full operator -D, not only
its transcendental restriction, commutes with simultaneous quaternionic
rotation: it is scalar on the positive three-plane and preserves the
trivial orthogonal summand. Thus the cited stable connection criterion
applies to the actual invariant Chern classes. Each factor embedding
is quaternionic-equivariant, so the restricted curvature remains
invariant coefficientwise and has zero contraction on that K3. This
gives polystability on every fibre, not merely on a generic fibre or
from ambient zero contraction alone. Restricting (2) gives charge seven
independently of b. The two-line case would have charge 14r^2, hence
is impossible. Stability and dual stability kill H^0 and H^2, and
RR gives exactly three middle-cohomology dimensions on each fibre.
These checks use only L071 and the cited surface inputs; no statement
about the opposite projection or image stability enters.

For the algebraic passage, F[0] is a finitely presented complex flat
over the base because F is locally free and pi is flat; its support
is proper over S. Together with the perfect object O_X, this is the
Noetherian case of 0A1H. The resulting derived fibres are actual fibre
cohomology. The degree-one, rank-three locus supplied by 0BDK is open;
its complement is closed in a finite-type complex scheme and cannot
be nonempty without a closed point. Consequently the entire derived
pushforward is G[-1]. In the base-change square pi is flat, so there
is no extra derived fibre product; pulling back F and G gives ordinary
locally free sheaves. This checks arbitrary algebraic base change,
not just equality of fibre dimensions. Proper GAGA comparison then
identifies the analytic G used in the transform theorem.

For that theorem, the kernel is this actual F with its compatible
connection, and the source is the flat line on compact S. The fixed
identification of the two hyperkähler spheres is exactly the simultaneous
rotation used above. Equation (6) verifies odd IT at every parameter.
The published Definition 2, Lemmas 1--2 and Theorem 3 identify the
connection on the actual holomorphic higher images; since the only
nonzero image is G, no virtual subtraction is involved in preservation.
The theorem requires neither rank two for the image nor a positive
mixed scalar. Its invariant surface curvature has zero contraction,
so the real-metric correspondence gives slope-zero polystability of
G at h. Reducible G is allowed. The sign in pi_!F=-G affects GRR,
not this positive-rank bundle or its connection.

An independent degree-by-degree check can be written directly on the
whole admitted domain. Since 5 is invertible modulo 12, (1) is
equivalent to t=-6-12j, j>=0. Rank-two truncation with c_1=0 gives
ch_3=0 and ch_4=ch_2^2/12; it does not give ch_4=0. In the full
cup-product ring, e_1^2=e_2^2=e_i tau_D=0 and tau_D^2=156P.
Therefore the character on this domain is exactly

\[
\operatorname{ch}(F)=2-7e_1-(6+12j)e_2-\tau_D
                       +(20+14j)P.
\]

Multiplication by the relative Todd class 1+2e_1 produces first-factor
top degree -3e_1 and top-product degree (8-10j)P. All remaining terms
have insufficient first-factor degree to push forward. In particular
there is no degree-six term that could give c_1(G). Thus

\[
\operatorname{ch}(\pi_!F)=-3+(8-10j)\eta,
\qquad \operatorname{ch}(G)=3-(8-10j)\eta.
\]

Torsion-freeness of H^2(S,Z) removes the possible integral first-class
ambiguity. With that established, the arbitrary-rank real-Kähler
inequality cited in (10) applies to the actual semistable rank-three
G and requires 48-60j>=0. It passes exactly j=0, fails already at
j=1 with discriminant -12, and strictly decreases thereafter; there
is no integral equality case. This is a proof over all admitted
integers, not an extrapolation from a finite check. Absolute HRR
independently yields

\[
8+2(-13-12j)+(20+14j)=2-10j
   =-\bigl(6-(8-10j)\bigr)=-\chi(S,G),
\]

which checks the alternating sign without replacing the actual-image
argument. No mathematical script is needed for these exact identities.

This audit confirms only the necessary directional filter. At j=0 its
discriminant is 48, so neither equality-case rigidity nor existence
follows. The exhausted inequality route is retained; testing the
remaining input by another mechanism requires separate coverage.
No new direct mathematical input or DAG edge is introduced.

## Mathlib

Full matching coverage of this changed-sign filter and supporting
preservation, perfect base change, relative GRR and real-metric
Bogomolov results: **not checked**. Unknown availability is not
absence. L071 supplies the full integral signed character, actual
connection and exact-metric factor input; the precise primary
citations above supply the general theorems. This is a conditional
REPRODUCTION under the prior SPECIALIZE assessment, not progress
beyond the checked general results or a complete Hodge solution.
