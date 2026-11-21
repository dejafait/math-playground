# C020e — Finite source-index Poisson with a paid outer-summed tail

## Hypotheses

Use exactly C020c's fixed witness and scales as positive integers d tend
to infinity. In particular
\[
 d=\frac{T}{2\pi}(\log(T/(2\pi))-1),\quad T>2\pi e,
 \quad X=T/\sqrt{2d},\quad q=\log X,\quad B=(\sqrt2-1)X,
 \quad h=3\pi/q,
\]
\[
 L=\lfloor X^{1/1000}\rfloor,\quad R=L^4,\quad
 N(Z)=\left\lfloor\sqrt{Z/(2\pi)+Z^2/(32d)}\right\rfloor,
 \quad N_*=N(\sqrt2X).
\]
Keep the original real Euler-product coefficients alpha of zeta^(-1/2)
on Re(s)>1 and all four linear tapers w(a)=(1-log(a)/log L)_+ in
\[
 c_r=\sum_{a_1a_2a_3a_4=r}
   \prod_{j=1}^4\alpha(a_j)w(a_j)(a_2a_4)^{-ih}.
\]
The witness v=p*b runs over unordered distinct primes p<b in
[sqrt(X)/10,sqrt(X)/5]. Retain the original own-time factors
\[
 t(Z)=Z^2/(2d),\quad u(Z)=\tfrac12\log(Z/(2\pi)),\quad
 E_y(Z)=\exp\{\tfrac14t(Z)((u(Z)-\log y)^2-\pi^2/16)
                  +i\pi t(Z)(u(Z)-\log y)/8\},
\]
\[
 \theta(Z)=\tfrac Z2\log(Z/(2\pi))-\tfrac Z2-\pi/8,
 \quad a_v(Z)=b^{-ih}E_p(Z)E_b(Z+h)
                         +p^{-ih}E_b(Z)E_p(Z+h).
\]
For real positive y the displayed formula defines E_y even between
integer sources. F,W,A,C and the mixed channel
\[
 \mathcal M=2\operatorname{Re}\int_{X}^{\sqrt2X-h}
                    W^2(CA+C\overline A)
\]
are exactly C020c's finite reference quantities. No coprimality
restriction, change of alpha, taper, floor, or heat time is made.
No actual-P, resonance estimate, nonvanishing or RH premise is used.
All asymptotic constants below are absolute beyond one integer onset.

## Conclusion

Put J=[X,sqrt(2)X], D0=[X,sqrt(2)X-h], D1=[X+h,sqrt(2)X], and
\[
 f_Z(y)=y^{-1/2-iZ}E_y(Z),\qquad S(Z)=\sum_{m=1}^{N(Z)}f_Z(m).
\]
For each n<=N*, r,s<=R and witness v, set lambda=vr/(ns), and define
\[
 \chi_0(Z)=\mathbf1_{D0}(Z)\mathbf1_{\{n\le N(Z+h)\}},\qquad
 \chi_1(Z)=\mathbf1_{D1}(Z)\mathbf1_{\{n\le N(Z-h)\}},
\]
\[
 \Omega_{nvrs}(Z)=
 n^{ih}\chi_0(Z)\overline{E_n(Z+h)}a_v(Z)
 +\lambda^{ih}\chi_1(Z)\overline{E_n(Z-h)}a_v(Z-h).
 \tag{1}
\]
Every shifted smooth factor here uses its own argument; the two
indicators are not identified. All sums over n,v,r,s below are full.
There is an exact pre-transform identity
\[
 \mathcal M=2\operatorname{Re}\sum_{n,v,r,s}
 \frac{c_r\overline{c_s}}{\sqrt{nvrs}}
 \int_J e^{2i\theta(Z)}\lambda^{-iZ}\Omega_{nvrs}(Z)S(Z)\,dZ.
 \tag{2}
\]

For an integer K>=1 and N=N(Z)>=2 define the explicit finite dual form
\[
 \mathcal T_K(Z)=\frac{f_Z(1)+f_Z(N)}2
       +\sum_{k=-K}^{K}\int_1^N f_Z(y)e^{-2\pi i k y}\,dy.
 \tag{3}
\]
For N=0 set T_K=0, and for N=1 set T_K=f_Z(1). In our asymptotic
regime N>=2 uniformly on J. Let M_K be the right side of (2) with
S replaced by T_K. Then, uniformly in the original integer d,
\[
 |\mathcal M-\mathcal M_K|
 \le C\frac{X^{15/4}R(1+\log R)^2}{K}.
 \tag{4}
\]
In particular the common, explicit choice K=ceil(X^3) gives
\[
 \mathcal M=\mathcal M_{\lceil X^3\rceil}
       +O(X^{377/500}q^2)=\mathcal M_{\lceil X^3\rceil}+o(B),
 \qquad
 \frac{|\mathcal M-\mathcal M_{\lceil X^3\rceil}|}{Bq^2}
       =O(X^{-123/500}).
 \tag{5}
\]
Thus (1)--(3) are a complete finite dual expression with error smaller
than the required o(Bq^2). They retain the zero mode, every mode
|k|<=K, both full endpoint corrections, all common factors and both
translated entry domains. No estimate or sign of M_K is asserted.
The large cutoff is a conservative truncation, not a shortened
arithmetic representation. The endpoint-deletion stop in C020c and
the direct additive-modulus stop in C020d remain valid in their scopes.

