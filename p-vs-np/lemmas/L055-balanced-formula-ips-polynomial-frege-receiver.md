# L055 — Polynomial Frege receiver for supplied balanced formula certificates

## Hypotheses

Use L048's unconditional occurring-variable original-CNF and ordered-axiom encoding, with all names, dictionaries, axiom positions and syntax charged. Thus F is a CNF of width at most three, A consists of its ordered clause-falsity polynomials, original Boolean axioms and pair-once commutators, and different axiom positions have different placeholders even when their polynomials agree. Supply a division-free fan-in-two ordered noncommutative **tree** C over F₂ with s nodes and depth at most a log₂(s+2), for one fixed a. Permit constants, mixed and arbitrary syntactic degrees, repeated symbols and nonlinear placeholder occurrences. Assume the formal free-algebra identities

    C(x,0)=0,                     C(x,A(x))=1.

Put Q=2+|F|+|C|+|A| in complete binary encoding. No formula-length bound for C is assumed. Fix an ordinary complete Frege system over AND/OR/NOT, with formula substitution and explicit proof-line references as in L053. Let Φ_F be the actual written conjunction of the clauses of F. XOR, equivalence and Boolean constants below are fixed formula abbreviations, never extension variables.

## Conclusion

There are constants K,k, depending only on a and the fixed encoding and Frege conventions, such that the supplied package yields an ordinary-Frege proof of ¬Φ_F of complete binary length at most KQ^k, constructible in polynomial time in Q on valid supplied packages.

This is a local receiver with a full informal argument below; the separate critical audit in §8, including L054's suffix interface, found no substantive defect. The claimed compiler remains an **UNVERIFIED CANDIDATE at the proof-string level**: no proof strings have been generated or checked. It is not a candidate resolution of P versus NP. The result supplies no certificates from F, polynomial bound in |F| alone, arbitrary ER-to-formula representation, unrestricted-ABP polynomial receiver or SAT decision/separation. The construction's classification POTENTIALLY_NEW records the unmatched interface in the checked sources, not certified originality; the audit is REPRODUCTION.

## Proof

### 1. Assessed specialization and inputs

