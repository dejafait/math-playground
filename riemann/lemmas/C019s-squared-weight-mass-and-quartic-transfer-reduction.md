# C019s — Squared weight mass and an incomplete quartic transfer

## Hypotheses

Use exactly C019m/p's P,V,d,T,X,q,B,h,J,D,t,N,a_n,f_n and
positive actual-Jensen normalization. Thus d tends through positive
integers, d=(T/(2*pi))(log(T/(2*pi))-1), T>2*pi*e,
X=T/sqrt(2d), q=log X, B=(sqrt(2)-1)X, h=3*pi/q,
J=[X,sqrt(2)X] and D=[X,sqrt(2)X-h]. Every shifted reference
retains its own heat time and true source floor. All estimates are
beyond one absolute existential integer onset.

Retain L=floor(X^(1/1000)), K=L^2, the Euler-product coefficients
alpha of zeta(s)^(-1/2) on Re(s)>1, and the linear taper
omega(n)=log(L/n)/log L. With C019p's b_k, write

\[
 H(Y)=M(Y)M(Y+h)=\sum_{k\le K}b_k k^{-1/2-iY},\qquad
 W(Y)=|H(Y)|^2,\qquad R=K^2=L^4,
\]
\[
 c_r=\sum_{uv=r;\ u,v\le K}b_ub_v,\qquad
 H(Y)^2=\sum_{r\le R}c_r r^{-1/2-iY}.                       \tag{1}
\]

There is no RH, nonvanishing, simplicity, critical-line reciprocal
or random-law hypothesis. All polynomial products are finite. The
covered target is exactly assessment1402's fixed M2; this is a partial
calculation, not a changed mollifier or a proved M2 theorem.

## Conclusion

Put \(\mathcal H=\int_D W^2\). Then

\[
 \left|\mathcal H-|D|\sum_{r\le R}\frac{|c_r|^2}{r}\right|
 \le16R^2(1+\log R),\qquad
 \mathcal H\le |D|(1+\log R)^4+16R^2(1+\log R)
             =O(Xq^4).                                    \tag{2}
\]

Define the still-unbounded reference quantities

\[
 I_V=\int_D V(Y)^2V(Y+h)^2W(Y)^2\,dY,\qquad
 E_j=\int_D V(Y+j)^2W(Y)^2\,dY\quad(j=0,h),
\]

and let \(I_P\) denote the same quartic integral as \(I_V\)
with both V factors replaced by P. There is an absolute
\(\epsilon\le C/q\) with \(\sup_J|P+V|\le\epsilon\), and

\[
 \|\{PP_h-VV_h\}W\|_{L^2(D)}
 \le\epsilon(\sqrt{E_0}+\sqrt{E_h})+
                       \epsilon^2\sqrt{\mathcal H},         \tag{3}
\]
\[
 I_P\le4I_V+4\epsilon^2(E_0+E_h)+4\epsilon^4\mathcal H
      \le4I_V+Cq^{-2}(E_0+E_h)+CX.                         \tag{4}
\]

In particular the pure comparison-error contribution is paid at
O(B), without a higher norm hypothesis on P+V. A sufficient remaining
payment is I_V=O(X) and E_0+E_h=O(Xq^2). Neither bound is proved.
C019r's squares weighted by W are not these E_j.

The proof also records the exact sixteen-channel quartic expansion,
with all entry intervals, and its derivative scales. Applying only
the separately available second-derivative estimate to the ten
nonbalanced channels gives the inadequate upper bound
O(X^(3/2+1/250)q^2). The six balanced channels do not inherit the
pair calculation's uniform nonresonant first-derivative separation
from its integer-gap comparison. These are limitations of the tested
estimates, not lower bounds for I_V or I_P, and do not refute M2.
Density, root selection, bulk separation and RH remain open. This
first partial derivation has not had an independent conceptual audit.

## Proof

### Coefficients, diagonal and the complete weight error

C019p proves |b_k|<=1 from the finite taper and the prime-power
coefficients of alpha; that coefficient bound is used unchanged.
Consequently |c_r|<=tau(r), where tau is the divisor function.
Pairing divisors gives tau(r)<=2sqrt(r), including r=1.
If d_4 counts ordered factorizations into four positive integers,
then tau(r)^2<=d_4(r). Indeed both sides are multiplicative, and
at a prime power p^e the inequality is
(e+1)^2<=binom(e+3,3). For e=0 it is equality; for e>=1 it
reduces to e(e-1)>=0. Thus

\[
 \sum_{r\le R}\frac{|c_r|^2}{r}
 \le\sum_{r\le R}\frac{d_4(r)}r
 =\sum_{r_1r_2r_3r_4\le R}\frac1{r_1r_2r_3r_4}
 \le\left(\sum_{r\le R}\frac1r\right)^4
 \le(1+\log R)^4.                                         \tag{5}
\]

