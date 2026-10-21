# L076 — Factor exchange excludes the changed-sign pair (-10,-9)

## Hypotheses

Retain L071's marked smooth projective complex K3 surface S and its
real Kähler class h, with the identical hyperkähler metric on both
factors of X=S x S. Write Omega=p_1^*h+p_2^*h,
e_1=eta tensor 1 and e_2=1 tensor eta, where integral_S eta=1.
Retain L071's full integral mixed class tau_D in
H^2(S,Q) tensor H^2(S,Q), including its divisor and transcendental
components, with q-self-adjoint correspondence operator D on the
full H^2(S,Q). The convention is

\[
\Theta(x\otimes y)(v)=q(v,x)y,
\qquad q(v,w)=\int_S v\smile w,\qquad \Theta(\tau_D)=D.
\]

Suppose F is locally free of rank two on X, holomorphic and
slope-polystable at the actual real class Omega, with integral
c_1(F)=0 and

\[
\operatorname{ch}_2(F)=-6e_1-5e_2-\tau_D.
\tag{1}
\]

This is precisely L071's pair (a,b)=(-10,-9). Initial higher
characters and K-class are unrestricted. Use the separately audited
exclusion L072 with its exact changed-sign hypotheses. No existence,
opposite-fibre stability, inverse transform or transport is assumed.

## Conclusion

No such F exists. Factor exchange changes its correction pair to
(-9,-10) while retaining the full mixed tensor and every hypothesis
of L072. This is a REPRODUCTION application under the prior SPECIALIZE
assessment, and a new local exclusion of a residual bundle candidate,
not progress beyond the general functorialities and slice exclusion
checked. It constructs no cycle or transverse surface and does not
disprove the rational Hodge conjecture. The flat b=-17 input in the
a=-10 slice and other larger-charge inputs remain unresolved here.
The separate critical audit below preserves this exclusion; it finds
no substantive defect or stronger conclusion.

## Proof

Let s:X->X be the holomorphic algebraic isomorphism s(x,y)=(y,x).
It is its own inverse. Identical marked factors give
s^*e_1=e_2, s^*e_2=e_1 and s^*Omega=Omega. Identical factor metrics
also make it an isometry of the retained product metric.

