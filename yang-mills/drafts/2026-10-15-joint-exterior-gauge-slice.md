# Joint exterior gauge-slice cancellation — working record

The unchanged ready EXPLORE assessment is
literature/2026-10-14-joint-cubic-probe-jet-scale.md. The exact target
remains the finite cubic-scaled limit of L011's joint cubic probe-jet
response for both actual L010 probes. The main construction gap is the
ultraviolet-uniform interacting reflected comparison, followed by
continuum axioms and infrared finite positive mass.

This attempt tests the residual and both rough action slices jointly
in L194(5). For n=S e_k put phi=Phi n, alpha=q phi, beta=Rn.
The proposed intermediate identity is
s_(D phi)=[L,diag(alpha)]/2 and r_(D phi)=[A,diag(alpha)],
from L156(4). Substitute these identities into L194 before any norm.
The expected cancellation removes its explicit multiplier term against
the residual gradient slice, leaving beta-sliced action/residual traces
and L196's already cubic-bounded transport. This is an exact
specialization of existing gauge identities, not a new coverage target.

Continue if signs, both action placements and all projected matrix
orders give exact cancellation; abandon this algebraic mechanism if
an uncancelled multiplier or invalid gradient restriction remains.
Even success leaves the O(N) upper jump in beta and requires actual
signed trace bounds and a controlled scaled limit. Plausible use:
replace the stopped factorwise covariance-commutator estimate by a
boundary-aware bound on the retracted exterior action slice.

Inputs read: L155 full alternating tensors; L156(4) full gauge-jet
identity; L183 full residual retraction; L187 projected product rule
and corrected transpose order; L194(5),(16) common trace; L196 full
transport bound; L197 low-mode obstruction. The local targeted slice
search found the general gauge identity, but no application canceling
L194's explicit multiplier in its joint trace. ATTEMPTS/039–044 and
unfinished work remain intact. No synthetic fixture can replace the
actual action/residual identities in this step.

Saved before completing the proof: with J=J_y, Dalpha=diag(alpha),
L194's replacement 2s_n S+U_n^T becomes
2s_beta S+L Dalpha S-V^T diag(beta)P inside the supported trace.
Since M L=2SA, its L Dalpha term should cancel
-6 Tr(J S[A,Dalpha]S) by transpose and cyclicity. This uses
LS=SL=P and never PH^T=P. All full normal end rows remain.

No positive signed tilt, smooth upper-prefix continuation, separate
convergence, actual-probe lower bound or forest invariance is assumed.
Independent f_(i,2),r_0, full compensation, finer asymptotics, finite
matching and the reflected error <=c_box/2 remain unresolved.

Completed: [L198](../lemmas/L198-joint-exterior-gauge-slice-cancellation.md)
proves the cancellation with its full color sign and matrix order.
It also splits the deterministic beta exterior into the upper normal
slice and its complement. Compact support kills only the residual's
upper slice. The bulk-exterior residual/action trace is
O(N^3 sqrt(log(eN))); the retained transport is O(N^3), and the
remaining error is o(N^3). Only the upper-exterior action trace is
outside this near-cubic control. Its inherited bound is still
O(N^(7/2)); no full-group power improvement or limit is asserted.

Outcome ADVANCE / RESEARCH / REPRODUCTION: an exact local cancellation
and a more specific remaining estimate, with no progress beyond the
checked sources claimed. Verification is analytic; no mathematical
script was created. The proposed cancellation test passes. Continue
the unchanged approved target by examining the actual upper-exterior
action slice in L198(3), retaining the bulk trace and transport for
the subsequent signed-limit question. This slice is not L196's
already removed upper-output quartic partition.
