# 2026-10-04 — Remaining radial flow pairings

Reuse the unchanged SPECIALIZE assessment in
`drafts/literature/2026-09-26-current-target.md`. This is one bounded
mathematical step within its full original-probe coefficient target.
Existing unfinished work, including L019 and L020, is preserved.

The gap is the complete coefficient Gamma_(i,a), including possible
cutoff logarithms and faster terms. The intermediate test is to include
all the Wick pairings of L020's selected radial cubic flow vertex in
kappa(f_(i,2),r_0). Its internal pairings were bounded in L020; the
remaining pairings connect a cubic input to the outer probe leg. If
these also vanish uniformly, this entire selected flow vertex can be
removed from the possible unsuppressed logarithmic sources. If the
bound fails, preserve the specific unsmoothed contraction for a future
cancellation test. This does not address the other action/flow vertices
or the interacting reflected-error threshold c_box/2.

## Working reasoning saved before the final check

Use orthonormal cochain coordinates with A = Delta^(-1/2) xi. In these
coordinates the stored plaquette circulation Y = D z_1(s) is H_s xi,
where H_s = d E_s Delta^(-1/2). Moving the radial flow propagator to the
outer probe leg gives X = Z_s xi with
Z_s = d E_(tau-s) Q_i E_tau Delta^(-1/2).
The full quartic probe correction is
(1/12) integral sum_(p,c,b) X_p^c Y_p^b Y_p^b Y_p^c ds.
The cancellation of a factors uses conversion from stored coordinates
to orthonormal cochain coordinates, each equal to a^2 times the stored
connection/plaquette coordinate; it needs explicit checking in the proof.

Set v_p = (H H*)_pp, alpha_p = (Z H*)_pp,
beta_p = (H R H*)_pp and delta_p = (Z R H*)_pp, where R is the symmetric
one-color whitened residual. Connected six-field Wick pairings suggest
(5/2) integral sum_p (v_p delta_p + alpha_p beta_p) ds for three colors.
The first term is L020. For the second, |beta_p| <= ||R|| v_p and
sum_p |alpha_p| <= ||Z H*||_1. Factorization gives
Z H* = [d E_(tau-s) Delta^(1/2)] B_i E_tau H*, hence its trace norm is
bounded by a constant times ||Delta E_(tau-s)||. L020's time splitting
then gives an integrated O(a^2) bound before ||R|| = O(a^-1), suggesting
O(a) for all remaining pairings as well. No spatial derivative of v or
translation-invariant heat-kernel substitution is needed.

## Completed result

[L021](../lemmas/L021-complete-radial-flow-vertex-bound.md) proves the
suggested identity and bound. The coefficient 5/2 accounts for three
colors and the radial flow/probe prefactor 1/12. The remaining pairing
class is O(a); combined with L020, the entire selected cubic flow
summand is O(a) for both probes. The trace-diagonal estimate avoids
assuming pointwise control of spatial derivatives of the heat diagonal.
The independent exact check passes 24 rational cases, treating both
pairing classes separately and including indefinite residual matrices.

This is an ADVANCE in the local calculation by reproduction/specialization,
not claimed progress beyond the checked literature. It removes one
complete selected flow summand from possible logarithmic sources, but
not the radial action's separate occurrences elsewhere in L011. The
other flow, insertion, action and measure terms and the full cutoff
coefficient remain open, with no improvement of the interacting error
threshold c_box/2. The recorded continuation retains the same ready
assessment and turns to the nonradial/two-quadratic flow terms, where
a Hodge-law transfer must be proved rather than assumed.
