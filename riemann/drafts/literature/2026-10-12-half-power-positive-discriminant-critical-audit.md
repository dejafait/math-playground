# L403 critical-audit source coverage

TARGET: Critically audit L403's unconditional shifted twelfth-moment localization, ordinary jet transfer and H^(1/2)(log H)^(-5/2) positive-discriminant measure bound, including complete tails and all-real-H quantifiers.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 91's exact-statement and stronger-result searches; narrowly searched October 12 drafts/histories/ATTEMPTS for L403, Gaussian and twelfth-moment duplicates, and read the older higher-moment-upper-bounds failure. Retrieved only the primary passages needed to compare the newly written Gaussian audit scope.
SOURCE_EVIDENCE: Reinspected Ivic arXiv:1406.0604v1 Lemma 10 and its justification, p. 7; AOR arXiv:1901.04061v4 Proposition 3.3 and Corollary 3.4, pp. 22-23; Curran-Heycock arXiv:2403.00902v1 Section 4, p. 8, through its RH qualification. Read L403 and the relevant audited L389/L390/L391/L401 input ranges.
COMPARISON: Existing unconditional scalar and fixed-order analytical coverage suffices for this independent audit. The Gaussian calls for bounded-strip Proposition 3.3, not the stronger half-plane Corollary 3.4 or the rectangle-window lemma; the sharp RH-dependent k=6 conclusion remains excluded. No inspected source directly supplies the physical measure assertion.
GAP: Independently verify L403's family-specific localization, uniform small-shift bounds, normalized ordinary jets and concentration accounting; source coverage is approved, but the mathematical audit is not performed here.
REASON: The separate review closes the coverage question for the newly written audit target without endorsing L403's proof or deriving new mathematics; the next turn should perform the unchanged critical audit.
LITERATURE_REASON: Step 92 introduced the explicit pole-canceled Gaussian window; its exact strip hypotheses and source/dependency scope required the separately mandated comparison before a proof audit.
SCOPE: Audit L403 (1)-(3) for fixed ordinary jet orders 0,1,2, the complete response, existential constants and every sufficiently large real H; excludes new moment asymptotics, growing orders/heads, positive density and any RH conclusion.

The source review reuses the existing
`2026-10-12-positive-discriminant-higher-moment-concentration.md`
assessment, including its searches and retrieval qualifications. The exact mathematical
inputs are L389's zero-safe ordinary Hardy identification; L390's full
physical pointwise bound (including curvature and complete response);
L391 (3) and its Omega/Omega' bounds; and audited L401 (1), (3)
for W=Re(R zeta(5/2+it))f. L402 is a comparison benchmark, not a
mathematical premise of L403. The external inputs are the unconditional
finite-log scalar twelfth moment, AOR's integral strip-convexity theorem,
standard Cauchy/Holder, the functional equation, conjugation and Stirling.

The separate research audit must check the explicit window F_H(s)=(s-1)zeta(s)
exp((s-3iH/2)^2/H^2)/H, its pole removal, closed-strip uniform decay,
boundary integrability and uniform-H bounds, both infinite tails and
the lower bound of its multiplier on [H-1,2H+1]. Check negative
horizontal shifts by the bounded functional-equation multiplier,
vertical endpoint shifts by nonnegative enlargement, and the exact
factorial and normalized derivatives in the Cauchy transfer. Retain
Omega' without dividing by a Hardy value. Finally verify that the
complete |Delta W^2|^3 bound and positive weighted mean give the
exponents H^(1/2) and (log H)^(-5/2) for every large real H.

## Primary-source comparison and qualifications

The inspected editions are unchanged from step 91. This turn reopened
their selected load-bearing passages, rather than rerunning discovery.

