# L021 — Shared ER-to-original-axiom noncommutative circuit certificates

## Hypotheses

Let F be an explicitly encoded CNF of width at most three and pi a valid ER refutation under [the fresh acyclic AND-extension convention](../foundations/05-refutation-systems-and-simulation.md). Clauses are represented as sorted sets of signed literals; complementary literals are retained. Initial clauses can be supplied in a different explicit order, with repeated identical literals removed when matched to a proof clause. Resolution removes just its selected positive and negative pivot occurrences and takes the set union of the remaining literals. Weakening, earlier-clause reuse and auxiliary nonextension variables are allowed. Binary length charges all literals, identifiers, definitions and inference references. Put T=2+|F|+|pi|.

Work over F₂ in the free noncommutative polynomial ring. A positive literal x_i has falsity factor 1+x_i, a negative literal has factor x_i, and a clause polynomial is their ordered product, with empty product 1. The explicitly written original axiom list A(x) consists of these original clause polynomials, x_i²+x_i for the distinct original variables, and x_i x_j+x_j x_i for each original pair i<j. Let t index exactly this list.

Use L020's shared substitution sigma: each original variable remains an input x_i, each extension z iff (a AND b) has internal value P_z=L_a L_b, and a nonextension variable absent from F is sent to 0. For a positive proof literal v put L_v=P_v, and put L_(NOT v)=1+P_v. The falsity factor q(l) of a signed proof literal l is L_(NOT l). Both positive and negative values are retained as shared evaluation nodes. No syntactic-degree bound is assumed.

## Conclusion

There are fixed constants K,e, independent of F, pi, syntactic degree and literal unfolding, and a polynomial-time construction from (F,pi) of a division-free, fan-in-two, ordered-multiplication circuit C(x,t) satisfying the formal identities

C(x,0)=0,                         C(x,A(x))=1.                      (1)

Only the original x and t are free inputs. No extension or auxiliary variable, defining-clause placeholder, or additional Boolean/commutator placeholder remains. Every monomial of C contains exactly one placeholder when nonzero; in particular its placeholder degree is at most one, with coefficients on either side allowed.

A common construction network has at most K T⁴ gates, and the single rooted certificate together with the full explicit original axiom list has at most K T⁵ bits under the conservative identifier accounting below. Thus e=5 suffices for the described representation. The bound is in the original ER/CNF binary input length, rather than a degree or unfolded-size parameter.

This supplies the reverse **circuit** certificate implication: a polynomial ER bound on a family implies a polynomial bound for these original-axiom noncommutative circuit certificates. Consequently a superpolynomial lower bound against every such circuit certificate would exclude polynomial ER refutations. No such lower bound is supplied. The statement does not provide tree conversion, deterministic polynomial-time checking of arbitrary circuit identities, a circuit-IPS-to-ER simulation, or a passage from ER lower bounds to unrestricted SAT decision time. It is local progress under the screened SPECIALIZE comparison, potentially beyond the checked full-statement match, without certified originality or a main-problem candidate.

## Proof

**Formal operations supplied by the shared witnesses.** L020 gives an x-only value DAG of size O(T), an acyclic shared table K(g,h) for evaluation-node pairs, Boolean witnesses B_g, and witnesses for each actual normalized defining clause. All are circuits over exactly the original x,t. For value nodes with polynomials a,b their identities are

K(a,b)(x,0)=0,          K(a,b)(x,A)=ab+ba,
B_a(x,0)=0,            B_a(x,A)=a²+a.                               (2)

Here a,b abbreviate evaluation-node values, not new inputs. Their common network has O(T²) nodes. Original clauses use their own placeholders. In particular the negative-literal factors, constants and variables sent to zero have witnesses. L020's correction for noncommutative product Booleanity is retained; no commuting assumption replaces (2).

For any current ordered factor list, an adjacent interchange u,v in a product LuvR changes its polynomial by L(uv+vu)R. Adding the witness L K(u,v) R therefore changes a certificate for that product to one for LvuR. Every coefficient L,R is an x-only product of evaluation nodes. Removing an adjacent repeated factor q changes LqqR to LqR; adding L B_q R supplies exactly their difference. Both operations preserve zero when t=0. Sorting by adjacent swaps and then deleting repeated identical literals therefore produces a certificate for the actual sorted-set clause polynomial. Opposite literals are never deleted. This applies also to a tautological clause: its polynomial need not vanish formally, so its certificate is retained.

These operations only require witnesses for pairs of individual evaluation factors. No table for all newly formed clause-product gates is needed. Prefixes and suffixes can be written afresh as multiplication chains, referencing the existing evaluation roots without expanding them.

**A certificate for every source line.** In source order construct one root Q_D for each written proof clause D, maintaining

