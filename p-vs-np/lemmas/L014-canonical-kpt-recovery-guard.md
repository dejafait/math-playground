# L014 — The proof obligation left by canonical KPT substitution

## Hypotheses

Use ordinary extended Frege (EF) and circuit Frege (CF), with full binary proof lengths. A polynomial bound means one polynomial for the whole family. Use the polynomial substitutions and simulations in the [reflection source note](../foundations/06-reflection-specialization.md).

Write V_N(f,y) for **the particular CNF evaluator fixed in L013**, with N formula bits and N densely indexed assignment bits. In particular, L013 proves a polynomial-time constructible CF identification

V_N(code(F), a(F,z)) ↔ F(z)                              (1)

for each well-formed length-N CNF F. The map a pads the assignment and respects F's original binary variable identifiers. No claim about arbitrary semantically equivalent evaluators is used.

Let B_N and W_N be circuits from N bits to N bits, whose full descriptions have size polynomial in N. B_N is the fixed first solver candidate. W_N is a proposed canonical selector. For the converse proof-length assertion below, assume **external** search correctness of W_N:

∀f,y, V_N(f,y) → V_N(f,W_N(f)).                         (2)

A hypothetical polynomial-time SAT decider supplies such a family by ordinary search-to-decision self-reduction. No EF or PV proof of (2) is assumed. Lexicographic minimality is unnecessary for this test.

