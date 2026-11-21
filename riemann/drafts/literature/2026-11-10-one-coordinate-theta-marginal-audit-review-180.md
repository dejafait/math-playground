# One-coordinate marginal obstruction — audit coverage approved

TARGET: Audit C969a's complete one-coordinate marginal and negative diagonal limit at n=2, including every signed term, actual normalization and moment domination.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step181 reused step179's exact-marginal searches and primary comparison without repeating external searches; narrowly searched November10 Li/theta/profile assessments, histories and stops for C969a, one-coordinate, marginal and moment comparison. Read the complete C969a proof and the step179/180 history and stop records; no separate completed C969a audit was found in these records. No novelty inference.
SOURCE_EVIDENCE: Reused the inspected primary Mathlib Integral.Prod statements integral_prod and integral_integral_swap recorded in 2026-11-10-one-coordinate-theta-marginal-review-178.md, and the calculus/normalization comparison in 2026-11-10-h-derivative-profile-audit-review-176.md. Read L019 in full, L966 hypotheses/(1)-(4) and its H-series convergence proof, and L969 hypotheses/(1)-(8), integration proof and audited scope. No new external source or certificate computation was needed for this scope review.
COMPARISON: Absolute Fubini, convergent nonnegative-series comparison, order preservation of integration, finite-sum limit laws and continuity cover the proof methods under explicit hypotheses; none verifies C969a's coefficients or signed limit. The prior assessment's conditional-positivity and Oudghiri results supply no automatic marginal sign. Independently checking this fixed contraction and actual-moment specialization is necessary; reproof of integration theorems or the L967 transfer is unnecessary.
GAP: The exact audit now has adequate source coverage, but its mathematical checks remain pending: reconstruct every labeled contraction, prove all-point slice convergence, check actual normalization and moment domination, and verify the complete diagonal limit and negative-region implication. The final integral and all-n positivity remain unresolved.
REASON: Step181 separately approves known-method coverage for the unchanged audit target; no new mathematical result is derived or accepted. Preserve step180's informative negative while independently checking its proof in the next research turn. No essential source is blocked.
LITERATURE_REASON: The newly nominated independent audit was REVIEW_REQUIRED at invocation; this literature-only turn compares its precise scope with ready coverage. This is separate approval of the changed audit object, not another sign test or a repeated review of an already ready audit.
SCOPE: Only C969a at n=2,b=1/4,h=5184,q=72,gamma=1/[2(c_0+c_1)], with complete L969(5) and actual A,H_r moments. No profile tuning, general-n extension or second-coordinate averaging.

## Completed source-scope comparison — step181

The exact TARGET is ready for one independent proof audit, classified
REPRODUCTION under SPECIALIZE. This turn is EXPLORATION, LITERATURE,
NOVELTY_UNCHECKED: it completes a previously missing scope comparison,
without accepting C969a or claiming mathematical progress beyond the
checked sources. Its independent verification remains pending.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity;
on this route the unpaid condition is all-index L966(16), R_n<=N_n.
The intermediate target validates or corrects C969a's reason for
retiring one-coordinate pointwise payment. Its downstream use is a
reliable obstruction for selecting a different payment mechanism.
It cannot decide the final signed integral or the all-index inequality.

### Primary hypotheses reused and audit specialization

