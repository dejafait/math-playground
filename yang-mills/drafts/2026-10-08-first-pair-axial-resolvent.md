# First-pair axial resolvent normalization test

Saved before completing the mathematical attempt. The unchanged
SPECIALIZE assessment `drafts/literature/2026-09-26-current-target.md`
covers the approved combined response target. This is checkpoint 095's
bounded axial-covariance subtest, not a new response target.

Main gap: the complete interacting response and its cutoff logarithm.
Intermediate target: evaluate the full relative transverse covariance
on L070's level-weighted base row S, with its physical normalization,
all transverse frequencies and actual axial averaging. Downstream use:
an exact input to the retained L074 trace, before attempting its spatial
trace or claiming that L070(9) is an original coefficient. Continue a
bulk-profile replacement only if its end-row correction is negligible
at the required scale; otherwise retain the correction and park that
replacement. Success would leave the path/path term, variable path
coefficients, scaled exterior defect and pinned residual remainder open.

Inputs: L026's relative component tensor spectrum, L041's last-column
Dirichlet inverse, L070's S and trace, L074's ordered two-term trace,
and L065/L072's actual axial average and displacement. ATTEMPTS/019–023
and history/095 were checked; they supply no axial linear-profile
resolvent evaluation. This specializes finite difference operators,
without reproving the assessed general renormalization results.

Working calculation: transverse components have axial Dirichlet matrix
L_V, not the component-1 Neumann matrix. For b_s=s and lambda>0,
(L_V+lambda)b=lambda b+N delta_(N-1). Hence the inverse is
(s-N sinh(s eta)/sinh(N eta))/lambda, eta=2 asinh(sqrt(lambda)/2).
The upper correction is comparable at lambda=O(N^-2), although it is
exponentially localized for high transverse frequencies. Check the
physical scaling a^3 of this profile and the actual odd axial factor
x rho(x) of u_1 before concluding anything about averaging. The
intervening level-dependent operator Lambda_l+D^T bar Q_l cannot be
commuted through the covariance. No signed trace result is presumed.

Unresolved: all original trace asymptotics, other mixed placements,
full response jets, interacting reflected error <=c_box/2, continuum
fields, reflection positivity, infrared control and finite positive mass.
No candidate solution exists.

Completed: L075 is the canonical proof. It establishes the exact
Dirichlet inverse and base-row formula, bounds over the full spectrum,
and the physical a^3 scaling. Its actual-u_1 average test has a strictly
nonzero fixed-mode limit, so the uniformly negligible bulk-profile
replacement is parked in ATTEMPTS/024. This is an exact covariance
input, not an original coefficient or a sharper signed-trace estimate.
The full variable path operator remains inside L075(11). Eight rational
finite-matrix tests pass exactly; no numerical asymptotic is invoked.

Continuation within the same approved response target: test the
centered circulation/path contribution at O(N²) using the full kernel
in L075(11), with Z_l=D^T bar Q_l for that selected contribution.
Essential inputs: L062's full heat and coefficient bounds, L064's
actual first pair, L070's ordered circulation trace, L074's centering
defect and L075's complete axial inverse. Keep the actual residual
A_0, E_0 average, every level, end row and transverse projection in
order. Continue only if an O(N²) complete heat-sum estimate or a
controlled scaled coefficient is established; otherwise record the
specific surviving contracted obstruction, without treating an operator
norm or frozen symbol as signed growth. Independently unresolved are
the path/path term, scaled exterior defect, variable-coefficient/pinned
remainder and all other response and construction requirements. No
new literature assessment was written or changed.
