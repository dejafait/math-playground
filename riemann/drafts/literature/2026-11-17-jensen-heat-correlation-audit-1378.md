# Shifted heat-correlation proof — audit nomination1378

TARGET: Audit C019l's full shifted heat-correlation proof, including the gamma reduction, both moving-entry product channels, the O(X*log log X) error and the negative leading coefficient.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1379 reuses assessment1377 and assessment1376/review1377 exact-target searches; narrowly read C019l, C019k definitions/audit1376, and stops1345/1355. No changed correlation, new discovery search or novelty claim.
SOURCE_EVIDENCE: Direct sources https://arxiv.org/html/0803.1141v2#A and https://dlmf.nist.gov/5.11.i (equations https://dlmf.nist.gov/5.11.E3 and https://dlmf.nist.gov/5.11.E4); recovery1380 reopened the cited statements on 2026-11-17. Review1379 inspected Koesters0803.1141v2 AppendixA.2-A.3 directly and DLMF5.11(i)/(5.11.3)-(5.11.4), including sector hypotheses; reused assessment1376/1377 for the primary product proof cases and shifted-moment comparison. C019k definitions/audit1376 fix the normalization.
COMPARISON: C019l derives the actual moving-heat signed correlation using those inputs, rather than importing a shifted-zeta theorem. Its claimed remainder and coefficient are local mathematical work, not independently audited source facts.
GAP: Check C019l's gamma sign/factor, all phase derivatives, actual entry intervals, amplitude variation, both product channels, diagonal floor replacement, coupled-scale limiting coefficient and one common onset. No root-transfer assertion is included.
REASON: Separate literature review1379 approves source coverage for the unchanged conceptual audit only. No essential unread theorem was identified in the proof inventory; C019l remains unaudited and no mathematical correctness is certified.
SCOPE: Exact C019k data, d tending through positive integers, X=Y_-, h=3*pi/log(X), both actual floors, no RH/nonvanishing/simplicity/heat real-zero assumption, existential onset.

## Inputs and reuse

The canonical result is C019l. Its sole direct mathematical notebook
input is C019k. The latter inherits C019j and L018/L021's actual-xi
conventions; no cross-notebook input is needed. Read C019k's explicit
functions and the relevant gamma/scale ranges, not unrelated histories.
The source assessment is
[assessment1377](2026-11-17-jensen-heat-correlation-attempt-1377.md),
with its detailed inspected-source record in assessment1376.
No historical Selberg or Atkinson proof is a premise.

The completion of attempt1378 and this nomination do not independently
validate C019l. Review approval should reuse the unchanged coverage,
checking that every new manipulation is within its explicit finite-sum,
Stirling, variation and oscillatory-estimate scope. Refresh source
coverage only if an essential unassessed theorem or changed hypothesis
is actually found. No further browsing is needed merely because a new
proof file exists. Matching full Mathlib coverage remains unchecked.

## Bounded audit and downstream limits

The critical claims are that the entire sum-phase channel is O(X),
including entry endpoints, and that the unequal-index difference
channel is O(sqrt(X)*log(X)) on its asymmetric actual entry intervals.
The gamma reduction is pointwise; its errors must not be differentiated.
Verify that every discarded term is o(B*log(X)), not just that the
diagonal has a negative sign. The exact limiting weight and constant
in C019l (1)--(2), and the comparison at z=1/6, must also be checked.

Accept the local result only if its negative margin and common onset
survive all cases. Otherwise isolate the first failed claim and repair
it within assessed scope or return it to review; do not infer RH is
false or automatically reopen stopped routes.

Even a successful audit leaves quantitative amplitude control, robust
disjoint ordered samples, C019j/C019k error transfer to actual Jensen
values, c*sqrt(d) additional roots, bulk separation and all-degree
positivity open. No such assumptions are supplied by this nomination.
The next settings are a conceptual proof audit, not candidate-RH review.

## Completed source gate1379 — 17 November 2026

