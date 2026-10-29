# L129 — The first excluded retained-star boundary

## Hypotheses

Let |H|=1024, let K be a 60-subset of H, and let a,b be distinct
points outside K. Put C=K union {a}, C'=K union {b}, and
Y=H minus (K union {a,b}). Set q=137,
T={16,64,70,102,112,118,121}, and
Omega=(T times F_q) disjoint union D_0, where |D_0|=4.
Let V be all polynomials over F_q of degree at most two, including zero,
and B_p={(t,p(t)):t in T}. Choose arbitrary bijections
sigma:Omega -> H minus C and sigma':Omega -> H minus C', with
sigma^{-1}(b)=(16,y_0). These are exactly L030's local families:

\[
F_L=\{C\cup\sigma(B_p):p\in V\},\qquad
F_R=\{C'\cup\sigma'(B_r):r\in V\}.
\]

Let A_L subset F_L and A_R subset F_R satisfy

\[
W=\{S\in A_L:b\in S\}=\{S\in A_R:a\in S\},
\qquad |W|=s=18632=q^2-q.
\]

Every two distinct supports in A_L union A_R intersect in at most
63 points. Equal supports are identified in that union and permitted.
No ambient-star equality, column-preserving labels, full-star retention,
probability law or RS realization is assumed.

## Conclusion

The retained-size bound is

\[
|A_L|+|A_R|\le2552584+2s=2589848,\qquad
\min(|A_L|,|A_R|)\le1294924<1532496.
\]

**Accepted by the separate critical audit of 2026-10-26 below.** This is a
restricted intermediate result, not a candidate solution of the grand
list-decoding challenge. Original ambient-star equality is not claimed.
Lower overlap, unequal retained indicators, other distinguished columns,
arbitrary local laws, global compatibility and actual RS lists remain
unresolved. The bracket 955–957 and arbitrary-center 67/68 safety are
unchanged. No sharpness or attainability is asserted.

## Proof

**Scope and imported inputs.** The pre-invocation EXPLORE
[boundary assessment](../drafts/literature/2026-10-26-boundary-retained-star-obstruction.md)
covers exactly this test. L030 supplies the polynomial construction.
L126's audited structural argument supplies a nonstar bijection once
the full ambient stars are equal, using L125's audited 840-map rigidity.
We will apply it to an auxiliary labeling, then transfer the forbidden
pairs back to the original labels. This does not assume full retention.
The boundary recovery and approximate-base-line completion below are
the differences from the strict-overlap argument in L127; L127's
conclusion is not invoked at its excluded threshold.

