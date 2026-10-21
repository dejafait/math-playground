# Linear sixteen-support family rigidity — cyclic construction comparison

TARGET: Determine whether every simple linear degree-four four-uniform family on sixteen vertices is isomorphic to L072's sixteen-support family, or exhibit a counterexample.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the October 12 classification/source-blocker assessments; new cyclic-configuration and modular-Golomb-ruler searches found an accessible primary construction and explicit four-mark ruler, recorded below.
SOURCE_EVIDENCE: Inspected Buratti–Stinson arXiv:2007.01908v2, definitions and Theorem 1.6 (pp. 1–2), Lemma 2.1 with its full proof (p. 5), and Table 1's k=4 rows (p. 6); also Davydov et al. arXiv:1203.0709v1, Definitions 1.1–1.2, Theorem 1.5 and Definition 3.3/equation (3.8).
COMPARISON: The sources cover cyclic incidence construction from the published ruler {0,1,4,6} at modulus sixteen; neither inspected theorem compares it with L072 under arbitrary vertex bijections.
GAP: Specialize the cited construction, retain simplicity and both degrees, and test nonisomorphism to L072 using a fully verified incidence invariant; no nonisomorphism or rigidity conclusion is established in this review.
REASON: Essential construction coverage is now accessible without the blocked classification or graph dataset; the remaining isomorphism comparison is a bounded mathematical specialization, not a new general construction or census.
SCOPE: Abstract families on sixteen vertices with sixteen distinct four-element blocks, degree four at each vertex and pairwise block intersections at most one; isomorphism permits arbitrary vertex bijections, not just cyclic H-label changes.

## Relevance and bounded test

The main local gap remains exclusion of sixteen, with the uniform
triangle twelve bound open on the current route. A positive rigidity
result could reduce the surviving support families to the already
studied L072 family; applying its moment exclusion would still require
exact applicability checks. A counterexample would rule out this
proposed combinatorial bridge and require further moment constraints.
Neither outcome by itself resolves the challenge qualifications.

Essential local inputs for motivation are audited L086 and the exact
L072 abstract family. L079's existing family exclusion is a prospective
downstream input only, not a premise in this abstract classification
test. No assumption that every abstract family admits actual weights,
moments or original parameters is allowed. No cross-notebook input is
proposed. This target has no rational-chart assumption.

Search the terminology linear symmetric (16_4) configuration, partial
linear space and affine-plane parallel-class deletion, and inspect
primary statements with exact parameters before deciding coverage.
Known broader configuration lists must be checked for the required
intersection convention. A counterexample needs explicit blocks and
a checkable isomorphism invariant, not a different presentation of
L072. A positive claim needs complete coverage, not a sampled census.
Do not claim novelty from an unsuccessful search.

This differs from ATTEMPTS/027: that failure rules out forcing a
nonlinear pair from balance and a triangle, whereas the new target
asks whether families already known to be linear are unique up to
isomorphism. ATTEMPTS/029 concerns one fixed field-label assignment
and gives no abstract classification. No fixed-label sweep is proposed.
Continue toward rigidity only if source comparison supports a concrete
complete proof route; a verified nonisomorphic family abandons this
bridge. No part of this target was tested or approved in the preceding audit turn.

## Completed source comparison (step 216)

The main gap and exact TARGET above are unchanged. This literature-only
step approves a concrete counterexample test within that target, without
performing it. No lemma, mathematical script, DAG row or argument in
PROOF.md changes. No complete solution or abstract counterexample is claimed.

### Primary construction and inspected hypotheses

