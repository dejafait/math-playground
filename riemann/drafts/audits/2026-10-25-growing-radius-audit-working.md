# Working record: approved A=2 growing-radius audit

Started 2026-10-25. Gate: existing SPECIALIZE assessment
`drafts/literature/2026-10-25-growing-radius-audit-coverage.md`.
No new target is being approved here. Actual task: proof_audit,
RESEARCH / REPRODUCTION. L018 is the mathematical local input;
L464 is downstream context only; no fixed zero-free premise is used.

Main gap: initial Xi signs at unbounded heights, effective bounded-height
coverage and global mixed positivity. Intermediate target: audit the
Section 4.2 analytic estimates for fixed c_0>1/2, ell=log(t/(2pi)),
R=ell^2 and even n=2p with c_0<=n/ell<=R. Downstream use: support a
later overlap with L464's coefficient tail. Continue only if constants
are uniform throughout this range; record a failure at its exact bound
otherwise. The scope does not include the Section 4.5 saddle.

Source v4, displayed 24 October 2026 07:18 UTC, equations (8)-(18b)
retrieved on 25 October. Existing source comparison and failure checks
are reused; targeted local searches found no completed duplicate audit.
All pre-existing changes are retained.

Unfinished proof plan (not yet a verdict): use sector digamma expansion
on disks |y|<=4R; integrate the anchored four-term logarithmic derivative.
On the positive saddle wedge the zeta derivative series decays with
Re(y), so multiplication by c remains bounded. Keep exp(ell*u), not
an unbounded conversion to t^u, above u=1/2. Treat 1<=sigma<=2 using
the near-one logarithmic theorem and sigma>=2 by absolute convergence.
For the gauge, compute the paired trigamma terms before bounding them:
1/(1/2+iz)+1/(1/2-iz)=1/(z^2+1/4). This cancels individual O(1/t)
terms and permits a uniform O(1/t^2) second logarithmic derivative.
Cauchy extraction costs sqrt(n)<=ell^(3/2); the fixed arc exponent
gap must pay this factor. No division by Xi(t) is permitted.

Completion: the approved audit passed. The full proof, precise classical
citations, sector/branch choices, uniform arc errors, gauge cancellation
and coefficient normalization are canonical in
`lemmas/L465-growing-radius-stirling-amplitude-and-xi-audit.md`.
The unfinished checkpoint above is retained as historical working text.
The result is local verification of a source-stated component; it does
not check the separate all-order assembly or conditional saddle.
