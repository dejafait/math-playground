# Corollary 673d: the symmetric angular pair fails the real crossing test

## Hypotheses

Use L666's complete rational angular family and L673's admissible phase
nodes. Explicitly, for an integer q>=1 set

    n=12q+3, h=27/(10n), rho=h/10, c=10*pi/27,
    d=5/4, x=-d, U=121/64, t_j=j/n (0<=j<n),
    W_(x+z)(u)=product_j [(x-t_j*u)/(x+z-t_j*u)]
                           *[(U*u-t_j*(x+z))/(U*u-t_j*x)],
    s_k=k+1/2+atan(1/(10*s_k))/pi, 0<=k<2q,
    y_k=h*s_k, Z={x} union {x+-i*y_k}.

The j=0 factor is x/(x+z). The original residues are all one.
Only the auxiliary, angle-independent nonnegative coefficients below
are changed; they have no mass cap. Put

    v=(-99+20i)/101, p0=109/404,
    S={z: |Re z|<p0}, D={z: |x+z|>1},
    A_n(z)=[W_(x+z)(v)*W_(x-z)(v)
             *W_(x+z)(conj(v))*W_(x-z)(conj(v))]^(1/4),
    A_n(0)=1, g_n(z)=(1-z/rho)*exp(-c*n*z)/A_n(z).

The fourth root will be defined explicitly in the proof. For the contour
claim let Gamma be a positively oriented rectifiable Jordan curve with
bounded interior Omega, with 0 and all +-i*y_k in Omega and
closure(Omega) contained in S intersect D. This is a specified common
analytic domain, not a claim about every finite-n permissible contour.

For r=9/20 define the real logarithmic integrals

    F(z,u)=integral_0^1 log|[(x-t*u)/(x+z-t*u)]
                           *[(U*u-t*(x+z))/(U*u-t*x)]| dt,
    K(z)=(10/27) integral_(-r)^r [log|t|-log|z-i*t|] dt,
    H_v(z)=[F(z,v)+F(-z,v)+F(z,conj(v))+F(-z,conj(v))]/4,
    E_pair(z,u)=F(z,u)-H_v(z)-c*Re z+K(z).

The auxiliary H_v is only this gauge contribution; it is not L666's H.

## Conclusion

A_n is a holomorphic, nonvanishing, even function on S, and A_n(i*y)>0
for all real y. With

    P(z)=product_(0<=k<2q)(z^2+y_k^2),
    ell_k=(1/2) product_(l!=k) y_l^2/(y_l^2-y_k^2),
    b_(x+i*y_k)=b_(x-i*y_k)
      =|ell_k|*sqrt(1+100*s_k^2)
         /sqrt(|W_(x+i*y_k)(v)*W_(x-i*y_k)(v)|)>0,

the exact signed remainder, simultaneously for every |u|=1, is

    1+sum_(a!=x)b_a W_a(u)
      =(1/(2*pi*i)) integral_Gamma
           g_n(z)W_(x+z)(u)*P(0)/[z*P(z)] dz.          (1)

However, already at the real crossing and u=-1,

    E_pair(s,-1)>-3/400  for 0<=s<1/4,                (2)
    sup_(z in Gamma, |u|=1) E_pair(z,u)>-3/400>-1/100. (3)

Thus the proposed angular-pair factor cannot satisfy the sufficient
uniform absolute-contour exponent bound <=-1/100 in this class. Its
strict gap is greater than 1/400. No test at height 3/20 is needed once
this necessary crossing fails.

This does not lower-bound kappa_e, the finite-n integrand, or the signed
integral (1). It does not establish that these coefficients fail to
approximate at rate 1/100. Signed cancellation, angular integration,
other approximants or domains, the unit-residue H application, support,
Xi realization and mixed signs remain unresolved. This result has not
had a separate critical audit. It is a family-specific test under the
prior EXPLORE assessment `drafts/literature/2026-11-02-displaced-positive-cone-distance.md`;
the search did not establish coverage or certify originality. C673a--c
are comparisons, not mathematical inputs.

Section 5 records the exact normalized angular mean of this residual,
specializing C645o's existing residue formula. The finite numerical
diagnostic there supplies no asymptotic mean or norm bound.

## Proof

### 1. Common fourth-root branch, signs and residue applicability

For w=v or conj(v), write

    alpha_j(w)=1/(d+t_j*w), beta_j(w)=-t_j/(U*w+d*t_j),
    W_(x+z)(w)=product_j (1+beta_j(w)*z)/(1-alpha_j(w)*z).

