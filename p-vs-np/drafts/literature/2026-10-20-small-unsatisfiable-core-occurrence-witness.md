# Small unsatisfiable cores — completed source comparison

TARGET: Construct a polynomial-full-bit Boolean/commutator affine-ABP witness for L087's unchanged occurrence product fg when its source CNF has a supplied unsatisfiable core of at most floor(log₂ M) clauses.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 373 searched exact occurrence-product/core witnesses, Boolean-ideal and noncommutative-IPS restrictions, OBDD cores and small-subset resolution; inspected L087, L035 and L090 including its separate audit, the relevant L072 statement and existing primary-source assessments, and Attempts 018/031. No inspected full target match; queries and source limits below.
SOURCE_EVIDENCE: Bryant, IEEE TC 35(8), 677–691 (1986), annotated author copy §4.4 printed p.15; Li–Tzameret–Wang arXiv:1412.8746v4 (2015-09-11), Theorem 3.4 and Lemmas 3.5–3.7 printed pp.16–18, including extraction/commutation cases; Fellows–Szeider–Wrightson, author-hosted 12-page manuscript, Theorem 2 printed p.6 and §4.1 p.8. Reuse L087's inspected occurrence-splitting coverage and L090's restriction/lift/recombination coverage; exact links and qualifications below.
COMPARISON: L090 already supplies exact restriction lifts and paid indicator recombination, but its whole theorem assumes agreement of residual orders. The present promise supplies a small source-clause core instead; formal branch closure and a revised original-M ledger remain to be justified. LTW's extraction retains supplied axioms/formula costs, and a small-core finder is different from receiving supplied indices.
GAP: Test whether branching on the selected core's occurrence variables closes each restricted product without common-order multiplication, then use only L090's applicable lift/recombination components to recover unchanged fg. Prove both formal identities and one original-M polynomial, charging annotation, verification, all branches/pairs and original dictionaries; no branch-closure theorem or new bound is established here.
REASON: Primary comparison and reusable component coverage suffice for one separate bounded mathematical attempt on the unchanged TARGET. The unresolved branch ending and changed cutoff accounting are the specialization to prove, not an essential unread source or an approved theorem; no new mathematics is derived in this literature-only turn.
SCOPE: Exactly L087's constructed occurrence testers from a width-at-most-three source CNF, supplied source-clause indices for an unsatisfiable core of at most floor(log₂ M) clauses, unchanged ordered representatives fg and complete original pre-witness B/M; no arbitrary pair, residual-order agreement, core finder or additional witness alphabet is assumed.

## Preserved startup proposal

The following proposal records the state before step 373. Its statements
that coverage is missing or mathematics unapproved describe that earlier
state; the completed comparison below supplies coverage for a separate
attempt without proving its proposed construction.

This file records a candidate target, not an approved construction or
derivation. No mathematics for it was undertaken in step 372. The
supervisor should route the next invocation to literature comparison.
The assessment date records creation, not a completed source search.

The intended inputs are the exact L087 occurrence construction, its dense
width-three testers, full Boolean/commutator dictionary and original
pre-witness M. Supply a list of clauses from its source width-at-most-three
CNF whose conjunction is unsatisfiable, with at most floor(log₂ M) clauses.
The intended conclusion must retain the original full ordered product fg
and both formal witness identities, not merely a certificate for the core,
a Boolean equality or a smaller pair. All selected clause occurrences,
signs, other input records and the unchanged u/v gadget remain accounted
for. Core verification, construction time, annotation encoding and the
output's full binary length require explicit treatment in any approved
version; no witness availability is assumed.

The proposed mechanism is to exploit a small supplied contradiction while
allowing the rest of the occurrence orders to remain complicated. This
differs from bounding a global contiguous partition or the number of
order-mismatch variables. L095 is relevant stop evidence only; L094 is not
an assumed receiving theorem for the new promise. Any future use of L035
or earlier order-lifting components must inspect their exact hypotheses
and compare existing local results before claiming coverage. Their
applicability here is unproved.

The source review should search the precise small-core/occurrence-product
statement, stronger proof-to-algebraic-witness simulations and known
obstructions, then inspect primary hypotheses. Continue only with a
concrete imported or independently testable ordered lifting target and
a complete polynomial bound in the unchanged input parameter. If known
results already cover it, import them with the necessary specialization.
If the proposed shortcut changes fg, assumes a missing universal witness
bound, or leaves only the already stopped global partition promise,
abandon that shortcut rather than repeat its name.

