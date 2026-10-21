# Pair-plus-recursive-theta reduction — source-ready continuation

TARGET: Establish a sound core-conditioned pair-plus-recursive-theta upper-bound reduction and its exact local threshold test for 68-agreement support families.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the bounded core-conditioned comparison in 2026-10-06-core-conditioned-determinant-transfer.md, including recursive theta with packing/forbidden-intersection searches and the targeted local duplicate/failure check; no matching RS core-transfer theorem was inspected.
SOURCE_EVIDENCE: https://link.springer.com/content/pdf/10.1007/s00493-023-00040-9.pdf — Castro-Silva et al., Combinatorica 43 (2023), 909–938, equation (2), Definition 1.1, Theorem 2.1 with full proof and Corollary 2.3; exact statements and qualifications are in foundations/07-core-conditioned-theta-source.md. L001, C001a and L020 were read in their relevant full proof passages.
COMPARISON: The source covers independent-set lifts for finite uniform hypergraphs with unit vertex weights. It does not state a shared-lift combination with pair conflicts, selected RS tuple support applicability or summation over 61-cores; only those differences and the necessary finite strength test are approved for specialization.
GAP: Prove joint-lift soundness, handle zero diagonal and empty links, preserve labeled singular triples, and derive exact core-incidence normalization and the required local cap. An improved cap and tractable certificate remain independent unresolved work.
REASON: A bounded applicability-and-counting proof can establish a usable finite certificate specification without generic labels or uniform induced measure; optimization is premature until the reduction is sound.
SCOPE: C001a's n=1024,k=64,H<=F_65537^*,F=F_(65537^28), all m>=1; selected size-68 supports with extra agreements permitted; source specialization and exact counting only, with no SDP implementation, eigenvalue calculation or asserted optimum.

LITERATURE_REASON: Supervisor recovery identified a missing direct source URL in this ready assessment; this bounded review repairs that field and verifies the same primary passages without broadening the target.

## Proposed construction and obligations

For each 61-subset C of H use vertices A in the 7-layer of H\C.
The proposed pair-conflict graph joins distinct vertices with
|A intersect B|>=3. The proposed 3-uniform hypergraph has an edge
exactly when the residual supports have empty triple intersection,
all three pair intersections have size two, and L020's matrix for those
pair-only points is nonsingular. Include no determinant-zero triple as
an edge. These are model specifications, not proved applications.

Test the model whose lift F simultaneously obeys the source's graph
edge-zero equations, recursive hypergraph row constraints and R(F)>=0,
with objective sum diag(F). Explicit 3-subset packing clique rows must
be justified if included. Use the same lifted matrix throughout;
intersecting projected theta bodies is a different relaxation. A feasible
lift is not an actual support family or a received-word/list realization.

The proof must establish that choosing one 68-support for each candidate
produces distinct supports and legitimate local independent families for
every m, using L001 and L020. Import the source's indicator-lift argument
without re-proving its recursive theorem. Check empty links and f(A)=0
without division. Count support/core incidences exactly, allowing local
caps to depend on C; do not assume one core represents all others.
State a uniform cap as a sufficient alternative only after that proof.

Compute the exact cap required to certify
B_m(956/1024)<=T=65537^28/2^128 and compare with the ordinary 3-subset
packing cap on the 7-layer. Retain an exact integer comparison, rather
than an approximate ratio. This tests the strength required of future
certificates; it does not assert an improved numerical cap.

## Downstream use and stopping test

A sound reduction and concrete local strength requirement would give
later labeled certificates a defined test against the global threshold.
Continue only if every actual family has a shared lift and the incidence
transfer has explicit multiplicities. Reject a formulation needing generic
points, exclusion of allowed antipodal triples, zero-diagonal division,
transitivity or a lost core multiplicity. If soundness holds but no improved
cap is established, report only the reduction and quantitative gap.

Essential inputs: L001, C001a, L020 and foundations/07-core-conditioned-theta-source.md.
Preserve ATTEMPTS/010 and L021–L026; their stops do not decide this labeled
model. Exact local optima, sufficient improved cap, list realization,
full strengthened-SDP feasibility, exponent m, sharpness, 67-agreement
safety and ABF equivalence remain open. Matching Mathlib coverage is not
checked. Classification for the next specialization: REPRODUCTION.
The separate source-review recovery on 2026-10-06 verified the direct PDF
URL and retained this SPECIALIZE scope. No dependent mathematics was
performed in either source-review turn. The next invocation may attempt
the exact saved target subject to the supervisor gate.


## 2026-10-06 — Direct-source recovery review

Retrieved the final publisher PDF directly at the URL in SOURCE_EVIDENCE.
Rechecked equation (2), printed p. 911; Definition 1.1, p. 912;
Theorem 2.1 and its complete proof, pp. 915–916; and Corollary 2.3
and its proof, p. 917. The finite-uniform-hypergraph hypotheses,
r=1 base, indicator lift and empty-link convention agree with the
canonical source note. The definition retains scaled row membership;
it does not authorize dividing by a zero diagonal. No new source
comparison changes the existing decision.

Reused the prior bounded search and local-input reading recorded in
2026-10-06-core-conditioned-determinant-transfer.md. A targeted check
of ATTEMPTS/010, history/056 and the earlier global extremal assessment
retains the antipodal obstruction and confirms that the current checkpoint
still has no proved joint model or local cap. No repeat general search
was needed because the target and assumptions are unchanged. This is
a process repair, not a new theorem or an informative mathematical
negative. All proposed obligations and stopping tests above remain.
