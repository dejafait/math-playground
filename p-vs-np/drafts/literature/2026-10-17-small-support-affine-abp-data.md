# Small syntactic support — source comparison

TARGET: Construct polynomial-full-bit L037 data when every extension's syntactic original-variable support has size at most floor(log₂(T+2)), allowing exponential exact syntactic degree.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L026, L071 including its step-274 audit, L037, their saved OBDD/treewidth assessments and Attempts 019–020; the October 5 assessment already proposed logarithmic support as an unproved alternative. Fresh queries for few-variable OBDDs, logarithmic-support noncommutative certificates and small-support OBDD circuits found no inspected full-statement match; no novelty inference follows.
SOURCE_EVIDENCE: Freshly read Bryant IEEE TC 35(8) (1986), author-restored §1 equation (1), §2 Definitions 1–2 (PDF pp.3–4), and de Colnet–Ordyniak–Szeider AI 351 (2026), 104458, §2.3 and Proposition 2 with its dummy-node discussion (PDF pp.3–4); reuse the prior formal-witness and graph-composition coverage through L026/L071 rather than repeat its discovery search.
COMPARISON: Standard ordered Shannon representation and same-order completion cover the Boolean diagram operations; L026 supplies the exact formal H identities and L071's post-compilation construction realizes their identical polynomials by affine ABPs. Neither L071's treewidth-two theorem as stated nor an inspected external theorem is a full match for the new support premise. No new witness recurrence is called for.
GAP: In a separate mathematical step justify syntactic-support extraction, support-table construction in one fixed global order, all-root completion and a single polynomial full-bit/time ledger; apply the existing L026 identities and L071 graph construction without assuming the full source DAG has small treewidth.
REASON: Essential source coverage is available for one bounded specialization attempt. The support-to-diagram applicability and total encoding argument remain to be written and checked; this literature-only turn does not establish that construction or its bounds.
SCOPE: L037's width-at-most-three signed-AND ER conventions and actual binary T, all signed and unused roots, exact original/signed values, arbitrary reduced extension representatives, and complete original-axiom dictionaries; no small-support assumption is inferred for arbitrary ER.

## Proposed promise and use

Syntactic original-variable support means the distinct original generators
reachable through the canonical value DAG, ignoring signs and counting
repeated occurrences once. Absent nonextension variables have no original
support. The promise applies to every positive extension, including unused
ones. It is an input restriction, not a semantic-support oracle or a
consequence of short ER proofs. Retain all original variables and both
signs in the resulting package. Reduced extension representatives are
permitted; identical free-polynomial representatives are not required.

The main gap is unrestricted SAT decision/separation; the immediate gap
is polynomial-in-T supplied data for general ER. This proposed restriction
could test a different way to obtain data where L076's numeric D is too
large. It does not propose a general degree bound or reopen the stopped
arbitrary-circuit same-output conversion. Independent formula-only,
alternative-certificate, W/V/U and decision-transfer gaps remain.

## Separate review and discriminating test

First compare the exact target with L026, L071 and their existing source
assessments; inspect only the needed construction/hypothesis passages.
Determine whether fixing one global original-variable order and supplying
explicit support-based diagrams falls entirely within their scope, or
whether a further witness/encoding specialization is needed. Import any
full match rather than reproving it. The prospective inputs are L026,
L071 and L037, with L076 only a comparison. No cross-notebook input is
proposed; Mathlib coverage is not checked.

Relevant existing stops to compare are the common-order-width obstruction
L027/Attempt 019 and the arbitrary arithmetic-circuit obstruction
L033/Attempt 020. Their broader inputs must not be treated as a failure of
this restricted promise without checking hypotheses. No new obstruction
or sufficiency inference is made in this continuation note.

Continue only if the separate review identifies ready coverage and a
concrete construction/import paying all roots, local relations and full
binary dictionaries in one polynomial in T. If a claimed source interface
does not preserve both formal H identities or explicit affine-edge
graphs, record the exact missing obligation before attempting mathematics.
A duplicate fully covered result calls for import, not a novelty claim.
This assessment does not approve itself; the next invocation is
literature-only.


## Separate literature comparison — step 295, 2026-10-17

The TARGET is unchanged. The proposal above is preserved as the pre-review
record: its statements that coverage is incomplete describe the starting
state. This section discharges that source gate, not the mathematical
construction. No lemma, mathematical script, PROOF.md or DAG.md is changed.

**Main gap and use.** Unrestricted SAT decision/separation remains open;
the immediate representation gap is polynomial-in-T complete L037 data for
general supplied ER. The intermediate target is exactly TARGET. Success
would supply L037 on a restricted class where exact syntactic degree need
not be small. It supplies neither arbitrary-ER coverage, a formula-only
bound, W/V/U, every-certificate hardness nor a SAT decision transfer.

**Discovery and duplicates.** Actual new queries were `Bryant 1986 binary
decision diagram truth table full binary tree 2 n variables`;
`"logarithmic" "support" "OBDD" circuit`;
`"OBDD" "few variables" "truth table"`;
`"logarithmic support" "noncommutative" certificate`; and
`"OBDD" "small support" "circuit"`.
No retrieved exact theorem is imported on the strength of a search hit.
A sampling/order heuristic paper was only a discovery lead, not theorem
coverage. Bryant's 1992 survey was opened, but its reversed text extraction
and screenshot calls supplied no reliable additional load-bearing passage;
no statement from it is needed or asserted inspected in readable form.

