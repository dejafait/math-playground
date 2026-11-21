# Lemma 704: a partial payment of the complete inner-disk charge

## Hypotheses

Fix one actual profile e from audited L703, with every choice made
before n. Use L666's exact family, including its unit masses, anchor,
j=0 factor, inverse denominator angle and all M spatial moments:

    n=12q+3, q>=1, M=4q+1=n/3, J=n-1, h=A/n,
    A=27/10, x=-d=-5/4, R=11/8, U=R^2=121/64, Y=9/20,
    a_m=x+i*h*(m+1/2+e_m), -2q<=m<2q,
    T_M(z)=sum_(k=0)^(M-1) z^k,
    G_n(u,zeta)=R^(-1)*[T_M(x*zeta/R)
                +sum_m W_(a_m)(u)*T_M(a_m*zeta/R)].

Here W is the full rational continuation in L666 (6). Retain L657's
complete numerator K and denominator Q. Set r=1/2 (an angular disk
radius, unrelated to the Picard ball radius), s=1/10000 and

    t_j=j/n, p_j=-d*j/(U*n) (1<=j<n), tau=r*U/d=121/160,
    P_n=sum_(|p_j|<r) log(r/|p_j|),
    Z_n=mean_(|zeta|=1) sum_(K(beta,zeta)=0, |beta|<r)
                                      log(r/|beta|).

The last sum counts multiplicities and cancelled Q factors. As in
L657, omit the finite spatial set with K(0,zeta)=0. All means are
normalized. No separation of numerator roots, simple-root hypothesis,
reflection, gap for a head/path profile or signed-residue hypothesis
is imposed. L703 supplies, for this same fixed e,

    sum_m |e_m|<infinity, |e_m|<=1/8,
    F_(2pi) mu=1+delta_0-chi_w on (-3/8,3/8),
    mu=delta_0+sum_m delta_(m+1/2+e_m),
    chi_w=0 on (-1/8,1/8).

The Fourier identity, including its off-support part, is established
in L703 Sections 5-6 for the actual prescribed data.

## Conclusion

The complete charge Z_n is finite. For this fixed profile, eventually

    Z_n >= n/4000,              P_n/n -> 121/160.             (1)

More precisely, putting kappa=4999/5001,

    liminf Z_n/n >= gamma,
    gamma=[2057/1600000-(1-kappa)*(401/160)]/kappa
                                                   >1/4000. (2)

The onset may depend on the fixed profile and is not effective. The
positive-point comparison used in the proof retains the full spatial
polynomial and is uniform on its entire circle:

    G_n(s,zeta) -> 1/[R*(1-x*zeta/R)],       |zeta|=1.         (3)

This is a small quantitative partial payment of the approved target
Z_n>=P_n-o(n), not that target. The certified bound still permits a
linear deficit up to (189/250)n+o(n); it does not prove that any such
deficit actually occurs. The remaining inner charge, annulus, complete
mean, H/support and Xi realization/signs are open. There is no RH
candidate. The separate conceptual audit in Section 7 accepts this
local specialization of known contour, Fourier and Jensen tools, with
its fixed-profile and existential-onset qualifications. No originality
beyond the sources checked is claimed.

## Proof

