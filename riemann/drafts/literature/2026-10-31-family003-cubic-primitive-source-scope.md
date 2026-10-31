# Cubic primitive source applicability — source comparison complete

TARGET: Assess whether Heath-Brown's Theorem 2 in Kummer's conjecture for cubic Gauss sums supports L542 (2) for arbitrary complex coefficients on ideal-squarefree primary rows and columns, including primes above 2, conjugate-prime pairs, units and transpose/conjugation orientation.
CHECKED: 2026-10-31
DECISION: IMPORT
SEARCH_EVIDENCE: Searched Heath Brown Kummer conjecture cubic Gauss sums Theorem 2 pdf 2000 cubic large sieve; Heath-Brown Theorem 2 cubic large sieve squarefree erratum; cubic large sieve rational squarefree Heath-Brown. Searched family003 assessments/history and ATTEMPTS for the cited theorem and cubic primitive; only retained premises and recorded access failures matched this target, not a completed import.
SOURCE_EVIDENCE: Read Heath-Brown's author-uploaded 26-page manuscript, Theorem 2 pp. 3–4, Section 4 pp. 15–16 including Lemma 4 and its orientation paragraph, Section 5 Lemma 7 proof pp. 19–20, Section 6 primitive-character hypotheses p. 20 and the CRT/reciprocity conclusion p. 22; compare L542 (2) and the previously inspected pinned eq:cubic-large-sieve 7036–7053.
COMPARISON: The primary theorem has exactly the retained length charge and arbitrary complex coefficients; squarefreeness is in Z[omega], with congruence 1 modulo 3, rather than squarefreeness of the rational norm. No extra rational-prime or prime-above-2 exclusion appears. Its orientation paragraph covers duality, reciprocity and symbol inversion.
GAP: No stronger cubic estimate is needed; the remaining local work is a canonical import with the retained primary-ideal parametrization, zero and unit conventions and orientation checked explicitly. This turn does not discharge L542 (2) in a lemma or certify the source's full analytic proof.
REASON: Primary access is now resolved and the source scope matches the proposed primitive; importing it can remove one retained hypothesis from L542 without providing reflection/global closure or Xi signs.
LITERATURE_REASON: Heath-Brown's original Theorem 2 is an essential unread source explicitly excluded from the previous conditional hybrid audit; its ideal-squarefree versus rational-support hypotheses must be checked before specialization.
SCOPE: Theorem-level comparison for L542 (2), with all its supports preserved, using the primary conventions already retained in L544. No reproof, nonsquarefree extension, arbitrary two-index mask, reflection/global audit or Xi-sign claim.

