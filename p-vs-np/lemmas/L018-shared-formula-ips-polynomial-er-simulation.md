# L018 — Shared formula-IPS assembly with polynomial binary EF/ER length

## Hypotheses

Fix standard circuit Frege (CF), extended Frege (EF) and ER calculi with the full binary encoding and fresh AND-extension convention in [the proof-system foundation](../foundations/05-refutation-systems-and-simulation.md). Let F be a well-formed CNF of width at most three, with n distinct base variables and m clauses. Write Phi for its ordinary propositional conjunction. Dense relabeling is allowed, but all original binary identifiers must be restored and charged.

Over F₂, the falsity factor of a positive literal x_i is 1+x_i, and that of a negative literal NOT x_i is x_i. Encode each clause by the product of these factors in its supplied order, with the empty product equal to 1. The explicitly supplied axiom list A(x) contains these clause polynomials, every Boolean polynomial x_i x_i+x_i, and the base-variable commutators x_i x_j+x_j x_i for i<j. Repeating commutators changes only polynomial bookkeeping. Placeholder variables y index this list.

Let C(x,y) be a supplied division-free, fan-in-two noncommutative **tree formula**, with coefficients in F₂, s nodes and ordered multiplication. It is in the screened balanced-input scope: its depth is at most a log₂(s+2) for one fixed a>0. Its two requirements are formal identities in the free noncommutative polynomial ring:

    C(x,0)=0,                 C(x,A(x))=1.                       (1)

There is no logarithmic syntactic-degree restriction. Set

    T=2+|F|+|A|+|C|,

counting all explicit syntax, coefficients, variable/placeholder identifiers and axiom entries. An arithmetic circuit certificate, a Boolean-only identity, a division gate or a field other than F₂ is outside the statement.

## Conclusion

There are fixed constants K,e such that one can construct an EF proof sigma of the **formula** NOT Phi and an ER refutation rho with the clauses of the original F as its original premises, satisfying

    |sigma| + |F| + |rho| <= K(T+2)^e.                          (2)

The construction has polynomial running time in T and can reject invalid encodings or identities in polynomial time. The degree of this polynomial is fixed independently of C's syntactic degree. Thus a family with polynomial total binary length of supplied certificates in this fragment has polynomial ER refutations.

This closes the screened arbitrary-degree, shared-component assembly obligation using L017. It does not supply certificates for arbitrary UNSAT formulas, lower bounds for their certificates, unrestricted EF/ER lower bounds or a passage from proof size to SAT decision time. It is a local informal result requiring critical review, not a candidate resolution of P versus NP. Known representations and proof conversions are imported; the explicit shared identification/assembly and binary accounting are potentially beyond the checked source comparison, without a certified originality claim.

## Proof

**Imported inputs and the identified difference.** Use the standard formula-to-ABP and constant-edge/component construction in Raz and Shpilka, [*Deterministic Polynomial Identity Testing in Non Commutative Models*, author-hosted 16-page manuscript, §2.1–2.2, Lemma 2, its five construction steps, and Theorems 4–5, printed pp. 4–10](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf). The [inspected source note](../drafts/2026-10-03-shared-homogeneous-ips-source-notes.md) preserves its version and zero-constant-term qualification. Degree zero will be checked separately below; the component ABPs represent only positive degrees. No new PIT theorem is needed.

