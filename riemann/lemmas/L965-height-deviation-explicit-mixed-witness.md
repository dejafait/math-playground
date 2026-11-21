# Lemma 965: height and deviation give an explicit mixed-witness degree

## Hypotheses

Use the actual completed zeta function of L018 and the paired Xi zeros
alpha_j of L024, with beta_j=alpha_j^(-2) and all multiplicities retained.
Let T>=1 and 0<delta<1/2 be finite real numbers. Suppose there is an
actual nontrivial zeta zero rho_0 satisfying

    |Im rho_0| <= T,       |Re rho_0-1/2| >= delta.             (1)

This is a hypothetical input; no such zero is asserted to exist.
The mixed form is L030's Q(q)=sum_j beta_j^2 q(beta_j)^2, with real
polynomial coefficients and algebraic squares.

## Conclusion

The following constants depend only on T and delta. All logarithms are
natural, and all ceilings are ordinary integer ceilings:

    R = sqrt(1+2delta/(T^2+1/4)),    r = sqrt(R),    a = log(r),
    B = ceil(2((R-1)^(-1)+1/4)),
    N = ceil(max{1, 40B/a, 1440/a^3}),
    n_* = 5BN,
    U = 3^(n_*),                   b = 8 sqrt(2) U^2,
    D(T,delta) = ceil(
        log(b(8U^2+1)(2b+1)/2) / log(1+1/(8U^2)) ).          (2)

Here R>r>1, a>0, and B,N,n_*,D are positive finite integers.
There is an integer n with N<=n<=n_* and N dividing n for which

    lambda_n <= -R^n/40 <= -1.                               (3)

There is consequently a real polynomial q with

    deg q <= D(T,delta),             Q(q) < -3/4.             (4)

Equivalently, the actual H_D of L030 has a negative quadratic direction.
No separation, simplicity, supplied finite head, zero-count asymptotic,
or uncertified Li coefficient is an additional hypothesis. The bound
is deliberately very large; no practical computation is claimed.

This conditional result was written in step162 and passed an independent
conceptual audit in step163 on 10 November 2026, with its hypotheses,
statement and constants unchanged. It is a finite witness implication,
not a proof or disproof of RH. Actual mixed signs, an actual off-line
zero and all-height exclusion remain open.

## Proof

### Imported power-sum result and specialization scope

