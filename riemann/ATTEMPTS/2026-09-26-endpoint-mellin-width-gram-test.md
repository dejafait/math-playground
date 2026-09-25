# Endpoint Mellin-width Gram test — 2026-09-26

Gap: L350 leaves H_N(1)=o(1), equivalently its normalized
sampling-operator bound, unproved at the prescribed endpoint
heights. Even that bound would only give a vanishing discrete
mean; exceptional indices, the pointwise endpoint margin and the
remaining low Laguerre signs would still be unresolved.

Intermediate target: retain L350's maximum weights and actual
height gaps, and test the collision diagonal and a local common-
dilation average of H_N(θ). Here G_N^θ(n,m) is obtained by
replacing a_n−a_m by θ(a_n−a_m), with the weights unchanged.
Seek an O(1/N) average on an explicit shrinking θ interval,
uniformly in its position. This would establish that these weights
permit a small sampling norm for most nearby dilations and isolate
the exceptional-dilation problem. It would not put θ=1 outside
that exceptional set or preserve the exact endpoint height-index
relation at θ≠1. Continue this intermediate test if both the
collision mass and the integrated off-diagonal error reach O(1/N);
abandon this implementation if either budget stays bounded away
from zero. A deterministic inference must be checked separately.

Redundancy review: the shared and local goals, full proof overview,
local DAG and current checkpoint were read; tracked and untracked
work was inspected and preserved. L344–L345 stop the tested
fixed-order sample-index derivative certificates. L346 concerns
unweighted full-support sampling, and L347–L348 concern a different
normalization with diverging mass. L349–L350 remove those mass and
variation obstructions but do not estimate the present Gram
matrix. L333 supplies a continuous-height harmonic-sum estimate,
not a statement about this moving maximum-weight matrix. Searches
found no previous common-dilation Gram estimate. No historical
stop is being treated as a prohibition on this distinct test.

Unfinished reasoning saved before the proof: L349's pointwise
coefficient remainder appears to imply
||w_N−γ/sqrt(2N)||_2=O(1/N), where γ is its nonnegative
axial von Mangoldt sequence. Hence Σw_N² should be
C_w/(2N)+O(N^(-3/2)), although Σw_N has positive lower
limit. With σ_N=1+1/(2sqrt(N)), the divisor formula also gives
w_N(p,q)≤C τ(p)τ(q)/(pq)^σ_N. Grouping products into
log(k/l) then suggests the inverse-gap budget O(N^(17/2)),
using L333's positive d_4 harmonic-sum estimate.

Integrating exp(iθ(a_n−a_m)log(k/l)) over an interval of
length T costs at most 2/(T|a_n−a_m||log(k/l)|).
The exponential sample gaps should give
Σ_(n≠m)|a_n−a_m|^(-1)=O(exp(−4N)), not N² times
this amount. After normalization, the proposed error is
O(N^(13/2)exp(−4N)/T); T≥N^8 exp(−4N) would make
it O(N^(-3/2)). All equal-frequency collisions, the maximum
over samples, infinite sums and the distinction from θ=1 still
need checking. No conclusion is asserted at this saved stage.

Completed assessment — 2026-09-26: ADVANCE.
[L351](../lemmas/L351-endpoint-mellin-width-local-gram-average.md)
proves both the maximum-weight square-norm asymptotic and the
proposed uniform local average. The exact mean is
1/N+(1−1/N)B_N/W_N² with error
O(N^(13/2)exp(−4N)/T), where
B_N=C_w/(2N)+O(N^(-3/2)). Thus T≥N^8 exp(−4N)
attains O(1/N), not just boundedness. This is a partial sampling
input; the original deterministic H_N(1)=o(1) is neither proved
nor refuted. It is not classified as an advance on endpoint signs.

Continue the weighted sampling investigation at the deterministic
arithmetic question. The exact nonnegative frequency-side formula
reduces a sufficient test to vanishing weight of frequency pairs
with |C_N(ω_ν−ω_μ)|>N^(-1/8). A fourth moment of these
correlations that is o(N^(-1/2)) would suffice by Markov's
inequality. This is a proposed test, not an established estimate;
its true equal-frequency contribution is O(1/N) by the new bound.
The earlier fixed-order derivative failures remain relevant.

WHY THE AVERAGE DOES NOT COMPLETE THE TARGET: a set of small
Lebesgue measure in the auxiliary dilation can contain the exact
value 1 for every N. Even this actual Gram family has H_N(0)=1
while satisfying the same uniform local-average theorem there.
No pointwise inference from measure and continuity is justified.
Dilated samples also lose the prescribed endpoint height-index
relation. The main positivity gap, exceptional indices and every
established sign/exclusion range are unchanged; no RH candidate.
Zero consecutive unresolved exploration turns remain.

Analytic review checked the coordinatewise maximum before taking
its square norm, the positive divisor majorant, every reduced-ratio
collision, convergence of the inverse-frequency-gap sum, uniformity
in the interval position, the exact exponential sample-gap bound,
and both independent diagonals in the mean. The check
`python3 scripts/laguerre/check_endpoint_gram_collisions.py` passes
24 exact finite collision, Gram/correlation and constant-term
identities; six repeated-sample cases check the diagonal count.
These checks use formal prime-log frequencies, not actual a_n,
and do not certify the analytic estimates or sampled signs. Full
Mathlib coverage is not checked; inherited supporting names and
links keep their qualifications. All earlier work is preserved.