## Proof

### 1. Recover both source sums before the prime sum

Use the exact formula C020c (5), without its stationary-phase
approximation. Write kappa=m*lambda. On its first domain J0, the
integrand and exterior coefficient combine to
\[
 \frac{c_r\overline{c_s}n^{ih}}{\sqrt{nvrs}}
 \overline{E_n(Z+h)}a_v(Z)e^{2i\theta(Z)}\lambda^{-iZ}f_Z(m).
 \tag{6}
\]
C020c's entry formula says exactly Z in D0, m<=N(Z), n<=N(Z+h).
On its second domain J1, the exterior m phase satisfies
\[
 m^{ih}e^{-ih\log(m\lambda)}=\lambda^{-ih}.
\]
The second integrand is therefore
\[
 \frac{c_s\overline{c_r}\lambda^{-ih}}{\sqrt{nvrs}}
 E_n(Z-h)\overline{a_v(Z-h)}e^{-2i\theta(Z)}
                        \lambda^{iZ}\overline{f_Z(m)},
 \tag{7}
\]
with exactly Z in D1, m<=N(Z), n<=N(Z-h). In particular the
translation factor is essential for eliminating the exterior m phase.

Inside the real part, conjugate the entire second term (7). Its
coefficient becomes c_r*conjugate(c_s)*lambda^(ih), and its source
weight becomes f_Z(m), the same as in (6). This is a scalar identity
for the real part, not an equality of the original complex channels.
Finite rearrangement of the m sum and Z integral gives (2) and (1).
There is no smoothing, infinite-sum interchange or gcd deletion.
Source-entry equalities keep their original inclusions; singleton
Z intervals contribute zero. Floors still occur explicitly in both
chi factors and in S.

### 2. Source-variable analyticity and derivatives

For fixed real Z in J, use principal Log y on Re y>0 in f_Z. This
is a holomorphic extension on a neighborhood of [1,N(Z)]. The
factor agreeing with conjugate(E_y(Z)) for positive real y has the
same formula with the sign of i*pi*t/8 reversed; it too is holomorphic.
Conjugating a complex argument is not used as an analyticity claim.
In (2) only f_Z needs Poisson, because (7) was conjugated first.

C019's scale calculation gives d comparable to X^2q^2 and
N*=O(sqrt(X)). Hence, uniformly for 1<=y<=N* and Z in J,
t(Z)=O(q^(-2)) and |u(Z)-log y|<=Cq. In particular
\[
 |f_Z(y)|\le C y^{-1/2}.
\]
To check derivatives in the source variable rather than in Z, put
\[
 A_Z(y)=-\tfrac12-iZ-\tfrac{t(Z)}2(u(Z)-\log y)
                              -i\pi t(Z)/8.
\]
Direct differentiation of the specified holomorphic formula gives
\[
 f_Z'(y)=f_Z(y)\frac{A_Z(y)}y,\qquad
 f_Z''(y)=\frac{f_Z(y)}{y^2}
                 \{A_Z(y)^2-A_Z(y)+t(Z)/2\}.
 \tag{8}
\]
Here the primes mean y derivatives, and A_Z'(y)=t(Z)/(2y).
Since |A_Z(y)|<=CX, (8) proves
\[
 |f_Z'(y)|\le CXy^{-3/2},\qquad
 |f_Z''(y)|\le CX^2y^{-5/2}.
 \tag{9}
\]
Thus for every integer 2<=N<=N*,
\[
 Q_Z(N):=|f_Z'(1)|+|f_Z'(N)|+\int_1^N|f_Z''(y)|\,dy
       \le CX^2,
 \tag{10}
\]
using integral_1^infinity y^(-5/2)dy=2/3. None of these bounds
differentiates the moving floor or discards the heat weight.

### 3. Import finite Poisson and pay its symmetric tail

