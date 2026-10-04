# L019 — ER literal substitution: conditional certificate bound and exponential cost

## Hypotheses

Fix standard Frege and binary encodings. Let F be a well-formed CNF of width at most three and pi a valid ER refutation under [the fresh AND-extension convention](../foundations/05-refutation-systems-and-simulation.md). All written literals, original identifiers, extension definitions and inference references are charged. Put T=2+|F|+|pi|.

For each original variable x let B_x=x. In extension order, a definition z iff (a AND b), with a,b previously available literals, defines the **occurrence tree** B_z=(sigma(a) AND sigma(b)), where sigma(v)=B_v and sigma(NOT v)=NOT B_v. Copies are made separately at every occurrence. Substitute into each written proof clause, represent its disjunction by a fixed binary tree, and represent the empty clause by false. Define

U(pi) = sum over all written proof clauses C of the node count of sigma(C).   (1)

This is syntactic substitution with no Boolean simplification or retained circuit sharing. A negation, conjunction, disjunction, variable leaf or false constant is one node. The size of an original variable's identifier remains charged separately by T.

Over F₂, encode each original clause by the ordered product of its falsity factors: 1+x for a positive literal, x for a negative one. Include the original-variable Boolean axioms x²+x and all pair-once commutator axioms xy+yx. Write A(x) for that explicit list. Placeholder variables t index A; no extension variable or extension-axiom placeholder is allowed in the final certificate.

## Conclusion

There are fixed K,e such that the original F has a balanced, division-free, fan-in-two noncommutative **tree** formula-IPS certificate C(x,t) with full binary length, including the axiom list, at most

|F|+|A|+|C| <= K(T+U(pi)+2)^e.                            (2)

Its depth is O(log(s+2)), where s is its arithmetic tree node count, and its identities are formal identities in the free noncommutative polynomial ring:

C(x,0)=0,                       C(x,A(x))=1.             (3)

The construction takes time polynomial in T+U(pi). Thus polynomial U(pi) would suffice for this route, but ER binary length does **not** control that parameter polynomially.

In particular, for every integer m>=2 there is a valid ER refutation pi_m of the fixed 3CNF

F_* = (x) AND (y) AND (NOT x OR NOT y)                    (4)

with 6m-1 written clauses, T_m=Theta(m log(m+2)), and

U(pi_m)=Theta(Fib_(m+1)) >= 2^floor(m/2),                 (5)

where Fib_0=0 and Fib_1=1. Every introduced extension has a defining clause in the actual inference ancestry of the final contradiction. Even counting only that ancestry retains the exponential unfolding cost.

This stops the unrestricted **literal-substitution construction**. It does not refute the existence of other small tree certificates or an unrestricted reverse simulation. In fact F_* has the constant-size certificate given below. The known Frege-to-IPS and balancing stages are imported; the parameter accounting and used-extension example reproduce the standard distinction between circuit sharing and formula unfolding. No originality or P-versus-NP resolution is claimed.

## Proof

**Elimination produces a Frege proof at cost polynomial in T+U.** Put Phi_F equal to the explicitly parenthesized conjunction of the original clauses. For each source clause C, derive the tautology Phi_F implies sigma(C), in source order, using ordinary Frege alone.

For an initial clause, this is a conjunction projection; sigma fixes its original variables. The three defining clauses for z iff (a AND b) become

NOT(A AND B) OR A,
NOT(A AND B) OR B,
(A AND B) OR NOT A OR NOT B,

where A=sigma(a) and B=sigma(b). They are substitutions into three fixed tautologies, so have proofs proportional to a fixed polynomial in their written tree sizes. Adding the antecedent Phi_F is another fixed tautology instance. This does not use semantic correctness of an arbitrary circuit as an unproved proof premise.

A resolution step with premises D OR v and E OR NOT v becomes the fixed Boolean inference from D' OR B_v and E' OR NOT B_v to D' OR E'. Use the same inference under the antecedent Phi_F. Weakening is also a fixed tautology instance. If clauses are stored as sorted sets, explicitly rearrange their OR lists and remove duplicate literals by associativity, commutativity and idempotence, using fixed Frege proofs and connective congruence. Each source list has at most T literal occurrences; there are at most quadratically many adjacent moves and at most T surrounding OR contexts for any move. Each substituted literal tree already occurs in a written source clause, and no such move recursively expands an additional definition. Intermediate lists have at most a constant multiple of those occurrence trees.

