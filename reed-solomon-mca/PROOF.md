# Reed–Solomon grand MCA challenge: argument overview

Incomplete. Status: [PROGRESS.md](PROGRESS.md). Sole dependency graph: [DAG.md](DAG.md). Full proofs and qualifications: lemmas/.

## Assembly and unresolved gap

The [source audit](foundations/01-target-and-source-audit.md) fixes rates/error target; the July ABF26 definition remains unread. The [pinned ArkLib event](foundations/02-pinned-affine-line-model.md) is a frozen comparison model, not an identification with the challenge.

L001's safe set is right-open; C001a gives a smooth-code crossing for a specified field. L002 shows why that witness does not refute an eventual assertion at sufficiently large field size. The interval stays 11/q–16/q; source definition and universal representation/extraction remain open.

## Partial results

At q=97^20 with an order-sixteen subgroup of F_97^* and fixed supports/parameter cell, incidence, kernel and chart exclusions cover only selected necessary equality patterns; none supplies a coding converse.

Audited L151 conditionally excludes the complete original L125 pair domain. Audited L152/C152a extract a disjoint pair for represented t=0 events without identifying a numeric pair. Audited L155/C155a identify the nine-dimensional common exterior kernel and its decomposable locus; audited L156/L157 retain zero/nonzero strata and shared representatives for one/two added rows, without evaluating an original quadruple. L158 rejects three specified constructions. Uniform twelve-row exclusion, all coding gates and arbitrary representation remain open; full scopes and earlier failures are canonical in the lemmas and history.

L159–L161 remain unaudited conditional leads, not premises. Audited L162 constructs an injective projective-line family for labels (35,522,477,566), refuting universal four-row finiteness. Audited L163 covers all 112 additions (72 empty, 40 precisely [1:94], none rank zero); audited L164 bounds additions by three through the shared label 27. L165 exhausts the four-row locus, including the coincident-line branch and both projective endpoints, so this seed cannot extend to twelve rows. Its separate critical audit remains pending. Other quadruples, extraction, coding realization and the challenge remain unresolved.

Audited L166/L167 refute marked extraction with degree-four completion. L168 excludes that one labeled completion by rank 21. L169 excludes every twelve-row linear degree-at-most-four family containing its numerical pair (237,570): a deficient-extension-envelope cover gives selected capacity at most eleven over every extension of F_97. All 300 spans and 12508 separate histories pass same-step independent checking; a separate critical audit is pending. C152a supplies no identification of this pair, so uniform exclusion remains open.

L170 prunes no cover (audit pending). L171 stops geometric emptiness for (0,51,98,177,318); audited L172 excludes it by scalar zero. L173 proves scalar zero for prefix (0,51,98), using L109 necessity and reused complete saved kernels over E/F_97 (audit pending). All 1665 obligations remain; no cover is pruned.

L174 specializes L010/L109 to exclude coordinate-axis lift planes on fixed S for twelve fully gated rows of degree at most four, over every extension of F_97. Full recovery certifies nonpersistence; twelve full directions and the separate weight-one axis require locator multiplicity 96 against degree at most 64. This reproduces the locator mechanism without importing L076's automatic fullness. Separate critical audit is pending. No arbitrary-plane reduction or cover pruning follows.

## Known traps checked

- An unsafe grid point and a real supremum do not give an attained maximum. Preserve field-size and endpoint qualifications.
- Count sums are not ordered coverage or measure/code realization; all extension kernels, zero branches, actual row predicates, locators and arbitrary-weight/chart hypotheses remain necessary.
- A finite replay under fixed supports is not an all-pair sweep, global bound or disproof of the original challenge. Do not rewrite original inputs to make an audit pass.
- Abstract pair extraction does not identify a particular labeled pair. L152 permits isolated labels and handles both the twelve-edge boundary and the projective-plane exception without assuming a plane embedding.
- In L155 quotient-kernel disjointness follows from the full intersection-dimension calculation and audited rank, not from literal support disjointness. Its mixed-wedge span is a linear space; C155a identifies only its decomposable locus. Its two selected rank-zero branches contradict injectivity on the opposite kernel, without using coding gates; other rows still need their own rank tests.
- L156 compares both factor images in the same actual third-row target, separates zero images before normalization, and rejects rank zero. Its affine fibers require choices and give no global product trivialization, simultaneous-row exclusion or scheme-theoretic assertion.
- L157 keeps the two row targets separate and uses joint images, not independent lifts. Relative image scalars must be nonzero; incompatible quotient vectors, empty projective kernels and finite-field empty fibers remain excluded. Its image-ratio scalar is not a recovered coding weight, and its parameter formulas provide no many-row exclusion.
- L159 bounds only planes having a coincident pair of kernel-intersection lines. Pairwise-distinct lines cannot be replaced by a common coordinate line; the three-row rational numerator need not have enough forced zeros to vanish.
- L160 bounds cross-ratios, not their fiber sizes. Its possible projective-line family has exact ranks one and cannot be discarded for having zero generator coefficients or being invisible to samples. A base-field exceptional parameter does not prove that an eligible quadruple realizes it.
- L161's three surviving polynomial pencils are necessary conditions only. Proportional evaluations within two coordinate pairs need not be proportional between the pairs; the failed exclusion threshold is retained. The small exact pencil certificate is not an all-quadruple rank census or an infinite-family construction.
- L162 verifies identities for two independent coefficient vectors and proves exact ranks and distinctness for every projective parameter, including both endpoints. Its algebraic-closure counterfamily refutes only universal four-row finiteness; finite-field samples, weight recovery and twelve-row compatibility are not substituted for the remaining challenge conditions.
- L163 retains every eligible label and all homogeneous coefficients. Divisibility and Bezout identities cover extension-field roots; direct minors cover infinity. L164 counts the fixed rows in every integer degree. L165 retains the coincident-line branch before normalization and both projective endpoints afterward; its exact basis/minors prove exhaustion over the algebraic closure. The cost-three dual has no hidden edge upper bounds or conflict multipliers. The resulting seven-row upper bound concerns this seed alone and asserts neither attainment nor coding realization.
- L167's labeling preserves incidence only. L168 is one completion. L169 bounds deficient descendants using their entire extension envelope, retains separate selection histories and optional closure members, and checks integer capacities. Its numerical pair has no symmetry-transfer or coding converse.
- L170 needs full residual degrees and B-inclusion, not equal spans alone. Acyclic representatives retain search obligations; capped relation counts give no uniform bound or coding realization.
- L174 uses an auxiliary chart only to contradict existence, retaining prescribed-chart gates in any coding application. Its extension-field bound counts thirteen selected directions, not all parameters of an infinite field. Full weights, distinctness and nonzero actual locators are established before multiplicity counting; other plane classes remain open.

## Historical overview

Historical context: [pre-compaction overview](history/2026-10-24-proof-overview-before-compaction.txt).
