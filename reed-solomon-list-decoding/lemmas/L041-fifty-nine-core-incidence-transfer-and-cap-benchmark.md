# L041 — Fifty-nine-core incidence transfer and exact cap benchmark

## Hypotheses

Use C001a's E=F_65537, F=F_(65537^28), order-1024 subgroup
H<=E^*, k=64, epsilon*=2^(-128), and any integer m>=1.
Messages are polynomial m-tuples over F with every row of strict
degree less than 64. Use closed simultaneous column-Hamming balls.
Set

\[
 T=65537^{28}/2^{128},\quad M=\lfloor T\rfloor,\quad
 N=\binom{1024}{59},\quad D=\binom{68}{59}=\binom{68}{9}.
\]

Use C040a's generator h=19139 and its ordered edges
12,13,14,15,23,24,25,34,35,45, indexed by r=0,...,9.
For each C subset H of size 59, call a family I of nine-element
subsets of H minus C admissible if both of the following hold:

1. Distinct A,B in I satisfy |A intersect B|<=4.
2. There do not exist five distinct ordered members A_1,...,A_5 in I,
   a common s in H, and singleton sets W_1,...,W_5 such that, putting
   U_ij={s h^(2r),s h^(2r+1)} for edge ij of index r,
   C is disjoint from every U_ij, all W_i are mutually disjoint and
   disjoint from C and every U_ij, and

\[
 A_i=W_i\cup\bigcup_{j\ne i}U_{\min(i,j),\max(i,j)}
 \qquad(1\le i\le5).                                      \tag{A}
\]

The twenty overlap points are distinct by C040a. This definition uses
their actual labels and the full ordered assignment, for every common
shift and every admissible private choice. It excludes no other
five-block incidence pattern. Independent edge shifts and arbitrary
label bijections are not included.

Let alpha_C be the maximum size of an admissible family at C. This
maximum exists because the ground family is finite; the empty family
is admissible. Let beta_C be any finite real upper bound on alpha_C,
so beta_C>=0. These caps can differ with C and need not have any label
symmetry. They are bounds on the defined families, independently of
the center and tuple width; no useful values are assumed.

## Conclusion

For every m>=1,

\[
 B_m(956/1024)\le
 \left\lfloor\frac{\sum_{C\in\binom H{59}}\lfloor\beta_C\rfloor}{D}\right\rfloor
 \le\left\lfloor\frac{\sum_C\beta_C}{D}\right\rfloor.       \tag{1}
\]

For the integral U=sum_C floor(beta_C), the first upper certificate
in (1) meets the threshold T exactly when

\[
 U<D(M+1),\qquad\text{equivalently}\qquad U\le D(M+1)-1.    \tag{2}
\]

The greatest sufficient uniform integer cap for this certificate is

\[
 b_* =\left\lfloor\frac{D(M+1)-1}{N}\right\rfloor
     =19800268651.                                         \tag{3}
\]

Thus alpha_C<=19800268651 at every core would certify safety at
956 errors for every m>=1. Real caps beta_C<19800268652 at every
core also suffice after local flooring. The uniform integer cap
19800268652 fails this certificate; that failure does not imply
unsafety. With a uniform real cap u used without local flooring,
the exact test is u<D(M+1)/N; u<=TD/N is a conservative sufficient
closed condition. Unequal caps may pass (2) even if some exceed b_*.

Ordinary packing supplies only

\[
 \alpha_C\le\left\lfloor\frac{\binom{965}{5}}{\binom95}\right\rfloor
 =54774358874,
\]

and the stronger nested-floor bound

\[
 \alpha_C\le
 \left\lfloor\frac{965}{9}
  \left\lfloor\frac{964}{8}
   \left\lfloor\frac{963}{7}
    \left\lfloor\frac{962}{6}
     \left\lfloor\frac{961}{5}\right\rfloor
    \right\rfloor
   \right\rfloor
  \right\rfloor
 \right\rfloor=54717350548.                                \tag{4}
\]

Neither ordinary cap meets (2) uniformly. No sufficient labeled cap,
boundary improvement, large RS list or complete candidate follows.
The bracket 955<=t_star(m)<=957 remains unchanged.

