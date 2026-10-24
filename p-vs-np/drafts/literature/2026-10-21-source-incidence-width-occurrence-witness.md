# Source incidence width: completed witness-supplier source comparison

TARGET: Assess whether a supplied width-k incidence-tree decomposition of an unsatisfiable width-three source CNF yields L087's exact-fg witness in size and time 2^{O(k)}Q^{O(1)}, where Q=2+M+|F|+|decomposition| is fixed before construction.
CHECKED: 2026-10-22
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 405 searched incidence/primal treewidth, constructive resolution and directional Davis–Putnam bounds; checked the specific local L087/L097 receiver, L071/L096 promise comparisons and Attempt 035; inspected the primary sources and proof ranges below.
SOURCE_EVIDENCE: Kolaitis–Vardi author full version p.25 incidence conversion; Bodlaender–Jansen–Kratsch arXiv:1104.4217v2 Proposition 7 p.23 with proof; Rish–Dechter 58-page author manuscript Figure 4/Theorem 1 pp.7–8, Theorem 4/Lemmas 1–2 p.12 and Appendix A pp.54–55. Precise versions, bounds and qualifications follow. Direct primary URLs: https://www.cs.rice.edu/~vardi/papers/pods98rj.pdf ; https://arxiv.org/pdf/1104.4217v2 ; https://ics.uci.edu/~dechter/publications/R80.pdf (rechecked step 406).
COMPARISON: Known constructive components cover the source structural route; L097 already receives ordinary resolution with a full polynomial ledger and preserves exact fg. No inspected theorem states the complete occurrence-witness specialization. L071/L096 and the stopped full-map procedure have different promises.
GAP: A separate research turn must justify the original-clause reception, construct and retain ordinary resolution records, and compose all binary size/time bounds in original Q. No supplier theorem or new graph-conversion lemma is proved in this literature turn.
REASON: Essential source coverage is now sufficient for a known-mechanism specialization; import the structural results and prove only the exact-source/full-record/L097 applicability interface in a later turn.

## Preserved proposal scope from step 404

The next turn is a source comparison, not permission to derive a new
supplier. Input is an explicitly written unsatisfiable width-at-most-three
CNF F with its actual clause/literal trees; exactly L087's occurrence pair,
provenance and full B/M package; and a fully written tree decomposition
of the bipartite variable–clause incidence graph. Every bag, tree edge,
name, source occurrence and reference must be charged. Clarify the
incidence convention for repeated literals, tautological clauses, empty
clauses and unused names before applying a theorem. The supplied width
is k, and Q is fixed before any proof or witness is constructed.

The comparison should first inspect the strongest applicable primary
theorem statement and the proof cases that actually produce refutation
records. A SAT decision algorithm or existence of a small dynamic-program
table is not by itself the required ordinary-resolution proof. If an
input graph conversion or stronger proof system is needed, read its
exact hypotheses and quantitative cost before proposing a specialization.
Then check reception by L097, which permits ordinary resolution with
weakening but not extension axioms. The candidate target requires one
bound 2^{c k} Q^d with fixed constants c,d, including construction time,
all written proof records and L097's subsequent independent copies.
No such bound is asserted here.

The exact output must retain L087's original ordered free-ring fg and
unchanged Boolean/commutator dictionary, with both formal identities.
Neither a Boolean-equivalent reordered product nor a decision of F
suffices. L097's qualified existing theorem is a possible receiver;
this proposal does not reprove it or assume that its source proof has
already been supplied. The named local inputs for the future comparison
are L087 and L097; L071 and L096 are promise comparisons only.

## Reuse, relevance and decision test

