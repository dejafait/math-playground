# Endpoint calculation working record — step386

Approved target: unchanged actual-coefficient q-Pascal norm test on k=1024r.
Sources and scope: reuse drafts/literature/2026-11-04-actual-toeplitz-qpascal-endpoint.md.
Inputs read: L018/L019/L021/L763; no cross-notebook input. Existing work preserved.

Pending calculation: O'Sullivan v2 Theorem1.4 at K=2 gives f(n)=G(n)+O(log(n)^2/n^2), after retaining gamma_n/(8*4^n*n!) and using log(1+x)=x+O(x^2). With w=W(2x/pi), set
U=x*(2+2log(w)-log(64)-2log(x)-2/w),
B=log(pi^2/2)+7w/4+log(w/(w+1))/2-log(2pi*x)/2+(c1(w)-1/12)/x,
G=U+B. Then U'=2log(w)-log(64)-2log(x), U''=-2w/[x*(1+w)], B''=O(x^-2). Need prove uniform scaled second derivative limit and finite-difference error before concluding endpoint sign.

Endpoint h uses errors with O(r^2) total coefficient size; on k=1024r this is O(log(k)^2)=o(r), not a derivative estimate. Candidate limit with alpha=1/1024:
C=[alpha^2+2alpha-2(1+alpha)log(1+alpha)]/alpha.
Need a rigorous positive bound, and check F_00=exp(h_(r-1))-1 from the first row of L^-1 and D0=1. This would force norm>=F_00 and stop only the unchanged comparison on the selected ray. No minor sign or RH conclusion. Calculation not yet canonically proved or audited.

The pending calculation above is now resolved in canonical L765. The positive
limit and exact entry give norm divergence; independent critical audit remains
pending. This draft preserves the pre-calculation checkpoint, not a second proof.
