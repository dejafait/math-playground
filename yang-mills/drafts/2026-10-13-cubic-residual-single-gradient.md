# Cubic residual/action: one-gradient mixed-sector attempt

The unchanged EXPLORE assessment is
`drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md`.
The main gap remains the ultraviolet-uniform interacting comparison
with error <=c_box/2, followed by continuum and infrared control.
This attempt tests whether L156's gauge identity removes the complete
mixed (C_g,E)+(E,C_g) sector at cubic scale. Its possible downstream
use is to isolate which part can contribute to compensation; the E,E
sector and all other jets remain independent unresolved requirements.

Checkpoint before verification: polarizing L156(4) in two unrestricted
link fields should give 6 T_F(h,z,D_0 phi) equal to minus the sum of
the terms with A_F on h and on z. Define B_h phi=[h,phi_tail+phi_head].
The proposed mixed-sector trace is then
`-sum c_(i;kl) Tr((A B_h-B_(A h)) K (L B_l-B_(L l))^T E)`,
with three-color extensions and the exterior color sum retained.
This uses a signed bilinear contraction, not a Gaussian with covariance E.

The proposed subcubic part contains B_(A h). Test it with
E L=R Sigma L, ||E||<=C N^3, ||E L||<=C N and Tr K<=C N^5,
together with ||A h||_infinity<=C a^5 p(k),
||L l||_infinity<=C a^3 p(l), and the global pinned
||l||_infinity<=C p(l). These would give O(N) and O(1) for
its two terms. The part A B_h retains A on a rough line and cannot
use smooth residual consistency. No bound for that trace is claimed.

Essential inputs: L018 L026 L028 L085 L149 L155 L156. Full tensors,
both residual insertion subtractions, all action faces, the upper pinned
jump, constant prefix and complete heat spectrum must remain.
Continue on a proved subcubic remainder and an exact retained trace;
abandon extending the smooth-column estimate to A acting on a rough
line without a separate argument. ATTEMPTS/009, /011 and /036 stand.
Completed: [L157](../lemmas/L157-cubic-residual-mixed-smooth-column-reduction.md)
proves the exact mixed-sector trace and the O(a^-1) removed part, retaining
the rough-residual trace and E,E without a cubic bound. Its canonical
proof includes all estimates and qualifications. The 1728 exact basis
checks and two signed tensor/trace comparisons pass. Continue the same
approved complete target using L157(6); no new assessment was written.
