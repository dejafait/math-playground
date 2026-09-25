# L011 — Decider traces and the missing fixed-system simulation

## Hypotheses

Use well-formed UNSAT, certificate size s_Q, and the distinction between size simulation and p-simulation from [the proof-system conventions](../foundations/05-refutation-systems-and-simulation.md). Let A be a fixed correct, total deterministic one-tape SAT decider on the ordinary binary input encoding. No efficient formal proof of A's correctness in ER or in an arithmetic theory is supplied. A may initially have arbitrary running time t_A(F).

Where a polynomial running-time hypothesis is explicitly imposed, assume t_A(F)≤C(|F|+1)^d on every input for fixed C,d. Let Q be any fixed sound, complete polynomial-time-checkable refutation system, with ER as the intended special case.

## Conclusion

1. There is a refutation system R_A checking explicit rejecting computation traces of A. For F in UNSAT, its shortest certificate has total size at most K_A(t_A(F)+1)(|F|+t_A(F)+1). In particular, a polynomial-time A yields a polynomially bounded R_A.
2. Under that polynomial-time hypothesis, the following are equivalent: Q size-simulates R_A; Q p-simulates R_A; and Q is polynomially bounded. The reverse construction uses polynomial-time NP witness search obtained from A, and assumes a polynomial Q-proof bound. It does not establish that bound.
3. Polynomial-time checkability of a fixed target system is insufficient for a general simulation theorem. An explicit full-truth-table system Q_tab has shortest proofs of size at least 2^{Ω(N/log N)} on an easy family of UNSAT formulas of binary length N. One correct total SAT decider B has polynomial rejecting traces on this family, so Q_tab does not even size-simulate R_B. Under the hypothesis of part 2, Q_tab also cannot simulate R_A. This is a counterexample to a system-independent transfer, not to the ER-specific transfer.
4. Under the polynomial-time hypothesis on A, its rejection soundness at input length n has a uniformly constructible polynomial-size CNF H_(A,n): its satisfying assignments describe a well-formed satisfiable formula of length n which A rejects. Correctness of A makes every H_(A,n) unsatisfiable. The construction encodes that soundness obligation without producing an ER refutation of it.

Consequently, replacing resolution by ER leaves a specific unproved requirement: an arbitrary hypothetical polynomial-time SAT decider must imply polynomial boundedness of ER, equivalently the simulation in part 2. No ER lower bound, simulation theorem, or P-versus-NP resolution is claimed.

## Proof

**The trace system.** Use a fixed finite-alphabet one-tape model, with halting states made stationary if padding is needed. Standard polynomial machine simulations preserve the polynomial-time case. A certificate π explicitly lists the configurations from the initial input F through a rejecting configuration. Require a common tape window large enough to include the input and every possible visited cell during the listed number t of transitions, for example cells −t−1 through |F|+t+1. Each cell has a constant-size symbol, with the head and finite control recorded by a marked symbol at exactly one cell. Include the row delimiters. There is no succinct or implicit trace encoding.

The verifier first checks that F is a well-formed CNF. It checks the exact initial configuration, row format, boundary blanks, one head per row, each local application of A's fixed transition table, and the final rejecting state. It can count the supplied rows before checking the window sizes; no claimed binary clock is used to run for more steps than the explicit certificate supplies. Comparing consecutive rows and checking each transition takes time polynomial in |F|+|π|, including for invalid certificates. A genuine t-step run has certificate size O_A((t+1)(|F|+t+1)); adding |F| is absorbed by this bound.

A valid trace is an actual rejecting computation of A on F. External correctness of A therefore gives F in UNSAT. Conversely, every F in UNSAT has such a trace because A is correct and total. Thus R_A is a sound and complete refutation system. Its verifier checks transitions, not the universally quantified assertion that A decides SAT. If A were incorrect, the same syntactic construction could cease to be sound.

