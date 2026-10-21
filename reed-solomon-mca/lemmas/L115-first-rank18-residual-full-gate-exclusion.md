# L115 — First rank-18 residual fails the complete recovery gates

## Hypotheses

Use F=F_(97^20), the order-sixteen subgroup H of F_97^*, dimension
eight, L010's shifted moments and the pinned event on
1/4<=delta<5/16. The actual Hankel determinant and every coordinate
locator are nonzero polynomials. Both coefficient syndromes belong to
U_S, where S={1,8,12,18,22,27,33}. Assume sixteen original finite bad
parameters and L104's t=0, with all inherited L010/L103/L104 and L109
finite-certificate qualifications. Weights and the prescribed original
chart are arbitrary over F. Suppose the following four supports are
actual two-overlap errors:

| Row | I subset S | K subset J=H minus S |
| --- | --- | --- |
| 1 | {1,8} | {47,50} |
| 2 | {12,18} | {64,70} |
| 3 | {1,12} | {75,79} |
| 4 | {8,12} | {85,89} |

Use L109's six-row exterior blocks, with increasing S-pair columns.

## Conclusion

These hypotheses are inconsistent. The four-row stack has rank 18,
but every nonzero tensor of its complete kernel has a plane containing
E_12. At row 2, that plane has either rank-zero projection, forbidden
by actual nonpersistence, or unique recovery line F*E_12, which has
lambda zero and overlap weight zero at label 18. Thus the whole locus
is excluded over every extension of F_97, in every prescribed chart.

This removes only L114's indexed residual (third 0, fourth 249).
It does not exclude its third, the fixed pair, arbitrary seven-sets or
arbitrary t=0 profiles. No new global upper bound follows. L114's
partition remains unaudited; this proof validates only the specified
input independently. Same-step replay passes; the separate step-315
critical audit below found no defect in this restricted exclusion.

## Proof

### Scope and imported results

Apply audited L109's necessary direction: the actual lift coefficients
are independent, their wedge is nonzero and lies in the four-row
kernel, and every actual row must pass the rank-one, full-weight and
prescribed finite-direction gates. All its field, shortening and
nonpersistence hypotheses are those above. This uses neither its
r>=6 converse nor an extraction of these four supports from an arbitrary
pencil. L114 is the provenance of the saved input, not an assumed
correct partition or an essential theorem for this proof.

