# Cyclic individual-height feasibility — completed scope review

TARGET: Determine whether L045's eighteen-word scalar system remains feasible after retaining L041's individual logarithmic valuation bounds and cyclic tail-dependent shifted endpoint constraints.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Three focused cyclic-height/real-relaxation/exact-word queries plus one bibliographic query; read L041 through (11), L044 (3)–(6), L045 scalar-system statement, Attempt 019, Attempt 021 and history 069; reuse named ready general-input assessments.
SOURCE_EVIDENCE: Reopened Simons–de Weger Lemmas 6/7 with complete proofs pp. 58–59 and Hercher Theorem 16 proof pp. 10–11; inspected Halbeisen–Hungerbühler published Lemmas 1/2 and complete proof cases pp. 228–229; reuse qualified Lemma 12/Corollary 2 coverage.
COMPARISON: Known chaining uses every local minimum; rational affine closure is already covered by Halbeisen–Hungerbühler, but neither that theorem nor L045's height-free witness decides the specified eighteen-word simultaneous system with the retained integer-cycle restrictions.
GAP: Decide feasibility of the exact necessary relaxation specified below; no simultaneous height witness, infeasibility proof or eighteen-word exclusion has been obtained.
REASON: Essential source comparison is complete; approve one separate RESEARCH/REPRODUCTION attempt assembling existing wordwise identities and bounds, without reproof of general cycle or rational-coding theorems.
SCOPE: Exactly r=18, the integer guards and scalar restrictions of L045, real shifted junctions bounded below by 540/11, L041's smallest-junction seed and own-index logarithmic bounds, and its exact shifted endpoint equation at every index including the closing tail; integrality/residue realization of the junctions is relaxed.
LITERATURE_REASON: The new target retains simultaneous individual heights and tail-dependent cyclic constraints omitted from the previously approved scalar system; this turn completed the missing theorem-level comparison for that changed hypothesis set.

This separate literature turn approves the unchanged TARGET for one later
mathematical attempt within the scope below. It derives no new inequality
and tests no tuple. The previous pending proposal is resolved by source
comparison, not by a feasibility result. Existing ready coverage is reused
for unchanged general inputs.

Main gap: universal eventual descent. Proposed intermediate target:
decide feasibility of a necessary cyclic system at eighteen words,
retaining information suppressed by the exhausted scalar comparison.
Plausible downstream use: an infeasibility certificate could strengthen
the restricted cycle exclusion; a rigorously feasible relaxation could
show whether this added information is still insufficient. Neither
outcome supplies entry, unrestricted cycle exclusion or descent.

Essential input IDs: L041 (seed, occurrence partition, scaling, own-index
valuation bounds and shifted endpoint identity), L044 (the comparison
that discarded individual tail sizes), L045 (the exact aggregate system
and its eighteen-word witness). L043's logarithm enclosure may be reused
if certified numerical constants are essential. No sibling input is
proposed. Keep r=18, integer J_i>=2,H_i>=3,a_i>=0 congruent to 2 modulo
18, and positive counts d,K_0,L_0 with K=dK_0,L=dL_0,K_0>225640000.
Actual closed words have positive odd residue-20 junctions; a proposed
real-height relaxation must explicitly retain its necessary lower heights
and cyclic consistency, without silently asserting integer or parity
realizability. The review must delimit exactly which endpoint constraints
are retained and which are relaxed before approving a mathematical test.

Continuation/abandonment test: after scope approval, seek a rigorous
infeasibility argument for the entire specified system or a simultaneous
certified feasible tuple of all its variables. Rejecting only L045's
displayed tuple would not establish infeasibility. A finite parameter
screen or unverified solver output cannot decide the unrestricted system.
If the constraints reduce to the already exhausted aggregate comparison,
or no discriminating bounded test is justified, park this proposal rather
than rename or repeat Attempt 021. Attempt 019's guard-only failure and
history 069's full-minimum-count mismatch remain relevant evidence.

Published computation qualifications, Rhin/Crandall originals and unknown
Mathlib/Lean coverage remain unchanged. Universal entry, unrestricted
counts/cycles, divergence and eventual descent are independent unresolved
assumptions, not established inputs.

