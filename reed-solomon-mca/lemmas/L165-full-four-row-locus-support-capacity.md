# L165 — Complete four-row locus and its support-weight capacity

## Hypotheses

Let E be the algebraic closure of F_97, with W=E^S in the order
S=(1,8,12,18,22,27,33), and J=(47,50,64,70,75,79,85,89,96).
Use the original 756 labels in binom(S,2) times binom(J,2), I outermost
and both pairs in increasing lexicographic order, starting at zero.
For label j write T_j=I_j union K_j and use L109's actual maps

    g_j(X)=product over z in J minus K_j of (X-z),
    z_j=min(S minus I_j),
    (Q_j w)_x=g_j(z_j)w_x-g_j(x)w_(z_j),
                    x in (S minus I_j) minus {z_j}, increasing.

Put V_j=ker Q_j, and fix the ordered labels (a,b,c,d)=(35,522,477,566):

    T_a={1,8,89,96}, T_b={12,33,64,85},
    T_c={12,27,50,70}, T_d={18,22,75,79}.

Let Omega consist of every two-dimensional E-subspace L of W with
rank(Q_j restricted to L)=1 for j=a,b,c,d. No full weight, chart,
nonpersistence, coding or descent condition is assumed. Use audited
C155a's original-pair conclusions, including its L155/L153 finite-input
qualifications; use audited L162's family and L163–L164's exact
family-mask and incidence conclusions. L159–L161 are not premises.

An additional label is eligible when it is different from a,b,c,d
and its support meets each fixed support in at most one coordinate.
For L in Omega, let M(L) be all eligible labels j with exact rank
rank(Q_j restricted to L)=1. For z in S union J, define the ordinary
integer residual capacity

    b_z=4-#{i in {a,b,c,d}: z belongs to T_i}.

These capacities and the weights below are not finite-field numbers.

## Conclusion

The entire field-valued locus is exactly the family of L162:

    Omega = {L_[r:s] : [r:s] in P^1(E)}.

Thus M(L_[r:s]) is precisely L163's forty-label set B when
[r:s]=[1:94], and is empty at every other parameter. In particular,
the single nonnegative coordinate-weight vector

    w_27=1, w_z=0 for z different from 27

covers every support in every M(L) to weight at least one. Its cost is

    sum_z b_z*w_z = 3 < 8.

Every nonnegative real fractional packing of the available supports
within the residual capacities therefore has total size at most three.
In particular no plane in this full four-row locus supports eight
additional distinct eligible rows under degree at most four. The total
row count is at most seven, without an attainment or coding claim.

This excludes this fixed seed from a twelve-row family under these
necessary conditions. It supplies neither a theorem extracting this
quadruple nor exclusions for other quadruples, and does not resolve
the MCA challenge or its radius. The finite certificate has passed
same-step independent checking and the separate step-518 critical proof
audit below. POTENTIALLY_NEW refers only to the new local cover not supplied
by the sources checked, not to certified originality of the method.

## Proof

