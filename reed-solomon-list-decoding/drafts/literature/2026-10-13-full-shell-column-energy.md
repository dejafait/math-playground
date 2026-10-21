# Full-shell one-column energy — source comparison approved

TARGET: Determine whether any column in L059's complete nonnegative interval satisfies the scalar generalized-Schur energy inequality for one distance-six extension of L056's anchored shell.
CHECKED: 2026-10-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped duplicate/failure comparison in L056,L059, ATTEMPTS/038–041 and the existing nullspace assessments; directly read Sano's additional inverse-action passage and searched singular inverse spectral action and convex quadratic minimization, then inspected Boyd–Vandenberghe's author slides. Exact queries and inspected passages are recorded below.
SOURCE_EVIDENCE: Reuse foundations/09,10,12; additionally inspected Sano (2026), DOI 10.1007/s44146-026-00231-y, Section 2 Lemma 2.7/full proof; Boyd–Vandenberghe–Nobel revised 402-page author slides, PDF pp. 53–55,97–99,105–106, retrieved 2026-10-13. Primary citations and qualifications are in foundations/10.
COMPARISON: Known singular-Schur, range-inverse, orthogonal product-spectrum and convex-QP inputs cover the required tools under the unchanged real finite unlabeled hypotheses. They do not supply the prescribed interval's energy coefficients, minimizer or inequality verdict; this is an exact finite specialization, not a novelty claim.
GAP: Research must justify the weighted inverse-energy realization and transported anchor, reconstruct the exact scalar quadratic on the entire audited interval, and certify its minimum against the unchanged new diagonal. No energy formula, minimizer, sign or PSD verdict is derived in this review.
REASON: Essential coverage now permits one materially different energy calculation after the audited kernel test is exhausted; standard theorems are imported, and only their problem-specific application and exact certificate require work.
LITERATURE_REASON: The changed energy target lay outside the prior kernel-only assessments; inverse action and interval-minimization coverage were essential unread inputs. Reuse all unchanged spectral/hierarchy coverage rather than repeat its source searches.
SCOPE: Exactly TARGET at L053's fixed positive rho,p_i, audited L056's unchanged full shell and critically verified L059's complete invariant interval; normalization, weighted spectral application and exact scalar minimization only. No changed pairs, shell coefficients, actual-label constraints or other columns.

Essential inputs: L053's positive rational rho and unchanged p_i,
L054's full-region dictionary, audited L056's entire PSD shell and its
positive/zero mode data, and critically verified L059's full nonnegative
affine interval, fixed represented entries and transported anchor.
Preserve the new diagonal and anchor rho*p_6, the five represented
entries, ten zeros and 21 free entries. Retain foundations/09,10,12.

