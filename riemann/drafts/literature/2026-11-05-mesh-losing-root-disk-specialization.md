# Relative root disks — proposed quantitative specialization

TARGET: Derive an explicit epsilon(d,Q)>0 ensuring that every real coefficient perturbation |e_j|<=epsilon(d,Q)|p_j| of a degree-d positive-rooted polynomial with consecutive root ratios at least Q>1 retains d simple positive roots, using disjoint relative root disks and allowing mesh loss.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed step490 source comparison in 2026-11-05-mesh-losing-root-disk-tolerance.md; its exact all-coefficient norm, disk-count and conjugation cases cover this proposed specialization. No fresh search or calculation in this nomination.
SOURCE_EVIDENCE: Graillat--Langlois P32 (6 January 2004), https://perso.lip6.fr/Stef.Graillat/papers/P32.pdf , Theorem3/proof pp.6--7 and Corollary5 p.9 eq.(8); Alexanderian (28 January 2022), https://aalexan3.math.ncsu.edu/articles/polyroots.pdf , Theorem2.2 pp.1--2 and Theorems3.2/3.5 proofs pp.3--5. Direct author PDFs reopened in recovery step491; detailed proof inspection reused from step490. Mosier is unread and unnecessary.
COMPARISON: Import the finite componentwise certificate and standard zero-count/conjugation mechanism; derive only a uniform bound using d,Q. The cited cases alone do not state that uniform bound. Universal and same-mesh preserver obstructions do not decide this weaker output target.
GAP: Select relative disks and obtain a positive explicit lower bound for the certificate uniformly over arbitrary root scales and unbounded upper ratios; justify positivity, simplicity, degree exhaustion, varying leading coefficient and the d=1 case. No formula or result has yet been derived.
REASON: The known mechanism has complete essential coverage; one bounded conventional calculation can determine its degree/mesh threshold. Newly written continuation requires separate supervisor approval before execution.
SCOPE: Integer d>=1, Q>1, real p of exact degree d with 0<rho_1<...<rho_d and rho_(i+1)/rho_i>=Q; real e of degree at most d, including constant and leading coefficients. No same-mesh output, actual-Xi transfer, optimal tolerance or growing-degree sign theorem is asserted.

The [completed comparison](2026-11-05-mesh-losing-root-disk-tolerance.md)
contains precise source versions, hypotheses, proof cases, norm distinctions,
queries and limitations. Its original TARGET was a source assessment;
this TARGET is the subsequent mathematical work, not already executed.

The bounded attempt is to choose one relative radius prescription,
use the imported finite boundary certificate, and seek an explicit
epsilon(d,Q) with 0<epsilon(d,Q)<1. Check all root disks, not just a
central root. Any successful bound must be unchanged by multiplying p
by a nonzero scalar or applying a positive change of variable, and
must not require an upper ratio bound or a compact root interval.
Import standard theorems by citation; only the mesh-dependent estimates
and applicability argument need local proof. No numerical sweep is needed.

Continue if a strictly positive explicit bound and complete all-root
argument result. If only a p-dependent minimum remains or an additional
uncontrolled root-scale parameter is essential, preserve that failure
and stop this uniform disk prescription. Merely restating fixed-p
openness does not satisfy the target. Later usefulness requires comparing
actual relative residual coefficients against the achieved tolerance;
this comparison is outside this abstract attempt.

Main gap: actual-Xi all-degree mixed positivity. Local context is
L791/L792 and inherited L778/L018/L021/L776; C792a and unaudited C792b
are route evidence, not premises of this abstract perturbation theorem.
Any later actual-Xi application must retain exact F_j=R_j through4,
S=B R1, strict t_m,t_a,delta>0 and full original data/quadrature/software
contracts. Growing-degree model existence, separation, actual signed
or relative residual bounds and all-degree signs remain unresolved.
No cross-notebook input is used. Mathlib matching coverage is unchecked.

This is ordinary known-method specialization, suitable for calculation
with standard/high routing. It is not a new central creative mechanism.
No approval, mathematical conclusion or novelty assertion is inferred
from writing this ready assessment; the next invocation must separately
approve it under the supervisor's continuation gate.

## Separate recovery approval — step491, 2026-11-05

The supervisor reported missing direct source URLs in this ready assessment.
Both author PDFs above were opened successfully; the recovered statements
were checked at Graillat--Langlois Theorem3 and Corollary5, including the
index range 0 through n and relative weights, and Alexanderian Theorems2.2,
3.2 and 3.5, including real coefficients and multiplicity-one disk count.
The complete relevant proof inspection in step490 is reused, not replaced
by a search snippet. No changed source hypothesis or new mathematical
claim was found. The monic absolute-perturbation theorem alone remains
insufficient: the all-coefficient certificate and Rouche theorem provide
the intended inputs for the later specialization.

This separate literature-only recovery approves SPECIALIZE for the exact
unchanged TARGET and SCOPE above. The required difference remains the
unproved uniform d,Q estimate; no radius or tolerance has been calculated.
The original future-approval statements above record nomination timing,
now superseded by this separate approval. No further source review is
required before one bounded mathematical attempt under these hypotheses.
Mathlib matching coverage remains unchecked. This is a process repair,
not new source coverage or mathematical progress.
