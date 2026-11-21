# Exact arithmetic theta bracket: two-coefficient diagnostic

TARGET: Compute the q and q^2 coefficients of the order-two Rankin-Cohen self-bracket of theta(q)=sum_(n in Z) q^(n^2), with weights (1/2,1/2) and Wang's binomial normalization, and decide whether they already exclude coefficientwise nonnegativity under either global orientation.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step20 searched exact Rankin-Cohen/theta/xi, self-bracket, coefficient-sign and stronger cusp-sign terminology; checked local bracket/transvectant duplicates and reused completed modular-scale, partition, Levy and variation-diminution comparisons. See the completed post-partition discovery assessment; no originality claim.
SOURCE_EVIDENCE: Wei Wang arXiv:2406.14254v1 (20June2024), Section1 bracket definition printed p2, primary HTML/PDF inspected; DLMF20.2.3 and Section20.2(ii) supply the theta series and analytic domain. The exact convention is below. No modularity, Shimura or cusp-sign theorem is needed or imported for this finite test.
COMPARISON: This is exact specialization of a known signed differential operation to the primitive actual theta series through two coefficients. It is not H_1/H_2 certification, a logarithmic Newton expansion, common Favard realization or scalar modular inversion. A general cusp-sign-change lead is unread; no novelty or actual sign claim relies on it.
GAP: Neither coefficient has been evaluated. A pass leaves global coefficient signs, pointwise signs, the interface to L019's kernel and L025/L030's transform-logarithm, and all-degree extension open. Failure stops only this coefficientwise sufficient mechanism.
REASON: Primary definitions adequately cover a bounded exact diagnostic after separate approval. No broader sign theorem, new mechanism or cutoff extension is approved.
SCOPE: One exact calculation, coefficients q and q^2 only, retaining the constant theta term and specified normalization. REPRODUCTION. No transcendental evaluator or new script is necessary. No bracket expansion or coefficient was derived in preparing this assessment.

This continuation was written during a literature-only discovery step.
It requires separate next-turn approval; preparation is not a completed
mathematical attempt.

## Source convention

Wang, [*Shimura lift of Rankin-Cohen brackets of eigenforms and theta
series*, arXiv:2406.14254v1](https://arxiv.org/pdf/2406.14254v1),
Section1, p2, defines for smooth functions and integer or half-integer
weights k,l:

    [f,g]_w = (2 pi i)^(-w) sum_(j=0)^w (-1)^j
      binom(k+w-1,w-j) binom(l+w-1,j) f^(j) g^(w-j).

Derivatives are in the upper-half-plane variable. The test must explain
the normalized derivative in q coordinates and retain this binomial
normalization, rather than silently substitute the gamma/factorial
convention of another source.

[DLMF20.2.3](https://dlmf.nist.gov/20.2#E3) gives the theta_3 series;
Section20.2(ii) specifies analyticity for |q|<1. Here theta is the
series sum q^(n^2), q=exp(2 pi i tau). Match it explicitly to L019's
primitive theta law, distinguishing DLMF's exp(pi i tau) convention.
It is not the differentiated kernel K.

A definition needs no theorem proof for this application. Cohen's
modularity theorem, Wang's Shimura theorems and the unread
Knopp-Kohnen-Pribitkin sign-change lead are not mathematical inputs.
The finite calculation is not claimed to go beyond known literature.

## Purpose and stopping rule

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The proposed diagnostic tests a possible arithmetic sign source.
A coefficientwise signed theta differential expression could be one
ingredient of a later representation. An independently justified
interface to the logarithm of the transform would still be needed.

Compute both exact coefficients and report actual values against the
required nonnegative coefficient threshold under each global
orientation. Opposite strict signs park this coefficientwise mechanism
immediately. Do not extend the cutoff or create a lemma merely to
record a short algebraic specialization; preserve the exact reasoning
in a suitable draft/attempt artifact. A pass gives only the two tested
signs and no automatic technical continuation. Failure says nothing
against pointwise bracket positivity, other representations or RH.

Essential local input is L019's primitive theta normalization.
L021/L024/L025 and L030/C032a describe the downstream gap and must not
supply assumed positivity. L033/L796 and the September20 audit are
contrasts, not premises. No certified moments, external certificates,
cross-notebook input or additional source access is required. Full
matching Mathlib coverage is unchecked.

This is calculation/specialization, not proof_attempt/creative. The
unpaid transform-logarithm interface blocks that stronger routing;
scheduling pressure does not change the mathematical classification.
