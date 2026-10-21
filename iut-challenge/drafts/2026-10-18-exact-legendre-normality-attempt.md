# Exact auxiliary Legendre normality attempt — step315

Completed bounded attempt; the initial working checkpoint below was
saved before completing the kernel calculation.
The invocation-start assessment is
`drafts/literature/2026-10-18-auxiliary-exact-legendre-field-galois.md`
(SPECIALIZE); the target and auxiliary witness are unchanged.

Main gap: original finite B>=A. Intermediate target: decide normality
of the actual G/Q, or isolate the missing full-kernel information.
A pass would close one independent initial-data prerequisite; a
failure would stop this exact field under that prerequisite.

Use L073,L074,L077,L078 and audited L079, with the same roots,
cross-residue D, s, t and embedding. Write K=Q(E_aux[2])=Q(t)
and k=K(zeta_60). The candidate finite Galois ambient field is
F_aux with square roots of all three unsigned root differences.
Its Galoisness must be justified by actual conjugation of generators.

Planned bounded test: compute the subgroup fixing the full G,
compare it with its actual ordered-root conjugates, and evaluate
L073's recorded Frobenius generator and all its powers. The
expected unresolved data are mixed radical/15-torsion actions;
no radical independence, full mod-two image, G=F', or reselection
is available. Continue only with a proved all-conjugation test or
a verified changing conjugation; otherwise record the missing
membership conditions without a normality verdict.

The complete proof is now canonical in
[L080](../lemmas/L080-exact-legendre-conjugate-fields-and-frobenius-nonseparation.md).
It gives the exact conjugate compositum and a normal-closure index
bound four, while normality requires index one. It also computes
all four elements of the recorded Frobenius cyclic image: every
ordered-model pointwise kernel has trivial intersection with it.
This is new negative evidence for a cyclic-subgroup separator test,
not a normality verdict or a result beyond the known methods used.
The actual radical-ratio memberships and mixed full kernel remain
unevaluated. The next separate review concerns this calculation;
no repeated search or new source coverage was claimed here.
