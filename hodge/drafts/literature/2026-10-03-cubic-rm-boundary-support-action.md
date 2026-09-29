# Cubic-RM action of boundary-contained support maps — assessment

TARGET: Review whether every stable sheaf map f:S -> M_H(2,0,-1) with support contained in the collision locus induces only a scalar on T(S) when End_Hdg(T(S))=Q(zeta_7+zeta_7^{-1}).
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Dedicated searches covered the exact Mukai vector, boundary/collision actions, partition-stratum normalizations, regular and rational K3 self-maps, and totally real Hodge isometries; followed the stratum paper's primary normalization reference. The inspected statements cover useful ingredients, but no full boundary-action theorem was matched; queries and access limits are recorded below.
SOURCE_EVIDENCE: de Cataldo--Migliorini, The Douady Space of a Complex Surface, Advances in Mathematics 151 (2000), Lemma 3.3.1, printed p. 299, https://www.math.stonybrook.edu/~mde/MyPublishedPapers/DouadySpaceCplexSfceAdvances.pdf#page=18; their Journal of Algebra 251 (2002) paper, section 2, printed p. 827, https://www.math.stonybrook.edu/~mde/MyPublishedPapers/MotiveHilbSchJournOfAlg.pdf#page=4; Dedieu, arXiv:0704.3163v1, introduction 0.2, PDF pp. 1--2, https://arxiv.org/pdf/0704.3163v1#page=2; Huybrechts, 449-page author draft, Chapter 3, Lemmas 2.7 and 3.3 and section 3.5, PDF pp. 48,52,59, https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=59; Stacks Tags 0BXR, https://stacks.math.columbia.edu/tag/0BXR, and 0AB1, https://stacks.math.columbia.edu/tag/0AB1. Precise imported statements and scope are in foundations/07-collision-stratum-and-regular-k3-map-inputs.md.
COMPARISON: Known stratum-normalization and regular K3 self-morphism results supply a concrete mechanism for the proposed action bound; the totally real isometry restriction was already covered in L004. L039 and L040 supply the actual weighted-support convention. None of the inspected statements alone factors every prescribed boundary map or states the full normalized universal-sheaf scalarity claim.
GAP: Check descent through the collision-stratum normalization for a regular map from the smooth parameter K3, including triple collisions and images contained in smaller strata; then identify the actual weighted graph action and handle nondominant component maps. These are the scoped applicability differences, left unproved in this literature-only turn.
REASON: Import the known inputs instead of redoing normalization or K3 endomorphism theory. A separate specialization can decide whether boundary-contained maps can exceed the already attained scalar direction; a source normalization by itself is not that decision. The unchanged target is ready for that test, with no originality claim or non-scalar cycle supplied here.

## Scope and discriminating test

Keep S smooth projective complex, T(S) of rank eighteen and
its full Hodge endomorphism field the displayed totally real
cubic field. Keep H general in Yoshioka's sense, the fine
universal sheaf and the positive weighted-support convention
of L039. The collision locus in S^{(3)} consists of cycles
with a repeated point. The condition concerns the entire
image of the actual support morphism, not only the points
at which a generic distinct-support family degenerates.

This remains a proposed action bound, rather than an established
scalarity result. Continue with one specialization if the cited
normalizations can be applied to the actual parameter morphism
and the weighted-support convention agrees throughout the
boundary. A failure of regular descent or an additional action
term would reject that scalarity mechanism. A complete bound
would screen out this supply; a non-scalar example would justify
construction work. A lifting criterion alone decides neither.

The one-moving-point stop is retained. Generic distinct-point
maps and arbitrary correspondences lie outside this proposed
test. Its usefulness is local to the cubic-RM route; even a
successful bound would supply no general Hodge resolution
or new transverse surface. The available span is still 21 on
the Dickson family; its three attained RM deformation directions
remain short of four. The one-moving-point recipe has one
transcendental direction against three required by E. This
assessment improves the source inputs and supplies no new class.

## Closest inspected results and applicability

The precise known inputs are imported, without reproof, in
[the source note](../../foundations/07-collision-stratum-and-regular-k3-map-inputs.md).
The earlier [support-lifting assessment](2026-10-03-degree-three-support-stable-lifts.md)
is reused for Yoshioka's global model and the Hilbert--Chow
description; its target and assumptions have not changed.
That assessment does not cover the new action assertion.

The partition-normalization result concerns the **closure** of
a stratum, so it supplies an input that retains further
collisions. For the saved degree-three target, the relevant
partitions are (2,1) and (3). This is a theorem-scope comparison,
not a factorization of g or an action computation.

An essential application check remains: S need not dominate
the four-dimensional collision stratum. Do not apply a
normalization universal property requiring dominance without
checking it. The finite-normalization and finite-birational
isomorphism theorems give appropriate tools to examine the
pullback and its reduced component. The entire triple-point
image needs explicit treatment too. No such construction or
proof is carried out in this review.

