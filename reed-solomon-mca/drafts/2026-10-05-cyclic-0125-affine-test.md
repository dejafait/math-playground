# Cyclic 0125 affine compatibility attempt

Approved target: decide the fixed cyclic 0125 family in the saved
2026-10-05 cyclic-0125 affine-compatibility assessment. Inputs are L010
(moment kernel and sparse-error syndrome) and the supports of L025.
Weights and distinct parameters remain arbitrary in F_(97^20).

The main gap is the possible sixteen-count equality, against allowable
count fifteen. Excluding this family would eliminate the new incidence
counterexample as a witness, without treating other families or ABF26.

Initial test: for each support A_t form its four-dimensional moment
subspace U_t in dimension eight, and a four-row annihilator R_t. If
u+gamma_t v lies in U_t, then the alternating coordinates
p_jk=u_j v_k-u_k v_j satisfy R_t p R_t^transpose=0. These are linear
necessary conditions independent of the unknown weights and parameters.
Compute their exact rank over F_97; a trivial kernel would exclude
every nonzero two-dimensional syndrome span over all extensions. A
nontrivial kernel alone is not a witness and would leave decomposability,
full weights and all L010 gates unresolved. A line through zero must
be treated separately using disjoint supports and moment invertibility.

This uses the approved direct support-subspace test, not L009's shifted
weight assumption. Continue if exact rank gives an obstruction or the
remaining kernel supports a bounded compatibility test; abandon a
sampling-only conclusion. The eight possible subgroup generators must
be covered, or the outcome restricted explicitly to those checked.

Completed: [L026](../lemmas/L026-cyclic-0125-affine-support-exclusion.md)
excludes the fixed family for all eight generators over every extension
of F_97. The exact necessary-condition matrices have rank 28, the
required full rank, and thirteen small coefficient blocks give explicit
nonzero minors. The one-dimensional syndrome case is impossible by
the disjoint pair and Vandermonde independence. Full proof and finite
arithmetic are canonical in L026 and its cited certificate. No actual
pencil exists to test at subsequent locator gates. Other families and
arbitrary labelings remain unresolved; a separate critical audit is the
continuation under the unchanged approved fixed-family target.
