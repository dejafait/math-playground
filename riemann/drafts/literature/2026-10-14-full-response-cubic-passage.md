# Full-response signed cubic passage — completed source comparison

TARGET: Establish the full-response signed cubic asymptotic at scale H(log H)^2 by passing from L408 with H tending to infinity before N.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 116 reused steps 103/107/112/114 and narrowly searched uniform rational-twist gamma primitives, shifted triple-divisor summation and twisted third moments; retrieved the original Gonek proof cases, an explicit single-frequency remainder in the Milinovich–Ng author manuscript and the Julia-lines restatement. No matching full-response theorem or completed local duplicate was established by this bounded search; no novelty follows.
SOURCE_EVIDENCE: Gonek, Invent. Math. 75 (1984), Section 4, Lemmas 1–5, especially Lemma 2 p. 130 and Lemmas 4–5 pp. 131–132; Milinovich–Ng, author-hosted 19-page Lower_Bounds.pdf, Lemma 6.1 p. 9; Steuding–Suriajaya (2020), Section 2 between (18)–(19); Fazzari 2306.15553v1, (1.3), Theorem 1.1, Lemma 3.2 and (3.5); DLMF 25.2.1 and 25.11.5; audited L407/L408/L391/L406 scopes reused.
COMPARISON: Fixed-head asymptotics and absolute cubic moments do not themselves justify the required sequential limit. The inspected frequency-level kernel exposes endpoint and twist dependence before coefficient summation, permitting a later bounded uniform-tail specialization; no inspected theorem states the complete local statistic or its full-response limit.
GAP: Still unproved are an N-independent signed-tail estimate at H(log H)^2, summable control of every kernel/connector/resonance contribution, convergence of beta_N and the sequential passage. These are application obligations for a later attempt; no essential source remains unread for that bounded test. Clipping and the main positivity/count gaps remain independent.
REASON: Approve source coverage for one separate bounded attempt on the unchanged target, using the explicit kernel rather than assuming uniformity in an O_N term; no tail theorem, coefficient limit or new mathematical result is derived in this literature turn.
LITERATURE_REASON: The changed full-response target needs parameter dependence hidden by the assessed fixed-twist statements; the original endpoint cases and explicit frequency-level remainder are essential new coverage. Ready finite-head and physical-transfer assessments are reused.
SCOPE: Actual ordinary critical jets through order two, complete response zeta(5/2+it), both zero/single carriers, sharp dyadic endpoints and H first then N. Uniform summation is a proof obligation, not an imported conclusion; no clipping, growing-N asymptotic, regulator selection or RH premise is approved.
COVERED_TARGET: Establish the full-response signed cubic asymptotic at scale H(log H)^2 by passing from L408 with H tending to infinity before N.

## Original proposed scope, preserved

Use the full response Z=sum_(n>=1)n^(-5/2-it), and the complete d and
B0 corresponding to L407's d_N and B0_N. Required input IDs are L408,
L407, L391 and L406; definitions and physical-transfer scope also require
the narrowly relevant L390/L405 passages. No cross-notebook input is
proposed. Reuse existing cubic source exclusions and ready assessments
only within their stated scopes.

The proposed discriminating tail threshold is

    lim_(N->infinity) limsup_(H->infinity)
      |integral_[H,2H] (d B0-d_N B0_N) dt|/[H(log H)^2]=0.

This is a requested estimate, not a proved assertion. Assess whether
known signed mean-value tools cover it, and whether convergence of the
explicit beta_N series and sequential passage suffice for the desired
full-response asymptotic. Do not silently replace a signed-tail estimate
by an absolute envelope at a larger logarithmic scale. A citation must
cover every ordinary derivative, rational twist, response tail and sharp
endpoint needed by the selected implementation. An adequate primary
assessment can approve a later bounded mathematical attempt; an
obstruction must be recorded at its actual threshold.

Unresolved assumptions: this tail estimate and coefficient passage,
clipping, regulator choice, total L367 margin/remainder, actual common-zero
upper counts and global actual-theta mixed positivity. The audited fixed-N
coefficient is a benchmark, not an RH criterion or candidate solution.
No full-response proof or new source approval is supplied in step 115.

## Completed comparison — 2026-10-14, step 116

The original proposal above is preserved; its pending coverage status is
superseded by this comparison. ADVANCE denotes newly usable local source
coverage, not a proved tail bound or progress beyond the inspected sources.
No lemma, mathematical script or certificate was created or changed.