All displayed constants are defined. At j=0, alpha_0=1/d and beta_0=0.
The roots of 1-alpha_j*z are d+t_j*w, whose real parts are at least
p0=d-99/101>1/4. For j>0 the roots of 1+beta_j*z are d+U*w/t_j;
their real parts are at most

    d-99*U/101=-3899/6464<-3/5<-p0.

The roots of the reflected factors are the negatives of these roots.
Each linear factor avoids the nonpositive real axis throughout S.
Indeed, a factor with value -lambda, lambda>=0, has its argument z
equal to (1+lambda) times its root, outside this strip. The factor
with beta_0=0 is identically one. Hence the principal logarithms define

    A_n(z)=exp((1/4) sum_(w=v,conj(v)) sum_j
       [Log(1+beta_j(w)*z)+Log(1-beta_j(w)*z)
        -Log(1-alpha_j(w)*z)-Log(1+alpha_j(w)*z)]).

It is holomorphic and nonzero on S, even, normalized at zero, and has
the stated fourth power. Because alpha_j and beta_j at the two angles
are conjugate, the logarithms at z=i*y pair with their conjugates.
Their sum is real, so A_n(i*y)>0. Also

    A_n(i*y)=sqrt(|W_(x+i*y)(v)*W_(x-i*y)(v)|).

L673 proves sign(ell_k)=(-1)^k and the exact phase identity

    (1-i*y_k/rho)*exp(-i*c*n*y_k)
      =(-1)^(k+1)*sqrt(1+100*s_k^2).

Division by the even positive nodal value A_n(i*y_k) preserves the
sign. Thus ell_k*g_n(+-i*y_k)=-b_(x+-i*y_k)<0 as claimed.
The coefficients are real and independent of the observation angle u.

On a neighborhood of closure(Omega), g_n is holomorphic. A pole of
W_(x+z)(u) in z requires x+z=t_j*u and hence |x+z|<1, excluded by D.
The angle-only denominator is nonzero since U>t_j*d. Cauchy's residue
theorem therefore applies to the integrand in (1): the residue at zero
is one and the residue at +-i*y_k is
-ell_k*g_n(+-i*y_k)*W_(x+-i*y_k)(u). This gives (1).
This is the standard named residue theorem with its hypotheses checked,
specializing L673's remainder rather than reproving a general cone theorem.

Exactly,

    log|g_n(z)|=log|1-z/rho|-c*n*Re z
       -(1/4) sum_(w=v,conj(v)) [log|W_(x+z)(w)|+log|W_(x-z)(w)|].

This motivates E_pair, but no finite-product-to-integral substitution
is used in a norm inequality. The continuum sufficient criterion itself
will fail. Any conclusion about (1) needs further finite-n and signed
estimates.

### 2. Compact real-interval derivative bounds and the endpoint tail

On the real axis conjugate angles have equal log moduli. Write

    f(s)=E_pair(s,-1)
        =F(s,-1)-[F(s,v)+F(-s,v)]/2-c*s+K(s),
    B(s)=[F(s,v)+F(-s,v)]/2.

For 0<=s<=1/4 and a=-d+-s, 1<=|a|<=3/2. Since |v|=1,

    |a-t*v|=|a/v-t|>=|Im(a/v)|>=20/101=:delta,
    |U*v-t*a|>=U-|a|>=25/64=:g,    0<=t<=1.

Differentiation under the integral is justified by these positive
uniform bounds. Each variable logarithm has first derivative bounded
by 1/|a-t*v| or t/|U*v-t*a| and second derivative bounded by the
square of the corresponding bound. Reflection changes no absolute bound.
Thus on the full interval

    |B'(s)|<=1/delta+1/(2*g)=633/100,
    |B''(s)|<=1/delta^2+1/(3*g^2)=830611/30000.

For the real angle -1 and 0<=s<1/4,

    F(s,-1)=integral_0^1 [log(1+beta(t)*s)-log(1-alpha(t)*s)] dt,
    alpha(t)=1/(d-t)>0, beta(t)=t/(U-d*t)>=0.

In particular F(s,-1) is increasing. On 0<=s<=6/25 its second
derivative has absolute bound

    |F_ss(s,-1)|
      <=integral_0^1 [(d-s-t)^(-2)+t^2/(U-d*t+t*s)^2] dt
      <=1/(d-6/25-1)+1/[3*(U-d)^2].

The omitted term -1/(d-s) in the first integral only improves this
upper bound. Direct integration of the real K gives, for s>0,

    K'(s)=-(20/27)*atan(r/s),
    K''(s)=20*r/[27*(s^2+r^2)].

K is continuous at zero and these derivatives have finite right limits
there. The restriction to s>=0 admits these derivatives at its endpoint;
no two-sided differentiability across the nodal segment is claimed.
Consequently

    |f''(s)|<=531621584371/4084830000<132,
                     0<=s<=6/25.                    (4)

