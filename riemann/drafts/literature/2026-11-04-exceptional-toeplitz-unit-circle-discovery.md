# Exceptional Toeplitz unit-circle mechanism — source comparison

TARGET: Assess whether a Heine–Szegő unit-circle determinant integral for actual-Xi exceptional minors k=r-1 supports one bounded signed saddle test distinct from the stopped real-moment and q-Pascal routes.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step418 found the already assessed exact angular representation in step389; inspected primary Katkova hypotheses/proof cases and Blackstone–Charlier–Lenells' varying-symbol theorem; searched actual-Xi/Heine/Toeplitz/growing-order terms and scoped local failures. Details below; no originality claim.
SOURCE_EVIDENCE: Reuse 2026-11-04-actual-toeplitz-signed-integral-review.md for Katkova math/0505174v1 Lemmas1–2/(10)–(13), pp.7–8 and fixed-order proof; additionally inspected Lemma4(c) and its proof pp.11–12, (32)–(35) pp.13–14. Blackstone–Charlier–Lenells 2212.06763v2 Theorem1.1/(1.1)–(1.12), pp.1–3, (1.16) p.4 and (3.5)–(3.10), pp.12–13 were read.
COMPARISON: The proposed Heine representation duplicates step389 exactly. Fixed-order positivity does not cover r=k+1. The inspected varying-symbol theorem needs a real analytic leading potential with full-circle strictly positive equilibrium density, plus analytic background and restricted Fisher–Hartwig data; no such reduction or uniform error bound is established for the shifted Xi symbol.
GAP: No exceptional minor sign or signed collective saddle estimate follows. A shrinking-box core with an absolute complement budget is independently testable; its growing-order modulus-mass comparison is not supplied by the sources checked.
REASON: Reject a new-representation claim and automatic Szegő import. Prepare one quantitative concentration obstruction test before further investment in this particular local-core sign certificate; do not reject all possible angular cancellation mechanisms.
LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED and needed essential determinant-integral and varying-dimension source comparison; step389 coverage was recovered and reused rather than rederived.
SCOPE: Literature-only comparison for actual a_n=M_(2n)/(8*4^n*(2n)!) and D_(r,r-1), r>=2. No new integral derivation, lemma, script, saddle calculation or sign result. The proposed test has its own assessment and requires separate approval.

## Nomination retained from startup

The following records the original question and missing-coverage status;
the completed comparison below supersedes its prospective instructions.

Main gap: actual-Xi all-degree mixed positivity. The intermediate aim is
an independently testable signed estimate for exceptional actual minors,
using a unit-circle integral rather than a pointwise real-moment sign or
the q-Pascal symmetric part. Such an estimate could help pay exceptional
signs; other centers, initial orders and full mixed positivity remain open.
No positive symbol, real-rootedness or favorable saddle geometry is assumed.

Essential continuation inputs are L018/L021 for the coefficient convention,
and the audited L765/L774 stops for comparison. L766's recorded real-moment
pointwise-sign stop and the step407 condensation/multiplier assessment must
be checked narrowly for overlap; L766 is unaudited and is not a theorem input.
No cross-notebook input is proposed. The current audit establishes no
unit-circle theorem, complex-contour justification or effective onset.

First inspect primary determinant-integral statements with all hypotheses,
normalization, symbol/shift conventions and relevant proof cases. Search
the actual-Xi Toeplitz/saddle terminology and stronger existing results.
Ordinary positive-symbol or fixed-symbol asymptotics must not be transferred
to a possibly complex, shifted, growing-dimension setting without the exact
hypotheses. Retrieve only needed theorem passages before longer extracts.

Continue only if the review identifies one explicit bounded signed test
with a result/threshold, an error budget to be tested and a plausible use
for D_(r,r-1). Reject the proposed mechanism if its only available premise
is the missing minor positivity or RH, or if it reproduces a recorded stop
without a materially new input. If source access is persistently blocked,
park it and choose an independently testable target. A missing match is
not evidence of novelty. Mathlib coverage for this target is unchecked.

A creative proof attempt was not ready at nomination: the exact signed
integral interface and useful saddle control had not been assessed.

## Completed comparison — step418

Main gap: actual-Xi all-degree mixed positivity. The reviewed intermediate
aim was a signed angular estimate for D_(r,r-1), potentially supplying an
exceptional sign input. Other indices, initial orders and full mixed
positivity remain unresolved. A useful test must distinguish an estimate
from an identity equivalent to the missing sign.

### Recovered exact coverage and conventions

