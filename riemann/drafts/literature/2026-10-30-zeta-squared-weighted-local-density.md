# Proposed amplitude-weighted local zero count

TARGET: Review coverage for W_delta(T)<=C T delta(log T)^2 exp(-c delta log T), uniformly for 1/log T<=delta<=1/8, where W_delta is the zeta-squared weighted local zero count defined in the assessment.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded exact-weight, stronger-result and zero-detection searches; inspected primary weighted one-level density, weighted CLT, joint log-derivative and two-branch detector statements and relevant proof cases. Reused the named local count, moment and failure assessments; query and source details appear below. No matching theorem was identified; no novelty or nonexistence claim.
SOURCE_EVIDENCE: Bettin--Fazzari arXiv:2208.08421v1 Theorem 1.2, pp. 1--3 and Section 2.1 pp. 5--7; Fazzari arXiv:1912.08127v2 Theorem 1.1, Proposition 1.1, Lemmas 2.1--2.2, pp. 2--3 and Section 2; Fazzari arXiv:2310.15918v2 Theorem 1; Fazzari--Gerspach--Minelli arXiv:2507.04150v1 Theorems 1.1--1.2; Baier Acta Arith. 113 (2004), Proposition 4 pp. 83--84 and Section 6 pp. 90--92. Exact scope and qualifications below; source arithmetic proofs remain citations.
COMPARISON: The strongest inspected unconditional theorem with the exact amplitude weight is a smoothed analytic statistic at complex zero coordinates, not the positive strict off-line count. RH-dependent weighted results cannot fill this gap. Count-only moments repeat L486's loss. A two-branch detector and an unconditional short-polynomial twisted second moment provide distinct tools for an attempt, not the missing correlation estimate.
GAP: Prove the stated positive weighted off-line count estimate with common C,c,T_0, or obtain an informative obstruction for a specified detector implementation. Neither a positive complex-zero majorant, a weighted detector transfer, near-line parameter uniformity nor the proposed W_delta inequality has been established.
REASON: Primary theorem comparison is now sufficient for a bounded EXPLORE attempt at the saved weighted target. A direct import fails at the positive off-line selection; detector-before-separation is materially different from the count-only and disk-supremum stops. This approves an attempt, not a result.

## Exact proposed input and its purpose

Let T be real, L=log T, and count actual zeta zeros rho=beta+i gamma
with full multiplicity. For 1/L<=delta<=1/8 define

    n_delta(t) = sum_{rho: beta>1/2+delta/2,
                         |gamma-t|<=2delta} multiplicity(rho),
    W_delta(T) = integral_T^(2T) |zeta(1/2+it)|^2 n_delta(t) dt.

The target asks for absolute C,c>0 and T_0, common to every real
T>=T_0 and every displayed delta, with

    W_delta(T) <= C T delta L^2 exp(-c delta L).

The real-part cutoff is strict, the ordinate window is closed, and
no zeros on the critical line are counted. No selected-zero values
replace the integral. Positivity of this finite local count is not
positivity of the mixed forms. In particular this target is not asserted
as a theorem, a consequence of the cited moment bounds, or an RH criterion.

The main gap is actual-Xi initial signs at unbounded heights and all-degree
mixed positivity. The immediate downstream possibility is to apply a
weighted count bound to L486's exact nonnegative aggregate kernel while
retaining the |Z(t)|^2 factor, rather than separating amplitude and counts
by Cauchy--Schwarz. The proposed scale is intended to test whether the
surviving extra logarithmic loss can be removed. Any kernel transfer,
dyadic summation and treatment of larger displacements still require a
separate mathematical check; none is derived or approved here. Even a
successful mass bound leaves individual-height signs and full RH open.

Essential local inputs for comparison: L471's normalization and pair
windows, L483/L486's exact kernel and failure threshold, L485's count
scope, and L474 only for its cited deterministic shifted-moment scope.
No cross-notebook theorem is used. Matching Mathlib coverage is unchecked.

## Distinguishing this nomination from recorded stops

