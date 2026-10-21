# Triangle high-count descent — completed bounded source comparison

TARGET: Determine whether thirteen distinct additional recovery parameters for a gated L057 triangle pencil force all three normalized pair weights into F_97, retaining both-zero lifts and the original finite exclusions.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Twelve targeted high-count, subfield, syndrome-line and triangle searches; inspected primary confinement, recurrence and circuit statements/proofs; compared L010/L041/L057, local descent analogues and ATTEMPTS/008–009,022–024. Queries and limits below.
SOURCE_EVIDENCE: Chojecki author TeX v9.2, July 17, 2026, inspected 2026-10-10: thm:subfield-confinement-full, lines 2445–2457; DR0–DR8/DRC, lines 2785–2935; residual-kernel and single-MDS-circuit statements/proofs, lines 1370–1460. Reused saved Hall and Marquez-Corbella–Pellikaan coverage as identified below.
COMPARISON: Confinement assumes subfield-valued received generators; it cannot establish their descent. Recurrence covers recovery, not high-count rationality. L034 uses a union-six affine lift, and L044/L055 use tau=1 equations excluding the triangle's both-zero cases. No inspected theorem matches the TARGET.
GAP: Connect thirteen distinct additional finite recoveries to rational p,q,r using actual shared-label equations and both-zero lifts; neither an isolated recovery nor simultaneous descent is established.
REASON: Essential recurrence, distance and local equality inputs are accessible and adequately assessed; the bounded search found no adequate match, permitting one proof attempt on the unchanged TARGET without claiming novelty or proving the implication in this literature turn.
SCOPE: Exact TARGET only: F_(97^20), fixed order-sixteen H in F_97, k=8, pinned four-omission cell, audited L041/L057 tau=0 triangle, nine distinct labels, distinct original finite gamma_i, lambda!=0 and p(1-p)q(1-q)r(1-r)!=0; thirteen distinct additional original finite relaxed recoveries, all quotient ranks and both-zero lifts, zero recovered weights and unrestricted original excluded direction. No unconditional completion, rational chart, global count or extraction premise.
LITERATURE_REASON: Checkpoint 131 changed the target from a single-support critical audit to simultaneous high-count descent; its saved assessment was REVIEW_REQUIRED. This turn supplies that missing theorem-level comparison.

## Saved target and decision test

The main gap remains exclusion/extraction of arbitrary L010 sixteen-count
equality families, with global interval 11/q–16/q. This intermediate target
concerns only the audited L057 triangle on fixed H over F_(97^20). Keep
nine distinct labels, three distinct original finite gamma_i, lambda!=0
and p(1-p)q(1-q)r(1-r)!=0. Count distinct original finite parameters
outside the bases with representatives of weight at most four; retain
initially zero weights and do not count supporting four-sets as distinct
parameters. Do not rationalize the original chart.

Essential local inputs are L010, audited L041 and audited L057. No
cross-notebook input is proposed. Thirteen additional parameters would
complete the three base events to sixteen; their existence is not assumed
unconditionally. A descent result could enable a later finite normalized
weight count while retaining the original excluded direction. A negative
result requires an actual gated pencil or a precise failure of the proposed
implication, not merely a projected support pattern.

The completed review below checks exact statements, stronger results and
recorded failures, reusing recurrence and local-triple assessments where
applicable. ATTEMPTS/008–009 forbid transferring a fixed-label generator
conclusion to all extension-field triangles. ATTEMPTS/022–024 explain why
isolated degrees or support-only conditions need not give simultaneous
recovery. These stops do not prohibit a new high-count descent test. Import
a matching theorem by precise citation rather than reprove it.

Continuation test: after essential coverage is ready, require a mechanism
that controls both-zero lifts or otherwise connects high count to actual
normalized weights. Repeating L057's isolated descent formula is
insufficient. A failed implication should redirect the mechanism rather
than be silently weakened. The count, other triple patterns, arbitrary
extraction and ABF26 identification remain independent gaps. Exact and
supporting Mathlib coverage for this new target are not checked.

