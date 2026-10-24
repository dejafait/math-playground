# Coverage: subendpoint relative Mellin freezing

TARGET: Attempt uniform relative Mellin freezing S_{r,m}(a)/|ζ((1+m/r)/2+ia)|²=1+o(1) on 31/32≤m/r≤63/64, retaining both shifted-line residues and complete tails under the pinned external input.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches for logarithmic Riesz means, high-order Dirichlet smoothing and paired-zeta Mellin freezing found no inspected matching theorem. Reused the Littlewood and pinned-input assessments; inspected L303, L307, L326/L327, L330 and the relevant L452/L453 proof ranges, plus four recorded failures. Queries and source scope are recorded below; no novelty claim.
SOURCE_EVIDENCE: Reused Titchmarsh–Heath-Brown (1986), Theorem 14.2 and proof, pp. 336–337, and Section 14.3, pp. 338–339, through the existing assessment and audited L452. Newly inspected DLMF 25.2(i)/25.2.4, 1.14(iii)/1.14.20 and 5.11.3/5.11(ii), including hypotheses and relevant cases. L307 supplies the already proved remote-pole/contour precedent, not this band’s conclusion.
COMPARISON: L452 (1) covers the proposed real-part band, and its proof (8) retains analytic-logarithm control. L453’s σ>1 Euler tail bound and bounded-offset kernel domain do not cover this target. Standard inversion, meromorphy and Stirling plus L307 cover the source mechanisms for a new contour/tail specialization; none states the proposed uniform relative asymptotic.
GAP: Prove the changed-exponent kernel bounds on c=m/(2r), the complete two-pole contour identity, a quantitative non-Euler normalization and a relative tail estimate on every vertical region. These uniform estimates remain research obligations; the comparison and any resulting arithmetic sign are unproved.
REASON: The changed proportional band and contour required separate source comparison. Essential mechanisms are now covered for one bounded known-method specialization attempt; no reproof of the external half-plane theorem or Littlewood interpolation is needed.
SCOPE: Proposed arithmetic comparison only; no sector extension, every-height rounding, smaller-index segment as a whole, or external-theorem certification.
LITERATURE_REASON: The fixed proportional band below m=r and its pole-crossing contour were outside the ready endpoint scope; this review supplies the missing comparison and does not repeat its audit.

## Proposed mathematical target and relevance

Let m be a positive even integer, r tend to infinity with
31/32≤m/r≤63/64, and set h=9/2+m/(2r),
a²=4π²exp(4r)−h² with a>0. Define the finite full sum by
the weight formula in L453 (7), retaining exponent m:

    S_{r,m}(a)=Σ_{j,k≥1}(jk)^(−1/2)
        (1−log(jk)/(2r))_+^m exp(ia log(k/j)).

The proposed test is the uniform comparison

    S_{r,m}(a)/|ζ((1+m/r)/2+ia)|² = 1+o(1).

This is a question, not an asserted result. The candidate Mellin line
is c=m/(2r), whose zeta real part is (1+m/r)/2<1.
Shifting the absolutely convergent starting line in L453 would require
accounting for the poles at z=1/2±ia, a justified bound for the entire
contour, and a quantitative nonzero normalization. Existing σ>1
reciprocal-series estimates do not provide that normalization here.
The assessment must compare these obligations with precise known
results and existing failures before authorizing any calculation.

The main gap remains global mixed positivity. A successful arithmetic
input could support sign estimates in a band below L453's endpoint
index. Extending the sector estimates to that proportional band would
remain an independent uncovered task, as would the initial low-index
segment and bounded exterior heights. No main-gap closure is claimed.

Essential local inputs to inspect are audited L453, L452 (1), L303,
L330 and the exact L326/L327 subendpoint interfaces; use the existing
Littlewood and pinned external-input source assessments. Preserve the
coefficientwise-freezing and fixed-r/unit-phase stops. Continue only if
source coverage identifies a concrete way to control the complete
relative error and residues uniformly. If the hypotheses or full-tail
comparison cannot be justified, record the obstruction and park this
dependent target rather than repeat the endpoint audit.

