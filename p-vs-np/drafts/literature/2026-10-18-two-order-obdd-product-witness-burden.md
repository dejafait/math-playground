# Two-order OBDD product witnesses — source comparison

TARGET: Test whether a universal polynomial Boolean/commutator witness bound for Boolean-zero products of two differently ordered OBDDs implies NP=coNP.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched two-OBDD intersection/consistency with distinct orders, exact Boolean/commutator and noncommutative-IPS witness terminology, and followed the Meinel–Theobald Lemma 8.14 reference trail; compared L026/L041/L042, Attempt 030 and history/335. Actual queries and primary reading scope are recorded below.
SOURCE_EVIDENCE: Read Meinel–Theobald's English book content, Theorem 4.32 proof and Lemma 4.35 on displayed pp.72–74, Definitions 4.28 and 6.1–6.2 on pp.69,89–90; Darwiche–Marquis JAIR 17 (2002), Appendix A pp.253,260–261; Itsykson et al. STACS 2017 §1.1 p.43:3; Raz–Shpilka Definition 1 p.4 and Theorem 4/proof p.9; reused the audited L041 affine receiving model. Access and source-wording qualifications appear below.
COMPARISON: Known two-diagram consistency hardness and the inspected occurrence-splitting construction address the decision input; L041 supplies formal-identity checking for explicit affine graphs. No inspected source states the exact free-F₂ two-order witness-bound implication with complete binary accounting. Neither general W nor L042's universal faithful-collection premise follows from the restricted premise by citation alone.
GAP: Apply the known occurrence-splitting mechanism from ordinary 3-SAT without importing the book's mismatched bounded-occurrence statement; justify dense supplied distinct orders, exact ordered representatives/product, witness-excluding full input length and promise-free verifier reception. These are next-turn applicability/encoding obligations, not results established here.
REASON: Essential mechanism and verifier coverage suffice for one bounded specialization of the unchanged target. No new hardness mechanism or PIT reproof is needed; the conditional implication and its full-bit specialization remain unproved pending mathematics and later audit.
SCOPE: Two explicit deterministic OBDDs over the same occurring original variables, each in its own supplied permutation, dense levels with Boolean terminals; their standard ordered free-F₂ representatives f and g; all-assignment zero of the ordered product fg; Boolean and pair-commutator placeholders only, and one fixed polynomial in complete supplied input length for an affine-ABP H with H(x,0)=0 and H(x,A)=fg.

The original proposal below is retained as historical scope and stop
criteria. Its initial literature-only gate is superseded by the completed
comparison below. This review approves coverage for a future mathematical
attempt; it establishes neither the proposed implication nor a witness bound.

The main gap remains unrestricted SAT decision/separation. A useful
intermediate outcome would diagnose whether allowing separate orders
already places a strong conditional burden on the missing formal-witness
premise. This could guide a representation supplier that tries to relax
L085's common-order condition. It need not settle graph availability,
arbitrary ER data, proof/certificate selection or SAT itself.

Essential proposed inputs are L026 for the exact ordered diagram
representatives, L041 for the formal-identity verifier and conditional
NP=coNP mechanism, L042 for comparison with an existing defect premise,
and L085/L086 for the scope being left behind. Read only the needed
canonical cases next turn. Whether the restricted challenge class
supports the required reduction remains unresolved; neither an
intersection-hardness theorem nor its receiving encoding is assumed.
Do not use the contradictory host's clauses as a fidelity restriction.

The review should search the exact two-OBDD intersection/satisfiability
problem with distinct orders, its strongest known restrictions and
obstructions, and compare primary hypotheses with this product target.
Possible search terms are `intersection two OBDDs different variable
orders satisfiability complexity` and `conjunction OBDD distinct orders
NP complete`. These are proposed queries, not recorded search results.
Check whether a cited construction has exactly two diagrams, not an
unbounded conjunction, and whether each diagram and its order can be
written in polynomial full bits. A primary statement and essential
reduction cases are required before approving a mathematical attempt.

Continue only if there is adequate source coverage for this exact
restricted burden test, or a sharply scoped alternative test supported
by the comparison. Abandon this proposed NP=coNP transfer if the
purported hardness input requires more diagrams, stronger labels or
unpaid representations and no covered replacement is available.
An easy restricted case is informative only with its exact restrictions;
NP=coNP is not assumed false. No finding here would by itself settle
P versus NP. Mathlib coverage is not checked.

