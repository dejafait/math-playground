# First-factor Atiyah image in the actual point quotient — source coverage ready

TARGET: Determine L116's actual finite-point projection of L174's first-factor Atiyah image by comparison with the split-fibre Atiyah contraction.
CHECKED: 2026-10-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 585 screened the three saved Gram/KS/point-bracket assessments, relevant L111/L116/L164/L165/L174 passages and ATTEMPTS/092–095; searched Atiyah pullback, direct sums, line Chern classes and edge restriction, then inspected primary passages below. No matching completed local point-projection result was found; no novelty claim.
SOURCE_EVIDENCE: Kuhn, Forum Math. Sigma 12 (2024), e100, Lemma 4.2, Lemma 4.4/Claim 4.5, Corollary 4.7, Example 4.10 and Corollary 5.10; BF math/9912245v1, Remark 3.17 and Section 4 opening, printed pp.27–28; live Stacks 0B91, 0H99 and 08J5; reuse L164's actual top-fibre comparison and saved BF contraction coverage, with source scope below.
COMPARISON: The sources cover derived restriction of Atiyah classes, coefficient functoriality, determinant trace and the line Chern convention. L164 already compares the same actual a with top fibre cohomology independently of its bracket input. None evaluates A mathfrak a_1 or locates L174's residual image; that family-specific specialization remains mathematical work.
GAP: In a later research step compare first-factor contraction with restriction, apply split-fibre functoriality while retaining both line Chern classes and the trace-free diagonal coefficient, then pass through L164's actual top comparison. No essential source gap remains for this bounded test; its formula and consequences remain unproved.
REASON: This separate literature turn approves the unchanged TARGET for one bounded specialization of known identities. Import the general results; justify only the actual-family map, coefficient and normalization comparisons. No new mathematics, lemma or mathematical script is supplied here.
SCOPE: The unchanged hypothetical rank-two equality family on identical marked K3 factors, fixed actual connection/forms/ch, actual j,r,a,Q, finite reduced possibly empty Z and unknown s,t; no other-factor Leray splitting, ordinary middle-base-change isomorphism, section integrability or F existence.
LITERATURE_REASON: The target has changed from the two-factor Gram rank to its actual finite-point projection; the essential new operation is the comparison of first-factor Atiyah contraction with the top-fibre edge map at split points.

## Invocation-start scope and test, retained

The main gap remains primitive realization and existence of F. The
bounded intermediate target is the composite A mathfrak a_1 from
H^1(S_1,T_S1) to U=H^0(B,W), with A and mathfrak a_1 exactly as in
L116/L165 and L174. Determining it could locate the independent
residual detector relative to the normal and point obstruction
components. No formula, rank, vanishing or square-count consequence
for this composite is asserted here.

Essential local results to retain are L071,L094,L108,L109,L111,L116,
L165,L173,L174, including their split line-bundle and trace conventions.
The intended source comparison should reuse the precise pullback and
Atiyah/KS coverage recorded in
`2026-10-26-split-ks-extended-tangent-comparison.md`, and top-fibre
comparison coverage in
`2026-10-25-adjoint-point-obstruction-projection.md`, only where their
hypotheses and maps actually match. These are leads for comparison,
not an assertion that they already approve the new target. No
cross-notebook input is proposed. Full matching Mathlib coverage
has not been checked.

For a later approved mathematical step, the continuation test is an
actual edge-map identity at every reduced split point, with the
trace-free diagonal coefficient and its first Chern class retained.
An explicit map or a proved failure of the comparison is useful
evidence. Numerical dimensions, generic-fibre calculations or arbitrary
point functionals do not meet that test. Empty Z must be included.
If the actual comparison remains unevaluable, park this projection
test instead of repeating the now-completed Gram audit. The existing
stops in ATTEMPTS/092–095 remain; none settles this different linear
projection target. No mathematics for this target was derived here.

## Completed source comparison — step 585

2026-10-27. LITERATURE / EXPLORATION / REPRODUCTION; actual task
literature_comparison. The ready decision above supersedes the proposed
gate. This is source-coverage progress, with no mathematical advance
beyond the sources and no evaluation of the target composite.

### Primary coverage and applicability

