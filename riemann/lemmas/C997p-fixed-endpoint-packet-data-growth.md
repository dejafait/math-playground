# Corollary 997p: the fixed theta=1 endpoint packet grows on the data band

## Hypotheses

Use the COMPLETE response H_n^+ of C997c(1), including both beta
terms, both short intervals and K_(n+2)=(L_(n+1)^(2)-1)/(n+1).
Let n>=2 be an integer, delta=1/8, J=[15/8,17/8], beta=1/8+i,
and use the real branches of C997e's phi, q=phi' and b_- on J,
continued holomorphically to C997o's fixed U. Set

    b_n(x)=(1-64*x^2)^n,
    N_n=integral_(-delta)^delta b_n(x)dx,
    dnu_n(c)=1_J(c)*b_n(c-2)*exp(in*(phi(c)-c))dc/N_n,
    s=delta^2*beta/(1+sqrt(1+delta^2*beta^2)), y=Im(s),
    Phi(z)=log(1-64*z^2)+beta*(2+z), S=Phi(s).             (1)

The square root has positive real part. The logarithm is its power
series near zero, on |64*z^2|<1. For the compensated conclusion also
fix A>=A_0>=16 before n and take exactly C997n(1)'s mu_n with
theta=1, lambda=A/128. No parameter varies with n, other than the
specified integer indices. These are hypothetical complex slope
measures, with original total variation one, not actual zeta-zero data.

## Conclusion

Define c_*=2+s and, using the same analytic branches,

    d(c)=3/8+2i-i*q(c),
    a_-(c)=-b_-(c)*(exp(2*c*d(c))-1)/d(c),
    D=sqrt(128/(-Phi''(s)))*a_-(c_*).                     (2)

The quotient is interpreted by its removable value if needed. The
Gaussian square root is continued from positive real numbers in
Re(-Phi''(s))>0. In fact a_-(c_*)!=0, D!=0, and

    Re(S)>15/64>13/64,
    H_n^+(2;nu_n)=n^(-3/2)*exp(n*S)*(D+o(1)),
    H_n^+(2;mu_n)=n^(-3/2)*exp(n*S)*(D+o(1)).             (3)

Consequently both complete responses have logarithmic rate Re(S).
In particular C997n(4) holds with rho=7/32, for all sufficiently
large integers, hence on an unbounded integer subsequence. This stops
uniform exponential data-band suppression only for this fixed
theta=1, lambda=A/128 subfamily. Its target retention remains as in
C997n and C997m; no family-wide stop or RH conclusion follows.

