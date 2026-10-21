# Reverse crossed middle-mass test

The unchanged ready EXPLORE assessment is
`drafts/literature/2026-10-19-reverse-crossed-quantitative-remainder.md`.
This is one mathematical attempt at its complete R_R remainder, with
an intermediate target of removing the macroscopic middle mass length.
The main gap remains interacting reflected error <=c_box/2, continuum
construction, infrared control and finite positive mass. A successful
partial estimate could enable subsequent quantitative localization;
independent freezing, boundary, other-component and interacting gaps remain.

Inputs checked: L085's relative spaces, L103(13),(16)'s energy and
shell estimates, L105's exact trace, L106's uniform covariance comparison,
L107's exact subtraction and L242's two reduced ordered terms. The
target-specific ready assessment and reverse drafts/history contain no
middle-mass coarsening estimate. ATTEMPTS/028--032 remain intact.
No literature retrieval or new source assessment is required.

Work saved before completing the estimate: for 0<=eta<=h<=1,

    T(G_eta-G_h)W_t^T
      =(T G^(1/2)) J_(eta,h) (W_t G^(1/2))^T,
    J_(eta,h)(lambda)=lambda(h-eta)/((lambda+eta)(lambda+h))
                      <=h/(lambda+h).

Thus the proposed HS bound is C N^(3/2)h^(3/4), independent of eta,
under N sqrt(h)>=1. In the first term of L242(3), join D R_ts D^T;
in the second retain R_ts D^T at its original left position. The
additional heat estimate to check is

    sum_st ||R_ts^epsilon D^T|| <= C (N-1)epsilon^(-1/2),

using the nonnegative pinned axial heat kernel and
sup_lambda sqrt(lambda)exp(-r lambda)<=C r^(-1/2).
With the exact a prefactor and all transverse rows, the candidate
middle-mass error is

    C_i N^3 h^(3/4)[log(e/epsilon)+epsilon^(-1/2)].

Continuation test: verify both rectangular trace placements and the
complete level/heat count before claiming the bound. If valid,
epsilon=N^-1 and h=N^(-4/3) give O(N^(5/2)); delta=N^(-2/3)
retains L242's projection budget. All inverse mass lengths would then
be sublinear, but no finite-to-bulk comparison or freezing follows
merely from those lengths. Failure of this count is not signed growth.
Keep both coefficient levels, S_st including the diagonal half, all
filters, source/end rows, constant indices and the complete heat sum.
The required subtraction remains exactly a^-3 K_(i,R) of L107(2),
without an outside factor 3.

Completed: [L243](../lemmas/L243-reverse-crossed-middle-mass-coarsening.md)
proves the proposed estimate for both ordered terms, uniformly in the
original middle mass and in delta, retaining the epsilon^(-1/2) cost
of the second term. Combining directly with L106's covariance-only
step at middle mass zero avoids needing eta=N^-2 at all. The displayed
three-mass schedule gives a full inverse/projection comparison of
O(N^(5/2)log(eN)). This is local partial progress by established
methods, with separate critical audit pending. No complete R_R
remainder, polynomial localization or construction claim is made.
