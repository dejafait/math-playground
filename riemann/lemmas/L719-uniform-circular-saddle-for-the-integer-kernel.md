# Lemma 719: a uniform circular saddle for the exact integer-size kernel

## Hypotheses

Use the original fixed L703 bump through L714 and the audited L714
finite inverse, L715 function F and L716 moment formulas. In particular

    U=121/64, A=27/10, d=5/4, u=(3+4i)/10, alpha=11/8,
    n=12q+3, q>=1,
    omega=A*[log(9/5)-4/5+(121/100)*log(201/121)],
    I=[omega-delta,omega+delta], 0<delta<1/3000,
    z_v=exp(-u*v/A), s_v=-z_v*F'(z_v),
    D_n=d*product_(k=1)^(n-1) (d+u*k/n)/(U*u+d*k/n),
    R_n(s)=product_(k=1)^(n-1)(U+s*k/n)
                         /product_(j=0)^(n-1)(s+j/n).

R_n here is a rational function of s, not L714's signed outer remainder
R_n(c). This lemma uses no claim about that outer remainder, L714 (6),
L713's envelope, L717 or L718. No extension or endpoint law for chi is
assumed. Define, locally for Re(s)>0,

    f(s,t)=Log(U+s*t)-Log(s+t),
    g(t)=Log(d+u*t)-Log(U*u+d*t),
    ell_D=integral_0^1 g(t)dt,
    Phi(s;v)=u*v*s/A+integral_0^1 f(s,t)dt,
    S(v)=ell_D+1+log(U)-d*v/A+F(z_v).

The logarithms in these definitions are the right-half-plane branches.

## Conclusion

There is a bounded complex neighborhood W of the entire closed interval
I, with the same statements uniform on its closure, such that:

1. s_v is holomorphic, Phi_s(s_v;v)=0, and

       9/5<Re(s_v)<37/20, -37/20<Im(s_v)<-9/5,
       5/2<r_v=|s_v|<21/8,
       Re(u*v/A)>1/10, Im(u*v/A)>3/20.

   The positively oriented circle C_v: s=s_v*exp(i*tau),
   -pi<=tau<=pi, encloses all poles -j/n and excludes alpha/u.
   Its distances from them are respectively >3/2 and >1/8.
   The exact identity, for complex v in W, is

       p_n(v)=(n*D_n/A)/(2*pi*i)
          *integral_(C_v) exp(n*(u*s-d)*v/A)
                            R_n(s)/(alpha-u*s) ds.       (1)

2. The saddle is nondegenerate, with a fixed angular Hessian bound

       H(v)=s_v^2*Phi_ss(s_v;v), Re(H(v))>1/3.           (2)

   The real logarithmic phase on the whole circle, using integrals of
   log moduli away from the local branch, has a unique maximum at s_v.
   Outside |tau|<1/10 its gap from that maximum is at least 1/2400.
   For all sufficiently large permitted n, the exact finite integrand
   has the uniform bound there

       |exp(n*u*v*s/A)*R_n(s)/(alpha-u*s)|
          <= C*exp(n*Re(Phi(s_v;v))-n/5000).             (3)

   This is a bound for the entire complementary compact arc. There is
   no omitted unbounded contour tail and no crossed residue.

3. On a fixed complex neighborhood of |tau|<1/10, both product factors
   have legal local logarithms. With s=s_v*exp(i*tau),

       log[D_n*R_n(s)]-n*[ell_D+integral_0^1 f(s,t)dt]
        =c_0(s)+sum_(j=1)^(m-1) c_(2j-1)(s)/n^(2j-1)+E_(n,m)(s),
       |c_(2j-1)(s)|<=C^(2j)*(2j-1)!,
       |E_(n,m)(s)|<=C^(2m)*(2m-1)!/n^(2m-1),          (4)

   for every integer m>=1 and n>=15, on a possibly smaller common
   complex neighborhood. The logarithm is the specified sum of factor
   logarithms, not an unspecified principal logarithm of the product.
   In particular

       c_0(s)=log(d)-Log(s)
                 -[g(0)+g(1)+f(s,0)+f(s,1)]/2.        (5)

