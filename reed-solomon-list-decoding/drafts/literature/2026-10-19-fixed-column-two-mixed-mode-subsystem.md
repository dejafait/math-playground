# Fixed columns with both mixed-mode constraints — source scope approved

TARGET: Test whether L092's retained subsystem together with mode (2, 5) has a nonnegative moment completion at L086's unchanged columns.
CHECKED: 2026-10-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 341 searched two-mixed/both-mixed/31-and-23 terms in the 19 October assessments, histories/333–340 and ATTEMPTS/071–076; compared L092 original-row/equality-lift proof, L093 original-row/partition proof, ready single-row and complementary/audit assessments, and foundations/09,10,12. Reuse their primary discovery; no completed two-row verdict was located in these scoped records.
SOURCE_EVIDENCE: Reuse inspected Schrijver (2005) Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64), manuscript pp.5–7; Sano version of record 27 February 2026 Section 2 Corollary 2.2, Theorem 2.6 with both singular proof directions, Lemma 2.7; Polak arXiv:1703.05171v1 Section 1.1 (1)–(3), Proposition 1.1 proof p.2, Section 1.2 p.3; Ye October 2017 Theorem 1.11 p.13 and Section 1.5.1 pp.23–24; Goemans and MIT rational-LP/Phase-I sources precisely cited below.
COMPARISON: L092 passes the retained subsystem plus row 31=(3,4); L093 rejects its fixed moments at row 23=(2,5), not every completion. Known singular-Schur, equality-elimination and rational-LP methods cover the two-row necessary subsystem at fixed columns, but supply no finite verdict. Free-entry completion does not preserve shared moments; stopped full-row/conic runs remain inconclusive.
GAP: Essential method coverage is adequate for this exact later calculation. Reconstruct both full old blocks, whole ranges and inverse costs, complete original/raw equality lifts and every retained inequality before one bounded rational Phase I; no feasibility or separator is established by this review.
REASON: Approve exactly TARGET for a later RESEARCH / REPRODUCTION calculation using unchanged known methods. Varying the moments in this smaller subsystem is independently testable and does not restart a stopped full-mode or conic prescription.

Main gap: arbitrary-center safety at 67/68 agreements, bracket 955–957.
The intermediate test can either expose incompatibility of two mixed-mode
restrictions at these columns or give a stronger necessary-subsystem
witness. It supplies no automatic bound over other columns or moments.

Essential inputs: L021, L053, L073, L075, L076, L078, L082, L083, L084, L086,
L090, L091, L092, L093. Freeze rho, p8, original pairs, seven-column RREF and
completion, all L086 columns and t78=s. Preserve the complete 18-coordinate
equality locus, 85 domain rows, 90 weighted/original kernel equations,
500 types/3000 presentations, 36 forced entries, positive raw scaling,
28 selected equalities, 43 zero-old-block modes and 45 signs. Add precisely
both nonzero-old-block rows 31=(3, 4) and 23=(2, 5), retaining the full anchor,
singular whole ranges and exact inverse costs. Only the 45 free moments
may vary. Ancestral PSD, uniqueness, whole-kernel and normalization contracts
remain conditional. Scalar upper rows, other anchors/columns/base/pairs,
global moments, representing measures, RS realization and 955–957 remain open.

Proposed discriminating test after approval: reconstruct both rows in
original/raw coordinates and pull them through L084's complete equality
locus. Permit at most one exact rational Phase I, capped at 300 seconds;
write full trace/certificate and stop at a completed pivot if the cap is
reached. Continue only with a completely verified feasible witness or
exact nonnegative infeasibility separator. A capped run is inconclusive;
no restart, budget increase, full-row solve, conic solve or further row
addition is authorized by this proposal. A witness would park only this
two-row exclusion test; a separator would exclude this fixed-column
subsystem only. Preserve ATTEMPTS/067, 068, 071 and the distinctions in
ATTEMPTS/075, 076. These are proposed review boundaries, not work done here.

## Separate source comparison — step 341

LITERATURE_REASON: The changed target adds mode (2,5) while retaining (3,4); earlier ready assessments cover one row or fixed-assignment rejection, not variation of moments with both rows imposed. Reuse adequate inspected source coverage without fresh browsing.
SCOPE: Exactly TARGET at L086 columns and t78=s; vary only the 45 moments through the complete 18-coordinate equality locus. One fresh exact Phase I, capped at 10000 pivots or 300 seconds, with no extra row, second run, retuning, scan, cap increase or full-row/conic restart.

The proposal above was unapproved in step 340. This separate literature
comparison approves its method and scope only; it constructs no system,
calculates no new bound and asserts no subsystem verdict.

### Primary results, hypotheses and applicability

Reuse the inspected statements and essential proof cases recorded in
`2026-10-18-zero-old-block-plus-3-4-subsystem.md`,
`2026-10-19-l092-complementary-mode-residuals.md` and foundations/04,09,10,12.
These are previously inspected sources, not fresh external retrieval.

Alexander Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7: the inspected tensor change of basis, extension/reset
argument and positive binomial normalization cover finite unequal-layer
restrictions. Ground sets 68,956 and layers 0,5,6,7,8 meet those ranges.
Retain both rectangular directions, positive multiplicities, L078's
coherent positive congruence and full anchor. No suspect complement
prefactor (61) or actual-label averaging is used. This source supplies
no local coefficients or finite feasibility verdict.

