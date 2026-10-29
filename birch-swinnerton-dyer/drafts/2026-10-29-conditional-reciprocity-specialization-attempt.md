# Conditional reciprocity specialization — step 542

2026-10-29. Completed under the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-28-retained-plus-conditional-reciprocity-specialization.md`.
One proof attempt; no discovery or new source gate is being combined with it.

Main gap: rank/order equality for arbitrary elliptic curves over Q.
Target: conditional finite-at-p membership of L123's actual complete,
projected and descended outer-plus coefficient. Its possible downstream
use is a Selmer input, still short of rational Kummer membership,
nonvanishing, strictness and a rank comparison.

Continue only if descent to Q, one global integral scaling and every
local condition match the assessed duality theorem. Stop the application
at a failed transfer. The nonzero rational Kummer localization is an
assumption, never an inference from analytic order two.

Inputs read: L123 including its step-515 audit, the step-540 source note,
the relevant Rubin I.2.2, I.3, I.4, I.5, I.6.4 and I.7.3 passages and
elliptic Section 5. Duplicate/failure comparison is reused from step 540;
ATTEMPTS/058 and /061--063 were checked and remain unchanged.

Provisional proof path (not yet accepted): let b be the global K-class
before localization in L123 (5). Its construction is (1+c) times the
unsymmetrized descended coefficient, so rational inflation--restriction
gives a unique z in H^1(Q,V). Check that res at p of loc_p(z) is R.
Choose a common integral scaling of z and the assumed rational Kummer
class. Check the away-p full integral Kummer identification against the
published paragraph, then use Rubin I.7.3(ii), Sigma={p}, Sigma_0=empty,
at every p-power level. Compatibility of cup products should give
orthogonality at the rational level. The finite local line is
one-dimensional and self-orthogonal, so the nonzero rational Kummer
localization would force loc_p(z) into that line. No projected raw
moment bound or finite-Sha input is used.

Completion: the checks named above pass in the written specialization;
the full proof and qualifications are canonical in
[L130](../lemmas/L130-conditional-retained-plus-finite-local-membership.md).
The provisional sketch is retained as pre-completion reasoning, not a
second proof. The separate critical audit has not been performed.

RESEARCH / proof_attempt / development / REPRODUCTION / ADVANCE:
local progress is the conditional applicability result for the actual
coefficient, with no progress beyond the checked standard sources and
no new BSD case. No point or nonzero coefficient is constructed. One
common global scaling is justified by the cited rationalization; no
numeric bound for it is asserted or needed. All bad primes use the
induced finite local condition, not an unramified substitute.

The published away-p paragraph was retrieved to check an already
assessed convention; this was not an additional literature-review
task. No mathematical script or numerical experiment was needed.
Only the direct local input L123 is added to the canonical DAG row.
Prior unfinished notebook changes and all recorded failures remain.

Supplied settings: gpt-6-astra, xhigh, development. Actual backend
identity and effort are not independently observable here.