## Proof

**Assessed tools and scope.** The prior
[SPECIALIZE assessment](../drafts/literature/2026-10-10-fifty-nine-core-incidence-transfer.md)
covers exactly this target. L034 is a comparison for the counting and
rounding method; its eight-set local criteria and numeric cap are not
used as premises here. L001 supplies uniqueness from 64 columns,
C001a fixes the instance and threshold, and audited C040a supplies
equality for the full common-shift configuration. Its proof already
includes arbitrary cores, private singletons, ambient-field tuple rows
and extra agreements, using L040's audited inverse. No matrix or
polynomial theorem is reproved in this step.

Import Bailey–Burgess, *Generalized packing designs*,
[arXiv:1107.4120v2](https://arxiv.org/pdf/1107.4120v2),
15 November 2011, printed p. 2, Definitions 1.1.1/1.1.3 and
Proposition 1.1.4. For positive integers v>=block size>=strength
and lambda, this gives the ordinary packing nested-floor bound,
with the innermost floor taken first. The specialization
(v,block size,strength,lambda)=(965,9,5,1) is justified below
before invoking (4). The proposition supplies neither (A) nor a
sufficient labeled cap. This is REPRODUCTION of assessed counting
and packing tools, with a changed applicability proof and benchmark;
no progress beyond those sources is claimed.

**Actual-list membership at every core.** Fix any center Y:H -> F^m
and its list L of candidates with at least 68 simultaneous agreement
columns. For each P in L choose one 68-subset S_P of those columns.
This is possible for every list member, including those with extra
agreements. If distinct P,Q shared 64 selected columns, every row
of P-Q would have degree less than 64 and vanish at 64 distinct
points, contradicting L001's uniqueness argument. Therefore

\[
 |S_P\cap S_Q|\le63\quad(P\ne Q),                         \tag{5}
\]

and selected supports are distinct.

Fix any 59-core C and set
I_C={S_P minus C : P in L, C subset S_P}. Removing a fixed contained
core is injective on these distinct supports. Each residual member
has size nine and lies in H minus C. For two such members their
intersection has size |S_P intersect S_Q|-59<=4, proving condition 1.

Suppose condition 2 failed. The five distinct ordered members in
(A) correspond by injectivity to five distinct tuples P_1,...,P_5.
Their full selected supports are exactly C union A_i. All twenty
overlap points are distinct and outside C; every W_i is outside
the core and overlaps and has a single owner. Each support has
59+8+1=68 points. For i!=j its intersection with the other support
is C union U_ij, because their only common incident edge is ij
and all private and overlap sets are disjoint. Every intersection
of at least three supports is C. Thus these are the complete
supports in C040a, with its prescribed ordered overlaps, common
shift and arbitrary disjoint core/private choices. All five tuples
agree with the same Y on their selected supports. C040a consequently
forces P_1=...=P_5, contradicting their distinctness. This checks
every forbidden ordered configuration, not just one ordering or
one shift. It uses tuple necessity over F in every row; no descent,
scalar projection or arbitrary-label transport is imposed.

It follows that I_C is admissible for every C, including cores with
empty residual families, and
|I_C|<=alpha_C<=floor(beta_C). Empty original lists also satisfy
everything above.

**All-core transfer and exact rounding.** Count pairs (P,C) with
P in L and C a 59-subset of its selected support. Every support
has exactly D such cores, while injectivity gives exactly |I_C|
incidences at C. Hence

\[
 D|L|=\sum_C|I_C|\le\sum_C\lfloor\beta_C\rfloor
                         \le\sum_C\beta_C.                 \tag{6}
\]

Divide by positive D and floor using integrality of |L|. The caps
are independent of Y and m, so maximizing over Y gives (1).
No representative-core argument or equality of caps is used.

For any real U, floor(U/D)<=T is equivalent to floor(U/D)<=M,
equivalently U<D(M+1). With integral U this is (2): the sum
D(M+1)-1 passes with quotient M, whereas D(M+1) fails with
quotient M+1. For a uniform integer cap b, U=Nb; integer division
by N gives (3) and the adjacent failure. Local flooring of a
uniform real cap less than b_*+1 gives at most b_* at every core.
Without local flooring, substitute U=Nu to obtain the stated strict
real endpoint. Since T<M+1, u<=TD/N implies that strict endpoint.
These are exact tests of the displayed upper certificate, not
necessary conditions for actual list safety.

**Packing membership and comparison.** In any admissible family,
condition 1 implies that no five-subset can belong to two blocks.
Its ground set has 1024-59=965 points and blocks have size nine,
so it is an ordinary (965,9,5,1) packing. All parameters satisfy
the positive-integer hypotheses 965>=9>=5. Proposition 1.1.4 now
gives (4); the five inner-to-outer quotients are
192, 30784, 4234998, 510317259, 54717350548.
The elementary count of five-subsets gives the weaker bound,
using binomial(965,5)=6901569218193 and binomial(9,5)=126.
Neither uses the extra exclusion (A).

Before flooring the ordinary transfer exactly equals L001's ratio:

\[
 N\binom{965}{5}=\binom{1024}{64}\binom{64}{59},\qquad
 D\binom95=\binom{68}{64}\binom{64}{59},
\]

by choosing a 64-set with a marked 59-subset in either order.
Cancellation gives

\[
 \frac ND\frac{\binom{965}{5}}{\binom95}
 =\frac{\binom{1024}{64}}{\binom{68}{64}}.                  \tag{7}
\]

Thus a quantitatively useful cap must exploit additional restrictions;
the transfer alone makes no improvement on the main bracket.

**Exact benchmark evidence.** The integer parameters are

```text
N=5318441074986002758526437708747645121416050983530562646704342106482030360808428918128789492485120
D=49280065120
M=2136899816051353757057904852229805411030924365970844208573659527927004771612162841121670742371611
```

The division remainder in (3) is

```text
R=690643728519663209428521692884996071419997745953230376395804103652758070332831858640460979400319
```

It satisfies D(M+1)-1=N*19800268651+R with 0<=R<N.
Consequently N*b_*<D(M+1)<=N*(b_*+1), and direct global
division verifies

\[
 \lfloor N b_*/D\rfloor\le M<\lfloor N(b_*+1)/D\rfloor.
\]

The ordinary nested cap gives floor(N*54717350548/D)>M.
Its unfloored global bound divided by T is strictly in (2.763,2.764).
The certificate also records zero global remainders for both adjacent
uniform caps and both ordinary caps, so that interval applies to the
nested global integer certificate as well.

Run `python3 scripts/finite-support/fifty_nine_core_threshold.py`.
Full integer/rational evidence is saved in
`scripts/finite-support/fifty-nine-core-threshold-results.json`.
All 33 checks pass, with no failures. They include factorial checks
of the binomial counts, both marked-subset identities, exact threshold
division, greatest-cap and adjacent inequalities, both nonuniform
endpoints, every nested floor and every global division/remainder.
The complete counts, threshold, local_caps, nonuniform_endpoint,
global_transfer and checks fields were inspected with the JSON inspector;
no preview is used as verification. Arithmetic checks do not prove
family membership or compute alpha_C: the proof above establishes
membership and the transfer, and alpha_C remains unknown. The separate
critical audit below retains the specialization without correction.

**Limits and continuation test.** The incidence and arithmetic test
succeeds, so the transfer is retained as an input to a possible future
labeled cap. A useful finite cap remains an independent gap, along
with cross-core consistency, large RS realization, 67-agreement safety
and the ABF definition comparison. ATTEMPTS/019–021,023–025 stop
different models and remain intact. A failed uniform upper certificate
proves no unsafe list; no arbitrary-label symmetry or independent edge
shift has been introduced.

**Independent critical audit (2026-10-10, step 118).** The separately
approved [SPECIALIZE audit assessment](../drafts/literature/2026-10-10-fifty-nine-core-transfer-critical-audit.md)
covers this exact scope. The full L001 uniqueness proof, C001a instance,
and C040a statement, proof and recorded critical audit were compared
with every use above. L040's audited inverse is imported through
C040a; this audit does not claim to reverify that finite matrix.

Fix an arbitrary center and tuple width. There are finitely many
messages, so selecting a 68-subset for every candidate entails no
additional existence hypothesis. If two selected supports intersect
in at least 64 points, **every** row of the tuple difference vanishes
at those points. The degree bound forces equality in every row,
including zero rows. Consequently neither support selection nor
removal of a fixed contained core identifies different tuples.
For residual supports at that core, the intersection is the original
intersection minus precisely the 59 core points, so its size is at
most four. This also verifies ordinary packing membership: a repeated
five-subset would contradict this inequality. The imported
Bailey–Burgess Proposition 1.1.4 has positive integer parameters
965>=9>=5 and lambda=1; its ordinary conclusion requires no labels.

For any violation of (A), retain its actual ordering, shift and private
singletons. The ten prescribed edges are mutually disjoint outside
the core, by the order of h and the nonzero common shift. Each vertex
owns four edges and one private point; two vertices share just their
common edge outside the core, and three vertices share none there.
Thus adjoining C gives exactly C040a's five 68-supports, with all
disjointness hypotheses satisfied. The injective correspondence gives
five distinct polynomial tuples agreeing with the same center on
those supports. C040a forces equality of the full tuples, a
contradiction. This reasoning quantifies over every violating ordered
choice; no assumption that shifts act on admissible families is
needed. Extra agreements do not affect these necessary equalities.

For each selected support the cores are all its D distinct 59-subsets.
For each fixed core injectivity identifies its incidences with its
residual family, including the empty case. These are two counts of
the same finite set of pairs, establishing (6) without any core
symmetry. Integrality first gives |I_C|<=floor(beta_C) for each
possibly unequal real cap, then gives the global floor after division
by D>0. The beta_C are uniform in the choice of center and tuple width,
as required before taking their maxima. For a real sum V, the integer
floor(V/D) is <=T iff it is <=M, iff V<D(M+1). For the integral sum U,
the last passing endpoint is therefore D(M+1)-1. Equality at D(M+1)
fails. This verifies both floors, nonuniform caps, the uniform integer
benchmark and the stricter unfloored-real test. None is asserted to be
a necessary condition for actual safety.

Independent arithmetic is reproducible with
`python3 scripts/finite-support/audit_fifty_nine_core_threshold.py`.
It does not import or execute the original generator. Pascal addition
constructs the binomial coefficients; rational product formulas
cross-check them. Each division also satisfies its full Euclidean
interval and remainder identity. The audit reconstructs and compares
**every one of the original certificate's 139 scalar fields**, including
all 33 independently recomputed check meanings, and verifies the exact
schema rather than reading old pass flags. Its complete evidence is
`scripts/finite-support/fifty-nine-core-threshold-audit-results.json`.
There are no failures. The historical check names ending in
`_factorial` are retained for comparison; this audit checks those
identities with Pascal addition and rational products, not the
original factorial routine.

The complete reconstructed counts, threshold quotient and remainder,
local caps, every nested division, four global quotients/remainders,
nonuniform endpoints and checks were inspected. They agree with the
displayed N,D,M,R. The nested quotients are exactly
192,30784,4234998,510317259,54717350548, with remainders
1,0,6,0,3. All four global remainders are zero. Both marked-subset
identities and their rational cancellation pass; integer
cross-multiplication confirms the strict (2.763,2.764) interval.
The adjacent cap fails by an exact negative threshold slack, not
floating-point rounding. These checks retain b_*=19800268651 and
the ordinary nested cap 54717350548. They do not compute alpha_C.

This REPRODUCTION audit establishes a checked local input using the
assessed counting and packing tools, with no substantive correction,
new extremal bound or claim of progress beyond those sources. The
main boundary remains unresolved. The direct mathematical inputs
remain L001, C001a and C040a, so the existing DAG row is unchanged.

## Mathlib

Full matching coverage and supporting finite-incidence/nested-floor
theorem names were **not checked** in Mathlib; no absence is asserted.
The ordinary bound is imported by the precise primary citation above.
The supporting polynomial declarations cited in C040a concern its
algebraic input, not this transfer or a finite cap. This is an informal
specialization with arithmetic evidence, not a formal verification.
