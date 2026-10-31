# Two-shift cusp variation: source comparison

TARGET: Test whether iterating L520's localized inverse along the shifts log(2) and -log(3), with all path collisions retained, forces an unbounded BV seminorm from a nonzero endpoint trace when ell>log(6).
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed a bounded search for logarithmic translated singularities, difference-differential propagation and logarithmic-Laplacian BV; checked the specific prime-image/BV assessments and stops against L520/L521. The inspected propagation and regularity results do not match the required lower bound; no novelty or nonexistence conclusion follows. Exact queries and route disposition are below.
SOURCE_EVIDENCE: Inspected Chang-Lara–Saldana arXiv:2208.12841v3 Theorem 4.12, Lemma 4.14 and Corollaries 4.16–4.17; Galerne doi:10.1017/apr.2016.60 Section 2 Theorem 1/proof pp.951–953; Wang–Yu–Zhang arXiv:2502.19262v1 (1.1), Theorem 2.1, Remark 2.2 and Section 5.1 (5.2)–(5.4)/converse; Biswas et al. arXiv:2608.07315v1 Theorems 1.1–1.2. Direct primary links and applicability are below.
COMPARISON: The actual BV criterion concerns the variation of the combined function; inspected propagation tracks changing Sobolev order, not additive BV mass. L521 already controls the full signed equation with every collision, while L520's one-image remainder is not depth-uniform. Iterating their upper estimates adds no independent signed lower information. These are scope obstructions, not a contradiction to the target or RH.
GAP: A lower bound for the combined signed profiles, with all collisions and a depth-controlled remainder, remains missing. No inspected theorem provides it. The review identifies no independent noncancellation mechanism making that test actionable; an absolute path count or dense location set cannot replace it.
REASON: Park this iteration-only implementation after the completed source comparison. EXPLORE records an unmatched bounded search, not permission to repeat the parked calculation. Reopening needs a materially new signed lower-bound mechanism and separate assessment; do not derive or approve a propagation theorem from this literature turn.
LITERATURE_REASON: Iterated intersecting prime-shift images and depth-uniform variation estimates are outside the single-image and fixed-vector BV assessments; ell>log(6) is also a new restriction. This is missing essential coverage, not a repeat review of the ready transport target.
SCOPE: Conditional L516 model with 0<a<A, ell=2a>log(6), actual c, nu_rho, signed pole, both shifts, every equality atom, fixed-interval b>=0, a real normalized nullvector and nonzero left trace. Retain L520's direct reflected-image exclusion, but impose no unproved separation of later images, sign of the vector or forcing, H1 regularity, or uniform family bounds. No computation is approved yet.

## Original continuation nomination

The main gap is actual-Xi all-degree positivity. The proposed
intermediate question is whether the equation forces more total
variation than L521 permits when the endpoint trace is nonzero.
A justified contradiction could exclude such conditional nullvectors
in this restricted support range. Smaller supports, realization,
positive-eigenvalue rates, collars and Xi transfer would still be open.

The precise mathematical test, after source coverage and separate
approval, should be finite-depth first: keep every signed contribution
and every collision among paths made from +log(2) and -log(3), with
all intermediate positions inside the interval. Determine whether
an independently justified lower bound on total variation can grow
without bound with depth while all remainder constants are controlled.
No existence, density, disjointness or noncancellation theorem about
these paths is asserted in this nomination. The prime weights and
all other terms of the complete equation must remain. Identical image
positions do not authorize adding absolute contributions before their
signs and remainders are known.

The source comparison must use the inspected single-image work as an
input rather than automatically import a stronger gradient theorem.
In particular L521 (19)-(20) already obtains a strict contraction
for an upper variation estimate by fixing the collars and then the
high-frequency cutoff. Any proposed growth must confront that
regularization and cannot treat each cusp as a fixed unsmoothed copy.
The old direct Green/automatic regularity stops remain intact.
The first comparison must decide whether this existing absorption
already exhausts the proposed iteration-only mechanism. If so, record
that scope obstruction rather than restating it as a new propagation
theorem or authorizing a calculation with no independent sign input.