The main gap is global actual-theta mixed positivity. The intermediate
target is exactly TARGET above: a full-response signed cubic asymptotic
with the stated sequential limits. Its plausible downstream use is a
complete signed benchmark for a later clipping/sign-imbalance test, using
L406 for physical transfer. Success here would not supply that clipped
estimate, a regulator choice, a total L367 margin or common-zero control.

### Reuse, discovery and failures

Read L407's exact carrier identity (3), coefficient bounds (4)–(5),
ordinary-jet formulas and complete reduction (8)–(9); L408's hypotheses,
coefficient, fixed-twist pole/Mellin argument and weight passage; L406's
absolute cubic transfer; L391's value-tail argument; and narrowly relevant
L390/L405 definitions. The step-115 audit is reused, not repeated.
Narrow searches of the recent cubic drafts, assessments and histories
found only explicit deferrals of this passage, not a completed duplicate.

Reused step 103's discovery/exclusions, step 107's fixed-carrier coverage,
and steps 112/114's Hurwitz and coefficient assessments. Read the three
L394/L399/L400 ATTEMPTS records: their failed weights are different
targets and remain stopped; they neither forbid nor establish this cubic
passage. L391's quartic tail argument has a different normalization.
L406 controls the absolute critical cubic envelope at logarithmic exponent
9/4, while the present target has exponent 2. That comparison does not
license the fixed-N limiting argument at the smaller scale.

New locator queries included `zeta function Gonek lemma rational twist
uniform error gamma Dirichlet series q`, `Gonek lemma uniformly Dirichlet
series gamma`, `Gonek lemma stationary phase integral rational twist`,
`Fazzari shifted triple divisor rational additive twist uniform modulus
Voronoi 2306.15553`, and `twisted third moment zeta unconditional`.
Followed the explicit kernel lead to primary author manuscripts and the
original proof. Search snippets were locators, not theorem evidence.
No global absence or novelty conclusion follows from these searches.

### Primary inputs and exact qualifications

S. M. Gonek, *Mean values of the Riemann zeta-function and its derivatives*,
Invent. Math. **75** (1984), 123–141,
[author-hosted scan, Section 4](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=7).
Read Lemmas 1–5 and their relevant proofs, pp. 129–132. Lemma 2,
p. 130, distinguishes a saddle in the dyadic interval, its endpoint
transition neighborhoods, and exterior saddles. Its proof uses stationary
phase centrally and integration by parts for the complementary pieces.
Lemma 3 retains fixed logarithmic weights; Lemmas 4–5 sum the unscaled
integer frequencies. The last summation cannot simply be asserted for
the present rational grid. Import the kernel estimate and check that
changed summation locally; no reproof of stationary phase is proposed.
These analytic lemmas are unconditional, unlike some zero-moment
applications elsewhere in the paper.