For 6/25<=s<1/4, use monotonicity of F(s,-1), the bound on B',
K'(s)>=-c, and pi<22/7 to get

    f(s)>=f(6/25)-(s-6/25)*(633/100+2*c)
         >=f(6/25)-163637/1890000.                   (5)

This avoids the diverging derivative of F(s,-1) at s=1/4.

### 3. Rational enclosures and complete real-interval coverage

Reproduce the certificate with

    python3 scripts/one-sided-hankel/positive-cone-angular-pair-certificate.py

It writes `scripts/one-sided-hankel/positive-cone-angular-pair-certificate.json`:
all 121 sample enclosures, the constants, 18 exact checks and the complete
failure list. Every check passes. No floating value enters a decision.
The floating screen with the same basename ending `-screen.py` and its
JSON output are design evidence only, not proof inputs.

Here are the exact formulas and enclosure justification, so the finite
certificate's role is explicit. For b>=0 define

    J(b,t)=(t/2)*log(b^2+t^2)-t+b*atan(t/b), b>0,
    J(0,t)=(t/2)*log(t^2)-t, t!=0,
    I(A+i*B)=J(|B|,1-A)-J(|B|,-A).

Differentiating J shows I(w)=integral_0^1 log|w-t| dt for all inputs
used here. The real inputs have A>1; complex inputs and endpoints are
nonsingular. With a=x+s,

    F(s,u)=I(x/u)-I(a/u)+(1/2)*log(|a|^2/d^2)
                         +I(U*u/a)-I(U*u/x),
    K(s)=(10/27)*[2*r*(log r-1)-J(s,r)+J(s,-r)].

The formulas for F(-s,v) use a=x-s. Coordinates and squared moduli
are rational for s=j/500, 0<=j<=120, and u=v or -1.

The script scales each positive logarithm argument by a power of two
into [1,2]. For z=(w-1)/(w+1) in [0,1/3], summing the first 24 terms
of 2*sum_(j>=0) z^(2j+1)/(2j+1) gives a lower bound; its positive
tail is at most 2*z^49/[49*(1-z^2)]. Log 2 is enclosed the same way,
with the correct sign when a power is negative. Arctangent reciprocal
and pi/4 addition identities reduce to arguments of absolute value
<=1/2; 32 alternating terms have absolute error <=|z|^65/65.
The classical Machin identity pi=16*atan(1/5)-4*atan(1/239) encloses
pi and verifies pi<22/7. It follows from tangent addition with the
quadrant fixed. The logarithm and arctangent remainder bounds follow
by integration of the finite geometric identities. All interval sums,
signed scalar products and rounding use exact fractions.

Sample bounds are rounded outward to multiples of 10^(-12). The minimum
of the 121 lower endpoints and the last lower endpoint are respectively

    m=-3466760611/500000000000,
    f(6/25)>=12180131927/100000000000.                 (6)

For adjacent samples, the elementary linear-interpolation remainder
and (4) lower-bound f by the smaller endpoint minus

    (132/8)*(1/500)^2=33/500000.

Therefore the entire compact interval satisfies

    f(s)>=-3499760611/500000000000>-3/400,
                      0<=s<=6/25.

Combining (5) with (6) yields on the remaining interval

    f(s)>=665674934203/18900000000000>0,
                      6/25<=s<1/4.

This proves (2) on its full interval. The sample minimum alone is not
the continuous bound, and the excluded singular endpoint is not sampled
or silently covered by a bounded-derivative assertion.

### 4. Every allowed contour crosses this interval

Zero is in Omega, whereas 1/4 is outside closure(Omega), because
|x+1/4|=1 violates D. The connected component containing zero of
{s in [0,1/4]:s in Omega} contains an initial interval. Its right
endpoint s_* is strictly between zero and 1/4 and belongs to Gamma.
Apply (2) at z=s_* and u=-1 to prove (3). No rectangular shape,
symmetry, convexity, height restriction or n-independent contour is
assumed. The result applies to every q>=1 in the stated class.

The height-3/20 floating test was also recorded but is unnecessary to
this proof. Nothing here turns a lower bound on a supremum of continuum
exponents into a lower bound on an oscillatory contour integral, or
identifies the auxiliary coefficients with the original unit residues.

### 5. Signed angular mean specialization — 2 November 2026, step 46

Put J=n-1, p_j=t_j*x/U and a_k=x+i*y_k. Define

    T_j(a)=(x-a)/a
      *product_(l=1..J) (x-t_l*p_j)/(a-t_l*p_j)
      *product_(1<=l<=J, l!=j) (t_j*x-t_l*a)/(x*(t_j-t_l)),
    I_n(a)=x/a+sum_(j=1..J) T_j(a).

