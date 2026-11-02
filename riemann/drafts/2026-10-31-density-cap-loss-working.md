# Density cap loss: working checkpoint

Approved target: test O(T) mass removed by the (log T)^4 cap in
C481a, using the unchanged SPECIALIZE assessment
`literature/2026-10-31-density-cap-loss-specialization.md`.

Candidate finite argument, pending full write-up: write A_M^2 with
support N=M^2, coefficients d_2(k;M)/sqrt(k). The imported sharp
mean square has error O(N), not O(N log N). The elementary prime-power
inequality d_2(k)^2<=d_4(k) should give coefficient norm <=(1+log N)^4.
Thus the fourth moment is O(T (log T)^4). Weighted Cauchy gives
|D_h|^2<=4(F_M(t+h)^2+2F_M(t)^2+F_M(t-h)^2). Each translated J is
inside [T,2T], so its integral is at most 16 times that fourth moment.
Finally (x-B)_+<=x^2/B with B=(log T)^4 would give O(T).

Check every coefficient inequality, interval endpoint and absolute
constant before promotion. No lower density bound is asserted.
C481a's positive premise, full-residual comparison, defects, negative
mass and Xi signs remain independent. No new mathematical script.

Completed: all candidate inequalities and translated endpoints were
checked and written in canonical L573. The obtained loss is <=81 C_0 T,
where C_0=1+C_MV/(2 pi) for the absolute imported mean-square error
constant. This meets O(T), not merely O(T log T). The conditional
lower-premise comparison loses any chosen positive difference c-c'
eventually; neither positive premise is proved. This preserves the
initial reasoning above rather than replacing it with a new target.
