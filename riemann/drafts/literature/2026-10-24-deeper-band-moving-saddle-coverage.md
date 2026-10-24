# Coverage: a strictly lower moving-saddle arithmetic band

TARGET: Test whether L457's moving-saddle arithmetic margin extends uniformly to 13/16≤m/r≤7/8 under the unchanged pinned external premise, with complete relative error o(1) and |log M*|=o(r).
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched paired-zeta moving-saddle arithmetic, logarithmic Riesz positivity and the exact 13/16 saddle terminology; reused the earlier exact-sum and saddle searches and screened L452/L456/L457, their assessments, and the scoped L323/L327/L331/L335 failures. No inspected matching full-band theorem was identified; search returns alone are not theorem evidence.
SOURCE_EVIDENCE: Reinspected DLMF 2.4(iii)–(iv), equations 2.4.10–2.4.16 including hypotheses (a)–(c), both half-path cases and the branch rule; Temme 1308.1547v1 Sections 2.2–2.3 and 4.1, equations (2.9)–(2.13) and (4.1)–(4.5). Reused the inspected Titchmarsh–Heath-Brown (1986) Theorem 14.2/proof and Section 14.3, pp. 336–339, and prior inversion/pole/Stirling and pinned-premise assessments.
COMPARISON: The named interpolation and simple-saddle mechanisms cover a bounded specialization, not the requested arithmetic conclusion. L456's radius-273/256 logarithm disk does not cover the proposed lower endpoint; its larger Borel–Caratheodory domain is a starting input for a new intermediate-radius test. L457's exponent 2/3, constants and final errors cannot be imported on the new band.
GAP: Prove new reserved fixed logarithm neighborhoods with a fixed sublinear logarithmic-power bound, then a real saddle, positive factorial-normalized M*, |log M*|=o(r), and the entire relative error o(1), including annulus, middle range, both remote-height-zero neighborhoods, unbounded tails and both original residues, uniformly on the closed band.
REASON: Essential primary mechanisms are accessible and already assessed; the changed domain requires application estimates rather than an additional general theorem. This review approves one bounded known-method attempt, not its estimates or conclusion; the newly ready assessment receives separate supervisor approval next turn.
SCOPE: One proposed arithmetic target only, not a changed-band theta theorem, a Laguerre sign theorem, an analytic zero-free extension or an external-proof audit.
LITERATURE_REASON: The nominated lower endpoint is outside L457's ready domain and its inherited bounded-logarithm disk; this turn compares that changed hypothesis while reusing unchanged primary-source coverage.

## Original nomination, preserved

The following paragraphs record the initial REVIEW_REQUIRED proposal.
Their request for source comparison is discharged below; the completed
decision and bounded scope govern continuation. No proposed estimate in
the nomination has been proved by this literature turn.

The main gap remains initial low-index signs and global mixed positivity.
The intermediate target is the displayed arithmetic comparison with a
subexponential positive moving-saddle scale, on one specified lower
band. Its plausible downstream use is a lower logarithmic-index sign
band if a separate matching whole-plane theta estimate and parameter
transfer can also be established. Those independent steps are unproved
on this proposed domain. No extension is asserted or derived here.

