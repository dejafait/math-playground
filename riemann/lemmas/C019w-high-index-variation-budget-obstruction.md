# C019w — The exact high-index variation budget is too large

## Hypotheses

Retain exactly C019p/u's fixed actual-Jensen setup, with d tending
through positive integers and

\[
 d=\frac{T}{2\pi}(\log(T/(2\pi))-1),\quad T>2\pi e,
 \quad X=T/\sqrt{2d},\quad q=\log X,\quad h=3\pi/q,
\]
\[
 D=[X,\sqrt2X-h],\quad L=\lfloor X^{1/1000}\rfloor,
 \quad \ell=\log L,\quad R=L^4,\quad
 \omega(n)=\log(L/n)/\ell\quad(1\le n\le L).
\]

Use the real Euler-product coefficients alpha of zeta(s)^(-1/2)
on Re(s)>1, so alpha(1)=1 and alpha(p)=-1/2 for a prime p.
There is no evaluation of that reciprocal on the critical line.
Write M(Y)=sum_(n<=L) alpha(n) omega(n) n^(-1/2-iY), and define
the exact c_r by

\[
 (M(Y)M(Y+h))^2=\sum_{r\le R}c_r r^{-1/2-iY}.
\]

For Z in J=[X,sqrt(2)X], retain both actual heat times and floors:

\[
 t(Z)=Z^2/(2d),\quad u(Z)=\tfrac12\log(Z/(2\pi)),\quad
 N(Z)=\left\lfloor\sqrt{Z/(2\pi)+Z^2/(32d)}\right\rfloor,
 \quad N_*=N(\sqrt2X),\quad Z_*=N_*^2R,
\]
\[
 E_n(Z)=\exp\{t(Z)((u(Z)-\log n)^2-\pi^2/16)/4
                      +i(\pi/8)t(Z)(u(Z)-\log n)\}.
\]

If rho_n solves rho_n/(2*pi)+rho_n^2/(32d)=n^2, use exactly
C019u (4), not an unrestricted convolution:

\[
 G_k(Y)=\sum_{\substack{m,n\le N_*;\ a\le R\\mna=k}}
 c_a n^{-ih}E_m(Y)E_n(Y+h)
 \mathbf1_{\{Y\ge\max(\rho_m,\rho_n-h)\}},
 \qquad \mathcal B_k=\sup_D|G_k|+\operatorname{Var}_D(G_k).
                                                               \tag{1}
\]

All conclusions have an absolute existential onset. No RH,
random-law, nonvanishing, or ordinary-to-heat moment input is used.

## Conclusion

There is an absolute c>0 such that, for every sufficiently large d,

\[
 \inf_{Y\in D}\sum_{L<k\le Z_*}|G_k(Y)|^2
       \ge \frac{cXL}{q^2\ell^3},\qquad
 \sum_{L<k\le Z_*}\mathcal B_k^2
       \ge \frac{cXL}{q^2\ell^3}.                         \tag{2}
\]

Consequently the second sufficient budget proposed in C019u (8)
is impossible, even for the high-index block alone:

\[
 \frac{(1+\log Z_*)\sum_{L<k\le Z_*}\mathcal B_k^2}{X}
       \ge c\frac{L}{q^4}\longrightarrow\infty.          \tag{3}
\]

This is an obstruction to that sufficient estimate, not a lower
bound for its actual off-diagonal integral. It does not refute
the high-index time norm, the full grouped norm, the real-pair
moment I_V, or the actual-Jensen moment I_P at scale O(X).
In particular (2) is an *unweighted* coefficient sum; it does not
show that the diagonal with weight 1/k is too large. C019v's
low-index bound remains unaffected. C019t's transfer and the
inherited conceptual audit qualifications remain as recorded.

The result is a local elementary obstruction under unchanged
assessment1402, classified as reproduction, without a claim of
progress beyond the literature checked. It has not received a
separate critical audit. No sign-density, root-count or RH result
is asserted.

## Proof

### Counting input and exact range

