# L054 — Shallow suffix formulas for the distinct-terminal formula graph

## Hypotheses

Use L048's unconditional occurring-variable width-at-most-three original-CNF, ordered-axiom and complete binary encoding conventions, without either existential certificate-size premise. Supply a division-free, fan-in-two ordered noncommutative **tree** C over F₂ with s nodes and depth at most a log₂(s+2), for a fixed a. Constants 0 and 1, repeated symbols, arbitrary syntactic degree, mixed degrees and nonlinear placeholder occurrences are allowed. Put Q=2+|F|+|C|+|A|, charging the actual names, dictionaries, ordered axioms and tree syntax. For its intended application assume C(x,0)=0 and C(x,A)=1 formally; the interface below does not need these identities.

Make fully copied trees f₀=C(x,0) and f₁=C(x,A)+1. For each separately, use exactly L018's graph: two distinct terminals s_v,t_v at **every occurrence**, disjoint children, one labelled leaf edge, four constant-one addition connectors and three constant-one multiplication connectors. Retain a zero-labelled leaf edge, or delete just that edge; both conventions are covered below. No terminals are merged. The output is the root exit t, and the input is the root entry s. Fix an ordinary complete Frege system with formula substitution, over AND/OR/NOT, with full binary proof encoding as in L053. XOR, constants and equivalence in the proof are fixed formula abbreviations, not extension gates.

## Conclusion

For both graphs, every vertex u has an explicitly written tree S_u representing its entire ordered u-to-t path polynomial, including the empty path at t. There are fixed K,k, depending only on a and the encoding/Frege conventions, such that the graphs, all these trees, and ordinary-Frege proofs of all the following Boolean interpretations have aggregate full binary length and construction time at most KQ^k:

    S_t = 1,
    S_u = delta_(u,t) + sum_(edges u->w) label(u,w) S_w,
    S_s = f_j.                                                    (1)

The sum retains the actual constant/variable/zero labels. Every temporary XOR/AND proof formula has depth O(log(Q+2)); its actual ordinary-basis expansion is paid. Each suffix is separately written, with no gate variables or free sharing. Equivalently these are coordinate proofs of S=e_t+E₀S+sum_b x_b E_b S for the actual constant/letter adjacency matrices, with zero coefficients omitted and the original factor order retained.

This is only the syntactic suffix interface. In particular, (1) does **not** prove S_s=0, even when formal zero is supplied externally. Applying finite closure, coefficient-space invariants, final original-CNF guards and their complete ordinary-Frege ledger remains a separate receiving obligation. No polynomial arbitrary-degree formula-IPS receiver, certificate existence, arbitrary ER representation or SAT conclusion is claimed here. The separate informal audit in §5 found no substantive defect; no proof strings were checked and no originality is certified.

## Proof

### 1. Assessed difference and exact graph

