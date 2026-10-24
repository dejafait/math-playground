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

**Current qualification — steps 438/440.** Section 6 replaces the unsupported
template reception and extraction in the preserved proof below. It
translates the supplied proof in its original three-scheme/MP presentation
into L108's four-rule system, without assuming source completeness or
strengthening the supplied-proof hypothesis. The independent step-440
audit in §7 finds no substantive defect in the whole-CNF assembly or
original-Q ledger under these hypotheses. No fixed library archive or
implementation is verified.

**Preserved old-interface qualification — step 422.** L107 establishes incompleteness
of the exact source presentation specified above. Even when an exact
source proof π is supplied, §3's separate invocation of completeness
for guarded literal-OR templates is unsupported in that presentation.
The conditional witness assembly below therefore has an unresolved
template-interface gap; the historical step-384 audit did not detect it.
The whole-proof variable substitution remains a syntactically valid
operation, but does not by itself supply those additional templates.
This is not a counterexample to witness existence by other methods.

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
The step-384 audit is preserved as historical reasoning, subject to the
step-422 qualification. It does not validate the old completeness appeal
or the new section 6, certify an implementation, or strengthen the
supplied-proof hypothesis.

## Proof

Sections 1–5 and their step-384 audit are preserved superseded work where
qualified above. Section 6 is the current proof, receiving only their
actual-tree definitions and simultaneous-substitution operation, and
the specified audited components of L097. In particular its receiving
extractor is L108, not the historical three-scheme recurrence.

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

**6. Four-rule source-Frege replacement — step 438, 2026-10-23.**

This proof keeps the original hypotheses, Q and ordered output fg/B.
It replaces the old guarded-template completeness invocation, growing
proof assembly and extraction ledger. The pre-invocation SPECIALIZE
assessment is
`drafts/literature/2026-10-23-four-rule-source-frege-repair.md`.
Use L087's exact occurrence provenance and L097 §§1–2/6.2–6.3/6.5–7
for the separately audited tester identification, ordered correction,
primitive premise reception and fixed-library tree operations. L097's
resolution-input conclusion is not applied to this Frege input.
Use L108 for extraction and L109 for fixed-library preparation/replay.

