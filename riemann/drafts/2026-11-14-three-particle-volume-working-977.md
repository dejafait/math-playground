# Three-particle weighted-volume attempt977 — working checkpoint

Approved target: continuation975's full coupled-H, all-separation
stopped determinant bound, without changing initial plane or time.
Main gap: L030-L032/C032a actual-Xi signed all-degree positivity.
The proposed bound would supply only a multidivisor mass input.

Working mechanism, not yet an independently audited result:
write g=grad log Delta, f_0=-2g, and
P=sum_(i<j)|z_i-z_j|^(-2). Direct three-vertex expansion appears to give
||g||^2=2P+16 Area(z_1,z_2,z_3)^2/|Delta(z)|^2 >=2P.
For each pair the real Hessian map has eigenvalues
+4/|z_i-z_j|^2, -4/|z_i-z_j|^2, and four zeros.
Thus its trace on any real three-plane is at most the positive
eigenvalue. Summing and adding D^2H suggests
mu_2(A^[3]) <=4P+3M_2 <=||f_0||^2/2+3M_2.
Completing the square against ||f_0+grad H||^2 would give
mu_2(A^[3])-||grad S||^2 <=3M_2+M_1^2.

Still to check completely: triangle identity including collinear
triples; pair Hessian signs and factors; real three-volume versus
the full complex determinant; compact-survivor source hypotheses;
stopped extension and common initial H bound. No endpoint theorem is
needed for the specified zero extension. No script or numerical
sample establishes this mechanism. Continue only if all checks yield
the full fixed-data bound; otherwise retain the precise failure.

Inputs: assessed TNV Appendix B and WKM Theorem4/Proposition5,
with C466s as comparison and C466k as sign convention, not premises
for the new collective estimate. Prior stops971/972/974 remain in
their single-divisor sign scope. No symmetry of H, spacing bound,
restart, global contour or Xi realization is assumed.

## Completion977

The working mechanism above closed with the stated constants.
The full hypotheses, exact triangle expansion, third-volume estimate,
coupled-H square completion and stopped quantifiers are canonical in
[C466x](../lemmas/C466x-three-particle-stopped-weighted-volume.md).
This draft preserves the pre-proof checkpoint, not an alternative
proof or current status record. Independent conceptual audit remains
pending. No numerical calculation or mathematical script was needed.