Takashi Sano, *Moore-Penrose inverse, generalized Schur complement and
inertia*, [version of record, 27 February 2026](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2 Corollary 2.2, Theorem 2.6 and Lemma 2.7: a finite Hermitian
block is PSD exactly when its old block is PSD, its entire cross vector
lies in that block's range and its Schur remainder is PSD. The inspected
square-root necessity and invertible triangular-congruence sufficiency
include singular old blocks. Finite real symmetric blocks with a scalar
new coordinate are covered. The range is closed in finite dimension.
Both selected rows have fixed old block and cross at the frozen columns;
research must verify their full range solves and inverse costs rather
than assume a nonzero block is invertible. This is the same criterion
already applied in L092/L093, not a new Schur theorem. Albert's original
proof remains an unread historical attribution; Sano supplies the
essential proof cases independently.

Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight Codes*,
IEEE TIT 65 (2019), 28–38, DOI 10.1109/TIT.2018.2854800,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Section 1.1 (1)–(3), Proposition 1.1 and indicator proof p.2, Section
1.2 p.3, covers ordinary union moments at n=1024,d=10,w=68. Retain the
constant-weight qualification and constraint-preserving averaging
condition. It supplies no representing measure, uniqueness or RS list.

Yinyu Ye, *Conic Linear Programming*, revised October 2017,
[monograph](https://web.stanford.edu/class/msande310/sdpmain.pdf),
Theorem 1.11 printed p.13 (stated without proof there), Section 1.5.1
pp.23–24, supplies the assessed equality alternative and elimination
method. L084's complete lift, specialized and checked in L092, is the
local input. Adding an inequality leaves those same equalities intact;
research must still verify both forward and reverse original/raw lift
identities at the frozen columns. One particular solution is insufficient.

Michel X. Goemans, *Advanced Algorithms*, Lecture 3, 19 September 2001,
[primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf),
Theorems 1,3 printed pp.1–2, supplies finite Farkas alternatives, including
free variables and no strict-feasibility premise. The inspected projection
proof resolves the OCR sign defects as recorded in foundations/10.
MIT 6.854 (2020), [Notes 11](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
Introduction, Linear Equalities and Basic Feasible Solutions, covers
free-variable splitting, slacks and rational basic solutions for rational
data. No rational SDP feasibility or strict-separation theorem is imported.
For pivoting reuse Goemans, *An Introduction to Linear Programming*,
October 1994, The Simplex Method pp.7–8,
[notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/908fe54d659623efadda2d033b895caf_notes_lp.pdf),
and Nannicini–Nasrabadi, MIT 15.053 Spring 2013,
[Recitation 3 solutions](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/05885823def0372adb5eae09c7f5490d_MIT15_053S13_rec03sol.pdf),
Problem 3.A–B pp.4–6. Worked artificial initialization gives no bounded
termination guarantee. The certificate, not the solver status, decides.

No general theorem needs reproof. Full matching and supporting Mathlib
coverage is not checked; unknown coverage is not absence. No source-level
novelty follows from the absence of a finite verdict in these sources.

### Duplicates, stops and exact later test

The targeted search located this two-row proposal only in step 340 and
its pending assessment. L092 changes moments to satisfy row (3,4);
L093's negative row (2,5) fixes that complete assignment. Neither
quantifies over the complete equality locus with both rows imposed.
ATTEMPTS/075 and /076 preserve those distinct exclusions/nonexclusions.
ATTEMPTS/071 stops one direct unreduced full-mode Phase I without a
verdict; ATTEMPTS/067 and /068 stop distinct conic prescriptions.
This smaller equality-reduced subsystem is independently testable;
none of those caps is reset or extended by this approval.

The stronger free-entry completion comparison remains unchanged:
Grone–Johnson–Sa–Wolkowicz, *Positive definite completions of partial
Hermitian matrices*, LAA 58 (1984), 109–124, Proposition 2 and Theorem 7,
[author-hosted paper](https://www.math.uwaterloo.ca/~hwolkowi/henry/reports/pdcomplGJSW84.pdf),
assumes otherwise free unspecified entries and uses chordality for its
universal statement. Shared union moments constrain these entries;
chordality and all-clique hypotheses are not established locally.
It gives no shortcut. There is no essential unread source within this
fixed scope; do not reopen the general SDP or source-access routes.

For the later test consume complete relevant input evidence, not previews.
Reconstruct both i=31 and i=23 from L092/L093's full beta formulas,
including every old entry, whole cross vector, principal minors, fresh
range solve, inverse cost, forced term, anchor and positive mode scale.
Retain L091's conditional coherent weighted normalization. Recheck the
complete original/raw equality lifts and every original retained row;
keep overlaps, duplicate and zero pullbacks. Freeze all contracts and
essential IDs listed above. The old L092 moments are a regression control,
not a restriction on the new solution.

Save original/raw systems and complete lifts before pivoting. Reuse
L092's deterministic signed-variable splitting, oriented slacks,
artificial initialization and least-index entering/minimum-ratio leaving
rule with least-index ties. Extend only its row set by i=23. Preserve
full initial/terminal tableaux, transforms, basis and pivot trace. Stop
at zero artificial sum, certified positive optimum, 10000 pivots or the
first complete pivot after 300 seconds. No restart or additional row.

Continue only with a full exact rational witness satisfying every retained
original/raw row and frozen contract, or an exact lifted separator with
nonnegative inequality multipliers, free equality multipliers, cancellation
of all 45 original coefficients and a strictly contradictory constant.
Verify transport through elimination, orientations and positive raw scales.
A reduced-only separator or positive intermediate artificial sum is no
verdict. Save a capped run without either certificate as inconclusive
and stop this prescription; a mathematical discrepancy halts interpretation.

A witness parks only this two-row exclusion test; a separator excludes
only this fixed-column subsystem under its conditional ancestral inputs.
The untested modes, scalar upper rows, other anchors/columns/base/pairs,
global moments, representing measures, RS realization and arbitrary-center
67/68 safety remain unresolved. No mathematical attempt occurs in step 341.
