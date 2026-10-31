# Cubic matrix interface — source record

2026-10-31. Literature comparison only. Main gap: actual-Xi all-degree
positivity. Intermediate target: L542's retained symbol identification,
restricted to the nominated source setting. Downstream use: the conditional
hybrid norm. No sign estimate or mathematical discharge is claimed.

## Primary statements and reused coverage

OpenAI, *The Quasi-Riemann Hypothesis*, 30 September 2026,
[pinned TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a: inspected 519–591,
7036–7084 and the complete hybrid proof 7085–7194. Relevant locators
are the Euler definition, eq:cubic-large-sieve, lem:hybrid-energy and
eq:hybrid-after-quadratic-reduction. The fixed datum excludes primes
above 6. Negative powers preserve collision zeros. The cubic sieve
allows squarefree primary indices, arbitrary complex coefficients and
fixed supports. In its application j may retain S-primes other than
lambda; h,t,D,r are frozen before the coefficient vector is used.
These are inspected source claims, not a new proof of their application.

Dunn–Radziwill, *Bias in cubic Gauss sums: Patterson's conjecture*,
[arXiv:2109.07463v3, 14 May 2024, Section 1.2](https://arxiv.org/html/2109.07463v3#S1.SS2):
read the primary-generator convention, prime cubic Euler definition,
denominator multiplicativity and reciprocity (1.4). These identify the
ordinary Euler convention. No GRH-conditional prime-average result is
used. L548 (A2) is the existing local all-residue comparison; its proof
need not be reproduced.

Reuse the [cubic primitive comparison](../literature/2026-10-31-family003-cubic-primitive-source-scope.md)
and [import assessment](../literature/2026-10-31-family003-cubic-primitive-import.md).
They record Heath-Brown, *Kummer's conjecture for cubic Gauss sums*,
Israel J. Math. 120A (2000), 97–124, Theorem 2,
[DOI](https://doi.org/10.1007/s11856-000-1273-y), author manuscript
pp. 3–4, Section 4 pp. 15–16, Lemma 7 pp. 19–20 and Section 6
pp. 20–22. L545's full proof was read for this comparison. Its existing
ideal parametrization and complex-matrix operations cover the norm
interface. The original analytic proof remains imported.

## Scope and remaining application

L542 initially requires only lambda in S; L548 (A2) and this review
cover good denominators away from both 2 and 3. A future discharge
must explicitly specialize L542 to S containing all primes above 6,
not silently assert its wider initial domain. This qualification was
already in the nominated target.

The remaining finite test compares the matrix with rows j and columns
P' against the operations allowed by L545, checking exponent -2,
collisions and either norm-one index. Numerator S-primes must remain:
L548 (A2) concerns all numerator residue classes. Use only its finite
subsection, without importing unrelated theta/DR analytic hypotheses.
The entrywise application proof belongs to the next research step;
no such derivation is performed here.

No stronger sieve charge, new reciprocity law or arbitrary joint phase
is authorized. Stop/narrow on an unmatched entry, phase or denominator
domain. The quadratic input, upstream proofs, global closure and Xi
transfer remain unresolved. Full matching Mathlib coverage is not
checked; supporting Gauss-sum theorems do not supply this interface.

## Search, overlap and failures

Local reads covered hybrid source/working notes, cubic primitive
history, composite-normalization history and relevant L548 critical
working notes. Identification/phase searches in family003 histories,
corresponding literature files and 2026-10-31 ATTEMPTS found no completed
exact L542 discharge. L545's norm import and L548's finite comparison
are already complete and should be reused. Earlier access failures
remain in the reused assessments and were resolved for that import;
there is no present essential source blocker.

External queries: `"sextic" "cubic" "residue symbol" square Eisenstein large sieve`
and `"Heath-Brown" "cubic large sieve" conjugate primary squarefree`.
Results included *Metaplectic cusp forms and the large sieve*,
*Vanishing of quartic and sextic twists of L-functions*, and newer
two-mark/cubic-moment manuscripts. These were not inspected or used
as theorem evidence; their changed scopes are unnecessary here.
Primary/local coverage suffices. No novelty claim, cross-notebook input
or new actual-Xi creative mechanism is asserted.
