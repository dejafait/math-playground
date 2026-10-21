# L052 — Quasipolynomial ordinary-Frege bound for supplied affine ABPs

## Hypotheses

Use **only the unconditional encoding and axiom conventions in L048's Hypotheses**, over the free associative algebra F₂⟨x,t⟩. Thus F is an explicitly written occurring-variable width-at-most-three CNF; its written literal order, repetitions and complementary literals are retained. Its complete ordered axiom package is A=(c₁,…,c_m,B_x), with c_j the ordered product of literal falsity factors, and B_x consisting of Boolean axioms and pair-once commutators. Each axiom position, including a repeated clause, has its own independent placeholder t_a. Complete dictionaries store actual original names and deterministic A-position placeholder names.

Supply an explicitly encoded finite acyclic affine-F₂ edge-labelled graph C with designated entrance s and exit t and the ordered path-sum convention, including the empty path. Assume the two **formal** identities

    C(x,0)=0,                  C(x,A(x))=1.

The full |C| pays for vertices, edges, parallel edges, all affine-label records, endpoints, names, permitted-but-unused symbols, axiom lists and framing. Dead vertices, nonextremal endpoints, zero edges, cancellation, unequal path lengths, mixed labels and nonlinear placeholder paths are permitted. Circuit-valued labels and implicit graphs are excluded. Set

    Q=2+|F|+|C|+|A|,          H=log₂(Q+2).

Fix an ordinary complete Frege system with the bounded-arity connective/rule conventions of Li–Tzameret–Wang (LTW), and a binary proof encoding storing written formula occurrences, names and line references. Let Φ_F be the parenthesized conjunction of the actual written clauses, with empty disjunction false and empty conjunction true. The conclusion is a proof of ¬Φ_F, with no extension rule. No P_A, P_product, ER refutation, matrix receiver, universal witness bound or certificate finder is assumed.

## Conclusion

There are fixed constants K,k≥1, depending only on these encodings and the Frege system, such that a Frege proof of ¬Φ_F exists with complete binary length at most

    K Q^{k (log₂(Q+2))³}.

The intermediate identical-polynomial noncommutative tree formula has complete binary length at most K Q^{k log₂(Q+2)} after increasing K,k. The constants are independent of F and of the supplied certificate choice. These conservative bounds are not asserted optimal. This is a **REPRODUCTION/specialization of known conversion and simulation machinery**, not certified originality. It establishes no polynomial ordinary-Frege converse, formula-only certificate existence, arbitrary ER-to-ABP representation, every-certificate hardness or unrestricted SAT conclusion. The separate critical audit on 2026-10-11 (step 157), recorded in §6, found no substantive error; no propositional proof strings are verified here.

## Proof

### 1. Imports, scope and exceptional inputs

