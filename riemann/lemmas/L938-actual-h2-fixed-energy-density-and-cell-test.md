# Lemma 938: the fixed actual-theta H2 energy density and its cell test

## Hypotheses

Use exactly L019's positive kernel K, L058's family, and L874's local
logarithm convention. For real lambda put

    M_j(lambda) = integral_0^infinity u^j exp(lambda u^2) K(u) du,
    A_k(lambda) = M_(2k)(lambda)/(2k)!,             0<=k<=6,
    log(F(lambda,z)/M_0(lambda)) = -sum_(n>=1) S_n(lambda) z^(2n)/n,
    H2(lambda) = (S_(i+j+2)(lambda))_(0<=i,j<=2).

No contact, positive semidefiniteness, real-zero law, endpoint sign or
RH premise is assumed. In particular the fixed positive normalization
is M_0^12, even though a smaller power would clear the denominators.

The numerical enclosures below are conditional on L037's directed
Decimal basic operations and correctly rounded nearest exponential,
widened by adjacent values. All three contexts have precision 200;
invalid operations, overflow, underflow, subnormal arithmetic and
zero-containing divisors are rejected. Python integer arithmetic is
used exactly. Square-root endpoints are checked by exact rational
squaring, so no additional square-root rounding assumption is needed.
The implementation of these libraries is not independently verified.

## Conclusion

There is a fixed real continuous density v on [0,infinity), with v(0)=0,
such that for every real lambda

    M_0(lambda)^12 det H2(lambda) = integral_0^infinity exp(lambda E)v(E)dE. (1)

For every finite b>=0 and integer r>=0,

    integral_0^infinity (1+E)^r exp(bE)|v(E)|dE < infinity.              (2)

Here v is exactly the 34-term signed convolution specified below, with
no optional factor or substitute kernel. Its measure has no atoms,
including at E=0. The representation and bounds are unconditional
analytic consequences of the stated theta inputs; only the numerical
enclosures depend on the arithmetic contracts.

For the 32 stipulated cells I_j=(j/4,(j+1)/4), put B_j=integral_(I_j)v.
The corrected fixed-budget certificate gives, subject to the arithmetic
contracts,

    B_j<0,    j=0,1;
    B_j>0,    2<=j<=14;
    zero-containing enclosures,    15<=j<=31.                        (3a)

In particular v is nonzero on open intervals of both signs and has
at least one sign change. No certified alternating triple occurs in
this record. The remaining enclosures do not determine their true
signs. The at-most-one-crossing premise is neither established nor
refuted, and no H2, contact, endpoint or RH sign conclusion follows.

## Proof

### Exact normalization and polynomial

Set e_k=A_k/A_0. L058 gives M_0>0 for every real lambda. L874 and
L917's finite-log algebra give S_2,...,S_6 by the Newton recurrence

    q_0=1, q_n=(-1)^n e_n,
    S_n=-n q_n-sum_(j=1)^(n-1) S_j q_(n-j),       1<=n<=6.            (3)

With a=S_2,b=S_3,c=S_4,d=S_5,e=S_6,

    det H2 = ace-ad^2-b^2e+2bcd-c^3.                                 (4)

Every monomial of (4) has weighted degree 12 when e_k has weight k.
Substitution and collection cancel every term of ordinary degree
greater than 6. Thus

    P(A_0,...,A_6)=A_0^12 det H2=sum_alpha c_alpha product_(k=0)^6 A_k^alpha_k, (5)

where all coefficients and exponents are in this table. Each row has
sum alpha_k=12 and sum k alpha_k=12.

