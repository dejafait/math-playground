# C019x — The exact weighted high-index diagonal exceeds the required scale

## Hypotheses

Use C019p/u's unchanged fixed actual-Jensen setup, with d tending
through positive integers and the positive solution T>2*pi*e of

\[
 d=\frac{T}{2\pi}(\log(T/(2\pi))-1),\quad X=T/\sqrt{2d},
 \quad q=\log X,\quad h=3\pi/q,\quad B=(\sqrt2-1)X,
\]
\[
 J=[X,\sqrt2X],\quad D=[X,\sqrt2X-h],\quad
 L=\lfloor X^{1/1000}\rfloor,\quad \ell=\log L,
 \quad R=L^4,\quad \omega(n)=1-\log n/\ell\quad(n\le L).
\]

Let alpha be the real multiplicative coefficients of the
Euler-product branch of zeta(s)^(-1/2) on Re(s)>1. In particular,
alpha(1)=1 and alpha(p)=-1/2. These are finite-polynomial
coefficients here, never a reciprocal evaluated on the critical line.
Define c_r by the exact finite product

\[
 M(Y)=\sum_{n\le L}\alpha(n)\omega(n)n^{-1/2-iY},\qquad
 (M(Y)M(Y+h))^2=\sum_{r\le R}c_r r^{-1/2-iY}.
\]

Retain both source floors and own heat times:

\[
 t(Z)=Z^2/(2d),\quad u(Z)=\tfrac12\log(Z/(2\pi)),\quad
 N(Z)=\left\lfloor\sqrt{Z/(2\pi)+Z^2/(32d)}\right\rfloor,
 \quad N_*=N(\sqrt2X),\quad Z_*=N_*^2R,
\]
\[
 E_n(Z)=\exp\{t(Z)((u(Z)-\log n)^2-\pi^2/16)/4
                      +i(\pi/8)t(Z)(u(Z)-\log n)\}.
\]

For rho_n>0 solving rho_n/(2*pi)+rho_n^2/(32d)=n^2, use exactly

\[
 G_k(Y)=\sum_{\substack{m,n\le N_*;\ a\le R\\mna=k}}
 c_a n^{-ih}E_m(Y)E_n(Y+h)
 \mathbf1_{\{Y\ge\max(\rho_m,\rho_n-h)\}}.                \tag{1}
\]

All assertions below have an absolute existential integer onset.
There is no RH, random-law, nonvanishing, simplicity or
ordinary-to-heat moment assumption.

## Conclusion

There is an absolute c>0 such that, for every sufficiently large d,

\[
 \inf_{Y\in D}\sum_{L<k\le Z_*}\frac{|G_k(Y)|^2}{k}
       \ge c\frac{\ell^4}{q^2}\ge c' q^2,
 \qquad
 \int_D\sum_{L<k\le Z_*}\frac{|G_k(Y)|^2}{k}\,dY
       \ge c''Xq^2.                                      \tag{2}
\]

Thus the proposed O(X) high-index weighted diagonal is false.
This stops the independent diagonal payment in C019u's sufficient
two-budget method, in addition to C019w's unweighted-variation stop.

Equation (2) is not a lower bound for the full grouped time norm:
its unequal-index terms may have either sign. It does not refute
the grouped norm at O(X), the real-pair moment I_V, or C019r's
actual-Jensen squared moment I_P. Even a failure of the stronger
grouped norm alone would not refute the real-pair target. No sign
density, root-count or RH conclusion follows. Independent conceptual
audit1409 below retains (2) and its limited implications; inherited
transfer, variation-budget and low-index audit qualifications are
unchanged.

This is local elementary reproduction under unchanged ready
assessment1402, not a claimed discovery beyond the checked literature.
The new route evidence is the exact weighted lower bound (2).

## Proof

### A finite squarefree harmonic mass estimate

Write nu(r) for the number of distinct prime divisors of r, with
nu(1)=0. We first establish, for all sufficiently large real U,

\[
 \sum_{\substack{r\le U\text{ squarefree}\\p\mid r\Rightarrow p>11}}
       \frac{4^{\nu(r)}}{r}\ge c_0(\log U)^4,\qquad c_0>0.
                                                               \tag{3}
\]

