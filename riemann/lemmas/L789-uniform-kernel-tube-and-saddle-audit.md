# Lemma 789: restricted kernel tubes and analytic full-saddle continuation

## Hypotheses

Let
\[
 \Phi(u)=\sum_{n\ge1}\Phi_n(u),\quad
 \Phi_n(u)=\pi n^2e^{5u}(2\pi n^2e^{4u}-3)e^{-\pi n^2e^{4u}},
\]
\[
 B(u)=2\pi e^{4u},\quad
 H(u)=B(u)-\frac92-\frac6{B(u)-3},\quad K(u)=uH(u).
\]
For a tube write T(x_0,nu)={u:Re(u)>=x_0, |Im(u)|<=nu}.
The general tube assertion below requires x_0>=0,
0<=nu<pi/8, X=exp(4x_0), 2pi X>3 and
q=16 exp(-3pi X cos(4nu))<1. In the saddle assertions fix an
integer k>=10^9 and D_k={z:|z-k|<=k/20}.

No real-saddle existence, tube estimate, phase-derivative bound,
coefficient positivity or RH hypothesis is assumed.

## Conclusion

On each qualified tube, R=Phi/Phi_1-1 is well defined and
\[
 |R(u)|\le\sum_{n\ge2}\frac{|\Phi_n(u)|}{|\Phi_1(u)|}
 \le\frac{2\pi X+3}{2\pi X-3}\frac{q}{1-q}.                 \tag{1}
\]
With nu=1/10, the following strict uniform bounds hold:
\[
 \begin{array}{c|c|c}
 x_0&\text{proved upper bound for }|R|&\text{required bound}\\
 3/10&6.548\,10^{-12}&11\,10^{-12}\\
 7/20&1.054\,10^{-14}&11\,10^{-15}\\
 2/5&4.166\,10^{-18}&10^{-15}.
 \end{array}                                               \tag{2}
\]
The larger tube includes the complete circles used in L788; its required
bound is 11/10^12, not 11/10^13.

There is exactly one positive real u_k with K(u_k)=k, and
\[
 1<u_k<\frac{\log k}{4},\quad B_0=B(u_k)>300,\quad
 \frac{21}{25}B_0<H_0:=H(u_k)<B_0,\quad k=u_kH_0.           \tag{3}
\]
On the complete disk |u-u_k|<=1/20,
\[
 K'(u_k)>4k,\qquad |K''(u)|<\frac{555}{14}k<60k.            \tag{4}
\]
For every z in D_k the principal equation K(u)=z has exactly one
zero in this disk, counted with multiplicity, and it lies in
|u-u_k|<3/200.

