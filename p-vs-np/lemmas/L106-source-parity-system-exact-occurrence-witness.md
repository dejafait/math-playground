# L106 — Supplied source parity contradiction gives an exact occurrence witness

## Hypotheses

Work over F₂. Supply an explicit list of m equations

    Σ_{x in S_j} x = b_j,       j=1,…,m,

where each S_j is an ordered list of at most three distinct source
variable names and b_j is a bit. Rows may repeat. Supply m explicit bits
λ_j satisfying the finite, exactly checkable conditions

    for every occurring name x: Σ_{j:x in S_j} λ_j=0,
    Σ_j λ_j b_j=1.                                           (1)

No dense dimension inferred from a binary variable name is assumed.
Supply the exact canonical width-at-most-three CNF F for these rows:
in row order and then lexicographic assignment order, for each assignment
α to S_j with Σα≠b_j include the clause forbidding precisely α.
Its ith literal is x_i if α_i=0 and ¬x_i if α_i=1, in S_j's order.
Every actual disjunction tree and the actual global conjunction tree
are explicitly supplied and retained. An empty clause is false; an empty
global clause list is true. A consistent zero-arity row contributes no
clause, and an inconsistent zero-arity row contributes an empty clause.
The variable names, ordered rows, all clauses and λ, including unused
rows, are charged and checked against this exact F.

Supply L087's exact occurrence pair and full provenance for this F,
including its appended u/v gadget, original occurrence alphabet y,
ordered representatives f,g, and unchanged Boolean/commutator dictionary
B with placeholders σ_i,τ_ij. M is its full pre-witness input length in
L087/L098's model. Put, before constructing any proof or witness,

    Q=2+M+|F|+|system|+|λ|.                                  (2)

All records are explicit binary strings. Malformed inputs or a failure
of (1), the canonical-F comparison or the occurrence provenance are
rejected; the conclusion concerns inputs meeting these hypotheses.

## Conclusion

**Current replacement — step 442, 2026-10-24.** Section 6 constructs a
direct assumption-free proof π₄ of exactly ¬F in L108's four-rule
system, then composes the occurrence replay, guarded-CNF, extraction
and ordered-correction components separately. It does not apply L098's
whole old-proof theorem to π₄. In the original Q of (2), it gives

    |π₄| ≤ C Q¹²,             time_source ≤ C Q¹²,
    |H| ≤ C Q¹⁷⁰,             time_total ≤ C Q^max(340,12b,2d+3),

where b,d are fixed bit-time exponents of L108 and L035. The output
satisfies H(y,0)=0 and H(y,B(y))=fg with unchanged F, fg and B.
This is an abstract specialization/reproduction of the assessed
machinery. The independent step-444 audit in §7 finds no substantive
defect under the stated hypotheses. Fixed-library preparation is
unbounded; no serialized library or implementation is verified.

**Preserved old-interface qualification — step 422.** L107 proves that the retained
three-row fixture's exact ¬F has no proof in the specified serialized
three-scheme/MP/ground-constant interface. Thus the general exact-source
compiler asserted below cannot exist in that unchanged presentation;
this supersedes the earlier merely unresolved completeness qualification.
The historical proof/audit and successful zero-row streams are preserved.
Ordinary Frege in a separately justified complete presentation and
alternative affine-witness constructions are outside this obstruction.
That obstruction remains valid; the historical claim below is not the
proof of the replacement in §6.

**Superseded conclusion, preserved:** There is a deterministic construction of an assumption-free ordinary
Frege proof π of exactly ¬F in L097/L098's fixed Schoenfield ∨/¬/MP
presentation, including its ground axioms true and ¬false. No extension
or substitution inference rule occurs. One fixed polynomial in original
Q bounds its full binary size and construction time.

Applying audited L098 constructs an explicit acyclic affine-F₂ ABP H
using only y,σ,τ with the formal free-algebra identities

    H(y,0)=0,                    H(y,B(y))=fg.                (3)

The complete proof/witness export, independently copied dictionaries,
references and retained input records have polynomial full size and
deterministic bit time in the same original Q. Neither F, f, g, B nor M
is replaced or recomputed at an enlarged cutoff.

This reproduces known parity/Frege mechanisms with an exact-CNF and
local receiver specialization. The separate step-417 all-size informal
critical audit below finds no substantive defect; no implementation, verified proof
stream or certified originality is claimed. It supplies no general short
source proofs, M-only bound, universal W₂, arbitrary ER data or unrestricted
SAT decision/separation result.

## Proof

Sections 1–5 and their historical audits/implementation are preserved
with the step-422 qualification. The current proof is §6. It reuses the
balanced native construction, but replaces its unsupported source basis
and its invocation of L098's whole theorem.

