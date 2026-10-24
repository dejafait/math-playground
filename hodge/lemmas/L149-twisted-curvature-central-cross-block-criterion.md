# L149 — Central cross-block test for the actual twisted curvature

## Hypotheses

Retain L148's hypothetical locally free rank-two Omega-polystable F
on the identical marked K3 product p:S_1 x B -> B, its compatible
smooth Hermitian connection, integral c_1(F)=0 and
ch_2(F)=-14e_1-21e_2-tau_D. Retain the common hyperkähler metric,
the line L with c_1(L)=k=(-4,-2,1,2), and the **same arbitrary fixed
smooth positive metric** on L^{-1}. Put G=F tensor p_1^*L^{-1}.
L147's M=R^1p_*G is locally free of rank 24; its actual harmonic
metric H is defined away from the finite, possibly empty, split set Z.

Select z in Z. Use L146's entire Koszul splitting and L148's natural
spectral comparison. In its extending holomorphic frame K^1=P plus J,
P has rank two, J has rank 24, and the boundary is v=(w,0), where
w=(x,y)^t are holomorphic coordinates centered at z. Write the smooth
positive metric pulled back from the cutoff complex as

\[
 H_K(w)=\begin{pmatrix}A(w)&B(w)\\B(w)^*&C(w)\end{pmatrix}.       \tag{1}
\]

The first Hermitian slot is anti-linear. Thus B is a 2 by 24 matrix;
the star denotes conjugate transpose. No vanishing of B(0) is assumed.
The norm of curvature uses H and the fixed smooth base metric.

## Conclusion

For this actual metric and selected parameter,

\[
 \sup_{0<|w|<\epsilon}|\Theta_H(w)|<\infty
 \text{ for some }\epsilon>0
 \quad\Longleftrightarrow\quad B(0)=0.                         \tag{2}
\]

If B(0) is nonzero, there are constant linear holomorphic coordinates
and a constant change of the extending J-frame for which, along
w=(r,0) with r>0,

\[
 (\Theta_H)_{\bar y y}(r,0)
  =r^{-2}\operatorname{diag}\left(
   \frac{s_1^2(1-s_2^2)}{1-s_1^2},-s_2^2,0,\ldots,0\right)
     +O(r^{-1}),                                             \tag{3}
\]

where 0<=s_2<=s_1<1 and s_1>0. The coefficient convention in (3)
is dbar(y) wedge dy. In particular actual curvature would be unbounded
in that alternative, even when the leading trace happens to vanish.
All higher coefficients of the original complex and metric are retained.

The condition in (2) is precisely orthogonality, for the given central
twisted harmonic product on V=H^1(S_1,L^{-2}), of

\[
 P_z=\operatorname{span}(q_1,q_2),\qquad
 J_z=\bigcap_{i=1}^2\ker\big(c\mapsto T(p_i\wedge c)\big).     \tag{4}
\]

Here p_i and q_i are L146's actual positive and negative KS classes,
and T is its nonzero normalized Serre functional. This conclusion
does **not** evaluate that harmonic product. Neither alternative is
asserted to occur for the hypothetical family and its given metric.
If Z is empty there is no local test. The bounded-curvature attempt
remains inconclusive at (4), with no F nonexistence, extension,
positivity, split-count bound, cycle or transport conclusion. This is
a REPRODUCTION specialization of the assessed Chern/quotient tools.
The separate critical audit below preserves the criterion without a
substantive repair or stronger conclusion; it is not a Hodge-conjecture
resolution.

## Proof

