# Corollary C030j: far-time scalar joining audit

## Hypotheses

Let N>=1 be an integer. Use C030h's definitions

\[
 D_N=22500N^2,\quad
 S_N=\frac{\binom{2N-2}{N-1}}{((N-1)!)^2},\quad
 \Delta=T^2-D_N-\tfrac14,
\]
\[
 \rho_N(T,\tau)=\frac4{10000}
   \left(\frac3{10000}\right)^{2N-2}
   S_N T^{4N}e^{-\Delta\tau}.
\]

The scalar conclusions below need no zero hypothesis. For the
actual-spectrum application use the actual zero occurrences,
multiplicities and exponents a=-(rho-1/2)^2 of C030i, and assume
ALL nontrivial zeros with 0<Im(rho)<=T lie on the critical line.
Choose either

\[
 T=T_N=20000N\sqrt{1+\log N},\quad
 \tau=\tau_N=\frac1{4000000N},                             \tag{1}
\]

or the separate choice N=3,T=10000,tau=10^-6. For the time-joining
statement only, retain the entire near-time assertion of Polson
v24 Lemma7.7/(26) as an imported preprint input, specified below.
Its analytic proof and error margins are not independently audited.

## Conclusion

For (1), all scalar hypotheses of C030h hold, including

\[
 T\ge\max(1000,150N),\quad \Delta>0,\quad \tau T^2\ge4N,
 \quad \log\rho_N(T,\tau)<-57N-93N\log N\le-57N.           \tag{2}
\]

For the separate choice, those hypotheses also hold, and

\[
 D_3=202500,\quad S_3=\tfrac32,\quad \tau T^2=100>12,
 \quad \rho_3(10000,10^{-6})<10^{-12}<1.                  \tag{3}
\]

Under the corresponding all-zero verification hypothesis, C030i
therefore supplies every remaining spectral hypothesis of C030h.
Both parity blocks are strictly positive for every t>=tau.
Together with the explicitly retained near-time import, the two
ranges cover every t>0, including the shared endpoint t=tau.
There is no assertion at t=0, no enlarged degree cap and no
all-degree conclusion under one fixed finite verification height.

## Proof

### Source and reason for replay

