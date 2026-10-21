# One weighted-decomposition prerequisite test

TARGET: Test Gruslys–Letzter Corollary 1.2's normalized missing-weight hypothesis on L098's fixed-pair distinct-triple demands.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed bounded decomposition search and local duplicate/failure comparison in 2026-10-21-unrestricted-scalar-triangle-comparison.md; the selected target checks one explicit hypothesis, not unrestricted feasibility.
SOURCE_EVIDENCE: Gruslys–Letzter, arXiv:2008.05313v1, Corollary 1.2 p.2; definitions pp.1–4 and full Section 3 pp.4–5 inspected. L098 supplies the exact pair vector, orbit multiplicities and contractions; L105/L106 retain repetitions and scalar capacities.
COMPARISON: The source covers weighted edge sums under an explicit finite deficit condition but does not supply the original triple-dependent capacities; evaluating that condition at these fixed demands is the necessary specialization, not a reproof of the theorem.
GAP: Evaluate the normalized missing weight exactly, justify the chosen common normalization, and compare with H-4; the source-to-capacitated-system equivalence and all capacities remain separate unresolved issues.
REASON: This finite prerequisite can reject one direct theorem application without another solve or support scan; a pass would only justify a later capacity/lift investigation.
SCOPE: One exact hypothesis test on the full fixed Boolean universe and one common normalization, with no decomposition construction, new support selection, optimizer, parameter scan, PSD test or feasibility conclusion.

This continuation was written during literature step 397. Its source
coverage is ready for the supervisor's separate approval next turn;
no calculation or theorem application has been executed here.

## Inputs and bounded future attempt

Use L021–L023,L098,L105,L106 and foundations/04,12,13. The canonical
source comparison is
[the completed assessment](2026-10-21-unrestricted-scalar-triangle-comparison.md).
The primary citation is Gruslys–Letzter,
[arXiv:2008.05313v1](https://arxiv.org/pdf/2008.05313v1), Corollary 1.2,
printed p.2. Use that statement, not the qualified wording of Lemma 2.4.
The theorem's proof is imported by citation; no reproof or reproduction
of its computer-assisted base cases is necessary for a hypothesis test.

Freeze N=floor(65537^28/2^128)+1 and precisely L098's c_i, with
g_i=binomial(68,i)binomial(956,i). The graph under comparison has
H=binomial(1024,68) vertices, one for each 68-subset. All unordered
distinct vertex pairs remain in the complete weighted graph, with
zero weights at forbidden half-distances 1,...,4. The candidate
distinct-third-word demand on a permitted pair at half-distance i is
(N-2)c_i: verify its use against the two repeated contributions in
L098/L105 before the test, without claiming an equivalence of systems.
Repeated vertices are not triangles and must not enter a distinct-edge
count; Boolean repetitions remain fixed in the original problem.

Use a single positive common normalization: divide these demands by
their maximum over permitted distinct pairs. Justify that it puts every
edge weight in [0,1], and determine whether any larger common divisor
could improve the missing-weight comparison. Count unordered edges
using the full g_i multiplicities; justify the factor of two and keep
every forbidden pair. Compute the resulting total missing weight
exactly and compare it with the required H-4. Use rational arithmetic
and integer cross-multiplication, not an asymptotic estimate or floating
point preview. A symbolic exact bound is enough if it decides the
inequality rigorously. No enumeration of the H vertices is needed.

Limit this to the 69 fixed pair coordinates and one finite comparison.
If a small certificate is useful, save the full exact inputs,
normalization, edge counts, actual and required deficit, comparison
slack and failures under `scripts/finite-support/weighted-triangle-deficit-*`
only after the research gate permits it; print a short verdict and paths.
Do not load the large old control certificate merely for orientation;
use the small canonical pair data or selected exact values through the
JSON inspector. A load-bearing selected value must be inspected fully.

## Relevance, continuation and abandonment

The main gap is arbitrary-center 68/67 safety. This intermediate test
can decide whether this particular weighted theorem merits further
specialization to shared triples. If the deficit exceeds H-4, park
this direct global common-normalization application; do not conclude
that no decomposition exists or that no other weighted method applies.
If it passes, keep the theorem application conditional: derive no
shared-feasibility verdict until a separately assessed step controls
all source capacities and the complete t-s-preserving lift. If the
candidate demand interpretation cannot be justified from the inputs,
save that precise issue and stop before numerical evaluation.

No source theorem licenses discarding scalar upper/lower rows, setting
null pairs positive, identifying distinct t-s classes, or enlarging
L106's support as a construction. This test does none of those things.
PSD, other pairs, actual support-code realization, common-center RS
realization and the 955–957 bracket remain independent gaps. Preserve
ATTEMPTS/081–082,088–089, all numerical-run stops and the exhausted
translated-pole exploration. Mathlib coverage is not checked; none is
assumed and unknown coverage is not an absence claim.
