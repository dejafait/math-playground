# L876 fixed coefficient exclusion — independent audit scope

TARGET: Independently audit L876's fixed primitive-K Hankel-square exclusion, including the whole-half-line interval certificate and implementation, and verify or correct the strict residual bound 0.00021317<c^2 Tr(A^2)-S_2<0.00050451 without changing the ansatz.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact fixed-ansatz search/duplicate comparison in 2026-11-06-post-bracket-interface-discovery.md and separate step23 approval in 2026-11-06-primitive-theta-hankel-square-test.md. The target changes from production to independent audit of the same exclusion; no new operator, theorem hypothesis or replacement identity is proposed. Local filename search found no prior L876 audit assessment.
SOURCE_EVIDENCE: Reuse inspected Bothner2205.15007v2 Section2.1 (10)-(13), https://arxiv.org/pdf/2205.15007v2#page=5; Bornemann0804.2543v2 Section2 pp6-8 and Section3 (3.1)-(3.3), https://arxiv.org/pdf/0804.2543v2#page=7 and https://arxiv.org/pdf/0804.2543v2#page=10. Exact versions, weighted-factor hypotheses, product theorem and local Plemelj cases were separately checked in step23; source scope is unchanged.
COMPARISON: Known operator/determinant theory covers the framework, not L876's actual-theta integrals or implementation. Audit adjoint, trace-class and local-logarithm specializations and every certificate bound; a proof assertion, replay exit code or rigor flag alone is insufficient. No inspected theorem supplies the specific residual enclosure.
GAP: L876 remains unaudited. Interval directions, elementary function enclosures, omitted theta terms, cell integration, half-line tails, trace bounds and coefficient normalizations remain obligations. No replacement mechanism or Xi positivity is asserted.
REASON: Independently verify a relevant exclusion before using it to guide central-gap discovery; do not reopen its coefficients or fit a replacement. This is an audit of potentially new local evidence, not an originality claim or new sign theorem.
SCOPE: Exactly the existing unweighted unshifted primitive-K operator and one scalar c; one conceptual audit with meaningful replay after proof/code inspection. No higher traces, repairs of the ansatz or determinant identification. Newly ready continuation requires separate approval next turn.

The main gap remains L030-L032/C032a. The intermediate audit target is
the claimed nonzero second-coefficient residual. Its downstream use is
a trustworthy exclusion of one arithmetic-to-logarithm bridge, not RH.
A certified strict residual retains the stop; a proof, implementation or
enclosure defect requires correction or honest unresolved status. An
interval meeting zero is inconclusive. No outcome authorizes a sweep.

Essential input IDs: L019/L021/L025 and the result under review L876.
Consult L016/L024 only if inherited series/product justifications need
their exact proof ranges, resolving them narrowly through the DAG.
L030-L032/C032a are downstream only. No real-zero, determinant-equality,
mixed-sign or cross-notebook assumption is allowed.

Read complete L876 and scripts/primitive-hankel/coefficient-test-24.py.
Inspect complete relevant values of its coefficient-test-24.json using
the shared JSON inspector. A preview or the explicitly nonrigorous
diagnostic JSON cannot verify the result. Any replay writes separate
audit evidence, preserving original artifacts.

Check weighted Hilbert-Schmidt integrability, real adjoint, trace-square
bounds from J and T, positive denominators and local Plemelj radius;
the exact K and all omitted series/tails; monotone cell enclosures;
rational pi/exponential errors and every rounding direction; final
factorials and sign. These are future audit questions, not claims
verified by this source-only nomination. Import known operator theory
without reproof; justify its application and any real repair.

Preserve failures and unfinished reasoning. If successful, record the
audit in canonical L876 and concise history, changing DAG/PROOF only if
the argument changes. Mathlib matching/supporting coverage remains
unchecked, with no absence claim. Recommend conceptual_audit,
deep_research/xhigh for the delicate link between whole-domain analytic
inequalities and outward-rounded executable evidence. This is not creative.