The external input, reused from the assessed source, is Michael Ben-Or,
Don Coppersmith, Mike Luby and Ronitt Rubinfeld, *Non-Abelian Homomorphism
Testing, and Distributions Close to their Self-Convolutions*, Random
Structures & Algorithms 32(1) (2008), 49–70, DOI
[10.1002/rsa.20182](https://doi.org/10.1002/rsa.20182), Theorem 1,
p. 3 of the [18-page author preprint](https://people.csail.mit.edu/ronitt/papers/convd.pdf).
For a map between finite groups, additive-test failure probability
delta<2/9 on two independent uniform inputs gives a homomorphism
with disagreement fraction at most
tau=(3-sqrt(9-24 delta))/12. We use tau<=delta/2, which follows for
positive delta by rationalization, tau=2 delta/(3+sqrt(9-24 delta)),
and sqrt(9-24 delta)>5/3>1. At delta=0 the map is already a
homomorphism, since every ordered pair has positive probability.
The theorem is imported, not reproved. Its single-map and uniform-input
hypotheses are verified below before application.

**1. Common residual rows and the possible unseen label.** Let S_L,S_R
be the full ambient stars, selected by b in F_L and a in F_R.
Their intersection contains W. Positive overlap forces
sigma'^{-1}(a)=(t_1,y_1) for some t_1 in T, because dummy labels
occur in no polynomial block. Set t_0=16. Remove the common 62-set
K union {a,b} from both stars, obtaining residual six-subset families
R_L,R_R in Y. Removal is injective on their union. Each family has
q^2 rows: its polynomials have one prescribed evaluation, and values
at the other six arguments distinguish them. Put

\[
\mathcal W=R_L\cap R_R,\qquad m=q^2-|\mathcal W|\le q.
\]

This uses the full ambient intersection, which may exceed the retained
overlap. Each side has exactly m omitted rows relative to this common
family. Its used labels form six disjoint columns, each of size q.
Each label lies in q rows. Two labels in different columns lie in a
unique row, by interpolation at those two arguments and t_i; two
distinct labels in one column never cooccur.

Write U for the union of the common residual family mathcal W. On either
side a full used label can be absent from U only if all its q rows
are omitted. There cannot be two such labels: their incident-row sets
are disjoint if they share a column, and intersect in exactly one row
otherwise. Their union would have size at least 2q-1>m. Hence at most
one label disappears on each side. Since each full used set has size
6q, the number e of disappearing labels is the same on both sides,
and e is either zero or one. Each observed column (its intersection
with U) has size q or q-1. If e=1, m=q, and the omitted rows are
exactly the q rows through the missing label. Every other used label
then lies in at most one omitted row.

**2. Recovering the observed columns without untouched points.**
Call a subset of U independent if no two of its distinct points
cooccur in the common residual family. Every observed right column Q is independent.
Relative to the six full left columns P_i, let n_i=|Q intersect P_i|,
n=max n_i, and t=|Q|-n. Since |Q|>=136, n>=23.
Choose a column P_i attaining n. Each of the n*t cross pairs between
Q intersect P_i and Q minus P_i occurs in a unique left full row,
and that row must be omitted, by independence. An omitted row contains
at most one selected point of P_i and at most five selected points
outside it, so accounts for at most five such pairs. Thus

\[
nt\le5m\le685.
\]

If 23<=n<=130, then t>=136-n and
n(136-n)>=min(23*113,130*6)=780>685; the minimum is at an
endpoint because this quadratic is concave. Therefore n>=131.
If t>=2, take two outsiders y,z in Q minus P_i. For each outsider,
its pairings with the n selected P_i points require n distinct omitted
rows through it. The two sets of required rows overlap in at most
one row, by the full-star cooccurrence property. This forces
m>=2n-1>=261>137, impossible. Consequently t<=1, and Q has
at least |Q|-1>=135 points in its dominant left column.

Two different observed right columns cannot have the same dominant
left column, since they are disjoint and 2*135>137. The six dominant
columns therefore give a bijection between the six right and left
columns. We next exclude even one outsider in this correspondence.
An outsider y in Q requires at least 135 omitted left rows through y,
one for each dominant point of Q. Two distinct outsiders, wherever
they lie, would require at least 2*135-1>137 omitted rows. Thus there
is at most one outsider in all six right observed columns together.

If e=0, both partitions have six full q-point classes on the same U.
A single outsider is impossible: its dominant class would receive a
point from another left class, hence omit a point of its own q-point
left class; that omitted point must occur in a different right class
and is a second outsider. If e=1, every point of U belongs to at most
one omitted left row by step 1, so even one outsider, requiring at
least 135, is impossible. Hence in both cases there are no outsiders.
Each observed right class is contained in its distinct dominant left
class. Since both partitions cover U, these observed classes are
exactly equal. In particular, if e=1, their unique short columns
correspond to each other.

**3. An auxiliary labeling with common full columns.** If e=0, take
pi to be the identity on H. If e=1, let x_L,x_R in Y be the respective
missing full used labels. If they coincide, again take pi to be the
identity; otherwise take pi to be the transposition of x_L and x_R,
fixing every other element of H. Both missing labels are outside U.
If they differ, x_L is not in the right full used set U union {x_R},
and x_R is not in the left full used set U union {x_L}.
In all cases pi fixes U,K,a,b pointwise. Define
tilde sigma'=pi composed with sigma'. It is still a bijection onto
H minus C', with the same preimage (t_1,y_1) of a. Its full used
columns now equal the left full used columns under the recovered
column correspondence: in the e=1 case, the only added labels complete
the two short columns. Every common residual row is fixed pointwise by pi,
so at least q^2-m common rows persist for this auxiliary labeling.

**4. Completing each partial three-function equation.** Normalize
each side's symbol z at argument t != t_i to (z-y_i)/(t-t_i).
The factorization p(X)=y_i+(X-t_i)(uX+v) identifies the full residual
star with the affine rows {(t,ut+v):t in T minus {t_i}}.
The now common full columns give a column bijection tau and full
symbol permutations f_t:F_q -> F_q, induced by identity on actual
labels. On a set D of q^2-m left coefficient pairs from the common residual family, these
maps send the entire left affine row to a right affine row.

Fix two distinct left arguments s_1,s_2 and a third s_3; put
r_j=tau(s_j). With X=us_1+v and Z=us_2+v, define

\[
A=(s_2-s_3)/(s_2-s_1),\quad B=(s_3-s_1)/(s_2-s_1),
\quad A'=(r_2-r_3)/(r_2-r_1),\quad B'=(r_3-r_1)/(r_2-r_1).
\]

All four coefficients are nonzero. The coefficient-to-(X,Z) map is
a bijection, so a set E subset F_q^2 of size q^2-m satisfies

\[
f_{s_3}(AX+BZ)=A'f_{s_1}(X)+B'f_{s_2}(Z).                 \tag{1}
\]

At most floor(m/2)<=68 rows of the square contain two or more pairs
outside E, and the same holds for columns. Thus at least 69 rows
and at least 69 columns each miss at most one pair. Their intersections
number at least 69^2=4761>m, so choose (X_0,Z_0) in E with both its
row and its column missing at most one pair. Put c=AX_0+BZ_0 and
h(w)=f_{s_3}(c+w)-f_{s_3}(c). This is a permutation of F_q and h(0)=0.
Subtract (1) at (X_0,Z_0) from the valid instances on these two lines.
For all but at most one X, respectively one Z, this gives

\[
h(A(X-X_0))=A'(f_{s_1}(X)-f_{s_1}(X_0)),\qquad
h(B(Z-Z_0))=B'(f_{s_2}(Z)-f_{s_2}(Z_0)).                \tag{2}
\]

For a pair in E at which both identities (2) hold, subtraction in
(1) gives h(U+V)=h(U)+h(V), with
U=A(X-X_0), V=B(Z-Z_0). At most m+2q<=3q ordered pairs are excluded
by these three conditions. This coordinate change is bijective on
the entire square, not just on E. Therefore h is a single full-domain
map between the additive finite groups F_q, and its failure probability
on independent uniform U,V obeys

\[
\delta\le3/q=3/137<2/9.
\]

Apply the cited Theorem 1. Some additive homomorphism g differs from
h on at most q*tau<=q*delta/2<=3/2<2 elements, hence on at most one.
Because F_q is the prime field, every additive homomorphism has form
g(w)=lambda*w: repeated addition of 1 proves this for all elements.
It cannot be zero, since the permutation h takes the value zero just
once and would then disagree with g on q-1=136 elements. Thus g is
a permutation. Two permutations of a finite set cannot disagree on
exactly one element: their images on all the other elements already
coincide, leaving the same single image. Hence h=g everywhere.

Each side of either identity in (2), viewed as a function of X or Z,
is also a permutation: all multipliers are nonzero and all f's and h
are permutations. Each identity holds except at at most one argument,
so the same permutation fact completes both identities everywhere.
Using them, exact additivity of h and (1) at (X_0,Z_0) now proves (1)
for every X,Z, including the originally omitted pairs.

Repeat this argument for each of the four arguments outside the fixed
two anchors. It incurs no accumulated error: each three-function
equation is separately completed on the whole square. Given any left
affine row, its two anchor images specify a unique right affine row;
the four completed equations place all its remaining images in that
same row. Identity on the common full used labels is injective on
subsets, and both families have q^2 rows. Thus the auxiliary right
full residual star equals the left full residual star. Restoring the
common 62-set proves equality of the auxiliary full ambient stars.

**5. Transfer the nonstar matching to the original labeling.** Apply
the structural and nonstar-bijection portions of L126 to sigma and
tilde sigma'. Their full stars are now equal; the left distinguished
column is still 16. Those portions use neither retention nor a packing
inequality for the auxiliary full families. The audited rigidity forces
t_1=16 and supplies lambda in F_q^*, u_0,v_0 in F_q and the bijection

\[
\Phi(p)(X)=\lambda p(X)+(X-16)(u_0X+v_0)+y_1-\lambda y_0
\]

from {p in V:p(16)!=y_0} onto {r in V:r(16)!=y_1}.
For each paired index p, Phi(p), the left support and the auxiliary
right support share the six distinct labels
sigma(t,p(t)), t in T minus {16}, as well as K. Each of these six
labels lies in the left full used set. If pi is nontrivial, that set
is U union {x_L} and excludes x_R; pi moves at most one of the six
labels. Since pi is its own inverse, reverting the auxiliary right
support to the original right support preserves at least five of
these common labels. If pi is trivial it preserves all six. Thus
the original paired supports intersect in at least 60+5=65>63.

They are distinct: the left nonstar contains a and excludes b, while
the right nonstar contains b and excludes a. The transposition fixes
a and b and never changes this distinction or the nonstar index sets.
Therefore every pair is forbidden by the original retention hypothesis.
There are N=q^3-q^2=2552584 disjoint such pairs covering both full
nonstar index sets. Polynomial-to-support maps are injective on each
side, since seven evaluations distinguish degree-at-most-two
polynomials, and Phi is the established bijection. Summing at most
one retained endpoint per pair bounds the retained nonstar size sum
by N. The retained star family is exactly W on each side, contributing
s to each size, even though equal supports are identified in their
union. Consequently the total is at most N+2s=2589848, and at least
one family has size at most 1294924. This is 237572 below 1532496;
the sum is 475144 below twice that threshold.

**Original attempt and qualifications.** The original attempt was symbolic;
it used no numerical search or new mathematical program. Its critical
points for the separate audit were recovery of observed columns from
the deletion budget, completion of possibly different unseen labels,
the independent-uniform error count for h, permutation elimination of
one disagreement, and the loss of at most one of the six matched labels
when undoing pi. Original ambient equality is unnecessary and has not
been inferred. The auxiliary families need not satisfy a packing bound;
only the original retained families do. The original attempt reused the
finite rigidity certificate through audited L126 without rerunning it.

**Separate critical audit, 2026-10-26.** The pre-existing
[SPECIALIZE audit assessment](../drafts/literature/2026-10-26-l129-critical-audit-coverage.md)
approves exactly this audit. The verdict is acceptance under the stated
hypotheses, with no change to the bound or its mathematical argument.
This audit is REPRODUCTION: local verification of the earlier candidate,
not a claim of progress beyond the sources checked. The original
boundary assessment, inspected primary stability coverage and accepted
L126 are reused; no additional literature discovery is needed.

The following independent checks address every boundary implication.
Removing K,a,b is injective on shared supports, and each full star
has exactly q^2 residual rows. Thus m<=q follows from retained overlap,
without identifying retained and ambient overlap. A missing label
requires q omitted rows. For two missing labels the union of their
incident rows has size 2q or 2q-1, both above q. The same observed
union U on both sides makes the missing-label counts equal. When
e=1, the omitted set is precisely the missing label's incidence set;
any observed label has zero or one row in that set. This includes
observed labels in the same column as the missing label.

For each observed right column Q, n>=23 and nt<=5m count pairs
with their exact left row, so no multiplicity assumption is hidden.
Every n from 23 through 130 gives n(136-n)>=780>685. Hence n>=131;
two outsiders would need at least 261 omitted rows. Each remaining
possible outsider needs at least 135 omitted rows, so two distinct
outsiders anywhere need at least 269. Six distinct dominant columns
follow from 2*135>137. In the e=0 case, one outsider forces another
by equality of class sizes and coverage of U. In the e=1 case, even
one contradicts the zero-or-one incidence count just checked.
Consequently observed columns coincide, including their short column
if present. This does not use an untouched-point assumption at m=q.

If the missing labels differ, each is absent from the other side's
full used set. Both lie in Y, outside U. Their transposition therefore
fixes K,a,b and every observed row and sends exactly the right missing
label to the left missing label. It aligns the entire six-column used
sets and retains a genuine ambient bijection. It need not fix labels
in the unused distinguished column, nor is that required. When e=0
or the missing labels agree, the identity handles the case.

For the partial functional equation, the original coefficient map to
(X,Z) is a bijection of the full square; all four interpolation
multipliers are nonzero. With m<=137, at least 69 lines in each
direction miss at most one pair. At least one of their 4761 crossings
lies in E. Thus the chosen base instance really is valid, and each
base-line identity fails at at most one argument. The union of the
missing E pairs and the two possible bad-coordinate strips has size
at most m+2q<=411. The separate nonzero coordinate scalings and
translations send the uniform full square bijectively to the uniform
full square. They do not sample conditionally on E. The single map h
therefore meets precisely the cited theorem's finite-group and
independent-uniform hypotheses with delta<=3/137<2/9.

For positive delta, rationalization gives tau=2 delta/(3+sqrt(9-24
delta))<=delta/2; indeed the square root exceeds 1 throughout the
range used here. Hence q tau<=3/2<2. At delta=0 exact additivity
holds on every pair, with no limiting argument. Prime-field additivity
makes g scalar multiplication. A zero g would disagree with the
permutation h at 136 arguments, contradicting the at-most-one bound.
Nonzero g and h are permutations, so one disagreement is impossible.
The same argument completes each base-line identity because both of
its sides are permutations. Exact additivity and the valid base
instance then recover the full three-function equation. Repeating
with the same two anchors for each remaining coordinate specifies
one right affine row for every left row. There is no accumulated
error or assumed agreement between independently chosen approximations.
Injectivity and the equal q^2 cardinalities prove auxiliary star equality.

L126's structural paragraphs and its explicit inverse for Phi use
only full ambient star equality; full retention and the packing bound
first enter its later counting paragraphs. Reading L125's underlying
proof confirms that arbitrary symbols become affine over this prime
field and the projective map runs from the right six-set to the left
six-set, with no pole on the source. Every such map is uniquely
determined by the images of three fixed distinct source points.
Thus the seven choices of removed point and 120 ordered target triples
are complete. Their sole identity survivor forces t_1=16 and the
scalar linear part needed for L126's formula. No probability law or
auxiliary packing hypothesis has entered this chain.

For each nonstar polynomial, the auxiliary paired support shares six
distinct labels in the left full used set, all outside K,a,b. That
set excludes x_R when the transposition is nontrivial, so at most
the single label x_L is moved. Undoing the transposition preserves
five labels and all 60 points of K, giving an original intersection
at least 65>63. The supports remain distinct by opposite a/b membership.
Phi is still bijective on the original nonstar polynomial indices;
the transposition changes labels, not this index set or its size.
Polynomial evaluation is injective on each family's supports. The
resulting N disjoint forbidden pairs therefore bound the retained
nonstar size sum by N. Each side's retained star is exactly W and
contributes s separately, even though its supports coincide in the
union. This verifies the factor two without full-star retention.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_l129.py`.
The complete certificate is `scripts/finite-support/l129-critical-audit.json`.
The audit checks hashes linking L126 to the unchanged L125 audit and
original rigidity inputs, complete equality with L125's 840 records,
all ordered anchor cases, each determinant, all six images with poles,
and every acceptance decision. The only accepted map remains the
identity with removed point 16. All records are checked programmatically,
not by a preview. It also checks the full excluded dominant-size range,
base-line counts, exact rational stability thresholds and every final
size comparison. Complete check, arithmetic, stability, accepted-map
and empty-failure fields were inspected. All checks pass.

The verified sum bound 2589848 is below required 3064992 by 475144;
the smaller-size bound 1294924 is below required 1532496 by 237572.
The certificate checks arithmetic and the inherited finite input, while
the universal reasoning is the symbolic audit above. No enumeration
of retained families or proof of sharpness is claimed. Original ambient
star equality, lower overlaps, unequal retained indicators, arbitrary
laws, global compatibility and RS realization remain outside this result.
The grand challenge remains IN_PROGRESS. This dated acceptance supersedes
the overview's pending-audit qualification without changing its argument.

## Mathlib

The full boundary theorem: **not checked**. Supporting incidence counts,
finite permutations, prime-field additive maps, the cited finite-group
stability theorem and the finite matching count: **not checked**. Local
audited L126 is a mathematical input, not a Mathlib coverage assertion.
The ready source comparison found no matching theorem; the original
attempt's POTENTIALLY_NEW records that limited comparison, not certified originality or progress
beyond all known literature.
