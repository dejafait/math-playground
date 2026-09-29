# First associated theta kernel: arithmetic representation assessment

TARGET: Review whether two-dimensional Poisson summation or theta addition identities supply a positive-definite representation of A(t)=∫_R s²k(s+t)k(s−t)ds for the actual theta kernel k, retaining the polynomial weights and modular boundary terms.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the exact associated-kernel sign, theta addition with unequal parameters, and polynomial-weighted Poisson transforms on 2026-09-27; the inspected formulas cover transformations but no full-target positivity theorem was found. Queries and scope comparisons are recorded below.
SOURCE_EVIDENCE: DLMF 20.7.6–9, 21.2.1, 21.5.8 and 21.6.8; Roehrig, Siegel theta series for indefinite quadratic forms (2021), Definition 4.3 and Lemmas 4.4–4.5, pp. 20–22, https://doi.org/10.1007/s40993-021-00272-y; Borcherds, author-hosted corrected manuscript, Lemma 3.2 and Corollary 3.4, pp. 11–12, https://math.berkeley.edu/~reb/papers/aut/aut.pdf; Csordas, arXiv:1309.0055v2, Theorems 4.5–4.6 and Open Problem 4.7, pp. 11–12, https://arxiv.org/pdf/1309.0055v2.
COMPARISON: Common-parameter addition formulas are not directly formulas for k(s+t)k(s−t); the general polynomial-Gaussian transform retains lower-degree corrections but asserts no positive spectrum in t. The first associated-kernel sign is an open problem in the inspected Csordas version, as already recorded locally. Complete parity blocks give a specific larger regrouping to test beyond L254's two-index swaps.
GAP: Establish nonnegative Fourier spectrum for the full actual A, or a nonnegative main spectrum with an explicit compensating bound for every signed remainder, uniformly over all real frequencies; none of the inspected statements supplies this.
REASON: Import the standard transformation formulas by citation and specialize only their weights, cosets and integration to the actual kernel. A bounded parity-block sign test is specified and screened below; do not reprove Poisson summation, assume a positive-definiteness preservation rule, or repeat the generic countermodels. No specialization or new result is derived in this literature-only turn.

## Exact scope and discriminating test

Use the normalization of L233: the even actual-theta kernel k has
Fourier transform 2Ξ and the Fourier transform of A at 2x is
D_1(Ξ;x). The target is a representation supplying a sign, rather
than the already proved equivalence between that sign and positive
definiteness. A useful partial result could instead bound a residual
signed term at a stated scale; its required compensation threshold
must be explicit.

The [theta arithmetic audit](../../ATTEMPTS/2026-09-20-theta-logarithm-relevance-audit.md)
found no all-degree sign mechanism in the recorded identities.
L233's generic autocorrelation decomposition leaves a signed second
derivative. L234–L235 obstruct the tested finite approximations;
L254 leaves negative blocks in a second-level expansion. Repeating
those calculations or merely re-expressing the missing sign would
not justify continuation. These failures do not forbid a distinct
full-lattice identity at the first level.

The review compares primary statements about theta addition and
Poisson identities with these weights, domains and signs. Its
continuation condition was a concrete representation or remainder
test not already stopped; the complete parity-block test below
meets that condition as an investigation, not as an established
sign mechanism. No calculation for this target was performed in
the preceding turn or in this literature-only turn.

Even first-level success would leave the other low Laguerre signs
required by L320, exterior heights and the endpoint arithmetic margin
unresolved. No RH candidate or novelty claim is attached to this
assessment. PROGRESS.md is the sole current next-action record.

## Search and reading record

The shared rules, local goal, current checkpoint, whole overview,
DAG, existing diff, L019, L233–L235, L254 and the relevant prior
source screen were read. Existing unfinished work is preserved.
The earlier Csordas assessment is reused for its sign criterion;
the new work here concerns the proposed lattice identities.

Searches included:

