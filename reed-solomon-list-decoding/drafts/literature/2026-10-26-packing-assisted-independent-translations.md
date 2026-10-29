# Packing-assisted independent translations — completed source comparison

TARGET: Test whether cross-packing forces an L031 full-rank witness among independently translated left and right pairs for L131's fixed maps at retention threshold 1532496 per side.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Eleven bounded queries below compared translated polynomial graphs, code intersections, restricted cross-intersections and bipartite certificates; read the primary statements below and reused the completed mixed-core supersaturation comparison. Scoped duplicate/failure searches covered recent mixed-core assessments, ATTEMPTS/103–107 and history/512–514; no inspected result settles this fixed-map assertion.
SOURCE_EVIDENCE: Read Adriaensen arXiv:2512.07547v1 Definitions 1.4/1.8 and Theorems 1.7/1.11, printed pp. 2–4; Keevash–Sudakov, SIAM J. Discrete Math. 18(4) (2005), cross-intersection definition and Theorem 1.1, pp. 713–714. Reuse the recorded primary inspections of Konig arXiv:2009.03780v1, main theorem p. 3 and graph proof pp. 1–2, and AGL/ST signed-matrix/common-root inputs through audited L031/L131.
COMPARISON: Neither generic rank nor the inspected intersection results supplies fixed-label packing-to-rank expansion. L132's cover is not cross-packed, while L130's existential labeling need not be L131's maps. First check whether a sparse forbidden-pair matching already makes the fixed-map packing premise impossible; no instance matching has been computed.
GAP: Decide the fixed-map implication without assuming balanced packing exists. The first diagnostic tests the three prescribed coefficient-translation matchings below; insufficient matching size leaves both feasibility and independent-translation witness forcing unresolved.
REASON: Essential source comparison is complete for this bounded first diagnostic of the unchanged target. Matching certificates are standard; their instance-specific conflict counts are not supplied by the sources. No rank-expansion theorem, packed counterexample or novelty claim is established.
SCOPE: Exactly TARGET with all L031/L131 parameters/maps unchanged; cover only the first sparse conflict-matching diagnostic c=0,1,-1 below, with complete exact evidence. No q^6 search, other shifts, changed labels, arbitrary-map theorem or RS safety claim is covered.

LITERATURE_REASON: Invocation-start REVIEW_REQUIRED lacked coverage for independent left/right parameters with essential cross-packing. Reuse the ready signed-rank and universal-supersaturation comparisons; add only the missing intersection/certificate comparison.

## Main gap and exact scope

Keep L131's maps, cores, fields, T and r=Z-16 unchanged. For independent
f,g in Q, consider the ordered supports C union sigma(B_f),
C union sigma(B_(f+r)), C' union sigma'(B_g), C' union sigma'(B_(g+r)).
The proposed retained sets A_L,A_R each have at least 1532496 indices;
their associated distinct supports must jointly have intersections at
most 63. Ask whether some f,f+r in A_L and g,g+r in A_R give precisely
L031's complete incidence pattern and signed rank twelve at the actual
labels. This is a proposed question, not a result or a promised algorithm.

Essential existing inputs are L030's graph family, L031's exact signed
criterion, L131's complete fixed maps and L132's synchronized-cover
obstruction. L130 and ATTEMPTS/106 remain warnings against recovering
high star overlap from retention. ATTEMPTS/107 closes the diagonal
retention-only test. No cross-notebook input is proposed.

The main gap remains arbitrary-center 67/68 safety and the bracket
955–957. A nonvacuous fixed-map forcing result could give a
label-sensitive common-center restriction beyond L030's local packings.
Arbitrary maps and transfer to a global list cap remain independent
gaps. Proving that these fixed maps admit no packed threshold pair
would instead close this test instance before rank expansion; that
would establish neither nonvacuous expansion nor a universal cap.

## Primary comparison and literature reuse

Reuse `2026-10-26-mixed-core-rank-supersaturation.md`: its inspected
removal, sparse supersaturation and Frankl–Rodl-type statements lack
the finite extremal premise or actual-label encoding needed here.
The signed framework remains Alrabiah–Guruswami–Li,
[arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3), Definition 2.5,
Lemma 2.7 and proof, printed pp. 7–8, and Shangguan–Tamo,
[arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1), Lemma 4.3's
common-root division case, pp. 11–12. Audited L031/L131 already justify
the pinned fields, actual consecutive labels and every m>=1. No rank
specialization or reproof is needed for the first diagnostic. Generic
or random-domain rank does not certify expansion through these maps.

