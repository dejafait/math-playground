# L604 layer cancellation scale: completed source comparison

TARGET: Determine whether L604's M has a strictly positive x^(-2) leading term for nonconstant tau, and quantify the cancellation with R under the same density hypotheses.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed exact/stronger weighted truncated-transform, Stein-layer and endpoint-asymptotic searches listed below; checked the scoped Stein assessments, working notes and pointwise/generic stops for duplicates. No complete matching aggregate theorem was identified. Standard endpoint-error, nonstrict monotone-substitution and Fourier-decay results were inspected instead; a search miss is not novelty evidence.
SOURCE_EVIDENCE: Read NIST DLMF v1.2.8, Section 2.3(i), (2.3.4)-(2.3.6); Hunter, 2009 PDE Appendix 5.A, Definition 5.15, (5.11), Theorems 5.25/5.29 and the preceding L1 proof, printed pp.132,134-137; Riva--Nardini, 35-page author Preprint.pdf, Appendix A Lemma A.1/Remark A.2 and its full noninjective proof, printed pp.31-32. Direct URLs and version qualifications below; retrieved 2026-11-01.
COMPARISON: Known Fourier estimates and monotone substitution cover the analytic ingredients, including nonstrict monotonicity, but do not state the L604 aggregate or its coefficient. Remaining work is a standard applicability/aggregation calculation, to be classified REPRODUCTION, without reproof of the imported theorems. L604 is audited; L607 and the pointwise stop remain contrasts.
GAP: The coefficient, its positivity for nonconstant tau, a uniform integrable truncation error, treatment of the floor, and precise M/R cancellation remain to be proved. Essential source coverage is adequate for this bounded test; no asymptotic or Fourier sign is established in this literature turn.
REASON: Newly inspected error bounds and a noninjective substitution theorem remove the specific source gap, avoiding an unjustified inverse-tau or strict-monotonicity assumption. Citation alone does not assemble the weighted squared transforms or check their coefficient. Attempt that specialization once; retain all generic positivity stops.
SCOPE: Exactly L604's positive even smooth probability density with every derivative faster than every exponential, and its centered tail-ratio tau nonincreasing and nonconstant on the positive half-line. Permit endpoint expansion, uniform error checks, monotone layer aggregation, the coefficient test and comparison with D=M+R under these unchanged hypotheses. Retain flat portions, a possible positive limiting floor, both R signs and a separate constant-tau comparison. No density-family search, actual-theta transfer, integrated-sign theorem or higher-sign result is covered.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED target required its first quantitative Fourier comparison; ready Stein identity coverage did not cover this asymptotic. This supplies missing sources rather than rebrowsing a ready calculation.


## Inspected primary statements

