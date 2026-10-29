# L162 — An explicit original four-row infinite family

## Hypotheses

Let E be the algebraic closure of F_97. Coordinates of W=E^7 are
ordered by S=(1,8,12,18,22,27,33), and

    J={47,50,64,70,75,79,85,89,96}, H=S union J.

Use exactly L109's original quotient maps: for a label j=(I_j,K_j),
put g_j(X)=product over z in J minus K_j of (X-z),
z_j=min(S minus I_j), and

    (Q_j w)_r=g_j(z_j)w_r-g_j(r)w_(z_j),
                  r in (S minus I_j) minus {z_j}, increasing.

Let V_j=ker Q_j. Select these four original labels, without a
symmetry quotient:

| row | I_j | K_j | zero-based lexicographic label |
| --- | --- | --- | --- |
| a | {1,8} | {89,96} | 35 |
| b | {12,33} | {64,85} | 522 |
| c | {12,27} | {50,70} | 477 |
| d | {18,22} | {75,79} | 566 |

Write T_j=I_j union K_j. The ordering is I outermost, both I and K increasing lexicographically
in binom(S,2) times binom(J,2), starting at zero. In particular a<b
and c<d. The designated supports T_a,T_b are disjoint, as are T_c,T_d.
The only nonempty intersection among all six support pairs is
T_b intersect T_c={12}. Thus all six intersections have size at most
one. No coding, weight, chart or descent hypothesis is imposed.

## Conclusion

Read all entries in the following vectors modulo 97:

    x_0=( 2,50, 5,77,16,45,81),
    y_0=(75,32, 0,69, 3, 1, 0),
    x_1=(58,92, 4,81,71,36,26),
    y_1=( 0, 0,30, 0, 0, 0, 1).

For every [r:s] in P^1(E), define

    X=r*x_0+s*x_1, Y=r*y_0+s*y_1,
    L_[r:s]=span_E(X,Y).

This is an injective family of two-dimensional planes with

    rank(Q_j restricted to L_[r:s])=1, j=a,b,c,d.

Their four kernel-intersection lines, in order, are

    E X, E Y, E(X+Y), E(X+26Y).

They are pairwise distinct. There are no excluded projective
parameters, including r=0 or s=0. Since E is infinite, this is an
explicit infinite family on the exact approved original domain.
It refutes universal four-row finiteness on that domain. It does not
claim to exhaust the four-row locus or to satisfy any coding gates.

This local counterfamily passed its separate critical audit on 2026-10-26,
as recorded below. It is not
a disproof or complete candidate solution of the MCA challenge.
Classification is REPRODUCTION of elementary linear-algebra tools
with a new local counterexample certificate; no source-level novelty
claim is made.

## Proof

