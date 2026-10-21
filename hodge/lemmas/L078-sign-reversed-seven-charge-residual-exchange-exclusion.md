# L078 — Factor exchange excludes the changed-sign residual pair (-11,-10)

## Hypotheses

Retain L071's marked smooth projective complex K3 surface S, the real
Kähler class h and the identical hyperkähler metrics on X=S x S. Put
Omega=p_1^*h+p_2^*h, e_1=eta tensor 1 and e_2=1 tensor eta, with
integral_S eta=1. Retain its full integral mixed tensor tau_D and the
q-self-adjoint D on all V=H^2(S,Q), including the divisor block, where

\[
q(v,w)=\int_S v\smile w,\qquad
\Theta(x\otimes y)(v)=q(v,x)y,\qquad \Theta(\tau_D)=D.
\]

Suppose F is a locally free holomorphic rank-two bundle on X,
slope-polystable at the actual real class Omega, with

\[
c_1(F)=0\text{ in }H^2(X,\mathbf Z),\qquad
\operatorname{ch}_2(F)=-7e_1-6e_2-\tau_D.
\tag{1}
\]

This is the correction pair (a,b)=(-11,-10). Initial higher characters
and the initial K-class are unrestricted. Use audited L075's exclusion
and the general exchange identities proved and audited in L076; its
pair-specific nonexistence conclusion is not applied to a different pair.
No F existence, opposite-fibre stability, rank-three image stability,
inverse transform, reconstruction or transverse transport is assumed.

## Conclusion

No F satisfying (1) and these hypotheses exists. Exchanging the factors
produces the precise a'=-10,b'=-11 input excluded by L075.

This is a REPRODUCTION application of known functorialities and the
assessed duality exclusion, with outcome NEGATIVE: one residual numerical
candidate is eliminated. It gives no beyond-source originality claim,
algebraic cycle, surface, transport or Hodge-conjecture resolution.
The flat (-10,-17) case and other charges remain outside this conclusion.
The separate critical audit below preserves this exclusion without a
substantive repair or stronger conclusion.

## Proof

Let s:X->X be s(x,y)=(y,x) and put F'=s^*F. The identical marked
factors make s an algebraic holomorphic isomorphism and s^2=id.
They give s^*e_1=e_2, s^*e_2=e_1 and s^*Omega=Omega; the identical
factor metrics also make s an isometry of the fixed product metric.

