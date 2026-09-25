# Lattice and reflection conventions

Coordinates on the infinite lattice are x in Z^4; physical positions are ax with a > 0. Direction 4 is Euclidean time. For each positively oriented nearest-neighbor edge (x,mu), U_(x,mu) lies in SU(2); reversal replaces U by its inverse. The trace below is the ordinary two-dimensional trace, without a factor 1/2.

In a finite region the Wilson weight is proportional to exp[(beta/2) sum_p Tr(U_p)] against product normalized Haar measure, with each elementary unoriented plaquette counted once using a chosen orientation. An additive constant in the action is immaterial. At beta = 0 the infinite-lattice measure is simply the countable product Haar measure. This is the infinite bare-coupling endpoint, not weak coupling. No interacting infinite-volume limiting argument is needed at this endpoint.

For a real smeared Euclidean field Phi, let theta reflect x_4 to -x_4, and write theta f = f composed with theta. For a polynomial F = P(Phi(f_1),...,Phi(f_k)), with real smooth compactly supported f_i in x_4 > 0, define F^theta = P(Phi(theta f_1),...,Phi(theta f_k)). The Osterwalder–Schrader form is

\[
\langle F,G\rangle_{\rm OS}=\mathbb E[\overline{F^\theta}G].
\]

When this form is positive semidefinite, divide by its null space and complete. The class of 1 is the vacuum. The proof in L001 computes this quotient directly; it does not invoke a reconstruction theorem while leaving that theorem's hypotheses unchecked.

## Named background and source coverage

Osterwalder and Schrader, *Axioms for Euclidean Green's Functions II*, Communications in Mathematical Physics 42 (1975), 281–305, [primary paper](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-42/issue-3/Axioms-for-Euclidean-Greens-functions-II-with-an-Appendix-by/cmp/1103899050.pdf), is the corrected reconstruction reference. Its abstract and contents identify the corrected equivalence and reconstruction results; their detailed hypotheses are not imported in this step. Reflection positivity alone is not the full reconstruction theorem.

Osterwalder and Seiler, *Gauge field theories on a lattice*, Annals of Physics 110 (1978), 440–471, [publisher source](https://www.sciencedirect.com/science/article/pii/0003491678900398), reports positivity and a positive self-adjoint transfer matrix for lattice approximations, and infinite-volume strong-coupling results. The abstract was checked. This is supporting lattice context, not a claim of continuum existence or a uniform continuum mass estimate; no result from this paper is an input to the calculation in L001.

Probability inputs used below are normalized Haar invariance, finite-product integration, Riemann sums, the moment–cumulant identity, and the named Lévy continuity theorem for characteristic functions. The specialized independence, scaling, and reflection arguments are written out in L001. No central limit theorem for dependent fields is assumed.

## Mathlib

Coverage of the full lattice-to-white-noise statement, reflection quotient, and supporting probability results: **not checked**. The named papers above are mathematical background references, not Mathlib matches.