| c_alpha | (alpha_0,alpha_1,alpha_2,alpha_3,alpha_4,alpha_5,alpha_6) |
|---:|---|
| 64 | (9,0,0,0,3,0,0) |
| -120 | (9,0,0,1,1,1,0) |
| 54 | (9,0,0,2,0,0,1) |
| -27 | (8,0,0,4,0,0,0) |
| 50 | (9,0,1,0,0,2,0) |
| -48 | (9,0,1,0,1,0,1) |
| 90 | (8,0,1,2,1,0,0) |
| -48 | (8,0,2,0,2,0,0) |
| -40 | (8,0,2,1,0,1,0) |
| 24 | (8,0,3,0,0,0,1) |
| -4 | (7,0,3,2,0,0,0) |
| 8 | (7,0,4,0,1,0,0) |
| -72 | (8,1,0,1,2,0,0) |
| 66 | (8,1,0,2,0,1,0) |
| 68 | (8,1,1,0,1,1,0) |
| -60 | (8,1,1,1,0,0,1) |
| 18 | (7,1,1,3,0,0,0) |
| -44 | (7,1,2,1,1,0,0) |
| 16 | (7,1,3,0,0,1,0) |
| -25 | (8,2,0,0,0,2,0) |
| 24 | (8,2,0,0,1,0,1) |
| -6 | (7,2,0,2,1,0,0) |
| 50 | (7,2,1,0,2,0,0) |
| -30 | (7,2,1,1,0,1,0) |
| -6 | (7,2,2,0,0,0,1) |
| 1 | (6,2,2,2,0,0,0) |
| -2 | (6,2,3,0,1,0,0) |
| -14 | (7,3,0,0,1,1,0) |
| 12 | (7,3,0,1,0,0,1) |
| -4 | (6,3,0,3,0,0,0) |
| 10 | (6,3,1,1,1,0,0) |
| -4 | (6,3,2,0,0,1,0) |
| -9 | (6,4,0,0,2,0,0) |
| 8 | (6,4,0,1,0,1,0) |

The producer also derives all six polynomials independently as
-n[t^n] sum_(j=1)^6 (-1)^(j+1)h(t)^j/j, with
h=sum_(n=1)^6 (-1)^n e_n t^n, discarding degrees above six.
Every exact rational residual is zero. This is verification of the
existing finite algebra, not a new logarithm theorem. The A_0^6
factor in (5) is retained in v, not removed as a normalization choice.

### Singular factors, continuity and full exponential domination

For x>0 define

    f_k(x)=x^(k-1/2) K(sqrt(x))/(2(2k)!),          0<=k<=6.            (6)

Extend them by zero on x<0; their individual values at zero are
irrelevant. They are nonnegative, locally integrable functions, since
K is continuous and k-1/2>-1. The substitution x=u^2 gives

    integral_0^infinity exp(lambda x)f_k(x)dx=A_k(lambda).             (7)

For a row alpha let h_alpha be the convolution of alpha_k copies of
f_k for each k, twelve factors in total, and set

    v(E)=sum_alpha c_alpha h_alpha(E).                               (8)

There is no combinatorial multinomial factor in (8): a product of
twelve transforms corresponds to one convolution of twelve labelled
factors. Commutativity allows the notation alpha but does not add
permutations.

Here is a pointwise continuous representative of each convolution.
Choose the twelve indices k_1,...,k_12 with these multiplicities, and
let Delta_11={t_i>=0, sum_(i=1)^12 t_i=1}, parametrized by t_1,...,t_11.
For E>0, changing x_i=Et_i in the convolution integral gives

    h_alpha(E)=E^17/(2^12 product_i (2k_i)!)
       * integral_Delta_11 product_i [t_i^(k_i-1/2)K(sqrt(E t_i))] dt. (9)