**Fix the full integral tensor.** Reuse L076's full-space exchange
identity, justified by Hatcher, *Algebraic Topology* (Cambridge, 2002),
Proposition 3.10 and Theorem 3.11, printed pp. 210--212, and the
cross-product definition and graded products, pp. 214--216
([author-hosted text](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf#page=219)).
The factors here have cohomological degree two, so their flip sign is
(-1)^(2*2)=+1, and s^*(x tensor y)=y tensor x. For any t=sum x_i
tensor y_i, the convention in the hypotheses yields

\[
q(\Theta(t)v,w)=\sum_i q(v,x_i)q(y_i,w)
             =q(v,\Theta(s^*t)w).
\tag{2}
\]

Thus Theta(s^*t)=Theta(t)^dagger for the q-adjoint. Named Poincaré
duality makes q nondegenerate, hence Theta is an isomorphism. The
retained full-space D^dagger=D therefore gives s^*tau_D=tau_D
rationally, with no deletion of divisor terms or complex conjugation.
This is also integral: K3 integral cohomology is torsion-free and
concentrated in even degrees, and named integral Künneth makes
H^4(X,Z) the torsion-free sum of its two pure factors and the tensor
of the second cohomologies. Rationalization is injective on this
group. Both tau_D and its pullback are integral by L071, so their
rational equality proves their integral equality. No integral NS/T
splitting is needed. Equation (2) checks applicability of the imported
exchange mechanism rather than reproving cup naturality or duality.

**Transport the actual bundle and Chern classes.** Isomorphism pullback
preserves holomorphic local freeness and rank, as in
[Stacks Lemma 17.14.3, 01C8](https://stacks.math.columbia.edu/tag/01C8).
Integral topological first-Chern naturality gives c_1(F')=s^*0=0
integrally. For character naturality import the Chern operations in
[Stacks Section 42.38, Lemma 42.38.7 and Definition 42.38.8, 02U4](https://stacks.math.columbia.edu/tag/02U4)
and the rational character polynomials in
[Stacks Section 42.45, 02UM](https://stacks.math.columbia.edu/tag/02UM).
Their applicability is exactly as in L076: GAGA algebraizes the
actual finite locally free F on smooth projective X; s is an algebraic
isomorphism, flat of relative dimension zero, and the cycle-class map
respects its pullback. Consequently

\[
\operatorname{ch}_2(F')=s^*\operatorname{ch}_2(F)
                       =-6e_1-7e_2-\tau_D.
\tag{3}
\]

No higher-character constraint is introduced by this calculation.

**Preserve every real-slope test.** Reuse L076's isomorphism argument
on the actual Omega. Pullback by s and its inverse are exact inverse
equivalences on coherent sheaves, matching all coherent torsion-free
subsheaves A of a torsion-free E with the subsheaves s^*A of s^*E.
They preserve ranks, properness and saturation when used, and commute
with exterior powers and double duals. Thus determinant and integral
c_1 of each such A pull back correctly even when A is not locally free.
Since s is holomorphic it has degree +1 in the complex orientation.
For every positive-rank A, real cup-product naturality gives

\[
\begin{aligned}
\mu_\Omega(s^*A)
 &=\frac{1}{\operatorname{rk}A}
   \int_X s^*c_1(A)\smile\Omega^3\\
 &=\frac{1}{\operatorname{rk}A}
   \int_X s^*(c_1(A)\smile\Omega^3)
  =\mu_\Omega(A).
\end{aligned}
\tag{4}
\]

A common positive factorial in the degree convention is immaterial.
Apply (4) also to E: every strict slope inequality for a proper
subsheaf of smaller positive rank is equivalent under s^*.
Each stable summand of a polystable decomposition of F therefore
pulls back to a stable summand, and their common slope is preserved.
The pulled-back direct sum is F', so F' is slope-polystable at this
same Omega. This checks all subsheaves, not just factor restrictions;
no rational replacement of h or general restriction theorem is used.

**Match L075 in full.** The pure coefficients in (3) are a'+4=-6
and b'+4=-7, so (a',b')=(-10,-11). In particular

\[
b'=-11\leq-9,\qquad -6(b'+4)=42\equiv6\pmod{12}.
\tag{5}
\]

The marked S, full integral negative tensor, full q-self-adjoint D,
identical hyperkähler metrics, real h and Omega, rank two, actual
holomorphic local freeness, integral c_1=0 and product polystability
all agree with L075. That lemma leaves the initial higher characters
and K-class unrestricted. Its actual-image stability and perfect
symmetric pairing are established in its audited proof using L073
and L074; they are not extra assumptions here. Import its b=-11
nonexistence conclusion directly, without repeating duality, transform
preservation or GRR. It excludes F'. Since s is an isomorphism, the
assumed F would supply F', which is a contradiction.

All comparisons and the domain check (5) are exact. No numerical
certificate or mathematical script is needed. L077 only selects
this endpoint as the residual input of its directional filter; its
rank-three image is not used to obtain the present contradiction.

**Separate critical audit, 2026-10-10.** Under the prior SPECIALIZE
assessment, independently check the exchange and the entire destination
rather than reuse L076's pair-specific conclusion. This is REPRODUCTION
with outcome EXPLORATION: no substantive error, newly excluded pair or
stronger conclusion was found.

For a full-space check independent of the displayed bilinear identity,
choose an arbitrary rational basis of V, with symmetric invertible cup
matrix Q. If T=(t_ij) is the coefficient matrix of tau_D, the stated
Theta convention gives D=T^t Q. The exchanged tensor has matrix T^t
and operator TQ. Self-adjointness says

\[
D=Q^{-1}D^tQ=TQ.
\]

Consequently T^tQ=TQ, hence T^t=T. This uses the whole cup space,
including the divisor block, and works for the indefinite cup form.
No orthonormal basis, integral divisor/transcendental decomposition or
complex conjugation is involved. The cohomological factor degrees are
two, so the flip sign is positive. Integral Kunneth has no Tor term:
H^4(X,Z) is the sum of two copies of Z and the tensor of two free
H^2(S,Z) groups. Its rationalization is injective. Thus this rational
matrix verification proves equality of the actual integral tensors.

The isomorphism's pullback has an exact inverse. Given any coherent
torsion-free subsheaf B of s^*E, pulling back again supplies a subsheaf
s^*B of E, and pulling that inclusion back recovers B. This checks
surjectivity of the subsheaf correspondence as well as preservation
of injections. Generic ranks, properness, torsion-freeness and, if
required, saturation survive. Exterior powers and double duals commute
with this local-ring isomorphism, so determinant Chern classes do too.
The flip preserves the real Omega exactly, and has topological degree
+1 because it is holomorphic (also (-1)^(4*4)=+1 on the real product).
Equation (4) therefore compares every positive-rank torsion-free
subsheaf, even a singular one. All smaller-rank strict inequalities
and all stable summands of equal slope survive. This proves actual
product polystability, without any claim about restriction stability.
There is no hidden rationality requirement on h.

Integral c_1 vanishes directly by integral naturality, independently
of the rational character calculation. GAGA and the cited Chern
pullback apply to this finite locally free bundle and algebraic
isomorphism. Formula (3) has pure coefficients -6 and -7, so the
destination is a'=-10,b'=-11, with b'<=-9 and
(-6)(-7)=42=6 modulo 12. The negative full mixed tensor, marked S,
identical hyperkahler metrics, actual real polarization, rank,
holomorphic local freeness and integral first class all agree with
L075. Its hypotheses impose no extra initial higher-character or
K-class restriction. Swapping cannot introduce such a restriction.

The destination conclusion has been separately audited: L075 uses
L073's actual rank-two image and L074's charge six at b'=-11; six
is outside its split alternative 14r^2. Its proof establishes the
image's stability and trivial determinant before comparing the perfect
symmetric Serre pairing with alternating rank-two wedge by simplicity.
These are consequences of that imported exclusion, not extra
hypotheses that must be assumed for F'. No rank-three image from
L077 enters. Therefore the matched L075 conclusion excludes F',
and the inverse isomorphism excludes F. No duality or GRR reproof
is needed for this audit.

The direct mathematical inputs remain L071, L075 and L076. L077
only motivates the endpoint; combining its separately audited filter
with this exclusion adds no new statement in the present audit.
The flat (-10,-17) case, other charges, kernel construction,
reconstruction, transverse transport and universal primitive
Hodge-class algebraicity remain unresolved. No script or numerical
evidence is used in this exact verification.

## Mathlib

Full matching coverage of this residual exchange application and
supporting functorialities: **not checked**. Unknown availability is
not absence. The precise Hatcher/Stacks citations and named Poincaré
duality, integral Künneth and GAGA supply imported general tools.
L071 supplies the full data, L076 the audited exchange mechanism,
and L075 the destination exclusion. The necessary specialization is
the full tensor, integral Chern, all-subsheaf and destination matching
above. No new general theorem or complete Hodge solution is claimed.