The known input is J.-H. Evertse, *The functional equation for the
Riemann zeta function*, lecture-notes Chapter 9, Section 9.1,
Theorem 9.2, printed p.128, with the endpoint proof of Theorem 9.1
on pp.125--127: https://pub.math.leidenuniv.nl/~evertsejh/ant13-9.pdf .
The inspected undated author-hosted file is ant13-9.pdf (source review
18 November 2026). For integers a<b and f holomorphic near [a,b],
it identifies the full sum from a through b with half the two
endpoint values plus the symmetric limit of the Fourier integrals.
Apply this theorem with a=1, b=N(Z) and the extension above. The
identity is imported, not reproved. Its theorem alone supplies no
uniform moving-parameter truncation rate; that is the difference
checked next under the pre-existing SPECIALIZE assessment1421.

For fixed Z,N abbreviate I_k=integral_1^N f_Z(y)e^(-2*pi*i*k*y)dy.
For k nonzero, two integrations by parts give
\[
 I_k=-\frac{f_Z(N)-f_Z(1)}{2\pi i k}
     -\frac{f_Z'(N)-f_Z'(1)}{(2\pi i k)^2}
     +\frac1{(2\pi i k)^2}
                       \int_1^N f_Z''(y)e^{-2\pi i k y}\,dy.
 \tag{11}
\]
Both endpoints are integers, so every boundary exponential is exactly
one. Consequently the first boundary term cancels in I_k+I_{-k},
without requiring f_Z(N)=f_Z(1). The remaining terms satisfy
\[
 |I_k+I_{-k}|\le\frac{Q_Z(N)}{2\pi^2 k^2}\quad(k>=1).
\]
The paired tail is absolutely summable and
\[
 |S(Z)-\mathcal T_K(Z)|
 \le\frac{Q_Z(N(Z))}{2\pi^2}\sum_{k>K}k^{-2}
 \le\frac{CX^2}{K}.
 \tag{12}
\]
This uses the imported symmetric limit. It does not claim absolute
convergence of the individual I_k. The bound is uniform across every
integer crossing of N(Z). For N=0 or 1 the separate definitions are
exact, so the a<b hypothesis is never misapplied.

At each fixed d there are only finitely many entry crossings. The
finite expressions in (1)--(3) are bounded and piecewise continuous.
We substitute the finite T_K and integrate (12) as an error estimate;
no conditionally convergent series is interchanged with an outer
sum or integral. In particular the discontinuity of a floor needs
no derivative and contributes no omitted boundary distribution.

### 4. Uniform outer payment and limits of the result

C019's heat bounds (or the same real-part estimate used above) give
|E_n(Z+h)|+|E_n(Z-h)|<=C on J for n<=N*, and bounded a_v at
the arguments in (1). Thus |Omega_{nvrs}(Z)|<=C. All other
phases in (2) have modulus one. C019's finite coefficient bounds give
\[
 \sum_{r\le R}|c_r|/\sqrt r\le2\sqrt R(1+\log R),\quad
 \sum_{n\le N_*}n^{-1/2}=O(X^{1/4}),\quad
 \sum_v v^{-1/2}=O(X^{1/2}).
\]
The last estimate compares the witness primes with all positive
integers up to sqrt(X)/5; it uses no distribution theorem. Therefore
\[
 \sum_{n,v,r,s}\frac{|c_rc_s|}{\sqrt{nvrs}}
             \le CX^{3/4}R(1+\log R)^2.
 \tag{13}
\]
Multiplying (12) by (13) and the length O(X) of J proves (4),
including both channels and the factor 2 in the real part. Since
R<=X^(1/250), 1+log R=O(q), and K>=X^3, its exponent is
3/4+1/250=377/500. Dividing by Bq^2 gives X^(-123/500), and
dividing by B gives O(X^(-123/500)q^2), which tends to zero.
This proves (5) along the original integer sequence d.

This is an analytic representation advance within standard finite
Poisson methods, not an estimate beyond the checked literature for
the arithmetic channel. It does not remove C020c's boundary terms:
we started from its exact integrals and retained their entire
domains. The endpoint terms and all retained modes in (3) may be
large. Neither a main form nor cancellation of their outer sum is
proved. C019y's other numerator channels O(G,J), UA, its denominator
and E_P remain unpaid; its separate resonant estimates and C020a/b
are not certified. Later actual-P use keeps the C019t contracts.
No cBq^2 versus O(B) quotient decision, all-degree Xi positivity or
RH candidate follows. A future reduction of the retained dual sum
requires its own source assessment and quantitative error test.

## Mathlib

Full matching Mathlib coverage of this moving-heat, sharp-floor,
outer-summed specialization has not been checked. No absence or
formal verification is claimed. Evertse Theorem 9.2 is the precise
standard identity imported; the parameter bounds, phase combination
and truncation payment above are the local applicability proof.
This new corollary has not yet received an independent conceptual audit.
