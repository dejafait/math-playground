# L053 — Polynomial Frege reception of supplied width-two affine certificates

## Hypotheses

Use only the unconditional original-CNF, ordered-axiom and complete binary encoding conventions in L048. Thus F is an explicitly written occurring-variable CNF of width at most three; A contains its ordered clause-falsity products, Boolean axioms and pair-once commutators, with distinct position-named placeholders even for duplicate axioms. Work over F₂ in the free associative algebra. Supply an explicitly encoded layered affine-edge ABP C, with edges only between consecutive layers 0,…,d, each layer of width at most two, and singleton source and output layers. Its designated source and output are those singleton vertices. Parallel edges, constant terms, zero labels, cancellations, repeated symbols, unused dictionary entries and nonlinear placeholder paths are allowed. Assume the formal identities

    C(x,0)=0,                 C(x,A(x))=1.

Set Q=2+|F|+|C|+|A|, charging all records, names, dictionaries, axiom formulas, layers and endpoints as in L048. Circuit-valued labels and implicit layers are excluded. Fix an ordinary complete Frege system over the usual AND/OR/NOT basis and full binary proof encoding as in L052. Let Φ_F be the conjunction of the actual written clauses, with their actual literals and order. There are no extension axioms or gate names in the desired proof.

## Conclusion

There are fixed constants K,k such that F has an ordinary-Frege proof of ¬Φ_F of complete binary length at most KQ^k. The constants depend only on the encodings and fixed Frege system, not on d, F or the supplied valid certificate. The construction uses polynomial-time finite linear algebra and explicit propositional rewrites; it needs the supplied certificate, not a certificate finder from F.

This is a local informal result under the prior EXPLORE assessment `drafts/literature/2026-10-11-width-two-affine-abp-frege-scope.md`. It is classified POTENTIALLY_NEW solely for the unlocated full propositional-interface match, not as certified originality. The separate informal critical audit on 2026-10-11 (step 161), recorded in §9, found no substantive defect; no Frege proof strings were generated or verified. No width-two certificate existence theorem, arbitrary ER representation, polynomial bound for unrestricted ABPs, proof-system lower bound or SAT decision/separation follows.

## Proof

### 1. Imports and scope of the specialization

