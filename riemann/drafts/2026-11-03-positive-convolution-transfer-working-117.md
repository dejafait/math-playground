# Positive-convolution scalar transfer — working checkpoint, step 117

Approved target and gate: reuse the unchanged EXPLORE assessment
`literature/2026-11-03-fourier-gap-positive-convolution-transfer.md`.
Main gap is actual-Xi mixed positivity; the bounded intermediate test is
exponential decay of L666's finite c_0(1) for one fixed summable profile
with a gap at the saved omega_*. Angular, spatial and logarithmic
transfer remain independent open issues.

Relevant inputs read: L666's exact product, L694's full construction and
audit (including its L1 signed-interval primitive), L693's prescription
conventions, and L690/L695's qualified conclusions. The step-105 screen
and L695 absolute-tail stop are preserved; neither settles this scalar.

Initial calculation: at u=1, writing y=Im(a), each factor is
(1-i*alpha_j*y)/(1-i*beta_j*y), alpha_j=t_j/(U+d*t_j),
beta_j=1/(d+t_j). Set r_j=alpha_j/beta_j. Then 0<=r_j<1,
and the factor is r_j+(1-r_j)/(1-i*beta_j*y). In particular
r_0=0: the anchor weight is 1, and the j=0 exponential is retained.
Durrett's assessed mixture/product rules give W(y)=E exp(i*y*S_n).

Outstanding checks before any theorem claim: center placement in the
L694 construction; quantitative concentration of h*S_n; a valid
non-Schwartz lattice pairing; both finite endpoints. W has a 1/y tail
at infinity, so an absolutely convergent unpaired infinite sum is not
available. Test symmetric unshifted summation plus the absolutely
convergent l1 displacement correction. A qualitative gap identity or
tail probability alone is not the sought finite exponential estimate.

Continue only with C exp(-c*n), c>0, after these errors, or preserve a
precise obstruction. No new theorem is claimed by this checkpoint.

## Reasoning saved before canonical write-up

Let V_n=h*S_n and p_n be its probability density. The j=0 exponential
has rate lambda_0=d/h; other factors are mixtures with atomic weights
r_j<=48/67. Hence p_n(0+)=lambda_0*product_(j>=1)r_j. For v>=0,
exponential tilting at n/20 gives
p_n(v)<=lambda_0*exp(n/8-n*v/20). Thus all nonzero Fourier-comb
samples 2*pi*k, k>=1, have an exponentially summable bound. The zero
sample receives half its right-hand density; omitting this endpoint
would invalidate the pairing.

For the half-translated signed interval primitive F, the infinite
symmetric sum is the Fourier-comb contribution plus
E[1+i*V_n*F-hat(-V_n)]. The multiplier in this expectation vanishes
on the positive gap, by real reflection of the distributional gap.
Its growth is at most 1+||e||1*V_n. Bernstein and a uniform second
moment then give an exponential bound. Justify the comb formula by
Gaussian regularization and Schwartz Poisson, not formal substitution.

At |y|>=2/5 every factor has modulus <=kappa=sqrt(99/100).
Subtracting the real limits r_j in a finite telescoping identity yields
|Re W(y)|<=3*n*kappa^(n-2)/y^2. Also
|W'(y)|<=(81/20)*n*kappa^(n-1)/y^2. The exact omitted index pairs
start at m=2q and -2q-1, with unshifted |y|=9/20 and shifted
|y|>=9/20-h/8>2/5. Their symmetric sum is bounded by
9*n^2*kappa^(n-2)+70*||e||1*kappa^(n-1).

Center: the integral f(t)=1/(d+t)-t/(U+d*t) is positive;
omega_*>=702/847>pi/4, and omega_*<=54/25<3*pi/4.
Thus c=omega_*/(2*pi) stays in L694's original annulus (1/8,3/8).
Replace only its center and reduce the cutoff width to fit the annulus
and the same small-norm threshold. All kernel constants precede width.

These calculations are to be fully justified in the canonical proof;
they are not independently audited. No numerical script is needed.

Completed disposition: the full proof is now canonical in L696, with
the quantitative inequality (26). Report ADVANCE for this finite scalar
transfer only; no independent audit or broader transfer is claimed.
The next source-scope review is REVIEW_REQUIRED in PROGRESS.md.
