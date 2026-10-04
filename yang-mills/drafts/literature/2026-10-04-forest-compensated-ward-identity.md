# Forest-compensated nonlinear Ward identity — source assessment

TARGET: At fixed mesh, derive the boundary-pinned compensator that keeps L009's link variation on L003's rooted forest slice, and test its exact reduced-Haar Ward identity including the compensator divergence.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched maximal-tree/axial-gauge compensating transformations, rooted-forest Haar reduction, tree-gauge Ward and Schwinger-Dyson identities, and reduced derivative/divergence formulas; read the primary graph gauge-fixing and Hamiltonian derivative statements below. No inspected statement covers the exact pinned L009 generator.
SOURCE_EVIDENCE: Read Freidel–Livine https://arxiv.org/pdf/hep-th/0205268v2 sec. 2.1 (2.1)–(2.8), sec. 4.3 Theorem 3 and sec. 5.1–5.2 (5.3), Theorem 4; Ligterink–Walet–Bishop https://arxiv.org/pdf/hep-lat/0001028v1 sec. 3.2 (55)–(71); Schaden https://arxiv.org/pdf/hep-lat/9805020v3 sec. I pp. 2–4. Reused and rechecked Del Debbio–Patella–Rago https://arxiv.org/pdf/1306.1173 sec. 6 (6.1)–(6.11) against the earlier combined-response assessment.
COMPARISON: Known tree path maps, reduction of tree-link derivatives and compact Haar integration cover the mechanism. They do not state the compensator/divergence for the boundary-rooted forest and endpoint-averaged generator here. Freidel–Livine's unit Jacobian for changing trees and the translation paper's measure-preserving transformation cannot be assigned to this field-dependent variation without an applicability calculation.
GAP: Differentiate the cited path gauge-fixing map with pinned roots in L009's conventions, retain derivatives of every compensating factor, and compare the reduced divergence with L010's full-link insertion. L003's measure and L007's integration-by-parts identity are already available; no new general gauge-fixing theorem is needed.
REASON: Approve only the finite boundary/generator specialization needed to make forest-coordinate Ward derivatives usable in L011's interacting expansion. This completes the missing source comparison after L015's stopped global BRST route; it does not prove a new identity, ultraviolet bound or normalization cancellation.
SCOPE: SU(2), the unchanged TARGET at a fixed even N >= 2 satisfying L009's supported-stencil condition, transformations identity at every boundary vertex, L003's existing forest, positive bare coupling, and smooth gauge-invariant observables including L010's two probes at tau = 1/16. Only finite group-coordinate derivatives and compact integration are covered; continuum BRST, physical-boundary subtraction and mesh-uniform estimates are excluded.
COVERED_TARGET: At fixed mesh, compare the compensated reduced-Haar Ward insertion with L010's full-link insertion for the two gauge-invariant Wilson-flow probes, retaining all differentiated forest-path terms.
COVERED_TARGET: At fixed mesh, test the free linearization of the compensated forest-slice generator against L009's gauge-quotient Ward identity for L010's two Wilson-flow probes.

## Relevance, reuse and stopping test

The intermediate gap is a nonlinear Ward representation consistent with
the exact forest measure. Its plausible use is to evaluate derivatives in
L011's forest-coordinate expansion without discarding the effect of removed
tree links. The finite Ward functional itself is already covered by L007;
the required work is its explicit representation on the specified slice.
This review began with REVIEW_REQUIRED coverage and performs no derivation.

The whole overview and ID-only DAG were read before the relevant portions
of L003, L007 and L009–L011. L003 already proves normalized product Haar
reduction for this pinned forest. L007 already proves compact Haar
integration by parts for a field-dependent vector field. L009 already
proves smooth gauge covariance and the free quotient identity, and L010
already gives the nonzero nonlinear full-link divergence. Reproving these
inputs or merely renaming the Ward functional would be redundant. L011's
coordinate Haar-density correction remains distinct from its Ward insertion.

The old bulk-locality failure, L012's strong off-shell boundary-domain
failure and L015's global BRST normalization stop are preserved. Tree gauge
is a different finite prescription; it does not undo those obstructions.
The [same-day official target check](2026-10-04-compact-brst-gauge-fixing-normalization.md)
and [target audit](../../foundations/01-target-and-scope.md) are reused without
another browse of the unchanged Clay formulation.

The discriminating mathematical test is an explicit pinned compensator
that preserves every forest link, together with its full reduced-Haar
divergence and the resulting Ward identity for the existing smooth
gauge-invariant probes. Compare that insertion with the full-link one;
report any discrepancy and whether it is pointwise or only cancels after
integration. No equality or zero compensator contribution is established
here. Failure to preserve the pinned roots or to account for all path
derivatives stops the proposed formula. Success would justify using it for
the existing expansion, not repeated audits of an already exact identity.
Nonlocal forest paths alone do not refute the finite identity, but any later
claim of locality or a uniform bound would need separate evidence.

The achieved estimate remains the existing positive Gaussian coefficient.
No interacting bound is improved: the needed reflected error is still
<= c_box/2 along a specified coupling trajectory. Finite interacting
matching, physical-boundary remainders, continuum fields, full limiting
reflection positivity, infrared control and finite positive mass remain
unresolved. No complete candidate is present.

## Search and inspected primary statements

Queries on 2026-10-04 included:

