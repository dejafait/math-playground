# Spatial growth near i/2 — working record, step 166

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-spatial-doubling-growth-attempt-scope.md`.
Its exact B_sp target and the actual fixed L703 profile are retained.
The unresolved main gap is actual-Xi all-degree positivity; this step
tests one unpaid angular neighborhood for the spatial Jensen payment.
The bounded test is uniform o(n) growth on a fixed arc near i/2, or
a positive linear lower rate there, with the actual S_(n,1) denominator.
Neither finite samples nor a failed upper certificate decide it.

Inputs read: L666's exact rational weights, L703's fixed Gevrey
construction, audited L708's complex convolution and signed pairing,
and C708a's two paid arcs. The parent source comparison and the
interpolation, absolute-envelope and two-arc completion stops were
reused. No new source theorem or analytic continuation of S_e to
nonreal frequencies is assumed. C708a remains unaudited and is used
as orientation, not as an essential input to the new local test.

For u=i/2, L708's exact factor Q_t gives

    |Q_t(i/2,y)|^2 = (d^2+t^2/4)/(d^2+(t/2-y)^2)
                    *[d^2*t^2+(U/2-t*y)^2]/[d^2*t^2+U^2/4],
    partial_y log|Q_t| = (t/2-y)/[d^2+(t/2-y)^2]
                    -t*(U/2-t*y)/[d^2*t^2+(U/2-t*y)^2].

The phase of the product is still present in the signed spatial sum.
An initial diagnostic will distinguish endpoint dominance from an
interior modulus maximum before choosing a rigorous estimate. If the
maximum is interior, absolute variation cannot replace the complex
convolution; the real-frequency correction and both finite tails must
still be paired. All n=12q+3, M=n/3, unit masses, W_x=1, j=0 and
inverse angular factors remain in force.

Unresolved at this checkpoint: a signed lower bound for S_(n,1), the
relative finite geometric tail, and a uniform fixed-arc conclusion.
Global amplitude/full charge, L657 accounting, H/support and Xi
realization remain independent. No result or outcome is claimed yet.

## Phase-sensitive refinement before certification

The two saved diagnostic JSON files are uncertified quadrature/grid
screens. They suggest an interior real-ordinate modulus peak and a
useful upper contour y=x+3i/20. For the limiting product rate

    Phi_c(x)=integral_0^1 log|Q_t(i/2,x+i*c)|dt,

the proposed certified bounds are sup_x Phi_(3/20)<-41/1000,
sup_x Phi_(-1/10)<74/1000, sup_x Phi_0<24/1000,
Phi_0(-Y)>1/50, Phi_0(Y)<-1/10, and
Phi'_0(x)>1/25 on [-1,-Y]. All must be proved, not inferred from
the diagnostics. The actual positive bump ends before 543/500;
its tilted density exponent would then be below 29/1500<1/50.
The high-frequency part starts at 9/4 and uses the lower contour.

At z=1/2 the extra resolvent pole is below these contours. The exact
signed infinite sum could therefore be smaller than the negative
finite-tail endpoint, giving a nonzero scalar normalization. The
real-line absolute rate and s*rho<1 would then pay T_n/S_(n,1).
This is a useful intermediate target within the unchanged B_sp test.

The same upper contour is NOT automatically admissible for every
|z|<=s. The resolvent pole is y_z=-i*(d+R/z). For example
y_z=-2/5+7i/100 corresponds to z=-R/(33/25+2i/5), and lies inside
the unit spatial disk. A full-radius contour argument must include
the crossed residue. This is not evidence that B_sp/n is positive.
The earlier tentative height 1/25 put that example outside the
comparison disk; 7/100 is the corrected, exactly checked example.

## Completed attempt

The full proof and all qualifications are canonical in L709. The final
certificate uses the explicitly derived cubic-Taylor quadrature error
K/(45*N^4), rather than relying on the sharper Simpson theorem. All
21 auxiliary comparisons pass. The scalar negative-tail limit gives
S_(n,1)>=exp(n/50) and the relative geometric remainder is
O(exp(-n/500)) on a fixed arc near i/2. No separate critical audit or
full B_sp conclusion is claimed. The mandatory spatial residue remains
unestimated; the pole-free extension is recorded separately in ATTEMPTS.
The two diagnostic JSON files are preserved but are not proof evidence.

The unchanged ready target can continue with the complete signed
residue-plus-contour comparison at both spatial radii. L709's new
normalization is a lower bound, not an upper bound for S_(n,1); a
positive growth obstruction would require the latter as well. The
global complementary arc, amplitude, charge and Xi gaps remain open.
