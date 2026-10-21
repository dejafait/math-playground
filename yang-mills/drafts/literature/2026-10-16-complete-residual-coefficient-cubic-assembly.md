# Complete residual coefficient — completed scope review

TARGET: Determine whether the complete L011 order-g^2 residual coefficient has a finite a^3-scaled limit and whether that limit vanishes for both actual L010 probes.
CHECKED: 2026-10-16
DECISION: EXPLORE
SEARCH_EVIDENCE: Compared L011(6) with the canonical scope statements listed below; searched notebook-local nonradial/S4 matches and recorded failures, then searched flowed translation Ward and maximal-tree/axial-gauge one-loop terminology. No adequate theorem for the bare full coefficient or remaining nonradial action response was established; no novelty inference follows.
SOURCE_EVIDENCE: Reused the complete-quartic and original combined-response assessments; rechecked Del Debbio–Patella–Rago 1306.1173v1 sec. 6 (6.1)–(6.16), Luescher–Weisz 1101.0963v2 secs. 7.1–7.4 and 8.2/8.4, and Ramos–Sint 1508.05552v1 secs. 3.1/3.4. The Clay page and its linked 14-page Jaffe–Witten statement were accessible on 2026-10-16.
COMPARISON: The evaluated groups do not yet cover all of -kappa_0(f_(i,0),r_0,S_4-S_(4,rad)): L025 is a full fixed-mesh contraction, whereas L028 and L047 control selected plaquette/pairing classes. Renormalized flow/Ward statements do not supply the missing bare forest estimate. L019 forbids assigning termwise forest invariance.
GAP: Cubic-scale control and a signed limit for the complete nonradial quartic-action response remain missing, including transverse plaquettes and the interior axial no-internal-pair class; other excluded boundary classes require exact accounting. A complete-coefficient limit or its vanishing cannot presently be inferred by assembly.
REASON: This literature-only comparison identifies a concrete independently testable missing summand and approves a bounded attempt on it; no essential source is blocked. EXPLORE is coverage for research, not a theorem of finiteness, compensation or originality.
LITERATURE_REASON: Changed target and essential hypotheses: complete order-g^2 response, all cumulants and possible forest compensation, beyond the approved selected quartic target.
SCOPE: Proposed unchanged SU(2) relative cube, straight lower-rooted direction-1 forest, a=8/N, both L010 probes at tau=1/16, bare expansion before refinement; no interacting or continuum conclusion is included.
COVERED_TARGET: Determine whether L025's complete nonradial quartic-action response -kappa_0(f_(i,0),r_0,S_4-S_(4,rad)) has a finite a^3-scaled limit for both actual L010 probes.

## Main gap, intermediate target and decision

The main construction gap remains ultraviolet-uniform interacting
matching with reflected error <=c_box/2, followed by continuum axioms
and infrared control with finite positive mass. The supplied overview
and DAG were used before loading detailed proofs. The immediate target
is the full L011 coefficient at cubic scale. This review finds a missing
action input, so a numerical sum of the available coefficients would
not answer that target.

The next intermediate target is the complete nonradial quartic-action
response named in COVERED_TARGET. It is already defined and contracted
in L025(1)–(6); no new polynomial or lemma is introduced here. A bound,
limit, or informative obstruction for that exact summand would determine
whether full cubic assembly can proceed or requires joint compensation.
Even a completed cubic assembly would leave finer powers/logarithms,
finite matching, the interacting reflected estimate and the independent
continuum/infrared gaps unresolved.

Continue if a complete signed contraction estimate, a controlled
plaquette partition with a specific unresolved remainder, or a
discriminating obstruction changes that decision. The desired threshold
is a finite a^3-scaled limit for each i=3,6; O(a^-3) alone is partial
progress, not convergence. Do not infer zero from a frozen local test.
Abandon a proposed estimate if it needs bounded raw forest covariance,
termwise curvature transfer, or a smooth continuation through the upper
pin. An above-threshold absolute bound without a new signed mechanism
does not justify repeating the old route. This is not a global ban on
the nonradial response.

## Exact local coverage and overlap comparison

Read L011 in full, L019 through its compensation formulas and Gaussian
IBP, L025 through its full contraction and non-transfer qualification,
and L048 through the cubic color/pairing classification. Read the
hypotheses/conclusions of L023–L024, L028–L029, L047, L049, L054,
C057a, L058, L147–L148, L154, L180, L211 and C212i. L180's separate
audit scope and history/262 were also inspected. These are scope
comparisons, not recursive audits of all their analytic inputs.

The following rows refer to existing canonical statements; they are
not a dependency index or a new assembled formula.

