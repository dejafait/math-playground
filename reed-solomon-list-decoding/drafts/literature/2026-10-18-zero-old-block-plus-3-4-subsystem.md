# Fixed-column zero-old-block subsystem plus mode (3,4) — proposed scope

TARGET: Test whether L090's fixed-column zero-old-block subsystem remains feasible after adding mode (3,4).
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 333 searched mode (3,4), i=31 and changed-subsystem terms in the ready zero-block/residual assessments, history/318,320,322,326,332 and ATTEMPTS/071,075; inspected L084 complete lift, L090 proof/audit, L091 original-row/range formulas and history/324,328,330. Reuse prior primary-source discovery; no completed test of this added-row subsystem was located in these scoped records.
SOURCE_EVIDENCE: Reuse inspected Schrijver (2005) Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64), pp.5–7; Sano version of record 27 February 2026 Section 2 Corollary 2.2, Theorem 2.6 and both singular proof directions, Lemma 2.7; Ye October 2017 Theorem 1.11 p.13 and Section 1.5.1 pp.23–24; Goemans Lecture 3 (19 September 2001) Theorems 1,3 pp.1–2 and October 1994 Simplex Method pp.7–8; MIT 6.854 (2020) Notes 11 standard-form/basic-solution passages and MIT 15.053 Spring 2013 Recitation 3.A–B pp.4–6. Precise links and qualifications below.
COMPARISON: L090 covers the complete equality/sign/43-zero-block subsystem; L091 rejects only its fixed moments at the added row. Known singular-Schur and rational-LP methods cover a later fixed-column single-row test after the complete equality lift; neither known completion theorems nor the capped unreduced full-row run supplies its verdict.
GAP: Essential method coverage is adequate for this exact bounded subsystem. Reconstruct its unchanged old block/range cost, both complete equality lifts and original/raw rows before one bounded Phase I; no feasibility, separator or new finite result is established by this review.
REASON: Approve exactly TARGET for a later RESEARCH / REPRODUCTION calculation, preserving all ancestral qualifications and prior full-row/conic stops; changing the free moments distinguishes a fixed-assignment rejection from a necessary-subsystem obstruction.

The main gap remains arbitrary-center 67/68-agreement safety with bracket
955–957. The proposed intermediate target adds only L091's minimum mode
(3,4) to L090's reviewed necessary subsystem. It is independently
testable without restarting the stopped full-row or conic prescriptions.
All columns, rho, p8, original pairs and seven-column completion remain
fixed. Only the 45 previously free eight/eight moments may change.

Essential proposed inputs are L076,L078,L082,L083,L084,L086,L090,L091,
with L021,L053,L073,L075 for the immutable original model. Retain the
85 original domain rows, 90 kernel equations, full anchor, 500 types/3000
presentations, 36 forced entries, all 28 equalities, 43 zero-block rows
and 45 signs. Preserve foundations/04,09,10,12's ancestral PSD, uniqueness,
whole-kernel and coherent-normalization qualifications. The complete
18-coordinate equality locus and both raw/original lifts are needed;
their use in this changed subsystem must be assessed separately.

Proposed bound for later approval: one equality-reduced rational Phase I,
at most 10000 pivots and 300 seconds, stopping at the first complete pivot
after the time bound. No second run, retuning, scan, extra mode, full-row
restart or cap increase. Preserve the entire input system, trace and
terminal state. A direct original/raw feasible witness would park this
single-mode exclusion test; a checked exact separator would exclude this
necessary subsystem at the fixed columns. A timeout with neither is
inconclusive and stops this prescription. Do not infer a verdict from
solver status alone. No such system or run was constructed in step 332.

Plausible downstream use: determine whether the strongest observed negative
row is compatible with all already retained conditions when the moments
can vary. Feasibility would not settle the 29 other complementary rows;
infeasibility would not exclude other columns or bases. Scalar upper rows,
other anchors/columns/base/pairs, global moments, representing measures,
RS realization and the 955–957 boundary remain unresolved.

The original proposal above was REVIEW_REQUIRED at step 332. The separate
step-333 comparison below approves only the later bounded calculation;
this literature turn performs no mathematical test.

## Separate source comparison — step 333

LITERATURE_REASON: The target adds one nonzero-old-block row to the reviewed zero-old-block subsystem; its fixed-column Schur cost and equality-reduced LP scope require separate comparison. Reuse ready coverage rather than repeat external discovery.
SCOPE: Exactly TARGET at L086 columns and t78=s, changing only the 45 free moments through the complete 18-coordinate equality locus; one fresh exact Phase I, at most 10000 pivots/300 seconds, with no additional row, scan, retuning, second run or full-row/conic restart.

### Primary results and applicability

Reuse the inspected primary statements and essential proof cases recorded in
`drafts/literature/2026-10-18-fixed-column-zero-old-block-subsystem.md`,
`drafts/literature/2026-10-18-zero-old-block-remaining-modes-critical-audit.md`
and foundations/10. No new external retrieval was needed; source versions
and mathematical hypotheses are unchanged. These are source reuse records,
not claims that the articles were freshly downloaded in this turn.

Alexander Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7: finite unequal-layer restrictions and positive binomial
normalization cover ground sets 68,956 and layers 0,5,6,7,8. Keep both
rectangular directions and L078's coherent positive congruence. No
actual-label averaging or suspect complement prefactor (61) is used.