If t_A(F)≤C(n+1)^d, enlarge d to at least 1. The displayed trace bound is at most a fixed polynomial q(n), for instance K(n+1)^(2d+2) after increasing K. This proves the first part with one bound for the whole language, not merely a particular easy subfamily.

**What the transfer entails.** Continue under the polynomial-time hypothesis on A. If Q size-simulates R_A with polynomial p, then for every unsatisfiable F of length n,

s_Q(F) ≤ p(s_(R_A)(F)) ≤ p(q(n)),

after replacing p by a nondecreasing polynomial upper bound. Thus Q is polynomially bounded. A p-simulation in particular gives a size simulation.

Conversely, suppose Q is polynomially bounded by a fixed integer-valued polynomial r(n), enlarged as necessary. Then every F in UNSAT has a certificate σ with |σ|≤r(n). Define the prefix-extension language

B_Q = { (F,1^ℓ,u) : some σ of length exactly ℓ extends u and V_Q(F,σ)=1 }.

This is in NP: reject |u|>ℓ, guess at most ℓ missing bits, and run the verifier. The unary bound ensures that the guess and verification time are polynomial in the query length. By the [Cook–Levin input](../foundations/02-standard-results.md), a polynomial-time reduction converts these queries to SAT instances. Running A on the reduced instances decides B_Q in polynomial time.

To translate (F,π), first check V_(R_A)(F,π). If it fails, output an arbitrary failure string and stop. Otherwise F is unsatisfiable. Test ℓ=0,…,r(n) with empty prefix until a positive B_Q query is found. Then, while the prefix is shorter than ℓ, query whether appending 0 permits an extension; append 0 if so and 1 otherwise. At each stage at least one extension exists. The completed σ is accepted by V_Q. There are at most 2r(n)+1 queries, each of length polynomial in n, and each query is decided in polynomial time. Including source-proof verification, the translator is polynomial-time in n+|π| on every input.

This proves all three equivalences. The constants in r and the translator depend on Q and A; no procedure finding a valid polynomial r from the bare code of V_Q has been shown. Under the polynomial-time hypothesis, selecting a different correct SAT decider does not remove the target-system boundedness requirement. The passage from short proof existence to proof search used A; outside this hypothesis, the two notions of simulation have not been identified.

**A target system where trace checking cannot give a simulation.** For a CNF F with m distinct variables and c clauses, list the variable identifiers in increasing order and set b=max(1,ceil(log₂(c+1))). Define a Q_tab certificate to consist of exactly 2^m rows of m+b bits. Each row contains one m-bit assignment and the index of an initial clause falsified by that assignment. Require the assignments to appear exactly once each, in lexicographic order.

This is polynomial-time checkable in its complete input and certificate lengths. First check divisibility of |π| by m+b and compare the row count with the binary integer 2^m, which has m+1 bits. Reject a count mismatch before attempting to enumerate assignments. Then scan the supplied rows, compare their assignment fields with an incrementing m-bit counter, check each clause index, and evaluate the indicated clause. The work is polynomial in |F|+|π|, even if π is far too short. Soundness follows because every assignment falsifies a clause. Completeness follows because every assignment to an unsatisfiable F falsifies at least one clause. This also covers m=0, when there is one row and an unsatisfiable formula must contain an empty clause.

For m≥2, let

E_m = (x₁) ∧ (¬x₁) ∧ (x₂) ∧ ⋯ ∧ (x_m).

With consecutive binary variable indices, its length is N_m=Θ(m log m). All m variables occur in the original formula, and Q_tab uses that formula without a preprocessing or abbreviated-proof rule. Every Q_tab proof of E_m has (m+b)2^m bits, hence at least 2^m=2^{Ω(N_m/log N_m)} bits. This exceeds every polynomial in N_m. In contrast, ER resolves the first two unit clauses immediately; no ER lower bound follows from this example.

