# C020g — Joint source frequencies, multiplicity and complementary cutoffs

## Hypotheses

Use exactly C020e's finite reference model, along positive integers d:
\[
 d=\frac{T}{2\pi}(\log(T/(2\pi))-1),\quad T>2\pi e,\quad
 X=T/\sqrt{2d},\quad q=\log X,\quad B=(\sqrt2-1)X,\quad h=3\pi/q,
\]
\[
 L=\lfloor X^{1/1000}\rfloor,\quad R=L^4,\quad K=\lceil X^3\rceil,
 \quad N(Z)=\left\lfloor\sqrt{Z/(2\pi)+Z^2/(32d)}\right\rfloor,
 \quad N_*=N(\sqrt2X).
\]
The coefficients c_r have all four original linear tapers and the two
shifted factors of C019y (1); alpha is the real Euler-product coefficient
sequence of zeta^(-1/2) on Re(s)>1. No coefficient is replaced by its
untapered limit. Witness indices v=pb use the original unordered distinct
primes in [sqrt(X)/10,sqrt(X)/5]. Retain F,W,A,U,C and a_v exactly as
in C019y (1),(3)--(5), and in particular every own heat time in
\[
 E_y(Z)=\exp\{t(Z)((u(Z)-\log y)^2-\pi^2/16)/4
                    +i\pi t(Z)(u(Z)-\log y)/8\},\quad
 t(Z)=Z^2/(2d),\quad u(Z)=\tfrac12\log(Z/(2\pi)).
\]
The displayed smooth formula defines E_y for every positive real y;
using it outside a source cutoff does not extend the truncated F.

Put J=[X,sqrt(2)X], D0=[X,sqrt(2)X-h], D1=D0+h. For
n<=N*, r,s<=R and each witness v, set lambda=vr/(ns) and retain
\[
 \Omega_0(Z)=n^{ih}\mathbf1_{D0}(Z)\mathbf1_{n\le N(Z+h)}
                  \overline{E_n(Z+h)}a_v(Z),
\]
\[
 \Omega_1(Z)=\lambda^{ih}\mathbf1_{D1}(Z)\mathbf1_{n\le N(Z-h)}
                  \overline{E_n(Z-h)}a_v(Z-h),\qquad
 \Omega=\Omega_0+\Omega_1.
\]
These are C020e (1), with their different indicators intact. All sums
below include common factors, repeated source indices and zero coefficients.
No actual-P approximation, selected resonance estimate from C019y or
C020a/b, nonvanishing hypothesis or RH premise is used.

## Conclusion

Let \(\mathcal U=2\operatorname{Re}\int_{D0}W^2U\overline A\).
For 1<=l<=K define
\[
 \delta_l=\log\frac{lns}{vr},\quad
 b_l(Z)=\mathbf1_{l\le N(Z)}l^{-1/2}\overline{E_l(Z)},
 \quad I_l(Z)=\int_1^{N(Z)}y^{-1/2}E_y(Z)e^{-iZ\log y+2\pi i l y}\,dy,
\]
\[
 D_l(Z)=e^{2i\theta(Z)}l^{-iZ}I_l(Z),\qquad
 \theta(Z)=\tfrac Z2\log(Z/(2\pi))-\tfrac Z2-\pi/8.
 \tag{1}
\]
If \(\mathcal M_-\) denotes all negative modes k=-1,...,-K in
C020e's finite mixed-channel formula, then exactly
\[
 \mathcal M_-+\mathcal U
 =2\operatorname{Re}\sum_{n,v,r,s}\frac{c_r\overline{c_s}}{\sqrt{nvrs}}
   \sum_{l=1}^K\int_J e^{iZ\delta_l}\Omega(Z)
                             \{D_l(Z)+\tfrac12 b_l(Z)\}\,dZ.
 \tag{2}
\]
The factor 1/2 is necessary: the two translated descriptions of
\(\mathcal U\) are representations of the same channel, whereas
the mixed channel contains their sum. Formula (2) remains valid
after restricting both channels to the same condition on delta_l.
In particular its restriction to 0<|delta_l|<=100/X defines the exact
joint near layer \(\mathcal J_{\rm near}\).