Expanding |H^2|^2 and integrating every term gives the diagonal
in (2). For r!=s the elementary antiderivative gives
|integral_D exp(iY log(s/r))dY|<=2/|log(s/r)|.
Since |c_r|/sqrt(r)<=2, the absolute off-diagonal error is at most

\[
 16\sum_{1\le r<s\le R}\frac1{\log(s/r)}
 \le16\sum_{s=2}^R s\sum_{j=1}^{s-1}\frac1j
 \le16R^2(1+\log R).                                      \tag{6}
\]

Here log(s/r)>= (s-r)/s follows by integrating 1/x from r to s.
This proof needs no mean-value theorem with unchecked coefficient
hypotheses and makes no cancellation claim for c_r. The diagonal
estimate (5) and (6) prove the explicit inequalities (2).
Because R<=X^(1/250), its off-diagonal bound is
O(X^(1/125)q)=o(X), while 1+log R=O(q). Also |D|<=B=O(X).
These facts prove the final bound in (2), uniformly for the actual
integer L and without a continuous-cutoff replacement.

### What the actual-Jensen comparison does and does not pay

C019m (8),(19) give S_d+V=O(X^(-3/4)) and
P-S_d=O(1/q) uniformly on the closed J, including every source
entry. Therefore e=P+V has sup norm at most epsilon=C/q after
one increase of the onset. Since Y,Y+h belong to J for Y in D,

\[
 (PP_h-VV_h)W=(-eV_h-Ve_h+ee_h)W.                           \tag{7}
\]

The L2 triangle inequality, and the pointwise bound on each error
factor, prove (3). Alternatively expand PP_hW into its four terms
VV_hW, -eV_hW, -Ve_hW, ee_hW. The elementary inequality
|z_1+z_2+z_3+z_4|^2<=4 sum |z_i|^2 and integration prove the
first inequality (4). Equation (2) then gives

\[
 \epsilon^4\mathcal H
 \le Cq^{-4}\{X(1+\log R)^4+R^2(1+\log R)\}=O(X).         \tag{8}
\]

This is a bound for the actual pure-error contribution, not a claim
that its size is asymptotic to X or tends to zero relative to X.
No division by a reference value has occurred. In particular an
unproved higher weighted norm of e has not been assumed. The first
unpaid comparison term in this argument is epsilon^2(E_0+E_h).
Equation (4) is a sufficient upper-bound route only; it does not
claim those separate conditions are necessary for M2.

### Exact reference quartic and all moving entry intervals

Set N_*=N(sqrt(2)X), b=sqrt(2)X-h. For each positive n let
rho_n be the positive solution of Y/(2*pi)+Y^2/(32d)=n^2.
The defining function is strictly increasing. For a tuple
bold n=(n_1,n_2,n_3,n_4), with every n_i<=N_*, its exact domain is

\[
 I_{\bold n}=[\max(X,\rho_{n_1},\rho_{n_2},
                     \rho_{n_3}-h,\rho_{n_4}-h),b],         \tag{9}
\]

empty when the left endpoint exceeds b. Singletons contribute zero.
Use Z_1=Z_2=Y, Z_3=Z_4=Y+h and
A_bold n(Y)=product_{i=1}^4 a_(n_i)(Z_i). For
bold epsilon in {+1,-1}^4 put

\[
 F_{\bold n,\bold\varepsilon,r,s}(Y)
    =\sum_{i=1}^4\varepsilon_i f_{n_i}(Z_i)
                                  +Y\log(s/r).
\]

The exact finite identity is

\[
 I_V=\sum_{r,s\le R}\frac{c_r\overline{c_s}}{\sqrt{rs}}
       \sum_{n_1,n_2,n_3,n_4\le N_*}
       \sum_{\bold\varepsilon\in\{+1,-1\}^4}
       \int_{I_{\bold n}} A_{\bold n}(Y)e^{iF(Y)}\,dY.       \tag{10}
\]

This follows directly from 2cos f=e^(if)+e^(-if) in each V,
and (1). No factor 2 is lost: each V is already twice its cosine
sum. Terms are paired with their complex conjugates in the total,
which is real and nonnegative; individual channels need not be.
Both own times and both source floors are preserved in (9)-(10).

### The tested oscillatory bounds and their actual thresholds

Write c_0=pi/8, u(Z)=log(Z/(2*pi))/2 and
v_n(Z)=u(Z)-log n. Differentiating the explicit C019m (7)
phase, not an asymptotic remainder, gives exactly

