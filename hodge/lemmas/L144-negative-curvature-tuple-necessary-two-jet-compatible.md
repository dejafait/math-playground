# L144 — Negative curvature tuple passes the necessary two-jet test

## Hypotheses

Retain L071/L131's identical marked hyperkähler K3 factors and their
actual product Levi-Civita connection. The conditional global bundle is
locally free of complex rank two, slope-polystable at h_1+h_2, with
integral c_1=0 and ch_2=-14e_1-21e_2-tau_D. L131 supplies its compatible
SU(2) connection if it exists; existence remains hypothetical.

At a prospective point use L143's ordered orthonormal quaternion frames
and su(2) basis, with [T_1,T_2]=2T_3 and cyclic versions. Fix exactly
its negative tuple

\[
P=2T_3M_1,\qquad Q=T_3M_1,\qquad
K_m=T_1M_0+T_2M_1,\qquad R^0=P+K_m+Q.                 \tag{1}
\]

Here M_0=1, M_1,M_2,M_3 are the skew matrices in L143 (6), with
M_3=M_1M_2. The mixed block is R^0_{a,4+mu}=(K_m)_{a,mu}, and its
transpose block is negative. In all formulas below indices run from
0 to 7, with 0,...,3 in the first factor.

The base curvature is the actual R^g at that point, with convention
R^g(u,v)=[nabla^g_u,nabla^g_v]-nabla^g_[u,v]. Keep both factor blocks;
their values are not known or assigned here. The problem is only the
existence of prospective real tensors U=nabla R and V=nabla^2 R with
the curvature-slot quaternionic type, Bianchi, its first derivative,
and the full Ricci commutator. No sufficiency theorem for these tensor
conditions is assumed.

## Conclusion

For **every** pair of hyperkähler algebraic base-curvature blocks there
are such U,V. One can take U=0 and V affine, with rational coefficients,
in all ten base-curvature parameters. There is no residual restriction
on those parameters. The construction has nonzero second derivatives;
in particular

\[
\sum_i V_{ii;a\mu}=-4(K_m)_{a\mu}.                    \tag{2}
\]

The upper-derivative-pair system has rank 255 among 360 unknowns per
su(2) coordinate, leaving 105 free dimensions per coordinate. An exact
affine witness, its construction and complete checks are recorded below.
Thus this bounded necessary two-jet mechanism cannot exclude (1), even
at the fixed K3 metric. This is an informative NEGATIVE / REPRODUCTION
specialization of the assessed identities, with no originality claim.
The separate step-459 critical audit below preserves this verdict.

This does not produce an actual curvature jet of an SU(2) instanton,
a local connection, a global F, or a cycle. It does not reverse L143's
pointwise sign stop or establish a higher-order compatibility theorem.
Universal primitive rational Hodge realization remains unresolved.

## Proof

