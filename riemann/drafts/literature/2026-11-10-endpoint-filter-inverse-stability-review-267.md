# Exact filter inverse stability — bounded source assessment

TARGET: Assess subexponential stability of L990's exact three-term coefficient operator on real sequences of at most exponential growth.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step268 completed bounded exact-filter, inverse-growth, Poincare-Perron, Bohl-Perron and singular-cocycle searches and the scoped November10 duplicate/failure check; queries and inspected versus unread sources are recorded in 2026-11-10-endpoint-filter-inverse-source-notes-268.md. No adequate match was established; this is not a novelty conclusion.
SOURCE_EVIDENCE: Read Borcea-Friedland-Shapiro2011 Theorems2-5 pp198-200 https://staff.math.su.se/shapiro/Articles/Poincare-Perron.pdf#page=2; Berezansky-Braverman2004 Theorem1 with full proof pp23-25 and assumptions pp20,22 https://www.ariel.ac.il/wp/fde/wp-content/uploads/sites/97/2020/02/2004-1-2.pdf#page=24; their0906.3239v1 Lemma1 pp2-3 https://arxiv.org/pdf/0906.3239v1#page=2; Jitomirskaya-Marx1106.6097v1 Theorem1.2, equations1.5-1.8, Lemma2.9/proof and Theorem3.1 pp1-2,7-8 https://arxiv.org/pdf/1106.6097v1#page=2; Czornik-Kitzing-Siegmund2305.16408v2 section1 pp2-3 https://arxiv.org/pdf/2305.16408v2#page=2. Step269 rechecked direct access and selected hypotheses; full comparison remains in source-notes268. Reuse the existing L990/C990a asymptotic contracts without refresh.
COMPARISON: None of the inspected results decides this exact implicit operator: coefficient convergence, explicit bounded recursion, bounded-forcing admissibility, stable comparison, analytic cocycle representation and requisite frequency/control hypotheses are not established here. Cesaro inversion and the polynomial degree recurrence concern different operators. Cofinite vector definition supplies no pivot bound. These are missing applicability hypotheses, not proofs that such hypotheses fail.
GAP: The E-to-S implication below remains unresolved; no exact null sequence, finite positive growth rate, inverse estimate, individual coefficient bound or arithmetic transfer has been derived. Phase collisions and arbitrary finite initial data must be retained.
REASON: The source gate now permits one bounded exact-operator attempt, first testing an exponentially growing homogeneous null sequence; no general stability theorem is imported and no source needs to be reproved. The unused descriptor-system lead is not essential to this explicit test and is not a premise.
LITERATURE_REASON: Essential coverage for the newly nominated infinite-sequence question was absent from the ready finite-transform assessment; step268 supplies this one source comparison, not another synthetic-response audit.
SCOPE: Exact integer-index coefficients from L990, all n beyond a fixed cofinite-definition onset furnished by C990a; arbitrary real scalar sequences of at most exponential growth, two-sided every-epsilon bounds, no actual-prime or RH assertion. One bounded attempt on the stated implication, initially its homogeneous counterexample test; no leading-phase replacement, unproved pivot division or generic cocycle import.

## Exact test, not a derived theorem

Fix any N beyond C990a's existence onset. Use exactly the oriented,
l1-normalized coefficients c_(n,j) of L990 for n>=N. For a real
sequence x=(x_n)_(n>=N), define the proposed sequence operator

    (T x)_n = c_(n,0)*x_n+c_(n,1)*x_(n+1)+c_(n,2)*x_(n+2).

Let E consist of sequences with |x_n|<=C*exp(A*n) for some finite
C,A>=0. Let S consist of sequences for which, for every epsilon>0,
there is a finite C_epsilon with |x_n|<=C_epsilon*exp(epsilon*n)
for all n>=N. The proposed implication to assess is

    x in E and T x in S  ==>  x in S.

