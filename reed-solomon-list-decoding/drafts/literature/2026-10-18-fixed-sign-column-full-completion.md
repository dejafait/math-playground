# Fixed L086 columns — complete moment feasibility scope approved

TARGET: Test exact feasibility of all 81 original mode inequalities and 45 moment signs at L086's fixed column parameters in one bounded rational Phase I run.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 315 compared L086's full coordinate and equality-lift specification, L087's hypotheses and original/raw mode formulas, L078's complete fixed-column reduction, history/310,312,314 and ATTEMPTS/067,068,070. Reused the discovery and stronger-result comparisons in the ready simultaneous-eight fixed-column, full-domain remaining-mode and exact sign/equality assessments; no fixed-L086-column full-completion verdict was found in the inspected records. No fresh external search or novelty inference is claimed.
SOURCE_EVIDENCE: Reuse the inspected primary passages recorded in the assessments cited below: Schrijver (2005) Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64), pp.5–7; Sano (2026) Section 2 Corollary 2.2, Theorem 2.6 with both proof directions, Lemma 2.7; Polak arXiv:1703.05171v1 Sections 1.1–1.2 and Proposition 1.1 indicator proof; Goemans Lecture 3 (19 September 2001) Theorems 1,3 pp.1–2; MIT 6.854 (2020) Notes 11 standard-form/rational basic-solution passages; Goemans October 1994 simplex pp.7–8; Nannicini–Nasrabadi MIT 15.053 Spring 2013 Recitation 3 solutions Problem 3.A–B pp.4–6. No new primary retrieval is claimed.
COMPARISON: L078 and L087 already specify all original mode rows at fixed rational columns, including singular ranges and new-only modes. Fixing only L086's columns permits the known rational LP method to test all 45 moment choices; L087 rejects only its particular moments. L086's earlier Phase I omits 53 modes and varies columns. General completion theorems do not impose equal-union moments, and general SDP alternatives do not guarantee rational certificates; neither substitutes for this fixed-column LP specialization.
GAP: Essential source coverage is adequate. The later attempt must reconstruct all fixed-column rational bounds, complete original/raw conversions and all 81 mode and 45 sign rows, then provide an exact original-coordinate certificate or an honest inconclusive exit; no feasibility verdict is supplied here.
REASON: Approve one later RESEARCH / REPRODUCTION exact rational attempt at the saved target using ready methods, without reproving general results or reopening either stopped full-plane conic prescription.
LITERATURE_REASON: The saved target changes from evaluating one complete witness to testing every moment assignment at its fixed columns; this separate review combines ready fixed-column Schur coverage with exact Phase I coverage and checks certificate scope.
SCOPE: Exactly TARGET; freeze all L086 column parameters including t78=s and permit only the 45 original eight/eight moments to vary. Retain all 81 modes and 45 signs, 85 fixed domain rows, 90 kernel equations, full anchor and original/raw normalization. One exact run capped at 10000 pivots or 300 seconds; no scans, retuning, additional constraints or second run.

## Reused primary theorems and applicability

Reuse these completed assessments, without refreshing unchanged searches:
`2026-10-17-simultaneous-eight-shell-fixed-column-completion.md`,
`2026-10-17-zero-plane-remaining-mode-feasibility.md`,
`2026-10-18-zero-plane-affine-sign-feasibility.md` and
`2026-10-18-affine-sign-witness-remaining-modes.md` in this directory.
Their primary proof inspections, not snippets or remembered theorems,
are the coverage reused here. Foundations/04,09,10,12 retain source
qualifications. This review approves applicability; it does not audit
all ancestral mathematics or calculate new coefficients.

Alexander Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf), at the
locations above, covers invariant unequal-layer real matrices on factors
68,956. The inspected extension/reset argument provides completeness;
principal restriction retains layers 0,5,6,7,8. Preserve L078's coherent
positive normalization and both rectangular directions. All 81 positive-
multiplicity modes remain, including singular and empty old blocks.
No code or measure is required. The suspect complement prefactor (61)
is unused. This input supplies the decomposition, not the desired verdict.

