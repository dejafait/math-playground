# L034 — Sixty-core incidence transfer and exact cap benchmark

## Hypotheses

Use C001a's E=F_65537, F=F_(65537^28), order-1024 subgroup H,
k=64, epsilon*=2^(-128), and any integer m>=1. Messages are
m-tuples of polynomials over F with strict row degree less than 64.
Use closed simultaneous column-Hamming balls. Put

\[
 T=65537^{28}/2^{128},\quad M=\lfloor T\rfloor,\quad
 N=\binom{1024}{60},\quad D=\binom{68}{60}=\binom{68}{8}.
\]

For each C in binomial(H,60), define an admissible family I of
8-subsets of H minus C by the following three requirements:

1. Distinct A,B in I satisfy |A intersect B|<=3.
2. For each three distinct members with empty triple intersection and
   all three pair intersections of size three, form the monic cubics
   on U_12=A_1 intersect A_2, U_23=A_2 intersect A_3 and
   U_31=A_3 intersect A_1. Their ascending-coefficient 4-by-3 matrix
   has rank two over E, as in L033.
3. For each four distinct members whose six pair intersections U_ij
   have size two and are mutually disjoint, and with no point in three
   members, use the signed matrix M_C and difference maps D_ij from
   L031 on these actual overlap labels. For every ij,
   rank_E [M_C;D_ij]>rank_E M_C.

The matrix M_C here is L031's 12-by-12 matrix, distinct from the
integer threshold M. In (2) the pair sets are disjoint because their
possible intersections lie in the empty triple intersection. Each block
then has two private points. In (3) each block contains three disjoint
incident pairs, leaving two private points. Private points belong to
no other block, so the core, overlaps and private parts meet all
disjointness hypotheses of the respective criteria. No other incidence
type is excluded. Realizable rank-two triples and quadruples passing all
six tests are retained, including singular M_C.

Let alpha_C be the maximum cardinality of an admissible family at C.
It exists: the ground family is finite, and the empty family is admissible.
Let beta_C be any finite real upper bound on alpha_C. Thus beta_C>=0;
the caps may differ with C and no label symmetry is assumed.

## Conclusion

For every m>=1,

\[
 B_m(956/1024)\le
 \left\lfloor\frac{\sum_{C\in\binom H{60}}\lfloor\beta_C\rfloor}{D}\right\rfloor
 \le\left\lfloor\frac{\sum_C\beta_C}{D}\right\rfloor.       \tag{1}
\]

For U=sum_C floor(beta_C), this integral upper certificate meets
the required threshold T exactly when

\[
 U<D(M+1),\quad\text{equivalently}\quad U\le D(M+1)-1.       \tag{2}
\]

Consequently the greatest sufficient uniform integer cap b for this
certificate is

\[
 b_* =\left\lfloor\frac{D(M+1)-1}{N}\right\rfloor
     =184665717.                                             \tag{3}
\]

It suffices to prove alpha_C<=184665717 at every core, or to prove
beta_C<184665718 at every core before local flooring. A uniform integer
cap 184665718 fails this certificate test; this asserts no unsafety.
For a uniform real cap used without local flooring the exact condition
is u<D(M+1)/N; u<=TD/N is a conservative sufficient closed condition.

The ordinary packing bounds are

\[
 \alpha_C\le
 \left\lfloor\frac{\binom{964}{4}}{\binom84}\right\rfloor
 =510848942,
\]

and, more strongly by the Johnson–Schonheim nested floors,

\[
 \alpha_C\le
 \left\lfloor\frac{964}{8}
  \left\lfloor\frac{963}{7}
   \left\lfloor\frac{962}{6}
    \left\lfloor\frac{961}{5}\right\rfloor
   \right\rfloor
  \right\rfloor
 \right\rfloor=510317259.                                  \tag{4}
\]

Neither bound meets (2) when used uniformly. No sufficient labeled cap,
boundary improvement, large RS list or resolution of the challenge follows.

## Proof

**Assessed specialization and known source.** The preexisting
[SPECIALIZE assessment](../drafts/literature/2026-10-07-sixty-core-incidence-transfer.md)
covers this target. The incidence and rounding method is the existing
method of L027, with core size changed from 61 to 60 and the new labeled
criteria retained. Its theta body is not used. The justification below
checks changed membership hypotheses and specializes the counting;
it makes no claim of a new counting theorem.

