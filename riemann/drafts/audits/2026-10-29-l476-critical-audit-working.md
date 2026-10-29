# L476 critical audit working record, 29 October 2026

Approved target: critically audit L476's shrinking-cutoff tail estimate,
zero-safe central extension and clipped integral error, including all
multiplicities and cutoff endpoints. The invocation-start SPECIALIZE
assessment is `drafts/literature/2026-10-29-l476-critical-audit-coverage.md`.

Main gap: actual-Xi initial signs at unbounded heights and global mixed
positivity. Intermediate target: accept or repair the O(T(log T)^(5/2))
approximation in L476, for use in a later signed local cancellation test.
Acceptance requires the uniform tail bound, real-zero extension and
clipping estimate to hold; failure requires an identified repair or
restriction, not a conclusion about RH. No optimization or N_h saving
is being attempted.

Read the complete L476 proof; L471's identity, normalization, moments
and saved application audit; L018; L467's exact count convention; the
construction assessment's relevant comparisons and retained ordinary-
moment/global-envelope failure records. The supplied separate audit
assessment already supplies the primary source-scope comparison. No
new source theorem or literature search is needed for this audit.

Preliminary replay: (5) has the correct modulus, and the positive near
shell only uses O(log t) zeros with weight h^(-2). Both positive far
shells admit the stated closed unit-interval covers. Reflected negative
ordinates have distance t+gamma and an absolutely summable log(k)/k^2
bound independent of t. The imaginary-axis zero set is compact and
finite, so its Q/t^2 term is harmless. At a real zero of order nu,
the only singular term after weighting is nu(t-r)^(2nu-2)g(t)^2/A(t)^2;
all other potentially selected terms stay bounded before multiplication
by Xi(t)^2, even through a cutoff switch. No preliminary repair found.

Completed: the uniform constant, finite-indicator representation,
identity (9) at real zeros and all cutoff endpoints, and the dyadic
moment/error exponent pass without repair. The full audit is canonical
in [L476 Section 5](../../lemmas/L476-mesoscopic-signed-kernel-truncation.md).
No new bound, mathematical input or informative obstruction is claimed:
STALLED / RESEARCH / REPRODUCTION, actual task proof_audit. No mathematical
script is necessary for these analytic checks. N_h cancellation,
individual signs, higher signs and full matching Mathlib coverage remain
unresolved. The imported source manuscripts are not independently audited.
