# Twenty-word simultaneous height subsystem — completed source comparison

TARGET: Decide feasibility of L046's simultaneous real-height subsystem at twenty words, retaining integer counts, exact shifted endpoints and cyclic closure.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Three focused twenty-word/cyclic-height/rational-closure queries and one high-cycle follow-up; compared L046 (1)–(4), L041's all-r applicability and Attempts 019/021–023 with the ready eighteen-word and twenty-word assessments; exact queries and limits below.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbühler published Lemmas 1/2 and complete relevant proof passages pp. 228–229; reused inspected Simons–de Weger Lemmas 6/7, Lemma 12/Corollary 2 and Hercher Theorem 16 coverage; read Knight's publisher preview only, without importing its theorem.
COMPARISON: Known binary-word affine closure supplies the fixed point for fixed parameters, but does not guarantee the additional height/count constraints; L046 excludes eighteen occurrences only and L049's scalar survivor supplies no simultaneous assignment at twenty.
GAP: Decide the specified twenty-word subsystem over all admissible integer parameters and real heights; no witness, infeasibility proof, parity/integer realization or twenty-word exclusion is established.
REASON: Essential source/scope comparison is complete for one separate RESEARCH/REPRODUCTION attempt using existing inputs and cited affine coding; do not reprove general cycle theorems or add constraints.
SCOPE: The subsystem in L046 (1)–(4) with exactly twenty indices, log20 in the seed and 1380/1034 in the length conversion; all other hypotheses retained as specified below.
LITERATURE_REASON: Simultaneous own-index heights and every exact cyclic endpoint were absent from the ready scalar approval; this changed constraint set required comparison with rational closure and the previously assessed eighteen-word system.

Main gap: universal eventual descent. Proposed intermediate target: decide
this simultaneous necessary subsystem. An infeasibility result could exclude
actual twenty-word closed concatenations after verifying the applicability
bridge; a feasible relaxation would delimit this stronger test without
implying an integer orbit. Accept only an all-parameter contradiction or a
complete rigorously certified simultaneous witness. If neither is obtained,
record the unresolved constraint rather than reuse L049's scalar survivor.
This review covers that discriminating test for a later mathematical
turn; the supervisor separately approves the newly completed assessment.
No mathematical feasibility attempt is performed here.

Essential input IDs for the later comparison: L041, L046 and L049.
L044 and L048 are scalar-transfer comparators only. Reuse
`2026-10-10-cyclic-individual-height-feasibility.md` for its inspected
source statements where their scope actually matches, and the ready
L049 audit assessment for the unchanged integer-cycle source bridge.
Do not extend the eighteen-word conclusion to twenty without proof.
These local applicability passages were inspected in this review; their
conclusions, not their unresolved comparisons, are reusable inputs.

## Exact assessed subsystem

Indices are modulo twenty. The unknowns J_i>=2,H_i>=3,a_i>=0 are
integers with a_i congruent to 2 modulo 18. Define
P_i=4J_i+H_i, K=sum_i(3J_i+H_i), L=sum_i(J_i+a_i), N=K+L.
Require positive integers d,K_0,L_0 with K=dK_0, L=dL_0 and
K_0>225640000, together with Lambda=N log2-K log3>0 and
N<(8/5)K+1380/1034.

The unknown s_i>=540/11 are real, h_i=log s_i, with
s_0=min_i s_i and s_20=s_0. Require
0<h_0<(133/10)log N+8+log20,
4J_i log2<=h_i+log(11/4), and
H_i log2<h_i+J_i log(27/16) for each index.
For G_i=(27/16)^J_i(3/2)^H_i require all twenty equations
s_(i+1)=2^(-a_i)[G_i s_i-(12/11)(3/2)^H_i-1]+23/11.

These are the retained constraints, not assertions of real-cycle source
theorems. Integer parity, exact valuations and residue membership of
s_i-23/11 are deliberately absent from this relaxation. The application
to actual closed words must still retain exact independent tails,
positive odd residue-20 junctions, repeated periods and coincident
junctions. No global-minimum or least-root hypothesis is available.
Do not silently add the larger eighteen-word assessment's optional
inequalities: this target specifies L046's stated subsystem only.

