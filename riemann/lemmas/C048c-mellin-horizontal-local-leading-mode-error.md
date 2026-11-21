# Corollary C048c: the finite horizontal leading-mode Mellin error

## Hypotheses

Let p be complex, r=|p|, L=log r, with L>=12 and Re p>=-r/(4L).
Use C048a's principal branch w=W_0(2p/pi)=U+iV and put

\[
 u_0=w/2,\quad d=1/(3L),\quad
 h_p(u)=2p\operatorname{Log}u-\pi e^{2u},\quad
 g(u)=8\pi^2e^{9u/2}/u,\quad g_0=g(u_0),\quad
 A_0=-h_p''(u_0)/2.
\]

The logarithm is principal; all local integrations below are over
real s, oriented from -d to d. Set

\[
 K(s)=g(u_0+s)/g_0,\quad
 J_{\rm loc}=\int_{-d}^d K(s)e^{h_p(u_0+s)-h_p(u_0)}\,ds,\qquad
 G_{\rm loc}=\int_{-d}^d e^{-A_0s^2}\,ds.
\]

This audits precisely the leading positive-power part of theta mode1,
not the full kernel. It reproduces the local allowance stated in
K. Kawano, *Logarithmic Inequalities of Arbitrary Order for the Riemann
Xi Coefficients*, [Preprints.org202611.0383v1, posted4November2026,
DOI10.20944/preprints202611.0383.v1](https://www.preprints.org/manuscript/202611.0383/v1),
Section5.2(28), AppendixB's local Taylor/four-term calculation and
AppendixC's local inequalities and A_loc. This preprint's quantitative
bounds are conclusions to verify, not hypotheses. Assessment1627
approved this exact reproduction target before step1628; its extracted
primary cases are retained in source-notes1627.

## Conclusion

The segment lies in Re u>1 and |Im u|<pi/4; g_0 and A_0 are nonzero.
With the principal Gaussian square root,

\[
 T_{\rm loc}(p):=\frac{|J_{\rm loc}-G_{\rm loc}|}
                         {|\sqrt{\pi/A_0}|}
 \le A_{\rm loc}\frac{L^{9/2}}r,                         \tag{1}
\]

where the exact constant is

\[
 A_{\rm loc}=\sqrt6\left[
 \frac{13}{2(39/10)^{3/2}12^2}
 +\frac{33}{2(39/10)^{5/2}12}
 +\frac{15}{(799/300)^{7/2}}\right]<1.318214.             \tag{2}
\]

The normalization has the source's exact phase:

\[
 g_0e^{h_p(u_0)}\sqrt{\pi/A_0}
 =\frac{8\pi^{5/2}e^{9w/4}}{\sqrt{p(1+w)}}
       e^{2p\operatorname{Log}(w/2)-2p/w}=S(p).          \tag{3}
\]

The square roots in (3) agree with continuation from positive real p.
These statements include both angular boundaries, r=e^12, real p,
negative Re p permitted by the sector, and arbitrarily large L.

This is REPRODUCTION of a claimed source component, independently checked
in conceptual audit1629 below. It supplies neither the full (29)
remainder nor a zero count, inversion theorem or sufficient sign bridge.
The lower-power mode1 term, n>=2 modes, Gaussian extension, horizontal
tails and the global actual-Xi positivity gap remain separate.

## Proof

### 1. Uniform geometry and curvature

C048a and the geometry portion of C048b, (4)-(5), give

\[
 we^w=2p/\pi,\quad U>3L/4\ge9,\quad |V|<\pi/2,\quad
 U+\log|w|=L-\log(\pi/2),\quad |w|<U+2.
                                                               \tag{4}
\]

For Im p>=0 they also give 0<=V and, without argument wrapping,

\[
 \arg p=V+\arctan(V/U)
 \le\pi/2+\eta,\qquad \eta=\arcsin(1/(4L)).             \tag{5}
\]

Only these proved facts are used from C048b, not its origin estimate.
Since |w|>9 and e<3, log|w|>2. Thus (4), with pi/2>1, implies

\[
 U+2<L,\qquad |w|<L.                                  \tag{6}
\]

Here is a stronger strip clearance than was needed for C048b:

\[
 \cos V>1/L.                                          \tag{7}
\]

It suffices to treat Im p>=0. If V<=4/3, then
cos V>=1-V^2/2>=1/9>1/L. If V>4/3, put delta=pi/2-V.
By (5) and U<L,

\[
 \delta\ge\arctan(V/U)-\eta
 >\arctan(4/(3L))-\eta.
\]

For 0<=x<1, arcsin x<=x/sqrt(1-x^2), by its integral formula;
at L>=12 this gives eta<13/(50L). Indeed squaring the needed
positive-quantity comparison reduces to
1/[16(1-1/2304)]<(13/50)^2. Also
arctan x>=x-x^3/3 for x>=0, by integrating
1/(1+t^2)>=1-t^2. Consequently

\[
 \delta>\frac1L\left(\frac43-\frac4{729}-\frac{13}{50}\right)
 >\frac{16}{15L}.                                    \tag{8}
\]

The last strict comparison is equivalent to 1/150>4/729.
Since 0<delta<pi/2 and a=16/(15L)<=4/45, sine is increasing there,
and sin a>=a-a^3/6. This latter inequality follows by integrating
cos t>=1-t^2/2. Hence

\[
 \cos V=\sin\delta>\frac1L\frac{16}{15}
                \left(1-\frac{(4/45)^2}6\right)>1/L.
\]

Conjugation of the principal Lambert branch treats Im p<0, since
cos V is even. All steps use non-strict domain inequalities and
strict numerical slack, so the closed boundaries are included.

The identity pi e^w=2p/w gives h_p'(u_0)=0 and

\[
 A_0=\frac{4p(1+w)}{w^2}=2\pi e^w(1+1/w).
\]

Writing b=Re A_0, its real part is

\[
 b=2\pi e^U\left[\cos V+
                \frac{U\cos V+V\sin V}{|w|^2}\right]
 >2\pi e^U\cos V
 =\frac{4r\cos V}{|w|}>rac{4r}{L^2}
 >\frac{39r}{10L^2}.                                 \tag{9}
\]

The extra numerator is positive for either sign of V. Moreover

\[
 |A_0|\le\frac{4r}{|w|}(1+1/|w|)
 <\frac{160}{27}\frac rL<\frac{6r}L.                  \tag{10}
\]

Thus A_0 is nonzero and in the open right half-plane. These estimates
also verify the source's weaker auxiliary bounds |w|<=1.01L,
cos V>=1/L and v_0=pi e^U cos V>2r/L^2>1.9r/L^2.

### 2. Segment and exact complex normalization

For real |s|<=d, (4) gives

\[
 \Re(u_0+s)>3L/8-1/(3L)\ge161/36>40/9>1,\qquad
 |u_0+s|>L/3.                                       \tag{11}
\]

The first bounding function increases for L>=12; the second follows
from L^2>=144>8. The imaginary part is the fixed V/2, strictly inside
the theta strip. Thus h_p and g are holomorphic in a neighborhood of
the whole segment, all denominators are nonzero, and g_0 is nonzero.

Use the principal sqrt(A_0). By (9) its argument has absolute value
less than pi/4. Since |V|<pi/2<U, |arg w|<pi/4. Therefore
w sqrt(A_0)/2 has positive real part. Its square is p(1+w), so it is
exactly the principal sqrt(p(1+w)). This also proves that this latter
argument avoids the nonpositive real axis throughout the sector.
The roots are continuous and agree with positive roots for positive p.
In particular

\[
 \sqrt{\pi/A_0}=\frac{\sqrt\pi}{\sqrt{A_0}}
 =\frac{\sqrt\pi\,w}{2\sqrt{p(1+w)}}.
\]

Substitute g_0=16pi^2 e^(9w/4)/w and
h_p(u_0)=2p Log(w/2)-2p/w to obtain (3), with no modulus-only
replacement of its phase. The standard complex Gaussian identity is
also applicable: [NIST DLMF7.7.6](https://dlmf.nist.gov/7.7.E6),
with its coefficient a=A_0, b=c=x=0, gives the integral on [0,infinity);
evenness gives the full integral sqrt(pi/A_0). Its hypothesis Re a>0
is precisely (9), and absolute convergence follows from e^(-b s^2).
We use its branch, although the finite Gaussian in (1) is not extended.

### 3. Amplitude estimates on the entire finite interval

Put q=r/L and use (11). Exactly,

\[
 K(s)=\frac{e^{9s/2}}{1+s/u_0},\quad
 |s/u_0|<8/(9L^2)\le1/162.
\]

For 0<t<1, the exponential power series gives e^t<1/(1-t).
Thus

\[
 |K(s)|\le\frac{e^{1/8}}{1-1/162}
 <\frac87\frac{162}{161}<\frac{29}{25}=1.16.          \tag{12}
\]

Let a_1=K'(0)=9/2-1/u_0. Then |a_1|<85/18<19/4=4.75.
Differentiation gives, for real s throughout this interval,

\[
 K''(s)=K(s)\left(81/4-9/(u_0+s)+2/(u_0+s)^2\right).
\]

By (11)-(12), one half of the supremum of |K''| is less than

\[
 \frac{29}{50}\left(\frac{81}4+\frac{81}{40}
                                  +\frac{81}{800}\right)
 =12.978225<13.
\]

Taylor's integral remainder along the real segment, valid also for
negative s by reversing the integration limits, proves

\[
 |K-1-a_1s|\le13s^2,\qquad
 |K-1|\le(19/4+13/36)|s|=(46/9)|s|.                  \tag{13}
\]

No assumption that K or the complex Gaussian is real is used.

### 4. Phase Taylor bounds and residual absorption

Set B_0=h_p'''(u_0)/6. Direct differentiation gives

\[
 B_0=16p/(3w^3)-8p/(3w),\qquad
 h_p''''(u)=-12p/u^4-16\pi e^{2u}.
\]

Since |w|>3L/4>=9,

\[
 |B_0|\le\frac{8r}{3|w|}(1+2/|w|^2)
 <\frac{2656}{729}q<\frac{73}{20}q=3.65q.            \tag{14}
\]

Write the exact Taylor decomposition

\[
 h_p(u_0+s)-h_p(u_0)=-A_0s^2+B_0s^3+R_4(s)
                   =-A_0s^2+Z(s).
\]

Taylor's integral remainder bounds |R_4(s)| by |s|^4/24 times
the supremum of |h_p''''| between 0 and s. On that interval (11)
and pi e^U=2r/|w| show

\[
 \frac1{24}\sup|h_p''''|
 \le\frac{81r}{2L^4}+\frac{4r}{3|w|}e^{2d}
 <q\left(\frac3{128}+\frac{32}{17}\right)<2q.        \tag{15}
\]

