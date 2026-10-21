# Reverse crossed projection estimate — work in progress

Gate: `drafts/literature/2026-10-19-reverse-crossed-quantitative-remainder.md`, unchanged EXPLORE coverage at invocation start.

Main gap: interacting reflected error <=c_box/2, continuum construction and finite positive mass. Intermediate target: a uniform projection-removal error within the registered complete R_R remainder budget. Downstream use: quantitative localization of that original ordered trace for a later L011 assembly. Independent localization, freezing, boundary and other component estimates remain unproved.

Inputs being checked: L085 L088 L103 L105 L106 L107. Preserve the same relative SU(2) cube, a=8/N, admitted even N, tau=1/16, probes 3 and 6, original two coefficient levels, S_st, middle inverse and full heat sum; no outside factor 3.

Tentative mechanism: write Z_k=Zeta_k/a and O_k=Z_k^T D-D^T Z_k. Exact DT=0 and PT=T appear to reduce the normalized circulation-only trace to

    a^4 sum_(kl,st)c_(i;kl,a) S_st {
      Tr[R_ts^epsilon D^T Z_k(s) T G_eta W_t^T Q Z_l(t)^T D]
      -Tr[R_ts^epsilon D^T Z_k(s) T G_eta W_t^T D^T Z_l(t)]}.

Only the displayed Q in the first trace would then need replacement. Cyclically join D R_ts^epsilon D^T before estimating. Proposed finite bound:

    sum_st ||D R_ts^epsilon D^T|| <= C N log(e/epsilon).

Test it by the exact axial heat kernel exp(-r L_D), with nonnegative entries and row sums <=1, and the transverse bound sup_(0<=lambda<=12) lambda exp(-r lambda)<=min(12,1/(er)). The already established layer estimate ||P-P_delta||_HS<=C N^(3/2)delta^(3/4) and ||T G_eta W_t^T||<=C would then give unnormalized projection error <=C_i N^3 delta^(3/4)log(e/epsilon), independently of eta. No projection is moved through a coefficient. This is not yet a checked lemma.

Continuation test: check all exact algebra and dimensions on the full relative spaces, then the complete level and heat sums. The proposed schedules epsilon=N^-1, eta=N^-2, delta=N^(-2/3) would put inverse plus this projection error within O(N^(5/2)log(eN)). Reject the estimate if an omitted projection, end row or mass loss invalidates it. Even success supplies no remaining localization or complete remainder theorem.

Completed: [L242](../lemmas/L242-reverse-crossed-reduced-projection-error.md)
proves the exact reduction, the full axial energy-block sum and the
uniform projection estimate above. Its canonical proof includes both
original coefficient levels, all normal end rows and constant indices,
the diagonal half and the full heat majorant. This is REPRODUCTION and
local partial progress, without progress beyond checked source methods
or a complete R_R remainder claim. The new estimate needs separate
critical audit. No literal all-projection regularization is equated with
the reduced approximant, and no mass-dependent qualitative theorem is
used at the displayed schedule.

The retained trace's quantitative localization must still confront the
middle inverse at eta=N^-2: an ordinary mass-length truncation would
have macroscopic range. An ordered joint energy comparison is a
possible test, not an established bound. The canonical target remains
the unchanged assessment's exact R_R remainder, subtracting L107(2).
The actual current status and sole Next action are in PROGRESS.md.