The source saddle y0=Z/(2*pi*l) lies in [1,N(Z)] precisely when
\[
 \frac{Z}{2\pi N(Z)}\le l\le\frac{Z}{2\pi}.
 \tag{3}
\]
Its intersection with the direct support l<=N(Z) contains at most
l=N(Z), beyond one absolute onset. If that index occurs, then
\[
 0\le N(Z)-y0\le \frac{Z^2}{32dN(Z)}
                         =O(X^{-1/2}q^{-2}).
 \tag{4}
\]
Thus this is an endpoint overlap, not a common interior source range.
Nevertheless the smooth weights satisfy the exact reflection identity
\[
 E_{Z/(2\pi l)}(Z)=\overline{E_l(Z)}.                 \tag{5}
\]

The finite Gaussian decomposition (8) below makes the center term of
D_l a **positive** multiple of this reflected weight under full-Gaussian
normalization, with an exact retained remainder. It supplies no negative
pairing with b_l/2, and no sign or size estimate for the full kernel.
All rational-frequency fibers can be grouped exactly as in (9), but
their signed sum has not been bounded by o(Bq^2).

These findings stop the automatic tuplewise cancellation implementation.
They do not rule out cancellation between different factorizations in a
frequency fiber, or a paid arithmetic completion of complementary ranges.
In particular no counterexample to the requested o(Bq^2) estimate, no
quotient decision and no progress beyond the checked standard methods
are claimed. Independent audit of this result is pending.

## Proof

### 1. Check the inherited expressions used here

C019y (1),(3)--(5) and its audit1421 give the finite channel expansion.
C020c (4)--(5) retains the exact source entries: its second domain is
obtained by swapping the two sources and two mollifier indices and
then setting Z=Y+h. Its phase m^(ih) exp(-ih log(m*lambda)) is
lambda^(-ih). Conjugating the entire term inside the real part gives
lambda^(ih), the second summand of Omega. This is the justification
for C020e's two domains; no equality of complex channels is assumed.

For k=-l, multiplication of the source integral by
e^(2i*theta(Z))*lambda^(-iZ) gives e^(iZ*delta_l)*D_l exactly.
The real phase in the two variables is C020f (1); its source derivative
is -Z/y+2*pi*l and its source second derivative is Z/y^2. Thus (3)
and the orientation in (1) require no stationary-phase approximation.

The finite-Poisson input remains J.-H. Evertse, *The functional equation
for the Riemann zeta function*, Chapter 9, Section 9.1, Theorem 9.2,
printed p.128, with the endpoint proof on pp.125--127,
https://pub.math.leidenuniv.nl/~evertsejh/ant13-9.pdf (undated author
file, inspected in review1422). C020e verifies holomorphy near [1,N]
and the integer endpoints; N>=2 here eventually. Its derivative
formula f'=f A/y, f''=f(A^2-A+t/2)/y^2, with
A=-1/2-iZ-t(u-log y)/2-i*pi*t/8, gives its uniform O(X^2) derivative
budget. Pairing k and -k cancels the 1/k endpoint terms. The remaining
O(X^2/K) tail, times the outer mass O(X^(3/4)R(1+log R)^2) and
height length O(X), is O(X^(377/500)q^2)=o(B) for K=ceil(X^3).
This checks the inherited truncation used to locate (2) in the complete
channel; it does not audit C019y's selected resonance estimates.

### 2. The direct channel has two descriptions, not two copies

Direct finite multiplication gives
\[
 \mathcal U=2\operatorname{Re}\sum_{m,n,v,a,b}
 \frac{c_a\overline{c_b}\,n^{-ih}}{\sqrt{mnvab}}
 \int_{D0}\mathbf1_{m\le N(Y),\ n\le N(Y+h)}
 E_m(Y)E_n(Y+h)\overline{a_v(Y)}
            e^{iY\log(vb/(mna))}\,dY.                    \tag{6}
\]
Conjugate the entire integrand and its coefficient within the real
part, rename a=s,b=r,m=l, and put Z=Y. This expresses (6) as
2 Re of the sum in (2) with Omega_0*b_l in place of
Omega*(D_l+b_l/2). Since K>=N* eventually, extending the direct
l sum to K adds only zeros. The equality and unequal-frequency
pieces are precisely those of C019y (4)--(5); the phase has merely
been conjugated and relabeled.