## Completed literature-only comparison — step 336, 2026-10-18

**Gap and relevance.** The main gap is unrestricted SAT decision or
separation. The intermediate target is the exact conditional implication
in TARGET, for existential alternative witnesses with one fixed polynomial
in the complete supplied pair encoding. It could diagnose the witness
cost of relaxing the common-order supplier. It would not supply witnesses,
faithful values for arbitrary ER, other certificates or a SAT algorithm.
No implication is proved in this source-review step.

**Search record.** Queries actually used included `two OBDD different
variable orders intersection satisfiability NP complete`, `OBDD conjunction
two different orders NP complete Meinel Theobald`, `Meinel Theobald "Lemma
8.14"`, `"OBDD" "8.14" "Proof"`, `"COMMON-PATH" "OBDD" NP`, `Gergov
Meinel 1994 complexity analysis manipulation Boolean functions decision
diagrams pdf`, `"OBDD" "noncommutative" "IPS"`, `"OBDD" "Boolean"
"commutator" witness`, and `"two OBDDs" "proof" certificates polynomial`.
Follow-ups sought the English book and accessible primary copies. No
inspected full-statement match for the algebraic conditional was found;
this is not a novelty claim. The newer structured-circuit proof-system
and OBDD compilation search hits were not inspected and supply no premise.