Only elementary finite products are required. Set
z=floor(U^(1/32)) and suppose z>=13. Expand the finite product

\[
 A_z=\prod_{11<p\le z}(1+4/p)
    =\sum_{r\in\mathcal S_z}\frac{4^{\nu(r)}}r,
\]

where S_z consists of all squarefree products of primes in (11,z],
including 1; it is a finite set with no imposed size cutoff.
Counting the terms that contain each prime gives exactly

\[
 \sum_{r\in\mathcal S_z}\frac{4^{\nu(r)}}r\log r
       =A_z\sum_{11<p\le z}\frac{4\log p}{p+4}
       \le8A_z\log z\le\tfrac14 A_z\log U.               \tag{4}
\]

Here the elementary factorial estimate already used in C019v (10)
gives sum_(p<=z) log p/p<=2 log z: the first prime powers in z!
give sum floor(z/p) log p<=log(z!)<=z log z, and
floor(z/p)>=z/(2p). Applying (4) only to r>U shows that at most
A_z/4 of the nonnegative mass lies there. Thus at least 3A_z/4
is supported on r<=U.

We also have a uniform lower bound for A_z. For p>=13, put
F_p=(1+4/p)(1-1/p)^4. The elementary logarithmic inequalities

\[
 \log(1+x)\ge x-x^2/2\quad(x\ge0),\qquad
 \log(1-y)\ge-y-\frac{y^2}{2(1-y)}\quad(0<y<1)
\]

imply log F_p>=-11/p^2. The first inequality follows by
differentiation; the second by bounding the terms of the usual
absolutely convergent logarithm series from degree two onward.
Since sum_(n>=12) n^(-2)<=integral_11^infinity x^(-2)dx=1/11,

\[
 A_z\ge e^{-1}\prod_{11<p\le z}(1-1/p)^{-4}.              \tag{5}
\]

Let a_11=product_(p<=11)(1-1/p)>0, a fixed number. The finite
Euler product product_(p<=z)(1-1/p)^(-1) expands into the sum
of 1/n over integers whose primes are at most z. Its geometric
series converge because there are only finitely many primes.
It contains every integer 1<=n<=z, so this product is at least
H_z>=log(z+1). No Euler product for zeta at s=1 is being asserted.
Equation (5) consequently gives

\[
 A_z\ge e^{-1}a_{11}^4(\log(z+1))^4
      \ge e^{-1}a_{11}^4(\log U/32)^4.                    \tag{6}
\]

The last inequality uses z+1>U^(1/32). Combining (4)--(6) proves
(3), for example with c_0=3e^(-1)a_11^4/(4*32^4). The sum
in (3) includes every term retained from S_z; no estimate for
unretained terms is needed. In particular no Mertens asymptotic,
Selberg--Delange theorem or additional source premise is used.

### The four tapered factors retain their squarefree sign

Take U=floor(sqrt(L)). For squarefree r<=U, expand the exact c_r as

\[
 c_r=\sum_{a_1a_2a_3a_4=r}
       \prod_{j=1}^4\alpha(a_j)\omega(a_j)\,
                         (a_2a_4)^{-ih}.                 \tag{7}
\]

All a_j are at most r<=sqrt(L)<=L, so every displayed assignment
is permitted by the original four truncations. C019p's
multiplicativity gives alpha(a_j)=(-1/2)^(nu(a_j)). Squarefreeness
therefore makes each product of four alpha coefficients equal to
(-1)^(nu(r))*2^(-nu(r)). There are exactly 4^(nu(r)) assignments,
one of four positions for each distinct prime. Moreover each taper
is at least 1/2, and

\[
 0\le h\log(a_2a_4)\le h\log r
       \le h\ell/2\le3\pi/2000<\pi/3.
\]

Rotate (7) by the real sign (-1)^(nu(r)) and take real parts.
Every term lies in the stated common sector, with cosine at least
1/2, and the product of the four tapers is at least 1/16. Hence

\[
 |c_r|\ge 2^{\nu(r)}/32\quad(r\le U\text{ squarefree}).    \tag{8}
\]