4. The nominated phase is exactly the saddle phase:

       ell_D+Phi(s_v;v)-d*v/A=S(v).                    (6)

   Uniformly on a smaller fixed complex neighborhood of I,

       n^(-1/2)*exp(-n*S(v))*p_n(v)=a_0(v)+O(1/n),
       a_0(v)=s_v*exp(c_0(s_v))
                   /[A*sqrt(2*pi)*(alpha-u*s_v)*sqrt(H(v))]. (7)

   The square root of H has positive real part. The holomorphic a_0
   is bounded away from zero on compactly contained neighborhoods of I.

This partial result passed the separate conceptual audit in Section 7
(step 192). It supplies the contour, local logarithmic product
remainders, the exact phase, beta=1/2 and elliptic leading amplitude.
It does NOT establish the target's every-order factorial remainder for
the exponentiated product after stationary integration. That closure
and combination, including truncation through epsilon*n, are supplied
separately by L720. Neither (4) nor a relative O(1/n) error substitutes
for that closure.
No signed rate for integral chi*p_n, support-edge transfer, full response,
spatial Jensen payment, H/support, Xi realization or RH claim follows.
The comparison did not locate this exact-array contour result; it does
not certify originality. The audit accepts only the stated local input.

## Proof

### 1. Reused source scope and exact finite contour

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-signed-bump-analytic-symbol.md`.
Its comparison and recorded failures are reused. The finite residue
theorem is [NIST DLMF 1.10(iv), (1.10.8)](https://dlmf.nist.gov/1.10.iv),
already applied under the audited L714 finite hypotheses. For the local
Gaussian step use M. Hitrik and J. Sjostrand, *Two Minicourses on Analytic
Microlocal Analysis*, [arXiv:1508.00649v1](https://arxiv.org/pdf/1508.00649v1),
Section 2.3, Theorems 2.3.1 and 2.3.3, Lemma 2.3.2 and their deformation /
Morse reduction, pp.37--40. These are fixed analytic phase/amplitude
theorems; their use in Section 6 is only at fixed expansion order.
For (4) use the exact Euler--Maclaurin formula
[DLMF 2.10(i), (2.10.1)](https://dlmf.nist.gov/2.10#E1), with analytic
derivatives and hence its integrability hypotheses. The source review
checked these inputs before this attempt. General inversion, stationary
phase and Euler--Maclaurin are imported, not reproved. The estimates below
are the needed application to the growing integer array.

From L714's rational product, setting z=u*s-d gives

    W_n(u,i*z)=D_n*R_n(s)/u.

More directly, Res_(s=-j/n) R_n(s)=b_(n,j): its other denominator
factors have product (-1)^j*j!*(n-1-j)!/n^(n-1), and its numerator
is product_(k=1)^(n-1)(U-j*k/n^2). Thus the residues of the integrand
in (1) are exactly

    b_(n,j)*exp(-(d+u*j/n)*n*v/A)/(alpha+u*j/n).

Multiplication by n*D_n/A gives precisely L714 (2). This proves (1)
on any positively oriented loop enclosing -j/n and excluding alpha/u,
for all complex v. There is no appeal to decay of an infinite contour.
The numerator's negative-real zeros are harmless on a residue contour;
we will not impose a global logarithm through them.

### 2. A certified holomorphic saddle on a fixed neighborhood

Write y(z)=-z*F'(z). Audited L715--L716 give

    y(z)=integral_0^1 a*z/(1-a*z) kappa(da)
        =sum_(k>=1) m_k*z^k, 0<=m_k<=1,
    m_1=exp(-1/(2U))>0.

On the disk D={z: |z|^2<Re(z)}, Re(y(z))>0: the real part of each
integrand is (a*Re(z)-a^2*|z|^2)/|1-a*z|^2, positive for a>0.
The first moment makes the integral strictly positive. Also Im(y(z))
has the sign of Im(z), by the analogous numerator a*Im(z).

Define the holomorphic function on Re(s)>0

    K(s)=Log(s+1)-Log(s)-J(-s),
    J(-s)=integral_0^1 t/(U+s*t)dt.

L716's audited germ identity y=z*(1+y)*exp(-J(-y)) implies
exp(-K(y(z)))=z near zero inside D. Both sides are holomorphic on
the connected disk D. Thus the identity holds throughout D.
K(y(z))+Log(z) is then a continuous multiple of 2*pi*i; on positive
z near zero it is zero, so it vanishes on D. Consequently

    K(y(z))=-Log(z), z in D.                            (8)

The certificate described below gives, for every real v in the entire
maximal interval [omega-1/3000,omega+1/3000],

    2/5<x=v/A<41/100, |z_v|<9/10<cos(2*x/5),
    9/5<Re(y(z_v))<37/20,
    -37/20<Im(y(z_v))<-9/5.                            (9)

The cosine comparison puts z_v in D. Its argument lies between -1 and
zero, so -Log(z_v)=u*v/A without a period. Differentiation under the
integral defining Phi gives Phi_s=u*v/A-K(s); (8) proves the saddle
equation. All integrands have positive real denominator on this domain.

Here are the complete analytical error controls for (9). Use L716 (6)--(7)
to recompute m_k, 1<=k<=80, by exact rational coefficients multiplied
by exp(-k/(2U)). At the rational center x_0=4019/10000, evaluate
sum_(k=1)^80 m_k*exp(-u*k*x_0) in outward intervals. The omitted tail
in either component has absolute bound 10*(9/10)^81. On the whole
interval between x_0 and either possible bump endpoint,

    |d/dx y(exp(-u*x))|
       <=(1/2)*sum_(k>=1) k*(9/10)^k=45.

Thus add the tail and 45*max(|x_0-x_-|,|x_+-x_0|) to both component
errors. The endpoints x_-,x_+ are enclosed using

    2*sum_(j=0)^11 r^(2j+1)/(2j+1)
       <=log(q)<=that sum+2*r^25/[25*(1-r^2)],
    r=(q-1)/(q+1), q=9/5 or 201/121.

All exponentials have arguments in [0,1]; their degree-41 and degree-40
alternating polynomials enclose exp(-a). For sine and cosine, truncation
at term index 20 is an upper bound; subtracting the next term's absolute
value gives a lower bound. Complex powers are formed with outward
fixed-point multiplication at scale 2^120. These are decreasing
alternating series on the used interval. The cosine comparison also
uses cos(t)>=1-t^2/2 for 0<=t<=41/250. None of the decisions uses a
floating-point number.

The script and full certificate are

    python3 scripts/one-sided-hankel/analytic-symbol-saddle-certificate-190.py
    scripts/one-sided-hankel/analytic-symbol-saddle-certificate-190.json

They retain every exact moment coefficient, interval term, endpoint,
error and comparison. All fifteen exact comparisons pass. Decimal
previews of the enclosed real and imaginary ranges are respectively
[1.811418402487,1.828348141269] and
[-1.831324508865,-1.814394770083]; the certificate's rational comparisons
with (9), not these previews, establish (9). The full `/checks` object
was inspected with the scoped JSON inspector. The separate floating
Newton/circle diagnostic is not an input to this proof.

Since 2*(9/5)^2>(5/2)^2 and 2*(37/20)^2<(21/8)^2, (9) gives the
radius bounds in the conclusion. Holomorphy and strict margins on the
compact interval allow a small bounded open tube W about I whose closure
retains (9)'s s bounds, z_v in D, the principal-log identity, and
Re(u*v/A)>1/10, Im(u*v/A)>3/20. This is an existence argument for
one fixed complex tube, independent of n, not a numerical claim of its
width. Its closure can be chosen within a slightly larger such tube.
For C_v, distances to -j/n are at least r_v-j/n>3/2; the distance to
alpha/u is at least 11/4-r_v>1/8. This completes the contour admissibility
and complex-parameter claims in part 1.

### 3. Concavity controls the full circle, including numerator zeros

Fix any v in the closure of W, and write r=|s_v|,
a=Re(u*v/A), b=Im(u*v/A)>3/20. For -1<c<1 set

    L(c)=1/2*integral_0^1 log[(U^2+r^2*t^2+2*U*r*t*c)
                                     /(r^2+t^2+2*r*t*c)]dt,
    V(c)=r*(a*c+b*sqrt(1-c^2))+L(c).

V is the real phase on the lower semicircle. The upper semicircle's
phase is V(c)-2*b*r*sqrt(1-c^2). Both limits at c=-1 are finite
for the integral: a possible logarithmic singularity at t=U/r is
integrable. All assertions below extend by one-sided limits there.

Put P=U*r*t/(U^2+r^2*t^2+2*U*r*t*c) and
Q=r*t/(r^2+t^2+2*r*t*c). For t>0 and -1<c<1, P>Q>=0 because

    U*(r^2+t^2)-(U^2+r^2*t^2)=(r^2-U)*(U-t^2)>0.

Here r^2>25/4>U and U>1>=t^2. Thus
L''(c)=-2*integral(P^2-Q^2)dt<=0. It follows that

    V''(c)<=-b*r/(1-c^2)^(3/2)<-1/3.                  (10)

Let theta_* be the argument of s_v in (-pi/2,0), and c_*=cos(theta_*).
The complex saddle equation implies that the angular derivative of
the real phase is zero there. Since sin(theta_*) is nonzero, V'(c_*)=0.
Integrating (10) on either side yields

    V(c)<=V(c_*)-(c-c_*)^2/6.                         (11)

This proves the unique maximum on the lower half; the upper-half
comparison proves uniqueness on the full circle. Moreover

    24/35<c_*<37/50,
    |sin(theta_*)|>24/35.

If a point on the lower semicircle has angular distance at least 1/10
from theta_*, monotonicity of cosine on that semicircle and its derivative
give |c-c_*|>(24/35-1/10)/10>1/20. Equations (10)--(11) give a gap
>1/2400. On the upper semicircle, either |c-c_*|>=1/20, giving the
same gap, or |c|<37/50+1/20=79/100. In the latter case
sqrt(1-c^2)>3/5 and the extra loss 2*b*r*sqrt(1-c^2)>9/20.
Thus the stated gap holds on the whole complementary arc.

The angular second derivative at the saddle is
V''(c_*)*sin(theta_*)^2<=-b*r/|sin(theta_*)|<-1/3.
On the other hand the complex second derivative of
Phi(s_v*exp(i*tau);v) at zero is -s_v^2*Phi_ss(s_v;v), because
Phi_s(s_v;v)=0. This proves Re(H)>1/3 and nondegeneracy. In particular
|Phi_ss|>(1/3)/(21/8)^2. No numerical Hessian is used.

### 4. A finite-product bound on every complementary arc

The finite logarithmic modulus on the lower semicircle is

    V_n(c)=n*r*(a*c+b*sqrt(1-c^2))-log(r)
      +1/2*sum_(k=1)^(n-1) log[(U^2+r^2*t_k^2+2*U*r*t_k*c)
                                          /(r^2+t_k^2+2*r*t_k*c)],
    t_k=k/n.

The same pointwise comparison P>Q proves V_n''(c)<-n/3. Its value
and first derivative at c_* satisfy

    V_n(c_*)=n*V(c_*)+O(1), V_n'(c_*)=O(1),            (12)

uniformly on W. Indeed the summands and their t derivatives, also after
one c derivative, are bounded on the compact set c_*>24/35,
5/2<r<21/8. The elementary first-derivative Riemann-sum error is O(1)
for the unnormalized sums. The continuous derivative is V'(c_*)=0.
No approximation near c=-1 is used in (12).

Concavity now gives, everywhere on the lower half,

    V_n(c)<=n*V(c_*)+O(1)+O(1)*|c-c_*|-n*(c-c_*)^2/6.

For |c-c_*|>=1/20 this is at most n*V(c_*)-n/5000 for all sufficiently
large n, uniformly in v. At c=-1 a finite numerator can vanish; its
log modulus is then -infinity and the upper bound still holds. If it
does not vanish, use continuity. On the upper semicircle the exact
additional loss is 2*n*b*r*sqrt(1-c^2); the second case in Section 3
handles |c-c_*|<1/20. This proves the same bound on all arcs outside
|tau|<1/10, with one uniform onset. Finally

    |alpha-u*s|>=|u|*(11/4-r)>1/16

on every circle. Its length is bounded by 2*pi*21/8. These facts prove
(3) and also the corresponding integrated bound. They pay the entire
compact complement; taking a modulus here has not replaced the local
signed saddle integral by its variation.

### 5. Local product logarithms and factorial bounds

For complex |tau|<101/1000, the exponential series gives
|exp(i*tau)-1|<=|tau|/(1-|tau|)<101/899.
Thus s=s_v*exp(i*tau) satisfies

    Re(s)>9/5-(21/8)*(101/899)>3/2, |s|<3.

If the complex t has distance <1/4 from [0,1], then
Re(s+t)>5/4 and Re(U+s*t)>U-3/4>1. Both logarithms of f
are consequently holomorphic on this common domain and uniformly
bounded on slightly smaller closed domains. For g, the same t domain
gives Re(d+u*t)>=d-|u|/4>0 and
Re(U*u+d*t)>=3*U/10-d/4>0. Its two logs are likewise uniformly bounded.
There is therefore a fixed rho>0 and M such that, for all derivative
orders l and s in the common local domain,

    |partial_t^l(f(s,t)+g(t))|<=M*l!*rho^(-l), t in [0,1]. (13)

This is Cauchy's estimate on the fixed t neighborhood; one may take any
rho<1/4 after compactly shrinking the s domain. No derivative count is
restricted to a fixed order.

Apply the cited Euler--Maclaurin formula to h_s(t)=f(s,t)+g(t).
The exact factor logarithm on the left of (4) is

    log(d)-Log(s)+sum_(k=1)^(n-1) h_s(k/n)-n*integral_0^1 h_s(t)dt.

Its endpoint correction is (5), and

    c_(2j-1)(s)=B_(2j)/(2j)!
                 *[h_s^(2j-1)(1)-h_s^(2j-1)(0)].       (14)

To see uniform factorial constants without an asymptotic assertion
about Bernoulli numbers, use their generating function
z*exp(t*z)/(exp(z)-1), with the removable value at z=0. It is uniformly
bounded for real 0<=t<=1 and |z|=1, so Cauchy's coefficient estimate
gives |B_l(t)|/l!<=M_B for every l. Apply Euler--Maclaurin through its
m-th correction: its periodic-Bernoulli remainder has modulus at most

    M_B*n^(1-2m)*integral_0^1 |h_s^(2m)(t)|dt.

Move the m-th endpoint correction into the remainder if retaining only
j<m. Bound it by (13)--(14). Both terms are bounded by
C^(2m)*(2m-1)!*n^(1-2m), on increasing C once to absorb
2m<=2^(2m). This proves (4) for every m>=1, not just for a fixed m.
It proves factorial control of the logarithm only. Exponentiation and
integration with uniform factorial constants are not asserted here.

### 6. Exact phase identification and the elliptic first term

For z in D put s=y(z) and

    T(z)=-s*Log(z)+integral_0^1 f(s,t)dt.

Using (8), differentiation cancels the s' terms and gives
T'(z)=-s/z=F'(z). As positive z tends to zero, s=m_1*z+O(z^2),
s*Log(z) tends to zero and the integral tends to log(U)+1. The last
limit follows directly from
integral_0^1 Log(s+t)dt=(s+1)Log(s+1)-s*Log(s)-1
on positive s; the numerator integral tends to log(U). Since F(0)=0,
T=F+1+log(U) on D. Substitute z=z_v, -Log(z_v)=u*v/A to obtain (6).
This identifies the complex phase, not just its real part modulo a
constant or its logarithmic magnitude.

Taking m=1 in (4) shows that on the common complex local domain

    D_n*R_n(s)=exp(n*[ell_D+integral f])*exp(c_0(s))*(1+O(1/n)), (15)

uniformly and holomorphically in s and v. In the contour parameter,
ds=i*s_v*exp(i*tau)dtau. The local phase difference
Phi(s_v;v)-Phi(s_v*exp(i*tau);v) is analytic, vanishes to second
order, and has Hessian H with Re(H)>1/3. The bounds of Section 3 also
give, for real |tau|<=1/10,

    Re[Phi(s_v;v)-Phi(s_v*exp(i*tau);v)]>=tau^2/20:

indeed the lower semicircle stays there, |cos(theta_*+tau)-c_*|
>=(24/35-1/10)*|tau|, and (11) applies. Uniform local analyticity,
the nonzero Hessian and compact parameter closure allow a smaller fixed
complex neighborhood with a unique critical point. For example bound
the third derivative on a common disc and shrink until the derivative
is H*tau+O(tau^2) with the error <|H*tau|/2. On the remaining real
annulus up to 1/10 the displayed quadratic decay gives a strict gap.
Section 4 controls the rest of the circle.

These are the common-domain, unique-saddle and boundary-separation
hypotheses of the cited analytic Morse / stationary-phase theorem.
Applying its Gaussian expansion at fixed order to the fixed analytic
amplitude s*exp(c_0(s))/(alpha-u*s), with positive circle orientation,
gives the leading factor

    exp(n*[ell_D+Phi(s_v;v)-d*v/A]) / sqrt(2*pi*n)
       *s_v*exp(c_0(s_v))/[(alpha-u*s_v)*sqrt(H(v))]

before multiplication by n/A. The constants can be chosen uniformly:
the analytic domains are common, the Hessian has a common lower bound,
derivatives have common upper bounds, and the local and complementary
gaps just established are fixed. The analytic Gaussian estimate of
Theorem 2.3.1 at the next fixed order yields an O(n^-1) relative
correction to this fixed-amplitude leading term. The additional O(n^-1)
amplitude error in (15) contributes O(n^-3/2) times the saddle exponential
before multiplication by n/A: integrate its uniform bound against
exp(-n*tau^2/20). The complement is exponentially smaller by Section 4
and boundedness of D_n*exp(-n*ell_D), also given by Euler--Maclaurin.
This proves (7).

Every factor in a_0 is holomorphic and nonzero: s_v is in the specified
right half-plane, exp(c_0) never vanishes, the resolvent is separated,
and H is in Re(H)>1/3. The square root with positive real part agrees
with the Gaussian orientation. Compactness on a smaller neighborhood
then supplies a positive lower bound for |a_0|. This justifies ellipticity
and beta=1/2, but does not combine the all-order logarithmic remainder
with exponentiation and stationary integration. That is the remaining
analytic-symbol step supplied separately by L720, as distinct from the unpaid outer signed
integral and all full-family/Xi gaps.

### 7. Separate conceptual audit — 3 November 2026, step 192

**Verdict: accepted within the stated local scope.** The unchanged
invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-signed-bump-analytic-symbol.md` covers this
audit and L720's closure. All conclusions (1)--(7) survive. No new
asymptotic claim, width for W, effective onset, source theorem or signed
bump rate is asserted. This is independent validation of the specialization,
classified REPRODUCTION, not a claim of progress beyond the checked sources.

