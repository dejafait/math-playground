# L098 — Supplied source Frege gives an exact occurrence-product witness

## Hypotheses

Work over F₂. Supply an explicitly written width-at-most-three CNF F,
including its literal order, clause order and binary conjunction and
disjunction trees. Supply an assumption-free ordinary Frege proof π
whose last formula is exactly ¬F. Use L097's fixed three-scheme/MP
presentation, with the ground axioms true and ¬false. Implication and
conjunction are the fixed abbreviations in that presentation; expanding
them duplicates neither argument. Intermediate proof formulas have no
width or depth restriction. Every formula, name, axiom-instance record
and earlier-line reference is explicit. There is no extension rule or
substitution inference rule. Foreign variables may occur in π.

Supply exactly L087's occurrence pair D,E constructed from this F and
its appended two-clause u/v gadget, with the full provenance/naming map.
Retain the prescribed occurrence alphabet y, ordered representatives
f=r_D, g=r_E, and the complete unchanged Boolean/commutator dictionary
B with placeholders σ_i,τ_ij. The input includes all provenance needed
to rebuild and compare the actual testers. Put

    Q=2+M+|F|+|π|,

where M is L087's full pre-witness input size. No output, witness degree
or unwritten proof tree contributes to Q.

## Conclusion

There is a deterministic construction of an explicit acyclic affine-F₂
ABP H using only y,σ,τ with the formal free-algebra identities

    H(y,0)=0,                 H(y,B(y))=fg.

One fixed polynomial in Q bounds both full binary output length and
construction time, including every independent graph copy, reference,
name and complete dictionary. No polynomial bound on the supplied |π|
in terms of M or |F|, or proof finder from F, is asserted.

This specializes known extraction and local corrected components. It
does not claim certified originality, an executable verified translator,
universal W₂, arbitrary ER data or a SAT decision/separation result.
The separate step-384 all-size informal critical audit below finds no
substantive defect in the interface or composed ledger. It does not
certify an implementation or strengthen the supplied-proof hypothesis.

## Proof

