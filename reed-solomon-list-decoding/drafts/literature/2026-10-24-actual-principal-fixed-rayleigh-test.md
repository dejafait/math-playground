# Actual-principal fixed Rayleigh test — source comparison completed

TARGET: Assess one fixed Rayleigh test of L120's lower block C using v_B=1_{0 in B}-1_{1 in B}, A={0,...,67}, and all B in W, with all L112 data unchanged.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 458 searched Johnson coordinate-difference Rayleigh tests, constant-weight principal matrices, equitable partitions and product-scaled triangle moments; notebook-scoped exact-vector/marked-coordinate searches found only the pending proposal and its historical routing. ATTEMPTS/098–100 and the preceding ready assessments were compared. No matching fixed-assignment verdict was identified; this bounded search establishes no novelty.
SOURCE_EVIDENCE: Freshly inspected Brouwer–Haemers Spectra of Graphs author preprint §2.4 Rayleigh expansion and Theorem 2.4.1 p.33, with §2.3 Lemma 2.3.1 and its proof p.32; Polak arXiv:1703.05171v1 §1.1 Proposition 1.1 and full indicator proof p.2. Reuse foundations/09,12,13,14 and L120's audited entrywise reduction, L112/L113's retained root evidence and L114's scalar result. Schrijver DOI 10.1109/TIT.2005.851748 III.B (62)–(65), manuscript p.7, was cross-checked for normalization/actual-orbit conventions, without a new block theorem import.
COMPARISON: Rayleigh's standard finite real-symmetric criterion covers a fixed negative quadratic direction directly. Existing union-moment and enclosing-arithmetic inputs cover the matrix and its immutable box. They do not compute the marked-coordinate coefficients or the sign of this assignment. The full-global mode-one test and the actual-principal test are different quantities; no theorem transfers the earlier straddles into a verdict here.
GAP: Essential general theorem coverage is ready; the research obligation is one complete marked-coordinate count and rigorous enclosure of this fixed quadratic form, including Boolean diagonal, forbidden opposite pairs, all W and endpoint multiplicities. No coefficient, value, sign or new mathematical lemma is established by this literature turn.
REASON: This fills the changed actual-principal target's missing discovery and source comparison; it approves a known-method finite specialization rather than reopening the stopped global estimates.
SCOPE: Exactly TARGET, with essential inputs L021,L098,L112,L113,L114,L120 and foundations/09,12,13,14, retaining N,H,rho,pairs, all 64 equations, points, scales, endpoints, preconditioner and root. One fixed vector on C itself; no D inverse, optimized vector, solve, scan, retuning, root change, coordinate refinement or midpoint verdict.
LITERATURE_REASON: The actual-principal vector and marked-coordinate counting scope were outside the ready residual-functional assessment; this separate required review supplies that scope, with unchanged general sources reused.

## Main gap, intermediate target and decision test

Arbitrary-center 67/68 safety remains the main gap; full source PSD is
an unresolved necessary condition for this particular fixed assignment.
The intermediate target is exactly TARGET. A rigorous upper endpoint
strictly below zero would reject this assignment's included-anchor PSD,
using L120's existing reduction. Such rejection could guide replacement
of this prescription; it would supply no uniform safety bound. A
nonnegative lower endpoint parks only this vector, without establishing
PSD. A strict straddle parks this estimate. Input/count verification
failure must be reported before any sign claim. There is no automatic
second vector or enclosure repair in this scope.

## Discovery, duplicates and failures

Queries actually submitted on 2026-10-24:

- `Johnson scheme coordinate difference vector Rayleigh quotient constant weight semidefinite principal submatrix`
- `"Johnson scheme" "equitable partition" stabilizer`
- `"Johnson scheme" "difference" "characteristic functions" eigenfunctions`
- `"Rayleigh" "product" "constant weight" semidefinite Johnson`
- `"Johnson" "Rayleigh" "indicator" "principal"`
- `"semidefinite" "triangle" "product scaling" "Johnson"`

Results included generic Rayleigh summaries, equitable-partition papers,
Johnson eigenspace/design discussions and unrelated false positives.
Only the primary sources explicitly inspected below are theorem inputs.
The search supplied no exact verdict for this prescription. Secondary
summaries, snippets and search misses are not coverage or novelty evidence.
The general equitable-partition literature is an optional lead, not an
essential unread source: a direct exhaustive finite count is sufficient.