Import Bailey and Burgess, *Generalized packing designs*, author
manuscript dated November 14, 2011,
[printed p. 2, Definitions 1.1.1/1.1.3 and Proposition 1.1.4](https://www.math.mun.ca/rbailey00/papers/packings.pdf).
Its one-coordinate packing specialization with v=964, block size 8,
strength 4 and lambda=1 gives (4). All are positive integers with
964>=8>=4. The theorem does not use evaluation labels or impose either
labeled restriction above. Those restrictions are justified by L031
and audited L033, retaining their signed-kernel and extension-field
qualifications. No generic/random-domain theorem is applied to H.

**Membership for an arbitrary center and width.** Fix Y:H -> F^m
and its list L at 956 errors, hence at least 68 simultaneous agreements.
For each P in L select any 68-subset S_P of its agreement columns.
L001's uniqueness from 64 columns gives
|S_P intersect S_Q|<=63 for distinct P,Q: otherwise every row of their
difference vanishes at 64 distinct points and has degree less than 64.
In particular the selected supports are distinct, regardless of extra
agreements.

Fix a 60-core C and put I_C={S_P minus C : C subset S_P, P in L}.
The map from its containing supports to these 8-subsets is injective,
and pair intersections have size at most 63-60=3. Suppose three members
meet the incidence hypotheses in (2) of the local definition. Their
full supports have common intersection exactly C, pair-only overlaps
the stated three disjoint triples, and two private points each. The
corresponding three distinct tuples already share Y on these supports.
L033's necessity, for arbitrary F-valued tuples and allowing extra
agreements, forces the coefficient matrix to have rank two over E.

Similarly four members meeting (3) give full supports exactly of L031's
form: the 60-core, six mutually disjoint pair-only overlaps of size two,
and four disjoint private pairs. L031's tuple necessity forces every
one of its six noncontainment/rank conditions over E. The rank descent
is part of those criteria; no message descent or single row preserving
all distinctions is assumed. Thus I_C is admissible at every C, not
merely at a representative core. Consequently
|I_C|<=alpha_C<=floor(beta_C), including empty local families and lists.

**All-core incidence and endpoint.** Count pairs (P,C) with P in L
and C subset S_P of size 60. Each selected support contributes exactly
D incidences, and the number at C is |I_C| by injectivity. Therefore

\[
 D|L|=\sum_C |I_C|\le\sum_C\lfloor\beta_C\rfloor\le\sum_C\beta_C.
\]

Divide by positive D, floor because |L| is integral, and maximize over
centers to obtain (1). Caps depend on C and the labels, but not Y or m.
For any real U, floor(U/D)<=T is equivalent to floor(U/D)<=M,
equivalently U<D(M+1). For integral U this is U<=D(M+1)-1.
In particular U=D(M+1)-1 passes with global floor M, whereas
U=D(M+1) fails with global floor M+1. This distinguishes safe equality
at the integer cutoff from the strict real upper endpoint.

For integral uniform b, set U=Nb. Integer division now proves (3) and
its adjacent-cap failure. With no local flooring use U=Nu instead;
this proves the two stated real-cap tests. These are exact tests for
the displayed upper certificate, not necessary conditions for actual
RS safety. Better nonuniform caps may satisfy (2) even when an
individual cap exceeds b_*.

**Ordinary benchmark and exact checks.** Pair intersections at most
three mean any 4-subset belongs to at most one block. Ordinary incidence
counting yields alpha_C*binomial(8,4)<=binomial(964,4), with
binomial(964,4)=35759426001 and binomial(8,4)=70. This is the trivial
packing count underlying the imported theorem; no labeled cap is
deduced. The nested floors in (4), from inside outward, are
192,30784,4234998,510317259.

The exact parameters are

\[
 D=7392009768,
\]

```text
N=85538260622691544366300206482357959036108153318449882567828168879252654969668898433238031004135680
M=2136899816051353757057904852229805411030924365970844208573659527927004771612162841121670742371611
```

Inserting them in (3) gives b_*=184665717 and verifies

\[
 \lfloor Nb_*/D\rfloor\le M<\lfloor N(b_*+1)/D\rfloor.
\]

The nested ordinary cap has floor(N*510317259/D)>M. Before flooring,
its global bound divided by T lies strictly between 2.763 and 2.764.
Thus even the stronger ordinary bound cannot certify safety here.
For the unfloored ordinary count, the identities

\[
 N\binom{964}{4}=\binom{1024}{64}\binom{64}{60},\qquad
 D\binom84=\binom{68}{64}\binom{64}{60}
\]

follow by choosing a 64-subset with a marked 60-subset in either order,
in H or in a fixed 68-set. Cancelling gives

\[
 \frac{N}{D}\frac{\binom{964}{4}}{\binom84}
 =\frac{\binom{1024}{64}}{\binom{68}{64}},
\]

exactly L001's original support ratio. The local restrictions might
improve that benchmark, but no such improvement is established here.

Run `python3 scripts/finite-support/sixty_core_threshold.py`. It writes
`scripts/finite-support/sixty-core-threshold-results.json`, containing
the integer/rational endpoints, full division remainders, all four
nested-floor stages, global transfers and all 22 check outcomes.
All 22 pass, with no failures. Factorial formulas independently check
N and D; an expanded integer expression checks the nested-floor order;
exact identities check both subset counts and both endpoint equalities.
The complete relevant local_caps, global_transfer, nonuniform_endpoint,
counts and checks fields were inspected. The script verifies arithmetic
only; the membership and transfer proofs above provide applicability.
It neither enumerates admissible families nor computes alpha_C.

The independent gaps remain a sufficient finite labeled cap, cross-core
consistency of possible local witnesses, large-list realization at one
center, 67-agreement safety and the ABF definition comparison. Earlier
61-core and shortened-cubic stops remain valid for their own models.

**Separate critical audit, 2026-10-07.** The preexisting
[audit assessment](../drafts/literature/2026-10-07-sixty-core-transfer-critical-audit.md)
approved the membership, normalization and exact endpoint checks.
All statements above survive without correction. This is independent
verification of the stated specialization, not a new packing theorem or
a bound on the unknown alpha_C.

For clarity, the complete pattern-applicability check is as follows.
For three residual blocks, intersections of any two pair-overlap sets
are contained in the triple intersection, hence empty. The two overlaps
incident to each block account for six of its eight points. A remaining
point cannot belong to another block, since then it would already lie
in their pair intersection. Thus the three private pairs are disjoint
from all overlaps and each other. All residual points lie outside C.
For four residual blocks, the six disjoint pair intersections and absence
of triple membership similarly account for six points of each block;
the remaining two cannot lie in any other block. Every selected pattern
therefore satisfies the full hypotheses of L033 or L031, respectively,
even when its tuples have additional agreements outside the supports.

Tuple necessity remains valid over F for every m>=1: division of each
row difference by the degree-60 core polynomial leaves degree at most
three, including the zero polynomial. For a triple, division by each
overlap cubic gives a coefficient vector in the 4-by-3 kernel; rank
three would annihilate all differences in all rows. Disjoint monic root
cubics give rank at least two. For a quadruple, each row gives a vector
in the signed kernel; for each distinct pair at least one row survives
its difference map. Thus each augmented rank must increase. Minors in
E preserve all these ranks over F. Neither argument selects one common
distinguishing row, assumes descent of messages, or tests arbitrary
unlabeled patterns. The existing shared center supplies compatibility.

The incidence normalization was checked independently: 64 shared
selected columns would identify every row, so the support selection is
injective; removing a fixed core preserves that injectivity. Consequently
the count is exactly D per tuple and |I_C| at every core. Empty families,
unequal real caps and all choices of selected supports are permitted.
The integer certificate is at most T precisely when it is at most M.
For U=sum_C floor(beta_C), this is U<D(M+1), with equality at
U=D(M+1)-1 passing and equality at D(M+1) failing. No averaging or
representative-core assumption enters either floor.

Run `python3 scripts/finite-support/audit_sixty_core_threshold.py`.
Without importing the original generator, it reconstructs binomial
counts by Pascal addition, q by repeated multiplication, the greatest
passing uniform integer cap by binary search using the rational safety
test, and the nested packing bound by recursive shortening. It compares
every saved value in parameters, counts, threshold, local_caps,
nonuniform_endpoint and global_transfer, including rational numerators
and denominators, every nested division and the full remainders.
All 80 value/structure comparisons and all 22 audit checks pass, with no
failures. The complete evidence is
`scripts/finite-support/sixty-core-threshold-audit-results.json`.
The full relevant original fields and the full audit comparisons/checks
were inspected, rather than relying on previews or original pass flags.
The search returns 184665717 and the adjacent failure 184665718; the
ordinary nested cap remains 510317259. These checks validate only the
displayed certificate and its arithmetic. No actual labeled maximum,
cross-core realization or arbitrary-center safety is established.

## Mathlib

Full matching coverage and supporting finite-incidence/nested-floor
theorem names were not checked in Mathlib; no absence is asserted.
The known packing bound is imported by the precise primary citation
above. No formal verification of the labeled transfer is claimed.
