# L076 — Automatic fullness of an affine-plane transversal

## Hypotheses

Let k=F_97, H its order-sixteen multiplicative subgroup, and F=F_(97^20).
Fix any bijection from the sixteen abstract points of L072 to H. Use
exactly its sixteen selected blocks, in four parallel classes. Put
V=F^8, m_x=(x,x^2,...,x^8)^transpose, and U_A=span_F{m_x:x in A}.
Let S be a two-dimensional subspace of V meeting every U_A nontrivially.
No full-coefficient condition is assumed. The auxiliary F_4 specifies
incidence only. For the matrix-rank consequence use L075, including
its unaudited L073/L074 inputs.

## Conclusion

For every A, S intersect U_A is a line, and every nonzero t_A on that
line has all four coefficients nonzero in its unique moment-column
expansion. Moreover S contains none of the moment columns. All sixteen
intersection lines are distinct.

Consequently L075's 96-by-28 matrix M has rank 27 if and only if this
labeled family admits an L010 equality pencil over F. Its 64 nonzero
coefficient gates follow automatically in the rank-27 case, and L075
constructs an equality pencil already over k. Rank 28 excludes it.
Thus a rank-27 labeling would be a realization, rather than a candidate
that could still fail a full-weight test.

No rank-27 labeling or uniform rank-28 theorem is exhibited here. This
conditional criterion does not decide the family, improve the global
11/q–16/q interval, or resolve the challenge qualifications. This result
and the earlier L073/L074/L075 chain need a separate critical audit.

## Proof

### Intersections and a finite-chart test

L010 gives independence of any eight distinct moment columns, hence
of every smaller set. Each U_A has dimension four. Disjoint blocks
have complementary spans. Since each A has a disjoint block B in
its parallel class, S cannot lie in U_A: that would make its required
intersection with U_B zero. Thus S intersect U_A has dimension one.
Choose a nonzero t_A on it, and write

    t_A = sum_(x in A) w_(A,x) m_x,
    R_A = {x in A : w_(A,x) != 0}.

The support R_A is nonempty and independent of scaling t_A. For
distinct blocks A,B, independence on A union B gives

    U_A intersect U_B = span{m_x : x in A intersect B}.       (1)

Indeed subtracting their two column expansions forces coefficients
outside the intersection to vanish. L072 has |A intersect B|<=1.
In particular coincident intersection lines require a moment-column
line in S. Lines for disjoint blocks are always distinct.

We will use the following direct application of L010 twice. Choose
a finite chart of S whose excluded projective point avoids all its
at most sixteen intersection lines. Such a chart exists: F contains
k and its projective line has at least 98 points. In a basis u,v of
S with v at the excluded point, scale each distinct intersection line
to u+gamma v. Its coefficients give an error e_gamma with syndrome
u+gamma v, supported on the corresponding R_A. If multiple blocks
give one line, their normalized errors agree whenever asserted below.
Choose input words a,b with sigma(a)=u and sigma(b)=v using L010's
surjective moment map.

If a full four-support error occurs, L010's pointwise formula gives

    D(gamma)=det(V_A)^2 product_(x in A)(e_gamma(x)x) != 0,
    L(gamma,X)=D(gamma) product_(x in A)(X-x).              (2)

Thus D is a nonzero polynomial. If for every y in H there is such a
full support A avoiding y, (2) also gives ell_y(gamma)!=0. All locator
polynomials are then nonzero. L010 applies to this constructed pencil,
including every lower-weight event and its multiplicity cost. It
provides same-support failure; it is not being inferred merely from
projected compatibility. The chart changes only the basis of S, and
the weights are not assumed to be in k.

### A moment column in S is impossible

Suppose m_x belongs to S. The four blocks through x have intersection
line F m_x, by the dimension-one assertion. Their normalized error
is one and the same nonzero weight-one vector at x.

Every block A avoiding x is full. To prove this, its parallel class
has exactly one block containing x and three avoiding x. Choose a
different avoiding block B in that class. Their disjoint moment spans
make t_A,t_B independent, so they span S. If |R_A|<=3, then

    |R_A union R_B union {x}| <= 3+4+1 = 8.

Independence of those columns would imply m_x is not in the span of
t_A,t_B, contradicting m_x in S. Hence |R_A|=4. This argument applies
to each of the twelve blocks avoiding x.

