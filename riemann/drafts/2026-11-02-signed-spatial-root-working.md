# Signed spatial-root stability: bounded attempt in progress

Invocation target and gate: the unchanged EXPLORE assessment
`literature/2026-11-02-signed-spatial-root-deformation.md`, supplied at
startup, permits one signed full-mean test or an admissible countersequence.
Main gap: actual-Xi mixed positivity; the local intermediate gap is the
uniform logarithmic loss from L664's undisplaced baseline to L666's cube.
Support, realization and signs are independent. Existing anchor,
absolute-contour, scalar-energy and inverse-data stops are preserved.

Essential inputs read: L649's full product, L666's exact admissible family,
L664's audited uniform anchor approximation, L668's nonzero finite-moment
identity. The supplied source comparison covers the complete-root formula,
fixed-degree continuity and local monic regularity. No new literature,
numerical screen, root separation or degree-uniform regularity is assumed.

Current possible countersequence (unproved, checkpoint before work):
use only finitely many symmetric central node pairs for each fixed order K.
For t=r+1/2 and H_0=27/(10n), the complete weight at y=H_0*t tends to
exp(i*kappa*t), kappa=(27/10)*integral_0^1(A(t)+b(t))dt in (243/50,297/50).
Attempt to cancel the anchor and the first K centered moments by paired
shifts |e|<1/8. For large finite pair count L, the scaled Jacobian rows
are oscillatory polynomials; their real Gram limit might be positive.
If the desired correction has controls O_K(1/L), a concrete contraction
could solve the finite limiting system and its actual finite-n version.
Taylor expansion of the *full* geometric polynomial, plus L664's
exponentially small baseline remainder, would then give
sup_|zeta|=1 |G_e(-1,zeta)| <= C_K*n^(-K-1).
That would imply signed full-root loss/log n >= K+1-o(1), and a diagonal
sequence would refute the stronger stability target only. None of these
existence or error bounds is yet established.

Tests still required: invertibility and quantitative control of the actual
paired Jacobian; nonlinear residual with the box constraint; actual-n
moment equations; exact Taylor remainder including all M moments;
nonzero slices and leading-factor/degree-loss qualifications. If these
cannot be justified, preserve the failed step and report EXPLORATION.
No bound on absolute root speed or inverse interpolation cost will decide
this test. No mathematical script has been run.

## Mid-attempt checkpoint: concrete existence argument to verify

For j=0,...,K and L positive nodes t_r=r+1/2, set
Psi_(n,j)(t)=2 Re[(i*t/L)^j w_n(t)], where w_n(t)=W_(x+i*H_0*t)(-1).
Seek sum_r[Psi_(n,j)(t_r+e_r)-Psi_(n,j)(t_r)]=-1 if j=0 and 0 otherwise.
The limiting Jacobian J has normalized Gram matrix tending, as L grows,
to Q_jk=2*kappa^2*cos((j-k)*pi/2)/(j+k+1). Its quadratic form is
2*kappa^2*integral_0^1 |sum_j v_j*(i*u)^j|^2 du>0 for v!=0.
The oscillatory remainder vanishes by finite geometric summation because
pi<kappa<2pi. This is finite-dimensional and K is fixed first.

Let lambda be the positive minimum eigenvalue of Q. Uniform column and
second-derivative bounds B,H give a right inverse T_n with
||T_n||_(2 to infinity)<=A/L, A=4B/lambda, once L and then n are large.
For the nonlinear remainder R(e), ||R(e)||_2<=H*L*||e||_infinity^2/2.
The explicit iteration e_next=T_n*(-unit_0-R(e)) contracts the cube
||e||_infinity<=2A/L if L>=max(16A,4A^2*H). It solves the actual-n
equations, not just limiting ones. Need write complete bounds and proof.

These equations cancel the anchor plus signed old/new node difference
against every polynomial in a-x of degree <=K; actual final residues
remain one. Full T_M Taylor remainder on |a-x|<=1/16 is bounded by
R*16^(K+2)*|a-x|^(K+1). With |w|<=1 this would give
sup|G_e|<=1000*n*exp(-n/3000)+C_K*n^(-K-1),
C_K=4L*16^(K+2)*[(27/10)*(L+1)]^(K+1).
L664 gives m_0>=-log(2R). L668 gives nonzero slices on the entire
straight path; fixed-degree continuity and the complete-root identity
handle crossings/degree drops without differentiating a reciprocal.
The remaining task is to check and write this analytic proof, not a
numerical root screen. This draft is unfinished and not canonical evidence.

## Completion

The complete argument and its qualifications now live in
[L669](../lemmas/L669-signed-spatial-root-logarithmic-stability-countersequence.md).
The provisional sections above are preserved as work checkpoints, not
additional canonical proofs. Outcome: an unaudited countersequence to
uniform logarithmic stability, with the weaker linear-rate mean and
all actual-Xi gaps unchanged. The next checkpoint nominates a separate
conceptual audit; no such audit was performed here.
