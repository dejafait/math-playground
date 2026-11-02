# Outer-variable period grouping: completed source comparison

TARGET: Assess full-period outer-variable grouping of L609's exact allocation, using the proposed single test integral_0^(2pi/11) G_11(a) da<0, against known results and recorded stops.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact Stein/period/allocation and stronger Fourier/Laguerre searches, plus the scoped local duplicate/failure comparison below, found no matching theorem for the selected integral in the inspected material; this does not establish novelty or absence.
SOURCE_EVIDENCE: Csordas https://arxiv.org/pdf/1309.0055v2 Remark 4.3(b), Theorems 4.4--4.6, pp.11--12; Dimitrov--Xu https://arxiv.org/pdf/1606.05011v1 Theorems 2.5--2.6 and proof, pp.5--6; Johansson https://arxiv.org/pdf/1802.07942v1 Sections 2--2.1, pp.2--4. Planat https://www.preprints.org/manuscript/202606.1957/v1 Definitions 1--3/Proposition 2 checked against L559 and the ready paired-tail/nonlocal assessments. Reused numerical-tail/arithmetic coverage and exact URLs specified below.
COMPARISON: The inspected transform, convexity and block statements concern different quantities or conditional signs, not the first-period integral of L609's G. L609's fixed-a negative witness, C604b's total cancellation and L559's retained block endpoints do not decide this integral. Known box inclusion supports a bounded test, with its new domain/endpoint application still to be proved.
GAP: The grouped sign is uncomputed. A research continuation must certify the entire triangular domain, a=0, irrational endpoint, moving J and H, uniform positive denominators, theta/spatial tails and all arithmetic/integration errors. No all-group or higher sign follows.
REASON: Essential source comparison for this changed allocation is now complete enough for one bounded calculation. No source sign, new identity, numerical result or new algorithm is claimed by this literature-only review.
SCOPE: Exactly x=11 and the first interval [0,2pi/11], with unchanged p=k/Z, q, J and full four-term K. The separate continuation below specifies real-box inclusion and its required specialization; no wider frequency, interval or grouped-positivity search.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED nomination changes a fixed-a witness into an outer integral with an irrational endpoint and moving triangular domain; the ready single-point assessment did not cover this application.

## Result of the review

The main gap is actual-Xi all-degree positivity at unbounded heights.
The intermediate target remains exactly the proposed negative test for
the first-period integral. It could reject a different sufficient
first-sign allocation, in which complete outer groups rather than
individual a values must be nonnegative. A positive enclosure would
only remove this one proposed obstruction. All other groups/frequencies,
their complete sum with the floor, and higher signs remain independent.

Continue to one calculation only after separate next-turn approval of
`2026-11-01-theta-first-period-integral-test.md`. A strictly negative
upper endpoint stops universal grouped nonnegativity for this allocation.
A nonnegative lower endpoint rejects this particular negative-witness
proposal; a zero-straddling enclosure or exhausted error budget is
inconclusive. In each case stop this test without a larger sweep unless
a materially refined mechanism is separately assessed. None of these
outcomes determines D or RH.

## Primary theorem comparison and reuse

Reopened George Csordas, *Fourier transforms of positive definite kernels
and the Riemann xi-function*, arXiv:1309.0055v2, 21 February 2014.
Remark 4.3(b) averages the theta cosine transform over frequency from
zero; Theorem 4.4 gives positivity of the cosine transform of
Phi(sqrt(t)), using its strict convexity. Neither integrates this
Stein allocation over its outer spatial variable. Theorems 4.5--4.6
give admissible associated kernels and the all-degree positive-definite
criterion; they supply no grouped sign. Open Problem 4.7 is historical
context, not a present-day status assertion. The auxiliary square-root
density cannot replace L609's p. No new specialization of these sign
claims is imported.