Alternatively, after that conjugation call the first source n and
the second source l, and set Z=Y+h. Its shifted factor becomes
\[
 l^{ih}e^{-ih\delta_l}
       =l^{ih}\left(\frac{lns}{vr}\right)^{-ih}
       =\lambda^{ih}.                                   \tag{7}
\]
The indicators are now Z in D1, n<=N(Z-h), l<=N(Z), and the
weights are conjugate(E_n(Z-h))*conjugate(E_l(Z))*a_v(Z-h).
Consequently (6) is also 2 Re of the expression with Omega_1*b_l.
Averaging the two exact identities gives the direct part of (2).
The mixed part follows from Section 1. The product ln, and hence
delta_l, is unchanged by the source exchange, so the averaging is
valid for any restriction depending only on this rational frequency.
There is no extra factor even when l=n: each source permutation is
a bijection, not a deletion of diagonal terms.

### 3. Floors and exact heat reflection

Write a=Z/(2*pi), epsilon=Z^2/(32d) and N=N(Z). C019's audited
scales give epsilon=O(q^(-2)), N comparable to sqrt(X), uniformly
on J. Since N^2<=a+epsilon, any l in both ranges satisfies
\[
 N-\epsilon/N\le a/N\le l\le N.
\]
Eventually epsilon/N<1. Thus only l=N is possible; it occurs
exactly when a<=N^2 (the other upper constraint l<=a is automatic
eventually). If it occurs, N-a/N=(N^2-a)/N<=epsilon/N, proving
(4), including a saddle exactly at the endpoint. If N^2<a, there
is no overlap. No averaging over floors is used.

Because log(y0)=2u(Z)-log l, u(Z)-log(y0)=-(u(Z)-log l).
The square in the real part of log E is unchanged and its imaginary
linear term changes sign. This proves (5) at the same heat time;
no replacement of a factor at Z+h by one at Z is made.

### 4. An exact finite center decomposition, with its remainder

This subsection determines a coefficient sign, not an asymptotic.
For tau>0 put
\[
 w(\tau)=\operatorname{sgn}(\tau-1)
            \sqrt{2(\tau-1-\log\tau)}.
\]
It is a smooth increasing bijection onto the real line, with
w'(1)=1; this follows from the positive derivative on either side
and the Taylor expansion at 1. Write tau(w) for its inverse and
\[
 w_-=w(1/y0),\quad w_+=w(N/y0),\quad
 b(w)=\sqrt{y0}\,\tau(w)^{-1/2}E_{y0\tau(w)}(Z)\tau'(w).
\]
The phase in D_l is exactly Z*(tau-1-log tau)-pi/4.
Also b(0)=sqrt(y0)*conjugate(E_l(Z)) by (5). Therefore
\[
 \begin{split}
 D_l(Z)&=l^{-1/2}\overline{E_l(Z)}\,\mathfrak F_l(Z)
                         +\mathfrak R_l(Z),\\
 \mathfrak F_l(Z)&=e^{-i\pi/4}\sqrt{Z/(2\pi)}
                     \int_{w_-}^{w_+}e^{iZw^2/2}\,dw,\\
 \mathfrak R_l(Z)&=e^{-i\pi/4}\int_{w_-}^{w_+}
                              (b(w)-b(0))e^{iZw^2/2}\,dw.
 \end{split}                                               \tag{8}
\]
This is an exact change of variable and subtraction, valid even
when the saddle lies outside the finite interval. The classical
Fresnel integral, in its symmetric improper sense for Z>0, is
integral_R exp(iZ*w^2/2)dw=exp(i*pi/4)*sqrt(2*pi/Z).
Thus full-Gaussian normalization would make F_l equal to +1.
In (2) the exact center bracket is F_l+(1/2)*1_{l<=N}, with
R_l still present. It is not F_l-(1/2)*1_{l<=N}.

No replacement by a full Gaussian is made. F_l can be complex,
and no bound for the full outer sum of R_l is supplied. In
particular the positive normalization is not a positivity assertion
for D_l, Omega, a frequency fiber or the real height integral.

The ready smooth-interior comparison is Kıral--Petrow--Young,
*Oscillatory integrals with uniformity in parameters*, JTNB 31(1)
(2019), Definition 2.1, Main Theorem (3.1)--(3.2), pp.147--149,
Lemma 3.1, p.150; https://www.numdam.org/item/10.5802/jtnb.1072.pdf .
The corresponding arXiv:1710.00916v1 Section 3 and Section 5 expansion
were checked again for this sign comparison:
https://arxiv.org/html/1710.00916v1 . Its smooth compact support
hypotheses do not cover the whole sharp integral above. No invocation
or reproof of that stationary-phase theorem is needed for (8), and
none is used to discard its remainder or finite endpoints.

