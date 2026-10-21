# Left crossed prefix: keep its gradient attached

One mathematical attempt at the unchanged EXPLORE target in
`literature/2026-10-19-left-crossed-quantitative-remainder.md`.
The desired component estimate is O(N^(5/2) log(eN)^2); a useful
intermediate result would put L237(12)'s entire prefix term within
that budget at epsilon=N^-1. This could support the quantitative
L011 assembly. The local companion, other component rates,
interacting reflected error <=c_box/2 and continuum/infrared
construction remain independent gaps.

Unfinished reasoning saved before the proof check: write
E_pref=-T sum_mu D_mu, D_mu=S[U_mu,T_1]C_mu. Each D_mu has
HS norm O(N^(3/2)). Its transverse output is confined to the
compact transverse projection of the displacement support, although
its axial output retains the full prefix tail. Choose a transverse
vertex cutoff chi equal to one there, with fixed physical clearance
from transverse faces. Then D_mu=chi D_mu. Do not move chi through
T, P, a covariance or a multiplier.

Test ||K_epsilon Omega_k^T T chi|| <= C p(k)
[a+a^2/sqrt(epsilon)+a^2/epsilon]. The complete H part in L089(1)
has T^T Cc^T=0, leaving only (Bq T)^T M_b Cc and
-(Bb T)^T M_q Cc after transposition. The two-edge paths on
gradients telescope to opposite-vertex differences, as L087(9)
records. On the chi-selected vertices, their adjoints differentiate
M Cc K_epsilon with no transverse face exception. A discrete
product rule gives a times two natural transverse differences of
K_epsilon plus a^2 times one difference. The complete F part can
instead use its O(a^2 p(k)) operator norm and the massive inverse
bound. At epsilon=N^-1 this would be O(a p(k)), which combines
with the original right HS bound O(p(l)N) and D_mu's HS count to
give O(N^(5/2)).

Load-bearing checks still to complete: the full relative tensor
second-difference estimate, all endpoint signs and placements,
transverse support of D_mu after the axial prefix, and the full
exterior heat sum. No estimate has yet been claimed. Abandon this
mechanism if it needs a cutoff on covariance sources or a boundary
condition not present on normal links. ATTEMPTS/029--032 and L237's
failed separate-factor count remain applicable limitations; this
test keeps a different ordered composite intact. Essential inputs
are L087 L088 L089 L090 L093 L100 L237 and their imported relative
spectral and actual-mode hypotheses. L237 remains unaudited.

Completed: [L238](../lemmas/L238-left-crossed-full-prefix-gradient-bound.md)
establishes the ordered composite estimate and the entire O(N^(5/2))
prefix bound at epsilon=N^-1. Its finite tensor Parseval argument
includes the relative sine/cosine boundary types and constant normal
indices. Only the deterministic transverse vertex output is selected;
the full axial tail and every covariance source remain. Together
with L237, the original R_L differs from its local massive companion
by O(N^(5/2)sqrt(log(eN))). This is partial local progress by standard
methods, not a complete R_L rate or a novelty claim. L238 requires
a separate critical audit; the load-bearing compact gradient
composition and the untouched local companion are now explicit.

The continuation is the unchanged covered target, with that local
companion in its exact gh/hh order. Projection regularization must
include P inside A_loc as well as all alternating/covariance selectors;
L225--L229's different co-closed product cannot simply be transferred.
No mass-dependent qualitative limit supplies a rate. The sole current
Next action and routing are in PROGRESS.md.
