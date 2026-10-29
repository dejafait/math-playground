# Ratio-weighted core energy — bounded calculation coverage

TARGET: Certify a one-sided cyclic spectral upper bound for L123's pair-intersection sum on every 61-point core and compare its Bonferroni survivor bound with 1600876449624.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed weighted-mixing, circulant, exact-parameter and duplicate/failure searches in 2026-10-25-ratio-weighted-core-energy.md; the target and fixed-field hypotheses are within that comparison. No inspected source supplied this table-specific numerical bound; no novelty claim follows.
SOURCE_EVIDENCE: Reuse the inspected primary statements: Brouwer–Haemers §2.4 p.33 https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf ; Gray §3.1 (3.5)–(3.13) pp.32–34 and Theorem 3.1 pp.34–35 https://ee.stanford.edu/~gray/toeplitz.pdf ; Hansen 2020-10-14 Lemma 3.1 (5) pp.12–13 https://www.jakobhansen.org/publications/mwgraphs.pdf ; NIST DLMF 4.21.2–3,16,21–22 https://dlmf.nist.gov/4.21 ; Rump §5.3–5.5 (5.14)–(5.17) author pp.27–28 https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf ; Bonferroni Proposition 15.2 printed pp.196–197 https://probability.oer.math.uconn.edu/wp-content/uploads/sites/2187/2020/08/ch15M.pdf . All six direct URLs reopened successfully on 2026-10-25; L123 remains the audited ratio-count input.
COMPARISON: Known finite diagonalization, centered-indicator and Rayleigh tools cover the method; the finite cyclic indexing, one-sided specialization, exact enclosures and numerical comparison remain to be supplied. This is a reproduction of known methods, not an assessed claim of new general mathematics.
GAP: Justify every normalization and every nonprincipal-mode enclosure, obtain one uniform unordered-pair bound, and perform the exact Bonferroni comparison; no spectrum, sign, core optimum or improvement has been computed or proved in this assessment.
REASON: Essential coverage is ready for this one independently testable calculation, with no essential source blocker. Direct-source-link recovery review completed on 2026-10-25; ready for the next research invocation within unchanged scope.
SCOPE: Exactly TARGET for L123's E=F_65537, order-1024 H, complete ordered-triple count and arbitrary 61-element K; one full finite spectral enclosure, with at most one preset precision retry for rounding width. No selected-support transfer, exact core optimization, new relaxation or RS safety is covered.

Main gap: arbitrary-center 67/68 agreement safety. The intermediate
target is a sharper uniform core-deletion diagnostic that retains the
audited ratio dependence. Its plausible downstream use is later local-link
work; selected-family supersaturation and threshold transfer remain
independent unsolved requirements.

Essential local inputs: L123 in full, L122's fixed subgroup/ratio setting,
audited C122a's configuration count, and
`scripts/finite-support/endpoint-pair-counts.txt`,
`scripts/finite-support/endpoint-pair-count.json`,
`scripts/finite-support/l123-critical-audit.json`.
Use the exact source citations, source qualifications and method comparison
in `2026-10-25-ratio-weighted-core-energy.md`; full matching Mathlib
coverage is not checked. No cross-notebook input.

The research step must check input hashes and the entire 1023-ratio table,
construct and verify the cyclic ordering, and prove that the zero-diagonal
endpoint matrix matches the finite circulant theorem. It must justify
constant row sum, inverse symmetry, the constant-orthogonal subspace,
the centered indicator's normalization and the factor converting the
ordered quadratic sum to unordered pairs. Retain every nonconstant mode,
including the real antipodal mode and repeated eigenvalues. Do not assume
that all cores are equivalent or that a real maximizing vector is a core.

Use the largest algebraic eigenvalue on the constant-orthogonal subspace
for the one-sided Rayleigh application. Do not use Hansen's problematic
display (4); the reviewed centered identity (5) and independent Rayleigh
expansion suffice. Cite the generic results without reproof. The finite
specialization and implementation are the work to be done.

One allowed certification mechanism is rational enclosing arithmetic,
with positive-branch half-angle identities and the cosine-product identity
from the inspected DLMF formulas. Certify square-root endpoints by exact
inequalities and all subsequent operations by enclosing rational bounds.
Explain branch choices, cyclic residues and accumulated error. A suitable
fixed budget is 128 binary fractional bits with one 256-bit retry only
if rounding prevents the threshold comparison; justify actual error,
rather than presuming these precisions sufficient. An alternative exact
algebraic evaluation must remain within the same imported finite method.

Save a complete certificate under scripts/finite-support/ with all input
hashes, cyclic weights, spectral enclosures, completeness checks, rational
pair-sum bound, survivor bound, threshold and failures. Print only summary,
actual/required bounds and artifact paths. Inspect the complete evidence
needed for the mathematical claim; a preview or numerical FFT is not
verification. No enumeration rerun is needed unless input linkage fails.

Continuation test: a certified survivor upper bound strictly below
1600876449624 supports retaining this diagnostic. Otherwise park the
tested scalar spectral certificate as an improvement attempt. A rounding
straddle after the preset retry is inconclusive; failure of an upper
certificate does not prove that no stronger bound exists. Any finite
improvement still leaves exact core maxima, selected-family transfer,
threshold saving, RS realization, 67/68 safety and ABF equivalence open.
Preserve ATTEMPTS/010 and /019 and the 2026-10-06 transfer obstructions,
as well as unfinished L121/root work. No mathematical specialization was
derived or approved as a completed result during either source-review turn.


## Direct-source-link recovery review (2026-10-25)

The parent assessment's completed comparison and duplicate/failure checks
are reused; no changed target or fresh discovery search is needed.
The six primary URLs now appear directly in SOURCE_EVIDENCE rather than
only in the parent assessment. All six were reopened successfully. Gray's
Theorem 3.1 and its finite unitary-diagonalization passage were checked
again for link-to-statement correspondence; the prior primary reads and
qualifications for the other sources are reused, not claimed as new reads.
In particular, Hansen display (4) remains excluded, the one-sided input
remains the symmetric Rayleigh expansion, and no asymptotic theorem,
independence assumption or core transitivity is imported. Rump's nonlinear
root theorem is unnecessary; only enclosing arithmetic is covered.

This repairs source traceability and separately reviews the saved ready
continuation. It establishes no new mathematical input, numerical bound,
or discovery beyond the sources checked. SPECIALIZE remains justified
for exactly TARGET, with REPRODUCTION intended for the ensuing calculation.
The main gap, intermediate target, downstream use and strict continuation
test above are unchanged. Full matching Mathlib coverage remains unchecked.
