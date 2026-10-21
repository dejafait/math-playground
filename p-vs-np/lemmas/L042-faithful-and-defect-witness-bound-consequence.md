# L042 — Universal faithful AND-defect witnesses would imply NP=coNP

## Hypotheses

Work over the free associative algebra over F₂, with L037's explicit affine-edge ABP, original-axiom, abstract-value-DAG and fresh signed-AND ER conventions. A host original CNF K has width at most three, and π is a valid supplied ER refutation. Every extension has a defining clause and a derived signed unit in the final inference ancestry. All original variables occur in K. Fidelity means agreement with the recursively defined extension function on **every** original Boolean assignment, independently of satisfaction of K.

Supply a complete x-only representative collection: originals and constants have their exact formal values, signed nodes have exactly r_NOT_v=1+r_v, and extension roots are all-assignment faithful. Graphs are finite explicit acyclic affine-F₂ multigraphs with designated endpoints, with the empty-path convention; all records, labels, roots, alphabets and framing are charged. Implicit graphs and circuit-valued edge labels are excluded. No local relation witnesses are inputs. Set

    M=2+T+S+E_val,       T=2+|K|+|π|,

where S counts abstract value nodes and E_val includes all representative graphs, root associations and complete original-axiom/placeholder dictionaries. E_val includes no H graph; M includes neither an H degree h nor a supposed H size bound. Construct any omitted framing before measuring M.

For original variables y define B_y to consist only of b_i=y_i²+y_i and b_ij=y_i y_j+y_j y_i for i<j, with independent placeholders σ_i and τ_ij. Assume the **unproved restricted universal premise V**: one polynomial p, independent of the supplied instance and collection, bounds the full aggregate encoding of some alternative affine-ABP witnesses H_i for every AND node of every such supplied faithful collection, with formal identities

    H_i(y,0)=0,       H_i(y,B_y)=r_i+r_u r_v.                (1)

Here u,v are its actual signed operands, in their specified order. Only Boolean and pair-once commutator placeholders are allowed in H_i; original-clause and extension-axiom placeholders are forbidden. Nonlinear placeholder use and cancellation are allowed. Complete witness framing is charged to p(M). This is universal over **every supplied faithful collection**, not merely existence of a convenient collection. No constructor, fidelity tester, earlier H, premise U or class equality is assumed. Finite root-degree bounds can be chosen after the graphs exist; no sought bound is charged to M.

Use L041's ordered 3-CNF translation and repaired deterministic formal-identity verifier, with its precise primary PIT and completeness inputs.

## Conclusion

    V implies NP=coNP.

Indeed V supplies polynomial-size Boolean/commutator-only witnesses for L041's ordered challenge polynomials f_F. One genuinely used extension z iff (a AND a), with the supplied representative r_z=aa+f_F, suffices. This is a conditional burden on the faithful relation premise, not a proof or refutation of V, a constructor, a converse, an ER lower bound or a P-versus-NP resolution. The separate critical audit on 2026-10-08 found no substantive error within these hypotheses; the argument remains informal, without a verified implementation. The approved search found no full matching theorem; originality is not certified.

## Proof

**Assessed scope and imports.** The pre-invocation EXPLORE assessment is `drafts/literature/2026-10-08-faithful-and-defect-witness-obstruction.md`. Its universal supplied-collection quantifier and witness-excluding M are retained exactly. L037 specifies the interface being tested; its certificate-assembly conclusion is not used. L039's generic used-ancestry construction motivated the check, but no representatives from U or that construction are needed: the three resolutions below prove ancestry directly. L035/L036 concern particular commutator/Booleanity defects and do not furnish (1) for this collection. Attempts 020/021 concern fixed outputs and are unchanged.