The substantive duplicate is the [step389 assessment](2026-11-04-actual-toeplitz-signed-integral-review.md),
not just a similarly named route. Reuse its complete angular formula and
applicability comparison. Katkova, *Multiple positivity and the Riemann
zeta-function*, [math/0505174v1](https://arxiv.org/pdf/math/0505174v1#page=7),
Section2 Lemmas1–2, pp.7–8, assumes an entire, nonzero f with nonnegative
ordinary coefficients, k>=0, dimension nu>=1, and any positive radius.
Its Cauchy/composition/Vandermonde proof and real-part sign equivalence
were read previously and their exact hypotheses rechecked here.

Set f=G with G(z)=xi(1/2+sqrt(z)/2)/8, nu=r, k=r-1. L018/L021
and the existing source normalization give exactly the required entire
function and coefficients; G(R)>0. The sine Vandermonde, r!, (2pi)^r
and R^(kr) factors in the existing formula are retained. In Fourier
language the shift is z^(-k)G(Rz); the two common row/column conventions
transpose the determinant. This compares the already recorded identity;
no new derivation, branch choice or positive symbol is assumed.

The fixed-order core/tail proof is already assessed in step389. Theorem2
has an order-dependent onset, not uniform coverage of k=r-1. Additionally
read Lemma4(c)'s complete proof: sectorial Stirling and upper/lower
Euler-product bounds in Re(s)>=2 provide its angular modulus input.
Read the scalar saddle choice (33) and local logarithm (32)–(35).
Only those inputs are proposed; the full analytic proof and auxiliary
derivative lemmas remain unaudited. The generated title-page date
does not change the cited version.

### A varying-dimension theorem does not supply the missing estimate

Elliot Blackstone, Christophe Charlier and Jonatan Lenells,
[*Toeplitz determinants with a one-cut regular potential and Fisher–Hartwig singularities I*](https://arxiv.org/pdf/2212.06763v2),
v2, 26 July2023; Proc. Roy. Soc. Edinburgh A154 (2024),1431–1472,
DOI10.1017/prm.2023.73. Read Theorem1.1, pp.1–3:
f=exp(-nV+W)omega; V,W analytic near the circle; V real there;
equilibrium density strictly positive with full-circle support.
Fixed finite singularity data require Re(alpha)>-1 and
|Re(beta)|<1/2, with separated locations in the stated compact set.
The logarithmic error is O(n^(-1+2 beta_max)); listed uniformity
concerns compact parameter ranges. Complex W is allowed.
Read (1.16) and (3.5)–(3.10): equilibrium-density positivity supplies
the off-circle decay used in opening lenses.

Our radius and shift vary with r. Neither a fixed analytic background
with controlled bounds nor the required real leading potential/density
has been exhibited. Taking a logarithm of the whole shifted symbol
also requires checking zeros and winding; W=log(symbol) alone is not
a theorem application. The Heine identity needs none of these
asymptotic hypotheses. No impossibility of every possible reduction
is asserted. This is a new inspected comparison, not an imported
actual-Xi sign input or full proof audit.

### Retained failures and one discriminating continuation

Read L766 completely to identify its exact real-moment test, without
auditing or using it as a premise. Its negative pointwise witness does
not determine the integral. Reuse audited L765/L774 conclusions as
contrasts for their specified q-Pascal norm/accretivity tests.
The [step407 comparison](2026-11-04-exceptional-coefficient-mechanism-discovery.md)
rejects identity-only condensation and an uninstantiated multiplier;
neither pays the angular phase. No stopped test is repeated.

The new [concentration assessment](2026-11-04-exceptional-angular-box-mass-test.md)
specifies one prospective attempt: compare actual modulus mass inside
and outside the shrinking scalar-saddle box. Its explicit threshold
would obstruct paying the entire complement by absolute values while
using only that core. Cancellation within the complement remains open.
No mass ratio, phase bound, saddle calculation or new mathematical
conclusion is established here. The new EXPLORE assessment needs
separate approval before research.

This is established-route development, not a justified creative sign
mechanism. A creative collective-contour attempt still lacks a specific
contour and independent signed error estimate. Source gates cannot be
bypassed to fill the creative scheduling preference.

### Search, source access and qualifications

Queries included `Heine Szego identity Toeplitz determinant integrable
complex symbol theorem integral winding number`, `Riemann xi Toeplitz
determinants Taylor coefficients minors asymptotic saddle point Katkova`,
`Riemann xi Toeplitz Heine`, and exact one-cut/author terms. Local searches
covered drafts/literature, ATTEMPTS, indicated same-day history and
selected coefficient lemmas. Step389 was the exact match; no exhaustive
duplicate exclusion or novelty is claimed.

Garcia-Garcia–Tierz (1706.02574) was a search lead, not an inspected
theorem input: its repository PDF open was restricted. It was unnecessary
after recovering Katkova. A BCL screenshot timed out; readable PDF text
supplied the relevant statement and proof passage. No essential source
blocker persists. The tilted-minor and k=1 preprints found by search were
not read or used. Mathlib matching coverage is unchecked. No cross-
notebook material, lemmas, scripts, PROOF or DAG were modified.