M. B. Milinovich and N. Ng, *Lower bounds for moments of zeta'(rho)*,
[author-hosted 19-page manuscript, Lemma 6.1, p. 9](https://home.olemiss.edu/~mbmilino/Lower_Bounds.pdf#page=9),
retrieved 2026-10-14; the displayed manuscript has no reliable version
date and a placeholder publication DOI. It is not arXiv:0706.2321v1,
which has seven pages. With r,kappa_0>0 and kappa_0<=kappa<=2 it states

    (1/(2pi i)) integral_(kappa+i)^(kappa+iT)
                   chi(1-s) r^(-s) ds
      = indicator_{0<=r<=T/(2pi)} exp(-2pi i r)
        + O(r^(-kappa) [T^(kappa-1/2)
             + T^(kappa+1/2)/(|T-2pi r|+sqrt(T))]).

The proof cites Gonek Lemma 2 and Stirling. Read the complete displayed
remainder and its adjacent coefficient-summation application. The lemma
has no RH/GRH hypothesis; the manuscript's later character-error bound
does, and is excluded here. This frequency-level formula retains the
endpoint transition explicitly. It does not itself sum the notebook's
response triples, weights or jets. The published Lemma 5.2 was a locator;
its inaccessible full text is not an additional premise.

J. Steuding and A. I. Suriajaya, *Value-distribution of the Riemann
zeta-function along its Julia lines*, Comput. Methods Funct. Theory
**20** (2020),
[Section 2, between (18) and (19)](https://link.springer.com/article/10.1007/s40315-020-00316-x),
was read as a comparison: it displays the gamma-primitive remainder
O(m^alpha T^(alpha-1/2+epsilon)), both exponential branches, series
coefficients subpolynomial in the index, and 1<alpha<=2. Its displayed
positive-branch exponent is written a rather than alpha. Do not use this
typographic ambiguity, or an implicit coefficient constant, as uniform
infinite-response coverage. The precise single-frequency bound above is
the selected input. Sourmelidis–Steuding–Suriajaya 2007.14008v2, Section 3
between (35)–(36), is reused only in its audited fixed-parameter scope.

A. Fazzari, *A Voronoi summation formula for the shifted triple divisor
function*,
[2306.15553v1, 27 June 2023, (3.5)](https://arxiv.org/html/2306.15553v1#S3),
was narrowly rechecked with (1.3), Theorem 1.1 and Lemma 3.2.
Its shifts are independent complex parameters, with coprime additive
numerator/modulus; the progression identity includes nonunits and the
zero residue. Theorem 1.1 uses a Schwartz function supported in the
positive half-line. It is not the required sharp infinite-response
estimate. Reuse audited L408 at each fixed twist; do not derive a
growing-modulus residue asymptotic or use the previously flagged expanded
polar-factor display. The full Voronoi transformation is unnecessary
for the selected bounded test.

[DLMF 25.2.1](https://dlmf.nist.gov/25.2.E1) supplies the absolute
Dirichlet series for real part greater than one.
[25.11.5](https://dlmf.nist.gov/25.11.E5), Apostol (1976), (25), p. 269,
has real part positive, s!=1, a>0 and nonnegative integer cutoff.
These support the already assessed fixed-twist tools. No new DLMF
release date is certified. Curran–Heycock 2403.00902v1 Theorem 1.1/(2)
and its derivative cases are reused through audited L406; they supply
absolute power-three bounds, not a signed asymptotic.

### Bounded specialization and continuation/abandonment test

Coverage is SPECIALIZE for a later proof attempt, not IMPORT of the
desired asymptotic. Retain L407's exact zero/single-carrier identity and
ordinary jets, rather than seek a new general third-moment theorem.
Apply the explicit kernel before summing the rational response twists;
use L407's coefficient bound and analytic-weight variation. Preserve
both sharp endpoint errors and all exact zero-carrier resonances.
The mathematical work must exhibit summable parameter dependence,
including small and large rational frequencies, not merely O_N constants.

One permitted implementation is a justified auxiliary response cutoff
depending on H: use L406's absolute envelope only for the far response
tail, and obtain uniform signed-primitive bounds on the remaining
rational twists from the explicit kernel. Such an auxiliary cutoff is
not an assumed growing-N version of L408. The concluding limits must
still take H first at every fixed N. Alternatively sum an established
integrable rational-twist majorant directly. No bound for either
implementation is proved here.

The discriminating requirement is exactly the displayed signed-tail
limit in the original scope, together with a justified finite positive
limit of L408's beta_N series. The later proof must also justify all
series/contour interchanges, derivative orders, endpoint weights and
physical transfer via L406. A possible coefficient series is already
specified in L408; neither its convergence nor its infinite value is
asserted by this review. Do not reevaluate its audited finite algebra.

Continue if these obligations yield the required normalized vanishing
tail and sequential asymptotic. Abandon this uniform-kernel certificate
if an unavoidable response-parameter factor is not summable, an endpoint
or resonance contribution exceeds the scale, or only the larger absolute
cubic envelope is obtained. Preserve the actual failed bound; failure
of this certificate would not disprove the asymptotic or RH. A genuinely
new theorem outside this scope needs REVIEW_REQUIRED, not an improvised
source approval during mathematics.

Essential continuation inputs are audited L408, L407 (3)–(5), (8)–(9),
L391's ordinary-jet/polygamma/connector bounds, L406's physical transfer,
and the narrow L390/L405 definitions. Unresolved assumptions remain the
signed-tail estimate, coefficient convergence/passage, clipping,
regulator choice, total L367 margin/remainder, actual common-zero upper
counts and global mixed positivity. No phase independence or RH is
assumed. Full matching Mathlib coverage was not checked; no absence or
formal verification is claimed. This newly completed ready assessment
receives separate supervisor approval before a mathematical invocation.