### 1. Approved scope and precise source imports

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-gevrey-inner-disk-complete-charge-scope.md`.
Its exact target permits a useful partial weighted payment. L657
supplies the actual K,Q and center exceptions; L666 supplies the
admissible family; L703 supplies the fixed profile and displayed Fourier
identity. The common-shift conclusion of L690 is not used at this new
radius. Its exact finite-contour method is specialized below instead.
L700/L701's scalar stops and C703a's absolute-variation failure are
contrasts, not inputs or claims about this full charge.

Import the following known tools through the saved assessments and
their cited local source interfaces, without reproving the theorems:

* F. Brunault and W. Zudilin, *Many Variations of Mahler Measures*,
  ISBN 9781108794459, [Propositions 1.4-1.5, pp.6-7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf):
  the complete polynomial root integral, including boundary roots.
* Z. Issa and M. Lalin, *A generalization of a theorem of Boyd and
  Lawton*, [arXiv:1203.5379v1, Remark 3.8 and Theorem 4.1/proof,
  p.7](https://arxiv.org/pdf/1203.5379v1), s=1: absolute logarithmic
  integrability of a nonzero polynomial. No degree-uniform constant
  is imported.
* T. Tao, *246B, Notes 1*, 23 December 2020,
  [Theorem 2 and proof (3)-(5)](https://terrytao.wordpress.com/2020/12/23/246b-notes-1-zeroes-poles-and-factorisation-of-meromorphic-functions/):
  Jensen's formula on a disk for a meromorphic function with a finite
  nonzero center value. Below it is applied to an analytic rational
  function after an explicit disk automorphism. Boundary cases use
  the finite root formula, not an unproved limiting interchange.
* R. B. Ash and W. P. Novinger, *Complex Variables*, hyperlinked web
  text, [Theorem 4.8.3, printed pp.33-34, and Lemma 4.8.4,
  pp.34-36](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesWithHyperlinks.pdf#page=94):
  Poisson--Jensen for a function analytic near the closed disk and
  nonzero at its interior evaluation, allowing boundary zeros and
  their improper logarithmic integrals. Corollary 4.7.4, printed p.27,
  gives Poisson kernel mass one. These exact boundary cases were
  inspected in the separate step-149 source assessment. Its proof's
  even-kernel calculation applies here because s is real; no such
  symmetry is assumed for a general complex evaluation point.
* J. H. Mathews and R. W. Howell, *Complex Analysis*,
  [Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
  and [Section 6.2, Theorems 6.2.18-6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html):
  the residue theorem, simple-pole rule and contour bound, as already
  used in L690. Every pole of the changed rectangle is checked below.
* S. D. Miller, *Some notes on distributions*, 15 January 2006,
  [Theorems 4.1-4.2 and Section 6, pp.7-9](https://sites.math.rutgers.edu/~sdmiller/musagei/distributions.pdf):
  Schwartz Poisson summation and Fourier duality, reused from the
  L694/L696 source interface only for the translated lattice comb.

The new applicability work is the positive-radius finite contour,
uniform transfer of the actual summable shifts, whole-boundary upper
estimate and the signed Poisson comparison. It is not an assumed
strict Rouche inequality, a scalar sample or a generic root count.

### 2. The exact unshifted finite sum at the positive point

Temporarily put all shifts equal to zero and keep the anchor separately.
For complex y=z+i*v let a=x+i*y=-d-v+i*z. At the fixed real u=s define

    f(t,z,v)=log|(d+t*s)/(d+v+t*s-i*z)|
              +log|(U*s+t*(d+v)-i*t*z)/(U*s+t*d)|,
    Phi(z,v)=integral_0^1 f(t,z,v)dt,
    omega=A*integral_0^1 [1/(d+t*s)-t/(U*s+t*d)]dt,
    lambda=2*pi/A.

All denominators, and the numerator inside the second logarithm, are
nonzero on a sufficiently small fixed rectangle |z|<=Y, |v|<=v_0.
At v=0,

    f(t,z,0)=(1/2)log[1+t^2*z^2/(U*s+t*d)^2]
                 -(1/2)log[1+z^2/(d+t*s)^2].              (4)

Since t*(d+t*s)<U*s+t*d for 0<=t<=1, (4) is strictly negative
when z!=0. Also Phi(0,0)=0 and

    partial_v Phi(0,0)=-omega/A,
    0<omega<=A/d<2*pi.                                  (5)

Here positivity follows directly from

    1/(d+t*s)-t/(U*s+t*d)
          =s*(U-t^2)/[(d+t*s)*(U*s+t*d)]>0.

These facts give a complete rectangle bound, not just endpoint data.
Near z=v=0, continuity makes partial_v Phi strictly negative and
partial_v(Phi+lambda*v) strictly positive. For sufficiently small
fixed v_0>0 this makes Phi(z,v_0)<0 and
Phi(z,-v_0)-lambda*v_0<0 for all sufficiently small |z|,
using Phi(z,0)<=0. On the remaining compact z intervals, (4) is
strictly negative; decreasing v_0 preserves that negativity on both
horizontal edges and on both vertical sides. Take also v_0<1/100.
Then |a|^2<=(d+1/100)^2+Y^2=17901/10000<U=R^2.

Put Y_n=2q*h=Y-A/(2n), and let Gamma_n be the positive boundary
of [-Y_n,Y_n]+i[-v_0,v_0]. The preceding compact estimates imply,
for some fixed epsilon>0 and all sufficiently large n,

    Phi(z,v)-lambda*(-v)_+ <= -epsilon on Gamma_n.        (6)

Indeed Y_n->Y, and the vertical sides remain in the compact negative
region, bounded away from z=0. All assertions so far are for the fixed
s, not uniform as s tends to zero.

Use the exact half-lattice kernel

    J_n(y)=-i*lambda*n/[exp(i*lambda*n*y)+1].              (7)

Its poles inside Gamma_n are exactly y=h*(m+1/2),
-2q<=m<2q, each of residue one. On a vertical side the exponential
has argument an integer multiple of 2*pi, since Y_n=2q*h. On the
two horizontal sides the elementary bounds for |1+exp(i*lambda*n*y)|
give, for all sufficiently large n,

    |J_n(z+i*v)|<=2*lambda*n*exp[-lambda*n*(-v)_+].       (8)

The other factor W_(x+i*y)(s) has no poles in the rectangle:
a=0 and a=t_j*s correspond to Im y<=-d. Its j=0 factor x/a is
bounded on the rectangle. The summands f and their t derivatives
are uniformly bounded there, so the finite-product Riemann sum gives

    log|W_(x+i*y)(s)|=n*Phi(z,v)+O(1)                    (9)

uniformly on Gamma_n. The bound |a|<R makes
|T_M(a*zeta/R)| uniformly bounded for every |zeta|=1 and every M.
The residue theorem applied to J_n(y)W_(x+i*y)(s)T_M(a*zeta/R),
with (6)-(9) and bounded rectangle length, therefore gives

    sum_(-2q<=m<2q) W_(x+i*h*(m+1/2))(s)
                    *T_M((x+i*h*(m+1/2))*zeta/R)
                         =O(n*exp(-epsilon*n)),          (10)

uniformly on the spatial circle. Both actual endpoints are included.
No infinite lattice sum or discarded signed interior has replaced
this finite contour. Thus its anchored G_(n,0)(s,zeta) converges
uniformly to 1/[R*(1-x*zeta/R)].

### 3. Transferring the actual fixed profile on the whole spatial circle

For real xi write W_(x+i*h*xi)(s) as

    (1-i*lambda_0*xi)^(-1)
          *product_(j=1)^J (1-i*beta_j*xi)/(1-i*lambda_j*xi),
    lambda_0=h/d, lambda_j=h/(d+t_j*s),
    beta_j=h*t_j/(U*s+t_j*d).                            (11)

We have 0<=beta_j<lambda_j<=h/d. Consequently |W|<=1 and
|partial_xi W|<=lambda_0+sum_j(lambda_j+beta_j)<2*A/d
on the whole real line. The derivative estimate follows directly by
logarithmic differentiation; all factors in (11) are nonzero there.

Along every allowed shift segment, |a|<=r_*=273/200<R. With
rho=r_*/R, the geometric-series derivative bound yields

    |T_M(a*zeta/R)|<=1/(1-rho),
    |partial_xi T_M(a*zeta/R)|<=h/[R*(1-rho)^2].          (12)

Thus the difference of the two summands at m+1/2+e_m and m+1/2
is bounded uniformly in n,zeta by C*|e_m|. For each fixed xi,
expanding the logarithms in (11) gives

    W_(x+i*h*xi)(s) -> exp(i*omega*xi).                  (13)

Indeed the linear coefficient is lambda_0+sum(lambda_j-beta_j)
and tends to omega by a Riemann sum; the quadratic remainder is
O_xi(n*h^2)=O_xi(1/n). Also T_M(a*zeta/R) tends uniformly to
(1-x*zeta/R)^(-1). Absolute summability of e and (12) therefore
justify uniform dominated summation, including the expanding finite
endpoints. The difference G_(n,e)-G_(n,0) tends uniformly to

    S_e(omega)/[R*(1-x*zeta/R)],
    S_e(v)=sum_(m in Z) exp(i*v*(m+1/2))
                                      *[exp(i*v*e_m)-1]. (14)

This series converges uniformly on compact real v intervals because
each difference has modulus at most |v|*|e_m|. It is the continuous
Fourier transform of mu minus its anchored unshifted comb, evaluated
with positive exponent. To check the distributional identification,
pair with a compactly supported smooth frequency test; its integrand
is bounded by a constant times |e_m|. Fubini applies to the differences.
Equivalently the spatial delta differences act by an absolutely
convergent sum bounded by ||phi'||infinity*sum|e_m|.

The translated-comb Fourier identity gives
F_(2pi)(delta_0+sum delta_(m+1/2))=1+sum_k(-1)^k delta_k.
Subtract this from L703's actual identity. On (-1/8,1/8), both chi_w
and the difference of the two frequency atoms at zero vanish. Hence
S_e(-2*pi*t)=0 there, first distributionally and then pointwise by
continuity. In particular S_e(omega)=0: explicitly,

    omega <= (A*U*s/d^2)*log(1+d/(U*s))
           <3267/1000000<1/2<pi/4.                     (15)

For the middle inequality, 1+d/(U*s)=1+800000/121<10000 and
log 10000<10, since exp(1)>8/3 and (8/3)^10>10000.
Together (10),(14),(15) prove (3). In particular, uniformly in zeta,
|G_n(s,zeta)| is eventually at least 1/[2*(R+d)]>0 and

    m_s:=mean_zeta log|G_n(s,zeta)| -> -log R.            (16)

The value of the limit mean follows from the cited root formula and
|x|/R<1. Uniform convergence and the positive lower modulus justify
passing to this logarithmic mean. No truncated profile has been
assigned a gap, and no scalar coefficient substitutes for G.

### 4. A bound on the complete radius-1/2 boundary

For |u|=r and any original node a=x+i*y, |y|<=Y, we have

    |(x-t*u)/(a-t*u)|<=1+Y/(d-r)=8/5,
    |(U*u-t*a)/(U*u-t*x)|
                        <=1+(9/25)/|t-tau|.            (17)

The first follows from the triangle inequality and
|a-t*u|>=d-t*r>=d-r. The second uses
|U*u+t*d|>=|U*r-t*d| and t<=1. The j=0 factor has modulus<=1.
Here tau*n is never an integer: n is odd and gcd(121,160)=1.
For t=j/n its distance from tau is at least 1/(160*n).

Let c=9/25 and f_0(t)=log(1+c/|t-tau|). The full products and
all M summands therefore obey

    log|G_n(u,zeta)|<=log(100*M)+J*log(8/5)
                                  +sum_(j=1)^J f_0(j/n). (18)

This is uniform on both circles, including spatial zeros. The factor
100 is exactly 1/[R*(1-rho)]. On each side of tau, f_0 is monotone.
Compare its grid sum with the integral cell by cell, excluding the
at most two adjacent cells. Their integral is O((log n)/n), and
their sampled terms are O(log n) by the rational distance bound.
The same monotone comparison on the remaining cells has error
O(log n). It follows that

    sum_(j=1)^J f_0(j/n)=n*I+O(log n),
    I=F(tau)+F(1-tau),
    F(b)=b*log(1+c/b)+c*log(1+b/c).                      (19)

F''(b)=-c/[b*(b+c)]<0. Hence I<=2*F(1/2), and

    log(8/5)+I
      <=log(8/5)+log(43/25)+(18/25)*log(43/18)
      <1/2+3/5+(18/25)*(9/10)=437/250<7/4.              (20)

Each strict logarithmic inequality follows by lower-bounding its
exponential with respectively the degree-3, degree-2 and degree-3
positive Taylor sums; the exact rational checks are recorded below.
Thus, on the entire boundary,

    log|G_n(u,zeta)| <= U_n,
    U_n=(7/4)*n+O(log n).                               (21)

This is an upper bound used inside a signed comparison. It is never
reported as a lower bound for the actual response or loss.

### 5. Complete divisors, the signed boundary comparison and the margin

Put b_j=|p_j| and form the finite disk Blaschke product

    B_n(u)=product_(b_j<r) r*(u+b_j)/(r^2+b_j*u),
    F_n(u,zeta)=B_n(u)*G_n(u,zeta).                      (22)

Every angular pole inside |u|<r is among these simple p_j. L666's
other poles have modulus>=d>r; the remaining p_j are strictly outside
the closed disk. Hence F_n is analytic on a neighborhood of that
closed disk. Its zeros inside are exactly the complete K zeros:
in F_n=B_n*K/Q, the inner Q factors cancel B_n's factors, leaving
a multiplier of K holomorphic and nonzero throughout the disk.
This remains true when a pole of G already cancels. Multiplicities
and those extra numerator zeros are retained, not removed.

We have |B_n|=1 on |u|=r and log|B_n(0)|=-P_n. The polynomial
K(r*v,zeta) is nonzero, and K(0,zeta) has only finitely many circle
zeros by L657. The imported integrability theorem applies to these
polynomials; the remaining rational factors have no boundary poles.
The finite root formula, for almost every spatial slice and then
Fubini, gives

    A_r:=mean_(|u|=r,|zeta|=1) log|G_n(u,zeta)|
                              =m_0+Z_n-P_n,            (23)
    m_0=mean_zeta log|G_n(0,zeta)|=log M+O(1).

The last bounds are precisely L657 (4). The same root formula proves
Z_n finite and nonnegative; boundary numerator zeros have zero weight
and integrable logarithms. Center exceptions are omitted only from
the almost-everywhere root identity, never assigned an infinite value.

By (3), F_n(s,zeta)!=0 for every |zeta|=1 once n is large. Apply
Jensen to F_n composed with u=r*(v+s/r)/(1+(s/r)*v). This automorphism
sends 0 to s and the unit circle to |u|=r. Its boundary change of
variable gives the Poisson weight

    P_s(theta)=(r^2-s^2)/|r*exp(i*theta)-s|^2,
    mean_theta P_s=1,   P_s>=kappa=(r-s)/(r+s)=4999/5001.

The source center condition is therefore satisfied. Boundary zeros
are covered by rational factorization and the imported boundary root
case. Equivalently, Ash--Novinger Theorem 4.8.3 applies directly with
R0=r and evaluation s. Its interior-zero terms are nonpositive.
Thus for each spatial slice

    log|F_n(s,zeta)|<=mean_theta P_s(theta)*log|F_n(r*exp(i*theta),zeta)|.

On that boundary log|F_n|=log|G_n|<=U_n. Since P_s-kappa>=0,
the right side is at most kappa*mean_theta log|G_n|+(1-kappa)*U_n.
All logarithms are integrable as just proved, so spatial integration
is justified, with no exceptional spatial contribution discarded:

    kappa*A_r >= log|B_n(s)|+m_s-(1-kappa)*U_n.          (24)

Define the exact increase from the center

    D_n=log|B_n(s)|+P_n
       =sum_(b_j<r) [log(1+s/b_j)-log(1+b_j*s/r^2)].     (25)

The grid b_j=d*j/(U*n) gives

    P_n/n -> tau,
    D_n/n -> D=(U/d)*integral_0^r
                         [log(1+s/b)-log(1+b*s/r^2)]db. (26)

For the first, write P_n=N*log(tau*n)-log(N!), N=floor(tau*n);
integral comparison for log(N!) gives tau*n+O(log n). For the
second, the first integrand has only an integrable logarithmic
singularity at zero. Its monotone right Riemann sums converge, with
the first-cell integral O((log n)/n); the second integrand is smooth.
These checks include the last partial cell and require no formal
interchange with a varying zero set.

The two elementary integral bounds give

    integral_0^r log(1+s/b)db
        =(r+s)*log(1+s/r)+s*log(r/s)>=s+s*log(r/s),
    integral_0^r log(1+b*s/r^2)db<=s/2.

Consequently

    D >= (U/d)*s*[log(r/s)+1/2] >2057/1600000.            (27)

Here r/s=5000 and log 5000>8. For example the exponential series
gives exp(1)<8/3+5/96=87/32<11/4, while (11/4)^8<5000.

Combining (23)-(25), with every sign retained, yields

    kappa*Z_n >= D_n+m_s-kappa*m_0
                              -(1-kappa)*(P_n+U_n).    (28)

Use (16),(21),(26),(27) and m_0=O(log n) in (28). This proves
(2), since tau+7/4=401/160 and

    [2057/1600000-(2/5001)*(401/160)]*(5001/4999)
                                                    >1/4000.

The strict margin implies the eventual inequality (1), without
asserting an effective onset. This is a complete weighted lower
charge from a signed full-boundary comparison. It does not use a
favorable subset, scalar residues, microscopic pairing or the stopped
absolute-tail variation estimate.

### 6. Verification and limits

The small exact-arithmetic certificate checks the radius and frequency
constants, the exponential-series inequalities in (15),(20),(27),
and the strict final margin. From the notebook root run

    python3 scripts/one-sided-hankel/inner-disk-charge-148.py

It writes the full certificate to
`scripts/one-sided-hankel/inner-disk-charge-148.json` and prints the
actual/required margins and failures. It does not certify the analytic
contour, uniform limit, source theorems or Jensen argument. Section 7
records the separate audit of the local analytic applications; it does
not assert an independent audit of every imported source manuscript.
There is no numerical approximation of the Picard profile or zero
census, and no numerical evidence is a premise of (1).

The bound n/4000 pays only 1/3025 of the leading pole charge
(121/160)n. In particular the proof does not establish an o(n)
deficit, any sign of the complete full-circle mean, or any of the
independent actual-Xi assumptions. Increasing this constant by a
routine arithmetic optimization is not by itself a route to the
missing compensation.

### 7. Separate conceptual audit — 3 November 2026, step 150

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-03-inner-disk-charge-partial-audit-scope.md`.
This audit checks the claimed partial bound, not a larger compensation
constant. The full argument passes. No additional hypothesis or
substantive mathematical repair is needed. The pole index range in
the hypotheses is made explicit, and the approved boundary-zero
Poisson--Jensen citation is recorded in Section 1.

