# L096 — Finite reducible-fibre locus of the hypothetical equality kernel

## Hypotheses

Retain L071's identical marked projective K3 surfaces S_1 and S_2,
the fixed hyperkähler metric g and real Kähler class h on each,
Omega=p_1^*h+p_2^*h, and the full integral self-adjoint tensor tau_D.
Its action on the metric's holomorphic two-form is 2lambda, where
1<lambda<5/4. The exact zero-slope divisor lattice is Z k,
k^2=-14. Let L be the holomorphic line bundle with c_1(L)=k.

Suppose F on X=S_1 x S_2 is locally free of rank two,
slope-polystable at Omega, with integral c_1(F)=0 and

\[
             \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D,
             \qquad e_1=\eta\otimes1,\quad e_2=1\otimes\eta.
\]

Use its actual compatible hyperholomorphic unitary connection from
L071. For y in S_2 write F_y=F|_{S_1 x {y}} and define
Z={y : F_y is not h-slope-stable}. Neither F nor a split parameter
is assumed to exist. No generic stability, smooth quotient, exact
quadratic normal form or integrated abstract tangent is a premise.

## Conclusion

Z is a finite set, possibly empty. Equivalently, the reducible
S_1-connection fibres occur at finitely many parameters. Each such
holomorphic fibre is L direct sum L^{-1}. The other fibres are stable.
This is a set-theoretic conclusion, with no assertion about a locus
scheme's multiplicities or reducedness.

This conditional ADVANCE / REPRODUCTION specializes the known slice,
inverse-function and cohomology theorems below. The separate critical
audit below preserves the conclusion. It supplies no kernel, mixed-action realization,
extension of a moduli map across Z, algebraic cycle or transport.
Equality/positive-Euler kernel existence and universal primitive Hodge
realization remain unresolved. It does not contradict L094's compatible
quaternionic line or assert that any such line integrates.

## Proof

**All split fibres belong to one determinant-fixed unitary orbit.**
L071 gives h-polystability of every F_y through the actual restricted
connection, integral c_1(F_y)=0 and charge c_2(F_y)=14. Its complete
rank-two alternatives are stable or M direct sum M^{-1}, with
c_1(M)=r k and charge 14r^2. Thus a nonstable fibre has r=+1 or -1.
Pic^0(S_1)=0 makes the first Chern class determine its holomorphic
line bundle; in particular the unordered pair is exactly {L,L^{-1}}.
There is no additional flat line twist. The two choices of r give
the same direct sum, not two connection types.

Integral c_1(F)=0 and Pic^0(X)=0 trivialize det F holomorphically.
Its induced determinant connection is flat with a global parallel
unitary frame, as proved in the L094/L095 audits. Fix this frame.
On each split fibre, polystable Hermite--Einstein uniqueness identifies
the restricted connection unitarily with the direct-sum connection A
on E=L direct sum L^{-1}, at this same metric. This is the same
uniqueness input used in L094, with no change of polarization. The
determinant of such an isometry, relative to the parallel determinant
frames, is a constant in U(1). Multiplying the isometry by a constant
unit scalar whose square is its inverse makes it determinant-preserving.
Consequently all split connections lie in the SU(2) gauge orbit of A.
Unordered factors do not create an exchanging component of A's
stabilizer: L094 proves that stabilizer is exactly U(1), since
L and L^{-1} are nonisomorphic. We need one orbit, not smoothly chosen
isometries at all split parameters.

**The actual slice coordinate isolates each split parameter.** Fix
y_0 in Z. On a contractible real parameter neighborhood U of y_0,
choose smooth unitary determinant-preserving identifications of the
bundles F_y with the central smooth bundle E; take the central
restricted connection to be A. Such local identifications can also
be obtained by parallel transport along the radial parameter paths
using F's actual determinant-one connection. They yield an actual
smooth family of ASD connections A_y, with A_{y_0}=A.

