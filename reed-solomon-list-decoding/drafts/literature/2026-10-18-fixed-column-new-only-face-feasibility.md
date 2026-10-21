# Fixed-column new-only face subsystem — source scope approved

TARGET: Test exact feasibility of L084's 28 equalities, all 17 new-only mode inequalities and 45 moment signs at L086's fixed column parameters.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 317 compared canonical L084's complete parametrization, L086's forward/reverse scaled and raw lift, L087's original modes and audited empty-block case, foundations/10's equality and polyhedral source coverage, history/314,316, ATTEMPTS/067,068,071 and the prior full-completion working record. Reused discovery and stronger-result comparisons from the ready assessments named below; no fresh external search or duplicate subsystem verdict is claimed.
SOURCE_EVIDENCE: Reuse inspected Schrijver (2005) Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64), pp.5–7; Sano (2026) Section 2 Corollary 2.2, Theorem 2.6 with both proof directions, Lemma 2.7; Polak arXiv:1703.05171v1 Sections 1.1–1.2 and Proposition 1.1 indicator proof; Ye October 2017 Theorem 1.11 p.13 and Section 1.5.1 pp.23–24; Goemans Lecture 3 (19 September 2001) Theorems 1,3 pp.1–2; MIT 6.854 (2020) Notes 11 standard-form/basic-solution passages; Goemans October 1994 simplex pp.7–8; MIT 15.053 Spring 2013 Recitation 3 solutions Problem 3.A–B pp.4–6. Precise primary links and qualifications below; no new primary retrieval.
COMPARISON: L084/L086 already give both directions of the equality lift. Freezing columns leaves 18 free moments and a rational LP for the retained new-only rows and signs. L086's sign/equality witness and L087's rejection of its particular moments do not decide this subsystem. Step 316's direct full-row cap supplies no verdict; general free-entry completion and general SDP alternatives do not replace shared-moment rational LP certification.
GAP: Essential source coverage is adequate; the later calculation must reconstruct the fixed equality lift, all 17 new-only rows and 45 signs and verify a full original/raw witness or lifted separator. No coefficients, feasibility verdict or new theorem are supplied by this review.
REASON: Approve one later RESEARCH / REPRODUCTION attempt using the existing equality reduction and known exact LP method on this independently testable subset; preserve the full-row and conic stops.
LITERATURE_REASON: The target changes to a smaller row set with an 18-free-moment equality reduction; the previous approval named the complete fixed-column target, not this separately bounded subset.
SCOPE: Exactly TARGET; all L086 columns frozen, all 28 equalities, 17 modes with max(a,b)=8 and 45 signs retained. One equality-reduced rational Phase I run capped at 10000 pivots or 300 seconds; no full-row rerun, scan, retuning, added constraint or second run.

## Relevance, known results and reuse

Main gap: arbitrary-center 67/68-agreement safety, bracket 955–957.
The intermediate target tests whether the new-only modes can be repaired
by changing moments at precisely L086's columns. A rational witness
would park only this smaller necessary subsystem as an exclusion test.
A lifted strict separator would reject these columns for the full
system. Neither supplies a uniform family bound or changes the bracket.
The 36 omitted mixed modes, other plane points, scalar upper rows,
other anchors, global consistency and RS realization remain unresolved.

Reuse the inspected primary statements and proof cases recorded in
`2026-10-18-fixed-sign-column-full-completion.md`,
`2026-10-18-zero-plane-affine-sign-feasibility.md`,
`2026-10-18-affine-sign-witness-remaining-modes.md` and
`2026-10-17-zero-plane-positive-mode-compatibility.md` in this directory.
Their searches include rational LP feasibility, exact simplex, linear
compatibility, parametric systems and stronger completion results.
This is reuse of adequate coverage, not a new search or originality claim.
The reviewed target changes the selected rows, not the source hypotheses.

