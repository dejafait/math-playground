# Step520 — finite-level unit-image test

Gate: reuse the invocation-start SPECIALIZE assessment `drafts/literature/2026-10-27-variable-norm-finite-level-unit-image.md`, without changing its target or hypotheses. Completed task is an ordinary known-method specialization, not creative work or a claim of originality.

Main gap: native-pilot membership and finite B>=A. Intermediate target: decide preservation of the actual unramified cubic unit image by L125's F_{Q_3}. Downstream use: necessary same-index lattice condition in the ordinary realization of IUT II Definition 4.9(i). Continue this use only on containment; abandon this same-index use on a rigorously excluded representative. Neither verdict resolves the main gap.

Saved reasoning: Kedlaya Proposition 4.2.5 gives u in O_E^times with N_{E/Q_3}(u)=4. L125 gives F_{Q_3}([u])=[4]^(1/3). If [w] were this output for an E-unit w, then t=w^3/4 is a root of unity lying in E. Every E-root of unity has order dividing 26: reduction has order dividing |F_27^times|=26 and its kernel 1+3O_E is torsion-free by the covered logarithm isomorphism (depth 1>1/(3-1)). Thus w^78=4^26. But w^26 lies in 1+3O_E by reduction; its cube is 1 modulo 9O_E, whereas 4^26=7 modulo 9. The residue 6 has valuation 1, not at least 2. This excludes every E-representative, including torsion changes originating outside E.

Completed: the full proof and precise source qualifications are canonical in [L126](../lemmas/L126-variable-norm-fails-unramified-cubic-unit-image.md). No mathematical script was needed. The result is a local obstruction to the proposed map, not an original-hypothesis IUT counterexample. Separate critical audit remains necessary before relying on it downstream; its newly proposed assessment is REVIEW_REQUIRED.
