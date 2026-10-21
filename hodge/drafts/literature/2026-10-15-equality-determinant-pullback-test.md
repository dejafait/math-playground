# Equality map — determinant pullback calculation coverage

TARGET: Compute the pulled-back determinant classes L_0 and L_1 for L097's finite map and test their ample-combination constraint on the full integral D.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed determinant-line source review of 2026-10-15; its exact general determinant, positivity and family-GRR statements cover this calculation. Local line-twist, jumping-cycle and gerbe stops do not evaluate these two classes.
SOURCE_EVIDENCE: Huybrechts–Lehn (1997), 8.1.1/8.1.4/8.1.5/8.1.9–8.1.12, pp. 178–185, and 8.3/8.3.1(ii), pp. 195–197, https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf ; Abe (2017), Section 10.1, pp. 151–152, https://doi.org/10.1017/nmj.2016.50 ; finite pullback: Stacks Lemma 30.17.2, https://stacks.math.columbia.edu/tag/0B5V . Inspected statements/proof cases are recorded in drafts/literature/2026-10-15-equality-determinant-line-positivity.md; direct source endpoints rechecked 2026-10-15.
COMPARISON: Known descent, positivity and GRR apply without primitivity, generic H, a universal sheaf or constant higher-cohomology ranks. Only their explicit evaluation for the retained full family and the ensuing ample-cone compatibility test remain.
GAP: Compute both first Chern classes with the determinant-of-alternating-pushforward convention, justify integral interpretation, and test the actual sufficiently-large-ell ample combination on B; compatibility gives no kernel-existence conclusion.
REASON: One bounded reproduction of the applicable published framework can now test this independent integral positivity mechanism. Reproving determinant descent or positivity is unnecessary; newly written ready coverage receives separate supervisor approval before mathematics.
SCOPE: L071/L093's conditional equality kernel on the identical marked K3 product, integral c_1=0 and ch_2=-14e_1-21e_2-tau_D; L096's finite possibly empty Z; L097's actual flat family and common very ample H with H.k=0; audited L098's finite classifying map and finite surjective reduced-image factor. Higher characters are only those forced by actual rank two in L071. L099 is unnecessary.

The universal main gap is primitive rational Hodge realization. The
intermediate target is a necessary integral ample-cone condition for
this equality kernel, potentially useful as an exclusion or as a
precise compatibility boundary before any construction attempt.
F existence, other representatives, transport and the universal target
remain independent gaps.

Use the canonical source review's notation b=[O_H], numerical
fibre class c, u_i=-2b^i+chi(c b^i)[O_x] and L_i=lambda(u_i).
Import the whole-space family formula and sufficiently-large-ell
positivity there. Verify applicability at the finite split set rather
than restrict the argument to the stable open. Compute via the actual
family; no virtual jumping cycle or moduli universal sheaf is needed.
Keep the full mixed tensor and its correspondence orientation, the
relative Todd factor and determinant sign. The book's general GRR
statement on K-theoretic pushforward is the cited input; constant
cohomology ranks of F tensor u_i are not assumed.

The continuation threshold is a fully evaluable constraint on the
actual allowed H and integral pullback. Test whether it is violated
or is compatible, accounting for the freedom to choose H in L097's
same stratum near h. Do not substitute positivity on the metric's
three-plane for a divisor-cone check or assume H is generic. If the
only condition is compatible, record an informative bounded negative
and stop this filter; no extra iteration on the same calculation is
justified. If a concrete incompatibility is found, document its exact
scope and leave separate critical audit pending. No result, value,
cone inclusion or family-specific pullback formula is established by
this assessment. Mathlib full matching coverage is not checked.

## Direct-source recovery check (2026-10-15)

The missing direct URLs in SOURCE_EVIDENCE are repaired. The linked
[primary book](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=192),
[Abe paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E99CFB15879252A08B4D71D09ACEA734/S0027763016000507a.pdf/semistable-sheaves-with-symmetric-c1-on-a-quadric-surface.pdf#page=66)
and [Stacks statement](https://stacks.math.columbia.edu/tag/0B5V)
resolve. Targeted checks located the book's whole-space descent,
fixed-determinant positivity and family-GRR statements at the cited
locations; the existing full source comparison is reused. No changed
hypothesis, new source conclusion or family-specific calculation is
claimed. This repair leaves SPECIALIZE and the exact target unchanged.

ATTEMPTS/064 remains a stop for the different universal-gerbe test.
Neither that stop nor the existing line-twist/jumping-cycle comparisons
evaluate these determinant pullbacks. No lemma or mathematical script
is changed. Full matching Mathlib coverage remains not checked.
