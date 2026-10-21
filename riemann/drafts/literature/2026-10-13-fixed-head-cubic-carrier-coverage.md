# Fixed-head cubic carrier compatibility: completed source review

TARGET: Assess source coverage for a fixed-head carrier decomposition of d_N B0_N into rationally twisted cubic zeta jets and comparison with the proved single-gamma mean-value theorem.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 103's signed-cubic discovery/exclusions and step 46's single-gamma/rational-twist assessment; narrowly inspected L369/L390/L391/L405 and step-106 records for an existing cubic reduction. No completed duplicate was located in these records; no novelty follows. Followed the specific derivative-reflection and zero-carrier cases in primary sources.
SOURCE_EVIDENCE: Retrieved Sourmelidis–Steuding–Suriajaya 2007.14008v2 Section 3 between (35)–(36), both branches, and the zero-carrier argument before (37); DLMF 25.4.1, 25.4.5–6 and 25.2.1; reused L391's audited ordinary jets, rational encoding, coefficient variation and sharp connector tools with its cited Bourgain theorem.
COMPARISON: Known tools cover fixed rational twists of right-line cubic derivative series with zero or one exact gamma carrier, and exact derivative reflection. They permit a bounded compatibility attempt, conditional on establishing a complete reduction to those forms. They do not state d_N B0_N's decomposition or its signed mean, and do not license unreduced higher carrier powers.
GAP: A later research step must establish the complete carrier reduction, ordinary order-two identities, analytic weights and sharp connector error; none is proved in this review. Signed coefficient/scale, infinite response-tail passage at that scale and clipping remain uncovered.
REASON: Essential known-tool scope is now assessed for one finite-head compatibility test with an explicit connector threshold; cite the sources and reuse audited inputs, rather than reprove a cubic moment theorem. Keep the complete signed evaluation parked.
SCOPE: Fixed N independent of H; exact L390 d_N and L405 B0_N; actual phase and ordinary jets through order two; finite rational twists; zero/single-gamma right-line reduction with sharp connectors. No full-tail limit, growing N, signed asymptotic, clipping, phase independence or RH premise.
COVERED_TARGET: Test whether the fixed-N sharp integral of d_N B0_N admits an exact finite reduction to zero-carrier and single-gamma rationally twisted cubic jet integrals, retaining ordinary jets through order two and total connector error o(H(log H)^2).
LITERATURE_REASON: The gate requested this narrower fixed-head compatibility comparison; derivative reflection and the zero-carrier source case were essential additions to the reused single-gamma coverage. No broad cubic search was repeated.

Main gap: global actual-theta mixed positivity. The intermediate target
is a source-supported map of the finite cubic polynomial's carrier
terms. Its plausible use is identifying one signed term that admits a
rigorous bounded calculation, or a concrete obstruction to this contour
mechanism, after L406 has removed the complete physical error at its
stated test scale. There is no asserted signed main scale.

Fix N independently of H and put Z_N=sum_(n<=N) n^(-5/2-it).
Define d_N and B0_N by replacing Z with Z_N in L390's d and
L405's B0, retaining the actual critical jets and gamma phase. This
defines the proposed target only: no carrier decomposition is proved
or approved here. Constants depending on N are allowed. No passage
N to infinity, growing head or clipped weight belongs to this target.

