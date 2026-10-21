# Triangle high-count descent — completed separate audit-scope review

TARGET: Critically audit L058's conditional triangle high-count descent, checking fullness before balance, isolated missing-label coverage, both-zero pivots and original finite exclusions.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the twelve targeted searches and stronger-result comparison in 2026-10-10-triangle-high-count-descent.md; read full L058, L010 hypotheses/conclusion, L041 local-converse statement/audit, L057 hypotheses/recovery statement/audit, histories 132–133 and ATTEMPTS/008–009,022–024; no new external query or mathematical calculation.
SOURCE_EVIDENCE: Reused Chojecki author TeX v9.2 (July 17, 2026), confinement lines 2445–2457, recurrence DR2/DR6–DRC lines 2785–2935 and circuit compilers lines 1370–1460 as assessed on October 10; read saved recurrence, Hall Theorem 5.1.1 pp. 63–64 and Marquez-Corbella–Pellikaan section 5 pp. 7–8 extracts identified below; no fresh original-source retrieval.
COMPARISON: No inspected theorem supplies L058's incidence-to-missing-label bridge: confinement assumes already-subfield generators, recurrence tests individual supports, and circuit bounds assume all counted supports in a fixed set. Ingredient coverage includes the original chart and exceptional lifts but does not certify their new assembly.
GAP: Source scope is ready for the exact conditional audit; fullness-before-balance, isolated coverage and post-descent pivots remain to be checked separately. No finite normalized count or arbitrary-family extraction is established.
REASON: Approve one POTENTIALLY_NEW proof audit of the unchanged TARGET under the prior bounded EXPLORE comparison; approval concerns coverage only, with no new mathematics, reproof or originality finding.
SCOPE: Exact TARGET only: F_(97^20), fixed order-sixteen H in F_97, k=8 and pinned cell, L057 gated tau=0 triangle on nine distinct labels, distinct original finite gamma_i, lambda!=0 and p(1-p)q(1-q)r(1-r)!=0; thirteen distinct additional original finite relaxed recoveries, all quotient ranks, both-zero lifts and initially zero recovered weights. No rational original chart, existence, finite count or extraction assumption.
LITERATURE_REASON: Step 133 proposed a separate REVIEW_REQUIRED audit continuation after deriving L058; unchanged ingredient coverage is reused to approve that exact audit boundary without repeating discovery.

## Main gap, use and discriminating test

The main gap remains arbitrary L010 sixteen-count equality-family
exclusion/extraction, with global interval 11/q–16/q. The intermediate
target is exactly TARGET. A successful audit could make L058 usable for
a later finite normalized-weight count while the original excluded
direction remains unrestricted. Existence, counting, other patterns,
arbitrary extraction and ABF26 identification remain independent gaps.

Continue only if every inference survives the full conditional hypotheses.
A failed implication or missing case requires recording and repairing that
precise defect. A sample or weaker isolated-descent statement cannot
substitute. This source/scope review does not perform the mathematical
audit or declare L058 correct.

## Precise primary coverage and unchanged specializations

Reuse Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*,
[author TeX v9.2](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
dated July 17, 2026, as inspected in
`2026-10-10-triangle-high-count-descent.md`. The mutable file is not
certified identical to ePrint 2026/1463 or freshly checked for changes.
The confinement theorem `thm:subfield-confinement-full`, lines
2445–2457, requires D contained in a subfield B and both generators in
B^D. L058 permits extension-field generators: that theorem cannot
establish their missing descent. Residual-kernel and single-MDS-circuit
compilers, lines 1370–1460, require all counted supports inside a fixed
U; the latter gives 36 at R=8,t=4 and does not supply descent.

DR2 (`drc:lem-locator-recurrence`) and DR6–DRC
(`drc:thm-exact-compiler`), lines 2785–2935, require distinct weighted
Vandermonde columns, nonzero multipliers and t<R. Read the saved complete-
proof extraction under “Primary recurrence input and applicability” in
`2026-10-08-nine-union-fourth-support-incidence.md`. R=8, t=4,
multiplier x!=0 and eta_j=s_(j+1) are L057's unchanged specialization
over F. Full-vector zero-direction cases in the source do not discard
both-zero vectors after L057's three-column quotient; its audited
restored lift is required. No recurrence reproof is needed.

Reuse J. I. Hall, *Notes on Coding Theory*, Theorem 5.1.1 and proof,
printed pp. 63–64 of the undated
[author GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf).
Read “Primary theorem and applicability” in
`2026-10-05-two-block-moment-obstruction.md`. Any field, distinct labels,
nonzero multipliers and 0<k<=n give distance n-k+1. At n=16,k=8,
unit multipliers give distance nine. L010 already supplies moment-kernel
and eight-column independence proofs. No distance reproof is needed.

Reuse I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS
codes that have an error correcting pair*, FFAA 40 (2016), 224–245,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
section 5, Definitions 5.1–5.2, Lemma 5.3 and following unnumbered GRS
shortening formula, printed pp. 7–8 of the
[accepted manuscript dated 2016-02-29](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
Read “Primary shortening input” in
`2026-10-07-six-coordinate-triple-equality-obstruction.md`. L041's
audited seven deletions use dimensions 8 through 2 and nonzero retained
label differences. Its local converse, rather than its equality-conditioned
necessary direction, supplies the triangle. No shortening reproof is needed.

## Duplicate/failure comparison and approved audit boundary

The prior exact searches found no inspected matching descent theorem;
this is not evidence of novelty. L034's union-six lift and L044/L055's
tau=1 equations are comparisons only: their scopes do not cover triangle
both-zero lifts. No cross-notebook result is used. ATTEMPTS/008–009
preserve determinant-only blindness and a fixed-triple generator stop;
ATTEMPTS/022–024 preserve insufficient isolated degrees, support-only
recentering and a false unqualified same-tag exclusion. This audit
reopens none of them. It checks an actual high-count bridge to restored
equations, rather than treating incidence as moment compatibility.
All stop evidence and unfinished work remain intact.

Essential inputs are L010, audited L041 and audited L057; L058 is the
result under review. Check distinct original finite recoveries and
same-support failure before L010, its polynomial hypotheses before its
bound, and fullness/unique supports before balance. Check L057's m=3
restriction for both-zero systems and m=0 exclusion before counting
shared incidences. Audit the six-incidence count, at least three isolated
recoveries and each separately missed label. Check all three restored
equations and denominators, and both-zero pivot rationality only after
p,q,r descend. Do not assume one isolated recovery misses all of P.
Retain E!=0, mu!=0,-1 and original base/infinity exclusions throughout.
No rational original chart, finite count or equality-family existence is
assumed. A failed inference is grounds for repair, not a weakened claim.

L058 has no computational premise or finite certificate to replay.
L057's selected regression is not a new uniform input; its symbolic
criterion and completed audit are used. Full matching and supporting
Mathlib coverage for L058 remain **not checked**. No absence claim,
Lean verification or challenge solution follows. This literature-only
turn changes no lemma, mathematical script, DAG or argument overview;
the separate correctness audit remains pending.