L041 supplies the challenge translation, endpoint-safe graph operations and the repaired verifier for arbitrary affine-ABP descriptions. Its primary zero-test input is Raz–Shpilka, [*Deterministic Polynomial Identity Testing in Non Commutative Models*, author-hosted 16-page manuscript, Definition 1 p.4 and Theorem 4 p.9](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf): deterministic O(s⁵+s n⁴) field operations for homogeneous adjacent-layer linear-edge ABPs with unique source/sink and singleton terminal layers. We apply it only through L041's finite constant-path closure, designated-output restriction, support-path pruning and direct no-path/degree-zero cases, which meet those hypotheses. F₂ has constant-cost field operations. No PIT algorithm is reproved or applied to unrestricted circuits.

The standard named Cook–Levin theorem, including 3-SAT completeness, is cited in Cook, [*The P versus NP Problem*, §2 pp.4–5](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf). The short-certificate consequence also agrees with Cook–Reckhow, [*The Relative Efficiency of Propositional Proof Systems*, JSL 44(1), 36–50 (1979), §1 Definitions 1.3/1.5 and Propositions 1.1/1.4/1.6, pp.37–38](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf). Foundations/02 and /05 fix the encoding/complement conventions. These imports establish supporting verification and completeness facts; the new specialization to supplied faithful defects is the construction below. No claim about a particular polynomially bounded ER system follows from Cook–Reckhow.

**Challenge graph.** Let F be any well-formed width-at-most-three CNF, N=|F| and L=N+2. Its n distinct variables x_1,...,x_n and m clauses are explicitly listed; n,m=O(L). Preserve identifier names in a dictionary and retain literal/clause order. For clause D_j use

    c_j=product_(ell in D_j) v(ell),
    v(x_i)=1+x_i,     v(NOT x_i)=x_i,
    s_j=1+c_j,        f_F=s_1 ... s_m.                     (2)

Empty products are 1. As proved in L041, f_F(b)=1 exactly when b satisfies F. Its explicit graph G_F has O(m+1) records: expand only each at-most-three-factor clause, into at most nine word paths of length at most three, then concatenate the clause gadgets. There is no expansion across clauses. The graph and original-name dictionary have O(L³) full bits. Literal repetition, complementary literals, empty clauses and m=0 are covered by this construction. In particular F is UNSAT exactly when f_F is Boolean-zero.

**A host with one genuinely used extension.** Introduce one fresh original variable a and a fresh extension z, using new identifiers distinct from all challenge identifiers. The host is the easy contradiction

    K=(x_1) AND ... AND (x_n) AND (a) AND (NOT a).

Thus its original variables are exactly y=(x_1,...,x_n,a), including any variables unused by the eventual witness. Their all-assignment fidelity domain is all of {0,1}^(n+1); the host units do not restrict that domain. The challenge F is not K and need not have a short ER refutation.

Introduce z iff (a AND a). Its three defining-clause slots, after sorted-set duplicate-literal removal, are

    D_1=(NOT z OR a),  D_2=(NOT z OR a),  D_3=(z OR NOT a).

The two identical projection clauses are permitted defining slots, not two fresh definitions. Keeping both records is valid; no argument needs both. Resolve D_3 with the initial (a) on a to derive (z); resolve D_1 with initial (NOT a) on a to derive (NOT z); resolve those two units on z to obtain the empty clause. These are selected-pivot resolutions with earlier premises and fresh z. There are n+2 initial unit records, three defining slots and three resolutions, at most n+8 proof records. Every clause has width at most two.

The final inference has both derived signed units as parents, with D_1 and D_3 as ancestors. There is exactly one extension, so every extension has a defining clause and a derived signed unit in final ancestry (in fact both signs). No accumulator or challenge-circuit extension has been introduced. Unused host input units are allowed by the premise. The immediate alternative refutation of K is irrelevant to the supplied-proof quantifier.

**Complete representatives and the defect.** Supply exact representatives y_i for every original variable, 0 and 1 for constants, and

    r_z=aa+f_F.                                             (3)

