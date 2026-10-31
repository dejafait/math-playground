# Constructive finite-interval ratio/chirp dual: completed source screen

TARGET: Assess primary-source coverage for a constructive finite-interval bounded dual giving integral_T^(2T)|R_T(t)|dt >= c integral_T^(2T)|U_T(t)|dt-o(T(log T)^3), with fixed c>0 and exact L477/L481 phases, without a sign multiplier or Haar replacement.
CHECKED: 2026-10-31
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Completed bounded searches for constructive finite-interval Littlewood duals, nonlinear-phase L1 inequalities and chirped bounded-dual separation; inspected the primary construction and previously unread short-interval refinement below. No matching full-residual theorem was found; no novelty or falsity is inferred.
SOURCE_EVIDENCE: Rechecked Jaming--Kellay--Saba arXiv:2303.10919v2 Theorem 1.1(iii), (2.2), Proposition 2.4, Lemmas 2.6/2.8--2.11, Proposition 2.12, Remark 2.13 and Corollary 2.14; Jaming--Kellay--Saba--Wang arXiv:2409.07093v1 Theorem 1.5 and proof opening; newly read Jaming--Saba arXiv:2311.17714v1 Theorem 4.2/(4.4), Section 4.2 essential construction and R1/R2 proof cases. Primary links and qualifications below.
COMPARISON: The bounded recursive dual and its one-sided Fourier correction control pairings with separated fixed linear exponentials. The short-interval refinement retains that phase class and a threshold loss. Neither supplies the required theta-chirp pairing or a ratio-norm comparison. A source coefficient bound is not the proposed full-residual inequality.
GAP: Essential source scope for the exact dual/chirp cross term is missing, although sources are accessible. The stated separation inequality and the independent full-scale integral|U_T| lower bound remain open; no uniform arithmetic frequency gap, negligible discarded block or bounded projection is assumed.
REASON: Park this constructive full-residual mechanism after the bounded source test fails to supply its essential curved-phase estimate. Do not repeat scalar-dual searches or invoke a creative proof attempt from boundedness alone. A separate ratio-only coefficient-certificate calculation is nominated with precise known-tool coverage, not executed or claimed here.
LITERATURE_REASON: Constructive bounded finite-interval duals and their chirped cross term are outside the inspected Laplace implementation and the previous sign-multiplier target; their exact source hypotheses remain essential unread coverage.
SCOPE: Exact L477/L481 U_T,V_T,R_T,theta and fixed M=floor(sqrt(T/(2pi))), with arbitrary real T tending to infinity or one specified unbounded sequence. Both ordered pair sums, endpoints and all rational-frequency coincidences are retained. No RH, independent phases, source theorem for the new inequality, bounded projection operator, uniform frequency gap, negligible discarded block or finite-height Haar transfer is assumed.

## Original nomination, preserved

The main gap remains actual-Xi all-degree positivity and initial signs
at unbounded heights. A constructive separation inequality could combine
with a separate full-scale nonchirped L1 lower bound to obstruct L477's
selected square as a little-o approximation. Even that would not give
a negative-mass saving, higher signs or RH. Essential local inputs for
the proposed definitions are L477 and L481; L482/L484 are contrasts
only. No cross-notebook input is proposed.

First reuse the actual-height/linear-frequency distinction and complete
failure comparison in `2026-10-29-fixed-square-residual-hardy-l1-coverage.md`,
and the sign-boundary issue in
`2026-10-29-sign-adapted-chirped-leakage-coverage.md`. The historical
stationary-involution stop in
`ATTEMPTS/2026-09-24-actual-phase-poisson-ratio-test.md` also remains.
Do not relabel any of these failed automatic transfers as a construction.
No new inequality or dual function is supplied by this nomination.

The bounded source test is whether a primary constructive finite-interval
inequality supplies a dual whose full correlation with both exact phase
sums can be analyzed with explicit norm, frequency and endpoint losses.
A theorem for a complex analytic polynomial, a bound for U_T alone,
a generic separated linear system, or a bounded but unevaluated test
function does not pass. The full proposed inequality is retained as the
target while assessing it. Do not derive it in the source-review turn.
If essential coverage remains absent, park this mechanism with its
specific mismatch and select independently testable work; another broad
search of the same scalar inequalities is insufficient.

A genuinely source-supported new construction at this gap could later
justify proof_attempt/creative, with a concrete dual and a bounded
correlation test. None is justified now. No proof-purpose routing or
escalation is requested until that construction is specified and
reviewed. Mathlib matching is unchecked, not asserted absent.

## Completed comparison, 31 October 2026

The exact target above was retained throughout this literature-only
step. L477 was read in full, including its audit and all cutoff/endpoints;
L481's definitions and finite-norm interface were read. No mathematical
proof or calculation of a new bound was performed. The main gap and
downstream limitations in the original nomination remain unchanged.

### Primary evidence

