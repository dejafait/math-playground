# Fourth comparison: cancellation-based sparse certificate — completed review

TARGET: Assess a cancellation-based simulation certificate for job-7 R_axiom=FG+GF with total matrix support and intermediate graph size O(S_comm), where S_comm counts the two explicit normalized endpoint graphs.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 524 searched scalar simulations, sparse equivalence certificates, commutator/telescoping ABPs, constructive conjugacy, functional factorization and up-to congruence; exact queries, inspected primary passages, local duplicates and retained stops are recorded below. No full quantitative match was established; this is not an exhaustive absence or novelty claim.
SOURCE_EVIDENCE: Reused steps 519/520 and October 25 coverage; inspected Ésik–Maletti 2010 Definition 3.1/Theorem 4.2, Sakarovitch 19-Sep-2008 Theorem 24, Ésik–Maletti arXiv:1005.2079v1 Lemmas 8–10/Theorem 11, Li–Tzameret–Wang arXiv:1412.8746v4 Lemma 3.7, Kiefer et al. author journal manuscript Proposition 3.1/§3.1, and Bonchi–König–Küpper arXiv:1701.05001v1 Proposition 3.1/Definition 4.1/Proposition 4.2/Theorem 4.3; versions, pages, proof cases and direct links below.
COMPARISON: The semantic identity, general simulation soundness and qualitative common simulators are known. Inspected factorizations start from an already supplied matrix and do not establish linear total graph/support cost in S_comm. Ring congruence membership reduces to span membership; neither that fact nor sparse randomized rational zeroness testing supplies the requested exact chain.
GAP: A uniform linear bound for explicit cancellation-cut intermediates and oriented scalar maps between independently recipe-bound R_axiom and P remains uncovered. No maps, bounds, finite receipts, counterexample or lower bound are supplied by this literature step.
REASON: Accessible sources fix the semantics and separate the quantitative gap sufficiently for one bounded construction test; import those inputs and test the cancellation-cut family rather than reprove equality, repeat ancestry pruning or rely on unbounded general existence.
LITERATURE_REASON: The endpoint pair and mechanism change from literal copy ancestry/pruning to F₂ cancellation in marked-edge telescoping; essential coverage for the quantitative certificate claim is missing, not an inaccessible old source.
SCOPE: This completed step is source comparison only. The separately saved construction assessment requires next-turn approval before research; no row search, finite replay, receiver/format change, cap increase, historical-cost recovery or new mathematical derivation occurred here.

The original question and candidate-selection text below are preserved from
step 523. Its prospective instructions describe the review now completed;
the completion section at the end records the actual evidence and decision.

## Exact question and possible use

Fix source record 78, events 2642–2643, output-493 `jobs[7]` and the
original-only F,G specified independently as in L110 §§2–3. R_axiom is
the normalized full-copy marked-edge graph with its complete ordered
dictionary substitution. P is the separate serial/parallel graph for
FG+GF in L110 §3, with fresh copies, roots and constant connectors.
Set S_comm=g(R_axiom)+g(P), where g counts all explicit vertices, edges
and singleton-label entries before finite constant closure. The proposed
threshold is one constant C independent of operand sizes, with both total
support across a finite simulation chain and summed intermediate graph
size at most C*S_comm. Its number of arrows, boundary/index cost and
checking work must also be accounted for; padding the endpoints or
replacing S_comm by path counts is not the question.

The candidate mechanism is to represent the ordered telescoping cuts and
their F₂ cancellations by intermediate states and oriented scalar maps.
This is a proposal only: no such representation or equations are supplied.
No occurrence-core isomorphism between R_axiom and P is assumed, and maps
need not be partial permutations. General scalar simulation soundness is
already covered, as is the semantic identity. Reproving either would not
answer the quantitative question. Finite right closure, unequal dimensions,
empty/coincident/nonextremal roots, constants, zero labels, repeated words
and parallel cancellation remain mandatory if a construction is later tried.

The local use would be a sparse certificate for the fourth comparison left
open by L111, before any complete receiver is considered. The main gap is
still uniform worst-case P versus NP. This target supplies neither general
certificates nor a lower bound or decision algorithm, even if successful.

## Candidate selection and retained stops

Three alternatives were compared without attempting their mathematics:

1. Implement strict sparse W/R reception from the audited L111. This is a
   meaningful later engineering target, but it leaves Dcomm untouched and
   needs its own full binding/decoding/work ledger. It is not selected now.
