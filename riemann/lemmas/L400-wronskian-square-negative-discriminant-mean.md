# Lemma 400: the Wronskian-square weighted discriminant mean has negative coefficient

## Hypotheses

Use the fixed actual F=F_0,G,A of L370/L381 on t>=40, with ordinary
height derivatives, T=1+t, L=log(2+t), and the complete physical normalized
discriminant Delta of L370. Put

    f=F/A, x=f, y=f'/L, z=f''/L^2, U=x^2+y^2+z^2,
    Wcal=(F'G-FG')/(A^2 T^2 L),
    Z=zeta(5/2+it), R=exp(i phi), E=R^2, c=1/(4pi).

R is the actual gamma carrier of L390. Let B(h,k) and Psi be exactly
the positive finite Euler factors and absolutely convergent arithmetic
series of L393:

    B(h,k)=product_(p^e || hk) [1+e(p-1)/(p+1)]  (coprime h,k),
    Psi=sum_(m,n>=1) tau(m)tau(n)(mn)^(-5/2)
                 B(m/g,n/g)/sqrt((m/g)(n/g)), g=gcd(m,n).

Here tau counts positive divisors and B(1,1)=1. H tends to infinity
through real values; response heads are fixed before height limits.
There is no mollifier, RH, simplicity, disjointness, independent-phase,
pointwise sign, common-zero count or growing-head-rate assumption.

## Conclusion

With ell=log H,

    (1/H) integral_[H,2H] Delta(t) Wcal(t)^2 dt
       = gamma_W ell^4+o(ell^4),
    gamma_W= -c^4 * [281/(604800 zeta(2))] * Psi < 0.       (1)

