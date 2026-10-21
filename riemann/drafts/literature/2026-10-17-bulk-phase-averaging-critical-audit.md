# Source assessment: critical audit of the actual-height bulk limit

TARGET: Critically audit L426's actual-height phase-averaging reduction, retaining all joint characters, the fixed mixture, both branch stages and the full response.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 183's bounded search and inspected-source assessment; compared the full L426 proof with its source domains and audited L425, L423's fixed mixture and L424's exact observable; additionally located Kowalski Example B.6.2(1)--(2) for the complete product-character scope.
SOURCE_EVIDENCE: Kowalski January 19, 2021, Example B.6.2(1)--(2), p.145, Theorem B.6.3, p.146, and Proposition 3.2.5/Lemma 3.2.6, pp.42--43; Tao 247B Notes 8, Lemma 2.3 and (4), pp.4--5; reused the previously inspected Morters--Peres May 25, 2008 Appendix Theorem 1.6(v), pp.331--333.
COMPARISON: Standard sources cover finite-support product characters, character-to-Haar convergence, sharp nonstationary integration and a fixed bounded test with null discontinuities; they do not certify L426's carrier bounds, exact matrix comparisons, two-stage selection or sequential limits. A critical audit of those specializations is covered, without a new general theorem or integral evaluation.
GAP: L426 remains unaudited; I's value and sign are unknown. No actual realization, nonzero transport defect, clipped statistic or full-error regulator margin is supplied by these sources.
REASON: This separate literature-only comparison approves the newly written audit scope, preserving the completed step 184 and reusing its ready source coverage; the next turn should perform the mathematical audit.
SCOPE: Only the exact TARGET, with fixed sigma=5/2, fixed k=13,14 mixture and prescribed ordered equality/strict branches; no sign calculation, growing character family, critical-line phase law or global independence assumption.
LITERATURE_REASON: The saved continuation explicitly required a separate source-gate comparison for the newly written L426 audit; this turn closes that comparison rather than repeating discovery for the already covered averaging target.

## Source scope and what was actually read

Reuse `2026-10-17-covariance-free-bulk-phase-averaging.md`, including
its recorded search queries, versions, inspected proof cases and exclusions.
No new broad search is needed for unchanged tools. This turn read all of
L426, L425's separate step-182 audit, L423 through its exact fixed mixture,
L424's hypotheses/conclusion, the step-183/184 history locations, and the
step-175 failure record. These are scope comparisons, not a critical audit
or a derivation of new mathematics.

The following precise standard imports are adequate for the later audit:

