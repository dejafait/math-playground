# Source comparison for the width-one selected-constraint audit

TARGET: Critically audit L449 (1)--(8)'s width-one selected-constraint preservation, including endpoint calibration, full covariance correction, support and all rare/translated moment budgets on the original real-H cutoff ray.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 301 compared the complete L449 statement/proof with the ready width-one and L447-audit assessments, L438 (9)--(20) and its envelopes, L443 (1)--(16), L445/L446 interfaces, L447's separate step-287 audit and the L444/L446/L448 stop records; reuse the recorded exact variance/covariance and endpoint occupation-measure searches, with no fresh external retrieval or novelty inference.
SOURCE_EVIDENCE: Reuse Hunter Chapter 1 Theorem 1.29/Example 1.30 p. 12 and compiled notes revision 2014-06-18 Theorems 3.60, 3.62--3.63 pp. 79--80; Boyd--Vandenberghe (2004, corrected seventh printing 2009) sections 2.2.5--2.3.1 pp. 34--36; Boyd EE263 Lecture 8 (2007--08) slides 8-2--8-7 and 8-9; Carlen--Lieb arXiv:0904.0734v2 pp. 1--2, Horn theorem after (1.1), proof through (1.2); Bourgain arXiv:1408.5794v2 Theorem 5 (0.5) p. 2 and completion (4.1)--(4.3) p. 19; necessary occupation identity math/0703377v1 sections 2.1--2.3 pp. 3--5. Precise hypotheses and reuse paths below.
COMPARISON: These inputs cover the unchanged general cutoff, scalar peak, positive-matrix, finite right-inverse, real orthogonal and fixed-H endpoint interfaces without a narrow-width hypothesis. Neither they nor audited L447 establish L449's unit-width budgets, peak support, exact calibration or full selected-constraint conclusion; independent application checks remain necessary.
GAP: Independently audit L449 (1)--(8) and the complete stated selected list on the original real-H ray, including every endpoint, rare/mass/translation term and Borel branch; coverage is adequate but the claims remain unverified, with no revised law or forced-cross PSD verdict.
REASON: No essential unread source is identified for this unchanged finite-dimensional audit; SPECIALIZE authorizes a later REPRODUCTION proof audit of the law-specific application, not a new theorem, source reproof or endorsement of L449.
LITERATURE_REASON: The newly selected full L449 preservation audit removes the amplitude/support assumptions left in the completed L450 audit; this required separate theorem-scope comparison reuses ready primary coverage instead of repeating browsing.
SCOPE: L449 (1)--(8) and their full selected-constraint conclusion, including the fixed-H Lipschitz representative and exact scalar endpoint equality, with original cutoff, rare components, probabilities, w, m and selected tolerances; no audit of (9)--(12), new law, extra identity, actual excursion, full forced covariance feasibility or RH claim.
COVERED_TARGET: Critically audit L449 (1)--(8)'s width-one selected-constraint preservation, including endpoint calibration, full covariance correction, support and all rare/translated moment budgets on the original real-H cutoff ray.

Main gap: global mixed positivity. The intermediate target is validation
or correction of the still-unaudited width-one construction used by L450.
Its downstream use is to establish which selected constraints genuinely
survive for the fixed data in the now-audited block comparison. It need
not decide that comparison's remaining unsaturated interior or layers.

Use L438's complete rare/mass/mean/covariance construction, L443's
finite correction interface, L445's branch-safe scalar regularity,
L446's endpoint functional, L447's endpoint calibration and L449's
width-one formulas. Keep the original real-H cutoff, rare components,
w, m and all selected tolerances. The exact surviving tolerances,
support and measurability are claims to audit, not new assumptions
that the audit may silently grant. L450's local validation does not
discharge them.

## Completed source comparison — step 301

LITERATURE / NOVELTY_UNCHECKED / literature_comparison; outcome
EXPLORATION. This completed comparison changes the pending coverage
to SPECIALIZE. It is no mathematical validation, new estimate,
novelty finding or progress beyond the checked sources. No lemma or
mathematical script is written. Mathematical exploration usage stays
2 of 3 since step 294; this literature step does not renew it.

The existing ready records reused here are
`drafts/literature/2026-10-20-width-one-endpoint-forced-cross.md`
and `drafts/literature/2026-10-20-endpoint-repair-critical-audit.md`.
Their previously inspected statements and essential proof cases remain
adequate; no fresh external source inspection is claimed. This exact
audit scope is approved here for a later, separate research turn.

### Primary hypotheses, proof cases and specialization limits

