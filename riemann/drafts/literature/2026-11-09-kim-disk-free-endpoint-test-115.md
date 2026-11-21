# Bounded Jensen-disk endpoint test

TARGET: Test whether evenness, reality, genus at most one, f(0)>0 and zeros in |Im z|<1/2 guarantee arbitrarily large real points outside J(f), using a rescaled trigonometric-polynomial family and a complete zero-and-disk certificate.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Prepared during step115's boundary-hypothesis comparison; searched Jensen disks real axis cos and Jensen disks cover strip entire, plus exact endpoint/coverage terminology locally. Found L052/L057 as related prefactor families, not an exact disk-coverage result. No novelty inference and no mathematical attempt yet.
SOURCE_EVIDENCE: Kim Proc.AMS124(1996),819–830, definitions pp819–820, Theorem1 p821, complete Section2 pp822–823 and Example2 p829 inspected through published PDF mirror. NIST DLMF1.2.8, released15September2026, 4.14.1–3 and entire-function/complex-zero/periodicity paragraph inspected. L052's full elementary prefactor-zero proof and L057's exact scope read locally.
COMPARISON: Kim assumes endpoints outside closed Jensen disks; neither his Theorem1 nor the inspected periodic example asserts they follow from the listed generic hypotheses. L052 already solves a related trigonometric zero equation, but its parameters and conclusion do not certify complete real-axis disk coverage. This target reuses that algebra and changes only the independently tested geometric property.
GAP: Complete zero set, multiplicities, genus/growth and disk-union geometry for a parameter choice have not been verified. No implication for the actual theta kernel, actual-Xi endpoints, critical counts or mixed signs is covered by a generic model.
REASON: Test the newly exposed necessary applicability premise before spending work on conditional count lemmas or unsupported global zero-loss transfer. Existing elementary formulas suffice for this bounded mathematical test; no further literature retrieval is essential under the same hypotheses.
SCOPE: Real even nonconstant entire trigonometric polynomials after real rescaling and positive normalization. Genus<=1, strict strip and f(0)>0 must all be certified. J(f) means Kim's closed conjugate-zero disks. Do not require a theta representation, matching zeta zero density, a kernel-shape condition, RH, or finitely many nonreal zeros. This assessment is newly prepared and requires separate next-turn approval.

## Relevance and one bounded discriminator

Main gap: L030–L032/C032a actual-Xi all-degree algebraic-square mixed
positivity. Kim's known first-derivative count interface can reveal
sign-sensitive loss only under its endpoint premise. Determining whether
the generic facts already pay that premise is a useful filter for the
interface, independent of the still-missing critical-zero estimates.

Use one real trigonometric-polynomial family with a frequency and a
real constant as parameters; reuse L052's exponential-quadratic method
for its complete complex zero set. Verify all hypotheses before making
any disk claim. This is an elementary symbolic calculation/model test,
not a creative RH mechanism and not a numerical scan. No candidate
parameter choice or coverage assertion has been established this turn.

Decisive negative certificate: one qualifying f for which J(f) contains
the entire real line, or contains both real tails. A verified unbounded
complement theorem for the stated full class would justify continuing
the generic implication. If the family does neither, record the test
as inconclusive and reassess; do not claim that a search failure proves
endpoint existence. Do not broaden into a kernel-shape/Hankel audit.

Downstream use: a countermodel parks the shortcut from strip/order/
symmetry to arbitrarily large admissible Kim rectangles. It leaves an
actual-Xi-specific endpoint mechanism possible. A positive generic
result would supply an actual applicability input, still leaving
critical-zero bounds, global transfer and all mixed signs open.

## Ready inputs and qualifications

[Kim published PDF](https://scispace.com/pdf/critical-points-of-real-entire-functions-and-a-conjecture-of-3sul01urof.pdf),
DOI10.1090/S0002-9939-96-03083-3, supplies the exact disk definition and
the role of the endpoint premise. Example2, p829, is the primary
trigonometric-polynomial class comparison, not a matching coverage
theorem. The completed detailed assessment is
`2026-11-09-xi-first-derivative-critical-count-scope-114.md`.

[NIST DLMF4.14](https://dlmf.nist.gov/4.14), formulas4.14.1–3,
specifies sine/cosine by complex exponentials and records entirety,
complex zeros and periodicity. These elementary identities support a
complete zero computation without graphs or an original special-function
theorem. The use of a scaled/shifted constant polynomial must be checked
explicitly; no derived zeros are imported from a search snippet.

L052 supplies the existing exponential-quadratic root calculation for
its own parameters; any generalization used must be written out locally.
L057 explains why finite-Hankel masking is a different assertion. Neither
result establishes the new coverage property. L018/L023/L024 motivate
the generic assumptions from actual Xi, but are not inputs certifying a
new model. L030/L032/C032a describe relevance only.

Reproduction/specialization is the expected classification if the test
succeeds. The search did not certify originality. No reproof of Kim is
justified. Full matching Mathlib coverage is unchecked/unknown; no
cross-notebook theorem, source blocker, numerical certificate, mathematical
script or new lemma is introduced here. The next mathematical task is
calculation/standard/high, after separate approval of this new assessment.