Essential inputs are L369, L390, L405 and L406. Reuse the source
comparison in `2026-10-13-signed-cubic-discriminant-mean.md` and the
ready single-gamma/rational-encoding material in
`2026-10-10-discriminant-unequal-orientation-projection.md` only within
their stated scopes. The precise primary lead is
[Sourmelidis–Steuding–Suriajaya, arXiv:2007.14008v2, Section 3 between (35)–(36)](https://arxiv.org/html/2007.14008v2#S3).
Step 103 read it; this proposal does not claim a new retrieval or a
matching theorem. Bui 1410.2433v1 Theorem 5.1 remains excluded as an
unproved input. Do not differentiate a real-shift cubic formula without
complex-uniform derivative coverage. No phase independence is assumed.

Continuation test: approve one bounded later algebra/application attempt
only if source coverage permits checking every required orientation and
ordinary derivative through order two, with an explicit error threshold
for the proposed reduction. A finite arithmetic reduction is acceptable
without a sign theorem, provided its downstream limitation is explicit.
If an essential orientation requires an unproved third-moment theorem
or uncontrolled connector, record that precise obstruction and park this
implementation; do not repeat a broad cubic search or claim impossibility.

Even success leaves the signed full-tail arithmetic, leading scale/sign,
clipping, regulator scale, total L367 margin/remainder, actual common-zero
upper counts and global positivity unresolved. Preserve L394/L399/L400
stops and the audited even L405 benchmark. Full matching Mathlib coverage
has not been checked. At proposal time this required a separate literature
turn; the completed comparison and its restricted scope follow below.

## Completed comparison — 2026-10-14, step 107

The proposal above records its original admission test. This review
supersedes its pending source status, without establishing the proposed
decomposition. ADVANCE means newly usable local source coverage; there
is no mathematical result beyond the sources checked, no new lemma,
script, carrier identity or computed cubic coefficient.

### Precise known inputs and their limits

Sourmelidis–Steuding–Suriajaya, *Dirichlet Series with Periodic
Coefficients and their Value-Distribution Near the Critical Line*,
[arXiv:2007.14008v2, Section 3, immediately after (35)](https://arxiv.org/html/2007.14008v2#S3):
for fixed positive integer q and epsilon>0, and a Dirichlet series
convergent for Re s>1 with a(n)<<_eta n^eta for every eta>0,
the primitive on Re s=1+epsilon with kernel
(q/(2pi))^s Gamma(s) exp(omega*pi*i*s/2) equals, after division
by 2pi*i, sum_(n<=Vq/(2pi)) a(n) exp(-2pi*i*n/q)
+O_epsilon(V^(1/2+epsilon)) for omega=-1, and O_epsilon(1)
for omega=+1. Constants may depend on the fixed series and q.
Periodicity is used only in the following simplification. Neither
growing q nor higher gamma powers is covered. Both branches were read.
The same section before (37) treats the zero-carrier case by absolute
right-line expansion, isolating its constant frequency and using the
first-derivative test for the rest; a rational twist needs its own
resonance isolated, not just the n=1 term.

The prior assessment already inspected the originating stationary-phase
interior, endpoint and exterior-index cases through readable restatements;
the original Gonek scan/access qualifications remain unchanged. The
Steuding (2002), Lemma 3 proof remains an unread lead, not a newly assumed
input. No further proof-case retrieval was essential for reusing this
stated fixed-parameter theorem.

NIST DLMF, version 1.2.8 (2026-09-15),
[25.4.1](https://dlmf.nist.gov/25.4.E1) gives the exact reflected
factor 2(2pi)^(-s) Gamma(s) cos(pi*s/2) for s!=0,1.
[25.4.5–6](https://dlmf.nist.gov/25.4.E5) explicitly states the
derivative reflection formula for every integer k>=1, with the same
exclusions (Apostol 1985a, (6), p. 224). Read the entire double sum
and its constant in 25.4.6, including the k=1,2 cases. This covers
reflected derivatives without differentiating a real-shift asymptotic.
It does not itself cancel this notebook's carrier powers.
[25.2.1](https://dlmf.nist.gov/25.2.E1) supplies the ordinary
Dirichlet series on Re s>1 and its sole meromorphic pole at s=1.
Absolute local derivative convergence there is the standard termwise
holomorphic-series application; the later proof must record its
logarithmic coefficient bounds.

The necessary local conversion is already in audited L391 (3): exact
ordinary x,y,z, including i factors, Omega' and normalization after
differentiation. Its audited tuple/weight argument controls the analytic
coefficient variation, and its rational encoding treats a fixed u/v by
integer support vn and gamma scale u. Reuse these procedures only after
checking the present polynomial. Its four-factor evaluation is a
contrast, not a cubic input or a new DAG dependency. L369 (5),(9)
supplies zero-safe actual reflection through the second ordinary jet;
L390 and L405 supply d and B0 with their signs. L406 discharges the
physical error only at its stated log^2 H test scale.

For endpoint tools, reuse J. Bourgain, *Decoupling, exponential sums
and the Riemann zeta function*, JAMS 30 (2017), 205–224,
[1408.5794v2, Theorem 5/(0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2),
as assessed in step 46 and specialized/audited in L391. L391's
fixed-strip Cauchy estimate (11), exact carrier estimate and coefficient
bounds are available; its connector proof is not a statement for an
arbitrary new carrier. The later cubic application must count the
actual derivative factors and bound both connectors anew. Do not
substitute an unreduced power into a single-gamma theorem or differentiate
an O-term.

### Bounded next test and stop condition

The covered test is to attempt a complete finite polynomial reduction
using the cited reflection and existing ordinary identities. Retain
every term, conjugation, rational twist and analytic scalar weight.
Check each resulting zero/single-gamma term individually on the fixed
right line and its holomorphic rectangle. For a zero-carrier series,
retain all exact resonances and bound the remaining primitive; for a
single-gamma series, retain its additive-phase arithmetic sum and both
branches, with normalization and endpoint signs. Partial summation may
keep the actual analytic weight rather than postulate a frozen constant.
No signed sum need be evaluated or claimed nonzero for this test.

Seek total connector and theorem-remainder error o(H(log H)^2), compared
explicitly with the required threshold. This is a compatibility threshold
aligned with L406, not an asserted cubic main scale. An exact reduction
with a controlled residual and an unevaluated finite arithmetic expression
would be a useful local input; an O(H log^2 H) signed bound alone does
not establish a scale, sign or cancellation.

Stop this implementation if a surviving orientation cannot be reduced
to the assessed zero/single-gamma forms, or if a coefficient/connector
hypothesis fails at the stated threshold. Record the precise surviving
term or failed bound; do not import Bui's unproved Theorem 5.1, approve
a new higher-carrier theorem, or reopen the complete signed mean in that
turn. This is an independently testable target, not repetition of the
step-103 broad comparison. L394/L399/L400 stops remain intact.

Essential continuation inputs: L369, L390, audited L405/L406 and audited
L391 ordinary/reflection/contour tools, plus the cited sources. The
complete decomposition and connector comparison are unresolved
application obligations. Even a successful reduction leaves full-tail
arithmetic at a signed scale, scale/sign, clipping, regulator choice,
total L367 margin/remainder, actual common-zero upper counts and global
mixed positivity unresolved. Full matching Mathlib coverage was not
checked; no absence or formal verification is asserted.

This newly completed assessment proposes a ready bounded continuation.
The supervisor supplies its separate approval next turn; this literature
turn does not perform the algebra or assert the continuation succeeded.
