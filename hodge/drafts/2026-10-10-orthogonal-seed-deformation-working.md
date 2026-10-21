# Bounded orthogonal-seed deformation attempt

Approved target: Determine whether L079's acyclic stable orthogonal rank-five block J_5 exists at the exact metric h.
Prior EXPLORE assessment: drafts/literature/2026-10-10-rank-five-acyclic-orthogonal-existence.md.

Main gap: universal primitive Hodge algebraicity; even this route still lacks the other image and a common kernel.
Intermediate target: justify the skew-adjoint DG Lie splitting for L080's actual (J_0,Q), then compute its cohomological quadratic deformation model. Downstream use: decide whether this actual seed has form-preserving directions worth realization/stability work.
Test: stop this recipe if no suitable formal direction exists; retain formal-to-actual realization and underlying-vector exact-h stability as separate bridges even if the quadratic model has points.

Inputs: L080 (actual seed, spherical E and cohomology), L052 through L080 (Zk, k^2=-14); L079 only identifies the desired output. Prior ATTEMPTS/043,/045,/053 are necessary-index stops, not deformation exclusions. No cross-notebook input.

Unfinished reasoning, saved before source retrieval: coefficientwise Q-transpose splits End(J_0) into skew and self-adjoint bundles; commutator with skew endomorphisms preserves each, so Dolbeault skew forms split as a module and Theorem 2.3 should apply after Theorem 5.1. The adjoint bundle is wedge^2 J_0 = End(E) plus E plus E^vee plus det(E) plus det(E)^vee. Expected H^1 dimensions are 0+1+1+5+5=12. H^0,H^2 each have dimension one. Torus weights should be +/-1 and +/-2. Need check complete dual pairings and quadratic equation, rather than infer unobstructedness from formality. No J_5 existence or analytic realization asserted.

Completed result: L081 contains the complete proof. The splitting and expected dimensions hold. The normalized quadratic equation admits x=y=u_1=1,v_1=-1/2 with remaining coordinates zero, and evaluation on the unique central section is nonzero. This is a formal intermediate ADVANCE / REPRODUCTION, not actual J_5 existence. Essential actual-realization and vector-stability coverage is now recorded as REVIEW_REQUIRED in drafts/literature/2026-10-10-orthogonal-seed-realization-and-stability.md; no mathematics under that new continuation was attempted.