L017 supplies polynomial shared CF/EF zero proofs for the specified homogeneous ABP evaluations, using imported coefficient-space witnesses. The ordinary formula simulation in Li, Tzameret and Wang, [*Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, 11 September 2015, Theorems 1.7/4.1, Lemma 4.4 and Theorems 4.11–4.12](https://arxiv.org/pdf/1412.8746v4), is not imported as a polynomial arbitrary-degree simulation: its general stated formula cost is quasipolynomial. Its reflection step is a supporting match, not the missing shared identification. Hrubeš and Tzameret's [*Short Proofs for the Determinant Identities*, §3, Lemmas 3.1–3.2, printed pp. 15–17](https://users.math.cas.cz/~hrubes/PDFs/DetSIAM.pdf), supplies short circuit decomposition proofs in a commutative arithmetic system; it is not used as a proof that an arbitrary noncommutative zero circuit has short zero proofs.

We fix a concrete version of the known formula/ABP representation and prove its Boolean identification. This is required because semantic equality of two encodings alone does not give a short CF proof. All Boolean circuits below use XOR for addition and AND for multiplication. Unless explicitly named as propositional variables for an application of L017, their nodes are circuit references, not additional unproved premises.

**Size of the two substituted trees.** Form the trees

    f_0=C(x,0),                f_1=C(x,A(x))+1.

Every width-three clause polynomial has at most 11 arithmetic tree nodes; Boolean and commutator polynomials have at most five and seven nodes respectively. Copy every substitution occurrence. Each tree therefore has at most U=11s+2 nodes. Its degree is at most 3s, but no bound logarithmic in n is used. Their Boolean evaluations are circuits of O(U) gates, using a fixed constant-size implementation of XOR. Sharing in these circuits avoids a Boolean tree expansion. The input remains the explicit arithmetic tree, not an arbitrary shared arithmetic circuit.

We first construct a polynomial CF proof of the zero Boolean evaluation of any supplied formally zero tree f of this size. The same construction will be used twice.

**A specified constant-edge graph.** For every occurrence v of a tree node, create distinct terminals s_v,t_v. A leaf has one edge from s_v to t_v, labeled by its constant or variable. For an addition node with disjoint child graphs L,R, add constant-1 edges

    s_v -> s_L, s_v -> s_R, t_L -> t_v, t_R -> t_v.

For a multiplication node, add constant-1 edges

    s_v -> s_L, t_L -> s_R, t_R -> t_v.

Keep the children disjoint, even when they have identical syntax. This is the series/parallel formula-to-ABP construction in the imported representation result. It has N=2U vertices and O(U) edges. Number vertices in the recursive order s_v, all L vertices, all R vertices, t_v. The root source is 0, the root sink t is N-1, and all edges point to a larger index. Its path polynomial is f, with ordered products along paths; no monomial expansion is performed by the constructor.

Let E_0 be its constant-edge coefficient matrix and E_b its x_b-edge coefficient matrix. Combine parallel edges modulo two. All are strictly upper triangular N by N matrices. Over F₂ define the finite constant table

    K=I+E_0+...+E_0^(N-1),
    G_b=E_b K,                 b_b=e_0 K E_b K.                 (3)

The notation e_0 denotes the source row, not E_0. Triangularity gives E_0^N=0 and hence

    K E_0=E_0 K=K+I.                                       (4)

The entries of K are the known constant-path sums, including the empty path. Computing (3) and checking (4) is finite polynomial-time bit arithmetic. Each G_b is strictly upper triangular. These numeric facts are checked, not introduced as arbitrary symbolic identity axioms.

For 1<=k<=D=N-1, take a homogeneous ABP B_k with a single source in layer 0 and N vertices in each layer 1,...,k. Its first-layer x_b coefficient row is b_b. Subsequent-layer x_b coefficient matrices are G_b. Its sink is coordinate t in layer k. It has no constant edges. Its path coefficients are exactly the degree-k component of f: a path splits uniquely into a constant block before its first variable edge, a constant block after each variable edge, and k variable edges in their original order. The K factors in (3) are precisely those constant blocks. This is the applicability of the imported constant-edge/component construction. No path has more than N-1 variable edges. The degree-zero component is the ground bit

    c_0=e_0 K e_t.

For formally zero f, c_0=0 and every B_k has formally zero output. Grading here is by word length in the free polynomial ring. Boolean-zero but formally nonzero inputs do not imply these statements.

**Shared evaluation and the finite degree boundary.** In CF use the row circuits

    h_0=e_0 K,
    h_1=sum_b b_b x_b,
    h_k=sum_b (h_(k-1) G_b) x_b,  2<=k<=D,
    r=sum_(k=0)^D h_k.                                        (5)

Every component h_k(v) is a fixed-parenthesized XOR; empty sums are 0. Earlier h-values are shared circuit nodes. The total evaluation size is O(nDN²+DN+1). Checking the first table in (3) and expanding its constant coefficients proves

    h_1=sum_b (h_0 G_b) x_b.

Thus the same recurrence is valid for k=1 as well. In matrix notation put X=sum_b E_b x_b; multiplication appends x_b on the right of the preceding value. The recurrence is h_k=h_(k-1) X K.

There are polynomial CF proofs of

    h_k(v)=0 when v<k.                                       (6)

For k=1 the first table b_b has zero entry at coordinate 0: K is upper triangular and E_b K is strictly upper triangular. For k>=2 the only nonzero coefficients contributing to coordinate v have preceding coordinate u<v. If v<k, then u<k-1, and the previous zero equations discharge every such term. This is an induction over at most DN coordinates using local constant reductions. The last row h_D may have a nonzero t-coordinate; (6) does **not** assert h_D=0. Since the last row of every G_b is zero, it does prove

    h_D X K=0.                                              (7)

Summing the recurrences and using (7) gives

    r=e_0 K+r X K.                                          (8)

Multiply (8) on the right by the constant matrix E_0 and use (4):

    r E_0=e_0(K+I)+r X(K+I)
         =r+e_0+r X.

Cancel r in this XOR equation to obtain

    r=e_0+r E_0+r X.                                        (9)

These are circuit proof steps described below, not an appeal to their semantic truth or an unproved infinite geometric-series identity. Only the finite boundary (7) permits the summation in (8).

**Identification with the original graph and tree.** Let p_v be the shared circuit evaluating the original graph at vertex v in topological order:

    p_v=delta_(v,0)
        XOR XOR_(u<v, E_0(u,v)=1) p_u
        XOR XOR_(b,u<v, E_b(u,v)=1) (p_u AND x_b).             (10)

This is a circuit definition. Equation (9) is exactly (10) for r_v. At v=0 both values are 1. Induction on v, substituting the already proved p_u=r_u for earlier coordinates, yields p_v=r_v with polynomial circuit congruence cost.

Separately let f_v be the shared Boolean evaluation of the formula subtree at v. For every subtree, CF proves

    p_(t_v)=p_(s_v) AND f_v.                                (11)

For a leaf this is its edge recurrence. At an addition node, its child source values both equal p_(s_v); their sink identities and distributivity give p_(s_v) AND (f_L XOR f_R). At a multiplication node, the right child source value equals the left child sink, and the terminal recurrences give p_(s_v) AND f_L AND f_R. Only source terminals have incoming edges from outside their subtree. Thus each use of (10) in this induction is justified by the specified graph. At the root p_0=1, so (11) proves

    Eval(f)=p_t=r_t.                                        (12)

No formula/component equivalence is inferred from an external PIT answer. Equations (6)–(12) give explicit local identification proofs for this encoding.

**Why the identification proofs have polynomial CF size.** Use fixed Frege proofs of XOR associativity, XOR commutativity, cancellation, constant reduction, AND distributivity and connective congruence. Each is a tautology on a fixed number of variables. Standard circuit substitution, with polynomial cost, is recorded in Pudlák, [*Reflection principles, propositional proof systems, and theories*, arXiv:2007.14835v1, §2.1–2.2, pp. 4–5, Lemma 2.1](https://arxiv.org/pdf/2007.14835v1). Substituting circuits into these fixed proofs does not assume correctness of an arbitrary circuit identity.

Expand only the sums of a single coordinate identity, retaining references to all earlier h-circuits. Collect terms h_j(u) AND x_b (or h_j(u) when only a constant table occurs). For the largest identities in (8)–(9), a conservative O((D+1)(n+1)N³) bound counts occurrences per coordinate before collecting, including all intermediate indices of X K E_0. Coefficient parity is the checked table equality (3) or (4). Sort by the finite indices and cancel equal pairs. A list of H terms uses O(H²) adjacent swaps; each swap or cancellation can be lifted through its enclosing XOR context using O(H+1) congruence steps. Distribution and substitution into the similarly bounded sums have polynomial cost as well. This is the same local proof operation justified in L017, here applied to the explicit identification tables.

For (8), substitute each h_k recurrence only once, as a circuit equality, and distribute r into the sum of the h_k values; (7) removes the one boundary term. For (9), expand only constant matrix products and reduce their checked parities. For (6), (10)–(12), induction uses earlier equalities and polynomial-size contexts. No recurrence is recursively unfolded into words or formula trees. All these identification circuits have O((T+2)^5) gates as a conservative bound. There are O((T+2)^2) coordinate/support equations and O(T) subtree equations. The preceding term-list procedure bounds their total CF symbol occurrences by, for example, O((T+2)^24). The exact exponent is immaterial, but it is fixed; whole circuit descriptions per line, enclosing contexts and projection/congruence steps are charged.

**Application of L017 and discharge of its definitions.** There are two circuit encodings to distinguish. L017's recurrence is a flat XOR of individual products. A direct implementation of the matrix notation (5) can instead multiply a preceding-row XOR by x_b before summing over b. Parenthesization alone does not identify these circuits. Fix (5) in this latter, factored implementation, and explicitly define flat circuits

    a_1(v)=XOR_(b : b_b(v)=1) (1 AND x_b),
    a_i(v)=XOR_(b,u : G_b(u,v)=1) (a_(i-1)(u) AND x_b), i>=2.   (15)

Use exactly L017's fixed parenthesization, Boolean implementation and empty-sum convention in (15). Its initial scalar is 1, and the later layers have N coordinates. The evaluation of B_k is the prefix through a_k. The first-layer scalar gates in (15) are retained until their constant reductions are proved.

CF proves a_i(v) iff h_i(v), for every i,v, with the assignment free. At i=1 apply the fixed law 1 AND x_b iff x_b and the checked b_b coefficients. At i>=2 first replace each a_(i-1)(u) by h_(i-1)(u) using the preceding equivalences and AND congruence. For each b, distribute `(XOR_u h_(i-1)(u)) AND x_b` into the XOR of `h_(i-1)(u) AND x_b`, retaining only the indices with G_b(u,v)=1. Empty sums use 0 AND x_b=0. Reassociate the outer XOR to the flat order in (15); all old h-values remain circuit references. There are at most nN terms per coordinate and DN coordinates. Fixed distributivity, associativity and congruence proofs therefore give polynomial cost by the same term-list bound used above. This step is an explicit proof of the encoding identification, rather than structural congruence between different connective structures.

For each k>=1, apply L017 to B_k, whose formal zero output was established from (1) and the imported component construction. Let Delta_k and o_k be that lemma's specified gate-definition formula and output variable. L017 supplies an EF proof of Delta_k implies NOT o_k. Convert this supplied proof to CF using the standard EF-to-CF simulation. Rename its input gate variables to avoid the base-variable names. Then substitute the actual **flat** evaluation circuit for every original evaluation-gate variable, including constants and all internal XOR/AND gates. Construct each substitution circuit in the same topological order as those gates. A substituted elementary equivalence is consequently `P_g iff op(P_inputs)` with identical rooted circuits on both sides; constants and aliases have the same fixed local proofs. The output after substitution is a_k(t), not automatically the factored h_k(t).

The conjunction of all substituted definitions has a polynomial CF proof by reflexivity, local constant proofs and conjunction. Modus ponens yields NOT a_k(t); the already proved a_k(t) iff h_k(t) then yields NOT h_k(t). All original evaluation-gate variables have been replaced, and the EF-to-CF conversion already eliminates that proof's extension variables. No definition hypothesis remains and no assignment to x has been fixed. Separate copies of an identical flat circuit can be identified by structural congruence; the conversion to a factored circuit uses (15)'s explicit derivation.

For completeness, let M_k be the number of gates in B_k's flat evaluator, including its fixed connective implementations. Every rooted substitution circuit has at most M_k+n+2 nodes. The sum of their full rooted DAG descriptions, even if each is written separately, is O((M_k+n+2)^2) node occurrences. Across all components set M=sum_k(M_k+n+2)=O((T+2)^5); then the total is at most O(M^2). Dense reference names and at most T bits per original identifier give O(M^2(T+log₂(M+T+2)+1)) binary bits, still polynomial. Rooted circuits retain their internal sharing; this estimate does not unfold them into trees. Standard circuit substitution is charged in the supplied proof lengths plus these complete substitution descriptions.

The ground bit c_0=0 proves h_0(t)=0 by constant reduction. Combining it with the D positive-degree zero proofs gives r_t=0. Equation (12) now gives a CF proof of NOT Eval(f). Its intermediate conclusion is a circuit; no CF-to-EF conversion is invoked on this conclusion. This applies to f_0 and f_1, giving free-assignment CF proofs of

    Q_0=0,                  Q_A XOR 1=0,
    Q_A=1,                                                     (13)

where Q_0=Eval(C(x,0)) and Q_A=Eval(C(x,A(x))). Copies in the substituted arithmetic trees are retained and charged. Their corresponding C-node evaluation circuits have identical recursive syntax; any use of a shared axiom evaluation instead of a copy is justified by structural gate congruence.

**Both identities and the original CNF.** Under Phi, every clause falsity product evaluates to zero. For a width-at-most-three clause, this is a fixed local tautology relating its disjunction to the AND of the negated literals. XOR with 1 evaluates to literal negation by a fixed tautology. Boolean and commutator polynomials have the fixed proofs

    (x AND x) XOR x=0,
    (x AND z) XOR (z AND x)=0.

Projecting the appropriate clause from Phi, and using these local proofs, gives Phi implies A_j(x)=0 for every entry and each needed substitution copy. Their number and total length are polynomial in T. The original assignment remains free.

Induction on the gates of C then proves

    Phi implies (Q_A iff Q_0).                              (14)

The placeholder leaves use the proved zero axiom values, and the base-variable/constant leaves match. Every addition and multiplication node uses fixed connective congruence. This is the Boolean reflection step of Li–Tzameret–Wang Lemma 4.4 with an explicit shared-circuit implementation. It uses the clauses of F as hypotheses, not a CNF augmented with Boolean or commutator axioms. Equations (13) and (14) give a CF proof of the ordinary **formula** NOT Phi. This final conclusion has only F's original variables and polynomial formula length.

**One polynomial for all binary costs and conversions.** With U<=11s+2 and N=2U, both graphs have O(T) vertices, D=O(T), and n<=T. The total number of coefficient bits in all positive-degree component ABPs is at most

    O(sum_(k=1)^D n k N²)=O(nN^4)=O((T+2)^5).

Layer/vertex syntax and dense names add logarithmic cost. Even charging T bits at every occurrence for restored sparse variable identifiers, their complete total binary length is at most c(T+2)^6. Each individual input to L017 satisfies the same bound. Its witness generation and zero-proof construction have a fixed polynomial bound, say K_0(L+2)^e_0; D applications therefore have total cost at most c'(T+2)^(6e_0+1). Empty coefficient spaces are already covered in L017. Degree zero uses only the checked bit, including the empty variable alphabet.

The EF-to-CF conversions, circuit substitutions and definition discharges use fixed polynomial-time operations in these proof lengths and the polynomial-length circuit data. Compose their fixed polynomials with the preceding bound and the O((T+2)^24) identification bound. The reflection proof has polynomial length too. This gives one polynomial P(T) bounding all CF symbol occurrences and steps, with degree independent of N,D or C. It is an actual polynomial, unlike the previously known quasipolynomial formula-homogenization factor. None of the component circuits is unfolded.

If P bounds the number of written symbols and references, binary encoding and restoration of original names cost at most

    c(P+1)(T+log₂(P+T+2)+1),

still polynomial in T. Internal labels and inference references are densely named. Constants have one-bit coefficients; an original identifier uses at most T bits. No unbounded label, matrix or entire circuit is counted as a single unit-cost symbol.

Convert the resulting CF proof with formula conclusion NOT Phi to EF by Jeřábek, [*Dual weak pigeonhole principle, Boolean complexity, and derandomization*, 25 November 2003 author manuscript, §2, pp. 12–14, Lemmas 2.4–2.5](https://users.math.cas.cz/~jerabek/papers/wphp.pdf). The formula-conclusion restriction is satisfied **only at this final stage**. Use the standard polynomial EF/ER comparison recorded by Pudlák, §2.1, in its CNF-refutation formulation and the [checked reflection foundation](../foundations/06-reflection-specialization.md). It produces a refutation from the original clauses of F, introducing fresh definitions only, with no PIT or arithmetic axiom clauses as extra original premises. Fixed-connective definitions are converted to the fresh AND convention using a fixed number of gates; NOT is an opposite literal and OR is the negation of an AND on negated inputs. Fresh indices and inference references have polynomial binary cost as above.

An empty original clause already supplies the refutation and a constant-size local EF contradiction. Otherwise any valid (1) forces F unsatisfiable, so F cannot have zero variables and no empty clause. If a false constant is needed in ER, with an original variable x define z iff (x AND NOT x); its defining clauses derive NOT z. This handles constants without arbitrary unit assumptions. Compose the fixed conversion polynomials to obtain K,e in (2). On invalid inputs the polynomial syntax, finite matrix and imported ABP basis tests reject; no superpolynomial search for certificates or proofs is performed. This also gives a polynomial-time translator bounded on invalid inputs.

**Critical qualifications and finite verification.** The source scope is reused, not refreshed, for the unchanged covered target. The new step is the explicit shared identification and full assembly, rather than an imported claim of the full theorem or a reproof of semantic PIT. Balance is part of the screened input scope; the proof's internal sharing does not authorize replacing its tree by an arbitrary arithmetic circuit. The disjoint-tree construction is essential to N=O(U). No complete informal P-versus-NP argument results.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/shared-abp/check_formula_assembly.py`. Its independent noncommutative word expansion for small examples, direct graph evaluation, component/basis tables and Boolean evaluations passed 64 cases, 1,192 components and 237 assignments, including constant-only paths, mixed degrees, empty alphabets, degree-32 cancellation and both identities of two supplied IPS certificates. It detects omitted trailing constant closure and a corrupted closure table, and distinguishes the Boolean-zero commutator/Boolean axiom from formal zero. A draft test incorrectly required h_D=0; a one-edge variable example corrected it to the proved h_D X K=0. The final row is allowed to be nonzero. These checks establish finite indexing evidence, not verification of CF/EF/ER proof strings. The informal proof still warrants an independent audit of the constant closure, degree boundary, definition discharge and final conversion.

The 2026-10-04 binary-bound audit repairs the previously implicit flat/factored conversion with (15). Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/shared-abp/check_definition_discharge.py` for its six finite syntax/sharing cases. Direct factored substitution fails the claimed reflexivity check already for 1 AND x; flat substitution makes every elementary definition reflexive, and both evaluators agree on the checked assignments. Damaged AND definitions are detected. Full rooted descriptions are counted without unfolding, including sparse original names and a dense layered example whose unfolded root exceeds 10^14 nodes. The [audit record](../drafts/2026-10-04-shared-formula-ips-audit.md) gives the mathematical reasoning and limitations. This is an informal proof repair using standard local laws, not a new simulation theorem, a proof-string verification or certified progress beyond the checked literature.

## Mathlib

Coverage: **not checked** for the full arbitrary-degree shared simulation, its CF identification or ABP proof encoding. The direct Raz–Shpilka citation supports semantic formula/ABP representation and polynomial coefficient-space computation; Li–Tzameret–Wang supports the distinct formula simulation and reflection step; Hrubeš–Tzameret supports a different circuit-decomposition result; Pudlák and Jeřábek support proof operations/conversions with the stated restrictions. No inspected source is asserted to match this full binary-length statement or to establish originality. No Mathlib theorem name or absence claim is inferred from this calculation.
