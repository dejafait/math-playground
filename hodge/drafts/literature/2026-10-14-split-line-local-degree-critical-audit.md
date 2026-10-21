# Split-line local degree — approved critical-audit source coverage

TARGET: Critically audit L103's finite local invariant classifying germ and generic-degree-at-most-two proof.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse drafts/literature/2026-10-14-split-line-local-classifying-degree.md for the unchanged actual slice, full ratio-C* action, finite-germ and multiplicity scope; compare L103 with audited L094/L101/L102 and the scoped failures ATTEMPTS/046,/061 and histories/261,/265,/274. No additional discovery or newly inspected external source is claimed.
SOURCE_EVIDENCE: Reused primary coverage: Buchdahl--Schumacher (2022) Corollary 4.9 with 4.6/4.8; 2008.04625v3 Definition 1/Theorems 1--3/6 and 2108.03255 Section 6 Theorem 1; Mond--Nuño-Ballesteros (2020) Appendix C Lemma C.1/Corollaries C.1/C.2 and Appendix D Theorems D.5/D.6/Lemma D.2; Huneke--Swanson (2006, February 2023 author revision) Theorem 11.2.7/Proposition 11.2.9(1)/Example 11.1.11. Direct primary URLs: https://d-nb.info/1262812674/34 ; https://arxiv.org/pdf/2008.04625v3 ; https://arxiv.org/pdf/2108.03255 ; https://link.springer.com/content/pdf/bbm:978-3-030-34440-5/1 ; https://www.math.purdue.edu/~iswanso/book/SwansonHuneke.pdf . Prior inspected appendix coverage is reused; current accessibility and focused rechecks are recorded below.
COMPARISON: These known tools cover L103's general analytic quotient, finiteness, generator and multiplicity inputs under their unchanged hypotheses; they do not certify its exact pullback ideal, actual image ring, simultaneous local assumptions or degree calculation.
GAP: A separate critical audit must check the complete invariant map, higher-term ideal equality, actual reduced image and ring inclusion, minimal-generator bound, multiplicity specialization, generic orbit interpretation and reduced-versus-weakly-normal scope without assuming smoothness or Cohen--Macaulayness.
REASON: The audit is within previously assessed source scope and needs no new theorem or discovery search; this separate literature approval repairs direct-source provenance and approves the unchanged target for a subsequent mathematical audit.
SCOPE: One fixed actual convergent L101 alpha with the prescribed jet and arbitrary higher coefficients, L102's stability ball and L094's unchanged S,I,g,h,k,E; reduced analytic GIT quotient only, with no F or quaternionic family assumed.

## Reuse and proposed discriminating test

The main gap remains universal primitive rational Hodge realization.
L103 supplies local identification control for the chosen complex family
only. This review proposes reuse of the existing complete source
assessment; it does not perform the future mathematical audit or add
an original result. Matching Mathlib coverage is not checked.

Check that the quotient uses the full effective ratio character and all
products P_iQ_j, and that the complete integrable slice gives the
analytic map in that quotient. Verify both inverse-function uses on
the actual convergent coefficients, not just their leading terms.
Verify that the coordinates generate the maximal ideal of the actual
reduced irreducible image, that the image extension is finite and
local of dimension two with residue field C, and that the generator
and multiplicity formulas apply to this very extension. Check the
special-fibre length/generic-degree distinction and the positivity
and integrality used to intersect the two degree bounds.

Preserve the bound only if those bridges survive; otherwise name and
repair or restrict the failed claim. In particular an ordinary reduced
analytic image cannot silently be replaced by its weak normalization
or an arbitrary algebraic coarse image. The finite generic orbit count
must follow from the actual family and the imported orbit comparison.
The audit may leave degree one versus two unresolved.

L094/L101/L102 and L103 are essential inputs; no nonempty global
reducible locus, W=r(TB), smooth central unitary gauge, quaternionic
family, common F, global mixed tensor, separation or transport is
assumed. All prior second-order, relative-Hom, tangent and curvature
stops remain intact. This assessment permits REPRODUCTION if approved;
it does not itself certify L103 or a Hodge-conjecture candidate.

## Separate source approval and recovery repair — 2026-10-14

LITERATURE_REASON: Supervisor recovery identified missing direct URLs in this ready assessment; repair provenance for the exact saved audit target, reusing adequate coverage rather than repeating discovery.

The earlier source assessment was read in full through its theorem comparison
and relevant discovery/failure notes. L103's imported-input paragraphs were
checked for citation agreement only; its mathematical argument was not audited.
ATTEMPTS/046 and /061 and histories/261, /265 and /274 were read narrowly:
they concern different global Hom, quadratic, tangent or curvature tests and
contain no replacement for this local degree audit. No new discovery search
or novelty claim is made.

Direct links and retained source scope:

- [Buchdahl--Schumacher, published 2022 PDF](https://d-nb.info/1262812674/34):
  Corollary 4.9, printed p. 91, was reopened with its complete short proof.
  It compares integrable slice-bundle isomorphism with the full reference
  automorphism orbit, referring to Corollaries 4.6 and 4.8(2). Those earlier
  proof cases remain covered by the prior assessment; smallness, the actual
  slice and reference polystability must be checked in the audit.
- [Analytic GIT, 2008.04625v3](https://arxiv.org/pdf/2008.04625v3):
  Theorem 6, printed p. 11, was reopened. It requires a polystable bundle
  on a compact Kähler manifold and its semi-universal parameter space;
  it supplies a closed reduced analytic quotient, not finiteness of the
  selected two-parameter map. Definition 1 and Theorems 1--3 and their
  proof cases remain reused coverage, without a fresh full reread.
- [Analytic GIT II, 2108.03255](https://arxiv.org/pdf/2108.03255):
  Section 6 Theorem 1, printed p. 16, and the category/extension proof
  outline were reopened. Coarse universality is in weakly normal spaces;
  it does not identify our ordinary reduced analytic image with its weak
  normalization or an algebraic Gieseker germ.
- [Mond--Nuño-Ballesteros, 2020 primary back matter](https://link.springer.com/content/pdf/bbm:978-3-030-34440-5/1):
  Appendix C pp. 491--492 and Appendix D pp. 522--527 retain precisely
  the previously inspected Nakayama, finite-germ, image and fraction-field
  degree coverage. Today's browser open returned Internal Error; no fresh
  appendix inspection is claimed. This transient retrieval failure does
  not erase the saved adequate assessment. Its smooth-target colength
  statements remain inapplicable to an arbitrary singular image.
- [Huneke--Swanson, author PDF](https://www.math.purdue.edu/~iswanso/book/SwansonHuneke.pdf):
  Theorem 11.2.7, printed p. 228, and its complete proof were reopened.
  The base is a local Noetherian domain, the extension a module-finite
  domain, and the ideal maximal-primary. The formula retains the residue
  degrees and the maximal ideals of full dimension; the proof uses
  generic rank and semilocal length decomposition. Proposition 11.2.9(1),
  p. 229, and regular-ring Example 11.1.11, p. 225, remain reused coverage.
  No Cohen--Macaulay image hypothesis is needed for this input.

DECISION remains SPECIALIZE: the imported general tools are adequately
covered, while the actual invariant ideal and image-ring applicability
remain the separate audit's mathematical work. No reproof is authorized
merely to reproduce the source theorems. Mathlib matching coverage is not
checked. This is a process repair with no new mathematical evidence:
L103 remains pending audit and all independent gaps remain open.
