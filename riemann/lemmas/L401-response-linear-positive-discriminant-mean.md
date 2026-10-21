# Lemma 401: a positive direction in the complete response-linear weighted mean

## Hypotheses

Use the fixed actual real functions F=F_0,G and positive gamma envelope A
of L370/L390, on t>=40. All primes mean ordinary height derivatives. Put

    T=1+t, L=log(2+t), f=F/A,
    X=(x,y,z)=(f,f'/L,f''/L^2), U=x^2+y^2+z^2,
    Z=zeta(5/2+it), R=exp(i phi), E=R^2, c=1/(4pi),
    a=Re(RZ), h=Im(RZ).

R is the actual gamma carrier, not an independent phase. The complete
physical discriminant and its positive normalization are

    D=(2F'G'-FG''-F''G)^2-4(F'^2-FF'')(G'^2-GG''),
    Delta=D/(A^4 T^4 L^4).

Fix u,v in R^3, independent of H, and define

    p=u dot X, r=v dot X, W_(u,v)=a p+h r,
    theta=(u_0,u_1,u_2,v_0,v_1,v_2)^T.

Use the positive arithmetic scalar of L393:

    B(h_0,k_0)=product_(p_0^e || h_0 k_0)
                         [1+e(p_0-1)/(p_0+1)], gcd(h_0,k_0)=1,
    B(1,1)=1,
    Psi=sum_(m,n>=1) tau(m)tau(n)(mn)^(-5/2)
                 B(m/g,n/g)/sqrt((m/g)(n/g)), g=gcd(m,n).

Here tau is the divisor-counting function; the prime symbol p_0 in B
is unrelated to the jet polynomial p. H tends to infinity through all
real values. All response heads and smoothing widths are fixed before
height limits. There is no mollifier, growing twist/order/head, RH,
simplicity, disjointness, phase independence, eventual sign, common-zero
upper bound or favorable total L367 margin assumption.

## Conclusion

Writing ell=log H, the complete sharp mean is

    (1/H) integral_[H,2H] Delta(t) W_(u,v)(t)^2 dt
       =gamma_(u,v) ell^4+o_(u,v)(ell^4),
    gamma_(u,v)=(c^2 Psi/zeta(2)) theta^T C theta,       (1)

where the full symmetric matrix, in the stated theta ordering, is

    C=[ 1/4480       0          -19/2419200     0          -1/10080       0
        0           -89/2419200  0             -1/10080    0              1/226800
       -19/2419200   0          -257/319334400  0           1/226800      0
        0           -1/10080    0             -53/40320   0              83/1036800
       -1/10080      0           1/226800      0          -209/7257600    0
        0            1/226800    0              83/1036800 0             -25/4257792 ]. (2)

C has inertia (1 positive, 5 negative, 0 zero eigenvalues). Its nullspace
is trivial; it does have nonzero isotropic vectors because it is indefinite.
In particular u=(1,0,0), v=0 gives

    gamma_(u,v)=c^2 Psi/(4480 zeta(2))
                =Psi/(71680 pi^2 zeta(2))>0.           (3)

Thus Delta, and equivalently D, is strictly positive at some point in
every sufficiently high [H,2H]. In particular eventual D<=0 is false.
The separate step 86 critical audit below validates this local REPRODUCTION
specialization of known-source tools. It is not a new
moment theorem or an RH candidate. It supplies no total L367 pencil
margin, common-zero upper count, global mixed positivity, new Laguerre
sign/zero-exclusion range or RH conclusion. On isotropic directions (1)
alone decides no lower-order sign. Constants and onset are not evaluated.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-12-response-linear-weight-family.md`.
The imported theorems, not reproved here, are:

- C. P. Hughes and M. P. Young, *The twisted fourth moment of the Riemann
  zeta function*, J. reine angew. Math. 641 (2010), 203–236,
  [arXiv:0709.2345v2, Theorem 1.1, (12)–(17), pp. 4–5 and its holomorphy remark](https://arxiv.org/pdf/0709.2345v2#page=4).
- H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
  [arXiv:2304.05178v1, Theorem 3 and the defining asymptotic](https://arxiv.org/html/2304.05178v1).
- A. Sourmelidis, J. Steuding and A. I. Suriajaya, *Dirichlet Series with
  Periodic Coefficients and their Value-Distribution Near the Critical Line*,
  [arXiv:2007.14008v2, Section 3 between (35) and (36), both branches of the modified-Gonek lemma](https://arxiv.org/html/2007.14008v2#S3).
- J. Bourgain, *Decoupling, exponential sums and the Riemann zeta function*,
  [arXiv:1408.5794v2, Theorem 5 (0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2).

L390 supplies the complete physical replacement and fourth norms;
L391/L392 supply the exact ordinary jets and audited contour bounds;
L393 supplies the general complete four-jet functional; L394 supplies
the absolute endpoint method. The changed full-family coefficient and
carrier identities require a specialization, rather than substitution of
L394's fixed-jet or L400's single Wronskian coefficient. Those earlier
stops remain valid. No imported source states (1) for this statistic.

### Physical replacement and exact carrier decomposition

L390 proves, with the full response series and its first two derivatives,

    d=c^2(M|Z|^2+Re(K E Z^2)),
    M=(z^2+3xz/2+x^2/16-y^2)/2,
    K=((z-x/4)-iy)^2/2,
    |Delta-d|<=C U/L, |Delta|+|d|<=C U,
    (1/H) integral_[H,2H] U^2=O(ell^4).              (4)

In particular the error includes L370's exact common-envelope correction
4q(x v_1-y v_0)^2/L^2, where q=(log A)''=O(T^(-2)) and
v_j=(G/A)^(j)/(T^2 L^j) are uniformly bounded. Response derivatives and
the divisors taken after ordinary differentiation are retained. On the
real ray |Z|<=zeta(5/2), so |W_(u,v)|^2<=C_(u,v) U. Hence

    |(Delta-d) W_(u,v)^2|<=C_(u,v) U^2/L,
    (1/H) integral |(Delta-d) W_(u,v)^2|=O_(u,v)(ell^3). (5)

No replacement of the exact weight itself is needed. The argument is
valid at all zeros and uses four critical factors, not a sixth moment.

Define the real quadratic V and complex quadratic J by

    V=(p^2+r^2)/2, J=(p-i r)^2/2.

Since RZ=a+ih, exactly

    W_(u,v)^2=V|Z|^2+Re(J E Z^2).

Using Re(b_1)Re(b_2)=Re(b_1 conjugate(b_2)+b_1 b_2)/2 gives

    d W_(u,v)^2/c^2
       =P|Z|^4+Re(P_1 E Z^2)|Z|^2+Re(P_2 E^2 Z^4), (6)
    P=MV+Re(K conjugate(J))/2,
    P_1=MJ+VK, P_2=KJ/2.

These are degree-four polynomials in x,y,z, with fixed u,v coefficients.
Both nonzero harmonics are retained, even if a particular vector makes
one polynomial vanish. Put b=z-x/4 and define

    S=M/2+Re(K)/4=3z^2/8+5xz/16+3x^2/128-3y^2/8,
    T_*=M/2-Re(K)/4=z^2/8+7xz/16+x^2/128-y^2/8.

Because Im(K)=-by and Im(J)=-pr, the balanced polynomial is exactly

    P=S p^2+T_* r^2+(by/2) p r.                    (7)

The cross term has a plus sign. This is real polynomial algebra with the
actual carrier, not independent-phase averaging or a modulus-square
replacement of K or J.

### Every changed projection is lower order

Fix N and write Z_N=sum_(n<=N)n^(-5/2-it) and its reflected entire
height extension V_N(tau)=sum_(n<=N)n^(-5/2+i tau).
On the real line the conjugates of the first and second projections in
(6) have the respective holomorphic extensions

    E conjugate(P_1)(D_0,D_1,D_2) V_N^3 Z_N,
      conjugate(P_2)(D_0,D_1,D_2) V_N^4.            (8)

Here conjugation means coefficient conjugation in polynomials in real
jets, never conjugation at complex tau. L391's exact formulas on
H<=Re tau<=2H, -11/20<=Im tau<=0, with s=1/2+i tau, are

    (x,y,z)=-R(D_0,D_1,D_2), L=Log(2+tau),
    D_0=h_0, D_1=i(h_1+Omega h_0)/L,
    D_2=(-h_2-2Omega h_1-Omega^2 h_0+i Omega' h_0)/L^2,
    h_j=zeta^(j)(s), R'/R=i Omega,
    Omega=O(ell), Omega'=O(1/H), Omega''=O(1/H^2).

Every quartic supplies R^4=E^2. Thus the first conjugated carrier
E^(-1) leaves E, and the second E^(-2) cancels, proving (8) for every
direction. All branches are those of L391, holomorphic in a neighborhood
of the same pole-free rectangle; possible gamma, polygamma and zeta poles
have real height zero, and Log(2+tau) has no cut or zero here.

Each expansion term of either polynomial in (8) is
w(tau) product_(j=1)^4 h_(p_j)(s), p_j<=2, d_*=sum p_j<=8.
Its scalar is a constant times Omega^b_0(Omega')^e_0/L^m, with
m=d_*+b_0+2e_0. This follows term by term from the D formulas: the
(p_j,b_0,e_0,m) tuples for a single factor are

    D_0: (0,0,0,0);
    D_1: (1,0,0,1), (0,1,0,1);
    D_2: (2,0,0,2), (1,1,0,2), (0,2,0,2), (0,0,1,2).

Product differentiation, with L'=1/(2+tau) and the separate Omega bounds,
gives |w|<=C_(u,v) ell^(-d_*) and |w'|<=C_(u,v) ell^(-d_*)/H.
This includes all Omega' terms and remains valid when a scalar vanishes.

Each finite head product in (8) is a constant times rho^(i tau),
rho=a_0/b_0 a fixed positive rational. Encode it in s as
rho^(s-1/2); the fixed rho^(-1/2) is absorbed into the constant.
On Re s>1 the product of four h derivatives has coefficients c_p(n)
bounded by d_4(n)(log n)^(d_*) for n>=2, with n=1 interpreted directly.
Its series is absolutely convergent, and c_p(n)=O_eta(n^eta) for every
eta>0. Exactly

    rho^s product_j h_(p_j)(s)
        =a_0^s sum_(n>=1)c_p(n)(b_0 n)^(-s).

Thus the modified-Gonek lemma applies with fixed integer q=a_0,
delta=1/20 and a=21/20, to the series supported at b_0 n. Periodicity
is not a hypothesis. The actual surviving first carrier is exactly

    E=chi(1-s)=(2pi)^(-s)Gamma(s)
                         [exp(-pi i s/2)+exp(pi i s/2)].

Subtract the imported primitives at H and V, H<=V<=2H. The negative
exponential branch gives the additive-phase coefficient sum and
O(H^(11/20)) error; the opposite branch is O(1). Bounding the sum by
sum_(n<=C H)d_4(n)(log n)^(d_*)=O(H ell^(d_*+3)) yields the full
primitive O_(N,p)(H ell^(d_*+3)+H^(11/20)). The elementary divisor
bound follows by summing the first three reciprocal divisor variables
and counting the fourth. Partial summation with w and its complete
variation gives O_(N,u,v)(H ell^3), including both boundary values.

For both sharp connectors, L391's audited Bourgain/interpolation/Cauchy
bound is

    |h_j(sigma+it)|<=C_j ell^j H^B_0(sigma),
    B_0(sigma)=(5/18)(11/10-sigma),
    |chi(1-s)|<=C H^(sigma-1/2), 1/2<=sigma<=21/20.

For the first projection, normalization cancels the ell^(d_*) factors
and the exponent is sigma-1/2+4B_0(sigma)<=2/3. For the second it is
4B_0(sigma)<=2/3. Fixed rational twists are bounded on this fixed strip,
so both connectors cost O_(N,u,v)(H^(2/3)). On Re s=21/20 the second
projection has no carrier, and all derivatives are absolutely bounded;
its horizontal edge costs O_(N,u,v)(H). Cauchy's theorem on the pole-free
rectangle therefore gives the sharp bounds

    integral Re(P_1 E Z_N^2)|Z_N|^2=O_(N,u,v)(H ell^3),
    integral Re(P_2 E^2 Z_N^4)=O_(N,u,v)(H).         (9)

No constant in (9) is asserted uniform in N. These verify the changed
polynomials; L390's failed absolute O(H^2) certificate is not used.

### Complete balanced coefficient and inertia

For each quartic monomial use L393's general four-jet formula (5).
Its Hughes–Young application has fixed coprime h_0,k_0, four shifts
O(1/ell), a smooth nonnegative weight supported in [H/2,4H], and
derivative scale T_0 a fixed small multiple of H. With epsilon=1/16,
fixed twists eventually meet h_0 k_0<=H^(2/11-epsilon), the derivative
scale meets H^(1/2+epsilon)<<T_0<<H, and the theorem error is
O_(h_0,k_0,w)(H^(13/16)). The complete six-term total is holomorphic
at coincident shifts. L393 differentiates that total on separated nested
scaled Cauchy circles, not its individually singular pieces. Ordinary
i factors, the half-log carrier and every finite Euler factor are retained;
conversion and finite-factor derivative errors are O_(h_0,k_0,w)(H ell^3).

Let mu be its universal derivative functional on real quartic jets.
The required complete nonzero table is

| Monomial | mu |
|---|---:|
| x^4 | 1/12 |
| x^3 z | -1/240 |
| x^2 y^2 | 1/720 |
| x^2 z^2 | 1/4032 |
| x y^2 z | -1/20160 |
| x z^3 | -61/3628800 |
| y^4 | 1/6720 |
| y^2 z^2 | 19/3628800 |
| z^4 | 17/10644480 |

All other quartic monomials have odd total height order, and mu=0 by
complementing each two-element selection in the complete centered kernel
of L393 (4). This is exact kernel parity, not phase independence.
Writing C in u and v blocks, (7) gives every entry explicitly as

    (C_uu)_ij=mu(S X_i X_j),
    (C_vv)_ij=mu(T_* X_i X_j),
    (C_uv)_ij=mu(by X_i X_j)/4.                    (10)

The factor 1/4 in the last line retains the factor two in theta^T C theta.
Substituting the complete table into (10) gives precisely (2), including
all mixed entries. For the positive direction this can be checked directly:

    mu(S x^2)=1/512-1/768-1/1920+1/10752=1/4480.    (11)

For completeness the exact inertia certificate is a rational congruence,
not numerical eigenvalue estimation. Reorder theta as
(u_0,u_2,v_1,v_0,v_2,u_1). The reordered matrix is block diagonal and
equals diag(L_1,L_2) diag(d_1,...,d_6) diag(L_1,L_2)^T, where

    L_1=[ 1          0          0
         -19/540     1          0
         -4/9       -825/971    1 ],
    L_2=[ 1          0          0
         -581/9540   1          0
          4/53       77715/47419 1 ],
    (d_1,...,d_6)=(1/4480,
                  -971/898128000,
                  -508159/7047129600,
                  -53/40320,
                  -47419/47600784000,
                  -3054431/114716044800).

Exact multiplication proves the equality. Both triangular factors are
invertible with determinant one, so Sylvester's law of inertia gives
(1,5,0). Nonzero isotropic vectors are distinct from a nullspace.
As a contrast check, the L400 direction u=(0,1,0), v=(1/2,0,0) gives
theta^T C theta=-281/604800; its additional c in the weight explains
the c^4 factor there. That stopped direction does not preclude (11).

For a fixed head let b_(m,N)=m^(-5/2) #{(a_0,b_0):a_0 b_0=m,
1<=a_0,b_0<=N}. Expand |Z_N|^4 before reducing ratios; this retains
every ordered product collision. With g=gcd(m,n), put

    Psi_N=sum_(m,n<=N^2) b_(m,N)b_(n,N)
                       B(m/g,n/g)/sqrt((m/g)(n/g)).

Applying the four-jet formula term by term to P, with each fixed reduced
twist (m/g)/(n/g), proves for any permitted fixed smooth nonnegative w

    integral w P|Z_N|^4
      =ell^4 [Psi_N/zeta(2)] theta^T C theta integral w
                              +o_(N,u,v,w)(H ell^4). (12)

This is the |Z|^4 arithmetic scalar, not L394's |Z|^2 scalar or a product
of separate means. All equal ratios and both functional-equation diagonals
are included by the complete six-term formula.

### Absolute sharp endpoints and uniform full response tail

P is signed, so direct nonnegative bracketing of (12) is invalid. For
fixed 0<delta<1/8 use L394's smooth 0<=w_delta<=1 supported in [H,2H],
equal to one except in endpoint strips of width delta H, with derivatives
O_(j,delta)(H^(-j)) and integral H(1+O(delta)). Let b_delta be a smooth
nonnegative majorant of the omitted strips, supported in fixed-width
enlargements inside [H/2,4H], with integral <=C delta H and the same
derivative bounds. Uniformly in N,

    |P| |Z_N|^4<=C_(u,v) U^2,
    U^2<=3(x^4+y^4+z^4).

Apply the untwisted four-jet formula to these three nonnegative powers
with b_delta. At each fixed delta the source hypotheses hold and give

    limsup_(H->infinity) integral b_delta U^2/(H ell^4)
       <= (3/zeta(2)) * (1/12+1/6720+17/10644480)
                        limsup integral b_delta/H <=C delta. (13)

Thus the omitted signed integral has absolute normalized error
O_(u,v)(delta), with a constant independent of N. Apply (12) to w_delta,
take the height limit at fixed N,delta, then delta->0. The sharp balanced
coefficient is (Psi_N/zeta(2)) theta^T C theta for all real H.

For the full tail put eta_N=sum_(n>N)n^(-5/2). On the real line
|Z|,|Z_N|<=zeta(5/2), |Z-Z_N|<=eta_N, |E|=1, and
|P|+|P_1|+|P_2|<=C_(u,v) U^2. Telescoping each of the four response
factors in (6) bounds the full-minus-head balanced and each projected
integrand separately by C_(u,v) eta_N U^2. Their sharp mean errors
are <=C_(u,v) eta_N ell^4, independently of N. The response derivative
tails were already retained in (4)–(5); this passage truncates only values
in the exact leading product. From (9), first height limsup at each N
and then N->infinity makes both complete projections o_(u,v)(ell^4).

Moreover b_(m,N) increases to tau(m)m^(-5/2). For reduced ratios,
B(h_0,k_0)<=tau(h_0)tau(k_0)<=tau(m)tau(n), so every Psi summand
is at most tau(m)^2 tau(n)^2 (mn)^(-5/2)<=16(mn)^(-3/2), a
summable majorant using tau(n)<=2sqrt(n). Thus Psi_N->Psi<infinity,
and positivity and the m=n=1 term give Psi>=1. If q_theta=theta^T C theta,
the normalized balanced mean A_H satisfies

    limsup_(H->infinity)|A_H-q_theta Psi/zeta(2)|
       <=C_(u,v) eta_N+|q_theta| |Psi_N-Psi|/zeta(2),

which tends to zero. This displays the sequential limits: fixed vector,
head and width, height limit, width removal, then head removal. No growing-N
rate, N-uniform signed primitive, or simultaneous optimization is used.
Together with (5), (6) and the physical factor c^2 this proves (1).

Finally (11) and Psi>=1 prove (3). For this fixed direction the sharp mean
is positive for every sufficiently large H. Its squared weight is
nonnegative everywhere. If Delta<=0 throughout an interval, its mean
against that weight could not be positive. Thus Delta>0 somewhere in each
such interval; D has the same sign because A^4 T^4 L^4>0. This is a
physical-sign consequence, not a sign assertion about F's Laguerre form
or all mixed theta moments. It excludes only eventual D<=0, leaving the
total pencil margin, actual common-zero bounds and RH unresolved.

**Finite verification.** Run
`python3 scripts/discriminant/check_response_linear_family.py`.
The full certificate is
`scripts/discriminant/response-linear-family-certificate.json`.
Its rational sparse-polynomial routines are reused from the L400 script;
they reconstruct the complete alternating six-term kernel through
exponential degree twelve by exact Vandermonde division. The program
checks low/odd cancellations and permutation symmetry, the weight identity,
all three carrier terms, (7), every signed contribution to the six-parameter
coefficient, reconstruction of the symmetric matrix and the exact LDL
identity. Complete relevant moment rows, matrix, factors/pivots, zero
residuals, division checks and the positive witness were inspected with
the shared JSON inspector. No arithmetic failures occurred. This checks
finite algebra only; the analytic asymptotic is justified above and checked
in the separate audit below. The achieved positive coefficient meets the
approved existence threshold without claiming progress beyond the checked
moment theorems or an RH resolution.

### Separate critical audit — 2026-10-12, step 86

This REPRODUCTION proof_audit uses the unchanged prior SPECIALIZE assessment
`drafts/literature/2026-10-12-response-linear-family-critical-audit.md`.
The full asymptotic, all entries of (2), inertia and positive-D consequence
pass. The primary theorems cited above are imported in their already
inspected scopes; they are not reproved. This verifies the local application,
not progress beyond those sources, a new moment theorem or an RH candidate.

**Physical normalization and carrier algebra.** The normalization of D is
exactly L370's: its denominator is positive on the whole ray. In L390 the
ordinary response triple, divided only after differentiation, is
(ca,-ch/2,-ca/4)+O(1/L). Its boundedness and the quadratic minor identity
give |Delta-d|<=CU/L at zeros as well as nonzeros. The envelope term is
4q(xv_1-yv_0)^2/L^2, not an unnormalized Wronskian term; q=O(T^(-2)).
Since a^2+h^2=|Z|^2 is uniformly bounded, the exact squared weight is at
most C_(u,v) U. Thus the physical replacement costs O_(u,v)(ell^3)
in the sharp mean. This weight contains no c: the outside factor is c^2.

Writing b=z-x/4, K=(b^2-y^2)/2-i by and
J=(p^2-r^2)/2-i pr gives
Re(K conjugate(J))=(b^2-y^2)(p^2-r^2)/4+bypr.
This checks the plus sign and factor 1/2 of bypr in (7). Multiplication
of the two real-part decompositions yields the balanced term and both
nonzero carriers in (6), with precisely the displayed factors 1/2.
No averaging over the actual phase has been performed.

**Changed polynomials on the sharp rectangle.** Conjugating a projection
on the real line conjugates its polynomial coefficients, its response
head and E, while leaving the real jets unchanged. Substituting each jet
as -R D_j into either quartic supplies R^4. Consequently the two net
carriers are R^4 E^(-1)=E and R^4 E^(-2)=1, with head factors V_N^3 Z_N
and V_N^4 respectively, exactly (8). The ordinary D_2 contains i Omega'
and no differentiation of the later divisor L^2. Its listed tuples exhaust
all terms. In a product of four tuples m=d_*+b_0+2e_0, so the separate
Omega, Omega', Omega'' estimates give both |w|=O(ell^(-d_*)) and
|w'|=O(ell^(-d_*)/H), without dividing by any possibly zero factor.

For a fixed rational rho=a_0/b_0 the series supported on b_0 n retains
absolute convergence to the right of one and subpolynomial coefficients.
Thus the cited modified-Gonek theorem applies with the fixed integer
q=a_0 and delta=1/20. Its additive phase has cutoff b_0 n<=Va_0/(2pi).
The fourfold divisor count is bounded by X(1+log X)^3; multiplying by
(log X)^(d_*) bounds its complete coefficient sum. Subtracting the two
source primitives bounds every partial interval [H,V] by
O_N(H ell^(d_*+3)+H^(11/20)). Partial summation includes its boundary
term and the entire variation of w, giving O_N(H ell^3). The opposite
gamma branch is O(1) before that operation and is included. No fast
gamma factor has been placed into the slowly varying coefficient.

The audited L391 interpolation/Cauchy estimate has
sigma-1/2+4B_0(sigma)=13/18-sigma/9<=2/3 on [1/2,21/20].
The carrier-free exponent 4B_0(sigma) is also at most 2/3. All logarithmic
derivative factors are cancelled by the scalar bound; hence both connectors
are O_N(H^(2/3)), including disks at both height endpoints. On the displaced
line the second projection is O_N(1) pointwise by absolute convergence,
so its long edge is O_N(H). Zeta and gamma poles lie outside this rectangle,
and the inherited R and Log branches are holomorphic there. This proves
both bounds (9) for the changed full polynomials, without reusing L390's
failed absolute O(H^2) estimate.

**Four-jet functional and every matrix entry.** L393 (5) applies to each
of the fifteen quartic monomials: all orders are at most two and the total
is at most eight. At fixed head and width the reduced twists eventually
satisfy the Hughes–Young size condition; T_0 is a fixed multiple of H.
The six-term total, including all swaps and finite Euler factors, is
holomorphic. Its scaled nested Cauchy circles are separated, so all required
derivatives retain O_N,w(H ell^3)+O_N,w(H^(13/16)) error. The leading
ordinary jet operators retain i^j and (-i)^j and the carrier 1/2; L/ell
replacement and Omega' terms have the same absolute O(H ell^3) bound.
Complement pairing in the complete centered kernel kills odd total order,
not individual singular summands. Thus all fifteen monomials are covered
by the nine nonzero values in the table and six zero values.

Here is an entrywise check in terms of that table. Temporarily denote its
nine moment values, in the printed order, by m_0,...,m_8. Define

    F_s(A,B,C,D)=3A/128+5B/16-3C/8+3D/8,
    F_t(A,B,C,D)=A/128+7B/16-C/8+D/8.

The four potentially nonzero upper entries of C_uu, in order
(00),(02),(11),(22), are F_s applied respectively to

    (m_0,m_1,m_2,m_3), (m_1,m_3,m_4,m_5),
    (m_2,m_4,m_6,m_7), (m_3,m_5,m_7,m_8).

Replacing F_s by F_t gives the four corresponding C_vv entries.
Their (01),(12) entries vanish by odd-order parity. The nine C_uv entries
have just four nonzero positions: (01),(10) both equal m_4/4-m_2/16,
and (12),(21) both equal m_7/4-m_4/16; the other five vanish by parity.
These formulas check all 21 upper entries, including the cross-block
factor two of theta^T C theta. Substitution gives exactly (2).
In particular its first diagonal is the full signed sum (11), not a
positive term selected from that sum.

The script was inspected and rerun with exact Fraction arithmetic. It
forms V/C_I by exact polynomial division, expands all exponential degrees
0 through 12, verifies cancellation below degree four and at odd degrees,
and multiplies Taylor coefficients by every derivative factorial. It then
integrates every signed term of P and reconstructs the matrix with the
off-diagonal factor 1/2. The complete 66 contribution rows, matrix, all
division checks, three zero polynomial residuals, six pivots and full LDL
identity residual were inspected, not just a preview or success message.
The certificate reproduces the displayed triangular factors and pivots.
Their exact congruence has one positive and five negative pivots, all
nonzero; determinant-one triangular factors therefore prove inertia (1,5,0).
It also reproduces -281/604800 on the L400 subdirection. That contrast
is not a mathematical premise for the positive sign, and no new DAG input
is required. A trivial nullspace does not exclude nonzero isotropic vectors.

**Arithmetic collisions, endpoints and all limits.** Expanding Z_N^2 first
gives the ordered-product multiplicities b_(m,N). Reducing each (m,n) by
its gcd retains every ratio collision; all six terms have the same
zero-shift factor B(h_0,k_0)/(sqrt(h_0 k_0) zeta(2)). Thus (12) has Psi_N,
not a product of separate means or L394's smaller arithmetic scalar.
For the signed polynomial, nonnegative bracketing would be invalid.
Instead the untwisted formula applied to x^4,y^4,z^4 with b_delta gives
an absolute endpoint limsup O_(u,v)(delta), since each leading constant
is positive and integral b_delta=O(delta H). Its constant is independent
of N. The theorem error can depend on delta, which is held fixed until
after the height limit. This justifies the sharp fixed-head limit even
for a negative or zero q_theta.

Each of the three harmonic integrands is a bounded-degree product of
four response values times a quartic in the jets. Telescoping those four
values gives the uniform absolute error C_(u,v) eta_N U^2, and hence
C_(u,v) eta_N ell^4 in each sharp mean. No derivative tail is needed at
this stage: all such errors are already in the physical O(U/L) remainder.
The arithmetic bound 16(mn)^(-3/2) is summable and dominates all Psi_N
terms, so Psi_N tends to Psi>=1. For any tolerance, first fix N making
the full-tail and arithmetic-limit errors small; at that fixed N remove
endpoints by a fixed sufficiently small delta and then a sufficiently
large height. This is equivalent to the displayed sequential limits.
Together with (9) it proves (1) for all real H tending to infinity,
without a rate for N growing with H or a uniform-in-width source error.

**Consequence and limits of the result.** For u=(1,0,0), v=0, (1) has
the strictly positive coefficient Psi/(71680 pi^2 zeta(2)). The exact
weight a^2 x^2 is everywhere nonnegative. Therefore a positive sharp
integral forces Delta>0 somewhere in each sufficiently high dyadic
interval, and the positive denominator transfers that sign to physical D.
This excludes eventual D<=0, a premise of the conditional count route;
it does not refute its conditional theorems. It does not locate common
zeros, give a positive-regulator pencil sign, or sign F's Laguerre form.
The total L367 margin, actual common-zero upper counts, low-index signs,
global mixed positivity and RH remain unresolved. No thresholds or
constants are made effective by this audit.

## Mathlib

Full matching Mathlib coverage for the twisted shifted fourth moment,
signed modified-Gonek primitive, these Hardy-jet moments and (1) is not
checked. Supporting polynomial arithmetic, Sylvester inertia, Cauchy
differentiation, contour integration and dominated convergence do not by
themselves formalize the imported analytic inputs. No Lean verification,
library absence, certified originality or RH resolution is claimed.