**Jaming--Kellay--Saba**, v2, 24 July 2023,
[primary text](https://arxiv.org/html/2303.10919v2), Theorem 1.1(iii):
ordered real frequencies satisfying |lambda_k-lambda_l|>=|k-l|,
arbitrary complex coefficients, and interval length H>=72 give
H^(-1) integral |sum a_k exp(2pi i lambda_k t)| >=
(1/122) sum |a_k|/(k+1). Read the indicated construction, including
the bounded recursion F_(j+1)=F_j exp(-eta h_(j+1))+f_(j+1),
Re h_j=|f_j|, and its bound (1-exp(-eta))^(-1).
Proposition 2.12 uses the nonnegative Fourier modes of the correction
in linear frequency differences. Remark 2.13 combines adjacent/tail
blocks to remove the preliminary dimension dependence. This is not
a theorem about pairing that correction with a nonlinear chirp.

**Jaming--Kellay--Saba--Wang**, v1, 11 September 2024,
[primary preprint](https://arxiv.org/pdf/2409.07093v1), Theorem 1.5,
printed p. 3 and proof opening p. 4: any positive interval is allowed
for a fixed increasing sequence whose gaps tend to infinity at both
ends. The constant depends on the sequence and interval; the proof
selects a tail-gap index and uses compactness. The theorem does not
give uniform constants for the changing arithmetic spectrum here.

**New inspected lead: Jaming--Saba**, v1, 29 November 2023,
[primary preprint](https://arxiv.org/html/2311.17714v1), Theorem 4.2,
(4.4), Section 4.2, printed pp. 38--48. There are c_*,delta_*>0
such that for 0<delta<delta_*, ordered real frequencies with
lambda_(k+1)-lambda_k>=1 and arbitrary complex coefficients satisfy

    sum_(k=0)^N |a_k|/(k+1)
       <= c_* delta^(-15/2)
          integral_(-(1+delta)/2)^((1+delta)/2)
             |sum_(k=0)^N a_k exp(2pi i lambda_k t)|dt.

Read Lemma 4.4's near/far split, Lemmas 4.7--4.12's bounded analytic
correction, both R1/R2 cases in Lemma 4.13, and the final proof.
The short-interval loss is retained; linear separation remains essential.
This is theorem-level scope inspection, not an independent source-proof
audit; intermediate displayed notational inconsistencies are not imported
as separate claims. No curved-phase extension is stated here.

### Applicability and decision

In the source constructions the relevant integrals reduce to Fourier
transforms of an interval cutoff at fixed frequency differences plus
periodic Fourier shifts. L481's second component instead contains the
actual 2theta(t)-t log(nm) phase. The cited results provide no estimate
for its complete correlation with their constructed dual. One-sided
Fourier support and a bounded norm do not themselves state that estimate.
No stationarity, derivative separation or aggregate error bound is
proved in this review. In particular, L477's unweighted signed bound
cannot be cited for a new multiplier.

The source lower bound is a rank-weighted coefficient sum, whereas the
target requires a fixed fraction of integral|U_T|. Grouping equal ratios,
ordering both frequency signs, checking the actual scaled minimum gap,
and evaluating that coefficient certificate remain unperformed even
for U_T alone. No subset can be discarded from a lower-bound application
without controlling its complement. The source constant's dependence
on normalized interval length must be kept. These are precise missing
applicability obligations, not estimates inferred from a search.

The full-residual continuation test fails for missing theorem scope;
SOURCE_BLOCKED means that mismatch, not inaccessible texts or a proof
that separation is false. Reopening requires a quantitative actual-chirp
pairing input or an explicitly covered construction with complete losses.
The old sign-boundary, Haar-transfer, saturation and L319 involution
stops are preserved. No new lemma, mathematical script, RH evidence,
or claim beyond the inspected sources is produced. Mathlib matching
and supporting formal declarations remain unchecked.

### Search and continuation record

Queries included `"Littlewood" "chirp" "L1" exponential sums bounded dual`,
`nonharmonic Fourier series Littlewood bounded test function curved phases
oscillatory integrals`, `"Littlewood" "nonlinear phases" inequality`,
`"bounded" "dual" "chirped" Fourier inequality`,
`"Jaming" "Saba" "Ingham" "L1" 2025`,
`"L1" "non-harmonic" "non-linear" inequality phases`,
and `"Littlewood" "bounded test function" finite interval Fourier`.
Unrelated oscillatory-operator and signal-processing hits were excluded;
search snippets were not theorem evidence. The prior Hardy-L1 assessment
had explicitly left the short-interval survey unread; its Theorem 4.2
is the new primary evidence in this turn. No search establishes novelty.

Nominate the separate ratio-only coefficient-certificate test in
`2026-10-31-grouped-ratio-nazarov-certificate.md`. It asks whether a
specific known inequality supplies the other necessary norm scale,
without any chirped-separation assumption. Its saved assessment is a
new SPECIALIZE nomination for separate next-turn approval, not an
executed specialization. No covered central dual/chirp mechanism yet
justifies creative routing; the ratio-only test is a calculation.
