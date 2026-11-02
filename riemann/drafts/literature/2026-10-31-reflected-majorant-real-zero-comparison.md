# Reflected majorant versus a real-zero comparison kernel

TARGET: Assess whether reflected-majorant nonnegativity follows from a positive even Schwartz input kernel with Laguerre–Pólya Fourier transform, using F(x)=(1-x^2)^2 exp(-2x^2) as an independently testable comparison and retaining the full odd-harmonic tail.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed the exact-form, reflected-majorant, Laguerre–Pólya/periodization and signed sine-series searches recorded below; compared L233/L598 in full and the relevant local countermodel statements. No inspected result decides the reflected condition; this is not a novelty claim.
SOURCE_EVIDENCE: Inspected Csordas arXiv:1309.0055v2 Definition 1.1, (2.1), Definition 1.2 and Proposition 3.10/Remark 3.11; Knapp Basic Real Analysis, digital second edition (2016), VIII Propositions 8.1/8.2/8.10 and Theorems 8.4/8.15; exact locations and applicability below. Official Mathlib periodization support checked at a pinned source revision.
COMPARISON: Known results cover the first spectral sign for Laguerre–Pólya transforms and the tools for a full periodization calculation. They do not supply the pointwise reflected sign or the proposed comparison's inverse-kernel positivity. A fixed-pair analytic test is now source-covered in scope, with its calculation unperformed.
GAP: Verify the comparison hypotheses, derive the correctly normalized odd-harmonic representation from L598 and periodization, and bound the entire tail before deciding its sign. Actual-theta validity and all higher Xi signs remain unresolved.
REASON: The changed comparison has essential coverage for a bounded specialization, independently of the stopped actual-theta grid. No reproof of the imported Fourier or Laguerre theorems is needed; the missing work is their exact reflection/normalization and polynomial-Gaussian specialization.
SCOPE: Source comparison only in this turn. The separately nominated fixed-pair test requires the supervisor's separate approval before mathematics. No general Schwartz-to-admissible implication, Xi realization or RH conclusion is covered.
LITERATURE_REASON: The prior ready assessment concerned actual theta on a finite box; it did not cover this changed real-zero Schwartz comparison or the periodization interface.

## Gap and discriminator

The main gap is actual-Xi all-degree positivity at unbounded heights.
The intermediate question is whether the stronger pointwise reflected
condition can be inferred even for the proposed real-zero comparison.
Its downstream use is to decide whether a spectral-to-reflected shortcut
is justified before seeking a theta-specific bound. No such shortcut is
assumed. A negative comparison would stop only that generic implication;
one nonnegative pair would not establish the implication.

Use F(x)=integral_R k(u)exp(ixu)du and L233's A. Form G, S_h and D_h
exactly as in L598, whose full convergence/reflection proof was read.
Do not change full-line/half-line normalizations, replace algebraic
squares by modulus squares, or infer spatial positivity from real zeros.
L598 remains unaudited; this review does not promote its status.

## Primary source coverage

[Csordas, v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2),
printed pp.2–3, Definition 1.1 and (2.1), covers finite real-rooted
polynomials times exp(-a*z^2), a>=0, and their first Laguerre inequality.
Definition 1.2 additionally requires strict decrease and derivative decay
O(exp(-|t|^(2+epsilon))) for some epsilon>0. Gaussian decay alone does
not meet this condition: Theorems 3.5–3.7 cannot be applied merely from
the proposed Schwartz hypothesis. Use L233's direct identity instead.
Proposition 3.10 and the complete Remark 3.11 proof, pp.8–9, control an
integrated defect, not its pointwise reflection. Retain the previously
recorded missing factor x and restrict the divided inequality to x>0.
These statements were read at theorem/proof level; no matching reflected
obstruction was found there.

