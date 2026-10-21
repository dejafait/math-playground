# Lemma 393: positive leading coefficient for the complete discriminant square

## Hypotheses

Use the fixed actual functions, ordinary height derivatives, positive gamma
normalization and discriminant of L390/L392, for sufficiently large positive
real t. In particular L=log(2+t), f=F_0/A, x=f, y=f'/L, z=f''/L^2,
Z=zeta(5/2+it), c=1/(4pi), and

    M=(z^2+3xz/2+x^2/16-y^2)/2,
    K=((z-x/4)-iy)^2/2,
    P(x,y,z)=M^2+|K|^2/2
            =M^2+((z-x/4)^2+y^2)^2/8.

Delta is the complete actual normalized discriminant, including envelope
curvature. Set ell=log H. No RH, simplicity, noncoincidence, phase
independence, eventual discriminant sign or growing-twist assumption is made.

For coprime positive h,k, define the finite positive factor

    B(h,k)=product_(p^e || hk) [1+e(p-1)/(p+1)],
    B(1,1)=1.

Write tau(n) for the number of positive divisors, and define

    Psi=sum_(m,n>=1) tau(m)tau(n)(mn)^(-5/2)
               B(m/g,n/g)/sqrt((m/g)(n/g)),  g=gcd(m,n).

## Conclusion

For all sufficiently large real H tending to infinity,

    (1/H) integral_[H,2H] Delta(t)^2 dt
        = beta (log H)^4 + o((log H)^4),
    beta=c^4 * [263/(1425600 zeta(2))] * Psi > 0.       (1)

The series defining Psi converges absolutely and Psi>=1. Every physical
projection and the complete response tail are retained through L392 and the
norm transfers below. This is a local reproduction using known moment
theorems. The separate critical audit below validates the asymptotic and
its L392 input. It neither proves an optimal negative-set size nor improves the
existing negative-set bound by itself. No global positivity, eventual D sign,
common-zero upper count, total pencil margin or RH consequence follows.

## Proof

The prior EXPLORE assessment is
`drafts/literature/2026-10-10-discriminant-second-moment-leading-scale.md`.
The analytic theorem is imported, not reproved. The new local work is its
ordinary-jet specialization, finite coefficient algebra, sharp bracketing and
full-tail limit. The historical coarse four-factor rectangle failure remains
valid for that certificate; it is not used here.

### Imported six-term input and fixed-twist arithmetic factor

