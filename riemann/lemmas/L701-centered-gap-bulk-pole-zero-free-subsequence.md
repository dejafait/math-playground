# Lemma 701: zero-free microscopic bulk disks on an infinite subsequence

## Hypotheses

Fix any one of L699's exact prescribed-center Picard profiles. Its choices,
including the cutoffs and positive gap width, precede n. The properties
used here are its real shifts, summability, cap and reflection:

    sum_(m in Z)|e_m|<infinity,  |e_m|<=1/8,
    e_(-m-1)=-e_m.

Use exactly L666/L699's constants and finite family:

    d=5/4, x=-d, R=11/8, U=121/64, A=27/10, Y=A/6=9/20,
    n=12q+3, q>=1, j=(n-1)/2=6q+1, M=4q+1,
    a_m=x+i*(A/n)*(m+1/2+e_m),       -2q<=m<2q,
    Z_n={x} union {a_m},
    p_j=-d*j/(U*n),       c_(0,n)(u)=R^(-1) sum_(a in Z_n) W_a(u).

The W_a are the full rational continuations in L666 (6). Retain unit
original masses, the anchor, the original product's j=0 factor, inverse
denominator angle and all M downstream spatial moments. No approximation
to the infinite profile, finite support, tail rate, same-sign residues,
scalar charge payment, H/support or Xi realization is assumed.

## Conclusion

For every such fixed profile, infinitely many allowed n have the following
property: the removable extension

    (u-p_j)*c_(0,n)(u)

has **no zeros in the closed disk** |u-p_j|<=d/(4*U*n). Consequently the
proposed eventual count of exactly one zero in this disk is false, for
each fixed profile in the stated class. This is an obstruction to the
particular microscopic pairing target, not to aggregate scalar charge,
other disks or indices, full-spatial compensation, realization, or RH.

The proof tests the prescribed constant-plus-linear Taylor comparison.
On an infinite subsequence its polynomial is zero-free in the disk and
strictly dominates the nonlinear remainder on the entire boundary.
Multiplicities, possible cancelled poles and boundary zeros are handled
below. The onset can depend on the fixed profile; no effective onset or
uniform onset over the Picard choices is asserted.

Step 137 critically audited the analytic proof and complete rational
certificate under the separately approved EXPLORE audit scope. The
conclusion survives with the stated fixed-profile quantifiers; the
replay is byte-identical and the actual Taylor margin is 1/25. This is
an audited local obstruction, not a new discovery in the audit turn.
The bounded source search found no matching theorem; that does not
certify originality. There is no candidate resolution of RH.

## Proof

### 1. Approved scope, exact local coordinate and holomorphy

Reuse `drafts/literature/2026-11-03-centered-gap-bulk-pole-pairing.md`.
The target and its exact family are unchanged. L666 supplies the rational
continuation, and L699 supplies the selected reflected summable profile.
L699's conditional interlacing and charge conclusions are not premises.
L700's audited fixed-index obstruction is a contrast; none of its
fixed-index error terms is used at the moving index j.

Set u(s)=-d*(j+s)/(U*n), so the prescribed circle becomes |s|=1/4.
For a real ordinate y set w(y)=(1-i*y/d)^(-1), and define

    P_n(z)=product_(k=1)^(n-1)(1-z/k),
    T_n(z,w)=product_(k=1)^(n-1)(1-w*k*z/(U*n^2)),
    h_n(s,y)=w(y)*P_n((j+s)*w(y))/T_n(j+s,w(y)),
    S_n(s)=sum_(a in Z_n) h_n(s,Im a).

Exact division in L666 (6) gives

    W_(x+i*y)(u(s))
       =w(y)*P_n((j+s)*w(y))*T_n(j+s,1)
                      /[P_n(j+s)*T_n(j+s,w(y))],
    F_n(s):=(u(s)-p_j)*c_(0,n)(u(s))
       =-d/(U*n*R) * [s*T_n(j+s,1)/P_n(j+s)] * S_n(s).       (1)

The anchor contributes h_n(s,0) to S_n, so its original W_x=1 has
not been dropped. The leading w is precisely the original j=0 factor.
On a neighborhood of |s|<=1/2 the only possible interior angular pole
is the one at s=0, removed in (1). The other interior poles are at
nonzero integer s. L666's exterior poles a/t_k have modulus at least
d, whereas |u(s)|<=d/(2U)<d on this closed disk. Also |w(y)|<=1 and
|k*(j+s)/(U*n^2)|<1/(2U)<1 there, so every T denominator is nonzero.
P_n has a simple root at j, making s/P_n(j+s) holomorphic and nonzero.
Thus F_n and S_n are holomorphic on a neighborhood of the closed disk,
including if the original scalar pole cancels. No residue sign is used.