The full phase Psi_z(u)=2z Log(u)+log(Phi(u)) has exactly one
saddle u_s(z) in |u-u_k|<=1/20, with
\[
 |u_s(z)-u_k|<3/200.                                       \tag{5}
\]
Both saddle branches are holomorphic on an open neighborhood of D_k.
The log(Phi) branch is analytic on the interior of T(7/20,1/10)
and agrees with the real logarithm on its positive real interval.
The full map is
\[
 K_\Phi(u)=K(u)-\frac u2\frac{R'(u)}{1+R(u)},\qquad
 |K_\Phi(u)-K(u)|<7\,10^{-15}k                             \tag{6}
\]
throughout the full control disk. Neither branch is defined by an
assumed consequence of L788.

These are reproductions of the required restricted claims in
W. Michałowski, *An explicit uniform cubic wedge for consecutive
Toeplitz minors of the Riemann xi-coefficients*,
[arXiv:2607.16795v1, Section 3](https://arxiv.org/html/2607.16795v1#S3),
18 July 2026, (5), Lemmas3.1–3.3 and the opening real data of
Lemma3.5's proof. Numbering binds to v1. The small-strip and q<1
restrictions are essential to this proof; no assertion for other
cosine-positive bands or the source's full k>=16 range is made.
The source's ancillary enclosures are not imported or replayed.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-11-05-uniform-moment-tube-saddle-audit.md`.
The purpose of this reproduction is to discharge the explicit
tube/real/full-saddle inputs, including domain and constant checks.
The standard inputs are geometric summation, Cauchy's derivative
estimate, Rouché's theorem (zeros counted with multiplicity), and
the holomorphic implicit function theorem. For the latter see
A. Waldron, *Complex Manifolds*, spring2020,
[Theorem2.5.6, printed p.36](https://people.math.wisc.edu/~awaldron3/Notes/Complexnotes20.pdf#page=36).
Their hypotheses are verified below. No phase-derivative conclusion
or theorem about the moment transform is used.

### Tube estimate on its complete domain

On a compact subset of |Im(u)|<pi/8, Re(e^(4u)) has a positive
minimum. Every differentiated summand is bounded there by
C n^N exp(-c n^2), with c>0 and finite C,N depending on the compact
set and derivative order. The series and all differentiated series
therefore converge normally. In particular Phi is holomorphic in
this strip. On a qualified tube |B|>=2pi X>3, so Phi_1 is nonzero
and R is analytic in a neighborhood of every tube point.

Write a=2pi e^(4x) and c=cos(4y). The strip restriction gives
c>=cos(4nu)>0 on the whole tube, and
|B-3|>=a-3. Thus for n>=2,
\[
 \frac{|\Phi_n(x+iy)|}{|\Phi_1(x+iy)|}
 \le\frac{n^4a+3n^2}{a-3}
       e^{-\pi(n^2-1)e^{4x}\cos(4y)}
 \le n^4\frac{2\pi X+3}{2\pi X-3}
       e^{-\pi(n^2-1)X\cos(4\nu)}.                         \tag{7}
\]
For the second inequality, the first rational expression decreases
with a>3: its derivative is -3(n^4+n^2)/(a-3)^2. Also n^2<=n^4
and the exponential decreases as e^(4x)cos(4y) increases. For n>=2,
n^2-1>=3(n-1) and n^4<=16^(n-1). The latter follows from equality
at n=2 and successive ratios ((n+1)/n)^4<=81/16<16.
Summing the geometric series proves (1), using q<1 explicitly.

Here is a reproducible rational verification of (2); it requires no
floating point or omitted numerical optimization. Put
\[
 p=223/71<\pi,\quad
 c_* =1-\frac{(2/5)^2}{2}+\frac{(2/5)^4}{24}
                    -\frac{(2/5)^6}{720}<\cos(2/5),\quad
 P_N(t)=\sum_{j=0}^N t^j/j!.
\]
The pi bound is the classical Archimedean bound; the cosine inequality
is the alternating Taylor bound at 2/5. At x_0=3/10,7/20,2/5,
respectively, choose
\[
 X_* =33201/10000,\quad40551/10000,\quad49530/10000.
\]
In each case P_20(4x_0)>X_*, so X>X_*. Set
a_*=2pX_*, t_*=3pX_*c_*, m=floor(t_*/4), d=t_*-4m, and
\[
 Q=\frac{16}{P_{16}(4)^mP_{16}(d)},\qquad
 M=\frac{a_*+3}{a_*-3}\frac{Q}{1-Q}.                       \tag{8}
\]
All t_* and d are positive here; P_N(t)<e^t for t>0 gives q<Q.
Every Q<1. The prefactor decreases with its argument and Q/(1-Q)
increases, so (1)'s bound is strictly below M. Exact rational
evaluation of (8) gives, respectively,
\[
 M<6.54738941\,10^{-12},\quad
 M<1.05370862\,10^{-14},\quad
 M<0.00416548\,10^{-15},                                  \tag{9}
\]
which implies every comparison in (2).

On U={Re(u)>3/10, |Im(u)|<1/10}, one has
Re(B)>=2pi exp(6/5)cos(2/5)>3 (even pi>3, exp(6/5)>3 and
cos(2/5)>9/10 suffice). By (2), |R|<1 on U. Hence
\[
 \log\Phi(u)=\log\pi+5u+\operatorname{Log}(B-3)-B/2
                         +\operatorname{Log}(1+R(u))       \tag{10}
\]
is an analytic branch there: use the principal logarithm on the
right half-plane for B-3, and its power series for log(1+R).
On the real interval every summand is positive and Phi_1>0, so
(10) agrees with the real logarithm. This also proves the required
nonvanishing and normalized branch on the smaller tube interior.

### Real initialization without circular saddle data

For real u>=1, B(u)>300: pi>3 and P_7(4)>50 suffice. For B>300,
\[
 \frac{H}{B}=1-\frac{9}{2B}-\frac6{B(B-3)}
 >1-\frac9{600}-\frac6{300\cdot297}>\frac{21}{25}.          \tag{11}
\]
Also H<B, and
\[
 H'=4B+\frac{24B}{(B-3)^2}>4H>0.
\]
Consequently K'=H+uH'>0 on [1,infinity), and K tends to infinity.
The elementary bound e<3 gives K(1)<2pi e^4<8*81=648<10^9.
For 0<u<=1, H(u)<B(u), so K(u)<uB(u)<=2pi e^4<10^9;
this argument does not assume H positive near zero. The intermediate
value theorem and monotonicity now give exactly one positive root
K(u_k)=k, with u_k>1.

Let v=(log k)/4. Since k>=10^9>e^4, v>1. At this point
B(v)=2pi k, and (11) gives K(v)>(21/25)2pi k>k.
Monotonicity implies u_k<v. This proves (3), and at the root
K'(u_k)=H_0+u_kH'(u_k)>4u_kH_0=4k.

### Complete principal control disk

If |u-u_k|<=1/20, then
\[
 |B|<\frac54B_0,\qquad
 |B-3|\ge e^{-1/5}B_0-3>
                  (4/5-3/300)B_0>\frac7{10}B_0.            \tag{12}
\]
Use e^(1/5)<1/(1-1/5)=5/4 and e^(-1/5)>4/5.
The pole B=3 is therefore absent in a neighborhood of the whole
disk. Differentiating explicitly,
\[
 H'=4B+\frac{24B}{(B-3)^2},\qquad
 H''=16B+\frac{96B}{(B-3)^2}-\frac{192B^2}{(B-3)^3}.
\]
By (12) and B_0>300,
\[
 \frac{|H'|}{B_0}
 <5+\frac{24(5/4)}{(7/10)^2\,300^2}<5.001<51/10,
\]
\[
 \frac{|H''|}{B_0}
 <20+\frac{96(5/4)/(7/10)^2+192(5/4)^2/(7/10)^3}{300^2}
 <20.013<22.
\]
Since K''=2H'+uH'', u_k>1 and H_0>(21/25)B_0,
\[
 \frac{|K''|}{k}
 <\frac{2(51/10)+22(u_k+1/20)}{(21/25)u_k}
 <\frac{10.2+22(21/20)}{21/25}=\frac{555}{14}<60.           \tag{13}
\]
This controls every point of the disk, not just its center or boundary.

Taylor's formula integrated on the segment from u_k to u gives
|K(u)-k-K'(u_k)(u-u_k)|<=30k|u-u_k|^2. On a circle
|u-u_k|=r, compare K(u)-z with the linear function K'(u_k)(u-u_k).
For |z-k|<=k/20 the latter has modulus >4kr, while the error is
at most k(30r^2+1/20). At r=1/20 these bounds are 0.2k and
0.125k; at r=3/200 they are 0.06k and 0.05675k. They are
strictly separated. All functions are holomorphic near both closed
disks. Rouché's theorem gives exactly one zero counted with
multiplicity in each disk, and no boundary zero. It is the same
zero, is simple, and has distance strictly less than 3/200.

### Full saddle, branches and the parameter boundary

For every point of the control disk its entire radius1/25 Cauchy
circle is within |u-u_k|<=9/100, hence Re(u)>91/100 and
|Im(u)|<=9/100. This lies strictly inside T(7/20,1/10), where
R is analytic and |R|<rho:=11/10^15. Cauchy's estimate gives
\[
 |R'|\le25\rho,\qquad
 \left|\frac{R'}{1+R}\right|\le\frac{25\rho}{1-\rho}.       \tag{14}
\]
To bound the factor u, note k-5log k-1 increases for k>=10^9.
At k=10^9 it is positive since log(10)<3 implies
5log(10^9)+1<136<10^9. Thus u_k+1/20<log(k)/4+1/20<k/20.
The control disk also excludes u=0. Differentiating (10) gives
\[
 \Psi_z'(u)=\frac2u\bigl(z-K_\Phi(u)\bigr),\qquad
 K_\Phi=K-\frac u2\frac{R'}{1+R}.
\]
It follows throughout the disk that
\[
 \frac{|K_\Phi-K|}{k}
 <\frac1{40}\frac{25\rho}{1-\rho}
 <6.87500001\,10^{-15}<7\,10^{-15}.                        \tag{15}
\]
This verifies (6) directly, without using a derivative bound for Psi
or either lemma whose inputs are being checked.

Repeat each Rouché comparison with K_Phi(u)-z. The errors become
at most (0.125+7*10^-15)k<0.2k and
(0.05675+7*10^-15)k<0.06k. There is exactly one zero counted
with multiplicity, and therefore a simple zero, inside both disks.
Because u!=0, the phase has exactly the same saddles as these zeros.

For completeness these same comparisons still hold on the open
parameter disk |z-k|<51k/1000: the two errors are bounded by
(0.126+7*10^-15)k<0.2k and
(0.05775+7*10^-15)k<0.06k. The principal map obeys the same
bounds with its perturbation omitted. At every parameter value,
the simple-zero count gives a nonzero u-derivative. The holomorphic
implicit function theorem supplies a local branch. Any overlapping
branches coincide, because each value is the unique zero in the
control disk. They patch to a holomorphic branch on this larger open
parameter disk. This proves holomorphy across the entire boundary
of D_k, not merely a germ at k or an interior assertion.
Complex conjugation and uniqueness also make the branches real
for real z in the disk. The full saddle at z=k need not equal u_k;
u_k initializes the first-summand map only.

All scalar comparisons in (8)–(9), (11)–(15) and the Rouché budgets
are checked exactly by
`python3 scripts/complex-moment-audit/tube-saddle-470.py`.
The full rational certificate is
`scripts/complex-moment-audit/tube-saddle-470.json`.
The proof of the full-domain reductions and analytic branches is the
argument above; the scalar certificate does not replace it. The first
run used a mistakenly transcribed larger-tube threshold 11/10^13;
that failed output is preserved in
`scripts/complex-moment-audit/tube-saddle-470-initial-threshold-error.json`.
The actual L788 threshold 11/10^12 is met. No source inequality was
weakened to conceal a failed check.

This discharges the needed restricted premises, not a coefficient-sign
theorem. The conditional downstream proofs remain in their own files.
The saddle action, growing-order Taylor estimate, remaining wedge gates,
bounded k/r region and all-degree mixed positivity are not conclusions
of this audit. No original result beyond the checked source claims is
asserted; tighter intermediate margins only verify those claims locally.

## Mathlib

Full matching coverage is not checked. No formal theorem for these
specific theta-tube constants or this saddle continuation is asserted.
Geometric series, Cauchy estimates, Rouché's theorem and the holomorphic
implicit function theorem are supporting named mathematical inputs;
library availability alone would not verify the explicit estimates here.