### Standard inputs and the specialization

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-10-26-full-four-row-capacity-dual-attempt-review.md`
and its step-514 comparison. For arbitrary-field kernels, rank-nullity
and consistency use A. I. Kostrikin and Yu. I. Manin, *Linear Algebra
and Geometry*, Gordon and Breach, 1997 paperback, ISBN 90-5699-049-7,
Chapter 1 Theorem 3.12, pp. 20–21, and sections 6.2–6.9, pp. 44–46,
[primary book](https://www.math.mcgill.ca/darmon/courses/19-20/algebra2/manin.pdf),
as already assessed and imported in L162. All matrices here have
coefficients in F_97; a nonzero minor remains nonzero in E. No new
general linear-algebra theorem is being reproved.

For the finite nonnegative incidence relaxation use S. Boyd and
L. Vandenberghe, *Convex Optimization*, Cambridge University Press,
2004, sections 5.1.3 and 5.2.1–5.2.2, printed pp. 216 and 224–226,
[author PDF](https://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf).
Only the feasible-multiplier/weak-duality bound is needed. Its use below
has a finite ordinary 0/1 incidence matrix, nonnegative integer
capacities, and an explicitly feasible nonnegative dual vector.
No strong duality, solver, edge upper bound, integrality or conflict
multiplier is assumed. The local work missing from these sources is
exhaustion of this particular original four-row locus.

### All possible coincidences of the four kernel lines

Write A=V_a, B_0=V_b, C=V_c and D=V_d; the symbol B without a
subscript continues to mean L163's forty-label set. For L in Omega,
rank-nullity gives a line ell_j=L intersect V_j for each fixed j.
The only nonempty fixed-support intersection is T_b intersect T_c={12}.
For each of the other five pairs, C155a's original disjoint-pair input
gives V_i intersect V_j=0. Apply it with the two labels in increasing
order when necessary. Hence the only possible coincidence among the
four lines is ell_b=ell_c. In particular ell_a and ell_b are distinct,
and C155a writes every L as the span of its unique ordered A and B_0
factor lines. No plane outside their sum has been removed by a chart.

We first exclude ell_b=ell_c. Let e=e_12=(0,0,1,0,0,0,0).
The actual maps satisfy Q_b e=Q_c e=0. In the eight-by-seven matrix
(Q_b;Q_c), the submatrix with zero-based rows (0,1,2,3,5,7) and
columns (0,1,3,4,5,6) has integer determinant

    74121743112 = 55 (mod 97).

Consequently that stack has rank exactly six: the minor gives the
lower bound and its nonzero kernel vector e gives the upper bound.
Thus B_0 intersect C=E e. A coincident-line plane would have the form
span(x,e) for a nonzero x in A and would lie in A+E e.

L109's kernel formula gives

    A=span(e_1,e_8,g_a), g_a=(25,43,46,10,89,26,8).

The four images of (e_1,e_8,g_a,e), as columns under Q_d, are

    [ 4 27  0  0
     13  0 15 27
     10  0 79  0
     36  0 49  0 ].

Its integer determinant is 1716066, residue 39 modulo 97. The four
vectors are therefore independent, and Q_d is injective on A+E e.
Any plane in that space has Q_d-rank two, contradicting membership
in Omega. This eliminates the entire possible coincident-line branch,
not just the planes represented by a nonzero normalization coefficient.

### The normalized three-row space is exactly three-dimensional

All four lines are now distinct. Choose nonzero representatives x in
ell_a and y in ell_b so that ell_c=E(x+y): both coefficients of an
ell_c representative in the two-factor basis are nonzero, since
ell_c is different from both factor lines. Rescaling the two factors
separately therefore gives this normalization. The fourth line has a
representative x+t*y for t in E with t different from 0 and 1; its
x coefficient is also nonzero. These statements use the already
proved line distinctions, not genericity or a base-field parameter.

The pair (x,y) belongs to the kernel of the twelve-by-fourteen matrix

    T = [ Q_a  0
           0  Q_b
          Q_c Q_c ].

Use the four explicitly given vectors x_0,y_0,x_1,y_1 of L162 and put

    Z_0=(x_0,y_0), Z_1=(x_1,y_1), Z_2=(0,e).

L162 supplies T Z_0=T Z_1=0; the identities Q_b e=Q_c e=0 give
T Z_2=0. The three-by-fourteen matrix with these Z_i as rows has
the following minor in columns (0,2,9), where x coordinates precede
y coordinates:

    [ 2 5  0
     58 4 30
      0 0  1 ].

Its determinant is -282, residue 9, so the three kernel vectors are
independent. In T, take rows (0,1,2,3,4,5,6,7,8,9,11) and columns
(0,1,2,3,4,5,6,7,8,10,11). The resulting eleven-by-eleven minor,
using residues 0 through 96 of the original maps, has integer determinant

    703005902194751856 = 94 (mod 97).

This proves rank T at least eleven. The three independent kernel
vectors imply rank T at most 14-3=11. Thus they are a basis of the
whole kernel over E. Every normalized pair, including those with
vanishing coordinates or nonrational parameters, has a unique expression

    (x,y)=alpha*Z_0+beta*Z_1+gamma*Z_2.                 (1)

No census of base-field points is used to infer this exhaustion.

### The fourth row forces precisely the original family

In the four-dimensional target of Q_d, direct evaluation gives

    U=Q_d y_0=(0,5,1,81),
    V=Q_d y_1=(0,34,0,27),
    W_0=Q_d e=(0,27,0,0).

The minor in target rows (1,2,3) of the matrix with these columns is

    [ 5 34 27
      1  0  0
     81 27  0 ],

whose integer determinant is 729, residue 50. Thus U,V,W_0 are
independent over E. L162's exact fourth-row identities give
Q_d x_i=-26*Q_d y_i for i=0,1. Applying Q_d to x+t*y in (1) yields

    0=alpha*(t-26)*U + beta*(t-26)*V + gamma*t*W_0.

Independence implies

    alpha*(t-26)=0, beta*(t-26)=0, gamma*t=0.

Since t is nonzero, gamma=0. The pair (x,y) is not zero, so alpha
and beta cannot both vanish. Therefore t=26 and

    x=alpha*x_0+beta*x_1, y=alpha*y_0+beta*y_1.

This is exactly L162's plane L_[alpha:beta]. Neither alpha nor beta
was divided out; both projective endpoints and every E-valued parameter
remain. Conversely audited L162 proves that each of these planes has
four exact ranks one and that its parameter is unique. This proves
the asserted equality of field-valued loci. No scheme-theoretic
equality, reducedness or descent conclusion is asserted.

### A single cost-three weight covers the full locus

L163's eligible-label definition depends only on the four fixed
supports, so its exhaustive list of 112 labels applies unchanged.
The new locus equality now licenses its complete rank test everywhere
on Omega: the available mask is exactly its forty-label B at [1:94]
and empty elsewhere. In particular, no zero-rank additional row has
been silently treated as rank one or used to discard a plane.

By L164, every label in B has 27 in its support, and fixed row c is
the only fixed row containing 27. Hence b_27=4-1=3. The displayed
weight w has nonnegative entries and gives weight one to each support
in B; it vacuously covers the empty masks. Its cost is three at every
plane. This is a complete cover by one weight certificate, with no
unclassified residual stratum.

For clarity, the imported weak-duality theorem applies with variables
xi_j>=0 on the finite mask M(L), constraints
sum_(j:z in T_j) xi_j<=b_z for every z, and objective sum_j xi_j.
The verified dual vector w satisfies every support inequality and
therefore bounds that objective by three. This includes fractional
multiplicities and requires no constraint xi_j<=1. Selecting distinct
supports is a special case; eight additions would exceed this bound.
No candidate/candidate pair compatibility was assumed by the dual or
needed for this necessary upper bound. All four fixed rows are counted.

### Exact finite evidence and its limits

Reproduce from the active notebook with

```bash
python3 scripts/seven-coordinate/full_four_row_capacity.py
python3 scripts/seven-coordinate/verify_full_four_row_capacity.py
```

The producer saves the complete original maps, the twelve-by-fourteen
matrix T, all three kernel vectors and residuals, every specified minor,
the coincident-line matrix, all fourth-row images and the residual
capacity vector in `scripts/seven-coordinate/full-four-row-capacity.json`.
The generator tests only structural hypothesis H1: complete coverage
by the displayed family after retaining the possible coincident branch.
It performs no all-mask, all-quadruple, parameter-sampling or solver sweep.

The independent verifier imports no producer routines. It enumerates
the original labels with explicit index loops, expands each g_j into
integer polynomial coefficients, evaluates by Horner, and reconstructs
each quotient through normalized coordinate differences with every
denominator checked nonzero. It reads the canonical vectors from L162
and the complete B from L163. All matrices, kernel identities, minor
entries, capacities, forty support weights and relevant incidence tests
are checked. Rational Gaussian elimination evaluates the integer
determinants independently of the producer's modular elimination.
All 157 checks pass, with zero failures. The five determinant residues
are 94,9,55,39,50 for T, its kernel basis, the B_0/C stack, the boundary
map and (U,V,W_0), respectively.

Full results, exact integer determinants, forty support records and
source hashes are in
`scripts/seven-coordinate/full-four-row-capacity-verification.json`.
The complete load-bearing maps, basis, selected minors, fourth-row
coefficients and forty support-weight records were inspected. L163's
earlier all-parameter polynomial identities and C155a's inherited
finite input are reused with their audited qualifications, not reaudited
here. Both new implementations share Python and integer arithmetic.
Same-step independent checks do not replace the separate critical
audit below; no proof-assistant verification is claimed.

Only this seed is excluded. Other quadruples, extraction of a suitable
second pair or this exact seed, q=97^20 and k=8 coding realization,
the pinned cell, U_S, nonzero D and locators, sixteen original finite
events, t=0, recovered weights and original chart, inherited
L056/L069/L040 and L051/L055 qualifications, L104/L151 limits,
arbitrary representation, challenge identification and sharp radius
remain unresolved. L162's infinite-family result and all recorded
failures remain intact. There is no complete challenge candidate.

### Separate critical audit — step 518, 2026-10-26

The first separate conceptual audit passes under the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-26-l165-critical-audit-review.md`.
This is REPRODUCTION/verification of the existing local proof, with no
new locus claim or stronger bound. The arbitrary-field linear-algebra
and weak-duality sources above are reused; no fresh source reading or
general theorem reproof is claimed.

