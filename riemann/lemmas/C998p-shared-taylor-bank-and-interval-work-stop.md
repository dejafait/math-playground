# C998p: Shared Taylor bank and endpoint-interval work stop

## Hypotheses

Use C998i/audit682 for modes0..255 of equal parity, its independent
dotted data, BOTH endpoint brackets and coefficient1/4. Use C998a(4)
and C999q's EXACT neutral completion Z for the three frozen real columns.
The free modes2..255 are the binary rationals in `free_middle_dyadics`
of `scripts/separation-seven/frozen-reference-proposal-652.npz`, SHA256
`2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6`.
No coefficient is retuned. Original source/core/operator contracts are
retained, not revalidated here. This is a square-only service test.

The prior SPECIALIZE assessment685/comparison686 covers this REPRODUCTION
attempt. Its fixed prescription is recorded before the calculation in
`drafts/2026-11-13-shared-taylor-bank-working-696.md`. Put b=1/8, K=192.
Use128 Taylor terms (powers2..256) on[0,b] with the seven scaled power
banks constructed below. On[1/2,1],[1/4,1/2],[1/8,1/4], respectively,
use117,81,63 Gauss points and rho=2. C998o/audit695 supplies all261
node/weight enclosures, separately of radius<=2^-512, at scalar cost
3290939. Its exact-real model and exclusions remain in force.

The prospective service uses exact rational endpoint intervals; their
widths come from analytic tails and input uncertainty, not an assumed
finite-machine rounding guarantee. Each arithmetic operation and its
destination assignment cost two; comparisons cost one and division
guards are additional. Wire/address storage and rational bit complexity
are outside this scalar model, exactly as in C998o.

At each interior node use the explicit Q formula in C998i(3), with three
separate D calls and the shared logs log(z),log(1+z),log(1-z). Each
real log uses512 atanh terms after powers-of-two reduction. Each D
uses real inversion/Landen to a Li_2 argument<=1/2 and768 Li_2 terms.
Each polynomial is evaluated by two scalar endpoint Horner evaluations:
767 multiply-add stages for the Li_2 polynomial before its leading
factor,511 for the atanh polynomial in u^2 before its leading factor.
All coefficient, branch, reduction and tail operations must also be
paid in a full service. No consolidation of the three D calls or of
these three elementary logs is part of this prescription.

Each of the fourteen moment families for each positive mode is a
separate interval sum. On the interior it accumulates its261 products;
on the endpoint it accumulates128 coefficient-times-bank products.
Even a known-sign product forms its two endpoint products, then adds
them to the two running endpoints. The first term may initialize its
sum. Sign uncertainty can require more work. Common weights, nodes and
bank values are shared; midpoint/radius aggregation of whole sums and
coefficient contraction before moment evaluation are not prescribed.

Imported general mathematics, already inspected in source-notes683/686:

- Conrad, *The Remainder in Taylor Series*, Theorems1.1/1.2, pp1-4,
  [author PDF](https://kconrad.math.uconn.edu/blurbs/analysis/TaylorRemainder.pdf):
  real Taylor remainder with a derivative bound. Sine and cosine are
  smooth on every interval here and their real derivatives have modulus
  <=1. The local weighted and dotted specializations are proved below.
- NIST DLMF [4.6.1-7](https://dlmf.nist.gov/4.6) and
  [4.19.1-2](https://dlmf.nist.gov/4.19): logarithm/geometric and
  trigonometric series on their stated domains. Endpoint weight series
  here have |z|<=1/8; log(z) is kept explicitly for z>0.
- Maximon, *The dilogarithm function for complex argument*, Proc.R.Soc.
  Lond.A459(2003),2807-2819, Sections2-3(a)(i), equations(2.1)-(3.10),
  [primary PDF](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=150847),
  especially inversion(3.2) and Landen(3.4); also
  [DLMF25.12.1-4](https://dlmf.nist.gov/25.12#i).
  Apply inversion to negative real -z,-1/z, and Landen to -x,x>0.
  These avoid the excluded cuts. In particular
  D(1/z)=pi^2/6+log(z)^2/2-D(z), D(1)=pi^2/12 and
  D(1)=Li_2(1/2)+(log2)^2/2. No branch continuation is assumed.
- Trefethen, *Approximation Theory and Approximation Practice*(2013),
  Chapter19 Theorem19.3/(19.8), PDFpp153-154,
  [primary PDF](https://people.math.ethz.ch/~hiptmair/Seminars/RAP_22/TRE13.pdf):
  for a function holomorphic on a neighborhood of E_rho and bounded
  there by M, the(n+1)-point Gauss error on[-1,1] is at most
  (64/15)M*rho^(-2n)/(rho^2-1). Affine scaling and actual domains
  are checked below. C998o supplies the separately certified node setup.

The general theorems are not reproved. C998j's ideal estimates are
comparison evidence, not certified inputs; the needed bounds and
contraction are checked again. No new literature comparison is claimed.

## Conclusion

The finite rational formulas below specify a common bank for all128
even powers and seven weights, with each bank error<2^-570. The two
reciprocal banks are exact. These are analytic formula/error guarantees;
the bank values have NOT been numerically evaluated in this attempt.

With exact frequency coefficients and exact interior Gauss nodes,
weights and primitive values, using those finite bank formulas gives
endpoint moment error<2^-149, complete moment error<2^-64 and

    |S_ij - S_ij,ideal| < 2^-37 < 1e-10, i,j=0,1,2.       (1)

This accounts for all fourteen families, both W/V endpoints, every
positive diagonal residue class, mode zero and the unchanged exact-Z
contraction. It is an IDEAL-interior bound, not a complete numerical
service or an enclosure of an evaluated S_ij.

The prescribed endpoint-interval implementation nevertheless requires

    mandatory scalar work >=22199915 >20000000,           (2)

even giving three midpoint nodes and every omitted task in Section6
away. Stop before the full bank/quadrature batch. Node setup is now
paid, but its success does not pay the full service. Finite interior,
primitive, density-coefficient and Z uncertainties remain unpaid.
This is a qualified stop of one implementation, not a necessary
complexity bound for shared moments or an obstruction to RH.

Local progress is a reusable finite bank formula and new implementation
failure evidence using known numerical methods. No novelty beyond the
checked sources, signed S3 comparison or RH candidate is claimed.
Independent conceptual audit698 in Section8 upholds these scoped claims
without a changed formula, prescription or bound.

## Proof

### 1. Dimensionless data and convergent bank integrals

Put a=ell/2, omega_n=a*k_n=n*pi/2 and A=2^18. For1<=n<=255,
1<omega_n<512 and omega_n^2<A, using3<pi<4. Set

    f_n(z)=cos(omega_n*z)-1,
    d_n(z)=-z*sin(omega_n*z)/(2omega_n).

Writing r=log(1/z), c=log2, define the seven weights in their order:

    w=(Qbar,Abar1,Abar2,1/z,-1/z^2,1/(1+z),-1/(1+z)^2),
    Abar_j(z)=integral_0^1 dt/[(1+t)^j(t+z)],
    Qbar(z)=integral_0^1 log((1+t)/t)/(t+z) dt.             (3)

These identities and bounds are C998i's audited shared weights:

    0<Abar_j<=1+r, 0<Qbar<=2+2r+r^2/2, 0<z<=1.           (4)

The seven f_n moments are h,p,t,r_0,r_1,r_a,r_b; replacing f_n
by d_n defines the seven dotted moments (derivative in omega^2).
For p even,2<=p<=256, the scaled bank is

    M_(w,p)=integral_0^b (z/b)^p w(z) dz.                 (5)

All seven integrals converge. The worst reciprocal is z^(p-2),
whose exponent is>=0; the other weights have at most log^2 growth.
In particular no divergent zeroth reciprocal moment is introduced.
For j>=-2 with p+j+1>0, direct integration gives

    integral_0^b (z/b)^p z^j dz = b^(j+1)/(p+j+1),
    integral_0^b (z/b)^p z^j r dz
      =b^(j+1)[L/(p+j+1)+1/(p+j+1)^2],
    integral_0^b (z/b)^p z^j r^2 dz
      =b^(j+1)[L^2/(p+j+1)+2L/(p+j+1)^2+2/(p+j+1)^3],   (6)

where L=log(1/b)=3c. These follow by integration by parts twice;
the boundary terms z^alpha log(z)^k vanish for alpha>0,k<=2,
as seen by z=e^-u. Thus all finite formulas below require only
rational arithmetic and c,D(1), without an endpoint limit oracle.

### 2. A finite expansion of the primitive and all weights

Define finite polynomials

    S_K(z)=sum_(j=1)^K (-1)^(j+1) z^j/j,
    D_K(z)=sum_(j=1)^K (-1)^(j+1) z^j/j^2,
    G_K(z)=sum_(j=0)^(K-1) z^j,
    E_K(z)=sum_(j=0)^(K-1) (-z)^j,
    A1_K=(r+S_K-c)G_K, A2_K=(A1_K-1/2)G_K.              (7)

For the Q bank, first set F(z)=integral_0^1 log(1+t)/(t+z) dt.
Then F(0)=D(1). Dominated convergence at0 uses log(1+t)/t<=1.
Integration by parts for z>0, followed by differentiation on compact
positive z intervals, gives

    F(z)=c log(1+z)-integral_0^1 log(t+z)/(1+t) dt,
    F'(z)=c/(1+z)-Abar1(z).                              (8)

The differentiated integrands are bounded on every such compact
interval; the behavior near0 of the right side is integrable by(4).
Taking the lower integration endpoint to0 therefore yields the
integrated form of(8), with F(0)=D(1). The real inversion identity
above and the log(t) part of(3) now give

    Qbar(z)=3D(1)+r^2/2+integral_0^z F'(u)du-D(z).

Hence prescribe the finite log-polynomial

    Q_K(z)=3D(1)+r^2/2
            +integral_0^z [c E_K(u)-A1_K(u)]du-D_K(z).    (9)

The integral in(9) is explicit: integrate monomials, and use
integral_0^z u^j log(1/u)du
=z^(j+1)[r/(j+1)+1/(j+1)^2], j>=0.
This is a finite formula, not a newly unevaluated bank integral.
No series interchange on the t integral in(3) was made.

On0<z<=b, the cited series give

    |log(1+z)-S_K|<=2z^(K+1), |D(z)-D_K|<=2z^(K+1),
    |(1-z)^-1-G_K|<=2z^K, |(1+z)^-1-E_K|<=2z^K.         (10)

Here |S_K|<1,c<1. Since Abar1=(r+log(1+z)-c)/(1-z),
(10) yields |Abar1-A1_K|<8(1+r)z^K. Also
Abar2=(Abar1-1/2)/(1-z), and8b^K<1 gives
|A1_K|<=2(1+r). The same decomposition therefore yields

    |Abar2-A2_K|<=22(1+r)z^K<32(1+r)z^K.

For Q, (8)-(10) bound the integrand error by10(1+log(1/u))u^K.
Its integral is10z^(K+1)[(1+r)/(K+1)+1/(K+1)^2]. Adding
the D tail bounds the error by22(1+r)z^(K+1), hence by
32(1+r)z^K. Finally |E_K|<=2 gives
|(1+z)^-2-E_K^2|<=6z^K. Thus the five nonreciprocal weights
are approximated by Q_K,A1_K,A2_K,E_K,-E_K^2 with common error

    error <=32(1+r)z^K.                                (11)

The two reciprocal weights are retained exactly. Integrate these
finite approximations with(6). Since L=3c<3, every nonreciprocal
bank truncation error is at most

    32b^(K+1)[4/(p+K+1)+1/(p+K+1)^2]<2^-571.            (12)

### 3. Rational constants, cancellation and bank error

Take the rational centers

    c0=2sum_(j=0)^511 (1/3)^(2j+1)/(2j+1),
    D0=sum_(j=1)^768 2^-j/j^2+c0^2/2.

The positive tails, with the real Landen identity for D(1), imply

    |c-c0|<2^-1024,
    |D(1)-D0| <=2^-768/769^2+2^-1024<2^-760.             (13)

In(6)-(9), replace c,D(1),L by c0,D0,3c0 and perform all
finite rational arithmetic exactly. This specifies each bank center.
There is no rounding loss from a cancellation of rational terms in
this exact-real model; their bit sizes are not bounded by this claim.

Here is an explicit error bound for the constant substitution, rather
than an appeal to nominal precision. Write delta=c0-c. Replacing L
in(6) is equivalent to replacing r(z) throughout each integrand by
r(z)+3delta. In A1_K, this and c->c0 change the factor r-c by
2delta, giving error<=4|delta| since |G_K|<=2. For A2_K the
error is<=8|delta|. In(9) the integrand changes by at most6|delta|,
the r^2/2 term by at most3|delta|r+(9/2)delta^2, and the constant
by3|D0-D(1)|. For p>=2,
integral_0^b(z/b)^p r dz <=b[3/(p+1)+1/(p+1)^2]<1/2,
and integral_0^b(z/b)^p dz<=b. These estimates, |delta|<1,
and integrating the6z|delta| term bound every constant substitution
error by16(|delta|+|D0-D(1)|). The regular rational weights and
the reciprocal weights do not use these constants at all.

Combining(12),(13) gives the uniform bank radius

    eta_bank=2^-570.                                    (14)

The returned interval can be defined as its rational center plus/minus
eta_bank, with exact zero radius for the two reciprocal banks. This
definition does not assert that the bank has already been evaluated.
It pays the weight-series and constant errors analytically, including
cancellation in Q. Generation and interval arithmetic cost are not free
in a complete implementation; Section6 gives them away only in a lower
bound that already fails.

### 4. Both Taylor densities and the interior join

For each positive n use the polynomials

    f_n^T=sum_(r=1)^128 (-1)^r omega_n^(2r) z^(2r)/(2r)!,
    d_n^T=sum_(r=1)^128 (-1)^r r omega_n^(2r-2) z^(2r)/(2r)!.

Taylor's theorem for cosine through degree257 and sine through
degree256, with their zero parity terms included, gives

    |f_n-f_n^T|<=omega_n^258 z^258/258!,
    |d_n-d_n^T|<=omega_n^256 z^258/(2*257!).              (15)

It does not require that the alternating terms decrease at small
indices. Since omega_n<512, z<=b, and129/512^2<1, both
remainders are bounded by T(z/b)^258, T=64^258/258!<2^-150.
The absolute weighted integral of(z/b)^258 is<1 for EACH weight:
for Q it is at most
b[(25/2)/259+5/259^2+1/259^3], for either A it is at most
b[4/259+1/259^2], for the reciprocals it is1/258 and8/257,
and for either regular rational weight it is at most b/259.
These follow by(4),(6). In particular the reciprocal singularities
are paid by the actual vanishing order, not an integrable-weight
assumption that would be false at power zero.

The absolute sums of the scaled Taylor coefficients are each<e^64.
For f this follows from cosh(omega_n*b)-1; for d the sum is
b*sinh(omega_n*b)/(2omega_n)<e^64 because omega_n>1.
As log2>2/3, e^64<2^96. Thus using the rational bank instead of
the true bank costs<2^96 eta_bank=2^-474 per moment, despite
the possibly severe cancellation. The complete endpoint error is

    epsilon_end < T+2^-474 <2^-149.                     (16)

Here the density coefficients still use exact omega_n. Their finite
enclosures are an unpaid later obligation, not included in(16).

For completeness check the interior holomorphic hypotheses anew.
The integrals(3) extend holomorphically to Re(z)>0: on each compact
subset, expanding1/(t+z) locally is uniformly dominated by an
integrable multiple of1 or log((1+t)/t). This also passes through
z=1; separated real primitive singularities at1 are removable.
On the rho=2 ellipse over[b_j,2b_j], b_j=2^-j,j=1,2,3,

    Re(z)>=7b_j/8, |z|<3b_j, |Im(z)|<=3b_j/8.

Bounds(3)-(4) at the real part give |Abar_j|<j+2 and
|Qbar|<(j+3)^2, where the latter j denotes the panel index.
The integral representations of cos(w)-1 and sin(w) give
|f_n(z)|<=(A/2)|z|^2 e^(192b_j) and
|d_n(z)|<=|z|^2 e^(192b_j)/2. The reciprocal denominators
cancel the displayed powers of |z|; |1+z|>=1 for the regular ones.
Since b_j^2(j+3)^2<=4, every weighted integrand is bounded by

    M_j=2^23*2^(288b_j).

Use log2>2/3 for the exponential comparison. The cited Gauss theorem
and the interval half-length give, with n=N-1,

    error_j <=(32/45)b_j*2^23*2^(288b_j-2n)
             =(32/45)b_j*2^-65.                        (17)

For N=117,81,63 respectively,2n=88+288b_j. Their intervals
join exactly to[b,1], with no strip omitted or duplicate positive
measure. Combining(16),(17) gives every one of the fourteen moments

    epsilon < (28/45)2^-65+2^-149 <2^-64.               (18)

This is exact-node quadrature with exact primitive values. C998o's
node radii are not silently identified with zero error in a finite
service; their propagation and all interior interval widths are unpaid.

### 5. Complete ideal entry propagation

The scale substitution ds=a dz in C998i gives
H=a h,P=p,T=t/a,R(0)=r_0,R'(0)=r_1/a,
R(a)=r_a,R'(a)=r_b/a. For dotted quantities the factors are
a^3,a^2,a,a^2,a,a^2,a respectively, since chi_n(a z)=a^2 d_n(z).
Put j0=J/a, beta_n=omega_n sin(n*pi/2), c_n=1-cos(n*pi/2),
alpha_n=sin(n*pi/2)/(2omega_n),
gamma_n=sin(n*pi/2)/(2omega_n)+cos(n*pi/2)/2.
At endpoint0 take r=r_0,r'=r_1, and at1 take r=r_a,r'=r_b.
Let w_nm=r'_n r_m-r_n r'_m, v_n=r'_n dot r_n-r_n dot r'_n,
and Delta mean endpoint1 minus endpoint0. For F_nm=I_nm/a,

    F_00=j0, F_0m=F_m0=j0+h_m (m even),
    F_nm=j0+[Delta w_nm+omega_m^2 h_m-omega_n^2 h_n
       +c_m t_n+beta_m p_n-c_n t_m-beta_n p_m]
             /(omega_m^2-omega_n^2), 1<=n<m, equal parity,
    F_nn=j0+Delta v_n+h_n+omega_n^2 dot h_n
       +alpha_n t_n+gamma_n p_n-c_n dot t_n-beta_n dot p_n.

These are exactly C998i's formulas, not a diagonal limit used without
independent dotted data. Constants here are ideal exact constants.
All true undotted moments have modulus<=A and dotted ones<=1:
use |f|<=Az^2/2, |d|<=z^2/2, (4),
z^2(1+r)<=1, z^2(2+2r+r^2/2)<=2, and the canceled reciprocal
powers. The two inequalities follow by differentiation in r>=0.

For moment errors<=epsilon<2^-64, the four products in Delta w
cost at most8A epsilon+4epsilon^2. The remaining distinct-frequency
numerator errors are at most(2A+1028)epsilon. The same-parity gap
omega_m^2-omega_n^2>=2pi^2>18>1, so their total is
<(10A+1028+4epsilon)epsilon<2^22 epsilon.
The four products in Delta v cost at most4(A+1)epsilon+4epsilon^2;
the remaining diagonal errors cost at most(A+517)epsilon since
|alpha|,|gamma|<=1, |c_n|<=2, |beta|<512. Thus their total is
<(5A+521+4epsilon)epsilon<2^22 epsilon.
Both endpoints have been counted in each case. This includes n=0
mod4, whose gamma_n=1/2 term persists. Zero-mode error is<=epsilon,
and no dotted zero mode is used.

C998i's normalized multiplier a nu_n nu_m/2 is1/2 when both modes
are positive, sqrt(2)/4 when only one is zero and1/4 when both are
zero. Consequently normalized basis-entry error is<=2^21 epsilon.
C999q's exact Z has
r_n=(nu_n/nu_p)(1/4+k_p^2)/(1/4+k_n^2), p=n mod2, and0<r_n<1:
for odd modes this is monotonicity in k_n; for even n>=2 use
numerator sqrt(2)/4 and k_n>10, as independently checked in C998a.
The exact rational archive check below gives each free-column l1
mass M_i<7/3; hence completed mass U_i<=2M_i<8.

Every same-parity product occurs in S_ij=sum u_ni u_mj B_nm. Thus

    error(S_ij)<=U_i U_j 2^21 epsilon<2^27*2^-64=2^-37.

This proves(1), with both parity blocks, all nine column products,
unchanged coefficients and no assumed coefficient cancellation.

### 6. A mandatory scalar prefix stops the implementation

A known-sign interval product uses two scalar multiplications, each
with its assignment: cost4. Accumulating it uses two additions and
their assignments: another4. Giving initialization of the first term
away except for its products, a length-L interval dot costs at least
8L-4. This counts neither sign tests nor extra products for sign
uncertainty. It applies to the explicitly prescribed endpoint arithmetic;
it is not a lower bound for an algorithm accumulating centers/radii
by another method.

To be favorable, discard all work at the three exactly centered Gauss
nodes, leaving258 nodes. The interval-dot work still includes14*255
interior sums of that length and14*255 endpoint sums of length128.
The polynomial primitive calls on those258 nodes separately require
767 or511 multiply-add Horner stages for each of TWO scalar endpoints.
One stage costs4 (multiplication and addition, each with its assignment),
hence8 for the two endpoints. The leading factors, argument construction,
coefficients, comparisons, transformations, signs and series tails are
all given away. There are three D calls and three elementary log calls
at each node. Extra logs inside D are given away as well.

| Mandatory component | Scalar operations |
| --- | ---: |
| C998o audited node/weight setup |3290939|
| 14*255 interval dots,258 interior terms |7354200|
| 14*255 interval dots,128 endpoint terms |3641400|
| 3*258 paired Li_2 Horner evaluations,8*767 each |4749264|
| 3*258 paired log Horner evaluations,8*511 each |3164112|
| Total lower bound |22199915|

The excess over the full cap is2199915. This table also gives away
ALL bank generation, density evaluation, frequency coefficients,
remaining constants, node uncertainty propagation, exact Z, moment
entry assembly and final three-column contraction. All would have
nonnegative extra cost. They cannot repair(2), even if their errors
could be certified. The first decisive failed threshold is therefore
the complete work cap; no full batch or post hoc parameter sweep is run.

The counts depend on separate interval-endpoint sums and separate
primitive calls. Reusing primitive identities, aggregating error radii
or contracting coefficients before evaluating moments would be
different implementations requiring their own proof. The old C998j
graded-summation stop and C998k bisection stop are neither reused as
current cost estimates nor erased. C998o supplies a real improvement
to the setup, while the complete service remains open.

### 7. Finite evidence and qualifications

Reproduce the exact planning checks from this notebook:

    python3 scripts/separation-seven/shared-taylor-bank-696.py

The complete certificate is
`scripts/separation-seven/shared-taylor-bank-696.json`. All299 checks
pass: the128 bank remainder bounds, constant tails, seven singular
weighted Taylor bounds, three panel balances, exact witness hash and
all762 binary-rational coefficients, both endpoint product-error bounds,
all nine ideal contraction bounds and the complete displayed work sum.
The certificate explicitly reports the failed service threshold and
unpaid finite errors. It contains formulas/bounds, not computed bank,
quadrature or S_ij values. Continuous inequalities are proved above;
numerical previews are not their proofs. The original specialization
and its complete planning evidence are audited separately in Section8.

A-square, both mixed terms, projection, the full100000000 service,
reference inverse debt, signed S3, higher/mixed signs, C744q/H2,
non-neutral coverage and actual-Xi/global assembly remain unresolved.
Refuting this implementation is not refuting RH or all square services.

### 8. Separate conceptual audit698

The invocation-start SPECIALIZE assessment696, with completed source
comparison697, covers precisely Sections1-7 and the fixed696 prescription.
The primary Taylor, series, real dilogarithm and Gauss statements cited
in the hypotheses are reused within their inspected domains. This is a
REPRODUCTION audit, not a reproof of those general theorems, a new bank
implementation or an audit of the original source/core/operator contracts.
C998i/audit682, C998a(4)/audit655, C999q's exact completion and
C998o/audit695 are retained as audited local inputs.

**Primitive and finite weights.** With D(x)=-Li_2(-x), all inversion
and Landen arguments used here are real and avoid the excluded cuts.
Separating the two logarithms in(3) gives Qbar=F+D(1/z), by t=zy
in the negative-log part followed by integration by parts. Its boundary
term is zero because log(1+y)log(yz) tends to zero as y->0. The upper
boundary log(yz) vanishes at y=1/z. Thus the contribution is exactly
D(1/z), with no endpoint constant lost. The cited inversion is
D(1/z)=2D(1)+r^2/2-D(z); F(0)=D(1) therefore gives the constant
3D(1) in(9), not2D(1). Integration by parts for F and dominated
differentiation on compact positive z intervals give(8). Its derivative
is O(1+log(1/z)), integrable at zero, so the lower endpoint in its
integrated form is justified.

The formulas for Abar1 and Abar2 follow directly by partial fractions
in(3), with the second subtraction equal to integral_0^1(1+t)^-2dt=1/2.
On[0,1/8], the four tails in(10) are dominated by geometric tails.
For Abar2, decomposing the error into the Abar1 error divided by1-z
and (A1_K-1/2) times the geometric tail gives at most
16(1+r)z^K+5(1+r)z^K<22(1+r)z^K. For Q the integrated error is
bounded by the displayed10-term majorant plus the D tail. These
estimates imply(11) for all five approximated weights, including the
square E_K^2. The reciprocal weights are unchanged.

Every power in the bank has p>=2. In(6) the smallest exponent after
integration is p-1>=1, so all boundary terms really vanish, including
the1/z^2 case. Integrating(11) gives(12); the audit checks its rational
value at EACH of the128 powers, not just a selected bank or preview.

**Constant substitution and cancellation.** The positive log2 tail
is at most9/(4*1025*3^1025), below2^-1024. For Li_2(1/2), summing
the geometric tail after term768 gives2^-768/769^2. Since0<c0<c<1,
|(c0^2-c^2)/2|<=|c0-c|; this proves the D0 bound in(13).

The shift argument in Section3 applies to the ENTIRE finite expression,
including the nested integral in Q_K. Indeed the explicit primitive of
u^j log(1/u) is u^(j+1)[r/(j+1)+1/(j+1)^2]. Substitution
r->r+3delta changes it by3delta*u^(j+1)/(j+1), exactly the primitive
of the constant-shifted integrand. The polynomial primitive and the
outer bank integral therefore commute with that substitution. The
quadratic r term occurs outside the inner primitive and its change is
3delta*r+(9/2)delta^2. Combining these changes with |G_K|,|E_K|<=2,
integral(z/b)^p r<1/2 and integral(z/b)^p<=b proves the bound16 in
Section3. Exact rational cancellation incurs no rounding error in the
stated model. This does not assert small rational bit complexity or
finite-frequency enclosure accuracy.

**Both densities and the join.** Cosine Taylor degree257 and sine
Taylor degree256 yield the respective orders258 and257. Multiplying
the latter remainder by z/(2omega) gives precisely the second bound
in(15). At omega<512 and z<=1/8 its coefficient relative to the first
uniform bound is129/512^2<1. Thus BOTH densities have the same z^258
vanishing majorant; it is not permissible to integrate a uniform
constant against1/z^2. All seven absolute weighted masses in Section4
are checked exactly and are below1. The absolute Taylor coefficient
sums are bounded by the stated cosh and b*sinh/(2omega) expressions.
The positive atanh series gives log2>2/3, hence the common2^96 bound.
This proves the endpoint error with cancellation paid explicitly.

On each rho=2 ellipse the positive real-part bound is7b_j/8. This
puts every denominator t+z in the integral weights away from zero on
a neighborhood of the ellipse; their logarithmic t-majorant is
integrable. It also excludes the reciprocal singularity. In particular
crossing the real point1 does not create a pole of the integral weights.
The density bounds follow by integrating the sine/cosine derivatives
on the segment from0 to z, using exp(omega*|Im z|). For Q the largest
prefactor is (9/2)A b_j^2(j+3)^2<=18A<2^23; the other six weights
have smaller bounds after canceling their displayed reciprocal powers.
This verifies M_j, rather than inferring it merely from analyticity.
The affine half-length and n=N-1 convention give exactly(17). The
three closed panels cover[1/8,1] up to their shared null endpoints;
their error sum is(28/45)2^-65. Adding the endpoint contribution gives
(18). No enclosed node was replaced by its exact value in a claimed
finite computation: exact nodes and weights are hypotheses of this
IDEAL bound only.

**All entries and the frozen contraction.** Substituting s=a z in
C998i multiplies undotted H,P,T by a,1,a^-1 and the endpoint data by
1,a^-1. Since chi_n(a z)=a^2 d_n(z), the dotted factors are a^3,a^2,a
and a^2,a. Thus Delta W contributes a^-1 Delta w before division by
the frequency difference, while Delta V contributes a Delta v before
division by a. The formulas in Section5 follow with BOTH endpoints
and the indicated independent dotted data. The positive diagonal
residues have (alpha,gamma,c,beta) equal to

    (0,1/2,0,0), (1/(2omega),1/(2omega),1,omega),
    (0,-1/2,2,0), (-1/(2omega),-1/(2omega),1,-omega),

in residue order0,1,2,3. In particular the P term survives at positive
multiples of4. Mode zero instead uses j0 or j0+h_m, with j0 exact
in the ideal calculation; no parameter derivative at zero is used.

For the true moment envelopes, differentiating e^-2r(1+r) gives a
negative derivative on r>=0; differentiating
e^-2r(2+2r+r^2/2) gives e^-2r(-2-3r-r^2). Their maxima at zero
give the stated A and1 bounds. A product of two undotted data costs
at most2A*epsilon+epsilon^2, and an undotted/dotted product costs
(A+1)*epsilon+epsilon^2. Each Delta contains four such products.
Adding every remaining term gives exactly the two Section5 bounds,
both below2^22 epsilon. The distinct positive same-parity gap is at
least2pi^2; discarding this beneficial divisor is valid. No diagonal
entry is estimated by dividing by that gap.

C998a's unitary has disjoint parity outputs, so opposite-parity square
entries vanish. Same-parity normalization gives the three multipliers
1/2,sqrt(2)/4,1/4. C999q's exact Z and0<r_n<1 therefore give the
completed column mass U_i<=2M_i. The audit loads EVERY binary-rational
free coefficient from the pinned archive and compares it exactly to
certificate696, before recomputing each M_i. It then checks all nine
ordered contraction bounds, including all completion coefficients via
this analytic mass bound. Exact Z is an ideal input, not a computed
finite enclosure. The result remains(1), not a residual-size or sign
estimate.

**Prescribed cost and complete finite evidence.** The cost claim is
about the fixed endpoint arithmetic in working696. A product pair costs
four scalar operations including destinations. A subsequent addition
pair costs four more, giving4L+4(L-1)=8L-4 per interval sum. This
prescription still forms both endpoints when a coefficient or bank is
exact. It is not the cost of an optimized degenerate-interval or
midpoint/radius algorithm. The two Horner evaluations have767 or511
stages, each stage costing two arithmetic operations plus their two
assignments. The three D calls and three logs are distinct prescribed
calls. Their reductions, leading factors and tails are omitted only
in the favorable lower count; no claim is made that the polynomial
alone evaluates either primitive accurately.

The audited C998o cost is reused as an input. Its full694 source,
certificate and compressed transcript and the695 audit program are
bound to the saved695 audit by their complete SHA256 hashes; its full
instruction inventory reproduces3290939. The earlier rational replay
and source-correspondence proof are not rerun or newly claimed here.
Adding the other four independent mandatory categories reproduces
22199915, exceeding the cap by2199915. The already discarded three
midpoint nodes and all other omitted work cannot decrease this lower
count. This verifies the scoped stop while leaving alternative
implementations untested.

The separate verifier is
`scripts/separation-seven/shared-taylor-bank-audit-698.py`; run it with

    python3 scripts/separation-seven/shared-taylor-bank-audit-698.py

Its full report is `scripts/separation-seven/shared-taylor-bank-audit-698.json`.
All1636 exact checks pass, including all128 bank rows, seven weighted
masses, three panels,762 coefficients, nine square bounds, every displayed
cost category and unchanged input hashes. Its exact bound fields admit
the dyadic upper enclosures bank<=2^-579, endpoint<=2^-152,
moment<=2^-65 and ideal square<=2^-40; these verify the original looser
thresholds and do not change the prescribed computation. No bank center,
quadrature value or S_ij has been evaluated. The original299-check696
certificate and all stopped implementations are preserved.

No formula or hypothesis correction was necessary. The bank and its
ideal contraction are now audited local inputs; finite-service accuracy,
complete work and every independent gap listed in Section7 remain open.

## Mathlib

Full matching coverage for this finite bank, weighted tails and scalar
implementation bound has not been checked. Supporting power-series,
integration and finite-arithmetic results alone would not verify the
complete service. Unknown availability is not evidence of absence.
The standard Taylor, series, branch and Gauss results are cited above;
the local specialization is explicitly qualified and independently
audited in Section8; full matching Mathlib coverage remains unchecked.
