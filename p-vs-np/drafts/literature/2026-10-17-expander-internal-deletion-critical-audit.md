# Expander internal-deletion result — critical-audit coverage

TARGET: Critically audit L074's incidence-subgraph identification, separator constant and encoded-length threshold comparison for both signs of L031.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the threshold assessment's discovery and comparison; focused follow-up searches for expander vertex deletion, epsilon/n/4 separators and incidence-graph treewidth found no inspected full signed-ER audit theorem. Read the exact local interfaces and recorded failures; search failure is not novelty evidence.
SOURCE_EVIDENCE: Reopened Gurski–Weishaupt arXiv:2406.08985v1 §2.1/Definition 1, Theorems 17–18/24–25 and Corollaries 22/26, printed pp.3,8–13, including the relevant operation proofs; reopened Marx, Theory of Computing 6 (2010), §3.1 definition and Lemma 3.2(a,b), pp.92–93. The prior threshold assessment supplies the expansion-convention comparison.
COMPARISON: Known graph inputs cover the audit's external mathematical premises; they do not verify the signed-gate identification, real component-union thresholds, deletion iteration or full-bit ceiling comparison in L074. Those are a bounded applicability audit of an existing specialization, not a new general treewidth theorem.
GAP: Source coverage is ready; independent mathematical checking of L074's existing proof and both finite-size tests remains pending. No claim here certifies L074 or supplies arbitrary ER-to-ABP data.
REASON: The new critical-audit target now has explicit source scope and all essential statements available; proceed to one REPRODUCTION proof audit without further literature unless a concrete hypothesis discrepancy appears.
SCOPE: L074 as written, both sigma choices of L031, n>=2 and m>=1, fixed 0<epsilon<1 and integer Delta>=3, the unchanged full signed graph, positive-internal vertex deletion only, and actual full binary T without padding.

## Gap, use and bounded decision

The exact P-versus-NP gap remains a deterministic polynomial-time SAT
algorithm or an argument excluding every such algorithm. The nearer
representation gap is arbitrary ER-to-affine-ABP data. The intermediate
target is solely independent checking of L074's restricted negative test
of L073's sufficient promise. A successful audit would make the recorded
family stop reliable and prevent reusing this structural promise on the
same supplied expanders. It would not exclude other data, certificates,
proofs or structural families. Formula-only bounds, W/V/U and unrestricted
SAT transfer remain unresolved.

Continue with the restricted conclusion only if every source hypothesis,
gate interface and displayed inequality survives independently. If any
fails, record the first exact defect and its effect on the claimed bound,
preserving the original derivation and Attempt 028. This is a test of
existing work, not a renewed search for deletions meeting the promise.
No new theorem, proof derivation or mathematical script is produced here.

## Inspected source scope

