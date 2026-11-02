# Density-derived Peano dual: completed chirp source comparison

TARGET: Assess source coverage for L477's theta-chirp correlation with the Peano-smoothed L574 normalized-density dual.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the bounded exact-weight and standard weighted-oscillatory-integral search below; reused the prior linear-frequency comparison and L319 obstruction. No inspected theorem states this normalized-density chirp bound; this is not a novelty claim.
SOURCE_EVIDENCE: Inspected McKee--Sun--Ye 1601.07887v2 (25 August 2016), Theorems 1.1/1.2, pp. 2--3, Section 2's interval split and Section 3's outer/central/boundary cases; and Blomer--Khan--Young 1203.2573v2 (22 February 2013), Lemma 8.1, Proposition 8.2, Corollary 8.3 and their proofs, pp. 19--22. Reuse L574's audited finite density input and C481a's de Boor import; no new source-proof audit.
COMPARISON: Finite-interval weighted derivative estimates provide a concrete tool for testing the exact amplitude with boundary terms retained. Smooth compact-support stationary expansions have additional amplitude-scale restrictions and retain a stationary main term; neither source supplies denominator-weighted aggregate cancellation. The earlier linear-frequency mismatch is unchanged.
GAP: Quantify the exact multiplier's piecewise regularity and derivative/variation costs, check actual phase separation or retain exceptional intervals, sum the complete ordered-pair bound, and compare with c T(log T)^3/2. The weighted Peano/Fubini transfer also remains to be proved. No leakage bound, full-residual lower bound or Xi sign is established.
REASON: Approve one bounded hypothesis-and-loss test with accessible primary tools, not import of the desired conclusion. All amplitude bounds and phase cases must be proved in that attempt; failure to reach the threshold parks this direct estimate rather than authorizing unsupported cancellation or repeated source searches.
SCOPE: Exact L477 R_T=U_T+V_T and theta, arbitrary sufficiently large real T, fixed M=floor(sqrt(T/(2pi))), h=1/log T, J=[T+h,2T-h], and L574 g_T=D_h/Q_T. Complete ordered sums, all cutoff transitions and boundary strips; no RH, simplicity, independent phases, Haar replacement, bounded projection or discarded block.
COVERED_TARGET: Test the Peano-smoothed L574 dual against L477's complete theta-chirp using finite-interval weighted derivative estimates with all boundary losses retained.

## Original nomination, preserved; approval status superseded above

The main gap is actual-Xi all-degree positivity and unbounded-height
initial signs. The next independent gap here is cancellation between
L477's two residual components. A reliable full-scale residual lower
bound would obstruct the selected fixed-square little-o defect route;
it would not disprove RH, prove a Xi sign or save negative mass.

The candidate multiplier to be assessed is, for x in [T,2T],

    psi_T(x)=-h^(-2) integral_J (h-|x-t|)_+ g_T(t) dt,
    g_T(t)=D_h(t)/Q_T(t),

with exactly L574's definitions. Retain the entire chirped component

    V_T(x)=sum_(n,m<=M) log(n/m)^2/sqrt(nm)
                         cos(2 theta(x)-x log(nm)).

The proposed discriminating test is whether sources support an eventual
bound

    |integral_T^(2T) V_T(x) psi_T(x) dx|
          <=(c/2) T(log T)^3,
    c=sin(1/32)^4 log(2)^2/512,

or a uniform little-o bound at this scale. Neither bound is established.
A future argument would also need to verify the multiplier's bound and
its exact Peano/Fubini pairing with U_T, matching the audited positive
density input before drawing a full-residual conclusion. This file
proposes those obligations; it does not perform that derivation.

Essential input IDs for that future work are L477, C481a and L574.
L573 is unnecessary. The two unconditional imported source theorems in
L574 retain their unaudited-source-proof qualification. No cross-notebook
input, effective onset or Mathlib coverage is available by assertion.
Full matching and supporting Mathlib coverage remain unchecked.

## Three mechanisms compared for recovery

1. A separate L573 cap-loss audit is independently decidable with ready
   finite mean-square tools, but concerns concentration rather than the
   remaining two-phase cancellation. L574 does not require it.