[Hunter, Notes on Partial Differential Equations, Chapter 1,
Theorem 1.29 and Example 1.30, printed p. 12](https://www.math.ucdavis.edu/~hunter/pdes/ch1.pdf#page=13)
give a smooth cutoff valued in [0,1], equal to one on the smaller
set, for compactly nested open sets. The convolution proof and
example were inspected in the endpoint-construction record
`drafts/literature/2026-10-20-endpoint-localized-bulk-covariance-repair.md`.
The separate chapter is undated; the compiled notes have revision
18 June 2014. L449 retains the same fixed real-line cutoff and
translates it at width one before restricting to the closed height
interval. No existence hypothesis changes. The theorem does not
assert the recentered endpoint signs or any moment budget.

[Boyd--Vandenberghe, Convex Optimization, 2004, corrected seventh
printing 2009, sections 2.2.5--2.3.1, pp. 34--36](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=48)
cover convexity of the real PSD cone by its quadratic-form proof.
This applies to the nonnegative K multiple, with no restriction on
temporal width. Signed recentering and finite correction are separate
perturbations: their norms, the lower covariance margin and negative
J-trace are local claims, not supplied by cone convexity. The scalar
Schur-complement theorem used in L449's later forced-block section
is not needed to validate (1)--(8); no PSD verdict for that block
is in this audit target.

[Boyd, EE263 Autumn 2007--08, Lecture 8, slides 8-2--8-7 and 8-9](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/min-norm.pdf)
states the least-norm solution A^T(AA^T)^(-1)y for real full-row-rank
A. The inspected proof uses orthogonality and the projection formula.
L443 already implements it with the zero-column augmentation of its
three-dimensional triangular map. L449 keeps that coefficient space,
w, C_H and D_H; only the input residual changes. Full rank and its
old uniform conditioning may be reused, but the new residual vector,
signs and exact cancellation must be audited. There is no new
infinite-dimensional projection or general right-inverse reproof.

[Carlen--Lieb, Short proofs of theorems of Horn and Mirsky on
diagonals and eigenvalues of matrices, arXiv:0904.0734v2,
13 May 2009, pp. 1--2](https://arxiv.org/pdf/0904.0734v2),
Horn theorem after (1.1), proof through (1.2), supplies a real
orthogonal realization when the proposed diagonal is majorized by
the real eigenvalue list. The reused inspection includes the scalar
and equality cases and induction. Its application to real symmetric
SJS uses the constant trace-average diagonal and requires the new
positive covariance first. The source supplies neither a measurable
parameter selection nor translated negative support. L419's finite
rotation implementation, as retained in L438/L443 and checked in
L447's step-287 audit, covers arbitrary positive covariance matrices,
including equality and tie branches. The later audit must verify
that L449 actually remains in this domain and that the new peak
amplitudes allow the translation estimate. Closeness of old and new
selected bases, or small integrated peak mass, cannot replace it.

[Bourgain, Decoupling, exponential sums and the Riemann zeta
function, JAMS 30 (2017), 205--224, arXiv:1408.5794v2,
Theorem 5 (0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2)
gives the unconditional critical-line bound with exponent
13/84+epsilon for each fixed epsilon>0. The reused source record
also inspected completion cases (4.1)--(4.3), p. 19. L447's audited
complete old-density bound uses only the actual scalar Hardy modulus,
including zeros, with its stated fixed epsilon. L449 keeps exactly
that old density before the new bump, so this source has no changed
hypothesis. Its inequality supplies no derivative-jet bound, no
artificial-law estimate and no uniform onset in epsilon. Reuse the
old scalar specialization and check its role in L449's amplitudes;
do not reprove Bourgain or import a stronger jet assertion.

[Hunter, compiled notes, revision 18 June 2014, Theorems 3.60,
3.62--3.63, printed pp. 79--80](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf)
cover AC reconstruction and integration by parts on a finite closed
interval, with the actual endpoint values. The same fixed-H setting
has smooth positive L. L445 supplies the original Lipschitz
representative, not an H-uniform derivative bound. The changed
representative must still agree with its full raw 11 entry at both
endpoints; the zero-11 correction cannot be silently omitted without
checking that fact. L446's weak-uniqueness application belongs to
the later forced-cross problem; no new uniqueness proof is needed
to audit the scalar endpoint cancellation itself.

[Lasserre--Henrion--Prieur--Trelat, Nonlinear optimal control via
occupation measures and LMI-relaxations, math/0703377v1,
sections 2.1--2.3, (2.7), (2.10)--(2.12), pp. 3--5](https://arxiv.org/pdf/math/0703377v1)
supplies the necessary C1 finite-interval trajectory identity.
The reused exact-block assessment specializes it at fixed H on
compact trajectory boxes. L443 already records all three complete
raw-second test polynomials and their triangular residual map.
L449 needs no derivative of a Borel atom and no occupation-measure
converse. A pass would concern only those finite identities.

L429's existing finite-stage Poisson limits and real-H cutoff
consequences are unchanged local inputs. L446 records the original
stage conditions B_(j+1)>=2B_j and log B_j>=M_j^8; L429's
cutoff section establishes finitely many stages on compact parameter
ranges and every-real-height validity within each stage. The audit
must retain those exact stages, not obtain estimates by choosing a
new diagonal sequence. No new growing-prime theorem or additional
equidistribution source is required for this fixed-data audit.

### Exact local audit obligations and duplicate/failure check

The inspected L438 (9)--(20) provide the entire rare components,
probabilities, remaining mass, translation and full matrix correction,
as well as the selected tolerances and separately fixed character/cap
quantifiers. L443 (1)--(16) give the complete residual map, uniform
inverse and realized negative-cone covariance. L445 and L446 fix
the representative and endpoint functional; L447's separate audit
checks their use for its original width. These inputs define the
application obligations; reading them here does not audit L449.

The later audit must check all the following in the canonical proof:

- (1)--(3): restricted unit supports, both recentered endpoint signs,
  every old rare peak in the inherited defect, amplitude definitions
  including zero defect, and exact J_H[q]=0 with both endpoints.
  All changed integrated peak powers must be checked at width one.
- (4): complete raw-second residuals, including the middle identity's
  K22+K13 cancellation, the unchanged inverse, zero integrated full
  correction, exact six integrated seconds and first B mean. Tiny
  odd-second tolerances cannot be paid with an absolute o(ell) bound.
- (5) and the support paragraphs: signed perturbation versus the
  covariance margin, trace at the full peak amplitude, all six atoms
  after translation and their Borel selection cases. Parameter
  integrals, denominators and local bounds must hold across original
  stage jumps on one eventual real-H ray. A fixed-H Lipschitz claim
  must use the stated pointwise representative, including endpoints.
- (6)--(8) and the final physical-envelope paragraph: both weighted
  second tests at their original tolerances; all signed cubic
  remainders and every separately fixed three-prime cosine limit;
  all 23 quartic coefficients including zero and signed ones; both
  absolute third envelopes and the fourth envelope; physical
  bounds; and one family with vanishing capped absolute cubic for
  every fixed cap. Signed cubic linearity must remain distinct from
  the absolute third and fourth bounds.

The strongest reusable local result is L447's audited preservation
at width H^-10. L449 is not covered by merely copying its negative
powers of H. The original width-one source assessment approved a
construction/test attempt, not an independent verification of its
eventual result. L450's step-300 audit checks its remainder and
interior pass regions using L449's structural/amplitude inputs; it
does not duplicate this full preservation audit.

Recorded failures remain in
`ATTEMPTS/2026-10-20-all-temporal-bounded-covariance-extension.md`,
`ATTEMPTS/2026-10-20-unchanged-x-second-integrated-xy-extension.md`
and `ATTEMPTS/2026-10-20-endpoint-repair-fixed-data-forced-cross.md`.
L444 fixes the 11 entry and a bounded repair; L446 fixes the entire
density; L448 tests a narrow-layer derivative-forced block. None
decides this changed-density, width-one selected-preservation claim.
Their stops remain evidence on those scopes. No historical stop is
treated as a ban on changed data, and no stopped envelope or scalar
excursion search is reopened by this audit.

The exact discovery queries already recorded in the ready width-one
assessment are `"prescribed variance" "derivative" covariance positive
semidefinite` and `"endpoint" "covariance" "occupation measures"
positive semidefinite`. They supplied no inspected theorem for the
full law; no novelty inference follows. Ready primary coverage above,
rather than search snippets or a new search quota, justifies reuse.
Full matching Mathlib coverage remains unchecked, not absent.

Continue to the separate REPRODUCTION mathematical audit if these
unchanged input hypotheses are available. The pass test is the full
stated selected list and exact equalities on the original eventual
ray, with the original separately fixed quantifiers. If a budget,
branch, equality or source hypothesis fails, identify the exact
failure and correct, narrow or withdraw that claim; an unresolved
check stays unfinished. No new law or unassessed repair is authorized.
Even a pass validates only a local selected-law input. Actual
excursions, monotonicity and duration, remaining PSD regions/layers,
other temporal/mean identities, actual/global realization, clipping,
capped nondegeneracy, L413's margin and mixed positivity remain open.