Sam Adriaensen, *Intersection problems for linear codes and polynomials
over finite fields*, [arXiv:2512.07547v1](https://arxiv.org/pdf/2512.07547v1),
8 December 2025, Theorem 1.7, printed p. 3: for each integer k>=3 there
is sigma_k such that for every prime power q an intersecting family of
homogeneous bivariate degree-k polynomials of size at least
q^k/sqrt(2)+sigma_k q^(k-1) is contained in a star. Definitions 1.4/1.8,
pp. 2–3, require lower pairwise agreement in one incidence structure;
our condition is an upper cross-intersection restriction between two
labelings, and the auxiliary degree is two. The complete Theorem 1.11,
p. 4, was also read; its asymptotic projective-code-family hypotheses
and intersecting-family conclusion do not supply this finite assertion.
No theorem is imported or reproved. Its Result 1.2 cites quadratic
stability results; those are secondary leads here, not inspected inputs.

Peter Keevash and Benny Sudakov, *Set systems with restricted
cross-intersections and the minimum rank of inclusion matrices*,
SIAM J. Discrete Math. 18(4) (2005), 713–727,
DOI [10.1137/S0895480103434634](https://doi.org/10.1137/S0895480103434634),
[author PDF](https://people.maths.ox.ac.uk/keevash/papers/cross-intersections-journal.pdf),
Theorem 1.1, p. 714: for |L|=s, n>100s^2 log(s+1), and uniform
L-cross-intersecting systems A_1,...,A_k on [n], their total size is at
most max{k binom(n,s),binom(n,floor(n/2))}. The definition on
pp. 713–714 permits equal sets across families and constrains distinct
cross pairs. On H, L={60,61,62,63} fails its displayed size hypothesis
at n=1024. Its full-layer conclusion also supplies no threshold within
L030's families. This theorem is excluded, not applied or reproved;
no proof case is needed for either excluded application above.

For the certificate method reuse
`2026-10-25-two-core-full-star-thinning.md` and
`2026-10-26-threshold-retention-ambient-overlap.md`: Denes Konig,
*Graphs and matrices*, authorized translation of the 1931 paper,
[arXiv:2009.03780v1](https://arxiv.org/pdf/2009.03780v1), unnumbered
main theorem p. 3 and complete graph proof pp. 1–2. In a finite
bipartite graph the maximum matching size equals the minimum
vertex-cover size. The recorded primary proof covers the augmenting
path and endpoint cases without regularity assumptions. An explicit
matching uses only disjoint-edge counting, with no reproof of duality.
A sum bound can exclude simultaneous lower thresholds; an optimum
sum alone does not construct a balanced retained pair.

## Search, duplicate and failure evidence

Queries on 2026-10-26, used for discovery rather than theorem evidence:

- `Reed Solomon agreement hypergraph fixed evaluation points translated polynomial graph cross intersection full rank`
- `cross intersecting Reed Solomon codes polynomial graphs families forbidden agreements`
- `bipartite independence number maximum matching weighted vertex cover forbidden intersections polynomial graphs`
- `"Intersection problems for linear codes and polynomials over finite fields"`
- `"cross-intersecting" "polynomials" finite field`
- `"Reed-Solomon" "cross" "intersecting"`
- `"bipartite" "holes" "mixing lemma" expander`
- `"Reed Solomon" "independent" "translations" "intersection"`
- `"polynomial graphs" "cross" "packing"`
- `"signed" "intersection matrix" "supersaturation"`
- `"Reed-Solomon" "forbidden" "four" "rank"`

Searches found the two primary comparisons above, graph matching
references and unrelated translation/cycle-packing hits. Agreement-test,
affine-subspace intersection and recent deep-hole/MCA hits were not
inspected as theorem inputs and supply no coverage. No conclusion is
drawn from snippets or absence of matches. There is no essential access
blocker for this test. The unavailable July ABF comparison remains the
pinned model's existing qualification.

Read the complete L131 construction, relevant L030/L031 proof passages,
L132's complete symbolic cover and ATTEMPTS/106–107; scoped searches
compared recent mixed-core assessments, ATTEMPTS/103–107 and
history/512–514. L132 does not certify cross-packing. The prior
full-star matching uses rigidity hypotheses absent here. L130 chooses
a right labeling, so it gives no retained-size certificate for L131's
fixed map. No duplicate of the three-shift conflict diagnostic was
found in these records. All stops and unfinished L129 work are preserved.

## Bounded first diagnostic and continuation test

Keep the exact target. Before seeking rank expansion, test whether
its fixed-map packing premise is already empty using just three
candidate correspondences g=f+c, c=0,1,-1 in F_137. For each c,
enumerate Q once and compare the original actual supports
C union sigma(B_f) and C' union sigma'(B_(f+c)). Retain a pair only
when its supports are distinct and intersect in more than 63 points.
Save every qualifying pair and its exact intersection, account for
all nonqualifying pairs, and verify disjoint tagged endpoints using
the coefficient-translation permutation. No translation invariance
of actual-label conflicts or rank may be assumed.

Seek a matching larger than twice the allowed deletion budget 1038857.
Justify this stopping threshold by the cited disjoint-edge principle
in the research proof and report actual/required integers. This is a
proposed sufficient certificate, not a computed matching-size claim.
It uses three linear-sized lists rather than q^6 cross comparisons.
Success would establish the fixed-map implication only vacuously:
no threshold packed pair exists. Abandon these maps as a nonvacuous
rank-expansion example in that case; do not infer an arbitrary-map cap.

If no matching reaches the threshold, stop this diagnostic and save
complete counts. That is inconclusive about both balanced packing and
rank forcing, not a counterexample. Other shifts or a rank-sensitive
rectangle/interpolation mechanism need a refined, separately assessed
target; do not expand this scan automatically. A genuine counterexample
would require complete packed retained families and exclusion of every
independent-translation full-rank witness, not sampled ranks or L132's
synchronized cover. No independent witness or matching is derived here.

This recommends an ordinary calculation first. Creative packing-to-rank
work lacks a justified nonvacuous fixed-map mechanism while feasibility
is untested; this is the concrete blocker, not missing source coverage
or a general prohibition. The newly ready scope receives separate
supervisor approval before research. No lemma, mathematical script,
PROOF or DAG is changed. Full/supporting Mathlib coverage is not checked;
no cross-notebook input or certified originality is claimed.
