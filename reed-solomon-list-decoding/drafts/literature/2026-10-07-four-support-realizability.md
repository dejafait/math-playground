# Four-support realizability — source comparison

TARGET: Establish and test an exact realizability criterion for four selected 68-agreement supports with a 60-point common core, six disjoint size-two pair-only overlaps and no other shared points on C001a's instance, for every m>=1.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the RS-support and BGM assessments; searched four/common intersection-matrix realizability, exact 60/68 support terms and higher-order MDS terminology; checked relevant local assessments, histories and ATTEMPTS/010,019,021. No completed matching diagnostic was located; this does not establish novelty.
SOURCE_EVIDENCE: Alrabiah–Guruswami–Li, arXiv:2304.09445v3 (https://arxiv.org/pdf/2304.09445v3), Definition 2.5 and Lemma 2.7 with complete proof, printed pp. 7–8; Shangguan–Tamo, arXiv:1911.01502v1 (https://arxiv.org/pdf/1911.01502v1), Section 5 opening, Definition 5.2, Example 5.3 and Lemma 5.4, printed pp. 12–15, plus common-root division in Lemma 4.3, pp. 11–12.
COMPARISON: The signed reduced intersection matrix covers arbitrary finite fields and scalar necessary rank deficiency; the displayed unsigned four-way cycle matrix assumes characteristic two. Neither inspected input supplies the exact fixed-subgroup converse with four pairwise distinct tuples.
GAP: Specialize the signed matrix, justify common-core removal, distinguish mere kernel nontriviality from four-message realizability, and certify actual subgroup examples with full finite-field evidence.
REASON: Additional RS agreement constraints address a different gap from exhausted 61-core independent-set refinements and the administratively parked global pair slice; no new rank criterion is derived in this literature turn.
SCOPE: Exactly four supports on C001a's fixed subgroup, the common-core/pair-only pattern specified below, selected agreements permitting extra roots, arbitrary ambient-field messages and every tuple width; one exact criterion and at most two fixed subgroup configurations.

## Main gap and proposed test

Arbitrary-center safety at 68/67 agreements remains open, with
955<=t_star(m)<=957. Use C001a's E=F_65537, F=F_(65537^28),
H of order 1024, k=64 and threshold 65537^28/2^128. Realizability
asks for one received array and four pairwise distinct m-tuples of
strict-degree-less-than-64 messages agreeing on their respective
selected supports. Extra agreements are permitted; arbitrary messages
and centers may lie in F rather than E.

Specify a core C of size 60, pair-only sets U_ij of size two for
1<=i<j<=4, and private sets W_i of size two. All these sets are
mutually disjoint subsets of H. Set
S_i=C union W_i union (union of U_ij incident to i).
There are no additional shared points. These are input hypotheses,
not an asserted realizable construction.

The proposed finite diagnostics assign the six pairs, in order
12,13,14,23,24,34, from either consecutive powers
{h^(2r),h^(2r+1)} or antipodal powers {h^r,-h^r}, for r=0,...,5.
Reuse L020's certified generator h=3^64 modulo 65537, verifying its
order and distinctness in any new certificate. Choose C and the W_i
deterministically from remaining domain points. Do not infer either
rank or realizability from the triple examples.

Import the signed matrix framework; do not reprove generic full-rank
theorems. The prospective proof must handle the common-root factor,
degree cutoff, extension-field rank and six pairwise-distinctness
requirements. A nonzero kernel vector can identify two messages;
scalar projection can identify two tuples. Whether a scalar witness
suffices at all widths is an obligation, not an assumption. Conversely
construct a center compatible on every overlap. Save full matrices,
points, finite-field elimination, kernels and any messages/center in
a research-turn certificate. Verify all equalities and degree and
distinctness conditions exactly. Neither numerical determinants,
sampled universality nor nonzero vectors alone certify realizability.

## Primary source coverage

Alrabiah, Guruswami and Li, *Randomly punctured Reed–Solomon codes
achieve list-decoding capacity over linear-sized fields*,
[v3](https://arxiv.org/pdf/2304.09445v3), header 26 July 2023:
Definition 2.5 uses signed Vandermonde blocks for any prime power.
Lemma 2.7's full proof uses differences from the last message to
give a nonzero specialized kernel. These are the imported inputs.
Theorem 2.9 assumes weak partition connectivity and gives symbolic
rank over a rational-function field. Lemma 3.1 concerns random
distinct evaluations. Neither proves rank at this fixed subgroup;
neither is essential to the proposed test. Earlier ECCC numbering
is not used for these v3 citations. The ECCC download returned an
internal error; arXiv was readable, so no essential blocker remains.

Shangguan and Tamo, *Combinatorial list-decoding of Reed-Solomon
codes beyond the Johnson radius*,
[v1](https://arxiv.org/pdf/1911.01502v1), header 4 November 2019:
Section 5 explicitly assumes characteristic two. Definition 5.2,
Example 5.3 and Lemma 5.4 use its unsigned cycle matrix.
They cannot be imported unchanged into characteristic 65537.
Lemma 4.3's common-root division is the existing L020 input.
The signed framework above avoids that applicability failure.

Reuse the prior BGM v4 comparison in
[the earlier assessment](2026-09-26-current-target.md), “New primary
readings,” solely for its generic/random-domain qualification.
Its unchanged scope needs no new retrieval. Generalized GM-MDS and
the merged later AGL journal version remain unread search leads.
Only primary passages named above were inspected for this comparison.

## Mechanisms, duplicates and failures

| Mechanism | Comparison and decision |
| --- | --- |
| Higher moments for the same 61-core edge system | L030 realizes all orders on large actual independent families. ATTEMPTS/019–021 stop this mechanism as a threshold certificate. Preserve that mathematical obstruction. |
| Prescribed global pair extension | Source coverage exists, but the supervisor requires a different action after repeated process recovery. Park without claiming infeasibility, feasibility or mathematical exhaustion; see ATTEMPTS/022. |
| Four-message compatibility on a 60-core | Select this independent algebraic test. L020 treats three messages on a 61-core; L030's local independence does not assert a common RS center. |

Queries issued included `higher order MDS codes Brakensiek Gopi Makam
Reed Solomon intersections theorem 2023`, `Reed Solomon prescribed
agreement sets common received word four polynomials determinant
higher order MDS`, `"Reed Solomon" "four" "common" "intersection matrix"
realizability`, `"Reed Solomon" "60" "68" agreement supports`, and
`"four" "selected supports" "Reed"`. Exact-number searches yielded
irrelevant hits; no originality claim follows. Narrow local searches
found four-word packing SDP leads but no completed matching RS diagnostic.
L025's finite four-block test is a different packing inequality.

## Downstream use and decision test

A forbidden configuration could supply an additional labeled support
constraint beyond existing local triple edges. A realizable case would
delimit that constraint. Compare only the two prescribed configurations;
no universal nonvanishing claim is licensed. Continue toward a separately
assessed extremal-family problem only if the criterion yields a genuine
restriction with a plausible counting use. If both cases are realizable,
park their exclusion claim. If the criterion or distinctness remains
unresolved, save unfinished reasoning rather than declaring exhaustion.

Essential local inputs are L001, C001a and L020's common-root and
field-rank arguments. L030 is a contrast explaining the old stop, not
a mathematical premise. Quantitative extremal transfer, effect on
L030's families, cross-core moments, full SDP, RS list maxima and ABF
equivalence remain unresolved. Neither four-word witness nor forbidden
pattern settles the threshold.

Mathlib: full matching fixed-support realization and supporting coverage
not checked; unknown availability is not absence. Future specialization
classification: REPRODUCTION. This review adds no lemma or mathematical
script. Newly saved coverage receives separate approval next turn before
mathematical invocation.
