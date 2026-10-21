# Lemma 394: every nonzero fixed quadratic jet weight has negative discriminant mean

## Hypotheses

Use the fixed actual functions and ordinary height derivatives of L390:
L=log(2+t), f=F_0/A, x=f, y=f'/L, z=f''/L^2,
Z=zeta(5/2+it), E=R^2, c=1/(4pi), and the complete physical
normalized discriminant Delta, including envelope curvature. Let
v=(v_0,v_1,v_2) be a fixed real vector, independent of H, and put
p_v=v_0 x+v_1 y+v_2 z. H tends to infinity through positive real values.
No RH, simplicity, noncoincidence, independent phases, growing twists,
or eventual discriminant sign is assumed.

For coprime positive h,k let

    B(h,k)=product_(p^e || hk) [1+e(p-1)/(p+1)],
    J=sum_(m,n>=1) (mn)^(-5/2) B(m/g,n/g)/sqrt((m/g)(n/g)),
    g=gcd(m,n).

B is the finite Euler factor in L393, not a statistical model.

## Conclusion

With ell=log H,

    (1/H) integral_[H,2H] Delta(t) p_v(t)^2 dt
        = gamma_v ell^4+o_v(ell^4),
    gamma_v=(c^2 J/zeta(2)) v^T C v,

where the full real symmetric matrix is

    C = [ -11/10080          0           131/1814400
               0       -17/259200             0
           131/1814400       0          -533/79833600 ].       (1)

