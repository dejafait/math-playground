# Corollary C048o: finite signed Rice-tail endpoint expansion

## Hypotheses

Use C048a's actual theta kernel Phi and its canonical meromorphic
continuation of

\[
 I(p)=2\int_0^\infty u^{2p-1}\Phi(u)\,du\quad(\Re p>0),
\]

C048j's principal main term

\[
 w=W_0(2p/\pi),\qquad
 S(p)=\frac{8\pi^{5/2}e^{9w/4}}{\sqrt{p(1+w)}}
       \exp\{2p\operatorname{Log}(w/2)-2p/w\},
\]

and C048m/n's normalization, with the fixed positive constant
Z=gamma_0:

\[
 B_d(s)=\frac{d!}{\prod_{k=0}^d(s-k)},\quad
 F_d(s)=F_d^I(s)=\frac{\sqrt\pi\,4^{-s}I(s+1/2)B_d(s)}
                            {Z\Gamma(s+1/2)},\quad Q_d=F_d'/F_d.
\]

All branches are those principal branches. Primes mean complex
s-derivatives (or p-derivatives for functions displayed in p); the
shift p=s+1/2 has derivative one. For positive integer d put

\[
 \ell=\log d,\quad c=-1/4,\quad a=2d^{1/3},\quad b=d^{2/3}/2.
\]

Reuse the audited local conclusions of C048a/j/m/n. In particular
the actual-I phase bound is an input, not an assumption of signed
positivity. No infinite opening, stationary point, theta-boundary
continuation, lower-endpoint phase, or Xi/height implication is assumed.

## Conclusion

There is one integer d_0 such that for every integer d>=d_0, F_d
and Q_d are holomorphic and nonzero on a neighborhood of the segment
c+i[a,b], and

\[
 \int_a^b F_d(c+it)\,dt
 =\left[\frac{F_d(c+it)}{iQ_d(c+it)}\right]_{t=a}^{t=b}
       +\mathcal E_d,                                      \tag{1}
\]
\[
 \frac{|\mathcal E_d|}{|F_d(c+ia)/Q_d(c+ia)|}
 \le\frac{762696000\,\ell^6}{a}
 =381348000\frac{(\log d)^6}{d^{1/3}}\longrightarrow0.       \tag{2}
\]

The bracket means the value at b minus the value at a. The
normalization in (2) is the specified lower endpoint, not the
possibly cancelling endpoint difference. The onset is existential;
the numerical constant is only a convenient coarse bound.

This is a REPRODUCTION specialization under unchanged assessment1672,
reusing its completed source comparison1673. It imports standard
complex calculus and Cauchy estimates; the work here is the uniform
moving-degree application. It is local progress, with no assertion
of originality beyond the sources checked. Independent conceptual
audit1675 below accepts the expansion without correction. This controls
one signed part of C048l's finite
vertical contour; it does not control its bounded core, remaining
segments, total cancellation, other polynomial arguments, or a
sufficient actual-Xi positivity/height bridge. It is not an RH candidate.

## Proof

### 1. The whole segment and the existing amplitude margin

For s=c+it and p=s+1/2=1/4+it, set r=|p| and L=log r. Exactly
|s|=r=sqrt(t^2+1/16). For d>=64 the interval is nonempty, and
for every t in [a,b],

\[
 d^{1/3}\le a\le r\le b+1/4\le d^{2/3},\qquad
 t\ge r/2,\qquad \Re p=1/4>0.                         \tag{3}
\]

Thus the entire closed segment satisfies C048n's inner-sector
hypotheses. Above that result's single onset,

\[
 F_d(s)\ne0,\qquad \Im Q_d(s)\ge\frac1{60L}
                         \ge\frac1{60\ell}.            \tag{4}
\]

Here L<=ell follows from (3). All points have positive imaginary
part, excluding every finite-kernel pole and gamma pole. C048n gives
local holomorphy of F_d and its nonvanishing; then Q_d is locally
holomorphic and (4) makes it nonzero. The union of these neighborhoods
is a neighborhood of the closed segment on which both are nonzero,
after shrinking individual neighborhoods if necessary.