## Distinction from the completed stop and review limits

Attempt 023 stops a single necessary scalar N inequality with all
individual variables eliminated. Its witness is not a witness for these
constraints. Here the own-index parameters must simultaneously determine
both counts and every shifted endpoint, including closure. This is the
specific materially different retained information to assess, rather than
a larger-count search or another rounding of the stopped scalar bound.
The earlier eighteen-word test found an impossible subsystem without
using closure; it provides no feasibility verdict at twenty words.

No independent claim is made about universal entry, unrestricted counts
or cycles, divergence or eventual descent. Published height/computation,
continued-fraction and Rhin/Crandall qualifications remain; external Lean
and full matching Mathlib coverage are not checked. No mathematics on this
changed target was derived or approved during L049's audit. The present
separate literature turn completes its missing comparison, without
deciding feasibility.

## Primary theorem comparison and applicability

Lorenz Halbeisen and Norbert Hungerbühler, *Optimal bounds for the length
of rational Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[published Lemmas 1/2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
were reopened. For g_0(x)=x/2, g_1(x)=(3x+1)/2, a nonempty binary
word w of length ell with k ones has affine map
(3^k x+phi(w))/2^ell and fixed point phi(w)/(2^ell-3^k).
Lemma 1 identifies pseudo-cycles with cycles in the rationals with odd
denominator, using numerator parity. Its preceding denominator argument
and Lemma 2's base/induction cases, including the stated analogous
last-bit-1 case, were inspected. Here ell=N, k=K>0; the empty-word
degeneracy is irrelevant. The displayed theorem is known affine coding,
not a new result. For prescribed word parameters it is the appropriate
import for testing closure; no independent continuous choice of a closing
height is justified. It does not guarantee the retained logarithmic,
lower-height, tail-congruence or integer-cycle count restrictions. Rational
parity coding does not supply integer junctions or residue-20 realization.
No reproof is needed. The paper's stronger extremal-minimum estimates
remain outside the inspected proof coverage and are not used.

Reuse the full relevant source/proof-case evidence in
`2026-10-10-cyclic-individual-height-feasibility.md`,
`2026-10-08-multi-postspell-represented-length-bound.md`,
`2026-10-09-retained-transfer-word-count-range.md` and
`2026-10-10-twenty-exact-transfer-obstruction-audit.md` in this directory.
Their source passages were read; no fresh retrieval of those general
cycle proofs is claimed. The retained-range assessment's 2026-10-10
inspection of the MathPrize page dated 2021-07-07 covers the unchanged
positive-integer reaching-1 target and shortcut convention.

John Simons and Benne de Weger, *Theoretical and computational bounds
for m-cycles of the 3n+1-problem*,
[Acta Arithmetica 117 (2005), 51–70](https://www.impan.pl/shop/en/publication/transaction/download/product/82263),
section 1.2 p. 52 permits nonminimal periods. Lemma 12 and complete
proof p. 61 give Lambda>exp[-13.3(0.46057+log K)], using Rhin's
Proposition and supporting Lemma 8. Corollary 2 and complete proof
p. 53 give the nontrivial positive integer-cycle odd-count threshold
K_0>225640000. These unchanged source hypotheses are not statements
about arbitrary real or rational cycles. Their role here is to impose
necessary conditions on a relaxation of actual integer closed words.

Christian Hercher, *There are no Collatz m-Cycles with m <= 91*,
[JIS 26 (2023), Article 23.3.5, Theorem 16 and complete proof pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
controls the positive linear form by one third of the full odd-input
reciprocal mass. L041's disjoint word intervals, period scaling and
smallest designated junction supply the already proved all-r bridge.
Read L041's hypotheses, source/scaling, seed, own-index identities,
endpoint and length-conversion passages and L046's subsystem and
applicability/audit passages. L041 explicitly allows r=20: its seed
contains log r and its length conversion contains 69r/1034, exactly
as transcribed above. Its finite own-word identities apply at every
occurrence. Actual junctions are positive odd residue-20 integers at
least 47, so their shifted heights meet the prescribed lower bound.
Positive closure gives a nontrivial primitive orbit and represented
counts K=dK_0, L=dL_0; relabeling to the smallest designated junction
preserves every outgoing exact tail, ties and repeated periods. This
checks existing applicability, without deriving a new feasibility result.

Simons–de Weger Lemmas 6/7 pp. 58–59 chain all consecutive local minima
with integer height guards, and Lemma 14 p. 61 is a full-m ceiling.
Hercher's minimum cutoff also uses the full minimum count. Twenty
designated junctions do not license m=20 or a global-minimum
identification; none of these inspected statements decides this subsystem.
The source's published height x_min>301*2^50, distributed [Ro]
computations, Roosendaal communication, continued-fraction denominators
225644606 and 397573379, and Rhin/Crandall originals remain qualified
imports. Their original certificates and external Lean builds are not
independently checked. The previously inspected June 2026 correction
leaves Hercher Theorem 16 unchanged; amended Theorem 21 is not used.

## Discovery, duplicates and bounded continuation

Queries on 2026-10-10: `Collatz "postspell" "twenty" cycle`;
`Collatz rational cycles cyclic height valuation constraints affine fixed
point Halbeisen Hungerbuhler`; `Collatz cycles simultaneous local minima
real relaxation logarithmic bounds twenty`; and the follow-up
`"Collatz high cycles do not exist" definition high theorem`.
The focused search supplied the primary rational-coding paper and general
cycle papers, public ledgers, forum discussions and unchecked preprints.
No inspected theorem matched the exact simultaneous system; failed search
does not establish novelty. Those nonprimary results are not inputs.

Kevin Knight, *Collatz high cycles do not exist*, Discrete Mathematics
349 (2026), Article 114812, DOI 10.1016/j.disc.2025.114812:
the [publisher preview](https://www.sciencedirect.com/science/article/abs/pii/S0012365X25004200)
describes extremal cycles whose minimum is largest among rational cycles
with fixed length/odd count, and a nonexistence result for integer high
cycles. Its introduction and Definition 4.1/section-5 preview were read;
formulas were incomplete and the full proof was not inspected. It is
not imported. Extremality and integer realization are not assumptions of
our relaxation, so this lead is not essential coverage for the present
fixed-input feasibility attempt. No source blocker is being evaded by
assuming its result. Brox and other previously unread optimal-bound
proofs remain parked; no new threshold or external Lean theorem is used.

The narrowly inspected local records contain no completed twenty-word
simultaneous test. L046's eighteen-word contradiction drops closure;
its conclusion cannot be extended by replacing the occurrence count.
L049 and its separate audit concern a scalar length only. Attempts
021–023 retain their original stops; Attempt 019 retains boundary-guard
redundancy after integer closure. The present test requires simultaneous
parameters, heights and all endpoint equations, including the twentieth
closing equation. Refuting a particular scalar survivor does not exclude
the full system. The eighteen-word assessment's optional quantitative
linear-form and aggregate inequalities are not added to this smaller
subsystem. No sibling notebook or mathematical certificate was loaded.

SPECIALIZE covers one later RESEARCH/REPRODUCTION attempt at the exact
TARGET, after the supervisor's separate assessment approval. Accept an
all-parameter contradiction or a complete certified simultaneous tuple
checking every stated restriction. Imported affine coding can check a
proposed fixed parameter word; existing canonical enclosure methods may
certify strict real inequalities. Finite search, an uncertified solver,
or the survival of L049's scalar length is insufficient. A bounded
attempt may leave feasibility unresolved, but must identify the constraint
blocking its certificate. If the test eliminates the retained cyclic
information and returns only Attempt 023's stopped scalar comparison,
park that attempt. Changes to constraints or word count need new review.

Completed EXPLORATION, LITERATURE/NOVELTY_UNCHECKED: this review supplies
new changed-target source/scope comparison, not a mathematical advance or
a feasibility verdict. No lemma or mathematical script was written or
executed. Mathematical exploration usage remains one consecutive turn;
no counter reset is claimed. Mathlib matching coverage of the subsystem,
rational coding and cycle imports remains unknown, not absent.
