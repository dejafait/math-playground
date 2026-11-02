# Prime-block quadratic test for the normalized density contrast

TARGET: Test the normalized microscopic contrast lower bound c T log T using the prime block T^(1/16)<p<=T^(1/8) and its exact denominator-weighted second moment.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: The completed normalized-density source review searched the exact functional, triangular-discrimination duals, shifted lower bounds and clipped/prime-block probes; checked L481/L482/L572 and the density/saturation/fixed-witness comparisons. No matching result was found; no novelty conclusion is asserted.
SOURCE_EVIDENCE: Directly checked Curran 2303.10123v2 Lemmas 2.3--2.5 at https://arxiv.org/html/2303.10123v2#S2 and Villarino math/0504289v3 Theorem 6, (2.3.4)--(2.3.5), printed p. 7 at https://arxiv.org/pdf/math/0504289v3#page=7; reuse 2026-10-31-normalized-density-contrast-review.md for named weighted Cauchy--Schwarz and the limitations of Reid--Williamson Appendix F/(83) and Curran 2405.08725v1 Theorem 1.1. No uninspected theorem is needed for the bounded test as proposed.
COMPARISON: Known finite mean-square and prime reciprocal asymptotics cover tools, not this joint signed/weighted contrast. The test uses an actual-height growing prime block and a Q_T-weighted quadratic norm rather than global fourth-moment interpolation, rank bounds, full-zeta replacement, Haar transfer or global polynomial saturation. All arithmetic estimates and the dual specialization remain unproved.
GAP: Establish a positive c_1 T log T signed probe correlation and an O(T log T) denominator-weighted probe second moment with complete finite-height errors, then justify the normalized and bounded-dual comparisons; no theorem currently supplies these claims together.
REASON: Separate source-only approval and direct-URL repair completed on 2026-10-31; preserve the exact nominated mechanism and EXPLORE scope. Source interfaces are ready for a later mathematical invocation; no probe estimate or new specialization is proved here.
SCOPE: Real T tending to infinity; L=log T, h=1/L, M=floor(sqrt(T/(2 pi))), J=[T+h,2T-h], A_M=sum_(n<=M)n^(-1/2-it), F_M=|A_M|^2, D_h=F_M(t+h)-2F_M(t)+F_M(t-h), Q_T=F_M(t+h)+2F_M(t)+F_M(t-h)+L. No RH, moving cutoff, independent phases or full-residual transfer.

The main gap is actual-Xi all-degree positivity and unbounded-height
initial signs. The intermediate target is

    H(T)=integral_J D_h(t)^2/Q_T(t) dt >= c T L

with fixed c>0 at all sufficiently large real T. Its proposed use is
positive actual-height density mass for C481a's conditional ratio-norm
transfer. The complete L477 residual, both defect thresholds, negative
mass and all Xi signs remain independent unresolved questions.

Specify the single test polynomial

    P_T(t)=-sum_(T^(1/16)<p<=T^(1/8)) cos(t log p)/sqrt(p).

Try to prove simultaneously

    integral_J D_h(t)P_T(t)dt >= c_1 T L,
    integral_J Q_T(t)P_T(t)^2dt <= C_1 T L,

for fixed c_1,C_1>0. These are thresholds sought, not facts. A future
weighted Cauchy--Schwarz/quadratic-dual specialization must be written
out for these finite continuous functions, followed by the precise
comparison with the absolute density difference and its bounded dual.
Do not call P_T bounded, replace algebraic by modulus squares, infer
separation from total mass alone, or invoke probability normalization
for unequal-mass measures without accounting for it. Clipping is not
a required implementation if a direct weighted test suffices.

Use Curran's unconditional arbitrary-coefficient finite mean square as
an import, not a theorem to reprove. Group equal integer products before
applying it; overlapping prime supports forbid the disjoint-support
splitting lemma. Prove the actual coefficient bounds and keep all
product lengths, translated coefficients, repeated primes, n=1 terms,
integer transitions and J boundary strips. Mertens supplies only a
standard prime reciprocal asymptotic at real endpoints. No uniform
time-distribution statement follows from it. Weighted Cauchy--Schwarz
is a named elementary input; its application is a specialization.

Continue if both obligations yield a fixed positive H(T)/(T L), with
errors smaller than the signed main scale. An informative negative
would identify a subscale signed correlation, a growing normalized
weighted cost, or an unavoidable finite-height error for this probe.
Record a rigorous weaker result honestly if only one obligation is
settled; do not claim a lower bound from an incomplete pair. Park this
probe after a decisive failure unless materially new input refines it.
Numerical quadrature or a fixed-T sample cannot certify the eventual
uniform threshold. No script is necessary for the proposed proof test.

Essential local inputs are C481a's exact definitions; L573 is cap-loss
context only and is not needed unless a capped consequence is claimed.
L477 locates the independent residual gap. L481/L482/L572 are contrasts,
not premises of the proposed inequality. No cross-notebook input.
Full matching and supporting Mathlib coverage remain unchecked.

This is a potentially new local mechanism only in the limited sense
that the bounded search found no matching result; it is not certified
originality. Import the general known tools and prove only the proposed
observable-specific difference in a later authorized research turn.

## Separate source approval and direct-URL recovery, 31 October 2026

The supervisor required a direct source URL in the ready assessment.
The source field now links the inspected statements, without changing
the target, hypotheses, or proposed thresholds. Reuse the completed
comparison's searches and failure assessment; no new novelty search or
mathematical attempt was necessary for this repair.

[Curran, v2, 15 May 2024, Section 2, Lemma 2.3](https://arxiv.org/html/2303.10123v2#S2)
states the finite mean square for arbitrary complex coefficients, with
error O(N) times their squared norm. It has no RH hypothesis. Read
Lemmas 2.4--2.5 as well: disjoint prime supports are required for the
splitting result; the unweighted prime-moment bound has a length
condition and does not supply our weighted moment. The later attempt
must group equal products, retain actual lengths and translation
phases, and handle J explicitly. Import Lemma 2.3; do not reprove the
Montgomery--Vaughan theorem or assume diagonal averaging is exact.

[Villarino, v3, 17 May 2005, Theorem 6, printed p. 7](https://arxiv.org/pdf/math/0504289v3#page=7)
states the prime reciprocal asymptotic for real x>2 with error bounded
by 4/log x. Inspected the statement and the adjoining partial-summation
argument (2.3.2)--(2.3.5), retaining its cited bounded weighted-prime
remainder as a named input. This covers real prime endpoints, not
height distribution or the signed correlation. Import the classical
named theorem; no reproof or explicit constant is needed for this test.
The PDF screenshot request returned no inspectable image; readable
formula extraction and the prior source review supply the statement.

Reread C481a fully, L477's hypotheses/conclusion and the L572 ATTEMPTS
record; reused the completed comparison for L481/L482 and L573.
The grouped-ratio certificate failure remains preserved and does not
settle this denominator-weighted probe. No cross-notebook input or
full-zeta/Haar substitution is authorized. Weighted Cauchy--Schwarz
is a named elementary tool; its observable-specific application remains
for the research turn. Full matching/supporting Mathlib coverage is
unchecked. This approval repairs source traceability only: both moment
obligations, normalized-to-absolute comparison and all independent
Xi gaps remain unresolved. Further literature on this unchanged ready
target requires a new essential source reason.
