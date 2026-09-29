# L013 — Specializing a supplied rejection-soundness refutation

## Hypotheses

Use the binary CNF encoding and ER convention in [the proof-system foundation](../foundations/05-refutation-systems-and-simulation.md). Fix a correct polynomial-time SAT decider A and its clock as in L011. Write N for formula length. Fix the implementation of L011's parse/sort/evaluate algorithm as described below, and use its circuit Eval_N in H_(A,N). The other circuit C_(A,N) is L011's clocked rejection circuit.

This implementation fixes choices that L011 left unspecified; it uses the same formula encoding, sorted dense assignment indexing, gate truth-table clauses, and two asserted outputs. The statement is about this fixed realization of L011's construction. It does not assert a translation from a different evaluator merely because that evaluator computes the same function.

Let F be a well-formed length-N CNF rejected by A, and let π be a supplied ER refutation of this H_(A,N). All lengths below are binary lengths, including variable names and proof references. Existence of short π is an additional hypothesis wherever used.

## Conclusion

For the fixed A, clock, and evaluator implementation, a uniform procedure produces an ER refutation ρ of F. For some fixed constants K,e, both its running time and |F|+|ρ| are at most

K (N + |H_(A,N)| + |π| + 1)^e.

The procedure has polynomial running time on invalid inputs too, returning failure when its syntactic checks fail. No exponent or constant depends on the particular F or π.

Consequently, if these H_(A,N) have ER refutations of length at most one polynomial in N, ER is polynomially bounded on all well-formed UNSAT formulas. This implication does not produce the soundness refutations, even nonuniformly, from A's running-time bound or external correctness.

This is a reproduction of the standard reflection specialization after checking the concrete evaluator and representation. It is not a result beyond the assessed literature or an unconditional P-versus-NP bound.

## Proof

