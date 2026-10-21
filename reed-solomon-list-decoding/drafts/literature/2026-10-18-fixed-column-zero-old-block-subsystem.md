# Fixed-column zero-old-block subsystem — source scope approved

TARGET: Test the fixed L086 columns for a nonnegative completion of L084's equalities and every zero-old-block mode.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 325 compared L084's complete equality locus, L088's original/raw forward and reverse lift, L089's original mode formulas and zero-block case, ready L088 feasibility and L089 critical-audit assessments, foundations/10, history/318,320,322,324 and ATTEMPTS/071,073; targeted search of ATTEMPTS/067–073 and the fixed-column full-completion/new-only-audit assessments found no completed verdict for this changed row set. Reuse their recorded discovery and stronger-result comparisons; no fresh external retrieval or novelty inference.
SOURCE_EVIDENCE: Reuse inspected Schrijver (2005) Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64), pp.5–7; Sano version of record 27 February 2026 Section 2 Corollary 2.2, Theorem 2.6 including both singular proof directions, Lemma 2.7; Ye October 2017 Theorem 1.11 p.13 and Section 1.5.1 pp.23–24; Goemans Lecture 3 (19 September 2001) Theorems 1,3 pp.1–2; MIT 6.854 (2020) Notes 11 standard-form/basic-solution passages; exact Phase-I references specified below.
COMPARISON: Known finite singular-Schur and rational-LP methods cover this necessary subsystem after complete equality reduction. L088 covers only new-only rows; L089 rejects its fixed moments, not all completions. The capped unreduced full-row run and stopped conic runs give no verdict. Neither unrestricted partial-matrix completion nor general SDP separation supplies this shared-moment verdict.
GAP: Essential source coverage is adequate; the later attempt must reconstruct the entire zero-old-block index set, including empty blocks, verify every cross/range condition, specialize both directions of the 18-variable lift, and check an original/raw witness or lifted separator. No row enumeration or feasibility conclusion is supplied here.
REASON: Approve one later RESEARCH / REPRODUCTION calculation on exactly this equality-reduced necessary subsystem; the unchanged general methods need no reproof and no essential source blocker remains.
LITERATURE_REASON: The saved target adds every zero-old-block mixed row to the previously assessed new-only subsystem; this separate comparison checks that changed selection and its singular-case hypotheses without repeating external discovery.
SCOPE: Exactly TARGET at immutable L086 columns; all 28 selected equalities, all 45 signs and every original mode whose entire old block is zero, including empty blocks. One equality-reduced rational Phase I capped at 10000 pivots or 300 seconds; no second run, parameter scan, retuning or full-row/conic restart.

## Relevance and discrimination

Main gap: arbitrary-center 67/68-agreement safety, with bracket 955–957.
The intermediate target changes the 45 moments at fixed L086 columns,
using L084's complete 18-dimensional equality locus. It can distinguish
L088's poor complete assignment from a fixed-column obstruction already
visible in this necessary subsystem. A verified separator rejects all
completions at these columns; a witness parks only this subsystem.
Neither establishes a uniform bound or changes the RS bracket.

Continue only with a complete original/raw witness or exact lifted
separator, or save an honest bounded inconclusive result. A cap or failed
reconstruction stops this attempt without a rerun or larger budget.
Nonzero-old-block modes, scalar upper rows, other anchors, other plane
points/columns/base/pairs, global consistency and RS realization remain
unresolved in either successful outcome.

## Reused primary results and changed specialization

The ready assessments
[fixed-column new-only feasibility](2026-10-18-fixed-column-new-only-face-feasibility.md)
and [L089 critical audit](2026-10-18-new-only-witness-mixed-mode-critical-audit.md)
record the inspected primary statements, relevant proof cases and source
versions. Their coverage is reused while changing the selected rows;
no new external passage, local coefficient calculation or general lemma
is claimed in this literature-only turn.

Alexander Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7, supplies the real invariant unequal-layer decomposition.
Ground sets 68,956 and restriction to layers 0,5,6,7,8 remain unchanged.
Retain one coherent positive congruence, both rectangular directions,
positive multiplicities and the full anchor. The suspect complement
prefactor (61) remains unused. The theorem does not validate local beta
coefficients or transport actual-label restrictions by averaging.

