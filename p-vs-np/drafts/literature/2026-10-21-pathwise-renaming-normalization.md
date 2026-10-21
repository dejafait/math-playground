# Pathwise renaming normalization: source comparison

TARGET: Assess known bounds and obstructions for L101's exact request normalization when only the number of renaming lines on each backward ancestry path is at most floor(log₂ Q), with Q fixed before normalization.
CHECKED: 2026-10-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 397 searched Frege substitution depth, nesting, logarithmic renaming, bounded substitutions and DAG substitution elimination; inspected Finger's author manuscript §2 Lemma 3 and reused step-393/395 component coverage. No inspected result settles the exact pathwise request bound; no novelty or absence claim follows.
SOURCE_EVIDENCE: Finger, DAG Sequent Proofs with a Substitution Rule, author-hosted 16-page Fin05.pdf, size conventions pp.2–3, §2 definitions pp.4–6 and Lemma 3 with complete proof sketch p.7; reopened Pudlák, The Lengths of Proofs (1998), Theorem 8.1.10 with proof pp.593–594; reuse saved Buss/LTW theorem comparisons below.
COMPARISON: L101 counts total renaming lines, whereas the proposed promise counts them per source-reference path. Finger's exponential elimination upper bound and Pudlák's prefix-replay warning provide mechanisms to compare, not a depth-parameterized bound or an admissible lower-bound family. L099's written diamond family traverses all n renamings on a backward path and does not meet the proposed cutoff for large n.
GAP: Bound actual request/cache/materialization cost polynomially in original Q under the pathwise promise, or exhibit an admissible family with superpolynomial requests/materialized records; no such result is established by this review.
REASON: Essential source and local-failure comparison is adequate for one separate bounded mathematical test of this exact implementation; the changed parameter remains unproved rather than source-blocked.
SCOPE: L101's unchanged request initialization, closure, subset cache and ordinary-record materialization; only the global renaming-count hypothesis is replaced by the stated pathwise cutoff, including unused starting lines.
COVERED_TARGET: Test L101's unchanged request normalization under the original pathwise floor(log₂ Q) renaming cutoff: prove a uniform polynomial full-bit/time bound or give an explicit admissible family forcing superpolynomial requests/materialized records.
LITERATURE_REASON: The pathwise cutoff changes the previously assessed global-count hypothesis; this is its first discovery and theorem-level comparison.

The initial proposal was saved in step 396 with REVIEW_REQUIRED. Step 397
completes its literature comparison only. EXPLORE covers the separate
test above; it neither proves its conclusion nor certifies originality.
The newly completed continuation assessment remains subject to the
supervisor's separate next-turn approval.

Keep the L101 source syntax, assumption-free schemes/MP/ground constants,
explicit variable-to-variable maps, all proof/map variables in Var(F),
and original Q=2+M+|F|+|π|. Count renaming lines on backward paths in
the given source-reference DAG, including paths starting from unused
lines. The proposed change removes only the global bound on the total
number of renaming lines. Receive exactly the request initialization,
closure, subset cache and ordinary-record materialization specified in
L101; do not silently change its output or cache semantics.

The main gap remains unrestricted SAT decision/separation. A polynomial
normalization bound for this larger supplied-proof class would feed the
same audited L098 exact-fg receiver without another occurrence-map
construction. A counterexample to this exact normalization would instead
give a concrete reason to seek a different method. Neither outcome alone
settles availability of short proofs, alternative normalization, an M-only
bound, universal W₂, arbitrary ER data or SAT.

The completed comparison below checks standard bounded-substitution and
renaming terminology against primary hypotheses and the relevant
L099/Attempt 032 ranges. L100/Attempt 033 remains an isolated-output
comparison, not a normalization lower bound. Preserve all three stops.