**1. Precise imports and why a specialization is needed.** Reuse the
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-23-source-parity-system-occurrence-witness.md`,
whose COVERED_TARGET is this construction. Import the finite-field
equational/Frege correspondence and named **Reckhow basis-invariance
theorem** as stated in S. Buss, R. Impagliazzo, J. Krajíček, P. Pudlák,
A. A. Razborov and J. Sgall, *Proof Complexity in Algebraic Systems and
Bounded Depth Frege Systems with Modular Counting*, Computational
Complexity 6 (1996/97), 256–298,
[DOI](https://doi.org/10.1007/BF01294258), inspected
[37-page author manuscript](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/nullstellensatz/token.pdf),
§2.2, printed p.9 and symbol-size footnote; manuscript revision date
unestablished. The fixed-field equational rules have an ordinary-Frege
simulation, with written term/proof symbols charged. This is not an
EF/ER simulation or a semantic Gaussian-elimination oracle.

For fixed-language rule replacement use S. A. Cook and R. A. Reckhow,
*The Relative Efficiency of Propositional Proof Systems*, JSL 44(1)
(1979), 36–50,
[primary scan](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf),
Definitions 2.1–2.2, Theorem 2.3, Corollary 2.4 and Lemma 2.5 with
proof pp.39–40. Different-basis invariance is the separately named
Reckhow theorem, also stated in the first source, not Theorem 2.3 alone.
The original thesis proof was not inspected. We do not reprove either
general simulation. Below we specify just the finite additive schemas,
their balanced written terms, guarded reception and exact final formula
needed here. This also makes the symbol bound independent of a literal
expansion of an unbalanced parity chain.

The separate explicit-linear-system result in Impagliazzo–Segerlind,
*Constant-Depth Frege Systems with Counting Axioms Polynomially Simulate
Nullstellensatz Refutations*, arXiv:cs/0308012v1, §6, Theorem 4 pp.15–16,
uses counting axioms. It is a comparison, not an input removing those
axioms. L012's ER construction is likewise not a premise here.
L098, with its step-384 informal audit and L097's step-380 constant
repair, supplies precisely the final occurrence receiver. Its extraction
or graph theorem is not reproved.

**2. Exact row reception and constants.** Parse all inputs, check (1)
by toggling bits in a dictionary of the actually written names, rebuild
the bounded-arity forbidden-assignment clauses, and compare them with
every actual clause position and literal of F. Check its trees and the
given occurrence provenance as in L098. This neither finds λ nor tests
arbitrary F for unsatisfiability. All source and unused records remain
available in the retained input archive.

If F has an empty clause, actual-tree conjunction projections give
F→false. The fixed tautology (F→false)→¬F gives the required source
proof. Its constant case F=false is already the axiom ¬false. L098 then
returns its exact no-path zero witness, since the original tester f is
formally zero. No source equation or occurrence is changed. Henceforth
assume F has no empty clause; every zero-arity row then has b_j=0.

For every row define the four-leaf additive term

    R_j=(a_{j1}+a_{j2})+(a_{j3}+b_j),

where a_{ji} is its ith variable, or 0 if the list is shorter. Thus the
row equation is R_j=0. Let K_j be the conjunction of its actual clauses,
using any fixed bracketing of these at most four clauses; K_j=true when
there are no clauses. Each clause is false at exactly the assignment it
forbids. Consequently K_j is true exactly when Σ_{x in S_j}x=b_j,
and hence exactly when R_j=0. This verification is on at most three
schematic variables, not on all variables of the system.

There are finitely many arity/right-side and clause-tree shapes. For
each, fix once an ordinary-Frege proof of K_j→(R_j=0), with equality
translated as below. Standard propositional completeness supplies these
fixed proofs. Constants are implemented using L097's precise method:
replace true,false in a fixed tautology V by schematic t,d, prove the
constant-free tautology t→(¬d→V(t,d)), substitute the constants in the
entire fixed proof, and use the ground true and ¬false axioms. Thus the
templates have fixed size and contain no unexplained constant axiom.

Project every actual original clause from the actual F tree, by earlier
references to the parent projections. Combine the at most four projected
clauses of a row by fixed guarded conjunction templates to obtain F→K_j;
the empty row uses the fixed proof F→true. Compose with its fixed row
template. This produces F→(R_j=0) for every row, including λ-unused
ones, retaining their records. Neither global rebracketing nor replacing
F by a Boolean-equivalent source is involved. The equality notation
and the guard are ordinary formulas, not new inference rules.

**3. An explicit polynomial additive derivation.** Let r be the number
of selected rows λ_j=1. Condition (1) implies r≥1. Let t be the least
power of two at least r, so t<2(r+1). Form a complete balanced sum U of
t four-leaf blocks: the selected R_j in source order, followed by blocks
(0+0)+(0+0). It has

    N=4t≤8(r+1),              h=log₂N

leaf slots and height h. Combining the selected R_j=0 and zero-block
identities bottom-up by additive congruence and 0+0=0 gives U=0.
This is a derivation from the row equations, not an unconditional claim
about U.

Here is a concrete paid reordering procedure, using only associativity,
commutativity, additive identity, a+a=0, equality symmetry/transitivity
and one-level congruence. For a binary addition tree of height d and a
chosen leaf a, expose that occurrence as a+V. If it is in the right
child, first commute the children. Recursively expose it in the left
child; if that child is not already the leaf, replace (a+W)+C by
a+(W+C). If the left child is the leaf, nothing more is needed.
An induction on d shows that V has height at most d, all intermediate
trees have height at most d+1, and at most O(d) local rewrites are used.
For a singleton there is no remainder and no exposure operation is needed.
Rewrites below the root are implemented by one-level congruences along
the at most d+1 ancestors, not by an implicit context rule.

To swap two distinct leaf slots of the complete tree, expose a, then
expose b in its remainder. For N>2 this gives a+(b+V). Use

    a+(b+V) = (a+b)+V = (b+a)+V = b+(a+V),

then reverse the second and first exposure sequences with the two marked
leaf occurrences interchanged. For N=2 use commutativity directly.
The marking is positional bookkeeping for the constructor: no marked
letters or new variables occur in the exported proof. Other occurrences
of the same variable are untouched. Each reversed sequence is a valid
instance of the same identities with its actual leaf arguments. All
intermediate whole trees have exactly N leaves and height at most h+2;
there are O((h+1)²) one-level equational records per slot transposition.
This includes root lifting and equality transitivity. No variable or
subtree is duplicated in these additive rearrangements.

By (1), every variable occurs an even number of times in U, whereas the
number of constant-one leaves is odd. Since N is even, the number of
constant-zero leaves is odd as well. Arrange its leaf slots so that all
but one sibling pair consist of equal symbols, and the remaining sibling
pair is (1,0). Such an arrangement exists by pairing each variable's
occurrences, the remaining ones, and the remaining zeros. A deterministic
greedy position matching gives a permutation; at most N−1 arbitrary
slot transpositions implement it. Comparing the written names and
constructing these lists uses polynomial bit time.

Apply the explicit slot-swap procedure for that permutation. At the
bottom level use a+a=0 for each equal pair and 1+0=1 for the special
pair. The tree above them has just one leaf 1 and otherwise zero leaves.
Collapse its all-zero subtrees and use 0+A=A or A+0=A along the path of
that one leaf. This gives U=1 with O(N(h+1)) further one-level records
including all lifted equalities. Combine U=0 and U=1 to obtain 0=1
from the selected row equations. Every native term written anywhere
has O(N+1) nodes and depth at most h+2. The algorithm has specified each
rewrite and its earlier references; it does not certify parity by a
semantic solver, a new definition or an uncharged rearrangement.

**4. Actual ordinary-Frege strings and assumption discharge.** Spell out
the received additive part of the finite-field simulation on these
terms. Translate 0,1 as false,true, variables as themselves, and addition
as a fixed XOR formula, for example

    X(A,B)=(A∨B)∧¬(A∧B).

Expand ∧ as ¬(¬A∨¬B), and implication as ¬A∨B; these two expansions
duplicate neither argument. Write T(s) for the resulting ordinary
formula for an additive term s. Write E(A,B)=(A→B)∧(B→A), fully
expanded. The additive equation s=t is E(T(s),T(t)). This uses no
extension variables. Although X duplicates its arguments, if s has L
native nodes and depth d, its expanded formula has at most cL·2^d
nodes: each native occurrence is copied at most twice per addition
ancestor, with fixed connective overhead per copy. Our d≤log₂N+2 and
L=O(N+1) therefore give O((N+1)²) ordinary nodes per translated term.
In particular no left-associated long XOR is literally expanded.

Only finitely many additive axiom/congruence and equality templates are
used. Their Boolean translations are fixed classical tautologies on
their argument formulas. The imported finite-field/Frege correspondence
and Reckhow basis invariance allow their ordinary presentation; the
fixed-language Cook–Reckhow rule replacement supplies fixed proofs in
the L097 presentation. Equivalently select these finite template proofs
by the completeness/constant method in §2. This specifies the finite
part of the known simulation being received, rather than assuming a
new uniform simulation of a parity algorithm. Substituting the actual
written T(s) into a fixed proof copies each argument a fixed number of
times. Substitution is performed on the entire fixed proof before it is
appended; it is never a substitution inference on an earlier source line.

To discharge the row equations, guard every equational assertion by
the same exact original F. An axiom equality E(A,B) gives F→E(A,B)
by a fixed template. Transitivity, for example, uses the fixed tautology

    (F→E(A,B)) → ((F→E(B,C)) → (F→E(A,C))).

Additive congruence uses the fixed guarded version of

    E(A,B) → E(X(A,C),X(B,C)),

and its other-argument version; symmetry is similarly fixed. Thus each
native one-level step in §3 is compiled into a bounded number of fixed
proof instances and MPs with references to the already written guarded
premises. Section 2 provided exactly the initial F→E(T(R_j),false)
premises, assumption-free. Native zero-padding steps are axiom instances.
This process proves F→E(false,true). The fixed final tautology

    (F→E(false,true))→¬F

and MP give exactly ¬F with its original trees and names. No global
deduction transformation, extension axiom, inference substitution,
source-CNF replacement or proof-ancestry unfolding remains. The imported
basis theorems are not used to translate an uncontrolled XOR expansion;
the explicit shallow terms above already bound every actual argument.

The impossible edge cases are also explicit: λ=0 or m=0 cannot satisfy
(1); an empty original conjunction has only consistent zero-arity rows
and cannot satisfy (1). A selected-list contradiction without occurring
variables entails an actual inconsistent zero-arity row, handled in §2.
Units, unused zero rows, repeated rows and arbitrary right sides are
included. All distinct names are compared as complete strings, never
allocated according to a nominal numeric dimension.

**5. Full original-input ledger and L098 composition.** Each of the
source trees, row/name/λ records, occurrence records and largest input
name has length at most cQ. N≤cQ and h≤log₂(cQ). Source-tree projection
and row assembly need O(Q²) fixed proof instances even with separately
requested clause projections. The additive construction has O(N(h+1)²)
instances, plus its row assembly and equality-composition records;
allowing cQ⁴ instances covers all of them, native administrative records
and constant cases. Unused row proofs and all original records are
retained, not erased to improve this count.

Each actual template argument has O(Q²) ordinary formula nodes, including
the exact guard F as an opaque argument. A fixed proof has a bounded
number of lines and a fixed number of copies of each argument per line.
With O(Q)-bit input names, a fully written proof line, its explicit
axiom-instantiation data and references cost at most cQ³ bits after
enlarging the constant. Global reference numbers have O(log(Q+2)) bits
because the record count is polynomial; they name earlier records rather
than copying derivations. Original dictionaries, original trees, source
associations, native worksheets if retained, and the final proof framing
fit this ledger. A conservative full bound is

    |π|≤c₀Q¹²,             time_source≤c₁Q¹².               (4)

For time in (4), bit-dictionary coefficient checks, bounded row-CNF and
tester/provenance reconstruction are polynomial explicit scans; names
and clause positions are paid by Q. Greedy slot matching uses O(Q²)
name comparisons of O(Q) bits. Streaming fixed-template instantiation
and reference relocation use time linear in the written records, up to
polynomial scans of the input name/location tables. Even quadratic scans
within each O(Q³)-bit instantiated record and O(Q⁴) instances fit Q¹⁰;
Q¹² covers parsing, checking, all copying and the direct empty-clause
case. No unbounded search for a fixed template proof is done at runtime:
the finite proofs are fixed once as part of the construction.

Now and only now apply L098 to the exact π and the unchanged pair. Its
own input parameter is

    R=2+M+|F|+|π| ≤ c₂Q¹².                                  (5)

Its audited size bound is cR¹⁶⁸. Its deterministic time bound is
cR^[12 max(30,2d+2)], where d≥6 is the fixed exponent for its received
L035/L036 constructors. Consequently this specialization has

    |H|≤c₃Q²⁰¹⁶,
    time_total≤c₄Q^[144 max(30,2d+2)].                        (6)

Constants are fixed independently of the source, system, λ and pair.
The original inputs and π can also be exported alongside H within these
bounds. L098 charges every independent graph copy, unchanged complete
B/placeholder dictionary, nested record, name and final global reference.
Those are its actual input R costs, composed in (5) before (6); M is
never redefined using an output. Its conclusion is exactly (3), not a
different source polynomial or a Boolean-equivalent product. The direct
empty-clause witness fits the same bounds. Actual path degree is at most
the finite output edge count; no witness degree was an input parameter.

Equations (4)–(6) meet the sought one-fixed-polynomial threshold in the
full supplied data. This is local conditional supplier progress using
known machinery, not progress beyond the checked source theorems. The
separate critical audit below checks this all-size assembly and its
ledger. General source proof availability, a bound in M alone, universal
W₂, arbitrary ER data and unrestricted SAT remain unresolved.

**Independent critical audit — 2026-10-23, step 417.** Receive the
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-23-parity-system-supplier-critical-audit.md`,
whose exact TARGET and COVERED_TARGET match this audit. Reuse the primary
passages cited in §1; no new theorem or general simulation is proved.
L106 is the object being checked. The received mathematical inputs are
L087's exact occurrence pair/provenance and L098's step-384 audited
interface, including L097's repaired ground-constant seeds.

