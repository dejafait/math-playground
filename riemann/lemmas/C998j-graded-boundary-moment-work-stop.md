# C998j: Graded boundary moments — ideal error and direct-work stop

## Hypotheses

Use C998i(3)-(8), including its independent dotted data, both endpoint
brackets and all same-parity modes0..255. Retain C998g Section1/audit674's
square coefficient1/4 and C998a's three real frozen columns, completed by
the EXACT C999q map Z. Their free modes2..255 are the binary rationals in
`free_middle_dyadics` of `scripts/separation-seven/frozen-reference-proposal-652.npz`,
SHA256 `2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6`.
No coefficient is retuned. All original source/core/operator contracts
remain qualified as in these inputs; this square calculation does not
validate them or use an RH sign assumption.

The prior SPECIALIZE assessment682, completed683 and repaired684,
licenses this REPRODUCTION attempt. Import Trefethen, *Approximation
Theory and Approximation Practice*(2013), Chapter19 Theorem19.3/(19.8),
[primary PDF](https://people.math.ethz.ch/~hiptmair/Seminars/RAP_22/TRE13.pdf),
PDFpp153-154, with the inspected proof and point-count convention:
a function holomorphic on a neighborhood of the Bernstein ellipse
E_rho and bounded there by M has (n+1)-point Gauss error at most
(64/15)M*rho^(-2n)/(rho^2-1), n>=1, on[-1,1]. Multiply by half the
interval length after affine scaling. The positive weights integrate
constants exactly. The general theorem is not reproved here; the local
complex bounds and full-entry propagation are the specialization.

Prescribe ONE rule, in the dimensionless coordinate z=s/a:

    eta=2^-84; omit (0,eta);
    [b_j,2b_j], b_j=2^-j, j=1,...,84;
    rho=2, n_j=44+ceil(144*b_j), N_j=n_j+1 Gauss points.       (1)

At every node accumulate all seven undotted and seven dotted moments
for every n=1,...,255, in the dimensionless normalization below.
Share nodes, Gauss weights, the seven weight factors and generation of
the sine/cosine bases. Each moment is a separate sum of its weighted
density samples. No mode transform, endpoint Taylor fill, aggregation
across frequencies or algebraic elimination of these sums is prescribed.
Mode0 is exact zero and incurs no moment evaluations.

For completeness the prospective finite realization is fixed as follows.
This specifies the work that would have to be certified after the
pre-batch test; it is NOT a paid finite-arithmetic claim.

- Use outward interval arithmetic with512 fractional bits, arbitrary
  integer parts, explicit truncation tails and no overflow convention.
  Form the base sin(pi*z/2), cos(pi*z/2) by256 Taylor terms each and
  generate all255 frequencies by their addition recurrences. Subtract1
  only in interval arithmetic. Share the base values across moments.
- Generate Legendre polynomials by the three-term recurrence, as in
  Johansson--Mezzarobba, *Fast and rigorous arbitrary-precision computation
  of Gauss-Legendre quadrature nodes and weights*,
  [arXiv:1802.03948v1](https://arxiv.org/pdf/1802.03948v1), Sections1-3,
  equations(2),(3),(9). Isolate all N simple roots in(-1,1) by exact
  signs on successively halved dyadic meshes; record an exact zero root
  separately. Once disjoint brackets account for all N roots, bisect
  them to width<=2^-640 and refine further if necessary until interval
  evaluation of P_N' excludes zero. Enclose weights by the displayed
  derivative formula2/[(1-x^2)P_N'(x)^2]. Exact rational recurrence/sign
  work and outward conversion are setup costs, never free node oracles.
  No concrete upper setup count is asserted or used here.
- Evaluate real logarithms by powers-of-two reduction to[1,2] and512
  terms of 2*sum u^(2r+1)/(2r+1), u=(x-1)/(x+1), with its positive
  geometric tail. Use the same series for log2 and log3 (u=1/2 for3),
  and512 terms in each arctangent of Machin's formula for pi, with
  alternating-series tails. Integer square roots with exact comparisons
  enclose the normalization factors for Z.
- Evaluate the primitive in C998i(3) using D(x)=-Li_2(-x), x>0. For
  0<x<=1 use D(x)=Li_2(x/(1+x))+(log(1+x))^2/2, with768 terms of
  the Li_2 series and its geometric/n^2 tail. For x>1 use
  D(x)=pi^2/6+(log x)^2/2-D(1/x). These are the principal real cases
  of [DLMF25.12.1-4](https://dlmf.nist.gov/25.12#i), with arguments
  away from the cuts; no complex numerical transformation is needed.
  If an argument interval meets1, split it at1 and take the hull of
  the two valid evaluations. Use C998i's explicit A1,A2,Q formulas
  at real interior nodes, retaining cancellation in interval arithmetic.
  Do not substitute their undefined separated expressions at z=1.
- Complete Z, all C998i entries and all nine real S_ij contractions
  with outward intervals. Stop rather than claim the service if a
  returned enclosure, domain check or remaining work allowance fails.

The series/branch and interval qualifications are those inspected in
source-notes683, including Johansson, *Numerical integration in
arbitrary-precision ball arithmetic*,
[arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942v1), Sections2/2.1,
and the cumulative-error warning in the
[Arb2.23.0 integration contract](https://arblib.org/acb_calc.html).
These sources do not certify the proposed precision, cancellation,
node setup or total finite error. No asymptotic complexity theorem or
library timing is imported as a scalar-work bound.

Count scalar work as in C998g: one real addition, subtraction,
multiplication, division, comparison or assignment counts one. Interval
and complex operations must be expanded into real work. Fused operations
do not identify an addition with a multiplication in this convention.
The lower count below favorably ignores interval overhead altogether.

## Conclusion

In exact arithmetic, with exact constants, nodes, weights and Z, (1)
approximates each COMPLETE square entry S_ij with absolute error

    error(S_ij)<2^-37<7.3e-12<1e-10, i,j=0,1,2.               (2)

Nevertheless the specified direct moment accumulation has at least

    12*255*(2*4002-1)=24489180 scalar operations>20000000.     (3)

This omits two of the fourteen moment sums per mode and every setup,
scalar-function, interval, entry-assembly and contraction cost. Stop
the prescription before those tasks or a batch. The complete numerical
service has NOT been certified, and no S_ij value is evaluated here.
Only this sufficient graded schedule/direct summation is stopped;
neither a necessary integration complexity bound nor a large residual
or sign obstruction follows. Earlier prescription/source stops remain.

This is a standard-method specialization, not a claim of new general
mathematics. It supplies informative negative feasibility evidence for
this square service. Full residual/inverse debt, A-square, both mixed
terms, projection, the full100000000 work budget, signed S3, higher/mixed
signs, C744q/H2, non-neutral coverage and actual-Xi assembly remain open.

## Proof

### 1. Dimensionless entries and exact coefficient contraction

Put omega_n=a*k_n=n*pi/2 and A=2^18. For 1<=n<=255,
0<omega_n<512 and omega_n^2<A, using3<pi<4. Write

    f_n(z)=cos(omega_n*z)-1,
    d_n(z)=-z*sin(omega_n*z)/(2*omega_n).

Let L(z)=log((1+z)/z), let Abar_j(z)=a^j*Aj(a*z), and write
Qbar(z)=Q(a*z). C998i(3) gives the exact identities

    Abar_j(z)=integral_0^1 dt/[(1+t)^j*(t+z)], j=1,2,
    Qbar(z)=integral_0^1 L(t)/(t+z) dt.                       (4)

Define h,p,t,r_0,r_1,r_a,r_b by integrating f_n against, respectively,

    Qbar, Abar_1, Abar_2, 1/z, -1/z^2, 1/(1+z), -1/(1+z)^2. (5)

Define their dotted counterparts by replacing f_n with d_n. Here the
dot is differentiation with respect to omega^2, not lambda=k^2;
the independent moment definitions are what is used numerically.
The exact scale conversion to C998i(4) is

    H=a*h, P=p, T=t/a;
    R(0)=r_0, R'(0)=r_1/a, R(a)=r_a, R'(a)=r_b/a;
    dot H=a^3*dot h, dot P=a^2*dot p, dot T=a*dot t;
    dot R(0)=a^2*dot r_0, dot R'(0)=a*dot r_1,
    dot R(a)=a^2*dot r_a, dot R'(a)=a*dot r_b.              (6)

Indeed ds=a dz, q_n(a*z)=f_n(z), and chi_n(a*z)=a^2*d_n(z).
These substitutions justify every factor in(6).

Put j_0=J/a=2*((log2)^2+D(1)), beta_n=omega_n*sin(n*pi/2),
c_n=1-cos(n*pi/2), alpha_n=sin(n*pi/2)/(2*omega_n), and
gamma_n=sin(n*pi/2)/(2*omega_n)+cos(n*pi/2)/2.
At the endpoint label x=0 use r=r_0,r'=r_1; at x=1 use r=r_a,r'=r_b.
Let w_nm=r'_n*r_m-r_n*r'_m and v_n=r'_n*dot r_n-r_n*dot r'_n,
and Delta mean the value at1 minus the value at0. Writing F_nm=I_nm/a,
C998i(6)-(8) become exactly

    F_00=j_0, F_0m=F_m0=j_0+h_m, m even;
    F_nm=j_0+[Delta w_nm+omega_m^2*h_m-omega_n^2*h_n
              +c_m*t_n+beta_m*p_n-c_n*t_m-beta_n*p_m]
                /(omega_m^2-omega_n^2), 1<=n<m, equal parity;
    F_nn=j_0+Delta v_n+h_n+omega_n^2*dot h_n
              +alpha_n*t_n+gamma_n*p_n-c_n*dot t_n-beta_n*dot p_n.
                                                                  (7)

There is no coincident-frequency division. The four diagonal residue
classes are retained: alpha=0,gamma=1/2,c=beta=0 when n=0 mod4;
alpha=1/(2omega),gamma=1/(2omega),c=1,beta=omega for1 mod4;
alpha=0,gamma=-1/2,c=2,beta=0 for2 mod4; and
alpha=-1/(2omega),gamma=-1/(2omega),c=1,beta=-omega for3 mod4.
In particular the positive0 mod4 class still uses p_n/2.

C998i(2), already including the parity map and coefficient1/4, gives

    B_nm=(a*nu_n*nu_m/2)*F_nm.                              (8)

The multiplier is1/2 if both indices are positive, sqrt(2)/4 if only
one is zero, and1/4 if both are zero. Thus it is always<=1/2;
there is no residual ell-dependent normalization error in the ideal rule.
Opposite parities are separate blocks, not omitted raw mixed integrals.
For the frozen real raw coefficients u_nj, the complete square is

    S_ij=sum_(n,m of equal parity) u_ni*u_mj*B_nm.            (9)

All products and both parities occur. The same absolute estimate would
hold with a conjugated second coefficient for complex columns.

The complete exact free arrays are checked in the certificate below.
Their absolute sums M_j are each<7/3. C999q's exact neutral completion
has0<r_n<1 for all free indices: the odd ratios follow from increasing
k_n^2, and for even n>=2 the ratio is (sqrt(2)/4)/(1/4+k_n^2)<1,
using k_n>10. Thus the completed coefficient sum U_j satisfies

    U_j=sum_(n=0)^255 |u_nj| <=2*M_j<14/3<8.                (10)

No rounded raw vector or sampled amplitude is used for this estimate.

### 2. Entire real strip and complex panel bounds

For0<z<=1 put r=log(1/z). The audited bounds in C998i(3), with log2<1,
give Abar_j(z)<=1+r and Qbar(z)<=2+2r+r^2/2. Also
|f_n(z)|<=omega_n^2*z^2/2 and |d_n(z)|<=z^2/2.
The functions e^(-2r)(1+r) and e^(-2r)(2+2r+r^2/2)
decrease for r>=0; their respective derivatives have factors
-1-2r and -2-3r-r^2, and their values at0 are1 and2.
It follows directly for EVERY weight in(5) that

    |undotted integrand|<=A, |dotted integrand|<=1.           (11)

For the reciprocal weights cancel the available z^2; for1/(1+z)
and its square use1+z>=1. In particular all true undotted moments
have modulus<=A and all true dotted moments<=1. Omitting(0,eta)
therefore costs at most A*eta=2^-66 in each of the fourteen moments.
There is no upper-end omission.

Here is an actual holomorphic neighborhood for applying the source
theorem. The integrals(4) extend to Re(z)>0. On a compact subset of
that half-plane their integrands are dominated by an integrable
multiple of1 or L(t). Locally, expand1/(t+z) about z_0 with radius
less than Re(z_0); the resulting geometric series converges uniformly
relative to these majorants. Integration gives a convergent power
series. This justifies holomorphy, including across z=1, without
using a separated logarithm formula at its removable endpoint.
For x=Re(z)>0, their absolute values are bounded by the same real
integrals at x and these bounds decrease as x increases.

On the ellipse with rho=2 over[b,2b], b=2^-j,

    Re(z)>=7b/8, |z|<=17b/8<3b, |Im(z)|<=3b/8.             (12)

Thus Abar_j is bounded by log(1+8/(7b))<j+2, and Qbar by(j+3)^2:
apply its real bound at7b/8 with r=log(8/(7b))<j+1.
The occurrence of j as a panel index in these inequalities does not
change the two weight indices1,2. The sine/cosine integral formulas
give throughout this ellipse

    |f_n(z)|<=(A/2)|z|^2 exp(192b),
    |d_n(z)|<=|z|^2 exp(192b)/2.                            (13)

For example cos(w)-1=-w^2*integral_0^1(1-t)cos(tw)dt and
sin(w)=w*integral_0^1 cos(tw)dt; use |cos(w)|<=exp(|Im w|).
The reciprocal weights at0 again cancel powers of |z|. The other
denominators have modulus>=1. For the largest remaining estimate use

    b^2*(j+3)^2<=4, j>=1,

whose value at1 is4 and whose successive ratio is
((j+4)/(2j+6))^2<1. Equations(12)-(13) now bound every integrand
in(5), undotted or dotted, by

    M_j=2^23 * 2^(288b).                                  (14)

Indeed the Q prefactor is at most (A/2)*9*4=18A<2^23;
the other six are smaller. Finally exp(192b)<2^(288b) since
log2>2/3. These elementary logarithm bounds follow also from the
positive atanh series for log2; they introduce no numerical oracle.

### 3. Ideal moments and every entry case

By the cited Gauss theorem, (12)-(14) and interval length b, the
error of panel j for any one moment is at most

    (32/45)*b*2^23*2^(288b-2n_j)
       <=(32/45)*b*2^-65.                                 (15)

The degree rule(1) has2n_j>=88+288b. The panels cover[eta,1] and
sum_j b_j=1-eta. Combining (11) and(15), every individual undotted
and dotted moment has ideal error at most

    epsilon=2^-66+(32/45)*(1-2^-84)*2^-65 <2^-64.            (16)

The same bound is valid simultaneously for all255 modes; no independence
of quadrature errors is assumed. Constants j_0,omega,c,beta,alpha,gamma
and the coefficients are exact ONLY at this ideal stage.

If two true undotted values have modulus<=A, the error in their
product is at most2A*epsilon+epsilon^2. Therefore Delta w_nm,
which has two products at each of two endpoints, has error at most
8A*epsilon+4epsilon^2. For distinct positive same-parity indices,
omega_m^2-omega_n^2>=2*pi^2>18>1. The remaining numerator errors
in(7) are bounded by(2A+1028)*epsilon: two omega^2 terms, two
coefficients |c|<=2 and two |beta|<512. Consequently

    error(F_nm) <=(10A+1028+4epsilon)*epsilon<2^22*epsilon.  (17)

This deliberately discards the further saving from division by>18.
It covers every off-diagonal residue combination.

For a product of one undotted value and one dotted value, the true
moduli are<=A and<=1, so its error is at most
(A+1)*epsilon+epsilon^2. Thus Delta v_n has error at most
4(A+1)*epsilon+4epsilon^2. Since |alpha|<=1,|gamma|<=1,
|c|<=2,|beta|<512, the six remaining moment terms in the diagonal
formula cost at most(A+517)*epsilon. It follows that

    error(F_nn) <=(5A+521+4epsilon)*epsilon<2^22*epsilon.    (18)

This includes omega_n^2*dot h_n and all four residue classes,
including their nonzero gamma term when n=0 mod4. Both endpoints
of v_n have been counted. The zero-mode formula has error at most
epsilon (zero for F_00); no dotted zero mode is invoked.

Equations(8),(17),(18) give a uniform error bound2^21*epsilon
for normalized B_nm. Applying(9),(10) without assuming coefficient
cancellation yields

    error(S_ij) <= U_i*U_j*2^21*epsilon
                 <2^27*2^-64=2^-37.                       (19)

This proves(2) for the whole ideal contraction, not merely a moment
or unnormalized basis entry. All nine sharper rational upper bounds
using U_j<=2M_j are saved in the certificate. None pays finite
primitive, node, coefficient or rounding uncertainty.

### 4. Mandatory work and stopping scope

The exact integer point count from(1) is4002:
sum_j N_j=84*45+sum_j ceil(144/2^j)=3780+222.
The first seven ceilings are72,36,18,9,5,3,2; the remaining77 equal1.

Count only the seven undotted sums and the dotted h plus four dotted
endpoint sums, for each of255 positive frequencies. Even giving the
two other dotted sums away, there are3060 directly accumulated sums.
Each takes4002 weighted-density products and at least4001 additions;
allow its first product to initialize the sum without charging an
assignment. All common weights and density samples are given free
for this favorable count. It follows that

    products=12246120, additions=12243060,
    total=24489180>20000000.                               (20)

Charging all fourteen prescribed sums alone would give28570710.
The inequalities do not charge node/root setup, elementary functions,
primitive cancellation, interval arithmetic, initialization, constants,
Z, moment-to-entry assembly or the final contractions. Counting these
cannot repair(20). Therefore the pre-batch test fails independently
of whether the proposed512-bit implementation could pay the remaining
error allowance. No such setup, large batch or precision proof is run.

The prescription enforces direct accumulation; algebraic aggregation,
analytic evaluation of some sums or different endpoint rules would be
different methods. Thus(20) is NOT a lower bound for all realizations
of C998i. The count differs materially from C998g's stopped tensor
evaluation, but both are preserved. A shared analytic endpoint-moment
method is only a future source-review nomination, not proved here.

### 5. Exact finite evidence and limitations

Reproduce the planning arithmetic from the notebook directory:

    python3 scripts/separation-seven/boundary-moment-feasibility-685.py

The complete certificate is
`scripts/separation-seven/boundary-moment-feasibility-685.json`.
It checks the full archive hash; reads all762 free binary64 values
as exact rational numbers; records every coefficient and absolute
sum; checks all84 panel endpoints, degrees and error inequalities;
propagates the error to all nine ideal entries; and records the exact
mandatory work. All finite planning checks pass. Its service-failure
field explicitly records the budget failure and unpaid finite error.
This is a planning certificate, not a certificate of evaluated S_ij.

The uniform continuous inequalities are proved above, not inferred
from sampled weights or numerical agreement. Source and upstream
operator hypotheses are retained rather than silently revalidated.
There is no positivity, inverse bound or RH conclusion, and the
20-million service remains open for materially different methods.

## Mathlib

A full matching theorem for this fixed moment prescription, its complete
error propagation and cost has not been checked. Supporting integration,
power-series and finite-sum results would not alone formalize this
conclusion. Unknown full coverage is not evidence of absence. The
precise Trefethen citation supplies the general quadrature result;
the primitive/arithmetic/node citations only specify the prospective
unexecuted realization. Local progress is a qualified prescription
stop and ideal-arithmetic bound, not progress beyond these general
numerical-analysis sources or a new RH result.
