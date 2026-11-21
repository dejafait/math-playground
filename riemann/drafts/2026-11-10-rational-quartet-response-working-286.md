# Rational quartet response working checkpoint — step286

10 November 2026. Work in progress under unchanged EXPLORE review285;
this draft asserts no completed result. Actual task: proof_attempt/creative.

Main gap: L030–L032/C032a positivity and L966/L968 signed forcing.
Test only the rational quartet specified in review285, replacing F in
both branches of L994(4). No actual complementary holomorphy is assumed.
Reuse review284 step285 source statements and duplicate/failure comparison.
L985 supplies only the exact finite K identity; L994 supplies the contours.
All pre-existing work, including unfinished inverse working271, is retained.

Preliminary plan to verify: write alpha=omega-1 and use multiplicity mu
(to avoid collision with L994 m=n+r). Rational denominators put every
s-pole to the left of Re(s)=1. The complete vertical integrand has an
integrable O((1+|Im(s)|)^(-2)) tail, uniformly on compact initial z-disks
and the fixed w-circle. Residues should identify a continuous exponential
input, including both shifted branches and all four endpoints.

For each endpoint slope c in {1,2}, the inverse map suggested by the
Laguerre generating function is x=f_c(w)=w*exp(c*w/(1-w)),
x=z*exp(c*alpha). Applying theta+r-1 removes S_r denominators.
The factor D_c(w)=1+c*w/(1-w)^2 vanishes at e^(+-i*pi/3)
for c=1, and at +-i for c=2. These are only candidate branch points;
reachability, coincident terms and nonzero full-quartet coefficients
remain to be proved. No isolated-integrand singularity is evidence yet.

Bounded decisive test: obtain the exact response with justified limits,
then prove a reachable nonremovable singularity of one full component,
including all parameter exceptions, or exhibit a concrete cancellation.
Success would be only a finite-detector ingredient. Actual other zeros,
J_r/-C_r, common-domain continuation, signed outputs, L993 recovery and
L984(H) remain independent gaps. Do not turn this into actual extraction.

## Partial noncancellation calculation (not yet an audited result)

Let delta=beta-1/2>0, alpha_sigma=beta-1+sigma*i*gamma,
f_2(w)=w*exp(2*w/(1-w)), and D_2=(1+w^2)/(1-w)^2.
The selected small inverse U_2 is unique in |w|<1 for |x|<exp(-1)
by Rouche on |w|=t<1: |x|<t*exp(-2*t/(1+t)).
A proposed reachable point is z_*=exp(-2*alpha_+)*f_2(i), with
|z_*|=exp(-2*delta). The path exp(-2*alpha_+)*f_2(t*i), 0<=t<1,
stays strictly inside that disk, since the derivative of
log(t)-2*t^2/(1+t^2) is (1-t^2)^2/[t*(1+t^2)^2]>0.

For q=1-z/z_*, the branch selected from the disk should satisfy
1/D_2(U_2(x))=((1-w_0)/2)*q^(-1/2)+O(1)
at w_0=+-i. This follows from f_2''(w_0)/f_2(w_0)=w_0 and
selection of the root lying inside the unit disk; verify all signs.
The relevant diagonal kernel is
h_(c,r,alpha)(w)=w^(1-r)*(1-w)^(-3)*(exp(c*r*(alpha-b(w)))-1)/(alpha-b(w)).
For Y_r=(theta+r-1)Z_r, Lagrange inversion gives h(U_c)/D_c,
with its Laurent degrees below 2 removed, and the full constant
branch subtracted. The c=2, r=2 critical coefficient then simplifies
to mu/4*(1+z_*^(-2))*sum 1/(alpha_sigma-b(w_0)), over ALL colliding
right-pair contributions. Each denominator has real part delta>0;
the reciprocal sum cannot vanish and |z_*|<1 excludes the prefactor
zero. If justified, Z_2 has coefficient minus twice this multiplying
q^(1/2). The r=1 and left-pair branches are holomorphic here.

Remaining proof duties in this checkpoint: exact response signs and
low-degree subtraction; full rational height domination and removable
lambda=0 cases; analytic continuation of the selected inverse to
noncritical boundary points (in particular exclude escape to w=1);
convergent Puiseux expansion on a common slit disk and all collisions.
No actual-Xi conclusion follows even if these duties are completed.

## End-of-attempt disposition

The proposed finite-input duties are now addressed in the canonical
proof L995, which is awaiting a separate critical audit. The earlier
working checkpoints above are preserved as intermediate reasoning;
they are not the current proof or current notebook status. The
complete r=2 collision coefficient supplies the positive detector
result, without an actual-complement conclusion. See history286 and
the compact PROGRESS.md checkpoint for the continuation decision.
