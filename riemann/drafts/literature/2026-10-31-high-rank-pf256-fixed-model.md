# Fixed high-rank reciprocal-density diagnostic

TARGET: Test the fixed polynomial P_*(z)=(1-z^2)^270(1-z^2/a^2)(1-z^2/conjugate(a)^2), a=2^20+i/4, for a strict-PF256 reciprocal density and a negative first Laguerre sign at t=2^20, using Sra v2 Lemma C.6.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: The completed parent comparison searched strict finite-order rational Laplace transforms, reciprocal-polynomial Laguerre signs, complex-pole convolution and finite-order perturbation statements; additional searches for Polya frequency with 270/polynomial and repeated/Laplace/strict found no inspected theorem supplying the two requested properties of this fixed model. No novelty is inferred.
SOURCE_EVIDENCE: https://suvrit.github.io/papers/riem-xi/riem-xi-v2.pdf (29 October 2026), Appendix C.1 Lemma C.1/proof and C.4 Lemma C.6/proof, printed pp.18,21, directly reopened 2026-10-31; https://arxiv.org/pdf/2008.05121v2 Theorems D/E p.7 and D proof p.21; https://arxiv.org/pdf/2007.12889v1 definition/Theorem 1 pp.1-2. Comparison scopes are reused from the completed parent assessment; both arXiv URLs also reopened successfully.
COMPARISON: Sra C.6 covers the implication from global signed differential determinants through 256 and C^510 to strict ordered minors. It proves none of those determinants for this model. Khare's compact-support transform-zero theorem and the all-order Schoenberg characterization do not settle this model. L560 is a PF2 contrast only; its proof does not certify the new high-rank convolution.
GAP: Existence/positivity/normalization/regularity and the bilateral identity for the candidate density, every required global differential determinant including the tails, and the polynomial's negative first sign at the fixed real point remain unproved. No calculation of this model has been performed.
REASON: Test one stronger finite-order mechanism with fixed data and a primary sufficient criterion; do not replay L560 or tune its parameters. A successful global certificate would obstruct the generic strict-PF256 implication, while a failure would concern this model or criterion only. Separate literature approval completed in the 2026-10-31 direct-URL recovery; the next turn defaults to the mathematical attempt.
SCOPE: Exactly P_* and the proposed reciprocal Fourier density below; one proof attempt with no parameter search, Xi application, source-certificate audit or assertion of novelty. Ready coverage after the separate 2026-10-31 direct-URL literature recovery; no model property is certified.

## Fixed object and requested certificate

Put A=2^20 and a=A+i/4; define P_* exactly as in TARGET. Define the
candidate function by the inverse Fourier integral with the convention

    p_*(x)=(1/(2*pi)) integral_R exp(i*u*x)/P_*(i*u) du.

This specifies a candidate, not a proved density. The later attempt
must justify the integral and its manipulations, p_* real/even and
strictly positive, total mass 1, at least C^510 regularity, absolute
bilateral convergence on |Re z|<1, and transform 1/P_*(z) there.
An alternative exact residue/convolution representation must be proved
equal to this candidate before use. Do not assume positivity of a
convolution factor coming from the nonreal pair.

The proposed sufficient strictness test is

    H_k(x)=(-1)^(k*(k-1)/2)
           det[p_*^(i+j)(x)]_(i,j=0)^(k-1) > 0
                  (x in R, 1<=k<=256).

Only after these hypotheses are established may Sra v2 Lemma C.6
be cited to obtain strict ordered minors through 256. That lemma and
its complete Wronskian proof were inspected in the parent source review;
no need to reproduce the theorem. It requires global signs, rather
than sampled minors, pointwise numerics or a tail-only statement.
Do not invoke C.7's Xi-specific certificate for this function.

The second threshold is exactly

    P_*'(A)^2-P_*(A)*P_*''(A) < 0.

No value or sign is asserted. Exact rational sign comparison is
appropriate; enormous expanded coefficients need not be printed.
Both thresholds are necessary for this proposed obstruction certificate.
Complex roots alone do not prove failure of the first Laguerre sign,
and a negative sign alone does not prove PF256.

The 270-fold real-pole factor is a fixed high-rank convolution candidate,
inspired by the finite many-factor interface in Sra C.4. Establishing
global determinant stability under this particular nonreal factor is
new work relative to the checked sources. It is not justified by
convolution closure unless the factor's required minor signs have
themselves been established. The constants are frozen; changing them
would require a newly scoped target and review.

## Relevance, bounds and stopping test

Main gap: actual-Xi all-degree positivity; even the first complete
signed residual at unbounded heights is uncontrolled. This diagnostic
tests a generic finite-order transfer before an Xi-specific effort.
It uses no Xi realization and cannot prove or disprove RH.

Inputs: Sra v2 Lemmas C.1/C.6 as cited in
[the parent assessment](2026-10-31-strict-pf256-reciprocal-polynomial-transfer.md).
Audited L560 is a contrast, not a premise implying strict PF256.
No other notebook or unevaluated probability certificate is used.

Bound the next attempt to this one object and determinant mechanism.
Seek an exact global certificate; otherwise preserve any exact reduction
or informative failed determinant with its domain. One rigorously
nonpositive ordered minor rules out the candidate's strict hypothesis.
A nonpositive differential determinant merely defeats this sufficient
criterion unless a valid necessity argument is separately supplied:
a negative confluent limit can be informative, while a zero need not
exclude strict distinct-point minors. A resource limit or inconclusive
interval is unresolved evidence, not a sign. No parameter tuning,
numerical preview as proof, or automatic repeat of an unchanged
incomplete attempt. Two unproductive mathematical turns require
reassessment under the shared rule.

If both full thresholds are met, the result is a model obstruction
requiring a later independent audit. If either model property fails,
do not infer that the universal implication is true. Actual-Xi
transfer, higher signs and a complete signed-remainder bound remain
independent in all outcomes.

Mathlib: full matching finite-order transform/differential criterion
coverage was not checked; availability is unknown.

## Separate source-link recovery — 31 October 2026

LITERATURE_REASON: The supervisor reported missing direct URLs in this
ready assessment; this bounded recovery supplies them and reopens the
load-bearing criterion, without repeating the broader discovery search.

The [primary Sra v2 PDF](https://suvrit.github.io/papers/riem-xi/riem-xi-v2.pdf#page=21)
was accessible. Lemma C.6 and its full proof on printed p.21, and
[C.1 and its full proof](https://suvrit.github.io/papers/riem-xi/riem-xi-v2.pdf#page=18)
on p.18 were rechecked. C.1 uses real functions on an interval,
positive initial Wronskians and increasing distinct evaluation points;
its proof reduces by the first function and integrates consecutive row
differences. C.6 applies that transfer twice. The existing global
smoothness and strictness requirements above match its hypotheses.
No density, transform or determinant claim for P_* follows automatically.
C.7 concerns the source's own Xi convolution and remains excluded.

The [Khare v2 PDF](https://arxiv.org/pdf/2008.05121v2) and
[Grochenig v1 PDF](https://arxiv.org/pdf/2007.12889v1) also resolved;
their theorem comparisons are reused from the parent assessment, not
newly established here. The original Schoenberg DOI sources remain
unread and are not needed for invoking C.6. No new source blocker or
change of target was found. This is a process repair, not a mathematical
advance or renewed search establishing novelty. All previous failures
and the fixed model's unproved hypotheses remain in force.