Consequently the number of these local proof operations and their written formula sizes are bounded by one polynomial in S=T+U(pi)+2. For example, O(S^5) total Frege symbol occurrences is a conservative bound: at most T source lines, O(T²) list operations per line, at most T context lifts per operation, and O(S) symbols per fixed template instance. Initial conjunction projections and the fixed entailment combinations fit this bound. Original labels cost at most T bits each, and dense line references cost O(log(S+2)) bits, so full binary proof length is polynomial in S too. The last line gives Phi_F implies false, hence a Frege proof of NOT Phi_F with polynomial cost in S. No extension inputs remain.

**Import the certificate and balancing stages.** Use Li–Tzameret–Wang, [*Characterizing Propositional Proofs as Non-Commutative Formulas*, arXiv:1412.8746v4, 11 September 2015, Theorems 1.4 and 3.4, Lemmas 3.5–3.7, pp. 7 and 14–18](https://arxiv.org/pdf/1412.8746v4). Their construction turns a Frege proof into a polynomial-size noncommutative tree certificate over F₂. For applicability to the original **clause** system rather than a single translation of the tautology, use the explicit clause-form statement in Forbes–Shpilka–Tzameret–Wigderson, [*Proof Complexity Lower Bounds from Algebraic Circuit Complexity*, Theory of Computing 17(10), 2021, Theorem 1.4, pp. 5–6](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf). It includes the Boolean and base-variable commutator axioms and yields the formal identities (3). These are the inspected supporting theorems, not an ER-to-tree theorem. Import their construction rather than reprove it.

Let p be a fixed polynomial bounding that translation in the Frege proof's symbol count and original formula/list sizes. The original-variable axiom list has O(|F|+n²) entries with constant-size clause/Boolean/commutator arithmetic trees, since the original clause width is at most three and n<=T. Its full binary length is polynomial in T even with original identifiers restored. The unbalanced certificate therefore has node count bounded by p applied to a fixed polynomial in S.

Import tree balancing from Li–Tzameret–Wang, **Lemma 4.2**, pp. 19–20, of the same inspected v4 manuscript. It preserves the computed formal noncommutative polynomial, has polynomial node cost and logarithmic depth, and introduces no new free variables or divisions. Thus it preserves both identities (3). Over F₂ all coefficient descriptions have constant cost. Base-variable labels have at most T bits and axiom placeholder labels have O(log(T+2)) bits. Composing the fixed translation and balancing polynomials, and charging every tree occurrence and identifier, proves (2). If F already contains the empty clause, its clause polynomial is 1 and its placeholder alone is the certificate, covering the variable-free exception.

Computing and writing the literal substitutions is output sensitive. Every B_z appears in the substituted defining clauses, so materializing its occurrence tree costs at most the total U parameter, up to fixed bookkeeping factors. The subsequent Frege, certificate and balancing constructions have the polynomial costs just stated. This establishes the constructive bound in T+U without asserting a polynomial algorithm in T alone.

**A used-extension family with uncontrolled U.** For (4), put z_0=x and z_1=y. For 2<=i<=m introduce the distinct fresh variable

z_i iff (z_(i-1) AND z_(i-2)).                            (6)

The original positive units give z_0 and z_1. For each i, resolve the third defining clause z_i OR NOT z_(i-1) OR NOT z_(i-2) against those previous positive units, in two steps, to derive z_i. Next resolve the original NOT x OR NOT y against the projection NOT z_2 OR y to derive NOT z_2 OR NOT x, and against NOT z_2 OR x to derive NOT z_2. For 3<=i<=m, resolve NOT z_(i-1) against NOT z_i OR z_(i-1) to derive NOT z_i. Finally resolve the two units z_m and NOT z_m.

The complete count is three original clauses, 3(m-1) defining clauses, 2(m-1) positive-unit inferences, two initial negative inferences, m-2 negative propagations and the final empty clause. Their sum is 6m-1. All clauses have width at most three; each inference has a constant number of references and all variable/line indices are O(m). The explicit binary length is O(m log(m+2)). Conversely the written fresh identifiers, already in the definitions, contribute Omega(sum_(i=2)^m log(i+2))=Omega(m log(m+2)) under the fixed binary encoding. Hence the claimed T_m bound.

The positive unit z_m is a premise of the final resolution. Its derivation recursively uses the positive units at both preceding indices, so the third defining clause of **every** z_i is an ancestor of the final empty clause. The negative chain uses the first projection of every z_i, and both projections at i=2. The three original clauses are ancestors as well. There are unused individual projection clauses required by the extension blocks, but no extension definition is padding unrelated to the chosen refutation. Discarding unused individual lines still retains the final positive unit and all its expansion.

Write B_0=x, B_1=y and B_i=(B_(i-1) AND B_(i-2)). If s_i is its occurrence-tree node count, then

s_0=s_1=1,            s_i=1+s_(i-1)+s_(i-2).

Induction gives s_i=2 Fib_(i+1)-1. Monotonicity gives s_i>=1+2s_(i-2), so in particular s_m>=2^floor(m/2). The written positive unit z_m alone contributes s_m to U and to the ancestor-only count. Each level contributes only a fixed number of clauses, each with node count O(s_i+s_(i-1)+s_(i-2)+1). Also s_i+1>=2(s_(i-2)+1); summing the two parity subsequences yields sum_(i=0)^m s_i=O(s_m+1). Thus the full U and the ancestor-only count are both Theta(s_m), proving (5). For every fixed exponent d, 2^floor(m/2)/(m log(m+2))^d tends to infinity. There is no universal polynomial U<=P(T) for valid ER refutations, even under the ancestry restriction.

An implementation that actually writes the fully substituted proof requires at least U intermediate nodes and corresponding time. This is a lower bound on that materialized intermediate object. The upper bound (2) and an uncontrolled U do not by themselves lower-bound the final certificate produced after simplification, or any alternative translation.

**Why this is not certificate hardness.** The original F_* has a refutation by resolving (x) with (NOT x OR NOT y), then resolving the resulting NOT y with (y). Its first three clause polynomials are A_1=1+x, A_2=1+y, A_3=xy, in the displayed literal order. With placeholders t_1,t_2,t_3, the seven-node formula

C_*(x,y,t)= (t_3 + t_1 y) + t_2

has C_*(x,y,0)=0 and, formally over F₂,

C_*(x,y,A)=xy+(1+x)y+(1+y)=1.

It ignores the additionally included Boolean and commutator placeholders. Thus even this concrete family has constant-size certificates. The exponential cost is the literal substitution of the **supplied** proof, not a lower bound on the best proof or certificate, and balancing an arbitrary different certificate is not ruled out. The direct route needs a justified polynomial U premise or a different construction. General certificate lower bounds, a reverse bound for ER and the decision-to-proof transfer remain unresolved.

**Finite checks.** `PYTHONDONTWRITEBYTECODE=1 python3 scripts/er-unfolding/check_literal_substitution.py` verifies all ER inferences and extension freshness for ten values of m through 128, checks ancestry of every extension, and charges a documented self-delimiting binary encoding. Independent recursive expansion checks 198 clauses for m<=12 against the size recurrence; four original-variable assignments check the expanded local implications. A wrong resolvent and a nonfresh extension are rejected. For m=128, T=52,518 bits while the final positive unit has 814,611,591,808,161,107,664,147,907 tree nodes. The saved result is `scripts/er-unfolding/literal-substitution-results.json`. The asymptotic proof above, rather than these finite values, establishes the obstruction; no Frege/IPS proof strings were verified by this script.

## Mathlib

Coverage: **not checked** for ER extension elimination, the parameterized binary bound, the formula-IPS translation or balancing. Li–Tzameret–Wang's named theorems and lemma, and Forbes–Shpilka–Tzameret–Wigderson Theorem 1.4, match supporting Frege/certificate/balancing inputs under the stated field and representation hypotheses. They do not match a polynomial ER-to-tree theorem in the original binary parameter. No Mathlib identifier, library-absence conclusion or originality claim is inferred. The elementary recurrence, full inference family and size accounting are proved here.
