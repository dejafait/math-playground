# Expander weighted-value availability — source comparison

TARGET: Test whether L030's expander cut-rank obstruction rules out polynomial-size L085 value graphs for L031's unchanged used extension.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read local L030/L031 proofs, L085 hypotheses and Attempts 019/020/029; searched weighted/parity OBDD rank, roABP evaluation dimension and expander/independent-set algebraic lower bounds; inspected the primary sources below, without finding an inspected full-statement match for the unchanged ER/weighted-value interface.
SOURCE_EVIDENCE: Read FSTW ToC 17(10) (2021), Lemmas 3.4–3.7 and 3.11, printed pp.19–20; Andrews et al., ITCS 2026 article 9, Definitions 5–7/11 and Theorems 8/12; Kayal–Nair–Saha author-hosted 30-page manuscript, Definition 6, Lemma 12 and its complete Appendix B proof, manuscript pp.7,9,21; primary URLs and limited reading scopes below. Reuse L030's assessed graph/rank inputs.
COMPARISON: Known all-field roABP lower-direction results cover weighted paths and cancellation; their converse is unnecessary. They do not identify L031's root, translate L085 scalar terminals/explicit encoding, or state this proof-relative availability obstruction. Those are the permitted specialization obligations.
GAP: Relate L030's established Boolean cut-matrix rank to the imported prefix evaluation-dimension bound for an L085 graph, retaining arbitrary order and scalar terminals; charge any normalization and compare total explicit bits with L031's actual T. No weighted obstruction has been proved in this literature turn.
REASON: Essential weighted-model coverage is now sufficient for one bounded specialization of the unchanged target; import the known rank mechanism rather than reprove it, and leave the ER/fidelity/encoding reception to the mathematical attempt. No originality is certified.
SCOPE: L030's supplied finite simple graphs on n>=2 originals, fixed Delta>=3 and fixed 0<epsilon<1 external vertex expansion; L031's unchanged genuinely used positive root h=f_G and either derived unit sign; explicit L085 common-order read-once layered affine-F₂ graphs, scalar terminals, all-assignment fidelity, arbitrary cancellation and total encoded size. No arbitrary-order general ABP, different-order sum, implicit matrix, circuit-valued edge, repeated variable or changed ER proof.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes the availability question from deterministic diagrams to weighted affine graphs with cancellation; prior supplier coverage did not assess this lower-bound specialization.

## Main gap, intermediate target and decision test

The main gap remains unrestricted SAT decision/separation. The nearer
representation gap is polynomial faithful common-order value-graph
availability for every supplied ER proof; L085 supplies relations only
once those graphs are supplied. This review preserves the exact TARGET.
The intermediate target is a superpolynomial-in-actual-T lower bound for
just L031's designated faithful root in every order, or a precise failure
of the proposed cut-rank mechanism in that model.

A successful specialization would test universality of this restricted
supplier, without addressing alternative nonfaithful data, other ER
proofs, general affine ABPs, optimal certificates, formula-length-only
bounds or unrestricted SAT. L031's opposing-unit originals still have
an immediate refutation and a three-node certificate.

The sought quantitative threshold is L030's existing 2^(c n), with
c=epsilon/(16*Delta*(Delta+1)), charged to a width/size measure of the
weighted graph and hence beyond every polynomial in L031's actual
T=O_Delta(n log(n+2)). These are a proposed receiving bound and an
already established input length respectively, not a new conclusion.
Continue if the weighted model admits the cited prefix-dimension
comparison with correctly charged terminals and no lost order quantifier.
Abandon this mechanism if a polynomial graph for this same faithful
root appears or the required rank/receiving comparison fails; preserve
the exact failure. A bad single order, ordinary OBDD lower bound,
distinct residual count or finite numerical test is insufficient.

## Local inputs and recorded failures inspected

Read complete L030, including its independently audited induced matching,
exact disjointness submatrix and equations (3)–(5). Its proof already
establishes rank_F₂ M>=2^(c n) at the half-prefix cut of every order;
its stated deterministic-sum conclusion must not be quoted as a weighted
conclusion. Reuse its graph/rank sources under the unchanged hypotheses,
through `drafts/literature/2026-10-06-expander-parity-obdd-total-width.md`.
No new graph selection/existence theorem or reproof is needed.

Read L031's construction and complete encoding/ancestry audit. The
original-variable set is exactly the n graph vertices. The positive h
has value f_G on every assignment, even when the ancestry uses NOT h.
There are 4m extensions; with R_*=22m+n+2 and
L=ceil(log₂(R_*+2)), its recorded bound is
T<=128(R_*+n+3)L. Fixed Delta and 2m<=Delta*n yield its stated asymptotic
bound. Do not restrict assignments to models of the contradictory CNF
or silently replace the positive root by its complement.

Read L085's exact hypotheses/conclusion and retain scalar F₂ terminal
values, parallel edges, zero labels, missing paths, cancellation, one
original per level, independently encoded graphs and complete dictionaries.
No availability bound in T is a premise of L085. Its audited supplier
identities are not being reaudited here; only its receiving value model
is relevant. Reuse step 328's same-day verification of the official Clay
statement and Cook description in the weighted-supplier assessment;
this restricted availability target does not change the main problem.

Attempts 019/020/029 were read. They stop respectively universal
deterministic OBDD width, degree-only identical-output circuit-to-ABP
conversion, and the unsimplified counted-path sets/trees. They neither
prove this weighted obstruction nor ban the present independently
testable target. L051's diagonal-entry assessment was also checked as a
nearby duplicate: its FSTW hard polynomial is inside arbitrary supplied
valid certificates, not L031's unchanged all-assignment extension value.
No cross-notebook input is used; all unfinished work is preserved.

