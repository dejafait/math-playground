# Logarithmic original-input deletion — source comparison

TARGET: Test whether a supplied set of at most floor(log₂(T+2)) original-variable vertices whose deletion leaves the full signed value graph of treewidth at most two suffices for polynomial-full-bit L037 data.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Targeted conditioning/backdoor/deletion and noncommutative-IPS queries below found Boolean restriction, order-sensitive closure and a CNF deletion-distance compilation theorem; scoped local searches found no completed deletion-promise construction. No novelty inference.
SOURCE_EVIDENCE: Read Bryant author-hosted annotated manuscript Definition 1 and section 4.4; Darwiche–Marquis Definitions 5.3–5.5, Shannon discussion and Proposition 5.1 proof CD/AND-closure cases; Bova–Slivovsky published DOI 10.1007/s00224-016-9715-z section 3.4 Lemma 12/Theorems 13–14 with complete proofs. Reuse L071's inspected compilation/completion coverage and L035/L036's ready witness and graph-composition assessments.
COMPARISON: Known Boolean restriction does not supply free-ring witnesses; CNF deletion distance is a different graph promise. L071 supplies the fixed-width component but requires a complete Boolean circuit. Independent branch orders cannot be merged by an unproved common-order assertion or unrestricted OBDD Apply.
GAP: Justify conditioned circuit framing and all-root compilation, then test paid ordered case recombination of the supplied branch data with both formal H identities and one polynomial aggregate bit/time bound; none of those new applicability steps is established by this review.
REASON: Essential component sources and proof cases are accessible. The remaining difference is an explicit graph-level specialization test using audited local Booleanity/commutator witnesses, rather than an essential unread theorem. Permit one bounded attempt after separate assessment approval; sufficiency and originality remain unproved.
SCOPE: Exactly TARGET under L071's signed-AND ER/original-axiom conventions, with the supplied deleted set consisting only of original-variable vertices; all signed and unused roots, original names, separate graph copies and pre-substitution degrees remain charged. Branch orders may differ; no global OBDD or L071's unchanged degree bounds are promised.

## Preserved proposal and review boundary

The paragraphs below preserve the proposed test at invocation start. Their
missing-coverage description is superseded by the completed comparison
below, without asserting its mathematical conclusion. This literature-only
step writes no lemma, mathematical script or new specialization proof.

Retain L071's width-three original CNF, valid supplied signed-AND ER proof,
T=2+|F|+|π|, shared original vertices, all signs and unused roots. The
additional supplied set consists only of original-variable vertices, not
arbitrary internal gates; graph deletion removes those vertices and their
incident edges. Charge its explicit names as additional polynomial input
framing. Do not infer that the resulting graph is already a Boolean value
circuit, that assigning the deleted inputs preserves an unstated width
bound, or that independently compiled branches have a common order.

Main gap: unrestricted SAT decision/separation. Potential downstream use:
supply L037 data on a larger explicitly promised class. The proposed
mechanism to assess is conditioning followed by paid formal recombination;
no correctness, size bound or applicability argument for that mechanism
has been established here. The literature review should compare exact and
stronger known statements, primary hypotheses and essential proof cases,
plus local duplicates and stops. L026, L035, L036, L037 and L071 are the
anticipated local inputs to compare, not asserted sufficient premises for
the new conclusion. No cross-notebook theorem is proposed.

Continue toward a mathematical test only if the review identifies adequate
coverage and a concrete way to test all-root representatives and formal H
relations with one polynomial aggregate bound. An essential unread source
requires source work. An identified incompatible-order or recombination
obstruction should narrow or reject the proposed mechanism, rather than be
hidden by Boolean equivalence or uncontrolled copied branches. Arbitrary
ER data existence, formula-only bounds, W/V/U and SAT transfer stay open.
Mathlib matching coverage is not checked. No novelty claim is made.

## Completed source review, step 275

The exact TARGET is retained. The current ordinary uniform P-versus-NP
statement and its Cook-description version are already recorded in
`foundations/01-model-and-target.md` and the ready treewidth assessment;
neither the target nor that same-day source scope changed. A larger
promised class could feed L037, but would still leave arbitrary ER data,
formula-only bounds, W/V/U and unrestricted SAT transfer unresolved.

Queries actually issued:

