# Finite spectral-span intersection: completed audit coverage review

TARGET: Critically audit L907's proof that ker L intersects H_finite trivially, including the complex integral, finite invariance and Fourier hypotheses.
CHECKED: 2026-11-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step147 read and reused the step145 exact-identifier, finite-domain, independence, resolvent and ODE search record in 2026-11-08-hedenmalm-spectral-span-kernel-review.md; checked L906/L907 and the exact Hedenmalm ATTEMPTS stops; reopened the primary Hedenmalm v1 HTML, Tao statements/inversion argument and Mathlib characteristic-polynomial hypotheses. No fresh discovery query or novelty claim.
SOURCE_EVIDENCE: Reused inspected inputs: Hedenmalm arXiv:2606.17494v1 https://arxiv.org/pdf/2606.17494v1 pp5-7, (3.3.2), Theorem3.3.1 kernel proof, Theorem3.3.3 and Section4.2; Cayley-Hamilton and LinearMap.aeval_self_charpoly https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Charpoly/Basic.html#LinearMap.aeval_self_charpoly; Tao, 245C Notes2 (6 April 2009), Exercise30/Remark31, Definition32, Exercise38 and inversion(11) https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/; audited L906 endpoint estimates.
COMPARISON: This audit uses precisely the hypotheses and techniques covered before step146; it checks the new local specialization rather than extending it or claiming an imported full intersection theorem. Eigenvector independence still cannot justify an unconstructed inverse.
GAP: L907's finite-span proof has not received independent critical review; check the complex lower-end integral, kernel reduction, conditional invariance, all Schwartz seminorms, exact Fourier multiplier and continuity at polynomial roots.
REASON: Step147 completes the separate literature approval for the unchanged audit target. Existing SPECIALIZE coverage suffices; next turn should audit L907, without further literature absent a changed essential hypothesis. This review does not certify the proof.
LITERATURE_REASON: The supervisor explicitly required a separate literature-only approval of the newly saved step146 continuation; this turn checks its source coverage and does not extend it.
SCOPE: Only L907's stated finite span and its L906/algebra/Fourier inputs; no closure, generalized eigenfunctions, Mellin normalization, positive form, symmetry or mixed-positivity transfer.
COVERED_TARGET: Critically audit L907's proof that ker L intersects H_finite trivially, including the complex integral, finite invariance and Fourier hypotheses.

## Reused coverage and bounded test

The [prior source comparison](2026-11-08-hedenmalm-spectral-span-kernel-review.md)
records the actual primary passages read and the known-results and local
failure searches. Its scope covers the mathematics in L907 exactly.
No changed analytical hypothesis or unread essential source has been
introduced, and this nomination is not an additional literature turn.
The standard Fourier theorem is used on the ordinary logarithmic real
variable, not as a Mellin-to-Xi identity.

The audit should check whether a nonzero kernel vector really forces
w into one finite D-invariant space, without assuming independence or
the existence of L inverse. Verify that Cayley-Hamilton applies to a
genuine endomorphism and yields a nonzero polynomial. Check all complex
integral signs, both logarithmic endpoints, the 2pi Fourier factor and
why a continuous transform supported on the finite root set vanishes.
The estimates must apply to every derivative, not just w and Dw.

Essential local inputs are L906 and L907. Retain all complex zeros and
allow repeated labels, but do not adjoin parameter derivatives. No RH
or simplicity premise is permitted. A passing audit confirms only the
kernel intersection; a failure must identify a precise unpaid
hypothesis or faulty deduction. Do not silently change the domain or
promote the result to a positive spectral realization. The enlarged V
stop and the missing positive-metric/symmetry stop remain intact.

Mathlib coverage is unchanged: the two supporting characteristic-
polynomial results are documented in L907; full intersection coverage
and supporting Fourier/Schwartz coverage remain unchecked. The
independent audit, not a program replay, is the required next check.


## Separate coverage approval, 8 November 2026 (step147)

The exact TARGET is retained and DECISION remains SPECIALIZE. This
is a completed source-scope check, not an independent proof audit or
an additional mathematical advance. The inherited search assessment
is adequate for the unchanged hypotheses. No new lemma is derived.
The nominated-audit text above is preserved as the step146 record;
its pending-acceptance language is superseded by this approval.

Primary passages reopened for this review:

- Hedenmalm v1 [HTML](https://arxiv.org/html/2606.17494v1),
  (3.3.2), kernel reduction in the proof of Theorem 3.3.1,
  Theorem 3.3.3 and Section 4.2 (PDF pp5-7 in the reused assessment).
  The complex statement uses weighted endpoint conditions, retains
  the displayed integral, and omits its proof details. The finite
  span includes possible nonreal zeros. These passages neither
  assert finite-span injectivity nor construct a positive symmetric
  form. The local audit therefore remains necessary; it need not
  audit the full boundary-value characterization or Mellin identity.
- Tao [Notes 2](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/),
  Exercise 30/Remark 31, Definition 32, Exercise 38 and (11), including
  the Gaussian inversion argument using Exercises 40-42. Differentiation
  requires L1 function and derivative with the stated fundamental
  theorem from minus infinity. Preservation and pointwise inversion
  apply to Schwartz functions. The audit must check all derivative
  seminorms and endpoint limits, not merely local smoothness or
  decay of the function alone; finite-interval FTC must support the
  required improper endpoint identity. This is an audit obligation,
  not a claimed new defect in L907.
- Mathlib [Charpoly.Basic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Charpoly/Basic.html#LinearMap.aeval_self_charpoly),
  charpoly_monic and aeval_self_charpoly: commutative ring, finite
  free module, actual module endomorphism. A finite-dimensional
  complex function space fits this framework only after its invariance
  is established. No additional Mathlib coverage claim is made.

Local comparison read L907 in full and L906's endpoint proof and
recorded audit, the step145 search record, step146 history, and
ATTEMPTS/2026-11-08-hedenmalm-positive-pair-import-stop.md and
ATTEMPTS/2026-11-08-hedenmalm-enlarged-domain-inverse-stop.md.
These preserve the distinct enlarged-domain and missing-metric stops;
the finite-span audit does not reopen either claim. No duplicate
intersection theorem was identified in this narrowly reused record.
Unread ODE/resolvent leads remain unread; no search-completeness or
originality conclusion follows.

Bounded next test: independently verify the complete complex integral,
conditional finite invariance, characteristic-polynomial application,
Schwartz hypotheses, multiplier convention and continuity/inversion
steps in L907. Retain the result only if every obligation passes;
otherwise identify the exact failure without changing the domain.
Metric, symmetry, completion and actual-Xi mixed positivity remain
unresolved even if it passes. No lemma, script, DAG or PROOF change
is authorized by or made during this literature-only step.
