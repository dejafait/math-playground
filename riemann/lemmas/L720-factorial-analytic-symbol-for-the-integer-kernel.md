# Lemma 720: factorial analytic symbol for the exact integer-size kernel

## Hypotheses

Use L719's exact kernel, contour, common complex neighborhoods, logarithmic
product estimates and phase identification. Its proof is an input and
passed the separate step-192 audit in L719 Section 7. In particular retain

    U=121/64, A=27/10, d=5/4, u=(3+4i)/10, alpha=11/8,
    n=12q+3, q>=1,
    omega=A*[log(9/5)-4/5+(121/100)*log(201/121)],
    I=[omega-delta,omega+delta], 0<delta<1/3000,
    z_v=exp(-u*v/A), s_v=-z_v*F'(z_v),
    D_n=d*product_(k=1)^(n-1) (d+u*k/n)/(U*u+d*k/n),
    R_n(s)=product_(k=1)^(n-1)(U+s*k/n)
                         /product_(j=0)^(n-1)(s+j/n),
    b_(n,j)=(-1)^j*n^(n-1)/[j!*(n-1-j)!]
                         *product_(k=1)^(n-1)(U-j*k/n^2),
    p_n(v)=(n*D_n/A)*exp(-n*d*v/A)
                     *sum_(j=0)^(n-1) b_(n,j)*z_v^j/(alpha+u*j/n).

F is the open-unit-disk function specified in L719 through the audited
polynomial limit. The original fixed bump and its width are unchanged.
The proof needs no analyticity, endpoint law or sign property of that
bump. Define, with the right-half-plane logarithms used in L719,

    f(s,t)=Log(U+s*t)-Log(s+t),
    g(t)=Log(d+u*t)-Log(U*u+d*t),
    ell_D=integral_0^1 g(t)dt,
    Phi(s;v)=u*v*s/A+integral_0^1 f(s,t)dt,
    S(v)=ell_D+1+log(U)-d*v/A+F(z_v),
    c_0(s)=log(d)-Log(s)-[g(0)+g(1)+f(s,0)+f(s,1)]/2,
    H(v)=s_v^2*Phi_ss(s_v;v).

Here c_0(s) is the logarithmic endpoint correction, not the constant
1/8 in the original inverse transform. L719 gives Re(H)>1/3 and fixes
the positive-real-part branch of sqrt(H). Its fixed complex neighborhood
keeps z_v in the unit disk and the saddle away from every pole. Only
positive integer n of the displayed form are used.

## Conclusion

