# Finite count for the three-width cap — source review1877

TARGET: Locate and inspect a primary rigorous bound N(100)<=100, counting all positive-ordinate zeta zeros with multiplicity and the endpoint, for C034k(11)'s missing cap input.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused assessment1196 and C030i's precise HSW import and endpoint passage; checked C034k's exact hypotheses and(11), stop1876 and source-notes1875. External query: Hasanalizade Shen Wong Counting zeros Riemann zeta function Corollary 1.2 100 multiplicity. The fixed-height bound is not a new counting theorem; no exhaustive-search or originality claim.
SOURCE_EVIDENCE: Hasanalizade–Shen–Wong, Counting zeros of the Riemann zeta function, J.Number Theory235(2022),219-241, DOI10.1016/j.jnt.2021.06.032; directly retrieved arXiv:2107.06506v1,14July2021, definition p1, Corollary1.2/(1.5) p2, Section2/(2.1)-(2.3) p3 and complete small-height proof(5.5)-(5.6) p15; https://arxiv.org/pdf/2107.06506v1 . Existing C030i supplies the inclusive-height reconciliation, not a fixed count at100.
COMPARISON: The primary unconditional explicit total-count estimate is valid for all T>=e and covers the needed height; C030i already reconciles multiplicities and boundary atoms. A later elementary specialization must compare its upper bound at100 with100. No approximate zero table, critical-line-only count, or new zero-counting proof is needed.
GAP: The source gate is paid. The fixed-height arithmetic and application to C034k(11) are deferred to research, together with independent audit of C034k(1)-(5). No N(100) value, S4 bound or actual cap is certified in this literature-only step.
REASON: The missing count input has inspected primary coverage, reused from1196 rather than renewed Rosser retrieval. The source statement is imported; only the bounded application remains. A ready audit nomination1877 receives separate approval before invocation.
LITERATURE_REASON: Nomination1876 explicitly left the essential finite-count input uncovered; this source-only review supplies it without repeating interpolation research.
SCOPE: Full actual positive-ordinate zeta-zero occurrence count at100, multiplicities and closed upper endpoint; elementary specialization of HSW Corollary1.2 only. No reproof of its analytic estimates or certified finite computations; no changed divisor, scalar evaluator, new zero-free region or Xi realization.

## Exact imported input and inspected cases

Import Elchin Hasanalizade, Quanli Shen and Peng-Jie Wong,
*Counting zeros of the Riemann zeta function*, the version and
locations above. Corollary1.2 states, unconditionally for every T>=e,

    |N(T)-F(T)| <= B(T),
    F(T)=T/(2*pi)*log(T/(2*pi*e)),
    B(T)=0.1038*log(T)+0.2573*log(log(T))+9.3675.

The center has no7/8. The definition includes 0<gamma<=T in the
whole critical strip. Section2's argument principle establishes
multiplicity, rather than a count of distinct ordinates. Its
small-height proof covers e<=T<=30610046000 using(1.7),(2.7),
(5.5)-(5.6); it does not require applying the large-height theorem
at100. Those finite-computation inputs are imported with the theorem,
not independently reproduced. No RH assumption is imposed.

C030i's existing proof passage immediately after(4) reconciles a
contour initially avoiding zeros with inclusive counts by a decreasing
sequence of nonzero contour heights and continuity of F,B. Reuse
that argument in the later application; do not assume100 is not an
ordinate. Its hypotheses are the actual locally finite zeta divisor.
The source completion differs from the local completion by a nonzero
constant, so the zero counts agree, as already recorded in C030i.

The direct reading confirms the needed statement and essential
small-height case. Source-wide correctness, the finite computations
inside the imported theorem, and full matching Mathlib coverage are
not independently certified here. The count theorem may be cited;
none of its proof needs a local reproof. The new work needed is only
explicit elementary arithmetic and the exact local multiset interface.

## Reuse, failure comparison and continuation

Assessment1196 had already inspected this theorem. C030i imports it
and proves interval-existence for r>=100 and a quadratic envelope
for r>=1000; neither conclusion states the needed fixed count at100.
Its theorem statement and endpoint argument are ready inputs, so do
not repeat its interval/separation calculations or certificate. The
persistent original-Rosser access failures recorded in1196 need no
retry. Search also located the stronger Bellotti–Wong2412.15470 lead;
no theorem or proof was read for this review, and it is unnecessary
for this coarse threshold. No stronger bound is asserted here.

C034k(11) already identifies the downstream threshold and inherited
tail qualification. Preserve stop1876 as historical evidence, adding
this review as source access recovery without editing its conclusion.
The analytic comparison still awaits independent audit. Stops1798,
1839/1843/1847/1866 concern other mechanisms and remain untouched.

The main gap is L030-L032/C032a actual-Xi all-degree positivity.
The intermediate use is a possible feasible three-atom input for
C033w's two observations. Continue only if rigorous fixed-height
arithmetic and every estimate in C034k pass; otherwise record the
first failed comparison and stop this cap application. No full
observation, signed-height/cancellation or Xi-realization gap closes.
The absent independently paid central transfer mechanism still blocks
a justified creative nomination; the essential analytic audit takes
precedence and is conceptual, not a creative proof attempt.

The complete inherited assumptions and proposed audit are recorded in
[assessment1877](2026-11-20-three-width-analytic-cap-audit-1877.md).
No lemma, mathematical script, DAG or PROOF change was made.
