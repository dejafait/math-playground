# Suzuki kernel-to-form gate — bounded audit coverage1121

TARGET: Audit Suzuki's two kernel-to-form domination steps in Theorem 4.2 for arbitrary complex L2 tests, with explicit uniform constants and Fourier normalization.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Discovery1121 searched the exact Suzuki4.2/kernel/pointwise/Plancherel and erratum terms, checked the prior screw remainder screen's explicit warning, and found no completed local audit of these two form bounds. This is bounded coverage, not an originality or absence claim.
SOURCE_EVIDENCE: Suzuki, Aspects of the screw function corresponding to the Riemann zeta-function, JLMS108(2023),1448-1487, DOI10.1112/jlms.12785, arXiv2206.03682v4 PDF internal31May2023, Theorem4.2/(4.2)-(4.11), printed pp12-15; Theorem4.3 proof pp15-16. Tao, 245C Notes2,6April2009, Section3 Theorem43/Exercise44, with the Parseval argument immediately preceding them. Primary passages and relevant proof cases read in1121.
COMPARISON: The source asserts the required form bounds but presents intervening pointwise kernel comparisons. Independent form-level justification and explicit constants are the precise audit difference; the standard Plancherel theorem is imported, not reproved. No all-window positivity or new RH criterion is sought.
GAP: Establish or refute the two stated form inequalities for arbitrary complex L2 tests without assuming pointwise kernel order implies quadratic-form order; justify the transform representation, integration, shifts and normalization. No constant or audit verdict is established here.
REASON: A suspect proof passage and quantitative applicability justify this bounded reproof of known source claims. This new continuation requires separate supervisor approval before research; it does not reopen C030c or the stopped scalar-tail source.
SCOPE: Only the shifted-line L2 comparison and small-window low-frequency loss in Theorem4.2; no full theorem audit, arbitrary-window sign, source numerical certificate, zero subtraction or change of test space. Proposed completion classification REPRODUCTION.

## Exact audit obligations

For a>0 and arbitrary complex phi in L2(-a,a), use the source's
Fourier convention hat(phi)(z)=integral_(-a)^a phi(t) exp(izt)dt and
Phi(phi,z)=(hat(phi)(z)-hat(phi)(0))/z, with its removable value at zero.
Define the target quantities

    E_y(phi) = integral_R |Phi(phi,r+iy)|^2 dr,
    L_T(phi) = integral_(-T)^T |Phi(phi,r)|^2 dr.

Fix a1>0, c>1 and T>0. The audit must justify finite explicit
C2(a1,c), C3(a1,T) and a2(a1,T)>0 such that

    E_(+c)(phi), E_(-c)(phi) <= C2(a1,c) E_0(phi)   (0<a<=a1),
    L_T(phi) <= a C3(a1,T) E_0(phi)               (0<a<=min(a1,a2)).

These are proposed quantitative versions of the source's two form
claims, not inequalities proved in this assessment. Include both
frequency signs used in the source. Require finiteness, all complex
tests, and constants independent of a and phi in the displayed ranges.
Do not impose mean zero, positivity, parity or unmentioned regularity.

## Sources, specialization and limit of the test

Controlling source: [Suzuki v4 PDF](https://arxiv.org/pdf/2206.03682v4),
printed pp14-15. The passage after (4.9) treats shifted integrals;
the passage after (4.11) treats bounded frequencies. The whole surrounding
proof and its subsequent reuse were read. The earlier
`2026-11-01-screw-function-signed-remainder-screen.md` flagged the
logical issue without auditing it. This nomination does not assert
that the inequalities, Theorem4.2 or Theorem4.3 are false. Other
steps, constants and the complete positivity conclusion remain outside
this audit, even if these two inequalities pass.

Import the standard Euclidean Plancherel theorem from
[Tao, 245C Notes2](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/),
Section3 Theorem43 and Exercise44. The source uses a negative 2pi
exponent; explicitly convert to the convention above. Its unitary
extension is on L2 and agrees with the integral transform on L1 intersect
L2. A suitable primitive with compact support and any exponential
weight must first be justified in that common domain. Then a real-axis
form argument may replace the disputed inference. No primitive formula,
constant or bound is supplied as an established input here.

The single coherent test is whether this analytic gate can be justified
with those exact hypotheses. Continue if both bounds have full form
proofs and explicit constants, or record a rigorous violating test for
one bound. Stop and preserve any unresolved interchange, endpoint or
norm issue if neither verdict is obtained; a grid or failure to find a
constant is inconclusive. One bounded audit precedes reassessment.

Plausible use: reliable analytic control for later arithmetic/complement
work in the Weil/screw representation. L030/L032/C032a give main-gap
context; C030c and the finite-block stop are contrasts, not mathematical
premises. Low-block signs/coupling, all-support positivity, conversion to
L030 and common-graph realization remain independent. No new central
creative sign mechanism is claimed. No cross-notebook input. Full
matching Mathlib coverage is not checked; named Fourier support would
not by itself certify these specialized inequalities.