**Sources and scope.** Reuse the unchanged pre-invocation SPECIALIZE
assessment `drafts/literature/2026-10-23-twisted-harmonic-metric-curvature.md`.
Import the Chern formula from J.-P. Demailly, *Complex Analytic and
Differential Geometry*, version 21 June 2012, Chapter V, section 12,
(12.2)-(12.3) and Theorem 12.4, pp. 268-269; its quotient-connection
framework is in section 14, Theorems 14.3/14.5 and (14.6)-(14.7),
pp. 273-275 ([inspected primary text mirror](https://www.ime.usp.br/~cordaro/wp-content/uploads/2022/03/Jean-Pierre-Demailly-Complex-Analytic-and-Differential-Geometry-1.pdf#page=269)).
The formula is applied only on the puncture, where M and its metric
are smooth. Its hypotheses do not imply extension across a jumping
cohomology fibre. L148 supplies the actual natural harmonic quotient
and uniform positive norm bounds, using Bismut--Gillet--Soulé III,
Section 1(b)-(c), Theorem 3.5 and Lemmas 3.6-3.8, as precisely cited
there. No general source formula is reproved. The calculation below
specializes those formulas to the shrinking boundary in this complex.
L113 is a comparison for a different coefficient, not an input giving
central orthogonality here.

**The full quotient and its central meaning.** Minimizing L148's
exact least-norm expression over the scalar boundary coefficient gives

\[
 H(w)=C(w)-\frac{B(w)^*ww^*B(w)}{w^*A(w)w},\qquad w\ne0.       \tag{5}
\]

This is the original harmonic metric in its actual extending frame.
All terms in (1) are smooth at zero. On a smaller closed ball their
derivatives of every fixed finite order are bounded, and positive
definiteness gives w^*A(w)w>=c|w|^2. L148 bounds H and H^{-1} there.

The central natural comparison identifies K^1_z with all of
H^1(G_z)=H^1(L^{-2}), since H^1(O)=0. L146 identifies the residues
of the two P-generators with q_1,q_2. For every holomorphic section
j of J, the exact equation rho(j)=0 implies that both linear
coefficients of the outgoing row annihilate j(0). Those coefficients
are c -> T(p_i wedge c). Their restrictions to P form L146's
invertible alternating two by two matrix, so they are independent.
Their common kernel has dimension 24 and therefore equals J_z.
This proves (4), including equality rather than just containment.
L148's central comparison is the natural cohomology identification,
so B(0)=0 is exactly the asserted harmonic orthogonality.

In particular this test is not changed by arbitrary choices in the
higher-order splitting: its two central subspaces are intrinsic for
the chosen tangent basis, and changing that basis preserves them.
For the arbitrary line metric, q_i and c in (4) are represented by
their harmonic representatives for that metric. One may not simply
use the raw adjoint-harmonic representatives from L095 as though
they were harmonic for this different coefficient metric.

**Sufficiency, retaining all derivatives.** Suppose B(0)=0. Set
r=|w|, u=B(w)^*w, N=uu^* and d=w^*A(w)w. Use real coordinate
derivatives D, with every estimate uniform on one full punctured ball.
Smoothness and B(0)=0 give B=O(r), DB=O(1), D^2B=O(1), hence

\[
 D^ku=O(r^{2-k}),\quad D^kN=O(r^{4-k}),\quad
 D^kd=O(r^{2-k})\qquad(0\le k\le2).                           \tag{6}
\]

The term D^2u includes D^2B^* times w and both first-derivative
products. Since d>=cr^2,

\[
 D(d^{-1})=-d^{-2}Dd,\qquad
 D_iD_j(d^{-1})=2d^{-3}(D_i d)(D_j d)-d^{-2}D_iD_jd,
\]

give D^k(d^{-1})=O(r^{-2-k}) for k<=2. Every product-rule term in
D^k(N/d) is consequently O(r^{2-k}). Equation (5) proves bounded
first and second derivatives of H, as well as H itself. The imported
formula expands, in this holomorphic frame, as

\[
 \Theta_H=-H^{-1}(\bar\partial H)H^{-1}\wedge\partial H
                         +H^{-1}\bar\partial\partial H.       \tag{7}
\]

Together with the uniform bound on H^{-1}, these estimates bound all
curvature coefficients. Smooth positivity of the base metric and
L148's uniform norm equivalence give the claimed bound in the actual
norms. No axis or direction has been removed.

**Necessity and the full remainder.** Make constant changes of P
and J bases, and the corresponding invertible linear change of w,
so that A(0)=I_2 and C(0)=I_24. Such a simultaneous change keeps
the incoming column (w,0); it does not change the metric or its
cohomology identification. Independent unitary changes on these
two spaces put B(0) in rectangular singular-value form

\[
 B_*=[\operatorname{diag}(s_1,s_2)\ \ 0].                       \tag{8}
\]

Positive definiteness of the full matrix (1) at zero implies
I_24-B_*^*B_*>0 by completing the square in its P component.
Thus 0<=s_2<=s_1<1. Nonzero B(0) means s_1>0. Constant coordinate
and frame changes preserve boundedness in the given smooth norms.

Define the homogeneous degree-zero leading metric on the puncture by

\[
 H_*(w)=I_{24}-\frac{B_*^*ww^*B_*}{|w|^2}.                     \tag{9}
\]

It is uniformly positive since its least eigenvalue is at least
1-s_1^2. We claim, for k=0,1,2,

\[
 D^k(H-H_*)=O(r^{1-k}),\quad
 D^kH_*=O(r^{-k}),\quad H^{-1}-H_*^{-1}=O(r).                  \tag{10}
\]

Here is the control of every singular remainder. Each of A-I,
B-B_* and C-I is O(r), its first derivatives are O(1), and its
second derivatives are O(1), hence also O(r^{-1}) on r<=1. Writing
N=B^*ww^*B, N_*=B_*^*ww^*B_*, d=w^*Aw and d_*=r^2, the product
rule gives D^k(N-N_*)=O(r^{3-k}) and
D^k(d-d_*)=O(r^{3-k}) for k<=2. The denominator estimates used
above hold without B(0)=0. Applying them to
d^{-1}-d_*^{-1}=(d_*-d)/(dd_*) gives O(r^{-1-k}) for its kth
derivatives. Now

\[
 N/d-N_*/d_*=(N-N_*)d^{-1}+N_*(d^{-1}-d_*^{-1})
\]

has kth derivatives O(r^{1-k}). This proves the first assertion of
(10), including all second derivative terms of A,B,C. Homogeneity
and smoothness of H_* on the unit sphere prove the second. The last
follows from H^{-1}-H_*^{-1}=-H^{-1}(H-H_*)H_*^{-1} and the two
uniform inverse bounds.

Substitute H=H_*+(H-H_*) into (7). In the second-derivative term,
the inverse difference O(r) multiplies O(r^{-2}), or a bounded
inverse multiplies O(r^{-1}). In the product of first derivatives,
an inverse difference multiplies two O(r^{-1}) factors, or at least
one derivative difference O(1) replaces an O(r^{-1}) factor; the
term with both derivative differences is O(1). Consequently the
complete curvature tensors satisfy in coordinate coefficients

\[
                       \Theta_H-\Theta_{H_*}=O(r^{-1}).        \tag{11}
\]

This comparison does not discard smooth higher terms by assertion;
their maximum possible contribution has been bounded explicitly.

It remains to exhibit a nonzero leading curvature component. Near
the line y=0 with x!=0, write zeta=y/x. The only nonidentity block
of (9) is

\[
 H_*^{(2)}=I_2-\frac1{1+|\zeta|^2}
  \begin{pmatrix}s_1^2&s_1s_2\bar\zeta\\
                  s_1s_2\zeta&s_2^2|\zeta|^2\end{pmatrix}.
\]

At zeta=0 its value is diag(1-s_1^2,1), and its derivatives are

\[
 (H_*)_\zeta=\begin{pmatrix}0&0\\-s_1s_2&0\end{pmatrix},\quad
 (H_*)_{\bar\zeta}=\begin{pmatrix}0&-s_1s_2\\0&0\end{pmatrix},\quad
 (H_*)_{\zeta\bar\zeta}=\operatorname{diag}(s_1^2,-s_2^2).
\]

Formula (7) makes the coefficient in dbar(zeta) wedge dzeta equal to

\[
 H_*^{-1}(H_*)_{\zeta\bar\zeta}
 -H_*^{-1}(H_*)_{\bar\zeta}H_*^{-1}(H_*)_\zeta
 =\operatorname{diag}\left(
 \frac{s_1^2(1-s_2^2)}{1-s_1^2},-s_2^2\right).                 \tag{12}
\]

At (x,y)=(r,0), differentiation in y introduces 1/r and in bar(y)
introduces 1/r. Equations (11)-(12) prove (3). Its first diagonal
entry K=s_1^2(1-s_2^2)/(1-s_1^2) is strictly positive. For sufficiently
small r the corresponding entry of actual curvature has absolute
value at least K/(2r^2), since its error is bounded by C/r.
Uniform equivalence of both actual metrics with coordinate norms
then gives unbounded actual curvature. This proves the necessary
direction of (2); it also treats rank-one B and equal singular values.

**What the attempt does and does not decide.** The algebraic split
data and the actual Chern formula now give an exact discriminating
test at the central fibre. They do not supply the value of its matrix.
L146's Serre matrix T(p_i wedge q_j) is nondegenerate, but it is not
the arbitrary-metric Hermitian product in (4). L095's harmonicity
is for the compatible adjoint connection, not automatically for G
with the retained line metric. L113's real-structure argument therefore
does not fill this remaining comparison. No theorem asserting that
all smooth choices of the line metric preserve (4) is used, and no
nonzero actual block is manufactured by an abstract finite complex.
The recorded automatic-extension, singular-metric, strict-Euler and
duality-only stops retain their scopes. Only evaluation of (4) for
the actual allowed metric can select the bounded or divergent branch.

**Second bounded attempt: the retained line metric (step 478).**
This is a continuation under the same prior SPECIALIZE assessment, not
the separate critical audit of (2). It still does not select a branch.
The following computation records the obstruction to applying the
connection-metric harmonic identity to the metric actually specified.

At the selected split fibre let h_0 be the metric on the negative
coefficient E=L^{-2} induced by the split compatible connection and its
dual line metric. The actual metric on that same holomorphic coefficient
is w h_0 for a fixed smooth function w>0 on S_1. The factor w is the
ratio of the specified twisting-line metric to the dual connection
metric; it is not assumed constant. The split coefficient summands are
orthogonal for both metrics. Since H^1(O)=0, the entire middle harmonic
product is the one on E. Using h_0 as a reference in the calculation
does not change the metric being tested.

Write D=bar-partial_E on sections, and D_0^* for its adjoint for h_0
and the fixed fibre metric. For each cohomology class a, write a_0 for
its h_0-harmonic representative. Set

\[
 A_w=D_0^*wD,\qquad f_a=D_0^*(w a_0),\qquad
 u_a=A_w^{-1}f_a.                                           \tag{13}
\]

These are operators on the fixed fibre, not on the punctured base.
The inverse in (13) exists: the degree-zero weighted Dolbeault
Laplacian is w^{-1}A_w, and its kernel is H^0(E)=0, as in the split
cohomology calculation used by L146. Import the ordinary compact-fibre
Hodge decomposition and smooth harmonic representatives in the BGS III
Section 1(b)-(c) setup cited in L148. Positivity and compactness give
the closed range and inverse on smooth sections. Equivalently, A_w is
self-adjoint for the reference product and
<u,A_w u>_0=<Du,wDu>_0; its kernel is precisely the holomorphic sections.
No inverse through a cohomology jump on the parameter base is asserted.

On E-valued one-forms the weighted adjoint is
D_w^*=w^{-1}D_0^*w, by its defining integration-by-parts identity.
Consequently the actual harmonic representative and actual pairing are

\[
 a_w=a_0-Du_a,\qquad
 h_w(a,b)=\langle a_0,w b_0\rangle_0
                -\langle f_a,A_w^{-1}f_b\rangle_0.           \tag{14}
\]

Here every Hermitian product is anti-linear in its first argument.
Indeed a_w is closed, represents a, and D_0^*(w a_w)=0 by (13),
so weighted Hodge uniqueness identifies it with the actual harmonic
representative. To check all terms in (14), expand
<a_0-Du_a,w(b_0-Du_b)>_0. Each of
<Du_a,w b_0>_0, <a_0,wDu_b>_0 and <Du_a,wDu_b>_0 equals
<u_a,A_w u_b>_0: use f_b=A_w u_b, f_a=A_w u_a and self-adjointness
in the second equality. Thus the two subtracted terms and the one
added term leave one subtraction, equal to the last term in (14).
This retains both exact corrections, with no multiplicativity claim
for harmonic projection.

For a=q_i and b=c in J_z, (14) is therefore an exact expression for
the block in (4) using the unchanged fixed metric. The pointwise
connection identities used in L094/L113 do not remove its weight w
or identify its second term with its first. In particular even knowing
an unweighted orthogonality would not evaluate this expression: neither
weighted integral nor elliptic correction has been shown zero or equal
to the other. No value for the actual w, q_i or their corrections has
been obtained from the retained hypotheses. Treating f_a as zero would
silently assert that the reference harmonic form is weighted harmonic,
which is precisely not justified.

This second attempt leaves the actual central test unresolved and is
EXPLORATION / REPRODUCTION, not a bound, divergence result or new
nonexistence theorem. No concrete allowed metric or actual split family
with nonzero block is exhibited. After two unresolved attempts at this
bound, repeating quaternionic orthogonality or quotient differentiation
is parked. A different test varying the coefficient metric while fixing
the actual holomorphic family would need its own source-scope review;
no variation formula, generic nonvanishing or perturbation counterexample
is asserted here. All earlier qualifications, including Z possibly
empty and the pending separate critical audit, remain in force.

**Separate critical audit, 2026-10-23 (step 484).** Reuse the unchanged
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-23-twisted-curvature-criterion-critical-audit.md`.
The precise Demailly Chern/quotient formulas and BGS III comparison
coverage are those cited above and in L148. The verdict is
EXPLORATION / REPRODUCTION: both directions of (2), the coefficient
(3), and the natural central identification (4) survive. No substantive
error, necessary repair or stronger result was found. This verifies
an existing specialization, not progress beyond the sources checked.
L150 is not an input to this audit and its preferred-metric conclusion
is not applied here.

First check the metric being differentiated. With the anti-linear
first-slot convention, the squared norm of j+t v is

\[
 j^*Cj+\bar t\,w^*Bj+t\,j^*B^*w+|t|^2d,
 \qquad d=w^*Aw>0.
\]

Completing the scalar square gives the minimum
j^*(C-B^*ww^*B/d)j. L148's natural chain comparison identifies
precisely this minimum with the actual harmonic norm. It is not a
Schur complement minimizing over the whole two-dimensional P: only
the boundary line Cw is divided out. The chain equation makes
ker d^1=J plus Cw on the whole puncture. Thus (5) uses the entire
closed subspace and its entire boundary, in the extending holomorphic
M-frame. The smooth full metric is positive at the center; L148 gives
uniform bounds for H and its inverse on a smaller punctured ball.

At the center L146 fixes the incoming residues as q_1,q_2. The
linear outgoing functionals are ell_i(c)=T(p_i wedge c). For a
holomorphic J-section j, differentiating rho(j)=0 at zero gives
ell_i(j(0))=0, since rho(0)=0. The two functionals have invertible
restriction to P_z by L146's actual unit test. Hence their common
kernel has dimension 26-2=24 and equals the central J fibre.
These facts prove the precise subspaces in (4), rather than choosing
an unrelated complement. In particular changing higher splitting
coefficients cannot change that kernel or the incoming plane. The
natural central comparison from L148 identifies their product with
the specified twisted harmonic product. No adjoint harmonic metric,
real structure on G, or Serre-to-Hermitian orthogonality is inferred.

For sufficiency, every real partial derivative is allowed, including
mixed ones. If B(0)=0 then u=B^*w has bounds
|u|<=C r^2, |Du|<=C r, |D^2u|<=C. Product differentiation gives
|D^k(uu^*)|<=C r^(4-k) for k=0,1,2. The smooth A and d>=c r^2
give |D^k d|<=C r^(2-k) and
|D^k(d^{-1})|<=C r^(-2-k) in the same range. Thus a term with
i derivatives on uu^* and k-i on d^{-1} is bounded by
C r^(4-i) r^(-2-(k-i))=C r^(2-k). This controls every term in
the second derivatives of (5), on one full ball, not just on rays.
The smooth C contributes bounded derivatives. Consequently partial H
and dbar partial H are bounded. Formula (7), with its two inverse
factors in the quadratic term and uniformly bounded H^{-1}, bounds
all curvature coefficients in the actual bundle and base metrics.
No bound for derivatives of a jumping harmonic projection is used.

For necessity, a constant P-frame change S sends the boundary
coordinates to S^{-1}w. One can choose S so S^*A(0)S=I, and a
constant J-frame change so C(0)=I. The subsequent unitary singular
value changes preserve these identities and the boundary-coordinate
form. All these are holomorphic constant changes, so they preserve
boundedness in the original smooth norms. The Schur complement of
the full central positive matrix is I-B_*^*B_*>0, giving s_1<1.
This is stronger than positivity of the leading quotient alone and
justifies the uniformly bounded H_* inverse used in (10).

Here is a separate check of the differentiated error. Put
delta N=N-N_* and delta d=d-d_*. For k<=2, smoothness gives
D^k delta N=O(r^(3-k)) and D^k delta d=O(r^(3-k)). For example,
every second-derivative term retains either one O(r) coefficient
or one of the remaining coordinate factors; terms with two
derivatives on a smooth coefficient are smaller. Since
d^{-1}-d_*^{-1}=-delta d\,d^{-1}d_*^{-1}, its kth derivative
is O(r^(-1-k)): for derivative orders i,j,l summing to k, the
product bound is r^(3-i)r^(-2-j)r^(-2-l).
The decomposition preceding (11) now gives
D^k(H-H_*)=O(r^(1-k)). Homogeneity bounds D^kH_* by O(r^(-k)).
The algebraic inverse identity gives H^{-1}-H_*^{-1}=O(r);
no derivative of that inverse difference is needed in (7).

Subtract the two curvature formulas term by term. In the linear
second-derivative term the possible bounds are
O(r)O(r^(-2)) or O(1)O(r^(-1)). In the quadratic term, replace
one of its four factors at a time; an inverse difference O(r)
multiplies two first derivatives O(r^(-1)), or a derivative
difference O(1) multiplies one first derivative O(r^(-1)). All
remaining inverse factors are bounded. The same estimates hold if
the other derivative is the full H derivative, since DH=O(r^(-1)).
Thus the complete difference is O(r^(-1)), proving (11) without
omitting any inverse-metric or smooth-coefficient contribution.

Finally set a=1-s_1^2 and c=s_1s_2. At zeta=0 the inverse
two-by-two metric is diag(a^{-1},1). The quadratic term in (7)
has coefficient diag(c^2/a,0), while the second-derivative term
has coefficient diag(s_1^2/a,-s_2^2). Their difference is exactly
(12). Its first entry s_1^2(1-s_2^2)/a is positive for every
s_1>0, including s_2=0. If s_1=s_2>0 the coefficient is
diag(s_1^2,-s_1^2), so trace cancellation does not remove it.
At (r,0), dbar zeta wedge d zeta pulls back to
r^{-2} dbar y wedge dy. A fixed positive leading entry divided by
r^2 dominates the entire O(r^(-1)) error for sufficiently small r.
Uniform equivalence with the original norms converts the divergent
coordinate component into divergent actual curvature norm. This
proves necessity and covers all singular-value cases.

The direct inputs remain L146 and L148, with L071 retained through
them. The audit proves no assertion selecting a block for an arbitrary
metric, nor any preferred-metric curvature application. The weighted
calculation (13)-(14) is outside this criterion-audit target and is
not newly audited. ATTEMPTS/086 remains parked. Empty Z is vacuous;
F and nonempty Z, extension, positivity, split-set control, cycle,
transport and universal primitive Hodge realization remain unresolved.

## Mathlib

Full matching coverage for this actual-family criterion is **not
checked**. The Chern formula and spectral quotient are imported from
the precise sources above and L148; (6)-(12) are their finite matrix
specialization. Unknown coverage is not evidence of absence. No
mathematical script, new general source theorem or originality claim
is needed. The separate critical audit preserves the criterion and
its actual central identification; it adds no Mathlib coverage claim.
