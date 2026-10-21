# L109 — Parameter-free support compatibility for seven-coordinate lifts

## Hypotheses

Use F=F_(97^20), the order-sixteen subgroup H of F_97^*, dimension
eight, L010's shifted moments, and the pinned event on
1/4<=delta<5/16. The actual D and every locator are nonzero
polynomials. Both coefficient syndromes belong to U_S for a seven-set
S subset H; let f(T)=u+Tv be L104's unique lift on S, and J=H minus S.
For the equality application assume |B|=16 and L104's t=0.
All original coefficients and the original finite chart are arbitrary
over F. L104's smaller-class computational qualifications remain.

Write the distinct two-overlap supports as A_j=I_j union K_j, where
I_j subset S and K_j subset J have size two, and set
g_j(X)=product_(y in J minus K_j)(X-y). For each j choose z_j in
O_j=S minus I_j. For x in O_j minus {z_j} define the covector on F^S

\[
 c_{jx}(w)=g_j(z_j)w_x-g_j(x)w_{z_j}.
\]

Let Q_j be the four-by-seven matrix of these covectors. With S in
increasing order, define the six-by-21 block N_j by

\[
 (N_j)_{(x,y),(a,b)}=c_{jx,a}c_{jy,b}-c_{jx,b}c_{jy,a},
 \quad x<y\text{ in }O_j\setminus\{z_j\},\ a<b\text{ in }S. \tag{1}
\]

Let N be the stack of the N_j. Every entry belongs to F_97 and depends
only on the support labels, not on the unknown row parameters or weights.

## Conclusion

At t=0 equality, r=12+n_0 lies between 12 and 14. The matrix N has a
nonzero decomposable kernel vector p=u wedge v, so

\[
 \operatorname{rank}_{F_{97}}N\le20.                       \tag{2}
\]

Each block has rank six. Unlike L104's matrix, (1) contains no unknown
parameters. Rank 21 for any selected subfamily excludes that subfamily
from an equality pencil over every extension of F_97.

There is also an exact gated projective feasibility test, described
below: impose the Plucker equations on a nonzero kernel vector, retain
the rank-one restriction of Q_j to its reconstructed plane, and test
all recovered weights. For a prescribed original chart, retain its
finite-direction gate. Rank drops and arbitrary extension-field kernels
are not discarded. A nonzero kernel by itself is not sufficient.

For S={1,8,12,18,22,27,33}, the following four rows already give rank 21:

| j | I_j | K_j |
| --- | --- | --- |
| 1 | {1,8} | {47,50} |
| 2 | {12,18} | {64,70} |
| 3 | {22,27} | {75,79} |
| 4 | {1,33} | {85,89} |

Thus these four supports cannot coexist in the represented equality
class. They are pairwise linear, so this is a moment-compatibility
filter beyond that incidence test. No arbitrary t=0 profile is excluded
here. The seven-coordinate fifteen bound and global 11/q–16/q interval
remain unresolved. The separate step-298 critical audit found no defect
in this partial reduction or its complete small certificate.

## Proof

### Reused inputs and elimination

