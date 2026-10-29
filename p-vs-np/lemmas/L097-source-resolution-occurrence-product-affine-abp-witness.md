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

**10. Direct retained empty-clause endpoint — step 470, 2026-10-24.**
This is one finite reproduction under the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-24-empty-clause-structural-proof-construction.md`.
It supersedes §§8–9's historical zero count of verified endpoint proofs only;
zero full positive compositions are still verified. It proves no new general
proof-availability or resource theorem and does not reopen Attempts 036/037/038.

**Exact hypotheses and conclusion.** Receive only the retained
`scripts/four-rule-extraction/output-461/final/empty-clause/` source,
annotations and request. The source is one empty clause. Occurrence rows are
[], [y0,y1], [y2,y3], with alphabet [y3,y2,y1,y0]; the complete ten-entry
dictionary retains its original order and colliding display names.
There is an assumption-free 31-record proof of that request's exact goal
using only L108's primitive tags, with no names outside that alphabet.
This is a checked finite endpoint construction, not extraction or composition.

**Full structural proof.** Write N(X)=¬X, O(X,Y)=X∨Y and
A(X,Y)=N(O(N(X),N(Y))) as literal tree abbreviations, not proof tags. Put

    g₁ = O(N(y0),N(y1)),
    g₂ = O(N(N(y2)),N(N(y3))),
    u₀ = O(A(N(N(y0)),N(N(y2))),A(N(y0),N(y2))),
    u₁ = O(A(N(N(y1)),N(N(y3))),A(N(y1),N(y3))),
    C = A(A(false,g₁),g₂),    U = A(u₀,u₁),
    T = N(A(C,U)) = N(N(O(N(C),N(U)))).

These are the actual complemented gadget/consistency trees of §8, including
all occurrences and constants. Expanding the displayed definitions gives
literal equality to the unchanged request goal; no negation is cancelled.

The sole imported structural operation is Shoenfield, *Mathematical Logic*
(1967), §3.1 Lemma 1, printed p.28
([primary scan](https://w2.cs.uni-saarland.de/op/fullpaper/logics/SHOENFIELD_Mathematical_logic.pdf)):
from an actual proved O(X,Y), append axiom O(N(X),X), then cut on X to
obtain O(Y,X). This is two literal primitive records. To append a right
disjunct Y to a proved X, expansion gives O(Y,X), and those two records
give O(X,Y). This costs three records. Arbitrary tree arguments, including
constant-bearing ones, satisfy the primitive schemes without a freshness
condition; this is the necessary local specialization, not a new rewrite rule.

The assessment explicitly requires a standalone double-negation bridge;
the source's contextual auxiliary (B), pp.29–30, does not supply it with an
empty context. From an actual earlier proved X, append exactly:

    j: O(N(N(X)),N(X))                     axiom on N(X),
    k: O(N(N(X)),X)                        expansion of X,
    h: O(N(N(N(X))),N(N(X)))               axiom on N(N(X)),
    p: O(X,N(N(X)))                        cut k,h on N(N(X)),
    q: O(N(X),N(N(X)))                     cut j,h on N(N(X)),
    r: O(N(N(X)),N(N(X)))                  cut p,q on X,
    s: N(N(X))                            contraction of r.

For each cut, the second premise's left argument is literally the negation
of the first premise's left argument, and the displayed residuals are in
the required order. All references point backwards. Thus these seven records
prove the bridge directly in the admitted rules; no contextual operation or
semantic normalization is used. This finite expansion is required because
the cited source does not give a serialized standalone operation here.

Start with the ground axiom N(false). Append N(g₁) on the right by the
three-record operation, then apply the seven-record bridge. The result is
N(N(O(N(false),N(g₁)))) = N(A(false,g₁)) literally. Append N(g₂) and
apply the bridge again to obtain N(C). Append N(U) and apply it once more
to obtain exactly T. Off-branch trees are copied verbatim into each operation.
The ground axiom plus three ten-record stages gives 31 records. Every
operation is expanded into primitive records; there are no assumptions,
auxiliary variables, substitution inferences, association changes or new tags.

**Complete executable evidence and bounds.** Reproduce in a fresh output
directory with
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/construct_empty_endpoint.py`.
The default output `scripts/four-rule-extraction/output-470/` is retained;
the driver refuses to overwrite it. It saves complete records incrementally
and would save a checked partial prefix and exact failure on construction
failure. The complete successful `proof.jsonl` passes the independent
`scripts/parity-four-rule/checker.py` byte checker, then the unchanged strict
`parameterized_input.request` preflights and checker. No extraction is called.
The full receipt in `scripts/four-rule-extraction/output-470/verification.json`
reports no failures:
1 not-false, 6 expansion, 9 axiom, 12 cut and 3 contraction records.
The proof has 1,628 written formula nodes; including the requested goal gives
1,696 aggregate nodes / 100,000. Other actual/required values are 31 records
/ 1,000 attempt limit (10,000 interface limit), 13,453 source bytes /
2,000,000, 1,643 request bytes / 2,000,000, depth 16 / 64, 4 alphabet names
/ 256, 10 dictionary entries / 32,896 and maximum name bytes 4 / 4,096.
The strict parser also enforces the unchanged JSON-depth cap of 160.

The original four retained source/annotation/request/diagnostic-proof files
are compared byte-for-byte after execution and remain unchanged; their
digests are saved in `scripts/four-rule-extraction/output-470/retained-inputs.json`.
The original request binds the invalid diagnostic proof. A fresh
`scripts/four-rule-extraction/output-470/request.json` changes
only `source_sha256` to bind the new proof bytes, whose SHA256 is
`deedd552999e2bde40e39f2aa050b8632e43804e83639eb0ed14570644eacd81`.
The goal, alphabet and entire dictionary are exactly equal to the original
request, including list positions and display-name collisions. Its old
diagnostic proof is neither relabeled as valid nor overwritten. The fresh
digest is an explicit caller request for these new bytes, not acceptance
under the old digest or an external authorization guarantee.

**Qualifications.** This supplies one positive endpoint input for a later
receiver test. It has not supplied K or checked a positive K+fJ composition.
Since the source contains an empty clause, f=0 by §1; even successful future
composition on this case cannot test a nonzero fJ correction. General
supplied-proof availability, total interpreter resources, trusted caller
paths and remaining SHA bindings, original-only correction qualifications,
M-only/W₂/ER and unrestricted SAT remain open. The byte-boundary issue noted
historically in §§8–9 has its separate repair/audit in L108 §§12–13, without
a total-resource conclusion. Full matching Mathlib coverage of this finite
transcript/bridge is not checked. No novelty beyond the assessed sources is
claimed; DAG inputs and the abstract argument are unchanged.

**11. Supplied positive-input resource stop — step 471, 2026-10-25.**
Under the unchanged pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-24-supplied-four-rule-occurrence-composition.md`,
the existing bounded emitter was invoked on exactly §10's legal 31-record
proof. No theorem, proof constructor, production receiver, cap or dictionary
was changed. This is a finite reproduction attempt, with an informative
negative executable outcome, not a disproof of the conditional theorem.
The precise primary imports and applicability arguments of §§1–2,6.5 and
L108 remain unchanged; no reproof or new external result is used.

**Inputs and execution.**
`scripts/four-rule-extraction/receive_positive_occurrence.py` copies the
retained step-461 empty-clause source, annotations and pair byte-for-byte,
and the step-470 proof and fresh request byte-for-byte, into fresh
`scripts/four-rule-extraction/output-471/inputs/`. A new local caller manifest
binds those five files. The occurrence provenance/endpoint front end and
the independently literal-checked generic request both pass. The proof has
31 records, 13,453 bytes / 2,000,000, depth 16 / 64 and aggregate
source/request nodes 1,696 / 100,000, with four originals and the unchanged
ten-entry dictionary. Full pre-output input measure is 16,366 bytes,
including the 422-byte manifest and the five separately charged files.
The complete preflight receipt is `output-471/preflight.json` under the
same script directory.

The generic extraction stops at zero-based line 7, a cut with references
[5,6], before attaching its prefixed-commutator seed. Its outer-graph
preflight requires **2,008,364 records / 2,000,000**. The retained outer
graph has 847,199 vertices and 1,059,040 edges, totaling 1,906,239 records;
the unattached seed has 45,388 vertices and 56,735 edges, totaling 102,123.
Their sum plus two connectors exceeds the cap by 8,364. Eleven seed/transition
blocks for lines 0–6 have been attached; all 31 source-line vertices remain
allocated. The constructor reports 83 commutator calls, a bounded counter
claim rather than a measurement of total interpreter work.

**Complete saved failure and independent check.** The driver saves full
relevant exception frames rather than just a count or graph preview:
`output-471/failure-frame-2.json` contains the complete outer graph, block
inventory, current source record and pending seed;
`output-471/failure-frame-3.json` retains the complete attachment operands.
`output-471/failure.json` records the exact preflight and traceback.
No K or H certificate was emitted. The driver refuses an existing output
directory; reproduce only with a fresh OUT rather than overwriting this run.

`scripts/four-rule-extraction/verify_positive_stop.py` imports neither graph
constructor nor algebra verifier. It reads both complete saved graph states,
checks their equality across the two frames, all endpoints and labels,
acyclicity, every retained block partition/interior/connector, and the complete
record counts. It independently obtains the exact rejected sum above. Its
full receipt is `output-471/stop-check.json`, with no failed structural check.
Seven pinned original files and all ten recorded source hashes remain unchanged;
the copied inputs equal their originals and meet the manifest digests. The
driver's source-path existence filter omitted the actual marked-edge module
because its candidate path was misspelled; the independent receipt explicitly
pins `scripts/alternative-abp-commutator/check_marked_edges.py` as a supplement.
This does not change the code executed or the measured resource stop.

**Boundary and route decision.** No partial-K polynomial correctness is claimed:
the partial graph is not a complete L108 archive, even though it is structurally
valid. Neither full root/block arithmetic reception nor K+fJ composition was
reached, so the number of verified positive compositions remains zero.
The other diagnostic arithmetic caps were not exercised here. Empty-clause
f=0 still prevents testing nonzero correction. This failure stops this exact
unoptimized extraction/input/cap combination; it neither refutes L108/L097 nor
bans every supplied-proof receiver. Attempts 036/037/038 remain parked.
A proposed constant-aware original-only translation is a different executable
representation mechanism requiring its own separate literature approval before
any derivation or implementation. No benefit from it has yet been established.
Trusted caller paths, remaining SHA bindings, total interpreter resources,
general proof availability and unrestricted SAT remain unresolved. Full matching
Mathlib coverage of this finite stop is not checked. The abstract argument and
direct mathematical DAG inputs are unchanged.

**12. Scalar-aware original operands: later fixed-cap stop — step 473,
2026-10-25.** This is a finite REPRODUCTION under the prior SPECIALIZE
assessment `drafts/literature/2026-10-25-constant-aware-occurrence-translation.md`.
It tests only the unchanged §10 proof and §11 caller data. It neither changes
the conditional theorem nor supplies a full positive composition. The scalar
mechanism passes §11's zero-based record-7 stop, then fails at record 22.
The exact combination of scalar folding, unchanged correction constructors,
this input and these caps is stopped. Attempt 039 and all its evidence remain
valid for the earlier unoptimized representation.

**Implementation and preservation argument.** The isolated
`scripts/four-rule-extraction/constant_translation.py` adapter replaces only
the generic emitter's original-only formula translation, in a fresh process.
Neither production file nor L035/L036 constructor is edited. Its internal
nodes are tagged scalar 0/1, original index, ordered product and one-plus.
Input names cannot be mistaken for scalar tags. At an original leaf the graph
has the corresponding original edge; true and false give 0 and 1. At a
negation, a scalar c gives 1+c in F₂; every other child retains one-plus.
At a product, a scalar zero child gives zero, a scalar unit child is removed,
and two remaining nonconstant children retain their order. These cases also
cover both scalar children. There is no nonconstant cancellation search,
Boolean idempotence, factor permutation, or rewriting of source trees.

Here is the necessary applicability justification, rather than an invocation
of LTW's different constant-free conclusion. Interpret the internal tags in
the free associative F₂ algebra. By induction on the unchanged source tree,
the children have their exact tr values. Each replacement just listed is one
of 1+0=1, 1+1=0, 0u=u0=0, or 1u=u1=u; otherwise the same ordered operation
is retained. Thus the internal expression has exactly tr of that tree.
The graph builder uses distinct two-vertex scalar/original graphs, independent
serial copies for products, and the original one-branch-plus-child graph for
one-plus. A path in a product uses the two child paths in order; a path in a
sum chooses its one branch or child branch. Finite distributivity therefore
gives the internal expression's polynomial at each builder node, including
zero/no-path cases. Both inductions preserve formal polynomials, rather than
Boolean functions. Every resulting graph is acyclic with the same exterior
endpoint convention, so L035/L036 still apply to its original-only operands.

The imported conversion is Raz–Shpilka, *Deterministic Polynomial Identity
Testing in Non Commutative Models*, author-hosted 16-page manuscript,
§2.1 pp.4–5, Lemma 2, complete Step 1 (revision date unestablished),
[primary PDF](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf).
Only its ordered serial/parallel component conversion is used; its complete
homogeneous lemma's zero-free-term premise is not imposed on arbitrary
operands here. The scalar laws are field/ring laws. LTW, *Characterizing
Propositional Proofs as Non-Commutative Formulas*, SIAM J. Comput. 47(4)
(2018), DOI 10.1137/16M1107632, Definition 1.3 p.6 and Lemma 4.8 p.26 in
the assessed 40-page author manuscript, remains a scope comparison, not an
arbitrary-operand optimizer theorem. The two elementary checks above justify
this finite integration's applicability; they claim no new normalization or
resource theorem. Correction identities are the unchanged L035/L036 inputs.

**Exact execution and independent evidence.** Run in a workspace without the
retained `scripts/four-rule-extraction/output-473/` using
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/run_constant_occurrence.py`.
It reuses §11's caller/preflight/failure driver with a fresh OUT and installs
the adapter. Its `run-scope.json` records this exact target and supplementary
source hashes; the reused driver's preflight still names its original receiver
target. All source, annotation, pair, proof, request and manifest bytes retain
the original caller contracts. The 31 records, trees, original alphabet,
all ten ordered dictionary entries, block roles, multiplicities and all source
root vertices are retained. No unused source record or dictionary entry is
removed. All caps and the occurrence correction J recipe are unchanged.

