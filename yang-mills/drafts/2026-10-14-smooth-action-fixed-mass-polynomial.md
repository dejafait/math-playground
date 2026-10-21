# Smooth-action fixed-mass polynomial test — working record

This is one bounded attempt under the unchanged ready assessment of the
complete cubic residual/action response. The main gap remains the
ultraviolet-uniform interacting reflection comparison and the independent
continuum/infrared requirements. The intermediate target is controlled
finite transverse polynomial approximation of L177(4), with its exact
M,P profiles and multiplier/generator order; this would enable a signed
fixed-mass limit and then the L172/L174 coefficient comparison.

Candidate mechanism: for Delta_T=6I-adjacency on the transverse interior
vertices, use B=(adjacency)/(6+epsilon) and
Q_d=(6+epsilon)^(-1) sum_(n=0)^d B^n. Both Q_d and the resolvent are
nonnegative, with absolute row/column sums <=epsilon^(-1); their
difference has sums <=epsilon^(-1)(6/(6+epsilon))^(d+1).
In the ordered trace, locality of A^gen and S forces the component-1
edge level r to be within a fixed distance of the closing vertex s.
Count sum_(s,t,r near s) min(s,t) 1_(r<t)=O(N^3), without shortening
either axial profile. Combining m=O(a^3), supported h=O(a), and
A^gen=O(a^-1) with the transverse row-sum bound should yield
an O(N^3 rho^(d+1) epsilon^(-2)) approximation error.

Continue only if that bound is uniform in N with fixed mass/degree and
the actual trace order remains exact. A naive operator-norm estimate
above cubic scale or freezing before controlling this error would not
justify continuation. Essential inputs being examined: L028 L156 L159
L175 L177. No signed limit or coefficient is yet claimed. The relevant
history/207–209 has no polynomial approximation proof; ATTEMPTS/009,
/011, /036, /037 and the ready assessment's scope remain respected.

Completed: [L178](../lemmas/L178-smooth-action-fixed-mass-polynomial-control.md)
proves the candidate bound by expanding the actual trace indices before
absolute values. The exact axial sum is bounded by a fixed multiple of
(N-1)N(2N-1)/6; no prefix is shortened. Its uniform polynomial error is
C_i epsilon^(-2)rho^(d+1) after cubic scaling. This succeeds at the
approximation threshold. The conditional transfer is also proved, but
no fixed-degree signed limit or coefficient is claimed. PROGRESS.md
is the sole current continuation record.
