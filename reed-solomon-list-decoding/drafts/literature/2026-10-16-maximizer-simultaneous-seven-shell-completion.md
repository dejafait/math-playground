# L072 maximizer — simultaneous completion source scope approved

TARGET: Test simultaneous seven-shell PSD completion at L072's exact maximizer with the original 36 nonnegative new/new variables.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 251 searched the exact maximizer/completion terms in the 2026-10-16 assessments, history/244–250 and ATTEMPTS/053–054, and read ATTEMPTS/049–054 and L067/L072's relevant proof passages. Reused the ready simultaneous-shell and remaining-mode discovery; primary LP and singular-Schur passages were freshly retrieved as detailed below. No completed duplicate changed-point verdict was found in this scope.
SOURCE_EVIDENCE: Reuse foundations/04,09,10,12 and the ready 2026-10-14 simultaneous-five-six-seven-shell and 2026-10-15 zero-point-remaining-mode assessments. Freshly read Sano DOI 10.1007/s44146-026-00231-y, Section 2 Theorem 2.1/proof, Corollary 2.2, Theorem 2.6/proof and Lemma 2.7/proof; Goemans Lecture 3 (19 September 2001), Theorems 1/proof and 3, printed pp.1–2; MIT 6.854 2020 LP notes, standard-form conversion, rational representation and complete standard-form basic-solution argument.
COMPARISON: The known mixed-layer and singular-Schur inputs cover the same finite matrix at a changed rational column; Farkas and rational LP certificates cover the resulting affine feasibility test. L072 certifies this column and one positive dual pairing, not joint feasibility. L071's separator and L070's particular equality solution apply to the origin and cannot supply this point's verdict or unchanged right sides.
GAP: Reevaluate all 64 original mode bounds at exactly L072's maximizer, preserve every singular range, anchor term and forced entry, and test all 36 original nonnegativity conditions. No inspected source decides these coefficients; no new system, rank, assignment or separator was computed here.
REASON: Essential coverage is adequate for one later REPRODUCTION application at exactly TARGET. The changed-point certificate requires finite specialization, without reproof of matrix decomposition, generalized Schur or linear alternatives. This approval closes source scope only and claims no source-level discovery.
LITERATURE_REASON: The supervisor requires separate approval of the newly proposed maximizer test; prior approvals covered either a different fixed column or the sign of one dual on a plane. This review resolves that changed-point scope while reusing ready general coverage.
SCOPE: Exactly TARGET at u=0,v=v_dagger,w=w_star, original positive rho,p7,pairs and RREF, all 28 forced entries, 270 types/1620 presentations, all 64 original modes and 36 original positive-valency-scaled nonnegative variables. No new/new scalar upper rows, retuned columns/base/pairs, excluded-anchor test, labeled constraints or global feasibility conclusion.

The main gap remains arbitrary-center safety at 67/68 agreements; the
955–957 bracket is unchanged. Essential inputs are L061,L062,L065,L067,
L068,L069,L071,L072 and foundations/04,09,10,12. Fix exactly L072's
u=0,v=v_dagger,w=w_star and all its rational column entries, original
rho,p7,pairs, RREF, anchor and 28 forced seven/seven entries. Retain all
270 types and 1620 presentations. The original 36 positive-valency-scaled
variables must be nonnegative, and all 64 original Schur inequalities
must hold. The already checked ranges remain essential premises.

The bounded next calculation, now source-scope approved, should reconstruct
the original right sides at this exact point and seek either a rational
feasible assignment or a rational nonnegative separating certificate.
Neither a numerical optimizer status nor L072's positive pairing decides
this. The continuation/abandonment test is exact substitution into every
original row and sign, or exact cancellation with a strictly negative
fixed pairing. An unresolved search should retain its actual obstruction
and evidence without asserting infeasibility.

A feasible assignment would retain this particular included-anchor
five/six/seven matrix as a nonexclusion witness. A separator would reject
this maximizer and motivate a different column or a family-level argument.
Both outcomes leave other zero-plane points, untested seven/seven scalar
upper rows, excluded-anchor and other-anchor matrices, global moment
consistency, representing measures and RS realization unresolved. No
uniform safety bound or list is inferred. This target is not a repetition
of the exhausted unchanged-product-weight strict-exclusion route.

## Primary theorem comparison — step 251

