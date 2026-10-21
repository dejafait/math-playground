# Variable-table cyclic-order criterion — source assessment

TARGET: Assess a variable-table sufficient criterion for cyclic-order rigidity under endpoint/domain/J guards, for r>=3, strictly increasing integer J_i>=2, integer H_i>=3 and integer tail allocations b_i>=0 of fixed total B.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Six focused cyclic-affine, prescribed-block, prefix-dominance and constrained-order queries; reused step-266 discovery and inspected ordering comparisons; checked L051/L055/L069/L074, relevant October 12/14/16 assessments and Attempts 026–031 for scope and failures.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), equations (2)–(4), Lemma 2 and printed induction pp. 228–229, Lemma 4 and exchange proof p. 230; reopened Kubo–Makino–Sakamoto (ISAAC 2024) scalar objective and Theorem 1 definitions/cases pp. 44:2–44:3 and Theorem 3 p. 44:4; reused inspected proof-case, rotation-extremum and positive-real DLMF coverage.
COMPARISON: General affine identities apply with variable finite counts, but inspected scalar ordering theorems do not give simultaneous own-input guard rigidity; L074 supplies an audited fixed-table method and benchmark, not a variable-table theorem or numerical constants for new tables.
GAP: Formulate and prove a table-dependent sufficient test by making the minimum bound, tail-2 offset signs and all first-displacement margins explicit; its generalized implication and numerical nonvacuity have not been established in this literature turn.
REASON: Essential source coverage supports one separate bounded specialization of L074's method; import the general affine/analytic machinery and derive only its variable-table applicability and sufficient inequalities, without assuming rigidity or universal sign conditions.
SCOPE: Exactly TARGET and the proposed scope below, with Lambda>0; a sufficient test may reject tables whose explicit tail-2 offset or margin checks fail. No claim of rigidity for every J,H,B, necessary-and-sufficient criterion, signed-offset extension, new-table arithmetic or actual-word exclusion is approved.
LITERATURE_REASON: The saved gate requires comparison of changed word count, pair table and budget; those hypotheses lie outside the ready fixed-table assessment, so this single essential review is justified despite the recent literature balance.

## Proposal retained from step 277

The following proposal records its original pending state. The separate
step-278 comparison below supersedes its REVIEW_REQUIRED and next-turn
literature-only wording. It does not establish the proposed theorem.

This is a proposed direction, not a new theorem, a ready assessment or
an assertion that all tables are rigid. The completed C074b audit does
not depend on it. The next turn must be literature-only. Reuse the
ready affine coverage and inspect recorded ordering leads before fresh
discovery; do not repeat the fixed-table audit or reopen stopped prime
diagnostics. An exact statement from an inspected primary source may
make an import or specialization appropriate. A failed search would
not establish novelty.

## Proposed scope and discriminating test

Fix an integer r>=3, an indexed pair table with
2<=J_0<...<J_(r-1) and H_i>=3 integral, and a nonnegative integer
B. Attach a_i=2+18b_i to row i, where b_i are nonnegative integers
of total B. Permit any permutation pi. Use L051's endpoint formula
and non-strict J guards at each outgoing row's own real input,
s_k>=540/11 and s_r=s_0. Do not impose its H/seed, minimum,
primitive/count-ray or actual-word assumptions. Counts are defined by
K=sum(3J_i+H_i) and N=sum(4J_i+H_i)+2r+18B; retain the explicit
qualification Lambda=N log2-K log3>0 for the proposed product-bound
mechanism. This specifies the object to assess, not an exclusion.

The intermediate target is an explicit sufficient test, depending only
on this pair table and B, that forces every feasible order to be a
cyclic rotation of 0,...,r-1. It should expose the precise minimum-root
bound, comparison-offset sign conditions and all strict rejection
margins required by the first-displacement argument, rather than assume
them from L055's numbers. A possible later benchmark is whether the
test recovers the already audited L074 instance without new hypotheses.
No formula for the generalized margins or proof of such a test is
derived in this proposal.

Essential prospective local inputs are L074's argument, L069's
first-displacement comparison, L051's endpoint/J definitions and L055
only as the known benchmark. C074b records what the fixed-table work
already excludes. These inputs have not been newly audited for the
variable-table scope. Arbitrary H_i may change offset signs; variable
counts change Lambda and the minimum-root bound. These are unresolved
coverage and hypothesis questions, not premises silently inherited
from the fixed table. Both cuts, tail-2 boundary allocations and
occurrencewise pairing must remain explicit. Full Mathlib coverage for
the proposed criterion is unchecked.