Import the standard named prime number theorem (Hadamard and
de la Vallee Poussin, 1896), in the form pi(x)~x/log x. A precise
reference for this form is the first term of
[NIST DLMF 27.12.4](https://dlmf.nist.gov/27.12.E4), inspected
18 November 2026. Only this qualitative unconditional asymptotic
is used. For fixed 0<a<b it gives

\[
 \#\{p\text{ prime}:ay\le p\le by\}
       \sim (b-a)y/\log y\quad(y\longrightarrow\infty).
                                                               \tag{4}
\]

Indeed log(ay),log(by)=log y+O(1); subtract the two prime-counting
asymptotics, whose errors are o(y/log y). Including endpoints
changes the count by at most two. No shrinking interval or
arithmetic progression estimate is involved. This named theorem
is imported rather than reproved; no RH-strength error term is used.

Let P_X be the primes in [sqrt(X)/10,sqrt(X)/5], and let R_L
be the primes in [L/4,L/2]. C019u's scale relations give

\[
 d\asymp X^2q^2,\quad N_*\asymp\sqrt X,\quad
 t(Z)=O(q^{-2})\quad(Z\in J),\quad
 \ell=q/1000+o(1),\quad L\longrightarrow\infty.
                                                               \tag{5}
\]

Here ell follows directly from L=floor(X^(1/1000)). Also
N(X)>=floor(sqrt(X/(2*pi))), so every p in P_X is at most
N(X) eventually. Increasing the onset if needed, for p,p' in
P_X and r in R_L we have

\[
 p>R,\quad pr>N_*,\quad pp'>N_*,\quad r\le L.
                                                               \tag{6}
\]

For clarity, p/R>=X^(1/2-1/250)/10 tends to infinity;
pr>=sqrt(X)L/40 while N_*=O(sqrt X); and pp'>=X/100.
These prove all three exclusions in (6), uniformly in the primes.

### An isolated, noncancelling coefficient

Choose distinct p_1,p_2 in P_X and r in R_L, and put k=p_1p_2r.
In any nonzero summand of (1), the index a<=R cannot contain
either p_j by (6). Hence p_1,p_2 must divide mn. They cannot
both divide m or both divide n, since p_1p_2>N_*. Neither m
nor n can also contain r, since p_j r>N_*. As k is squarefree,
the only possibilities are

\[
 (m,n,a)=(p_1,p_2,r)\quad\hbox{or}\quad(p_2,p_1,r).
                                                               \tag{7}
\]

Both source primes have already entered at Y=X. Monotonicity of
N gives both entry indicators exactly one everywhere in D, for
both assignments and for their own shifted floors. Thus no jump
or discarded contribution can cancel (7).

At the prime r, exactly one of the four mollifier factors supplies
r. The other three supply 1, whose taper is omega(1)=1. Two
copies are unshifted and two shifted. Therefore, using alpha(r)=-1/2,

\[
 c_r=-\omega(r)(1+r^{-ih}),
\]
\[
 G_{p_1p_2r}(Y)=c_r\{p_2^{-ih}E_{p_1}(Y)E_{p_2}(Y+h)
                  +p_1^{-ih}E_{p_2}(Y)E_{p_1}(Y+h)\}.
                                                               \tag{8}
\]

This is an equality of the original truncated coefficients.
For p in P_X and Z in J,

\[
 u(Z)-\log p=\tfrac12\log((Z/X)/(2\pi))
                                  -\log(p/\sqrt X)=O(1).
\]

Combining this with (5) in the exact definition of E gives
E_p(Z)=1+O(q^(-2)), uniformly including Z=Y and Z=Y+h.
The shift has the fixed, common limiting phase

\[
 p^{-ih}=\exp\{-i(3\pi/q)(q/2+\log(p/\sqrt X))\}
       =i\{1+O(q^{-1})\}.                                \tag{9}
\]

The two terms in braces in (8) consequently sum to
2i+O(q^(-1)), uniformly in Y,p_1,p_2. Their modulus is at least
1 eventually. This uses the actual shift and each actual heat
time; it does not identify the two heat times.

Since r<=L/2, omega(r)>=log(2)/ell. Also
0<=h log r<=3*pi/1000, and hence
|1+r^(-ih)|=2|cos(h log r/2)|>=1. Equation (8) proves

\[
 \inf_{Y\in D}|G_{p_1p_2r}(Y)|\ge\frac{\log 2}{\ell}.
                                                               \tag{10}
\]

### Count distinct indices and compare with the required budget

The two prime intervals are disjoint eventually. Unique prime
factorization shows that different r and different unordered pairs
{p_1,p_2} give different k. All these indices occur in (1), since
p_j<=N(X)<=N_* and r<=L<=R. They lie in the high block, as

\[
 XL/400\le k\le XL/50,\qquad L<k\le Z_*
\]

eventually. Applying (4) at y=sqrt X and y=L gives absolute
positive lower bounds

\[
 |P_X|\ge c_1\sqrt X/q,\qquad |R_L|\ge c_2 L/\ell,
\]
\[
 \binom{|P_X|}{2}|R_L|\ge c_3 XL/(q^2\ell).             \tag{11}
\]

Here |P_X| tends to infinity, so choose(|P_X|,2)>=|P_X|^2/4
eventually. Sum the square of (10) over these distinct indices.
This proves the first inequality of (2), uniformly in Y; the
second follows from B_k>=sup_D|G_k|.

Finally N_*^2 is comparable to X, R=L^4, and ell=q/1000+o(1).
Thus log Z_*=q+4ell+O(1) is comparable to q. Multiplying (2)
by (1+log Z_*)/X gives at least cL/(q ell^3)>=c'L/q^4.
Since L is asymptotic to X^(1/1000), L/q^4 tends to infinity.
This proves (3), with an existential onset uniform over the
integer d sequence. There is no numerical or effective-onset claim.

C019u (8) bounds the absolute off-diagonal by a positive expression
in the B_k. Its largeness does not make that off-diagonal large:
the implication cannot be reversed. Nor does (2) control the
weighted diagonal from below at a growing normalized scale, since
the indices isolated here have size comparable to XL. The only
closed route is payment of C019u's *global unweighted variation
budget*. Direct signed integration and the weighted diagonal remain
independent possible steps for the unchanged full M2 target.

The explicit calculation is needed because the earlier absolute
d_4 envelope is only an upper estimate and could not rule out its
sufficient budget. The local search reviewed C019p/u/v and
stops1403/1405; no earlier exact-budget lower bound was identified.
Assessment1402's ordinary moment sources are not applications to
(8), and no assertion of novelty follows from that comparison.

## Mathlib

Full matching coverage is unchecked. Unique factorization, finite
Dirichlet convolution, elementary exponential bounds and the prime
number theorem are supporting inputs, not a claimed formalization
of this moving-heat budget obstruction. Mathlib coverage of the
prime number theorem itself was not checked in this step. No
absence claim is made.
