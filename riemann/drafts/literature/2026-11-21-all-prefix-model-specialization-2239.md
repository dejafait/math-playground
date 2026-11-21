# All-prefix model: source-covered specialization nomination2239

TARGET: Test whether every finite quotient F_n of F(z)=exp(-z^2)(2+cos(z))sin(z)/(3z) has a smooth strictly positive probability inverse with super-exponential derivative decay and uniformly bounded second moments while retaining a fixed nonreal zero, and establish the exact growth-order limitation.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed review2239 of startup target2238; exact local comparisons and external queries are recorded in drafts/literature/2026-11-21-all-prefix-source-notes-2239.md. No inspected matching all-prefix theorem and no novelty claim.
SOURCE_EVIDENCE: Direct primary sources: https://dlmf.nist.gov/5.12.E5 (cosine-power integral, Re(a)>0), https://dlmf.nist.gov/5.12.E1 (beta-gamma relation), https://dlmf.nist.gov/5.5 (5.5.1/5.5.3), https://dlmf.nist.gov/5.2.i (reciprocal gamma), https://dlmf.nist.gov/4.22.E1 (sine product), https://dlmf.nist.gov/4.14 (complex trigonometric definitions); https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/ (Exercises14/16/29/41 and inversion(11)); https://arxiv.org/pdf/1309.0055v2 (Theorem3.7 p8, Xi order p10). Base-factor overlap URL and inspection qualifications remain in source notes2239. Direct-link recovery2240 rechecked essential identity/transform access; no new theorem claimed.
COMPARISON: This is reproduction/specialization of standard transforms and elementary analytic operations. The base factor is already known; the combined every-prefix assertion is not imported from it. Existing finite actual-Xi results and finite-block countermodels do not establish the required quantifier, and correlation-kernel criteria do not describe these inverses.
GAP: Prove the normalized all-n quotient identity, removability, strict probability inverses with all derivative tails, a uniform second-moment bound, exhaustive real-zero list and multiplicities, a retained nonreal zero, and exact order. No actual-Xi iteration, order-one sufficiency or all-degree mixed sign is covered.
REASON: Exact ordinary source coverage is ready; only the stated applicability and assembly obligations warrant a mathematical attempt. Do not reprove the cosine-power integral, gamma identities, sine product or Gaussian transform.
LITERATURE_REASON: Supervisor recovery requires direct source URLs in the ready assessment itself; this bounded repair reuses review2239 without expanding the target or repeating discovery.
SCOPE: The single proposed F, P_n(z)=product_(k=1)^n(1-z^2/(k*pi)^2), P_0=1, F_n=F/P_n, all integers n>=0 with removable extension. No changed parameters, additional hypothesis on residual zeros or numerical surrogate. Newly written ready continuation: separate approval next turn; no mathematics executed2239.

Use angular transforms integral_R f(u)exp(izu)du. For the cosine-power
source the proposed parameter identification is a=2n+1, b=2z/pi and
t=pi*u/2. Prove normalization and the identification with sin(z)/(z P_n)
using the cited gamma formulas, initially away from their poles and
then with an explicitly justified entire extension. In particular
include n=0 and all removed real roots. No particular inverse density
or all-n identity is asserted in this nomination.

The source's compact cosine-power inputs and Gaussian convolution are
a concrete test mechanism. Verify the mass and sign before using them
as probability laws. Justify all derivative interchanges and Gaussian
tail estimates; polynomial Schwartz decay is insufficient for the
requested every-fixed-exponential property. Obtain one explicit bound
independent of n, rather than finite-n moments or numerical samples.
No uniformity of unrequested derivative constants may be assumed.

Determine the complete positive real-zero inventory and multiplicities
of F, not merely a list of visible factors. Exhibit one exact nonreal
zero that survives every P_n removal. Prove the exact growth order by
both an upper estimate and a matching lower-growth test. Compare the
result with Xi's known order one, using Csordas's source normalization
and the existing L019 normalization if needed. A Gaussian-based result
must retain its order-two limitation.

L018/L019/L058 and accepted C919m/C919o are essential scope comparisons,
not premises supplying model signs. L262 and the nonreal-deflation,
finite-block1117 and finite-divisor667 stops retain their original
qualifications. C919f's backend contracts are not imported into an
analytic model proof. No cross-notebook theorem is used.

Continue only if every required obligation holds for this fixed model
and all n. Stop at the first genuine failed obligation and preserve
the defect; do not alter the model to rescue this test. An unsuccessful
estimate alone leaves the model unresolved. Success could limit a
generic positivity-removal bridge in the stated growth class; it would
not prove or disprove RH or settle an order-one bridge. A complete
model proof would need its later independent critical review. Full
matching Mathlib coverage and supporting theorem names are unchecked.

## Direct-source gate repair2240

The 21 November 2026 recovery review placed direct source URLs in
SOURCE_EVIDENCE rather than relying solely on the linked source-notes
file. Reopened DLMF5.12.5 with its Re(a)>0 condition and the surrounding
beta conventions; gamma recurrence/reflection, reciprocal-gamma and
sine-product pages; Tao's Gaussian and measure-convolution statements;
and Csordas's theorem statement. Prior detailed inspection and local
duplicate/failure comparisons in source notes2239 remain reused.
No changed hypotheses, new literature discovery, model calculation or
proof is reported. SPECIALIZE still authorizes only the previously
listed assembly obligations. The exact TARGET and proposed parameters
are unchanged. This is a process repair, not mathematical progress.
