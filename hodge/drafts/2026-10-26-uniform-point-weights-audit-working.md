# Uniform point weights critical audit — step 563

Approved target: Critically audit L169's Ext-generator sign, global base-trace scalar and cancellation proving uniform point weights under L111 and L168.
Invocation-start assessment: drafts/literature/2026-10-26-uniform-point-weights-critical-audit.md (SPECIALIZE). Completed work will be RESEARCH / REPRODUCTION / proof_audit.

Main gap: primitive realization and existence of the conditional F. Intermediate target: verify L169 (1)–(13), especially the augmentation-compatible injective comparison and same global trace. Downstream use: a common coefficient in an actual section-quartic test; no section values or square-length conclusion follow.

Test: compare the full tensor/internal-Hom differential, augmentation, even shift, residue generator, global dualizing isomorphism and L111 KS normalization. Preserve L169 if all agree; correct a common sign if necessary; retain L168's symbolic formula if a point-dependent factor remains. Empty and singleton support remain included.

Inputs: L169, L111, L168; their retained conditional hypotheses, actual maps, fixed forms, h_0 and one common relative scalar kappa. Reviewed ATTEMPTS/092–094: neither section-image vanishing, scalar-isotropy exclusion nor cyclicity-only vanishing is reopened. No cross-notebook input. All pre-existing changes are preserved.

Audit in progress: the actual incoming coefficient in L111 is -8 lambda sigma_B(u_1,u_2); L168 contributes 4 kappa^2/bar(c_0). The remaining check is the source-compatible Ext/residue sign and trace, not a recalculation of these upstream results. Primary PDFs are being consulted only for the approved proof cases, reusing source coverage; this is not a new literature assessment.

Completed: the canonical L169 audit preserves (1)–(13). The full tensor/internal-Hom recurrence is s_(i+1)=(-1)^(i+1)s_i, compatible with augmentation; r=2 introduces no additional shift/determinant sign. The same base counit gives -delta_B f_z(z), and the actual KS coefficient is -8 kappa lambda f_z(z). Both coordinate factors in L168 give mu_z=delta_B kappa/(2 lambda). No substantive error or stronger result was found: EXPLORATION / REPRODUCTION, one mathematical exploration turn since step 561. No mathematical script was needed. Full reasoning and source citations are canonical in L169.

Continuation proposed, not attempted or approved: identify the actual restricted radical in L164's ordinary middle-fibre image using L111's incoming KS plane. A targeted duplicate check found L164's rank>=48 statement and t>26 threshold; no exact restricted-radical assertion in the inspected passages. Separate source coverage is required in drafts/literature/2026-10-26-ordinary-middle-bracket-radical.md. Existing parked routes remain parked.
