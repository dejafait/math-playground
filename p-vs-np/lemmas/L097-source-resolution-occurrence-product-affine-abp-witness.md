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

**Current qualification — steps 434/436.** The replacement proof in §6 below
establishes the asserted conditional construction using audited L108/L109
and Shoenfield's four primitive rules, with a newly justified original-Q
ledger. The independent step-436 audit in §7 finds no substantive defect
within the stated supplied-resolution hypotheses; no executable library
or implementation has been verified. Sections 3–5 and their step-380 audit
are preserved historical derivations, superseded only at their source
compiler, extraction and ledger interfaces by §6.

**Preserved old-interface qualification — step 422.** L107 proves that the exact
three-scheme/MP/ground-constant presentation on unrestricted primitive-OR
trees is incomplete. Thus §3's invocation of completeness to obtain
arbitrary literal-OR templates is invalid for that exact interface, and
the source assembly below is unsupported as written. The historical
step-380 audit is preserved, but does not settle this newly identified
gap. This does not refute the asserted existence of H by another method;
the corrected axiom extraction blocks and retained finite strings are
not the failed step. Section 6 changes the presentation rather than
asserting validity of those old proof streams.

There is a deterministic construction of an explicit acyclic affine-F₂
ABP H using only y,σ,τ such that, formally in the free algebra,

    H(y,0)=0,                 H(y,B(y))=fg.

One fixed polynomial in Q bounds its full binary length and construction
time, including complete original/axiom/placeholder dictionaries and
every independent graph copy. No bound on |π| in terms of M or |F| is
asserted. This is a specialization/reproduction of the inspected Frege
extraction mechanism with an exact occurrence interface and a corrected
graph reception of its axiom seeds; no originality is certified.

The historical step-380 informal critical audit repairs the previously
unspecified constant axioms and their extraction seeds. With that repair,
it found no further defect then; L107 subsequently invalidated its
template-completeness check. It does not audit §6. No implementation or
machine-checked proof is claimed. This is
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

**6. Four-rule replacement — step 434, 2026-10-23.**

This section replaces the unsupported source-template construction in
§3, the three-scheme extraction in §4, and their composed ledger in §5.
It retains the hypotheses and the exact formulas/polynomials of §§1–2.
The pre-invocation SPECIALIZE coverage is
`drafts/literature/2026-10-23-four-rule-resolution-occurrence-reception.md`,
whose COVERED_TARGET is this repair. No arbitrary source-Frege,
renaming or parity compiler is constructed here. In particular L098
and L106 are not automatically repaired by this section.

