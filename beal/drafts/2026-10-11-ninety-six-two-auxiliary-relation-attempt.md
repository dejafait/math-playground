# Two-auxiliary relation test — working reasoning

Approved target: Test whether L96 admits a generalized norm relation using only K96 and F=Q(T), retaining all conjugate composita.

Main gap: unconditional 96a1 branch emptiness in L032, with other twists and residual signatures independent. This test concerns only algebraic applicability, not class arithmetic.

Inputs being checked: L050's complete twelve-line Galois-set interpretation; L051's exact field models and degree 36; L052's audited index eleven; L054's cubic-base degree. Reuse Etienne v2 Proposition 2.7 and Algorithm 4.1/Theorem 4.2 from the approved SPECIALIZE assessment. Existing ATTEMPTS/020-021 concern normality, not this target.

Proposed bounded mechanism: identify the joint permutation action from the projective mod-eleven action, its order-eleven inertia, and the cubic discriminant. Then compute every orbital map from each auxiliary permutation module to the 36-point product module. This avoids selected-compositum traces and retains arbitrary map multiplicities.

Unfinished obligations: certify the projective action is PGL2(F11), rather than guess it; certify the intersection of the two splitting fields; enumerate all orbital maps and compare their actual rank with 36. No group identification, relation existence/nonexistence, or rank has yet been established. In particular the tempting primitive-generator additive identity is not the permutation criterion.

Continuation test: full rank 36 justifies further arithmetic review; a certified missing constituent or complete-map rank below 36 parks only this auxiliary pair. If group or compositum coverage is uncertified, retain an unfinished test and do not claim a negative result.

Independent unresolved inputs: unconditional auxiliary class/unit arithmetic, integral transfer and saturation, torsion lifts, prime support/norm maps, descent compatibility, and full-disk disjointness. No GRH or branch exclusion is assumed.

Completed result: the working obligations above are resolved in
[L055](../lemmas/L055-ninety-six-two-auxiliary-relation-obstruction.md).
The actual joint group has order 3960. Every compositum is retained,
with relative degrees [1,11] and [1,2]. The full image rank is 14
against required rank 36, with a nonzero annihilator and no failed
finite checks. This is an informative negative result for this pair;
independent critical review remains pending. The earlier working
paragraphs preserve the saved pre-calculation reasoning.
