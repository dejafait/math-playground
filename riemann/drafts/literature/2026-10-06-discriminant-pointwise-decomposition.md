# Pointwise discriminant decomposition — bounded source assessment

TARGET: Determine whether L367's discriminant admits a zero-safe pointwise Wronskian decomposition with controlled envelope-curvature terms.
CHECKED: 2026-10-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact/stronger-result searches and targeted local duplicate checks completed; primary determinant/Wronskian definitions and a polynomial comparison were inspected, with no matching full discriminant theorem found.
SOURCE_EVIDENCE: DLMF 1.3.1–1.3.2, 1.3.7–1.3.8, 1.13.1 and 1.13.4–1.13.5; Hägg–Shapiro–Shapiro (2023), p. 7 equation (2.2) and Remark 7; local L358 (3), L367 (1)–(3), L368 (8)–(10), L369 (4)–(7).
COMPARISON: Standard algebra covers finite determinant tools and existing inputs control envelope curvature, but neither the inspected identities nor the polynomial comparison gives this actual-function discriminant decomposition or residual sign.
GAP: Establish the exact polynomial decomposition at zeros, track the common-envelope transformation and bound its curvature contribution in retained real jets; signed arithmetic residual and total L367 margin remain independent gaps.
REASON: Approve one finite pointwise test independent of the parked sharp-moment source; reproduce elementary algebra as needed to check normalization and curvature without claiming originality or positivity.
SCOPE: Real C² function pairs with a positive C² common envelope, specialized to L367 ordinary jets on |ξ|≥40; no means, regulator differentiation, division by F_0/G, real-zero premise or common ODE is covered.

The main gap is global actual-theta mixed positivity. Essential inputs are
L367's P_j,V_j and positive A,T,L, L358's envelope and L369's actual
reflection/carrier; L368 is available for its eventual C margin. Preserve
ordinary real-frequency derivatives and all envelope derivatives. No
regulator curve, prime-phase replacement, zero hypothesis or division by
F_0/G is allowed. No cross-notebook input is proposed.

A pointwise decomposition could identify a square contribution and the
precise residual obstruction before a later mean or sign test. Continue
only if an exact identity valid at zeros and quantified curvature terms
is established at the eventual research stage; otherwise record the
specific algebraic or bound failure. An identity by itself does not sign
the discriminant or theta. Total margin, higher mixed signs, heights above
forty and endpoint arithmetic margin remain unresolved. Full matching
Mathlib coverage is not checked. This assessment approves the bounded test, not a decomposition or sign conclusion.


## Sources and applicability

Online DLMF pages were inspected on 2026-10-06 in their displayed form;
an exact release number was not recorded. [§1.3(i)](https://dlmf.nist.gov/1.3#i),
equations 1.3.1–1.3.2, gives finite determinant expansions; 1.3.7 gives
multiplicativity. These polynomial tools require no nonzero function
value. Equation 1.3.8 bounds the absolute determinant for real entries,
not the sign of our discriminant. It cannot replace computing a residual.

[DLMF 1.13.4](https://dlmf.nist.gov/1.13.E4) defines the Wronskian
as f g′−g f′, usable for differentiable real functions at zeros.
[Abel identity 1.13.5](https://dlmf.nist.gov/1.13.E5) concerns solutions
of the same second-order equation 1.13.1 with analytic coefficients on
a simply connected domain. No such common equation for F_0 and G is
an input here; no exponential/nonvanishing conclusion is approved.

Christian Hägg, Boris Shapiro and Michael Shapiro,
*Introducing isodynamic points for binary forms and their ratios*,
Complex Analysis and its Synergies **9**, article 2 (2023),
[published author PDF](https://staff.math.su.se/shapiro/Articles/DiscPolar.pdf),
[DOI](https://doi.org/10.1007/s40627-022-00112-4), was inspected at the
introduction, p. 3 Theorem 1, and p. 7 equation (2.2)/Remark 7.
The latter uses U_P=zP′−dP, V_P=P′ and reports a Wronskian
(d−1)(P′)²−dPP″. This degree-dependent single-polynomial expression
is not our arbitrary real-function pencil discriminant. Theorem 1
concerns Möbius equivariance of an isodynamic map on degree-d binary
forms with roots of multiplicity at most two, not positivity of our
functions. References [4] and [9] are unread leads, not inspected
sign theorems. No import from this paper is required for the finite test.

Reuse L369 (6)–(7): q=(log A)″=O(t⁻²) and the exact polarized
common-envelope identity. L368's response envelope is A|b|; its
curvature must not replace q. Supporting primary formulas were checked:
[DLMF 5.15.8](https://dlmf.nist.gov/5.15.E8) expands polygamma in
|arg z|≤π−η, η>0; [§5.11(ii)](https://dlmf.nist.gov/5.11#ii)
controls complex digamma remainders by sector factors times neglected
terms. The arguments 1/4+it/2 remain in a closed admissible sector.
Use L369's separately controlled derivative expansion, without
differentiating a bare error. No sharper q estimate is essential to
begin the finite test; retain the actual jets multiplying it.

## Search and duplicate comparison

Queries used: `site:dlmf.nist.gov determinants Sylvester identity 1.3`,
`"Laguerre" "Wronskian" "discriminant" inequality`,
`"f" "g" "Wronskian" "Laguerre" inequalities quadratic`,
`"Laguerre inequality" "pencil" discriminant`,
`"f" "g" "Laguerre" "discriminant" Wronskian identity`, and
`site:dlmf.nist.gov "Wronskian" "definition" 1.13`.
Several hits concern Laguerre polynomials rather than differential
inequalities. Snippets and unread Sylvester-identity leads are not
inputs. Failure to find an exact match is not evidence of novelty.

Scoped local inspection covered L367's coefficients/product proof,
L369's carriers and common-envelope identity, L368's curvature expansion,
L358 (3), L359's projected-square certificate, L316's gamma cancellation
and stated germ obstruction, and the discriminant source-review drafts
and relevant October histories. L367 contains no full discriminant
decomposition. L358/L369 already supply the scalar/polarized identities.
L359 completes a different regulated projection square with beta
subtraction. L316 warns that small gamma curvature does not by itself
sign an arithmetic differential form. No duplicate full decomposition
was found in these inputs. The sharp-mean source blocker and L365 stop
remain recorded; neither forbids this independent finite test.

## Approved attempt and decision test

The research step may expand the discriminant in L367's six real jets
and express it using polynomial 2-by-2 minors/Wronskians of F_0,G.
It may apply existing envelope identities with f=F_0/A and g=G/A,
retaining every q contribution. The polynomial identity must hold for
arbitrary real jets, including zeros. Only A,T,L are allowed positive
divisors. Ordinary real-frequency derivatives are required; the T²
response normalization is pointwise, not constant under differentiation.

Seek an exact zero-safe decomposition and a quantified absolute
curvature bound in retained jets using the existing q estimate.
If successful, isolate the signed arithmetic residual still requiring
control; an indefinite exact identity is not a positivity certificate.
If useful residual separation or curvature comparison requires an
unproved lower bound, record the failure and stop this certificate.
A later mean, new sign mechanism or stronger residual theorem requires
its own assessment. No derivation, new lemma or mathematical script
was made in this literature-only turn. Full matching Mathlib coverage
is not checked; determinant support is not a match for the full result.