Supply every negative signed root as its exact formal complement, including r_NOT_z=1+aa+f_F and r_NOT_a=1+a. These cover every value used in the proof and both signed operands of its one AND node. One possible abstract DAG contains n+1 original nodes, two constant nodes, the one reduced AND node z with operands a,a, and one complement node for each original or extension variable. Thus S≤2n+6; constant complements can be aliases of the two exact constants. The internal vertices of G_F are implementation records of r_z, not extra extension gates or abstract AND nodes needing further representatives.

Construct aa by a two-symbol path and r_z by its parallel sum with a disjoint G_F, with fresh exterior endpoints and 1-connectors. Construct r_NOT_z by a further constant-1 branch. Constant zero can have distinct disconnected endpoints; constant one a 1-edge. Each other signed/base representative has constant-size graph apart from its variable identifier. All copies, including a separate G_F copy in the signed root, are charged; no graph sharing or implicit list is needed. L041's endpoint-safe serial/parallel operations apply, and our constructed roots already have fresh distinct terminals.

For completeness now suppose F is UNSAT. For every scalar assignment (b,α) to (x,a), (2) gives f_F(b)=0, so r_z(b,α)=α²=α. This equals the recursive Boolean function a AND a on that assignment. Exact complements give fidelity of every signed root as well; base and constant roots are exact regardless of F. This proves the supplied collection belongs to V's domain for UNSAT F, without assuming V to create any of its graphs. Fidelity is not asserted on satisfiable challenges.

Its sole AND defect is the formal free-ring identity

    r_z+r_a r_a=(aa+f_F)+aa=f_F.                            (4)

This cancellation uses identical ordered words and F₂ addition, not Boolean reduction or commutation. Repeated operands are permitted by the assessed ER/interface convention. No original-clause placeholder discharges any part of (4).

**One noncircular input bound.** There are O(n+m+1)=O(L) representative graph records and O(L) abstract associations. The host proof has O(L) bounded-width records. Dense fresh identifiers and proof references use O(log L) bits; even charging each retained original name O(L) bits gives T=O(L²). The complete host original-axiom framing consists of n+2 constant-width clause falsity polynomials and (n+1)+(n+1)n/2 Boolean/commutator polynomials with their independent placeholders. It has O(L²) constant-size word records; even repeating O(L)-bit names at every occurrence gives O(L³) bits. Graph framing, affine labels, separately written signed roots, all root associations and dictionaries fit the same bound. Fresh a,z can be assigned dense tagged identifiers, preserving the old-name map with polynomial length. Hence for one encoding-dependent absolute C,

    E_val≤C L³,       S≤C L,       M≤C L³.                 (5)

Enlarge C once to cover small encodings. Construction is polynomial bit time in N. This ledger includes neither sought witnesses nor their degrees. If a representative-degree parameter is desired, d=max(2,3m) bounds every supplied root before substitution, since each word of (2) has length at most 3m. It is not necessary to assume h: once V supplies finite affine DAGs, their vertex counts bound their complete formal degrees, and h can be set to the maximum of these bounds and 1. This retrospective observation does not put h into M or invoke L037's assembly.

**Witness extraction and removal of the anchor.** Apply V only when F is UNSAT and the preceding fidelity argument holds. There is just one AND node, so V supplies some H=H_z with full length at most p(M), using only B_y placeholders, satisfying

    H(x,a,0)=0,       H(x,a,B_y)=f_F(x).                    (6)

No other relation is needed. H may use a, σ_a and every anchor commutator τ_(i,a), as well as nonlinear placeholder products. Define a substitution φ on its free alphabet by setting a, σ_a and all τ_(i,a) to zero, retaining every x_i, σ_i and τ_ij with i,j≤n. Call the resulting graph H'. Implement φ by deleting those terms from affine labels (or keeping zero edges), then replace its framing by the challenge-only dictionary. The graph stays acyclic and affine and its full encoding is polynomial in |H|+L; there is no path expansion. Endpoints, cancellation and nonlinear terms are preserved under the complete substitution.