The input statements were checked against the exact ordered S, J,
756-label order, maps and four labels here. C155a applies to each of
the five disjoint fixed-support pairs after sorting its two labels;
its L155/L153 qualifications are retained. Exact restricted rank one
makes each intersection with a kernel a line. If two such lines agree,
they lie in the intersection of the two ambient kernels, so those five
coincidences are impossible. The sole remaining case is b/c. Its
rank-six stack and nonzero kernel vector prove equality with E e_12,
not merely containment. The boundary determinant 39 proves both
independence of the four displayed generators and injectivity of Q_d
on their span A+E e_12. It therefore rules out every plane in that
coincident branch, without a nonzero-coordinate chart assumption.

In the remaining branch, x and y are independent because they represent
distinct lines in L. The c-line has both factor coefficients nonzero,
which licenses their separate rescalings to x+y. The d-line has a
nonzero x coefficient since it differs from the b-line; its y coefficient
is nonzero since it differs from the a-line. Thus x+t*y is exhaustive
with finite t, t!=0,1. There is no omitted t=infinity case. These facts
hold over E and do not require an F_97-rational line or parameter.

The complete twelve-by-fourteen matrix, three fourteen-coordinate
kernel vectors, zero residuals and all selected minor entries were
inspected. The rank-eleven minor and independent three-vector kernel
give both sides of the dimension squeeze over E. In particular the
third generator (0,e_12) has not been discarded during normalization.
The independently reconstructed fourth-row images give exactly
alpha*(t-26)*U+beta*(t-26)*V+gamma*t*W_0. Their minor 50 is nonzero,
so t!=0 forces gamma=0; nonzero (x,y) then forces (alpha,beta)!=0
and t=26. Neither alpha nor beta is inverted. L162 supplies the converse,
uniqueness and exact ranks at every projective parameter, including
[1:0] and [0:1]. This establishes exhaustion of field-valued planes;
it makes no scheme or descent assertion.