2. Search for dense invariant rows for Dcomm using L110. The qualitative
   theorem is available, but actual ranks and finite costs remain unknown;
   the failed full-rank endpoint is not a lower bound on actual rank.
   Dependent coordinate execution stays parked pending a new complete
   finite preflight. It is not selected or declared impossible.
3. Assess a cancellation-based sparse chain for the independent Dcomm
   endpoint pair. This is selected as a different mathematical certificate
   question, whose equations and support threshold could be tested without
   reexecuting a stopped word expansion or recovering historical costs.

Attempts 042–045 preserve their particular record/word/evidence failures;
Attempt 046 preserves the unbounded historical administrative remainder.
The L111 audit passes and is not an exhausted or failed proof. No new failed
attempt is manufactured to satisfy recovery metadata. The CSR06/HAL access
lead remains parked and is not an essential prerequisite here: accessible
primary definitions already fix the simulation equations. No failed URL
retry or reapproval of unchanged ancestry coverage is the next task.

## Sources to reuse, missing comparison and discriminating test

Reuse [Ésik–Maletti's author manuscript](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf)
and [Sakarovitch's 19-Sep-2008 Handbook draft](https://perso.telecom-paristech.fr/jsaka/ENSG/MPRI/Files/References/JS-HWA.pdf)
at the precise statements above, as inspected in steps 519/520. F₂ fits
their finite-semiring/field settings; qualitative existence and functional
factorization have no imported bound in S_comm. Reuse
[Kiefer v1](https://arxiv.org/pdf/2009.01217v1) for field-valued word
coefficients and invariant-space coordinates. L110 §4 and L111 §7 already
justify the chosen finite right closure. L035 (2), (4)–(7) gives the exact
ordered commutator identity and four-copy realization; its LTW formula
comparison is not a sparse-simulation bound for arbitrary ABPs.

Next review must search the exact cancellation certificate claim, stronger
constructive simulation results, standard weighted-automaton conjugacy and
algebraic telescoping terminology, and relevant support-size obstructions.
Inspect primary hypotheses and relevant constructive proof cases; import a
matching theorem with its actual bound rather than construct a duplicate.
Unknown/unread sources remain leads. The scoped local searches so far do
not establish absence or originality. Full matching Mathlib coverage is
not checked.

The review succeeds if it identifies a precise import or a bounded uncovered
specialization with independently checkable oriented boundary/transition
equations and a uniform support/intermediate-size threshold. A later attempt,
if approved, must either give that certificate or retain a fully specified
failed equation/size obstruction for its proposed cut-state maps. Failure
of those maps would stop that mechanism, not refute Dcomm or all sparse
certificates. Any primary theorem proving only equality, an unspecified
common simulator or arbitrary polynomial size must retain that difference.

This pending assessment does not approve the candidate or classify it as
creative mathematics. The comparison must determine whether it is known
specialization or has a substantive new quantitative obstruction. No
justified mechanism for the unrestricted P-versus-NP gap has been prepared;
source coverage is the immediate blocker to this distinct local candidate.
Independent byte/recipe/occurrence binding, strict reception, full finite
wire/work/live costs, later jobs, Boolean/K/H/nonzero-fJ, general availability
and L087 W₂ remain unresolved. No cross-notebook input is proposed.

## Completed comparison — step 524, 2026-10-26

This was one LITERATURE / EXPLORATION / NOVELTY_UNCHECKED step. It did not
construct cut states, derive a new identity or run a mathematical script.
The main gap, intermediate threshold and downstream use remain exactly
those in the original question. The result is a bounded coverage decision,
not a mathematical advance beyond the inspected sources.

### Local comparison and exact discovery queries

Read L035 in full; L038's evaluator, local substitution and finite-closure
passages; L110 §§2–4, §21's recipe/copy cases and §24's terminal disposition;
L111 §7; steps 519/520; and the October 25 coefficient-space assessment.
Searches were restricted to these relevant local assessments/proofs and
Attempts 042–046. L035 already supplies the semantic telescoping identity.
L111's accepting-core isomorphism is a different premise and cannot be
assumed for R_axiom and P. L110's dense coordinate interface remains a
conditional alternative; no actual ranks or fitting evidence were imported.
The retained stops concern particular record, word, evidence and historical
accounting contracts, not all symbolic cancellation certificates.

Queries actually issued, grouped by discovery purpose:

- `weighted automata simulation equivalence sparse simulation matrix size bound field cancellation`
- `algebraic branching programs commutator telescoping sparse certificate automata conjugacy`
- `weighted automata "conjugacy" "size" simulation chain field sparse`
- `weighted automata "telescoping" simulation`
- `"noncommutative" "commutator" "branching programs" certificate`
- `"weighted automata" "sparse" "equivalence"`
- `"weighted automata" "simulation" "certificate"`
- `"algebraic branching programs" "identity" "certificates" noncommutative`
- `"weighted automata" "commutator"`
- `"weighted automata" "cancellation" "simulation"`
- `"weighted automata" "strongly proper" field simulation size`
- `"algebraic branching program" "commutator" telescoping certificate sparse`
- `"noncommutative" "telescoping" "automata"`
- `weighted automata bisimulation up to congruence field linear combinations certificate size Bonchi Pous`
- `weighted automata conjugacy equivalence polynomial size sparse matrices support lower bound`

These searches found the primary constructions below, plus unrelated
telescoper, ordered-semiring and partially commutative-monoid results.
Search silence does not establish a lower bound or originality. No inspected
source establishes an obstruction to **all** sparse chains for this pair.

### Primary statements and load-bearing constructive cases

**Ésik–Maletti**, [*Simulation vs. Equivalence*, 2010 author manuscript](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf),
Definition 3.1 and soundness, printed p.2; Theorem 4.2, complete construction,
Corollaries 4.4–4.5 and deterministic finite-semiring variant, p.3. Rechecked
the oriented initial/transition/final equations and paired reachable-row
generators. The common simulator's maps are the two coordinate blocks of
those generators; transitions express their images as linear combinations.
F₂ satisfies the finite-semiring and field hypotheses. This imports
qualitative existence and soundness. The proof does not bound nonzero
entries and explicit intermediate transitions by our preclosure endpoint
measure. Enumerating all reachable paired rows in its deterministic variant
does not supply that bound either. No sparse-map inference is made from
qualitative properness. The manuscript has no further established revision
date here; the inspected version is the four-page author PDF.

**Sakarovitch**, [*Rational and recognisable power series*, Handbook draft,
19-Sep-2008](https://perso.telecom-paristech.fr/jsaka/ENSG/MPRI/Files/References/JS-HWA.pdf),
reuse Definitions 11–13/Proposition 12, printed pp.26–27; freshly inspect
Theorem 24 and its joint-reduction proof, pp.58–59. The theorem includes
(skew) fields. Its paired-representation construction chooses generating
vectors and splits their transfer matrix into left and right blocks.
This is not an endpoint-size support theorem. Also inspected Theorem 5
and its first factorization paragraph, p.30: its stated automata theorem
is over Z; the subsequent property-(P) discussion includes fields. Neither
passage alone justifies importing the Z state-splitting theorem as an
F₂ quantitative graph bound. The inaccessible historical CSR06/HAL lead
is unnecessary for the scalar equations and is not retried.

**Ésik–Maletti**, [*Simulations of Weighted Tree Automata*,
arXiv:1005.2079v1, 12-May-2010](https://arxiv.org/pdf/1005.2079v1),
Lemmas 8–10 and Theorem 11 with its full constructive proof, printed
pp.7–10. Read unit-sum factorization, degenerate/zero-sum padding, recursive
row/column completion, and transition reconstruction by the matrices Y.
The hypotheses are equisubtractivity and additive generation by units;
F₂ meets them as a field, with nontrivial zero sums. The theorem factors
an **already given** simulation into cofunctional, invertible diagonal and
functional simulations. Its index set comes from unit decompositions of
the starting matrix entries, and its intermediate transitions are built
from prescribed row/column sums. This does not produce the missing sparse
starting matrix or a linear transition ledger in S_comm. Sparse factors
alone do not account for those transitions. This source is a comparison
against a proposed shortcut, not a new tree-to-string construction input.

**Li–Tzameret–Wang**, [*Characterizing Propositional Proofs as
Non-Commutative Formulas*, arXiv:1412.8746v4,
11-Sep-2015](https://arxiv.org/pdf/1412.8746v4), Lemma 3.7 and its entire
proof, printed p.18. Read constants/variables and both additive and
multiplicative induction cases. The known witness has size at most
|P|²|Q|² for **formula** inputs. F₂ changes subtraction to addition.
This covers the product-commutator algebra already used in L035; it does
not give scalar simulation maps or their support for arbitrary supplied
ABPs. Formula unfolding is not licensed as a linear-cost operation here.
Reproving this identity would not address the reviewed gap.

**Kiefer–Murawski–Ouaknine–Wachter–Worrell**, [*On the Complexity of
Equivalence and Minimisation for Q-Weighted Automata*, author journal
manuscript](https://www.cs.ox.ac.uk/james.worrell/fossacs12-journal.pdf),
22-page version, revision date unestablished; Proposition 3.1 and §3.1,
printed pp.5–7, including Figure 1, polynomial encoding, Schwartz–Zippel
hypotheses and stated O(n|M|) sparse runtime. The bounded-word span fact
allows any field, but the inspected randomized algorithm samples rational
integers and reports probabilistic zeroness. Neither a sampled zero nor
its sparse arithmetic runtime is an exact F₂ simulation certificate of
linear support. No large-field/random-evaluation hypothesis is silently
applied to F₂. This resolves the particular misleading sparse-runtime lead;
the ready deterministic Kiefer 2020 coordinate coverage is unchanged.

**Bonchi–König–Küpper**, [*Up-To Techniques for Weighted Systems*,
arXiv:1701.05001v1, 18-Jan-2017](https://arxiv.org/pdf/1701.05001v1),
§§2–3.2/Proposition 3.1, printed pp.3–4; §4.1 Figure 1, Definition 4.1,
Proposition 4.2 and Theorem 4.3 with both return cases, pp.7–9; Appendix A.2,
Lemma A.3's submodule/congruence correspondence and Proposition 3.1's proof,
pp.18–20. Scalars are a commutative semiring; the ring clause covers F₂.
Congruence membership is membership of a vector difference in the submodule
generated by the given differences. Sound up-to reasoning therefore handles
linear cancellation without pathwise isomorphism. The inspected results
do not bound generator support, transition-coordinate evidence or explicit
intermediate graph size by S_comm. They also use column-vector transition
conventions, requiring translation before any local application. Up-to
soundness cannot substitute for the requested scalar chain and its ledger.
The tropical/l-monoid rewriting and similarity results are not imported.

Kiefer 2020, Mohri and Raz–Shpilka retain the exact ready coverage and
qualifications in the October 25 assessment. L038/L110 fix right finite
constant closure and word gadgets; no new closure lemma is needed.
Full matching Mathlib coverage of the quantitative cancellation-chain target
is **not checked**; supporting coverage is not a full matching theorem.

### Coverage decision and bounded continuation

DECISION is EXPLORE. Sources suffice for the scalar equations and known
algebra, but the bounded search establishes no matching uniform support
and graph-size theorem. This does not assert novelty. General simulator
existence, functional factorization and up-to congruence are insufficient
as *justifications of the requested ledger*, not proved impossible routes.

The independently testable proposal is to lift L035's adjacent-cut
cancellations to scalar maps on graph-indexed cut states. First account
for the inner G cuts and then the outer F cuts in their fixed order; use
operand vertices and marked edge occurrences, not complete paths or words.
This describes a family to test, not any constructed states, arrows or
equations. Count every required occurrence and repeated intermediate;
no path history, dense uncharged state table, polynomial-valued map or
assumed common accepting core may supply missing information.

The continuation succeeds only with explicit oriented initial/final and
constant/letter transition equations, compatible finite right closure,
and an explicit universal C for both total map support and summed g of
all intermediates. It must account separately for arrow count, boundaries,
indices and graph checking work, including constants, literal-empty central
lists, zero-valued but structurally nonempty graphs, parallel cancellations,
unequal paths and coincident/nonextremal roots. Endpoints stay fixed and
independent; no padding or replacement of S_comm by operand path counts.
A fully specified failed equation or superlinear size requirement for
this proposed cut-state family is an informative stopping result for the
family only. An unproved map or unresolved estimate remains unfinished work.

Prepared `drafts/literature/2026-10-26-dcomm-cancellation-cut-construction.md`
for separate approval next turn. No construction was derived and approved
in this turn. The new quantitative mechanism could address the branch's
fourth-comparison bottleneck; there is still no prepared creative route
closing unrestricted P versus NP, general availability or total reception.
