# 2026-09-25 — Testing the length-two fibre thickening

## Gap, intermediate target, and decision test

The immediate gap is a representative of the cubic RM generator U that extends in the fourth NS-fixed RM tangent direction. Test exactly the checkpoint's scheme Y_2 = C union B_2, where B_2 is the inverse image of the length-two point on the base conic at (t_+,t_+). Its fundamental cycle is [C]+2[B], so it retains the action U. A four-dimensional first-order kernel would justify higher-order lifting and algebraization work; those steps, arbitrary K3 self-products, and the universal Hodge target would still be unresolved. A forced flat residual C would instead stop this representative, leaving the kernel at the known three dimensions.

Read the shared rules and prompt, the local goal and checkpoint, the whole overview and DAG, existing changes, the needed preceding proofs, and the reduced fibre-product failure. All pre-existing changes and inactive branches are preserved. The rational target was rechecked against Clay's linked Deligne statement. The proposed change is genuinely nonreduced; L010 does not already assert its obstruction calculation. No local smoothing is being identified with a global lift.

## Reasoning saved before completing the test

Use base coordinates s,r near the conic point, with conic s=0 and the length-two point (s,r^2). Near the diagonal elliptic curve D, local ideals are I_C=(s,z), I_B2=(s,r^2), I_Y2=(s,r^2 z). The intersection D_2=C intersect B_2 is an effective Cartier divisor of B_2, reducing to D. The normal module of B_2 is O_B2 direct sum O_B2, from the globally defined base equations s,r^2 near its support.

A reference B_2 lift is obtained by extending the elliptic pencil and pulling back the fixed length-two base scheme. On B_2 minus D, the difference between that reference and a hypothetical Y_2 lift is a normal section. The local ideal suggests its components are alpha modulo I_B2 and beta/z modulo I_B2, so the allowed pole along D_2 is still simple, despite the exponent two on r.

The square-zero filtration 0 -> r O_B2 -> O_B2 -> O_B -> 0 has r O_B2 isomorphic to O_B. Tensoring with O_B2(D_2) gives successive quotients O_B(D). Since H^0(B,O_B(D))=H^0(B,O_B), reduction followed by subtraction of a constant suggests H^0(B_2,O_B2(D_2))=H^0(B_2,O_B2). This would extend every normal displacement regularly, without selecting a reduced B branch.

Outstanding checks: justify that D_2 is Cartier globally, the pole bound for the nonreduced deformation torsor, scheme-theoretic containment using a non-zero-divisor rather than reduced density, and flatness of the residual when the thickening itself may deform as r^2=epsilon b. The prospective colon argument writes a contained pair as K=(S,R), J=(S',R Z) with S'=S+epsilon qR; then J:K=(S',Z). It must not assume that every deformation of r^2 can be flattened to r^2. The reverse kernel inclusion requires a flat relative union along the Dickson family. No final outcome is asserted at this checkpoint.

## Completed assessment

[L011](../lemmas/L011-length-two-union-retains-cubic-obstruction.md) completes the test. The nilpotent filtration proves H^0(B_2,O_B2(D_2))=H^0(B_2,O_B2)=C direct sum C r. Thus there are four regular normal parameters but no extra polar ones. Every putative union lift contains a lift of B_2 given by a finite flat quadratic base scheme, potentially with r^2=epsilon(b_0+b_1r). Containment is proved by injective localization along the Cartier divisor, not by density on a reduced component. The explicit residual ideal is flat without requiring the quadratic base deformation to be trivial. Conversely, the Dickson family supplies flat unions, including their nonreduced intersections.

The obstruction kernel is exactly V_D, of dimension three versus four required. Outcome: NEGATIVE; exploration turns used are 0 after this new informative result. The result changes the decision on the checkpoint's previously untested thickening and is recorded in [Attempt 008](../ATTEMPTS/008-length-two-fibre-thickening.md). Multiplicity in r did not enlarge the allowed pole order in the separate coordinate z. The achieved 21-dimensional Hodge span is still confined to the known family, and no complete candidate has appeared.

This completes the specified test. A different representation of the class through a vector bundle is a reasoned next direction: forgetting the maps in a locally free resolution need not preserve the obstructed embedded support. Whether its Atiyah obstruction vanishes is an open test, not a consequence of the Hodge condition. No bundle-lifting calculation was performed in this step. Higher-order deformation, algebraization, and realization of all required classes would remain necessary after any first-order success.

The proof was checked at its two potential collapse points: a nonreduced scheme cannot use reduced-density reasoning, and a lift of r^2 cannot in general be flattened by ambient coordinates. The Cartier non-zero-divisor and regular-sequence cancellation arguments handle these separately. The reverse inclusion uses flatness of D_2 in the relative union sequence. These are symbolic mathematical checks; no numerical or symbolic sampling is needed to establish them. The current rational target was checked in [Deligne, section 1, p. 2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2).

## Mathlib

Coverage of the proposed full lifting statement: **not checked**. The supporting genus-one Riemann–Roch reference is [Stacks Project, Lemma 53.5.2, tag 0BS6](https://stacks.math.columbia.edu/tag/0BS6); it is not a match for the proposed union obstruction theorem.