This keeps the prescribed shift and all four linear tapers; replacing
the finite polynomial by an infinite reciprocal is unnecessary.
From (3),(8), and log U~ell/2 we obtain

\[
 \sum_{\substack{r\le U\text{ squarefree}\\p\mid r\Rightarrow p>11}}
             \frac{|c_r|^2}{r}\ge c_1\ell^4.              \tag{9}
\]

### Isolate exact coefficients with two source primes

Let P_X be the primes in [sqrt(X)/10,sqrt(X)/5]. We reuse the
counting input in C019w (4),(11): the standard prime number theorem,
pi(x)~x/log x (Hadamard and de la Vallee Poussin, 1896), as stated
in [NIST DLMF 27.12.4](https://dlmf.nist.gov/27.12.E4).
C019w checked this source and its fixed-ratio interval subtraction.
It yields |P_X|>=c_2 sqrt(X)/q eventually, without a shrinking
interval, progression estimate or RH-strength error term. Therefore

\[
 \sum_{\substack{p_1,p_2\in P_X\\p_1<p_2}}\frac1{p_1p_2}
    \ge\frac{25}{X}\binom{|P_X|}{2}\ge\frac{c_3}{q^2}.   \tag{10}
\]

Choose such a pair and any r occurring in (9). Set k=p_1p_2r.
We now check every possible assignment in (1), rather than assume
that C019w's single-prime r argument applies to composite r.
The scale relations of C019u/v give d comparable to X^2q^2,
t(Z)=O(q^(-2)), and

\[
 N_*^2\le\frac{\sqrt2X}{2\pi}+\frac{X^2}{16d}<X
\]

eventually. Also p_j<=N(X), p_j>R, and p_1p_2>N_* eventually:
N(X)>=floor(sqrt(X/(2*pi))), R<=X^(1/250), and
p_1p_2>=X/100 suffice. Thus neither large prime can divide a<=R,
and they cannot both divide the same m or n. Each must occupy
one source index. Any nontrivial divisor b of r is at least 13.
Consequently p_j b>=13 sqrt(X)/10>N_*. Neither source index
can contain any factor of r. There are exactly two assignments:

\[
 (m,n,a)=(p_1,p_2,r),\quad(p_2,p_1,r).                    \tag{11}
\]

Both source primes have entered by X. Since N is nondecreasing,
their indicators in (1) equal one throughout D, including its
endpoints and at each own shifted source argument. It follows that

\[
 G_{p_1p_2r}(Y)=c_r\{
 p_2^{-ih}E_{p_1}(Y)E_{p_2}(Y+h)
 +p_1^{-ih}E_{p_2}(Y)E_{p_1}(Y+h)\}.                     \tag{12}
\]

For p in P_X and Z in J, u(Z)-log p=O(1), uniformly. Hence
E_p(Z)=1+O(q^(-2)). Since log p=q/2+O(1), the exact h=3*pi/q
gives p^(-ih)=i(1+O(q^(-1))). The braces in (12) are therefore
2i+O(q^(-1)), uniformly in Y and the primes, and have modulus at
least one eventually. Each E still uses its own time. In particular,

\[
 \inf_{Y\in D}|G_{p_1p_2r}(Y)|\ge|c_r|.                  \tag{13}
\]

### Sum the disjoint indices and compare thresholds

The large primes exceed R, whereas r<=U<=R. Unique prime
factorization therefore recovers their unordered pair and r from k;
different choices give different indices. All selected k lie in the
high block: k>=X/100>L eventually, and
k=p_1p_2r<=N_*^2R=Z_* since p_j<=N(X)<=N_* and r<=R.
Thus (9),(10),(13), with the exact weight 1/(p_1p_2r), give

\[
 \sum_{L<k\le Z_*}\frac{|G_k(Y)|^2}{k}
 \ge\left(\sum_{p_1<p_2\in P_X}\frac1{p_1p_2}\right)
       \left(\sum_{\substack{r\le U\text{ squarefree}\\p\mid r\Rightarrow p>11}}
                          \frac{|c_r|^2}{r}\right)
 \ge c_4\frac{\ell^4}{q^2},\qquad Y\in D.                \tag{14}
\]

Here ell=q/1000+o(1), so ell^4/q^2>=c_5 q^2 eventually.
Finally |D|=(sqrt(2)-1)X-h is bounded below by a positive constant
times X. Integrating (14) proves (2). All sums are finite, all
nonnegative restrictions are explicit, and one common existential
onset makes these estimates hold for every sufficiently large integer d.

The required diagonal threshold was O(X); the actual lower bound
divided by X tends to infinity at least as c q^2. C019w's single
prime r near L did not detect this because its taper and harmonic
mass were too small. The larger family of squarefree r with no
prime divisor at most 11 contributes the factor ell^4 in (9).
This is why the present test differs from the already stopped
unweighted-budget test and the absolute upper estimates1403/1405.

For the grouped norm J_d of C019u, the exact identity is
J_d=D_d+O_d, where D_d is the full weighted diagonal and O_d is
the signed sum over unequal indices. Neither (14) nor its proof
controls O_d. It is invalid to discard it when lower-bounding J_d.
Furthermore C019u only provides I_V<=16 J_d. These two distinct
limitations prevent a conclusion about the original M2 target.
Direct signed integration of the full norm or the full real-pair
observable would be a different test; the separate diagonal budget
cannot be paid by improving an upper estimate.

Assessment1402 already covers this finite-sum subtest of the fixed
squared pair. The imported PNT is the same precisely cited counting
input as in C019w. The remaining derivation is included to justify
the exact truncated support, fractional coefficients, phase sector,
and moving-heat specialization; no ordinary fourth-moment theorem
or new source coverage is asserted. The local duplicate check found
no weighted-diagonal obstruction in C019u/v/w or stops1403/1405/1407.

### Independent conceptual audit1409 — 18 November 2026

This audit replays (2) from the displayed finite definitions. It
checks the used portions of C019p/u/v/w, not their other conclusions
or the inherited actual-Jensen transfer. No repair of (2) is needed.
For clarity the symbol c_0 in this subsection denotes the positive
constant in (3), not the phase constant pi/8 used in other lemmas.

**Finite mass and size truncation.** Give a squarefree product r of
primes in (11,z] weight 4^nu(r)/r. Its total weight is A_z, and the
fraction of the weight containing a fixed p is exactly 4/(p+4).
Thus the first logarithmic moment in (4) is exact. The factorial
argument applies to the integer z and gives sum log(p)/p<=2 log z;
no estimate of the number of primes is used at this stage. For r>U,
log r>log U, so (4) leaves at least 3A_z/4 at r<=U. This truncation
is essential: the full finite product itself is not supported below U.

The local logarithmic bound can be checked more precisely as

\[
 \log F_p\ge-\{8+2/(1-1/p)\}/p^2\ge-11/p^2\quad(p\ge13).
\]

Its sum is at least -1 by the stated convergent integer tail.
Removing the primes at most 11 multiplies the inverse Euler product
by a_11, rather than its reciprocal. Hence the direction and factor
a_11^4 in (6) are correct. Every integer n<=z occurs in the finite
geometric expansion, and H_z>=log(z+1)>log U/32. These observations
verify the stated c_0=3e^(-1)a_11^4/(4*32^4)>0. Neither an infinite
Euler product at s=1 nor an unproved prime asymptotic enters (3).

**Exact coefficient signs.** For r squarefree, each prime occupies
exactly one of the four ordered positions in (7). All 4^nu(r)
assignments occur because each factor is at most r<=sqrt L. Their
alpha products are (-1)^nu(r)2^(-nu(r)), their four taper products
are at least 1/16, and a_2*a_4<=r. Thus after the one real sign
rotation every summand has real part at least its unphased alpha
magnitude divided by 32. This verifies (8), including r=1. Squaring
and applying (3), with log(floor(sqrt L))>=ell/3 eventually, gives
the explicit sufficient version of (9)

\[
 \sum_{\substack{r\le U\text{ squarefree}\\p\mid r\Rightarrow p>11}}
       \frac{|c_r|^2}{r}\ge\frac{c_0\ell^4}{1024\cdot81}.       \tag{15}
\]

**Scales, all assignments and own times.** Independently putting
zeta_0=log(T/(2*pi)) in the defining scale equations gives

\[
 d=e^{\zeta_0}(\zeta_0-1),\quad
 X=\frac{\sqrt2\pi e^{\zeta_0/2}}{\sqrt{\zeta_0-1}},\quad
 q=\zeta_0/2-\tfrac12\log(\zeta_0-1)+\log(\sqrt2\pi),
 \quad t(Z)=\frac{\pi^2(Z/X)^2}{(\zeta_0-1)^2}.
\]

The positive branch has zeta_0 tending to infinity as integer d
tends to infinity. In particular d/(X^2q^2)->2/pi^2 and
t(Z)=O(q^(-2)) uniformly on J. The exact floor gives
N_*^2<=sqrt(2)X/(2*pi)+X^2/(16d)<X eventually. The fixed gap
1/5<1/sqrt(2*pi) ensures p<=N(X), including the floor, for every
p in P_X at one common onset. Also p>R and p_1*p_2>N_* uniformly.

For any factorization m*n*a=p_1*p_2*r in (1), neither large prime
can divide a<=R, and they cannot share a source slot. A source
containing any further factor must be at least 13*sqrt(X)/10>N_*.
This proves that (11) is exhaustive, including composite r with
arbitrarily many distinct factors; no omitted source term can cancel
the two retained terms. Each prime entered by X, so both indicators
are one on the closed D. At each Y in D both Y and Y+h belong to J.

Writing p=s*sqrt X, 1/10<=s<=1/5, makes
u(Z)-log p=(1/2)log((Z/X)/(2*pi))-log s uniformly bounded.
Consequently each of the four actual E factors in (12) is
1+O(q^(-2)). The shifted scalar is
p^(-ih)=exp(-3*pi*i/2)exp(-3*pi*i*log s/q)=i(1+O(q^(-1))).
The bracket in (12) is therefore within O(q^(-1)) of 2i uniformly;
its modulus is at least one eventually. No equal-time replacement
or nonvanishing hypothesis is used.

**Counting and threshold.** The precise PNT input and fixed-ratio
subtraction cited above give
|P_X|~sqrt(X)/(5q). Thus |P_X|>=sqrt(X)/(10q) eventually, and
binom(|P_X|,2)>=|P_X|^2/4 eventually. Since p_1*p_2<=X/25,
the unordered harmonic pair mass in (10) is at least 1/(16q^2).
The primes exceed R>=r, so unique factorization recovers the
unordered pair and r without overcounting. The inequalities
X/100>L and p_j<=N_* place every selected k in the claimed block.

Combine this count with (15), (13), ell>=q/2000, and
|D|>=((sqrt(2)-1)/2)X. One explicit, deliberately small lower
constant verifying (2) is

\[
 \int_D\sum_{L<k\le Z_*}\frac{|G_k(Y)|^2}{k}\,dY
 \ge \frac{(\sqrt2-1)c_0}
 {32\cdot1024\cdot81\cdot2000^4}\,Xq^2                 \tag{16}
\]

for every sufficiently large integer d. There are only finitely
many uniform onset conditions above, so their maximum is one
absolute existential onset. No numerical onset is certified.

Finally, C019u (4),(5) match (1) with exactly the denominator
sqrt(k), so the squared diagonal weight is 1/k. The full norm
adds the real signed unequal-index integral to the full diagonal,
including its nonnegative low block. It need not dominate either
diagonal block. Also I_V<=16 mathscr J_d cannot be reversed.
These two checks retain the stop on separate O(X) diagonal payment
and prohibit treating (16) as a disproof of M2 or RH. This audit
establishes the reliability of that local obstruction; it does not
claim a stronger asymptotic order or a result beyond the checked
sources. The actual-P transfer and the other quartic channels
remain outside this audit.

## Mathlib

Full matching coverage is unchecked. Finite Dirichlet convolution,
unique factorization, finite Euler products, the elementary factorial
and logarithmic inequalities, and the prime number theorem support
this argument; they are not a claimed formalization of the moving-heat
diagonal or M2. No absence or formal-verification claim is made.