Continue only if primary comparison identifies a concrete justified
finite-depth coefficient/remainder test capable of distinguishing an
unbounded lower bound from a summable, cancellation-compatible model.
Park the implementation if it merely reproduces a finite number of
L520-type profiles, uses dense locations as a contradiction, assumes
smoothness of other shifted terms, or lacks a way to control the
accumulated remainder. A summability obstruction would concern this
mechanism, not the validity of L520/L521 or RH.

No new result, mathematical script, source import, readiness approval
or cross-notebook input occurred in the original nomination above.
The completed review below supersedes its pending-review status;
it does not supersede the mathematical qualifications or old stops.

## Completed source comparison, 2026-10-30

The target text is unchanged. Its desired intermediate result would
exclude a conditional nonzero-trace nullvector by a variation
contradiction. Actual-Xi positivity, realization, smaller supports,
the eigenvalue-relative upper bound, collars and Xi transfer would
remain independent gaps. No such contradiction was established.

### Searches, reused coverage and inspected primary results

Search queries included `"logarithmic" "translated" "singularities"
pseudodifferential regularity`, `"logarithmic Laplacian" "propagation"
singularities translations`, `"logarithmic" "difference-differential"
"singularities"`, `"functional differential" "propagation of
singularities" delay equations`, and `"logarithmic Laplacian"
"translation" "bounded variation"`. Followed the relevant propagation
lead to its primary text. Unrelated q-difference asymptotics and wave
resolvent results were search leads only, not inspected theorems or
inputs. A failed search is not evidence of novelty.