Continue only if the source assessment identifies a precise sufficient
test with a plausible nonvacuous benchmark and covers its essential
ingredients, marking any remaining derivation honestly SPECIALIZE or
EXPLORE. Abandon or narrow this proposal if it only renames the full
feasibility question, assumes the desired order, or requires the fixed
table's numerical properties without an independently checkable test.
Actual literal-order integer exclusion would still be a separate gap
for each new table, as would arbitrary cycles, entry, divergence and
universal eventual descent. A rigidity criterion alone settles none of
those gaps and need not pass every table.

## Separate literature comparison — step 278, 2026-10-17

The main gap remains universal eventual descent. The intermediate target
is a portable sufficient rigidity test, not rigidity of every increasing
table. Its downstream use would be to reduce order questions for other
tables to their literal-order analysis. Arithmetic exclusion of that
literal order, arbitrary cycle languages, entry and divergence remain
independent gaps. The present review establishes source readiness only.

### Primary inputs and hypothesis comparison

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[published PDF](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
section 2, equations (2)–(4), Lemma 2, pp. 228–229: for a nonempty
binary word w of length N with K ones, the affine map is
(3^K x+varphi(w))/2^N, with fixed point
varphi(w)/(2^N-3^K). Read its length-one and appended-zero induction;
the printed appended-one case is stated analogous. Import the identity,
not a parity-realization conclusion. Finite integer row exponents give
finite formal words; proposed Lambda>0 ensures a nonzero denominator.
The shifted endpoint specialization remains an obligation using L051's
definitions. No general affine-coding reproof is needed.

Lemma 4, p. 230, requires distinct binary words with equal length and
one count, and domination of every prefix one count; the dominated
word has the greater numerator. Its complete exchange proof was read.
Equal totals and increasing J alone do not provide prefix domination.
Reuse step 266's Lemma 5/Corollary 1 rotation-extremum comparison;
these scalar extrema do not characterize all designated guards.

Kubo–Makino–Sakamoto, *Composition Orderings for Linear Functions and
Matrix Multiplication Orderings*, ISAAC 2024, 44:1–44:14,
DOI 10.4230/LIPIcs.ISAAC.2024.44,
[published PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol322-isaac2024/LIPIcs.ISAAC.2024.44/LIPIcs.ISAAC.2024.44.pdf):
reopened the prescribed-real-input scalar objective, pp. 44:2–44:3,
the vector-angle, collinearity and potential-identity definitions and all
three cases of Theorem 1. Rechecked Theorem 3's local/global minimum
equivalence, p. 44:4, with its adjacent-interval neighborhood as recorded
in step 222. Positive slopes may be contracting. None of these hypotheses
requires cyclic closure or simultaneous bounds on intermediate inputs.
Thus their optimizer characterization is not the desired guard criterion.
Reuse step 222's inspected cases-(i)/(ii) proofs, pp. 44:8–44:9;
case (iii)'s omitted proof and the full-version lead remain unread and
nonessential because no optimizer theorem is imported.

Reuse the precise Kawase–Makino–Seimi arXiv:1601.05480v1 comparison
in [the October 12 assessment](2026-10-12-fixed-allocation-j-guard-order-rigidity.md):
Theorem 1, Definition 7, Lemmas 9/10/14(b), including the recorded
exchange proof cases, concern a fixed-input scalar optimization. Reuse
[step 246](2026-10-16-earlier-recipient-all-order-j-feasibility.md)'s
inspected Fernandez–Ibanez arXiv:2607.24844v1, Theorems 7.3/8.1/8.2
and proof comparison: rotation extrema and actual-periodic-word bounds
do not supply prescribed-block intermediate-guard rigidity. No theorem
from that unaudited supporting theory is imported. These are reused
comparisons, not newly read papers or source blockers.

Reuse [step 254](2026-10-16-arbitrary-tail-literal-early-support.md)
and step 266's positive-real analytic coverage: NIST DLMF
[4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.2.19](https://dlmf.nist.gov/4.2.E19), and
[4.6.4](https://dlmf.nist.gov/4.6.E4). Their identity/series domains
cover the positive arguments in the proposed mechanism. New numerical
enclosures would still need rigorous remainders; existing numeric
constants are eligible only for the original benchmark. No analytic
theorem is reproved here. Full matching Mathlib coverage is unchecked;
supporting logarithm and finite-product facts are not a matching theorem.

Reopened [MathPrize's target](https://mathprize.net/posts/collatz-conjecture/):
the page with change-history date 2021-07-07 still asks that every
positive integer reach 1 under n/2 at even n and 3n+1 at odd n.
This is the precise unchanged target in foundations; prize rules are
not mathematical inputs.

### Local overlap and preserved failures

Read L051's endpoint/J definitions, L055's table/count and Lambda
passages, L069's minimum-product and complete first-displacement argument,
and L074's construction and supplied audit passages. The variable-count
product framework already occurs in L051 (8), but its subsequent bound
uses extra integer-count/ceiling and primitive hypotheses. Those hypotheses
are unavailable here. L069 and L074 instead import one particular
positive Lambda enclosure, minimum bound and finite margin table. Their
numbers cannot be transferred to arbitrary J,H,B. L074's offset comparison
uses its established H>=40 and the negative tail-2 offset; H>=3 alone
is not an assessed substitute for that sign condition.

The finite comparison to generalize is precisely L074 (5), (7)–(10):
a product-based minimum bound, a valid tail-2 upper comparison at actual
lower-domain inputs, literal comparison prefixes and strict rejection at
each first displacement. This identifies the proposed sufficient-test
architecture without asserting its generalized formula or implication.
Reproducing the cited general affine identity would add no relevant input;
the changed table-dependent bounds and their assembly are the intended
mathematical work. No duplicate variable-table theorem was found in the
supplied overview/DAG or the narrowly inspected local results.

Read Attempts 026–031 in full. The two rational witnesses and the real
feasibility stop remain valid. Prime-five/two-prime cancellations stop
those diagnostics; they do not decide own-input guard rigidity. L062's
fixed-order failure is not a general criterion. C074b's audited exclusion
remains exactly the fixed L055 table/budget application. No cross-notebook
input or reopened modular route is used.

### Discovery and bounded mathematical continuation

Queries actually run in this review:

- `Collatz "cyclic" "order" prescribed blocks inequalities affine maps`
- `positive affine composition cyclic order intermediate state constraints ordering`
- `Collatz cycles exponent permutation prefix dominance Halbeisen Hungerbuhler`
- `"Composition Orderings" "constraints" cyclic`
- `"Collatz" "guard" "ordering" affine`
- `"Collatz" "first displacement"`

Results included the primary 1997 paper, previously assessed cycle
literature, scalar-ordering references, unrelated constraint problems and
unverified claims. No inspected matching theorem was found. Search
snippets and claimed resolutions are not inputs; failed discovery does
not establish novelty. No essential source remains inaccessible.

SPECIALIZE covers one later proof attempt on the unchanged exact TARGET.
Use L051's definitions and L074's audited mechanism, L069's detailed
first-displacement coverage and L055 only as a benchmark. First formulate
an explicit test from table/count/budget data. Require a certified positive
Lambda lower bound, an explicit minimum-height upper bound justified
from every cyclic endpoint, directly checkable tail-2 offset signs, and
strict rejection margins for every eligible first displaced position and
larger remaining row. Deriving the variable-table expressions and proving
that these conditions suffice is work for that later research turn.

The first attempt is limited to the negative tail-2 offset mechanism
already used in L074. A sufficient test may fail its sign check for some
allowed H>=3; it need not classify those tables. It must not assume the
desired order, quantify over unknown feasible tuples as its test, or
substitute the full feasibility problem for explicit input inequalities.
Do not discard a positive actual large-tail offset; comparisons must be
justified at actual lower-domain inputs before propagation. Retain both
cyclic cuts and each outgoing row's own input and attached allocation.
No comparison-trajectory domain, minimum location or growth of every
row may be silently imposed.

Continue only if the explicit conditions have a proof and recover the
audited L074 benchmark using its existing complete bounds, or give a
precise mathematical repair with the same assessed ingredients. That
benchmark is evidence the proposed mechanism has a nonvacuous instance,
not verification of an as-yet-unwritten generalized test. Abandon or
narrow the proposed test if a required inequality cannot be justified,
its benchmark fails, or its conditions merely restate feasibility or
assume the order. A failed sufficient test proves neither nonrigidity
nor feasibility. No search over other tables, integer exclusion,
signed-offset alternative or actual-word application is approved here.

Outcome EXPLORATION records a new changed-hypothesis comparison and an
actionable bounded continuation, not mathematical progress beyond the
sources. Literature work spends no mathematical exploration turn. No
lemma, mathematical script, certificate, DAG or argument overview was
changed. A resulting mathematical theorem would require a separate
critical audit; this review certifies none of its conclusions.