2. Repeating the generic Littlewood/linear-frequency source import stays
   blocked: its construction supplies no theta-chirp cross correlation.
   Its exact failure is preserved in
   `ATTEMPTS/2026-10-31-constructive-ratio-chirp-dual-source-stop.md`.
   The L572 short-interval certificate stop remains unchanged as well.
3. The explicit normalized-density-derived smoothed multiplier above
   now has a specific audited actual-height density input. This is a
   different correlation to assess, not a claim that the older theorem
   has acquired a curved-phase extension. Select this source review.

The older actual-phase stationary-involution stop also remains: a small
transform error can simply transfer the unsigned main form. No automatic
sign or aggregate cancellation can be inferred from stationary phase.
The proposed multiplier has no sign jumps, but no uniform derivative or
Fourier-decay bound is asserted; its positive denominator depends on T.
Those quantitative obligations may themselves block the test.

Continue only if primary hypotheses and relevant proof cases cover a
concrete test of this exact weighted integral, or identify a specific
remaining difference with an adequate EXPLORE assessment. An accessible
linear-phase theorem or an unevaluated bounded multiplier is insufficient.
If the proposed threshold requires unsupported denominator control,
stationary cancellation or negligible discarded mass, record that precise
blocker and park the target. Do not repeat the same scalar-dual search.
Missing essential coverage requires literature-only work, no new lemma
or mathematical script. This nomination does not approve its own target.

## Completed source review, 31 October 2026

The separate literature-only turn has now performed the required search
and primary comparison. The EXPLORE decision covers exactly the
COVERED_TARGET above. It does not approve the desired bound as a known
result. The supervisor retains its separate next-turn continuation
approval; this file records source readiness and a recommendation.
No mathematical calculation, new transfer, lemma or script was
produced in this source review. The main gap and the proposed downstream
use are those in the preserved nomination.

### New primary evidence

