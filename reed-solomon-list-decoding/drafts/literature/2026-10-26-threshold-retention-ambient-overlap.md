# Threshold retention to ambient overlap — completed source comparison

TARGET: Assess whether two retained L030 families, each of size at least 1532496 and with distinct-support intersections at most 63, must have at least 18632 common ambient-star supports under L129's unchanged ambient hypotheses, without equal retained indicators.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches for cross-independent RS families, arbitrary relabelings, partial orthogonal-array isomorphisms, bounded upper intersections and random-permutation alteration found tools but no matching forcing theorem. Scoped local reads compared L030, L125, L129, ATTEMPTS/103–105 and the saved full-star, near-complete-star and boundary assessments; targeted working-record searches found no completed random-label alteration test.
SOURCE_EVIDENCE: Alon–Spencer, The Probabilistic Method, third edition (2008), Theorem 3.2.1 and full proof, printed pp. 29–30, plus Markov's inequality, Appendix A p. 308, were inspected in the primary book PDF. Reused prior primary inspections of König's matching theorem, Wang–Zhang Theorem 1.1, Borg–Feghali Theorem 1, and the finite-group stability theorem. Rechecked Camps-Moreno–Lau–López–Santos arXiv:2601.00122v1 Theorem IV.6, proof and Remark IV.10.
COMPARISON: Known rigidity assumes overlap and cannot force it from retention; matching bounds require a certified instance graph, and full-code automorphisms do not govern arbitrary actual-label bijections. Standard finite averaging and alteration cover a counterexample method, leaving exact conditional intersection counts and simultaneous retention/low-overlap verification as the instance-specific difference.
GAP: No forcing implication or counterexample is established. Test the admissible right-dummy branch by random relabeling and conflict deletion, accounting for eligible left/right sizes and every forbidden pair; certify both retained thresholds and ambient overlap on the same labeling.
REASON: Essential source comparison is complete for one bounded finite alteration specialization of this exact target. This mechanism does not require the high-overlap reduction and is materially different from ATTEMPTS/105; no essential unread source blocks the proposed test.
SCOPE: Exactly TARGET with q=137, unchanged T,H,K,a,b, arbitrary ambient bijections and left distinguished column 16. Approve one first-moment/counterexample test in the subcase where the right distinguished preimage is a dummy; consider deleting the left star before counting remaining cross conflicts. Do not add equal indicators, full retention, prescribed marginal laws, auxiliary packing or RS realization.

## Exact comparison and local reuse

The main gap remains arbitrary-center 67/68 agreement safety and the
finite bracket 955–957. This intermediate target asks whether retention
alone forces the ambient overlap needed by a rigidity-based route.
Even a positive overlap implication would leave unequal-indicator
transfer, lower-overlap cases, arbitrary laws, global extension and RS
realization unresolved. A counterexample would instead close this
particular proposed bridge, without refuting the main RS target.

The essential construction is L030, including its arbitrary-bijection
packing and finite permutation average (proof paragraphs “The packing
avoids the entire hyperedge incidence pattern” and “The pair moments
are exactly the old ones”). L125's distinguished-point projection
already records that each active label occurs in q^2 blocks and each
dummy label in none. Its full-law obstruction requires equal common
indicators; the proposed target explicitly removes that condition.
L129's hypotheses/conclusion likewise assume equal retained indicators
and exactly s=18632 retained common supports. Its accepted audit is
preserved. L126 and L129 are downstream comparisons, not unconditional
bounds for this target. The original right distinguished preimage is
unrestricted, so it must not silently be assumed active during review.

ATTEMPTS/103 preserves the failure of transferring an ambient budget to
a selected-family cap. ATTEMPTS/104 concerns complete pushforward laws;
ATTEMPTS/105 concerns identical full stars retained on both sides.
Neither supplies a test of independent deletion under unrelated labels.
Targeted searches of the two-core, full-star-thinning and boundary
working records found no completed first-moment alteration argument.
Unfinished drafts and all previous stop evidence remain intact.
No cross-notebook result is used.

## Newly inspected primary input

