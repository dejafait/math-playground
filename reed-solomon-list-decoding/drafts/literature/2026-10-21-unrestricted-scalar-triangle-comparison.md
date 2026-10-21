# Unrestricted shared scalar/cardinality coupling — completed source comparison

TARGET: Compare fractional triangle-decomposition results with unrestricted shared-triple scalar/cardinality feasibility at L098's fixed pairs.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched fractional triangle decomposition with weighted graph, edge demands, capacities and weight upper bounds; inspected Delcourt–Postle 1909.00514v2 and 2606.11178v1, Dross 1503.08191v2, and Gruslys–Letzter 2008.05313v1; checked local fixed-cardinality coverage and ATTEMPTS/081–082,088–089.
SOURCE_EVIDENCE: Delcourt–Postle 2020 Theorem 1.4 p.3 and 2026 Conjecture 1.3/Theorem 1.4 p.5 concern unit edge demands; 2026 Lemmas 2.1–2.2 p.7 give the finite Farkas alternative; Gruslys–Letzter Corollary 1.2 p.2 covers weighted demands under a total missing-weight hypothesis, with rational and limiting cases inspected in Section 3 pp.4–5.
COMPARISON: None of these existence statements supplies L105's prescribed triple-dependent scalar intervals; the weighted corollary is a real partial match, but its missing-weight hypothesis has not been tested for L098's demands. No decomposition equivalence or feasibility result is established.
GAP: Test the weighted corollary's exact finite missing-weight prerequisite before any attempted import; even a pass leaves source scalar capacities, repetitions, null pairs and the complete t-s-preserving lift to justify.
REASON: The comparison replaces an unsupported broad theorem application with one finite prerequisite test; it neither excludes unrestricted feasibility nor licenses another numerical run or support enlargement.
SCOPE: Completed theorem comparison only. A separate continuation assessment covers the proposed single missing-weight test; no weighted existence theorem is applied to this notebook here.
LITERATURE_REASON: The startup target had REVIEW_REQUIRED coverage: the new decomposition mechanism had no inspected primary theorem. This turn fills that essential coverage rather than repeating ready source work.

## Step 397: inspected primary results and decision

The main gap remains arbitrary-center safety at 68 or 67 agreements in
the 955–957 bracket. The intermediate target was a precise theorem
comparison for shared-triple feasibility at L098's fixed pairs. Its
downstream use would be a justified coupling certificate, or a finite
obstruction to a specific theorem application. The continuation test
was whether the sources supplied an applicable finite theorem or a
concrete, independently testable remaining hypothesis. The latter was
found; no new mathematical result was derived.

