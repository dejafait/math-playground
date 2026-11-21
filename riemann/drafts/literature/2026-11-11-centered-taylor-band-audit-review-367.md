# Centered Taylor band obstruction — source-approved audit

TARGET: Audit C997r's centered Taylor band norm/defect dichotomy, including exact coefficients, endpoint phase separation and the uniform Laguerre peak.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step368 reused reviews364/365 and reviews291/325, read full C997r and the relevant C997c/C997q definitions, C997e bulk conversion and audit329; directly rechecked DLMF4.6.7 and18.14.8 with domains. No new broad search or originality claim.
SOURCE_EVIDENCE: Audited C997c(1),(4)-(6) and C997e(4)/audit329; Vanlessen https://arxiv.org/pdf/math/0504604v2 Theorem2.4(b)/(2.13), Remarks2.3/2.5, Proposition3.31, Theorem3.32 and Proposition5.1/(5.5)-(5.6), printed pp5-7,32-34,39, at Q(x)=x, alpha=2, N=n+1; https://dlmf.nist.gov/4.6.E7 and https://dlmf.nist.gov/18.14.E8. Existing primary assessments are reused, not newly reread.
COMPARISON: Known sources cover the binomial coefficients, full-kernel upper bound and uniform real bulk formula, but do not establish C997r's specialized original-TV/complete-defect dichotomy. The audit must check that specialization and its strictly limited centered-Taylor scope.
GAP: Independently verify C997r(2)-(3), especially uniformity in m and n, the coefficient-l1 identity, phase branches, existence of a real bulk peak, and subtraction of the full target defect; scalar checks alone are insufficient.
REASON: Step368 separately approves source readiness for the unchanged conceptual audit after matching its real bulk interval, degree, normalization and complete-kernel scope to existing assessments. C997r itself remains unaudited; no new result was derived.
SCOPE: Audit only C997r's fixed center t=2n, fixed eta_n, integer 0<=m<=n and complete C997q definitions; no rescaling, other centers or arbitrary-grid lower bound.

The main gap remains actual-Xi positivity, signed forcing and L984(H).
A correct scoped stop would remove one explicit construction from the
positive-branch point bridge; it would not refute that bridge or RH.

The audit should read the full C997r proof and the needed C997c and
C997e passages, retaining the latter's SAME fixed J=[15/8,17/8],
alpha=2 and degree n+1. The evaluation point approaches J's endpoint
from inside; its uniform O(1/n) hypothesis is essential. C997q(1)-(2)
were checked from C997c during step367; no broader C997q audit is claimed.
All g_n zeros and both beta terms remain; the phase projection must
work with real g_n even at zeros. The lower boundary is retained and
left unestimated because TV or D already fails, which is sufficient
only for the simultaneous criterion, not for a point-residual lower bound.

Accept only if both branches of the dichotomy hold for ALL sufficiently
large n with constants independent of m, and the sequence argument
handles infinitely many high orders as well as eventually low orders.
If a phase, normalization or uniformity error is found, repair it or
withdraw the corresponding subclass stop while preserving the evidence.
Do not replace the result with a finite numerical fit.

The certificate scripts/adaptive-slope/centered-taylor-band-checks-367.json
contains 21 rational checks, not a certified bulk onset or an independent
proof. The exact coefficient identity has a written algebraic proof.
Full Mathlib matching coverage is unknown. C997g/i/m/p and stops314/315/364
are comparisons only. No cross-notebook result is used. Selected/both-sign
transfer, C997a(8), assay/reconstruction, complements/regulators, L993,
L984(H) and actual-Xi positivity remain unproved.

The original step367 nomination awaited separate approval. Step368 below
completes that source gate only; it does not certify C997r.


## Separate source approval — step368, 11 November 2026

SPECIALIZE is retained for the exact TARGET above. Read C997r in full,
C997q hypotheses/conclusion and its finite-measure residual passage,
C997c definitions and spectral-measure bounds, C997e's imported bulk
conversion, and history/audit329. Reused review291's primary theorem
and proof-case assessment and reviews364/365's finite-sum comparison.
Vanlessen was not freshly downloaded; its inspected primary contracts
and the audited local conversion are reused as required by policy.
The initial notebook-scoped status output was overlarge and truncated;
no sibling notebook was inspected and no existing work was discarded.

The source question has no changed analytic hypothesis: C997r requests
only real c in the SAME fixed closed J=[15/8,17/8], alpha=2, Q(x)=x,
N=n+1, and the same orthonormal-to-Laguerre normalization. Its moving
subinterval stays within this fixed bulk interval for large n. Thus the
existing uniform bulk contract covers the domain requested for audit;
no hard/soft-edge, complex continuation, growing-parameter or derivative
error theorem is needed. This is a scope comparison, not verification
of C997r's peak selection or the displayed specialized asymptotic.
The later audit must still check its conversion and use of uniformity.

Directly read [DLMF4.6.7](https://dlmf.nist.gov/4.6.E7), including its
qualification of any real or complex constant exponent and |z|<1,
and [DLMF18.14.8](https://dlmf.nist.gov/18.14.E8), with x>=0 and
alpha>=0. Served version1.2.8, release15 September2026. The former
covers the local binomial-series input, without a moving-window tail
rate. The latter covers a real Laguerre upper bound, without a lower
bound or control after the -1 subtraction. Those are already cited
inputs, not new imports or proofs. No primary source directly certifies
the original coefficient-l1 identity, all-order phase separation,
complete-defect subtraction, or the sequence dichotomy; these remain
the mathematical audit's work. A fresh superoscillation search would
not resolve these proof-specific obligations. No essential source is
blocked and no unread lead is used as a theorem.

Known overlaps and failures are retained: reviews364/365 distinguish
fixed-compact convergence and minimum-energy upper bounds from original
TV lower bounds; C997q's exact-cancellation stop is not an approximate
rate theorem; the earlier packet stops do not exclude arbitrary grid
measures. C997r is tested only with fixed eta_n, center2n and 0<=m<=n.
The prior duplicate assessment distinguishing C997g is reused, without
claiming a new duplicate search or originality certification.

Proceed next to the exact saved audit target. Accept its scoped stop
only after verifying every sufficiently large n with constants uniform
in m, the original atomic TV, endpoint phase projection, real bulk peak,
complete target subtraction, and mixed high/low-order sequence case.
Repair or withdraw a failing branch; do not infer an all-grid stop or a
point-residual lower bound. Both beta terms, K's -1, both windows and all
zeros remain mandatory. The audit may leave all independent positivity,
selected transfer, realization and regulator gaps unresolved. Mathlib
full matching coverage remains unchecked/unknown. No lemma or mathematical
script was changed or run, and no mathematical advance is claimed.
