# Affine Meixner-Pollaczek reference source assessment1594

TARGET: Assess source coverage for degree-dependent affine Meixner-Pollaczek references to unchanged P_d, with lambda_d>0 and 0<phi_d<pi, for three leading residual cancellations and a fourth/fifth Schmeisser-cost test.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1595 searched exact family, prescribed/leading-coefficient, Schmeisser, Jensen-reference, coefficient-matching and varying-parameter terminology; checked C028a/c/j and named flow failures plus reused source-notes1503/1591/1587. Queries/read limits are in source-notes1595; no novelty claim.
SOURCE_EVIDENCE: NIST DLMF v1.2.8 (18.19.6)-(18.19.9), (18.20.10), (18.22.7)-(18.22.8), (18.23.7), (5.11.9); author-hosted Koekoek-Swarttouw as98.pdf Section1.7(1.7.1)-(1.7.4),p37,(1.7.11),p38,Section2.7,p56; Wang-Qiu-Wong2011 doi10.1016/j.crma.2011.08.020 parameter setup and Theorem4 inspected as contrast only. Precise URLs/qualifications in drafts/literature/2026-11-18-affine-pollaczek-source-notes-1595.md; Schmeisser coverage reused.
COMPARISON: Exact formulas cover every finite admitted parameter tuple without uniform asymptotics. Wang-Qiu-Wong's lambda_n=(n+1/2)A,constant A>0,fixed angle does not cover arbitrary joint boundary approaches or fixed-P_d optimized cost. Existing local stops concern other reference recurrences or coefficient flows. No inspected result pays or obstructs this exact diagnostic.
GAP: Actual-P_d three-coefficient matching, admissible degree dependence and fourth/fifth retained cost remain uncomputed. Full Schmeisser payment, actual-Xi positivity and realization remain independent gaps.
REASON: Essential source coverage is now sufficient for a bounded routine specialization, not a new general orthogonal-polynomial theorem. Import the classical identities; justify affine/norm factors and compute only the stated difference after separate approval of assessment1595.
SCOPE: Integers d>=5; unchanged actual coefficients, fixed v=S_2>0,tau=S_3>0 from C028a; one common lambda_d,phi_d,real m_d and nonzero real sigma_d for all basis degrees 0<=n<=d, with arbitrary degree dependence and boundary approaches. No RH, root-reality, simplicity or conditioning premise.

## Completed review1595

The exact family and bounded test are recorded in
`2026-11-18-affine-pollaczek-retained-cost-test-1595.md`, with primary
citations and read limits in `2026-11-18-affine-pollaczek-source-notes-1595.md`.
No feasibility, cost bound, new lemma or mathematical script was produced.
The newly written ready continuation receives its separate approval next
turn. This completes source review, not its mathematical execution.

## Original nomination1594 (preserved historical scope)

The remaining paragraphs preserve the pre-review nomination; their
missing-source descriptions and search instructions describe its state
before review1595 and are superseded by the completed fields above.

### Proposed diagnostic, not approved mathematics in1594

Investigate the monic affine normalization of standard
P_n^(lambda)(z;phi), z=(x-m)/sigma. Retrieve its correct normalization
and positive measure rather than assuming them from notation. For the
resulting expansion P_d=sum a_n*q_n, first ask whether
 a_(d-1)=a_(d-2)=a_(d-3)=0
can hold along unbounded degrees. Only if feasible would the proposed
mathematical diagnostic test

    B_d=(h_(d-4)*a_(d-4)^2+h_(d-5)*a_(d-5)^2)/h_(d-1)

against the necessary threshold B_d=o(d^2). This is a proposed test,
not a calculation or approved result. Eventual infeasibility or a uniform
positive retained-cost floor stops this family; vanishing retained cost
still leaves the full sum unpaid. No parameter sweep is requested.

The candidate angle parameter and prospective two-sided weight motivate
checking a possible difference from the Gamma boundary stop. No advantage
is established. Reject redundant reparametrizations and known obstructions
before allocating mathematics; do not enumerate classical families without
a discriminating test.

## Failure comparison and missing coverage

The following narrowly relevant records were read for this nomination:

- ATTEMPTS/2026-10-30-moment-only-pollaczek-preservation.md: L530's
  two-atom outward-flow counterexample.
- ATTEMPTS/2026-10-30-theta-pollaczek-weighted-retest-overlap.md:
  the purported extra coefficient weight repeats that moment family.
- ATTEMPTS/2026-11-09-universal-pollaczek-discrete-step-stop-111.md:
  L955's fixed-parameter universal discrete-step obstruction.

They do not certify the new reference construction. No theorem beyond
their stated scope is imported. This proposal changes only the reference
basis of unchanged actual P_d, unlike the failed flow implications.
C028a/c and C028h/i retain their precise cost/compression stops.
Source-notes1503 already searched generic measure optimization; reuse
that comparison rather than repeating it without the specified new family.

Next turn must search exact-family and stronger-result terminology,
then inspect primary finite formulas and parameter qualifications before
larger extracts. Reuse Schmeisser's theorem/proof coverage. Fixed
lambda=3/4,phi=pi/2 coverage alone does not cover the proposed range.
Check varying parameters, negative affine scale and boundary cases.
No new external formula or theorem is claimed inspected by this note.

Main gap: L030-L032/C032a positivity and C028b's H_d=o(d), equivalently
C028g's S_F=0. Passing this diagnostic would not supply either. Odd
cancellation, unsmoothed realization and full residual control remain
open. Full matching Mathlib coverage is unknown. This nomination is not
ready or creative: exact sources and a concrete advantage are missing.
No mathematics on this target was performed or approved in audit1594.
