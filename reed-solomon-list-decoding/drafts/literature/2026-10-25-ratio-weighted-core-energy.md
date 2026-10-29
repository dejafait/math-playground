# Ratio-sensitive core bound — completed source comparison

TARGET: Assess a ratio-sensitive finite spectral bound for the 61-point pair-intersection sum in L123, comparing its certified Bonferroni upper bound with 1600876449624.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded searches for weighted/one-sided expander mixing, finite circulant subset bounds, hypergraph codegrees and the exact field/count parameters; notebook-scoped duplicate and failure searches found the proposal and earlier different core/theta and Johnson tests, but no completed ratio-table spectral bound. Search failure is not novelty.
SOURCE_EVIDENCE: Inspected Brouwer–Haemers author preprint §2.4 p.33's complete Rayleigh expansion; Gray author PDF §3.1 pp.32–34 (3.5)–(3.13) and Theorem 3.1 pp.34–35; Hansen 2020-10-14 preprint §2.1 pp.3–4 and Lemma 3.1 (3),(5) pp.12–13 with its centered-indicator proof; NIST DLMF 4.21.2–3,16,21–22. Reused foundations/14's enclosing arithmetic and the endpoint assessment's Bonferroni coverage; read L123 fully and the relevant L122/C122a applicability passages.
COMPARISON: Standard finite circulant diagonalization and the symmetric Rayleigh bound cover the proposed method, including nonnegative scalar weights; they do not evaluate this ratio table or optimize Boolean cores. The one-sided largest eigenvalue on the constant-orthogonal subspace is the relevant quantity, rather than an assumed absolute spectral gap.
GAP: A later research step must justify the cyclic indexing, centered-indicator and unordered-pair normalizations, enclose every nonconstant spectral mode exactly, and compare the resulting Bonferroni certificate with 1600876449624. No such bound or improvement is established here.
REASON: Essential new source coverage is sufficient for one bounded known-method specialization; no generic spectral theorem needs reproof and no selected-family transfer is imported.
SCOPE: Source review of exactly TARGET; the separate calculation assessment below scopes the finite specialization. No numerical spectrum, new inequality, exact core maximum, selected-family theorem or RS safety is approved as a result of this review.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED and changed from endpoint enumeration/audit to a cyclic weighted core objective; ready Bonferroni and generic enclosing-arithmetic coverage were reused rather than re-reviewed.

## Retained initial proposal

Main gap: arbitrary-center 67/68 agreement safety. A stronger uniform
core-deletion diagnostic could inform later local-link work, but no
selected-family transfer or threshold saving follows from that alone.
The precise prospective quantity is the sum of d(a,b) over unordered
pairs in a 61-element subset K of the fixed order-1024 subgroup H of
F_65537. L123 provides d(a,b)=d(1,b/a), its entire integer table and
inverse symmetry. No transitivity on 61-element cores is assumed.

The proposed mechanism retains this ratio dependence, instead of using
the maximum independently for all pairs. Review finite weighted spectral
bounds on a cyclic group and any applicable exact arithmetic methods.
Do not assume that an eigenvalue computation is a certified bound, that
an extremizing real vector is a core, or that a core bound transfers to
selected supports. No eigenvalues, new inequality or improvement have
been derived in this proposal.

Continuation test: source coverage must justify a concrete bounded
calculation whose resulting survivor upper bound can be compared with
1600876449624. A value no better than that threshold rejects that test
as an improvement. A source requiring generic evaluation points,
unproved core uniformity or a selected-family transfer is inapplicable;
record that obstruction without rejecting the grand challenge.

Essential inputs: audited L123 and its complete counts/certificate;
L122 and audited C122a for the configuration space; the existing endpoint
assessment for Bonferroni; ATTEMPTS/010 and the 2026-10-06 core-conditioned
transfer review for preserved obstructions. No cross-notebook input.
Exact core maxima, selected-family supersaturation, threshold saving,
RS realization, 67/68 safety and ABF comparison remain unresolved.
Full matching Mathlib coverage for the proposed target is not checked.
The preceding text is the initial proposal, retained as context; the
completed comparison and bounded continuation are recorded below.