Then the actual normalized angular mean, with all interior residues
retained, is exactly

    m_n=mean_(|u|=1) [1+sum_(a!=x)b_a*W_a(u)]
       =1+2*sum_(k=0..2q-1) b_(a_k)*Re I_n(a_k).       (4)

This is the b=x specialization of C645o's equation (4), not a new
residue theorem or a new general mean identity. For completeness the
product-specific applicability and simplification are as follows.
The exact rational continuation is

    W_a(u)=(x/a) product_(l=1..J)
      [(x-t_l*u)/(a-t_l*u)] [(U*u-t_l*a)/(U*u-t_l*x)].

Its only possible nonzero interior poles are the distinct p_j, since
|p_j|<80/121<1 whereas |a/t_l|>5/4>1. There is no boundary pole.
At zero all l>=1 factors cancel in pairs, so W_a(0)=x/a. The residue
of W_a(u)/u at p_j is obtained by replacing its j-th second factor
by t_j*(x-a)/U and dividing by p_j. Together with x/a this gives
(x-a)/a. All remaining second factors give the second product in
T_j(a); all first factors give its first product. Their denominators
are nonzero, because a is nonreal, p_j is real, x!=0 and t_j!=t_l.
Any cancelled candidate pole simply has zero residue. Thus the
residue theorem gives mean W_a=I_n(a).

The imported theorem is R. W. Howell and J. H. Mathews, *Complex
Analysis*, online edition (front matter updated 22 August 2025),
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
reusing the source reading recorded in C645o. Its circle integral
divided by 2*pi*i is the normalized angular mean of W_a. No contour
deformation through the interior poles or holomorphic disk-mean
substitution is made.

All constants in T_j except a are real. Hence
I_n(conjugate(a))=conjugate(I_n(a)). Section 1's even positive branch
and the L673 phase identity give equal positive coefficients at each
conjugate pair. This proves (4), including its reality. The branch
and sign argument needed here was checked directly in step 46; the
separate real-crossing certificate was not re-audited.

For every n the standard Cauchy--Schwarz inequality on the probability
space T gives

    ||1+sum b_a*W_a||_2 >= |m_n|.                      (5)

A lower bound |m_n|>=exp(-alpha*n)*n^(-C), alpha<1/100, on a specified
unbounded sequence would exclude these particular coefficients as a
rate-1/100 countersequence on that sequence. It would not exclude other
subsequences or lower-bound kappa_e, an infimum over all coefficients.
Conversely small or zero m_n
does not upper-bound this residual's norm. No such asymptotic bound
is proved here.

The standard-library script
`scripts/one-sided-hankel/positive-cone-angular-mean-screen.py`
evaluates the full finite expression, with every signed residue saved
in its `.json` sibling. Run it with

    python3 scripts/one-sided-hankel/positive-cone-angular-mean-screen.py

It uses Decimal at 80 and 140 digits and approximate solutions of the
phase-node equation. It does not use interval arithmetic; precision
agreement is a diagnostic, not a rigorous error bound. For q=1,2,4
it also independently integrates the full residual using 512 and
1024 angular samples in double precision. No alias or roundoff bound
for those samples is asserted. The values rounded below are diagnostic:

| n | computed m_n | computed -log(abs(m_n))/n |
|---|---:|---:|
| 15 | 2.07389446105 | -0.0486285481 |
| 27 | -0.573467966686 | 0.0205945630 |
| 51 | -0.249033956595 | 0.0272581573 |
| 99 | -0.0933167985947 | 0.0239571226 |
| 195 | -0.0115556350477 | 0.0228747799 |

The two precision runs differ by less than 2.4e-42 at every listed n;
the small-q independent mean comparisons differ by less than 1.4e-15.
These are observed discrepancies, not certified enclosures. In
particular these five values cannot establish a limiting exponent,
a sign, an onset, or a norm estimate on unbounded q. The required
discriminator remains unproved. The scalar test is parked without
asserting failure of the explicit witness or the cone bound. No claim
of progress beyond the already recorded residue formula is made.

## Mathlib

Full matching coverage for this angular-pair crossing obstruction has
not been checked; no absence claim is made. Principal logarithms,
residues, differentiation, interpolation remainders and elementary
series would be supporting results, not a matching quantitative theorem.
No formal verification or independent critical audit is claimed.
Full matching coverage for the specialization (4) was not checked.
The named residue theorem and Cauchy--Schwarz are supporting inputs;
neither supplies the missing quantitative signed-mean estimate.
