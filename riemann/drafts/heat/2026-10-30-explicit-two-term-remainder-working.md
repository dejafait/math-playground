# Explicit two-term remainder: working checkpoint

2026-10-30. Approved target: abs(H_t/B_t-(1+gamma))<=1/100 for
1/25<=t<=11/50, 0<=y<=1, x>=4*pi*exp(10000). Reuse the saved
SPECIALIZE assessment and the literal Theorem 1.3/Proposition 6.6(ii)
bounds in the preceding source note. No stronger tL/2 claim is used.

Let L=log(x/(4*pi))>=10000 and r=log N. The moving floor gives
N<=exp(L/2)+1, hence r<=L/2+1. The real-part correction is at most
t/(2x^2)<=x^(-2), since (1-3y+8y(1-y)/x^2)_+<=1.
Thus b_n^t/n^Re(s_*)<=n^(-50-y/2) for 1<=n<=N:
t(L/8-1/4)>=49.99 and the remaining 1/2-x^(-2) exceeds .49.
The source gamma estimate gives |gamma|n^y<=exp(1.02)<4;
|kappa|r<1 gives N^|kappa|<3. Both sums together have tail
at most 13 sum_(n>=2)n^(-50)<=26*2^(-50).

Remaining verification before canonicalization: bound every exponential
in e_A+e_B uniformly by exponent <=10^(-6), using
x>=exp L>=L^4/24; check the full sum <=26 and exp(v)-1<=2v.
For e_(C,0), retain its negative square term or drop it, prove
N-1/8>=1 and the last fraction <=1, obtaining exp(-L/4+6)
<=exp(-2494)<10^(-4). Proposed total <153/10^6<1/100.
These are provisional proof notes, not an audited theorem or zero count.
