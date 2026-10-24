# Twisted rank-24 image — stable-summand index source assessment

TARGET: Test whether exact-h stable-summand Mukai-index constraints sharpen L153's conditional |Z|<=162 bound for the actual rank-24 M.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the 2026-10-07 tangent-index and 2026-10-10 larger-charge assessments; read L052's lattice proof, L147/L153's hypotheses and conclusions, L079's stable-Hom passage and ATTEMPTS/043/047/053; five external queries below found general K3 simple-index coverage but no inspected theorem evaluating this rank-24 nonzero-determinant optimization.
SOURCE_EVIDENCE: Huybrechts, Lectures on K3 Surfaces, author-hosted prepublication draft, Chapter 9 Sections 1.2–1.3 equations (1.2)–(1.4), Definitions 1.2/1.4 and Remark 1.5 pp. 169–170, Section 3.1 including (iii)–(iv) pp. 175–176 and Theorem 4.9 p. 182, freshly read; reuse Perego (2021) Propositions 3.9–3.12/3.15 pp. 36–38 with previously inspected proof, and L153's assessed HE application.
COMPARISON: The general simple-sheaf Mukai bound applies to each stable factor at the actual real h, with arbitrary rank and first class; it is stronger than the whole-bundle discriminant condition on a simple bundle, but polystable M need not be simple. No inspected source performs this data-specific optimization or supplies exact-h existence from numerical feasibility.
GAP: In a separate research turn specialize the sourced necessary conditions to all stable types and multiplicities in M, justify any finite search range or uniform optimization, and compare its complete bound with 162; no endpoint or improved bound is evaluated here.
REASON: Essential source scope now matches the unchanged proposed target; one bounded REPRODUCTION calculation is ready, importing general results without reproof and retaining reducibility, nonzero first classes and empty Z.
SCOPE: Same conditional equality F and preferred metric as L147/L152/L153; actual M has rank 24, c_1=-4k, ch_2=(|Z|-167)eta, k^2=-14 and exact h, with L052's retained perpendicular integral lattice Zk; no simplicity, self-duality or kernel existence is assumed.
LITERATURE_REASON: The startup REVIEW_REQUIRED gate concerns a new arbitrary-rank, nonzero-determinant summand optimization outside the completed Chern audit; reuse ready general index coverage and inspect its precise real-h scope rather than repeat the connection audit.

The main gap remains universal primitive rational Hodge realization.
A stronger necessary restriction on the same equality kernel could later
be compared with independent lower control. This proposal is one bounded
numerical feasibility test, not a claim that such lower control exists.
It does not reopen the completed connection audit or alter the twisting
metric. F and nonempty Z remain unproved; empty Z must remain allowed.

The 2026-10-23 proposal in step 497 made no summand calculation. This
2026-10-24 literature-only completion approves its unchanged target's
source scope, without deriving its mathematical verdict. No cross-notebook
input is used. L052, L147, L152 and L153 remain the essential local inputs.

## Inspected standard results and applicability

Daniel Huybrechts, *Lectures on K3 Surfaces*, author-hosted prepublication
draft, [Chapter 9 Sections 1.2–1.3, printed pp. 169–170](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=169):
equations (1.2)–(1.4) give chi(E)=2 rank(E)+ch_2(E),
v(E)=(rank(E),c_1(E),rank(E)+ch_2(E)) and
chi(E,F)=-<v(E),v(F)>. Section 1.3 and Remark 1.5 give, for a simple
sheaf, chi(E,E)=2-dim Ext^1(E,E)<=2, hence <v(E),v(E)> >= -2.
There is no primitivity or determinant-zero hypothesis.

[Section 3.1, printed pp. 175–176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175)
defines slope using a Kähler class and proves stable implies simple in
(iii), with dual stability in (iv). [Theorem 4.9 and the following
definition, p. 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182)
identify HE bundles with direct sums of stable bundles of the same slope.
Read the slope kernel/image argument and the complete simple-index
passage, not just a moduli-dimension formula. The general HE proof is
reused from the earlier assessments; no new analytic proof is needed.