C. P. Hughes and M. P. Young, *The twisted fourth moment of the Riemann zeta
function*, J. reine angew. Math. 641 (2010), 203–236,
[arXiv:0709.2345v2, Theorem 1.1, equations (12)–(17), pp. 4–5](https://arxiv.org/pdf/0709.2345v2#page=4),
give the complete balanced shifted fourth moment with twist (h/k)^(-it).
Here h,k are coprime, hk<=T_Y^(2/11-epsilon), all four complex shifts are
O(1/log T_Y), and the weight w is smooth, nonnegative, supported in
[T_Y/2,4T_Y], with w^(j)=O_j(T_0^(-j)) and
T_Y^(1/2+epsilon)<<T_0<<T_Y. Their error is
O(T_Y^(3/4+epsilon)(hk)^(7/8)(T_Y/T_0)^(9/4)). The total six-term
expression is holomorphic in the shifts (the remark on p. 5); its individual
singular pieces may not be differentiated at coincident shifts.

In this proof the head, h,k and relative smoothing width are fixed before
H tends to infinity. Take T_Y=H and T_0 a fixed small positive multiple of H.
Choose, for example, epsilon=1/16. The support and derivative conditions
hold, the twist size condition eventually holds, and the theorem error is
O_(h,k,w)(H^(13/16))=o(H). Constants depending on that fixed smoothing
width are permitted; the width tends to zero only after the height limit.

At zero shifts and s=0, the finite Euler factors of (14) reduce to B(h,k).
Indeed a prime exponent e contributes the ratio

    sum_(j>=0) (j+1)(j+e+1)p^(-j)
       / sum_(j>=0) (j+1)^2 p^(-j)
       =1+e(p-1)/(p+1).

This uses sum (j+1)q^j=(1-q)^(-2) and
sum (j+1)^2q^j=(1+q)/(1-q)^3, valid for |q|<1. All six shift
permutations therefore have this same zero-shift factor. The denominator
zeta factor of (12) contributes 1/zeta(2), and the outside twist factor
is 1/sqrt(hk). The finite Euler factors and the denominator are analytic
near zero shifts. Keeping this factor does not discard any gcd collision.

### Holomorphic leading kernel and ordinary height jets

Write the four shifts as (a,b,d,e)/ell. For bounded scaled complex shifts
away from pair-sum zero, expand each pole factor using
zeta(1+v/ell)=ell/v+O(1); all remaining factors have their zero-shift
values with error O_(h,k)(1/ell). Uniformly on the height support,
log(t/(2pi))/ell=1+O(1/ell). Thus the leading scaled six-term kernel is

    S(a,b,d,e)=exp(-(a+b))
        sum_(I subset {1,2,3,4}, |I|=2)
           exp(sum_(i in I) v_i)
           / product_(i in I,j not in I) (v_i-v_j),
    (v_1,v_2,v_3,v_4)=(a,b,-d,-e).                  (2)

The selection I={1,2} is the unswapped term, I={3,4} the fully swapped
term, and the other four selections are the four single swaps in (17).
The differences in the denominator retain their signed orientations.
There is no diagonal-only approximation. On separated bounded shift
contours, the whole main term equals

    ell^4 B(h,k)/(sqrt(hk) zeta(2)) S(a,b,d,e)
        +O_(h,k)(ell^3),                             (3)

pointwise before integration against w.

Both the original theorem total and S extend holomorphically through
coincident shifts. To justify jet differentiation with a uniform remainder,
use u variables with (a,b,d,e)=(iu_1,iu_2,-iu_3,-iu_4), and nested Cauchy
circles |u_j|=r_j, for instance r_j=1,3,9,27. Every difference u_i-u_j
then has modulus at least |r_i-r_j|>0. Expansion (3) is uniform on the
product of these circles. Repeated Cauchy integration applies to the
holomorphic complete totals and their difference, giving (3) and its
derivatives at zero through total order eight, with error O_(h,k,w)(H ell^3)
after integration. The uniform theorem error gives O_(h,k,w)(H^(13/16))
in these scaled derivatives. Singular summands at zero are never separately
differentiated. This argument requires no real-shift-only asymptotic.

For ordinary jets, use L391's exact formulas and their negative-height
conjugates. If h_p=zeta^(p)(1/2+it), then

    f=-R h_0,
    f'/ell=-R i(h_1/ell+(Omega/ell)h_0),
    f''/ell^2=-R[-h_2/ell^2-2(Omega/ell)h_1/ell
                            -(Omega/ell)^2 h_0+i Omega' h_0/ell^2].

Here R'/R=i Omega, Omega/ell=1/2+O(1/ell), Omega'=O(1/H)
uniformly on the support. In the negative-height representation, i changes
to -i and the last term changes to -i Omega'h_0/ell^2. Also
L/ell=1+O(1/ell). The actual polygamma bounds justify these estimates
separately; no derivative of an unspecified asymptotic is taken.

Assign any two of the four jet factors to each orientation. The four minus
signs multiply to one and R^2R^(-2)=1. The leading positive-orientation
order-j operator is i^j(partial_a+1/2)^j, j<=2, and the negative one is
(-i)^j(partial_d+1/2)^j. These are operators on *scaled complex shifts*.
Their combined generating kernel is consequently

    Bcal(u)=exp(i(u_1+u_2-u_3-u_4)/2)
              S(iu_1,iu_2,-iu_3,-iu_4)
       =sum_(|I|=2) exp(i(sum_(i in I)u_i-sum_i u_i/2))
                    / product_(i in I,j not in I)(u_i-u_j). (4)

The denominator has four i factors, whose product is 1. This checks all
ordinary-derivative signs and the half-log gamma carrier. The expression
is symmetric in all four u variables, so the orientation assignment does
not change a monomial moment. It is not a statistical independence claim.

Errors in replacing the complete normalized jets by these leading operators
have integral O(H ell^3). To see this without an unproved shifted norm,
L390 gives integral U^2=O(H ell^4) on each comparable dyadic interval,
and hence on [H/2,4H]. The displayed triangular exact formulas invert to
bound each |h_p/ell^p|, p<=2, by a fixed multiple of |x|+|y|+|z|,
since |R|=1 on the real line. A coefficient change O(1/ell) in any
homogeneous quartic monomial thus has absolute integral O(H ell^3).
The Omega' term is smaller. Fixed twists have modulus one, and fixed
heads are bounded, so the same estimate covers every retained term.

It follows that for j_i in {0,1,2} and every permitted fixed smooth w,

    integral w(t) (h/k)^(-it) product_i [f^(j_i)(t)/L(t)^j_i] dt
       =ell^4 [B(h,k)/(sqrt(hk) zeta(2))]
          [partial_u^j Bcal(0)] integral w(t)dt
               +o_(h,k,w)(H ell^4).                 (5)

The j_i here denote ordinary height orders. Formula (5) imports the moment
theorem and derives only the family-specific conversion.

### Finite exact coefficient and noncancellation

Expansion of P gives the nine monomials in the table below. To make their
coefficient evaluation reproducible without evaluating singular expressions,
set V(u)=product_(i<j)(u_i-u_j), C_I(u)=product_(i in I,j not in I)
(u_i-u_j), and l_I=sum_(i in I)u_i-sum_i u_i/2. For even d>=0 define

    Q_d(u)= [i^(d+4)/(d+4)!]
                 [sum_(|I|=2) (V/C_I) l_I^(d+4)] / V. (6)

Each V/C_I is a signed polynomial of degree two. The numerator is alternating
under any variable transposition, so is divisible by V; its degree is d+6,
and Q_d is a homogeneous symmetric polynomial of degree d. The analogous
numerators for exponential degree below four vanish because an alternating
polynomial of degree less than six is zero. Odd degrees vanish by pairing
I with its complement, since l_(I^c)=-l_I and C_(I^c)=C_I. Thus (6) is
exactly the degree-d Taylor polynomial of (4). Equivalently, expansion of
the exponentials followed by their alternating factorization removes every
apparent pole. These polynomial identities also justify the holomorphic
extension of (4) used above.

For j=(j_1,...,j_4), d=sum j_i, the required derivative is

    partial_u^j Bcal(0)=(product_i j_i!) [u^j] Q_d(u). (7)

Equations (6)–(7), using only rational polynomial operations through
exponential degree twelve, give the complete table:

| monomial | coefficient in P | assigned orders j | derivative in (7) |
|---|---:|---|---:|
| x^4 | 3/2048 | (0,0,0,0) | 1/12 |
| x^3 z | 5/128 | (0,0,0,2) | -1/240 |
| x^2 y^2 | -1/64 | (0,0,1,1) | 1/720 |
| x^2 z^2 | 41/64 | (0,0,2,2) | 1/4032 |
| x y^2 z | -7/8 | (0,1,1,2) | -1/20160 |
| x z^3 | 5/8 | (0,2,2,2) | -61/3628800 |
| y^4 | 3/8 | (1,1,1,1) | 1/6720 |
| y^2 z^2 | -1/4 | (1,1,2,2) | 19/3628800 |
| z^4 | 3/8 | (2,2,2,2) | 17/10644480 |

For example the constant quotient in (6) is 1/12, consistent with the
untwisted fourth moment. Multiplying the two numerical columns and adding
*all nine* contributions gives

    q_P=1/8192-1/6144-1/46080+41/258048+1/23040
            -61/5806080+1/17920-19/14515200+17/28385280
        =263/1425600 > 0.                           (8)

This is the full coefficient, not a positive isolated term. In particular
some contributions are negative and have been retained.

The exact arithmetic check is
`python3 scripts/discriminant/check_balanced_coefficient.py`. Its full
certificate is `scripts/discriminant/balanced-coefficient-certificate.json`.
The script uses Fraction arithmetic, constructs every numerator in (6),
checks each division by multiplication, checks cancellation of low and odd
terms, and checks permutation symmetry of all relevant quotient coefficients.
The complete nine-row moment table and all homogeneous coefficients are saved.
The proof of the analytic moment applicability is the preceding argument,
not the finite script or a numerical preview of a certificate.

### Fixed heads, sharp brackets and the full coefficient

For fixed N let Z_N=sum_(n<=N)n^(-5/2-it) and
b_(m,N)=m^(-5/2) #{(a,b): ab=m, 1<=a,b<=N}. Then

    |Z_N|^4=sum_(m,n<=N^2) b_(m,N)b_(n,N)(m/n)^(-it).

Reduce each pair by its exact gcd and apply (5) with the nine monomials.
This retains every equal-product and equal-ratio collision. It gives

    integral w P(x,y,z)|Z_N|^4
       =ell^4 [q_P/zeta(2)] Psi_N integral w+o_(N,w)(H ell^4),
    Psi_N=sum_(m,n<=N^2) b_(m,N)b_(n,N)
                      B(m/g,n/g)/sqrt((m/g)(n/g)).   (9)

All b_(m,N) are nonnegative; B(h,k)>0; and the m=n=1 term is one.
Thus Psi_N>=1. The strict sign in (9) uses both (8) and these actual
arithmetic factors, rather than nonnegativity of P alone.

For any fixed 0<delta<1/8 choose smooth nonnegative weights w_- and w_+
such that w_-<=1_[H,2H]<=w_+, their supports lie in [H/2,4H],
they have derivative bounds O_(j,delta)(H^(-j)), and

    H(1-C delta)<=integral w_-<=H<=integral w_+<=H(1+C delta),

with a fixed C. Such weights follow by convolution of intervals shrunk
and enlarged by a fixed multiple of delta H with a nonnegative unit-mass
smooth bump supported on [-delta H,delta H]. The whole integrand
P(x,y,z)|Z_N|^4 is nonnegative. It is therefore bracketed by (9) for
w_- and w_+. Take the height liminf and limsup at fixed delta,N, then
let delta decrease to zero. This proves the sharp all-real-H asymptotic

    (1/H) integral_[H,2H] P|Z_N|^4
        =[q_P/zeta(2)] Psi_N ell^4+o_N(ell^4).       (10)

No absolute estimate of individual signed endpoint monomials is substituted
for the whole nonnegative bracket, and no fixed-width error is assumed
uniform as delta decreases.

Next eta_N=sum_(n>N)n^(-5/2) tends to zero. Since |Z|,|Z_N|<=zeta(5/2),
|Z-Z_N|<=eta_N, |P|<=C U^2, and integral U^2/H=O(ell^4) by L390,

    (1/H) integral_[H,2H] |P(|Z|^4-|Z_N|^4)|
          <=C eta_N ell^4,                          (11)

uniformly in N and sufficiently large H. This is a norm estimate before
the height limit, not merely pointwise series convergence.

For the arithmetic limit, b_(m,N) increases to tau(m)m^(-5/2).
Furthermore

    B(h,k)<=tau(hk)=tau(h)tau(k)<=tau(m)tau(n)

for the reduced coprime h=m/g,k=n/g. Consequently the summand in Psi_N
is bounded by tau(m)^2 tau(n)^2 (mn)^(-5/2). The elementary pairing
of divisors gives tau(m)<=2sqrt(m), so this majorant has sum at most
16 zeta(3/2)^2<infinity. Monotone convergence, or dominated convergence
on this positive double series, gives Psi_N->Psi<infinity, with Psi>=1.
No cancellation or conditional Euler sum is required for this limit.

Divide (11) by ell^4, apply (10) at each fixed N, then let N tend to
infinity. The height limsup and liminf coincide, yielding

    (1/H) integral_[H,2H] P|Z|^4
        =[q_P/zeta(2)] Psi ell^4+o(ell^4).          (12)

Finally L392 (2), based on audited L390/L391 and its separately proved
k=2 estimate, gives the complete square as c^4 times (12) plus
o(ell^4). This proves (1), including the full ordinary response-jet
errors, physical harmonics and envelope correction already controlled
there. The fixed positive beta is unconditional subject to the written
proofs; the separate audit below verifies this assembly and L392.

### Separate critical audit — 2026-10-11, step 53

This is a REPRODUCTION critical audit under the prior SPECIALIZE
assessment `drafts/literature/2026-10-11-complete-discriminant-second-moment-audit.md`.
Its target is the existing complete asymptotic, not a new moment theorem.
L390/L391 are audited inputs, and the present separate audit in L392
validates its remaining projection. Hughes–Young v2 Theorem 1.1,
(12)–(17), pp. 4–5, and its holomorphy remark were checked directly
against the specialization; the earlier assessment's proof-case coverage
is reused. No missing essential source hypothesis was found.

**Every six-term orientation.** With v=(a,b,-d,-e), the subsets in
(2) correspond to the source terms as follows:

| Selected I | Exponential prefactor after exp(-(a+b)) |
|---|---|
| {1,2} | 1 |
| {3,4} | exp(-(a+b+d+e)) |
| {2,3} | exp(-(a+d)) |
| {2,4} | exp(-(a+e)) |
| {1,3} | exp(-(b+d)) |
| {1,4} | exp(-(b+e)) |

For each row, the four pole arguments are precisely v_i-v_j with
i selected and j unselected. For example the {2,3} row has the
factors b-a, b+e, -d-a, -d+e, exactly the shifted source factor
A_(-d,b,-a,e)(0). Thus the orientations in (2), including all minus
signs, agree with the theorem. Every finite Euler factor tends to the
same B(h,k), since all its shift parameters tend to zero; the denominator
tends to zeta(2), not its square. Direct summation at a prime gives
1+e(p-1)/(p+1), including e=0. This factor is positive and at most e+1.

**Uniform complex differentiation.** On the four nested circles in
the proof, every u_i-u_j is separated from zero. All six transformed
pole arguments are such differences times i/ell, so their Laurent
expansions are uniform. Fixed h,k mean finitely many analytic local
factors; their variations are O_(h,k)(1/ell). On [H/2,4H], replacing
log(t/(2pi))/ell by 1 also costs O(1/ell). Thus the complete main-term
remainder on this product contour is O_(h,k)(ell^3). After integration
against a fixed smooth bracket it is O_(h,k,delta)(H ell^3).
The imported theorem error there is O_(h,k,delta)(H^(13/16)).

The original shifted moment is holomorphic in a neighborhood of the
closed scaled polydisc for large H: none of its zeta poles can occur
at these heights, and its integration interval is compact. The theorem's
complete main term is holomorphic by the cited cancellation remark.
For Bcal, multiplication by V gives an alternating entire numerator;
successive division by the linear factors of V removes all its apparent
diagonals. Alternatively this follows degree by degree from (6), with
locally convergent exponential series. Repeated Cauchy integration on
the fixed scaled circles therefore retains both error orders for every
required derivative, up to total order eight. There is no extra power
of ell from these scaled-variable Cauchy derivatives, nor any evaluation
of an individually singular summand at zero.

**Physical normalization and coefficient evidence.** Exact ordinary
jets give positive-orientation operators i^j(partial+1/2)^j and
negative-orientation operators (-i)^j(partial+1/2)^j. Multiplying their
generating functions yields (4): the exp(-(a+b)) in S combines with
the carrier to give exp(-i sum u_i/2), and the four denominator factors
of i multiply to one. Four factors of -1 and the two opposite pairs
of R cancel. The Omega' and L-versus-ell errors are controlled by
the triangular inversion of the exact jets and integral U^2=O(H ell^4),
so each quartic coefficient error O(1/ell) has integral O(H ell^3).
This works on the whole smoothing support by finitely many comparable
dyadic intervals. No shifted fourth-moment norm has been assumed.

The finite-algebra script was inspected and rerun. It constructs the
signed V/C_I factors, expands through exponential degree twelve,
checks exact division by multiplying back, and verifies low-degree
and odd cancellations and permutation symmetry. The complete nine-row
`moment_table` in its canonical certificate was inspected, as were the
full relevant Taylor coefficients. In particular the coefficients of
u^(0,2,2,2), u^(1,1,2,2), u^(2,2,2,2) are respectively
-61/29030400, 19/14515200, 17/170311680. Multiplication by the
multi-index factorials 8, 4, 16 yields the last higher-order entries
of (7). Degree-zero, degree-two and degree-four coefficients give the
remaining six entries in the printed table. Expanding P independently
as M^2+((z-x/4)^2+y^2)^2/8 gives all nine coefficients shown there.
The complete signed sum (8) is 263/1425600>0. The exact script reports
zero failures; its conclusion is finite algebra only. The analytic
arguments above are essential to interpreting these numbers as moments.

**All collisions, sharp brackets and the last limit.** Squaring the
finite Z_N series gives exactly b_(m,N), including repeated product
indices. Its modulus square sums every ordered pair (m,n), and reducing
each pair by its gcd gives the twist factor in (9). Repeated reduced
ratios are all summed; no diagonal or coprimality restriction is imposed
on the original m,n. Each of the nine signed monomials uses (5), but
sharp bracketing applies only after they are recombined into the
nonnegative P|Z_N|^4. The fixed-delta brackets meet the source hypotheses
with T_0 a fixed multiple of H. At fixed N and delta their errors vanish
after division by H ell^4. Sending delta to zero next proves (10) for
all real H, without a width-uniform theorem error or an estimate on
the absolute values of the signed endpoint monomials.

The norm bound (11) has a constant independent of N. Since reduced
h divides m and k divides n, B(h,k)<=tau(h)tau(k)<=tau(m)tau(n).
The positive double-series summands are bounded by
16(mn)^(-3/2), a summable majorant, while b_(m,N) increases to
tau(m)m^(-5/2). Thus Psi_N tends to the finite Psi>=1. More explicitly,
with A_H=(H ell^4)^(-1) integral P|Z|^4, (10)–(11) imply for each N

    limsup_(H->infinity) |A_H-(q_P/zeta(2))Psi|
      <= C eta_N + (q_P/zeta(2))|Psi_N-Psi|.

The right side tends to zero as N tends to infinity. This displays the
required order: fixed head and width, height limit, width limit, then
head limit. The O_N constants in the projection estimates never need
to be uniform in N. Finally the audited L392 reduction multiplies this
limit by c^4 and adds o(ell^4), including every physical projection,
response-derivative error and envelope correction.

The complete asymptotic and its positive coefficient pass unchanged.
No new dependency, new moment theorem, optimal sign-set estimate,
eventual discriminant sign or RH consequence is established by this
audit. The global positivity and actual common-zero gaps remain open.

## Mathlib

Full matching Mathlib coverage for Hughes–Young's twisted shifted fourth
moment, these Hardy moments and the complete physical discriminant
asymptotic has not been checked. Supporting finite polynomial arithmetic,
Cauchy differentiation, nonnegative bracketing and dominated-convergence
facts would not themselves formalize the imported analytic theorem.
No Lean verification, library absence, originality or RH resolution is claimed.
