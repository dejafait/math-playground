# Fixed-minor attempt1996: saved reasoning

Completed: the checked specialization is now written in canonical
lemmas/C029k-fixed-minor-polynomial-companion-regularization-stop.md.
This saved scratch reasoning is historical; independent audit is pending.

Approved target: assessment1994's polynomial-cutoff fixed-interval test.
Inputs: C028d's exact P_d,Q_d and C028f's positive-series growth
log F(r)<=K_0 r^(3/4), r>=1. No root hypotheses are added.

For x=y-b_1 in [1/4,1/2], positivity and binom(d,j)<=(d^j)/j!
give 0<Q_d(y)=P_d(x)<=x^d F(d/x). Thus
log Q_d(y)/d<=log x+K_0*x^(-3/4)*d^(-1/4).
Rows2..d, columns1..d-1 of yI-A_d form an upper bidiagonal
matrix with diagonal -1 and superdiagonal y; its determinant is
(-1)^(d-1). Knill's ordinary finite minor identity after scaling
therefore gives det(M^T M+epsilon^2 I)>=epsilon^2.
Off the roots, the full-size minor also gives det>=Q_d(y)^2,
so the discrepancy D=R-t is nonnegative.

For epsilon=d^(-K), the proposed final comparison is
D>=-log x-K_0*x^(-3/4)*d^(-1/4)-K*log(d)/d.
Its integral has limiting lower bound integral_(1/4)^(1/2)-log x dx
=1/4. Check every determinant power, positivity, and finite-window
consequence in canonical C029k before accepting this calculation.
This only stops the specified monomial companion polynomial cutoff;
signed payment, C028e assembly and H_d=o(d) remain open.
