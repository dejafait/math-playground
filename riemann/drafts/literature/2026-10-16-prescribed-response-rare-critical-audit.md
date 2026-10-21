# Source coverage for the prescribed-response rare-kernel audit

TARGET: Critically audit L418's capped prescribed-response rare kernel, including exact quartic preservation, fiber probability and all noncubic bounds.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 158 searched the scoped step-150/154/155/156/157 assessments, audit records and radial-lift/fixed-moment failures; read L418 in full and relevant L390/L406/L414/L416/L417 definitions and source applications. L419's audit checked necessary rare inputs but expressly left the complete L418 audit pending. Reused adequate primary assessments; no new external search or novelty claim.
SOURCE_EVIDENCE: Reuse Curran--Heycock arXiv:2403.00902v1 Theorem 1.1/(2), Sections 3.1 and 4 as inspected in step 105 and reused in step 156; Bui--Hall arXiv:2304.05178v1 Theorem 3, Proposition 3, Sections 5/7 and Introduction equation (1), as inspected in steps 44/146/148; and the step-150 Aumann/Jaskiewicz--Nowak framework comparison. Exact source qualifications and local applications are recorded below; none is newly retrieved this turn.
COMPARISON: Existing unconditional sharp-interval bounds cover actual fourth and absolute third moments of the fixed ordinary jets through order two. The explicit capped finite kernel needs no selection or purification theorem. The remaining difference is verification of its exact same-height polynomial homogeneity, probability, all lower-degree estimates and fixed pointwise constants; sources do not establish this construction or evaluate its cubic.
GAP: No essential unread source is identified for this bounded audit. The construction itself remains unaudited: check both cap regions and rho=0, all 23 quartics and U^2, matrix positivity, lower-degree bounds, uniform constants/onset and the exact unevaluated F_lambda identity. The capped asymptotic and full-law feasibility remain outside approval.
REASON: Separate source-scope comparison approves the unchanged TARGET for one later REPRODUCTION proof_audit; this is readiness only, with no new mathematical result or completed proof audit.
LITERATURE_REASON: Step 157 selected the outstanding independent L418 audit as REVIEW_REQUIRED after stopping a different fixed-moment certificate; this turn supplies its required scope approval using ready sources rather than repeating capped-cubic or clipping discovery.
SCOPE: Exactly L418 at fixed lambda>0, with the actual uniform height/response graph, ordinary jets through order two, exact curvature, every sufficiently large real H and fixed constants; no conditional independence, cap removal, actual/global critical realization, cubic equality or regulator margin.

The main gap remains actual negative-Bcal clipping and L413's full
regulator margin toward global mixed positivity. This audit can validate
or repair a necessary partial prescribed-response construction, without
evaluating its still-missing capped cubic or resolving RH.

Essential input IDs are L418, L390, L406, L409, L414, L416 and L417;
L419 is relevant only to the precise downstream bulk interface, and
L420 records the stopped cubic certificate. Those inputs remain the narrow proof-audit reading scope. Reuse adequate prior primary
assessments rather than reopen the blocked direct clipping search.

The following obligations were proposed before approval and remain
mathematical checks for the separate audit. It should
check p=(rho/max(lambda ell^2,rho))^4, the oriented output, both cap
regions and rho=0, exact uniform height marginal, preservation of all
quartics and U^2, matrix positivity, the small first-moment and absolute
cubic bounds, qualitative pointwise envelopes with fixed constants,
and the exact unevaluated F_lambda identity. Verify every sufficiently
large real H with fixed lambda; no height relocation, independence,
actual/global critical realization or regulator margin is supplied.

Continuation/abandonment test: validate these conditional assertions or
identify a precise false bound, unsupported input or missing uniformity
and repair only within the approved audit scope. Do not turn a successful
partial audit into a full-law claim. F_lambda=beta_* ell^2+o(ell^2),
actual clipping and global positivity remain unresolved independently.
Full matching Mathlib coverage is not checked. No new theorem, source
import or mathematical derivation is made in this source assessment.


## Completed comparison — step 158

This is LITERATURE / NOVELTY_UNCHECKED / literature_comparison, outcome
EXPLORATION. It approves a concrete independent audit, without validating
any L418 identity or bound. No lemma, mathematical script, PROOF.md or DAG.md
was changed. Source readiness is local process progress, not progress
beyond the checked mathematics.

### Reused primary hypotheses and exact applicability