It remains to bound Q_d', Q_d at a, and the integrated amplitude.
The lower bound (4) alone is not a signed-integral estimate.

### 2. Complete disks and a bound for the principal derivative

Take L>=13 and fix any p on the segment. Use exactly the disk from
C048n's proof:

\[
 R=\frac r{32L},\qquad D_p=\{z:|z-p|\le R\}.
\]

That proof establishes strict containment of the whole disk in
C048j's wider sector, including an open holomorphic neighborhood:

\[
 3r/4<|z|<2r,\quad \log|z|>L-1\ge12,\quad
 \Re z>-\frac{|z|}{4\log|z|}.
\]

It supplies the canonical, single-valued holomorphic function
E(z)=I(z)/S(z)-1 and the whole-circle bound

\[
 \sup_{D_p}|E|\le7\frac{L^{9/2}}r.                    \tag{5}
\]

The analytic branches and nonzero S are the same C048a/j branches
used in that disk proof. No value estimate on a ray is differentiated.

Let F_d^S be F_d with I replaced by S. C048m's exact formula gives,
with q_z=d+3/2-z,

\[
 G_d(z):=\frac{(F_d^S)'(z-1/2)}{F_d^S(z-1/2)}
 =-\log4+2\operatorname{Log}(w_z/2)+A(z)
                 -\psi(z)-\psi(1/2-z)+\psi(q_z),        \tag{6}
\]
\[
 w_z=W_0(2z/\pi),\quad
 A(z)=\frac94\frac{w_z}{z(1+w_z)}-\frac1{2z}
                         -\frac{w_z}{2z(1+w_z)^2},
 \qquad |A(z)|\le\frac{13}{4|z|}.                      \tag{7}
\]

The identity is valid wherever these canonical analytic functions
are defined: it follows from the exact gamma recurrence for B_d and
the exact S derivative, not from an annular asymptotic. We verify
its domain and estimates on all of D_p before applying Cauchy.

Since R<r/8, t>=r/2 and r>=2, throughout D_p

\[
 \Im z>3r/8,\qquad |\Re z|\le1/4+R\le r/4,
 \qquad |\Re(1/2-z)|\le1/4+R\le r/4.
\]

Consequently |arg z| and |arg(1/2-z)| are less than 3pi/4.
Both moduli lie between r/2 and 2r; for the second this also uses
the exact equality |1/2-p|=r. Moreover, using r<=d^(2/3)<=d/4
for d>=64,

\[
 \Re q_z\ge d+5/4-R>d/2,\qquad
 d/2<|q_z|\le d+3/2+|z|<2d.                           \tag{8}
\]

These strict angular and pole clearances, and the disk's previously
checked principal branches, make G_d holomorphic on an open
neighborhood of D_p. For all three digamma arguments xi in (6),
4<=|xi|<=2d and |arg xi|<=5pi/6 once d is large as above.

Import the already inspected digamma remainder, NIST DLMF version
1.2.8, [5.11.2 and 5.11(ii)](https://dlmf.nist.gov/5.11#ii):

\[
 \psi(\xi)=\operatorname{Log}\xi-\frac1{2\xi}+R_1(\xi),
 \qquad |R_1(\xi)|\le
 \frac{\sec^3(\arg\xi/2)}{12|\xi|^2}\le\frac6{|\xi|^2}.
\]

The fixed sector just verified is sufficient for this bound. Therefore
|Log xi|<=log(2d)+pi<ell+4, and

\[
 |\psi(\xi)|\le\ell+4+1/8+6/16
                    <\ell+5\le2\ell\quad(\ell\ge13).  \tag{9}
\]

For completeness, C048a's branch bounds give w_z=U+iV with
U>0 and |V|<pi/2. The argument in C048m's proof applies throughout
this disk: if U<=2 then
|z|=(pi/2)|w_z|e^U<8e^2<e^12, a contradiction. Hence U>2.
The identity U+log|w_z|=log(2|z|/pi) then gives U<log|z|.
Writing L_z=log|z|>=12 yields

\[
 2<|w_z|<L_z+2\le2L_z,\quad |\arg w_z|<\pi/4,\quad
 |\operatorname{Log}(w_z/2)|\le\log L_z+\pi/4\le L_z
                                                   \le\ell+1.
\]

These inequalities use principal branches and hold over the full
disk, not just its center. In (7), |z|>=4 gives |A|<1, so (6),(9)
imply the convenient whole-disk bound

\[
 \sup_{D_p}|G_d|\le8\ell+5\le10\ell.                 \tag{10}
\]

Import Cauchy's estimates, A. Nagel, *Math722: Complex Analysis*,
Spring2012, Corollaries3.11--3.12, printed pp10--11
([primary notes](https://people.math.wisc.edu/~nagel/Math722Spring2012.pdf)).
For a function holomorphic on a neighborhood of a closed radius-R
disk, its nth derivative at the center is bounded by n!R^(-n)
times the whole-circle supremum. Apply the n=1 case to (10):

\[
 |G_d(p)|\le10\ell,\qquad
 |G_d'(p)|\le\frac{320\ell L}{r}\le\frac{320\ell^2}{r}.
                                                               \tag{11}
\]

This estimates the derivative without differentiating any digamma
asymptotic remainder.

### 3. The actual-I second derivative and a common onset

Apply the same imported Cauchy theorem to (5), for n=1 and n=2:

\[
 |E'(p)|\le\frac{224L^{11/2}}{r^2},\qquad
 |E''(p)|\le\frac{14336L^{13/2}}{r^3}.                \tag{12}
\]

These applications have the complete disk and holomorphic
neighborhood already checked. Choose one real L_*>=13 such that,
for every L>=L_*, all three inequalities hold:

\[
 7L^{9/2}e^{-L}\le1/2,\qquad
 448L^{11/2}e^{-2L}\le1,
\]
\[
 28672L^{13/2}e^{-2L}+200704L^{11}e^{-3L}\le1.          \tag{13}
\]

Every expression tends to zero; each summand is decreasing for
L>=13, as follows by differentiating its logarithm. Thus one eventual
ray works, independently of d and t. A common integer onset can be
chosen at least the C048n onset, 64, exp(39), and
(exp(L_*)/2)^3. By (3) this ensures L>=L_* throughout the segment
and every preceding lower bound on ell and the moduli.

Since |E(p)|<=1/2, the exact actual/principal quotient identity is

\[
 Q_d(s)=G_d(p)+\frac{E'(p)}{1+E(p)},\qquad p=s+1/2.
\]

Its derivative is legitimate on a nonzero neighborhood of p. From
(12),(13),

\[
 \left|\frac{E'}{1+E}\right|\le1,
\]
\[
 \left|\left(\frac{E'}{1+E}\right)'\right|
 \le2|E''|+4|E'|^2
 \le\frac{28672L^{13/2}}{r^3}
       +\frac{200704L^{11}}{r^4}\le\frac1r.            \tag{14}
\]

Combining (4),(11),(14) gives uniformly on the entire closed segment

\[
 |Q_d(s)|\le11\ell,\qquad |Q_d(s)|^{-1}\le60\ell,
 \qquad |Q_d'(s)|\le\frac{321\ell^2}{r}
                            \le\frac{321\ell^2}{a}.    \tag{15}
\]

In particular the first bound applies at the exact lower endpoint
used for normalization; no lower bound on an endpoint difference
is required.

### 4. Amplitude, exact orientation and the relative remainder

Put f(t)=F_d(c+it). Since ds/dt=i and F_d is nonzero,

\[
 \frac{d}{dt}\log|f(t)|=\Re(iQ_d(c+it))=-\Im Q_d(c+it)
                                  \le-\frac1{60\ell}.
\]

The imaginary part in (4) is an amplitude-decay input on this
vertical parameterization; it is not its real phase derivative.
Integrating this differential inequality gives, for a<=t<=b,

\[
 |f(t)|\le|f(a)|e^{-(t-a)/(60\ell)},\qquad
 \int_a^b|f(t)|\,dt\le60\ell\,|f(a)|.                 \tag{16}
\]

Import the complex fundamental theorem of calculus and integration
by parts from M. Beck, G. Marchesi, D. Pixton and L. Sabalka,
*A First Course in Complex Analysis*, edition1.6 (August2025),
Theorem4.2.5 and Exercise4.5.10, printed pp65,76
([author-hosted PDF](https://matthbeck.github.io/papers/complex.pdf)).
Here the functions are holomorphic on a neighborhood of the compact
segment and Q_d never vanishes there. The specialization, keeping
the chain-rule factor i, is

\[
 \frac{d}{dt}\left(\frac{F_d(c+it)}{iQ_d(c+it)}\right)
 =F_d(c+it)-\frac{F_d(c+it)Q_d'(c+it)}{Q_d(c+it)^2}.
\]

The finite fundamental theorem therefore gives (1) with the exact
remainder

\[
 \mathcal E_d=\int_a^b
      \frac{F_d(c+it)Q_d'(c+it)}{Q_d(c+it)^2}\,dt.      \tag{17}
\]

By (15),(16),

\[
 |\mathcal E_d|\le
 \frac{321\ell^2}{a}(60\ell)^2(60\ell)|f(a)|.
\]

The scale |f(a)/Q_d(c+ia)| is strictly positive. Dividing by it
and using |Q_d(c+ia)|<=11ell proves (2), since
321*60^3*11=762696000. Finally ell^6 exp(-ell/3) tends to zero:
the exponential series gives exp(ell/3)>=(ell/3)^7/7!, so the
ratio is bounded by 3^7*7!/ell for ell>0.

This proves the requested relative o(1), not only an absolute
small error. All integrals are finite, with one common onset and
constants independent of d and t. No limit is interchanged with a
sum, product or contour. Stops1657/1665/1667 retain their original
scopes; the bounded core, other segments, total sign and sufficient
Xi/height bridge are still unpaid.

### Independent conceptual audit1675 — 19 November2026

Audited the exact conclusion (1)--(2) under the unchanged SPECIALIZE
assessment1672 and its completed source comparison1673. Read the full
C048o and C048n proofs, C048m's phase proof, and the relevant C048a/j
continuation, branch and value statements. Reused the already inspected
primary Cauchy, digamma and complex-calculus passages in notes1663,
1670 and1673, with the precise citations above. The audited C048j
component estimates remain inputs; this is not a new audit of every
component certificate. No mathematical correction was required.

**Segment and analytic neighborhoods.** The shift is exactly
p=1/4+it, so |p|=|s| and every point of the closed segment, including
both endpoints, satisfies C048n's annulus and inner-sector conditions.
Its positive margin implies both nonvanishing of Q and the inverse
bound 60ell. The local nonzero neighborhoods may be shrunk and united;
no globally defined logarithm of F is required. The radius r/(32L)
disk has strict clearance from C048j's radial and angular boundaries,
as proved in C048n, so the value estimate holds on its entire circle.
The canonical I has no pole there. C048a gives Re(w)>0 and
|Im(w)|<pi/2. For the square root in S, C048j's branch identity is
sqrt(z(1+w))=w sqrt(A_0)/2 with |arg(w)|<pi/4 and Re(A_0)>0.
The right side has argument strictly between -pi/2 and pi/2 and is
nonzero. Thus the principal square root and logarithm agree across
the disk; E=I/S-1 is one holomorphic function on a neighborhood of
the whole closed disk. Nonvanishing of I on the disk is not a
hypothesis of the Cauchy estimates for E.

**Principal logarithmic derivative.** Rechecked the exact kernel
identity B_d(s)=(-1)^(d+1) Gamma(d+1)Gamma(-s)/Gamma(d+1-s)
by recurrence. With s=z-1/2 its logarithmic derivative supplies
-psi(1/2-z)+psi(d+3/2-z), with the signs and shifts in (6).
The third digamma term -psi(z) comes from the reciprocal gamma in F.
Every z in the chosen disk has Im(z)>3r/8; the real parts of z and
1/2-z have absolute value at most r/4. Their arguments therefore
have absolute value less than 3pi/4 and their moduli lie between
r/2 and 2r. Since r<=d^(2/3)<=d/4 for d>=64, q_z has
Re(q_z)>d/2 and |q_z|<2d. All three arguments avoid poles and
meet the fixed digamma sector on the entire disk, not merely at p.
The imported remainder gives |psi|<=ell+4+1/8+6/16<ell+5.
The branch bounds give |Log(w/2)|<=log(log|z|)+pi/4<=ell+1,
and |A(z)|<1. Hence the full-circle bound 10ell used in (10)
is valid. The identity defining G is exact and holomorphic there;
its applicability does not require C048m's annulus at every disk
point. Cauchy therefore gives |G'|<=320ell L/r as asserted.

**Actual derivative and simultaneous onset.** The n=2 Cauchy
factor is 2!, so the second estimate in (12) has coefficient
2*7*32^2=14336 and logarithmic power 9/2+2=13/2.
For the derivative of E'/(1+E), the denominator bound |1+E|>=1/2
gives 2|E''|+4|E'|^2, with coefficients 28672 and
4*224^2=200704. The last condition in (13) is exactly what makes
this at most 1/r after factoring out 1/r. The other two conditions
give |E|<=1/2 and |E'/(1+E)|<=1. Each summand in (13) decreases
on L>=13 and tends to zero, so a single L_* works before d or t
is chosen. Taking an integer ceiling of the stated maximum for d_0
ensures r>=a>=exp(L_*) and ell>=39 on the entire segment.
This checks both the existential common onset and all auxiliary
modulus bounds. Continuity at each center legitimizes differentiating
the quotient, without assuming I is globally zero-free. Combining
these estimates gives all three bounds in (15), including the exact
lower endpoint bound |Q(c+ia)|<=11ell.

**Amplitude, orientation and relative scale.** The vertical
parameter has ds/dt=i. Thus d log|F(c+it)|/dt=-Im(Q), whereas
the derivative of its local argument is Re(Q). Using the former
quantity yields (16) with coefficient 60ell. Direct chain-rule
checking of F/(iQ) gives F-FQ'/Q^2; no extra i or reversed sign
belongs in (17). The finite complex fundamental theorem applies
on the nonzero neighborhood already verified. Dividing its remainder
bound by |F(c+ia)/Q(c+ia)| multiplies by the upper bound 11ell
for |Q(c+ia)|. The total power is therefore ell^(2+2+1+1),
and 321*60^3*11=762696000. Substitution a=2d^(1/3) gives
exactly (2). Its limit follows from the stated positive exponential
series bound. Neither a lower bound for a difference of endpoint
values nor an illicit absolute-to-relative comparison is involved.

The audit accepts the stated finite signed expansion and its explicit
coarse relative bound under the existing audited analytic inputs.
It does not extend the interval past b, make the onset effective,
sign the endpoint difference, or pay the bounded core or total
contour. C048l's further segment up to d/log d is outside the proved
range. Stops1657/1665/1667, other polynomial arguments, C028b's
height criterion, C028g's compact nonreal-zero mass, and the sufficient
Xi bridge retain their recorded status. This is local verification of
a REPRODUCTION specialization, not progress beyond the sources
checked or an RH candidate. No numerical evidence or new mathematical
script is used in this audit.

## Mathlib

Full matching Mathlib coverage of this actual-Rice endpoint
specialization has not been checked; availability is unknown.
The supporting standard mathematics is the precisely cited Cauchy
estimate, digamma remainder and complex fundamental theorem, with
the local canonical analytic inputs above. No absence from Mathlib,
formal verification, or numerical evidence is claimed. A separate
specialization is necessary because the inspected fixed-data endpoint
expansions do not supply this degree-uniform relative remainder.