1. Chang-Lara–Saldaña, *Classical solutions to integral equations with
   zero order kernels*, [arXiv:2208.12841v3](https://arxiv.org/html/2208.12841v3),
   3 October 2022. Theorem 4.12 requires bounded inner radius,
   translation invariance, uniform ellipticity, 1-regularity, bounded
   locally Dini u and a finite weighted 1-log forcing norm. Its result
   is an upper interior regularity estimate. Lemma 4.14's proof
   (4.13)–(4.14) estimates the cutoff tail by kernel differences;
   it does not regularize the atomic translates. Corollaries
   4.16–4.17 retain forcing norms and shrink the observation region.
   Section 6(1)'s stronger bootstrap question is not an available
   theorem. No signed profile or depth-uniform lower estimate is
   supplied. The required complete-forcing hypotheses are unverified.

2. Galerne, *Random fields of bounded variation and computation of
   their variation intensity*, Adv. Appl. Probab. **48** (2016),
   947–971, [doi:10.1017/apr.2016.60, primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/83627D38EAB49283AE917366027E8BE7/S0001867816000604a.pdf/random_fields_of_bounded_variation_and_computation_of_their_variation_intensity.pdf),
   Section 2, Theorem 1 and proof, pp.951–953. For an L1 function on
   an open set and a unit direction, finite directional variation
   is characterized by finite quotient liminf, with equality of the
   variation and quotient limit. The proof uses the signed
   distributional limit, measure compactness and lower
   semicontinuity. For Eu on R, L515 supplies integrability and
   there is no domain erosion. This is already imported in L521;
   a collection of formal summands has not thereby been assigned
   additive variation. No reproof or stronger import is needed.

3. Wang–Yu–Zhang, *Periodic propagation of singularities for heat
   equations with time delay*,
   [arXiv:2502.19262v1](https://arxiv.org/html/2502.19262v1),
   26 February 2025, equation (1.1), Theorem 2.1/Remark 2.2,
   Theorem 4.1 and Section 5.1. The equation is a Dirichlet heat
   evolution on a bounded C2 domain with one positive time delay,
   nonzero scalar coefficient, L2 initial data and, for Theorem 2.1,
   smooth compactly supported history. The propagated Sobolev
   threshold changes by two orders per forward period. The proof
   isolates one new term in (5.4), with smooth history contribution
   (5.2) and smooth earlier terms, then checks the converse by local
   heat regularity. Neither the equation nor that separation
   hypothesis matches the stationary two-sided logarithmic model.
   There is no BV-mass growth or intersecting-path theorem here.
   Publisher retrieval returned 403; the primary arXiv statement
   and relevant proof cases were accessible. No blocker remains.

4. Biswas–Roy–Sen–Sharma, *Hölder regularity and Harnack inequality
   for the logarithmic Laplacian*,
   [arXiv:2608.07315v1](https://arxiv.org/html/2608.07315v1),
   7 August 2026, Theorems 1.1–1.2 and the paragraph following
   Theorem 1.3. Both regularity theorems require n>=2 and
   positive-power Hölder forcing. The authors explicitly connect
   the dimension restriction to the sign of their zeroth-order
   coefficient. This does not cover n=1 or the present rough
   translated forcing, and states no signed variation lower bound.
   The earlier proof-scope comparison is reused, not independently
   audited or broadened.

5. Zdanowicz–Peradzyński, *Propagation of weak discontinuities for
   quasilinear hyperbolic systems with coefficients functionally
   dependent on solutions*, Ann. Polon. Math. **109** (2013),
   177–198, [doi:10.4064/ap109-2-6, primary PDF](https://www.ippt.pan.pl/repository/open/o2261.pdf),
   Section 2, Theorem 2.1/proof, pp.178–180. This assumes a
   first-order quasilinear system, continuous coefficients and
   solution, piecewise C1 regularity across a smooth hypersurface,
   and finite nonzero one-sided derivative jumps. It locates a
   characteristic surface by subtracting the two classical
   equations. Those hypotheses and its conclusion do not supply
   the logarithmic cusp or BV lower bound here. This inspected
   terminology match is excluded, not imported.

The [single-image comparison](2026-10-30-weil-prime-shift-cusp-coverage.md)
and [BV audit coverage](2026-10-30-weil-global-variation-closure-audit-coverage.md)
are reused for renewal normalization and the old Green/automatic-BV
scope failures. Their underlying sources were not all reopened.
No full matching Mathlib theorem has been checked; no absence is claimed.

### Duplicate check and disposition

Read L520 and L521 in full, including their recorded local audits;
searched their specific working records and the first-image history
for iteration/propagation claims. L520 (15) deliberately leaves
new shifted forcing inside a bounded remainder. It establishes no
signed profile for every subsequent image. Its constants depend on
the fixed localization, vector and isolation. L521 (17)–(20)
already retains the entire finite measure and all coincident images,
fixes collars before choosing frequency, and obtains theta<=1/2.
Neither is being rederived or independently reaudited in this turn.

This exhausts the proposed *upper-norm iteration* implementation:
it contains no new lower information beyond the existing closure.
It does not prove that the actual signed profiles are summable,
that cancellation occurs, or that a nonzero-trace nullvector exists.
A lower bound contradicting L521 could still exclude that nullvector;
L521 alone does not logically prohibit such a discovery. The missing
ingredient is an independently justified noncancellation/lower-bound
mechanism, not another upper estimate or a count of image locations.

Park this implementation rather than authorize a calculation that
merely repeats L521 or lists finitely many L520-type cusps. Reopen
only with a new combined signed coefficient/variation certificate
and a proposed depth-uniform remainder test retaining all collisions,
both traces and the complete equation. No such certificate was
derived or approved here. This source-scope NEGATIVE changes the
route decision; it is not a mathematical disproof of the target,
of L520/L521, or of RH. See the retained
[working record](../2026-10-30-weil-two-shift-source-review-working.md)
and [implementation stop](../../ATTEMPTS/2026-10-30-weil-two-shift-iteration-source-stop.md).