Here 81/(2L^3)<=3/128, and e^(2d)<=e^(1/18)<18/17.
It follows that

\[
 |R_4(s)|\le2q|s|^4,\qquad
 |Z(s)|\le(73/20+1/18)q|s|^3
             \le(371/100)q|s|^3.                     \tag{16}
\]

The last bound is strict when s is nonzero; at s=0 both sides vanish.

The complex exponential series, or its integral remainder, gives
|e^Z-1-Z|<=|Z|^2 e^|Z|/2 for every complex Z. Use the exact split

\[
 K e^Z-1-a_1s-B_0s^3
 =(K-1-a_1s)+(K-1)B_0s^3+KR_4+K(e^Z-1-Z).            \tag{17}
\]

The four bounds (12)-(16) imply

\[
 |K e^Z-1-a_1s-B_0s^3|
 \le13s^2+22q s^4+8q^2 s^6 e^{|Z|}.                 \tag{18}
\]

Indeed the quartic coefficient is at most
(46/9)(73/20)+58/25<22; the sextic coefficient is less than
(29/50)(371/100)^2=7.983178<8. The quadratic coefficient comes
only from the first summand of (17).

Finally (9), (16) and |s|<=1/(3L) give

\[
 -b s^2+|Z(s)|
 \le-\left(\frac{39}{10}-\frac{371}{300}\right)
                        \frac r{L^2}s^2
 =-b_*s^2,\qquad b_*:=\frac{799}{300}\frac r{L^2}>0.  \tag{19}
\]