- `lattice gauge theory maximal tree gauge Ward identity compensating gauge transformation Haar measure`
- `lattice axial gauge infinitesimal variation compensating gauge transformation divergence Ward identity`
- `maximal tree gauge fixing product Haar measure boundary rooted forest gauge theory`
- `lattice gauge theory gauge fixed Ward identities maximal tree compensating infinitesimal transformation`
- `"maximal tree" "divergence" "gauge"`
- `"tree gauge" "Ward"` and `"tree gauge" "Ward identity" gauge transformation`
- `"maximal tree" "Schwinger" "Dyson" gauge`

The primary texts below are the inspected comparisons. Unrelated chiral
axial-current identities and abstract-only results were not used as inputs.
A failed exact search supplies no originality claim.

**L. Freidel and E. R. Livine, *Spin Networks for Non-Compact Groups*,
[hep-th/0205268v2](https://arxiv.org/pdf/hep-th/0205268v2),
24 June 2002; J. Math. Phys. 44 (2003), 1322–1356.** Read section 2.1,
printed pp. 4–6, (2.1)–(2.8); section 4.3, pp. 18–21, especially
Theorem 3; sections 5.1–5.2, pp. 21–23, (5.3) and Theorem 4.
The path-product map sets tree links to identity and retains a residual
root conjugation. Theorem 3 gives unit Jacobian for changing the chosen
tree. Equation (5.3) reduces tree-link derivatives on invariant functions;
Theorem 4 states Hermiticity of the specified reduced Laplacians for h > 1.
These are supporting results, not a theorem for an arbitrary
field-dependent compensated generator. The paper's noncompact residual
quotient construction is unnecessary here. Multiple boundary roots fixed
to identity and L009's precise variation still require specialization;
L003 supplies the notebook's measure statement.

**N. E. Ligterink, N. R. Walet and R. F. Bishop, *Towards a Many-Body
Treatment of Hamiltonian Lattice SU(N) Gauge Theory*,
[hep-lat/0001028v1](https://arxiv.org/pdf/hep-lat/0001028v1),
25 January 2000.** Read section 3.2, printed pp. 10–14, (55)–(71).
Equations (56)–(57) define non-tree variables using endpoint tree paths;
(58)–(60) retain link derivatives acting on those paths. The discussion
after (71) explicitly retains the action of electric fields on links set
to identity. This directly supports retaining compensated path derivatives.
Its Hamiltonian setting and unpinned global root differ from the present
Euclidean forest. It does not compute L009's reduced divergence or a
physical-boundary remainder.

**M. Schaden, *Equivariant Gauge Fixing of SU(2) Lattice Gauge Theory*,
[hep-lat/9805020v3](https://arxiv.org/pdf/hep-lat/9805020v3),
21 October 1998; Phys. Rev. D 59, 014508.** Rechecked section I,
printed pp. 2–4, including (1) and the distinction between maximal-tree
reduction and normalizable covariant gauge fixing. This supports keeping
the proposed forest prescription separate from the stopped standard BRST
completion. No equivariant construction or later continuum claim is imported.

**L. Del Debbio, A. Patella and A. Rago, *Space-time symmetries and the
Yang–Mills gradient flow*,
[1306.1173v1](https://arxiv.org/pdf/1306.1173), 5 June 2013;
JHEP 11 (2013), 212.** Rechecked section 6, printed pp. 13–15,
(6.1)–(6.11), against the
[existing assessment](2026-09-26-current-target.md). Its particular clover
transformation is treated as measure preserving after (6.2); (6.3) and
(6.8) retain a lattice-breaking residual, and (6.11) describes flowed
probes at finite spacing. L009 uses a different endpoint-averaged,
transported generator, whose full Haar divergence is already nonzero in
L010. Thus its simplified Ward formula is supporting precedent, not an
import for this target. The paragraph before (6.9) additionally assumes
continuum translation restoration; no construction theorem is imported.

## Access and applicability boundaries

The arXiv record lists only v1 for 1306.1173. Requests for v2/v3 failed;
the linked v1 PDF was then read successfully. The CERN published-PDF
mirror returned a bot check. Neither is an essential source blocker,
because the relevant v1 statements and prior assessment are readable.
Search snippets for textbooks, theses and recent Hamiltonian work remain
unread leads and supply no theorem-level evidence here. No essential
unread source remains for the bounded finite specialization.

Import the cited path map and derivative-reduction machinery, and use
L003/L007 by citation. The remaining calculation must translate orientation
and root conventions, differentiate the map along the actual L009 field,
and retain its configuration dependence in the divergence. Unit Jacobian
under a change of tree is a different statement from zero divergence for
this flow. Ordinary Haar invariance under a fixed gauge transformation
also does not license dropping derivatives of a field-dependent one.
The source's residual global conjugation must not introduce an unpinned
boundary transformation into L003's prescription.

**SPECIALIZE** is justified by these explicit measure, root and generator
differences. The unchanged TARGET and the two bounded COVERED_TARGET
subcases are ready for mathematical attempts classified REPRODUCTION.
This source review is EXPLORATION / LITERATURE / NOVELTY_UNCHECKED:
it supplies a new comparison and an actionable specialization mandate,
not a completed compensator, mathematical advance or claim beyond the
checked literature. It spends no mathematical exploration turn.

## Mathlib

Coverage of the full pinned compensated Ward statement: **not checked**.
Coverage of supporting Haar integration, Lie derivatives and graph
gauge reduction: **not checked**. The named primary statements and direct
links above are literature references; no matching Mathlib theorem is asserted.