The run stops while constructing record 22's axiom Booleanity seed, in a
nested L035 call. Full pending operand graphs are in
`output-473/trace/event-00201.json` and `output-473/failure-frame-7.json`.
Each has 87 vertices and 114 edges (201 records). Independent counts give
p=114²=12,996, q=48 and the unchanged L035 exact-copy ledger

    N = 2+2p(87+87) = 4,522,610,
    M = 2p(114+114)+4p+48 = 5,978,208.

Thus N+M=10,500,818 required records exceeds 2,000,000 by 8,500,818,
before L035's copy loops. The retained outer graph has 206,142 vertices,
263,751 edges and 469,893 records, with 45 seed/transition blocks for
source lines 0–21. The current axiom seed is incomplete. Neither K nor H
was emitted, and no partial-K polynomial acceptance is claimed.

`verify_constant_translation.py` imports neither emitter, adapter nor correction
constructor. It reads all 202 complete trace events, transports the actual
graphs through the unchanged typed dictionary, checks original-only labels
and topology, and uses the independent backward free-word receiver arithmetic.
All 66 translation calls through the interrupted axiom match the complete
ordered list reconstructed from the actual source, and each graph equals the
arithmetic translation of its unchanged tree. For each Boolean input it
independently normalizes labels/deletes outgoing sink edges and reconstructs
the exact sequence of atom/suffix and prefixed-suffix operand pairs, including
dead edges and coinciding suffix endpoints. All actual nested operands match
that recipe. Direct correction inputs match the actual translation graphs.
It checks every saved commutator/Boolean output's free polynomial and both
zero/substituted contracts against these independently evaluated inputs.

There are 60 received commutator input pairs, 59 completed commutator outputs,
nine Boolean inputs and eight completed Boolean outputs. The missing outputs
are exactly the failed call at event 201 and its Boolean parent at event 196;
their contracts are not verified. The pending pair's actual polynomials,
retained completely in `trace-received-prefix.json` event 201, are 1 and the
listed 48-word original polynomial; its commutator target is zero. This
observation is a receiver calculation, not an optimizer decision or a license
to replace that graph inside this run. Trace arithmetic uses 1,856,251
multiplication pairs / 100,000,000; at most 49 words / 1,000,000, word
length eight / 256 and 112,888 stored words / 20,000,000. The final
`trace-verification.json` explicitly has accepted=false and
verified_trace_prefix=true. An initial diagnostic used the wrong hard-coded
pending Boolean event number (88 rather than 196); it failed only after
checking all 202 events. Its complete failed receipt is preserved as
`trace-verification.initial-failure.json`. Correcting that bookkeeping assertion
and replaying yields the reported prefix receipt; no arithmetic failure is hidden.

`verify_constant_stop.py` independently reads the complete failure-frame outer
graph and pending operands. Without constructors or arithmetic it checks all
labels/endpoints, acyclicity, fresh block partitions/interiors/connectors,
all 22 completed source lines, absent K/H, and the exact rejected N+M above.
Its full `stop-check.json` receipt also verifies unchanged source/input hashes
and byte equality of all five copied caller files with their retained originals.
Both verifier commands use `PYTHONDONTWRITEBYTECODE=1 python3` followed by
their script path and refuse existing final receipt paths. Complete trace
graphs, arithmetic evidence, failure frames and receipts remain in output-473.

**Limitations.** This is an informative negative bounded implementation
outcome, with local progress past the earlier stop, not progress beyond the
assessed mathematical sources. No completed K/H, source-root or full-composition
arithmetic acceptance exists. Incomplete constructors are not assigned their
promised identities by this diagnostic. This f=0 case still cannot test
nonzero correction. Trusted caller paths/remaining SHA assumptions, general
proof availability, total interpreter resources, M-only/W₂/ER transfer and
unrestricted SAT remain unresolved. Full matching Mathlib coverage of this
finite adapter and negative run is not checked. The abstract argument and
direct DAG inputs are unchanged.

**13. Isolated path-trimming test of the failed pair — step 475,
2026-10-25.** This finite REPRODUCTION uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-25-failed-operand-path-trimming.md`. It supplies
the approved two-operand preservation/cap test only. It does not integrate
trimming into extraction or change the conditional theorem.

**Hypotheses and source input.** Use exactly §12's complete event-201
original-only operands, with Boolean parent event 196, unchanged caller
proof/request from step 470, and source/annotation/pair data from step 461.
Their receiving convention is L035's finite affine DAG with designated,
possibly internal or coincident endpoints; parallel occurrences and empty
paths are retained. The source mechanism is Raz–Shpilka, *Deterministic
Polynomial Identity Testing in Non Commutative Models*, author-hosted
16-page manuscript, Definition 1 and Lemma 2 Steps 3 and 5, printed pp.4–6,
[primary PDF](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
revision date unestablished, inspected in step 474. Import only its pruning
mechanism, already used for layered components in L041. Its formula-size,
homogeneity and zero-free-term conclusions are not asserted for these
operands. Step 4's constant-edge rewiring is not used. The receiving-model
justification below is necessary because these graphs have arbitrary roots,
constants and empty paths; it does not reprove the source's formula theorem.

**Conclusion.** Both complete ordered polynomials survive the filter.
The first operand becomes 2 vertices/1 edge and the second 86 vertices/112
edges. The unchanged L035 exact preflight requires 45,474 records, below
2,000,000. This is local implementation progress using known mathematics,
not an advance beyond the inspected sources or a complete K/H receipt.

**Proof of applicability and exact operation.** For a designated pair s,t
in an acyclic graph, let R be the vertices reachable from s, including s,
and C those from which t is reachable, including t. If t is reachable,
retain R∩C and every original edge whose endpoints both lie there.
Every s-to-t path lies entirely in this induced graph. Conversely every
path in the induced graph is an original path, so this gives a bijection
of accepting paths with their original edge occurrences. In particular
incoming edges at s or outgoing edges at t cannot contribute an extra
accepting path: returning to either designated endpoint would create a
cycle. More precisely an edge u→v belongs to an accepting path iff
s reaches u and v reaches t. Concatenating those paths with the edge
cannot repeat a vertex, since such a repetition would give a directed
cycle. This is equivalent to retaining both endpoints in R∩C.

Labels are copied verbatim and accepting path edge order is unchanged.
Consequently every ordered label product is identical, and summing them
in the free associative F₂ algebra preserves the whole polynomial,
including constant products, parallel-edge multiplicities, zero labels
and cancellation between paths. No nonzero-label or Boolean promise is
needed. If there is no s-to-t path, retain just the two distinct designated
vertices and no edges: both polynomials are the empty sum zero. If s=t,
acyclicity makes R∩C={s} with no edges; both graphs have exactly the empty
accepting path of value one. This includes an edgeless graph. Thus there
is no deletion of the empty path or degree-zero component.

For internal numbering, sort retained old vertex identifiers and number
them densely, transporting both endpoint references. Retain edges as a
subsequence of the original edge list, with unmodified label lists. Save
the full old-to-new and inverse vertex maps and original edge indices.
Only these internal operand vertices are renumbered. Original variable
and placeholder names, the full ordered dictionary and caller data are
retained; no supplied proof root is renumbered or source record removed.

For the first saved operand only old vertices 1,86 and edge 113 survive:
the new graph is 1→0 labelled 1, with source 1, sink 0. This follows from
reachability, not recognition of a scalar polynomial. For the second,
old vertices 1,…,86 survive and exactly original edges 0 and 111 are
deleted. Its source becomes 85 and sink 0. All other 112 edge occurrences
retain their relative order. Both still meet L035's hypotheses. Their
full received polynomials equal §12's saved event-201 values, respectively
1 and the complete 48-word polynomial; equality is checked for each
operand, not inferred from their zero commutator.

The first retained operand has no original-variable label entry. Therefore
L035's q=0, but all p=1·112=112 branches remain charged. The unchanged
four-copy ledger gives

    N = 2+2·112·(2+86) = 19,714,
    M = 2·112·(1+112)+4·112+0 = 25,760,
    N+M = 45,474 ≤ 2,000,000.

The original full pair still requires 10,500,818 records. No branch is
omitted because its central label is empty, and no label combination,
constant-edge contraction or semantic scalar folding is performed.

**Complete finite evidence and reproduction.** In a workspace without the
retained `scripts/four-rule-extraction/output-475/`, run, in order,
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/trim_saved_operands.py`
and `PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/verify_path_trimming.py`.
Both refuse existing final output/receipt paths. `trimmed-pair.json` saves
both complete original/trimmed graphs, all maps, full alphabet/dictionary,
caps, exact old/new ledgers, boundary fixtures and preservation hashes.
The filter uses forward/reverse adjacency traversal and no polynomial
evaluator or correction constructor.

The independent receiver imports neither filter, emitter nor correction
constructor. Boolean all-pairs transitive closure checks the complete
retained vertex and edge sets; exact occurrence maps check every label,
parallel edge, endpoint and original edge position. The audited typed
backward receiver evaluates both full original and trimmed graphs in the
free algebra, comparing the complete values with the saved event-201
receipt. Its separate reconstruction of L036's normalized parent-196
graph and nested schedule matches all three actual pairs at events
197,199,201. Both event-201 originals also match every failure-frame-7
operand record. An independent Counter-based computation reproduces the
original rejected and new passing ledgers. This tests the unchanged exact
preflight formulas; no L035 witness graph is constructed or received here.

Six small boundary fixtures also pass complete topology/map/polynomial
reception: internal endpoints with ordered variable products, parallel and
zero-labelled edges; interior coincident roots; distinct no-path roots;
an edgeless coincident root; parallel constant cancellation; and affine
labels with repeated entries. These diagnostics supplement the path
bijection above; they do not establish its all-input statement by sampling.
`reception.json` stores all full polynomials and an empty failure list.
The run uses 3,643 multiplication pairs/100,000,000, at most 49
words/1,000,000, word length eight/256 and 1,045 stored words/20,000,000.
The complete caller proof is literal-checked through the unchanged
immutable-byte request interface. Every source/annotation/pair/proof/request
file matches its retained original byte-for-byte and its original manifest;
the recorded input and implementation hashes remain unchanged.

**Limitations and Mathlib.** Only the exact local discriminator passed.
No integrated extraction, Boolean-parent completion, K/H certificate,
all-root/all-block reception, or positive K+fJ composition was attempted.
Future integration changes internal correction graphs and needs separate
source/receiver-scope assessment; preservation of operand polynomials alone
does not verify that implementation. All later caps may still fail.
This f=0 input cannot test nonzero correction. Trusted paths/remaining
SHA provenance, total interpreter resources, general certificate availability,
M-only/W₂/ER transfer and unrestricted SAT remain unresolved. Attempts
039/040 and their fixed-representation stops remain valid. Full matching
Mathlib coverage is **not checked**; no absence claim is made. The abstract
argument and direct mathematical inputs in the DAG remain unchanged.

