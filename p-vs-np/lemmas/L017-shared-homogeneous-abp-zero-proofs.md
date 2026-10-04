# L017 — Shared propositional zero proofs for homogeneous F₂ ABPs

## Hypotheses

Fix standard circuit Frege (CF) and extended Frege (EF) calculi and binary encodings. Let B be an explicitly represented homogeneous noncommutative algebraic branching program over F₂, with nonempty layers 0,…,d, d≥1, layer widths w₀,…,w_d, a specified source s in layer 0 and sink t in layer d. Edges go only from layer i−1 to layer i and have homogeneous linear labels in the explicitly listed variables x₁,…,x_n. Parallel edges are combined modulo two. There are no constant edges, divisions or implicit exponentially long layers. Variables may first be densely relabeled; their original binary identifiers remain charged.

Write M(i,a)∈F₂^(w_(i−1)×w_i) for the coefficient matrix of x_a at layer i. Thus the coefficient row of a prefix word x_(a₁)…x_(a_i) is

    e_s M(1,a₁) … M(i,a_i),

and the coefficient of a complete word in the output is its t-th coordinate. Assume the output polynomial is formally zero in the free noncommutative ring, rather than only zero on Boolean assignments.

For the explicit Boolean evaluation encoding, put p₀=e_s and define, over Boolean assignment variables that remain free,

    p_(i,v) = XOR_{a,u : M(i,a)_(u,v)=1} (p_(i−1,u) AND x_a).       (1)

Each sum has a fixed binary XOR-parenthesization; an empty sum is 0. Introduce names for the gates, using a fixed constant-size Boolean implementation of XOR, AND and constants. Let Delta_B be the conjunction of all their elementary defining equivalences, including the initial constant gates. Let o_B=p_(d,t) be the output name. Delta_B is an ordinary propositional formula of polynomial size, with the gate names as propositional variables.

Put L=2+|B|, including the full binary graph, layers, labels and variable list. If an evaluation encoding is separately supplied, also charge its full length in L. It must be the encoding (1), up to explicitly supplied gate aliases or a fixed choice of parenthesization; no equivalence proof for an arbitrary alternative evaluator is asserted.

## Conclusion

There are fixed constants K,e such that an EF proof of the formula

    Delta_B -> NOT o_B                                            (2)

can be constructed in time and full binary length at most K(L+2)^e. Equivalently, EF can derive NOT o_B from these evaluation definitions with the original assignment variables free. This is a proof of a specified evaluation circuit's zero value, with its defining hypotheses retained.

More generally, the construction accepts finite constant matrices R_i∈F₂^(r_i×w_i), r_i≤w_i, and T(i,a)∈F₂^(r_(i−1)×r_i), satisfying

    r₀=1,  R₀=e_s,
    R_(i−1) M(i,a) = T(i,a) R_i  for every i,a,
    R_d e_t = 0.                                                 (3)

Empty row spaces and matrices with zero columns are allowed. The construction checks every bit equality in (3) and produces (2) without assuming these equalities as propositional axioms. Formal zero ABPs have such polynomial-size witnesses by the imported coefficient-space basis construction.

This settles the screened shared-gate transition obligation. It does not identify an original formula with its homogeneous-component ABPs, assemble both formula-IPS identities or supply the total original-CNF ER simulation. The local propositional realization is potentially beyond the checked literature comparison; no certified originality is claimed.

## Proof