This absorption is uniform in p; it does not require |Z| to be small
at the finite endpoints as r grows.

### 5. Odd cancellation, Gaussian moments and the constant

The functions s e^(-A_0s^2) and s^3 e^(-A_0s^2) are odd on [-d,d].
Their integrals vanish even for complex A_0. Subtracting these terms
in the integral for J_loc-G_loc is therefore exact. By (18)-(19),

\[
 |J_{\rm loc}-G_{\rm loc}|
 \le\int_{-d}^d\left[(13s^2+22q s^4)e^{-bs^2}
                         +8q^2s^6e^{-b_*s^2}\right]ds. \tag{20}
\]

These are nonnegative real integrands, so extending only the error
majorants to the real line increases their integrals. For t>0,
the standard real Gaussian integral and repeated integration by parts
give, for j=1,2,3,

\[
 \frac1{\sqrt\pi}\int_{\mathbb R}s^{2j}e^{-ts^2}\,ds
       =\frac{(2j-1)!!}{2^j t^{j+1/2}}.
\]

For completeness, integration by parts reduces the 2jth moment to
(2j-1)/(2t) times the (2j-2)th moment; the boundary polynomial times
e^(-ts^2) vanishes at each infinity. All moments converge absolutely.
Starting with the j=0 Gaussian (also DLMF7.7.6 with positive real a)
proves the displayed specializations without differentiating a
parameter integral or interchanging a theta series and an integral.

