# Centered theta Appell obstruction — approved independent-audit coverage

TARGET: Review source coverage for an independent audit of L825's centered degree2/3 factor inversion and certified nonzero Appell defect.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step630 reused steps620/627/628 exact-statement searches and inspected the scoped common-symbol stop and step629 history; reaccessed the two primary definitions needed to compare the audit scope. No changed mathematical target or novelty search.
SOURCE_EVIDENCE: Marcus–Spielman–Srivastava https://arxiv.org/pdf/1504.00350v2 Definition1.1/(1)–(2), printed p.2, and Theorem1.3 p.3; Campbell https://arxiv.org/html/2412.20488v3 (1.1), Section1.4/(1.23)–(1.26); reused Arizmendi–Perales https://arxiv.org/pdf/1611.06598v2 Propositions3.4/3.6 and full proofs pp.7–8 from steps620/628; L791 step478 and L778 step433 inherited analytic/software coverage.
COMPARISON: The algebraic operation and formal Appell condition cover this finite audit without real-root, entire-symbol or LP assumptions; generic inversion is context, not a substitute for checking every specialized coefficient equation and actual enclosure. Reciprocal orientation and fixed-degree symbol freedom do not supply common-degree compatibility.
GAP: Source coverage is adequate; the separate mathematical audit of L825 and its full rational evidence remains unperformed. Uniform signs, alternative realizations and mixed/shifted transfer remain unresolved.
REASON: Step630 completes the saved source-approval target and approves only the covered audit below; no new theorem, arithmetic verification or audit pass is claimed. Step629's completed NEGATIVE evidence is preserved.
LITERATURE_REASON: The saved REVIEW_REQUIRED continuation asks for separate applicability approval of the new L825 audit; this review reuses ready results and checks only the essential operation/orientation and inherited-error scope.
SCOPE: Source coverage for the exact L825 statement, not new factors, degree sweeps, alternative normalizations or a uniform positivity mechanism.
COVERED_TARGET: Critically audit L825's centered degree2/3 inversion, every lowering-defect coefficient and full rational enclosure under its inherited L791/L778 contracts.

The separate source approval is complete in step630, 5 November 2026.
Reuse this assessment for its exact covered audit target. The prior ready
assessment and canonical L825/L791/L778 retain their mathematical detail;
there is no essential source-access blocker.

The approved audit must check monic centering before inversion, every
degree2/3 convolution coefficient and uniqueness, the complete polynomial
lowering defect, source orientation, exact rational interval arithmetic,
coefficient-error retention and hashes. It must distinguish consistency
checks and saved prior audits from an independent backend verification.
The decisive bound is a defect interval disjoint from zero; a defect in
normalization, an unenclosed input or a zero-straddling recomputation would
require correcting or qualifying the restricted stop. Nothing here proves
an audit pass or licenses a different mathematical target.

Essential continuation inputs: L019/L021/L795 actual law, L791 gamma through
j=3 and L778/step433/step478 contracts; L825's complete new certificate is
`scripts/central-jacobi/centered-appell-629.json`. L823/L824 are not premises.
Uniform signs, other realizations, mixed/shifted transfer and RH remain
open. Mathlib matching coverage is unchecked; no cross-notebook input.

## Completed source comparison — step630

The main gap remains actual-Xi all-degree mixed positivity. This audit's
intermediate target is the reliability of the finite common-symbol
obstruction. Its downstream use is deciding whether the stated realization
stays parked; it cannot supply the missing positivity. Continue the stop
only if the full algebra and strict enclosure survive; repair or qualify
it if normalization, input enclosure or the strict bound fails.

### Exact known inputs and scope