There really are near-layer tuples in the complementary dual range:
C020f's construction takes n=1,s=7, r in {4,5,6}, and
l=(vr-sigma)/7 for a sign sigma making vr congruent to sigma mod 7.
Eventually p,b>7, so such r and sign exist for every witness v.
Its elementary bounds X/175-1<l<6X/175+1 give l>N*, whereas
4<y0<45<N(Z) and 4<X|delta_l|<26. The last inequalities follow
by substituting y0=Z/(2*pi*l) and expanding log(1-sigma/(vr));
the limiting extremes are 175/(12*pi)>4 and
175*sqrt(2)/(2*pi)<45, and 25/6<=X/(vr)<=25.
The direct term b_l is zero for these same tuples on all of J.
For the use of C020f's O(B) family bound, its small-source interval
[1,80] has phase second derivative at least X/6400 and uniformly
bounded amplitude variation, so its cited second-derivative estimate
gives O(X^(-1/2)). On [80,N(Z)] the increasing phase derivative is
at least (2*pi/175-sqrt(2)/80)*X-2*pi>=cX; integration by parts
retains both endpoints and gives O(X^(-1)). There is one tuple per
v, its fixed-index coefficients and Omega are bounded, and
sum_v v^(-1/2)=O(sqrt(X)) by comparison with all integer pairs.
Multiplying these bounds by the height length O(X) verifies O(B),
uniformly through every floor crossing. Thus this support mismatch
is not a counterexample at the Bq^2 scale. Other tuples can have
the same rational frequency and are retained.

### 5. Full arithmetic grouping and the unpaid threshold

For each positive rational rho attained by lns/(vr), define the
finite coefficient function
\[
 A_\rho(Z)=\sum_{lns/(vr)=\rho}
 \frac{c_r\overline{c_s}}{\sqrt{nvrs}}\Omega_{nvrs}(Z)
                     \{D_l(Z)+\tfrac12 b_l(Z)\}.
\]
Then exactly
\[
 \mathcal J_{\rm near}
 =2\operatorname{Re}\sum_{0<|\log\rho|\le100/X}
                           \int_J e^{iZ\log\rho}A_\rho(Z)\,dZ.
 \tag{9}
\]
Every factorization, including those with common factors, is present.
The functions inside a fiber have different weights and cutoffs;
coincidence of rho alone does not make them negatives of one another.
Neither Section 3 nor the particular family just checked excludes
cancellation across these factorizations. Such a claim would require
an additional arithmetic argument, which is not provided here.

To recover the whole mixed-plus-direct observable, add the analogous
rho=1 and |log rho|>100/X pieces of (2), C020e's complete k=0,...,K
integrals, and its half-endpoint source values (f_Z(1)+f_Z(N))/2
inside the original outer expression. Then add the o(B) finite-Poisson
tail. This is a disjoint partition; both translated boundaries and
all source-entry indicators occur in every relevant piece. No part
of the direct channel is left unassigned and none is counted twice.

The required bound remains |J_near|=o(Bq^2). No bound meeting it,
nor a lower bound violating it, follows from (9). The unchanged
C020f absolute envelope is not promoted to a residual lower bound.
This is one bounded matching attempt with an exact, but unpaid,
joint expression. A further attempt would need a specified mechanism
for the full frequency fibers or a different independently testable
target; repeating a tuplewise negative-pairing assertion is unjustified.
Exact resonance, other modes/endpoints, UA, denominator and E_P remain
open. Actual-P transfer would still need C019t's C019j/k/l/s,L320,
L018/L021 contracts. There is no all-degree Xi positivity or RH candidate.

### 6. Completion test1431: the full coefficient and exact unpaid difference

18 November 2026. This is the third bounded exploration of the
near-layer completion mechanism. The following finite identities do
not establish its required error estimate. They make the completion
test explicit; neither its success nor its impossibility is asserted.