**Imported semantic witnesses, with the orientation fixed.** Use the coefficient-space basis construction in Raz and Shpilka, [*Deterministic Polynomial Identity Testing in Non Commutative Models*, author-hosted 16-page manuscript, §2.1–2.2, Claim 3 / Theorem 4, printed pp. 4–10](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf), and Li, Tzameret and Wang, [*Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, 11 September 2015, Definition 4.13 / Lemma 4.15, printed pp. 32–35](https://arxiv.org/pdf/1412.8746v4). The inspected scope and source versions are preserved in the shared-component source note. These supply the semantic linear-algebra witnesses, not the propositional proof being constructed here.

In row-vector notation, the length-i coefficient space S_i is spanned by the prefix-word coefficient rows. Choose R_i as a basis matrix of S_i. The imported layer-by-layer calculation forms S_i from the rows of R_(i−1)M(i,a), so their coordinates in R_i are exactly T(i,a) in (3). The source row is R₀=e_s. Formal output zero means that every prefix row at the last layer has zero t-coordinate; hence R_d e_t=0. These observations fix the applicability and orientation of the imported construction. They are not a new PIT theorem. A basis need not be proved to be a basis inside EF: the propositional construction below uses only the checked finite identities (3).

Let V=sum_i w_i and W=max_i w_i. Since every layer and its vertices are explicit, d,W,n,V≤L after including the variable list. Dense coefficient matrices and all R/T matrices have at most O(d n W²+d W²) bits, hence polynomial length in L. Over F₂, generating the bases, computing the coordinates and checking (3) are polynomial-time finite linear algebra. There is no word enumeration in that algorithm. The same bit checks suffice for separately supplied witnesses, regardless of whether their rows form bases.

**Shared coordinates and the invariant.** Addition below denotes XOR and multiplication denotes AND on Boolean values. Define auxiliary CF circuits

    q₀=1,
    q_(i,k) = XOR_{a,h : T(i,a)_(h,k)=1} (q_(i−1,h) AND x_a).     (4)

If r_i=0, q_i is an empty vector; every linear combination of its entries is 0. The circuits (4) are built in layer order and share their earlier q-gates. Their total size is O(d n W²+1); syntactic unfolding is never performed.

We construct CF proofs, under the single hypothesis Delta_B, of all coordinates of

    p_i = q_i R_i.                                               (5)

At layer 0, Delta_B gives p₀=e_s; R₀=e_s and q₀=1 give (5) by constant reductions. Now suppose the previous layer's coordinates have been proved. Equation (1), the previous invariants and distributivity give, coordinatewise,

    p_i = sum_a ((q_(i−1) R_(i−1)) M(i,a)) x_a
        = sum_a (q_(i−1) T(i,a) R_i) x_a
        = (sum_a (q_(i−1) T(i,a)) x_a) R_i
        = q_i R_i.                                               (6)

Here x_a is multiplied on the right of each preceding q-value. No permutation of the variables in a noncommutative word is used. The middle equality comes from the constant transition tables, not an assumed symbolic matrix identity. The next paragraphs explain an actual polynomial CF derivation of (6), rather than using its semantic truth as a proof.

**Local proof compiler.** Boolean XOR/AND obey the fixed associativity, commutativity and cancellation laws for XOR, distributivity of AND over XOR, the constant laws, and congruence for each fixed connective. Each such schema is a tautology on a fixed number of propositional variables and has a fixed finite Frege proof. Importing a fixed proof and substituting circuits gives a CF proof whose size is polynomial in the substituted circuit descriptions; this is the standard circuit substitution operation recorded by Pudlák, [*Reflection principles, propositional proof systems, and theories*, arXiv:2007.14835v1, Lemma 2.1, §2.1–2.2, printed pp. 4–5](https://arxiv.org/pdf/2007.14835v1). In particular, we do not assume an arbitrary circuit identity schema.

For a coordinate v, project the relevant definitions from Delta_B. Within that layer's evaluation circuit, induction in gate order proves that each named gate equals the corresponding circuit in the preceding p-wires and x. Each gate uses just its defining equivalence, its input equivalences and fixed connective congruence. This gives (1) under Delta_B with polynomial proof cost, retaining references to preceding-layer wires rather than unfolding the whole ABP. Substitute the already derived p_(i−1,u) equivalences into this recurrence. Distribute to a list of terms q_(i−1,h) AND x_a. The number of occurrences of the term with indices (h,a) is

    sum_u R_(i−1)_(h,u) M(i,a)_(u,v).

On the right of (5), substitute (4), distribute, and obtain the same kind of term list, with multiplicity

    sum_k T(i,a)_(h,k) R_i_(k,v).

All sums of multiplicities here are ordinary integers; their parity is the corresponding bit in (3). Each list has at most H=n W² terms. Sort the lists by (h,a), using adjacent swaps justified by XOR associativity/commutativity. Cancel adjacent equal terms by u XOR u=0 and eliminate zeros. Equality (3) says precisely that the two remaining lists are identical. This gives the desired equivalence through fixed local proof steps. Repeated occurrences are counted before cancellation; no term is discarded for being merely semantically zero. Empty lists reduce to the constant 0. Each term retains references to the shared q-circuits and the assignment variables.

The derivations can be guarded throughout by Delta_B, using fixed tautologies for modus ponens, congruence and conjunction. A definition is obtained from this conjunction by polynomially many projections. Thus no unproved equality of free p-gate variables is used. Circuits q_i are explicit circuits in x, rather than unconstrained new propositional variables. Alternatively they can later receive EF definitions, but their values are not asserted as axioms here.

**Polynomial proof size, including the contexts.** There are at most dW coordinate transitions. Let Q=2+L+d+n+V=O(L), and use max(1,H) for the empty-alphabet case. All original evaluation wires, their definitions and all q-circuits have O(Q⁴) size. Expanding either local coordinate produces O(H) terms. At most O(H²) adjacent swaps are needed; rewriting an enclosing binary XOR context uses O(H+1) congruence steps per swap. Cancellation, distribution and substitution also have polynomially many such local steps. This bounds all transition operations by O(dW(H+1)³), apart from polynomial-cost projections of Delta_B. Each CF proof line, even when charged as its entire circuit rather than a cross-line reference, has polynomial size: it contains shared q-circuits, at most polynomially many XOR/AND gates and the guard Delta_B. A conservative O(Q¹⁶) bound on total circuit-symbol occurrences absorbs these contexts, guards, projections, base cases and the terminal step. Its exponent is fixed independently of degree, width, assignment or B. Only a fixed polynomial bound matters here, rather than this loose exponent.

Binary encoding costs remain polynomial. Each original variable/gate identifier uses at most L bits from the supplied description. New circuit nodes and proof-line references can be densely named; their bit lengths are O(log(P+L+2)) for P total symbols/lines. Full proof length is therefore at most O((P+1)(L+log(P+L+2)+1)), still one polynomial in L. Dense relabeling and restoration of sparse original names have this same bound. Constant coefficients use one bit. Neither an unbounded identifier nor an entire circuit is treated as a unit-cost object.

**Terminal step and formula conclusion.** The last invariant gives

    o_B = XOR_{k : R_d_(k,t)=1} q_(d,k) = 0,

because the checked terminal table in (3) has no such k. This is derived under Delta_B by the same constant reductions, not by a PIT-correctness axiom. The resulting conclusion (2) is an ordinary formula in the original assignment variables and original evaluation-gate variables. It contains no auxiliary q-circuit and has polynomial length.

Apply Jeřábek, [*Dual weak pigeonhole principle, Boolean complexity, and derandomization*, 25 November 2003 author manuscript, §2, printed pp. 12–14, Lemma 2.5](https://users.math.cas.cz/~jerabek/papers/wphp.pdf): CF proofs with a **formula conclusion** have polynomial-time EF simulations. The formula-conclusion restriction is satisfied by (2); we do not apply this conversion to the bare circuit expression NOT B(x). This imported conversion and the preceding binary estimate give fixed K,e as asserted. From Delta_B as premises, modus ponens gives NOT o_B. If its definitions are introduced as fresh EF extensions, the same derivation can be used as part of a larger proof. No equivalence between unrelated evaluation encodings follows.

**Qualification and finite checks.** Formal zero was used only to obtain witnesses with zero terminal table. A Boolean-zero but formally nonzero ABP, for example xy+yx, need not have these witnesses; it is outside that semantic implication. Degree-zero components are also outside the stated d≥1 theorem and require only ground constant evaluation in a later assembly. Constant-edge elimination, component identification and the original formula-IPS reflection step have not been proved here. In particular, this lemma alone is not the polynomial arbitrary-degree formula-IPS-to-EF/ER theorem sought in the broader target.

Run `python3 scripts/shared-abp/check_witnesses.py`. Its small finite checks compare the generated matrices with independently enumerated noncommutative word coefficients and all Boolean assignments, including empty row spaces, cancellations and the formally nonzero xy+yx example. It also rejects a corrupted transition. These checks test the matrix indexing and recurrence (6); they are not a propositional proof verifier or a substitute for the informal proof above.

## Mathlib

Coverage: **not checked** for the full shared propositional zero-proof theorem, ABP coefficient witnesses or CF/EF simulation. The named Raz–Shpilka / Li–Tzameret–Wang results support the semantic basis construction; Pudlák and Jeřábek support the proof operations and conversion. Direct source links and theorem qualifications are retained above. None is claimed as a full statement match or a Mathlib entry. The assessed difference is the explicit free-variable shared-gate derivation and its encoding bound; potential originality is not established by the prior search.
