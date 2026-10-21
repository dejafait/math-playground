# Five-support uniform extension — ready specialization scope

TARGET: Prove L040's equality conclusion for every multiplicative subgroup shift and every admissible 59-core/private-singleton choice.
CHECKED: 2026-10-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The completed shift/core source comparison in 2026-10-08-five-support-shift-and-core-extension.md records the actual bounded queries, scoped duplicate search, preserved stops and unread automorphism leads; no inspected exact-match extension was found, and no originality inference is made.
SOURCE_EVIDENCE: Reuse the inspected AGL arXiv:2304.09445v3 Definition 2.5/Lemma 2.7, pp. 7–8 (https://arxiv.org/html/2304.09445v3#S2.SS3), ST arXiv:1911.01502v1 Lemma 4.3 common-root proof case, pp. 11–12 (https://arxiv.org/pdf/1911.01502v1), and primary Mathlib declarations at the immutable source URLs listed below. Both paper URLs resolved on 2026-10-09; the prior theorem/proof inspection is reused, not repeated. L040 supplies the separately audited fixed matrix input; no fresh certificate verification is claimed.
COMPARISON: Standard signed equality constraints, factor-theorem division and composition tools cover the algebra over both instance fields; their precise application to shifted labels and arbitrary 59-cores must still be written. Generic higher-order rank does not certify fixed labels; L031's arbitrary-core theorem has four messages only.
GAP: Establish signed-system transport for every s in H and row-wise necessity for every admissible C,W_i and every ambient-field tuple width, preserving strict degree and extra agreements; no proof of the extension or quantitative transfer is yet present.
REASON: Essential literature coverage is complete for this narrow specialization; a later REPRODUCTION proof attempt can use the audited unshifted rank without another source search or generic-rank reproof. The 2026-10-09 literature-only recovery supplies direct URLs and preserves the prior ready decision; the next invocation may attempt the specialization subject to the supervisor gate.
SCOPE: Exactly the universal statement below; no independent edge shifts, arbitrary label permutations, changed generator, general five-support theorem, family cap or list threshold conclusion.

## Exact statement to prove, not an established result

Use C001a's E=F_65537, F=F_(65537^28), H=<h> of order 1024,
h=19139, k=64 and any m>=1. Order the edges 12,13,14,15,23,24,25,
34,35,45 with indices r=0,...,9. For every common s in H set
U_ij=s{h^(2r),h^(2r+1)}. Choose any C subset H of size 59 disjoint
from those twenty points, and five pairwise disjoint singleton sets
W_i subset H disjoint from C and all U_ij. Put
S_i=C union W_i union the four U_ij incident to i.

The desired conclusion is that any five polynomial m-tuples P_i over F,
each row of strict degree less than 64, agreeing with one Y:H -> F^m
on their respective S_i, are equal as polynomial tuples. They need
not be pairwise distinct. Extra agreements are permitted. Neither
coefficients nor Y are required to descend to E. Core and private
choices are not required to arise by shifting L040's fixed choices.

## Sources, relevance and test

Full inspected theorem hypotheses, proof cases, precise citations,
source revisions, Mathlib qualification and duplicate/failure comparison
are in [the completed source assessment](2026-10-08-five-support-shift-and-core-extension.md),
sections “Completed primary comparison” and “Supporting algebra and
Mathlib coverage”. Reuse them without refreshing this unchanged scope.
The only reproof/application work needed is the specialization above;
do not reprove the imported algebra or generic/random full-rank results.

Essential local mathematical inputs are L040's audited unshifted rank,
C001a's instance and L031's signed-kernel/common-root methodology.
L034 is a transfer comparison only: its 60-core cap criterion cannot
be applied to this 59-core target. The main gap is arbitrary-center
67/68 safety, with 955<=t_star(m)<=957. A uniform prohibition could
provide an additional necessary support constraint in a later 59-core
family certificate. A sound transfer, useful cap and cross-core use
remain independent unproved steps; no boundary gain is assumed.

The discriminating test is a universal symbolic proof of the transformed
signed constraints and tuple necessity, or a valid counterconfiguration.
Check every disjointness and degree hypothesis, zero differences,
extension-field rows and the direction of variable substitution.
Do not infer rank invariance from an arbitrary labeling bijection or
from genericity. Reuse L040's audited certificate instead of repeating
its finite audit. No mathematical calculation or extension proof was
performed while preparing this assessment.

Retain the exclusion only after the universal argument succeeds;
otherwise preserve the specific failed obligation or counterconfiguration
and narrow or abandon this extension. No family-size bound, common-center
large list, 67/68 safety or ABF equivalence follows from this test alone.
Preserve ATTEMPTS/019–021,023–025. Expected classification of the later
attempt is REPRODUCTION of known tools, without a novelty claim.

## Direct-source recovery, 2026-10-09

This is a citation-format repair of the unchanged target, not a new
theorem comparison or mathematical advance. The previous assessment
contains the inspected hypotheses, full relevant proof cases, duplicate
check and recorded failures; that coverage is reused. Both direct paper
URLs in SOURCE_EVIDENCE resolved during this turn. No theorem proof was
re-audited and no new search or mathematical derivation was performed.

The supporting Mathlib source URLs from that inspection are:

- `eval_comp`, `comp_assoc`: [Eval/Defs.lean at 6be3d352cec3ceabd28bf85266d28646e02f1975](https://github.com/leanprover-community/mathlib4/blob/6be3d352cec3ceabd28bf85266d28646e02f1975/Mathlib/Algebra/Polynomial/Eval/Defs.lean).
- `comp_C_mul_X_coeff`, `comp_C_mul_X_eq_zero_iff`: [Eval/Degree.lean at 9e6b3aac99b624d10c84653ab9c5357283b9b3b8](https://github.com/leanprover-community/mathlib4/blob/9e6b3aac99b624d10c84653ab9c5357283b9b3b8/Mathlib/Algebra/Polynomial/Eval/Degree.lean).
- `natDegree_comp`, `natDegree_C_mul`: [Degree/Lemmas.lean at 6be3d352cec3ceabd28bf85266d28646e02f1975](https://github.com/leanprover-community/mathlib4/blob/6be3d352cec3ceabd28bf85266d28646e02f1975/Mathlib/Algebra/Polynomial/Degree/Lemmas.lean).
- `dvd_iff_isRoot`: [Div.lean at 9e6b3aac99b624d10c84653ab9c5357283b9b3b8](https://github.com/leanprover-community/mathlib4/blob/9e6b3aac99b624d10c84653ab9c5357283b9b3b8/Mathlib/Algebra/Polynomial/Div.lean).

These are supporting declarations, not a full matching five-support
theorem. Their hypotheses and zero/constant cases remain as recorded
in the completed source assessment. Full-library coverage is not checked.
The need for a later application proof, and every independent downstream
gap stated above, is unchanged.
