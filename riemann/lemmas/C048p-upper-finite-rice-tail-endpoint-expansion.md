# Corollary C048p: upper finite Rice-tail endpoint expansion

## Hypotheses

Use C048a's actual theta kernel and its canonical meromorphic function
I, initially defined by

\[
 I(p)=2\int_0^\infty u^{2p-1}\Phi(u)\,du\quad(\Re p>0).
\]

Use C048j's nonzero principal main term and audited value estimate:

\[
 w=W_0(2p/\pi),\qquad
 S(p)=\frac{8\pi^{5/2}e^{9w/4}}{\sqrt{p(1+w)}}
       \exp\{2p\operatorname{Log}(w/2)-2p/w\},
\]
\[
 |I(p)/S(p)-1|<\frac{17}{10}\frac{(\log|p|)^{9/2}}{|p|}
 \quad\left(|p|\ge e^{12},\quad
       \Re p\ge-\frac{|p|}{4\log|p|}\right).                 \tag{1}
\]

All branches are the canonical principal branches in those results.
With the fixed positive normalization Z=gamma_0, define

\[
 B_d(s)=\frac{d!}{\prod_{k=0}^d(s-k)},\qquad
 F_d(s)=F_d^I(s)=\frac{\sqrt\pi\,4^{-s}I(s+1/2)B_d(s)}
                            {Z\Gamma(s+1/2)},\qquad Q_d=F_d'/F_d.
\]

Here d is a positive integer, primes on F_d and Q_d are complex
s-derivatives, and p=s+1/2 has derivative one. Put

\[
 \ell=\log d,\qquad c=-1/4,\qquad
 u=d^{2/3}/2,\qquad v=d/\ell.
\]

Reuse C048m's exact logarithmic-derivative identity and C048n's
degree-independent complete-disk estimate, with their domains checked
below. Their annular phase conclusions are not extended by citation.
No signed positivity, infinite opening, contour deformation, zero
count, or actual-Xi height implication is assumed.

## Conclusion

There is a single integer d_0 such that for all integers d>=d_0,
F_d and Q_d are holomorphic and nonzero on a neighborhood of the
entire closed segment c+i[u,v], and

\[
 \int_u^v F_d(c+it)\,dt
 =\left[\frac{F_d(c+it)}{iQ_d(c+it)}\right]_{t=u}^{t=v}
       +\mathcal E_d,                                    \tag{2}
\]
\[
 \frac{|\mathcal E_d|}{|F_d(c+iu)/Q_d(c+iu)|}
 \le\frac{225984\ell^6}{u}
 =451968\frac{(\log d)^6}{d^{2/3}}\longrightarrow0.        \tag{3}
\]

The bracket is the upper endpoint minus the lower endpoint. The
normalizing scale in (3) is nonzero; it is not the possibly cancelling
endpoint difference. The onset is existential, and the coarse constant
is not asserted to be sharp. Independent conceptual audit1679 below
accepts the result without a mathematical correction.

This is a REPRODUCTION specialization under assessment1675, compared
in notes1676 and separately approved1677 before attempt1678. The known
complex-calculus, digamma and Cauchy tools are imported below; only
their uniform application to this moving segment is established here.
No originality beyond the sources checked is claimed. The result
controls one more retained part of C048l's scalar J_d(-1) contour.
It leaves its bounded core, remaining lower segment, total cancellation,
other polynomial arguments, C028b/C028g and the sufficient actual-Xi
bridge unresolved. It is not a candidate solution of RH.

## Proof

### 1. Geometry and complete neighborhoods

For s=c+it, write p=1/4+it, r=|p|=|s| and L=log r.
For d>=exp(39), the whole segment satisfies

\[
 u\le t\le v,\quad u\le r\le v+1/4\le d/4,\quad
 t\ge r/2,\quad \ell/2\le L\le\ell.                     \tag{4}
\]

Indeed v/u=2exp(ell/3)/ell>=ell/9>1, using the quadratic
term of the exponential series. Also ell>=39 and d>=2 imply
d/ell+1/4<=d/4. Finally L>=log u=2ell/3-log 2>=ell/2;
t>=u>=2 gives r<=t+1/4<2t. These bounds include both endpoints.

At each such p with L>=13 take the closed disk