Use Neea Palojarvi, *Explicit zero-free regions and a tau-Li-type
criterion*, [arXiv:1807.01506v2](https://arxiv.org/pdf/1807.01506v2#page=6),
20 January 2020, Lemma 2.2, printed p.6: for M>=1 complex numbers
z_1,...,z_M with max_j |z_j|=1, there is an integer 1<=k<=5M with

    Re sum_{j=1}^M z_j^k >= 1/20.                            (5)

This is the Turan power-sum theorem cited there to *On a New Method of
Analysis and its Applications*, Chapter 5, Theorem 11. Its statement
was checked in the versioned primary article; the book proof was not
read and is not reproved here. Repeated values are allowed by (5).

We do not apply Palojarvi's Theorem 3.1 or its printed count constants.
The specialization below cuts by Mobius modulus and uses an elementary
actual-Xi mass bound, to obtain a margin usable in L964. This supplies
quantitative inputs beyond a bare sign window. The existing literature
assessment found no matching L030 degree theorem; that is not a claim
of originality or of absence from the wider literature.

### An explicit actual-Xi mass bound

Put M_0=Xi(0) and use the positive kernel and moments of L019-L021.
L020 and L026 imply

    M_0 = 1/2-J(0)/2 > 1/2-1/144 = 71/144.                  (6)

L018 gives Xi(i/2)=xi(0)=1/2. For u>=0 the elementary cosine-hyperbolic
series gives cosh(u/2)-1>=u^2/8. Positivity of K and L020-L021 therefore
give, with all integrals convergent,

    M_2 <= 8 integral_0^infinity K(u)(cosh(u/2)-1) du
        = 8(1/2-M_0) < 1/18.

By L025, S_1=sum_j beta_j=M_2/(2M_0), so S_1<4/71. Write
alpha=x+iy. L026 says |x|>4 and |y|<1/2, whence

    Re(beta)/|beta| = (x^2-y^2)/(x^2+y^2) >= 63/65.

L024 licenses taking real parts in this absolutely convergent series.
Thus the complete paired mass A_0 satisfies

    A_0 := sum_j |beta_j| <= (65/63)S_1
         < 260/4473 < 1.                                    (7)

For every zeta zero rho=sigma+i gamma, L018 and L026 give
0<sigma<1 and |gamma|>4, and its Xi coordinate is
alpha=gamma+i(1/2-sigma). There are two Xi zeros per sign pair, with
the same modulus and multiplicity. Also

    1/gamma^2
      <= (65/64)/(gamma^2+(1/2-sigma)^2).

Summing over ALL zeta zeros, including both signs and all multiplicities,
gives the useful companion bound

    S_gamma := sum_rho 1/(Im rho)^2
             <= (65/32) A_0 < 3.                            (8)

These bounds do not assume RH or sign any higher mixed form.

### The real Li sum and a bound for every omitted zero

Set w(rho)=rho/(rho-1) and u=w-1=1/(rho-1). No denominator vanishes.
For rho=sigma+i gamma,

    |Re u| <= 1/gamma^2,     |u|^2 <= 1/gamma^2,
    |w|^2 = 1+(2sigma-1)/((1-sigma)^2+gamma^2)
           <= 1+1/gamma^2 < 17/16.                          (9)

For any real v>=1 and any zero with |w|<=v, Taylor's formula along
the straight segment from 1 to w gives, for integers n>=2,

    w^n = 1+nu+n(n-1)u^2
                    integral_0^1 (1-t)(1+tu)^(n-2) dt.

This identity is simply twice-integrated differentiation of a polynomial;
it has no branch or limiting-series requirement. Convexity of the disk
gives |1+tu|<=1-t+t|w|<=v. Taking absolute values only after taking the
real part of the linear term yields

    |Re(1-w^n)|
      <= [n+n(n-1)v^(n-2)/2]/gamma^2
      <= n^2 v^n/gamma^2.                                   (10)

For n=1 the same bound follows directly from (9). Taking
v=sqrt(17/16) in (10) and using (8) proves absolute convergence of
the REAL series sum_rho Re(1-w(rho)^n), for each fixed n.
It does not assert absolute convergence of the complex linear Li sum.

This real series equals the ordinary real Li coefficient lambda_n of
L964. To see the normalization without rearranging a conditionally
convergent complex sum, pair rho and 1-rho, for which w becomes w^(-1).
For the corresponding Xi sign pair, L964's exact algebraic identity is

    2-w^n-w^(-n) = beta_j a_n(beta_j)^2,
    lambda_n = sum_j beta_j a_n(beta_j)^2.                    (11)

The inverse convention for w does not change the left side. The latter
series is absolute by L964; the real series is absolute by (10).
Grouping its real terms in the two-element sign pairs and taking real
parts of (11) therefore proves

    lambda_n = sum_rho Re(1-w(rho)^n).                        (12)

L964 imports the underlying normalization from J. C. Lagarias,
*Li coefficients for automorphic L-functions*, Ann. Inst. Fourier 57(5)
(2007), [Theorem 3.1, equations (3.1)-(3.6), pp.1704-1706](https://www.numdam.org/article/AIF_2007__57_5_1689_0.pdf#page=17).
Its already-audited zeta specialization is reused here. No Li positivity
criterion, Weil positivity or unknown sign is used.

### A finite head selected by modulus, with no node separation

Reflection in L018 lets us replace the supplied zero in (1) by one with
sigma>=1/2+delta, preserving the bound on |gamma|. For that zero,

    |w|^2 = 1+(2sigma-1)/((1-sigma)^2+gamma^2)
           >= 1+2delta/(T^2+1/4) = R^2.                     (13)

Let E be the multiset of ALL zeros with |w(rho)|>r, counting every
multiplicity. It contains the zero of (13), because R>r. If rho is in E,
then |w|^2>r^2=R, so (9) implies

    gamma^2 < (R-1)^(-1) =: H^2,
    |alpha|^2 < H^2+1/4.

Each copy in E consequently contributes more than (H^2+1/4)^(-1)
to the reciprocal-square mass over ALL Xi zeros, which is 2A_0<2
by (7). This proves finiteness and the multiplicity-sensitive count

    1 <= M := |E| < 2(H^2+1/4) <= B.                        (14)

Zeros with |w|=r are assigned to the complement. In particular there is
no boundary zero omitted from both parts. The head is a theoretical
set, not supplied data; its size is bounded without knowing its nodes.

Let W=max_{rho in E}|w(rho)|, which exists and satisfies W>=R. For
each head copy put z_rho=(w(rho)/W)^N. These are exactly M complex
numbers with maximal modulus one. Apply (5) to obtain 1<=k<=5M
and put n=Nk. Then N<=n<=5MN<=n_* and

    Re sum_{rho in E} w(rho)^n
       = W^n Re sum_{rho in E} z_rho^k
       >= W^n/20 >= R^n/20.                                (15)

Repeated zeros repeat the corresponding number in (5). No simplicity,
angular separation or interpolation denominator enters this use.

On the entire complement of E we have |w|<=r. Summing (10), with
v=r, using (8), and then (12) and (15), gives the complete estimate

    lambda_n <= M - R^n/20 + 3n^2 r^n
              <= B - R^n/20 + 3n^2 r^n.                    (16)

In particular the complement includes all left-half zeros, all critical
zeros, all near-threshold zeros and the infinite high-ordinate tail.
No presumed nonnegative or negligible part has been discarded.

### Explicit payment of both errors

Since r=e^a and R=e^(2a), divide (16) by R^n. For any n>=N,
the nonnegative exponential series gives e^(2an)>=2an and
e^(an)>=(an)^3/6. The definition of N therefore ensures

    B e^(-2an) <= B/(2an) <= 1/80,
    3n^2 e^(-an) <= 18/(a^3 n) <= 1/80.                    (17)

It follows that lambda_n/R^n<=-1/20+1/80+1/80=-1/40.
Moreover R^n>=2an>=80B, so R^n/40>=2B>=1. This proves (3),
including a fixed usable negative margin. All inequalities apply to
the index selected in (15); no assertion about every Li index is made.

### Uniform composition with L964

By (7) and (3), L964 applies to this n with epsilon=A=1. To express
one degree bound independent of the unknown selected n, write m=3^n.
For these supplied values, the minima in L964's constants simplify to

    eta = 1/(64m^2),       B_L = 8 sqrt(2)m^2,
    theta = 8m^2/(8m^2+1), tau = 2/(2B_L+1),
    D_n = ceil(
      log(B_L(8m^2+1)(2B_L+1)/2) / log(1+1/(8m^2)) ).      (18)

Indeed m>=3 makes eta<1/16 and tau<1, so both stated branches of
the minima are valid. As m increases on [3,infinity), the positive
numerator in (18) increases and the positive denominator decreases.
Their quotient and its ceiling are consequently nondecreasing.
Since n<=n_*, m<=U, (18) gives D_n<=D(T,delta) as defined in (2).
L964 supplies a real polynomial of degree at most D_n with Q(q)<-3/4.
Padding its coefficient vector with zeros through index D preserves Q
and proves (4) and the H_D conclusion by L030.

The polynomial can be selected from the finite family of L964 recipes
for n=N,2N,...,5BN, all using epsilon=A=1. Under (1) at least one
member works. The argument does not identify an actually negative
member or claim a computational certificate for a hypothetical zero.

### Qualifications and comparison

The gain over the local L032/L895 bounds is removal of the supplied
head and its conditioning factors from the degree bound. Those results
are comparisons, not mathematical inputs. The mass estimate, modulus
cut, real-tail estimate and degree composition are the specialization
proved here; the power-sum theorem and L964 are imported inputs.
No claim of novelty beyond the assessed sources is made.

For fixed T and delta this gives a sufficient finite set of mixed signs
to exclude zeros in the stated region, conditionally on establishing
those signs. The degree grows without bound as T grows or delta shrinks.
No one finite sign check yields RH. No signs have been established here,
and (1) is not a rigorous counterexample certificate. The unresolved
Palojarvi printed-constant comparisons remain unresolved but are unused.

### Independent conceptual audit, step163

The audit reread the complete proofs of L018-L021, L024-L026, L030
and audited L964. It checked Palojarvi v2 Lemma 2.2 on printed p.6
against (5): the hypothesis is a finite list with maximum modulus one,
and the conclusion concerns the real part at an integer exponent at
most five times the list length. No distinctness condition occurs.
Only this cited theorem is imported from that paper; its zero-count
assumptions, Theorems 2.3/3.1 and disputed printed constants are unused.
L964's already-audited Lagarias identity is reused with its stated
absolute-convergence and normalization qualifications.

For (6)-(8), L020 at zero is exactly M_0=1/2-J(0)/2, while L018
at z=i/2 gives Xi(i/2)=xi(0)=1/2. Both integrals in their difference
converge by L019-L020, and positivity of K licenses the cosh inequality.
The arithmetic is

    M_2 < 8/144=1/18,
    M_2/(2M_0) < (1/18)/(71/72)=4/71,
    (65/63)(4/71)=260/4473<1.

Writing t=y^2/x^2 gives 0<=t<1/64, so
Re(beta)/|beta|=(1-t)/(1+t)>63/65. Since L024 supplies absolute
summability before this comparison, summing it neither assumes a sign
for a mixed form nor rearranges a divergent series. The comparison
(x^2+y^2)/x^2<65/64 and the exactly two members of each sign pair
give S_gamma<=(65/64)*2A_0. Critical-line zeros also have two distinct
members since |x|>4; multiplicities enter both sums identically.

For (10)-(12), the polynomial Taylor remainder holds for every integer
n>=2 on the complex straight segment. For v>=1,

    n+n(n-1)v^(n-2)/2
      <= [n+n(n-1)/2]v^n <= n^2 v^n.

The separate n=1 estimate is valid as stated. The global choice
v=sqrt(17/16) is independent of rho, so (8) proves absolute
convergence of the real series for each fixed n. The pairing in (11)
is rho with 1-rho, rather than necessarily rho with conjugate(rho).
Their sum is Re[beta*a_n(beta)^2] after real parts are taken.
Summing these real parts and using L964's real, absolute paired sum
gives exactly lambda_n, with no factor two. Neither complex linear
Li-series absolute convergence nor a limit uniform in n is required.

For (13)-(16), reflection preserves |gamma| and gives
1/2+delta<=sigma<1, hence (1-sigma)^2<=1/4. The closed input
inequalities in (1) imply |w|>=R, strictly larger than r. Each
head copy has reciprocal-square mass greater than
1/(H^2+1/4). Applying the mass bound first to any finite selection
of copies proves that the full head cannot be infinite, and then
proves (14). In particular this argument counts multiplicities
without assuming beforehand that the selected head is finite.
The maximum W is now attained, and (w/W)^N has maximal modulus
exactly one. Its kth power scales by W^(-Nk), a positive real
number, so the cited real-part inequality gives (15) with n=Nk.

Every zero outside this head satisfies |w|<=r, including equality,
and the bound (10) is an absolute bound on its real contribution.
Summing over this entire complement costs less than 3n^2 r^n.
The head contributes exactly M minus its real power sum. This
checks the sign, constant term, finite head, intermediate zeros and
infinite tail in (16), without an assumption about their individual
Li signs. If T<=4, L026 already makes (1) impossible; the formula
still defines finite positive constants and the implication is vacuous.

For (17), n>=N implies an>=40B and a^3 n>=1440. The exponential
lower bounds therefore pay at most 1/80 for each error, and the
remaining coefficient is -1/40. Also R^n/40>=2B>=2, so the
advertised margin at least one is conservative. These checks apply
to the selected exponent; they do not assert negativity for all n>=N.

Finally, with m=3^n>=3, L964 gives eta=1/(64m^2),
B_L=8 sqrt(2)m^2 and tau=2/(2B_L+1)<1. Substitution into its
degree formula gives exactly (18). Its numerator is positive and
increasing; its denominator is positive and decreasing. Thus the
quotient, and then its ceiling, are nondecreasing. This remains true
when a ceiling argument is an integer. Using A=epsilon=1 is licensed
by (7) and (3), and L964's strict upper error yields Q(q)<-3/4.
L030's H_D has indices 0 through D, hence dimension D+1; padding
the degree-D_n polynomial introduces no index shift or changed form.

No defect or needed change to the claimed bound was found. This is
local validation of the conditional result, not new sign evidence or
certified originality. All direct local inputs in the existing L965
DAG row are used; L032/L895 remain comparisons, and no additional
lemma input, numerical certificate or zero-count theorem was introduced.

## Mathlib

Coverage of the full T,delta-only Li-to-mixed-witness degree bound and
of the precise Turan real-power-sum constant has not been checked;
availability is unknown, not asserted absent. No Mathlib result is
imported. Supporting finite-sum, Taylor or order facts would not alone
verify the actual-Xi mass, Li normalization or complete-tail argument.
