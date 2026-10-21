# Conditional pair-link obstruction test — source comparison

TARGET: Determine whether L028's averaged lift extends to graph-link theta bodies with both determinant-link edges and pair-conflict edges.
CHECKED: 2026-10-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched graph theta bodies with added edges, recursive theta with pair constraints, conditional constant-weight packing and mixed hypergraphs; compared L027/L028 and ATTEMPTS/019. No inspected result decides the specified constant-row membership.
SOURCE_EVIDENCE: Castro-Silva, de Oliveira Filho, Slot and Vallentin, A Recursive Theta Body for Hypergraphs, Combinatorica 43 (2023), 909–938, DOI 10.1007/s00493-023-00040-9: equation (2) p. 911, Definition 1.1 p. 912, Theorem 2.1 and complete proof pp. 915–916, Theorem 2.4 and complete proof pp. 917–918; primary publisher PDF retrieved and inspected today, with canonical statements in foundations/07-core-conditioned-theta-source.md.
COMPARISON: General finite-graph theta membership and supporting inequalities apply to the edge-union graph without regularity; neither supplies its theta values or preserves L028's original independent-class mixture after adding edges.
GAP: Membership of the exact constant row on every strengthened actual link, or a rigorous exclusion certificate on one link, remains unproved; soundness and useful global caps for a new assembled model are separate tasks.
REASON: The changed conditional graph has adequate primary theorem coverage for one bounded witness diagnostic, but no matching certificate was found; this is not a novelty claim or a revival of the refuted unchanged cap.
SCOPE: Fixed L028 outer f,F only; exact graph-link feasibility or exclusion, with original labels and W_A. No full-SDP, list-realization or global-safety claim is approved.

## Exact diagnostic and relevance

The main gap is arbitrary-center safety at 68 or 67 agreements in the
fixed instance, with 955<=t_star(m)<=957. The intermediate target is
membership of L028's unchanged row in a stronger graph body, not a new
local-cap optimization. For each C,A retain W_A exactly as in L027.
On this vertex set let Q_(C,A) have all edges of (J_C)_A and all distinct
pairs B,B' with |B intersect B'|>=3. Extra edges do not introduce new
vertices. Keep determinant-zero triples as nonedges of J_C; pair
conflicts are an independent reason for an edge of Q_(C,A).

L028 gives f_A=rho>0 and normalized row
h=tau*1_(W_A), tau=136/binomial(956,5)=1/48419392161.
These constants are quoted from L028, not newly derived here. The next
attempt asks whether h belongs to TH(Q_(C,A)) for every actual C,A.
An empty W_A is vacuous. Do not replace W_A by all two-intersection
vertices without a justified restriction argument.

Exclusion on one actual link would show that this conditional repair
detects the fixed witness and justify assessing its downstream cap
potential. An exact all-link feasibility construction would stop this
repair for this witness. Failure of one proposed construction is
inconclusive. Neither outcome certifies 68-agreement safety or an unsafe
list. L028/ATTEMPTS/019 still stop the unchanged model.

## Inspected source and applicability

Primary source: [published PDF](https://link.springer.com/content/pdf/10.1007/s00493-023-00040-9.pdf).
For any finite simple graph, equation (2) requires a symmetric matrix
with prescribed diagonal, zero entries on every edge, and augmented PSD.
Theorem 2.1 contains independent-set indicators and gives compactness,
convexity and clique inequalities. Its proof checks the indicator lift,
closed scaled links, PSD bounds and cliques, including the r=1 base.
Theorem 2.4 gives all nonnegative weighted supporting inequalities;
its proof handles negative weights by an indicator Hadamard product,
then separation and downward closure. Both apply at r=2 to Q_(C,A):
its vertices are finite and its edge union consists of distinct pairs.
No regularity, transitivity or special labeling is required.

Thus a future membership proof can exhibit a separate graph matrix for
each link, or an explicit convex mixture of Q_(C,A)-independent sets.
A future exclusion proof can use a valid weighted theta upper bound or
clique inequality. These are standard imported tests; their quantitative
values here are not supplied by the source. No theorem is reproved.
The assessment does not assert soundness of replacing all links in an
assembled outer model; that would require its own applicability proof.

## Comparison, duplicates and failures

L027 imposes outer pair zeros and original determinant-link theta rows.
L028's original link certificate uses the 21 classes indexed by pairs
U subset A, with A intersect B=U. Independence there uses the original
empty-triple-intersection requirement. That argument does not check
pair-conflict edges between vertices inside a class. Hence neither the
old mixture nor feasibility in the old body settles this target.
The permutation average establishes the outer matrix, not an
actual-label symmetry of Q_(C,A). Preserve all singular and antipodal
cases, actual cores and zero-scaled cases in any generalization.

The relevant unchanged-cap assessment is
`drafts/literature/2026-10-06-core-theta-uniform-cap.md`;
its graph-theta inputs are reused. L028 and ATTEMPTS/019 explicitly
leave this diagnostic open. ATTEMPTS/010's universal-triple exclusion
failure remains relevant; no universal nonsingularity is assumed.
Earlier shell/four-block and selected-SDP tests concern different
feasible sets and do not decide these graph rows. No duplicate local
certificate was found in these named inputs.

## Search record and limitations

Queries: `"theta body" graph adding edges independent sets semidefinite Lovasz`;
`"recursive theta" hypergraphs "link" pair constraints`;
`"theta" "conditional" "constant weight" packing graph`;
`"recursive theta body" "mixed" hypergraphs`;
`"theta body" "union" "graphs" independent`.
The primary recursive-theta paper was the relevant inspected match.
Search also surfaced de Carli Silva–Tuncel, *An Axiomatic Duality
Framework for the Theta Body and Related Convex Corners*,
[arXiv:1412.2103](https://arxiv.org/abs/1412.2103), an unread duality lead,
not an input. Other snippets and software pages were not used as theorem
evidence. The bounded search does not establish originality or rule out
a stronger known result. General theta duality is unnecessary for the
approved direct membership/exclusion test.

Mathlib: a full matching strengthened-link result and supporting graph
theta coverage are not checked. No absence is inferred.

## Continuation

Essential inputs: L001, L027, L028 and
`foundations/07-core-conditioned-theta-source.md`. Use L028's canonical
exact constants and averaging proof. For the approved diagnostic all
strengthened memberships remain unknown; a sufficient global cap,
actual list realization, 67-agreement safety, full earlier SDP feasibility
and ABF equivalence remain unresolved. This review approves a later
mathematical attempt only and performs no new derivation or calculation.
