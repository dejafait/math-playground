# Complete nonradial action — scalar prefix replacement attempt

The approved target remains the complete L025 response's finite
a^3-scaled limit for both probes. L213 leaves the complete transverse
24-pair class, and L214 gives cubic boundedness. This attempt tests
only a signed asymptotic replacement inside its two-prefix A_11 block;
the direct/direct and mixed blocks remain in the original response.

Saved before the longer verification: write a transverse forest row
prefix as w_e=b_j tensor q_e, where b_j selects axial edge levels
0,...,j-1 and q_e is the pinned transverse endpoint difference.
With H=Delta_3, G=H^(-1), L_E the full axial Neumann edge Laplacian,
compare f_e=(L_E tensor I+I tensor H)^(-1)w_e with
g_e=b_j tensor Gq_e. The desired threshold is a uniform O(1) bound
for ||H_T^(1/2)(f_e-g_e)||, not an unweighted covariance replacement.

For axial eigenvalue alpha and transverse eigenvalue lambda, the
error multiplier relative to b_j tensor Gq_e is -alpha/(alpha+lambda).
The inequality alpha^2/(alpha+lambda)^2<=alpha/lambda would bound
the squared H_T error by <b_j,L_E b_j> ||Gq_e||^2. The first factor
is exactly one for 1<=j<N, including j=N-1. The second should be
uniformly bounded by the three-dimensional sine spectrum and the
endpoint-difference numerator, including normal transverse end edges.
The normalized constant axial mode is retained and has zero error.

If these bounds hold, L065's actual scalar energy form and the
O(sqrt(N)) energies of f_e,g_e give an O(sqrt(N)) error in each
two-prefix residual-covariance entry. L213's full heat estimate
|U_(i,p)|<=C_i a^2 then gives O(N^(5/2)) summed response error,
which is o(N^3). This would justify this scalar plateau replacement
inside the complete action target, without assuming its limit or
transferring the estimate to mixed residual blocks.

Continue if the complete endpoint spectrum and all-prefix energy
error meet this threshold. Abandon the shortcut if it needs a smooth
upper extension, scalar-to-mixed transfer, or an error only controlled
pointwise without a uniform plaquette/heat sum. The plateau quadratic
form itself, the other residual blocks, full compensation, finer
asymptotics and the interacting/continuum/infrared gaps remain open.

Completed in [L215](../lemmas/L215-transverse-action-scalar-prefix-plateau.md).
The full endpoint spectrum proves ||Gq_e||^2<=6, and the exact axial
step has <b_j,L_E b_j>=1. These give the desired uniform O(1)
transverse-energy error and hence O(N^(5/2)) for the summed response
replacement. This is below cubic scale for both actual probes, with
all end rows and full heat sums retained. The two-prefix block is
now reduced to its sharp plateau quadratic form; that form and the
untouched direct/mixed blocks still require signed asymptotics.
No mathematical scripts or numerical sign premises were used.