Potential downstream use is a different restricted W₂ supplier that is
not ruled out by the audited partition obstruction. General small-core
availability, arbitrary-order W₂, arbitrary ER data and unrestricted SAT
would remain independent gaps even if this target succeeds. No novelty,
Mathlib coverage or completed literature decision is claimed.

## Completed comparison — step 373, 2026-10-20

This is LITERATURE / literature_comparison / NOVELTY_UNCHECKED, outcome
EXPLORATION. It is a new source comparison, not an imported full witness
theorem, a construction, a negative witness-size result or an unchanged
approval repeat. No lemma, mathematical script, DAG or argument assembly
is changed. Mathematical exploration usage remains zero since step 369;
literature does not spend or renew that budget.

LITERATURE_REASON: The hypothesis changed from a global oriented-order
partition to a supplied small clause core. No adequate assessment covered
the core-to-original-product interface at invocation start; this review
fills that essential comparison despite the current literature balance.

### Exact gap, relevance and scope

The main gap is still a polynomial-time SAT algorithm or a proof excluding
every such algorithm. This intermediate target concerns only a restricted
supplier for W₂. If it works it could cover small-core occurrence inputs
despite complicated full orders, including inputs not handled by the
partition promise stopped in Attempt 031. It would supply neither small
cores for general UNSAT, arbitrary-order W₂, arbitrary ER data nor SAT
transfer. It is not a candidate resolution of P versus NP.