The inspected official [Mathlib Integral.Prod statements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Prod.html#MeasureTheory.integral_prod),
including [integral_integral_swap](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Prod.html#MeasureTheory.integral_integral_swap),
are recorded with retrieval date 10 November 2026 in the step179
assessment. They identify product and iterated integrals for integrable
functions with S-finite measures. They supply no sign. The proposed
specialization is the real-valued finite tensor sum under the measure
A(u)du in each coordinate. Its finiteness and absolute integrability
must be checked using L019's bound and the fixed hyperbolic factors.
General Fubini gives slice integrability only almost everywhere;
C969a's all-u,v statement instead needs its explicit factorwise bound
for each fixed slice. Neither a nonnegative input nor a probability
normalization is required for absolute Fubini.

The local primary input for the proposed moment comparison is the
entire series L966(3), with its convergence justification in the
section “Positive theta derivatives and finite chain differentiation.”
The series is indexed from l=r, with powers x^(l-r). The audit must
check its parameter domain and nonnegative coefficients before using
ordinary comparison of convergent nonnegative series at h>b>0.
It must then check positivity of A, convergence of the actual moment
integrals and order preservation of integration. These elementary
order arguments require no new probability theorem. This review
identifies their hypotheses; it does not perform the comparison or
verify C969a(5)-(6).

L969(5) is the complete starting tensor, and L969(7)-(8) provide the
fixed-parameter factor limits. The audit must verify the proposed
contraction against that tensor before taking limits of its finite
sum. No limit through an improper integral is proposed: a common
majorant for such an interchange is therefore unnecessary. All
normalization moments and gamma remain fixed before t tends to
infinity. The separate proof must justify continuity and positive
A-product measure when passing from a strict negative limit to a
negative box; no effective onset is required.

The prior ready profile-audit comparison covers finite-interval
integration by parts and improper endpoints (NIST DLMF 1.4.16,
1.4.22-23), but this audit starts after the established L967 transfer.
Repeating that transfer or proving the calculus afresh would not
check the new contraction. Reuse the inherited scope. The step179
assessment also inspected Oudghiri, arXiv:2012.08808v2, Section3,
Theorem3 p5 and continuous proof pp6-7: its independent log-concave
density and weighted monotonicity hypotheses concern conditioning
on a sum. They are not hypotheses of this fixed-coordinate audit.
Its conclusion is not a sign import here. No new theorem application
or extended literature search is warranted by the unchanged factors.

### Bounded decision and limits

Continue to the exact audit once this assessment receives the separate
supervisor approval. Reconstruct the six labeled placements of each
of the four tensors, including repeated labels and every sign; check
the h-origin, complete C_1, actual normalization, all slices, and
every surviving limit term. Accept the scoped obstruction only if
the complete limit and actual-moment argument are valid. A concrete
coefficient, convergence, normalization or inequality defect requires
correction or qualification. A positive grid cannot decide the audit.
The stored certificate is construction evidence, not independent
verification; no certificate values were checked in this review.

The step180 stop, audited L967/L969 full-kernel stops and finite-window
stop are preserved. The local searches found only the C969a construction
and this nomination as the matching new marginal records, not a
duplicate independent audit. The bounded search establishes neither
originality nor absence of a theorem elsewhere. Optional source
blockers in earlier comparisons remain inessential and parked.

Essential inputs are C969a (audit object), L019, L966 and audited L969;
L967 and the L018/L024/L026 framework remain inherited. No RH,
simplicity, numerical normalization bound, uniform onset or cross-
notebook premise is added. Full matching Mathlib coverage is unknown;
the cited Fubini statements are supporting results only. Final integral
and all-n signs remain open. No lemma, mathematical script, DAG or
PROOF argument changes in this literature step.

Recommend proof_audit/routine_audit, standard/high for the exact TARGET:
the bounded work is independent finite contraction and ordinary
explicit analytic hypothesis checks, using the established transfer,
with no new mechanism or candidate RH argument. Further literature
requires a specific newly essential source or changed hypothesis.

## Original nomination — step180, preserved

The following prospective instructions record nomination time and are
superseded by the completed coverage decision above.

### Separate coverage review requested

Step180 completed the ready marginal test and found a strict negative
diagonal limit. The canonical proof is C969a; its finite check is
`scripts/li-theta/one-coordinate-marginal-check-180.py` with the matching
JSON certificate. This nomination does not approve that proof or
invalidate the completed NEGATIVE research outcome.

The next turn should compare this precise audit with the prior ready
marginal assessment and its inspected integration hypotheses. Reuse
the already checked sources while their scope is unchanged; identify
a concrete missing hypothesis before opening any new source. The
review itself must not modify lemmas or mathematical scripts.

The subsequent audit should reconstruct the six labeled placements
per original tensor, retain the h-origin and complete C_1, and verify
that (2) is the entire exact contraction. Check slice convergence for
every u,v, not just almost everywhere. Then check (4), the normalization
substitution, the moment comparison and (6), and whether continuity
really supplies a positive-measure negative box. An audit must accept
the proof with its scope or identify a concrete failed identity or
hypothesis; a positive grid cannot overturn or verify an asymptotic
argument.

Essential mathematical inputs are C969a, L019, L966 and L969; L967's
transfer and the L018/L024/L026 framework are inherited through those
inputs. No cross-notebook result, RH, simplicity, effective gamma
estimate or uniform onset is assumed. C969a's independent verification
is pending; its final integral and all-index comparison remain open.
Full matching Mathlib coverage is unknown. After separate approval,
the expected task is proof_audit/routine_audit, standard/high: the
remaining work is exact finite contraction and explicit elementary
analytic hypothesis checking, without a new payment mechanism.