Thus the requested gamma_W>0 witness fails. This is a local REPRODUCTION
of known-source tools with a changed family-specific polynomial, not an
original moment theorem. The separate step 82 critical audit below validates
the complete asymptotic and its negative coefficient. A negative weighted mean neither rules out positive Delta elsewhere nor establishes
eventual D<=0. It supplies no mixed positivity, total L367 margin,
common-zero upper bound, new zero-exclusion range or RH consequence.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-12-wronskian-square-weighted-discriminant.md`.
The known analytic inputs are imported without reproof:

- C. P. Hughes and M. P. Young, *The twisted fourth moment of the Riemann
  zeta function*, J. reine angew. Math. 641 (2010), 203–236,
  [arXiv:0709.2345v2, Theorem 1.1, (11)–(17), pp. 3–5 and the holomorphy remark](https://arxiv.org/pdf/0709.2345v2#page=4).
- H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
  [arXiv:2304.05178v1, Theorem 3](https://arxiv.org/html/2304.05178v1).
- The fixed-right-line modified-Gonek lemma in A. Sourmelidis, J. Steuding
  and A. I. Suriajaya, *Dirichlet Series with Periodic Coefficients and
  their Value-Distribution Near the Critical Line*,
  [arXiv:2007.14008v2, Section 3 between (35) and (36), both gamma branches](https://arxiv.org/html/2007.14008v2#S3).
- J. Bourgain, *Decoupling, exponential sums and the Riemann zeta function*,
  [arXiv:1408.5794v2, Theorem 5 (0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2).

L390/L391 give the audited physical norms, exact ordinary jets, signed
primitive and connector estimates. L392 gives the carrier-free contour
method. L393 gives the general four-jet conversion of the complete six-term
moment. L394 gives the signed-endpoint method. Their particular previously
evaluated coefficients are not substituted for this changed statistic.
The finite algebra below is needed to check this response-dependent weight.

### Physical replacement without extra critical factors

Put g=G/A and v_j=g^(j)/(T^2 L^j), j=0,1,2, using pointwise divisors
after ordinary differentiation. Set a=Re(RZ), h=Im(RZ). L390 (4) retains
the complete response series and its derivatives and proves uniformly

    (v_0,v_1,v_2)=(c a,-c h/2,-c a/4)+O(1/L),
    |v_j|<=C, (1/H) integral_[H,2H] U^2=O(ell^4).

The constants here are independent of a response head. Envelope terms
cancel exactly in F'G-FG'=A^2(f'g-fg'), including at zeros; this is the
same common-envelope Wronskian identity used in L370. Therefore

    Wcal=y v_0-x v_1,
    w_0=c(ya+xh/2),
    |Wcal-w_0|<=C sqrt(U)/L,
    |Wcal|+|w_0|<=C sqrt(U),
    |Wcal^2-w_0^2|<=C U/L.                            (2)

Use L390's leading discriminant

    d=c^2(M|Z|^2+Re(K E Z^2)),
    M=(z^2+3xz/2+x^2/16-y^2)/2,
    K=((z-x/4)-iy)^2/2.

Its proof gives the pointwise bound |Delta-d|<=CU/L, including the
complete O(U/(T^2 L^2)) envelope-curvature term of L370; also |d|<=CU.
Consequently

    |Delta Wcal^2-d w_0^2|<=C U^2/L,
    (1/H) integral |Delta Wcal^2-d w_0^2|=O(ell^3).    (3)

This uses a quartic jet envelope, never a sixth critical-line moment.
It divides by no function value and is valid at every zero.

### Complete changed carrier decomposition

Define the real quadratic V and complex quadratic J by

    V=(y^2+x^2/4)/2, J=(y-i x/2)^2/2.

For RZ=a+ih, elementary real-part expansion gives exactly

    w_0^2/c^2=V|Z|^2+Re(J E Z^2).

The identity Re(u)Re(v)=Re(u conjugate(v)+uv)/2 yields

    d w_0^2/c^4=P|Z|^4
          +Re(P_1 E Z^2)|Z|^2+Re(P_2 E^2 Z^4),      (4)
    P=MV+Re(K conjugate(J))/2,
    P_1=MJ+VK, P_2=KJ/2.

All three terms are retained. In particular P_1 is not identically zero.
Each P_i is homogeneous of degree four in the critical jets. The real
balanced polynomial is

    P=x^4/512+7x^3z/64-9x^2y^2/128+x^2z^2/32
                       +9xy^2z/16-3y^4/8+3y^2z^2/8. (5)

For direct checking, if b=z-x/4 then

    Re(K conjugate(J))/2
       =(b^2-y^2)(y^2-x^2/4)/8+bxy^2/4.

Expanding this with MV proves (5), without replacing any algebraic
square by a modulus square or averaging independent phases.

### Both changed nonzero harmonics are lower order

Fix N and Z_N=sum_(n<=N)n^(-5/2-it). On the real interval let
overline(P_i) mean coefficient conjugation of its polynomial in real
x,y,z. The conjugate of the k=1 integrand in (4) is exactly

    overline(P_1)(x,y,z) E^(-1) conjugate(Z_N)^3 Z_N.

Use L391's exact holomorphic jets on H<=Re tau<=2H,
-11/20<=Im tau<=0, with s=1/2+i tau and L=Log(2+tau):

    (x,y,z)=-R(D_0,D_1,D_2),
    D_0=h_0,
    D_1=i(h_1+Omega h_0)/L,
    D_2=(-h_2-2Omega h_1-Omega^2 h_0+iOmega'h_0)/L^2,
    h_p=zeta^(p)(s), R'/R=i Omega.

Here zeta derivatives are s derivatives and Omega' is a tau derivative.
All branches and factors are holomorphic on a neighborhood of the same
pole-free rectangle. The four critical factors supply R^4=E^2, so this
conjugate has the extension

    E overline(P_1)(D_0,D_1,D_2) V_N^3 Z_N,
    V_N(tau)=sum_(n<=N)n^(-5/2+i tau),               (6)

where Z_N also denotes its entire height extension. This does not mean
complex conjugation off the real line. Every finite head product in (6)
is a fixed scalar times r^(i tau), r=u/v a positive rational.

Expand the displayed D_j, retaining every Omega' term. Each quartic
monomial is w(tau) product_(j=1)^4 h_(p_j)(s), p_j<=2, d_*=sum p_j<=8,
where each constituent scalar is C Omega^b(Omega')^e/L^m with
m=d_*+b+2e. The separate bounds of L391 imply

    |w|=O(ell^(-d_*)), |w'|=O(ell^(-d_*)/H).

They follow from Omega=O(ell), Omega'=O(1/H), Omega''=O(1/H^2) and
L'=1/(2+tau); they remain valid at zeros of these factors.

Exactly E=chi(1-s)=(2pi)^(-s)Gamma(s)
[exp(-pi i s/2)+exp(pi i s/2)]. The product of four h factors has an
absolutely convergent series on Re s>1, with coefficients c_p(n) bounded
by d_4(n)(log n)^(d_*) for n>=2, with n=1 separately interpreted.
These coefficients are O_eta(n^eta) for every eta>0. Encode the rational
twist by r^s F_p(s)=u^s sum c_p(n)(vn)^(-s). The latter series has
c_p(n) at index vn and zero otherwise. Thus the imported modified-Gonek
lemma applies with fixed integer q=u, fixed delta=1/20 and a=21/20.
Both gamma branches, subtracted at H and at V in [H,2H], give the full
right-line primitive bound of L391:

    O_(r,p)(H ell^(d_*+3)+H^(11/20)).

Indeed the theorem's additive-phase main sum is bounded by
sum_(n<=X)d_4(n)(log n)^(d_*)<=X(1+log X)^(d_*+3);
the opposite gamma branch is O(1). Partial summation using w and its
full variation gives O_N(H ell^3), including both boundary terms.

L391's audited Bourgain/interpolation/Cauchy bounds on the connectors are

    |h_p(sigma+it)|<=C_p ell^p H^B(sigma),
    B(sigma)=(5/18)(11/10-sigma),
    |chi(1-s)|<=C H^(sigma-1/2), 1/2<=sigma<=21/20.

The coefficient cancels all ell^(d_*) powers. Each connector is at most
O_N(H^(2/3)), since sigma-1/2+4B(sigma) has maximum 2/3 at sigma=1/2.
Fixed rational twists are bounded on this fixed strip. Cauchy's theorem
therefore proves the sharp k=1 integral is O_N(H ell^3).

For k=2, the conjugate extension instead is exactly

    R^4 E^(-2) overline(P_2)(D_0,D_1,D_2) V_N^4
       =overline(P_2)(D_0,D_1,D_2) V_N^4.            (7)

The carrier cancels, as in L392, but for the changed polynomial. The same
scalar expansion holds. On Re s=21/20 every h_p is bounded by its absolute
derivative series, so the horizontal integral costs O_N(H). Both connectors
cost O_N(H^(2/3)), because 4B(sigma)<=2/3. Holomorphy on the same rectangle
excludes residues. Thus the sharp k=2 integral is O_N(H).

These arguments verify the new polynomials' scope, rather than substituting
L391/L392's particular projections or the failed O(H^2) absolute rectangle.
No fixed-head bound is claimed uniform in N.

### Balanced coefficient, all collisions and signed sharp endpoints

L393 (5) applies to every quartic monomial in (5), with each ordinary
height order in {0,1,2} and every fixed reduced rational twist. To recall
the source hypotheses: take Hughes–Young scale H, epsilon=1/16, fixed
coprime h,k and fixed-width smooth nonnegative weight supported in
[H/2,4H], derivative scale T_0 a fixed small multiple of H. Eventually
hk<=H^(2/11-epsilon); all complex shifts are O(1/ell); the error is
O_(h,k,w)(H^(13/16)). L393 differentiates the complete holomorphic six-term
kernel on nested scaled Cauchy circles, retaining the half-log carrier,
ordinary-derivative i factors and all finite Euler factors. Finite-factor
derivative and physical-jet conversion errors are O_(h,k,w)(H ell^3).

Let mu be its universal quartic derivative functional. The complete table
for (5), including every signed contribution, is

| Monomial | Factor in P | mu | Contribution |
|---|---:|---:|---:|
| x^4 | 1/512 | 1/12 | 1/6144 |
| x^3 z | 7/64 | -1/240 | -7/15360 |
| x^2 y^2 | -9/128 | 1/720 | -1/10240 |
| x^2 z^2 | 1/32 | 1/4032 | 1/129024 |
| x y^2 z | 9/16 | -1/20160 | -1/35840 |
| y^4 | -3/8 | 1/6720 | -1/17920 |
| y^2 z^2 | 3/8 | 19/3628800 | 19/9676800 |

Summing the seven contributions exactly gives

    q_W=mu(P)=-281/604800 < 0.                       (8)

For fixed N write b_(m,N)=m^(-5/2) #{(a,b): ab=m, 1<=a,b<=N}.
Expanding |Z_N|^4 retains every ordered product pair and gives

    Psi_N=sum_(m,n<=N^2) b_(m,N)b_(n,N)
                  B(m/g,n/g)/sqrt((m/g)(n/g)), g=gcd(m,n).

Reducing every pair by its gcd and applying the four-jet formula gives
for every permitted fixed smooth nonnegative w

    integral w P|Z_N|^4
        =ell^4 [q_W Psi_N/zeta(2)] integral w+o_(N,w)(H ell^4). (9)

The arithmetic scalar is Psi_N, with all equal-product and equal-ratio
collisions, not a product of separate means or the |Z_N|^2 scalar of L394.

Since P is signed, direct nonnegative bracketing of (9) is invalid.
Use L394's endpoint construction: for fixed 0<delta<1/8 take 0<=w_delta<=1,
supported in [H,2H], equal to one off strips of width delta H at both
endpoints, with derivative bounds O_(j,delta)(H^(-j)) and integral
H(1+O(delta)). A smooth nonnegative b_delta majorizes the omitted strips,
has support in their fixed-width enlargements inside [H/2,4H], satisfies
the same derivative bounds, and has integral <=C delta H.

Uniformly in N, |P| |Z_N|^4<=C U^2, since |Z_N|<=zeta(5/2).
Also U^2<=3(x^4+y^4+z^4). The untwisted four-jet formula applied to these
three nonnegative powers with b_delta gives

    limsup_(H->infinity) integral b_delta U^2/(H ell^4)
       <= (3/zeta(2))*(1/12+1/6720+17/10644480)
                          limsup integral b_delta/H <= C delta. (10)

Hence (10) controls the absolute signed endpoint error in (9), with a
constant independent of N. Take the height limit at fixed N,delta, then
delta->0. This yields the sharp coefficient q_W Psi_N/zeta(2), for all
real H. A whole-interval O(H ell^4) estimate alone would not suffice.

### Uniform full-tail transfer and final sign

Let eta_N=sum_(n>N)n^(-5/2). On the real line |Z|,|Z_N|<=zeta(5/2),
|Z-Z_N|<=eta_N, |E|=1 and |P|+|P_1|+|P_2|<=CU^2. Telescoping the
four response factors in each term of (4) proves separately

    |full-minus-head balanced or projected integrand|<=C eta_N U^2.

Thus each sharp mean error is <=C eta_N ell^4, uniformly in N and large
H. The derivative tails already occur in (2)–(3)'s full physical replacement;
none is dropped in this algebraic tail passage. The fixed-head k=1 and k=2
bounds above, followed by height limsup and then N->infinity, make both
complete projections o(ell^4).

Furthermore b_(m,N) increases to tau(m)m^(-5/2). Since
B(h,k)<=tau(h)tau(k)<=tau(m)tau(n) for the reduced pair, each Psi summand
is bounded by tau(m)^2 tau(n)^2 (mn)^(-5/2)<=16(mn)^(-3/2), a summable
majorant. Hence Psi_N->Psi<infinity; positivity and the m=n=1 term give
Psi>=1. After the sharp fixed-head limit, the full balanced coefficient
error is bounded by C eta_N+|q_W| |Psi-Psi_N|/zeta(2), which tends to zero.
Together with (3), (4), (8) and the physical c^4 factor this proves (1).
No simultaneous growing-head limit or twist-uniform source error is used.

**Finite verification.** Run
`python3 scripts/discriminant/check_wronskian_weight.py`.
The full certificate is `scripts/discriminant/wronskian-weight-certificate.json`.
Rational sparse-polynomial arithmetic verifies the weight and complete
three-harmonic identities, reconstructs L393's six-term alternating kernel
through exponential degree twelve by exact Vandermonde division, and checks
low/odd cancellations and permutation symmetry. It saves the complete
balanced polynomial, both complex projected polynomials, seven-row moment
table, kernel coefficients, zero residuals and all division checks. The full
polynomials, relevant moment table, residuals and division checks were
inspected. No arithmetic failure occurred. The script proves only finite
algebra; all analytic estimates and limit orders are justified above.

The achieved coefficient is strictly negative, against the required strictly
positive coefficient. Stop this specific leading-mean diagnostic. It does
not prove positive Delta impossible, eventual negative Delta, or RH. The
separate audit below validates this asymptotic and its specialization.

### Separate critical audit — 2026-10-12, step 82

This REPRODUCTION proof audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-12-wronskian-weight-critical-audit.md`.
The inspected primary coverage is unchanged; no additional literature or
new theorem hypothesis is needed. The conclusion passes unchanged.
The checks below concern this complete statistic, not multiplication of
L381 and L393's separate means. L394's fixed-vector and L399's specified
mollifier failures are independent contrasts, not premises.

