# Step 245 working record: signed intermediate feasibility

Approved target: the exact step-244 target in
`literature/2026-10-19-finite-witness-signed-intermediate-feasibility.md`.
RESEARCH / POTENTIALLY_NEW / proof_attempt. The working notes below were
saved before the full verification. The completed proof is canonical in
L437; these notes are superseded, not a second proof. Separate critical
audit remains pending.

Main gap: global mixed positivity. Intermediate target: preserve L431's
selected law while adding L436's fixed negative P-weighted cubic.
Downstream use: determine whether that witness forces the favorable
joint-sign orientation in this relaxation. Continue only if positive
masses, uniform exact support and every induced correction close; an
unavoidable leading error would stop this repair alone.

The L419 leading response has s=a^2+h^2 in a fixed positive annulus.
For U=(a+h,(a-h)/2,-(a+h)/4), the leading forms give
B_0(U)=c s/2, ell_0(U)=s/2 and D_0(U)=-c^2 s^2/4.
Also s/2<=|U|^2<=17s/8. Normalization and uniform small coefficient
errors should therefore give an exact measurable unit direction with
B>0,D<0, both separated from zero. This differs from reversing
L421's positive direction, which would violate the required support.

For torus Haar average, let C(x)=cos x_2, p1=<P C>,
Q=P-1-2p1 C. The coefficient of Q at the prime-3 unit frequency
is (1-1/131072)/sqrt(3), hence <Q^2>>0. With rho=gamma_2/beta,
f=beta(1+2rho C)+tau Q and
tau=[beta I-beta(1+2rho p1)]/<Q^2>, the three requested Haar
averages are beta,gamma_2,beta I. All functions are fixed bounded
polynomials; actual-height means of their products have O(1/H) error.

Pending verification: split f into f_+,f_-; use L421's positive direction
and the new negative-D positive-B direction at radius ell^(3/2), with
nonnegative masses ell^2 f_+/(R^3 h_+) and ell^2 f_-/(R^3 h_-).
Recompute all masses and L429/L431 corrections, rather than invoking
the old law as unchanged. Expected intermediate costs are the same
powers of ell with constants depending on fixed P. Actual/global
realization, clipping, capped nondegeneracy and L413's regulator margin
remain outside this test. L417's antipodal and L418's radial failures
are restricted contrasts; ready primary-source coverage is reused.
