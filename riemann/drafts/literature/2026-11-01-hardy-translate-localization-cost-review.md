# Inverse Hardy-translate localization: completed source review

TARGET: Assess primary-source coverage for an inverse Hardy-translate localization test: determine the total-variation coefficient cost of approximating a normalized width-1/log T bump on the L622 window, and whether that cost can fit the complete shifted-moment error budget.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded searches for actual-Hardy translate approximation, atomic/TV duality, quantitative Runge and local Fourier/Riemann--Siegel obstructions; full queries and access outcomes are in drafts/2026-11-01-hardy-translate-localization-source-working.md. Narrow checks of L620, L622, L636 and the recorded theta/Runge stops found no duplicate exact cost statement. Search failure is not evidence of novelty.
SOURCE_EVIDENCE: Read Hughes--Young arXiv:0709.2345v2 Theorem 1.1/(11)--(17), printed pp. 3--5; Chandrasekaran et al. arXiv:1012.0621v3 Section 2.1/(2)--(3), p. 5; Bodmann--Flinth--Kutyniok arXiv:1803.04218v1 Sections 2.1--2.2, Definition 2, Lemma 1 and Proposition 1 with full proof, pp. 6--8; DLMF 25.10.1--3 including the remainder and cutoff; Hughes July 2017 LMS notes Theorem 2.2 and its explicitly heuristic reduction, pp. 18--19; Tuck (2005), (7), (19)--(22), pp. 326--328. Exact qualifications below.
COMPARISON: None of the inspected theorems gives C_(T,X). Atomic duality suggests a lower-certificate method, but finite-dimensional and unit-kernel assumptions cannot be silently transferred. The named real-axis Riemann--Siegel formula supplies a quantitative remainder, not exact bandlimitation. Hughes--Young supplies uniform per-product errors, not inverse realization or a bound in the present TV norm.
GAP: Construct and estimate a weighted-window dual certificate for the exact bump and every |s|<=1 atom; justify the full TV-squared moment-error accounting, including curvature and complex orientations. No C_(T,X) bound, density, signed approximation control or growing-observer positivity has been established.
REASON: Essential named inputs for a bounded Fourier-filtered dual attempt are available; no exact matching inverse-cost theorem was identified. Park the inaccessible high-order sources and mismatched generic approximation theorems. The continuation needs a separate approval turn; this literature step does not execute or certify its mathematics.
SCOPE: The exact fixed bump, L2 tolerance 1/4, unnormalized Hardy atoms, finite complex measures with |s|<=1, no amplifier, fixed w,u0 and X-uniformity defined below. Approves source coverage for a bounded cost diagnostic only; no lemma or mathematical script was written in this literature turn.

## Completed comparison — 1 November 2026

Outcome EXPLORATION, classification NOVELTY_UNCHECKED. The new source
comparison identifies a concrete test but no mathematical cost bound or
known overlap that settles it. Mathematical exploration usage is unchanged.
The invocation-start nomination is preserved below as historical scope.

### Inspected inputs and limits

