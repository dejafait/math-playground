# Resolution width inputs

## Hypotheses

For an unsatisfiable CNF F on m variables, let w₀(F) be its maximum initial clause width, W(F) its minimum refutation width, and S(F) its minimum number of proof lines. Resolution permits reuse of derived clauses and weakening, but no extension axioms or new variables.

For a connected graph G, let T(G,χ) encode its vertex parity equations by all clauses forbidding incorrect local assignments. Define e(G) as the minimum number of crossing edges over vertex sets of size between |V(G)|/3 and 2|V(G)|/3.

## Conclusion

For an absolute constant K,

W(F) ≤ w₀(F) + K sqrt(m ln S(F)).

If the total charge χ is odd, then W(T(G,χ)) ≥ e(G).

## Proof

These are **Ben-Sasson–Wigderson, Theorems 3.5 and 4.4**, in *Short Proofs Are Narrow—Resolution Made Simple*, J. ACM 48(2), 149–169 (2001), [DOI 10.1145/375827.375835](https://doi.org/10.1145/375827.375835). The [author-uploaded journal text](https://www.researchgate.net/publication/2370656_Short_proofs_are_narrow-resolution_made_simple) was checked on 2026-09-25, including §§2.1–2.3 and Definition 4.3. These statements apply to general resolution, not only tree-like proofs. The first theorem concerns minimum width, not the width of every short proof.

## Mathlib

Coverage: **not checked** for either theorem or the combined algorithmic discriminator. The cited external theorems match the two displayed inputs; neither alone matches the full decision-time comparison or resolves P versus NP.
