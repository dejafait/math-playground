# L157 — Two additional rows with shared factor representatives

## Hypotheses

Let E be any field extension of F_97. Retain the original C155a/L156 domain

    H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96},
    S={1,8,12,18,22,27,33}, J=H minus S.

The 756 labels j=(I_j,K_j) are binom(S,2) times binom(J,2), with I
outermost and both pairs in increasing lexicographic order. Fix any
original a<b whose four-element supports are disjoint. Let c,d be any
distinct labels outside {a,b}, with their order fixed for the formulas.
No disjointness, incidence or genericity assumption is imposed on c,d.
Put W=E^S in increasing coordinate order. For j=a,b,c,d define

\[
 z_j=\min(S\setminus I_j),\qquad
 g_j(X)=\prod_{v\in J\setminus K_j}(X-v),\qquad
 (Q_jw)_u=g_j(z_j)w_u-g_j(u)w_{z_j}
 \quad(u\in(S\setminus I_j)\setminus\{z_j\}).                 \tag{1}
\]

Each target has increasing u-order. Write T_c,T_d for these separately
labelled copies of E^4, and A=ker Q_a, B=ker Q_b. Use audited C155a:
dim A=dim B=3, A intersect B=0, and its selected-pair decomposable locus
has unique ordered factor lines ([x],[y]) in P(A)(E) times P(B)(E).
The corresponding plane is L=span_E(x,y), with both selected ranks one.
Inherit its audited L155/L153 original-domain qualifications, including
the complete original 79,380 disjoint pairs, without a new census.

For Z=A,B and r=c,d set f_{r,Z}=Q_r|_Z. Define the **joint** linear data

\[
 F_Z:Z\longrightarrow T_c\oplus T_d,\quad
 F_Z(z)=(f_{c,Z}(z),f_{d,Z}(z)),\qquad
 K_Z=\ker F_Z,\quad V_Z=\operatorname{im}F_Z,
 \quad C_Z=(T_c\oplus T_d)/V_Z,                              \tag{2}
\]

with quotient map pi_Z:T_c direct-sum T_d -> C_Z. Thus K_Z is a
two-row kernel, not either of L156's single-row kernels. Choose an
E-linear section s_Z:V_Z -> Z of F_Z onto its image. Such a section
exists also when V_Z=0. All projective spaces below mean E-valued
lines; P(0)(E) is empty. These are field-valued assertions only.
No coding, weight or prescribed-chart gate is assumed.

## Conclusion

The following explicit disjoint parameters give exactly the locus

\[
 \mathcal R_{c,d}=
 \{([x],[y]):\operatorname{rank}(Q_c|_L)
                   =\operatorname{rank}(Q_d|_L)=1\}.       \tag{3}
\]

First select for each row r a symbol sigma_r in {A,B,M}: A means
only its A-factor image is nonzero, B means only its B-factor image
is nonzero, and M means both are nonzero. Choose an image line

\[
 \ell_r\in\begin{cases}
 \mathbb P(\operatorname{im}f_{r,A})&\sigma_r=A,\\
 \mathbb P(\operatorname{im}f_{r,B})&\sigma_r=B,\\
 \mathbb P(\operatorname{im}f_{r,A}\cap\operatorname{im}f_{r,B})
                                                &\sigma_r=M.
 \end{cases}                                               \tag{4}
\]

The intersection in (4) is inside the same actual T_r. The c and d
targets are not identified. Let t_r be the unique generator of ell_r
whose first nonzero coordinate in the original T_r order equals one.
Put e_c=(t_c,0), e_d=(0,t_d) in T_c direct-sum T_d.

For each Z record the rows where its image is required nonzero as
S_Z subset {c,d}. All nine cases are as follows; no row has both
images zero in this table.