1. C. P. Hughes and M. P. Young, *The twisted fourth moment of the
   Riemann zeta function*, J. reine angew. Math. 641 (2010), 203--236,
   [v2 Theorem 1.1/(11)--(17), pp. 3--5](https://arxiv.org/pdf/0709.2345v2#page=3).
   The retrieved PDF identifies v2, 27 September 2007, compiled
   26 November 2024. The theorem assumes coprime h,k,
   hk<=T^(2/11-epsilon), complex shifts O(1/log T), nonnegative smooth
   weight supported in [T/2,4T], all fixed derivative bounds
   O_j(T0^(-j)), and T^(1/2+epsilon)<<T0<<T. The raw remainder is
   O(T^(3/4+epsilon)(hk)^(7/8)(T/T0)^(9/4)). Its complete six-term
   main expression is holomorphic at shift collisions (p. 5 remark,
   citing CFKRS Lemma 2.5.1). Reuse L622's audited exact-phase,
   complex-weight and Cauchy application; do not reprove the manuscript.
   No bound on inverse coefficients occurs in this statement.

2. V. Chandrasekaran, B. Recht, P. A. Parrilo and A. S. Willsky,
   *The Convex Geometry of Linear Inverse Problems*, Found. Comput.
   Math. 12 (2012), 805--849,
   [arXiv:1012.0621v3, Section 2.1/(2)--(3), p. 5](https://arxiv.org/pdf/1012.0621v3#page=5).
   Read the compact-atom subset of R^p hypothesis, extreme-point
   convention, nonnegative-coefficient gauge representation,
   central-symmetry qualification and support-function formula. These
   identify standard terminology. Finite-dimensional recovery or
   Gaussian measurement results do not apply to this T-dependent
   Hilbert-space dictionary. No inverse-cost asymptotic is imported.

3. B. G. Bodmann, A. Flinth and G. Kutyniok, *Compressed Sensing for
   Analog Signals*,
   [arXiv:1803.04218v1, Sections 2.1--2.2, pp. 6--8](https://arxiv.org/pdf/1803.04218v1#page=6).
   The fetched artifact is dated 31 August 2021 on its title page;
   the v1 identifier is retained to make the source reproducible.
   Definition 2 uses a separable RKHS of Borel functions on a locally
   compact Hausdorff space with a unit-norm kernel, allowing complex
   regular Borel measures. Lemma 1 additionally assumes second
   countability and density of H intersect C0, and proves attainment.
   Proposition 1 and its complete proof identify the dual norm as
   sup_x |g(x)| via the integral pairing and Dirac atoms. Read also
   the warning that normalization transfers weights. The present
   Hardy atoms are unnormalized; replacing them by unit vectors
   would change the stipulated TV cost. Neither attainment nor
   strong duality is needed for a later finite-sum lower certificate.
   The required elementary weak-duality specialization must be
   written with the present weighted inner product; it is not an
   application of a sparse-recovery theorem.

4. The standard named Riemann--Siegel formula, Titchmarsh,
   *The Theory of the Riemann Zeta-Function*, 2nd ed. (1986),
   Section 4.17/(4.17.4), p. 89, is explicitly stated in the inspected
   [NIST DLMF 25.10.1--3](https://dlmf.nist.gov/25.10#E3)
   (version 1.2.8, 15 September 2026). For positive real t tending
   to infinity it reads

       Z(t)=2 sum_(n<=floor(sqrt(t/(2pi))))
                    n^(-1/2) cos(theta(t)-t log n)+O(t^(-1/4)).

   Its exact Hardy/gamma normalization and integer cutoff were read.
   C. Hughes's author-hosted [July 2017 LMS notes, Theorem 2.2,
   pp. 18--19](https://personal.maths.manchester.ac.uk/jm/wiki/uploads/LMS/Hughes-lectures.pdf#page=20)
   independently state the same formula and phase (2.1), then label
   their AFE reduction heuristic. The classical named theorem is
   the import; the lecture sketch is not a new rigorous proof.
   No differentiated remainder, constant-frequency representation,
   exact bandlimitation or Fourier-tail estimate is supplied.

5. E. O. Tuck, *Riemann--Siegel sums via stationary phase*, Bull.
   Austral. Math. Soc. 72 (2005), 325--328,
   [publisher PDF, (7), (19)--(22)](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F177CA78EE9240A1AE1C22380338CD5B/S0004972700035115a.pdf/riemannsiegel_sums_via_stationary_phase.pdf).
   Read the statement and stationary-phase cases, including the
   cutoff when the stationary point leaves the integration range.
   This does not supply the present weighted dual estimate; no
   uniform summed or differentiated remainder is imported from it.

The earlier Runge assessment's Ruland--Salo Theorems 2--3 concern
elliptic solutions in nested bounded domains and boundary Sobolev
cost, while the superoscillation sources allow other bandlimited
functions. Reuse those inspected scope comparisons; they do not
realize translates of the actual Z with this TV cost. The theta
translate stop concerns a different kernel and qualitative density.
No conclusion about actual Z follows from those failed constructions.
No full matching Mathlib theorem was checked; availability is unknown.

### Required moment-error scale: source comparison, not a new theorem

There is no Dirichlet amplifier: the source application has h=k=1,
T0=T and epsilon=1/100. Its undifferentiated, exact-phase per-product
raw error is O_w(T^(19/25)), uniformly for bounded scaled complex
shifts. The proposed observer quadratic uses pairs (s_j,s_k), not
just two Euclidean channels. All complex orientations and all m^2
pairs must remain, weighted by c_j conjugate(c_k). The source remark
about summing errors and L622's finite coefficient accounting are
the relevant precedents. A bound stated only for each fixed m, or
an error constant growing silently with m, is insufficient.

The exact expression nominated for verification in research is

    E_T(C)=C_w C^2 [T^(19/25) L^2 + T^(-1) L^4],
    C=sum_j |c_j|,  L=log T.                         (TEST, UNPROVED HERE)

It is a proposed *raw absolute error envelope*, retaining the
complete exact-phase source main term. The first term must account
for the two ordinary derivatives and TV pair sum; the second must
account for W's gamma curvature using the shifted mixed fourth
moments. In the old T L^6 normalization the proposed expression is
C_w C^2[T^(-6/25)/L^4+T^(-2)/L^2]. This is the unamplified
comparison to check, not L636 (5)'s coefficient-Euclidean budget.
No new arbitrary-measure transfer theorem or proof was derived
this turn; finite-sum specialization and uniformity are explicit
obligations of the continuation. Freezing the phase would require
additional errors and is outside this proposed accounting.

Even making this envelope o(T L^6) is only a coarse diagnostic.
A unit-L2 bump does not have the size of a globally unnormalized
Hardy observer, so an eventual signed local witness needs its own
signal scale. A lower cost that makes this sufficient envelope
unusable would stop this absolute-budget certificate; it would not
lower-bound the true remainder or exclude cancellation-sensitive
methods. L2 error alone supplies neither weighted signed control
nor positivity of the complete continuum observer kernel.

### One bounded continuation and its discriminating test

The selected mechanism is a Fourier-filtered *dual* localizer,
rather than constructing more forward observer blocks. Search for
a test vector q_(T,X) in L2(w_XT dt) whose pairing with the saved
g exceeds (1/4)||q|| by a fixed positive margin, but whose pairing
with every Z(.-s/L), |s|<=1, is small. Either shift sign describes
the same allowed dictionary. The intended correlation scale to
test is O_w(T^(-1/4)/sqrt(L)), with bounded ||q||; this is a
conjectured test threshold, not a consequence asserted above.
The corresponding TV lower bound and the complete E_T comparison
must be proved subsequently, without assuming atom-count control.

An admissible design may remove a fixed frequency band in the
microscopic variable x=L(t-a). It must handle Fourier-filter tails,
the smooth weight (including its zeros away from u0), phase
variation, both cosine orientations, the integer cutoff and the
undifferentiated Riemann--Siegel remainder. Exact bandlimitation
cannot be assumed. Plancherel and elementary integral duality are
standard inputs; no spectral gap or localized-Z theorem is imported.
Reproving the elementary finite-sum pairing is justified only to
preserve the unnormalized dictionary and finite atomic definition,
not to claim novelty in duality or Fourier uncertainty.

Continue only if a certificate with overlap above the tolerance
and X-uniform correlations produces a cost bound discriminating
against the proved absolute error envelope. If the overlap or
uniform correlation estimate fails, retain the failed construction
and stop this particular filter test. Do not replace missing bounds
by numerical sampling, density, or a statement about another kernel.
Effective heights, signed approximation, observer positivity and
all-degree mixed positivity remain independent gaps.

The ready but unapproved continuation is saved separately in
`2026-11-01-hardy-translate-dual-test-scope.md`. Its separate approval
is required before research execution; completion of this source
review asserts no new theorem or mathematical outcome.

## Invocation-start nomination (historical text retained below)

## Exact proposed test, with no asserted estimate

Retain L622's actual zero-safe Z, fixed smooth w>=0 of integral one,
L=log T, T<=X<=2T, and w_XT(t)=w((t-X)/T). Choose once and for
all u0 in (0,1) with w(u0)>0. Fix the nonzero smooth bump

    psi(x)=exp(-1/(1-4x^2)) for |x|<1/2, and 0 otherwise.

Let a=X+u0 T and normalize

    g_(T,X)(t)=psi(L(t-a))/||psi(L(.-a))||_(L2(w_XT dt)).

For an arbitrary finite atomic complex measure
mu=sum_(j=1)^m c_j delta_(s_j), with distinct s_j in [-1,1], set

    U_T mu(t)=sum_(j=1)^m c_j Z(t+s_j/L),
    ||mu||_TV=sum_j |c_j|,
    C_(T,X)=inf {||mu||_TV : ||U_T mu-g_(T,X)||_(L2(w_XT dt))<=1/4}.

The infimum is +infinity if there is no admissible finite sum.
There is no Dirichlet amplifier in this proposed test. The number
of translates is unrestricted in the definition, so a source proving
only fixed-dimension interpolation is insufficient. All coefficient
costs must be measured in this norm and all asymptotic statements
must specify uniformity in X. These definitions select a later
test; they prove no density, cost bound, obstruction or transfer.

The proposed mechanism is to compare the inverse approximation cost
with the error after summing all translated fourth-moment products.
A useful source must give a quantitative upper construction or a
lower cost bound (for example through a dual singular-value estimate),
not merely a statement of dense translates. The review must identify
the precise source-error scale for this larger family rather than
copying the two-channel Euclidean estimate (5) of L636. Dependence
on the number of atoms, total variation, window and shifts matters.

Continue to a mathematical test only with enough coverage to seek
a coefficient-cost bound that discriminates against that error scale.
If known lower bounds already exclude the needed budget, import and
specialize them instead. If no quantitative source applies, identify
the exact missing estimate and decide whether a bounded dual test
has independent justification. Do not restart a sequence of
qualitative density citations. The new target remains REVIEW_REQUIRED.

## Why this target, and limits of its possible use

Main gap: actual-Xi pointwise initial signs at unbounded heights and
all-degree mixed positivity. A successful affordable localization
construction could connect a hypothetical negative region to a
signed averaged witness, provided separate control of |W| times the
approximation error and of all multiobserver moment terms were obtained.
The L2 norm in this test alone does not give either control. There
is no assumed negative interval, RH premise, zero simplicity, spacing
or known lower width of a negative region. The fixed bump is a
diagnostic for a mechanism, not an assertion that every negative
region has this width or location.

Three mechanisms were compared for continuation, without new calculations:

- Another fixed finite observer block: L636 and C635a now have positive
  margins. Increasing its size alone supplies no materially new route
  to pointwise realization; this is not selected.
- Pure Dirichlet weight concentration: L620's microscopic mass fraction
  tends to zero in its allowed range. No new idea changing that test
  is present, so preserve the stop.
- Inverse localization by actual Hardy translates, with a coefficient
  cost and a moment-error comparison: selected for source review.
  It correlates with Z and is outside L620's pure-weight assertion;
  it tests realization rather than another finite block margin.

The local `ATTEMPTS/2026-10-31-theta-translate-proof-construction-stop.md`
records that Dimitrov--Xu's remaining proof supplied no constructive
L1 error sequence for the actual theta correlation. It is a different
inverse problem and is not reopened here. Likewise the older
`drafts/literature/2026-10-30-genuine-positive-class-runge-flux-test.md`
warns that qualitative approximation does not give its weighted norm
cost; its full-space/positive-class distinction must not be imported
as a theorem about Z translates. Their relevant quantitative source
leads can be compared narrowly, with exact hypotheses, before fresh
search. No matching theorem or originality is asserted by this nomination.

No creative mathematical attempt is yet approved. Essential source
coverage for the inverse cost problem is the blocker; after it is
resolved, a genuine construction or dual obstruction test may warrant
proof_attempt/creative routing with its precise bounded threshold.
Full matching Mathlib coverage is unchecked and unknown.