## Exact approved necessary relaxation

This is a specification transcribing existing L041/L044/L045 inputs,
not a new lemma or a claim that the system is feasible. Indices are modulo
18; repeated parameters and coincident junction values are allowed.
Keep integer J_i>=2, H_i>=3, a_i>=0 with a_i=2 modulo 18; set
P_i=4J_i+H_i, K=sum_i(3J_i+H_i), L=sum_i(J_i+a_i), N=K+L.
Keep positive integers d,K_0,L_0 with K=dK_0, L=dL_0 and
K_0>225640000. With c=6.125581 and Lambda=N log2-K log3, retain
all of L045's stated scalar restrictions:

\[
K<\frac{15}{4}(2^{18}-1)
  \left(\frac{133}{10}\log N+9+\log18\right),
\]
\[
N<\frac{399}{5}(2^{18}-1)\log N
 +(54+6\log18)(2^{18}-1)+\frac{69\cdot18}{1034},
\quad N<\frac85K+\frac{69\cdot18}{1034},
\]
\[
e^{-c}K^{-133/10}<\Lambda<\frac{23\cdot18}{517}.
\]

Introduce real s_i and h_i=log s_i. Require s_i>=540/11 at every
occurrence, and relabel cyclically so that s_0=min_i s_i. L041 (6)
supplies the retained seed

\[
0<h_0<\frac{133}{10}\log N+8+\log18.
\]

Retain the two own-index valuation bounds immediately before L041 (7),
equivalently as transcribed in L044 (3):

\[
4J_i\log2\le h_i+\log(11/4),\qquad
H_i\log2<h_i+J_i\log(27/16).
\]

For every i define G_i=(27/16)^{J_i}(3/2)^{H_i} and retain the
exact endpoint identity displayed before L041 (8), with the shift in
the next junction explicitly represented:

\[
z_i=G_i s_i-\frac{12}{11}(3/2)^{H_i}-1,
\qquad s_{i+1}=z_i/2^{a_i}+23/11,\qquad s_{18}=s_0.
\]

Thus the final equation uses the same s_0 as the seed, and every a_i
is its own outgoing tail. L044's established
h_{i+1}+1<2(h_i+1) may also be retained at every cyclic index;
it cannot replace these exact endpoint equations in a certificate for
this target. All these inputs were already proved for actual words.
No sharper seed, tail cap, individual reciprocal-mass refinement or
unproved junction-height relation is approved by this assessment.

Here s_i-23/11 is allowed to be real. The lower height records the
necessary n_i>=47 from actual positive odd residue-20 junctions;
it does not impose n_i integrality, oddness or residue membership.
No actual integer parity path, exact integer valuation, primitive orbit
or residue-20 closure is inferred from feasibility. The equations
K=dK_0,L=dL_0 are count constraints, not a realization of a primitive
orbit with those counts. Published integer-cycle bounds are imposed as
necessary conditions for the original problem, not asserted for every
rational or real cycle.

## Primary sources, applicability and known overlap

Reuse `drafts/literature/2026-10-08-multi-postspell-represented-length-bound.md`,
`drafts/literature/2026-10-08-unrelaxed-thirteen-word-estimates.md`,
`drafts/literature/2026-10-09-retained-transfer-word-count-range.md` and
`drafts/literature/2026-10-10-retained-transfer-range-audit.md`.
The same-day public-target check in the range assessment remains adequate:
the exact target is reaching 1 from every positive integer.