Reopened Dimitrov--Xu, *Wronskians of Fourier and Laplace Transforms*,
the PDF served as arXiv:1606.05011v1 (header 16 June 2016, manuscript
footer 21 November 2021), Theorems 2.5--2.6 and the determinant/Fourier
proof, printed pp.5--6. The former assumes f and t^(2n-2)f integrable;
the latter uses an even nonnegative measure with the stated moments.
Its Fourier conclusion is positive definiteness, which does not assert
pointwise nonnegativity or allocate a truncated Stein layer. Its
Laplace-domain conclusions concern another transform. The prior
assessment's normalization/strictness qualifications remain; no
Wronskian constants or strictness assertion is used here.

Reused `2026-11-01-theta-integrated-layer-compensation-scope.md` for
Saumard v3 Section 2 (5)--(6), and the ready C604a actual-theta and
independent L609 audit assessments. Their connected-support, moment,
Stein-test integrability, endpoint and density hypotheses are unchanged.
No reproof of the Stein identity, theta shape, numerical inclusion or
arithmetic specifications is needed. The new finite-domain application
and its error propagation are the difference requiring mathematical work.

Johansson, *Numerical integration in arbitrary-precision ball arithmetic*,
arXiv:1802.07942v1, 22 February 2018, Section 2 algorithm step 2,
printed p.2, encloses a finite interval using an enclosure on its whole
input. Sections 2--2.1, pp.2--4, distinguish that rule from the analytic
Gaussian branch and make the returned radius decisive when tolerances
or evaluation limits fail. Repeated real inclusion is supporting
machinery, not a theorem about this moving triangle or its sign. The
continuation must verify its parameterization and all endpoint uncertainty;
complex analyticity is not assumed. This review does not implement it.

For theta/derivative tails reuse Johansson, *Numerical Evaluation of
Elliptic Functions, Elliptic Integrals and Modular Forms*,
https://arxiv.org/pdf/1806.06725v1, Section 1.2, p.4 and Section 1.4.2,
(1.18)--(1.20), pp.12--13, as assessed in the ready compensation review.
Its geometric-tail method does not automatically convert z derivatives
to the u derivatives of k. L609 already supplies explicit u-derivative
and complete spatial envelopes; their stated domains must cover every
new evaluation box. The audited CPython v3.15.0 arithmetic reference is
https://raw.githubusercontent.com/python/cpython/v3.15.0/Doc/library/decimal.rst,
named entries Decimal, Context, Rounding modes, copy_negate/copy_abs,
exp and next_minus/next_plus. Reuse its guarantees and L609's exact
Machin/Taylor construction, not its singleton numerical values as
uniform bounds. No new library/API or source-proof audit is claimed.

## Duplicates, endpoint failures and search scope

Specific local reads: L609's definition, normalization cancellation,
full certificate method and audit; L604's complete kernel, triangle
assembly and convergence; C604a/C604b; L016/L019 and L564's complete
kernel envelope. Searched the November 1 theta assessments and the
October 31 Stein records for period/group/block. The selected integral
was found only as the supplied nomination, not an earlier certificate.
Retained the fixed-a ATTEMPTS stop and the pointwise/generic Stein stops.
L607 is an audited generic contrast, not a mathematical input here.

A primary search hit was Michel Planat's *Curvature Transition Layers
and Paired-Tail Positivity*, Preprints.org 202606.1957 v1, posted
26 June 2026 (page labels it not peer-reviewed). Definitions 1--3 use
Phi(a+b)Phi(a-b), a y-dependent envelope and phase-aligned blocks for
sin(2xa), unlike this G. Proposition 2's Taylor proof concerns one
C^2 weighted sine integral; it is not a sign theorem for G. Reused
`2026-10-31-paired-tail-endpoint-cancellation-audit.md` and
`2026-10-31-nonlocal-paired-tail-remainder-comparison.md` rather than
reopening their mathematics. L559's canonical conclusion and the two
ATTEMPTS records retain weighted corrections on a complete block.
The later source, https://www.preprints.org/manuscript/202608.1692,
Theorems 4--6, has compact-region/fixed-y hypotheses and does not
provide a separately signed total residual. This is already assessed
coverage, not a new audit of that source. Its negative blocks are not
witnesses for G. No endpoint deletion or y-to-zero transfer is licensed.