**Finite contour and order of choices.** In (4), strict negativity
for z!=0 follows from t^2<U, including t=0. Near the origin choose
a fixed small z neighborhood and v strip where both
-partial_v Phi and partial_v(Phi+lambda*v) are positive, using
0<omega/A<lambda. Integrating these derivatives from v=0 makes
the upper and lower horizontal edges strictly negative after the
kernel correction. On the complementary compact z set, Phi(z,0)<0
has a fixed negative margin; continuity preserves it throughout a
sufficiently thin v strip. This also covers the entire vertical
edges z=+/-Y_n for all sufficiently large n. Thus one v_0, then one
epsilon>0, works on all four moving edges, independently of n and
zeta. Dependence on the fixed s is allowed.

The kernel poles are y=h*(m+1/2), of residue +1: the denominator
derivative there is -i*lambda*n. The real endpoints are +/-2q*h,
so exactly -2q<=m<=2q-1 occur. The vertical-edge phases are integer
multiples of 2*pi. The horizontal denominator bounds are
1-exp(-lambda*n*v_0) and exp(lambda*n*v_0)-1, respectively;
they prove (8). There is no boundary pole. The rational factor's
possible poles a=0 or a=t_j*s have Im y=-d or -d-t_j*s, outside
the rectangle. All logarithmic factors in f are bounded away from
zero on the compact (t,z,v) domain; in particular Us+t*(d+v)>0.
The t derivative is therefore bounded, giving the uniform O(1)
Riemann-sum error. The j=0 factor is separately bounded. The strict
bound |a|<R bounds the entire T_M regardless of its growing degree.
Thus (10) holds uniformly on the full spatial circle with both
finite endpoints retained.