**Unit-demand results.** Delcourt–Postle,
[arXiv:1909.00514v2](https://arxiv.org/pdf/1909.00514v2), 14 September
2020, Section 1.1 p.2 and Theorem 1.4 p.3: a simple graph on h vertices
with minimum degree at least ((7+sqrt(21))/14)h has a nonnegative
triangle weighting summing to one on every edge. The stronger 2026
preprint is recorded separately below; the old bound is not called
current best. No nonuniform edge demands or prescribed triangle
capacities appear in this statement. Its integral-decomposition
corollary has additional divisibility and sufficiently-large hypotheses
and is unused.

Delcourt–Postle, [arXiv:2606.11178v1](https://arxiv.org/pdf/2606.11178v1),
9 June 2026, Conjecture 1.3 and Theorem 1.4 p.5, assert the corresponding
fractional conclusion at minimum degree 3h/4, without an asymptotic
qualification. This is the inspected preprint's claim, not a critical
audit of its 120-page proof. Section 2.1.1, Lemmas 2.1–2.2 p.7, was read
in full: the finite alternative is Ax=b, x>=0 versus A^T z>=0,
b^T z<0; the edge/triangle specialization uses b=1. Section 2.1.2
p.8 identifies this unit-demand dual as the object of discharging.
These statements supply no triangle-specific upper or lower capacities.
Farkas describes a certificate alternative, not a verdict for our data.

Dross, [arXiv:1503.08191v2](https://arxiv.org/pdf/1503.08191v2),
31 March 2015, definitions pp.1–2 and Theorem 5 p.3, was inspected as
a predecessor. This version states 0.913h, whereas search metadata
describes a later 0.9 asymptotic result. No conclusion here relies on
merging those versions or on a search snippet.

**Weighted result.** Gruslys–Letzter,
[arXiv:2008.05313v1](https://arxiv.org/pdf/2008.05313v1), 12 August
2020, Corollary 1.2 p.2: for h>=7 and edge weights phi in [0,1]
on K_h with sum phi>=binomial(h,2)-(h-4), a nonnegative triangle
packing has edge sums exactly phi. Read definitions, Theorem 2.1
and Lemma 2.4 pp.3–4, and Section 3's full rational averaging and
irrational subsequence cases pp.4–5. Theorem 2.1 controls triangle
weights by 1/2 in its stated unweighted near-complete setting; it
does not prescribe our individual capacities. Lemma 2.4 prints
missing weight at most a in its conclusion, while its proof uses m;
do not import that line literally or silently repair it. The separately
stated corollary is the comparison target, and its missing-weight
hypothesis remains untested here. Computer-assisted small base cases
are cited inputs, not independently reproduced in this review.

**Exact local comparison.** L098 fixes
N=floor(65537^28/2^128)+1 and the entire rational pair vector c_i.
Its Boolean universe has H=binomial(1024,68) vertices. L105 gives
the complete scalar interval
max(0,c_i+c_j-1,c_i+c_h-1,c_j+c_h-1)<=y<=min(c_i,c_j,c_h),
with repetitions fixed and forbidden pairs zero. These are capacities
on triple values, distinct from the weighted source's edge demands.
L098 and L106 already account for both repeated third words; they
cannot be replaced by triangles on three distinct vertices without
retaining their contributions. Source equalities preserve t-s; no
distance-only collapse has been proved. Null pairs require no division.

The inspected unit-demand theorems do not directly assert the needed
weighted, capacitated conclusion. The weighted corollary does address
nonuniform edge sums, so declaring all weighted methods inapplicable
would be unjustified. There is no verified normalization meeting its
finite missing-weight hypothesis, and even such a normalization would
not settle the scalar-capacity issue. No failure of that hypothesis
is claimed yet. A finite Farkas reformulation with added capacity rows
would also require a new specialization and would not by itself solve
the feasibility problem. Do not repackage that alternative as progress
on safety.

Local duplicates/failures checked: the fixed-pair feasibility assessment
steps 391/393, the row-capacity assessment, the shared-scalar working
record, L098/L105/L106's relevant proofs and ATTEMPTS/081–082,088–089.
They contain no matching weighted-decomposition application. Search
queries included `fractional triangle decomposition weighted graph edge
demands capacities theorem`, `fractional triangle decomposition upper
bounds weights`, and `fractional triangle edge demands fractional
decomposition capacities`. Random-graph, weighted triangle-factor and
weighted packing/covering search hits were not inspected and are unused;
they do not establish the needed statement or its absence. No novelty
claim follows from the bounded search.

Decision: park a direct import of the unrestricted capacitated conclusion.
Propose exactly the weighted corollary's finite prerequisite test under
`2026-10-21-weighted-triangle-missing-weight-test.md`. Passing would
justify examining capacities and the full source lift, not importing
feasibility; failing would stop this direct global-normalization
application only. No solve, support scan, new equivalence, lemma or
mathematical script was produced. PSD, other pairs, support-code/RS
realization and the boundary remain open. Mathlib coverage of these
decomposition theorems and the capacitated specialization was not checked.

## Original proposal, preserved as historical scope

This is a proposed next literature-only step, not approved coverage and
not a claim that the source system already is a covered decomposition
problem. Do not derive a new equivalence or approve and execute a new
construction during that review. Inspect primary theorem hypotheses and
essential proof cases, with finite parameters and weights retained.

Essential continuation inputs are L021–L023,L098,L105,L106 and
foundations/04,12,13. Use L098's exact N and fixed pairs; L106's new
audit is an obstruction to its support only. The Boolean universe is
the set of 68-subsets, not the 1024 evaluation positions. The two repeated
third words, null pairs, invariant t-s and every original scalar upper
and lower capacity must survive any applicability comparison. Ordinary
unweighted or merely asymptotic existence is not automatically enough.

Main gap: arbitrary-center 68/67 safety in the 955–957 bracket.
Potential downstream use: a justified unrestricted coupling certificate
or a principled obstruction test, addressing shared entries instead of
independent row capacities. Continue only if inspected source hypotheses
yield a concrete finite intermediate target or a precise, independently
testable remaining difference. Otherwise record the mismatch and park
this theorem application; do not infer full infeasibility or novelty
from an unsuccessful search. PSD, other pairs, actual support-code
realization and RS safety remain separate unresolved gaps.

Preserve ATTEMPTS/081–082,088–089, the numerical-run stops and the
translated-pole exploration exhaustion. No support enlargement, solve,
parameter scan, PSD test or new mathematics was performed when writing
this continuation. Its separate approval belongs to the next turn.