There are bounded complex neighborhoods I subset W' with closure(W')
compact in W, holomorphic functions a_k on W for every integer k>=0,
and constants C,c,epsilon>0 and n_0 such that

    sup_(v in W') |a_k(v)| <= C^(k+1)*k!,                 (1)
    sup_(v in W') |n^(-1/2)*exp(-n*S(v))*p_n(v)
                   -sum_(k=0)^(m-1) a_k(v)*n^(-k)|
                   <= C^(m+1)*m!*n^(-m),                (2)

for every permitted n>=n_0 and every integer 1<=m<=epsilon*n.
The same constants work at every such order, not just at each fixed
order separately. The leading coefficient is

    a_0(v)=s_v*exp(c_0(s_v))
             /[A*sqrt(2*pi)*(alpha-u*s_v)*sqrt(H(v))],
    inf_(v in W') |a_0(v)|>0.                            (3)

After decreasing epsilon, truncation at m=floor(epsilon*n) has error
at most C*exp(-c*n). Neither the formal series nor its infinite sum
is asserted to converge. The power in the assessed target is beta=1/2.

This completes the local analytic-symbol target, accepted in the separate
step-192 conceptual audit in Section 5 together with its L719 input.
It is a specialization and combination
of the assessed analytic product/Morse/Gaussian tools, not a new general
analytic-symbol calculus or a certified originality claim. It supplies
no rate or lower bound for integral chi(v)*p_n(v)dv. Support-edge transfer,
signed cancellation, comparison with the actual residue, other response
terms, complementary Jensen payment, amplitude/full charge, H/support,
Xi realization and RH positivity remain unresolved. L713, L714 (6),
L717 and L718 are not premises. No RH candidate is asserted.

## Proof

### 1. Source scope and common domains

The invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-signed-bump-analytic-symbol.md` covers exactly
this target and is reused unchanged. The stationary-phase inputs are
M. Hitrik and J. Sjostrand, *Two Minicourses on Analytic Microlocal
Analysis*, [arXiv:1508.00649v1](https://arxiv.org/pdf/1508.00649v1),
Section 2.2, (2.2.1), pp.32--33; Section 2.3, Theorem 2.3.1,
Lemma 2.3.2 and the deformation/Morse proof of Theorem 2.3.3,
pp.37--40. The Gaussian theorem supplies all-order factorial remainders.
The general saddle theorem's optimal-order statement alone would not
prove (2). Its general proof is imported, not reproved; Section 3 below
checks a single uniform one-dimensional chart, the boundary connectors
and the all-order Gaussian hypotheses for this particular phase.

The product estimates are L719 (4)--(5), which already specialize the
exact Euler--Maclaurin formula
[NIST DLMF 2.10(i), (2.10.1)](https://dlmf.nist.gov/2.10#E1).
No noninteger-size interpolation or new Stirling hypothesis is used.
The finite auxiliary-polynomial estimates below verify the missing
exponentiation/truncation hypotheses of this array. Merely citing
closure of analytic symbols would leave those hypotheses unchecked.

Put h=1/n. Choose nested tubes about I whose closures lie in L719's
neighborhood. On the largest closed tube used below, and a common complex
tau disk of radius slightly larger than 1/10 (as provided by L719
Section 5, inside |tau|<101/1000), put

    s=s_v*exp(i*tau),
    psi(tau,v)=Phi(s_v;v)-Phi(s_v*exp(i*tau);v),
    L_n(tau,v)=log[D_n*R_n(s)]
                 -n*[ell_D+integral_0^1 f(s,t)dt]-c_0(s),
    B(tau,v)=s*exp(c_0(s))/(alpha-u*s).

The logarithm in L_n is the factorwise logarithm specified by L719.
All these functions are holomorphic on common domains independent of n.
The denominator in B stays separated from zero. Shrinking these fixed
domains preserves L719's conclusions, in particular

    psi(0,v)=psi_tau(0,v)=0,
    psi_tautau(0,v)=H(v), Re(H(v))>1/3,
    Re(psi(tau,v))>=tau^2/20 for real |tau|<=1/10.     (4)

Bounds below are supremum bounds on these domains or smaller fixed
domains explicitly chosen inside them. Constants can increase from
line to line but never depend on n, m, k or v.

### 2. Finite exponentiation with a uniform factorial remainder

Write ell_j(tau,v)=c_j(s_v*exp(i*tau)) for odd j>=1, where c_j is
L719's logarithmic coefficient, and put ell_j=0 for even j>=2.
After enlarging a fixed B_0>=1, L719 (4) gives

    ||ell_j||<=B_0^j*j!,
    ||L_n-sum_(j=1)^(m-1) ell_j*h^j||
                          <=B_0^(m+1)*m!*h^m          (5)

whenever m*h<=1/2 and h is sufficiently small. Here and below an empty
sum is zero. To check the order conversion in (5), for odd m apply
L719 (4) with its index (m+1)/2. For even m use index m/2+1:
the retained odd powers are exactly those below m, and the remainder
is bounded by C^(m+2)*(m+1)!*h^(m+1). Since (m+1)*h<=1 for the
range in question, enlarging B_0 gives (5). Its m=1 case also gives
||L_n||<=C*h on the whole common complex domain.

For each m>=1 form the finite polynomial in an auxiliary variable z

    P_m(z;tau,v)=sum_(j=1)^(m-1) ell_j(tau,v)*z^j,
    r_m=1/(4*B_0*m).

For |z|<=r_m, the elementary bound j!<=m^(j-1), valid for 1<=j<m,
gives

    ||P_m(z)|| <= (1/m)*sum_(j=1)^(m-1) 4^(-j)
                 <=1/(3*m),
    ||exp(P_m(z))||<=2.                               (6)

Define d_k as the formal coefficient of z^k in
exp(sum_(j>=1) ell_j*z^j). This means a finite polynomial expression in
ell_1,...,ell_k; it requires no convergence of the infinite series.
For k<m it equals the actual Taylor coefficient of exp(P_m(z)).
Cauchy's coefficient estimate with m=k+1 proves

    d_0=1,
    ||d_k||<=2*[4*B_0*(k+1)]^k<=C^(k+1)*k!.           (7)

For example (k+1)^k<=exp(k+1)*k! suffices for the last inequality.
All d_k are holomorphic on the same original domain.

If m*h<=1/(8*B_0), then h<=r_m/2, so Cauchy's Taylor-tail bound and
m^m<=exp(m)*m! give

    ||exp(P_m(h))-sum_(k=0)^(m-1) d_k*h^k||
       <=4*(h/r_m)^m<=C^(m+1)*m!*h^m.                (8)

Both L_n and P_m(h) have uniformly bounded modulus, by (5) at m=1
and (6). The identity

    exp(x)-exp(y)=(x-y)*integral_0^1 exp((1-t)*y+t*x)dt

therefore bounds the difference exp(L_n)-exp(P_m(h)) by a fixed
constant times the error in (5). Combining with (8), and multiplying
by the fixed bounded holomorphic B, yields

    A_n=B*exp(L_n), b_k=B*d_k,
    ||b_k||<=C_b^(k+1)*k!,
    ||A_n-sum_(k=0)^(m-1) b_k*h^k||
                       <=C_b^(m+1)*m!*h^m,            (9)

for every 1<=m<=epsilon_0/h with epsilon_0>0 fixed and small.
Here A_n denotes the exact local amplitude and b_k its formal coefficients.
Also ||A_n|| is uniformly bounded. These estimates hold on a fixed
complex tau domain, before any stationary integration. In particular
their constants do not depend on a truncation-specific shrinking of
that domain. Only the auxiliary z disk depends on m.

### 3. Uniform Morse specialization and the Gaussian functional

Choose a smaller common tau disk. The one-dimensional Morse coordinate
for this phase can be written explicitly as

    w(tau,v)=tau*sqrt(2*psi(tau,v)/tau^2),
    w_tau(0,v)=sqrt(H(v)), psi(tau,v)=w(tau,v)^2/2.     (10)

The quotient at tau=0 is its removable value H. A single branch is
available: on a sufficiently small disk the quotient stays uniformly
close to H, whose real part is >1/3. The branch agrees with the
positive-real-part square root at zero. Common derivative bounds give
w_tau=sqrt(H)+O(tau) uniformly. By shrinking once, this derivative
differs from sqrt(H) by less than one quarter of its modulus. Integration
on line segments in the disk proves injectivity, and Rouche's theorem
on its boundary gives one fixed w disk in every image. The holomorphic
inverse-function theorem then gives a jointly holomorphic inverse
tau=T(w,v) on that disk. Its derivative and range are uniformly bounded
on smaller closed disks. Thus (10) supplies the common-domain and
parameter-uniform hypotheses needed for the cited Morse reduction.

Fix a small real a>0 so that the image of [-a,a] and both its endpoints
lie well inside this inverse disk. Since H has a fixed positive-real-part
lower bound and a fixed modulus upper bound, sqrt(H) stays in a closed
subsector of |arg w|<pi/4. After decreasing a, there is eta>0 with

    |arg w(a,v)|<=pi/4-eta,
    |arg(-w(-a,v))|<=pi/4-eta,
    |w(a,v)|, |w(-a,v)| >= c_a>0                     (11)

uniformly for complex v in the selected tube. Choose a fixed rho>0
smaller than c_a/2 and small enough that |w|<=2*rho lies strictly
inside the inverse disk. The endpoints can be connected to rho and
-rho, respectively, by radial segments followed by circular arcs of
radius rho within their respective sectors in (11). Along these
connectors

    Re(w^2/2)>=rho^2*sin(2*eta)/2=:kappa>0.           (12)

Their lengths are bounded uniformly. All paths lie inside the inverse
disk and cross no singularity. Their dependence on v need not be
holomorphic: they are used for estimates, not to define coefficients.
Cauchy's theorem compares the original image path with [-rho,rho]
plus these two connectors exactly, with their oriented signs retained.

For any holomorphic amplitude b on the common tau disk, define

    T_h(b)(v)=1/(2*pi*A*sqrt(h))
                  *integral_(-a)^a exp(-psi(tau,v)/h)*b(tau,v)dtau,
    b_tilde(w,v)=b(T(w,v),v)*T_w(w,v).

The transformed amplitude is holomorphic and bounded by C*||b|| on
a fixed disk larger than |w|<=rho. Here ||b|| is the supremum on
the original common domain. Equation (12) bounds the normalized
connector contribution by

    C*h^(-1/2)*exp(-kappa/h)*||b||
                         <=C*exp(-kappa/(2*h))*||b||. (13)

Apply Hitrik--Sjostrand Theorem 2.3.1 with dimension one to the real
Gaussian segment [-rho,rho], rescaling w=rho*x. Its amplitude is
holomorphic on a neighborhood of the closed complex unit disk after
rescaling, as required in that theorem. Its small parameter is
h/rho^2, which is <=1 once n is large. The theorem's factor
(r+1)^(1/2)*2^r and the fixed rescaling factors are absorbed into
one constant to the power r+1. It gives the Gaussian coefficients

    G_l(b)(v)=1/[A*sqrt(2*pi)*2^l*l!]
                     *partial_w^(2l) b_tilde(0,v).    (14)

The all-order remainder, divided by the Gaussian sqrt(h), is bounded
by C^(r+1)*r!*h^r*||b|| for every integer r>=1. This uses the
all-order Gaussian theorem, not a conclusion stated only at optimal
truncation order. For the connector term use, for every r>=1,

    exp(-c/h)<=r!*(h/c)^r,                            (15)

which follows from the r-th term of exp(c/h). Thus (13) is absorbed
with the same type of constants. Finally Cauchy's derivative estimate
and (2*l)!/(2^l*l!)<=2^l*l! give, uniformly,

    ||G_l(b)||<=C_G^(l+1)*l!*||b||,
    ||T_h(b)-sum_(l=0)^(r-1) G_l(b)*h^l||
                         <=C_G^(r+1)*r!*h^r*||b||.   (16)

These estimates hold for every r>=1 and all sufficiently small h>0.
The constants, inverse chart and amplitude domain are the same for all
r. The coefficients are jointly holomorphic in v by (10) and (14).
This verifies the required specialization of the imported Gaussian
estimate, including its uniformity and boundary error.

### 4. The exact contour and every-order combination

Set Q_n(v)=n^(-1/2)*exp(-n*S(v))*p_n(v). In L719's positive circle
parameter ds=i*s_v*exp(i*tau)dtau, its exact phase identity gives on
the local arc exactly the normalization T_h(A_n) above. In particular
there is no extra factor of i, n, D_n or sqrt(H). The remaining circle
contribution satisfies

    Q_n=T_h(A_n)+E_n, ||E_n||<=C*exp(-c_*/h)           (17)

for a fixed c_*>0. Here are the complete complement controls. Between
a and 1/10 in absolute tau, (4) and the uniform bound on A_n give a
normalized bound C*h^(-1/2)*exp(-a^2/(20*h)). Outside |tau|<1/10,
L719 (3) gives C*h^(-1/2)*exp(-1/(5000*h)), after multiplying by
the bounded factor D_n*exp(-n*ell_D). This last boundedness follows
from L719's Euler--Maclaurin estimate applied to g alone:

    log D_n-n*ell_D=log d-[g(0)+g(1)]/2+O(h).

Circle length is uniformly bounded, and the resolvent remains separated
there. Polynomial h factors are absorbed by halving the positive
exponents. This proves (17) for the entire complement; there is no
unbounded contour tail or omitted residue.

On the real local tau segment, (4) implies the operator bound

    |T_h(b)|<=C*||b||,                                (18)

by integration of exp(-tau^2/(20*h)) and cancellation of sqrt(h).
Use (9) and (18) to replace A_n by its m-term amplitude expansion
with error at most C^(m+1)*m!*h^m. For its term b_k, apply (16)
at r=m-k, for each 0<=k<m. The total resulting error is at most

    h^m*sum_(k=0)^(m-1)
                 C_G^(m-k+1)*C_b^(k+1)*(m-k)!*k!
                          <=C^(m+1)*m!*h^m.          (19)

Indeed k!*(m-k)!<=m!, and the number m of terms is at most 2^m.
This bound includes all the individual Gaussian/connector remainders;
it does not exchange an infinite double series with an integral.
Define the finite sums

    a_j(v)=sum_(k=0)^j G_(j-k)(b_k)(v).               (20)

They are independent of m and n, holomorphic on a fixed tube W, and
(7), (9), (16) and the same factorial convolution give (1), on a
compactly contained tube W' still containing the entire I. Equations
(9), (16)--(20), and (15) for the single error E_n prove (2) for
every 1<=m<=epsilon_0*n. All domains were fixed before n or m.

Since d_0=1, b_0=B. The inverse derivative in (10) at zero is
T_w(0,v)=1/sqrt(H(v)); (14) and (20) therefore give exactly (3).
Every factor is nonzero on a larger tube by L719, so compactness gives
its stated positive lower bound. This also checks the orientation
and n^(1/2) normalization independently of an absolute-value limit.

Finally increase C to cover all estimates and shrink epsilon so that
epsilon<=epsilon_0 and C*epsilon<=1/4. At m=floor(epsilon*n), for
n>=2/epsilon, m>=epsilon*n/2 and

    C^(m+1)*m!*n^(-m)<=C*(C*m/n)^m
                         <=C*4^(-m)<=C*exp(-c*n)

with c=epsilon*log(4)/2. This is a consequence of the every-order
estimate, not a substitute for it. It completes the exact covered
inner-kernel target, without integrating against chi or inferring
any signed outer rate. The separate conceptual review is recorded below.

### 5. Separate conceptual audit — 3 November 2026, step 192

**Verdict: accepted for every 1<=m<=epsilon*n on fixed complex tubes.**
The exact invocation-start EXPLORE target and assessment were reused.
L719's entire proof and exact saddle evidence were audited in the same
step before this input was accepted; see its Section 7. The analysis
here uses the already assessed Hitrik--Sjostrand v1 Theorem 2.3.1 and
Morse reduction with their precise hypotheses in Section 1. No new
general calculus is claimed or reproved. This audit is REPRODUCTION
and validates the local specialization, not a signed-rate theorem.

**Product exponentiation.** L719's remainder index converts correctly:
at odd m it starts at h^m; at even m it starts at h^(m+1) and all
retained odd powers are below m. The extra factor (m+1)h is bounded
in the stated range. Enlarging B_0 once controls all coefficients
and all remainders on the same complex tau domain. In (6), for
1<=j<m, j!<=m^(j-1), so each polynomial term is at most 4^(-j)/m.
The exponential is bounded by 2 on the auxiliary disk. Its coefficients
below order m coincide exactly with the formal coefficients; this is
a finite algebraic statement, not convergence of a factorial series.
Cauchy's bound at m=k+1 gives (7), and the Taylor tail at h<=r_m/2
gives (8). The exact exponent is O(h) by the m=1 case, independently
of the truncation order, so comparison of the two exponentials in
(9) has a fixed Lipschitz constant. Only the auxiliary z disk shrinks
with m; the spatial and parameter domains do not.

**Uniform Gaussian geometry.** The resolvent stays separated on the
whole original complex tau disk by L719 Section 7, so B and all b_k
are bounded holomorphic amplitudes there. On a smaller fixed disk the
removable quotient 2*psi/tau^2 stays in the right half-plane. The
single square-root branch and the estimate
|w_tau-sqrt(H)|<|sqrt(H)|/4 give injectivity by integration on a line
segment. On the boundary, w differs from sqrt(H)*tau by at most a
quarter of its modulus, so Rouche gives a common image disk. The
unique inverse is jointly holomorphic; its bounds follow after one
fixed compact shrink. Both a and rho are chosen only after those
domains, independently of n and m.

The lower bound for Re(H) and the upper bound for |H| keep sqrt(H)
in a strict Gaussian sector uniformly even for complex v. Hence the
two image endpoints and their radial/circular connectors have the
claimed positive phase gap. They lie in the inverse disk, as does
the image path. Cauchy's theorem uses holomorphy there, not a favorable
phase everywhere in the intervening region. The connectors need not
vary holomorphically: they only bound the difference of exact contour
integrals. The coefficients use the holomorphic inverse at w=0.
After rescaling by rho, the amplitude is holomorphic on a neighborhood
of the closed unit disk. This verifies the dimension-one hypothesis
of the cited all-order Gaussian theorem, with small parameter h/rho^2.
Its bound and the connector bound yield (16) for every r>=1, with
one constant. An optimal-order statement alone was not used to infer it.

**Normalization and all-order combination.** From the exact contour,

    n^(-1/2) exp(-n*S) p_n
      =1/(2*pi*A*sqrt(h))*integral exp(-psi/h) A_n d tau
         + full complementary error.

The factor i from ds cancels 1/i, and D_n's exponential and endpoint
terms have already been included in S and A_n. The positive/negative
Morse endpoints connect to +rho/-rho, so the Gaussian orientation
is positive. Thus G_0(B) is precisely a_0 in (3), including sqrt(H)
and beta=1/2. The arc between a and 1/10 has a fixed quadratic gap;
the rest of the circle has the 1/5000 gap. Boundedness of
D_n*exp(-n*ell_D) follows from Euler--Maclaurin applied to g alone.
All normalized errors are exponential after absorbing h^(-1/2).

The amplitude-remainder integral is controlled by the real Gaussian
operator norm (18), without multiplying it by another factorial.
For each k<m the Gaussian remainder is taken to order m-k, so its
power is exactly h^m and its factorial product is k!*(m-k)!<=m!.
The m summands and all fixed constants are absorbed into C^(m+1).
The same finite convolution controls every a_j. For any positive c,
exp(-c/h)<=m!*(h/c)^m for all m>=1; this pays the full contour error
at every requested order. Choosing epsilon after C also proves the
optimal exponential bound. No n-dependent tube, infinite-series
interchange, or unproved noncancellation is used.

The elliptic a_0 and factorial remainder therefore constitute an audited
inner-kernel input. They do not control cancellation of
integral chi(v)*p_n(v)dv, even along n=12q+3. A source comparison and
separate argument for that outer problem remain necessary, as do the
other response, complementary spatial defect and actual-Xi assumptions.

## Mathlib

Full matching Mathlib coverage for this exact growing-product kernel
and its uniform factorial expansion has not been checked. No absence
claim is made. Residue/complex-analysis and analytic stationary-phase
inputs are cited mathematical results; this proof claims neither Lean
verification nor a matching general analytic-symbol implementation.