\[
 D_p=\{z:|z-p|\le R\},\qquad R=r/(32L).
\]

The complete-disk argument in C048n is independent of d and of its
later annular phase conclusion. Its center hypothesis
Re p>=-r/(8L) holds here since Re p=1/4. In detail, throughout D_p,

\[
 3r/4<|z|<2r,\quad \log|z|>L-1\ge12,\quad
 \Re z\ge1/4-R>-r/(32L).
\]

Monotonicity of x/log x for x>e gives
|z|/(4log|z|)>3r/(16L). Hence the full closed disk lies strictly
inside (1)'s sector and radial boundary. C048a's possible poles of
I are on the nonpositive integers and are excluded here. Its Lambert
branch is analytic near this disk. C048j supplies the same nonzero
holomorphic S: its branch identity
sqrt(z(1+w_z))=w_z sqrt(A_0)/2, with Re A_0>0 and
|arg w_z|<pi/4, agrees with the principal root. Thus there is an
open neighborhood of the whole closed disk on which

\[
 E(z)=I(z)/S(z)-1
\]

is one holomorphic function. Canonical branches agree on overlaps;
nonvanishing of I on this disk is not needed for this assertion.
Reuse C048n's full-circle conversion of (1):

\[
 \sup_{D_p}|E|\le7L^{9/2}/r.                              \tag{5}
\]

Its constants apply because log|z|<L+1<=13L/12 and |z|>r/2;
(17/5)(13/12)^(9/2)<34/5<7. No ray estimate is differentiated.

### 2. Exact principal derivative and full gamma arguments

Let F_d^S denote F_d with I replaced by S, and set
G_d(z)=(F_d^S)'(z-1/2)/F_d^S(z-1/2). The exact identity from
C048m is

\[
 G_d(z)=-\log4+2\operatorname{Log}(w_z/2)+A(z)
                  -\psi(z)-\psi(1/2-z)+\psi(q_z),        \tag{6}
\]
\[
 q_z=d+3/2-z,\quad w_z=W_0(2z/\pi),\quad
 A(z)=\frac94\frac{w_z}{z(1+w_z)}-\frac1{2z}
                         -\frac{w_z}{2z(1+w_z)^2},
 \qquad |A(z)|\le\frac{13}{4|z|}.                        \tag{7}
\]

Its use outside C048m's annulus needs no asymptotic extension:
B_d(s)=(-1)^(d+1)Gamma(d+1)Gamma(-s)/Gamma(d+1-s)
is an exact recurrence identity, and w'=w/[z(1+w)] gives
S'/S=2Log(w/2)+A exactly. The factors in (6) are analytic and
nonzero locally wherever used, as the following full-disk checks show.

Because R<r/8, t>=r/2 and r is large, for all z in D_p,

\[
 \Im z>3r/8,\quad
 |\Re z|,|\Re(1/2-z)|\le1/4+R\le r/4,
\]
\[
 r/2<|z|,|1/2-z|<2r,\quad
 |\arg z|,|\arg(1/2-z)|<3\pi/4.
\]

The modulus assertion for 1/2-z uses |1/2-p|=r. Moreover (4)
implies

\[
 \Re q_z\ge d+5/4-R>d/2,\qquad d/2<|q_z|<2d.          \tag{8}
\]

