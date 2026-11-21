# Joint inverse-kernel sign test: nomination2234

TARGET: Attempt a direct two-real-zero inverse-kernel positivity test for actual roots x in (14,29/2) and y in (21,22): construct the exact even quotient kernel, seek a complete signed certificate on 0<=u<=1 and an analytic positive exterior for u>=1, or record the first rigorous obstruction.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed2234 exact/stronger Fourier division, real-zero removal, characteristic-function factor and divided-difference searches found no matching joint positivity theorem. Reused2225/2230 and the distinct recorded failures; source record drafts/literature/2026-11-21-direct-two-real-zero-source-notes-2234.md. No novelty claim.
SOURCE_EVIDENCE: Csordas1309.0055v2 Theorem4.1/(4.2),p10, https://arxiv.org/pdf/1309.0055v2 ; Tuck2006 pp133-135,(1)-(4), https://doi.org/10.1017/S0004972700047511 ; DLMF1.13(iii),(1.13.8)-(1.13.10), https://dlmf.nist.gov/1.13.iii ; Tao2009 Section3 Exercise30/Remark31 and inversion(11), https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/ ; DLMF3.5(ii),(3.5.6)-(3.5.8), https://dlmf.nist.gov/3.5.ii ; Strang-Herman CalculusVolume2 Section6.3 Theorem6.7, https://openstax.org/books/calculus-volume-2/pages/6-3-taylor-and-maclaurin-series . Reuse2225/2230/C919f; recovery2235 reopened the core ranges below. Dimitrov-Xu1606.05011 Theorems2.5-2.6, https://arxiv.org/pdf/1606.05011 , remain an inspected nonmatch, not an import.
COMPARISON: Standard ODE/Fourier tools permit attempting the joint construction. Tuck's shape hypotheses remain to be verified on any exterior where used; neither positivity nor local decrease of G_x supplies global decrease. Simpson/Taylor cover a smooth finite integral after every derivative/error bound is paid. The required actual-theta two-frequency sign, origin compatibility and complete exterior estimates are additional specialization obligations, not source conclusions.
GAP: Construct the exact smooth even inverse of Xi(z)/((1-z^2/x^2)(1-z^2/y^2)), prove all boundary and tail conditions, and establish the joint pointwise sign without global decrease of G_x. Neither the compact margin nor the exterior criterion is known. No actual y existence, arbitrary iteration or all-degree bridge is established.
REASON: A direct complete signed slab test with an independent theta exterior addresses the nominated joint-removal gap and is distinct from the unpaid global one-factor cosine comparison. This is ordinary finite specialization, not a justified creative uniform-removal mechanism. Separate recovery2235 approves this unchanged scope for one subsequent research invocation; it establishes no joint sign.
SCOPE: Actual L018/L019/L058; accepted C919f/C919m/C919n with their backend contracts if used. Conditional actual roots in disjoint open brackets, possibly multiple, no first-zero/census premise and no y-existence claim. Stronger numerical box x in[14,29/2],y in[21,22],u in[0,1]; fixed exterior u>=1. No heat-time or root-bracket enlargement, unbounded removal index or global G_x-decrease assumption.

## Prospective construction and one fixed sign test

The trial function is to be constructed by applying C919m's decaying
half-line sine operator first with x and then with y to K. This is
a proposed construction, not an asserted quotient identity. Verify
the full tails, differentiation, origin matching at both actual roots,
even smooth extension, entire transform, removable factors and
inversion before identifying it with the joint inverse. Distinct
brackets separate the roots; multiplicity does not authorize omitting
any boundary check. No identity is proved in this assessment.

Seek one uniform rational delta>0 lower bound for the trial integral
on the full compact box in SCOPE, using its complete signed integrand.
One-factor positivity cannot sign the difference or the composition.
Select and prerecord finite quadrature, Taylor and parameter-cell
settings before the test; include the two complete theta tails and
all arithmetic errors. C919f's tail bounds apply only within their
proved domains and after accounting for every new factor/weight.
Retain the CPython/Fraction/libmpdec directed arithmetic and correctly
rounded HALF_EVEN exp contract if that backend is reused. Save full
certificates and failures; samples or an old certificate are not proof.

For the fixed exterior u>=1, attempt to verify an actual-theta
additive-coordinate shape condition from the full series and give
a valid restricted-half-line application of Tuck's criteria. The
candidate condition is strict convexity of K there. Its validity,
boundary conditions and sufficiency for the joint sign are all
unproved tasks. Csordas's square-coordinate shape theorem cannot be
silently substituted. Restricted exterior monotonicity, if proved,
does not supply an assumption of global decrease of G_x.

## Continuation and abandonment

Success requires the exact quotient construction, a paid strictly
positive compact margin and strict analytic exterior positivity.
Retain the first rigorous obstruction or inconclusive error budget.
A certified negative value at a nonroot refutes only the stronger
box test; refuting the conditional root target requires actual-root
compatibility. No automatic split movement, bracket sharpening or
parameter sweep follows a failure. A failure of this mechanism is
not a disproof of RH. No mathematical test is run during approval.

Plausible use is a qualified two-removal positivity input beyond
C919m, avoiding unpaid global residual decrease. Arbitrary iteration,
uniform estimates as roots/removal count grow, and the actual-Xi
all-degree L030-L032/C032a bridge remain independent gaps even if
this succeeds. C919n is context, not an essential premise proving
the new sign. No cross-notebook theorem is used. Full matching
Mathlib coverage is unchecked, not asserted absent. A later result
should be labeled as a specialization/reproduction unless stronger
evidence supports a different classification.


## Separate source-link recovery and approval2235

LITERATURE_REASON: The supervisor reported missing direct source URLs in
this ready assessment. This turn repairs that defect and separately
approves the unchanged nomination2234; no renewed discovery search or
new mathematical claim is needed.

Reopened the direct primary pages on 2026-11-21: Csordas v2 printed p10,
Theorem4.1/(4.2); Tuck printed pp133-135, introduction and sine/convex-cosine
proof cases; DLMF1.13(iii),(1.13.8)-(1.13.10); Tao Section3 Exercise30
and Remark31; DLMF3.5(ii),(3.5.6)-(3.5.8). Direct publisher Tuck PDF:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D232B9DEB4819E4D2FF17E8162B8B066/S0004972700047511a.pdf/on_positivity_of_fourier_transforms.pdf
The parsed display(4) is incomplete; retain the previously inspected
complete parallel argument in Csordas Remark3.11 from recovery2226.
Tao inversion(11), OpenStax Taylor remainder, local arithmetic contracts
and the Dimitrov-Xu theorem comparison are reused from the recorded
assessments, not newly recertified here. The Dimitrov-Xu PDF was reopened
for identity/version confirmation only this turn.

The relevant restrictions remain: Tuck needs convergent transforms,
decay and the stated strict amplitude shape; DLMF's ODE formula leaves
homogeneous freedom and does not choose decaying or even boundary data.
Tao requires integrable function/derivative and absolute continuity.
Composite Simpson requires C4 regularity, even subdivision count and
a proved fourth-derivative error bound. None supplies the new joint
kernel sign. Source normalization must still be matched to L018/L019/L058.
No original Wintner/Spira proof, optional Spigler result or full matching
Mathlib theorem is newly claimed as inspected.

DECISION remains EXPLORE. The exact TARGET and SCOPE are unchanged and
approved for one subsequent REPRODUCTION or POTENTIALLY_NEW attempt
under the shared classification rules. This is a process repair,
outcome STALLED: no new mathematical advance or negative evidence,
no calculation, no lemma/script write, and no counter reset claimed.
All continuation and abandonment conditions above remain binding.
