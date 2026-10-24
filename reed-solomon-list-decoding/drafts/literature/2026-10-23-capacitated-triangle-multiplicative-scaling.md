# Multiplicative triangle-weight construction — completed source comparison

TARGET: Assess whether positive multiplicative edge scaling of the triangle weights c_i*c_j*c_h can meet L098's demands while respecting min(c_i,c_j,c_h), with zero-demand edges retained.
CHECKED: 2026-10-23
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched prescribed-marginal entropy scaling, structural zeros, generalized iterative scaling and capacity-constrained Bregman projections; inspected Csiszar–Shields (2004), Sections 3 and 5.1, and Benamou et al. arXiv:1412.5154v1 Sections 2 and 5.2; reused the previous triangle comparison and checked ATTEMPTS/081–082,088–092.
SOURCE_EVIDENCE: Primary URLs https://www.renyi.hu/~csiszar/Publications/Information_Theory_and_Statistics:_A_Tutorial.pdf and https://arxiv.org/pdf/1412.5154v1 ; Csiszar–Shields Theorems 3.1–3.2 and proofs pp.440–443, Remark 3.1 p.444, Theorems 5.1–5.2 and proofs pp.460–463; Benamou et al. v1 setup (2), Sections 2.1–2.2 pp.6–7 and capacity formulation (22)–(23) pp.21–22; local source normalization remains foundations/04,12,13.
COMPARISON: The inspected scaling characterization requires a nonempty marginal family and full feasible support for finite positive factors; convergence is conditional on feasibility. The inspected capacity algorithm imposes an additional inequality set. Neither result verifies L098's demands or proves that its unconstrained product scaling stays below the triangle capacities.
GAP: Positive scaling existence, invariant-factor specialization and quantitative capacity control remain unproved; two-distance dual nonseparation supplies none of these. A separate conditional equilateral-capacity test is proposed without presuming scaling existence.
REASON: Source evidence parks an automatic scaling/convergence import and redirects the proposal to a finite sufficient-capacity diagnostic with existing exact equilateral counts; no construction or nonexistence result is claimed.

SCOPE: One source comparison for a positive multiplicative construction on all actual distinct triangles; no new numerical solve, support scan, dual-support enlargement or restart of ATTEMPTS/082.
LITERATURE_REASON: Essential unread source coverage concerns multiplicative scaling with prescribed edge marginals and pointwise upper capacities, not the already assessed uncapacitated decomposition or two-weight box test.

The following proposal records the startup scope, not an established construction. Essential
local inputs are L021,L098,L105,L109 and foundations/04,12,13. Retain
N=floor(65537^28/2^128)+1, d_i=(N-2)c_i, both removed endpoint
repetitions, all actual source multiplicities and t-s. Edges with c_i=0
must stay present with zero demand and zero incident triangle weights.

The new idea is a positive primal ansatz based on the product of the
three pair coordinates, modified multiplicatively at edges. A source
must address marginals on graph edges of triangles, not merely vertex
marginals in an unrelated complete tensor. Arbitrary structural zeros,
actual orbit multiplicities, finite rather than asymptotic existence,
and the specific capacities are essential comparison points. An
existence theorem assuming exactly the sought feasible marginals would
be circular as a feasibility certificate. Plain convergence of an
iteration would also not certify the upper bounds.

Search precise terminology and stronger known results before approving
any local specialization. Reuse the prior triangle source comparison
for its inspected results; do not repeat L107's failed common scaling.
A theorem with checkable sufficient conditions and quantitative capacity
control would justify a separately gated mathematical target. If no
such coverage or concrete independently testable specialization emerges,
park this construction template with the source-level obstruction.

This could help decide the remaining fixed-pair scalar relaxation but
would not itself establish PSD, other pair feasibility, a packing or an
RS list. Boolean lower rows and source-lift compatibility must still be
checked before any full scalar claim. No scaling theorem, local lemma,
numerical result or novelty claim is established in this proposal.

Mathlib: full matching scaling and capacitated edge-marginal coverage
not checked; unknown availability is not evidence of absence.

## Step 410 working source checkpoint — preserved access record

The local comparison has retained L098's homogeneous equations, L105's
full scalar interval, L109's actual triangle box and ATTEMPTS/082's
stopped numerical prescription. No mathematical construction is being
run. Benamou–Carlier–Cuturi–Nenna–Peyré, arXiv:1412.5154v1,
Sections 2.1–2.2 and 5.2, is accessible: its general setup assumes a
nonempty constraint intersection, and its capacity treatment adds a
separate inequality projection. Exact entropy-scaling support/positivity
hypotheses are still being extracted from primary sources. MIT's
Csiszár scan is accessible to web retrieval but has no parsed text;
the NYU Stern mirror returned 404, and shell DNS access failed. These
are recorded access limitations, not mathematical nonexistence claims.

## Completed comparison — step 410

The main gap remains arbitrary-center safety at 67/68 agreements. The
reviewed intermediate target is the exact TARGET above. A successful
construction could settle a necessary fixed-pair upper-capacity/cardinality
relaxation, leaving the Boolean lower rows, source lift and PSD unresolved.
The review test was an applicable sufficient existence/capacity theorem,
or a concrete independently testable specialization. Only the latter is
proposed. No lemma or mathematical script was written or run.

### Inspected primary theorem passages

