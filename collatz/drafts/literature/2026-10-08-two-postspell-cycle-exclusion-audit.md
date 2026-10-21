# Approved critical-audit coverage for the two-postspell exclusion

TARGET: Critically audit L040's two-postspell cycle exclusion, including L039's ceiling, primitive counts, published source qualifications and L031's closure implication.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the four focused queries and primary comparison in 2026-10-08-two-postspell-cycle-length-comparison.md; read complete L040/L031, L035's period application, L039's scope, the total-length assessment/audit, finite-coding source records, histories 069/089/091 and Attempt 019; no external search repeated.
SOURCE_EVIDENCE: Reused inspected Simons–de Weger, Acta Arith. 117 (2005), sections 1.1–1.3 pp. 51–53, Lemma 1 and Corollary 2 with complete proof; inherited Lemmas 8/12 pp. 59/61, Hercher Theorem 16 pp. 10–11 and 2026 corrigendum; Bernstein–Lagarias author manuscript 19960215 section 1 pp. 1–3 and Sodelin sections 2–3 with qualifications below.
COMPARISON: Recorded primary coverage matches the positive nontrivial shortcut-cycle and finite-word hypotheses; the general odd-count theorem needs only local period/count specialization, while the two-word ceiling and closure bridge require a later independent audit rather than a source theorem reproof.
GAP: Audit the complete load-bearing local argument, primitive scaling, inherited ceiling and closure implication; this review approves scope but does not verify L040 or repair a mathematical claim.
REASON: No changed essential hypothesis or missing essential source remains; ready coverage suffices for one RESEARCH/REPRODUCTION audit of the exact saved target.
SCOPE: Exactly L040 with integer J_i>=2,H_i>=3,a_i>=0 congruent to 2 modulo 18, actual positive closed W_1W_2, positive odd residue-20 n,x,n>1, independent exact tails, repetitions and x=n; include its all-parameter arithmetic conclusion via L031 without least-root, tail-cap, primitive-word or global-minimum assumptions.
LITERATURE_REASON: The newly saved critical-audit continuation was REVIEW_REQUIRED; this separate literature-only step compares its scope with reusable primary coverage, without another source search or mathematical audit.

## Reused primary results and qualifications

The length-comparison assessment records the exact queries, source access,
versions and inspected proof cases. John Simons and Benne de Weger,
*Theoretical and computational bounds for m-cycles of the 3n+1-problem*,
[Acta Arithmetica 117 (2005), 51–70](https://www.impan.pl/shop/en/publication/transaction/download/product/82263),
sections 1.1–1.3, printed pp. 51–53, use the shortcut map, K odd
inputs and L even inputs, permitting nonminimal periods. Corollary 2,
p. 53, states K>2.2564*10^8. Its complete recorded proof invokes
Lemma 1, xmin>301*2^50, and continued-fraction denominators
q_18=225644606 and q_19=397573379. The distributed computation [Ro]
and Roosendaal personal-communication footnote remain qualifications
of the imported published result. No independent computation is claimed.
There is no fixed-m restriction on this corollary. Stronger modern
bounds are unnecessary. Crandall's inaccessible original and Eliahou's
abstract remain unread leads, not extra inputs or blockers to this import.

Inherited coverage is recorded in
`drafts/literature/2026-10-08-two-postspell-total-length-audit.md`
and the total-length-bound assessment: Simons–de Weger Lemma 8 and
proof, p. 59, Lemma 12 and complete proof, p. 61, and period convention,
p. 52; Christian Hercher, *There are no Collatz m-Cycles with m <= 91*,
[JIS 26 (2023), Article 23.3.5](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
Theorem 16 and complete proof, pp. 10–11. Rhin and published source
computations remain imports. The full two-page
[2026 corrigendum](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf)
was inspected in the length comparison; it concerns Theorem 21, not
Theorem 16. Its replacement proof is not independently certified here.
L035 uses L034's occurrence/return argument, not its Theorem 23 cutoff.
Do not silently promote that non-load-bearing cutoff to an exclusion input.

L031's finite coding is covered by the existing initial-size and
extendible-inverse assessments. Bernstein–Lagarias,
[*The 3x+1 Conjugacy Map*, author manuscript 15 February 1996](https://websites.umich.edu/~lagarias/doc/bernstein.pdf),
section 1, pp. 1–3, equations (1.3)–(1.6), the uniqueness argument
following (1.4) and reduction-modulo-powers-of-two permutation statement
were inspected there. This is finite parity coding for the same shortcut
map; the Periodicity Conjecture is unproved and not imported. The local
identification of the coded residue class with the affine integrality
class must still be audited. L020/L021's single-word affine inputs reuse
Sodelin, node AC-POSTSPELL-GUARDED-ROOT-DESCENT-001,
[Postspell_Guarded_Root_Descent.md, sections 2–3](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md),
live main inspected 2026-10-04 without an immutable revision or checked
Lean build. The sharp-halving and two-word assessments retain its proof
coverage. No new general coding or affine theorem needs reproof.

These are reused source records, not newly retrieved primary passages.
No failed search establishes novelty. Full matching and supporting
Mathlib coverage remains not checked.

## Relevance, duplicates and bounded audit obligations

The main gap is universal eventual descent. The single intermediate
target is a reliable critical audit of the restricted cycle exclusion.
A successful audit would retain an exclusion of this periodic obstruction
and its positive integer divisibility formulation. Universal entry into
this language, other cycles, divergence and descent remain independent
gaps; there is no complete Collatz candidate.

L039's existing audit (history 089 and its canonical audit) covers the
ceiling, not L040's new assembly. L035's prior audit checks odd-occurrence
accounting and repeated-period mass scaling. L031's closure implication
needs attention in this new audit even though its finite machinery is
covered. History 091 records the new local exclusion, not a prior completed
audit. Attempt 019's guard-only failure and history 069's full-minimum
mismatch remain preserved: this audit does not retry either mechanism.

Essential inputs are L040, L039, L035 and L031; inherited L036/L038/L037
and L020/L021/L034 are inspected only as needed for load-bearing details.
Read complete relevant proofs, not certificate previews. Check all allowed
parameters, both independent exact tails, positive odd residue-20 n,x,
n>1, actual closure, repeated periods and x=n. Distinguish primitive
odd count K_0, represented odd count K and total represented shortcut
count N. Check nontriviality and source m-cycle applicability without
identifying either junction with a global minimum. Audit the exact
threshold contradiction and L031's sufficient direction, including
positive integral C, Delta>0, divisibility, finite parity coding,
residue membership and exact tail guards. L039's elementary inequalities
and inherited scope must remain justified; earlier no-defect findings
are reusable records, not substitutes for essential proof inspection.

Continuation/abandonment test: retain L040 only if every load-bearing
step and imported applicability condition survives this exact scope.
A precise defect requires a covered repair, narrowed claim or withdrawal
of the affected conclusion; changed essential scope requires separate
review. Source computations remain imported and are not recertified.
Do not impose a tail cap, least root, primitive word, distinct junctions,
or replace full counts by two long tails. No new mathematical result is
approved by this literature-only step beyond permission to perform the audit.

This turn is conservatively STALLED, LITERATURE/NOVELTY_UNCHECKED:
separate scope approval reuses adequate evidence without new source
information, repair, theorem application or audit verdict. No lemmas,
mathematical scripts, PROOF.md or DAG.md were modified. Mathematical
exploration usage remains zero and no counter reset is claimed. The
unchanged TARGET is ready for one later RESEARCH/REPRODUCTION proof audit.