1. **Endpoint estimates.** [NIST DLMF Section 2.3(i)](https://dlmf.nist.gov/2.3#i),
   v1.2.8 (15 September 2026), (2.3.4)-(2.3.6), gives the Fourier
   endpoint expansion for smooth q on a finite interval. Its stated
   nth remainder bound is x^(-n) times the variation of q^(n-1),
   defined as the integral of |q^(n)|. The infinite-endpoint case
   requires uniform convergence of the oscillatory derivative integrals
   for sufficiently large x. Both sets of hypotheses were read.
   The cited Olver, *Asymptotics and Special Functions*, 1997 reprint,
   pp.66-70,75-76, was not opened. Use the explicit variation bound
   when checking uniformity across truncation boundaries, rather than
   importing a pointwise expansion as uniform. The source gives no
   L604 aggregate coefficient.

2. **Nonstrict monotone substitution.** Filippo Riva and Lorenzo Nardini,
   *Existence and uniqueness of dynamic evolutions for a one-dimensional
   debonding model with damping*, [35-page author preprint](https://cvgmt.sns.it/media/doc/paper/3947/Preprint.pdf),
   Appendix A Lemma A.1, (A.1), Remark A.2 and proof, printed pp.31-32.
   Substitution holds for nondecreasing Lipschitz phi on a compact
   interval and nonnegative measurable g, hence also integrable g.
   The appendix explicitly allows nonincreasing maps with orientation
   changes. Its proof uses the area formula and establishes singleton
   fibres almost everywhere, including the noninjective case. Remark
   A.2 specifies Borel representatives in weighted compositions; retain
   that qualification. The local Lipschitz version suffices for smooth
   tau on compact intervals; passage to the half-line and levels below
   the limiting floor remain applicability obligations. No inverse
   derivative is required. This is the unversioned 35-page PDF served
   on the check date, not a differently paginated revision or journal
   copy. [Repository provenance](https://cvgmt.sns.it/paper/3947/)
   identifies its publication and revisions; they were not substituted
   for the inspected statement.

3. **Fourier decay.** John K. Hunter, *Notes on Partial Differential
   Equations*, [2009 Appendix 5.A](https://www.math.ucdavis.edu/~hunter/m218a_09/ch5A.pdf),
   Definition 5.15, (5.11), Theorems 5.25/5.29, printed pp.132,134-137.
   The Fourier transform preserves Schwartz space; 5.25 states the
   derivative/monomial identities. Theorem 5.29 maps L1 to continuous
   functions vanishing at infinity, with an L1-to-sup bound. The
   preceding approximation argument was read. The source uses
   (2pi)^(-n) integral f(u) exp(-ik.u) du; L604 uses an unnormalized
   positive exponent. Carry scalar and reflection consistently.
   The unchanged all-derivative decay assumption supplies the source
   regularity class for p; a new weighted oscillatory amplitude still
   needs its own L1 check. Riemann--Lebesgue alone gives no power rate.

These supporting standard results do not already state the complete
proposed diagnostic. Their specialization must connect the layers to
uniform truncation estimates and check the aggregate coefficient.
No coefficient, asymptotic or new mathematical estimate is derived
here. Theorems are imported, not reproved. This is sufficient coverage
for one standard calculation, with no originality claim.

## Search and overlap

New search queries included:

- `Fourier transform truncated smooth function endpoint asymptotic integration by parts Riemann Lebesgue weighted squared`
- `Stein kernel monotone layer cake Fourier transform Laguerre inequality`
- `"truncated Fourier" "squared" "asymptotic" endpoint`
- `"Stein kernel" "layer" "Fourier" asymptotic`
- `"weighted" "truncated Fourier transforms" asymptotic`
- `"Stein kernel" "layer cake"`
- `"Stein kernel" "truncated" "Fourier" asymptotic`
- `"squared" "Fourier integral" "endpoint" "weight" asymptotic`
- `"integrated" "truncated Fourier transform" "asymptotic"`
- `"area formula" "nondecreasing" "absolutely continuous" change variables`
- `"Lemma A.1" "nondecreasing" "Lipschitz"`
- `"change of variables" "nondecreasing" "Borel" absolutely continuous formula pdf`

Additional change-of-variables and Riemann--Lebesgue searches led to
the primary statements above. Truncated-FFT algorithm hits are unrelated.
Dimitrov--Xu, *Wronskians of Fourier and Laplace Transforms*,
arXiv:1606.05011, and quantitative Fourier-tail papers were leads only;
no theorem from them was inspected or imported. Other Stein hits
concern different estimates. No unread lead counts as coverage.

Scoped local searches covered the October 31 Stein assessments and
working notes, November 1 L604 source/audit records, post-L607 discovery,
and the pointwise/generic Stein ATTEMPTS. Their saved source comparisons
are reused as background; only needed records were opened, without
reloading old source packages. No completed weighted-layer high-frequency
result was found in that scope. The complete L604, relevant L233
normalization, L604 audit scope and both stops were read. This source
comparison does not repeat the identity audit. The known generic
counterexample does not obstruct a diagnostic with no Fourier-sign
claim, and the historical pointwise stop is not a ban on this test.

A Hunter--Nachtergaele book-chapter PDF lead had garbled extraction;
its search preview was not used as evidence. The accessible Hunter
Appendix 5.A above supplies the exact standard statements needed, so
this is not an essential source blocker. No sibling notebook or
cross-notebook mathematical input was read.

## Approved continuation and decision test

The main gap is actual-Xi all-degree positivity at unbounded heights.
This intermediate target measures the separate terms in L604's identity,
without signing the full determinant. Its downstream use is to identify
what cancellation accuracy a later integrated compensation estimate
must preserve. It leaves independent higher-sign and Xi-transfer gaps.

Use L604 and its L233 normalization. Check errors uniformly in the
truncation boundary before squaring or integrating; a fixed-layer limit
is insufficient. Preserve all levels, justify the treatment of flat
levels using the inspected substitution result, and retain the
untruncated-floor contribution. Check L1 of each amplitude before
Riemann--Lebesgue. Give the actual coefficient or a precise hypothesis
obstruction, distinguishing qualitative little-o from any stronger
power-rate or effective bound. No density-uniform or theta-height-uniform
constant is promised. Compare R and M through the full determinant
without discarding either signed remainder contribution.

Continue if the coefficient and an error smaller than the proposed
leading scale can be justified under the unchanged class, including the
constant comparison, flats and floor. Otherwise record the exact
obstruction and park this diagnostic. Do not strengthen hypotheses or
reopen generic positivity in the same test. A successful diagnostic
specifies an accuracy threshold; it does not establish D>=0. No
independently controlled creative theta-compensation mechanism is yet
specified, so this standard specialization is not labeled creative.
L605 is later applicability only, L607 a contrast, and L608 is not needed.
Mathlib full-result and supporting coverage remains unchecked; no absence
claim is made.

This literature-only step completes the missing source comparison and
changes REVIEW_REQUIRED to SPECIALIZE for the unchanged exact target.
The next mathematical step is REPRODUCTION. No lemma, mathematical
script, DAG or PROOF edit is made; existing unfinished work is retained.
The earlier nomination below is preserved as historical evidence and
its instruction to make the next invocation literature-only is superseded
by this completed review.

## Original nomination (historical scope, superseded above)

The main gap remains actual-Xi all-degree positivity at unbounded
heights. The intermediate target is the scale of the positive layer
term in the now-audited identity, independently of the sign of D.
If an algebraic positive leading term is present while the full
Fourier determinant decays more rapidly, future compensation must
retain the corresponding cancellation. This would help evaluate a
specific class of coarse absolute budgets; it would neither supply
the missing sign nor exclude more accurate theta-specific estimates.
No such asymptotic conclusion is asserted here.

The next invocation is literature-only. Search the exact statement,
the stronger weighted truncated-transform asymptotic, and the relevant
standard Fourier integration-by-parts/Riemann--Lebesgue results. Read
their hypotheses and needed proof cases before granting scope. Check
whether flat superlevel sets or a nonzero floor require a measure
formulation; do not silently assume strict tau monotonicity, an inverse
tau, or a missing boundary condition. A matching theorem should be
imported with the necessary applicability argument. If the claim is a
standard specialization, classify it accordingly, not as creative or
new mathematics. Failed searches do not establish novelty.

The mathematical continuation, only after approval, has one bounded
test: establish the actual leading scale and its coefficient or find a
precise counterexample/hypothesis obstruction within the fixed class.
Compare the full residual with the separate terms, retaining both R
signs. Stop after that test. A successful diagnostic must say which
error scale a later estimate would have to preserve; it must not label
the equivalent requirement D>=0 as a new sufficient estimate. Failure
of the proposed asymptotic parks that diagnostic without reopening
generic positivity or enlarging the density class in the same turn.

Essential local mathematical input for the proposed calculation is
L604 (and its use of L233). L605 is only a possible later actual-theta
specialization, with its source qualifications retained. L608 is not
needed; its conditional orbit imports cannot substitute for a Fourier
estimate. The post-L607 discovery and L607 are contrasts only. There
is no cross-notebook input. All integrated Xi signs and higher-degree
signs remain unresolved. Mathlib full-result and supporting coverage
for this new target is not checked.

This file nominates an uncovered target only. No asymptotic proof,
coefficient evaluation, new lemma, script or source approval occurred
during the L604 identity audit. There is still no specified justified
creative theta-compensation mechanism; the source comparison must
decide the value and scope of this independent diagnostic first.
