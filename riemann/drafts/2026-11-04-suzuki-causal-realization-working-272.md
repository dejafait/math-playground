# Causal realization working record, step 272

Approved target: the exact finite-window realization in the unchanged
`literature/2026-11-04-suzuki-causal-generator-realization.md` (SPECIALIZE).
Main gap: unconditional actual-Xi mixed positivity. This construction could
make a later original-norm energy comparison well defined; no sign or
uniform-window estimate is attempted here.

Inputs read: L018 and L618; step-270 primary-source assessment and the two
Suzuki stop records. L739 is contrast only. Existing changes are preserved.
No cross-notebook input or mathematical script is needed.

Provisional calculation, not yet a theorem: write p=-iz, s=p+1/2. The
complete logarithmic symbol should be -log(p)+log(2*pi)+Laplace(q)(p)
+2 sum Lambda(n)n^(-1/2)exp(-p log(n)), Re(p)>1/2, where
q(x)=(exp(-x/2)-1)/x+2 exp(-x/2)(h(2x)-1)-2 exp(x/2),
h(v)=1/(1-exp(-v))-1/v. The first term is the known Riemann--Liouville
generator. q is locally integrable; each finite window sees finitely many
arithmetic shifts. Check every coefficient, endpoint trace and domain.

Remaining construction checks: bounded perturbation in the unweighted
norm; an exponentially weighted convolution algebra solely to identify
the kernel (not to replace the target norm); theta=0 strong convergence;
reflection and inactive subspace. Continue only if all of these hold.
Abandon this implementation if an unproved global L2 multiplier or changed
target norm is essential. Success still leaves total dissipativity,
all-window control and Xi sign transfer open.

Completed the one construction. The canonical proof and qualifications
are now in `lemmas/L740-suzuki-finite-window-causal-generator.md`; the
provisional formula above agrees with its complete-symbol calculation.
Finite-L boundedness, exact domain, strong zero limit and reflection
passed the construction test. No energy calculation was undertaken.
The separate conceptual audit is not yet complete; its newly saved
scope needs approval on the following turn.