No assertion about this implication is made now. Finitely many
initial values are unrestricted. A counterexample must give an exact
x in E with T x in S and limsup log(1+|x_n|)/n>0; an exact
exponentially growing null sequence would suffice. Finite numerical
growth, a leading-phase substitute for c_n, or division by an
unproved nonzero c_(n,2) is insufficient. C990a does not bound any
one coordinate away from zero. L990's phase-collision neighborhoods
must not be discarded in an all-index stability claim.

## Relevance, comparison and stopping test

Main gap: actual-Xi positivity L030–L032/C032a and L966/L968 signed
forcing. Actual B_n and L984(H) remain unbounded. This question tests
only whether bounds for a single filtered observable could retain
the unfiltered information. Stability would still require a separate
identity between common-interval arithmetic integrals and T B,
control of the shifted boundary intervals, all prime powers, a signed
filtered bound, both complements and transfer to L984(H). None is
assumed or proved here. Failure stops only this single-observable
norm-transfer mechanism; extra arithmetic structure could matter.

Three directions were compared at nomination level:

1. Repeat synthetic response or sharpen its already sufficient
   remainder: the diagnostic now passes, but supplies no arithmetic
   information. Close this continuation without another parameter test.
2. Direct automatic lobe/average or centered-Vaughan payment: the
   stops233/235/244 retain their exact obstructions and no new signed
   arithmetic input is available. Do not repeat those mechanisms.
3. Test exact inverse stability of the coefficient operator: select
   this different transfer gap. It is neither the classical Laguerre
   degree recurrence nor Cesaro inversion and has a concrete failure
   witness independent of assuming actual off-line zeros.

Step268 completed the source comparison in
[source-notes268](2026-11-10-endpoint-filter-inverse-source-notes-268.md).
The nomination's REVIEW_REQUIRED state is superseded by EXPLORE,
with the exact target unchanged. No implication, counterexample or
operator identity has been derived in this literature-only step.

For the subsequent mathematical attempt, first seek an exact real
homogeneous witness Tx=0 on every n>=N with both a finite exponential
upper bound and a strictly positive limsup log(1+|x_n|)/n. A positive
finite sample or an unbounded transfer-matrix norm alone does not meet
this test. Any recurrence division must first justify its pivot on
every index where used, and every exceptional index must be treated.
If this construction cannot be justified, preserve the actual obstruction;
it does not prove stability. A proof of the original implication instead
must cover nonzero subexponential forcing and all permitted initial data.
Only a rigorously established witness stops this transfer mechanism;
absence of a witness in one attempt is inconclusive.

Essential inputs: L990 and C990a; L985 only for kernel conventions.
L982/L984 are downstream comparisons, not premises about arbitrary x.
No cross-notebook input. Full matching Mathlib coverage is unchecked.
The next mathematical routing is proof_attempt/development,
deep_research/xhigh: this is a singular infinite-sequence growth problem,
not another finite asymptotic check. No
central creative proof attempt is nominated: an independently useful
signed arithmetic mechanism and source coverage are still missing;
do not relabel an abstract inverse-stability prerequisite as such.

## Direct-source recovery, step269

10 November 2026. The supervisor reported that ready assessments need
a direct source URL. Source-notes268 already contained these URLs;
SOURCE_EVIDENCE above now carries them directly. All five PDFs opened
successfully. Rechecked Theorems2–3 of Borcea–Friedland–Shapiro,
Berezansky–Braverman2004 Theorem1 and its bounded-forcing hypothesis,
their2009 Lemma1 and its strict comparison bound,
Jitomirskaya–Marx Theorem1.2 and its analytic/Diophantine setting,
and Czornik–Kitzing–Siegmund section1's invertibility and bounded-inverse
assumptions. The original detailed comparison and proof-case coverage
are reused, not claimed as new evidence. The target, scope, EXPLORE
decision and mathematical threshold are unchanged. This is a STALLED
process repair, not a new obstruction or mathematical advance; no
lemma, mathematical script or operator argument was written.