The count-only certificate is stopped in
`ATTEMPTS/2026-10-30-local-density-all-mesoscopic-certificate.md`:
its upper bound does not decay for every delta L tending to infinity.
The joint extraction stop in
`ATTEMPTS/2026-10-30-joint-blaschke-weighted-sparsity-source-gap.md`
requires a new weighted selection input and forbids assuming one.
The selected-cell squared-supremum energy comparison in
`history/2026-10-28-zero-selected-energy-source-comparison.md`
likewise did not import a weighted little-o result. Here the proposed
new input is an explicitly defined continuous weighted first moment,
not the old disk supremum, further factor extraction, or another
recalculation of an unweighted L2 estimate. The source review must still
check whether earlier evidence also disposes of this precise target.

## Bounded continuation or abandonment test

First inspect primary weighted zero-density/zero-detection statements
for the exact weight, displacement scale, uniform constants and endpoint
conventions. Reuse the named assessments for their original scopes;
do not promote unweighted moments or count bounds to a weighted theorem.
A matching known theorem should be imported, not reproved. A genuine
uncovered difference needs an approved SPECIALIZE or EXPLORE assessment
before any calculation. Use REVIEW_REQUIRED or SOURCE_BLOCKED if
essential comparison remains incomplete.

For a later approved mathematical attempt, one discriminating scale is
delta=log log T/log T. The required test is the displayed W_delta bound
with some fixed c>0, not merely the old Cauchy--Schwarz bound or a finite
grid. A source-implied alternative saving should be compared with the
actual L486 threshold before expanding the target. Stop this mechanism
if the only justified estimate repeats its old loss and no independent
correlation input survives. A failure of a proposed sufficient upper
bound is not a counterexample to the actual mass saving.

This was the nomination-stage routing. The completed review below now
supports a bounded detector attempt, subject to the separate approval of
the newly written continuation assessment; no mathematics was attempted
during this literature turn.

## Completed primary-source comparison (30 October 2026)

### Exact-weight theorem and its positivity limitation

