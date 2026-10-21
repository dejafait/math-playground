# Initial derivative heat placement — completed bounded attempt

The unchanged approved target is the joint cubic probe-jet limit in
`drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md`.
The main gap is the interacting reflected comparison with error <=c_box/2,
followed by the continuum and infrared requirements. This bounded attempt
tests L190(8), seeking a cubic-scaled integrable majorant for its three
quadratic W placements. Such a bound would justify initial-time removal;
it would not establish the remaining positive-time or prefix-probe limits.

The supplied overview/DAG and ready assessment were used. Narrow reads of
L183 sections 1–3, 5–6, L189, L190, L182 and L185, plus ATTEMPTS/039–043,
confirm that neither the signed initial derivative estimate nor its
external W placement has an established bound. Existing changes remain.
No further literature is needed for this unchanged assessed target.

Discriminant: keep the external W placement separately only if the actual
positive-time output heat provides a subcubic integrable estimate. Expand
E_(i,s)=H_(tau-s) Q_i H_tau in full relative modes. The candidate bound uses
a deterministic smooth mode against W=P db[t], estimating the quadratic
b coefficient first and applying the signed whitened tilt on its two input
slots. This does not assign smoothness to t(z). The two other placements
must remain explicit; a bound for this placement is not full removal.
Continue on an integrable bound uniform down to s=0; abandon this estimate
if it loses a power beyond N^3 or omits a prefix endpoint.

Essential inputs: L010 L018 L020 L026 L028 L181 L182 L183 L185 L189 L190.
Retain both probes, both residual subtractions, all physical rows, moving
prefixes, constant modes and complete heat sums. No separate-term limit,
forest invariance, signed-tilt positivity or negligible initial time is
assumed. The preceding paragraphs preserve the initial working discriminant.


The completed analytic proof is [L191](../lemmas/L191-initial-flow-external-derivative-placement.md).
It establishes the external W placement bound C_i N^2 m_a(s), with
m_a dominated by L189’s integrable initial-time envelope. Its full
cubic-scaled integral on [0,delta] is at most C_i N^(-1) eta(delta).
The argument expands the actual external heat matrix in all relative
modes, bounds the projected output coefficient of b by O(N^2), and
applies the whitened tilt to both quadratic input slots. It neither
assigns smoothness to t(z) nor replaces the pinned prefix.

Outcome ADVANCE / REPRODUCTION is local partial progress by standard
Gaussian and spectral methods, not progress beyond checked sources.
No mathematical script or new literature assessment was needed. The
other two W placements coincide by symmetric polarization and remain
one signed term with factor -12/a^2. They have only short-time heat on
the W output; the proved external bound does not transfer to them.

The continuation stays on the unchanged approved target. Test that
remaining joint contraction before inequalities, keeping both prefix
variations and the actual exterior covariance. Add L191 to the essential
inputs above. Seek an integrable cubic-scaled majorant or a controlled
signed cancellation, without returning to the stopped global norm
counts. Q_3, its sextic partner, positive-time limits and the independent
construction gaps remain unresolved.
