# Lemma 702: a signed interior remainder obstructs the full-circle endpoint extension

## Hypotheses

Use L666's exact family, with

    d=5/4, x=-d, R=11/8, U=121/64, A=27/10, Y=9/20,
    n=12q+3, q>=1, M=n/3, h=A/n, t_j=j/n (0<=j<n),
    a_m=x+i*h*(m+1/2+e_m),             -2q<=m<2q,
    c_n(u)=R^(-1)*[1+sum_(-2q<=m<2q) W_(a_m)(u)].

Every W is the full product in L666 (6), including j=0 and the
inverse denominator angle. All masses are one; the anchor is fixed.
All M spatial moments remain in the downstream polynomial G.

The profile is one exact prescribed-center Picard solution from L696,
with L694's real cutoffs and constants selected before n. Write

    r<=1/8,       sup_m |e_m|<=r,       E=sum_m |e_m|<infinity.

For the signed lower bound assume the additional quantitative condition

    r*E <= 1/(16*pi^2).                                      (1)

Part of the conclusion is that this condition is attainable within
L696's construction. It is not assumed for every previously selected
profile. In choosing a profile, an already valid constant in Lev's
coefficient estimate may be enlarged before L694's r and L696's gap
width are fixed. No choice is allowed to depend on n.

Define the exact outer-band contribution and its absolute envelope by

    O_n={m: -2q<=m<2q, |h*(m+1/2+e_m)|>=2/5},
    E_n(u)=R^(-1)*sum_(m in O_n) W_(a_m)(u),
    B_n=R^(-1)*sum_(m in O_n) |W_(a_m)(-1)|,
    I_n(u)=c_n(u)-E_n(u).

Thus I_n retains the anchor and every remaining interior node. This is
an exact decomposition of the original scalar, not a changed family.

## Conclusion

There exists a fixed L696 profile with positive centered gap satisfying
(1). For every such profile there is an onset, allowed to depend on
that fixed profile, after which

    |c_n(-1)| >= 3/(4*R),
    0<B_n <= n/(3*R)*exp(-kappa*n),       kappa=16/6413,
    |I_n(-1)| >= 1/(2*R),
    |I_n(-1)|/B_n >= (3/(2*n))*exp(kappa*n).                 (2)

The upper bound for B_n holds for all permitted n. Positivity and
inclusion of both actual outermost nodes hold for n>=63.

Consequently a full-circle expansion which retains these endpoint
bands and discards the signed interior as a relative o(1) error is
false for this admissible fixed-profile class. Even the larger outer
bands are exponentially smaller than the omitted signed remainder at
u=-1. An endpoint expression that is exponentially small there cannot
approximate c_n with an o(1) absolute error. This rejects that direct
extension of L701's endpoint method; it does not reject expansions
which also estimate the signed interior and transition terms.

This is a method obstruction, not a scalar logarithmic-rate estimate.
A lower modulus at one angular point gives no lower bound for the
full angular logarithmic mean or its numerator-zero charge. The
existential scalar target, other Picard choices without (1), angular
transition integrals, H/support and Xi transfer remain open. There is
no RH candidate. The separate conceptual audit in Section 7 accepts
this restricted obstruction; the bounded prior search does not certify
originality or a stronger scalar conclusion.

## Proof