The discriminating future test is a uniform polynomial full-bit/time
bound for this fixed implementation in original Q, or an explicit
admissible family forcing superpolynomial requests/materialized records
under its cache rule. It must count actual requests, aliases and written
data, not infer cost from an unused context universe. A literal-copy
failure would not lower-bound all ordinary proofs or all witnesses.
This test is covered for separate mathematical work; no part of its
mathematical conclusion is derived here.

Essential inputs for coverage are L101's step-396 audit, L098's checked
receiver interface and L087's unchanged pair/B/M. L099 is a targeted
failure comparison, not an assumed input to a new theorem. No
cross-notebook result is proposed. Full matching Mathlib coverage remains
not checked. No lemma or mathematical script is written in this turn.

## Inspected sources and exact comparison

**New primary near-match.** Marcelo Finger, *DAG Sequent Proofs with a
Substitution Rule*, [author-hosted manuscript](https://www.ime.usp.br/~mfinger/home/papers/conf/Fin05.pdf),
16 pages, filename Fin05.pdf (revision date unestablished), accessed
2026-10-21. Read the conventions, definitions and complete Lemma 3 sketch
at the pages recorded above. Formula-valued substitutions permit reuse;
ordinary rules focus. The exponential upper bound concerns **line count**;
the sketch also discusses symbol growth through prefix duplication.
There is no depth/fan-out parameter, cache analysis or lower bound.
These model differences prevent direct application to L101. Theorem 4
and its p.9 qualification retain substitution and were checked only as a
contrast. No bound is imported; branching/reuse is a diagnostic for the
future test.

**Reopened standard comparison.** Pavel Pudlák, *The Lengths of Proofs*,
in *Handbook of Proof Theory* (1998),
[author-hosted chapter](https://users.math.cas.cz/~pudlak/length.pdf),
Definitions 8.1.3–8.1.6 pp.591–592, Theorem 8.1.10 and proof pp.593–594.
The saved step-385 reading is reused; this turn reopened the theorem
and full proof, including axiom, MP and substitution cases. SF and EF
are polynomially equivalent; the SF-to-EF proof introduces fresh
extension variables. Its naive prefix-replay discussion warns of
exponential growth. It supplies neither ordinary-Frege normalization
for the pathwise class nor a request-cache lower bound. No reproof or
new consequence of SF/EF equivalence is needed.

**Ready component coverage reused.** The step-393 assessment
`2026-10-20-logarithmic-renaming-source-supplier.md` and step-395
`2026-10-21-logarithmic-renaming-supplier-critical-audit.md` retain the
inspected hypotheses and qualifications of these precise sources:

- Samuel R. Buss, *Some Remarks on Lengths of Propositional Proofs*,
  [July 3, 2002 manuscript](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/proplengths/paper.pdf),
  §8 Theorem 15, Corollary 16 and Lemma 17, pp.22–24: renaming can
  identify variables, and the simulation of assumption-free SF/EF
  outputs renaming proofs, not ordinary proofs with this cache bound.
  Today's fetch timed out; the prior inspected comparison is adequate
  and is reused rather than reported as a fresh reading or blocker.
- Fu Li, Iddo Tzameret and Zhengyu Wang, *Characterizing Propositional
  Proofs as Non-Commutative Formulas*, SIAM J. Comput. 47(4) (2018),
  1424–1462, [40-page author revision](https://www.doc.ic.ac.uk/~itzamere/Ideal_non-commutative.pdf),
  Definition 1.3 p.6, Theorem 3.1/Lemma 3.3 pp.13–14. Its ordinary
  extraction has no renaming case. L098 receives the corrected generic
  extraction and constant seeds; applying it after normalization avoids
  rederiving any algebraic renaming case. Revision date remains unknown.
- Chubaryan–Chubaryan–Nalbandyan, *Comparison of the Efficiency of Frege
  Systems with Restricted Substitution Rules*,
  [CSIT 2009 note](https://csit.am/2009/proceedings/1AAL/5.pdf), §§2–3
  pp.1–2: its depth parameter concerns substitution **images**. It is
  not the number of renaming nodes on a proof-reference path.

These are comparisons and component citations, not a full-statement
import of the proposed pathwise theorem. L101's normalization itself
needs no additional algebraic extraction theorem. No source claims that
a bound on this proof class supplies short proofs for all source CNFs.

## Local duplicates, failures and admissibility

Read L101 §§1–2 and the corresponding step-396 audit items 1–2: requests
start at **every** (i,∅), MP preserves the subset, renaming inserts its
own source index, and different subsets remain separate even if their
actions coincide. Renaming requests store resolved ordinary-line aliases;
axiom/MP requests write actual records. Its N·2^r estimate counts the
global set R and cannot be invoked with a different meaning of r.

Read L099 §2's four-line diamonds and final attachment, §3's request
description and §5's original-Q ledger, plus Attempt 032. In that
recorded family the backward chain through R_n, R_(n−1), …, R_1 visits
all n renaming lines. The existing Q_n≤C(n+2)³ ledger makes that chain
longer than floor(log₂ Q_n) eventually. Thus the existing exponential
family does **not** establish failure inside the changed promise. No
new family or amplification of it is constructed in this literature
turn. The old all-context result also concerns whole-seed extraction;
an exact-normalization lower bound must count L101's own requests and
written records, including aliases, rather than citing that result alone.

Attempt 033 obstructs only a selected isolated initial-seed aggregate;
later seeds can cancel it in the full output. Attempt 020 obstructs a
general same-output degree-only conversion. Neither settles pathwise
ordinary-proof normalization. L098's hypotheses/conclusion were checked
for the downstream interface; L087's hypotheses fix fg, B and M. Their
full proofs need no repetition in a source-only step. PROOF.md and DAG.md
are unchanged because the mathematical argument has not changed.

## Search record, decision and bounded continuation

Queries actually issued: `Frege renaming substitution depth logarithmic
proof simulation bounded substitution nesting`; `Buss Some Remarks
Lengths Propositional Proofs renaming theorem 15`; `"Frege"
"substitution depth"`; `"Frege" "renaming" "path"`; `"Frege"
"bounded" "substitutions" proof`; `"Frege" "substitution" "nesting"`;
`"renaming" "Frege" "logarithmic"`; `"DAG Sequents with Substitution"
pdf`. Finger's primary manuscript was followed from discovery to its
definitions and relevant elimination proof. General bounded-depth Frege
hits concern formula depth and were not promoted to this path parameter.
Secondary discussions of renaming power and a single-renaming claim
remain unread primary-theorem leads, not essential inputs or coverage.
This bounded search establishes no originality or global nonexistence.

After separate continuation approval, perform exactly COVERED_TARGET.
Save the proposed request invariant or candidate family before lengthy
work. In a positive attempt, charge actual requests, subset keys, maps,
formulas, instantiation records, resolved aliases, ordinary references
and bit time in original Q. In a negative attempt, exhibit actual legal
source proofs, the pathwise promise including unused starts, full input
encoding, and superpolynomial **realized** requests or written records.
Branching at a renaming layer is a diagnostic to test, not a result
proved here. An unused universe of subsets, an unverified preview or
failure of an isolated arithmetic output is insufficient evidence.

Continue only with the uniform polynomial bound or an explicit
admissible obstruction to this implementation. If the obstruction is
proved, abandon this normalization for the pathwise promise while
retaining the global L101 theorem; do not infer hardness of all ordinary
proofs or all witnesses. If neither closes in the bounded attempt,
record the precise unresolved count and reassess under the shared
exploration limits. Short-proof availability, an M-only bound, general
normalization, universal W₂, arbitrary ER data and unrestricted SAT
remain independent gaps. No new mathematical result is claimed here;
outcome EXPLORATION records a new source comparison and actionable test,
with zero mathematical exploration turns spent.
