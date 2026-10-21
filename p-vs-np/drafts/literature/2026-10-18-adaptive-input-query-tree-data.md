# Adaptive input-query trees — source comparison

TARGET: Construct L037 data polynomial in T+B from a supplied B-bit adaptive original-input query tree whose leaves satisfy L079's counted-path promise at the original cutoff.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 311 searched noncommutative IPS/decision-tree/Shannon/conditioning and adaptive backdoor-tree terminology; compared L080/L072 formal interfaces, L079 original-cutoff reception, the ready commutator assessment and Attempts 019–020. Located established adaptive Boolean backdoor trees and stronger backdoor DNFs, but no inspected full free-algebra/full-bit target match; no novelty inference.
SOURCE_EVIDENCE: Read Darwiche–Marquis JAIR 17 (2002) Definitions 2.6–2.10 pp.232–233 and Proposition 5.1 CD/AND-closure cases pp.256,259–260; Ordyniak–Schidler–Szeider JCSS 144 (2024) 103547 sections 2.3–3 pp.3–4 and Theorem 3/Algorithm 2 proof pp.10–11; Li–Tzameret–Wang arXiv:1412.8746v4 Lemmas 3.6–3.7 complete proofs pp.17–18; Raz–Shpilka 16-page author manuscript Definition 1/Lemma 2 Step 1 pp.4–5. Reuse Bryant/table and local L026/L035/L071 coverage at the locations below.
COMPARISON: Adaptive Boolean conditioning is established; the 2024 detection theorem concerns specified tractable CNF base classes, not the full signed value DAG. LTW supplies contextual formula commutation witnesses, not the adaptive data theorem. L080 supplies leaf components and L072 receives formal interpolation/pair corrections, but its fixed-set indicator construction does not cover different path orders.
GAP: Prove exact path-ordered partition and original/signed interpolation, explicit Boolean/commutator pair corrections without generic Boolean-zero witnesses, and one full-bit/time/degree polynomial in T+B; receive L080's circuit-only leaves at unchanged original T/k and retain every unused root.
REASON: Essential supporting coverage is now adequate for one separate bounded proof attempt on the unchanged target. Import the cited operations; the adaptive formal interface and aggregate ledger remain unproved. This decision approves an attempt, not a new identity, bound or theorem.
SCOPE: A supplied explicit rooted binary query tree of full length B, internal nodes querying original inputs, each input queried at most once on each path, both outcomes retained, and every leaf retaining the full scalar-replaced signed/unused-root DAG without simplification. Every leaf obeys L079's counted-path promise with k=floor(log₂(T+2)) from the original ER length T. No bound on query depth other than no repeated input on a path; no finder or universal existence promise.

## Proposed comparison, not a result

The main gap is unrestricted SAT decision/separation; the nearer gap is
polynomial L037 data for arbitrary supplied ER. The one proposed target
is TARGET. An adaptive tree could use different queried inputs in
different regions, expanding the restricted supplier if its formal
interfaces and cost can be proved. No such expansion is established here.
The intended cost is polynomial in T+B; a polynomial bound solely in T
would additionally require B polynomial in T. Supplying such trees for
arbitrary ER remains a separate unresolved obligation.

The separate review should compare primary decision-tree/conditioning
results and stronger known representations with this exact full-bit
free-algebra target. Reuse L080's original-cutoff leaf construction and
L072's ordered recombination only after matching their input interfaces.
Essential local inputs proposed for comparison are L080, L079, L072,
L026, L071, L035 and L037. The fixed-set indicators of L080 cannot simply
be assumed to cover unequal-depth, differently queried leaves.

The discriminating obligations are exact partition and original/signed
interpolant identities, explicit zero-at-zero indicator-product witnesses
for every ordered leaf pair, and one polynomial paying all leaf data,
corrections, copies, degrees and original dictionaries. Query order may
vary across branches. Boolean partition properties alone do not prove
free identities or provide witnesses. No generic polynomial Boolean-zero
witness theorem, branch-common OBDD order or arithmetic unfolding oracle
is permitted. If a required correction cannot be supplied within the
explicit-tree budget, isolate that obstruction and narrow or abandon
this proposed mechanism. No adaptive identity or bound has been derived
in step 310.

Attempts 019–020 remain the recorded stops on universal common-order
width and degree-only same-output conversion. The source review must
check adaptive compilation overlap and other relevant recorded failures;
this initial proposal does not certify that search complete or claim
novelty. No cross-notebook input is proposed. Full matching Mathlib
coverage is not checked. All source notes and this scope require separate
approval before dependent research.

## Completed separate comparison — step 311