Takashi Sano, *Moore-Penrose inverse, generalized Schur complement and
inertia*, version of record 27 February 2026,
[Section 2](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Theorem 2.6 applies to finite Hermitian [A,B;B*,C]: PSD is equivalent to
C PSD, ker(C) contained in ker(B), and A-B C^dagger B* PSD.
Corollary 2.2 and Lemma 2.7 supply range and inverse-action interpretations.
The inspected square-root necessity and triangular-congruence sufficiency
allow singular C. L073 supplies the retained base and L076 the whole-kernel
contract. Use the already specified scalar Schur rows in L078/L087 at
L086's rational columns, retaining the entire anchor subtraction and
actual weighted inverse action. The univariate-new-layer blocks, not a
general rational SDP assertion, are why the existing fixed-column LP
formulation applies. Every original range residual remains a check.

Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight Codes*,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Section 1.1 (1)–(3), Proposition 1.1 and indicator proof p.2, Section 1.2
p.3, supplies equal-union moments and constraint-preserving averaging
for n=1024,d=10,w=68. Preserve the constant-weight conclusion of the
proof despite its displayed notation. The fixed ordinary slice permits
anchor-stabilizer averaging; no actual-label condition is transported.
There is no inferred representing measure or RS realization.

Michel X. Goemans, *Advanced Algorithms*, Lecture 3, 19 September 2001,
scribes Kumar and Sitchinava,
[primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf),
Theorems 1,3 pp.1–2, supplies the finite linear Farkas alternative without
Slater or strict feasibility. Reuse the inspected projection proof and
sign qualifications in the sign/equality assessment. MIT 6.854 (2020),
[Notes 11](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
Introduction, Linear Equalities and Basic Feasible Solutions, covers
standard-form conversion and rational certificates via basic solutions.
Apply it only after slack conversion; retain degenerate and lower-dimensional
cases. Rationality concerns this rational LP, not arbitrary SDP systems.

For the bounded procedure reuse Goemans, *An Introduction to Linear
Programming*, October 1994,
[primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/908fe54d659623efadda2d033b895caf_notes_lp.pdf),
The Simplex Method pp.7–8, reduced costs, ratio tests and degeneracy;
and Nannicini–Nasrabadi, MIT 15.053 Spring 2013,
[Recitation 3 solutions](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/05885823def0372adb5eae09c7f5490d_MIT15_053S13_rec03sol.pdf),
Problem 3.A–B pp.4–6, artificial-sum initialization. The latter is a worked
example, not a termination theorem. No unread Bland proof, polynomial
pivot guarantee or library dependency is needed. The fixed cap bounds
work regardless of eventual termination; final substitution or a Farkas
certificate supplies correctness. No general theorem needs reproof.

## Frozen target and bounded acceptance contract

Main gap: arbitrary-center 67/68-agreement safety, bracket 955–957.
The intermediate target asks whether another choice of moments repairs
L087's failure at exactly L086's columns. A feasible completion keeps
this matrix slice available for further tests; infeasibility stops these
columns independently of the failed moments. Neither resolves other
plane points, global consistency, scalar upper rows, other anchors,
actual-label restrictions, RS realization or a uniform boundary bound.

Essential inputs are L076,L078,L082,L083,L084,L086,L087 and complete
step-308/310/312/314 original/raw evidence; retain L021,L053,L073,L075
and ancestral PSD, uniqueness, whole-kernel and normalization qualifications.
Freeze rho,p8,pairs, seven RREF/completion, the entire rational L086
column point including t78=s, 85 domain factors, 90 kernel equations,
500 types/3000 presentations, 36 forced entries and the full anchor.
Use the 45 lexicographically indexed z moments and positive raw scaling
Y=p8*z/V exactly as specified by L086/L087. Read the complete selected
load-bearing witness values, not previews. L086's old z is comparison
evidence only; it is not imposed as the unknown completion.

Before pivots, save the complete rational original system A*z<=b,z>=0,
all row labels and positive raw conversions. Reconstruct every bound
using the original forced, anchor and inverse-action terms; verify every
range and full-key identity. Keep all 81 modes and 45 signs, even when
zero or duplicate. The 28 selected equalities are necessary by L082/L083;
if L084's equality elimination is used, verify its full lift and reverse
at the frozen columns, and split every free coordinate without adding
sign restrictions. Preserve and verify the original rows regardless of
internal representation. Any failed reconstruction halts without a verdict.

Run one exact rational artificial-sum Phase I with fixed variable order,
nonnegative right-side orientation, artificial initial basis, least-index
negative-reduced-cost entering variable and exact minimum-ratio test
with least-index leaving-basic-variable tie break. Save conversions,
row transformations, initial tableau and checkpointed current state.
Stop at zero artificial objective, verified positive optimum, 10000
pivots or 300 seconds, whichever occurs first. These inherited bounds
are suitable work limits, not a prediction that this larger test will
finish. No warm-start scan, alternate columns, second run or conic solve.

Accept feasibility only by complete rational substitution in all 81
original modes, all 45 signs and every raw Schur remainder, retaining
full anchor and singular/empty cases. Recheck the 85 fixed domain rows,
90 kernel equations and complete presentations at the same columns.
For infeasibility require nonnegative weights on the complete original
inequalities (including signs), zero total coefficient on all 45 moments
and a strictly negative weighted right side. Equality multipliers, if
used in an internal reduction, must be lifted through both orientations
or recorded as free multipliers and eliminated back to original rows.
Check the corresponding raw-coordinate cancellation and fixed pairing.
A positive Phase I status without this certificate is insufficient.
A cap exit, exceptional pivot or failed original/raw identity is
inconclusive. Save full evidence and stop; do not infer infeasibility
or silently increase the budget.

## Duplicate, failure and coverage limits

L086 decided only signs plus selected equalities with variable columns;
L087 decided only one complete (column,moment) point. The older L078,
L080 and L082 fixed-point obstructions concern different columns.
ATTEMPTS/067–068 are stopped full-plane numerical conic prescriptions,
with failed reconstructions and no infeasibility certificate. This test
has one fixed rational column and varies moments only, so it is a
materially different, independently checkable LP test. Those stops remain
intact. Free-entry completion results in foundations/10 do not enforce
these equal-union identifications. No checked source supplies the exact
finite verdict; no novelty is inferred from that fact.

Full matching and supporting Mathlib coverage remains not checked.
This literature-only step writes no lemma, mathematical script, new
coefficient or feasibility result. The mathematical argument and DAG
are unchanged. Approval applies to the saved target for a later turn.