For the two-round application, assume a supplied KPT strategy of the form in [Pich–Santhanam §3](https://arxiv.org/pdf/2312.08163v1), pp. 19–20, with polynomial proofs of its disjunction. The source's predicate has a solver term Q_B(x,y) and an antichecker term K_U(C,η), where U contains B and the entire output tuple of lists A,A′ and pairing data D. Here η packages all remaining universal assignment-certification challenges. The later output is U₂(x₁,y₁,C₁,η₁), with n and the fixed first output suppressed. All output-format conditions are retained; we consider the nontrivial case in which the first circuit encoding is valid. Invalid fixed output encodings can be evaluated separately. This supplied two-round hypothesis is not a consequence of general KPT, and the existential arithmetic premise remains unproved.

The source's assignment relation and V_N are not silently identified. The guard calculation applies to either relation separately. The proof-length assertion uses V_N and its proved identity (1); use with another encoding requires its corresponding polynomial proof of identification. Thus it already tests the repair on an explicitly justified evaluator.

For the antichecker specialization only, suppose a correct comparison circuit C_N fits the strategy's n^k gate bound. SAT∈P provides this for a sufficiently large fixed k, not necessarily for an arbitrarily prescribed k. This assumption is not needed for the guard's proof-length equivalence.

## Conclusion

Define

Q_B(f,y) := V_N(f,y) → V_N(f,B_N(f)),

G_(B,W),N(f,y) :=
  (V_N(f,y) ∧ ¬V_N(f,B_N(f))) → V_N(f,W_N(f)).           (3)

Then:

1. The exact Boolean condition Q_B(f,W_N(f)) → Q_B(f,y) is G_(B,W),N. Consequently (3) suffices to restore the original universally quantified first solver term after canonical substitution, whatever the second disjunct is. This inference is invalid without that condition. This is an assertion about this direct recovery inference, not about every use of a specific KPT strategy.
2. G_(B,W),N is the search-correctness statement for the fallback circuit that returns B_N(f) if its assignment verifies, and W_N(f) otherwise. It asks for correctness of W_N only where B_N fails, but its **polynomial CF proof-length bound is equivalent to polynomial boundedness of EF**, under the external hypothesis (2). The forward implication needs no correctness assumption on W_N or B_N: supplied proofs of (3) already suffice. Equivalently one can use polynomial EF proofs of the guard's standard definitional formula encoding, as justified below.
3. The first antichecker term, whose whole output is fixed at a length, can be falsified by fixing both C₁ and η₁ to concrete data with polynomial-size proofs of their evaluations. This does not establish a uniform bound for (3) or remove the later tuple's dependence on x₁. For an unsatisfiable fixed F, the canonically substituted first solver term becomes true, while its missing recovery guard reduces to ¬F through (1).

This is a reproduction of Boolean reasoning and the existing reflection specialization for the exact proposed repair. It supplies an informative obstruction to that repair's missing proof step, not an EF lower bound, a proof of unprovability, or a separation of P and NP.

## Proof

### Retaining the complete first-round challenge

For a fixed first output U₁, the antichecker term has the form

K_U₁(C,η) = D′_U₁(η) ∧ Err_U₁(C),

Err_U₁(C) = OR_(a in A) [V(a,d(a)) ≠ C(a)].             (4)

Here d(a) is the assignment selected by the pairing relation D when that relation is well formed. D′ retains the pairing conditions and the challenges to the assertion that each satisfiable member a has a satisfying selected assignment. The notation V in this paragraph can be the source's assignment-checking relation. A challenge η to that latter assertion selects a member a and an assignment w, and tests V(a,w) → V(a,d(a)). Other conjuncts and other components of η remain present. Lists, pairing data and the challenge have polynomial encoding length. This is an explicit packaging of the source's suppressed certification data, not a deletion of it.

Fix an externally correct C_N within the permitted comparison size. If the pairing conditions fail, a concrete falsifying check makes D′ false. Otherwise evaluate every selected label v_a=V(a,d(a)) and C_N(a). If they all agree, Err is false and any fixed η suffices. If they disagree somewhere, the disagreement must have C_N(a)=1 and v_a=0: v_a=1 already exhibits a satisfying assignment, which forces C_N(a)=1. Choose an actual satisfying assignment w for this a. It makes the corresponding implication in D′ false. This also covers an empty list, for which Err is false.

Thus in every case there is a concrete η_N making K_U₁(C_N,η_N) false. The choice may use external correctness; the resulting proof checks only polynomial-size circuits on constant inputs, including the assignment verification. Fixed local truth-table derivations in topological gate order certify this evaluation with polynomial length. They assert neither C_N's correctness on every input nor unsatisfiability of all negatively labelled members. Under SAT∈P, satisfying witnesses for these concrete queries can also be computed with one polynomial bound for fixed algorithms, but this is not a formal proof of their universal specification.

Apply the already imported circuit substitution theorem to the supplied two-round proof, setting C₁=C_N and η₁=η_N and discharging the first antichecker term by the preceding evaluation. The result has the form

Q_B(x₁,y₁) ∨ P_N(U₂(x₁,y₁,C_N,η_N); z₂),               (5)

where z₂=(x₂,y₂,C₂,η₂) remains universally free. The second term retains its whole solver-or-antichecker predicate, its output data and any format tests. Substituting y₁=W_N(x₁) gives a polynomial-size proof of

Q_B(x₁,W_N(x₁)) ∨
P_N(U₂(x₁,W_N(x₁),C_N,η_N); z₂).                       (6)

This removes y₁ from the later tuple's inputs; x₁ and z₂ still remain. No assertion about the second antichecker term being false for all x₁ has been made. The rest of the argument tests exactly the recovery of the first universal solver term in (6).

### The exact recovery condition

Put a=V_N(f,y), b=V_N(f,B_N(f)) and c=V_N(f,W_N(f)). Then

Q_B(f,W_N(f)) → Q_B(f,y)
  = ((¬c ∨ b) → (¬a ∨ b))
  ↔ (¬a ∨ b ∨ c)
  ↔ ((a ∧ ¬b) → c).                                   (7)

These are constant-size Boolean identities. After substituting the verifier circuits they have polynomial-size CF proofs; this does not require correctness of W_N. If H abbreviates the entire second term in (6), (7) and (3) give

[Q_B(f,W_N(f)) ∨ H] → [Q_B(f,y) ∨ H].                  (8)

Conversely, an inference (8) valid for arbitrary H must hold when H=0, and then is exactly (7). For example a=1,b=0,c=0,H=0 makes the premise of (8) true and its conclusion false. This valuation tests the propositional inference without a correctness premise; it is not a counterexample to an externally correct W_N. A particular strategy could conceivably supply useful additional relations involving H, and such a different proof is outside this necessary-condition claim.

Let T_N(f) be the fallback circuit, selecting B_N(f) when b=1 and W_N(f) otherwise. Substituting that multiplexer into the verifier and proving the two cases b=1 and b=0 gives

V_N(f,T_N(f)) ↔ (b ∨ c).                               (9)

One can prove (9) by congruence through the verifier gates in each case, with polynomial overhead. Hence V_N(f,y) → V_N(f,T_N(f)) is exactly the guard (3). The guard is semantically weaker than correctness of W_N alone: where B_N already gives a verified answer it places no constraint on W_N. This semantic weakening does not imply a weaker global proof-length requirement.

### Polynomial guard proofs imply EF polynomial boundedness

Suppose CF proofs π_N of (3) have length bounded by one polynomial in N. Let F be any unsatisfiable, well-formed length-N CNF. Substitute code(F) for f in π_N and a(F,z) for y. Circuit substitution costs polynomial time and length in the supplied proof and circuit descriptions.

The circuits B_N(code(F)) and W_N(code(F)) now have only constant inputs. Evaluate them to concrete assignments b_F and w_F. Since F is unsatisfiable, both checks V_N(code(F),b_F) and V_N(code(F),w_F) return 0. Their values have polynomial-size CF proofs by concrete gate evaluation. No universal correctness theorem for either circuit is used. The specialized guard therefore gives

¬V_N(code(F),a(F,z)).                                  (10)

Combine (10) with L013's identity (1) to obtain ¬F(z). Its conclusion is a formula, so the imported CF-to-EF and refutation simulations apply. We obtain an ER refutation of F and an EF proof of its negation with polynomial overhead. Standard Tseitin encoding and the same refutation/tautology simulations give polynomial EF proofs of arbitrary tautologies from polynomial ER refutations of all UNSAT CNFs. Empty clauses and the finitely many degenerate encoding lengths are immediate cases.

More explicitly, if

M=N+|V_N|+|B_N|+|W_N|+|π_N|+1,

all substitution descriptions, constant-evaluation derivations, the identification proof (1), and the final simulations have total time and output length at most p(M) for a fixed polynomial p. Gate sharing is retained; no circuit is expanded into its potentially exponential formula tree. Every circuit description other than π_N is polynomial in N by hypothesis. Thus a bound |π_N|≤q(N) yields one polynomial bound for all length-N UNSAT CNFs and hence polynomial boundedness of EF. The proof transformation takes π_N as input; it does not produce these guard proofs from N. This is the same supplied-proof distinction already present in L013.

### EF polynomial boundedness implies polynomial guard proofs

Under (2), (3) is a tautological circuit of size polynomial in N. To respect the source conversion's formula-conclusion restriction, give every gate of this circuit a fresh variable and form the polynomial-size formula

Θ_N := (AND of all gate-defining equivalences) → output.

This formula is a tautology: any values satisfying all definitions compute the guard, whose output is 1. Its binary length is polynomial in N. If EF is polynomially bounded, Θ_N has a polynomial-length EF proof. Convert that proof to CF and substitute each gate's defining subcircuit for its variable. Every defining equivalence becomes a local identity, leaving a CF proof of (3) with polynomial overhead. Conversely, from a CF proof of the guard, its local gate identities give a CF proof of Θ_N, which converts to EF because Θ_N is a formula. This establishes the stated equivalence of the two proof representations and the converse bound.

Only external truth of (2) is used to show Θ_N is tautological. A single PV1 proof, or uniform production of π_N from N, is a separate stronger assertion and is not inferred from a nonuniform polynomial EF bound.

### The unsatisfiable-input test and the route decision

For fixed unsatisfiable F, both b and c in (7) are concrete zeros. Consequently Q_B(F,W_N(F)) is the constant true statement (0→0), with an easy ground evaluation proof. Thus (6) by itself supplies no constraint on its second term. Recovering Q_B(F,y) requires the guard, which at this specialization is exactly ¬V_N(F,y), and hence ¬F by (1). Verifying the selector's answer on one concrete first-round counterexample cannot repair this case: the formula F has no satisfying assignment to fix, while y must remain free to prove its unsatisfiability.

The achieved bound is polynomial cost for substitution, ground antichecker falsification and the two directions of the guard/proof-system equivalence. The missing bound is polynomial length of proofs of the guard itself. That missing bound is already equivalent to the desired EF boundedness under the hypothetical correct selector. Therefore the direct canonical substitution plus universal-recovery argument has not weakened the required proof-system obligation. Stop this direct repair. This is not a lower bound on those proofs or a theorem ruling out another use of the original adaptive strategy.

**Literature relation.** The adaptive disjunction and the warning about assignment dependence are imported from Pich–Santhanam, [arXiv:2312.08163v1, §3, pp. 19–20](https://arxiv.org/pdf/2312.08163v1). KPT witnessing itself is imported in the [KPT source note](../foundations/10-kpt-witness-substitution.md). The proof operations are Pudlák, [arXiv:2007.14835v1, Lemma 2.1 and Fact 1](https://arxiv.org/pdf/2007.14835v1), and Jeřábek, [25 November 2003 manuscript, Lemmas 2.4–2.5](https://users.math.cas.cz/~jerabek/papers/wphp.pdf). L013 supplies the concrete evaluator identification. The work here is the exact guard calculation and its application of these existing operations, classified as reproduction rather than a new witnessing or reflection theorem. The [prior assessment](../drafts/literature/2026-09-27-canonical-kpt-witness-substitution.md) did not identify a full canonical-repair theorem; that search outcome is not a novelty claim.

## Mathlib

Coverage: **not checked** for the exact guard statement, KPT witnessing, or the supporting CF/EF simulations. The named source results above supply the standard components; none is represented as a full Mathlib match. No absence from Mathlib or mathematical novelty is asserted.