**Imported proof operations.** Use the named results in [the reflection source note](../foundations/06-reflection-specialization.md): Pudlák, *Reflection principles, propositional proof systems, and theories*, [arXiv:2007.14835v1, §2.1–2.2, pp. 4–5, Lemma 2.1, and §3.1, pp. 8–9, Fact 1](https://arxiv.org/pdf/2007.14835v1). These give polynomial circuit substitution and the global-to-local reflection method, with its evaluator-identification premise. Section 2.1 records polynomial equivalence of ER, extended Frege (EF), and circuit Frege (CF). In refutation form, we use the standard conversions from an ER refutation of a CNF G to a CF proof of ¬G, and from a CF proof of ¬G to an ER refutation of G. Here G denotes the explicit conjunction of its clauses, so the final conclusion is a formula, not just an arbitrary circuit.

For the CF-to-EF part, retain the formula-conclusion hypothesis of Jeřábek, *Dual weak pigeonhole principle, Boolean complexity, and derandomization*, [25 November 2003 manuscript, §2, pp. 12–14, Lemmas 2.4–2.5](https://users.math.cas.cz/~jerabek/papers/wphp.pdf). We use these conversions, not a new general proof compiler. Cook's ER Simulation Theorem 6.8 supplies background for the formally proved soundness route; it is not applied here to infer a proof of A's correctness.

Within CF, each bounded-size propositional tautology has a fixed Frege derivation; substituting circuits in that derivation gives a proof of its instance. In particular, Boolean identities, gate evaluation under known constant inputs, and congruence of ∧, ∨, and ¬ have such derivations. Circuit representations retain sharing. This permits the following explicit gate-by-gate identification without expanding a circuit into an exponentially large formula.

**Fixing the evaluator specified in L011.** A frontend, whose inputs are only the N formula bits f, parses the explicit CNF, sorts its distinct variable identifiers in increasing numerical order, and replaces each occurrence's identifier by its rank in that list. It outputs a well-formedness bit v. There are at most N clauses, N occurrences per clause, and N distinct variables. Use padded arrays with N clause slots and N occurrence slots per clause; the unused slots are inactive. For each clause slot c output an activity bit b_c. For each occurrence slot (c,j) output an activity bit b_cj, a sign bit s_cj (1 means negative), and a rank r_cj in {1,…,N}. Inactive slots receive arbitrary fixed default signs and rank 1. On malformed inputs set v=0 and supply bounded default arrays.

Parsing, sorting, and filling these polynomial-length arrays take polynomial time in N, including the bits of the original identifiers. Unroll this fixed frontend into a fan-in-two Boolean circuit using the same constructive machine simulation as L011. No assignment bit is an input to that frontend. Lengths N=0 can be treated by the finite constant-size evaluator for that encoding; the following layout is for N≥1.

The evaluation phase consists of fixed bounded Boolean loops. Let a_1,…,a_N be L011's dense assignment bits. For every slot define

u_cj = OR_(i=1,…,N) ([r_cj=i] AND a_i),

t_cj = b_cj AND ((NOT s_cj AND u_cj) OR (s_cj AND NOT u_cj)),

q_c = NOT b_c OR OR_(j=1,…,N) t_cj,

Eval_N(f,a) = v AND AND_(c=1,…,N) q_c.

Equality of ranks is computed bitwise; all conjunctions and disjunctions use fixed binary folds, with empty OR equal to 0 and empty AND equal to 1. This is a concrete implementation of evaluating the parsed clauses after sorting and dense indexing. It can itself be specified as the straight-line, bounded-loop part of the algorithm that is unrolled. It introduces no additional semantic test on F and no branching on assignment values. Its gate count is polynomial (the deliberately padded selectors use O(N^3 log(N+1)) gates as a safe upper bound). Fix this circuit generator once for all N.

For a well-formed F with distinct identifiers x_(i_1),…,x_(i_m) in increasing order, replace a_j by x_(i_j) for j≤m and by 0 for j>m. This is exactly L011's dense assignment convention. Repeated occurrences use the same assignment bit; the original identifier may have up to N bits. Padding does not assume small numerical identifiers.

**A proof of evaluator identification, rather than semantic equivalence alone.** Substitute the constant code of F for f in the frontend. Evaluate every frontend gate in topological order. Its truth-table axiom, together with the already derived values of its at most two inputs, gives its constant value by a fixed local Frege derivation. Thus polynomially many such derivations establish the actual validity, activity, sign, and rank bits for F. Determining what these constants are uses the explicit parse/sort algorithm on the fixed string; it does not require a proof of that algorithm's correctness on all strings.

For an active occurrence (c,j), exactly one [r_cj=i] is 1, with i the rank of its actual identifier. Gate evaluation and the identities 0∧X=0, 1∧X=X, 0∨X=X reduce the selector u_cj to the corresponding original variable. The known sign bit reduces the signed expression to its literal. For an inactive occurrence t_cj=0 regardless of its selector and sign. Each reduction has a CF derivation by the fixed local identities and congruence just described.

Induct over the binary OR fold in each clause. Removing inactive zero terms leaves precisely that clause's literals, in their parsed order, including repeated or complementary literals. A used empty clause gives q_c=0; an unused clause slot gives q_c=1. Induct over the final AND fold, using v=1 and removing unused true terms. If F is viewed as the conjunction of its clauses with the same fold convention, this yields a uniformly constructible CF proof of

Eval_N(code(F), a(F,x)) ↔ F(x).                         (1)

There is no appeal to the existence of short proofs for arbitrary equivalent circuits. Every step of (1) is a local reduction in the specified evaluator. The separate rejection circuit has only constant inputs after substituting code(F). Topological constant evaluation, and the checked fact A(F)=NO, similarly give a CF proof of

C_(A,N)(code(F)) = 1.                                  (2)

Neither (1) nor (2) proves that all rejections by A are sound.

**Substituting the supplied refutation.** Convert π into a CF proof of ¬H_(A,N). The variables in H are its formula bits, assignment bits, and gate variables. Define one simultaneous circuit substitution σ as follows: formula bits become code(F); assignment bits become a(F,x) as above; a gate variable becomes the subcircuit computing that gate's value, after these input substitutions. The latter circuits use only original variables of F and constants; they contain no unresolved H gate variables. Shared subcircuits are represented as DAGs, not recursively expanded formulas. Apply the imported circuit-substitution theorem to the entire CF proof. Its conclusion is ¬σ(H_(A,N)).

Every gate clause of σ(H_(A,N)) has a short CF proof: its output has been replaced by the circuit operation on its replaced inputs, so it is an instance of that gate's fixed truth-table tautology. Constant gates are included. The assertion of the rejection output follows from (2). The asserted evaluation output follows from F by (1). Combining the clauses and the two output assertions therefore gives a CF proof of

F → σ(H_(A,N)).                                        (3)

Combine (3) with the already translated proof of ¬σ(H_(A,N)) by propositional inference to obtain ¬F. The polarity is essential: π refutes the conjunction of rejection and satisfaction, while F supplies the satisfaction assertion after specialization. We never infer F or its refutation from the gate definitions alone.

Now convert this CF proof of the formula ¬F through EF to an ER refutation of the original CNF F, using the imported simulations. Thus H's original gate clauses are discharged inside the CF argument; they are not silently added as original premises of the final refutation of F.

**Matching the ER convention.** The standard conversions use fresh definitional variables. Rename all such variables to avoid the original identifiers of F and previously allocated variables, and introduce definitions in topological order. Fan-in-two Boolean definitions can use exactly the notebook's AND-of-literals rule: NOT and copying are aliases or repeated operands; an OR is a negated AND of negated inputs, with a further copy definition if a positive output variable is required. Each change has constant local size. False is supplied, when needed, by z↔(x∧¬x) for an original variable x; its first two clauses resolve to ¬z. True is the opposite literal. The standard conversion's local definitional consequences are then obtainable from these fixed truth tables by constant-size resolution and weakening. This checks the basis convention without supplying a new general simulation theorem.

If F contains an empty clause, return that initial clause as the refutation. Otherwise a rejected well-formed F under the correctness hypothesis has an original variable: a variable-free CNF without an empty clause is the empty, true conjunction. Thus a variable for the constant definition is available whenever the conversion needs one. This also handles the degenerate encoding lengths. Unused assignment bits, tautological clauses, and repeated literals cause no variable-freshness or truth-table exception. Any proof-only free propositional variables in an intermediate Frege proof can first be replaced by 0 using the same substitution theorem.

**Binary length and uniform running time.** Put M=N+|H_(A,N)|+|π|+1 and let S be the number of gates and inputs in its two circuits. Their explicit gate encoding gives S=O(M). If a separate DAG is written for every circuit in σ, their total number of gates is O((S+N+1)^2); cross-output sharing is not needed for this bound. Including original variable names of at most N bits and dense gate references gives a total substitution description of at most cM^3 bits. All these circuits are generated in polynomial time. In particular, this bound does not use the size of a formula obtained by unfolding their fan-out.

The constant-evaluation proofs, the clause-fold inductions for (1), and the gate-clause and conjunction proofs for (3) use at most O(M^2) local identity instances. Each can be written with circuits and labels in O(M^2) bits, giving a safe cM^4 bound for this part of the CF argument. Actual operations are gate traversals, bounded array scans, and instances of fixed derivations; there is no truth-table enumeration over F's variables.

To make the imported overhead explicit, let p be a fixed nondecreasing polynomial bounding ER-to-CF conversion, q one bounding circuit substitution, and r one bounding the final CF-to-EF-to-ER conversion including the constant-factor basis normalization. Increase them to bound both time and output length in ordinary binary encodings. Then the produced ER proof has length at most

r(q(p(M)+cM^3) + cM^4 + N).

This is one fixed polynomial in M. Construction and validation of H for the fixed A and clock take some fixed polynomial g_A(N), and source-proof checking and renaming take polynomial time in M. Including these operations gives K M^e for fixed K,e, as claimed. The converter can check well-formedness, evaluate C_(A,N) on code(F), and verify the supplied ER proof before proceeding, so invalid inputs do not trigger an unbounded proof search. The constants are attached to the fixed algorithms and proof calculi, not selected anew for F.

If |π_N|≤b(N) for one polynomial b, L011 gives |H_(A,N)|≤h_A(N) for one polynomial h_A. Every unsatisfiable F is rejected by A, so the displayed output bound is at most K(N+h_A(N)+b(N)+1)^e. This proves the stated conditional polynomial boundedness. It uses existence of π_N; uniform production of π_N from N is a separate, stronger requirement and is not inferred.

**Required versus achieved.** The achieved threshold is polynomial overhead for a supplied soundness refutation, including the previously unchecked evaluator identification. No polynomial upper bound for those supplied refutations has been proved. Therefore the automatic computation-to-ER transfer from A's external correctness is still unjustified. The proof-complexity route also still lacks a superpolynomial ER lower bound on an appropriate family; the existing parity family has the polynomial upper bound already recorded in L012. Neither required main ingredient follows from this specialization.

## Mathlib

Coverage: **not checked** for the full specialization, its concrete evaluator identification, or the supporting proof-system simulations. No library absence or identifier is asserted. Pudlák's Lemma 2.1 and Fact 1 and Jeřábek's Lemmas 2.4–2.5, with direct links above, cover the standard substitution/reflection and representation machinery. Their statements do not directly specify this padded evaluator or its binary accounting; the argument above supplies that applicability check. No new general reflection theorem is claimed.