**Summable transfer and actual Fourier data.** Formula (11) follows
from L666 (6), including x/a. Each beta_j<lambda_j since t_j^2<U.
Hence |W|<=1 on the real xi axis and

    |partial_xi W| <= lambda_0+sum_j(lambda_j+beta_j)
                    <=(2n-1)*h/d <2*A/d.

The L666 radius bound holds along every allowed shift segment.
Together with (12), this bounds the derivative of W*T_M independently
of n and zeta. For a fixed integer H, the finite head |m|<=H
converges uniformly in zeta by (13) and the geometric formula for
T_M. Both the finite-n difference tail and its limiting tail are
bounded by C*sum_(|m|>H)|e_m|. Send n to infinity for the head,
then H to infinity. This proves uniform (14) with expanding endpoints;
no unshifted infinite oscillatory series is summed in this passage.

The differences pair termwise with a compact smooth frequency test
because |exp(i*v*e_m)-1|<=|v*e_m| supplies a summable majorant.
Thus S_e is the continuous transform of the measure difference in
the positive-exponent convention. L703 (9) places both bump supports
strictly inside (1/8,3/8) and its reflection. Subtracting the
translated-comb identity from the actual L703 identity cancels the
constant 1 and the atom at zero on (-1/8,1/8), where chi_w=0.
It gives S_e(-2*pi*t)=0 there. Bound (15) puts -omega/(2*pi)
strictly in that interval. No head/path gap or n-dependent profile
is used. The uniform limit (3) has modulus at least 1/(R+d), which
justifies eventual nonvanishing and the logarithmic limit (16).

