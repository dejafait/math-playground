# L097 — Supplied source resolution gives an exact occurrence-product witness

## Hypotheses

Work over F₂. Supply a width-at-most-three CNF F, a valid explicit
ordinary resolution DAG refutation π of F, and exactly L087's constructed
occurrence pair D,E, with its provenance, orders, names and dictionaries.
Weakening, clause reuse, repeated literals, tautological clauses and empty
clauses are allowed. Extension axioms are not allowed in π. Every proof
line, literal name and reference is written and charged.

Retain L087's actual ordered representatives f=r_D, g=r_E and its complete
Boolean/commutator list B, with placeholders σ_i,τ_ij. The original
alphabet is precisely the occurrence names y, including the four
occurrences of the appended u/v gadget. Put

    Q=2+M+|F|+|π|,

where M is L087's pre-witness input size. No witness, witness degree or
unwritten source-proof tree contributes to Q. Provenance means the actual
L087 construction, not just an arbitrary Boolean-equivalent pair of OBDDs.
It may be verified by rebuilding the two specified transition systems,
using the supplied naming map; all source data for that check are charged.

## Conclusion

There is a deterministic construction of an explicit acyclic affine-F₂
ABP H using only y,σ,τ such that, formally in the free algebra,

    H(y,0)=0,                 H(y,B(y))=fg.

One fixed polynomial in Q bounds its full binary length and construction
time, including complete original/axiom/placeholder dictionaries and
every independent graph copy. No bound on |π| in terms of M or |F| is
asserted. This is a specialization/reproduction of the inspected Frege
extraction mechanism with an exact occurrence interface and a corrected
graph reception of its axiom seeds; no originality is certified.

The separate step-380 informal critical audit repairs the previously
unspecified constant axioms and their extraction seeds. With that repair,
it finds no remaining defect in the stated identities or polynomial
ledger. No implementation or machine-checked proof is claimed. This is
not a solution candidate for P versus NP. Polynomial resolution
availability, arbitrary-order W₂, general ER data and unrestricted SAT
remain open.

## Proof

