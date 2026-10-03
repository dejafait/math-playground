# L016 — Binary ER bound for logarithmic-degree formula-IPS certificates

## Hypotheses

Fix constants a,b>0 and fixed standard propositional proof calculi. Let F be a well-formed CNF of width at most three, with n distinct base variables and m clauses. Use the full binary encoding and fresh AND-extension convention in [the proof-system foundation](../foundations/05-refutation-systems-and-simulation.md). Variable occurrences may first be densely relabeled x₁,…,xₙ; the final refutation is of the original F with its original identifiers.

For a positive literal xᵢ its falsity factor is 1+xᵢ over F₂; for a negative literal ¬xᵢ it is xᵢ. Encode a clause as the ordered product of its falsity factors, with the empty product equal to 1. Include the Boolean axioms xᵢxᵢ+xᵢ and all base-variable commutator axioms xᵢxⱼ+xⱼxᵢ, i<j. Write A(x) for this explicitly supplied list. Using all ordered pairs instead only repeats these axioms or adds zero polynomials and changes the list size by a polynomial factor. Placeholder names y₁,…,y_q identify its entries, where q=m+n+binom(n,2) for the pair-once convention.

Let C(x,y) be a supplied division-free, fan-in-two noncommutative **tree formula** over F₂, with ordered multiplication and s total nodes, including leaves. It is a formula-IPS certificate: in the free noncommutative polynomial ring,

C(x,0)=0,                    C(x,A(x))=1.                 (1)

These are formal identities, not just equalities on Boolean assignments. All base and placeholder variables have syntactic degree 1, constants degree 0, addition takes the maximum and multiplication the sum. If d is the supplied tree depth and r its syntactic degree, assume

d ≤ a log₂(s+2),             r ≤ b log₂(n+2).             (2)

Put T=2+|F|+|A|+|C|, charging the entire explicit binary CNF, axiom list, tree syntax, coefficients and all variable/placeholder labels. The bounds a,b are fixed across a family, rather than chosen anew for each certificate. No arithmetic circuit sharing, other field, division or semantic-degree-only hypothesis is used.

## Conclusion

There are fixed constants K,e, depending only on a,b and the fixed calculi/encodings, for which F has an ER refutation ρ satisfying

|F|+|ρ| ≤ K(T+2)^e.                                      (3)

Thus a family with polynomial total binary certificate length in |F|, and the fixed depth/degree bounds (2), has polynomial-size ER refutations of its original CNFs. The axiom list itself has polynomial length in |F|. This does not assert that arbitrary UNSAT formulas have such certificates or that they can be found efficiently.

This is an encoding/applicability reproduction of Li–Tzameret–Wang's known logarithmic-degree Frege simulation and the standard EF/ER conversions. It is not a polynomial simulation for arbitrary-degree certificates, a lower bound, or a resolution of P versus NP.

## Proof

