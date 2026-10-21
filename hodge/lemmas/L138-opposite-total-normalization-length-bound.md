# L138 — Fixed-parameter upper bound for the opposite normalization length

## Hypotheses

Retain L071/L118's identical marked smooth projective complex K3
surfaces B=S_1 and Y=S_2, the common hyperkähler metric and real
product polarization Omega, and the full integral self-adjoint mixed
tensor tau_D. Suppose F on B x Y is holomorphic locally free of
rank two, Omega-slope-polystable, with integral c_1(F)=0 and

\[
                 \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D,
\]

where e_1=eta tensor 1, e_2=1 tensor eta and integral_S eta=1.
Use L118's fixed charge-21 polarization H and actual all-stable
classifying map. Let Z be its original integral reduced image.
L120 identifies the finite birational unramified normalization as
nu:B -> Z. L121 supplies its finite reduced off-diagonal coincidence
scheme, possibly empty.

Use exactly L137's fixed projective embedding j:Z -> P^N, obtained
by restricting the embedding of the fixed projective moduli space.
Write L=O_Z(1) and

\[
 \delta=\deg j(Z)=4k^2\ell^2q(D(H),D(H)),\qquad
 T=\frac{\delta(\delta+1)}2,\qquad c=N-2.
\]

The positive integers ell,k and the integer N are fixed from the
surface/moduli data before choosing F or Z; no numerical values
are assumed. No normality, Cohen--Macaulayness, projective normality,
untwisted coherent vanishing, nonempty collision locus or existence
of F is assumed.

## Conclusion

The coherent normalization quotient

\[
           Q=\nu_*O_B/O_Z
\]

has finite support, contained in the finite set of multiple-fibre
values. Its total algebraic length Lambda is finite and satisfies

\[
 \boxed{\quad
 0\leq\Lambda=2-\chi(Z,O_Z)
 \leq 2+\frac\delta2+
       \frac32\delta^{N-2}
                \left(\frac{\delta(\delta+1)}2\right)^4.
 \quad}                                                       \tag{1}
\]

Every parameter on the right is independent of F and of the unknown
normalization defect, with fixed auxiliary choices as in L137.
The bound is potentially ineffective because ell,k,N have not been
numerically specified. Empty collisions and Q=0 are allowed. This is
a conditional ADVANCE / REPRODUCTION of known tools; the separate
critical audit below preserves it. It is not a new general coefficient theorem
or progress beyond the checked sources. It supplies neither a useful
contradictory lower bound, F, collision existence, a cycle nor transport.
Universal primitive rational Hodge realization remains unresolved.

## Proof

**Approved scope and sources.** The pre-invocation SPECIALIZE gate is
`drafts/literature/2026-10-20-opposite-total-defect-bound-specialization.md`.
Reuse its completed bridge and projective-degree assessments.
The direct local mathematical inputs used here are L120, L121 and
audited L137; L071/L118's hypotheses are retained through them.
No different family, embedding, projection or tensor is introduced.

