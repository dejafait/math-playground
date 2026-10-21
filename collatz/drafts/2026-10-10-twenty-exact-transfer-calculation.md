# Twenty-word exact-transfer calculation — work saved before arithmetic

Approved target: Assess whether the unchanged exact logarithmic transfer and L041 bounds exclude twenty-word closed concatenations.
Prior assessment: `drafts/literature/2026-10-10-twenty-exact-transfer-comparison.md` (SPECIALIZE).

Main gap: universal eventual descent. Intermediate target: one twenty-word
scalar full-ray exclusion-or-obstruction test, using L041, L044, L046 and
L048's assembly pattern. A successful contradiction could extend the
restricted exclusion; a surviving scalar length stops this comparison
without asserting simultaneous heights, parity realization or a cycle.
Universal entry, unrestricted counts/cycles, divergence and descent remain
independent gaps.

Relevant hypotheses and proof passages have been read: L041 through (11),
L044 through its exact transfer (5), L046's relaxed applicability passage,
and L048's complete proof and audit. The preapproved source comparison and
Attempts 021/022 were reused. No matching completed twenty-word calculation
was found in the targeted local search. Existing unfinished work is intact.

Retain actual closed words, each occurrence's J_i>=2,H_i>=3, independent
exact a_i>=0 congruent to 2 modulo 18, positive odd residue-20 junctions,
both shifted endpoint terms, primitive scaling, repetitions and coincident
junctions. No least-root or global-minimum assumption is imposed. Imports
retain their published computation/Rhin/Crandall qualifications; matching
Mathlib coverage is unknown.

Planned calculation: sum twenty occurrences of h_(i+1)<q h_i+b, with
q=3 delta^2/4, b=delta(3 delta-4)log(11/4)/4 and delta=log3/log2.
Keep L041's unchanged numerical prefix and length bounds. Use finite
integral-remainder rational logarithm enclosures to test a scalar length
above the necessary ray N>=338460000. This is not a parameter search.
Certify a full-ray contradiction or a surviving scalar length; do not move
to larger counts or sharpen any other input within this step.

## Completed bounded decision

The canonical argument is L049 in
`lemmas/L049-twenty-word-exact-transfer-scalar-obstruction.md`.
The exact scalar comparison survives at N=370000000, with certified RHS
strictly between 545558861 and 632443324, so the unchanged twenty-word
comparison stops. The full certificate is
`scripts/postspell-word-count/twenty-exact-transfer-certificate.json`;
29 exact checks pass without failures. Complete logarithm enclosures,
comparison operands and final strict RHS bounds were inspected with the
JSON inspector. No heights, parameters or actual cycle were constructed.

Completed NEGATIVE, RESEARCH/REPRODUCTION, actual task calculation.
This is an informative local obstruction, with no originality claim.
The separate critical audit is proposed in a REVIEW_REQUIRED assessment;
it has not been performed or approved here. Attempts 021/022 and L048
are preserved. The next audit validates this negative result rather than
reopening the stopped scalar comparison.
