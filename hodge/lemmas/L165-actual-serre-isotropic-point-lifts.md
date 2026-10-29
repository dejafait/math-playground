# L165 — Actual Serre-isotropic lifts of every point-quotient vector

## Hypotheses

Retain L071's identical marked projective K3 factors S_1 and B, their
original common metric, ordered hyperkähler triple and real product
class. Retain L116's entire conditional family and conclusions, including
its uses of L108/L109/L111/L115. Thus the hypothetical locally free,
rank-two, product-polystable F on X=S_1 x B has integral c_1(F)=0 and

\[
 \operatorname{ch}(F)=2-14e_1-21e_2-\tau_D+62P,
 \qquad P=e_1e_2,
\]

with the full prescribed mixed tensor and actual connection. Fix the
nonzero holomorphic forms sigma_1 and sigma_B used in duality. Set
V=End_0(F), p:X -> B, C=Rp_*V, M=R^1p_*V and W=R^2p_*V.
Use L116's actual arrows j:M[-1] -> C, a:C -> W[-2], and its actual
trace-adjoint retraction r:C -> M[-1]. In particular rj=id.
M is locally free, b:M -> M^vee is its nondegenerate alternating
relative Serre form, and M=T_B direct sum N. The finite set Z may
be empty; W has length one at each of its points. Put s=|Z| and
retain the unknown t=h^0(B,N), with no assumed value.

Let Q be the complex bilinear fourfold Serre form on H^2(X,V), using
matrix trace on V and the product volume form. Normalize its relative
trace by the same nonzero scalar as b in L109/L116 and its base trace
by sigma_B. Any other common nonzero scalar multiple of this Q has the
same null cone and conclusions. Q is not a Hermitian norm.

No existence of F, integrability of first-order deformations, value of
the bracket, multiplicative splitting, or compatible Kuranishi map is
assumed. The question concerns elements of the obstruction vector space
with no additional geometric or polynomial constraints.

## Conclusion

Write

\[
 K=H^1(B,M),\quad E=H^2(X,V),\quad U=H^0(B,W),
 \quad i=H^2(j),\quad A=H^2(a),\quad R=H^2(r).
\]

Then the actual included subspace i(K) is Q-nondegenerate,

\[
 \ker R=i(K)^{\perp_Q},\qquad
 E=i(K)\mathbin{\perp_Q}\ker R,\qquad
 A|_{\ker R}:\ker R\xrightarrow{\sim}U.                 \tag{1}
\]

Moreover dim K=724-s+2t>=20. Every w in U has a lift x in E with
A(x)=w and Q(x,x)=0. Equivalently, A maps the Q-null cone onto U.
This includes U=0 without requiring a point of Z.

This is a conditional NEGATIVE / REPRODUCTION for the proposed
scalar-isotropy exclusion route: scalar isotropy alone puts no restriction
on the point quotient when the complementary component is unrestricted.
It is a local actual-map specialization of the assessed standard tools,
not a new general quadratic-form theorem or progress beyond those tools.
The separate critical audit below preserves this conclusion, with outcome
EXPLORATION / REPRODUCTION and no substantive error or stronger result.
No bracket value, compatible map of
deformation spaces, kernel existence, new cardinality exclusion, transport
or primitive Hodge realization follows.

## Proof

