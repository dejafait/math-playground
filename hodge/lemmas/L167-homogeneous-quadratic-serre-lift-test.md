# L167 — Homogeneous quadratic lifts fail universally at the formal endpoint

## Hypotheses

First consider only complex vector spaces H,U,K of dimensions 48,800,20,
respectively, with prescribed nondegenerate symmetric bilinear forms Q_U
on U and S on K. A quadratic map means a homogeneous polynomial map of
degree two. No geometric realization of these spaces or maps is assumed.

For the separate necessary-condition application, retain the entire
conditional family of L116 and L165, including their L071 and
L108/L109/L111/L115 hypotheses. Thus X=S_1 x B is the product of the
identical marked projective K3 surfaces with their original common metric,
ordered hyperkähler triple, fixed holomorphic forms and actual connection.
The hypothetical locally free rank-two product-polystable F has integral
c_1(F)=0 and ch(F)=2-14e_1-21e_2-tau_D+62P, P=e_1e_2, with the full
prescribed mixed tensor. Write V=End_0(F), C=Rp_*V, M=R^1p_*V and
W=R^2p_*V, retaining the full finite-point W. Use the actual maps
j:M[-1] -> C, a:C -> W[-2] and the normalized trace-adjoint retraction
r:C -> M[-1], with rj=id. Put

\[
 H=H^0(B,M),\quad K=H^1(B,M),\quad U=H^0(B,W),\quad E=H^2(X,V),
 \quad j_1=H^1(j),\ i=H^2(j),\ A=H^2(a),\ R=H^2(r).
\]

In this application impose only the formal endpoint s=|Z|=800, t=48
from L116; do not assume that it is realized or survives other notebook
constraints. Use L165's normalized complex bilinear Serre form Q on E,
S(u,v)=Q(iu,iv), and the actual inverse

\[
 T=(A|_{\ker R})^{-1}:U\longrightarrow\ker R,
 \qquad Q_U(u,v)=Q(Tu,Tv).
\]

These forms are not Hermitian. Use L164's actual point-bracket map beta
and L166's actual complementary operation kappa, with their commutator
convention and no factor 1/2 on Sym^2 H. No integrability, multiplicative
splitting, full Kuranishi presentation, value of beta or kappa, genericity,
or existence of F is assumed.

## Conclusion

There exists a homogeneous quadratic beta_0:H -> U for which there is
**no** homogeneous quadratic g_0:H -> K satisfying

\[
 S(g_0(h),g_0(h))+Q_U(\beta_0(h),\beta_0(h))=0
                       \quad\text{for every }h\in H.                 \tag{1}
\]

The witness can be chosen so that its quartic Q_U(beta_0,beta_0) is an
exact sum of 21 quadratic squares and lies outside even the Zariski
closure of sums of 20 quadratic squares. This is an existence proof;
no explicit coefficient tuple or realized geometric point map is supplied.

In the conditional geometric application the actual maps instead satisfy

\[
 \beta_{\rm br}(h)=\beta(h,h)=A[j_1h,j_1h],\qquad
 g_{\rm br}(h)=\kappa(h^2)=R[j_1h,j_1h],
\]
\[
 S(g_{\rm br}(h),g_{\rm br}(h))+
 Q_U(\beta_{\rm br}(h),\beta_{\rm br}(h))=0.                          \tag{2}
\]

Consequently the actual point quartic in (2) is an exact sum of at most
20 complex quadratic squares, possibly zero. The abstract witness cannot
be that actual map. Neither the actual quartic nor its minimum number of
squares is computed here. This disproves universal *formal* lifting,
not existence of F, and gives no new split-cardinality exclusion, cycle,
transport, or primitive Hodge realization. It is a local NEGATIVE /
REPRODUCTION specialization of known dimension and cyclicity results,
not a claim of progress beyond those results. The separate step 555
critical audit below confirms this specialization without a substantive
correction or stronger conclusion (EXPLORATION / REPRODUCTION).

## Proof

