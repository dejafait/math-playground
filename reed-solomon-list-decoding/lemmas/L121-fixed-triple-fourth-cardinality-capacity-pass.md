# L121 — Fixed-triple fourth-order Boolean/cardinality capacity passes

## Hypotheses

Use the universe V of all H=binomial(1024,68) supports, N=floor(65537^28/2^128)+1
and rho=N/H. Use L021's canonical rational vector and the unchanged pairs
c_i of L098/L112: c_0=1, c_1=...=c_4=0 and

    c_i=(N-1)a_i/((U-1)binomial(68,i)binomial(956,i)),
    U=binomial(1024,64)/binomial(68,64), 5<=i<=68.

Let x be any point in L112's original positive rational box, without
refinement, changing scales or choosing another root. For distinct
supports the normalized pair moment is c_|A\B|. The normalized triple
moment b(ABC) is the product of the three corresponding x factors if
all three half-distances are at least five, and zero otherwise. Repeated
variables collapse as in L113/L114. The raw nonempty moments are rho
times these values; raw singleton moments are rho, and the empty moment
is 1. At L112's enclosed root all lower-order exact-N contractions hold.

Fix exactly

    A={0,...,67}, B={0,...,62,68,...,72},
    C={0,...,62,73,...,77}.

The labels are abstract evaluation-position labels for this ordinary
support diagnostic; no labeled RS nonface or coordinate averaging of
an RS condition is imposed. Each fixed pair has half-distance five.

## Conclusion

For every distinct fourth support D, all smaller local distributions
on subsets of {A,B,C,D} are valid and the exact admissible interval for
the normalized fourth moment q_D=m(ABCD)/rho is

    0 <= q_D <= U_D,
    U_D=min(b(ABC),b(ABD),b(ACD),b(BCD)).                 (1)

This includes U_D=0 whenever D has a forbidden distance to A,B or C.
For D=A,B,C the fourth moment instead collapses to rho*z, z=x_5^3>0.
There are simultaneous choices for all these fourth moments, preserving
every specified moment through order three, satisfying the one row

    sum_(D in V) m({A,B,C,D})=N*m({A,B,C}).              (2)

In particular this test passes at L112's enclosed root. It does not
require or prove any other triple-conditioned row. If S(x)=sum_(D
distinct from A,B,C) U_D, the complete original-box calculation proves

    93301984669 < S(x)/((N-3)x_5^3) < 93301984670.        (3)

Thus this fixed-triple local-distribution/cardinality diagnostic is
parked as an exclusion test. This is a REPRODUCTION and finite
specialization of known Boolean inversion and cardinality methods,
not a new general theorem or progress beyond the inspected sources.
It gives no shared system for other triples, full/excluded PSD,
representing measure, packing, RS realization or boundary improvement.
The 955–957 bracket is unchanged. A separate critical proof audit is
pending; independent exact reconstruction is recorded below.

## Proof

