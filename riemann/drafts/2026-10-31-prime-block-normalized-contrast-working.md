# Prime-block normalized contrast: working checkpoint

Completed: the moment calculation and its full proof are canonical in
`lemmas/L574-prime-block-normalized-density-lower-bound.md`. Both
required scales hold in that argument, with errors O(T^(5/8)log T)
and O(T^(3/4)log T). It supplies C481a's mass premise and ratio lower
bound. This first derivation awaits a separate audit. The planning
notes below preserve the unfinished reasoning as it was saved;
their pending language is superseded by L574, not independent evidence.

Approved target and source scope: the unchanged invocation-start
`literature/2026-10-31-prime-block-normalized-contrast-attempt.md`.
Main gap: actual-Xi positivity. This attempt tests only C481a's missing
positive density mass, with the full L477 residual remaining independent.

Use the supplied T,L,h,M,J,D_h,Q_T and prime block. Set B(t)=sum
p^(-1/2-it), so P=-Re B. Planned finite calculation (not yet certified):
the diagonal of integral |A_M(t+sigma)|^2 B(t) is |J| times
sum_p p^(i sigma) H_floor(M/p)/p. Its second difference with -Re
therefore has positive weights 4 sin^2(log p/(2L)). Mertens gives
sum_block 1/p=log 2+O(1/L), and the harmonic factor has size L.

For the weighted second moment, expand P^2 exactly into |B|^2 and
Re B^2. Group A_sigma B and A_sigma B^2 by integer products, retaining
all p=q and p!=q cases. Maximum lengths are M T^(1/8) and M T^(1/4),
both o(T). Need prove coefficient norms O(L), justify the polarized
finite mean-square error and the exact interval shift, and retain
all floor and translation phases. No independence or disjoint-support
factorization is available. The proposed moments and lower bound are
still pending at this checkpoint.

If both moments pass, apply weighted Cauchy--Schwarz on the finite
interval, then check |D_h|<=Q_T and the bounded dual D_h/Q_T.
Use C481a only for its already proved curvature transfer. No L573
cap claim, full-residual claim, Xi sign, or RH resolution is sought.