The prior SPECIALIZE assessment is `drafts/literature/2026-10-11-formula-origin-suffix-receiver-scope.md`. Li, Tzameret and Wang, *Characterizing Propositional Proofs as Non-Commutative Formulas*, [arXiv:1412.8746v4, 11 September 2015, Lemma 4.17, printed pp.36–39](https://arxiv.org/pdf/1412.8746v4), provides the inspected homogeneous constant-free formula-origin suffix construction. Its terminal convention and hypotheses do not directly provide this mixed-degree constant-edge interface. The same paper's Theorem 4.1 is a quasipolynomial receiver, not a polynomial import for the current target. L018 specifies the distinct-terminal representation of the standard formula-to-ABP construction; its shared EF proof is not used as an ordinary-Frege proof. The short construction below is needed to justify the changed terminals, constants and written-proof costs. It is not a reproof of a new PIT theorem. L053 motivates the requested interface, but its width-two theorem is not a premise here.

A width-three clause axiom has at most 11 arithmetic nodes, a Boolean axiom at most five, and a commutator at most seven. Substitute these actual trees separately at every placeholder occurrence, preserving their order and position names. An empty clause contributes 1. Thus each f_j has U≤11s+2 nodes and height h≤a log₂(s+2)+5 (height counts edges). Actual symbol payloads cost at most Q bits each. No expansion into all monomials or constant-free replacement is made.

For an addition occurrence v with children l,r, the connector edges are s_v→s_l, s_v→s_r, t_l→t_v and t_r→t_v. For a product occurrence they are s_v→s_l, t_l→s_r and t_r→t_v. All have label 1. A leaf has the single edge s_v→t_v labelled by its actual constant or original variable. There are exactly 2U vertices and at most 4U edges. The recursive ordering s_v, the left graph, the right graph, t_v is topological. Every vertex is an entry or an exit of exactly one occurrence; no gadget-internal vertex is omitted, since substituted axiom nodes themselves are occurrences in f_j. In f₁ the final +1 is an actual root addition, so its constant branch and all connectors are covered by this construction, rather than by an unproved identification with a different graph.

### 2. Explicit continuation trees and sizes

Let B_v denote the actual subtree of f_j rooted at v. Define the **written tree** R_v top down, making independent copies at each use:

    R_root = 1.
    If v is an addition:       R_l = R_v,        R_r = R_v.
    If v is a product:         R_l = B_r R_v,    R_r = R_v.       (2)

Every multiplication in (2) has the displayed order and bracketing. Define

    S_(s_v) = B_v R_v,                 S_(t_v) = R_v.           (3)

These equations are construction instructions, not shared-circuit definitions retained in proof lines.

More explicitly, list the product ancestors at which the route from the root to v enters the left child, starting with the nearest such ancestor and proceeding outward. Let B_(r₁),…,B_(r_q) be their right-child subtrees in this order. Then R_v is the right-associated tree

    B_(r₁)(B_(r₂)(…(B_(r_q) 1)…)),

with R_v=1 when q=0. All selected right subtrees are pairwise disjoint occurrences of f_j and are disjoint from B_v: for any two selected ancestors, the lower ancestor lies in the upper one's left subtree. Therefore the sum of their node counts plus |B_v| is at most U. Also q≤h≤U−1 unless U=1, in which case q=0. It follows directly that

    |R_v| = 1+q+sum_i |B_(r_i)|,
    |S_(s_v)| = 2+q+|B_v|+sum_i |B_(r_i)| ≤ U+h+2 ≤ 2U+1.

Exit suffixes satisfy the same bound. No semantic cancellation is needed for this size estimate. A path in R_v crosses at most q new product nodes and then at most h levels of one selected subtree, so depth(R_v)≤2h. This also holds for q=0, and depth(S_(s_v))≤2h+1. Thus all 2U suffixes together have O(U²) arithmetic nodes, depth at most 2h+1 individually, and O(QU²) full written bits before ordinary-basis expansion, up to fixed syntax factors.

This estimate uses tree occurrences. Replacing the input by a shared circuit would invalidate the disjoint-subtree counting argument and is outside the statement.

### 3. Every local recurrence and ordered path semantics

At the root output t, R_root=1, there are no outgoing edges, and the empty path gives exactly the terminal injection in (1). At any other vertex there is no injection. The following cases exhaust all vertices; for these displays write B_l=L, B_r=R and R_v=T.

* **Leaf entry.** Its suffix is bT, where b is its actual label, and the outgoing contribution is b S_(t_v)=bT. For a retained zero edge the equation is 0T=0T. If that zero edge is deleted, the outgoing sum is empty and the needed identity is 0T=0. Constants 1 and repeated variable labels require no extra promise.
* **Addition entry.** Its suffix is (L+R)T. The two child entry suffixes are LT and RT by (2). Including connector labels, its outgoing sum is 1(LT)+1(RT). Right distributivity and the two unit laws give the recurrence. Factor order is never exchanged.
* **Product entry.** Its suffix is (LR)T. The only outgoing contribution is 1 S_(s_l)=1(L(RT)), since R_l=RT. One associativity and one unit law give the recurrence.
* **Exit of a child of an addition.** Either child exit has suffix R_v=T. Its only outgoing edge goes to the parent's exit with suffix T, so the recurrence is T=1T.
* **Exit of the left child of a product.** Its suffix is R_l=B_r R_v=RT. The only outgoing edge goes to the right child's entry, whose suffix is B_r R_r=RT. Thus the recurrence is RT=1(RT). This is the connector case that cannot be replaced by an edge to the parent exit.
* **Exit of the right child of a product.** Its suffix is R_r=T, and the only outgoing edge goes to the parent exit with suffix T. Again the recurrence is T=1T.

Every identity is valid in the free associative F₂ algebra, using only ordered associativity, distributivity, units and zero. The cases also give ordinary propositional identities when + is XOR and multiplication is AND.

For completeness, let P_u be the actual u-to-t path polynomial. In a finite DAG, partitioning nonempty paths by their first edge gives the recurrence in (1) for P, with the empty path contributing only at t. Descending induction in the displayed topological order makes its solution unique: all successor values have already been fixed when computing P_u. The terminal case and the verified recurrence for S therefore prove P_u=S_u at every vertex. This is a semantic correctness argument and does not masquerade as a Frege identity proof. The latter is provided separately below by the explicit local identities. Finally S_s=f_j·1 by (2)–(3), giving a paid source identification by the right-unit law.

For adjacency notation, the only nonzero edge labels are 1 and individual x_b. Bit coefficients record parallel multiplicities; here terminals are distinct and no nonzero parallel edges are needed. Each coordinate's outgoing list has at most two terms. Omitting zero coefficients in a matrix sum thus leaves exactly the above outgoing terms, possibly with unit factors or zero terms removed. The terminal coordinate is 1. Collecting terms is unnecessary in this graph; writing all zero coefficients explicitly would require only polynomially many zero/unit simplifications. No variable is moved past a suffix in obtaining S=e_t+E₀S+sum_b x_b E_b S.

### 4. Actual ordinary-Frege proofs and full ledger

Fix, once and for all, Frege proofs of the Boolean interpretations of the associativity, right distributivity, unit and zero identities used in §3, and reflexivity of equivalence. These are tautologies in at most three formula arguments, so completeness of the fixed Frege system supplies finite proofs independent of the input. Select such proofs once; their line counts, formula sizes, rule instances and argument multiplicities are fixed constants. Substitution into their proofs is a legitimate Frege proof operation: it preserves axiom instances and inference rules. It does not posit an identity of arbitrary formulas as an axiom.

Instantiate the appropriate proof with the actual copied Boolean interpretations of L,R,T or b,T. Where two laws are used, use a fixed transitivity-of-equivalence proof schema to combine them. Include the constant number of connector unit simplifications displayed in §3. Consequently each vertex recurrence uses a bounded number of such schema instances. The output injection and source identification each use one fixed schema. The forest contains O(U) recurrences per graph, and every displayed formula argument is one of the copied trees from §2 or a bounded product/sum of them. The same chosen written subtree is used wherever an argument must repeat; no costly equivalence between alternate evaluators is being assumed.

Let M be a constant larger than all line counts and formula node counts of these fixed proof schemas, including their combining schemas. Every temporary proof line is a fixed template containing at most M copies of arguments, each of depth at most 2h+1 or that depth plus a fixed constant. Thus its temporary depth is at most 2h+c, for a fixed c (depending on the chosen schemas). There are at most c' U lines for another fixed c'. The complete temporary node count is O(U²); even an overly conservative O(U³) bound would suffice. All proof line references and rule tags are written.

Implement XOR, for example, as (p∧¬q)∨(¬p∧q); equivalence and constants also have fixed ordinary formulas. Over a nonempty original alphabet, constants can use one original variable in fixed tautology/contradiction formulas. If the selected encoding has primitive Boolean constants, use them directly. If there is no original variable and constants are not primitive, one fixed auxiliary propositional variable suffices for these constant tautologies; it is not an extension variable or an assumed axiom, and adds a fixed name cost. No claim of fresh-variable elimination is required for this interface.

There is a fixed c₀≥2 such that fully expanding any binary temporary formula of depth d, including the fixed schematic line templates, uses at most c₀^(d+1) ordinary nodes. This follows by induction on d from the bounded number of argument copies in each connective's implementation; choose c₀ to dominate those fixed recurrences. Since U≤11s+2≤13Q and h≤a log₂(Q+2)+5, each actual proof line has at most

    c₀^(2h+c+1) ≤ c₁ (Q+2)^(2a log₂ c₀)

ordinary nodes after increasing c₁ to account for the fixed overhead. There are O(Q) such lines, so this is a fixed polynomial total. The same depth argument bounds every separately written suffix expansion. The original names each have at most Q bits; dense vertex names and line references have logarithmic length in this polynomial output. All graph records, suffix copies, repeated original names, dictionaries, two substituted trees, proof formula framing, rule tags and references therefore fit one KQ^k bound, for an integer k increased to dominate the displayed fixed exponent and framing factors. Construction time is bounded by the same kind of fixed polynomial by explicitly copying and expanding the trees and schema instances. No implicit arrays or gate sharing remain in any proof line.

These proofs establish local **equivalences**, with assignment variables free. They do not insert the external formal-zero promise as a propositional axiom. In particular the same interface is constructed for a nonzero input formula. The unproved receiving step must use additional checked coefficient equalities and derive a source-zero theorem from them with its own paid ordinary-Frege argument. This separation prevents treating semantic correctness of this graph or a successful PIT computation as that missing proof.

### 5. Independent critical audit, 2026-10-11 (step 166)

The prior SPECIALIZE assessment `drafts/literature/2026-10-11-formula-origin-receiver-critical-audit.md` approves this joint L054/L055 audit. The supplied-tree, fixed-depth and unconditional L048 hypotheses are retained. L018's graph paragraph was checked directly; its EF conclusion is not an ordinary-Frege premise. The already inspected LTW/Kiefer statements recorded in that assessment remain supporting inputs with their stated restrictions. No new theorem is imported.

For an occurrence v, any two selected right siblings in §2 are disjoint: the lower selected ancestor belongs to the upper selected ancestor's left subtree. Neither contains v. Thus the individual suffix-size estimate counts actual occurrences, even with repeated symbols or identical subtrees. Along a path in a continuation one visits at most q product nodes before entering one selected right subtree, whose height is at most h. This proves depth at most 2h, including q=0. An entry adds one product node. Every graph vertex is an occurrence entry or exit; no extra vertex requiring a different suffix is hidden in the substituted axiom trees.

The graph's six local cases in §3 exhaust all outgoing possibilities. In particular, the left exit of a product has continuation B_r R_v and goes to the right entry, whose suffix is exactly B_r R_v; it does not go to the parent exit. Both addition exits keep R_v, whereas the product's right exit keeps R_v. The root output has no outgoing connector and suffix 1. The extra +1 of f₁ is a genuine addition occurrence with its own leaf and four connectors. A deleted zero leaf edge requires the fixed law 0T=0; retaining it requires reflexivity followed, if desired, by the same law. The non-root exits still have their parent connector. Descending path induction therefore agrees with every written suffix, including constant-only and empty terminal paths.

Each recurrence uses a constant number of fixed tautology proofs substituted with the actual L,R,T arguments. Each such argument has depth at most 2h+O(1); a fixed schema adds constant depth and bounded argument multiplicity. There are O(U) local proof instances and O(U²) copied suffix nodes before ordinary expansion. With h bounded by a fixed multiple of log(s+2), expanding the fixed XOR/equivalence abbreviations costs a fixed power of Q per line. Names, references, zero-edge branches and both graphs are all paid. This verifies the interface's polynomial threshold without assuming a formal-zero proof or a homogeneous suffix theorem. No change to its mathematical argument or DAG inputs was needed. This is an informal audit, not mechanized verification or checked Frege output; matching Mathlib coverage remains not checked.

## Mathlib

Matching coverage for the complete suffix/proof compiler and its ordinary-Frege full-bit bound is **not checked**. The finite ordered path recurrence, tree formulas and Boolean ring identities are elementary supporting mathematics proved here. The precisely cited LTW homogeneous suffix theorem supplies comparison, not a matching mixed-degree/constant-edge theorem or a Mathlib claim. L018 supplies the chosen graph/substitution conventions and L048 supplies the unconditional package. Unknown Mathlib availability is not evidence of absence.