John Simons and Benne de Weger, *Theoretical and computational bounds
for m-cycles of the 3n+1-problem*,
[Acta Arithmetica 117 (2005), 51–70](https://www.impan.pl/shop/en/publication/transaction/download/product/82263),
section 1.2 p. 52, uses all local minima and admits nonminimal periods.
Lemma 6 p. 58 chains consecutive minima via x_(i+1)<b^delta x_i^delta,
where delta=log3/log2 and b=(1+1/X_0)/2^(1/delta). Its complete proof
uses the full odd run, a following halving, and the integer height guards.
Lemma 7 pp. 58–59 iterates cyclically, bounds the product using all
odd-run counts and chooses the global minimum. Both full proofs were
reopened, including the terminal Corollary 5 application. Lemma 14 p. 61
is a full-m ceiling, not an eighteen-junction feasibility theorem.
Reuse Lemma 12 p. 61 and Corollary 2 p. 53 with their inspected proofs
and published height, continued-fraction, Rhin and Crandall qualifications.
Their applicability to represented counts is already justified in L041.
None permits m=18 merely because eighteen postspell boundaries are selected.

Christian Hercher, *There are no Collatz m-Cycles with m <= 91*,
[JIS 26 (2023), Article 23.3.5, Theorem 16 and proof, printed pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
controls the positive linear form by the full odd-input reciprocal mass.
The product/mass proof was reopened; L041 supplies the occurrence partition
and primitive scaling. Reuse the recorded June 2026 correction assessment;
Theorem 16 is unchanged. Its full-minimum cutoff does not decide this
system; no amended Theorem 21 or new computational threshold is imported.

Lorenz Halbeisen and Norbert Hungerbühler, *Optimal bounds for the length
of rational Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[published version, Lemmas 1/2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
was inspected after the author-hosted manuscript. Lemma 1 identifies
pseudo-cycles with cycles over Q[(2)], using odd-denominator numerator
parity. Lemma 2 gives the unique fixed point
phi(s)/(2^l-3^k) for a nonempty binary word with k ones, with its full
induction cases inspected. Our words have k>0. Formal affine closure
and its rational coding are therefore covered mathematics; no reproof
or novelty claim is appropriate. These statements do not decide the
extra height and integer-cycle count restrictions above, nor do they
make a rational fixed point an integer cycle. The manuscript's Theorem 4
statement was also inspected as a general minimum/length lead, but its
supporting optimal-bound proof chain was not fully reviewed and is not
an input. No local specialization of these rational results is derived here.

Mathlib: matching coverage of this full feasibility system, the rational
coding result and the general cycle inputs was not checked. This is
unknown availability, not a claim of absence. External Lean declarations
and original computational certificates remain unchecked.

## Search, duplicates and bounded decision

Queries on 2026-10-10: `Collatz cycles simultaneous local minima logarithmic
bounds cyclic recurrence integer feasibility Simons de Weger chaining`;
`Collatz "postspell" cycle "eighteen"`; `Collatz cycle real relaxation
valuation bounds cyclic heights`; and `Halbeisen Hungerbuhler "Optimal
bounds for the length" 1997 1998 publication`. Results included the primary
papers above, unreviewed modern preprints, public ledgers and discussions.
Only the stated primary passages supply this comparison. New threshold
claims, ledgers and other preprints remain unread leads, not inputs.
No matching theorem was established by the focused search; this is not
evidence of novelty. No sibling notebook was read.

Attempt 021 remains stopped: its feasible aggregate certificate omits all
the individual heights and cyclic equations specified here. L044 supplied
the factor-2 transfer but did not test this simultaneous system. The scoped
records inspected contain no completed test of this target. Attempt 019
retains the two-word boundary-guard redundancy after integer closure;
this target does not rerun that audit or infer a new residue obstruction.
History 069's full-minimum-count mismatch and inaccessible Brox proofs
remain parked; neither is essential to this independent necessary-system
test. Essential coverage for the proposed bounded attempt is not blocked.

SPECIALIZE approves one later RESEARCH/REPRODUCTION attempt at exactly
TARGET. Seek either a proof excluding every assignment of the specified
integer parameters and real heights or a complete certified simultaneous
assignment satisfying every restriction, including the closing tail.
Use exact arithmetic and certified real bounds as needed; L043's proved
logarithm enclosures are an optional existing input. Rejecting L045's
particular witness, searching finitely many parameters, or obtaining
uncertified solver output cannot establish infeasibility. A failed bounded
attempt may honestly leave this decision open and must record its obstacle.
If the test discards the cyclic information and returns only Attempt 021's
exhausted comparison, park it. A new constraint or different target needs
separate review; no such extension is approved here.

Completed EXPLORATION, LITERATURE/NOVELTY_UNCHECKED: changed-target coverage
and scope were completed, with no mathematical advance or feasibility
claim. No lemma or mathematical script was written or executed. No
mathematical exploration turn was spent and no counter reset is claimed.