**Imported tools and their applicability.** Import Monique Laurent,
*A Comparison of the Sherali–Adams, Lovász–Schrijver, and Lasserre
Relaxations for 0–1 Programming*, [CWI PNA-R0108, 31 July 2001](https://ir.cwi.nl/pub/4319/04319D.pdf),
Section 3.1 (11)–(12), Lemma 2(ii) and full proof, printed pp.5–6.
The Boolean cone criterion applies to a complete moment vector on any
finite variable set. Here the local variables are the distinct supports
among A,B,C,D, of cardinality at most four. Nonnegative inverted atoms
are equivalent to a probability distribution on those variables. This
finite theorem is imported without reproof. Its general statement and
qualifications are retained in foundations/15. The prior SPECIALIZE
assessment is `drafts/literature/2026-10-24-fixed-triple-fourth-cardinality-capacity.md`.
Eliminating one coordinate and computing its interval for this
prescription are the necessary finite specialization, not a reproof
of the hierarchy or an assertion about general prescribed marginals.

For cardinality import Raghavendra–Tan,
[*Approximating CSPs with Global Cardinality Constraints Using SDP Hierarchies*, arXiv:1110.1064v1](https://arxiv.org/pdf/1110.1064v1),
Section 3, Definitions 3.1,3.3 p.7, local-distribution and conditional-
cardinality displays p.8, and the global-measure qualification p.9.
Use round four, uniform weights on H Boolean variables, cardinality
fraction N/H and the all-ones assignment on the three distinct variables
A,B,C. These are supports, not the 1024 positions or field elements.
Multiplying the conditional display by H*m(ABC) gives (2). At zero
conditioning probability the homogeneous equation is the necessary
indicator equation, with all containing moments zero by nonnegativity;
no division by that probability is required. Here rho*z>0 in fact.
For an actual exact-N family it is also the expectation of the
pointwise identity X_A X_B X_C sum_D X_D=N X_A X_B X_C.
This only specializes the imported necessary condition; consistency
alone is not assumed to imply cardinality. Foundations/12–13 retain
the constant-weight indicator framework and its qualifications.

**All sixteen atoms, with the correct normalization.** Write W={A,B,C,D}
when these are distinct, and b(J)=m(J)/rho for nonempty proper J.
The singleton values b are one. If S is the ones-set of an atom, its
mass is

    sum_(S subset J subset W) (-1)^|J\S| m(J).

Apply the imported inversion and divide this expression by rho>0.
The term for J=empty, when present, is 1/rho, not one. The unknown
term has coefficient (-1)^(4-|S|)*q_D. Consequently the lower
candidates for q_D are

    0;
    b(S+i)+b(S+j)-b(S) for each two-set S, {i,j}=W\S;
    4-sum_(pairs J) b(J)+sum_(triples J) b(J)-1/rho.     (4)

The upper candidates are

    b(J) for the four triples J;
    1-sum_(pairs J containing a) b(J)
      +sum_(triples J containing a) b(J) for each a.    (5)

There are eight lower and eight upper candidates. Their maximum and
minimum give exactly the full extension interval, rather than only
containment constraints. The calculation below verifies throughout
the unchanged box that every lower candidate in (4) is at most zero,
with zero present, and that every singleton candidate in (5) is at
least an upper enclosure of the minimum triple. Hence the interval
is exactly (1), and it is nonempty. All smaller marginal atoms are
also checked, without assuming L114's ordinary source scalar rows
already establish a full raw local distribution.

**Exhaustive finite counting.** Index regions by the three membership
bits of A,B,C, with A the least significant bit. Their sizes for masks
0,...,7 are

    (946,5,5,0,5,0,0,63).

A fourth support is specified up to permutations within these regions
by occupancies (o,a,b,0,c,0,0,r), where 0<=a,b,c<=5, 0<=r<=63,
o=68-r-a-b-c and 0<=o<=946. Its positive integer multiplicity is

    binomial(946,o)binomial(5,a)binomial(5,b)
      binomial(5,c)binomial(63,r).                     (6)

Conversely every 68-subset determines exactly one occupancy and is
counted once by (6). Its three half-distances to A,B,C are
68-r-a,68-r-b,68-r-c. Region-preserving permutations fix A,B,C and
preserve every distance, hence every prescribed pair and triple
moment. This justifies using one scalar calculation per distance
triple. It asserts no symmetry for additional labeled restrictions.
Vandermonde convolution gives total multiplicity H. There is no
ordered-quadruple factorial or division by six in this fixed-triple row.

There are exactly 13,214 occupancies and 5,729 distance types. Of the
occupancies, 12,888 are permitted distinct, 323 are distinct with a
null distance, and three are repetitions. The null multiplicity is
84,519,008,318,260,044; the repeated multiplicity is three; the
permitted multiplicity is H-84,519,008,318,260,047. Each repeated
occupancy has multiplicity one and is exactly D=A,B or C. It has
three distinct variables after Boolean collapse, with top moment
rho*z. Null cases remain in all atom and multiplicity checks.

**Exact interval evidence and independent reconstruction.** The
constructor is `scripts/finite-support/fixed_triple_fourth_capacity.py`;
its full lossless factored certificate is
`scripts/finite-support/fixed-triple-fourth-capacity.json.gz`. It binds
the unchanged canonical pairs, root box, retained audits and lemma
inputs by SHA-256. It reconstructs c from L021's primal vector and
checks the exact objective sum_i g_i*c_i=N, N,H,rho and the original
box. It derives regions from the literal sets, enumerates every
occupancy, and saves every multiplicity and distance-type reference.
For every type it evaluates all smaller atoms by inversion, and for
four distinct variables saves all eight upper enclosures of (4), all
four lower enclosures of the singleton candidates in (5), and the
four full triple intervals. Its 396,970 checks have zero failures.

For positive endpoints l_i,u_i from L112, each permitted triple is
enclosed by [l_i*l_j*l_h,u_i*u_j*u_h], including repeated distances.
Null triples are exactly zero. For sums with signed coefficients the
appropriate opposite endpoints are used. Nonpositive upper bounds
in (4) and redundant lower bounds in (5) prove (1) throughout the
box; no midpoint sign or numerical optimizer supplies a verdict.
For each D write U_D^- for the minimum of its four triple lower
endpoints and U_D^+ for the minimum of their upper endpoints. Then

    S^- = sum_distinct multiplicity*U_D^- <= S(x)
        <= sum_distinct multiplicity*U_D^+ = S^+,
    R^-=(N-3)l_5^3 <= (N-3)x_5^3 <= (N-3)u_5^3=R^+.

The independent script
`scripts/finite-support/verify_fixed_triple_fourth_capacity.py` imports
no constructor routines. It computes smaller atoms from their explicit
one-, two- and three-variable formulas. It separately reconstructs
every candidate in (4)–(5), every saved endpoint and all null/repeated
cases. It generates occupancies by fixing the outside and core counts
and solving for the third private count, instead of the constructor's
private-first enumeration. It builds actual representative D sets,
checks their size and distances, computes multiplicities by factorials,
compares every saved row, and independently convolves all eight region
polynomials to obtain H. All 117,635 checks pass with no failures.
The complete relevant summary, including the full exact capacity and
required-value fractions, was inspected in
`scripts/finite-support/fixed-triple-fourth-capacity-verification.json`.
It verifies exactly

    93301984669 < S^-/R^+ <= S^+/R^- < 93301984670,

with R^->0. This gives (3). The smallest smaller-atom enclosure is
zero, with no negative cases. An outer upper estimate alone would
not establish a pass: here S^- is a lower bound on the actual upper
capacity, so [0,S^-] is contained in the attainable sum interval.

Reproduce from this notebook:

    python3 scripts/finite-support/fixed_triple_fourth_capacity.py
    python3 scripts/finite-support/verify_fixed_triple_fourth_capacity.py

**Attainment of the one row and limitations.** Fix x in the box and
let lambda=(N-3)z/S(x). Equation (3) gives 0<lambda<1. Set
q_D=lambda*U_D for every distinct D. Each q_D is in its exact local
interval; setting it to zero on null cases is automatic. For repetitions
use q_D=z. Their total is 3z+lambda*S(x)=Nz, which, after multiplying
by rho, proves (2). Every local vector has nonnegative atoms and total
mass one by the imported inversion theorem. Its marginals match the
shared prescribed lower moments. Each distinct D contributes a unique
four-set containing ABC, so no fourth moment is assigned conflicting
values within this diagnostic. At the enclosed root L112–L114 also
supply the inherited exact-N and ordinary scalar conditions.

This construction covers only four-sets containing this fixed triple
and only its all-ones conditioned cardinality row. Other assignments
on that triple, other triples, shared fourth moments outside this
collection, full PSD, global root uniqueness and all realization
questions remain unresolved. A very wide capacity pass is not a
representing measure or a code-size bound. No previous spectral stop
or capped prescription is reopened, and no second triple is tested.

## Mathlib

Full matching fixed-triple fourth-order/cardinality result and these
exact certificates: not checked. Supporting finite Boolean inversion,
probability distributions, rational interval arithmetic and subset
counts: not checked. Unknown availability is not evidence of absence;
the precise primary theorems above are the imported inputs.