### Standard input, discovery, and the required specialization

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-10-25-four-row-finiteness-review.md`.
For kernels, rank-nullity, direct sums and linear-system consistency,
use A. I. Kostrikin and Yu. I. Manin, *Linear Algebra and Geometry*,
Gordon and Breach, 1997 paperback, ISBN 90-5699-049-7, Chapter 1
Theorem 3.12, pp. 20–21, and sections 6.2–6.9, pp. 44–46,
[primary book](https://www.math.mcgill.ca/darmon/courses/19-20/algebra2/manin.pdf).
These tools apply over E, an arbitrary-field setting. No inspected
source supplies this original quadruple or its family: the explicit
map identities and all-parameter applicability checks below are
necessary. No enumerative, generic or complex-field theorem is used.

L161's residual h=8 pencil motivated this choice. The preliminary
scalar test in `scripts/seven-coordinate/residual-pencil-singletons.json`
left survivors; it was not a realization theorem. The present proof
uses only the displayed original maps and exact vectors. It does not
use the correctness or completeness of L159–L161, their pencil
classification, L153's census or C155a as mathematical premises.
Those results retain their existing audit status.

### Complete actual-map identities and pair disjointness

Substitution in the product definition of g_j gives the following
four-by-seven matrices, with the original target-row order:

    Q_a = [ 0  0 87 46  0  0  0
            0  0  8  0 46  0  0
            0  0 71  0  0 46  0
            0  0 89  0  0  0 46 ],

    Q_b = [18 73  0  0  0  0  0
           57  0  0 73  0  0  0
           32  0  0  0 73  0  0
           43  0  0  0  0 73  0 ],

    Q_c = [83 51  0  0  0  0  0
           91  0  0 51  0  0  0
           63  0  0  0 51  0  0
           95  0  0  0  0  0 51 ],

    Q_d = [ 4 27  0  0  0  0  0
           13  0 27  0  0  0  0
           10  0  0  0  0 27  0
           36  0  0  0  0  0 27 ].

Direct multiplication, for each i=0,1, gives eight vector identities

    Q_a x_i=0, Q_b y_i=0,
    Q_c(x_i+y_i)=0, Q_d(x_i+26*y_i)=0.                 (1)

Each equality here is a four-component zero vector, giving 32 scalar
equalities in total. Thus (1) holds
identically for X,Y with arbitrary coefficients r,s in E; these
are linear identities, not a finite sample of parameter values.

For completeness, pair disjointness is certified directly on these
matrices. Number rows of each eight-by-seven stack from zero. In
the stack (Q_a;Q_b), select rows (0,1,2,3,4,5,7); its integer
determinant on the displayed residue representatives is

    158723284464 = 24 (mod 97).

In the stack (Q_c;Q_d), select rows (0,1,2,3,5,6,7); its determinant is

    -70496180091 = 77 (mod 97).

Both are nonzero over F_97 and every extension. Both stacks therefore
have rank seven, proving

    V_a intersect V_b=0, V_c intersect V_d=0.          (2)

All values in (1)–(2), the matrices and the vector entries are exact
finite arithmetic; the full certificate also retains each selected
minor and each zero residual, permitting direct verification.

### Nonzero vectors, all ranks, and all parameter values

The two vectors (x_0,y_0),(x_1,y_1) in W direct sum W are linearly independent: the
coordinates of Y at 27 and 33 are respectively r and s. Therefore
(X,Y) is nonzero whenever (r,s) is nonzero.

If X=0, (1) gives Y in V_c and 26Y in V_d. Since 26 is nonzero
and (2) holds, Y=0, a contradiction. If Y=0, (1) puts X in
V_c intersect V_d, again a contradiction. Thus X and Y are both
nonzero. By (1), they belong to V_a and V_b; their independence
now follows from (2). Their span is a plane.

On that plane Q_a kills X but not Y, since a nonzero Y cannot
belong to both V_a and V_b. Thus Q_a has rank exactly one. The
same argument gives rank one for Q_b. The vectors X+Y and X+26Y
are independent: their coefficient determinant in the basis X,Y
is 26-1=25, nonzero in E. They belong to V_c and V_d respectively
by (1). Disjointness in (2) implies that Q_c kills the first but
not the second, and Q_d kills the second but not the first.
These two ranks are also exactly one.

The four kernel-intersection lines are consequently precisely the
ones displayed in the conclusion. In the basis X,Y their projective
coordinates are [1:0], [0:1], [1:1], [1:26]. They are all distinct
because 26 is neither 0 nor 1. No division by r, s or a generator
coefficient was made, so no zero-coefficient or endpoint case was lost.

### Projective well-definedness and distinct planes

Scaling (r,s) by a common nonzero scalar scales X,Y by that scalar,
so it preserves their span. Suppose another parameter [r':s'] gives
the same plane. The exact ranks just proved uniquely specify its
intersections with V_a and V_b, so X'=lambda*X and Y'=mu*Y for
some nonzero lambda,mu in E. Its intersection with V_c is also
unique. Thus X'+Y' is a nonzero scalar multiple of X+Y. Independence
of X,Y forces lambda=mu. Comparing coordinates 27 and 33 of Y'
and Y gives (r',s')=lambda*(r,s). Hence the two projective parameters
are equal. This proves injectivity.

An algebraically closed field is infinite: if E were finite,
the nonconstant polynomial product over u in E of (T-u)-1 would
have no root in E, a contradiction. Therefore P^1(E) and this
injective family are infinite. This completes the counterexample to
the universal finiteness assertion, with every parameter accounted for.

### Reproduction and limits

Run from the active notebook:

    python3 scripts/seven-coordinate/residual_pencil_family.py

The complete certificate is
`scripts/seven-coordinate/residual-pencil-family.json`. It records
the original labels and all six intersections, the four maps, the
sixteen-by-fourteen linear system for (x,y), its row reduction and
two-vector kernel, all residuals, parameter independence, and the
two integer minor determinants. It checks the maps again by an
independent implementation of their defining products. Actual kernel
dimension is two (required two), both pair ranks are seven (required
seven), the minor residues are 24 and 77, and failures is empty.
The proof needs only the two explicit independent vectors and (1)–(2),
not a claim that row reduction exhausts every four-row plane. The
complete load-bearing vectors, matrices, selected minors and zero
residuals were inspected, not merely a bounded preview.

This is a counterfamily for four rank conditions, not for the original
MCA target. It neither supplies twelve compatible rows nor a second-pair
extraction theorem. Although its formulas are over F_97, its infinite
parameter set is over the algebraic closure; no finite coding-field
cardinality conclusion follows. Recovery weights, all original chart
and nonpersistence gates, representation, challenge identification
and radius remain unproved. The 11/q–16/q interval is unchanged.

### Separate critical audit, 2026-10-26

The first independent audit under the saved SPECIALIZE assessment
`drafts/literature/2026-10-26-l162-critical-audit-review.md` passes on
the full stated domain. It reuses the precise arbitrary-field source
coverage above; the necessary specialization is the explicit arithmetic
and all-parameter proof, not a reproof of a general linear-algebra theorem.

Run the independent check from the active notebook:

    python3 scripts/seven-coordinate/audit_l162.py

Its complete certificate is
`scripts/seven-coordinate/l162-critical-audit.json`. The checker imports
neither the producer script nor any prior certificate. It enumerates
the specified Cartesian label order, evaluates each defining product,
and computes the displayed integer minors by the Leibniz formula,
without using the producer's elimination. All four original labels and
maps match. All six support intersections match: only b,c intersect,
at 12. The sixteen specified nonzero field elements satisfy t^16=1,
confirming the original subgroup. All eight four-component identities
vanish, and both seven-column stacks have rank seven, with minor
residues 24 and 77. The complete labels, product values, maps, vector
identities, minors and parameter-recovery matrix were inspected. There
are no failed checks. The original phrase "sixteen identities" was a
counting typo, corrected to eight vector identities (32 scalar equalities).

The all-parameter argument was checked separately from the arithmetic.
The coordinate map Y -> (Y_27,Y_33) recovers (r,s), so a nonzero
parameter never gives the zero pair. If X or Y were zero, (1),
26 != 0 and V_c intersect V_d=0 would force both to vanish. The
nonzero X,Y in the disjoint kernels V_a,V_b are independent. The
coefficient determinant 25 makes X+Y and X+26Y independent; disjointness
of V_c,V_d then excludes rank zero in the remaining restrictions.
Thus each of the four kernels meets the plane in precisely its stated
line, for every parameter. All identities and nonzero minors remain
valid under the field inclusion F_97 -> E. In particular the proof
excludes no endpoint and uses no base-field sampling inference.

Projective scaling preserves the plane. Equality of two planes forces
their X and Y lines to agree; agreement of their X+Y lines forces the
same scaling on both generators. Recovering (r,s) from Y then proves
injectivity, including r=0 and s=0. The stated polynomial argument
establishes that E is infinite. No classification, full pencil-kernel
dimension, scheme structure, descent, additional-row compatibility or
coding realization is needed or certified. This verifies the local
counterfamily and its obstruction to unconditional four-row finiteness,
not a solution or disproof of the MCA challenge.

## Mathlib

Full matching explicit-family statement: not checked. Supporting
linear algebra, finite-field arithmetic and projective points: not
checked anew. No exact Mathlib theorem name or Lean verification is
claimed. Unknown coverage is not evidence of absence. This is an
informal field-valued construction, not a scheme-theoretic assertion.