**Exact saddle evidence.** The complete certificate code was checked
against L716 (4)--(7). Its coefficient recurrence computes exactly the
coefficient of the finite exponential needed at each k<=80; the separate
exponential interval is raised to the kth power using outward arithmetic.
No assertion that a Taylor polynomial in a large argument encloses
exp(-k/(2U)) is used: the argument 1/(2U) is in [0,1]. The complex power
calculation similarly starts from exp(-3*x_0/10), cos(2*x_0/5) and
-sin(2*x_0/5), all in the proved alternating-series range. Floor and
ceiling on all four products of interval endpoints give outward products
even when the rational coefficient or complex component is negative.

The preserved script was copied without alteration and replayed by

    python3 scripts/one-sided-hankel/analytic-symbol-saddle-replay-192.py
    scripts/one-sided-hankel/analytic-symbol-saddle-replay-192.json

All 80 moment rows, all 80 complex-sum rows and all remaining certificate
data exactly match step 190. All fifteen rational comparisons were
reevaluated, and the complete `/checks` and `/bounds` values were inspected,
not just their decimal previews. The finite center sum is enclosed near
1.819883271878-1.822859639474*i; the rational error is less than 0.008465.
Its two components include the entire geometric tail
10*(9/10)^81 and the Lipschitz contribution 45*distance. The derivative
bound follows from 0<=m_k<=1, |u|=1/2 and |z|<9/10 along the whole
segment connecting x_0 with either enclosed endpoint. Thus both endpoints
and all smaller original bump widths are included. The component boxes
strictly imply 5/2<|s_v|<21/8. The certificate's conservative radial
comparison 1/8>1/9 is not substituted for the required strict >1/8:
that strict inequality follows from 11/4-|s_v|>11/4-21/8=1/8.