**Physical sign, divisors and degree.** L381 defines Wcal with F'G-FG',
the negative of L370's Wronskian. Direct product differentiation gives
F'G-FG'=A^2(f'g-fg'). Hence, with ordinary derivatives taken before
normalizing, Wcal=yv_0-xv_1 exactly. The full response estimates of
audited L390 therefore give w_0=c(ya+xh/2), with the plus sign and
factor 1/2 as in (2). The O(1/L) response errors include b'Z, bZ',
all second derivative terms and the exact gamma derivatives; no response
series was truncated in obtaining them. Each error in Wcal is at most
C sqrt(U)/L and both Wcal and w_0 are at most C sqrt(U).

L370's physical correction is exactly
4q(xv_1-yv_0)^2/L^2, q=(log A)''=O(T^(-2)). Together with the
quadratic response-minor polynomial it gives |Delta-d|<=CU/L and
|Delta|+|d|<=CU. Thus the decomposition

    Delta Wcal^2-d w_0^2
      =(Delta-d)Wcal^2+d(Wcal^2-w_0^2)

has absolute value at most CU^2/L, including all zeros and the full
curvature term. L390's imported fixed-order fourth norms give
integral U^2/H=O(ell^4), so (3) is O(ell^3). There are four critical
factors, not six; no division by a function value or nonvanishing
assumption enters this argument.