Since |sqrt(pi/A_0)|=sqrt(pi)/sqrt(|A_0|), (20) becomes

\[
 T_{\rm loc}\le\sqrt{|A_0|}\left[
 \frac{13}{2b^{3/2}}+
 \frac{33r}{2L b^{5/2}}+
 \frac{15r^2}{L^2b_*^{7/2}}\right].                   \tag{21}
\]

Insert (9)-(10) and b_* from (19). The result is at most

\[
 \frac{\sqrt6 L^{9/2}}r\left[
 \frac{13}{2(39/10)^{3/2}L^2}
 +\frac{33}{2(39/10)^{5/2}L}
 +\frac{15}{(799/300)^{7/2}}\right].
\]

Using L>=12 proves (1)-(2), apart from the last rational comparison.
The exact rational certificate
`scripts/mellin-horizontal-local/local_constants_1628.json`, reproduced by
`python3 scripts/mellin-horizontal-local/local_constants_1628.py`,
checks sixteen fixed rational comparisons from this proof. In particular
it encloses sqrt6, sqrt(39/10) and sqrt(799/300) between adjacent
multiples of 10^-15, verifying the squared endpoints exactly. Positive
upper/lower substitution into (2) gives an exact rational upper bound
less than 659107/500000=1.318214, with slack greater than 3.12*10^-7.
Its decimal display is about 1.318213687763102; the proof uses the
saved rational values and their square checks, not that display.

No parameter grid or quadrature is involved. Every p-dependent estimate
above is analytic and uniform; the certificate checks only fixed rational
comparisons. The reasoning for negative imaginary p follows either
directly from the even estimates or from conjugating h, g and their
principal branches. At Im p=0 the sector forces p>0, and no step divides
by V or by Im p. All denominators have been paid uniformly at L=12.
This completes the reproduction proof. Its independent conceptual audit,
including the precise scope of the inputs C048a/b, is recorded below.

### Independent conceptual audit1629 — 19 November 2026

The unchanged SPECIALIZE assessment1627 covers this exact finite local
target. The full proof, C048a's principal-branch argument, C048b's geometry
(4)-(5) and its audit, and the previously inspected primary cases in
source-notes1627 were checked. The bound (1), exact constant (2) and
complex identity (3) pass. One endpoint precision error was corrected:
the final strict sign previously printed in (16) is false at s=0.
The non-strict version above holds there with equality and suffices for
every later estimate. No constant or substantive argument changes.

**Inputs and sector geometry.** C048a's continuation of W_0 along each
fixed-radius arc avoids the cut; all three first-exit cases are excluded,
including at the sector's angular boundary. C048b's U>3L/4 follows from
the modulus identity and 3L/4+log L<L-log(pi/2), whose base case is
6pi<e^3 and whose difference increases for L>=12. Thus the stronger (6)
uses the exact inequality |w|>9>e^2, not an asymptotic expansion. In
(8), the cubic arctangent cost is
64/(81L^3)<=4/(729L); the arcsine cost is bounded after squaring
positive quantities. The split at V=4/3 covers the full interval,
and 16/(15L)<=4/45 is inside sine's increasing interval. These checks
establish cos V>1/L uniformly, with no division by V at zero height.