The precise additional primary input is Joseph R. Shoenfield,
*Mathematical Logic* (Addison-Wesley, 1967), §2.6 pp.21–22 and §3.1,
Tautology Theorem (Post) p.27, Detachment Rule and corollary p.28,
propositional proof pp.28–30, in the
[primary scan](https://w2.cs.uni-saarland.de/op/fullpaper/logics/SHOENFIELD_Mathematical_logic.pdf).
L109 specializes the inspected consequence theorem to fixed
constant-bearing libraries in exactly L108's system. L108, with its
independent step-428 audit, supplies conclusion extraction from an
actual assumption-free four-rule archive. Neither result depends on
this source receiver. LTW remains the translation/extraction comparison
cited above, not a premise that the old presentation is complete.
Only the fixed library is prepared using completeness; the growing
input proof is assembled syntactically from that library.

**6.1 Exact notation and the fixed library.** All displayed schemata
below specify ordered trees. Expand A→B as ¬A∨B, A∧B as
¬(¬A∨¬B), and A↔B as (A→B)∧(B→A), recursively and literally.
Every chain of → is right-associated. These are not additional
connectives or proof tags. Use precisely L108's axiom/rule tags,
including its local true and ¬false axioms. Set

    E_G(A,B) := G→(A↔B).

Prepare the following one finite library ℒ; letters are slots, not
source variables. Each choice indicated by a slash or ± is a separate
member of this fixed finite library.

| Family | Exact schema, before the specified literal expansion |
| --- | --- |
| Identity | A→A |
| Projections | (A∧B)→A; (A∧B)→B |
| Guarded composition | (G→A)→((A→B)→(G→B)) |
| Same positive branch | (X→A)→((X→B)→(X→(A↔B))) |
| Same negative branch | (X→¬A)→((X→¬B)→(X→(A↔B))) |
| Cases | (G→(A∨B))→((A→H)→((B→H)→(G→H))) |
| Guarded reflexivity | E_G(A,A) |
| Guarded symmetry | E_G(A,B)→E_G(B,A) |
| Guarded negation | E_G(A,B)→E_G(¬A,¬B) |
| Guarded OR congruence | E_G(A,B)→(E_G(C,D)→E_G(A∨C,B∨D)) |
| Guarded transport | (G→A)→(E_G(A,B)→(G→B)) |
| Guarded resolution | (G→(P∨A))→((G→(¬P∨B))→(G→(A∨B))) |
| Guarded weakening | (G→A)→(G→(A∨B)) |
| Guarded list laws | E_G(A∨B,B∨A); E_G(A∨(B∨C),(A∨B)∨C); E_G(A∨A,A); E_G(A∨false,A); E_G(false∨A,A) |
| Final discharge | (G→false)→¬G |

Here E_G occurrences are expanded by its definition as well. Thus the
table defines actual finite OR/NOT/constant trees, not an oracle for
an input-dependent family. At most six distinct slots are needed in
any member; unused slots can be included when invoking L109.

Verify their Boolean tautologicity as follows. The stated expansions
have their usual classical truth functions: implication fails exactly
when its antecedent is 1 and consequent 0; conjunction is 1 exactly
when both inputs are 1; equivalence is 1 exactly when its inputs agree.
Identity and projections follow directly. For guarded composition,
the only nonvacuous case is G=A=1, and A→B then forces B=1.
For either same-branch schema, if X=1, its two premises force A=B=1
or A=B=0 respectively, giving equivalence. In Cases, if G=1 then
A∨B=1, and whichever of A,B is 1 forces H=1. For the guarded
equivalence schemata, G=0 is vacuous; G=1 reduces them respectively
to equality, symmetry of equality, preservation by negation and by
the Boolean binary OR function. Transport then preserves truth of A.
For resolution with G=1, failure of A∨B would force P=1 from the
first premise and P=0 from the second, impossible. Weakening preserves
truth of A. Each list law holds for both bits A,B (and C where
present) by commutativity/associativity/idempotence of Boolean OR or
its identity 0, without a restriction on the slot images. Finally
G→false true forces G=0, giving ¬G. These arguments check all slot
assignments, including constants and coincident slot images.

L109 consequently supplies a fixed finite primitive proof δ_H of each
expanded H∈ℒ. Fix these once. One may find them by the terminating
proof enumeration described in L109, with no bound claimed on that
preparation. Their entire lengths and all slot occurrences are constants
independent of F, π, the occurrence groups and Q. No proof search is
performed on a receiving input, and no prepared library depends on that
input. This proof establishes existence of a deterministic compiler
with those finitely many strings built in; it does not exhibit a
serialized/verified choice of the δ_H.

**6.2 Receive actual premises by five primitive records.** Suppose
earlier records have exactly the endpoints A and ¬A∨B. Append:

    B∨A        expansion of the actual A record,
    ¬B∨B       propositional axiom,
    A∨B        cut on B, using the preceding two records,
    B∨B        cut on A, using A∨B and the actual ¬A∨B record,
    B          contraction of B∨B.

For the first cut the arguments are B,A,B; for the second they are
A,B,B. This checks literal matching in the directed cut rule. No
commutation tag, MP tag or residual assumption is present. To use a
curried library theorem, append its entire L109 instance with relocated
internal references and then repeat these five records for each actual
antecedent, in curried order. A library theorem has a bounded number
of antecedents, so this adds a bounded number of records, each copying
only the actual argument/consequent trees. Reusing an old endpoint
means referencing its earlier record, never copying its derivation.

**6.3 Guarded actual-tree operations.** Start from the library instance
G→G, where G is exactly the original C∧U tree in §1. Guarded
composition with a projection proves G→C and G→U, then G→C_j^split
and G→U_s by traversing the actual conjunction paths. At a path step
the projection theorem is separately instantiated and received by
§6.2; neither a path nor its conjunction is a fixed-size slot skeleton.
All trees are written and charged. This covers arbitrary bracketing.

For a source variable x, its selected occurrence r_x lies in one
group s with names z₁,…,z_k. Write the two actual conjunctions in U_s
as A₀ and A₁, so U_s=A₀∨A₁. Starting with A_b→A_b and using the
same projection/composition procedure gives A₀→¬z_i, A₀→¬r_x,
A₁→z_i, A₁→r_x. The two branch schemata yield
A₀→(z_i↔r_x) and A₁→(z_i↔r_x). Cases with the already obtained
G→U_s now yields E_G(z_i,r_x). No assumption A_b or G was opened.
For k=1 the path is empty and the same construction works, with the
two selected leaves identical. The gadget groups remain in U but
need no source-variable equivalences.

Use exactly §3's θ: each occurring source variable maps to r_x and
each proof variable absent from F maps to the existing gadget name y₁.
From each positive occurrence equivalence use guarded negation where
the literal is negative. Combine the resulting equivalences along
the actual OR tree of each original clause using guarded OR congruence.
This gives E_G(C_j^split,θ(C_j)). Together with G→C_j^split,
guarded transport gives precisely G→θ(C_j). All these operations use
the library and §6.2. At most three literal equivalences are combined
for an original nonempty clause. Repeated or opposite literals retain
their separate occurrence leaves until this literal replacement.

Here is also the required paid handling of arbitrary source clause
lists. A local instance of a guarded list law, or its inverse via
guarded symmetry, gives E_G(A,A') for one list rewrite. To lift the
rewrite through an actual OR context, use guarded reflexivity at each
unchanged sibling and guarded OR congruence at every ancestor. The
result is E_G(K[A],K[A']) for exactly that written context K; transport
changes a proved G→K[A] to G→K[A']. No context is supplied to L109
as a new slot-based inference with an unbounded number of premises.
Only this explicit tree traversal is used.

These rewrites suffice to right-associate any nonempty ordered list,
swap adjacent leaves (using association in either direction plus
commutativity on the adjacent pair), and group/delete duplicates by
idempotence. Reversing the moves reintroduces prescribed duplicates
and bracketing. Both false-unit laws cover a singleton pivot with empty
residual: P is converted to P∨false, rather than silently identified
with that different tree. Empty clauses are the literal constant
false. No law deleting a complementary pair is used. Each ordinary
literal-set clause can therefore be put into a distinct-literal list
in a chosen order and later into any supplied list with the same set.
Ordering/comparing literals is performed first on the source names;
apply θ to every displayed intermediate tree when writing the archive.
If θ collapses names or signs, each planned rewrite remains a valid
instance; it is not necessary to recover the source ordering from the
collapsed images.

**6.4 Compile every supplied resolution line.** Validate the supplied
ordinary proof using its actual clause associations and backward
references. For raw repeated-literal lists use the usual underlying
literal set when checking a pivot/resolvent or a weakening; the actual
list trees are received by §6.3. If a format separates list-normalization
records, they use that same procedure. Initial lines reference their
already constructed guarded original clause, using the selected original
clause association when equal clauses occur several times, and normalize
that endpoint to the actual initial proof-line list by §6.3 if needed.

For a resolution line on source variable p, normalize the two parent
trees to p∨A and ¬p∨B, where A and B list the other literals of each
parent set in chosen orders, including opposite pivot signs if present.
When a residual set is empty it is false and the false-unit inverse is
paid explicitly. The required guarded parent records already exist by
induction; their normalization references them and does not unfold
their ancestry. Instantiate guarded resolution with θ(p), θ(A), θ(B)
and receive its two premises by §6.2. Normalize A∨B to the actual
conclusion clause, deleting repeated literals and retaining all
complementary literals. An empty A and B reduce false∨false to false
using a false-unit law. If the permitted format combines resolution
with weakening, add its extra literals as in the next paragraph.

For weakening, append each newly present source literal with the
guarded weakening schema, then normalize to the actual ordered child
list, including its repetitions. A weakening from an empty clause to
a nonempty one starts with false∨L and pays the false-unit reduction.
If both sets are empty, the same earlier false endpoint is sufficient.
Equal clauses or an initial line repeating an old source clause can
likewise store its earlier guarded root index; no alias inference tag
is needed. Process unused source lines as well as used ones. Every
reference is to an earlier actual primitive record, including when a
parent is reused or two premise occurrences have the same index.

Thus induction supplies a root index for G→θ(C_i) for every source
line. The final line has C_i=false, giving the exact G→false.
The Final discharge library member and §6.2 produce exactly R=¬G.
All intermediate names are occurrence names; no source name, auxiliary
slot or assumption remains. Apply the uniform leaf substitution
y_i↦¬y_i to the *entire written archive*. The syntactic replay verified
in L109 preserves every primitive axiom/rule tag and reference and
fixes true and false. It produces an assumption-free four-rule proof
Π ending at exactly

    T=(¬G)[y_i:=¬y_i].

This writes transformed records rather than invoking a substitution
inference on one old endpoint. Its substitution is simultaneous and
does not recursively complement the new leaf images.

**6.5 Exact extraction and unchanged ordered output.** The literal
OR/NOT expansions in §6.1 have the same truth-polynomial v and
translation tr as §§1 and 3. For any expanded formula P, the
structural induction of §3 gives tr(P[¬y/y])=1+v(P): it holds for
both constants, for an atom, and for negation/OR, with conjunction
following by its stated expansion. Hence the endpoint just constructed
has tr(T)=v(G)=f g̃, with the original factor order.

Supply Π, the occurrence alphabet and precisely the original complete
B/placeholder dictionary to L108. All its hypothesis checks have been
made: every line is assumption-free and has one of its exact primitive
tags; it is nonempty; all premise indices go backwards; trees contain
only its connectives, constants and original names. The original input
may have foreign proof names, but θ has eliminated every one before
extraction. L108 yields an affine ABP K with K(y,0)=0 and
K(y,B(y))=f g̃. It supplies its own corrected original-only L035/L036
blocks, so the historical axiom-seed/MP recurrence is no longer the
receiver being invoked.

Retain exactly J from §2, including its singleton formula (1) and
ordered prefix/suffix telescoping (3)–(4). With independently copied
graphs and fresh exterior endpoints form H=K+fJ. Formal substitution
gives H(y,0)=0 and

    H(y,B(y))=f g̃+f(g+g̃)=fg.

The final cancellation is addition in the free F₂ algebra, with both
copies of f g̃ in the same order. No Boolean-only identity of fg, no
common-order injectivity for that product, and no changed consistency
tester is used. Original clause placeholders, source variables and
extensions do not occur. The early empty-source-clause case in §1
still returns the direct zero graph with all dictionaries retained.

For the original-only arithmetic formulas in J and f the repaired
proof can use the same elementary tree construction as L108 §2:
an atom/scalar is a single affine edge (zero may have no path), a sum
uses disjoint parallel child graphs and a product uses disjoint ordered
series child graphs, with fresh exterior endpoints and 1-connectors.
Every path chooses precisely the appropriate summand or pair of child
paths, so induction gives the exact polynomial; each written syntax
occurrence adds only constant records. This applies also to the truth
translation's sums and products. Thus the historical L049 reception
in the source discussion is not a separate input of this replacement.

**6.6 Fresh original-Q ledger.** The following bound is proved for the
replacement archive, rather than carried over from (10). Every source
line/literal count, occurrence/group count and individual name length
is O(Q); the entire written source, pair, provenance and dictionaries
are charged before output. All formulas C,U,G have O(Q) tree nodes,
as do branch conjunctions and each substituted source clause. The
library expands any bounded collection of such trees by a constant
factor. At all later local traversals, the guard G is copied, not
recursively substituted into itself; thus a template argument and
each instantiated primitive-record formula have O(Q) nodes and
O(Q²) full bits, paying each name occurrence pessimistically Q bits.
Library intermediate trees, not just endpoints, satisfy this bound
because their slot occurrence counts are fixed constants.

Conjunction projections and all branch projections take O(Q³) library
uses even if O(Q²) requested paths each cost O(Q). Literal-clause
transfer costs less. For one source clause-list conversion on O(Q)
leaves, at most O(Q²) adjacent leaf exchanges and O(Q²) duplicate
manipulations suffice. Right-association and each adjacent exchange
can conservatively be charged O(Q) elementary association/commutation
moves; false-unit and duplication moves cost less. Thus the looser
bound O(Q³) elementary rewrites suffices for the whole conversion.
One elementary rewrite lifted through a context uses O(Q) instances
of congruence/reflexivity/transport. Consequently O(Q⁴) library uses
per source line suffice, and O(Q⁵) suffice for the complete archive,
including both parent normalizations, the child normalization and
O(Q) weakenings per line. There are O(Q) source lines, all retained
in this accounting. Clause trees during these operations have O(Q)
leaves: parent residual unions and temporary duplicate lists have at
most a fixed multiple of the input-line leaf bound. No accumulated
proof derivation is a template argument.

Each use writes a constant number of L109 records and of the five
detachment records for each of its boundedly many premises. Thus
there are O(Q⁵) primitive records and O(Q⁷) formula/name bits.
Global references cost O(Q⁵ log(Q+2)); entire-archive complementation
adds only a constant node factor and no new names. Full dictionary,
framing and provenance copying fit these bounds after enlarging the
constant. In particular a conservative complete input bound for L108
is

    R=2+|Π|+|occurrence alphabet|+|B/dictionary| ≤ c Q¹².

This exponent has been independently obtained for the new archive.
For construction time, even charging one complete O(Q⁷)-bit archive
scan per one of O(Q⁵) template uses costs O(Q¹²); local copying uses
L109's quadratic input bound on O(Q²)-bit arguments, hence less.
If reference relocation and dictionary parsing use additional scans,
the safe bound O(Q²⁰) covers all this propositional construction.
Library preparation is a fixed constant, never included as a receiving
input parameter. Source/provenance validity checking is syntactic
polynomial work, not a test of UNSAT.

L108 gives |K|≤C R¹⁴≤C'Q¹⁶⁸ and bit time at most C R^b for one
fixed b. For J, at most O(Q) original-only L035 calls have full input
O(Q²), including B. The safe L035 bound O(E⁴) gives O(Q⁹) bits for
their sum before numbering. All independent original-only formula
contexts in J and f cost O(Q³) full bits in total; a further factor
Q safely pays their global numbering, giving O(Q¹⁰) full bits.
This keeps every independently copied correction block and repeated
dictionary, rather than sharing a recursively generated witness.
If d is a fixed exponent for L035's bit algorithm, the J construction
takes a fixed polynomial, for example O(Q^max(22,2d+3)).

Finally reindexing the independently copied K,f,J and writing their
exterior connectors costs at most an extra factor O(log(Q+2)) in
full size, and a quadratic scan of the complete data suffices in bit
time. One deliberately loose pair of common bounds is therefore

    |H| ≤ C Q¹⁷⁰,
    time(H) ≤ C Q^max(340,12b,2d+3).

Both constants/exponents are fixed independently of all source input
and output witnesses. They include complete original/placeholder
dictionaries and all references; the underlying path degree is at most
the explicit edge count. These bounds meet the fixed-polynomial
threshold in original Q. They do not assert an M-only bound, supply
a short π, or give polynomial-time SAT decision. No finite program
check is claimed. The later independent audit is recorded in §7.

**7. Independent critical audit — step 436, 2026-10-23.**

This audits precisely §§1–2 and the step-434 replacement §6 under the
pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-23-four-rule-resolution-repair-critical-audit.md`.
It does not validate the superseded §§3–5 presentation or its retained
streams. The primary inputs remain Shoenfield, §2.6 pp.21–22 and §3.1,
Tautology Theorem p.27, Detachment Rule/corollary p.28, propositional
proof pp.28–30, through the inspected L109 specialization, and the
audited L108 supplied-proof extractor. No additional completeness or
PIT theorem is assumed. L108 proves its own rule recurrences without
invoking this receiver's conclusion; its reference to the historical
right-transition design is not a circular mathematical input.

**Fixed library and primitive reception.** Each expanded library member
has a bounded number of slots and tree nodes independent of Q. Check
its truth function before L109 is invoked: identity/projections are
immediate; composition and transport preserve a true guarded consequent;
the two branch laws force equal bits; Cases selects a true disjunct;
guarded reflexivity, symmetry, negation and OR congruence preserve bit
equality. In guarded resolution, if G=1 and A=B=0, the two premises
would require P=1 and P=0. Weakening and all five list laws are valid
Boolean OR identities, and final discharge is implication to false.
This exhausts the table, including both projection/branch choices and
every list law. Literal expansions retain these truth functions and
are fixed before proof selection. Constant or coincident slot images
are allowed by L109; there is no fresh-name or bounded-depth premise.
The finite selected proofs may be extremely large, but their whole
lengths and slot multiplicities are fixed compiler constants. This
supports a uniform polynomial in receiving input Q, not a uniform
polynomial in an input library or arbitrary tautology.

For actual earlier endpoints A and ¬A∨B, expansion really yields B∨A.
The axiom ¬B∨B and that expansion match cut with pivot tree B,
first residual A and second residual B, giving A∨B. This new record
and the actual supplied implication match cut with pivot tree A and
both residuals B, giving B∨B; contraction gives B. These are exactly
the five stated records, in legal reference order. Curried reception
uses the newly obtained consequent at each subsequent application.
Each library instance imports its entire primitive proof; neither its
endpoint nor detachment is accepted as an additional inference tag.

**Occurrence and source-line induction.** For an actual conjunction
tree, each projection path starts from a proved implication with that
tree as consequent, and composition gives the next actual child.
No assumption is opened. The same process starts separately at each
A_b→A_b for a consistency-group branch. Its selected leaves give the
two signed implications for z_i and r_x; the appropriate branch law
and Cases receive exactly G→(A_0∨A_1). Thus the endpoint is
E_G(z_i,r_x). Singleton groups use zero-length projection paths;
repeated leaf roles are permitted. Negation congruence supplies negative
literals, and OR congruence follows the original clause's actual tree.
Consequently the guarded source clause is exactly G→θ(C_j), even for
repeated, complementary or tautological literal lists. Gadget occurrences
stay in the guard and alphabet; no new unsplit source variable enters B.

For a single list rewrite, reflexivity supplies the unchanged sibling
at each ancestor, and OR congruence supplies the changed parent in its
actual left/right position. At the root guarded transport consumes the
earlier guarded clause. Right-association, adjacent swaps, idempotence
and their inverses connect all written lists with the same literal set;
the two false-unit laws handle empty residuals explicitly. Complementary
literals are never removed by these operations. Normalization is planned
on signed source names before θ. Literal simultaneous instantiation
then preserves every planned tree equality and rule instance even if
foreign names collapse to y_1. No ordering or distinctness test on the
collapsed images is needed.

For resolution, removing just the chosen signed pivot from each source
parent set leaves A and B; the opposite sign, if present in that same
parent, remains. The normalized parents therefore match the two
antecedents of the guarded-resolution schema, and its child is the
union list A∨B before duplicate/list normalization. This remains valid
for tautological parents, coincident transformed premises, empty A or B,
and two empty residuals. A permitted combined weakening then adds its
extra literals. Pure weakening adds source literals individually; from
false, the first false∨L is paid by the false-unit law. Equal clauses
reuse an actual earlier root index without inventing an alias rule.
Every original-clause association is retained, and all supplied lines,
including unused ones, are covered by this induction. Validity of π is
a hypothesis and is checked syntactically; arbitrary extra axiom rules
or extension definitions are not admitted. A final empty clause yields
the exact G→false and hence ¬G. If F already has an empty clause, the
separate zero-graph branch is valid directly; an empty conjunction with
no empty clause cannot have a valid ordinary-resolution refutation.

**Exact free-ring endpoint and correction.** Complementation is a replay
of every written record under simultaneous y_i↦¬y_i. It preserves all
four directed rule patterns, the propositional axiom and both ground
axioms, with the same backward indices. It introduces no variable name
and leaves B entirely unchanged. For any OR/NOT/constant tree P,
the induction tr(P[¬y/y])=1+v(P) has atom case 1+y, constant cases
1=1+0 and 0=1+1, negation case 1+(1+v(A))=v(A), and OR case
(1+v(A))(1+v(B))=1+v(A∨B). Literal conjunction expansion therefore
has v(A∧B)=v(A)v(B) in that order. The exact final endpoint has
tr((¬G)[¬y/y])=v(G)=v(C)v(U)=f g̃.

L026 is used separately in each diagram's order. Every word in v(C)
is increasing multilinear in D's order because clauses have disjoint
occurrence leaves; the dense suffix recurrence has the same property
and Boolean values. Every word in ∏e_s is increasing multilinear in
E's order, with the same group-equality values as E. Those are the two
valid injectivity applications. There is no such application to g̃ or
the different-order product fg. Unreachable states and equal-successor
edges do not affect these polynomial identifications.

For the correction, set z=z_1 in a fixed group. L035 receives only
the original-only graphs A,z and the original pair-once commutator
dictionary, with the Boolean entries retained as unused framing.
After substitution its block in R_s is (1+z)(Az+zA)B'. The other
block is (z²+z)AB'. Their last two contributions cancel because
(1+z)z=z+z², leaving (1+z)AzB'=a_s b_s. This checks the exact
order without exchanging A and z. For k=1, A=B'=1 and the
commutator is zero, so R_s substitutes to z²+z as required.
Each R_s vanishes at zero placeholders. The s-th term of J is the
difference (sum in F₂) of the two adjacent products in the sequence
replacing e_s by t_s from left to right. All inner products cancel
with the identical ordered neighboring product; only g and g̃ remain.
L108 receives the nonempty legal archive, full occurrence alphabet
and unchanged B, giving K(0)=0 and K(B)=f g̃. Disjoint serial/parallel
composition then gives H=K+fJ, H(0)=0 and H(B)=fg. Its exterior
connectors introduce no extra accepting paths; its original-only
formula graphs copy each written child occurrence once. Neither a
quotient-ring equality nor a changed tester enters this calculation.

**Independent original-input ledger.** All counts below use the original
Q=2+M+|F|+|π|, before any archive or graph is constructed. A source
line or temporary residual-union list has O(Q) leaves; duplicate
reintroduction stops at the supplied target list, so intermediate lists
also have O(Q) leaves. Each branch/projection/context tree and G has
O(Q) nodes. Guarded equivalences, curried endpoints and the five
detachment formulas contain a bounded number of copies of these trees.
Repeated congruence does not insert a previously written proof into a
formula: its next slots are the actual changed/unchanged subtrees.
Even long names therefore give O(Q²) bits per fixed-library argument
collection and per instantiated primitive formula. Fixed intermediate
library formulas satisfy the same bound, not just their endpoints.

There are at most O(Q²) requested conjunction paths, each of O(Q)
length. For a list conversion, O(Q²) adjacent swaps/duplicate operations
with O(Q) rotations per operation give O(Q³) elementary rewrites;
lifting each through at most O(Q) ancestors gives O(Q⁴) library uses.
Both parent conversions, the child conversion and at most O(Q)
weakenings fit O(Q⁴) per source line. The O(Q) lines consequently
require O(Q⁵) uses, with a fixed number of primitive records per use.
Global references have O(log(Q+2)) bits (fixed library constants are
absorbed), so O(Q⁷) total archive bits suffice. Complementation adds
only a constant node factor. Complete B and the original dictionaries
already cost at most Q; retaining them with individual library imports
still fits this bound. Thus the deliberately weaker R≤cQ¹² is valid.
Repeated archive scans give O(Q¹²) work; L109's quadratic procedure on
O(Q²)-bit arguments, O(Q⁵) times, costs O(Q⁹). Extra reference and
dictionary scans fit the stated O(Q²⁰) preprocessing allowance.

L108's fixed bound is C R¹⁴, hence C'Q¹⁶⁸. Each of the O(Q) J-block
calls receives complete original-only graphs and dictionary in O(Q²)
bits. L035's O(E⁴) allowance gives O(Q⁹) aggregate block bits before
numbering. All independently written prefix/suffix/formula contexts
cost O(Q³) bits; global numbering fits the stated O(Q¹⁰) allowance
for J. Complete dictionaries at every call and unused supplied input
records have therefore not been silently omitted. Final reindexing
adds at most a logarithmic factor to O(Q¹⁶⁸)+O(Q¹⁰); C Q¹⁷⁰ is safe.
If b,d are the fixed L108/L035 time exponents, their calls cost at
most C Q^{12b} and C Q^{2d+3}. A quadratic scan of the final bounded
output is at most C Q³⁴⁰, also covering the smaller preprocessing
terms. Hence the displayed common time exponent max(340,12b,2d+3)
survives composition without measuring input by its own output.

**Verdict and limitations.** No substantive defect, changed hypothesis
or changed bound was found. This is independent informal validation of
the repaired conditional input, classified as reproduction of the
assessed logical/extraction machinery, not a new source theorem or
certified originality. No serialized library, finite implementation
test or Mathlib match was verified. The main proof argument and direct
mathematical inputs are unchanged. L107/Attempt 036 still stop the old
presentation. L098/L106 repair, short source-proof availability, M-only
bounds, universal W₂, arbitrary ER data and unrestricted SAT remain
separate obligations.

**8. Bounded supplied-endpoint implementation attempt — step 461,
2026-10-24.** This section records an incomplete executable specialization
of §§1–2,6.5, not a new theorem or a verified source-proof compiler. Reuse
the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-24-supplied-four-rule-occurrence-composition.md`.
The precise primary imports and their qualifications remain in this proof
and L108 §1; no additional source theorem or composition identity is imported.

**Received hypotheses and serialization restrictions.** The new
`scripts/four-rule-extraction/occurrence_input.py` receives caller-selected
paths for an ordered width-three F, occurrence annotations, the actual pair,
the supplied proof, its generic request, and a separate digest manifest.
The manifest pins all five input files. Source literal positions carry exact
signs and names; ordered positional binary clause/CNF trees retain their
actual bracketing, with explicit empty-clause/conjunction constants.
Annotations supply one distinct name per literal position including the
four appended gadget occurrences, a permutation giving the original
alphabet, and two fresh unsplit gadget names. Groups use lexicographically
ordered occurring source names followed by those gadget names, retaining
within-group occurrence order. Only L087's canonical dense three-state
numbering, including unreachable states and both final terminals, is admitted;
arbitrary isomorphic or merely Boolean-equivalent testers are outside this
serialization. Every actual transition, order and root is compared literally.
The full input bytes and dictionary positions remain unchanged.

The source conjunction tree is retained and the gadget clauses appended in
the fixed bracketing ((F ∧ gadget₁) ∧ gadget₂); with no source clauses the
conjunction is gadget₁ ∧ gadget₂. The consistency conjunction and each of
its two group conjunctions are explicitly right-associated. Conjunction is
expanded literally as ¬(¬A∨¬B); simultaneous complementation visits old
original leaves only. The resulting exact tree must equal the generic
request goal. These are allowed fixed choices in §§1,6.1,6.4, not a
normalization of a supplied proof endpoint. The parser rejects substituted
source signs, annotations, alphabets, dictionary associations and transitions.

**Construction and independent receiving components.**
`scripts/four-rule-extraction/emit_occurrence.py` calls the audited generic emitter only on a supplied
proof of that endpoint. Separately, its correction constructor reproduces
each original-only A,z₁ call to L035, the singleton-inclusive formula (1),
every independently copied prefix/suffix term of (3), and fJ. Graph labels
use typed original/placeholder indices; caller dictionary list positions and
colliding display names are preserved. A complete graph/recipe archive
retains all those occurrences. The proposed final graph is the disjoint
sum K+fJ of §6.5, with fresh connectors. There is no library preparation,
proof finder, Boolean-equivalence acceptance or new asymptotic ledger.

`scripts/four-rule-extraction/receive_occurrence.py` imports no emitter or correction constructor.
It reconstructs the fixed recipe from the received occurrence groups,
checks typed graphs, endpoints, acyclicity and all copied partitions and
ordered connectors, and uses L108's bounded backward free-word evaluator
on every correction graph in free/zero/B-substituted modes. It compares
the complete formal W, R_s and J identities with the targets in §2, and
compares the actual D graph with v(C). The proposed full receiver separately
receives all K roots/blocks, pins the reread K bytes to that verdict and
to the original occurrence caller's proof text/digest/dictionary, and
checks both full H identities against the unchanged actual f,g graphs.
Its success branch has **not been executed on a valid occurrence proof**.
The shared input parser and new code still require separate critical review.

**Completed finite evidence and stopping boundary.** Reproduce the bounded
diagnostics by importing `scripts/four-rule-extraction/test_occurrence.py`,
assigning its OUT to a fresh directory, and calling main(), using the exact
command in the work note; do not overwrite an existing archive.
Canonical final evidence is `scripts/four-rule-extraction/output-461/final/`;
the four executed source snapshots are in
`scripts/four-rule-extraction/output-461/final-executed-sources/`.
Earlier runs are preserved. A mutation-test change
during the first execution and the later K-binding repair are explicitly
qualified; only the final run matches all four current source hashes.

Five local source/annotation/pair fixtures cover opposing units, singleton
groups with mixed signs, repeated mixed literals, the empty source and an
empty source clause. All five front ends and complete ordered-correction
components pass. Four have nonzero substituted fJ, so the correction is
not tested solely through the zero-clause shortcut. Reusing step 459's
independent forward integer-coefficient arithmetic checks **783 complete
graph/mode polynomials** against the backward evidence. These arithmetic
comparisons include all free words, not selected words or Boolean samples.
All **36** malformed/binding/resource cases reject. Direct helper tests
also reject an actual other-caller generic K archive, changed proof text,
changed digest and reordered dictionary; their sole successful helper call
is not an occurrence-proof acceptance. All 224 files in outputs 457/459
retain their hashes. Full graphs, words, targets, input metrics, rejection
reasons and source hashes are retained on disk.

All five diagnostic proof files are explicitly invalid: their headers name
the requested endpoint but their final line is true. They reject at the
literal endpoint check. **Zero valid supplied endpoint proofs were received
and zero full positive compositions were verified.** Neither the successful
front end/correction checks nor a generic byte-binding test supplies such
a proof. The attempted implementation stops with its complete receiving
success branch unverified; no proof/library synthesis is substituted.

The largest retained correction aggregate is 4,338 records / 2,000,000;
its largest graph certificate is 56,056 bytes / 200,000,000. Backward
diagnostics use at most 481,182 multiplication pairs / 100,000,000,
25,476 transient words / 1,000,000, word length 21 / 256 and 140,348
stored traversal words / 20,000,000. Independent forward maxima are
1,629,376 multiplication pairs, 21,230 transient words, length 21 and
668,574 stored words against the same respective caps. Per-file output
byte bounds, including larger complete word receipts, are recorded in
`scripts/four-rule-extraction/output-461/final/output-byte-bounds.json`;
individual input byte/depth/name/dictionary
caps and the separate original pre-output byte measure are retained.
These measured component bounds do not bound all live Python objects or
total interpreter work; constructor counters remain bounded claims.
Trusted caller paths, SHA collision resistance and the generic checker's
separately uncapped second read remain qualifications. No all-size program
theorem, short-proof availability, M-only bound, universal W₂, arbitrary ER
data, certified originality or SAT consequence is established.

**9. Independent occurrence-component audit — step 464, 2026-10-24.**
This audit receives exactly §8's finite interface under the pre-existing
SPECIALIZE assessment
`drafts/literature/2026-10-24-occurrence-receiver-component-audit.md`.
The mathematical inputs are L087, §§1–2 and 6.5 above, L026's single-order
injectivity, audited L035/L036 and L108's supplied-proof interface. The precise
primary citations and their restricted roles above are reused; no theorem is
reproved, no new lemma or mathematical script is introduced, and no general
formula/circuit conversion is inferred. All four occurrence modules were read
completely and compared with their executed snapshots. Eight reused generic
parser/evaluator/constructor/checker modules match step 459's recorded hashes.

**Shared boundary review.** Strict JSON parsing, exact schemas and type-sensitive
equality precede reception. Source literal signs are Boolean; positional leaves
are integers excluding Boolean aliases. A positional tree visits exactly
0,...,k−1, so its actual bracketing and every occurrence are retained. Empty
clauses/conjunctions have the specified constants. The appended gadget names
are distinct and absent from the source; all occurrence names, including the
four gadget occurrences, are distinct. The alphabet is a permutation of those
names. Group order is sorted occurring source names followed by u,v; within-group
order is literal occurrence order. The complete typed dictionary retains caller
list positions even with original/placeholder display-name collisions.

For D, state 0 is absorbing failure. At a first literal a live state starts
with accumulated bit 0; otherwise its bit is state−1. OR with the signed input
updates it; at a clause end false goes to failure and true to live state 1.
For E, a group start overwrites any live remembered bit and later unequal bits
go to failure. Both final transitions send precisely the live states to terminal
1. An empty source clause sets D's root to failure. Exact pair comparison checks
all 6q transitions, including unreachable states and equal-successor branches,
not merely the accepting behavior. The gadget guarantees q≥4 and distinct orders.
This matches L087's stated machines. As an additional independent finite check,
direct table traversal on all 288 assignments across the five retained fixtures
agrees with the raw signed-clause/equal-group predicates. This scalar check is
separate from, and does not replace, the free-ring comparisons below.

The source conjunction bracketing survives gadget appending. Literal AND
expansion uses ¬(¬A∨¬B), and complementation visits old leaves once, including
under old negations, while leaving constants unchanged. Exact equality to the
request goal precludes replacement by a Boolean-equivalent endpoint. Independent
forward translation of each entire requested endpoint matches the complete
saved f g̃ polynomial. This tests the endpoint identification, not derivability:
every supplied diagnostic proof still ends at true and is invalid.

**Ordered graphs and complete evidence.** Both the code and every retained graph
were checked against (1)–(4). W receives exactly original-only A,z₁; R retains
(1+z₁)W B' + σ_(z₁) A B', including A=B'=1 for a singleton. Each J summand
retains its earlier t factors and later e factors in their displayed order.
The receiver verifies fresh contiguous child partitions, every interior edge
and every connector, including empty products/sums; endpoints and labels receive
strict graph checks. It computes complete zero/substituted W and R identities,
J(B)=g+g̃, and f=v(C). No Boolean-zero inference for the different-order fg
is used. The outer-copy component passes and its changed connector rejects.

Fresh backward evaluation matches every complete saved graph polynomial and
target after JSON serialization. Independently reused forward integer-coefficient
evaluation matches both saved forward and backward evidence for all **783**
graph/mode pairs. Four fixtures have nonzero fJ. All **36** recorded rejections
replay, including the five invalid endpoint proofs. Complete comparisons, case
receipts, actual/required bounds and source/artifact hashes are in
`scripts/four-rule-extraction/output-464/verified/verification.json` and its five
case receipts. These checks read the complete words in
`scripts/four-rule-extraction/output-461/final/`, not previews or selected terms.
The final archive is read only, and its hashes are recorded; the rejection replay
also checks unchanged before/after hashes. All 224 previously pinned files in
outputs 457/459 are unchanged, as recorded in
`scripts/four-rule-extraction/output-464/dependency-preservation.json`.

Two audit-harness interruptions are preserved: the first compared in-memory
tuple tokens with saved JSON list tokens; the second compared an error containing
a relative path with the saved absolute path. Comparing serialized results and
replaying with absolute paths resolves those mismatches without changing production
code, polynomial evidence or rejection conditions. Both failure artifacts remain;
the final receipt has no unresolved failure. No archive-writing driver was rerun.

**Provenance and limits.** The occurrence manifest pins all five caller files.
Generic reception independently checks the supplied proof/request and binds K's
source text and dictionary. The later K read must hash to that checked receipt
and H's K digest. `bind_K` then compares its complete source text/digest and typed
dictionary with the original occurrence context. Because the proof text contains
the exact header, this also retains the original endpoint/alphabet across reads.
The finite changed-text/digest/dictionary and foreign-K tests reject. This is
conditional on trusted caller paths and SHA256 collision resistance, and does
not certify an unexecuted positive K+fJ branch.

Measured backward maxima remain 481,182 multiplication pairs, 25,476 transient
words, length 21 and 140,348 stored traversal words; forward maxima are 1,629,376,
21,230,21 and 668,574 respectively. The required bounds are 100,000,000,
1,000,000,256 and 20,000,000. Independent endpoint translation uses at most
22,940 multiplication pairs and 22,000 transient words. Graph/input preflights
and the 4,338-record aggregate remain within §8's bounds. These counters do not
bound all interpreter work or simultaneously live objects. In particular the
literal checker's second source read remains separately uncapped; digest checking
after that read does not bound its resource consumption.

**Verdict.** No substantive defect was found in the audited finite components.
This establishes local verification evidence for §8, not progress beyond the
assessed mathematical sources. **Zero valid endpoint proofs and zero complete
positive compositions remain verified.** Full supplied-proof acceptance,
all-size executable resources, short-proof availability, M-only bounds,
universal W₂, arbitrary ER data and unrestricted SAT remain unresolved.
The abstract argument and direct DAG inputs are unchanged. Full matching Mathlib
coverage remains not checked. Attempts 036/037/038 are preserved.

## Mathlib

Full matching coverage of this transfer, the Frege extraction, the
explicit affine-ABP construction and its binary/time ledger: **not
checked**. No absence or machine-verification claim is made. Precise
primary imports and their restricted roles are stated above. The
ordered tester correction and graph reception are proved here rather
than inferred from Boolean equality of the two-order product.