**Transpose the entire mixed tensor.** Import naturality and graded
commutativity of the cup product from Hatcher, *Algebraic Topology*
(Cambridge, 2002), Proposition 3.10 and Theorem 3.11, printed
pp. 210--212, and the cross-product definition on p. 214
([author-hosted text](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf#page=219)).
With x tensor y=p_1^*x cup p_2^*y and deg(x)=deg(y)=2, these give

\[
s^*(x\otimes y)=p_2^*x\smile p_1^*y
 =(-1)^{2\cdot2}p_1^*y\smile p_2^*x=y\otimes x.
\tag{2}
\]

Put V=H^2(S,Q). Poincaré duality makes the symmetric pairing q
nondegenerate, so V tensor V -> End_Q(V), Theta as above, is an
isomorphism: it is the identification V->V^* by q followed by
V^* tensor V -> End(V). If t=sum x_i tensor y_i, then for v,w in V

\[
\begin{aligned}
q(\Theta(t)v,w)&=\sum_i q(v,x_i)q(y_i,w),\\
q(v,\Theta(s^*t)w)&=\sum_i q(w,y_i)q(v,x_i).
\end{aligned}
\]

The expressions agree since q is symmetric. Hence
Theta(s^*t)=Theta(t)^dagger, the q-adjoint. L071 supplies
D^dagger=D on the full V. Injectivity of Theta therefore proves
s^*tau_D=tau_D in rational cohomology. This verifies the entire
tensor, including its divisor block; equality just on T would not
suffice. It holds integrally as well: the integral cohomology of
a K3 is torsion-free, and the integral Künneth theorem makes
H^4(S x S,Z) torsion-free, so equality of these integral classes
after rationalization is equality before rationalization. No
integral NS/T splitting is used.

**Pull back the actual bundle and its Chern data.** Put F'=s^*F.
Isomorphism pullback and its inverse preserve holomorphic locally
free sheaves and rank; see [Stacks Lemma 17.14.3, Tag 01C8](https://stacks.math.columbia.edu/tag/01C8).
For Chern classes use [Stacks Section 42.38, Lemma 42.38.7 and
Definition 42.38.8, Tag 02U4](https://stacks.math.columbia.edu/tag/02U4):
Chern operations are bivariant classes defined through finite locally
free pullback. The algebraic isomorphism is flat of relative dimension
zero, X is smooth projective over C, and F is finite locally free
(by GAGA). Thus the Chern operations commute with this pullback,
and the cycle-class map respects it. This formulation avoids the
repeated symbol for rank and relative dimension in the displayed
statement of Lemma 42.38.5; no equality of those integers is required.
Integral topological first Chern naturality gives
c_1(F')=s^*c_1(F)=0 in integral cohomology. The rational character
polynomials, [Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM),
give ch_2(F')=s^*ch_2(F). Consequently (1)--(2) yield

\[
\operatorname{ch}_2(F')=-5e_1-6e_2-\tau_D.
\tag{3}
\]

No old higher character is imposed on F': L072 leaves these data
initially unrestricted, just as the present hypotheses do.

**Match every real-slope stability test.** For a torsion-free
coherent sheaf E of positive rank on the fourfold X use

\[
\mu_\Omega(E)=\frac{1}{\operatorname{rk}E}
             \int_X c_1(E)\smile\Omega^3.
\]

A common positive factorial in the degree convention changes no
inequality. Isomorphism pullback is an exact equivalence on coherent
sheaves and preserves torsion-freeness and determinants (defined by
the double dual of the top exterior power). Thus it gives a bijection
between subsheaves of E and of s^*E, with inverse s^*. Ranks agree.
The holomorphic isomorphism preserves the complex orientation; its
topological degree is one. Naturality and s^*Omega=Omega imply

\[
\int_X c_1(s^*E)\smile\Omega^3
 =\int_X s^*(c_1(E)\smile\Omega^3)
 =\int_X c_1(E)\smile\Omega^3.
\tag{4}
\]

Hence all slopes, and every strict inequality for proper positive-rank
subsheaves of smaller rank, agree under this equivalence. In particular
every stable summand of a polystable decomposition remains stable,
and the equality of the summands' slopes is preserved. Pullback
preserves their direct sum, so F' is slope-polystable at Omega.
This is a direct isomorphism application, with no general pullback
or restriction-stability assertion and no replacement of h by a
rational polarization.

**Apply the audited slice exclusion.** In (3) the coefficient of
e_1 is -5 and the other coefficient is b'+4=-6, hence b'=-10.
The complete domain requirements of L072 are satisfied:

\[
b'=-10\leq-9,\qquad -5(b'+4)=30\equiv6\pmod{12}.
\]

F' is an actual rank-two locally free holomorphic bundle with integral
c_1=0 and the same fixed tensor, marked metric and real product
polystability as in L072. That audited lemma excludes it. For this
specific input its forced actual line character would be
1-6eta with zero first character, contradicting the line character
identity. We import that conclusion rather than repeat its GRR or
base-change proof. Thus F' cannot exist; since s is an isomorphism,
neither can F. All identities and bounds above are exact; no numerical
or script check is required.

**Separate critical audit, 2026-10-09.** This is one REPRODUCTION
audit under the unchanged prior SPECIALIZE assessment. Its outcome
is EXPLORATION: the exclusion survives, with no substantive error,
new excluded pair or stronger conclusion found. The Chern citation
above is clarified using the already assessed bivariant formulation;
the argument and direct mathematical inputs are unchanged.

For an independent full-space transpose check, choose any rational
basis of V, let Q be its symmetric invertible cup matrix, and write
T=(t_ij) for the coefficient matrix of tau_D in that tensor basis.
The convention in the hypotheses gives D=T^t Q. Interchanging the
factors replaces T by T^t, so the resulting operator is TQ.
The q-adjoint of D is Q^(-1)D^t Q=TQ as well. Self-adjointness
therefore identifies the exchanged operator with D, and invertibility
of Q identifies the tensors. This works for the indefinite full
cup form; it requires neither an orthonormal basis nor an integral
splitting into divisors and transcendental classes. The tensor factors
have degree two, so graded commutativity gives sign +1. No complex
conjugation occurs: the flip is holomorphic, not antiholomorphic.

The equality just proved is initially rational. A K3 has integral
cohomology Z in degrees zero and four, a free group in degree two,
and zero odd cohomology. Integral Künneth thus writes H^4(X,Z) as
the direct sum of its two pure point factors and the free tensor
product H^2(S,Z) tensor H^2(S,Z), with no Tor term. Its map to
rational cohomology is injective. L071 supplies an actual integral
tau_D, so the flip fixes that integral class too. The separate first
Chern assertion needs no rational-to-integral inference: naturality
of integral Chern classes gives c_1(s^*F)=s^*0=0 directly. The cited
GAGA and bivariant Chern inputs apply to the actual bundle and
algebraic isomorphism, and character naturality follows over Q.
The resulting lower character is precisely (3), with the same
retained tensor and unrestricted initial higher characters.

For the all-subsheaf check, transport E and any injection A->E by
the exact inverse equivalences s^* and s^*. They preserve coherence,
torsion-freeness, generic ranks and properness of subsheaves; they
also preserve saturated subsheaves if that convention is used.
Exterior powers, duals and double duals commute with an isomorphism,
so the determinant of a positive-rank torsion-free A and its integral
first Chern class pull back correctly, even when A is not locally
free. Both factors carry exactly h, hence s^*Omega=Omega in real
cohomology. The flip has degree +1 on X: it is a holomorphic
isomorphism, also consistent with the real product sign (-1)^(4*4).
Equation (4) therefore applies to every such A, with no rationality
requirement on h. After division by its preserved positive rank,
each slope and each comparison with E is identical. Applying this
to each stable summand of F preserves stability and their common
slope zero. Their direct sum pulls back to F', proving the required
polystability. This uses no assertion about stability on a fibre.

Finally match the entire destination, not just the correction pair.
The surface, marking, identical hyperkähler metrics, real h and Omega,
full integral self-adjoint tensor (including its square 156P), rank
two, actual holomorphic local freeness, integral c_1=0 and product
polystability are unchanged. The pure coefficients become -5 and -6,
so L072 has a'=-9 and b'=-10. Its integer bound and congruence are
-10<=-9 and -5(-10+4)=30=6 modulo 12. No higher-character or K-class
condition has been added. Audited L072 then gives an actual line G
with rational c_1(G)=0 and ch_2(G)=-(7(-10)+106)eta/6=-6eta.
The line identity gives ch_2(G)=c_1(G)^2/2=0, while eta is nonzero
by its integral one. This is an exact contradiction. Opposite-fibre
stability, a transform inverse, determinant trivialization of G and
global existence are unnecessary. No separate GRR reproof is needed.

The direct inputs remain exactly L071 and L072. This verification
does not enlarge the exclusion or resolve the flat (-10,-17) pair,
larger charges, kernel existence, reconstruction or transport. It
does not change the universal primitive Hodge-class algebraicity gap.

## Mathlib

Full matching factor-exchange application and supporting functoriality
coverage: **not checked**. No declaration match or absence is asserted.
The primary cup/Chern pullback citations and named Poincaré duality,
integral Künneth and GAGA inputs support the application; L071 and
audited L072 supply its notebook-specific data and exclusion. The
general results are imported, with only the essential tensor and
real-slope specializations proved here.
