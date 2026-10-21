# Exact Tate exclusion — audit checkpoint

Approved target: critically audit L043's exact-curve number-field
exclusion, using the unchanged IMPORT assessment of 2026-10-10.
Main gap: original finite B>=A; this audit only tests whether one
exact local curve can be globalized. Downstream use: accept or repair
the exact-curve stop before changing the realization mechanism.

Initial inspection: L043 uses L042 only to identify H, q and the
standard curve. Its torsion-degree computations are not additional
premises of transcendence. The parameter has the required strict norm;
arbitrary number-field embeddings fix Q, and characteristic zero
permits the stated j formula even at residue characteristic 3.
The remaining check is the full modular normalization, using the
already inspected primary identities rather than initial coefficients.
No defect found yet; final audit verdict remains pending this check.

Recovery choice to assess after this audit: compare exact-curve descent,
finite-torsion-field realization by local approximation, and a return
to native input membership. The first has the recorded transcendence
obstruction; the second can change the curve while testing concrete
finite Galois data; the third still lacks an identified native input.
No approximation or local-constancy theorem is approved or applied
here. Any changed target will be REVIEW_REQUIRED, separately assessed.

Completed: the independent audit passes. The complete normalization
is checked through the identical numerator and discriminant product,
not finite initial terms. Full reasoning and exact primary citations
are canonical in L043's separate audit section. The direct primary
check used Waldschmidt pp.1-3 and Milne pp.102-103; the earlier proof
coverage and Milne II.2.1 coverage were reused. No reproof of imported
theorems and no mathematical script were needed. No defect was found.

Recovery selects the second mechanism for source review: approximate
curve coefficients over Q(zeta_60) while retaining full finite torsion
Galois data over its specified completion H. This changes the curve,
unlike the stopped exact-isomorphism target. The scoped duplicate
search in drafts/literature/2026-10-10-*.md and ATTEMPTS/02*.md for
local constancy, Krasner, nearby, approximation and torsion-field-only
found the explicit uncovered scope, but no assessed replacement theorem.
No novelty or realization claim follows from that search. The native
input-membership option is deferred because no concrete source input
has been identified here. Earlier field exclusions remain preserved.
