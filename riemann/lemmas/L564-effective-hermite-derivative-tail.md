# Lemma 564: explicit actual-Xi Hermite tails through two derivatives

## Hypotheses

Let Xi(t)=xi(1/2+it) have the normalization in L018–L020.
Use physicists' Hermite polynomials H_m and Romik's even kernel

    Phi_R(u)=2 sum_(k>=1) [2pi^2 k^4 exp(9u/2)
                           -3pi k^2 exp(5u/2)]
                          exp(-pi k^2 exp(2u)).

On u>=0 this is K(u)/2 in L019. Define

    b_m=1/(2^m m!) integral_R u^m exp(-u^2/4) Phi_R(u) du,
    P_N(t)=sum_(n=0)^N (-1)^n b_(2n) H_(2n)(t),

where N is a nonnegative integer. Import the coefficient formula and
the locally uniformly convergent expansion Xi=lim_N P_N from Dan
Romik, *Orthogonal polynomial expansions for the Riemann xi function*,
[arXiv:1902.06330v3](https://arxiv.org/html/1902.06330v3#S2),
(1.1), (1.8), (1.11), (2.1), Theorem 2.1, (2.2)–(2.3).
These are source inputs, not new expansion claims. The full-line
Fourier integral of Phi_R equals L020's cosine integral of K, since
Phi_R is even and K=2Phi_R on the positive half-line. Thus neither a
height rescaling nor an additional Gaussian factor is present.

The other imported standard inputs, with real x and integer m>=0,
are [NIST DLMF 18.14.9](https://dlmf.nist.gov/18.14.E9),

    |H_m(x)|<=exp(x^2/2) sqrt(2^m m!),                 (1)

and [NIST DLMF 18.9.25](https://dlmf.nist.gov/18.9.E25),

    H_m'=2m H_(m-1), m>=1;  H_0'=0.                 (2)

No bound for complex arguments is taken from (1).

## Conclusion

For every real T>=1, let N=ceil(16(T+1)^2). For j=0,1,2,

    sup_(T<=t<=2T) |Xi^(j)(t)-P_N^(j)(t)|
        <=exp(-8T)<=exp(-2pi T).                    (3)

In fact, for every integer N>=1 and every real t,

    |Xi^(j)(t)-P_N^(j)(t)|
        <=5000(4N+5) exp(t^2/2) 5^(-N)
        <=80000 N exp(t^2/2) 5^(-N), j=0,1,2.      (4)

The polynomial degree is 2N; the constant 16 refers to the cutoff
index n, as in the approved target. These are absolute errors, valid
also at zeros and multiple zeros. No sign of P_N'^2-P_N P_N'', no
relative error near zeros, and no positivity of any Xi form follows.

## Proof

### A numerical envelope for the complete kernel

For u>=0 put x=exp(2u)>=1. Each theta summand of Phi_R is positive:
its bracket is pi k^2 exp(5u/2)(2pi k^2 x-3)>0.
Dropping its negative part therefore yields

    0<Phi_R(u)<=4pi^2 exp(9u/2)
                        sum_(k>=1) k^4 exp(-pi k^2 x).

Since k^2 x>=k^2 and k^2 x>=x, we have
k^2 x>=(k^2+x)/2. Also pi>3 and pi k^2/2>=k. Hence

    sum_(k>=1) k^4 exp(-pi k^2 x)
        <=exp(-3x/2) sum_(k>=1) k^4 exp(-k)
        <=150 exp(-3x/2).                            (5)

Here exp(1)>2 and sum_(k>=1) k^4/2^k=150. To verify the latter
constant, write k^4=(k)_4+6(k)_3+7(k)_2+(k)_1, where
(k)_r=k(k-1)...(k-r+1). Differentiating the geometric series r
times inside its radius of convergence gives
sum_(k>=1)(k)_r/2^k=2r! for r>=1. Thus the sum is
48+72+28+2=150. This calculation controls all theta summands;
there is no first-summand approximation or omitted theta tail.

The elementary Taylor inequality exp(2u)>=1+2u+2u^2 gives

    u^2+(9/2)u-(3/2)exp(2u)
        <=-2u^2+(3/2)u-3/2
        =-2(u-3/8)^2-39/32<0.

Using pi<4 in (5), we obtain Phi_R(u)<=9600 exp(-u^2), and hence

    0<=Phi_R(u)<=10000 exp(-u^2), u in R.            (6)

The negative half-line uses the source's evenness, not an extension
of the positive-u estimate by a change to the theta summation.

### Complete coefficient bound

Put a=5/4. The defining coefficient integral and (6) give, for n>=0,

    b_(2n) sqrt(2^(2n)(2n)!)
      <=10000/[2^n sqrt((2n)!)]
                       integral_R u^(2n) exp(-a u^2) du.

The elementary Gaussian moment is

    integral_R u^(2n) exp(-a u^2) du
        =sqrt(pi/a) (2n)!/[(4a)^n n!].

For completeness, its n=0 case is the classical Gaussian integral;
integration by parts gives the recurrence I_n=(2n-1)I_(n-1)/(2a),
with vanishing boundary terms because polynomial times Gaussian tends
to zero. This proves the displayed formula for every n, including
the initial index, without any asymptotic estimate.
Consequently

    b_(2n) sqrt(2^(2n)(2n)!)
      <=10000 sqrt(pi/a) sqrt((2n)!)/[(8a)^n n!]
      <=20000 (4a)^(-n)=20000*5^(-n).              (7)

Indeed sqrt((2n)!)/n!=sqrt(binomial(2n,n))<=2^n, since the
binomial coefficient is one nonnegative term of the sum 2^(2n).
Also sqrt(pi/a)<2, using a=5/4 and pi<4. No unknown constants,
large-index onset or coefficient-saddle approximation enters (7).

### Derivative majorants and legitimate limits

For m>=2, (1)–(2) imply

    |H_m^(j)(t)|<=exp(t^2/2) sqrt(2^m m!) M_(m,j),
    M_(m,0)=1,
    M_(m,1)=sqrt(2m),
    M_(m,2)=2sqrt(m(m-1)).                          (8)

In particular, M_(2n,j)<=4n for n>=1 and j=0,1,2. The m=0
polynomial is 1 and has zero first and second derivatives; it is
irrelevant to a tail with N>=1. Combining (7)–(8), for n>=1,

    |b_(2n) H_(2n)^(j)(t)|
        <=80000 n exp(t^2/2) 5^(-n), j=0,1,2.     (9)

On every bounded real interval |t|<=R, the right side is bounded
by 80000 exp(R^2/2) n 5^(-n), a summable sequence. Thus the
polynomial series and its first two termwise derivatives converge
uniformly there. The standard termwise differentiation theorem for
uniformly convergent derivative series applies successively: the
fundamental theorem of calculus applied to the partial sums, followed
by uniform convergence under the finite-interval integral, first
identifies the derivative of their limit and then its second
derivative. The undifferentiated limit is Xi by Romik's cited theorem.
This proves that both derivative limits equal the actual Xi
derivatives. The argument works on any bounded interval, so there is
no fixed-compact estimate silently asserted uniform in T.

Sum (9) from n=N+1 to infinity. The differentiated geometric series
gives, exactly,

    sum_(n>N) n 5^(-n)=5^(-N)(4N+5)/16.

This proves the first inequality in (4). For N>=1,
(4N+5)/16<=N, proving its second inequality.

### Cutoff and the required threshold at every height

For T>=1 and |t|<=2T, the second bound in (4) is at most

    80000 N exp(2T^2) 5^(-N).

For every integer N>=1, N<=2^N (by induction). Also
80000<2^17<exp(17), and log(5/2)>1/2: exp(1)<3<4 implies
exp(1/2)<2<5/2. These elementary exponential comparisons give

    80000 N exp(2T^2) 5^(-N)
        <=exp(17+2T^2-N/2).

With N=ceil(16(T+1)^2), the exponent is at most

    17+2T^2-8(T+1)^2
        =9-6T^2-16T<=-8T,

because 9-6T^2-8T<=-5 for T>=1. Finally pi<4 implies
exp(-8T)<=exp(-2pi T). This proves (3), including T=1 and
all cutoff and interval endpoints. The crude constant 16 is not
claimed optimal.

This specializes the known coefficient integral and Hermite bound;
it does not reprove Romik's expansion or certify its manuscript
independently. Its purpose is the explicit all-T derivative error
missing from the inspected source statements. A later discriminant
comparison still needs a signed truncation margin or an alternative
zero-compatible signed argument; higher positivity remains separate.

### Independent application audit, 2026-10-31

The complete argument above passes the approved quantitative audit.
L019's coefficients are exactly twice those of Phi_R on u>=0;
source evenness and L020 then identify the same Xi with no height or
Gaussian rescaling. Evenness on the negative half-line is an imported
source property, not an inequality extrapolated from the theta series.

All theta indices are covered by 2k^2 x>=k^2+x for k,x>=1.
The fourth-moment calculation gives 2(24+36+14+1)=150;
the completed square has maximum -39/32. Thus the constants 9600
and 10000 in (6) are valid for the whole kernel. The coefficient
normalization is 2^n sqrt((2n)!), so insertion of the full Gaussian
moment gives (8a)^n before the binomial bound, then (4a)^n=5^n.
This also includes n=0; positivity makes the coefficient bounds
absolute bounds, without any cancellation assumption.

The derivative ratios in (8) are respectively sqrt(2m) and
2sqrt(m(m-1)); for m=2n>=2 they are <=4n. H_0 is handled
separately. The common majorant on each finite interval is summable
for j=0,1,2. Applying the fundamental theorem of calculus first
to P_N and then to P_N' identifies both limits with the actual
derivatives, including at zeros. No derivative of a coefficient
asymptotic, infinite-interval interchange or complex Hermite bound
is used. The sum starts at N+1, with exact value
5^(-N)(4N+5)/16; its two constants in (4) therefore agree.

Finally N>=16(T+1)^2 and the elementary comparisons in the proof
give exponent at most -8T-5 for T>=1, so the asserted weaker
exponent -8T has slack even at T=1. Increasing N at a ceiling
endpoint preserves this upper bound. The real interval endpoints
t=T,2T and all three derivative orders are included. No repair or
change of cutoff is needed. This audits the specialization, not the
proof of Romik's imported theorem or any signed truncation margin.

## Mathlib

Coverage of this full numerical specialization, Romik's expansion,
the Hermite bound and supporting derivative/Gaussian-moment facts
has not been checked. Availability is unknown; absence and formal
verification are not claimed. Standard source inputs are cited above.
General reference: https://leanprover-community.github.io/mathlib4_docs/