2026-10-18. LITERATURE_REASON: different paths may query different original
sets in different orders and at unequal depths, outside the fixed-set
scope approved for L080. This is the first completed comparison of this
exact target. The proposal above remains a historical pre-review record;
the current single-line decision and this section supersede its pending
review language. No lemma, mathematical script, adaptive identity or
resource bound is established in this literature-only step.

The main gap is unrestricted uniform worst-case SAT decision/separation.
The nearer gap is L037 data for arbitrary supplied ER. The intermediate
target remains exactly TARGET. Its plausible downstream use is a
restricted supplier allowing branch-dependent conditioning, with cost in
the supplied tree length as well as proof length. Polynomial tree size
in T, a tree finder, formula-only certificate bounds and unrestricted SAT
transfer remain independent missing obligations. Reuse the main-target
version in `foundations/01-model-and-target.md`; the problem has not changed.

### Primary sources actually inspected

**Adaptive Boolean representations.** Darwiche and Marquis, *A Knowledge
Compilation Map*, JAIR 17 (2002), 229–264, DOI
[10.1613/jair.989](https://doi.org/10.1613/jair.989),
[published PDF](https://www.cs.cmu.edu/afs/cs.cmu.edu/project/jair/pub/volume17/darwiche02a.pdf):
Definitions 2.6–2.10, pp.232–233, distinguish decision nodes, pathwise
read-once FBDDs and a common-order OBDD. Proposition 5.1's conditioning
proof, p.256, bypasses fixed-variable nodes. Its conjunction cases,
pp.259–260, distinguish unrestricted BDD composition, same-order OBDD
bounded conjunction and the conditional obstruction for arbitrary FBDDs.
These are Boolean equivalences. No free-ring witness theorem follows.
The cited underlying Meinel–Theobald hardness proof was not read here;
no new hardness specialization is imported from it. In particular, do
not posit a polynomial FBDD conjunction algorithm for the adaptive target.

**Backdoor trees and a stronger Boolean interface.** Sebastian Ordyniak,
Andre Schidler and Stefan Szeider, *Backdoor DNFs*, JCSS 144 (2024),
103547, DOI [10.1016/j.jcss.2024.103547](https://doi.org/10.1016/j.jcss.2024.103547),
[published version in the authors' institutional repository](https://eprints.whiterose.ac.uk/id/eprint/213187/7/1-s2.0-S0022000024000424-main%20%281%29.pdf).
Read sections 2.3–2.5 and the opening of section 3, pp.3–4: the base
class has polynomial membership/SAT and is closed under assignments;
the tree has two outcomes and no repeated variable on a path. A
backdoor DNF instead supplies a tautological cover of partial assignments.
Read Theorem 3 and Algorithm 2 with the full theorem proof, pp.10–11;
D+ is defined on p.6 as 2CNF, Horn, AntiHorn and the two unions with 2CNF.
The theorem gives parameterized detection for those classes. The proof
uses class-specific branching sets and bounded-variable enumeration;
its tree case invokes Proposition 2, whose statement and enumeration
proof on p.4 were also read. This is neither a polynomial-in-tree-length
formal-witness theorem nor detection for L079's value-DAG promise.
Backdoor DNFs are a relevant stronger Boolean representation, not an
approved replacement for the supplied tree or its ordered identities.

The 2008 Samer–Szeider *Backdoor Trees*, AAAI pp.363–368, was a discovery
lead. Its author-hosted PDF returned retrieval errors; search-index
excerpts are not treated as inspected theorem evidence. The accessible
2024 primary paper supplies its own definitions and comparison, so that
older access failure is not an essential source blocker for this target.
No 2008 detection claim is independently imported. Other search hits on
probabilistic backdoors and symmetry diagrams remain unread leads.

**Formal commutation.** Fu Li, Iddo Tzameret and Zhengyu Wang,
*Characterizing Propositional Proofs as Non-Commutative Formulas*,
[arXiv:1412.8746v4](https://arxiv.org/pdf/1412.8746v4), 11 September 2015,
Lemmas 3.6–3.7, printed pp.17–18: read the complete context, base,
addition and ordered-product cases. For supplied formulas P,Q, Lemma 3.7
provides a commutator-placeholder formula vanishing at zero placeholders
and specializing to PQ−QP, with size at most |P|²|Q|². Lemma 3.6 covers
one such exchange inside an addition/product formula context. F₂ is
permitted; subtraction becomes addition and pair-once commutators match
the local dictionary. These theorems may be cited for the paid literal
products and their explicitly written contexts. They do not provide an
arbitrary-ABP-to-formula conversion, Boolean reductions or a bound for a
whole adaptive sequence without accounting for its copies. No reproof
of these theorems is needed. L035 is the audited local graph-input
commutator result for branch values; the formula theorem is not silently
applied to arbitrary branch graphs.

**Graph reception.** Raz and Shpilka, *Deterministic Polynomial Identity
Testing in Non Commutative Models*,
[16-page author manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf),
Definition 1 and Lemma 2 Step 1, PDF pp.4–5: read the path convention,
the full lemma hypotheses and all Step 1 cases. Only conversion of
already paid formula trees by leaves, parallel sums and ordered serial
products is imported. Step 1 allows constants and mixed degree; the
full lemma's later zero-free-term restriction is not imposed on that
component. It supplies no uncharged sharing or unfolding operation.

### Local reuse, duplicate search and remaining difference

Targeted local searches for adaptive query trees, free decision diagrams
and indicator corrections in `drafts/literature/`, `ATTEMPTS/` and
`history/` found the current proposal, step 310's proposal record and an
older graph-representation comparison, not a completed adaptive supplier.
The relevant fixed-set construction remains L080, proof sections
“Circuit-only reception at the original cutoff”, “Indicator reception
and exact roots”, “Ordered formal recombination”, and its step-310 audit.
L072's equations (2)–(7) were read in full: the recombination algebra
receives formal partition/interpolants and pair Q identities; its proof
of those indicator premises specifically uses one fixed queried set/order.
The adaptive premises must be proved before reusing that component.

The unchanged leaf receiver and its polynomial construction cost are
covered by `2026-10-18-input-deletion-counted-path-critical-audit.md`
and `2026-10-18-input-deletion-large-branch-depth-data.md`. Reuse L080's
L079 component specialization, not a restricted ER refutation or a new
cutoff. The original alphabet inclusions must retain exact root scalars,
unqueried originals, both signs and all unused extensions at each leaf.

The ready `2026-10-07-alternative-abp-commutator-witnesses.md` and
L035's audited theorem supply graph-input commutation. L026's common-order
diagram hypotheses and L072's constant-width indicator reception were
compared. L071's post-compilation graph component is available only after
matching the actual ordered polynomials; its whole treewidth theorem is
not being applied to arbitrary residuals. Bryant's 1986 section 1
equation (1)/section 2 Definitions 1–2 small-table coverage is reused from
the ready leaf assessment, without a fresh retrieval or reproof.

Attempts 019–020 remain intact. This target supplies a tree and restricted
leaf components; it asserts neither universal common-order width nor a
degree-only same-output circuit conversion. No assertion is made that
adaptive trees evade either obstruction on all ER proofs. Changing branch
orders also does not permit identifying arbitrary Boolean-equivalent
polynomials in the free ring. Full matching Mathlib coverage is not
checked, and no absence claim or cross-notebook theorem input is made.

### Boundary of the separately approved proof attempt

Use the explicit tree's actual path order for proposed leaf indicators.
The following are proof obligations, not results of this review:

1. Establish formal partition and every exact original/scalar/signed
   interpolation, including leaves that stop without querying a given
   original and trees with different orders in disjoint subtrees. A
   proposed subtree induction must retain path assignments; Boolean
   agreement is insufficient.
2. Construct zero-at-zero Q witnesses for every ordered leaf pair,
   specializing to e_l e_m+delta_(l,m)e_l. One assessed technique to test
   is explicit contextual commutation of paid literal products followed
   by explicit Boolean reductions. Any passage through canonical order
   must pay both order-change corrections, including the diagonal target
   in its original path order. The inspected LTW operations cover the
   commutation steps; their number, Boolean steps and total size remain
   to be proved. A global common-order partition identity is not supplied.
3. Only then receive the unchanged ordered L072 recombination component,
   with L035 applied to x-only leaf/indicator graphs. Prove both formal
   H identities for all definitions. No recursive H graph is an input
   to the commutator constructor.
4. Bound the actual number of leaves, total written path lengths, all
   pair corrections and all independent copies by the explicit input
   budget. Combine with the original-T leaf construction, complete
   dictionaries and pre-substitution degrees in one polynomial in T+B.
   Do not enumerate all assignments to the union of queried variables,
   or replace full B-bit encoding by depth or logarithmic leaf count.

Discriminators for the later proof are the singleton unqueried leaf,
unequal-depth branches, a variable queried in just one subtree, two
subtrees querying shared remaining variables in opposite orders,
diagonal/off-diagonal leaf pairs, scalar-only residuals and unused roots.
These are proposed proof cases; no computation or identity test was run.

Continue only upon full formal identities and a uniform polynomial in
the actual T+B. If a proposed exact interpolation is false, preserve its
counterexample rather than weakening L037's exact bases silently. If
pair corrections or accounting require a generic polynomial Boolean-zero
witness premise, arbitrary FBDD conjunction or exponential union-set
enumeration, abandon that mechanism and isolate the failed obligation.
Essential source coverage is now ready for this bounded attempt; no
additional literature is required without a changed hypothesis or a
specific new essential source. This approves the unchanged target for
the next research turn, without deriving or approving its mathematics.