Queries issued for this review:

- `"Riemann" "theta" "Stein kernel" period positivity`
- `"Laguerre inequalities" "period" kernel integral`
- `"Fourier transform" positivity "full periods" decreasing kernel`
- `"Stein kernel" "period" "Fourier" positivity`
- `"Laguerre" "theta" "period" positivity integral kernel`
- `"Stein" "layer" "truncated Fourier" positivity`
- `"Pólya" "cosine transform" "convex" positivity theorem`
- `"theta" "Stein" "allocation" integral positivity`
- `"Riemann xi" "period grouping"`
- `"Laguerre inequality" "truncated" "integral" theta`

Many hits were unrelated. Csordas--Varga finite-transform leads,
growing-order/filtered-Hardy papers and non-primary web journals were
not inspected as new theorem inputs; none supplies an asserted G sign.
The ready assessed theta/transform statements above cover the relevant
comparison. This bounded search is not a novelty certification.

No essential source blocker remains for a direct-real-box test. Full
matching/supporting Mathlib coverage for the grouped integral is
unchecked; L016 retains its existing supporting theorem links.
No cross-notebook input, new lemma, script, DAG or PROOF change is made.
A creative proof attempt remains unjustified without an independently
controlled signed-theta coupling: this single allocation discriminator
does not supply one. It is a calculation continuation, not a relabeled
creative mechanism or another approval/audit of L609.

## Original nomination (historical; source comparison completed above)

This is a nomination, not an approved research target or a sign claim.
Keep exactly L609's p=k/Z, q, J and full four-term K, with its floor
and source-proof qualifications. The candidate groups outer a over
intervals whose endpoints have xa in 2pi times the nonnegative integers.
An entire period may retain cancellations that pointwise allocation
forbids; the density, weighted tail and partial cosine integral are
not periodic. Thus periodicity of trigonometric factors alone supplies
no positivity or endpoint cancellation. Assess that distinction rather
than assume a source theorem applies.

The bounded discriminator proposed for eventual coverage is the first
complete interval at the already selected frequency x=11:
integral from 0 to 2pi/11 of G_11(a). Its sign is uncomputed. A rigorous
negative upper bound would exclude nonnegativity of every such grouped
contribution, without another grid or any implication for total D.
Failure to find negativity would prove only the tested enclosure; it
would not sign other groups, frequencies, the floor plus sum, or higher
Laguerre forms. Stop rather than enlarge the interval/frequency search
without a refined mechanism. A complete grouped first-sign strategy
would still need all groups/frequencies and summability; higher signs
are independent. This proposal derives none of those claims.

Before mathematics, compare exact known integrated-allocation results,
stronger sign claims and failures, reusing the adequate prior Stein,
theta and numerical assessments where they really match. Search only
the relevant local allocation/Stein source records, L609 and its
direct inputs; no sibling notebook is needed. Read primary hypotheses
and any relevant endpoint cases before importing a theorem. If the
target survives, specify rigorous inclusion for the curved/triangular
domain, the irrational endpoint, kernel/weighted-tail divisions and
the complete error budget. Existing single-a arithmetic does not
automatically certify this two-variable integral. Full and supporting
Mathlib coverage remains unchecked.

The main gap is actual-Xi all-degree positivity at unbounded heights.
The proposed downstream use is a different sufficient first-sign
allocation; no independently controlled signed-theta estimate yet
justifies routing it as an approved creative proof. Prepare its missing
coverage first. If review identifies a substantive new coupling with a
discriminating proof test, a later proof_attempt/creative nomination
must name that mechanism and decisive evidence explicitly. No new lemma,
mathematical derivation, source approval or computation accompanies
this nomination.