**Curvature, denominators and phase.** The expression for Re A_0 in (9)
has an extra positive term U cos V+V sin V for either sign of V.
The upper bound uses |w|>3L/4 and |w|>9, giving 160/27<6.
For all intermediate points on each Taylor segment,
Re(u_0+s)>3L/8-1/(3L)>=161/36 and
3/8-1/(3L^2)>1/3. Hence the logarithm and every denominator used in
the derivatives are valid throughout the entire integration interval.
The arguments of w and sqrt(A_0) each have absolute value less than
pi/4, so w sqrt(A_0)/2 has strictly positive real part. Squaring it
identifies the principal root of p(1+w); this checks (3) with its phase,
including permitted negative Re p. DLMF7.7.6 applies because Re A_0>0,
with its other parameters zero and erfc(0)=1. There is no replacement
of the oscillatory Gaussian by a positive one in this identity.

**Taylor estimates and cancellation.** Direct differentiation verifies
the displayed K'', B_0 and h_p'''' formulas. The amplitude quadratic
coefficient is half of the supremum of |K''|, including the factor |K|.
The two quartic phase costs after division by q are bounded by
81/(2L^3)<=3/128 and (16/9)e^(2/(3L))<32/17; both decrease with L.
Taylor's integral remainders are along real segments and apply to both
orientations, so negative s has the same absolute bounds. Expanding
the right side of (17) recovers its left side exactly. The two odd
terms cancel against the same complex even Gaussian on [-d,d].
The residual bounds therefore retain the amplitude-phase cross term
and give (20), without supposing K, Z or A_0 is real.

The absorption uses |Z|<=371q|s|^3/100 and |s|<=1/(3L), giving
39/10-371/300=799/300>0. It does not assume |Z| is uniformly small
at the endpoints: that would be unjustified as r grows. Only the
nonnegative error majorants in (20) are extended to the real line.
The Gaussian moment factors are respectively 1/2, 3/4 and 15/8;
multiplying by 13, 22q and 8q^2 yields precisely (21).
The normalization costs sqrt(|A_0|), even when A_0 is nonreal.
After substituting b, b_* and |A_0|, the three powers are
L^(5/2)/r, L^(7/2)/r and L^(9/2)/r. Taking L>=12 then gives (2).
All integrations are absolutely convergent in the uses made here;
the moment recurrence has vanishing boundary terms. No infinite theta
sum, contour interchange or Gaussian-extension allowance is invoked.

**Exact arithmetic and endpoints.** Replaying the original certificate
passes all sixteen rational comparisons. The root intervals, their
squared endpoints, all coefficient comparisons and the complete A_loc
rational enclosure were inspected. A separate saved-value check,
`python3 scripts/mellin-horizontal-local/audit_constants_1629.py`,
reconstructs the constant bounds from the root intervals and checks
the exact margin against 39/125000000=3.12*10^-7. Its complete evidence
is `scripts/mellin-horizontal-local/audit_constants_1629.json`.
These are fixed-coefficient checks, not a substitute for the uniform
analytic argument. The zero-s case corrected above is included;
zero height forces positive real p, the negative-imaginary cases follow
by conjugation, and all domain boundaries retain strict geometric slack.
Every radial comparison is valid for the full ray L>=12, not a grid.

This audit validates the source's claimed local component as reproduced
here. It does not establish any stronger result than the source claim.
The direct mathematical inputs remain C048a's branch and C048b's stated
geometry. The full-mode, Gaussian-extension, horizontal-tail and global
sign obligations listed above remain open; there is no full RH candidate.

## Mathlib

Full matching coverage has not been checked. No absence claim is made
for this effective moving-sector complex saddle inequality. The Gaussian
integral input is the precise standard DLMF specialization cited above;
its applicability, moment recurrence, branches and numerical comparisons
are justified here. The Lambert geometry is imported only from the stated
proved portions of C048a/b. No Lean or other formal verification is claimed.
