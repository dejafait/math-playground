# Shared formula-IPS assembly calculation

Research calculation dated 2026-10-04, on the exact preapproved binary-bound target in `drafts/literature/2026-10-03-shared-homogeneous-ips-ef.md`. Reuse that EXPLORE assessment and its inspected semantic ABP, decomposition and proof-conversion inputs; no source search is needed for the unchanged target.

The main problem still lacks either a polynomial-time SAT algorithm or an unconditional lower bound. This intermediate upper-bound screen seeks one fixed polynomial in `T=2+|F|+|A|+|C|` for an EF/ER refutation of the original 3CNF from its supplied balanced F₂ noncommutative formula-IPS certificate. Its use would be to exclude polynomial formula-IPS certificates as an ER-hard-family mechanism. Certificate existence, unrestricted proof lower bounds and proof-to-decision transfer remain independent gaps. L016 only covers logarithmic degree; L017 supplies the missing shared homogeneous-ABP zero proofs, but not formula identification.

## Saved construction before completion

Use the standard formula-to-ABP series/parallel construction covered by Raz–Shpilka Lemma 2. Keep each tree occurrence disjoint and use constant-1 connector edges. The resulting acyclic graph has `N=O(U)` vertices for a size-U substituted tree. With topological indices, let `E_0` be its constant-edge matrix and `E_a` its x_a-edge matrices. Set

    K = I + E_0 + ... + E_0^(N-1),
    G_a = E_a K,
    b_a = e_source K E_a K.

These are finite F₂ matrices. `K E_0=K+I` and every `G_a` is strictly upper triangular. Degree-k component ABPs have a single source, first edge row `b_a`, subsequent layer matrices `G_a`, and the original sink coordinate. Constants before, between and after variable edges are accounted for by K. The degree-zero component is the ground bit `e_source K e_sink`. Components with `k>N-1` vanish by acyclicity. Import the semantic path/component construction rather than treat this as a new PIT result.

For shared Boolean evaluation, define the row circuits

    h_0=e_source K,
    h_k=sum_a (h_(k-1) G_a) x_a,  1<=k<=N-1,
    r=sum_(k=0)^(N-1) h_k.

The first recurrence must be identified with the explicitly checked b_a table. A support induction should prove `h_k(v)=0` for `v<k`, and therefore `h_(N-1) G_a=0`. Summing the recurrences gives `r=e_source K+r X K`, where `X=sum_a E_a x_a`. Using the checked constant identity for K, derive `r=e_source+r E_0+r X`. This is the original graph's triangular path-evaluation recurrence, so coordinate induction identifies r with its path evaluation p. Separately, a tree induction over the series/parallel constructors should give `p_sink=Eval(tree)`. Both derivations must retain shared gates, not enumerate words or unfold components.

For a formally zero tree, every component ABP output is formally zero. Apply L017 to each positive degree, discharge its defining guard by substituting the actual shared evaluation circuits, and check the degree-zero bit directly. This should give a polynomial CF zero proof of the original tree evaluation.

Apply this to `C(x,0)` and `C(x,A(x))+1`. Under the original CNF, each clause polynomial evaluates to zero, and Boolean/commutator axioms have fixed local zero proofs. Gate induction on C then identifies its A-substituted evaluation with its zero-substituted evaluation. The two free-assignment zero proofs should yield a formula conclusion negating the original CNF, permitting the screened CF/EF/ER conversions.

The continuation test is a complete identification and boundary proof with fixed polynomial costs for all matrix, component, guard-substitution and conversion stages. Any need for unrestricted circuit PIT proofs, uncharged formula unfolding or an unsupported recurrence identity would stop this assembly. Small exact checks will test orientation, constant paths, degree truncation and the two identities; they cannot verify the propositional proof.

## Mathlib

Coverage: **not checked** for the full assembly or its circuit identities. Supporting theorem names, versions and direct links are preserved in the unchanged assessment and source note. They cover semantic representations and standard proof operations, not a full-statement match or a novelty claim.

## Completed calculation

The complete informal assembly is recorded in [L018](../lemmas/L018-shared-formula-ips-polynomial-er-simulation.md). It specifies the imported series/parallel tree graph, compiles constant edges into finite checked tables, and proves its shared evaluation agrees with the formula and with the sum of the homogeneous evaluations. L017's gate-definition hypotheses are discharged by actual circuit substitution. Both formal identities then yield a formula conclusion negating the original CNF and permit the standard EF/ER conversions. Total component descriptions are O((T+2)^6) bits under conservative sparse-name charging; the zero proofs and all identification/conversion stages compose fixed polynomials, rather than a quasipolynomial homogenization bound.

The exact finite check `PYTHONDONTWRITEBYTECODE=1 python3 scripts/shared-abp/check_formula_assembly.py` passed 64 formulas, 1,192 degree components, 205 sparse coefficient-row checks and 237 Boolean assignments. It includes two supplied IPS certificates and degree-32 cancellation. It catches missing trailing constant closure and damaged constant tables, and rejects treating Boolean-only zero as formal zero. A preliminary check incorrectly demanded an empty final coefficient row for every formula; the one-edge variable case corrected this to a zero **next** transition. The proof permits a nonzero final row and explicitly uses strict triangularity to annihilate its outgoing transition.

The identification-cost bound includes all three intermediate matrix indices when X K E_0 is expanded, not merely those in X K. All full circuit descriptions and surrounding proof contexts remain polynomial; no word expansion is used in the proof or translator. Word enumeration is restricted to the finite examples in the check script.

This is ADVANCE / RESEARCH / POTENTIALLY_NEW as local proof assembly using known semantic inputs, not an originality certification or a P-versus-NP candidate. The result enlarges the algebraic upper-bound screen; certificate existence/hardness, unrestricted proof lower bounds and decision transfer remain missing. The same covered full binary-bound test should next critically audit this proof, especially constant closure, the finite boundary, definition discharge and the original-CNF conversion, before further reliance.