**14. Integrated operand trimming: later nonzero-pair cap — step 477,
2026-10-25.** This is one finite REPRODUCTION implementation attempt under
the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-25-path-trimming-extraction-integration.md`.
It stops the exact approved integration/input/cap combination; it does not
disprove an extraction identity, a representation theorem or P versus NP.

**Hypotheses and imported inputs.** Use exactly §10's supplied 31-record
proof/request, the unchanged step-461 empty-clause source/annotations/pair,
and §12's scalar-only formula translator. Preserve every source tree and root,
the ordered four-original alphabet, all ten dictionary entries and display
names, all multiplicities, caller bytes and all original interface caps.
Reuse §13's arbitrary-root path-restriction justification. Its primary source
is Raz–Shpilka, *Deterministic Polynomial Identity Testing in Non Commutative
Models*, author-hosted 16-page manuscript, Definition 1 and Lemma 2 Steps 3
and 5, printed pp.4–6,
[primary manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
revision date unestablished, inspected in steps 474/476. Only pruning is
imported; no formula-size bound, homogeneity, constant-edge rewiring or
general integrated cap guarantee is imported or reproved.

L035 permits alternative corrections satisfying its two formal identities;
it does not prescribe their free polynomial. L036 (5)–(8) and L108 §2
consume those identities with original-only inputs. Hence the operand
restriction may be inserted before a call while retaining its original
recipe and normalized Boolean parent. These are existing results, not new
lemmas. The unchanged L035 constructor still copies every edge-pair branch,
including those with empty central label. Its exact ledger and all preflights
remain mandatory. Neither whole Boolean-output trimming nor changing a
normalized parent is performed.

**Conclusion.** The isolated pair of §13 now completes, with a received
45,474-record L035 output. Integration nevertheless stops at event 219,
the twelfth nested call of Boolean parent 196 at zero-based source axiom
record 22. Its restricted operands require **3,586,238 records / 2,000,000**.
No K/H certificate, complete root/block arithmetic reception or positive
K+fJ composition exists. This is informative local negative evidence using
known pruning, without a claim beyond the inspected mathematical sources.

**Exact operation and full trace proof.**
`scripts/four-rule-extraction/trimming_translation.py` reuses the exact
filter of §13. Both `m.witness` and occurrence's direct `checked_witness`
entry delegate once to the retained checked constructor. Original-only
guards run on the original operands and again on the restricted operands;
the exact-copy/L035 preflight still precedes the constructor. No forbidden
label can be concealed by pruning. No polynomial evaluator chooses a
rewrite. Each input event persists both original recipe graphs, both full
restrictions, complete vertex and edge-occurrence maps, endpoints and old/new
ledgers before the potentially long call. Every completed output is saved
with its exact input parent. Translation, Boolean normalization, constructor
bodies, copying guards, all receivers and caps are unchanged.

The independent `verify_trimmed_occurrence.py` imports no emitter, adapter,
filter or correction constructor. It reconstructs the exact source rule
event order, all repeated translation occurrences, direct argument pairs,
normalized parents and L036's complete ordered suffix/prefix schedule before
checking restrictions. Separate Boolean transitive closure determines every
retained vertex and edge; the full occurrence maps and label lists check
endpoint transport, order and multiplicities. Backward free-word arithmetic
evaluates both original and restricted operands in full, not merely their
commutator. Counter-based independent ledgers reproduce every old/new count.
Every completed output's actual free/zero/substituted polynomials are
retained, and the zero/substituted identities and parent/exact-output counts
are checked. Coincident and no-path conventions are those of §13; no
semantic zero or scalar recognition removes calls.

All 220 saved events receive this complete prefix verification: 66 source
translations, 69 commutator input pairs (56 nested, 13 source-direct), 68
commutator outputs, nine Boolean inputs and eight Boolean outputs. All 138
operand restrictions preserve their complete ordered polynomials; 67 change
the graph. The missing outputs are exactly commutator 219 and Boolean 196.
The occurrence-stage direct entry is installed but **not reached**; its
positive provenance/reception branch remains unexercised. This is not a
complete integration acceptance or a critical code audit.

**Failure and exact count.** The rejected pair consists of L036 prefixed
graphs in its sum-commutator schedule. Each original has 87 vertices and
114 edges. After restriction the first has 45 vertices/57 edges and the
second 83 vertices/107 edges. Their full polynomials have respectively
seven and 42 words; the independently evaluated commutator has 420 words,
so this pending call is not the earlier zero-target pair. With every
empty-central branch still charged, the unchanged ledger is

    p = 57·107 = 6,099,             q = 24,
    N = 2+2·6,099·(45+83) = 1,561,346,
    M = 2·6,099·(57+107)+4·6,099+24 = 2,024,892,
    N+M = 3,586,238 > 2,000,000.

The excess is 1,586,238 records. The same original pair's ledger is
10,500,818 records. These are exact counts, not asymptotic predictions.
The complete original pair matches failure frame 8, and the complete
restricted pair matches the actual checked-constructor frame 9. Independent
schedule reconstruction identifies it as nested job 11, preserving the
normalized parent. The rejected graph is not allocated or accepted.

The full retained outer graph has 28,324 vertices and 33,072 edges, totaling
61,396 records. `verify_trimmed_stop.py` checks every endpoint, label and
acyclicity; all 45 source seed/transition blocks for lines 0–21 have exact
source metadata, complete contiguous fresh interiors and connectors.
Every copied seed/transition graph is bound to its actual trace output;
cut seeds are checked as the exact ordered two-factor product. All 31
source-root vertices remain. The saved unfinished Boolean graph has
319,298 records and passes topology/label checks only; no identity is
assigned to it or to the partial outer graph. The earlier event-201
restrictions equal §13's full certificate, and output 202 is now complete
and received at exactly 45,474 records. No cap is raised.

**Evidence, reproduction and bounds.** In a workspace without output-477,
run these commands in order, each prefixed by `PYTHONDONTWRITEBYTECODE=1 python3`:
`scripts/four-rule-extraction/run_trimmed_occurrence.py`,
`scripts/four-rule-extraction/verify_trimmed_occurrence.py`, then
`scripts/four-rule-extraction/verify_trimmed_stop.py`.
The run and receivers refuse their existing output/receipt paths. Full graphs,
maps, ledgers, failure frames, source/input hashes and all ordered polynomials
are retained in `scripts/four-rule-extraction/output-477/`. The decisive
receipts are `integration-reception.json` (accepted=false, complete saved
trace prefix received) and `stop-check.json` (verified_resource_stop=true,
no failed evidence checks). The trace arithmetic uses 2,656,305
multiplication pairs / 100,000,000, at most 420 words / 1,000,000,
word length 12 / 256 and 209,441 stored words / 20,000,000.
K/H serialization and complete reception are not reached. The streaming
200,000,000-byte evidence limit and all input/label caps remain unchanged;
these do not bound aggregate interpreter work or memory.

The original five caller files compare byte-for-byte with steps 470/461 and
their complete manifest. Production implementations, the reused scalar
adapter/filter and old pair certificates retain their recorded hashes.
New integration sources are pinned before emission; the later independent
stop receiver records its supplemental source hash. Exact failed operands,
all completed outputs and the entire relevant saved graphs were read by the
receivers; previews or hashes alone are not the mathematical verification.

**Limitations and scope.** Stop whole-operand path trimming with
this supplied proof and unchanged constructor/caps. Attempts 039/040 remain
valid and preserved. The later nonzero commutator supplies a different
obstruction than the isolated zero-target pair, without refuting the
underlying identities. No internal branch omission, changed ledger or
positive integrated conclusion is established here. Nonzero fJ (this
endpoint has f=0), full positive occurrence reception, total resources,
general proof availability, M-only bounds, L087's unproved W₂, ER transfer
and unrestricted SAT remain unresolved. Trusted caller paths and remaining
SHA provenance assumptions persist. Full matching Mathlib coverage is
**not checked**. No new mathematical DAG input is introduced.

**15. Isolated empty-central branch omission — step 479, 2026-10-25.**

**Hypotheses.** This finite REPRODUCTION attempt uses the pre-invocation
SPECIALIZE assessment `drafts/literature/2026-10-25-empty-central-branch-omission.md`
and exactly §14's event 219, parent 196, restricted operands and original
recipe/maps. The step-470 proof/request, step-461 source/annotations/pair,
four original names, complete ten-entry dictionary and all caps are unchanged.
Only pair branches whose literal L035 (2) central lists are empty are omitted.
Every nonempty-list branch retains all four full copies and all connectors
and central occurrences; cancellation or substitution never selects omission.

**Conclusion.** The isolated candidate has **6,146 vertices + 7,992 edges =
14,138 records / 2,000,000**. Its entire free polynomial equals L035 (4),
with 1,440 surviving words; its zero-placeholder value is zero; its axiom
substitution is the original 420-word nonzero commutator. This passing finite
representation test is not a new general lemma or a passing integration.
§14's unchanged-constructor failure and Attempts 039–041 remain valid.

**Proof and reception.** The mathematical justification is L035's existing
empty-central audit observation: such a branch has no accepting path.
The stronger equality with the particular free polynomial (4) is also
independently checked below. Source roles remain as assessed: Li–Tzameret–Wang,
[*Characterizing Propositional Proofs as Non-Commutative Formulas*,
arXiv:1412.8746v4, Lemma 3.7, printed p.18](https://arxiv.org/pdf/1412.8746v4),
provides formula-input witnesses, not this arbitrary-ABP free polynomial or
finite cap. Raz–Shpilka, [*Deterministic Polynomial Identity Testing in Non
Commutative Models*, author-hosted 16-page manuscript, Definition 1 and
Lemma 2 Steps 1,3,5, printed pp.4–6](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
supports separate graph operations under its stated formula/layering
hypotheses. No formula-size bound or constant-edge rewiring is imported for
this arbitrary-root pair. Existing L035 identities and the source comparison
are reused; no source theorem is reproved.

All paths below are relative to `scripts/four-rule-extraction/`.
`omit_empty_central.py` saves complete operands, original event, parent,
failure frame, dictionary and source/input hashes before construction,
enumerates every edge pair and literal central list, and allocates only
nonempty-list branches. `receive_empty_central.py` imports no constructor,
filter or selector. It reconstructs normalized parent 196's ordered L036
schedule and twelfth job, verifies both complete restriction maps using
all-pairs Boolean reachability, and evaluates the full original and restricted
operand polynomials, obtaining equality. The complete originals match failure
frame 8 and restrictions match frame 9. The prior prefix/stop receipts retain
their limited §14 scope. All five caller files also compare byte-for-byte
with their step-470/461 originals and manifest; preservation hashes pass.
This reuses §14's source-prefix binding, without claiming a new integrated run.

From each received operand, forward and backward free-word F₂ traversals
calculate all source-to-vertex prefixes and vertex-to-sink suffixes, including
empty paths. Independently enumerating **all 6,099 edge pairs**, the receiver
uses the typed dictionary for L035 (2)'s coefficient rule and evaluates each
term in exactly F-prefix, G-prefix, central, G-suffix, F-suffix order.
`output-479/reference.json` saves complete subpath tables, every literal
central list and full term polynomial, and the entire resulting free
polynomial. No absent old correction graph is claimed received.

Every candidate record is separately received in contiguous four-copy
partitions: all original endpoints, labels, edge occurrences, connectors,
central edges and order are checked. Every omitted pair has a literally
empty central list. There are independently counted **24 retained pairs**,
**6,075 omitted pairs**, and **24 central edges**; the pair count is not
inferred from q. With r=24 the independently reconstructed ledger is

    N = 2 + 2r(45+83) = 6,146,
    M = 2r(57+107) + 4r + 24 = 7,992.

This equals the entire actual allocation. A separate backward traversal of
the complete candidate evaluates free, zero and substituted values, comparing
free with the all-pair reference and substituted with ordered fg+gf from the
received operands and §14's saved 420-word target. Structural forward
path-count sets disregard cancellation and even treat empty-labelled copied
edges as graph edges. They never exceed one placeholder on reachable paths
and equal {1} at the sink. Thus the path property covers cancelling paths,
not just surviving monomials.

**Bounds and reproduction.** The candidate charges 7,992 label entries,
all ten dictionary entries, 40 original/placeholder display-name bytes,
roots and full framing in 152,085 serialized bytes. All five evidence files
total 1,432,988 bytes / 200,000,000. Arithmetic uses 408,662 multiplication
pairs / 100,000,000, at most 1,440 words / 1,000,000, word length 12 / 256
and 104,947 traversal stored words / 20,000,000; retained reference subpath
tables are also explicitly storage-cap checked. All input/label/name caps
remain unchanged. These finite checks give no total-interpreter-resource or
polynomial-time theorem. In a workspace without output-479 run, in order,
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/omit_empty_central.py`
and `PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/receive_empty_central.py`
from the active notebook. Both refuse existing outputs/receipts. Complete
inputs, inventory, candidate, reference and reception are in `output-479/`;
`reception.json` reports accepted=true, no failures, complete polynomials,
provenance and actual/required bounds.

**Qualifications and Mathlib.** The isolated continuation test passes;
broader integration requires separate coverage. No full K/H, occurrence
direct-entry reception, nonzero fJ, total resource bound, general certificate
availability or M-only/W₂/ER/Frege/SAT conclusion follows. L087 W₂ remains
unproved; trusted paths and remaining SHA bindings keep their old boundaries.
This is local implementation progress using known identities, with no claim
beyond inspected mathematical sources. Full matching Mathlib coverage is
**not checked**; no absence claim or new DAG input is introduced.

**16. Complete empty-central integration reception — step 481, 2026-10-25.**

**Hypotheses and source coverage.** This is the single finite REPRODUCTION
attempt approved before invocation by
`drafts/literature/2026-10-25-empty-central-integration.md` (SPECIALIZE).
The exact §10 step-470 proof/request and step-461 source/annotations/pair,
all 31 literal records and trees, alphabet [y3,y2,y1,y0], complete ordered
ten-entry dictionary, original-only correction inputs and CAPS are unchanged.
Retain §12's scalar translator and §14's whole-operand restriction. Only
branches whose literal L035 (2) central lists are empty are omitted; all
nonempty lists, including repetitions and cancelling terms, are retained.
The original Boolean constructor, normalized parents and ordered L036 jobs
are unchanged. No complete general availability or complexity theorem is a
hypothesis or conclusion of this finite exercise.

