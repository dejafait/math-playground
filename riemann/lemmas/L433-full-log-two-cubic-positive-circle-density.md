# Lemma 433: the full fixed log-2 cubic sequence has a positive circle density

## Hypotheses

Use the actual complete physical Delta and Bcal, ordinary critical jets,
response and normalizations of L406--L409 and L432. Set
c=1/(4pi), kappa=17c^3/20160, ell=log H and
E_H=H^(-1) integral_[H,2H]. Let beta>0 be L409's coefficient.
For each integer j>=0 take the real-H limit with j fixed. Each response
head N is also fixed in its inner height limit. No uniform estimate for
growing j, RH, clipping, conditional actual law or regulator margin is
assumed. Write num(r) for the reduced numerator of a positive rational
r, and A_u=u^(-2) sum_(a=1)^u gcd(a,u).

Reuse the arbitrary fixed-rational interface in L408, the explicit
frequency bounds in L409/L430, L431's local valuation factorization,
and L432's audited finite-prefix transfer template. The prior SPECIALIZE
assessment is `drafts/literature/2026-10-18-prime-two-cubic-generating-density.md`;
its covered target is this infinite-sequence analytic sign attempt.

## Conclusion

For every separately fixed integer j>=0,

    E_H[Delta Bcal cos(j t log 2)]=g_j ell^2+o_j(ell^2),       (1)
    g_j=(kappa/2) sum_(m,n,k>=1) (mn)^(-2) k^(-3)
          [2^(j/2) A_num(2^j mn/k)
                         +2^(-j/2) A_num(mn/(2^j k))].       (2)

Each sum is absolutely convergent, and g_0=beta. Set c_j=g_j/beta
and c_(-j)=c_j. The entire bilateral sequence is absolutely summable.
It is the Fourier sequence, with normalized Haar measure dtheta/(2pi),
of the following strictly positive, continuous, even probability density:

    B_0=571520/329623,
    w(theta)=128[9-5sqrt(2)cos(theta)] /
       {B_0[3-2sqrt(2)cos(theta)]^2[33-8sqrt(2)cos(theta)]^2}.
                                                                  (3)

In particular w(theta)>8/6075 for every real theta. Its cosine moments
are c_j for every j>=0; its sine moments are zero. This is the unique
finite symmetric circle measure with these cosine moments. Every finite
Toeplitz section of this sequence is strictly positive definite, as a
consequence of the full density, not an extrapolation of finite minors.
The analytic function F(z)=1+2 sum_(j>=1)c_j z^j has positive real part
throughout the open unit disk and boundary real part w.

Thus the full single-prime cosine family supplies no positive-measure
obstruction to a nonnegative intermediate mass. No mass is implemented
in a new law here. Other constraints need not survive that change, and
no actual sine-weighted coefficient, conditional physical distribution,
growing-frequency estimate, actual clipping, capped nondegeneracy,
full-error regulator margin, global mixed positivity or RH consequence
is asserted. This is local REPRODUCTION of assessed analytic interfaces
and harmonic-analysis tools with an arithmetic specialization; originality
beyond the sources checked is not asserted. The separate step-229
critical audit below validates this specialization with its stated scope.

## Proof

The relevant source comparison and local duplicate/failure checks are
recorded in the prior assessment. L432's finite-prefix stop and
L427/L428/L430's narrower failures are retained. Only the approved
analytic alternative is attempted. There is no new Toeplitz cutoff,
new law construction or reproof of a general moment theorem.

### 1. Extension of the physical coefficient to each fixed harmonic

Fix an arbitrary integer j>=0. L407's carrier expansion, as used in
L430 and L432, is multiplied exactly by
cos(j t log 2)=(2^(jit)+2^(-jit))/2. For alpha=(mnk)^(-5/2),
the single-carrier twists are r=a0 mn/k and the zero-carrier twists
are r=a0 mnk, with a0=2^j,2^(-j), each of weight alpha/2.
For j=0 the coincident characters still have total weight one.
The exact ordinary-jet weights are unchanged; in particular the
characters enter r^(s-1/2), not a discarded derivative of a weight.

At fixed N these are positive fixed rationals. L408 (12) gives, for
reduced r=u/v and a monomial nu of total derivative order D<=6,

    S_(r,nu,w)=H ell^2 sqrt(r) A_u a_nu m_nu
                                    +o_(r,nu)(H ell^2),
    m_nu=(-1)^D product_(i=1)^3 p_i!/(D+2)!,
    sum_nu a_nu m_nu=17/20160.                              (4)