S. Bettin and A. Fazzari, *A weighted one-level density of the non-trivial
zeros of the Riemann zeta-function*,
[arXiv:2208.08421v1, 17 August 2022](https://arxiv.org/pdf/2208.08421v1),
Theorem 1.2, printed pp. 1--3; Section 2.1, pp. 5--7.
Its k=1 theorem is unconditional: f is even, with smooth compactly
supported Fourier transform; the macroscopic weight is smooth and
compactly supported in the positive real axis. The k=2 case additionally
requires Fourier support in (-1/2,1/2). The statistic sums
f((gamma-t)log T/(2pi)), where rho=1/2+i gamma and gamma may be complex
(p. 1 footnote). Its k=1 limiting kernel on the real axis is
1-(sin(pi x)/(pi x))^2. Read the explicit-formula decomposition (2.3),
the complex growth estimate preceding (2.4), and the twisted-moment
and contour computation (2.5) onward. These preserve analytic complex
zero evaluations; they do not state domination of the positive
beta-selected count. No nonnegative off-line indicator or uniform
moving-delta theorem is supplied. A positive real-axis kernel alone
licenses no such selection. The paper's shifted discrete-moment
connection (1.3) expressly assumes RH. This is a scope comparison,
not an independent audit or a proof that all analytic detectors fail.

### Weighted value-distribution results

A. Fazzari, *A weighted central limit theorem for log|zeta(1/2+it)|*,
[arXiv:1912.08127v2, 20 January 2021](https://arxiv.org/html/1912.08127v2),
Theorem 1.1 and Proposition 1.1 assume RH. The explanation immediately
following Proposition 1.1 identifies the weighted shifted-zero moment
as the RH-dependent point; Section 2 uses the conditional Gonek
Lemma 2.2. This cannot be imported unconditionally.

The same paper's Lemma 2.1, printed p. 3, is an unconditional tool:
A(s)=sum_(n<=T^theta) a(n)n^(-s), B(s)=sum_(m<=T^sigma) b(m)m^(-s),
coefficients bounded by n^epsilon and m^epsilon for every epsilon>0,
and theta+2sigma<1. Its integral of A|B|^2|zeta|^2 over [T,2T]
is an explicit gcd/lcm sum plus o(T), with convolution a*b and
constant 2 EulerGamma+log 4-log(2pi)-1. No arbitrary zero-selected
weight or uniform error for a new varying family is asserted here.
Any later use must verify coefficient bounds, a fixed length margin,
and sufficient uniformity. Its arithmetic proof is not reproved.

A. Fazzari, *On the joint second moment of zeta and its logarithmic
derivative*, [arXiv:2310.15918v2, 1 June 2024](https://arxiv.org/html/2310.15918v2),
Theorem 1, assumes RH, despite the introductory phrase about not assuming
moments. The displacement parameter satisfies
(log T)^(-1/4+epsilon) << a << 1, 0<epsilon<=1/4. It bounds the
zeta-squared weighted squared log derivative at 1/2+a/log T, not n_delta.
Neither its hypothesis nor its parameter scope covers the target.

A. Fazzari, M. Gerspach and P. Minelli,
[arXiv:2507.04150v1](https://arxiv.org/html/2507.04150v1), Theorem 1.1,
gives fixed polynomial joint moments of log zeta and analytic linear
statistics, with even k and Fourier support inside (-2/(k+2),2/(k+2)).
Theorem 1.2 assumes RH. Neither gives an exponential amplitude moment
with positive off-line selection or growing-order uniformity. Read also
(1.6), Proposition 3.1's Holder step and the explanation of its support
restriction. The arXiv version is labelled 5 July 2025; the HTML renders
an internal date 24 August 2026. Only the explicitly retrieved v1
statement is compared; no inference about an uninspected revision.

### Detector lead: both branches are essential

S. Baier, *On the p^lambda problem*, Acta Arith. 113 (2004), 77--101,
[primary journal PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83115),
Proposition 4 pp. 83--84, Section 6 pp. 90--92; also
[arXiv:math/0512445v1](https://arxiv.org/html/math/0512445v1).
For X,Y>=1, large N, log N comparable to log T and log Y,
and log X=O(log N), it supplies two alternatives U_1(rho)>1/2
or U_2(rho)>1/2 for zeros above (log N)^2 and through T.
U_1 is a Gamma-weighted integral of zeta M_X on the critical line;
U_2 is a smoothed Dirichlet-polynomial tail; M_X uses truncated
Mobius coefficients. The target's strict beta>1/2 avoids the displayed
Gamma integrand's beta=1/2 boundary, which is not audited here.
Section 6 retains both types but weights by its particular finite
polynomial |D_theta(u,i gamma)|; its Holder/fourth-moment estimates
are not the desired W_delta theorem. Replacing that weight by a
local zeta-squared integral remains a new application obligation.
The addendum [arXiv:math/0512447v1](https://arxiv.org/pdf/math/0512447v1),
Theorem 3 pp. 1--2, removes a length restriction with a weaker
logarithmic loss; it supplies no amplitude-weighted near-line estimate.
No detector reproof or application was performed in this review.

### Reused inputs, searches and decision

Maples--Rodgers v2 Theorem 2.4 and Proposition 2.5 were checked again
only for this changed-weight comparison. Proposition 2.5 integrates a
count power under dt, for integer k>=1, 1<=H<=T^(1/4), c in (0,1/2),
with strict beta cutoff; L485's restricted repair remains the permitted
local import. Bettin v1 Theorem 1, p. 2, was inspected for deterministic
real shifts O(1/log T) and its coincident-pole convention. Neither
contains the proposed correlation weight. Reuse the canonical L474,
L485 and L486 qualifications and the already completed source audits;
no new zero-free claim, reciprocal continuation or parked arithmetic
estimate is proposed, so the October fixed-half-plane reassessment
is not invoked.

Queries included `zeta weighted zero density second moment`,
`zeta weighted zero-density second`, `zeta weighted density Fazzari`,
`zeta zeros second moment off critical line weighted`,
`zeta weighted zero-detection`, and exact author/title searches for
the primary papers above. Searches also returned weighted prime-interval
and L-function-family results; their snippets were not imported.
The earlier selected-energy comparison already assessed positive
discrete moments and reflected bilinear moments in their original
scopes; no further scope is inferred here. Source access via the web
provided the essential statements; a failed shell PDF download did not
block this review. No model, finite grid or numerical experiment was used.

Decision EXPLORE means a bounded search did not identify an adequate
known result. It is not a novelty claim, a proof of the inequality,
or an impossibility theorem. The new independently testable mechanism
is to retain the amplitude through both detector branches before
separating counts. The first test remains delta=log log T/log T;
a merely renamed L486 Cauchy--Schwarz separation does not meet it.
The exact full-range target above is preserved. Full matching Mathlib
coverage is unchecked; no Lean theorem or library homepage is used as
coverage. Any genuine import belongs in a later canonical lemma with
its own applicability argument; this literature turn changes no lemma.
