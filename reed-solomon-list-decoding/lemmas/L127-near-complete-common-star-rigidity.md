# L127 — Near-complete common stars determine their full ambient stars

## Hypotheses

Use exactly L030's polynomial model in the two-core setting of L126.
Let |H|=1024, |K|=60, and let a,b be distinct elements of H outside K.
Put C=K union {a}, C'=K union {b}, and Y=H minus (K union {a,b}).
Set q=137, T={16,64,70,102,112,118,121}, and
Omega=(T times F_q) disjoint union D_0, where |D_0|=4.
For every polynomial p over F_q of degree at most two, including zero,
write B_p={(s,p(s)):s in T}. Let
sigma:Omega -> H minus C and sigma':Omega -> H minus C' be arbitrary
bijections, with sigma^{-1}(b)=(16,y_0).

The two ambient stars are families of actual 68-subsets:

\[
\mathcal S_L=\{C\cup\sigma(B_p):\deg p\le2,\ p(16)=y_0\},
\qquad
\mathcal S_R=\{C'\cup\sigma'(B_r):\deg r\le2,
                         \ a\in\sigma'(B_r)\}.
\]

Assume |S_L intersect S_R|>=18633. No packing inequality on their
ambient full families, retained nonstar members, probability law,
column-preserving labels or independence is assumed.

## Conclusion

The two full ambient stars are equal: S_L=S_R. Each has 18769 members.
Thus the exact-star hypothesis needed for L125's rigidity is recovered
from the proposed overlap threshold, under the original arbitrary
ambient bijections.

The separate critical audit of 2026-10-25 below accepts this intermediate
rigidity claim under exactly the stated hypotheses. It is not a candidate
resolution of the grand list-decoding challenge. It gives no lower-overlap
claim, no equality of retained star subsets, no incomplete-star retention
bound, no assertion for arbitrary local laws and no actual RS realization.
The bracket 955–957 and arbitrary-center 67/68 safety remain unresolved.

## Proof

**Scope and imports.** The pre-invocation EXPLORE assessment is
[the near-complete-star source review](../drafts/literature/2026-10-25-near-complete-common-star-rigidity.md).
The changed hypothesis is overlap rather than the complete equality
used in L125. The incidence recovery and reduction to a one-map test
below are the differences not covered by the inspected sources. L030 supplies
the polynomial construction; L125 supplies its normalized affine-star
description. Its exact-star 840-map certificate is not used to assume
any part of the completion being proved.

The external input is Michael Ben-Or, Don Coppersmith, Mike Luby and
Ronitt Rubinfeld, *Non-Abelian Homomorphism Testing, and Distributions
Close to their Self-Convolutions*, Random Structures & Algorithms
32(1) (2008), 49–70, DOI
[10.1002/rsa.20182](https://doi.org/10.1002/rsa.20182), Theorem 1,
p. 3 of the [18-page author preprint](https://people.csail.mit.edu/ronitt/papers/convd.pdf).
For a map f:G->J between finite groups, let delta be its homomorphism
test failure probability for two independent uniform elements of G.
If delta<2/9, a homomorphism differs from f at at most tau|G| elements,
where tau=(3-sqrt(9-24 delta))/12. In particular tau<=delta/2;
the delta=0 case gives tau=0. This precise statement was already
assessed; its hypotheses and bound were rechecked in the primary text
for this application. The theorem is imported, not reproved.

**1. Common used labels and untouched points.** The positive overlap
implies sigma'^{-1}(a)=(t_1,y_1) for some t_1 in T: a dummy point
lies in no polynomial block. Set t_0=16 and S_i=T minus {t_i}.
Remove K,a,b from every member of each star to obtain six-subset
families A_L,A_R in Y. This removal is injective on the union of the
stars, since every support contains K,a,b. Consequently it preserves
both family sizes and intersection size.

Each star has q^2=18769 distinct members, because the polynomials with
a specified evaluation form a two-dimensional affine space and
different such polynomials cannot agree at six other distinct points.
Put W=A_L intersect A_R and m=q^2-|W|. Thus 0<=m<=136=q-1, and
exactly m rows of each full residual star are absent from W.

The used points of A_i are exactly the six labeled columns
S_i times F_q. Every such point lies in exactly q rows: prescribing
its value and the distinguished value leaves one free coefficient.
Any two points in different columns lie together in exactly one row,
by interpolation at three distinct arguments. Distinct points in a
single column never cooccur. These statements hold after either
arbitrary ambient bijection. Since m<q, every used point still occurs
in W. The two full used ground sets therefore agree with the common
set U=union W, of size 6q. Unused distinguished-column and dummy
labels cause no ambiguity inside U.

Fix any one left column. Each omitted left row touches one point of
it, so at most m<q points in the column touch an omitted row. Choose
a point x which touches none. It has degree q in W. The right full
star also has degree q at x, so none of its right rows through x is
omitted either. Define N(x) to consist of x and all other points of U
which do not cooccur with x in W. The complete incidences through x
on the left make N(x) exactly its left column, and the complete
incidences through x on the right make N(x) exactly its right column.
The two columns are therefore the same actual subset of U.

Do this for each left column. The six disjoint left columns become
six distinct right columns, exhausting them. This proves a column
bijection tau:S_0->S_1 induced by the actual ambient labels, with
individual symbol bijections. No guessed correspondence was imposed.

**2. The partial three-function equations.** Normalize a symbol z
at argument s on side i to (z-y_i)/(s-t_i). L125's affine-star
description, from p(X)=y_i+(X-t_i)(uX+v), gives

\[
\mathcal A(S_i)=
 \{\{(s,us+v):s\in S_i\}:(u,v)\in\mathbb F_q^2\}.
\]

The identity on U now has the form
(s,z) -> (tau(s),f_s(z)), with every f_s a permutation of F_q.
There is a set D of q^2-m left coefficient pairs whose rows belong
to W. For each (u,v) in D, some unique right pair (u',v') satisfies

\[
f_s(us+v)=u'\tau(s)+v' \quad(s\in S_0).                 \tag{1}
\]

Fix two distinct anchor arguments s_1,s_2, and choose any other s_3.
Write r_j=tau(s_j), X=us_1+v and Z=us_2+v. The map (u,v)->(X,Z)
is a bijection of F_q^2, so the image D_XZ omits exactly m pairs.
Define the nonzero field elements

\[
A=(s_2-s_3)/(s_2-s_1),\quad B=(s_3-s_1)/(s_2-s_1),
\quad A'=(r_2-r_3)/(r_2-r_1),\quad
B'=(r_3-r_1)/(r_2-r_1).
\]

Interpolation of the left and right affine rows in (1) gives

\[
f_{s_3}(AX+BZ)=A'f_{s_1}(X)+B'f_{s_2}(Z)
                       \quad((X,Z)\in D_{XZ}).          \tag{2}
\]

**3. Exact completion with justified base points.** Because fewer
than q pairs are omitted, there is an X_0 whose entire row belongs
to D_XZ, and a Z_0 whose entire column belongs to D_XZ. Their
intersection also belongs to D_XZ. Set c=AX_0+BZ_0, and define

\[
h(w)=f_{s_3}(c+w)-f_{s_3}(c).
\]

Subtract (2) at (X_0,Z_0) from its valid instances on the full column
and full row. For every X,Z respectively, this proves

\[
h(A(X-X_0))=A'(f_{s_1}(X)-f_{s_1}(X_0)),
\qquad
h(B(Z-Z_0))=B'(f_{s_2}(Z)-f_{s_2}(Z_0)).                \tag{3}
\]

For every surviving pair in (2), subtracting the same base identity
and substituting (3) yields h(U+V)=h(U)+h(V), with
U=A(X-X_0), V=B(Z-Z_0). This is a bijective change of ordered pairs,
since A and B are nonzero. Thus the actual additive test failure
probability for h:F_q->F_q is

\[
\delta\le m/q^2\le136/18769<2/9.
\]

Apply the cited theorem to the additive groups G=J=(F_q,+), with
independent uniform U,V. The resulting homomorphism g differs from h
on at most

\[
q\tau\le q\delta/2\le136/(2\cdot137)=68/137<1
\]

elements. The cardinality of a disagreement set is a nonnegative
integer, hence it is zero. Therefore h itself is additive everywhere.
This upgrades closeness to exact equality; no unproved stability of
the complete-star result is used. For completeness, the displayed
tau<=delta/2 follows by rationalizing
tau=2 delta/(3+sqrt(9-24 delta)); delta<2/9 makes that denominator
greater than 4. At delta=0 it holds directly.

Now take arbitrary X,Z, including omitted pairs. Equations (3),
additivity of h, and the valid base identity at (X_0,Z_0) imply (2)
for this pair too. This completes the three-function equation on the
whole square without ever assuming its original zero row or column
survived. Repeat this argument for each of the four choices of s_3
outside the same two anchors. Each repetition uses the same bound m;
there is no union bound or accumulation of errors between repetitions.

**4. Completion of the actual stars.** For any left coefficient
pair (u,v), choose the unique right affine polynomial u'X+v' whose
values at r_1,r_2 are f_{s_1}(us_1+v), f_{s_2}(us_2+v). The two
anchor images r_1,r_2 are distinct, giving unique
interpolation. All four completed equations (2) assert that its other
four values are exactly f_s(us+v). Thus the identity on U sends every
left residual star block to a right residual star block. It is a
bijection on U, so distinct left blocks remain distinct. The two
families have the same finite size q^2, proving A_L=A_R. Restoring
K,a,b gives S_L=S_R as actual 68-support families, as claimed.

The exact-star rigidity in L125 is now applicable if needed later;
its finite certificate was not invoked prematurely and need not be
recomputed to prove this equality. A later retention argument must
still distinguish ambient equality from which common supports were
actually retained. No such argument is asserted here.

**Verification and audit boundary.** The proof is symbolic; no new
mathematical script or numerical search was needed. The critical
checks are degree preservation under m<q, recovery of whole columns
from an untouched point, the two complete base lines, the bijective
error transfer, the imported theorem's exact hypotheses, and the
integer disagreement bound. Their separate critical audit is recorded
below. The 18633 threshold is exactly 137^2-136; no optimality of
this threshold is claimed.

**Separate critical audit, 2026-10-25.** The pre-invocation
[audit coverage](../drafts/literature/2026-10-25-l127-critical-audit-coverage.md)
permits this unchanged symbolic audit. Verdict: accepted for the stated
ambient-star equality, with no strengthened conclusion. The following
checks address the universal implications, rather than sample bijections.

1. Positive overlap forces the right distinguished label to be active.
   Every support on either side then contains the same 62-set K union
   {a,b}. Removing it is injective even across the two families: adding
   it back recovers the original support. The remaining six values,
   together with the specified distinguished value, distinguish all
   q^2 polynomials. Thus both residual families really omit the same
   number m<=136 of distinct blocks from their intersection.

2. For each side separately, fixing two polynomial evaluations leaves
   q solutions, while fixing three distinct arguments gives exactly one.
   These facts establish degree q, unique cross-column cooccurrence,
   and no same-column cooccurrence without label assumptions. Deleting
   at most 136 rows cannot erase any degree-137 label. In a fixed left
   column the omitted rows touch at most 136 of its 137 points. An
   untouched point therefore has all 137 incidences in W. Its degree in
   the right full star is also exactly 137, so all right incidences
   survive as well. Its set of nonneighbors in U, together with itself,
   is consequently its full column on both sides. Repeating separately
   in the six disjoint columns proves the column bijection; their
   witnesses need not lie on a common row. No degree comparison is made
   at unused labels.

3. L125's factorization p(X)=y_i+(X-t_i)(uX+v) applies algebraically
   before any full-star equality or coupling assumption. On each used
   column the denominator s-t_i is nonzero, so normalization is a
   symbol bijection. The identity on actual U gives the f_s and tau;
   it is not an imposed isomorphism. The two-anchor map has determinant
   s_1-s_2 nonzero. It therefore transports the common coefficient set
   to exactly q^2-m distinct ordered pairs. Distinctness of s_1,s_2,s_3
   and of their images makes all four interpolation coefficients
   nonzero; A+B=A'+B'=1. Equation (2) is exactly interpolation of (1).

4. Fewer than q omitted pairs spoil fewer than q rows and fewer than q
   columns of the square, so both complete base lines exist. Their
   intersection is valid. Subtracting its identity from (X,Z_0) and
   (X_0,Z) gives (3) for every X and every Z, not merely for surviving
   pairs. Subtraction at a surviving (X,Z) then gives precisely the
   additive test at (A(X-X_0),B(Z-Z_0)). This transformation is a
   bijection of the whole square. It transfers the exceptional count
   without conditioning the test distribution; independent uniform
   U,V have failure probability at most m/q^2. Possible additional
   successes in the omitted set only decrease delta.

5. Theorem 1 and the independent-uniform convention were checked again
   in the cited author preprint, p. 3. Both groups here are finite
   additive groups and h is defined on every field element. The exact
   inequality 9*136=1224<2*18769=37538 verifies delta<2/9. For delta>0,
   rationalization gives tau=2 delta/(3+sqrt(9-24 delta))<delta/2,
   since sqrt(9-24 delta)>5/3>1. Thus the disagreement count is at most
   68/137<1 and must vanish. At delta=0 every ordered pair has positive
   uniform probability and none can fail, so h is already a
   homomorphism; this also verifies the endpoint directly without using
   the source's printed strict inequality there. No rounding or
   numerical approximation is involved.

6. For arbitrary X,Z, equations (3), the valid base identity and exact
   additivity give (2), including previously omitted pairs. The same
   anchors and common domain serve all four other coordinates. Each
   coordinate's separately defined h is proved exact on its entire
   domain, so there is no error union or requirement that these h maps
   coincide. For any left row, the two anchor values specify a single
   right affine row, and all four completed equations give its remaining
   values. The identity on U is injective on subsets, so this is an
   injection of the q^2 left blocks into the q^2 right blocks, hence
   equality. Restoring the common 62-set proves the actual-support claim.

No mathematical gap was found in this proof. The DAG row remains
unchanged: L030 provides the construction and L125 the algebraic
normalization; the stability theorem is cited directly above. L125's
840-map classification, L126's nonstar matching, and any retained-size
inequality are not used by this argument. This audit reproduces and
accepts the local candidate, not a new result beyond the checked
literature. In particular, it does not assert equality of retained
subsets or that an incomplete-star packing meets or fails a size bound.

## Mathlib

The full near-complete common-star theorem: **not checked**. The
finite-group stability theorem and supporting interpolation, finite
incidence and cardinality results: **not checked**. The local L125
normalization is a mathematical input, not a Mathlib coverage claim.
The ready assessment found no matching result in the sources checked;
POTENTIALLY_NEW describes this limited comparison, not certified novelty.
