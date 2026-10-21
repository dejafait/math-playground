# L072 criterion audit — source coverage approved

TARGET: Critically audit L072's norm-square unit-exhaustion criterion, including all lift choices and the all-finite-even scope.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed 2026-10-15 even-valuation-unit-exhaustion assessment; compared its inspected theorem scope with the full L072 statement and proof, L033/L069 hypotheses, ATTEMPTS/032 and histories/225–226. No new external search was needed for the unchanged machinery.
SOURCE_EVIDENCE: Reused inspected primary passages: Lemmermeyer arXiv:1108.5674v1 Sections 2.1–2.2 pp.2–3 https://arxiv.org/pdf/1108.5674v1; Milne ANT v3.08 Proposition 4.1(a),(c) and proof pp.68–69 https://www.jmilne.org/math/CourseNotes/ANTc.pdf; Simon 2002 Propositions 1.3–1.4 pp.8–9 https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8FAFF26D93D01A154C51CF897E4BE6CD/S1461157000000668a.pdf/computing_the_rank_of_elliptic_curves_over_number_fields.pdf; BPT arXiv:2001.02263v3 Lemma 2.14 and Remark 2.15 pp.12–13 https://arxiv.org/pdf/2001.02263v3. Full passage inspection is recorded in drafts/literature/2026-10-15-even-valuation-unit-exhaustion.md; URL repair reuses that coverage.
COMPARISON: These inputs cover the ordinary all-finite-even sequence, nonnormal ideal norms and cubic scalar-unit norm mechanism needed to audit L072. The norm-kernel specialization, choice formulas, extension section and exact norm-one normalization are local application arguments requiring proof audit, not additional general descent theorems or class-group computations.
GAP: Coverage is sufficient for the exact audit target; correctness of L072 remains unaudited, and actual class data, full Kummer containment and downstream rank/integer conclusions remain unresolved.
REASON: Approve one independent critical audit as a specialization/reproduction of the already inspected machinery; this source review does not certify its mathematical conclusion.
LITERATURE_REASON: The supervisor required separate approval of the newly written L072 audit target; the prior ready assessment supplies the essential sources without repeated browsing.
SCOPE: Exactly TARGET for L033's entire K and L069's entire cubic D/K, ordinary maximal rings and all finite primes; includes all L072 equivalences and dimension formula, but no class arithmetic or assertion of full Kummer containment.

## Bounded continuation

Reuse `drafts/literature/2026-10-15-even-valuation-unit-exhaustion.md` for
the inspected primary hypotheses and source versions. This turn completes coverage approval only. The next turn may perform
the independent proof audit using this assessment. No essential mismatch
or new source blocker was found in the source-scope comparison, and no
additional browsing was performed. Approval is of coverage, not of L072.

Essential inputs are L033's entire K and L069's entire cubic D/K, V and
dim V=12, together with L072 and the primary exact-sequence/norm inputs.
No cross-notebook theorem is used. The check must keep ordinary classes,
fractional ideals, every finite prime and the full cubic field. Test the
lift beta=alpha/epsilon and the change alpha -> alpha eta explicitly;
square norm cannot be replaced by exact norm one without the formula
gamma=beta³/b² when N(beta)=b².

Continue if each equivalence and quotient map is justified with precisely
these hypotheses; repair any failed step without inferring a class value.
Unresolved assumptions for downstream descent remain actual class data,
full all-finite-even Kummer containment, further local filtering, rank,
indices/cosets and primitive integer lifting. An audit of this criterion
cannot resolve those assumptions. Mathlib coverage remains not checked.

## Source-to-audit comparison and boundaries

The reused assessment contains the exact source URLs, versions, numbered
statements and relevant proof cases. Lemmermeyer's ordinary ideal-square
sequence includes fractional ideals and every finite prime, without a
positivity condition. It is the matching imported result; Simon's abstract
S-unit splitting supplies supporting context, not a norm-compatible section.
Milne's Proposition 4.1 covers finite separable nonnormal extensions; the
audit must still check L072's passage to fractional ideals and compatibility.
BPT's scalar-unit argument is relevant in degree three; its separate
positivity/class assumptions and global Selmer bounds are not imported.
Simon Proposition 1.4 supplies the essential warning about exceptional
finite support, rather than containment in the all-finite-even space.

The audit must independently check that the map W to the class-norm kernel
is well-defined and onto, its kernel is V, and its quotient is canonical.
It must check the changes of norm-ideal generator, ideal representative
and principal generator; extension of two-torsion classes as a section;
finiteness and the use of L069's dimension twelve; and the displayed exact
norm-one normalization for both field classes and unit classes. Listing
these obligations is not a verification of the identities or a new proof.
The short local application is justified because the inspected sources do
not state this entire field-specific criterion with its choice formulas.

Duplicate/failure comparison: L069 counts units only, and ATTEMPTS/032
stops the unfiltered rank shortcut. L072 adds a conditional class criterion;
its audit neither reopens that shortcut nor repeats an arithmetic search.
Histories/225–226 establish source readiness and the completed derivation,
but neither is a substitute for independent critical review. No unread
source lead is essential to this audit. No novelty or Mathlib absence is
claimed; Mathlib coverage remains not checked.

Outcome: source coverage changes from REVIEW_REQUIRED to SPECIALIZE.
This is local source-review progress only, with no new mathematical result
or progress beyond the checked sources. No lemma, script, PROOF or DAG
change is needed. Continue with the exact saved audit; repair any failed
claim in the later research turn, retaining every independent unresolved
assumption stated above.

## Direct-source metadata repair — 2026-10-15

The supervisor rejected readiness metadata because this assessment lacked
a direct source URL. The SOURCE_EVIDENCE field now carries all four primary
URLs and their existing version/theorem/page locators. The prior inspected
assessment remains the substantive source review. Direct opens reconfirmed
access to the Lemmermeyer, Milne and BPT PDFs; Lemmermeyer's displayed
Sections 2.1–2.2 retain the ordinary ideal-square definition and exact
sequence. Simon's URL and passage evidence are reused from the prior
assessment, without claiming a fresh retrieval. No theorem comparison or
mathematical conclusion changes. SPECIALIZE and the exact TARGET remain
unchanged. This is a STALLED metadata repair, not another source advance
or a proof audit. The independent audit and its continuation test above
remain the next mathematical step; no new assessment is introduced.
