# Coverage: lower-band moving-saddle positive margin

TARGET: Attempt a moving-real-saddle proof of a uniform margin S_{r,m}≥exp(-o(r)) on 7/8≤m/r≤31/32 under the pinned premise, retaining both residues and complete deformed-contour tails.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready inversion/logarithm assessments; searched moving-saddle, parameter-dependent analytic amplitude, logarithmic Riesz zeta products and paired-zeta Mellin positivity terminology. Inspected DLMF 2.4(iii)–(iv) and Temme 1308.1547v1 Sections 2.2–2.3 and the opening of Section 4/4.1; checked the scoped L331/L456 failures and L303/L330/L452/L454 interfaces. No inspected theorem directly states this arithmetic margin.
SOURCE_EVIDENCE: DLMF 2.4.10–2.4.16, including hypotheses (a)–(c), the two half-path proof and the simple-saddle branch rule; Temme (2013), equations (2.9)–(2.13) and (4.1)–(4.5), including parameter dependence and pole separation. Reuse the precise pinned half-plane and Littlewood/inversion/Stirling assessments below. Flajolet–Sedgewick is an unread nonessential lead after retrieval failures, not a theorem input.
COMPARISON: The inspected simple-saddle mechanism covers central expansion and complete-contour dominance only after its hypotheses are verified. DLMF's fixed-phase formulation does not supply uniformity for the moving paired-zeta exponent. L456 provides a bounded analytic logarithm on fixed disks, but its straight-line tails are not automatically deformed tails. SPECIALIZE permits checking these differences, not importing the desired margin.
GAP: Establish a uniform real saddle in reserved zero-free disks, positive oriented leading normalization with logarithm -o(r), a uniform local remainder, and every deformed annulus, connector, remote-height tail and both residues as o of that same positive leading scale. None is proved by this review; no assumption S/B→1 is authorized.
REASON: Accessible primary hypotheses and proof cases now cover one bounded known-method specialization test of the unchanged target. No essential source is blocked; application estimates and parameter uniformity are mathematical obligations. This changed ready assessment requires separate supervisor approval next turn before research.
SCOPE: The exact TARGET and L456's real-r, even-m coupled definitions on the entire closed band, including m/r=7/8; arithmetic moving-saddle comparison only, without theta-sector extension, every-height transfer, external-proof audit or a general new saddle theorem.
LITERATURE_REASON: The new positive-margin target uses a displaced saddle and full deformed contour, outside the ready fixed-circle relative-freezing assessment; L456 supplies a specific failed threshold motivating this change.

## Initial proposal, preserved before the completed review

The following proposal records the initial uncovered state. Its request
for a literature-only next invocation is discharged by this review;
the completed decision above and scope below govern continuation.

The main gap remains the initial low-index segment and global mixed
positivity. A positive arithmetic margin could support a separately
assessed theta-sector reduction and lower-index sign band; those
sectors, every-height passage, still smaller indices and bounded
exterior heights remain independent unresolved steps.

Essential local inputs are L303, L330, L331, L452, L454 and L456.
Use the exact r,m,h,a,S,B definitions of L456, not an endpoint or
fixed-r substitute. L331's old regional obstruction concerns shrinking
Vinogradov--Korobov neighborhoods; L452 changes those available source
domains, but establishes no complete moving-saddle asymptotic. L456's
new fixed-circle obstruction is not an obstruction to every saddle
method. Its local calculation has not received a separate critical audit.

Retain OpenAI's September 30, 2026 Theorem 1.1 at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, the strict Re(s)>7/8
half-plane, allowed pole and unaudited manuscript/import closure in
the external-input register. Do not substitute Liu's boundary or RH.
The proposed exp(-o(r)) lower margin is uniform in m/r on the whole
closed band: one function eta(r) tending to zero should give
S_{r,m}>=exp(-r eta(r)) beyond one real-r onset. Such a margin would
dominate a separately proved error O(r^C exp(-c r)) with fixed c>0;
no changed-band theta error is assumed. The proposed target is this margin,
not the already failed requirement of proving relative error o(1) by
the same fixed-circle magnitude certificate.

