# L015 — Two-round transfer from supplied complete-output covers

## Hypotheses

Use ordinary extended Frege (EF) and circuit Frege (CF), full binary description/proof lengths, and the imported polynomial proof operations in [the reflection source note](../foundations/06-reflection-specialization.md). A polynomial bound below is one polynomial for the family, not a new bound for each formula.

The strategy and coverage proofs may be supplied as EF proofs of the standard definitional formula encodings of their circuit conclusions. Convert them to CF and substitute each gate's defining subcircuit; local gate identities discharge the definitions with polynomial overhead. Thus the CF formulation below does not demand an additional proof family beyond the screened EF premises.

Use the particular assignment evaluator V_N(f,a) fixed in L013, with N formula bits and N dense assignment bits. For every well-formed length-N CNF F, that lemma supplies a polynomial-time constructible CF proof of

V_N(code(F),a(F,z)) ↔ F(z).                              (1)

The map a pads the assignment and respects F's original variable identifiers. If a strategy uses a different encoding, its identification and proof-system translation must instead be supplied with polynomial bounds; semantic agreement alone is insufficient. For this statement the strategy is realized with V_N.

Assume SAT∈P externally. Fix a correct comparison family C_N deciding whether there exists a with V_N(f,a)=1, including the malformed-input convention. Fix a comparison exponent k for which C_N fits the strategy's N^k gate bound at all sufficiently large N. A supplied strategy at one arbitrary k does not ensure this compatibility. Finitely many smaller lengths can be handled separately.

Assume a supplied two-round solver-or-antichecker strategy, its polynomial-size output circuits, and CF proofs π_N of its universal disjunction

P_N(u^(1)_N; x_1,y_1,C_1,η_1) ∨
P_N(U_2,N(x_1,y_1,C_1,η_1); x_2,y_2,C_2,η_2).           (2)

All challenge variables displayed in (2) are free propositional inputs. The first output u^(1)_N is fixed at the length. The second complete output retains its dependence on the first challenges and has no second-challenge inputs. Two rounds, the strategy proofs, and their polynomial bound are additional premises, not conclusions of SAT∈P or general KPT witnessing.

The predicate is the full solver-or-antichecker interface in [the antichecker source note](../foundations/09-antichecker-existence-and-generation.md) and L014. Its solver branch entails

Q_B(x,y) := V_N(x,y) → V_N(x,B(x))

when the encoded solver is valid; an invalid solver encoding fails that branch's format check. Its antichecker branch retains the lists A,A′, pairing D, all format conditions, and every certification challenge η. For a well-formed pairing selecting d(b) for each b∈A, the error conjunct is

Err_u(C) := OR_(b∈A) [V_N(b,d(b)) ≠ C(b)],

and certification includes V_N(b,w) → V_N(b,d(b)) for every challenged member b and assignment w. The source's additional format/conjunction tests are retained. Invalid encodings are totalized for circuit evaluation, not granted valid solver or antichecker status. Use the explicit gate implementation of this interface; its circuit size is polynomial in the full encoded inputs. L014's constant-tuple antichecker falsification applies to it.

Choose a concrete η^(1)_N falsifying the first antichecker against C_N, as provided by that ground-falsification argument. For every well-formed CNF F of length N, supply a list u_1,…,u_m of **complete** encoded second outputs, independent of y_1 and all second challenges, and a CF proof γ_(N,F) of

[V_N(code(F),y_1) ∧ ¬V_N(code(F),B^(1)_N(code(F)))]
  → OR_(i≤m) [U_2,N(code(F),y_1,C_N,η^(1)_N)=u_i].       (3)

The first solver B^(1)_N is totalized in the same fixed convention if necessary. All tuple bits, lengths, padding, flags, circuit descriptions, lists and pairing data count. Tuples use the full output encoding; an entry with incompatible encoded length has an equality test that is identically false. Extra or malformed entries are permitted. Require

|γ_(N,F)| + Σ_(i≤m)(1+|u_i|) ≤ p(N)                     (4)

for one polynomial p uniform over F and the chosen fixed prefixes. Empty OR is false. The list and proof may be supplied nonuniformly. Their existence with (4), and efficient generation of them, are different assertions; neither is established here.

## Conclusion

These hypotheses imply polynomial CF proofs of ¬F for every unsatisfiable CNF F, and consequently polynomial boundedness of ordinary EF (and ER under the imported refutation simulations).

For fixed calculi and strategy implementation there is a polynomial r such that the resulting proof length is at most r(M), where

M = N + |π_N| + |γ_(N,F)| + |V_N| + |C_N|
    + |u^(1)_N| + |U_2,N| + Σ_(i≤m)(1+|u_i|) + 1.       (5)

In (5), |U_2,N| is the full output-circuit description length. No EF proof of the hypothetical SAT algorithm's universal correctness or of a canonical selector's correctness is used. The result settles only the supplied-cover sufficiency test; it supplies no unconditional EF bound or P-versus-NP resolution.

