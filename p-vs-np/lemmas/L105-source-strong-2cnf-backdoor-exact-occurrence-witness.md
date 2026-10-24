# L105 — Supplied strong 2-CNF backdoor gives an exact occurrence witness

## Hypotheses

Supply an explicitly written unsatisfiable width-at-most-three source
CNF F, exactly its L087 occurrence pair D,E with its actual provenance,
orders, occurrence names and complete dictionaries, and a list S of k
**distinct occurring source variables**. Repeated literals/clauses,
tautologies, units and empty clauses are permitted in the source lists.
The alphabet of the desired witness is precisely L087's occurrence
alphabet y, including its four appended u/v occurrences.

The backdoor promise has the following exact convention. Form an
auxiliary literal-set view F₀: remove repeated equal literals in a
clause, discard tautological clauses, and optionally identify identical
clauses with their earliest actual source position. For every total
assignment α to S, discard satisfied clauses of F₀ and remove false
assigned literals from the others. The resulting F₀↾α has width at most
two. No unit propagation or other inference is part of this restriction.
This is the ordinary strong syntactic 2-CNF backdoor convention on
nontautological clause sets. A stronger raw-list promise also suffices.
The normalization changes neither the original supplied F nor its pair.

Retain exactly f=r_D, g=r_E, B and the pre-witness M of L087. Fix

    Q = 2 + M + |F| + |backdoor|,

where the last term includes every supplied backdoor name, annotation
and framing bit. All source/provenance records are charged before any
proof or witness is generated. No proof/witness size or degree enters Q.
Use the audited L097 receiver, including its step-380 constant repair.
No extension axioms, strong-backdoor finder or short-proof oracle are
assumed.

## Conclusion

There is a deterministic construction of an explicit acyclic affine-F₂
ABP H, using only y and B's Boolean/commutator placeholders, such that
formally in the free associative algebra

    H(y,0) = 0,                 H(y,B(y)) = fg.

Absolute constants C,c,a give the common bound C 2^{c k} Q^a for full
binary output size and deterministic bit time. This includes every
independent receiver block, full dictionaries, the original retained
input and the ordinary-resolution archive with actual source-leaf
associations; unused supplied records are retained. In particular a
supplied k=O(log Q) promise gives a polynomial original-Q bound, with
the constant in that promise fixed.

This is a specialization/reproduction of known branch, lifting and
combination machinery through L097, without certified originality. The
separate step-413 all-size informal critical audit below finds no
substantive defect in its reception or common size/time ledger. No
implementation or finite certificate check is claimed. Small backdoors
for arbitrary sources, general short proofs, M-only bounds, universal
W₂, arbitrary ER data and unrestricted SAT decision/separation remain
unproved. This is not a main-problem solution candidate.

## Proof

**1. Coverage and the restricted use of known results.** The assessment
saved before this invocation is
`drafts/literature/2026-10-22-source-2cnf-backdoor-specialization.md`;
its completed primary comparison is
`drafts/literature/2026-10-22-source-2cnf-backdoor-occurrence-witness.md`.
No new literature approval is made here. The exact imports are:

- Nishimura–Ragde–Szeider, *Detecting Backdoor Sets with Respect to Horn
  and Binary Clauses*, SAT 2004 proceedings pp.96–103, [proceedings
  copy](https://www.satisfiability.org/SAT04/programme/51.pdf), §2 p.98,
  Theorems 3–4/Lemma 2 pp.100–101: ordinary clause-set restriction and
  strong binary backdoors. Their finder is unnecessary here.
- Buresh-Oppenheim–Mitchell, *Minimum 2CNF Resolution Refutations in
  Polynomial Time*, SAT 2007, LNCS 4501, pp.300–313, [14-page author
  copy](https://www.cs.sfu.ca/~mitchell/papers/sat07-2res.pdf), §2 PDF
  pp.2–3, Proposition 1 and IR(P): contradictory directed paths with
  actual clause labels yield input-resolution derivations. The
  optimization theorem and its proof are not imported.
- Lauria–Nordström, *Tight Size-Degree Bounds for Sums-of-Squares
  Proofs*, [April 7, 2015 full version](https://www.massimolauria.net/documents/sizesos.pdf),
  §2 pp.6–7, Fact 2.5 and its resolution convention: restriction lifting
  in ordinary resolution with weakening.
- Järvisalo–Matsliah–Nordström–Živný, *Relating Proof Complexity Measures
  and Practical Hardness of SAT*, CP 2012, LNCS 7514, pp.316–331,
  [17-page author copy](https://people.csail.mit.edu/jakobn/research/RelatingProofCplxHardnessSAT.pdf),
  §6 Theorem 2(1), proof pp.13–14: combine lifted backdoor branches
  using the total-assignment blocking clauses. Its space estimate is
  not used as a binary-size or construction-time estimate.

The author-copy revision dates of the second and fourth sources are
not established. Numbering is that of the inspected copies. The
second source's §2 path/label and unit cases were also narrowly checked
during this application; this is not another discovery review.

The general operations are imported. Sections 2–5 specify only the
actual list/set reception, leaf labels, written records and bit ledger
needed to apply them to this supplied source. L104 and L096 are
comparisons, not mathematical inputs. Attempts 030–035 concern other
universal promises or renaming implementations; none is invoked.

**2. Keep the actual source and occurrence data.** Parse S, check that
its names are distinct and occur in F, and keep their supplied order
s₁,…,s_k. Parse all source and pair data, and check L087 provenance by
its specified reconstruction with the actual naming map, as permitted
by L097. This is polynomial in Q. The semantic UNSAT hypothesis is
not an algorithmic test used below. Every branch of an unsatisfiable F
is unsatisfiable: a satisfying residual assignment, combined with α,
would satisfy F. Auxiliary normalization preserves this statement.

Store a table from every normalized clause to its chosen actual source
position and raw signed literal positions. Keep all removed equal
literals, duplicate-clause associations and discarded tautology records
in this table or the unchanged input. Ordinary resolution uses clauses
as finite literal sets. A leaf for a normalized clause is therefore
its actual original clause in set interpretation, with that raw list
and source position attached. It is not a new strengthened axiom. L097
§3 pays ordered-list permutation, rebracketing and idempotence at its
propositional receiving stage. This is an interface already admitted
by that receiver; it requires no new normalization theorem or rule.

An original empty clause can be received directly by L097: D has the
absorbing failure root and f=0 formally. Return a zero graph with
distinct endpoints, retaining all dictionaries/input. Its size and time
are polynomial in Q. Below assume no original empty clause.

For each α, form F₀↾α by the convention above, retaining an actual
original position for every residual axiom. Different source clauses
can have equal residuals; keep their separate labelled records, or
choose the earliest and retain the other associations. Check width at
most two on each branch before using the subsolver. Failure rejects
the promised-input reception, rather than claiming a witness. The
promise guarantees no such failure. No characterization of strong
backdoors on raw tautological lists is assumed.

**3. Export labelled branch proofs.** If a branch contains an empty
residual clause, take that single labelled axiom as its refutation.
Otherwise use the imported implication-graph criterion/construction on
its nonempty clauses. Represent a unit l by the single-literal clause
l, giving the edge ¬l→l (the source permits equal literals in a binary
clause). For each binary clause l∨t use ¬l→t and ¬t→l, retaining
its source label. Parallel labels may be kept. Tautologies were removed
only from the auxiliary source view.

Let n be the number of distinct variables of F outside S. When n>0,
finite graph searches find a variable x and paths x→¬x and ¬x→x.
Choose shortest paths by fixed literal/edge order; each is simple and
has at most 2n−1 edges. There is no search for a shortest refutation.
For clarity, the application of IR(P) at these particular endpoints
can be exported as follows. Write a path a=l₀,l₁,…,l_t=¬a. Its edge
labels are the actual residual clauses ¬l_(i−1)∨l_i. Start with its
first labelled axiom, then append successive binary resolutions on
l₁,…,l_(t−1), stopping if the required unit ¬a has already been derived.
Simplicity ensures that no internal vertex is a or ¬a. Before stopping,
the current clause is ¬a∨l_i. At the next edge, if l_(i+1)≠¬l_i,
resolution gives ¬a∨l_(i+1), with equal literals interpreted as a set;
the endpoint gives the unit ¬a. If l_(i+1)=¬l_i, the edge label is the
unit ¬l_i, so resolution already gives ¬a and the path derivation
stops early. All unused edge labels remain available as residual axiom
records. A length-one path already has its endpoint unit axiom. This
specifies the unit-edge reception of the cited contradictory-path
construction, with actual axiom occurrences and backward references.

The two paths thus give opposite units; resolve them to the empty
clause. Each path uses at most t axiom occurrences and at most t−1 derived
records. Reuse is allowed but not required. There are at most 8n+1
records after enlarging the harmless constant, all of width at most
two. One may retain all unused residual clauses as additional axiom
records, giving at most C₀(n+m+1), where m is the original clause
count. Every axiom has its actual original source association.

If n=0, there are no nonempty nontautological residual clauses.
Unsatisfiability therefore forces an empty residual clause, already
handled. If a branch closes early, its one-axiom proof is simply used
for that full α; there is no need to introduce assumptions or prune
other supplied records. Units, repeated literals and repeated clauses
are covered by the set interpretation and labelled axiom reception.

**4. Export lifted ordinary source records and combine.** For a prefix
assignment γ on s₁,…,s_r let T_γ be the clause of its falsified literals:
s_i occurs positively if γ(s_i)=0 and negatively if γ(s_i)=1. In
particular T_α has width k, and T_∅ is the empty clause. We use the
cited restriction-lifting fact and published blocking-clause assembly;
the following describes their records under the actual source convention.

First write all original clauses of F as source axioms of the final
ordinary-resolution archive π, even if unused. Store their positions
and raw lists. For every residual-axiom occurrence A in branch α, let
j be its attached original position, and C_j its literal set. The
clause was not satisfied by α. Its assigned literals are false and
hence belong to T_α, while its remaining literals are precisely A.
Consequently

    C_j ⊆ T_α ∪ A.

Append a weakening from the actual earlier source axiom j to T_α∨A,
or reuse that row if the clauses already agree. Thus the branch leaf
is not used as an unlifted original axiom. An empty residual clause
works identically and gives T_α directly.

Replace every branch resolution record A,B→R on pivot p by the
resolution of T_α∨A and T_α∨B on the same p, yielding T_α∨R.
All branch pivots lie outside S, so neither sign of p is in T_α;
taking the union and deleting pivot signs gives exactly that clause.
All references point to the already exported rows. The final row for
this branch is T_α. This retains the source association required by
L097 while instantiating ordinary restriction lifting. No extension
axiom or free assignment assumption enters π.

Write all 2^k lifted branches consecutively with relocated backward
references. Combine their last rows in the complete assignment tree:
for every prefix γ of length r<k, the already available child clauses
are T_γ∨s_(r+1) and T_γ∨¬s_(r+1), in the appropriate child order.
Resolve them on s_(r+1) to T_γ. Bottom-up processing writes 2^k−1
resolution rows and finishes with T_∅. For k=0 there is one branch,
T_α is empty, and no combination row is required. Every line is now
an actual original axiom, a weakening of an earlier row or an ordinary
binary resolvent. In particular π is precisely an admitted L097
refutation of the unchanged F, not a refutation of a restricted or
rebuilt source. All its leaf variables are source variables.

Restricted branch worksheets and the normalization/association table
may also be retained as separate auxiliary archive records. They are
not passed as extra source axioms or inference rows to L097. All
unused supplied records, original occurrence names, D,E, orders, B,
placeholder dictionaries and M remain present and unchanged.

**5. One original-Q full-bit and deterministic-time ledger.** Fix an
ordinary self-delimiting explicit binary record encoding. A fixed
constant absorbs its framing. Counts of clauses, literal occurrences,
variables, annotations and maximum written source-name length are
at most C₁Q; k≤C₁Q as well. The bounds below can enlarge C₁ for any
fixed receiving encoding. Enumerating a written k-element set does
not use a binary numerical k as an uncharged list length.

For each assignment, rebuilding the residuals/associations, graph
searches and writing the two path proofs take polynomially many
operations in Q. For example scanning name lists, constructing all
edges and repeated breadth-first searches from the at most 2n literal
vertices fit C₂Q⁶ bit operations using naive explicit comparisons and
arrays. Each branch proof and its lift have O(Q) rows; even retaining
all residual axioms and raw-list associations gives O(Q²) local
fields. Source axioms contribute O(Q) rows and the combination tree
O(2^k) rows. Thus the full archive has at most C₃2^kQ² fields/records
under this deliberately loose convention.

Every clause has at most max(3,k+2) literals: branch clauses have
width at most two, lifted clauses at most k+2, and source axioms at
most three. Restoring full source names costs at most C₄Q² bits per
clause/association record, including a raw width-three source list.
References and new dense row identifiers have bit length

    O(log(2^k Q²+2)) = O(k+log(Q+2)) = O(Q).

The same bound covers branch tags, positions and length fields.
Recording each row explicitly, independently copying all branch
worksheets and retaining the original input therefore gives the safe
common archive/output estimate

    X = K₀ 2^k Q⁸,           |π| + |auxiliary archive| + Q ≤ X.   (1)

The larger exponent leaves room for every normalization table,
original/provenance dictionary and original leaf association. It is
not an estimate merely of distinct stored clauses. Parsing/input
checks and local construction take O(2^kQ⁶) plus output writing.
Even allowing a quadratic scan/copy/renumber of the whole X-bit archive
bounds its deterministic construction and verification by K₁X².
No global search through an exponential universe of clauses is used.
No polynomial exponent here depends on k. The algorithm can verify
all width and resolution conditions within this bound; it does not
test semantic UNSAT separately.

L097 receives

    Q_res = 2 + M + |F| + |π| ≤ K₂ 2^k Q⁸.                      (2)

Its audited bounds (11)–(12) give output length O(Q_res^168) and time
O(Q_res^[12 max(30,2d+2)]), for a fixed d≥6 from its deterministic
L035/L036 bit algorithms. Set once and for all

    b = max(168, 12 max(30,2d+2)),       c=b,       a=8b.

In particular b≥2. Apply that receiver once, retaining all of its
independent graph blocks and complete repeated dictionaries. Equations
(1)–(2), the archive's quadratic construction cost and the receiver's
bounds imply, after enlarging a fixed C,

    full retained output length ≤ C 2^{c k} Q^a,
    total deterministic bit time ≤ C 2^{c k} Q^a.                (3)

The output includes H and the retained input/source/archive, not just
the final graph's vertex count. The constants depend only on fixed
encodings and the already fixed local algorithms. There is no
recomputation of Q after proof generation, or replacement of k by a
cutoff computed on that expanded proof.

**6. Exact receiver endpoint and limitations.** The source F and the
L087 provenance supplied to L097 are unchanged throughout. Its output
therefore satisfies H(y,0)=0 and H(y,B(y))=fg for the original ordered
representatives, not for a restricted pair, an ordinary consistency
formula in place of g or a merely Boolean-equivalent product. Only
the prescribed Boolean/commutator placeholders and occurrence names
survive. The two identities are L097's formal conclusions; Boolean
vanishing alone is never used to identify a different-order product.

This passes the stated construction threshold at the informal all-size
level; the separate critical review is recorded below.
It imports published general mechanisms and supplies their local
reception/accounting; it is not progress beyond those sources in a
certified originality sense. Finding small backdoors for arbitrary
sources, supplying general short refutations, a bound in M alone,
universal W₂, arbitrary ER data and unrestricted SAT transfer remain
independent gaps. No comparison asserting domination of L104's supplied
incidence-width promise is made.

**Independent critical audit — 2026-10-23, step 413.** The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-22-source-2cnf-backdoor-critical-audit.md`.
This audit reuses its completed primary-source comparison and the
precise imports in §1. It checks the full construction against L087's
actual occurrence interface and the audited L097 receiver, including
the step-380 constant repair. No stronger source theorem, new supplier,
implementation or finite certificate is asserted. Attempts 030–035
concern different universal promises or renaming implementations; this
construction invokes none of them.

- **Source syntax and the promise.** Width at most three is the original
  L087 source-list convention, so repeated literal occurrences are still
  counted in the input. Deduplicating literals and discarding tautologies
  is confined to F₀. A normalized surviving clause is associated with
  an actual raw source clause, including every repeated signed position;
  its set interpretation is the same clause, not a derived stronger
  axiom. Dropping duplicate clauses retains an original representative
  and leaves the whole original input in the archive. Thus normalization
  preserves satisfiability while the original split tester, including
  distinct names for repeated occurrences and discarded tautologies,
  remains unchanged. Every assignment to S has an unsatisfiable residual
  of width at most two by the stated hypotheses, not by a propagation
  or semantic-width inference.
- **Labelled contradictory paths.** With no empty residual clause, the
  imported implication-graph criterion applies to this unsatisfiable
  2-CNF, units included. For a simple path a=l₀,…,l_t=¬a, its first
  edge is exactly the labelled clause {¬a,l₁}. If t=1 it is already
  {¬a}. Otherwise simplicity excludes a and ¬a internally, so the
  maintained clause {¬a,l_i} is a genuine two-literal clause before an
  early stop. Resolve it with the actual next edge clause
  {¬l_i,l_(i+1)}. When l_(i+1) differs from ¬l_i, deletion of the pivot
  signs leaves {¬a,l_(i+1)}; if the next vertex is the endpoint, this
  is the unit {¬a}. When l_(i+1)=¬l_i, the next clause is the unit
  {¬l_i} and the resolvent is already {¬a}. Both literal signs of the
  pivot are handled by the same ordinary variable-resolution rule with
  parents interchanged if necessary. No tautological-clause inference
  or assumption about the remaining unused suffix is needed. Applying
  this to both directions gives opposite units and then the empty
  clause. At most 2n−1 edges per path give at most 8n+1 records; adding
  all unused residual axioms preserves the O(n+m+1) count.
- **Actual leaves and lifted inferences.** A residual axiom A comes from
  a source C_j not satisfied by α. Every removed literal of C_j is
  false under α, hence belongs to T_α; every other literal lies in A.
  This proves the required C_j⊆T_α∪A without silently replacing F by
  F₀ or F₀↾α. Its row is a weakening of the actual original axiom.
  Set/list reconciliation is precisely admitted by L097 §3. No lifted
  pivot variable is in S, so deleting its opposite signs from the two
  lifted parents leaves exactly T_α united with the branch resolvent.
  All inference parents are earlier rows. Resolving each pair of child
  blocking clauses removes its one assigned variable and gives the
  exact prefix clause, ending at the empty prefix. The branch worksheets
  are auxiliary data, never additional axioms of π.
- **Boundary cases and retained data.** An original empty clause starts
  D in its absorbing failure state. Backward suffix induction makes its
  representative formally zero, even with unreachable live states and
  all four gadget occurrences retained; the distinct-endpoint zero graph
  has both required identities. If an ordinary proof archive is desired
  in this shortcut, retain the original axioms and designate that actual
  empty axiom as the final row (copy its axiom record last if necessary).
  A branch empty clause instead weakens its associated original clause
  directly to the full T_α. With no variables outside S, an unsatisfiable
  residual must contain the empty clause; an empty residual conjunction
  would be satisfiable and is excluded by the hypothesis. For k=0 there
  is one branch and no combination inference. Early closure does not
  shorten T_α or discard the other full assignments. Units, repeated
  literals/clauses and source tautologies are covered by the preceding
  cases. An empty source conjunction cannot satisfy the UNSAT hypothesis.
- **One complete size/time bound.** Put X=K₀2^kQ⁸ as in (1). The actual
  O(2^kQ) proof rows, at most O(Q) literals per lifted row, O(Q)-bit
  names, retained raw-source associations and O(k+log(Q+2))-bit global
  references all fit X, including independently retained worksheets and
  input dictionaries. The looser field count in §5 also fits X. Fixed
  ordered searches in each O(Q)-vertex/edge graph require polynomial
  bit time; the stated Q⁶ local allowance and output writing are below
  a fixed multiple of X². A quadratic scan verifies each explicit
  weakening/resolution and reference without searching for a proof.
  L097 receives only the charged source/refutation input, with
  Q_res≤K₂2^kQ⁸; its exponent does not depend on the generated proof.
  Writing e=12 max(30,2d+2) and b=max(168,e), its two costs are bounded
  by fixed multiples of (2^kQ⁸)^168 and (2^kQ⁸)^e. Since k≥0, Q≥2
  and b≥2, the archive cost (2^kQ⁸)² and retained output are absorbed
  by the same C2^{bk}Q^{8b}. Constants such as K₂^b are fixed once and
  for all. No logarithmic factor, name restoration, unused supplied
  record or independently copied receiver dictionary is omitted, and
  no exponent or cutoff is chosen after observing the output.
- **Formal endpoint.** The exported π is an ordinary-resolution
  refutation of the original F with weakening and no extension axioms.
  Those are the repaired L097 receiving hypotheses, and its actual
  occurrence data are unchanged. Its conclusion is therefore exactly
  H(y,0)=0 and H(y,B(y))=fg. There is no substitution of a simplified
  occurrence product or Boolean-equivalent consistency polynomial.

The all-size informal audit finds no substantive defect or need to
change the theorem, its direct mathematical inputs or its bound. This
validates a conditional local input as a reproduction of known
machinery; it is not a new theorem beyond the sources, formal verification
or progress on general backdoor availability. The independent gaps
listed above remain unresolved.

## Mathlib

Full matching coverage of this supplied-backdoor/exact-occurrence
transfer, the constructive resolution archive, affine-ABP identities
and common binary size/time ledger: **not checked**. Supporting named
primary inputs and their precise roles are given above; no absence or
machine-verification claim is made. The new source-leaf reception and
ledger are written out because a clause-count, space or SAT-decision
bound does not alone specify this exact full-bit interface.