**Imported results and applicability.** Reuse the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-25-global-point-quotient-isotropic-lift.md`.
Import smooth proper relative duality from
[Stacks Lemma 48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT),
its actual cup/evaluation/trace pushforward pairing from
[Remark 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81),
and shift-compatible global Serre duality and its evaluation/trace
pairing from [Lemma 48.27.1 and Remark 48.27.2,
0FVU](https://stacks.math.columbia.edu/tag/0FVU).
Here p is smooth proper of relative dimension two, B and X are smooth
projective, V and M are locally free, and C is perfect bounded coherent.
The fixed forms trivialize the canonical lines. The trace form on V is
perfect: End(F)=O id direct sum V is trace-orthogonal and Tr(id^2)=2.
Thus Q is perfect; graded symmetry makes it symmetric in total degree
two, since (-1)^(2*2)=1. These duality statements do not require W to
be locally free. No ordinary middle base change at Z is used.

For the finite-dimensional algebra import Elman--Karpenko--Merkurjev,
*The Algebraic and Geometric Theory of Quadratic Forms*, AMS Colloquium
Publications 56 (2008), Chapter I, Proposition 1.6 and Corollary 1.9,
[printed pp. 13–15](https://www.math.ucla.edu/~rse/book/Kniga.pdf#page=23):
nondegenerate-subspace orthogonal decomposition and diagonalization of
symmetric forms in characteristic different from two. Apply them only
after verifying the actual kernel restriction below. Their general proofs
are not repeated. The specialization is necessary because an arbitrary
additive splitting of C would not identify these actual orthogonal arrows.

**The kernel and its form, with shifts.** L116's split truncation gives

\[
 0\longrightarrow K\xrightarrow{i}E\xrightarrow{A}U
 \longrightarrow0,\qquad Ri=\mathrm{id}_K.              \tag{2}
\]

The shifts are cohomological: H^2(M[-1])=H^1(M) and
H^2(W[-2])=H^0(W). Let D=RHom_B(-,O_B). L116 fixes
alpha:C[2] -> DC as the actual normalized relative trace adjoint and

\[
 f=(Dj)[-2]\,\alpha[-2]:C\longrightarrow M^\vee[-1],
 \qquad fj=b[-1],\qquad f=b[-1]r.                      \tag{3}
\]

These identities are actual global derived morphism identities, including
at Z; they do not assert ordinary base change there.

Let Tr_B:H^2(B,O_B) -> C be the fixed base Serre trace, and set

\[
 B_M(u,v)=\operatorname{Tr}_B\bigl((H^1b)(u)\smile v\bigr),
 \qquad u,v\in K,                                    \tag{4}
\]

where cup is followed by evaluation M^vee tensor M -> O_B.
This is a perfect bilinear form: Serre duality gives a perfect pairing
H^1(M^vee) times H^1(M) -> C, and H^1b is an isomorphism.
It is symmetric: the base cup of two degree-one classes changes sign
on interchange, as does the alternating coefficient form b. Neither
sign is a complex conjugation or a positivity assertion.

Here is the sign comparison with the shifted relative pairing. Use a
base-first totalization: a local degree-one base cochain eta with
relative degree-one coefficient m is eta tensor m. The product with
theta tensor n moves m past theta and hence is

\[
 (\eta\otimes m)(\theta\otimes n)
               =-\eta\theta\otimes(mn).               \tag{5}
\]

Thus the normalized global pairing restricted through j is
Q(iu,iv)=-B_M(u,v). This calculation is the tensor-shift sign for
M[-1] tensor M[-1], not a choice of a new form on K. It applies to
the derived pairing as well: pullback of that pairing by j tensor j
is adjoint to fj=b[-1], so is exactly the shifted coefficient form b.
One need not represent global classes by fibrewise harmonic sections.
With a different shift identification both formulas use the same fixed
nonzero scalar, and nondegeneracy and orthogonality are unchanged.

More generally functoriality of the imported evaluation/trace pairing
identifies pairing against j with applying Dj to the trace adjoint.
Consequently (3), with the very same sign (5), gives for all x in E
and u in K

\[
 Q(x,iu)=-\operatorname{Tr}_B\bigl((H^2f)(x)\smile u\bigr)
        =-B_M(Rx,u).                                   \tag{6}
\]

Indeed H^2(f) has target H^1(M^vee), and (3) gives
H^2(f)=(H^1b)R. Equation (6) is the global adjoint identity for
these actual arrows; no perfectness of an arbitrarily chosen restriction
has been substituted for it. In particular S(u,v):=Q(iu,iv)=-B_M(u,v)
is nondegenerate and Q(x,iu)=S(Rx,u).

**The actual orthogonal complement and its size.** By (6), x is
orthogonal to i(K) exactly when Rx=0, proving the first equality in
(1). The imported nondegenerate-subspace theorem applies to i(K).
Its complement is therefore the actual ker R, not a separately selected
summand. More explicitly every x has decomposition

\[
                   x=i(Rx)+(x-i(Rx)),\qquad
                   R(x-i(Rx))=0.                       \tag{7}
\]

The summands intersect trivially by Ri=id. By (2), A restricts to an
isomorphism on ker R: it is injective because its kernel is i(K), and
it is surjective by (7). For w in U the unique orthogonal lift y is
x-i(Rx), where x is any lift; replacing x by x+iu changes neither y
nor this construction. Since Q on E and S on K are perfect, the form
on ker R is perfect too, although this extra fact is not needed below.

There is always a nonzero kernel direction. L116 gives the actual
bundle splitting M=T_B direct sum N, and its K3 computation gives
h^1(B,T_B)=20. Hence

\[
 \dim K=20+h^1(B,N)=724-s+2t\ge20.                     \tag{8}
\]

The equality uses L116's h^1(N)=704-s+2t. No guessed value of t,
acyclicity, strict stability, or nonempty Z has entered this inequality.

**Pointwise isotropic lifts.** Apply the imported diagonalization theorem
to the nonzero finite-dimensional complex space (K,S). Since S is
nondegenerate, it has a diagonal basis with nonzero diagonal entries;
fix one basis vector e and put d=S(e,e)!=0. For a given w in U, let
y be its actual orthogonal lift from (1). Algebraic closure of C gives
c in C satisfying

\[
                        c^2=-Q(y,y)/d.                 \tag{9}
\]

Set x=y+c i(e). Orthogonality, Ai=0 and (9) give

\[
 A(x)=w,\qquad
 Q(x,x)=Q(y,y)+2cQ(y,i(e))+c^2d=0.                    \tag{10}
\]

If Q(y,y)=0 take c=0. If U=0, w=y=x=0 suffices. This proves the
claimed surjectivity for all retained values of s,t. It is an existence
statement for each vector separately, not a choice of a Kuranishi map,
a polarized obstruction identity, or a prescribed polynomial lift of
the actual bracket. No such additional compatibility is proved here.

The continuation test is therefore answered affirmatively. Scalar
isotropy of an otherwise unspecified full obstruction vector cannot by
itself exclude any value of its point projection. This parks exactly
that proposed exclusion mechanism; it does not show that an actual
geometric obstruction has any chosen value or even that F exists.
Other independent gaps in the Hodge route remain unchanged.

**Separate critical audit (2026-10-25, step 549).** The invocation-start
SPECIALIZE assessment is
`drafts/literature/2026-10-25-actual-serre-isotropic-lift-critical-audit.md`.
This audit checks the displayed argument conditional on L071 and L116,
including L116's retained L108/L109/L111/L115 hypotheses and conclusions.
It does not independently reprove that entire conditional family.
The primary duality and quadratic-form results above are imported with
the stated hypotheses. For the tensor convention use
[Stacks Section 15.59, 0GWN](https://stacks.math.columbia.edu/tag/0GWN),
the commutativity constraint and differential calculation preceding
Lemma 15.59.1, and its sheaf-complex version
[Lemma 20.50.1, 0FP7](https://stacks.math.columbia.edu/tag/0FP7),
as inspected in the prior assessment. No new source search is needed.

First, the duality hypotheses hold for the actual trace coefficient:
V is locally free and trace-self-dual over C, X and B are smooth
projective with the specified canonical trivializations, and C is
perfect. The shift calculation is
D(M[-1])=M^vee[1], so (Dj)[-2] alpha[-2] lands in M^vee[-1].
The assertion fj=b[-1] is precisely L116's actual morphism identity.
Its verification uses a sheaf Hom group after shifting both arguments
by one: agreement on the stable dense open therefore extends globally
between locally free sheaves. It is not an inference that arbitrary
derived morphisms agreeing off Z agree on B. Multiplying the normalized
relative trace by a nonzero scalar multiplies f and b together and
leaves r=b^{-1}[-1]f unchanged. The same scalar multiplies Q and B_M;
it does not change the orthogonal complement or null cone.

Next check the mixed identity (6), not merely its restriction to K.
Let p_C:C tensor^L C -> O_B[-2] denote the actual relative pairing.
By adjunction its restriction p_C(1 tensor j) factors through
f tensor 1 and evaluation
M^vee[-1] tensor M[-1] -> O_B[-2]. This equality is in D(B),
before global sections, so it also controls classes supported over Z.
Apply the functorial derived cup on global sections and then Tr_B.
Both resulting inputs in M^vee[-1] and M[-1] have coefficient degree
one and base cohomology degree one. In base-first totalization the
first coefficient crosses the second base input once. The resulting
factor is (-1)^(1*1)=-1, exactly (5); no further odd interchange is
introduced by the degree-two canonical forms or shifts. Since
H^2(f)=(H^1b)R, this proves (6) for every x, not only x in i(K).
Functoriality here is that of the actual cup/evaluation/trace map of
0G81 and 0FVU. There is no use of a multiplicative Leray splitting,
ordinary middle base change, or representatives with pure fibre degree.

The restriction is consequently S=-B_M. Serre duality on the smooth
projective surface pairs H^1(M^vee) perfectly with H^1(M), using the
fixed trivialization of omega_B; H^1b is invertible. Thus S has zero
radical. Alternation of b cancels the odd base-cup interchange, making
S symmetric. This independently checks both the sign comparison and
the hypothesis needed for the quoted nondegenerate-subspace theorem.
Equation (6) says Q(x,iu)=S(Rx,u), so nondegeneracy gives
x in i(K)^perp if and only if Rx=0. Ri=id and ker A=i(K) then give
the orthogonal direct sum and the bijection A|ker R in (1). For any
lift x of w, subtracting iRx preserves A(x) and kills R; if a second
lift differs by iu, that subtraction removes exactly the same iu.
This checks existence and uniqueness of the actual orthogonal lift.

The dimension computation uses actual cohomology, not formal allowed
integers: L116 gives h^1(N)=704-s+2t, and M=T_B direct sum N gives
dim K=20+h^1(N). In particular dim K>=20 even if Z is empty or
t=0. Together with dim U=s it also recovers dim E=724+2t from (2),
consistent with L116. The lower bound does not assume nonempty Z,
a positive section multiplicity, or existence for each numerical s,t.

Finally the quoted characteristic-not-two diagonalization applies to
the nonzero symmetric nondegenerate complex space (K,S). Its vector
e has d=S(e,e) nonzero. For every w, algebraic closure supplies the
scalar c in (9); there is no requirement that the square root be real,
vary regularly in w, or agree with a geometric obstruction component.
Because y is in ker R=i(K)^perp, the cross term in (10) is zero,
and Ai=0 keeps the prescribed projection. If U=0 the sole vector 0
has the lift 0. Thus all cases of the conclusion survive the audit.

No substantive correction or stronger conclusion is obtained. The
scalar-isotropy-only stopping result is preserved; the actual bracket
and its complementary component remain unevaluated. In particular the
set-theoretic surjectivity just verified neither prescribes an actual
obstruction map nor contradicts existence of F. This completed audit
is EXPLORATION / REPRODUCTION, not a new mathematical advance or a
resolution of the main Hodge gap.

## Mathlib

Supporting coverage inspected in the prior assessment is
[`QuadraticForm.equivalent_weightedSumSquares_of_isAlgClosed`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/QuadraticForm/AlgClosed.html).
Its finite-dimensional, algebraically closed, invertible-2 and separating
associated-form hypotheses hold for the nondegenerate S over C. This
supports scalar normal form only. Full matching Mathlib coverage for
this actual-derived-adjoint comparison and quotient-lift specialization
has not been checked. No absence or formal certification is claimed.
The separate informal audit above does not supply formal certification.
