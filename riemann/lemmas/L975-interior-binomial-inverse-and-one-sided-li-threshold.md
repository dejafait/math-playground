# Lemma 975: the interior binomial inverse and a sufficient one-sided threshold

## Hypotheses

Use the actual completed xi of L018, with its zero localization from
L026, including all multiplicities. Let lambda_n denote the ordinary,
undivided zeta Li coefficients in L968. No RH, simple-zero hypothesis,
coefficient sign, or radius-two logarithm is assumed.

On U={z: |z+1|<3/2}, define the analytic logarithm

    F(z)=log xi(1/(1-z)),          F(0)=-log 2,
    F(z)=sum_(m>=0) b_m (z+1)^m.                         (1)

Existence, uniqueness and agreement of this branch with the ordinary
Li germ are verified below; (1) is not an assumed zero-free domain.

For the conditional conclusion only, consider the additional hypothesis

    for every delta in (0,1) there is C_delta>0 such that
    b_m >= -C_delta (2-delta)^(-m) for every integer m>=1. (H)

An eventual version permits a finite exceptional prefix depending on
delta, without any assumed signs in that prefix. Neither version is
established for the actual coefficients here.

## Conclusion

The logarithm in (1) exists, all b_m are real, and for every integer
n>=1 the complete series is absolutely convergent and satisfies

    lambda_n/n = sum_(m>=n) binom(m,n) b_m.               (2)

Under (H), or its eventual version, for every epsilon>0 there is a
finite K_epsilon>0 such that simultaneously for all n>=1,

    lambda_n >= -K_epsilon exp(epsilon*n).                (3)

Consequently (H) would imply RH by the criterion imported in L968.
This proves a sufficient conditional transfer, not (H), its necessity,
its compatibility with actual zero singularities, or RH. The inverse
is known; the contribution here is its domain/branch audit and explicit
one-sided amplification specialization. Classification: REPRODUCTION.
Written in step207, 10 November 2026; no independent later audit claimed.

## Proof

### Known formula and the domain that is actually used

