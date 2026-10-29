# Mixed cubic insertion/action attempt — 2026-10-26

Approved target: Determine the N^2 leading asymptotic of L280(20)'s complete cubic response on the same relative box and compare it with L285(4).

The main gap is the interacting continuum theory with a nonzero sector
and finite positive mass. This bounded attempt addresses the two mixed
insertion/action groups, retaining their -1/2 prefactors. A controlled
limit would identify further compensation in the exact reflected
coefficient. The distinct-line group, subleading control, uniform higher
remainder and continuum/infrared construction remain independent gaps.

Coverage is the unchanged ready EXPLORE assessment
`drafts/literature/2026-10-26-complete-cubic-quadratic-asymptotic.md`.
Local duplicate/failure checks use L280(20), L284, L286–L289 and
ATTEMPTS/047–049. No new literature theorem is being assumed.
The exact product bump and all relative boundary qualifications persist.

## Saved unfinished reasoning

Let V_h=sum h_p (Cx)_p dot zeta_p(x), with h only on 12-plaquettes.
Define E_h by u^T E_h v=2 E[DV_h[u] DV[v]]. Its rows are supported
on the edges incident to supp h. The mixed group is
-Tr(E_h G_opposite)/2. Split each derivative into A_h (external curl)
and B_h (internal curl), exactly as in L287.

The promising test is stronger than a Hilbert–Schmidt estimate:
for an edge cutoff chi supported away from the opposite source,
seek ||chi U_opposite||_1=O(N), and the analogous local curl map
with trace norm O(1). The separated mode formula L284(8) should
give rank-one summands with an exponentially summable coefficient.
Together with ||U_opposite||=O(N), ||CU_opposite||=O(1), this
would give ||G_opposite chi||_1=O(N^2), so the weighted version
of L288's full operator approximation could be used without losing
a power of N. All estimates still need verification.

For fixed polynomial covariance, the weighted internal-curl row sum
must be computed with a 12 insertion and the complete action, not
replaced by L289's orientation-summed scalar without calculation.
Actual raw-edge phases and the three external colors must be retained.

Continue only with a uniform complete trace error, a justified weighted
bulk tensor and boundary/source passage; abandon this mechanism if only
an unestimated source or internal tail remains. No asymptotic is claimed
by this saved note.

## Completed partial result

[L290](../lemmas/L290-cubic-mixed-insertion-action-asymptotic.md)
completes both mixed groups with limit -3 I_1 J_f/16 apiece and
o(N^2) errors. The separated rank-one edge/source expansion supplies
||chi U||_1=O(N); L281 supplies the local curl nuclear norm O(1).
Together these give the full O(N sqrt(log(eN))+log(eN)) external-curl
error and the uniform O((m+1)^-1) normalized internal approximation
error. No unestimated action-anchor tail is left in these groups.

The weighted 12-vertex/action row sum is calculated explicitly with
the transverse matrix: its limit is 8 I_1 Pi_12. Summing orientations
recovers L289's 24 I_1 identity coefficient. Compact insertion support
controls every fixed-range boundary path after the uniform approximation
bound; Riemann sums retain the actual source fields and all colors.
The factor -1/2 in each mixed group gives the stated limits. The
subtotal with L289(3) is (3-22 Z_0)J_f/128. L290 holds the complete
proof and qualifications; this note does not replace them.

Exactly one cubic group remains: B(T,T;G_-,G_+,G)/2. Its scale and
possible compensation are not presumed. L286–L290 need separate
critical audits. Subleading control, uniform higher remainders and
the continuum/mass construction remain open. No mathematical script
or new external theorem was needed in this bounded attempt.
