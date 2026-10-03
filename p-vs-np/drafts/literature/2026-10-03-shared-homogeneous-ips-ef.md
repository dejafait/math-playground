# Shared homogeneous components: assessment required

TARGET: Test whether shared homogeneous-component circuits yield a polynomial EF/ER simulation of arbitrary-degree balanced F₂ noncommutative formula-IPS certificates for 3CNFs.
CHECKED: 2026-10-03
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: No target-specific source search has been performed for this changed degree and representation hypothesis; reuse the prior formula-IPS assessment only as background.
SOURCE_EVIDENCE: The prior source note records Li–Tzameret–Wang, https://arxiv.org/pdf/1412.8746v4, Theorem 1.7 with its degree/depth note, Theorem 4.1 and Theorem 4.11; those inspected formula statements do not screen the proposed shared-circuit replacement.
COMPARISON: L016 applies the known logarithmic-degree formula simulation; the checked general-degree statement has quasipolynomial Frege overhead. Whether EF sharing removes that overhead while preserving provable identity witnesses has not been compared at theorem level.
GAP: Determine the strongest known EF simulation for these certificates and whether shared homogeneous components retain the required identity-witness/proof construction with one polynomial total binary bound; do not infer this from external PIT or the formula theorem.
REASON: This changes the screened logarithmic-degree hypothesis and introduces shared representations inside the simulation. A separate source review is required before calculations; the new target is not approved by the prior SPECIALIZE scope.

This is a pending assessment created after the completed L016 application, not a literature step or an executed mathematical test of the new target. The [prior assessment](2026-10-03-noncommutative-ips-er-simulation.md) and [source note](../2026-10-03-noncommutative-ips-source-notes.md) are adequate for that completed application and remain unchanged.

The proposed continuation concerns an upper-bound screen for prospective ER-hard CNFs. A polynomial simulation for a larger algebraic fragment would show that polynomial certificates in that fragment still supply short ER proofs. It would leave certificate lower bounds, exclusion of all EF/ER proofs and the decision-hardness transfer unresolved. There is no assumption that this proposed simulation is true or new.

The next source comparison must distinguish sharing in a propositional EF proof from replacing a formula zero-identity input by an arithmetic circuit. It must check the applicability of the homogeneous identity-witness theorem to that representation and to the substituted clause/Boolean/commutator identities. A known theorem meeting the exact full-binary bound should be imported; retained PIT-proof premises or a larger bound must be recorded. No stronger simulation, obstruction or auxiliary homogeneous-component lemma is derived here.

## Mathlib

Coverage: **not checked** for the new target. The existing direct source link is a background lead, not a full match or an absence claim. No essential source for the completed L016 specialization is being reopened.
