# Two-term inverse diagnostic — working checkpoint905

Approved target: assessment `literature/2026-11-14-two-term-mobius-pole-diagnostic-904.md`, unchanged SPECIALIZE scope. Inputs: C466a's normalized h and p>=0, integral p=1. C466b(7) supplies downstream motivation only.

Main gap: actual-Xi all-degree algebraic-square positivity at L030-L032/C032a. Test only whether the fixed two-term inverse head admits globally negligible relative error. Do not reopen broad blocked signed-contact coverage.

Let q=sqrt(s) be principal and

    G_2(s)=2c_0 pi^(q/2+1/4)(1-2^(-1/2-q))/((s-1/4)Gamma(q/2+1/4)).

Initial exact check: at s=1/4 the numerator multiplier excluding 2c_0 is 1/2, so the proposed pole residue is c_0. This is not yet a justified inverse asymptotic.

Pending load-bearing estimates: sectorial Stirling uniformly on 1/8<=Re(s)<=1, integrability of every polynomial frequency weight, vanishing horizontal edges, and the full residue term. To call the Bromwich integral a one-sided inverse, also justify support and its Laplace transform. Expected test: if g_2=c_0 exp(x/4)+O(exp(x/8)), eventual |p-g_2|<=g_2/2 contradicts finite mass. No pointwise tail bound for p may be assumed. Failure of inversion/edge estimates stops this test before any asymptotic claim. Compact joint cancellation and contact signs remain open.

Status: unfinished calculation; this note is not evidence of the proposed conclusion. Existing work preserved. No mathematical script needed.

Completed905: the inverse, support, sectorial bound, full residue and finite-mass contradiction are now proved in canonical C466f (`lemmas/C466f-two-term-mobius-head-global-relative-error-stop.md`, notebook-relative). The initial pending reasoning above is retained as the pre-calculation checkpoint, not a second proof. Outcome NEGATIVE for global relative domination only; independent critical review is still pending. No pointwise tail bound for p, infinite-tail continuation, or contact sign was used or obtained.