Only after this equality is established is L163's complete 112-label
test transferred to the full locus. Its audited all-parameter mask and
rank-zero exclusion are imported, not inferred from base-field samples.
All forty support records were inspected against the canonical mask.
They contain 27; precisely fixed row 477 also contains 27. The integer
capacity b_27=3 and weight w_27=1 therefore bound every nonnegative real
packing by three, including unrestricted fractional multiplicities.
No upper bounds on individual multiplicities or pair-conflict constraints
enter the dual. The empty masks cause no exception. The strict threshold
is eight additions, and the resulting total-row upper bound is seven.

The verifier logic was reviewed in full and replayed once. Its alternate
polynomial/normalized-map construction checks all nonzero denominators;
its rational elimination independently verifies all five integer
determinants. All 157 checks pass with zero failures and determinant
residues (94,9,55,39,50). Source hashes match the recorded inputs. The
producer certificate SHA-256 remains
`8bc0b391673704ae00f60ab0b06a7e7d184331c5b70d831fea2855630d93b29d`;
the complete verification certificate remains
`7c201d57bd4fec2bc4f7798e2f3e7ccd14ca6901694513ecd53e41ab871de1e1`.
No input audit was rerun and no producer, verifier, map or claim was
changed to obtain the pass. No mathematical input changed, and
L159–L161 are not used. All scope
limits stated above remain, and this audit provides no source-level
novelty claim or complete MCA candidate.

## Mathlib

Full matching locus/capacity result: not checked. Supporting
finite-field, matrix-rank, rank-nullity and finite LP weak-duality
coverage: not checked anew. No theorem name or formal proof is claimed;
unknown coverage is not evidence of absence. Precise standard inputs
and their specialization are stated above.