Use all the hypotheses above. For Y in D0 write
\[
 A=N(Y),\quad B_Y=N(Y+h),\quad a=Y/(2\pi),\quad a_h=(Y+h)/(2\pi),
 \qquad x_l=\mathbf1_{l\le A},\quad y_n=\mathbf1_{n\le B_Y}.
\]
B_Y is a source cutoff, not the height length B. Extend the smooth
E factors by their stipulated formula only; this does not extend F.
They are nonzero exponentials. Define, for 1<=j<=K,
\[
 Q_j(Z)=\frac{\sqrt j D_j(Z)}{\overline{E_j(Z)}}
       =\mathfrak F_j(Z)
          +\frac{\sqrt j\mathfrak R_j(Z)}{\overline{E_j(Z)}}.
 \tag{10}
\]
The equality is exactly (8), with both finite endpoints retained.

Here is a specific completed coefficient, rather than a renamed
rational-frequency fiber:
\[
 \mathscr C_k(Y)=
 \sum_{sln=k}\overline{c_s}\,n^{ih}
                 \overline{E_l(Y)}\,\overline{E_n(Y+h)}.
 \tag{11}
\]
All factors are positive integers and c_s is extended by zero for
s>R. Thus this is the full finite divisor convolution of the original
four-taper conjugate coefficient with the two indicated own-time
source sequences. In particular
\(\overline{c_s}=\sum_{a_1a_2a_3a_4=s}
\prod_j\alpha(a_j)w(a_j)(a_2a_4)^{ih}\).
There is no untapered replacement. It is not the ordinary unweighted
shifted-divisor convolution unless the heat factors are removed,
which is not justified here.

For a divisor triple sln=k put
\[
 H_{ln}(Y)=y_n Q_l(Y)+x_l Q_n(Y+h)+x_l y_n.
 \tag{12}
\]
Then the exact joint near layer is
\[
 \begin{split}
 \mathcal J_{\rm near}
 =2\operatorname{Re}\int_{D0}\sum_{v,r}
 \frac{c_r a_v(Y)}{\sqrt{vr}}
 \sum_{\substack{k\ge1\\0<|\log(k/(vr))|\le100/X}}
 \frac{e^{iY\log(k/(vr))}}{\sqrt k}
 \sum_{sln=k}\overline{c_s}\,n^{ih}
 \overline{E_l(Y)}\,\overline{E_n(Y+h)}H_{ln}(Y)\,dY.
 \end{split}                                                   \tag{13}
\]
To check finiteness and the dual-mode range, every k in (13) satisfies
\[
 k\le e^{100/X}vr\le e^{100/X}XR/25<K
 \tag{14}
\]
beyond one onset, since R<=X^(1/250). Hence every divisor l,n of k
is below K. Extending a short source index to this finite divisor
sum adds only zeros whenever its indicator occurs. No dual mode
beyond C020e's cutoff is introduced.

For the proof of (13), the Omega_0 term of (2), using (10), gives
the first term of (12) and half of its rectangle term. In the
Omega_1 term set Z=Y+h. With delta=log(lns/(vr)) and
lambda=vr/(ns), the exact phase identity is
\[
 e^{ih\delta}\lambda^{ih}=l^{ih}.
\]
Now exchange l and n. This gives the second term of (12) and the
other half of the same rectangle term. The short source now has
exactly l<=N(Y); only the direct half additionally requires
n<=N(Y+h). The dual n remains unrestricted up to K, and its Q
factor is evaluated at Y+h, not Y. Both original bands become D0 by this change of
variable, with all their entry conditions intact. The near condition depends
on ln and is unchanged by the exchange. Finally
\(\sqrt{lnvrs}=\sqrt{vr}\sqrt{k}\), proving (13) by finite
regrouping. This proves an equality of real observables; no stronger
identity between the original unconjugated complex channels is used.

Let \(\mathcal J_{\rm comp}\) be the right side of (13) with
H_{ln} replaced by 1, so its inner coefficient is (11). Let
\(\mathcal E_{\rm comp}\) be the same finite expression with
H_{ln} replaced by H_{ln}-1. Thus, exactly,
\[
 \mathcal J_{\rm near}=\mathcal J_{\rm comp}
                         +\mathcal E_{\rm comp}.
 \tag{15}
\]
This extension defines a new comparison expression, not a claim
that the original truncated source polynomials equal a full series.