- D. R. Heath-Brown, *The twelfth power moment of the Riemann
  zeta-function*, Q. J. Math. Oxford (2) 29 (1978), 443-462,
  Theorem 1, p. 444, DOI [10.1093/qmath/29.4.443](https://doi.org/10.1093/qmath/29.4.443).
  Its original scan's unreadable displayed formula remains a recorded
  limitation. The exact unconditional scalar estimate
  `integral_0^T |zeta(1/2+it)|^12 dt << T^2(log T)^17`
  was read again in A. Ivic, *On some mean value results for the
  zeta-function and a divisor problem*,
  [arXiv:1406.0604v1, Lemma 10 and its justification, p. 7](https://arxiv.org/pdf/1406.0604v1#page=7),
  which explicitly attributes it to Heath-Brown. This readable primary
  corroboration resolves essential statement coverage; visual inspection
  of the original scan is not claimed. No derivative theorem is imported.
- L.-P. Arguin, F. Ouimet and M. Radziwill, *Moments of the Riemann
  zeta function on short intervals of the critical line*, Ann. Probab.
  49 (2021), 3106-3141,
  [arXiv:1901.04061v4, Proposition 3.3, p. 22](https://arxiv.org/pdf/1901.04061v4#page=22):
  for p>0, closed-strip analyticity and uniform decay at imaginary
  infinity give integral log-convexity between the boundary lines.
  L403 proposes p=12 and strip [1/2,2], with finite full-line integrals.
  This is the matching theorem scope. Corollary 3.4 adds half-plane
  analyticity, uniform decay there and integral decay as sigma tends
  to infinity. L403's Gaussian is not offered as satisfying that
  stronger horizontal requirement. Neither the corollary nor Lemma 3.5
  is an essential input here. The latter's construction/proof remains
  covered by step 91; no new window theorem is needed for this audit.
- M. J. Curran and A. Heycock, *Sharp bounds for joint moments of
  the Riemann zeta function*,
  [arXiv:2403.00902v1, Section 4, p. 8](https://arxiv.org/pdf/2403.00902v1#page=8):
  the fixed-n Cauchy/Hölder calculation reduces derivative moments to
  uniform shifted scalar moments with the expected logarithmic derivative
  cost. Its subsequent sharp estimate is unconditional only for k<=2;
  for k>2 it assumes RH. At k=6 the audit may use the transfer calculation
  and Heath-Brown's weaker input only. The printed reciprocal-factorial
  prefactor must be replaced by the standard n! Cauchy prefactor, as
  already recorded and written in L403. No cited FHK near-line lemma
  is needed: L403 writes its own functional-equation applicability check.

These named theorems need citation and specialization checks, not reproof.
The elementary pole-removal/growth check, Gaussian shell bounds, negative
horizontal-shift transfer and physical concentration implication are
local applicability arguments absent from the cited statements. This
turn assigns those obligations to the audit; it does not establish them.

## Local inputs, duplicate/failure checks and audit decision

Read L389's zero-safe Hardy identification; L390's complete response
derivatives, exact physical formula (5) and its audit; L391 (3) and the
audited separate Omega/Omega' bounds; and L401's hypotheses, (1), (3),
and audited endpoint/full-tail quantifiers. Their scopes match the
recorded inputs, with no truncation or division by a Hardy value.
L403's full argument was read for coverage mapping, not critically
validated. Its DAG row names exactly these four inputs; no dependency
or argument change is proposed in this literature step.

The October 12 narrow search found the construction and pending audit,
not an already completed independent L403 audit. The older
`ATTEMPTS/2026-09-13-higher-moment-upper-bounds-alone.md` concerns L154's
different mass-concentration inference; it warns against positive-density
claims from upper moments and does not ban this bounded sublinear target.
The L394/L399/L400 weight failures and audited L402 benchmark are already
compared in the supplied overview and reused assessment. None is reopened.
No novelty inference follows from this duplicate check.

Continue with the exact saved audit. Its pass condition is a complete
check of (1)-(3) with H-independent constants, complete positive and
negative tails, every radius-1/log H shift, zero-safe ordinary jets and
the claimed half-power/logarithmic threshold. A missing domination,
positive height-power loss or hidden RH/phase assumption fails that
implementation; preserve the evidence and identify the precise repair
or a materially different test. Mathematical correctness is still pending.

No RH, sharp k=6 conjecture, independent carrier, response truncation,
weight lower bound or actual common-zero assumption may enter. Global
mixed positivity, total L367 signed margin and actual common-zero upper
counts remain unresolved even if the audit passes. Full matching Mathlib
coverage has not been checked. This file approves source coverage for
the separate audit, not L403's correctness or a new mathematical conclusion.
