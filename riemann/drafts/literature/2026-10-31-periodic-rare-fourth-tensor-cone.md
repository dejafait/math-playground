# Periodic rare trajectories: leading-fourth cone test

TARGET: Test whether L473's full leading fourth tensor has positive bounded-periodic C2 occupation representations with uniformly bounded total weight and second-moment cost.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Prepared within the bounded-periodic compensation review; its recorded prescribed-derivative-moment, occupation/holonomic, cubature and Hardy random-trigonometric searches found no inspected matching construction or global separator. This does not establish novelty.
SOURCE_EVIDENCE: Directly verified https://arxiv.org/pdf/math/0502473v2 (Corollary 2/Remark 2 and pushforward proof, pp.3--4), https://arxiv.org/pdf/math/0701451v2 (Definition 28, Lemmas 29--30, Theorem 31, pp.17--19), and https://web.stanford.edu/class/ee364a/lectures/duality.pdf (slides 5.34--5.35, PDF pp.36--37); reuse the completed occupation comparison and L473/L578/L579/L581--L584 scope restrictions.
COMPARISON: Existing cubature requires feasibility, finite LP alternatives apply only to a certified finite dictionary, and first-velocity closure supplies no bounded C2 lagged fourth tensor. L473's rare atoms and covariance map need not respect dynamics. Packet and exact-law stops do not settle this changed leading-tensor target.
GAP: No positive periodic-path representation of all 126 q_m with uniformly bounded weight/cost is established. Even success leaves positive trajectory-based second completion, clipping and actual-Xi transfer unresolved.
REASON: A bounded new mechanism replaces rare jet atoms by entire trajectories instead of imposing the stopped absolute exceptional-energy budget. Separate literature approval on 2026-10-31 verified the direct sources and retained EXPLORE for the unchanged exact target; no representation or separator is imported.
SCOPE: Real periodic C2 paths, ordinary derivatives, lags 0 and 1, the complete real leading tensor q_m from L473 (9), positive finite weights, uniform bounds for real ell on one eventual ray. No import of full feasibility, compactness, spectral equality, finite-Hardy stationarity or the exact law nu_H.

## One proposed mathematical test, not a result

The main gap remains actual-Xi all-degree signs at unbounded heights.
This intermediate target concerns the bounded stationary support
interface. Its plausible use is a derivative-consistent replacement
for the rare quartic carrier in L473; it need not settle independent
second-moment completion or positive clipping to be informative.

For a real P-periodic C2 path h, P>0, write

    J_h(s)=(h(s),h'(s),h''(s),h(s+1),h'(s+1),h''(s+1)),
    T_m(h)=P^(-1) integral_0^P product_a J_h(s)_a^m_a ds,
    C_2(h)=P^(-1) integral_0^P |J_h(s)|^2 ds.

The proposed feasibility test is the existence of fixed finite
W,C,C_2^*,ell_0 such that, for every real ell>=ell_0, some finite
list of paths h_(ell,i), periods P_(ell,i)>0 and weights a_(ell,i)>=0
satisfies all of

    sup_s |J_h_(ell,i)(s)|<=1 for every used path,
    sum_i a_(ell,i)<=W,
    sum_i a_(ell,i) C_2(h_(ell,i))<=C_2^*,
    max_(|m|=4) |sum_i a_(ell,i) T_m(h_(ell,i))-q_m|<=C/ell.

These are the proposed thresholds, not proved conclusions. No bound
on the number of paths, uniform period, common frequency cutoff or
attainment in a C2 closure is assumed. Exact representation by a
fixed positive finite mixture would pass the stated approximation
test, but none has been supplied. L473 (9) specifies every q_m,
including lag allocations and odd-total-order coefficients; omitting
vanishing or cross entries is not permitted.

The contemplated later amplitude and weight choices are ell^2 h
and ell^(-4)a. Their probability normalization, support and all
moment consequences must be proved during research, not inferred
from this nomination. The hard part to attempt is the simultaneous
positive trajectory representation of q with the uniform weight bound.
Do not count the formal amplitude substitution as a successful test
if that representation remains assumed.

## Available sources and exact restrictions

