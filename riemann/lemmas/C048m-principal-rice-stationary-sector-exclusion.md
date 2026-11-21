# Corollary C048m: exclusion of principal Rice stationary points in the audited sector

## Hypotheses

Use C048a's actual theta kernel and principal Lambert branch, C048j's
principal nonzero main term, and C048l's exact finite Rice kernel:

\[
 w=W_0(2p/\pi),\qquad
 S(p)=\frac{8\pi^{5/2}e^{9w/4}}{\sqrt{p(1+w)}}
       \exp\{2p\operatorname{Log}(w/2)-2p/w\},
\]
\[
 B_d(s)=\frac{d!}{\prod_{k=0}^d(s-k)},\qquad
 F_d^S(s)=\frac{\sqrt\pi\,4^{-s}S(s+1/2)B_d(s)}
                           {Z\Gamma(s+1/2)},\qquad Z=\gamma_0>0.
\]

Here d is an integer, p=s+1/2, and all branches agree with the
principal ones in those results. Put rho=|s|, r=|p|, L=log r.
The region under test is precisely

\[
 d^{1/3}\le\rho\le d^{2/3},\qquad \Im s\ge\rho/2,\qquad
 r\ge e^{12},\qquad \Re p\ge-r/(4L).                    \tag{1}
\]

No derivative estimate for I/S, saddle contour, sign of a Jensen
polynomial, height implication, or RH is assumed.

## Conclusion

For all sufficiently large integers d, uniformly at every s in (1),