- [Kowalski, January 19, 2021 manuscript](https://metaphor.ethz.ch/x/2021/fs/401-3109-65L/probabilistic-number-theory-fs-2021.pdf),
  Example B.6.2(1)--(2), printed p.145, explicitly describes circle
  characters and finite-support characters of arbitrary compact products.
  Theorem B.6.3, p.146, applies to compact abelian groups, not merely a
  finite torus. Reopened these statements and B.6.5's continuous-orbit
  proof; also reopened Proposition 3.2.5/Lemma 3.2.6 and the Re(s)>1
  Euler-log argument, pp.42--44. These give the character and response
  framework; the carrier and dyadic interval still require local checks.
- [Tao, Lecture Notes 8 for 247B, Winter 2007](https://www.math.ucla.edu/~tao/247b.1.07w/notes8.pdf),
  Lemma 2.3 and equation (4), printed pp.4--5: reopened the complete
  sharp-interval integration-by-parts proof, including the endpoint
  term and derivative of the reciprocal phase derivative. It requires
  both |phase'|>=b>0 and |phase''|<=C, yielding
  O(lambda^(-1)(b^(-1)+C|J|b^(-2))). Lemma 2.4 instead requires
  monotonicity. Example 2.2 forbids inference from speed alone.
- [Morters--Peres, Brownian Motion, May 25, 2008 draft](https://www.stat.berkeley.edu/users/aldous/205B/bmbook.pdf),
  Appendix Section 1, Theorem 1.6(v), printed pp.331--333: reuse the
  prior assessment's inspected statement and (iv)-to-(v) proof. Weak
  convergence on a metric space permits a bounded measurable fixed
  test with limiting-law-null discontinuities. It does not cover an
  H-dependent selector directly. A fresh web open indexed the PDF,
  but targeted retrieval then timed out; no fresh inspection of that
  passage is claimed. The unchanged prior inspected coverage remains
  adequate; this refresh failure is not an essential source blocker.

These citations suffice for the standard theorems; no reproof is needed.
The full prescribed-observable reduction is a local specialization, not
an imported theorem. Matching Mathlib coverage remains not checked;
supporting formal results alone would not certify the branch comparisons.

## Exact audit obligations approved for the next turn

The main RH gap is the unproved global mixed positivity assertion. The
intermediate target is reliability of L426's qualitative B_H^0=I+o(1)
reduction, with L424/L425's complete-law consequence. If valid, this
could support a separately reviewed rigorous test of the remaining
transport observable. It neither supplies a sign nor bypasses the
independent realization, clipping and regulator obligations.

1. Compare L426's complete character list with Kowalski B.6.2 and
   B.6.3, including the countable compact product topology and its
   metrizable Borel laws. Check both zero-carrier and nonzero-carrier
   cases on sharp [H,2H], negative indices, the trivial character and
   the real-H limit. Use L369's actual carrier derivative estimates;
   check Tao's two derivative hypotheses and both endpoints. Neither
   a finite-prime law alone nor speed alone proves the joint law.
2. Check the full response series/Euler-log identity at sigma=5/2,
   continuity, uniform nonvanishing and actual-path identification
   against L368 and the cited absolute-convergence domain. Composite
   coordinates must remain multiplicative. A circle-valued phase
   suffices; no global real argument on the torus may be presumed.
3. Check the exact fixed test against L419's literal ordered rule and
   audited L425's branch analysis. Retain both equality rules and the
   complementary stage, and verify that the proposed exceptional set
   covers every discontinuity. Its nullity must concern the combined
   carrier/response phase. Check Borel measurability, boundedness and
   the fixed-test hypothesis before importing Morters--Peres.
4. Verify L423's exact alpha, both powers, w and g_H normalization;
   L390's complete physical J expansion; positive-scalar invariance
   at both stages; and L425's uniform compact-branch comparison.
   In L426 (10), check fixed tie tolerance before H tends to infinity,
   followed by tolerance tending to zero, with constants independent
   of tolerance where asserted. Keep complete derivative/curvature
   errors and use the averaged mass loss, not pointwise smallness.
   Finally check L424/L425 at the exact X/sqrt(ell) normalization.

These are established-source application checks, not approval of their
answers. SPECIALIZE / REPRODUCTION is appropriate for that audit.
IMPORT would incorrectly suggest that a source already certifies the
whole local formula. No stronger lemma or sign computation is approved.

## Duplicates, failures and continuation test

The step-183 source assessment covered the original derivation, not an
independent audit of the subsequently written proof. L425's step-182
audit covers covariance deletion and supplies reusable branch controls;
it does not by itself audit L426's joint law or fixed-test passage.
The additional exact product-character citation narrows a specific audit
obligation without introducing another equidistribution proof.

Preserve `ATTEMPTS/2026-10-17-gaussian-jet-trajectory-diagnostic.md`:
the step-175 leading-matrix samples of both signs were not certified
quadrature or actual-height averaging. L426 proposes a qualitative
replacement only, so this audit does not reopen numerical signing.
The unavailable alternative probability PDFs recorded in step 183 are
unneeded because its inspected null-discontinuity theorem suffices.
No sibling notebook, critical-strip universality theorem or new phase
independence premise is an input.

Continue with one critical audit of the exact TARGET using L368, L369,
L390, L419, L423, L424 and audited L425. Success requires verifying every
load-bearing use above, with any repair fully recorded; I may remain
unevaluated. If a character case, discontinuity locus, response comparison
or limit order is unsupported, identify that exact claim and withhold
reliance on the affected conclusion. Do not substitute a different basis,
free composite phases, or a numerical margin. Actual realization, nonzero
transport defect, capped nondegeneracy, negative-Bcal clipping, L413's
full-error regulator margin and global mixed positivity remain unproved
and are not audit premises. No new lemma or mathematical script was
written in this literature step.