### 1. Scope and existing inputs

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-centered-gap-scalar-complete-log-lower.md`.
The attempt tests its exact scalar target by a signed finite-endpoint
expansion, stopping when the remainder cannot be paid. L701's
interior-disk endpoint limit is motivation, not an asymptotic premise
on the unit circle. L699's conditional signs and charge payment and
the stopped common-sign, absolute-tail and microscopic-pairing
mechanisms are not used.

Use L666 for the exact rational family. L690 (1), with common shift
zero, supplies its audited unshifted scalar limit as explained in
Section 3. L694 supplies the exact Picard equation and two-norm
convergence, and L696 supplies the prescribed-center construction.
Their coefficient input is N. Lev, *An example concerning Fourier
analytic criteria for translational tiling*, Rev. Mat. Iberoam. 38
(2022), 1975--1991, Lemma 4.3, p.1984, equation (4.6), and the
construction in Sections 4.5--4.10, especially Theorem 4.8
([DOI 10.4171/RMI/1318](https://doi.org/10.4171/RMI/1318),
[arXiv:2007.09930v3, Sections 4.3--4.10](https://arxiv.org/html/2007.09930v3#S4.SS3)).
Absolute summability and the prescribed center are the local L694/L696
specializations, not conclusions silently attributed to Lev's theorem.
No Picard existence theorem or contour theorem is reproved here.

The necessary additional applicability argument is a uniform Wiener
bound for the scaled prescribed data, allowing (1) to be selected.
The subsequent signed finite-family limit and endpoint comparison are
written out; they do not follow from qualitative gap existence alone.

### 2. An admissible profile satisfying the smallness condition

Fix Phi, eta and Psi as in L694, independently of a valid coefficient
constant C_0. Write a=1/8, b=3/8, K=sum_(j in Z)(1+j^2)^(-1),
and M_Psi=max(1,||Psi||infinity). The center c_*=omega_*/(2*pi)
is L696's fixed center in (a,b). For any C>=C_0 the same coefficient
inequality remains valid. Apply the unchanged construction with

    r=min(1/8,1/(4*C*K)),
    w=min((c_*-a)/2,(b-c_*)/2,r/(8*M_Psi)),
    chi_w(t)=eta((t-c_*)/w)+eta((t+c_*)/w),
    Q_w(t)=phi(t)*chi_w(t),       phi(t)=-exp(-pi*i*t)/(2*pi*i*t).

The formula for phi is used on the two support bands only. The full
Q_w is smoothly extended by zero and periodically, as in L696.
In particular its support avoids (-a,a). For every such width,
||Q_w||Y<=4*M_Psi*w<=r/2. L694 therefore applies to these exact data.

We need a bound independent of w for ||Q_w||A, not merely the
finiteness proved for each w in L694. Let B_j be bounds for |phi^(j)|
on [-b,-a] union [a,b], j=0,1,2. Put

    A_0=2*B_0*||eta||L1,
    A_2=2*(B_2*||eta||L1+2*B_1*||eta'||L1+B_0*||eta''||L1).

Since 0<w<=1, scaling and the product rule give

    ||Q_w||L1<=A_0*w,       ||Q_w''||L1<=A_2/w.

Two integrations by parts, with no boundary terms for the smooth
periodic extension, yield for k!=0

    |Q_w-hat(k)|<=min(A_0*w,A_2/(4*pi^2*w*k^2)).

The first bound also holds for k=0. With N=ceil(1/w), the modes
|k|<=N contribute at most (2N+1)*A_0*w<=5*A_0. The remaining
ones contribute at most

    A_2/(2*pi^2*w)*sum_(k>N) k^(-2)
       <=A_2/(2*pi^2*w*N)<=A_2/(2*pi^2).

Thus the fixed number

    B=5*A_0+A_2/(2*pi^2)>0

bounds ||Q_w||A for every permitted w. It depends on the fixed
cutoffs and center, not C, r, w or n. L694 (9), with C*K*r<=1/4,
now gives for this same Picard limit

    E<=||Q_w||A/(1-C*K*r)<=4*B/3.

Choose the valid constant C sufficiently large that
r<=3/(64*pi^2*B). This is possible since 1/(4*C*K) tends to zero.
Then r*E<=1/(16*pi^2). Fix this C and all its data once and for
all. L696 supplies the real l1 sequence, cap r and positive centered
gap g=pi*w. No second fixed point or limit of profiles is substituted,
and w is not sent to zero as n varies. This proves attainability of (1).

### 3. Exact signed limit at the negative angular point

For real y, direct substitution u=-1 in L666 (6), including j=0,
gives

    W_(x+i*y)(-1)=product_(j=0)^(n-1)
                      (1+i*alpha(t_j)*y)/(1-i*beta(t_j)*y),
    alpha(t)=t/(U-d*t),       beta(t)=1/(d-t).                 (3)

For 0<=t<=1 both denominators defining alpha,beta are positive, and

    beta-alpha=(U-2*d*t+t^2)/[(d-t)*(U-d*t)]>0.

Indeed the numerator decreases on [0,1] and its minimum is
U-2*d+1=25/64. Consequently |W_(x+i*y)(-1)|<=1 for every real y,
not just the ordinates present in the finite family.

Put F_n(s)=W_(x+i*A*s/n)(-1) for real s. Here alpha<=64/41 and
beta<=4. Logarithmic differentiation, with no zero factors on the
real s axis, gives

    F_n'(s)=i*(A/n)*F_n(s)*sum_j
       [alpha(t_j)/(1+i*A*alpha(t_j)*s/n)
          +beta(t_j)/(1-i*A*beta(t_j)*s/n)],
    |F_n'(s)|<=A*(64/41+4)=3078/205<16.                    (4)

For s in any fixed compact real interval, each logarithm in (3)
has its Taylor expansion at 1 with quadratic error O(s^2/n^2),
uniformly in j. Summing n errors gives O(s^2/n). The linear terms
are a Riemann sum of the smooth function alpha+beta, so

    F_n(s) -> exp(i*Omega*s),
    Omega=A*integral_0^1 [alpha(t)+beta(t)]dt
          =A*[log(5)-4/5+(121/100)*log(121/41)].              (5)

This convergence is uniform on each such compact interval. It makes
no assertion at a moving index m of size n.

Let c_n^0 be the unshifted finite scalar. L690 (1), with alpha=0
in that lemma's common-displacement notation, applies to the full G.
Taking its constant coefficient by integration in the spatial circle
variable gives

    |c_n^0(u)-1/R|<=n^2*exp(22-n/500),       |u|=1.           (6)

This coefficient extraction retains the entire spatial polynomial;
it is not deletion of the higher moments. It imports the established
finite unshifted contour estimate, not an informal infinite comb sum.

For fixed m, (5) gives the limit of
F_n(m+1/2+e_m)-F_n(m+1/2). By (4) its modulus is at most
16*|e_m| for every n. Extend that difference by zero outside
-2q<=m<2q. Each fixed m is eventually included, and the majorant
is summable. Passing to the limit first on a fixed finite set and
then bounding both complementary tails proves

    R*c_n(-1) -> H:=1+Delta,
    Delta=sum_(m in Z) exp(i*Omega*(m+1/2))
                                      *(exp(i*Omega*e_m)-1).  (7)

The series in (7) converges absolutely. This argument uses (6) for
the undisplaced sum and dominated convergence only for its l1
difference; no absolutely convergent undisplaced exponential comb
is being asserted.

### 4. The exact Picard equation bounds the signed correction

The strict frequency bounds needed below are

    11/2<Omega<6<2*pi,       tau=Omega/(2*pi)-1 in (-1/8,0).  (8)

Here the last lower bound uses pi<22/7, since 7*pi/4<11/2.
These inequalities can be verified entirely by rational arithmetic:
for 0<z<1 put

    S_N(z)=2*sum_(k=0)^(N-1) z^(2*k+1)/(2*k+1),
    T_N(z)=2*z^(2*N+1)/[(2*N+1)*(1-z^2)].

Integrating the geometric series for 2/(1-z^2) gives
S_N(z)<log((1+z)/(1-z))<S_N(z)+T_N(z). Use N=12,
z=2/3 for log 5, and z=40/81 for log(121/41) in (5).
The resulting rational lower bound for Omega exceeds 11/2 and
the upper bound is below 6. Section 6 records the complete certificate.

Let T be the exact continuous Wiener-algebra limit in L694. Its
Fourier coefficients are e_m, and T+R(e)=Q_w pointwise. At tau in
(8), Q_w(tau)=0 and Phi(tau)=1, since the prescription is supported
in the two annuli outside (-1/8,1/8). Set v=2*pi*tau=Omega-2*pi<0,
and, for a real parameter z, define the absolutely convergent series

    N(z)=sum_m exp(i*v*m)*(exp(i*z*e_m)-1-i*z*e_m).

The elementary real Taylor bound |exp(i*z*e)-1-i*z*e|<=z^2*e^2/2
gives

    |N(z)|<=z^2/2 * sum_m e_m^2,
    sum_m e_m^2<=r*E.                                     (9)

By the exact definition of R in L694, at tau the Picard equation is

    T(tau)=-N(v)/(i*v).

There is no division by zero since v<0. Also exp(i*Omega*m)=exp(i*v*m)
for integer m. Splitting the absolutely convergent series (7) into
its linear part and (9) therefore gives the signed identity

    Delta=exp(i*Omega/2)*[N(Omega)-(Omega/v)*N(v)].          (10)

This uses the actual fixed-point equation at the aliased frequency,
not a hypothesized gap or complex-frequency continuation there.
As |v|=2*pi-Omega, (9)--(10) imply

    |Delta|<=Omega*(Omega+|v|)/2 * sum_m e_m^2
            =pi*Omega*sum_m e_m^2
            <2*pi^2*r*E<=1/8.                            (11)

Thus |H|>=7/8. By (7), eventually |R*c_n(-1)|>=3/4. This
proves the first part of (2). No effective or profile-uniform onset
is claimed for the l1 dominated limit.

### 5. All endpoint-band terms decay, while the signed interior survives

For 0<=t<=1 the bounds already used in Section 3 imply

    beta-alpha >= (25/64)/(d*U)=20/121,
    beta+alpha >= beta >=4/5,
    beta^2-alpha^2 >=16/121.

For 2/5<=|y|<=Y, one also has 1+beta^2*y^2<=1+16*Y^2=106/25.
The squared modulus of each exact factor in (3) is consequently

    (1+alpha^2*y^2)/(1+beta^2*y^2)
       =1-(beta^2-alpha^2)*y^2/(1+beta^2*y^2)
       <=1-32/6413.

Using log(1-z)<=-z and keeping all n factors gives

    |W_(x+i*y)(-1)|<=exp(-16*n/6413).                       (12)

Every available ordinate has modulus less than Y by the original
cap. The positive outermost ordinate is exactly

    y_+=Y-A/n+A*e_(2q-1)/n >= Y-9*A/(8*n).

The negative outermost ordinate has absolute value
Y-A/n-A*e_(-2q)/n with the same lower bound. For n>=63 this
lower bound is at least 45/112>2/5. Hence both outermost nodes
belong to O_n. Their factors at -1 are nonzero, so B_n>0.
There are at most M-1<n/3 nodes in O_n. Summing (12) proves
the stated bound for B_n, including the case O_n is empty at a
smaller n. It also gives |E_n(-1)|<=B_n.

For sufficiently large n this upper bound is at most 1/(4*R).
Combine it with the first part of (2) to obtain

    |I_n(-1)|=|c_n(-1)-E_n(-1)|>=1/(2*R).

Dividing by the positive B_n and using its full upper bound proves
the last inequality in (2). The normalized omitted signed remainder
therefore has a positive exponential rate, at least 16/6413.
This is the first failed requirement of the proposed global endpoint
extension; no scalar Jensen or charge conclusion is drawn from it.

### 6. Exact checks and verification limits

Run from the active notebook:

    python3 scripts/one-sided-hankel/centered-gap-global-endpoint-138.py

The complete exact-arithmetic certificate is
`scripts/one-sided-hankel/centered-gap-global-endpoint-138.json`.
All 12 rational checks pass, with no failures. They include the full
12-term logarithmic bounds and their tails, (8), the derivative bound
3078/205<16, the product rate 16/6413 and the actual finite-endpoint
lower bound 45/112>2/5 at n=63. The rational enclosure for Omega
is approximately (5.721075554296,5.721090959155), strictly inside
the required (5.5,6); the stored rational endpoints, not rounded
decimals, are used in the comparisons.

These checks verify constants only. The width-uniform Fourier bound,
fixed-profile selection, dominated signed limit and use of the exact
Picard equation are analytic arguments above, not numerical evidence
from a finite approximation to the profile. Section 7 records the
subsequent analytic audit and complete exact replay.

### 7. Separate conceptual audit — 3 November 2026, step 140

The unchanged invocation-start EXPLORE assessment was
`drafts/literature/2026-11-03-centered-gap-global-endpoint-audit-scope.md`.
Its primary-source comparison and the earlier L694/L696 audits are
reused. This audit checks the full argument above against L666 (6),
L690 (1) at common shift zero, L694 (2)--(9) and L696 Section 2.
It does not re-audit their source manuscripts or import a new general
theorem. The scalar-charge, common-sign, bulk-pairing and absolute-tail
stops remain scoped comparisons, not mathematical premises.

**Parameter selection and actual reflected data.** On both support
bands, Psi(-t)=1/(2*pi*i*t) and chi_w(-t)=chi_w(t). Thus the actual
L696 prescription is exactly

    Q_w(t)=Psi(-t)*[-exp(-pi*i*t)*chi_w(-t)]
          =-exp(-pi*i*t)*chi_w(t)/(2*pi*i*t).

The support lies strictly inside the fixed annuli, so this expression
has no singularity there, vanishes near the periodic boundary and has
the required Hermitian symmetry. The constants B_j bound a fixed
smooth function on fixed compact annuli. Neither they nor A_0,A_2,B
depend on C, r or w. For each bump the three contributions to the
second-derivative L1 norm are bounded by

    B_2*w*||eta||L1 + 2*B_1*||eta'||L1 + B_0*w^(-1)*||eta''||L1.

There are two bumps; w<=1 gives precisely A_2/w. With N=ceil(1/w),
(2N+1)w<=2+3w<=5 and sum_(k>N) k^(-2)<=1/N. These check both
frequency tails and the zero mode in the asserted uniform A bound.
Reflection does not alter the coefficient-sup bound 4*M_Psi*w<=r/2.
One may therefore enlarge a valid C, choose the stated r and positive
w, and apply L694 to this same Q_w. Its same-limit bound E<=4B/3
then verifies (1), without circular dependence on w or an assumed
small weighted-data norm. All these choices precede n. Q_w is nonzero
on a plateau, so its fixed point is not the zero sequence. This is
existence of a selectable profile, not a claim about all old choices.

**Exact finite baseline and the signed limit.** Dividing the actual
L666 factors at u=-1 gives

    [(x+t)/(x+t+i*y)] * [(U+t*x+i*t*y)/(U+t*x)],

which is (3), including the t=0 factor 1/(1-i*y/d). Both real
denominators in alpha,beta are positive; U-2*d*t+t^2 decreases to
25/64 on [0,1]. Thus the global real-s modulus and derivative bounds
used for domination hold, not just bounds at the finite nodes. The
two integrals in (5) are log 5 and
(U/d^2)*log(U/(U-d))-1/d, with U/d^2=121/100. Taylor expansion
on a fixed s-compact set pays n errors of size O(n^(-2)); only then
is the Riemann sum limit taken.

For the undisplaced finite family, integrating L690 (1) over the
spatial circle removes every positive spatial power exactly. The
anchor polynomial has constant coefficient 1/R, so (6) retains the
same bound and normalization. For the displacement difference, the
real mean-value estimate gives 16*|e_m|, even at large moving indices.
On a fixed finite index set the summands converge by (5); outside it
both the finite sums and their limiting series have arbitrarily small
tails bounded by 16*sum |e_m|. Every fixed index is eventually included.
This verifies (7) for the fixed profile and the actual two endpoints.
It never assigns an ordinary sum to the undisplaced oscillatory comb.

**Continuous alias identity and strict lower bound.** The rational
logarithm bounds below put 7*pi/4<Omega<2*pi, using 3<pi<22/7.
Consequently tau is strictly in (-1/8,0), where Q_w=0 and Phi=1.
The A limit in L694 is continuous and has the absolutely convergent
Fourier series T(tau)=sum_m e_m*exp(i*v*m). Its nonlinear series
also converges absolutely at this point by sum e_m^2<=r*E. Hence
the exact equation reads T(tau)+N(v)/(i*v)=0, with v nonzero.
Since exp(i*Omega*m)=exp(i*v*m), the linear part of Delta is
i*Omega*T(tau)*exp(i*Omega/2). This gives the minus sign and the
factor Omega/v in (10). The real exponential Taylor remainder follows
by integrating its second derivative and is at most z^2*e_m^2/2.
Since Omega+|v|=2*pi, it yields (11) and |H|>=7/8. Convergence
in (7) pays an eventual error at most 1/8, giving |R*c_n(-1)|>=3/4.
No uniform onset or complex-frequency identity is needed.

**Entire outer bands and actual endpoints.** The denominator product
in beta-alpha is at most d*U. Multiplying its resulting lower bound
20/121 by beta+alpha>=4/5 gives 16/121. With |y|>=2/5 and
|y|<=Y, the squared factor loss is at least 32/6413. Taking a square
root after all n factors gives exp(-16*n/6413), including j=0.
For the positive endpoint m=2q-1 and negative endpoint m=-2q, the
identity 2q-1/2=n/6-1 gives the two distinct signed formulas in
Section 5. Both absolute values are at least Y-9*A/(8*n), which is
45/112 at n=63 and increases with n. Its margin above 2/5 is 1/560.
Every node has |y|<=Y-7*A/(8*n)<Y. The endpoint terms are nonzero,
and there are at most 4q=n/3-1 outer terms. Thus positivity is
valid from n=63, while the upper bound is valid for every permitted n.
The eventual envelope bound B_n<=1/(4R) then gives the stated signed
interior lower bound and ratio by the triangle inequality. No hidden
sign assumption on the outer sum is used.

**Complete arithmetic evidence and result.** The entire step-138
generator, both complete logarithm records, both exact Omega bounds,
all twelve actual/required comparisons, failures and aggregate result
were inspected. The positive logarithm tails are strict because their
later denominators exceed the first omitted denominator; N=12 and
both rational z are in (0,1). Rounded output is not a proof operand.
The replay preserves the original certificate and is byte-identical.
A separate recurrence assembles all 24 series terms, both tail bounds
and every comparison from the defining constants, using the same
Fraction arithmetic backend. This is not an independent backend.

    python3 scripts/one-sided-hankel/centered-gap-global-endpoint-audit-140.py

Full artifacts are
`scripts/one-sided-hankel/centered-gap-global-endpoint-replay-140.json`
and `scripts/one-sided-hankel/centered-gap-global-endpoint-audit-140.json`.
All twelve original comparisons and twelve audit checks pass, with
no failures. The analytic checks above, rather than the certificate,
validate the profile selection and limits. No substantive error,
new theorem, strengthened conclusion or added mathematical input was
found. The audit accepts this restricted method obstruction and retires
the tested endpoint-only extension. Angular means, charge payment,
other profile choices, H/support and Xi realization remain unresolved.

## Mathlib

Full matching coverage for this fixed-profile signed limit and endpoint
obstruction has not been checked. No absence claim or formal
verification is made. The elementary Fourier integration-by-parts,
dominated-series and real Taylor facts are proved in the applicability
argument; L694/L696 retain their original source and Mathlib
qualifications. The scalar logarithmic root formula is not used to
infer any new zero-charge bound here.