\[
 \Im\frac{(F_d^S)'(s)}{F_d^S(s)}\ge\frac1{30L}>0.          \tag{2}
\]

In particular there is no stationary point of this specified main term
in (1). The proof even permits the sufficient onset d>=exp(36);
no assertion that this onset is sharp is intended.

This is a NEGATIVE answer to the approved stationary-point existence
test and a REPRODUCTION specialization of the assessed branch,
gamma and Rice tools. It is local progress, not a claim of a result
beyond the sources checked. It stops only the proposed use of an
in-region stationary point. Stationary points elsewhere, nonstationary
methods, other representations and RH are not excluded. The result
concerns the explicit S main term, not the actual I integrand.

Independent conceptual audit1672, performed as the essential phase
input to C048n, accepts (2) and the sufficient onset without correction.

## Proof

### 1. Exact derivative and domains of the imported tools

Write q=d+1-s, theta=arg p and theta_s=arg s. The upper-half-plane
condition implies pi/6<=theta_s<=5pi/6. A positive real shift decreases
the argument of an upper-half-plane number, so 0<theta<=theta_s.
Also |arg(-s)|<=5pi/6. For d>=8,

\[
 |p|\ge\rho-1/2\ge\rho/2,\qquad
 \Re q\ge d+1-d^{2/3}\ge d/2,\qquad |q|\ge d/2.          \tag{3}
\]

None of p,-s,q is a gamma pole; none of s,s-1,...,s-d is zero.
C048a gives w=U+iV with U>0 and 0<V<pi/2. C048j fixes the
nonzero S and its locally analytic square root. These branch statements
hold on open neighborhoods, including at the closed sector boundary.
Thus F_d^S is locally holomorphic and nonzero at every point in (1),
and its logarithmic derivative is defined independently of a logarithm
of its value. Gamma is nonzero away from its poles
([DLMF5.2(i)](https://dlmf.nist.gov/5.2#i)).

Reuse C048l(13),(17), without differentiating an asymptotic error:

\[
 B_d(s)=(-1)^{d+1}\frac{\Gamma(d+1)\Gamma(-s)}{\Gamma(q)},
\]
\[
 \frac{S'(p)}{S(p)}=2\operatorname{Log}(w/2)+A(p),\qquad
 A(p)=\frac94\frac{w}{p(1+w)}-\frac1{2p}
                     -\frac{w}{2p(1+w)^2}.
\]

The gamma identity is exact by recurrence, and valid on neighborhoods
of the nonreal points in (1). Since |w/(1+w)|<1 and |1+w|>=1,

\[
 |A(p)|\le\frac{13}{4r},\qquad
 Q_d(s):=\frac{(F_d^S)'(s)}{F_d^S(s)}
 =-\log4+2\operatorname{Log}(w/2)+A(p)
                       -\psi(p)-\psi(-s)+\psi(q).          \tag{4}
\]

In particular the derivative of log Gamma(-s) contributes -psi(-s),
and that of -log Gamma(q) contributes +psi(q). Both signs matter.

Import NIST DLMF version1.2.8,
[5.11.2](https://dlmf.nist.gov/5.11#E2) and
[5.11(ii), first complex-remainder paragraph](https://dlmf.nist.gov/5.11#ii),
as inspected in source-notes1663. The n=1 digamma truncation gives

\[
 \psi(z)=\operatorname{Log}z-\frac1{2z}+R(z),\qquad
 |R(z)|\le\frac{\sec^3(\arg z/2)}{12|z|^2}.
\]

For |arg z|<=5pi/6 this is at most 6/|z|^2, since
cos(5pi/12)>1/4 and 64/12<6. It applies to all three full arguments
in (4), uniformly, by (3) and their fixed angular clearance. This
imports a derivative theorem directly, rather than differentiating
the log-Gamma or Mellin remainders. No fixed-shift approximation with
a growing displacement is used, and no general Rice-saddle theorem
is asserted to apply. The assessment1662 and source-notes1663 document
the comparison with known saddles for different observables.

Put phi=arg w. Since arg(-s)=theta_s-pi, taking imaginary parts of
(4) with this expansion yields

\[
 \Im Q_d(s)=\pi-2\theta+2\phi+e_d(s).                    \tag{5}
\]

Here the error comprises theta-theta_s, arg q, A and the three
digamma corrections. All arguments in this equation are principal;
in particular the pi from -s has not been dropped.

### 2. Uniform error bound in the whole annulus

Integrate 1/z on the segment from s to s+1/2, which stays in the
upper half-plane and at distance at least rho/2 from zero. Consequently

\[
 |\theta-\theta_s|\le1/\rho,\qquad
 |\arg q|\le\frac{|\Im s|}{\Re q}\le\frac{2\rho}{d}.      \tag{6}
\]

For rho>=30 and d>=24, (3),(4) and the imported remainder give

\[
 \begin{split}
 &|A|+\frac1{2r}+\frac1{2\rho}+\frac1{2|q|}
                +\frac6{r^2}+\frac6{\rho^2}+\frac6{|q|^2}\\
 &\qquad\le\frac8\rho+\frac1d+\frac{30}{\rho^2}
                                     +\frac{24}{d^2}
 \le\frac9\rho+\frac2d.
 \end{split}
\]

Thus throughout (1), for d large enough to meet these elementary
conditions,

\[
 |e_d(s)|\le\frac{10}\rho+\frac{2\rho}{d}+\frac2d
         \le\frac{10}\rho+\frac{4\rho}{d}
         \le14d^{-1/3}.                                    \tag{7}
\]

This controls the complete annulus, including its endpoints and its
closed angular boundary. It is not a sample of roots or a pointwise
estimate with an s-dependent constant.

### 3. Principal Lambert argument supplies a positive margin

From w exp(w)=2p/pi and C048a's branch bounds,

\[
 U+\log|w|=\log(2r/\pi).
\]

In fact U>2 for r>=exp(12). Otherwise |w|<=U+V<4 and
r=(pi/2)|w|exp(U)<8exp(2)<exp(12), a contradiction. Since
|w|>2, the same identity also gives U<L. Hence

\[
 U>2,\quad 0<V<\pi/2,\quad
 \phi=\arctan(V/U),\quad \theta=V+\phi.                  \tag{8}
\]

There is no argument wrapping in (8): V+phi<pi/2+pi/4<pi,
and it is positive, so it is the principal argument of p.

The sector in (1) gives

\[
 \theta\le\pi/2+\delta,\qquad
 \delta=\arcsin(1/(4L))\le\frac3{10L}.                    \tag{9}
\]

For the last inequality, arcsin(x)<=6x/5 for 0<=x<=1/2:
its derivative is at most 2/sqrt(3)<6/5 on that interval.
Here L>=12, so it applies.

If theta<=1, then pi-2theta+2phi>=pi-2>1, which is certainly
at least 1/(15L). If theta>=1, (8) and U>2 imply
phi<=V/U<=V/2 and hence V>=2theta/3>=2/3. Also V/U<1,
and arctan(x)>=x/2 on [0,1], by its derivative bound there.
It follows, retaining the full argument of w, that

\[
 2\phi\ge V/U\ge\frac{2}{3L}.
\]

Combining this with (9) gives in this second case also

\[
 \pi-2\theta+2\phi
       \ge-\frac3{5L}+\frac2{3L}=\frac1{15L}.             \tag{10}
\]

### 4. Comparison with the required zero threshold

Uniformly in (1), r<=d^(2/3)+1/2<=d for d>=8, so L<=log d.
The elementary limit log(d)d^(-1/3)->0 implies that (7) is at most
1/(30L) for all sufficiently large d. Together (5),(10) prove (2).
This proves nonvanishing of the derivative itself because F_d^S
is nonzero, rather than just nonvanishing of an auxiliary phase.

For the optional explicit sufficient onset, put v=log d. The function
v exp(-v/3) decreases for v>=3. If d>=exp(36),

\[
 420\log d\,d^{-1/3}\le15120e^{-12}<1,
\]

where e^12>12^10/10!>15120. This onset also ensures d>=27000
and rho>=30, as required for (7). Therefore
14d^(-1/3)<=1/(30log d)<=1/(30L) at that onset.

The conclusion is exclusion in the specified region only. The finite
closing budget of C048l remains valid, but it supplies neither a signed
value of the retained integral nor derivative control of the actual I.
No limit of fixed-d infinite contours, interchange of integrals, zero
count, height criterion or actual-Xi positivity is used or proved.

### Independent conceptual audit1672 — 19 November2026

The full proof was checked as an essential input to assessment1669's
actual-I transfer. Reused C048a's continuation and principal-branch
proof, C048j's audited nonzero S, and C048l's exact identities (13),(17).
The quantitative C048j component proofs are retained, not re-audited
by this phase calculation. Source-notes1663 supplies the inspected
DLMF digamma theorem and its precise remainder; no fresh literature
claim or new source differentiation rule is used.

**Exact derivative and arguments.** The identity
w'=w/[p(1+w)] makes the exponent's extra derivative terms cancel:
2p w'/w - 2/w + 2p w'/w^2=0. The remaining prefactor terms
are exactly A in (4). Since Re w>0, |w|<|1+w| and
|1+w|>1, their sum has modulus at most 13/(4r).
Differentiating the exact finite-kernel gamma identity gives
-psi(-s)+psi(q), with q=d+1-s. The normalization contributes
-psi(p). These signs agree with (4).

The points p,-s,q avoid the nonpositive integers, with arguments
bounded in absolute value by 5pi/6; q is in the right half-plane.
The imported n=1 digamma remainder is
sec^3(arg(z)/2)/(12|z|^2), not the log-gamma remainder.
The inequality cos(5pi/12)>1/4 makes the uniform cap
6/|z|^2 valid. Taking imaginary parts of the three principal logs
gives -theta-(theta_s-pi)+arg q. Thus the exact leading
part is pi-2theta+2phi, with theta-theta_s+arg q in the error.
The pi in (5) is indispensable and has the stated positive sign.

**Uniform error.** Along the half-unit segment from s to p the
modulus is at least rho/2, so the argument change is at most 1/rho.
Also |arg q|<=2rho/d. With r>=rho/2 and |q|>=d/2,
the A term and the p,-s reciprocal corrections cost at most 8/rho;
the q correction costs at most 1/d. The three remainders cost
30/rho^2+24/d^2. For rho>=30,d>=24 this totals
9/rho+2/d. Adding the argument errors gives (7), uniformly at
both annular endpoints. No displacement is treated as a fixed shift
in a gamma-ratio asymptotic.

**Margin and onset.** C048a's strict U>0 and 0<V<pi/2 imply
U>2 when r>=exp(12): otherwise r<8exp(2)<exp(12).
Then U<L, 0<phi<pi/4 and theta=V+phi without argument wrapping.
The sector bounds theta by pi/2+3/(10L). If theta<=1, the
leading phase exceeds 1. If theta>=1, phi<=V/2 implies
V>=2/3, while arctan(V/U)>=V/(2U) gives 2phi>=2/(3L).
In either case the lower bound 1/(15L) in (10) is valid.

For d>=exp(36), L<=log d and
420(log d)d^(-1/3)<=15120exp(-12)<1. The last comparison follows
without a decimal approximation from
12^10=61917364224 > 15120*10!=54867456000 and the positive
exponential series. All subsidiary conditions d>=27000,rho>=30
hold at this onset. Thus the error is at most 1/(30L), proving
the claimed margin. The audit finds no missing boundary case,
branch switch, pole, or degree-dependent constant.

This verification establishes the existing local phase input; it
neither strengthens (2) nor creates a signed-contour or Xi conclusion.
The recorded stationary-point stop retains its original scope.

## Mathlib

Full matching coverage of this principal-Rice stationary-sector
exclusion has not been checked; availability is unknown. No absence
or formal verification is claimed. The supporting inputs are the
precisely cited DLMF digamma remainder, gamma nonvanishing, and the
existing local exact branch and derivative results. The mathematical
content added locally is their combined uniform phase comparison for
this observable, classified REPRODUCTION under assessment1662. The
known derivative theorems alone do not locate this observable's
stationary points; this specialization is necessary for the saved test.
No numerical roots or mathematical script serve as evidence.