Import L104's exact shortening criterion and equality balance, including
its checked application of J. I. Hall, *Notes on Coding Theory*, GRS
chapter, [Theorem 5.1.1, pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
[accepted manuscript, section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2, Lemma 5.3 and the following GRS shortening formula.
Precisely the seven coordinates J minus K_j are shortened; the dimension
decreases from eight to one and all retained multipliers are nonzero
products of distinct label differences. The field, labels and positive
dimensions are unchanged. No general distance or shortening theorem is
reproved. L010 supplies moment injectivity, sparse-error uniqueness,
pointwise factorization, nonpersistence implications and equality balance.

At equality L104 gives full activity and
2n_0+n_1=4, r=12+n_0, hence 0<=n_0<=2. Every actual row satisfies
f_x(gamma_j)=lambda_j g_j(x) on O_j with lambda_j nonzero.
Thus Q_j u+gamma_j Q_j v=0. Expansion of the pairwise two-by-two
minors gives precisely N_j(u wedge v)=0.

The vectors u,v are independent. Otherwise all nonzero syndromes at
the sixteen full errors are proportional. Choose two distinct actual
supports, which L010 guarantees. Scaling one error to match the other's
syndrome would give a kernel word on at most eight coordinates, so L010
injectivity makes the two scaled errors equal, contradicting their
distinct supports. Hence u wedge v is nonzero.

All g_j values on S union K_j are nonzero. The four Q_j rows are
independent because their four x-coordinates have respective coefficient
g_j(z_j) nonzero and are otherwise zero in those columns. Their kernel is

\[
 V_j=\operatorname{span}\{\mathbf e_i:i\in I_j\}
                  +\operatorname{span}\{(g_j(x))_{x\in S}\},
 \qquad \dim V_j=3.                                     \tag{3}
\]

The exterior square of a surjective map to a four-space is surjective:
lift each pair of basis vectors. Therefore (1) has rank six. Nonzero
p in its stacked kernel proves (2); base-field and extension ranks
agree because rank is determined by minors over F_97.

This is the elementary alternating-coordinate mechanism already used
in L026/L027, specialized here to the seven-coordinate shortening
quotients. Their cyclic-family rank conclusions are not imported.
The new output is the explicit support-only matrix and its exact gates,
not a new general theorem about exterior powers.

### All kernel ranks and the exact recovery gates

For completeness, the following test specifies exactly what a retained
matrix kernel still has to satisfy. Extend p antisymmetrically, with
p_aa=0. In addition to Np=0 and p nonzero impose

\[
 p_{ab}p_{cd}-p_{ac}p_{bd}+p_{ad}p_{bc}=0
 \quad(a,b,c,d\text{ distinct}).                         \tag{4}
\]

These are equivalent to decomposability. In fact choose p_ab nonzero
and set u_x=p_xb/p_ab and v_x=p_ax. Then u_a=1, u_b=0, v_a=0,
v_b=p_ab, and (4) gives u_x v_y-u_y v_x=p_xy. The same identity for
indices including a or b follows directly. Thus this reconstructs an
independent pair over the field of p without assuming rational descent.
Conversely a wedge satisfies (4) by expanding the products.

For L=span(u,v), N_jp=0 says rank(Q_j|_L)<=1. Rank two is excluded
by the equations, while ranks zero and one must be distinguished.
In an actual nonpersistent pencil rank zero is impossible. Indeed,
L subset V_j would put both coefficient syndromes in U_(A_j): for
any h in V_j, write h_x=lambda g_j(x) on O_j, set

\[
 e_i=h_i-\lambda g_j(i)\ (i\in I_j),\qquad
 e_k=-\lambda g_j(k)\ (k\in K_j).                        \tag{5}
\]

Extending h by zero off S gives h-e=lambda*g_j on all H, so their
syndromes coincide. Hence the whole pencil would have a representative
supported on A_j. The polynomial moment factorization from L010 then
makes each locator indexed by A_j identically zero, contrary to the
actual hypotheses. This argument includes deficient weights and lambda=0.
Consequently rank(Q_j|_L)=1 in every admissible actual pencil.

At rank one the intersection L intersect V_j is a unique line. Choose
any nonzero h_j on it, put lambda_j=h_(j,z_j)/g_j(z_j), and require

\[
 \lambda_j\ne0,\qquad
 h_{j,i}-\lambda_j g_j(i)\ne0\quad(i\in I_j).             \tag{6}
\]

These conditions do not depend on the representative of that line.
They are precisely the full-weight gates in (5), since g_j(k) is nonzero
on K_j. Lambda=0, including an intersection contained in the coordinate
space on I_j, is an explicitly rejected branch, not an implicit division.
For a specified original basis u,v write h_j=alpha_j u+beta_j v.
The original finite event additionally requires alpha_j nonzero. Its
parameter is beta_j/alpha_j, and its recovered error is (5) divided by
alpha_j. This retains the original omitted point even when nonrational.

Conversely, suppose 6<=r<=14 distinct supports of the stated type have
degree at most four at every label of H, and a p over F passes (4),
all rank-one tests and (6). These conditions construct their projective
recoveries by (5), with all eight moments, not just projected equations.
Different supports have different projective lines h_j: otherwise sparse
moment uniqueness after scaling would make their full supports equal.
There is a chart making all these r directions finite, because a
projective line over F has q+1>r points; choose its omitted point outside
this finite set. For a prescribed chart the alpha_j gates are required
instead. No rationality of that chart is claimed.

Use a=u and b=v in the selected chart, extended by zero off S. The
recovered full errors make D nonzero at each selected parameter by
L010's pointwise factorization. Every coordinate of H is omitted by
some selected support, since its degree is at most four and r>=6.
The same factorization makes its locator nonzero at that parameter.
Thus all actual polynomial nonpersistence hypotheses hold before L010
is used to conclude same-support badness. Every coordinate of S is
active, since some row omits it from I_j and then its h_j value equals
the nonzero lambda_j*g_j(x). Constants in the selected chart are allowed.

This proves exact feasibility for the selected full recoveries under
these gates. It does not prove sixteen events, their remaining coordinate
balance, or absence of equal-lift events elsewhere (t=0). A higher-rank
alternating tensor, a rank-zero restriction, a zero recovered weight or
an omitted original direction cannot be counted as an event. A kernel
of dimension one is not assumed, and no extension-field descent follows
from the matrix alone.

### A nonvacuous fixed support obstruction

For the four displayed rows use the least element of O_j as z_j,
lexicographic covector pairs, and increasing coordinate pairs as in (1).
The resulting 24-by-21 matrix has successive block ranks 6,12,18,21.
Its first 21 rows, with residues in {0,...,96}, have integer determinant

\[
 -87637416100784452193048153074475550000\equiv28\pmod {97}.
\]

This is a complete specified nonzero minor, proving rank 21 over F_97
and every extension. The two determinant evaluations and all entries are
saved in `scripts/seven-coordinate/zero-anchor-support-filter.json`.
Reproduce with `python3 scripts/seven-coordinate/zero_anchor_support_filter.py`.
The program evaluates (1) directly, selects independent rows, evaluates
the minor by modular elimination, and checks it separately by fraction-free
integer elimination with exact division at every step. This is a small
exact certificate for four fixed rows, not an enumeration or generic-rank
argument. Both computations share the matrix construction and Python;
their agreement alone is not a separate critical proof/program audit.
The separate replay below supplies an additional independent construction
and determinant path, with its stated remaining shared infrastructure.

The first two supports are disjoint. L104's local construction supplies
u=(29,73,44,81,42,9,33), v=(43,83,68,76,13,30,87) on the ordered S.
Its two errors, at 0 and 1, have weights (1,1,63,28) and (1,1,6,27)
on the respective ordered supports. The certificate checks all eight
moment differences at both events, all twelve matrix residuals and the
nonzero wedge. All residuals vanish and all weights are nonzero. This
positive control prevents treating every nonzero kernel as an exclusion;
it is not a t=0 or sixteen-event example. The rank-21 minor and algebraic
necessity, rather than this control, prove the four-row obstruction.

The unchanged ready assessment is
`drafts/literature/2026-10-17-seven-coordinate-syndrome-bound-review.md`.
This is REPRODUCTION of the local alternating/shortening mechanism; no
originality or progress beyond the checked literature is claimed. No
universal support-profile census, global fifteen bound, or challenge
resolution follows. ATTEMPTS/036–037's stopped triangle eliminations
remain stopped: the present rank obstruction uses different seven-set
quotients and an actual nonzero minor, not their automatic identities.

### Separate critical audit, 2026-10-18

Step 2026-10-18-mca-298-zero-anchor-critical-audit checked the complete
proof and producer, L104's full reduction and prior audit, L010's full
pointwise, same-support and equality proofs, and L103's exact audited
scope. The unchanged ready assessment supplies the inspected Hall and
shortening statements. No mathematical error or new dependency was found.
L103's finite-certificate qualifications are retained, not independently
replayed here. The audit validates a reproduced partial input; it supplies
no mathematical conclusion beyond this support filter.

Equality is used before full weights, distinct supports, full activity
and r=12+n_0 in 12–14. Independence of u,v follows from full errors on
two distinct supports and eight-column injectivity; zero syndromes cannot
occur for a full four-error. Consequently the exterior tensor used for
the necessary rank bound is nonzero. The four quotient covectors are
independent, their kernel is precisely (3), and their exterior-square
map is (1). All rank comparisons are valid over every extension because
the entries are in F_97; no rank conclusion about a different support
family is imported from L026/L027.

For every kernel dimension, (4) and a nonzero pivot reconstruct the
stated independent u,v with the correct signs. The equations Np=0
give exactly projected rank at most one. Projected rank zero is excluded
by constructing both coefficient representatives on A_j via (5), which
forces persistent locators even when a coefficient or recovered weight
vanishes. At rank one the unique intersection line must separately pass
lambda!=0 and both overlap-weight gates. These are necessary conditions,
not consequences of a nonzero kernel. A prescribed original chart also
needs alpha_j!=0, with actual errors rescaled by alpha_j; a nonrational
omitted direction remains allowed.

In the converse, (5) gives the complete codeword identity h_j-e_j=lambda_j
g_j on all sixteen labels, including the seven zeros outside S union K_j.
Thus it restores all eight moments. Distinct full supports give distinct
projective directions by sparse moment uniqueness. A newly chosen chart
can avoid those at most fourteen directions because q+1>14; this does
not rationalize or replace a prescribed chart. With r>=6 and every label
used at most four times, a selected full error omits every coordinate
somewhere. L010's pointwise factorization gives nonzero actual D and a
nonzero value of each locator before same-support badness is invoked.
Every S-coordinate is active because an omitted overlap coordinate has
nonzero lambda_j*g_j value. This does not certify t=0, equality balance
for remaining events, or sixteen total events.

Independent reproduction command:
`python3 scripts/seven-coordinate/verify_zero_anchor_support_filter.py`.
The verifier imports no producer routines. It generates H by powers,
computes each g from its polynomial coefficients by Horner evaluation,
and reconstructs each quotient from w_x/g(x)-w_z/g(z). Rescaling its
exterior rows by g(z)^2*g(x)*g(y) independently reproduces all 504 entries
of the 24-by-21 matrix and every saved block field. Column-oriented
reduction gives block ranks six and prefix ranks 6,12,18,21. Rational
Gaussian elimination of all 441 minor entries gives the identical
integer determinant displayed above, hence residue 28. This path shares
neither modular elimination nor fraction-free elimination with the
producer. The original certificate also reproduced byte for byte.

All 35 positive-control Plucker equations and all twenty nonzero-pivot
reconstructions pass. Both projected restrictions have rank one and
lambda=1, their original finite parameters are 0 and 1, both overlap
weights are one, and all four weights in each error are nonzero. Every
one of the sixteen moment residuals and twelve exterior residuals
vanishes. Independently evaluated actual determinants give D(0)=33 and
D(1)=62; all thirty-two locator evaluations agree with the complete
pointwise factorizations. Since the supports are disjoint, each locator
has a nonzero value at one control event. This checks actual polynomial
nonpersistence of the control, not a complete bad-set count.

All 79 checks passed with no discrepancies. The complete rebuilt matrix,
all check results, determinant, projective gates, actual locator values
and producer replay evidence are in
`scripts/seven-coordinate/zero-anchor-critical-audit.json`.
Both paths still share Python, exact integer/rational arithmetic and
the residue field; no independent proof assistant verification is claimed.
The four-row exclusion stays local. Arbitrary t=0 profiles, other
seven-sets, the seven-coordinate fifteen bound and the main challenge
qualifications remain unresolved.

## Mathlib

Full matching seven-coordinate support filter and gated converse:
**not checked**. Supporting exterior-square, Plucker, matrix-rank and
finite-field results: **not checked**. Unknown coverage is not absence.
The standard GRS inputs are imported through L104 with their precise
citations and hypotheses above. The fixed four-row exclusion has the
explicit finite-computation qualification stated above.