Alexander Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
at the locations in SOURCE_EVIDENCE, supplies the invariant unequal-layer
real decomposition for factors 68,956. The inspected extension/reset
proof permits principal restriction to layers 0,5,6,7,8. Preserve the
coherent positive congruence and both rectangular directions; the
suspect complement prefactor (61) remains unused. L078/L087 already
identify all 17 new-only modes, with empty old blocks and no anchor.
Dropping the mixed inequalities gives a necessary subsystem, not an
alternative full PSD criterion.

Takashi Sano, *Moore-Penrose inverse, generalized Schur complement and
inertia*, version of record 27 February 2026,
[Section 2](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Theorem 2.6, Corollary 2.2 and Lemma 2.7, covers finite Hermitian blocks:
retain old PSD, the full kernel/range condition and the Schur remainder.
The previously inspected square-root necessity and triangular-congruence
sufficiency include singular old blocks. New-only blocks have no old
inverse cost. No Slater condition or rational-SDP assertion is needed.
Retain the full anchor in the selected equalities and ancestral checks,
even though it is absent from the 17 new-only inequalities.

Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight Codes*,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Sections 1.1–1.2, Proposition 1.1 and its indicator proof p.2, supplies
equal-union moments and constraint-preserving averaging for the ordinary
n=1024,d=10,w=68 slice. Preserve the constant-weight conclusion proved
there despite the displayed notation. No actual-label condition is
averaged and no representing measure or common-center RS list follows.

Yinyu Ye, *Conic Linear Programming*, December 2004, revised October 2017,
[monograph](https://web.stanford.edu/class/msande310/sdpmain.pdf),
Theorem 1.11 printed p.13 (PDF p.26), stated without proof there, and
Section 1.5.1 pp.23–24 (PDF pp.36–37), supplies the equality alternative
and pivot/back-substitution method. Section 2.3 opening p.42 covers
scalar complementarity. L084 already specializes these to the full
rank-27 equality system; this review does not redo its elimination.
L086 records scaled and raw lift/reverse identities, not just a
particular feasible solution. That complete locus contract is essential.

Michel X. Goemans, *Advanced Algorithms*, Lecture 3, 19 September 2001,
scribes Kumar and Sitchinava,
[primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf),
Theorems 1,3 printed pp.1–2, provides the finite Farkas alternative,
including free-variable inequalities. Reuse the inspected projection
proof and source-sign qualifications in foundations/10; no strict
feasibility is required. MIT 6.854 (2020),
[Notes 11](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
Introduction, Linear Equalities and Basic Feasible Solutions, covers
free-variable splitting, slacks, rational basic solutions and degeneracy.
Apply it after standard-form conversion; neither original-coordinate
vertices nor boundedness are assumed. Normalize a strict dual pairing
before applying the same rational-feasibility coverage to certificates.

For the bounded procedure reuse Goemans, *An Introduction to Linear
Programming*, October 1994,
[notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/908fe54d659623efadda2d033b895caf_notes_lp.pdf),
The Simplex Method pp.7–8, and Nannicini–Nasrabadi, MIT 15.053 Spring 2013,
[Recitation 3 solutions](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/05885823def0372adb5eae09c7f5490d_MIT15_053S13_rec03sol.pdf),
Problem 3.A–B pp.4–6. The latter is a worked artificial-sum initialization,
not a termination theorem. No polynomial pivot guarantee or unread Bland
proof is imported. Exact substitution or a lifted Farkas certificate,
not solver status, establishes the eventual verdict.

The stronger-result comparisons remain applicable: foundations/10's
Grone–Johnson–Sa–Wolkowicz (1984), Proposition 2/Theorem 7, allows
unrestricted missing entries and does not enforce equal-union moments;
chordality is not established here. The assessed Garloff–Popova–Smith
interval theorem assumes square systems and inclusion hypotheses,
not this underdetermined exact equality locus. No such result supplies
the finite verdict. QSopt_ex and other unread algorithm leads remain
unnecessary; no new installation or source blocker is introduced.
Full matching and supporting Mathlib coverage is not checked.

## Frozen inputs and bounded certificate contract

Essential inputs: L076,L078,L082,L083,L084,L086,L087 and complete
step-316 original/raw systems, initial/final tableaux and trace; retain
step-308/310/312/314 evidence and L021,L053,L073,L075 with
foundations/04,09,10,12's ancestral PSD, uniqueness, whole-kernel and
normalization qualifications. The cap record is historical evidence,
not a new audit of every pivot. No cross-notebook input is used.

Freeze rho,p8,pairs, seven RREF/completion, all rational L086 column
parameters including t78=s, 85 domain rows, 90 kernel equations,
500 types/3000 presentations, 36 forced entries, full anchor, 45
lexicographic z moments and positive scaling Y=p8*z/V. Consume complete
load-bearing witness arrays, not previews. L086's old 45 moments are
comparison evidence only; they are allowed to change.

Before any pivot reconstruct all selected original/raw equalities and
the saved L084 particular solution and 45-by-18 homogeneous matrix.
Verify the saved forward and reverse identities from L086 in both
scaled and raw coordinates, specialized to the fixed columns. Preserve
all 28 equalities despite their rank 27. Use exactly the existing
18 equality-free coordinates, all signed real, without imposing a sign
on those coordinates. Do not infer completeness from a forward lift
alone. Any failed equality, raw identity or reverse check halts.

Reconstruct all 17 original rows max(a,b)=8 from the complete original
mode formulas, keeping forced and free contributions separately. Verify
their raw counterparts and positive multipliers p8*D_i. Retain all
45 signs, even zero or duplicate rows. Save the complete original
28-equality/62-inequality system, every row label, equality lift and
its pulled-back rows before solving. Recheck the 85 frozen domain
rows, all kernel equations and presentation identities. This is a new
subsystem model; do not resume step 316's stopped tableau.

Run one rational artificial-sum Phase I after splitting the 18 free
coordinates into positive/negative parts and introducing oriented
slacks. Keep fixed column numbering and nonnegative right sides; start
with the artificial identity basis. Enter the least-index nonbasic
variable with negative reduced cost and use the exact minimum-ratio
test with least-index leaving-basic-variable tie break. Save initial
and checkpointed current tableaux, basis, row transformations and full
pivot trace. Stop at zero artificial objective, verified positive optimum,
10000 pivots or 300 seconds, whichever occurs first. No second run,
warm-start scan, retuning, new variable bounds or conic solve is approved.

Accept feasibility only by lifting a complete rational witness and
checking all 28 original/raw equalities, 17 original/raw inequalities
and 45 signs, with the unchanged column/domain/kernel contracts.
This would not certify the 36 omitted mixed inequalities. Accept
infeasibility only with nonnegative weights on the original 62
inequalities and explicitly free multipliers on the 28 equalities,
zero total coefficients on all 45 original moments and strictly
negative weighted right side, also checked in raw coordinates.
Track every elimination, orientation and scaling multiplier. Free
equality multipliers are allowed because the selected equalities are
necessary by L082/L083; do not incorrectly require them nonnegative.
A reduced-only separator or positive intermediate objective is inadequate.

A cap, exceptional pivot or failed original/raw reconstruction is
inconclusive. Save the full state and stop this bounded attempt without
raising the budget. A witness parks this subset alone; a separator
rejects precisely these fixed columns. Either informs the joint-matrix
route while independent global and RS gaps remain open.

## Duplicate and failure decision

L086 solves signs/equalities while allowing columns to vary; L087
rejects only one complete point. Neither decides whether another moment
assignment works at these fixed columns. Step 316 and ATTEMPTS/071
stop the direct unreduced full-row exact prescription after a time cap;
no infeasibility was certified. ATTEMPTS/067–068 stop two full-plane
numerical conic prescriptions with failed exact reconstructions.
This target drops all mixed inequalities and uses the complete equality
reduction at one fixed rational column. Its independently checkable
outcomes differ from those stopped prescriptions; their evidence remains
intact. No new calculation, lemma or mathematical script is written in
this literature-only step. Approval covers the saved target only.