**Imported results and scope.** Reuse the invocation-start SPECIALIZE
assessment `drafts/literature/2026-10-25-quadratic-isotropic-lift-extremal-test.md`.
Import Ferguson, Ottaviani, Safey el Din and Teixeira Turatti,
*On the degree of varieties of sum of squares*, J. Pure Appl. Algebra
228 (2024), 107638, DOI 10.1016/j.jpaa.2024.107638,
[arXiv:2206.07473v2, Definitions 1.1–1.3 and Corollary 1.7,
printed pp. 2–3](https://arxiv.org/pdf/2206.07473v2).
For a complex vector space V_0 of dimension n+1, let SOS_k be the
Zariski closure in Sym^(2d)V_0 of the sums of k squares from Sym^d V_0.
The cited corollary gives the affine dimension

\[
 \dim\mathrm{SOS}_k
     =k\binom{n+d}{n}-\binom{k}{2}\qquad(k\le n).                    \tag{3}
\]

We use neither a formula outside this small-rank range nor a generic
rank or identifiability conjecture. Import diagonalization of symmetric
forms in characteristic different from two from Elman–Karpenko–Merkurjev,
*The Algebraic and Geometric Theory of Quadratic Forms*, AMS Colloquium
Publications 56 (2008), Chapter I, Proposition 1.6 and Corollary 1.9,
[printed pp. 13–15](https://www.math.ucla.edu/~rse/book/Kniga.pdf#page=23),
as already used in L165. The general dimension and diagonalization
theorems are not reproved. The work below is their exact endpoint,
closure and prescribed-form specialization.

**Dimensions and an exact-image witness.** Set V_0=H^*, n=47, d=2,
and P_2=Sym^2 H^*. Then dim P_2=binom(49,2)=1176. For k=20,21,
both satisfying k<=47, (3) gives

\[
 \dim\mathrm{SOS}_{20}=20\cdot1176-190=23330,
 \qquad
 \dim\mathrm{SOS}_{21}=21\cdot1176-210=24486.                        \tag{4}
\]

Padding by a zero square shows SOS_20 is contained in SOS_21.
Their dimension difference is 1156, so the containment is proper.
For completeness this does yield an *exact* witness, rather than just a
border representation. Let

\[
 f_{21}:P_2^{21}\longrightarrow\operatorname{Sym}^4H^*,\qquad
 (q_1,\ldots,q_{21})\longmapsto\sum_{a=1}^{21}q_a^2.
\]

If its entire image were contained in the closed set SOS_20, its Zariski
closure SOS_21 would also be contained there, contrary to (4). Hence
choose a tuple with

\[
 \varphi=\sum_{a=1}^{21}q_a^2\notin\mathrm{SOS}_{20}.                 \tag{5}
\]

Equivalently the inverse image of the complement of SOS_20 is nonempty
and Zariski open. In particular varphi admits no expression using 20
or fewer quadratic squares. Its exact minimum is 21. No assertion that
every point in SOS_21 has an exact representation is needed, and no
rank of an arbitrarily chosen Gram matrix is substituted for this test.

**Transfer through the prescribed forms.** Diagonalization and square
roots of the nonzero diagonal coefficients over C give bases e_1,...,e_800
of U and v_1,...,v_20 of K satisfying
Q_U(e_a,e_b)=delta_ab and S(v_a,v_b)=delta_ab. These are changes of
coordinates for the prescribed forms, not changes to the forms. Set

\[
 \beta_0(h)=\sum_{a=1}^{21}q_a(h)e_a.
\]

This pads exactly 779 zero coordinates and has Q_U(beta_0,beta_0)=varphi.
If a quadratic g_0 existed as in (1), write
g_0(h)=sum_{b=1}^{20}p_b(h)v_b with homogeneous quadratic p_b.
Then sum p_b^2=-varphi, so
varphi=sum (sqrt(-1)p_b)^2, contradicting (5). Equality at every h is
equality of polynomials over the infinite field C. This proves (1) is
not universally solvable for any prescribed pair of nondegenerate forms
of these dimensions. The argument uses just 21 of the 800 directions;
it makes no dominance claim for the 800-square parameterization and
uses neither real positivity nor pointwise choices of square roots.

**Actual degree-four cyclic identity.** Import the cyclic DG-Lie
construction from Bandiera, Manetti and Meazzini, *Formality conjecture
for minimal surfaces of Kodaira dimension 0*, Compositio Math. 157
(2021), 215–235, DOI 10.1112/S0010437X20007605,
[arXiv:1907.10690v2, Definition 3.6 and Example 3.7,
pp. 7–8, and Section 5 through (5.1), p. 14](https://arxiv.org/pdf/1907.10690v2).
Example 3.7 applies to locally free F on a smooth projective n-fold
with a holomorphic volume form, here n=4 and volume sigma_1 wedge
sigma_B. Restrict the integrated matrix-trace pairing to the actual
commutator-closed coefficient V. It is perfect by the trace-orthogonal
splitting End(F)=O id direct sum V and Tr(id^2)=2, as in L165.
Differential compatibility passes the invariant pairing to cohomology.
Theorem 3.8's n<=2 formality theorem is not used. As in the assessment
and L166, use the final invariant identity, retaining the source's
intermediate [h,g] versus final [g,h] discrepancy without importing the
intermediate line as an extra identity.

Denote the pairing in complementary cohomological degrees by < , >;
its degree-two restriction is Q. With the same normalization it obeys

\[
 \langle[a,b],c\rangle=\langle a,[b,c]\rangle,
 \quad [a,b]=-(-1)^{|a||b|}[b,a].                                    \tag{6}
\]

For x in H^1(X,V), the graded Jacobi identity with three copies of x
reads -3[x,[x,x]]=0. Since the coefficient field is C,

\[
 Q([x,x],[x,x])=\langle x,[x,[x,x]]\rangle=0.                        \tag{7}
\]

This has total degree four: the two arguments on the left have degree
two; those on the right have degrees one and three. It is not the
unevaluated 1,1,2 triple trace of L166. In particular (7) does not say
that R[x,x] vanishes.

The full polarized sign check is as follows. For x_1,...,x_4 of degree
one, Jacobi on x_2,x_3,x_4 gives
[x_2,[x_3,x_4]]+[x_3,[x_4,x_2]]+[x_4,[x_2,x_3]]=0.
Pair with x_1 and use (6), symmetry of the bracket on degree-one
inputs, and symmetry of Q on degree-two inputs. The result is

\[
 Q([x_1,x_2],[x_3,x_4])+
 Q([x_1,x_3],[x_2,x_4])+
 Q([x_1,x_4],[x_2,x_3])=0.                                         \tag{8}
\]

All three signs are plus. This also follows by polarizing (7): the
coefficient of t_1t_2t_3t_4 is eight times the left side of (8).
Individual terms need not vanish. No full Kuranishi isotropy theorem
or bracket-compatible splitting has been invoked.

**Endpoint and actual components.** L116 gives
dim H=t=48, dim U=s=800, and L165 gives
dim K=724-s+2t=20. The actual orthogonal decomposition from L165 is

\[
 E=i(K)\mathbin{\perp_Q}\ker R,
 \qquad x=i(Rx)+T(Ax).                                             \tag{9}
\]

Both restrictions of Q are nondegenerate, so the transported Q_U has
exactly the hypotheses of the formal part. Apply (9) to [j_1h,j_1h]
and (7) to j_1h. Orthogonality gives exactly (2). L164 and L166
identify its two components with the actual beta and kappa, using
actual arrows and retaining W; no arbitrary splitting replaces them.
These are homogeneous quadratic maps because the bracket is bilinear
and the arrows are linear. In the normalized S-basis, write
g_br=sum p_b v_b. Then (2) expresses the actual quartic as
sum (sqrt(-1)p_b)^2, an exact expression with at most 20 squares.

To check the bracket/Yoneda-square normalization, on closed degree-one
Dolbeault representatives alpha the commutator is
[alpha,alpha]=2 alpha cup alpha. The square is trace-free:
graded cyclic trace gives Tr(alpha cup alpha)=-Tr(alpha cup alpha),
so its scalar component is zero. Thus the quadratic Yoneda square is
one half the bracket diagonal in V. Its point and complementary
components are BOTH beta_br/2 and g_br/2. Using that convention
multiplies (2) by 1/4; it does not permit a factor change in just one
component. The same convention also rescales (8) uniformly.

This answers the approved universal question negatively while retaining
the necessary actual quadratic identity. L165's separate vector-by-vector
isotropic lifts and the scalar-only stop in ATTEMPTS/093 remain valid;
they give no quadratic polynomial choice. L166's unknown complementary
operation and the cyclicity-only stop in ATTEMPTS/094 remain unevaluated.
The actual quartic need not resemble the formal witness, and a nonzero
point map can even have identically zero quartic. Nothing here proves
genericity or failure of (2) for an actual F. Kernel existence, actual
section quadrics, integrability, transport and global primitive
realization remain independent unresolved gaps.

**Separate critical audit (2026-10-25, step 555).** This audit uses the
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-25-quadratic-isotropic-lift-critical-audit.md`.
It is conditional on the stated L116/L165 family, not an independent
audit of every earlier result or evidence that the endpoint exists.
The cited FOST, EKM and BMM results are imported with their recorded
hypotheses; no new general theorem or source discovery is needed.

For (3)--(5), the polynomial variables lie in H^*, of dimension 48,
so n=47 rather than 48. Quadratic roots have dimension
49*48/2=1176. Both 20 and 21 satisfy the printed k<=n condition.
The products are 23520 and 24696, and the subtracted binomial terms
are 190 and 210. Thus the affine dimensions in (4) and their difference
1156 are correct. No projectivization or subtraction of one occurs.
Zero-padding gives inclusion of the exact images and hence their
closures. Since the dimensions differ, the closed smaller locus cannot
contain the larger closure. If every exact 21-square value lay in the
smaller locus, closedness would force precisely that impossible
containment. Thus (5) selects an actual tuple. This argument does not
assume the exact image is closed or every border decomposition is exact.

For (1), both prescribed forms are symmetric, nondegenerate and complex.
EKM diagonalization therefore has nonzero weights, whose square roots
give the displayed normalized bases. No Hermitian or positive form is
substituted. The 21 chosen coordinates fit into U with 800-21=779
zeros. A homogeneous quadratic map to K has exactly 20 homogeneous
quadratic coordinate functions. Its claimed lift identity would give
varphi=sum (i p_b)^2. Padding represents any shorter expression by
20 squares, so this contradicts exclusion from SOS_20. The argument
does not require an explicit tuple, dominance of an 800-square map,
or a polynomial choice of pointwise square roots.

For the actual application, L116 gives dim U=800 and dim H=48,
while dim K=724-800+96=20 and dim E=724+96=820. These are conditional
dimensions, not an existence assertion. In L165 the actual identities
Ri=id, ker A=i(K), and Q(x,iu)=S(Rx,u) identify ker R with i(K)^perp.
For any x, x-iRx is in ker R and has A-image Ax; hence it equals
T(Ax) by the actual isomorphism A|ker R. This verifies (9), including
the inverse used to define Q_U. Nondegeneracy of Q and S makes Q_U
nondegenerate. An arbitrary splitting of the truncation would not
suffice. The full finite-point W remains present.

L164 defines beta by the very same A and j_1, using derived restriction
at each split point; it does not replace M(z) by the full derived
middle fibre. L166 identifies kappa(h^2) with R[j_1h,j_1h] using r
and the quotient convention uv in Sym^2 H, without division by two.
Only this identification, not a vanishing assertion or the value of its
global Ext^1 class, is used here. Thus (2) concerns the actual two
components with the common trace normalization of L165.

For (6)--(8), BMM's cyclic construction applies to the smooth projective
fourfold with its fixed nowhere vanishing holomorphic volume form and
locally free F. End_0(F) is closed under the differential and graded
commutator, and the trace-orthogonal scalar splitting makes its pairing
perfect. No n<=2 formality statement enters. At the needed degrees
1,1,2, the direct trace check is
Tr(beta alpha gamma)=-Tr(alpha gamma beta); hence
Tr([alpha,beta]gamma)=Tr(alpha[beta,gamma]). This checks the final
invariant identity despite the recorded source's intermediate reversed
bracket. The fixed canonical forms have even degree. A common nonzero
scalar multiplying the trace leaves the same invariant identity.

For odd x all three terms of graded Jacobi are -[x,[x,x]], giving
-3[x,[x,x]]=0 in characteristic zero. Pairing with x has degrees 1,3,
and cyclicity identifies this with Q([x,x],[x,x]) in degrees 2,2.
As an independent check on these particular signs, a degree-one
Dolbeault representative alpha satisfies [alpha,alpha]=2 alpha^2;
cyclically moving the first alpha past the other three gives
Tr(alpha^4)=-Tr(alpha^4)=0. This is only a check at the used degrees,
not a reproof of the general cyclic construction. For four independent
odd inputs the bracket is symmetric on each pair and Q is symmetric
between pairs. Each of the three pair partitions therefore occurs
2*2*2=8 times in the quartic expansion, with plus sign. This confirms
both the polarized relation (8) and its coefficient. It does not make
any individual pair-partition term zero.

Finally Tr(alpha^2)=0 by odd cyclic trace, so the Yoneda square is in
V and is half the bracket diagonal. Linearity of both actual arrows
then halves both components, multiplying the scalar identity by 1/4.
With (9), the degree-four identity proves precisely the necessary
at-most-20-square representation already stated. It supplies no actual
quartic coefficients, minimum square count or genericity. A nonzero
point map can have zero quartic. L165's pointwise result and the
scalar-only and cyclicity-only stops in ATTEMPTS/093 and /094 are
unchanged. No substantive error or stronger conclusion was found;
the audit outcome is EXPLORATION / REPRODUCTION. Kernel existence,
actual operations, integrability, transport and primitive realization
remain unresolved.

## Mathlib

Supporting normal-form coverage, already recorded in L165, is
[`QuadraticForm.equivalent_weightedSumSquares_of_isAlgClosed`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/QuadraticForm/AlgClosed.html).
The finite-dimensional complex and nondegenerate-form hypotheses hold
here; normalization of nonzero weights uses complex square roots.
Full matching Mathlib coverage for the cited complex SOS-locus dimension
theorem, the exact-image counterexample and the actual cyclic/derived
component specialization is not checked. No absence or formal
verification is claimed. The argument and integer arithmetic above are
informal; no mathematical script or numerical certificate is used.
The separate audit is also informal and adds no Mathlib verification.