The ready assessments reused are
`2026-10-14-simultaneous-five-six-seven-shell-extension.md`,
`2026-10-15-zero-point-remaining-mode-feasibility.md` and
`2026-10-16-alternative-product-dual-zero-plane.md`.
Their discovery and inspected theorem coverage remain adequate; changing
a rational column requires a new application, not another discovery of
the same general machinery. No fresh broad external search was needed.

Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B
(64), printed pp.5–7. Reuse the inspected tensor change of basis and
complete extension/reset proof in foundations/09. Factors 68,956 and
layers 0,5,6,7 meet its index ranges. Changing the cross entries does
not change this algebra's scope. Preserve all blocks meeting the chosen
layers, including new-only modes, and the audited coherent normalization.
The complement prefactor is unused. This is an applicability comparison,
not a fresh verification of the prescribed matrices.

Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2 and Theorem 2.6. Freshly read their statements,
Theorem 2.1's complete range/congruence proof, Theorem 2.6's square-root
necessity and triangular-congruence sufficiency, and Lemma 2.7's proof.
For finite Hermitian [A,B;B*,C], PSD is equivalent to C PSD,
ker(C) contained in ker(B), and A-B C^dagger B* PSD. Singular C
is allowed. Real symmetric mode blocks satisfy these hypotheses;
finite-dimensional ranges are closed. The actual column must satisfy
every range equation before inverse-on-range costs are used. Keep
the transported anchor and weighted normalization. This theorem
does not supply the prescribed finite feasibility verdict.

For ordinary union moments and constraint-preserving averaging reuse
Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight Codes*,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
15 March 2017, Section 1.1 (1)–(3), Proposition 1.1 and indicator
proof, p.2, and Section 1.2, p.3, as qualified in foundations/12.
Here n=1024,d=10,w=68; retain the proof's constant-weight conclusion.
Only the ordinary unlabeled slice can be averaged under a group
preserving every prescribed entry and sign. No actual subgroup-label
symmetry or representing measure is assumed.

Import Michel X. Goemans, *Advanced Algorithms*, Lecture 3,
19 September 2001, scribes Abhinav Kumar and Nodari Sitchinava,
[MIT OCW primary PDF](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf),
Theorems 1 and 3, printed pp.1–2 (PDF pp.2–3). Freshly read the
full projection proof and strict-sign ending, and the inequality
alternative. For a finite real affine inequality system, the alternative
supplies an infeasibility certificate with nonnegative multipliers,
zero total variable coefficient and strictly negative total bound.
It requires no strict feasibility. Include sign rows among the original
inequalities. OCR garbles some signs; the nonnegative-variable proof
and the mutually exclusive inequality display clarify the convention.
The OCW wrapper is Fall 2008; the lecture itself is dated 2001.
No general SDP strong-separation theorem is imported.

Reuse rational-certificate coverage in foundations/10, freshly checked
against [MIT 6.854's 2020 LP notes](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
“Introduction”, “Linear Equalities” and “Basic Feasible Solutions”.
Read standard-form conversion using slacks and split free variables,
Cramer's-rule rational representation, and the complete movement-to-a-
basic-solution and tight-system reconstruction arguments. These support
exact rational certificates for the intended rational linear problem;
they do not decide it. The notes combine multiple lecture years.
Their unrelated informal compactness and geometry assertions are unused.
No source or general theorem is reproved in this review.

## Fixed-point distinction, evidence requirements and limits

The local searches were `maximizer`, `v_dagger` and
`seven-shell.*completion` in the paths in SEARCH_EVIDENCE.
L067 and ATTEMPTS/049 exclude the immutable old column. L068–L070
and ATTEMPTS/050–052 retain, respectively, an old-dual zero, column
scalar feasibility and signed equality consistency at the origin.
L071 and ATTEMPTS/053 reject that origin. L072 and ATTEMPTS/054 stop
strict plane exclusion by L071's unchanged product weights. Their
conclusions are preserved; none tests this maximizer's joint completion.

Use L072's exact definition v_dagger=beta_v/alpha and its exact w_star,
not rounded certificate previews. Reconstruct L067 equation (1) with
the original 36 variables and reevaluated fixed bounds at this point.
L070's rank-23 origin particular solution and its 13-coordinate affine
space are not an unchanged solution at the new column. Any equality
reduction must have freshly checked right sides, consistency and a
checked translation back to all original rows. No equality reduction
is derived or asserted valid for the new right sides here.

The later pass requires one exact rational nonnegative assignment
substituted into all 64 original mode rows, with all fixed lookups,
singular ranges, positive scalings and full anchor correction recovered.
An obstruction requires a rational separating combination checked on
the original mode and sign rows, with exact coefficient cancellation
and strictly negative fixed pairing. Sign multipliers may be needed;
do not restrict discovery to product weights or sign-free separators.
Numerical LP status, a sampled minor or a single positive dual pairing
is insufficient. Save complete evidence and independently reconstruct
the load-bearing residuals. An unresolved bounded search must report
its concrete obstruction without claiming infeasibility.

A pass retains only the specified included-anchor matrix and the tested
nonnegativity. Untested seven/seven scalar upper rows, other anchors,
global consistency, measures and RS realization remain independent gaps.
A separator rejects only this point and requires a changed, separately
assessed continuation. No uniform family bound, unsafe list or boundary
improvement follows in either case. Full matching and supporting Mathlib
coverage for these matrix/LP statements and the finite instance is not
checked; unknown availability is not evidence of absence.

Step 251 approves one later REPRODUCTION research attempt at exactly
TARGET. No lemma, mathematical script, coefficient calculation or
feasibility verdict was produced in this literature-only turn. The
main argument and DAG are unchanged.
