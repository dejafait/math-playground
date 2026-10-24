# L104 — Supplied source incidence width gives an exact occurrence witness

## Hypotheses

Work over F₂. Supply an explicitly written unsatisfiable CNF F of
clause width at most three, together with exactly L087's occurrence
pair D,E and its complete provenance, names, orders and dictionaries.
Retain its actual ordered free-ring polynomials f=r_D, g=r_E and its
Boolean/commutator dictionary B with placeholders σ_i,τ_ij. M is exactly
L087's pre-witness full input length. No changed source formula or
Boolean-equivalent pair may replace these objects.

Define I(F) to be the simple bipartite incidence graph with one vertex
for every written clause position and one vertex for every source
variable occurring in F. Membership gives an edge, irrespective of
literal sign or multiplicity. Distinct clause positions remain distinct
vertices even when their clauses agree. Empty clauses are isolated
clause vertices. Declared but nonoccurring names are retained in the
source serialization but are not vertices of I(F).

Supply a finite explicit tree decomposition (T,(X_t)) of I(F) of width
at most k, where k is a nonnegative integer. All bags, tree edges,
vertices, names, headers and references are written. Permit empty bags
and a one-node empty decomposition of the empty graph. Set, before
construction,

    Q = 2 + M + |F| + |decomposition|.

Sizes mean full binary lengths, not numbers of clauses, bags or states.
No generated resolution proof, witness or witness-degree parameter
enters Q. All supplied unused records remain charged.

## Conclusion

A deterministic construction produces an explicit acyclic affine-F₂
ABP H using only L087's occurrence originals and σ,τ, with the formal
identities

    H(y,0)=0,                 H(y,B(y))=fg.

For fixed absolute constants C,c,a, independent of F,k and the supplied
decomposition, both its full binary size and deterministic bit
construction time are at most C 2^{c k}Q^a. Complete dictionaries,
names, references, independent graph copies and the retained source,
decomposition and generated ordinary-resolution records are included.
The algorithm may reject malformed input; on a valid satisfiable input
it may instead report satisfiability and need not output H.

This specializes known incidence/primal-width, elimination and
directional-resolution machinery and audited L097. It is REPRODUCTION,
with no certified originality or verified implementation. The separate
step-409 all-size informal critical audit below finds no substantive
defect in the reception, identities or full size/time ledger. It supplies
neither small decompositions for arbitrary sources, general short
proofs, an M-only bound, universal W₂, arbitrary ER data nor an answer
to P versus NP. In particular it is not a main-problem candidate.

## Proof

**1. Coverage and precise imports.** The pre-invocation SPECIALIZE
assessment is
`drafts/literature/2026-10-22-source-incidence-width-supplier-specialization.md`.
Its completed comparison is
`drafts/literature/2026-10-21-source-incidence-width-occurrence-witness.md`.
Reuse those searches, applicability limits and stopped-route comparisons;
no fresh discovery or stronger unread construction is an input here.

Import the following results in exactly their inspected versions.