Let ψ be the free-ring homomorphism on original variables setting a=0. It sends b_a=a²+a and every b_(i,a)=x_i a+a x_i to zero, and fixes B_x. Therefore on **each generator** the two substitutions agree, yielding

    H'(x,0)=0,       H'(x,B_x)=ψ(H(x,a,B_y))=f_F(x).        (7)

The generator check extends to every ordered product and sum, including all nonlinear placeholder sectors; no commutation is used. Unused host clause-placeholder dictionary entries, if retained in input framing, are removed; none can occur in H by V. Thus H' has precisely L041's permitted challenge alphabet and identities. A polynomial majorant of p composed with (5) and the polynomial framing cost gives one fixed polynomial q such that |H'|≤q(N+2) for every UNSAT F. Its exponent and constants do not depend on F. No search algorithm for H is claimed.

**Promise-free verification and consequence.** Use exactly L041's deterministic verifier on (F,H'). It recomputes (2) and B_x, validates all explicitly written graph/dictionary records and acyclicity, and checks the two formal identities in (7) by bounded axiom substitution and its repaired PIT normalization. Invalid formulas, foreign symbols or malformed graphs are rejected. Declared counts cannot cause allocation beyond the written records. Runtime is polynomial in |F|+|H'| for every submission, including false identities, nonextremal/coincident endpoints and cancellation-based graphs. No host proof, supplied collection, fidelity claim or UNSAT promise is submitted or checked.

For clarity, soundness uses only the accepted identities: if b satisfies F, all B_x(b)=0, whereas (2) gives f_F(b)=1. Evaluating (7) at b instead gives f_F(b)=H'(b,B_x(b))=H'(b,0)=0, a contradiction. This remains valid for arbitrary malformed-promise submissions that pass syntactic checks; V is used only for completeness and the polynomial certificate bound. Guessing H' up to q(N+2) and running this fixed verifier places well-formed 3-CNF UNSAT in NP. Cook–Levin and complement closure give NP=coNP as in L041 and foundations/05. The host's short ER proof alone proves nothing about F.

**Boundary cases and limitations.** Empty clauses give s_j=0 and hence f_F=0 formally; the construction and a zero witness remain valid. With m=0, f_F=1 and F is satisfiable, so completeness makes no claim and verifier soundness rejects every proposed H'. With n=0 the fresh a still permits the same host/refutation; an unsatisfiable variable-free CNF contains an empty clause, and after anchor elimination the challenge dictionary is empty and the degree-zero check suffices. Short, repeated and complementary literals are covered by (2) without semantic simplification. The host remains valid and polynomial-size for all challenges; only its supplied representative fidelity depends on UNSAT. This conditional use is legitimate because the verifier does not accept on the basis of that promise.

V is unproved. Universal coverage of supplied representatives is essential: an existential premise could choose r_z=aa and avoid encoding the challenge. This proof does not transfer to that different premise, forbid contradictory hosts, bound witnesses using T alone, or supply a constructor. It does not assume U, NP≠coNP, earlier H or an ER simulation. The result identifies a conditional proof-complexity burden already present in local faithful defects. General data existence, nonfaithful alternatives, every-certificate hardness and unrestricted SAT decision/separation remain unresolved.

**Separate critical audit (2026-10-08, step 109).** Under the pre-existing SPECIALIZE assessment `drafts/literature/2026-10-08-faithful-and-defect-critical-audit.md`, the following checks independently support the preceding conditional argument. No theorem hypothesis, construction or bound required repair.

The logical order is one fixed p, then every eligible supplied collection, then some witnesses. For each UNSAT challenge the explicitly constructed collection is eligible; p cannot depend on that challenge, its graph or its chosen witness. The collection is constructed for all challenges, but its fidelity is proved only in the UNSAT completeness case. There is no need to decide which collections are eligible. Applying V to this collection therefore gives the clause-specific certificates used by L041. It does not assert V⇒W for arbitrary Boolean-zero graphs. The existential-choice variant has a different quantifier and is not reached by this argument.