## Primary sources actually inspected

**Weighted lower-bound mechanism.** Michael Forbes, Amir Shpilka, Iddo
Tzameret and Avi Wigderson, *Proof Complexity Lower Bounds from Algebraic
Circuit Complexity*, Theory of Computing 17(10), 2021,
[journal PDF](https://toc.cs.uchicago.edu/articles/v017a010/v017a010.pdf),
§§3.2–3.3, Lemmas 3.4–3.7/3.11, printed pp.19–20. The matrix-product
normal form and coefficient-dimension characterization allow arbitrary
fields. The evaluation-space inclusion in Lemma 3.11 needs no field-size
hypothesis; its equality clause assumes |S|>ideg f. Use only the lower
direction/inclusion, so no large-field interpolation is required. The
journal states these supporting facts and points to Forbes's thesis for
full proofs; the primary lower-direction proof below was read instead.
Do not import the characteristic-restricted functional lower bound of
Proposition 5.8 or Corollary 6.22's different hard polynomial here.

**Primary proof of the needed direction.** Neeraj Kayal, Vineet Nair and
Chandan Saha, *Separation between Read-once Oblivious Algebraic Branching
Programs (ROABPs) and Multilinear Depth Three Circuits*,
[author-hosted 30-page manuscript](https://www.csa.iisc.ac.in/~chandan/research/multd3_and_ROABP.pdf),
dated 22 September 2015, retrieved 2026-10-18, Definition 6 p.7,
Lemma 12 p.9 and its entire Appendix B proof p.21 (PDF pages 8,10,22).
The proof chooses the first i variables in the program's actual order;
a prefix evaluation becomes a scalar row, and every residual is in the
span of the same k suffix entries. It assumes neither determinism,
positivity nor an infinite field. This identifies the relevant prefix,
not merely an unspecified subset. The main expander separation's
statement/construction overview, pp.4–6, was checked as a stronger-result
lead: its polynomial is a sum of matching products, not this Boolean
independent-set indicator. Its full lower-bound proof is not imported.

**Independent statement check, with qualification.** Robert Andrews,
Jules Armand, Prateek Dwivedi, Magnus Rahbek Dalgaard Hansen, Nutan Limaye,
Srikanth Srinivasan and Sébastien Tavenas, *On Closure Properties of Read-Once Oblivious Algebraic Branching
Programs*, ITCS 2026, article 9,
[published text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.9/LIPIcs.ITCS.2026.9.html),
§2.1, Definitions 5–7/11 and Theorems 8/12. The lower direction of
Theorem 12 is the relevant evaluation-dimension statement. Its stated
converse invokes an infinite field and is unnecessary here; no converse
or single-cut equality is used. Theorem 8's maximum-over-prefix
coefficient-rank statement is a cross-check only. The primary proof
above removes dependence on a converse or a large-field equivalence.

Searches included `read once oblivious algebraic branching programs
evaluation dimension rank Nisan coefficient matrix any field`,
`weighted OBDD rank finite field lower bound independent set`,
`independent set algebraic branching expander`, `read-once graph CNF
parity lower bound`, and `expander roABP multilinear depth three`.
Snippets were used to locate sources, not as theorem evidence. The MIT
thesis landing page was accessible but its download link returned an
internal error; it is an unread lead, not an essential blocker because
the necessary primary proof above is accessible. An attempted STACS PDF
URL and one screenshot also failed; neither is relied on. Search failure
does not establish novelty.

## Approved next mathematical scope

SPECIALIZE approves one attempt at the unchanged TARGET. It does not
assert that the following reception obligations have been discharged:

1. Pass the supplied ordered free-algebra value graph to the source's
   commutative scalar-polynomial setting without changing its Boolean
   evaluations, actual order, affine labels or fidelity domain. Show how
   arbitrary terminal scalars, parallel edges and nonuniform layer sizes
   fit its matrix-product receiving model. Charge any completion/padding;
   do not lose an exponential bound through uncharged normalization.
2. Connect the Boolean truth-table cut rank already proved inside L030
   to the appropriate residual-polynomial dimension. State the direction
   of the evaluation map explicitly; neither Boolean agreement of general
   polynomials nor distinct residuals gives formal independence by itself.
   Cite the known weighted lower direction, rather than reprove it.
3. Account for every explicit cut state or use the imported maximum-width
   bound with a justified normalization cost, then obtain a bound on the
   supplied root's total vertex/edge/bit encoding. Retain unreachable
   records and cancellations; never require semantic zero testing or path
   unfolding. Missing paths cannot simply be discarded by semantic tests.
4. Receive that root in both L031 sign choices and compare the resulting
   bound with its unchanged full T, for each fixed polynomial exponent
   along a supplied unbounded family with fixed epsilon,Delta. State the
   graph hypotheses conditionally; no uniform expander finder is supplied.

A direct application needs only these model and encoding differences;
no reproof of disjointness rank, expander selection or roABP
characterization is justified. If successful, expected classification
is REPRODUCTION, with the known sources and the local specialization
distinguished. Full matching Mathlib coverage and supporting theorem
names are not checked; unknown coverage is not absence.

This literature-only step writes no lemma or mathematical script,
derives no weighted lower bound, and changes neither PROOF.md nor DAG.md.
The unchanged exact target is now ready for a separate mathematical
attempt; no further literature is required absent changed scope/evidence.
