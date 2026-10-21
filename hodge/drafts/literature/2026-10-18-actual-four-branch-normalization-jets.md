# Completed source comparison — four-preimage normalization length and nonlinear jets

TARGET: Assess coverage for determining how nonlinear normal jets affect the normalization-quotient length at an actual four-preimage collision with quaternionic tangent span two.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared the general subspace-arrangement regularity theorem, generic degree-two Hilbert-function results and curve-parametrization determinacy; reused the two three-branch assessments and ATTEMPTS/070--072; exact queries and inspected cases appear below.
SOURCE_EVIDENCE: Derksen--Sidman (2002), Theorems 1.2 and 2.1 and the complete Section 2 proof; Carlini--Catalisano--Geramita, arXiv:0909.3802v2, Theorem 3.2 with its proof and Remark 3.3; Greuel--Pfister, arXiv:2101.01784v1, Definition 7, Proposition 11 with full proof and Corollary 12; reused Li 5.2.3 and Stacks completion/length coverage.
COMPARISON: The general linear-arrangement bound and previously inspected complete-filtered tools support a bounded tail-and-jet specialization. Generic quadratic ranks and one-dimensional conductor determinacy cannot be imported for every quaternionic surface configuration. No inspected theorem directly gives the actual four-branch length or tangent-only determination.
GAP: Verify a uniform complete tail for the nonlinear restriction map, then compute its remaining finite-jet image with all normal coefficients retained; determine whether the resulting criterion is tangent-only. None of these specializations is proved in this review.
REASON: Essential tool coverage is accessible; proceed to one separate mathematical attempt after the supervisor's separate approval of this newly covered continuation. No source blocker requires another discovery search.
SCOPE: Conditional actual opposite image of L118/L120/L121, exactly four distinct preimages with quaternionic tangent span two in ambient quaternionic dimension 39; retain arbitrary nonlinear normal jets.
COVERED_TARGET: Determine a finite-jet formula for the normalization-quotient length at a four-preimage span-two collision, retaining arbitrary nonlinear normal jets.
LITERATURE_REASON: The saved gate requires comparison for the changed branch count, outside the three-branch assessment; general regularity and determinacy coverage had not been inspected for this target.

The main gap remains universal primitive rational Hodge realization.
L125's audited triple case gives a usable conditional local input but
leaves other multiplicities open. A four-preimage test is a concrete
extension of image-gluing bookkeeping, not a reopening of the stopped
minimal-defect or curvature mechanisms. Its possible downstream use is
understanding which local contributions can enter the global normalization
quotient. There is no proposed global exclusion or existence theorem.

Essential inputs for the proposed source comparison are L118's actual
quaternionic immersion, L120's finite normalization and L121's distinct
tangents. L122 and L125 are comparison cases only: their numerical
conclusions must not be reassigned to four branches. Retain the rank-two
locally free Omega-polystable F with integral c_1=0 and
ch_2=-14e_1-21e_2-tau_D on identical marked K3 factors, scale c=2lambda.
F existence and the occurrence and geometry of this collision remain
unproved. No simultaneous linearization may be assumed.

## Primary statements and proof cases

[Derksen--Sidman, *A sharp bound for the Castelnuovo--Mumford regularity
of subspace arrangements*, Advances in Mathematics 172 (2002),
151--157](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.10.pdf),
Theorem 2.1, printed p. 154, states that the intersection ideal of an
arrangement of d projective linear spaces is d-regular. No general-position
hypothesis is imposed. Theorem 1.2, p. 153, gives the equivalent ideal-sheaf
vanishing H^i(I_X(k))=0 for i>=1 and k+i>=d. Read both statements and
the complete proof through Proposition 2.2, pp. 154--156: induction on
linear-ideal height and ambient dimension, followed by the saturation
argument. These are imported tools, not a nonlinear-image theorem.
Over C, L121 supplies the pairwise-disjoint projectivized tangent
spaces needed for a restriction comparison. The later attempt must check
that comparison, the cutoff and the passage to complete nonlinear maps.
The sharpness example on p. 155 warns against reducing a uniform bound
without additional input; it does not decide this configuration's ranks.