The exact primary criterion to compare is Takashi Sano, *Moore-Penrose
inverse, generalized Schur complement and inertia*, Acta Scientiarum
Mathematicarum (27 February 2026),
[Theorem 2.6 and Corollary 2.2](https://link.springer.com/article/10.1007/s44146-026-00231-y).
Its relevant criterion/proof coverage is reused from foundations/10.
The additional inverse-action coverage and duplicate comparison below
complete approval for the exact changed application. The conclusion of
the criterion still has to be tested by research.

Main gap: arbitrary-center safety at 67/68 agreements. This intermediate
target can decide one larger retained PSD matrix at the fixed pairs.
Its downstream use is to exclude this prescription or retain one valid
PSD extension as an input for a later, separately assessed test. The
test is an exact energy comparison against the fixed new diagonal over
the complete interval. A strict minimum above the diagonal would stop
this invariant one-column extension; a certified passing parameter
would park this exclusion diagnostic. Any broader exclusion must also
justify averaging for the full PSD question, rather than inheriting a
kernel-only conclusion silently. No outcome is anticipated here.

Other columns, consistency between anchors, all scalar inequalities,
actual-label RS constraints, representing measures and common-center
realization remain unproved. A pass is not full hierarchy feasibility;
a failure is not a uniform bound over other pair/shell prescriptions.
Neither alone improves the 955–957 boundary. Full matching Mathlib
coverage and supporting coverage are not checked.

## Sources actually compared

Reused the ready nullspace-extension and critical-audit assessments,
foundations/09,10,12, and the canonical L056 and L059 proofs, including
L059's separate critical review. This avoids repeating the earlier
generalized-Schur, moment-hierarchy and Johnson searches. New queries:
`site.stanford.edu boyd convex optimization pdf quadratic programming 4.4`
and `Moore Penrose inverse Hermitian spectral decomposition reciprocal
nonzero eigenvalues lecture notes`. Secondary search results are not
imported. Directly inspected Sano's additional Lemma 2.7/proof; the
criterion and both proof directions remain covered by Theorem 2.6 and
Corollary 2.2. Exact primary source details, the sufficient author-slide
replacement for the inaccessible book PDF, and unread-lead qualifications
are in [foundations/10](../../foundations/10-psd-completion-source.md).

Sano's strongest relevant conclusion is an iff PSD criterion for finite
Hermitian blocks. It includes a real symmetric retained block and a
scalar new diagonal, with no nonsingularity or maximal-rank hypothesis.
Lemma 2.7's range-inverse construction covers the inverse action needed
for energy. Its closed-range hypothesis is automatic in finite dimension.
This is source applicability, not a proof of a compressed energy formula.

The inspected Boyd–Vandenberghe–Nobel slides give convex quadratic and
polyhedral-constraint formulations and the differentiable optimality
criterion. The future application uses a real scalar parameter on a
closed bounded interval, and must verify the actual objective's curvature.
Singular, linear or constant cases cannot be silently excluded. No
Slater condition, strict convexity, numerical optimizer, or reproof of
the general QP theory is required. The source supplies no interval-specific
minimum. Full matching Mathlib coverage is not checked.

## Approved specialization and proof obligations

The reused Johnson/product inputs are Brouwer–Cioaba–Ihringer–McGinnis,
arXiv:1709.09011v2, Sections 1.2,3,3.4, pp. 3,10,12, and
Brouwer–Haemers, *Spectra of Graphs*, author preprint, Sections 11.2,
1.4.7 and Theorem 2.7.1(i), pp. 162–163,19,36, as recorded in
[foundations/09](../../foundations/09-global-pair-johnson-source.md).
The finite real factors J(68,5), J(956,5) satisfy n>=2*5. Audited L056
already supplies their complete shell PSD signs and constant Schur
coordinate; critically verified L059 supplies all invariant eigenvectors
and their actual orbit weights. This is adequate coverage for a finite
inverse-energy specialization; it does not turn the weighted quotient
into an ordinary symmetric matrix.

Research must use the full orbit-size inner product, or equivalently
orthonormal orbit indicators, and verify the inverse action on the
positive modes and annihilation on the zero modes. An ordinary Euclidean
pseudoinverse of an unweighted quotient is not authorized. The norms of
the lifted invariant vectors carry their orbit sizes; unrelated full-mode
multiplicities cannot be inserted as a replacement. The positive constant
mode and separate anchor contribution must both be retained. Recover all
entries of L059's affine column and all required fixed data, rather than
use only its displayed endpoint witness or the sign table in L056.

Normalize by the unchanged positive rho, or keep rho everywhere, and
apply the same anchor congruence to the enlarged matrix and column.
L059's transported column is the established input, including its
constant subtraction. Pseudoinverses are not generally transported by
an arbitrary congruence as ordinary inverses would be. Research must
apply the known criterion to the transported block itself and justify
the scalar comparison with the original enlarged matrix. No new formula
for either energy is asserted in this source review.

The 36-orbit interval exhausts L059's invariant kernel-compatible
nonnegative columns. The next step may decide exactly this interval.
Any claim excluding the entire unlabeled one-column slice must additionally
verify averaging of the FULL enlarged PSD matrix under the four-region
stabilizer, retaining every fixed coefficient and diagonal. The applicable
known averaging input is Polak arXiv:1703.05171v1, Section 1.2, p. 3,
recorded in foundations/12. L059's kernel-only averaging conclusion must
not be silently promoted. No action on actual subgroup labels is imported.

## Duplicate/failure check and bounded decision

ATTEMPTS/038–040 concern shell-only, small reanchored and one four-index
pattern diagnostics. ATTEMPTS/041 and L059's critical review explicitly
leave energy untested. Their passing certificates are not energy evidence.
L054/L055's exclusions retain a different incidence-zero prescription.
Grone–Johnson–Sa–Wolkowicz's chordal-completion theorem and Dreyer v1
Theorem 5.2, compared in foundations/10, do not decide this constrained
column: unrestricted missing entries are a different hypothesis. No
duplicate energy verdict was found in these relevant local records;
no claim of novelty follows.

Approve exactly one REPRODUCTION calculation. It must save the complete
exact quadratic, interval endpoints, candidate minimizer/endpoint cases,
inverse-action residuals and actual-versus-required comparison to a local
certificate and canonical proof if a result is obtained. The optimizer
must be certified over the entire interval, including equality. A strict
minimum above the new diagonal excludes this interval; a certified
passing parameter gives only this retained one-column PSD extension.
A normalization, coverage or reconstruction failure requires preserving
unfinished reasoning and repairing that failure, not reporting exclusion.
No independent mathematical result is derived or approved as proved in
this literature turn. Other columns and the main boundary stay unresolved.