1. **Actual source and row reception.** Each nonempty row has at most
   four forbidden assignments, each clause has at most three literals,
   and their clause-tree shapes form a finite collection. A clause
   forbidding α is false precisely at α, so their conjunction is
   equivalent to the stated parity row, including both right sides and
   each ordering of the distinct schematic variables. This checks the
   bounded template, rather than asserting a short proof from a semantic
   solver. Repeated rows receive separate projections at their actual
   clause positions. Begin projection with the fixed reflexivity proof
   F→F. From a proved F→(A∧B), fixed curried templates and MP give
   F→A and F→B. Thus any actual global conjunction depth is admitted;
   projecting a unit clause needs no artificial binary node. A fixed
   number of guarded conjunction steps forms each K_j, preserving the
   original F as guard and the original clause trees as arguments.

   For arity zero and b=0, K_j=true and R_j is the four-zero term; the
   row template remains valid. For arity zero and b=1, the actual source
   contains an empty clause. Projecting it gives F→false and hence
   exactly ¬F, also when F itself is false. L098's separate empty-clause
   reception returns the no-path graph with distinct endpoints and all
   dictionaries, because the actual D-root is the absorbing failure
   state and its formal f is zero. No algebraic identity is inferred
   solely from Boolean vanishing. An empty global clause list or an
   all-zero λ cannot satisfy (1). Unused consistent zero rows and
   repeated rows remain charged and are not silently deleted.

2. **Exposure invariant and reversal.** Check the claimed exposure
   algorithm on an arbitrary, possibly incomplete, binary tree, not
   merely on the original complete tree. At height d≥1, after a possible
   root commute, its marked leaf lies in a left child of height at most
   d−1. If that child is the leaf, its right sibling is the required
   remainder. Otherwise recursive exposure gives that child as a+W
   with height(W)≤d−1; all intermediate left children have height at
   most d. Within the original root they therefore have height at most
   d+1. The final rotation (a+W)+C → a+(W+C) leaves remainder W+C
   of height at most d, since height(C)≤d−1. The final whole height is
   at most d+1. The recurrence for elementary local rewrites is
   e(d)≤e(d−1)+2, so e(d)=O(d). Leaves are neither duplicated nor lost.

   Apply this at d=h to the original complete tree. Its final remainder
   has height at most h. Exposing the second marked leaf inside that
   remainder has intermediate height at most h+1 there, and hence at
   most h+2 in the whole tree. For N>2 the remainder after this second
   exposure is nonempty. The middle three rewrites through
   (a+b)+V, (b+a)+V and b+(a+V) also have height at most h+2.
   Reverse the second and first exposure histories, exchanging only the
   two marked leaf occurrences. Each recorded associativity or
   commutativity step remains a valid instance after this exchange.
   All exchanged objects are leaves of height zero, so every reversed
   tree has exactly its forward counterpart's shape and height. The
   endpoint is the original complete shape with just those positions
   exchanged; other occurrences, even identically named ones, are fixed.
   For N=2 the direct commute suffices; admitted U actually has N≥4.

   Each elementary rewrite is first an equality of local subterms.
   Lift it through its current ancestors by one-level congruence,
   using at most h+2 lifts, and chain successive root equalities by
   transitivity. There are O(h+1) elementary rewrites per swap, giving
   O((h+1)²) records including lifts and chaining. Neither a recursive
   proof substitution nor an uncharged context rule is needed. After
   each complete swap the shape is again complete, so depth bounds do
   not accumulate over the at most N−1 swaps.