J is absolutely convergent and J>=1. C is strictly negative definite.
Hence gamma_v<0 for every nonzero v; gamma_0=0. No fixed real vector
satisfies the proposed gamma_v>0 test. This stops that implementation,
not the possibility of positive Delta at some heights. This local
REPRODUCTION of known-source tools passes the separate critical audit below.
No eventual physical sign, positive-part bound, common-zero estimate,
actual-theta positivity range, RH candidate or new source theorem follows.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-11-positive-weighted-discriminant-mean.md`.
Reuse its inspected source coverage and audited L390/L391/L393.
The imported primary inputs are Hughes--Young, *The twisted fourth
moment of the Riemann zeta function*, J. reine angew. Math. 641 (2010),
203--236, [arXiv:0709.2345v2, Theorem 1.1, (12)--(17), pp. 4--5](https://arxiv.org/pdf/0709.2345v2#page=4);
Bui--Hall, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1, Theorem 3](https://arxiv.org/html/2304.05178v1);
the fixed-right-line modified-Gonek lemma in Sourmelidis--Steuding--Suriajaya,
[arXiv:2007.14008v2, Section 3 between (35) and (36)](https://arxiv.org/html/2007.14008v2#S3);
and Bourgain's unconditional subconvex bound,
[arXiv:1408.5794v2, Theorem 5 (0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2).
None is reproved. The changed polynomial and signed endpoint specialization
are necessary: L391's particular projection and L393's nonnegative square
bracket are not conclusions for this signed weighted statistic.

### Physical replacement and complete tails

Set U=x^2+y^2+z^2. By audited L390,

    d=c^2(M|Z|^2+Re(K E Z^2)),
    M=z^2/2+3xz/4+x^2/32-y^2/2,
    K=((z-x/4)-iy)^2/2,
    ||Delta-d||_(2,H)=O(ell),
    (1/H) integral U^2=O(ell^4).

Here ||.||_(2,H) is the normalized dyadic L2 norm. Since
p_v^2<=|v|^2 U, Schwarz gives

    |(1/H) integral (Delta-d)p_v^2|=O_v(ell^3).        (2)

This retains all ordinary response derivatives and the envelope curvature
already in L390; it is valid at zeros and requires no relative margin.
For Z_N=sum_(n<=N)n^(-5/2-it), eta_N=sum_(n>N)n^(-5/2),
|Z|,|Z_N|<=zeta(5/2), |Z-Z_N|<=eta_N, and |M|+|K|<=CU.
Thus both balanced and projected full-minus-head errors, after multiplication
by p_v^2, have absolute value at most C_v eta_N U^2. Their sharp means
are at most C_v eta_N ell^4, uniformly in N and large H. Fixed heads
are taken before height limits. No growing-twist source theorem is used.

### The changed carrier is lower order

On the real interval conjugate K=((z-x/4)+iy)^2/2 and conjugate E=E^(-1).
Use L391's exact holomorphic ordinary jets, s=1/2+i tau,

    (x,y,z)=-R(D_0,D_1,D_2),
    D_0=h_0,
    D_1=i(h_1+Omega h_0)/L,
    D_2=(-h_2-2Omega h_1-Omega^2 h_0+iOmega' h_0)/L^2,
    h_j=zeta^(j)(s), R'/R=iOmega.

Divisors are applied after differentiation. In the conjugate of
K p_v^2 E Z_N^2 the four critical factors contribute R^4=E^2;
the net carrier is E, and the changed polynomial is exactly

    P_v(D)=((D_2-D_0/4)+iD_1)^2
                     (v_0D_0+v_1D_1+v_2D_2)^2/2.     (3)

Consequently that conjugate has extension E P_v(D) conjugate(Z_N)^2,
where the last factor means the analytic extension of its real-line values.
For fixed N it is a finite sum of positive integer twists r^(it), r=mn,
with coefficients (mn)^(-5/2), 1<=m,n<=N. In s coordinates the twist
is r^(s-1/2). There is only this k=1 harmonic, and no k=2 term.

Every monomial of (3) is a product of four D factors, each of order at
most two. On L391's rectangle, its expansion is w(tau) product_j h_(a_j)(s),
0<=a_j<=2, d=sum a_j<=8. Each constituent scalar is a constant times
Omega^b(Omega')^e/L^m with m=d+b+2e, hence

    |w|=O_v(ell^(-d)), |w'|=O_v(ell^(-d)/H).

These estimates follow from the exact jet expressions and the separately
controlled Omega,Omega',Omega'' bounds in L391, including at their zeros.
They cover every term of the changed polynomial, regardless of its signs.

Exactly E=chi(1-s)=(2pi)^(-s)Gamma(s)
[exp(-pi i s/2)+exp(pi i s/2)]. On Re s>1 the product of four h factors
has absolute convergent coefficients c_a(n), with
|c_a(n)|<=d_4(n)(log n)^d for n>=2 and the separately included n=1 term.
They are O_eta(n^eta) for every eta>0. For fixed integer r the imported
modified-Gonek theorem applies with q=r to r^s product h_(a_j)(s),
on the fixed line a=21/20. Its two branches give, uniformly H<=V<=2H,
a primitive O_(r,a_j)(H ell^(d+3)+H^(11/20)). Here the main sum is
bounded using sum_(n<=X)d_4(n)<=X(1+log X)^3; the positive exponential
branch is O(1). These are precisely the fixed integer q, fixed positive
delta=1/20 and subpolynomial coefficient hypotheses of the cited lemma.
Partial summation with w gives O_(N,v)(H ell^3).

Both sharp connectors are included. L391's audited consequence of Bourgain,
strip interpolation and Cauchy is

    |h_j(sigma+it)|<=C_j ell^j H^B(sigma),
    B(sigma)=(5/18)(11/10-sigma),
    1/2<=sigma<=21/20, j<=2,
    |chi(1-s)|<=C H^(sigma-1/2).

Thus every term of (3), after its coefficient normalization, is bounded
on each connector by C_(N,v) H^[sigma-1/2+4B(sigma)]
<=C_(N,v) H^(2/3). Their fixed lengths give O_(N,v)(H^(2/3)).
All factors are holomorphic on the same pole-free rectangle, with the
Log(2+tau) and R branches fixed as in L391; no residue is crossed.
Taking the real part after contour transfer proves

    (1/H) integral_[H,2H] p_v^2 Re(K E Z_N^2)
        =O_(N,v)(ell^3)=o_(N,v)(ell^4).              (4)

The uniform tail inequality above implies the complete version is o_v(ell^4)
by first taking the height limsup for each N, then sending N to infinity.
This specializes the general method, not L391's specific polynomial identity.

### Balanced coefficient with every gcd collision

Use L393's four-jet formula (5). Its imported Hughes--Young hypothesis check
uses fixed coprime twists, four complex shifts O(1/ell), fixed relative-width
smooth nonnegative weights in [H/2,4H], T_0 a fixed multiple of H, and
hk<=H^(2/11-epsilon) eventually. With epsilon=1/16 its theorem error is
O_(h,k,w)(H^(13/16)). The complete six-term holomorphic kernel, not singular
individual pieces, is differentiated on the nested scaled Cauchy circles.
All four orders are at most two. This applies unchanged to M p_v^2.

Let mu(x^a y^b z^d) be the complete kernel derivative for the assigned four
orders (0 repeated a, 1 repeated b, 2 repeated d), with a+b+d=4.
The even-total-order values in L393 are

    mu(x^4)=1/12, mu(x^3z)=-1/240,
    mu(x^2y^2)=1/720, mu(x^2z^2)=1/4032,
    mu(xy^2z)=-1/20160, mu(xz^3)=-61/3628800,
    mu(y^4)=1/6720, mu(y^2z^2)=19/3628800,
    mu(z^4)=17/10644480.

All remaining quartic monomials have odd total height order. Their derivatives
vanish: in L393 (4) complementing each two-element selection changes the
centered linear form to its negative and leaves its four-factor denominator
unchanged. The whole holomorphic kernel is even under u->-u. This is exact
kernel symmetry, not a probabilistic symmetry or independence assumption.

Write C_ij=mu(M X_i X_j), (X_0,X_1,X_2)=(x,y,z). Retaining all terms gives

    C_00=1/384-1/320-1/1440+1/8064=-11/10080,
    C_02=-1/7680+1/5376+1/40320-61/7257600=131/1814400,
    C_11=1/23040-1/26880-1/13440+19/7257600=-17/259200,
    C_22=1/129024-61/4838400-19/7257600+17/21288960
        =-533/79833600,
    C_01=C_12=0.                                    (5)

The coefficient of v_0v_2 in mu(Mp_v^2) is 2C_02, as required by v^T C v.
For a fixed head, |Z_N|^2 sums all ordered pairs (m,n), 1<=m,n<=N,
with coefficient (mn)^(-5/2) and twist (m/n)^(-it). Reducing each pair by
its exact gcd gives

    J_N=sum_(m,n<=N) (mn)^(-5/2) B(m/g,n/g)/sqrt((m/g)(n/g)).

L393 (5), applied to every monomial, gives for permitted smooth w

    integral w M p_v^2 |Z_N|^2
       =ell^4 [J_N/zeta(2)] v^T C v integral w
                        +o_(N,v,w)(H ell^4).        (6)

The arithmetic factor is for |Z_N|^2, not the |Z_N|^4 factor of L393's
square. Every repeated reduced ratio and diagonal pair is retained.

### Signed endpoints and head limit

Direct nonnegative bracketing of the signed integrand in (6) is unavailable.
For fixed 0<delta<1/8 choose 0<=w_delta<=1, supported in [H,2H], equal to
one off endpoint strips of width delta H, with derivatives
O_(j,delta)(H^(-j)); its integral is H(1+O(delta)). Choose a smooth
nonnegative b_delta majorizing those strips, supported in their fixed-width
enlargements within [H/2,4H], with integral at most C delta H and the same
kind of derivative bounds. Nonnegative smooth bumps give both constructions.

Uniformly in N, |M p_v^2 |Z_N|^2|<=C_v U^2 and
U^2<=3(x^4+y^4+z^4). Applying the untwisted four-jet formula with b_delta
to each of these three nonnegative powers gives

    limsup_(H->infinity) (H ell^4)^(-1) integral b_delta U^2
       <= (3/zeta(2))*(1/12+1/6720+17/10644480)
                   limsup_(H->infinity) integral b_delta/H
       <= C delta.                                  (7)

The explicit moments are positive and the source hypotheses hold at each
fixed width. This controls the absolute signed endpoint error. At fixed
N,delta apply (6) with w_delta, use (7), take H->infinity, then delta->0.
The sharp mean coefficient is therefore [J_N/zeta(2)]v^T C v. No width-uniform
theorem error is needed; a whole-interval O(H ell^4) alone would not prove (7).

B(h,k)<=tau(h)tau(k)<=tau(m)tau(n) for reduced h=m/g,k=n/g. Since
tau(n)<=2sqrt(n), every J summand is at most 4(mn)^(-2). This is summable,
so J_N->J<infinity by positive monotone convergence; the m=n=1 term is one.
The uniform O_v(eta_N ell^4) balanced-tail bound then transfers the sharp
mean to full Z: after taking the height limsup at fixed N the normalized
error is at most C_v eta_N plus
|v^T C v| |J_N-J|/zeta(2), which tends to zero. Together with (2), (4)
and the factor c^2 this proves the stated complete weighted asymptotic.

### Strict matrix sign and scope of the obstruction

The x,z block determinant is

    C_00 C_22-C_02^2=853/411505920000>0.

Both its diagonal entries are negative, and C_11<0, with the two y cross
entries zero. Equivalently the leading principal minors of -C are

    11/10080,
    187/2612736000,
    14501/106662334464000000,

all strictly positive. Sylvester's criterion proves -C positive definite.
Since c^2 J/zeta(2)>0, gamma_v<0 for every nonzero fixed v.

The exact finite reproduction command is
`python3 scripts/discriminant/check_weighted_coefficient.py`;
its full certificate is `scripts/discriminant/weighted-coefficient-certificate.json`.
It constructs the six-term alternating kernel, checks exact Vandermonde
division through exponential degree twelve, low/odd cancellations and
permutation symmetry, and records every contribution to all six entries
and their exact principal minors. The full entry tables and division checks
were inspected. Zero arithmetic failures were reported. The analytic
moment, carrier, physical, endpoint and tail proofs above are essential;
the script certifies none of them.

The achieved threshold is gamma_v<0 for v!=0, against the sought gamma_v>0.
This supplies a complete obstruction to this fixed quadratic-weight test,
not to arbitrary weights or positive physical discriminant values. It
changes no eventual sign or global positivity conclusion. The independent
RH gaps remain unresolved; the separate critical audit below validates
only the stated fixed-weight obstruction.

### Separate critical audit — 2026-10-11, step 57

This is a REPRODUCTION proof audit under the prior SPECIALIZE assessment
`drafts/literature/2026-10-11-fixed-quadratic-weight-audit.md`. Its exact
target is the existing full asymptotic and negative-definite coefficient.
The source statements and essential proof cases recorded in that assessment
are reused without a new discovery search. The Hughes--Young, Bui--Hall,
modified-Gonek and Bourgain inputs are precisely those cited above; none
is reproved. The audited physical reduction in L390, ordinary-jet and
primitive estimates in L391, and general four-jet formula (5) in L393
remain within their fixed-order, fixed-twist hypotheses. No additional
mathematical input or assumption is introduced by this audit.

**Physical replacement and its scale.** On [H,2H], L is comparable to ell.
The exact L390 response triple includes derivatives of the whole response
series and the gamma carrier before division by T^2 L^j. Its pointwise
error is O(U/L); the common-envelope correction is retained and bounded
by O(U/(T^2 L^2)). Together with ||U||_(2,H)=O(ell^2) these give
||Delta-d||_(2,H)=O(ell). Also p_v^2<=|v|^2 U, so
||p_v^2||_(2,H)<=|v|^2||U||_(2,H)=O_v(ell^2). Schwarz proves exactly
the O_v(ell^3) error in (2), smaller than the required ell^4 scale.
This argument divides by no jet or function value and works at zeros.

For either balanced or projected terms,
||Z|^2-|Z_N|^2| and |Z^2-Z_N^2| are at most
2 zeta(5/2) eta_N. Multiplication by |M|+|K|<=CU and
p_v^2<=|v|^2 U bounds their absolute errors by C_v eta_N U^2.
This uniform estimate is obtained before taking a height limit; it
contains no N-dependent moment constant. The response-derivative errors
are already in Delta-d, rather than silently discarded in this last tail.

**Changed carrier and the complete primitive.** Because p_v is real on
the original line, conjugating its projected statistic gives exactly
p_v^2 conjugate(K) E^(-1) conjugate(Z_N)^2. Replacing the four critical
jet factors by -R D_j supplies R^4=E^2. Thus the net carrier is E and
the remaining polynomial is precisely (3), including its factor 1/2,
the +iD_1 sign and the two factors of the linear combination. There is
no extra factor two when the real part is restored, and no k=2 harmonic.
Every head pair contributes the positive integer twist r=mn; in s
coordinates its constant r^(-1/2) is absorbed into the fixed coefficient.

Expand the polynomial using the exact D_j, not derivatives of normalized
divisors. In each scalar Omega^b(Omega')^e/L^m the identity
m=d+b+2e follows term by term from D_0,D_1,D_2. The separate bounds
Omega=O(ell), Omega'=O(1/H), Omega''=O(1/H^2), L'=1/(2+tau)
therefore give |w|=O_v(ell^(-d)) and
|w'|=O_v(ell^(-d)/H), even when a factor Omega vanishes. The product
of four zeta derivatives has coefficients bounded by d_4(n)(log n)^d,
with the n=1 term explicitly interpreted. Absolute convergence on
Re s>1 and subpolynomial coefficient growth meet the modified-Gonek
hypotheses on a=21/20 for each fixed integer q=r. Its two branches
produce the entire primitive, bounded by
O_(r,a_j)(H ell^(d+3)+H^(11/20)) for every H<=V<=2H.
The elementary d_4 summatory bound controls the theorem's additive-phase
output; it is not an absolute bound on the original oscillatory integrand.
Partial summation includes both boundary terms and the full coefficient
variation, giving O_(N,v)(H ell^3).

On the two connectors all derivative powers ell^d cancel their coefficient
normalizations. L391's audited interpolation/Cauchy estimate then gives
the exponent sigma-1/2+4B(sigma)=13/18-sigma/9, whose maximum on
[1/2,21/20] is 2/3. Their fixed lengths yield O_(N,v)(H^(2/3)),
also smaller than H ell^4. This uses the complete chi(1-s), with its
two-exponential identity on the shifted line, and the same pole-free
rectangle and holomorphic branches as L391. No omitted residue or sharp
endpoint remains. These checks verify (4) for the changed polynomial;
L391's original MK identity was not imported as that conclusion.

**Full balanced coefficient and exact finite evidence.** The new balanced
polynomial M p_v^2 is homogeneous of degree four. Assigning two of its
four ordinary jets to each height orientation puts every monomial within
L393 (5), with order at most two per factor. The fixed reduced twists
eventually meet Hughes--Young's size condition; each fixed relative-width
smooth weight meets its support and derivative conditions. The complete
six-term kernel is differentiated on the separated scaled Cauchy circles
already justified in L393, with no extra unnormalized log factors or
evaluation of singular individual terms. Jet and local-factor errors
are O_(h,k,w)(H ell^3), and the theorem error is
O_(h,k,w)(H^(13/16)), both o(H ell^4).

The finite script was read and rerun. Its signed Vandermonde construction
checks division by multiplication for every exponential degree zero
through twelve. Degrees below four vanish; complement pairs give zero
at every odd exponential degree. The surviving kernel polynomials are
permutation symmetric. The complete `/entries` and `/division_checks`
values of the canonical certificate were inspected with
`python3 ../scripts/loop/inspect_json.py` using `--full` for those selected
fields, as were all three leading principal minors of -C. The six entry
tables include every term, including all eight zero contributions in
C_01 and C_12. The nonzero derivatives and their factorial conversion
agree with L393 (6)--(7). In particular the xz entry sums four signed
contributions, and its contribution to the polynomial in v is twice
C_02. No coefficient, odd-order term or off-diagonal factor is omitted.
The rational totals are exactly (1) and (5). The x,z block determinant
is 853/411505920000 and the three principal minors are the positive
numbers printed above. Sylvester's criterion verifies strict negative
definiteness. Zero arithmetic failures were reported. The finite check
does not certify any source theorem or analytic limit.

Expanding |Z_N|^2, rather than |Z_N|^4, gives exactly one coefficient
(mn)^(-5/2) for each ordered pair m,n<=N. Reduction by its gcd retains
every diagonal and every repeated reduced ratio. L393 (5) supplies
B(h,k)/(sqrt(hk) zeta(2)) for each pair, so the arithmetic factor is
J_N as written, without the tau(m)tau(n) factors of the square statistic.
It is positive. Since h divides m and k divides n,
B(h,k)<=tau(h)tau(k)<=tau(m)tau(n)<=4sqrt(mn). Dropping the reduced
sqrt(hk) denominator gives the summable majorant 4(mn)^(-2).
Consequently J_N increases to the finite J>=1 with no conditional sum.

**Signed endpoints and limit order.** The signed balanced polynomial
cannot use L393's nonnegative whole-polynomial brackets. Here the
absolute bound C_v U^2 is uniform in N. A smooth nonnegative endpoint
majorant b_delta has integral O(delta H) and permitted derivatives at
each fixed delta. Its support stays in [H/2,4H]. Applying the untwisted
four-jet formula to x^4,y^4,z^4 individually proves (7), because their
leading moments 1/12, 1/6720, 17/10644480 are positive and
U^2<=3(x^4+y^4+z^4). Thus the absolute endpoint error after division
by H ell^4 has height limsup O_v(delta). Merely knowing a dyadic
O(H ell^4) norm would not have supplied this vanishing strip estimate.

At fixed N and delta apply (6), then take H to infinity. The deviation
of integral w_delta/H from one and the endpoint error are both
O_(N,v)(delta). Sending delta to zero next gives the sharp fixed-head
coefficient J_N v^T C v/zeta(2). Sending N to infinity last is legitimate
by the uniform C_v eta_N tail and the convergent positive J_N series.
In particular for B_H=H^(-1) integral_[H,2H] M p_v^2 |Z|^2 the
normalized limit satisfies

    limsup_(H->infinity)
      |B_H/ell^4-(J/zeta(2))v^T C v|
      <= C_v eta_N + |v^T C v| |J_N-J|/zeta(2).

The right side tends to zero. The same fixed-head/height/head argument
annuls the projected statistic using (4). Restoring c^2 and the smaller
physical error (2) proves the claimed complete asymptotic. All statements
hold for fixed real v and all sufficiently large real H; no uniformity in
growing v, head, twist or shrinking smoothing width has been inferred.

The full weighted asymptotic and strict negative-definite coefficient
pass unchanged. This validates the local known-tool obstruction to the
sought positive leading quadratic direction. The earlier O(H^2) absolute
contour failure remains independently valid and is not a premise here.
Neither the audit nor the obstruction gives eventual D sign, an actual
positive-discriminant witness, a common-zero upper count, total L367
margin, a new actual-theta positivity range or an RH conclusion.

## Mathlib

Full matching Mathlib coverage for this weighted asymptotic, Hughes--Young,
modified-Gonek and Bourgain is not checked. Finite rational arithmetic,
Sylvester's criterion, Schwarz, contour integration and dominated convergence
are supporting facts, not a matching implementation of the analytic inputs.
No Lean verification, library absence or mathematical novelty is claimed.