Dedieu's regular self-morphism statement applies to arbitrary
projective complex K3 surfaces. It is the relevant input if
the component maps are regular. Results about very general
Picard-rank-one K3 surfaces or dominant **rational** maps cannot
be substituted on this rank-eighteen, Picard-rank-four RM locus.
Huybrechts' Hodge statements supply separate inputs for the
transcendental restriction and maps with smaller images;
their application to component maps remains to be written.

For the action comparison, retain f^*theta_v(0,t,0) and L039's
positive weighted cycle. A tautological class, raw ch_2,
unweighted reduced incidence or choice of punctual tangent
direction cannot simply be substituted for that convention.
Pointwise weighted support in L040 covers collisions already;
the remaining job is its application to the normalized strata,
not a reproof of the relative hull or Hilbert-cube model.

## Redundancy, continuation and later gaps

L038 stops a fixed one-moving-point family and hypothetical
repairs at two parameter points; it does not bound all boundary
images. L039 and L040 control support/action compatibility and
stable lifting, but do not establish the proposed scalarity.
L004 already establishes the totally real isometry limitation
under its hypotheses, with Huybrechts as the standard input.
Reuse that input rather than append another isometry proof.
The source note adds no duplicate notebook lemma or DAG node.

The action specialization is expected to be a **REPRODUCTION**
of known tools. SPECIALIZE is justified by the identified
descent, all-stratum and action-convention differences; it is
not a claim that the full action bound is new. A failed search
does not establish novelty. No unread source is essential to
the supporting statements imported here.

If the proposed bound is established, constructing an independent
non-scalar map with support outside the collision locus remains
open. Stable lifts, a new algebraic class on a transverse cubic-RM
surface and the universal Hodge target remain separate later
requirements. Even a positive answer to the scalarity test
would supply no general resolution. The exact saved target and
Next action text are preserved for the separate application turn.

## Search and reading record

Representative actual queries, including the exact-vector and
closest-theorem searches, were:

- `Hilbert scheme symmetric product surface stratum normalization partition de Cataldo Migliorini 2 1`
- `K3 surface surjective endomorphism automorphism nonconstant morphism self map`
- `K3 Hilbert cube exceptional divisor surface map real multiplication scalar transcendental cohomology`
- `de Cataldo Migliorini Chow groups motive Hilbert scheme surface normalization X lambda pdf`
- `Dedieu Severi varieties self rational maps K3 surfaces dominant morphism pdf`
- `"K3" "boundary" "Hilbert" "morphism" scalar`
- `"symmetric product" "normalization" "partition" "de Cataldo"`
- `"K3" "dominant endomorphism" automorphism "Dedieu"`
- `"finite birational" "normal" site:stacks.math.columbia.edu/tag`
- `"symmetric product" "collision locus" "normalization"`
- `de Cataldo Migliorini "Douady space" "normalization"`
- `"Hilbert" "cube" "K3" "exceptional" "morphism"`
- `"K3" "real multiplication" "regular" "endomorphism"`
- `"M_H(2,0,-1)" "K3" morphism`
- `"K3" "Hilbert" "collision" "transcendental"`
- `"K3" "boundary" "universal sheaf" "scalar"`

Read the published de Cataldo--Migliorini section 2, then followed
its reference [4] and read the earlier paper's section 3.3 and
Lemma 3.3.1 with proof, printed p. 299. The arXiv:math/0005249v1
HTML was also inspected to resolve the published PDF's garbled
notation; do not confuse its reference numbering with the
published paper. Read Dedieu's versioned introduction and
argument, Huybrechts' stated Hodge inputs, and both Stacks
statements and proofs. Only these portions, not the full books
or papers, were inspected.

Unread discovery leads: Fujimoto--Nakayama's 60-page RIMS paper
was located, but subsequent fetches timed out before its theorem
could be read; it is not used. Chen's arXiv:1008.1619 and broader
Hilbert-cube motive/contraction papers appeared as search leads;
their theorems were not inspected and support no conclusion here.
Forum answers and secondary aggregators were discovery aids only.
No essential source gap remains because the regular-morphism
input was read directly in Dedieu.

Web PDF text was sufficient for the stated inputs after the
HTML cross-check. Screenshot requests returned references without
viewable image data; no visual reading of those pages is claimed.
A local PDF download failed DNS resolution and was not evidence.

## Mathlib

Coverage: **not checked** for this target, the normalization,
regular K3 maps or supporting Hodge inputs. The named results
and direct links match the separate imported portions. Neither
a full Mathlib match nor absence from checked Mathlib sources is
asserted. They are supporting results, not a match for the full
universal-sheaf scalar-action claim.

## Source checkpoint during the literature-only review

Saved a partial source checkpoint in this assessment while
its decision was still REVIEW_REQUIRED, before following the
Douady-space reference and finishing the scope comparison.
Completion changes the decision to SPECIALIZE. No factorization,
action calculation, scalarity proof or new lemma was derived
between that checkpoint and this completed source assessment.