[Carlini--Catalisano--Geramita, *Subspace arrangements, configurations
of linear spaces and the quadrics containing them*,
arXiv:0909.3802v2, 7 October 2009](https://arxiv.org/pdf/0909.3802v2),
Theorem 3.2, printed p. 15, assumes s>=2, m_1>=...>=m_s>=0,
m_1+m_2<n, and a **generic** configuration of projective m_i-planes.
It gives

\[
 \dim (I_\Lambda)_2=
 \max\left\{\binom{n+2}{2}-\sum_i\binom{m_i+2}{2},0\right\}.
\]

Read the statement, both proof cases (the cited Proposition 3.1 case
and adding generic points), and Remark 3.3 on four equal-dimensional
spaces, pp. 15--16. This is a comparison theorem, not an imported
rank for the retained configuration: distinct quaternionic tangents
are not an assertion of genericity. Proposition 3.1's longer incidence
proof was not independently checked and is not used as a mathematical
input. The generic result supplies neither nonlinear jet control nor
an all-configurations replacement. No generic rank is calculated here.

[Greuel--Pfister, *On Delta for parameterized Curve Singularities*,
arXiv:2101.01784v1, 5 January 2021](https://arxiv.org/pdf/2101.01784v1),
Definition 7, printed p. 5, uses a target product of one-variable rings
k[[t_i]]. Proposition 11, p. 7, assumes finite conductor colength c_phi
and gives (2c_phi-1) left determinacy, hence right-left determinacy.
Corollary 12 gives (4delta_phi-2) left determinacy when delta_phi is
finite. Read the full Proposition 11 proof: it uses the target's
principal-ideal property to factor the conductor and absorb high-order
errors by an ambient automorphism. This is essential one-dimensional
coverage. Our branches have rings C[[u_i,v_i]], so that proof and its
numerical thresholds are not transferred to surfaces. No general
right-left classification is needed for the narrower colength question.

Reuse the inspected Li, *Yanqi Lake Lectures on Algebra, Part 3*,
version 2026-07-05, Lemma 5.2.3, printed p. 53
([PDF p. 58](https://www.wwli.asia/downloads/YAlg3.pdf#page=58)):
a filtration-preserving map with complete source, Hausdorff exhaustive
target and surjective associated graded is surjective. Reuse
[Stacks 00MA](https://stacks.math.columbia.edu/tag/00MA),
[07N9](https://stacks.math.columbia.edu/tag/07N9),
[00MC](https://stacks.math.columbia.edu/tag/00MC),
[0C0S](https://stacks.math.columbia.edu/tag/0C0S) and
[02M1](https://stacks.math.columbia.edu/tag/02M1) for exact finite-module
completion, finite-algebra product completion, faithful flatness,
regular formal coordinates and flat-local length comparison.
Their hypotheses and complete relevant proofs are recorded in the
two three-branch assessments; those readings are reused unchanged.
Here L120 supplies a finite normalization with the four assumed
preimages and L118 supplies smooth branches and ambient germ.
Identifying the actual completed cokernel remains a specialization
to prove; no normalization-commutes-with-completion theorem is presumed.
Reuse [Stacks 0120](https://stacks.math.columbia.edu/tag/0120) as the
strictness warning. No reproof of these general tools is justified.

## Discovery, duplicates and recorded failures

Queries on 2026-10-18 included `Derksen Sidman subspace arrangements
regularity d subspaces theorem 2002 pdf`, `normalization length smooth
branches higher dimension nonlinear jets delta invariant tangent spaces
multiple point finite determinacy`, `smooth branches delta higher
singularity tangent`, `parametrization finite determinacy higher
dimensional Greuel Pfister`, `Greuel Pfister finite determinacy
parametrization reduced curve singularities theorem delta 2 delta`, and
`subspace arrangements normalization module Hilbert function disjoint
linear spaces regularity restriction map`.
Search snippets were leads only; the three primary texts above were
opened at their statements and indicated proof cases. No exact matching
four-surface theorem or counterexample was identified in this bounded
search; this establishes no novelty or tangent-invariance claim.

Local reads checked L118/L120/L121's exact hypotheses and conclusions,
L125's completion and filtered-tail proof ranges, L122's statement and
source scope, the two three-branch assessments, the prior
normalization-quotient comparison and ATTEMPTS/070--072.
The relevant scoped searches found no earlier four-branch calculation.
L125's length and quadratic-tail interpolation are not inputs for four
branches. ATTEMPTS/070's failed minimal-defect inference remains closed;
ATTEMPTS/071--072's curvature stops remain separate and are not reopened.
The earlier Leahy--Vitulli simultaneous-gluing and Greuel--Pfister
isolated-nonnormal finiteness readings are adequate background, not
a four-branch value. The inaccessible all-orders source is unnecessary
for this local-algebra continuation and was not retried.

## Separate bounded attempt and decision test

The sole covered continuation is the COVERED_TARGET above. Its first
test is whether the cited regularity and sheaf restriction tools give
surjectivity in every homogeneous degree at least three, followed by
Li's complete lifting theorem for ambient order three and branchwise
order three. This is a proposed cutoff to verify, not a result established
here. Check the exact four-factor completion diagram first. If this
tail check succeeds, compute the remaining jet map through degree two,
retaining every ambient coordinate and every allowed nonlinear branch
coefficient. In particular, do not omit the restrictions of ambient
linear forms vanishing on the tangent span. Do not replace the image
of the full jet map by the image of its associated graded without proof.

The output sought is a rigorous finite-jet colength criterion and a test
of whether its value is fixed by the tangents. A conditional formula
with unknown actual coefficients is useful even if it does not decide
the actual length. Continue only with a proved full-tail statement and
an explicitly identified finite map; otherwise preserve the failed
application or missing hypothesis and abandon this proposed cutoff.
Any smooth-branch model showing variation tests only the stated
local-algebra inference; it is not an actual F collision. Conversely,
neither algebraic feasibility nor jet independence constructs one.
Actual geodesy constraints may only be invoked with their own justified
input, not by silently prescribing actual jets.

No four-branch rank, length, finite-jet theorem or special nonlinear
comparison has been derived here. This is LITERATURE / REPRODUCTION /
EXPLORATION: usable coverage for a known-tool specialization, without
a mathematical advance or certified originality. The newly written
ready continuation receives separate supervisor approval next turn;
no research is invoked in this turn. F existence, collision occurrence,
global defect consequences, reconstruction, transport and universal
primitive Hodge realization remain unresolved. Full matching Mathlib
coverage remains not checked. Lemmas, scripts, PROOF.md and DAG.md are
unchanged.
