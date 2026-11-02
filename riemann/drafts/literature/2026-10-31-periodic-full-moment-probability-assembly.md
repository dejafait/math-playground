# Periodic full-moment probability assembly: source comparison

TARGET: Test whether L585's fourth carrier and L586's second completion can form positive periodic occupation probability laws satisfying all 147 L473 tolerances with phasewise jet norm at most ell^2 on one eventual ray.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready bounded-occupation, fourth-carrier audit and second-cone assessments; bounded added searches for interior moment representations with uniform weights, finite-mixture second/fourth scaling and periodic occupation support. Primary statements/proof cases and queries are recorded below; no exact assembly theorem was established.
SOURCE_EVIDENCE: Bayer--Teichmann math/0502473v2 Corollary 2, Remark 2 and pushforward proof pp.3--4; Blekherman--Fialkow 1804.04276v1 Proposition 2.1 and Corollary 2.2 with proofs pp.5--6; saved primary Rockafellar--Wets Theorem 2.33 pp.58--59 and Proposition 2.40 p.64 coverage reused; di Dio (2025), DOI 10.1007/s00013-025-02175-1, Definition 2.1, Theorems 2.4--2.5/proof inspected as comparison only.
COMPARISON: Known finite-representation and interior geometry cover the general tools. L585/L586 supply local fourth-carrier and second-cone inputs, but neither cubature nor a generic moment theorem supplies the coupled probability/support/fourth-error conclusion. Approve only this remaining uniform finite-mixture specialization, without a novelty claim or feasibility verdict.
GAP: Establish uniform second-completion weight and fourth cost, then choose nonnegative occupation probabilities and path amplitudes meeting all 147 tolerances and phasewise support on the same eventual real-H ray. L586's critical audit and arithmetic-source audits remain unresolved.
REASON: Essential source comparison for the unchanged target is complete; a bounded mathematical assembly test is justified. This literature-only step derives no assembly, scaling estimate, uniform representation theorem or new lemma.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED added coupled mass-one normalization, ell-dependent support and fourth errors beyond the ready second-cone scope; this review covers those added requirements and reuses unchanged coverage.
SCOPE: All six ordinary lag-one coordinates, 21 second and 126 fourth entries, including L473's four tighter same-height odd second bounds; finite positive mixtures of smooth periodic occupation laws, possibly with different periods, on one eventual ray of real H with ell=log H. Amplitude scaling acts on whole paths; no time dilation or arbitrary coordinate repair is assumed.

## Completed comparison, 31 October 2026

This is source approval for a future test of the exact TARGET, not an
assembly theorem or a critical audit of L586. The main gap is actual-Xi
all-degree positivity at unbounded heights. A bounded law meeting the
moment tolerances would close one feasibility interface; positive
clipped mass, selected-law realization and Xi transfer remain independent.
No lemma, mathematical script, DAG or argument overview changed.

### Exact interface, existing inputs and failures

Read L473 through (1)--(2), (6), (9), L585's hypotheses/conclusion (1),
and the full L586 proof to identify its actual representation guarantees.
Ordinary second errors are O(1), fourth errors O_m(ell^3); the four
same-height odd seconds require the two stated H^(-2/3) bounds with
ell^(-1) and ell^(-3). A generic O(1) correction in these four entries
fails the target. The constants and onset must be common to all real H
on one eventual ray. The norm bound applies at every phase of every
positive-weight trajectory, not just to averaged covariance or a
six-dimensional collection of atoms.

L585 supplies one fixed finite unit-jet fourth carrier and fixed finite
covariance R. L586 asserts restricted-frequency interiority and exact
finite representation of ell K-R, but expressly supplies no uniform
normalized weight or probability normalization. Its stronger interior
statement is relevant to controlling a family of representations;
that control must be proved during the mathematical attempt. Its
separate critical audit is pending. Bui--Hall Proposition 3's arithmetic
proof remains an imported, unaudited input through L473 (9).