Noga Alon and Joel H. Spencer, *The Probabilistic Method*, third edition,
Wiley, 2008, ISBN 978-0-470-17020-5,
[primary book PDF](https://math.bme.hu/~gabor/oktatas/SztoM/AlonSpencer.ProbMethod3ed.pdf),
Theorem 3.2.1, printed pp. 29–30 (PDF pages 48–49).
For a finite graph with n vertices and nd/2 edges, d>=1, it gives
alpha(G)>=n/(2d). Its full proof samples vertices, averages vertex
count minus edge count, then removes one endpoint per surviving edge.
The deletion argument permits repeated endpoint choices. Appendix A,
printed p. 308 (PDF page 327), states Markov's inequality for any
nonnegative random variable; independence is not required there.
These are tools, not a theorem about balanced bipartite retention.
The specialization must justify conditional permutation probabilities,
per-side deletion losses and simultaneous overlap control. Import the
standard principles rather than reprove the general theorem; new
finite counting is necessary because its displayed bound does not
answer this instance.

The PDF's OCR substitutes some strict inequalities for weak ones;
the proof explicitly obtains “at least” the claimed independent-set
size. Do not infer a strict endpoint from the extracted theorem line.
No numerical specialization of this source was performed this turn.

## Reused theorem comparisons and a rechecked mismatch

The [full-star assessment](2026-10-25-two-core-full-star-thinning.md)
contains the previously inspected primary statements and proofs:
König, *Graphs and matrices*, authorized translation of the 1931 paper,
[arXiv:2009.03780v1](https://arxiv.org/pdf/2009.03780v1), unnumbered
main theorem p. 3 and graph proof pp. 1–2, identifies finite bipartite
matching and vertex-cover optima. It does not supply the conflict
edges or a balanced retained pair. An explicit deletion certificate
need not invoke matching/cover duality. Wang–Zhang,
[arXiv:1101.2257v1](https://arxiv.org/pdf/1101.2257v1), Theorem 1.1
p. 5, requires part-transitivity and primitive fragments, unverified
under arbitrary labels. Borg–Feghali,
[arXiv:2012.15356v2](https://arxiv.org/pdf/2012.15356v2), Theorem 1
p. 3, assumes lower cross-intersection, unlike the upper restriction
here. These are reused inspections, not newly read full proofs.

The [boundary assessment](2026-10-26-boundary-retained-star-obstruction.md)
and [rigidity assessment](2026-10-25-near-complete-common-star-rigidity.md)
record the prior finite-group stability and orthogonal-trade source
comparisons. Ben-Or–Coppersmith–Luby–Rubinfeld, *Non-Abelian
Homomorphism Testing, and Distributions Close to their Self-Convolutions*,
Random Structures & Algorithms 32(1) (2008), 49–70,
[Theorem 1, author preprint p. 3](https://people.csail.mit.edu/ronitt/papers/convd.pdf),
completes an already supplied full-group approximate homomorphism;
it does not derive overlap from retained family sizes. Four-column
trade existence on variable foundations likewise gives no fixed
six-column-star overlap-forcing statement. Keep the prior qualification
excluding the suspect extracted Theorem 4.5 from use. No trade theorem
or new stability application is needed for the approved alteration test.

Eduardo Camps-Moreno, Jun Bo Lau, Hiram H. López and Welington Santos,
*The permutation group of Reed-Solomon codes over arbitrary points*,
[arXiv:2601.00122v1, 31 December 2025](https://arxiv.org/html/2601.00122v1),
Theorem IV.6 and its proof: for 1<k<n-1, coordinate permutations
preserving the full RS code are exactly those induced by affine
permutations of its evaluation set. Remark IV.10 distinguishes this
from monomial and semilinear groups. These passages were rechecked;
no full-code-preservation hypothesis is available for two arbitrary
actual-label bijections. Thus even this exact automorphism conclusion
supplies no forcing implication, and it is not imported into a proof.

## Bounded discovery record

Queries on 26 October 2026 included `cross independent families Reed
Solomon codes arbitrary permutations stability intersection bipartite
graph`, `cross intersecting families bounded intersection upper bound
bipartite matching part transitive`, `orthogonal arrays large common
subcodes arbitrary coordinate permutations stability`, `"cross"
"Reed-Solomon" "families"`, `"orthogonal arrays" "intersection"
"isomorphic"`, `"linear" "MDS codes" "large" "intersection"
permutations stability`, `probabilistic method alteration delete edges
random permutation packing set systems theorem`, `Erdos Spencer
probabilistic method alteration independent set expected number edges
theorem pdf`, and `"random" "relabeling" "packings" "alteration"`.
The results repeated lower-cross-intersection theorems, OA trade papers
and full-code automorphism statements, and identified the primary
alteration source above. No exact forcing theorem or ready numerical
counterexample was located. Failed discovery is not a novelty claim.

Optional unread leads remain Dür's full automorphism paper and
Cavenagh–Stones near-automorphisms, already qualified in the saved
assessments. Neither is essential for the proposed finite averaging
test. A catalog record for Erdős–Spencer (1974) was opened, but no
result from that book is used. Lecture-note search hits were not used
as theorem evidence. No blocked publisher endpoint was retried.
Mathlib coverage for the complete target and proposed specialization
was not checked; that is not evidence of absence.

## One approved next test, with continuation and abandonment criteria

Keep exactly TARGET. First examine the admissible right-dummy subcase,
fixing the left labeling with b in column 16. Consider removing the
left blocks containing b, then sampling the right labeling uniformly
conditional on its chosen dummy mapping to a. This is a proposed
counterexample experiment, not an asserted retained construction.
Obtain exact finite expectations or rigorous upper bounds for all
remaining forbidden distinct cross pairs using the conditional
permutation action. Verify the ground-set size and both eligible
family counts; equal supports are permitted by the original target.
Use a deletion rule with a proved loss bound on each side, and check
ambient-star overlap for that same permitted labeling. If a joint
probability argument is needed, do not confuse separate expectations
with simultaneous existence. Dependence between conflict events
cannot be discarded without justification.

Continue only if an exact certificate proves both retained sizes
>=1532496, distinct-support intersections <=63, and common ambient-star
overlap <18632 for a permitted instance, or if a valid finite argument
instead proves the stated implication. A rational probabilistic
existence proof is acceptable when fully written; no random sample
alone is evidence of the universal claim or its negation. If the
first-moment deletion budget fails, record the actual bound and stop
this mechanism rather than assuming a favorable matching. Do not
extend automatically to other label models or reopen full-law coupling.
This review does not calculate the expectations, derive a new lemma,
or decide the implication. The next turn defaults to mathematics.
