# Mixed seventh-power conditional q=29 parameter-bridge assessment

TARGET: Critically audit Chocian's Section 6.2 claim that an exceptional descent field forces eta modulo 29 into {10,14,24,28}, conditional on a primitive signed solution of X^5+Y^3=Z^7 and A_eta being that field.
CHECKED: 2026-10-04
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: The parent mixed-signature assessment locates this candidate, but the exact parameter/branch statement has not received a theorem-level comparison or a dedicated search. No new search was performed while completing the character audit.
SOURCE_EVIDENCE: Chocian arXiv:2609.26996v1 Section 6.2, between equations (37) and (38), https://arxiv.org/html/2609.26996v1#S6.SS2 , was already read and states the four ordinary residues and three scaled branch patterns. Those claims are not yet independently reproduced; the original global descent and the V4 modular archive remain parked.
COMPARISON: The printed source claims exactly the conditional four-parameter restriction. L016 verifies the curves' arithmetic and L017 verifies conditional reducible characters; neither proves this solution/field-to-parameter implication. General Hensel and Newton-polygon inputs need their exact scope compared before an audit is approved.
GAP: Assess coverage of every ordinary and branch residue at 29, retaining primitivity, signed nonzero and base-one coordinates, the field-isomorphism hypothesis and local factor-type transport. A residue enumeration without the branch/interface proof would not suffice.
REASON: The target changes from an abstract conditional Galois representation to an integer solution and specified descent field, outside the saved character assessment. Screen this independent local-algebra bridge rather than retry either persistent source blocker or infer it from terminal trace arithmetic.
SCOPE: Pending review only. No new source comparison, polynomial enumeration, local-algebra proof or parameter exclusion has been executed for this target.

## Intended conditional scope and relevance

Use Phi(T)=15T^7-35T^6+21T^5, eta=X^5/Z^7, and A_eta=Q[T]/(Phi(T)-eta). The proposed field assumption is that A_eta is isomorphic to Q[T]/(T^7-483T^2+3955T-3945). These are explicit hypotheses for the new target; no claim that every original solution meets the field assumption is proposed. In the source the specified prime over 29 has sqrt(5)=11. Its corresponding t0=eta/(eta-1) conversion would connect the four eta values to L016, only after local applicability is justified.

The main target remains zero primitive solutions uniformly over the residual signatures. The possible downstream use is to supply the missing four-parameter quantifier in the exceptional-field comparison. The actual threshold is a proof for every eligible solution, including 29 dividing any one coordinate, rather than a finite list of ordinary specializations.

The source's exact statement and all needed local-algebra inputs must be compared in a separate literature turn. If coverage is adequate, approve the full conditional statement and explicitly list any useful subtargets; reuse that coverage for later mathematical work. The character audit does not approve this changed target. Persistent global-descent and archive access failures should remain parked, since the conditional statement is designed not to need their applicability conclusions.

## Mathlib

Coverage of the full conditional parameter restriction and supporting local-algebra/Hensel results: **not checked**. The printed candidate is a lead, not an imported theorem or formal proof.
