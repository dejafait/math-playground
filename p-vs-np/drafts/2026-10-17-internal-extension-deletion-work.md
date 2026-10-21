# Internal extension deletion — step 280 work checkpoint

Approved target: assess logarithmic internal extension deletion for full-bit
L037 data, under the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-17-internal-extension-deletion-data.md`.

Main gap: unrestricted SAT decision/separation; this attempt addresses only
the missing restricted representative/relation input to L037. Reuse
L026/L035/L036/L037/L071/L072 and Attempts 019–021. No common order across
conditioned branches, independent internal values, extension axioms or
generic Boolean-zero witnesses are available.

Working mechanism (not yet proved): order deleted gates topologically.
For each assignment prefix, compile the ancestor circuit of the next
deleted gate with earlier deleted outputs fixed, obtaining a small x-only
test q. A full binary decision tree of these tests selects compatible
branches. Products of path literals give small affine-ABP weights. Branch
compilation orders may differ. To relate a prefix test to its full-branch
operands, try a one-sided formal comparison recurrence on their common
ancestor circuit using the already supplied local relations and L035.
Then test explicit partition/orthogonality and guarded deleted-definition
witnesses via L035/L036, followed by L072's flat recombination.

Continue only with both formal H identities and one fixed polynomial in
T and 2^k for all independent graph copies, dictionaries, pre-substitution
degrees and bit time. Stop this mechanism if comparison/guard witnesses
require uncontrolled recursive copying or generic Boolean-zero witnesses.
No sufficiency conclusion is recorded at this checkpoint.

## Completed attempt

The all-size construction is now in canonical
[L073](../lemmas/L073-logarithmic-internal-deletion-affine-abp-data.md).
Prefix tests are never recursively substituted. A one-sided comparison
graph supplies the needed formal prefix/full-branch bridges; adaptive
weight-product and guarded-definition witnesses then permit L072's flat
recombination. The required fixed polynomial in T and 2^k is obtained,
including independent copies, original dictionaries, time and degrees.
Only compatible branches are used for semantic fidelity; all witness
identities are proved in the free ring.

Outcome: ADVANCE / RESEARCH / POTENTIALLY_NEW, meaning local restricted
progress, not certified originality or a P-versus-NP resolution. The
proof and aggregate ledger await separate critical audit. No mathematical
script or implementation was needed or claimed. Existing source coverage
and the same-day primary problem-statement verification are reused without
new browsing. Attempts 019–021 and all unfinished work are preserved.