**Sources and scope of their use.** The pre-invocation SPECIALIZE
assessment is
`drafts/literature/2026-10-20-source-resolution-occurrence-product-witness.md`.
Use Li–Tzameret–Wang, *Characterizing Propositional Proofs as
Non-Commutative Formulas*, SIAM J. Comput. 47(4), 1424–1462 (2018),
[DOI](https://doi.org/10.1137/16M1107632), specifically the inspected
[40-page author revision](https://www.doc.ic.ac.uk/~itzamere/Ideal_non-commutative.pdf):
Definition 1.3 p.6 and Theorem 3.1/Lemma 3.3 pp.13–14. Numbering is that
PDF's, accessed 2026-10-20; its revision date is not established.
We use its ordered conclusion translation and modus-ponens extraction,
not the differently worded introductory Theorem 1.4. We bypass Lemma
3.6's product case, which omits a needed commutator, by L035/L036.
The construction below explains this necessary repair in the ABP model;
it makes no claim to repair the source's formula-size bound.

For formula-to-graph conversion use only Raz–Shpilka,
[*Deterministic Polynomial Identity Testing in Non Commutative Models*,
author manuscript, Lemma 2 Step 1, p.5](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
with L049's inspected reception. Ordered serial/parallel conversion
preserves the polynomial, including constants; homogeneous splitting
and PIT are not used. The other mathematical inputs are L026's
single-order injectivity and the audited arbitrary-graph witnesses
L035/L036. L037 and C046a are comparisons, not inputs: their source
certificate outputs are not identified with fg.

**1. Compact polynomials for the exact testers.** If F has an empty
clause, L087's D starts in its absorbing failure state. Its representative
is formally zero by the suffix recurrence. Return a zero ABP with distinct
endpoints and no accepting path, retaining all dictionaries. Henceforth
there are no empty clauses.

Let C(y) be the conjunction of the split clauses of F⁺, in their actual
clause and literal order. All conjunctions/products below have any fixed
explicit binary bracketing preserving the displayed leaf order.
For an occurrence literal let l=y for a positive sign and l=1+y for a
negative sign. Define the truth-polynomial translation v by

    v(y)=y,    v(false)=0,    v(true)=1,    v(¬A)=1+v(A),
    v(A∧B)=v(A)v(B),
    v(A∨B)=1+(1+v(A))(1+v(B)).

Its size is linear in the written formula size; neither argument is
duplicated at a connective. For a clause its value is
1+∏(1+l), in literal order, and v(C) is the product of these values in
clause order. Every occurrence name appears in only one clause. Thus
v(C) and f both lie in the increasing-multilinear word space in D's
order and agree on all Boolean assignments. L026's injectivity, applied
in that order only, proves the formal identity v(C)=f.

List E's nonempty groups in their actual group order. In group s write
its names z₁,…,z_k in their actual within-group order and put

    a_s=∏_{i=1}^k(1+z_i),   b_s=∏_{i=1}^k z_i,
    e_s=a_s+b_s,
    U_s=(¬z₁∧…∧¬z_k) ∨ (z₁∧…∧z_k),
    t_s=v(U_s)=a_s+b_s+a_s b_s.

For k=1 these are interpreted as the corresponding one-leaf conjunctions,
so e_s=1 while t_s=1+z₁+z₁². Put U=∧_s U_s, preserving group order,
and g̃=v(U)=∏_s t_s. The products ∏_s e_s and g are increasing multilinear
in E's order and agree on all Boolean assignments, including singleton
groups. Again L026, in this order alone, gives g=∏_s e_s.
No injectivity claim is made about fg or g̃.

The formulas for C,U,f, all a_s,b_s,e_s,t_s and g̃ have O(q+|F|+1)
nodes in aggregate up to a fixed factor if full products are written
once. Prefix/suffix copies used later are charged separately. Unreachable
tester states and redundant dense queries change neither identification.
Repeated source literals have distinct occurrence names; their signs
are used only in C. The u/v groups and clauses are included unchanged.

**2. Correct the ordinary consistency formula to the exact tester.**
Fix a group and write

    A=∏_{i=2}^k(1+z_i),       B'=∏_{i=2}^k z_i,

with empty products 1. Apply L035 to the original-only formula graphs
for A and z₁, obtaining W(A,z₁). Define a graph by disjoint serial and
parallel compositions for

    R_s=(1+z₁) W(A,z₁) B' + σ_(z₁) A B'.                 (1)

Then R_s(y,0)=0 and

    R_s(y,B(y))
      =(1+z₁)(A z₁+z₁ A)B'+(z₁²+z₁)AB'
      =(1+z₁)A z₁ B'=a_s b_s=e_s+t_s.                  (2)

The cancellation uses the adjacent factor (1+z₁)z₁, without moving a
factor for free. When k=1, the commutator is zero and (1) reduces
polynomially to σ_(z₁), as required.

Using independent copies, construct

    J=Σ_s (∏_{h<s}t_h) R_s (∏_{h>s}e_h).               (3)

All contexts in (3) are original-only formulas. Replacing e_s by t_s
successively from left to right proves by additive telescoping that

    J(y,0)=0,                 J(y,B(y))=g+g̃.           (4)

In detail the s-th summand after substitution is the sum of the two
successive products with prefix t₁,…,t_(s−1), suffix
e_(s+1),…,e_r and middle e_s or t_s; internal products cancel in pairs.
This keeps every factor in its displayed position and requires no common
order between D and E.

**3. An occurrence-only Frege proof from the supplied resolution DAG.**
Put G=C∧U. Choose for each source variable occurring in F its first
occurrence name r_x. For source proof variables absent from F choose
y₁; the gadget ensures y₁ exists. This defines one uniform substitution
θ on all variables of π. It is allowed to be noninjective.

Here are explicit polynomial proof operations, rather than an appeal
to the semantic unsatisfiability of G. Projection from G gives C, U,
each split clause and each U_s, under the same guard G. Projection from
the two conjunctions inside U_s, followed by disjunction elimination,
gives, under G, z_i↔r_x for each occurrence of each source variable.
For the all-zero disjunct both sides are false; for the all-one disjunct
both are true. These are instances of fixed propositional implications
together with conjunction projection. Singleton groups give z₁↔z₁.
The u/v groups need no source-variable inference.

Negation congruence retains the literal signs, and at most three
literal replacements per original clause give G→θ(C_j) for every
written original clause C_j. No source symbol remains. Repetition,
opposite signs and tautological clauses require no special inference:
the same equivalences are substituted at the actual leaf positions.

Process π in its given topological order. Suppose a resolution line
uses parents p∨A and ¬p∨B and concludes A∨B. From the previously
written guarded parents obtain the guarded conclusion by the fixed
resolution tautology, uniformly substituted by θ and guarded by G.
The rule is still valid if θ identifies different old variables.
Weakening uses its fixed implication. Rebracketing, permutation,
duplicate removal or the actual source clause convention can be paid
by adjacent OR exchanges, associativity and idempotence followed by
connective congruence. Complementary literals need not be deleted.
This gives G→θ(C_i) for every line, with references to previous guarded
lines, not copies of their derivation ancestry.

The final empty clause yields G→false and then R=¬G by a fixed
implication. Use the three Schoenfield schemes with modus ponens,
explicitly augmented by the ground axioms true and ¬false. This makes
the interpretation of the two constants part of the proof presentation;
the three schemes alone do not fix it. No free variable is introduced
by these ground axioms.

Here is why the required fixed tautology templates have fixed proofs
in that precise presentation. For a template containing constants,
replace true and false by schematic letters t and d. If its resulting
formula is V(t,d), then t→(¬d→V(t,d)) is a constant-free tautology
(the other schematic arguments remain arbitrary). Standard classical
propositional completeness supplies a fixed Schoenfield proof of it.
Substitute true for t and false for d, then apply MP using the two
ground axioms. A fixed inference template with premises is treated by
first forming its curried tautological implication and then applying
MP to its actual premises. Instantiation and congruence along the
written formula tree therefore give finite Frege derivations, with
constant overhead per fixed template, rather than truth-table axioms
on a growing alphabet. In particular (G→false)→¬G is covered in this
presentation. Uniform substitution in all proof lines preserves the
ground axioms, so the complement substitution below is still valid.

To receive LTW's translation use the assumption-free conclusion

    T=R[ y_i := ¬y_i for every occurrence name ].

Perform that same uniform substitution in every line of the constructed
Frege proof. LTW's tr has tr(y)=y, tr(false)=1, tr(true)=0,
tr(¬A)=1+tr(A), tr(A∨B)=tr(A)tr(B), and
tr(A∧B)=1+(1+tr(A))(1+tr(B)).
Induction on a formula P, checking its leaf and three connective cases,
therefore gives

    tr(P[¬y/y])=1+v(P).

For example the AND case is
1+(1+(1+v(A)))(1+(1+v(B)))=1+v(A)v(B);
the OR case is (1+v(A))(1+v(B))=1+v(A∨B).
Consequently the exact conclusion has

    tr(T)=v(G)=f g̃.                                      (5)

This complement substitution addresses the source's truth convention;
it does not rename arithmetic y to 1+y in the desired output.

**4. Receive the extracted conclusion, with corrected axiom blocks.**
We describe the ABP specialization of LTW Lemma 3.3's extraction so
that its suspect Boolean-only subcase is not a hidden hypothesis.
Take the fixed Schoenfield Frege presentation with ∨,¬, modus ponens
and the two explicitly specified ground constant axioms above.
The preceding finite templates can be fixed in this presentation;
∧ is the abbreviation ¬(¬A∨¬B), which duplicates neither argument
and has exactly the stated tr. Let the resulting proof be
ℓ₁,…,ℓ_k, and put P_i=tr(ℓ_i). These are original-only formulas,
whose total size is linear in the total Frege symbol count.

For completeness, corrected seed graphs exist for all three axiom
schemes, without using the source's “similar” axiom case as an extra
assumption. With a,b,c denoting translations of their substituted
arguments, the three axiom translations are the fixed polynomials

    q₁=(1+a)(1+b)a,
    q₂=(1+a(1+b))(1+ab)a,
    q₃=(1+(1+a)(1+b)c)(1+(1+a)b)(1+a)c.                  (6)

Each is zero on scalar Boolean a,b,c. For q₁ and q₂, a=0 or a=1
checks this directly (q₂ at a=1 is b(1+b)). For q₃, either
(1+a)c=0 or a=0,c=1; the latter leaves b(1+b).

Here is a finite algebraic recipe for their seeds. Expand each fixed
polynomial (6) into words in at most three letters. In each word sort
adjacent distinct letters in the order a,b,c; the change at each swap
is u(de+ed)v. Delete adjacent repetitions using
u(d²+d)v. Record every change additively. Each operation decreases
either the inversion count or word length in this two-stage process.
The final sum is increasing multilinear and is zero by its scalar
Boolean vanishing and L026's injectivity. Hence each q_j equals the
recorded finite sum of contextual commutators and Boolean polynomials.
The degrees in (6) are at most seven, so the word count, number of
changes and context lengths are absolute constants, independent of
the actual argument formulas. This is a justified bounded seed repair,
not Boolean normal-form enumeration of the actual growing proof.

Now replace a,b,c by their actual original-only translated argument
formulas. Convert each such formula and each finite context to its
ordered graph by the cited conversion. Replace every central d²+d
by an independently copied L036 witness on that original-only argument
graph; replace every central de+ed by an independently copied L035
witness on those two argument graphs. Concatenate the actual original-only
left and right contexts and sum the terms. This produces a seed Z_i
with Z_i(y,0)=0 and Z_i(y,B(y))=P_i for each axiom instance.
All source auxiliary a,b,c have been substituted out. Every L035/L036
input is original-only, never a previously built placeholder witness.
Both kinds of blocks retain the full occurrence B dictionary, including
unused positions. No Boolean-only product identity is invoked.

For modus ponens, if line i follows from lines j: A and h: A→ℓ_i,
the imported LTW recurrence specializes in F₂ to

    K_i=K_j P_i+K_h,                                      (7)

since P_h=(1+P_j)P_i. Thus K_i(B)=P_j P_i+(1+P_j)P_i=P_i,
and K_i(0)=0. Schematic axiom lines use K_i=Z_i. For the remaining
ground axiom lines, tr(true)=0 and tr(¬false)=1+1=0; assign Z_i to
be a zero graph with distinct endpoints and no accepting path. This
has both required zero identities and retains the complete B dictionary.
Thus every possible proof line in the specified presentation has a
seed or an MP transition. There is no appeal to the source's handling
of constant axioms.

To implement (7) without proof-tree unfolding, make a vertex v_i
for each proof line and a fresh source s. At an axiom line attach a
disjoint seed graph from s to v_i with constant-one connectors. At
each MP line attach a fresh copy of the original-only formula graph
P_i from v_j to v_i, and a separate constant-one edge from v_h to v_i.
All internal vertices are fresh. The topological order of proof lines
with the transition interiors inserted before their destination proves
acyclicity. The accepting endpoint is the final-line vertex v_k.
The sum of s-to-v_i path products obeys exactly (7); the argument uses
incoming transitions, so later outgoing edges at v_i cannot change it.
All proof-line reuse is graph reconvergence. If both premises have
the same index, retain both transitions, including their multiplicities.
There is no source-to-output path apart from paths starting in a seed.

Induction over i now proves both formal identities. For the final
graph K, equation (5) gives

    K(y,0)=0,                 K(y,B(y))=f g̃.             (8)

This directly realizes the inspected extraction recurrence in the
requested graph model. It imports no general graph-to-formula theorem
and does not claim the new seed graphs are small tree formulas.

**5. Output and complete polynomial ledger.** Construct, with disjoint
copies and fresh exterior endpoints,

    H=K+fJ.                                                (9)

Equations (4) and (8) prove H(y,0)=0 and
H(y,B(y))=f g̃+f(g+g̃)=fg. There are no source clause placeholders,
unsplit variables or extension variables. Parallel edges and cancellation
are retained. Constant and singleton cases are already included.

Here is one full ledger, with all bounds measured before H exists.
The counts q, number of clauses/groups, number of proof lines, every
source clause width and every written name length are bounded by Q
up to a fixed encoding constant. Original names are stored in dictionaries
and may also be pessimistically charged Q bits at each written leaf.
Rebuilding provenance, checking resolution references and parsing all
data take polynomial bit time in Q; the proof does not require solving
SAT or testing the semantic promise.

The Boolean formulas C,U,G have O(Q) nodes. Each clause line after θ
also has O(Q) nodes. The guard is copied in every generated guarded
line, not expanded recursively. Per source line, O(Q²) adjacent
exchanges/contractions suffice to reconcile clause lists; lifting each
through a context needs at most O(Q) fixed-template instantiations.
Projection and the occurrence equivalences have at most O(Q²) such
paths of length O(Q). Thus O(Q⁴) fixed-template instances suffice
overall, each with O(Q) nodes and O(Q²) full name bits. Constant
expansion factors for the fixed proofs, final complement substitution,
global reference renumbering and all input/provenance copying can
therefore be bounded by

    S ≤ c₀ Q¹²                                              (10)

for the complete constructed Frege proof, with construction time bounded
by another fixed multiple of Q¹² after a conservative enlargement.
This loose exponent does not depend on the width or ancestry depth of
π; in particular it never measures an unfolded resolution proof.

Put R₀=2+Q+S. Each translated argument, conclusion or context in a seed
has O(S) nodes. Formula-to-graph conversion gives O(S) records;
even charging R₀ bits per name, endpoint and framing item gives input
length at most c₁R₀² for any L035/L036 call, including a fresh complete
B dictionary. Their full-bit output bounds are respectively O(E⁴)
and O(E⁶). Hence every seed, containing only an absolute constant
number of these blocks and contexts, has at most c₂R₀¹² bits before
global renumbering. There are at most S seeds.

There are at most S MP lines; their independently copied P_i graphs
and all connecting edges use at most O(R₀³) bits under the same
conservative name allowance. All seed, proof-line and transition graphs
therefore fit c₃R₀¹³ bits before global renumbering. Dense new vertex
identifiers and global length fields add at most a factor O(log R₀),
or the looser factor R₀. No label is circuit-valued.

For (1)–(3), at most Q original-only L035 calls have input length
O(R₀²). Each context in a summand of (3) copies at most O(Q) formula
nodes: the group formulas have total O(Q) nodes, even though t_s has
two copies of each a_s,b_s. There are O(Q) summands and each R_s is
copied once. Thus the entire J, f and final connectors fit within
the same conservative c₄R₀¹⁴ allowance. Repeating the complete
dictionary for each separately constructed intermediate block has
already been paid; the final output dictionary is paid again.
Combining with (10), one valid nonoptimized full-output bound is

    |H| ≤ c₅R₀¹⁴ ≤ c₆Q¹⁶⁸.                              (11)

For time, let d≥6 be one fixed exponent bounding the deterministic
bit algorithms of L035 and L036 on E-bit inputs, enlarged to cover
their output writing. Such a fixed d is part of their polynomial-time
conclusions, not an input parameter or a semantic search assumption.
There are O(R₀) calls, each on at most c₁R₀² bits. Formula conversion,
independent copying and final numbering have polynomial cost in the
bounded records. Even a quadratic scan of the complete written records,
together with parsing and the Frege construction, gives the common bound

    time ≤ c₇ R₀^max(30,2d+2)
         ≤ c₈ Q^[12 max(30,2d+2)].                       (12)

All constants and exponents depend only on fixed encodings, the fixed
Frege templates and the cited algorithms, not on F, π, their names or
the wanted witness. The constructed affine DAG also has path degree at
most its number of edges. No PIT, path enumeration, dense polynomial
expansion of actual arguments, or uncharged proof conversion occurs.
The only expanded polynomials are the three fixed schemes (6); the
two ground constant axioms use the zero seeds specified above.

The comparison threshold is polynomial in Q, and (11)–(12) meet it.
They do not imply a polynomial in M alone when the supplied π is long.
The construction step supplied no implementation or finite certificate
test. Its separate critical audit is recorded next.

**Independent critical audit — 2026-10-20, step 380.** This is the
mathematical audit authorized by the pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-20-source-resolution-occurrence-critical-audit.md`.
It uses L026/L035/L036/L049/L087 with their stated hypotheses. A narrow
primary reread confirms the actual Schoenfield schemes (author PDF
p.2), Definition 1.3 (p.6), and Lemma 3.3's axiom/MP cases (pp.13–14);
the citations and version qualification above remain in force. It
imports neither the source's Boolean-only product argument nor its
tree-ancestry formula bound.

The original constant convention was incomplete: with only the three
schemes and MP, treating false as an uninterpreted atom preserves
soundness of every rule, but does not validate (G→false)→¬G. Merely
calling it a standard constant therefore left a missing proof case.
The explicit two ground axioms, constant-template construction and zero
extraction seeds above repair this without changing any hypothesis,
target polynomial, dictionary or bound. The repair is part of this
audit, not a new general theorem or a restriction of the admitted input.

The rest of the audit proceeds as follows.

- **Exact tester reception.** Occurrence names in C are distinct even
  when source literals repeat or have opposite signs. Each clause
  polynomial and their ordered product are increasing multilinear in
  D's actual order. Each e_s and their ordered product have that property
  in E's actual order, including e_s=1 for singletons. The suffix
  recurrence gives the same Boolean tests, so L026 applies separately
  to each factor. Empty source clauses take the direct zero graph.
  All four gadget occurrences and their groups remain in both factors.
- **Group correction and final target.** Expanding (1) after substitution
  cancels the two copies of (z₁+z₁²)AB', leaving
  (1+z₁)Az₁B'=a_s b_s. This uses no interchange of A and z₁.
  For a singleton, A=B'=1, its commutator vanishes and the substituted
  correction is z₁²+z₁. The ordered product telescope (3) cancels each
  internal prefix-t/suffix-e product exactly twice; its endpoints are
  g and g̃. Equations (5), (8) and (9) then give exactly fg, not just
  its Boolean value or f g̃. At zero placeholders every seed and R_s
  vanishes, and (7) and (9) preserve zero.
- **Occurrence proof and substitution.** Each group contains the chosen
  representative r_x, so conjunction projections in each disjunct of
  U_s yield both implications between that representative and every
  occurrence. Fixed case-elimination templates put these implications
  under G. Sign congruence and at most three replacements transfer each
  source input clause. Reordering/idempotence only reconcile written
  clause conventions; each guarded resolution or weakening step uses
  already derived lines. Foreign source proof variables map to the
  existing y₁ and do not survive in any output. Substitution is
  simultaneous in the entire derivation, with the same composition on
  each axiom instance and MP pair, rather than a new substitution rule
  on a single proved line. After complementing every occurrence, the
  leaf, constant, negation, OR and AND cases prove
  tr(P[¬y/y])=1+v(P). Hence the assumption-free last line has precisely
  translation f g̃. No source clause placeholder enters extraction.
- **All axiom seeds.** Directly translating the three schemes printed
  on source p.2 gives (6), in exactly that factor order. Their respective
  maximal degrees are 3, 5 and 7. For q₁ and q₂ split on a; for q₃
  either its final (1+a)c is zero or a=0,c=1, leaving b(1+b).
  Thus each vanishes at every Boolean scalar assignment. Sorting each
  of the boundedly many expanded words and then contracting repeated
  adjacent letters records its exact difference as contextual
  commutators and d²+d. After these changes the increasing-multilinear
  remainder is zero by L026, including its empty-word coefficient.
  Under substitution the recorded central expressions are received by
  L035/L036 on original-only argument graphs. No witness is fed as an
  operand to either lemma. Constants among the arguments satisfy their
  hypotheses. The additional ground axiom seeds are zero as proved
  above; this exhausts all axiom types.
- **DAG realization.** For every MP destination i, the incoming
  transitions contribute K_j P_i and K_h, in that order. Topological
  placement of their fresh interiors between predecessor vertices and
  v_i prevents cycles. Seed interiors start only at the fresh global
  source. Every path to v_i has a unique final incoming seed/transition,
  proving the recurrence without enumerating paths. Later outgoing
  edges cannot change these path sums in a DAG. Repeated predecessor
  indices retain separate transitions, so F₂ cancellation has its
  correct multiplicity. Serial/parallel copies for J and H have fresh
  exterior endpoints and cannot create extra accepting paths.
- **Complete bounds and time.** At most O(Q) source lines each require
  O(Q²) clause-list operations, with at most O(Q) congruence steps per
  operation, yielding O(Q⁴) fixed-template instances. Group projections
  and equivalences fit the stated O(Q²) paths of length O(Q). Each
  actual instance has O(Q) formula nodes, O(Q²) restored-name bits and
  boundedly many proof lines; reference bits add only a logarithmic
  factor. The two constant axioms and their fixed template proofs add
  only constant factors. Thus the deliberately loose S≤c₀Q¹² and its
  construction-time bound cover guard copies, normalization, complement
  substitution and global Frege references. No expanded proof ancestry
  appears in this count.

  Each seed uses only a constant number of original-only graphs and
  L035/L036 calls with full input length O(R₀²), including B. The larger
  O(E⁶) output bound therefore gives O(R₀¹²) per seed, O(R₀¹³) over
  at most S seeds. Zero constant seeds are smaller. Original-only MP
  transitions cost O(R₀³) altogether. Final dense identifiers add
  O(log R₀), absorbed by the R₀¹⁴ allowance. The at most Q correction
  calls and O(Q²) total context nodes of J also fit it. All complete
  dictionaries are included at each claimed independent block and at
  final export. Since R₀=2+Q+S=O(Q¹²), (11)'s Q¹⁶⁸ bound survives.
  A fixed d for the two input-polynomial bit algorithms gives at most
  O(R₀^(2d+1)) call time; quadratic copying/renumbering of the complete
  O(R₀¹⁴)-bit record set fits O(R₀³⁰). These and Frege construction
  fit (12). The exponent is fixed independently of the supplied proof.

The repaired all-size informal argument passes these checks. This is a
local repair and verification of known-mechanism specialization, without
certified originality, executable certificates or formal verification.
It leaves short source-resolution availability, a bound in M alone,
universal W₂, arbitrary ER data and unrestricted SAT decision/separation
unresolved. Structural validation alone cannot certify this audit.

## Mathlib

Full matching coverage of this transfer, the Frege extraction, the
explicit affine-ABP construction and its binary/time ledger: **not
checked**. No absence or machine-verification claim is made. Precise
primary imports and their restricted roles are stated above. The
ordered tester correction and graph reception are proved here rather
than inferred from Boolean equality of the two-order product.