Marco Buratti and Douglas R. Stinson, *New Results on Modular Golomb
Rulers, Optical Orthogonal Codes and Related Structures*,
[arXiv:2007.01908v2](https://arxiv.org/pdf/2007.01908v2), arXiv stamp
11 October 2020, manuscript date 13 October 2020; published in
*Ars Mathematica Contemporanea* 20(1) (2021), 1–27,
[DOI 10.26493/1855-3974.2374.9ff](https://doi.org/10.26493/1855-3974.2374.9ff).
The inspected manuscript defines a modular ruler by distinct ordered
differences modulo v. Configurations are set systems with fixed block
size, constant point degree and no repeated point pair. Theorem 1.6,
p. 2, states equivalence with cyclic symmetric configurations, without
proof. Lemma 2.1, p. 5, keeps a length-L ruler for v>=2L+1; its full proof
separates positive and negative residues. Table 1, p. 6, gives
(0,1,4,6) at v=13 and extends it for v>=14 with L=6.
Thus v=16 is covered. No small-order completeness census is needed.

Alexander A. Davydov, Giorgio Faina, Massimo Giulietti, Stefano Marcugini
and Fernanda Pambianco, *On constructions and parameters of symmetric
configurations v_k*, [arXiv:1203.0709v1](https://arxiv.org/pdf/1203.0709v1),
4 March 2012. Definitions 1.1–1.2, pp. 1–3, match the incidence and
ordered-difference conventions. Theorem 1.5(ii), p. 4, gives the
circulant-matrix characterization; Definition 3.3, p. 12, equation
(3.8), explicitly develops the blocks by adding each residue to the
ruler. Theorem 1.5(ii) is attributed to consequences of Gropp (1990),
Section 4, rather than an explicitly stated theorem there. Gropp's
original text was not inspected and is not asserted to have been read.

### Exactly what remains to specialize

The prospective block family is the sixteen translates of the published
four-mark ruler in Z/16Z. Applying the inspected construction requires
only its stated modulus and ruler hypotheses. A future canonical proof
should cite it, give the sixteen blocks or their exact translate formula,
and verify the local hypotheses explicitly. Reproving general cyclic
existence, optimality or enumeration is unnecessary. A finite difference
or incidence check is an applicability check, not a new construction.

The unproved difference is nonisomorphism to the exact L072 table under
arbitrary point bijections. Test the noncollinearity graph: vertices
are the sixteen points, and an edge joins a pair contained in no block.
Compare complete connected-component data or triangle counts for both
families. This is a proposed test, not a computed graph or an asserted
invariant difference. If no invariant separates them, do not call
different presentations a counterexample; use an exact isomorphism test
or record a failed bounded attempt. A verified difference abandons
uniqueness as the bridge to L079. No marked-triangle or RS realization
claim is included in this target. No additional source review is needed
for this exact specialization; a broader census or moment target is uncovered.

### Duplicate and failure comparison

Reused `2026-10-12-linear-four-support-structure.md` and
`2026-10-12-linear-support-complete-census.md` in this directory. The
nineteen-type statement remains a reported lead: original Betten–Betten
classification conventions and representatives remain unread. Do not
rerun persistent access failures or use nineteen as an oracle. The
independent cubic-graph reproduction remains parked; this test needs neither.

Read the exact L072 construction and L086 hypotheses/conclusion after
the supplied overview and DAG. ATTEMPTS/027 stops useful-pair forcing
from balance plus a triangle; ATTEMPTS/029 stops a fixed-label anchor
search. Neither settles abstract uniqueness. Narrow searches of those
assessments, corresponding histories and L025/L028 found no recorded
test of this ruler against L072. This is not a novelty claim.

L086 motivates the abstract test, retaining its audited finite inputs
when returning to actual equality. L079 is a prospective downstream
input restricted to L072. Arbitrary moment compatibility, field-labeling
exclusion, uniform triangle twelve and challenge qualifications remain
unresolved. No cross-notebook input is used. Mathlib coverage of the
comparison and construction was not checked; unknown is not absent.

### Search and access record

New queries included `"16_4" configurations cyclic`,
`"symmetric configurations" "16" "cyclic"`,
`"cyclic" "16" "configurations" "Golomb"`,
`"modular Golomb ruler" "16" "4"`,
`"On constructions and parameters of symmetric" configurations arxiv`,
and `"New results on modular Golomb rulers" arxiv`.
The two primary PDFs supplied inspectable text; their load-bearing
definitions, theorem statements, extension proof and k=4 rows were read.
Screenshot calls supplied no inspectable images and are not verification.
A dLib entry confirmed publication metadata only. A miscued unrelated
arXiv page supplied no evidence. Secondary summaries, search snippets,
and unread original Gropp/Betten–Betten texts are not imported evidence.

Outcome: ADVANCE in source coverage for a known construction and an
actionable specialization, not a mathematical novelty or verified
counterexample. Mathematical exploration usage in this step is zero.