## Primary statements and essential proof cases

1. A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*,
   [author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
   §2.4, printed p.33, accessed 2026-10-25. Read the complete
   orthonormal-eigenvector expansion and its subspace Rayleigh bounds.
   They hold for finite real symmetric matrices, with repeated or zero
   eigenvalues permitted. These inspected statements suffice; the
   external proof reference for adjacent Theorem 2.4.1 is not imported.
   Coverage was already recorded in foundations/09 and the 2026-10-24
   actual-principal Rayleigh assessment; this read checks the changed
   constant-orthogonal application, without reopening the old root box.

2. Robert M. Gray, *Toeplitz and Circulant Matrices: A Review*,
   [98-page author PDF](https://ee.stanford.edu/~gray/toeplitz.pdf),
   accessed 2026-10-25; its acknowledgments identify 2005–2006 revisions.
   Read §3.1, printed pp.32–34, and Theorem 3.1, pp.34–35: every finite
   circulant is unitarily diagonalized by the Fourier vectors, and its
   eigenvalues are the DFT of its first row. The proof checks the cyclic
   wrap, every root of unity, orthogonality and completeness, not just
   guessed eigenvectors. No asymptotic Toeplitz conclusion is used.
   Match the first-row convention in (3.1) and (3.7) explicitly.

3. Jakob Hansen, *Expansion in Matrix-Weighted Graphs*,
   [author preprint dated 14 October 2020](https://www.jakobhansen.org/publications/mwgraphs.pdf),
   §2.1 pp.3–4 and Lemma 3.1 pp.12–13, accessed 2026-10-25.
   Nonnegative scalar weights are the k=1 case. Read (3), the centered
   decomposition, (5), vanishing cross terms and the indicator norm.
   These justify the weighted mixing framework, including S=T and
   overlapping sets; its edge sum is ordered. Use (5) with the independent
   Rayleigh input for a one-sided application. Do not import display (4):
   the retrieved text omits the degree factor there, although (5) has it;
   the subsequent operator-norm text is also unsafe as a one-sided bound.
   The failed second screenshot retrieval supplies no visual verification.
   No general matrix-weighted theorem beyond this scalar case is needed.

4. Reuse Siegfried M. Rump, *Verification methods: Rigorous results using
   floating-point arithmetic*, Acta Numerica 19 (2010), 287–449,
   DOI [10.1017/S096249291000005X](https://doi.org/10.1017/S096249291000005X),
   [corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
   §5.3–5.5, (5.14)–(5.17), author pp.27–28, already inspected in
   foundations/14. Enclosing expression evaluation permits signed sums
   and repeated variables but promises no sharpness. No Krawczyk or
   root-box theorem is needed for the new finite calculation.

5. NIST *Digital Library of Mathematical Functions*, live
   [§4.21](https://dlmf.nist.gov/4.21), accessed 2026-10-25:
   (4.21.2)–(4.21.3) give addition formulas, (4.21.16) the cosine-product
   identity, and (4.21.21)–(4.21.22) the half-angle square roots, with
   signs explicit. These supply standard identities for an optional
   rational enclosing evaluation at power-of-two angles. Branches,
   square-root endpoint certificates and every later arithmetic operation
   must be justified in the research step; a floating-point cosine call
   is not a certificate.

Bonferroni is reused without new browsing from
`2026-10-25-endpoint-pair-incidence-count.md`: *Probability inequalities*,
Section 15.1, Proposition 15.2, printed pp.196–197,
[UConn chapter](https://probability.oer.math.uconn.edu/wp-content/uploads/sites/2187/2020/08/ch15M.pdf).
The finite-event statement requires no independence. L123 already gives
the event model, singleton count and the complement direction. Its
complete numerical ratio certificate is an input, not re-certified here.

## Applicability and what remains to be done

The proposed matrix is the real weighted endpoint matrix on H, with
zero diagonal and off-diagonal entries d(a,b). L123 gives nonnegativity,
ratio dependence and inverse symmetry under exactly the fixed subgroup
hypotheses. L122 and audited C122a supply the configuration meaning;
the generator and all ratios must still be checked against the saved
artifact when choosing a cyclic ordering. No theorem requires generic
evaluation points, prime group order, connectedness or transitivity on
61-element subsets. In particular repeated nonconstant eigenvalues,
including any equal to the constant-mode eigenvalue, must be retained.

The later application must prove its centered-indicator identity, use
the largest eigenvalue on the constant-orthogonal subspace, and convert
the ordered quadratic sum to unordered endpoint pairs. Those are finite
specialization obligations, not inequalities derived in this literature
turn. It must preserve the antipodal ratio, the diagonal convention and
every nonprincipal Fourier mode. Replacing the largest algebraic
eigenvalue by a guessed absolute gap or dropping a repeated mode is
unjustified. A real extremizing vector need not represent a Boolean core.

A full interval certificate must save the exact input hashes, cyclic
row, all spectral enclosures, the certified uniform pair-sum and survivor
upper bounds, and the exact comparison. Rational square-root brackets
and rational interval operations avoid relying on an uncertified FFT.
All branches and accumulated error remain research obligations. There
is no source blocker for this finite test, but no numerical result yet.

## Duplicate and failure comparison

Read ATTEMPTS/010 and ATTEMPTS/019, the 2026-10-06 core-conditioned
determinant-transfer assessment, the endpoint assessment and L123's
audit scope. The antipodal configurations refute universal pattern
exclusion; the old unchanged pair/theta model has a feasible lift above
its required cap. Neither result evaluates this actual-label ratio-table
objective. Conversely a new core-deletion diagnostic would not repair
their selected-family or cardinality-transfer failures. The prior Johnson
and root-Rayleigh assessments concern different matrices and do not
supply this finite bound. Preserve their stops and unfinished L121 work.

Bounded queries: `Brouwer Haemers Spectra of graphs expander mixing lemma
symmetric matrix weighted circulant eigenvalues pdf`; `weighted expander
mixing lemma symmetric regular matrix eigenvalue upper bound induced
subgraph`; `"pair codegrees" "spectral" hypergraph induced subset upper
bound weighted`; `"multiplicative subgroup" "collinear" "sum" "product"
triples weighted spectral`; `"one-sided" "expander mixing" regular
weighted graph`; `"65537" "1024" "collinear" spectral core`;
`"67798380" "67331553840"`; `"weighted" "circulant" "subset" "Rayleigh"
bound`. No matching field-specific bound was identified. Search hits
about unweighted expansion, irregular/matrix mixing and subgroup energy
do not constitute inspected matching results. Becchetti et al.'s 2020
bounded-degree-expander paper was opened only at its introductory page;
its one-sided theorem/proof remains an unread lead and is not an input.
No novelty conclusion follows from the searches.

## Decision and continuation test

SPECIALIZE, with REPRODUCTION as the intended research classification:
import the standard spectral and enclosing-arithmetic inputs, and derive
only the finite application and its certificate. The bounded calculation
is specified in `2026-10-25-ratio-weighted-core-energy-calculation.md`.
It is a newly written ready continuation for separate approval next turn.

Continue this diagnostic only if its certified survivor upper bound is
strictly less than 1600876449624. If the tested certificate gives no
improvement, park that scalar spectral test; an interval straddle is
inconclusive, not a disproof. No core sharpness or grand-challenge verdict
follows in either case. Exact core maxima, selected-family transfer,
threshold saving, RS realization, 67/68 safety and the ABF comparison
remain open. Full matching Mathlib coverage for this application and
supporting circulant/Rayleigh/interval theorems was not checked in this
step; no absence is inferred. No lemma, script, DAG or PROOF argument
was changed.