Frank Gurski and Robin Weishaupt, *The Behavior of Tree-Width and
Path-Width under Graph Operations and Graph Transformations*,
[arXiv:2406.08985v1](https://arxiv.org/pdf/2406.08985v1), 13 June 2024:
§2.1 and Definition 1 use finite simple undirected graphs and ordinary bag
width. Theorems 17–18 (pp.8–9) bound vertex-deletion loss by one and
vertex-addition increase by one. Corollary 22 (p.10) gives subgraph
monotonicity. Theorem 24 (pp.11–12) gives contraction monotonicity;
Theorem 25 (p.12) preserves treewidth under one edge subdivision;
Corollary 26 (p.13) preserves it under subdividing all edges. Inspected
proof cases: deleting/adding a vertex in bags, merging adjacent endpoints,
and subdivision's forest case versus attachment of a three-vertex bag
when width is at least two. The edge hypothesis excludes the edgeless
case in Theorem 25; the prospective audit must retain L031's m>=1.
No pathwidth conclusion is needed. The broader minor statement is
unnecessary. These facts are imported; reproof is unnecessary.

Dániel Marx, *Can You Beat Treewidth?*, Theory of Computing **6** (2010),
85–112, [journal PDF](https://www.theoryofcomputing.org/articles/v006a005/v006a005.pdf),
§3.1, pp.92–93: the definition balances every remaining connected
component by at most half the original nonempty W. Lemma 3.2(b) supplies
such a separator of at most k+1 vertices when treewidth is at most k.
The separator may intersect W. Read (a) as well; it is not the implication
needed here. This lemma cites Reed and Flum–Grohe rather than printing
its proof; those antecedents were not newly read. The precise named
statement suffices as an imported standard input. Do not substitute a
2/3-balanced partition or balance relative to W minus the separator.

The earlier [threshold assessment](2026-10-17-expander-internal-deletion-threshold.md)
already inspected Böttcher et al.'s external-neighborhood convention and
Dvořák–Norin's opposite-direction separation-number theorem. Their full
results are unnecessary for this audit; no repeated extraction is needed.
Search also returned the later published Gurski–Weishaupt article, whose
numbering differs, and work on noisy graphs/tree-cut width. These are
uninspected leads, not replacements for the versioned inputs above.
No essential source remains blocked.

## Local interfaces and duplicate/failure comparison

Read canonical L074 in full, L031's hypotheses, exact p_i/r_i/h gates,
accumulator operands and full binary accounting, L071's full signed-graph
hypothesis, and L073's hypothesis/conclusion for the promise only.
The prior threshold assessment, step-283/284 histories, the step-284 work
note and Attempt 028 describe one completed derivation, not independent
audit evidence. Attempts 019–021 concern universal OBDD width,
degree-only identical-output ABPs and a prescribed pair-table output;
they supply no deletion-number theorem. No duplicate independent audit
of L074 was identified in these exact local records. No sibling notebook
or cross-notebook result was read.

The mathematical audit should check these existing obligations, without
silently replacing them by stronger conclusions:

- Match the retained original vertices and fresh edge gates against the
  full signed graph. Check both sigma choices and m=1; preserve NOT
  wrappers, repeated operands, accumulators and unused roots in the host.
  Check that deleting other positive gates cannot remove an adjacency
  of the chosen subgraph. Do not simplify by original unit assignments.
- Check the component-union count at real n/4 and n/2, including small n
  and a separator meeting originals. The sought bound is exactly L074's
  epsilon*n/4-3, not an unspecified asymptotic expander bound.
- Check the direction of the iterated deletion inequality and subgraph
  comparison. Only D intersect {p_i} is charged by the selected subgraph.
- Use L031's R_*=22m+n+2 and ceil(log₂(R_*+2)) bound on the supplied T.
  Check L074's U(n,m), B=11Delta+5, C_Delta, both finite-size tests,
  ceilings, strict comparison with the integer allowance and fixed-parameter
  eventual quantifier. No encoding changes or padding are permitted.

These are audit obligations, not conclusions established in this source
review. The local signed-gadget and length checks are necessary because
no cited general theorem mentions these ER definitions or this encoding.
They justify SPECIALIZE rather than claiming a full-statement IMPORT.
Mathlib coverage remains **not checked**, for both the complete result and
supporting theorem names; no absence claim is made.

## Search record and next-step classification

Follow-up queries: `"treewidth" "expander" "vertex deletion" separator`;
`"treewidth" "subdivision" "Corollary 26" Gurski Weishaupt`;
`"expander" "treewidth" "epsilon" "separator" "n/4"`;
`"incidence graph" "treewidth" "vertex deletion" expander`.
Only the two primary theorem sources above were newly used as mathematical
inputs. General search hits and snippets did not establish theorem coverage.
The earlier assessment retains the broader exact/stronger-result search.

The source-to-obligation comparison now approves precisely TARGET for a
separate RESEARCH / proof_audit / REPRODUCTION turn. This step is LITERATURE /
literature_comparison / REPRODUCTION: local coverage progress, with no
claim of mathematics beyond the sources or independent verification of
L074. Reuse this unchanged assessment next turn.