3. **Cancellation and the guarded endpoint.** Condition (1) makes
   every variable multiplicity even and the multiplicity of 1 odd.
   Since N is even, the multiplicity of 0 is odd as well. Remove one
   occurrence each of 1 and 0; every remaining symbol multiplicity is
   even. Pairing those occurrences provides precisely the claimed
   sibling arrangement. Replacing equal sibling pairs by zero and the
   special (1,0) pair by one only decreases term size and depth.
   All-zero subtree collapses and the remaining identity rewrites keep
   that property. The chain therefore proves the original U equal to
   one, with O(N(h+1)) further records after ancestor lifts. In the
   separate row derivation, combine child equalities to zero bottom-up;
   one fixed two-premise congruence/zero template per internal sum node
   suffices. It proves that same U equal to zero, under the same F.
   Guarded symmetry and transitivity give F→E(false,true).

   In every guarded inference, actual subformulas are template arguments;
   their previously written proof derivations are not inserted as
   arguments. For example guarded one-level congruence is the fixed
   tautology (F→E(A,B))→(F→E(X(A,C),X(B,C))), with its symmetric
   argument version. The quoted transitivity template uses two earlier
   guarded premises, with two MPs. Row templates are composed under F
   in exactly the same way. The fixed final constant-containing
   implication then gives precisely ¬F, with its actual trees intact.
   The §2 constant-template method is valid: the curried formula with
   schematic t,d is tautological because t=true and d=false are its
   only case with both premises true. Substitute those constants in
   its entire fixed proof, then apply true and ¬false. Any auxiliary
   variables in a chosen finite proof can first be replaced throughout
   by an existing schematic argument or t; fixed proof length remains
   fixed. No new constant axiom or inference substitution is admitted.

4. **All written formulas and the original-Q ledger.** A native node
   below k addition ancestors has at most 2^k copies in the expansion:
   the chosen XOR copies each argument twice, while expanding ∧ and
   → copies each argument once. Summing the fixed local connective
   overhead over native nodes gives cL·2^d. Every actual subterm in
   the exposure, reversal, cancellation and row derivations has
   L=O(N+1), d≤h+2, hence O((N+1)²) ordinary formula nodes.
   Equality, guard and finite template expansions add fixed factors.
   Partial lifted equalities use subtrees of the same bounded whole
   terms; they introduce no deeper native context. The exact F is
   copied as a formula argument of size O(Q), irrespective of its depth.

   At most O(Q²) source projection/row instances and
   O(N(h+1)²) additive instances fit the cQ⁴ allowance. Each fixed
   template contributes a bounded number of lines, each with O(Q²)
   nodes and O(Q)-bit names, so explicit formulas, instantiation data
   and references cost O(Q³) bits per line. The number of records is
   polynomial, making reference fields O(log(Q+2)). Thus the direct
   source ledger is already O(Q⁷) bits; the stated Q¹² bound has slack
   for all retained worksheets and framing. Parsing actual name lists,
   toggling coefficients, bounded row reconstruction and comparing the
   supplied explicit occurrence/provenance data need only bounded
   polynomial scans. Reconstructing the O(Q) tester states and O(Q²)
   axiom entries with O(Q)-bit names also fits this allowance.
   Greedy slot matching costs O(Q³) bit operations as stated.
   Even quadratic processing of each O(Q³)-bit instantiated record
   over O(Q⁴) instances costs O(Q¹⁰); generation and reference
   relocation therefore fit time_source≤cQ¹². Fixed template proofs
   are constants of the constructor, with no runtime proof search.

   L098 receives exactly the required width-three F, assumption-free
   ordinary proof π ending ¬F, and unchanged occurrence pair/provenance.
   Its intermediate-formula interface permits all depths used here.
   Put R=2+M+|F|+|π| only after charging π: R≤cQ¹².
   Its received bounds cR¹⁶⁸ and cR^[12 max(30,2d+2)] give exactly
   Q²⁰¹⁶ and Q^[144 max(30,2d+2)], respectively. The source proof
   and original records fit both exports. Each received complete
   dictionary and independent graph copy is already charged in R;
   neither M nor Q includes a sought witness. The resulting identities
   remain H(y,0)=0 and H(y,B(y))=fg in the original free algebra.

The audit finds no substantive defect requiring a change to the
construction, identities, exponents or direct mathematical inputs.
This supplies a checked local informal specialization of known machinery,
not progress beyond the inspected source mechanisms, a verified
implementation or a P-versus-NP candidate. No finite proof stream was
generated or checked. The absence of general short source proofs,
M-only bounds, universal W₂ and arbitrary ER data remains unresolved.

**Bounded implementation attempt — 2026-10-23, step 419.** Under the
saved SPECIALIZE assessment
`drafts/literature/2026-10-23-parity-source-proof-compiler.md`,
`scripts/parity-source/attempt.py` reuses L056's implication/negation
synthesis tactic, leaving its files unchanged, and exports to the
separate exact-basis `scripts/parity-source/checker.py`. The latter
imports no emitter code and permits only the three specified source
schemes, MP, true and ¬false. It reparses every formula, declared
substitution and earlier reference, and reconstructs each requested
endpoint independently from the retained canonical row input and actual
global tree. These bounded outputs are reproductions of finite logical
operations, not a verification of §§2–5 for arbitrary inputs.

The fixed ax-3 replacement is paid explicitly. For schematic A,B, put
h=(¬A→¬B). Under h and B, ax-1 gives ¬A→B; the source second scheme
and two MPs give A. Discharging B and h by the ax-1/ax-2 deduction
construction gives h→(B→A), with all deduction steps materialized.
The complete 43-record source library is
`scripts/parity-source/output/replacement-library.jsonl` (6,264 bytes).
This reproof is necessary only to supply concrete executable records
in the specified basis rather than accepting L056's different ax-3 as
a primitive. A fixed two-variable proof of
¬d→¬(A∧d), with ∧ literally expanded, is also fully materialized and
independently checked in `zero-projection-library.jsonl` (1,869 records,
482,386 bytes). No truth-table proof on the growing parity instance is
attempted.

The complete direct inconsistent-zero-row and unused-zero-row exports
each have 1,876 records, 483,009 bytes (3,864,072 bits), and endpoint
exactly ¬false. A source containing the unused consistent row x=0,
then 0=1 and an unused 0=0 row, has actual F=(¬x∧false); its complete
1,996-record export is 536,998 bytes (4,295,984 bits) and ends at exactly
¬(¬x∧false). Each original row/λ/tree record is retained separately.
Every generated assumption-free primitive record is exported, including
unused template records; assumption-dependent synthesis scratch is never
asserted in the stream. Global relocation and an explicit last MP preserve
earlier references. Nine complete altered streams reject: altered axiom,
forward and out-of-range references, wrong MP, ground-constant misuse,
header and last endpoints, unapproved old ax-3 and assumption rule.
Full statistics, names, substitutions, references, retention counts,
hashes and rejection reasons are in `scripts/parity-source/output/report.json`;
every original/corrupt stream is retained, uncompressed.

The three-row fixture **does not receive a proof**. The literal source
clauses include x∨¬y, y∨¬z and x∨z. Decoding only syntactic ¬A∨B as
an implication leaves those positive-left OR nodes opaque. The component's
decoded requested ¬F fails its tautology test at x=y=z=false with all
three opaque tokens true. The first exact row template using §4's
displayed X and E also fails that component's reception test; its full
formula, token map and countervaluation are retained in
`scripts/parity-source/output/failed-row-template.json`. Neither failed
formula is passed to the primitive checker as an axiom. No partial
parity stream, semantic rewrite or normalized replacement endpoint is
reported as a proof.

This is a concrete limitation of the implemented implication-only
receiver, **not a proved nonderivability theorem**. In particular a
failed synthesis diagnostic alone cannot invalidate every exact-basis
construction. It exposes an unreviewed hypothesis in the use of ordinary
completeness/basis invariance for a presentation whose arrows are literal
abbreviations inside a primitive OR syntax. The step-417 completeness
check in item 3 above therefore requires a separate primary-source
convention review before the general exact-OR source reception is relied
on. That review must distinguish unrestricted primitive OR, an
implication-generated fragment, and any additional connective rules;
no such rule has been added here. The all-size argument and L097/L098
interfaces are preserved with this unresolved qualification.

