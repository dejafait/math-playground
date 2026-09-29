# Resolved-parameter Hilbert-cube test — saved reasoning

Target at invocation: Review whether a lift from a smooth resolution of Bl_{J O_S}(S) to S^[3] can deform in the fourth RM direction when both the parameter surface and the map may vary.

The prior assessment is
[SPECIALIZE](literature/2026-10-03-resolved-parameter-hilbert-cube-deformation.md).
This is one specialization of that target, not a new source review.

## Gap and discriminating test

Seek a representative reaching an RM tangent outside V_D, allowing every
source class in H^1(B,T_B). A successful transverse first-order map would
justify later tests of action, higher orders and transverse coverage.
If every such map forces kappa in V_D, stop this resolved-lift recipe.
The attained span is still 21 on the Dickson family and its three
directions are short of the required four; the universal Hodge gap is
much larger. L009 alone is not a theorem about varying-source maps.

## Reasoning saved before completion

This outline was saved while the test was unfinished. The completed
full informal proof is now in
[L043](../lemmas/L043-resolved-parameter-lift-retains-transverse-obstruction.md).
Its result is NEGATIVE: the central lift exists, but all source
motions still give exactly V_D. The outline below records the route
used; its conditional wording describes that earlier working stage.

1. Outside the three q_i, Y=C union Delta is finite flat of degree three
   over its first factor. At its finite double curves the local algebra
   is O_S[z]/(z^2-u^2), plus the disjoint third point. Away from these
   curves the finite flat normalization and the diagonal are disjoint.
   This identifies the Hilbert family and principalizes K there.
2. At each q_i, L042 gives K=(uv,u^3,v^3)^2. Blowing up the origin gives
   (uv,u^3,v^3)=x^2(y,x) on u=x,v=xy; the symmetric chart has one more
   base point. Blow up those two points. This is three point blowups
   per q_i, and the full image ideal is then invertible.
3. For a point blowup r, the local Jacobian gives
   0 -> T_B -> r^*T_D -> O_E(1) -> 0. Its H^1-cokernel vanishes.
   Together with Rr_*O_B=O_D and Iacono's inspected map criterion,
   every source deformation extends some deformation of the blowdown
   map. Iteration allows all source motions; it does not impose a fixed
   configuration before checking the tangent condition.
4. Let mu be the degree-two universal-incidence correspondence. The
   central f^*mu on T equals p^*(1+U): the transpose of C is C, and
   any possible exceptional correction is a rational Hodge map from
   T to exceptional (1,1)-classes, hence zero. In an RM target
   deformation, (1+U)omega_A=(1+theta)omega_A. Functoriality of the
   first-order Hodge filtration would then force the blowdown source
   period to equal the target period. Infinitesimal K3 Torelli would
   identify their Kodaira--Spencer classes.
5. After that identification, the deformed universal family gives an
   embedded flat Y lift away from the exceptional parameter points.
   L009's diagonal vector-field and residual arguments operate there;
   Hartogs for N_C then fills the omitted isolated points. This would
   force kappa in V_D even with source motion allowed.

The completed proof supplies the point-blowup cohomology argument,
the incidence transpose check and exceptional-correction argument,
the first-order period comparison, and the punctured residual
extension. It never asserts flatness of the image at the exceptional
points. The current checkpoint schedules an independent literature
audit of the all-source blowdown and period passages; that audit
was not performed as a second step here.

## Mathlib

Coverage: **not checked** for this test or its supporting map-deformation,
point-blowup and infinitesimal Hodge inputs. The inspected Iacono
Theorem 5.5 and Remark 5.12 equation (7), linked in the prior assessment,
cover the map criterion, not the proposed fourth-direction conclusion.