The scoped exact-term search covered lemmas/, drafts/literature/,
ATTEMPTS/ and history/ for Rayleigh, v_B, coordinate differences and
marked-coordinate terms. It found this proposal, ATTEMPTS/100 and
history/457; an unrelated L104 coefficient notation is not a duplicate.
Relevant proofs and source records were then read selectively.
ATTEMPTS/098 concerns a distance-68 shell's 47 straddles;
ATTEMPTS/099 concerns a sufficient global minimum-plus-correction bound;
ATTEMPTS/100 concerns a residual-corrected global mode-one functional.
None evaluates this vector on C. Their no-refinement stops are preserved.
L115–L119's smaller-slice passes also supply no full-W quadratic verdict.
The bounded search does not certify originality. This is a reproduction
of standard variational and finite-counting methods.

## Primary hypotheses and applicability

Import [Brouwer–Haemers, Spectra of Graphs, author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
§2.4, printed p.33: finite real symmetric matrices and nonzero real
vectors have Rayleigh quotients between their extreme eigenvalues.
The complete orthonormal-eigenvector expansion was freshly read; it
covers singular matrices. Theorem 2.4.1 is adjacent, but its external
proof reference was not followed and is unnecessary for this one-vector
criterion. No generic spectral theorem is to be reproved. The proposed
matrix is L120's finite real symmetric C. Verifying the vector is
nonzero and matching its actual entries remain explicit application
checks. No global Johnson eigenvector assertion is needed.

The same preprint §2.3, Lemma 2.3.1, p.32, gives the equitable-partition
intertwining and proof. It is a comparison tool, not a license to call
the marked partition equitable without checking its row sums. A direct
count avoids needing an eigenvector or quotient-spectrum claim.
The proposed vector must not be replaced by its congruence-transformed
version or treated as a global-kernel mode merely from its appearance.

Import [Polak v1](https://arxiv.org/pdf/1703.05171v1), §1.1 (1)–(3),
Proposition 1.1 and indicator proof, p.2, as already canonical in
foundations/12. The proof establishes the constant-weight conclusion
A(n,d,w), retaining the printed A(n,d) qualification. At order three
and a singleton anchor this is the included union-moment matrix;
(n,w,d)=(1024,68,10) satisfies its hypotheses. Necessity for code
indicators is not sufficiency for a representing measure.

Reuse L120's audited entrywise reduction, zero-row treatment and
root-only exact-cardinality equivalence. Its lower block has Boolean
pair moments on the diagonal, zero at forbidden opposite distances,
and the prescribed product on permitted distinct entries. Its full W
includes all distances 5 through 68. No new Schur argument is needed.
The subsequent residual addition has no separate critical audit; this
test consumes the earlier audited reduction, not the residual estimate.

Reuse Rump, Acta Numerica 19 (2010), DOI
[10.1017/S096249291000005X](https://doi.org/10.1017/S096249291000005X),
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
§5.5 (5.16)–(5.17), author p.28, as inspected in foundations/14.
These enclosing-expression rules allow signed sums and repeated
variables but promise no sharpness. L112/L113 supply the root and
unchanged positive rational endpoints; no fresh nonlinear theorem or
solve is required. L114 supplies the unchanged scalar qualifications.

## Finite specialization to verify next turn

The standard method covers the target, but a citation does not supply
its assignment-specific marked counts. The research turn must justify
any coordinate permutation used directly from L120's ordinary support
entries. It must retain A and the marked roles of 0,1 as appropriate;
permutations of unmarked points may be used only after that verification.
No averaging of RS labels, field operations or determinant exclusions
is licensed. A general block diagonalization is unnecessary.

A direct finite occupancy count may separate the two marked points
from the remaining anchor points and its complement, retaining every
membership case for both support indices. The resulting coefficients,
feasible ranges and multiplicities must be proved and independently
reconstructed; none is derived here. Diagonal coincidences must be
handled with their pair moments before any distinct-entry product is
used. Forbidden opposite pairs contribute zero, not a fictitious x_0
or x_1,...,x_4. Ordered versus unordered pair multiplicities must be
explicit, and zero vector entries do not license deleting nonzero
contributions elsewhere. Full-W coverage must include the boundary
layers even if some marked cases there vanish.

The next turn may write one constructor and independent verifier,
saving full certificates under scripts/finite-support/ and printing
only conclusions, actual/required sign bounds, failures and paths.
It must preserve the root evidence and inspect complete load-bearing
counts and endpoints, not certificate previews. No formula or sign
is preapproved as correct; only this bounded attempt is approved.

## Limitations and Mathlib

No quadratic form has been evaluated in this review, and no lemma or
mathematical script was written. No full source PSD, excluded-anchor
PSD, stronger distribution, global root uniqueness, measure, packing,
RS realization or improvement to 955–957 follows. Full matching
Mathlib coverage for this marked-coordinate finite specialization was
not checked; unknown availability is not evidence of absence.