| sigma_c | sigma_d | S_A | S_B |
| --- | --- | --- | --- |
| A | A | {c,d} | empty |
| A | B | {c} | {d} |
| A | M | {c,d} | {d} |
| B | A | {d} | {c} |
| B | B | empty | {c,d} |
| B | M | {d} | {c,d} |
| M | A | {c,d} | {c} |
| M | B | {c} | {c,d} |
| M | M | {c,d} | {c,d} |

For the fixed symbols and image lines compute

\[
 u_Z=\pi_Z(e_c),\qquad v_Z=\pi_Z(e_d).                      \tag{5}
\]

The factor parameter set D_Z and its reconstruction rho_Z:D_Z -> P(Z)
are explicitly the following.

* If S_Z is empty, D_Z=P(K_Z), and rho_Z is the inclusion into P(Z).
  If dim K_Z=m>0, completely disjoint coordinates for this set are
  (0,...,0,1,h_{i+1},...,h_m), h_j in E, with the first 1 in position
  i=1,...,m in any fixed ordered basis of K_Z. If m=0 this set is empty.
* If S_Z={c}, the set is empty unless u_Z=0. When u_Z=0, take D_Z=K_Z
  and rho_Z(k)=[s_Z(e_c)+k].
* If S_Z={d}, the set is empty unless v_Z=0. When v_Z=0, take D_Z=K_Z
  and rho_Z(k)=[s_Z(e_d)+k].
* If S_Z={c,d}, form the following fully resolved scalar set:

\[
 \Lambda_Z=\begin{cases}
 E^*&u_Z=v_Z=0,\\
 \{-\alpha\}&v_Z\ne0\text{ and }u_Z=\alpha v_Z
                                  \text{ for some }\alpha\in E^*,\\
 \varnothing&\text{otherwise}.
 \end{cases}                                               \tag{6}
\]

  In the second case alpha is unique. Put D_Z=Lambda_Z times K_Z and

\[
 \rho_Z(\lambda,k)=[s_Z(e_c+\lambda e_d)+k].                \tag{7}
\]

Only vectors in V_Z are passed to s_Z; tests (5)–(6) ensure this.
For complete explicit coordinates in (6), choose any basis of C_Z.
If v_Z is nonzero, choose its first nonzero coordinate i, set
alpha=(u_Z)_i/(v_Z)_i, and retain it exactly if alpha is nonzero and
(u_Z)_j=alpha*(v_Z)_j at every coordinate j. When C_Z=0, both quotient
vectors are zero and the first case applies. Thus (6) leaves no scalar
equation unsolved and does not call for a polynomial solver.

For every choice in (4), reconstruction is the bijection onto its
specified stratum and image-line fiber

\[
 D_A\times D_B\longrightarrow\mathcal R_{c,d},\qquad
       (p_A,p_B)\longmapsto(\rho_A(p_A),\rho_B(p_B)).       \tag{8}
\]

The full locus is the disjoint union of these images over all nine
symbol pairs and all permitted ordered image lines. An empty D_Z
means an empty fiber even when (4) admits the image lines individually.
At fixed image lines every nonempty D_Z with S_Z nonempty is, as a
parameter set, either K_Z or E^* times K_Z; the singleton scalar case
in (6) contributes K_Z. No full affine-space claim is made for a
punctured factor. If S_Z is empty it contributes the projective space
P(K_Z). The sections make these descriptions noncanonical; no global
product trivialization, scheme structure or descent is asserted.

The extra compatibility beyond independent L156 fibers is exactly
the joint-image tests (5)–(6). For instance a nonzero image at c and
zero image at d requires (t_c,0) in im F_Z, not just t_c in im f_{c,Z}.
Two nonzero images require one nonzero relative scalar satisfying (6),
not two independently chosen lifts. All tests use the same factor.

In an ordered factor basis h_1,h_2,h_3 of Z, the two four-by-three
blocks of F_Z have entries

\[
 (F_Z)_{(r,u),i}=g_r(z_r)(h_i)_u-g_r(u)(h_i)_{z_r},
 \quad r=c,d,\quad u\in(S\setminus I_r)\setminus\{z_r\},   \tag{9}
\]