Reuse [the larger-charge assessment](2026-10-10-larger-charge-orthogonal-image-test.md),
its arbitrary-rank index coverage, and [the flat-image assessment's
inspected parallel-morphism proof](2026-10-05-flat-transform-orthogonal-residual.md):
Arvid Perego, *Kobayashi–Hitchin corrispondence for twisted vector
bundles*, Complex Manifolds **8** (2021), 1–95,
[Propositions 3.9–3.12 and 3.15, pp. 36–38](https://unige.iris.cineca.it/retrieve/e268c4cd-97f6-a6b7-e053-3a05fe0adea1/10.1515_coma-2020-0107.pdf#page=36).
At equal zero Einstein functions the morphisms are parallel. Use ordinary
bundles, trivial cocycle and zero B-field. This reusable coverage permits
the usual distinct-stable-type Hom test and, with Serre duality and RR,
pairwise Ext indices. No fresh reopening of that source is claimed.

M is the ordinary bundle obtained by tensoring the kernel with an actual
line bundle; it is not a Brauer-twisted sheaf. L153 already supplies its
polystability at this very h. The stable factors must be treated as
locally free direct summands, with their own integral first classes.
Apply L052's exact perpendicular-lattice conclusion only after checking
each factor's zero slope. Repeated isomorphic factors remain possible;
the simple inequality belongs to a stable type, not to its multiplicity
sum or to all of M. No symmetric form on M is available, so orthogonal
partition rules from L079 must not be imported.

## Precisely covered numerical attempt

Allow every stable-type rank and positive multiplicity consistent with
total rank 24, and arbitrary integral first and second characters subject
to the actual total character. Covered constraints are the exact-h slope
and lattice condition, integral Chern data, simple self-Ext index,
distinct-type Hom/Serre-dual pairwise index, and the rank-one line
character identity. The usual section/dual-section test is also covered,
but its applicability must be justified for each nontrivial stable type;
no independent cohomology of M is assumed. Distinct types with identical
numerical characters must not be silently identified.

The separate calculation must give a uniform argument or prove all
search cutoffs from these necessary inequalities and character sums.
No arbitrary bound on individual first classes or partition sampling is
approved as exhaustive. At an alleged endpoint witness, check every
chosen constraint, including pairwise tests, and distinguish a formal
character assignment from actual stable bundles at h. Stable-sheaf
existence, a generic ample polarization, or primitivity is not required
to apply the simple-index obstruction and must not be assumed in reverse.
No new finite bound, partition or numerical witness is derived here.

## Discovery, overlap and failure comparison

Queries actually run:

- `K3 polystable vector bundle Mukai vector stable summands square minus two non primitive slope real Kahler`
- `K3 surface stable sheaf rank arbitrary first Chern class simple Euler pairing Mukai square -2`
- `"K3" "polystable" "discriminant" "summands" Mukai`
- `"K3" "rank 24" "Mukai" stable bundle`
- `"K3" "stable" "Mukai vector" "non-primitive" square -2 slope`

Search results also led to generic-polarization and Picard-rank-one
existence statements, including Coskun's author-hosted
*The cohomology of the general stable sheaf on a K3 surface*, Section 2.
Those results were discovery snippets only, not inspected theorem inputs
or exact-h existence coverage. They are nonessential for this necessary
index test. No novelty is inferred from failure to find this optimization.

ATTEMPTS/043 and /047 retain compatible stable higher-rank branches;
ATTEMPTS/053 retains repeated stable blocks. Their lesson is to preserve
all stable ranks and multiplicities and never infer existence from a
compatible index. They do not decide this different character with
nonzero determinant. The tangent-index and larger-charge assessments
supply reusable tools, not their old numerical verdicts. L153's full
discriminant and audited same-bundle/same-metric applicability stay fixed;
neither the connection audit nor a stopped orthogonal filter is reopened.

The eventual discriminating test is an exhaustive necessary bound strictly
below 162, or a complete compatible numerical witness at the current
endpoint showing that these selected constraints cannot improve it.
Any search must retain all stable-summand ranks and integral first classes,
and must justify exhaustiveness rather than sample partitions. Passing
numerical constraints would not construct M or F. If the scoped test gives
no improvement, stop this filter instead of repeating the whole-bundle
inequality. A failed essential applicability or completeness argument is
an explicit remaining gap, not permission to discard a branch.

Full matching Mathlib coverage is not checked; unknown availability is
not evidence of absence. This completed source comparison is
EXPLORATION / REPRODUCTION of known tools, with no mathematical advance
beyond the sources checked. It writes no lemma or mathematical script
and changes neither the argument nor its DAG. The exact TARGET is ready
for one separate mathematical calculation; further literature is not
needed unless a genuinely new essential hypothesis enters.
