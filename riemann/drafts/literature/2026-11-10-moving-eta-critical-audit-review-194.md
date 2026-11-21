# Moving-eta result — approved critical audit coverage

TARGET: Critically audit L972's all-n fixed-index moving-eta bound, checking sector sign, absolute separation, off-diagonal normalization and the constant 1/9.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step195 reuses the two-eta search/duplicate screen in 2026-11-10-prescribed-q-moving-eta-loss-review-192.md and 2026-11-10-prescribed-q-index-recurrence-review-191.md; read both assessments and the L967/L971 stop records. No new discovery search or novelty claim.
SOURCE_EVIDENCE: Read full L972, L024 and L026 and L964 through its analytic estimates; reuse step193's inspected DLMF https://dlmf.nist.gov/1.9.E30 and https://dlmf.nist.gov/1.9.E31 and https://dlmf.nist.gov/1.10.E1 version1.2.8 and Xiao https://arxiv.org/pdf/2006.13103v1 Theorem3.2/Corollary3.3 pp4-5. Primary source passages were not reloaded in step195.
COMPARISON: Standard Cauchy/Taylor tools cover the analytic inputs, not L972's signed two-denominator estimate. The unchanged actual-node audit scope is now separately approved; no known theorem is imported as validation of L972 or as an unconditional sign recurrence.
GAP: Mathematical critical audit of L972, particularly its separated constant-part series, remains undone. Source coverage is adequate; signed fixed-eta forcing and the broader index recurrence remain outside this target.
REASON: Separate literature-only step195 approves reuse of ready coverage for the exact saved audit, without validating its conclusion or deriving new mathematics. Audit the local specialization before downstream use; no reproof of standard analytic theorems is warranted.
LITERATURE_REASON: The L972 audit was REVIEW_REQUIRED at invocation; approve its new audit scope using adequate existing sources, without repeating browsing or extending the target.
SCOPE: Audit only actual-Xi paired nodes with multiplicities, fixed A>0 bounding their absolute mass, fixed a_n in both terms, eta_j=1/(64*9^j), algebraic squares, and the complete sum. No index recurrence, new finite sign, alternate eta sweep or RH premise.

## Exact evidence and audit obligation

The full proof is canonical in `lemmas/L972-fixed-index-moving-eta-uniform-loss.md`.
Essential inputs are L024, L026 and L964. L966 supplies a normalization
comparison only; L968 is a downstream conditional result, not a sign
premise. Check the claim that L964's analytic bounds are independent
of its supplied negative-margin hypothesis. No such hypothesis occurs
in the new lemma's statement; independence of the estimates remains an audit obligation.

The proposed audit must examine the complete rational real-part
identity, rather than a numerical sample or a preview. Check the
beta-sector implication from |Re alpha|>4 and |Im alpha|<1/2; the
off-diagonal definition and all denominators; absolute convergence
of both separated series; conjugation with multiplicity; Cauchy disk
and branch; and the uniform cancellation delta*C_n=1/9. Its test is
to uphold the all-n -A/9 bound or identify a precise defect and repair
or withdraw that bound, preserving the original derivation.

No theorem-level external source is missing or asserted inaccessible.
Source and failure comparisons may be reused while these hypotheses
are unchanged. The original step194 nomination left this audit
REVIEW_REQUIRED. Step195 now supplies its separate literature-only
approval. The next turn defaults to the mathematical audit using
proof_audit/routine_audit, standard/high, unless a delicate analytic
issue requires escalation. No audit has been performed in step195.

The strongest local conclusion sought is validity of L972. Even a
successful audit leaves signed fixed-eta index forcing, initialization,
recurrence closure and cumulative margins unresolved. Full matching
Mathlib coverage is unchecked/unknown. No cross-notebook input.

## Separate scope approval — step195, 10 November 2026

The prior tool assessment remains adequate: DLMF 1.9.30-31 assumes
continuity on and inside a simple closed contour, analyticity inside,
and an interior evaluation point. DLMF 1.10.1 assumes analyticity in
an open disk and gives its Taylor expansion there. Step193 read these
primary statements and recorded version 1.2.8. The present comparison
identifies L964(5),(9)-(10) as the passages whose application must be
replayed: analyticity/branch, the closed Cauchy circle strictly inside
the domain, its supremum, and the remainder radius. Their use without
L964's negative-margin premise remains an audit obligation, not a
conclusion of this literature turn. These source hypotheses and the
target have not changed; another external retrieval is unnecessary.

The complete L972 text was read to set audit scope, without checking
its rational identities or accepting its constant. L024 and L026 were
read as the stated local summability/geometry inputs. No new theorem
about the sector, denominators, separated series or uniform constant
was proved. The audit must check those claims independently, including
the off-diagonal definition and conjugation with all multiplicities.
L966 is a convention comparison only; its theta formula need not be
extended, and L968 supplies no sign premise.

Reuse Xiao's exact recurrence and full RH-conditional corollary proof
as inspected in step192/193: neither compares two eta parameters.
The scoped records
`ATTEMPTS/2026-11-10-li-theta-boundary-spreading-stop-168.md` and
`ATTEMPTS/2026-11-10-complete-bell-reflected-prefix-stop-189.md`
were read. They stop specific pointwise/prefix payment rules, not
this fixed-index audit. No stopped mechanism is reopened, no duplicate
recurrence is reproved, and no inaccessible parked lead is essential.

Success means the full all-n bound survives audit; a defect must be
identified precisely for repair or withdrawal with its original proof
preserved. A finite sample or sign-free estimate cannot pass. Even
success supplies only an audited local specialization: an A/9 loss
per step is not a summable budget, and initialization, signed index
forcing, recurrence closure and all-degree positivity stay unresolved.

Outcome: STALLED in mathematical evidence, LITERATURE,
NOVELTY_UNCHECKED. Approval changes process readiness only; it is not
an ADVANCE, a mathematical audit, or evidence beyond the checked
sources. No lemma, mathematical script, PROOF or DAG was modified.
