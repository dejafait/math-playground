# L139 — Ordered opposite coincidences from total normalization length

## Hypotheses

Retain L120, L121 and L138's conditional opposite-family setting.
In particular B=S_1 and Y=S_2 are the identical marked smooth
projective complex K3 surfaces of L071/L118, with the common
hyperkähler metric and real product polarization Omega. Suppose F
on B x Y is holomorphic locally free of rank two and
Omega-slope-polystable, with integral c_1(F)=0 and

\[
          \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D,
\]

where e_1=eta tensor 1, e_2=1 tensor eta, integral_S eta=1, and
tau_D is the unchanged full integral self-adjoint mixed tensor.
Use L118's actual charge-21 stable classifying map f:B -> M.
By L120 its original reduced integral image Z has finite
birational unramified normalization nu:B -> Z. By L121,
R_off=(B x_M B)\Delta_B is a finite reduced complex scheme,
possibly empty. Since Z -> M is a closed immersion, the same
fibre product is B x_Z B.

Let Q=nu_*O_B/O_Z and Lambda=length(Q). L138 gives finite
support and a bound using L137's fixed embedding of the original
Z in P^N. Write

\[
 \delta=4k^2\ell^2q(D(H),D(H)),\qquad
 T=\frac{\delta(\delta+1)}2,\qquad
 U=2+\frac\delta2+\frac32\delta^{N-2}T^4,\qquad K=\lfloor U\rfloor.
                                                               \tag{1}
\]

Thus 0<=Lambda<=U. H, ell, k, N and delta are the fixed choices
and parameters of L137/L138, independent of F and of its unknown
image defect. No existence of F or of a collision, image normality,
Cohen--Macaulayness, coherent vanishing or minimal gluing is assumed.

## Conclusion

For every closed z in Z, put r_z=#nu^{-1}(z), and let
lambda_z=length_{O_{Z,z}}(Q_z). There is a natural surjection
of O_{Z,z}-modules

\[
 Q_z\twoheadrightarrow
 \mathbf C^{r_z}/\mathbf C(1,\ldots,1),\qquad
                \lambda_z\geq r_z-1.                         \tag{2}
\]

Let C be the finite set of multiple-fibre values and put
D_0=sum_{z in C}(r_z-1). The total ordered coincidence count P is

\[
 \boxed{\quad
 P=\operatorname{length}_{\mathbf C}(R_{\rm off})
   =\sum_{z\in C}r_z(r_z-1)
   \leq D_0(D_0+1)
   \leq\Lambda(\Lambda+1)
   \leq K(K+1).
 \quad}                                                       \tag{3}
\]

In particular #C<=Lambda and r_z<=Lambda+1 for every closed z.
Empty C gives D_0=P=Lambda=0. The fixed bound K(K+1) meets
the approved ordered-count target, including arbitrary multiple
fibres. It is potentially ineffective through L137's choices,
and is not asserted sharp for the actual geometry.

This conditional ADVANCE / REPRODUCTION specializes known algebra
and elementary finite-sum arithmetic; it makes no originality claim.
The separate critical audit below preserves it. It supplies no contradictory
lower bound, collision existence, F, cycle or transverse transport.
Universal primitive rational Hodge realization remains unresolved.

## Proof