Takashi Sano, *Moore-Penrose inverse, generalized Schur complement and
inertia*, [version of record, 27 February 2026](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2 Corollary 2.2, Theorem 2.6 and Lemma 2.7, supplies the finite
Hermitian block PSD criterion, including singular old blocks: old PSD,
whole cross-kernel annihilation and nonnegative Schur remainder are all
required. Its inspected square-root necessity and invertible triangular
congruence sufficiency are already assessed in foundations/10. Real
symmetric matrices are a covered specialization. For a selected zero
old block, verify its entire cross vector vanishes; do not replace this
with a zero inverse-cost assertion. An empty old block is the already
assessed new-only scalar case. No new singular-block theorem is needed.
Selection must inspect every entry of the original B_i after anchor
transport, not its determinant, rank deficiency, diagonal alone or a
previous witness's failed modes. No count or list of selected modes is
asserted by this review. L089 provides one tested nonempty zero-block
case, index 66; it is a regression control, not exhaustive coverage.

L084 and L088 supply the complete equality-lift specialization, rather
than requiring a new parametric elimination theorem. Reuse Yinyu Ye,
*Conic Linear Programming*, revised October 2017,
[monograph](https://web.stanford.edu/class/msande310/sdpmain.pdf),
Theorem 1.11 printed p.13 (stated without proof there), Section 1.5.1
pp.23–24 and scalar complementarity Section 2.3 opening p.42.
The selected equalities remain necessary by L082/L083, independently
of which remaining inequalities are retained. The later calculation
must check both forward and reverse scaled/raw lift identities at the
fixed rational columns, not infer completeness from one feasible lift.

Michel X. Goemans, *Advanced Algorithms*, Lecture 3, 19 September 2001,
[primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf),
Theorems 1,3 printed pp.1–2, gives the finite free-variable Farkas
alternative; foundations/10 records the inspected projection proof and
sign qualifications. MIT 6.854 (2020),
[Notes 11](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
Introduction, Linear Equalities and Basic Feasible Solutions, covers
free-variable splitting, slacks and rational standard-form solutions.
No boundedness or original-coordinate vertex assumption is needed.
These are LP statements, not a general rational-SDP alternative.

For the same bounded procedure reuse Goemans, *An Introduction to Linear
Programming*, October 1994,
[notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/908fe54d659623efadda2d033b895caf_notes_lp.pdf),
The Simplex Method pp.7–8, and Nannicini–Nasrabadi, MIT 15.053 Spring 2013,
[Recitation 3 solutions](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/05885823def0372adb5eae09c7f5490d_MIT15_053S13_rec03sol.pdf),
Problem 3.A–B pp.4–6. The latter is worked artificial-sum initialization,
not a termination theorem. No polynomial pivot guarantee is imported.

Stronger-result comparisons from foundations/10 and L088's assessment
remain applicable: Grone–Johnson–Sa–Wolkowicz (1984), Proposition 2 and
Theorem 7, leaves unspecified entries free and does not preserve shared
union moments; chordality is unproved. General affine SDP alternatives
need qualifications absent from rational LP feasibility, and are not
needed here. No known source evaluates this finite subsystem. Full
matching and supporting Mathlib coverage is not checked; this is no
absence or originality claim.

## Later calculation contract

Essential inputs: L076,L078,L082,L083,L084,L086,L088,L089 and complete
step-318/320/322/324 evidence. Preserve L021,L053,L073,L075 and
foundations/04,09,10,12's PSD, uniqueness, whole-kernel and normalization
qualifications. No recursive ancestor audit or cross-notebook input is
claimed. Freeze rho,p8,pairs,seven RREF/completion,t78=s,L086 columns,
85 domain rows,90 kernel equations,500 types/3000 presentations,36 forced
entries,positive raw scaling and full anchor. L088's moments are only a
regression control. Consume complete load-bearing arrays, not previews.

Reconstruct every original B_i and cross vector at the frozen columns;
record all 81 membership decisions and complete selected index set Z.
Include empty blocks and every nonempty identically zero block. Check
all selected cross vectors vanish and all inherited range identities.
A discrepancy halts rather than silently deleting the offending mode.
Reconstruct the selected original/raw inequalities and their positive
p8*D_i multipliers from L089's full formulas, retaining forced terms
and anchor. Keep all 28 equalities and 45 signs, including duplicate or
zero rows. Verify L084/L088's complete lift and reverse identities in
both coordinates, with 18 signed free variables. Save the full systems,
row labels, membership evidence and pulled-back rows before solving.

Use one fresh rational artificial-sum Phase I, free-variable splitting,
oriented slacks and nonnegative right sides. Use the L088 fixed column
order and least-index entering/minimum-ratio leaving rule with the same
least-index tie break. Save initial/current tableaux, transformations,
basis and full pivot trace. Stop at zero artificial objective, verified
positive optimum, 10000 pivots or 300 seconds, whichever comes first.
Do not resume the stopped unreduced tableau or conic prescriptions.

Accept feasibility only after lifting a full rational 45-vector and
checking every original/raw selected equality, selected mode and sign,
plus all frozen contracts. Accept infeasibility only with nonnegative
weights on original Z-mode/sign inequalities, free multipliers on the
28 equalities, exact cancellation of all 45 original moment coefficients
and a strictly contradictory constant, also reconstructed in raw
coordinates. Track equality-elimination, orientation and positive-scale
multipliers. A reduced-only separator, numerical status or positive
intermediate artificial objective does not suffice. An inconclusive
run is preserved and stopped; no automatic budget increase follows.

## Duplicate and recovery decision

L088's audited witness addresses only the 17 empty-old-block modes.
L089's audited rejection changes no moments and does not settle Z.
ATTEMPTS/071 preserves the capped unreduced full-row run; ATTEMPTS/073
preserves the fixed-assignment rejection. ATTEMPTS/067–068's conic stops
remain intact. This target uses a complete equality reduction and a
structurally selected necessary row set, with a separately testable
witness-or-separator verdict. It does not reopen any stopped run.
The literature gate is complete; the next turn defaults to the single
bounded calculation. No lemmas, mathematical scripts, PROOF.md or DAG.md
are changed by this assessment.