Nisan, *Lower Bounds for Non-Commutative Computation (Extended Abstract)*, STOC 1991, §2 Lemma 1(3)–(4), [primary-paper mirror, PDF pp.4–5](https://www.csa.iisc.ac.in/~chandan/courses/arithmetic_circuits/notes/noncomm.pdf), supplies the ordered matrix-product and binary-tree unfolding mechanism. Its homogeneous real-field statement is not invoked verbatim. L052 §3 already justifies this mechanism for affine F₂ entries using only associative addition, ordered multiplication and distributivity. Here the supplied width is two, and we must additionally give short proofs of the suffix recurrences. We do not apply L052's general quasipolynomial receiving bound as a polynomial theorem.

Kiefer, *Notes on Equivalence and Minimization of Weighted Automata*, [arXiv:2009.01217v1, §§1–3, Algorithms 1–2 and Propositions 2.1–2.2](https://arxiv.org/pdf/2009.01217v1), supplies word-coefficient semantics and forward-space linear algebra over a field. The exact-length specialization below uses the same span-and-coordinate operation at each length, as in Li–Tzameret–Wang (LTW), *Characterizing Propositional Proofs as Non-Commutative Formulas*, [arXiv:1412.8746v4, Definition 4.13 and Lemma 4.15, pp.32–35](https://arxiv.org/pdf/1412.8746v4). Over F₂ these are finite bit computations. Neither source is imported as a Frege theorem for this affine graph. The necessary specialization is explicitly described in §5, including all empty spaces and word lengths.

L038's bounded axiom word gadgets and finite constant closure are used with a suffix, rather than prefix, orientation. LTW's Lemma 4.4, pp.20–23 of the same version, supplies the standard final two-identity receiving pattern; §7 spells out its application to the present written formulas. L017's shared-gate invariant is comparison context only: no shared q-gates, EF definitions or circuit-Frege substitution are retained here. The assessed difference is the polynomial written suffix/proof interface, which requires the argument below instead of merely importing semantic PIT or the homogeneous formula theorem.

If d=0 the sole source/output path is empty and C=1, contradicting the first identity. An empty intermediate layer or no source-output path makes C=0, contradicting the second. Thus valid nonexceptional inputs have d≥1. If F contains an empty clause, use the direct polynomial Frege proof by conjunction elimination described in L052 §1. Otherwise every axiom has a fixed-size arithmetic formula: a clause has one to three ordered falsity factors; Boolean and commutator axioms have their usual two terms. Their actual name payloads are charged. Scalar Boolean evaluation of the identities also rules out a zero-clause F. No semantic noncancellation test is used to delete paths.

### 2. Polynomial written suffixes and their peeling proofs

Pad each layer with zero states to dimension two, and form 2-by-2 matrices M_i whose entries are balanced sums of the actual parallel affine labels, for 0≤i<d. Missing entries are 0; affine sums include the actual constants. Each leaf entry is a formula of depth O(log(Q+2)) and full length polynomial in Q. Temporarily regard + and multiplication as XOR and AND for propositional interpretation; §6 pays for their expansion into the fixed ordinary Frege basis.

Let D be the least power of two at least d. Pad the matrix list through D with identity matrices. This is formula notation, not an assertion that an expanded graph retains width two. A complete balanced interval tree on [0,D) defines every dyadic block product. Its entry formulas use the ordered rule

    (UV)_(a,b)=U_(a,1)V_(1,b)+U_(a,2)V_(2,b).

For each original layer i, cover [i,D) by its maximal dyadic blocks, in left-to-right order, and multiply these blocks with right association. There are at most log₂D+1 blocks. An empty interval is the identity. Expand every matrix entry as a tree, copying every repeated occurrence. Every root-to-leaf path crosses at most 2log₂D+2 matrix multiplication nodes; each entry multiplication adds at most two Boolean connective levels. With the entry leaves this gives depth O(log(Q+2)), hence polynomial tree size. For an original vertex u at layer i, define S^j_u as the designated output-coordinate entry of this suffix, after placeholder substitution j=0 or j=A. Each substituted axiom formula has bounded node count and O(Q) name bits, so the same depth and full-size bounds hold. At layer d the suffix is the designated output unit column; at the actual output its value is 1. All these formulas are written separately.

The following are polynomial ordinary-formula proofs, not merely semantic identities:

    S^j_(i,u) = sum_v M^j_i(u,v) S^j_(i+1,v).              (1)

To obtain them, expose the leftmost matrix of the first dyadic block in the suffix cover. If that block is not a leaf, split it into its two children. The matrix associativity step ((UV)W)=U(VW) moves its right child to the beginning of the remaining tail. Repeat down the left spine until M_i is exposed. The remaining list is exactly the maximal dyadic cover of [i+1,D), in right association. Already right-associated tail blocks are preserved. There are at most log₂D splits/rotations. Identity padding and i=d−1 reduce to constant matrix laws. During this procedure the exposed block, its right siblings and the old suffix tail have a total matrix nesting depth at most 3log₂D+4; every expanded entry therefore still has depth O(log(Q+2)).

For each associativity step and each of its four entries, distribute both sides into the four ordered triple terms U_(a,b)V_(b,c)W_(c,e), b,c∈{1,2}. Fixed scalar associativity/distributivity and additive rearrangement give a fixed proof schema for this entry identity. Substitute the actual entry formulas. Lift the four entry equalities through the surrounding matrix-expression context using scalar connective congruence, once per node of its fully expanded tree. That context has polynomial size by the preceding depth bound. Thus no matrix or intermediate entry name is introduced as a propositional variable, and no unbounded associativity identity is assumed as an axiom. Repeating for all O(d) suffixes gives polynomially many polynomial-size formula rewrites. This proves (1) with all copies charged. These recurrences, not an arbitrary formula-equivalence assertion, are the required local interface.

### 3. Substituted graphs and suffixes at every gadget vertex

Apply L038's edge splitting and bounded original-axiom expansion separately to C(x,0) and C(x,A). A width-three clause expands into at most eight ordered words of length at most three; Boolean and commutator axioms into at most two words of length at most two. Each word is an independent path with fresh internal vertices. An empty word is a direct constant-one edge. Zero-substituted placeholder terms are deleted, but all other paths remain. Parallel multiplicities are retained or canceled modulo two. This requires O(Q) records/vertices after dense renaming, with polynomial full bits. It preserves all nonlinear placeholder products and all formal cancellations. These graphs need not have width two.

For the second graph add one constant-one edge directly from source s to output t. Call the graphs H₀,H₁. Their formal polynomials are C(x,0) and C(x,A)+1, respectively, and hence both are zero. The source has no incoming edge and the output no outgoing edge. Every edge goes forward in a topological order, also after adding the direct edge.

Supply explicit suffix formulas at every vertex of H_j as follows. At each old vertex use the formula from §2, with its appropriate substitution. For H₁ only, replace the source suffix by S^A_s+1. At an internal vertex on a word path ending at old vertex v, use the remaining word letters, in order, multiplied by S^j_v. The remaining word has at most two letters. At t use 1. Because the source has no incoming edge, an internal word never ends at s; hence the exceptional added source constant propagates into no other suffix. Denote the resulting column of formulas by S. All entries have depth O(log(Q+2)) and polynomial full size, even after copying them separately for every vertex.

At a gadget-internal vertex the local suffix recurrence follows from at most three-factor associativity and the single outgoing word edge. At an old vertex, (1), distributivity of each explicit affine entry and the bounded word expansions of its axiom occurrences prove the recurrence. At s of H₁ add the direct constant-one contribution. At t the injection is 1. Repeated labels and words are handled by XOR cancellation, not by deleting semantically zero paths. Thus there are polynomial formula proofs of every coordinate of

    S = e_t + E₀ S + sum_a x_a E_a S.                     (2)

Here E₀ and E_a are the N-by-N F₂ adjacency matrices for constant-one and x_a edges of H_j, with multiplicities reduced modulo two. Matrix notation is shorthand for explicitly written sums of S_v formulas. There are no new gate variables. Every matrix is strictly upper triangular in the chosen ordering. Equation (2) holds as an ordered formal identity and its Boolean interpretation has the just-specified Frege derivation; all x_a factors remain to the left of suffix factors. Alphabet size n and N are O(Q).

### 4. Left constant closure, including the empty word

Compute and check the bit matrices

    K=I+E₀+…+E₀^(N−1),     G_a=K E_a,     beta=K e_t.      (3)

Since E₀^N=0, K E₀=K+I. Each G_a is strictly upper triangular. This is deliberately LEFT closure, appropriate to suffix columns; L038's prefix convention G_a=E_a K is not silently reused.

Take the K-linear combinations of the already proved coordinates of (2). Expand their finite sums and use the checked bit equality K E₀=K+I. This gives, coordinatewise,

    K S = beta + (K+I)S + sum_a x_a K E_a S
        = beta + K S + S + sum_a x_a G_a S.

Cancel the identical K S sums on both sides to derive

    S = beta + sum_a x_a G_a S.                          (4)

Every term here is a constant or a copy of S_v, possibly preceded by one x_a. The transformations only distribute finite lists, reassociate/reorder XORs, cancel paired identical terms, and apply fixed connective congruence. In a coordinate at most O((n+1)N³) occurrences suffice even before cancellation. The entries of K are checked bits, not unproved propositional hypotheses. In particular beta records constant-only suffixes, including the length-zero path at t. We neither discard degree zero nor replace constants by fresh letters.

### 5. Exact-word-length spaces and backward zero invariants

A path word in H has a unique decomposition into an initial constant segment, its first variable edge, the next constant segment, and so on, ending with a constant segment. The finite closure in (3) therefore gives, for every word w=x_(a₁)…x_(a_i),

    [w] H = e_s G_(a₁)…G_(a_i) beta.                    (5)

For i=0 this is e_s beta. The product order follows the path order. This verifies the applicability of the imported weighted-automaton coefficient semantics to epsilon edges after closure; no epsilon-edge theorem is presumed in the source.

Let V_i be the span of the rows e_s G_(a₁)…G_(a_i) over all words of length i. Use the standard coefficient-space span-and-coordinate algorithm to choose a row basis R_i. Set R₀=e_s and r_i=number of rows of R_i≤N. The rows of all R_i G_a span V_(i+1), so Gaussian elimination produces bit matrices T_(i,a) with

    R_i G_a = T_(i,a) R_(i+1).                           (6)

This is the exact-length layered use of the inspected coefficient-space construction, not a new PIT algorithm. It computes at most N+1 spaces of dimension at most N from at most nN candidate rows per step. It uses polynomial bit time and O((n+1)(N+1)³) stored witness bits, up to fixed polynomial framing factors. For n=0 the first successor space is empty. All empty matrices have their actual dimensions.

Because H is formally zero, (5) says every generating row of V_i annihilates beta. Consequently

    R_i beta=0  for 0≤i≤N.                              (7)

Every product of N strictly upper triangular N-by-N matrices is zero: a possibly nonzero product entry would require N strict increases among N indices. Thus V_N={0}, and R_N is the zero-row matrix. This is a finite stopping boundary. It does not claim that the last suffix, last evaluation row or an entire nonempty last basis must vanish. All entries in (6)–(7) can be checked directly before compiling the proof. The proof uses those bit equalities, not the assertion that a supplied matrix really is a basis.

Prove backward, for i=N,N−1,…,0, every coordinate of

    R_i S=0.                                             (8)

At i=N there are no coordinates and no premise. Suppose the coordinates at i+1 have already been derived. For a row r of R_i, take its linear combination of (4), use r beta=0, and sort/cancel coefficients using (6). In full matrix shorthand this is

    R_i S = R_i beta + sum_a x_a R_i G_a S
          = sum_a x_a T_(i,a)(R_(i+1) S)
          = 0.                                           (9)

For one row, expanding the middle expression gives at most nN² terms of the form x_a S_v; the parity of each occurrence is the checked coefficient in (6). Conversely distributing the last expression into the same terms gives exactly those parities. Sort the two finite lists, cancel equal pairs, and then use the previously proved zero coordinates of R_(i+1) S to reduce the factored expression to zero. When r_(i+1)=0 it is an empty sum directly. This specifies an actual sequence of fixed-law Frege rewrites and applications of earlier theorem lines. No component of a recursively defined q-vector is substituted. Each R_i S is just a balanced XOR of at most N of the SAME explicit S_v formulas from §3, regardless of i.

There are at most N² nonempty row claims, each using a polynomial number of polynomial-size lists and congruences. At i=0, R₀=e_s, so (8) proves S_s=0. For H₀ this is the Boolean value of the original balanced matrix-entry formula with placeholders zero. For H₁ it is that formula with axiom substitution, XOR 1. We have proved both required zero identities with the assignment variables free.

### 6. Ordinary Frege syntax and full binary ledger

We now justify the size assertions in §§2–5 without treating XOR, matrix notation or a rooted circuit as an unpaid gate. All sums are balanced XOR trees; all S_v formulas are the explicit trees constructed above. Let L=Q+2. For fixed constants c,b independent of the input:

* d,D,N,n≤cL, all coefficient/transition tables and their checks have L^{O(1)} bits, and there are L^{O(1)} coordinate claims.
* Every suffix and every intermediate expanded matrix-expression entry has depth at most c log₂L in the temporary XOR/AND basis. Every linear combination or transition proof line is a polynomial-size balanced list of these suffixes with bounded extra products, hence has depth at most b log₂L and at most L^{O(1)} occurrences.
* Finite sum distribution, comparison and cancellation can be implemented with polynomially many such shallow lines. Distribute a balanced sum recursively. Concatenate/rebalance the resulting polynomial term lists. To exchange adjacent terms, expose their two positions by rotations along the paths to their lowest common ancestor, exchange them using the fixed commutativity law, then restore a balanced tree. Each operation has O(log L) context depth; a polynomial-length list needs at most polynomially many adjacent exchanges. Cancellation is treated by bringing equal terms together and rebalancing. Thus no long left-associated XOR list is ever required. Congruence is applied node by node along these contexts with already derived equivalences.

Each local associativity, distributivity, constant, cancellation or congruence schema is a fixed tautology and has a fixed finite proof in the chosen complete Frege system. Substitute the actual formula arguments into that proof, writing every occurrence. A lifted equivalence may use an earlier theorem line as a premise; this is ordinary proof-line reuse and does not name the theorem's formula as an extension variable. Formula substitution in a fixed schema has size linear in the total written substituted occurrences, up to its fixed multiplicities. Equality notation here means Boolean equivalence, expanded as a fixed formula.

For example XOR may be implemented as (u∧¬v)∨(¬u∧v). At most a fixed number h of argument copies is made at each temporary connective. Expanding a depth-b log₂L binary formula into the fixed basis yields at most (2h)^{b log₂L+O(1)}=L^{O(1)} nodes. The same applies to every intermediate line and the fixed-law proof instances, whose depths have the same logarithmic bound with a larger constant. This is why balancing the scalar lists and the matrix suffixes matters. We do not claim polynomial conversion of arbitrary deep XOR trees. Constants can be primitive abbreviations or fixed ordinary tautology/contradiction formulas; in the latter case their fixed proofs and payloads are charged too.

For additional explicit accounting, take c₀ large enough that every temporary line has depth at most c₀ log₂L, and c₁ such that their number is at most L^{c₁}. These constants exist by the displayed matrix nesting bounds and the list bound O((n+1)N³), with at most polynomially many swaps per list and O(N²+d) claims. If each implemented connective has at most h copies of each argument, all written proof formulas have at most c₂ L^{c₀ log₂(2h)+c₁+2} total nodes, after increasing fixed c₀,c₁ to include local proof instances. This is a fixed exponent, not one depending on d or degree.

An original name has at most Q bits. Dense coefficient indices and proof-line references need O(log(L+P)) bits when P is the resulting polynomial node count. Complete input dictionaries and axiom lists have at most Q charged bits here; copying them per construction or occurrence adds at most a polynomial factor. Formula framing, rule tags, all root occurrences, all references and actual raw names therefore give complete proof length at most K₀Q^{k₀}. There are no implicit arrays in proof lines: matrix notation in the argument denotes the explicitly bounded coordinate/list construction. The linear algebra tables are construction data, not extra Frege axioms. This ledger also shows polynomial construction time for the specified rewrites and tables on valid supplied certificates; no polynomial-time test for arbitrary circuit identities is used.

### 7. Final original-CNF identification

Let T(x,t) be the source-output balanced matrix-entry formula from §2 before placeholder substitution. It has logarithmic depth and polynomial full length, and computes the identical formal polynomial C by the ordered matrix-product construction. The two results of §5 are ordinary-Frege proofs that Eval(T(x,0))=0 and Eval(T(x,A)) XOR 1=0, hence Eval(T(x,A))=1. The possible identity padding is removed by fixed constant laws; the source suffix at i=0 is the full balanced block, so there is no unproved alternative-evaluator equality here.

Under the formula hypothesis Φ_F, conjunction elimination gives each actual written clause. Its clause-falsity product evaluates to zero: positive literal falsity is 1 XOR x, negative literal falsity is x. This is a fixed-width propositional calculation on the at most three literal occurrences, valid also with repeated or complementary literals. Each Boolean axiom x²+x and commutator xy+yx evaluates to zero unconditionally by fixed laws. Thus polynomial Frege derivations give Φ_F→(Eval(A_a)=0) for every actual axiom position a. Duplicates keep their own positions and can reuse an established theorem line; all copies are paid. These are exactly the receiving hypotheses of LTW Lemma 4.4, without any placeholder-linearity requirement.

Use structural connective congruence on the explicit T tree to derive, under the same guard Φ_F,

    Eval(T(x,A)) = Eval(T(x,0)).

One may replace placeholder leaves one at a time, lifting their guarded equivalences through their ancestor contexts. There are polynomially many leaves and each context is a subtree of a polynomial-size, logarithmic-depth T with bounded-size axiom formulas at its leaves. All intermediate formulas and their ordinary-basis expansions have polynomial full length. Guards and the fixed propositional derivations for combining implications add only a polynomial factor. The actual parenthesization of Φ_F may be deep, but it uses ordinary conjunction and disjunction with no duplicating XOR expansion; its complete written size and all guarded copies remain polynomial. Its projections are ordinary explicit conjunction-elimination proofs.

Combining the guarded equality with the two unconditional identity proofs yields Φ_F→(1=0), then ¬Φ_F. This last assembly has polynomial full binary size in Q and uses no extension gate. Increasing K,k covers it, all input framing and the empty-clause case. The threshold achieved is one fixed polynomial in the SUPPLIED package Q, not a polynomial in |F| alone unless an additional certificate-size existence premise is supplied.

### 8. Limits and traps

The source graph's width two is used only to obtain polynomial written suffixes and their peeling proofs. The axiom-expanded graphs may be wide; their actual vertices and suffix formulas are paid. Formal zero is used for all R_i beta=0, including i=0; Boolean-only zero would not justify these coefficient equations. All constants, empty segments, parallel cancellations and nonlinear placeholder occurrences remain present. The boundary is R_N empty, not an incorrect last-row vanishing assertion. No external PIT answer is inserted as a Frege axiom, and no recursively shared invariant is unfolded for free. No exponential word list is enumerated.

Attempts 020/021/022/024 address different representation or importing claims and are neither contradicted nor reopened. This restricted supplied-certificate receiver leaves general representation, certificate existence, alternative-certificate hardness and unrestricted SAT complexity unresolved. The mathematical novelty of the interface is not established; §9 records the separate informal audit of the balancing/congruence ledger and its limitations.

### 9. Independent critical audit, 2026-10-11 (step 161)

**Scope and verdict.** The unchanged prior EXPLORE assessment `drafts/literature/2026-10-11-width-two-frege-critical-audit.md` covers exactly this audit. The complete proof above was checked against L048's unconditional package, L038's bounded word gadgets and L052's ordered matrix/encoding conventions. The already inspected Nisan, Kiefer and LTW source cases in §1 are reused with their recorded restrictions; no source theorem is promoted to an affine ordinary-Frege theorem. No substantive mathematical defect was found. This is an independent informal audit, not a generated proof-string check, a new receiver theorem or certified originality.

**Canonical suffixes and peeling.** Put m=log₂D. When the first maximal block is [i,i+2^q), splitting down its left spine exposes the leaf [i,i+1) and, in order, the right siblings [i+1,i+2), [i+2,i+4), …, [i+2^(q−1),i+2^q). These are exactly the maximal blocks needed to replace the old first block in the cover of [i+1,D); the old later blocks remain in order. If q=0, just remove the first leaf. The rotations in §2 right-associate these siblings with the old tail; they neither reorder factors nor expand the product into all complete words. For i=d−1 the remaining matrices are identities, and the coordinate constant laws give the chosen unit-column S_d. At d=D the tail is empty and the same unit column is the empty product. D=1 uses only this constant-law case. Padding singleton layers by a zero state contributes no extra path term.

During a peel, a root-to-leaf path crosses at most the old suffix-tail length, the exposed sibling-chain length, and the depth of one balanced block. Each is at most m+O(1); hence the stated bound 3m+4 on matrix nesting is sufficient. A 2-by-2 entry multiplication contributes one XOR and one AND level. Including affine-entry depth gives temporary scalar depth at most 6m+O(log(Q+2)), with an absolute constant. Distributing a single matrix associativity step into its four triple terms adds only constant depth, since the two summation indices each have two values. Lifting that fixed equality through all occurrences in a surrounding expanded entry tree uses its already polynomial number of nodes and logarithmic context depth. It does not unfold an ancestor proof or introduce a gate variable. These checks justify the syntactic recurrence (1), beyond equality of the represented polynomials.

**All substituted suffixes.** A split affine term has one symbol or constant edge. An axiom occurrence gives an independent word gadget with at most three letters. Its internal suffix is the remaining at-most-two letters followed by the actual old-vertex S_v; no other branch enters or exits its internal vertices. At old vertices, distributing the explicit entry sums and the bounded axiom trees gives precisely all these suffix contributions, retaining repeated words with their parity. A constant word is a direct edge and contributes S_v. The output has suffix 1 and no outgoing edge. The additional source-to-output constant edge contributes 1 only to S_s: consecutive layering makes the source indegree zero, so no old or internal suffix can reach it. Thus H₁'s modification does not require changing any other S_v. Dead or zero records, canceled parallel paths and multiple placeholders on a path cause no exception. Equations (1)–(2) are proved by these local formula equalities, without a polynomial-width assertion about the substituted graphs.

**Left closure and word lengths.** Since E₀ is strictly upper triangular, E₀^N=0 and K E₀=K+I, including the diagonal contribution of I. Each K E_a is strictly upper triangular: any contributing indices satisfy u≤v<w. The path decomposition gives exactly K E_(a₁) K … E_(a_i) K, so the source/terminal expression in (5) has G_a=K E_a and beta=K e_t in the stated order. Its length-zero coefficient is e_s K e_t. Applying K to (2) leaves the letter on the left of every suffix; bit coefficients can move across a letter, while suffix factors are never commuted across it. Pair cancellation of K S then proves (4). This is not L038's prefix orientation.

For exact length i, multiplying a spanning basis by every G_a spans exactly the next length, not the cumulative space. Finite Gaussian elimination therefore gives (6) with r_i-by-r_(i+1) coordinate matrices. Formal zero makes every generating word row annihilate beta and hence gives (7) for every basis row, including R₀=e_s. N consecutive strict index increases are impossible; consequently R_N has zero rows. At the terminal induction step there is no assertion about a nonempty row vector. If the alphabet is empty, R₁ and all successors are empty and the sole obligation is the checked length-zero bit. Empty spaces at earlier lengths stay empty. All these facts are consequences of the supplied formal zero identities, not Boolean-zero promises or unproved Frege axioms.

For a row at level i, the two sides of the transition comparison expand into at most nN² terms x_a S_v on each side, with bit parities equal by (6). Canceling equal pairs identifies the written middle and factored expressions in (9). Each selected row claim from level i+1 is an earlier theorem about the same explicit S formulas; multiplying its equality by x_a and combining balanced sums needs ordinary congruence and previous-line references only. The depth does not grow with the induction index. No formula for a recursively defined q-vector, or proof of the earlier row, is inserted into a later line.

**Shallow lines and complete costs.** Treat each S_v as an actual copied tree when measuring size and as a term boundary when sorting a list. The closure comparison has at most O((n+1)N³) such term occurrences per coordinate; transition comparisons have polynomially many as above. Recursive distribution over a balanced list increases context depth by its logarithmic height. Adjacent exchange exposes two consecutive leaves using rotations along their paths to their lowest common ancestor and restores the balanced template afterward. The temporary sibling chains have logarithmic length. Sorting P terms uses at most P² such exchanges. Identical adjacent terms cancel by the fixed XOR law; constant leaves can be retained and balanced or removed by the constant laws. Thus these operations use polynomially many lines of logarithmic temporary depth, rather than a left-associated list of depth P. Inverse distribution has the same bound. Fixed-law proof instances and nodewise congruence add only a fixed depth overhead to these actual contexts.

Since d,D,N,n are O(Q), both the number of term boundaries and the number of coordinate claims are bounded by fixed powers of L=Q+2. The suffix construction, local rotations, list comparisons and earlier-line applications consequently admit input-independent constants c₀,c₁ in §6. Expanding each temporary connective with its fixed argument multiplicity gives at most L^{O(1)} ordinary nodes per line; multiplying by the polynomial number of lines preserves a fixed polynomial. Original payloads have at most Q bits and all reference numbers have logarithmic length in this polynomial output. No dictionary, axiom copy, suffix occurrence or guard is represented by an unpaid circuit. This checks the claimed KQ^k threshold without deriving a particular optimal exponent or measuring an emitted proof.

**Final guards and limits.** For the explicit unmodified T, each placeholder replacement is guarded by the same Φ_F and justified at its actual axiom position. Width-one/two/three clauses, repetitions and complements use their actual bounded literal products; Boolean/commutator values vanish by fixed laws. The deep written Φ_F is copied as an ordinary AND/OR/NOT formula, so its depth causes no iterative XOR duplication. The guarded congruence proof copies Φ_F only a fixed number of times per proof instance; across polynomially many instances its cost is polynomial. The two unconditional source-suffix theorems therefore close the stated original-CNF proof. Empty clauses use the direct branch, while coincident endpoints or a no-path certificate cannot satisfy both identities. No extra assumptions, mathematical dependency edges or changes to the argument were needed. Certificate existence, arbitrary ER representation, unrestricted-ABP polynomial reception and SAT decision/separation remain unresolved. Full matching Mathlib coverage remains not checked.

## Mathlib

Coverage of the full receiver, the suffix proof compiler and the ordinary-Frege binary ledger is **not checked**. Nisan's matrix unfolding, Kiefer's coefficient spaces and LTW's specified semantic/receiving statements are cited with versions and restrictions above; none is asserted to be a matching Mathlib theorem. L038 provides the local bounded gadget/constant-closure construction, not a full ordinary-Frege result. Unknown Mathlib coverage is not evidence of absence.
