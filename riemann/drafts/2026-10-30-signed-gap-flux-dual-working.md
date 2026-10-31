# Signed gap-flux dual attempt: working checkpoint

Gate: `drafts/literature/2026-10-30-signed-gap-flux-dual-test.md`,
saved EXPLORE assessment supplied at invocation. This is one mathematical
attempt at its exact target; source comparison and endpoint cautions are
reused from its parent assessment. No source theorem is imported as a
conditional gap estimate.

Main gap: actual-Xi all-degree positivity and initial signs at unbounded
heights remain unproved. The intermediate target is Q<=C_R a M in the
unchanged L503 smooth Fourier family and rectangle. If valid, it could
combine with L503's necessary leakage inequality to give nonvanishing
detector cost; L503's full proof still awaits independent audit, and
actual-zero signs and arithmetic transfer would remain independent.

Read L503 in full and the exact-bound source comparison and first-mode
failure. The elementary N<=A_R M proof is available for replay. The
previous unconditional exponential norm closure is stopped. No Fourier
derivative bound or positivity in the gap is available. Existing notebook
changes are preserved. No other notebook is an input.

Attempt: for the linear gap functional Q, seek a positive measure mu
supported on the closed known-positive rectangle (closure justified by
continuity) such that Q(f)+integral Re f dmu has a real-axis representation
with actual L-infinity norm O_R(a). Then positivity gives Q(f) at most
that residual functional, without normalizing away the lower bound 1.
The plus sign is essential. Formal distributional equality is not enough.

Test: prove the continuum representation and uniform residual norm, or
record a quantitative obstruction to the chosen measure ansatz. An
admissible unbounded Q/(a M) would refute the inequality itself. Merely
recovering the old exponential estimate warrants stopping this ansatz.

## Concrete measure and unresolved norm check

For 0<=y<b define the even nonnegative strip kernel

    p_b(t,y) = (1/(2b)) Re sech(pi(t+iy)/(2b)).

The intended angular Fourier transform is
cosh(s y)/cosh(s b). Define

    w_b(t)=integral_0^b exp(-lambda y)p_b(t,y)dy,
    W_a(x)=w_b(x-a)+w_b(x+a).

The candidate positive measure is W_a(x)dx on y=b, |x|<=a.
If the exact kernel calculation holds, then

    Q(f)=-integral_R W_a(x)u(x,b)dx,
    E_a(f)=Q(f)+integral_{-a}^a W_a(x)u(x,b)dx
          =-integral_{|x|>a} W_a(x)u(x,b)dx.

For the formal cosine with s a=2pi n, write
I(s)=integral_0^b exp(-lambda y)cosh(sy)dy and
J(s)=integral_{2a}^infinity w_b(t)cos(st)dt. Then the
candidate formula is E_a(cos(s z))=-I(s)-2cosh(s b)J(s).
Scaling w_b(t)=W(t/b), where beta=lambda b=pi/8 is fixed,
suggests J(s)=O(1/(b s^2)) by two integrations by parts,
because 2a=8b and sin(2as)=0. Meanwhile I(s) is of order
exp(s b)/s. This would leave exponential residual norm.

The cosine is not an admissible Fourier-smooth L1 test. To validate the
norm obstruction, replace it by h(z/a^2)cos(s z), with h the inverse
Fourier transform of a fixed even nonnegative smooth bump of mass 1.
Check support inside [-R,R], N<=a^2||h||_1 and uniform approximation
on |x|<=a, 0<=y<=b. This test need not satisfy rectangle positivity:
its role is to test the dual residual's required full-class norm, not
to refute the conditional inequality. No conclusion is claimed until
the Fourier formula, tail bound and approximation error are proved.

## Completed bounded attempt

The calculation above is now completed, with the full proof and every
qualification canonical in
`lemmas/L504-clipped-strip-poisson-dual-residual-obstruction.md`.
The positive measure has an exact continuum representation and a finite
residual norm for each geometry. Its full-class N-norm is at least
c_R L^(R/4)/a^2, so its ratio to the required O_R(a) threshold diverges
at least as L^(R/4)/a^3. A smooth bump times a resonant cosine supplies
actual V_R tests at every sufficiently large real T; a plane wave or
sampled certificate is not used as evidence for the norm conclusion.

The calculation is an informative negative for this clipped measure,
not for the proposed conditional inequality. Tests are not asserted to
satisfy rectangle positivity. No L503 conclusion or weighted norm
conversion is used, and no source theorem is claimed to imply the new
norm bound. Classical kernel calculations are reproduction; originality
of the specialized obstruction is unchecked beyond the saved assessment.

Stop this ansatz. Other positive measures and a cone-restricted residual
estimate remain open. Before using L504 as a route exclusion, obtain its
separate critical audit, especially the clipping factor, complete signed
functional, Fourier support and all-height uniformity. There was one
coherent proof attempt, no mathematical script or numerical experiment,
and no claimed improvement in actual-Xi signs or detector cost.