**Whole boundary and complete divisors.** The ordinates satisfy
|y|<Y even at the displaced endpoints. Triangle and reverse-triangle
inequalities give (17) for every boundary angle. Odd n makes tau*n
nonintegral and |j/n-tau|>=1/(160*n). For the monotone grid comparison,
the adjacent sampled terms and n times the adjacent-cell integrals
are O(log n); the remaining errors telescope. This verifies (19).
Concavity of F and the checked exponential bounds give (20). The
factor 100*M covers all M terms including the anchor. Spatial zeros
do not invalidate this upper bound.

For fixed n write N=floor(tau*n). L657's exact denominator has
C_x(u)=U^J*product_(j=1)^J(u+b_j). After cancelling these factors,

    F_n(u,zeta)=K(u,zeta)*r^N /
      [U^J*product_(1<=j<=N)(r^2+b_j*u)
           *product_(N<j<=J)(u+b_j)*product_(a!=x) A_a(u)].

The displayed denominator roots have moduli r^2/b_j>r, b_j>r
and |a|/t_j>d>r, respectively. The multiplier of K is holomorphic
and nonzero near the closed disk for each n; a neighborhood uniform
in n is unnecessary. Thus F_n has precisely the complete K zeros,
including cancelled poles and multiplicities, with no reduced
numerator substituted.

