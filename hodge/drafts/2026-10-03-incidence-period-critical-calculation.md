# Incidence-period comparison — critical calculation

Completed-target wording: Critically verify L043's cohomological period comparison for arbitrary first-order map motion, retaining the map-motion homotopy and the relative incidence marking.

The prior SPECIALIZE assessment is
[the contraction assessment](literature/2026-10-03-resolved-lift-contraction-compatibility.md).
Its supporting sources and unchanged hypotheses are reused; this is a
mathematical application, not another retrieval attempt.

## Gap and test

The local gap is a representative reaching the fourth NS-fixed RM
direction. The intermediate question is whether L043 really identifies
the K3 blowdown deformation with the prescribed target deformation for
every source and map motion. A cohomological correction that survives,
or a failure of the incidence marking, requires a qualified exclusion.
If both comparisons hold, preserve that scoped stop and select a
materially different representative mechanism. The attained span 21
on the Dickson family and three directions against four required do
not increase from this check; arbitrary primitive fourfold classes and
the universal rational Hodge target remain unresolved.

## Saved reasoning before completion

For a map r:D -> M, Iacono's general first-order cocycle retains a
smooth section z of r^*T_M with
bar-partial z = dr(eta) - r^*(chi). Contract this equation with a
closed holomorphic two-form alpha on M, pulling the remaining slot
back to D. The proposed correction is the bar-partial of the
one-form alpha(z,dr(-)); it must be evaluated rather than set to zero.

For the relative incidence, use the actual universal family on
S_A^[3] x_A S_A. Check its constant marked class, including the
collision locus, by representing its codimension-two class as the
leading Chern character of its structure sheaf and retaining the
Chern--Weil transgression under a differentiable nilpotent
trivialization. Then check pullback, multiplication and fibre
integration in the same markings. This must establish filtration
compatibility, not merely naturality in the Artin algebra.

The period conclusion will be tested using the nonzero eigenvalue
1+theta and the injectivity of p^*. The blowdown and later punctured
residual arguments are not new targets of this step.

## Completed calculation

The full argument is incorporated into the existing proof of
[L043](../lemmas/L043-resolved-parameter-lift-retains-transverse-obstruction.md),
equations (7a)--(7d) and their period application. This outline is
preserved as the reasoning saved while that calculation was unfinished.

The contraction of the complete map cocycle has correction
bar-partial c_alpha(z), so the arbitrary map motion disappears in
H^1(Omega^1). The same calculation is applied to both f_A and p_A.
The relative universal complex supplies ch_2(O_Z_A) on the entire
product. Its differentiable nilpotent marking is constant by the
explicit Chern--Weil transgression, and its holomorphic character
lies in F^2. Cup product and surface integration therefore give the
constant marked incidence operator preserving F^2, including
collision fibres. The de Rham Cartan homotopy also makes the two
marked pullbacks constant.

The contraction derivative then gives
(1+theta)p^*(xi contracted with omega)
=(1+theta)p^*(kappa contracted with omega).
The scalar is nonzero, p^* is injective and contraction with omega
is an isomorphism on a K3. Hence xi=kappa without imposing NS or
RM preservation on xi in advance.

This establishes the previously unverified compatibility input;
it is a reproduction and specialization of known tools, not an
additional cycle or claimed new discovery. The argument's blowdown
and later punctured recovery are reused, not rechecked here. The
resolved-lift recipe remains stopped with three directions against
four required. The next mechanism is the rank-two higher-Chern
identity for a mixed terminal bundle, to be screened before work;
it is distinct from another deformation of this Hilbert-cube map
or a renewed factor-residue search. No calculation on that new
target is performed in this step.

## Mathlib

Coverage: **not checked** for the compatibility calculation. The named
Iacono and Fiorenza--Manetti statements in the prior assessment cover
the supporting cocycle and formal-period frameworks, not this full
incidence-specific application.