**Branch, contour and global maximum.** The L715 probability measure
and positive first moment make Re(y)>0 on the connected disk D. This
justifies composing K with y throughout D; the germ identity extends
there before choosing the logarithmic period. On positive z near zero
that period is zero. The computed z_v lies in D and has principal
argument -2v/(5A), so the resulting saddle equation has its stated
complex phase, not only its real part. Strict real-interval margins
and holomorphy give one tube whose compact closure preserves every bound.

The finite residues are b_(n,j); ds=i*s*d tau on the positive circle.
The extra resolvent pole alpha/u remains outside, and no other residues
are dropped. For every complex v in that tube the real circle phase
still has real parameters r=|s_v|, a=Re(uv/A), b=Im(uv/A)>3/20.
The identity (r^2-U)(U-t^2)>0 proves P>Q on -1<c<1, hence strict
concavity. The critical point is on the lower semicircle with
|sin(theta_*)|>24/35. The lower-half gap is at least
(1/20)^2/6=1/2400; the upper-half loss supplies the other case.
The finite-product tangent error is uniformly O(1) at c_*>24/35.
Consequently the gap 1/2400 strictly exceeds 1/5000 even after that
error is divided by n. No uniform Riemann-sum approximation at c=-1
is required. A zero numerator there gives modulus zero and satisfies
the upper bound by a limit. Circle length and the resolvent reciprocal
are uniformly bounded, so the integrated complement is also paid.