The source review should first identify an applicable complete-saddle
result or a bounded specialization test with all analytic neighborhoods
reserved. Continue only if it gives a concrete test of local remainder,
positive leading normalization and the entire contour complement
relative to the proposed margin. A local saddle alone is insufficient.
If the source comparison reveals an equivalent missing arithmetic
condition or uncontrolled complement, record that precise obstruction
instead of deriving or approving the new mathematics in the review.
Matching Mathlib coverage is unchecked; no absence or novelty is asserted.

## Completed source comparison — 2026-10-23

This is a LITERATURE / NOVELTY_UNCHECKED / EXPLORATION step. It supplies
source coverage and a bounded application test, with no new mathematical
result, lemma, calculation script or change to the main argument.
The exact TARGET is unchanged. A subsequent mathematical specialization
within this scope should be classified REPRODUCTION. The newly ready
assessment must receive its separate supervisor approval first.

### Primary statements and essential proof cases actually inspected

[DLMF 2.4(iii)–(iv)](https://dlmf.nist.gov/2.4#iii), online text retrieved
2026-10-23, equations 2.4.10–2.4.16: the endpoint theorem requires
analytic phase and amplitude on a domain containing the path, local
convergent expansions with nonzero first phase coefficient and the
stated positive exponents, absolute uniform convergence at the other
endpoint, and strict real-phase increase with a uniform endpoint gap.
The saddle case splits into two half-path integrals. A simple stationary
point gives the Gaussian expansion (2.4.15); the square-root branch in
(2.4.16) is selected by the outgoing contour direction. The text does
not require an exactly steepest path. It initially fixes the phase
angle and a saddle independent of the large parameter. This is a
source for the mechanism, not a uniform theorem for our varying exponent.

[N. M. Temme, *Uniform Asymptotic Methods for Integrals*,
arXiv:1308.1547v1, 7 August 2013](https://arxiv.org/html/1308.1547v1),
Sections 2.2–2.3, equations (2.9)–(2.13), supplies the Gaussian
reduction and analytic-domain/convergence requirements. Section 4's
opening explicitly separates additional-parameter uniformity;
Section 4.1, (4.2)–(4.5), keeps a nearby pole separate by subtraction
and residue treatment. These passages were read, not just the abstract.
No zeta-specific uniformity or positive arithmetic margin is stated.

The Olver book pages cited by DLMF (1997 reprint, pp. 121–127)
were not independently retrieved; DLMF's displayed hypotheses and
two-half-path argument are the inspected input. Flajolet–Sedgewick,
*Analytic Combinatorics*, Theorem VIII.3, appeared in search results,
but the author-hosted full PDFs exceeded the web fetch limit, the
Princeton copy returned 403, and shell retrieval failed DNS. Neither
its theorem nor its proof is counted as read. These failures do not
block the independently accessible DLMF/Temme mechanism; no further
retrieval is essential to the bounded test authorized here.

Reuse [the lower-band assessment](2026-10-23-lower-band-relative-mellin-coverage.md),
[L454's assessment](2026-10-23-subendpoint-relative-mellin-coverage.md)
and [the fixed-half-plane assessment](2026-10-21-fixed-half-plane-endpoint-derivative-review.md)
for their unchanged inspected primary logarithm, inversion, meromorphy
and Stirling inputs. The pinned premise and all external trust limits
remain exactly those in the initial proposal and register. The printed
RH estimates are not imported with weakened hypotheses.

### Differences that a mathematical specialization must actually prove

Use exactly L456's S, A, c, sigma, B, h and a. L303's inversion,
L330's retained linear phase and L454's pole bookkeeping explain the
interface; their endpoint or narrower-band conclusions are not lower-band
theorems. Locally use the complete logarithm of L456's meromorphic
integrand, with exponent m+1 in its power of z, and normalize the paired
logs to have real sum on the real diameter. A logarithm is needed only
on the reserved local domain, not through the remote poles.

L456's proof already bounds its normalized analytic logarithm on the
whole radius-273/256 disk about 2+it, using the stated larger disks.
This is the relevant available domain, rather than L452's narrower
conclusion strip. Reserve a fixed smaller disk for every required
derivative and a further disk for Taylor remainders. The first bounded
test may try disks of radius 2d about the bare saddle (m+1)/(2r),
with d=1/4096, using reflection for the negative-height factor.
Inclusion of every disk in the existing log domains, strict clearance
from Re(s)=7/8 and the pole, and uniform constants are obligations of
the attempt, not new disk estimates established here. L331's endpoint
criterion must be checked with the changed m,r normalization before
it is reused; its conclusion cannot simply be relabeled.

Continue only after a real saddle x_* and strictly positive curvature
are established uniformly. The upward vertical orientation, the positive
factor A and the correct square-root branch must give a positive
leading scale M_*. Prove log M_* >= -r eta(r), eta(r) tending to zero,
with one uniform onset. Retain the factorial in A: a positive zeta
value at x_* alone is not this normalization estimate.

Choose and justify a central window whose Taylor error tends to zero
and whose scaled Gaussian width tends to infinity. Uniformity must
include both closed band endpoints. Conjugacy is not cancellation of
the linear phase at the bare saddle. Neither DLMF's fixed-phase theorem
nor a formal stationary equation proves these varying-parameter claims.
Only the actual application estimates need proof; do not reprove the
general saddle theorem as a purported new result.

For the full contour, test a displacement from Re(z)=c to Re(z)=x_*.
Justify the finite rectangles first and the height limit at fixed
parameters; inventory any crossed poles before taking uniform limits.
Keep L456's two original residues even if this additional displacement
crosses none. Prove the annulus between the central window and a fixed
small boundary, the remainder up to heights comparable to a, and the
complete far tails including v near plus/minus a. Use the meromorphic
product, rather than a local logarithm, outside its valid domain.
Bound every connector, residue and tail relative to M_*, with sum
o(M_*). L456's straight-contour estimate relative to B does not by
itself verify any of these deformed-contour comparisons.

These are independently checkable success conditions, not assumed
positivity or a derived asymptotic. If any neighborhood, orientation,
remainder or full-complement condition cannot be justified from the
assessed inputs, record its precise failed threshold and park that
implementation. A local saddle alone is not success. A completed
positive asymptotic would still need its later critical audit.

### Duplicate and obstruction comparison; downstream limits

The September 24 L331 attempt fails for a shrinking classical zero-free
domain. L452/L456 change the available analytic domain; the old models
retain their original hypotheses and do not ban this different test.
L456's new fixed-center exponent obstruction concerns the stronger
relative-freezing certificate. L330 already distinguishes failure of
that comparison from failure of a positive margin. L306/L307 obstruct
uniform positive-square replacement and residue dominance, respectively;
neither supplies the proposed displaced-contour estimate. Preserve
L323/L327 and the fixed-r/unit-phase stops; do not enlarge their
quantifiers to the coupled moving-height target.

Queries used included `saddle point method parameter dependent analytic
amplitude uniform error contour tails theorem Olver Temme`,
`"Riesz" "zeta" "saddle point" logarithmic`,
`"zeta" "paired" "saddle point" Mellin positivity`,
`"saddle" "Riesz means" "zeta" logarithmic high order`,
and `"zeta" "product" "moving saddle" Mellin`, followed by
author-hosted Flajolet–Sedgewick retrieval searches. No inspected
matching full arithmetic theorem was found. Third-party RH discussions
and unrelated search returns were not used as evidence. This bounded
search does not establish novelty or exhaustive absence of a theorem.

A uniform margin would be one arithmetic input toward a lower-index
Laguerre sign band. The changed-band whole-plane theta reduction,
every-height transfer, smaller indices, bounded exterior heights and
global mixed positivity remain separate. No sign range, zero exclusion
or RH conclusion changes in this source review. Full matching Mathlib
coverage and supporting saddle APIs are unchecked; no absence is asserted.