**Imported result and exact scope.** Use Li, Tzameret and Wang, [*Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, 11 September 2015, Definition 1.6, Theorem 1.7 and the following degree/depth note, pp. 8–9; detailed 3CNF formulation Theorem 4.1](https://arxiv.org/pdf/1412.8746v4). Over F₂ their noncommutative formula-IPS simulation produces Frege proofs of the negated CNF. The general stated bound is quasipolynomial; the degree/depth note bounds the relevant construction polynomially in s·binom(d+r+1,r) and states its polynomial logarithmic-degree case. Import the identity-witness and Frege construction, rather than reprove it. The [prior source note](../drafts/2026-10-03-noncommutative-ips-source-notes.md) retains the inspected version, theorem statements and scope.

The two zero identities used in that construction can be represented by C(x,0) and C(x,A(x))+1. We bound both their syntax and the supplied certificate conservatively; thus whether a construction stage uses the original or substituted degree/depth does not weaken the estimates below. Theorem 4.11's homogeneous-zero-identity result is not treated as a standalone theorem about substituted homogeneous certificates. No homogeneity preservation is assumed.

**Axiom substitution.** Each clause polynomial has at most 11 tree nodes, depth at most three and syntactic degree at most three: at most three falsity factors of at most three nodes each, with at most two multiplication nodes. A Boolean axiom has five nodes, depth two and degree two; a commutator has seven nodes, depth two and degree two. All coefficients are 0 or 1, with constant binary cost.

Replace each placeholder leaf by its axiom tree separately, preserving operand order and repeated occurrences. If C has l placeholder leaves, the node count increases by at most 10l, so C(x,A(x)) has at most 11s nodes. Along a root-to-leaf path this adds depth at most three. Structural induction on C gives syntactic degree at most 3r: the assertion holds at leaves, maximum at addition preserves it, and sum at multiplication preserves it. Replacing y by 0 instead increases neither node count, depth nor degree. Consequently the two zero identities have node count at most 11s+2, depth at most d+4 and degree at most 3r. No step expands a polynomial into its monomials.

There are O(m+n²+n) axiom entries. Their explicit descriptions with dense labels and placeholder indices have total length O((m+n²+n+1) log₂(n+m+2)). Generating or copying the whole list, including unused entries, is polynomial in T. In particular s,n,m,q≤T. Original sparse binary identifiers cost at most |F|≤T each, so dense normalization and eventual restoration remain polynomial in the full input length, independently of their numerical magnitudes.

For completeness, Booleanizing an arithmetic addition as XOR can duplicate both child formulas. A direct tree translation of a depth-h arithmetic formula with u nodes has at most c u·2^h Boolean symbols: any source occurrence is copied at most twice for each ancestor. Multiplication is AND and does not require this duplication. For the substituted formulas h≤d+4 and u≤11s+2, hence this elementary expansion is also polynomial in T, bounded by c'(s+2)^(a+1). The imported Frege construction already accounts for its own proof formulas; this estimate separately prevents a hidden exponential cost in the input translations. No claim about unfolding arbitrary shared circuits is involved.

**The source factor is polynomial in full input length.** Set

D=ceil(a log₂(s+2))+4,       R=ceil(3b log₂(n+2))+1.

These bound all depths and syntactic degrees above, with a spare degree level for the constants. The binomial factor is increasing in each of the nonnegative depth and degree parameters. By the binomial theorem,

binom(D+R+1,R) ≤ 2^(D+R+1)
              ≤ 256(s+2)^a(n+2)^(3b)
              ≤ 256(T+2)^(a+3b).                         (4)

The constant 256 absorbs the two ceiling errors and the six added levels: D+R+1≤a log₂(s+2)+3b log₂(n+2)+8. This bound does not assume n≤s or use the largest identifier in place of n.

After loading the CNF/list and making the substitution copies, their total arithmetic node count U is at most cT. The source's polynomial construction cost, its CNF bookkeeping and the preceding Boolean input expansions can therefore all be bounded by one fixed polynomial p evaluated at

X=c₀(T+2)^(a+3b+1).

Increase c₀ and p if necessary to absorb fixed local syntactic conversions. The imported result supplies a Frege proof σ of ¬Φ, where Φ is the explicit conjunction of the clauses of the densely relabeled F, with at most P=p(X) symbol occurrences and proof steps. Because a,b and p are fixed, P is bounded by one polynomial in T. The general s^{O(log s)} bound alone would not justify this conclusion; it is the degree/depth estimate (4) that meets the required threshold.

**Why the conclusion concerns the original clauses.** The source simulation derives ¬Φ, rather than a negation of an enlarged CNF requiring Boolean/commutator clauses as extra original premises. In its Boolean interpretation xᵢxᵢ+xᵢ is identically zero and xᵢxⱼ+xⱼxᵢ is identically zero. Under an original clause, its product of falsity factors is zero. Those facts are established in the source's Frege argument, with assignment variables still free. Together with the formal identities (1) they give the contradictory values 0 and 1. Deterministic identity verification or semantic correctness alone is not substituted for that imported Frege proof. There is no additional PIT-axiom or SAT-decider soundness-proof premise in this theorem.

**Binary proof length and ER conversion.** A proof with P total symbol occurrences/steps uses at most O(P+n+q) distinct labels and P inference references. Encode its auxiliary labels and line numbers densely. After original-variable names are restored, each original identifier costs at most T bits and each auxiliary label/reference costs O(log₂(P+T+2)) bits. Thus its complete binary encoding has length at most

c₁(P+1)(T+log₂(P+T+2)+1) ≤ c₂(P+T+2)^2.                (5)

All written substitutions are charged as occurrences in P; a reference to a previous proof line is charged as a binary reference. No unit-cost assumption for unbounded labels or coefficients is being made.

Regard σ as an EF proof, or as a CF proof with the formula conclusion ¬Φ. Import the standard polynomial conversions from [the reflection source note](../foundations/06-reflection-specialization.md): Pudlák, [*Reflection principles, propositional proof systems, and theories*, arXiv:2007.14835v1, §2.1, pp. 4–5](https://arxiv.org/pdf/2007.14835v1), records the polynomial equivalence of CF, EF and ER; Jeřábek, [*Dual weak pigeonhole principle, Boolean complexity, and derandomization*, 25 November 2003 manuscript, §2, pp. 12–14, Lemmas 2.4–2.5](https://users.math.cas.cz/~jerabek/papers/wphp.pdf), supplies the circuit/formula simulations with the formula-conclusion restriction retained. Any proof-only free variables can first be substituted by 0 using the standard substitution operation; the conclusion uses only F's variables, and this adds polynomial overhead. In refutation form, an EF proof of ¬Φ translates to an ER refutation with the clauses of F as its original premises. We use these known conversions, not a new proof compiler or a simulation inferred from checkability.

Match their definitional basis to the notebook's ER rule by naming gates freshly in topological order. NOT uses the opposite literal; OR uses the opposite literal of an AND gate on negated inputs; a copy, if needed, uses a repeated operand. Any other fixed connective uses a fixed number of these gates. The resulting local definitional consequences have constant-size resolution/weakening derivations. Only fresh definitional clauses are added. Fresh indices can be chosen among the first n+v integers avoiding the n original indices, where v is the number of extension variables to be introduced; this keeps their binary length logarithmic in n+v+2 even if original identifiers are sparse.

If F has an empty clause, that clause is already a refutation. Otherwise a CNF admitting (1) must be unsatisfiable by the standard IPS soundness argument: a satisfying Boolean assignment makes every A-entry zero, forcing C(x,A)=C(x,0)=0 against (1). Such an F has at least one original variable. A false constant, if the conversion needs it, can then be defined by z↔(x∧¬x); its first two extension clauses resolve to ¬z. True is the opposite literal. This covers the constant convention and the variable-free exception without introducing an unrestricted extension axiom.

Let h be a fixed nondecreasing polynomial bounding the imported proof conversions and this constant-factor basis normalization in full binary length. Equations (4)–(5) give

|F|+|ρ| ≤ h(c₂(p(c₀(T+2)^(a+3b+1))+T+2)^2)
         ≤ K(T+2)^e

for fixed K and an integer e. This proves (3). Uniformly polynomial certificate lengths in |F| imply a uniformly polynomial T, since n,m≤|F| and the explicit axiom list costs O((|F|+2)² log₂(|F|+2)) bits. No new exponent is selected for each family member.

**Effect on the required gap.** This establishes the screened polynomial upper-bound translation in total binary length. Any prospective ER-hard CNF family having such polynomial certificates is therefore excluded. It provides neither those certificates for general UNSAT nor a polynomial simulation of unrestricted-degree formula-IPS. Even a formula-IPS lower bound would not by itself exclude all EF/ER proofs, and an ER lower bound would still need a justified passage to uniform decision hardness. The prior parity and KPT obstructions are unaffected.

## Mathlib

Coverage: **not checked** for the full binary specialization, noncommutative formula-IPS or the Frege/EF/ER simulations. Li–Tzameret–Wang's named degree/depth result matches the algebraic/Frege input under the stated F₂/3CNF/tree hypotheses; Pudlák and Jeřábek support the proof-system conversions. None is presented as a Mathlib theorem or as a literal match for all local encoding conventions. Direct theorem links are retained above. The only local addition is the explicit applicability and binary-length accounting; no originality is claimed.