Step359, 11 November 2026: RESEARCH / REPRODUCTION under the unchanged
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-11-11-pure-endpoint-data-rate-review-357.md`.
Outcome NEGATIVE is a local subclass obstruction obtained by
specializing standard analytic tools. It is not progress beyond the
sources checked or certified originality. Independent conceptual
audit was pending at step359; the step361 audit below accepts (1)-(14)
and the concluding comparison without changing their hypotheses or
bounds. This is not an RH candidate.
All constants and asymptotic onsets are existential.

## Proof

### Imported tools and the difference being proved

Use C997e(4),(15)-(16)'s EXACT analytic two-branch amplitudes on the
fixed U certified by the audited C997o. Their source is M. Vanlessen,
*Strong asymptotics of Laguerre-type orthogonal polynomials and
applications in random matrix theory*,
[math/0504604v2, 29 August 2005](https://arxiv.org/pdf/math/0504604v2),
Theorem2.4(b), Proposition3.31, Theorem3.32/(3.110) and
Proposition5.1/(5.5)-(5.6), printed pp5-7,32-34,39. The specialization
Q(x)=x, alpha=2>-1, N=n+1, beta_N=4N and exact normalization are
already justified in C997e/o, including the entire deformation below.
We do not reprove that source theorem or continue a real-axis error.

Use Cauchy's theorem and local holomorphic Taylor expansion, as in
[DLMF1.9.29-31](https://dlmf.nist.gov/1.9#iii) and
[1.10.1-3](https://dlmf.nist.gov/1.10#i), the complex Gaussian integral
[DLMF7.7.3](https://dlmf.nist.gov/7.7#E3), and dominated convergence
in S. Axler, *Measure, Integration & Real Analysis*,
[author version12 June2026](https://measure.axler.net/MIRA.pdf),
Theorem3.31, pp92-93, with the complex-valued extension after6.22,
p157. These are the already inspected contracts in review357 through
review347. Below the Gaussian coefficient has positive real part,
and an explicit integrable majorant pays the n-dependent amplitudes.
The direct limit argument is necessary because a scalar Bessel or
fixed-amplitude saddle formula alone does not pay this complete
response. No general asymptotic theorem is being reproved as new.

The large-theta result in C997m does not cover theta=1. Its elementary
contour strategy motivates this calculation, but none of its unpaid
small-theta estimates is assumed. C997i's degree<=n restriction also
does not cover the present degree 2(n+floor(lambda*n))>n. The prior
stops retain their hypotheses. The work here is the fixed-saddle
quantitative specialization and complete comparison permitted by
review357, not another source search.

### Exact response and original variation

Since b_n>=0 on [-delta,delta], N_n>0, and phi is real on J,
||nu_n||_TV=1. Put x=v/sqrt(n) and extend the rescaled integrand by
zero outside |v|<=delta*sqrt(n). It tends pointwise to exp(-64v^2)
and is bounded by that integrable function, using 1-t<=exp(-t) for
0<=t<=1. Dominated convergence gives

    N_n=n^(-1/2)*(sqrt(pi)/8+o(1)).                       (4)

For the exact B_(+/-,n) in C997e/o define

    a_(+/-,n)(c)=-c*integral_0^2
                        exp(c*u*(3/8+2i))*B_(+/-,n)(c,u)du.

They are holomorphic on a neighborhood of C997o's closed deformation
rectangle K, uniformly bounded there, and converge uniformly to their
holomorphic limits. Finite integration and the uniform O(1/n) limit
in C997e(4) justify these assertions. Its minus limit is exactly a_-
in (2). Expanding cosh and K first, then putting t=c(n+u) in the
upper positive-beta Laguerre term of C997c(1), gives exactly

    H_n^+(2;nu_n)=n^(-3/2)*N_n^(-1)*(I_(-,n)+I_(+,n))+Rem_n,
    I_(-,n)=integral_(-delta)^delta
             (1-64*x^2)^n*exp(n*beta*(2+x))*a_(-,n)(2+x)dx,
    I_(+,n)=integral_(-delta)^delta
             (1-64*x^2)^n*exp(n*beta*(2+x)+2in*phi(2+x))
                                                   *a_(+,n)(2+x)dx,
    |Rem_n|<=C*(n+2)*exp(-n/16).                          (5)

For clarity, the coefficient -2 cancels cosh's 1/2. Before the
measure phase the remaining exponential is
exp(nc*(1/8+2i)+cu*(3/8+2i)); multiplying the measure phase and
exp(-in*phi(c)) leaves exp(nc*(1/8+i)), as in (5).
The other Laguerre exponential leaves the displayed extra 2in*phi.

The remainder consists of the reflected-beta upper Laguerre term,
the ENTIRE constant-subtraction upper term and the COMPLETE lower
interval. As established by C997e's real bound and C997c(5), their
real exponential factors are at most exp(-5cn/8), exp(-3cn/8),
and exp(-n/16), respectively, with only a fixed multiple of n+2.
Here c>=15/8, upper lengths are 2c<=17/4, and original TV is one.
The first two factors follow from exp(-cn/4-3t/8) and
exp(-cn/4-t/8) with t>=cn. The lower bound is exactly C997c(5).
Thus (5) uses no hidden second division by N_n. For each n the
integrands are Borel and absolutely integrable against the product
of Lebesgue measure and finite variation on compact intervals;
substitution and Fubini are justified before taking any limit.

### Fixed saddle, branches and a quantitative lower rate

C997o's audited proof gives |s|<1/112 and 0<y<1/112, and its K
and U cover the full rectangle with vertices +/-delta and
+/-delta+iy in the x variable. Algebra from (1) gives

    beta=2s/(delta^2-s^2), Phi'(s)=0,
    Phi''(z)=-128*(1+64*z^2)/(1-64*z^2)^2.                (6)

No denominator vanishes, since |s|<delta. In particular
|64*s^2|<1/196. The convergent logarithm series and |beta|<9/8
imply

    |S-2*beta|<=|beta*s|+|log(1-64*s^2)|
                <9/896+1/195<1/64,
    Re(S)>1/4-1/64=15/64.                               (7)

For the logarithm bound use sum_(k>=1)|w|^k/k<=|w|/(1-|w|).
This is a rigorous lower bound for the eventual rate, not a sampled
saddle value. Also |Re(s)|<1/112<delta/2, so the saddle is strictly
inside the central horizontal segment.

We will need the sign of Im(phi) on the WHOLE rectangle. Write
c=r+iv, r in J, 0<=v<=y. Then

    |(4-c)/c-1|=2*|c-2|/|c|
       <2*(1/8+1/112)/(15/8)=1/7.

This disk lies in the right half-plane. The branch of its square
root agreeing with the positive real one satisfies
Re(sqrt((4-c)/c))>=sqrt(Re((4-c)/c))>sqrt(6/7)>2/3.
Thus Re(q(c))>1/3 on the rectangle. Integrating the analytic
derivative vertically from the real J gives

    Im(phi(r+iv))=integral_0^v Re(q(r+it))dt>=v/3.        (8)

This explicitly checks the sign on the fixed domain; a sign bound
on an unspecified smaller neighborhood is not being imported.

### Limiting coefficient is nonzero at this fixed point

For c_*=2+s put h=(2-s)/(2+s)-1. Then
|h|=2|s|/|2+s|<2/223. Its chosen square root has positive real
part, so rationalizing the difference from 1 gives

    |q(c_*)-1/2|
       =|h|/(2*|sqrt(1+h)+1|)<1/223<1/112.

Let d_0=3/8+3i/2. We have |d_0|<2, |c_*|<3, and hence

    |c_*d(c_*)-2*d_0|
       <=|s|*|d_0|+|c_*|*|q(c_*)-1/2|
       <5/112<1/16,
    Re(c_*d(c_*))>3/4-1/16=11/16>0.                     (9)

It follows that d(c_*)!=0 and |exp(2*c_*d(c_*))|>1, so the
numerator of (2) cannot vanish. The explicit b_-(c) in C997e(4)
is a product of nonzero fractional powers of c and 4-c and a
complex exponential, on the stated branches; c_* is away from 0
and 4. Thus b_-(c_*)!=0, and a_-(c_*)!=0. No continuity-based
unspecified nonvanishing disk is needed.

### Both endpoint segments and both horizontal outer pieces

Deform each integral in (5) to the horizontal line Im(x)=y.
The polynomial, exact amplitudes and phi are holomorphic on a
neighborhood of the closed rectangle by C997o. Cauchy's theorem
retains both vertical segments. There is no use of a logarithm
on these outer pieces or an assumption that an endpoint zero erases
its vertical contribution.

For delta/2<=|x|<=delta and 0<=v<=y<1/112,

    |1-64*(x+iv)^2|
       <=1-64*x^2+128*|x|*v+64*v^2
       <=3/4+1/7+1/196=44/49.                           (10)

At either vertical side x=+/-delta the sharper bound is
16*v+64*v^2<=29/196<44/49. Everywhere on these pieces,
Re(beta*(2+x+iv))=(2+x)/8-v<=17/64. Since
log(44/49)<=-5/49, both minus outer pieces and both minus
vertical sides have absolute exponential rate at most

    V=17/64-5/49<13/64<Re(S).                            (11)

The extra plus-branch factor has modulus exp(-2n*Im(phi))<=1
by (8), so the SAME bound pays all its corresponding pieces.
Their lengths and exact amplitudes are uniformly bounded. Each
total error is O(exp(n*V)), including the zero at each bottom
endpoint by continuity. All these errors are o(n^(-1/2)*exp(n*Re(S))).

### Central curvature and the complete local limit

On the central horizontal line z=x+iy, |x|<=delta/2,

    |64*z^2|<=1/4+1/196=25/98<1/3.

Thus the logarithm in (1) is a single holomorphic power-series
branch on a neighborhood of that segment. Since n is an integer,
exp(n*log(1-64z^2)) equals exactly the original polynomial factor.
For w=64z^2 with |w|<=1/3, rationalizing gives

    Re((1+w)/(1-w)^2)
      =Re((1+w)*(1-conj(w))^2)/|1-w|^4
      >=(1-|w|-3|w|^2-|w|^3)/(1+|w|)^4>=3/32.

Indeed the numerator is >=8/27 and the denominator <=256/81.
Consequently Re(Phi''(z))<=-12. Write s=a+iy. Integrating this
second-derivative bound on the horizontal line from the stationary
point in (6), in either direction, proves

    Re(Phi(x+iy))<=Re(S)-6*(x-a)^2.                      (12)

In particular Re(-Phi''(s))>=12>0: the saddle is nondegenerate.
For the minus central integral set x=a+v/sqrt(n). After factoring
exp(n*S)*n^(-1/2), its integrand, extended by zero outside the
rescaled segment, converges for every fixed real v to

    exp(Phi''(s)*v^2/2)*a_-(c_*).

This follows from Taylor expansion at the FIXED saddle, (6), and
uniform convergence of the exact holomorphic amplitudes. Both
rescaled endpoints tend to opposite infinities, since |a|<delta/2.
Bound (12) and the uniform amplitude bound give the integrable
majorant C*exp(-6v^2) on all of R, including the varying domains.
Complex-valued dominated convergence and the complex Gaussian
integral therefore give, including the paid outer and vertical pieces,

    I_(-,n)=exp(n*S)*n^(-1/2)*[
           a_-(c_*)*sqrt(2*pi/(-Phi''(s)))+o(1)].         (13)

The Gaussian square root is the analytic branch on Re(-Phi'')>0,
positive on the positive real axis. Its value is nonzero.

On the plus central segment (8) supplies the strict fixed factor
exp(-2ny/3). Together with (12) it gives

    |I_(+,n)|<=C*n^(-1/2)*exp(n*Re(S)-2ny/3)
                         +C*exp(n*V)
                 =o(n^(-1/2)*exp(n*Re(S))).              (14)

Here y>0 is fixed before n; (11) pays both plus vertical sides and
outer pieces. Thus no possible cancellation with a same-scale
uncontrolled branch is being suppressed. Equation (9) guarantees
that the actual surviving coefficient in (13) is nonzero.

Insert (4), (13)-(14) in (5). Its COMPLETE Rem_n is exponentially
smaller on this scale because Re(S)>15/64 and its rate is -1/16.
The leading factor is
(8/sqrt(pi))*sqrt(2*pi/(-Phi''(s)))*a_-(c_*)=D, proving
the pure-endpoint assertion in (3), through all large integers.
All convergence is for fixed parameters; n>=63 in C997o certifies
only geometric containment, not an effective asymptotic onset.

### Compensation and the precise scope of the obstruction

C997n(3), already audited, gives on this same fixed subfamily

    |H_n^+(2;mu_n)-H_n^+(2;nu_n)|
                                  <=C*n^(-1)*exp(13n/64).

After multiplication by n^(3/2)*exp(-n*S), its absolute value is
at most C*sqrt(n)*exp(-(Re(S)-13/64)*n), tending to zero by (7).
This proves the second asymptotic in (3) with the SAME nonzero D.
Taking absolute values and logarithms now proves the asserted rates.
Since 7/32<15/64<Re(S), the polynomial prefactor and nonzero
coefficient give |H_n^+(2;nu_n)|>=exp(7n/32) eventually, not
merely on a numerically observed subsequence. C997n's conditional
transfer also gives |H_n^+(2;mu_n)|>=exp(7n/32)/2 eventually.

Because 2 lies inside the closed data band, this is inconsistent
with uniform exp(-sigma*n) suppression, for any fixed sigma>0,
even on an unbounded subsequence of this subfamily. C997n's cited
target-retention conclusion remains valid. We have not excluded
other fixed parameters, n-dependent parameters, other phases or
densities, or a different point-bridge mechanism.

The main actual-Xi gap L030-L032/C032a, signed forcing in L966/L968,
unpaid L984(H), the point bridge, selected/both-sign transfer,
C997a(8), assay/reconstruction, signed recovery, complementary zeros,
regulators and L993 remain open. No cross-notebook input is used.

The elementary rational margins in (7),(9)-(12), and the chosen rho,
are independently replayed by
`python3 scripts/endpoint-packets/pure-endpoint-rate-bounds-359.py`.
Its full exact-rational certificate is
`scripts/endpoint-packets/pure-endpoint-rate-bounds-359.json`.
This arithmetic check is not a verification of the source contracts,
analytic branches, dominated-convergence argument or the entire proof;
those are addressed by the separate conceptual audit below.

### Independent conceptual audit — step361, 11 November 2026

RESEARCH / REPRODUCTION under the unchanged SPECIALIZE assessment
`drafts/literature/2026-11-11-fixed-endpoint-rate-audit-review-359.md`,
separately approved in step360, exactly its COVERED_TARGET. The audit
accepts (1)-(14) and the complete compensation comparison. No bound,
parameter range or onset is strengthened. This verifies a previously
unaudited local specialization; it is not a new general theorem or
progress beyond the sources checked.

**Source contracts and domains.** Reuse the inspected Vanlessen,
Cauchy/Taylor, Axler and Gaussian contracts cited above and the source
comparison in assessment359. C997e(15)-(16) give an exact identity,
with both entries of the residual matrix retained inside the two
amplitudes. The hypotheses are Q=x, alpha=2>-1, N=n+1 and beta_N=4N;
no degree-dependent change of weight is passed to Vanlessen. C997o's
audited conclusion supplies the fixed U and uniform limits on a
neighborhood of its closure, for every u in [0,2]. Its K contains the
whole deformation, not just the saddle. Thus integrating the exact
amplitudes in u gives holomorphic, uniformly bounded a_(+/-,n) and
uniform convergence on K. The compact-support indicator is only used
on the original real integral; it is not analytically continued.

**Normalization and the complete identity.** On real J the packet
phase has modulus one and b_n is nonnegative, so original TV is exactly
one. After x=v/sqrt(n), the zero-extended normalization integrands are
bounded by exp(-64v^2) and converge to it at each fixed v. Both rescaled
endpoints escape, proving (4) with sqrt(pi)/8, without changing the
measure norm. Expanding K and cosh before substitution gives coefficient
-1 for the positive-beta upper Laguerre term. Its exponent is exactly

    -cn/4+t/2-t/8+2it
        =nc*(1/8+2i)+cu*(3/8+2i), t=c*(n+u).

The Jacobian is c. Multiplying by the measure phase cancels the minus
Laguerre phase, leaving beta=1/8+i; the plus phase leaves +2i*phi.
These checks give (5), including its sign, n^(-3/2) and only one N_n
division. The reflected-beta upper term has factor exp(-cn/4-3t/8),
and the entire constant subtraction is bounded with factor
exp(-cn/4-t/8). Since t>=cn and c>=15/8, both decay faster than
exp(-n/16). C997c(5) pays the COMPLETE lower interval in original TV.
All three bounds are for the normalized measure before any deformation;
none receives another N_n^(-1). Compact Borel integrands against the
finite product variation justify the substitutions and finite Fubini.

**Saddle and branches.** The chosen root satisfies
beta*(delta^2-s^2)=2s, hence (6). C997o's audited calculation has
sqrt(1+delta^2*beta^2)=p+iq, p>31/32 and 0<q<1/496; it proves
|s|<1/112 and Im(s)>0. Thus the central saddle is interior and
|64s^2|<1/196. The power-series logarithm gives the loss in (7),
2651/174720<1/64, so Re(S)>15/64. On the full rectangle the ratio
(4-c)/c is in the disk of radius 1/7 about 1. Its square root agrees
with the real branch and has real part greater than sqrt(6/7).
Integrating Re(q)>1/3 vertically proves (8), also at both sides.
This sign is available on every piece of both deformations.

At c_*=2+s the ratio differs from 1 by less than 2/223. Rationalizing
its square root, whose real part is positive, gives
|q(c_*)-1/2|<1/223<1/112. Since |d_0|<2 and |c_*|<3,
the error in c_*d(c_*) from 2d_0 is less than 5/112<1/16.
Its real part therefore exceeds 11/16. In particular d(c_*) is
nonzero and exp(2c_*d(c_*)) cannot equal 1. All factors of b_-(c_*)
are nonzero on the fixed branches away from 0 and 4. This verifies
the actual amplitude in (2), rather than assuming nonvanishing in an
unspecified neighborhood of the real center.

**Every contour contribution.** The polynomial factor and exact
amplitudes are holomorphic on a neighborhood of the closed rectangle;
Cauchy's theorem therefore retains two vertical sides as well as the
horizontal segment. For delta/2<=|x|<=delta the three-term triangle
bound in (10) uses 1-64x^2>=0 and is at most 44/49. At x=+/-delta
that first term is zero, giving the stricter 29/196. The remaining
real exponent is (2+x)/8-v<=17/64, so all four outer pieces for the
minus branch have rate at most V=513/3136<13/64. The plus factor has
modulus at most one there by (8). Fixed lengths and bounded exact
amplitudes give O(exp(nV)) errors for both integrals. Their ratios to
n^(-1/2)*exp(n*Re(S)) tend to zero. A real endpoint zero alone has
not been used to discard either vertical segment.

**Curvature and the varying-amplitude limit.** On the central segment,
|64z^2|<=25/98<1/3. For w=64z^2, the real numerator after
rationalization is

    Re((1+w)*(1-conj(w))^2)
      =1-Re(w)-2|w|^2+Re(w^2)+|w|^2*Re(w)
      >=1-|w|-3|w|^2-|w|^3>=8/27.

The positive denominator is at most 256/81, giving (12)'s curvature
bound Re(Phi'')<=-12. The real derivative on the horizontal line
vanishes at s; integration in either direction gives the quadratic
drop 6(x-Re(s))^2. The logarithm is a single power-series branch
there and exponentiates to the polynomial for integer n. At each
fixed real v, Taylor expansion gives
n*(Phi(s+v/sqrt(n))-S)->Phi''(s)*v^2/2. Uniform amplitude convergence
and continuity give a_(-,n)(c_*+v/sqrt(n))->a_-(c_*).
The zero-extended rescaled integrands have the common integrable
majorant C*exp(-6v^2), and both endpoints tend to opposite infinities.
This checks Axler's infinite-domain, complex-valued dominated-convergence
hypotheses for the varying amplitudes, rather than applying a fixed-
amplitude saddle formula. Re(-Phi''(s))>=12 ensures the stated Gaussian
branch and its nonzero integral. Together with the paid outer terms
this proves (13).

For the plus central integral the additional factor is at most
exp(-2ny/3), with fixed y>0. The same quadratic majorant supplies
the n^(-1/2) factor in (14); the other four pieces are already paid.
Thus no same-scale contribution can cancel the minus coefficient.
Combining (4) and (13) gives the exact constant
(8/sqrt(pi))*sqrt(2*pi/(-Phi''(s)))*a_-(c_*)=D.
The complete Rem_n is smaller even after multiplication by
n^(3/2)*exp(-n*S), since its real rate is -1/16.

**Compensation, quantifiers and scope.** C997n(3) is uniform on the
closed J, hence applies at 2. Its correction, divided by the obtained
leading scale, is O(sqrt(n)*exp(-(Re(S)-13/64)*n))=o(1).
It therefore leaves the same nonzero D for mu_n. For either response,
|D+o(1)| is bounded below by |D|/2 eventually, so taking the modulus
removes the harmless phase exp(in*Im(S)); no favorable subsequence
or assumed noncancellation is needed. Since

    13/64 < 7/32 < 15/64 < Re(S),

C997n(4) is now supplied with rho=7/32 through all sufficiently large
integers. Parameters A>=A_0>=16 and lambda=A/128 remain fixed; the
contour and all analytic onsets are independent of n but existential.
No n-dependent parameter or uniform effective onset is asserted.

The existing exact-rational script was read and replayed: all 19 checks
passed, with no failures, in the certificate named above. It corroborates
only the elementary margins; the analytic checks in this audit supply
the remaining justification. Direct mathematical inputs stay C997c/e/n/o;
no DAG edge changes. Target retention is used only through C997n's
existing conclusion. C997i/m remain scoped contrasts, not extra premises.
Other slope families, the general point bridge and the listed selected-
response, actual-Xi, signed-forcing and H gaps remain unresolved.

## Mathlib

Full matching coverage for this weighted complete-response saddle
specialization has not been checked and is unknown. Cauchy/Taylor,
dominated convergence and Gaussian integration are standard informal
inputs here; no matching Mathlib theorem name, absence claim or Lean
verification is asserted.