The narrow local hit in
`2026-10-17-logarithmic-input-deletion-data.md` records Simone Bova and
Friedrich Slivovsky, *On Compiling Structured CNFs to OBDDs*, published
open-access version ©2016, DOI
[10.1007/s00224-016-9715-z](https://doi.org/10.1007/s00224-016-9715-z),
§3.4 Lemma 12/Theorems 13–14, journal-PDF pp.11–13. That existing
comparison was read locally; no primary source was reopened in step 404.
It treats deletion distance to a class with a polynomial subterm bound
and conditions for a constructive order. It is a related compilation
lead, not an inspected theorem establishing this target. The next review
must check relevant proof-complexity/structural-width sources, rather
than reusing that different conclusion as approval.

The main gap remains unrestricted SAT decision/separation. A supplier
with this bound could give a further explicit promised family of
occurrence witnesses, with a logarithmic-width regime worth comparing
to the existing suppliers. This is a conditional downstream use, not
universal availability or evidence of a separation. Independent gaps
remain: small decompositions for arbitrary sources, general short-proof
availability, a bound in M alone, general ER data and unrestricted SAT.

Continue only if primary coverage supports a concrete constructive
refutation interface at the stated bound, or identifies a precise
bounded specialization needing proof. If only decision algorithms or
different proof systems are covered, record that distinction and leave
the missing interface unapproved. A documented known match should be
imported, not reproved for novelty. The existence of this proposal is
not evidence that it is new. Mathlib coverage is not checked.

## Completed comparison — step 405, 2026-10-22

LITERATURE / literature_comparison / NOVELTY_UNCHECKED, outcome
EXPLORATION. This completes essential component coverage, not the
mathematical supplier. The preceding proposal's statements about unread
sources describe step 404 and are superseded by this comparison.

LITERATURE_REASON: The gate required essential constructive resolution
and incidence-conversion coverage absent from the saved continuation;
this is not additional browsing on an already ready mathematical target.

Queries included `resolution refutation incidence treewidth constructive
size bound Atserias Dalmau`, `CNF primal incidence treewidth clause size
treewidth resolution Davis Putnam proof size`, `Rish Dechter resolution
versus search 2000 pdf directional resolution theorem induced width`,
and `tree decomposition elimination ordering construct given tree
decomposition lemma proof`. Author publication lists located the exact
manuscripts below after unsuccessful guessed endpoints. Search snippets
and failed downloads are not theorem evidence.

### Primary structural inputs actually inspected

1. Phokion G. Kolaitis and Moshe Y. Vardi,
   *Conjunctive-Query Containment and Constraint Satisfaction*, JCSS
   61(2), 302–332 (2000), DOI
   [10.1006/jcss.2000.1713](https://doi.org/10.1006/jcss.2000.1713).
   Read the [31-page author full version](https://www.cs.rice.edu/~vardi/papers/pods98rj.pdf),
   printed p.25, the unnumbered paragraph beginning the incidence-graph
   comparison. For maximum relation arity a, it gives treewidth at most
   a(k+1)−1 from incidence width k, by replacing tuple vertices in bags
   by their elements. This direction preserves the underlying elements;
   it introduces no satisfiability extension variables. Applicability
   to a clause-indexed width-three source and its supplied decomposition
   belongs to the next specialization. The paragraph's reverse-direction
   construction and its final example are not needed or imported.
   No manuscript revision date was established.

2. Hans L. Bodlaender, Bart M. P. Jansen and Stefan Kratsch,
   *Preprocessing for Treewidth: A Combinatorial Analysis through
   Kernelization*, [arXiv:1104.4217v2](https://arxiv.org/pdf/1104.4217v2),
   version label 26 September 2013; PDF title page says 3 October 2018.
   Read Proposition 7 and its proof, printed p.23. Weighted treewidth
   at most w is equivalent to an elimination ordering of closed-neighborhood
   cost at most w+1. The forward construction completes bags to cliques
   in H, then removes simplicial vertices. Use unit weights. Its sentence
   naming an ordering “of G” must be read with the explicitly constructed
   chordal H; the next application must state which graph is searched.
   No optimal-decomposition finder is required or imported.

3. Irina Rish and Rina Dechter, *Resolution versus Search: Two Strategies
   for SAT*, J. Automated Reasoning 24(1–2), 225–275 (2000).
   Read the [58-page author manuscript](https://ics.uci.edu/~dechter/publications/R80.pdf):
   interaction graph p.5; Figure 4 p.7; Theorem 1 p.8;
   Definition 1 p.11; Lemmas 1–2/Theorem 4 p.12;
   Appendix A pp.54–55. Revision date was not established; numbering
   here is this manuscript's. For induced width w, Theorem 4 states
   O(n·9^w) time and at most n·3^(w+1) stored clauses.
   Figure 4 uses unit resolution or opposite-polarity pairs at each
   bucket, routes resolvents earlier, and stops at the empty clause;
   Theorem 1 supplies completeness. Appendix A checks original/derived
   edge cases, three literal choices per parent and all bucket pairs.
   These are actual resolution operations on existing variables.
   The counting convention requires distinct, nontautological clause
   sets. Binary records and source-list normalization are not the
   manuscript's stated cost model; those are explicit reception work,
   not a new proof of directional-resolution completeness.

### Stronger lead and limits of the comparison

Also read Shaowei Cai and Ziqun Li, *Short Resolution Refutations for
CNFs with Bounded Weighted Incidence Treewidth*,
[arXiv:2610.02047v1](https://arxiv.org/html/2610.02047v1),
1 October 2026, abstract, §1.1, Theorem 1(3), Theorem 2 and §1.3.
With maximum clause width a, Theorem 1(3) states ordinary resolution
length (n+m)a^{O(tw*(F))}; the unrestricted-clause-width incidence-FPT
question remains open there. Sections 5–6's constructions were not
inspected: this lead supplies no imported constructor here. The older
inspected route suffices for the fixed a≤3 target; there is no reason
to add this stronger source's machinery to the continuation.

The selected sources do not justify a generic use of bounded-width
resolution search, whose exponent in the number of variables can depend
on width. Nor does a small SAT dynamic-program table alone produce the
required proof records. Avoid equisatisfiable transformations introducing
fresh variables: L097 accepts ordinary source resolution, not an ER
refutation of a transformed formula. These distinctions decide which
source route to use, without deriving its application in this turn.

### Exact remaining specialization and decision test

The proposed mathematical action is recorded in
[its separate ready assessment](2026-10-22-source-incidence-width-supplier-specialization.md).
Its only local mathematical inputs are L087 and audited L097; reuse
[L097's source assessment](2026-10-20-source-resolution-occurrence-product-witness.md)
and [audit coverage](2026-10-20-source-resolution-occurrence-critical-audit.md).
L097's hypotheses/conclusion and §5 full ledger were read: its polynomial
uses the supplied proof's full binary length, not its line count alone.
The actual occurrence product, original alphabet, provenance, B and both
formal identities must be retained throughout.

The pending reception must specify one incidence vertex per written
clause position and per occurring source variable, with a simple edge
for membership irrespective of sign or repetition. Empty clauses permit
L097's direct zero branch. Repeated literals/clauses, tautologies and
unused declared names require explicit source associations; normalizing
the proof's clause sets must not rebuild L087 on a changed source.
The supplied decomposition records and all source names remain charged
even when irrelevant. Validate the input decomposition; do not search for
one or recompute Q after expansion.

Continue if a complete, deterministic ordinary-resolution record export
and its L097 reception admit one 2^{c k}Q^d size/time bound with fixed
c,d in the original Q. Expose a failure if any essential inference
needs extension axioms, loses a source-clause association, changes fg/B,
or introduces an exponent d depending on k. Mere proof width or Boolean
equivalence does not pass this test. No such export or bound is proved
here, and no new lemma or mathematical script was written.

The possible downstream use is another promised exact-occurrence
supplier, including a possible logarithmic-width regime after the
bound is established. Small decompositions for arbitrary sources,
general short-proof availability, an M-only bound, arbitrary ER data
and unrestricted SAT remain independent gaps. L071's full signed
value-DAG promise and L096's small-core promise do not cover this
input. Attempt 035 stops a specific full-map normalization; choosing
a structural resolution supplier does not reopen that procedure.
No originality is inferred from this review. Mathlib coverage was not
checked; no matching formalized supplier is asserted.