Takashi Sano, *Moore-Penrose inverse, generalized Schur complement and
inertia*, [version of record, 27 February 2026](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2, Theorem 2.6 and Lemma 2.7: a finite Hermitian
block matrix is PSD precisely when its old block is PSD, the whole cross
vector lies in its range, and the Schur remainder is PSD. The inspected
proof includes square-root necessity and triangular-congruence sufficiency;
no invertibility is assumed. Real symmetric blocks with a scalar new
coordinate are covered. At frozen columns the old block and cross vector
are fixed, so the added row uses L091's already assessed scalar remainder
formula. This is applicability of a known criterion, not a new Schur
lemma. The later test must check the entire range and full inverse action;
a nonzero block is not automatically invertible. Unknown ancestral PSD,
uniqueness, whole-kernel and normalization qualifications in foundations/
04,09,10,12 remain conditional imports.

Yinyu Ye, *Conic Linear Programming*, revised October 2017,
[monograph](https://web.stanford.edu/class/msande310/sdpmain.pdf),
Theorem 1.11 printed p.13 (stated without proof there), Section 1.5.1
pp.23–24 and Section 2.3 opening p.42 cover equality alternatives,
elimination and scalar complementarity. L084's separately audited full
identities, specialized at L086 columns as in L090, supply both directions
of the 18-coordinate equality lift. Adding an inequality changes neither
the selected equalities nor that complete parametrization. Verify the
original and raw forward/reverse identities, including augmented first
coordinate one; do not assume a particular solution exhausts the locus.

Michel X. Goemans, *Advanced Algorithms*, Lecture 3, 19 September 2001,
[primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf),
Theorems 1,3 printed pp.1–2, covers finite Farkas alternatives, including
free variables and no strict-feasibility requirement. The inspected
projection proof fixes signs despite OCR defects. MIT 6.854 (2020),
[Notes 11](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
Introduction, Linear Equalities and Basic Feasible Solutions supplies
standard-form conversion, free-variable splitting and rational basic
solutions for rational data. These are LP statements; no rational SDP
feasibility assertion is imported.

For the bounded procedure reuse Goemans, *An Introduction to Linear
Programming*, October 1994,
[notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/908fe54d659623efadda2d033b895caf_notes_lp.pdf),
The Simplex Method pp.7–8, and Nannicini–Nasrabadi, MIT 15.053 Spring 2013,
[Recitation 3 solutions](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/05885823def0372adb5eae09c7f5490d_MIT15_053S13_rec03sol.pdf),
Problem 3.A–B pp.4–6. Worked artificial-sum initialization is no complexity
or termination guarantee. Exact certificates, not solver status, decide
the finite result. No general result needs reproof; the source does not
evaluate this notebook subsystem. Full matching and supporting Mathlib
coverage remains not checked; unknown availability is not absence.

### Duplicates, failures and bounded decision contract

L090's audited pass does not include mode (3,4). L091's audited negative
value fixes all its moments; it does not quantify over other completions.
The targeted history search finds the new proposal in step 332, not a
completed test. ATTEMPTS/071 stops the capped unreduced full-row run with
no verdict; ATTEMPTS/075 stops the complete L090 assignment only. This
single-row equality-reduced system is a smaller, independently testable
prescription. Preserve both stops and the conic stops, without cap increases.

Grone–Johnson–Sa–Wolkowicz (1984), Proposition 2/Theorem 7, as inspected
in foundations/10, permits otherwise free missing entries; it supplies no
verdict for shared union moments, and notebook chordality is unproved.
General affine SDP alternatives are unnecessary here. No inspected source
settles the finite added-row test, and this is not a novelty claim.

For later work retain all essential IDs and frozen contracts in the
proposal above. Read the complete relevant L084/L086/L090/L091 evidence;
check 85 domain rows,90 kernel equations,500 types/3000 presentations,
36 forced entries,28 equalities,43 zero-block rows,45 signs, positive raw
scaling and full anchor. Reconstruct the added original i=31 row from
L091's full beta/forced/anchor/inverse-cost formula, including every old
block entry, cross coordinate and full range residual. Do not use its
negative value at the old witness as its variable bound. Recheck both
complete equality lifts and pull back every retained inequality without
dropping duplicate or zero rows. Save original/raw systems and lifts
before pivoting.

Use L090's deterministic column ordering, signed-free-variable splitting,
oriented slacks, artificial initialization and least-index entering/
minimum-ratio leaving rule with least-index ties, extending only the row
set by mode (3,4). Save full initial/terminal tableaux, transforms, basis
and pivot trace. Stop at zero artificial sum, certified positive optimum,
10000 pivots or the first complete pivot after 300 seconds. No second run.

Continue only with a full exact rational witness satisfying every retained
original/raw row and frozen contract, or an exact separator: nonnegative
multipliers on all selected mode/sign inequalities, free multipliers on
the equalities, cancellation of every one of the 45 original coefficients,
and a strictly contradictory constant, also checked in raw coordinates.
Transport elimination, orientations and positive-scale factors explicitly.
A positive intermediate artificial sum or reduced-only separator is no
verdict. Preserve a timeout without either certificate as inconclusive and
stop this prescription; a mathematical discrepancy halts interpretation.

Feasibility parks only this single-mode exclusion test; infeasibility
excludes only these fixed columns under the retained conditions. The 29
other complementary rows, scalar upper rows, other anchors/columns/base/
pairs, global consistency, representing measures, RS realization and
arbitrary-center 67/68-agreement safety remain unresolved. No calculation,
new lemma, new mathematical script or boundary improvement occurs here.