Here is the complete surplus/missing-domain accounting in that error.
For either Z=Y or Z=Y+h put
\[
 S_j(Z)=\mathbf1_{Z/(2\pi N(Z))\le j\le Z/(2\pi)},\quad
 \epsilon_j(Z)=\mathfrak F_j(Z)-S_j(Z)
                 +\frac{\sqrt j\mathfrak R_j(Z)}{\overline{E_j(Z)}}.
 \tag{16}
\]
Thus Q_j=S_j+epsilon_j exactly, including saddles at endpoints
and nonstationary j. Define
\[
 o_l=x_l S_l(Y),\quad m_l=(1-x_l)(1-S_l(Y)),\qquad
 o'_n=y_n S_n(Y+h),\quad m'_n=(1-y_n)(1-S_n(Y+h)).
\]
The exact residual is
\[
 \begin{split}
 H_{ln}-1={}&-(1-x_l)(1-y_n)
              +y_n o_l+x_l o'_n-y_n m_l-x_l m'_n\\
            &+y_n\epsilon_l(Y)+x_l\epsilon_n(Y+h).
 \end{split}                                                   \tag{17}
\]
Indeed S_l=(1-x_l)+o_l-m_l, and the analogous identity holds
for S_n. Substitution in (12) gives (17). This is the elementary
hyperbola inclusion/exclusion specialized to the actual indicators.
The known method is Koukoulopoulos, *The Distribution of Prime
Numbers*, author-hosted preliminary version, Chapter 3, equations
(3.4)--(3.5), printed pp.37--39,
https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=48 .
Its finite partition is applicable to these finite weighted sums;
Theorem 3.3's divisor-count estimate for unit weights is not an
estimate for (15). The algebra above supplies the changed cutoffs
and weights, not a reproof of that divisor-count theorem. Source
coverage is reused from assessment1428/source-notes1429.

More explicitly, o_l is supported at most at l=A, and only if
A^2>=a; this is (3)--(4). The missing-arm indicator m_l is the
disjoint union
\[
 \{A<l<a/A\}\ \cup\ \{l>A,\ l>a\}.
 \tag{18}
\]
The first set contains at most the integers A+1,A+2 eventually:
from A=floor(sqrt(a+Y^2/(32d))) one has a<(A+1)^2, so
a/A<A+2+1/A<A+3 for A>=2. The second is the large-source end.
The same statements hold for o'_n,m'_n at Y+h. Strict inequalities
in (18) and inclusive inequalities in (16) retain every equality
case. Floors are never differentiated or averaged.

The first term of (17) consists of factorizations with both sources
above their respective cutoffs. It vanishes whenever ln<=A B_Y,
but the full near condition gives only ln<=e^(100/X)vr/s, with
r/s as large as R. Thus the near condition and available scale bounds
do not verify that sufficient product-domain condition for the full sum. This observation
does not assert that this term has nonzero total mass, let alone a
lower bound at the target scale. The two o terms count overlaps;
the two m terms retain the gaps and large ends. The epsilon terms
retain the entire finite-Gaussian discrepancy and amplitude remainder
at both own times. In particular neither epsilon term is set to zero
or replaced by a full-Gaussian normalization. All common factors,
zero coefficients, equality cases and source permutations remain.

The test has now specified the full four-taper coefficient and its
exact difference from the observable. It has **not** proved
\(|\mathcal E_{\rm comp}|=o(Bq^2)\), a violating lower bound, or
any adequate bound on \(\mathcal J_{\rm comp}\). A support
partition alone does not control cancellation among its signed
factorizations. Consequently this outcome is EXPLORATION, not an
advance or a negative result about the estimate. The three-attempt
completion exploration is exhausted and is parked pending materially
new quantitative input; another regrouping or absolute-envelope
repetition is not a continuation. This is a scoped stop on the
present mechanism, not a global ban on arithmetic cancellation.
The full numerator/denominator, actual-P contracts and actual-Xi
positivity remain unresolved. Independent review of this section
is pending.

## Mathlib

Full matching Mathlib coverage has not been checked. The identities
here are finite algebra, changes of variables and the standard named
Fresnel integral; supporting library facts would not establish the
unpaid arithmetic estimate. No absence or formal verification is claimed.
The same limitation applies to (10)--(18): finite convolution and
indicator identities are supporting algebra, not a matching theorem
paying the completion remainder. No further Mathlib lookup was needed
to identify this unpaid estimate.