\[
 f_n'(Z)=v_n(Z)(1+c_0Z/d)+c_0Z/(4d),\qquad
 f_n''(Z)=1/(2Z)+(c_0/d)(v_n(Z)+3/4).                      \tag{11}
\]

On J and for n<=N_*, |v_n|=O(q). C019m (9) also gives
sup |a_n|<=C/sqrt(n) and sup |a_n'|<=C/(X sqrt(n)),
even before entry. Thus on every (9)

\[
 \sup |A_{\bold n}|+\int_{I_{\bold n}}|A_{\bold n}'|
                         \le C/(n_1n_2n_3n_4)^{1/2}.       \tag{12}
\]

For sigma=sum epsilon_i nonzero, (11) gives
F''=sigma/(2Y)+O(h/X^2+q/d). Here |sigma| is 2 or 4,
d is comparable to X^2q^2, and h=O(1/q). Hence F'' has
one sign and |F''|>=1/(4X) eventually on every entry interval.
Import the already assessed H. Koesters, *On the Occurrence of the
Sine Kernel in Connection with the Shifted Moments of the Riemann
Zeta Function*, arXiv:0803.1141v2, 5 September 2008,
[Appendix A, Lemma A.2](https://arxiv.org/html/0803.1141v2#A),
also Titchmarsh, *The Theory of the Riemann Zeta-function*, second
edition, Lemma4.4: a real twice differentiable phase with F''>=eta>0
or F''<=-eta throughout has integral bounded by 8/sqrt(eta).
Its hypotheses hold on every subinterval here. Integration against
the bounded primitive, using (12), bounds each weighted integral
by C sqrt(X)/(n_1n_2n_3n_4)^(1/2). There are ten such sign
patterns. Their aggregate absolute bound in (10) is at most

\[
 C\sqrt X\left(\sum_{n\le N_*}n^{-1/2}\right)^4
             \left(\sum_{r\le R}\frac{|c_r|}{\sqrt r}\right)^2
 \le C X^{3/2}R(1+\log R)^2
 \le C X^{3/2+1/250}q^2.                                  \tag{13}
\]

For the second inequality use N_*=O(sqrt X), and
sum_{r<=R}tau(r)/sqrt(r)
=sum_{uv<=R}1/sqrt(uv)<=2sqrt(R)(1+log R).
Compared with the required O(X), (13) loses a factor
X^(1/2+1/250)q^2. This is an upper bound only.

For completeness the other six patterns have sigma=0. Set
sigma_h=epsilon_3+epsilon_4,
A_h=epsilon_3 log n_3+epsilon_4 log n_4,
a=-sum_i epsilon_i log n_i,
eta=a+log(s/r), and delta_u=u(Y+h)-u(Y). Formula (11) gives
the exact derivative

\[
 F'=\eta+\sigma_h\delta_u+
 \frac{c_0}{d}\{Ya+Y\sigma_h\delta_u
                      +h(\sigma_h u(Y+h)-A_h)\}
                 +\frac{c_0h\sigma_h}{4d}.                 \tag{14}
\]

In particular |F'-eta|<=C/(Xq). As each sign occurs twice,
exp(eta)=U/V for positive integers U,V<=N_*^2 R.
When eta!=0, the elementary integer gap supplies only

\[
 |\eta|\ge1/(2N_*^2R),                                   \tag{15}
\]

using log(1+1/m)>=1/(m+1). This scale is of order
1/(XR), while the available upper bound for the perturbation in
(14) is of order 1/(Xq). The ratio R/q tends to infinity for
the prescribed integer L. Thus these two bounds cannot certify
|F'|>=|eta|/2 uniformly, as the shorter pair calculation could.
This does not assert that a stationary tuple actually exists or
that every possible refinement of the arithmetic gap fails.
Resonant eta=0 terms also remain present. No balanced channel,
stationary point, incomplete entry or endpoint has been discarded.

Equations (13)-(15) identify why direct termwise reuse of the pair
estimates does not close (10); a quartic arithmetic cancellation or
another genuinely stronger bound is still needed. Equation (8)
is a separate paid part of the actual-P transfer, not a replacement
for that missing reference estimate or the mixed energies in (4).
All sums and integrations in this proof are finite, and the named
standard oscillatory lemma is imported rather than reproved. The
coefficient specialization and error bookkeeping are elementary
local reproductions; no progress beyond the checked literature
or novelty certification is asserted.

## Mathlib

Full matching coverage is unchecked. The finite convolution,
divisor inequality, harmonic sum, L2 triangle/Cauchy--Schwarz and
derivatives are supporting ingredients, not a claimed formalization
of this exact moving-heat statement. No absence claim is made.