L657's center calculation Re c_0(0)>0 makes K(0,zeta) a nonzero
polynomial with finitely many exceptional circle points. Its logarithm
and that of K(r*v,zeta) are absolutely integrable by the imported
theorem; Q has no boundary zeros. Fubini and the finite root formula
give (23), finiteness of Z_n and m_0=log M+O(1). Boundary roots
have zero charge and integrable logarithms. Center exceptions are
omitted only from the slice identity, without discarding any positive
measure or unpaid logarithmic cost. This checks the L657/L666 uses
here, not their unrelated arc or quadrature conclusions.

**Poisson direction and asymptotic margin.** For a=s/r, the map
u=r*(v+a)/(1+a*v) sends 0 to s. Its inverse boundary angular
derivative is (1-a^2)/|exp(i*theta)-a|^2=P_s(theta). This verifies
the weight direction, mass one and minimum kappa in Section 5.
F_n is analytic near the closed disk and nonzero at s for every
spatial slice once n is large. Ash--Novinger Theorem 4.8.3 applies
with real s and allows boundary zeros. Its nonpositive zero terms
give log|F_n(s,zeta)|<=mean P_s*log|G_n|. Crucially, the upper
bound log|G_n|<=U_n then gives

    mean P_s*log|G_n|
      <=kappa*mean log|G_n|+(1-kappa)*U_n.

