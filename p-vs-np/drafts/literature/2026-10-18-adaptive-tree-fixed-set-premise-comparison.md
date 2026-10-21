# Adaptive versus fixed-set conditioning — source comparison

TARGET: Test whether every L081-admissible M-leaf adaptive tree admits a fixed queried set whose full assignment tree has at most M leaves and satisfies the same original-cutoff leaf promise.
CHECKED: 2026-10-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 315 compared the exact L079/L080/L081 hypotheses, step-311 source assessment, step-314 audit record, relevant adaptive work notes and Attempts 019–020; searched backdoor trees/backdoor sets/shortest path, syntactic support/backdoor, assignment-independent backdoor trees, value-independent decision trees, and full binary tree/Kraft equality. No inspected theorem supplies the exact replacement claim; failed searches do not certify novelty.
SOURCE_EVIDENCE: Reuse Darwiche–Marquis (2002), Definitions 2.6–2.10 and Proposition 5.1 conditioning case, through the step-311 assessment. Newly read Ordyniak–Schidler–Szeider (2024), sections 2.2–2.5 and Observations 1–2 with their complete displayed proofs, pp.2–3,5; inspected Cortes Reina–Foldes–Mardoukhi–Singhi arXiv:1409.3855v1 (2014), introduction and theorem statement, pp.1–3, as binary-tree/Kraft terminology only.
COMPARISON: The inspected backdoor result supplies the union of queried variables as a strong backdoor set and bounds its cardinality by M−1; it does not supply the desired at-most-M assignment count. Its assignment operation simplifies CNFs. L081 instead retains every gate and uses syntactic unions; the exact shortest-path replacement still requires a separate proof.
GAP: Establish or refute the exact replacement at unchanged T/k: justify whether residual acceptance is independent of assigned bits for a fixed queried set, and verify the shortest-path candidate's full-tree leaf bound and every original-cutoff ancestry promise.
REASON: Essential source and hypothesis comparison is now sufficient for one bounded proof/counterexample attempt. No full matching theorem was found in the sources checked; do not infer originality or prove the replacement during this literature turn.
SCOPE: Explicit finite full binary original-input trees, no repeated input per path, all M including singleton and unequal-depth cases, unchanged T and k, scalar occurrence replacement without simplification, both signs and unused roots; no compressed DAG, semantic simplification, finder or arbitrary-ER tree-existence claim.

### Gap, target and downstream use

The main gap is ordinary unrestricted SAT decision/separation. The nearer
route gap is L037 data for arbitrary supplied ER. L081 supplies data only
when its explicit adaptive tree is supplied, with cost polynomial in T+B;
existence of a polynomial-size tree remains unproved. This review concerns
only the exact TARGET above. A positive replacement would redirect search
for this structural promise toward fixed sets; a negative result would
identify a concrete adaptive advantage. Neither result is established.

### Primary evidence and its applicability

Ordyniak, Schidler and Szeider, *Backdoor DNFs*, JCSS 144 (2024), 103547,
[doi:10.1016/j.jcss.2024.103547](https://doi.org/10.1016/j.jcss.2024.103547),
[published PDF](https://eprints.whiterose.ac.uk/id/eprint/213187/7/1-s2.0-S0022000024000424-main%20%281%29.pdf):
section 2.2 deletes satisfied clauses and false literals under assignment;
section 2.3 assumes assignment-closed tractable CNF base classes. Sections
2.4–2.5 define strong sets and pathwise read-once, two-child trees.
Observations 1–2, p.5, give a strong set consisting of all queried variables
and at most M−1 such variables for an M-leaf tree. The displayed proof
uses a consistent covering assignment and closure under further assignment;
the tree statements refer back to [59]. This is a weaker size guarantee
than the TARGET and a different restriction operation. Theorem 3 detection
coverage is reused from step 311; it is not detection for the signed DAG.
Theorem 2 was encountered as a lead about minimal backdoor sets, but its
full proof was not inspected and no specialization is imported. The 2008
Samer–Szeider author PDF again returned an internal retrieval error; the
accessible 2024 statements suffice here, so this is not an essential blocker.

Darwiche and Marquis, *A Knowledge Compilation Map*, JAIR 17 (2002),
229–264, [doi:10.1613/jair.989](https://doi.org/10.1613/jair.989): reuse the
inspected Definitions 2.6–2.10, pp.232–233, and Proposition 5.1 conditioning
case, p.256, from
`drafts/literature/2026-10-18-adaptive-input-query-tree-data.md`.
These cover Boolean decision representations/conditioning, not the exact
syntactic counted-path replacement. No rereading or new import is needed.

Santiago Cortes Reina, Stephan Foldes, Yousof Mardoukhi and Navin M. Singhi,
*Note on islands in path-length sequences of binary trees*,
[arXiv:1409.3855v1](https://arxiv.org/pdf/1409.3855), 12 September 2014,
pp.1–3: the introduction uses finite rooted trees with left/right children
and root-to-leaf binary codewords; the unnumbered theorem on p.3 is a
variant of [FS, Theorem 4] characterizing topological length sequences
with Kraft sum one. Only these statements were read, not the theorem's
proof. This is contextual tree terminology, not an imported replacement
or a proof of the TARGET's numerical bound. The later elementary leaf
count should be justified directly on L081's supplied full tree; it needs
no general characterization theorem or reproof of this paper.

### Local comparison, duplicate and failure checks

Read L081's complete hypotheses and its scope/leaf-reception interface,
L080's fixed-set hypotheses, and L079's support/counting definitions.
L037's supplied-data interface is the downstream receiver, not an input
to the proposed combinatorial proof. L081 permits up to n queries on a
path; L080's whole theorem requires at most k queried inputs. That latter
hypothesis must not be inferred from an at-most-M branch bound when
M>T+2. Circuit-only reception at original T/k remains the relevant
component if a later application needs it.

The definitions explicitly retain zero products and compute supports by
singleton/empty bases, inheritance at signs and union at ANDs. Whether
these rules yield assignment-independent acceptance for a fixed queried
set is an explicit proof obligation of the next turn, not a result of
this review. No Boolean function support or CNF clause deletion may be
substituted for these definitions. Preserve source ancestry paths,
repeated operands, every unused definition and both signed roots.

The targeted work-note/history search located the step-314 proposal and
no completed replacement proof in those paths. Attempts 019–020 stop
universal common-order OBDD width and degree-only identical-output
conversion; neither decides this promise comparison. Their stop evidence
is preserved. No cross-notebook theorem input is used. Full matching
Mathlib coverage is not checked; no absence claim is made.

### Separately approved bounded attempt

Test the queried set of a shortest root-to-leaf path. Prove all needed
claims from the exact definitions, including the full binary tree count,
assignment reception and unchanged original-cutoff promise. Handle M=1,
unequal depths, all-input queries, M>T+2, constants, signed nodes, repeated
operands and unused roots. No new formal H identities or receiver theorem
is sought.

Continue if that candidate gives the exact at-most-M assignment threshold
and all residual promises. If the candidate fails, isolate the exact
failure; that alone does not refute the existential TARGET. Abandon the
replacement claim only with an L081-admissible full tree and a rigorous
argument that every fixed set meeting the same promise has more than M
assignments. An inconclusive search is EXPLORATION. Do not enlarge the
scope to simplification, a tree finder, polynomial tree existence, a new
receiver or SAT transfer. Arbitrary-ER data existence, formula-only bounds
and unrestricted SAT remain independent gaps.

This is ready coverage for a later mathematical attempt, not a completed
mathematical result. This turn writes no lemma or mathematical script.