The cited primary progression input is A. Fazzari, *A Voronoi summation
formula for the shifted triple divisor function*, arXiv:2306.15553v1,
[(3.5)](https://arxiv.org/html/2306.15553v1#S3), combined with the
residue-one Hurwitz pole in [DLMF 25.11(i)](https://dlmf.nist.gov/25.11#i)
and continuation [DLMF 25.11.5](https://dlmf.nist.gov/25.11.E5).
Its additive numerator is -v, modulus u, and (-v,u)=1. All classes,
including nonunits and the zero class, are retained. The finite residue
sum is u^(-3) sum_(a,b,c=1)^u exp(-2pi i vabc/u)=A_u.
L408's already audited smooth-first argument and absolute endpoint
majorants give (4) at sharp endpoints. Its scope is every fixed
positive rational, so no new uniform-modulus theorem is required.
The real projection leaves this real coefficient unchanged. Using
alpha sqrt(r)=sqrt(a0)(mn)^(-2)k^(-3) gives the head of (2).

For clarity, all dependence on the arbitrary fixed j in the complete
passage is checked next; merely extending L432's conclusion by notation
would not establish (1). Use a=21/20, delta=11/20, eta=1/100.
On the shifted rectangle tau=t-iq, 0<=q<=delta, twists have
modulus r^q. Response convergence is normal on a neighborhood because
-3/2<q<3/2 is the allowable open interval for all response exponents.
Each of the two fixed characters preserves that convergence.
L409/L430's bounds for both sharp connectors are

    C(1+r^delta)H^(71/120) (single carrier),
    C(1+r^delta)H^(1/2) (zero carrier).                     (5)

The primary kernel is Milinovich--Ng, *Lower bounds for moments of
zeta'(rho)*, [Lemma 6.1, p. 9](https://home.olemiss.edu/~mbmilino/Lower_Bounds.pdf#page=9),
for x>0, with abscissa in a fixed compact subinterval of (0,2].
The saddle, endpoint and exterior cases are covered by Gonek, *Mean
values of the Riemann zeta-function and its derivatives*, Invent. Math.
75 (1984), [section 3, Lemma 2, p. 130](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=8).
Use x=l/r and subtract primitives at H and 2H. Integration by parts
uses the exact weight bounds |w|<=C ell^(-D) and
|w'|<=C ell^(-D)/H. L430 (11)--(12) then bound the weighted
single-carrier error and the absolute arithmetic main sum respectively by

    C[H^(11/20)r^(11/20)
       +H^(1/100)r^(-49/100)(1+log_+r)^D
       +H^(51/100)ell r^(51/100)(1+log_+r)^D],              (6)
    C H sqrt(r)ell^2(1+log_+r)^(D+2).                     (7)

The connector input in (5) uses the fixed-strip subconvex/Cauchy
specialization of Bourgain, JAMS 30 (2017),
[arXiv:1408.5794v2, Theorem 5/(0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2),
already justified in L407/L409. The inspected coverage is reused.

For r=a0 mn/k,
alpha r^q=a0^q m^(-5/2+q)n^(-5/2+q)k^(-5/2-q).
Every q in (5)--(6) lies strictly inside (-3/2,3/2), and
1+log_+(a0 mn/k)<=C_j(1+log m+log n). Thus the response sum
of (6) is O_j(H^(11/20)+H^(1/100)+H^(51/100)ell), and
(5) sums to O_j(H^(71/120)). Each is o_j(H ell^2), uniformly
over subsets of tuples. Equation (7), after alpha multiplication, has
the summable majorant

    C_j H ell^2 (mn)^(-2)k^(-3)(1+log m+log n)^8.            (8)

For the zero carrier r=a0 mnk, put h=2^(-j). All r lie in h Z,
r>=h. The integer resonance l=r occurs always for a0=2^j and
exactly when 2^j divides mnk for a0=2^(-j). Retain its exact term
r^(-1/2)C_nu(r) integral_[H,2H] w_(0,nu)(t-i delta)dt.
The bound |C_nu(l)|<=C l^eta log(2l)^D makes its response sum
O_j(H), since alpha r^(-49/100)log(2+r)^D is summable.

Off resonance, the primitive has absolute bound
2r^delta sum_(l!=r)|C_nu(l)|l^(-a)/|log(r/l)|.
Outside (r/2,2r) it is O(r^delta). Inside, use
|log(r/l)|>=|l-r|/(2r). The nonzero distances are at least h;
the first distance interval costs O(1/h), subsequent unit intervals
have bounded occupancy and harmonic total. Therefore the sum of
inverse distances is O_j(log(2+r)), also in h<=r<1. The resulting
interior primitive is O_j(r^(51/100)log(2+r)^(D+1)). The exact
weight variation costs O(ell^(-D))<=O(1). Both powers 11/20 and
51/100 are summable against alpha for r=a0 mnk, giving O_j(1)
for the nonresonant integrals. Both zero-carrier connectors sum to
O_j(H^(1/2)). The complete zero carrier is consequently O_j(H),
with no omitted denominator-2^j resonance or endpoint saddle.

The vanishing tail of (8) yields

    limsup_(H->infinity)
      |E_H[(d B0-d_N B0_N)cos(j t log 2)]|/ell^2
                                    <=C_j epsilon_N,
    epsilon_N -> 0.                                       (9)

Because 0<A_u<=1, (2) is absolutely convergent at each fixed j.
For any tolerance choose N controlling (9) and that coefficient tail,
then take H large at this fixed N. This gives (1) for d B0.
L406's absolute error O(ell^(5/4)) survives multiplication by a
cosine of modulus at most one and gives (1) for the complete physical
product. H tends through every sufficiently large real value. No
physical asymptotics are summed over j and no j-uniform onset is used.

### 2. Joint absolute convergence and a bilateral generating identity

Put rho=sqrt(2), and define for every integer k

    b_k=1 (k<=0), b_k=2^(-k)(1+k/2) (k>=1),
    B_j=sum_(s,v>=0)(s+1)4^(-s)8^(-v)b_(s-v+j), j in Z.    (10)

L431's multiplicativity and A_(2^e)=2^(-e)(1+e/2), e>=0,
applied to (2), give for each j>=0

    g_j=(kappa T_odd/2)(rho^j B_j+rho^(-j)B_(-j)),
    beta=kappa T_odd B_0,                                 (11)

where T_odd is the same positive finite odd-index sum as in L432.
This use is justified directly by nonnegative Tonelli summation and
the unique powers of 2 in each integer: the odd part of num(mn/k)
is unchanged by either power-of-two twist, even when the odd indices
share factors. Thus it factors out exactly, and cancels in c_j.
The value B_0=571520/329623 is the audited L431/L432 evaluation.

For 1<R<2, the nonnegative series

    sum_(k in Z)b_k R^k
      = R/(R-1) + (R/2)/(1-R/2) + (R/4)/(1-R/2)^2

is finite. Also

    sum_(s,v>=0)(s+1)4^(-s)8^(-v)R^(v-s)
                          =1/[(1-1/(4R))^2(1-R/8)]<infinity.

Their product equals sum_(j in Z)B_j R^j by the bijection
k=s-v+j and Tonelli. In particular it proves the full joint absolute
majorant needed to rearrange (10) and sum its harmonics at every
complex u with 1<|u|<2. The same bounds at compact inner/outer
radii give local uniform convergence. Geometric series and its first
derivative, both used within their domains, now give

    sum_(k in Z)b_k u^k
      =u/(u-1)+u/(2-u)+u/(2-u)^2
      =u/[(u-1)(u-2)^2],
    sum_(s,v>=0)(s+1)4^(-s)8^(-v)u^(v-s)
      =1/[(1-1/(4u))^2(1-u/8)].

Consequently, throughout the annulus 1<|u|<2,

    Q(u):=sum_(j in Z) B_j u^j
      =128u^3/[(u-1)(u-2)^2(4u-1)^2(8-u)].               (12)

There is no pole on |u|=rho. At u=rho the majorant is finite and
all summands are nonnegative. From (11),

    sum_(j in Z)c_j
       = (1/B_0)sum_(j in Z)rho^j B_j=Q(rho)/B_0<infinity. (13)

This proves absolute summability (c_j>=0), including both bilateral
tails, without a truncation or an interchange with a height limit.

For |z|=1, all coefficients B_j are real, and absolute convergence
gives

    sum_(j in Z)c_j z^j
       =[Q(rho z)+Q(rho/z)]/(2B_0)
       =Re Q(rho z)/B_0.                                 (14)

This is the circle-density generating function. It follows from the
infinite identity, not agreement at a finite number of harmonics.
As consistency checks, (10)--(11) at j=0,...,4 reproduce L432's
1, 1161sqrt(2)/1786, 3504/4465,
52201sqrt(2)/114304, 594309/1143040. Those prefix values are
not used to infer (12) or (14).

### 3. Exact whole-circle sign

Set u=rho exp(i theta) and X=Re u=rho cos(theta), so u conjugate(u)=2.
The two identities

    u-2=-u(conjugate(u)-1),
    8-u=u(4conjugate(u)-1)

transform (12) into

    Q(u)=128 /
       {|u-1|^2 |4u-1|^2 (conjugate(u)-1)(4u-1)}.

Multiplying the last two factors by their complex conjugates shows

    Re Q(u)=128 Re[(u-1)(4conjugate(u)-1)] /
                        [|u-1|^4 |4u-1|^4]
      =128(9-5X)/[(3-2X)^2(33-8X)^2].                    (15)

Here the real numerator is exactly 4|u|^2+1-5Re u=9-5X;
no imaginary term is discarded before taking the real part.
Because -sqrt(2)<=X<=sqrt(2), all denominator factors are strictly
positive, including the circle endpoints. The numerator is at least
9-5sqrt(2)>0 (81>50). Equations (14)--(15) prove (3) on the
entire circle. For the stated explicit bound use sqrt(2)<3/2,
B_0<2, 9-5X>3/2, 0<3-2X<6, and 0<33-8X<45:

    w(theta)>128(3/2)/(2*6^2*45^2)=8/6075.                (16)

The strict lower bounds for the two denominator factors follow also
from 3>2sqrt(2) and 33>8sqrt(2). This sign proof uses no plot,
Fourier truncation or finite matrix test.

### 4. Normalization, uniqueness and analytic criterion

The Weierstrass M-test applied to (13) proves uniform absolute
convergence of sum c_j exp(ij theta). Thus termwise integration is
valid. Its integral against normalized Haar measure is c_0=1, and
its Fourier integrals are precisely c_j. Real evenness gives the
stated cosine moments and zero sine moments. Positivity in (16) makes
w dtheta/(2pi) a finite positive probability measure.

Import Zhou--Siadat, *Notes on Harmonic Analysis Part II: the Fourier
Series*, [arXiv:2206.05105v1 (8 June 2022), Theorem 3.5, p. 14](https://arxiv.org/html/2206.05105v1#S3):
a finite complex Borel measure with every Fourier--Stieltjes
coefficient zero is zero. For another finite symmetric measure with
these cosine moments, the sine moments are zero and the difference
has all coefficients zero, so the theorem applies. Any positive
measure with only the specified cosine moments can first be reflected
and averaged; its symmetrization must equal the displayed measure.
Uniqueness of a nonsymmetric measure from cosine moments alone is
not asserted, and no actual physical sine coefficient is assumed.

For any nonzero finite vector v=(v_0,...,v_n), Fourier integration
and (16) give

    sum_(a,b=0)^n conjugate(v_a)c_(a-b)v_b
       =integral w(theta)|sum_(a=0)^n v_a exp(ia theta)|^2
                                                   dtheta/(2pi)
       >=(8/6075)sum_(a=0)^n|v_a|^2>0.                    (17)

The sign convention is immaterial because c_j are real and even.
This establishes all finite sections at once without computing one.

Import Helton--Putinar, *Positive Polynomials in Scalar and Matrix
Variables, the Spectral Theorem, and Optimization* (2007),
[section 3.1, Theorem 3.3(a)--(d), pp. 245--246](https://mathweb.ucsd.edu/~toal/READ07/hpSurvey07.pdf#page=17).
Its finite positive measure, conjugate symmetry and c_0>0 hypotheses
are all verified. Its analytic clause gives positive real part for
F(z)=1+2 sum_(j>=1)c_j z^j in the disk. The series converges
uniformly on the closed disk by (13), and its boundary real part is
(14). Equivalently the cited Herglotz representation uses the kernel
(exp(i theta)+z)/(exp(i theta)-z), whose real part is positive
for |z|<1. The general representation and uniqueness theorems are
imported, not reproved; only their arithmetic specialization is new
to this notebook.

The representing density decides the proposed whole-sequence moment
compatibility question. It does not identify an actual conditional
critical-function law or automatically preserve the selected other
moments when used as a mass. The complete high/bulk comparisons and
all independent clipping, regulator and global positivity gaps remain
as recorded in L432. No sine limit, infinite summation of physical
asymptotics, or uniform-in-j estimate enters this proof.

### Exact algebra check

`python3 scripts/discriminant/prime_two_cubic_density.py` writes the
complete certificate to
`scripts/discriminant/prime_two_cubic_density_certificate.json`.
It uses exact rational Laurent polynomials and independently checks
(15) by substituting conjugate(u)=2/u in (12), adding the conjugate
rational function, and clearing both denominators. The complete
residual polynomial is zero. A second cleared identity checks the
geometric numerator in (12); its complete residual is also zero.
It evaluates L432's convergent-tail formula only at the already
audited prefix and verifies all five exact values, including the odd
sqrt(2) factors, B_0 and the rational sign inequalities in (16).
All nine checks pass; failures=[]. The complete check object, both
residuals, prefix multipliers and global bound were inspected.
Actual global bound >8/6075 exceeds the required nonnegativity
threshold zero. The script verifies finite algebra only: the joint
majorant and fixed-harmonic transfer are the written proofs above.
No increased Toeplitz cutoff or numerical sampling is used.

### Separate critical audit — 2026-10-18, step 229

This RESEARCH / REPRODUCTION / proof_audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-18-prime-two-positive-density-critical-audit.md`.
Reuse the inspected primary hypotheses and proof cases in steps
213/221/226/228 and the audited local interfaces. The audit does not
reprove the general harmonic-analysis or stationary-phase theorems.
The earlier finite-prefix and narrower law obstructions are contrasts,
not premises for the full-circle sign.

**Every separately fixed physical harmonic.** Fix j before H and N.
L407's exact real-part expansion has precisely the two response patterns
mn/k and mnk. Multiplication by the two cosine characters gives the
four patterns stated in section 1, with weights 1/2. At j=0 the two
equal terms add to one, rather than doubling the coefficient. On the
height rectangle their analytic continuations are included in
r^(s-1/2); the slowly varying weights retain their O(ell^(-D)/H)
derivative bounds. The real-line conjugate response is continued by
its opposite Dirichlet series, not by off-line complex conjugation.

For reduced r=u/v, L408's progression decomposition includes all
residue classes. Summing exp(-2pi i vabc/u) over c gives u when
u divides ab and zero otherwise. There are gcd(a,u) choices of b
for each a, so division by u^3 gives exactly A_u. This checks the
reduced-numerator convention, including u=1. The cited Hurwitz pole,
L408's smooth-first absolute endpoint argument and its exact signed
ordinary-jet sum give (4) for every positive fixed rational. Multiplying
by alpha sqrt(r)/2 gives (2), with no additional half from the real
projection. Neither a Schwartz theorem with an indicator substituted
into it nor the excluded expanded polar display is used.

All response continuations converge normally near 0<=q<=11/20.
The connector bounds explicitly retain 1+r^(11/20). In (6) the
three powers are 11/20, -49/100 and 51/100. For each of them the
exponents -5/2+q and -5/2-q are below -1, so both fixed character
scalings are summable with every indicated logarithmic factor.
The frequency kernel's two nearest lattice points include exact
endpoint saddles. Subtracting its H and V primitives and using
|w(2H-i delta)|+integral |w'| therefore covers both sharp endpoints
and weight variation. Constants may depend on j, but not on the
response indices or head N. Every resulting height exponent is below
one, including the connector exponent 71/120.

For zero carrier the common lattice is h Z with h=2^(-j).
The positive character always has integral r; the negative character
has integral r exactly when 2^j divides mnk. Its exact resonance
amplitude on the right line is r^(a-1/2)r^(-a)=r^(-1/2).
The response-summed bound is O_j(H), including r=1. Off resonance,
the first unit distance band costs O(1/h), and subsequent bands have
bounded integer occupancy and harmonic total. This gives
O_j(log(2+r)) for the inverse distances; r in [h,1) causes no
exception. The near-band power is
11/20+(1/100-21/20)+1=51/100; the far-band power is 11/20.
Both are summable against alpha for the product pattern. The entire
zero carrier, including both connectors, is O_j(H). No denominator
resonance or leading-scale contribution has been silently discarded.

The absolute arithmetic main-sum bound (8) has exponents -2,-2,-3
and only fixed logarithms. Its cube-complement mass tends to zero.
Applying the preceding frequency bounds to that complement proves
(9); it does not multiply an already integrated signed error by cosine.
Choose N to control this tail and the absolutely convergent coefficient
tail, then H sufficiently large at that N,j. L406's absolute physical
error divided by ell^2 is O(ell^(-3/4)), and multiplication by a
bounded cosine preserves it. This verifies the complete physical
statistic for every separately fixed j and every sufficiently large
real H, without exchanging a harmonic sum and a height limit.

**Two-sided convergence and normalization.** In unique 2-adic
decomposition the odd reduced numerator is unchanged by either twist,
even when the odd indices share factors. Nonnegative Tonelli summation
therefore gives the same finite positive T_odd in both coefficients
and beta. Its cancellation in (11) is legitimate. The factor s+1
counts all ordered pairs of valuations of m,n; k has weight 8^(-v).
Thus the b_(s-v+j) indices and both signs in (11) are correct.

For any 1<R<2, set k=s-v+j. This is a bijection in j for each
s,v. The joint positive sum becomes the product of sum_k b_k R^k
and sum_(s,v)(s+1)4^(-s)8^(-v)R^(v-s). The negative k tail
requires R>1, the positive tail requires R<2, and the remaining
two geometric sums converge since 1/(4R)<1 and R/8<1. This
establishes an actual absolute majorant before rearrangement. For a
compact subannulus, use the outer radius for j>=0 and inner radius
for j<0 to obtain local uniform convergence. The elementary sums
then give exactly (12), including its constant 128 and u^3 numerator.

At R=sqrt(2) the majorant is finite. Extending (11) symmetrically
to negative j and reindexing its second term gives (13); the factor
1/2 disappears only because the two bilateral sums are equal.
For complex |z|=1 it instead gives the half-sum in (14). These
are distinct operations, and neither loses B_0. The uniform absolute
Fourier series has constant coefficient c_0=B_0/B_0=1. Termwise
integration therefore establishes mass one independently of the sign
calculation. No odd-prime product or finite-prefix agreement supplies
this normalization.

**Whole-circle sign and finite-measure conclusion.** Substituting
conjugate(u)=2/u checks both factorizations preceding (15). After
cancelling u^3, multiplication by the conjugate of the remaining
two factors gives exactly numerator 128(9-5 Re u), with squared
denominators (3-2 Re u)^2(33-8 Re u)^2. On the whole circle,
3-2sqrt(2)>0 and 33-8sqrt(2)>0, so clearing denominators has not
hidden an endpoint zero. Using sqrt(2)<3/2 and B_0<2 gives the
strict lower bound 8/6075 as written. The normalization and this
bound prove a finite positive probability measure, not merely a formal
positive Fourier sequence.

Finite symmetry forces zero sine coefficients. The difference of two
finite symmetric measures with these cosine moments consequently has
every Fourier coefficient zero, exactly the hypothesis of the cited
Zhou--Siadat uniqueness theorem. It would not follow for arbitrary
nonsymmetric measures from cosine data alone. The same positive
density gives (17) by a finite polynomial integral, with a lower bound
independent of the section size. Helton--Putinar's positive-measure,
conjugate-symmetry and positive-mass hypotheses are verified; absolute
summability also gives the claimed continuous boundary real part.
No actual sine-weighted asymptotic is used in any of these deductions.

**Exact evidence and outcome.** Read the complete algebra script,
replayed it, and inspected the complete selected certificate fields:
all checks and failures, both residual polynomials, numerator and
denominator polynomials on both sides, B_0, all five prefix values
and their sqrt(2) parities, and the actual/required global bound.
The substitution u -> 2/u is exactly circle conjugation for rational
coefficients. The cleared real-part identity has the required factor
two, and both complete residuals are zero. All 9/9 checks pass,
failures=[], with actual bound >8/6075 against required >=0.
The certificate path is given above. Its finite algebra is corroborating
evidence; the written joint majorant and physical argument establish
the infinite statements.

No defect or missing direct input was found. The audit validates the
single-prime positive-measure compatibility stop. ADVANCE records
independent validation of this local known-tool specialization, not
novelty beyond the inspected sources or progress on RH's missing sign.
The mathematical argument and direct DAG inputs are unchanged. No law
is implemented; joint arithmetic constraints, actual/global realization,
clipping, capped nondegeneracy and the full-error regulator margin remain
unresolved, as does global mixed positivity.

## Mathlib

Full matching coverage for this physical cubic sequence, the rational
circle density and this specialization has not been checked. The
precisely cited primary harmonic-analysis theorems and audited local
analytic interfaces are the mathematical inputs. Unknown availability
is not evidence of absence. The exact algebraic identities and global
sign bounds above are an informally audited proof, not a claimed Lean
formalization.
