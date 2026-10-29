# L110 equality case — published cycle-exclusion assessment

TARGET: Assess whether the published Simons–deWeger m-cycle exclusion covers L110's equality divisor case, including repeated words and the trivial cycle.
CHECKED: 2026-10-28
DECISION: IMPORT
SEARCH_EVIDENCE: Reused step538/two-peak comparisons; searched Simons "On the nonexistence of 2-cycles" theorem pdf and Simons de Weger 2005 m cycles erratum Theorem 3; retrieved the published primary PDF rather than relying on search summaries.
SOURCE_EVIDENCE: Simons–deWeger, Acta Arithmetica117(2005),51–70, section1.1/p.51, section1.2/p.52, Theorem3(b)/p.55, section1.3/pp.52–53 and Lemma15 with its complete proof/p.62; cyclic scope in section3.3/p.58 reused.
COMPARISON: The published exclusion covers the closed two-run case once L110's existing exact-run and equality premises are matched; no primitive-period or global-minimum assumption is needed. It supplies no open-endpoint exclusion.
GAP: The canonical application and combination with L110 are deferred to a separate research turn; no new nondivisibility theorem or descent corollary is established in this literature turn.
REASON: Exact source coverage replaces an unresolved equality-only applicability question with a direct known-result import; redoing the source's exclusion proof or L110's elimination is unnecessary.
SCOPE: Equality-only application under every L110 hypothesis, followed by its already proved non-equality descent alternative; no unit-growth exclusion, larger family or universal descent claim.
LITERATURE_REASON: The equality-only target changes from finite-word algebra to a closed-cycle theorem; repetition, trivial-cycle exceptions and the computational basis had not been checked for this application.
COVERED_TARGET: Audit and record the direct Simons–deWeger Theorem3(b) application to L110's equality case and its resulting descent-by-j+1 corollary.

## Primary theorem and qualifications inspected

[Simons–deWeger, *Theoretical and computational bounds for m-cycles of
the 3n+1-problem*, Acta Arithmetica117(2005),51–70,
doi:10.4064/aa117-1-3](https://www.impan.pl/shop/en/publication/transaction/download/product/82263)
uses exactly L110's shortcut map (p.51). Section1.2 (p.52) permits
nonminimal periods, counts local minima by their positions, and requires
only a local starting minimum. It explicitly includes repeated {1,2}
as the trivial m-cycle. Theorem3(b) (p.55) excludes nontrivial m-cycles
for 1<=m<=68. Lemma15 (p.62) already covers m=2; its proof compares
Lemma14's upper bound with Corollary11's lower bound. Section1.3
(pp.52–53) records the external verified lower bound X0=301*2^50 used
in these estimates. This is a published theorem import, including its
computational basis, not an independent verification of those computations.
No additional unproved conditional hypothesis is attached to Theorem3(b).

## Applicability checklist for the separate import

The essential local input is audited L110 (hypotheses/conclusion and
the complete divisor converse, especially equation(12)); L002 supplies
the exact-run conventions. Compare on L110's original tuple, without
adding any minimum, primitive-period or distinctness premise:

1. Retain n>1, a,c,d>=1 and every proper-prefix/terminal coefficient
   guard. Work only in the hypothetical equality case y=n; L110 already
   identifies its final even run as exact, unlike the unit-growth case.
2. Match the source's two chronological blocks with (k0,l0)=(a,1),
   (k1,l1)=(c,d), period p=j, K=a+c and L=1+d. Check the junctions
   at indices 0 and a+1, and the peaks at a and a+1+c using the actual
   run statements. No count of distinct numerical junction values is
   required by the source convention.
3. Check nontriviality using the existing facts that n is odd and n>1;
   do not use n>1 alone for an arbitrary even starting state. Do not
   discard repetition or silently replace the displayed period by a
   least period. The source's repeated trivial-cycle exception must be
   addressed explicitly in the canonical application.
4. Cite the m=2 case, rather than reprove its number-theoretic exclusion.
   Keep the original first-drop guards in the resulting restricted
   descent statement even though the cycle theorem itself needs none.

These are routine source-to-hypothesis checks for the next turn, not
a new symbolic elimination or a proof written here. The expected
downstream use is to combine the equality exclusion with L110's existing
non-equality alternative to establish descent by j+1 for its family.
Unit growth at j need not be excluded to obtain that conclusion.

## Reuse, failures and boundary of approval

Reused `2026-10-28-orbitwise-mechanism-discovery.md` and
`2026-10-28-two-peak-unit-gap-test.md`: their obstruction to applying a
cycle theorem to an open endpoint remains valid. The change is L110's
separately identified equality case, not a relaxation of closure.
L110's audited divisor converse is sufficient to pass from a proposed
equality divisor to an actual word; no integrality/realization assumption
may be supplied merely from the published cycle equations. No duplicate
canonical equality exclusion was found in the targeted L110 working,
audit and step539/541 records. Preserve the stopped elimination and
margin-order evidence; no census or family expansion is approved.

Continue only if the canonical check preserves all four items above;
a mismatch in exact closure, run count or exception treatment stops this
import. Other shapes and finite coefficient-drop existence remain open.
The sole next mathematical target is the COVERED_TARGET above; newly
updated coverage remains subject to the supervisor's separate approval.

The bounded searches also surfaced Simons2005 (Math. Comp.74,1565–1572),
Simons2007's inductive proof and an updated deWeger manuscript. Those
theorems were not inspected or imported here: the accessible published
2005 Theorem3(b) suffices for the nominated m=2 scope. No assertion of
novelty or exhaustive absence of corrections follows from these searches.

The MathPrize page dated 2021-07-07 was revisited on 2026-10-28; its
accessible text names the conjecture but does not spell out the iteration.
The exact local target remains GOAL.md/foundations/01-target-and-scope.md;
no prize-rule conclusion is used. Matching Mathlib coverage is **not
checked**. The original step541 nomination is superseded by this source
assessment, with its unresolved broader targets retained above.
