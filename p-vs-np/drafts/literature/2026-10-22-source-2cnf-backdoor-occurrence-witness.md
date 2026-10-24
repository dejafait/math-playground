# Supplied source backdoor to 2-CNF: completed source comparison

TARGET: Assess whether a supplied k-variable strong backdoor to 2-CNF yields L087's exact-fg witness with full size and deterministic bit time 2^{O(k)}Q^{O(1)} in original Q=2+M+|F|+|backdoor|.
CHECKED: 2026-10-22
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 410 searched strong backdoors/2-CNF (Krom), constructive resolution refutations, restriction lifting/deduction and stronger proof-size results; inspected the primary passages below and narrowly checked source assessments, L087/L097 and Attempts 030–035. The branch/lift/combine mechanism is already published; no novelty inference is made.
SOURCE_EVIDENCE: Nishimura–Ragde–Szeider, SAT 2004 proceedings PDF https://www.satisfiability.org/SAT04/programme/51.pdf pp.98,100–101, definitions/Theorems 3–4/Lemma 2; Buresh-Oppenheim–Mitchell, 14-page author PDF https://www.cs.sfu.ca/~mitchell/papers/sat07-2res.pdf §2 pp.2–3, Proposition 1 and IR(P); Lauria–Nordström, April 7 2015 full version https://www.massimolauria.net/documents/sizesos.pdf §2 pp.6–7, resolution definition/Fact 2.5; Järvisalo–Matsliah–Nordström–Živný, 17-page author PDF https://people.csail.mit.edu/jakobn/research/RelatingProofCplxHardnessSAT.pdf §6 Theorem 2(1)/proof pp.13–14. Audited L097 coverage is reused.
COMPARISON: Known sources supply clause-labelled 2-CNF resolution derivations and the backdoor restriction-lifting/assignment-combination mechanism, beyond a SAT decision algorithm. They do not state L087's occurrence-specific full-bit/time export. L104 and L096 have different supplied promises; no domination or separating example is established here.
GAP: The remaining specialization is original-clause list/set/provenance reception and a common fixed-exponent original-Q ledger for the complete ordinary-resolution archive and L097 composition; no such specialization is proved in this turn.
REASON: Essential source coverage is now available for a separate REPRODUCTION attempt, importing the general operations and proving only the exact-source reception and encoding/composition obligations. No new lemma or mathematical script is written in this literature-only turn.
SCOPE: Original explicit unsatisfiable width-at-most-three F, its exact L087 occurrence pair/provenance/B/M and a supplied k-element subset of occurring source variables whose every ordinary restriction is 2-CNF; no propagation-defined or weak backdoor, no extension axioms, and Q fixed before generated records.

Supply the original explicit unsatisfiable width-at-most-three F, exactly
its L087 occurrence pair/provenance/B/M, and an explicit set S of k
distinct variables occurring in F. A strong backdoor here means that
for every total assignment to S, the source restriction is a CNF of
width at most two. The literature comparison must fix the restriction
convention, including satisfied/tautological clauses, repeated literals,
empty clauses and original-clause associations. Do not silently use a
solver's additional propagation or a weak (some-assignment) backdoor.
All supplied records enter Q before any branch or proof is generated.

Main gap remains unrestricted SAT decision/separation. The prospective
intermediate target would supply exact occurrence witnesses under a
different structural promise, possibly where L104's source-width premise
is unavailable. No claim of such a separating example is made here.
Essential prospective local inputs are L087 and audited L097; L104 and
L096 are comparisons, not assumed proofs of this proposed supplier.

## Inspected primary inputs and qualifications

**Backdoor syntax.** Naomi Nishimura, Prabhakar Ragde and Stefan Szeider,
*Detecting Backdoor Sets with Respect to Horn and Binary Clauses*, SAT
2004 proceedings copy, printed pp.96–103; use §2 p.98, §4 Theorems 3–4
pp.100–101 and Lemma 2 p.101 at the direct URL above. Its clauses are
nontautological literal sets, binary means at most two literals, and
restriction removes satisfied clauses and false literals, without unit
propagation. Strong quantifies over every assignment; weak additionally
requires a satisfying restriction. Lemma 2 identifies the strong promise
with membership after deleting both signs of the backdoor variables.
Theorem 3 already finds a strong 2-CNF backdoor in O(3^k N), or reports
nonexistence; Theorem 4 uses all assignments for SAT decision. Read the
branching argument, not just the statements. These are stronger search
inputs than this supplied-set target needs. N counts literal occurrences,
not complete binary records. Source normalization conventions therefore
need explicit reception; its set characterization must not be applied
verbatim to a raw list containing tautologies. No finder is needed here.

**Constructive branch proofs.** Joshua Buresh-Oppenheim and David G.
Mitchell, *Minimum 2CNF Resolution Refutations in Polynomial Time*, SAT
2007, LNCS 4501, pp.300–313; use the 14-page author copy, §2 PDF pp.2–3,
Proposition 1 and the paragraph defining IR(P). The author-page link
identifies this as the SAT-2007 paper; a revision date is not established.
Proposition 1 is the contradictory implication-path criterion. Every
edge carries its actual input-clause label; equal literals are permitted,
covering unit clauses. The IR(P) paragraph constructs successive input
resolutions along a path, deriving the endpoint clause or its stronger
unit, and states size 2 length(P)−1. These explicit operations, rather
than SAT decision alone, are the needed import. Empty clauses require
direct reception outside the graph criterion. Its introduction claims
the stronger minimum-refutation algorithm, with O(n^6 m) time. The later
optimization proof was not inspected and is not imported; shortest-proof
optimality is unnecessary. The elementary labelled-path construction is
already adequate coverage for the prospective branch export.