The weight is bounded, so spatial integration preserves absolute
integrability. Substitution of (23) gives (28), including its negative
(1-kappa)*(P_n+U_n) term. Kernel positivity alone would not suffice.

The pole-grid spacing is d/(Un); the factorial formula gives
P_n=tau*n+O(log n). For D_n/n, the sole singular integrand is
log(1+s/b), whose first-cell integral tends to zero; monotone
comparison handles the remaining cells. The second integrand is
smooth, and the last partial cell tends to zero. Thus (26) requires
no interchange involving moving numerator roots. The inequalities
(r+s)*log(1+s/r)>=s and log(1+v)<=v give (27). In the certificate's
exp(1) bound, the tail starting at 1/4! has successive ratios at
most 1/5, so its sum is at most 5/96; this verifies that premise.

All 16 rational checks and their actual/required values were read in
full. Executing the unchanged step-148 code with redirected output
produced the byte-identical certificate
`scripts/one-sided-hankel/inner-disk-charge-replay-150.json`, SHA256
`34a58487addedf2e9a8f75d40acb242c4fbc9c737e1ebf6b5c8673309aef4194`.
The original was preserved. An initial harness used a relative
__file__ and failed only while printing its output path after checks
and writing; using an absolute path completed the replay. The replay
retains the original certificate's historical unaudited scope text.
It certifies arithmetic only; the analytic audit is the prose above.
To reproduce without overwriting the original certificate:

    python3 - <<'PY'
    from pathlib import Path
    import runpy
    p = Path('scripts/one-sided-hankel/inner-disk-charge-148.py').resolve()
    ns = runpy.run_path(str(p))
    ns['main'].__globals__['__file__'] = str(p.with_name('inner-disk-charge-replay-150.py'))
    ns['main']()
    assert p.with_suffix('.json').read_bytes() == p.with_name('inner-disk-charge-replay-150.json').read_bytes()
    PY

The coefficient gamma=2267057/7998400000 exceeds 1/4000 by
267457/7998400000. With m_s=O(1) and m_0=O(log n), (28) implies
liminf Z_n/n>=gamma, so the strict margin proves the eventual bound.
No effective onset, o(n) deficit, annular payment, complete-mean sign,
H/support or Xi realization follows. This first audit validates the
partial local input, without claiming novelty beyond the source-based
specialization or reopening the scalar/absolute-cost stops.

## Mathlib

Full matching coverage of this inner-disk lower charge and finite
profile transfer has not been checked. Reuse the supporting module
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html)
recorded in L657, including
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure` and
`Polynomial.mahlerMeasure_mul`. These are supporting one-variable
results, not a formalization of (1)-(3). Coverage of the additional
contour, distribution and Poisson specialization is unknown; no
absence claim or formal verification is made.