| Part of L011(6) | Inspected coverage and limitation |
| --- | --- |
| kappa(f_(i,2),r_0) | C212i(2), transferred through C212h, states a zero cubic limit; its separate endpoint audit is in C212i section 6. Upstream bounds remain imported. |
| kappa(f_(i,1),r_1)-kappa(f_(i,1),r_0,S_3) | L211(4) states a zero cubic limit for this whole joint group. Splitting it into separate limits is unnecessary and unproved here. |
| kappa(f_(i,0),r_2) | L154(1)–(2) evaluates this whole quartic insertion; it has no extra outside factor 3. Its full heat and IEEE premises remain. |
| -kappa(f_(i,0),r_1,S_3) | L180(3), with its separate section 5 audit, concerns this complete single-action term; upstream analytic and heat premises remain. |
| -kappa(f_(i,0),r_0,M_2) | L148(1) gives O(a^-2) and a zero cubic limit in this forest. It is distinct from L010's divergence insertion. |
| -kappa(f_(i,0),r_0,S_(4,rad)) | L023's two pairing classes are both retained by L024(1)'s O(1) bound. This does not estimate the BCH/nonradial remainder. |
| -kappa(f_(i,0),r_0,S_4-S_(4,rad)) | L025(6) contracts both classes over all action plaquettes, but gives no cutoff estimate. L028(1) controls only the one-internal-pair class on axial plaquettes with four interior vertices. L047(3) concerns both upper axial classes. Transverse plaquettes, the interior axial no-internal-pair class and excluded boundary cases are not supplied with a complete cubic estimate by these results. |
| (1/2)kappa(f_(i,0),r_0,S_3,S_3) | L048(3) is the complete finite contraction. L058(1)–(2) defines the full top/other split; L147 concerns mixed and other/other contributions, while C057a(4) covers top/top at a^2 scale. These are different, retained regions, not extra corrections to be added twice. |

C057a explicitly defines its W as the upper nonradial quartic and its
C as the top/top cubic term. Its joint G=W+C overlaps L047's W;
C057a(4) already obtains C by subtraction. Use that separately
identified term if later assembling L048, not G and W independently.
L058's mixed cumulant already combines both ordered mixed regions;
there is no second factor 1/2. L147's O and M definitions concern
other/other and mixed regions only. L059's conditional quartic is
inside that same mixed response, not another contribution.

The present comparison does **not** add the interval endpoints, derive
a new scaled limit, or assert that the missing action input vanishes.
L019(2)–(5) locates forest compensation across complete jets; invariance
of the full coefficient cannot be assigned to a selected action term.
L011(14) also separates Gamma from the full Ward coefficient
Gamma+gamma^H. L010(8)–(9)'s finite divergence correction does not
replace any row of L011(6).

## Reused and rechecked primary sources

Reuse [the original combined-response assessment](2026-09-26-current-target.md),
[the forest assessment](2026-10-04-forest-compensated-ward-identity.md)
and [the complete-quartic assessment](2026-10-16-complete-quartic-probe-jet-scale.md).
Their exact theorem scope remains useful; the changed full-coefficient
comparison above is the reason for this additional literature turn.

