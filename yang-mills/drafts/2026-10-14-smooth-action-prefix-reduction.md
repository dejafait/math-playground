# Smooth-action branch — cubic-scale prefix reduction

The unchanged ready assessment is
`literature/2026-10-12-cubic-residual-action-cubic-scale.md`.
Main gap: ultraviolet-uniform interacting reflection error <=c_box/2,
then continuum and infrared construction. This bounded proof attempt
addresses the missing limit of L159's V_i, within the approved complete
cubic residual/action target. The intermediate test is whether its direct
Hodge part, residual subtractions and axial transport can be removed at
cubic scale, leaving one precisely ordered transverse prefix trace.
That reduction could support a later signed limit and the comparison
with 6K_(i,R)-K_(i,T). It does not assume that comparison or convergence.

Unfinished reasoning saved before completing the proof: split only
R=I-D_0 Phi in L159(1). For the direct part,
||K^(1/2) B_q^T Sigma^(1/2)||_HS^2 is at most
||Sigma||_HS ||B_q K B_q^T||_HS. The full relative spectrum and
L156 give O(N^2 sqrt(log(eN))) and O(a^6 N^4), respectively,
so the factor is O(log(eN)^(1/4)), improving L159's O(N^(1/2)).
Combined with its compact-input factors this suggests
O(N^(5/2) log(eN)^(1/4)). The two Q forms have whitened norm O(1),
so their prefix contribution is O(N^2). For q=L h_l the complete
co-closed transport is O_q=S^T M_q D_0; L159's axial transport and
midpoint-error sandwiches are O(1), whereas the transverse ones
are O(N^(1/2)). This should leave only the transverse transport
against the generator part of A. Exact sign, color, order and all
domain/heat estimates still need to be checked. No result is claimed
by this saved paragraph.

Inputs: L018 L026 L028 L156 L157 L159, with L172/L174 only fixing
the later comparison. Prior ATTEMPTS/009, /011, /036, /037 remain.
No duplicate limit was found in the targeted smooth-action drafts,
recent histories or L173/L174. Existing coverage is reused; no new
source or theorem is needed. Abandon the reduction if its actual
ordered error is merely O(N^3), or if it needs a cutoff of the action
column, omission of an upper end edge, or a smooth forest extension.

Completed: [L175](../lemmas/L175-smooth-action-transverse-prefix-reduction.md)
proves the proposed subcubic reductions and identifies the retained
transverse prefix trace W_i with a^3(V_i-W_i)->0. Its full signed
order and -6 color/prefix factor remain explicit. Ten rational
identities and two squared trace inequalities pass with zero failures
in the saved certificate named in L175; they verify finite algebra,
not the analytic mesh estimates or a limiting coefficient. This is
local standard-method progress, without a novelty claim. No value or
limit for W_i, and no complete-response vanishing, is established.
Continue the unchanged approved target through that retained trace;
the exact hypotheses and unresolved upper/prefix/heat requirements
are in L175. The comparison still requires 6K_(i,R)-K_(i,T), using
L172/L174, and all independent construction gaps remain.
