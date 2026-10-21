# Two postspell excursions: completed scope comparison

TARGET: Derive an exact original-root descent criterion for two consecutive actual residue-20 postspell excursions, with the first endpoint above the root and the second below it, and test guarded realizability while retaining all integer and parity guards.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Two changed-scope queries executed on 2026-10-04; reread the closest primary note and supporting finite-word comparison, reusing the prior single-excursion assessment; queries and limits below.
SOURCE_EVIDENCE: Sodelin, Postspell_Guarded_Root_Descent.md, AC-POSTSPELL-GUARDED-ROOT-DESCENT-001, live main read 2026-10-04, sections 1–5; Rozier–Terracol, arXiv:2502.00948v2 (2025-02-13), equations (2), (8)–(9), parity-congruence paragraph before Theorem 2.2 and Lemma 2.3's coding statement; prior companion-obstruction coverage reused.
COMPARISON: Arbitrary finite-word affine arithmetic, full-word parity coding and positive-remainder comparison cover the general machinery; the inspected single-excursion margin does not state the intermediate-overshoot/two-excursion specialization or ensure a second descent is below the unchanged first root.
GAP: The explicit two-excursion inequality and intersection of its overshoot/descent conditions with joint parity and residue guards remain to be calculated; no checked theorem guarantees universal entry into a compensating pair.
REASON: Approve only a bounded specialization of covered arithmetic and its joint guarded applicability test; avoid reproof of finite-word coding and any claim that compensating pairs occur at arbitrary surviving roots.
SCOPE: Positive shortcut root n congruent to 20 modulo 27; two consecutive actual words W_i=(OOEO)^(J_i) O^(H_i) E^(a_i), J_i>=2, H_i>=3, nonnegative a_i congruent to 2 modulo 18; retain every input parity, positivity, integer endpoints and both residue-20 endpoints; compare both endpoints with the unchanged n. No maximality of the last even tail is presumed except where forced by the next actual letter or explicitly imposed.

## Hypotheses

The TARGET is preserved exactly from the saved checkpoint. The main gap
is universal eventual descent on the infinite domain surviving L014–L020.
The intermediate target is a conditional original-root test over two
specified excursions. Its plausible downstream use is an additional
least-root exclusion when a first excursion grows and a later one repays
that growth. Entry, arbitrary failed tails and universal compensation
would remain separate unresolved steps.

This is one LITERATURE step, outcome EXPLORATION. It approves a future
mathematical test without deriving a composed formula, constructing a
witness, or executing a parameter screen. It supplies no mathematical
advance or new obstruction and resets no calculation counter.

## Conclusion

SPECIALIZE is ready for the exact saved action. General arithmetic is
covered; the parameter specialization and a genuinely joint guarded
example still require work. Report that work as REPRODUCTION unless
additional evidence warrants a different qualified classification.
No priority or exhaustive literature-absence claim is made. There is no
essential unread source blocking this bounded test.

## Proof

This section is a source comparison, not a proof of the proposed target.

### Source statements actually read

Sodelin, [*Guarded root descent after independently unbounded return
spells and odd runs*, sections 1–5](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md),
node `AC-POSTSPELL-GUARDED-ROOT-DESCENT-001`, uses the same shortcut map.
Section 1 gives exact guarded orbit identities and a sufficient margin
with final exponent at least J+H. Section 2 proves parity recursion for
an arbitrary finite word and supplies a CRT construction. Section 3
checks residue-20 endpoint membership for its congruent even tail.
Section 4 gives an actual growing residue-20 example with J=2,H=3,a=2
and stresses the unresolved failed-guard boundary. Section 5 distinguishes
prose proofs, finite checks and pending Lean formalization. Read the full
199-line raw note and rendered note on 2026-10-04; no immutable revision
was obtained. These statements support concatenation machinery, but
its one-excursion margin is not a theorem about the saved pair.

Rozier–Terracol, [*Paradoxical behavior in Collatz sequences*,
arXiv:2502.00948v2, 13 February 2025](https://arxiv.org/html/2502.00948v2),
equations (2) and (8), express a shortcut iterate as coefficient times
start plus remainder. Equation (9) characterizes the contracting but
non-descending case. The paragraph before Theorem 2.2 and Lemma 2.3's
proof describe parity classes modulo the corresponding power of two
and realization of every finite vector. These apply to whole finite
words, not only single spells. The paper does not give this specific
two-postspell criterion. Its CST conjecture is not an available theorem.
No density statement removes all exceptional roots.

The prior [single-word assessment](2026-10-04-sharp-postspell-final-halving.md)
remains adequate for the companion odd-run obstruction and remainder
bounds. Those sources need no repeated broad search. The
[MathPrize statement](https://mathprize.net/posts/collatz-conjecture/),
posted 7 July 2021 and reread on 2026-10-04, still asks for convergence of
every positive integer, so a conditional pair remains a partial input.

### Necessary difference and redundancy check

Import finite-word coding and the single-word identities by citation.
The necessary new local work is specialization to the concatenated word,
keeping both positive offsets and strict comparison with the first root.
Separate existence of a growing first word and a contracting second word
does not establish their simultaneous realization by one orbit. Coding
must be applied to the complete concatenation, and the intermediate
endpoint must satisfy the second word's first input parity. If the final
tail of the second word is claimed maximal, impose its following parity
explicitly. Retain exact integer and residue guards throughout.

L020 already supplies a single-word criterion; redoing it alone is
redundant. L019's sufficient margin is relative to that excursion's
input and does not by itself compare a second endpoint with a smaller
original root. L005 concerns complete-block conventions, so is background
rather than an automatic match. L003's bounded-block obstruction prevents
promoting a bounded positive test to universal compensation. The
first-return and bounded-ancestor failures remain preserved; Attempts
009–011 are not reopened. No known obstruction in the checked coverage
prohibits the conditional pair test as stated.

### Bounded next test and decision threshold

For a finite initial applicability screen use 2<=J_i<=12, 3<=H_i<=12
and a_i in {2,20}. On the first word restrict a_1<e(J_1,H_1), where e is
the previously defined least exponent >=J+H congruent to 2 modulo 18;
this focuses the test on the insufficient-tail cases rather than
repeating a known first descent. Keep the second word's selected tail
in the stated screen, whether or not it meets its sufficient threshold.
This is an approved bounded subtest of the unchanged TARGET, not a
parameter computation performed in this review.

The test must intersect full concatenation coding with residue-20
membership and exact root inequalities. An actual positive joint witness
with first endpoint >n and second endpoint <n would justify recording
conditional applicability. A rational composed slope or two unrelated
examples would not. If the screen fails, record its finite scope and
any exact obstruction it reveals; do not enlarge it mechanically or
claim all pairs impossible. A symbolic impossibility for the proposed
guards would stop this particular mechanism. Either result leaves
universal pair entry and control of all remaining roots open.

### Search record and evidence limits

Queries executed on 2026-10-04:

- Collatz "postspell" "two" excursions compensation
- Collatz parity vector concatenation affine composition stopping time original start

No search hit established a full statement matching the saved target.
Trümper's 2014 semigroup paper, Niu's 2026 parity-vector preprint and
other unrelated or unreviewed hits were discovery leads only. They are
nonessential for this specialization because the needed arbitrary-word
coding is directly covered above; no assertion depends on their unread
theorems. Search snippets and informal discussion were not used as
mathematical evidence. This is a narrow changed-scope assessment,
not a claim of exhaustive coverage or novelty.

## Mathlib

Full two-excursion compensation statement and supporting coverage:
**not checked**. No matching declaration or library absence is asserted.
External pending Lean work is not Mathlib coverage.