**Restriction lifting in the receiving system.** Massimo Lauria and
Jakob Nordström, *Tight Size-Degree Bounds for Sums-of-Squares Proofs*,
April 7, 2015 full-length CCC'15 version, §2 printed pp.6–7. Despite the
paper's title, the cited passage is ordinary resolution: clauses may be
axioms, weakenings of earlier clauses, or binary resolvents; size counts
all clause records with repetitions. Fact 2.5 states: if a partial
assignment ρ sets ℓ variables and A is the width-ℓ clause falsified by
ρ, then a width-w, size-S derivation of C from F restricted by ρ gives
a derivation of A∨C from F of width at most w+ℓ and size at most S+1.
The source calls this forward induction and omits its proof. Import the
fact, without treating its clause count as a full binary implementation
bound. L097 explicitly admits weakening. The next specialization must
write actual leaf/inference records and may use a looser polynomial
archive bound; such detail justifies the receiving conventions, not a
reproof of the general restriction theorem.

**The backdoor combination already appears in the literature.** Matti
Järvisalo, Arie Matsliah, Jakob Nordström and Stanislav Živný,
*Relating Proof Complexity Measures and Practical Hardness of SAT*,
CP 2012, LNCS 7514, pp.316–331. Use the 17-page author version at the
direct URL above, §2 pp.4–5 and §6 Theorem 2(1) with its full proof,
pp.13–14; its revision date is not established. The theorem gives clause
space b+O(1) from a size-b 2-CNF backdoor to an unsatisfiable formula.
Its proof explicitly lifts restricted refutations, refutes all total-
assignment blocking clauses in tree-like length 2^{b+1}, and calls each
branch derivation once. Its subsolver definition includes 2-SAT and is
broader than the syntactic promise here. The space statement alone is
not a construction-time bound; use the displayed composition mechanism
with the separately inspected branch proof input. The informal wording
“unique minimal clause” is not used as a definition: Fact 2.5 fixes the
intended full-width blocking clause precisely. No space theorem is
being converted into an unproved short-proof finder.

## Exact comparison and remaining work

Searches included `strong backdoor 2CNF resolution proof size refutation
restriction lifting`, `2 CNF unsatisfiable resolution refutation
polynomial implication graph proof`, `resolution deduction theorem
restriction refutation`, and `backdoor 2-CNF resolution proof size`.
Searches of exact titles located the author/proceedings copies above.
Search snippets and third-party summaries were discovery leads only.
The read-once/copy-complexity paper arXiv:1610.04523 was opened as a
stronger lead; no theorem or proof case from it is imported. None of the
essential inputs is source-blocked. One optional shell download failed
DNS; browser extraction of the primary manuscripts supplied the cited
passages, so no local PDF archive or hash is claimed.

The narrow local reads were L087's hypotheses and occurrence construction;
L097's hypotheses, source/list interface and (11)–(12); and L104's source
normalization and step-409 reception audit. L104's bag conversion/DR
proof and L096's small-core mechanism are comparisons, not assumptions
for the new target. Attempts 030–031 stop universal restricted-value or
partition availability. Attempts 032–035 stop specified renaming-copy
normalizations. The proposed source-backdoor construction uses none of
those failed universal premises or renaming procedures. No local exact
backdoor supplier was located in the targeted source assessments.

The reviewed sources support a plausible common C2^{ck}Q^a threshold,
with absolute constants: their operations are explicitly finite branch
construction, ordinary-resolution lifting and assignment combination,
and L097 has fixed exponents. This is coverage approval, **not** a
derivation of that combined bound. The separate research step must
justify the following actual-source interface and complete ledger:

- Keep original F and every original occurrence name, order, fg, B and
  M. Normalize only an auxiliary literal-set view, retaining original
  clause/literal positions and all unused source/backdoor records.
- State the restriction convention before using the backdoor promise.
  Receive empty clauses, unit clauses, repeated literals/clauses,
  tautologies, zero remaining variables, k=0 and early branch closure.
  Label every branch axiom by its actual unsatisfied source clause.
- Export a complete ordinary-resolution archive with actual earlier
  references, paid weakening and original-clause associations. Do not
  substitute restricted leaves for original axioms without lifting.
- Fix Q before every proof/witness. Pay branch counts, all written
  literals and binary names, all generated/global references, all
  retained records and dictionaries, then L097's full polynomial.
  A Q exponent depending on k fails the target.

Continue with the [separate ready specialization](2026-10-22-source-2cnf-backdoor-specialization.md).
Abandon or narrow if the export needs extension axioms, loses original
leaf provenance/fg/B, or cannot meet a common C2^{ck}Q^a size **and** bit
time bound. No separating example versus L104 is asserted. Small
backdoors, general short proofs, M-only bounds, universal W₂, arbitrary
ER data and unrestricted SAT transfer remain unresolved. Mathlib matching
coverage is not checked. No lemma, calculation or mathematical script
was produced in this source review.

The Clay page was reconfirmed on 2026-10-22 and still links Stephen
Cook's official *The P versus NP Problem*, §1 pp.1–2,
https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf. Its exact
question remains equality of deterministic polynomial-time languages
with polynomial-time verifiable languages, as in foundations/01. This
restricted supplier would not answer it; prize adjudication is separate.