This separate literature-only step approves the saved audit target, not
C019l's conclusion. Its source inventory is within assessment1377's
finite-sum/Stirling/oscillatory-estimate scope. EXPLORE permits the
conceptual audit with REPRODUCTION or POTENTIALLY_NEW classification;
it does not import the heat-correlation theorem. No lemma or mathematical
script was changed, and no new asymptotic or sign was derived.

The directly reopened primary item is H. Kösters, *On the Occurrence of
the Sine Kernel in Connection with the Shifted Moments of the Riemann
zeta function*, arXiv:0803.1141v2, 5 September 2008, Appendix A.
A.2 requires a real twice differentiable phase and a uniform strictly
positive lower bound for either its second derivative or its negative;
the bound is 8/sqrt(epsilon). A.3 bounds the unweighted sum over
1<=m<n<=M of 1/(sqrt(m*n)*log(n/m)) by O(M log M).
These match the source statements cited in C019l, not proofs that its
phases or weights satisfy them. The canonical lemma gives an abbreviated
paper title; the exact bibliographic title is recorded here. The
Titchmarsh attributions are Lemmas 4.4 and 7.2 in its second edition;
the original book was not newly consulted.

DLMF §5.11(i), equations (5.11.3)-(5.11.4), accessed 17 November
2026, states the scaled-gamma expansion in a fixed sector
|arg z|<=pi-delta, delta>0, with g_0=1 and g_1=1/12.
C019k's specified z=s/2 and principal branches are the intended
specialization; its audit1376 already checks the fixed sector. This is
a pointwise expansion, not a license to differentiate an unspecified
error. C019l's explicit phase reduction and its complex sign remain
mathematical claims for the next audit.

No additional shifted-moment theorem is needed merely to review this
proof. Assessment1376/review1377 retains the inspected primary
Section2 product proof cases, Bettin comparison, and Mawia entry-method
qualifications. The unread Selberg/Atkinson originals are not premises.
Stops1345 and1355 were read narrowly: unpaid exterior control and fixed
endpoint opposition do not certify or refute the different band average.
Stop559 and the parked direct (A) route remain as recorded in the reused
assessment. No duplicate matching heat theorem is established by this
review; failure to locate one does not establish novelty.

The audit must still check every local step: exact C019k functions in
(6), gamma sign/factor in (7), uniformity before index entry, derivative
and variation estimates, the two distinct entry thresholds, all of the
sum channel, both unequal-index orders in the difference channel, and
the diagonal floor replacement. It must also check the coupled-scale
error, constant and sign comparison, and one common onset. Elementary
finite-sum identities, differentiation, integration by parts and sum to
integral comparisons are local proof obligations, not new literature
hypotheses or results established by this gate.

Accept only if the full error is below the claimed negative margin;
otherwise isolate the first failed claim and repair only within assessed
scope. A changed target or essential unassessed theorem requires renewed
coverage. Even acceptance supplies neither quantitative amplitude/error
transfer nor disjoint ordered Jensen samples, an exceptional-root count,
bulk separation, or all-degree positivity. Full matching Mathlib coverage
remains unchecked. No further browsing is prescribed for the unchanged
ready audit.

## Direct-source repair1380 — 17 November 2026

The supervisor reported missing direct source URLs in this ready assessment.
Opened [Kösters v2, Appendix A](https://arxiv.org/html/0803.1141v2#A)
and [DLMF §5.11(i)](https://dlmf.nist.gov/5.11.i) successfully.
Rechecked the complete A.2 and A.3 statements, and DLMF's sector condition
and [equation (5.11.3)](https://dlmf.nist.gov/5.11.E3).
The corresponding coefficient reference is
[equation (5.11.4)](https://dlmf.nist.gov/5.11.E4).
These direct links repair traceability; they do not establish that C019l
satisfies the hypotheses or that its remainder and sign are correct.
The saved TARGET, EXPLORE decision and scope remain unchanged. Existing
source comparisons and route stops are reused; no new discovery search,
mathematical derivation, lemma or script is part of this recovery.
This is a STALLED process repair, not mathematical progress or a claimed
counter reset. The exact conceptual audit remains the single next action.
