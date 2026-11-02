# L644 fixed-reserve consequence — completed source comparison

TARGET: Assess the exact finite-Hermitian implication from audited L644 to failure of a uniform fixed margin ||C^(-1/2) K C^(-1/2)/ell_X-I||<=1-epsilon, using only L641's checked Gram and zero-pair identities and retaining all zero orders.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready L644 audit, simultaneous-selection and constrained-trace assessments; checked the exact local conditional diagnostic and both vertical-Pick failure records. New bounded searches for finite Hermitian Rayleigh/trace/operator-norm statements and the exact L644/fixed-margin terminology located the primary linear-algebra sources below, but no external actual-Xi consequence. No exhaustive search or novelty claim.
SOURCE_EVIDENCE: MIT 18.701, The Spectral Theorem for Hermitian Matrices, 15 November 2010, p.1 theorem, complete induction proof and real-eigenvalue corollary; Mark W. Meckes, Lecture notes on matrix analysis, 27 April 2019, Lemma 1.5/Definition 1.7 p.5, Theorem 3.1 and complete proof p.20, Section 4.4 induced-norm definition/Proposition 4.17 and following Euclidean formula p.38. Author PDF metadata matched the accessible nLab mirror. Exact links and source limitations below. Mathlib Spectrum eigenvector-basis statements inspected as supporting coverage only.
COMPARISON: These sources cover finite complex Hermitian diagonalization, trace invariance, Rayleigh bounds and the Euclidean induced norm without positivity or simple eigenvalues. L642 already states the conditional average-Rayleigh construction; audited L644 supplies its simultaneous prerequisite. The sources do not state the resulting actual-Xi margin obstruction; checking that precise application and its quantifiers remains mathematics.
GAP: In a later mathematical turn, specialize the existing conditional diagnostic through L641's antilinear rational-coordinate bijection and full Gram normalization, then test the single-epsilon/eventual-all-heights norm-margin claim. Do not substitute an eigenvalue near zero in absolute value, negative eigenvalue, invariant interpolation subspace or positive paired measure.
REASON: Essential changed-target source comparison is complete. SPECIALIZE licenses one bounded standard-tool application, classified REPRODUCTION, on the unchanged TARGET; it does not certify the consequence. No essential source is blocked and no new analytic premise or reproof is justified.
SCOPE: Exact L641 C,K,ell_X and grid N=floor(log T), actual Xi zeros of every order, L642 full Hermitian form/conditional diagnostic and audited L644 positive-measure conclusion. Finite spectral, trace, Cauchy--Schwarz and induced Euclidean norm tools only; no L640 arithmetic, RH, simplicity, effective onset or spectral-sign assumption.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED changed the target from auditing selection to its finite-Hermitian diagnostic consequence; the essential missing theorem comparison is completed here while count, density, projection and zero-expansion coverage is reused.

## Main gap, target and discriminating test

Actual-Xi initial signs at unbounded heights and all-degree mixed
positivity remain unresolved. The intermediate target is exactly TARGET.
Its downstream use is to decide whether to close the proposed eventual
fixed positive norm reserve and redirect work toward an actual signed
mechanism. Even a successful obstruction would concern that budget;
positivity of K and RH would remain separate questions.

The later attempt must decide the exact hypothesis with one epsilon>0,
one eventual onset, every sufficiently large T and every X in [T,2T].
It may use only the selected positive-measure S_T in L644; it must not
upgrade L644 to a conclusion at every height. Continue if the standard
finite tools apply through the stated coordinates and settle this precise
uniform-margin test. Abandon or repair this implication if it requires
positivity, an invariant U_X, a small absolute eigenvalue, a changed zero
sum, or a new analytic estimate. This review derives no such consequence.

## Primary statements actually inspected