This reproduces the scalar substitutions in Nicholas G. Polson,
*On Hilbert's 8th Problem*,
[arXiv:1708.02653v24, 11 September2026, Theorem7.4/(21),
printed p18 and its joining proof p22](https://arxiv.org/pdf/1708.02653v24#page=22).
The conditional tail input is its Lemma7.9/(28), independently
replayed in C030h. C030i checks the actual node/count interface
using a separately cited explicit counting theorem. Assessment1198
already covered this exact target before audit1199. A replay is
justified to check strict constants, the N=1 case, the special N=3
clause and the distinction between a sufficient threshold and a
printed auxiliary margin. This is local verification of known
source mathematics, with no result beyond that source claimed.

Use elementary real log/exp monotonicity, exp(x+y)=exp(x)exp(y),
the positive-term exponential series, and log x<=x-1 for x>0.
All arguments of logs below are strictly positive. Selected finite
rational comparisons are certified by
`python3 scripts/far-time/joining-audit-1199.py`, which writes the
complete rational terms, margins and failures to
`scripts/far-time/joining-audit-1199.json`.
The script does not certify imported theorems or the uniform proof.

### General heights and exponential loss

Write L=1+log N. Since N>=1, log N>=0, and the log tangent bound
gives 1<=L<=N. Thus T>=20000N>=max(1000,150N), and

\[
 T^2=400000000N^2L,\qquad \tau T^2=100NL\ge100N>4N.
\]

Moreover

\[
 \Delta\ge(400000000-22500)N^2-\tfrac14
 \ge\frac{1599909999}{4}>0.
\]

The exact correction to tau*T^2 is

\[
 (D_N+\tfrac14)\tau
 =\frac9{1600}N+\frac1{16000000N}
 \le\left(\frac9{1600}+\frac1{16000000}\right)N
 <N\le NL.
\]

The penultimate strict inequality has positive rational margin
15909999/16000000. Consequently

\[
 \Delta\tau=100NL-(D_N+\tfrac14)\tau>99NL.                \tag{4}
\]

### Factorial and logarithmic comparison, including N=1

Put m=N-1>=0. The closed form for S_N, established in C030h
by the coefficient identity for (1+x)^m(1+x)^m, gives

\[
 0<S_N=\frac{\binom{2m}{m}}{(m!)^2}\le4^m,
\]

since (m!)^2>=1 and every binomial coefficient is at most the
sum 2^(2m)=4^m. For m=0, both sides are1. Since
exp(2)>1+2+2=5>4, log4<2. It follows, also when N=1, that
log S_N<=m log4<2N.

To avoid a decimal log evaluation, the positive exponential series
gives exp(1)>sum_(k=0)^4 1/k!=65/24, and exact arithmetic gives

\[
 (65/24)^{10}
 =\frac{1346274334462890625}{63403380965376}>20000.
\]

Hence log20000<10. Since 1<=L<=N, log L<=log N, so

\[
 \log T=\log20000+\log N+\tfrac12\log L
 <10+\tfrac32\log N.                                    \tag{5}
\]

In rho the factor 4/10000 is strictly between0 and1, and
(3/10000)^(2N-2)<=1. Dropping their logarithms thus yields a
strict upper bound even at N=1, where the latter factor is1.
Using (4)-(5) and log S_N<2N gives

\[
 \begin{split}
 \log\rho_N(T,\tau)
 &<\log S_N+4N\log T-\Delta\tau\\
 &<2N+40N+6N\log N-99N(1+\log N)\\
 &=-57N-93N\log N\le-57N<0.
 \end{split}
\]

For N=1, the interpolation product is empty, 0!=1, S_1=1,
L=1,T=20000 and tau*T^2=100. Every displayed bound applies;
neither an N>=2 assumption nor an asymptotic onset is hidden.
This proves (2), in particular rho<exp(-57N)<1.

### Separate N=3 choice

Now T=10000>max(1000,450), tau=1/1000000>0,
D_3=22500*9=202500 and S_3=1/4+1+1/4=3/2. Directly,

\[
 \Delta=\frac{399189999}{4}>0,\quad
 \tau T^2=100>12,\quad
 A:=\Delta\tau=\frac{399189999}{4000000}>98+\frac74.
\]

The margin in the last comparison is 189999/4000000>0.
Multiplying all prefactors of rho exactly gives

\[
 \rho_3(T,\tau)=\frac{243}{50}\,10^{30}e^{-A}.            \tag{6}
\]

Two finite positive-term bounds suffice:

\[
 e^{7/3}>\sum_{k=0}^{8}\frac{(7/3)^k}{k!}
 =\frac{389437879}{37791360}>10,
\]
\[
 e^{7/4}>\sum_{k=0}^{4}\frac{(7/4)^k}{k!}
 =\frac{34193}{6144}>\frac{243}{50}.
\]

Their strict rational margins are respectively 11524279/37791360
and 108329/153600. Thus log10<7/3 and
42log10<98, giving exp(98)>10^42. Since A>98+7/4,

\[
 e^A>e^{98}e^{7/4}>10^{42}\frac{243}{50}.
\]

Substitution in (6) proves rho_3<10^-12, strictly, without a
floating-point approximation to exp or log. This proves (3).

### Actual spectrum and the retained near-time input

For either parameter choice, the checked height condition means
verification through T includes verification through150N.
C030i consequently supplies C030h's positive low exponents,
selected distinct separated nodes, occurrence count N_*(r)<=r^2
for every real r>=T, strip bounds and conjugation invariance.
Together with (2) or (3), these meet every C030h hypothesis.
Its conclusion applies to every t>=tau and both epsilon=0,1,
with all multiplicities retained, gamma=T low and gamma>T high.
No replacement of algebraic squares by modulus squares occurs.

For the other time range import
[Polson v24 Lemma7.7/(26), printed pp19-20](https://arxiv.org/pdf/1708.02653v24#page=19)
in its entirety. More precisely, with c_k(t)=(-1)^k W^(k)(t),
p(x)=sum_(i=0)^(N-1) v_i*x^i real, q(x)=x^epsilon*p(x^2),
and ||q||_G^2=integral_R exp(-x^2)|q(x)|^2 dx, it states

\[
 4\pi t^{\epsilon+1/2}
 \sum_{i,j=0}^{N-1}v_iv_j t^{i+j}c_{i+j+\epsilon}(t)
 \ge\eta_N(t)\|q\|_G^2\quad(0<t\le\log2/180),
\]

where eta_N decreases on this domain,
eta_N(tau_N)>0.7 for every N>=1, and eta_3(10^-6)>1/4.
These margins and the inequality, including their analytic and
arithmetic estimates, remain imported together. The proof here
does not independently certify any of them.

Both joining times are in that domain: log2=integral_1^2 dx/x>1/2,
and 0<tau_N<=1/4000000<10^-6<1/360<log2/180.
For 0<t<=tau the imported eta bound is strictly positive. A
nonzero p gives a nonzero q, so its Gaussian squared norm is
positive. The positive scalar 4pi*t^(epsilon+1/2) and invertible
diagonal matrix diag(1,t,...,t^(N-1)) then identify the normalized
inequality with strict positivity of [c_(i+j+epsilon)(t)].
Using the actual trace identification already retained in C030b,
these are exactly C030h's actual spectral blocks. Thus 0<t<=tau
and t>=tau cover every positive time; both include the joining
endpoint. No matrix at zero is used.

No scalar inequality in this approved audit fails. This completes
the joining interface relative to the full near-time import and
the stated all-zero verification premise. It does not upgrade
C030b to an independently audited analytic source proof. Finite
verification still supplies only a finite degree range; actual-Xi
all-degree mixed positivity, actual-theta signing and graph
realization remain unresolved. There is no RH candidate here.

## Mathlib

Full matching coverage for this parameterized joining statement,
the imported near-time inequality and the explicit zero count is
unchecked. Supporting exp/log inequalities, binomial identities,
finite sums and positive-definite congruence do not by themselves
constitute a matching theorem. Availability is unknown; no absence
claim or formal verification is made. The rational certificate
checks finite constants only.
