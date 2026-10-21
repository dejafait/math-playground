# Alternative ABP commutator witness — work checkpoint

Completed: [L035](../lemmas/L035-alternative-affine-abp-commutator-witness.md) contains the full proof of the marked-edge construction, both formal identities and the O(E³ log(E+2)) full encoding bound. Every fixed edge pair uses four separate graph copies; the intermediate subpath choices are independent because the input graphs are acyclic. The graph algorithm takes polynomial time and does not enumerate paths. The 83 finite graph diagnostics pass, including exact counts and 18 detected suffix-order mutations; complete evidence is under `scripts/alternative-abp-commutator/marked-edge-results.json`. The initial reasoning below is preserved as a checkpoint, superseded by canonical L035.

Outcome ADVANCE, kind RESEARCH, classification POTENTIALLY_NEW under the pre-existing EXPLORE assessment. This supplies a local representation input beyond the full statement scope established in the inspected sources, with no certified novelty or P-versus-NP resolution. L025/L034 are downstream/scope comparisons, not proof premises of L035. A separate critical audit has REVIEW_REQUIRED scope; no new downstream theorem was attempted or approved in this step.

Approved target: the unchanged EXPLORE target in `literature/2026-10-07-alternative-abp-commutator-witnesses.md`. One mathematical attempt, reusing its inspected LTW Lemma 3.7 and Raz–Shpilka Lemma 2 Step 1 coverage. L025's pair stage is downstream context; Attempts 020/021 exclude prescribed outputs only. Existing uncommitted work is preserved.

Initial construction under examination: for an edge e:u→v of F and d:a→b of G, let F[s,u], F[v,t], G[s,a], G[b,t] denote path-sum polynomials. Sum

    F[s,u] G[s,a] T(e,d) G[b,t] F[v,t]

over edge pairs, where T(e,d) is the affine placeholder expression for the commutator of their affine labels. Double ordered-product telescoping suggests the substituted sum equals fg+gf. Fixing the two marked edges may make the four subpath choices independent; four separate graph copies per pair would then avoid path-history storage. This is unfinished reasoning, not yet a proved result.

Remaining checks: exact product order and telescoping, uniqueness of path decomposition in acyclic graphs, constants/parallel edges/empty paths, output graph acyclicity, both formal identities, and full binary encoding and construction time with alphabet/axiom framing included. Continue only if all checks give one polynomial bound in supplied E. General reduced data, Boolean and defining-clause witnesses, final assembly and decision transfer remain unresolved.