where z_r is the label anchor from (1). Hence (2), (5) and (6) are
kernels, images and quotient-vector
tests for the original eight-by-three matrices, over E itself.

This is a local REPRODUCTION; the first separate critical audit below
passes with the inherited finite-input qualifications. It is not a two-row exclusion, an evaluated classification
of original quadruples, a many-row solver or a radius improvement.

## Proof

### Imported tools and scope

Import A. I. Kostrikin and Yu. I. Manin, *Linear Algebra and Geometry*,
Gordon and Breach paperback, 1997, ISBN 90-5699-049-7, translated by
M. E. Alferieff, [Chapter 1 Theorem 3.12, pp. 20–21; sections 6.2–6.9,
pp. 44–46; Chapter 3 sections 6.2–6.4, pp. 222–226, 6.8–6.10,
pp. 227–228, 8.1, p. 233, and 8.10, pp. 239–240](https://www.math.mcgill.ca/darmon/courses/19-20/algebra2/manin.pdf).
The inspected arbitrary-field tools give linear kernels, images,
quotients, coimage/image identification, complements and projective
normalizations away from a kernel. In particular a linear map onto
its image has a section, and the lifts of a vector in that image form
one coset of its kernel. These general results are imported, not reproved.
Zero maps use the linear definitions, not a projection construction
requiring nonzero summands.

The unchanged invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-25-two-additional-row-factor-compatibility-review.md`.
Its arbitrary-field source comparison and previous duplicate/failure
checks are reused. No complex-field linear-relation normal form is
imported. The general tools do not themselves specify the shared-scaling
branches for these original maps; their explicit specialization and
exhaustion are what is proved below. No novelty claim is made.

### The same two factors and actual maps

C155a gives unique factor lines and independent nonzero representatives
x in A, y in B, so L=span(x,y). Formula (1) is exactly L109's actual
quotient; its g_j(z_j) is nonzero because J minus K_j is disjoint from
S. Substituting each factor basis vector into (1) gives (9), with the
same target coordinates for both factors of a row. Stacking the rows
does not identify T_c with T_d and does not change either rank test.

Apply audited L156 to c and separately to d. In each row the only
rank-one alternatives are: the A image alone is nonzero; the B image
alone is nonzero; or both images are nonzero with a common projective
image. Their common or sole nonzero line is unique and lies exactly
in the appropriate space in (4). A row with two zero images has rank
zero and is rejected. A row with independent nonzero images has rank
two and is also rejected. Thus any point of (3) uniquely determines
the two symbols, the two image lines and the displayed active sets.
There are exactly nine combinations, as listed in the table.

It remains to impose that the same [x] and [y] realize both rows.
This is not implied by the independent applications of L156. Fix the
symbols and lines from now on. Their normalized t_c,t_d are well
defined over E; they are never assumed to lie in the base field.

### Shared lifts for each active set

Fix Z=A or B. If S_Z is empty, both images of its representative must
vanish. This is exactly a nonzero vector of ker F_Z, modulo scaling,
so D_Z=P(K_Z) gives every possibility once. The stated first-nonzero
coordinate charts explicitly remove the scaling ambiguity, including
the empty zero-dimensional case.

If S_Z={c}, a representative z has f_{c,Z}(z)=beta*t_c with beta
nonzero and f_{d,Z}(z)=0. Dividing z by beta is the unique representative
of its line with F_Z(z)=e_c. Such a lift exists if and only if e_c
belongs to V_Z, equivalently u_Z=0. If it exists, the imported coset
description gives all lifts uniquely as s_Z(e_c)+k, k in K_Z. These
vectors are nonzero because their c-image is t_c. Two of them on the
same projective line differ by a scalar preserving t_c, which forces
that scalar to be one and then forces their k parameters equal.
The proof for S_Z={d} uses its unique representative with d-image
t_d and c-image zero; its exact existence condition is v_Z=0 and its
unique parameters are s_Z(e_d)+k. No lift may have an unrecorded
nonzero image in the other row.

If S_Z={c,d}, write the two images of any representative as beta*t_c
and gamma*t_d with beta,gamma both nonzero. Divide by beta. The
normalized images are t_c and lambda*t_d where lambda=gamma/beta
belongs to E^*. This lambda is independent of the initial nonzero
representative and is uniquely determined by the factor line. A
normalized lift exists exactly when

\[
 e_c+\lambda e_d\in V_Z,
 \quad\text{equivalently}\quad u_Z+\lambda v_Z=0.          \tag{10}
\]

If v_Z=0, equation (10) admits every lambda in E^* when u_Z=0,
and none when u_Z is nonzero. If v_Z is nonzero, (10) forces
u_Z=alpha*v_Z with alpha=-lambda nonzero. That alpha is unique,
and conversely any such alpha gives the unique admissible lambda.
In particular u_Z=0, v_Z nonzero would force lambda=0 and is rejected.
If the quotient vectors are not proportional there is no solution.
These are precisely all cases of (6). The coordinate recipe following
(7) tests equality in the entire quotient space, not only its chosen
nonzero coordinate.

For every retained lambda the lifts of e_c+lambda*e_d are exactly
s_Z(e_c+lambda*e_d)+k, k in K_Z. Their c-image t_c makes them
nonzero. If two such lifts give the same projective point, the scalar
relating them must be one by their equal c-image; their d-images then
force the same lambda and their difference forces the same k. This
proves both existence and uniqueness in (7). It also explains why
independently normalizing both row images to t_c and t_d would lose
solutions: their relative scalar is lambda and need not equal one.

### Joint reconstruction and exhaustive inverse

Take any parameters in a nonempty D_A times D_B. The factor formulas
just proved give nonzero representatives whose row images vanish
exactly as specified by S_A,S_B. At a row with symbol A or B, the
specified unique nonzero image spans ell_r. At a row with symbol M,
both images are nonzero scalar multiples of t_r, hence span the same
line ell_r. Their scalars need not agree between A and B: each rank
test requires proportional images, not equal chosen vectors. C155a
ensures the two representatives are independent, so their image spans
are exactly Q_r(L). Both ranks are therefore one. This proves (8)
lands in (3), without imposing an unwarranted common normalization on
the two factors.

Conversely any point of (3) uniquely gives its symbols and lines by
L156. For each of its two factor lines the corresponding normalization
in the preceding subsection gives its unique parameters in D_Z.
The no-active case is already a projective line in K_Z. Thus (8) is
surjective onto its stated fiber and injective there, and different
fibers or symbol pairs do not overlap. This proves the complete
disjoint parametrization in both directions.

### Degeneracies, choices and boundary

If a restriction f_{r,Z} is zero, no pattern requiring its nonzero
image has an image line in (4); patterns requiring its zero image are
still handled by the joint maps. If both restrictions for a row vanish,
every line set in (4) for that row is empty, and so is (3). If F_Z=0,
K_Z=Z and V_Z=0: only S_Z empty can survive the formulas, consistently
with the required images. If K_Z=0, the inactive case contributes no
factor line, whereas a compatible active case contributes one lift
per admitted scalar; the zero vector k=0 is a legitimate affine
parameter. An empty image intersection or a failed quotient test
produces no fiber. None is filled in by closure or by a generic-position
argument. In particular the discarded lambda=0 case cannot be restored.

All section choices, quotient bases, t_r and lifts are over E. For
each retained parameter, the reconstruction gives an E-point directly;
for each E-point the inverse normalization remains in E. This includes
finite E. The parameter domains retain exactly P(0)=empty, empty line
sets, incompatible quotient vectors and the deletion of zero scalars;
no nonemptiness is inferred from dimension or algebraic-closure points.
Changing a section translates the relevant k by the difference of two
lifts of the same joint image, which lies in K_Z. Changing generators
of the image lines changes the unique normalizations and scalar ratios
invertibly. These choices do not change the locus. The proof is a
statement about E-valued sets and their displayed coordinates, not a
global trivialization or a scheme-theoretic fiber assertion.

The construction fixes arbitrary original a,b,c,d and uses no further
support incidence or injectivity. It preserves arbitrary intersections
of the additional-row kernels with A or B. It supplies explicit
two-row compatibility, but does not evaluate its surviving image-line
pairs for any quadruple or exclude a twelve-row family. In particular
passing these two rows is not sufficient for a represented equality.

Any coding use still requires q=97^20, k=8, the pinned
1/4<=delta<5/16 cell, coefficient syndromes in U_S, nonzero actual D
and locators, sixteen original finite events, coding t=0, arbitrary
weights and the original chart, and L056/L069/L040 plus L051/L055
qualifications. Nonzero recovered lambda, full weights, finite chart
directions, other rows and remaining-event balance are not consequences
of (3). The scalar lambda in (6) is merely an image ratio, not L109's
recovery lambda. C152a/L086/L152 and L154 are prospective uses only.
L104 survivors, L151's label limits and ATTEMPTS/041–043,/048–049
remain evidence. Universal representation, challenge identification and
the wider-radius question remain unresolved; the comparison-model
interval remains 11/q–16/q. There is no complete challenge candidate.

### First separate critical audit — step 497, 2026-10-25

**Scope and inputs.** The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-25-l157-critical-audit-review.md`. Its inspected
arbitrary-field tools and completed step-494 comparison are reused.
This audit checks the written specialization, not a new source theorem.
C155a supplies unique ordered factor lines and their independence;
L156 supplies the one-row alternatives; L109 supplies the actual maps
and the distinct recovery gates. L155/L153 remain inherited audited
inputs, with the original 756 labels and all 79,380 disjoint pairs.
No finite certificate or already passed input audit was replayed.

**Original coordinates.** The displayed H,S,J and ordering agree with
C155a/L156. For every label, z_j is in S minus I_j, and every root of
g_j is in J minus K_j. Thus g_j(z_j) is nonzero already in F_97 and
remains so over E. Formula (1) is L109's covector, and substitution
of each h_i gives exactly (9). The two factors use the same target
coordinates within each row. Stacking uses a direct sum of separately
labelled targets, so no equality between c- and d-target vectors is
assumed. The section domain is precisely V_Z, not the whole direct sum.

**Nine strata.** In the basis x,y of L, each row has the two columns
Q_r(x),Q_r(y). Rank one has exactly the alternatives A, B and M stated
above: a single nonzero column, or two nonzero proportional columns.
The corresponding image line is unique. Both zero gives rank zero;
two independent images give rank two. Neither can enter any row symbol.
Reading c then d, the table gives respectively
({c,d},empty), ({c},{d}), ({c,d},{d}), ({d},{c}),
(empty,{c,d}), ({d},{c,d}), ({c,d},{c}), ({c},{c,d}),
({c,d},{c,d}) for (S_A,S_B). These are exactly the active sets of
AA, AB, AM, BA, BB, BM, MA, MB, MM, with no missing or repeated symbol.
Condition (4) is necessary for these lines, but is not asserted sufficient
for joint lifts; the subsequent tests retain that distinction.

**Full inverse for one factor.** Fix the symbols and lines. If S_Z is
empty, the allowable lines are exactly P(K_Z); first-nonzero coordinates
in a fixed kernel basis represent each once. If S_Z={c}, take any
nonzero representative z and write f_{c,Z}(z)=beta*t_c. Here beta is
nonzero and f_{d,Z}(z)=0. Its uniquely normalized vector is z/beta.
The inverse parameter is k=z/beta-s_Z(e_c), which is in K_Z since
both terms have joint image e_c. Existence is exactly u_Z=0. The same
argument with d gives k=z/beta-s_Z(e_d) and the condition v_Z=0.
These arguments constrain the inactive row as well as the active row.

When S_Z={c,d}, write F_Z(z)=(beta*t_c,gamma*t_d) with both scalars
nonzero. The inverse is lambda=gamma/beta and
k=z/beta-s_Z(e_c+lambda*e_d). This is defined precisely when
u_Z+lambda*v_Z=0, and then k lies in K_Z. Rescaling the original z
changes neither normalized vector nor either inverse parameter.
Conversely every displayed k and admitted lambda reconstruct this
same joint image. Equality of two projective outputs forces the
representative scaling to be one by their c-image t_c, then forces
lambda equality by their d-image and finally k equality. For a single
active row its fixed nonzero image gives the same uniqueness argument.
For no active rows the parameter already is a projective line.

**Scalar exhaustion and section domains.** If v_Z=0, then u_Z=0
allows all nonzero scalars and u_Z nonzero allows none. If v_Z is
nonzero, u_Z=0 forces the forbidden lambda=0; a nonzero u_Z proportional
to v_Z gives the unique lambda=-alpha; nonproportional vectors give
none. These cases exhaust the quotient space, including C_Z=0.
The coordinate recipe divides only by a nonzero coordinate of v_Z,
rejects alpha=0 and checks every coordinate, so it is equivalent to
vector equality, including higher-dimensional cokernels. These exact
tests put e_c, e_d or e_c+lambda*e_d in V_Z before s_Z is evaluated.
Every active reconstructed vector is nonzero because its normalized
active image is nonzero.

**Product, disjointness and rationality.** At fixed image lines the
two factors have independent projective scalings. There is no requirement
that their relative row ratios agree: row rank one compares image lines,
not their chosen generators. The product in (8) therefore imposes all
and only the two rank-one tests. C155a ensures its representatives are
independent. Conversely the symbols and lines are recovered uniquely
from their images, and the preceding inverse recovers each factor's
parameters uniquely. Hence different fibers cannot overlap, even if
one factor is inactive in both rows: the other factor still determines
both image lines. Every normalization, quotient, section and inverse
is over E. No base-field representative or algebraic-closure lift is
substituted for an E-point.

**Empty cases and choices.** A zero restriction excludes every pattern
requiring its nonzero image. If both factors vanish at a row, its line
sets are empty. If F_Z=0, only the inactive case can survive. If K_Z=0,
P(K_Z) is empty but its affine kernel set contains the legitimate
parameter k=0. Failed quotient tests, empty image intersections and
deleted zero scalars remain excluded also over finite E. No positivity
of a dimension is used to manufacture points.

For the same joint image w, replacing s_Z by s'_Z sends
k to k+s_Z(w)-s'_Z(w), an invertible translation in K_Z. Replacing
t_c,t_d by eta_c*t_c,eta_d*t_d, with eta_c,eta_d nonzero, sends the
two-active parameters to lambda'=(eta_c/eta_d)*lambda and
k'=eta_c*k for a fixed linear section. A single active row r sends
k to eta_r*k. Inactive projective lines are unchanged. These transitions
are invertible and check the asserted independence of choices, without
claiming a global product or a scheme assertion.

**Verdict and limit.** Pass for the complete stated E-point bijection
for every original a,b,c,d and every E/F_97, conditional on the stated
audited inputs. No statement repair, added hypothesis or new dependency
is needed. This is a first audit of an existing partial result, not a
new mathematical result or progress beyond the sources checked. The
parameters have not been evaluated for original quadruples. The coding
qualifications above, including the distinction between an image ratio
and the recovered lambda, remain essential. No twelve-row exclusion,
weights/chart conclusion, universal representation or challenge
identification follows. ATTEMPTS/041–043,/048–049 and the L104/L151
limitations remain intact.

## Mathlib

Full matching original-pair two-additional-row parameter theorem:
**not checked**. Supporting linear-map kernels, quotients, sections,
projective coordinates and finite-dimensional image coverage:
**not checked anew**. The precise imported source above supplies the
standard mathematics. Unknown Mathlib availability is not evidence of
absence. The separate informal audit above is not formal verification
or a challenge resolution.