[Knapp, Basic Real Analysis, digital second edition (2016)](https://www.math.stonybrook.edu/~aknapp/download/b2-realanal-inside.pdf),
VIII, Proposition 8.1(f,g), p.413: moment integrability permits Fourier
differentiation; spatial differentiation needs an L1 derivative (or C1,
integrable derivative and vanishing at infinity). Proposition 8.2,
pp.416–417, supplies the Gaussian pair. Theorem 8.4, p.418, requires
both function and transform in L1. Proposition 8.10, p.423, supplies
Schwartz inversion. Theorem 8.15 and its complete proof, pp.427–428,
give periodization for Schwartz functions, with uniform convergence of
all differentiated spatial sums on bounded intervals. The convention is
exp(-2*pi*i*x*y). Rescaling, reflection, odd-mode selection, integration
constant and full-tail bounds remain specialization obligations. Apply
periodization to the verified Schwartz A, not automatically to a
half-line extension of G with a cusp or jump. PDF text was inspected;
screenshot retrieval was unsuccessful and no image-dependent claim is used.

No inspected source states that nonnegative Fourier coefficients make the relevant
sine primitive pointwise nonnegative. No exact inverse polynomial or
odd-harmonic expansion has been computed in this literature turn.

## Duplicate and failure check

Read L233's complete signed-transform proof and positive Gaussian-mixture
counterexample. That example has a negative first spectrum, so it does
not test the extra real-zero hypothesis. L055's statement/proof concerns
nonreal-zero positive kernels. L569's multiple-zero statement concerns
absolute compensation, not reflected periodization. A narrow search
also located L487's double-real-zero collision; its energy functional
is a different target, not an input here. No identical fixed reflected
comparison was located. These are comparisons, not dependencies.

The prior actual-theta bounded search and its stop are preserved in
ATTEMPTS/2026-10-31-associated-theta-reflected-majorant-bounded-test.md.
This nomination uses an exact real-zero comparison rather than reopening
its grid. The radial, contour and parity stops are not being retried.

Local searches used exact variants of the proposed F, reflected defect,
odd-harmonic, polynomial-Gaussian and multiple-real-zero terminology in
lemmas/, the associated-theta assessments and matching ATTEMPTS files.
Web queries included `"reflected majorant" Fourier`,
`"periodization" "Laguerre-Pólya"`,
`"(1-x^2)^2" "Fourier" Gaussian`,
`"Laguerre" "Pólya" "associated kernels" "positive definite"`,
`"Poisson summation" Schwartz periodization theorem Fourier series`,
and `"Laguerre" "sine series" "kernel" positive`.
Several broad queries returned irrelevant results; none is theorem
evidence. The exact-object search supplied no matching theorem. The
Csordas and Knapp primary statements above, not those failed searches,
provide the positive coverage. No uninspected lead is essential here.

## Bounded continuation and abandonment test

Nominate only h=pi/2, r=pi/4 for the proposed F. First verify a positive,
even Schwartz inverse kernel and Laguerre–Pólya applicability. Then
specialize L233 and Knapp to L598's exact D. Derive all constants and
justify reconstruction before testing the sign. Seek an analytic bound
on the absolute sum of the remaining odd-frequency terms smaller than
the magnitude of a signed finite part. Prove that comparison using exact
polynomial-Gaussian estimates; a numerical preview is insufficient.

A strictly negative D with a complete remainder bound would refute the
generic implication only. If the hypotheses fail, the representation is
inconsistent, or the fixed-pair full-tail test fails to decide a sign,
record the obstruction and stop this bounded attempt; no wider grid or
parameter change is preapproved. Success would still leave every
theta-specific sign and higher-degree gap independent.

The exact nominated action and assessment are in
2026-10-31-reflected-majorant-fixed-pair-test.md. No mathematical script
or lemma was written, and no new negative value is asserted.

## Mathlib

Supporting periodization is present as
`SchwartzMap.tsum_eq_tsum_fourier` and
`Real.fourierCoeff_tsum_comp_add` in the
[official source at a151a9c425dad802e4e1578282116f26004739b8](https://github.com/leanprover-community/mathlib4/blob/a151a9c425dad802e4e1578282116f26004739b8/Mathlib/Analysis/Fourier/PoissonSummation.lean).
The Schwartz theorem takes f in S(R,C) and real x and identifies the
periodized sum with its Fourier series. Source declaration inspected;
documentation prose still mentions older `fourierIntegral` names.
Full reflected-comparison and Laguerre–Pólya coverage is not checked;
supporting periodization is not a full matching theorem.