**Every harmonic and its analytic extension.** Put b=z-x/4. Then
K=(b^2-y^2)/2-i b y and J=(y^2-x^2/4)/2-i xy/2. Their product with
one conjugate gives

    Re(K conjugate(J))/2
      =(b^2-y^2)(y^2-x^2/4)/8+bxy^2/4.

This verifies the cross-term sign and both halves in (4). Multiplication
with MV gives precisely the seven monomials in (5). The complete exact
certificate also verifies the two real polynomial identities in a,h,
not merely their balanced pieces. Its full real and imaginary P_1 and
P_2 polynomials were inspected; P_2 includes the factor 1/2. For example
P_1 has x^3z coefficient -1/8 in its real part and x^3y coefficient
1/64 in its imaginary part, so it cannot be discarded algebraically.

Conjugation on the real line changes E to E^(-1) and Z_N to V_N.
Conjugate(P_i) means conjugating its coefficients in real jets.
All monomials have degree four, so substituting (x,y,z)=-R(D_0,D_1,D_2)
contributes R^4=E^2, with no surviving minus sign. The first projection
therefore leaves exactly E conjugate(P_1)(D)V_N^3 Z_N; the second
leaves exactly conjugate(P_2)(D)V_N^4. These are holomorphic extensions
of the real-line conjugates, not conjugation of functions off that line.
All branches are those of L391 on its pole-free rectangle.