The September 30 external theorem and its unaudited manuscript/import
closure remain qualifications. Matching Mathlib coverage for this
proposed comparison has not been checked. This completed source review neither proves a lemma nor validates the
proposed comparison. The changed ready continuation receives separate
supervisor approval next turn.

## Review completed in this invocation

The invocation reviewed the saved action: “Assess source coverage for
uniform relative Mellin freezing on 31/32≤m/r≤63/64, retaining shifted-line
residues and complete tails.” TARGET now names the precise proposed
mathematical continuation, so it matches PROGRESS.md. SPECIALIZE approves
source coverage for an attempt, not the truth of its conclusion. The
mathematical attempt should be classified REPRODUCTION within this scope.
No new result, lemma, mathematical script, DAG edge or argument change
was made in this literature-only step.

The main gap, intermediate target and downstream use remain those stated
above. The continuation test is the complete relative error o(1), uniformly
in the stated band, with both residues divided by the same nonzero square.
Abandon this implementation if the available bounds leave any tail or
residue non-small relative to that square; record the precise failed
threshold. Even success leaves the sector extension, initial low indices,
bounded exterior heights and all-degree mixed positivity independent.

## Exact primary inputs and reuse limits

The existing [Littlewood assessment](2026-10-21-fixed-half-plane-endpoint-derivative-review.md)
records direct inspection of Titchmarsh–Heath-Brown, second edition (1986),
Theorem 14.2 and its proof, printed pp. 336–337, and Section 14.3,
pp. 338–339. The printed theorem assumes RH. Its conclusion is not
imported with that assumption suppressed. Audited L452 already supplies
the needed fixed-half-plane specialization, including its normalized
analytic logarithm, fixed radii and Cauchy neighborhood. Its proof (8),
not just its derivative conclusion (1), is available for the proposed
non-Euler modulus estimates. The normalization real parts lie in
[63/64,127/128], inside L452 (1); both large positive shifted heights
must be checked before applying it. Conjugation handles the other sign.
A fresh fetch of the book PDF timed out; the existing inspected coverage
and local audited proof suffice, so this is not an essential source block.

The pinned OpenAI September 30, 2026, Theorem 1.1 and commit remain exactly
as in the [external-input register](../../foundations/2026-10-quasi-riemann-input.md).
Neither that theorem nor its manuscript/import closure was re-audited.
Its strict half-plane, allowed pole and lack of a boundary assertion
remain qualifications. Liu’s stronger boundary is unnecessary here.
No reciprocal Euler series is continued left of 1.

Newly inspected standard inputs, accessed 2026-10-23:

- [DLMF 25.2(i) and 25.2.4](https://dlmf.nist.gov/25.2): the Dirichlet
  series requires Re(s)>1; continuation is meromorphic with only the
  simple pole at 1, of residue 1. The Laurent expansion is also recorded.
  This supports pole bookkeeping, not a positivity theorem.
- [DLMF 1.14(iii), especially 1.14.18–1.14.20](https://dlmf.nist.gov/1.14.E20):
  inversion assumes continuity, piecewise continuous derivative and
  exponential growth, with the inversion line to the right of its growth
  exponent. The subsection also gives a decaying-transform version.
  This supports the scalar inversion already proved in L303, not an
  exchange with nonabsolutely convergent zeta series.
- [DLMF 5.11.3 and 5.11(ii)](https://dlmf.nist.gov/5.11): Stirling’s
  expansion applies in a closed sector away from the negative real axis;
  the error section includes the positive-real and complex cases. Only
  positive real m+1 is needed for the proposed kernel normalization.
  The contour tails still require bounds on the entire zeta product.

Named residue theory is the remaining standard contour input. L307’s
complete proof already justifies horizontal edges at fixed parameters
by polynomial zeta growth and retains the two remote poles. It also
records an elementary bound on ζ(1+2ia). Its endpoint conclusion cannot
be imported after replacing exponent r by m. A new uniform parameter
argument is necessary. In particular no shift through zero or functional-equation
duality is needed for the proposed positive line c; L307’s
central-residue/self-reproduction conclusion supplies no sign here.

## Complete-error obligations for the bounded attempt

This is a proposed proof organization, not a derivation of the estimates.
Begin with the absolutely convergent line c_start>1/2 from L303’s scalar
inversion mechanism. Keep exponent m throughout. Shift to c=m/(2r),
retaining the residues at z=1/2±ia with correct orientation, factorial
and exponential normalization. Establish horizontal-edge convergence
before taking an infinite contour limit. The pole at zero lies outside
this shift. Treat a as fixed during each shift, then establish uniform
bounds on the coupled domain; fixed-a constants alone are insufficient.

For the target line, seek the bounded kernel mass and Gaussian core
using Stirling with m/r in the specified compact interval. L453 (34)–(36)
are a method precedent only: their bounded q−m proof domain has changed.
The exact scalar integral of the normalized kernel, rather than its
absolute integral, must remain one. On a central window use L330’s
quotient identity and L452 (1) with the new σ. This addresses variation
relative to the square without treating the two factors as conjugates
off the center or treating the Mellin kernel as a positive measure.

The entire outer part must be covered. A concrete candidate partition
uses a small fixed δ>0 and the window V=log(r)/sqrt(r): the core; the
region V<|v|≤δ; the region δ<|v|≤a/2; and |v|>a/2. On the first
outer region retain integrated logarithmic-derivative control rather
than replacing the relative quotient by a global modulus bound. For
the middle region inspect L452’s already bounded logarithm for upper
and lower normalization control, together with the kernel decay. On
the final unbounded region use elementary meromorphic growth, including
where either shifted height is small, and integrate the actual high
power of |c+iv|. L452 (4) and L307’s contour proof supply already checked
growth mechanisms. The fixed distance of σ from 1 must be retained at
small shifted height. Quantify the resulting tail and both residues
relative to the same square, with constants uniform in m/r.

In particular L453 (40) is unavailable on this line. Merely substituting
an exponential-in-log-height modulus bound into its old tiny-window tail
estimate does not establish a relative little-o estimate. The proposed
partition is independently testable and does not require a missing
source theorem, but every estimate and threshold remains to be proved.
No kernel bounds, new residue estimate or normalization inequality are
claimed by this review.

## Local overlap and failure comparison

L326’s full-sector interface and L327’s balanced AFE have exponent
m/r=3/4, outside this band. Their exact sum and error are informative
precedents, not a sector theorem for the proposed h. L327 leaves the
same unsigned ratio form and excludes a phase-uniform PSD replacement
at its recorded accuracy. The new attempt instead uses actual-zeta
logarithmic variation; it does not repeat that Gram replacement.

Read the recorded endpoint Mellin, saddle-freezing and Liouville-phase
failures and the below-five balanced-AFE failure. L304’s absolute
coefficient loss cannot justify relative freezing. L330’s zero-free
model shows why the derivative scale matters; L452 changes that input
for actual ζ. L335’s negatives at fixed r/arbitrary phases do not
satisfy the new coupled-height quantifiers. None is discarded or
reinterpreted as a counterexample to the proposed comparison. L307’s
self-dual shift is not a residue-dominance positivity argument.

Scoped searches found no duplicate statement in the named local
interfaces or assessments. This is a scoped comparison, not a new scan
of all lemmas and not an originality claim. Full matching Mathlib
coverage and supporting API names were not checked; absence is not
asserted. Any completed lemma must retain those qualifications and
precise supporting citations.

## Search record and uninspected leads

Queries used: `Riesz logarithmic means zeta product Mellin Perron
zeta(s+it) zeta(s-it)`; `Riemann zeta function zero free half plane
reciprocal zeta Littlewood log zeta bound theorem`; `"zeta" "logarithmic
Riesz means" product`; `"zeta" "Mellin" "freezing" modulus square`;
`"zeta" "Perron" "large" "Riesz" means order`; `"Riesz means" "large
order" "Dirichlet"`; and `"zeta" "logarithmic weights" "saddle point"
Mellin product`.

Search results included general Riesz summation, Maass-form Riesz means,
shifted critical-line moments and statistical freezing terminology.
Those result snippets are not theorem evidence. No returned result was
identified as a matching coupled-height, growing-order relative theorem;
these adjacent leads were not inspected or used as inputs. Primary
coverage for this bounded attempt is the standard sources and existing
local proofs explicitly inspected above. The search is not exhaustive.