Their twelve full intersection lines are distinct: by (1), a common
line between two blocks would be supported on at most one coordinate,
contrary to four nonzero coefficients. They differ also from F m_x.
There are therefore twelve distinct full events and one weight-one
event in the chart above. Each coordinate y belongs to only four
selected blocks, so among these twelve full blocks at least eight
avoid y. Formula (2) verifies all L010 nondegeneracy hypotheses. Its
weighted inequality would give

    64 >= 4N_4+16N_3+32N_2+48N_1+64N_0
       >= 4*12+48 = 96,

a contradiction. Thus S contains no moment column. In particular
|R_A|>=2 for every A, and (1) makes all sixteen lines distinct.

### Two disjoint deficient blocks are impossible

Suppose disjoint blocks A,B in one parallel class both have fewer
than four nonzero coefficients. Then 2<=|R_A|,|R_B|<=3. Choose an
abstract point v whose label is in R_A. In the full auxiliary affine
plane there is one omitted parallel class, namely slope u+1. Its
line through v meets B in exactly one point. Since R_B contains at
least two points, choose w in R_B not on that omitted line.

The unique auxiliary line through v,w is therefore selected. Call
it C. It is not in the parallel class of A,B, since v and w lie in
different blocks of that class. It meets A only at v and B only at
w. This uses just the coordinate affine-plane construction cited in
L072: different parallel classes meet once, and every pair of points
has a unique line in one of the five classes. More explicitly, points
with equal auxiliary X share a vertical line; otherwise their unique
slope is (Y-Y')/(X-X'). Excluding the omitted slope selects C. No RS
label permutation or embedding of F_4 into F is involved.

The actual moment columns indexed by

    R_A union R_B union C

are independent, because this union has size at most 3+3+4-2=8.
The vectors t_A,t_B span S, so t_C=alpha t_A+beta t_B. There is a
point in R_A outside C, since |R_A|>=2 and C meets A once. Comparing
its coefficient in these independent columns gives alpha=0. A point
in R_B outside C gives beta=0 in the same way. Then t_C=0, a
contradiction. Thus each parallel class has at most one deficient
block, and at least three full blocks. There are at least twelve
full blocks overall.

### The weighted bound forces every block to be full

For each y, at most four of the at least twelve full blocks contain
y. Formula (2) again verifies D and every ell_y are nonzero
polynomials. As S contains no moment column, its sixteen intersection
lines are distinct, so the chart gives sixteen distinct parameters,
each with a nonzero error of weight at most four. L010 makes all of
them bad on the same complementary supports and supplies

    4N_4+16N_3+32N_2+48N_1+64N_0 <= 64.                 (3)

Each of the sixteen events costs at least four in (3); a weight-two
or weight-three event costs strictly more. Already one deficient
event would give at least 15*4+16=76, contradicting (3). Weight one
was separately excluded. Hence all sixteen chosen blocks are full.
The same inequality excludes any additional sparse parameter, as
in L010's equality argument. In particular no singular event or
lower-weight representative has been dropped before applying it.

### Consequence for the fixed-H rank test

L075 says M has rank 27 or 28 and, at rank 27, its rational kernel
defines a plane S meeting every U_A in a line. The result just proved
verifies all 64 of L075's coefficient gates. Its finite-chart
construction then supplies all L010 equality gates already over k,
and still over F. Conversely L075's necessary-kernel argument gives
rank 27 from any equality realization. Rank 28 and realization are
therefore mutually exclusive and exhaustive for a given labeling.

The new local result is automatic fullness, not a fixed-H rank
decision. It shows why the proposed uniform zero-coefficient test
cannot settle this family: a surviving kernel cannot have such a
zero. A closure requires either a uniform rank-28 proof for all
bijective labelings or an exact rank-27 labeling. The latter must
still be recorded with its full kernel and the L075 construction,
and critically reviewed; no such labeling is supplied here. The
ready EXPLORE comparison did not establish literature coverage of
this specialization, which does not certify its originality.

## Mathlib

Coverage of this exact family-specific automatic-fullness statement
is not checked. No Mathlib theorem is used; unknown availability is
not evidence of absence. L010 supplies the already established
moment independence, full-error determinant formula, same-support
argument and weighted inequality. L072 supplies the cited design and
its specialization. L075 supplies only the corank, descent and
conditional realization inputs for the final rank consequence. No
general design or decoding theorem is reproved.