The current [Clay problem page](https://www.claymath.org/millennium/p-vs-np/)
still links Stephen Cook's [official 12-page description](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf).
Inspected §1 pp.1–2 on 2026-10-20: the target is equality of deterministic
and nondeterministic polynomial-time language classes, with worst-case
input-length bounds and the equivalent checking-relation definition.
The URL has an upload date, not an established manuscript revision date.
No change to the already audited local model is called for.

### Search and primary comparison

Queries included `"noncommutative" "unsatisfiable core"`, `"OBDD"
"unsatisfiable core" polynomial`, `"noncommutative" "restriction"
"IPS" Boolean axioms`, `"small unsatisfiable" resolution proof clauses`,
`"noncommutative IPS" restriction Boolean`, `"occurrence" "OBDD"
"noncommutative"`, `"Boolean" "ABP" "witness" "unsatisfiable" core`,
`"noncommutative" "Shannon" proof`, and `"small unsatisfiable subsets"
resolution refutations`. These searches found no inspected full match;
unrelated hits and unsuccessful searches are not novelty evidence.

1. Randal E. Bryant, *Graph-Based Algorithms for Boolean Function
   Manipulation*, IEEE TC 35(8), 677–691 (1986), [annotated author-restored
   PDF](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf), §4.4 printed
   p.15 (PDF page 15). Read the complete restriction algorithm, including
   root pointers, selected successors, reduction, linear graph work and
   simultaneous restrictions. This covers Boolean restriction; it does
   not equate an original free polynomial with a front-indicator expansion.
   L090 already supplies that stronger local interface with corrections.

2. Fu Li, Iddo Tzameret and Zhengyu Wang, *Characterizing Propositional
   Proofs as Non-Commutative Formulas*, [arXiv:1412.8746v4, 11 September
   2015](https://arxiv.org/html/1412.8746v4), Theorem 3.4 and Lemmas
   3.5–3.7, printed pp.16–18. Read tree-like F-PC extraction, including
   axiom, addition, variable-product, rewriting and contextual commutation
   cases, and the scalar/variable, addition and product commutator cases.
   Lemma 3.5 retains the supplied equation and commutator placeholders;
   Lemma 3.7 supplies a zero-at-zero formula for PQ−QP with a bound in
   the input formula sizes. F₂ is allowed. Neither changes a core
   refutation into the required Boolean/commutator-only original fg
   witness with an ABP-size bound. No unfolding or new extraction theorem
   is assumed; L035 provides the audited graph-sized commutator component.

3. Michael R. Fellows, Stefan Szeider and Graham Wrightson, *On Finding
   Short Resolution Refutations and Small Unsatisfiable Subsets*, [author-
   hosted 12-page manuscript](https://www.ac.tuwien.ac.at/files/pub/FellowsSzeiderWrightson06.pdf),
   Theorem 2 printed p.6, definitions pp.3,5 and §4.1 p.8. Revision date
   of this download is not established. Read the W[1]-completeness
   statement for finding at most k unsatisfiable clauses, its 3-CNF
   qualification and the §4.1 transformation. This is comparison evidence
   about finding a core, not a theorem on a supplied core's witness or
   an unconditional polynomial-time impossibility. The source treats
   clauses as sets without complementary pairs. No transfer of its
   finder theorem to L087's occurrence syntax or logarithmic cutoff is
   claimed, and no Tarsi/minimal-core theorem is needed here.

Reuse the previously inspected Meinel–Theobald occurrence-splitting
mechanism through L087's precise Theorem 4.32-proof/Lemma 4.35 citation
and its explicit transition specialization. No new Boolean reduction
is required. The earlier L090 assessment
`drafts/literature/2026-10-19-small-deletion-set-order-pair-witness.md`
also covers Raz–Shpilka's graph serial/parallel operations and the
diagram-only indicator correction interface. These are reused rather
than reproved or promoted to whole-theorem imports.

The assessment
`drafts/literature/2026-10-08-boolean-zero-affine-abp-ideal-witness.md`
already compares FSTW's commutative, common-order roABP multilinearization
and finite-field restricted IPS lower bounds with this free-ring model.
Their stated order/model/placeholder hypotheses do not supply the
present full witness. Reuse that inspected comparison; no fresh reading
or claim about current general lower bounds is made. Unread search hits
on MUS extraction and other OBDD proof systems are leads only; none is
an essential theorem input to the bounded component test proposed here.

### Local overlap, preserved stops and mathematical work remaining

Read L087's exact testers, occurrence names, literal signs, appended u/v
gadget and complete B/M convention. The annotation refers to clauses
of the source CNF, not merely to an arbitrary Boolean-zero graph. It
does not replace any original record or enter the definition of M.
Malformed indices, repetitions, tautological/repeated clauses, empty
clauses and the empty source conjunction require explicit handling in
the attempted supplier; no promise is silently converted to an oracle.

Read L090's complete proof and separate step-351 audit. Its exact scalar
restriction, one-variable lift (2)–(4) and additive telescoping (5)–(6)
do not use agreement of the remaining orders. Its indicator correction
(8), ordered recombination calculation (9), and recovery (10) likewise
identify specific reusable components, conditional on receiving their
branch-product witnesses. Its common-order branch construction (7) does
use order agreement and is unavailable under the new promise. The
whole L090 theorem therefore does not cover this target. Its ledger
retains the number of queried variables before the final cutoff, so
the revised resource test must start there, not at its stated exponent
14. Read L035's hypotheses, marked-edge proof, endpoints and bit ledger
to check that any proposed calls must have original-only affine graphs,
never recursively generated witnesses. L072's indicator/recombination
coverage is reused via L090; no treewidth hypothesis is removed from
L072's whole theorem.

The local search for small cores and branch-annihilation duplicates found
only the saved proposal. This records search scope, not certified
absence. L088–L094 have order promises described in the supplied overview;
none is imported wholesale here. Attempt 031/L095 remain a valid stop on
universal oriented partitions even with an opposing-unit core. Attempt
018 rules out repeating approval without new source evidence; the new
core hypothesis and component comparison are the present evidence.
Attempt 030's independent universal representation stop is preserved.
No cross-notebook input is used.

### Bounded continuation and decision test

Approve a single separate mathematical attempt on the exact TARGET above.
The proposed test is to restrict just the selected clauses' occurrence
variables and examine whether each complete assignment makes one of the
two original restricted tester polynomials formally zero. This is a
research obligation, not a result of this source review. Do not equate
scalar zero of a two-order product with free-ring zero or assume the
remaining orders agree. Establish any needed factor-zero identification
inside its own ordered multilinear space or directly from the exact
transition recurrence, including cancellations and dense dead levels.

If that branch ending is established, test reception by L090's named
lift, indicator and ordered-recovery components. Pay for up to three
queried occurrence names per selected clause rather than substituting
the clause count for L090's queried-variable count. The attempted ledger
must show that all assignment and ordered-pair copies, full original B,
names, dead/unused original records, core annotation and its verification,
global references and construction time fit one fixed polynomial in the
unchanged original M. Original unsplit variable names may be used to
read the source/core annotation, but cannot become new witness variables.
Both formal identities H(y,0)=0 and H(y,B)=fg are required; a certificate
only for the core or a changed product does not meet this target.

Continue on a complete formal branch argument and paid original-product
assembly meeting that threshold. Abandon this proposed shortcut on an
explicit surviving branch polynomial, a failed ordered interface, or a
demonstrated superpolynomial required cost; preserve that evidence
without claiming every alternative witness is large. A merely unfinished
proof is unfinished, not an obstruction. No bound, branch closure or
lemma is proved or audited in this literature step. The result, if later
established, still requires a separate critical review. Mathlib coverage
for the complete target is **not checked**, not absent.
