# Right horizontal theta-Mellin attempt — step523

Approved target: the exact standalone T_R bound in
`literature/2026-11-05-mellin-right-horizontal-tail-test.md` (unchanged
SPECIALIZE assessment available before invocation). This is a source
reproduction attempt, not a new sufficient-sign mechanism.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
T_R <= (14u/sqrt(Q)) exp(-(77/50)Qd^2) on all D. A paid single tail
could support a later, separately assessed Mellin assembly. Continue
only if the whole-ray amplitude and concave endpoint envelope pay this
threshold; otherwise preserve the exact failed sufficient inequality.

Inputs inspected: L797 geometry/branches, L798 phase derivatives,
endpoint decrement and B-normalization, L799 full theta series,
factorization and finite-diameter amplitude argument. Reused step522's
primary-source assessment and duplicate/failure search; the narrow
Mellin-file search finds no other standalone T_R proof. The global
import stop in `ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md`
remains in force. No other notebook input.

Work in progress: write z_R=v_0+iy, z(t)=v_0+t+iy and
phi(t)=Re(S_s(z(t))-S_s(x)). Since Re(a)>0, v_0>u. L799 puts the
endpoint in U and gives tau(0)>Q/(5u); along the ray
tau(t)=exp(2t)tau(0). Its series majorant should therefore extend,
but this extension must be justified explicitly. The phase obligations
are phi''(t)<0 for all t>=0 and a uniform negative phi'(0).
L798's third-derivative bound can estimate phi'(0) from -Ada;
the global concavity estimate must retain the sign of Re(s/z^2)
rather than replace it by an unnecessarily large absolute bound.

Unresolved: those phase inequalities, quantitative normalized allowance
and absolute convergence. Left tails, continued endpoint, global
deformation/assembly, quotient/inversion, certificates and sufficient
signs remain outside this target. No claimed result yet.

## Completion note

The preceding text preserves the initial checkpoint. The completed
proof is canonical in `lemmas/L801-right-horizontal-theta-mellin-tail-bound.md`.
It pays the nominated threshold by a stronger right-ray bound; the
whole-ray amplitude, horizontal slope and concavity were established
without a script. The proof is awaiting independent conceptual review.
No left-tail or global-assembly claim was added. The gate-approved
target was unchanged; no new central sign mechanism was attempted.