No actual L087 pair/provenance or H was constructed. Thus original M/Q
integration and the measured cQ^12 requirement are explicitly UNVERIFIED;
source-only bytes are not labeled Q, no constant is fitted to these
fixtures, and finite checking supplies no all-size size/time theorem.
The main SAT gap is unchanged. Reproduction command:
`python3 scripts/parity-source/attempt.py`.

### 6. Direct four-rule replacement — step 442, 2026-10-24

**6.1 Scope, imports and exact notation.** The prior SPECIALIZE assessment
is `drafts/literature/2026-10-23-direct-four-rule-parity-source-repair.md`;
its exact TARGET covers this construction, its changed receiver and the
original-Q ledger. This is a mathematical attempt under that saved
coverage, not a new approval of uncovered mathematics. L107 and Attempt
036 rule out the old interface, not the following four-rule construction.

Use L109, including its step-432 audit, for preparation/instantiation of
a fixed finite Boolean-valid library. Its precise primary input is
Joseph R. Shoenfield, *Mathematical Logic* (Addison-Wesley, 1967),
§2.6 pp.21–22 and §3.1, Tautology Theorem (Post) p.27, Detachment
p.28 and propositional proof cases pp.28–30,
[primary scan](https://w2.cs.uni-saarland.de/op/fullpaper/logics/SHOENFIELD_Mathematical_logic.pdf).
We import that consequence theorem through L109, rather than reprove
completeness or claim short proofs for growing tautologies. The
Buss-et-al./Cook–Reckhow passages in §1 remain the assessed comparison;
no general basis conversion is required here.

All produced records use exactly L108's axioms ¬A∨A, true, ¬false,
and its expansion, contraction, directed association and cut. Expand
A→B as ¬A∨B, A∧B as ¬(¬A∨¬B),
E(A,B) as (A→B)∧(B→A), and X(A,B) as (A∨B)∧¬(A∧B),
recursively and literally. Chains of implications associate right.
Set E_G(A,B)=G→E(A,B). These notations specify ordered formula trees,
not additional connectives or inference tags. The guard G is a slot
in the library and later exactly F or the occurrence formula specified
below.

Use L097 §§6.1–6.3 for its already Boolean-checked fixed library and
actual-tree operations, and §6.2 for actual premise reception. In
particular, from earlier A and ¬A∨B append B∨A by expansion,
¬B∨B by axiom, A∨B by cut with pivot B, B∨B by cut with pivot A,
and B by contraction. Thus every displayed use of detachment below
means these five primitive records with the actual earlier indices.
The first cut has residuals A,B, and the second B,B; literal directed
matching holds. Curried theorems receive their antecedents in order.
No proof ancestry or assumed premise is inserted into a formula slot.

**6.2 The finite additional library and its Boolean verification.**
Adjoin the following schemata to L097 §6.1's library. Every slash choice
is a separate fixed member, with its own fully expanded tree.

| Family | Schema |
| --- | --- |
| Guard introduction | A→(G→A) |
| Guarded conjunction/true | (G→A)→((G→B)→(G→(A∧B))); G→true |
| XOR commutation | E(X(A,B),X(B,A)) |
| XOR association | E(X(X(A,B),C),X(A,X(B,C))) |
| XOR zero | E(X(A,false),A); E(X(false,A),A) |
| XOR cancellation | E(X(A,A),false) |
| Guarded transitivity | E_G(A,B)→(E_G(B,C)→E_G(A,C)) |
| Guarded XOR congruence | E_G(A,B)→E_G(X(A,C),X(B,C)); E_G(A,B)→E_G(X(C,A),X(C,B)) |
| Guarded zero sum | E_G(A,false)→(E_G(B,false)→E_G(X(A,B),false)) |
| Inconsistent equality discharge | (G→E(false,true))→¬G |
| Refutation transport | ¬A→((G→A)→¬G) |

Also adjoin the finite row family K→E(T(R),false): take each
a=0,1,2,3, b=0,1, the ordered distinct slots x₁,…,x_a, all actual
binary disjunction shapes on each canonical forbidden-assignment
clause, and a fixed right-associated conjunction K of those clauses
(a single clause is itself, an empty list is true). Here
R=(a₁+a₂)+(a₃+b), with missing slots zero, and T uses X for +.
There are at most four clauses of at most three literals each, so this
specifies finitely many fixed trees independently of the receiving input.
No actual global F tree or growing parity term belongs to the library.

Here is the complete Boolean check for this addition. Literal X has
value a+b modulo two: it is true exactly on (a,b)=(0,1),(1,0).
E has value one exactly when its two bits agree. Consequently XOR
commutation and association are respectively a+b=b+a and
(a+b)+c=a+(b+c) in the two-element group, zero is its identity and
a+a=0 for both possible a. These checks include a=0 and a=1 and
exhaust all arguments; in particular E(X(true,false),true) is the
zero-law instance A=true, not a new template. If G=0, every E_G and
G→H in these schemata is true. If G=1, transitivity is transitivity
of equality of bits, either congruence preserves equality under the
fixed XOR function, and zero sum adds two zero bits. Guarded
conjunction asserts that two true bits have true conjunction, while
G→true and guard introduction follow directly from implication's
truth table. E(false,true) is false, so its discharge has a true
antecedent only when G=0. For refutation transport, ¬A true forces
A=0; a true G→A then forces G=0. Finally a canonical clause is
false exactly on its forbidden assignment. Therefore K=1 precisely
when Σx_i=b, which is precisely when T(R)=Σx_i+b=0. This covers
all at most eight assignments per row, both b, every clause shape,
the consistent zero row (K=true,R=0) and the inconsistent zero row
(K=false,R=1). Thus every row implication is a tautology. Constants,
equal slot images and arbitrary formula depth do not affect any check.
The reused L097 members have their full checks in §§6.1/7 there.

L109 now selects one whole primitive proof δ for each member of this
single finite union library. All proof lengths and all slot occurrences
in their intermediate and unused records are compiler constants. A
possible preparation by terminating enumeration has no asserted
polynomial bound; it is done once, independently of Q. Runtime calls
write these whole fixed proofs after literal slot instantiation and
internal-reference relocation. L109 eliminates all auxiliary atoms,
so each produced variable comes from an actual argument. This is the
necessary specialization, not a reproof of the source completeness
theorem or a claim to have serialized the selected proofs.

**6.3 Exact source proof π₄.** Check all hypotheses of this lemma before
construction: actual row names/arity, λ bit conditions, canonical F
including row/assignment/literal order and actual trees, and the L087
occurrence provenance. Retain all records, including λ-zero and
zero-arity rows and unused dictionaries. Parsing uses actual names,
not a dimension inferred from their numerical spelling.

If F contains false as an empty clause, begin at F→F (the Identity
member of L097's library) and project down the actual conjunction
path, using projection and guarded composition, to F→false. Final
discharge gives exactly ¬F. This is also valid when F=false and the
path has length zero. The remaining construction concerns no-empty-
clause inputs; every zero-arity row then has b=0.

For every row project each of its actual clauses from the actual F
tree by that same procedure. Use the guarded conjunction member to
assemble F→K_j in the fixed row conjunction shape. An empty row uses
F→true. The matching row library proof and guarded composition give
exactly E_F(T(R_j),false). Generate these for unused rows too. All are
assumption-free earlier endpoints, and F's global tree is never changed.

Now implement §3's native balanced additive construction. Its non-basis
proof, including step 417 items 2–3, can be reused independently of the
stopped source presentation. For clarity its discriminating invariants
are supplied here. Let r≥1 selected rows, t the least power of two
≥r, N=4t≤8(r+1), h=log₂N. The initial U is a complete tree with
the selected four-leaf R_j blocks followed by four-zero blocks. Combine
their E_F(T(R_j),false) endpoints and padded zero identities bottom-up
using Guarded zero sum to obtain E_F(T(U),false).

For a singleton there is no remainder and exposure uses no step. For
a leaf in a possibly incomplete height-d tree with d≥1, commute at the root
if necessary, expose the leaf recursively in the left child, and rotate
(a+W)+C to a+(W+C). If the left child is already that leaf, stop.
The final remainder has height ≤d; every intermediate whole tree has
height ≤d+1, and at most O(d) local rewrites occur: induction applies
at left-child height ≤d−1, and the new remainder W+C has both child
heights ≤d−1. To exchange two slots in the complete tree, expose a,
then b in its remainder, obtaining a+(b+V). For N>2 change this through
(a+b)+V, (b+a)+V, b+(a+V), then reverse both exposure histories with
only the two marked leaves exchanged. Reversal preserves each identity
and tree shape because the exchanged objects have height zero. N=2
would use direct commute; here N≥4. Every whole term in a swap has
N leaves and height ≤h+2, and the endpoint is again the complete
shape. Lift each local equality through its actual ancestors by the
two guarded one-argument XOR congruences, and chain root equalities
with guarded transitivity. This costs O((h+1)²) library uses per swap,
not a context rule. A reversed identity uses guarded symmetry from
L097's library. Thus depth does not accumulate over successive swaps.

The λ conditions make every variable multiplicity in U even and its
number of ones odd. Its even N makes the number of zeros odd too.
After reserving one 1 and one 0, pair all remaining identical symbols.
Greedy positional matching arranges these pairs as siblings and the
reserved pair as (1,0), using at most N−1 arbitrary slot transpositions.
Names are compared as full strings. Apply the preceding swaps. Cancel
equal bottom siblings to zero and the special pair to one using the
fixed cancellation/zero laws. Collapse all-zero subtrees and the zeros
along the surviving-one path. Lifting and transitivity cost at most
O(N(h+1)) further uses; terms only shrink. This yields E_F(T(U),true).
Guarded symmetry on the U=0 endpoint followed by transitivity yields
E_F(false,true). Its discharge produces exactly ¬F.

Every local additive identity is first an unguarded fixed-library
instance and then guarded by Guard introduction with G=F. Row endpoints
are guarded from their construction. Every equality lift, combination
and discharge uses its actual earlier endpoints, with five primitive
records for each detachment as in §6.1. Native terms and position marks
are constructor worksheets, never propositional extension variables
or proof rules. The result π₄ is thus an actual finite assumption-free
four-rule record sequence ending at the exact ¬F, not merely a semantic
refutation or an instruction to prove a growing tautology. Every unused
instantiated library line is retained. Conditions (1) exclude λ=0,
m=0 and empty global F. Selected rows with no occurring variables and
odd total b force an inconsistent zero row, already handled above.

**6.4 Direct occurrence replay and receiver components.** Do not invoke
L098's whole theorem: its required supplied old-presentation proof is
not π₄. Instead receive these matching components explicitly.

For an empty original clause, L097 §1 identifies f=0 formally by D's
absorbing failure state and suffix recurrence. Export the source π₄
if desired and return a no-path ABP with distinct endpoints, retaining
all original dictionaries and records. Both requested identities hold.
Assume henceforth that F has no empty clause.

Use L087/L097's C_F,C_gad,C=C_F∧C_gad,U and G=C∧U, with original
occurrence/group order. C_F retains F's actual expanded tree. For each
source x in F let r_x be its first occurrence. Define θ(x)=r_x; any
other source name, if present in retained data, maps to the existing
gadget occurrence y₁. Constants are fixed. Apply θ simultaneously
to **every** record of π₄, not just its endpoint. At ¬A∨A its image
is exactly ¬θA∨θA. Ground axioms stay fixed. Expansion, contraction,
association and cut become those same exact rule instances on their
argument images. Their earlier references remain earlier even if
formulas or names collapse. A linear pass therefore gives a primitive
occurrence-only archive ending exactly at ¬θF. No old-source axiom/MP
converter is used; this is the literal replay justified by L109 §§2–3.

Append the whole-CNF component of L098 §6.3, using the fixed L097
library already included here. In detail, projections from G→G give
G→C_F and each G→U_s. In group s, U_s=A₀∨A₁ consists of actual
all-zero/all-one conjunctions. Actual-tree branch projections give
A₀→¬z_i, A₀→¬r_x, A₁→z_i, A₁→r_x. The same-negative and
same-positive members, followed by Cases, give E_G(z_i,r_x).
Singleton groups have empty projection paths; the same records remain
valid with coincident leaves. Gadget groups remain in G and B.

Traverse the entire expanded pair C_F,θF. At a variable use that
occurrence equivalence, at constants guarded reflexivity, at negation
guarded negation, and at OR guarded OR congruence on its two actual
children. All expanded conjunction nodes are included. This proves
E_G(C_F,θF), retaining arbitrary global conjunction depth. Transport
from G→C_F gives G→θF. Refutation transport receives first the
earlier ¬θF and then this implication, giving exactly ¬G. The
component's premises are precisely those now present; it never requires
the old-presentation source proof. Endpoint use is by earlier index;
no source/child derivation is unfolded or substituted as an argument.

Complement y_i↦¬y_i simultaneously in this *whole* occurrence archive,
fixing constants, to get Π ending at T=(¬G)[¬y/y]. The replay just
checked applies also to arbitrary formula images, so all primitive
tags and backward references remain valid. This is proof copying,
not a substitution-inference tag and not a substitution in B or fg.

Receive L097 §§1–2/6.5 and L098 §6.4's audited components. Their exact
definitions give v(C)=f, v(U)=g̃ and an ordered correction J with
J(y,0)=0 and J(y,B)=g+g̃, including singleton groups. The needed
endpoint calculation is tr(P[¬y/y])=1+v(P): constants give 1=1+0
and 0=1+1, an atom gives tr(¬y)=1+y, negation adds 1, and OR gives
(1+v(A))(1+v(B))=1+v(A∨B) in that order. Literal conjunction
expansion preserves the identity. Consequently tr(T)=v(G)=f g̃.

Π is nonempty, assumption-free, acyclic, over only original occurrence
names/constants, and has exactly L108's syntax/tags. Its input is the
original alphabet and full unchanged B, including unused entries.
L108 yields K with K(y,0)=0, K(y,B)=f g̃. With independent copies,
fresh exterior endpoints and ordered series/parallel connectors form
H=K+fJ. Then H(y,0)=0 and

    H(y,B)=f g̃+f(g+g̃)=fg.

Only identical ordered products cancel. No claim that g=g̃, no
Boolean-only identification of fg, no single-order injectivity on fg,
and no changed occurrence or dictionary is used. Original-only formula
graphs and J's correction operands are precisely L097's audited ones;
all labels remain affine. We import their identities instead of reprove
the ordered correction or the extractor.

**6.5 Fresh original-Q ledger.** Constants in the following estimates
depend only on the fixed encoding, prepared finite library and received
algorithms, before any input is chosen. Input counts, occurring names,
individual name lengths and original dictionaries are O(Q); N=O(Q).
Every native term has O(N+1) nodes and depth ≤h+2. In its literal XOR
image, a native occurrence below k additive ancestors is copied at
most 2^k times. Thus T(s) has at most c|s|2^depth(s)=O(Q²) nodes.
This applies also to subterms in lifted equalities. Fixed equality/
guard/template expansions add constant factors, and the actual F has
O(Q) nodes irrespective of its depth. No previous equality proof or
expanded guard is nested into a new argument recursively.

Actual source projection/row assembly uses O(Q²) library calls.
There are O(N(h+1)²) additive calls and O(N(h+1)) cancellations,
including ancestor lifts and equality chaining. A loose O(Q⁴) bound
therefore covers all calls/primitive records, padding, unused row
proofs and the empty-clause branch. A whole fixed library proof has a
fixed number of records and slot occurrences. Each output line and
its explicit arguments, if retained, has O(Q²) nodes, at most O(Q)
bits per name, and hence O(Q³) full bits. Global indices cost
O(log(Q+2)) bits. The source archive and its worksheets/indices thus
fit O(Q⁷) full bits, and conservatively |π₄|≤C Q¹².

For source time, checking names, λ, bounded canonical clauses and the
explicit pair/provenance uses polynomial syntactic scans: at most
O(Q²) source coefficient/name comparisons of O(Q) bits suffice;
reconstructing the explicitly charged tester and O(Q²) dictionary
entries likewise fits the allowance. Greedy slot matching uses at
most O(Q²) O(Q)-bit comparisons. Native history generation is bounded
by the preceding record count. L109 takes quadratic bit time in each
O(Q³)-bit argument package; O(Q⁴) calls therefore cost O(Q¹⁰).
Even scanning the accumulated O(Q⁷)-bit source archive at every such
call costs O(Q¹¹); retained input/framing and reference relocation fit
time_source≤C Q¹². No template search is included at runtime.

In the direct θ replay each source line still has O(Q²) nodes and
each replacement occurrence name has O(Q) bits. There are O(Q⁴)
records, hence O(Q⁷) replay bits, rather than the O(Q³) source-part
estimate for L098's different input. This new count is essential.
The source-to-replay index map has O(Q⁴) entries. The guarded receiver
adds at most O(Q³) calls/records: each requested group projection has
length O(Q), there are at most O(Q²) requests, and the expanded-CNF
traversal has O(Q) nodes. Each call's G and actual subtrees have O(Q)
nodes and O(Q²) bits; their whole added archive costs O(Q⁵) bits.
No growing proved formula is used as a context argument. Complementing
every record adds only a constant node factor, retaining all names.
Even keeping both versions, π₄, inputs, maps and full dictionaries gives

    R₁=2+|Π|+|occurrence alphabet|+|B/dictionary| ≤ C Q¹².

This bound is established for the direct archive, not obtained by
applying L098 to an inadmissible proof. Full syntactic replay, explicit
reference-table scans and relocation, repeated O(Q⁷)-bit archive scans,
retention and complementation all fit a loose preprocessing allowance
O(Q²⁰). No semantic UNSAT test, ancestry copying or new-name dimension
allocation is performed.

L108 gives |K|≤C R₁¹⁴≤C'Q¹⁶⁸ and time ≤C R₁^b for a fixed
bit-time exponent b. For the pair-only J, L097's audited ledger applies
with original pair data ≤Q: at most O(Q) L035 calls have full inputs
O(Q²), including the unchanged B. The safe O(E⁴) correction-size
bound gives O(Q⁹) aggregate block bits. Independently copied original-
only prefix/suffix/formula contexts cost O(Q³); full numbering and
dictionaries fit O(Q¹⁰). For fixed L035 bit-time exponent d, the
received safe time bound is O(Q^max(22,2d+3)). No output witness is
fed back as an L035 input.

Disjoint final copies, connectors, dictionary associations and global
renumbering add at most a logarithmic size factor; even a quadratic
scan of the fully written output suffices for bit construction.
Consequently, including retained π₄ and original input records,

    |H| ≤ C Q¹⁷⁰,
    time_total ≤ C Q^max(340,12b,2d+3).

The actual path degree is at most the explicit output edge count.
All estimates use Q=2+M+|F|+|system|+|λ| fixed before output;
neither M nor any logarithmic cutoff is enlarged or recomputed.
The bounds meet the required fixed-polynomial threshold, without
effective estimates on the fixed library constants.

This repairs the conditional abstract supplier by a different rule
interface and explicit component composition. A separate critical
audit of this new assembly/ledger is still required. It does not repair
the old serialized compiler or its retained streams, exhibit a verified
library/program, certify originality, establish arbitrary-CNF short
proofs, an M-only bound, universal W₂, arbitrary ER data or SAT
decision/separation. No main-problem candidate is claimed.

### 7. Independent critical audit — step 444, 2026-10-24

This audits the original Hypotheses and the step-442 replacement §6,
using §§2–4/step-417 only for the native additive construction. The
pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-24-direct-four-rule-parity-audit-coverage.md`;
its TARGET exactly matches this audit. The reported gate mismatch does
not persist in the supplied snapshot. Neither the old compiler nor the
old audit's source-completeness verdict is validated. L107 and Attempt
036 remain intact. No new external source or completeness theorem is
needed: receive Shoenfield (1967), §2.6 pp.21–22 and §3.1, Tautology
Theorem p.27, Detachment p.28, propositional proof pp.28–30, through
the separately audited L109 fixed-library contract. Receive L108 only
for legal supplied primitive archives and L097/L098 only for the
specific component arguments used below.

**Finite library and all row cases.** The union in §6.2 is finite before
an input is chosen. Arity is at most three, so there are at most eight
assignments and four forbidden-assignment clauses for a nonzero arity.
Each clause has finitely many binary shapes, and K has the specified
fixed conjunction shape. For arity zero the two cases are K=true,
T(R)=false and K=false, T(R)=true. Both row implications are valid.
For positive arity, each clause forbids precisely its indexed assignment;
their conjunction is true exactly when the row parity is b. Missing
slots contribute zero and b occurs once in R, so T(R) is zero exactly
in that case. This proves the row implication for every assignment
and every admitted clause shape, without a global truth-table test.

For the other added members, literal X computes the two-element sum
and E tests equality. Commutation, association, zero and cancellation
are their respective group identities. With G=0 all guarded consequents
are true. With G=1, transitivity and either XOR congruence preserve bit
equality, and zero sum adds two zero bits. Guarded conjunction combines
two true consequents; guard introduction and G→true follow from the
implication truth table. E(false,true) is false, giving its discharge.
For refutation transport, ¬A true implies A=0 and G→A true then forces
G=0. These exhaust the additional library, including constants and
coincident slot images. L097's reused library is already Boolean-checked.
L109 therefore applies to this fixed union, with arbitrary-depth actual
arguments and no fresh image atoms. All intermediate/unused records of
its selected proofs count as fixed compiler data. Their preparation
may be unbounded in library size; no bound for arbitrary tautologies is
being inferred.

**Native exposure, reversal and literal expansion.** Check exposure
on an arbitrary height-d binary tree, including the incomplete remainder
of a prior exposure. After an optional root commute, the marked leaf
is in a child of height at most d−1. A singleton child needs no recursive
step. Otherwise induction exposes it as a+W, with height(W)≤d−1
and intermediate child height≤d. Inside the original root those
intermediates have height≤d+1. Rotating (a+W)+C to a+(W+C) leaves
remainder height≤d because both W and C have height≤d−1. The
elementary rewrite count satisfies e(d)≤e(d−1)+2. No leaf is copied.

From an initial complete height-h tree, first exposure thus has
remainder height≤h. Exposing the second leaf there has intermediate
whole height≤h+2. For N>2 its final remainder V is nonempty; the
three middle rewrites through (a+b)+V, (b+a)+V and b+(a+V) stay
within that height. Reverse the recorded exposures after exchanging
the two marked leaf tokens. Each exposure identity is linear in its
subterms, so the exchanged records remain actual association/commutation
instances. Tokens distinguish positions even when their written names
agree. Exchanging two height-zero objects changes no intermediate
shape. The final shape is complete again; height cannot accumulate
over successive swaps. N=2 would use commutation, while admitted U
has N≥4.

Each local identity is guarded using guard introduction. Either
orientation is available by the reused guarded symmetry. Lift it through
the actual ancestor chain using one-argument XOR congruence, and chain
the resulting root comparisons by guarded transitivity. O(h+1) local
rewrites times O(h+1) ancestor lifts give O((h+1)²) calls per swap.
Their arguments are the actual subterms, never a prior proof derivation
or a recursively nested equality formula. This is the crucial ordinary
formula interface, not an implicit context rule.

Every variable multiplicity in U is even and its number of ones is
odd. Since N is even, its number of zeros is odd too. Reserving one
one and one zero leaves even multiplicities for all symbols. Pair them
as siblings; a permutation of N positions takes at most N−1 swaps.
Cancel equal sibling pairs and use the zero law on (1,0), then collapse
the remaining zero subtrees. Terms shrink; ancestor lifts and chaining
cost O(N(h+1)). This gives the exact guarded U=1 endpoint. Independently,
selected row U=0 endpoints combine bottom-up by guarded zero sum.
A padded four-zero block has its zero endpoint from XOR cancellation
with argument X(false,false), followed by guard introduction. Thus
padding needs no extra library member. Symmetry on U=0 and transitivity
with U=1 yield E_F(false,true), and discharge yields exactly ¬F.

All intermediate native terms have O(N) nodes and height≤h+2, with
N=O(Q). In the literal image each occurrence is copied at most twice
per additive ancestor. Hence |T(s)|≤c|s|2^depth(s)=O(Q²).
The equality, guard and fixed proof skeletons multiply this by constants.
F is copied as its actual tree, of O(Q) nodes regardless of depth.
Arbitrary F depth therefore causes no uncontrolled XOR expansion.

**Primitive assembly and exceptional inputs.** From actual earlier
A and ¬A∨B, expansion gives B∨A. Together with the axiom ¬B∨B,
cut with pivot B gives A∨B; cut with pivot A and the supplied implication
gives B∨B; contraction gives B. This verifies the five records and
their exact ordered arguments/references. Repeating this for curried
antecedents receives every library use. Inverse association is a proved
equality obtained using guarded symmetry, never an extra directed rule.

Identity and projection/composition follow the actual F conjunction
paths. Guarded conjunction assembles precisely the specified K_j, whose
row theorem composes to F→E(T(R_j),false). Consistent zero rows use
F→true and their row theorem, including when λ_j=0. Unused rows and
records are retained. If an empty clause is present, the same projection
path gives F→false and final discharge gives ¬F; F=false has an empty
path. The λ conditions exclude r=0 and an empty global F. In particular,
if selected rows have no variable occurrences and odd total b, some
selected zero row is inconsistent and the empty-clause branch applies.
No exceptional case relies on the stopped three-scheme presentation.

**Direct occurrence replay and complete receiver.** The direct π₄
archive has no old-source axiom/MP tag needing L098's whole converter.
Simultaneous θ maps every record to the same primitive rule instance,
preserving backward references and literal repeated arguments even if
images coincide. Source names not occurring in F, if retained, can map
to the existing gadget occurrence; constants remain fixed. The final
tree is exactly ¬θF.

L098 §6.3's component requires precisely this earlier endpoint, not an
old-presentation source tag. Projections from G→G yield G→C_F and
G→U_s. Branch projections, same-negative/same-positive and Cases give
E_G(z_i,r_x); singleton groups use empty paths and coincident selected
leaves. The entire expanded C_F/θF pair has the same connective skeleton.
Guarded reflexivity at constants, these occurrence comparisons at
variables, and negation/OR congruence at every internal node prove
E_G(C_F,θF). This includes all nodes of each expanded conjunction and
the arbitrary global F tree. Transport gives G→θF, and refutation
transport receives first ¬θF and then G→θF to give exactly ¬G.
Every antecedent is an actual earlier endpoint; no assumption is opened.

Complement the whole archive, not just ¬G. Arbitrary formula substitution
preserves each primitive pattern; y↦¬y adds one negation per leaf and
fixes constants. The result meets every L108 hypothesis with unchanged
alphabet/dictionary. The structural identity tr(P[¬y/y])=1+v(P) holds
at atoms/constants, adds one at negation, and at OR multiplies the two
child values in their actual order. Thus its endpoint translates to
f g̃. L097 identifies f and g in their separate increasing-multilinear
orders; it does not identify g̃ with g or apply injectivity to fg.
Its unchanged ordered correction gives J(0)=0, J(B)=g+g̃, including
singleton groups. L108 gives K(0)=0, K(B)=f g̃. Disjoint copies and
fresh exterior endpoints form H=K+fJ; the two identical ordered
f g̃ terms cancel. For an empty clause f=0 formally by the absorbing
tester recurrence, so the no-path output with distinct endpoints is
valid. The gadget, unused records and full original B remain present.

**Independent original-Q ledger.** Q is fixed by (2), before any source
archive exists. Source projections and row assembly use O(Q²) calls.
The additive part uses O(N(h+1)²)+O(N(h+1)) calls. The looser O(Q⁴)
bound covers all calls and primitive records. Each complete instantiated
library/detachment line has O(Q²) nodes and O(Q³) bits, including long
names and explicit slot arguments. Global references contribute only
O(log(Q+2)) per field. Thus the source and direct θ replay each fit
O(Q⁷) bits, including worksheets and their polynomially many indices.
This is a fresh count: L098's O(Q³) source-part estimate is inapplicable.

L109's quadratic instantiation takes O(Q⁶) time per argument package
and O(Q¹⁰) over O(Q⁴) calls. Even rescanning the O(Q⁷)-bit archive
per call costs O(Q¹¹); coefficient/name comparisons, canonical-F and
provenance checks, worksheet construction and reference relocation fit
the stated source allowance CQ¹². No runtime library search occurs.

The receiver adds O(Q³) calls/records, each with O(Q²) bits, hence
O(Q⁵) added bits. Whole-archive complementation preserves the counts
within constants. Retaining source/replay/receiver archives, maps, input
and dictionaries still permits R₁≤CQ¹². A full scan at every source
or receiver call and ordinary name/reference comparisons fit O(Q²⁰)
preprocessing time. L108 therefore gives |K|≤CR₁¹⁴≤C'Q¹⁶⁸
and time O(Q^{12b}), for its fixed bit-time exponent b.

For J, O(Q) original-only L035 inputs have full size O(Q²), including
B. The safe O(E⁴) bound gives O(Q⁹) aggregate correction bits.
Independent contexts cost O(Q³), and global numbering fits O(Q¹⁰).
Its fixed construction and scans fit O(Q^max(22,2d+3)). Final disjoint
copying and global reindexing add a logarithmic size factor to the
sum of these archives, not a multiplication by their sizes. Hence
|H|≤CQ¹⁷⁰ remains valid. Quadratic processing of that full output
fits Q³⁴⁰ and absorbs preprocessing; the total time bound is exactly
the stated CQ^max(340,12b,2d+3). All constants/exponents are fixed
independently of the input, though the library constants have no explicit
numerical estimates here. The actual degree is bounded by the explicit
edge count.

**Verdict.** No substantive defect, changed hypothesis, bound or direct
mathematical input was found. This is an informal audit of a conditional
restricted supplier using assessed machinery, not progress beyond the
inspected sources, certified originality or a main-problem candidate.
No concrete library, executable compiler, complete stream or Mathlib
match is verified. L107/Attempt 036 still stop the old interface.
General short source proofs, M-only bounds, universal W₂, arbitrary ER
data and unrestricted SAT remain open. The main argument and DAG do
not change.

## Mathlib

Full matching coverage has not been checked. No Mathlib theorem is used
as a certificate for the ordinary-Frege compilation, exact occurrence
receiver or binary ledger. Availability of supporting field or finite-sum
facts would not supply those proof-system interfaces. The full matching
theorem, direct four-rule compiler, component receiver and original-Q
ledger in §6 have not been checked in Mathlib. Supporting Boolean/F₂
identities alone would not verify literal primitive-proof replay.