Q_D(x,0)=0,              Q_D(x,A(x))=sigma(f(D)).                    (3)

Here f(D) uses the explicit literal order on that proof line. Store roots and reuse them by gate reference, not by recursive copying. The invariant is a formal polynomial identity in x; it does not quantify over satisfying assignments.

For an initial clause use its original placeholder, whose substitution gives the original ordered product. If the source line has normalized order or removes repeated identical literals, apply the operations above. Width at most three makes this a bounded local adjustment. For an extension defining clause use L020's witness for its actual order and duplicate normalization. This witness already represents sigma(f(D)) using original axioms alone. The fresh extension values are internal x-only roots, including at defining-clause lines; no extension placeholder is introduced. This proves (3) for all initial lines.

For a weakening from D to E, let J be the ordered list of literals in E absent from D. Multiply Q_D on the right by the x-only product f_sigma(J). After original-axiom substitution its value is f_sigma(D)f_sigma(J), the falsity product of the concatenated list D,J. Normalize this list to E using (2). It is exactly E's set of literals because weakening requires D to be a subset of E. If weakening introduces a nonextension variable absent from F, its value is the specified constant 0; (2) still applies. Both identities in (3) are preserved.

**Resolution with its commutator term.** Consider a resolution inference whose left clause contains the selected positive pivot v and whose right clause contains its negative. Move these selected literals to the fronts of their respective lists by adjacent swaps, modifying the two certificates by the same formal corrections. Write the remaining lists as E,G, put

p=P_v,                    U=f_sigma(E),              V=f_sigma(G),

and denote the corrected certificates by R,S. Then

R(x,A)=(1+p)U,                    S(x,A)=pV.                        (4)

The remaining lists may themselves contain the opposite pivot literals. Their factors are retained in U,V; the selected occurrences alone have been removed. Thus (4) applies to tautological premises as well.

Construct a witness H(p,U) for pU+Up by a product induction on E's factors q_1,...,q_r. Starting with U_0=1 and H_0=0, use

U_j=U_(j-1) q_j,
H_j=H_(j-1) q_j+U_(j-1) K(p,q_j).                                 (5)

After original-axiom substitution the second expression is

(pU_(j-1)+U_(j-1)p)q_j+U_(j-1)(pq_j+q_jp)
  =pU_j+U_jp.

The two U_(j-1)pq_j terms cancel in characteristic two, without a factor permutation. When t=0 every H_j is zero. Set H=H_r and define

Q_raw = R V + U S + H V.                                           (6)

Substituting the original axioms and using (4)–(5) gives

Q_raw(x,A)=(1+p)UV+UpV+(pU+Up)V=UV.                                (7)

The two pUV terms and two UpV terms cancel separately. Omitting H V generally leaves the nonzero commutator term (pU+Up)V; the coefficients in (6) cannot be reversed freely. Each summand contains a certificate or witness that vanishes at t=0, so Q_raw(x,0)=0.

The raw product UV is the falsity product of the multiset concatenation E,G. Sort it and remove repeated identical literals with (2). The result is precisely the encoded resolvent. Shared nonpivot literals require the Boolean correction at duplicate deletion; this is not a syntactic deletion of a factor from a noncommutative polynomial. These operations prove (3) for resolution, even with retained complementary literals or multiple uses of either parent clause.

Induction now proves (3) at every line. The final empty clause has product 1, so its root is C and gives both identities (1). No soundness of an arbitrary circuit evaluation, external PIT answer, or semantically valid but formally unproved Boolean equality is used.

**Placeholder degree and elimination.** All initial roots are placeholders or L020 witnesses, and every nonzero monomial in each contains exactly one original placeholder. Every new operation adds roots or multiplies a root on either side by x-only coefficients. Formula (6) has the same form and never multiplies two placeholder-dependent roots. Thus the syntactic upper bound on placeholder degree remains one. The constant term in t is formally zero; cancellation cannot introduce a zero-placeholder monomial. All x-only values are constructed from original x and field constants. This also proves that neither auxiliary free variables nor augmented placeholders have appeared, at any stage of the construction. The identities already incorporate their elimination through L020, so a separate unchecked placeholder-composition step is unnecessary.

**Full binary cost.** There are O(T) source records, O(T) distinct written variable/extension identifiers and at most O(T) literal occurrences on any source line. L020's fixed common value/witness network has O(T²) nodes. Parent roots are referenced, not duplicated. Per source inference, a transient list contains at most 2T literals, including the concatenation before resolvent normalization. Moving pivots costs O(T) swaps; sorting a list costs O(T²) adjacent swaps and duplicate removal costs O(T) operations. Each correction can construct its x-only prefix/suffix chains in O(T) new nodes, together with a constant number of coefficient multiplications and additions. Even this deliberately unsophisticated implementation costs O(T³) new nodes per source line. Building U,V,H in (5) and the root (6) adds O(T) nodes; weakening has the same or smaller allowance. Hence all records together add O(T⁴) nodes.