**Scope and imported tools.** The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-20-opposite-coincidence-count-from-total-length.md`.
Its primary coverage is reused unchanged. Import the Chinese
remainder theorem in
[Stacks, Lemma 10.15.4 (00DT)](https://stacks.math.columbia.edu/tag/00DT):
for finitely many pairwise comaximal ideals of a commutative ring,
evaluation onto the product of the quotient rings is surjective.
Distinct maximal ideals satisfy this hypothesis. Import also
[Lemma 10.52.3 (00IV)](https://stacks.math.columbia.edu/tag/00IV),
length additivity in a short exact sequence, and
[Lemma 10.52.6 (00IY)](https://stacks.math.columbia.edu/tag/00IY),
which identifies the length of a module annihilated by a maximal
ideal with its dimension over the residue field. These results have
no dimension-one restriction. We apply them, rather than reprove
them or invoke a curve delta theorem on the surface Z.

L120 supplies the actual finite normalization, L121 the reduced
off-diagonal scheme, and L138 the finite-length and fixed-bound
conclusions. L137's parameters are retained through L138; no new
embedding argument is used. L136's middle Hom sheaf and its Euler
identity are downstream comparisons only, not proof inputs.
The relevant local search found no completed conversion (2)--(3).
ATTEMPTS/070 rejects minimal-defect equality, not the lower bound
in (2). ATTEMPTS/073's vanishing and ATTEMPTS/078's middle-Euler
estimate are not assumed or reopened.

**Actual semilocal residue quotient.** Fix a closed z in Z and set
A=O_{Z,z}, m=m_z and C_z=(nu_*O_B)_z. The subscript distinguishes
this finite A-algebra from the finite set C. Finite surjectivity of
nu gives a nonempty finite fibre, say {b_1,...,b_r}, r=r_z>=1.
Equivalently Spec(C_z) is the finite base change over Spec(A).
Its closed-fibre points give distinct maximal ideals n_1,...,n_r
with residue fields k(b_i)=\mathbf C; the residue field k(z) is
also \mathbf C. Localization at z does not change these fields.
All are the specified complex-algebra residue maps.

The ideals n_i are pairwise comaximal. Applying 00DT to this finite
list gives the surjective evaluation map

\[
     \operatorname{ev}:C_z\longrightarrow
          \prod_{i=1}^r C_z/n_i=\mathbf C^r.                    \tag{4}
\]

This is a residue map from the actual semilocal algebra; no
decomposition of C_z itself as a product of local rings is used.
Each composite A -> C_z -> C_z/n_i is the residue map at z:
the point b_i maps to z and the residue extension is the identity
on \mathbf C. Therefore A acts on the right side of (4) by

\[
       a\cdot(t_1,...,t_r)=\bar a(t_1,...,t_r),
          \qquad \bar a\in A/m=\mathbf C.                     \tag{5}
\]

Evaluation is A-linear for this action, and its image on A is
exactly the diagonal \mathbf C(1,...,1). The inclusion of that
diagonal follows from the residue description; equality follows
since A contains every complex constant. The normalization
inclusion A -> C_z is injective by L120's integral birational
setting. Stalk exactness identifies Q_z with C_z/A. Thus (4)
composed with quotient by diagonal constants factors through the
A-linear surjection in (2). Its target is killed by m and has
complex dimension r-1. By 00IY its A-length is r-1. L138 makes
Q_z finite length, so 00IV applied to this surjection and its
kernel proves lambda_z>=r-1. This also treats r=1, with zero
target; no equality of lengths is inferred.

**All fibre partitions and the ordered scheme count.** By L121 the
set C of values admitting at least two distinct preimages is
finite: it is the image of the finite scheme R_off. Every closed
point of R_off is an ordered pair of distinct complex points in
one such fibre, and each such pair is a closed point of R_off.
L121's reducedness and its residue fields \mathbf C make its
scheme length equal to its number of these ordered pairs. A
fibre of size r_z contributes exactly r_z(r_z-1), with both orders
retained. This proves the equality in (3), rather than identifying
an arbitrary nonreduced coincidence scheme with its point count.

Put d_z=r_z-1>=1 for z in C. Summing (2), and using the
nonnegativity of every other local length, gives

\[
 D_0=\sum_{z\in C}d_z
       \leq\sum_{z\in C}\lambda_z\leq\Lambda.                 \tag{6}
\]

Every term is a nonnegative integer. The identity

\[
 \left(\sum_{z\in C}d_z\right)^2
       -\sum_{z\in C}d_z^2
      =2\sum_{\{z,w\}\subset C,\ z\ne w}d_zd_w\geq0          \tag{7}
\]

where each unordered two-element subset appears once, shows

\[
 P=\sum_{z\in C}(d_z^2+d_z)
       \leq D_0^2+D_0\leq\Lambda^2+\Lambda.                  \tag{8}
\]

The last inequality follows also by subtracting: its difference
is (Lambda-D_0)(Lambda+D_0+1)>=0 by (6). Since Lambda is an
integer and L138 gives Lambda<=U, it is at most K=floor(U).
The same monotonicity gives the last inequality of (3). This is
the desired expression solely in the fixed parameters (1).
Also #C<=D_0<=Lambda, and each r_z-1<=Lambda by (2).
For singleton values the latter bound holds as well. If C is
empty, L138's support containment gives Q=0, hence Lambda=0;
the empty sums in (6)--(8) give D_0=P=0. Thus neither a nonempty
collision set nor a positive normalization defect is being forced.

All fibre sizes and all their partitions are covered by (7);
no numerical sampling or mathematical script is needed. The
continuation test passes without uncontrolled multiplicities or
extra geometry. The inequality is weaker than minimal-gluing
equality and remains consistent with L122's length-four
three-branch example. It provides upper control only. A useful
contradictory lower estimate, F existence, collision existence,
transverse transport and the universal Hodge target remain open.

**Separate critical audit, 2026-10-20 (step 435).** The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-20-opposite-ordered-count-critical-audit.md`.
This is RESEARCH / EXPLORATION / REPRODUCTION, actual task proof_audit:
no substantive error, sharper estimate or existence conclusion was
found. The complete argument above was checked against the applicable
conclusions of audited L120/L121/L138, including L138's finite-support
proof and unchanged fixed-parameter specialization. Their upstream
proofs are not rederived here. The direct inputs remain precisely
L120, L121 and L138.