The power 17 is sum k_i+12/2-1=12+6-1. The weight in the simplex
integral is integrable. Iterated Euler beta integration gives its
integral as product_i Gamma(k_i+1/2)/Gamma(18), which is finite.
This is the ordinary beta-integral identity with strictly positive
parameters k_i+1/2; it follows by iterating the change of variable
x=(1-s)t in the one-dimensional Euler beta integral
([DLMF 5.12.1](https://dlmf.nist.gov/5.12#E1), whose two real
parameters must be positive). Thus on each
bounded E interval the integrand in (9) has a fixed integrable
majorant, using the boundedness of K there. Dominated convergence
proves continuity on (0,infinity), and the same bound gives
h_alpha(E)=O(E^17) at zero. Set h_alpha(0)=0. Equation (8) is therefore
continuous on the closed half-line.

For b>=0 and integer r>=0, (6) and L058's domination imply

    integral (1+x)^r exp(bx) f_k(x)dx
      =1/(2k)! integral (1+u^2)^r u^(2k) exp(bu^2)K(u)du < infinity.  (10)

For nonnegative x_i, 1+sum x_i<=product(1+x_i). Tonelli applied to
the twelve nonnegative factors shows that the integral of
(1+E)^r exp(bE)h_alpha(E) is at most the product of the twelve
integrals (10). Taking the finite sum with |c_alpha| proves (2).
It also justifies Fubini for exp(lambda sum x_i) for every complex
lambda, by using b=max(0,Re lambda). Equations (5), (7), (8) prove
(1). Compact domination with additional powers E justifies any
later differentiation in lambda. The conventional Laplace variable
is x=-lambda; the positive tilt has not been reversed accidentally.

These arguments use Tonelli, Fubini, dominated convergence and Euler's
beta integral. The usual convolution/product identity is recorded in
[NIST DLMF 1.14.30–31](https://dlmf.nist.gov/1.14#E30).
Its endpoint piecewise-continuity formulation alone does not cover
f_0's singularity. Equations (9)–(10) provide the required specialization
instead of applying that hypothesis incorrectly.

Every h_alpha is an integrable density, so there is no boundary atom.
Zero intervals are permitted. Nonzero density must be certified
separately before applying a zero-count theorem. Constant K would
make the leading simplex coefficient vanish: the exact table satisfies
sum c_alpha/product_k(k!)^alpha_k=0. Thus positivity of K alone has
not been substituted for an oscillation or nonvanishing argument.

### One fixed full-kernel polynomial enclosure

Write k(x)=K(sqrt(x)) for x>=0. We justify the analytic approximation
on the entire compact interval [0,8], not only at sampling points.
The theta series is normally convergent on compact subsets of
|Im u|<pi/4. Indeed the real part of exp(2u) is strictly positive
there, uniformly on each compact set, and dominates every polynomial
in n. It defines an analytic K on this strip.

The theta transformation used in L019 gives, first for real u,
A(-u)=A(u)+sinh(u/2). The operator 2d^2/du^2-1/2 annihilates the
extra term, so K(-u)=K(u). The identity theorem extends this evenness
to the strip. It removes the square-root branch at zero: locally
the even Taylor series for K is a power series in x=u^2.

On the energy Bernstein ellipse rho=3/2 write

    x=4+4 cos(theta+i log rho),
    u=sqrt(8) cos((theta+i log rho)/2),       -pi<=theta<=pi.

Then u^2=x, 0<=Re u<=5/sqrt(3)<3 and |Im u|<=1/sqrt(3)<pi/4.
The interior and a neighborhood of the ellipse also map into the
analytic domain, with evenness resolving the two choices of root.
More explicitly, for x=a+ib the squared real and imaginary parts of
a root are (|x|+a)/2 and (|x|-a)/2. Both are convex functions of x,
so their maxima on the filled ellipse occur on its boundary. The
displayed bounds therefore hold throughout the filled ellipse, with
a strict margin from |Im u|=pi/4. At nonzero x choose either local
analytic root; evenness makes the two definitions agree. At zero
use the even Taylor series. This gives an analytic k on a neighborhood
of the entire closed ellipse, not just a boundary parametrization.
Since cos(2 Im u)>=1-(2 Im u)^2/2>=1/3 and pi>3,

    |K(u)| <= (128 exp(27/2)+48 exp(15/2)) sum_(n>=1)n^4 exp(-n^2)
            < 10^9.                                                   (11)

For explicit elementary bounds, e<3 gives exp(27/2)<3^14<5*10^6
and exp(15/2)<3^8<10^4. Also e>8/3. With n=2+j,
n^4<=16*6^j and n^2>=4+5j, so
sum n^4 exp(-n^2)<=e^-1+16e^-4/(1-6e^-5)
<3/8+20/57<1. These bounds prove (11) with room to spare.

Use the degree N=256 interpolant at the n=N+1=257 root nodes
x_j=4+4cos((2j+1)pi/(2n)), 0<=j<n. Its Chebyshev coefficients are

    c_0=(1/n) sum_j k(x_j),
    c_l=(2/n) sum_j k(x_j)cos(l(2j+1)pi/(2n)),       1<=l<=N.         (12)

Here and below T_l(x/4-1) is the Chebyshev basis. The Laurent coefficient
formula on the annulus for k(4+2(w+w^-1)), integrated on |w|=rho,
gives coefficients of magnitude at most 2*10^9*rho^-l for l>=1
([DLMF 1.10.6–7](https://dlmf.nist.gov/1.10#E6)). No analyticity at
w=0 is used. This Laurent function is invariant under w->1/w, so
its two equal Laurent coefficients combine to a multiple of T_l.
Root-node discrete orthogonality, including norm n for the constant
mode and n/2 for the other modes, gives (12)
([DLMF 18.3.1–2](https://dlmf.nist.gov/18.3#E1)).

For the alias statement write m=2qn+r, with -n<=r<=n. At
theta_j=(2j+1)pi/(2n), cos(m theta_j)=(-1)^q cos(r theta_j).
If |r|=n these values vanish; otherwise the degree-at-most-N
interpolant is (-1)^q T_|r|. Thus every T_m interpolates to zero or
a signed basis polynomial, with sup norm at most 1 on [-1,1].
This is the root-grid case; no extrema-grid alias formula is assumed.
Absolute uniform convergence permits interpolation term by term
(there are finitely many evaluations). The series tail and its interpolant each
have norm at most the sum of their absolute coefficients. Consequently
the full analytic interpolation error is at most

    4*10^9 sum_(l=N+1)^infinity rho^-l
       = 8*10^9*(2/3)^256.                                          (13)

This short Cauchy/aliasing argument is included to verify the specific
approximation and its constant; no general interpolation theorem or
new source result is claimed.

The implementation encloses pi using 128 terms of each Machin
arctangent from L037. It encloses cosine on [0,4] by the Taylor sum
through degree 256 with error at most 4^258/258!, using the vanishing
degree-257 coefficient and the bounded degree-258 derivative. Cosines
of higher multiples in (12) use the exact Chebyshev recurrence with
interval arithmetic. Square roots of positive node intervals are
enclosed and then checked by rational squaring of both endpoints.

At each node retain theta terms 1,...,8. The full omitted positive
tail on 0<=u<=3 is bounded by

    tau = 256*9^4*10^6/20^81.                                      (14)

Indeed, dropping the negative part of K_n gives
K_n<=128 n^4 exp(27/2) exp(-3n^2). For n=9+j,
n^4<=9^4*2^j and n^2>=81+19j. Since exp(3)>20,
the geometric ratio is less than 1/2. Thus the sum is at most
256*9^4 exp(27/2) exp(-243), which is bounded by (14).
The inequalities exp(3)>20 and exp(27/2)<10^6 are verified by the
positive Taylor sum through degree 8 for the first, and the sum
through degree 64 plus its geometric remainder for the second.
There is no omitted spatial tail for this cell calculation: total
energy E<=8 forces every individual energy x_i<=8.

Choose each coefficient d_l as the rounded midpoint of the enclosing
interval in (12), on the fixed rational grid 10^-120. If eta_l is
the larger distance to its two endpoints, the rational polynomial

    p(x)=sum_(l=0)^256 d_l T_l(x/4-1)

satisfies, uniformly on [0,8],

    |k(x)-p(x)| <= epsilon
       :=8*10^9*(2/3)^256+sum_l eta_l < 6.664*10^-36 < 10^-34.        (15)

The complete coefficient intervals, chosen rational values, errors,
node kernel intervals and exact power-basis coefficients are saved
in `scripts/heat/actual-h2-energy-cell-48.json` under `approximation`.
Endpoint comparisons check the exact change of polynomial basis.
Neither the nodes nor an uncontrolled sampled convolution are used
as sign evidence; (13)–(15) are the required uniform error estimate.

### Exact convolution integration and complete error allowance

For all real u>=0, the positive kernel obeys K(u)<7. To check this,
e^(9u/2-pi n^2 e^(2u)) decreases from its value at zero, since its
logarithmic derivative is 9/2-2pi n^2 e^(2u)<0. Thus

    K(u)<=128 sum n^4 exp(-3n^2)
        <=128 exp(-3)/(1-16 exp(-9))<7,

using n^4<=16^(n-1), n^2>=1+3(n-1) and exp(3)>20. Since epsilon<1,
|p(x)|<=8 on [0,8]. Telescoping twelve factors gives

    |product_i k(x_i)-product_i p(x_i)|<=12 epsilon 8^11.             (16)

Replace K(sqrt(x)) by p(x) in (6), (8) to define v_p on [0,8].
This polynomial replacement is only an integration device on this
compact domain; no assertion of its integrability at infinity is made.
The beta integral and Gamma(k+1/2)=sqrt(pi)(2k)!/(4^k k!) give

    |integral_a^b (v-v_p)(E)dE|
      <=12 epsilon 8^11 * pi^6*(b^18-a^18)/(2^36*18!)
                      *sum_alpha |c_alpha|/product_k(k!)^alpha_k     (17)

for 0<=a<=b<=8. Notice that the factorial is 18!, not 17!, after
integration over a cell. Equation (17) pays the full kernel error
and all singular simplex integrations simultaneously.
The exact absolute coefficient weight in (17) is 293/540.
The half-integer identity follows from the gamma recurrence,
duplication formula and factorial values
([DLMF 5.5.1/5](https://dlmf.nist.gov/5.5#E5),
[5.4.1](https://dlmf.nist.gov/5.4#E1)); all arguments here are
positive half-integers, so none of the excluded poles occurs.

The integration of v_p is exact before its final directed conversion.
Write p(x)=sum_(l=0)^N a_l x^l/D with integer a_l and
D=10^120*4^N. Define integer polynomials

    Q_k(t)=sum_(l=0)^N a_l (2k+2l)!/(k+l)!
                          *4^(N+6-k-l)*12!/(2k)! t^l,
    C=2*12!*D*4^(N+6),
    R(t)=sum_alpha c_alpha product_k Q_k(t)^alpha_k=sum R_l t^l.

All divisions displayed in Q_k are exact integer divisions. Applying
the beta integral term by term yields

    v_p(E)=pi^6/C^12 sum_l R_l E^(17+l)/(17+l)!,
    integral_0^E v_p=pi^6/C^12 sum_l R_l E^(18+l)/(18+l)!.             (18)

All signed cancellations in R and in (18) are performed with integers.
If d=deg R, evaluations at E=j/4 have the common rational denominator
C^12*(d+18)!*4^(d+18), before the common pi^6 factor. The complete
integer numerators are retained; there is no floating-point
cancellation or quadrature remainder. The saved multiplication
checks are sanity checks only, not replacements for these identities.

The producer multiplies polynomials by Kronecker substitution in
base 2^w, choosing w at least the sum of the input coefficient
bit lengths plus the bit length of the shorter polynomial and two,
rounded upward to a whole byte.
Every true product coefficient then has absolute value <2^(w-2).
Packing positive and negative coefficients separately evaluates each
polynomial exactly at 2^w. Multiplication and balanced-digit extraction
therefore recover the polynomial exactly: the prescribed coefficient
bound prevents an ambiguous carry. The implementation checks the
final carry, coefficient bound and two modular evaluations per
multiplication. This is an implementation of exact finite algebra,
not a probabilistic sign certificate.

For the signed extraction detail, let B=2^w. If the maximum input
bit lengths are a,b and the shorter length is L, then each product
coefficient has absolute value less than L*2^(a+b)<2^(w-2), including
the upward byte rounding of w. Every input digit fits into its byte
block, so separately packing positive and negative parts computes
the signed evaluations at B exactly. If the output has length m,
the absolute evaluated product is less than B^m, by the geometric
sum of these coefficient bounds; its unsigned byte array fits.

Choose sigma as the sign of that integer (sigma=1 at zero). In each
base-B digit position the code adds the incoming carry to the unsigned
digit, subtracts B if the result is at least B/2, and passes carry
one exactly in that case. Reduction modulo B determines the unique
coefficient in [-B/2,B/2). The true coefficient sigma times the
product coefficient lies in (-B/4,B/4), so induction from the lowest
position recovers it. After the last position the true remaining
quotient is zero, proving the final carry is zero. Multiplication
by sigma restores the coefficients. Unequal input lengths and
negative coefficients require no nonnegativity hypothesis; constant
and zero inputs are handled directly. The modular checks only detect
incidental implementation mistakes and do not prove this identity.

For each stipulated cell I_j=(j/4,(j+1)/4), subtract the two exact
primitive numerators from (18), convert outward and multiply by the
enclosing pi^6. Enlarge by plus/minus the full upper bound in (17).
Open versus closed cell endpoints have the same mass because v is a
continuous density. These are the only 32 cells tested; all budgets
were fixed before invocation, and no refinement is authorized here.

### Sign criterion, scope and verification status

The corrected complete intervals imply (3a). For convenient outward
abbreviations, four of them are

    -3.658*10^-54 < B_0 < -3.657*10^-54,
     3.156*10^-43 < B_2 <  3.157*10^-43,
     4.541*10^-38 < B_14 < 7.034*10^-38,
    -3.076*10^-38 < B_15 < 4.615*10^-38.

All 32 full endpoints, rather than these abbreviations, are saved and
checked. The polynomial approximation's mass in cell 15 lies between
7.69560*10^-39 and 7.69561*10^-39, while the full error allowance is
less than 3.84518*10^-38 and greater than 3.84516*10^-38. Thus this
valid bound loses the sign already at cell 15. It supplies no reason
to declare that cell negative, zero or positive. No refinement of
the fixed degree, theta cutoff, arithmetic precision or cell set was
made after this uncertainty was found.

Since B_0<0 and B_2>0, continuity of v supplies a negative open
interval within (0,1/4) and a positive open interval within (1/2,3/4).
This excludes an identically zero density and proves at least one
sign change. Possible other zero intervals, including outside [0,8],
remain unrestricted. The certified signs form only a negative block
followed by a positive block, with seventeen unresolved cells; they
are not the requested three alternating nonzero signs.

If three ordered cell masses have strictly alternating signs, each
cell contains a point where v has that sign: otherwise its integral
could not have the indicated strict sign. Continuity supplies open
intervals around those points. The three ordered nonzero signs imply
at least two sign changes, even if there are intervening zero intervals.
They would therefore refute the at-most-one-sign-change premise for
this exact normalization. They would not refute positivity of the
Laplace transform, actual H2 positivity, or RH.

The downstream comparison is Bhaskar–Song, *Descartes' rule of signs
and the identifiability of population demographic models from genomic
variation data*, Ann. Statist.42(6) (2014),2469–2493,
[arXiv:1309.5056v3](https://arxiv.org/pdf/1309.5056v3), Definition3,
Theorem4, proof p14. Its density sign-change premise is not assumed
here. Equation (2) supplies the improper-integral differentiation
qualification recorded in the approved assessment; the conventional
transform variable is -lambda. No zero-count theorem is invoked
without both a nonzero density and its full crossing bound.

Reproduction command: `python3 scripts/heat/actual-h2-energy-cell-48.py`.
The main certificate and the exact convolution polynomial are separate
JSON files beside that script. The full degree-3072 integer polynomial
is `scripts/heat/actual-h2-energy-cell-polynomial-48.json`.
The exact-rational consistency check is
`python3 scripts/heat/check-actual-h2-energy-cell-48.py`; all 969 checks
pass and its complete record is
`scripts/heat/actual-h2-energy-cell-checks-48.json`. It checks the Machin
enclosure, both elementary exponential inequalities, all saved square
root and coefficient-error bounds, the complete epsilon and beta-weight
formulas, all 32 polynomial/error/final enclosures and signs, the
absence of a certified alternating triple, and arithmetic traps/flags.
The full load-bearing endpoint fields and the checker summary were
inspected, not accepted from a bounded preview. The check does not
independently replay the transcendental node producer or the large
polynomial multiplication. Those remain subject to the analytic/code
proof above and the explicitly retained implementation contracts.

**Invalid first pass, preserved.** The consistency checker initially
rejected the final lower endpoint of cell 1. Two expressions
`I(-er.hi, er.hi)` used ambient Decimal negation at precision 28, once
for a cosine remainder and once for the final cell error. That could
shrink a lower error endpoint. No sign or approximation enclosure
from that run is accepted. The original script and full records are
preserved in `scripts/heat/actual-h2-energy-cell-first-pass-48.py`,
`scripts/heat/actual-h2-energy-cell-first-pass-48.json`,
`scripts/heat/actual-h2-energy-cell-polynomial-first-pass-48.json`, and
`scripts/heat/actual-h2-energy-cell-first-pass-failure-48.json`.
The latter stores the exact failed inequality, not merely an error
message. Only those two operations were replaced by `copy_negate`,
and the identical budget was rerun. A source comparison verifies
that these were the only two producer changes. This repairs invalid
arithmetic; it is not a refinement of a valid failed sign bound.

### Independent conceptual audit — 9 November 2026, step50

The separate audit under the pre-existing SPECIALIZE assessment
`drafts/literature/2026-11-09-l938-energy-certificate-audit-48.md`
validated the analytic and computational conclusions above, retaining
the arithmetic contracts and every uncertainty in (3a). The additional
root-domain, root-grid and signed-digit details above make explicit
the hypotheses needed by the inspected standard methods. No general
nonnegative-coefficient Kronecker theorem was applied to signed data.

The independent verifier is
`scripts/heat/audit-actual-h2-energy-cell-50.py`; run it with `python3`.
Its complete report is `scripts/heat/actual-h2-energy-cell-audit-50.json`.
All 5101 checks passed. Its verification has the following scope.

1. Direct finite-log extraction and the six-term Leibniz determinant
   reproduce all 34 coefficients, compared against both (5)'s table
   and the saved certificate. The weighted degrees, ordinary-degree
   cancellation, beta weight and constant-kernel cancellation agree.
2. The original transcendental node producer was replayed at exactly
   degree256, 257 nodes, theta cutoff8 and precision200. Every saved
   node, coefficient interval, chosen coefficient and epsilon field
   agrees exactly. The full replay is
   `scripts/heat/actual-h2-energy-cell-node-replay-50.json`.
   This is a replay of the reviewed implementation, not a separate
   transcendental library. The audit runtime identifies itself as
   Python3.15.2; the original producer runtime was not recorded.
   The explicitly assumed arithmetic contracts remain necessary.
3. All 257 power coefficients were independently rebuilt with
   T_n(y)=(n/2) sum_(j=0)^floor(n/2)
   (-1)^j (n-j-1)! (2y)^(n-2j)/(j!(n-2j)!), n>=1,
   and T_0=1, then y=x/4-1. Substitution of the coefficients in
   T_n=2yT_(n-1)-T_(n-2), with the initial n=1,2 cases, verifies
   this closed formula: if b_(n,j) denotes its coefficient of
   y^(n-2j), then b_(n,j)=2b_(n-1,j)-b_(n-2,j-1), with absent
   coefficients zero. After extracting the common factorial factor,
   the identity is (n-1)(n-2j)+(n-2)j=n(n-j-1); the boundary
   coefficients satisfy it as well. The audit uses exact rational arithmetic,
   independently of the producer's recursive basis conversion.
4. Every Q_k coefficient was rebuilt from its rational gamma weight,
   with all 1799 integer divisions checked exactly. All 3073 saved
   R coefficients were then validated without balanced-digit recovery
   or a modular inference, as follows.

   Put U=sum_alpha |c_alpha| product_k (sum_l |Q_(k,l)|)^alpha_k
   and V=max_l |R_l| for the saved coefficients. The actual polynomial
   sum_alpha c_alpha product Q_k^alpha_k has every coefficient bounded
   in absolute value by U, by repeated convolution and the triangle
   inequality. With w=bit_length(U+V)+1=32471 and B=2^w, the audit
   checks U+V<B/2. Direct signed Horner evaluation of the saved
   polynomial at B agrees exactly with evaluation of the 34-term
   expression there; the exact residual is zero. The retained Q_0^6
   factor reduces computation without changing the expression.

   If D is the difference polynomial, each |D_l|<B and D(B)=0.
   Reduction modulo B gives D_0=0; division by B and induction give
   every D_l=0. Thus this single integer equality with its proved
   coefficient bound verifies the full polynomial, rather than
   sampling it. U, V, w, zero residual and input hashes are saved in
   the report; no claim rests on the original modular sanity checks.
5. Direct factorial quotients rebuild the integrated coefficients.
   Even/odd Horner evaluation checks all 33 primitive endpoints and
   every saved cell numerator. Exact rational comparisons check all
   32 polynomial enclosures, full kernel error allowances, final
   endpoint inclusions and signs. The measured epsilon is less than
   6.663888*10^-36, against the required 10^-34. There are zero
   certified alternating triples, against the test's requirement of
   at least one; seventeen cells remain unresolved.

The original 969-check rational verifier was also rerun with its
output redirected to
`scripts/heat/actual-h2-energy-cell-rational-recheck-50.json`; all
checks pass. The exact old cell1 endpoint defect was independently
reproduced and saved in
`scripts/heat/actual-h2-energy-cell-regression-audit-50.json`.
The first-pass producer differs from the corrected producer in exactly
the two documented sign-copy substitutions. All original certificates
and both producers are preserved. Hash comparisons confirm the
corrected producer and its two original certificates were unchanged
by this audit. Every saved pass/fail entry was checked, and the zero
residual and full summary were inspected; bounded previews were not
treated as evidence.

This establishes local validation of L938's existing input, not a
new density, new sign experiment, full crossing theorem or RH result.
The direct mathematical uses remain L019, L037, L058, L874 and L917;
no DAG edge or main-argument assembly changes as a result of this audit.

The original construction reused the pre-existing EXPLORE assessment
`drafts/literature/2026-11-09-actual-h2-energy-cell-test-46.md`.
Convolution identities, finite logarithms, Cauchy estimates and beta
integration are standard methods, reproduced only where the actual
normalization, singular endpoints or implemented constants require
justification. No progress beyond the inspected sources is claimed
for those methods. The actual fixed-cell question is the bounded
research test. Endpoint signs, contact/tangency, other degrees,
initialization, realization and global continuation remain independent
gaps in the main L030–L032/C032a problem.

## Mathlib

Full and supporting Mathlib coverage for this exact statement and
certificate has not been checked. Availability is unknown, not
asserted absent. The named standard analytic inputs above do not
constitute a formal verification of the interval implementation or
the actual-Xi sign problem.