Import [Stacks, Lemma 41.7.3 (04DG)](https://stacks.math.columbia.edu/tag/04DG)
for a finite unramified map with a singleton fibre and a purely
inseparable residue extension. It gives a closed immersion over
a neighborhood of that target point. For the polynomial comparison
import [Lemma 30.14.3 (0AG7)](https://stacks.math.columbia.edu/tag/0AG7)
(eventual graded-piece/global-section comparison),
[Lemma 30.14.1(4) (01YS)](https://stacks.math.columbia.edu/tag/01YS)
(eventual higher-cohomology vanishing), and
[Lemma 33.35.14 (08AC)](https://stacks.math.columbia.edu/tag/08AC)
(Euler polynomial for all integral twists). For Euler additivity,
finite-support cohomology and affine pushforward use respectively
[Lemma 33.33.2 (08AA)](https://stacks.math.columbia.edu/tag/08AA),
[Lemma 33.33.3 (0AYT)](https://stacks.math.columbia.edu/tag/0AYT), and
[Lemma 30.2.4 (089W)](https://stacks.math.columbia.edu/tag/089W).
Their precise statements and relevant proofs are covered by the
saved assessment. They require none of the omitted singularity
or cohomology assumptions above; these general results are not reproved.

For regularity and coefficients use Le Tuan Hoa,
[*Finiteness of Hilbert functions and bounds for Castelnuovo--Mumford
regularity of initial ideals*, arXiv:math/0608118v1 (4 August 2006),
Theorems 0.2 and 4.1, printed pp. 2 and 15--16](https://arxiv.org/pdf/math/0608118v1).
The saved assessment includes the relevant proof cases. The two
statements and the dimension/coordinate conventions were checked
again for this substitution, without new theorem discovery.
For a reduced homogeneous quotient S=R/I of dimension d>=2,
with e=deg S and a=adeg S, Theorem 0.2 gives

\[
       \operatorname{reg} I\leq
            \left(\frac{e(e-1)}2+a\right)^{2^{d-2}}.             \tag{2}
\]

Over an infinite field Theorem 4.1 gives, with c=n-d and the
binomial-basis coefficients epsilon_i of S,

\[
 |\epsilon_1|\leq a^c\operatorname{reg}I,\qquad
 |\epsilon_i|\leq\tfrac32a^c(\operatorname{reg}I)^i\quad(i\geq2).
                                                                    \tag{3}
\]

Its intermediate saturated sections are taken in generic linear
coordinates. One may choose those coordinates over C; the final
quantities in (2)--(3) are unchanged by that linear automorphism.
This does not replace the embedding or remove its possible linear
equations. We use ideal regularity, not ring regularity, in both
inequalities. The notation epsilon_i distinguishes Hoa's coefficients
from the factor-point classes e_1,e_2 in the hypotheses.

**Finite support on the actual image.** Since Z -> M is a closed
immersion, B x_Z B equals B x_M B. Let C be the set-theoretic image
in Z of L121's off-diagonal scheme under either value map. It is a
finite closed set of complex points: that scheme is finite over C.
Every closed multiple-fibre value belongs to C, since any two distinct
preimages give an off-diagonal point. Surjectivity and finiteness of
nu imply that a closed z outside C has exactly one point in its
fibre. Both residue fields are C. L120 makes nu itself finite and
unramified, so 04DG applies, giving a neighborhood U of z on which
nu^{-1}(U) -> U is a closed immersion.

The defining normalization map O_Z -> nu_*O_B is injective because
Z is integral and nu is finite birational. On U it is also surjective
by the closed immersion just obtained. Thus it is an isomorphism
there and Q|_U=0. The quotient Q is coherent, since nu is finite
and Z noetherian, so its support is closed. If Supp(Q) outside C
were nonempty, its intersection with the finite-type open Z\C
would contain a closed complex point, by the Jacobson property.
Such a point is closed in Z and is one of the singleton values
already excluded. Consequently Supp(Q) is contained in C.
This argument retains the full coherent quotient, not just the
set-theoretic or reduced normalization defect.

By 0AYT, Q has no higher cohomology and its Euler characteristic
is the sum of the local lengths, since every residue field is C.
This is Lambda; it counts module length, not just support points.
The finite affine map nu and 089W identify
chi(Z,nu_*O_B)=chi(B,O_B)=2, the standard K3 value. Euler
additivity in

\[
       0\longrightarrow O_Z\longrightarrow\nu_*O_B
                      \longrightarrow Q\longrightarrow0          \tag{4}
\]

now gives Lambda=2-chi(Z,O_Z), with no assumption on H^1(Z,O_Z).

**Coordinate and Euler polynomials.** Let
R=C[x_0,...,x_N], let I be the saturated homogeneous prime ideal
of j(Z), and put S=R/I. As established in L137, S is a domain,
dim S=3, n=N+1, c=N-2 and deg S=adeg S=delta. In particular
S is reduced. The ideal I is nonzero: otherwise Z=P^N, and its
dimension forces N=2; its normalization would be P^2 rather than
the K3 surface B of L120 (their h^2(O) are 0 and 1). Thus no
zero-ideal regularity convention is needed. Also I is proper and
N>=3. Linear forms in I are permitted throughout.

The finite graded R-module S sheafifies to j_*O_Z. The comparison
0AG7 gives S_m=H^0(Z,L^m) for all sufficiently large m. Eventual
vanishing 01YS then identifies this dimension with chi(Z,L^m)
for sufficiently large m. By 08AC the latter is a polynomial in
m for all integral m. It therefore agrees identically with the
coordinate Hilbert polynomial P_S, not merely at large values.
With Hoa's precise binomial convention and d=3, this polynomial is

\[
      P_S(m)=\delta\binom{m+2}{2}-\epsilon_1(m+1)+\epsilon_2.
                                                                    \tag{5}
\]

In particular chi(Z,O_Z)=P_S(0)=delta-epsilon_1+epsilon_2.
Neither the last binomial coefficient epsilon_2 alone nor the
small-degree Hilbert function S_0 gives this Euler constant. Equation
(4) consequently gives the exact identity

\[
                    \Lambda=2-\delta+\epsilon_1-\epsilon_2.       \tag{6}
\]

**Fixed-parameter substitution.** Apply (2) with d=3 and e=a=delta.
It yields reg I<=T^2, because
delta(delta-1)/2+delta=T. Equation (3) gives

\[
       |\epsilon_1|\leq\delta^cT^2,\qquad
       |\epsilon_2|\leq\tfrac32\delta^cT^4.                    \tag{7}
\]

Already (6)--(7) give the valid coarse estimate

\[
       \Lambda\leq2-\delta+
                         \delta^c(T^2+\tfrac32T^4).             \tag{8}
\]

We can retain more of the same input without any additional theorem.
L137's already-established K3 HRR polynomial is
chi(B,(nu^*L)^m)=2+(delta/2)m^2. Tensoring (4) by L^m,
the finite projection formula and 089W identify its middle Euler
characteristic with this expression. By 0AYT the finite-support
sheaf Q tensor L^m has Euler characteristic Lambda for every m:
an invertible twist does not change any local length. Hence

\[
                    P_S(m)=\frac\delta2m^2+2-\Lambda.           \tag{9}
\]

Expanding (5) gives linear coefficient 3delta/2-epsilon_1.
Comparison with (9) forces epsilon_1=3delta/2 and then
Lambda=2+delta/2-epsilon_2. Applying the second inequality of
(7) proves (1). In this specialization delta is at least eight:
L137's integral ample D(H) has positive even square on the K3
lattice, and k,ell are positive. Thus (1) is indeed no larger
than (8), since delta^cT^2>=3delta/2. No sharpness is claimed.
These are exact symbolic inequalities; no numerical script or
finite sampling is part of the proof.

The right-hand side depends only on L137's fixed choices and
intersection form. Its existence does not depend on a Hilbert
constant, Q, unknown fibre sizes or any vanishing on the singular
image. This meets the intermediate fixed-parameter threshold,
while giving no lower bound that would exceed it. ATTEMPTS/070's
minimal-defect failure, ATTEMPTS/073's failed automatic vanishing,
ATTEMPTS/078's uncontrolled middle Hom Euler term and the parked
order-five route remain untouched. F existence, collision counts,
a useful global comparison, transport and the universal Hodge
target are independent unresolved requirements. The new local
bound is preserved by the separate critical review below.

**Separate critical audit, 2026-10-20 (step 431).** The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-20-opposite-total-length-critical-audit.md`.
The completed task is proof_audit, classified EXPLORATION /
REPRODUCTION: no substantive error, stronger bound or existence
conclusion was found. A stray typographical plus sign above was
removed; this is not a mathematical repair. The direct inputs remain
L120, L121 and audited L137, with all their conditional hypotheses.
Their conclusions and the relevant fixed-parameter and HRR passages
were checked; this audit does not reprove their upstream results.

At a closed value outside the finite image of L121's off-diagonal
scheme, surjectivity gives a nonempty fibre and absence of an
off-diagonal pair makes it a singleton. Both residue fields are C.
The map to which 04DG applies is the finite unramified nu:B -> Z,
not merely its composite into the moduli space. The theorem's
neighborhood closed immersion gives surjectivity on structure
sheaves; finite birationality onto the integral image gives the
independent injection. Hence Q vanishes on that neighborhood.
The support of a coherent Q is closed. A nonempty part outside the
finite collision image would contain a closed complex point of the
finite-type open complement, also closed in Z, contradicting this
vanishing. Thus the entire module Q has zero-dimensional support.
No reduction of Q or identification of its length with its number
of support points enters. The singleton theorem and its complete
finite-module/Nakayama proof were rechecked directly at Stacks 04DG;
the remaining bridge-source coverage is reused unchanged.

Finite pushforward identifies all cohomology of O_B with that of
nu_*O_B. Additivity therefore gives exactly 2=chi(O_Z)+Lambda.
For every integer m, tensoring (4) by L^m remains exact; each local
length of Q is unchanged by this invertible twist. Finite projection
and L137's full K3 HRR formula yield (9), including its zero linear
coefficient and constant 2-Lambda. The eventual graded-piece and
Serre-vanishing statements are used only to identify two polynomials.
Evaluation at zero then concerns the Euler polynomial, not S_0.
Expansion of the complete binomial expression (5) gives
delta*m^2/2+(3delta/2-epsilon_1)*m+
delta-epsilon_1+epsilon_2. Thus both epsilon_1=3delta/2 and
Lambda=2+delta/2-epsilon_2 have the stated signs and factors.
No untwisted cohomology vanishing on Z is required.

Hoa's v1 Theorems 0.2 and 4.1 and the latter's full dimension-three
top-coefficient proof case on printed pp. 15--16 were rechecked
directly against the cited primary PDF. The reduced domain S has
ring dimension three and arithmetic degree delta, with its original
presentation in N+1 variables. The generic-coordinate qualification
in Theorem 4.1 allows a coordinate automorphism over C and does not
require removing linear equations. The homogeneous prime ideal
cannot be zero: that would force Z=P^2 and contradict its K3
normalization. Thus ideal regularity is well defined here, and
N>=3. Theorem 0.2 has exponent 2^(d-2)=2, so reg I<=T^2.
The coefficient estimate uses (reg I)^2, giving T^4, with factor
3/2 and exponent c=N-2 exactly as in (7). The top-coefficient
case includes the odd ring dimension d=3; no Cohen--Macaulay
hypothesis is added. This recheck validates the cited substitution,
not a reproof or improvement of Hoa's theorem.

L137 fixes H from the fixed-invariant wall stratum, then ell, k
and the complete section space defining N on the fixed projective
moduli space, before F or its image is chosen. Its restriction
embedding is of the original image and its finite pullback has
class 2k*ell*D(H). Consequently delta and every parameter in (1)
are independent of Q, its Hilbert constant and unknown fibre sizes.
The integral ample class D(H) has positive even square, giving
delta>=8; this also checks the comparison of (1) with the coarser
(8). These remain symbolic fixed choices, not numerical estimates.

The bounded audit test passes. The conclusion is still only the
conditional upper bound (1). In particular, an empty collision
locus is permitted and no lower estimate contradicting (1) has
been established. ATTEMPTS/070, 073 and 078 are not bypassed by
assuming minimal local defect, coherent vanishing or a sign for
the middle Hom Euler characteristic. F existence, transport and
universal primitive Hodge realization remain unresolved.

## Mathlib

Full matching coverage for the finite-unramified singleton argument,
this normalization-length specialization and Hoa's coefficient
bounds is **not checked**. The precise general inputs are cited
above; unknown Mathlib availability is not evidence of absence.
This is a checkable informal specialization, not a Lean verification.