The inverse (2) is stated in Y.-H. He, V. Jejjala and D. Minic,
*Eigenvalue Density, Li's Positivity, and the Critical Strip*,
[arXiv:0903.4321v2, 22 April 2009, (3.4), printed p.8](https://arxiv.org/pdf/0903.4321v2#page=8).
Its k_n denotes ordinary lambda_n. We do not import the preceding
radius-two assertion or the formal positivity manipulations in their
Section 3.3, printed p.14. Local verification is necessary because
the stated radius is not a justified domain for our logarithm.

The coefficient convention and the ordinary Li germ are those of
M. W. Coffey, *On certain sums over the nontrivial zeta zeros*,
[arXiv:0912.2390v1, 12 December 2009, (1.1)-(1.3), printed pp.2-3](https://arxiv.org/pdf/0912.2390v1#page=2):

    F(z)=-log 2+sum_(n>=1) (lambda_n/n) z^n               (4)

near z=0. Only this local generating identity is imported; no
conditional asymptotic, forward infinite transform, or larger
convergence domain is used. Its undivided normalization agrees with
the ordinary zeta coefficients in L968. Multiplication of xi by a
nonzero constant changes only the constant logarithm coefficient.

Set w=z+1. For |w|<3/2,

    s=1/(2-w),       |2-w|>1/2,       |s|<2.             (5)

L018 makes xi entire. If xi(s)=0, L018 identifies the corresponding
Xi zero alpha=(s-1/2)/i; L026 gives |Re alpha|>4, hence
|Im s|>4. This contradicts (5). Thus g(z)=xi(1/(1-z))
is analytic and nonvanishing throughout U. The pole z=1 of the
inner map is outside U, since |1+1|=2.

The disk U is simply connected and contains z=0. The standard
holomorphic logarithm theorem therefore gives a unique analytic
F on U with exp(F)=g and F(0)=-log 2, since L018 gives
g(0)=xi(1)=1/2. Equivalently its branch is fixed by integrating
g'/g from 0 inside this disk; path independence is Cauchy's integral
theorem. Uniqueness makes it agree with the local logarithm in (4).
L018 gives g(conj z)=conj(g(z)). The function conj(F(conj z))
is an analytic logarithm with the same value at 0, so equals F.
In particular all its Taylor coefficients b_m at the real center -1
are real. No loop around a zero or separate logarithm branch is used.

### Complete differentiated sum

Import the analytic Taylor theorem and interior differentiation of
power series, [NIST DLMF 1.10.1](https://dlmf.nist.gov/1.10.E1),
[1.9(vi), (1.9.48), (1.9.63)](https://dlmf.nist.gov/1.9.vi),
version 1.2.8. These require analyticity in the relevant disk and
assert absolute uniform convergence on closed strict subdisks and
termwise derivatives inside the radius. The domain check above
verifies these hypotheses, with the evaluation point z=0 strictly
inside U, at distance 1 from its center.

Explicitly, for any fixed r with 1<r<3/2 let

    M_r=max_(|w|=r) |F(w-1)| < infinity.

The Cauchy coefficient estimate gives |b_m|<=M_r r^(-m).
For every fixed n>=1, the binomial series yields

    sum_(m>=n) binom(m,n) |b_m|
       <= M_r sum_(m>=n) binom(m,n) r^(-m)
        = M_r r/(r-1)^(n+1) < infinity.                 (6)

Here the elementary binomial generating identity is

    sum_(m>=n) binom(m,n) t^m=t^n/(1-t)^(n+1), |t|<1;

it is [DLMF 4.6.7](https://dlmf.nist.gov/4.6.E7) with exponent
-(n+1), followed by multiplication by t^n. We use t=1/r,
strictly less than 1, with no boundary substitution.

Interior termwise differentiation at z=0 now gives

    F^(n)(0)/n! = sum_(m>=n) binom(m,n) b_m,

since (z+1)^(m-n)=1 there. Comparing with the local identity (4)
proves (2), including absolute convergence of its entire tail.
All assertions are for each finite n; no uniform n-limit or zero-sum
interchange is needed. The fixed-radius absolute estimate (6) alone
does not imply (3) for every epsilon.

### Exact one-sided amplification and all quantifiers

Fix delta in (0,1), put a=2-delta>1, and first assume the all-index
version (H). Positivity of binom(m,n), absolute convergence in (6),
and convergence of the comparison series imply, by passing to the
limit in finite partial inequalities,

    lambda_n/n >= -C_delta sum_(m>=n) binom(m,n) a^(-m)
                = -C_delta a/(a-1)^(n+1),
    lambda_n >= -C_delta [a/(a-1)] n (a-1)^(-n)          (7)

for every n>=1. This compares complete sums. The hypothetical
one-sided bound is not used to enlarge the analytic Taylor disk:
a may exceed 3/2, and (7) requires only a>1 and the already proved
convergence at w=1. In particular it assumes no radius-two domain.

For an arbitrary epsilon>0 choose

    delta=1-exp(-epsilon/2) in (0,1).

Then a-1=exp(-epsilon/2). The elementary maximum of
x exp(-epsilon*x/2) for x>=0 is 2/(e*epsilon). Hence

    K_epsilon=C_delta [a/(a-1)] 2/(e*epsilon)>0         (8)

is finite and (7) implies (3) at every integer n>=1. Constants
may depend on epsilon, through delta, but never on n. For a single
fixed delta, (7) has exponential rate -log(1-delta)>0 and does not
establish all of the required rates. The factor n is retained and
paid in (8), rather than silently dropped.

If (H) holds only for m>=M_delta, replace C_delta by the finite

    C'_delta=max({1,C_delta} union
                 {max(0,-b_m)*a^m: 1<=m<M_delta}).       (9)

This pays every exceptional coefficient without a sign assumption
and gives (H) for all m>=1. Repeating (7)-(8) proves (3), including
all small n. Nothing about b_0 is needed because n>=1.

Finally import the every-epsilon one-sided criterion with its zeta
specialization already audited in L968: J. C. Lagarias,
*Li coefficients for automorphic L-functions*, Ann. Inst. Fourier
57(5) (2007), 1689-1740,
[Theorem 2.4(2), (2.21), pp.1702-1703](https://www.numdam.org/article/AIF_2007__57_5_1689_0.pdf#page=15).
Its trivial GL(1) case uses the entire completion 2*xi; that constant
does not affect ordinary Li coefficients, as checked in L968.
The real lambda_n here and the all-n, every-epsilon bound (3) meet
exactly that criterion. Thus (H) implies RH, conditionally.

### Limits of this result

No actual b_m lower bound has been proved or imported. In particular
the hypothesis is only sufficient; we do not claim that RH implies
it or that it is compatible with the actual logarithmic singularities.
The actual all-degree positivity gap L030-L032/C032a and L966's
integrated sign inequality remain unresolved. L974's polynomial
regularization budget supplies no estimate for (H). No candidate
proof or disproof of RH results. Prior source and route stops remain.

## Mathlib

Full matching coverage of this actual-xi inverse with the one-sided
threshold has not been checked and is unknown. No Mathlib theorem
is imported. Generic Taylor or binomial support alone would not
establish the actual zero-free domain, branch or Li normalization.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
