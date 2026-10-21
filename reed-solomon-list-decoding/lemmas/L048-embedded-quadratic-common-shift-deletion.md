# L048 — Common-shift deletion leaves an above-benchmark quadratic family

## Hypotheses

Use C012a's subgroup H of order 1024 in E=F_65537. Fix any
61-subset C of H and put X=H minus C. Use precisely C047a's five
distinct outside seven-sets B_0,...,B_4, with their displayed E-labels.
Only one common multiplicative shift s in H is permitted per pattern.

Let Omega=(T times F_137) disjoint union four dummy points, where
T={16,64,70,102,112,118,121}. Fix any set bijection sigma:Omega->X.
Let P be the image under sigma of L030's full quadratic graph family
{B_p: p in F_137[Z], deg p<=2}, including the zero polynomial.
The auxiliary field is not a subfield of E.

Call a family admissible here if it is independent in L030's pair graph
G_C and determinant hypergraph J_C, and contains no complete collection
{sB_0,...,sB_4} for any s in H for which their union is disjoint from C.
There are no independent shifts, private completions, other embeddings
of the forbidden five-set pattern, or additional RS conditions in this
definition.

## Conclusion

There is a set R of at most 1024 original members of P such that
P'=P minus R is admissible and

\[
 |P'|\ge137^3-1024=2570329>1532495.
\]

This holds for every C and every sigma. The excess over L027's greatest
sufficient uniform integer cap is at least 1037834 blocks.

Consequently, if alpha_C is the maximum cardinality of families satisfying
exactly these three local restrictions on X, then alpha_C>=2570329 for
every core. Using these exact maxima in L027's core-incidence upper
certificate cannot certify 68-agreement safety, even with nonuniform
local caps. No common-center RS list, cross-core support family, unsafe
radius, useful cap under stronger restrictions or improvement of the
955–957 bracket follows. The deletion loss is not claimed optimal.
This specialization is a REPRODUCTION of assessed finite tools. The
separate critical audit below retains its stated scope and conclusion.

## Proof