**Coverage and precise imports.** The pre-invocation SPECIALIZE
assessment is
`drafts/literature/2026-10-20-source-frege-occurrence-product-witness.md`;
its COVERED_TARGET is this construction. It inspected Fu Li, Iddo
Tzameret and Zhengyu Wang, *Characterizing Propositional Proofs as
Non-Commutative Formulas*, SIAM J. Comput. 47(4), 1424–1462 (2018),
[DOI](https://doi.org/10.1137/16M1107632), using the
[40-page author revision](https://www.doc.ic.ac.uk/~itzamere/Ideal_non-commutative.pdf),
Definition 1.3 p.6 and Theorem 3.1/Lemma 3.3 pp.13–14, accessed
2026-10-20 (revision date unestablished). These supply the ordered
conclusion convention and ordinary-Frege extraction recurrence.

Receive through L097 §4 its already proved arbitrary-written-proof
graph implementation of that recurrence, including its corrected axiom
seeds and zero seeds for true and ¬false. That component takes any
assumption-free proof in the stated presentation; its induction uses
only the line's axiom/MP justification, never a resolution premise.
We do not apply L097's resolution-input conclusion to a Frege input.
Receive its §1–2 exact tester identifications and correction J as well.
Those components depend on the occurrence pair alone. In particular the
L035/L036 calls and single-order injectivity used below are received
inside those components, with their original-only input qualifications.

The ordered formula-to-graph input remains Ran Raz and Amir Shpilka,
[*Deterministic Polynomial Identity Testing in Non Commutative Models*,
author manuscript, Lemma 2 Step 1, p.5](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
as received in L049/L097. It preserves constants and factor order by
serial/parallel composition. No PIT or graph-to-formula theorem is used.
L049's whole-proof substitution argument supplies the syntactic closure
operation below, not its source-axiom certificate as an fg witness.
The new work is the exact occurrence interface and its written-proof
ledger; no reproof of these extraction or graph results is needed.

**1. Receive the actual trees and exceptional case.** If F has an empty
clause, D starts in its absorbing failure state. Its suffix recurrence
gives f=0 formally. Return the distinct-endpoint no-path zero graph with
all dictionaries. This has the two desired identities and polynomial
size/time. All variable-free unsatisfiable cases are covered this way.
Without an empty clause the empty conjunction would be satisfiable and
cannot have a valid proof of its negation by soundness; it is not a lost
input under the hypotheses.

Otherwise let C_F be F with every literal leaf replaced by its actual
signed occurrence name, keeping exactly F's written connective trees.
Let C=C_F∧C_gad, where C_gad is the conjunction of the two split gadget
clauses in their prescribed order. Thus clause/literal leaf order is
D's order; only conjunction parenthesization is being chosen. L097's
tester identification allows any explicit parenthesization preserving
that order. Equivalently finite associativity of ordered multiplication
preserves its polynomial. No diagram, literal or clause is changed.

For each E-group z₁,…,z_k in its actual order, let

    U_s=(¬z₁∧…∧¬z_k)∨(z₁∧…∧z_k),    U=∧_s U_s,
    G=C∧U.

All trees here are explicit; singleton conjunctions mean their one leaf.
The gadget ensures at least four occurrence names and nonempty groups.
Write v for L097's truth-polynomial translation:

    v(y)=y, v(false)=0, v(true)=1, v(¬A)=1+v(A),
    v(A∧B)=v(A)v(B), v(A∨B)=1+(1+v(A))(1+v(B)).

L097's exact separate-order identifications and correction give

    v(C)=f,    v(U)=g̃,    J(y,0)=0,    J(y,B(y))=g+g̃.       (1)

The equality v(C)=f uses increasing-multilinear injectivity in D's order
only. For clarity the received correction is the ordered telescope
J=Σ_s(∏_{h<s}t_h)R_s(∏_{h>s}e_h), where e_s=a_s+b_s,
t_s=e_s+a_s b_s, a_s=∏(1+z_i), b_s=∏z_i, and
R_s(B)=a_s b_s with R_s(0)=0. Its group witness uses one original-only
commutator call and one Boolean placeholder; L097 proves its exact
factor order, including singletons. Thus g̃ is not silently identified
with g or assumed increasing multilinear.

**2. Transform the complete source proof once.** For each variable x
occurring in F choose its first occurrence r_x; it is z₁ in that
variable's E-group. Let θ(x)=r_x for these variables and send every
other variable in π to a fixed existing gadget occurrence y₁. Apply θ
simultaneously to every formula and axiom-instantiation record in π,
retaining the old line order and MP references. Call the result θπ.

If an old axiom instance substitutes η into a fixed scheme, its new
instance substitutes θ composed with η. Ground constant axioms are
unchanged. An MP pair A,A→B becomes θA,θA→θB, with conclusion θB.
Thus θπ is a valid assumption-free proof ending exactly ¬θF; it has
only occurrence variables. Noninjectivity of θ causes no problem for
these syntactic statements. This transforms the entire written proof;
it does not introduce substitution as an inference from one old line.

**3. Construct the guarded original-CNF implication.** We give actual
finite proof operations rather than using the semantic unsatisfiability
of G. Every operation in this paragraph is a substitution instance of
a fixed classical tautological implication, implemented with MP in the
same three schemes. Fixed proofs exist by classical propositional
completeness. For a fixed template containing constants, first replace
true,false by letters t,d, prove the constant-free curried implication
t→(¬d→V(t,d)), then substitute the constants and use the two ground
axioms. This is precisely L097's constant-template reception and has
constant overhead per template, independent of F and π.

Put E(A,B)=(A→B)∧(B→A), an explicitly expanded formula. Conjunction
projections through the actual binary trees yield G→C_F and G→U_s.
In each disjunct of U_s, projection yields the values of both z_i and
z₁: the first gives ¬z_i,¬z₁ and the second z_i,z₁. The fixed
implications from either pair to E(z_i,z₁), followed by the fixed
disjunction-case implication, yield U_s→E(z_i,z₁). Compose with
G→U_s. All projections are performed through the written conjunction
trees. For k=1 the reflexivity template gives the same result directly.
Consequently there is an assumption-free proof of

    G→E(z_i,r_x)

for every occurrence of every source variable x. Gadget groups need
no replacement. Repeated or opposite source literals have distinct z_i
and the same chosen r_x, with their literal signs still written.

Apply guarded negation congruence at each negative literal. Then traverse
the common connective tree of C_F and θF from leaves to root. For each
binary connective ◇ use the fixed guarded congruence implication whose
premises are G→E(A,A') and G→E(B,B') and whose conclusion is
G→E(A◇B,A'◇B'). It follows by MPs from the already written child
lines. A unary node uses the unary version. This writes the actual
subformulas at every node, not recursively expanded child derivations.
The roots yield G→E(C_F,θF). Together with G→C_F, fixed composition
gives G→θF.

Concatenate θπ with this finite guarded derivation, relocating every
reference by its prefix offset. From its proved last line ¬θF and
G→θF, the fixed tautology

    ¬A→((G→A)→¬G)

and two MPs give R=¬G. This is an assumption-free occurrence-only
ordinary Frege proof. No deduction theorem with an uncharged proof
transformation, extension definition or assumption-discharge rule was
used. The arbitrary intermediate formulas of θπ remain unguarded and
are imported once, with all their original references.

**4. Complement, extract and recover the unchanged product.** Uniformly
substitute ¬y_i for y_i in every line of this constructed proof. This
again preserves axiom instances, constant axioms and MP. Its last line
is T=R[¬y/y]. L097's checked leaf/constant/connective induction for
LTW's falsity convention states

    tr(P[¬y/y])=1+v(P).

It applies to the actual trees above, including their abbreviations.
Since R=¬G, it gives tr(T)=v(G)=f g̃ formally. This is a substitution
in the propositional proof, not a change of the target arithmetic y.

Apply L097 §4's generic corrected graph extraction to this entire
written proof. It returns K(y,0)=0 and K(y,B(y))=f g̃. More explicitly,
each schematic axiom receives its corrected zero-at-zero seed, the
ground true/¬false seeds are zero graphs, and an MP destination i from
j,h receives K_i=K_j tr(ℓ_i)+K_h. One fresh transition graph for each
MP destination and one vertex per line realize this recurrence without
proof-ancestry unfolding. The L035/L036 seed operands are translated
original-only formulas; recursively produced K_j never become their
operands. These are the unchanged qualified components of L097.

Finally take disjoint copies and fresh exterior endpoints for

    H=K+fJ.

Equation (1) gives H(y,0)=0 and
H(y,B(y))=f g̃+f(g+g̃)=fg, in exactly this factor order. Only y,σ,τ
occur and the supplied B is unchanged. Different-order Boolean
vanishing was never used to assert a formal zero identity. Parallel
edges, cancellation and redundant tester records are retained.

**5. Full written-proof and graph ledger.** All counts below use the
original Q, before constructing any witness. Source/proof nodes,
occurrence counts, groups, input records and original name lengths
are at most cQ for a fixed encoding constant. C_F,C,U,G and θF each
have O(Q) nodes. Macro expansion, including E and connective templates,
has fixed factors. Each actual subformula in the synchronized traversal
has O(Q) nodes, even at unbounded depth. It never contains an expanded
proof of a child as a subformula.

θπ keeps at most O(Q) source formula nodes and line records, now with
O(Q)-bit occurrence names, so has O(Q²) bits before harmless reference
framing. Constructing the substitution map, matching old names and
checking all supplied proof records are polynomial-time explicit scans.
For the guarded part there are O(Q) requested occurrence comparisons.
Each uses at most O(Q) projection steps through the written trees plus
fixed case/composition steps. Projecting G to its groups and C_F fits
the same O(Q²) count. The synchronized C_F/θF traversal has O(Q) nodes,
with a fixed number of guarded congruence instances per node. Even
allowing O(Q³) instances for every projection, abbreviation and prefix
administration is a uniform upper bound. Each fixed proof instantiation
has a bounded number of lines of O(Q) nodes, hence O(Q²) actual name
bits per line. Global reference lengths add O(log(Q+2)), not a copy of
the referenced derivation. Complementing every occurrence multiplies
node count and name cost by a fixed factor. Therefore both the complete
constructed Frege bit length S and its construction time satisfy the
deliberately loose bound

    S≤c₀Q¹²,                  time_Frege≤c₁Q¹².             (2)

In particular no bound on a proof's intermediate width, depth or
ancestry has been assumed. Arbitrary axiom arguments in π are paid
as actual formula trees from the input, not expanded into their words.

Put R₀=2+Q+S. The generic graph ledger in L097 §5 after its equation
(10) depends only on this written-proof length S and the occurrence
input Q. Thus it receives (2) without a resolution hypothesis. To make
the composition explicit: each seed has a constant number of received
L035/L036 blocks on inputs of O(R₀²) full bits, including B. Their
respective O(E⁴),O(E⁶) bounds give O(R₀¹²) bits per seed. At most S
seeds give O(R₀¹³) bits. At most S MP destinations have fresh copied
translated-conclusion graphs and connectors costing O(R₀³) in total.
Dense global identifiers/length fields cost at most another factor R₀.
The O(Q) group-correction blocks, all their independently copied
prefix/suffix contexts, the f copy and final dictionary also fit this
O(R₀¹⁴) full-bit bound by L097's pair-only correction ledger. No new
argument is substituted into a witness recursively.

Consequently fixed constants give

    |H|≤c₂R₀¹⁴≤c₃Q¹⁶⁸.                                  (3)

Let d≥6 be a fixed exponent bounding the received L035/L036 bit
algorithms, including writing their output. There are O(R₀) calls on
O(R₀²)-bit inputs. Quadratic copying/renumbering of the entire bounded
record set, formula conversion, reference relocation and parsing fit
the same conservative time estimate as L097:

    time_H≤c₄R₀^max(30,2d+2)
          ≤c₅Q^[12 max(30,2d+2)].                       (4)

All constants depend only on the fixed encodings/templates and received
algorithms. Every complete dictionary is paid within each independent
block and once again at final export. Graph edges remain affine labels;
arbitrary endpoint issues are handled by the fresh exterior terminals,
and the direct zero case has distinct endpoints. Actual path degree is
at most the output edge count. No path enumeration, PIT, expansion of
growing translated arguments or implicit graph is used.

The required threshold is one fixed polynomial in supplied Q; (3)–(4)
meet it. The separate critical audit is recorded below. The construction
supplies no bound in M alone without short
source proofs. Short-Frege availability, arbitrary-order W₂, general ER
representation, every-certificate hardness and unrestricted SAT remain
independent unresolved obligations.

**Independent critical audit — 2026-10-20, step 384.** This audit uses
the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-20-source-frege-occurrence-critical-audit.md`.
The precise LTW and Raz–Shpilka passages cited above were already
inspected in that assessment; no additional source import is made.
L098 is the object checked, not a premise establishing its own transfer.
Receive L049's simultaneous whole-proof substitution, L087's actual
testers, and only the pair-only and generic-written-proof components
of L097. The latter's resolution-input theorem is not applied here.

1. **Source syntax and every variable.** For a fixed axiom scheme A
   and its supplied instance η(A), simultaneous substitution gives
   θ(η(A))=(θη)(A). For MP, θ(¬A∨B)=¬θ(A)∨θ(B), with the original
   predecessor references. True and ¬false remain the same ground
   axioms. Applying θ to all formulas and instantiation records therefore
   yields a proof of precisely ¬θF even if θ identifies distinct source
   variables, including variables absent from F. The output alphabet is
   the occurrence alphabet: the gadget provides an existing image for
   every foreign name. Replacement images are not substituted again.
   No assumption line, extension rule or single-line substitution
   inference is admitted. All connectives are expanded in the fixed
   ∨/¬ basis with their specified factor order; expanding ∧ and → does
   not duplicate either argument.

   The finite template proofs in §3 can also be fixed with no auxiliary
   variables outside their schematic arguments and constants. If a chosen
   completeness proof uses other variables, simultaneously replace all
   of them throughout that fixed proof by one of its schematic arguments
   (each template here has one). The conclusion is unchanged, the same
   axiom/MP check applies, and the proof remains a fixed finite object.
   For constant-containing templates, first use the constant-free
   curried tautology with letters t,d described in §3, eliminate any
   other auxiliary variables in this way, and then substitute true,false
   and apply the two ground axioms. Thus no uncharged or surviving
   variable is hidden in the appeal to fixed-template completeness.
   This spells out a choice already available in that appeal, rather
   than adding a proof rule or a new hypothesis.

2. **Actual-tree guard transfer.** Let A_s and D_s denote the all-zero
   and all-one conjunctions in U_s, respectively. At every occurrence
   i, actual-tree projections prove A_s→¬z_i and A_s→¬r_x, and
   D_s→z_i and D_s→r_x. Fixed curried implications combine the first
   pair into A_s→E(z_i,r_x), the second into D_s→E(z_i,r_x), and
   these into (A_s∨D_s)→E(z_i,r_x). Composition with G→U_s gives
   the claimed guarded equality. The singleton case uses reflexivity
   and does not assume a two-child conjunction exists.

   At a negative literal the two implication directions are transported
   by the fixed negation-congruence template. At a binary source node
   the precise template is

       (G→E(A,A')) → ((G→E(B,B')) →
                      (G→E(A◇B,A'◇B'))),

   for ◇ equal to that node's ∨ or ∧. It is a fixed tautology on five
   schematic arguments, independent of source depth. The argument
   formulas A,B,A',B' are the actual child subformulas, not their
   equality proofs. Two MPs using earlier child lines suffice. This
   checks arbitrary-depth synchronized traversal without nesting child
   derivations or duplicating their ancestry. The leaf signs and actual
   conjunction/disjunction trees of θF are retained, including repeated,
   opposite or tautological source literals.

   The root equality and G→C_F imply G→θF. The imported, unguarded
   proof θπ already proves ¬θF. The final fixed contradiction template
   therefore gives exactly ¬G, assumption-free. Copy θπ only once;
   every later use of its conclusion is a reference. The separate
   guarded derivation has its references offset on concatenation.

3. **Exact arithmetic reception and boundary cases.** In C each
   occurrence name appears in one literal only. Its ordered truth
   polynomial and D's suffix polynomial are increasing multilinear in
   D's order and have the same Boolean evaluations. L097's received
   use of L026 therefore identifies v(C)=f formally. It makes no
   injectivity assertion for the different-order product. Similarly
   g=∏e_s in E's own order, whereas v(U)=∏t_s, with
   t_s=e_s+a_s b_s. For a singleton e_s=1 but
   t_s=1+z₁+z₁², so their correction is necessary even in this case.

   The complemented translation identity follows for a variable from
   tr(¬y)=1+y and for constants from tr(false)=1,tr(true)=0.
   Negation adds 1 to the inductive identity; OR multiplies the two
   complements, and AND gives 1+v(A)v(B). Thus it holds on the actual
   written tree and yields tr((¬G)[¬y/y])=v(G)=f g̃, with no
   factor exchange and without substituting 1+y into the target fg.

   The received group correction is also exact: in L097's notation,
   (1+z₁)(Az₁+z₁A)B'+(z₁²+z₁)AB' leaves
   (1+z₁)Az₁B'=a_s b_s after cancelling the two adjacent
   (z₁+z₁²)AB' terms. Its original-only A,z₁ operands satisfy
   L035, and its Boolean placeholder is the existing B position.
   The ordered prefix-t/suffix-e telescope cancels only consecutive
   intermediate products and leaves g+g̃. Hence K+fJ has endpoint fg,
   and zero placeholders give zero in both summands. No original,
   axiom or placeholder dictionary changes.

   An empty clause makes every D-root path end at scalar zero, so the
   direct distinct-endpoint zero graph is valid formally. In the
   absence of literals an unsatisfiable CNF has an empty clause; the
   empty conjunction is satisfiable and cannot have the assumed proof
   in the sound fixed presentation. Nonempty-clause cases include all
   gadget occurrences, singleton groups and all retained redundant
   tester states. No exceptional input is silently removed.

4. **Generic extraction at arbitrary arguments.** L097's three fixed
   schematic polynomials have degrees at most 3,5,7. Its finite
   commutator/Boolean reduction is in the schematic letters before
   inserting any proof argument. Substituting the actual original-only
   translated argument formulas is a free-algebra homomorphism, so it
   preserves every contextual identity of that finite reduction.
   L035 and L036 receive those argument graphs with the complete B;
   neither receives a recursively generated witness. Constants, repeated
   arguments, high depth and semantic cancellation satisfy those input
   hypotheses. Only the fixed polynomials are expanded into words.
   The ground axiom translations are both zero and use distinct-endpoint
   zero seeds. These cases exhaust all source and generated axioms.

   For an MP line i with antecedent j and implication h, the ordered
   equality P_h=(1+P_j)P_i gives
   K_j(B)P_i+K_h(B)=P_jP_i+(1+P_j)P_i=P_i. At zero
   placeholders the same recurrence preserves zero. Each global path
   to a line vertex ends in either its seed or one of its incoming
   proof-reference transitions. Fresh transition interiors and strictly
   earlier predecessors give an acyclic graph and precisely that
   recurrence. Reused parents are vertices, not expanded proof trees;
   parallel transitions retain multiplicity. Fresh exterior endpoints
   for the final disjoint compositions prevent additional accepting
   paths. The received graph proof therefore applies to the supplied
   Frege sequence without using the former resolution premise.

5. **Independent full-bit/time accounting.** Fix the encodings and
   finite proofs once. Every original count and name length is O(Q).
   θπ has O(Q) nodes/records and O(Q²) restored-name bits. All guards
   and actual subformulas have O(Q) nodes. There are O(Q) requested
   occurrence comparisons; even independently projecting their two
   leaves and group roots uses O(Q²) fixed-template instances. The
   source-tree congruences use O(Q) further instances. The stated
   O(Q³) allowance consequently covers them, with every instance
   contributing a bounded number of O(Q)-node, O(Q²)-bit lines.
   The two uniform substitutions, explicit instantiation records,
   reference offsets and logarithmic reference framing fit S=O(Q¹²).
   Parsing and naive name/subtree comparisons can use polynomial
   scans within the same deliberately loose time bound. No truth-table
   test on an unbounded argument or inference search is required.

   With R₀=2+Q+S, each translated argument or finite seed context has
   O(S) nodes. An independently serialized input graph, with complete
   dictionary, has O(R₀²) bits. The received O(E⁴) and O(E⁶) block
   bounds give O(R₀¹²) per seed and O(R₀¹³) over at most S seeds.
   The at most S independently copied MP conclusion graphs cost
   O(R₀³) in aggregate. Renumbering all graph vertices and length
   fields adds at most O(log R₀), absorbed by the displayed R₀ factor.
   Group correction has O(Q) calls and O(Q²) total copied context
   nodes, and the f copy and final dictionary fit O(R₀¹⁴) as well.
   Thus |H|≤c₂R₀¹⁴≤c₃Q¹⁶⁸ is a full bit bound, not a gate count.

   The fixed exponent d bounds actual received bit algorithms on their
   O(R₀²)-bit inputs. O(R₀) calls therefore cost O(R₀^(2d+1)).
   Even quadratic processing of the entire O(R₀¹⁴)-bit output
   fits the R₀³⁰ allowance. Formula conversion, input checks,
   dictionary copies and the O(Q¹²) Frege construction fit too.
   This proves the claimed time exponent 12 max(30,2d+2) in Q,
   with constants and exponent fixed before choosing F or π.

The all-size audit finds no substantive defect or need to change the
argument, identities, bounds or DAG inputs. This establishes the checked
conditional interface locally; it is a reproduction audit, not a new
extraction theorem, certified originality or a verified translator.
Attempts 018/030/031 and L097's constant repair remain intact.
There is still no short-proof availability theorem, polynomial bound
in M alone, arbitrary ER supplier, universal W₂ or SAT conclusion.

## Mathlib

Full matching coverage for this occurrence transfer, corrected extraction,
explicit affine-ABP construction and complete binary/time bounds: **not
checked**. No theorem-absence or machine-verification claim follows.
The precise primary results and local component qualifications above are
the mathematical inputs; this is an informal specialization, with no
implementation or finite certificate experiment claimed.
