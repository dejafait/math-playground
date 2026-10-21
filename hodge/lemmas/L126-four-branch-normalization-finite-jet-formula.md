# L126 — Four-branch normalization length from the full second jet

## Hypotheses

Retain the conditional setting of L118, L120 and L121. Thus
X=B x Y=S_1 x S_2 consists of the identical marked projective complex
K3 surfaces, with common hyperkähler metric g, ordered structures I,J,K,
real ample class h and Omega=p_1^*h+p_2^*h. Normalize the point class
by integral_S eta=1 and put e_1=eta tensor 1, e_2=1 tensor eta.
The full integral mixed tensor tau_D has self-adjoint cup operator D,
D[sigma]=2lambda[sigma], sigma=omega_J+i omega_K, and 1<lambda<5/4.
Suppose F is holomorphic locally free of rank two, Omega-slope-polystable,
with integral c_1(F)=0 and

\[
             \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Use L118's actual opposite stable classifying map f:B -> M, where
M=M_H^s(2,0,-19), with its natural differential and compatible local
hyperkähler connection-moduli chart. Its normalized metric pullback is
2lambda g. By L120, f identifies B with the finite normalization nu:B -> Z
of its integral reduced scheme-theoretic image. By L121, tangent
quaternionic lines at distinct preimages are distinct and intersect only
at zero.

Let z in Z have exactly four distinct preimages b_1,...,b_4. Suppose
their tangent quaternionic lines span quaternionic dimension two in
T_zM, whose quaternionic dimension is 39 and complex dimension is 78.
Fix I and write V=T_zM, U for this common complex four-dimensional span,
and V_i=T_{b_i}B as complex two-dimensional spaces. Write L_i:V_i -> V
for the injective differentials and identify their images with subspaces
of U. All nonlinear normal jets of the actual branches are retained.
No simultaneous linearization, generic tangent configuration or occurrence
of this collision is assumed.

## Conclusion

Choose ambient and branch formal coordinates with the specified tangent
bases, and write the branch maps through order two as

\[
             f_i(u)=L_i u+Q_i(u)+O(|u|^3),
\]

where Q_i is a V-valued homogeneous quadratic polynomial; it includes
every ambient coordinate, including the 74 coordinates normal to U.
Set

\[
 W_2=\bigoplus_{i=1}^4\operatorname{Sym}^2 V_i^*,\qquad
 E_2=\operatorname{im}\left(
  \operatorname{Sym}^2 U^*\longrightarrow W_2,\quad
  P\longmapsto(P(L_i u))_i\right),\qquad C_2=W_2/E_2.
\]

For U^ann={ell in V^*: ell|_U=0}, define

\[
 \overline N:U^{\rm ann}\longrightarrow C_2,\qquad
 \ell\longmapsto[(\ell(Q_i(u)))_{i=1}^4],\qquad
 s=\operatorname{rank}\overline N.                         \tag{1}
\]

Then the actual algebraic normalization quotient satisfies

\[
 \boxed{\ \operatorname{length}_{\mathcal O_{Z,z}}
     ((\nu_*\mathcal O_B)_z/\mathcal O_{Z,z})
          =7+\dim C_2-s=19-\dim E_2-s.\ }                 \tag{2}
\]

It is annihilated by the cube of the maximal ideal. No branch terms of
degree at least three affect this formula.

More explicitly, quaternionic linear changes put the four tangent
inclusions into the form

\[
 (u,0),\quad(0,u),\quad(u,u),\quad(u,Au)
                 \quad\hbox{in }U=\mathbf C^2_x\oplus\mathbf C^2_y,
                                                               \tag{3}
\]

where A is a quaternionic-linear automorphism and A-id is invertible.
There are exactly two tangent-rank cases:

\[
 \begin{array}{c|c|c|c}
 A&\dim E_2&\dim C_2&\text{length in (2)}\\ \hline
 t\,\mathrm{id},\ t\in\mathbf R\setminus\{0,1\}&9&3&10-s,\quad0\le s\le3\\
 A\text{ not scalar}&10&2&9-s,\quad0\le s\le2.
 \end{array}                                                \tag{4}
\]

In particular 7<=length<=10. The rank s is determined by the full
normal second jets modulo the tangent quadratic image. Arbitrary smooth
complex branch maps with the same quaternionic tangent configuration
can have different s. The examples below establish this only for that
local-algebra relaxation; they are not actual quaternionic totally
geodesic K3 branches. The rank of (1) for an actual collision is not
evaluated here, and the bounds need not be sharp under its additional
geodesy and global hypotheses.

This is a conditional REPRODUCTION/specialization of assessed tools.
The separate critical audit below preserves the formula. It supplies a finite local gluing
criterion, not F existence, collision occurrence, a global defect
exclusion, a cycle or transverse transport. The universal primitive
Hodge-realization gap is unchanged.

## Proof

**Coverage and imports.** The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-18-actual-four-branch-normalization-jets.md`.
It covers the complete tail and full second-jet specialization, with
arbitrary nonlinear normal coefficients. Its local duplicate/failure
comparison and the scoped checks of L122/L125 and ATTEMPTS/070--072 are
reused. Their three-branch numbers and curvature tests are not inputs.

Import Derksen--Sidman, *A sharp bound for the Castelnuovo--Mumford
regularity of subspace arrangements*, Advances in Mathematics 172
(2002), 151--157, Theorems 2.1 and 1.2, printed pp. 153--154
([author-hosted paper](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.10.pdf)):
the intersection ideal for d projective linear spaces is d-regular;
in particular H^i(I(k))=0 for i>=1 and k+i>=d. No genericity is required.
The assessment inspected these statements and the complete Section 2
proof. The specialization below concerns four projective lines.

Import Wen-Wei Li, *Yanqi Lake Lectures on Algebra, Part 3*, version
2026-07-05, Lemma 5.2.3, printed p. 53
([PDF p. 58](https://www.wwli.asia/downloads/YAlg3.pdf#page=58)):
a filtration-preserving map with complete source, Hausdorff exhaustive
target and surjective associated graded is surjective. Use also
[Stacks Lemma 10.97.1, 00MA](https://stacks.math.columbia.edu/tag/00MA)
(exact finite-module completion),
[Lemma 10.97.8, 07N9](https://stacks.math.columbia.edu/tag/07N9)
(finite-algebra product completion),
[Lemma 10.97.3, 00MC](https://stacks.math.columbia.edu/tag/00MC)
(faithfully flat local completion),
[Lemma 10.160.10(2), 0C0S](https://stacks.math.columbia.edu/tag/0C0S)
(formal coordinates with the given residue coefficient field), and
[Lemma 10.52.13, 02M1](https://stacks.math.columbia.edu/tag/02M1)
(flat-local length comparison). Their primary hypotheses and relevant
proofs were inspected in the reused assessments. No general theorem
is reproved; the necessary restriction-rank specialization follows.
The generic quadratic-arrangement theorem and curve-parametrization
determinacy are deliberately not imported.

**The actual completed cokernel.** Put R=O_{M,z}, A=O_{Z,z} and
T=(nu_*O_B)_z. The scheme-theoretic image gives a surjection R -> A
and an injection A -> T. All are finite R-modules: A is a quotient
and T is finite over A by L120. Thus exact completion of both maps
and of 0 -> A -> T -> Q_z -> 0 identifies

\[
 \widehat Q_z=\operatorname{coker}\left(
 \rho:\widehat R\longrightarrow\widehat T\right),\qquad
 \operatorname{im}\rho=\widehat A.                         \tag{5}
\]

Completion over R and over A agrees on these modules, since m_R maps
onto m_A. The four maximal ideals of the finite semilocal algebra T
over m_A correspond exactly to the four assumed preimages. By 07N9
and smoothness of B and the ambient germ, 0C0S gives

\[
 \widehat R=\mathbf C[[z_1,\ldots,z_{78}]],\qquad
 \widehat T=\prod_{i=1}^4 T_i,\qquad
 T_i=\mathbf C[[u_{i1},u_{i2}]].                           \tag{6}
\]

Here rho is the actual completed branch pullback, and its linear and
quadratic terms are L_i and Q_i. This does not assert that normalization
commutes with completion. Let m=(z_1,...,z_78) and n_i=(u_i1,u_i2).

**The whole cubic tail.** Projectivizing L_i(V_i) gives four pairwise
disjoint projective lines in P(U)=P^3, because the vector spaces have
zero pairwise intersection. Let Lambda be their reduced union and
I_Lambda its ideal sheaf. For every d>=3 the cited regularity theorem
gives H^1(P^3,I_Lambda(d))=0. The ideal-sheaf exact sequence therefore
makes

\[
 \operatorname{Sym}^d U^*\longrightarrow
 H^0(\Lambda,O_\Lambda(d))
   =\bigoplus_{i=1}^4\operatorname{Sym}^d V_i^*             \tag{7}
\]

surjective. The equality uses the disjoint projective union, with no
general-position assumption. A linear splitting V=U plus a complement
extends every polynomial on U to V, so restrictions from Sym^d V^*
are surjective as well.

Apply Li's lemma to rho restricted to

\[
     m^3\longrightarrow J_3:=\prod_i n_i^3
\]

with filtrations F^k(m^3)=m^{k+3} and
F^k J_3=product_i n_i^{k+3} for k>=0, and the full modules for k<=0.
The source is a closed ideal in a complete power-series ring, hence
complete for this filtration; the target is complete, Hausdorff and
exhaustively filtered. They are modules over widehat R via rho and
the map preserves the filtrations. Its degree d=k+3 graded map is the
tangent restriction in (7): substituting a nonlinear branch correction
into a homogeneous degree-d term changes it only in order at least
d+1. This checks every d>=3, including monomials in all ambient normal
coordinates. Consequently

\[
                      \rho(m^3)=J_3.                    \tag{8}
\]

This is a complete formal lifting statement, not a finite-jet
extrapolation or an assertion of strictness of the original image map.

**The exact finite map, with its off-diagonal block.** By (8) the
cokernel in (5) is the cokernel after reducing each branch modulo n_i^3.
This target is a complex vector space of dimension
4(1+2+3)=24. Ambient terms of order at least three map to zero, so the
full remaining map has source

\[
 \mathbf C\oplus V^*\oplus\operatorname{Sym}^2 V^*.
\]

For (c,ell,P) its i-th entry, separated by homogeneous branch degree, is

\[
       \big(c,\ \ell(L_i u),\ \ell(Q_i(u))+P(L_i u)\big).   \tag{9}
\]

The constant image has dimension one. The linear map
L:V^* -> direct_sum_i V_i^*, ell -> (ell L_i)_i, has kernel U^ann
and rank four, since U is the span of the four images. The pure
quadratic ambient part has image E_2; every quadratic on U extends to V.

Project the image of (9) onto its constant and linear components. This
projection has rank 1+4. Its kernel inside the image consists exactly
of the quadratic tuples

\[
             E_2+\{(\ell Q_i)_i:\ell\in U^{\rm ann}\}.
\]

Indeed zero constant and linear output forces c=0 and ell in ker L;
conversely each such tuple occurs. Thus the full image rank is
1+4+dim E_2+s. This proves (2) for widehat Q_z, without replacing
the full jet image by its associated graded. In particular quadratic
terms of a linear form with nonzero linear output do not add an extra
free quadratic rank; the kernel condition in (1) is essential.

**The two tangent ranks.** The first two quaternionic lines are a
direct sum. Each projection of the third line is a quaternionic-linear
isomorphism, since its kernel would be its intersection with another
line. Transport a basis through these projections, putting the third
line on the diagonal. The fourth line projects isomorphically to each
axis as well, so it is the graph of a quaternionic-linear A. Its zero
intersection with the diagonal says A-id is invertible. This proves
(3), with A invertible, while retaining the entire nonlinear maps.

A homogeneous quadratic on U vanishing on both axes is x^T B y for
a complex 2-by-2 matrix B. Vanishing also on the diagonal is the
identity u^T B u=0. In characteristic zero this says B is alternating.
Thus the quadrics vanishing on the first three planes are precisely
the multiples of

\[
                       q(x,y)=x_1y_2-x_2y_1.
\]

Its fourth restriction is det(u,Au). For
A=[[a,b],[c,d]], this polynomial is
c u_1^2+(d-a)u_1u_2-b u_2^2. It vanishes identically exactly when
b=c=0 and d=a, that is, A is complex scalar. A complex scalar
commutes with the anti-complex structure J exactly when it is real:
J(a u)=bar(a)J(u). Since A is quaternionic-linear, the scalar cases
are precisely real t not equal to zero or one. Finally dim Sym^2 U^*=10.
The kernel of its restriction to all four planes has dimension one
in that case and zero otherwise. This proves every rank in (4),
and then the displayed length bounds.

**Coordinate independence and a discriminating normal-jet test.** The
formula already computes the actual cokernel, so its total rank is
independent of coordinates. More explicitly, a quadratic branch
reparametrization changes Q_i by L_i times a quadratic vector, which
is killed by ell in U^ann. A quadratic ambient coordinate change adds
to ell(Q_i) the restriction of one common ambient quadratic, hence an
element of E_2. Linear coordinate changes just identify the spaces
in (1). Thus s is well-defined up to the resulting vector-space
identifications and no artificial freedom was introduced by choosing
formal parameters.

For a concrete test keep (3) with A=2 id. Use ambient coordinates
(x,y,w_1,...,w_74). Take the first three branch maps to be exactly
(u,0,0), (0,u,0), (u,u,0), and the fourth to be

\[
             (u,2u,q_1(u),\ldots,q_k(u),0,\ldots,0),
                                                               \tag{10}
\]

where k is any of 0,1,2,3 and q_1,...,q_k are linearly independent
members of {u_1^2,u_1u_2,u_2^2}. These are smooth complex branch
embeddings with identical specified quaternionic tangents for every k.
In this scalar case the restriction to the first three planes has
rank nine: its kernel is the one-dimensional span of q(x,y), by the
calculation just made. The restriction to all four has rank nine too,
with the same kernel. Hence projection from E_2 to the first three
quadratic factors is an isomorphism. The fourth-only quadratic factor
therefore intersects E_2 trivially and maps isomorphically to C_2.
The k normal coordinates in (10) supply k independent elements of this
factor; all other normal restrictions vanish. Thus s=k and the formal
restriction cokernel has dimension 10-k, realizing 10,9,8,7.
Equation (8) applies to each full formal map in this test, so this is
an entire cokernel calculation, not only a leading-jet preview.

These examples test dependence on arbitrary smooth complex branch
jets. They do not satisfy or purport to satisfy the actual geodesy,
global K3 normalization or F hypotheses. In particular they do not
prove that an actual collision has variable length or that its s can
be prescribed. Additional constraints on actual Q_i must be justified
separately; no conclusion about their rank is assumed here.

**Algebraic descent and scope.** If a is in m_{widehat A}, each of
its four branch images vanishes to order at least one. Therefore
m_{widehat A}^3 widehat T is contained in J_3, which is in widehat A
by (8). It follows that m_{widehat A}^3 widehat Q_z=0. Exact completion
identifies widehat Q_z with Q_z tensor_A widehat A; faithful flatness
then gives m_A^3 Q_z=0. The original finite module Q_z has finite
length. Local completion has closed fibre C of length one, so 02M1
identifies its length with the computed complex dimension of widehat Q_z.
This proves (2) for the actual algebraic quotient.

The direct local inputs are L118, L120 and L121. The argument extends
the available gluing bookkeeping to four preimages without a generic
rank assumption, an analytic convergence claim, simultaneous branch
linearization, or use of curve conductor bounds for surfaces. It does
not evaluate actual normal second jets using geodesy, exclude the
collision, compute a global quotient, or construct F. The independent
curvature stops in ATTEMPTS/071--072 remain unchanged. No algebraic
Hodge class or transport is supplied.

**Separate critical audit, 2026-10-18 (step 379).** This audit uses the
pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-18-four-branch-finite-jet-critical-audit.md`.
It checks the formula under the stated conditional geometric inputs;
it does not re-audit their earlier proofs or evaluate actual geodesic
normal jets. The original argument above survives without a substantive
repair. The following are the complete load-bearing checks.

1. **Actual image and four factors.** The point z is a closed complex
   point in L118's smooth ambient germ of dimension 78. Its local ring
   R is Noetherian and regular. The closed image supplies R -> A
   surjective, and L120 supplies A -> T injective and T finite over A.
   Thus A, T and T/A are finite R-modules. Applying 00MA to these
   actual maps identifies the image with the completed A, not an
   abstract subring having the same jets. The maximal ideals of T
   correspond to precisely the four b_i. The local factors in 07N9
   are completions of O_{B,b_i}; their residue field is C and each is
   regular of dimension two. Consequently (6) has exactly four
   power-series factors. The base maximal ideal and the semilocal
   branch ideals have the equivalent completion topologies supplied
   by 07N9. No normalization/base-change commutation is needed.

2. **Every degree of the tail.** L121 and the span-two hypothesis
   give four disjoint projective lines in P^3. The cited four-regularity
   yields H^1(I_Lambda(d))=0 whenever d+1>=4. In particular the
   borderline d=3 is included, as is every larger degree. Since the
   lines are disjoint, their section space is the direct sum in (7),
   and the exact restriction sequence gives its surjection from
   Sym^d U^*. The same holds from V by linear extension. For the
   shifted filtration on m^3 and J_3, the degree-k graded map is
   exactly this map with d=k+3: any occurrence of a quadratic or
   higher term of f_i raises the branch order. For negative k both
   graded pieces are zero. Each source filtration term is a closed
   ideal in the complete power-series ring; the source is complete
   and the branch target is Hausdorff and exhaustive. One may apply
   Li 5.2.3 simply as a filtered C-linear module map, avoiding any
   need to identify branch-order filtration with the intrinsic
   A-adic filtration. It proves equality (8), including all ambient
   normal coefficients. No strictness assertion for rho is used.

3. **Full finite image.** After removing J_3, the target has dimension
   24. Its constant and linear spaces have dimensions 4 and 8.
   Equation (9) includes every term of order at most two. Projection
   of its image to those two spaces has rank 1+4=5. Vanishing of
   that projection forces c=0 and ell|_U=0; a quadratic source term
   has no linear output and cannot cancel a nonzero one. Therefore
   the pure quadratic kernel has dimension dim E_2+s, exactly as
   in (1). Rank-nullity gives 24-5-dim E_2-s, or
   7+dim C_2-s. In particular this is not the cokernel of a
   block-diagonal associated-graded approximation. The contributions
   3 from constants and 4 from linear degree explain the lower bound
   seven; the remaining nonnegative dimension is dim C_2-s.

4. **Both tangent cases without genericity.** The first two
   quaternionic lines give a direct sum and all projections of either
   remaining line onto an axis are isomorphisms. Choosing the third
   line as the diagonal therefore puts the fourth in graph form,
   with both A and A-id invertible. An axis-vanishing quadratic is
   x^T B y; diagonal vanishing makes B alternating, leaving exactly
   one possible kernel vector. Its fourth restriction has the three
   coefficients c, d-a and -b displayed above. All vanish precisely
   for a complex-scalar A. Commutation with the anti-complex J then
   forces that scalar to be real. Hence the kernel dimensions are
   one and zero, and the image dimensions are nine and ten in every
   allowed configuration. Subtracting from dim W_2=12 gives exactly
   the two rows of (4); there is no third rank case.

5. **Coordinate invariance and relaxed examples.** Changes with fixed
   first derivative act on the quadratic jet by an ambient common
   quadratic restriction and a branchwise vector in im L_i. The
   former disappears in C_2 and U^ann kills the latter. Invertible
   linear changes identify all spaces and preserve ranks. Thus s
   is coordinate-independent for the given map. In (10), the
   restriction E_2 -> the first three quadratic factors is both
   injective and surjective, since both spaces have dimension nine
   and the first-three and all-four restriction kernels coincide.
   The fourth-only factor is therefore a complementary copy of
   C_2. The k chosen independent monomials give rank exactly k,
   with all other normal coordinates zero. These are full polynomial
   embeddings (projection onto u is an inverse on each branch).
   The tail calculation applies to each, so their cokernel lengths
   really are 10, 9, 8 and 7. They establish variability only for
   the explicitly relaxed smooth complex-branch problem. They
   establish no such variability under L118's total geodesy.

6. **Annihilation and algebraic descent.** Each element of the
   completed image's maximal ideal has zero constant term on every
   branch. Products of three such elements, even multiplied by any
   element of widehat T, belong to J_3. Since (8) places J_3 inside
   widehat A, its cube annihilates widehat Q_z. Exact completion
   and faithful flatness descend this annihilation to the original
   finite A-module Q_z. A finite module killed by m_A^3 has finite
   length. Completion has closed fibre C of length one; 02M1 thus
   identifies that length with the calculated dimension of its
   completion. This step uses the actual A-module structure, not
   just an abstract vector-space cokernel.

The result is a confirmation, classified RESEARCH / REPRODUCTION /
EXPLORATION, not a second mathematical advance. No load-bearing error,
new exclusion or stronger geometric conclusion was found. The direct
mathematical inputs remain L118, L120 and L121. Evaluation of s for
actual totally geodesic branches is a distinct, still unproved target;
the present bounds are not asserted sharp for them. F existence,
collision occurrence, global defect consequences, transport and the
universal Hodge gap remain unresolved. The earlier stops in
ATTEMPTS/070--072 are unaffected.

## Mathlib

Full matching coverage for this four-branch nonlinear normalization
formula and its tangent-rank specialization is **not checked**. Unknown
coverage is not evidence of absence. The general regularity, filtered
lifting, completion and length inputs are cited precisely above; their
specialized hypotheses and the full finite rank calculation are checked
in this informal proof. No Lean or numerical verification is claimed.