The primary statements and full proofs of Stacks 00DT, 00IV and 00IY,
linked above, were rechecked in live HTML on 2026-10-20. This verifies
the imports used in this audit; it does not change the saved source
scope or undertake new literature discovery. CRT has no dimension-one
restriction, and the length statements concern modules over the actual
base ring, not lengths over the normalization.

At a closed image point, the finite A-algebra C_z is integral over
the local ring A. Every maximal ideal of C_z therefore contracts to
m; the full list is the closed fibre's r points. The residue fields
are exactly C because the finite fibre is over a closed complex point.
The structure maps are complex-algebra maps, so their residue-field
identifications introduce no automorphisms of C. Distinct maximal
ideals are comaximal, and CRT gives (4) from the uncompleted algebra.
Neither the fibre algebra nor C_z is assumed to split before taking
its residue quotients.

All composites from A are its one residue map. Consequently evaluation
is A-linear for (5), and constants in A make its image exactly the
diagonal, not merely a subspace of it. The diagonal is an A-submodule;
the quotient of C^r by that diagonal is used as a module, not as a
quotient ring. The injective normalization map and exact stalk
functor identify the domain quotient with the actual Q_z. Thus the
induced quotient map is surjective. Its target is killed by m, with
A-length r-1 by 00IY. It is the target, not necessarily Q_z, that is
killed by m. Finite length of Q_z comes from L138, and 00IV applied
to the kernel sequence gives precisely the lower comparison (2).
For r=1 the target is zero; this argument alone does not say Q_z=0.

The fibre products over M and Z agree because the closed immersion
Z -> M is a monomorphism. L121 supplies both finiteness and reducedness
of their off-diagonal part. Its closed points are exactly the ordered
distinct pairs in the same normalization fibre, and each local ring
is C. Thus r(r-1), with no factor of one half or additional local
multiplicity, is the contribution to P. The image set C is finite.
L138 identifies Lambda with the sum of all local A-lengths, so (6)
uses the same length convention as (2).

For the finite list d_z=r_z-1, expansion of the square gives exactly
twice each unordered cross product in (7). All cross products are
nonnegative, including lists of length zero or one. Adding the common
linear sum gives (8). The two subsequent differences are
(Lambda-D_0)(Lambda+D_0+1) and (K-Lambda)(K+Lambda+1);
both are nonnegative once 0<=D_0<=Lambda<=K is checked.
L138 gives Lambda<=U with exactly (1)'s delta, N and T, and integral
Lambda gives Lambda<=floor(U). No parameter depends on the unknown
partition or Q. The floor is a symbolic integer bound; no numerical
choice of ell, k or N has been produced.

If C is empty, vanishing of Lambda uses L138's separately justified
support containment, not the zero-target r=1 residue inequality.
This proves the stated empty case without an extra singleton-fibre
assumption. The bounds on #C and on individual r_z follow from the
same nonnegative sums; singleton values contribute zero.

The audit therefore preserves the conditional upper bound and every
boundary case. ATTEMPTS/070's failure of minimal-defect equality is
untouched, as are ATTEMPTS/073's missing vanishing and ATTEMPTS/078's
uncontrolled middle Euler term. No new DAG edge or argument-assembly
change is required. A contradictory lower bound, F, collisions,
cycles, transverse transport and universal primitive Hodge realization
remain unestablished. Full matching Mathlib coverage remains not checked.

## Mathlib

Full matching coverage for this actual normalization-quotient and
ordered-coincidence specialization is **not checked**. The imported
general tools are the precisely cited Chinese remainder and length
lemmas above. Unknown Mathlib availability is not evidence of
absence. This is an informal proof, not a Lean verification.