The preceding completed comparison contains precise primary links,
versions, hypotheses and proof cases; reuse it without a repeat
literature turn unless this scope changes. Bayer--Teichmann's
conditional compression can shorten a feasible measure's observables;
it cannot create this measure. The inspected finite LP alternative
can certify a particular dictionary's failure. It does not certify
failure over all paths. Bernard's approximation does not preserve
the required lagged full-jet support or quantitative fourth errors.
None of these named inputs is to be reproved as a new discovery.

L473 (6),(9) and (14)--(18) are essential mathematical inputs for the
reference tensor and comparison, with the existing Bettin/Bui--Hall
qualifications. Bui--Hall Proposition 3's proof remains imported and
unaudited. L582's ordinary lagged-jet convention is reused. L581 and
L578/L579, and L583/L584, are scope contrasts rather than premises
of an unproved representation. No new arithmetic estimate is needed
for this tensor test. The Arguin--Creighton qualification remains
attached to the prior budget stop, not a new input here. Matching
Mathlib coverage is unchecked; no cross-notebook input is proposed.

## Continue or abandon

One coherent attempt should construct a candidate occupation measure
and prove all displayed bounds, or seek a finite-coefficient quartic
functional with a strict gap between q and every admissible path's
occupation tensor, accounting for allowed weight and approximation
errors. A certified failure of a chosen finite dictionary is narrower
evidence and must be labeled that way. No numerical fit, preview or
assumed convex-hull membership counts as verification.

Retain a constructed uniform carrier or a genuine global separating
inequality as decisive evidence. Abandon the attempted mechanism if
it merely repeats the fixed packet stop, presupposes a path extension
of L473's atoms, loses uniform weight, or uses L583's failed absolute
fourth budget under another name. Save partial reasoning; a failed
creative attempt requires a new input or refined test before repeating.
No result on q, no new lemma and no mathematical script was produced
by the literature turn that wrote this assessment. The separate
source-approval turn below completes the required review.

## Separate direct-source approval, 31 October 2026

This literature-only recovery repairs missing direct URLs, without
changing TARGET or SCOPE. Reused the completed occupation comparison,
its recorded searches and local failure comparisons. Read L473's full
fourth formula (9) and L582's jet convention to check scope; no tensor
calculation or new specialization was performed.

Bayer--Teichmann, *The proof of Tchakaloff's Theorem*, v2 (4 May
2005), [Corollary 2, Remark 2 and proof, pp.3--4](https://arxiv.org/pdf/math/0502473v2#page=3):
the positive measure must already exist on a measurable space,
be concentrated on a measurable A, and have an integrable finite
observable map. Positive finite cubature reproduces those observables;
the constant observable preserves finite mass. The proof lifts
pushforward atoms back to A. This supplies no path-space feasibility
or uniform-weight bound for the prescribed q. No reproof is needed.

Bernard, *Young measures, superposition and transport*, v2 (9 July
2008), [Definition 28, Lemmas 29--30 and Theorem 31, pp.17--19](https://arxiv.org/pdf/math/0701451v2#page=17):
for compact connected M, closed measures equal the closure of smooth
integer-periodic tangent occupation measures in the stated transport
topology. Checked the W1,1 smoothing and the convexity proof's geodesic
joins. Neither supplies bounded second derivatives, lag-one joint
observables, nor quantitative quartic errors. Thus this theorem is a
comparison, not an import proving the target. No audit of its full
proof is claimed.

Boyd--Vandenberghe, slides revised with Nobel,
[slides 5.34--5.35](https://web.stanford.edu/class/ee364a/lectures/duality.pdf#page=36),
retrieved 31 October 2026: finite Ax=b, x>=0 has strong alternative
A^T nu>=0, nu^T b<=-1. The next slide states Farkas' homogeneous
alternative and its LP-duality proof. This justifies a certified finite
dictionary test only; it supplies no separation over every periodic
path or closure/attainment theorem for this target.

Decision remains EXPLORE, not IMPORT or a novelty claim. The existing
arithmetic-source qualifications, unresolved positive second completion,
clipping and Xi transfer remain. Matching Mathlib coverage is unchecked.
The stated all-126-entry uniform carrier or strict global separator is
the unchanged decisive test. No additional source blocker was found;
the next turn can attempt the approved mathematics. This URL/approval
repair itself is STALLED as mathematical evidence.
