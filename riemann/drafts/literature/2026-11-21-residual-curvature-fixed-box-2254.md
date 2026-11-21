# Fixed residual-curvature calculation coverage2254

TARGET: Certify or refute W_x(u)=(G_x'(u))^2-G_x(u)G_x''(u)>0 for all (x,u) in [14,29/2] times [0,1], with G_x(u)=x integral_0^infinity K(u+t)sin(xt)dt, using complete tails and closed-cell enclosures.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed2254 exact/stronger searches and scoped duplicate/failure comparison in drafts/literature/2026-11-21-residual-curvature-source-notes-2254.md; no matching theorem identified and no novelty inference. This ready nomination requires a separate next-turn literature approval before invocation.
SOURCE_EVIDENCE: Csordas1998 Corollary2.11/full proof p43 https://web.math.pmf.unizg.hr/glasnik/33.1/33105.pdf ; Csordas1309.0055v2 Theorems3.5/3.7/4.5 https://arxiv.org/pdf/1309.0055v2 ; Prekopa1973 Theorems6-7/proofs pp342-343 https://acta.bibl.u-szeged.hu/14411/1/math_034_335-343.pdf . Calculus/Simpson/Taylor/Decimal inputs reuse2249/2251/2252 with exact hypotheses and links below; local exact formulas/tails are C919m and C919r(5)-(14).
COMPARISON: The primary shape theorems do not supply curvature of this signed residual. General rigorous integration and the local theta formulas cover the proposed technique; effective bounds, nonlinear cancellation and complete closed-box certification are the specialization, not a source theorem or new general mechanism.
GAP: W_x's sign and a usable error margin have not been calculated or proved. Exterior curvature, preservation under further removals and the all-degree actual-Xi interface remain independent open gaps.
REASON: One independently testable actual-residual condition survives the source comparison and is not the stopped finite-count or generic-prefix bridge. Reuse ready calculus instead of reopening optional sources; do not reprove named general results.
SCOPE: L019/L058 normalization, x in[14,29/2], u in[0,1], half-line derivatives at u=0. Smooth even inverse-quotient interpretation only when14<x<29/2 and Xi(x)=0, multiplicity allowed. No first-zero census, exterior assertion, arbitrary-removal invariant or RH sufficiency is assumed.

## Imported tools and precise applicability obligations

Use the completed source review2253/2254 and source notes2254, including
the exact scope and unread-source qualifications. No primary theorem
there proves the target. The reason for a local certificate is precisely
that the direct import is unavailable; no originality is asserted.

For dominated differentiation use K. Conrad, *Differentiating under
the integral sign*, author-hosted30-page version inspected21November2026,
[Theorem12.3,p16](https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf):
continuous integrand/parameter derivative and parameter-independent
integrable majorants. Its proof is referred out. Dominated convergence,
signed Fubini and Tonelli reuse T. Tao, *245B notes0*,1January2009,
[Theorem3(4)-(5),Theorem4(1)-(2)](https://terrytao.wordpress.com/2009/01/01/245b-notes-0-a-quick-review-of-measure-and-integration-theory/),
whose general proofs are omitted. Absolute integrability must be
verified for every signed interchange. Closed endpoints require
one-sided arguments or a justified open extension, not interior-only
parameter differentiation. Reuse the existing C919m formulas with
their full scope rather than deriving a second general ODE theorem.

For composite Simpson use [NIST DLMF3.5.6-8](https://dlmf.nist.gov/3.5.ii),
citing Davis--Rabinowitz(1984),pp57-58: real C4 integrand on the entire
finite interval, positive even panel count, and a global fourth-derivative
bound. For Taylor use Strang--Herman, *Calculus Volume2*, Section6.3,
[Theorem6.7](https://openstax.org/books/calculus-volume-2/pages/6-3-taylor-and-maclaurin-series),
with the next derivative controlled on the whole intervening interval.
These theorem statements/proof qualifications are already inspected
in2249/2232; no new general proof is needed. Neither theorem supplies
the numerical constants for this determinant.

Retain the [Python Decimal contracts](https://docs.python.org/3/library/decimal.html#decimal.Decimal.exp)
approved2252: correct integer/Fraction operations, directed basic
operations, context-relative neighbors, correctly rounded HALF_EVEN
exp, and exceptional-signal checks. This is a conditional arithmetic
certificate, not an independent backend verification. Ordinary nearest
floating-point trigonometry cannot serve as a certified node.

## Exactly one bounded mathematical attempt after approval

Seek a strictly positive rational lower bound on the entire unchanged
box, or a rigorous nonpositive countervalue. Save one finite setup and
the intended test before the sign pass. Reuse existing C919m integral,
first derivative and second-derivative ODE, C919r's derivative bounds
through order17, and existing Simpson/Taylor tools only within their
verified domains. Any needed higher derivative requires its own bound.
The choice of enclosure representation and effective constants is
future mathematical work; none is calculated or approved as sufficient
in this literature turn.

Pay omitted theta indices, the full spatial tail, quadrature and
parameter interpolation errors, and arithmetic errors before forming
the squares/products. Check the entire relevant certificate rather
than its preview. Include all closed cells, faces x=14,29/2 and u=0,1,
and every shared boundary. Do not infer W_x from C919r's linear margins.
At nonroots do not impose G_x'(0)=0 or claim a smooth even extension.
For actual roots, C919m supplies its root-qualified positive smooth
even quotient kernel without a simplicity premise. No new zero
census or decimal near-root substitution is needed or permitted.

A complete positive lower bound justifies retaining compact curvature
as a partial shape input. A rigorously nonpositive value rejects the
stronger box, and at a nonroot does not reject actual-root curvature.
A zero-crossing enclosure is inconclusive. Preserve any failed setup;
do not shrink the box or run repeated automatic retuning. Do not infer
exterior curvature, repeated-removal closure, all-degree positivity,
or RH from either outcome. A subsequent continuation outside this
scope needs its own review.

The proposed task is calculation / REPRODUCTION specialization, with
standard/high routing. It is not a creative central mechanism. The
lack of a concrete shape-preservation law and all-degree interface
currently blocks a justified creative nomination. Full matching
Mathlib coverage is unchecked; no absence claim is made.