**McKee--Sun--Ye**, *Weighted stationary phase of higher orders*,
[arXiv:1601.07887v2](https://arxiv.org/html/1601.07887v2),
Theorems 1.1/1.2, printed pp. 2--3. Theorem 1.1 requires real
f in C^(n+2), g in C^(n+1), positive scale parameters M,N,T,U,
M>=beta-alpha, |f^(r)|<=C_r T/M^r (2<=r<=n+2),
|g^(s)|<=C_s U/N^s (0<=s<=n+1), unchanged signs of f',f'',
and positive min|f'| for a finite bound. It retains the boundary
recursion (1.2); errors depend explicitly on min|f'| and amplitude
scales. Theorem 1.2 instead needs f in C^(2n+3), g in C^(2n+1),
n>=2, the analogous derivative bounds, f''>=T/(C_2 M^2), one
interior negative-to-positive crossing, and T^(1/(2n+3))Delta>1
with Delta in (1.7). Its (1.8) includes inverse endpoint distances.
Read the three-interval split in Section 2, outer first-derivative
case (3.1)--(3.2), central quadratic integral and final matching of
boundary recursions in Section 3. This is a finite-endpoint tool;
Theorem 1.1's proof is referred to prior sources, not supplied there.

**Blomer--Khan--Young**, *Distribution of mass of holomorphic cusp
forms*, [arXiv:1203.2573v2](https://arxiv.org/html/1203.2573v2#S8),
printed pp. 19--22. Lemma 8.1 requires a smooth compactly supported
weight with w^(j)<<_j X U^(-j), |h'|>=R>0, and
h^(j)<<_j Y Q^(-j), j>=2, with Y>=1 and positive X,Q,U,R.
Its bound is (beta-alpha)X[(QR/sqrt(Y))^(-A)+(RU)^(-A)].
Proposition 8.2 also requires 0<delta<1/10, Z=Q+X+Y+V_1+1,
Y>=Z^(3delta), V_1>=V>=Q Z^(delta/2)/sqrt(Y),
w^(j)<<_j X V^(-j), a unique critical point,
h''>>Y/Q^2 and h^(j)<<_j Y Q^(-j), j>=1.
It gives a stationary expansion with a weight-dependent leading
term; Corollary 8.3 localizes it rather than cancels it. Read the
Lemma 8.1 integration-by-parts recursion and the Proposition's
outer localization, quadratic/Fourier expansion and derivative-cost
cases. These results have no arithmetic denominator hypothesis.

These are inspected supporting theorems, not matching theorems for
the proposed integral. Their proofs remain unaudited. Use their stated
results by citation if their hypotheses can be verified; no reproof is
needed. Matching or supporting Mathlib coverage remains unchecked.

### Applicability obligations and bounded mathematical continuation

The exact weight is the one displayed in the preserved nomination,
with its real-height, fixed-cutoff denominator from L574. That lemma's
Q_T>=log T and |g_T|<=1 are established inputs. They do not supply
quantitative derivative costs. Triangle smoothing is not permission to
assume the all-order flatness conditions of the compact-support source.
The continuation must determine differentiability on the actual pieces
of [T,2T], including where the kernel support meets J's endpoints.
It may partition there and use the finite-endpoint theorem with every
new boundary term retained. It may instead justify the corresponding
finite integration-by-parts identity directly as ordinary calculus;
that is an applicability calculation, not a reproof of stationary phase.

Use the exact phase (2theta(x)-x log(nm))/(2pi) when invoking the
source convention e(f)=exp(2pi i f). Check its derivative signs and
minimum magnitude for each retained range. No uniform positive gap
is assumed. Where a first-derivative hypothesis fails or degenerates,
retain and bound the entire exceptional integral. The stationary
expansion is only an alternative after its additional hypotheses and
endpoint-distance errors have been checked; it is not a substitute
for a bound on that contribution. Do not insert an external Fourier
mode into the phase without accounting for its coefficient and the
full new stationary-point analysis.

The denominator is not a finite coefficient vector to which the
reused mean-square theorem applies directly. Any polynomial or Fourier
replacement needs a complete approximation-error estimate, including
its pairing with V_T. No such replacement is preapproved. Equal
products and zero log(n/m) coefficients must be retained correctly;
termwise estimates may avoid arithmetic cancellation, but their full
coefficient budget must be paid. All constants used to claim a uniform
estimate must be independent of sufficiently large real T. No floor
derivative, negligible boundary strip or effective onset is available
by assertion.

The first task in that one mathematical attempt is to verify the
proposed bounded multiplier and its exact weighted Peano/Fubini
pairing with U_T, with the sign and h^(-2) normalization checked.
Then produce a rigorous complete upper estimate for
|integral V_T psi_T| from these derivative tools. Compare its actual
scale and constants to c T(log T)^3/2 with the exact L574 c above.
A little-o bound also passes. A bound of order T(log T)^3 with an
unspecified constant does not pass the fixed-constant test.

If amplitude costs or exceptional intervals prevent that threshold,
record the actual rigorous estimate and the specific loss, and park
this direct derivative implementation. That would not refute the
correlation bound or RH. Do not repeat the old linear-dual retrieval,
claim a stationary main term is small without proof, or continue by
assuming denominator decorrelation. A further mathematical attempt
would require a materially new input or a refined independently
testable mechanism. L573's separate audit remains available as a
different task, not an input or an instruction to perform it now.

### Search, overlap and remaining source scope

New queries (31 October 2026) included `stationary phase weighted
amplitude derivative uniform asymptotic Blomer Khan Young lemma inert`,
`Riemann Siegel Dirichlet polynomial normalized nonlinear weight
oscillatory integral ratio absolute square`, `"Dirichlet polynomial"
"nonlinear" "weight" "stationary phase"`, `"Dirichlet polynomial"
"reciprocal" "weighted" "mean"`, `"Dirichlet polynomials"
"nonlinear weights"`, and `"Dirichlet polynomial" "stationary phase"
"denominator"`. Exact-context queries involving Riemann, normalized
density, chirp and Peano dual returned unrelated terminology and were
not mathematical evidence. Secondary summaries, notebook-like web
hits and search snippets were not imported. No novelty inference is
made from the absence of a matching result.

The earlier constructive-dual assessment remains adequate for its
linear-frequency sources; they were not retrieved again. L319's
stationary involution and L481/L482/L572 stops remain unchanged.
The new source comparison adds finite-endpoint weighted tools and
their explicit applicability tests. The source texts are accessible;
the desired cancellation is an open mathematical difference, not an
access blocker. The bounded test can check that difference without
assuming it, so EXPLORE is appropriate. No theorem establishing the
exact normalized-density chirp correlation has been identified or
imported. No claim about full-residual mass, either defect threshold,
negative mass, Xi signs, or a complete RH candidate follows.
