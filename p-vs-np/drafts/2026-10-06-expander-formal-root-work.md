# Exact graph-root degree specialization — saved reasoning

Approved unchanged target and REPRODUCTION coverage: `drafts/literature/2026-10-06-expander-formal-root-relations.md`. Existing work and Attempts 017/019 are preserved.

Saved before full assembly: use L031's exact ordered roots, not Boolean simplifications. Edge values have syntactic degree 2, conjunction prefix i has degree 2i, and the repeated root has degree 4m. The sum of circuit-gate degrees is m²+7m−2, including the m=1 boundary. Each signed eta has the same syntactic upper degree as its positive gate, so the final accumulator has bound d=1+(m²+7m−2)=m²+7m−1 for either sigma. All earlier accumulator and internal degrees are bounded by d. Positive/complement roots plus constants give S=2n+8m+2 abstract nodes. Every AND is exact, so H_i=0 and L025 can use h=1.

Remaining work in this attempt: justify complete Boolean/commutator/normalized-clause witness degrees using the ranked recurrences, charge all separate rooted outputs and axiom framing, and apply L025 with these S,d,h,E. A possible conservative local-witness threshold is 1+(4S+6)d. The common local witness DAG has O(S²) nodes and O(S²) roots; dense identifiers suggest O(S⁴ log(S+2)) full encoding. These are pending proof obligations here, not a verified result. The general ER-data, tree-conversion, every-certificate and decision gaps remain open.

Completed: canonical L032 contains the full proof and receiving-parameter application. The saved plan above is retained as unfinished-at-save reasoning, not a second canonical proof. The threshold passes for all supplied graphs and both signs, including m=1. A separate audit is pending its own coverage approval; no further mathematical target was attempted here.