The precise completeness input, only through L109, is Joseph R.
Shoenfield, *Mathematical Logic* (Addison-Wesley, 1967), §2.6 pp.21–22,
§3.1 Tautology Theorem (Post) p.27, Detachment Rule/corollary p.28,
propositional proof pp.28–30, in the
[primary scan](https://w2.cs.uni-saarland.de/op/fullpaper/logics/SHOENFIELD_Mathematical_logic.pdf).
It applies to the receiving system, not the old source presentation.
L109 supplies the truth-constant and full-bit specialization absent from
that source statement. The LTW citation above remains a translation/
extraction comparison; no tree-size or source-completeness theorem is
imported for this construction. No completeness reproof is needed.

**6.1 Fix the library before receiving any input.** Use primitive ∨,¬
and constants, and expand A→B as ¬A∨B, A∧B as ¬(¬A∨¬B), and
A↔B as (A→B)∧(B→A). Expand recursively, preserving both ordered
arguments. Chains of → associate to the right. Set
E_G(A,B)=G→(A↔B), with the same literal expansion. These are formula
notations, not new rule tags. Start with the fixed library of L097
§6.1 and adjoin exactly these four ordered templates:

    S₁ = A→(B→A),
    S₂ = (¬A→¬B)→((¬A→B)→A),
    S₃ = (A→(B→C))→((A→B)→(A→C)),
    D  = ¬A→((G→A)→¬G).

These are fixed finite trees after expansion. S₁ is true when A=0 by
its outer implication and when A=1 by its final consequent. In S₂,
A=1 makes the inner consequent true; when A=0 its first antecedent
has value ¬B and its second antecedent value B, so they cannot both
be true. For S₃, if A=0 its last implication A→C is true. If A=1
and both outer antecedents are true, B→C and B are true, forcing C.
For D, true ¬A makes A=0; true G→A then forces G=0 and hence ¬G.
Thus all four are tautologies for every assignment to their slots.
The other library members have the exhaustive Boolean checks and
independent audit recorded in L097 §§6.1/7. Constants and coincident
slot images do not restrict these truth-function arguments.

Apply L109 to this single finite union library, choosing one entire
primitive proof for each member once and for all. This preparation
has no polynomial bound in library size; the fixed finite strings and
their slot multiplicities are compiler constants. No input tautology
is searched for a proof. A library call writes its full instantiated
primitive proof with relocated internal references. Its endpoint is
exactly the expanded template instance, with only names in its argument
trees. Use L097 §6.2's five expansion/axiom/cut/cut/contraction records
for each actual antecedent of any curried theorem. No MP tag is added
to the receiving system, and no antecedent proof is copied or opened
as an assumption. This receives arbitrary-depth argument trees.

**6.2 Translate every source record without a new input premise.**
Keep the empty-source-clause branch of §1: f=0 formally, so return a
distinct-endpoint no-path graph with the unchanged full dictionaries.
Otherwise form exactly C_F,C=C_F∧C_gad,U,G=C∧U from §1. Their
literal and clause orders are the prescribed ones; C_F retains F's
actual conjunction/disjunction bracketing, while the final ∧ with the
gadget changes only product parentheses. L097's separate D-order
identification still gives v(C)=f. All gadget occurrences remain.

Choose r_x as the first occurrence for each variable in F, and map
every foreign source-proof variable to one existing gadget name y₁.
The gadget ensures that this name exists. Apply this simultaneous θ
to every supplied source formula and axiom-instantiation argument,
with constants fixed. A source axiom instance η(S_j) becomes
(θη)(S_j), so append the full L109 proof of that S_j instance.
Append each source true or ¬false record as the corresponding permitted
ground axiom. Store for every source line i the actual receiving record
index ρ(i) with endpoint θ(π_i). This association is metadata, not a
receiving inference or an assumption.

If line i is MP with earlier lines j:A and h:¬A∨B and conclusion B,
the endpoints at ρ(j),ρ(h) are exactly θA and ¬θA∨θB. Append
L097 §6.2's five primitive records with these actual premise indices,
and set ρ(i) to the last, whose tree is exactly θB. This checks both
literal matching and reference order. Induction over all supplied lines
therefore produces an assumption-free primitive archive ending at
¬θF. Every source line, including unused records, is processed once.
Repeated premises, repeated source formulas, constants, noninjective θ
and foreign variables cause no change to this syntactic induction.
Intermediate depth is unrestricted. In particular the old source is
not assumed complete: only its legal supplied records are translated.

**6.3 Traverse the entire original CNF under the guard.** Append to
that archive an instance of G→G. Using the actual conjunction paths,
L097's projections and guarded composition give G→C, G→C_F and
G→U_s for every relevant original-variable group s. All are proved
implications; no guard is opened as an assumption.

For each occurrence z_i of x in group s, receive L097 §6.3's branch
construction with representative r_x. More explicitly, write
U_s=A₀∨A₁ for its actual all-zero and all-one conjunctions. Start
separately with A_b→A_b and project along their actual trees to obtain
A₀→¬z_i, A₀→¬r_x, A₁→z_i and A₁→r_x. The fixed same-negative/
same-positive branch implications give A_b→(z_i↔r_x), and Cases
with G→U_s gives E_G(z_i,r_x). For singleton groups these paths
have length zero and the same construction applies with equal selected
leaves; guarded reflexivity is also available. Gadget groups require
no source replacement but remain in U and B.

Now literally expand the entire pair C_F,θF into ∨/¬/constant trees.
They have the same connective skeleton. Traverse it from leaves to
root, storing an actual endpoint E_G(A,A') for each pair of subtrees.
At a variable leaf use the occurrence equivalence just proved; a
constant leaf uses guarded reflexivity. At a unary node use guarded
negation on the child endpoint. At a binary OR node use guarded OR
congruence on both earlier child endpoints, with their actual ordered
subtrees as arguments. Each use is a library proof followed by the
five primitive detachment records per antecedent. The expansion of
every source conjunction is handled by these same NOT/OR steps; no
new AND inference or depth assumption is introduced. Negative literals,
repetitions, complementary literals, tautological clauses and arbitrary
original conjunction bracketing are consequently retained exactly.

This induction ends at E_G(C_F,θF). Guarded transport from the earlier
G→C_F yields G→θF. Instantiate D with A=θF and this exact G, and
receive first the earlier source endpoint ¬θF and then G→θF. The
result is exactly R=¬G. Every endpoint use is an earlier index; neither
the source proof nor a child's derivation has been unfolded. All
slot names have disappeared on instantiation and all source names have
been replaced by θ, so only occurrence names remain throughout.

**6.4 Complement the complete archive and extract the exact product.**
Apply y_i↦¬y_i simultaneously to every written primitive record, fixing
the constants. Literal axiom/rule replay is L109's substitution argument:
each of expansion, contraction, association and cut has exactly its
substituted argument trees and the same backward references. Ground
axioms remain ground axioms. This produces a nonempty assumption-free
L108 archive Π with exact endpoint T=(¬G)[¬y/y]. It is not a new
substitution inference and is not a substitution in the target fg or B.

For completeness of the endpoint calculation, L097 §6.5's induction
tr(P[¬y/y])=1+v(P) applies on these literal expanded trees. At an atom
it says tr(¬y)=1+y; at false/true it says 1=1+0 and 0=1+1.
Negation adds 1 to the previous value; OR gives
(1+v(A))(1+v(B))=1+v(A∨B), with that order. Conjunction follows
from its literal expansion. Thus tr(T)=v(G)=f g̃, where g̃=v(U).

Supply this entire Π, the original occurrence alphabet and unchanged
B/placeholder dictionary to L108. All its syntax, alphabet, constant,
assumption and reference hypotheses were checked above. It gives K
with K(y,0)=0 and K(y,B(y))=f g̃. Receive L097 §§1–2's exact J,
including singleton groups, J(y,0)=0 and J(y,B(y))=g+g̃. Its original-
only inputs and ordered prefix-t/suffix-e telescope are unchanged;
it does not identify g̃ with g. Independently copy the graphs and use
fresh exterior endpoints to form H=K+fJ. Then, in the free algebra,

    H(y,0)=0,
    H(y,B(y))=f g̃+f(g+g̃)=fg.

Only identical ordered products cancel. No single-order injectivity
is applied to fg, no occurrence is deleted, and B is never changed.
L108 and L097's elementary ordered series/parallel formula graphs
ensure that all edge labels are affine, including constant/zero cases.

**6.5 Fresh original-Q full-size/time ledger.** All constants below are
fixed by the encodings, prepared finite library and received algorithms,
before the input is chosen. Every source record/formula node count,
occurrence/group count and individual name length is O(Q). Literal
expansion multiplies source tree size by a fixed factor. θ replaces
one name leaf by one name leaf, so even a deep source formula, each
source axiom argument, and every subtree of C_F or θF has O(Q) nodes.
C,U,G also have O(Q) nodes. Each has O(Q²) full bits when names are
pessimistically charged Q bits per occurrence.

Source translation has O(Q) library calls/MP operations and ground
records. Each fixed proof has a bounded number of records, all of
whose slot occurrences are fixed constants; source arguments and
intermediate library formulas therefore have O(Q²) full bits. The
whole source translated part has O(Q³) formula bits. Its root-index
map has O(Q) entries. It stores actual earlier indices, not copies
of the subproofs they reference, and pays every unused source record.

Group/branch projections need at most O(Q²) requested actual paths,
each of length O(Q), a conservative O(Q³) library-use bound. The
whole expanded CNF traversal has O(Q) nodes and a bounded number of
library uses per node, including reflexivity/negation/OR and transport.
Each use copies G and a bounded collection of actual subtrees of
O(Q) nodes; it never inserts a previously proved equivalence or its
derivation as a new growing argument. Final discharge adds boundedly
many uses. Thus O(Q³) calls/primitive records and O(Q⁵) full formula
bits cover the entire archive. Global references cost
O(Q³ log(Q+2)); fixed library constants are absorbed. Retaining the
complete occurrence dictionary even at each library call still fits
this bound. Complementation adds a constant node factor, not new names.
In particular the complete input length for L108 satisfies the fresh,
deliberately loose bound

    R₁=2+|Π|+|occurrence alphabet|+|B/dictionary| ≤ c Q¹².

This is derived for this assembly, not inherited from the superseded
ledger or from a resolution proof. L109 takes O(Q⁴) bit time per call
on O(Q²)-bit argument data, so all O(Q³) calls cost O(Q⁷). Even a
full O(Q⁵)-bit archive scan at every such call costs O(Q⁸). Syntactic
input/provenance checking, θ-name comparisons, explicit reference-map
lookups and relocation, writing complemented copies and retaining all
supplied records fit the conservative preprocessing allowance O(Q²⁰).
These are syntactic operations; no semantic validity or UNSAT test is
used. Fixed-library preparation remains an unbounded compiler constant.

L108 now gives |K|≤C R₁¹⁴≤C'Q¹⁶⁸ and time at most C R₁^b for
one fixed b. For J, receive L097's pair-only ledger: at most O(Q)
original-only L035 calls have full inputs O(Q²), including B, and
the safe O(E⁴) block-size bound gives O(Q⁹) aggregate bits before
numbering. Independently copied prefix/suffix/formula contexts cost
O(Q³) bits; global numbering and all dictionaries fit O(Q¹⁰) bits.
If d bounds L035's bit algorithm, O(Q^max(22,2d+3)) suffices for J.
This uses Q only as an upper bound for the pair data, not as a witness
size. No recursively generated witness is an L035 input.

Final disjoint copying, connectors, full dictionaries and reindexing
add at most a logarithmic factor to the graph size. A quadratic scan
of the fully numbered result suffices for straightforward bit copying.
Therefore one valid common pair of bounds is

    |H| ≤ C Q¹⁷⁰,
    time(H) ≤ C Q^max(340,12b,2d+3).

Actual path degree is at most the explicit edge count. These bounds
meet the required fixed-polynomial threshold in the original Q with
arbitrary intermediate depth, foreign variables and unused records.
This repairs a conditional receiver, classified as reproduction of the
assessed machinery, without certified originality. The independent
step-440 audit in §7 checks this all-size assembly; no serialized library,
mathematical program test or implementation is claimed. L107 and Attempt 036 remain
valid old-interface failures. In particular this construction supplies
no proof for their forbidden old-source endpoint and does not repair
L106's stopped source compiler. Short proofs, M-only bounds, universal
W₂, arbitrary ER data and unrestricted SAT remain independent gaps.

**7. Independent critical audit — step 440, 2026-10-23.**

This audit concerns the original Hypotheses, §§1–2's actual-tree
definitions and the step-438 replacement §6. Its pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-23-source-frege-four-rule-repair-critical-audit.md`.
It does not validate the superseded source-completeness appeal or its
historical audit. Receive L087's exact construction, L097's audited
tester/correction and primitive tree operations, L108's audited supplied
archive extractor, and L109's audited fixed-library specialization.
The precise Shoenfield citation in §6 supports the receiving library
only; no completeness or short-proof theorem for the old source is used.

**Library and source reception.** After literal expansion the four new
members are fixed Boolean tautologies. For S₁, A=0 makes the outer
implication true and A=1 makes its final consequent true. S₂ is true
if A=1; if A=0 its two successive antecedents have values ¬B and B,
so cannot both hold. For S₃, A=0 makes both A→B and A→C true;
if A=1, truth of A→(B→C) and A→B forces B and then C.
D has its only nonvacuous case A=0 and G→A true, which forces
G=0. These arguments exhaust all Boolean slot assignments. Literal
expansion retains these truth functions; constant or coincident formula
images are allowed. L097's other library members retain their audited
truth checks. The union library and its selected entire proofs are fixed
independently of F, π and Q. L109 therefore applies without requiring
bounded image depth, fresh image names or a uniformly efficient search
over input tautologies. Every auxiliary atom of its prepared proofs has
already been eliminated as in L109, so only instantiated occurrence
names and constants can enter this archive.

For each legal source axiom η(S_j), θ commutes with every connective
and gives exactly (θη)(S_j), which is the endpoint of the corresponding
whole library instance. Source true and ¬false remain permitted ground
axioms. For source MP endpoints A and ¬A∨B, their stored images are
θA and ¬θA∨θB. With X=θA and Y=θB, the actual receiving records
are Y∨X by expansion of X, ¬Y∨Y by axiom, X∨Y by cut with pivot Y,
Y∨Y by cut with pivot X and the stored ¬X∨Y, and Y by contraction.
Each cut has precisely its ordered residuals; each premise is earlier.
The final record thus has the exact required tree, without a new MP
tag. The same five-record check applies successively to the curried
antecedents of every later library theorem.

Induction over all source lines gives an actual index ρ(i) for θπ_i;
the last source endpoint is exactly ¬θF. Noninjective θ preserves
syntactic equality and every rule instance. No rule imposes distinctness
of formula images or premise indices. Every source record, including an
unused one, is translated once; referring to ρ(i) copies no derivation.
An arbitrary-depth intermediate formula is copied as a written tree,
not balanced or semantically normalized. Foreign variables are replaced
everywhere, including axiom argument records, by an existing gadget
occurrence. This verifies the exact old supplied-proof hypothesis rather
than silently replacing it by a proof in a stronger source system.

**Whole expanded-CNF induction.** Projection/composition from G→G
follows the actual conjunction edges to give G→C_F and G→U_s.
For each group, projection from A_b→A_b gives the two selected
leaves in each branch. The negative branch has A₀→¬z_i and
A₀→¬r_x; the positive branch has A₁→z_i and A₁→r_x. The two
same-branch templates give A_b→(z_i↔r_x). Cases receives exactly
G→(A₀∨A₁), followed by these two implications, and yields
E_G(z_i,r_x). For a singleton, both selected leaves coincide and
both projection paths have length zero; the same literal reception
is legal. Gadget groups stay in G and B even though no replacement
of their leaves is needed.

The entire expanded C_F and θF have identical connective skeletons:
their only differences are corresponding variable leaves. Maintain at
each paired node the proved endpoint E_G(A,A') for its two actual
subtrees. An occurrence leaf has the comparison just established;
an equal constant leaf has guarded reflexivity. At a negation node the
guarded-negation template consumes the earlier child comparison and
gives exactly E_G(¬A,¬A'). At an OR node, the congruence template
consumes the earlier left and right comparisons, in that order, and
gives E_G(A∨B,A'∨B'). This induction includes the negation of a
negative literal and every node of every expanded conjunction. In
particular a conjunction A∧B expands to ¬(¬A∨¬B); its two inner
negations, OR and outer negation are all paid induction steps. It is
not treated as a new primitive rule or left to a clause-width argument.
Repeated literals, opposite signs and arbitrarily deep original
conjunctions leave this correspondence unchanged.

At the root, guarded transport consumes exactly G→C_F and
E_G(C_F,θF), giving G→θF. The final D instance has successive
antecedents ¬θF and G→θF, both already present. Two applications
of the checked primitive reception end at precisely ¬G. No guard was
opened as an assumption and no deduction transformation is unpaid.
If the source has an empty clause, the separate D-tester failure
recurrence gives f=0 formally and the no-path output with distinct
endpoints is valid. Without an empty clause, an empty conjunction
cannot admit the assumed proof of its negation: every source axiom is
a classical tautology and MP preserves truth. No new exceptional-input
premise is required.

**Complemented endpoint and original product.** Simultaneous y↦¬y
on every receiving record preserves the exact axiom and all four
directed rule patterns, their bracketing and backward references. It
fixes the ground axioms, introduces no names and doubles no argument
tree; it adds one negation at each variable leaf. Thus the entire
result is a legal nonempty L108 archive, with T=(¬G)[¬y/y] as its
exact last tree and the original alphabet/B supplied separately.

The formal identity tr(P[¬y/y])=1+v(P) has atom value 1+y;
false and true give respectively 1 and 0. Its negation step adds 1,
and its OR step multiplies the child values in their displayed order:
(1+v(A))(1+v(B))=1+v(A∨B). The expanded conjunction therefore
gives ordered multiplication v(A)v(B). It follows that
tr(T)=v(G)=v(C)v(U)=f g̃, using L097's separate-order identifications.
The C identification is valid because each occurrence appears in one
clause, so its truth polynomial is increasing multilinear in D's order.
The E identification applies to ∏e_s in E's order. It is not applied
to g̃, which may repeat variables, or to the different-order product fg.

For clarity, the received correction has R_s=(1+z)W(A,z)B'+σ_zAB'
with z=z₁, A=∏_{i>1}(1+z_i) and B'=∏_{i>1}z_i. Its only
L035 arguments are original-only graphs. Substituting B gives
(1+z)(Az+zA)B'+(z²+z)AB'=(1+z)AzB'=a_sb_s;
the cancellation is between the adjacent (1+z)z and z²+z terms.
For a singleton A=B'=1, this is z²+z. Every R_s vanishes at zero
placeholders. The ordered prefix-t/suffix-e telescope for J hence gives
J(0)=0 and J(B)=g+g̃ without commuting a factor. L108 gives
K(0)=0 and K(B)=f g̃. Independent ordered graph composition yields
H=K+fJ, whose zero substitution vanishes and whose B substitution is
f g̃+fg+f g̃=fg. The exact occurrence names, signs, gadget and complete
dictionary are retained. Fresh exterior graph endpoints preclude extra
accepting paths; no quotient-ring equivalence is used.

**Independent original-Q accounting.** Fix Q before any transformation.
All source syntax occurrences, record counts, group counts and name
lengths are O(Q). Each source argument, actual subtree, branch guard
and G has O(Q) nodes after the nonduplicating abbreviation expansion.
Replacing names by θ can increase the full bits of such a tree to
O(Q²), but not its node count. The fixed intermediate library proofs
contain only a constant number of copies of their slot images, so this
bound applies to every record, not just a library endpoint. Curried
consequents and the five detachment records likewise contain boundedly
many copies. Congruence at a parent uses the actual child subtrees as
slots, never a recursively growing prior equivalence as a slot image.

The O(Q) source lines require O(Q) library/MP uses and O(Q³) formula
bits, retaining unused records and an O(Q)-entry endpoint map. There
are at most O(Q²) requested group/branch/projection paths, each of
length O(Q); thus O(Q³) uses safely cover them. The whole expanded
CNF traversal adds O(Q) nodes and boundedly many uses per node.
Since each use has a fixed number of records, each with O(Q²) bits,
the archive has O(Q³) records and O(Q⁵) formula bits. Its global
references add O(Q³ log(Q+2)) bits. The dictionary costs at most Q;
even retaining a copy at every call fits this archive bound. Whole
complementation changes only a constant node factor. This independently
establishes R₁≤cQ¹², with substantial slack.

L109's copying time is O(Q⁴) per O(Q²)-bit argument collection, hence
O(Q⁷) over all calls. An archive scan at each call costs at most
O(Q⁸); even less economical syntactic matching, provenance rebuilding,
name lookup and reference relocation fit the stated O(Q²⁰) allowance.
These check supplied explicit objects, not semantic validity of arbitrary
tautologies. Unbounded one-time fixed-library preparation is a compiler
constant, with no efficiency claim in a varying library size.

The received L108 bound gives |K|≤C R₁¹⁴≤C'Q¹⁶⁸ and time
O(Q^{12b}) for its fixed bit-time exponent b. The O(Q) correction
calls for J each receive O(Q²)-bit original-only graphs and the full
dictionary. L035's safe O(E⁴) output bound gives O(Q⁹) aggregate
block bits. Independent prefix/suffix/formula copies cost O(Q³);
global renumbering fits O(Q¹⁰) for J. Its received polynomial-time
algorithm and ordinary scans fit O(Q^{max(22,2d+3)}) for fixed d.
Final copying and reindexing of K, f and J add at most a logarithmic
factor. Thus |H|≤CQ¹⁷⁰ remains valid; quadratic processing of this
output and all preceding terms fit CQ^{max(340,12b,2d+3)}. Every
exponent and constant is fixed independently of the input. No bound
is measured in a transformed Q or in the sought witness itself.

**Verdict.** No substantive defect, changed hypothesis or changed bound
was found. This verifies a relevant conditional input informally; it is
reproduction of assessed machinery, not a new source theorem or certified
originality. Direct mathematical inputs remain L087/L097/L108/L109;
the superseded extractor, L049 and the old source-completeness appeal
are not premises. No DAG edge or main argument changes. No serialized
library, executable translator, finite program certificate or Mathlib
match is verified. L107/Attempt 036 remain valid for the old interface.
This supplies neither L106's blocked source proof nor short-proof
availability, an M-only bound, universal W₂, arbitrary ER data or an
unrestricted SAT decision/separation result.

## Mathlib

Full matching coverage for this occurrence transfer, corrected extraction,
explicit affine-ABP construction and complete binary/time bounds: **not
checked**. No theorem-absence or machine-verification claim follows.
The new section 6 four-rule compiler/composed bound is also **not
checked** against Mathlib. Supporting Boolean logic does not by itself
give a matching explicit compiler theorem. The precise primary results
and local component qualifications above are
the mathematical inputs; this is an informal specialization, with no
implementation or finite certificate experiment claimed.
