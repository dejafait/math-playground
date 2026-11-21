# Assessment657, completed658: finite-cosine Carleman evaluation

TARGET: Assess validated finite-cosine Carleman evaluation for the six frozen parity densities at a*2^-80<=t<=a to pointwise error at most2^-53, including small-argument cancellation and a finite scalar work bound.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review658 checked the scoped12November Carleman records and separation-seven code for Si/Ci/Cin duplicates, then searched DLMF definitions/series and validated Si/Ci algorithms; inspected primary DLMF statements, Johansson1606.06977v2 Theorem1/proof and algorithm cases, Arb2.23.0 si.c/ci.c, and1410.7176v2 Sections2-5. Full evidence is in2026-11-12-finite-cosine-source-notes-658.md; no novelty inference.
SOURCE_EVIDENCE: DLMF1.2.8 equations6.2.9,11-13,19-20;6.6.5-6;6.7.13-14;6.12.5-8 and remainder bounds; Johansson1606.06977v2 Sections3.1,4.1 Theorem1/proof,4.2,6.5; stable Arb2.23.0 Si/Ci implementation branches; Johansson1410.7176v2 Sections2-5. Reuse C998a/audit655 and review655/comparison656 inclusion coverage.
COMPARISON: Known primitives, convergent tails and positive-real auxiliary asymptotic remainders cover a standard validated-evaluation method. They neither import the six frozen transforms verbatim nor guarantee requested accuracy, uniform cancellation control or a practical work bound. C998b's direct3031-node cost stop remains prescription-specific and unaudited.
GAP: A separate REPRODUCTION must derive/check the finite-interval identity and parity signs, retain the zero mode and exact neutral coefficients, and specialize truncation, input, rounding, cancellation and all scalar costs to the whole six-sum error2^-53 on the stated t range; no such ledger is proved658.
REASON: Primary identities and effective error algorithms are now accessible and inspected. Quantitative fixed-data assembly and cost are the remaining specialization, not an essential missing general theorem. The continuation is separately nominated in review658 and must receive its own approval before research.
LITERATURE_REASON: The next target changes the inner oracle from assessed Gauss integration to special-function evaluation of a finite cosine transform; its identities, cancellation control and certified evaluation costs were not covered by the ready quadrature assessment.
SCOPE: Unchanged a=log(3)/4, B0 delta=.01,m=286,J=14, three frozen652 trials with exact C999q neutral completion, and the six real C998a parity densities; no trial/reference retuning or sign theorem.

The main gap remains L030-L032/C032a actual-Xi positivity and the signed
S3 remote-plus-induced comparison. A certified point evaluator could
support the incomplete outer full-norm ledger, then C999 inverse-action
errors and a separate signed pairing test. It would not settle those
pairings, higher/mixed endpoints, C744q/H2 or global assembly.

The658 source record gives exact URLs, versions, hypotheses and inspected
algorithm cases. Ordinary floating implementations and successive-precision
agreement remain inadequate certificates. Exact identities, enclosure error
and practical work are distinct obligations. Mathlib matching coverage is
unchecked. No new lemma, evaluator or mathematical script was written658.

The pointwise threshold is for each entire parity density, not one
frequency term. Pay every coefficient, neutral-completion and argument
error, the constant frequency and the complete sum through255. The
interval starts at a*2^-80>0; behavior there can involve cancellation
even though no endpoint pole is sampled. No special-function identity
or error formula has been derived in this nomination. The six arrays
are nonzero; no rank6 assertion is made.

Coverage now supports a separate bounded attempt to construct that ledger;
it does not assert that any sufficient cost is usable. Continue only after
the specialization supplies a uniform whole-sum error and explicit scalar
work count. A black-box precision request or adaptive doubling is not a
finite worst-case ledger. If the prescribed evaluator misses its declared
budget, preserve that stop and choose an independently testable mechanism;
do not repeat the stopped652 or657 direct prescriptions.

Essential local inputs are C998a/audit655 and complete654/655 ledgers;
C999/audit650 Sections3-4; C999z/audit646; C999q exact Z; C999y/audit642
exact X; and the full C744v operators. Retain C744w/z and C999k's
analytic/arithmetic/source-to-Xi/whole-core/unreplayed c_* contracts.
The archive remains `scripts/separation-seven/frozen-reference-proposal-652.npz`,
SHA256 `2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6`.
C998b and its complete657 planning certificate record the new stop and
partial budgets, but remain unaudited; no downstream certificate may
silently treat them as audited. Outer analyticity/error, finite scalar,
forcing, Gram-projection and norm-width control remain unpaid. No
cross-notebook input is proposed.

This is preparatory numerical analysis, not a new sign-producing central
mechanism. The blocker to a justified creative nomination remains a
complete quantitative residual/pairing estimate and an independently
motivated signed comparison. Do not label this evaluator creative to
meet a scheduling preference.