**Primary Boolean mechanism and qualification.** Christoph Meinel and
Thorsten Theobald, *Algorithms and Data Structures in VLSI Design: OBDD —
Foundations and Applications* (Springer, 1998), English book content in a
[readable scan/text mirror](https://www.slideshare.net/slideshow/algorithms-and-data-structures-in-vlsi-design-259675197/259675197):
read Theorem 4.32's two proof cases and Lemma 4.35, displayed pp.72–74,
plus Definitions 4.28 and 6.1–6.2, pp.69,89–90. These page labels refer
to that copy, not the differently paginated HPI text. The construction
replaces query occurrences by fresh variables; its two oblivious read-once
programs test the clauses and consistency of copies. Lemma 4.35 defines
simultaneous acceptance of exactly two programs. It is not an unbounded
intersection theorem.

There is a source-wording mismatch: Problem 4.29 says exactly three
literals per clause, while Lemma 4.30's transformation adds two-literal
clauses. Do not import that bounded-occurrence formulation. The permitted
specialization uses ordinary Cook–Levin 3-SAT and the inspected
occurrence-splitting mechanism; verifying this applicability without the
disputed intermediate premise is an explicit next-turn obligation.

The [author's book page](https://hpi.de/meinel/publikationen/buecher/obdds-im-vlsi-design.html)
links the [279-page English manuscript](https://hpi.de/oldsite/fileadmin/user_upload/fachgebiete/meinel/books/OBDD-Book.pdf).
Its extracted text is garbled; screenshot calls returned no inspectable
images, and shell download failed at DNS. The mirror exposes only the
earlier relevant chapters. Thus Lemma 8.14 itself was **not read**.
The [publisher's chapter 8 page](https://link.springer.com/chapter/10.1007/978-3-642-58940-9_8)
has final pagination 123–144 and a subscription preview, not the theorem.
Do not equate those page numbers with the manuscript or infer its exact
wording. Gergov–Meinel, IPL 50(6), 317–322 (1994),
DOI 10.1016/0020-0190(94)00048-4, was followed as a reference but its
primary theorem text was inaccessible; it is an unread lead, not an input.
These access failures do not block the scoped test: the readable book
proof supplies the actual mechanism, with the stated applicability check.

**Exact problem corroboration and proof-system contrast.** Adnan Darwiche
and Pierre Marquis, [*A Knowledge Compilation Map*, JAIR 17 (2002)
229–264](https://www.cril.univ-artois.fr/~marquis/darwiche-marquis-jair02.pdf),
Appendix A, printed pp.253,260–261 (PDF pages 25,32–33), explicitly uses
NP-completeness of consistency of two differently ordered OBDDs, citing
Meinel–Theobald Lemma 8.14. Read those consistency, bounded-conjunction
and bounded-disjunction cases. This is a cross-check of the problem
statement; it does not replace the inspected reduction or give an
algebraic certificate theorem.

Dmitry Itsykson, Alexander Knop, Andrey Romaschenko and Dmitry Sokolov,
[*On OBDD-Based Algorithms and Proof Systems That Dynamically Change
Order of Variables*, STACS 2017, article 43](https://drops.dagstuhl.de/opus/volltexte/2017/6991/pdf/LIPIcs-STACS-2017-43.pdf),
§1.1, p.43:3, restricts conjunction inference to a common order even
though reordering is allowed. Its coNP-completeness warning concerns
verification of differently ordered conjunction inference. It does not
provide small alternative Boolean/commutator affine-ABP witnesses. No
lower-bound theorem from that paper is needed or imported here.

**Formal verifier coverage.** Reused
`drafts/literature/2026-10-08-boolean-zero-abp-conditional-obstruction-audit.md`
and read L041's complete canonical proof, including the repaired final
layer, pruning, no-path and degree-zero cases. Reopened Ran Raz and Amir
Shpilka, [*Deterministic Polynomial Identity Testing in Non Commutative
Models*](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
16-page author manuscript, Definition 1 p.4 and Theorem 4 with its proof
p.9: homogeneous linear-edge adjacent-layer ABPs, singleton first/final
layers and unique terminals; deterministic O(s⁵+s n⁴) field operations.
The theorem has no common-variable-order premise. L041, rather than that
source definition alone, covers affine inputs by finite constant closure
and paid homogeneous normalization. F₂ has constant-cost operations.
No new normalization or PIT proof is attempted.

Read L026's ordered suffix representative and semantic bridge and L042's
exact universal-collection hypotheses/host distinction. L026's circuit
output is not silently received as an ABP; the next step must explicitly
encode each diagram's own path representative as an affine graph and
retain the specified multiplication order. L041's printed verifier takes
F and recomputes its clause-product graph. Reusing its graph zero-testing
component for a supplied two-diagram product requires an explicit
specialization; it is not a literal invocation of that F-specific verifier.
Neither Boolean-zero promise testing nor general free-ring injectivity is
available. Original-clause placeholders remain forbidden.

**Approved bounded application and test.** On the unchanged target, the
next attempt may import the named completeness/PIT results and the
inspected occurrence-splitting construction, then establish only the
needed reception and accounting. Required checks are exactly two explicit
deterministic diagrams; supplied permutations and dense Boolean-terminal
completion; strict order distinction including small/degenerate cases;
the exact L026 ordered representatives and ordered product; and complete
graph/name/Boolean/commutator dictionaries measured before H exists.
All padding must have paid size and preserve the required polynomials,
not merely a convenient Boolean-equivalent output. Prove verifier
soundness on arbitrary candidate H without testing the semantic promise,
and completeness only under the one fixed existential polynomial bound.
No efficient witness finder, degree promise, class equality or fidelity
restriction from contradictory host clauses may be assumed.

Continue only if these conditions give one polynomial reduction and one
polynomial-bit verifier. Abandon or narrow the proposed transfer on any
essential unbounded conjunction, hidden occurrence-consistency cost,
exponential completion, unreceived graph model or lost formal identity.
Do not reprove an imported hardness theorem as new mathematics; explain
the specific ordinary-3-SAT/source-wording and full-bit specializations.
The conditional implication, universal witness bound, general ER data,
alternative-certificate hardness and unrestricted SAT remain unresolved.

**Local overlap and record.** The narrowly searched 2026-10-18 assessments,
Attempt 030 and history/335 contain the common-order stop and this proposed
target, not a completed two-order burden result. L041 is stronger in its
witness hypothesis; L042 concerns every supplied faithful collection.
Neither establishes the restricted premise's sufficiency without the
reduction above. L085/L086 and Attempt 030 remain intact. No lemma,
mathematical script, PROOF or DAG changed. Mathlib coverage for the full
conditional, two-order hardness and supporting results is **not checked**;
unknown availability is not an absence claim.

The [current Clay page](https://www.claymath.org/millennium/p-vs-np/)
and its linked [Cook description](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf),
§1 pp.1–2, were reconfirmed on 2026-10-18: the exact target remains
ordinary deterministic versus nondeterministic polynomial-time languages,
and is still listed as unsolved. This review changes no main argument.