**Local domain and all-order logarithm.** On |tau|<101/1000,
|s-s_v|<(21/8)*(101/899). The pole is
alpha/u=33/20-11i/5, whereas Im(s_v)>-37/20. Therefore

    |s-alpha/u|>7/20-(21/8)*(101/899)
                 =1981/35960>1/20,
    |alpha-u*s|>1/40.

This makes explicit the local complex resolvent separation needed by
L720; radial separation on the real circle alone would not suffice.
The same domain has Re(s)>3/2 and |s|<3. Writing complex t=t_0+e,
t_0 in [0,1], |e|<1/4, proves the claimed right-half-plane log domains.
The exact product logarithm contains -Log(s), not an extra -log(n).
Its Euler--Maclaurin endpoint term is exactly (5). Cauchy bounds on
one fixed t tube and the generating function for Bernoulli polynomials
give a constant independent of derivative order. The order-2m integral
remainder and the moved endpoint correction both have the required
n^(1-2m) bound after absorbing 2m into C^(2m). No fixed-order estimate
has been promoted to an all-order one.

Finally T'=F', its positive-zero limit log(U)+1 and F(0)=0 determine
the full complex constant in (6). The local real decay follows from
(24/35-1/10)^2/6>1/20. Positive circle orientation and the branch
Re(sqrt(H))>0 give exactly (7); every factor of a_0 is nonzero on
the fixed tube. This audit validates the contour/logarithm input used
by L720, without integrating it against chi. The finite comparison
replay and the additional local-domain margin are also recorded in
`scripts/one-sided-hankel/analytic-symbol-audit-192.json`.

## Mathlib

Full matching coverage for this exact growing-product contour and its
uniform asymptotics has not been checked. No absence claim is made.
The cited classical residue, Cauchy, Euler--Maclaurin and analytic
stationary-phase results are mathematical inputs; no Lean verification
or formal library coverage is claimed for their specialization here.