Import Tobias Diez and Gerd Rudolph, *Normal form of equivariant maps
in infinite dimensions*, Ann. Global Anal. Geom. **61** (2022),
159--213, DOI
[10.1007/s10455-021-09777-2](https://link.springer.com/article/10.1007/s10455-021-09777-2),
Theorem 5.3, Section 5.3 (5.14)--(5.23), Theorem 5.8, Definition B.1
SL2--SL3 and Proposition B.2. SU(2) is compact semisimple and S_1
is compact oriented of real dimension four, so the ASD specialization
applies, including at the reducible A. In a sufficiently high Sobolev
completion, take its sufficiently small Coulomb slice through A.
L094's audited actual-family gauge construction gives a smooth
choice g_y with g_{y_0}=1 such that B_y=g_y dot A_y lies in this
slice and d_A^*(B_y-A)=0. Here dot denotes the gauge action, not
a derivative. Restrict U so the choices remain in the slice tube.
The residual U(1) is retained.

The slice-intersection property SL2 has the following decisive use:
if B_y lies in the gauge orbit of A and in this slice, any gauge
transformation carrying A to B_y must belong to the stabilizer of A.
It therefore fixes A, so B_y=A. Indeed both A and its transform
are slice points, which is exactly the hypothesis of SL2. This
controls even gauges not chosen close to the identity. Hence

\[
                       y\in Z\cap U\quad\Longrightarrow\quad B_y=A.
\tag{1}
\]

Let V=ker d_A^* intersect ker d_A^+ be the finite-dimensional real
harmonic space of L094 and P_V its L2 orthogonal projection. Define
the genuine smooth, finite-dimensional coordinate
s(y)=P_V(B_y-A), with s(y_0)=0. For u in T_{y_0}S_2 put
b_u=D B_{y_0}(u) and r_u(t)=R_F(u,t). Differentiating the Coulomb
and ASD equations puts b_u in V. In the local trivialization,
r_u=dot A_u-d_A H_u, while differentiating g_y changes dot A_u
only by d_A of a zero-form. Thus b_u-r_u=d_A t_u for some
trace-free skew-adjoint zero-form t_u, with an immaterial gauge sign
absorbed into t_u. L095 proves that r_u itself lies in V. Integration
by parts now gives

\[
 \|b_u-r_u\|_{L^2}^2
   =\langle b_u-r_u,d_A t_u\rangle_{L^2}
   =\langle d_A^*(b_u-r_u),t_u\rangle_{L^2}=0.
\]

No inversion on the parallel gauge generators occurs. Therefore
D s_{y_0}(u)=P_V b_u=r_u. L095's actual norm identity is
G(r_u,r_w)=2lambda g(u,w), for its normalized positive inner product
G on V. In particular a:u mapsto r_u is injective on the real
four-dimensional T=T_{y_0}S_2. Define a linear left inverse
ell=(a^*a)^{-1}a^*:V to T using g and G; explicitly a^*a=2lambda id_T.
The smooth map f=ell composed with s:U to T has f(y_0)=0 and
D f_{y_0}=id_T in a local chart with that tangent identification.

Apply the finite-dimensional inverse function theorem, e.g. Lang,
*Fundamentals of Differential Geometry*, Theorem I.5.2, also cited
in Diez--Rudolph Appendix A, Theorem A.1. After shrinking U, f is
a diffeomorphism onto a neighborhood of zero. Thus f(y)=0 there
only at y_0. Equation (1) implies Z intersect U={y_0}. This proves
local isolation before any stabilizer quotient. An injective tangent
alone would not justify this conclusion without the actual smooth
coordinate and the orbit-return property.

**The reducible parameter set is closed.** For a stable F_y,
stable-bundle simplicity gives h^0(S_1,End(F_y))=1. This standard
stable-Hom/simplicity theorem applies to slope stability at a real
Kähler class; it requires no rational polarization. For a split fibre,

\[
 End(L\oplus L^{-1})\simeq O^{\oplus2}\oplus L^2\oplus L^{-2}.
\]

Neither L^2 nor L^{-2} has a section: each is nontrivial of zero
h-degree, whereas a nonzero effective divisor has positive h-degree.
This is the endpoint argument already proved in L094. Hence its
endomorphism dimension is exactly two. Every fibre is polystable
and has charge fourteen, so these are all possibilities, and

\[
              Z=\{y:h^0(S_1,End(F_y))\geq2\}.             \tag{2}
\]

Regard F and End(F) as algebraic bundles by GAGA on the projective
X. Apply the Stacks Project,
[Lemma 36.30.1, Tag 0A1H](https://stacks.math.columbia.edu/tag/0A1H),
with its Noetherian proof case
[36.27.2, 0DJQ](https://stacks.math.columbia.edu/tag/0DJQ) and derived
base change [36.26.4, 0A1D](https://stacks.math.columbia.edu/tag/0A1D).
For p_2, the morphism is projective, flat and finitely presented,
the first object O_X is perfect, and the bounded coefficient End(F)
is locally free, finitely presented and flat over S_2, with proper
support. Thus K=Rp_{2*}End(F) is perfect and

\[
        K\otimes^{\mathbf L}\mathbf C(y)
                    \simeq R\Gamma(S_1,End(F_y)).        \tag{3}
\]

The Stacks Project,
[Lemma 36.31.1, Tag 0BDI](https://stacks.math.columbia.edu/tag/0BDI),
applies to this perfect, hence pseudo-coherent, K. The degree-zero
derived-fibre dimension in (3) is upper semicontinuous, so the
threshold set (2) is Zariski closed, hence closed analytically.
This uses fibre cohomology, not the rank of the ordinary sheaf
p_{2*}End(F); ordinary degree-zero base change at a jump is not assumed.

**Compactness finishes the set-theoretic assertion.** The projective
complex surface S_2 is compact. Its closed subset Z is compact. Each
y_0 in Z has an open neighborhood meeting Z only at y_0 by the slice
argument. These neighborhoods cover Z, so a finite subcover contains
all its points. Thus Z is finite; the empty case needs no slice.
All other fibres are stable by L071's exhaustive classification.
This derives stability on the complement, rather than assuming
generic stability in the proof. No multiplicity or quotient-smoothness
conclusion follows. The actual bound sought was finiteness, not
absence of reducibles, and no cardinality bound is established.

**Separate critical audit, 2026-10-12 (step 248).** The approved
audit finds no substantive error or stronger conclusion. This is
EXPLORATION / REPRODUCTION: verification of the conditional argument,
not a new mathematical advance or a claim beyond the sources checked.
The direct mathematical inputs remain L071, L094 and L095.

The charge and Picard argument concerns actual bundles. In rank two,
polystability and local freeness make the nonstable alternative a sum
of line bundles; their determinant classes are opposite. The equation
14=14r^2 leaves only the unordered pair {L,L^{-1}}. Nonzero k and
torsion-free Picard group exclude L=L^{-1}, including an extra
exchanging stabilizer. Fixed-metric HE uniqueness gives a unitary
connection isomorphism, not merely a holomorphic S-equivalence. Its
determinant is a parallel U(1)-valued function on the connected fibre,
hence constant relative to the fixed frames. A constant scalar square
root corrects it to determinant one. A square root is needed for each
comparison separately, never continuously over all of Z. The global
parallel determinant frame is justified by the trivial holomorphic
determinant with constant HE line metric, as in L095; flatness alone
on an arbitrary base would not suffice.

The slice assertions apply to actual smooth connections. The primary
source's Section 5.3, equation (5.14), explicitly supplies the Coulomb
slice; Definition B.1 SL2 and SL3 and Proposition B.2 give its orbit
and local coordinate properties. These passages were checked against
the saved source coverage. One can keep the slice in that source's
smooth category and use L094's Sobolev implicit-function construction
only to choose the smooth gauge of this finite-dimensional family.
Regularity returns smooth connections and smooth gauges, so SL2
applies to the same representatives. If q carries A to B_y, then
B_y belongs to both the slice and q times the slice, regardless of
the size of q. Thus q stabilizes A and B_y=A. The local gauges g_y
are used for coordinates, not as substitutes for this arbitrary q.
Neither Theorem 5.8's quotient chart alone nor the unrelated
instanton-one finiteness discussion supplies this implication.

For the derivative, differentiating the actual ASD and Coulomb
equations puts b_u in V; the horizontal coefficient and the derivative
of g_y show b_u-r_u is d_A-exact. L095 places r_u in V too, so
orthogonality kills their difference even in the presence of the
parallel diagonal zero-form. The metric factor a^*a=2lambda id is
strictly positive. Choose a real chart psi with psi(y_0)=0 and
D psi at y_0 the identity on T. The square map
ell composed with s composed with psi^{-1} then has derivative id
at zero. The ordinary inverse function theorem gives an isolated
zero. Only the implication Z implies s=0 is used; no converse, exact
Kuranishi equation or injectivity after the circle quotient is needed.

For closedness, stable simplicity uses the real Kähler slope theorem.
On the split fibre a section of either L^{+/-2} would yield a
nonzero effective divisor of degree zero, or would trivialize the
nontrivial line. Both are impossible. Thus the complete two-branch
classification gives exactly the dimensions one and two, not merely
a necessary lower bound on reducibility. GAGA algebraizes F on the
projective product and preserves its local freeness. The smooth
projective projection is flat and finitely presented; its locally
free End(F) is base-flat with proper support. The first object O_X
in Tag 0A1H is perfect. Its stated Noetherian case and derived base
change therefore apply with no ordinary H^0 base-change assumption.
Tag 0BDI gives a closed threshold subset of the scheme S_2 whose
complex points are exactly Z. This closed algebraic subset has
closed analytification, hence compact complex point set. The local
isolating neighborhoods form an open cover of that compact set;
a finite subcover proves finiteness, including the empty case.

The audit verifies the requested threshold only. It supplies no
cardinality, absence of split fibres, multiplicities, integrated germ,
kernel or extension across the exceptional set. The compatible-line
and index-curvature stops remain intact. The universal primitive
Hodge realization gap remains open.

## Mathlib

Full matching coverage of this conditional exact-family finiteness
specialization: **not checked**. Unknown availability is not absence.
The load-bearing standard inputs are cited precisely above; the local
slice and harmonic derivative are the audited L094/L095 inputs.
The argument derives only their family-specific orbit, coordinate and
cohomological-locus consequences, without reproving the slice or
semicontinuity theorems or claiming novelty beyond the sources checked.