**Assessed tools and application obligations.** The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-11-embedded-quadratic-deletion-test.md`.
Import the ordinary packing terminology from R.A. Bailey and A.C.
Burgess, *Generalized packing designs*,
[arXiv:1107.4120v2](https://arxiv.org/pdf/1107.4120v2),
15 November 2011, printed p. 2, Definitions 1.1.1/1.1.3.
L030's distinct seven-sets have intersection at most two, so each
three-subset lies in at most one member. Thus they form a
(v,k,t,lambda)=(963,7,3,1) packing, with 963>=7>=3.
No packing upper bound, existence theorem or uniqueness of partial
completions is needed for the deletion argument.

Use the definition of a transversal in Artem Chernikov,
*Topics in Combinatorics*, updated 28 February 2017,
[Definition 4.1, printed p. 21](https://www.math.ucla.edu/~chernikov/teaching/Combinatorics285N/CombinatoricsNotes.pdf).
Take original family members as vertices and complete present shifted
five-block patterns as hyperedges. We exhibit a transversal directly;
Remark 4.5's maximal-matching inequality is neither needed nor reproved.
The definition does not provide the loss or surviving-size bound.
Those exact application obligations are proved below. L042's different
nine-set/private-completion result is a comparison only, not an input.
No theorem asserting this seven-set specialization was located in the
assessed scope, and no originality claim is made.

**Imported family and exact pattern.** L030 proves that P has exactly
137^3=2571353 distinct members and is independent in both G_C and J_C
for every sigma and every C. This is incidence invariance under a set
bijection, not actual-field rank invariance. C047a specifies five distinct
seven-sets contained in H and excludes precisely the associated five
selected 68-supports at one common center. Its equality conclusion is
valid for every disjoint core and every common shift. Its nonvacuity
statement for some embeddings is not needed: the present sigma may
contain none of the prescribed patterns.

Write U=B_0 union ... union B_4. For each s in H, multiplication by s
is a bijection of H. The shifted blocks are distinct seven-sets and
their union is sU. Define the set of active shifts

\[
 A_C=\{s\in H:sU\cap C=\varnothing\}.
\]

An inactive shift has at least one block outside the vertex set of
seven-subsets of X and cannot yield a complete pattern in P. For each
active shift the designated anchor is the entire specified block sB_0;
there is no undetermined private point or possible completion.

**The transversal, including missing and repeated anchors.** Define

\[
 R=\{sB_0:s\in A_C,\ sB_0\in P\},\qquad P'=P\setminus R.
\]

R is a subset of the original family. It is the image of a subset of
A_C under s->sB_0, so

\[
 |R|\le|A_C|\le|H|=1024.
\]

Different shifts may select the same member; the set definition counts
and deletes it once. A missing anchor selects nothing, and already
prevents a complete pattern at that shift. Selecting an anchor when
some other required block is absent is harmless, since the upper loss
bound covers all such selections. Empty active-shift sets and families
with no complete violation are included.

Suppose that P' contained all five sB_i for an allowed common shift s.
Each belongs to P and is a subset of X, so sU is disjoint from C and
s is active. In particular sB_0 belongs to the original P, hence to R
by its definition. This contradicts sB_0 in P'. Thus every complete
shifted pattern is hit. Viewing the same collection in a different
order does not evade the argument: the required block sB_0 is still
one of its members. If one collection arises from multiple shifts,
the argument applies to each shift separately. No new complete pattern
can be created by deletion, because all its members and their fixed
labels would already belong to P.

Taking a subfamily preserves both old independence conditions: every
pair or triple among surviving members was already a pair or triple
among original members, with the same labels and intersections.
Therefore P' is admissible. No preserved first/second moments, label
symmetry, or auxiliary-field operation is asserted after deletion.

**Strict cardinality and all-core cap comparison.** Since R is a subset
of the finite P,

\[
 |P'|=|P|-|R|\ge2571353-1024=2570329,
 \qquad2570329-1532495=1037834>0.
\]

This proves the approved target uniformly without enumerating embeddings,
patterns or cores. On a finite ground set the maximum alpha_C exists,
and this construction gives alpha_C>=2570329 independently for each C.

For the downstream certificate, import L027's quantities

\[
 T_*={65537^{28}\over2^{128}},\quad M=\lfloor T_*\rfloor,
 \quad N=\binom{1024}{61},\quad D=\binom{68}{61}.
\]

Its greatest sufficient uniform integer cap is 1532495, equivalently

\[
 N\,1532495<D(M+1)\le N\,1532496.
\]

All alpha_C are integers. There are exactly N cores, so

\[
 \sum_C\lfloor\alpha_C\rfloor
 =\sum_C\alpha_C\ge N\,2570329
 >N\,1532496\ge D(M+1).
\]

L027's strict sufficient-certificate test therefore fails with these
exact local maxima. Any valid local upper bounds for this same
admissibility class are at least alpha_C, and flooring them cannot
reduce them below that integer; nonuniform choices cannot fix the test.
Every actual selected-support list obeys the old restrictions and the
C047a exclusions, so these maxima remain legitimate local upper inputs.
Their insufficiency concerns this certificate, not necessity for RS
safety. The independently chosen surviving families need not be
compatible across cores or realizable at one received word. Other
embeddings of the obstruction, stronger restrictions and 67/68 safety
remain unresolved.

The continuation test succeeds: at most 1024 deletions hit every
specified violation and preserve a strictly above-benchmark family.
It parks only the proposed cap mechanism using exactly these extra
common-shift exclusions.

**Separate critical audit (2026-10-11, step 150).** The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-11-embedded-quadratic-deletion-critical-audit.md`.
This audit imports L030's audited size and every-bijection independence,
C047a's audited equality conclusion for its exact five blocks, C012a's
subgroup, and L027's local-support and incidence statements and exact
adjacent-cap inequality. It does not rerun their determinant, inverse
or moment certificates. The primary definitions cited above are enough
for this specialization; no removal theorem or packing bound is used.

