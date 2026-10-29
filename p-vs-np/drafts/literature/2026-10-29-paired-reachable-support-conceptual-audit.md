# Paired reachable support obstruction — conceptual-audit source scope reviewed

TARGET: Critically audit L127's paired-reachable superlinear generator bound, checking residual membership, full A_f projection rank and the single-charge minor in original coordinates.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 550 separately compared the changed residual-membership, original A_f binomial-projection and distinct-generator minor obligations, reusing step-548 and step-545/547 coverage and Attempts 058–060. New paired-reachable support, Pascal/Krylov and projected/total generator-weight searches established no adequate exact-family import; literal queries and inspected ranges are in drafts/2026-10-29-paired-reachable-audit-source-review-work.md. Search failure does not establish novelty.
SOURCE_EVIDENCE: Reuse Ésik–Maletti, 2010 author manuscript Definition 3.1/Theorem 4.2 pp.2–3 (https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf), and all primary theorem/proof-case reads and direct URLs in drafts/literature/2026-10-28-paired-reachable-generator-support.md and drafts/literature/2026-10-28-full-relation-support-conceptual-audit.md. New supporting read: Edelman–Strang, Pascal Matrices, undated 12-page MIT course manuscript pp.1,3,7 and equations (5)–(8) (https://web.mit.edu/18.06/www/Essays/pascal-work.pdf); published Amer. Math. Monthly 111(3) (2004), 189–197, DOI 10.1080/00029890.2004.11920065. The local endpoint identification and quantitative K_N conclusion are not imported from it.
COMPARISON: Qualitative paired reachable common sources and supporting Pascal/rank/determinant algebra are known; none of the inspected sources supplies the exact original-coordinate K_N generator bound. L126's separately audited individual-row inequality is the available quantitative input; its full-E_N basis conclusion does not establish L127. The changed endpoint membership/projection and one-charge applicability bridges remain mathematical audit obligations, not source blockers. No characteristic-zero/large-characteristic sparse-shift result is transferred to F₂.
GAP: Audit that K_N is contained in E_N, that original-coordinate reversed A_f parameters have rank N for every k>=0, and that each selected minor entry charges a distinct generator through precisely L126 §3's inequality; independently reproduce the complete N=4 evidence without inferring asymptotics from finite ranks. No bridge is accepted by this literature decision.
REASON: The separate bounded source-scope comparison is complete and no essential source is blocked. The exact saved target is ready for a later conceptual audit; this approval neither verifies L127 nor rejects step 549 or its finite evidence.
LITERATURE_REASON: The target changed from testing K_N generator support to independently auditing L127's newly written membership/projection/minor argument; step 550 completes that separate scope comparison while reusing adequate prior primary reads.
SCOPE: F₂, N=2^k, all original L122 endpoints and coordinates, K_N generating families and expanded support only; no equality K_N=E_N, combined parameter projection, other invariant space or arbitrary-chain theorem is assumed.

Essential inputs are L127 §§1–6, L122 §2's literal rows and boundaries,
L125 §2's reversed-coordinate parametrization, and L126 §§2–3,7's
audited row inequality. The full certificates are
`scripts/batched-incidence/output-549/paired-reachable.json` and
`scripts/batched-incidence/output-549/audit.json`; both producing scripts
must be checked before treating their successful summaries as reception.

Step 550 completes the separate source-approval turn; full comparisons,
access qualifications and unread leads are in
[its source notes](../2026-10-29-paired-reachable-audit-source-review-work.md).
The actual mathematical audit is conceptual_audit (deep_research/xhigh), because
projection surjectivity and quantifier transfer are load-bearing, even
though the finite replay itself is routine. Check all k=0, empty-sum,
zero-residual-coordinate, cancellation and generator-redundancy cases.
A failed bridge retracts only the unsupported uniform obstruction while
preserving all exact finite evidence and older attempts.

The continuation test is explicit: retain the paired-reachable stop only
if the uniform projection, row-bound applicability and distinct-row charge
all survive. Finite rank 7<9 is never a substitute. No cross-notebook
theorem is needed; Mathlib coverage of the full bound remains unchecked.