The actual ER convention in foundations/05 allows identical earlier operands. The two projection slots coincide as clauses without violating freshness of z. The positive-unit derivation uses D₃ and (a); the negative-unit derivation uses D₁ and (NOT a); the final resolution uses both units. This checks the required ancestry directly, without any circuit-embedding theorem. The n unused host units ensure original occurrence of the challenge variables and are permitted: the hypothesis requires used extensions, not that all original clauses be used. The abstract count is (n+1)+2+1+(n+2)=2n+6. Each negative root has its exact formal complement. The paths implementing f_F add no abstract extension, so V owes exactly one H in this construction.

For the input bound, each clause contributes a bounded word gadget, not a factor in an expanded product. Two written copies of G_F suffice for the positive and negative extension roots; all other roots have bounded graph size. The O(L) proof/root records and O(L²) axiom records, with at most O(L) bits per retained original name, give the claimed O(L³) bound on full input bits. The exact constants and complements and every root association are included. In particular, neither a proof of fidelity nor the sought H nor its degree is present in M. To make the witness quantifier explicit, dominate p(t) by A(t+1)^d. If extraction has fixed encoding bound C'(|H|+L+1)^e, then one may take

    q(L)=C'(A(CL³+1)^d+L+1)^e.

All these constants are independent of F. This justifies the single polynomial certificate bound without assuming monotonicity of p, a witness constructor or a uniform choice of witnesses.

The anchor substitution fixes each x_i, sends a to zero, retains each challenge placeholder and sends σ_a and every anchor-pair placeholder to zero. Composing it with axiom substitution agrees with setting a=0 after substitution: the anchor Boolean axiom and both ordered monomials of every anchor commutator go to zero; challenge axioms are fixed. Composing with zero-placeholder substitution also agrees generator by generator. These equalities are free-algebra homomorphism equalities and hence preserve arbitrary ordered nonlinear placeholder products and cancellation. At graph level they only change affine coefficients and framing. They do not duplicate paths, introduce cycles, change the designated endpoints or require a fidelity test.

Finally the receiving verifier is exactly the repaired L041 interface, whose proof was read in full. Every extracted graph fits its explicit affine-label/alphabet syntax. Its constant-size axiom gadgets, finite constant-path closure, designated-output restriction, support-path pruning and separate degree-zero/no-path cases retain formal identities for all submissions. F₂ and the bounded-size trimmed homogeneous graphs meet the cited Raz–Shpilka theorem. Soundness uses only these accepted identities and scalar evaluation; the contradictory host, p and V play no part in that argument. An NP machine may fix q in its code even though the verifier itself does not know q. Empty clauses, the no-clause formula, n=0, repeated/complementary literals, sparse identifiers, foreign symbols, invalid counts, nonextremal/coincident endpoints and cancellation-based graphs are covered by the displayed construction or L041's all-input verifier. The standard complement inference then gives precisely NP=coNP.

The audit establishes no new witness bound or stronger complexity consequence. It leaves V, constructors, converses and the main decision gap open. L041 remains the sole direct mathematical lemma input; L037 supplies interface conventions and no assembly theorem is invoked. The prior fixed-output stops remain intact. No finite diagnostic or new mathematical script was needed for these symbolic and all-size checks.

## Mathlib

Full matching implication, graph specialization and complete-bit bound: **not checked**; no absence or mechanization claim. Supporting PIT and completeness results are imported by the precise primary citations above and L041's repaired receiving-model proof. The elementary one-gate host, faithful zero perturbation and anchor substitution justify the part not supplied by those source statements. POTENTIALLY_NEW classified the original construction only because its ready comparison found no full match; it did not certify novelty. The separate step-109 audit is REPRODUCTION and found no substantive error; it is neither mechanization nor a main-problem resolution.