An earlier root can be referenced by arbitrarily many later records: each explicit reference requires a new edge/record of bounded fan-in, already charged by this count. No occurrence-tree parameter enters it. Extract the final rooted sub-DAG once and densely renumber its gates; it has at most O(T⁴) nodes. Dense references require O(log(T+2)) bits because the exponent four is fixed, and coefficients over F₂ require one bit. Each original identifier requires at most T bits even if it is sparse. A self-delimiting record/list framing and each node's tag can be charged at the same O(T) bits per node, giving O(T⁵) certificate bits. Decimal identifiers in the fully framed JSON diagnostic below also fit this upper bound.

The original axiom list has O(T²) entries. Every entry has a bounded number of arithmetic operations because clause width is at most three and the other axioms are constant width. Charging O(T) bits for each restored identifier and reference gives O(T³) axiom-list bits, absorbed by O(T⁵). Both the axiom expressions and the output/root framing are charged; gate-record payload alone is not called the full output length.

All witness construction, proof verification, sorting, table indexing, rooted-DAG extraction and writing are polynomial-time operations on these explicitly bounded objects. Invalid source strings can be rejected after the polynomial-time ER check, before construction. The bounds do not assume that pi is short in |F|, or that its substituted values have polynomial degree. This proves the constructive threshold in T. It also yields the family implication in the conclusion by composing fixed polynomial bounds; the converse certificate implication and its proof-checking complexity have not been asserted.

**Finite checks and their limits.** Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/shared-extension/check_assembly.py`. The checker validates source ER inferences, then independently expands arithmetic gates into noncommutative words after zero/original-axiom substitution. A separate evaluation of extension definitions and source clause lists checks (3), rather than comparing two products built from the same gate roots. It also checks permitted placeholder labels and placeholder degree. The 280 formal cases check 1,080 source lines, including all 256 pairs of width-at-most-three selected-pivot premises on three variables, retained tautologies, shared nonpivot literals, reversed input orders, repeated input literals, weakening with auxiliary variables mapped to 0, the variable-free empty-clause case, signed/duplicate extension definitions and five complete used-extension refutations. The local-premise cases need not be refutations; their per-line checks test the resolution invariant. Complete refutation cases separately check (1).

Five deliberate errors are detected: omitted pivot commutator, reversed coefficient order, omitted sorting corrections, omitted duplicate corrections, and an invalid resolvent. Nine cases of L019's used-extension family, through m=128, verify all source inferences and serialize the entire rooted output plus original axioms. Only m<=8 cases expand words. At m=128 the 767-line proof has T=52,518 bits and exponential literal-unit unfolding size 814,611,591,808,161,107,664,147,907. The common assembly has 137,958 nodes, its final rooted certificate has 56,041 nodes, and its fully framed serialization with all original axioms has 7,024,432 bits. The [saved output](../scripts/shared-extension/assembly-results.json) identifies the finite versus structural scopes. Large cases do not provide an identity test at exponentially large degree; the formal induction above supplies the general proof.

This is an informal construction with discriminating computational checks. The checks do not verify arbitrary circuit identities, all possible ER strings, or a proof-assistant formalization. L019's stopped literal-tree construction, L018's tree-input forward direction and all earlier decision-transfer obstructions remain intact. The completed assembly removes a local original-axiom circuit-certificate gap while leaving the representation, lower-bound and decision gaps in the conclusion.

## Mathlib

Coverage: **not checked** for this full shared noncommutative ER translation, its two IPS identities or binary bound. L020's formal witnesses are the direct mathematical input; their use in the clause invariant, ordered resolution calculation and output count is proved above. Li–Tzameret–Wang, [*Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, 11 September 2015, Lemmas 3.5–3.7, printed pp. 16–18](https://arxiv.org/pdf/1412.8746v4), supply supporting certificate-propagation and formula-commutation mechanisms. Forbes–Shpilka–Tzameret–Wigderson, [*Proof Complexity Lower Bounds from Algebraic Circuit Complexity*, Theory of Computing 17(10), 2021, Theorems 1.2/1.4 and Remark 1.3, pp. 5–6](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf), supply commutative EF/circuit and noncommutative Frege/formula comparisons, with exponential degree allowed in the former. These inspected sources support components in their stated models; they do not provide a checked full match for this original-axiom shared noncommutative circuit conclusion. No Mathlib identifier, library-absence conclusion or certified originality claim is inferred.