Define a total SAT decider B to reject immediately if a well-formed input contains opposing unit clauses, and otherwise to decide it by exhaustive assignment enumeration; reject malformed inputs separately. The early rejection is sound and runs in polynomial time, and the fallback is correct and total. Thus t_B(E_m) is polynomial in N_m, and part 1 gives polynomial R_B certificates of E_m. Any polynomial size simulation by Q_tab would contradict its proved lower bound on this sequence. This is an unconditional failure of the proposed general transfer from checked computations to an arbitrary fixed polynomial-time-checkable system.

If a globally polynomial-time A exists, its traces are likewise short on E_m, so the Q_tab simulation fails under that hypothesis as well. This conditional observation asserts neither that P=NP nor a counterexample to ER simulation. It exposes the missing quantifier in the Cook–Reckhow characterization: NP=coNP promises **some** polynomially bounded system, while the target of a particular lower-bound argument is a prescribed system.

**Writing the soundness obligation does not prove it in ER.** Suppose again that A is polynomial-time with a fixed bound. For each n, the constructive [machine-to-circuit simulation](../foundations/02-standard-results.md) yields a polynomial-size circuit C_(A,n)(f) that outputs 1 exactly when A rejects the n-bit input f. The bounded run is unrolled, with stationary halting states; the circuit generator takes polynomial time in n for this fixed A and its fixed clock.

There is also a uniformly constructible polynomial-size circuit Eval_n(f,a) that checks whether f is a well-formed CNF and a satisfies it. Supply n assignment bits, densely indexing the distinct variable identifiers after parsing f and ignoring unused bits. Parsing, sorting identifiers, and evaluating the explicit clauses is polynomial-time; unrolling that fixed algorithm supplies Eval_n.

Introduce gate variables for both circuits, add constant-width clauses enforcing each Boolean gate's truth table, and add unit clauses setting both output gates to 1. Call this CNF H_(A,n). Gate values extend any input assignment uniquely, so

H_(A,n) is satisfiable iff some length-n well-formed F has a satisfying assignment and A(F)=NO.

Its full binary length, including gate identifiers, is polynomial in n, and the construction is uniform. Consequently all H_(A,n) are unsatisfiable if A is correct. More precisely, unsatisfiability for every n expresses only the absence of false rejections; full correctness also excludes false acceptances and is a stronger premise already assumed here.

These gate clauses encode both correct and incorrect algorithms. For a machine that always rejects, H_(A,n) is satisfiable at every length admitting a satisfiable encoded formula. Thus local computation constraints are not themselves a proof of rejection soundness. No bound on the ER refutation lengths of the H_(A,n), or theorem converting such a bound into the required simulation, is established here. External semantic correctness and efficient formal derivations of its propositional instances remain separate claims.

**Required versus achieved.** The required target remains a polynomial-time SAT algorithm or exclusion of every such algorithm. Part 1 conditionally supplies short certificates in R_A, not in ER. Part 2 identifies exactly the global proof-length property that an ER translation would deliver under the hypothetical algorithm. Part 3 supplies a superpolynomial lower bound only for Q_tab, with an unconditional trace-system counterexample, while part 4 supplies formulas for a prospective correctness proof rather than their refutations. To derive P≠NP from ER lower bounds by this route still requires both a superpolynomial ER lower bound and a justified implication from SAT∈P to polynomial boundedness of ER. Neither has been established. The quantified alternative that every sound complete refutation system is unbounded would imply NP≠coNP, a stronger sufficient objective; it is not inferred from failure of one system.

## Mathlib

Coverage: **not checked** for the full trace-system result, conditional simulation equivalence, truth-table discriminator, or soundness CNF construction. No Mathlib identifier or absence claim is asserted. The complete informal proofs are above. The Cook–Reckhow propositions pinned in the foundation note support the definitions and existential class characterization, not an ER-specific simulation theorem. The standard Cook–Levin and constructive circuit simulations supply only their explicitly indicated uses.