Reuse the completed comparison in
`2026-10-31-bounded-periodic-occupation-moment-compensation.md`:
L578/L579 exclude their particular packet dictionaries; L581 excludes
the exact corrected law, with a defect smaller than the permitted
fourth error; L584 stops its absolute exceptional-budget sufficient
condition. None is a separator for this broader tolerance problem.
L473's arbitrary covariance map does not preserve ordinary derivative
relations. The new assembly must use entire paths rather than that map.
No failed route is reopened and no cross-notebook input is used.

### Primary representation results and their limitations

Christian Bayer and Josef Teichmann, *The proof of Tchakaloff's
Theorem*, Proc. Amer. Math. Soc. 134 (2006), 3035--3040,
[v2, Corollary 2, Remark 2 and proof, pp.3--4](https://arxiv.org/pdf/math/0502473v2#page=3),
assumes a positive measure concentrated on a measurable set and a
measurable finite observable map with integrable pushforward first
norm. It gives positive finite quadrature in that set; adding the
constant observable preserves finite mass. Read the pushforward/lift
proof and the lower-dimensional/supporting-plane cases of Theorem 1.
Thus mass must be included when using cubature for a probability law.
This theorem compresses existing feasibility; it does not establish
that the prescribed moment vector belongs to the supported path cone.
Its pushforward formulation is adequate background for amplitude
scaling and finite-mixture integration, which need only definitions
and finite algebra, not a new general theorem or reproof.

Grigoriy Blekherman and Lawrence Fialkow, *The core variety and
representing measures in the truncated moment problem*,
[v1, Proposition 2.1/Corollary 2.2, pp.5--6](https://arxiv.org/pdf/1804.04276v1#page=6),
works with a nonempty T1 space and a finite-dimensional space of real
Borel functions. Strict positivity on its nonzero nonnegative functions
characterizes interior membership in the finite evaluation cone.
Read the bipolar argument, perturbation by an evaluation, atom insertion
and Remark 2.4. These hypotheses refer to the actual function space,
not all ambient symmetric matrices. They cover L586's general source
input, not simultaneous second/fourth feasibility or a mass bound for
its varying normalized paths. No reproof is needed.

R. T. Rockafellar and R. J-B Wets, *Variational Analysis*, third printing
(2009), [Theorem 2.33, pp.58--59; Proposition 2.40, p.64](https://sites.math.washington.edu/~rtr/papers/rtr169-VarAnalysis-RockWets.pdf#page=66).
Reuse the primary passage/proof coverage in
`2026-10-31-l585-periodic-carrier-audit-scope.md` and
`2026-10-31-periodic-second-cone-interior.md`. These cover relative
interior in the affine hull, equality under convex closure, and the
proof's finite-simplex perturbation with continuous positive
barycentric coordinates. A finite-neighborhood representation is
therefore a standard convexity specialization to test, not grounds
for a new general lemma. The current author-PDF extraction retries
timed out; no new read of those passages is claimed. Saved coverage
is sufficient, so this is not an essential source blocker. It gives
no numerical path or weight constants for our assembly.

Philipp J. di Dio, *Absolutely continuous representing measures of
moment functionals: the general truncated case*, Archiv der Mathematik
125 (2025), 627--636,
[Definition 2.1, Theorems 2.4--2.5 and proof](https://doi.org/10.1007/s00013-025-02175-1),
was inspected as a stronger representation comparison. Theorem 2.5
assumes a finite-dimensional measurable function space, an interior
moment functional and a family approximating every point evaluation
on that space; it represents the functional using finitely many
members of that family. Its proof uses a simplicial representation
and perturbation. No periodic full-jet family with the required
approximation, support and quantitative errors has been supplied
here. The proof's simplicial assertion has not been independently
audited. This result is not imported or needed; smooth densities of
jet atoms would still not establish the required law of whole paths.
The cited earlier theorem behind it is an unread lead, not a premise.

### Bounded mathematical test now covered

Use L473 (1)--(2), (6), (9), L585 (1) and L586, with its audit status
explicit. Seek one construction from the fixed fourth carrier and
positive periodic second completion. The earlier rare-carrier
assessment already nominated amplitude ell^2 and weights ell^(-4)
for that component; their consequences are still to be checked in
the simultaneous assembly. Do not infer probability feasibility from
the two separate conic representations.

The next attempt must establish each of these obligations, without
assuming its desired conclusion:

- Control a family of second-completion representations uniformly in
  normalized weight and fourth cost, using L586's actual cone/span
  and the inspected finite-dimensional interior geometry. Pointwise
  finite attainment alone does not provide that control.
- Choose amplitudes and nonnegative occupation probabilities, prove
  that total mass is at most one before filling any deficit with the
  zero path, and prove the final support bound at every phase. Check
  that amplitude changes preserve ordinary derivative/lag relations.
- Compute all second entries, retaining the four tight signed bounds;
  compare all 126 fourth entries with ell^4 q_m and prove a uniform
  O_m(ell^3) remainder. Transfer to the actual reference integrals
  only via L473's qualified formulas. No time rescaling is permitted
  without rechecking the fixed lag and derivative coordinates.
- Choose fixed constants and a single eventual real-H ray for all
  requirements; do not substitute independent finite-H fits.

Continue if all four checks pass. A necessary lower bound on mass,
phasewise amplitude or fourth cost incompatible with these thresholds
rejects this scaling/completion mechanism; retain that obstruction and
select a materially changed mechanism. Failure of one selected finite
dictionary alone is narrower. If feasibility succeeds, report only
bounded periodic moment feasibility, with no implied positive clipping
or actual-Xi sign. No new construction or estimate is proved here.

### Search record, task balance and coverage

Added queries: `moment cone interior representing measures fixed nodes
neighborhood positive weights uniform bounded`; `finite mixture moment
scaling rare events second fourth moments probability normalization
bounded support`; `"periodic" "occupation" "moment" "mixtures" bounded
derivatives fourth`; and `"interior" "moment cone" "bounded" "weights"
representing measures neighborhood`. Search hits for general quadrature,
mixture approximation and polynomial optimization are unread leads
unless explicitly inspected above. No originality conclusion follows
from this bounded search. Bernard/Bochner/finite-LP comparisons remain
as previously assessed; none needs another import or repeated proof.
Matching Mathlib coverage for the full target remains unchecked.

Source coverage is now ready for the unchanged target. Next defaults
to one mathematical calculation/specialization, not another source
turn. No justified creative central-sign mechanism is identified by
this assembly review: the current task is standard mixture/cone
specialization, and the independent clipping/Xi-transfer gap blocks
calling it a creative sign mechanism. Preserve that distinction rather
than manufacturing a creative target to meet a scheduling aim.

## Invocation-start nomination (historical; superseded by comparison)

This is a future target, not a new approved mathematical result. The
main gap remains actual-Xi all-degree signs at unbounded heights. Its
plausible downstream use is a bounded derivative-consistent law
meeting the moment tolerances; positive clipped mass and Xi transfer
remain independent and are not requirements that can be silently
inferred from feasibility.

Essential local inputs are L473 (1)--(2), (6), (9); L585 (1); and
L586's exact finite second completion. Retain L473's imported arithmetic
proof qualifications, including Bui--Hall Proposition 3. L585 has an
application audit, while L586's new standard-theorem specialization
has not yet received a separate critical audit. Its finite covariance,
interior radius and onset are nonnumerical. No uniform choice of
completion nodes or normalized weights as ell varies has been proved.

The saved occupation assessment records why the L578/L579 packet
restrictions, L581 exact-law obstruction and L584 absolute-budget stop
do not by themselves decide this broader tolerance problem. Reuse
those comparisons instead of reopening the same stopped models.
An arbitrary linear correction of the six coordinates is still not
a derivative-preserving completion. No cross-notebook input is needed.

Continue only after the source comparison approves a bounded test
that controls nonnegative weights summing to one, support at every
phase, all second entries (especially the four tight ones), and all
fourth errors with constants on the same eventual real-H ray.
An unavoidable normalization/support/error conflict changes the
assembly mechanism; success would still leave clipped mass,
selected-law realization and actual-Xi transfer open. No scaling
construction, quantitative error estimate or new lemma is derived
in this nomination. Matching Mathlib coverage is unchecked.
