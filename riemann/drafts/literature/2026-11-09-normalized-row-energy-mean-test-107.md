# Normalized row-energy increasing-convex order: first-moment test

TARGET: Test the first-moment compatibility of increasing-convex order from L938's normalized negative row-energy law to its normalized positive row-energy law at lambda=0, using one fixed full-theta moment enclosure through M14.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step107's three-family discovery and exact L938/convex-order searches in 2026-11-09-central-mixed-positivity-discovery-106.md. No completed matching mean test was found in the scoped ratio, simplex, primitive, contact and Hall records inspected; no originality claim.
SOURCE_EVIDENCE: Direct primary source https://arxiv.org/pdf/1404.0999v3 (30 October 2015), Leskela-Vihola Section1.1 definition,p1; Section2.1 integrable-test convention,p4; Section2.2 Proposition2.3/Remark2.4,p5, inspected again in step108; known midpoint-Taylor/interval methods in L036/L037 and L917, with convergence framework in L938(6)-(10). Reuse saved numerical-method coverage, not a new integration theorem.
COMPARISON: Increasing-convex order is known and requires compatible means; positive convolution factors do not establish it. C938a refutes the stronger unnormalized density-ratio property. L916 concerns score coordinates. Neither settles this proposed normalized energy-law test.
GAP: Establish applicability, derive exact full first-moment formulas and certify their normalized difference with all rows/factorials. Numerical tail constants through M14 require proof. No mean sign, order or determinant sign is established by this assessment.
REASON: Step108 repairs the missing direct source URL and confirms the saved scope; the unchanged fixed mean test is approved for a subsequent research turn. This is source/process repair, with no new mathematical evidence or actual-law specialization.
SCOPE: Exactly TARGET, one REPRODUCTION calculation at lambda=0; all34 rows,twelve labelled factors,M_0^12. Fix64 equal spatial panels on[0,2],theta indices1..4,midpoint Taylor order8 and100-digit directed Decimal arithmetic as in L917. No grid,cutoff,precision,parameter or representation campaign; a zero-containing enclosure ends this test.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
Use L938's h_alpha and c_alpha without changing their definitions.
Proposed objects for the later application are

    V_plus(E)  = sum_(c_alpha>0) c_alpha h_alpha(E),
    V_minus(E) = sum_(c_alpha<0) (-c_alpha) h_alpha(E),
    m_plus/minus = integral_0^infinity V_plus/minus(E) dE,
    b_plus/minus = integral_0^infinity E V_plus/minus(E) dE,
    mu_plus/minus(dE) = V_plus/minus(E)dE / m_plus/minus.

Proposed mechanism, not a fact: mu_minus <=icx mu_plus. The test asks
only for its necessary mean compatibility, with intended orientation

    delta = b_plus/m_plus - b_minus/m_minus >= 0.

The later attempt must establish probability normalization, finite first
moments and the diagnostic's applicability from the named definition.
No such specialization is proved here. Leskela-Vihola assumes integrable
real random variables; increasing-convex order needs no endpoint
smoothness, contact or equal-mean premise. Its hinge criterion requires
every threshold. The cited proposition references Shaked-Shanthikumar4.A.2;
that book proof is unread and no new coupling theorem is imported.

Plausible use: a later full normalized comparison, independently proved
m_plus>=m_minus, and a justified integrable exp(lambda E) comparison
could support L938's d=2 Laplace signs for nonnegative heat time.
This is a proposed application, not a derived theorem. Do not discard
the mass ratio or assume detH2(0)>=0. A mean pass proves none of these
remaining statements. Other degrees, initialization, contacts, global
continuation and realization remain independent gaps.

Essential inputs: L019/L058 actual kernel/domination; L938 exact34-row,
12-factor convolution representation; L036/L037 inclusion and arithmetic
assumptions. L917 supplies a method and failure comparison, not M14
enclosures. C938a/L916/L943/L949/L953 are scoped contrasts, not sign
premises. No cross-notebook input. Mathlib coverage is unchecked.

Use nonnegative row algebra before division. Derive moments by justified
Tonelli/Fubini on full factors, retaining factorials when one factor
acquires an energy power; no undocumented size-bias or multinomial
substitution. Moments through M14 are prospective values to enclose.
Prove complete omitted-theta and spatial tails for every needed moment;
do not reuse L917's twelfth-moment constant for M14 without proof.
Retain L037's library/exponential/pi/operation assumptions explicitly.

Decisive evidence: certified upper endpoint delta<0 rejects this fixed
normalized-order direction. A certified lower endpoint delta>=0 passes
only the mean prerequisite; zero-containing bounds are inconclusive.
Report achieved bounds against zero, positive normalizers, all moment
tail/error allowances and full certificate paths. Midpoints and loose
intervals are not sign evidence. Stop after this one fixed test without
refinement. A later coupling, other threshold or sign mechanism needs
new coverage. This known-method discriminator is not a creative attempt;
no independently supported signed coupling warrants that escalation.

## Direct-source approval, 9 November 2026 (step108)

Inspected [Leskela–Vihola, arXiv:1404.0999v3](https://arxiv.org/pdf/1404.0999v3),
30 October 2015, Sections 1.1, 2.1 and 2.2, printed pp.1,4,5.
Section 1.1 defines the probability-measure order using nonnegative
increasing convex tests. Section 2.1 allows real integrable tests for
integrable variables. Proposition 2.3 characterizes the scalar order
by stop-loss inequalities for every real threshold; Remark 2.4 permits
rational thresholds. No coupling theorem or book proof is imported.

Applicability remains a task for the fixed calculation: prove positive
finite normalizers, finite first moments and the exact energy mean
formula before testing its sign. This approval imports the criterion,
not an actual row-law comparison. No new specialization was derived.
The book source cited by Proposition 2.3 remains unread and unnecessary
for this citation-based use.

Reused step107's scoped duplicate/failure comparison and numerical-method
coverage. Rechecked L036's C8 panel hypothesis and L037's directed
operations, widened nearest-rounded exp, rational pi and rejected
exception contracts. Their canonical proofs remain unchanged. L917's
method is supporting coverage only; its bounds do not cover M14.
The [official Decimal contract](https://docs.python.org/3/library/decimal.html)
is recorded in L037 and reused, not independently verified here.
No new numerical-method accuracy guarantee, tail bound or Mathlib
coverage is asserted.

Recovery decision: SPECIALIZE retained for exactly TARGET. Source URL
repair supplies no mathematical advance and does not renew exploration
budgets. Proceed once to the fixed calculation; no additional browsing
is needed unless its hypotheses change. All existing failure evidence
and the zero-containing-enclosure stop remain in force.