1. Nikolas Kuhn, *The Atiyah class on algebraic stacks*, Forum Math.
   Sigma **12** (2024), e100,
   [published article](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/atiyah-class-on-algebraic-stacks/92C44757D4DCF43E4B6F368DDC5179EC),
   Construction 4.1, Lemma 4.2, Lemma 4.4/Claim 4.5, Corollary 4.7,
   Example 4.10 and Corollary 5.10. Lemma 4.2 supplies functoriality
   in the coefficient; Corollary 4.7 supplies derived pullback with
   the induced cotangent map for a 2-commutative square and
   E in D^{<=0}_qcoh. No simple-fibre hypothesis occurs. Read the
   principal-parts/flat-representative/K-flat-cone proof case, reusing
   the saved published pp.32–35 coverage. The determinant identity
   applies to finite locally free resolutions; read its vector-bundle
   case and induction proof. F and each split line meet this scope.
   These inputs license later checks of split inclusions/projections
   and trace subtraction; they do not evaluate the contraction.

   The DOI resolver and HTML diagram-image links failed. The
   [arXiv v1, Corollary 4.7, printed p.32](https://arxiv.org/pdf/2306.13934#page=32)
   supplied the complete derived-pullback square in extracted PDF text;
   it has the same theorem number. Do not transfer published page
   numbers to this 52-page preprint. No essential access blocker remains.

2. Buchweitz–Flenner, *A Semiregularity Map for Modules and Applications
   to Deformations*,
   [math/9912245v1, Remark 3.17 and Section 4 opening, printed pp.27–28](https://arxiv.org/pdf/math/9912245v1#page=27).
   Read the principal-parts convention, the Euler-sequence sign check
   and the usual Chern-character identification for vector bundles on
   complex manifolds: their convention is ch=Tr exp(-At).
   The degree-one normalization is available for line bundles;
   it must be matched to L174's fixed first-order convention, not
   silently copied with a new sign or a missing curvature scalar.
   Reuse Definition 4.1, Proposition 4.2 and Corollary 4.3 from the
   ready Gram assessment for contraction/trace. Neither injectivity
   nor a vanishing theorem is supplied for the present composite.

3. [Stacks Lemma 36.30.4(1), 0B91](https://stacks.math.columbia.edu/tag/0B91):
   proper finite presentation, flat f and perfect coefficient give
   perfect pushforward commuting with arbitrary base change. Read
   both alternatives and the reduction to 36.30.1. The smooth
   projective product projection and locally free V satisfy (1).
   [Lemma 20.31.8, 0H99](https://stacks.math.columbia.edu/tag/0H99)
   gives cup compatibility with the complete ringed-space base-change
   square; its proof is omitted in the source. Reuse the inspected
   composition/counit coverage in the saved point-bracket assessment.
   Evaluation of cotangent against tangent is a coefficient morphism
   within this scope. [Remark 13.12.4, 08J5](https://stacks.math.columbia.edu/tag/08J5)
   supplies the canonical truncation, with its short-exact-sequence
   and quasi-isomorphism construction. No ordinary R^1 base-change
   isomorphism or multiplicative splitting is imported.

4. Local reuse, not a new derivation: L164, Proof, “Actual
   ordinary-to-derived maps” and “Restriction of the projected global
   bracket”, identifies the top comparison for the very same C,a,W
   and fibre square. The first passage precedes specialization to a
   bracket input. It retains the lower Tor terms and distinguishes
   W(z) from the derived middle space. This already established
   comparison can be applied to another degree-two input; its
   application to mathfrak a_1 remains the later task. L111 supplies
   the actual split fibre L plus L^{-1}, k=c_1(L), k^2=-14,
   h.k=0 and reduced length-one W. L165 fixes A=H^2(a).
   L174 defines the input with Atiyah-first cup order. These exact
   maps and conventions, including possible empty Z, must be retained.

The primary target was also rechecked against Deligne, *The Hodge
Conjecture*, [Clay-hosted statement, Section 1, p.2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2):
rational cycle combinations on projective nonsingular complex varieties.
This source review changes neither that target nor its status.

### Search scope, comparison and next mathematical test

External queries actually run included `"Kuhn" "The Atiyah class on
algebraic stacks" "additivity"`, `"Atiyah class" "direct sums"
"line bundle" "first Chern"`, `"Atiyah" "edge map" "K3"
restriction family`, `"Nikolas Kuhn" "Atiyah" arxiv 2023 pdf`, and
`"Atiyah class" "line bundle" "c_1" Buchweitz Flenner`.
Search snippets and secondary discussions were discovery leads only.
Primary retrieval focused on the numbered statements above. A guessed
Stacks tag 0B94 resolved to the unrelated Hilbert scheme of points;
it is not an input. No matching explicit family-specific projection
theorem was identified, and this bounded screen makes no novelty claim.

The saved Gram assessment covers a different pairing; the KS assessment
covers the other cotangent component. They cannot supply the answer.
The stronger generality of the cited naturality theorem does cover
nonsimple split fibres. The saved point-bracket assessment and L164
cover the actual top edge but do not determine the new input's value.
ATTEMPTS/092 leaves section quadrics unknown, /093 concerns unrestricted
scalar-isotropic lifts, /094 global bracket cyclicity and /095 an
unavailable metric comparison. None evaluates this linear projection.
Their stopping evidence remains unchanged.

Next perform exactly TARGET as RESEARCH / REPRODUCTION: import the
general identities, verify the actual edge/restriction square, then
specialize to the split summands with trace-free coefficients and both
line Chern classes retained. This is why a local specialization rather
than a reproof is needed. An explicit actual-map formula or a proved
failure of the comparison is decisive. If required data remain
unevaluable, park this projection test. No rank equality, vanishing,
square-count improvement or exclusion is approved as a premise. Normal
placement, actual brackets, F existence, transport and primitive
realization remain independent gaps. Full matching Mathlib coverage
is not checked; no absence claim is made. No cross-notebook input,
mathematical script, new lemma, DAG edit or argument change was made.