**Imported identities and conventions.** Import Janyška, *On the
curvature of tensor product connections and covariant differentials*,
[arXiv:math/0304042v1](https://arxiv.org/pdf/math/0304042v1), Proposition
3.3, Theorems 4.6–4.7 and Example 4.9, PDF pp. 6–8. The connection is
smooth, the base connection torsion-free, and the coupled tensor
connection acts on End(F) and both curvature covectors. In the stated
unnormalized commutator convention its necessary equations are

\[
\begin{split}
 U_{j;ab}+U_{a;bj}+U_{b;ja}&=0,\\
 V_{ij;ab}+V_{ia;bj}+V_{ib;ja}&=0,                       \tag{3}\\
 V_{ij;ab}-V_{ji;ab}=W_{ij;ab}
 &:=[R^0_{ij},R^0_{ab}]
 -\sum_c (R^g_{ij})^c{}_a R^0_{cb}
 -\sum_c (R^g_{ij})^c{}_b R^0_{ac}.                    \tag{4}
\end{split}
\]

Thus V_{ij;ab} differentiates first in the j slot and then in the i
slot, including the connection correction on the derivative covector.
Example 4.9's normalized Alt factor is not inserted into (4). Its two
negative terms are precisely the two covector actions, not a Ricci-only
replacement. These are imported identities, not a reproof of the general
theorem. Janyška's unrestricted realization results are not used.

**All base parameters.** In either oriented four-frame, the three
parallel Kähler forms are self-dual and their skew endomorphisms are
left multiplication by i,j,k. Hyperkähler curvature commutes with all
three, so its skew endomorphism values lie in span(M_1,M_2,M_3).
Pair symmetry of R^g then puts both two-form factors in that span and
makes its coefficient matrix symmetric. First algebraic Bianchi is
exactly its trace-zero condition: the M_k are orthogonal ASD forms and
M_k wedge M_l=-2 delta_kl vol. Hence every actual factor tensor has
the form

\[
(R^g_{ij})^c{}_a=\sum_{k,l=1}^3 H_{kl}(M_k)_{ij}(M_l)_{ca},
\qquad H=H^t,\quad\operatorname{tr}H=0.               \tag{5}
\]

This defines H with the chosen curvature sign and basis normalization;
no claim about its numerical value is made. Use the ordered basis

\[
\operatorname{diag}(1,-1,0),\quad
\operatorname{diag}(0,1,-1),\quad
E_{12}+E_{21},\quad E_{13}+E_{31},\quad E_{23}+E_{32}.   \tag{6}
\]

Use it independently on the two factors, with all mixed product-base
curvatures zero. This retains every actual possibility as a value of
ten real parameters z_1,...,z_10; it does not choose those values.
The exact checks also verify pair/skew symmetries, all first algebraic
Bianchi components, Ricci-flatness and quaternionic commutation for
each of the ten spanning tensors. No derivative of R^g enters (4).

**Finite system and exact witness.** Let B_0,...,B_9 be the invariant
eight-by-eight skew matrices obtained by putting M_1,M_2,M_3 in the
first pure block, then in the second pure block, then M_0,...,M_3 in
the upper mixed block with negative transpose below. L143 proves this
is the entire invariant two-form space; none of the pure blocks is
discarded. Choose U=0 as a prospective tensor. It satisfies its type,
reality and first Bianchi requirements. This choice does not assign the
derivative of an existing connection and does not set V=0.

For each i<=j introduce unknown coefficients x_{ij,t} in su(2) and set

\[
 V_{ij;ab}=\sum_{t=0}^9 x_{ij,t}(B_t)_{ab} \quad(i\le j),\qquad
 V_{ij;ab}=V_{ji;ab}+W_{ij;ab} \quad(i>j).             \tag{7}
\]

Equation (4) and curvature-slot skew symmetry are then automatic.
The right side W also has the invariant type: the coefficient action
does not alter form slots, and R^g_{ij} commutes with the parallel
quaternionic structures. This is checked coefficientwise for the
constructed W as well. There is no imposed type on the derivative
slots.

It remains to impose (3). For every i=0,...,7 and every increasing
triple j<a<b, substitute (7) into
V_{ij;ab}+V_{ia;bj}+V_{ib;ja}=0. This gives 8 binom(8,3)=448 rows
in 36 times 10=360 unknowns per su(2) coordinate. The matrix is the
same in each coordinate. The right side is affine in z and the fixed
coefficient brackets. Thus 33 rational right-hand columns suffice:
eleven affine coefficients for each of three su(2) coordinates.

Here is an exact, deterministic construction of a witness, including
the elimination prescription so that it is reproducible independently
of the saved values. Order unknowns lexicographically as (i,j,t) with
i<=j. Order rows as i and then the increasing triple (j,a,b).
For each row eliminate its smallest nonzero column using the previously
normalized pivot there; if none exists divide by that column's value
and save the row as its pivot. Apply the identical rational operations
to all 33 right-hand columns. A row with zero unknown part has zero
right-hand part in all 33 columns. There are exactly 255 pivots.
Set every nonpivot unknown to zero and solve the pivot equations in
decreasing pivot order. These instructions, (1), (4)–(7), and the
ordering specify the witness completely, without numerical tolerance
or choices of real base values.

The full witness is saved as `solution` and, equivalently, as
`solution_sparse` in
`scripts/curvature-two-jet/fixed_tuple_certificate.json`.
In the sparse field an outer key i,j,t and inner key c,h give the
coefficient of T_(c+1) z_h in x_{ij,t}, where z_0=1 and h=1,...,10
follow (6), first factor then second. All omitted entries are zero.
The 218 nonzero scalars are integers of absolute value at most eight;
there are 136 nonzero x rows. Dense and sparse forms agree in all
11880 scalar entries. `elimination_trace` retains the row operations;
`nonzero_residual_conditions` is empty. The denominators are all one.

**Complete exact verification.** The reproduction command is
`python3 scripts/curvature-two-jet/check_fixed_tuple.py`. The script is
part of this finite computation proof: it constructs the bases and
R^0, constructs both complete base-curvature blocks, performs the
rational elimination just specified, reconstructs all V by (7), and
checks every original equation. In particular it does not merely test
the reduced pivot rows or parameter samples. For all 8^4 index choices
and all 33 affine columns it checks differentiated Bianchi, the full
Ricci commutator, curvature-slot skew symmetry, and quaternionic type
under each of I,J,K. It separately checks every original linear row.
Every comparison is equality of exact rational integers/fractions.
The complete basis and tensor checks pass: 14/14 aggregate checks,
with no failures and no residual conditions. These are finite
coefficientwise identities, not numerical evidence for an infinite
parameter assertion. Evaluation of the affine witness at the actual
two K3 curvature blocks therefore gives real U,V satisfying all the
required identities, without knowing those values.

As an additional convention check, differentiated Yang–Mills divergence
sum_j V_{ij;jb}=0 holds in every component. It also follows from the
primitive quaternionic type and (3), but is checked directly. Using
this divergence and (3), commute the two derivative slots to obtain

\[
\sum_i V_{ii;ab}=-\sum_i W_{ia;bi}-\sum_i W_{ib;ia}.   \tag{8}
\]

For mixed output, the base terms in (8) are Ricci contractions or
mixed product-base terms and vanish, as in L143. Its coefficient
part is -2 sum_i[R^0_{ai},R^0_{ib}], exactly L143's C. The tuple (1)
has C=-4K_m; direct verification checks all sixteen mixed components
in every affine column, proving (2). Thus nabla* nabla K_m=+4K_m
at this prospective jet and C=-4K_m, consistent with the same signed
Weitzenböck equation. In particular V is not zero. Pairing gives
the original pointwise coupling -32 and mixed norm squared eight;
no integrated norm or global realization is inferred.

**Scope of the negative conclusion.** The necessary conditions now
have a witness for every actual base value, so unavailable K3 point
values are not a blocker for this bounded test. The result is stronger
than existence after freely choosing a favorable base tensor, and
weaker than prescribed quaternionic SU(2) jet realization. No higher
prolongation, formal sufficiency, prepotential interpolation or global
Hodge argument is supplied. ATTEMPTS/083–084 remain valid stops for
their different mechanisms. The present result parks only this exact
finite-order exclusion route.

**Independent critical audit (2026-10-21, step 459).** The approved
SPECIALIZE audit preserves the statement without a substantive correction
or stronger conclusion. This is EXPLORATION / REPRODUCTION, not a second
NEGATIVE, a new mathematical discovery, or a realization theorem.

The source-to-equation translation was checked against Janyška's
Definitions 1.3/1.5, Proposition 3.3, Definition 4.1, Corollary 4.5,
Theorems 4.6–4.7 and Examples 4.8–4.9 in the cited v1, PDF pp. 2,6–8.
Writing the source's splitting coefficient matrices as K_i, its
covariant derivative is partial_i-K_i. Its curvature component formula
therefore equals the unnormalized commutator curvature of this
derivative. Successively appended source derivative slots (j,i) mean
outer derivative i and inner derivative j, as in V here. Antisymmetrizing
in the source's appended order accounts for the minus sign and normalized
one-half; reversing the derivative order to V_ij-V_ji gives (4).
Proposition 3.3 and Example 4.9 retain both dual-slot actions. The
interchanged connection labels printed in Theorem 4.7 do not enter this
translation. This imports the stated identities, not unrestricted
curvature-jet surjectivity.

More explicitly, with D denoting the connection on End(F)-valued
two-forms and Gamma the ordinary Levi-Civita coefficients, the tensor
represented by V is D_i(D_j R)-Gamma^k_ij D_k R. This retains the
derivative-covector correction. Torsion-freeness makes that correction
symmetric in i,j; the induced curvature acts on End(F) by [R_ij,-]
and on each covector by its negative action. Differentiating the actual
three-tensor Bianchi identity gives precisely the second equation (3).
Parallelness of I,J,K differentiates only the curvature-slot type
condition; it does not impose invariance on a derivative slot. Thus no
extra derivative-slot type or discarded covector action enters the test.

The completeness assertions were checked separately from substitution.
For an invariant skew operator on H direct sum H, its two diagonal
blocks are skew operators commuting with left quaternion multiplication;
each is an imaginary right quaternion, of dimension three. The upper
off-diagonal block is any right quaternion, of dimension four, and
skewness determines the lower block. A commuting real-linear map on H
is determined by its value at 1. This proves that the ten B_t span the
entire invariant module, and their Gram diagonal (4 six times, then 8
four times) proves independence in the displayed ordered-entry pairing.

For a hyperkähler four-factor, the curvature endomorphisms commute with
the three parallel left multiplications, so the output two-form space
is the same three-dimensional ASD space. Riemann pair symmetry puts
the input two-form space there as well and makes H symmetric. In
dimension four the Bianchi alternation of a symmetric two-form-pair
tensor is its wedge contraction. Here M_k wedge M_l is
-2 delta_kl vol, so its vanishing is exactly trace(H)=0. Consequently
(6) spans all five possibilities, with no missing self-dual, scalar,
Ricci or cross-factor block. This agrees with the standard curvature
decomposition of LeBrun, *Curvature and Smooth Topology in Dimension
Four*, Séminaires et Congrès 4 (2000),
[section 1, p. 180, unnumbered display following (1)](https://smf.emath.fr/sites/default/files/2026-04/smf_sem-cong_4_179-200__sample.pdf#page=2),
and the scalar-flat Kähler Weyl specialization in his *Einstein
Manifolds, Self-Dual Weyl Curvature, & Conformally Kähler Geometry*,
[18 April 2023, PDF pp. 193–194](https://www.math.stonybrook.edu/~claude/UF23.pdf#page=193). The primary passages
and URLs are recorded in the approved critical-audit assessment. This
is a covering argument for actual point values, not their realization
or free assignment on the fixed K3 metric.

An independent verifier is
`python3 scripts/curvature-two-jet/audit_fixed_tuple.py`; its full
certificate is `scripts/curvature-two-jet/fixed_tuple_audit_certificate.json`.
It does not import or run the original solver. It constructs left and
right quaternion multiplication from the quaternion multiplication
table, uses the faithful four-real-dimensional coefficient matrices
with pairing -trace/4 to compute every bracket, and constructs the two
base-curvature actions as full matrix actions on two-forms. These are
the same normalized su(2) brackets as the two-complex-dimensional
matrices above. The verifier reads **every** saved dense and sparse
coefficient and checks their agreement, rather than inferring validity
from the preview, summary flags or a repeated reduced matrix.

All 11880 dense scalar entries agree with the sparse encoding. The
218 nonzero entries occupy 136 unknown rows, are integral and have
absolute value at most eight. Parameter and unknown orderings agree.
Reconstruction evaluates all 33 affine columns over Python arbitrary
precision integers. Curvature skewness, all three type identities,
the complete differentiated Bianchi and Ricci equations, differentiated
Yang–Mills divergence, and the contracted identity (8) have exactly
zero residual. In particular each of the full Bianchi and Ricci tests
checks 8^4 times 33 = 135168 scalar entries. Each of the 448 original
linear rows is also independently checked in all 33 columns. The ten
base tensors pass all skew, pair, first-Bianchi, Ricci and quaternionic
commutation checks. The audit certificate records counts, maximum
residuals and all nonzero residual entries (none), not sampled base
values. Its 481 aggregate checks pass with no failures.

The homogeneous rank was verified separately by exact Fraction
elimination of the reconstructed matrix, processing rows in reverse
order and taking the largest available column as pivot, independently
of the original smallest-column forward algorithm. There are 255
pivots; every zero coefficient row has zero augmented entries in all
33 columns. Hence the nullity is 360-255=105 per su(2) coordinate.
This rank computation is additional information: the direct full tensor
substitution already proves existence of the affine witness. The
original reproducer was also run once and passed all 14 of its checks;
the original certificate is retained byte-for-byte (its regenerated
sparse-field serialization order was restored).

Finally, the audit sums the full W expression in (8), before taking
mixed components. All base-parameter coefficients cancel in that
mixed contraction. Its constant part is exactly -4K_m, and the actual
contracted pairing is -32 at mixed norm squared eight. Thus V is
necessarily nonzero for this witness despite U=0. The derivative-zero
choice concerns a prospective first jet at one point, not a parallel
connection. Both signs of the rough-Laplacian comparison in L143 are
retained. No missing metric value or residual parameter condition was
found. ATTEMPTS/085 therefore remains parked; higher compatibility,
SU(2) jet sufficiency, local/global realization, F and transport all
remain unproved.

## Mathlib

Full matching coverage for this prescribed real quaternionic
curvature-two-jet feasibility statement has not been checked.
Supporting connection or Bianchi APIs would not establish the finite
specialization. Unknown availability is not evidence of absence;
no Lean verification is claimed.
