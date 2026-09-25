# Totally real multiplication: scope of the isometry mechanism

Date: 2026-09-25. Saved assessment for one focused step; PROGRESS.md remains the current checkpoint.

## Gap, intermediate target, and test

The first general gap is algebraicity of arbitrary primitive rational (2,2)-classes on fourfolds. On a quartic self-product, L003 makes the required threshold explicit: all of E = End_Hdg(T(S)) must occur as algebraic correspondence actions. This step tests the Q-span of rational Hodge isometries when E is a totally real field of degree d > 1. Buskin's theorem supplies algebraic cycles for isometries of the full second cohomology, so a spanning result would turn an established construction into surjectivity on this restricted family. Extending to arbitrary fourfolds and higher dimensions would remain unresolved.

The discriminating test is dimension 1 versus d: if all rational Hodge self-isometries are scalar, the mechanism adds nothing to the diagonal on T(S). If their span is E, continue the algebraic-realization route. Also check whether composing such isometries through other projective K3 surfaces enlarges the self-action span.

## Redundancy and source checks

The existing changes, whole PROOF.md, DAG.md, L003, C003a, and both failed-generator attempts were read and preserved. L003 already proves the exact correspondence threshold but does not compute the real-multiplication isometry span. The CM consequence is already in Buskin's paper and the preceding assessment; it is not the target of this step.

The Clay page and Deligne's official rational formulation were rechecked. Buskin, Theorem 1.1, [arXiv v3, p. 2](https://arxiv.org/pdf/1510.02852v3#page=2), requires a rational Hodge isometry of full H^2. Huybrechts, *Lectures on K3 Surfaces*, [Chapter 3, p. 59 in the author's draft](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=59), already records that the totally real case has only the two scalar Hodge isometries. This will be a notebook-level scope test of a known fact, with a local proof and the precise comparison to L003, not a novelty claim.

## Saved reasoning and completed checks

For a nonzero holomorphic two-form omega, the action gives a unital field embedding sigma: E -> C. Total reality puts its image in R. A rational Hodge isometry u preserves q(omega, conjugate(omega)), which is nonzero, so sigma(u)^2 = 1. Injectivity then gives u = +id or -id. This proves the core claim without importing a classification of all endomorphism fields.

The proof obligations were the nonzero pairing by the perfect Hodge-type pairing, restriction of full H^2 isometries to T and extension by id on N, the exact generated correspondence space using L003, and the closed-composition check. They are now written out in [L004](../lemmas/L004-totally-real-isometry-span.md). The hypothesis is that the *full* endomorphism field is totally real, not merely that it contains a real subfield. No existence assertion for a particular quartic and no nonalgebraicity claim follow from this conditional calculation.

## Result and threshold comparison

The transcendental span has dimension 1 rather than d. The entire tested cycle span, including closed chains through other projective K3 surfaces, has dimension rho^2 + 3, compared with the required rho^2 + 2 + d. Thus for d > 1 this construction reaches none of the residual directions identified in L003. It still suffices for d = 1. This is an informative NEGATIVE for the proposed real-multiplication extension of the isometry mechanism; [Attempt 003](../ATTEMPTS/003-totally-real-isometry-generation.md) records its precise stop. The result does not deny the existence of nonisometric algebraic cycles realizing the missing directions. Exploration turns used: 0 after this new informative negative result.

## Reason for a different geometric direction

Bert van Geemen and Matthias Schütt, *On families of K3 surfaces with real multiplication*, Forum of Mathematics, Sigma 13 (2025), e2, [Proposition 6.2, Remark 6.3, and section 6.4](https://doi.org/10.1017/fms.2024.146), provide a specific candidate source: the real-multiplication family with field Q(sqrt(2)) has degree-two rational self-maps. The statements and the paper's convention that the named field is the full endomorphism field of a very general member were checked. Their self-map construction and its induced action are reserved for a separate step, not asserted here as a locally verified cycle-spanning proof.

Such a graph could supply a non-scalar Hodge endomorphism without being an isometry, directly addressing the limitation just found. The concrete test is whether its action and the identity span the two-dimensional field for a very general member. Handling the rational map on a smooth model and applying the correspondence calculation to these projective K3 surfaces, not assumed to be quartics, require checking. Even a successful family calculation would leave arbitrary real-multiplication K3 surfaces, arbitrary fourfolds, and higher dimensions unresolved. This is a change of geometric mechanism, not a reopening of the scalar-only isometry span by renaming it.
