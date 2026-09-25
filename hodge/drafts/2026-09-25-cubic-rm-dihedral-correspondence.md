# 2026-09-25 — Cubic RM dihedral-correspondence test

## Scope and discriminating target

The universal gap remains algebraic realization of primitive rational (2,2)-classes on arbitrary fourfolds, followed by the higher-dimensional cases. The focused intermediate target is full algebraic realization of the transcendental endomorphism field for the very general cubic RM family of van Geemen–Schütt, sections 5.3–5.4. The downstream use is the residual cycle-class criterion of L003, with its projective K3 extension checked in L005. This is a restricted family result, not a proposed reduction of arbitrary fourfolds to K3 self-products.

The required transcendental dimension is three. Test whether the descended dihedral correspondence has minimal polynomial z^3+z^2-2z-1, so its action, its composition square, and the identity span the full field. With rho = 4, success means the full rational (2,2)-dimension 4^2+2+3 = 21, compared with 19 for divisor products and the diagonal. A scalar action, failure of algebraic descent, or lack of a justified full-field hypothesis would prevent this conclusion.

## Redundancy and source check

Read the required shared/local guidance, whole overview, DAG, local changes, L003–L005, and Attempts 001–003. Preserve all existing work. L004's scalar-only isometry obstruction does not apply to a push-pull correspondence through a dihedral cover. L005 supplies a quadratic field only; the cubic construction has not been carried out in this notebook. The Clay primary page and the published van Geemen–Schütt paper were opened on 2026-09-25. The exact rational target agrees with the existing primary-source audit.

Source: Bert van Geemen and Matthias Schütt, *On families of K3 surfaces with real multiplication*, Forum of Mathematics, Sigma 13 (2025), e2, [sections 4.6–4.8 and 5.3–5.4](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=12). Theorem 1.2(7) supplies rho = 4 and equality with the full field for the very general member. Section 4.8 already supplies a known algebraic construction; the step audits its descent normalization and completes the local spanning calculation, with no novelty claim.

## Unfinished reasoning saved before detailed verification

Write P(t) = t^7-7a t^5+14a^2 t^3-7a^3 t, with a nonzero. The family has chart y^2 = x^3+(b_1 P(t)+b_0)x+(c_1 P(t)+c_0). On the cover t = v+a/v, P(t) = v^7+(a/v)^7. Rotation v -> zeta_7 v and reflection v -> a/v preserve the resulting equation.

Let p denote the degree-two map from a smooth cover model to S. The source's rotation-graph sum acts upstairs by sigma^*+(sigma^(-1))^*. Its pushforward under p x p requires a factor 1/2 to give that action downstairs, since p_*p^* = 2. A single pushed rotation graph may already give the same normalized action. This must be proved with the graph convention and rational-map resolutions, not assumed.

The pullback of dx wedge dt/y is (1-a/v^2) dx wedge dv/y. Adding its two rotation pullbacks gives (zeta_7+zeta_7^(-1)) times this form. Remaining obligations: justify a smooth equivariant model and push-pull on forms; check the factor of two; promote the holomorphic-line calculation to the full transcendental action using the stated full field; distinguish correspondence composition from cup-product squaring; and verify the residual sequence for this nonquartic K3 model. No completed result is asserted at this save point.

## Completed result and critical assessment

[L006](../lemmas/L006-cubic-rm-dihedral-correspondence.md) supplies the complete restricted proof from the [published family input](../foundations/05-cubic-rm-family.md). Both the Clay page and Deligne's rational formulation were rechecked. The exact identities are reproducible with `python3 scripts/rm-cubic/check_correspondence.py`.

The final construction avoids needing an equivariant resolution: resolve the three rational maps with t_j = zeta^j v+zeta^(-j)a/v for j = 0, 1, -1, obtaining morphisms g_j from one smooth projective W. Define C_j = (g_0,g_j)_*[W] and Z = (C_1+C_(-1))/2. Pushforward includes multiplicities, so the action is exactly (g_j)_*g_0^*. The top-form trace is checked on the finite etale locus and extends globally. It does not assume a transfer identity on all second cohomology of a singular quotient. No assertion that W is a K3 is needed.

Each C_j acts on the holomorphic line by theta = zeta+zeta^(-1), whereas their unnormalized sum acts by 2 theta. The faithful full-field action promotes the irreducible cubic relation to all of T. Rational independence of id, U, U^2 and the degree-three full-field hypothesis give the entire required endomorphism space. The action of the Chow composition Z^(circ 2) is U^2; a cup square would have the wrong codimension. The residual calculation is justified for the present projective K3 rather than assuming it is quartic. Only an endomorphism relation, not a Chow relation, is proved.

The achieved dimension is exactly 21, against 19 for divisor products and the diagonal and 20 after adjoining only Z. Thus the chosen family gap closes. The result uses a known construction, makes no novelty claim, and supplies no universal Hodge candidate. Mathlib coverage is not checked. The only new DAG row is L006's use of L003's residual argument; the earlier isometry obstruction and quadratic construction provide contrasts, not additional mathematical inputs.

Outcome: ADVANCE. Exploration turns used: 0 after this relevant mathematical input. Continue beyond the explicit family rather than enumerate further cyclotomic examples. The reason is a specific remaining scope gap: [sections 5.3–5.4 of the same paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=15) place this three-dimensional construction in a four-dimensional RM deformation space. Algebraic deformation of the cycle in its missing direction remains unproved; preservation of its Hodge type alone cannot be substituted for that step. That deformation question has not been investigated in this step.