The unchanged prior SPECIALIZE assessment is `drafts/literature/2026-10-11-formula-origin-suffix-receiver-scope.md`. Li, Tzameret and Wang, *Characterizing Propositional Proofs as Non-Commutative Formulas*, [arXiv:1412.8746v4, 11 September 2015](https://arxiv.org/pdf/1412.8746v4), Theorem 4.1 and Lemma 4.4 (printed pp.19–23), give the known quasipolynomial receiver and its two-identity receiving pattern. Definition 4.13 and Lemma 4.15 (pp.32–35) give the inspected coefficient-space construction. Theorem 4.11 and Lemma 4.17 retain homogeneous/constant-free hypotheses that are not imposed here. No polynomial arbitrary-degree receiver is imported from those statements.

Kiefer, *Notes on Equivalence and Minimization of Weighted Automata*, [arXiv:2009.01217v1, 2 September 2020](https://arxiv.org/pdf/2009.01217v1), §§1–3, Algorithms 1–2, Propositions 2.1–2.2 and Proposition 3.1 (pp.1–5), supplies word-matrix coefficient semantics and the forward-space span/coordinate algorithm. Its inspected field-arithmetic argument applies over F₂ with fixed-cost bit operations. The source is not an epsilon-edge Frege theorem; the finite closure and exact-length applicability are specified below. We reuse these standard semantic and linear-algebra inputs, rather than reprove PIT or treat a successful PIT computation as a Frege axiom.

L054 supplies the actual distinct-terminal graphs, their explicitly written suffix trees and local ordinary-Frege proofs for f₀=C(x,0) and f₁=C(x,A)+1. L053 §§4–7 and §9 supply the previously checked closure, row-invariant and balanced-list proof operations. Here their applicability is justified using L054's suffixes; **L053's width-two conclusion is not applied**. L048 supplies only its unconditional encoding conventions, not either existential size premise. L052's quasipolynomial theorem is comparison context, not a further input needed for the polynomial bound.

### 2. Fixed suffixes and finite left closure

Work separately with either f=f_j. L054 gives an ordered graph with N=2U vertices, U≤11s+2, at most 4U edges, source s_* and output t. Every edge label is 0, 1 or one original variable x_b, and every edge increases the vertex index. Write E₀ for the constant-one adjacency matrix and E_b for the x_b adjacency matrix, with multiplicities reduced modulo two. All matrices are strictly upper triangular. Zero-labelled edges contribute nothing. The source and output are distinct, and t has no outgoing edges.

Write S for the column of the SAME explicit suffix trees furnished by L054. This notation abbreviates fully copied formulas in every occurrence. Each S_u has at most 2U+1 arithmetic nodes and depth at most 2h+1, where h≤a log₂(s+2)+5. Their formal path semantics and ordinary-Frege coordinate proofs are

    S=e_t+E₀ S+sum_b x_b E_b S,       S_(s_*)=f.          (1)

In a coordinate, x_b precedes each suffix product. The terminal injection includes the empty path S_t=1. L054 proves all connectors, including the left product exit going to the right entry, constant/zero leaves and both substituted graphs. There is no graph unfolding or homogeneous-component formula in (1).

Compute the bit tables

    K₀=I+E₀+...+E₀^(N−1),   G_b=K₀ E_b,   beta=K₀ e_t. (2)

Strict triangularity gives E₀^N=0 and K₀ E₀=K₀+I. Each G_b is strictly upper triangular: a nonzero summand in entry (u,w) has u≤v<w for some v. All of these identities are checkable finite bit equalities. They are construction data used to select and cancel literal formula occurrences, not propositions about unknown matrix entries.

Take the K₀-linear combinations of the proved coordinates of (1). Expanding the finite sums, grouping bit coefficients and using K₀ E₀=K₀+I gives coordinate proofs of

    K₀ S=beta+(K₀+I)S+sum_b x_b G_b S
         =beta+K₀ S+S+sum_b x_b G_b S.

Cancel the identical K₀ S expressions from the two sides, obtaining

    S=beta+sum_b x_b G_b S.                             (3)

The required rules are fixed Boolean ring identities for XOR and AND, including distributivity, reassociation, permutation of XOR summands, pair cancellation and unit/zero laws. Bit coefficients may move past letters; no suffix is commuted across a letter. A coordinate comparison expands into at most c(n+1)(N+1)^3 copies of constants, S_v and x_b S_v, for a fixed c, even if all zero coefficients are initially written. Section 5 pays the actual proof lines of these transformations. This is a LEFT-closure convention, and includes constant-only suffixes in beta.

### 3. Exact-length coefficient witnesses and the finite boundary

Decompose each path at its variable edges. There is an initial constant-only segment, then the first variable edge, then another constant segment, and so forth, ending with a constant segment. Multiplication of finite matrices enumerates these choices with their F₂ parities. Consequently the coefficient of a word w=x_(b₁)...x_(b_i) in f is

    [w]f=e_(s_*) G_(b₁)...G_(b_i) beta.                 (4)

Indeed (2) makes its matrix product K₀ E_(b₁) K₀ ... E_(b_i) K₀. Every path has a unique such decomposition, including zero-length constant segments, so there is no overcount beyond the actual path multiplicities. For the empty word (4) is e_(s_*) beta. This proves the needed constant-edge specialization of the imported word-coefficient semantics without changing the formal alphabet.

For 0≤i≤N let V_i be the span of the rows e_(s_*) G_w for words of **exactly** length i, and choose a row basis R_i with r_i≤N rows. Set R₀ to the single row e_(s_*). From R_i, apply the standard span/coordinate procedure to the at most nN rows in all R_i G_b, selecting a basis of their span. Distributivity of right multiplication over spans shows that their span is exactly V_(i+1). Gaussian elimination supplies bit matrices T_(i,b) of dimensions r_i by r_(i+1) satisfying

    R_i G_b=T_(i,b) R_(i+1).                            (5)

No list of all words is constructed. There are N stages of polynomial-size F₂ elimination, hence polynomial bit time, with O((n+1)(N+1)^3) stored basis/transition bits up to fixed framing factors. This is the exact-length specialization of the inspected coefficient-space algorithm.

Because f is formally zero, (4) makes every generating row annihilate beta; hence every basis row does so:

    R_i beta=0  for all 0≤i≤N.                          (6)

A product of N strictly upper triangular N-by-N matrices is zero: a contributing entry would require N strict index increases among N indices. Thus V_N={0}, and R_N has **zero rows**. If the alphabet is empty, V₁ is already zero. A zero space at any earlier level has no successor candidates and stays zero. All empty matrices retain their actual dimensions. The proof requires neither a false terminal-row-vanishing assertion nor a homogeneous nonzero-degree promise.

Equations (5)–(6) are checked explicitly as bit tables before compilation. The semantic formal-zero promise ensures those checks pass for a valid input. Frege subsequently uses only the checked parities and the coordinate formulas, not the claim that a matrix is a basis or an external assertion of zero. In particular Boolean-only vanishing would not justify (6).

### 4. Backward proofs with no recursive suffix substitution

For a bit row r define L(r) to be a fixed balanced XOR list of the selected S_v, or 0 for the empty selection. Coefficients and the chosen order specify literal syntax. Every L(r) uses at most N copies of the same S_v. Establish, backward for i=N,N−1,...,0, the zero equality for L(r) for every row r of R_i. At level N there are no rows or premises.

Given the previously proved rows of R_(i+1), take row r's linear combination of (3). Equation (6) cancels its constant term. This gives a Frege equivalence

    L(r) = sum_b x_b (sum_v (r G_b)_v S_v).             (7)

For each b, the b-term in (7) is equivalent, by (5), to

    x_b (sum_j (T_(i,b))_(r,j) L((R_(i+1))_j)).         (8)

This is a paid syntactic comparison: expand the inner selected L rows into the S_v lists. The parity of each occurrence S_v is exactly the corresponding checked coefficient in (5). Sort the lists and cancel duplicate terms. Multiplication by x_b is distributed or factored with a fixed law. Across b there are at most nN² occurrences x_b S_v on either fully expanded side. Thus (7)–(8) involve polynomial-length lists of the actual suffix formulas, with no recursively generated invariant formula.

Every selected L((R_(i+1))_j)=0 is an earlier Frege theorem line. Use it via connective congruence to reduce the inner list in (8) to zero, then use x_b·0=0 and zero-sum laws. If r_(i+1)=0, (8) is an empty sum directly, and (5) says rG_b=0. This proves L(r)=0. Combining row equivalences and applying a previous line uses ordinary proof-line references: it does not copy the earlier proof into a later formula or declare a name for L(r).

There are at most N² row claims. At i=0, L(e_(s_*))=S_(s_*), up to removable zero padding. Together with L054's source identification, this gives an ordinary-Frege proof of Eval(f)=0 with the assignment variables free. Perform this twice, obtaining

    Eval(C(x,0))=0,              Eval(C(x,A))=1.         (9)

For the second graph f₁ is the actual tree C(x,A)+1, so its conclusion first reads Eval(C(x,A)) XOR 1=0. A fixed truth-functional law gives (9). There is no alternate evaluator whose equality is assumed without proof.

### 5. Balanced rewrites and one polynomial full-bit bound

Here is the syntactic cost justification for §§2–4 on these formula-origin graphs. Choose a fixed c so that R=c(Q+2) bounds N,n,U and all single input payload lengths for both graphs, with R≥2. There is a fixed b_a, depending only on a and the conventions, such that each suffix and each temporary local-interface proof line has depth at most b_a log₂R. L054 supplies polynomially many such lines. In this section a “term” always includes its fully copied suffix; it is only treated as a leaf when describing list rearrangement.

The closure and transition comparisons have at most c'(n+1)(N+1)^3 term occurrences per side. A fixed large power-of-two capacity M≤c''R^5 accommodates these lists, together with zero padding and intermediate distributions. Pad individual summation ranges to powers of two, with zero coefficients. There are only a fixed number of nested ranges in each expression: for example closure has vertex, successor and letter indices, and a transition has letter, basis-row and vertex indices. Balanced nested lists therefore have depth O(log R) above their terms; flattening them preserves a logarithmic bound. A single variable factor precedes a suffix, and distributing or factoring it never forms an unbounded multiplication chain.

The finite-list operations can be implemented as follows, spelling out the shallow-line requirement from L053 §6 and its audit.

* Distribute over a balanced sum recursively. Each branch adds at most that sum's logarithmic height to the context depth; the resulting term count is bounded by the displayed expanded count. For several nested sums there are only a fixed number of such heights. Inverse distribution traverses the same equalities backward.
* Regard all balanced padded leaves as fixed slots. To exchange adjacent terms, follow their paths to the lowest common ancestor. Associativity rotations expose the two neighboring terms with at most O(log M) intervening sibling blocks, apply commutativity to the exposed pair, and reverse the rotations. Throughout, the sibling chain and each untouched subtree each have height O(log M). The original balanced slot shape is restored before the next exchange. At most M² adjacent exchanges implement any requested permutation. Congruence is lifted one context node at a time using already proved equivalences.
* For a pair of equal neighboring terms use the same exposure, replace their sum by 0 using u XOR u=0, and then expand that zero to 0 XOR 0 if necessary to retain both slots. Restore the original slot tree. Keep zero slots during further transformations; fixed zero laws finally remove or add the needed padding. Pair cancellations therefore do not accumulate an unbalanced chain. Bit equalities specify precisely which literal copies pair. Constants 0 and 1 use the same procedure.
* A balanced XOR of already proved coordinate equalities is built upward along its binary sum tree. Previously established L(r)=0 lines can likewise replace one selected occurrence at a time through its ancestor contexts. None of these operations increases the number of nested summation ranges with i. Matrix notation is eliminated into these coordinate/list operations before producing a Frege line.

All local laws, including congruence, implication combination and equality transitivity, are fixed tautologies with fixed finite proofs in the chosen complete Frege system. Substitution into these fixed proofs is legitimate and writes a bounded number of copies of each actual argument. A use of an earlier equivalence is an inference from its already written line through such a schema; no arbitrary formula equivalence is an axiom. At each step the temporary formula depth is bounded by

    d_temp ≤ (b_a+c_*) log₂R+c_**,                      (10)

for input-independent constants c_*,c_**. The rotations above add logarithmic context depth, and the fixed schemas add only constant depth. A lifted congruence keeps its two surrounding expressions as the consequent; it does not nest all previous equivalence formulas inside a new formula. Thus the induction length N cannot multiply (10).

For explicit coarse counting, there are O(N²+N) principal row/closure claims and at most a fixed polynomial number of their coordinate combinations, distributions and coefficient comparisons. Each claim can be compiled using at most O(R^3) such list procedures, since all selected coordinate/basis/letter indices range over at most R and the expanded lists themselves have already been bounded. A list procedure uses O(M²(log M+1)²+M²) fixed-schema instances: sorting has M² exchanges, each with logarithmically many rotations and context lifts, and distribution/cancellation is cheaper within this bound. Hence, increasing a fixed multiplicative constant, R^30 bounds the number of temporary proof lines for both instances, including L054's O(U) schema instances, all coordinate combinations and the final guards of §6. This is deliberately a coarse upper bound, not a measured proof length.

Let d₀≥2 dominate the fixed argument duplication in the implementation of temporary connectives and the fixed schemas. By induction on depth, expanding a temporary binary formula of depth d into AND/OR/NOT gives at most c₀ d₀^(d+1) nodes, with a larger fixed d₀ if necessary. Equation (10) therefore bounds each ordinary-basis line by

    c₁ R^((b_a+c_*) log₂ d₀).

Multiplying by the polynomial number of lines yields a fixed polynomial total node count. Raw original names cost at most Q bits per occurrence; dense indices and proof references have O(log R) bits in this polynomial output. Charge every suffix copy, both substituted trees, graph and matrix tables, dictionaries, axiom occurrences, formula framing, rule tags and line-reference fields. Increasing the fixed exponent and constant gives a single KQ^k complete binary bound and polynomial construction time. There is no implicit shared formula in that accounting. Constants can be fixed tautology/contradiction formulas using an original variable, or one fixed auxiliary propositional variable if no original variable exists; it is not an extension variable or an assumed hypothesis.

### 6. Original-CNF guards and exceptional cases

If F has an empty clause, conjunction elimination and fixed constant laws give the desired direct polynomial proof. Otherwise each clause has one to three literals. Under Φ_F, its actual clause holds, so its ordered falsity product evaluates to zero by a fixed propositional calculation on those at most three literal occurrences. This applies equally to repeats and complementary literals, without padding or changing the formal clause polynomial. Boolean axiom x²+x and commutator xy+yx evaluate to zero unconditionally. Thus for every actual axiom position j there is a paid proof of

    Φ_F implies Eval(A_j)=0.                            (11)

Different placeholder positions retain their own dictionary names. Equal axioms may reuse a proved theorem line but all written copies are charged. Projections from Φ_F can be proved down its actual conjunction tree; even if deeply bracketed, it has ordinary AND/OR/NOT syntax of O(Q) nodes and polynomial total projection cost.

Replace placeholder occurrences in the ORIGINAL tree C one at a time. Use (11) at that leaf, then lift the guarded equality through its ancestor contexts by fixed guarded congruence schemas for XOR/AND. There are at most s replacements and O(log(s+2)) ancestors per replacement. During replacements every leaf contains either its bounded-size actual axiom or 0, so all intermediate C formulas have logarithmic temporary depth and polynomial ordinary-basis length. This constructs

    Φ_F implies Eval(C(x,A))=Eval(C(x,0)).               (12)

The possibly deep Φ_F stays outside the algebraic contexts. Each congruence schema has only a fixed number of copies of this guard; we never insert it beneath a recursively expanded XOR tree. Its written ordinary-basis cost therefore multiplies the proof bound by at most a fixed polynomial, and does not invalidate (10) for the algebraic subformulas. Combining (12) and (9) yields Φ_F implies 1=0 and hence ¬Φ_F.

With no original variables the empty-clause branch handles any unsatisfiable F; the formal construction also handles a zero alphabet through the empty-space rule of §3. If F has no clauses, all Boolean and commutator axioms vanish under every Boolean assignment. Evaluating the supplied identities would give C(x,0)=0=1, so no valid supplied package meets that case. No semantic step is used as an extra Frege axiom. The constructor on promised valid packages can include the direct empty-clause branch; malformed promises are outside the theorem.

### 7. Threshold, remaining obligations and traps

The achieved candidate threshold is one fixed KQ^k in the FULL SUPPLIED package, with constants independent of syntactic degree and certificate and allowed to depend on fixed a. The new applicability point is that L054's small shallow suffixes replace width-two suffixes throughout the SAME closure/row proof operations. It is not an application of a width-two theorem to a wider graph. No formal degree reduction, constant-free substitution or homogeneous-component tree bound is presumed.

Empty words survive in beta; only exact length N is killed by triangularity. The assignment stays free, formal coefficient equalities are not replaced by Boolean evaluations, and checked bit tables select actual tautological cancellations rather than becoming Frege hypotheses. The same explicit S_v occurs at every induction level; no recursively shared invariant is unfolded for free. Matrix dimensions may grow polynomially without widening any uncharged formula gate. Guard substitution uses the actual C and ordered A at both identities.

The separate critical audit of L054 and this assembly is recorded in §8. Its local comparison is stronger than the inspected general quasipolynomial receiver, and the delicate compiler has not been checked on emitted proof strings; no originality claim follows from an unmatched search or a favorable informal audit. Attempts 020/021/022/024 remain intact because none concerns this supplied-tree receiver. Certificate existence, arbitrary ER representation, formula-only bounds and unrestricted SAT transfer are not established.

### 8. Independent critical audit, 2026-10-11 (step 166)

**Scope and verdict.** The prior SPECIALIZE assessment `drafts/literature/2026-10-11-formula-origin-receiver-critical-audit.md` covers exactly this audit, for fixed a and both supplied formal identities. Complete L054/L055 were checked, with L053 §§4–7 and §9 as proof operations, L048's unconditional encoding, L018's exact graph and L052 as the quasipolynomial comparison. No width-two conclusion, existential certificate-size premise or ER representation is used. The source assessments' inspected LTW/Kiefer cases are reused with their recorded restrictions. No substantive mathematical defect was found. This verdict is informal and does not verify an implementation, a Frege proof string or mathematical originality.

**Closure, coefficients and the backward boundary.** L054 §5 verifies all actual suffixes and connectors independently. For the chosen ordering, E₀ is strictly upper triangular, and a nonzero entry of K₀E_b has indices u≤v<w, so G_b is also strictly upper triangular. Taking K₀-linear combinations of the coordinate recurrences gives K₀S on both sides and the additional S term from K₀E₀=K₀+I. Canceling the identical K₀S lists gives (3), with letters on the left of suffixes. Only bit scalars move across letters. No prefix-closure convention is substituted here.

The ordered coefficient expression is e_s K₀E_(b₁)K₀⋯E_(b_i)K₀e_t. A path has a unique decomposition at its letter edges, including zero-length constant segments and the final constant segment. For the empty word it is e_sK₀e_t. Thus the beta in (2), rather than e_t alone, is essential. Right multiplication of a spanning basis by every G_b spans exactly the next word-length space. Elimination gives r_i-by-r_(i+1) transition matrices, and formal zero implies R_i beta=0 for every i, including i=0. N strictly increasing transitions cannot occur in N indices, so R_N has no rows. With no letters R₁ is already empty; an earlier empty space stays empty. This checks the terminal induction without asserting that a nonempty last row or suffix vanishes.

Every row theorem is a balanced selected list of the same fully written S_v, independently of i. Expanding a row transition gives at most nN² occurrences x_b S_v, with exactly the checked parities in (5). Prior level theorems are used by their line references through fixed congruence rules, rather than by unfolding a recursively named invariant or copying earlier proofs into formulas. If the next space is empty, all the row's next coefficients are zero and no missing premise is required. The bit computations select literal copies for cancellation; neither the basis assertion nor a PIT answer appears as a propositional axiom.

**Concrete shallow list operations.** Write H=log₂ M for a padded balanced scalar list, and measure height above its actual term trees. The following checks justify the key bound in §5; they do not rely on a small semantic representation of an intermediate line.

To expose adjacent leaves p,q, their lowest common ancestor has p at the right boundary of its left child and q at the left boundary of its right child. Rotating along those two boundary spines exposes the sibling blocks and the pair. There are at most 2H sibling blocks, each of height at most H. Associativity produces an expression with the pair (p+q) and these blocks in their unchanged order. Its height is O(H), including the untouched outer context. Apply commutativity to the pair, then reverse the rotations; the original slot shape is restored before the next exchange. Each rotation can be lifted along at most O(H) context nodes. Thus an exchange uses O((H+1)²) fixed-schema instances, all of height O(H) above terms. At most M² exchanges suffice for any permutation.

For cancellation use the same exposure with q literally equal to p. Replace p+p by 0 and then by 0+0, and reverse the rotations with the two zero leaves in the two exposed positions. Reversing is valid because associativity has arbitrary formula arguments; it does not require recovering p. Both original slots therefore persist, and later cancellation cannot accumulate a long chain. Zero coefficients, constant parities and identical suffix occurrences are handled by these same fixed laws. Removing a zero slot by a unit law does not increase height.

Comparisons may start with different balanced or fixed-depth nested-list shapes. Ordered reassociation can be done without a flat left-associated list: split at the desired midpoint by rotations along its boundary path, preserving the sibling blocks in order, then process the two sides recursively. After a midpoint split the child trees consist of original subtrees plus one boundary chain, of logarithmic height. For subsequent splits, the active child's leaves form an interval of the original ordered list; its boundary consists of subtrees along at most two original paths plus the already balanced target ancestors. Those paths have O(log M) length for the fixed number of nested ranges. Hence all intermediate heights stay O(log M), including target contexts. Each split and lift takes polynomially many fixed-law steps, and there are at most M splits. Zero padding can be inserted in the same target shape. This covers the flatten/rebalance operation without an unpaid depth-M line.

Distribution of a single left factor over a balanced list processes its binary nodes. Intermediate expressions have the same logarithmic list skeleton with some nodes distributed and some still under that one factor. Only a fixed number of index ranges is nested in closure and transition comparisons; each contributes at most O(log R) levels. There is never a product chain indexed by the induction level. Inverse distribution has the same height bound. Combining coordinate equalities or replacing an earlier row theorem proceeds one context node at a time. A fixed congruence implication has the previous equivalence as a premise and the enlarged equivalence as consequent. Applying it and modus ponens keeps both actual contexts shallow; it does not nest the proof of the premise inside the consequent.

**Ordinary-basis and binary costs.** The suffix height is b_a log₂R, the padded capacity is at most a fixed constant times R⁵, and the checked list operations add only a fixed multiple of log₂R. Every algebraic line and every substituted fixed-schema proof line therefore satisfies (10), with larger fixed constants if needed. The fixed finite proofs exist by completeness of the fixed Frege system and are chosen once; their line counts and argument multiplicities are independent of the input. Substitution and inference from earlier lines are legitimate operations in the stated system.

The M² exchange bound, logarithmic rotation/lift overhead, O(R³) coordinate/list procedures per principal claim and O(R²) principal claims fit the deliberately generous R³⁰ line majorant after increasing its fixed multiplier. Distribution, midpoint reassociation, cancellations and row replacement fit that same polynomial. Expanding each temporary connective has fixed branching multiplicity, so a line of depth O(log R) has R^{O(1)} ordinary nodes, with exponent depending only on a and the system. Actual suffix copies are included in the depth and size, rather than treated as named gates. At most Q bits per original name occurrence and logarithmic reference fields in the polynomial output add fixed polynomial factors. Both tree substitutions, all axioms/dictionaries, matrix construction data and every proof occurrence are charged. The audit verifies existence of an input-independent KQ^k bound, without assigning an optimal exponent or reporting an emitted proof length.

**Guarded conclusion and qualifications.** Each actual axiom position evaluates to zero under Φ_F: the clause-falsity proof has at most three literal arguments, including repeats and complements, while Boolean/commutator cases use unconditional fixed laws. The placeholder replacements use that position's axiom tree in the original C, so the two unconditionally proved source values are precisely the two sides of (12). During each replacement all other leaves remain bounded axiom copies or zeros. Guarded congruence copies Φ_F a fixed number of times per instance and keeps it outside the expanding algebraic contexts. Expanding XOR consequently does not repeatedly duplicate its potentially deep conjunction tree. Ordinary projections and all copied guards have polynomial written cost. Empty clauses take the direct branch. A zero-clause F cannot admit both identities; no-original-variable valid packages fall within the empty-clause branch. Auxiliary variables used only to spell constants have no assumed axiom.

No argument or direct mathematical input changed, so the DAG and PROOF overview are not modified by this audit. The known quasipolynomial source comparison is not claimed to prove the polynomial compiler. No full matching Mathlib coverage or proof-string verification is asserted. The separately reviewable continuation is a bounded explicit compiler/checker test of the adjacent-exchange and cancellation operations; it would test the implementation rather than certify unrestricted SAT separation.

## Mathlib

Full matching coverage of this receiver, L054's suffix compiler and the complete ordinary-Frege encoding bound is **not checked**. The precisely cited Kiefer and LTW results support semantics, coefficient-space linear algebra and the receiving pattern, with the restrictions stated above; they are not asserted to be matching polynomial-receiver or Mathlib theorems. Unknown Mathlib coverage is not evidence of absence. No mechanized proof or checked propositional proof string is claimed.