Essential prospective inputs are L452, L456 and L457, with their exact
pinned September 30 Theorem 1.1 premise at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`: strict Re(s)>7/8,
allowed pole at one, no boundary assertion, and unaudited external
manuscript/import closure. Retain positive real r, positive even m,
the exact coupled height, the full finite S with zero cutoff equality,
and the complete factorial-normalized moving-saddle scale. Any changed
reserved radius or error exponent must be assessed before derivation;
L457's existing numerical bounds are not assumed on the new band.

Reuse the existing primary-source records where their hypotheses still
apply, and compare the exact changed-domain obligations with stronger
known conclusions and duplicates. L456 stops fixed-center freezing;
the proposed comparison keeps a moving saddle. L323/L327 and fixed-r
unit-phase failures remain relevant scope restrictions, not a global
ban. Do not reprove an already covered theorem as a new result.

The continuation test is whether inspected source hypotheses and local
interfaces justify one bounded mathematical attempt controlling the
entire relative error and a subexponential positive scale uniformly
over this exact band. If a required neighborhood, residue or tail
interface cannot be covered, identify that specific obstruction and
withhold approval; a local Gaussian calculation alone is insufficient.
This is a nomination for separate source review, not a ready assessment
or a mathematical result. Full matching Mathlib coverage is unchecked.

## Completed source comparison — 2026-10-24

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. It supplies a
changed-domain source comparison, with no new lemma or mathematical
script and no change to the argument or DAG. A mathematical attempt
inside this scope should be classified REPRODUCTION. The exact TARGET
is preserved; its newly ready assessment requires the separate
next-turn approval specified by the shared policy.

### Primary hypotheses and proof cases

[DLMF 2.4(iii)–(iv)](https://dlmf.nist.gov/2.4#iii), accessed
2026-10-24, equations 2.4.10–2.4.16, requires analytic phase and
amplitude near the path, the stated convergent local expansions,
absolute uniform convergence at the far endpoint, and a strict
real-phase gap away from the dominant endpoint. The interior-saddle
argument divides the contour into two half-paths. A nonstationary
interior point gives cancellation of the expansions; a simple saddle
gives the Gaussian term with a direction-selected square-root branch.
An exactly steepest path is unnecessary. The formulation first fixes
the phase angle and saddle, so it does not assert uniformity for this
height-dependent paired-zeta exponent.

[N. M. Temme, *Uniform Asymptotic Methods for Integrals*,
arXiv:1308.1547v1, 7 August 2013](https://arxiv.org/html/1308.1547v1),
Sections 2.2–2.3, (2.9)–(2.13), supplies Gaussian reduction with
analytic-domain and convergence conditions. Section 4, (4.1), warns
that extra parameters can change validity, rates and contours;
Section 4.1, (4.2)–(4.5), separates a pole before expansion and
retains its contribution. These relevant cases were read directly.
They justify the method comparison, not a zeta-specific lower bound.
The Olver and de Bruijn books referenced there were not newly read;
the previously unread Flajolet–Sedgewick lead remains nonessential.

Reuse the [Littlewood assessment](2026-10-21-fixed-half-plane-endpoint-derivative-review.md)
for Titchmarsh–Heath-Brown, second edition (1986), Theorem 14.2 and
proof, printed pp. 336–337, and Section 14.3, pp. 338–339. Its printed
RH assumption is not replaced silently. Only its inspected analytic-log,
Borel–Caratheodory, Hadamard three-circles and Cauchy mechanisms are
used. L452 and L456 give the local implementations and growth identity;
L457's separate audit validates the inherited disk and inversion used
there. That audit does not validate a larger bounded-logarithm disk.

Reuse the [inversion assessment](2026-10-23-subendpoint-relative-mellin-coverage.md)
for DLMF 1.14.20 (continuity, piecewise continuous derivative,
exponential growth, and an inversion line to its right), DLMF
25.2(i)/25.2.4 (absolute series only right of one and the simple
unit-residue pole), and 5.11.3/5.11(ii) (Stirling with its sector/error
qualifications). Positive real factorial arguments suffice here.
The [earlier moving-saddle assessment](2026-10-23-lower-band-moving-saddle-coverage.md)
and its [audit coverage](2026-10-23-lower-band-moving-saddle-critical-audit-coverage.md)
provide the unchanged complete-contour comparison. No essential source
is blocked and no new external theorem is imported.

### Changed interface and bounded attempt

Keep positive real r, positive even m, alpha=m/r in [13/16,7/8],
c=m/(2r), sigma=1/2+c, h=9/2+c, and the exact positive
a=sqrt(4*pi^2*exp(4r)-h^2). Use L457's full finite S, including
zero weight at cutoff equality, A=m!/(2r)^m and N=m+1. The prospective
real saddle concerns the complete exponent
H(x)=2rx-N log x+log|zeta(1/2+x+ia)|^2. These are the interface
definitions, not an asserted changed-domain theorem.

The nominal real-part interval is [29/32,15/16]. Its lower endpoint
has distance 280/256 from 2, outside L456's proved radius-273/256
sublinear-logarithm disk. L452's narrower derivative conclusion also
does not cover it. L456's proof has a larger radius-284/256
O(log t) logarithm bound and an outer radius-286/256 zero-free,
pole-free disk. These larger domains are relevant source inputs,
but the O(log t) bound alone is not the needed sublinear estimate.

The attempt must select and justify new intermediate radii between
the Euler-controlled inner disk and the larger logarithm domain,
with fixed positive reserves for the whole changed saddle disk and
Cauchy/Taylor circles. Test a fixed interpolation power p<1 there;
neither a numerical p nor a changed-domain bound is proved here.
The proof must normalize the analytic logarithm by its Euler value,
reflect it correctly for the negative-height factor, and verify strict
clearance from Re(s)=7/8 and the pole. No Euler series left of one
or extension to the zero-free boundary is permitted.

After that test, check one uniform real saddle near N/(2r), curvature
comparable to r and the higher derivative estimates actually needed.
Retain L457's definition
M*=A exp(2rx*) (x*)^(-N)|zeta(1/2+x*+ia)|^2/sqrt(2*pi*H''(x*)).
Its positivity requires positive curvature, upward orientation and the
positive square root; |log M*|=o(r) requires the full factorial
normalization. The old O(r^(2/3)) logarithmic scale is not assumed.

For the complete error, choose a central Gaussian window and verify
its complex Taylor remainder and omitted mass. The shrinking annulus
must retain the quadratic real-part estimate, rather than pay the
global subexponential factor there. Beyond a fixed window, test the
kernel decay against the newly obtained logarithm bound. Recheck the
entire remaining vertical line, both shifted-height-zero neighborhoods
v=+-a and both unbounded rays using L452's all-height formula with
uniform pole clearance. Start inversion on the absolute-convergence
line; retain the two original residues at z=1/2+-ia with their signs.
Justify all finite rectangles and fixed-parameter connector limits
before taking uniform relative estimates. L456/L457's old numerical
tail exponents are precedents, not conclusions on this band.

Continue only if all these terms are o(M*) uniformly with one real-r
onset, M*>0 and |log M*|=o(r). If a reserved disk, derivative scale,
orientation, normalization, residue or complete-complement estimate
fails, record its actual bound against this threshold and stop this
implementation. A local Gaussian calculation alone does not pass.
No sharper relative-freezing claim S/B->1 is part of this approval.

### Duplication, failures and remaining gaps

The exact action was searched using `"zeta" "saddle point" "13/16"`,
`"zeta" "paired" "moving saddle" arithmetic`, and
`"zeta" "logarithmic Riesz" positivity`; the related queries
`"zeta" "Riesz" "moving saddle" positivity` and
`"zeta" "logarithmic Riesz" "positive"` were also screened.
Returned unrelated Riesz criteria, other notebooks and unverified RH
claims were not used as theorem evidence. No matching arithmetic theorem
was inspected; this bounded search establishes no originality or
exhaustive absence. The primary method coverage above, together with
L457's audited local precedent, is the reason for SPECIALIZE.

Scoped local comparison read L452's logarithm/growth proof, L456 and
L457 including the latter's full audit, the earlier assessments and
the relevant recorded failure statements. No prior changed-band
result was located in those paths. L456 parks fixed-center freezing,
not a moving-saddle margin; L331's older shrinking-domain models do
not satisfy the new fixed-disk obligations. L323's r/4 theta-strip
failure and L327's non-PSD/AFE self-reproduction do not supply this
arithmetic margin or its negation. L335's fixed-r/unit-phase negatives
do not locate a negative value at the exact coupled a(r,m). Preserve
all these scope restrictions; no stopped certificate is being retried.

The external premise remains September 30 Theorem 1.1 at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, as registered in
[the external-input note](../../foundations/2026-10-quasi-riemann-input.md).
Its strict half-plane, allowed pole and unaudited manuscript/import
closure remain load-bearing. This review uses neither Liu's stronger
boundary nor a new audit of that premise. Full matching Mathlib and
supporting saddle/interpolation APIs remain unchecked; absence is not
asserted. Success would supply one arithmetic input toward a separately
assessed lower logarithmic-index sign band. Matching theta reduction,
every-height transfer, initial indices, bounded heights, mixed positivity
and selected-law/regulator realization remain independent unresolved
steps. No sign range, zero exclusion or RH conclusion changes here.