## Proof

**Imported operations and the application being tested.** Use Pudlák, [arXiv:2007.14835v1, Lemma 2.1, pp. 4–5](https://arxiv.org/pdf/2007.14835v1), for polynomial circuit substitution, and Jeřábek, [25 November 2003 manuscript, Lemmas 2.4–2.5, pp. 12–14](https://users.math.cas.cz/~jerabek/papers/wphp.pdf), for EF/CF conversion with a formula conclusion. Standard refutation simulations are recorded in the reflection source note. These are imports, not new proof compilers. The solver-or-antichecker interface and adaptive strategy come from the supplied instance of [Pich–Santhanam, arXiv:2312.08163v1, §3, Theorem 7 and following discussion, pp. 19–20](https://arxiv.org/pdf/2312.08163v1). That theorem does not itself supply (3)–(4). The [prior assessment](../drafts/literature/2026-09-27-kpt-output-cover-transfer.md) screens exactly this remaining finite-case inference.

### Ground antichecker challenges

L014's ground-falsification argument supplies, for any fixed complete tuple u, a concrete η_u for which its antichecker branch against C_N has a polynomial CF proof of falsity. To recall the scope of this input: malformed lists/pairing/format are checked on constant data; otherwise evaluate all selected labels and C_N(b). If all agree, Err_u(C_N)=0. If they disagree, external correctness excludes a selected satisfying assignment labelled negatively by C_N. Thus some b has C_N(b)=1 and V_N(b,d(b))=0. An actual satisfying assignment w makes its certification implication false. Only this concrete w is inserted in the proof. Empty A has a false error disjunction. All other certification fields stay in the predicate.

Choosing w uses external SAT correctness. Its inserted verification, all comparison values, and all format checks are concrete gate evaluations, each proved by local truth-table identities in topological order. There is no proof asserting correctness of C_N on arbitrary inputs. Apply this already established input to u^(1)_N and separately to every u_i. Even an extra tuple not attained by the strategy receives its own challenge, or has a false format/length check. Different tuples may require different η_i.

### Leave the first satisfying-assignment variable free

Fix an arbitrary unsatisfiable, well-formed CNF F of length N. Put

t(z) := V_N(code(F),a(F,z)),

U(z) := U_2,N(code(F),a(F,z),C_N,η^(1)_N),

E_i(z) := [U(z)=u_i].                                  (6)

The first solver's fixed answer on F evaluates to an assignment b_1 with V_N(code(F),b_1)=0. This equality has a polynomial proof by concrete gate evaluation. Unsatisfiability is used only externally to know the outcome of that particular evaluation; no refutation of F is inserted into the argument. An invalid first solver instead has a false solver-format check, with the totalized answer handled in the same way for (3).

Substitute x_1=code(F), y_1=a(F,z), C_1=C_N, η_1=η^(1)_N in π_N. Discharge its first antichecker by the ground proof. The first solver branch entails ¬t(z), by the preceding evaluation, or is format-false. Propositional weakening therefore gives a CF proof, with every second challenge still free, of

¬t(z) ∨ P_N(U(z);x_2,y_2,C_2,η_2).                     (7)

Make the same assignment substitution in the supplied coverage proof (3). Since the first solver check evaluates to 0, obtain

t(z) → OR_(i≤m) E_i(z).                                (8)

The free assignment z is never replaced by a canonical satisfying-assignment circuit. In particular, (8) is a supplied proof even when its antecedent is semantically false for this unsatisfiable F. That semantic fact is not used to manufacture (8).

### One second-round challenge per complete listed output

For each i with a length-compatible tuple, let η_i be its concrete ground antichecker challenge. Substitute in a separate copy of (7)

x_2=code(F), y_2=a(F,z), C_2=C_N, η_2=η_i.               (9)

All these substitutions are permitted circuit substitutions into a supplied universally valid proof. Using z in both assignment blocks is permitted. The complete output U(z) is unchanged, because it had no second-challenge inputs.

Evaluate the fixed solver B_i(code(F)). If it is a valid solver, its answer b_i again satisfies V_N(code(F),b_i)=0, with a concrete evaluation proof. If it is invalid, its solver-format check is false. Together with the ground antichecker falsification, this yields a CF proof of

P_N(u_i;code(F),a(F,z),C_N,η_i) → ¬t(z).                (10)

No correctness of B_i on other formulas is assumed. It is enough to evaluate its one answer on F. Nor is a negative assignment label on some other listed formula used as a certificate of that formula's unsatisfiability.

Complete equality E_i gives, by bit equality and gate-by-gate congruence in the explicit predicate circuit,

E_i(z) → [P_N(U(z);code(F),a(F,z),C_N,η_i)
           ↔ P_N(u_i;code(F),a(F,z),C_N,η_i)].           (11)

For clarity about the proof bound, under E_i every tuple-input bit agrees. A fixed local congruence derivation propagates agreement through each fan-in-two gate, retaining the whole circuit as a DAG. Thus (11) has polynomial CF length; it is not an appeal to short proofs of arbitrary equivalent circuits. Equality includes certification, format and pairing data, which is why equality of solver descriptions alone would not suffice.

Combining this copy of (7), (10) and (11) by a fixed Boolean inference gives

E_i(z) → ¬t(z).                                        (12)

An entry incompatible with the output's encoded length has a ground proof of ¬E_i and therefore also (12), without any predicate substitution at that length. This treats every entry, including duplicates and unattained or malformed tuples, without assuming that the list consists only of valid outputs. No mutual exclusivity of the E_i is needed.

### Combine the cases and obtain a formula conclusion

Repeated binary disjunction elimination on (12) gives

[OR_(i≤m) E_i(z)] → ¬t(z).                              (13)

Combining (8) and (13) yields ¬t(z). For m=0, (8) directly has that conclusion. In ordinary Boolean terms, assuming t makes some E_i true by (8), while that same E_i makes t false by (12). This finite proof reasoning does not assert that any satisfying assignment to F exists.

Use the supplied evaluator identification (1) to obtain the formula ¬F(z). Its conclusion is a formula, so the imported CF-to-EF and refutation simulations apply with their actual representation restriction.

To get EF proofs of arbitrary tautological formulas T, form the standard polynomial-length CNF of gate definitions computing T together with the assertion that its output is false. It is unsatisfiable. The preceding result gives a CF proof of its negation. Substitute each gate's defining subcircuit for its gate variable and discharge the local gate identities. The remaining conclusion is T. It is a formula, and the same CF-to-EF conversion applies. This standard definitional translation and its substitutions have polynomial binary overhead; no exponential circuit unfolding is used. Degenerate constant formulas and finitely many short lengths are immediate cases.

### One polynomial bound for all the data and cases

There are at most M listed entries by the delimiter/count accounting in (5). The strategy, output and predicate evaluators have fixed polynomial circuit-size bounds. For each entry, the concrete challenges have polynomial length in N+|u_i|+|C_N|, and the ground checks, one-answer solver evaluations and congruence proof (11) have polynomial length in M. The fixed identity (1) has a polynomial bound in N including original binary variable names.

For each i, the total substitution-circuit description in the corresponding copy of π_N is bounded by a fixed polynomial in M. Even writing a separate DAG for each required circuit gives a polynomial bound; cross-copy sharing is unnecessary. By the imported substitution theorem each copy of (7)–(12) has length at most q(M) for a fixed polynomial q, increased to cover concrete evaluations and binary proof identifiers. At most M copies cost M q(M). Converting and substituting the supplied coverage proof, disjunction elimination, (1), and the final formula/refutation simulations each add or compose fixed polynomial costs. Absorb them into a fixed polynomial r to get (5).

Every term in M is polynomial in N under the hypotheses, including the **sum** of all tuple lengths and the supplied coverage proof. Thus r(M) is one polynomial in N, independent of the particular unsatisfiable F. With a fixed hypothetical SAT algorithm, positive assignments needed for the concrete challenges can also be found by polynomial-time self-reduction. The transformation takes π_N, the list and γ_(N,F) as inputs; it does not generate those supplied proofs or establish their bounds from external SAT correctness.

**Achieved versus required.** The finite-case inference and its total proof overhead are polynomial. Complete-output cover construction and short coverage proofs remain unproved, as do the existential arithmetic premise, a suitable arbitrary-round replacement, and an unrestricted superpolynomial EF/ER lower bound. No claim is made that the coverage-proof hypothesis is easier than EF boundedness: an empty cover for unsatisfiable F already has ¬F as its specialized coverage conclusion. The first-round canonical-recovery obstruction in L014 remains intact. The theorem here succeeds conditionally because it keeps the original assignment variable and handles a separately supplied finite range; it does not remove that range/proof premise.

**Literature classification.** The supporting substitution, simulations and adaptive interface are imported by the precise citations above. The residual conditional finite-cover assembly was not established by the inspected primary statements in the ready assessment. It is classified POTENTIALLY_NEW only in that limited coverage sense, not as certified originality or progress beyond all existing literature. No reproof of KPT or of a general proof compiler is needed; the displayed inference is the exact difference left by the source comparison.

## Mathlib

Coverage: **not checked** for this full conditional transfer, complete-output covers, or the supporting witnessing and CF/EF/ER simulations. Pudlák's Lemma 2.1 and Jeřábek's Lemmas 2.4–2.5, directly linked above, support the syntactic operations; Pich–Santhanam Theorem 7 supplies the related generator transfer, not a full match for these cover hypotheses. No library absence, matching Mathlib theorem, or originality claim is asserted.