### 2. Primary analytic inputs and a uniform finite-product estimate

Import gamma recurrence, reflection and the finite-product identity from
[NIST DLMF 5.2.5](https://dlmf.nist.gov/5.2#E5),
[5.5.1](https://dlmf.nist.gov/5.5#E1) and
[5.5.3](https://dlmf.nist.gov/5.5#E3). Their application gives

    P_n(zeta)=Gamma(n-zeta)*Gamma(zeta)*sin(pi*zeta)
                                    /[pi*Gamma(n)].          (2)

Initially this follows away from integer zeta. When both gamma arguments
have positive real part, their factors are holomorphic and finite, so
(2) extends to the integer zeros by continuity. We never divide by the
sine at a zero.

For quantitative Stirling use F. Johansson, *Arbitrary-precision
computation of the gamma function*,
[arXiv:2109.08392v1](https://arxiv.org/pdf/2109.08392v1),
17 September 2021, equations (21)–(27),(30)–(32), Theorem 3.2,
printed pp.11–14. For N=1 it gives

    log Gamma(z)=(z-1/2)log z-z+log(2*pi)/2+R_1(z),
    |R_1(z)|<=sec(arg(z)/2)^2/(12*|z|),     z not in (-infinity,0].

The source and its complete complex-case remainder proof were read in
the assessment. Use the principal logarithm in the right half-plane.
No constant-shift gamma-ratio theorem is applied to a varying shift.
The following specialization pays that uniformity directly.

For 0<=y<=Y put v=w(y)/2 and define, with principal logarithms,

    I(v)=integral_0^1 log(1-v*t/U)dt
        =-1-(U/v-1)*log(1-v/U),
    Jcal(v)=integral_0^1 t/(U-v*t)dt
        =-1/v-(U/v^2)*log(1-v/U),
    g(y)=(1-v)*log(1-v)+v*log(v)-i*pi*v-I(v),
    b0(y)=w*[log(v/(1-v))-i*pi+Jcal(v)],
    a(y)=i*w/sqrt(2*pi)
             *exp((log(1-v/U)-log(v)-log(1-v))/2).            (3)

Here I'(v)=-Jcal(v). All displayed logarithms have arguments in the
right half-plane, apart from the already explicit imaginary linear
term. Their branches are therefore fixed; a(y) never vanishes.

Uniformly for 0<=y<=Y and |s|<=1/2, let sigma=s-1/2. Then
zeta=(j+s)w=n*v+sigma*w, with Re(v)>=625/1412>0 and
Re(1-v)>=1/2. Both gamma arguments in (2) have modulus at least c*n
and lie uniformly inside the right half-plane, for an absolute c>0.
Johansson's bound is O(1/n) there. Expanding the bounded shifts
sigma*w in the logarithms, with remainder n*O(n^(-2))=O(1/n), yields

    Gamma(n-zeta)*Gamma(zeta)/Gamma(n)
      =sqrt(2*pi/n)*exp(n*((1-v)*log(1-v)+v*log(v)))
         *exp(sigma*w*log(v/(1-v)))
         *exp(-(log(v)+log(1-v))/2)*(1+O(1/n)).              (4)

This error is uniform over the stated compact y,s set. The equality
log(v)-log(1-v)=log(v/(1-v)) uses these same right-half-plane branches.

For T_n, apply the composite trapezoidal estimate
([DLMF 3.5.1–3](https://dlmf.nist.gov/3.5#i)) to
t -> log(1-v*t/U). Its second derivative is uniformly bounded since
|v|<=1/2<U. Taylor expansion in sigma*w/n has uniformly bounded
second derivative as well. Summing these remainders gives

    log T_n(j+s,w)
       =n*I(v)-log(1-v/U)/2+sigma*w*I'(v)+O(1/n).           (5)

For completeness, on each mesh interval the error between the integral
and the endpoint trapezoid is bounded by a constant times the supremum
of the second derivative times n^(-3). Summing n intervals and
multiplying by n gives O(1/n) in the sum. The shift expansion contributes
n*O(n^(-2)), also O(1/n). Thus (5) needs no unproved uniform
Euler–Maclaurin or changing-shift hypothesis.

Use the exact identity
sin(pi*zeta)=(i/2)*exp(-i*pi*zeta)*(1-exp(2*pi*i*zeta))
in (2), and combine (4)–(5). The result is

    h_n(s,y)=n^(-1/2)*a(y)*exp(n*g(y))*exp(sigma*b0(y))
        *(1-exp(2*pi*i*(j+s)*w(y)))*(1+O(1/n)).             (6)

The final multiplicative error belongs to the nonvanishing gamma/T
factors, not to a division by the sine. At sine zeros (6) is still an
identity with both sides zero. Since
Im((j+s)w)=n*Im(v)+Im(sigma*w)>=n*Im(v)-1 and Im(v)>=0,
the explicit sine bracket has modulus at most 1+exp(2*pi). Hence

    |h_n(s,y)|<=C*n^(-1/2)*exp(n*Re(g(y)))                  (7)

uniformly on the whole compact set, including y=0. This absolute
bound, rather than a relative estimate at a vanishing sine, will
justify the endpoint sum.

### 3. Strict endpoint growth and the exact shifted finite sum

Write t=y/d, so 0<=t<=9/25 and w=(1-i*t)^(-1). Then
v/(1-v)=1/(1-2*i*t), and differentiation of (3) gives

    dg/dt=(i/2)*w^2*[-i*pi-log(1-2*i*t)+Jcal(v)].           (8)

On this interval Re(w^2)=(1-t^2)/(1+t^2)^2>=2/3 and |w|<=1.
The first inequality follows by differentiating the decreasing function
of t^2, or checking its minimum 85000/124609>2/3. Also

    |log(1-2*i*t)|<=integral_0^t 2/|1-2*i*r|dr<=18/25,
    |Jcal(v)|<=1/[2*(U-1/2)]=32/89.

Using pi>3 in (8) gives

    d Re(g)/dt > 1-9/25-16/89=1024/2225>9/20,
    d Re(g)/dy >9/25.                                     (9)

In particular the two outer endpoints dominate in modulus and
Re(g'(Y))>0; the prime here and below is a y derivative.

For the positive half of the exact finite family, put l=2q-1-m. Its
ordinates, with no endpoint relaxation, are

    y_(n,l)=Y-A*(l+1)/n+A*e_(2q-1-l)/n,
                      0<=l<=2q-1.                         (10)

For each fixed l, summability implies e_(2q-1-l)->0. Consequently
n*(y_(n,l)-Y)->-A*(l+1). Equation (6), uniformly in |s|<=1/2,
therefore gives

    n^(1/2)*exp(-n*g(Y))*h_n(s,y_(n,l))
       ->a(Y)*exp((s-1/2)*b0(Y))*exp(-A*(l+1)*g'(Y)).       (11)

The sine bracket tends to one since Im(w(Y))>0. To justify summing
(11), the cap and (9) imply

    Y-y_(n,l)>=A*(l+7/8)/n,
    n^(1/2)*exp(-n*Re(g(Y)))*|h_n(s,y_(n,l))|
       <=C*exp(-(9*A/25)*(l+7/8)).                         (12)

The bound is summable in l and uniform in n,s. Extend the finite sum
by zero outside its allowed l range, first pass to the limit on any
fixed initial block, and then bound both tails by (12). This proves
uniform convergence of the summed asymptotic; no unproved exchange of
a signed sum and a pointwise limit is used. The exact anchor h_n(s,0)
is exponentially smaller by (7),(9), and is included in the error.
Reflection from L699 gives
h_n(s,-y)=conjugate(h_n(conjugate(s),y)). Thus, putting

    theta=Im(g(Y)),
    D=a(Y)*exp(-b0(Y)/2)/(exp(A*g'(Y))-1),                  (13)

we obtain, uniformly on |s|<=1/2,

    S_n(s)/(n^(-1/2)*exp(n*Re(g(Y))))
       =D*exp(i*n*theta)*exp(b0(Y)*s)
        +conjugate(D)*exp(-i*n*theta)*exp(conjugate(b0(Y))*s)
        +o(1).                                          (14)

The geometric denominator in (13) is nonzero because Re(g'(Y))>0;
D is nonzero. The constants in (13) do not depend on the shifts.
The rate of the o(1) can depend on the fixed profile, through its tail;
no tail rate or uniform onset has been supplied or assumed. This proof
only uses e_m->0, the cap and reflection, all satisfied by the selected
profiles. Their Fourier gap is not used to replace any signed estimate.

### 4. Restoring the pole-removed prefactor and its Taylor coefficients

Since n=2j+1, (2) gives the exact local identity

    s*P_n'(j)/P_n(j+s)
      =(pi*s/sin(pi*s))
         *Gamma(j)*Gamma(j+1)/[Gamma(j+s)*Gamma(j+1-s)].    (15)

Interpret both sides removably at s=0. The gamma quotient tends
uniformly to one on |s|<=1/2 by the same positive-real-sector Stirling
bound and bounded-shift expansion used above. Equation (5), or direct
logarithmic differentiation of the finite product, gives

    T_n(j+s,1)/T_n(j,1)->exp(-Jcal(1/2)*s)                 (16)

uniformly on that disk. Set

    C_n=-d/(U*n*R)*[T_n(j,1)/P_n'(j)]
                         *n^(-1/2)*exp(n*Re(g(Y))),
    b=b0(Y)-Jcal(1/2)=alpha+i*beta,
    V(s)=pi*s/sin(pi*s),       V(0)=1.

Here T_n(j,1)>0 and P_n'(j) has sign (-1)^j=-1, so C_n>0.
Equations (1),(14)–(16) yield the uniform analytic asymptotic

    F_n(s)/C_n
       =V(s)*[D*exp(i*n*theta)*exp(b*s)
          +conjugate(D)*exp(-i*n*theta)*exp(conjugate(b)*s)]
          +o(1),                 |s|<=1/2.                (17)

The error is also holomorphic. Uniform convergence on this larger disk
controls its first derivative at zero by the Cauchy integral formula
([DLMF 1.9.30–31](https://dlmf.nist.gov/1.9#E31)).
Thus (17) will control the actual Taylor polynomial, not merely values
or a formal asymptotic derivative.

### 5. Certified constants and infinitely many suitable phases

The exact-rational certificate is generated by

    python3 scripts/one-sided-hankel/centered-gap-bulk-pole-certificate-135.py

Its full output is
`scripts/one-sided-hankel/centered-gap-bulk-pole-certificate-135.json`.
It encloses (3) at w(Y)=(625+225*i)/706, v=w(Y)/2 and gives

    0.564 < alpha < 0.566,
    -2.177 < beta < -2.175,
    -5.257 < 12*theta/pi < -5.255.                          (18)

Here and below terminating decimals denote exact rationals. In
particular exp(24*i*theta)!=1. Write phi_n=n*theta+arg(D).
For n=12q+3, the finite geometric sum for exp(2*i*phi_n) divided
by the number of q tends to zero: its ratio exp(24*i*theta) is not
one, and its numerator has modulus at most two. Therefore

    lim_(Q->infinity) (1/Q)*sum_(q=1)^Q cos(phi_(12q+3))^2=1/2.

There are infinitely many q with cos(phi_n)^2>=49/100, since an
eventual upper bound below 49/100 would contradict that average.
On these indices cos(phi_n) is nonzero and

    |tan(phi_n)|<=sqrt(51/49)<21/20.                        (19)

No irrationality or equidistribution assertion is required. Define
t=tan(phi_n) and divide (17) by 2*|D|*cos(phi_n). This divisor has
modulus at least 7*|D|/5. On the selected subsequence the result is

    A_n(s):=F_n(s)/(2*C_n*|D|*cos(phi_n))
       =H_t(s)+o(1),
    H_t(s)=V(s)*exp(alpha*s)*(cos(beta*s)-t*sin(beta*s)),    (20)

uniformly on |s|<=1/2. Its constant-plus-linear polynomial is

    ell_t(s)=1+lambda*s,       lambda=alpha-beta*t.          (21)

### 6. A full-boundary Taylor margin, with zero interior comparison roots

The following certificate bounds hold for all real |t|<=21/20, not
just the phases selected above. Put r=1/4. From (18),

    |lambda|<=L=0.566+(21/20)*2.177=2.85185,
    |ell_t(s)|>=1-L*r=0.2870375>7/25,      |s|=r.           (22)

Since L*r<1, ell_t has no zeros in the closed disk. We now justify
the certified bound

    |H_t(s)-ell_t(s)|<1/5,                  |s|=r.          (23)

Let D0(s)=sin(pi*s)/(pi*s) and
N_t(s)=exp(alpha*s)*(cos(beta*s)-t*sin(beta*s)). The coefficient
of s^k in N_t is Re((1+i*t)*b^k)/k!. The coefficients of degrees
two through four in N_t-D0*ell_t are respectively A_k+t*B_k, where

    A_2=Re(b^2)/2+pi^2/6,         B_2=-Im(b^2)/2,
    A_3=Re(b^3)/6+alpha*pi^2/6,   B_3=-Im(b^3)/6-beta*pi^2/6,
    A_4=Re(b^4)/24-pi^4/120,      B_4=-Im(b^4)/24.          (24)

The constant and linear terms vanish exactly. The certificate retains
the shared t in these affine expressions before taking absolute bounds;
it does not infer cancellation from separately rounded sampled values.
Using the intervals (18), it bounds the three boundary costs
(|A_k|+(21/20)*|B_k|)*r^k by 0.116218, 0.042328 and 0.004718.

For the complete tails, |b|<B=9/4, |1+i*t|<=29/20 and
exp(B*r)<9/5. Thus the remaining N_t terms, k>=5, cost at most

    E_N=(29/20)*(9/5)*(B*r)^5/5!.

Write Q2=(pi*r)^2. The omitted D0*ell_t terms cost at most

    E_D=L*r*Q2^2/120
          +(1+L*r)*Q2^3/[5040*(1-Q2/72)].                  (25)

The first term is its degree-five term. The second bounds all D0
terms of degree at least six and their products with lambda*s;
their successive absolute ratios are at most Q2/72. Similarly

    |D0(s)|>=1-Q2/[6*(1-Q2/20)]>89/100.                   (26)

The ratio Q2/20 bounds successive terms starting with degree two.
Combining (24)–(26), with outward rational arithmetic throughout, gives

    |H_t-ell_t|
      <=[sum_(k=2)^4 (|A_k|+(21/20)|B_k|)*r^k+E_N+E_D]
                         /[1-Q2/(6*(1-Q2/20))]
      <0.186627<1/5.                                    (27)

The certificate's unrounded enclosing upper value is less than
0.186626247219239. Its full arithmetic margin against (22) exceeds
0.100411252780761. These bound the whole complex circle through
absolutely convergent power series; there is no boundary sampling.

To document the finite constants completely, the script uses only
Python integers and Fraction arithmetic. For each rational complex z
in the right half-plane it computes

    log z=2*sum_(k=0)^(N-1) tau^(2k+1)/(2k+1)+error,
    tau=(z-1)/(z+1),
    |error|<=2*q0^(2N+1)/[(2N+1)*(1-q0^2)],

with N=60, q0=2/3 and an exact check |tau|^2<q0^2. Import the
principal-logarithm series from [DLMF 4.6.4](https://dlmf.nist.gov/4.6#E4);
the absolute geometric tail above is needed for this finite certificate.
Re(z)>0 selects the branch. The four inputs
are v, 1-v, 1-v/U and the positive real 89/121. The exact transform
norm squares are respectively 949/5949, 625/6921, 80000/4038273 and
256/11025. For pi use Machin's identity with 40 terms of each alternating
arctangent series ([DLMF 4.24.3](https://dlmf.nist.gov/4.24#E3)) and the
absolute next-term error. The identity
4*atan(1/5)-atan(1/239)=pi/4 follows from the tangent addition formula
and its angle in (0,pi/2). These elementary series bounds are included
to certify constants, not presented as new source theorems. Each exact
interval is rounded outward to a rational decimal grid before storage.
The bound exp(9/16)<9/5 is separately checked by its positive Taylor
sum through degree 20 and geometric bound on the remaining ratios.

The generator reports PASS with no failures. All four complete logarithm
records, all three coefficient records, the b enclosure, phase bounds
and aggregate margins were inspected; they are finite rational evidence.
An initial unavailable mpmath import was replaced by this independent
standard-library certificate. A preliminary double calculation is not
an input to any displayed enclosure or to the analytic proof.

### 7. Transfer to the exact Taylor polynomial and Rouche zero count

Import analytic Rouche's theorem, with multiplicities and strict
full-contour inequality, from
[NIST DLMF 1.10(iv)](https://dlmf.nist.gov/1.10#iv), also the inspected
Mathews–Howell, *Complex Analysis*, Section 8.7,
[Corollary 8.7.12 and Remark 8.7.13](https://complexanalysis.org/web/sec_argument-rouche.html).
This is a named theorem application, not a reproof or a generalized
meromorphic variant. Both functions used below are holomorphic on a
neighborhood of the actual prescribed closed disk.

For each fixed profile, take sufficiently large n in the infinite
subsequence (19) that |A_n-H_t|<epsilon=1/100 on |s|<=1/2. The
Cauchy integral formula gives |A_n'(0)-H_t'(0)|<2*epsilon.
Let ell_n(s)=A_n(0)+A_n'(0)*s be the actual Taylor polynomial.
On |s|<=r,

    |ell_n-ell_t|<(3/2)*epsilon.

Consequently on the full boundary,

    |ell_n|>7/25-3/200=53/200,
    |A_n-ell_n|<1/5+5/200=45/200<|ell_n|.                  (28)

Moreover |ell_n-1|<=L*r+3/200<1 on the closed disk, so ell_n
has no zeros there. This also covers a vanishing derivative: its
nonzero constant then remains. Rouche and (28) imply zero interior
zeros of A_n, counted with multiplicity. The same strict inequality
excludes boundary zeros. Undoing the nonzero normalization in (20) and
the affine coordinate u(s) proves the conclusion for the exact F_n.
In particular F_n(0) is nonzero on these sufficiently large selected
indices, so a cancelled scalar pole cannot be a hidden center zero.

The subsequence is unbounded for every fixed profile. Thus this is a
failure of the stated eventual-one target, not a finite exceptional n
or a numerical failure to locate a root. No extension across bulk
indices, charge estimate or actual-Xi assertion follows from it.

### 8. Conceptual and exact-arithmetic audit, 3 November 2026

Step 137 used the prior EXPLORE assessment
`drafts/literature/2026-11-03-centered-gap-bulk-pole-audit-scope.md`.
It checked (1)–(28), including the complete generator and all four log
records, three coefficient records and aggregate bounds. It imports the
named source tools with their saved hypotheses; it does not reprove
Stirling, quadrature, Cauchy or Rouche. The following details make the
load-bearing uniformities and certificate checks explicit. No new lemma
or extension of the conclusion is asserted.

For (1), division of each pair of k>=1 factors in L666 (6) cancels
its a/x and x/a constants, leaving T_n(z,1)/T_n(z,w) and
P_n(zw)/P_n(z); the sole uncancelled factor is the original k=0
factor w. The anchor is exactly one before removal of the scalar pole.
All other possible poles remain outside |s|<=1/2, as stated in Section 1.
The direct mathematical inputs remain L666 and L699; the latter supplies
the already-audited reflected summable profile, not its conditional
charge estimate or a residue-sign hypothesis.

For n>=15, |sigma*w|<=1 and Re(v)>=625/1412 imply
Re(n*v+sigma*w)>=n/3 and Re(n*(1-v)-sigma*w)>=n/3.
Both gamma arguments have modulus <=2*n. Hence their arguments remain
in a fixed sector strictly inside the right half-plane, their moduli
grow at least linearly, and the N=1 Johansson remainder is uniformly
O(1/n). Every segment used to expand the bounded shifts also has real
part >=n/3. The logarithmic Taylor remainders in (4) are therefore uniform.
Here v/(1-v)=(1-2*i*y/d)^(-1) has positive real part; the two principal
arguments subtract within (-pi,pi), so no hidden 2*pi*i enters b0.

For (5), put delta=sigma*w and v_n=v+delta/n. On the whole parameter
set |v_n|<=17/30<U. Trapezoidal quadrature for
f(t,v_n)=log(1-v_n*t/U), with uniformly bounded t derivatives, gives
n*I(v_n)-f(1,v_n)/2+O(1/n), since f(0,v_n)=0.
Expanding I(v_n) and f(1,v_n) on that fixed compact set yields (5),
including delta*I'(v). This controls both the mesh and bounded-shift
errors for complex s. Applying the absolute quadrature remainder to
real and imaginary parts avoids a complex mean-value assertion.

The sine bracket in (6) is retained exactly. Thus (7) is valid also at
vanishing sine values, and (9) applies over every ordinate actually used.
The exact endpoint (10), the cap and e_m->0 give (11)–(12).
For any fixed initial number of endpoint terms, their convergence is
uniform in s; the remaining normalized terms are bounded by the same
summable geometric series in (12). Letting the initial number increase
after taking the n limit proves uniform convergence of the whole sum.
The anchor contribution included in the error is exponentially smaller because
Re(g(Y))-Re(g(0))>(9/25)*Y>0. Reflection then gives (14), with conjugation
applied to s as well as coefficients. The nonzero amplitude D follows
from Re(g'(Y))>0 and the nonvanishing exponentials in (13). No rate for
the profile tail or onset uniform in profiles is introduced.

Differentiating (2) at j gives
P_n'(j)=(-1)^j*Gamma(j)*Gamma(j+1)/Gamma(n), which verifies (15),
its removable center and the positive sign of C_n when j=6q+1.
The bounded-shift expansion verifies its gamma quotient tends to one;
(5) verifies (16). All factors and errors in (17) are holomorphic on
a neighborhood of the closed half-unit disk. Thus Cauchy controls the
actual derivative, even though the comparison phase changes with n.

The interval operations were checked for exact operand types: all
initial inputs are integers or Fraction values, interval reciprocals
exclude zero, and multiplication takes the four rational corner products.
No binary floating-point input is used. The negative and positive
rounding directions in outward() are floor and minus-floor respectively;
serialization preserves the resulting decimal rationals. Each logarithm
tail uses the exact transform norm test and includes all omitted terms.
For Machin's angle, tan(2*atan(1/5))=5/12 and
tan(4*atan(1/5))=120/119. Subtracting atan(1/239) gives tangent one;
the angle is positive and less than 4/5<pi/2, fixing the branch.
These checks justify the finite implementation of the cited series,
not a new logarithm or arctangent theorem.

The three affine coefficients (24) were checked against N_t-D0*ell_t.
For the N_t tail, (5+k)!>=5!*k! gives the stated exponential bound.
For D0, the successive absolute ratios from degree six and degree two
are at most Q2/72 and Q2/20 respectively; its degree-five product with
lambda*s is separately included. The positive exponential tail after
degree 20 has initial term x^21/21! and ratio at most x/22.
Thus the certificate controls the full complex boundary, not a grid.

Reproduction command, preserving the original step-135 files:

    python3 scripts/one-sided-hankel/centered-gap-bulk-pole-audit-137.py

The full replay is
`scripts/one-sided-hankel/centered-gap-bulk-pole-certificate-replay-137.json`;
the hash, exact transform/tail and independently recombined margin checks
are in `scripts/one-sided-hankel/centered-gap-bulk-pole-audit-137.json`.
The replay is byte-identical to step 135, and all 22 audit checks pass.
Recombining the outward stored coefficient boxes and tail bounds gives
the independent upper value

    170832799175257826082521596581851
       /915373918302995225092080866913280 < 0.186627 < 1/5.

The exact limiting linear lower bound is 22963/80000=0.2870375>7/25.
The complete phase enclosure (18) excludes every integer value of
12*theta/pi. Therefore the geometric average is 1/2; if only finitely
many cos(phi_n)^2 were >=49/100, its limsup average would instead be
<=49/100. This proves an infinite allowed subsequence without assuming
irrationality, and its normalizing factor is bounded away from zero.

Finally choose n on that subsequence with the proved uniform error
<1/100. Cauchy gives the first-derivative error <2/100 and the Taylor
polynomial error <3/200 on |s|<=1/4. The actual polynomial is zero-free
because its distance from 1 is <58237/80000<1. Its boundary modulus
is >53/200 while the full remainder is <45/200, leaving margin 1/25.
Analytic Rouche counts zero interior zeros with multiplicity, and the
same strict inequality excludes boundary zeros. Nonzero normalization
and the affine coordinate preserve that count; a cancelled center pole
cannot be concealed. These checks accept the original conclusion only
at its stated index/radius and fixed-profile quantifiers.

## Mathlib

Full matching coverage for this finite-family endpoint asymptotic and
zero-free-subsequence assertion is not checked. This is not evidence
of absence, and no formal verification is claimed. The named gamma,
Stirling-remainder, Cauchy and Rouche inputs are precisely cited above;
the family-specific estimates and rational certificate have passed the
step-137 conceptual audit. They remain an informal proof, not a formal
verification; effective/profile-uniform onsets and other disks are not
supplied.
