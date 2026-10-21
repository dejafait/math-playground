# Gradient residual lift test

The unchanged approved target is the complete other/other cubic a^3
limit and comparison with -12 gamma D_i. This bounded attempt tests
L091's gradient diagonal E, keeping the full-Hodge prefix in its row
map. A uniform E bound would put Tr(J_k^T E J_l) at O(N^3), while
leaving the off-diagonal residual and co-closed diagonal unresolved.

Unfinished reasoning saved before writing the proof: let B be the
lower-rooted axial prefix matrix and B0 the axial edge-to-vertex
difference of L085. Then B0 B^T=-I. With lambda a transverse vertex
eigenvalue, the exact interval resolvents suggest

    R_E(lambda) B^T-B^T/lambda
                      =B0^T R_D(lambda)/lambda.

Together with Delta_T T=T Delta_0, this says the covariance column
of the projected forest gradient row differs from the pure-component-1
column I_1 B^T G T^T only by a full relative gradient. L018's actual
residual annihilates that gradient. L065's all-axial scalar form bound,
not merely its axial-zero statement, should therefore give
|V_g|<=C K_g because the pure column's transverse energy is exactly
the Brownian-prefix covariance M tensor P. Check both endpoint signs
and the full relative vertex domain before asserting this identity.

Essential inputs: L018 L026 L065 L085 L091; L084 L079 L080 L082
fix the comparison coefficient and saved-table/IEEE qualifications.
Continue if the exact row identity proves the N^3 crossed-diagonal
bound; abandon this shortcut if a surviving transverse row invalidates
the pure-component specialization. No bound on F or H, signed limit,
compensation, finer remainder, logarithm or separate forest invariance
is assumed. Other jets, interacting error <=c_box/2, continuum axioms,
reflection positivity, infrared control and finite positive mass remain.

Completed result: [L092](../lemmas/L092-other-other-gradient-residual-uniform-bound.md)
proves the exact covariance-column identity modulo a pinned gauge
gradient. Both endpoint signs are retained. The existing scalar
all-axial form theorem then gives ||E||<=C and R_E=O(N^3); the
two-gradient sector sharpens to O(N). Twelve exact rational interval
checks pass with maximum error 0. This is local REPRODUCTION, not a
new result claimed beyond the checked sources or a scaled-limit result.

Concrete continuation within the unchanged approved target: use
L092(10)'s exact cross block C (I_1^T A_0 I_T) K_h jointly with the
remaining H diagonal and 2 Tr(J_k^T F D_l) traces in L091(4). Test
whether the actual generator's two orientations and pinned prefix
give a joint N^3 bound or a signed leading-scale identity. Keep the
already bounded R_E and gradient-base crossed pair in the complete
comparison; their limits remain unresolved. Do not infer a mixed
bound by scalar polarization, assume positivity of A_0, or discard
cross-component outputs. An insufficient generic bound is not growth.
Continue for actual signed control or an independently discriminating
obstruction; abandon the proposed gain if it requires a source/profile
replacement or annihilation refuted by ATTEMPTS/019–027.

Essential continuation IDs: L009 L018 L020 L026 L028 L048 L065
L085 L086 L087 L088 L089 L090 L091 L092, with L084 L079 L080
L082 for the comparison and saved-table/IEEE qualifications. Neither
separate forest invariance, differentiated base-law zeros, a finite
scaled limit nor compensation is assumed. All independent gaps listed
above remain. The unchanged assessment is reused; no new target
assessment or separate source approval is asserted here.