Imre Csiszár and Paul C. Shields, *Information Theory and Statistics:
A Tutorial*, Foundations and Trends in Communications and Information
Theory **1**(4) (2004), 417–528, DOI 10.1561/0100000004,
[author PDF](https://www.renyi.hu/~csiszar/Publications/Information_Theory_and_Statistics:_A_Tutorial.pdf):
Theorems 3.1–3.2, pp.440–443, start with a positive reference distribution
on a finite alphabet and a nonempty closed convex set, then a nonempty
linear family. The projection has the family's support. It lies in the
associated exponential family when that support is the whole alphabet;
in general only the closure is guaranteed. Remark 3.1, p.444, records
the restricted-support form. Theorem 5.1, pp.460–461, assumes a nonempty
intersection of linear families. Theorem 5.2, pp.462–463, uses nonnegative
features summing to one and their prescribed means; its convergence is
to the existing projection. Read the complete support, boundary-limit,
cyclic-projection and lifted-alphabet proof cases. These are conditional
scaling results, without a pointwise upper-capacity conclusion. This
author-written finite-alphabet treatment resolves the essential source
access issue; the unread original scans are not needed as premises.

Jean-David Benamou, Guillaume Carlier, Marco Cuturi, Luca Nenna and
Gabriel Peyré, *Iterative Bregman Projections for Regularized
Transportation Problems*, SIAM J. Sci. Comput. **37**(2) (2015),
A1111–A1138, DOI 10.1137/141000439; inspected
[arXiv:1412.5154v1](https://arxiv.org/pdf/1412.5154v1), 16 December
2014. Use the v1 PDF's printed pages, not the later HTML rendering date.
The setup (2), p.6, assumes a nonempty nonnegative intersection of
closed convex constraint sets. Sections 2.1–2.2, pp.6–7, distinguish
affine cyclic projections from Dykstra iterations for nonaffine sets.
Section 5.2, (22)–(23), pp.21–22, adds entrywise capacities to a
two-marginal transport problem; the capacity projection is componentwise
clipping. The complete setup, both iteration definitions and capacity
case were read. This describes optimization on an already feasible
intersection. It neither establishes our intersection's nonemptiness
nor transfers two-marginal transport automatically to overlapping
triangle-edge marginals. Its convergence references are not independently
audited here; no convergence theorem is used to claim local feasibility.

### Local applicability and qualifications

L109 supplies the actual unordered triangle box and edge incidence
problem Wz=d, with d_e=(N-2)c_i and upper b_T=min(c_i,c_j,c_h).
L105 supplies the remaining lower scalar interval. L098 supplies the
two endpoint repetitions and exact integer N. These are existing
results, not new deductions in this review. L021 fixes the exact c_i
through L098. L108 supplies actual equilateral triangles and a positive
third-support count at each permitted distance; it does not supply
capacities. Its proof and separate audit were checked for this scope.

For a future entropy application the alphabet would have to consist
of actual distinct triangles with positive base product. Null-demand
edges and their incident triangles remain zero in the full model, even
if eliminated from the positive reference alphabet. Normalizing total
mass and matching the edge-incidence features must be justified.
Full feasible support is a separate hypothesis from nonnegative cone
membership. A vertex-marginal tensor statement is insufficient.
Distance-dependent factors are a restriction requiring an argument;
the source does not identify entries with different t-s. Any formula
proposed on distances must still be assigned and checked on every
actual source class, retaining all multiplicities and repetitions.

The comparison does not conclude that positive scaling is impossible.
It stops inferring it, or its capacities, from generic scaling
convergence. Adding clipping is a different construction from the
unclipped product ansatz; repeated projections without their hypotheses
or a limiting residual plot give no certificate. A capacity-feasible
triangle weighting alone remains weaker than full scalar feasibility.

### Search and duplicate record

Queries included `iterative proportional fitting prescribed marginals
structural zeros exponential family convex support`, `Csiszar 1975
I divergence minimization linear constraints`, `entropy minimization
upper bounds capacities triangle fractional decomposition`, `generalized
iterative scaling upper bounds constraints`, `triangle edge scaling
marginals`, and `fractional triangle decomposition equilateral scaling`.
The precise triangle queries found no adequate matching theorem among
the inspected results; this is not an absence or novelty claim.

Reused `2026-10-21-unrestricted-scalar-triangle-comparison.md` for
Delcourt–Postle, Dross and Gruslys–Letzter instead of rereading those
papers. L107's failed common normalization is unchanged. Checked the
local statements/failures for L098,L105–L109 and ATTEMPTS/081–082,
088–092: no recorded product-scaling construction decides the new
question. ATTEMPTS/082's 200-sweep prescription stays parked.

Unread leads: Darroch–Ratcliff, Ann. Math. Statist. **43** (1972),
1470–1480, and Csiszár, Ann. Statist. **17** (1989), 1409–1413,
were located at NYU but their scans produced no parsed text. The
1975 MIT scan yielded indexed theorem text but no inspectable full
page text; do not treat that extract or its unseen proof as an import.
The publisher endpoint was unavailable. These leads are optional,
because the author treatment above covers the finite theorem needed
for this comparison. No persistent essential source blocker remains.

### Bounded continuation proposed for separate approval

The exact new target and its full scope are recorded in
`drafts/literature/2026-10-23-equilateral-scaling-capacity-test.md`.
It tests conditional upper-capacity control using equilateral
contributions, with distance-invariant positive factors and exact
L098 marginals assumed for that test only. It does not seek or assume
an actual scaling solution. No new bound has been derived here.
Continue this certificate mechanism only if it proves the capacity
ratio at most one on every permitted actual triangle. If its worst
allowance exceeds one, park this certificate without rejecting the
ansatz. This is independent of the old full-variable numerical solve.

Mathlib: matching entropy-scaling, structural-zero and capacitated
triangle-edge theorems not checked. No formalization is a premise of
this source comparison; unknown coverage is not evidence of absence.
