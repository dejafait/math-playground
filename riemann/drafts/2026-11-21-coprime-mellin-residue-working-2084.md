# Integrated coprime pole-pair attempt2084 — working checkpoint

Authorized target and source gate: unchanged EXPLORE assessment2081;
source-notes2082 and2080 read, C034r kernel/multiplier proof inspected.
Main gap remains actual-Xi algebraic mixed positivity L030-L032/C032a.
Possible use is the low primitive subpower upper, with high primitive,
source-energy, scale/error and mixed-transfer gaps independent.

Preserve all pre-existing work. No shared infrastructure/state edits,
cross-notebook input, delegation or mathematical scripts. The initial
notebook-scoped git status was unexpectedly large; subsequent inspections
are limited to touched paths. No pre-existing change has been removed.

Candidate calculation (not yet a proved conclusion): write the coprime
double Dirichlet series as reciprocal zeta in each variable times a
remainder convergent when Re(u),Re(v)>0 and Re(u+v)>1. For a conditional
zero rho=beta+i gamma, beta=1/2+delta, delta>0, the conjugate point may
make every remainder local factor strictly positive. The actual w_Q is
the autocorrelation of t exp(-t/4) times the indicator of [0,Q], so k should have
nonnegative Fourier density. A pair of Perron residues at u=rho and
v=conj(rho) then has denominators whose product is
delta^2+(gamma-t)^2, suggesting a strictly positive integrated highest
log coefficient for every finite multiplicity m>=1.

Still to justify before using this: exact absolute region; Fourier
normalization/regularity for the nonsmooth window; both finite square
cutoffs and their errors; all local nonvanishing and Laurent conditions;
integration of the entire finite-order principal part. A local residue
is not a proved asymptotic of M_K. No unbounded contour shift, rightmost
zero, simple-zero assumption or one-sided-upper contradiction is allowed.
Stop automatic pole removal only if the actual integrated pair survives.

## Mid-attempt checkpoint

The calculation now gives a candidate rigorous local obstruction, pending
canonical write-up/check: D(u,v)=H(u,v)/(zeta(u)zeta(v)) with
H=zeta(2)^(-1) product_p (1-c_p(p^-u+p^-v))/((1-p^-u)(1-p^-v)),
c_p=p/(p+1). H converges normally for Re(u),Re(v)>0,
Re(u+v)>1; at (rho,conj(rho)) each numerator exceeds
1-2 sqrt(p)/(p+1)>0. For k=w_Q C_h, its Fourier density lambda is
nonnegative integrable with integral 2pi k(0)>0. The integrated cutoff
multiplier B(u,v)=integral lambda(t)/((u-1/2-it)(v-1/2+it)) dt/(2pi)
is holomorphic for Re(u),Re(v)>1/2 and strictly positive at the pair.

Thus the integrated germ D B has an exact mixed pole of order (m,m).
Its finite square-cutoff double residue at x=K+1/2 is
x^(2delta) times a degree-(2m-2) polynomial in log x whose leading
coefficient is H(rho,conj(rho)) |m!/zeta^(m)(rho)|^2
B(rho,conj(rho))/((m-1)!)^2 >0. Full principal-part coefficients
are derivatives of the holomorphic numerator, not just this leading term.

Finite-height Perron identity will retain both errors H_a E_b and E_a H_b,
and E_a E_b. Half-integer x implements both inclusive integer cutoffs
without silently dropping half-weights. Fourier truncation has a separate
L1 tail. No contour shift is used: horizontal, other-pole and single-pole
terms in any proposed global shift remain unestimated. Accordingly the
result only rejects local automatic removal; it gives no asymptotic,
Omega result, upper-bound counterexample or RH conclusion.

## Completion

The candidate reasoning above was completed as canonical C034s,
including the exact additional height-end chains needed before taking
the ratio integral inside fixed finite contours. The canonical file
contains the full proof and citations; its independent audit remains
pending. Outcome NEGATIVE is limited to automatic local pole removal.
No global signed upper or off-line-zero assertion follows.