- `Boolean circuits small backdoor treewidth OBDD conditioning input variables deletion`
- `knowledge compilation map conditioning OBDD variable order Darwiche Marquis 2002`
- `noncommutative IPS Shannon expansion Boolean commutator axioms branching certificates`
- `"circuit" "treewidth" "backdoor" OBDD`
- `"non-commutative" "IPS" "Shannon"`
- `"branching programs" "ideal proof system" conditioning`
- `"noncommutative" "IPS" "conditioning"`
- `"noncommutative" "branching programs" "Boolean" "Shannon"`
- `"treewidth" "OBDD" "deletion" variables circuit`

Search hits are discovery evidence only. Scoped local searches used the
treewidth/OBDD/alternative-witness assessments, foundations, Attempts
019–021 and histories 270–274. No local deletion-promise theorem was found
there. Read L071's construction, L026/L037's exact receiving hypotheses,
and the full L035/L036 constructions and audits. Reuse their ready source
assessments; this is a changed structural promise, not a reason to redo
their unchanged literature comparisons. No cross-notebook input was read.

**Boolean restriction.** Randal E. Bryant, *Graph-Based Algorithms for
Boolean Function Manipulation*, IEEE Transactions on Computers C-35(8)
(1986), 677–691; inspected the [author-hosted annotated manuscript](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf),
Definition 1 (manuscript p.4), Table 1 (p.9), and complete section 4.4
(p.15). The increasing-index hypothesis fixes one variable order.
Restriction bypasses tested vertices according to assigned values;
simultaneous restriction is allowed, followed by reduction. The table
charges O(|G| log |G|) including reduction. This applies to an already
supplied ordered diagram, and supplies no order agreement between diagrams
compiled independently. This annotated version includes later corrections;
no corrected-away output-sensitive Apply claim is used.