The precise local duplicate check matters: the October 5 OBDD assessment
already lists logarithmic support per local gate as its second candidate,
without a proved construction. Thus the idea is recorded, not a new
mechanism discovery. L026's completed formal correction theorem is now
available, and L071's subsequent graph realization avoids proposing those
same corrections again. L071's whole theorem assumes full-graph treewidth
two; this review does not drop that hypothesis from its statement.
Only its explicitly separate post-compilation graph construction is a
component for the proposed specialization.

**Primary Boolean representation input.** Randal E. Bryant,
[*Graph-Based Algorithms for Boolean Function Manipulation*, IEEE TC
35(8), 677–691 (1986)](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf),
author-restored 28-page file: §1 equation (1), PDF p.3; §2 Definitions 1–2,
PDF p.4 (printed pp.4–5). The inspected Shannon equation specifies the
cofactor recursion. Definitions 1–2 give ordered tests with low/high
successors, constant terminals and assignment-path semantics. The fixed
order is shared between represented functions. Reducedness is unnecessary
for this target. These passages support using ordinary ordered truth trees;
they do not assert a formal noncommutative correction theorem. A later
proof must explain why syntactic reachable support suffices to evaluate
the appropriate cofactors and charge their enumeration. Semantic support
detection is neither supplied by this source nor needed as an oracle.

**Completion input and cases.** Alexis de Colnet, Sebastian Ordyniak and
Stefan Szeider, [*OBDDs, SDDs, and circuits of bounded width: Completeness
matters*, Artificial Intelligence 351 (2026), 104458](https://eprints.whiterose.ac.uk/id/eprint/234745/9/1-s2.0-S0004370225001778-main.pdf),
§2.3 and Proposition 2, PDF pp.3–4. Completion preserves the order and
function, takes O(n|B|) time and increases width by at most a factor n.
The surrounding discussion explicitly inserts equal-successor dummy
nodes and handles irrelevant variables and constants, despite the earlier
BDD definition's distinct-successor wording. The intended later
application must specify the full original-variable universe and fill
root, internal-edge and early-terminal gaps. No false constant-width
pathwidth converse is needed. These are Boolean operations; their runtime
is not the complete binary encoding ledger of the desired package.

**Reused formal and graph interfaces.** Read the complete L026 proof,
L071's explicit value/K/W/P graph construction, its all-root ledger and
step-274 audit, and L037's receiving hypotheses. Reused assessments are
`drafts/literature/2026-10-05-obdd-reduced-data.md`,
`drafts/literature/2026-10-16-treewidth-two-extension-data.md` and
`drafts/literature/2026-10-17-treewidth-two-data-critical-audit.md`.
Their inspected noncommutative/graph sources are retained as supporting
coverage; this turn does not claim a fresh reading of those primary PDFs.

L026 equations (4)–(9) supply exact signs, suffix commutation and the
paired W identities, with d=max(1,n), h=max(1,2n−1). Its increasing-
multilinear injectivity identifies the separately supplied output with
the paired product; Boolean equivalence of arbitrary free polynomials
would not suffice. L071's post-compilation construction explicitly
realizes these identical recurrences with affine edges: value states,
a one-way K-to-value switch, and paired W states with disjoint local
correction exits. The audited accounting uses B=T+n+2, v=w+2,
R=B(n+1)^2 v^3+n^2+1 and E_ABP=O(R(T+log(R+2))+T^3), for a common complete
width-w family. This is a component bound already written and audited,
not a new support-specialized bound established here. The treewidth
compiler and selectors belong to its earlier Boolean compilation stage;
the later construction explicitly receives the diagrams. A later proof
must isolate this component use instead of citing L071's whole conclusion
on an unchecked structural promise. L037 is used only after the full data
and dictionary framing meet its hypotheses.

**Stops and qualifications.** Attempt 019/L027 concerns unrestricted
extension functions with many reachable original generators, not a
logarithmic-support promise. Attempt 020/L033 concerns identical free
polynomials of arbitrary arithmetic circuits. Here reduced representatives
are permitted and signed-AND syntax supplies the support information.
Neither stop refutes this target. Conversely, neither the present source
review nor those exceptions establishes its sufficiency. L076's numeric-D
criterion remains intact; no small-degree assertion about exact repeated
squaring is made. All unused extensions and both signs stay in scope.

**One approved next mathematical step.** Keep TARGET verbatim. Test the
standard support-table/ordered-tree route in a fixed global original order;
use the completion input and import L026's H identities plus L071's
explicit graph realization rather than reprove their recurrences. The
remaining proof should cover syntactic support computation, absent
nonextension variables, zero-support/n=0 cases, repeated/signed operands,
all unused roots and every diagram, graph, symbol, reference and dictionary
write. It must compare the support-enumeration cost with the required
polynomial-in-T threshold, and bound bit time as well as output size.
No exact degree D may enter that final polynomial. A mathematical
specialization should be classified REPRODUCTION unless it identifies a
specific genuinely uncovered difference; no certified originality follows.

Continue if that applicability argument gives both formal H identities
and one full polynomial bound for all data. If it instead needs a semantic
support oracle, incompatible per-root orders, implicit graphs, uncharged
ancestry unfolding or a missing formal witness, record the exact failed
interface and narrow/abandon that construction. Independent general data,
formula-only and SAT gaps remain unresolved. No cross-notebook input is
used. Mathlib matching coverage is not checked; no absence is asserted.

This is a literature EXPLORATION / NOVELTY_UNCHECKED: it establishes source
readiness and identifies a recorded overlap, without proving the target
or claiming progress beyond the inspected sources. It spends no
mathematical exploration allowance. No further literature is needed for
this unchanged target before the bounded mathematical specialization.