Standard coding results are imported through L109: J. I. Hall,
*Notes on Coding Theory*, [Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
[accepted manuscript 2016-02-29, section 5, printed pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2, Lemma 5.3 and the following shortening formula.
Distinct labels, nonzero multipliers, dimension eight and shortening
exactly the seven labels J minus K retain their hypotheses. No general
distance or shortening result is reproved.

The saved EXPLORE assessment at invocation start was
`drafts/literature/2026-10-18-first-rank18-residual-full-gates-review.md`.
This is a REPRODUCTION of the assessed exact factor/gate mechanism,
specialized to one different locus. Its exact matrix and gates require
checking: the earlier label-1 containment test fails here. No general
new factor theorem or originality beyond the inspected sources is claimed.

### Complete kernel and extension validity

Construct g_j(X)=product_(y in J minus K_j)(X-y), z_j=min(S minus I_j),
c_jx=g_j(z_j)E_x^*−g_j(x)E_zj^*, and stack their exterior blocks
as in (1) of L109. The full 24-by-21 matrix is preserved in
`scripts/seven-coordinate/first-rank18-full-gates.json`.
Number rows and columns starting from zero. The minor with row indices

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19

and column indices

    0,2,3,4,5,7,8,9,10,11,12,13,15,16,17,18,19,20

has determinant 92 modulo 97. The three vectors below, expressed as
bivectors, are in the kernel:

    B0 = E_1 wedge E_12,
    B1 = E_8 wedge E_12,
    B2 = E_12 wedge (73 E_18 + 63 E_22 + 62 E_27 + E_33).

All 72 scalar residuals against the original stack are zero. The free
columns 1,6,14 give the identity matrix on B0,B1,B2, proving their
independence. The minor proves rank at least eighteen and these three
independent vectors prove rank at most eighteen, hence completeness.
The same nonzero minor and zero residuals prove the same statement
over every extension field; no rational descent is assumed.

Consequently every kernel vector has the unique form

    p=s B0+t B1+r B2 = E_12 wedge w,
    w=−s E_1−t E_8+r(73 E_18+63 E_22+62 E_27+E_33).

If (s,t,r) is nonzero, w is nonzero and has zero label-12 coordinate,
so w and E_12 are independent. Thus p is decomposable and its plane
is exactly span(E_12,w). Every one of the 35 homogeneous Plucker
equations vanishes identically in s,t,r; the decomposable projective
locus is the entire P^2 over every extension. This includes zero
kernel coordinates and infinity, rather than testing base-field points.

### Intrinsic obstruction and prescribed chart

Since 12 belongs to I2, Q_2 E_12=0. On the plane span(E_12,w),
the rank of Q_2 is at most one. If it is zero, L109's actual
nonpersistence argument rejects this branch: both coefficient
syndromes would be represented on A2 and its locators would be
identically zero. Do not count a direction from that branch.

If the rank is one, its kernel in the plane is exactly F*E_12.
Any nonzero recovery vector is therefore h=c E_12, c nonzero.
Here z2=1, and g_2(1) is nonzero because every label is distinct.
L109's restored formulas give

    lambda=h_1/g_2(1)=0,
    e_18=h_18−lambda*g_2(18)=0,
    e_64=−lambda*g_2(64)=0, e_70=−lambda*g_2(70)=0.

Thus the required full four-error recovery fails. No choice of
prescribed original chart can turn any of these zero weights into
nonzero weights. If the direction is omitted by that chart it is also
ineligible. This proves the contradiction for every nonzero p.

For explicit complete gate coverage, the certificate retains all
21 charts p_ab!=0. Fifteen have identically zero pivot; six remain.
In each nonempty chart use U_x=p_xb and V_x=p_ax. L109's Plucker
identity gives U wedge V=p_ab*p, so U,V span the plane. At every row
save qU=Q_j U, qV=Q_j V. All six projection minors vanish. Rank zero
is explicitly the branch with all eight entries qU,qV zero, rejected
by actual nonpersistence. Rank one is covered by choosing any of the
four indices n and either nonzero alternative qU_n or qV_n. Set

    alpha=−qV_n, beta=qU_n, H=alpha U+beta V.

Independence of U,V makes H nonzero on such a branch; the vanishing
minors give Q_j H=0. Save all three full-weight numerators

    H_z, g_j(z)H_i−g_j(i)H_z for i in I_j.

At row 2, H_1 and the numerator for label 18 are identically zero
quadratic polynomials on every branch. Their zero coefficient vectors
are exact identities, not a saturation heuristic or truncated solver.
If its projection pivot also vanishes, that branch is empty; the
other pivots and the rank-zero branch remain explicitly covered.
The common intrinsic failure removes every combination of row choices.

For a prescribed basis u_original=A U+B V, v_original=C U+D V,
AD−BC!=0, H has original first coefficient
(D alpha−C beta)/(AD−BC). The saved finite gate is therefore
D alpha−C beta!=0. All four basis entries can be extension-field
elements and the omitted direction can be nonrational. No replacement
chart is chosen. The intrinsic zero-lambda failure holds before imposing
this gate, so it excludes all such charts.

### Full certificates and independent replay

Reproduce from this notebook:

    python3 scripts/seven-coordinate/first_rank18_full_gates.py
    python3 scripts/seven-coordinate/verify_first_rank18_full_gates.py

The full certificate is
`scripts/seven-coordinate/first-rank18-full-gates.json` and its replay is
`scripts/seven-coordinate/first-rank18-full-gates-replay.json`.
The original input is identified by the exact shard SHA-256 and
`/cases/249`. The replay independently checks its third/fourth labels,
all six pair intersections, matrix, rank and complete basis. The
producer uses direct products and modular row elimination; the replay
uses derivative/Horner polynomial values, greatest-label ratio quotients,
independent forward elimination, and an integer fraction-free determinant
for the original 18-by-18 minor. No replay of the other L114 cases or
separate approval of L114 is implied.

All 35 Plucker equations, 21 projective charts, 96 row-projection
pivots and their 192 nonzero alternatives are retained. The replay
checks 672 original-generator coefficient identities, including the
projection and recovery identities. Every generator is identically
zero here, so no nonzero remainder is hidden in an ideal computation.
It reconstructs all linear forms and homogeneous quadrics independently.
For a homogeneous quadratic in three variables, the exact values at
e_i and e_i+e_j determine all coefficients: diagonal coefficients are
f(e_i), and mixed coefficients are f(e_i+e_j)−f(e_i)−f(e_j).
The six determining evaluations are coefficient verification, not an
inference about all extension points from sampling.

On each branch restore lambda=H_z/g_j(z), and e on I_j union K_j by
L109's formulas. Extend H by zero off S. All eight original shifted
moment differences sum_(x in H)(H_x−e_x)x^d, 1<=d<=8, are identically
zero. The replay checks every coefficient of these 96*8 quadratic
polynomials: 4,608 zero coefficients in total, as well as the complete
recovered errors and prescribed-chart forms. Invalid full weights are
retained while these identities are checked, not silently removed.
There are no failures or unresolved charts. Both implementations share
Python and residue arithmetic and reuse prior low-level utilities;
this is explicit finite-computation dependence, not a proof assistant
verification or a separate critical audit.

The only downstream inference is the stated four-support exclusion
from L109's necessary gates. No sixteen-event construction, t=0
converse, universal representation, uniform triangle bound or challenge
definition is supplied. The global interval remains 11/q–16/q.

### Separate critical audit, 2026-10-18

Step `2026-10-18-mca-315-first-rank18-critical-audit` checked this full
proof, audited L109's necessary gates and prior audit, both complete
programs above, and every mathematical utility they invoke for this
locus: original blocks, modular kernel elimination, independent ratio
blocks, forward elimination, determinant, Plucker coefficients and chart
encoding. The ready exact audit assessment and saved primary Hall and
shortening extractions were reused. No essential new source or theorem
was required. L109's inherited L010/L103/L104 qualifications remain;
this audit does not independently replay those earlier finite censuses.

The independently specified written matrix and basis were checked by
`python3 scripts/seven-coordinate/audit_first_rank18_full_gates.py`.
Its complete evidence is
`scripts/seven-coordinate/first-rank18-critical-audit.json`.
Each row shortens exactly seven distinct labels in J minus K, leaving
nine labels and dimension one. Throughout successive shortening the
dimension remains positive until the final dimension one, and each
multiplier is a product of nonzero differences. The saved source hash,
third and fourth labels, all six pair intersections and complete original
case `/cases/249` are checked by the replay; no other L114 case is used.

The fresh rational Gaussian determinant calculation gives the integer

    20019549951497103509777570611200

for the specified original minor, with residue 92 modulo 97. This is
independent of the existing modular and fraction-free determinant paths.
The written three basis vectors exactly match the certificate, all 72
original residuals vanish, and their free-column identity submatrix is
checked. Thus the original rank is both at least and at most eighteen.
Because this proof uses a nonzero base-field minor and a base-field
basis, it retains the entire extension-field kernel, not only rational
points or a computed sample of decomposable vectors.

The common-factor proof covers every nonzero (s,t,r), since w has zero
label-12 coordinate and is zero only when all three scalars are zero.
Hence E_12 and w are independent. On their plane Q_2 annihilates E_12.
Rank zero is rejected by L109's nonpersistence argument, including
deficient recovered weights; at rank one the entire kernel line is
F*E_12. At every nonzero representative of that line, lambda and the
weights at 18, 64 and 70 vanish. Fullness is an equality consequence
imported before imposing these necessary gates. An apparent one-error
representative therefore cannot supply the hypothesized full A2 error.
There is no assumed rational descent, and no four-row converse is used.

The full original producer and replay reproduced both certificates byte
for byte; the provenance shard also remained unchanged. The reviewed
replay checks every coefficient record through its original formulas:
35 Plucker equations, all 21 charts (15 empty, six nonempty), 96 row
projection pivots with both nonzero alternatives, 672 exact generator
identities, and all 4,608 coefficients of the 768 original moment
quadrics. All saved projection and recovery identities are zero
polynomials here, independently of any ideal-membership algorithm.
The six determining evaluations per homogeneous quadratic recover all
six coefficients; linear forms are determined by the three included
unit vectors. All formulas have the asserted degree before evaluation:
only fixed nonzero g(z) denominators are inverted. Evaluations outside a
particular pivot chart remain valid polynomial checks, not assertions of
admissible recovery at those points.

Nonempty charts require p_ab nonzero; the identity U wedge V=p_ab*p
therefore guarantees an independent plane basis. At rank one at least
one of the eight projection entries is nonzero, so the four pivots with
two alternatives cover every branch. The separate all-zero branch is
explicitly rejected using actual nonpersistence. When a branch pivot is
nonzero, H is nonzero by basis independence. The second row's universal
weight failure then excludes every possible combination of other rows'
choices; no product of branch lists needs to be sampled.

The prescribed-chart calculation also checks directly: writing
H=c*u_original+d*v_original gives
alpha=A*c+C*d and beta=B*c+D*d, so
c=(D*alpha-C*beta)/(AD-BC). Its nonzero condition and both saved signs
are correct. A finite actual error is the projective recovered error
divided by c; that nonzero scaling preserves all zero-weight failures.
A zero c is an omitted direction and never an actual finite event.
The entries A,B,C,D and the omitted point may lie anywhere in the
extension field. Thus choosing a convenient new original chart is
neither necessary nor permitted in this argument.

All 19 audit checks and the complete producer/replay pass, with no
failures or unresolved chart. Both old and new paths still share Python,
exact arithmetic and the same residue field; no proof-assistant
verification is claimed. This validates the existing reproduced local
input, not a new theorem beyond the checked sources, a third/pair
exclusion, L114's partition, or an improved global error bound.

## Mathlib

Full matching coverage for this exact labeled exclusion is not checked.
Supporting exterior-square, matrix-rank and coding coverage is likewise
not newly checked. The precise standard coding citations above and
audited L109 are imported with their qualifications. No absence from
Mathlib, formal verification or mathematical originality is claimed.