**Conditioning and orders.** Adnan Darwiche and Pierre Marquis,
*A Knowledge Compilation Map*, JAIR 17 (2002), 229–264, DOI
[10.1613/jair.989](https://doi.org/10.1613/jair.989),
[published PDF](https://www.cs.cmu.edu/afs/cs.cmu.edu/project/jair/pub/volume17/darwiche02a.pdf).
Read Definitions 5.3–5.5 and the Shannon discussion, printed p.241,
and Proposition 5.1's Appendix A proof: CD cases p.256 and
conjunction/bounded-conjunction cases pp.259–260. Conditioning substitutes
a consistent term. The CD proof treats NNF constants, preservation of
decomposability/determinism/smoothness, and decision-node bypassing.
Fixed-order OBDDs admit binary conjunction; arbitrary-order OBDDs do not
admit general polynomial binary conjunction unless P=NP. Its case expansion
is Boolean equivalence, not equality of free-ring polynomials or a formal
axiom certificate. Use these as restriction/closure facts, not as a
recombination theorem for the present H interface.

**Deletion-distance comparison.** Simone Bova and Friedrich Slivovsky,
*On Compiling Structured CNFs to OBDDs*, Theory of Computing Systems,
published open-access version ©2016, DOI
[10.1007/s00224-016-9715-z](https://doi.org/10.1007/s00224-016-9715-z),
[19-page journal PDF](https://d-nb.info/1119846765/34), section 3.4,
PDF pp.11–13, Lemma 12 and Theorems 13–14, complete proofs.
For a deletion-closed CNF class with polynomial subterm bound p, its
deletion-distance theorem gives OBDD size at most
2^k p(size(E)) |var(F)|, using deleted variables first and an order for E.
The algorithmic theorem additionally requires constructive few subterms
and computable deletion sets. Its proof separates deleted clauses from
deleted variables and then uses the residual-CNF construction.
This concerns deletion from CNF incidence graphs, not removal of original
vertices from a circuit-value graph. A Tseitin encoding would require a
separate graph analysis and elimination of auxiliary variables; neither is
supplied here. No automatic projection or all-root/free-ring consequence
is imported. The arXiv v1 has different numbering (Lemma 4, Theorems 4–5);
the journal version is the comparison reference. PMC access hit a browser
challenge; the journal PDF was accessible, so no source blocker persists.

**Fine-grained lead, delimited.** Michael Lampis, *Circuits and Backdoors:
Five Shades of the SETH*, [arXiv:2407.09683v2](https://arxiv.org/html/2407.09683v2),
13 October 2025: inspected section 2's modulator definition and Theorem 6's
complete statement. This compares sub-brute-force SAT algorithms with
supplied CNF modulators and linear-depth circuit hypotheses. It does not
state the required formal-witness theorem. Its reduction proofs were not
read or imported. New roABP-IPS lower-bound search hits also remain unread
leads, not results about unrestricted affine noncommutative graphs.

## Covered specialization test for a later research turn

Decision SPECIALIZE imports only the cited Boolean operations and the
already assessed compilation/graph machinery. It does not assert a full
statement match. Reuse the exact primary citations and inspected cases in
`2026-10-16-treewidth-two-extension-data.md`: Amarilli–Bourhis–Senellart
arXiv:1604.02761v1 Definition 6.4/Lemma 6.6 and Appendix A; Jha–Suciu
ICDT 2012 Corollary 2.14/section 4; de Colnet–Ordyniak–Szeider AI 351
(2026) Proposition 2. L071's selector construction and suffix graphs are
local inputs, not claims contained in those primary theorems.

For formal corrections reuse audited L035 and L036 and their ready
assessments `2026-10-07-alternative-abp-commutator-witnesses.md` and
`2026-10-07-affine-abp-boolean-witnesses.md`. Their source roles remain
LTW arXiv:1412.8746v4 Theorem 3.4/Lemmas 3.5–3.7, pp.16–18
(formula hypotheses retained), and Raz–Shpilka author manuscript Lemma 2
Step 1, p.5 (disjoint serial/parallel graph operations). Neither imports
an arbitrary-circuit-to-ABP conversion or the proposed gluing result.

One bounded attempt on the unchanged TARGET is now sufficiently covered:

1. Test a correct conditioned Boolean circuit for each assignment to the
   supplied deleted originals. Restore every missing operand explicitly;
   test fresh constant leaves per incident occurrence rather than assuming
   a shared new constant hub preserves width. Retain all signed and unused
   roots. Justify a fixed width bound and one all-root order **within** each
   branch. L071 cannot be invoked wholesale on an invalid or unencoded
   restricted ER proof: justify using its circuit/data construction part,
   or supply a valid restriction translation. Keep the original refutation
   unchanged for the final L037 application.
2. Test ordered Shannon case recombination at the affine-ABP data level,
   allowing different branch orders. Supply the missing formal correction
   argument using only original Boolean and commutator placeholders and
   L035/L036 on explicitly bounded x-only graphs. Exact original roots x_j,
   constants and signed wrappers 1+r_a must be retained; Boolean agreement
   does not justify replacing a formally different interpolant. Retain
   actual factor order, branch cross terms, and both H_i(x,0)=0 and
   H_i(x,A)=r_i+r_a r_b. The new gluing identity and graph realization are
   the proposed mathematical work, not a result proved in this review.
3. Seek one fixed polynomial in T and 2^k bounding all separately written
   values, relations, branch data, correction copies, full original axiom
   and name dictionaries, root associations and deterministic bit time,
   where k is the supplied deletion-set size. Compare this ledger with
   k≤floor(log₂(T+2)); do not hide a cost exponential in 2^k, T^k, a
   k-dependent exponent, or iterated polynomial blowups in depth. Bound
   pre-substitution formal degrees separately; L071's unchanged d,h are
   not part of the proposed conclusion.

Continue if this yields the exact complete polynomial-full-bit data, or a
rigorous intermediate interface that removes one named obstacle while
leaving others explicit. Narrow or abandon this mechanism if branch
framing needs growing width, order alignment is essential but unavailable,
formal corrections require unfolding paths or recursively enlarged witness
operands, or only Boolean/commutative identities can be shown.

Attempts 019–021 remain valid stops on unrestricted OBDD width, degree-only
same-output conversion and a prescribed two-sided pair table. None tests
this deletion promise or lower-bounds every alternative gluing witness.
L070's zero-data route still presupposes an original-axiom certificate and
supplies no existence shortcut. No historical stop is reopened by name.

The review's outcome is EXPLORATION: it completes new source comparison
and identifies a concrete covered test, without a mathematical advance or
informative impossibility result. Mathematical exploration usage stays 0.
The newly ready assessment requires separate approval next invocation;
no research attempt is performed now. Full matching Mathlib coverage is
not checked, and no novelty is certified.