For completeness, each summand of D_j is a constant times
Omega^b(Omega')^e L^(-m) h_p with the following (p,b,e,m) tuples:

    D_0: (0,0,0,0);
    D_1: (1,0,0,1), (0,1,0,1);
    D_2: (2,0,0,2), (1,1,0,2), (0,2,0,2), (0,0,1,2).

Every tuple satisfies m=p+b+2e. Multiplying any four proves the
claimed identity m=d_*+b+2e for every term of both changed polynomials.
The separately bounded Omega, Omega', Omega'' and L' prove both
|w|<=C ell^(-d_*) and |w'|<=C ell^(-d_*)/H by the product rule,
without logarithmic differentiation at a zero of a scalar factor.

At s=1/2+i tau, a fixed rational twist is
r^(i tau)=r^(-1/2)r^s. The harmless fixed r^(-1/2) is absorbed into
the scalar; r=u/v then gives exactly the series supported at vn and
integer gamma scale q=u. Its coefficients, including n=1, satisfy
the cited modified-Gonek hypotheses. The summatory bound
sum_(n<=X)d_4(n)<=X(1+log X)^3 follows by counting the fourth divisor
variable and summing the first three reciprocals. The signed primitive
on Re s=21/20 thus has bound H ell^(d_*+3)+H^(11/20), with both
gamma branches retained. Partial summation using the preceding full
variation bound gives O_N(H ell^3), including the boundary values.

The exact surviving carrier E=chi(1-s) has size H^(sigma-1/2).
For each sharp connector the audited L391 jet bounds therefore leave
exponent sigma-1/2+4B(sigma)=13/18-sigma/9<=2/3.
For the second projection there is no carrier, and 4B(sigma)<=2/3.
Both connectors have fixed length 11/20 and cost O_N(H^(2/3)).
On the right line the second projection uses absolutely convergent
zeta derivative series and costs O_N(H). Thus both estimates in L400
hold with the stated sharp endpoints. The historical O(H^2) absolute
certificate is not being reused, and no N-uniform connector constant
is asserted.

**Six-term coefficient and complete finite evidence.** Every monomial
of (5) falls within L393's general ordinary four-jet formula (5).
Fixed reduced twists meet Hughes–Young's size condition eventually;
fixed relative-width weights satisfy its support and derivative
conditions. The complete holomorphic six-term total is differentiated
on the separated scaled Cauchy circles of L393. Its ordinary height
operators retain the half-log gamma factors and all i powers. No
singular source summand is differentiated at coincident shifts.
Its application errors are O_(h,k,w)(H ell^3)+O_(h,k,w)(H^(13/16)),
which are o(H ell^4) with those parameters fixed.

The script was read and rerun. Its Vandermonde division multiplies
back exactly; the six selected subsets are all present. Exponential
degrees below four and odd degrees vanish, and the computed kernel
is permutation symmetric. Complete selected values were inspected
with `python3 ../scripts/loop/inspect_json.py` and `--full`: both zero
residuals, both projected polynomials, the balanced polynomial, all
thirteen division checks, all seven moment rows and the empty failures
field. The actual Taylor coefficients used for the seven rows are

    (0,0,0,0): 1/12;       (0,0,0,2): -1/480;
    (0,0,1,1): 1/720;      (0,0,2,2): 1/16128;
    (0,1,1,2): -1/40320;   (1,1,1,1): 1/6720;
    (1,1,2,2): 19/14515200.

Multiplication by their multi-index factorials 1,2,1,4,2,1,4
recovers every mu in the table. The endpoint z^4 coefficient
17/170311680, multiplied by 16, also gives the stated 17/10644480.
The seven full signed contributions sum exactly to -281/604800;
none is omitted or replaced by its absolute value. The script reported
zero failures. These finite checks certify algebra only; the imported
moment hypotheses and analytic estimates above are separate necessities.

**Collisions, absolute endpoints and ordered limits.** The square of
Z_N has coefficient b_(m,N) counting every ordered pair with product m.
Its modulus square therefore has every ordered (m,n), reduced by its
actual gcd. Applying the four-jet formula to each retains all repeated
product and reduced-ratio collisions, giving Psi_N, not L394's two-factor
arithmetic series. At a prime exponent e the common zero-shift factor
is 1+e(p-1)/(p+1), positive and at most e+1. Therefore the majorant
16(mn)^(-3/2) and monotone convergence prove Psi_N->Psi>=1.

The balanced polynomial is signed. Its absolute value times |Z_N|^4
is bounded by CU^2 with C independent of N. The nonnegative smooth
endpoint bump b_delta has integral O(delta H); the untwisted four-jet
formula for x^4,y^4,z^4 gives (10), on its whole support in [H/2,4H].
Thus the absolute missing endpoint contribution has normalized height
limsup O(delta), independent of N. At fixed N,delta the smoothed
asymptotic holds; then delta tends to zero, proving the sharp fixed-head
limit. This does not follow merely from a whole-interval fourth norm.

Finally four-factor telescoping gives, separately for all three
harmonics, the absolute bound C eta_N U^2 before integration. These
constants are independent of N. Derivative tails were already retained
in the physical replacement, so no separate derivative limit is hidden.
Writing A_H=(H ell^4)^(-1) integral_[H,2H] Delta Wcal^2, the assembled
estimates imply, for each fixed N after the endpoint-width limit,

    limsup_(H->infinity) |A_H-c^4 q_W Psi/zeta(2)|
      <= C eta_N+c^4 |q_W| |Psi_N-Psi|/zeta(2).

The physical O(ell^3) error and both fixed-head projections have
vanished in this height limit. Sending N to infinity makes the right
side zero. This is the complete sequential-limit justification for
all real H, without a growing-head rate or a width-uniform source error.
Since c>0, zeta(2)>0 and Psi>=1, the complete coefficient is negative.
The Wronskian-square witness stop is validated, with no new sign range,
eventual sign, common-zero bound or RH consequence.

## Mathlib

Full matching physical weighted asymptotic: **not checked**. The cited
shifted moment, signed primitive and subconvex results are analytic inputs;
no matching formal theorem or implementation is claimed. Polynomial and
Wronskian support alone would not cover the asymptotic. Unknown availability
is not evidence of absence.