The justification is L035's existing empty-central audit: a branch with no
central edge has no accepting path. L036 (5)–(8) and L108 §2 consume the
unchanged formal correction identities. The primary source comparison is
reused from §15 and the assessment: Li–Tzameret–Wang,
[*Characterizing Propositional Proofs as Non-Commutative Formulas*,
arXiv:1412.8746v4, 11 September 2015, Lemma 3.7, printed p.18](https://arxiv.org/pdf/1412.8746v4),
gives formula-input witnesses; Raz–Shpilka,
[*Deterministic Polynomial Identity Testing in Non Commutative Models*,
author-hosted 16-page manuscript, Definition 1 and Lemma 2 Steps 1,3,5,
printed pp.4–6](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
supports the assessed graph operations with its own formula/layering
hypotheses. Neither is imported as an arbitrary-ABP finite-cap guarantee or
as a formula-size bound for these inputs. No source theorem is reproved and
no new mathematical identity is proposed.

**Conclusion.** The full finite integration passes both the unchanged
production K/H receiver and the new independent trace/copy receiver. K has
118,696 vertices and 152,114 edges, hence **270,810 / 2,000,000 records**;
H has **271,112 / 2,000,000 records**. All 31 source roots and 64 source
seed/transition blocks are received. This replaces the historical absence
of a full positive supplied occurrence reception on this endpoint only.
It is local implementation progress using known identities, not progress
beyond the inspected mathematical sources or a resolution of P versus NP.
A separate critical code/evidence audit was pending at step 481; §17 records
its completion under these same hypotheses.

**Construction and exact preflights.** Paths in this paragraph are relative
to `scripts/four-rule-extraction/`. `empty_central_translation.py` reuses
the scalar adapter/filter and covers both `m.witness` (nested and source)
and occurrence's direct `checked_witness`, with one dispatch per call.
Original-only guards run before and after restriction. Before copying, each
input event persists the complete original graphs, both restriction maps,
original and restricted all-pair ledgers, every literal edge-pair central
list and the selected ledger. The baseline all-pair guard is replaced by
a selected allocation guard, never silently bypassed. With r the number of
nonempty lists, q their total length, and the actual restricted operands F,G,
the selected counts are N=2+2r(V_F+V_G) and
M=2r(M_F+M_G)+4r+q. The label-entry preflight also charges every copied
original label and all connectors/central occurrences. It does not identify
r with q. Allocation keeps the four complete copies, in prefix/prefix/
central/suffix/suffix order, and every connector. Actual counts must equal
the preflight; zero selected pairs produce two vertices and no edges.
No semantic zero, cancellation, substituted value or polynomial evaluation
selects deletion. Source/input hashes and full caller copies are saved before
construction. `run_empty_central_occurrence.py` retains the failure-checkpoint
and immutable-input driver; no cap or production acceptance contract changes.

**Independent finite proof reception.** `verify_empty_central_occurrence.py`
and `receive_selected_commutator.py` import no emitter, adapter, selector or
correction constructor. The reused trace receiver reconstructs the complete
source recipe and occurrence plan before restriction. Independent Boolean
reachability and literal occurrence maps verify all 412 restrictions; both
complete original/restricted ordered polynomials agree. Of these restrictions,
222 change a graph. Every actual input remains original-only.

The receiver enumerates every operand edge pair, reconstructing central lists
through the typed caller dictionary rather than the emitter's token parsing.
It checks both all-pair baseline ledgers and independently counts r, q and
all selected records/labels. Every output is bound to its input parent and
entry, with complete fresh four-copy partitions, labels, multiplicities,
connectors and central-edge order. All records must be accounted for.
Independent forward/backward subpath sums compute L035 (4) over ALL pairs,
with the full term and complete tables retained in one reference file per
call. Each output's complete free polynomial equals that reference; its
zero value vanishes and its substituted value equals ordered fg+gf from the
received operands. Expansion-cap failure would reject, rather than certify,
equality. Structural path-count sets ignore cancellation and allow the
no-path case: the sink set is a subset of {1}, not necessarily {1}.

For every Boolean output, independent reconstruction checks its complete
normalized propagation graph, every original suffix and beta branch, each
ordered product/sum-commutator job, all actual copied factor partitions and
connectors, and the complete attach ledger. No Boolean branch or job is
removed. Its full free/zero/substituted values are saved and the Booleanity
identity received. The trace then binds the exact outputs to every K block,
including ordered cut factors, and both occurrence-direct corrections to
the actual H correction archive. The unchanged production receivers receive
all K roots/blocks, literal source/proof/dictionary retention, checked K-byte
binding, the complete ordered J recipe and identities, and all copies of
K+fJ. All five caller files compare byte-for-byte with steps 470/461 and their
manifest; pinned source and prior-evidence hashes are unchanged.

Exactly **529 events** are consumed: 93 translations, 12 Boolean inputs and
12 outputs, and 206 commutator inputs and 206 outputs. The calls split into
186 nested, 18 source-direct and two occurrence-direct. All 206 complete
all-pair reference files are saved. `integration-reception.json` reports
accepted=true, complete_KH_received=true, complete_trace_received=true and
failures=[]. `reception.json` independently reports production acceptance;
neither an emitted graph nor a checked prefix alone establishes this result.

**Bounds and reproduction.** The largest selected L035 output is 29,276
records; the largest original all-pair baseline encountered is 10,500,818.
K uses 3,800,920 serialized bytes and H 3,801,070, each / 200,000,000.
The final new evidence, including `bounds-and-scope.json`, uses 49,491,927
bytes / 200,000,000. A streaming I/O alias wrapper retains the per-file guards
and charges every replacement's resulting aggregate evidence size; it changes
persistence only, not graph recipes or production accepting contracts. It
does not bound simultaneous old/temporary-file storage or interpreter memory.

Trace arithmetic uses 15,750,315 multiplication pairs / 100,000,000,
at most 10,899 words / 1,000,000, word length 16 / 256 and 2,881,905
stored traversal words / 20,000,000. Production K arithmetic respectively
uses 14,064,287 pairs, 10,899 words, length 16 and 2,884,044 stored words.
Occurrence correction/H arithmetic uses 8,529/4,065 pairs, at most 238 words,
length 12 and 1,538/1,548 stored words, against the same caps. Reference
subpath/term/partial-sum storage is separately cap checked during construction
of each complete reference; its peak is not included in the traversal counter.
Inventory entries, label payload, full serialization and all original input,
word, alphabet and name caps remain charged. These separately bounded finite
stages give no total-interpreter-time or aggregate-memory theorem.

In a workspace without output-481, run in order from this notebook, each
prefixed by `PYTHONDONTWRITEBYTECODE=1 python3`,
`scripts/four-rule-extraction/run_empty_central_occurrence.py` and
`scripts/four-rule-extraction/verify_empty_central_occurrence.py`.
Both refuse existing run/receipt paths. All mathematically essential inputs,
trace graphs/maps/inventories/partitions, 206 complete references, full K/H
archives, ordered polynomials and bound/acceptance receipts are in output-481.
The optional byte/count summary is `bounds-and-scope.json`; all final file
sizes listed there precede that summary itself, whose addition is included
in the final byte total above.

**Qualifications and Mathlib.** This is a finite REPRODUCTION; the critical
audit is recorded in §17. The endpoint has f=0, so positive full reception still cannot
test nonzero fJ. General certificate availability, total resources, M-only
bounds, L087's unproved W₂, ER/Frege transfer and unrestricted SAT remain
unresolved. Trusted caller paths and remaining SHA bindings retain their
existing boundaries. Attempts 039–041 and their original failed constructor
combinations remain valid and preserved. Full matching Mathlib coverage is
**not checked**; no absence or originality claim and no new DAG input are made.

**17. Independent finite integration audit — step 483, 2026-10-25.**

**Hypotheses and precise source use.** Audit exactly §16's step-470/461 caller,
saved step-481 source versions and unchanged caps under the pre-invocation
SPECIALIZE assessment
`drafts/literature/2026-10-25-empty-central-integration-critical-audit.md`.
Reuse L035 (2)/(4) and its empty-central no-path observation, L036 (5)–(8),
L108 §2 and its §13 byte-boundary audit, and this lemma's §§10,12,14–16.
The primary mathematical imports remain LTW, arXiv:1412.8746v4, Lemma 3.7,
printed p.18, and Raz–Shpilka, author-hosted 16-page manuscript, Definition 1
and Lemma 2 Steps 1,3,5, pp.4–6, with the exact narrower roles in §16.
Their formula-input conclusions are not promoted to a saved-instance cap.
No theorem is reproved and no new identity or unrestricted conclusion is added.

The runtime comparison reuses the assessment's official Python 3.15.1
specifications: [JSONEncoder.iterencode](https://docs.python.org/3.15/library/json.html#json.JSONEncoder.iterencode),
[PurePath.is_relative_to](https://docs.python.org/3.15/library/pathlib.html#pathlib.PurePath.is_relative_to),
[Path.replace](https://docs.python.org/3.15/library/pathlib.html#pathlib.Path.replace),
and [sys.modules](https://docs.python.org/3.15/library/sys.html#sys.modules).
These specify interfaces, not implementation correctness or total resources.

**Conclusion.** No substantive defect was found within this finite scope.
Both independent production reception and full trace/reference reception pass.
All 529 events, 206 full all-pair references, 31 source roots, 64 K blocks,
and both occurrence-direct calls are accounted for. The saved mathematical
and resource evidence is reproduced completely, not inferred from hashes,
samples or accepted flags. This is local REPRODUCTION validation progress,
not a new mathematical result beyond the inspected sources.

**Code and mathematical reception.** All four changed modules were read with
their reused dispatch, normalization, original-only, copy, input and production
receiving code. Both public entries dispatch once to the selected constructor;
Boolean parent state is restored even on failure. Original-only guards precede
restriction and are repeated afterwards, so dead forbidden symbols cannot be
hidden. Every edge pair and its literal central occurrences are retained in
the input event. Selection tests list emptiness only. With r retained pairs
and q central occurrences, the preflights charge exactly
2+2r(V_F+V_G) vertices, 2r(M_F+M_G)+4r+q edges and the complete copied label
payload. Both record and label bounds precede correction-graph allocation.
The four copies and connectors retain the order in L035 (4); r is not q.

The separate receiver reconstructs source formulas and every Boolean job,
checks all 412 restriction maps and complete original/restricted polynomials,
and derives central lists using typed dictionary positions. It reconstructs
the complete all-pair free reference, including omitted pairs, from forward
prefix and backward suffix sums. The candidate's full free polynomial equals
that reference; its zero value vanishes and its substituted value equals
the original ordered commutator. Actual copy partitions account for every
vertex, edge, connector and label occurrence. Structural placeholder counts
ignore cancellation and admit no-path outputs. Boolean reception checks the
entire normalized propagation graph, original suffixes, both suffix copies,
all beta/product/sum branches and their attachment order before receiving
the full Boolean identities. No correction is used as an original operand.

The trace's exact graphs are bound to every K block, including ordered cut
factors, and to both actual occurrence corrections in H. Production reception
independently validates the literal proof, full caller text/digest/dictionary,
all root/block identities, contiguous fresh partitions, original-only right
multipliers, the checked K-byte binding, every ordered J recipe and all copies
of K+fJ. All five caller files compare exactly with their step-470/461 inputs.
The run-scope pins are checked, and the unchanged generic/occurrence modules
are additionally matched to the earlier L108 §13 audit's dependency records.
This retains, rather than removes, the stated trusted-path and SHA boundaries.

**Fresh evidence and discriminating tests.** Paths in this paragraph are
relative to `scripts/four-rule-extraction/`. `audit_empty_central.py` starts
separate emitter and receiver processes. The latter imports no emitter,
adapter or constructor. Fresh graphs, all trace files and production receipts
match output-481 completely; only the absolute output path in two construction
receipts is normalized. All 206 reference files and the entire received trace
and integration receipt compare byte-for-byte. The complete isolated
output-479 event-219 inputs, inventory, candidate/copy partition and reference
also match their integrated counterparts. All 757 protected output-481 files
retain their recorded hashes; no earlier archive or production code is edited.

`audit_empty_central_units.py` separately receives six cases: repeated cancelling
central occurrences, identical original labels, constants, no path, coincident
roots, and four ordered noncommuting factors. In particular, a literal central
list of length two has r=1, q=2, zero free value and structural sink count {1};
it is retained. Empty cases have exactly two vertices and no edges. Six altered
outputs reject: copied label, connector, parent, extra vertex, central count
and branch order. Four guard tests reject forbidden originals before/after
restriction and record/label overflows before output allocation. The isolated
test limits are restored; no production acceptance cap is increased.

**Writer boundary and audit-harness qualifications.** The actual imported
runner and every existing module-global write_json alias are rebound, and a
later ordinary import sees the rebound function. Private Boolean/marked/checker
modules do not invoke an unpatched writer in the reviewed call paths. Actual
destinations are generated beneath the designated folder; the five direct
caller byte copies are received and included in subsequent aggregate sums.
The lexical path check supplies no symlink or parent-segment confinement.
Replacement subtracts the existing destination size, then charges each chunk
and the final newline before writing. Final aggregate size excludes the old
destination that will be replaced; it is not peak simultaneous old/temporary
storage. Failed writes leave a partial artifact and preserve the prior
destination. Surviving partials are included in later directory sums, which
can conservatively overcharge a retried partial file. No failure is converted
into an accepting receipt, and the complete accepted replay has no partials.
If the aggregate evidence budget itself is exhausted, writing a failure
receipt can also fail; the wrapper guarantees neither a final failure receipt
nor recovery/liveness. Earlier completed files and any partial remain evidence.

Six focused writer checks cover initial bytes/newline, replacement, per-file
failure (37/24 bytes), aggregate failure (59/40), an outside lexical path,
and final-newline failure (8/7). These tiny limits are isolated test bounds.
Full artifacts and rejection reasons are retained. The replay's relocated
in-memory runner namespace is outside sys.modules, so its two direct
run-scope/trace-summary writes use the original per-file-capped writer.
`replay-io-qualification.json` records this harness difference; the real
registered runner's aliases are separately verified, and all replay bytes
and final aggregate sizes are independently checked. No blanket claim about
unobserved closures or arbitrary later dynamic imports is made.

The first separate-reception comparison mistakenly compared a raw Python
receipt containing tuple symbols with parsed JSON containing lists. Its
failure is retained in `receive.log` and `audit-failure.json`. The harness was
corrected to compare the complete serialized receipts; they are byte-identical.
`comparison-boundary.json` records the type distinction. No receiving condition,
algebraic comparison, cap or production module was relaxed to obtain success.

**Actual bounds and reproduction.** K and H retain 270,810 and 271,112 records
/ 2,000,000 and 3,800,920 and 3,801,070 bytes / 200,000,000. The maximum
selected correction is 29,276 records. Trace/production-K/correction/H
arithmetic exactly reproduces §16's complete counters, including trace
15,750,315 multiplication pairs / 100,000,000, 10,899 words / 1,000,000,
length 16 / 256 and 2,881,905 traversal words / 20,000,000. Complete reference
tables, retained term words and partial sums are separately storage-cap checked;
these are not silently included in the traversal counter. The independently
enumerated original evidence is 49,491,927 bytes / 200,000,000. Fresh audit
evidence at completion is 49,823,749 bytes against that same byte threshold.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/audit_empty_central.py`
from this notebook in a workspace without output-483. The script refuses an
existing output directory, runs the focused units in a separate process and
saves complete evidence, comparisons, bounds and qualifications there.
The retained first execution's comparison error was followed by the corrected
`receive` stage and `finish`; both its failed log and the successful
`receive-wire-replay.log` remain. `verification.json` is the final successful
audit verdict, not the historical failed harness log.

**Remaining scope and Mathlib.** The audit establishes only the saved finite
implementation claim. Since f=0, it cannot test nonzero fJ. General certificate
availability, total interpreter time/memory, M-only bounds, L087 W₂, ER/Frege
transfer and unrestricted SAT remain unresolved. Attempts 039–041 retain their
original stops. Full matching Mathlib coverage is **not checked**; no absence,
formal machine proof or certified novelty is claimed. No DAG input changes.

**18. Direct retained opposing-units endpoint — step 485, 2026-10-25.**
This finite reproduction uses only the unchanged pre-invocation SPECIALIZE
assessment `drafts/literature/2026-10-25-opposing-units-structural-endpoint.md`.
It supplies an endpoint for possible later nonzero-fJ reception. No extraction,
positive composition or new general proof-availability theorem is established.

**Hypotheses.** Receive the exact source, annotations and request in
`scripts/four-rule-extraction/output-461/final/opposing-units/`.
The source consists of unit clauses x and ¬x with positional tree [and,0,1].
Occurrence rows are [y0], [y1], [y2,y3], [y4,y5], consistency groups are
[y0,y1], [y2,y4], [y3,y5], and the alphabet is [y5,y4,y3,y2,y1,y0].
The complete 21-entry dictionary retains its order and colliding display names.
Use exactly L108's assumption-free literal rules and its §13 byte boundary;
no ground constant axiom is needed. Trusted caller paths and remaining SHA
provenance assumptions are retained. The old diagnostic proof remains invalid.

**Conclusion.** There is a 212-record primitive proof of this request's exact
ordered goal, using only its alphabet. Its full bytes pass the independent
literal checker and strict caller preflight under unchanged interface caps
and the separately imposed 1,000-record attempt limit. The separate critical
audit was pending at step 485; §19 records its completed verdict. This
is local implementation progress, with no originality claim beyond the
assessed sources and no unrestricted complexity conclusion.

**Proof: exact trees and structural inputs.** Write N(t)=¬t, O(s,t)=s∨t
and A(s,t)=N(O(N(s),N(t))) as literal abbreviations only. Set

    p=N(y0), q=N(y1), S=O(N(p),N(N(q))), F=A(p,N(q)),
    a=A(N(p),N(q)), b=A(p,q), U₀=O(a,b),
    G₁=O(N(y2),N(y3)), G₂=O(N(N(y4)),N(N(y5))),
    C=A(A(F,G₁),G₂),
    U₁=O(A(N(N(y2)),N(N(y4))),A(N(y2),N(y4))),
    U₂=O(A(N(N(y3)),N(N(y5))),A(N(y3),N(y5))),
    U=A(U₀,A(U₁,U₂)), T=N(A(C,U)).

Expansion, without cancelling any negations, gives the retained request goal
literally. In particular F=N(S), so N(F)=N(N(S)). Variables y0 and y1
are distinct; closure uses their displayed consistency formula U₀.

The source is Joseph R. Shoenfield, *Mathematical Logic*, Addison-Wesley
(1967), §2.6 pp.21–22 and §3.1 Lemma 1 and auxiliary (A)/(A'), (B), (C),
printed pp.28–30
([primary scan](https://w2.cs.uni-saarland.de/op/fullpaper/logics/SHOENFIELD_Mathematical_logic.pdf)).
No completeness oracle or bound on library preparation is imported. The
specialization needed here expands the structural operations into actual
backward-referenced primitive records for this fixed request. For clarity,
the exact expansions used by the construction follow; they establish legality,
not a new completeness theorem or a general compiler bound.

Let D(xs) be the right-associated disjunction of a nonempty list, a singleton
being its sole tree. A commutation of a proved O(X,Y) consists of axiom
O(N(X),X), then cut, yielding O(Y,X). Association always has the admitted
forward direction. Define R on an actual proved D(xs), with every entry of xs
among the target list ys, to produce D(ys). Here are all its used cases:

- One premise entry: choose its first target position. If there is a suffix,
  expand by its entire disjunction and commute; prepend earlier entries by
  expansion in reverse order. This gives exactly D(ys).
- Two entries: contract if equal, or commute if their chosen target positions
  are reversed. With increasing distinct positions, the two-entry target
  needs no change. For a longer target, if both positions are after its first
  entry, perform R on the target tail and expand by the first entry. Otherwise
  write the target as [Y₁,Y₂]+tail, Z=D(tail). If the second selected position
  is after Y₂, first insert only tail, giving O(Y₁,Z); commute, expand Y₂,
  associate, commute, yielding O(Y₁,O(Y₂,Z)). If the selected pair is Y₁,Y₂,
  expand Z onto O(Y₁,Y₂), then associate, commute, associate, commute, with
  exactly the same endpoint. Each recursive target has fewer entries.
- At least three entries, beginning X₁,X₂: associate once, then apply R to
  the shorter premise list [O(X₁,X₂)]+xs[2:] and target [O(X₁,X₂)]+ys.
  Put Y=D(ys). The result is O(O(X₁,X₂),Y). Commute and associate to
  O(O(Y,X₁),X₂). The two-entry case with target [O(Y,X₁)]+ys gives
  O(O(Y,X₁),Y). Commute and associate to O(O(Y,Y),X₁). The two-entry
  case with target [O(Y,Y)]+ys gives O(O(Y,Y),Y). Expand Y, associate,
  commute, associate, obtaining O(O(Y,Y),O(Y,Y)); contract twice to Y.
  All recursive premise lists have fewer entries. The last four operations
  explicitly avoid assuming contextual contraction or inverse association.

This describes primitive record generation, with endpoint assertions after
each R call, not a replacement rule on arbitrary formula contexts. Repeated
target entries are allowed; all inserted and copied trees are fully written.

Operation B takes a proved O(X,Y) to O(N(N(X)),Y): start with the axiom
O(N(N(X)),N(X)), commute it, cut the original premise against the result,
then commute. Operation C takes actual proved O(N(X),Z), O(N(Y),Z).
Put H=N(O(X,Y)). Start with axiom O(H,O(X,Y)); twice associate and commute
to obtain O(X,O(Y,H)). Cut the first supplied premise, giving
O(O(Y,H),Z). Commute, use R from [Z,Y,H] to [Y,Z,H], and cut the second
supplied premise, giving O(O(Z,H),Z). Commute and use R from [Z,Z,H]
to [H,Z]. This gives exactly O(H,Z), as in the source's two-premise case.
Every cut uses literal complementary left arguments. Finally the seven-record
standalone bridge of §10 applies only to an already proved whole formula.

**Proof: the finite construction.** Axiom O(N(p),p), commutation and B give
O(N(N(p)),N(p)). Apply R to target
[N(p),N(N(q)),N(N(p)),N(N(q))], associate and commute. The result is
O(O(N(N(p)),N(N(q))),S); B yields O(N(a),S).
Independently axiom O(N(N(q)),N(q)), R to
[N(p),N(N(q)),N(p),N(q)], association, commutation and B give O(N(b),S).
These are actual complementary closures; no assumed proof of an open branch
is used. C with X=a,Y=b,Z=S gives O(N(U₀),S). Commute and apply B to obtain
O(N(F),N(U₀)). The complete saved stages end at zero-based records
32,49,149 respectively.

For each successive opaque gadget G₁,G₂, suppose the current proved formula
is O(X,Z), with X the negation of the previous conjunction and Z=N(U₀).
Use R from [X,Z] to [Z,X,N(Gᵢ)], commute, then B. This gives
O(N(N(O(X,N(Gᵢ)))),Z), exactly the negation of the next conjunction on
the left. The resulting record 183 is O(N(C),N(U₀)). Commute it, apply R
to [N(C),N(U₀),N(A(U₁,U₂))], commute, B and commute. The resulting
record 204 is O(N(C),N(U)). The standalone seven-record bridge gives
record 211, N(N(O(N(C),N(U))))=T, without cancelling or rearranging a
subtree. G₁,G₂,U₁,U₂ are copied literally and need no branch proofs.

**Complete evidence and qualifications.** The construction is
`scripts/four-rule-extraction/construct_opposing_endpoint.py`; execute with
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/construct_opposing_endpoint.py`
from the notebook root in a workspace without its output directory. It refuses
to overwrite `scripts/four-rule-extraction/output-485/`, writes all records
incrementally and saves a literal-checked prefix and precise error on a caught
construction failure. Such receipt writing is not a total recovery guarantee
under interpreter or filesystem failure. The full `proof.jsonl`, `stages.json`,
fresh `request.json`, input pins and `verification.json` are retained there.
The checker imports no construction code; strict reception checks every record,
backward reference, full tree, immutable source bytes and original dictionary.

The accepted stream has 77 axiom, 77 cut, 18 expansion, 35 association and
5 contraction records, totaling 212/1,000 (interface cap 10,000). It has
12,919 written formula nodes; including the requested goal gives
13,018/100,000. Proof/request bytes are 101,314/2,000,000 and
2,947/2,000,000; maximum formula depth is 19/64, alphabet size 6/256,
dictionary cardinality 21/32,896 and maximum name length 4/4,096 bytes.
Strict JSON parsing enforces depth 160; this is not a total interpreter bound.
The receipt has no failures and proof SHA256
`f779fa52af4eb63805e45aa9940620be1cd3ce6c993ff4a903a996a0b539c74e`.
The new request changes only source_sha256. All four original retained files
remain byte-identical; the old diagnostic and old request are preserved.

This supplies a second exact finite endpoint after §10. It does not by itself
verify the full nonzero-fJ component/composition, general certificate
availability, total interpreter resources, L087 W₂,
M-only/ER/Frege bounds or SAT. Attempts 037–041 retain their stops. No DAG input
changes. Full matching Mathlib coverage of this finite transcript and its
implementation is **not checked**; supporting source results are the precise
Shoenfield operations above, with no absence or formal-verification claim.

**19. Independent opposing-units endpoint audit — step 487, 2026-10-25.**

**Hypotheses and source use.** Receive exactly §18's output-485 transcript,
request, stages, pins and receipt, and the original output-461/final/opposing-units
source, annotations, request and diagnostic proof. Use the pre-invocation
SPECIALIZE assessment
`drafts/literature/2026-10-25-opposing-units-endpoint-critical-audit.md`.
Reuse Shoenfield, *Mathematical Logic*, Addison-Wesley (1967), §2.6 pp.21–22,
§3.1 Lemma 1 and (A)/(A'), (B), (C), pp.28–30, with the primary scan and
exact hypotheses in §18. The §10 standalone bridge needs an actual proved
whole formula. L108 §13 supplies only its previously audited byte boundary;
L109 supplies no effective library-preparation bound and is not needed here.
No new theorem or completeness argument is asserted.

**Conclusion.** No substantive defect was found in this finite construction,
complete transcript, caller binding or measured input ledger. All 212 primitive
records and all six saved stage endpoints pass an independent record-by-record
check, and strict production reception agrees with the reconstructed receipt.
This qualifies the supplied endpoint for a later reception experiment; it is
REPRODUCTION verification progress, not mathematics beyond the assessed sources.

**Proof and code audit.** The entire constructor, strict input module and
literal checker were read. The constructor was not imported or replayed.
Commutation appends the axiom before the referencing cut; Python evaluates the
nested axiom call before add. Every structural helper operates on an already
proved whole disjunction. The singleton rearrangement inserts its suffix and
then earlier entries; the two-entry branches contract duplicates or move the
selected entries into the requested positions using only forward association,
expansion and commutation. The longer-premise branch reduces the premise list,
then uses two two-entry rearrangements to reach (Y∨Y)∨Y. Its expansion and
three rotations give (Y∨Y)∨(Y∨Y), so two whole-formula contractions give Y.
This verifies the displayed §18 expansion; no contextual contraction or
inverse association is used. Double-negation-on-the-left and the two-premise
join have the literal complementary pivots stated there. The latter receives
both actual proved branch endpoints at records 32 and 49 before producing
record 149. Attachments preserve the opaque gadget trees, and the final
seven-record bridge uses the actual record-204 theorem.

The new audit program `scripts/four-rule-extraction/audit_opposing_endpoint.py`
imports no constructor. It parses every LF-delimited saved record, checks
syntax, alphabet, tag arity and strictly backward integer references, and
matches each directed rule against the entire ordered premise/conclusion
trees. Induction on record index therefore proves every conclusion, with no
assumption lines. Every per-record verdict, node count and depth is retained
in output-487/verified/records.json. Independent signed-occurrence construction
from the original source and annotations reconstructs the exact complemented
source and consistency trees. It retains groups [y0,y1], [y2,y4], [y3,y5],
all conjunction bracketing and all negations. The resulting six stage formulas
match both saved stages and records 32,49,149,183,204,211. Thus the final
checked theorem is the caller's literal goal, rather than only an equivalent
Boolean formula. This is a complete finite check, not a truth-table argument.

**Caller and receiving boundary.** Every original file matches its constructor
pin, original caller manifest and earlier step-468 archive pin. The entire
original ordered dictionary is reconstructed: six Boolean entries and fifteen
ordered commutator entries, in the retained reverse-list order, with the
original colliding display names. Type-sensitive full comparison shows that
only source_sha256 differs between old and new requests. All four original
files and all five output-485 files compare byte-for-byte before/after this
audit. Current checker and request code hashes match the step-466 versions
reviewed in L108 §13. The unchanged request implementation reads bounded bytes,
compares the second source read to the first, and passes that immutable first
object to check_bytes. Observed reads are one 2,947-byte request followed by
two equal 101,314-byte source objects; the returned source is the first object.
Both direct byte checking and complete strict reception match the independently
reconstructed receipt and every field of the saved verification artifact.
Trusted caller paths and the remaining SHA provenance assumptions persist.
This is not an atomic-filesystem or total interpreter-resource theorem.

Five fresh damaged transcripts, one for each used primitive tag, reject at
records 0,2,11,12,104 respectively. The untouched original diagnostic still
rejects at the exact final endpoint, and supplying the new proof under the
old request rejects at the caller digest. These controls supplement, rather
than replace, the complete positive checks.

**Full bounds, artifacts and qualifications.** Counts are exactly 77 axiom,
77 cut, 18 expansion, 35 association and 5 contraction. The independent
receipt counts 12,919 written formula nodes; adding the goal gives
13,018/100,000. Records are 212/1,000 for the attempt and 212/10,000 for
the interface; source/request bytes are 101,314/2,000,000 and 2,947/2,000,000.
Tree depth is 19/64, parsed JSON container depth 19/160, alphabet 6/256,
dictionary 21/32,896 and maximum name bytes 4/4,096. Every actual/required
input-bound field agrees with production and the complete saved receipt.
These measured bounds do not assert total work, simultaneous memory or
recovery guarantees. No extraction or nonzero-fJ composition ran.

Reproduce from the notebook with
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/audit_opposing_endpoint.py`
in a workspace without output-487/verified; existing output is refused.
The complete evidence is `scripts/four-rule-extraction/output-487/verified/`,
including records, stage trees, full caller comparison, negative transcripts,
negative-control receipts and verification.json. The initial audit-harness
failure is preserved at output-487/failure.json: the earlier hash manifest
used notebook-relative paths but the first lookup used an absolute path.
Correcting that lookup and writing to a fresh verified subdirectory changed
no production rule, artifact, cap or mathematical claim.

General proof availability, full nonzero-fJ reception, total executable
resources, L087 W₂, M-only/ER/Frege bounds and unrestricted SAT remain
unresolved. Attempts 037–041 and their exact stopping evidence remain intact.
No direct mathematical dependency changed. Full matching Mathlib coverage of
this finite transcript or implementation is **not checked**; no formal
verification, absence or novelty claim is made.

**20. Opposing-units nonzero reception: Boolean-copy cap stop — step 489,
2026-10-25.**

**Hypotheses and precise source use.** This is one REPRODUCTION implementation
test under the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-25-opposing-units-nonzero-reception.md`.
Use exactly §18's output-485 proof/request, §19's output-487/verified audit
and output-461/final/opposing-units source/annotations/pair. All 212 literal
records, alphabet [y5,y4,y3,y2,y1,y0], ordered 21-entry dictionary, groups
[y0,y1], [y2,y4], [y3,y5], original tester graphs and every CAPS value remain
fixed. The intended discriminator requires a nonempty complete substituted
fJ in addition to complete K/H, correction and trace/reference reception.
The relevant identities and construction hypotheses are §§1–2,6.5,8–9,16–19,
L035/L036 and L108 §§2,13; no new identity or source theorem is asserted.

The precise narrower sources from §§16–19 are reused: Shoenfield,
*Mathematical Logic* (1967), §2.6 pp.21–22 and §3.1 pp.28–30 for the supplied
literal proof; Li–Tzameret–Wang, arXiv:1412.8746v4 (11 September 2015),
Lemma 3.7 p.18 for formula-input commutator witnesses; Raz–Shpilka,
16-page author manuscript, Definition 1 and Lemma 2 Steps 1,3,5, pp.4–6
for the assessed graph operations. Their direct primary links and limitations
are given above. None guarantees arbitrary supplied-ABP cap feasibility.
This application neither rederives their results nor infers a new discovery.

**Fixed-caller adaptation and stopped execution.** All paths below are relative
to `scripts/four-rule-extraction/`. `run_opposing_occurrence.py` explicitly
sets the retained driver's BASE to output-461/final/opposing-units, SUPPLIED
to output-485 and OUT to the fresh output-489. It retains the driver's five
byte-for-byte caller copies, fresh manifest, complete strict preflight and
failure-frame persistence. The invalid original proof/request remain pinned
and unchanged. Before construction, reused source modules match the saved
step-481 scope and step-483 audited dependency hashes; both new fixed-caller
harnesses and the endpoint/audit artifacts are additionally pinned. Both
selected-constructor entries, all original-only guards, scalar translation,
whole-operand restriction, literal-empty selection, Boolean construction,
correction plan, production acceptance and caps are unchanged. Observed
module-global write_json aliases are checked after installing the existing
streaming per-file/aggregate evidence wrapper. Trusted paths, remaining SHA,
temporary-storage and failure-receipt persistence qualifications from §17 remain.

The complete strict preflight accepts the 212-record caller-bound proof,
with 12,919 written formula nodes and 101,314 source bytes. Emission then
stops at zero-based source record **78**, an axiom, while copying a selected
sum-commutator into its Boolean seed. The saved partial Boolean has
867,307 vertices and 1,117,028 edges, totaling **1,984,335 records**. The
pending block has 11,954 vertices and 15,300 edges, totaling **27,254 records**.
The unchanged checked_copy guard includes an eight-record allowance, giving

    1,984,335 + 27,254 + 8 = 2,011,597 > 2,000,000.

The actual graph after this particular two-connector attachment would itself
have 2,011,591 records, also beyond the cap; failure is not solely an allowance
artifact. This is a count of the saved proposed attachment, not an allocation
or identity claim for the unfinished graph. The driver saves all **2,888**
trace events, complete original/restricted operands, literal inventories,
selected outputs, pending block and partial Boolean/K frames. It reports
completed=false, accepted=false, stage=emission. No K/H archive exists and
no occurrence-direct correction is reached. Neither J nor nonzero fJ is
received by this run. No cap is raised and no changed-constructor retry occurs.

**Independent receiving evidence and second cap.** In a separate process,
`verify_opposing_occurrence.py` imports no emitter, adapter or constructor.
It reuses §16's complete selected-commutator and Boolean-copy reception and
the existing source/occurrence schedule. Its preservation function explicitly
compares all five copied caller files to the opposing-units/485 originals,
checks their manifest and all pinned source/input hashes, and retains the
existing production K-byte/caller-binding conditions. Its additional complete
nonzero-fJ success discriminator is **unexecuted**. No completed H exists on
which to apply it.

The last completely written `trace-received-prefix.json` contains precisely
events **0–2657**, a proper prefix of the saved events 0–2887: 205 translations,
31 Boolean inputs, 30 outputs, and 1,196 commutator inputs/outputs. Its indices
and kinds match the emission index entry by entry. Every received commutator
output has full literal-copy and all-pair free-reference acceptance; the exact
set of its 1,196 reference paths equals the complete on-disk reference set.
All these references contain full operand subpath tables and all ordered pair
terms, not samples. The saved statistics report 2,392 checked restrictions,
1,390 changed restrictions, 1,161 nested calls, 35 source-direct calls and zero
occurrence-direct calls. The prefix retains complete free/zero/substituted
polynomials for received outputs. It does not prove identities for the
unfinished Boolean graph, partial K, or the remaining **230 events**.

Reception then fails while saving the evidence for commutator input 2658,
whose parent is Boolean input 2643. The existing streaming aggregate guard
reports **200,000,001 / 200,000,000 bytes**. Its attempted failure receipt
also fails, at **205,762,516 / 200,000,000 bytes**. No
`integration-reception.json` or `integration-reception.failure.json` exists.
The old complete prefix receipt (5,762,516 bytes), its incomplete replacement
`trace-received-prefix.json.partial` (14,004,017 bytes), and the zero-byte
failure-receipt partial remain unchanged. The incomplete replacement is not
a parsed receipt and proves no additional comparisons. This is the §17
documented failure of final-receipt persistence, not a successful recovery.

Nonpartial files total **191,758,498 bytes**; including surviving partials,
physical storage is **205,762,515 bytes**. The writer bounds the resulting
replacement by subtracting the existing destination, and does not bound
simultaneous old/temporary storage. Thus the physical excess is retained and
reported; it is not an accepted aggregate evidence bound. No file is deleted,
no partial is reused, and no capped evidence write is retried.

**Supplemental read-only structural check.** After this evidence stop,
`verify_opposing_stop.py --read-only` reads the complete saved frames and trace
without writing into output-489. Strict proof reception again matches the
audited 212-record digest. It checks every label and endpoint, acyclicity and
full vertex/edge counts of the retained K, partial Boolean and pending block;
the complete Boolean/attach/copy frames agree. Replaying the source recipe
through rows 0–77 binds all **154** seed/transition blocks to actual trace
graphs, with fresh contiguous partitions, every copied interior, exact ordered
cut factors and all attachment connectors. Every retained K record is
accounted for: **227,179 vertices + 291,707 edges = 518,886 records**. All 212
allocated source-root vertices are retained; no identity for the whole partial
K is asserted.

For record 78 the checker binds its exact axiom argument translation to
Boolean input **2643**, reconstructs normalization, all ordered suffix jobs
and the Boolean propagation prefix, and checks every interior, wrapper,
factor and connector of all **128 completed attachments**. The **122 attempted
parent commutators** are matched to the actual ordered recipe and their saved
outputs. The last output, event **2887**, equals the pending sum-commutator
block as a complete parsed graph. At its failed attachment the copy
cursor and vertex count exhaust the entire partial Boolean graph, and all
2,888 events have been consumed. Independent counts give the rejected
2,011,597-record guard above. This confirms structural/count provenance of
the stopped allocation, not free-polynomial reception of the last 230 events.
Original caller and source hashes still match. The check completes with no
failed condition, but deliberately persists **no structural receipt** after
the evidence cap. Its result is reproducible from the unchanged full evidence
and this script; it is not a separate critical audit or complete reception.

The structural helper's first invocation had a syntax error from an unmatched
closing parenthesis; correcting it preceded any execution or output write.
No accepting predicate, construction or cap changed. The successful read-only
invocation and the two actual cap failures are recorded in the step work note.

**Bounds and reproduction.** The persisted arithmetic prefix uses 12,797,863
multiplication pairs / 100,000,000, at most 2,736 polynomial words / 1,000,000,
word length 18 / 256 and 874,665 traversal words / 20,000,000. Full reference
storage has its existing separate guards. These are counters for the saved
prefix only; no counter for the failed replacement or full trace is inferred.
The structural graph counts above are each below 2,000,000; their label-entry
counts respectively equal 291,707, 1,117,028 and 15,300 / 2,000,000. All
original input/name/dictionary/depth limits remain unchanged. No total work,
simultaneous-memory, temporary-storage or recovery guarantee follows.

In a workspace without output-489, execute in order from this notebook, each
prefixed by `PYTHONDONTWRITEBYTECODE=1 python3`,
`scripts/four-rule-extraction/run_opposing_occurrence.py` and
`scripts/four-rule-extraction/verify_opposing_occurrence.py`. The latter's
nonzero exit is the retained evidence-cap failure, not an acceptance. Do not
rerun them over this archive. The read-only structural command is
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/verify_opposing_stop.py --read-only`.
Full raw graphs, pending jobs, all saved trace events and extraction failure
frames are retained in output-489; arithmetic acceptance is limited to its
last complete prefix receipt and 1,196 reference files. No missing final
receipt or unreceived event is silently replaced by a preview or an accepting
flag. This exact constructor/input/cap combination is stopped.

**Qualifications and Mathlib.** This is a new measured failure of this exact
unchanged-copy constructor/input/cap combination, not a mathematical
counterexample, a proof lower bound or progress beyond the checked sources.
The full nonzero-fJ test fails to complete. Attempts 037–041 retain their
original evidence. General proof availability, full K/H reception on this
caller, total interpreter resources, L087 W₂, M-only/ER/Frege and SAT remain
unresolved. A different Boolean representation requires separate assessment;
no sharing identity or cap feasibility is established here. Full matching
Mathlib coverage is **not checked**; no absence claim or DAG change is made.

**21. Isolated final-suffix sharing: necessary retained-interior cap failure —
step 491, 2026-10-25.**

**Hypotheses and source scope.** This is one REPRODUCTION calculation under
the prior SPECIALIZE assessment
`drafts/literature/2026-10-25-stopped-boolean-final-suffix-sharing.md`.
Fix §20's source record 78, Boolean input event 2643, its normalized x-only
graph H, the complete ordered alphabet/dictionary, every CAPS value, existing
whole-operand restriction and literal-empty central selection. The proposed
change shares only one final original-only suffix across beta and product
branches. All selected L035 interiors, their separate copies and the sum
branches remain fixed. No extraction retry, cap increase or production
acceptance change is made. Output-489 and its partials remain untouched.

Reuse L035 (2)/(4), L036 (5)–(9), §§16–20 and L108 §§2,13.
The ready assessment imports only ordered cut semantics and a shared-suffix
precedent from Raz–Shpilka, *Deterministic Polynomial Identity Testing in Non
Commutative Models*, author-hosted 16-page manuscript, Definition 1 p.4 and
§2.2 pp.7–9
(https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf).
Its layered PIT transformation preserves zeroness and is not used as an exact
polynomial-preserving replacement. The unchanged component comparison is
Li–Tzameret–Wang, arXiv:1412.8746v4, 11 September 2015, Lemma 3.7 p.18
(https://arxiv.org/pdf/1412.8746v4), for formula-input commutators. Neither
source certifies this finite cap. No theorem is reproved. A count of unchanged
interiors is necessary before spending resources on a changed graph.

**Conclusion.** Final-suffix sharing alone cannot make this fixed witness fit
the unchanged 2,000,000-record cap. Its independently retained selected
commutator interiors already require **2,099,040 records**. Even discarding
every literal-empty W block leaves **2,098,666 records**. These are lower bounds
on the proposed full graph, excluding all propagation, beta branches, product
prefixes, outside connectors and the shared suffix. This is a failed necessary
resource discriminator, not a claim that the proposed sharing preserves the
free polynomial, nor a lower bound on arbitrary Boolean witnesses.

**Proof of the discriminator and complete finite count.** Normalize the entire
saved operand, rather than extrapolating the stopped Boolean prefix. It has
154 vertices, source/sink 0/1, and 199 singleton edges. Enumerating every
outgoing edge and ordered outgoing pair in L036 (5) gives 199 product-commutator
jobs and 46 sum-commutator jobs. Each actual input is respectively an atom and
a rooted H suffix, or two independently prefixed H suffixes. Apply exactly the
existing whole-operand path restriction to each input before selection.

For a restricted pair A,B let r be the number of literal edge pairs with
nonempty central list (2), and let q count all entries in those lists, with
multiplicity. The unchanged selected W has two exterior vertices, followed
by four disjoint operand copies per retained pair in order A,B,B,A. Each pair
also has four constant connectors and its q-pair central edges. Thus its exact
vertex and edge counts are

    N_W = 2 + 2r(V_A+V_B),
    M_W = 2r(M_A+M_B) + 4r + q.

These are the already justified §16 counts, not an identity test or a new
selection rule. Summing them over **all 245 jobs**, including the unsaved jobs
beyond output-489's stopped call, gives

    sum N_W = 918,110,     sum M_W = 1,180,930,
    sum (N_W+M_W) = 2,099,040 > 2,000,000.

All labels are singleton, so these interiors have 1,180,930 label entries.
There are 187 r=0 blocks, each having exactly two vertices and no edges.
Removing their 374 records, even though that is outside the fixed-copy
proposal, still leaves 917,736 vertices and 1,180,930 edges, totaling
2,098,666 > 2,000,000. Hence this stop is not caused by empty-block wrappers.

By the approved scope, these interiors occupy separate vertex/edge records.
Sharing a fresh final x-only copy does not identify, remove or relabel any of
them, and cannot give a negative outside-record contribution. Therefore the
full proposed graph must contain at least their summed records. The cap fails
before acyclicity, path-bijection or free-polynomial verification of a changed
graph is relevant. No changed graph is allocated and no complete L036 free
reference is evaluated; this proof does not silently substitute f²+f for it.
There is no claim of one-placeholder reception for an unconstructed graph.

**Implementation and independent reception.** The calculation program is
`scripts/four-rule-extraction/count_final_suffix_sharing.py`; its separate
receiver is `scripts/four-rule-extraction/verify_final_suffix_bound.py`.
The latter imports no emitter, correction constructor or path filter.
Both retain the strict caller request checks. The receiver binds the complete
212-record source hash, source row 78 and translation event 2642 to Boolean
input 2643, checks the whole alphabet/dictionary, and independently normalizes
all edge labels. Complete bounded word arithmetic verifies that this input
and normalized H equal the formal translation of the actual source argument.

The receiver reconstructs every L036 job and original edge occurrence.
For each of its two operands it computes bitset transitive closure, separately
from the calculator's forward/backward searches, and checks all retained
vertices, edges, roots, labels and maps. Reachability includes the empty path;
no-path inputs retain only their designated roots with no edges. This is the
existing path-restriction interface, not new semantic trimming. It recomputes
all central lists from typed dictionary positions, retaining literal
multiplicities, then counts each of the four copies and every connector
directly, independently of the calculator's closed count formulas. All 245
job counts and the complete sum agree. Thus the evidence is not a sample,
an extrapolation of the old prefix, or reception via the old disjoint-Boolean
copy predicate.

Full operands, restriction maps, selected central occurrences and per-job
counts are in
`scripts/four-rule-extraction/output-491/retained-interior-bound.json`;
the independent result and all job counts are in `bound-reception.json` there.
The early `checkpoint.json` preserves the input before enumeration. Every new
artifact uses the existing streaming per-file/aggregate evidence guard.
Their aggregate is **1,923,256 / 200,000,000 bytes**, with no partials or failed
writes. Unchanged writer/trusted-path/SHA/temporary-storage qualifications
from §17 and L108 §13 persist. Input-only arithmetic uses 15,725 multiplication
pairs / 100,000,000, at most 304 polynomial words / 1,000,000, word length
16 / 256, and 6,295 stored traversal words / 20,000,000. These counters do not
describe an unperformed Boolean free reference or a full extraction.

In a workspace where output-491 does not exist, reproduce sequentially from
the notebook root with `PYTHONDONTWRITEBYTECODE=1 python3` followed by
`scripts/four-rule-extraction/count_final_suffix_sharing.py`, then
`scripts/four-rule-extraction/verify_final_suffix_bound.py`. Both refuse
overwriting their completed evidence. The receiver verifies a failed necessary
discriminator, not an accepted shared witness. No K/H or nonzero-fJ is received.

**Qualifications and Mathlib.** Stop this exact final-suffix-only modification
of the fixed selected-interior witness. Internal copy trimming, merging or
semantic block deletion would change the scope and need separate assessment.
The full free-polynomial equality and path interface of the sharing proposal
remain unestablished; no such equality is needed to reject its record count.
The independent whole-run evidence stop in §20 is not repaired. General proof
availability, total interpreter resources, L087 W₂, unrestricted ER/Frege/SAT
and uniform worst-case P versus NP remain unresolved. This is new local
negative resource evidence, with no advance beyond the inspected mathematics
or certified novelty claim. L036 is now explicitly recorded as a direct input
for the complete Boolean recipe; no lemma ID is added. Full matching Mathlib
coverage is **not checked**.

**22. Isolated selected-copy endpoint restriction — step 493, 2026-10-25.**

**Hypotheses and source scope.** This is the single finite REPRODUCTION
attempt under the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-25-selected-copy-path-restriction.md`.
Fix §20's source record 78 / Boolean input 2643 / translation 2642, the
212-record opposing-units proof, exact formula trees, alphabet
[y5,y4,y3,y2,y1,y0], complete ordered dictionary and every CAPS value.
Keep §16's whole-operand restriction and literal-empty central selection.
For every retained L035 pair, change only its four internal copies by
restricting each to its designated entry-to-exit paths. Retain four separate
copies, all selected central occurrences and their multiplicities and factor
order. External L036 propagation, beta terms, product suffix copies, serial
wrappers and attachments remain unchanged. No final-suffix sharing, semantic
branch deletion, integration retry or production receiver change is allowed.

Reuse L035 (2)/(4), L036 (5)–(9), §§16–21 and L108 §§2,13. The inspected
primary pruning precedent is Ran Raz and Amir Shpilka,
[*Deterministic Polynomial Identity Testing in Non Commutative Models*,
author-hosted 16-page manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
Definition 1 p.4 and Lemma 2 Steps 1,3,5 pp.5–6 (revision date unestablished,
retrieved 2026-10-25). Step 1 uses constant/linear-edge serial/parallel graphs;
Steps 3 and 5 remove useless vertices and restrict individual output copies.
The theorem's formula-input, zero-free-term, homogenization and PIT bounds
are not imported for arbitrary-root inputs here. This is an application of
the assessed pruning mechanism, with the necessary finite-root specialization
proved below, not a new pruning theorem. Li–Tzameret–Wang,
[*Characterizing Propositional Proofs as Non-Commutative Formulas*,
arXiv:1412.8746v4, 11 September 2015](https://arxiv.org/pdf/1412.8746v4),
Lemma 3.7 p.18, retains its formula-input scope; it is not a cap guarantee
or a specification of this full free polynomial. Only the necessary local
root/path applicability is verified; no formula-size or PIT theorem is reproved.

**Path specialization and polynomial preservation.** Let D be any of the
finite original-only DAG operands and p,q its designated roots for one
internal copy. Reachability includes the empty path. If q is reachable from
p, retain precisely the vertices reachable from p and able to reach q, and
retain every original edge occurrence whose tail is reachable from p and
whose head reaches q. Keep their ordered affine labels and list order;
renumber retained vertices injectively in increasing old-index order.
If q is not reachable, retain just the distinct roots with no edges.
Record both vertex maps, every retained and deleted vertex/edge occurrence,
the original roots and their transported indices.

Every p-to-q path uses only retained vertices and edges. Conversely every
path in the restricted graph maps, edge occurrence by edge occurrence, to
a p-to-q path in D: endpoints and incidences are unchanged under the injective
renumbering. Thus these maps are inverse on accepting paths, preserving
ordered label products and distinct parallel-edge occurrences. An edge
satisfying the stated reachability test lies on an accepting path: concatenate
a p-to-tail path, that edge and a head-to-q path. A repeated vertex in this
directed walk would produce a directed cycle, impossible in D. This also
shows that the retained edges are exactly the edges on accepting paths;
no label value or cancellation is used to select them.

When p=q, a DAG has no nonempty p-to-p path. The retained graph is the single
root with no edges and its path polynomial is 1, as in D. Distinct roots
with no path yield zero in both graphs. Incoming entry edges, outgoing exit
edges and dead components cannot participate in an accepting path and are
removed by the same reachability test. Constant and zero labels are copied
literally whenever their edge survives; cancelling paths, repeated labels,
parallel edges and unequal lengths are preserved rather than detected or
deleted. The fixed normalized witness has singleton labels, but this
path argument does not require that restriction or a nonzero/zero-free-term
promise.

For a selected marked pair e:u→v in F and d:a→b in G, apply this restriction
separately to F[s_F,u], G[s_G,a], G[b,t_G], F[v,t_F]. Keep L035's four
copies disjoint, its four exterior constant connectors and every central
placeholder occurrence from (2). An accepting branch path must enter and
exit each copy at precisely those roots. There is no other inter-copy edge.
The four path bijections therefore give a bijection of complete branch paths
with the former four-copy construction, preserving the central occurrence
and the full factor order in (4). Empty paths and no-path factors are already
covered. In particular the equality is in the free enlarged alphabet before
placeholder substitution, not merely an equality after substitution. All
selected pairs and their multiplicities remain; literal-empty pairs still
contribute zero. Summing gives exactly the prescribed L035 free polynomial.

L036's outer construction is unchanged, so replacing each child by this
equal free polynomial preserves each R_u in (6), the reverse-topological
recurrence (8), and the complete sum (9). The free, zero-placeholder and
axiom-substituted polynomials agree with the original recipe. Every accepting
path still chooses one local branch, and exactly one central/sigma edge in
that branch; original-only subpaths and exterior connectors add no placeholders.
Acyclicity is preserved within each restriction and by the unchanged forward
copy/branch order. This is a specialization argument for the approved finite
interface, not an unrestricted proof-complexity or SAT theorem.

**Constructed finite inventory and preflights.** Paths in the remainder of
this section are relative to `scripts/four-rule-extraction/`.
`restrict_selected_copies.py` saves an early checkpoint and then all 245
L036 jobs (199 product and 46 sum jobs), rooted at the complete normalized
154-vertex/199-edge operand, rather than the stopped prefix. It preserves
output-491's original operands, whole-operand maps and central selection.
For each selected pair it records four complete restriction maps and counts
all retained vertex/edge records, four connectors and central multiplicities.
The summed new interiors have 459,300 vertices and 578,278 edges, totaling
**1,037,578 / 2,000,000 records**. The complete external recipe is preflighted
before Boolean allocation: **495,889 vertices + 626,043 edges = 1,121,932
records / 2,000,000**, with **626,043 / 2,000,000 label entries**. Copies
remain separate; all 187 empty W wrappers are kept. The actual allocation
must match these complete preflights. Full graph and occurrence partitions
are saved in output-493/restricted-boolean.json; the earlier inventory and
complete bound remain in restricted-interior-bound.json and full-count.json.
These constructor counts alone are not independent reception.

**Independent receiving design and implementation qualification.**
`verify_restricted_copies.py` imports no emitter, correction constructor or
path filter. It rechecks the entire source through the unchanged strict
caller interface, binds row 78 and both trace events, independently normalizes
every edge, and reconstructs all ordered original L036 jobs. Bitset transitive
closure, independently of the constructor's forward/backward searches,
reconstructs both whole-operand cuts and each internal cut for each reached
job. Its checks compare all retained/deleted occurrences and transported
endpoints, every copied edge/label, exact fresh vertex and edge ranges,
central occurrences and connectors. Exhausting all contiguous partitions
disallows extra, missing or cross-copy records. A later, **unexecuted** stage
checks complete external L036 propagation, factor wrappers, suffix copies,
attachments and final sink in their original order. This separate predicate
does not weaken §16's production literal-full-copy receiver. Actual completed
reception is limited to the prefix stated below.

For a reached job the arithmetic reference is L035 (4), computed from
independent complete prefix/suffix tables for both original selected operands.
All its edge pairs are examined; literal-empty central lists contribute exactly
zero without semantic testing. For a completed job, every nonempty marked
term, including those that cancel, and all reference tables are saved with
free/zero/substituted polynomials. The receiver compares the changed W against
that reference and its substituted ordered operand commutator. Its implemented
but **unexecuted** final stages independently assemble every R_u and recurrence
(8), compare the whole graph in all three modes with that full Boolean
reference separately from f²+f, and check forward structural placeholder
counts without coefficient cancellation. No all-job or whole-Boolean result
is inferred from that code's presence.

The first receiver execution was interrupted in job 7 after seven completed
reference files, in Arithmetic.mul's repeated scan of the full accumulated
word set after each pair. No cap/equality failure was observed; interruption
counters are unavailable. Its exact code is preserved as
output-493/receiver-before-incremental-check.py and references remain under
output-493/references/. The resumed receiver writes references-received/.
Its local IncrementalArithmetic.mul retains the same pair iteration,
concatenations, symmetric-difference updates, pre-concatenation length guard,
pre-insertion size guard, cumulative pair guard and final inherited check.
Every surviving word was length-checked when inserted. Removing a word
cannot increase size or maximum length; every new global maximum therefore
occurs on an insertion. Updating the two global maxima there gives the same
counters as the original per-pair scan, for the same iteration order. The
empty-product final check is retained. Seven diagnostics compare complete
outputs, errors and counters with the original engine, including collision,
empty, length-rejection and exhausted-pair cases; these finite comparisons
support implementation checking, not the invariant proof. No shared module
or CAPS value changes, and no capped-reference failure is bypassed.

**Reception outcome: terminal stored-word cap failure.** The resumed receiver
stops in **job 7**, a sum-commutator whose completely partitioned changed
graph has **81,464 records**, during its backward graph evaluation. The
unchanged Arithmetic.evaluate guard reports

    stored traversal words = 20,010,316 > 20,000,000.

This counter sums the sizes of the retained vertex-polynomial table as it
is populated. It is not the size of the output polynomial, a graph-record
count, or a lower bound on every exact evaluator. The guard occurs after
job 7's occurrence/map/partition checks and construction of its arithmetic
reference, but before the equality comparison and reference-file write.
The failure receipt does not identify which of the three evaluation modes
failed; no mode-specific acceptance for job 7 is inferred. Its full reference
and traversal table are not persisted. There is no complete reference file
for jobs 7–244, no complete outer occurrence receipt, and no complete Boolean
free/zero/substituted reception. In particular constructor record savings
alone do not pass the approved discriminator.

The complete preserved result is output-493/reception.failure.json, not an
accepting receipt. Its failed-process counters are **35,748,627 / 100,000,000
multiplication pairs**, **982,700 / 1,000,000 maximum polynomial words**,
**31 / 256 maximum word length**, and the rejected stored-word count above.
These include partial job-7 work and are not complete-run or accepted memory
bounds. No cap is raised, failed reference retried, or accepting production
predicate changed. Stop this exact restricted-copy/backward-word-receiver
combination. This is a measured finite receiving failure, not a counterexample
to the path-bijection proof or a lower bound on other representations.

Exactly jobs **0–6** have completed reference files. The metadata-only
`summarize_restricted_stop.py` compares all seven original and resumed files
as complete parsed objects; they agree, and it preserves hashes/sizes of
every existing artifact in output-493/stop-summary.json. It does not evaluate
a graph or repeat a failed calculation. The complete evidence aggregate,
including the interrupted code snapshot and both sets of seven reference
files, is **67,457,028 / 200,000,000 bytes**; no partial file remains. This
accepted byte count does not repair the failed arithmetic guard or §20's
independent whole-run evidence stop. All output-489/491 artifacts and prior
unfinished work remain untouched.

**Reproduction.** In a workspace without output-493, run from this notebook
with `PYTHONDONTWRITEBYTECODE=1 python3` followed by
`scripts/four-rule-extraction/restrict_selected_copies.py`, then
`scripts/four-rule-extraction/verify_restricted_copies.py`. The latter's
nonzero exit at the stored-word guard is the expected negative result, not
acceptance. The historical interrupted receiver and seven old references are
preserved evidence, not prerequisites of the resumed mathematical test;
their exact snapshot remains in output-493. The metadata summarizer expects
that preserved interruption prefix. All constructors/receivers refuse
overwriting their respective completed/failed evidence. Do not rerun them
over this archive. No integration is executed.

**Qualifications and Mathlib.** No K/H, nonzero-fJ or whole-run reception is
performed. §20's independent evidence obstruction is unresolved. Trusted
paths, remaining SHA bindings, temporary-storage and total interpreter-resource
qualifications persist. General proof availability, L087 W₂, unrestricted
ER/Frege/SAT and uniform worst-case P versus NP remain unresolved. This is
local reproduction of the assessed mechanism, with no claim beyond the
checked sources or certified originality. Full matching Mathlib coverage is
**not checked**. Existing mathematical DAG inputs already include L035,
L036 and L108; no new ID or edge is needed.

**23. Fixed job-7 forward reception: reference-evidence stop — step 495,
2026-10-25.**

**Hypotheses.** Receive exactly the prior SPECIALIZE target in
`drafts/literature/2026-10-25-forward-selected-job-reception.md`:
test free, zero-placeholder and substituted forward evaluation of §22's
unchanged restricted job-7 commutator against complete L035 references,
under every original CAPS value. The fixed inputs are output-493 job 7,
its inventory, failure and stop summary; output-491's matching inventory;
and output-489 row 78 / translation 2642 / Boolean input 2643. Preserve the
212-record source, literal trees, ordered alphabet [y5,y4,y3,y2,y1,y0],
complete dictionary, all selected occurrences, four separate copies and
F-prefix, G-prefix, central, G-suffix, F-suffix factor order. This is an
isolated REPRODUCTION attempt, with no backward W traversal, cap increase,
production change or integration retry.

**Conclusion.** The changed receiving mechanism stops at its complete raw
reference-evidence budget **before any forward W evaluation**. The proposed
aggregate reaches **200,000,001 > 200,000,000 bytes** during the reference
file's counting pass. This is the first observed over-cap prefix, not a
computed exact size of the complete proposed file, and not a lower bound
for every encoding. No job-7 all-mode equality, forward storage bound,
complete raw reference receipt, Boolean/K/H or nonzero-fJ reception follows.
The structural reception succeeds as qualified below. The result is new
finite negative evidence for this interface, not mathematics beyond the
reused sources or a P-versus-NP conclusion.

**Proof and source applicability.** Reuse L035 (2)/(4), L036 (5)–(9),
L108 §§2,11,13 and §§16–22. The inspected primary reference is Ran Raz and
Amir Shpilka, [*Deterministic Polynomial Identity Testing in Non Commutative
Models*, author-hosted 16-page manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
Definition 1 p.4, Lemma 2 Steps 1–2 p.5 and §2.2/Theorem 4 pp.7–9,
revision date unestablished, retrieved 2026-10-25 in step 494. Ordered path
semantics are reused; the layered homogeneous PIT bound does not certify
this full-word expansion or its raw evidence. Li–Tzameret–Wang,
[*Characterizing Propositional Proofs as Non-Commutative Formulas*,
arXiv:1412.8746v4](https://arxiv.org/pdf/1412.8746v4),
11 September 2015, Lemma 3.7 p.18, retains its formula-input scope.
No theorem is reproved to claim a new forward algorithm or finite cap bound.

`scripts/four-rule-extraction/receive_forward_job7.py` reuses the audited
integer-letter `Forward` arithmetic, adding a caller-wide retained-storage
guard to its same topological edge sweep. Starting with the empty word at
the designated entry, each incoming predecessor path appends its edge label
on the right. Topological induction gives precisely the ordered path sum
at each vertex, as in L108 §11. Incoming entry edges have zero
entry-reachable predecessor polynomial: otherwise they close a directed
cycle. Outgoing exit edges cannot return to the exit. Coincident endpoints
have only their empty path; no-path endpoints give zero. Constants append
the empty word, parallel edges contribute separately, and integer
coefficient reduction preserves F₂ cancellations. No root extremality,
layering, equal path length or nonzero promise is required. This checks
applicability of the existing invariant; it establishes no resource saving.

The separate typed-set arithmetic reconstructs complete original-operand
prefix/suffix tables and the marked sum (4), without traversing changed W
backward. A shared multiplication counter charges both engines before every
multiplication, without resetting between modes. The retained-storage ledger
jointly charges all operand tables, marked terms, complete references,
ordered products/commutator, every completed and partial forward table and
every separately decoded mode result. Completed entries are not released.
Replacement of a destination polynomial uses the original replacement
accounting convention. Temporary integer counters retain the original
polynomial-word and word-length guards. This is a retained-word measure,
not a total interpreter-memory bound.

The structural stage independently reconstructs all **37,050** edge pairs,
the **120** nonempty central lists with their multiplicities, both
whole-operand maps and all **480** internal restrictions by bitset closure.
It checks every retained/deleted occurrence and transported root, copied
edge/label, all four exterior connectors per selected pair, central edges
and exhausted vertex/edge partitions. All 480 fixed copies have distinct
roots and an entry-to-exit path. The received graph has **35,762 vertices +
45,702 edges = 81,464 / 2,000,000 records**, with **45,702 / 2,000,000 label
entries**. Its forward structural state at the sink is exactly **{1}**,
before coefficient cancellation. This structure-only result is saved
completely in `scripts/four-rule-extraction/output-495/structure.json`;
it does not receive the whole Boolean graph or other jobs.

The process then computes its independent reference and ordered operand
commutator. Its next stage sizes the complete proposed raw reference file
before writing it. The reference writer emits every word and every marked
term directly from retained sets, without retaining a second serialized
polynomial; JSON set ordering is immaterial. Both per-file and aggregate
200,000,000-byte guards apply during sizing. Upon the first over-cap prefix
it rejects before opening the proposed file. Thus existing evidence is
preserved and a failed receipt can be written under the original aggregate
cap. This changes neither equality acceptance nor the byte limit; it avoids
losing the failure receipt as in §20. It is not compression, sampling or
acceptance of incomplete references.

At failure the jointly retained word count is **8,624,336 / 20,000,000**:
23,740 operand-subpath words; 10,996 words in the last retained left
intermediate; 7,466,212 marked-term words across all modes; reference sizes
982,700 (free), 0 (zero) and 38,392 (substituted); ordered product sizes
34,728 and 29,176; and 38,392 in their commutator. The complete failed receipt
records **12,689,318 / 100,000,000 multiplication pairs**,
**982,700 / 1,000,000 maximum polynomial words**, and **31 / 256 maximum
word length**. These are partial-process counters only. The legacy reference
engine's `max_stored_words=0` is not the memory measurement; the joint ledger
is. Forward metrics are all zero and its position is null: **no forward mode
started**. In-memory reference construction is not substituted for the
missing complete persisted reference. No all-mode reference acceptance is
claimed from this stopped process.

The output contains exactly the checkpoint, complete structural evidence and
`scripts/four-rule-extraction/output-495/reception.failure.json`, totaling
**1,877,489 / 200,000,000 bytes**. There is no reference file, partial file,
mode receipt or accepting receipt. The first rejected proposed aggregate
count is distinguished from this actual saved aggregate. All prior artifacts
remain untouched. Reproduce only in a workspace without output-495 using
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/receive_forward_job7.py`;
the nonzero exit at the byte guard is expected negative evidence. The script
refuses an existing output directory. Do not retry this stopped interface.

**Qualifications and Mathlib.** This stops the explicit raw-reference
interface, not forward path semantics, §22's path bijection, every possible
encoding or noncommutative identity testing. Any alternative identity
receiver requires a separately assessed interface and cannot count as
passing this full-word contract or weaken production acceptance. Jobs 8–244,
complete Boolean/K/H/nonzero-fJ reception, the independent whole-run evidence
stop, trusted paths/SHA, total resources, certificate availability, L087 W₂
and unrestricted ER/Frege/SAT remain unresolved. Full matching Mathlib
coverage is **not checked**. Existing DAG inputs suffice; no ID or edge changes.

## Mathlib

Full matching coverage of this transfer, the Frege extraction, the
explicit affine-ABP construction and its binary/time ledger: **not
checked**. No absence or machine-verification claim is made. Precise
primary imports and their restricted roles are stated above. The
ordered tester correction and graph reception are proved here rather
than inferred from Boolean equality of the two-order product.