The primary source is D. R. Heath-Brown, *Kummer's conjecture for cubic
Gauss sums*, Israel J. Math. 120A (2000), 97–124, Theorem 2,
[DOI](https://doi.org/10.1007/s11856-000-1273-y).
The inspected version is the undated, 26-page
[author-uploaded manuscript](https://www.researchgate.net/profile/Roger-Heath-Brown/publication/254847691_Kummer%27s_conjecture_for_cubic_Gauss_sums/links/54db67950cf2ba88a6901164/Kummers-conjecture-for-cubic-Gauss-sums.pdf),
printed pp. 3–4 for the theorem; the hosting page attributes the upload
to the author on 11 February 2015. Publication metadata was compared
with the [Oxford record](https://ora.ox.ac.uk/objects/uuid%3A16c3966e-61cb-499d-839c-559b3794fcff).
The typeset journal version was not inspected; manuscript page numbers
are used throughout. Oxford and CiteSeer PDF endpoints returned 403;
the author PDF succeeded after correcting the host's malformed download
link. A local curl DNS failure did not block the primary web read.

## Exact theorem and essential source cases

Theorem 2 gives, for every epsilon>0 and arbitrary complex c_n,

\[
 \sum_{N(m)\le M}^{*}
   \left|\sum_{N(n)\le N}^{*}c_n(n/m)_3\right|^2
 \ll_\epsilon (MN)^\epsilon
       \{M+N+(MN)^{2/3}\}\sum_n^{*}|c_n|^2.
\]

Both stars restrict to squarefree elements congruent to 1 modulo 3.
For the finite target, coefficients outside the column cutoff are zero.
Section 4 repeats these supports in defining B_1. Lemma 4's following
paragraph invokes duality/cubic reciprocity and permits symbol inversion.
The Lemma 7 proof sorts arbitrary common element divisors and removes
the resulting coprimality condition by Moebius inversion. Section 6
requires squarefree, mutually coprime n_1,n_2 prime to 3 for its primitive
character; it adds no rational-support condition. Its proof concludes
with CRT and reciprocity. These are source statements, not a reproof.

The web extraction renders Lemma 4's displayed symmetry as a tautology;
no argument here relies on that corrupted display. Its explanatory
paragraph and the directly oriented Theorem 2 suffice for this scope
comparison. One page-image request timed out; extracted primary text
of the required passages was available. No unseen page image is evidence.

## Comparison with the local contract

The main gap is actual-Xi all-degree positivity. The intermediate target
is precisely L542 (2); the proposed downstream use is to discharge its
cubic premise alongside L543/L544's conditional quadratic input. This
does not resolve any sign or realization requirement.

The source support does not silently narrow L542's two stars. The local
translation uses the PID/unique primary-generator conventions retained
in L544 Hypotheses, not its quadratic-sieve conclusion. In particular
the future import must not substitute rational norm squarefreeness,
remove allowed primes above 2 or remove conjugate-prime pairs. Unit
ideals and bounded or empty norm ranges must be checked explicitly
under the stated residue-symbol conventions. The primary theorem has
upper cutoffs, so no new dyadic theorem or length loss is proposed.

The bounded continuation test is an exact match of this parametrization,
coefficient norm, collision zeros and orientation with L542 (2).
Continue by citation/application only; narrow or park if an additional
support condition, unit-dependent phase outside the covered orientation,
or an extra length loss is required. No new cubic derivation is approved.

Searches also returned quartic-sieve restatements, Baier–Young's cubic
Dirichlet-family application and Dunn–Radziwill's sharpness work. These
are unread leads, not theorem evidence used here. The primary match
already supplies the requested charge, so no broader source survey or
novelty assertion is justified. The previously recorded access stop is
preserved above and resolved for this particular primary input. No local
matching import or failed mathematical specialization was found.

No lemma, DAG row, mathematical script or proof overview is changed in
this literature turn. Mathlib coverage is not checked. No cross-notebook
input is used. A separate application assessment records the next target.

## Earlier nomination (preserved)

The pinned source is OpenAI, *The Quasi-Riemann Hypothesis*, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`eq:cubic-large-sieve`, lines 7036–7053. The nomination was to reuse the inspected pinned
formulation from the prior hybrid-mask assessment; distinguish that
statement from the unread original theorem. Read the primary theorem's
hypotheses before broader passages and inspect only the proof cases
needed for the support and orientation comparison.

The exact needed charge is (UV)^epsilon{U+V+(UV)^(2/3)} times
sum |z_v|^2, for U,V>=1. The stars in L542 (2) mean ideal
squarefreeness and allow both primes over a split rational prime in an
index, as well as primary factors over 2. Primary indices avoid lambda;
no additional rational-norm-squarefree restriction is present. Units,
zeros at shared prime ideals, coefficient normalization and conjugation
must also match. These are questions to assess, not conclusions about
what Heath-Brown's theorem says.

Continue to a separately approved application only if the primary
theorem and relevant proof cases cover this interface, or identify an
explicit limited specialization needing proof. Narrow or park the
application on an essential excluded support or unattained length
charge; do not silently strengthen the theorem. Existing L542 remains
conditional. L543/L544 concern only its quadratic side and cannot prove
the cubic input. Retained reciprocity, reflection, global closure and
actual-Xi all-degree positivity remain independent. Mathlib coverage is
not checked. No cross-notebook input is proposed.
