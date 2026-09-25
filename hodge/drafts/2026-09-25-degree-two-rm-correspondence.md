# Degree-two correspondences in the real-multiplication family

Date: 2026-09-25. Saved working assessment for one focused step; PROGRESS.md is the sole current checkpoint.

## Gap, intermediate target, and discriminating test

The general gap is algebraicity of arbitrary primitive rational (2,2)-classes on fourfolds. On K3 self-products the proposed intermediate target is algebraic realization of the full transcendental endomorphism field in the real-multiplication family of van Geemen–Schütt, Proposition 6.2. Its very general member has E = Q(sqrt(2)), so the required image has dimension two. Test whether the degree-two rational self-map and the diagonal give two independent actions. If so, the residual class in this family is algebraic; arbitrary K3 surfaces, fourfolds, and higher codimensions remain outside the conclusion. If the action is scalar, or the map cannot be defined on the claimed model, abandon this particular construction as a source of the missing direction.

## Redundancy and prior failures

Read and preserved the existing changes, shared and local rules, whole PROOF.md and DAG.md, L003, L004, and Attempts 001–003. L003 supplies the correspondence threshold only for quartics; its extension to the present smooth projective K3 models must be justified. L004 stops isometry spanning, including closed isometry chains, but does not stop degree-two maps, whose action can scale the pairing. This family construction was proposed but not carried out in the previous assessment. The Clay/Deligne rational target was rechecked on 2026-09-25.

## Source audit and reasoning at the initial save

Primary source: Bert van Geemen and Matthias Schütt, *On families of K3 surfaces with real multiplication*, Forum of Mathematics, Sigma 13 (2025), e2, [Proposition 6.2 and section 6.4, pp. 18–19](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26D90B781A518CB95969B4473C8852C8/S2050509424001464a.pdf/on-families-of-k3-surfaces-with-real-multiplication.pdf#page=18). The introduction defines the field of a family to mean the full endomorphism field of a very general member. No claim for every specialization is licensed.

Use a(t) = t alpha(t^2), b(t) = a(t)^2/2 + t beta(t^2), with deg(alpha) <= 1 and deg(beta) <= 3. Then a(-t) = -a(t), b(-t) = a(t)^2-b(t). On y^2 = x(x^2+2ax+b), the isogeny coordinates are u = x+2a+b/x and v = y(1-b/x^2), with v^2 = u(u^2-4au+4(a^2-b)). The displayed scaling in section 6.4 is (u,v,t) -> (2u,2sqrt(2)v,-t) in the direction X' -> X. Direct coefficient comparison instead suggests the inverse scaling (u/2,v/(2sqrt(2)),-t). This needs an exact substitution check rather than uncritical import of the display.

With the inverse scaling, the expected pullback on dx wedge dt/y is -sqrt(2). Remaining proof obligations: verify the rational map and its degree, give its graph/transpose convention on a resolution, prove its action preserves T, use the full-field hypothesis to deduce that its square is 2 id, and justify the residual exact sequence for a nonquartic K3. The degree-scaling identity must only be asserted on T, after checking that resolution exceptions contribute no transcendental part. No completed result is asserted at this save point.

## Completed result and assessment

The proof obligations above are now discharged in [L005](../lemmas/L005-degree-two-rm-correspondence.md). The [family input](../foundations/04-degree-two-rm-family.md) isolates the precise published result being used. This is a known geometric construction assembled into a restricted cycle-spanning proof; no novelty is claimed.

Direct substitution confirms the inverse scaling and shows that the published display works in the reverse direction. The exact coefficient test `python3 scripts/rm-degree-two/check_normalization.py` gives zero residual for the corrected map and residual -24 a u^2 + 30(a^2-b)u for the display in its stated direction. The degree is exactly two, proved by the quadratic equation for x together with the nontrivial involution fixing u and v. These are exact algebraic arguments, not parameter sampling.

The resolution calculation shows that the pullback of T has no exceptional part, so the transposed graph acts by U with q(Ur,Us) = 2q(r,s). The action -sqrt(2) on the holomorphic line and faithfulness of the full endomorphism field imply U^2 = 2 id. The ordinary graph acts by 2 U^(-1) = U on T as well. Identity and U therefore span the full quadratic field. The extension of L003's residual argument to a projective K3 uses h^2 = m e with m > 0 in place of the quartic value 4, with every other geometric input checked.

The achieved transcendental dimension is exactly the required two, and the entire rational (2,2)-space has dimension 104 = 10^2+2+2. The new graph increases the previous divisor-plus-diagonal dimension 103 by one, filling this family's gap. The explicit span proves algebraicity of every such class on a very general S x S in this family. It does not justify the same full-field assertion at all special parameters, or for arbitrary K3 self-products, general fourfolds, or higher dimensions.

Outcome: ADVANCE, a relevant algebraic-realization input and a checked coordinate repair. Exploration turns used: 0 after this mathematical advance. The test passes for its stated family; the scalar-only isometry route remains stopped. The reason for the subsequent direction is to test whether a different concrete correspondence can realize a field of degree greater than two. The same paper's section 4.8 points to dihedral-cover correspondences and section 5.3 to a cubic RM family. That construction was not investigated in this step. The universal gap remains open, and no complete candidate argument was produced.