The prior SPECIALIZE assessment `drafts/literature/2026-10-11-affine-abp-quasipolynomial-frege.md` covers this exact target. Reuse its inspected source cases and the step-140 receiving comparison. The conversion input is Noam Nisan, *Lower Bounds for Non-Commutative Computation (Extended Abstract)*, STOC 1991, pp.410–418, §2 Definition 1 and Lemma 1(3)–(4), [DOI](https://doi.org/10.1145/103418.103462), [paper mirror, PDF pp.4–5](https://www.csa.iisc.ac.in/~chandan/courses/arithmetic_circuits/notes/noncomm.pdf). Its statement concerns homogeneous linear-edge ABPs over the reals. We use **its inspected ordered transition-matrix product and binary-circuit unfolding proof**, with the explicit applicability argument in §§2–3 below; we do not apply that homogeneous statement verbatim to affine DAGs. This local argument is necessary because the receiving graph and size convention differ. It uses only addition and ordered multiplication, so neither division nor characteristic-zero reasoning is needed.

The receiving theorem is Fu Li, Iddo Tzameret and Zhengyu Wang, *Characterizing Propositional Proofs as Non-Commutative Formulas*, [arXiv:1412.8746v4, 11 September 2015](https://arxiv.org/pdf/1412.8746v4), Definition 1.2 (printed p.6), Theorem 4.1 and following note (p.19), with its balancing Lemma 4.2. For a 3CNF and a size-s noncommutative formula-IPS refutation over GF(2), it gives an ordinary-Frege proof of the negated CNF of size s^{O(log s)}. The general quasipolynomial theorem is used, without a logarithmic-degree premise. Boolean and commutator axioms and both free-ring identities are part of its certificate definition. Its existing inspected proof cases are reused rather than rebuilt. The complete composition and binary ledger are the specialization in §4.

If the designated endpoints coincide, acyclicity permits only the empty s-to-s path, so C=1, contradicting C(x,0)=0. If there is no designated accepting path, C=0, contradicting C(x,A)=1. Thus a valid supplied certificate has distinct endpoints and an accepting path; zero-valued accepting paths or cancellations are not excluded by this observation. Scalar evaluation at any Boolean assignment makes every Boolean/commutator axiom zero and makes each clause axiom zero precisely when that clause is satisfied. The identities therefore imply that F is unsatisfiable. In particular a zero-clause F cannot satisfy the hypotheses.

An empty clause gives a direct Frege proof of ¬Φ_F: by conjunction elimination derive Φ_F→⊥, then ¬Φ_F by a fixed propositional derivation. The written subformulas, their copies and actual names cost a polynomial in |F|+2; even successively peeling an arbitrary binary conjunction tree uses at most O((|F|+2)²) symbol occurrences. This lies inside the claimed bound and avoids LTW's printed false-constant translation convention. In the rest of the proof every clause has one, two or three written literals.

### 2. Polynomial-bit layered affine normalization

Let v≥2 be the original vertex count and e its edge-record count. Both are at most bQ for a fixed encoding constant b. Delete incoming edges of s and outgoing edges of t. No s-to-t path in an acyclic graph uses either kind: re-entering s or leaving and then re-entering t would make a directed cycle. Hence this preserves the identical free polynomial, not just its Boolean values. All other vertices and parallel edges may be retained.

Add fresh vertices s₀,t₀ and label-one edges s₀→s and t→t₀. For this construction only, permit a waiting edge t₀→t₀ labelled 1. Let D=v+1. Form the **acyclic unrolling** with vertices (u,i), for each augmented vertex u and 0≤i≤D, and for each augmented edge u→w add the edge (u,i)→(w,i+1) with the identical label, for 0≤i<D. The designated endpoints are (s₀,0) and (t₀,D). The waiting edge therefore produces edges between consecutive layers, never a cycle in the output graph. Restrict layer 0 to its designated source and layer D to its designated output; prune other vertices not on a designated accepting path if desired. Outer layers are then singletons. This pruning uses graph reachability, never semantic noncancellation.

Each original s-to-t path has k≤v−1 edges. Its augmented path has k+2≤D edges and can reach layer D only by taking exactly D−k−2 copies of the waiting edge after first entering t₀. These waits are unique; nowhere else can a path wait. Conversely, an accepting unrolled path starts with s₀→s, enters t₀ via t→t₀, and thereafter only waits. Removing these three types of constant-one edges recovers exactly one original accepting path. Thus this is a bijection of accepting paths with **equal ordered products**. Products are equal in F₂⟨x,t⟩ because the inserted factors are 1, including the case of no final waits. All cancellations and arbitrary placeholder multiplicities are preserved. Consequently the unrolled graph computes exactly C, with both formal IPS identities unchanged.

The common width is at most W=v+2; absent states can be regarded as zero matrix rows/columns. There are at most (D+1)W vertices and D(e+3) edge occurrences. An original label is copied at most D times. Name payloads are either dictionary references or charged by copying their original written payloads; complete original/placeholder dictionaries and A are retained, including unused symbols. Dense vertex numbers have O(log(Q+2)) bits and each old name has at most Q bits. This gives, conservatively, a complete normalization length at most b₁Q⁴. No accepting-path enumeration, circuit-valued edge, homogeneous-component assumption or omission of the constant part is involved.

### 3. Ordered matrix product and tree unfolding

For i=0,…,D−1 let M_i be the W-by-W matrix whose (u,w) entry is the **sum** of all labels on unrolled edges from (u,i) to (w,i+1), with absent entries zero. Treat all matrices as having the full augmented state set. Initial/final restriction is obtained by the designated entry of

    M₀ M₁ ··· M_{D−1}.

The usual entry multiplication rule (UV)_{a,c}=Σ_b U_{a,b}V_{b,c} preserves left-to-right label order. Distributivity identifies its designated entry with the layered path sum by induction on the number of factors. Matrix multiplication is associative over an associative noncommutative algebra: expanding either parenthesization gives the same Σ_{b,c} U_{a,b}V_{b,c}W_{c,d}, in that order. This is sufficient for a balanced binary product tree; the matrices' entries need not commute.

Represent each input matrix entry by a binary affine formula. An affine term with coefficient 0 is omitted, a coefficient-1 symbol is a leaf, and the constant is 0 or 1. Retaining repeated occurrences in a balanced binary sum remains exact in characteristic two. Across the parallel labels of any entry, at most b₂Q input term occurrences are present before layer copying, so entry depth is at most b₃H and its complete name payload is at most b₄Q². Constant entries and missing edges are leaves. There is no field extension, division, interpolation or rank choice.

Build a binary product tree on the D matrices without permuting them. Its height r is at most ⌈log₂D⌉. At an internal node each entry is a sum of W ordered products; binary multiplication followed by a balanced binary sum adds depth at most 1+⌈log₂W⌉. Every circuit gate has fan-in at most two. The designated entry therefore has depth

    δ ≤ b₃H + ⌈log₂D⌉(1+⌈log₂W⌉) ≤ b₅H².

This is precisely Nisan's inspected matrix-product depth mechanism with affine entry-formulas paid explicitly. It is valid over F₂ because the preceding proof used only associative addition/multiplication and distributivity. It applies to our layered affine graph without first discarding constants or homogenizing.

Unfold the designated binary circuit gate recursively into a tree, copying shared gates whenever they are reused. A binary circuit of depth δ yields a tree with at most 2^{δ+1}−1 nodes: the bound follows from the full binary tree of that depth, regardless of sharing. This is Nisan's Lemma 1(4) unfolding mechanism, with no general circuit depth-reduction claim. Denote the resulting formula by T. It computes **the identical free polynomial C**. In particular T(x,0)=0 and T(x,A)=1; placeholders stay independent and no new symbols are introduced. Each symbol name has at most Q bits; syntax framing is constant per tree node, with polynomial extra overhead if node offsets are explicitly stored. Dictionaries and A add at most Q bits in their original supplied representation. Thus for fixed b₆,b₇,

    |T|_full ≤ b₆ Q^{b₇H}.

Indeed log₂ of the unfolding bound is O(H²), log₂Q is comparable to H for Q≥2, and multiplying by any fixed polynomial in Q or H² is absorbed by increasing b₆,b₇. Unused permitted symbols remain in the complete dictionaries; no dense-name convention hides the actual payload.

### 4. Receiving hypotheses and complete Frege ledger

T is a tree noncommutative formula over GF(2) with LTW's two formal identities and original clause/Boolean/commutator package. Under GF(2), subtraction and addition coincide. Positive literal falsity is 1+x_i and negative literal falsity is x_i, in the actual written order. A Boolean axiom is x_i²+x_i and a commutator is x_ix_k+x_kx_i. Pair-once commutators suffice as in Definition 1.2; duplicate clause polynomials still have distinct placeholder positions. These are exactly the original equations, without scalar positional substitutions or a matrix receiver.

Here “3CNF” uses clauses of width at most three. The previously inspected bounded-width receiving proof cases also apply to widths one and two: the arithmetic translation is the ordered product of that clause's actual falsity factors, and its Boolean identification uses at most three factors. Removing a factor reduces this fixed local cost. Literal repetitions and complements do not change the identification on Boolean assignments. **No padding by repeated literals** is used, since that could change the formal clause polynomial; no clause is reordered or deduplicated. The empty-clause case was treated separately in §1. Retain the final formula ¬Φ_F in its actual clause order/parenthesization; elementary associativity/conjunction-identification proofs handle any fixed binary bracketing with polynomial overhead in the written CNF.

Let s be the tree node count after any balancing used in LTW Lemma 4.2; that lemma preserves the polynomial with only polynomial formula growth. This balancing is part of the receiving theorem and preserves noncommutative factor order; no graph evaluator is asserted to be a Frege formula without the paid unfolding of §3. Set R≥2 to a fixed polynomial majorant of s+Q and all formula/dictionary occurrences in the receiving instance. Then

    log₂R ≤ b₈H².

To make the dependence on the written axiom list explicit, each substituted placeholder is replaced by its actual axiom **formula**, not a shared circuit. Clause formulas have at most three factors, Boolean formulas constant size, and commutator formulas constant size. Each occurrence has at most a fixed multiple of Q bits with original name payloads. Formulas for T(x,0) and T(x,A), and the constant additions needed by the receiving simulation, therefore have complete size polynomial in |T|_full+Q and are charged in R. They are identities established by the imported simulation, not assumptions supplied as uncharged Frege axioms. Dictionary/alphabet counts, n and m, are at most bQ. If the symbol-count presentation of the receiving theorem suppresses these parameters, a polynomial factor in R pays them: equivalently its certificate size can be enlarged to at least these counts by adding syntactically written zero sums, which preserves both formal identities.

Theorem 4.1 now supplies at most R^{b₉ log₂R} Frege symbol occurrences, after increasing b₉ to cover polynomial preprocessing and fixed small cases. Let P=max(2,R^{b₉ log₂R}). Actual original names cost at most Q bits at each occurrence. The final ordinary-Frege proof contains no extension variables or unpaid circuit names; formula syntax is written explicitly. Line numbers/references have O(log₂(P+2)) bits, and the number of lines is at most the number of written symbol occurrences up to a fixed encoding factor. Hence a conservative full binary bound is

    |π|_bits ≤ b₁₀(P+Q+2)².

This includes original name payloads, all copied proof/formula occurrences, line-reference fields, rule tags, framing, and the written conclusion. Because Q≤R, the factors Q and log₂(P+2) are bounded by a fixed polynomial in P+Q+2. Therefore

    log₂ |π|_bits ≤ b₁₁(1+(log₂R)²) ≤ b₁₂H⁴.

For Q≥2, H/log₂Q is bounded by 2. Increasing fixed K,k gives

    |π|_bits ≤ K Q^{kH³},

as claimed. This proves the conservative composed bound, not a polynomial bound. It is an existence statement from a supplied valid certificate; no extraction of a certificate from F or arbitrary ER proof, and no uniform Frege proof finder from F, is concluded.

### 5. Threshold, dependencies and limitations

The achieved Q^{O((log(Q+2))³)} full-bit bound meets this turn's proposed quasipolynomial threshold. The direct inputs are L048's package conventions and the named Nisan/LTW mechanisms; no conditional size premise of L048 is used, and L038's EF/ER simulation is comparison context only. There is no call to PIT as an unproved Frege oracle, no scalar/matrix replacement of noncommuting variables, no degree-only circuit-to-ABP converter and no enumeration of all paths. Attempts 020/021/022/024 remain unchanged.

The main gap is still unrestricted SAT complexity. Even with a formula-length polynomial ABP existence premise, this comparison would yield a quasipolynomial, rather than polynomial, ordinary-Frege bound. That existence premise itself is unproved. Arbitrary ER-to-ABP representation, every-certificate lower bounds, proof-system decision transfer and the independent W/V/U/fidelity obligations remain unresolved. The result is local progress using already assessed sources, without a claim of progress beyond their mathematical machinery.

### 6. Independent critical audit, 2026-10-11 (step 157)

**Scope and verdict.** The prior SPECIALIZE assessment `drafts/literature/2026-10-11-affine-abp-quasipolynomial-frege-critical-audit.md` authorizes precisely this audit. The complete argument above and L048's unconditional conventions were checked, reusing Nisan conversion coverage from steps 154/156 and LTW receiving coverage from step 140. LTW v4 Definition 1.2, Theorem 4.1, Lemma 4.2 and the complete Lemma 4.4 receiving argument (printed pp.6,19–23 of the linked primary PDF) were reopened to check the actual interfaces. This is an application audit, not a reproof of LTW's identity-proof theorem. No substantive mathematical defect was found. The author's given name was corrected to Zhengyu; that bibliographic correction is not a mathematical advance.

**Paths and endpoints.** An s-to-t path cannot use an incoming edge of s or an outgoing edge of t in a DAG, since it would repeat that endpoint. Deletion is safe even for nonextremal endpoints. For s=t the empty path is the only path and contributes 1; for distinct endpoints with no path the sum is 0. The two formal identities respectively exclude those cases. Existence of a graph path does not imply a nonzero polynomial contribution, and no pruning tests semantic nonvanishing.

For an original accepting path of length k, first arrival at t₀ in the augmented graph is exactly step k+2. Since k≤v−1 and D=v+1, the remaining D−k−2 steps are nonnegative and have exactly one possible realization: copies of the sole waiting edge. Conversely an accepting unrolled path starts with the fresh entrance edge, enters t₀ through t, and cannot leave t₀. Its earlier edges are original DAG edges. Removing the entrance/exit edges and final waits is inverse to augmentation. Parallel-edge choices remain distinct until summation. All inserted factors are 1 in their actual positions, so the bijection preserves word expansions with multiplicity, including cancellation over F₂. The boundary k=v−1 uses zero waits. Restricting the outer layers removes no accepting path; padding absent states with zero matrix entries cannot add one.

There are at most (D+1)(v+2) vertices and D(e+3) edges before pruning. Original affine terms and raw names are copied at most D times, plus the new constant records. Dense vertex identifiers have O(log(Q+2)) bits. Complete input dictionaries are already paid in Q, so O(Q⁴) is conservative for the full output, including dead states and repeated labels. No path enumeration occurs.

**Ordered formula and balancing.** Expanding a product entry concatenates a prefix and a suffix at their unique middle state and multiplies their labels in that order. Induction on intervals of layers proves the designated-entry identity. Associativity changes bracketing alone. This uses neither commutation of algebra entries, division nor homogeneity. It justifies applying Nisan's inspected proof mechanism over F₂ without importing his real homogeneous statement verbatim.

Each entry has at most O(Q) original affine-term occurrences before layer copying, giving depth O(H). At each of ceil(log₂D) matrix-product levels, entry depth increases by at most 1+ceil(log₂W). Thus δ=O(H²). A binary circuit of depth δ unfolds into at most 2^(δ+1)−1 nodes, counting all duplicate occurrences. Actual names cost at most Q bits per leaf and optional offsets O(H²) bits per node; consequently log₂(|T|_full+2)=O(H²). The identical polynomial survives both substitution homomorphisms, even with nonlinear placeholders and cancellation. Balancing applies to this paid tree. LTW's temporary context variables disappear on recomposition with the ordered left and right factors. The balanced formula itself is a certificate, so no Frege proof equating a graph evaluator to it is a missing premise.

**Exact receiving package.** Definition 1.2 uses one commutator for each i<j. Its Boolean polynomial x_i(1−x_i) becomes x_i+x_i² over F₂, exactly x_i²+x_i in the free algebra by commutativity of addition. No multiplication is commuted. Clause positions and placeholder names match injectively, even for equal clause polynomials. Dense source indices can be renamed to actual supplied names without identifying distinct symbols.

For a clause of length r∈{1,2,3}, its Booleanized falsity product is the ordered AND of the negations of its actual literals. The clause implies the negation of this AND. There are finitely many arity/sign patterns on at most three formal atom positions; completeness of the fixed Frege system gives fixed proofs of these constant-size tautologies. Substitution of identical atoms for repeated variables, including complementary literal occurrences, preserves the proofs. No factor is added to the free polynomial. This verifies the local implication used by Lemma 4.4 at widths one and two as well as three. Its truth predicate may sum over the actual r positions; for fixed clause codes, the index comparisons simplify to the actual literals at polynomial cost. When n=1, the same direct fixed tautology avoids any zero-bit index convention.

Booleanized Boolean axioms and commutators are identically false, with fixed Frege proofs on at most two atom positions. Under Φ_F every clause axiom is also false by the preceding implications. Hence the full A tuple is false componentwise under Φ_F, precisely the replacement premise in the receiving argument. This does not turn Boolean vanishing into a formal identity: both formal identities are already properties of T, and their short Booleanized proofs are supplied by the imported LTW theorem. Replacement within T pays for its actual formula copies. Empty clauses instead use §1's direct proof; a no-clause formula cannot receive a valid C.

**Complete exponent.** Put U=|T|_full+Q+2. The audit gives log₂U≤cH². Polynomial balancing, constant-size axiom formulas per placeholder occurrence, repeated dictionaries and the written conclusion are bounded by R=U^a for a fixed a, increasing constants if needed. Thus R≥Q and log₂R=O(H²). The general LTW bound, with polynomial preprocessing absorbed, gives a symbol budget P≥2 satisfying log₂P=O((log₂R)²)=O(H⁴). No logarithmic-degree premise was introduced.

Bounded-arity inference rules use O(P) reference fields, each of O(log(P+2)) bits; actual names cost O(PQ) bits. Syntax, framing and the conclusion are also paid. In particular P(Q+log(P+2)+1)+Q≤c₀(P+Q+2)². If a choice of Frege presentation introduces auxiliary proof variables, specialize all those absent from ¬Φ_F to a fixed Boolean constant, preserving the proof rules with polynomial overhead. They need not carry unpaid fresh names, and no extension rule is used. Fixed polynomial Frege-presentation conversions are absorbed as well. Therefore log₂|π|_bits=O(H⁴). For Q≥2, H≤2log₂Q implies H⁴≤2H³log₂Q, giving exactly KQ^(kH³). The claimed full-bit threshold survives; it is not polynomial.

**Decision and limits.** The direct local mathematical input remains L048's unconditional conventions; no DAG edge changes. Attempts 020/021 concern other polynomial representation conversions, and Attempts 022/024 concern different all-certificate/matrix claims. None is reopened or contradicted. No certificate finder, formula-length existence bound, ER representation theorem, polynomial ordinary-Frege converse or SAT decision conclusion has been added. This audit establishes no new bound and repairs no mathematical error, so its completed outcome is RESEARCH / REPRODUCTION / EXPLORATION. The original argument and its independent unresolved premises are unchanged.

## Mathlib

Coverage of the complete ABP-to-formula/full-bit Frege specialization, Nisan's conversion and LTW's proof simulation is **not checked**. No absence claim is made, and no Mathlib theorem is used as a substitute for a cited primary theorem. The proofs here are informal; structural document validation is not proof verification.
