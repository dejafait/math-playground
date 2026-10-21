# Prescribed shortened cubic packing — finite avoidance diagnostic

TARGET: Test whether the prescribed shortened cubic graph packing over F_121 gives an above-threshold incidence-avoiding obstruction to a uniform 60-core bound.
CHECKED: 2026-10-07
DECISION: EXPLORE
SEARCH_EVIDENCE: The completed sixty-core review searched polynomial/cubic graph packings, four-block configurations, high-girth designs and exact 8/121 parameters; scoped checks of L027–L031 and ATTEMPTS/019–022 found no completed matching diagnostic. No originality claim follows from these searches.
SOURCE_EVIDENCE: Reuse the theorem-level comparison in 2026-10-07-sixty-core-extremal-transfer.md, including Glock–Joos–Kim–Kühn–Lichev arXiv:2205.05564v1 (https://arxiv.org/pdf/2205.05564v1), Theorems 1.1/1.6 and Section 9; reuse the previously read Alrabiah–Guruswami–Li arXiv:2304.09445v3 (https://arxiv.org/pdf/2304.09445v3), Definition 2.5/Lemma 2.7, printed pp. 7–8, from 2026-10-07-four-support-realizability.md. L001's full root-bound proof, L027's incidence/rounding proof and L030's polynomial-graph avoidance proof were read during the review.
COMPARISON: Standard root counting and signed equality matrices cover the algebraic tools; high-girth sources support avoidance as a mechanism but do not settle the prescribed finite family. L030's quadratic seven-position avoidance cannot be imported for eight-position cubics.
GAP: Check the specified finite family for the entire four-block incidence pattern, and only after avoidance is established compare its exact size with a justified 60-core uniform-cap threshold; neither conclusion has been derived.
REASON: One independently testable finite construction can discriminate a local counting obstruction without reopening the exhausted 61-core system or applying asymptotic existence at 964.
SCOPE: Only the fixed family below, exact incidence witness or complete avoidance certificate, ordinary pair packing, and the necessary 60-core incidence/threshold arithmetic; no search over new evaluation sets or claims about RS-center realization.

## Exact candidate, not an established construction

Use the prospective field presentation K=F_11[u]/(u^2-2); verify
irreducibility and field arithmetic before using it. Let T={0,1,...,7},
viewed in the prime subfield, and define

Omega=(T times K) minus {(0,0),(0,1),(0,2),(0,3)}.

Take the candidate family of graph blocks
B_p={(x,p(x)):x in T}, for deg p<=3 and
p(0) not in {0,1,2,3}. The proposed ground set has 964 points;
its count and the exact family size must be checked in the research step.
Distinctness of blocks and pair intersections at most three require the
root argument with the actual degree bound. No avoidance or size bound
is asserted here.

The forbidden abstract pattern to test consists of four distinct blocks
with every pair intersection of size two, all six intersections mutually
disjoint, and two private points per block. This is stronger avoidance
than actual L031 labeled independence. Points are pairs (x,y): disjoint
pair-only point sets may reuse x on opposite edges with different y.
Do not assume twelve different evaluation coordinates or miss these cases.
Triple intersections and unintended pair equalities must be checked.

The finite signed-matrix tool is reused from the assessed AGL framework
and L031; its application to the auxiliary field, additional inequalities
and coordinate reuse is a verification obligation. A nonzero kernel alone
is not a witness. Do not reprove random-puncturing, generic full-rank,
high-girth existence or hierarchy theorems. Local proof work is needed
only for this candidate's exact incidence evidence and finite comparison,
which the sources inspected do not supply.

## Continue or abandon

First seek one exact four-polynomial witness inside this *shortened*
family. A valid witness immediately abandons the proposed whole-pattern
avoidance construction; it does not assert failure of L031's labeled
bound. Save all coefficients, eight evaluation values, intersections and
private parts, and verify them exactly. A search miss is not avoidance.
If attempting exhaustive exclusion, enumerate every possible coordinate
collision pattern, justify completeness, and certify all relevant kernels
and noncontainments, retaining opposite-edge coordinate coincidences.
Stop at this prescribed family; do not change T or search other fields
within the same attempt.

Only if whole-pattern avoidance is rigorously established, specialize
L027's core-incidence and integer-threshold method to 60-cores. Count
all incidences with selected 68-supports and retain the ambient threshold
65537^28/2^128, integrality and the strict upper endpoint. Compare the
candidate family's exact size to the resulting sufficient uniform cap.
A large pattern-avoiding family could be relabeled into each H minus C;
justify that label-independent transfer rather than assuming it.
No lower bound on actual RS lists would follow, and cross-core consistency,
common-center realization, 67-agreement safety and ABF equivalence remain
unresolved. If the size is too small, abandon this obstruction test.

Essential inputs are L001, C001a, L031, and L027's transfer method;
L030 is a construction comparison, not an input proving cubic avoidance.
Full matching Mathlib coverage for this prescribed result: not checked.
The new ready assessment needs separate supervisor approval next turn;
no mathematics is executed while approving it in the present turn.