First, |Omega|=7*137+4=963=|H minus C|, so the required bijections exist
for every core. Fixing any one of them, L030 gives the full family P
with 137^3 distinct members; no distributional or average-size assertion
is substituted for this fixed-family statement. The five C047a blocks
are distinct seven-sets in H, so multiplication by a common nonzero s
preserves their sizes, distinctness and exact incidences. An inactive
shift has a point of sU in C, hence some block is not even a vertex of
the seven-subset universe. If an active anchor is absent from P, its
pattern cannot occur. Otherwise its entire specified block is selected
in R, whether or not the other four blocks are present. There is at
most one such selection per shift. Repeated selected blocks decrease
the number of deletions; they never require additional completions.

For any purported surviving collection, choose any shift describing it.
Its five blocks belong to P', hence to P, and its union misses C.
Its designated full anchor is therefore selected and cannot survive.
This contradiction covers all orderings, multiple shift descriptions,
and incomplete patterns without assuming uniqueness of the description.
It also covers the empty active set. The actual labels of a surviving
pair or triple have not changed, so subfamily heredity applies to both
G_C and J_C. No new rank invariance or moments after deletion are used.
The exact size checks are

\[
 137^3=2571353,\quad 2571353-1024=2570329,\quad
 2570329-1532495=1037834>0.
\]

The cardinality maxima require a separate logical bridge from L027's
relaxation. For each C the admissible class consists of subfamilies of
the finite set V_C of seven-subsets. It contains the empty family, so
its maximum alpha_C exists and is an integer. L048 does not identify
alpha_C with L027's relaxed beta_C or rely on an equality between them.
The construction proves alpha_C>=2570329 separately for each core;
no compatible choice of witnesses across different cores is required
for this numerical lower bound.

To check that these alpha_C are valid upper inputs for actual lists,
fix one center and any width m>=1. Select one 68-subset S_P of each
tuple's simultaneous agreement set. L027's proof gives distinct selected
supports and an injective local map S_P -> S_P minus C whenever
C is contained in S_P. Its residual family I_C is independent in both
old edge systems. If I_C contained all five sB_i at an active shift,
the five distinct residual sets would come from five distinct tuples
with selected supports C union sB_i. All share the original center,
and C047a forces them equal, a contradiction. Its theorem permits zero
differences, extension-field coefficients, arbitrary width and extra
agreements, so none is an omitted case here. Thus I_C belongs to the
strengthened class and |I_C|<=alpha_C for every core.

Each selected support has exactly D distinct 61-subsets, and there are
N such cores in H, irrespective of whether individual I_C are empty.
Consequently the same incidence count gives

\[
 D|L|=\sum_C|I_C|\le\sum_C\alpha_C,
 \qquad |L|\le\left\lfloor\frac{\sum_C\alpha_C}{D}\right\rfloor.
\]

For any valid real local bounds u_C>=alpha_C, integrality first gives
|I_C|<=floor(u_C); only after summation is division by D floored.
Since alpha_C is itself an integer, floor(u_C)>=alpha_C. In particular,
using exact cardinality maxima already gives the smallest certificate
obtainable from unrestricted upper bounds for this same local class.
With U_alpha=sum_C alpha_C, the imported adjacent-cap inequality yields

\[
 U_\alpha\ge N\,2570329>N\,1532496\ge D(M+1).
\]

Thus floor(U_alpha/D)>=M+1>T_*. Conversely the certificate would meet
T_* exactly if U_alpha<D(M+1), since M=floor(T_*). Equality at the
endpoint would still fail. This verifies both floors and the direction
of the strict comparison, and also rules out rescuing this certificate
by nonuniform real upper bounds on the same class.

No error or scope narrowing was found. The audit makes the cardinality
transfer explicit; it establishes no new extremal value or improvement
of the 955–957 bracket. Packing terminology and the transversal definition are
properly specialized above; L042 is not a mathematical input. This
retains the stop for exactly these exclusions, without an RS list lower
bound, a cross-core realization, or a conclusion about stronger pattern
sets, independently shifted blocks or other obstruction embeddings.
The unchecked Mathlib qualifications below remain unchanged.

## Mathlib

Full matching all-core deletion/cap-obstruction result: **not checked**.
Supporting finite-set image-cardinality, set-difference cardinality and
hereditary independence declarations: **not checked**. Unknown coverage
is not evidence of absence. Primary definitions are imported by the
precise citations above; the direct finite construction verifies their
specialization without reproving a general transversal theorem.