* Phokion G. Kolaitis and Moshe Y. Vardi, *Conjunctive-Query Containment
  and Constraint Satisfaction*, JCSS 61(2), 302–332 (2000),
  [DOI 10.1006/jcss.2000.1713](https://doi.org/10.1006/jcss.2000.1713),
  [31-page author full version, printed p.25](https://www.cs.rice.edu/~vardi/papers/pods98rj.pdf),
  unnumbered incidence comparison: replacing each tuple vertex in
  each bag by its elements converts incidence width k to structure
  width at most a(k+1)−1 for maximum arity a. No manuscript revision
  date was established. Only this direction is used.
* Hans L. Bodlaender, Bart M. P. Jansen and Stefan Kratsch,
  *Preprocessing for Treewidth: A Combinatorial Analysis through
  Kernelization*, [arXiv:1104.4217v2, Proposition 7 and proof,
  printed p.23](https://arxiv.org/pdf/1104.4217v2). The version label
  is 26 September 2013; the PDF title page says 3 October 2018.
  Weighted treewidth at most w is equivalent to an elimination
  ordering of closed-neighborhood cost at most w+1. Use unit weights
  and its forward construction: complete bags to cliques in H_c and
  repeatedly remove a simplicial vertex of the remaining H_c.
  Simpliciality is tested in this completion, rather than in the
  uncompleted primal graph. No optimal-decomposition finder is used.
* Irina Rish and Rina Dechter, *Resolution versus Search: Two Strategies
  for SAT*, J. Automated Reasoning 24(1–2), 225–275 (2000),
  [58-page author manuscript](https://ics.uci.edu/~dechter/publications/R80.pdf),
  Figure 4 printed p.7 and Theorem 1 p.8; Definition 1 p.11;
  Lemmas 1–2/Theorem 4 p.12; Appendix A pp.54–55. No manuscript
  revision date was established. Directional resolution (DR),
  processing buckets from the highest variable downwards, is sound
  and complete. For induced width w its distinct nontautological
  bucket clauses number at most 3^{w+1} per bucket, the stored
  directional extension has at most n3^{w+1} clauses, and the stated
  operation time is O(n9^w). Figure 4 performs actual resolution,
  with its unit-resolution branch when a unit is present. The
  operation count is not a binary proof-export bound.

Their general structural and resolution theorems are imported, not
reproved. The following details justify the clause-position conventions,
constructivity, original-leaf reception and full binary export that
those statements do not supply verbatim. L087 supplies the exact pair
interface; L097, including its step-380 constant-axiom repair and audit,
supplies the final polynomial receiver. No claim about general ER or
renaming normalization is used.

**2. Validate the data and preserve the source.** Parse the actual
serializations before allocating any claimed counts. Check the width
three syntax, the naming/provenance map, all decomposition references,
and that T is a tree. Check coverage of every graph vertex, edge
coverage by a bag, and connectedness of the bags containing each vertex.
These are finite scans and graph searches of polynomial bit cost in Q.
L087's provenance can be checked by reconstructing its two transition
systems with the supplied names, as allowed by L097. Do not change the
actual occurrence alphabet, D,E,B or M.

Compute the actual nonnegative decomposition width

    κ = max(0, max_t |X_t| − 1) ≤ k.

Thus κ≤C₀Q for a fixed encoding constant, even if the supplied upper
bound k is much larger. All algorithms below use the written bags and
actual vertex sets, not an array of length k or an enumeration in k.
An empty-clause position in F gives L097's direct zero branch: D's
root is absorbing failure, hence f=0 formally by the suffix recurrence.
A zero graph with distinct endpoints and no accepting path, retaining
the full dictionaries, satisfies both identities. Keep the supplied
source and decomposition. This case has polynomial size/time in Q.
Assume below that F has no empty clause.

Make an auxiliary clause-set view F₀ solely for DR. For each written
clause, sort signed variable names, remove repeated copies of the same
literal, and discard that clause if it contains both signs of a
variable. Keep one representative of identical remaining clauses,
choosing the earliest original position deterministically. Retain a
table of all original positions, literal positions, removed repetitions
and the chosen source association. Tautologies impose no constraint;
idempotence of OR and conjunction shows F₀ and F have the same satisfying
assignments. This is normalization of an auxiliary clause view, not a
replacement of the supplied F in L087 or L097.

Clauses in ordinary resolution are finite literal sets. A leaf for a
normalized clause is therefore the associated original clause with its
set interpretation; attach its actual original literal list and position
to the leaf record as well. If ordered clause syntax is used in the
receiver, L097 §3 explicitly pays permutation, rebracketing and duplicate
removal by propositional congruence. No new resolution axiom asserting
a strengthened clause is introduced. Dropped tautologies and duplicate
clauses need not be proof leaves. All their source/occurrence records
remain in the actual F and in the original-Q accounting.

**3. Receive the incidence conversion and obtain the order.** In each
bag retain its variable vertices and replace each clause-position vertex
j by the set V(C_j) of distinct source variables in that clause. Call
the result X'_t. Every replacement adds at most three variables, so

    |X'_t| ≤ 3|X_t| ≤ 3(κ+1),       W := 3κ+2.

This is the cited incidence conversion on clause-position constraints.
Its direct reception can also be checked in these conventions. For
each variable x, its original bag subtree T_x meets the subtree T_j
of every incident clause j, by the incidence-edge coverage condition.
The new bags containing x form exactly
T_x ∪ ⋃_{j:x∈V(C_j)}T_j, a connected nonempty union. Every pair of
variables in a clause occurs together in every replaced bag containing
that clause position. Thus these bags cover the original primal graph,
also when clauses or literals repeat or a clause is tautological.
No new variable is introduced. Empty clauses would replace a position
by the empty set and have already been handled separately.

Let V be the set of variables occurring in the original F, n=|V|.
Retain all of them, including names occurring only in discarded
tautologies; they may be isolated in F₀'s interaction graph G₀.
Completing the X'_t bags to cliques gives H_c. By the constructive
direction of Proposition 7 it is chordal with clique size at most W+1.
Choose, by a deterministic ordering of the input names, the first
simplicial vertex of the current induced H_c, remove it, and repeat.
Brute-force neighborhood-clique tests suffice: n stages, n candidate
vertices and at most n² adjacency checks per candidate, all polynomial
in Q. Write the resulting elimination order v₁,…,v_n in full.

Use the reversed list o=(v_n,…,v₁) for the DR manuscript's convention.
Its first processed bucket then eliminates v₁. The interaction graph
G₀ is a subgraph of H_c on V. Along this order its elimination fill
stays inside H_c: each inserted edge joins surviving neighbors of the
current simplicial vertex, which are already adjacent in H_c.
Consequently the induced width w of G₀ in the DR convention satisfies

    w ≤ W = 3κ+2 ≤ 3k+2.

Isolated variables have empty buckets. On the present unsatisfiable,
nonempty-clause input, n≥1; the zero-variable/empty-conjunction case
cannot meet unsatisfiability and may report satisfiability. The order,
filled-graph records and converted bags can all be retained at
polynomial cost in Q. This is construction from a supplied decomposition,
not a search for one.

**4. Export complete ordinary-resolution records.** Run Figure 4's DR
on F₀ in order o. Each bucket stores distinct nontautological clause
sets, each with an earlier proof-record identifier. Initialize each
clause with its associated original leaf from §2. At a bucket without
a unit, enumerate the positive/negative pivot-parent pairs in a fixed
lexicographic order. With a unit, select the first unit and perform
the unit resolutions with the opposite-polarity clauses in that bucket;
if its opposite unit is present the empty clause is obtained. This is
the unit branch of Figure 4, not an assignment axiom. Pure-polarity
buckets need no inference. Resolvents go to the bucket of their highest
remaining variable, which is strictly earlier in o. Tautological
resolvents do not enter buckets; duplicate clause sets retain an existing
bucket reference. An empty resolvent terminates the procedure.

The selected-unit convention is justified locally: with that forced
pivot value, every same-polarity clause is satisfied, and every
opposite-polarity clause has exactly its unit resolvent as residual.
Thus this branch imposes exactly the residual constraints of the
bucket. Selecting one unit loses no constraint; two opposite units
produce the empty clause. This fixes the manuscript's unspecified
unit-selection detail without assuming a stronger inference rule.

Whenever a resolution is actually performed, append its full resolvent
list, pivot name and two parent references to the proof, before the
bucket duplicate/tautology filter. Thus even an unused repeated or
tautological resolvent has a valid ordinary-resolution record. It
need not enter any bucket or be used later. All parent references
point backwards to actual written leaves or generated records; selected
bucket references are never deleted from the proof archive. Processing
a bucket stops future use of that bucket, not preservation of its
records. Unit inferences have the same two-parent format. No extension
axioms, fresh propositional variables, semantic inference or proof-tree
unfolding occurs. A record can be reused by arbitrarily many later
references without copying its ancestry.

Dropping tautological clauses and using sets is the cited counting
convention. The imported Theorem 1 supplies completeness for DR in
that convention; F₀ is unsatisfiable, so the process reaches the empty
clause. The resulting archive π is a valid ordinary-resolution DAG
refutation of the original F under the leaf convention already
specified, even though it may include unused records. It is not merely
a decision trace or a dynamic-program table. A direct scan can check
every pivot, literal-set union, original association and reference in
the completed archive. Such a scan is verification of π's actual
inferences, not a test of the unsatisfiability promise by assumption.

**5. Binary ledger in original Q.** Use the bucket bound from Lemmas
1–2/Theorem 4, including the Appendix A distinction between original
and derived edges. Put

    b := 3^{w+1},             A := 9^{3κ+3}.

There are at most nb² pivot-pair operations over all buckets, including
the unit branch; hence nb²≤nA. This counts every emitted resolution
record, even those later excluded from bucket storage. There are at
most n b distinct bucket clauses and at most the number of written
source clauses initial records. The count is bounded by C A Q, since
n, the source clause count and every name length are at most C Q.

Each record has at most n variables, at most one of each sign except
in the permitted tautological conclusions, and two references. A full
literal list, even repeating original Q-bit names at every occurrence,
costs O(Q²) bits. A reference uses
O(log(AQ))=O(κ+log Q)=O(Q) bits, because κ is actual written width.
Original leaf lists have at most three literals. Full proof dictionaries,
source associations, all generated records and optional pair-result
annotations therefore have the conservative common bound

    |π| + |retained source/decomposition/order records| ≤ C₁ A Q⁴.  (1)

Bucket lookup can be deterministic without expected hashing or unit-cost
large identifiers. Scan at most nb stored distinct clauses per proposed
insertion, comparing their full literal lists. There are at most nA
pair operations and at most C A Q stored records to scan, each of
polynomial bit length in Q. Full-name sorting, unions, tautology tests,
pair enumeration, backward references, output writing and a final
inference-verification scan consequently fit the loose bound

    preprocessing + proof export/check time ≤ C₂ A² Q⁸.          (2)

Polynomial graph construction, simplicial tests, input validation and
original associations fit (2) as well. It also pays quadratic scans
of the full bound (1). Increasing constants accommodates fixed binary
framing. There is no enumeration of all n^w variable subsets. The
exponential factor comes only from a fixed-base power of the induced
width. An oversized declared k is not used in these allocations.

**6. Apply the unchanged-source receiver.** Feed L097 the original F,
the complete π, and the unchanged L087 pair/provenance/B/M package.
All leaves of π have the recorded original associations; all inference
names belong to V. L097 allows the clause-set/list reconciliation,
reuse, tautologies and unused records just described, and its hypotheses
do not require every clause or proof line to be used. It therefore
returns H with exactly H(y,0)=0 and H(y,B(y))=fg. It does not run L087
on F₀, change the order of either tester, or identify two different
products using Boolean vanishing. Its group-polynomial correction and
constant-axiom cases remain the audited ones; no new extraction is
needed here.

To avoid confusing its input length with original Q, write

    R = 2 + M + |F| + |π| ≤ C₃ A Q⁴.

The retained decomposition and preprocessing archive in (1) remain
charged even though L097 need not read them. By L097 (11)–(12), fix
one component-algorithm exponent d₀≥6 and set

    t = 12 max(30, 2d₀+2) ≥ 360.

These are fixed constants, independent of the instance and width.
L097 gives |H|≤C₄R^{168} and construction time ≤C₅R^t. Combining
with (1)–(2), and retaining all earlier artifacts, yields

    total full output size ≤ C₆ A^{168} Q^{672}
                           = C₆ 9^{504(κ+1)} Q^{672},
    total bit time         ≤ C₇ A^t Q^{4t}
                           = C₇ 9^{3t(κ+1)} Q^{4t}.        (3)

The preprocessing term A²Q⁸ is absorbed since t≥360. Taking
c=3t log₂9, a=4t and enlarging C absorbs the fixed factors with
κ≤k, giving the announced common C2^{c k}Q^a bound. In particular
the exponent of Q never depends on k. Every L097 dictionary/copy is
already in R^{168}; all preliminary records are additionally retained.
Nothing recomputes M or original Q after expansion.

**Qualifications and test result.** The fixed-exponent/full-record
threshold is met by (3), conditional only on the explicit supplied
structural promise and the stated known/local inputs. For any fixed
α, k≤α log₂ Q makes this a polynomial in Q (with constants depending
on α). This observation supplies no logarithmic-width decomposition
for general sources, no bound in M alone without accounting for the
source/decomposition, and no unrestricted witness or SAT theorem.
L071's signed-value graph and L096's small-core promise are different;
the stopped renaming procedures in L102/L103/Attempt 035 are not used
or reopened. No executable certificate or implementation is asserted.
The separate audit below checks the original-source leaf convention,
the precise DR unit branch and the complete ledger, including unused
resolvents, without changing the construction or its bounds.

**Independent critical audit — 2026-10-22, step 409.** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-22-incidence-width-supplier-critical-audit.md`.
This audit reads the whole construction and checks reception against
L087's actual occurrence construction and L097's hypotheses, §3,
(11)–(12) and step-380 repair. It reuses the completed source comparison
and narrowly rechecks the primary passages cited in §1: Kolaitis–Vardi
p.25; Bodlaender–Jansen–Kratsch Proposition 7/proof p.23;
Rish–Dechter Figure 4/Theorem 1 pp.7–8, Definition 1 p.11,
Lemmas 1–2/Theorem 4 p.12 and Appendix A pp.54–55. The source versions
and qualifications in §1 are unchanged. No stronger unread construction
or new general theorem is used.

1. **Exact source and small cases.** A repeated source literal retains
   its distinct L087 occurrence name, even though its auxiliary
   resolution clause has only one copy of that literal. Every retained
   auxiliary clause has an actual original position whose set of signed
   literals is exactly that clause. L097 first obtains the guarded
   original list and then applies its explicit exchanges, associativity
   and idempotence; no stronger leaf is silently asserted. Equal source
   clauses can share an auxiliary reference, while their original
   occurrences stay separate. A tautological original clause may be
   omitted from the proof leaves, but is still present in F, D and E.
   Variables appearing only in such clauses stay in V and in the
   original incidence conversion. Declared nonoccurring names stay
   charged without becoming graph vertices or output originals.
   An empty clause makes every root-reachable D suffix the failure
   suffix, hence zero formally; unreachable live states cannot change
   f=0. The direct zero ABP therefore handles also a source consisting
   only of empty clauses. With zero occurring variables and no empty
   clause, F is the empty conjunction and is satisfiable, outside the
   unsatisfiable promise. Empty bags cause no coverage exception.

2. **Converted decomposition and order.** For each occurring x the
   original connected nonempty bag set T_x meets each incident T_j.
   Thus their union, exactly the new bags containing x, is connected.
   Each primal edge has both endpoints in a replaced clause bag.
   This verifies the conversion even with distinct repeated-clause
   vertices, repeated literal positions and opposite signs. At most
   three variable names replace one clause vertex, so the bag bound
   is 3(κ+1), not 3κ. Proposition 7 applies with unit weights to these
   bags. Its chordal completion is the graph searched for simplicial
   vertices. Each remaining closed neighborhood there is a clique
   of size at most 3κ+3; all fill edges for the subgraph G₀ remain
   inside it. Reversing the computed elimination list is essential:
   the highest-first DR convention then eliminates the same first
   vertex, giving w≤3κ+2. Empty buckets and variables isolated in G₀
   do not invalidate this argument or require a new graph vertex.

3. **Unit selection and ordinary records.** A unit in a bucket must
   be a literal on that bucket's pivot. Fix the selected unit's value.
   Same-sign clauses are then true; each opposite-sign clause has
   exactly its pivot-deleted residual, produced by resolving it with
   that unit. Conversely any assignment satisfying these residuals
   extends by the fixed pivot value to satisfy the whole bucket.
   Other active buckets contain no occurrence of this pivot. This
   checks the selected-unit specialization in both directions; an
   opposite unit immediately supplies the empty resolvent. It uses
   the existing unit as a proof parent, never an added assignment
   axiom. In a bucket without a unit, the imported DR pair procedure
   is unchanged. Duplicate resolvents impose no additional constraint
   and tautologies impose none, so the bucket filter preserves this
   reception of completeness. Each emitted record has two previously
   written parents and the exact set union after removing opposite
   pivot literals. Its association is valid whether it is retained,
   discarded as a duplicate, tautological, or unused. Bucket reuse
   refers to an existing proof record and cannot create a forward
   reference. The empty record concludes an ordinary refutation of F,
   not an equisatisfiable replacement with extension axioms.

4. **Every written record is counted.** The source bound concerns
   distinct nontautological bucket clauses. Here each bucket has at
   most b=3^{w+1} such parent references and receives no new clause
   after its processing begins: every generated nonempty resolvent
   goes strictly earlier. Thus there are at most b² actual pair
   operations there, including the selected-unit case. Filtering
   occurs after export, so n b² pays all generated records, not just
   the retained ones. Tautological exports never become future
   parents. Initial records and the entire original-position table
   have polynomial size in Q. Since b²=9^{w+1}≤9^{3κ+3}=A, the
   full record count is at most C A Q. Each generated literal set
   has at most 2n signed literals even if tautological; its full
   names cost O(Q²). References cost O(log(AQ))=O(Q), using the
   actual κ≤C₀Q rather than the possibly huge declared k.
   Equation (1)'s C₁ A Q⁴ therefore has sufficient room for lists,
   associations, dictionaries and retained preliminary data. Explicit
   insertion comparisons and even quadratic scans of that complete
   encoding fit C₂ A² Q⁸. No implicit unit-cost operation on large
   names or unfolded proof ancestry is needed.

5. **Receiver and composed threshold.** The exported proof has exactly
   L097's ordinary-resolution premise; all proof variables occur in
   original F. L097 receives F itself and its unchanged occurrence
   package, including the four gadget occurrences. Its normalization
   and corrected constant-axiom extraction cases are already audited.
   Consequently its output identities concern the actual fg and B,
   without using Boolean equality to equate reordered free polynomials.
   Its length parameter is R≤C₃ A Q⁴. Substituting this into its
   fixed exponents gives size C₆ A^{168}Q^{672} and time
   C₇ A^t Q^{4t}, t=12 max(30,2d₀+2)≥360. Since t≥168 and 4t≥672,
   one common choice c=3t log₂9, a=4t and an enlarged absolute C
   absorbs both bounds and all preliminary records for every κ≤k.
   The factors 9^{3t} independent of k go into C. No exponent of Q
   depends on k, and neither M nor original Q is recomputed.

The audit finds no substantive defect and requires no proof repair,
changed hypothesis or changed direct mathematical input. It validates
this existing conditional supplier locally; it establishes no new
general structural theorem or progress beyond the cited sources by
an originality claim. No implementation, finite execution or formal
verification was performed. L071/L096 have different promises;
L102/L103 and Attempt 035 remain stops for their specified renaming
procedures. Small decompositions for arbitrary sources, general short
proofs, M-only bounds, universal W₂, arbitrary ER data and unrestricted
SAT decision/separation remain unresolved.

## Mathlib

Full matching coverage of this incidence-to-source-proof-to-exact-fg
supplier, the directional-resolution export and its binary/time ledger:
**not checked**. No absence or formal-verification claim is made.
Precise sources and restricted roles are stated in §1; the local
reception and accounting are proved explicitly rather than inferred
from a SAT decision bound or a proof-width statement alone.