**Del Debbio, Patella and Rago, *Space-time symmetries and the Yang–Mills
gradient flow*, JHEP 11 (2013) 212,
[1306.1173v1](https://arxiv.org/pdf/1306.1173v1), 5 June 2013.**
Rechecked sec. 6, printed pp. 13–16, (6.1)–(6.16). Its clover generator
is treated as measure preserving; (6.4)–(6.8) retain stress matching and
the residual. Translation restoration is an assumption before (6.9).
Equations (6.11)–(6.13) give a flow-boundary representation and finite
normalization for the full flowed-probe response. Choosing SU(2) is
allowed, but does not identify L010's transported endpoint generator,
its nonzero divergence, or the all-face boundary prescription. These
statements neither evaluate this bare coefficient nor bound an isolated
nonradial cumulant. No new specialization theorem is imported.

**Luescher and Weisz, *Perturbative analysis of the gradient flow in
non-abelian gauge theories*, JHEP 02 (2011) 051,
[1101.0963v2](https://arxiv.org/pdf/1101.0963v2), 10 February 2011.**
Rechecked secs. 7.1–7.4, printed pp. 20–23, (7.1)–(7.8), and secs.
8.2/8.4, pp. 24–25. Four-dimensional renormalization is assumed;
directed flow trees exclude bulk counterterms, and the BRS diagram
comparison excludes the two candidate flow-time-zero counterterms.
Positive-time gauge-invariant composites then need no extra
renormalization. The lattice extension is discussed as an expectation.
SU(2) is included by rank choice. The boundary in this argument is
flow time zero, not a cube face. This theorem does not give a bound
for the bare unflowed residual or for the missing forest action term;
reproving it would not close the identified gap.

**Ramos and Sint, *Symanzik improvement of the gradient flow in lattice
gauge theories*, [1508.05552v1](https://arxiv.org/pdf/1508.05552v1),
23 August 2015.** Rechecked secs. 3.1 and 3.4, printed pp. 7–9 and
14–15, (3.1)–(3.6), (3.43)–(3.45). The connected Symanzik expansion
retains action insertions as well as observable corrections, including
the flow-time-zero boundary. Total derivatives can be omitted in the
one-point energy expectation only with translation invariance; the
paper explicitly excludes that simplification for physical Dirichlet/
Neumann boundaries or higher correlations. Thus neither smooth-field
consistency nor an infinite-volume energy expectation supplies the
present weighted box estimate. The improvement expansion is not a
proved uniform bound for this bare forest cumulant.

**Current exact target.** On 2026-10-16 the [Clay page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)
and its Official Problem Description link were accessible. The latter
still returns Jaffe–Witten, [*Quantum Yang–Mills Theory*](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf),
14 pages. Rechecked sec. 4, printed p. 6, and footnote 2, p. 12:
all compact simple groups, nontrivial R^4 theory with the stated
axiomatic strength and finite positive mass; compactness alone is
insufficient. This repairs the prior assessment's failed refresh as
source access evidence only. The construction target and route are
unchanged; no claim about prize adjudication is made.

## Search, duplicates and recorded failures

New bounded queries on 2026-10-16 were:

- `"gradient flow" "translation Ward" "lattice" "power divergences"`
- `"Yang Mills" "maximal tree" "one loop" Ward quartic`
- `"lattice" "maximal tree gauge" "quartic" perturbation`
- `"Yang-Mills" "axial gauge" "Ward identities" lattice one loop power divergences`

Results on continuum axial-gauge self-energies (Capper–Leibbrandt,
Phys. Rev. D 25 (1982) 1002, and Lee–Milgram, JMP 26 (1985)) and
Wilsonian flow equations (Litim–Pawlowski hep-th/9802064) are screened
leads only: their theorem/proof passages were not inspected and are
not used for coverage. A Wilsonian flow is not automatically the
Wilson gradient flow of L010. Secondary summaries and matrix-model
maximal-tree matches are not theorem evidence. No failed search is
evidence of novelty. The accessible primary comparisons above suffice
for this bounded scope decision; no essential theorem is parked behind
an access blocker.

Notebook-local searches for nonradial/S4 terminology located L025,
its 2026-10-05 draft and the selected-class results above. No full
cubic-scale theorem for the missing response was established by that
audit. Read ATTEMPTS/009 and /011–013: isolated forest-density
interpretation, a bounded raw loop, a bounded ordered quadratic Wick
coefficient, and transfer of interior exterior estimates across the
upper jump all fail for their recorded reasons. L025's pinned-gradient
test separately blocks curvature-only transfer. Their canonical results
and unfinished work are preserved. They do not prove signed growth or
rule out a new complete contraction estimate.

## Approved bounded continuation and qualifications

The original TARGET is assessed, with the explicit missing-sector
COVERED_TARGET approved for the next mathematical turn. Begin from
L025(6) rather than redoing its finite Wick/BCH calculation. First seek
a signed all-plaquette cubic-scale bound or a precise remaining class;
an O(a^-3) bound may be useful even before a limit is proved. No new
mathematics is derived or approved as a result in this literature turn.

Essential inputs for that continuation are L008 L010 L011 L018 L019
L023 L024 L025 L026 L027 L028 L029 L045 L047. Preserve the exact
forest covariance, both connected pairing classes and their 24/48
factors, all colors, physical faces/end rows, constant axial modes,
upper jumps, both residual subtractions and complete heat sums.
Do not assume coverage of an excluded boundary row merely because its
bulk formula is known. Assume neither termwise forest invariance,
nonlinear quotient transfer, cubic compensation, separate convergence
nor a cutoff-uniform coupling expansion. L147 L148 L154 L180 L211
C212i and C057a are context for later full assembly, not permission
to count an incomplete selection as the whole coefficient.

All numerical signs later imported from L047/L147/L154/L180 retain
their cited analytic inputs, certified full spectral omissions, moment/
node/weight inputs and the stated IEEE binary64 addition/product/FMA,
no-overflow and underflow qualifications. Local audits are not recursive
upstream or processor/BLAS verification. The new target can first be
tested analytically without new numerical sign premises. Full matching
Mathlib coverage and supporting specialized forest/flow coverage are
**not checked**; no absent-theorem or novelty claim is made.