## Primary statements and applicability

Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*,
[author TeX v9.2](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
dated July 17, 2026; inspected October 10. Title/date were checked at
lines 122–135. This mutable file is not certified identical to ePrint
2026/1463. Read complete statements and proofs at the anchors below.

`thm:subfield-confinement-full`, lines 2445–2457, assumes B subset F,
D subset B and both received generators in B^D. Explanation at a slope
outside B implies joint explanation on the same support. Its proof
compares field-basis components. Our generators range over F: assuming
this hypothesis would bypass the missing descent. The same mismatch
was already recorded for union six in
`2026-10-07-six-coordinate-twelve-incidence-bound.md`; this is a
triangle-specific comparison, not a newly discovered obstruction.

DR2 and DR6–DRC, lines 2785–2935, require distinct weighted columns,
nonzero multipliers and t<R; they give recurrence membership and exact
finite transverse recovery, separating zero directions. Use R=8,t=4,
multiplier x and eta_j=s_(j+1). L057 already justifies this specialization.
The full-vector zero-direction case does not discard its both-zero
quotient lifts.

The residual-kernel and single-MDS-circuit compilers, lines 1370–1460,
require every counted support inside a fixed U. Their bounds are
(t+1)|F|^kappa(U) and binom(R+1,2), respectively; the latter needs
|U|=R+1 and t<R. With R=8,t=4 its bound is 36. Our extra supports need
not lie in the base nine-set. Neither theorem establishes descent.

Reuse the full Hall Theorem 5.1.1 extraction, printed pp. 63–64,
in `2026-10-05-two-block-moment-obstruction.md`: any field, distinct
evaluation labels, nonzero multipliers and 0<k<=n give dimension k and
distance n-k+1. At n=16,k=8 this gives distance nine. Reuse the
Marquez-Corbella–Pellikaan section 5 extraction, printed pp. 7–8,
in `2026-10-07-six-coordinate-triple-equality-obstruction.md`, and
audited L041's seven-deletion applicability. Those saved extracts were
read; their original PDFs were not freshly retrieved. No reproof or
changed shortening hypothesis is needed.

## Duplicates, stronger comparisons and search limits

Read L010's weighted inequality, equality statement and multiplicity
proof, L041's local statement/converse, and L057's complete statement
and recurrence import. L010 can be applied only after counting distinct
actual finite recoveries supplied by L057. Its equality conclusions
are ready inputs, not evidence that a triangle completes to sixteen.

Read L034's hypotheses and paired-ratio proof through its rational-overlap
step; read L044's hypotheses, statement and shared-locator/two-scalar
descent proof; read L055's hypotheses, statement and rational-weight
reduction. L034 needs the union-six affine lift; the triangle has the
nonzero codeword defect stated in L041. L044's candidates exclude
both-zero quotients. L055 uses tau=1 shared h/d equations and a saturated
singleton row. These are comparisons only, not triangle theorem inputs;
L034/L044's outstanding audits are not silently resolved here.

Reuse `2026-10-08-nine-union-simultaneous-recovery-count.md` for the
inspected Guruswami–Kopparty Theorem 14/Claims 15–16 and
Goyal–Guruswami–Sun–Wootters arXiv:2607.08516v1 Theorems 3.27(1), 5.6.
The required structured disjoint blocks, established design/profile
inequality or random evaluation domain are absent. These counting
comparisons supply no fixed-H triangle descent theorem. No broader
MCA-source retrieval is repeated.

Queries actually run October 10:

- `Reed Solomon syndrome pencil equality finite subfield descent sixteen triangle recovery`
- `Reed Solomon mutual correlated agreement shortening bounds rational descent Chojecki`
- `Reed Solomon list decoding subfield syndrome rationality Galois descent`
- `"Reed-Solomon" "descent" "syndrome" subfield pencil`
- `site:github.com/przchojecki/rs-mca "triangle" "descent"`
- `"Reed-Solomon" "Galois" "affine line" correlated agreement`
- `"mutual correlated agreement" "subfield confinement"`
- `"syndrome" "line" "subfield" Reed Solomon rational descent`
- `"MDS" "subfield" "secant" line rationality`
- `"Reed Solomon" "thirteen" "descent"`
- `"mutual correlated agreement" "triangle"`
- `"Reed-Solomon" "subfield" "many" "syndrome line"`

Searches returned subfield-evaluation decoding/subcode constructions,
generic decoder sources, broader MCA papers and campaign material.
Only the primary author TeX above was selected for new theorem inspection.
The other hits are unread leads, not theorem coverage or evidence of
absence. In particular subfield-evaluation codes allow extension-field
messages; that terminology alone is no descent result. No originality
claim follows. Parked ABF26/Jo/campaign and ECCC access issues are
nonessential to this conditional local attempt and remain unresolved.

## Ready bounded continuation

Use only L010, audited L041 and audited L057 as essential local inputs.
Test the exact conditional implication in TARGET. First account for
distinct actual parameters before invoking L010's equality/fullness and
coordinate balance. Then seek a bridge from that balance to L057 (10)
at isolated recoveries, while retaining every both-zero lift (9).
Possible bridges are a uniform restriction on exceptional label systems
or simultaneous missing-label equations; neither is proved here.
Do not assume a single isolated support missing all three shared labels.

Continue on a proof of the exact implication, or a rigorous partial
restriction that controls the exceptional lifts and changes the remaining
test. Abandon a proposed implication on an actual gated counterexample
with thirteen distinct additional finite parameters and a nonprime
normalized weight, with full moments and original exclusions checked.
If the attempt produces only individual locator capacities or the already
proved isolated descent formula, preserve it as unproductive and reassess.
An abstract support family, prime-field sample or projected zero system
alone is neither proof nor counterexample. Any computational substep
needs complete coverage and a justified passage to arbitrary F weights.

This literature turn derives no new mathematical result, runs no
mathematical script, and changes no lemma or argument overview. EXPLORE
approves one subsequent bounded attempt; it does not certify the descent,
a thirteen-parameter construction or progress beyond inspected sources.