1. MIT 18.701 (Michael Artin's Fall 2010 course),
   [*The Spectral Theorem for Hermitian Matrices*, 15 November 2010](https://ocw.mit.edu/courses/18-701-algebra-i-fall-2010/2622987fba1e172b289fc78934b8404d_MIT18_701F10_spthm.pdf),
   p.1, unnumbered theorem and real-eigenvalue corollary. For a complex
   Hermitian matrix it supplies unitary diagonalization. Read the entire
   proof: normalized eigenvector, orthogonal complement, zero off-diagonal
   block by Hermitian symmetry, induction on dimension; then the real
   diagonal/eigenvalue corollary. It imposes neither definiteness nor
   simple spectrum. PDF p.2 contains the course attribution.

2. Mark W. Meckes, *Lecture notes on matrix analysis*, 27 April 2019,
   [author-hosted PDF](https://case.edu/artsci/math/mwmeckes/matrix-analysis.pdf),
   [accessible copy of the authored notes](https://ncatlab.org/nlab/files/MeckesMatrixAnalysis.pdf).
   The initial author PDF title/date/contents loaded, but subsequent
   theorem fetches timed out; local curl also failed DNS. The mirror's
   title/date/page count match that loaded record. The mirror is the
   authored primary document, not an nLab theorem paraphrase.
   Inspected Lemma 1.5 and Definition 1.7 (printed p.5): similarity
   preserves trace and defines an operator's trace independently of basis.
   Inspected Theorem 3.1 (p.20) and its entire spectral-coordinate proof:
   Rayleigh quotients of finite complex Hermitian matrices lie between
   the extremal eigenvalues, with both extrema attained. The proof uses
   squared moduli in orthonormal eigenvector coordinates; it does not
   require a definite form. Inspected Section 4.4 (p.38), induced-norm
   definition, Proposition 4.17, and the following Euclidean/singular-value
   formula. The relevant norm is the induced Euclidean norm, not the
   entrywise norm or the Frobenius norm. Cauchy--Schwarz is a standard
   named input. Corollary 3.2's displayed quotient is garbled or misprinted
   in the accessible text; do not import it. Theorem 3.1 and the MIT theorem
   suffice for the proposed application. No reproof of these inputs is
   warranted; no theorem from the unread remainder is being imported.

## Applicability and qualifications to preserve

Read L641's hypotheses/conclusion and norm/zero-pair proof through its
full-Gram check; L642's projection/trace statements, full-tail interchange
and conditional diagnostic; and L644's simultaneous conclusion and
coordinate check. Reuse the completed L644 audit and its saved source
coverage, rather than reopening Suzuki, Bellotti--Wong, Baluyot or Penrose.
No new density exponent, concentration space, zero array or constraint
is proposed. Those imported manuscripts remain unaudited as recorded.

L641's map v -> h_v is antilinear and bijective, with its stated norm
and quadratic-value identities. The full positive-definite C supplies
the coefficient norm. In the later specialization do not call this map
complex-linear unitary, assert unproved matrix similarity, or require
U_X to be invariant under conjugation or the ambient operator. L642's
compression is a finite Hermitian form in its own inherited orthonormal
coordinates; its scalar Rayleigh statement is the approved interface.
Writing that interface correctly is the remaining applicability work,
not a reason to reprove the known spectral theorem.

Keep s_j=2+i(X+j/N), C_jk=1/(3+i(j-k)/N),
K_jk=(F(s_j)+conjugate(F(s_k)))C_jk, ell_X=log(X/(2pi)), F=xi'/xi.
Only these L640 definitions are used. L641's checked norm/zero-pair
identities and L642's absolutely convergent complete mixed sum remain
essential. Both ordinate signs, both horizontal displacements, every
zero order, dependent value rows and both annulus boundaries survive.
No derivative constraints, tail truncation, positive paired measure,
small absolute eigenvalue, negative eigenvalue or effective onset is
part of the approved consequence. The selected trace is signed.

## Duplicate and failure comparison

L642's final conditional paragraph is the existing local source for the
average-Rayleigh construction. A later proof should cite and specialize
it, not introduce that construction as a new discovery. L644 is the
existing simultaneous dimension/full-trace input; do not derive it again.

Read [the boundary-only transfer stop](../../ATTEMPTS/2026-11-01-vertical-pick-boundary-paired-transfer-stop.md)
and [the deterministic annulus stop](../../ATTEMPTS/2026-11-01-vertical-pick-constrained-trace-annulus-inconclusive.md).
The former uses unconstrained test pairs, not asserted actual zeros;
the latter records failure of an upper-bound envelope, not a trace lower
bound. Neither duplicates the exact proposed application of L644's
selected-height conclusion. The arithmetic route stops also remain.

New queries: `Hermitian matrix Rayleigh quotient trace minimum maximum
spectral theorem lecture notes operator norm pdf`; `"L644" "vertical Pick"
"fixed margin"`; `Elizabeth Meckes lecture notes matrix analysis pdf
case.edu 2019`; and the scoped Mathlib spectral-basis query. The authored
notes identify Mark W. Meckes, correcting the search's author guess.
Search snippets were leads only. The Cornell 2026 norm page timed out and
is unused. General search results, uninspected texts, and surrounding
Meckes theorems are not imports. No stronger actual-Xi theorem or novelty
conclusion is inferred from this bounded search.

## Mathlib and completion

Inspected [Mathlib.Analysis.InnerProductSpace.Spectrum](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Spectrum.html),
`LinearMap.IsSymmetric.eigenvectorBasis`,
`LinearMap.IsSymmetric.apply_eigenvectorBasis`, and
`LinearMap.IsSymmetric.eigenvectorBasis_apply_self_apply`.
Their finite-dimensional real/complex inner-product-space hypotheses
supply supporting diagonalization, including repeated eigenvalues.
Full matching coverage for the Xi specialization is unchecked; no Lean
verification or assertion of absence is made.

Outcome of this literature step: source coverage ready (SPECIALIZE),
with the exact application still unproved. No lemma, mathematical script,
DAG or PROOF is changed. The original nomination's mathematical target,
limitations and stop evidence are retained; its REVIEW_REQUIRED status
is superseded by this separate comparison. A justified new creative sign
mechanism is still missing. Complete this finite diagnostic application
before selecting one; do not rename the specialization creative.