All three gamma arguments therefore avoid poles, have modulus at
least 4, and lie in |arg xi|<=5pi/6 on a neighborhood of the disk.
Gamma has no zeros (NIST DLMF [5.2(i)](https://dlmf.nist.gov/5.2#i));
the finite kernel has no pole there since Im(z-1/2)>0. Together
with Section 1's branches these facts make G_d holomorphic on an
open neighborhood of D_p.

Import the inspected digamma remainder from NIST DLMF version1.2.8,
[5.11.2](https://dlmf.nist.gov/5.11#E2) and
[5.11(ii), first complex-remainder paragraph](https://dlmf.nist.gov/5.11#ii):

\[
 \psi(\xi)=\operatorname{Log}\xi-\frac1{2\xi}+R_1(\xi),
 \quad |R_1(\xi)|\le\frac{\sec^3(\arg\xi/2)}{12|\xi|^2}
                         \le\frac6{|\xi|^2}.              \tag{9}
\]

The final cap follows from cos(5pi/12)>1/4. These are full arguments,
not a fixed-shift gamma-ratio expansion with a growing displacement.
All their moduli are at most 2d, so (9) yields
|psi(xi)|<=ell+4+1/8+6/16<ell+5<=2ell.

For any z in the disk, C048a gives w_z=U_z+iV_z with U_z>0
and |V_z|<pi/2. In fact U_z>4: otherwise |w_z|<6 and
|z|=(pi/2)|w_z|exp(U_z)<12e^4<e^12, contradicting Section 1.
Since |w_z|>4, the modulus identity
U_z+log|w_z|=log(2|z|/pi) gives U_z<log|z|. Writing L_z=log|z|,
we have |w_z|<L_z+2<=2L_z and |arg w_z|<pi/4. Consequently

\[
 |\operatorname{Log}(w_z/2)|\le\log L_z+\pi/4\le L_z
                                      \le\ell+1.
\]

Here the real part of Log(w_z/2) is positive, since |w_z|>4.
Since |A(z)|<1, (6) now gives the entire-disk bound

\[
 \sup_{D_p}|G_d|\le8\ell+5\le10\ell.                   \tag{10}
\]

### 3. Cauchy estimates and one common onset

Import A. Nagel, *Math722: Complex Analysis*, Spring2012,
Corollaries3.11--3.12, printed pp10--11
([primary notes](https://people.math.wisc.edu/~nagel/Math722Spring2012.pdf)).
The nth derivative at the center is bounded by n!R^(-n) times
the full-circle supremum for a function holomorphic near the closed
disk. Sections 1--2 verify precisely these hypotheses. Applying
n=1 to (10), and n=1,2 to (5), gives

\[
 |G_d(p)|\le10\ell,\quad |G_d'(p)|\le320\ell L/r,
\]
\[
 |E'(p)|\le224L^{11/2}/r^2,\qquad
 |E''(p)|\le14336L^{13/2}/r^3.                           \tag{11}
\]

Choose a single L_*>=13 such that all the following hold for every
L>=L_*:

\[
 7L^{9/2}e^{-L}\le1/2,\qquad
 448L^{11/2}e^{-2L}\le1,
\]
\[
 28672L^{13/2}e^{-2L}+200704L^{11}e^{-3L}\le1,
\]
\[
 48Le^{-L}+3584L^{13/2}e^{-2L}\le1.                      \tag{12}
\]

Each summand decreases for L>=13 and tends to zero: its logarithmic
derivative is a/L-b<0, and the exponential series with an integer
power greater than a proves the limit. Thus this is a simultaneous
eventual ray, fixed before d and t. Take an integer

\[
 d_0\ge\max\{e^{39},(2e^{L_*})^{3/2}\}.                 \tag{13}
\]

For every d>=d_0, (4) holds and r>=u>=e^(L_*), so all preceding
estimates apply throughout the segment. By (5),(12), |E(p)|<=1/2,
hence I(p)=S(p)(1+E(p)) is nonzero. It remains nonzero on a
neighborhood of each p by continuity. All factors of F_d are then
holomorphic and nonzero locally. With dp/ds=1 the exact quotient is

\[
 Q_d(s)=G_d(p)+\frac{E'(p)}{1+E(p)}.                     \tag{14}
\]

Equations (11)--(12) give

\[
 \left|\frac{E'}{1+E}\right|\le448L^{11/2}/r^2\le1,
\]
\[
 \left|\left(\frac{E'}{1+E}\right)'\right|
 \le2|E''|+4|E'|^2
 \le28672L^{13/2}/r^3+200704L^{11}/r^4\le1/r.
\]

Thus, using L<=ell and ell>=1,

\[
 |Q_d(s)|\le11\ell,\qquad
 |Q_d'(s)|\le321\ell^2/r\le321\ell^2/u.                 \tag{15}
\]

No asymptotic remainder was differentiated without a complete
holomorphic neighborhood and Cauchy estimate.

### 4. The widened-range phase comparison on the exact line

At the disk center write w=U+iV and phi=arg w. The preceding bounds
give U>4, U<L and 0<V<pi/2. There is no argument wrapping in

\[
 \theta:=\arg p=V+\phi,\qquad \phi=\arctan(V/U),
\]

because 0<V+phi<pi/2+pi/4<pi. For t>=2,
theta=pi/2-arctan(1/(4t))>3/2-1/8=11/8>4/3.
Also phi<=V/U<V/4, so V>4theta/5>16/15. Since
0<V/U<pi/8<1/2, the derivative of arctan x on [0,1/2]
is at least 4/5. Therefore

\[
 2\phi\ge\frac85\frac VU>\frac{128}{75L}>\frac3{2L}.
                                                               \tag{16}
\]

The competing gamma phase must be retained. Exactly on this line,
p=1/4+it and -s=1/4-it have opposite principal arguments and
the same modulus r. In (6),(9), the imaginary parts of their two
leading logarithms cancel, rather than contributing a residual
sector-bound error. With q=d+5/4-it the remaining logarithmic
phase is

\[
 \arg q=-\arctan(t/(d+5/4))\ge-t/d\ge-1/\ell.
                                                               \tag{17}
\]

Retaining every other term of (6),(9), their total error in the
imaginary part is at most

\[
 \frac{13}{4r}+\frac1r+\frac{12}{r^2}
                  +\frac1{2|q|}+\frac6{|q|^2}
 \le\frac5r+\frac1d\le\frac6r.                          \tag{18}
\]

Here r>=16, d>=12, |q|>=d and r<=d, all supplied by (4),(13).
This bound does not require an unproved gamma-phase cancellation
for the remainders. From (14),(16)--(18),

\[
 \Im Q_d(s)\ge\frac3{2L}-\frac1\ell
                    -\frac6r-\frac{448L^{11/2}}{r^2}.
\]

The last condition in (12) is exactly
6/r+448L^(11/2)/r^2<=1/(8L). By (4),
1/(8L)<=1/(4ell), while 3/(2L)-1/ell>=1/(2ell).
We have therefore proved on the entire new segment

\[
 \Im Q_d(s)\ge\frac1{4\ell}>0,\qquad
 |Q_d(s)|^{-1}\le4\ell.                                 \tag{19}
\]

This is a new uniform application of the full formula, not an
extension of C048m/n's annular sign by citation. Since Q_d is
holomorphic locally by Section 3, continuity and (19) give nonzero
neighborhoods of each segment point. Shrinking these neighborhoods
and taking their union supplies the asserted neighborhood of the
whole closed segment for both F_d and Q_d.

### 5. Amplitude and the normalized finite remainder

Put f(t)=F_d(c+it). The parameter has ds/dt=i, so by (19),

\[
 \frac d{dt}\log|f(t)|=\Re(iQ_d(c+it))
                  =-\Im Q_d(c+it)\le-1/(4\ell).
\]

This is an amplitude inequality; the local argument derivative would
instead be Re Q_d. Integrating it gives

\[
 |f(t)|\le|f(u)|e^{-(t-u)/(4\ell)},\qquad
 \int_u^v|f(t)|\,dt\le4\ell|f(u)|.                      \tag{20}
\]

Import the complex fundamental theorem and finite integration by
parts from M. Beck, G. Marchesi, D. Pixton and L. Sabalka,
*A First Course in Complex Analysis*, edition1.6 (August2025),
Theorem4.2.5 and Exercise4.5.10, printed pp65,76
([author-hosted PDF](https://matthbeck.github.io/papers/complex.pdf)).
All functions here are holomorphic near the finite segment, with
the denominator nonzero as just proved. The chain rule gives

\[
 \frac d{dt}\left(\frac{F_d(c+it)}{iQ_d(c+it)}\right)
 =F_d(c+it)-\frac{F_d(c+it)Q_d'(c+it)}{Q_d(c+it)^2}.
\]

Consequently (2) holds with the exact remainder

\[
 \mathcal E_d=\int_u^v
       \frac{F_d(c+it)Q_d'(c+it)}{Q_d(c+it)^2}\,dt.
\]

Equations (15),(19),(20), including (15) at the exact lower endpoint,
now give

\[
 \frac{|\mathcal E_d|}{|f(u)/Q_d(c+iu)|}
 \le\frac{321\ell^2}{u}(4\ell)^2(4\ell)(11\ell)
 =\frac{225984\ell^6}{u}.
\]

This proves (3). For its limit, the positive exponential series
gives exp(2ell/3)>=(2ell/3)^7/7!, so
ell^6 exp(-2ell/3)<=7!(3/2)^7/ell, which tends to zero.
The normalization is thus relative to the specified nonzero endpoint,
not inferred from absolute smallness or an endpoint difference.

Every integral is finite. One common onset (13) pays the whole
segment and all disk estimates; no sum, product or infinite contour
limit is interchanged. The separate fixed-degree opening, in-sector
saddle and theta-boundary stops1657/1665/1667 remain unchanged.
C048o concerns the adjacent lower interval and is not a premise
extending its own endpoint theorem to this interval.

### Independent conceptual audit1679 — 19 November2026

**Scope and verdict.** Independently replayed (4)--(20) and the finite
remainder under the unchanged, previously approved assessment1675.
The proof passes without correction. This is verification of the
existing REPRODUCTION specialization, not an additional estimate,
novel theorem, or RH candidate. C048a/j's audited continuation,
branches and value estimate remain mathematical inputs; their entire
upstream proofs were not re-audited here. Read the applicable exact
identity in C048m and the degree-independent disk argument in C048n,
and reused the inspected source hypotheses in comparison1676 and
approval1677. Neither input's annular sign conclusion is used outside
its annulus. C048l/o provide context only.

**Geometry and holomorphy.** For ell>=39, v/u=2e^(ell/3)/ell>=ell/9>1
and r=sqrt(t^2+1/16) lies between u and v+1/4<=d/4. Also
L>=log u=2ell/3-log2>=ell/2 and L<=ell. Thus these bounds hold at
both endpoints and every intermediate t. With R=r/(32L), every
z in the closed disk has |z|>3r/4, log|z|>L-1>=12 and
Re z>=1/4-R>-r/(32L). Since x/log x is increasing for x>e,

    |z|/(4log|z|)>3r/(16log(3r/4))>3r/(16L).

This verifies the full disk's strict inclusion in C048j's domain,
not merely the circle's intersection with the vertical line. The
strict radial and sector margins supply an open neighborhood. The
canonical I has no possible pole there. For S, C048j's identity
sqrt(z(1+w_z))=w_z sqrt(A_0)/2 has positive real part on the right:
|arg w_z|<pi/4 and Re A_0>0 give |arg sqrt(A_0)|<pi/4.
Its square is z(1+w_z), so this is the principal square root.
All other branch factors are analytic and nonzero there. This
justifies the single holomorphic E=I/S-1 on overlapping disks.

The full-disk estimate follows from |z|>r/2 and
log|z|<L+1<=13L/12:
(17/5)(13/12)^(9/2)<(17/5)(13/12)^5<34/5<7.
Nonvanishing of I is not a prerequisite for forming E or applying
Cauchy to it. It is established later from this bound.

**Exact gamma derivative and the whole-circle bound.** Gamma
recurrence gives B_d(s)=(-1)^(d+1)Gamma(d+1)Gamma(-s)/Gamma(d+1-s).
The two latter factors contribute -psi(-s)+psi(d+1-s), with these
signs. Differentiating S using w'=w/[z(1+w)] gives exactly (6)--(7);
the nonlogarithmic terms from differentiating
2z Log(w/2)-2z/w cancel. No asymptotic error is differentiated here.
Re w_z>0 gives |w_z/(1+w_z)|<1 and |1+w_z|>1, proving
|A(z)|<=13/(4|z|).

Throughout the disk, Im z>3r/8 and both real parts in z,1/2-z
have magnitude <=r/4. Their moduli lie between r/2 and 2r,
and their arguments have magnitude <3pi/4. The third full argument
q_z has Re q_z>d/2 and d/2<|q_z|<2d. Thus the fixed-sector
digamma remainder (9) applies everywhere on the disk and on a
neighborhood, without a growing-shift ratio theorem. There are no
gamma or finite-product poles or zeros in this use. For |xi|>=4,
|xi|<=2d and |arg xi|<=5pi/6, its bound is

    |psi(xi)|<=log(2d)+5pi/6+1/8+6/16<ell+5<=2ell.

For the Lambert factor, U_z<=4 would imply |w_z|<6 and
|z|<12e^4<e^12, a contradiction. Hence U_z>4; the modulus
equation gives U_z<log|z| and |w_z|<2log|z|. It follows that
|Log(w_z/2)|<=log(log|z|)+pi/4<=ell+1. Together these estimates
give sup|G_d|<=8ell+5<=10ell on the entire Cauchy circle.

**Cauchy constants and quantifiers.** Nagel's all-orders estimate
applies to both functions on these closed disks. The constants are
7*32=224 for E', 2!*7*32^2=14336 for E'', and 10*32=320
for G_d'. The quotient derivative has the bound
2|E''|+4|E'|^2, with constants 28672 and 200704.
Every summand in (12) has form C L^a exp(-bL), with a/b<13;
it decreases on [13,infinity) and tends to zero. A single L_*
therefore satisfies all four lines for every L>=L_*. Choosing d_0
by (13) puts every center above that same threshold. The first line
gives |E|<=1/2 and actual I nonvanishing; the next two give
|Q_d|<=11ell and |Q_d'|<=(320ell L+1)/r<=321ell^2/u.
These are uniform statements, not point-dependent choices of onset.

**Decisive phase margin.** At the centers, w=U+iV has U>4 and
0<V<pi/2. Since 0<V+arg w<pi, its argument equation has no
wrapping: theta=V+arctan(V/U). For t>=2, theta>4/3, whence
V>4theta/5>16/15. On 0<=x<=1/2, arctan'(x)>=4/5; since
V/U<pi/8<1/2 and U<L, this gives 2arg w>128/(75L)>3/(2L).
The arguments p=1/4+it and -s=1/4-it are conjugate, so their
principal logarithmic imaginary parts cancel exactly. The remaining
gamma logarithm contributes arg(d+5/4-it)>=-t/d>=-1/ell.
The full remainder cost is <=5/r+1/d<=6/r, using r>=16,
d>=12 and r<=d. This retains every digamma correction; cancellation
of their errors is not assumed.

The last line of (12) bounds this cost together with the actual-I
correction by 1/(8L). Since ell/2<=L<=ell, it follows that

    Im Q_d >= 3/(2L)-1/ell-1/(8L) >= 1/(4ell)>0.

This is the required comparison on the enlarged segment, independent
of the narrower annular phase theorem. Local holomorphy and continuity
give nonzero neighborhoods of each point for both F_d and Q_d;
their union is an open neighborhood of the entire closed segment.
No global logarithm or uniform neighborhood radius is needed.

**Orientation and exact relative error.** With ds/dt=i,
d(log|F_d(c+it)|)/dt=-Im Q_d<=-1/(4ell), so the amplitude
integral is at most 4ell|F_d(c+iu)|. Differentiating F_d/(iQ_d)
gives F_d-F_d Q_d'/Q_d^2, as printed. Applying the cited complex
fundamental theorem to this primitive along the finite segment yields
the stated plus-sign remainder and upper-minus-lower endpoints.
The remainder integrand is continuous there; no antiderivative for
an arbitrary function on a nonsimply connected region is presumed.
The lower-endpoint denominator is nonzero, and its normalization
multiplies the error by |Q_d(c+iu)|<=11ell. Consequently the exact
coefficient is 321*16*4*11=225984, giving (3) with u=d^(2/3)/2.
The exponential-series estimate printed after (20) proves the
normalized bound tends to zero. Neither endpoint cancellation nor
absolute smallness substitutes for that comparison.

The direct mathematical inputs in the existing DAG row suffice;
no new dependency or cycle is introduced. Finite calculus, actual
normalization, principal branches, multiplicative denominators and
one common onset all survive the audit. The fixed-degree opening,
stationary-sector and theta-boundary obstructions remain intact.
Total cancellation, the bounded core and lower segment, other
polynomial arguments, C028b/C028g and the sufficient Xi bridge remain
unresolved. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching Mathlib coverage of this actual-Rice upper-tail
specialization has not been checked; availability is unknown. The
supporting results are the precisely cited digamma remainder, gamma
nonvanishing, Cauchy estimates and complex fundamental theorem, with
the local canonical analytic inputs stated above. No formal proof,
absence from Mathlib, or numerical evidence is claimed. A separate
uniform application is necessary because the inspected endpoint/Rice
results do not provide this observable, growing interval and exact
lower-endpoint relative normalization.