M. J. Curran and A. Heycock, *Sharp bounds for joint moments of the
Riemann zeta function*, [arXiv:2403.00902v1, 1 March 2024](https://arxiv.org/html/2403.00902v1),
Theorem 1.1/(2), Sections 3.1 and 4. The inspected theorem allows fixed
order n, 0<=k<=2 unconditionally, nonnegative h_j with sum h_j<=k,
on the sharp interval [T,2T], with exponent k^2+2 sum j h_j for the
integrand |zeta|^(2k-2 sum h_j) product |zeta^(j)|^(2h_j).
The [step-105 assessment](2026-10-13-cubic-physical-replacement-audit.md)
records the equality-endpoint and all relevant Section 4 cases: Cauchy,
reflection, integral interpolation and sharp-rectangle approximation.
The [step-156 assessment](2026-10-16-capped-rare-cubic-asymptotic.md)
reuses this same scope. L406's separately audited application takes
n=2, k=3/2, with all h_j zero or one of h_1,h_2 equal to 3/2.
It includes the phase terms in the ordinary real derivatives, giving
the actual rho third-moment input. This is a bound on actual inputs;
it is not a moment theorem for conditional output states, a restricted
radial moment, or a capped-cubic asymptotic. No reproof is warranted.

H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
Bull. Lond. Math. Soc. 55 (2023), 2304--2323,
[DOI 10.1112/blms.12859](https://doi.org/10.1112/blms.12859),
[arXiv:2304.05178v1, 11 April 2023](https://arxiv.org/html/2304.05178v1),
Theorem 3 and its defining asymptotic, Proposition 3 in Section 4.2,
Sections 5/7. Reuse the primary extraction recorded in
[step 44](2026-10-10-discriminant-second-moment-leading-scale.md)
and [step 148](2026-10-15-compatible-jet-second-moment-critical-audit.md).
It covers the fixed-order quartic Hardy-jet envelopes, using uniform
small complex shifts for Cauchy differentiation. L390 imports their
unconditional fourth-power upper bound for j=0,1,2 with the divisors
applied after differentiation. L418 only needs this actual upper bound
and existing actual quartic observables; it proposes no new twisted
moment, growing derivative order or shifted-moment differentiation.

For the inherited six-second-moment list, the same Bui--Hall v1,
Introduction p. 1 equation (1) and preceding odd-order display, is
already inspected in [step 146](2026-10-15-compatible-jet-second-moment-scope.md).
It gives a monic cumulative polynomial with error
O(T^(3/4)(log T)^(j+k+1/2)) for even j+k, and O(T^(1/3)) for odd
j+k. L416's audited sharp partial-summation specialization specifies
the actual list. L418 does not claim to match it with zero completion;
its matrix bound and missing leading covariance must remain explicit.
The underlying Hall theorem is an unread independent source and is not
an additional premise. No new second-moment calculation is approved.

The [step-150 comparison](2026-10-15-compatible-jet-actual-response-marginal.md)
already inspected Aumann (1965), Theorems 1--4 and Proposition 2.1,
and Jaskiewicz--Nowak arXiv:1712.07577v1 Section 2, Theorem 1 and
Lemma 1/proof. Their measurable-graph, integrability and atomlessness
qualifications do not supply prescribed moments of a nonexistent kernel.
L418 writes explicit Borel atoms and weights, so no application of those
theorems is essential. The later audit must check measurability and
fiber normalization directly, including the zero-radius branch.
No additional source retrieval is needed for a finite mixture.

### Exact local scope, duplicates and stopping evidence

L414 defines the exact linear P conversion with bounded alpha and q,
the unchanged V response, quadratic ell_F, linear Bcal, quadratic Delta,
and linear omega. L417 fixes these at the actual height and uniform
base measure. These are the inputs to check, including q, before any
homogeneity assertion is accepted. Count the quartic list as Delta^2,
Delta Bcal^2 and all 21 Delta omega_i omega_j, with signed off-diagonal
entries; U^2 is a separately retained fourth-degree envelope. Do not
replace the actual response by its leading carrier or a separately
chosen response law. Existing L390/L406 bounds concern actual X0;
transfer to the output distribution is precisely the audit obligation.

The step-155 L419 audit and its history explicitly leave L418's complete
audit pending, despite checking some load-bearing rare inputs. Thus this
audit is independently testable and not a repetition of the completed
bulk audit. Preserve the radial-lift failure in
ATTEMPTS/2026-10-16-actual-response-capped-radial-lift.md: zero completion
does not meet the full list and O(1) odd entries cannot be charged to
tiny final tolerances. L419 supplies a separate audited bulk, not an
evaluation of the capped cubic. Preserve the step-157 stop in
ATTEMPTS/2026-10-16-capped-cubic-fixed-moment-certificate.md and L420;
this approval authorizes no repeated magnitude-envelope optimization.

The later audit should check the formulas, both cap regions, rho=0 and
sign boundaries, absolute integrability, all powers of the radial scale,
fixed lambda, and common constants/onset for every sufficiently large
real H. Accept the conditional partial construction if all claims pass;
otherwise record the precise defect and repair or narrow it only within
this scope. Do not infer feasibility of the full list from a correct
rare component. Inputs L390/L406/L409/L414/L416/L417 and L418 remain
essential; L419 is the downstream interface and L420 only stop evidence.
F_lambda=beta_* ell^2+o(ell^2), actual clipping, L413's full-error margin,
actual/global realization and global mixed positivity remain unresolved.
Full matching Mathlib coverage is not checked; absence is not asserted.