Marcus, Spielman and Srivastava, *Finite free convolutions of polynomials*,
arXiv:1504.00350v2 (3 July 2019 arXiv stamp; title page 4 July),
[Definition1.1, equations(1)–(2), printed p.2](https://arxiv.org/pdf/1504.00350v2),
allows complex polynomials of degree at most a fixed d. The factorial
coefficient convention and differential composition are algebraic; they
require neither a probability measure nor real roots. Definition1.1 also
warns that changing d changes the operation. Theorem1.3, printed p.3,
requires both degree-d inputs real-rooted for forward root preservation.
That theorem is not an input to the proposed obstruction audit. These
primary passages were reaccessed in this turn; no preservation proof or
matrix-averaging proof is needed for the algebraic definition used here.

Campbell, *Free infinite divisibility, fractional convolution powers, and
Appell polynomials*, arXiv:2412.20488v3, 18 December 2025,
[(1.1) and Section1.4/(1.23)–(1.26)](https://arxiv.org/html/2412.20488v3),
separates the Jensen coefficient orientation from its reversed Appell
orientation. It explicitly allows a formal power series in (1.26).
The lowering condition therefore applies to a common formal
constant-coefficient symbol; an entire LP symbol is unnecessary for this
necessary-condition audit. Its all-degree real-root conclusion has
additional hypotheses and is not imported. These are source statements,
not a new derivation of L825's compatibility or its failure. The audit
must not silently identify monic centering with reversal or replace one
symbol by degree-dependent truncations with unrelated coefficients.

Reuse Arizmendi and Perales, *Cumulants for finite free convolution*,
arXiv:1611.06598v2, 7 March 2017,
[Propositions3.4/3.6 and proofs, printed pp.7–8](https://arxiv.org/pdf/1611.06598v2),
as inspected in steps620/628. Their formal partition inversion and monic
additivity do not assume positive roots. No new external reading of those
proofs was needed. The proposed audit uses the explicit degree2/3
coefficient equations already in L825 rather than general fractional-power
or infinite-divisibility theorems. Rechecking the finite equations is
necessary to validate this specialization's normalization and uniqueness;
it is not a reproof of general inversion. Reuse the failures and stronger
theorem comparisons in the step620/627 assessments; the scoped common-symbol
stop and step629 history show that no earlier independent L825 audit is
being repeated. This bounded screen makes no exhaustive novelty claim.

### Inherited evidence and audit boundary

Read L791's actual-coefficient construction and step478 audit passage,
and L778's evaluator hypotheses, complex-disk error and relevant step433
normalization/interval passage. Reuse the source coverage in
[the fixed-central-model audit assessment](2026-11-05-fixed-central-model-audit.md).
The standard Cauchy coefficient estimate requires the analytic difference
on the full complex disk; a real-axis error would not suffice. L791
retains both polynomial-coefficient widths and the additional analytic
coefficient error. The future audit must check those premises and
normalizations through j=3, without importing the model's parameter or
root assertions. Johansson's validated-analysis method and the Decimal/
mpdecimal contracts are already assessed there and in L778; no changed
software contract has been proposed. They do not independently attest
the installed binary or validate the new L825 implementation.

The audit must inspect the complete load-bearing endpoints in
`scripts/central-jacobi/fixed-model-certificate-476.json`, the relevant
full checks/failures in `scripts/central-jacobi/audit-478/audit-report.json`,
and L825's entire relevant certificate fields. It must review
`scripts/central-jacobi/centered_appell_629.py` and the imported rational
interval implementation, preserve originals, and distinguish an independent
coefficient/enclosure check from rerunning the same program. Hash agreement
and alternate-form overlap are consistency evidence, not independent
verification of the transcendental backend. Exact rational conversion,
outward rounding, denominator exclusions and coefficient-error containment
remain mathematical audit obligations, not conclusions of this review.

The decisive reported claim is the full defect interval strictly inside
(9.582501,9.582502), versus the required value zero. This number is quoted
from unaudited L825, not independently verified here. The audit must check
every polynomial coefficient, including the cubic constant equation,
before using that interval. No new quadrature, adjustable normalization,
degree sweep, factor-sign claim or all-degree inference is covered.
Independent uniform signs and mixed/shifted transfer remain open.

This is STALLED procedural source approval: the known-method comparison
licenses a later audit but adds no mathematical evidence beyond steps628/629.
No JSON evidence was verified, calculation replayed, new mathematics
derived, or lemma/script/PROOF/DAG modified. Mathlib matching coverage is
unchecked. The exact covered audit is ready for the supervisor's next-turn
routing; this review does not request another source search.