- `Csordas associated kernels Riemann Xi first Laguerre inequality positive definite theta Poisson`
- `Riemann Xi Laguerre inequality theta addition formula two dimensional Poisson summation`
- `"Riemann" "associated kernel" "Poisson"`
- `"Laguerre" "theta addition"`
- `"theta" "unequal" "addition formula"`
- `"theta" "polynomial" "Poisson summation" "Hermite" weighted gaussian theorem`
- `Borcherds Automorphic forms singularities Grassmannians theorem 4.1 polynomial Fourier transform theta pdf`
- `"theta" "Poisson" "parity" "Laguerre"`
- `"associated" "theta kernel" "lattice"`
- `"Riemann" "first Laguerre" inequality 2025 2026`

The exact sign searches returned the already-screened associated-kernel
paper and adjacent kernel/coefficients results. The weighted search
located an explicit arbitrary-polynomial transform, which is closer to
the saved question than the unweighted Gaussian formula. The search for
the particular parity grouping yielded no matching sign theorem.
These are bounded search findings, not a claim of novelty or of an
exhaustive survey.

## Inspected statements and applicability

**Associated-kernel criterion.** George Csordas, *Fourier transforms of
positive definite kernels and the Riemann ξ-Function*,
[arXiv v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2#page=11).
Rechecked (4.1), Theorem 4.1, Theorems 4.5–4.6 and Open Problem 4.7
(pp. 10–12). Admissibility is proved; all-level positive definiteness
characterizes real zeros. The first sign is posed as a problem.
Use the notebook's existing k(u)=4Φ(u/2) and L233 normalization,
without importing a new constant from the source's transform formula.
The prior [nonasymptotic screen](../../ATTEMPTS/2026-09-21-theta-moment-literature-screen.md)
already records this scope. Its rediscovery is not new evidence,
and the dated open problem does not settle the literature's 2026 status.

**Addition identities.** Read the live NIST DLMF entries on
2026-09-27: [20.7.6–9](https://dlmf.nist.gov/20.7#ii) and
[21.6.8](https://dlmf.nist.gov/21.6#E8), including their parameter
conventions. The former relate products at shifted elliptic arguments
with a common nome and include subtractions. The latter gives a finite
sum over characteristics for two theta factors with the same Riemann
matrix. This identifies parity cosets as a standard regrouping device;
it does not assert positive definiteness of a weighted integral.
The general Riemann identity, 21.6.1–7, was also inspected; its rational
orthogonal matrix and common-period hypotheses must not be replaced by
an arbitrary real change of lattice.

The comparison with L019 is decisive for direct citation: s±t occurs
inside the Gaussian scale exp(2(s±t)), not as the additive elliptic
argument z of a theta function at one fixed nome. Thus a common-nome
addition formula cannot simply be substituted for this product.
This is a hypothesis comparison, not a proof that no addition-based
specialization can help.

**Multidimensional Gaussian transformation.** Read the definitions and
convergence conditions in [DLMF 21.2.1](https://dlmf.nist.gov/21.2#E1)
and the full inversion formula [21.5.8](https://dlmf.nist.gov/21.5#E8),
with the principal square-root convention. The Riemann matrix has
positive-definite imaginary part; inversion includes a determinant
factor and a quadratic exponential. This is an exact identity, not a
Fourier sign theorem for a function of the varying lattice parameter.
In the present application that parameter varies with s and t.
Positivity of its Gaussian quadratic form must not be confused with
positive definiteness of A as a translation kernel on R.

**Polynomial weights.** Christina Roehrig, *Siegel theta series for
indefinite quadratic forms*, Research in Number Theory 7, 45 (2021),
[version of record, 24 June 2021](https://doi.org/10.1007/s40993-021-00272-y).
Read Definition 4.3, §4.1, Lemmas 4.4–4.5 and the full proof of 4.5,
[PDF pp. 20–22](https://link.springer.com/content/pdf/10.1007/s40993-021-00272-y.pdf#page=20).
The arbitrary-polynomial Gaussian transform retains determinant
normalization and a finite Laplacian correction. No harmonicity or
nonnegativity is asserted. Parameters are fixed; the subsequent
unbounded integrals need separate justification. The update link
returned the same article; no separate correction was located there.

**Independent supporting formula.** Richard E. Borcherds,
*Automorphic forms with singularities on Grassmannians*, Inventiones
Mathematicae 132 (1998), 491–562; inspected the
[author-hosted manuscript](https://math.berkeley.edu/~reb/papers/aut/aut.pdf#page=11),
headed 29 September 1996, corrected 29 May 1997, with later annotations.
Read §3's convention, Lemma 3.2 and proof, Corollaries 3.3–3.4,
and §4's theta definition and Theorem 4.1 (manuscript pp. 11–14).
The polynomial transform retains its correction; the modular theorem
assumes an even lattice and homogeneous corrected weights, and gives
no spectral sign. Those hypotheses are not asserted for the unmodified
integrand. The sign erratum beside Lemma 5.1 concerns a later reduction,
which is not used here.

## Specific continuation and stop test

Three implementations were compared within the saved question:

1. Direct common-nome addition: the parameter mismatch above prevents
   a direct import. Replacing the polynomial weight by an unweighted
   theta square would change the target.
2. Bare simultaneous modular inversion: an identity alone leaves the
   signed spectrum unestimated. Repeating the existing reflection
   calculation is not a new sign mechanism.
3. Complete parity grouping with all correction terms: test the two
   infinite blocks n+m even and n+m odd in the actual first-associated
   sum. This is a specified larger grouping than L254's swap of a fixed
   pair at the second level. It is also different from L234's finite
   truncations and L235's modular averages of finite sums.

The third is selected for one bounded specialization. Its exact scope,
including the unchanged reflected summands of L254, is screened in the
[parity-block assessment](2026-09-27-first-associated-parity-blocks.md).
That record fixes the proposed blocks before any calculation; it does
not claim that a Poisson transform has already made them nonnegative.
No fresh positivity-preserving operation is assumed.

The discriminating threshold is nonnegative Fourier spectrum for both
complete blocks at every real frequency. If only a nonnegative main
spectrum P(x) and residual E(x) can be isolated, a useful sign certificate
must establish E(x)≥−P(x) at every x, including near zeros of P. An
unspecified small error, pointwise nonnegative spatial integrands, or
finite-frequency verification does not reach this threshold. A rigorous
negative block would stop the separate-block certificate, without
signing their total or disproving RH. A return to L233's same uncontrolled
spectrum with no new estimate also ends this implementation.

Existing actual bounds are unchanged: the notebook has all-level signs
on |x|≤10 and qualified finite-level exclusions through |x|≤40; it has
no global first sign. Even a successful first-level representation would
leave the other low indices in L320's logarithmic witness segment and
the separate endpoint margin unresolved. This review changes the next
test, not any achieved mathematical bound.

## Decision and access limits

The assessment is complete as SPECIALIZE: known transformations cover
the algebraic starting point, while the actual weighted, integrated
sign is the specified difference. Cite those starting formulas rather
than reprove them. No full-target theorem has been imported, reproduced
or proved here; neither originality nor an RH candidate is claimed.
This is EXPLORATION, the first of three consecutive unresolved exploration
turns after L355. The narrower test uses the same budget, not a reset.

The essential transformation statements are accessible and inspected.
Freitag's book, cited in Roehrig's proof, was not separately read;
Borcherds supplies an independently inspected proof of the polynomial
Gaussian formula. DLMF's Mumford/Dubrovin references were not opened;
the exact DLMF identities, not uninspected refinements, are compared.
An IISc Fourier-notes PDF returned an access error and is not used.
The Planat–Solé kernel-concavity lead remains only the abstract-scope
screen already saved locally, with no assertion about its proof or a
spectral consequence. A search-only recent half-plane Laguerre lead
was not adopted. None is an essential unread input to the selected test.

## Mathlib

Full-target and supporting theta-addition, polynomial-Gaussian,
Poisson and positive-definiteness coverage: **not checked**.
No Mathlib match or absence is asserted. The named analytical sources
above are supporting identities, not a match for the full sign statement.
